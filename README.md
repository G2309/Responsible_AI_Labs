# Explicaciones SHAP de un clasificador preentrenado (DeiT)

Josué Emanuel Say García (22801) · Gustavo Adolfo Cruz Bardales (22779)

| Ruta | Qué es |
|---|---|
| `paper/paper.tex` | Fuente LaTeX principal |
| `paper.pdf` | PDF compilado (5 páginas) |
| `paper/refs.bib` | Referencias |
| `paper/numeros.tex` | Cifras, generadas desde `results.json` |
| `shap_deit.ipynb` | Notebook SHAP, ejecutado y con salidas |
| `figures/` | Figuras como archivos independientes |
| `results.json` | Predicciones y estabilidad de la corrida |
| `BITACORA.md` | Bitácora de desarrollo y decisiones |
| `LIMITACIONES.md` | Limitaciones |

## Reproducir

**Colab:** subir `shap_deit.ipynb` y ejecutar todo. Descarga las 3 imágenes e instala lo que
falte. ~8 min en CPU.

**Local:** `pip install -r requirements.txt`, luego ejecutar el notebook. Para el PDF:
`python3 gen_numeros.py && latexmk -pdf -cd paper/paper.tex`.

Las imágenes no se redistribuyen: el notebook las descarga de su fuente (repo MIT y
iNaturalist CC BY-NC).
