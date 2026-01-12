# Apéndice F: Casos de Referencia {-}

## Nota metodológica {- .unlisted}

Los casos que siguen no son implementaciones del Decisión Readiness Gate. El DRG, como se ha establecido en este libro, es una propuesta conceptual sin casos de implementación documentados.

Lo que sí ofrecen estos casos es evidencia indirecta. Son reinterpretaciones de eventos públicos bajo el lente de las ocho capacidades. La pregunta no es "¿funcionó el DRG?" sino "¿qué capacidades estaban presentes o ausentes, y cómo se relaciona eso con el resultado?"

El lector puede verificar la lógica contra las fuentes citadas. Si la interpretación es correcta, debería ser posible predecir los modos de falla observados a partir del estado de las capacidades. Si no lo es, el framework necesita revisión.

---

## Caso 1: Toyota y el Sistema Andon {- .unlisted}

### Resumen {- .unlisted}

Toyota desarrolló un sistema donde cualquier trabajador de línea puede detener la producción completa al detectar una anomalía. Este mecanismo, conocido como Andon, representa un límite externo arquitectado en el diseño físico del sistema productivo: el poder de detener no depende de autorización jerárquica ni de deliberación política.

Durante décadas, este sistema funcionó como filtro efectivo de defectos. En 2009-2010, la crisis de aceleradores atascados reveló que algunas capacidades se habían erosionado sin que el sistema lo detectara. El caso ilustra tanto el funcionamiento del límite como sus modos de falla.

### Contexto {- .unlisted}

El Sistema de Producción Toyota emergió en las décadas de 1950-1970 como respuesta a restricciones específicas: capital limitado, mercado pequeño, necesidad de flexibilidad. Taiichi Ohno y sus colaboradores desarrollaron prácticas que minimizaban inventario y maximizaban detección temprana de problemas.

El Andon no fue diseñado como herramienta de governance. Fue diseñado como herramienta de producción. Pero su efecto es el de un límite externo: cuando un trabajador tira de la cuerda, el sistema se detiene. No hay comité que delibere. No hay escalación que autorice. El límite está en el diseño.

La filosofía subyacente, codificada en documentos internos y prácticas de entrenamiento, establece que detener la línea ante la duda es correcto; dejar pasar un defecto es incorrecto. El costo de una parada es visible e inmediato. El costo de un defecto que llega al cliente es mayor pero diferido. El sistema resuelve está asimetría haciendo que la parada no tenga costo personal para quien la activa.

### Estado de las capacidades {- .unlisted}

**Capacidad 1: Delimitación explícita — PRESENTE**

El criterio de activación es claro: cualquier anomalía, cualquier duda, cualquier desviación del estándar. No hay ambigüedad sobre qué dispara el límite. El umbral es bajo deliberadamente: es preferible parar por una falsa alarma que dejar pasar un defecto real.

**Capacidad 2: Criterio codificado — PRESENTE**

La regla "si hay duda, detener" existe antes del evento específico. No se evalúa caso por caso si está anomalía particular merece parada. El criterio es binario y previo.

**Capacidad 3: Gate vinculante — PRESENTE**

La línea se detiene físicamente. No es una recomendación ni una alerta que alguien puede ignorar. El veredicto tiene consecuencia inmediata y automática.

**Capacidad 4: Protección del NO — PRESENTE**

El trabajador que detiene la línea no enfrenta consecuencia negativa. La norma cultural, reforzada por décadas de práctica, es que parar ante la duda es comportamiento esperado. Las historias internas celebran a quienes detuvieron la línea, no a quienes la mantuvieron corriendo pese a dudas.

**Capacidad 5: Separación patrocinio/veredicto — PRESENTE**

El trabajador de línea no tiene interés financiero personal en que la producción continúe. Su compensación no depende de unidades producidas. No hay conflicto de interés estructural.

**Capacidad 6: Registro irreversible — PARCIAL**

Las paradas se documentan, pero el registro no siempre se preserva a largo plazo. La documentación sirve para análisis inmediato (qué causó la parada, cómo se resolvió) más que para auditoría histórica.

**Capacidad 7: Aprendizaje procedural — PRESENTE**

El proceso Kaizen incorpora las lecciones de cada parada. Los problemas detectados alimentan mejoras en el proceso, el diseño, o el entrenamiento. El sistema aprende.

**Capacidad 8: Revisión periódica — PRESENTE**

Los estándares de trabajo se revisan continuamente. No hay criterio fijo que permanezca inmutable por años. La evolución es parte del diseño.

### La erosión de 2009-2010 {- .unlisted}

Entre 2009 y 2010, Toyota enfrentó una crisis que resultó en el recall de más de 8 millones de vehículos por problemas de aceleración involuntaria. Las investigaciones posteriores revelaron que ingenieros internos habían documentado preocupaciones sobre el diseño del pedal y la interacción con los tapetes, pero estas preocupaciones no activaron el mismo tipo de respuesta que una anomalía en la línea de producción.

¿Qué capacidades fallaron?

**Delimitación explícita se estrechó.** El Andon funcionaba para problemas de manufactura. Los problemas de diseño de componentes, especialmente de proveedores externos, no tenían el mismo mecanismo de activación. La pregunta "¿qué pasa por el límite?" había cambiado sin que el sistema lo formalizara.

**Registro irreversible falló.** Las preocupaciones de ingenieros internos fueron documentadas pero no preservadas de manera que activara escalación. Los reportes existían, pero no había mecanismo que los convirtiera en señal de alarma institucional.

**Separación patrocinio/veredicto se debilitó.** A medida que Toyota creció y se globalizó, las presiones de volumen y costo se hicieron más intensas. Los equipos que evaluaban problemas de proveedores tenían incentivos mixtos que no existían en el piso de producción original.

### Implicación {- .unlisted}

El Andon funciona cuando las ocho capacidades están arquitectadas en el sistema y cuando el alcance del límite coincide con el alcance del riesgo. La crisis de 2009-2010 muestra que un límite efectivo puede erosionarse gradualmente cuando:

- El tipo de problema cambia (de manufactura a diseño de proveedores)
- El registro no escala con la complejidad de la organización
- Las presiones competitivas introducen conflictos de interés que antes no existían

Para el lector: ¿El alcance de sus mecanismos de límite coincide con el alcance de sus riesgos actuales? ¿O hay categorías de decisión que escapan al escrutinio porque el límite fue diseñado para un contexto diferente?

---

## Caso 2: Johnson & Johnson y el Credo como criterio previo {- .unlisted}

### Resumen {- .unlisted}

En septiembre de 1982, siete personas murieron en Chicago después de consumir cápsulas de Tylenol adulteradas con cianuro. Johnson & Johnson retiró 31 millones de frascos del mercado en 24 horas, asumiendo un costo de más de 100 millones de dólares, sin saber aún si el problema era de manufactura o de sabotaje externo.

Esta decisión se ha presentado frecuentemente como ejemplo de liderazgo ético. Lo que importa para este análisis es diferente: la decisión fue posible porque existía un criterio codificado previo al evento. El Credo de J&J, escrito en 1943, establecía una jerarquía explícita de responsabilidades: primero los consumidores, después los empleados, luego las comunidades, finalmente los accionistas.

### Contexto {- .unlisted}

Robert Wood Johnson, hijo del fundador, escribió el Credo en 1943, casi cuatro décadas antes de la crisis del Tylenol. El documento no era aspiracional ni decorativo. Era operativo: se usaba en decisiones de negocio, en entrenamiento de ejecutivos, en evaluación de opciones estratégicas.

James Burke, CEO durante la crisis de 1982, había liderado años antes una serie de sesiones con ejecutivos senior para debatir si el Credo seguía siendo relevante. El resultado fue reafirmación del documento con ajustes menores. El ejercicio tuvo un efecto importante: cuando llegó la crisis, el criterio no solo existía sino que había sido discutido, cuestionado y revalidado por el equipo que tendría que aplicarlo.

La noche del 30 de septiembre de 1982, cuando llegaron los primeros reportes de muertes, Burke y su equipo enfrentaron una decisión con información incompleta. No sabían si el problema era de manufactura (lo cual implicaría recall masivo) o de sabotaje local (lo cual implicaría respuesta focalizada). Elegir mal en cualquier dirección tenía consecuencias graves.

### Estado de las capacidades {- .unlisted}

**Capacidad 1: Delimitación explícita — PRESENTE**

El Credo era claro sobre qué decisiones requerían aplicar la jerarquía de responsabilidades: cualquier decisión que afectara al consumidor. No había ambigüedad sobre si está crisis calificaba.

**Capacidad 2: Criterio codificado — PRESENTE**

La jerarquía del Credo existía desde 1943. No se escribió mirando la crisis del Tylenol. No fue juicio ad-hoc. El criterio era: ante duda, proteger al consumidor aunque el costo sea alto.

**Capacidad 3: Gate vinculante — PARCIAL**

No existía un gate formal con proceso estructurado. El Credo funcionaba como principio orientador, no como checkpoint institucional. La decisión de retirar los productos fue tomada por el equipo ejecutivo, no por un mecanismo independiente.

**Capacidad 4: Protección del NO — PRESENTE**

Burke tenía autoridad para actuar sin aprobación del Board en situación de crisis. La estructura de J&J (descentralizada, con empresas operativas autónomas) significaba que la decisión de Tylenol no requería consenso corporativo amplio. El CEO podía decir "retiramos todo" sin costo político interno.

**Capacidad 5: Separación patrocinio/veredicto — PARCIAL**

El mismo equipo ejecutivo que manejaba Tylenol tomó la decisión. No había separación estructural entre quienes se beneficiaban del producto y quienes evaluaban el riesgo. Lo que existía era un criterio previo que subordinaba el interés del producto al interés del consumidor.

**Capacidad 6: Registro irreversible — PRESENTE (de facto)**

La decisión de retirar 31 millones de frascos fue pública e inmediata. No había posibilidad de reescribir la historia o escalar gradualmente. El registro fue irreversible por la naturaleza del acto, no por diseño documental.

**Capacidad 7: Aprendizaje procedural — PRESENTE**

La crisis resultó en innovación concreta: el packaging tamper-evident (con sello de seguridad) se convirtió en estándar de la industria. J&J no solo respondió a la crisis sino que cambió la categoría completa.

**Capacidad 8: Revisión periódica — PARCIAL**

El Credo se mantenía pero no evolucionaba formalmente. Las sesiones de Burke en los años previos fueron excepción, no práctica institucionalizada.

### La erosión posterior {- .unlisted}

Si el Credo funcionó en 1982, ¿por qué no funcionó igualmente bien en crisis posteriores?

En 2010, J&J enfrentó problemas con implantes de cadera DePuy que causaron fallas y requerían cirugías de revisión. En 2018-2020, demandas masivas alegaron que J&J sabía desde hace décadas que su talco para bebés contenía asbesto. En ambos casos, la respuesta fue más lenta, más defensiva, y más costosa en términos de confianza pública.

¿Qué cambió?

**Delimitación explícita se estrechó.** El Credo hablaba de "consumidores", pero ¿los pacientes de implantes de cadera eran consumidores en el mismo sentido que quienes compraban Tylenol? La adquisición de empresas de dispositivos médicos (DePuy fue adquirida en 1998) trajo categorías de producto donde la relación con el usuario final era diferente.

**Separación patrocinio/veredicto se debilitó.** A medida que J&J creció y se diversificó, los equipos que evaluaban riesgo estaban más cercanos a los equipos que generaban ingresos. La estructura descentralizada que en 1982 permitió decisión rápida, en contextos posteriores diluyó responsabilidad.

**Criterio codificado no evolucionó.** El Credo de 1943 no se actualizó para contextos de dispositivos médicos implantables o productos de uso prolongado donde el daño emerge lentamente.

### Implicación {- .unlisted}

El criterio codificado funciona cuando está arquitectado antes de la crisis y cuando la organización lo trata como límite operativo, no como aspiración cultural. La efectividad del Credo en 1982 dependió de:

- Existencia previa del criterio (décadas antes)
- Revalidación reciente por el equipo que lo aplicaría
- Autoridad concentrada para actuar sin deliberación extensa
- Naturaleza del problema (agudo, visible, atribuible)

Las crisis posteriores tenían características diferentes: problemas crónicos, atribución difusa, múltiples niveles de intermediación entre J&J y el usuario. El mismo criterio, sin evolución, no produjo el mismo resultado.

Para el lector: ¿Su criterio de decisión fue diseñado para el tipo de problema que enfrenta hoy? ¿O está aplicando un criterio de otra época a un contexto diferente?

---

## Caso 3: Boeing 737 MAX — Erosión de límites existentes {- .unlisted}

### Resumen {- .unlisted}

Entre octubre de 2018 y marzo de 2019, dos aviones Boeing 737 MAX se estrellaron en condiciones similares, matando a 346 personas. Las investigaciones revelaron que un sistema de control de vuelo (MCAS) activado por un único sensor podía forzar la nariz del avión hacia abajo repetidamente, y que los pilotos no habían sido informados adecuadamente sobre este sistema ni entrenados para desactivarlo.

Lo que hace relevante este caso no es la falla técnica. Es la erosión de límites que permitió que la falla llegara a producción. Boeing tenía un límite externo funcional: la certificación independiente de la FAA. Entre 2005 y 2018, ese límite fue erosionado gradualmente hasta volverse ceremonial.

### Contexto {- .unlisted}

La relación entre Boeing y la FAA tiene historia larga. Durante décadas, la FAA certificaba aeronaves mediante revisión independiente de diseños, pruebas y documentación. Este proceso era lento y costoso, pero funcionaba como límite externo genuino.

En 2005, la FAA expandió el programa Organization Designation Authorization (ODA), que permitía a los fabricantes designar a sus propios empleados como representantes autorizados para certificar aspectos del diseño. La lógica era eficiencia: Boeing conocía sus aviones mejor que nadie; permitirles certificar aspectos rutinarios liberaba recursos de la FAA para supervisión de alto nivel.

El problema fue la pendiente resbaladiza. Lo que comenzó como delegación de aspectos rutinarios se expandió gradualmente. Para cuando el 737 MAX entró en desarrollo, Boeing tenía autoridad para determinar qué aspectos requerían revisión directa de la FAA y cuáles podían ser auto-certificados.

### Estado de las capacidades {- .unlisted}

**Capacidad 1: Delimitación explícita — EROSIONADA**

¿Qué requería revisión independiente de la FAA? La respuesta cambió gradualmente. Al inicio del ODA, la FAA definía qué era "rutinario" y qué requería escrutinio. Con el tiempo, Boeing adquirió influencia sobre esa definición. El MCAS fue clasificado internamente como sistema menor que no requería certificación extensiva, pese a que podía mover superficies de control sin input del piloto.

**Capacidad 2: Criterio codificado — EROSIONADO**

Los criterios de certificación existían en regulaciones (FAR Part 25), pero la interpretación de esos criterios quedó delegada a Boeing. La FAA no tenía los recursos para revisar las interpretaciones. El criterio formal existía; el criterio aplicado era diferente.

**Capacidad 3: Gate vinculante — EROSIONADO**

La certificación de la FAA seguía siendo requisito formal. Pero si Boeing determinaba qué información presentar y cómo clasificarla, el gate perdía capacidad de filtro. El veredicto seguía existiendo; la información para producirlo estaba controlada por quien se beneficiaba de la aprobación.

**Capacidad 4: Protección del NO — AUSENTE**

Documentos internos revelados en investigaciones muestran que ingenieros de Boeing expresaron preocupaciones sobre el MCAS, la dependencia de un solo sensor, y la falta de información a pilotos. Estas preocupaciones fueron descartadas o minimizadas. Quienes cuestionaban enfrentaban presión de calendario y cultura que premiaba avanzar.

Un ingeniero escribió en comunicación interna: "Este avión está diseñado por payasos, supervisados por monos." La frase, cruda, captura la percepción de que las preocupaciones técnicas no tenían peso político.

**Capacidad 5: Separación patrocinio/veredicto — AUSENTE**

Boeing certificaba su propio avión. Los representantes ODA eran empleados de Boeing, evaluados por Boeing, con carreras que dependían de Boeing. No había independencia estructural. La FAA supervisaba, pero no tenía recursos para revisión sustantiva.

**Capacidad 6: Registro irreversible — PARCIAL**

Documentación existía. Los análisis de seguridad existían. Las comunicaciones internas existían. Pero está documentación no activaba alarmas institucionales. El registro existía pero no era visible para quienes podían actuar.

**Capacidad 7: Aprendizaje procedural — AUSENTE**

Boeing había enfrentado problemas serios con el 787 (baterías que se incendiaban, 2013). Las lecciones de ese episodio no se incorporaron al proceso del 737 MAX. Los problemas fueron tratados como eventos aislados, no como síntomas de un sistema de desarrollo bajo presión.

**Capacidad 8: Revisión periódica — AUSENTE**

El programa ODA no fue revisado sustantivamente entre su expansión (2005) y los accidentes (2018-2019). Las condiciones habían cambiado (presión competitiva intensa con Airbus, calendario agresivo, reducción de personal de FAA), pero el mecanismo de delegación no se ajustó.

### El mecanismo de erosión {- .unlisted}

La erosión no fue abrupta. Fue incremental:

**2005-2012:** ODA se expande. FAA reduce personal de certificación. La premisa es que la industria puede auto-regularse para aspectos rutinarios.

**2011-2015:** Airbus anuncia el A320neo. Boeing enfrenta decisión: desarrollar avión nuevo (costoso, lento) o actualizar el 737 (rápido, barato). Elige actualizar. El calendario es agresivo.

**2015-2016:** El MCAS se diseña para compensar características aerodinámicas del MAX. Se clasifica como sistema que no requiere entrenamiento adicional para pilotos (un argumento de venta clave: aerolíneas no tienen que reentrenar pilotos de 737 anteriores).

**2016-2017:** Pruebas de vuelo revelan que el MCAS puede activarse con más frecuencia de lo anticipado. Se expande su autoridad pero no se actualiza la clasificación ni la información a pilotos.

**2017:** Certificación. El MAX entra en servicio.

**2018:** Accidente de Lion Air. Boeing culpa a los pilotos. No emite directiva de seguridad obligatoria. Información sobre MCAS sigue siendo inadecuada.

**2019:** Accidente de Ethiopian Airlines. Flota global es puesta en tierra. Investigaciones revelan la secuencia completa.

### Implicación {- .unlisted}

Los límites externos que funcionan pueden ser erosionados gradualmente hasta volverse ceremoniales. La erosión es invisible porque:

- Cada paso individual parece razonable (eficiencia, delegación, confianza en expertise)
- No hay evento único que marque el cambio
- Quienes se benefician de la erosión son quienes podrían detectarla
- El costo de la erosión es diferido; el beneficio es inmediato

Para el lector: ¿Sus mecanismos de governance independiente siguen siendo independientes? ¿O la "eficiencia" y la "confianza" han transferido gradualmente el poder de verificación a quienes se benefician de la aprobación?

---

## Caso 4: Odebrecht — Ausencia estructural de límites {- .unlisted}

### Resumen {- .unlisted}

Odebrecht fue durante décadas la mayor constructora de América Latina, con operaciones en más de 20 países. En 2016, admitió ante el Departamento de Justicia de Estados Unidos haber pagado aproximadamente 788 millones de dólares en sobornos a funcionarios de 12 países. La multa combinada superó los 3.5 mil millones de dólares, la mayor en la historia por un caso de corrupción extranjera.

Lo que distingue este caso no es el soborno en sí, sino la institucionalización del soborno como estrategia corporativa. Odebrecht no tenía límites que fallaron o se erosionaron. Nunca los tuvo.

### Contexto {- .unlisted}

Odebrecht operó durante décadas con una estructura de "Departamento de Operaciones Estructuradas" —nombre corporativo para la división de sobornos. Este departamento tenía:

- Presupuesto propio
- Personal dedicado
- Sistema de comunicación paralelo (el software Drousys)
- Procedimientos operativos documentados
- Métrica de desempeño (contratos ganados por dólar de soborno invertido)

No era corrupción oportunista. Era corrupción como modelo de negocio. La pregunta relevante no es por qué hubo corrupción sino por qué no hubo ningún mecanismo que la detectara, cuestionara o detuviera.

### Estado de las capacidades {- .unlisted}

**Capacidad 1: Delimitación explícita — AUSENTE**

No había delimitación de qué decisiones requerían escrutinio adicional. El poder ejecutivo, concentrado en la familia Odebrecht, podía tomar cualquier decisión sin checkpoint. La estructura de holding con empresas operativas en múltiples jurisdicciones creaba opacidad, no governance.

**Capacidad 2: Criterio codificado — AUSENTE**

No había criterio previo que determinara qué era aceptable y qué no. Las reglas eran las que el poder dictaba. El único criterio operativo era efectividad: ¿el soborno produce el contrato?

**Capacidad 3: Gate vinculante — AUSENTE**

El Board de directores era ceremonial. La familia controlaba las decisiones relevantes. No había mecanismo que pudiera detener una iniciativa que el poder ejecutivo quisiera avanzar.

**Capacidad 4: Protección del NO — AUSENTE**

Quienes cuestionaban prácticas eran removidos. El sistema no toleraba disidencia. Los documentos judiciales incluyen casos de ejecutivos que expresaron dudas y fueron marginados o expulsados.

**Capacidad 5: Separación patrocinio/veredicto — AUSENTE**

Las mismas personas que se beneficiaban de los contratos obtenidos por corrupción eran quienes tomaban las decisiones sobre cómo obtenerlos. No había separación alguna.

**Capacidad 6: Registro irreversible — PERVERSO**

El sistema Drousys era, de hecho, un registro. Documentaba pagos, receptores, intermediarios. Pero era registro secreto, paralelo a los libros oficiales, diseñado para operar la corrupción eficientemente, no para auditarla.

**Capacidad 7: Aprendizaje procedural — PERVERSO**

El sistema aprendía. Cada ciclo de sobornos mejoraba la eficiencia del siguiente. Los procedimientos se refinaban. Pero el aprendizaje estaba al servicio del problema, no de la solución.

**Capacidad 8: Revisión periódica — AUSENTE**

No había revisión de prácticas porque no había interés en cambiarlas. El sistema funcionaba según los criterios de quienes lo operaban.

### El colapso {- .unlisted}

Odebrecht no se auto-corrigió. El colapso vino por límite externo involuntario: la investigación Lava Jato en Brasil, que comenzó investigando lavado de dinero en estaciones de servicio y terminó exponiendo la red de corrupción más grande documentada en América Latina.

El límite que funcionó no fue interno. Fue el sistema judicial brasileño, activado por circunstancias que Odebrecht no controlaba. Una vez que la investigación comenzó, el sistema de registro (Drousys) se convirtió en evidencia. Lo que había sido herramienta de operación se volvió herramienta de condena.

### Implicación {- .unlisted}

El caso Odebrecht ilustra el estado terminal: qué pasa cuando ninguna capacidad existe.

- Sin delimitación, nada está fuera del alcance del poder
- Sin criterio, las reglas son las que el poder dicta
- Sin gate vinculante, nada detiene lo que el poder quiere avanzar
- Sin protección del NO, nadie cuestiona
- Sin separación, los mismos que se benefician evalúan
- Sin registro legítimo, no hay accountability
- Sin aprendizaje legítimo, el sistema optimiza hacia sus propios fines
- Sin revisión, las condiciones nunca se cuestionan

En ausencia de límites internos, solo la intervención externa puede detener el sistema. Pero la intervención externa típicamente llega después del daño: cuando los contratos ya se firmaron, cuando los sobornos ya se pagaron, cuando la corrupción ya se normalizó.

Para el lector: ¿Existen decisiones en su organización que ningún mecanismo puede cuestionar? ¿Hay categorías de acción donde el poder ejecutivo opera sin checkpoint alguno? Esas son las zonas donde el riesgo es máximo.

---

## Síntesis comparativa {- .unlisted}

| Caso | Resultado | Capacidades presentes | Capacidades ausentes/erosionadas | Lección principal |
|------|-----------|----------------------|----------------------------------|-------------------|
| Toyota Andon | Éxito parcial (funcionó por décadas, falló en 2009-2010) | 1, 2, 3, 4, 5, 7, 8 | 6 (parcial), 1 y 5 erosionadas en crisis | Los límites arquitectados funcionan mientras el alcance coincide con el riesgo |
| J&J Tylenol | Éxito en crisis aguda, erosión posterior | 1, 2, 4, 6, 7 | 3, 5, 8 (parciales) | El criterio previo funciona si se mantiene operativo, no solo cultural |
| Boeing 737 MAX | Fracaso catastrófico | Ninguna funcional al momento de la crisis | Todas erosionadas gradualmente | La erosión incremental es invisible hasta el colapso |
| Odebrecht | Fracaso sistémico | Ninguna (6 y 7 presentes pero pervertidas) | Todas ausentes desde el diseño | Sin límites internos, solo la intervención externa detiene el sistema |

---

## Fuentes principales {- .unlisted}

### Toyota {- .unlisted}
- Liker, J. (2004). *The Toyota Way*. McGraw-Hill.
- Spear, S. & Bowen, H.K. (1999). "Decoding the DNA of the Toyota Production System". *Harvard Business Review*, Sept-Oct.
- NHTSA (2011). *Technical Assessment of Toyota Electronic Throttle Control Systems*.
- Cole, R.E. (2011). "What Really Happened to Toyota?" *MIT Sloan Management Review*, Summer.

### Johnson & Johnson {- .unlisted}
- Kaplan, T. (1998). "The Tylenol Crisis: How Effective Public Relations Saved Johnson & Johnson". Pennsylvania State University.
- Collins, J. & Porras, J. (1994). *Built to Last: Successful Habits of Visionary Companies*. Harper Business, Cap. 3.
- Rehak, J. (2002). "Tylenol Made a Hero of Johnson & Johnson: The Recall That Started Them All". *New York Times*, 23 marzo.
- Reuters Investigative Series (2018-2020). "Johnson & Johnson knew for decades that asbestos lurked in its baby powder".

### Boeing {- .unlisted}
- House Committee on Transportation and Infrastructure (2020). *Final Committee Report: The Design, Development & Certification of the Boeing 737 MAX*.
- Gates, D. (2019-2020). Serie investigativa en *Seattle Times*.
- Robison, P. (2021). *Flying Blind: The 737 MAX Tragedy and the Fall of Boeing*. Doubleday.
- Joint Authorities Technical Review (2019). *Boeing 737 MAX Flight Control System Observations, Findings, and Recommendations*.

### Odebrecht {- .unlisted}
- U.S. Department of Justice (2016). *Odebrecht S.A. and Braskem S.A. Plea Agreement*.
- Gaspar, M. (2020). *A Organização: A Odebrecht e o esquema de corrupção que chocou o mundo*. Companhia das Letras.
- Transparency International (2019). *The Odebrecht Case: Lessons for Latin America*.
- Brazilian Federal Prosecution Service. Documentos de Operação Lava Jato (2014-2021).

