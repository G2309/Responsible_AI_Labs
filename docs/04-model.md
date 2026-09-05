# 04 — Modelo

## Objetivo

Definir el clasificador de imágenes que se va a explicar con SHAP: origen, arquitectura,
framework, preprocesamiento y salidas. Este documento es la base para `05-shap.md`
(qué explicador usar) y para la sección de Método del `paper.tex`. Los datos que consume
están definidos en `06-data.md`.

## Modelo elegido

* **Nombre**: DeiT (Data-efficient Image Transformer) — Hugging Face
* **Documentación**: <https://huggingface.co/docs/transformers/v5.15.1/en/model_doc/deit#deit>
* **Checkpoint base**: `facebook/deit-small-patch16-224`
  (<https://huggingface.co/facebook/deit-small-patch16-224>)
* **Tipo**: preentrenado en ImageNet-1k, **con fine-tuning propio** de la cabeza de
  clasificación a 2 clases (`capybara`, `beaver`)
* **Framework**: PyTorch (`transformers` de Hugging Face)
* **Arquitectura**: Vision Transformer (ViT), parches 16×16, 224×224 de entrada, ~22M
  parámetros — **no es una CNN**. Esto es relevante para `05-shap.md`: los explicadores de
  SHAP basados en gradientes por capas convolucionales (`GradientExplainer`,
  `DeepExplainer`) no aplican directamente aquí.

### Por qué `deit-small` y no `tiny` ni `base`

| Checkpoint | Parámetros | Descarte / elección |
|---|---|---|
| `facebook/deit-tiny-patch16-224` | ~5M | Capacidad baja; peor representación preentrenada para el análisis de atribuciones |
| **`facebook/deit-small-patch16-224`** | **~22M** | **Elegido**: suficiente capacidad, entrenable en CPU/Colab gratuito, riesgo de sobreajuste manejable con ~360 imágenes de entrenamiento |
| `facebook/deit-base-distilled-patch16-224` | ~87M | Sobredimensionado para 360 imágenes; además el token de destilación añade una segunda cabeza que complica el envoltorio caja negra de SHAP sin aportar al objetivo explicativo |

Nota: `facebook/deit-small-patch16-224` se carga como `ViTForImageClassification`
(no tiene token de destilación), por lo que la salida es un único tensor `logits` — el
envoltorio `predict()` de `05-shap.md` es directo.

### Por qué hay fine-tuning y no uso zero-shot

Se verificó la lista de clases de ImageNet-1k:

* `beaver` **sí** existe → índice **337**
* `capybara` **no** existe en las 1000 clases

Las clases más cercanas a un capibara en ImageNet-1k son `porcupine` (334), `marmot` (336),
`guinea pig` (338) y `otter` (360). Por tanto el modelo preentrenado **no puede** resolver
la tarea capibara vs. castor tal cual, y el fine-tuning es obligatorio, no una preferencia.

Consecuencia para el paper: la asimetría del preentrenamiento (el castor es una clase vista
en ImageNet-1k, el capibara no) es en sí misma una hipótesis explicativa que SHAP puede
ayudar a examinar, y debe declararse.

## Carga del modelo

```python
from transformers import AutoImageProcessor, AutoModelForImageClassification

CHECKPOINT = "facebook/deit-small-patch16-224"
LABELS = ["capybara", "beaver"]

processor = AutoImageProcessor.from_pretrained(CHECKPOINT)
model = AutoModelForImageClassification.from_pretrained(
    CHECKPOINT,
    num_labels=len(LABELS),
    id2label={i: l for i, l in enumerate(LABELS)},
    label2id={l: i for i, l in enumerate(LABELS)},
    ignore_mismatched_sizes=True,   # sustituye la cabeza de 1000 clases por una de 2
)
```

Tras el fine-tuning, el modelo entrenado se guarda y se recarga desde disco para las
explicaciones, de modo que `05-shap.md` explique exactamente el modelo evaluado:

```python
model.save_pretrained("artifacts/deit-small-capybara-beaver")
processor.save_pretrained("artifacts/deit-small-capybara-beaver")

# en el notebook de SHAP:
CHECKPOINT = "artifacts/deit-small-capybara-beaver"
model = AutoModelForImageClassification.from_pretrained(CHECKPOINT).eval()
processor = AutoImageProcessor.from_pretrained(CHECKPOINT)
```

## Fine-tuning

* **Qué se entrena**: todo el backbone + cabeza nueva (full fine-tuning). Con ~360 imágenes
  es viable y da mejor separación que congelar el backbone.
* **Datos**: splits `train` / `val` de `06-data.md`
* **Hiperparámetros de partida** (a reportar tal como se ejecuten, no como intención):

  | Parámetro | Valor |
  |---|---|
  | épocas | 10 |
  | batch size | 16 |
  | learning rate | 5e-5 |
  | optimizador | AdamW |
  | scheduler | lineal con warmup 10% |
  | weight decay | 0.01 |
  | semilla | 42 |
  | selección de checkpoint | mejor `val_accuracy` |

* **Aumentación**: `RandomResizedCrop(224, scale=(0.7, 1.0))` + `RandomHorizontalFlip` solo
  en entrenamiento. En validación, test y **SHAP** no hay aumentación: `Resize(256)` +
  `CenterCrop(224)`.
* **Métricas a reportar**: accuracy y F1 macro en `test` (40 imágenes) y en el conjunto
  `control` (100 capibaras de iNaturalist). La brecha entre ambos es la medida del atajo de
  fuente descrito en `06-data.md`.

## Preprocesamiento

* Resolución de entrada: **224×224**
* Normalización: la que define `processor` (`image_mean = image_std = [0.5, 0.5, 0.5]`
  para los checkpoints DeiT; se lee de `processor`, no se codifica a mano)
* Encapsulado en una función reutilizable tanto por la inferencia normal como por el
  envoltorio que usará SHAP:

```python
import numpy as np, torch

def preprocess(images):
    """images: lista de PIL.Image o array (N, 224, 224, 3) uint8 -> tensor (N, 3, 224, 224)."""
    if isinstance(images, np.ndarray):
        images = list(images.astype("uint8"))
    return processor(images=images, return_tensors="pt")["pixel_values"]
```

Para SHAP las imágenes de prueba se llevan a 224×224 uint8 **antes** de entrar al masker,
de modo que el redimensionado del `processor` sea un no-op y las regiones enmascaradas
coincidan píxel a píxel con lo que ve el modelo.

## Clases de salida

* Espacio de clases: **2** — `0: capybara`, `1: beaver`
* Mapeo id → etiqueta: `model.config.id2label`
* Salida cruda: `logits` de forma `(N, 2)`; las probabilidades son `softmax(logits, dim=-1)`

## Dependencias externas

* **Imágenes de prueba (3) y pregunta explicativa concreta**: definidas en `06-data.md`
* **Explicador y figuras**: `05-shap.md`

## Entorno

```
torch>=2.2
transformers>=4.40
datasets>=2.19
shap>=0.45
pillow
scikit-learn
matplotlib
```
