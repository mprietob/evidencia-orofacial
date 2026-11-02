#!/usr/bin/env python3
"""Control local antes de publicar, sin dependencias ni servicios externos: python scripts/validar.py"""
from pathlib import Path
import csv, json, re, sys
root = Path(__file__).resolve().parents[1]
issues = []
paths = [p for p in root.rglob('*') if p.is_file() and '.git' not in p.parts]

# Archivos que no deben estar en un repositorio público
for path in paths:
    if path.suffix.lower() in {'.pdf', '.docx', '.epub', '.mp4', '.mov', '.mp3', '.wav', '.srt', '.vtt', '.zip', '.env'}:
        issues.append(f'Archivo no permitido: {path.relative_to(root)}')

# Enlaces locales rotos, restos del material privado y posibles secretos
PRIVADO = re.compile(r'content-research|estudio-propio|estudio propio|Todo anquiloglosia|Gestión de clínicas|C:\\Users|/c/Users', re.I)
SECRETO = re.compile(r'(ghp_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|sk-[A-Za-z0-9-]{20,}|AKIA[0-9A-Z]{16}|-----BEGIN [A-Z ]*PRIVATE KEY)')
for path in paths:
    if path.suffix.lower() not in {'.md', '.txt', '.csv', '.jsonl', '.py'}:
        continue
    content = path.read_text(encoding='utf-8')
    rel = path.relative_to(root)
    if rel.as_posix() != 'scripts/validar.py' and PRIVADO.search(content):
        issues.append(f'Referencia al material privado en {rel}: {PRIVADO.search(content).group(0)}')
    if SECRETO.search(content):
        issues.append(f'Posible secreto en {rel}')
    if path.suffix.lower() != '.md':
        continue
    for dst in re.findall(r'\[[^\]]+\]\(([^)]+)\)', content):
        if '://' in dst or dst.startswith('#') or dst.startswith('mailto:'):
            continue
        if not (path.parent / dst.split('#')[0]).exists():
            issues.append(f'Enlace local roto en {rel}: {dst}')

# Bibliografía
with (root / 'fuentes/bibliografia.csv').open(encoding='utf-8') as fh:
    rows = list(csv.DictReader(fh))
ids = [row['id'] for row in rows]
if len(ids) != len(set(ids)): issues.append('IDs bibliográficos duplicados')
dois = [row['doi'].lower() for row in rows if row['doi']]
if len(dois) != len(set(dois)): issues.append('DOIs duplicados')

# Cada ficha dice qué criterio diagnóstico usa
fichas = [p for p in (root / 'fuentes/articulos').glob('*.md') if p.name != 'PLANTILLA.md']
for f in fichas:
    if 'Criterio diagnóstico de anquiloglosia' not in f.read_text(encoding='utf-8'):
        issues.append(f'Ficha sin criterio diagnóstico: {f.name}')

# El índice de fichas está al día
sys.path.insert(0, str(root / 'scripts'))
from indice import generar
indice = root / 'fuentes/indice-fichas.csv'
if not indice.exists() or indice.read_text(encoding='utf-8') != generar():
    issues.append('fuentes/indice-fichas.csv no está al día: ejecuta python scripts/indice.py')

# Cada figura copiada tiene su fila de crédito y licencia
tabla = (root / 'figuras/README.md').read_text(encoding='utf-8')
figuras = sorted((root / 'figuras').glob('*.jpg'))
for img in figuras:
    fila = next((l for l in tabla.splitlines() if l.startswith(f'| [{img.name}]')), None)
    if not fila or 'CC BY' not in fila:
        issues.append(f'Figura sin crédito o sin licencia CC BY en figuras/README.md: {img.name}')

# Base de Zaghi: JSON válido y cada vídeo con enlace de YouTube
zaghi = root / 'expertos/soroush-zaghi/zaghi.jsonl'
n_zaghi = 0
if zaghi.exists():
    for i, line in enumerate(zaghi.read_text(encoding='utf-8').splitlines(), 1):
        try:
            rec = json.loads(line)
        except json.JSONDecodeError:
            issues.append(f'zaghi.jsonl línea {i}: JSON no válido'); continue
        n_zaghi += 1
        for v in rec.get('videos', []):
            if not v.get('url', '').startswith('https://www.youtube.com/watch?v='):
                issues.append(f"zaghi.jsonl {rec.get('id')}: vídeo sin URL de YouTube")

print(f'Verificados {len(paths)} archivos, {len(rows)} referencias, {len(fichas)} fichas, {len(figuras)} figuras y {n_zaghi} afirmaciones de Zaghi; errores: {len(issues)}')
for issue in issues: print('ERROR:', issue)
sys.exit(1 if issues else 0)
