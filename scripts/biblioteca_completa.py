#!/usr/bin/env python3
"""Junta la biblioteca en biblioteca-completa.md para subirla a una IA. Ejecutar tras cada cambio: python scripts/biblioteca_completa.py"""
from pathlib import Path
import re, datetime
root = Path(__file__).resolve().parents[1]
def body(p):
    t = p.read_text(encoding='utf-8')
    t = re.sub(r'\[([^\]]+)\]\((?!https?://|#)[^)]*\)', r'\1', t)  # enlaces relativos: solo texto
    return t.strip()
parts = ["# Evidencia orofacial: biblioteca completa",
         f"Generado el {datetime.date.today():%d/%m/%Y} desde https://github.com/mprietob/evidencia-orofacial . Un solo archivo para subir a ChatGPT, Claude, Gemini o NotebookLM.",
         "## Reglas para la IA que lea este archivo", body(root/'AGENTS.md'),
         "## Enfoque crítico", body(root/'docs/ENFOQUE-CRITICO.md'),
         "## Qué es esta biblioteca", body(root/'README.md')]
for sec, folder in [("Síntesis por tema", 'conocimiento'), ("Objeciones (a favor y en contra)", 'objeciones'),
                    ("Hipótesis abiertas (no demostradas)", 'hipotesis'), ("Opinión de expertos (no son estudios)", 'expertos'),
                    ("Fichas de estudios", 'fuentes/articulos')]:
    parts.append(f"# {sec}")
    for p in sorted((root/folder).rglob('*.md')):
        if p.name == 'PLANTILLA.md': continue
        parts.append(f"<!-- archivo: {p.relative_to(root).as_posix()} -->\n" + body(p))
out = root/'biblioteca-completa.md'
out.write_text("\n\n---\n\n".join(parts) + "\n", encoding='utf-8')
print('biblioteca-completa.md:', round(out.stat().st_size/1024), 'KB')
