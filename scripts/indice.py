#!/usr/bin/env python3
"""Genera fuentes/indice-fichas.csv a partir de las fichas: python scripts/indice.py

Una fila por ficha, para que una IA pueda filtrar por año, diseño o criterio diagnóstico
sin abrir las 167 fichas. Lo que manda es la ficha: el índice solo copia sus campos.
"""
from pathlib import Path
import csv, io, re, sys
root = Path(__file__).resolve().parents[1]
CAMPOS = ['archivo', 'anio', 'titulo', 'tipo_estudio', 'criterio', 'criterio_detalle', 'pmid', 'doi']
ETIQUETAS = [('NO PROPONE', 'NO PROPONE'), ('NO APLICA', 'NO APLICA'), ('LONGITUD', 'LONGITUD/ASPECTO'),
             ('FUNCIONAL', 'FUNCIONAL'), ('MIXTO', 'MIXTO'), ('PENDIENTE', 'PENDIENTE DE VERIFICAR')]


def campo(texto, *nombres):
    for n in nombres:
        m = re.search(rf'^- (?:\*\*)?{n}:?(?:\*\*)?:?\s*(.+)$', texto, re.M)
        if m:
            return m.group(1).strip()
    return ''


def limpia(s, n=None):
    s = re.sub(r'[`*]', '', s).strip()
    return s if n is None or len(s) <= n else s[:n].rsplit(' ', 1)[0] + ' […]'


def fila(path):
    t = path.read_text(encoding='utf-8')
    crit = limpia(campo(t, 'Criterio diagnóstico de anquiloglosia'))
    etiqueta = next((e for clave, e in ETIQUETAS if crit.upper().startswith(clave)),
                    'PENDIENTE DE VERIFICAR' if 'PENDIENTE' in crit.upper() else 'VER FICHA')
    pmid = re.search(r'PMID[^0-9\n]{0,6}(\d{5,8})', t)
    doi = re.search(r'\b(10\.\d{4,9}/[^\s`,\]]+)', t)
    doi = doi.group(1).rstrip('.;') if doi else ''
    while doi.endswith(')') and doi.count(')') > doi.count('('):
        doi = doi[:-1].rstrip('.')
    titulo = re.sub(r'^#\s*(Estudio:\s*)?', '', t.splitlines()[0]).strip()
    return {'archivo': path.name, 'anio': path.name[:4] if path.name[:4].isdigit() else '', 'titulo': titulo,
            'tipo_estudio': limpia(campo(t, 'Tipo de estudio', 'Diseño', 'Tipo'), 120),
            'criterio': etiqueta, 'criterio_detalle': limpia(crit, 200),
            'pmid': pmid.group(1) if pmid else '', 'doi': doi}


def generar():
    out = io.StringIO()
    w = csv.DictWriter(out, CAMPOS, lineterminator='\n')
    w.writeheader()
    for p in sorted((root / 'fuentes/articulos').glob('*.md')):
        if p.name != 'PLANTILLA.md':
            w.writerow(fila(p))
    return out.getvalue()


if __name__ == '__main__':
    (root / 'fuentes/indice-fichas.csv').write_text(generar(), encoding='utf-8', newline='\n')
    print('fuentes/indice-fichas.csv actualizado')
    sys.exit(0)
