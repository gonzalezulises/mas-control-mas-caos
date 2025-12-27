# Apéndice A: Criterios de Readiness por Tipo de Iniciativa

<!-- block: uso -->

Este apéndice contiene criterios operativos para evaluar iniciativas antes de autorizar ejecución. No son checklists universales. Son puntos de partida que cada organización debe calibrar según su contexto, tolerancia al riesgo y capacidad de absorber fracaso. Un criterio que es umbral mínimo para una organización con historial de fracasos puede ser excesivo para otra con capacidad probada de corrección en vuelo. La calibración es responsabilidad del comité que opera el gate, no del libro.

La calibración correcta depende de tres factores que varían por organización. El primero es la tolerancia al riesgo: una empresa en industria regulada con riesgo reputacional alto necesita umbrales más estrictos que una startup en fase de experimentación. El segundo es la capacidad de corrección: una organización con ciclos de feedback rápidos y cultura de iteración puede operar con menos validación previa porque corrige en vuelo. El tercero es el costo de oportunidad: en mercados donde la velocidad es ventaja competitiva decisiva, criterios excesivamente estrictos destruyen más valor del que protegen.

El rango saludable de tasa de rechazo es entre diez y treinta por ciento. Por debajo del diez por ciento, el gate probablemente aprueba todo y no está filtrando. Por encima del treinta por ciento, el gate probablemente está bloqueando iniciativas legítimas y generará bypass. Si la tasa de rechazo está consistentemente fuera de este rango, la calibración requiere ajuste.

Cada criterio está formulado con cuatro propiedades. Observabilidad significa que un tercero puede verificar el cumplimiento sin depender de interpretación subjetiva. Umbral explícito significa que hay un número, porcentaje, duración o condición binaria que separa cumplimiento de incumplimiento. Consecuencia predefinida significa que el incumplimiento dispara un veredicto específico, no una conversación. Anti-gaming significa que el criterio anticipa cómo alguien podría cumplirlo mecánicamente sin cumplir el espíritu, y cierra esa vía.

Los criterios de GO deben cumplirse todos para autorizar ejecución. Los criterios de RECHAZO automático disparan veredicto negativo si cualquiera de ellos aplica, sin importar cuántos criterios de GO se cumplan. Las señales de CONDICIONAL requieren resolución específica antes de poder emitir veredicto de GO; no impiden el avance permanentemente, pero sí lo suspenden hasta que la condición se resuelva.

<!-- block: transformacion_tecnologica -->

Las transformaciones tecnológicas de alcance organizacional tienen el mayor índice de fracaso documentado y el mayor costo de abandono tardío. El sesgo típico es subestimar dependencias con sistemas legacy, sobreestimar adopción por usuarios finales, y confundir prueba técnica exitosa con validación de negocio.

El primer criterio de GO es validación de supuestos de adopción. Es observable cuando existe documentación de prueba con usuarios reales del segmento objetivo, no usuarios internos ni early adopters autoseleccionados. El umbral es mínimo noventa días de prueba con al menos treinta usuarios que representan el perfil típico, no el perfil entusiasta. La consecuencia de incumplimiento es rechazo automático. El anti-gaming requiere que la prueba incluya métricas de retención y uso sostenido, no solo registro inicial o uso durante período de novedad.

El segundo criterio de GO es mapeo completo de dependencias técnicas. Es observable cuando existe documento de arquitectura firmado por CTO o CIO que identifica todas las integraciones con sistemas existentes. El umbral es cien por ciento de integraciones identificadas, testeadas en ambiente de staging, con plan de rollback documentado para cada una. La consecuencia de incumplimiento es condicional hasta completar. El anti-gaming requiere que el testeo incluya escenarios de falla y degradación, no solo happy path.

El tercer criterio de GO es cuantificación de costo de abandono por fase. Es observable cuando existe análisis financiero que muestra el costo acumulado si la iniciativa se abandona al final de cada fase. El umbral es que el costo de abandono en ninguna fase supere el quince por ciento del presupuesto anual del área afectada sin aprobación explícita de CFO. La consecuencia de incumplimiento es escalamiento a comité ejecutivo. El anti-gaming requiere que el análisis incluya costos de oportunidad y deuda técnica generada, no solo inversión directa.

El cuarto criterio de GO es disponibilidad de capacidad técnica interna. Es observable cuando existe asignación nominal de recursos técnicos con disponibilidad confirmada por sus gerentes de línea. El umbral es que al menos el sesenta por ciento de la capacidad técnica crítica sea interna, no dependiente de consultores externos. La consecuencia de incumplimiento es condicional hasta asegurar capacidad o reducir alcance. El anti-gaming requiere que la confirmación de disponibilidad incluya compromisos de dedicación porcentual, no solo nombres en lista.

El quinto criterio de GO es patrocinador con autoridad sobre todas las áreas afectadas. Es observable cuando el sponsor tiene reporte directo o línea de escalamiento clara hacia todas las unidades que deben adoptar el cambio. El umbral es autoridad formal documentada en organigrama o mandato de directorio. La consecuencia de incumplimiento es rechazo hasta definir governance cross-funcional. El anti-gaming requiere que la autoridad incluya capacidad de asignar recursos, no solo capacidad de convocar reuniones.

Los criterios de rechazo automático para transformación tecnológica son tres. Primero, ausencia de caso de negocio con supuestos explícitos y validados independientemente. Segundo, dependencia crítica de proveedor único sin plan B documentado. Tercero, timeline que requiere ejecución paralela de más de tres workstreams interdependientes sin program management dedicado.

Las señales de condicional son cuatro. Primera, cambio regulatorio pendiente que afecta el alcance o los requisitos técnicos. Segunda, reestructuración organizacional en curso que afecta las líneas de reporte del sponsor. Tercera, sistema legacy crítico en proceso de migración o estabilización. Cuarta, rotación reciente de CTO, CIO o equivalente funcional.

<!-- block: expansion_geografica -->

Las expansiones a nuevos mercados geográficos subestiman sistemáticamente diferencias regulatorias, culturales y operativas. El patrón típico es proyectar el modelo del mercado de origen sin validar supuestos locales, resultando en costos de adaptación que superan las proyecciones originales.

El primer criterio de GO es validación de demanda en mercado objetivo. Es observable cuando existen datos de investigación de mercado primaria realizada en el territorio objetivo, no extrapolación de mercados similares. El umbral es investigación con al menos doscientos respondentes del segmento objetivo, con preguntas sobre intención de compra y willingness to pay. La consecuencia de incumplimiento es rechazo automático. El anti-gaming requiere que la investigación sea realizada por tercero independiente, no por el equipo que propone la expansión.

El segundo criterio de GO es mapeo regulatorio completo. Es observable cuando existe dictamen legal de firma con presencia local que identifica todos los requisitos regulatorios para operar. El umbral es cobertura de cien por ciento de requisitos identificados con plan de cumplimiento y timeline. La consecuencia de incumplimiento es condicional hasta completar. El anti-gaming requiere que el dictamen incluya requisitos de facto, no solo requisitos formales, incluyendo prácticas de mercado que sin ser legales son esperadas.

El tercer criterio de GO es modelo operativo localizado. Es observable cuando existe documentación de cómo se adaptará el modelo operativo a las condiciones locales, incluyendo supply chain, talento, y canales. El umbral es que cada componente operativo tenga proveedor o socio local identificado y validado. La consecuencia de incumplimiento es condicional hasta completar. El anti-gaming requiere que la validación incluya visita física y due diligence, no solo intercambio de correos.

El cuarto criterio de GO es break-even timeline realista. Es observable cuando el modelo financiero muestra el período hasta break-even bajo escenarios conservador, base y optimista. El umbral es que el escenario conservador alcance break-even antes de agotar el presupuesto asignado más reserva del veinte por ciento. La consecuencia de incumplimiento es rechazo o reducción de alcance. El anti-gaming requiere que el escenario conservador use supuestos de penetración validados en mercados similares, no proyecciones del equipo comercial.

Los criterios de rechazo automático para expansión geográfica son tres. Primero, ausencia de liderazgo local confirmado con experiencia verificable en el mercado objetivo. Segundo, requisitos regulatorios que implican cambios en producto o servicio core sin plan de adaptación costeado. Tercero, competidor dominante con más del sesenta por ciento de market share y ventajas estructurales de escala.

Las señales de condicional son tres. Primera, elecciones nacionales o cambio de gobierno esperado en los próximos doce meses. Segunda, tipo de cambio con volatilidad superior al quince por ciento en los últimos veinticuatro meses. Tercera, dependencia de socio local exclusivo sin alternativas identificadas.

<!-- block: fusiones_adquisiciones -->

Las fusiones y adquisiciones tienen documentación abundante de fracaso, particularmente en captura de sinergias proyectadas. El sesgo típico es sobreestimar sinergias de ingresos, subestimar costos de integración, y asumir retención de talento clave que frecuentemente no se materializa.

El primer criterio de GO es due diligence técnico y operativo completo. Es observable cuando existe reporte de due diligence realizado por tercero independiente que cubre tecnología, operaciones, contratos y contingencias. El umbral es cobertura de cien por ciento de las áreas identificadas en term sheet con hallazgos clasificados por materialidad. La consecuencia de incumplimiento es rechazo automático. El anti-gaming requiere que el tercero no tenga relación previa con ninguna de las partes y que su fee no dependa del cierre de la transacción.

El segundo criterio de GO es plan de integración con owner asignado. Es observable cuando existe plan de integración post-cierre con responsable nominal para cada workstream y milestones específicos. El umbral es que el plan cubra los primeros ciento ochenta días con nivel de detalle semanal y el primer año con nivel de detalle mensual. La consecuencia de incumplimiento es condicional hasta completar. El anti-gaming requiere que los owners tengan confirmación escrita de disponibilidad y que el plan incluya métricas de éxito verificables, no solo actividades.

El tercer criterio de GO es validación de supuestos de sinergia. Es observable cuando cada sinergia proyectada tiene metodología de cálculo documentada y responsable de captura asignado. El umbral es que al menos el setenta por ciento del valor de sinergias tenga validación independiente o precedente en transacciones comparables. La consecuencia de incumplimiento es ajuste de valoración o rechazo. El anti-gaming requiere que las sinergias de ingresos tengan descuento del cincuenta por ciento respecto a estimación inicial, reflejando la tasa histórica de captura.

El cuarto criterio de GO es retención de talento crítico asegurada. Es observable cuando existen acuerdos de retención firmados con las personas identificadas como críticas para la operación post-cierre. El umbral es retención asegurada por al menos veinticuatro meses para el cien por ciento del talento clasificado como crítico. La consecuencia de incumplimiento es condicional hasta asegurar o recalcular valor sin ese talento. El anti-gaming requiere que la clasificación de talento crítico sea validada por tercero, no solo por el management del target que tiene incentivo a inflar su importancia.

Los criterios de rechazo automático para M&A son cuatro. Primero, ausencia de tesis de inversión escrita que explique por qué esta combinación crea valor que no existe por separado. Segundo, contingencias legales o regulatorias materiales sin cuantificar o sin provisión. Tercero, dependencia de sinergias de ingresos para justificar más del cuarenta por ciento del precio pagado. Cuarto, oposición del CEO o CFO del adquirente documentada en actas.

Las señales de condicional son tres. Primera, investigación regulatoria activa sobre el target. Segunda, rotación de más del veinte por ciento del equipo ejecutivo del target en los últimos doce meses. Tercera, cliente que representa más del treinta por ciento de los ingresos del target sin contrato de largo plazo.

<!-- block: plataformas_datos_ia -->

Las iniciativas de plataformas de datos e inteligencia artificial combinan riesgo técnico con riesgo organizacional. El patrón típico es subestimar la deuda de datos existente, sobreestimar la capacidad de la organización para actuar sobre insights, y confundir pruebas de concepto exitosas con capacidad de operación a escala.

El primer criterio de GO es calidad de datos de entrada validada. Es observable cuando existe assessment de calidad de datos que cubre completitud, consistencia, temporalidad y linaje de las fuentes requeridas. El umbral es que al menos el ochenta por ciento de los campos críticos cumplan estándares de calidad definidos, con plan de remediación para el resto. La consecuencia de incumplimiento es rechazo automático. El anti-gaming requiere que el assessment sea realizado sobre datos de producción, no sobre muestras limpias, y que incluya análisis de drift temporal.

El segundo criterio de GO es caso de uso con valor de negocio cuantificado. Es observable cuando existe documentación que conecta las capacidades técnicas propuestas con decisiones de negocio específicas y su impacto económico. El umbral es que el caso de uso esté validado por el líder de negocio que tomará las decisiones, con compromiso escrito de uso. La consecuencia de incumplimiento es condicional hasta obtener compromiso. El anti-gaming requiere que el compromiso incluya consecuencias para el líder de negocio si no usa los outputs, no solo intención declarada.

El tercer criterio de GO es governance de datos y modelos definida. Es observable cuando existe política aprobada que define ownership, acceso, retención, y ciclo de vida de datos y modelos. El umbral es cobertura de cien por ciento de los datos y modelos en scope con roles asignados. La consecuencia de incumplimiento es condicional hasta completar. El anti-gaming requiere que la política incluya proceso de enforcement y consecuencias por incumplimiento, no solo definiciones.

El cuarto criterio de GO es capacidad de MLOps verificada. Es observable cuando existe infraestructura operativa para monitoreo, reentrenamiento y rollback de modelos en producción. El umbral es capacidad demostrada de detectar degradación de modelo y ejecutar rollback en menos de cuatro horas. La consecuencia de incumplimiento es condicional hasta demostrar capacidad. El anti-gaming requiere que la demostración sea en ambiente de producción o staging equivalente, no en ambiente de desarrollo.

El quinto criterio de GO es evaluación de riesgo ético y reputacional. Es observable cuando existe assessment de riesgos de sesgo, privacidad y uso indebido con mitigaciones documentadas. El umbral es que todos los riesgos clasificados como altos tengan mitigación implementada antes de producción. La consecuencia de incumplimiento es rechazo hasta implementar mitigaciones. El anti-gaming requiere que el assessment sea revisado por función legal o compliance, no solo por el equipo técnico.

Los criterios de rechazo automático para plataformas de datos e IA son tres. Primero, ausencia de owner de negocio identificado que usará los outputs para tomar decisiones. Segundo, datos de entrenamiento con problemas de licenciamiento, privacidad o consentimiento no resueltos. Tercero, modelo que afecta decisiones sobre personas sin explicabilidad documentada.

Las señales de condicional son tres. Primera, regulación de IA pendiente en jurisdicciones donde opera la organización. Segunda, incidente reciente de privacidad o seguridad de datos en la organización. Tercera, rotación del Chief Data Officer o equivalente en los últimos seis meses.

<!-- block: lanzamiento_producto -->

Los lanzamientos de producto o servicio tienen el riesgo de consumir recursos en algo que el mercado no quiere. El patrón típico es confundir validación de concepto con validación de demanda, y asumir que la ejecución resolverá problemas de product-market fit.

El primer criterio de GO es validación de problema con clientes reales. Es observable cuando existe documentación de investigación cualitativa con clientes del segmento objetivo que confirma la existencia y urgencia del problema que el producto resuelve. El umbral es al menos veinte entrevistas en profundidad con clientes que experimentan el problema activamente. La consecuencia de incumplimiento es rechazo automático. El anti-gaming requiere que las entrevistas sean realizadas por personas distintas a quienes diseñaron el producto, para evitar sesgo de confirmación.

El segundo criterio de GO es willingness to pay validado. Es observable cuando existen datos de investigación cuantitativa o pruebas de precio que confirman que los clientes pagarán el precio propuesto. El umbral es que al menos el cuarenta por ciento de los clientes del segmento objetivo declaren intención de compra al precio propuesto. La consecuencia de incumplimiento es condicional hasta ajustar precio o propuesta de valor. El anti-gaming requiere que la prueba de precio incluya transacción real o compromiso vinculante, no solo intención declarada.

El tercer criterio de GO es unit economics positivos proyectados. Es observable cuando existe modelo financiero que muestra el margen por unidad bajo supuestos de costo y precio validados. El umbral es margen de contribución positivo a partir del mes dieciocho de operación bajo escenario conservador. La consecuencia de incumplimiento es rechazo o rediseño de modelo. El anti-gaming requiere que los supuestos de costo incluyan todos los costos variables, incluyendo soporte y churn, no solo costos de producción.

El cuarto criterio de GO es capacidad de distribución confirmada. Es observable cuando existe acuerdo o validación con los canales de distribución necesarios para alcanzar el segmento objetivo. El umbral es capacidad de distribución suficiente para alcanzar el punto de break-even en el timeline proyectado. La consecuencia de incumplimiento es condicional hasta asegurar distribución. El anti-gaming requiere que la validación de canal incluya términos económicos, no solo disposición general.

Los criterios de rechazo automático para lanzamiento de producto son tres. Primero, ausencia de diferenciación clara respecto a alternativas existentes que los clientes ya usan. Segundo, dependencia de cambio de comportamiento masivo del cliente sin evidencia de que ese cambio es posible. Tercero, canibalización proyectada de productos existentes sin análisis de impacto neto.

Las señales de condicional son tres. Primera, competidor preparando lanzamiento similar según inteligencia de mercado. Segunda, cambio regulatorio que afecta la categoría de producto en proceso legislativo. Tercera, dependencia de tecnología o componente con proveedor único.

<!-- block: reestructuracion_organizacional -->

Las reestructuraciones organizacionales tienen alto costo humano y frecuentemente no logran los objetivos declarados. El patrón típico es subestimar el impacto en productividad durante la transición, sobreestimar la velocidad de estabilización, y no medir resultados post-implementación.

El primer criterio de GO es diagnóstico de problema organizacional documentado. Es observable cuando existe análisis que identifica el problema específico que la reestructuración resolverá, con evidencia de que el problema es estructural y no de personas. El umbral es diagnóstico validado por tercero independiente o por análisis cuantitativo de métricas organizacionales. La consecuencia de incumplimiento es rechazo hasta completar diagnóstico. El anti-gaming requiere que el diagnóstico considere alternativas a la reestructuración y explique por qué fueron descartadas.

El segundo criterio de GO es diseño organizacional objetivo definido. Es observable cuando existe organigrama futuro con roles, responsabilidades y líneas de reporte claramente definidos. El umbral es cobertura de cien por ciento de las posiciones afectadas con definición de rol completa. La consecuencia de incumplimiento es condicional hasta completar. El anti-gaming requiere que el diseño incluya sizing de cada función basado en análisis de carga de trabajo, no solo en headcount actual.

El tercer criterio de GO es plan de transición con mitigación de riesgos. Es observable cuando existe plan que cubre comunicación, movimientos de personas, y continuidad operativa durante la transición. El umbral es que cada riesgo identificado tenga mitigación asignada con responsable y timeline. La consecuencia de incumplimiento es condicional hasta completar. El anti-gaming requiere que el plan incluya escenario de rollback si la transición genera disrupción operativa crítica.

El cuarto criterio de GO es métricas de éxito definidas pre-implementación. Es observable cuando existen métricas específicas que se medirán para evaluar si la reestructuración logró sus objetivos. El umbral es baseline medido antes de la reestructuración y target cuantificado para cada métrica. La consecuencia de incumplimiento es condicional hasta definir. El anti-gaming requiere que las métricas incluyan indicadores de productividad y clima, no solo reducción de costos.

Los criterios de rechazo automático para reestructuración organizacional son tres. Primero, ausencia de sponsor con autoridad sobre todas las áreas afectadas. Segundo, reestructuración motivada principalmente por reducción de costos sin diagnóstico de problema estructural. Tercero, tercera reestructuración en cinco años sin evaluación de por qué las anteriores no funcionaron.

Las señales de condicional son tres. Primera, proceso de negociación sindical activo. Segunda, rotación de CEO, CHRO o equivalente en los últimos seis meses. Tercera, fusión o adquisición en curso que afecta el perímetro de la reestructuración.

<!-- block: transformacion_cultural -->

Las transformaciones culturales son las iniciativas con mayor tasa de fracaso y menor capacidad de medición. El patrón típico es declarar intención de cambio cultural, lanzar comunicaciones y programas, y asumir que el cambio ocurrirá porque fue anunciado. La realidad es que la cultura cambia como resultado de cambios en sistemas, incentivos y comportamientos visibles de líderes, no como resultado de iniciativas de cambio cultural.

El primer criterio de GO es definición operativa de la cultura objetivo. Es observable cuando existe documentación que describe la cultura deseada en términos de comportamientos observables, no de valores abstractos. El umbral es que cada dimensión cultural tenga al menos tres comportamientos específicos que cualquier observador pueda verificar. La consecuencia de incumplimiento es rechazo automático. El anti-gaming requiere que los comportamientos sean verificables por terceros, no autoreportados, y que incluyan comportamientos de líderes, no solo de empleados.

El segundo criterio de GO es diagnóstico de barreras estructurales. Es observable cuando existe análisis de qué sistemas, procesos, incentivos y estructuras actuales producen la cultura actual y resistirán el cambio. El umbral es identificación de al menos cinco barreras estructurales con plan de intervención para cada una. La consecuencia de incumplimiento es condicional hasta completar. El anti-gaming requiere que el diagnóstico incluya entrevistas con empleados de diferentes niveles, no solo perspectiva de liderazgo.

El tercer criterio de GO es sponsor con autoridad para modificar sistemas. Es observable cuando el sponsor tiene capacidad de cambiar los sistemas de compensación, promoción, evaluación y reconocimiento que refuerzan la cultura actual. El umbral es autoridad documentada sobre al menos el ochenta por ciento de los sistemas que afectan comportamiento. La consecuencia de incumplimiento es rechazo hasta asegurar sponsor adecuado. El anti-gaming requiere que la autoridad incluya presupuesto para modificar sistemas, no solo autoridad nominal.

El cuarto criterio de GO es timeline realista. Es observable cuando el plan reconoce que el cambio cultural toma años, no meses, y tiene hitos intermedios verificables. El umbral es plan a tres años mínimo con métricas de progreso cada seis meses. La consecuencia de incumplimiento es condicional hasta ajustar timeline. El anti-gaming requiere que los hitos intermedios midan cambio de comportamiento, no actividades de comunicación o capacitación.

Los criterios de rechazo automático para transformación cultural son tres. Primero, ausencia de comportamiento visible del CEO que modele la cultura deseada. Segundo, inconsistencia entre cultura declarada y sistema de incentivos vigente. Tercero, iniciativa de cambio cultural lanzada en los últimos tres años que no logró sus objetivos, sin análisis de por qué.

Las señales de condicional son tres. Primera, proceso de reducción de personal en curso que contradice mensajes de la transformación. Segunda, rotación de más del veinte por ciento del equipo ejecutivo en los últimos doce meses. Tercera, adquisición o fusión en proceso que introducirá cultura diferente.

<!-- block: calibracion -->

Los umbrales presentados en este apéndice son puntos de partida, no estándares universales. Una organización con alta tolerancia al riesgo y capacidad probada de corrección en vuelo puede operar con umbrales más laxos. Una organización con historial de fracasos o baja capacidad de absorber pérdidas debería operar con umbrales más estrictos.

La calibración correcta no es la más estricta posible. Es la que produce una tasa de rechazo entre diez y treinta por ciento. Por debajo del diez por ciento, los criterios probablemente son tan laxos que no filtran nada relevante. Por encima del treinta por ciento, los criterios probablemente son tan estrictos que bloquean iniciativas que deberían avanzar, generando frustración y eventualmente bypass del gate.

El proceso de calibración debería ocurrir anualmente, usando como input los veredictos del año anterior. Las iniciativas que recibieron GO y fracasaron indican que los criterios fueron insuficientes para detectar riesgo. Las iniciativas que recibieron RECHAZO y cuyo análisis posterior muestra que habrían funcionado indican que los criterios fueron excesivos. El objetivo es minimizar ambos tipos de error, sabiendo que nunca serán cero.

<!-- block: manipulacion -->

Los criterios más sofisticados pueden ser manipulados por sponsors suficientemente motivados. Las señales de que un criterio se cumple mecánicamente sin cumplir el espíritu son predecibles y deben monitorearse.

La primera señal es documentación perfecta sin sustancia. El sponsor produce todos los documentos requeridos, pero los contenidos son genéricos, copiados de otras iniciativas, o producidos por consultores externos sin validación interna. La documentación existe pero no refleja trabajo real de análisis.

La segunda señal es usuarios de validación autoseleccionados. La validación de adopción se hace con usuarios que el sponsor eligió porque son entusiastas del proyecto, no porque representan al usuario típico. Las métricas de adopción son altas pero no predicen adopción real post-lanzamiento.

La tercera señal es supuestos validados por la misma persona que los propuso. El análisis financiero muestra retorno positivo, pero los supuestos fueron definidos por el equipo del proyecto y validados por el mismo equipo, sin challenge independiente.

La cuarta señal es mitigaciones de riesgo que existen en papel pero no tienen recursos asignados. El plan de riesgos lista mitigaciones para todos los riesgos identificados, pero ninguna mitigación tiene presupuesto, responsable con tiempo asignado, o métricas de efectividad.

La quinta señal es cumplimiento de umbral justo por encima del mínimo. Cuando múltiples criterios se cumplen exactamente con el mínimo requerido, sugiere que el equipo trabajó para alcanzar el umbral, no para resolver el problema subyacente.

El comité que opera el gate debe desarrollar sensibilidad para estas señales. El criterio codificado es necesario pero no suficiente. El juicio experto sobre la calidad del cumplimiento sigue siendo irreemplazable. El criterio protege al experto dándole base institucional para cuestionar; no lo reemplaza.
