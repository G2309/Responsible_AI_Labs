# Bitácora de desarrollo

Registro de las decisiones que dieron forma al entregable, siguiendo el ciclo de
`00-guide.md`: definir estructura → generar `.tex` → compilar → ejecutar SHAP → insertar
resultados → revisar afirmaciones.

## 1. Elección del modelo

Se optó por un Vision Transformer de la familia DeiT, en concreto
`facebook/deit-small-patch16-224` (~22M parámetros), preentrenado en ImageNet-1k y usado sin
modificar.

Antes de fijarlo se comprobó el vocabulario del modelo: ImageNet-1k **sí** contiene la clase
`beaver` (índice 337) pero **no** contiene `capybara`. Esa asimetría no se descubrió después
sino antes de diseñar el caso, y es la razón por la que el trabajo no evalúa acierto sino
atribución: el modelo no tiene forma de nombrar correctamente a una capibara.

## 2. Selección de las imágenes

Las capibaras provienen del repositorio `freds0/capybara_dataset` (licencia MIT). Para los
castores se buscó un repositorio equivalente y no existe: Roboflow Universe exige
credenciales, `images.cv` bloquea la descarga directa (HTTP 403) y Open Images V7 no incluye
la clase *Beaver* entre sus 601 clases con caja. Se recurrió entonces a la API pública de
iNaturalist, filtrando por calidad *research* y licencias CC0 / CC BY / CC BY-NC.

Las tres imágenes se eligieron para que el contraste respondiera la pregunta explicativa:
misma especie en contextos opuestos (IMG-01 seco, IMG-03 acuático) y la otra especie en
contexto acuático (IMG-02). El criterio se fijó antes de ejecutar nada.

## 3. Configuración de SHAP

Al ser DeiT un transformer y no una red convolucional, se descartaron `DeepExplainer` y
`GradientExplainer`, que asumen capas convolucionales. Se usó el explicador model-agnóstico
`shap.Explainer` con `shap.maskers.Image` (*Partition*).

Como *baseline* de enmascarado se eligió la imagen desenfocada en vez de un parche gris, para
no introducir estructura fuera de distribución. El criterio de lectura de los mapas —qué
contaría como «mira al animal» y qué como «mira al contexto»— se escribió **antes** de
generar ninguna figura, y no se modificó después.

## 4. Alcance

Una versión intermedia del trabajo incluía descarga masiva de imágenes, entrenamiento propio
y un experimento de ablación. Se descartó por exceder lo que pide `00-guide.md`, que solicita
un clasificador preentrenado o propio, de una a tres imágenes de prueba y una pregunta
explicativa. El entregable final se ciñe a eso.

## 5. Fallo detectado y corregido

En la primera ejecución completa, IMG-02 e IMG-03 devolvieron exactamente la misma
probabilidad (0.259). Esa coincidencia exacta no era plausible y llevó a revisar el código:
las dos fotografías de iNaturalist se guardaban con el mismo nombre de archivo local, porque
el nombre se derivaba del último segmento de la URL y ambas terminan en `medium.jpg`. IMG-03
estaba reutilizando la imagen de IMG-02.

Se corrigió el nombrado para usar el identificador de cada imagen y se reejecutó todo el
notebook desde cero. Las cifras y figuras entregadas provienen de la ejecución corregida.
Tras la corrección, IMG-03 se clasifica como `beaver` con p = 0.498.

## 6. Integración de resultados en el paper

Los resultados pasan del notebook al documento por un único camino: `results.json` →
`gen_numeros.py` → `paper/numeros.tex`. El paper no contiene ninguna cifra escrita a mano, de
modo que el texto no puede quedar desincronizado de la ejecución. Volver a correr el notebook
y recompilar actualiza el documento entero de forma consistente.
