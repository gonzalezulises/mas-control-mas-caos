# Apéndice D: Diseño y anti-patrones del gate

El Apéndice A contiene criterios para evaluar iniciativas por tipo. Este apéndice complementa con principios para diseñar el mecanismo evaluador. Ambos son necesarios: criterios correctos aplicados por gate capturado no producen filtro; gate bien diseñado con criterios vagos tampoco.

Lo que sigue no es estándar certificable. Son derivaciones lógicas de lo que haría que un mecanismo de límite funcione bajo las presiones que este libro describe. El lector que diseña un gate puede usar los principios como heurísticas de verificación. El lector que audita un gate existente puede usar los anti-patrones y señales como instrumentos de diagnóstico. En ambos casos, la pregunta es función real, no cumplimiento formal.

<!-- break -->

## Principios de diseño

Estos no son checklist de cumplimiento. Son heurísticas de diseño. Un gate puede violar alguna y funcionar; un gate que viola varias probablemente no funciona. El diseñador debe entender la lógica detrás de cada principio para saber cuándo puede flexibilizar y cuándo no.

**Principio 1: Independencia estructural del operador.** El operador del gate no puede depender jerárquica, económica o políticamente del sponsor cuyas iniciativas evalúa. La independencia nominal no sobrevive a la dependencia real. Si el operador reporta al sponsor, necesita al sponsor para su próximo rol, o su compensación depende del sponsor, el gate está estructuralmente capturado antes de operar. La independencia debe ser arquitectónica: a quién reporta el operador, quién evalúa su desempeño, de dónde viene su compensación. La declaración de independencia sin arquitectura que la soporte es promesa que no sobrevive al primer veredicto incómodo.

**Principio 2: Anterioridad del criterio.** El criterio de evaluación existe y es conocido antes de que la iniciativa llegue al gate. Si el criterio se define cuando llega la iniciativa, el criterio se adaptará a la iniciativa. El criterio posterior es racionalización, no filtro. Esto implica que los criterios deben estar codificados, publicados, y ser modificables solo mediante proceso formal que no coincide con la evaluación de ninguna iniciativa específica. Un criterio que cambia para acomodar una iniciativa particular ha dejado de ser criterio.

**Principio 3: Veredicto con consecuencia institucional.** El veredicto del gate cambia el estatus institucional de la iniciativa; no produce recomendación que otro órgano puede ignorar. Un gate que recomienda no es límite; es asesor. La recomendación transfiere la decisión a quien recibe la recomendación. El límite genuino retiene la decisión. El veredicto RECHAZO debe significar que la iniciativa no puede avanzar a ejecución sin nuevo sometimiento formal, no que se sugiere no avanzar. La diferencia entre sugerencia y veredicto es la diferencia entre ceremonia y governance.

**Principio 4: Inmutabilidad del registro.** El registro de veredictos no puede modificarse después de emitido; las correcciones se agregan como enmiendas, no como ediciones. El registro mutable permite reescribir historia. Si el veredicto fue GO y la iniciativa fracasó, la tentación de ajustar el registro es estructural. Si el veredicto fue RECHAZO y el sponsor tiene poder, la presión por suavizar el registro es predecible. El registro inmutable es la memoria institucional que permite aprender de veredictos pasados. El sistema de registro debe tener controles técnicos de inmutabilidad, no solo políticas de no-edición que dependen de voluntad individual.

**Principio 5: Protección estructural del operador.** La protección del operador contra represalias por veredictos negativos es estructural, no discrecional. Mandato fijo con duración definida, no renovable a discreción del evaluado. Proceso de remoción formal que requiere causa documentada, no decisión administrativa. La promesa de protección no sobrevive al primer veredicto que incomoda al poder. Solo la arquitectura que hace costoso remover al operador produce protección real. El operador que puede ser removido fácilmente por quienes evalúa no es independiente; está en período de prueba permanente.

**Principio 6: Carga de prueba en el sponsor.** La iniciativa debe demostrar readiness; el gate no debe demostrar que la iniciativa no está ready. Si el gate debe justificar cada rechazo mientras el sponsor solo debe presentar la iniciativa, la asimetría de esfuerzo favorece la aprobación. Rechazar requiere argumento; aprobar requiere solo ausencia de objeción. Esta asimetría ceremonializa el gate. El formato de sometimiento debe requerir evidencia de readiness según criterios publicados. La ausencia de evidencia es causa suficiente de rechazo; el gate no necesita probar que la evidencia faltante era necesaria. La carga de prueba invertida es el mecanismo más sutil de captura.

<!-- break -->

## Anti-patrones del gate

Un anti-patrón es una configuración que parece razonable pero produce disfunción predecible. Cada anti-patrón tiene lógica que lo hace atractivo y consecuencia que lo hace destructivo.

**Anti-patrón 1: Composición nombrada por patrocinadores.** Los operadores del gate son nombrados por el comité ejecutivo que patrocina las iniciativas más grandes. Parece razonable: queremos gente senior con credibilidad, y el comité ejecutivo sabe quién tiene el perfil. Falla porque los operadores deben su posición a quienes evalúan. La gratitud institucional es real aunque no se articule. La captura está arquitectada desde el nombramiento. Un gate cuyos operadores son nombrados por los sponsors es gate de los sponsors, independientemente del mandato formal.

**Anti-patrón 2: Convocatoria por demanda.** El gate no tiene calendario fijo; se convoca cuando hay iniciativas que evaluar. Parece razonable: no queremos burocracia innecesaria; nos reunimos cuando hay trabajo. Falla porque el sponsor controla cuándo su iniciativa es evaluada. Las iniciativas urgentes llegan cuando el gate no está convocado y la presión por decidir rápido no admite espera. El gate termina convocándose reactivamente, sin tiempo de preparación, bajo condiciones que el sponsor determina. El calendario fijo es fricción deliberada que protege la calidad de la deliberación.

**Anti-patrón 3: Veredictos reabribles.** Un veredicto RECHAZO puede reabrirse si el sponsor presenta información adicional, sin proceso formal de re-sometimiento. Parece razonable: a veces hay malentendidos; no queremos rigidez excesiva. Falla porque el RECHAZO se convierte en rechazado por ahora. El sponsor aprende que la persistencia produce aprobación. El rechazo deja de ser veredicto y se convierte en round de negociación. El proceso formal de re-sometimiento, con documentación de qué cambió y por qué el cambio resuelve las objeciones, es lo que distingue corrección genuina de persistencia exitosa.

**Anti-patrón 4: Ausencia de métricas de operación.** El gate no mide su propia operación: tasa de rechazo, tiempo de evaluación, distribución de veredictos por sponsor, correlación entre veredicto y resultado posterior. Parece razonable: no somos burocracia; somos governance. No necesitamos medirnos a nosotros mismos. Falla porque sin métricas, la ceremonialización es indetectable. El gate puede operar años con 98% de aprobación sin que nadie lo note. Las métricas no son para reportar a un superior; son para que el gate mismo detecte su propia deriva.

**Anti-patrón 5: Override informal.** Iniciativas avanzan a ejecución mientras se resuelve el proceso de gate, o con aprobación condicional que se formalizará después. Parece razonable: no podemos detener el negocio por proceso; avancemos y regularicemos. Falla porque el override informal se vuelve el proceso real. Una vez que la iniciativa está en ejecución, el gate solo puede ratificar lo que ya ocurrió. Rechazar post-facto tiene costo político máximo y beneficio mínimo. El gate formal se vuelve registro retrospectivo de decisiones ya tomadas. El override informal es el mecanismo más común de neutralización de gates.

**Anti-patrón 6: Criterios negociables por iniciativa.** Los criterios de readiness se adaptan al contexto de cada iniciativa durante la evaluación. Parece razonable: cada iniciativa es diferente; necesitamos flexibilidad para casos únicos. Falla porque si el criterio se adapta a la iniciativa, toda iniciativa cumple su criterio adaptado. El filtro desaparece. La flexibilidad legítima es tener criterios diferenciados por tipo de iniciativa, definidos antes de la evaluación. La flexibilidad ilegítima es ajustar los criterios durante la evaluación para que la iniciativa presente los pase.

<!-- break -->

## Señales tempranas de captura

La captura del gate no ocurre en un momento; se instala gradualmente. Estas señales son observables antes de que la captura sea completa. El ejecutivo que las detecta tiene ventana de intervención.

**Señal 1: Tasa de aprobación superior al 95% sostenida.** Observar la proporción de veredictos GO sobre total de iniciativas evaluadas, medida sobre ventana de doce meses o más. Una tasa consistentemente superior al 95% indica que o las iniciativas que llegan están perfectamente preparadas, lo cual es improbable dado lo que este libro describe sobre cómo se preparan las iniciativas, o el gate no está filtrando. La acción es auditar muestra de iniciativas aprobadas contra criterios declarados. Si los criterios se cumplían marginalmente o con interpretación generosa, el gate está ceremonializado.

**Señal 2: Tiempo promedio de evaluación inferior a tres días.** Observar el tiempo desde sometimiento hasta veredicto. Un tiempo consistentemente inferior a tres días para iniciativas significativas indica que no hay escrutinio sustantivo. La evaluación es revisión superficial, no challenge genuino. La acción es verificar si los operadores leen la documentación completa, si hacen preguntas de seguimiento, si deliberan antes de votar o si el voto es inmediato.

**Señal 3: Correlación sponsor-veredicto.** Observar si iniciativas de ciertos sponsors siempre reciben GO mientras iniciativas de otros sponsors reciben escrutinio diferente. Esta correlación indica que el gate trata diferente según quién presenta, no según qué se presenta. Es captura selectiva: funciona como límite para algunos, como trámite para otros. La acción es análisis estadístico de veredictos por sponsor. Si la varianza es significativa y no se explica por calidad diferencial de preparación, hay captura.

**Señal 4: Anticipación de veredictos.** Observar si los sponsors saben qué veredicto recibirán antes de la deliberación formal. Si el resultado se comenta antes de la sesión, la deliberación formal es teatro. La decisión real ocurre en conversaciones previas entre operadores y sponsors. La acción es verificar si hay comunicación entre operadores y sponsors antes de la sesión. Si la hay, reforzar protocolo de no-contacto previo a deliberación.

**Señal 5: Consulta previa informal.** Observar si los operadores consultan informalmente con sponsors sobre cómo enfocar la evaluación antes de la sesión formal. Esto indica que el operador está alineando su posición con el sponsor en lugar de evaluar independientemente. Es captura activa en proceso, no captura consumada. La intervención debe ser inmediata sobre composición del gate.

<!-- break -->

## Indicadores de falsa estabilidad

Un gate puede parecer estable porque existe, se reúne, produce veredictos y tiene registro documentado, mientras es funcionalmente inoperante. Estos indicadores revelan que la estabilidad es aparente.

**Indicador 1: Ausencia en conversaciones de governance.** En reuniones de comité ejecutivo, board, o planificación estratégica, el gate no se menciona como factor en decisiones. Nadie dice el gate evaluará esto o esperemos el veredicto del gate. El gate no es parte del proceso real de decisión. Existe en paralelo, no integrado. Las decisiones reales ocurren en espacios donde el gate no tiene presencia.

**Indicador 2: Preparación post-facto.** Los sponsors preparan documentación para el gate solo después de haber decidido internamente que van a ejecutar. El gate es trámite de legitimación, no punto de decisión. La iniciativa llega al gate con recursos ya asignados, equipos ya formados, comunicaciones ya enviadas. El veredicto RECHAZO en esas condiciones tiene costo político que nadie quiere pagar.

**Indicador 3: Registro no consultado.** Cuando llega iniciativa similar a una previamente evaluada, nadie consulta qué veredicto tuvo la anterior ni por qué. El gate no genera aprendizaje institucional. Cada evaluación es evento aislado sin memoria. Los errores que causaron rechazos previos se repiten porque nadie revisa el historial.

**Indicador 4: Criterios desconocidos por sponsors.** Los sponsors no conocen los criterios de evaluación hasta que llegan al gate. Preparan documentación genérica esperando descubrir qué se les pedirá. Los criterios no están operando como filtro anticipado que orienta la preparación. El gate sorprende en lugar de guiar. Esto indica que los criterios existen formalmente pero no se usan operativamente.

**Indicador 5: Ausencia de rechazos memorables.** Nadie en la organización puede citar una iniciativa significativa que el gate haya rechazado. O el gate no rechaza iniciativas que importan, o los rechazos son de iniciativas marginales que nadie nota. En ambos casos, el gate no está ejerciendo límite sobre lo que importa. Un gate que solo rechaza lo insignificante no es límite; es filtro de ruido.

<!-- break -->

Este apéndice no certifica gates. Provee instrumentos para diseñarlos con menor probabilidad de captura y diagnosticarlos cuando la captura comienza a instalarse.

Un gate bien diseñado no garantiza que funcione. Las presiones de captura son constantes y creativas. Un gate mal diseñado garantiza que no funcione, porque la arquitectura misma facilita la captura. La diferencia entre ambos es si el diseño dificulta la captura o la invita.

El lector que diseña un gate puede usar los principios como heurísticas de verificación: cada violación es señal de alerta que requiere justificación explícita. El lector que audita un gate existente puede usar los anti-patrones y señales como checklist de diagnóstico: cada patrón observado es evidencia de que el gate puede no estar funcionando. En ambos casos, lo que importa no es cumplimiento formal sino función real. ¿El gate produce veredictos que cambian comportamiento, o produce registros que legitiman decisiones ya tomadas? ¿El RECHAZO tiene consecuencias operativas, o es obstáculo temporal que la persistencia supera?

La diferencia entre límite genuino y ceremonia de governance es observable. Este apéndice intenta hacer esa observación sistemática.

<!-- break -->

| Categoría | Elemento | Señal de alerta |
|-----------|----------|-----------------|
| Principio violado | Independencia | Operador reporta a sponsor o depende de él para siguiente rol |
| Principio violado | Anterioridad | Criterios se definen o modifican durante evaluación |
| Principio violado | Consecuencia | Veredicto produce recomendación, no decisión vinculante |
| Anti-patrón | Override informal | Iniciativas avanzan mientras se resuelve proceso |
| Anti-patrón | Veredictos reabribles | RECHAZO se revierte con información adicional sin re-sometimiento |
| Anti-patrón | Sin métricas | Gate no mide tasa de aprobación ni tiempo de evaluación |
| Captura temprana | Tasa >95% | Aprobación casi universal sostenida 12+ meses |
| Captura temprana | Correlación | Ciertos sponsors siempre pasan |
| Captura temprana | Anticipación | Veredicto conocido antes de deliberación |
| Falsa estabilidad | Ausencia | Gate no se menciona en decisiones reales |
| Falsa estabilidad | Post-facto | Documentación se prepara después de decidir ejecutar |
| Falsa estabilidad | Sin memoria | Nadie consulta veredictos previos |
