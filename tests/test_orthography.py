#!/usr/bin/env python3
"""
Test de ortografía española para libros en castellano.
Detecta errores comunes de acentuación y uso de ñ.

Uso:
    python3 tests/test_orthography.py
    python3 tests/test_orthography.py chapters/drafts/B1-el-loop-del-poder.md
"""

import re
import sys
from pathlib import Path

# Palabras que deben llevar ñ (patrón incorrecto → correcto)
MISSING_ENE = {
    r'\banos\b': 'años',
    r'\bano\b': 'año',
    r'\bdiseno\b': 'diseño',
    r'\bdisenado\b': 'diseñado',
    r'\bdisenador\b': 'diseñador',
    r'\bdisenados\b': 'diseñados',
    r'\bsenales\b': 'señales',
    r'\bsenal\b': 'señal',
    r'\bdesempeno\b': 'desempeño',
    r'\bmontana\b': 'montaña',
    r'\bmontanas\b': 'montañas',
    r'\bpequeno\b': 'pequeño',
    r'\bpequenos\b': 'pequeños',
    r'\bpequena\b': 'pequeña',
    r'\bpequenas\b': 'pequeñas',
    r'\bcompania\b': 'compañía',
    r'\bcompanias\b': 'compañías',
    r'\bensenanza\b': 'enseñanza',
    r'\bespanol\b': 'español',
    r'\bespanola\b': 'española',
    r'\btamano\b': 'tamaño',
    r'\btamanos\b': 'tamaños',
    r'\bengano\b': 'engaño',
    r'\bsueno\b': 'sueño',
    r'\bsuenos\b': 'sueños',
    r'\bnino\b': 'niño',
    r'\bninos\b': 'niños',
    r'\bnina\b': 'niña',
    r'\bninas\b': 'niñas',
}

# Palabras que deben llevar acento (patrón incorrecto → correcto)
MISSING_ACCENT_PATTERNS = {
    r'([a-záéíóú]+)cion\b': r'\1ción',  # -cion → -ción
    r'([a-záéíóú]+)sion\b': r'\1sión',  # -sion → -sión
}

MISSING_ACCENT_WORDS = {
    r'\bhabia\b': 'había',
    r'\btenia\b': 'tenía',
    r'\bpodia\b': 'podía',
    r'\bsabia\b': 'sabía',
    r'\bdebia\b': 'debía',
    r'\bqueria\b': 'quería',
    r'\bpodria\b': 'podría',
    r'\bdeberia\b': 'debería',
    r'\btendria\b': 'tendría',
    r'\bseria\b': 'sería',
    r'\bestaria\b': 'estaría',
    r'\bhabria\b': 'habría',
    r'\bquerria\b': 'querría',
}

def check_file(filepath: Path) -> list:
    """Revisa un archivo y retorna lista de errores encontrados."""
    errors = []
    content = filepath.read_text(encoding='utf-8')

    # Verificar ñ faltante
    for pattern, correct in MISSING_ENE.items():
        matches = re.findall(pattern, content, re.IGNORECASE)
        if matches:
            errors.append({
                'file': filepath.name,
                'wrong': matches[0],
                'correct': correct,
                'count': len(matches),
                'type': 'ñ faltante'
            })

    # Verificar acentos en palabras específicas
    for pattern, correct in MISSING_ACCENT_WORDS.items():
        matches = re.findall(pattern, content, re.IGNORECASE)
        if matches:
            errors.append({
                'file': filepath.name,
                'wrong': matches[0],
                'correct': correct,
                'count': len(matches),
                'type': 'acento faltante'
            })

    # Verificar patrones -cion, -sion
    cion_matches = re.findall(r'\b[a-záéíóú]+cion\b', content, re.IGNORECASE)
    if cion_matches:
        errors.append({
            'file': filepath.name,
            'wrong': '-cion',
            'correct': '-ción',
            'count': len(cion_matches),
            'type': 'acento faltante',
            'examples': list(set(cion_matches))[:5]
        })

    sion_matches = re.findall(r'\b[a-záéíóú]+sion\b', content, re.IGNORECASE)
    if sion_matches:
        errors.append({
            'file': filepath.name,
            'wrong': '-sion',
            'correct': '-sión',
            'count': len(sion_matches),
            'type': 'acento faltante',
            'examples': list(set(sion_matches))[:5]
        })

    return errors

def main():
    # Determinar archivos a verificar
    if len(sys.argv) > 1:
        files = [Path(f) for f in sys.argv[1:] if f.endswith('.md')]
    else:
        chapters_dir = Path("chapters/drafts")
        if not chapters_dir.exists():
            print("Error: No se encuentra el directorio chapters/drafts/")
            sys.exit(1)
        files = list(chapters_dir.glob("*.md"))

    all_errors = []

    for md_file in files:
        if md_file.exists():
            errors = check_file(md_file)
            all_errors.extend(errors)

    if all_errors:
        print("❌ Errores ortográficos encontrados:\n")

        # Agrupar por tipo
        by_type = {}
        for err in all_errors:
            t = err['type']
            if t not in by_type:
                by_type[t] = []
            by_type[t].append(err)

        total = 0
        for error_type, errors in by_type.items():
            print(f"  [{error_type.upper()}]")
            for err in errors:
                count = err['count']
                total += count
                if 'examples' in err:
                    examples = ', '.join(err['examples'][:3])
                    print(f"    {err['file']}: {err['wrong']} → {err['correct']} ({count}x) ej: {examples}")
                else:
                    print(f"    {err['file']}: '{err['wrong']}' → '{err['correct']}' ({count}x)")
            print()

        print(f"  Total: {total} correcciones necesarias")
        print("\n  Ejecutar ./scripts/fix_orthography.sh para corregir automáticamente")
        sys.exit(1)
    else:
        print("✅ Ortografía verificada correctamente")
        print(f"   Archivos revisados: {len(files)}")
        sys.exit(0)

if __name__ == "__main__":
    main()
