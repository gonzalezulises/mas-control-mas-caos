# Gerencia Funcional - Sistema de Producción de Libros

Sistema completo para escribir, validar y generar libros en español con calidad editorial profesional.

## Contexto para IA

Este repositorio es una **plantilla reutilizable** para producción de libros técnicos/empresariales en español. Contiene:
- Pipeline de generación PDF/EPUB
- Validación ortográfica automatizada
- Sistema de referencias APA 7
- Tests de calidad editorial
- CI/CD con GitHub Actions

**Para replicar**: Copiar estructura, adaptar `CLAUDE.md` y `book-state.yaml` al nuevo contenido.

---

## Estructura del Repositorio

```
.
├── CLAUDE.md                    # LEER PRIMERO - Contexto completo para IA
├── .state/
│   ├── book-state.yaml          # Estado del libro (versión, progreso, historial)
│   └── references.yaml          # Base de datos de referencias bibliográficas
├── chapters/
│   └── drafts/                  # Capítulos en desarrollo (B*.md, appendix-*.md)
├── templates/
│   └── book-template.tex        # Template LaTeX para PDF
├── scripts/
│   └── fix_orthography.sh       # Corrección ortográfica automática
├── tests/
│   ├── test_orthography.py      # Validación de ñ y acentos
│   ├── test_references.py       # Validación de citas
│   ├── test_chapter_structure_blocks.py
│   └── ...                      # Otros tests de calidad
├── output/
│   ├── pdf/                     # PDFs generados
│   ├── epub/                    # EPUBs generados
│   └── md/                      # Markdown exportados
├── build-book.sh                # Script de generación
└── .github/workflows/
    └── validate.yml             # CI para validación automática
```

---

## Archivos Clave

| Archivo | Propósito | Cuándo modificar |
|---------|-----------|------------------|
| `CLAUDE.md` | Contexto completo para IA (tono, términos, reglas) | Adaptar para cada libro |
| `.state/book-state.yaml` | Estado, versión, estructura de capítulos | Actualizar con cada cambio significativo |
| `templates/book-template.tex` | Diseño visual del PDF | Solo si necesitas cambiar tipografía/layout |
| `scripts/fix_orthography.sh` | Diccionario de correcciones | Agregar palabras específicas del dominio |

---

## Comandos Principales

### Generación
```bash
# Libro completo (PDF + EPUB)
./build-book.sh full

# Capítulo individual
./build-book.sh chapter chapters/drafts/B1-el-loop-del-poder.md

# Todos los capítulos por separado
for f in chapters/drafts/*.md; do ./build-book.sh chapter "$f"; done

# Copiar Markdown a output
cp chapters/drafts/*.md output/md/
```

### Validación
```bash
# Ortografía (ñ, acentos)
python3 tests/test_orthography.py

# Corrección automática
./scripts/fix_orthography.sh

# Referencias bibliográficas
python3 tests/test_references.py

# Estructura de capítulos
python3 tests/test_chapter_structure_blocks.py chapters/
```

### Flujo Pre-Commit
```bash
python3 tests/test_orthography.py && \
./scripts/fix_orthography.sh && \
python3 tests/test_references.py && \
./build-book.sh full && \
git add . && git commit -m "descripción"
```

---

## Formato de Capítulos

Cada capítulo usa bloques HTML para estructura:

```markdown
# Título del Capítulo {-}

<!-- block: reconocimiento -->
Texto que el lector reconoce como su situación...

<!-- block: alivio -->
Lo que este capítulo ofrece como solución...

<!-- block: causa -->
Análisis de por qué ocurre el problema...

<!-- block: riesgo -->
Qué pasa si no se aborda...

<!-- block: proteccion -->
Cómo el lector queda protegido...
```

---

## Sistema de Referencias

### Formato en texto
```markdown
La Ley de Variedad Requerida (Ashby, 1956) establece que...
El 60% de las transformaciones fracasan (McKinsey, 2021).
```

### Base de datos
Las referencias se almacenan en `.state/references.yaml`:
```yaml
- id: REF-001
  citation_key: ashby1956
  type: book
  apa_formatted: "Ashby, W. R. (1956). *An introduction to cybernetics*. Chapman & Hall."
  verified: true
```

### Bibliografía en PDF
- **Conservar**: DOIs (`https://doi.org/...`) - cortos y estables
- **Eliminar**: URLs largas de sitios web - causan desbordamiento

---

## Validación Ortográfica

### Errores detectados automáticamente
| Tipo | Ejemplos |
|------|----------|
| ñ faltante | anos→años, diseno→diseño, senales→señales |
| -ción/-sión | decision→decisión, revision→revisión |
| Verbos | habia→había, tenia→tenía, podria→podría |

### Palabras que requieren revisión manual
- `solo/sólo`: adjetivo vs adverbio
- `aun/aún`: incluso vs todavía
- `hacia/hacía`: preposición vs verbo

---

## Crear Nuevo Libro (Plantilla)

```bash
# 1. Clonar estructura
git clone https://github.com/gonzalezulises/gerencia-funcional.git nuevo-libro
cd nuevo-libro
rm -rf .git && git init

# 2. Limpiar contenido específico
rm chapters/drafts/*.md
rm output/pdf/* output/epub/* output/md/*

# 3. Adaptar configuración
# Editar CLAUDE.md: título, tesis, términos, tono
# Editar .state/book-state.yaml: reiniciar versión, estructura

# 4. Crear primer capítulo
cat > chapters/drafts/B1-introduccion.md << 'EOF'
# Introducción {-}

<!-- block: reconocimiento -->
...
EOF

# 5. Validar y generar
python3 tests/test_orthography.py
./build-book.sh full
```

---

## Dependencias

```bash
# Ubuntu/Debian
sudo apt install pandoc texlive-xetex texlive-lang-spanish

# Fuentes (incluidas en texlive)
# TeX Gyre Termes, TeX Gyre Heros, DejaVu Sans Mono

# Python (para tests)
python3  # No requiere paquetes externos
```

---

## CI/CD

GitHub Actions valida automáticamente en cada push:
- Ortografía (test_orthography.py)
- Estructura de capítulos
- Lenguaje prohibido

Ver `.github/workflows/validate.yml`

---

## Convenciones

### Idioma
- Castellano neutro latinoamericano
- Anglicismos técnicos permitidos: feedback, sponsor, stakeholder
- Anglicismos traducidos: governance→gobernanza, timeline→cronograma

### Formato
- Sin emojis en contenido
- Sin bullets en capítulos (solo prosa)
- Tablas solo en apéndices
- Párrafos de 4-8 líneas

### Commits
```
Descripción breve del cambio

Detalles si necesario...

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>
```

---

## Estado Actual

- **Versión**: v3.8
- **Páginas PDF**: ~280
- **Capítulos**: 13
- **Apéndices**: 7
- **Diagramas**: 12 (Graphviz)
- **Fotografías**: 10 (Unsplash, licencia libre)

Ver `CLAUDE.md` para contexto completo del contenido.
