# Guía de tareas para agentes

Pasos para un agente de IA (Claude Code, Codex, Gemini, Copilot u otro) que responda con esta biblioteca o la mantenga. Las reglas de [AGENTS.md](../AGENTS.md) mandan sobre esta guía. Si algo de aquí choca con ellas, sigue AGENTS.md y avisa.

## Límites para cualquier tarea

- **No publiques nada.** No hagas `git push`, no abras «pull requests», no crees repositorios ni cambies su visibilidad sin el sí expreso de la persona que mantiene la biblioteca. Los cambios se quedan en commits locales.
- **Nada de pacientes.** Ni datos, ni fotos, ni casos, ni historias, aunque estén anonimizados. Tampoco de menores ni de familiares.
- **Nada con derechos de terceros.** Ni PDF de artículos con derechos de editorial, ni transcripciones de vídeos, ni figuras sin licencia CC BY, CC BY-SA o CC0. Citas literales cortas, con atribución.
- **Ningún secreto.** Ni contraseñas, ni claves, ni tokens, ni configuración de conectores.
- **No inventes.** Si un dato no está comprobado, escribe `PENDIENTE DE VERIFICAR` y di cómo comprobarlo.
- **Valida antes de cada commit:** `python scripts/validar.py` debe terminar con «errores: 0».

**Lectura previa obligatoria:** [ENFOQUE-CRITICO.md](ENFOQUE-CRITICO.md). Respuestas ordinarias breves; ante objeciones, comprobar la pertinencia de medidas y límites con el mismo rigor para hallazgos positivos y negativos.

## Mapa rápido

| Para | Lee |
|---|---|
| Mentalidad y protocolo de objeciones | [ENFOQUE-CRITICO.md](ENFOQUE-CRITICO.md) |
| Saber qué hay | [llms.txt](../llms.txt) |
| Filtrar estudios por año, diseño o criterio diagnóstico | [fuentes/indice-fichas.csv](../fuentes/indice-fichas.csv) |
| Ver la referencia completa | [fuentes/bibliografia.csv](../fuentes/bibliografia.csv) |
| El detalle de un estudio | `fuentes/articulos/<archivo>.md` |
| Debates con evidencia a favor y en contra | [objeciones/](../objeciones/) |
| Grado de apoyo de cada afirmación | [conocimiento/afirmaciones.md](../conocimiento/afirmaciones.md) |
| Sociedades científicas y guías | [conocimiento/sociedades-cientificas.md](../conocimiento/sociedades-cientificas.md) |
| Opinión de Soroush Zaghi | [expertos/soroush-zaghi/](../expertos/soroush-zaghi/README.md) |
| Lo que falta | [PREGUNTAS-ABIERTAS.md](PREGUNTAS-ABIERTAS.md) y [BUSQUEDA-2026-11.md](BUSQUEDA-2026-11.md) |

## 1. Responder una pregunta

1. Busca el tema en `llms.txt`. Si es un debate conocido, empieza por su objeción en `objeciones/`.
2. Filtra en `fuentes/indice-fichas.csv` los estudios del tema. La columna `criterio` dice cómo se diagnosticó la anquiloglosia: `FUNCIONAL`, `LONGITUD/ASPECTO`, `MIXTO`, `NO APLICA`, `NO PROPONE` (documentos que no proponen criterio) o `PENDIENTE DE VERIFICAR`.
3. Abre cada ficha que vayas a citar. El índice es un resumen: lo que vale es la ficha.
4. Contesta con esta estructura:
   - **Respuesta corta**, en una o dos frases.
   - **Qué dice la evidencia**, ordenada por diseño: revisiones y ensayos primero, después observacionales, casos y opinión.
   - **Por cada estudio:** autor, año, PMID o DOI, la ficha, su criterio diagnóstico y su resultado.
   - **Evidencia en contra o limitaciones decisivas, cuando sean pertinentes para la pregunta.**
   - **Interpretación**, si la hay, diferenciada del resultado.
   - **Cuestiones abiertas**, solo si aportan algo concreto.
5. Si la pregunta es sobre una persona concreta, no diagnostiques ni recomiendes tratamiento. Explica qué dice la evidencia en general y recomienda una valoración profesional en persona.
6. Si no está en la biblioteca, dilo. No rellenes con conocimiento general sin avisar de que no sale de aquí.

## 2. Fichar un estudio nuevo

1. **Comprueba que no esté.** Busca su PMID o DOI en `fuentes/bibliografia.csv` y en `fuentes/indice-fichas.csv`.
2. **Lee la fuente.** Al menos el resumen en PubMed. El texto completo si es de acceso abierto. Sin cuenta y sin clave:
   - Metadatos: `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&id=<PMID>&retmode=json`
   - Resumen: `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=<PMID>&rettype=abstract&retmode=text`
   - Licencia y acceso abierto: `https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:<PMID>%20AND%20SRC:MED&resultType=core&format=json` (campos `license`, `isOpenAccess` y `pmcid`).
3. **Añade una fila a `fuentes/bibliografia.csv`:** `id,tipo,autores,anio,titulo,doi,pmid,tema,estado_lectura`. El `id` es el apellido del primer autor en mayúsculas y el año, por ejemplo `DHAR2026`. Si ya existe, añade una letra.
4. **Crea la ficha** copiando [fuentes/articulos/PLANTILLA.md](../fuentes/articulos/PLANTILLA.md). Nombre del archivo: `<año>-<apellido>-<tema-corto>.md`, en minúsculas y sin tildes.
5. **Rellena el criterio diagnóstico.** Empieza el campo por la etiqueta (`FUNCIONAL`, `LONGITUD/ASPECTO`, `MIXTO`, `NO APLICA` o `PENDIENTE DE VERIFICAR`) y di de dónde sale el dato. Si el resumen no lo dice, es `PENDIENTE DE VERIFICAR`. No lo deduzcas.
6. **Copia solo cifras comprobadas** en la fuente que has leído. Di en «Estado de lectura» qué leíste y cuándo. Da protagonismo a los resultados: no rellenes la ficha con advertencias genéricas ni repitas en varios apartados una misma limitación.
7. **Sección «Figuras»:** ver la tarea 6.
8. **Si el estudio toca una objeción,** actualízala (tarea 4).
9. **Si sale de la búsqueda,** cambia su `estado` a `fichado` en `docs/busqueda-2026-11.csv` y quítalo de la lista de pendientes de `BUSQUEDA-2026-11.md`.
10. Ejecuta `python scripts/indice.py` y después `python scripts/validar.py`.

## 3. Poner al día la búsqueda bibliográfica

1. Repite la estrategia de [BUSQUEDA-2026-11.md](BUSQUEDA-2026-11.md) desde el día siguiente a la última búsqueda: `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=<consulta>&retmax=500&retmode=json`.
2. Crea `docs/BUSQUEDA-<año>-<mes>.md` y su CSV con las mismas columnas: `pmid,fecha,revista,titulo,tipo_pubmed,filtro_diseno,estado`.
3. Marca como `fichado` lo que ya tenga ficha. Separa los `pendiente prioritario` (revisiones, ensayos, guías, consensos) de los `pendiente de cribado`.
4. Enlaza la nueva búsqueda desde `llms.txt` y desde `docs/PREGUNTAS-ABIERTAS.md`.

## 4. Actualizar una objeción o una afirmación

1. Sigue [ENFOQUE-CRITICO.md](ENFOQUE-CRITICO.md): identifica hipótesis, medida y desenlace. Analiza limitaciones concretas cuando afecten a la objeción, sin enumerar automáticamente todo lo que el estudio no demuestra.
2. Añade el estudio en la cara que le toque: evidencia a favor o en contra. Si matiza las dos, ponlo en las dos.
3. Di su criterio diagnóstico. Longitud/aspecto no resuelve por sí solo la función; tampoco una prueba funcional parcial resuelve todas las funciones.
4. Distingue límite documentado de hipótesis de sesgo: una apertura máxima reducida **podría** alterar TRMR, pero no afirmes que ocurriera en un estudio sin datos.
5. **No cambies el nivel de certeza sin justificarlo** con estudios concretos.
6. No conviertas «no hay evidencia suficiente» en «no hay efecto», ni al revés.
7. Si cambia el grado de apoyo de una afirmación, actualiza también [conocimiento/afirmaciones.md](../conocimiento/afirmaciones.md).

## 5. Añadir un documento de una sociedad científica

1. Fíchalo como un estudio (tarea 2). En «Tipo de estudio» di qué es: guía, consenso, posicionamiento o informe clínico.
2. En el criterio diagnóstico, si el documento no propone ninguno, empieza por `NO PROPONE` y di qué dice al respecto.
3. Añade una fila a la tabla de [conocimiento/sociedades-cientificas.md](../conocimiento/sociedades-cientificas.md). Si estaba en «Lo que no se ha podido confirmar», quítalo de ahí.
4. La «Lectura de conjunto» de ese archivo es interpretación. Solo se cambia si el documento nuevo la cambia, y diciendo por qué.

## 6. Figuras

1. Comprueba la licencia del artículo en Europe PMC (tarea 2, paso 2). Solo se copian figuras con licencia CC BY, CC BY-SA o CC0.
2. **Fotos de bocas, caras, cadáveres o de un caso concreto: solo enlace,** aunque la licencia permita copiarlas.
3. Copia sin modificar en `figuras/<ID>-fig<N>.jpg` y añade su fila a la tabla de [figuras/README.md](../figuras/README.md): archivo, qué muestra, ficha, enlace en PMC, autores y licencia.
4. En la sección «Figuras» de la ficha, describe cada figura con palabras y da el enlace directo. Si no la has visto, di que no está revisada.

## 7. Soroush Zaghi

- **Para responder:** usa [zaghi.jsonl](../expertos/soroush-zaghi/zaghi.jsonl) o los archivos por tema. Cada entrada tiene `id`, `area`, `tipo`, `afirmacion`, `videos` (título, enlace y minuto), `anio_charla`, `pmid`, `verificacion` y `cita_corta`. Di siempre que es opinión de experto, el vídeo y si está verificada. Si choca con un estudio, da la cifra del estudio ([discrepancias.md](../expertos/soroush-zaghi/discrepancias.md)).
- **Para completar un minuto** que falta: abre el vídeo, busca la frase en la transcripción de YouTube y cambia `minuto` en `zaghi.jsonl` y en el archivo del tema.
- **Para añadir afirmaciones:** resumen propio y cita corta, con el vídeo y su enlace. Nunca la transcripción. Nada sacado de testimonios ni de casos de pacientes. Los vídeos tienen la licencia estándar de YouTube.

## 8. Cerrar el trabajo

1. `python scripts/indice.py` si has tocado alguna ficha.
2. `python scripts/validar.py`: debe dar «errores: 0».
3. Repasa [REVIEW.md](REVIEW.md).
4. Haz un commit local con un mensaje que diga qué cambió. No hagas `push`.
5. Resume a la persona qué has cambiado, qué queda `PENDIENTE DE VERIFICAR` y qué no has podido comprobar.
