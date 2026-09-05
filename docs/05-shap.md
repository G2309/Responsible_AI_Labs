# 05 — SHAP

## Objetivo

Definir qué hay que hacer para producir explicaciones SHAP del modelo descrito en
`04-model.md` sobre las imágenes de prueba de `06-data.md`, y qué se entrega como evidencia
en el paper.

## Pregunta que debe responder la explicación

> ¿El clasificador DeiT separa capibara de castor por rasgos del animal (hocico, orejas,
> cola, cuerpo), o por el contexto de la escena (agua, vegetación, madera roída) y el estilo
> de la fuente de las fotos?

(Definida en `06-data.md`, junto con las tres imágenes de prueba `IMG-01`…`IMG-03`.)

## Por qué no un explicador basado en gradientes de CNN

DeiT es un Vision Transformer, no una CNN. `shap.DeepExplainer` y `shap.GradientExplainer`
asumen arquitecturas con capas convolucionales cuyo gradiente por capa es interpretable de
forma directa; sobre un ViT no hay garantía de soporte ni de resultados sensatos.

## Explicador a usar

**`shap.Explainer` model-agnóstico con `shap.maskers.Image`** (algoritmo *Partition*).
Trata el modelo como caja negra (solo necesita `predict(images) -> probs`), perturbando
regiones de la imagen (blur o inpainting) y midiendo el cambio en la predicción. Funciona
igual para CNN, ViT o cualquier clasificador.

```python
import numpy as np
import shap
import torch
from PIL import Image
from transformers import AutoImageProcessor, AutoModelForImageClassification

CHECKPOINT = "artifacts/deit-small-capybara-beaver"   # modelo fine-tuned de 04-model.md
processor = AutoImageProcessor.from_pretrained(CHECKPOINT)
model = AutoModelForImageClassification.from_pretrained(CHECKPOINT).eval()
class_names = [model.config.id2label[i] for i in range(model.config.num_labels)]  # [capybara, beaver]

def load_224(path):
    """Misma transformación determinista que val/test en 04-model.md."""
    img = Image.open(path).convert("RGB")
    w, h = img.size
    s = 256 / min(w, h)
    img = img.resize((round(w * s), round(h * s)), Image.BICUBIC)
    left, top = (img.width - 224) // 2, (img.height - 224) // 2
    return np.array(img.crop((left, top, left + 224, top + 224)), dtype=np.uint8)

X = np.stack([load_224(p) for p in TEST_IMAGE_PATHS])   # (3, 224, 224, 3) uint8

def predict(images_np):
    # images_np: (N, 224, 224, 3) en [0, 255]; el resize del processor es no-op
    inputs = processor(images=list(images_np.astype("uint8")), return_tensors="pt")
    with torch.no_grad():
        logits = model(**inputs).logits
    return torch.softmax(logits, dim=-1).numpy()

masker = shap.maskers.Image("blur(128,128)", X[0].shape)   # (224, 224, 3)
explainer = shap.Explainer(predict, masker, output_names=class_names)

shap_values = explainer(
    X,
    max_evals=3000,     # ~1.5k evaluaciones/imagen es demasiado grueso a 224x224; 3000 es el compromiso
    batch_size=64,
    outputs=shap.Explanation.argsort.flip[:1],   # la clase predicha (top-1) de cada imagen
)

shap.image_plot(shap_values, show=False)
```

### Notas sobre la configuración

* **`blur(128,128)`**: el baseline de enmascarado es la imagen desenfocada, no gris ni negro.
  Evita introducir parches artificiales fuera de la distribución que el ViT interpretaría
  como estructura. Alternativa: `"inpaint_telea"` (más lento, resultados comparables).
  Si se cambia, hay que reportar cuál se usó: **la elección del baseline cambia los valores
  de Shapley**, no es un detalle cosmético.
* **`outputs=...flip[:1]`**: con 2 clases, `phi(capybara) ≈ -phi(beaver)`, así que basta
  explicar la clase predicha. Para `IMG-03` (el caso crítico) conviene además generar el
  mapa de la clase **verdadera** `capybara` aunque no sea la predicha, para ver qué evidencia
  encontró el modelo *a favor* de la respuesta correcta:

  ```python
  sv_true = explainer(X[2:3], max_evals=3000, batch_size=64, outputs=[0])  # 0 = capybara
  ```
* **`max_evals`**: Partition es aproximado. 3000 evaluaciones sobre 224×224 dan regiones
  del orden de decenas de píxeles, no atribución por píxel. Hay que decirlo en el paper y no
  interpretar bordes finos del mapa.

## Pasos

1. Cargar el modelo fine-tuned + processor desde `artifacts/` (ver `04-model.md`)
2. Cargar las 3 imágenes de prueba de `06-data.md` con `load_224` y registrar sus rutas /
   `photo_id` / atribución en `data/test_images.csv`
3. Envolver la inferencia en `predict(images) -> probs` (batch-friendly)
4. Definir el `masker` de imagen con shape `(224, 224, 3)`
5. Correr `explainer(...)` para la clase predicha de cada imagen, más la clase verdadera de
   `IMG-03`
6. Visualizar con `shap.image_plot` y guardar las figuras
   (`figures/shap_img01.png`, `shap_img02.png`, `shap_img03_pred.png`,
   `shap_img03_true.png`) en el formato que consuma el `paper.tex`
7. **Comprobación de estabilidad**: repetir `IMG-03` con `max_evals` ∈ {1500, 3000, 6000} y
   con otra semilla; reportar si el mapa cambia cualitativamente. Sin esto no se puede
   afirmar que una región «importa».
8. Redactar en el paper: qué muestran los mapas SHAP, si responden la pregunta explicativa,
   y qué limitaciones tiene la explicación
9. Registrar en el log de prompts qué se le pidió a ChatGPT en cada iteración del loop

## Cómo se lee el resultado (criterio fijado *antes* de mirar los mapas)

Para no ajustar la interpretación al resultado obtenido, se fija de antemano:

* **Evidencia a favor de «mira al animal»**: la masa de atribución positiva a la clase
  predicha se concentra sobre el cuerpo/cabeza del animal, y `IMG-03` se clasifica
  correctamente como capibara pese al agua.
* **Evidencia a favor de «mira al contexto»**: atribución positiva significativa sobre
  regiones de agua/vegetación sin animal, y/o `IMG-03` se clasifica como castor con
  atribución positiva sobre el agua.
* **Resultado mixto**: es el desenlace más probable y hay que reportarlo como tal, no
  forzarlo a una de las dos ramas.

La métrica cuantitativa de apoyo es la brecha `test accuracy` vs. `control accuracy` de
`04-model.md`: los mapas SHAP explican *por qué* existe esa brecha, no la sustituyen.

## Limitaciones de la explicación a declarar

* SHAP Partition es una **aproximación** con presupuesto finito de evaluaciones; los valores
  no son los valores de Shapley exactos.
* La atribución depende del baseline (`blur(128,128)`) y de la resolución del masker.
* Un mapa SHAP indica **asociación** entre regiones y salida del modelo, no un mecanismo
  causal ni una justificación de que el modelo sea correcto.
* Con 3 imágenes no se puede generalizar el comportamiento del modelo; son casos ilustrativos
  elegidos por diseño (ver `06-data.md`), no una muestra representativa.
* La asimetría de preentrenamiento (ImageNet-1k contiene `beaver` pero no `capybara`,
  ver `04-model.md`) es una explicación alternativa plausible de cualquier asimetría
  observada en los mapas, y no queda descartada por este experimento.

## Entregables que alimenta este paso

* Código/notebook SHAP (el snippet de arriba, ejecutable)
* Figuras (`shap.image_plot` por imagen + los mapas de estabilidad)
* Insumos para la sección de resultados y limitaciones del `paper.tex`
