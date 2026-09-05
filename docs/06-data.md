# 06 — Datos e imágenes de prueba

## Objetivo

Fijar **qué imágenes** se usan, de dónde salen, bajo qué licencia, y cuáles son las 1–3
imágenes de prueba que se explican con SHAP. Este documento cubre la entrada
«1–3 imágenes de prueba + pregunta explicativa concreta» del `00-guide.md`, y es la fuente
de verdad de datos para `04-model.md` (fine-tuning) y `05-shap.md` (explicación).

## Tarea

Clasificación binaria de imágenes: **capibara (`Hydrochoerus hydrochaeris`)** vs
**castor (`Castor canadensis`)**.

Motivo de esta pareja: son dos roedores semiacuáticos grandes que comparten hábitat visual
(agua, orilla, vegetación) pero difieren en morfología (hocico, orejas, cola). Es decir,
el fondo es un atajo plausible y la forma del animal es la señal correcta. Esa tensión es
justamente lo que SHAP tiene que poder distinguir.

---

## Fuente A — Capibaras

* **Repositorio**: `freds0/capybara_dataset`
* **URL**: <https://github.com/freds0/capybara_dataset>
* **Licencia**: MIT (Copyright 2021 Fred Oliveira)
* **Contenido verificado** (rama `main`):

  | Split | Imágenes | Anotaciones |
  |---|---|---|
  | `images/train` | 180 (178 `.jpeg` + 2 `.jpg`) | 180 `.xml` (Pascal VOC) |
  | `images/test`  | 20 `.jpeg`                    | 20 `.xml` (Pascal VOC) |
  | **Total**      | **200**                       | 200 |

* **Uso en este trabajo**: se usan **solo las imágenes**. Las cajas Pascal VOC (`.xml`) y
  los CSV de `data/` son para detección de objetos y **se ignoran**: aquí la tarea es
  clasificación de imagen completa, no detección.

```bash
git clone --depth 1 https://github.com/freds0/capybara_dataset.git data/raw/capybara_dataset
```

## Fuente B — Castores

No se encontró un repositorio GitHub de castores equivalente al de capibaras (mismo orden de
magnitud, licencia clara y descarga directa). Los candidatos revisados y descartados:

* Roboflow Universe (datasets de castores): requiere API key y cuenta → rompe la
  reproducibilidad sin credenciales.
* `images.cv`: descarga bloqueada tras registro (HTTP 403 al acceso directo).
* Open Images V7: **no** tiene la clase `Beaver` entre las 601 clases *boxable*
  (verificado sobre `oidv7-class-descriptions-boxable.csv`).

Fuente elegida en su lugar:

* **iNaturalist API v1** (`https://api.inaturalist.org/v1/observations`)
* **Taxón**: `Castor canadensis`, `taxon_id=43794` (American Beaver)
* **Filtros**: `quality_grade=research`, `photo_license=cc0,cc-by,cc-by-nc`
* **Disponibilidad verificada**: 57 033 observaciones que cumplen los filtros
* **Licencia**: CC0 / CC BY / CC BY-NC según foto — se guarda el `license_code`, el
  `attribution` y la URL de cada foto en un CSV de procedencia (`data/beaver_credits.csv`)
* **Uso**: se descargan las primeras **200 fotos** (tamaño `medium`), para igualar el
  tamaño de la clase capibara

## Fuente C — Conjunto de control (capibaras de iNaturalist)

Las clases A y B vienen de fuentes distintas, con fotógrafos, cámaras y estilos distintos.
Eso introduce una **correlación espuria de fuente**: el modelo podría aprender «estilo de
foto del repo» en vez de «capibara». Para poder detectarlo se descarga un conjunto de
control, **nunca usado en entrenamiento**:

* **Taxón**: `Hydrochoerus hydrochaeris`, `taxon_id=74442` (Capybara)
* **Mismos filtros**; disponibilidad verificada: 10 735 observaciones
* **Uso**: 100 fotos, solo evaluación. Si la exactitud cae fuerte aquí respecto al test
  in-domain, hay atajo de fuente y hay que decirlo en las limitaciones del paper.

## Script de descarga

Debe existir como artefacto ejecutable (`scripts/download_data.py`) para satisfacer A03/C09.

```python
"""Descarga las imágenes de capibara (GitHub) y castor (iNaturalist)."""
import csv, json, os, time, urllib.request

INAT = "https://api.inaturalist.org/v1/observations"
LICENSES = "cc0,cc-by,cc-by-nc"

def fetch_inat(taxon_id, n, out_dir, credits_csv):
    os.makedirs(out_dir, exist_ok=True)
    rows, page = [], 1
    while len(rows) < n:
        url = (f"{INAT}?taxon_id={taxon_id}&quality_grade=research&photos=true"
               f"&photo_license={LICENSES.replace(',', '%2C')}"
               f"&per_page=200&page={page}&order_by=id&order=desc")
        with urllib.request.urlopen(url) as r:
            results = json.load(r)["results"]
        if not results:
            break
        for obs in results:
            photo = obs["photos"][0]
            rows.append({
                "observation_id": obs["id"],
                "photo_id": photo["id"],
                "license": photo["license_code"],
                "attribution": photo.get("attribution", ""),
                "url": photo["url"].replace("/square.", "/medium."),
            })
            if len(rows) >= n:
                break
        page += 1
        time.sleep(1)  # cortesía con la API pública de iNaturalist

    for row in rows:
        ext = os.path.splitext(row["url"])[1].split("?")[0] or ".jpg"
        path = os.path.join(out_dir, f"{row['photo_id']}{ext}")
        if not os.path.exists(path):
            urllib.request.urlretrieve(row["url"], path)
        row["local_path"] = path

    with open(credits_csv, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    print(f"{len(rows)} imágenes -> {out_dir}")

if __name__ == "__main__":
    os.system("git clone --depth 1 https://github.com/freds0/capybara_dataset.git "
              "data/raw/capybara_dataset")
    fetch_inat(43794, 200, "data/raw/beaver_inat", "data/beaver_credits.csv")
    fetch_inat(74442, 100, "data/raw/capybara_inat_control",
               "data/capybara_control_credits.csv")
```

## Splits

Estratificado por clase, semilla fija `seed=42`:

| Split | Capibara | Castor | Total | Origen |
|---|---|---|---|---|
| `train` | 144 | 144 | 288 | A (`images/train`) + B |
| `val`   | 36  | 36  | 72  | A (`images/train`) + B |
| `test`  | 20  | 20  | 40  | A (`images/test`) + B |
| `control` | 100 | — | 100 | C (solo capibaras de iNaturalist) |

El split `test` de capibara respeta el split original del repositorio (`images/test`), para
no mezclar imágenes que el autor separó.

---

## Pregunta explicativa

> **¿El clasificador DeiT separa capibara de castor por rasgos del animal (hocico, orejas,
> cola, cuerpo), o por el contexto de la escena (agua, vegetación, madera roída) y el estilo
> de la fuente de la que provienen las fotos?**

Es una pregunta contestable con SHAP: los valores de Shapley por región dicen si la
atribución positiva a la clase predicha cae sobre el animal o sobre el fondo.

## Imágenes de prueba (3)

| ID | Clase real | Origen | Por qué esta imagen |
|---|---|---|---|
| `IMG-01` | capibara | `capybara_dataset/images/test` | Caso in-domain típico. Línea base: ¿la atribución cae sobre el animal? |
| `IMG-02` | castor | iNaturalist (`Castor canadensis`) | Caso in-domain típico de la otra clase, con agua en escena. Contraste directo con `IMG-01`. |
| `IMG-03` | capibara | conjunto de control iNaturalist | **Caso crítico**: capibara *en agua*, fuera del dominio de entrenamiento de esa clase. Si el modelo falla aquí y SHAP atribuye a la región de agua, queda evidenciado el atajo de contexto/fuente. |

Los tres IDs concretos (nombre de archivo y, para iNaturalist, `photo_id` + atribución) se
fijan al ejecutar el script y se registran en `data/test_images.csv`. La selección de
`IMG-03` es intencional: se elige entre las imágenes de control **una con agua visible**,
y ese criterio se declara en el paper (no es una imagen escogida por su resultado).

## Limitaciones de datos a declarar en el paper

1. **Fuentes heterogéneas por clase**: capibara viene de un repo curado, castor de fotos
   ciudadanas. Cualquier diferencia sistemática de estilo es confundible con la señal de
   clase. El conjunto de control existe para medir esto, no para eliminarlo.
2. **Tamaño pequeño**: 400 imágenes de entrenamiento + validación. Las métricas de test
   (40 imágenes) tienen intervalos de confianza amplios; no se deben reportar como
   estimaciones precisas.
3. **Sesgo geográfico**: `Castor canadensis` es norteamericano y el capibara sudamericano;
   el fondo (bioma, estación, vegetación) está correlacionado con la clase por construcción.
   Esto no es un defecto del muestreo, es una propiedad del problema, y limita cuánto puede
   concluirse de un mapa SHAP que resalte el fondo.
4. **Contenido de iNaturalist variable**: hay fotos con marcas de agua, trampas de cámara,
   rastros (diques, árboles roídos) o animales muy pequeños en el encuadre. No se filtran
   manualmente; se declara como ruido de etiqueta a nivel de imagen.
