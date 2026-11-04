# Cómo proponer cambios

**Esto no es una revisión sistemática cerrada:** puede haber artículos que aún no hemos leído o localizado. **El repositorio está privado** hasta que se autorice su apertura; por el momento, solo las personas con acceso podrán usar sus Issues. **Toda aportación pertinente es bienvenida**, también cuando cuestiona las hipótesis del proyecto. Queremos incorporarla al inventario con su referencia y, tras examinarla, a las fichas o síntesis que corresponda.

Para contribuir, basta con enviarnos el **DOI, PMID o enlace**, y, si quieres, el hallazgo que aporta, una objeción o una conexión con otros estudios. Puedes mandarlo por GitHub, con una «issue» y la plantilla «Proponer un artículo», o por Instagram a @dermaprieto si no tienes cuenta. **Toda aportación pertinente se incorporará a la biblioteca**, aunque contradiga otros hallazgos. Primero se comprobarán la referencia y los datos; si está duplicada se enlazará a la ficha existente.

**Buscamos conexiones:** un artículo puede respaldar A → B, otro B → C y otro C → D; aunque falte un estudio directo de A → D, esa cadena puede inspirar una hipótesis científica que merece investigar.

**Dos datos especialmente útiles:** cómo definió el estudio la anquiloglosia (**anatomía visible o limitación funcional**) y, cuando evalúe tratamiento, qué se hizo exactamente bajo la etiqueta de **cirugía** (**técnica, profundidad/extensión, intervención y cotratamientos**).

## Reglas para una ficha nueva

1. Registra el estudio en `fuentes/bibliografia.csv`.
2. Crea la ficha a partir de [fuentes/articulos/PLANTILLA.md](fuentes/articulos/PLANTILLA.md), con enlace verificable y datos de método.
3. Rellena siempre el campo «Criterio diagnóstico de anquiloglosia». Si no lo sabes, pon `PENDIENTE DE VERIFICAR`.
4. Copia solo cifras comprobadas. Citas literales, cortas y con atribución. Nunca texto completo ajeno.
5. Si la ficha cambia una objeción, actualiza sus dos caras: la evidencia a favor y la evidencia en contra.
6. Vídeos: usa [fuentes/videos/PLANTILLA.md](fuentes/videos/PLANTILLA.md). Resumen propio con enlace y minuto. Sin transcripciones completas.
7. Antes de enviar, ejecuta `python scripts/indice.py` (actualiza `fuentes/indice-fichas.csv`) y `python scripts/validar.py`, y repasa [docs/REVIEW.md](docs/REVIEW.md).

Si el cambio lo hace un agente de IA, los pasos de cada tarea están en [docs/TAREAS-AGENTES.md](docs/TAREAS-AGENTES.md).

## Lo que nunca entra

- Datos, fotos o historias de pacientes, aunque estén anonimizados.
- PDF de artículos con derechos de editorial.
- Figuras sin licencia abierta (CC BY, CC BY-SA o CC0). Las fotos de bocas, caras o cadáveres solo se enlazan, aunque su licencia permita copiarlas.
- Transcripciones completas de vídeos de terceros.
- Contraseñas, claves o tokens.
