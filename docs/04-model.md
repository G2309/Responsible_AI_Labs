# 04 — Modelo

## Objetivo

Definir el clasificador de imágenes que se va a explicar con SHAP: origen, arquitectura,
framework, preprocesamiento y salidas. Este documento es la base para `05-shap.md`
(qué explicador usar) y para la sección de Método del `paper.tex`.

## Modelo elegido

* **Nombre**: DeiT (Data-efficient Image Transformer) — Hugging Face
* **Documentación**: https://huggingface.co/docs/transformers/v5.15.1/en/model_doc/deit#deit 
* **Checkpoint**: `TODO` (ej. `facebook/deit-base-patch16-224`,
  `facebook/deit-base-distilled-patch16-224`, `facebook/deit-tiny-patch16-224`)
* **Tipo**: preentrenado en ImageNet-1k (no fine-tuning propio, salvo que se decida lo contrario)
* **Framework**: PyTorch (`transformers` de Hugging Face)
* **Arquitectura**: Vision Transformer (ViT) con destilación por token — **no es una CNN**.
  Esto es relevante para `05-shap.md`: los explicadores de SHAP basados en gradientes por
  capas convolucionales (`GradientExplainer`, `DeepExplainer`) no aplican directamente aquí.

## Carga del modelo

```python
from transformers import AutoImageProcessor, AutoModelForImageClassification

checkpoint = "TODO"  # ej. facebook/deit-base-distilled-patch16-224
processor = AutoImageProcessor.from_pretrained(checkpoint)
model = AutoModelForImageClassification.from_pretrained(checkpoint)
model.eval()
```

## Preprocesamiento

* Resolución de entrada: `TODO` (típico DeiT: 224x224)
* Normalización: la que define `processor` (mean/std de ImageNet)
* Debe quedar encapsulado en una función `preprocess(images) -> tensor` reutilizable
  tanto por la inferencia normal como por el wrapper que usará SHAP.

## Clases de salida

* Espacio de clases: ImageNet-1k (1000 clases) salvo que el checkpoint sea fine-tuned
* Mapeo id → etiqueta: `model.config.id2label`

## Dependencias externas

* **Imágenes de prueba (1–3)** y **pregunta explicativa concreta**:

