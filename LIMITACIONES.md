# Limitaciones

Versión resumida; la sección 4 del paper las desarrolla.

1. **Tres imágenes no generalizan.** Casos ilustrativos elegidos por diseño, no una muestra.
2. **El modelo no puede acertar en dos de las tres entradas**: `capybara` no existe en
   ImageNet-1k. Parte del error es limitación de vocabulario, no necesariamente un atajo.
   Ambas explicaciones son compatibles con los datos.
3. **Hábitat correlacionado con la especie** por construcción: un mapa que resalte el agua es
   ambiguo entre «atajo» y «señal legítimamente correlacionada».
4. **SHAP Partition es aproximado** y depende del baseline (`blur(128,128)`). Solo se
   comprobó estabilidad; no se aplicaron los tests de aleatorización de Adebayo et al.
5. **Asociación, no causalidad.**
6. **Fallo detectado y corregido:** en la primera ejecución IMG-03 reutilizaba el archivo de
   IMG-02 por colisión de nombres, produciendo probabilidades idénticas. Corregido y
   reejecutado; las cifras entregadas son de la corrida corregida.
