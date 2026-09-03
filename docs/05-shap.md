# 05 — SHAP

## Objetivo

Definir qué hay que hacer para producir explicaciones SHAP del modelo descrito en
`04-model.md` sobre las imágenes de prueba, y qué se entrega como evidencia en el paper.

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
import shap
import numpy as np
import torch

def predict(images_np):
    # images_np: (N, H, W, 3) uint8/float en rango [0,255]
    inputs = processor(images=list(images_np), return_tensors="pt")
    with torch.no_grad():
        logits = model(**inputs).logits
    return torch.softmax(logits, dim=-1).numpy()

masker = shap.maskers.Image("blur(128,128)", shape_de_la_imagen)  # TODO: shape real
explainer = shap.Explainer(predict, masker, output_names=list(model.config.id2label.values()))

shap_values = explainer(
    imagenes_de_prueba,          # TODO: viene de 03-inputs.md
    max_evals=500,                # TODO: ajustar costo vs. calidad
    batch_size=50,
    outputs=shap.Explanation.argsort.flip[:1]  # top-1 predicho, o fijar clase de la pregunta
)
```

## Pasos

1. Cargar modelo + processor (ver `04-model.md`)
2. Envolver la inferencia en `predict(images) -> probs` (batch-friendly)
3. Definir el `masker` de imagen y el tamaño de entrada
4. Cargar las 1–3 imágenes de prueba y la pregunta explicativa desde el doc de inputs
5. Correr `explainer(...)` para la(s) clase(s) relevante(s) a la pregunta
   (top-1 predicho, o una clase específica si la pregunta lo pide)
6. Visualizar con `shap.image_plot` y guardar las figuras (`.png`/`.pdf`) para el paper
7. Redactar en el paper: qué muestran los mapas SHAP, si responden la pregunta explicativa,
   y qué limitaciones tiene la explicación (número de evaluaciones, resolución del masker,
   costo computacional, estabilidad entre corridas)
8. Registrar en el log de prompts qué se le pidió a ChatGPT en cada iteración del loop

## Entregables que alimenta este paso

* Código/notebook SHAP (el snippet de arriba, ejecutable)
* Figuras (`shap.image_plot` por imagen)
* Insumos para la sección de resultados y limitaciones del `paper.tex`

