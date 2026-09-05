# Criterios de aceptación — Contenido

## 1. Propósito

Este documento define qué deben contener y demostrar los artefactos cuya existencia se exige en `01_acceptance_artifacts.md`.

Los criterios de este documento evalúan el contenido, la coherencia, la trazabilidad y la capacidad de interpretación de la entrega.

Este documento no define decisiones técnicas internas correspondientes al modelo de clasificación ni a SHAP.

---

## 2. Frontera de responsabilidades

### C15 — Separación respecto a modelo y SHAP

Los criterios específicos correspondientes al modelo y a SHAP quedan fuera del alcance de este documento.

En particular, este documento no establece criterios sobre:

* selección del modelo;
* arquitectura del modelo;
* configuración interna del modelo;
* entrenamiento del modelo;
* framework utilizado por el modelo;
* dataset requerido por el modelo;
* evaluación de la validez interna del modelo;
* selección del método SHAP;
* configuración interna de SHAP;
* implementación de SHAP;
* versión concreta de SHAP;
* decisiones técnicas propias del procedimiento explicativo;
* evaluación de la validez interna de la implementación SHAP.

Estas responsabilidades serán especificadas separadamente en:

* `04_modelo.md`, para el modelo;
* `05_shap.md`, para SHAP.

Los criterios `01`, `02` y `03` sí pueden exigir que los artefactos recibidos desde esos componentes sean correctamente integrados, identificados, utilizados y relacionados con las afirmaciones del paper.

También pueden exigir consistencia entre los resultados recibidos y aquello que el paper afirma sobre ellos.

Esta distinción no autoriza al agente encargado del paper a sustituir, modificar o completar unilateralmente decisiones pertenecientes a `04_modelo.md` o `05_shap.md`.

---

## 3. Estructura mínima del paper

### C01 — Estructura mínima identificable

El paper debe contener componentes identificables que cumplan, como mínimo, las siguientes funciones:

* introducción o contexto;
* metodología;
* resultados;
* discusión o interpretación;
* limitaciones;
* conclusiones.

No se exige que estos sean los nombres literales de las secciones.

Tampoco se establece mediante este criterio:

* cantidad de páginas;
* cantidad exacta de secciones;
* plantilla LaTeX específica;
* diseño visual concreto;
* distribución exacta del contenido.

### Verificación

Un evaluador debe poder localizar inequívocamente dentro del paper dónde se cumple cada una de las funciones anteriores.

---

## 4. Caso y pregunta explicativa

### C02 — Caso y objetivo explicativo explícitos

El paper debe identificar claramente el caso analizado y formular explícitamente la pregunta explicativa que pretende responder.

Debe ser posible determinar:

1. qué caso está siendo analizado;
2. cuál es la pregunta explicativa;
3. qué resultados del trabajo pretenden contribuir a responderla.

La pregunta no debe quedar únicamente implícita en la descripción general del ejercicio.

Este criterio no determina cuál debe ser la pregunta explicativa ni prescribe cómo debe responderse técnicamente.

---

## 5. Entradas analizadas

### C03 — Identificación de las entradas utilizadas

Las imágenes efectivamente utilizadas en el análisis deben quedar identificadas de manera suficiente para determinar cuáles fueron las entradas asociadas a los resultados presentados.

Cuando existan múltiples imágenes, debe ser posible distinguirlas inequívocamente.

### Verificación

Debe poder establecerse una relación entre:

`entrada analizada → resultado presentado`

No se exige mediante este criterio una cantidad de imágenes distinta de la definida por el ejercicio.

---

## 6. Evidencia experimental

### C05 — Resultados vinculados con evidencia

Todo resultado experimental relevante discutido en el paper debe poder relacionarse con evidencia producida por los artefactos experimentales aceptados en `01_acceptance_artifacts.md`.

Debe existir trazabilidad conceptual suficiente para establecer:

`ejecución → resultado → evidencia presentada`

Un resultado experimental no debe introducirse únicamente como una afirmación textual cuando no exista evidencia identificable que permita relacionarlo con la ejecución correspondiente.

Este criterio no prescribe cómo debe producirse técnicamente dicha evidencia.

---

## 7. Figuras

### C06 — Figuras referenciadas y utilizadas

Cada figura incluida en el paper debe:

* estar identificada;
* estar referenciada desde el texto;
* poseer una función reconocible dentro de la exposición, análisis o argumentación.

Las figuras utilizadas como evidencia deben poder relacionarse con el resultado o afirmación correspondiente.

No se prescribe:

* cantidad de figuras;
* ubicación exacta;
* dimensiones;
* formato gráfico;
* estilo visual.

### C14 — Captions informativos

Cada figura utilizada como evidencia debe disponer de un caption que permita identificar qué representa.

El caption debe proporcionar contexto suficiente para reconocer el propósito básico de la figura sin introducir afirmaciones que no estén respaldadas por la evidencia correspondiente.

No se establece una longitud ni estilo específico para los captions.

---

## 8. Afirmaciones y evidencia

### C07 — Afirmaciones respaldadas sin exceder la evidencia

Las afirmaciones derivadas de los resultados experimentales deben estar respaldadas por evidencia presentada en la entrega.

Debe poder distinguirse razonablemente entre:

* observaciones obtenidas de los resultados;
* interpretación de dichas observaciones;
* conclusiones derivadas.

Las afirmaciones no deben generalizar más allá de lo que permite la evidencia disponible.

En particular, la existencia de una visualización o resultado explicativo no autoriza por sí misma afirmaciones causales o generales que la evidencia no permita sostener.

Este criterio evalúa la relación entre evidencia y afirmación; no evalúa internamente la técnica SHAP utilizada.

---

## 9. Referencias

### C08 — Referencias con función verificable

Cada referencia citada debe tener una función identificable dentro del trabajo.

Una referencia puede utilizarse, entre otros propósitos, para respaldar:

* una afirmación;
* una definición;
* un antecedente;
* una descripción metodológica;
* información técnica;
* contexto necesario para el trabajo.

La similitud temática entre una fuente y el paper no es suficiente para justificar su inclusión.

Debe ser posible establecer:

`cita → fuente → contenido respaldado`

Las referencias no deben:

* ser inventadas;
* conducir a recursos distintos de los declarados;
* utilizarse para respaldar afirmaciones que la fuente no sostiene;
* añadirse únicamente para incrementar artificialmente la bibliografía.

No se establece una cantidad mínima arbitraria de referencias.

---

## 10. Información para reproducción

### C09 — Información suficiente para reproducción

Los artefactos experimentales y la especificación del entorno aprobados en `01_acceptance_artifacts.md` deben contener conjuntamente información suficiente para que un tercero pueda comprender cómo repetir las partes ejecutables correspondientes.

La reproducción no debe depender exclusivamente de conocimiento tácito del autor.

Debe poder determinarse, en la medida requerida por los componentes recibidos:

* qué artefactos intervienen;
* qué dependencias declaradas necesitan;
* cómo se relacionan dichos artefactos;
* qué procedimiento general permite repetir la ejecución.

Este criterio no prescribe:

* lenguaje;
* framework;
* gestor de dependencias;
* sistema operativo;
* contenedor;
* hardware;
* implementación del modelo;
* implementación de SHAP.

Cuando información necesaria dependa de `04_modelo.md` o `05_shap.md`, el agente del paper no debe inventarla: debe utilizar la información proporcionada por esos componentes o declarar el faltante conforme a los criterios correspondientes.

---

## 11. Consistencia entre artefactos

### C10 — Consistencia de la entrega

Los siguientes elementos deben representar de forma coherente el mismo estado final del trabajo:

* fuente LaTeX;
* PDF;
* código o notebook experimental;
* figuras;
* resultados discutidos;
* referencias utilizadas.

No deben existir discrepancias observables como:

* figuras referenciadas que no correspondan con las entregadas;
* resultados del paper incompatibles con los artefactos experimentales;
* contenido visible en el PDF que no corresponda con el fuente final;
* referencias utilizadas pero ausentes de los recursos entregados cuando sean necesarias;
* resultados antiguos presentados como si correspondieran a la ejecución final.

Este criterio establece consistencia observable, pero no prescribe mecanismos técnicos como hashes, commits o identificadores de builds.

---

## 12. Limitaciones

### C11 — Limitaciones concretas

La ubicación destinada a limitaciones según A08 debe documentar las limitaciones relevantes conocidas del trabajo.

Deben incluirse aquellas limitaciones que afecten significativamente:

* interpretación de resultados;
* alcance de las conclusiones;
* reproducibilidad;
* disponibilidad de evidencia;
* integridad de la entrega.

Las limitaciones documentadas deben corresponder a problemas o restricciones reales identificados durante el trabajo.

No deben inventarse limitaciones genéricas únicamente para satisfacer formalmente este criterio.

Cuando exista un fallo, faltante o dependencia externa que impida verificar una parte del trabajo, debe declararse como tal en lugar de presentar esa parte como completamente validada.

---

## 13. Identificación de integrantes

### C12 — Uso de las entradas de nombres

Las entradas `Nombres 1` y `Nombres 2` exigidas por A11 deben utilizarse para identificar a los integrantes/autores del paper.

Los valores proporcionados mediante dichas entradas deben reflejarse en el documento resultante.

No se exige:

* afiliación;
* correo electrónico;
* identificadores académicos;
* orden específico;
* formato visual determinado;
* información personal adicional.

---

## 14. Relación entre pregunta y conclusión

### C13 — La conclusión responde a la pregunta explicativa

La conclusión debe responder explícitamente a la pregunta explicativa establecida conforme a C02.

La respuesta debe derivarse de la evidencia y resultados presentados previamente en el trabajo.

Debe existir trazabilidad conceptual:

`pregunta explicativa → resultados → interpretación → conclusión`

La conclusión no debe:

* introducir resultados experimentales nuevos;
* responder una pregunta diferente sin justificar el cambio;
* presentar como demostrado aquello que la evidencia disponible no permite sostener.

Este criterio no determina cuál debe ser la respuesta a la pregunta explicativa.

---

## 15. Condición de aceptación de contenido

El cumplimiento de `01_acceptance_artifacts.md` demuestra únicamente que existen los artefactos necesarios para evaluar la entrega.

Para satisfacer este documento, dichos artefactos deben además cumplir los criterios C01–C03 y C05–C15 aprobados anteriormente.

El criterio C04 queda expresamente excluido.

La ausencia de C04 es deliberada: las decisiones técnicas específicas sobre modelo y SHAP pertenecen respectivamente a `04_modelo.md` y `05_shap.md`.

El cumplimiento de este documento tampoco sustituye las obligaciones operativas que se definirán en `03_agent_acceptance_behavior.md`.
