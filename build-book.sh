#!/bin/bash
# Build script para Gerencia Funcional
# Genera EPUB y PDF desde los capítulos Markdown

set -e

BOOK_DIR="$(cd "$(dirname "$0")" && pwd)"
OUTPUT_EPUB="$BOOK_DIR/output/epub"
OUTPUT_PDF="$BOOK_DIR/output/pdf"

# Colores
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m'

echo -e "${BLUE}=== Gerencia Funcional - Build ===${NC}"
echo ""

# Crear directorios si no existen
mkdir -p "$OUTPUT_EPUB" "$OUTPUT_PDF"

# Función para generar un capítulo
build_chapter() {
    local chapter="$1"
    local basename=$(basename "$chapter" .md)

    echo -e "${GREEN}Generando:${NC} $basename"

    # EPUB
    pandoc "$chapter" \
        --metadata-file="$BOOK_DIR/book-metadata.yaml" \
        --toc --toc-depth=2 \
        -o "$OUTPUT_EPUB/$basename.epub"
    echo "  ✓ EPUB: output/epub/$basename.epub"

    # PDF
    pandoc "$chapter" \
        --metadata-file="$BOOK_DIR/book-metadata.yaml" \
        --template="$BOOK_DIR/templates/book-template.tex" \
        --pdf-engine=xelatex \
        -o "$OUTPUT_PDF/$basename.pdf"
    echo "  ✓ PDF:  output/pdf/$basename.pdf"
    echo ""
}

# Función para generar libro completo
build_full_book() {
    echo -e "${GREEN}Generando libro completo...${NC}"

    # Orden de capítulos según book-state.yaml (sequence order)
    local chapters=(
        "chapters/drafts/B1-el-loop-del-poder.md"
        "chapters/drafts/B2-control-no-es-estabilidad.md"
        "chapters/drafts/B3-coding-trance.md"
        "chapters/drafts/B7-aprendizaje-grupal-procedural.md"
        "chapters/drafts/B8-ia-y-limites-humanos.md"
        "chapters/drafts/B4-los-sistemas-no-se-auto-limitan.md"
        "chapters/drafts/B5-capacidades-gerencia-funcional.md"
        "chapters/drafts/B6-casos-donde-decir-no-fue-exito.md"
        "chapters/drafts/B09-criterio-codificado.md"
    )

    local existing_chapters=""
    for ch in "${chapters[@]}"; do
        if [ -f "$BOOK_DIR/$ch" ]; then
            existing_chapters="$existing_chapters $BOOK_DIR/$ch"
        fi
    done

    # EPUB completo
    pandoc $existing_chapters \
        --metadata-file="$BOOK_DIR/book-metadata.yaml" \
        --toc --toc-depth=2 \
        -o "$OUTPUT_EPUB/gerencia-funcional-full.epub"
    echo "  ✓ EPUB: output/epub/gerencia-funcional-full.epub"

    # PDF completo
    pandoc $existing_chapters \
        --metadata-file="$BOOK_DIR/book-metadata.yaml" \
        --template="$BOOK_DIR/templates/book-template.tex" \
        --pdf-engine=xelatex \
        -o "$OUTPUT_PDF/gerencia-funcional-full.pdf"
    echo "  ✓ PDF:  output/pdf/gerencia-funcional-full.pdf"
}

# Modo de uso
case "${1:-all}" in
    chapter)
        if [ -z "$2" ]; then
            echo "Uso: $0 chapter <ruta-capitulo.md>"
            exit 1
        fi
        build_chapter "$2"
        ;;
    full)
        build_full_book
        ;;
    all)
        # Generar todos los capítulos individualmente
        for chapter in "$BOOK_DIR"/chapters/drafts/B*.md; do
            if [ -f "$chapter" ]; then
                build_chapter "$chapter"
            fi
        done
        build_full_book
        ;;
    *)
        echo "Uso: $0 [chapter <archivo> | full | all]"
        echo ""
        echo "  chapter <archivo>  - Genera un capítulo específico"
        echo "  full               - Genera el libro completo"
        echo "  all                - Genera todos los capítulos + libro completo"
        exit 1
        ;;
esac

echo -e "${BLUE}¡Build completado!${NC}"
