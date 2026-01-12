#!/usr/bin/env python3
"""
preprocess-chapters.py - Inserta assets en capítulos

Busca markers {{tipo:id}} en capítulos y los reemplaza con
el contenido generado apropiado para el formato de salida.

Markers soportados:
- {{diag:id}} - Diagrama Mermaid (inserta SVG o referencia)
- {{tabla:id}} - Tabla (inserta LaTeX o Markdown)
- {{fig:id}} - Figura (inserta imagen)

Uso:
    python3 build/preprocess-chapters.py --format latex
    python3 build/preprocess-chapters.py --format markdown
    python3 build/preprocess-chapters.py --chapter B10-implementacion
"""

import yaml
import re
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

# Regex para markers
MARKER_PATTERN = re.compile(r'\{\{(diag|tabla|fig):([a-zA-Z0-9_-]+)\}\}')

def load_manifest(manifest_path: Path) -> Dict[str, Any]:
    with open(manifest_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def get_asset_by_id(assets: List[Dict], asset_id: str) -> Optional[Dict]:
    """Busca asset por ID (parcial o completo)."""
    for asset in assets:
        if asset['id'] == asset_id or asset['id'].endswith(f'-{asset_id}'):
            return asset
    return None

def generate_latex_include(asset: Dict, base_path: Path) -> str:
    """Genera código LaTeX para incluir el asset."""
    asset_type = asset['type']
    display = asset.get('display', {})
    title = display.get('title', '')
    caption = display.get('caption', '')
    width = display.get('width', '0.9\\textwidth')
    
    if asset_type == 'mermaid':
        # SVG generado
        svg_path = base_path / 'assets' / 'generated' / 'diagrams' / f"{Path(asset['source']).stem}.svg"
        if svg_path.exists():
            latex = f"""
\\begin{{figure}}[htbp]
\\centering
\\includesvg[width={width}]{{{svg_path}}}
\\caption{{{caption}}}
\\end{{figure}}
"""
        else:
            latex = f"% Asset {asset['id']}: SVG no generado"
    
    elif asset_type == 'table':
        # LaTeX generado
        tex_path = base_path / 'assets' / 'generated' / 'tables' / f"{Path(asset['source']).stem}.latex"
        if tex_path.exists():
            with open(tex_path, 'r') as f:
                latex = f.read()
        else:
            latex = f"% Asset {asset['id']}: tabla no generada"
    
    elif asset_type == 'figure':
        fig_path = base_path / asset['source']
        latex = f"""
\\begin{{figure}}[htbp]
\\centering
\\includegraphics[width={width}]{{{fig_path}}}
\\caption{{{caption}}}
\\end{{figure}}
"""
    else:
        latex = f"% Asset {asset['id']}: tipo no soportado"
    
    return latex

def generate_markdown_include(asset: Dict, base_path: Path) -> str:
    """Genera Markdown para incluir el asset."""
    asset_type = asset['type']
    display = asset.get('display', {})
    title = display.get('title', '')
    caption = display.get('caption', '')
    
    if asset_type == 'mermaid':
        # Incluir el código Mermaid directamente
        source_path = base_path / asset['source']
        if source_path.exists():
            with open(source_path, 'r') as f:
                mermaid_code = f.read()
            md = f"""
```mermaid
{mermaid_code}
```
*{caption}*
"""
        else:
            md = f"<!-- Asset {asset['id']}: fuente no encontrada -->"
    
    elif asset_type == 'table':
        # Convertir YAML a Markdown table
        source_path = base_path / asset['source']
        if source_path.exists():
            with open(source_path, 'r') as f:
                table_def = yaml.safe_load(f)
            
            columns = table_def.get('columns', [])
            rows = table_def.get('rows', [])
            
            # Header
            headers = [col.get('header', col.get('key', '')) for col in columns]
            md_lines = ['| ' + ' | '.join(headers) + ' |']
            md_lines.append('| ' + ' | '.join(['---'] * len(headers)) + ' |')
            
            # Rows
            for row in rows:
                cells = [str(row.get(col['key'], '')) for col in columns]
                md_lines.append('| ' + ' | '.join(cells) + ' |')
            
            md = '\n'.join(md_lines) + f'\n\n*{caption}*\n'
        else:
            md = f"<!-- Asset {asset['id']}: fuente no encontrada -->"
    
    elif asset_type == 'figure':
        fig_path = asset['source']
        md = f"![{title}]({fig_path})\n\n*{caption}*\n"
    
    else:
        md = f"<!-- Asset {asset['id']}: tipo no soportado -->"
    
    return md

def process_chapter(chapter_path: Path, assets: List[Dict], base_path: Path, output_format: str) -> str:
    """Procesa un capítulo reemplazando markers con assets."""
    with open(chapter_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    def replace_marker(match):
        marker_type = match.group(1)
        asset_id = match.group(2)
        
        asset = get_asset_by_id(assets, asset_id)
        if not asset:
            return f"<!-- Asset no encontrado: {asset_id} -->"
        
        if output_format == 'latex':
            return generate_latex_include(asset, base_path)
        else:
            return generate_markdown_include(asset, base_path)
    
    processed = MARKER_PATTERN.sub(replace_marker, content)
    return processed

def main():
    # Parse args
    output_format = 'markdown'
    filter_chapter = None
    
    for i, arg in enumerate(sys.argv[1:], 1):
        if arg == '--format' and i < len(sys.argv) - 1:
            output_format = sys.argv[i + 1]
        elif arg == '--chapter' and i < len(sys.argv) - 1:
            filter_chapter = sys.argv[i + 1]
    
    # Paths
    script_dir = Path(__file__).parent
    base_path = script_dir.parent
    manifest_path = base_path / '.state' / 'assets-manifest.yaml'
    chapters_path = base_path / 'chapters' / 'drafts'
    output_path = base_path / 'chapters' / 'processed'
    
    print(f"{Colors.BLUE}=== Preprocesamiento de Capítulos ==={Colors.END}")
    print(f"Formato: {output_format}\n")
    
    # Crear directorio de salida
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Cargar manifest
    manifest = load_manifest(manifest_path)
    assets = manifest.get('assets', [])
    
    # Encontrar capítulos con markers
    chapters = list(chapters_path.glob('*.md'))
    if filter_chapter:
        chapters = [c for c in chapters if filter_chapter in c.stem]
    
    processed_count = 0
    for chapter in chapters:
        with open(chapter, 'r') as f:
            content = f.read()
        
        # Verificar si tiene markers
        if MARKER_PATTERN.search(content):
            print(f"Procesando: {chapter.name}")
            processed = process_chapter(chapter, assets, base_path, output_format)
            
            output_file = output_path / chapter.name
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(processed)
            
            print(f"  {Colors.GREEN}✓ → {output_file}{Colors.END}")
            processed_count += 1
    
    print(f"\n{Colors.BLUE}Capítulos procesados: {processed_count}{Colors.END}")

if __name__ == '__main__':
    main()
