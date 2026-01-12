#!/usr/bin/env python3
"""
validate-assets.py - Validación del manifest de assets

Verifica:
1. Estructura YAML válida
2. Campos requeridos en cada asset
3. Existencia de archivos fuente (excepto status=pending)
4. IDs únicos
5. Capítulos referenciados existen
6. Markers en capítulos tienen asset correspondiente (futuro)

Uso:
    python3 build/validate-assets.py
    python3 build/validate-assets.py --verbose
"""

import yaml
import sys
import os
from pathlib import Path
from typing import Dict, List, Any

# Colores para output
class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    END = '\033[0m'

def load_manifest(manifest_path: Path) -> Dict[str, Any]:
    """Carga y parsea el manifest YAML."""
    with open(manifest_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def validate_asset_fields(asset: Dict[str, Any], index: int) -> List[str]:
    """Valida campos requeridos de un asset."""
    errors = []
    required_fields = ['id', 'type', 'chapter', 'source', 'status']
    
    for field in required_fields:
        if field not in asset:
            errors.append(f"Asset #{index}: falta campo requerido '{field}'")
    
    # Validar tipo conocido
    valid_types = ['mermaid', 'table', 'figure']
    if 'type' in asset and asset['type'] not in valid_types:
        errors.append(f"Asset '{asset.get('id', f'#{index}')}': tipo '{asset['type']}' no válido")
    
    # Validar status conocido
    valid_statuses = ['pending', 'draft', 'review', 'ready', 'approved']
    if 'status' in asset and asset['status'] not in valid_statuses:
        errors.append(f"Asset '{asset.get('id', f'#{index}')}': status '{asset['status']}' no válido")
    
    return errors

def validate_source_exists(asset: Dict[str, Any], base_path: Path) -> List[str]:
    """Verifica que el archivo fuente existe (si no es pending)."""
    errors = []
    
    if asset.get('status') == 'pending':
        return errors  # No validar existencia para pending
    
    source = asset.get('source', '')
    source_path = base_path / source
    
    if not source_path.exists():
        errors.append(f"Asset '{asset['id']}': archivo fuente no existe: {source}")
    
    return errors

def validate_unique_ids(assets: List[Dict[str, Any]]) -> List[str]:
    """Verifica que todos los IDs son únicos."""
    errors = []
    seen_ids = {}
    
    for i, asset in enumerate(assets):
        asset_id = asset.get('id', f'#{i}')
        if asset_id in seen_ids:
            errors.append(f"ID duplicado: '{asset_id}' (assets #{seen_ids[asset_id]} y #{i})")
        seen_ids[asset_id] = i
    
    return errors

def validate_chapters_exist(assets: List[Dict[str, Any]], chapters_path: Path) -> List[str]:
    """Verifica que los capítulos referenciados existen."""
    errors = []
    warnings = []
    
    for asset in assets:
        chapter = asset.get('chapter', '')
        if not chapter:
            continue
        
        # Buscar archivo del capítulo
        chapter_file = chapters_path / f"{chapter}.md"
        if not chapter_file.exists():
            warnings.append(f"Asset '{asset['id']}': capítulo '{chapter}' no encontrado en drafts/")
    
    return errors, warnings

def main():
    verbose = '--verbose' in sys.argv or '-v' in sys.argv
    
    # Paths
    script_dir = Path(__file__).parent
    base_path = script_dir.parent
    manifest_path = base_path / '.state' / 'assets-manifest.yaml'
    chapters_path = base_path / 'chapters' / 'drafts'
    
    print(f"{Colors.BLUE}=== Validación de Assets Manifest ==={Colors.END}\n")
    
    # Cargar manifest
    if not manifest_path.exists():
        print(f"{Colors.RED}ERROR: Manifest no encontrado: {manifest_path}{Colors.END}")
        sys.exit(1)
    
    try:
        manifest = load_manifest(manifest_path)
    except yaml.YAMLError as e:
        print(f"{Colors.RED}ERROR: YAML inválido: {e}{Colors.END}")
        sys.exit(1)
    
    assets = manifest.get('assets', [])
    print(f"Assets encontrados: {len(assets)}")
    
    all_errors = []
    all_warnings = []
    
    # Validaciones
    print("\n1. Validando campos requeridos...")
    for i, asset in enumerate(assets):
        errors = validate_asset_fields(asset, i)
        all_errors.extend(errors)
    
    print("2. Validando IDs únicos...")
    all_errors.extend(validate_unique_ids(assets))
    
    print("3. Validando existencia de archivos fuente...")
    for asset in assets:
        all_errors.extend(validate_source_exists(asset, base_path))
    
    print("4. Validando capítulos referenciados...")
    chapter_errors, chapter_warnings = validate_chapters_exist(assets, chapters_path)
    all_errors.extend(chapter_errors)
    all_warnings.extend(chapter_warnings)
    
    # Estadísticas
    print(f"\n{Colors.BLUE}=== Estadísticas ==={Colors.END}")
    status_counts = {}
    type_counts = {}
    for asset in assets:
        status = asset.get('status', 'unknown')
        asset_type = asset.get('type', 'unknown')
        status_counts[status] = status_counts.get(status, 0) + 1
        type_counts[asset_type] = type_counts.get(asset_type, 0) + 1
    
    print(f"Por tipo: {type_counts}")
    print(f"Por status: {status_counts}")
    
    # Resultados
    print(f"\n{Colors.BLUE}=== Resultados ==={Colors.END}")
    
    if all_warnings:
        print(f"\n{Colors.YELLOW}Advertencias ({len(all_warnings)}):{Colors.END}")
        for w in all_warnings:
            print(f"  ⚠️  {w}")
    
    if all_errors:
        print(f"\n{Colors.RED}Errores ({len(all_errors)}):{Colors.END}")
        for e in all_errors:
            print(f"  ❌ {e}")
        print(f"\n{Colors.RED}Validación FALLIDA{Colors.END}")
        sys.exit(1)
    else:
        print(f"\n{Colors.GREEN}✓ Validación exitosa{Colors.END}")
        sys.exit(0)

if __name__ == '__main__':
    main()
