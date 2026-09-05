# Criterios de aceptación — Comportamiento del agente

## 1. Propósito

Este documento define el comportamiento obligatorio del agente encargado de ejecutar, integrar, comprobar y entregar el ejercicio.

Los artefactos requeridos se definen en `01_acceptance_artifacts.md` y sus requisitos de contenido en `02_acceptance_content.md`.

Las decisiones técnicas específicas correspondientes al modelo y a SHAP quedan fuera del alcance de este agente y serán definidas respectivamente en:

* `04_modelo.md`;
* `05_shap.md`.

El agente debe producir una entrega evaluable y trazable sin sustituir las responsabilidades asignadas a esos componentes.

---

## 2. Frontera de responsabilidad

El agente puede:

* integrar artefactos recibidos;
* utilizar resultados proporcionados por los componentes responsables;
* organizar el paper;
* relacionar evidencia con texto y figuras;
* comprobar consistencia;
* comprobar referencias;
* compilar LaTeX;
* documentar limitaciones;
* mantener trazabilidad;
* verificar los criterios de aceptación aplicables.

El agente no debe tomar unilateralmente decisiones técnicas que correspondan a `04_modelo.md` o `05_shap.md`.

Cuando una decisión, dato o corrección dependa de dichos componentes, el agente debe utilizar la información proporcionada por ellos, solicitar o identificar el faltante mediante el flujo correspondiente, o declarar que la información no puede verificarse.

---

## 3. Verificación inicial

### B01 — Verificar entradas antes de comenzar

Antes de construir o integrar el paper, el agente debe comprobar qué artefactos, datos e información requeridos están disponibles.

Debe identificar:

* entradas disponibles;
* entradas requeridas pero ausentes;
* dependencias externas conocidas;
* artefactos provenientes de otros responsables;
* impedimentos conocidos para continuar.

El agente no debe asumir silenciosamente que un artefacto existe cuando no puede localizarlo.

Cuando un faltante no impida continuar con otras partes independientes del trabajo, el agente puede continuar parcialmente, pero debe conservar el estado del faltante.

---

## 4. Prohibición de inventar información

### B02 — No inventar resultados ni evidencia

El agente no debe fabricar información para completar la entrega.

Esto incluye, entre otros:

* resultados experimentales;
* métricas;
* ejecuciones;
* figuras;
* referencias;
* contenido atribuido a referencias;
* logs;
* evidencia de validaciones que no ocurrieron;
* datos provenientes del modelo;
* resultados provenientes de SHAP;
* información técnica desconocida;
* estados de cumplimiento no comprobados.

Cuando la información necesaria no esté disponible, debe tratarse conforme a B12 en lugar de inferirse o inventarse.

---

## 5. Compilación

### B03 — Compilar y comprobar el LaTeX

El agente debe compilar el fuente LaTeX correspondiente al estado final de la entrega.

Debe comprobar que la compilación produce el PDF que será entregado y que dicho PDF puede abrirse y utilizarse para evaluación.

La relación que debe comprobarse es:

`fuente final → compilación → PDF final`

Una modificación posterior del fuente que pueda afectar el documento requiere volver a comprobar el resultado correspondiente.

Este requisito no exige conservar un log independiente de compilación como artefacto final, de acuerdo con la exclusión A06 de `01_acceptance_artifacts.md`.

---

## 6. Manejo de errores

### B04 — Resolver errores antes de declarar terminado

Cuando una comprobación obligatoria falle, el agente debe intentar corregir el problema si la corrección pertenece a su ámbito de responsabilidad.

No debe declarar como satisfecha una comprobación que continúa fallando.

Si el problema pertenece a `04_modelo.md`, `05_shap.md` u otro responsable externo, el agente no debe modificar unilateralmente ese componente para forzar el cumplimiento.

En ese caso debe:

1. identificar el problema;
2. identificar la dependencia o responsable correspondiente cuando sea posible;
3. conservar la evidencia relevante;
4. reflejar el problema en la evaluación final si permanece sin resolver.

---

## 7. Handoffs

### B05 — Handoffs explícitos

Cuando el trabajo sea transferido entre agentes, personas o componentes, debe existir un handoff identificable.

El handoff debe conservar contexto suficiente para que el siguiente responsable pueda continuar el trabajo y para que posteriormente pueda reconstruirse qué fue transferido.

No deben generarse handoffs artificiales cuando no exista una transferencia real.

### B11 — Contenido mínimo de un handoff

Cada handoff debe identificar, como mínimo:

* origen o responsable que entrega;
* destino o siguiente responsable, cuando sea conocido;
* objetivo de la transferencia;
* artefactos o información transferidos;
* pendientes conocidos;
* limitaciones o fallos relevantes conocidos en el momento de la transferencia.

No se exige una herramienta, formato de archivo o sistema específico para representar el handoff.

El contenido debe ser suficientemente explícito para evitar que el siguiente responsable tenga que reconstruir información crítica mediante suposiciones.

---

## 8. Registro de prompts

### B06 — Conservar prompts relevantes

El agente debe conservar los prompts o instrucciones que hayan influido materialmente en la producción del entregable.

El registro debe priorizar interacciones que hayan provocado o condicionado:

* decisiones relevantes;
* generación o modificación sustancial de contenido;
* integración de artefactos;
* correcciones relevantes;
* interpretación de requisitos;
* handoffs;
* cambios materiales del entregable.

No es obligatorio registrar como elemento independiente cada interacción trivial que no tenga impacto material en el trabajo.

La trazabilidad no debe reducirse únicamente a prompts: debe complementarse con los handoffs exigidos cuando ocurran transferencias de responsabilidad.

---

## 9. Verificación de referencias

### B07 — Verificar referencias antes de aceptarlas

Antes de considerar una referencia válida para la entrega, el agente debe comprobar razonablemente:

* que la fuente existe;
* que corresponde con la referencia declarada;
* que los enlaces proporcionados conducen al recurso esperado cuando corresponda;
* que la fuente se utiliza para respaldar contenido identificable;
* que el contenido atribuido a la fuente es compatible con lo que esta realmente sostiene.

Una referencia no debe incorporarse únicamente porque trate un tema similar al del paper.

La comprobación debe respetar A05 y C08.

El agente no debe inventar referencias ni atribuir a una fuente contenido que no pueda comprobar.

---

## 10. Artefactos provenientes de modelo y SHAP

### B08 — No modificar silenciosamente artefactos externos

Los resultados o artefactos recibidos de los responsables de `04_modelo.md` y `05_shap.md` no deben modificarse sustancialmente para hacerlos coincidir con la narrativa del paper.

El agente puede realizar operaciones necesarias para su integración o presentación siempre que estas no alteren el significado de los resultados.

Cuando una transformación pueda afectar la interpretación del resultado, no debe tratarse como un simple cambio de formato.

El agente no debe:

* modificar resultados para obtener una conclusión conveniente;
* sustituir resultados por otros no proporcionados;
* ocultar resultados incompatibles con la narrativa;
* atribuir al componente externo una decisión que no haya sido proporcionada;
* modificar decisiones técnicas pertenecientes a `04` o `05` para solucionar unilateralmente un problema del paper.

---

## 11. Información faltante

### B12 — Tratamiento explícito de información requerida pero faltante

Cuando falte información necesaria para cumplir o verificar un criterio, el agente debe identificar:

* qué información falta;
* para qué criterio o parte del trabajo es necesaria;
* cuál es su procedencia esperada, cuando pueda determinarse;
* qué parte del trabajo queda afectada.

El agente no debe sustituir información desconocida mediante una suposición presentada como hecho.

Cuando el faltante corresponda al modelo o a SHAP, debe asociarse respectivamente con `04_modelo.md` o `05_shap.md` en lugar de resolverlo mediante una decisión técnica unilateral.

La ausencia de información suficiente puede producir un estado `NO VERIFICABLE` conforme a B16.

---

## 12. Orden mínimo de validación

### B13 — Dependencia lógica del proceso

El proceso debe respetar, como mínimo, la siguiente dependencia lógica:

`verificar entradas → realizar/integrar trabajo permitido → generar artefactos → compilar → comprobar consistencia → validar criterios → declarar estado final`

Este orden representa dependencias entre etapas, no una prohibición de iterar.

El agente puede:

* regresar a etapas anteriores;
* corregir problemas;
* regenerar artefactos;
* recompilar;
* repetir comprobaciones.

Cuando una modificación posterior invalide potencialmente una comprobación anterior, dicha comprobación debe repetirse sobre el nuevo estado.

La evaluación final debe realizarse sobre los artefactos que efectivamente serán entregados.

---

## 13. Trazabilidad de cambios

### B14 — Registro de cambios relevantes

Los cambios materiales realizados durante el proceso deben conservar trazabilidad suficiente para determinar:

* qué cambió;
* por qué cambió;
* qué artefacto o parte del trabajo resultó afectada.

Se consideran especialmente relevantes los cambios que afecten:

* contenido sustantivo;
* evidencia;
* resultados integrados;
* figuras;
* referencias;
* estructura significativa del paper;
* conclusiones;
* cumplimiento de criterios;
* resolución de un fallo previamente identificado.

No es necesario registrar individualmente cambios puramente tipográficos o editoriales que no alteren materialmente el contenido, evidencia o interpretación.

---

## 14. Conservación de fallos relevantes

### B15 — No ocultar fallos

El agente no debe eliminar, disfrazar o dejar de reportar un fallo relevante únicamente para conseguir que la entrega parezca cumplir los criterios.

Cuando un problema conocido no pueda resolverse, debe permanecer reflejado en el estado de la entrega o en sus limitaciones cuando corresponda.

El agente no debe:

* eliminar silenciosamente una parte fallida para aparentar completitud;
* sustituir evidencia problemática por evidencia inventada;
* ignorar una comprobación fallida;
* declarar resuelto un problema que continúa presente.

Un problema que haya sido corregido satisfactoriamente no necesita permanecer clasificado como fallo actual.

La trazabilidad de un cambio material asociado a su resolución se rige por B14.

---

## 15. Comprobación final

### B09 — Comprobar los criterios antes de terminar

Antes de declarar terminado el ejercicio, el agente debe realizar una comprobación final contra todos los criterios obligatorios aplicables definidos en:

* `01_acceptance_artifacts.md`;
* `02_acceptance_content.md`;
* `03_agent_acceptance_behavior.md`;
* `04_modelo.md`;
* `05_shap.md`.

La comprobación debe realizarse sobre el estado final de los artefactos entregados.

Para `04_modelo.md` y `05_shap.md`, esta obligación no concede al agente autoridad para sustituir las decisiones o responsabilidades técnicas asignadas a sus respectivos responsables.

Cuando un criterio dependa de evidencia que el agente no puede comprobar, debe utilizar el estado correspondiente definido en B16.

---

## 16. Estado por criterio

### B16 — Clasificación explícita de cumplimiento

Cada criterio obligatorio aplicable debe clasificarse durante la comprobación final utilizando uno de los siguientes estados:

* `CUMPLE`
* `NO CUMPLE`
* `NO VERIFICABLE`

### `CUMPLE`

Existe evidencia suficiente para comprobar que el criterio se satisface.

### `NO CUMPLE`

Existe evidencia suficiente para determinar que el criterio no se satisface.

### `NO VERIFICABLE`

No existe evidencia suficiente para determinar objetivamente si el criterio se satisface.

`NO VERIFICABLE` no equivale a `CUMPLE`.

La ausencia de evidencia necesaria no debe transformarse automáticamente en una afirmación de cumplimiento.

---

## 17. Fallos parciales

### B10 — Estado explícito ante fallos parciales

Si uno o más criterios obligatorios no pueden satisfacerse o verificarse, el agente debe declararlo explícitamente.

El agente puede continuar produciendo y entregando aquellas partes que sí sean válidas cuando resulte posible hacerlo sin falsear el estado general.

Debe quedar identificable:

* qué criterio está afectado;
* cuál es su estado;
* cuál es el problema conocido;
* qué parte de la entrega resulta afectada;
* si existe una dependencia externa pendiente.

La existencia de un PDF, código, figuras u otros artefactos no implica por sí sola que la entrega esté completamente aceptada.

---

## 18. Condición de terminación

### B17 — Condición para declarar la entrega completamente aceptada

El agente solo puede declarar la entrega **completamente aceptada** cuando todos los criterios obligatorios aplicables se encuentren en estado:

`CUMPLE`

Si existe al menos un criterio obligatorio en estado:

`NO CUMPLE`

o:

`NO VERIFICABLE`

el agente puede entregar los artefactos disponibles, pero debe declarar la entrega como:

`INCOMPLETA / NO COMPLETAMENTE ACEPTADA`

Debe además identificar los criterios responsables de dicho estado.

Un fallo procedente de `04_modelo.md` o `05_shap.md` no autoriza al agente a modificar unilateralmente esos componentes para convertir el estado en `CUMPLE`.

---

## 19. Resultado de la validación

La validación final debe permitir reconstruir, como mínimo, la relación:

`criterio → estado → evidencia o motivo`

Para criterios satisfechos debe existir evidencia suficiente para justificar `CUMPLE`.

Para criterios fallidos debe indicarse la razón de `NO CUMPLE`.

Para criterios que no puedan evaluarse debe identificarse qué evidencia o información ausente produce `NO VERIFICABLE`.

Una afirmación global como “todo está correcto” no sustituye la comprobación individual de los criterios.

---

## 20. Regla final de actuación

El agente debe priorizar una entrega verificable sobre una apariencia de completitud.

Ante información desconocida:

`declarar faltante > inventar`

Ante evidencia insuficiente:

`NO VERIFICABLE > asumir CUMPLE`

Ante un fallo conocido:

`reportar fallo > ocultar fallo`

Ante una decisión perteneciente a `04_modelo.md` o `05_shap.md`:

`respetar frontera de responsabilidad > decidir unilateralmente`

Ante una modificación del estado final:

`volver a comprobar lo afectado > reutilizar una validación obsoleta`
