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
- Version: v2 (working)
- Capítulos mapeados: 2
- Capítulos drafted: 1 (B1)
- Blueprints nuevos pendientes: 4 (B7, B8, B9, B10)
- Fragmentos sin resolver: 7

## Secuencia de Capítulos (v2)
1. B1 - El loop del poder
2. B2 - Control ≠ estabilidad
3. B3 - Coding Trance
4. B7 - El aprendizaje no es individual
5. B8 - IA y los límites humanos
6. B4 - La renuncia al poder
7. B9 - Los sistemas no pueden auto-limitarse
8. B5 - Decision Readiness Gate (DRG)
9. B10 - Criterio codificado
10. B6 - Casos donde decir NO fue éxito

## Próximas Acciones
1. Completar mapeo v1→v2 para todos los capítulos
2. Definir criterios observables de Coding Trance
3. Especificar reglas A-D del DRG en formato evaluable
4. Desarrollar thesis y exit_criteria para B9 (auto-limitación)
5. Desarrollar thesis y exit_criteria para B10 (criterio codificado)

## Comandos Útiles
- Ver estado: `cat .state/book-state.yaml`
- Ver concepto: `cat concepts/C{N}-*.md`
- Ver blueprint: `cat chapters/drafts/B{N}-*.md`

