# CLAUDE.md - Contexto para Claude Code

## Proyecto
**Más control, más caos** - Límites externos para sistemas que no se detienen solos.

Nota: "Gerencia funcional" es concepto interno del libro, no título. Se define en el Capítulo 7 con la analogía a medicina funcional.

## Tesis Central (Option B)
> Los sistemas organizacionales sanos renuncian deliberadamente a parte de su poder
> para preservar adaptabilidad, sentido y supervivencia.

## Lector Objetivo
CEO / Comité Ejecutivo que necesita evitar que iniciativas estratégicas mal planteadas
entren en ejecución y quemen dinero, credibilidad y capital político.

## Tono
- Incómodo
- Riguroso
- Sistémico

## Anti-patterns (evitar)
- Framework genérico
- Checklists sin trade-offs
- Narrativa lineal sin loops
- Subtítulos visibles en prosa
- Listas con bullets en capítulos

## Términos Canónicos
- **Coding Trance**: Estado cognitivo organizacional donde capacidad reemplaza contexto
- **DRG (Decision Readiness Gate)**: Gate obligatorio con veredicto ✅/⚠️/⛔
- **Runaway Dynamics**: Realimentación positiva sin frenos
- **Fricción deliberada**: Límites explícitos como activos
- **Criterio codificado**: Reglas observables, con umbral y consecuencia predefinida

## Sistema de 8 Capacidades
El libro presenta un sistema de capacidades interdependientes (no soluciones aisladas):
1. **CAP-1**: Detección de loops y trance
2. **CAP-2**: Límite previo a ejecución (DRG)
3. **CAP-3**: Aprendizaje grupal y procedural
4. **CAP-4**: Criterio codificado resistente
5. **CAP-5**: Absorción de fricción y costo político
6. **CAP-6**: Override explícito y trazable
7. **CAP-7**: Gobernanza humano-algorítmica
8. **CAP-8**: Diferenciación por dominio

## Estructura del Repositorio
```
.state/           → YAML de estado del libro (fuente de verdad)
chapters/drafts/  → Capítulos y apéndices en desarrollo
chapters/published/ → Capítulos finalizados
concepts/         → Nodos conceptuales (C1-C7)
assets/
  references/     → Referencias teóricas
  cases/          → Casos de estudio
  fragments/      → Fragmentos reutilizables
templates/        → Plantillas LaTeX para PDF (reutilizable)
output/
  pdf/            → PDF generado
  epub/           → EPUB generado
  md/             → Capítulos individuales en Markdown
```

## Estado Actual
- Version: v3.8
- Blueprints totales: 21
- Capítulos con contenido: 20
- Apéndices: 7
- Páginas PDF: 263

## Secuencia de Capítulos (v3.8)
1. B0 - Introducción
2. B1 - El loop del poder
3. B2 - Control ≠ estabilidad
4. B3 - Coding Trance
5. B4 - Los sistemas no se auto-limitan
6. B7 - El aprendizaje no es individual
7. B8 - IA y los límites humanos
8. B5 - Capacidades de la Gerencia Funcional
9. B5.5 - Anatomía del Gate
10. B5.6 - Cuando el límite falla
11. B6 - Casos donde decir NO fue éxito
12. B09 - Criterio codificado
13. B10 - Implementación
14. Apéndice A - Criterios de Readiness por Tipo de Iniciativa
15. Apéndice B - Por qué no hay casos públicos
16. Apéndice C - Convergencias
17. Apéndice D - Diseño y anti-patrones del gate
18. Apéndice E - Instrumento de Diagnóstico
19. Apéndice F - Casos de Referencia
20. Apéndice G - Bibliografía

## Formato de Capítulos
Cada capítulo usa 5 bloques HTML obligatorios:
```markdown
<!-- block: reconocimiento -->
<!-- block: alivio -->
<!-- block: causa -->
<!-- block: riesgo -->
<!-- block: proteccion -->
```

## Comandos Útiles
```bash
# Ver estado del libro
cat .state/book-state.yaml

# Generar libro completo (EPUB + PDF)
./build-book.sh full

# Generar capítulo individual
./build-book.sh chapter chapters/drafts/B1-el-loop-del-poder.md

# Contar palabras
wc -w chapters/drafts/*.md
```

## Tests de Calidad
- **executive_sleep_test**: ¿Ayuda al CEO a dormir mejor la noche previa a la junta?
- **circularity_test**: ¿El argumento cierra en loop, no en línea?
- **depersonalization_test**: ¿El problema es estructural, no de personas?

## Invariantes de Edición
- El DRG es UNA capacidad crítica, no LA solución única
- Cada capítulo declara qué capacidades habilita
- Trade-offs explícitos, no consejos
- No vender sofisticación; traducir a alivio/protección/cobertura
- Cada capítulo incluye al menos una afirmación incómoda verificable

## Normas Editoriales de Lenguaje

### Anglicismos Corregidos
Usar siempre el equivalente castellano:
- governance → **gobernanza**
- timeline → **cronograma**
- checklist → **lista de verificación**

### Anglicismos Conservados
Sin equivalente natural en contexto empresarial hispanohablante:
- **feedback** (retroalimentación es aceptable pero menos fluido)
- **sponsor** (patrocinador pierde el matiz de respaldo político)
- **stakeholder** (interesado no captura la relación de poder)
- **software**, **hardware** (universales)
- **dashboard** (tablero es aceptable)
- **framework** (marco conceptual cuando sea posible)
- **deadline** (fecha límite es aceptable)

### Términos Técnicos del Libro (Canon)
No traducir ni modificar:
- **DRG** (Decision Readiness Gate)
- **Coding Trance**
- **Runaway Dynamics**

### Formato de Texto
- Sin emojis en contenido del libro
- Sin bullets ni listas numeradas en capítulos (solo prosa)
- Subtítulos invisibles (solo bloques HTML)
- Párrafos de 4-8 líneas preferidos
- Tablas permitidas solo en apéndices y resúmenes de capacidades

### Criterio General
Preferir castellano cuando:
1. Existe equivalente de uso común en ámbito empresarial
2. El término aparece en prosa (no en tecnicismos)
3. La RAE lo recomienda explícitamente

Conservar inglés cuando:
1. No existe equivalente natural
2. El equivalente castellano suena forzado o pedante
3. El término es universal en la industria

## Sistema de Referencias (OBLIGATORIO)

### Base de datos
Las referencias se gestionan en `.state/references.yaml`. Cada referencia tiene:
- `id`: identificador único (REF-XXX)
- `citation_key`: clave corta para citas (apellido+año)
- `type`: book | article | report | web | news | legal
- `verified`: true/false (¿URL/datos confirmados?)
- `used_in`: lista de archivos y contexto donde se usa
- `apa_formatted`: cita completa en formato APA 7

### Al agregar datos o citas nuevas
1. **Verificar** si existe en `.state/references.yaml`
2. **Si no existe**, agregar entrada completa:
   - Buscar fuente primaria con WebSearch
   - Verificar datos exactos
   - Obtener URL si disponible
   - Agregar a references.yaml con todos los campos
3. **En el texto**, incluir cita: (Autor, año)
4. **Actualizar** `appendix-E-bibliografia.md`
5. **Ejecutar** `python3 tests/test_references.py`

### Formato de citas en texto
```markdown
# Para teorías académicas:
La Ley de Variedad Requerida (Ashby, 1956) establece que...

# Para estadísticas:
El 60% de las transformaciones fracasan (McKinsey & Company, 2021).

# Para casos empresariales:
El colapso de OGX en 2013 (Reuters, 2013) ilustra...
```

### Qué citar formalmente
- Teorías académicas con autor identificable
- Estadísticas específicas (porcentajes, cantidades monetarias)
- Casos empresariales con datos verificables
- Leyes o principios nombrados (Ashby, Goodhart)

### Qué NO citar (conocimiento general)
- "Las organizaciones tienden a..."
- Umbrales propuestos por el libro (10-30% rechazo)
- Experiencia directa del autor (declarada como tal)
- Ejemplos hipotéticos marcados como tales

### Validación
```bash
# Ejecutar antes de commit
python3 tests/test_references.py
```
