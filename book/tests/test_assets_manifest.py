#!/usr/bin/env python3
"""
test_assets_manifest.py - Tests para el manifest de assets

Ejecutar:
    python3 tests/test_assets_manifest.py
"""

import sys
import yaml
from pathlib import Path

# Paths
REPO_ROOT = Path(__file__).parent.parent
MANIFEST_PATH = REPO_ROOT / '.state' / 'assets-manifest.yaml'
CHAPTERS_PATH = REPO_ROOT / 'chapters' / 'drafts'


def load_manifest():
    """Carga el manifest de assets."""
    with open(MANIFEST_PATH, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def test_manifest_exists():
    """El manifest debe existir."""
    assert MANIFEST_PATH.exists(), f"Manifest no encontrado: {MANIFEST_PATH}"
    print("[OK] test_manifest_exists")


def test_manifest_valid_yaml():
    """El manifest debe ser YAML valido."""
    try:
        manifest = load_manifest()
        assert manifest is not None
        print("[OK] test_manifest_valid_yaml")
    except yaml.YAMLError as e:
        assert False, f"YAML invalido: {e}"


def test_manifest_has_assets():
    """El manifest debe tener lista de assets."""
    manifest = load_manifest()
    assert 'assets' in manifest, "Falta clave 'assets'"
    assert isinstance(manifest['assets'], list), "'assets' debe ser lista"
    assert len(manifest['assets']) > 0, "Lista de assets vacia"
    print("[OK] test_manifest_has_assets")


def test_unique_ids():
    """Todos los IDs deben ser unicos."""
    manifest = load_manifest()
    ids = [a.get('id') for a in manifest['assets']]
    duplicates = [id for id in ids if ids.count(id) > 1]
    assert len(duplicates) == 0, f"IDs duplicados: {set(duplicates)}"
    print("[OK] test_unique_ids")


def test_required_fields():
    """Cada asset debe tener campos requeridos."""
    manifest = load_manifest()
    required = ['id', 'type', 'chapter', 'source', 'status']

    for asset in manifest['assets']:
        for field in required:
            assert field in asset, f"Asset '{asset.get('id', '?')}' sin campo '{field}'"

    print("[OK] test_required_fields")


def test_valid_types():
    """Los tipos deben ser validos."""
    manifest = load_manifest()
    valid_types = ['mermaid', 'table', 'figure']

    for asset in manifest['assets']:
        asset_type = asset.get('type')
        assert asset_type in valid_types, f"Tipo invalido '{asset_type}' en {asset['id']}"

    print("[OK] test_valid_types")


def test_valid_statuses():
    """Los status deben ser validos."""
    manifest = load_manifest()
    valid_statuses = ['pending', 'draft', 'review', 'ready', 'approved']

    for asset in manifest['assets']:
        status = asset.get('status')
        assert status in valid_statuses, f"Status invalido '{status}' en {asset['id']}"

    print("[OK] test_valid_statuses")


def test_chapters_exist():
    """Los capitulos referenciados deben existir."""
    manifest = load_manifest()

    for asset in manifest['assets']:
        chapter = asset.get('chapter', '')
        chapter_file = CHAPTERS_PATH / f"{chapter}.md"
        assert chapter_file.exists(), f"Capitulo no existe: {chapter} (asset: {asset['id']})"

    print("[OK] test_chapters_exist")


def test_sources_exist_for_non_pending():
    """Los archivos fuente deben existir para assets no-pending."""
    manifest = load_manifest()

    for asset in manifest['assets']:
        if asset.get('status') == 'pending':
            continue

        source = REPO_ROOT / asset['source']
        assert source.exists(), f"Fuente no existe: {asset['source']} (asset: {asset['id']})"

    print("[OK] test_sources_exist_for_non_pending")


def main():
    print("=" * 50)
    print("Tests de Assets Manifest")
    print("=" * 50)
    print()

    tests = [
        test_manifest_exists,
        test_manifest_valid_yaml,
        test_manifest_has_assets,
        test_unique_ids,
        test_required_fields,
        test_valid_types,
        test_valid_statuses,
        test_chapters_exist,
        test_sources_exist_for_non_pending,
    ]

    passed = 0
    failed = 0

    for test in tests:
        try:
            test()
            passed += 1
        except AssertionError as e:
            print(f"[FAIL] {test.__name__}: {e}")
            failed += 1
        except Exception as e:
            print(f"[ERROR] {test.__name__}: {e}")
            failed += 1

    print()
    print("=" * 50)
    print(f"Resultados: {passed} passed, {failed} failed")

    if failed > 0:
        sys.exit(1)
    else:
        print("Todos los tests pasaron")
        sys.exit(0)


if __name__ == '__main__':
    main()
