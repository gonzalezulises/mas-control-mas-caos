#!/usr/bin/env python3
"""
generate-assets.py - Genera assets visuales desde fuentes

Procesa:
1. Mermaid → SVG (requiere mmdc instalado)
2. YAML tables → LaTeX
3. Figures → copia a generated/

Uso:
    python3 build/generate-assets.py
    python3 build/generate-assets.py --type mermaid
    python3 build/generate-assets.py --id diag-B10-fases
"""

import yaml
import subprocess
import shutil
import sys
import os
from pathlib import Path
from typing import Dict, List, Any, Optional

class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    END = '\033[0m'

def load_manifest(manifest_path: Path) -> Dict[str, Any]:
    with open(manifest_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def generate_mermaid(source: Path, output: Path) -> bool:
    """Genera SVG desde archivo Mermaid usando mmdc."""
    try:
        # Verificar que mmdc está instalado
        result = subprocess.run(
            ['mmdc', '-i', str(source), '-o', str(output), '-b', 'transparent'],
            capture_output=True,
            text=True
        )
        if result.returncode != 0:
            print(f"  {Colors.RED}Error mmdc: {result.stderr}{Colors.END}")
            return False
        return True
    except FileNotFoundError:
        print(f"  {Colors.RED}Error: mmdc no instalado. Instalar con: npm install -g @mermaid-js/mermaid-cli{Colors.END}")
        return False

def generate_table_latex(source: Path, output: Path) -> bool:
    """Genera LaTeX desde definición YAML de tabla."""
    try:
        with open(source, 'r', encoding='utf-8') as f:
            table_def = yaml.safe_load(f)
        
        title = table_def.get('title', '')
        columns = table_def.get('columns', [])
        rows = table_def.get('rows', [])
        
        # Generar LaTeX
        latex = []
        latex.append(r'\begin{table}[htbp]')
        latex.append(r'\centering')
        if title:
            latex.append(f'\\caption{{{title}}}')
        
        # Formato de columnas
        col_format = '|' + '|'.join(['l'] * len(columns)) + '|'
        latex.append(f'\\begin{{tabular}}{{{col_format}}}')
        latex.append(r'\hline')
        
        # Headers
        headers = [col.get('header', col.get('key', '')) for col in columns]
        latex.append(' & '.join([f'\\textbf{{{h}}}' for h in headers]) + r' \\')
        latex.append(r'\hline')
        
        # Rows
        for row in rows:
            cells = [str(row.get(col['key'], '')) for col in columns]
            latex.append(' & '.join(cells) + r' \\')
        
        latex.append(r'\hline')
        latex.append(r'\end{tabular}')
        latex.append(r'\end{table}')
        
        with open(output, 'w', encoding='utf-8') as f:
            f.write('\n'.join(latex))
        
        return True
    except Exception as e:
        print(f"  {Colors.RED}Error generando tabla: {e}{Colors.END}")
        return False

def copy_figure(source: Path, output: Path) -> bool:
    """Copia figura al directorio de generados."""
    try:
        shutil.copy2(source, output)
        return True
    except Exception as e:
        print(f"  {Colors.RED}Error copiando figura: {e}{Colors.END}")
        return False

def process_asset(asset: Dict[str, Any], base_path: Path, asset_types: Dict[str, Any]) -> bool:
    """Procesa un asset individual."""
    asset_id = asset['id']
    asset_type = asset['type']
    source = base_path / asset['source']
    status = asset.get('status', 'pending')
    
    # Skip pending assets
    if status == 'pending':
        print(f"  {Colors.YELLOW}⏭️  {asset_id}: status pending, saltando{Colors.END}")
        return True
    
    # Verificar fuente existe
    if not source.exists():
        print(f"  {Colors.RED}❌ {asset_id}: fuente no existe: {source}{Colors.END}")
        return False
    
    # Determinar output
    type_config = asset_types.get(asset_type, {})
    output_dir = base_path / type_config.get('output_dir', f'assets/generated/{asset_type}')
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Determinar extensión de salida
    output_format = type_config.get('output_format', '')
    if output_format:
        output_file = output_dir / f"{source.stem}.{output_format}"
    else:
        output_file = output_dir / source.name
    
    # Procesar según tipo
    success = False
    if asset_type == 'mermaid':
        success = generate_mermaid(source, output_file)
    elif asset_type == 'table':
        success = generate_table_latex(source, output_file)
    elif asset_type == 'figure':
        success = copy_figure(source, output_file)
    else:
        print(f"  {Colors.YELLOW}⚠️  {asset_id}: tipo '{asset_type}' no soportado{Colors.END}")
        return False
    
    if success:
        print(f"  {Colors.GREEN}✓ {asset_id} → {output_file.name}{Colors.END}")
    
    return success

def main():
    # Parse args
    filter_type = None
    filter_id = None
    for i, arg in enumerate(sys.argv[1:], 1):
        if arg == '--type' and i < len(sys.argv) - 1:
            filter_type = sys.argv[i + 1]
        elif arg == '--id' and i < len(sys.argv) - 1:
            filter_id = sys.argv[i + 1]
    
    # Paths
    script_dir = Path(__file__).parent
    base_path = script_dir.parent
    manifest_path = base_path / '.state' / 'assets-manifest.yaml'
    
    print(f"{Colors.BLUE}=== Generación de Assets ==={Colors.END}\n")
    
    # Cargar manifest
    manifest = load_manifest(manifest_path)
    assets = manifest.get('assets', [])
    asset_types = manifest.get('asset_types', {})
    
    # Filtrar si aplica
    if filter_type:
        assets = [a for a in assets if a.get('type') == filter_type]
        print(f"Filtrado por tipo: {filter_type}")
    if filter_id:
        assets = [a for a in assets if filter_id in a.get('id', '')]
        print(f"Filtrado por ID: {filter_id}")
    
    print(f"Assets a procesar: {len(assets)}\n")
    
    # Procesar
    success_count = 0
    error_count = 0
    skip_count = 0
    
    for asset in assets:
        if asset.get('status') == 'pending':
            skip_count += 1
        elif process_asset(asset, base_path, asset_types):
            success_count += 1
        else:
            error_count += 1
    
    # Resumen
    print(f"\n{Colors.BLUE}=== Resumen ==={Colors.END}")
    print(f"  Generados: {success_count}")
    print(f"  Saltados (pending): {skip_count}")
    print(f"  Errores: {error_count}")
    
    if error_count > 0:
        sys.exit(1)

if __name__ == '__main__':
    main()
