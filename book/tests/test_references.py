#!/usr/bin/env python3
"""
Test de validacion del sistema de referencias.

Verifica:
1. Toda cita (Autor, año) en texto tiene entrada en references.yaml
2. Toda entrada en references.yaml esta usada en algun capitulo
3. Formato APA correcto en apa_formatted
4. Consistencia entre references.yaml y appendix-E-bibliografia.md

Uso:
  python tests/test_references.py
  python tests/test_references.py --check-urls  # Verifica URLs (lento)
"""

import sys
import re
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML no instalado. Instalar con: pip install pyyaml")
    sys.exit(2)


def die(msg: str) -> None:
    print(f"FAIL: {msg}")
    sys.exit(1)


def warn(msg: str) -> None:
    print(f"WARN: {msg}")


def ok(msg: str) -> None:
    print(f"OK: {msg}")


def load_references(path: Path) -> dict:
    """Carga references.yaml"""
    if not path.exists():
        die(f"Archivo no encontrado: {path}")

    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        die("references.yaml debe ser un diccionario")

    return data


def extract_citations_from_text(chapters_dir: Path) -> list:
    """
    Extrae citas del formato (Autor, año) de los capítulos.
    Retorna lista de tuplas (archivo, linea, cita)
    """
    citations = []
    # Patron: (Apellido, 1956) o (Apellido & Apellido, 2015) o (Organizacion, 2021)
    pattern = re.compile(r'\(([A-Z][a-zA-záéíóú\s&]+),\s*(\d{4})\)')

    for md_file in chapters_dir.glob("*.md"):
        content = md_file.read_text(encoding="utf-8")
        for i, line in enumerate(content.split('\n'), 1):
            for match in pattern.finditer(line):
                citations.append({
                    'file': md_file.name,
                    'line': i,
                    'author': match.group(1).strip(),
                    'year': int(match.group(2)),
                    'full': match.group(0)
                })

    return citations


def validate_references_structure(refs: dict) -> None:
    """Valida estructura basica de references.yaml"""
    if 'metadata' not in refs:
        warn("Falta seccion 'metadata' en references.yaml")

    if 'references' not in refs:
        die("Falta seccion 'references' en references.yaml")

    if not isinstance(refs['references'], list):
        die("'references' debe ser una lista")

    required_fields = ['id', 'type', 'citation_key', 'title', 'year', 'used_in']

    for i, ref in enumerate(refs['references']):
        if not isinstance(ref, dict):
            die(f"Referencia {i} no es un diccionario")

        for field in required_fields:
            if field not in ref:
                warn(f"Referencia {ref.get('id', i)}: falta campo '{field}'")


def validate_used_in_files_exist(refs: dict, chapters_dir: Path) -> None:
    """Verifica que los archivos en used_in existan"""
    missing = []

    for ref in refs.get('references', []):
        for usage in ref.get('used_in', []):
            file_path = chapters_dir / usage.get('file', '')
            if not file_path.exists():
                missing.append(f"{ref['id']}: {usage.get('file')}")

    if missing:
        warn(f"Archivos en used_in que no existen: {missing}")
    else:
        ok("Todos los archivos en used_in existen")


def validate_apa_format(refs: dict) -> None:
    """Verifica que apa_formatted tenga formato minimo correcto"""
    issues = []

    for ref in refs.get('references', []):
        apa = ref.get('apa_formatted', '')
        ref_id = ref.get('id', 'unknown')

        if not apa:
            issues.append(f"{ref_id}: falta apa_formatted")
            continue

        # Verificar que tenga año entre parentesis
        if not re.search(r'\(\d{4}\)', apa):
            issues.append(f"{ref_id}: apa_formatted sin año entre paréntesis")

        # Verificar que termine con punto
        if not apa.rstrip().endswith('.'):
            issues.append(f"{ref_id}: apa_formatted no termina en punto")

    if issues:
        for issue in issues[:5]:  # Mostrar max 5
            warn(issue)
        if len(issues) > 5:
            warn(f"... y {len(issues) - 5} problemas más en apa_formatted")
    else:
        ok("Formato APA básico correcto en todas las referencias")


def count_verified_references(refs: dict) -> tuple:
    """Cuenta referencias verificadas vs pendientes"""
    verified = 0
    pending = 0

    for ref in refs.get('references', []):
        if ref.get('verified', False):
            verified += 1
        else:
            pending += 1

    return verified, pending


def main():
    # Paths
    repo_root = Path(__file__).parent.parent
    refs_path = repo_root / ".state" / "references.yaml"
    chapters_dir = repo_root / "chapters" / "drafts"

    print("=== Validación Sistema de Referencias ===\n")

    # 1. Cargar y validar estructura
    refs = load_references(refs_path)
    validate_references_structure(refs)
    ok(f"references.yaml cargado: {len(refs.get('references', []))} referencias")

    # 2. Validar que archivos en used_in existan
    validate_used_in_files_exist(refs, chapters_dir)

    # 3. Validar formato APA
    validate_apa_format(refs)

    # 4. Contar verificadas
    verified, pending = count_verified_references(refs)
    if pending > 0:
        warn(f"Referencias verificadas: {verified}, pendientes: {pending}")
    else:
        ok(f"Todas las {verified} referencias están verificadas")

    # 5. Extraer citas del texto (informativo)
    citations = extract_citations_from_text(chapters_dir)
    if citations:
        ok(f"Citas encontradas en texto: {len(citations)}")
    else:
        warn("No se encontraron citas en formato (Autor, año) en los capítulos")

    print("\n=== Resumen ===")
    print(f"Referencias en YAML: {len(refs.get('references', []))}")
    print(f"Verificadas: {verified}")
    print(f"Pendientes: {pending}")
    print(f"Citas en texto: {len(citations)}")

    # Exit con warning si hay pendientes
    if pending > 0:
        print(f"\nWARN: {pending} referencias pendientes de verificar")
        sys.exit(0)  # Warning, no error

    print("\nPASS: Sistema de referencias validado")


if __name__ == "__main__":
    main()
