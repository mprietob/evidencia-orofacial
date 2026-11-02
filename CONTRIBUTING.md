# Cómo proponer cambios

Se agradecen correcciones, estudios que falten y evidencia contraria. Para proponer algo, abre una «issue» en GitHub con la referencia completa (DOI o PMID) y qué cambiarías.

## Reglas para una ficha nueva

1. Registra el estudio en `fuentes/bibliografia.csv`.
2. Crea la ficha a partir de [fuentes/articulos/PLANTILLA.md](fuentes/articulos/PLANTILLA.md), con enlace verificable y datos de método.
3. Rellena siempre el campo «Criterio diagnóstico de anquiloglosia». Si no lo sabes, pon `PENDIENTE DE VERIFICAR`.
4. Copia solo cifras comprobadas. Citas literales, cortas y con atribución. Nunca texto completo ajeno.
5. Si la ficha cambia una objeción, actualiza sus dos caras: la evidencia a favor y la evidencia en contra.
6. Vídeos: usa [fuentes/videos/PLANTILLA.md](fuentes/videos/PLANTILLA.md). Resumen propio con enlace y minuto. Sin transcripciones completas.
7. Antes de enviar, ejecuta `python scripts/validar.py` y repasa [docs/REVIEW.md](docs/REVIEW.md).

## Lo que nunca entra

- Datos, fotos o historias de pacientes, aunque estén anonimizados.
- PDF de artículos con derechos de editorial.
- Figuras sin licencia abierta (CC BY, CC BY-SA o CC0). Las fotos de bocas, caras o cadáveres solo se enlazan, aunque su licencia permita copiarlas.
- Transcripciones completas de vídeos de terceros.
- Contraseñas, claves o tokens.
