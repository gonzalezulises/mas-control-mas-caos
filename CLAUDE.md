# CLAUDE.md - Contexto para Claude Code

## Proyecto
**Gerencia Funcional** - Libro sobre sistemas organizacionales y fricción deliberada.

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
templates/        → Plantillas LaTeX para PDF
output/           → EPUB y PDF generados
```

## Estado Actual
- Version: v3.1
- Blueprints totales: 12
- Capítulos con contenido: 10
- Apéndices: 2
- Páginas PDF: 178

## Secuencia de Capítulos (v3.1)
1. B1 - El loop del poder
2. B2 - Control ≠ estabilidad
3. B3 - Coding Trance
4. B4 - Los sistemas no se auto-limitan
5. B7 - El aprendizaje no es individual
6. B8 - IA y los límites humanos
7. B5 - Capacidades de la Gerencia Funcional
8. B6 - Casos donde decir NO fue éxito
9. B09 - Criterio codificado
10. B10 - Implementación
11. Apéndice A - Criterios de Readiness por Tipo de Iniciativa
12. Apéndice B - Por qué no hay casos públicos

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
