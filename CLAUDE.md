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

## Términos Canónicos
- **Coding Trance**: Estado cognitivo organizacional donde capacidad reemplaza contexto
- **DRG (Decision Readiness Gate)**: Gate obligatorio con veredicto ✅/⚠️/⛔
- **Runaway Dynamics**: Realimentación positiva sin frenos
- **Fricción deliberada**: Límites explícitos como activos

## Estructura del Repositorio
```
.state/           → YAML de estado del libro (fuente de verdad)
chapters/drafts/  → Capítulos en desarrollo
chapters/published/ → Capítulos finalizados
concepts/         → Nodos conceptuales (C1-C5)
assets/
  references/     → Referencias teóricas
  cases/          → Casos de estudio
  fragments/      → Fragmentos reutilizables
architecture/     → Versiones de arquitectura del libro
.ai/              → Contratos y prompts para AI
```

## Estado Actual
- Version: v2.1 (restructured)
- Blueprints totales: 9
- Capítulos con contenido: 7
- Capítulos stub: 2 (B4 reserved, B09 closing pending)

## Secuencia de Capítulos (v2.1)
1. B1 - El loop del poder
2. B2 - Control ≠ estabilidad
3. B3 - Coding Trance
4. B7 - El aprendizaje no es individual
5. B8 - IA y los límites humanos
6. B4 - Los sistemas no se auto-limitan (reserved, not in print)
7. B5 - Decision Readiness Gate (DRG)
8. B6 - Casos donde decir NO fue éxito
9. B09 - Criterio codificado (closing chapter)

## Próximas Acciones
1. Escribir contenido de B09 (capítulo de cierre)
2. Revisar consistencia entre blueprints y archivos

## Comandos Útiles
- Ver estado: `cat .state/book-state.yaml`
- Ver concepto: `cat concepts/C{N}-*.md`
- Ver blueprint: `cat chapters/drafts/B{N}-*.md`

