#!/bin/bash
# =============================================================================
# fix_orthography.sh - Corrección ortográfica automática para español
# =============================================================================
# Uso:
#   ./scripts/fix_orthography.sh              # Corrige chapters/drafts/*.md
#   ./scripts/fix_orthography.sh archivo.md   # Corrige archivo específico
# =============================================================================

set -e

# Colores
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}=== Corrección ortográfica automática ===${NC}"
echo ""

# Determinar archivos a procesar
if [ -n "$1" ]; then
    FILES="$@"
else
    FILES="chapters/drafts/*.md"
fi

# Contador de cambios
CHANGES=0

# -----------------------------------------------------------------------------
# CORRECCIÓN DE Ñ FALTANTE
# -----------------------------------------------------------------------------
echo -e "${BLUE}[1/3] Corrigiendo ñ faltante...${NC}"

declare -A ENE_FIXES=(
    ["anos"]="años"
    ["ano"]="año"
    ["diseno"]="diseño"
    ["disenado"]="diseñado"
    ["disenador"]="diseñador"
    ["disenados"]="diseñados"
    ["senales"]="señales"
    ["senal"]="señal"
    ["desempeno"]="desempeño"
    ["montana"]="montaña"
    ["montanas"]="montañas"
    ["pequeno"]="pequeño"
    ["pequenos"]="pequeños"
    ["pequena"]="pequeña"
    ["pequenas"]="pequeñas"
    ["compania"]="compañía"
    ["companias"]="compañías"
    ["ensenanza"]="enseñanza"
    ["espanol"]="español"
    ["espanola"]="española"
    ["tamano"]="tamaño"
    ["engano"]="engaño"
    ["sueno"]="sueño"
    ["suenos"]="sueños"
    ["nino"]="niño"
    ["ninos"]="niños"
)

for wrong in "${!ENE_FIXES[@]}"; do
    correct="${ENE_FIXES[$wrong]}"
    count=$(grep -rwoE "\b${wrong}\b" $FILES 2>/dev/null | wc -l || echo 0)
    if [ "$count" -gt 0 ]; then
        sed -i "s/\b${wrong}\b/${correct}/g" $FILES
        echo "  ✓ ${wrong} → ${correct} (${count}x)"
        CHANGES=$((CHANGES + count))
    fi
done

# -----------------------------------------------------------------------------
# CORRECCIÓN DE ACENTOS EN -CIÓN Y -SIÓN
# -----------------------------------------------------------------------------
echo ""
echo -e "${BLUE}[2/3] Corrigiendo acentos en -ción/-sión...${NC}"

# -cion → -ción
cion_count=$(grep -rhoE '\b[a-z]+cion\b' $FILES 2>/dev/null | wc -l || echo 0)
if [ "$cion_count" -gt 0 ]; then
    sed -i 's/cion\b/ción/g' $FILES
    echo "  ✓ -cion → -ción (${cion_count}x)"
    CHANGES=$((CHANGES + cion_count))
fi

# -sion → -sión
sion_count=$(grep -rhoE '\b[a-z]+sion\b' $FILES 2>/dev/null | wc -l || echo 0)
if [ "$sion_count" -gt 0 ]; then
    sed -i 's/sion\b/sión/g' $FILES
    echo "  ✓ -sion → -sión (${sion_count}x)"
    CHANGES=$((CHANGES + sion_count))
fi

# -----------------------------------------------------------------------------
# CORRECCIÓN DE VERBOS SIN ACENTO
# -----------------------------------------------------------------------------
echo ""
echo -e "${BLUE}[3/3] Corrigiendo verbos sin acento...${NC}"

declare -A VERB_FIXES=(
    ["habia"]="había"
    ["tenia"]="tenía"
    ["podia"]="podía"
    ["sabia"]="sabía"
    ["debia"]="debía"
    ["queria"]="quería"
    ["podria"]="podría"
    ["deberia"]="debería"
    ["tendria"]="tendría"
    ["seria"]="sería"
    ["estaria"]="estaría"
    ["habria"]="habría"
    ["querria"]="querría"
)

for wrong in "${!VERB_FIXES[@]}"; do
    correct="${VERB_FIXES[$wrong]}"
    count=$(grep -rwoE "\b${wrong}\b" $FILES 2>/dev/null | wc -l || echo 0)
    if [ "$count" -gt 0 ]; then
        sed -i "s/\b${wrong}\b/${correct}/g" $FILES
        echo "  ✓ ${wrong} → ${correct} (${count}x)"
        CHANGES=$((CHANGES + count))
    fi
done

# -----------------------------------------------------------------------------
# CORRECCIÓN DE MAYÚSCULAS
# -----------------------------------------------------------------------------
echo ""
echo -e "${BLUE}[4/4] Corrigiendo variantes en mayúsculas...${NC}"

# Variantes con mayúscula inicial
declare -A CAPS_FIXES=(
    ["Tenia"]="Tenía"
    ["Habia"]="Había"
    ["Podia"]="Podía"
    ["Debia"]="Debía"
    ["Seria"]="Sería"
    ["Podria"]="Podría"
    ["Deberia"]="Debería"
)

for wrong in "${!CAPS_FIXES[@]}"; do
    correct="${CAPS_FIXES[$wrong]}"
    count=$(grep -rwoE "\b${wrong}\b" $FILES 2>/dev/null | wc -l || echo 0)
    if [ "$count" -gt 0 ]; then
        sed -i "s/\b${wrong}\b/${correct}/g" $FILES
        echo "  ✓ ${wrong} → ${correct} (${count}x)"
        CHANGES=$((CHANGES + count))
    fi
done

# Variantes en mayúsculas completas
sed -i 's/CION\b/CIÓN/g' $FILES 2>/dev/null || true
sed -i 's/SION\b/SIÓN/g' $FILES 2>/dev/null || true

# -----------------------------------------------------------------------------
# RESUMEN
# -----------------------------------------------------------------------------
echo ""
if [ "$CHANGES" -gt 0 ]; then
    echo -e "${GREEN}✓ ${CHANGES} correcciones aplicadas${NC}"
    echo ""
    echo "Siguiente paso: python3 tests/test_orthography.py"
else
    echo -e "${GREEN}✓ No se encontraron errores ortográficos${NC}"
fi
