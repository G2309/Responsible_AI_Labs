# Criterios de aceptación — Artefactos y evidencias

## 1. Propósito

Este documento define los artefactos y evidencias que deben existir para que la entrega pueda considerarse evaluable.

Los requisitos de contenido de estos artefactos se definen separadamente en `02_acceptance_content.md`, mientras que el comportamiento y las comprobaciones exigidas al agente ejecutor se definen en `03_agent_acceptance_behavior.md`.

Los criterios aquí definidos deben mantenerse agnósticos respecto al modelo de clasificación, arquitectura, framework, dataset, versión de SHAP y método explicativo utilizado.

---

## 2. Fuente LaTeX principal

**A01 — Fuente LaTeX disponible**

Debe existir un archivo fuente principal LaTeX identificable correspondiente al paper.

El archivo principal debe permitir identificar inequívocamente cuál es el punto de entrada del documento.

No se exige un nombre de archivo concreto salvo que posteriormente se establezca como requisito externo.

### Evidencia verificable

* Existe un archivo `.tex` principal.
* El archivo es legible.
* Puede identificarse inequívocamente como fuente principal del paper.

---

## 3. PDF resultante

**A02 — PDF compilado**

Debe existir un PDF correspondiente al paper entregado.

### Evidencia verificable

* Existe el archivo PDF.
* El archivo puede abrirse.
* El documento es legible.

La existencia de evidencia adicional o logs específicos de compilación no constituye un requisito de este documento.

---

## 4. Artefacto experimental

**A03 — Código o notebook de la parte experimental**

Debe existir el código, notebook u otro artefacto ejecutable utilizado para obtener los resultados experimentales incorporados al paper.

El criterio no prescribe:

* lenguaje de programación;
* framework;
* arquitectura del modelo;
* modelo utilizado;
* dataset;
* versión de SHAP;
* método explicativo;
* formato notebook frente a scripts;
* implementación técnica de SHAP.

### Evidencia verificable

Debe poder identificarse al menos un artefacto ejecutable como responsable de producir los resultados experimentales utilizados en la entrega.

---

## 5. Figuras

**A04 — Figuras como archivos independientes**

Las figuras utilizadas por el paper deben existir como archivos dentro del paquete entregado y no únicamente como contenido embebido en el PDF final.

### Evidencia verificable

* Los archivos gráficos utilizados por el fuente LaTeX están presentes.
* Las dependencias gráficas locales referenciadas por el documento no están ausentes.

No se prescribe formato gráfico, resolución, estilo ni cantidad de figuras.

---

## 6. Referencias y fuentes externas

**A05 — Evidencia bibliográfica y fuentes utilizadas**

Las dependencias bibliográficas utilizadas por el paper deben formar parte de la entrega cuando sean archivos locales.

Cuando una referencia dependa de un recurso externo accesible mediante URL, el enlace debe ser coherente con la referencia y conducir a un recurso accesible correspondiente a la fuente indicada.

No se exige un código HTTP concreto como condición universal de aceptación; se requiere que el recurso pueda resolverse razonablemente hasta el contenido correspondiente.

Las referencias no deben incorporarse únicamente por compartir temática general con el ejercicio: deben tener un uso identificable dentro del trabajo.

### Evidencia verificable

Debe ser posible comprobar:

* existencia de las dependencias bibliográficas locales utilizadas;
* correspondencia entre una URL y la fuente que declara representar;
* accesibilidad razonable de los recursos enlazados;
* existencia de un uso identificable de las referencias dentro del paper.

La evaluación semántica de si una fuente respalda correctamente una afirmación concreta se desarrolla en `02_acceptance_content.md`.

---

## 7. Trazabilidad del proceso

**A07 — Prompts y handoffs**

Debe existir evidencia persistente de las interacciones relevantes utilizadas durante la producción asistida del trabajo.

La trazabilidad debe contemplar:

* prompts relevantes;
* handoffs entre agentes, personas o componentes cuando dichos handoffs ocurran;
* evidencia suficiente para reconocer que una parte del trabajo fue transferida para continuar su procesamiento o integración.

No se prescribe en este documento un formato concreto para almacenar esta información.

Tampoco se exige crear handoffs artificiales cuando el flujo de trabajo no los requiera.

Los requisitos sobre qué información debe conservar cada prompt o handoff podrán establecerse en `02_acceptance_content.md` y las obligaciones operativas del agente en `03_agent_acceptance_behavior.md`.

---

## 8. Limitaciones y faltantes

**A08 — Evidencia explícita de limitaciones**

Debe existir una ubicación identificable dentro de los artefactos entregados donde puedan documentarse las limitaciones, fallos conocidos, elementos no reproducibles o faltantes relevantes del ejercicio.

No se exige que esta evidencia constituya necesariamente un archivo Markdown independiente.

Puede integrarse en un artefacto existente siempre que su ubicación sea identificable.

Este requisito no debe confundirse con los archivos:

* `01_acceptance_artifacts.md`;
* `02_acceptance_content.md`;
* `03_agent_acceptance_behavior.md`.

Estos tres archivos constituyen la especificación de aceptación, mientras que A08 se refiere a las limitaciones de la ejecución realizada posteriormente.

---

## 9. Entorno y dependencias

**A09 — Evidencia del entorno y dependencias**

Debe existir un artefacto o especificación que permita identificar suficientemente el entorno y las dependencias necesarias para reproducir las partes ejecutables de la entrega.

Este criterio no prescribe:

* gestor de paquetes;
* formato del archivo;
* sistema operativo;
* hardware;
* framework;
* mecanismo de aislamiento;
* uso de contenedores;
* versiones arbitrarias no justificadas.

La información concreta exigible dependerá de las necesidades reales de los artefactos ejecutables.

---

## 10. Identificación de integrantes

**A10 — Identificación de integrantes**

El fuente LaTeX debe disponer de una ubicación explícita destinada a identificar a los integrantes/autores del trabajo.

No se prescribe formato visual, orden, afiliación ni información personal adicional.

### Evidencia verificable

Debe poder localizarse inequívocamente en el fuente LaTeX dónde se proporciona la identificación de los integrantes.

---

## 11. Entradas para nombres

**A11 — Dos entradas de nombres**

El fuente LaTeX debe disponer de dos entradas claramente identificables destinadas a ser completadas posteriormente:

* `Nombres 1`
* `Nombres 2`

Estas entradas corresponden a los nombres de los integrantes.

El criterio establece la existencia de las dos entradas, pero no prescribe el mecanismo LaTeX concreto mediante el cual deben implementarse.

---

## 12. Exclusión explícita

**A06 — Evidencia separada de compilación**

No se exige como artefacto independiente un log específico de compilación u otra evidencia separada destinada exclusivamente a demostrar que ocurrió la compilación.

Esta exclusión no impide que `03_agent_acceptance_behavior.md` establezca posteriormente obligaciones relacionadas con compilar y comprobar el documento durante la ejecución.

---

## 13. Condición de evaluabilidad de artefactos

Para satisfacer este documento deben estar presentes los artefactos y evidencias aprobados en A01–A05 y A07–A11.

La existencia de estos artefactos únicamente establece que la entrega puede ser evaluada.

No implica por sí sola que:

* su contenido sea correcto;
* los resultados sean válidos;
* las afirmaciones estén respaldadas;
* el experimento sea reproducible;
* las referencias sean semánticamente adecuadas;
* el PDF corresponda correctamente al estado final de los fuentes;
* los resultados experimentales correspondan a las figuras presentadas.

Estas propiedades deberán establecerse mediante los criterios aprobados posteriormente en `02_acceptance_content.md` y `03_agent_acceptance_behavior.md`.
