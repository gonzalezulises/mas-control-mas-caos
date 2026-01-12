# CLAUDE.md - Monorepo Más control, más caos

## Estructura

```
├── website/    # Landing page
└── book/       # Manuscrito (ver book/CLAUDE.md para instrucciones detalladas)
```

## Contexto rápido

- **Proyecto:** Libro "Más control, más caos"
- **Autor:** Ulises González (ulises@rizo.ma)
- **Idioma:** Español neutro (tú, no vos)

## Comandos principales

### Website
```bash
cd website
# Servir localmente (requiere servidor HTTP)
python3 -m http.server 8000
```

### Book
```bash
cd book
./build-book.sh full           # Genera PDF + EPUB
python3 tests/test_orthography.py  # Validar ortografía
```

## Instrucciones detalladas

Para trabajar con el manuscrito del libro, consultar `book/CLAUDE.md` que contiene:
- Términos canónicos (DRG, Coding Trance, etc.)
- Sistema de 8 capacidades
- Normas editoriales de lenguaje
- Sistema de referencias
- Pipeline de generación de assets

## Deploy

- **Website:** Vercel (Root Directory: `website`)
- **Book outputs:** `book/output/pdf/` y `book/output/epub/`
