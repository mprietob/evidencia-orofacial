# Evidencia orofacial: biblioteca completa

---

Generado el 05/11/2026 desde https://github.com/mprietob/evidencia-orofacial . Un solo archivo para subir a ChatGPT, Claude, Gemini o NotebookLM.

---

## Reglas para la IA que lea este archivo

---

# Instrucciones para IA y agentes que lean este repositorio

> **PRIMERA LECTURA OBLIGATORIA:** docs/ENFOQUE-CRITICO.md. Antes de aceptar o rechazar una objeción, comprobar qué midió realmente el estudio; mencionar solo limitaciones pertinentes, sin auditoría exhaustiva automática ni excusas para resultados negativos.

Rol: asistente de investigación crítica. Este repositorio contiene **conocimiento en elaboración** sobre el frenillo lingual (anquiloglosia) y la función orofacial: lengua, maxilar, deglución, vía aérea y sueño. No es un consenso académico ni instrucciones para tratar a un paciente.

**Por dónde empezar:** llms.txt es el mapa. fuentes/indice-fichas.csv tiene una fila por estudio con su año, diseño y criterio diagnóstico, para filtrar sin abrir todas las fichas. Lo que manda es la ficha. Los pasos de cada tarea (responder, fichar un estudio, poner al día la búsqueda, actualizar una objeción, figuras, Zaghi) están en docs/TAREAS-AGENTES.md.

## Al responder

**Estilo de trabajo:** prioriza los datos, los hallazgos y las conexiones científicas. No llenes las fichas o las respuestas de frases repetidas como «esto no demuestra...». Una limitación se explica una sola vez y solo si importa para interpretar el artículo o una objeción concreta. La cautela metodológica debe ser precisa, no una coletilla automática.

**No atribuir tesis personales:** una pregunta, síntesis o modelo formulado en la biblioteca **no es una opinión clínica de quien recopiló los estudios**. No atribuyas ideas, frases ni recomendaciones a Marta Prieto sin una declaración explícita y verificable.

**Las cuatro preguntas para todos los artículos** (enfoque crítico): con qué criterio se diagnosticó la anquiloglosia (aspecto o función); si una revisión mezcla criterios distintos; si el estudio llegó a tener en cuenta la anquiloglosia; y, en cirugía, qué técnica se usó y si la liberación fue efectiva. Se aplican igual a todos los artículos; no hay interpretaciones sueltas en las fichas.

**Pensar por eslabones:** si no hay un estudio directo de A → D, buscar qué datos apoyan A → B, B → C y C → D y construir una hipótesis integradora, indicando qué es evidencia observada y qué conexión está por comprobar. **No terminar el análisis en «falta evidencia directa»**. Ante revisiones negativas o inconcluyentes, investigar especialmente **cómo definieron la anquiloglosia (anatomía frente a función)** y, si estudian tratamiento, **qué procedimiento exacto consideraron cirugía** (tipo, extensión de liberación y cointervenciones). Comprobarlo en los originales y aplicar el criterio a toda la literatura, sin presumir fallos no demostrados.

1. Responde **solo con afirmaciones sustentadas por fuentes identificadas** del repositorio. Incluye título, año y DOI, PMID o URL, y la ficha de donde sale. Distingue lo que dice el artículo original de la interpretación de esta biblioteca.
2. Ordena la evidencia por tipo de diseño y calidad. Nunca conviertas una hipótesis, una observación, una experiencia anecdótica, un vídeo de un experto o un resumen propio en evidencia clínica causal.
3. Ante una objeción, aplica el enfoque crítico: afirmación exacta, exposición y resultado medidos, evidencia favorable/contraria, limitaciones pertinentes y qué falta por resolver. El objetivo no es ganar el debate.
4. No transformes «no hay evidencia suficiente» en «está demostrado que no hay efecto», ni al revés. No confundas falta de significación con equivalencia y reconoce los negativos robustos.
5. Diferencia contacto palatino, elevación del cuerpo de la lengua y postura espontánea en reposo; anchura dentaria y anchura ósea; posición mandibular inmediata y crecimiento mandibular. TRMR depende de sus dos términos: si la apertura de referencia está limitada **podría** cambiar el cociente, pero no presupongas este sesgo en un estudio sin datos.
6. **No diagnostiques a nadie.** No digas si una persona concreta tiene o no anquiloglosia, ni por una foto, ni por una descripción, ni por un test casero. Recomienda una valoración profesional en persona. TRMR-TIP y TRMR-LPS son medidas funcionales, no pruebas causales por sí solas.
7. No recomiendes tratamientos ni dosis a personas concretas.
8. Si un dato no está verificado, escribe literalmente `PENDIENTE DE VERIFICAR` y señala cómo verificarlo.
9. No inventes tamaño muestral, resultados, efectos, DOI ni metodología que no estén en la ficha.
10. Antes de usar un estudio sobre anquiloglosia, lee el campo «Criterio diagnóstico de anquiloglosia». Las fichas no llevan interpretaciones propias: la lectura crítica la haces tú con las cuatro preguntas del enfoque crítico.
11. **Zaghi y otros expertos** (carpeta `expertos/`): son ideas expresadas en vídeos, reconstruidas por terceros. Di siempre que es opinión de experto, el vídeo de donde sale y su estado de verificación. No hables como si fueras Zaghi. Si una cifra suya choca con un estudio, da la del estudio (ver `expertos/soroush-zaghi/discrepancias.md`). La carpeta no recoge dosis de fármacos: si te piden una, dilo y remite a la ficha técnica y a un profesional. Si algo no está en la carpeta, di: «Las fuentes disponibles no permiten atribuir a Soroush Zaghi una postura fiable sobre este punto».
12. Figuras: si alguien pide ver una figura, busca la sección «Figuras» de la ficha. Si hay copia en `figuras/`, muéstrala con su crédito y su licencia (tabla de `figuras/README.md`). Si no, da el enlace directo y la descripción con palabras. No describas lo que no está en la ficha.
13. Responde en el idioma de quien pregunta. Recuerda, cuando proceda, que la biblioteca no sustituye una valoración profesional.

## Al modificar el repositorio

14. **Mantén la biblioteca privada.** Si se solicita explícitamente mejorar este repositorio, están autorizados los commits de mantenimiento en el repositorio privado existente. No cambies su visibilidad, publiques un sitio/release o distribuyas materiales a terceros sin autorización específica.
15. **Nunca entran:** datos, fotos o casos de pacientes (aunque estén anonimizados), PDF con derechos de editorial, transcripciones de vídeos, figuras sin licencia CC BY, CC BY-SA o CC0, ni contraseñas, claves o tokens.
16. Cada ficha nueva sale de fuentes/articulos/PLANTILLA.md, con su fila en `fuentes/bibliografia.csv` y su criterio diagnóstico. Si cambia una objeción, actualiza las dos caras. No cambies un nivel de certeza sin justificarlo.
17. Antes de cada commit: `python scripts/indice.py` y `python scripts/validar.py`, que debe dar «errores: 0».

---

## Enfoque crítico

---

# Enfoque crítico del agente — lectura obligatoria

**Lee este documento antes de responder preguntas científicas o trabajar con esta biblioteca.** No se trata de defender la anquiloglosia ni de desacreditar los resultados negativos: se trata de averiguar **qué pregunta respondió realmente un estudio** y qué conclusiones permite su diseño.

## Cuatro preguntas para todos los artículos

Se aplican igual a cada estudio, sea favorable o contrario. No basta con decir si se acepta la hipótesis o si hay o no hay evidencia: hay que analizar el artículo. En la literatura sobre el frenillo, los sesgos más importantes suelen ser estos:

1. **¿Con qué criterio diagnosticó la anquiloglosia?** Muchos estudios la definen por la longitud, la inserción o el aspecto del frenillo, sin medir la función (cuánto se mueve la lengua, si eleva el cuerpo, si compensa). Un estudio así responde sobre el aspecto, no sobre la restricción funcional.
2. **Si es una revisión, ¿mezcla estudios con criterios diagnósticos distintos?** Agrupar estudios que llaman «anquiloglosia» a cosas diferentes diluye o enmascara el efecto. Hay que mirar qué criterio usó cada estudio incluido.
3. **¿Tuvo en cuenta la anquiloglosia?** Muchos estudios de ortodoncia, vía aérea, sueño, deglución o habla ni la exploran. Si no la midieron, no pueden descartarla ni como causa ni como factor de confusión, y su conclusión no se puede usar para hablar del frenillo.
4. **Si estudia una cirugía, ¿qué se hizo y funcionó la liberación?** No hay una técnica uniforme: frenotomía, frenectomía y frenuloplastia no son lo mismo, y cambian la extensión del corte, los tejidos liberados y la terapia miofuncional de antes y después. Y no todas las intervenciones consiguen una liberación efectiva: hay que comprobar si se midió la movilidad después. Un mal resultado de una liberación incompleta no dice nada de una liberación completa.

Estas preguntas se hacen sobre lo que el artículo documenta. Si el dato no está, se dice que no está; no se da por hecho el sesgo.

## Principio rector

**El objetivo es relacionar investigaciones, no defender una hipótesis personal de quien ha reunido las referencias.** Las rutas de evidencia y preguntas surgidas aquí son recursos exploratorios del proyecto, salvo que un autor concreto haya formulado expresamente una hipótesis en su publicación.

No basta con responder «no hay evidencia» o «una revisión dice que no existe relación». Tampoco basta con encontrar una asociación favorable. Antes de aceptar o rechazar una afirmación, identifica la población, el diagnóstico, la variable medida, el desenlace, la precisión y los límites relevantes.

**Aplica el mismo rigor a estudios favorables y contrarios.** Una limitación metodológica no demuestra que la hipótesis alternativa sea cierta; un mecanismo anatómicamente plausible no prueba consecuencias clínicas. Los resultados negativos robustos sí deben debilitar las hipótesis que verdaderamente ponen a prueba.

Diferencia siempre:
- **Dato observado:** resultado que el estudio realmente midió.
- **Interpretación:** lectura de los autores del estudio, marcada como tal.
- **Hipótesis:** relación o mecanismo que aún no se ha contrastado directamente.

No confundas ausencia de estudios, pruebas insuficientes, resultados heterogéneos y evidencia suficientemente precisa para apoyar o descartar un efecto definido. «No significativo» no equivale por sí solo a «no hay efecto»; «significativo» no equivale a causalidad.

## Dos modos de trabajo

### Consulta normal

Prioriza los hallazgos y datos interesantes del artículo. Menciona únicamente las limitaciones decisivas para interpretar esos hallazgos, sin repetir advertencias en varios apartados. **No hagas una auditoría metodológica exhaustiva por defecto.** Si no has leído el texto completo, dilo.

### Cuando alguien plantea una objeción científica

Si se cita un artículo, metaanálisis, consenso o guía para refutar o defender una hipótesis, haz **solo las comprobaciones pertinentes**:

1. **Concreta la objeción:** ¿qué afirmación pretende refutar o sostener?
2. **Comprueba el encaje con el estudio:** ¿midió esa función o un sustituto? Ejemplos: longitud/inserción del frenillo frente a restricción funcional; elevación de la punta frente a succión posterior; anchura dentaria frente a crecimiento esquelético; cuestionario de sueño frente a polisomnografía.
3. **Revisa los límites relevantes:** diagnóstico, selección, variables de confusión, temporalidad, tamaño y precisión, denominadores de cocientes, compensaciones si realmente importan y están caracterizadas, protocolo de intervención y resultados medidos. **Distingue lo documentado de lo que solo sería posible.**
4. **Delimita la conclusión:** qué demuestra o apoya, qué no permite excluir o atribuir causalmente, qué evidencia contraria existe y qué estudio resolvería la duda.

No presentes una lista automática de fallos. No uses «quizá hubo compensaciones» para invalidar todos los resultados negativos. Una objeción puede ser correcta, parcialmente correcta o estar mal planteada.

**No cortes el razonamiento en «esto no demuestra aquello».** Tras señalar una limitación decisiva, investiga qué otros artículos pueden completar la explicación y plantea hipótesis integradoras claramente etiquetadas.

## Ejemplos

**Póvoa-Santos et al., JADA 2024:** la revisión incluyó 11 estudios observacionales con diagnósticos heterogéneos, **no todos basados en Kotlow**. La longitud/inserción no tuvo una asociación agregada concluyente con clase de Angle (heterogeneidad alta), pero dos estudios que midieron reducción de apertura encontraron diferencias en clase III. La certeza fue baja/muy baja. Esto no demuestra ni una causa general ni la ausencia universal de relación entre **restricción funcional** y desarrollo craneofacial. Ficha · Objeción.

**TRMR-TIP:** es una razón entre la apertura bucal con la punta en la papila y una apertura máxima de referencia. **El porcentaje depende de ambas mediciones**: si el denominador es anormalmente bajo, podría aparecer un valor alto con igual numerador. Es una **precaución teórica**, no la prueba de que un estudio concreto tenga ese sesgo. Tampoco alcanzar la papila con la punta equivale a evaluar el cuerpo lingual posterior ni la postura espontánea. Medición funcional.

## Conectar la evidencia: A → B → C → D

**La ausencia de un estudio directo A → D no significa que no podamos investigar la relación.** A menudo la ciencia avanza conectando resultados parciales: un trabajo estudia A → B, otro B → C y otro C → D. Si esos eslabones están bien sustentados y son compatibles en poblaciones, medidas y circunstancias, **la cadena permite construir una hipótesis razonada, biológicamente plausible y contrastable**.

El agente debe **buscar activamente esas conexiones**, no limitarse a advertir que «A no demuestra D». Para cada hipótesis interdisciplinar:
- Reconstruir la cadena con **estudios concretos por eslabón** y describir qué se observó realmente.
- Señalar qué uniones tienen evidencia directa y cuáles requieren una inferencia (incluidas posibles causas compartidas o sentidos inversos).
- Proponer el mecanismo integrado, explicar por qué resulta interesante y qué observación ayudaría a comprobarlo.
- Considerar hallazgos que contradigan un eslabón importante, en lugar de buscar únicamente publicaciones compatibles.

**La cadena no hereda automáticamente certeza causal de sus piezas:** asociaciones de poblaciones distintas no son una demostración matemática de A → D. Pero **sí pueden generar una sospecha científica fundamentada** que merece investigar. Esta distinción debe expresarse **una vez**, sin convertir cada párrafo de la ficha en una advertencia.

La biblioteca explora, entre otras, conexiones entre lengua, fascia, crecimiento mandibular y maxilar, nariz, amígdalas, vegetaciones, otitis, respiración oral, sueño, terapia miofuncional y postura. Su valor añadido es **conectar los puntos** y mostrar qué estudios sostienen cada conexión.

## Dos preguntas decisivas al valorar revisiones que dicen «no hay evidencia»

**1. ¿Qué se consideró «anquiloglosia»?** Revisar si se agrupó anatomía visible/longitud/inserción del frenillo con **restricción funcional medida**; si se exploró la elevación anterior, la succión o elevación posterior y la postura habitual, o solo una parte. Una revisión puede tener métodos rigurosos de búsqueda y, aun así, responder a una **definición de exposición demasiado heterogénea** para la hipótesis funcional planteada. Examinarlo en sus estudios originales.

**2. ¿Qué se consideró «cirugía de anquiloglosia»?** «Frenotomía», «frenectomía» y «frenuloplastia» no identifican necesariamente la misma intervención. Siempre que un resultado dependa de la técnica, registrar **criterio de indicación, localización y extensión de liberación, tejidos tratados, técnica, operador, terapia miofuncional/cotratamientos y seguimiento**, si esos datos están disponibles. Una incisión superficial y una liberación funcional con otra técnica o rehabilitación no deben darse por equivalentes sin comprobarlo. Tampoco debe darse por eficaz una técnica solo porque otra se estudió de manera insuficiente.

**Ejemplo ya verificado:** Póvoa-Santos/JADA 2024 combina definiciones anatómicas y funcionales parciales en 11 estudios; la incertidumbre de sus resultados debe interpretarse atendiendo a esa mezcla. Kotarska, a pesar de preguntar por los efectos de la cirugía en el título, **excluyó pacientes operados previamente**: sus estudios seleccionados no son comparaciones de técnicas quirúrgicas. Estos son problemas **concretos comprobados**; no convertirlos en la afirmación de que *todas* las revisiones contrarias son deficientes.

**Objetivo:** cuando una revisión concluye «evidencia insuficiente», averiguar *insuficiente para qué población, qué definición, qué operación y qué resultado*. Después, buscar estudios de los eslabones que permitan plantear hipótesis nuevas, aun cuando falte el estudio longitudinal directo.

## Cómo responder una objeción

**Qué dice el artículo → qué midió realmente y con qué certeza → límite pertinente (confirmado o solo posible) → qué sigue abierto**, citando la ficha y el DOI/PMID. Dos párrafos pueden bastar; una revisión formal requiere su propio protocolo.

Este documento complementa AGENTS.md, METODOLOGIA.md y TAREAS-AGENTES.md. No diagnosticar ni indicar tratamientos individuales. No subir datos de pacientes, PDFs protegidos ni cambiar la visibilidad del repositorio.

---

## Qué es esta biblioteca

---

# Evidencia orofacial

Biblioteca de investigación sobre lengua, frenillo lingual, maxilar, deglución, respiración, sueño y sus posibles conexiones. **El repositorio sigue privado por ahora** y está organizado para poder compartirlo cuando se decida publicarlo. Reúne estudios, revisiones, consensos y la opinión de algunos expertos. Cada estudio tiene una ficha con su enlace, sus resultados verificados y sus límites. Está pensada para que la lean médicos, otros profesionales y cualquier persona. También para que se la puedas dar a tu propia IA y preguntarle.

La ha reunido Marta Prieto, dermatóloga (@dermaprieto en Instagram): **son los artículos que ha ido revisando sobre el tema.** **No es una revisión sistemática, porque el tema es demasiado amplio.** Es conocimiento en elaboración, y **toda aportación será más que bienvenida, e incluida**: [cómo aportar](#una-investigación-abierta-a-aportaciones).

**¿Nunca has usado GitHub? Guía paso a paso para leerla con tu IA y para aportar: [recursos.inimamed.com/evidencia](https://recursos.inimamed.com/evidencia).**

## Qué es

- **190 fichas** de estudios, revisiones y documentos de sociedades científicas en fuentes/articulos/, con su DOI o PMID y el índice en bibliografia.csv. Puesta al día con una búsqueda en PubMed del 2 de noviembre de 2026: docs/BUSQUEDA-2026-11.md.
- **Objeciones frecuentes**, con resultados de estudios en distintos sentidos: objeciones/.
- **Cobertura comprobada** de la bibliografía: 222 referencias y 190 fichas registradas.
- **Un mapa interdisciplinar de evidencia** sobre vía aérea, crecimiento craneofacial, sueño, terapia miofuncional y otitis, con registro de la revisión por etapas y lista completa de textos completos/PDF por revisar y primera tanda práctica, cuya lectura de fuentes abiertas ya está documentada. Se ha completado otra tanda de originales sobre postura cervical, presión subpalatina, coordinación lingual y repetibilidad del CBCT (acta de lectura); también se ha ampliado el contraste sobre terapia miofuncional infantil y apnea, validación de herramientas diagnósticas y ensayos clínicos registrados aún sin resultados.
- **Preguntas e hipótesis exploratorias**, sin atribuirlas como tesis personales de quien recopila las referencias: hipotesis/.
- **Nueva tanda de cuatro textos originales** — Ricke 2005, Malhotra 2020, Zheng 2023 y Ye 2026 — con hallazgos sobre diagnóstico por apariencia frente a función, postura/fuerza de lengua, morfología y vía aérea.
- **Síntesis por temas** y una matriz de afirmaciones con su grado de apoyo.
- **Las ideas públicas de Soroush Zaghi** (cirujano de vía aérea, coautor de las escalas de movilidad TRMR), cada una con el vídeo del que sale: expertos/soroush-zaghi/.
- **Figuras** de artículos con licencia abierta, con su crédito: figuras/.

## Qué NO es

- **No diagnostica a nadie.** Ni esta biblioteca ni una IA que la lea pueden decir si una persona tiene anquiloglosia. Hace falta una exploración en persona.
- **No sustituye una valoración profesional.** No es una guía clínica ni una recomendación de tratamiento.
- **No es un consenso.** Recoge estudios con resultados en los dos sentidos y lo dice cuando la evidencia es débil.
- **La opinión de un experto no es un estudio.** Los vídeos de Zaghi están separados de los artículos y marcados como opinión.

## Por qué existe

Porque no hay criterios diagnósticos validados de anquiloglosia en los que todo el mundo esté de acuerdo.

- Una revisión de 71 estudios encontró que la prevalencia va del **2 % al 20 %** según la herramienta con la que se mire (Cruz 2022, JADA). Es decir, cuánta gente «tiene frenillo» depende de cómo se mire.
- El consenso de otorrinos pediátricos de Estados Unidos **no llegó a acuerdo en 28 de sus 89 afirmaciones** (Messner 2020). Sus autores lo atribuyen a lagunas de conocimiento y a falta de evidencia sobre el diagnóstico y el tratamiento. Tampoco pudieron recomendar ninguna escala diagnóstica.
- Muchos estudios diagnostican por la longitud o el aspecto del frenillo. Otros miden cuánto se mueve la lengua. No responden a la misma pregunta. Por eso **cada ficha dice qué criterio usa**.

Con ese punto de partida, nadie tiene la última palabra. Lo útil es ver **qué encuentra cada trabajo y cómo encaja con los demás**.

## Conectar los puntos

**Consultar las conexiones entre estudios y las preguntas que abren**.

**Un artículo puede observar A ↔ B, otro B ↔ C y un tercero C ↔ D, aunque todavía falte un estudio directo sobre A y D.** Este proyecto quiere reconstruir esas conexiones, valorar cada eslabón y formular **hipótesis que merezcan investigarse**, no dar una discusión por cerrada en cuanto alguien señala que falta el ensayo definitivo. Una hipótesis integrada no se confunde con un resultado demostrado, pero tampoco se descarta simplemente porque los estudios se hayan realizado por separado. Así razona el agente.

Al leer revisiones sobre anquiloglosia hay **dos preguntas fundamentales**: **qué consideraron anquiloglosia** (longitud/aspecto frente a restricción funcional) y, cuando hablan de tratamiento, **qué llamaron exactamente cirugía** (tipo y alcance de la liberación y tratamientos acompañantes). La mezcla de definiciones es una fuente importante de heterogeneidad. Por ejemplo, JADA 2024 incluyó criterios anatómicos y funcionales parciales; y Kotarska preguntó por los beneficios quirúrgicos pero seleccionó estudios que excluían a pacientes intervenidos.

## Una investigación abierta a aportaciones

**Esto no es una revisión sistemática:** el tema es demasiado amplio. Es una biblioteca en construcción: no se han leído todos los artículos publicados y puede haber estudios relevantes que falten. Agradecemos **cualquier aportación pertinente**, tanto si refuerza una hipótesis como si la contradice. **Toda aportación científica pertinente será más que bienvenida:** con el DOI, PMID o enlace se podrá comprobar e incorporar al inventario y, una vez examinada, a las fichas o síntesis correspondientes.

- **Con cuenta de GitHub:** abre una propuesta en [Issues](https://github.com/mprietob/evidencia-orofacial/issues/new/choose) con la plantilla «Proponer un artículo». Crearse la cuenta es gratis y es un momento: lo explica la guía.
- **Sin cuenta:** escribe por Instagram a **@dermaprieto** con el enlace o el DOI y una línea de por qué importa.

Cómo proponer referencias y correcciones.

## ¿Qué se consideró cirugía del frenillo?

**Comparativa de definiciones diagnósticas y técnicas documentadas**: los estudios de frenotomía, frenuloplastia y terapia miofuncional pueden estar estudiando poblaciones e intervenciones diferentes. Para interpretar las revisiones resulta útil identificar exactamente qué se midió y qué se hizo.

## Qué dicen las sociedades científicas

Resumen de los documentos de sociedades, agencias y guías localizados el 2 de noviembre de 2026. La tabla completa, con enlaces, está en conocimiento/sociedades-cientificas.md.

- **Ninguno ofrece un criterio diagnóstico validado y aceptado por todos.** Varios lo dicen de forma expresa: la sociedad pediátrica canadiense (2015), la guía de lactancia del Sistema Nacional de Salud español (2017), los otorrinos pediátricos de EE. UU. (2020), la odontopediatría de EE. UU. (2022) y los otorrinos pediátricos de Brasil (2026).
- **Los más recientes piden no diagnosticar solo por el aspecto y valorar la función.** El consenso australiano (2020) es el más concreto: exige una limitación funcional y una valoración objetiva con una herramienta (por ejemplo Martinelli o Hazelbaker). La guía de 2026 en *Pediatric Dentistry* aconseja valorar aspecto y función. Ninguno ha validado su criterio con certeza alta.
- **Casi todos hablan de lactantes y lactancia.** Coinciden en valorar primero la lactancia con profesionales expertos. Sobre la frenotomía, la evidencia que citan es baja o muy baja: menos dolor del pezón a corto plazo y resultados inconsistentes en la alimentación del bebé.
- **Sobre niños mayores y adultos dicen poco.** Los otorrinos de EE. UU. (2020) acordaron que la anquiloglosia no causa apnea y no suele afectar al habla. Los de Brasil (2026) no encuentran datos de relación con maloclusión ni apnea. Que no haya datos no demuestra que no exista relación.
- **No se ha encontrado** un documento oficial de la Asociación Española de Pediatría ni de otras sociedades españolas sobre anquiloglosia. Está marcado como pendiente de verificar.

## Cómo leer una ficha

Cada ficha de fuentes/articulos/ sigue la plantilla. Hay tres campos clave:

- **Criterio diagnóstico de anquiloglosia.** `FUNCIONAL` (mide movilidad, por ejemplo con TRMR), `LONGITUD/ASPECTO` (longitud del frenillo, inserción o forma), `MIXTO` o `NO APLICA`.
- **Resultados numéricos verificados.** Solo cifras comprobadas en el artículo o en su resumen. Lo que falta pone `PENDIENTE DE VERIFICAR`.
- **Interpretaciones editoriales**, cuando las haya, diferenciadas de los resultados originales. Las preguntas de la biblioteca no deben presentarse como opiniones personales de quien la compila.

El método completo está en docs/METODOLOGIA.md.

## Cómo preguntarle con tu propia IA

**Antes de consultar la biblioteca, lee su enfoque crítico.** Ante una objeción, no basta con repetir «no hay evidencia»: hay que comprobar si el estudio investigó realmente la hipótesis discutida y reconocer los límites relevantes sin inventarlos. Las consultas ordinarias no requieren auditorías completas.

Esta biblioteca son archivos de texto (Markdown y CSV). Cualquier IA que pueda leerlos puede responder con ellos. Hay un índice para IA en llms.txt, unas reglas de respuesta en AGENTS.md y una tabla de estudios para filtrar por criterio diagnóstico en fuentes/indice-fichas.csv.

En una IA de chat, pega en las instrucciones del proyecto las reglas de docs/INSTRUCCIONES-IA.md. Para una pregunta suelta basta con esto:

> Usa como fuente el repositorio https://github.com/mprietob/evidencia-orofacial. Lee primero AGENTS.md, docs/ENFOQUE-CRITICO.md y llms.txt y sigue sus reglas. Responde solo con lo que esté en el repositorio. Cita la ficha y el estudio (año y DOI o PMID). No te limites a decir si hay o no hay evidencia: analiza cada artículo con las cuatro preguntas del enfoque crítico (criterio diagnóstico, mezcla de criterios en las revisiones, si se tuvo en cuenta la anquiloglosia y, en cirugía, técnica y si la liberación fue efectiva). Si algo no está, dilo.

**¿Nunca has usado GitHub?** Tienes una [guía paso a paso](https://recursos.inimamed.com/evidencia) (también aquí, en GUIA.md): qué IA usar, cómo darle la biblioteca y cómo crearte una cuenta si quieres aportar.

Formas de dárselo, de más sencilla a más técnica:

0. **Un solo archivo (lo más fácil, también con cuentas gratuitas).** Descarga biblioteca-completa.md, que lo junta todo, y súbelo a NotebookLM (lo mejor para un archivo de este tamaño), ChatGPT o Gemini. Claude puede decir que no cabe; entonces usa NotebookLM o la forma 1.
1. **Subir los archivos.** En GitHub, botón verde «Code» y «Download ZIP». Descomprime y sube las carpetas que te interesen a un Proyecto de Claude, a un GPT o proyecto de ChatGPT, a NotebookLM o a Gemini. *Comprobado:* GitHub ofrece la descarga en ZIP de cualquier repositorio público. *Pendiente de probar con este repositorio:* el límite de archivos de cada aplicación. Si no caben todos, sube primero `llms.txt`, `AGENTS.md`, `objeciones/`, `conocimiento/` y las fichas del tema que te interese.
2. **Pegar el enlace en un chat con búsqueda web.** Pide que lea `llms.txt` y las fichas. *Comprobado:* los archivos de un repositorio público se pueden leer como texto en `raw.githubusercontent.com` sin cuenta. *Pendiente de probar:* si cada IA consigue abrir GitHub desde su navegación, que cambia según la aplicación y el plan.
3. **Conectarlo como servidor MCP con GitMCP** (gratuito, de terceros). La dirección sería `https://gitmcp.io/mprietob/evidencia-orofacial`. En Claude se añade como conector personalizado. *Comprobado* el 02/11/2026 con otro repositorio público: GitMCP responde y ofrece herramientas para leer la documentación, buscar en ella y buscar en los archivos. *Pendiente de probar:* con este repositorio y dentro de cada aplicación.
4. **Clonarlo y preguntar desde una IA de terminal** (Claude Code, Codex u otras): `git clone https://github.com/mprietob/evidencia-orofacial`. Hay un archivo de entrada para cada herramienta: `AGENTS.md` (Codex y otras), `CLAUDE.md` (Claude Code), `GEMINI.md` (Gemini CLI) y `.github/copilot-instructions.md` (GitHub Copilot). Todos llevan a las mismas reglas. Para mantener la biblioteca, los pasos están en docs/TAREAS-AGENTES.md. *Comprobado:* Claude Code lee `CLAUDE.md`. *Pendiente de probar con este repositorio:* que cada una de las otras herramientas cargue su archivo.

Aunque la IA cite bien, revisa la ficha original y el artículo. Las IA se equivocan.

## Licencia

Ver LICENCIA.md. Los textos propios tienen una licencia propuesta. El material de terceros (figuras, títulos de artículos, citas cortas, vídeos enlazados) conserva la licencia y los derechos de sus autores.

## Contribuir

Si encuentras un error, un estudio que falta o una cifra mal copiada, abre una «issue» en GitHub con la plantilla «Proponer un artículo», o escribe por Instagram a @dermaprieto. Cómo se añade una ficha: CONTRIBUTING.md. Preguntas que siguen abiertas: docs/PREGUNTAS-ABIERTAS.md.

## Privacidad

Aquí no hay datos de pacientes, fotos de pacientes, PDF con derechos ni transcripciones completas de vídeos de terceros.

---

# Síntesis por tema

---

<!-- archivo: conocimiento/afirmaciones.md -->
# Matriz de afirmaciones

| ID | Afirmación definida | Estado editorial | Evidencia clave | Reserva |
|---|---|---|---|---|
| L-001 | La lengua humana funciona biomecánicamente como un hidrostato muscular. | VERIFICADO | Kier 1985; Gilbert 2007 | La deformabilidad no implica movilidad ilimitada. |
| L-002 | El frenillo lingual se forma en parte por una fascia continua con inserción en la mandíbula interna. | VERIFICADO | Mills 2019; Mills 2020 | Anatomía cadavérica, heterogeneidad individual. |
| L-003 | Hay compartimentos intraorales con gradientes de presión distintos durante deglución y sellado palatino; su relación con crecimiento dental/esquelético exige otra evidencia. | VERIFICADO para presiones medidas, INTERPRETACION para crecimiento | Engelke 2011 (n=20 adultos sanos); Proffit 1978 | SPS −81,86 mbar e IOS −48,79 mbar bajo deglución+sellado instruido. No se midió crecimiento, fuerzas crónicas sobre hueso ni anquiloglosia. |
| L-004 | Menor movilidad lingual se asocia en algunas muestras a diferencias maxilares. | INTERPRETACION | Yoon 2017; Kotarska 2024 | Estudio transversal; confusión y causalidad no resueltas. |
| L-005 | La anquiloglosia causa de modo generalizable maloclusión o hipoplasia maxilar. | SIN_DATOS para establecer causalidad | Póvoa-Santos 2024; Kotarska 2024 | JADA: 11 estudios observacionales con medidas anatómicas y funcionales parciales; algunos resultados asociados, heterogeneidad y confusión no controlada. Certeza baja/muy baja. |
| L-006 | La fascia del suelo de boca ejerce en ciertos pacientes una tracción posterior capaz de mantener una posición mandibular retraída. | HIPOTESIS | Mills 2019 respalda anatomía, no este efecto | Faltan mediciones directas de fuerzas y cambio sagital objetivo. |
| L-007 | Liberar el frenillo causa adelantamiento óseo mandibular inmediato. | SIN_DATOS; no afirmarlo | — | En minutos/días, diferenciar postura mandibular vs hueso. |
| L-008 | El TRMR expresa la apertura con la lengua elevada respecto a la apertura máxima de referencia; escala TIP: grado 1 >80 %, 2 50-80 %, 3 <50 %, 4 <25 %. | VERIFICADO como definición publicada; validez diagnóstica con límites | Yoon 2017 (Sleep Breath, 1.052 sujetos); Zaghi 2021 | Depende del denominador: una apertura máxima limitada puede cambiar el cociente. Precaución teórica, no sesgo demostrado en una muestra. |
| L-009 | En niños, la anquiloglosia se asocia a trastorno respiratorio del sueño, y pesa más la movilidad lingual que la longitud del frenillo. | INTERPRETACION | Koento 2026; Cohen-Levy 2020; Guilleminault 2016 | Estudios transversales, cuestionarios, muestras pequeñas. Asociación, no causa. |
| L-010 | En adultos, frenillo más corto y menor movilidad (TRMR) van con una mandíbula más pequeña y retrasada. | INTERPRETACION | He 2026 | Correlaciones débiles (r 0,14-0,22), erratas, transversal. Los autores plantean también la dirección inversa. Ver H-001. |
| L-011 | Los trastornos respiratorios del sueño en niños se asocian a síntomas de TDAH, y operar amígdalas y vegetaciones mejora la conducta referida por los padres. | VERIFICADO | Sedky 2014; Bonuck 2012; Leow 2026; Marcus 2013; Lee 2026 | El ensayo CHAT no mejoró la atención medida con test. Las medidas objetivas de TDAH no salen significativas. |
| L-012 | La anquiloglosia se relaciona directamente con el TDAH. | SIN_DATOS; no afirmarlo | Búsqueda propia en PubMed del 15/10/2026: 0 resultados | La cadena posible (frenillo, vía aérea, sueño, conducta) solo está apoyada eslabón a eslabón. |
| L-013 | Añadir frenuloplastia a la terapia miofuncional mejora la movilidad y las funciones orofaciales más que la terapia sola, con selección por TRMR. | INTERPRETACION | Lichnowska 2024 (ensayo, 155 sujetos); Zaghi 2019 (serie, 348) | Asignación por orden de entrada, evaluación visual, coautoría de Zaghi. Solo pacientes con deformidad maxilofacial. |
| L-014 | De media, las extracciones de premolares no cambian el volumen ni el área mínima de la vía aérea medidos en CBCT. | VERIFICADO como resultado de metaanálisis | Papageorgiou 2025; Orabi 2021; Guo 2023 | Estudios retrospectivos con alto riesgo de sesgo y sin control de la postura. Ver O-003. |
| L-015 | La flexión/extensión de cabeza modifica la MCA en CBCT en adultos; asociación modelada NBC3 +5°≈+25 % y +10°≈+88 %. | VERIFICADO como cambio de imagen | Coppelson 2023, texto completo abierto y tabla 3 | 90 adultos, dos CBCT; flexión −41,4 mm² y extensión +147,4 mm²; condiciones sentado/de pie, mentonera y repetir deglución no significativas. El cambio de MCA no demuestra compensación cervical causal ni cambio de AHI. |
| L-016 | Que la anquiloglosia afecte al habla. | SIN_DATOS; evidencia enfrentada | Melong 2024; Kummer 2025; Cordray 2023 | Ver O-004. Ausencia de pruebas no es prueba de ausencia. |
| L-017 | En la clase II, lo más frecuente es la mandíbula retrasada y no el maxilar adelantado. | INTERPRETACION; cifras `PENDIENTE DE VERIFICAR` | McNamara 1981 | Las cifras que circulan (13 % maxilar adelantado) no se han comprobado en el original. |
| L-018 | La prevalencia de anquiloglosia depende sobre todo de la herramienta diagnóstica: del 2 % al 20 % (global 5 %). | VERIFICADO | Cruz 2022; Maya-Enero 2021 (46,3 % con búsqueda activa) | Por eso cada ficha declara su criterio. |
| L-019 | Con TRMR, la restricción posterior (LPS) es más frecuente que la anterior y se asocia a menos fuerza lingual. | INTERPRETACION | Hoang 2024 (512 niños) | Un estudio, niños de 6-8 años, edad en la que el TRMR es menos fiable. |
| L-020 | La frenotomía neonatal mejora la lactancia. | SIN_DATOS sólidos; evidencia contradictoria | Dinh 2025 (ensayo negativo inmediato); Albertsen 2024 (dolor -1,2 sobre 10, certeza baja); Feldens 2024 y 2025 (sin asociación con lactancia) | Cohortes sin control describen mejoría (Slagter 2021, Jones 2024B). |
| L-021 | La expansión rápida del maxilar mejora la apnea infantil a corto plazo. | VERIFICADO como resultado de metaanálisis | Camacho 2017 (17 estudios, IAH -70 %); Villa 2015; Yoon 2022 | Curación completa minoritaria; falta separar el crecimiento. |
| L-022 | Añadir frenectomía a los ejercicios mejora la apnea del adulto con anquiloglosia. | SIN_DATOS; un ensayo pequeño negativo | Preedeewong 2024 (15 adultos, TRMR) | Falta potencia. Mejoró la movilidad, no el IAH. |
| L-023 | Amígdalas grandes, lengua restringida y nariz obstruida se suman en el bruxismo del sueño infantil. | INTERPRETACION | Oh 2021 (Sleep Med, 96 niños) | Transversal; bruxismo por informe de padres. |

---

<!-- archivo: conocimiento/criterios-diagnosticos-anki-2024-2026.md -->
# ¿Qué significa que una herramienta de anquiloglosia esté «validada»?

**Síntesis crítica de publicaciones 2024–2026.** No es una revisión sistemática propia ni sustituye a las fichas; conecta resultados de revisiones con preguntas diferentes. Leer enfoque científico.

## La palabra «validez» es insuficiente sin especificar qué se ha validado

Un instrumento puede tener:
- **Fiabilidad interobservador:** dos clínicos coinciden al puntuar.
- **Consistencia interna:** sus ítems se parecen entre sí estadísticamente.
- **Validez convergente:** su puntuación se correlaciona con otra escala.
- **Discriminación:** separa grupos definidos de cierta manera (AUC ROC).
- **Validez clínica/predictiva:** identifica a las personas con disfunción relevante o predice quién se beneficia de una intervención.

**Ninguno de los primeros cuatro elementos garantiza automáticamente el quinto.** Si se compara una escala con otra escala que tampoco es patrón de referencia, la correlación puede ser alta sin establecer la realidad de la restricción funcional que preocupa al paciente.

## Un ejemplo primario especialmente ilustrativo: Ricke 2005

En **Ricke et al. 2005**, la selección inicial de **148/3.490 recién nacidos** como «anquiloglosia» dependió **solo de la apariencia** valorada por enfermeras; **después** se aplicó ATLFF a los casos. En los **49 casos** del análisis, la propia escala **dejó 31 (63 %) fuera de las categorías predefinidas** y el acuerdo interobservador para función alterada fue **κ=0,49**, pese a entrenamiento de los investigadores.

**La distinción que importa al revisar literatura:** un trabajo puede **usar una herramienta funcional durante el estudio sin haber seleccionado originalmente a los participantes por disfunción funcional**. Esta diferencia debe quedar clara en las tablas de revisiones y metaanálisis. El mismo estudio encontró riesgo relativo **3,11** de alimentación solo con biberón en semana 1 frente a controles y **1,00** al mes: resultados temporales distintos dentro de la misma cohorte.

## Qué dice exactamente cada fuente

| Fuente | Población y pregunta | Resultado | Límite que importa |
|---|---|---|---|
| AAP 2024 | Lactantes con dificultades de lactancia; criterios clínicos y decisión de frenotomía | Múltiples escalas estructurales/funcionales, pero según su revisión **ninguna validada plenamente** como herramienta que resuelva por sí sola la indicación; valorar una toma y el problema clínico. | Se enfoca en lactancia en bebés, **no** en restricción lingual funcional y crecimiento craneofacial a los 10–18 años. |
| Necus 2025 | Revisión sistemática de **117 estudios**, 9 instrumentos, 0–12 meses | La escala **LFPI** tuvo la mayor cantidad de propiedades de fiabilidad/validez **notificadas**. Solo pocos estudios incluían alimentación como criterio diagnóstico. | «Más datos disponibles» **no significa patrón oro** ni mejor predicción de beneficio quirúrgico. Existe una fe de erratas 2025 cuyo contenido exacto falta comprobar. |
| Kumar 2025 | Revisión sistemática de **17 estudios** de medición cuantitativa (11 transversales, 4 cohortes, 2 ECA) | No puede recomendar un instrumento cuantitativo único por **heterogeneidad y certeza baja**; se mezclan medidas anatómicas y de función. | La conclusión **no invalida automáticamente** cada escala; solo niega base suficiente para recomendarla universalmente. |
| Dhar et al. 2026, parte 1 | Revisión sistemática/metaanálisis de **20 estudios** (14 analizados), lactancia | Para **BTAT/TABBY**, AUC ROC **0,95**, α **0,708** y correlación **r=0,89** con Hazelbaker; certeza general **muy baja**. Asociación con problemas de alimentación: OR **5,57**, IC95 % **0,44–70,02**, p=0,18, I²=96 %. | El resumen no revela qué **patrón de referencia independiente** se usó para AUC. Un IC que cruza 1 y se extiende hasta 70 **no confirma una asociación**, pero tampoco prueba ausencia de relación. |
| ICAP 2024 | Posicionamiento de consorcio profesional | Define anquiloglosia en términos **funcionales** más allá de apariencia anatómica y aconseja evaluación multidisciplinar. | Es una posición profesional, **no** un ensayo que valide la definición y sus consecuencias clínicas. |

## Por qué las conclusiones no son idénticas

- **Preguntas distintas:** AAP juzga seguridad/indicación en lactancia; Necus compara datos psicométricos publicados en lactantes; Kumar evalúa instrumentos cuantitativos; Dhar intenta valorar tanto diagnóstico como asociación con dificultades de alimentación.
- **Instrumentos y ventanas temporales:** las revisiones tienen distintas fechas de búsqueda y conjuntos de estudios, **con solapamiento probable** que debe comprobarse, no sumarse como 117+17+20 estudios independientes.
- **Constructos distintos:** una escala de apariencia, el TRMR-TIP, la capacidad de succión posterior, la observación de toma y la deglución infantil no son equivalentes.
- **La normalización del TRMR puede ocultar límites:** Mpal/Mmax depende de apertura absoluta usada como denominador. Una apertura máxima restringida **podría** aumentar el cociente con igual numerador; hipótesis matemática legítima, pero **no prueba** que sucediera en el estudio concreto citado.

## Cómo responder una objeción

**«Kotlow no tiene validez funcional y por tanto ningún estudio que lo use sirve»**: demasiado categórico. Kotlow puede describir una dimensión anatómica; **no** valida por sí solo movilidad ni desenlaces a largo plazo. Un estudio que usa Kotlow puede ser pertinente para una pregunta **anatómica**, insuficiente para una **funcional**.

**«TRMR está validado, por tanto demuestra patología del frenillo»**: tampoco. Hay que definir la función que se pretende medir, el valor absoluto de apertura, posibles compensaciones y la capacidad de la medida de predecir **resultado clínico real**. No es tarea de un agente reconstruir cada paciente del artículo, sino detectar esa diferencia cuando alguien use la escala como objeción definitiva.

**«La AAP dice que no hay herramientas validadas; las revisiones posteriores dicen que sí»**: algunas revisiones posteriores reportan **mejor fiabilidad, convergencia o discriminación** para escalas concretas con certeza limitada. La divergencia puede derivar de **conceptos distintos de validez**, ventanas temporales y objetivos clínicos; no declarar una contradicción insoluble ni afirmar patrón oro inexistente.

## Qué aún necesitamos consultar

1. **Texto completo y anexos de Necus 2025, incluido corrigendum** (DOI `10.1016/j.ijporl.2025.112527`) para identificar exactamente qué se corrigió.
2. **Análisis de validez clínica del LFPI, BTAT/TABBY y TRMR** frente a desenlaces independientes y resultados después de tratamiento; no solo correlaciones entre escalas.
3. En Dhar 2026, el **comparador independiente usado para AUC** de 0,95, tamaños de muestra/intervalos de precisión y riesgo de sesgo de los estudios de herramientas.
4. Diferenciar escalas para **lactantes**, niños escolares y adultos; evitar extrapolación de diagnóstico neonatal a desarrollo óseo y apnea.

Fuentes enlazadas en las fichas; esta síntesis no autoriza intervención clínica sobre personas individuales.

---

<!-- archivo: conocimiento/definiciones-intervencion-frenillo.md -->
# Qué se llamó anquiloglosia y qué se llamó cirugía

En la literatura, el nombre «frenillo» puede referirse a **variables anatómicas o funcionales diferentes**, y «operar el frenillo» a procedimientos y combinaciones terapéuticas distintas. Esta matriz se construye con los datos **ya consignados en las fichas**; lo que falta describir sigue siendo una tarea de lectura.

| Publicación | Definición utilizada en la ficha | Tratamiento/comparador descrito | Resultado recogido |
|---|---|---|---|
| Ricke 2005 | Selección **visual** del frenillo en neonatos; ATLFF **mixto aplicado después** (κ=0,49; 31/49 sin categoría) | Cuatro frenotomías, cuyos datos posteriores **se excluyeron** de la comparación de alimentación | Riesgo relativo de solo biberón 3,11 en semana 1; 1,00 al mes |
| Messner y Lalakea 2002 | Niños de 1 a 12 años; criterio inicial exacto pendiente en el abstract | Frenuloplastia, con comparación pre/post pero sin control | Cambios de movilidad medidos en mm y articulación evaluada en parte de la muestra |
| O’Callahan 2013 | Lactantes, Coryllos I–IV (**anatómica**) | Frenotomía en consulta; la ficha no precisa planos ni extensión de liberación | Encuesta posterior de lactancia y dolor, sin grupo control |
| Dinh 2025 | Recién nacidos, Hazelbaker (**aspecto + función**) | Frenotomía frente a procedimiento simulado (55 y 57 díadas) | Sin diferencia significativa inmediata en LATCH ni dolor |
| Zaghi 2019 | Niños y adultos, clasificación funcional TRMR | Frenuloplastia con tijera y sutura, más terapia miofuncional previa | Encuestas de 348 respuestas con mejorías notificadas; sin grupo control |
| Lichnowska 2024 | Cohorte con deformidad maxilofacial, TRMR | Frenuloplastia + terapia miofuncional frente a terapia sola | Indicadores funcionales favorables; diferencia de edad entre grupos y asignación por día/orden |
| Kotarska, online 2024 / volumen 2025 | Revisión con criterios anatómicos y funcionales | **No comparó cirugías**; excluyó pacientes previamente intervenidos | Asociaciones con oclusión y morfología |
| Póvoa-Santos, JADA 2024 | Once estudios con diagnósticos heterogéneos | Revisión de anquiloglosia y maloclusión, no de técnica quirúrgica | Resultados sobre anatomía, apertura y oclusión |

## Qué registrar cuando revisemos el artículo íntegro

Para poder comparar tratamientos, extraer **solo si consta en el original**: criterio diagnóstico, edad, procedimiento declarado (frenotomía, frenectomía, frenuloplastia), técnica/instrumental, **extensión real de la liberación**, operador, terapia miofuncional y otras cointervenciones, resultado funcional pre/post y tiempo de seguimiento.

**La etiqueta quirúrgica por sí sola no garantiza procedimientos equivalentes.** Tampoco un diagnóstico anatómico por longitud/inserción es idéntico a uno de movilidad funcional. Esta clasificación permite identificar estudios comparables sin dar preferencia automática a una técnica.

## Uso ante objeciones

Antes de extrapolar el resultado de una revisión, preguntar **qué población estudió, cómo definió la anquiloglosia y qué tratamiento se realizó de hecho**. Después recuperar cifras positivas o negativas de los originales. Así se puede entender mejor de dónde procede la incertidumbre y qué nuevas comparaciones serían interesantes.

**Estado de este documento:** correspondencia de definiciones tomada de fichas existentes, no nueva revisión sistemática de ensayos. Ver rutas de evidencia.

---

<!-- archivo: conocimiento/evaluacion-funcional-lengua.md -->
# Cómo se mide la movilidad de la lengua

**Estado:** el método TRMR está VERIFICADO como descripción publicada. Las «cinco dimensiones» son opinión de experto en vídeo.

## Lo publicado

- **TRMR-TIP:** razón entre la apertura con la punta en la papila incisiva y la apertura máxima de referencia. Propuesto y estudiado en 1.052 sujetos por Yoon 2017 (ficha). **No es independiente de la apertura:** depende matemáticamente del numerador y del denominador.
- **TRMR-LPS:** lo mismo con la lengua succionada al paladar. Zaghi 2021 (ficha), 611 sujetos: refleja mucho mejor que TIP la dificultad para subir el cuerpo de la lengua.
- **Escala:** TIP grado 1 >80 %, 2 de 50 a 80 %, 3 <50 %, 4 <25 %. LPS grado 1 >60 %, 2 de 30 a 60 %, 3 <30 %, 4 <5 % o no puede.
- **Límites y precauciones:** los autores advierten límites de aplicación en ciertas edades y con apertura restringida; el cociente bajo no identifica por sí solo la causa. **Precaución teórica, no sesgo demostrado:** si la apertura máxima de referencia está reducida, una misma apertura con la lengua elevada puede dar un cociente relativamente alto. No afirmar que ocurrió en una cohorte sin comprobar sus aperturas absolutas. Alcanzar la papila no mide toda la elevación posterior ni la postura de reposo.
- **Lengua libre de Kotlow:** mide otra cosa (longitud), independiente del TRMR (Yoon 2017). Guilleminault 2016 recoge que Kotlow considera normal más de 16 mm.
- **Uso en estudios independientes:** Hoang 2024 (Vietnam, 512 niños: la restricción posterior es más frecuente que la anterior y se asocia a menos fuerza), Preedeewong 2024 (inclusión por TRMR en adultos con apnea), He 2026 (TRMR en adultos con apnea).

## Lo que dice Zaghi en sus clases (OPINIÓN DE EXPERTO, vídeo)

Resumen propio de una clase de Zaghi de unos 55 minutos. La transcripción no está en este repositorio. URL y minutos: `PENDIENTE DE VERIFICAR`. Las mismas ideas aparecen, con su vídeo y enlace, en el vídeo «5 dimensions of tongue-tie assessment» (https://www.youtube.com/watch?v=8dOq11N-qK8) y en [la síntesis de Zaghi sobre anquiloglosia.]

- El frenillo se valora en cinco dimensiones: sacar la lengua, elevar la punta (TIP), succión (LPS), compensaciones y tensión a la palpación. La mayoría de clínicos solo mira la primera.
- Sacar bien la lengua no descarta una restricción.
- Una medida normal no descarta frenillo, porque se puede compensar; una baja sí lo orienta. Se comprueba sujetando el suelo de la boca: si baja la movilidad, había compensación.
- Signos de compensación: el suelo de la boca sube, cuello y mandíbula se tensan, la mandíbula se adelanta, la cara hace fuerza.
- No todo es frenillo: también cuentan el tamaño de la lengua y de la boca, el tono, la fascia, la cabeza adelantada, la respiración oral y los hábitos.

Lo de las compensaciones aparece también, como limitación, en Zaghi 2021. La maniobra de sujetar el suelo de la boca como criterio diagnóstico no está validada en un estudio publicado: `SIN_DATOS`.

## Quién más mide y cómo

La mayoría de la literatura de lactantes usa escalas de aspecto o mixtas: Coryllos (inserción), Kotlow (longitud), Hazelbaker (aspecto y función), Bristol, Martinelli y Marchesan. Cruz 2022 (ficha) muestra que la prevalencia va del 2 % al 20 % según la herramienta. Por eso cada ficha de este repositorio dice qué criterio usa.

---

<!-- archivo: conocimiento/fascia-suelo-boca.md -->
# Anatomía fascial del suelo de la boca y frenillo

**Estado:** VERIFICADO como descripción anatómica cadavérica; alcance funcional y causal clínico sin demostrar.

Mills et al. (2019) describen, mediante microdisección de **nueve cadáveres adultos**, que el frenillo visible se forma dinámicamente por el pliegue de la fascia del suelo de la boca. La fascia se inserta en la superficie interna de la mandíbula y se continúa centralmente con el tejido conjuntivo ventral lingual. En algunos individuos, el geniogloso se moviliza hacia el pliegue. Esta arquitectura también se investigó en cuatro cadáveres neonatales y en un estudio histológico de trece adultos.

**Fuentes:**
- Mills et al. (2019), *What is a tongue tie? Defining the anatomy of the in-situ lingual frenulum*. DOI: 10.1002/ca.23343.
- Mills et al. (2019), *Defining the anatomy of the neonatal lingual frenulum*. DOI: 10.1002/ca.23410.
- Mills et al. (2020), *Understanding the Lingual Frenulum: Histological Structure, Tissue Composition, and Implications for Tongue Tie Surgery*. DOI: 10.1155/2020/1820978.

## Hipótesis derivada que NO debe tratarse como hecho
Que una configuración fascial restrictiva cambie las fuerzas y el equilibrio mandibular puede plantearse como mecanismo a comprobar. **La conexión anatómica y la tensión observada al mover la lengua NO prueban por sí mismas una fuerza posterior neta suficiente para retraer la mandíbula**, ni que una frenotomía produzca adelantamiento esquelético.

Ver hipótesis mandibular.

---

<!-- archivo: conocimiento/hidrostato-muscular.md -->
# La lengua como hidrostato muscular

**Estado:** VERIFICADO para el principio general; inferencias clínicas separadas.

Los hidrostatos musculares se deforman manteniendo volumen aproximadamente constante. La contracción de fibras con orientaciones complementarias permite acortamiento, elongación, curvatura y remodelado tridimensional de la lengua humana.

**Fuentes primarias:** Kier & Smith (1985), DOI: 10.1111/j.1096-3642.1985.tb01178.x; Gilbert et al. (2007), DOI: 10.1242/jeb.007096.

## Qué permite afirmar
- La lengua puede ajustar su forma sin reducir su volumen global.
- No se deduce que la anchura del paladar deba ser idéntica a la anchura espontánea del cuerpo lingual para poder elevarse.

## Qué NO prueba
- Que la elevación sea siempre posible en cualquier paladar estrecho.
- Que la limitación de elevación sea necesariamente consecuencia de un frenillo.
- Que un hidrostato no esté condicionado por inserciones, musculatura extrínseca, espacio, dolor, control neuromotor y fuerzas de contacto.

**Pregunta experimental:** medir elevación TIP/LPS, posturas de reposo y geometría palatina en sujetos con y sin restricción, separando antes/después de ortodoncia y/o intervención lingual.

---

<!-- archivo: conocimiento/mapa-craneo-orofacial-via-aerea-sueno-postura.md -->
# Mapa interdisciplinar de la evidencia: función orofacial, vía aérea, crecimiento, sueño y postura

**Primera actualización dirigida:** 03/11/2026. **Estado:** síntesis exploratoria crítica, **NO revisión sistemática completa ni metaanálisis propio**. Ver registro de búsqueda y enfoque científico.

## Por qué estudiarlo conjuntamente

El interés es investigar cómo interactúan estructuras y funciones, no atribuir todos los problemas al frenillo. La interpretación de una cadena como «obstrucción nasal → respiración oral → postura lingual → crecimiento facial → apnea → postura cervical» requiere distinguir los **eslabones realmente medidos** de los **mecanismos propuestos**; las asociaciones separadas no prueban una secuencia causal completa.

## Resultados de la primera ampliación

| Relación / pregunta | Datos que tenemos | Límite esencial | Estudios |
|---|---|---|---|
| **Rinitis alérgica ↔ respiración y sueño infantil** | Metaanálisis de 17 estudios/32.907 niños: rinitis asociada con ronquido (OR 2,24), SDB (OR 1,49) y apnea (OR 1,23). En 643 niños derivados a PSG, coexistencia de rinitis+apnea se relaciona con más eventos y microdespertares respiratorios. | No prueba dirección causal; metaanálisis publicado en 2026 con búsqueda hasta 2022; en el estudio PSG el resultado ajustado de activaciones de movimientos periódicos tiene **dirección inversa**. | Li 2026; Kang 2026 |
| **Respiración bucal ↔ apnea infantil** | Revisión sistemática de 13 estudios observa asociación y posible utilidad de la respiración bucal como signo de evaluación de SDB. | Métodos diagnósticos variables, no efecto causal demostrado ni reemplazo de PSG. | Vaishnavi 2026 |
| **Respiración bucal ↔ morfología craneofacial** | Revisión narrativa estructurada con 16 trabajos describe asociaciones con estrechez maxilar, paladar alto y patrón vertical. | Trabajos observacionales y revisiones previas mezclados: posible doble recuento; no crecimiento longitudinal causal ni efecto demostrado de tratamiento. | Sotero Grande 2026 |
| **Hipertrofia de adenoides/amígdalas ↔ morfología dentofacial** | Metaanálisis de 36 estudios transversales: SN-MP +2,20°, SNB −0,78°, SNA −0,30° en grupos con hipertrofia. | Diferencias medias a menudo pequeñas, confusores y temporalidad sin resolver; **ANB sin diferencia concluyente**. Certeza baja/muy baja. | Zhao 2025 |
| **Adenoidectomía/adenoamigdalectomía ↔ crecimiento después de la intervención** | Revisión de 10 estudios prospectivos/longitudinales encuentra algunas adaptaciones dentoalveolares favorables tras cirugía. | Falta atribución causal exclusiva frente a crecimiento y cointervenciones; normalización esquelética no predecible. | Singla 2026 |
| **Terapia miofuncional aislada ↔ apnea infantil objetiva** | Revisión de ensayos: IAH, 4 ECA con n=174; DM −1,68/h (IC95% −3,61 a +0,24; p=0,07): **no hay diferencia concluyente**. | Riesgo de sesgo serio; muchos niños con apnea residual tras cirugía; no generalizar a todos los fenotipos. **El resultado negativo sí importa**. | Cnockaert 2026 |
| **Terapia miofuncional ↔ apnea en adultos** | Umbrella review de 9 revisiones/21 estudios primarios sugiere mejoría de algunos desenlaces adultos, con IAH −9,54/h agrupado. | Calidad metodológica frecuentemente críticamente baja y alto sesgo primario. **No extrapolar los efectos de adultos a niños**. | Pisoni 2026 |
| **Adenoides / trompa de Eustaquio ↔ otitis media con efusión** | Umbrella review de intervenciones: eficacia dependiente de edad de tubos y adenoidectomía en OME; otras intervenciones con limitaciones. | No estudia frenillo, desarrollo maxilar ni postura. No conectar causalmente sin estudios que hayan medido ambas cosas. | Chandrasekharan 2026 |

## Nueva evidencia original sobre fuerza, postura lingual y geometría faríngea (04/11/2026)

- **Adolescentes y patrón sagital:** Ye et al. 2026 midieron **en las mismas 182 personas** fuerza lingual MTP, posición cefalométrica de punta/dorso y ANB. En clase III MTP mediana **1,65 kg** frente a **2,20–2,21 kg** en clases I/II; el análisis estadístico indicó asociación parcial MTP–TTI–ANB (**32,4 %** en ruta mediada). Da una nueva conexión cuantitativa entre función y morfología. No clasificaron frenillo; excluyeron predominantemente respiradores bucales y deglución atípica.
- **Adultos y segmentos faríngeos:** Zheng et al. 2023 compararon **98 adultos con lengua alta y 96 con lengua baja en CBCT**. **No hubo diferencia global significativa** de volumen/áreas de vía aérea; el subgrupo de lengua extremadamente baja tenía *mayores* valores en algunos segmentos retropalatinos y retroglosos. Este hallazgo aconseja investigar **subtipos, espacio intraoral y segmento** antes de generalizar sobre lengua baja y obstrucción.
- **OSA no se explica por anatomía aislada:** Malhotra et al. 2020 integran geometría faríngea, dilatadores musculares, control ventilatorio (*loop gain*) y umbral de despertar. Este marco permite formular preguntas sobre por qué resultados de imagen y sueño no siempre coinciden.

Mapa de conexiones actualizado.

## Actualización de terapia miofuncional: por qué las revisiones discrepan

**No basta con afirmar que un metaanálisis de 2020 es favorable y otro de 2026 es negativo:** Bandyopadhyay 2020 agrupa sobre todo cambios antes/después, con ejercicios activos y dispositivos pasivos (IAH −1,54/h, IC95 % −2,24 a −0,85; I² 72 %); Cnockaert 2026 estima diferencias frente a controles aleatorizados (IAH −1,68/h, IC95 % −3,61 a +0,24; no concluyente). Avivar-Pardo 2026 incluye un único ECA pequeño más observacionales, con certeza baja; Carey 2026 estudia **deglución**, no apnea, en 17 estudios con predominio de calidad pobre y cotratamientos. Análisis comparativo detallado.

**Próximo ensayo relevante, todavía sin resultados:** NCT07249944 medirá por separado oAHI en PSG, longitud lingual, Mpal/Mmax, fuerza, respiración y rasgos posturales. No es estudio de frenotomía y no se sabe el resultado.

## Tercera tanda: biomecánica medida directamente, no inferida de apariencia

**Coppelson 2023** está **abierto** y su texto completo confirma un efecto de la postura cervical sobre la **medición de MCA en CBCT**: flexión −41,4 mm², extensión +147,4 mm²; tres variantes no significativas. **Engelke 2011** midió directamente **presiones diferentes subpalatinas e interoclusales** durante deglución/sellado en 20 adultos con respiración nasal y oclusión normales; no midió frenillo ni crecimiento. **Knösel 2012** registró contacto lengua–paladar durante 542 degluciones de 29 niños con postura abierta: **el examen clínico no coincidía siempre con el patrón observado**, y **excluyó niños que no podían alcanzar la papila**. Síntesis con límites y preguntas pendientes.

Una **cuarta** fuente metodológica, Sun 2024, encontró grandes diferencias de volumen orofaríngeo entre CT consecutivas del mismo paciente, incluso con alta fiabilidad al volver a leer la imagen; no confundas variabilidad entre adquisiciones con error de observador, ni volumen con MCA. Síntesis ampliada.

Estos tres trabajos ofrecen tres mediciones objetivas pero **no prueban una cadena causal frenillo → pérdida de presión → anomalía maxilar → apnea → compensación cervical**.

## Piezas existentes que deben integrarse (sin confundir mecanismos y efectos)

- **Anatomía de la fascia lingual:** disección y análisis histológico de Mills describen la participación de la fascia del suelo de la boca en el frenillo; **no** documentan un efecto causal del frenillo sobre la posición sagital permanente o el crecimiento óseo mandibular. Ver fascia.
- **Función frente a longitud del frenillo:** no son el mismo constructo; TRMR-TIP depende del denominador de apertura y no equivale a succión posterior o postura espontánea. Ver evaluación funcional.
- **Anquiloglosia y oclusión:** JADA 2024 incluyó 11 estudios observacionales con diagnóstico heterogéneo, asociaciones específicas y GRADE bajo/muy bajo. Ver ficha JADA y objeción.
- **Cefalometría/hioides/postura de cabeza:** las medidas dependen de la posición y del protocolo de imagen. Un volumen faríngeo en CBCT o una posición craneocervical en un corte estático no prueban una adaptación funcional crónica. Ver matriz de afirmaciones, especialmente L-015.
- **Sueño y conducta:** el sueño objetivado, la conducta referida por padres y los test neuropsicológicos son desenlaces diferentes; no deducir TDAH a partir de un hallazgo anatómico.

## Preguntas que siguen realmente abiertas

1. ¿Hay cohortes pediátricas que midan **por separado** obstrucción nasal/adenoamigdalar, posición habitual de la lengua, movilidad anterior y posterior, respiración oral nocturna y crecimiento basal óseo?
2. ¿La modificación del flujo nasal durante el crecimiento cambia la postura lingual en reposo de modo objetivable? ¿Qué estudio distingue causa, consecuencia y factor común?
3. ¿Qué papel tienen el hioides, musculatura suprahioidea, fascia de suelo de boca y postura craneocervical en adaptaciones **medidas** y no solo propuestas?
4. ¿Existen ensayos o cohortes que permitan diferenciar los efectos de la terapia miofuncional, la frenectomía, la ortodoncia y la adenoamigdalectomía como tratamientos aislados y combinados?
5. ¿Qué investigaciones conectan hipertrofia adenoidea, ventilación de oído medio/otitis y fenotipos respiratorios en los **mismos niños**?
6. ¿Qué datos refutan de manera suficientemente precisa **cada hipótesis delimitada**, en vez de usar la etiqueta genérica «sin evidencia»?

## Reglas de lectura

- No usar un metaanálisis de asociación transversal para afirmar causalidad longitudinal.
- No mezclar desenlaces de **niños** y **adultos**, ni ancho dental con ancho esquelético.
- No invocar ausencia de significación como demostración de que no existe efecto clínicamente relevante, ni inventar subgrupos beneficiarios para eludir resultados negativos.
- No presentar la biblioteca como revisión sistemática/PRISMA terminada: faltan estrategias exhaustivas, selección por duplicado, extracción y evaluación de sesgo por pregunta.
- Las fichas distinguen **resumen/fragmentos de texto completo** de **lectura metodológica integral**. Ver solicitud documental.

---

<!-- archivo: conocimiento/miofuncional-pediatrica-resultados-contrapuestos.md -->
# ¿Funciona la terapia miofuncional pediátrica? Lo que cambia según el desenlace y el diseño

**Actualización del 03/11/2026.** Esta síntesis es un **contraste crítico de revisiones**, no un nuevo metaanálisis. Conforme a ENFOQUE-CRITICO.md, se deben comparar **preguntas y estimadores antes que titulares**. Las revisiones pueden contener los **mismos estudios primarios**.

## Preguntas que no son intercambiables

1. ¿Los niños con apnea mejoran el **AHI medido por PSG** después de un programa de ejercicios?
2. ¿La mejoría supera a la observada en un **grupo control equivalente**?
3. ¿Mejora la **deglución** en niños con trastornos miofuncionales específicos?
4. ¿La terapia aislada tiene el mismo efecto que un programa con **cirugía, aparatología o tratamiento ortodóncico**?
5. ¿Cambian la **morfología craneofacial/esquelética** y la **apnea** si se libera el frenillo? Esta última pregunta **no** puede contestarse con estudios sobre ejercicios de lengua aislados.

## Cuatro revisiones + una con resultado pediátrico indirecto

| Fuente | Población/desenlace | Qué compara | Resultado observado | Límite decisivo |
|---|---|---|---|---|
| Bandyopadhyay 2020 | 10 estudios, 241 niños tratados y 44 controles adicionales, AHI PSG domiciliaria/laboratorio | Principalmente **basal–final en tratados**, con ejercicios activos y dispositivos pasivos | −1,54 eventos/h (IC95 % −2,24 a −0,85), **I² 72 %**; AHI medio 4,32→2,48/h (~43 % relativa) | **No equivale a un efecto frente a control**; la maduración, selección de cumplidores y cotratamientos pueden explicar parte del cambio. Ninguno de 3 ECA describió cegamiento ni secuencia. |
| Cnockaert 2026 | 8 estudios (4 ECA, 4 no-ECA); objetivo apnea pediátrica | **Diferencia entre grupos en 4 ECA, n=174**, terapia/actividad **aislada** | −1,68 eventos/h (IC95 % −3,61 a +0,24; **p=0,07**): sin beneficio agregado estadísticamente concluyente | Riesgo de sesgo serio, muestra relativamente pequeña, niños con SDB persistente tras cirugía y heterogeneidad; el IC no excluye efectos beneficiosos, pero **no demuestra** eficacia. |
| Avivar-Pardo 2026 | 4 estudios: **1 ECA (n=27) y 3 observacionales (n=217)**, PSG | Síntesis **narrativa** de mejorías dentro de estudios y comparaciones heterogéneas | Varios trabajos describen menor AHI y mejoría funcional, GRADE **baja** | Predominio observacional y sin efecto agregado; la cifra de hasta 58 % alude a un estudio concreto y **no** puede extrapolarse a toda la población. |
| Carey 2026 | **17 estudios, n=633**, alimentación/deglución 4–12 años | Ejercicios orofaciales aislados o junto a cirugía/aparatología | Los 17 incluyen mejoras notificadas; **10/17 calificados de calidad pobre** y **11/17 con cotratamientos**; no hay tamaños de efecto | **No es resultado sobre AHI ni apnea**; sin controles adecuados y medidas heterogéneas, no se puede atribuir todo el cambio a ejercicios. |
| Pisoni 2026 | 9 revisiones, 21 estudios primarios únicos (n=716), principalmente **adultos** | Reevaluación de revisiones con control de solapamiento | En adultos, AHI aproximadamente −9,54/h frente a control; pediatría **escasa** | 5/9 revisiones de calidad críticamente baja y riesgo alto de sesgo; **no transportar efectos de adultos a niños**. |

### La discrepancia que merece atención

**Bandyopadhyay 2020 (resultado positivo) y Cnockaert 2026 (resultado no concluyente) no miden el mismo estimando.** Una reducción significativa respecto al basal **puede coexistir perfectamente** con una diferencia no significativa respecto a un control. Lo primero describe cambio temporal; lo segundo intenta aislar la aportación de la terapia, siempre sujeto a la validez de los ensayos.

La nueva revisión **Avivar-Pardo 2026** tampoco invalida automáticamente a Cnockaert: incluyó solo un ensayo de 27 niños junto a tres estudios observacionales; la propia revisión considera baja la certeza y **no confirma eficacia clínica**. Antes de declarar evidencia «contradictoria», identificar **los estudios primarios compartidos** entre revisiones, su edad, fenotipos y controles.

**Carey 2026** responde una pregunta distinta (deglución) y aporta un buen ejemplo de «todos los estudios incluidos mejoraron» sin que eso permita estimar **efecto causal atribuible** a OMT.

### Importante para las objeciones científicas

- No responder «está demostrado que los ejercicios curan la apnea» citando el 43 % de Bandyopadhyay: es **cambio basal-final**, no efecto neto frente a un grupo control, e incluye dispositivos pasivos.
- No responder «está demostrado que los ejercicios no sirven para nadie» citando Cnockaert: IC amplio y estudios principalmente posquirúrgicos, aunque **sí debilita la indicación de MFT aislada como tratamiento universal de primera línea**.
- No mezclar deglución, ronquidos, postura de reposo, AHI por PSG, dimensiones dentarias y crecimiento de la base esquelética.
- **Una prueba de movimiento de lengua (TRMR) no es prueba de mejoría de apnea**; el paciente puede mejorar postura lingual medida y no tener una reducción clínica pertinente de AHI.
- Las poblaciones adultas y pediátricas requieren síntesis distintas; también separar ejercicios **activos**, dispositivos **pasivos**, cirugía y terapia multimodal.

## Ensayo que podría resolver varias incertidumbres

NCT07249944 plantea **174 niños de 6–12 años**, asignación aleatoria, control, **oAHI objetivo por PSG**, fuerza lingual, cociente Mpal/Mmax, longitud libre del frenillo, respiración oral y fotogrametría craneofacial/postural. **Es un protocolo registrado sin resultados**, no evidencia de eficacia; tampoco incluye una intervención de frenotomía. El registro consultado estaba sin actualizar desde noviembre de 2025.

## Tareas para síntesis formal

1. Abrir originales de los **4 ECA** de Cnockaert y del ECA de Avivar y cotejar posibles participantes repetidos.
2. Extraer los **efectos entre grupos** por AHI, SpO₂ media/mínima, calidad de vida, adherencia y eventos adversos; no mezclarlos con cambios intragrupo.
3. Documentar si los ensayos miden realmente obstrucción nasal, TRMR-TIP, TRMR-LPS, frenillo corto y/o postura espontánea; **no presumir** que lo hacen.
4. Estratificar niños con OSA leve/moderada, apnea persistente tras cirugía, síndrome genético, terapia combinada y modalidad activa/pasiva.
5. Recalcular sesgo por estudio y certeza (RoB 2, ROBINS-I y GRADE) si se realiza revisión sistemática propia. **No se ha hecho todavía.**

**Regla de integridad:** revisión favorable ≠ prueba, revisión negativa ≠ refutación universal; pero los resultados comparativos negativos cuentan y deben informarse.

---

<!-- archivo: conocimiento/postura-cervical-presion-subpalatina-deglucion.md -->
# Postura cervical, presión subpalatina y coordinación lingual: tres fenómenos observados, una hipótesis aún abierta

**Síntesis crítica de tres estudios primarios abiertos** (textos originales revisados el 03/11/2026). No es una revisión sistemática exhaustiva, una prueba de causalidad ni una recomendación terapéutica. Esta sección no atribuye una condición clínica individual a una causa concreta.

## Los tres eslabones que sí se han investigado

| Estudio | Lo que realmente se manipuló | Variable medida | Hallazgo comprobado | Lo que NO demuestra |
|---|---|---|---|---|
| Coppelson 2023 | Posición de la cabeza durante dos CBCT en 90 adultos (cinco condiciones) | Área transversal mínima faríngea (MCA) y ángulo nasion–basion–C3 | Al extender la cabeza: MCA **+147,4 mm²**; en flexión **−41,4 mm²** frente a imagen basal; **sentado/de pie, mentonera y repetir deglución** no tuvieron diferencias medias significativas | Que la extensión sea **causada** por obstrucción respiratoria, que se cure apnea al extenderse, ni que una cirugía/ortodoncia produzca el cambio |
| Engelke 2011 | Boca abierta, cierre labial, deglución con sello y nueva deglución en **20 adultos sanos** | Presión intraoral simultánea en vestíbulo (IOS) y espacio **subpalatino** (SPS) | Tras tragar y conservar sello: IOS **−48,79 mbar** y SPS **−81,86 mbar**; labios solamente cerrados: valores muy próximos a 0 | Que el frenillo altere esa presión, que una falta de succión cause retrusión mandibular o que la presión genere crecimiento óseo concreto |
| Knösel 2012 | Pantalla oral y dos instrucciones de contacto palatino durante degluciones en **29 niños** | Momento del contacto lengua–paladar respecto a interrupción nasal de flujo (NAI) | Las instrucciones **con pantalla** aumentaron contactos palatinos tempranos; la **pantalla sola** no alcanzó significación (p=0,068). Se registraron **542 degluciones**, que no son 542 participantes | Que el cambio se mantenga al retirar la pantalla, que afecte crecimiento/apnea ni que funcione en niños con elevación lingual gravemente restringida |

## Dos advertencias metodológicas especialmente relevantes

### 1. Knösel excluyó precisamente a quienes no lograban elevar la lengua

La inclusión requería **poder colocar la punta en la papila incisiva superior con la boca abierta**. Se excluyeron los niños que no lo lograron. Este dato cambia radicalmente qué población responde el estudio: una mejoría inmediata con maniobras en niños **capaces de alcanzar la papila** no es una prueba de que todos los niños con restricción funcional severa puedan hacerlo sin dificultad ni de que la frenectomía fuera eficaz en otros.

A la inversa, **27 de 29** se clasificaron clínicamente como deglución visceral y las medidas con sensores mostraron contactabilidad palatina mucho más variable. La observación clínica deglutoria puede ser engañosa en algunos casos. **No** equivale a demostrar que toda observación clínica es inválida, ni que el contacto en papila representa la función posterior entera.

### 2. La imagen de una vía aérea no es su función nocturna

Coppelson comprueba que **modificar la posición** del cuello puede modificar **lo que mide una CBCT**. Por tanto, un cambio de MCA entre dos exploraciones puede reflejar diferencias de adquisición y no necesariamente una intervención clínica. Pero no estudió por qué un paciente mantiene espontáneamente esa postura, no midió polisomnografía mientras dormía y no estudió crecimiento. No usar el resultado como demostración de que toda postura adelantada de cabeza **se deba a obstrucción**.

## Control adicional: fiabilidad al repetir una exploración

Sun et al. 2024 examinaron **dos tomografías por paciente sin tratamiento** en 20 adultos, con dos técnicas de adquisición y dos programas de segmentación. Una fiabilidad intraobservador **ICC 0,998–0,999** al reexaminar imágenes no garantiza repetibilidad **entre adquisiciones**. Con Dolphin en CBCT, la diferencia absoluta media entre volúmenes orofaríngeos (OAV) fue **6097,1 mm³**, pero entre cohortes MDCT supinas fue **1793,1 mm³**; no son experimentos equivalentes en postura/protocolo y no prueban que el software sea la única causa. **MCA ≠ OAV.** En un estudio pre/post, antes de atribuir a un tratamiento un cambio de vía aérea hay que preguntarse si es mayor que la variabilidad del instrumento y, además, si se acompaña de un desenlace respiratorio funcional independiente.

**Coppelson mide el efecto de manipular el cuello sobre la MCA; Sun cuantifica variaciones entre tomografías sobre todo en volúmenes**. Son líneas de evidencia complementarias para diseñar estudios, sin demostrar ni descartar una relación causal concreta entre frenillo y postura.

## La hipótesis interdisciplinar que sigue abierta

Se puede **plantear** que en algunos fenotipos interactúen la permeabilidad nasal, el sellado palatino, la presión intraoral, la movilidad anterior/posterior de la lengua y la posición cervical. Los tres estudios hacen esa conexión **biológicamente investigable** porque muestran tres medidas objetivas posibles: **presión SPS/IOS, sincronización de contacto y postura NBC3/MCA**.

**No** han medido esas variables conjuntamente en pacientes definidos por anquiloglosia ni han demostrado esta cadena:

> Frenillo restrictivo → pérdida de sellado posterior → cambio crónico de presión → alteración esquelética → estrechez de vía aérea → extensión cervical.

Es una **hipótesis compuesta**, con varios eslabones pendientes de prueba y con posibles causas alternativas comunes (obstrucción nasal, hipertrofia adenoamigdalar, morfología previa, edad, alteraciones articulares o hábitos).

## Qué experimento permitiría examinarla

En una misma cohorte pediátrica o de adultos, bajo protocolos estandarizados y sin confundir diagnóstico con desenlace:

- Medir por separado **apertura bucal máxima absoluta**, MOTTIP/TRMR-TIP, elevación/succión posterior y variaciones de postura lingual; no confundir una **proporción de apertura** con un examen global del sello.
- Medir **permeabilidad nasal/ORL** y función adenoamigdalar según edad; evitar definir respiración oral solo por postura de labios abiertos.
- Medir **presión SPS/IOS** y estabilidad temporal después de deglución, con equipo validado y sin instruir automáticamente a todos a generar el sello.
- Cuantificar **NBC3** y MCA en imágenes comparables, y distinguir esas medidas en vigilia de **PSG/AHI** del sueño.
- Para crecimiento, usar seguimiento longitudinal y **medidas esqueléticas** separadas de la arcada dentaria, controlando crecimiento normal y ortodoncia.
- Si se investiga un tratamiento, medir contra un **comparador válido**, controles de confusión y resultados clínicos; no convertir cambios antes/después en causalidad.

Las sugerencias constituyen **agenda de investigación**. No son protocolos clínicos personales ni acreditan utilidad de frenectomía u otros procedimientos.

## Acceso y estado

Los **cuatro originales** se localizan abiertos en las páginas de editorial o PMC; se han leído texto y tablas disponibles en formato accesible, **sin duplicar PDFs ni reproducir figuras**. La revisión posterior de los comentarios editoriales de Coppelson y cualquier replicación independiente sigue pendiente.

Ver también enfoque de investigación, mapa interdisciplinar y criterios diagnósticos.

---

<!-- archivo: conocimiento/rutas-de-evidencia.md -->
# Rutas de evidencia: conectar estudios

Este mapa enlaza **hallazgos publicados sobre fenómenos relacionados** para abrir preguntas investigables. No es una hipótesis personal de quien recopila los artículos ni propone una explicación única. Se han utilizado las fichas existentes, sin añadir conclusiones clínicas nuevas.

## Lengua, fascia, contacto palatino y presión

| Resultado documentado | Estudio | Pregunta que abre |
|---|---|---|
| El frenillo se integra en la fascia del suelo de boca | Mills 2019 y Mills 2020: anatomía e histología | ¿Qué variantes anatómicas afectan a la función **en vivo**? |
| El sello oral genera gradientes de presión entre compartimentos | Engelke 2011: manometría en 20 adultos sanos | ¿Qué relación hay entre movilidad, sellado posterior y presión subpalatina? |
| Las maniobras cambian el contacto de la lengua con el paladar durante deglución | Knösel 2012: sensores en 29 niños | ¿Coinciden contacto, presión y postura espontánea **en los mismos sujetos**? |
| La movilidad anterior se puede expresar como cociente de aperturas | Yoon 2017: MOTTIP/MIO | ¿Qué información distinta aportan apertura absoluta, elevación posterior y succión? |

**Conexión exploratoria:** fascia y movilidad ↔ contacto y sellado ↔ presión oral. Son piezas investigadas por separado; el siguiente estudio útil debería medir varios eslabones conjuntamente.

## Fuerza, posición lingual y morfología esquelética: eslabones medidos en una misma cohorte

**Ye et al. (2026)** estudiaron **182 adolescentes de 11–17 años**. En clase III se observó una fuerza lingual MTP menor (**1,65 kg** frente a **2,20–2,21 kg** en I/II) y una posición diferente de la punta (**TTI 8,94 %** frente a **15,26–15,70 %**). En el modelo ajustado, MTP y TTI conservaron asociación con ANB y la **mediación estadística por TTI fue del 32,4 %**. Aquí los tres elementos (fuerza, postura, esqueleto) **sí se midieron en las mismas personas**.

La pregunta científica interesante es **cómo evolucionan juntos a lo largo del crecimiento** y qué ocurre en poblaciones con respiración bucal o deglución atípica, expresamente excluidas de esta cohorte. **TTI es la posición cefalométrica sagital de la punta, no TRMR ni prueba de anquiloglosia**.

## Nariz, sueño y crecimiento dentofacial

| Resultado documentado | Estudio | Conexión por investigar |
|---|---|---|
| Rinitis alérgica asociada a fenotipos de trastorno respiratorio del sueño infantil | Li 2026 | Medir obstrucción nasal, ronquido y PSG en la misma población |
| Rinitis y variables de activación respiratoria en niños derivados a PSG | Kang 2026 | Separar gravedad de apnea y efecto independiente de rinitis |
| Hipertrofia adenoamigdalar asociada con ciertas medidas dentofaciales | Zhao 2025 | Seguimiento de medidas esqueléticas frente a dentarias |
| Cambios dentofaciales estudiados tras cirugía adenoidea o amigdalar | Singla 2026 | Describir crecimiento natural y tratamientos concomitantes |

**Conexión exploratoria:** afecciones ORL ↔ respiración y sueño ↔ morfología dentofacial. El valor es formular **qué debería medirse conjuntamente** en una cohorte, no convertir asociaciones entre artículos en una conclusión causal automática.

## Posición lingual y vía aérea medida directamente

**Zheng et al. (2023)** compararon CBCT de **194 adultos**, con lengua en reposo alta (**98**) o baja (**96**): **no encontraron una diferencia global significativa** de dimensiones faríngeas entre los dos grupos. Sin embargo, el subgrupo con lengua extremadamente baja y mayor espacio intraoral mostró **volúmenes/áreas mayores** en segmentos retropalatino y retrogloso. Esta observación sugiere que **el espacio disponible y la postura lingual no se traducen en un único resultado faríngeo**; la dirección y el segmento estudiado importan.

**Malhotra et al. (2020)** proporcionan un marco para seguir conectando estos resultados: además de anatomía, cuentan los **músculos dilatadores faríngeos**, el *loop gain* y el **umbral de despertar**. Es especialmente útil para investigar por qué personas con geometrías semejantes pueden tener distinto sueño y distinta respuesta clínica.

## Postura cervical y medición de vía aérea

| Resultado documentado | Estudio | Pregunta que abre |
|---|---|---|
| La flexión/extensión modificó la MCA medida por CBCT | Coppelson 2023 | ¿Cómo registrar NBC3 al comparar dos imágenes? |
| Dos exploraciones del mismo paciente pueden arrojar medidas de vía aérea diferentes | Sun 2024 | ¿Cuánto cambio supera el error de repetición y segmentación? |

Estos trabajos complementan el **diseño de futuros estudios**; por qué una persona adopta espontáneamente una postura concreta es una pregunta diferente.

## Cómo sumar una aportación

Registrar el resultado **exacto** estudiado, población, variable, DOI/PMID y qué nueva relación sugiere investigar. Se incorporan también resultados discordantes; cada nuevo trabajo debe servir para completar, revisar o sustituir conexiones existentes. Ver definiciones diagnósticas y quirúrgicas y guía de aportaciones.

---

<!-- archivo: conocimiento/sociedades-cientificas.md -->
# Qué dicen las sociedades científicas y las guías

Documentos de sociedades científicas, agencias y grupos de consenso sobre anquiloglosia, comprobados el 02/11/2026. Para cada uno: si propone un criterio diagnóstico y qué dice en lo esencial. Aquí no se opina sobre ellos: el detalle está en cada ficha.

## Tabla

| Documento | Año | Ámbito | ¿Propone un criterio diagnóstico? | Lo esencial |
|---|---|---|---|---|
| NICE (IPG149, hoy HTG95) | 2005 | Reino Unido, lactancia | No | Frenotomía sin problemas importantes de seguridad; evidencia limitada de mejora de la lactancia. |
| Canadian Paediatric Society | 2015 | Canadá, lactancia | No. Dice que faltan criterios diagnósticos claros | No recomienda frenotomía a todos; sí en un subgrupo con problemas importantes. Hoy figura como retirado de su web. |
| AHRQ / Francis | 2015 | EE. UU., revisión sistemática | No | Evidencia baja o insuficiente sobre lactancia. |
| Cochrane / O'Shea | 2017 | Revisión de ensayos | No | Menos dolor del pezón a corto plazo; sin efecto consistente en la alimentación. |
| GPC de lactancia materna del SNS | 2017 | España, lactancia | No. Pide estudios que unifiquen criterios diagnósticos | Valorar la lactancia con expertos antes; frenotomía si persisten los problemas. Evidencia muy baja. |
| AAO-HNS / Messner | 2020 | EE. UU., otorrinos, 0-18 años | Definición funcional, sin escala. No pudo recomendar ninguna herramienta | 41 de 86 afirmaciones con consenso; sin acuerdo sobre la anquiloglosia «posterior». |
| Australian Dental Association | 2020 | Australia, multidisciplinar, todas las edades | Sí, funcional: exige limitación funcional y una valoración objetiva (por ejemplo Martinelli o Hazelbaker) | No usar «posterior tongue tie» como diagnóstico; manejo no quirúrgico como primera línea. |
| Academy of Breastfeeding Medicine | 2021 | Internacional, lactancia | No. Ninguna herramienta debe usarse sola para decidir | Valoración experta de la lactancia; no operar el frenillo labial ni el «bucal». |
| AAPD (odontopediatría, EE. UU.) | 2019, revisada 2022 | Pediatría dental | No. Ninguna clasificación aceptada por todos | Elevar la lengua importa más que sacarla; no liberar el frenillo labial solo por su aspecto. |
| IAPD (odontopediatría, internacional) | 2019, revalidada 2022 | Pediatría dental | Pide aspecto y función, sin herramienta concreta | Decidir por limitaciones funcionales, no solo por el frenillo. |
| American Academy of Pediatrics | 2024 | EE. UU., lactancia | Mixto: exploración más dificultad de lactancia que no mejora con apoyo; sin una escala única validada | No está claro que liberar el frenillo neonatal mejore la lactancia; trabajo en equipo. |
| ICAP | 2024 | Consorcio profesional internacional | `PENDIENTE DE VERIFICAR` | Guía de práctica de un consorcio de profesionales que tratan frenillos. |
| Academia Brasileña de ORL Pediátrica | 2026 | Brasil, otorrinos, niños | No. La mayoría de métodos no están validados | Sin datos de relación con maloclusión, apnea o reflujo; la frenotomía puede reducir el dolor materno. |
| Guía GRADE de Pediatric Dentistry (Dhar) | 2026 | Lactantes con dificultades de lactancia | Valoración anatómica y funcional; BTAT/TABBY con más apoyo | 12 recomendaciones, todas condicionales y de certeza muy baja. |
| Canadian Academy of Pediatric Dentistry | 2025 | Canadá, odontopediatría, lactancia | No. Pide investigación para estandarizar el diagnóstico | Valoración completa de la lactancia antes de tratar; equipo multidisciplinar; consentimiento informado que incluya no tratar. |
| New Zealand College of Midwives | 2025 | Nueva Zelanda, matronas, lactancia | Herramientas de aspecto y función (BTAT, TABBY, Hazelbaker), no solo el aspecto | El apoyo a la lactancia va antes que la cirugía; poca o ninguna evidencia para «posterior tie», frenillos labiales o bucales y estiramientos. |
| American Association of Orthodontists | 2019 | EE. UU., ortodoncia, apnea | No. Cita la escala funcional de Yoon 2017 | Frenectomía adecuada para habla y masticación, no apoyada para prevenir la apnea. |
| American Association of Orthodontists, actualización | 2026 | EE. UU., ortodoncia, trastornos respiratorios del sueño | No. Señala criterios diagnósticos heterogéneos | No considera la anquiloglosia una causa demostrada; no recomienda frenectomía rutinaria para prevenir ni tratar; ninguna intervención ortodóncica previene estos trastornos. |

## Guías y consensos de apnea infantil

Guías de apnea del sueño en niños, comprobadas el 05/11/2026. La columna «¿Nombra la anquiloglosia?» recoge si el documento llega a tenerla en cuenta, buscado en el texto completo cuando se ha podido leer.

| Documento | Año | Ámbito | ¿Nombra la anquiloglosia? | Lo esencial |
|---|---|---|---|---|
| Consenso español de SAHS infantil | 2011 | España, avalado por SEPAR, SES, SEPEAP, AEPap y SEORL | No (texto completo) | Adenoamigdalectomía como tratamiento de elección, eficacia citada del 78 % y de solo el 27,2 % en un estudio multicéntrico. |
| American Academy of Pediatrics (Marcus) | 2012 | EE. UU., atención primaria | No (texto completo) | Cribado del ronquido, polisomnografía, adenoamigdalectomía como primera opción, CPAP si persiste. Sigue siendo la versión vigente. |
| ERS, 2 a 18 años (Kaditis) | 2016 | Europa | No (texto completo) | Tratamiento escalonado con reevaluación tras cada paso; la terapia miofuncional tras la cirugía, con solo dos estudios de baja calidad. |
| ERS, 1 a 23 meses (Kaditis) | 2017 | Europa, lactantes | Solo en dos lactantes con Beckwith-Wiedemann (texto completo) | Adenoamigdalectomía y CPAP, más intervenciones dirigidas a cada causa. |
| AAO-HNS, amigdalectomía (Mitchell) | 2019 | EE. UU., otorrinos | No (texto completo) | Recomendar amigdalectomía si la apnea está documentada por polisomnografía. |
| AAPD, política sobre apnea | 2021 | EE. UU., odontopediatría | No (texto completo). Pide valorar la posición de la lengua | Cribar, derivar al médico, aparatos solo tras valoración ortodóncica. |
| Consenso de apnea persistente (Ishman) | 2023 | EE. UU., otorrinos | No (texto completo). Ninguna afirmación sobre terapia miofuncional ni expansión | 34 afirmaciones con consenso y 18 sin él sobre la apnea que persiste tras la cirugía. |
| ATS, apnea persistente (Ehsan) | 2024 | Internacional, GRADE | No (texto completo). La terapia miofuncional queda para una actualización | Hasta un 40 % sigue con apnea tras la adenoamigdalectomía; seis recomendaciones condicionales de certeza muy baja. |
| Canadian Thoracic Society / Canadian Sleep Society (MacLean) | 2026 | Canadá, diagnóstico | No (texto completo) | Polisomnografía como estándar; poligrafía domiciliaria como segunda opción en mayores de 5 años sanos. |

No se ha encontrado una guía española de apnea infantil posterior a 2011, ni una versión de la AAP posterior a 2012 (búsqueda del 05/11/2026). El consenso internacional de 2022 sobre apnea (Mediano et al., *Arch Bronconeumol*) trata solo adultos.

## Lo que no se ha podido confirmar (02/11/2026)

- **Asociación Española de Pediatría (AEP):** no se ha encontrado un documento oficial sobre anquiloglosia. Solo fuentes secundarias que citan recomendaciones de su Comité de Lactancia Materna. `PENDIENTE DE VERIFICAR` en aeped.es.
- **Otras sociedades españolas** (SEORL-CCC, odontopediatría, cirugía pediátrica, logopedia): no se ha encontrado un documento de posicionamiento. Hay artículos y protocolos de hospitales, que no son posicionamientos de sociedades.
- **«Consenso internacional de 2023»:** no se ha encontrado uno con ese nombre. Los documentos internacionales localizados son el de la IAPD (2019/2022), el de la ABM (2021) y el de ICAP (2024).
- **American Dental Association (EE. UU.):** una búsqueda web no encontró un posicionamiento propio sobre anquiloglosia: `PENDIENTE DE VERIFICAR` en ada.org. El documento estadounidense de odontopediatría es el de la AAPD.

## Lectura de conjunto (INTERPRETACION del equipo, 02/11/2026)

- Ningún documento ofrece un criterio diagnóstico validado y aceptado por todos. Varios lo dicen de forma explícita (CPS 2015, GPC española 2017, AAO-HNS 2020, AAPD 2022, Brasil 2026).
- Los más recientes coinciden en no diagnosticar solo por el aspecto y en valorar la función (Australia 2020, IAPD 2022, AAO-HNS 2020 en su definición, guía de 2026). Pero no coinciden en qué herramienta usar.
- Casi todos se centran en lactantes y lactancia. Sobre adultos, crecimiento facial o maloclusión dicen poco o que no hay datos.

---

# Objeciones (a favor y en contra)

---

<!-- archivo: objeciones/anquiloglosia-habla.md -->
# Objeción O-004: «El frenillo no afecta al habla»

**Estado:** los estudios comunican resultados diferentes según edad, selección de pacientes, herramientas de habla e intervención. El diagnóstico y el tipo de comparación importan.

## Cara A: no hay pruebas de efecto sobre el habla

- **Kummer 2005**, *The ASHA Leader*. Artículo de opinión. Según notas de trabajo previas (sin verificar en el original), sostiene que la R inglesa puede producirse con la punta abajo y que no hay pruebas de que el frenillo cause problemas del habla. Texto no leído: `PENDIENTE DE VERIFICAR`. Ficha.
- **Kummer 2025**, carta en *AJSLP* contra Cordray 2023. Argumento: incluso con la punta muy restringida se puede compensar y producir los fonemas con el mismo resultado acústico. Cita la revisión de la AHRQ (evidencia insuficiente) y el consenso de la AAO-HNS. Ficha.
- **Salt 2020**, *Int J Pediatr Otorhinolaryngol*, 59 niños preescolares en tres grupos (frenillo previamente tratado, no tratado y sin diagnóstico): **sin diferencias significativas** de movilidad, producción de habla o inteligibilidad. Criterios exactos de clasificación de los grupos pendientes de lectura completa. Ficha.
- **Melong 2024**, *Ear Nose Throat J*, 25 niños derivados por habla. Al mes de la frenotomía, sin mejora en articulación (GFTA-2 85,6 → 87,5; P=0,5) ni inteligibilidad. El 87,9 % de los errores eran propios de la edad. Ficha.
- **Messner 2020**, consenso de ORL pediátricos. Ficha.

## Cara B: hay síntomas descritos más allá de la lactancia

- **Messner y Lalakea 2002**, *Otolaryngol Head Neck Surg*: 30 niños intervenidos con frenuloplastia; protrusión media **14,2 → 25,8 mm** y elevación **5,2 → 22 mm**; de 15 reevaluados en habla, 9 mejoraron articulación. Cohorte pre/post sin comparador; criterio diagnóstico quirúrgico detallado pendiente. Ficha.

- **Cordray 2023**, *AJSLP*, revisión de alcance de 26 estudios. Describe dificultades de habla y articulación, entre otros síntomas, y dice que los datos no son concluyentes. Autores de Emory (no del grupo de Zaghi, como a veces se ha atribuido). Los autores respondieron a Kummer en 2025 (PMID 39913269). Ficha.
- Casos clínicos a favor: mencionados en notas de trabajo sin detalle. `PENDIENTE DE VERIFICAR`.

## Lo que no se puede decir

- «Está demostrado que el frenillo no afecta al habla». La cara A muestra ausencia de pruebas, no prueba de ausencia (ver AGENTS.md, regla 4).
- «El frenillo causa problemas del habla». No hay estudios controlados que lo apoyen.

## El problema del criterio (INTERPRETACION)

**Cuestión metodológica:** si un estudio selecciona por apariencia o longitud, sus resultados pueden no describir la población definida por movilidad funcional. En Melong 2024, la escala usada todavía no consta en la lectura disponible.

## Qué faltaría

Ensayos con selección por criterio funcional (TRMR-TIP y LPS), evaluación del habla cegada, grupo control y seguimiento de meses, separando errores propios de la edad de errores por movilidad.

---

<!-- archivo: objeciones/anquiloglosia-maloclusion.md -->
# Objeción O-002: «JADA 2024 demuestra que la anquiloglosia no influye en la maloclusión»

## Respuesta breve

La revisión de **Póvoa-Santos et al. (2024)** incluye 11 estudios observacionales (2.904 personas) y califica la evidencia como **baja o muy baja certeza**. No demuestra una relación causal general, pero **tampoco la ausencia universal** de asociación entre restricción *funcional* lingual y crecimiento craneofacial. Ficha actualizada a partir del texto completo.

## Qué midió y qué encontró realmente

- **Longitud/inserción del frenillo y clase de Angle (4 estudios):** para clase III vs I, DME 0,37 (IC 95 % −0,50 a 1,25; **I² 93 %**); frente a II, DME 0,55 (−0,52 a 1,63; **I² 95 %**). No hay una asociación agregada concluyente y los resultados individuales son muy heterogéneos.
- **Reducción de apertura bucal (2 estudios):** en clase III hubo 6,67 mm más de reducción que en clase I (IC 95 % 4,01–9,33) y 5,04 mm más que en clase II (2,35–7,72); diferencias estadísticamente significativas, **certeza baja** y sin dirección causal establecida.
- **Dimensiones transversales maxilares:** algunos estudios encontraron diferencias de anchura dental y pendientes palatinas; otros desenlaces mandibulares fueron negativos. No equivale a demostrar crecimiento óseo causado por el frenillo.
- **Diagnósticos distintos:** la **eTable 5** muestra criterios anatómicos y funcionales parciales, incluyendo succión y elevación; **no** sería correcto afirmar que los 11 estudios solo usaron Kotlow. Yoon 2017 midió TRMR-TIP y Kotlow, pero no TRMR-LPS.

## Límites que sí afectan a esta objeción

1. **Todos observacionales**, sin seguimiento prospectivo capaz de determinar cómo evoluciona el crecimiento esquelético con distinta movilidad lingual.
2. **Medidas no intercambiables:** longitud, inserción, elevación de la punta, succión, apertura, arcada dentaria y clase de Angle no resuelven una única hipótesis funcional.
3. **Confusión:** la evaluación JBI de la revisión detectó falta de identificación/control adecuado de confusores en los estudios incluidos. Esto limita resultados positivos **y negativos**.
4. **TRMR y apertura máxima:** como el TRMR es una proporción, un denominador reducido podría elevar el cociente. Es una **posibilidad metodológica**, no un sesgo observado o demostrado en los participantes de Yoon.

## Evidencia con resultados en varios sentidos

- **Yoon 2017:** asociación transversal entre medidas linguales y características maxilares; no permite demostrar que una intervención cambie el crecimiento. Ficha.
- **Kotarska 2024:** revisión adicional con resultados diversos y certeza limitada. Ficha.
- **Deregibus 2021:** algunos resultados mencionados en notas anteriores siguen **PENDIENTES DE VERIFICAR** en el original. Ficha.

## Una nueva pieza relevante: fuerza y postura de lengua en adolescentes (2026)

**Ye et al. 2026** examinaron a **182 adolescentes**: en clase III, MTP **1,65 kg** frente a aproximadamente **2,20 kg** en clase I/II y TTI sagital de punta lingual **8,94 %** frente a **15–16 %**. En modelos ajustados por inclinación incisiva, **MTP (p=0,001)** y **TTI (p=0,004)** siguieron asociados al ANB, con **32,4 % de la asociación total** mediada estadísticamente por TTI. Aporta **mediciones simultáneas de fuerza, postura y morfología** que enriquecen la pregunta. El estudio **no clasificó frenillo** ni investigó intervención; además, excluyó respiración bucal predominante y deglución atípica. Es una vía de investigación distinta del metaanálisis JADA, no una refutación de sus datos.

## Qué se puede concluir

**Sí:** la evidencia publicada y analizada por JADA hasta julio de 2022 es insuficiente para establecer una relación causal generalizable. Existen asociaciones específicas, resultados no significativos y heterogeneidad considerable.

**No:** que la anquiloglosia siempre produzca maloclusión; que liberar el frenillo prevenga maloclusiones; **ni** que la revisión haya descartado toda posible influencia de una restricción funcional bien caracterizada sobre el crecimiento óseo.

**Qué estudio ayudaría:** cohortes longitudinales con diagnóstico funcional explícito y validez examinada, medición separada de dimensiones dentales y basales óseas, control de edad, respiración nasal, hábitos, ortodoncia y otros confusores.

**Fuente:** Póvoa-Santos et al. *JADA* 2024. DOI `10.1016/j.adaj.2023.09.014` · PMID `37999659`. Texto completo y apéndices consultados el 03/11/2026; PDF protegido **no incorporado** al repositorio.

**Modo de uso:** responde según el enfoque crítico del agente. No repitas la conclusión de una revisión sin precisar a qué variables se refiere; tampoco uses sus limitaciones como prueba de la hipótesis opuesta.

---

<!-- archivo: objeciones/extracciones-via-aerea.md -->
# Objeción O-003: «Las extracciones de premolares no afectan a la vía aérea»

**Estado:** cara A con metaanálisis; cara B con una crítica metodológica y un estudio sobre la medida. Nadie ha medido todavía las dos cosas a la vez.

## Cara A: lo que dicen las revisiones

- **Papageorgiou 2025**, *Eur J Orthod*, 11 estudios retrospectivos, 891 pacientes. Sin diferencias en volumen ni área mínima de la vía aérea medidos en CBCT, salvo un área orofaríngea algo mayor con extracciones (+23 mm²). Fuerza de la evidencia moderada; estudios con alto riesgo de sesgo. Ficha.
- **Orabi 2021**, *AJO-DO*, 7 estudios, 268 con extracciones y 342 sin ellas. Sin diferencias salvo +0,41 cm³ orofaríngeo, de relevancia dudosa. Evidencia muy baja. Ficha.
- **Guo 2023**, *Chin J Dent Res*, 12 estudios (6 cuantitativos). Sin cambios significativos; en adultos el área mínima baja sin llegar a ser significativa. Ficha.
- **American Association of Orthodontists**, documentos de posición de 2019 y 2026. No son estudios: revisan la literatura. 2026: «no evidence to support a causal relationship between extractions and the development of SDB», y las medidas de vía aérea en CBCT o cefalometría no sirven para diagnosticar ni para valorar resultados.

**Lectura justa:** de media, y medida en CBCT, la vía aérea no se reduce de forma demostrable tras extracciones.

## Cara B: la crítica de la postura

- **Coppelson 2023**, *J Oral Maxillofac Surg*, **texto completo abierto examinado**. En 90 adultos con **dos CBCT por persona**, flexionar la cabeza cambió la MCA **−41,4 mm²** (p=0,03) y extenderla **+147,4 mm²** (p=0,0018); una agrupación por el ángulo NBC3/modelo describe +5° ≈ +25 % y +10° ≈ +88 % de MCA, **no porcentajes individuales garantizados**. Los cambios promedio por sentado/de pie, mentonera y deglución repetida **no fueron significativos**. Ficha completa.
- **Papageorgiou 2025 no controla la postura.** En el texto completo la posición de la cabeza solo aparece en la discusión, como uno de los factores que influyen en el CBCT.
- **Zaghi**, *Tongue Time 2026*, Zúrich (https://www.youtube.com/watch?v=y6VkQnMBBvc). [Resumen propio traducido al español] La investigación dice que las extracciones no cambian el espacio aéreo posterior porque el paciente compensa adelantando la cabeza y el cuello; hay que mirar la postura y el NBC3. Frase clave de esa traducción: «cuando quitas los premolares, compensan adelantando la cabeza y el cuello». Minuto exacto y frase original en inglés: `PENDIENTE DE VERIFICAR`. Es opinión de experto en vídeo, no un estudio.
- **Zaghi**, ALSC 2020 (https://www.youtube.com/watch?v=G9GrUw7YJD0). [Resumen] Cuenta el caso de una paciente con extracciones y retracción a la que le subió el índice de apnea. Es una anécdota: no prueba causa.

**Lectura justa:** Coppelson demuestra que **manipular la postura altera las mediciones** de vía aérea en CBCT; no demuestra que exista **compensación por obstrucción** tras extraer premolares. Una comparación de CBCT sin registrar NBC3 podría estar confundida por diferencias de adquisición, **sin que ello demuestre que las extracciones tengan efecto perjudicial**. Un estudio sobre cambio de MCA tampoco responde a un cambio real de AHI durante sueño.

## Otra limitación de medición: repetibilidad entre tomografías

- **Sun et al. 2024**, *J Dent Sci*, texto completo abierto: compararon dos escáneres de **10 adultos CBCT** con dos escáneres de **10 adultos MDCT** (dos momentos por persona). A pesar de una repetición de lectura casi perfecta sobre las imágenes (**ICC ≈ 0,998–0,999**), la diferencia absoluta de **volumen orofaríngeo** entre dos CBCT del mismo paciente promedió **6097,1 ± 4616,69 mm³** usando Dolphin; con otro software y protocolo fue menor. Además, se observaron **~5°** de variación en lordosis cervical sin tratamiento entre las exploraciones.
- **Alcance real:** no demuestra que todos los resultados de CBCT sean falsos ni que extraer premolares afecte/no afecte la vía aérea. Las imágenes se tomaron hasta con un año de separación y **CBCT erguido frente a MDCT supino**, de modo que no permite culpar únicamente a un equipo. Su aporte es que un cambio pre/post debe **superar la variación esperable del método** y que software, posición y segmentación deben ser comparables. **Volumen orofaríngeo y MCA son desenlaces distintos**.

La combinación de Sun y Coppelson plantea **dos problemas medibles**, postura y reproducibilidad, sin convertirlos en argumento automático para invalidar cada resultado negativo.

## Qué faltaría

1. Estudios de extracciones frente a no extracciones con CBCT en posición estandarizada (NBC3 registrado) o con el NBC3 como variable, **repetibilidad test–retest documentada** y software/segmentación comparables.
2. Medir también postura cervical, función (polisomnografía, flujo nasal) y síntomas, no solo volumen.
3. Seguimiento longitudinal y grupos comparables en maloclusión y edad.

---

<!-- archivo: objeciones/paladar-estrecho-impide-elevacion.md -->
# Objeción O-001: «No puede elevar la lengua porque no cabe en el paladar estrecho»

**Respuesta provisional:** no puede asumirse esa causalidad solo con la anatomía visible. La lengua es deformable, pero la configuración palatina también puede modificar el espacio y el contacto; la elevación puede estar limitada por distintos mecanismos.

## Apoyos para cuestionar la explicación simple
- Propiedad de hidrostato y deformación tridimensional: Kier & Smith 1985; Gilbert 2007.
- La fascia lingual puede modificar la restricción mecánica de movimientos: Mills et al. 2019 (anatomía).

## Datos que impiden una respuesta simplista inversa
- Deformable ≠ capaz de cualquier trayectoria y distribución de fuerzas.
- Puede haber limitaciones por inserciones, dolor, hábitos, obstrucción nasal, control motor y restricciones dentoalveolares.
- La falta de elevación no diagnostica automáticamente anquiloglosia ni justifica una intervención quirúrgica.

## Preguntas clínicas/experimentales
1. ¿Qué medimos: punta TIP, cuerpo posterior en LPS, succión, postura espontánea o solo contacto amplio palatino?
2. ¿Qué relación existe entre dimensiones palatinas y movilidad funcional? Controlar edad, entrenamiento, control motor y respiración.
3. ¿Se modificó la elevación tras expansión maxilar **sin** intervención lingual? ¿Y tras liberación **sin** expansión?
4. ¿Quién mide, con qué protocolo y cuál es el error intra/interobservador?

**Conclusión adecuada:** «Una bóveda estrecha no basta por sí sola para demostrar que no puede elevarse por falta de espacio; tampoco puede descartarse su influencia geométrica sin evaluación funcional».

---

# Hipótesis abiertas (no demostradas)

---

<!-- archivo: hipotesis/fascia-posicion-mandibular.md -->
# H-001 — ¿Restricción fascial y retroposición mandibular funcional?

**Estado: HIPÓTESIS DE INVESTIGACIÓN, NO HECHO PROBADO.**

## Origen de la pregunta

Es una **línea de investigación exploratoria** surgida al relacionar trabajos de anatomía fascial con estudios sobre función orofacial y posición mandibular. Este documento no expresa una tesis clínica personal de quien compila las referencias.

## Mecanismo propuesto

La fascia del suelo de boca está conectada anatómicamente con la superficie interna de la mandíbula y la superficie ventral lingual (Mills et al. 2019). Se propone investigar si, en un subgrupo con restricción mecánica y determinadas compensaciones neuromusculares, la tensión de tejidos del suelo bucal puede contribuir a una posición mandibular funcional más posterior, modificable tras liberar dicha restricción.

**Importante:** la inserción en mandíbula NO demuestra dirección ni magnitud de fuerza posterior. No equiparar la tensión al elevar la lengua con una fuerza persistente que mueva el hueso en reposo.

## Hipótesis que compiten
1. Cambio de postura mandibular por adaptación neuromuscular/deglución/respiración, sin alteración esquelética.
2. Variación de postura de cabeza o cuello, o del modo de obtener las fotografías.
3. Cambios oclusales o de posición condilar sin crecimiento óseo.
4. Variación normal, maduración o intervención concomitante en mediciones espaciadas.
5. Diferencias del observador al apreciar la proyección del mentón.
6. Posible componente biomecánico fascial restringente (hipótesis a demostrar).

## ¿Qué probaría cada nivel?

- **Respuesta inmediata (minutos/días):** cambio de *posición funcional* o postura; no implica crecimiento del hueso.
- **Datos cuantitativos:** mediciones estandarizadas y repetidas (posición natural de cabeza, reposo mandibular, relación dental/oclusal, exploración funcional) por evaluador cegado donde sea posible.
- **Mecanismo fascial:** biomecánica de cargas o movimiento en vivo + correlación pre/post de tensión funcional y posición; hipótesis falsables sobre dirección de fuerzas.
- **Causalidad clínica:** diseño prospectivo con grupo comparador, ajuste por edad, respiración, ortodoncia y otras intervenciones.
- **Crecimiento mandibular:** seguimiento longitudinal de medidas esqueléticas justificadas clínicamente, evitando radiación innecesaria.

## Fuentes de partida

- Mills et al., 2019, DOI: 10.1002/ca.23343 (anatomía de fascia con inserción mandibular).
- Mills et al., 2020, DOI: 10.1155/2020/1820978 (histología de fascia).
- Póvoa-Santos et al., 2024, DOI: 10.1016/j.adaj.2023.09.014 (certeza baja/muy baja para maloclusiones; no prueba esta hipótesis mecánica).
- He et al., 2026, DOI: 10.1007/s11325-026-03618-x (ficha). En 222 adultos, frenillo más corto y menor TRMR se asocian a una mandíbula más retrasada y pequeña, con correlaciones débiles. Es compatible con H-001, pero los autores proponen también la dirección contraria: mandíbula pequeña primero y frenillo corto como consecuencia. No discrimina entre ambas.

## Pendientes
- [ ] Búsqueda sistemática específica de estudios pre/post de posición mandibular tras frenotomía/frenuloplastia (funcional vs esquelética).
- [ ] Estudios de fuerzas mandibulares y musculatura supra/infrahioidea ligados a anquiloglosia.
- [ ] Elaborar protocolo de evaluación no invasiva y variables de confusión.
- [ ] Revisar trabajos que contradigan el mecanismo y documentarlos.

---

# Opinión de expertos (no son estudios)

---

<!-- archivo: expertos/soroush-zaghi/ambiente-moho-alergias.md -->
# Ambiente y alergias

Ideas públicas de Soroush Zaghi sobre este tema, reconstruidas a partir de sus vídeos. **No es Zaghi hablando ni una guía clínica.** Cómo leer cada entrada: README. Entradas: 13.

## zag-0362 · Opinión · sin verificar (dicho en vídeo)

Zaghi afirma que la inhalación de moho tóxico ambiental es una causa directa de la hipertrofia crónica de amígdalas y adenoides.

- Vídeo: [Excerpts From - TBI Ambassador Update (December 2024). Now Available On-Demand!](https://www.youtube.com/watch?v=DshE1KHc9s0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2024.

## zag-0363 · Experiencia clínica · sin verificar (dicho en vídeo)

Zaghi sostiene que si existe una exposición al moho en el hogar (humedad, filtraciones) y no se trata la causa raíz, las amígdalas y adenoides pueden volver a crecer (regrow) incluso después de una cirugía de extirpación.

- Vídeo: [Excerpts From - TBI Ambassador Update (December 2024). Now Available On-Demand!](https://www.youtube.com/watch?v=DshE1KHc9s0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2024.

## zag-0364 · Opinión · sin verificar (dicho en vídeo)

Según Zaghi, el moho no solo afecta las vías respiratorias, sino que causa disfunción neurocognitiva y emocional, además de inflamación sistémica.

- Vídeo: [Excerpts From - TBI Ambassador Update (December 2024). Now Available On-Demand!](https://www.youtube.com/watch?v=DshE1KHc9s0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2024.

## zag-0365 · Opinión · sin verificar (dicho en vídeo)

Según Zaghi, la inflamación causada por factores ambientales como el moho está vinculada a un aumento del riesgo de cáncer, infecciones y enfermedades cardiovasculares.

- Vídeo: [Excerpts From - TBI Ambassador Update (December 2024). Now Available On-Demand!](https://www.youtube.com/watch?v=DshE1KHc9s0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2024.

## zag-0366 · Experiencia clínica · sin verificar (dicho en vídeo)

Zaghi afirma que la causa más común de obstrucción nasal en bebés no es estructural, sino alergias a la proteína de la leche de vaca o a alimentos consumidos por la madre que pasan a través de la leche materna.

- Vídeo: [Long-term Implications of Untreated Tongue-Tie (Dr. Soroush Zaghi, The Breathe Institute)](https://www.youtube.com/watch?v=cuT6qrm5IT0), minuto `PENDIENTE DE VERIFICAR`.

## zag-0367 · Experiencia clínica · sin verificar (dicho en vídeo)

Zaghi distingue cronológicamente las alergias: las alimentarias predominan en la infancia temprana, mientras que las alergias ambientales suelen empezar a manifestarse entre los 3 y los 6 años de edad.

- Vídeo: [Long-term Implications of Untreated Tongue-Tie (Dr. Soroush Zaghi, The Breathe Institute)](https://www.youtube.com/watch?v=cuT6qrm5IT0), minuto `PENDIENTE DE VERIFICAR`.

## zag-0369 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, la inflamación reactiva a las alergias fuerza la lengua a una posición baja para permitir la respiración bucal, lo que con el tiempo altera el desarrollo del paladar (haciéndolo alto y estrecho).

- Vídeo: [Tongue-Tie, Sleep, Breathing, and Myofunctional Therapy: New Research Updates. Dr. Zaghi at ALSC '20](https://www.youtube.com/watch?v=G9GrUw7YJD0), minuto `PENDIENTE DE VERIFICAR`.
- Vídeo: [Evolution Of Myofunctional Therapy, Lingual Frenuloplasty - Dr. Soroush Zaghi at ALSC 2026.](https://www.youtube.com/watch?v=nlFVT6PUaYc), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2026.

## zag-0370 · Experiencia clínica · sin verificar (dicho en vídeo)

Zaghi observa que los pacientes con Síndrome de Activación de Mastocitos (MCAS), común en personas hipermóviles, sufren reacciones alérgicas severas e inexplicables a factores ambientales que afectan su vía aérea y bienestar general.

- Vídeo: [Evolution Of Myofunctional Therapy, Lingual Frenuloplasty - Dr. Soroush Zaghi at ALSC 2026.](https://www.youtube.com/watch?v=nlFVT6PUaYc), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2026.

## zag-0371 · Estudio citado · sin verificar (dicho en vídeo)

Zaghi se basa en la "Hipótesis Musculoesquelética de Guilleminault" que postula que factores como la salud intestinal, los niveles de vitamina D y la inflamación sistémica son "factores incitadores" que inician el ciclo de respiración bucal e hipertrofia de tejidos linfoides.

- Vídeo: [Tongue-Tie, Sleep, Breathing, and Myofunctional Therapy: New Research Updates. Dr. Zaghi at ALSC '20](https://www.youtube.com/watch?v=G9GrUw7YJD0), minuto `PENDIENTE DE VERIFICAR`.

## zag-0372 · Opinión · sin verificar (dicho en vídeo)

Zaghi propone que las dietas altas en carbohidratos y alimentos procesados obligan al cuerpo a "soplar" (eliminar) más CO2, lo cual se logra más fácilmente a través de la respiración bucal, perpetuando el hábito.

- Vídeo: [Tongue-Tie, Sleep, Breathing, and Myofunctional Therapy: New Research Updates. Dr. Zaghi at ALSC '20](https://www.youtube.com/watch?v=G9GrUw7YJD0), minuto `PENDIENTE DE VERIFICAR`.

## zag-0373 · Opinión · sin verificar (dicho en vídeo)

Zaghi menciona que elementos modernos como los microplásticos, los aceites de semillas y los colorantes alimentarios juegan un papel instrumental en la inflamación y la disfunción de las vías respiratorias.

- Vídeo: [Excerpts From - TBI Ambassador Update (December 2024). Now Available On-Demand!](https://www.youtube.com/watch?v=DshE1KHc9s0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2024.

## zag-0374 · Estudio citado · verificado en PubMed

Zaghi menciona los estudios de Egil Harvold en monos rhesus, donde la obstrucción nasal artificial (análoga a una alergia crónica o congestión ambiental) provocó que los animales desarrollaran paladares estrechos y caras largas.

- Vídeo: [Pediatric Sleep Disordered Breathing and Maxillofacial Development with Soroush Zaghi](https://www.youtube.com/watch?v=eA1Yqbruw4g), minuto `PENDIENTE DE VERIFICAR`.
- Estudio: PMID [6939331](https://pubmed.ncbi.nlm.nih.gov/6939331/), ficha 1981-harvold-primates-respiracion-oral.md.

## zag-0375 · Estudio citado · sin verificar (dicho en vídeo)

Zaghi cita que la transición de respiración bucal a nasal mediante expansión palatina puede reducir físicamente el volumen de las amígdalas y adenoides al eliminar la inflamación reactiva constante.

- Vídeo: [Long-term Implications of Untreated Tongue-Tie (Dr. Soroush Zaghi, The Breathe Institute)](https://www.youtube.com/watch?v=cuT6qrm5IT0), minuto `PENDIENTE DE VERIFICAR`.

---

<!-- archivo: expertos/soroush-zaghi/anquiloglosia.md -->
# Anquiloglosia: evaluación y diagnóstico

Ideas públicas de Soroush Zaghi sobre este tema, reconstruidas a partir de sus vídeos. **No es Zaghi hablando ni una guía clínica.** Cómo leer cada entrada: README. Entradas: 35.

## zag-0014 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, la anquiloglosia es una condición de movilidad lingual alterada debida a la presencia de tejido restrictivo entre la superficie inferior de la lengua y el piso de la boca.

- Vídeo: [Long-term Implications of Untreated Tongue-Tie (Dr. Soroush Zaghi, The Breathe Institute)](https://www.youtube.com/watch?v=cuT6qrm5IT0), minuto `PENDIENTE DE VERIFICAR`.

## zag-0015 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, distinción entre anquiloglosia estructural (la atadura física) y funcional (problemas de movilidad que pueden deberse al frenillo, pero también al espacio, tono o fascia).

- Vídeo: ["Do I Have A Tongue-Tie?" - 5 dimensions of tongue-tie assessment, Dr. Zaghi - The Breathe Course](https://www.youtube.com/watch?v=8dOq11N-qK8), minuto `PENDIENTE DE VERIFICAR`.

## zag-0016 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, cambio terminológico de "frenillo posterior" a "restricción del tercio medio de la lengua" (mid-tongue restriction) o "restricción de elevación media".

- Vídeo: [Updates from Dr. Soroush Zaghi - The Breathe Institute at ALSC Symposium 2024](https://www.youtube.com/watch?v=iGQlzOtT4C0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2024.

## zag-0017 · Experiencia clínica · sin verificar (dicho en vídeo)

Si se usa el término "posterior tongue-tie", Zaghi recomienda escribirlo con un guion ("posterior-tongue tie") para indicar que es la ubicación más posterior de los dos tipos de frenillo, no un problema en la base de la lengua.

- Vídeo: [Updates from Dr. Soroush Zaghi - The Breathe Institute at ALSC Symposium 2024](https://www.youtube.com/watch?v=iGQlzOtT4C0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2024.

## zag-0018 · Experiencia clínica · sin verificar (dicho en vídeo)

Zaghi define el frenillo no como una banda discreta en la línea media, sino como una "red" o "web" de tejido.

- Vídeo: [Myofunctional Therapy and Frenuloplasty Can Be Appropriate Treatments for Obstructive Sleep Apnea](https://www.youtube.com/watch?v=dlU8wxa8474), minuto `PENDIENTE DE VERIFICAR`.

## zag-0019 · Estudio citado · verificado en PubMed

Mills et al. Mediante disecciones cadavéricas, demostró que el frenillo lingual es una estructura compleja de mucosa y fascia, y a veces incluye fibras del músculo geniogloso.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.
- Estudio: PMID [30701608](https://pubmed.ncbi.nlm.nih.gov/30701608/).

## zag-0020 · Estudio citado · sin verificar (dicho en vídeo)

Kotlow (1999). Define la longitud desde la punta hasta la inserción del frenillo.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.
- Estudio: PMID [10635253](https://pubmed.ncbi.nlm.nih.gov/10635253/), ficha 1999-kotlow-clasificacion.md.

## zag-0021 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, umbral numérico: debe ser >16 mm para considerarse normal. Si es <16 mm, hay anquiloglosia estructural.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0022 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, la movilidad anterior de la lengua (TRMR) se mide comparando la apertura bucal con la punta de la lengua en la papila incisiva con la apertura máxima cómoda.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0023 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, umbral numérico: lo ideal es >50% (óptimo 60-80%). Grados 1 y 2 son normales; 3 y 4 son anormales.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0024 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, evalúa la capacidad de elevar la parte media/posterior de la lengua.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0025 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, umbral numérico: debe ser >30% de la apertura bucal máxima.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0026 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, evalúa si el paciente eleva el piso de la boca o tensa el cuello para compensar la falta de movilidad lingual.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0027 · Estudio citado · sin verificar (dicho en vídeo)

Moon (2022). Validó la maniobra de sujetar el piso de la boca para identificar la restricción del frenillo posterior.

- Vídeo: [Dr. Soroush Zaghi at ALSC - Breathe and Thrive 2022, in Las Vegas, NV](https://www.youtube.com/watch?v=3fq6w2buIy0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2022.

## zag-0028 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, evaluación subjetiva mediante palpación con el dedo para sentir la restricción física y fibrosa.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0029 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, dificultad para amamantar, dolor en el pezón de la madre, mal agarre, postura de boca abierta.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0030 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, dificultad con sonidos "R" (sobre todo la "R" rodada), "S", "T", "L", "D".

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0031 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, problemas con texturas sólidas (prefieren purés), náuseas (gagging), ronquidos, sueño inquieto.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0032 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, tensión crónica en cuello y hombros, clenching (apretamiento dental), bruxismo, migrañas, fatiga crónica, UARS.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0033 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, en pacientes con tejidos muy laxos, el problema suele ser la falta de estabilidad, no la restricción. Si pueden tocar el paladar con la lengua estirada hacia atrás pero no elevar la parte media, puede ser un problema de tono o hipermovilidad, no un frenillo que deba cortarse.

- Vídeo: [Evolution Of Myofunctional Therapy, Lingual Frenuloplasty - Dr. Soroush Zaghi at ALSC 2026.](https://www.youtube.com/watch?v=nlFVT6PUaYc), minuto `PENDIENTE DE VERIFICAR`.

## zag-0034 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, no se debe diagnosticar anquiloglosia solo por la presencia de un paladar ojival; el paladar alto es una consecuencia posible, no una prueba del frenillo.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0035 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, casos con buena movilidad (>50% anterior, >30% LPS) sin síntomas ni compensaciones: NO liberar.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0036 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, muchos bebés nacen con inserciones bajas (Grados 3 y 4 de Kotlow) que se remodelan naturalmente entre los 3 y 6 años.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.
- Estudio: PMID [10635253](https://pubmed.ncbi.nlm.nih.gov/10635253/), ficha 1999-kotlow-clasificacion.md.

## zag-0037 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, a menudo, la dificultad para sellar los labios no es culpa del frenillo, sino de una mandíbula retraída. Liberar el labio en estos casos es compensar un problema esquelético.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0038 · Experiencia clínica · sin verificar (dicho en vídeo)

Protocolo "Vita-Wide": Zaghi prefiere no remover tejido, sino realizar una z-plastia para alargar el labio y mejorar la competencia oral.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0039 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, los frenillos bucales (de las mejillas) se asocian con tensión facial y recesión gingival en los premolares.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0040 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, el diagnóstico de los frenillos bucales (de las mejillas) es muy controvertido: la incidencia reportada varía del 5% al 80% entre clínicos, y recomienda basarse en la palpación y en los síntomas, no solo en la apariencia.

- Vídeo: [Updates from Dr. Soroush Zaghi - The Breathe Institute at ALSC Symposium 2024](https://www.youtube.com/watch?v=iGQlzOtT4C0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2024.

## zag-0041 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, en adultos, prefiere un abordaje submucoso desde la línea media (túnel) para evitar cicatrices visibles.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0042 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, crítica el diagnóstico por email o foto sin examen funcional; esto no pasa el "examen del periódico".

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0043 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, crítica a los pediatras que solo miran si la lengua sale (protrusión) y no si sube (elevación).

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0044 · Experiencia clínica · sin verificar (dicho en vídeo)

Zaghi critica el pensamiento lineal ("si corto el frenillo, se cura la apnea"); la medicina es sistémica.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0045 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, crítica a los estudios que comparan grupos sin distinguir entre grados 3 y 4 (sesgo de medición).

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0049 · Estudio citado · sin verificar (dicho en vídeo)

Guilleminault et al. (2011). Sobre la inestabilidad de la condición de "boca semiabierta" (labios cerrados, lengua abajo).

- Vídeo: [Dr. Soroush Zaghi at Tongue Time 2026 in Zurich, Switzerland  (Full Lecture)](https://www.youtube.com/watch?v=y6VkQnMBBvc), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2026.

## zag-0620 · Opinión · sin verificar (dicho en vídeo)

Desde 2024 Zaghi sustituye el término "frenillo posterior" por "restricción del tercio medio de la lengua" para evitar confusión con la base de la lengua, que siempre debe estar baja.

- Vídeo: [Updates from Dr. Soroush Zaghi - The Breathe Institute at ALSC Symposium 2024](https://www.youtube.com/watch?v=iGQlzOtT4C0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2024.
- Cita corta (transcripción automática, puede tener errores): «We introduced this concept of mid tongue restriction... clarifying the concept of posterior tongue tie into mid tongue restriction... Instead of talking about posterior tongue Mobility we don't talk about that anymore we talk about mid tongue Mobility... if you […]»

## zag-0623 · Experiencia clínica · sin verificar (dicho en vídeo)

En su práctica clínica actual, Zaghi ya no mide el TRMR salvo para investigación: usa la maniobra de sujetar el suelo de la boca con el dedo (finger hold) para detectar la compensación y clasificar en tres categorías.

- Vídeo: [Updates from Dr. Soroush Zaghi - The Breathe Institute at ALSC Symposium 2024](https://www.youtube.com/watch?v=iGQlzOtT4C0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2024.
- Cita corta (transcripción automática, puede tener errores): «What we're doing in practice is not so much measuring the TRMR except for research rather be using the bite blocks or just eyeballing it to get into three categories... if there's one thing people should leave here knowing it's […]»

---

<!-- archivo: expertos/soroush-zaghi/contradicciones.md -->
# Contradicciones y cambios de postura

Ideas públicas de Soroush Zaghi sobre este tema, reconstruidas a partir de sus vídeos. **No es Zaghi hablando ni una guía clínica.** Cómo leer cada entrada: README. Entradas: 14.

## zag-0557 · Estudio citado · sin verificar (dicho en vídeo)

Zaghi et al. (2019), "Lingual frenuloplasty with myofunctional therapy", revista Laryngoscope Investigative Otolaryngology. Describe una técnica que a menudo requiere entrar en las fibras superiores del músculo geniogloso (genioglosectomía parcial) para lograr la liberación completa de la fascia profunda.

- Vídeo: [Tongue-Tie, Sleep, Breathing, and Myofunctional Therapy: New Research Updates. Dr. Zaghi at ALSC '20](https://www.youtube.com/watch?v=G9GrUw7YJD0), minuto `PENDIENTE DE VERIFICAR`.
- Vídeo: [Full Lecture: Evaluation, Diagnosis, and Treatment of Tongue, Lip, & Buccal Ties, Dr. Soroush Zaghi](https://www.youtube.com/watch?v=iP3c-C9L9b0), minuto `PENDIENTE DE VERIFICAR`.
- Estudio: PMID [31637291](https://pubmed.ncbi.nlm.nih.gov/31637291/), ficha 2019-zaghi-frenuloplastia-348.md.

## zag-0558 · Experiencia clínica · sin verificar (dicho en vídeo)

En sus actualizaciones más recientes, Zaghi afirma que la técnica es ahora "mucho, mucho menos invasiva" (Fascia Preserving Technique). Ahora evita activamente diseccionar el músculo geniogloso, limitándose a la mucosa y la fascia superficial para minimizar la inflamación y el dolor.

- Vídeo: [Updates from Dr. Soroush Zaghi - The Breathe Institute at ALSC Symposium 2024](https://www.youtube.com/watch?v=iGQlzOtT4C0), minuto `PENDIENTE DE VERIFICAR`.
- Vídeo: [Evolution Of Myofunctional Therapy, Lingual Frenuloplasty - Dr. Soroush Zaghi at ALSC 2026.](https://www.youtube.com/watch?v=nlFVT6PUaYc), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2026.

## zag-0559 · Experiencia clínica · sin verificar (dicho en vídeo)

Zaghi expresaba una fuerte preferencia por las tijeras quirúrgicas sobre el láser, argumentando que el láser da una "falsa sensación de seguridad", causa daño térmico y las tijeras permiten una mejor visualización de la anatomía profunda y de los planos fasciales.

- Vídeo: [Functional Approach to Frenuloplasty: How We Do It - Dr. Soroush Zaghi](https://www.youtube.com/watch?v=C0kel5PNc7c), minuto `PENDIENTE DE VERIFICAR`.
- Vídeo: [Tongue-Tie, Sleep, Breathing, and Myofunctional Therapy: New Research Updates. Dr. Zaghi at ALSC '20](https://www.youtube.com/watch?v=G9GrUw7YJD0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2020.

## zag-0560 · Experiencia clínica · sin verificar (dicho en vídeo)

Zaghi afirma que su preferencia actual es "definitivamente el láser CO2" (LightScalpel) con ajustes específicos para fascia, porque ha reducido su tasa de sangrado del 12% a prácticamente cero.

- Vídeo: [Dr. Soroush Zaghi at ALSC - Breathe and Thrive 2022, in Las Vegas, NV](https://www.youtube.com/watch?v=3fq6w2buIy0), minuto `PENDIENTE DE VERIFICAR`.
- Vídeo: [Updates from Dr. Soroush Zaghi - The Breathe Institute at ALSC Symposium 2024](https://www.youtube.com/watch?v=iGQlzOtT4C0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2024.

## zag-0561 · Experiencia clínica · sin verificar (dicho en vídeo)

Zaghi utiliza sistemáticamente el término "Posterior Tongue-Tie" (frenillo lingual posterior) para describir las restricciones que afectan la elevación del cuerpo de la lengua, a pesar de reconocer que es un término controvertido para los pediatras.

- Vídeo: [Full Lecture: Evaluation, Diagnosis, and Treatment of Tongue, Lip, & Buccal Ties, Dr. Soroush Zaghi](https://www.youtube.com/watch?v=iP3c-C9L9b0), minuto `PENDIENTE DE VERIFICAR`.
- Vídeo: [Frenums, Fascia and Physiology by Dr. Soroush Zaghi & Sanda Valcu-Pinkerton, COM - at AAPMD 2019](https://www.youtube.com/watch?v=BM3TmSXhUIw), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2019.

## zag-0562 · Experiencia clínica · sin verificar (dicho en vídeo)

Zaghi declara que el término "posterior" es un nombre inapropiado (misnomer) y confuso para los cirujanos (pues la base de la lengua es lo que es realmente posterior). Ahora instruye a su equipo y embajadores a usar "Mid-Tongue Restriction" (Restricción de la Lengua Media) para referirse exactamente a lo mismo.

- Vídeo: [Updates from Dr. Soroush Zaghi - The Breathe Institute at ALSC Symposium 2024](https://www.youtube.com/watch?v=iGQlzOtT4C0), minuto `PENDIENTE DE VERIFICAR`.
- Vídeo: [Dr. Soroush Zaghi at Tongue Time 2026 in Zurich, Switzerland  (Full Lecture)](https://www.youtube.com/watch?v=y6VkQnMBBvc), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2026.

## zag-0564 · Experiencia clínica · sin verificar (dicho en vídeo)

Zaghi advierte que en pacientes con hipermovilidad/EDS, los estiramientos tradicionales son "contraproducentes" y "hacen a los pacientes peores" al aumentar la inestabilidad. En estos casos, prohíbe los estiramientos agresivos y pide terapia de estabilidad.

- Vídeo: [Evolution Of Myofunctional Therapy, Lingual Frenuloplasty - Dr. Soroush Zaghi at ALSC 2026.](https://www.youtube.com/watch?v=nlFVT6PUaYc), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2026.

## zag-0565 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, abogaba por el cierre completo con suturas (catgut o PTFE) para lograr una cicatrización por primera intención. En 2022, mencionaba que el PTFE era su elección en heridas inflamadas por ser inerte.

- Vídeo: [Functional Approach to Frenuloplasty: How We Do It - Dr. Soroush Zaghi](https://www.youtube.com/watch?v=C0kel5PNc7c), minuto `PENDIENTE DE VERIFICAR`.
- Vídeo: [Dr. Soroush Zaghi at ALSC - Breathe and Thrive 2022, in Las Vegas, NV](https://www.youtube.com/watch?v=3fq6w2buIy0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2022.

## zag-0566 · Experiencia clínica · sin verificar (dicho en vídeo)

Zaghi rechaza ahora el uso de PTFE porque actúa como una "guillotina" que desgarra el tejido fino. Ha evolucionado a usar "pocas suturas" combinadas con PeriAcryl (pegamento quirúrgico) en los espacios intermedios para reducir la inflamación y la tensión.

- Vídeo: [Updates from Dr. Soroush Zaghi - The Breathe Institute at ALSC Symposium 2024](https://www.youtube.com/watch?v=iGQlzOtT4C0), minuto `PENDIENTE DE VERIFICAR`.
- Vídeo: [Grade 4 Tongue-Tie - Bleeding Management, PeriAcryl Glue, Sutures, Functional Frenuloplasty - TBI](https://www.youtube.com/watch?v=SQRk2zUQdvE), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2024.

## zag-0567 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, en "Updates ALSC 2024", afirma que si el frenillo es Grado 4 (atado a la punta) y el paciente es muy estrecho, se puede hacer una liberación Fase 1 (mínima) primero para permitir que la lengua se mueva lo suficiente para participar en la expansión.

- Vídeo: [Updates from Dr. Soroush Zaghi - The Breathe Institute at ALSC Symposium 2024](https://www.youtube.com/watch?v=iGQlzOtT4C0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2024.

## zag-0568 · Estudio citado · sin verificar (dicho en vídeo)

Yoon, Zaghi et al. (2017). El diagnóstico de anquiloglosia funcional se basaba casi exclusivamente en la medición del TRMR (Tip y LPS) y su comparación con la apertura máxima cómoda (CMO).

- Vídeo: [Full Lecture: Evaluation, Diagnosis, and Treatment of Tongue, Lip, & Buccal Ties, Dr. Soroush Zaghi](https://www.youtube.com/watch?v=iP3c-C9L9b0), minuto `PENDIENTE DE VERIFICAR`.
- Estudio: PMID [28994495](https://pubmed.ncbi.nlm.nih.gov/28994495/), ficha 2017-yoon-maxilar.md.

## zag-0569 · Experiencia clínica · sin verificar (dicho en vídeo)

Zaghi admite que el TRMR es "difícil de realizar" correctamente (especialmente en telemedicina) y que ahora el estándar de su clínica para decidir una cirugía es el "Floor of Mouth Hold" (maniobra manual). Afirma que el TRMR se mantiene más para investigación que para decisión clínica diaria.

- Vídeo: [Updates from Dr. Soroush Zaghi - The Breathe Institute at ALSC Symposium 2024](https://www.youtube.com/watch?v=iGQlzOtT4C0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2024.

## zag-0570 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, en el posoperatorio, realiza reaperturas de la herida de forma vigorosa para evitar el re-anclaje.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0571 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, "Nosotros no reabrimos la herida así de agresivamente". Prefiere un enfoque de "menos es más" y suturas para minimizar el trauma.

- Vídeo: [Evolution Of Myofunctional Therapy, Lingual Frenuloplasty - Dr. Soroush Zaghi at ALSC 2026.](https://www.youtube.com/watch?v=nlFVT6PUaYc), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2026.

---

<!-- archivo: expertos/soroush-zaghi/discrepancias.md -->
# Discrepancias entre lo que dice Zaghi y lo que dicen los estudios

**Qué es:** los 16 registros de la base original de la extracción (aquí, zaghi.jsonl con los registros publicables) que salieron `discrepante` al contrastarlos con PubMed, agrupados por afirmación. Para cada uno: qué dijo Zaghi (cita literal, vídeo y año si el título lo tiene) y qué dice el estudio (PMID y frase del resumen o del texto completo). La cita de Zaghi sale de una pregunta a NotebookLM que pedía la transcripción literal (q60-q65); las transcripciones son automáticas y traen errores de reconocimiento (por ejemplo "Lchnowski", "Yun", "Feres").

**Regla de atribución:** un error solo se le atribuye a Zaghi si lo dice él en la cita literal. Si el dato erróneo aparece únicamente en el resumen de NotebookLM y en la transcripción él no lo dice, el error es de NotebookLM. Un error de reconocimiento de voz no es de nadie.

**Límite:** el texto completo solo se pudo comprobar en los artículos de acceso abierto (Lichnowska 2024). Para los demás se usa el resumen de PubMed; lo que el resumen no recoge se marca "no comprobable", no como error.

## Resultado

| Clasificación | Registros | De quién es el error |
|---|---|---|
| Exagerada | 1 (0112) | **Zaghi** |
| Fuera de contexto | 2 (0537, 0479) | **NotebookLM** |
| Atribución equivocada | 10 (0184, 0233, 0325, 0556, 0480, 0040, 0328, 0151, 0326, 0039) | **NotebookLM** en 8; **mixto** en 2 (0039 y 0326: además Zaghi redondea o nombra la revista de forma coloquial); 0040 y 0328 incluyen un error de transcripción automática |
| Falso positivo (sí cuadra; se corrige el estado) | 3 (0240, 0477, 0562) | Ninguno (la cifra es correcta; el año 2024 es de NotebookLM) |
| Cifra cambiada de variable | 0 | |

**De los 16, 1 es error de Zaghi, 2 son mixtos, 10 son de NotebookLM (o de la transcripción) y 3 no son error.**

## 1. GRAVE: el ensayo aleatorizado con terapia miofuncional (0112). Exagerada. Error de Zaghi

- **Dijo Zaghi** (*Dr. Soroush Zaghi at Tongue Time 2026 in Zurich*, 2026): «my colleague Dr anna Lchnowski who used our protocol... to provide the first ever known randomized control trial on lingual frenuloplasty with myofunctional therapy demonstrating the immense effect effects it has not only on chewing swallowing tongue posture but also […]».
- **Dice el estudio** (Lichnowska A, Gnatek A, Tyszkiewicz S, Kozakiewicz M, Zaghi S, *J Clin Med* 2024, PMID 39336841; Zaghi es coautor): «prospective randomized control trial with 155 subjects... significantly more effective in improving tongue mobility and stomatognathic functions such as swallowing, breathing, and oral resting postures as compared to the reference group who underwent myofunctional therapy only».
- **Qué no cuadra:** en el texto completo abierto (PMC11432234) la palabra "retention" no aparece ni una vez, y "sleep" solo sale en la introducción, hablando de trabajos de otros. El ensayo mide función oral, no sueño ni retención ortodóntica. Que sea "el primer RCT conocido" es su afirmación; no se ha comprobado.
- **Nota:** el error de NotebookLM está en el año ("2022?" y "2025/2026"): Zaghi no da año y el artículo es de 2024. El nombre "Lchnowski" es un error de la transcripción automática; el nombre real es Lichnowska. Corregir en los registros 0040 y 0328 (ver grupo 7).

## 2. GRAVE para la integridad del registro: la varianza del 7.6% (0537). Fuera de contexto. Error de NotebookLM

- **Dijo Zaghi** (*Frenums, Fascia and Physiology*, AAPMD 2019): «Tongue tie actually only accounts for about seven point six percent of the variance that means that tongue tie counts for less than ten percent of the reason why you get high arch palate... It's not only tongue tie that […]»
- **Dice el registro** (NotebookLM): «restricción de movilidad lingual explica el 7.6% de la varianza en la estrechez del paladar, **validando la necesidad de expansión**».
- **Qué no cuadra:** Zaghi usa el 7.6% para decir que el frenillo explica una parte pequeña, no para justificar la expansión. NotebookLM le atribuye una conclusión que él no saca en esa cita. Además, el 7.6% no aparece en el resumen del artículo de PubMed (Yoon 2017, PMID 28994495): no comprobable; el texto completo no es de acceso abierto. Corregir la frase y marcarla `no_verificado`.

## 3. Rangos del ángulo NBC3 (0479). Fuera de contexto. Error de NotebookLM

- **Dijo Zaghi** (*Updates ALSC 2024* y *FAirEST 6 + 4*): «The NBC3 angle should be around 105 to 110 if it's like 120 125 that's where you're maxed out»; en otra ocasión «the average measurement is about 105 plus or minus 5»; y «the usual measurement... is about 115».
- **Dice el registro:** «El rango normal del ángulo NBC3 es de 105° a 115°».
- **Qué no cuadra:** NotebookLM funde dos citas distintas (105±5 y "en torno a 115") en un solo rango. El estudio (Coppelson et al., *J Oral Maxillofac Surg* 2023, PMID 36841260) da una media basal de 112.4 ± 8.3° en 90 voluntarios, que es la media de la muestra, no un rango normal. Se corrige: Zaghi da varias cifras según la charla.

## 4. Las cifras de la inclinación de la cabeza (0477, 0562). Falsos positivos; además un hallazgo sobre Zaghi

- **Dijo Zaghi**, con cifras distintas según la charla: «A small change of five degrees so if you're five degrees up or five degrees down you have a 25% difference» (*Dr. Zaghi on Research Principles*, AAPMD 2021, y *ALSC 2022*); «If you go up 10° or down 10° the results are different by 86%» (mismas fuentes, 2021-2022); «10° alters it by 88%... 20° by 150%» (*FAirEST 6 + 4*, sin año); «a 10 degree change changes by 80%» (*Updates ALSC 2024*).
- **Dice el estudio** (PMID 36841260): «increasing NBC3 by +5 and +10° resulted in MCA changes of +25% and +88%, whereas a decrease in NBC3 by −5 and −10° results in MCA changes of −21% and −23%».
- **0477 y 0562, 5° = 25%:** la cifra **cuadra** (hacia arriba). Son **falsos positivos**. El único error es el año «2024» (NotebookLM: el artículo es de 2023; Zaghi no dice el año). Se corrige el año y el estado pasa a `verificado`.
- **Hallazgo adicional, no entre los 16 (Zaghi, fuera de contexto):** en 2021-2022, antes de la publicación, Zaghi presenta el efecto como simétrico («up or down»: 25% y 86%). El estudio publicado muestra que es asimétrico: hacia abajo cambia solo −21% y −23%. Las cifras de 10° que da (86%, 88%, 80%) no coinciden entre charlas; la publicada es 88% hacia arriba. No es un error grave: es una simplificación oral de datos aún sin publicar. La base de conocimiento debe dar las cifras del artículo.

## 5. El ángulo NBC3 de 105-110° (0240). Falso positivo

- **Dijo Zaghi:** «should be around 105 to 110... 120 125 that's where you're maxed out». **Estudio:** media basal 112.4 ± 8.3° (PMID 36841260). Zaghi da un objetivo, el estudio una media de muestra: no se contradicen. El estado pasa de `discrepante` a `no_verificado`.

## 6. Yoon 2017: revista y título equivocados (0184, 0233, 0325, 0556) y ancho de 38-42 mm atribuido a Yoon (0480). Atribución equivocada. Error de NotebookLM

- **Dijo Zaghi** (*AACP 2018*, *AAPMD 2019*): «In the study researchers have gotten away the tongue mobility and 302 patients»; «we looked at 300 and two consecutive subjects in an orthodontic practice». **En las citas literales recuperadas no nombra la revista de este estudio** (la etiqueta «orthodontic journal» de la respuesta q60 es de NotebookLM, no una cita). En otro momento dice de otro trabajo de Audrey Yoon (que la transcripción escribe "Yun"): «published I think in the journal sleep», una hoja de ruta de crecimiento craneofacial.
- **Dice el estudio** (Yoon AJ, Zaghi S, Ha S, Law CS, Guilleminault C, Liu SY, *Orthod Craniofac Res* 2017, PMID 28994495): título «Ankyloglossia as a risk factor for maxillary hypoplasia and soft palate elongation: A functional - morphological study»; «Cross-sectional cohort study of 302 consecutive subjects from an orthodontic practice»; «Restricted tongue mobility was not associated with hyoid bone position or Angle's skeletal classification».
- **Qué no cuadra:** los registros dicen *Sleep Medicine* y el título «Impact of Tongue-tie on Maxillary Arch». Zaghi dice 302 sujetos en una consulta de ortodoncia: coincide con el artículo, y no se le oye decir *Sleep Medicine* en ninguna cita recuperada. La revista y el título erróneos son de NotebookLM (probable mezcla con el otro trabajo de Yoon que Zaghi sitúa en *Sleep*). No se descarta que lo diga en un vídeo que la búsqueda no devolvió. La sustancia (302 sujetos, asociación con estrechez del arco y elongación del paladar blando) sí cuadra; «grados 3 y 4» y el 7.6% no aparecen en el resumen: no comprobables.
- **0480 (38-42 mm):** el registro atribuye a Yoon 2017 que 38-42 mm es el ancho intermolar ideal. Zaghi y Coppelson (*Advances in Surgical Technique*): «if you look at interolar studies I would say anywhere between 38 to 42 millimeters of intermolear width tends to be a good spot for most adults». Es de Coppelson, refiriéndose a «estudios intermolares» sin nombrar autor; no hay cita que lo vincule a Yoon 2017. Error de NotebookLM.

## 7. Lichnowska / "Lchnowski": nombre y año (0040, 0328). Atribución equivocada. NotebookLM y transcripción

- Zaghi dice «Dr anna Lchnowski» (transcripción automática; el nombre real es Lichnowska) y «prospective randomized control trial»; **no da año**. Los registros dicen «2022?» y «2025/2026»: años inventados por NotebookLM. Estudio real: *J Clin Med* 2024, 155 sujetos (PMID 39336841).

## 8. FAirEST 6: año y revista (0151, 0326). Atribución equivocada. Mixto

- **Dijo Zaghi** (*Tongue Time 2026*): «The fairest six... is now published in the journal of pediatric dentistry»; y en *Research Principles* (2021) «for the fair 6 which is now available published and part of the guidelines». **No da año.** El OR de 19 («dental wear... 19 times odds») y el intervalo 4.8-77 sí los dice él.
- **Dice el estudio** (Oh JS, Zaghi S, Peterson C, Law CS, Silva D, Yoon AJ, *Pediatr Dent* 2021, PMID 34467840): «96 mixed dentition children... FAIREST-6 is a concise and validated clinical assessment tool».
- **Qué no cuadra:** el año «2020» es de NotebookLM (el artículo es de 2021; Zaghi no lo dice). La revista real es *Pediatric Dentistry* (la de la Academia Americana); Zaghi la nombra como «journal of pediatric dentistry»: nombre coloquial, no un error de fondo. El OR 19 no aparece en el resumen de PubMed; sí en su charla.
- **Nota:** «Ferris/Feres» son errores de reconocimiento de voz de "FAirEST". El "estudio Feres" con 600-650 pacientes que Zaghi cita en 2020-2022 se parece más al estudio de succión palatina (Zaghi 2021, 611 sujetos, PMID 33386612) que al FAirEST (96 niños).

## 9. Baxter y el diastema (0039). Atribución equivocada. Mixto

- **Dijo Zaghi:** «we've done the study with dr richard baxter where they took a hundred kids they took a picture of the diastema... and then took another picture six months to a year later and they saw that it closed»; «he had 100 photos». **No da año ni revista** (q64); cuenta que fue rechazado en ocho revistas.
- **Dice el estudio** (Baxter RT, Zaghi S, Lashley AP, *Int Orthod* 2022, PMID 35283058): «109 patients... a decrease in diastema width was observed in 94.7% [primary dentition]... 92.9% [mixed dentition]».
- **Qué no cuadra:** «100» es el redondeo que dice Zaghi (charla anterior a la publicación); 109 es el dato del artículo. El año «2020» es de NotebookLM.

## Correcciones que salen de esto (se aplican en la Fase 3)

1. 0477 y 0562: cifra verificada; año 2023; estado `verificado`, PMID 36841260.
2. 0240: pasa a `no_verificado`.
3. 0184, 0233, 0325, 0556: quitar «Sleep Medicine» y el título erróneo; escribir revista *Orthod Craniofac Res* y título real; lo que el resumen no recoge se queda `no_verificado`.
4. 0480: reatribuir a Coppelson, citando «estudios intermolares».
5. 0537: reescribir con el sentido que le da Zaghi (el frenillo explica solo el 7.6%; hay otros factores) y marcarlo `no_verificado`.
6. 0479: separar las tres cifras que dice Zaghi según la charla.
7. 0040, 0328, 0112: nombre Lichnowska, año 2024 (según PubMed); 0112: dejar la afirmación de Zaghi tal cual y añadir que el estudio mide función oral, no sueño ni retención.
8. 0151, 0326: año 2021; revista *Pediatric Dentistry*.
9. 0039: 109 pacientes, 2022; Zaghi dice «100».

---

<!-- archivo: expertos/soroush-zaghi/doctrina-negativa.md -->
# Lo que rechaza

Ideas públicas de Soroush Zaghi sobre este tema, reconstruidas a partir de sus vídeos. **No es Zaghi hablando ni una guía clínica.** Cómo leer cada entrada: README. Entradas: 18.

## zag-0539 · Experiencia clínica · sin verificar (dicho en vídeo)

Zaghi critica que es una encuesta de opiniones de 12 médicos sin experiencia clínica en frenuloplastia funcional y que rechazaron deliberadamente la participación de expertos por ser "controversiales".

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0540 · Experiencia clínica · sin verificar (dicho en vídeo)

Zaghi denuncia un sesgo de medición, ya que solo consideran frenillo si no se puede protruir la lengua, ignorando la elevación funcional.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0541 · Estudio citado · sin verificar (dicho en vídeo)

Zaghi rebate el estudio señalando que los propios datos de Salt et al. muestran puntuaciones más altas en niños tratados, pero los autores lo calificaron como "sin diferencia" por falta de significancia estadística (sesgo de confirmación).

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0542 · Experiencia clínica · sin verificar (dicho en vídeo)

Zaghi señala un sesgo de rendimiento, ya que los resultados de una "frenotomía" simple no son comparables a los de una frenuloplastia funcional con terapia.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0543 · Opinión · sin verificar (dicho en vídeo)

Zaghi califica el estudio de "broma" y respondió "LOL" en redes porque los autores califican de mentira que el frenillo cause reflujo o respiración bucal basándose en sus creencias y no en la fisiología.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0544 · Experiencia clínica · sin verificar (dicho en vídeo)

Zaghi califica este enfoque como "retrógrado" por buscar cortar más tejido en lugar de tratar la deficiencia ósea (espacio lingual) mediante expansión.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0545 · Experiencia clínica · sin verificar (dicho en vídeo)

Zaghi rechaza este enfoque porque elimina el espacio vital para la lengua (la "jaula"), forzándola a colapsar en la vía aérea y empeorar o causar apnea.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0546 · Experiencia clínica · sin verificar (dicho en vídeo)

Zaghi advierte que esto suele crear una cicatriz fija y gruesa que empeora la movilidad; "cortar sin terapia es como hacer una cirugía de hombro sin fisioterapia".

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0547 · Experiencia clínica · sin verificar (dicho en vídeo)

Zaghi desaconseja estos dispositivos porque causan una lesión térmica profunda que deriva en una cicatrización fibrótica excesiva y mayor dolor postoperatorio.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0548 · Experiencia clínica · sin verificar (dicho en vídeo)

Aunque son menos inflamatorias, Zaghi ya no las usa porque actúan como una "guillotina" y desgarran la mucosa delgada cuando el paciente mueve la lengua.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0549 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, ha refinado su técnica para ser "fascia preserving" (preservación de fascia); la disección muscular aumenta drásticamente el dolor (del 3.7% al 45%) y el riesgo de inflamación severa sin necesidad.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0550 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, el soporte del mentón empuja la lengua hacia el paladar artificialmente y altera la postura de la cabeza, ocultando la obstrucción real y falseando los resultados.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0551 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, el IAH ignora el esfuerzo respiratorio y los micro-despertares; pediatras y ENTs rechazan tratar a niños que sufren fatiga severa solo porque su IAH es normal.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0552 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, la tensión del mentalis es una compensación necesaria para cerrar la boca en una cara con crecimiento vertical; el Botox solo empeora el problema al no tratar la causa raíz (maxila deficiente).

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0553 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, en los pacientes con hipermovilidad (síndrome de Ehlers-Danlos) el tejido ya está demasiado suelto; estirarlos más aumenta la inestabilidad. Necesitan protocolos de fortalecimiento y estabilidad, no estiramiento.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0554 · Experiencia clínica · sin verificar (dicho en vídeo)

Zaghi desaconseja diagnosticar sin examen funcional (viola el "Newspaper Test") y critica eventos que dañan la reputación del campo, como conferencias con alcohol en el nombre.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0555 · Experiencia clínica · sin verificar (dicho en vídeo)

Sandraluz Gonzalez critica que el cuerpo no es compartimentable; ver la lengua sin ver el pie o la respiración es garantía de fracaso clínico.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0556 · Experiencia clínica · sin verificar (dicho en vídeo)

Tras una prueba de seguridad, Zaghi lo rechaza porque huele a gasolina, hace toser al paciente y no mostró beneficios clínicos claros.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

---

<!-- archivo: expertos/soroush-zaghi/estilo-vida.md -->
# Estilo de vida, dieta y rutinas

Ideas públicas de Soroush Zaghi sobre este tema, reconstruidas a partir de sus vídeos. **No es Zaghi hablando ni una guía clínica.** Cómo leer cada entrada: README. Entradas: 16.

## zag-0402 · Opinión · sin verificar (dicho en vídeo)

Soroush Zaghi sostiene que las dietas modernas ricas en carbohidratos procesados obligan al cuerpo a eliminar más CO2, lo cual se facilita mediante la respiración bucal, perpetuando este hábito disfuncional.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0403 · Opinión · sin verificar (dicho en vídeo)

Zaghi y Sandraluz Gonzalez afirman que el consumo de alimentos blandos, purés y bolsas de comida (pouch foods) no proporciona el estímulo mecánico necesario para el crecimiento óseo de los maxilares, lo que resulta en arcadas estrechas y falta de espacio para la lengua.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0404 · Experiencia clínica · sin verificar (dicho en vídeo)

Zaghi promueve el "Baby-Led Weaning" (destete guiado por el bebé) para que los niños mastiquen alimentos sólidos (como trozos de carne) desde temprano, estimulando el desarrollo facial hacia adelante.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0405 · Opinión · sin verificar (dicho en vídeo)

Zaghi menciona que los aceites de semillas, microplásticos y colorantes alimentarios son factores ambientales instrumentales en la inflamación crónica de las vías respiratorias.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0406 · Opinión · sin verificar (dicho en vídeo)

La Dra. Nora Gadisy Zaghi postula que las dietas pre-industriales de alimentos duros y enteros simuladas con aparatos funcionales pueden ayudar a desarrollar las arcadas en niños con mandíbulas pequeñas.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0407 · Experiencia clínica · sin verificar (dicho en vídeo)

Zaghi realiza una rutina de "movimiento intenso" de 1 a 2 minutos (calistenia, burpees o abdominales) justo después de meditar por la mañana para activar el corazón y entrar en el cuerpo.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0408 · Opinión · sin verificar (dicho en vídeo)

Zaghi es un firme creyente en la terapia de frío; utiliza duchas de agua fría y baños de hielo para restablecer el sistema nervioso y reducir la inflamación sistémica.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0410 · Experiencia clínica · sin verificar (dicho en vídeo)

Zaghi incluye en su protocolo rituales de respiración matutina (como respiración de caja, respiración Alpha o el método Wim Hof) con el objetivo de oxigenar plenamente el cuerpo y el cerebro al iniciar el día.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0411 · Experiencia clínica · sin verificar (dicho en vídeo)

Como otorrinolaringólogo, Zaghi introduce técnicas respiratorias para tratar la obstrucción nasal que no dependen de medicamentos ni de cirugía, enfocándose en la higiene nasal (lavados con xilitol) y reeducación funcional.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0414 · Opinión · sin verificar (dicho en vídeo)

Zaghi usa la metáfora del "termostato vs. termómetro": la rutina matutina permite ser un termostato que decide por adelantado qué emociones sentir (amor, curiosidad, gratitud) en lugar de solo reaccionar al ambiente.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0415 · Experiencia clínica · sin verificar (dicho en vídeo)

Zaghi dedica 15 a 20 minutos cada mañana a la meditación de atención plena (mindfulness) para entrar al día con la mente clara.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0416 · Experiencia clínica · sin verificar (dicho en vídeo)

Zaghi explica que la apnea del sueño y el UARS mantienen al paciente en un estado de "lucha o huida" (tono simpático elevado) durante la noche, lo que se traduce clínicamente en ansiedad, irritabilidad y fatiga extrema durante el día.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0417 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, para pacientes con alta ansiedad preoperatoria recomienda protocolos de CBD (cannabidiol) de espectro completo o terapia craneosacral. Las dosis y concentraciones no se recogen en esta base.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0418 · Experiencia clínica · sin verificar (dicho en vídeo)

Sandraluz Gonzalez resalta la importancia de gestionar la "defensividad oral" y la ansiedad mediante el trabajo corporal, citando el libro The Body Keeps the Score, para evitar que la fascia se tense durante y después de la cirugía.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0419 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, testimonios en TBI muestran que corregir la vía aérea estructuralmente (como la reconstrucción de un tabique desviado o cirugía MMA) puede permitir que los pacientes abandonen medicamentos para el insomnio como Ambien tras años de dependencia.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0420 · Experiencia clínica · sin verificar (dicho en vídeo)

[INFERENCIA FUERTE: Zaghi sugiere que la respiración bucal y los ronquidos pueden causar cambios físicos en la materia gris cortical, lo que explicaría la persistencia de problemas conductuales y de fatiga mental. INFERENCIA FUERTE] (Fuente: Long-term Implications of Untreated Tongue-Tie ).

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

---

<!-- archivo: expertos/soroush-zaghi/estudios-citados.md -->
# Estudios y referencias citados en el corpus (Soroush Zaghi / The Breathe Institute)

**Verificación PubMed (20/09/2026):** las tres columnas finales de cada tabla son el resultado de buscar cada referencia en PubMed. Solo se marca **verificado** con PMID/DOI y coincidencia de autor, año y cifra; **discrepante** si existe pero cambia algo; **no encontrado** si no aparece; **no aplica** si es libro, prensa o histórico no indexable.

**Alcance:** todo lo que NotebookLM identificó en las respuestas de NotebookLM como estudio, artículo, libro, ensayo o dato publicado mencionado en el corpus. Las columnas de la izquierda son lo que dio NotebookLM; **las tres últimas son la verificación en PubMed** (lo que no tiene PMID/DOI sigue sin verificar). Un nombre como "Lchnowski" o el nombre de un estudio ("Ferris 6" vs "FAirEST 6") puede ser un error de transcripción de los vídeos.
**Estado:** parcial, ampliado en la segunda sesión (q19-q29).
**Recuento:** ~70 referencias distintas tras deduplicar unas 280 menciones brutas (≈17 propias de Zaghi/TBI, ≈53 de terceros). ≈25 con referencia incompleta.

Las discrepancias entre respuestas se anotan en "Notas".

## A. Trabajos propios de Zaghi / The Breathe Institute
| # | Referencia | Revista (si la dice) | Dato clave | Notas | Estado PubMed | PMID / DOI | Nota PubMed |
|---|---|---|---|---|---|---|---|
| 1 | Zaghi et al. 2019, "Lingual frenuloplasty with myofunctional therapy: explore safety and efficacy" | Laryngoscope Investigative Otolaryngology | 348 casos consecutivos; 91% satisfacción; 87% mejora de calidad de vida; movilidad lingual 96.5%; bruxismo 91%; deglución 80%; respiración nasal 78%; tensión miofascial 77.5%; dolor severo 45%, sangrado 12.6% (2% prolongado), entumecimiento de la punta 4.9% | Muestra dada como 348 o 350; calidad de vida 86-87%. Según Zaghi, uno de los 3 artículos más descargados de la revista | verificado | PMID 31637291 / DOI 10.1002/lio2.297 | 420 pacientes tratados, 348 encuestas (83%): satisfacción 91%, calidad de vida 87%, respiración bucal 78.4%, ronquido 72.9%, apretamiento 91.0%, tensión miofascial 77.5%, complicaciones menores <5%. NO comprobadas en el resumen: movilidad 96.5%, deglución 80%, dolor severo 45%, sangrado 12.6%, entumecimiento 4.9% (pueden estar en el texto completo). |
| 2 | Yoon, Zaghi et al. 2017, "Impact of Tongue-tie on Maxillary Arch" | Sleep Medicine | 302 sujetos; grados 3-4 de movilidad lingual se correlacionan con paladar estrecho en V y paladar blando elongado; la restricción lingual explica el 7.6% de la varianza; sin relación con hioides ni clase de maloclusión | Otra respuesta habla de 200 pacientes (espacio lingual; posición de Freedman no predictiva) | discrepante | PMID 28994495 / DOI 10.1111/ocr.12206 | Existe, 302 sujetos correcto, sin relación con hioides ni clase de Angle (correcto). Pero la revista es Orthod Craniofac Res (no Sleep Medicine) y el título real es 'Ankyloglossia as a risk factor for maxillary hypoplasia and soft palate elongation'. Los grados 3-4 y el 7.6% no aparecen en el resumen. |
| 3 | Zaghi et al. 2020, FAirEST 6 (a veces "Ferris 6") | Journal of Pediatric Dentistry | 6 factores de riesgo de SDB pediátrico (respiración bucal, tensión del mentalis, amígdalas grandes, anquiloglosia, desgaste dental, paladar estrecho); desgaste dental OR 19 | Ampliado a "6 + 4" | discrepante | PMID 34467840 | Pediatr Dent 2021 (no 2020); 96 niños; los seis factores confirmados (P<0.01). El OR 19 del desgaste dental no aparece en el resumen (sí en cita literal de vídeo). |
| 4 | Zaghi, Coppelson et al., ángulo NBC3 y posición de la cabeza en CBCT | Journal of Oral Maxillofacial Surgery | NBC3 (nasion-basion-C3) de 105-110°; 5° de inclinación cambian la vía aérea un 25%; 10° entre 80% y 86% | Año 2021 en una respuesta, 2024 en otras | discrepante | PMID 36841260 / DOI 10.1016/j.joms.2023.01.016 | Coppelson et al., J Oral Maxillofac Surg 2023 (no 2021/2024). +5° → +25% y +10° → +88% confirmados (inclinación hacia arriba); las cifras 80% y 86% de otras respuestas son erróneas. NBC3 basal 112.4°, no 105-110°. 90 sujetos. |
| 5 | Baxter y Zaghi 2020 | (no dice) | 100 casos; cierre del diastema tras liberar el frenillo labial en 6-12 meses | | discrepante | PMID 35283058 / DOI 10.1016/j.ortho.2022.100630 | Baxter, Zaghi, Lashley, Int Orthod 2022 (no 2020); 109 pacientes (no 100); cierre del diastema en 94.7% (dentición primaria) y 92.9% (mixta). |
| 6 | Zaghi et al. 2019/2021, "Functional Ankyloglossia" / protocolo TRMR de 5 dimensiones | (no dice) | Umbrales: punta >50-60% de la apertura, succión palatina (LPS) >30-40% | Año no consistente | no encontrado | PMID 28097623 / DOI 10.1007/s11325-016-1452-7 | No hay un artículo con ese título. Candidato: Yoon 2017 Sleep Breath, validación de escalas de movilidad en 1052 sujetos (PMID 28097623); umbrales no confirmados. |
| 7 | Peterson y Zaghi, estudio "Feres" | (no dice) | 600 pacientes; validación de rangos normales | | discrepante | PMID 33386612 / DOI 10.1111/joor.13144 | Zaghi et al., J Oral Rehabil 2021, TRMR con succión palatina, 611 sujetos (no 600); el nombre 'Feres' no aparece; umbrales 60/40% no en el resumen. |
| 8 | Yoon, Liu, Zaghi 2019, técnica DOME | Sleep | 57 pacientes; mejora de IAH y RDI en 3-6 meses | Otra respuesta cita "Yoon, Liu et al." sobre expansión que reduce amígdalas y adenoides (posiblemente el mismo trabajo) | discrepante | PMID 31606311 / DOI 10.1016/j.sleep.2019.06.002 | Yoon, Guilleminault, Zaghi, Liu, Sleep Med 2020: 75 sujetos (57 eran varones: NotebookLM confundió el dato); AHI 17.65 → 8.17. |
| 9 | Zaghi et al., meta-análisis de avance maxilomandibular (MMA) | (no dice) | 518 pacientes, 45 estudios; mejora 65-80%; pocos alcanzan IAH<5 | Sin año | verificado | PMID 26606321 / DOI 10.1001/jamaoto.2015.2678 | Zaghi et al., JAMA Otolaryngol Head Neck Surg 2016: 45 estudios, 518 pacientes (confirmado). Los porcentajes 65-80% no se comprobaron. |
| 10 | Zaghi et al. 2025/2026, protocolo posoperatorio actualizado | IJOM | Dolor severo baja del 45% al 3.7% | | no encontrado | , | No indexado en PubMed; 2025/2026 y en prensa según el vídeo. |
| 11 | Zaghi et al. 2024, clasificación de frenillos bucales | (no dice) | Variabilidad entre proveedores | | discrepante | PMID 37823364 / DOI 10.1111/joor.13609 | Baxter, Merkel-Walsh, Lahey, Knutsen, Zaghi, J Oral Rehabil 2024; 466 profesionales; primer autor Baxter. |
| 12 | Zaghi y Gahiri 2020, carta de réplica al Consensus Statement | (no dice) | Critica su falta de base clínica funcional | | verificado | PMID 33137275 / DOI 10.1177/0194599820937299 | Ghaheri BA, Tylor DA, Zaghi S, Otolaryngol Head Neck Surg 2020, 'Lacking Consensus'. 'Gahiri' = Ghaheri. |
| 13 | Zaghi et al., cantantes y usuarios de voz profesional | (no dice) | Más claridad vocal, menos fatiga | | no encontrado | , | No se encontró en PubMed. |
| 14 | Zaghi 2018, 350 casos (preliminar del nº 1) | (no dice) | 91% satisfacción | | no encontrado | , | Preliminar sin publicación propia; corresponde al nº 1. |
| 15 | Datos preliminares en diapositiva (5° = 25%) | , | No publicado | | no aplica | , | No publicado. |
| 16 | Capítulo final de un libro de apnea del sueño y ronquido (invitación de Robson Capasso) | libro | Innovaciones | Referencia incompleta | no encontrado | , | Capítulo de libro, no indexado en PubMed. |

## B. Estudios de terceros que Zaghi cita como apoyo
| Referencia | Dato clave / uso | Estado PubMed | PMID / DOI | Nota PubMed |
|---|---|---|---|---|
| Camacho et al. 2015, meta-análisis, *Sleep* | La terapia miofuncional reduce el IAH un 50% en adultos y un 62% en niños | verificado | PMID 25348130 / DOI 10.5665/sleep.4652 | Camacho, Certal, Abdullatif, Zaghi et al., Sleep 2015: AHI −50% adultos y −62% niños (confirmado). Zaghi es coautor. |
| Guilleminault 1976 | Primer reporte de apnea pediátrica | verificado | PMID 934781 | 'Sleep apnea in eight children', Pediatrics 1976 (candidato más probable). |
| Guilleminault 2001 | Define UARS (limitación de flujo + micro-despertares) | verificado | PMID 11768783 / DOI 10.1053/spen.2001.29045 | 'Upper airway resistance syndrome in children: a clinical review', Semin Pediatr Neurol 2001. |
| Guilleminault 2011 / Kim et al. 2011 | Condición "boca semiabierta" (labios cerrados, lengua abajo) inestable; solo lengua arriba da presión negativa estable. La atribución oscila entre Kim y Guilleminault | no encontrado | , | No encontrado. Kim JH 2011 Sleep Breath (PMID 21394611) trata otro tema. |
| Guilleminault et al. 2013 (a veces "Guimino") | 24 niños; 11 que hicieron miofuncional no recayeron, 13 que no, sí a los 2 años | verificado | PMID 23522724 / DOI 10.1016/j.sleep.2013.01.013 | Sleep Med 2013: 24 sujetos, 11 con reeducación sin recaída, 13 sin ella con recaída (AHI 5.3±1.5). No es 'Guimino'. |
| Guilleminault (año no dado) | Respiración bucal >10% del sueño es patológica | no encontrado | , | No se puede buscar sin año ni tema. |
| Villa et al. 2011/2014/2015 | Respiración nasal continua como objetivo final tras amigdalectomía | discrepante | PMID 25934539 / DOI 10.1016/j.sleep.2014.11.019 | Candidato: Villa 2015 Sleep Med (expansión maxilar en OSA infantil). No confirma la afirmación atribuida; los años 2011/2014 no se encontraron. |
| Guimarães et al. 2009 | Ejercicios orofaríngeos reducen apnea moderada | verificado | PMID 19234106 / DOI 10.1164/rccm.200806-981OC | Am J Respir Crit Care Med 2009. |
| Kotlow 1999/2011 | "Lengua libre" <16 mm restrictiva; clases I-IV (validada de 18 meses a 14 años) | verificado | PMID 10635253 | Quintessence Int 1999. El umbral <16 mm no se comprobó en el resumen. |
| Mills (Nicky) 2019/2020 | Disección: frenillo = mucosa + fascia +/- fibras de geniogloso | verificado | PMID 30701608 / DOI 10.1002/ca.23343 | Clin Anat 2019, 'What is a tongue tie? Defining the anatomy of the in-situ lingual frenulum'. Acceso abierto. |
| Moon 2019/2020/2022 | Maniobra de sujetar el piso de la boca; asociación con mordida cruzada posterior | no encontrado | , | No encontrado. |
| Marchesan; Martinelli | Protocolo de inspección; "Teste da Lingua" (Brasil) | verificado | PMID 23367525, PMID 23362754 | Int J Orofacial Myology 2012 (protocolos de frenillo lingual). |
| Andrews (línea G) | La maxila debe llegar a la línea de la glabela | no encontrado | , | No encontrado en PubMed. |
| Harvold | Monos rhesus con la nariz tapada: caras largas, paladares estrechos | verificado | PMID 6939331 / DOI 10.1016/0002-9416(81)90379-1 | Am J Orthod 1981, 'Primate experiments on oral respiration'. |
| Boyd (Kevin) | Cráneos antiguos con paladares anchos | no encontrado | , | No encontrado. |
| Moss (Melvin) | Hipótesis de la matriz funcional (referencia incompleta) | no encontrado | , | No encontrado (hipótesis de la matriz funcional; libro). |
| Mew (John) | Reporte de caso: cara larga tras respiración bucal por alergia a un jerbo | no aplica | , | Caso anecdótico; no indexado. |
| Emerson 1860; Haskin 1912 | Primera expansión palatina rápida; expansión para obstrucción nasal | no encontrado | , | Histórico; no indexado. |
| Sullivan 1981 | Introducción de CPAP tras un estudio animal y 5 pacientes | verificado | PMID 6112294 / DOI 10.1016/s0140-6736(81)92140-1 | Lancet 1981, CPAP nasal. |
| Dickens 1836 (*Pickwick Papers*); serie de 1977 de traqueostomía (15 pacientes) | Historia de la apnea | no aplica | , | Literatura/histórico. |
| Catlin 1870; Rogers 1918; Angle 1907; Straub 1950; Bianchini 1993 | Historia de la respiración nasal y la miofuncional | no aplica | , | Libros/histórico. |
| Vivaer, RCTs de nivel 1 | Mejora duradera hasta 24 meses (referencia incompleta) | no encontrado | , | No se encontró un RCT de Vivaer. Candidato no confirmado: Kang 2024 (PMID 37702187). |
| Tom Myers 2009, *Anatomy Trains* (disección) | Línea Frontal Profunda pies-lengua | no aplica | , | Libro y vídeo de disección. |
| Stecco (atlas de fascia); Travell y Simons; Levin (biotensegridad) | Fascia y dolor referido | no aplica | , | Libros. |
| Lchnowski (2022? / 2025-2026), RCT | Frenuloplastia + miofuncional superior a miofuncional sola. Nombre y año inciertos | discrepante | PMID 39336841 / DOI 10.3390/jcm13185354 | Lichnowska A, Gnatek A, Tyszkiewicz S, Kozakiewicz M, Zaghi S, J Clin Med 2024: RCT con 155 sujetos, terapia miofuncional frente a terapia + frenuloplastia. El nombre real es Lichnowska y el año 2024 (no 2022 ni 2025-2026). Acceso abierto. |
| Estudio reciente sobre EDS/hipermovilidad | 99% dolor crónico, disautonomía peor que lupus o AR (referencia incompleta) | no encontrado | , | No confirmado. Candidato: Daylor 2025 (PMID 40869462), sin comprobar la cifra del 99%. |
| Startup de Stanford | Vídeo para medir despertares sin sensores | no aplica | , | Empresa, no publicación. |
| Sin referencia completa | Roncar el 5% del sueño = UARS (revista donde Zaghi es editor); artículo en *Nature and Science of Sleep* (OMT y CPAP); inmunidad innata amigdalar; ratones y estantes palatinos; Hazelbaker (succión-deglución-respiración) | no aplica | , | Sin datos para buscar. |

## C. Trabajos que Zaghi critica
| Referencia | Crítica | Estado PubMed | PMID / DOI | Nota PubMed |
|---|---|---|---|---|
| Clinical Consensus Statement 2020, AAO-HNS | Encuesta de 12 otorrinos pediátricos; sesgo de confirmación; sin experiencia funcional | verificado | PMID 32283998 / DOI 10.1177/0194599820915457 | Messner AH et al., Otolaryngol Head Neck Surg 2020, 'Clinical Consensus Statement: Ankyloglossia in Children'. |
| Salt et al. 2021 (habla) | Concluye "sin diferencia" cuando los datos muestran puntuaciones más altas en tratados | no encontrado | , | No encontrado con los datos disponibles. |
| Estudio sobre desinformación 2024 | Tres otorrinos: el 89% de los posts de frenillo en Instagram serían "mentiras"; basado en creencias | no encontrado | , | No encontrado. |
| Guías de Stacy Ishman | Cirugía de tejido blando (SMILE) en lugar de expansión; las llama "retrógradas" | verificado | PMID 36757810 / DOI 10.1002/ohn.159 | Ishman SL et al., Otolaryngol Head Neck Surg 2023, Expert Consensus Statement sobre OSA pediátrica persistente. Que recomiende SMILE en lugar de expansión no se comprobó. |
| Artículo de *The Atlantic* 2024 | Sensacionalista sobre la expansión | no aplica | , | Prensa. |
| Tweed 1995 | Extracciones de premolares | no aplica | , | Histórico/libros. |

## D. Referencias éticas e históricas
Informe Belmont 1979; Tuskegee; Talidomida (Kelsey); Willowbrook; grabado de 1679 con una frenotomía.


## E. Añadidas en la segunda sesión (q24, q25, q27)
Todas con referencia incompleta salvo indicación.
| Referencia | Dato | Estado PubMed | PMID / DOI | Nota PubMed |
|---|---|---|---|---|
| Cohorte retrospectiva (2004) | 85% de los niños mejora tras adenoamigdalectomía; 15% con síntomas persistentes | no encontrado | , | Sin autor; no buscable. |
| Revisión retrospectiva (2011), 400 niños de 2-17 años | Niños con SDB tienden a mandíbula pequeña, paladar alto, retrognatismo | no encontrado | , | Sin autor; no buscable. |
| Ensayo aleatorizado (2011) | Cirugía→ortodoncia vs ortodoncia→cirugía: sin diferencia por orden, a menudo se necesitan ambas | no encontrado | , | Sin autor; no buscable. |
| Guía clínica (2014) | Respiración nasal continua como objetivo final en apnea pediátrica | no encontrado | , | Sin autor; no buscable. |
| Zaghi et al., estudio fenotípico | 150 pacientes con apnea; frenillo corto se asocia con paladares más altos | no encontrado | , | No encontrado. |
| Guías nacionales, American Thoracic Society (Coppelson coautor) | Manejo de OSA persistente en niños tras adenoamigdalectomía | verificado | PMID 37890009 / DOI 10.1164/rccm.202310-1857ST | Ehsan Z, Ishman SL, ..., Coppelson K, et al., Am J Respir Crit Care Med 2024, guía oficial de la ATS. Acceso abierto. |
| Estudios sobre UARS (sin autor) | Hasta 29 despertares por hora (dato del clip) | no encontrado | , | Sin autor. |
| Estudios del implante Latera (sin autor) | 2 semanas de congestión; el polímero se reabsorbe y lo reemplaza colágeno en 12-18 meses | discrepante | PMID 32282129 / DOI 10.1002/alr.22543 | Candidato: Kim DH 2020 Int Forum Allergy Rhinol (Latera). No se sabe qué estudios cita Zaghi. |
| Ancho intermolar 38-42 mm (Coppelson cita estudios) | Rango ideal en adultos | no encontrado | , | Sin referencia. |
| Área transversal mínima de la vía aérea | No debería bajar de 150-200 mm² (Coppelson) | no encontrado | , | Sin referencia. |
| Rocabado (vía Valerie Sinkins) | Frenillo labial mandibular y desarrollo óseo (aparecía como "Rockavato") | no encontrado | , | No encontrado. |

**Fila añadida tras PubMed:**

| Referencia | Revista | Dato | Notas | Estado PubMed | PMID / DOI | Nota PubMed |
|---|---|---|---|---|---|---|
| Yoon, Liu et al., expansión palatina y amígdalas/adenoides | Sleep Med | 60 niños; la expansión reduce el volumen de amígdalas y adenoides | Yoon A et al. 2022 (no 2019/2020) | verificado | PMID 35390750 / DOI 10.1016/j.sleep.2022.02.011 | Acceso abierto. |

## F. Verificación con pasaje textual (q26)
Confirmadas con cita literal de la transcripción: Camacho 2015 (50%/62%, 3 vídeos), estudio de 24 niños (11 vs 13), RCT de Lchnowski (Tongue Time 2026 y IJOM), OR 19 del desgaste dental (IC 95% 4.8-77) y 5° = 25% de cambio en la vía aérea. Matices: el cambio para 10° se cita como 80%, 86% u 88% según el vídeo (y 20° = 150%). Los títulos y revistas completos que NotebookLM añade a esos estudios no aparecen en las citas literales y siguen sin verificar.


## G. Añadidas en la sesión 3 (q30-q34)
| Referencia | Dato | Estado PubMed | PMID / DOI | Nota PubMed |
|---|---|---|---|---|
| Estudio de 1995 "en el Journal Pediatrics": CPAP seguro en niños (Zaghi advierte de restricción del crecimiento facial por la mascarilla en estudios posteriores) | CPAP infantil | discrepante | PMID 7608817 | Candidato: Marcus CL et al. 1995, J Pediatr, uso de CPAP nasal en apnea infantil. La revista es J Pediatr, no Pediatrics. Sin confirmar. |
| Estudios sobre aparatos removibles o de alambre ligero (Crozat, DNA) | Expansión de 2-6 mm (media 2.4 mm) | no encontrado | , | Sin autor; no buscable. |
| Cohorte retrospectiva 2004 (repetida en q31b): 15% con síntomas persistentes tras cirugía de amígdalas | | no encontrado | , | Sin autor. |
| Ratificado en q33: meta-análisis MMA de Zaghi (65-80% de mejora) | | verificado | PMID 26606321 | Ver fila del meta-análisis en la sección A. |

## Advertencias
- r13 (estudios de terceros) llegó sin citas ancladas; se verificaron 5 afirmaciones clave con pasaje textual (sección F). El resto no.
- No se han comprobado autores, años ni revistas fuera del notebook.

---

<!-- archivo: expertos/soroush-zaghi/fascia.md -->
# Fascia

Ideas públicas de Soroush Zaghi sobre este tema, reconstruidas a partir de sus vídeos. **No es Zaghi hablando ni una guía clínica.** Cómo leer cada entrada: README. Entradas: 26.

## zag-0234 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, la lengua no es solo un músculo aislado; está conectada al pecho, al diafragma y a las piernas a través del sistema de la fascia.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0235 · Opinión · sin verificar (dicho en vídeo)

Según Zaghi, la lengua es el extremo superior de la "Línea Frontal Profunda" y su restricción puede tensar todo el sistema hasta los pies.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0236 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, al liberar el frenillo lingual, se está liberando el sistema fascial, lo que permite que el diafragma se expanda y los hombros se relajen.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0237 · Opinión · sin verificar (dicho en vídeo)

Según Zaghi, existe una relación entre la restricción de la lengua y la capacidad de extender el dedo gordo del pie, lo que podría usarse como herramienta de cribado.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0238 · Opinión · sin verificar (dicho en vídeo)

Según Zaghi, la compensación fascial en el cuerpo puede comenzar incluso antes del nacimiento, basada en que el feto traga y succiona desde la semana 12.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0239 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, la postura de la cabeza hacia adelante es una compensación funcional para abrir una vía aérea estrecha; el paciente "saca el cuello" para poder respirar.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0240 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, si la lengua está atada hacia adelante, tira de la fascia y obliga a una rotación interna de hombros y una postura encorvada.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0241 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, las asimetrías faciales (un lado de la cara más largo) suelen indicar que el paciente mastica de un solo lado debido a restricciones fasciales o de movilidad lingual, afectando la alineación de la columna.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0242 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, al expandir el paladar, lo primero que suele cambiar no es el tamaño de la vía aérea en el CBCT, sino la postura: el cuello se endereza porque el paciente ya no necesita compensar.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0243 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, quinta dimensión del diagnóstico: palpación de la tensión. Se debe sentir con el dedo si el tejido es fibroso y cuánto tira del piso de la boca.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0244 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, maniobra de "sujeción del piso de la boca" (Floor of Mouth Hold): al presionar el piso de la boca, se revela la verdadera restricción fascial que la lengua intenta ocultar mediante compensación.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0245 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, signo de "hoyuelo" (dimpling): cuando el paciente intenta elevar la lengua bajo resistencia y se forma un hoyuelo en la superficie dorsal, es una prueba directa de restricción fascial.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0246 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, en la cirugía, se debe buscar que la fascia "se separe" del músculo casi por sí sola tras una pequeña incisión si el paciente está bien preparado.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0247 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, el bruxismo y el apretamiento dental suelen ser compensaciones musculares para mantener la mandíbula hacia adelante y evitar el colapso de la vía aérea durante el sueño.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0249 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, la tensión crónica en el cuello y la base del cráneo suele deberse a que los músculos accesorios están trabajando en exceso para ayudar a una lengua restringida a tragar y hablar.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0250 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, la hipermovilidad es la "cuarta pieza del rompecabezas" (junto a lengua, tono y espacio). Afecta al 10-20% de la población.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0251 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, en pacientes con colágeno defectuoso (EDS), la fascia es demasiado laxa. Estos pacientes son más sensibles a las restricciones y pueden desarrollar inestabilidad craneocervical si se les estira demasiado.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0252 · Experiencia clínica · sin verificar (dicho en vídeo)

Zaghi diferencia técnica: "Tono" es el músculo (fuerza), "Hipermovilidad" es la fascia/colágeno (laxitud).

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0253 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, protocolo de "Preservación de Fascia": en pacientes hipermóviles, no se debe realizar una disección profunda en el músculo; solo se libera la mucosa y la fascia superficial para evitar la desestabilización.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0254 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, los pacientes hipermóviles necesitan ejercicios de estabilidad y carga, no de flexibilidad, ya que el estiramiento agresivo los empeora.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0255 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, al realizar el primer corte, sus pies, que estaban rotados hacia afuera, se enderezaron espontáneamente hacia una posición vertical paralela.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0257 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, reportó una realineación completa del lado izquierdo de su cuerpo y una nueva capacidad para sentir y usar su "núcleo" (core) y abdominales al bailar.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0259 · Estudio citado · sin verificar (dicho en vídeo)

Carla Stecco. Autora de un atlas de fascia que demuestra cómo el tejido se extiende por todo el cuerpo.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0260 · Estudio citado · sin verificar (dicho en vídeo)

Janet Travell y David Simons. Autores de los manuales de puntos gatillo; Zaghi cita su observación de patrones de dolor referido para explicar por qué la lengua causa dolor en los hombros.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0261 · Estudio citado · sin verificar (dicho en vídeo)

Andrews et al. Línea "G" o Andrews para determinar que el maxilar debe alinearse con la glabela para una postura óptima.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0618 · Opinión · sin verificar (dicho en vídeo)

Zaghi explica que la fascia forma una red continua, la línea frontal profunda, que va de la lengua al diafragma, las caderas y los pies (anatomía de Tom Myers), y por eso liberar la lengua puede tener efecto sobre la postura global; es una hipótesis apoyada en disecciones de Myers y en relatos de pacientes.

- Vídeo: [Full Lecture: Evaluation, Diagnosis, and Treatment of Tongue, Lip, & Buccal Ties, Dr. Soroush Zaghi](https://www.youtube.com/watch?v=iP3c-C9L9b0), minuto `PENDIENTE DE VERIFICAR`.
- Cita corta (transcripción automática, puede tener errores): «Fashio covers all the muscles in the body and there are actually facial networks that extend from the head and in fact the tongue all the way down to the toes and this is the deep front line and the […]»

---

<!-- archivo: expertos/soroush-zaghi/frameworks.md -->
# Marcos de razonamiento

Ideas públicas de Soroush Zaghi sobre este tema, reconstruidas a partir de sus vídeos. **No es Zaghi hablando ni una guía clínica.** Cómo leer cada entrada: README. Entradas: 20.

## zag-0421 · Estudio citado · sin verificar (dicho en vídeo)

Kotlow (1999/2011) para Dimensión 1; Zaghi et al. (2021) para el protocolo completo.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.
- Estudio: PMID [10635253](https://pubmed.ncbi.nlm.nih.gov/10635253/), ficha 1999-kotlow-clasificacion.md.

## zag-0422 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, los pediatras suelen conocer solo una dimensión; TBI utiliza las cinco para evitar falsos negativos.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0423 · Estudio citado · sin verificar (dicho en vídeo)

Zaghi et al. (2020), Journal of Pediatric Dentistry. El desgaste dental tiene un Odds Ratio de 19 para SDB.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0424 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, la posición de Freedman se eliminará del protocolo próximamente por falta de predictibilidad.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0425 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, una puntuación de 7-8 es considerada buena; <5 indica necesidad de intervenciones como Kenalog.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0426 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, liberar la lengua en un paladar muy estrecho puede empeorar la apnea al empujar la masa lingual hacia la garganta.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0427 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, la hipermovilidad afecta al 10-20% de la población y requiere protocolos de estabilidad en lugar de estiramientos.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0428 · Estudio citado · sin verificar (dicho en vídeo)

Zaghi, Coppelson et al. (2024), Journal of Oral Maxillofacial Surgery. Un cambio de 5° en la cabeza altera la medida de la vía aérea en un 25%.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0429 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, rango ideal: 105°-110°. Si es >120°, el paciente está compensando severamente.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0430 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, muchos pacientes son "falsos negativos" en apnea pero sufren fatiga crónica por UARS.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0431 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, la técnica de conservación de fascia (Fascia Preserving Technique) ha reducido el dolor posoperatorio severo del 45% al 3.7%.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0432 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, es físicamente imposible respirar por la boca si la lengua está en posición de succión palatina completa.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0433 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, el marco de los «68 tonos de gris» se usa para defender el tratamiento en áreas con «preponderancia de evidencia» aunque falten ensayos aleatorizados de nivel 1.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0434 · Experiencia clínica · sin verificar (dicho en vídeo)

Zaghi lo usa para criticar diagnósticos por email o sin examen funcional.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0435 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, si no se trata la obstrucción nasal (capa externa), la terapia de lengua fallará.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0436 · Opinión · sin verificar (dicho en vídeo)

Zaghi sitúa el estado actual de la frenuloplastia funcional entre la oposición violenta y la aceptación.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0437 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, la privación de sueño afecta estas cuatro dimensiones impidiendo el Highest Potential del individuo.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0438 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, es el paso previo obligatorio a cualquier cirugía de lengua.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0439 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, para intervenciones de bajo riesgo, la "preponderancia de evidencia" es suficiente.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0440 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, ayuda a los estudiantes a no olvidar que el frenillo es solo una causa.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

---

<!-- archivo: expertos/soroush-zaghi/frenuloplastia.md -->
# Frenuloplastia: técnica quirúrgica

Ideas públicas de Soroush Zaghi sobre este tema, reconstruidas a partir de sus vídeos. **No es Zaghi hablando ni una guía clínica.** Cómo leer cada entrada: README. Entradas: 45.

## zag-0006 · Estudio citado · verificado en PubMed

El ensayo aleatorizado de Anna Lichnowska y colaboradores (J Clin Med 2024, 155 sujetos, con Zaghi como coautor) comparó terapia miofuncional sola con terapia miofuncional más frenuloplastia lingual y encontró que la cirugía mejoró más la movilidad de la lengua y funciones como la deglución, la respiración y la postura de reposo; Zaghi lo presenta como el primer ensayo aleatorizado sobre frenuloplastia con terapia miofuncional.

- Vídeo: [Dr. Soroush Zaghi at Tongue Time 2026 in Zurich, Switzerland  (Full Lecture)](https://www.youtube.com/watch?v=y6VkQnMBBvc), minuto `PENDIENTE DE VERIFICAR`.
- Vídeo: [The 50th Anniversary of the IJOM: Paradigm Shifts in Orofacial Myology and Myofunctional Therapy](https://www.youtube.com/watch?v=Z8diyvDv0ag), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2026.
- Estudio: PMID [39336841](https://pubmed.ncbi.nlm.nih.gov/39336841/), ficha 2024-lichnowska-ensayo-frenuloplastia.md.
- Cita corta (transcripción automática, puede tener errores): «she did a randomized control trial looking at exactly that She compared myofunctional therapy alone to myofunctional therapy with tongue tie release»

## zag-0007 · Estudio citado · discrepante con el estudio (ver discrepancias.md)

Zaghi afirma en 2026 que el ensayo aleatorizado de Lichnowska muestra efecto de la frenuloplastia también en el sueño y en la retención ortodóntica; el artículo publicado no mide sueño ni retención ortodóntica, solo movilidad y funciones orales (discrepancia con el estudio).

- Vídeo: [Dr. Soroush Zaghi at Tongue Time 2026 in Zurich, Switzerland  (Full Lecture)](https://www.youtube.com/watch?v=y6VkQnMBBvc), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2026.
- Estudio: PMID [39336841](https://pubmed.ncbi.nlm.nih.gov/39336841/), ficha 2024-lichnowska-ensayo-frenuloplastia.md.
- Cita corta (transcripción automática, puede tener errores): «the first ever known randomized control trial on lingual frenuloplasty with myofunctional therapy demonstrating the immense effect effects it has not only on chewing swallowing tongue posture but also sleep breathing and orthodontic retention outcomes»

## zag-0009 · Estudio citado · verificado en PubMed

El estudio de Baxter, Zaghi y Lashley (Int Orthod 2022, 109 niños; Zaghi habla de «un centenar») mostró que la frenectomía labial superior con láser en niños no impide el cierre del diastema: se redujo en el 94.7% de los de dentición primaria y en el 92.9% de los de dentición mixta.

- Vídeo: [Dr. Zaghi -TBI - AAPMD: Ethical Principles in the Practice of Scientific Research and Public Policy](https://www.youtube.com/watch?v=wDuCMJxtjzE), minuto `PENDIENTE DE VERIFICAR`.
- Estudio: PMID [35283058](https://pubmed.ncbi.nlm.nih.gov/35283058/), ficha 2022-baxter-frenillo-labial.md.
- Cita corta (transcripción automática, puede tener errores): «we've done the study with dr richard baxter where they took a hundred kids they took a picture of the diastema snipped the frenum and then took another picture six months to a year later and they saw that it […]»

## zag-0046 · Estudio citado · verificado en PubMed

Zaghi et al. (2019), "Lingual frenuloplasty with myofunctional therapy", Laryngoscope Investigative Otolaryngology. Serie de 348 casos que validó el éxito del protocolo con un 91% de satisfacción, pero reportó un 12.6% de sangrado con la técnica antigua de tijeras.

- Vídeo: [Long-term Implications of Untreated Tongue-Tie (Dr. Soroush Zaghi, The Breathe Institute)](https://www.youtube.com/watch?v=cuT6qrm5IT0), minuto `PENDIENTE DE VERIFICAR`.
- Vídeo: [Myofunctional Therapy and Frenuloplasty Can Be Appropriate Treatments for Obstructive Sleep Apnea](https://www.youtube.com/watch?v=dlU8wxa8474), minuto `PENDIENTE DE VERIFICAR`.
- Vídeo: [Frenums, Fascia and Physiology by Dr. Soroush Zaghi & Sanda Valcu-Pinkerton, COM - at AAPMD 2019](https://www.youtube.com/watch?v=BM3TmSXhUIw), minuto `PENDIENTE DE VERIFICAR`.
- Estudio: PMID [31637291](https://pubmed.ncbi.nlm.nih.gov/31637291/), ficha 2019-zaghi-frenuloplastia-348.md.

## zag-0054 · Experiencia clínica · sin verificar (dicho en vídeo)

Zaghi diferencia entre Frenotomía (incisión simple), Frenectomía (extirpación de tejido) y Frenuloplastia (reparación de la mucosa con suturas para lograr cierre por primera intención).

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0055 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, la "Frenuloplastia Funcional" no es solo el corte, sino un protocolo que integra terapia miofuncional pre y postoperatoria para maximizar resultados.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0056 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, el concepto "Fascia Preserving Technique" (técnica de preservación de fascia) busca liberar solo las fibras restrictivas superficiales y evitar la violación de la fascia profunda que provee estabilidad.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0057 · Opinión · sin verificar (dicho en vídeo)

Según Zaghi, el dilema de "La Correa y la Jaula" (The Leash and the Cage): La lengua es el perro, el frenillo es la correa y el paladar estrecho es la jaula. No sirve de nada quitar la correa si el perro sigue encerrado en la jaula.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0058 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, la anestesia de la frenuloplastia empieza con anestesia tópica, seguida de una inyección local de lidocaína con epinefrina para vasoconstricción. Las dosis y concentraciones no se recogen en esta base.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0059 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, uso de Citanest (prilocaína) sin epinefrina por tener un pH más alto (6-7), lo que reduce el ardor al inyectar en comparación con soluciones ácidas con epinefrina.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0060 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, inyección directa en el músculo geniogloso con Marcaine (bupivacaína) al finalizar el procedimiento para proporcionar confort postoperatorio prolongado.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0061 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, maniobra de "Push Back" (empujar hacia atrás) o uso de un director de ranura para tensar el frenillo y visualizar los límites de la mucosa.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0062 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, marcado o pinzamiento con hemostato de la mucosa distal y proximal para delinear el sitio de incisión y controlar el sangrado preventivamente.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0063 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, incisión inicial a través de la mucosa, usualmente 1-2 mm por encima de las carúnculas sublinguales.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0064 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, disección por capas (Mucosa -> Fascia superficial -> Músculo si es necesario).

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0065 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, identificación y liberación del tabique lingual medio (Median Lingual Septum).

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0066 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, punto final funcional: La liberación termina cuando el paciente puede lograr una succión palatina completa (LPS) o cuando el geniogloso se ve plano y sin tensión al tacto.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0067 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, técnica de "Butterfly Hold" (agarre de mariposa): Presionar las venas linguales laterales con los dedos para crear un campo quirúrgico casi exangüe.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0068 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, si hay sangrado arterial/venoso, aplicar presión directa constante; si no cede, realizar una sutura en figura de ocho alrededor del vaso (no a través de él).

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0069 · Experiencia clínica · sin verificar (dicho en vídeo)

Uso de láser de CO2 (LightScalpel) con pieza de mano Zaghi que tiene un tope trasero (backstop) para mayor control y evitar ablación excesiva.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0070 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, tijeras de precisión (JEMM set) para disección roma y mayor sensibilidad táctil de las fibras restrictivas.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0071 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, suturas reabsorbibles (Vicryl o Chromic Gut 4-0) para cierre por primera intención.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0072 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, pegamento PeriAcryl (cianoacrilato): Aplicado en gotas pequeñas entre las suturas para mayor estabilidad de la herida sin introducir inflamación adicional.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0073 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, en la frenuloplastia evita el láser de diodo y el cauterio en tejidos profundos o en el músculo debido al daño térmico excesivo que provoca mayor inflamación, dolor y fibrosis postoperatoria.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0074 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, en la frenuloplastia evita las suturas de PTFE porque, aunque son menos inflamatorias, actúan como una "guillotina" que corta el tejido bajo tensión.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0075 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, en la frenuloplastia evita la disección agresiva hacia arriba en el músculo; en su lugar apunta el láser/tijera hacia abajo hacia el piso de la boca para que el músculo se libere y se retraiga naturalmente.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0076 · Experiencia clínica · sin verificar (dicho en vídeo)

Zaghi enfatiza la regla de "mirar antes de cortar". Si ocurre sangrado, el primer paso es mantener la calma, aplicar una gasa y ejercer presión firme directamente sobre la fuente, no en cualquier lugar.

- Vídeo: [Dr. Soroush Zaghi at ALSC - Breathe and Thrive 2022, in Las Vegas, NV](https://www.youtube.com/watch?v=3fq6w2buIy0), minuto `PENDIENTE DE VERIFICAR`.
- Vídeo: [Grade 4 Tongue-Tie - Bleeding Management, PeriAcryl Glue, Sutures, Functional Frenuloplasty - TBI](https://www.youtube.com/watch?v=SQRk2zUQdvE), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2022.

## zag-0077 · Experiencia clínica · sin verificar (dicho en vídeo)

Zaghi utiliza la maniobra "Butterfly Hold" (sujeción de mariposa) para comprimir las venas linguales con los dedos durante la disección, lo que permite un campo operatorio casi sin sangre.

- Vídeo: [Dr. Soroush Zaghi at ALSC - Breathe and Thrive 2022, in Las Vegas, NV](https://www.youtube.com/watch?v=3fq6w2buIy0), minuto `PENDIENTE DE VERIFICAR`.
- Vídeo: [Functional Frenuloplasty with Lightscalpel's Zaghi Handpiece at TBI (Full Procedure)](https://www.youtube.com/watch?v=j1aiuEtXRgQ), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2022.

## zag-0078 · Experiencia clínica · sin verificar (dicho en vídeo)

Zaghi emplea pinzas hemostáticas para pinzar el tejido antes de realizar la frenotomía inicial, lo que ayuda a obliterar pequeños capilares.

- Vídeo: [Grade 4 Tongue-Tie - Bleeding Management, PeriAcryl Glue, Sutures, Functional Frenuloplasty - TBI](https://www.youtube.com/watch?v=SQRk2zUQdvE), minuto `PENDIENTE DE VERIFICAR`.

## zag-0079 · Experiencia clínica · sin verificar (dicho en vídeo)

Si una vena lingual es perforada accidentalmente con la aguja de sutura, Zaghi indica retirar el hilo de inmediato y presionar; advierte que intentar anudar el vaso directamente suele desgarrarlo más.

- Vídeo: [Dr. Soroush Zaghi at ALSC - Breathe and Thrive 2022, in Las Vegas, NV](https://www.youtube.com/watch?v=3fq6w2buIy0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2022.

## zag-0080 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, como recurso extremo ante una hemorragia arterial incontrolable (que nunca ha tenido en esta cirugía pero conoce por cirugía de cuello), Zaghi describe el "Plan Z": trasladar al paciente a un hospital para realizar una embolización por Radiología Intervencionista introduciendo un catéter desde la arteria femoral.

- Vídeo: [Dr. Soroush Zaghi at ALSC - Breathe and Thrive 2022, in Las Vegas, NV](https://www.youtube.com/watch?v=3fq6w2buIy0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2022.

## zag-0081 · Experiencia clínica · sin verificar (dicho en vídeo)

Zaghi aboga firmemente por el cierre con suturas para lograr una cicatrización por primera intención, reduciendo el tamaño de la herida y, por ende, el de la cicatriz posterior.

- Vídeo: [Functional Approach to Frenuloplasty: How We Do It - Dr. Soroush Zaghi](https://www.youtube.com/watch?v=C0kel5PNc7c), minuto `PENDIENTE DE VERIFICAR`.
- Vídeo: [Evolution Of Myofunctional Therapy, Lingual Frenuloplasty - Dr. Soroush Zaghi at ALSC 2026.](https://www.youtube.com/watch?v=nlFVT6PUaYc), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2026.

## zag-0082 · Experiencia clínica · sin verificar (dicho en vídeo)

Zaghi utiliza suturas de tri-cromo o cromo simple (4-0 chromic gut) porque son absorbibles, aunque reconoce que son pro-inflamatorias.

- Vídeo: [Dr. Soroush Zaghi at ALSC - Breathe and Thrive 2022, in Las Vegas, NV](https://www.youtube.com/watch?v=3fq6w2buIy0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2022.

## zag-0083 · Experiencia clínica · sin verificar (dicho en vídeo)

RECHAZO: Zaghi ha dejado de usar suturas de PTFE. Aunque son inertes, actúan como una "guillotina" que desgarra la delicada mucosa lingual cuando el paciente mueve la lengua durante los ejercicios.

- Vídeo: [Updates from Dr. Soroush Zaghi - The Breathe Institute at ALSC Symposium 2024](https://www.youtube.com/watch?v=iGQlzOtT4C0), minuto `PENDIENTE DE VERIFICAR`.
- Vídeo: [Dr. Soroush Zaghi at ALSC - Breathe and Thrive 2022, in Las Vegas, NV](https://www.youtube.com/watch?v=3fq6w2buIy0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2022.

## zag-0084 · Experiencia clínica · sin verificar (dicho en vídeo)

Zaghi aplica pegamento PeriAcryl (cianoacrilato) entre los puntos de sutura para dar fuerza adicional y evitar la dehiscencia de la herida sin necesidad de poner demasiados puntos.

- Vídeo: [Updates from Dr. Soroush Zaghi - The Breathe Institute at ALSC Symposium 2024](https://www.youtube.com/watch?v=iGQlzOtT4C0), minuto `PENDIENTE DE VERIFICAR`.
- Vídeo: [Grade 4 Tongue-Tie - Bleeding Management, PeriAcryl Glue, Sutures, Functional Frenuloplasty - TBI](https://www.youtube.com/watch?v=SQRk2zUQdvE), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2024.

## zag-0085 · Experiencia clínica · sin verificar (dicho en vídeo)

Zaghi emplea la "sutura de colchonero horizontal" (horizontal mattress) en áreas de alta tensión para evitar que el hilo corte el tejido, y la sutura en "figura de ocho" para anclar bases sangrantes.

- Vídeo: [Dr. Soroush Zaghi at ALSC - Breathe and Thrive 2022, in Las Vegas, NV](https://www.youtube.com/watch?v=3fq6w2buIy0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2022.

## zag-0086 · Experiencia clínica · sin verificar (dicho en vídeo)

En bebés, Zaghi generalmente no pone suturas debido a la dificultad técnica del acceso y el riesgo; el enfoque es una liberación funcional rápida y segura.

- Vídeo: [Evolution Of Myofunctional Therapy, Lingual Frenuloplasty - Dr. Soroush Zaghi at ALSC 2026.](https://www.youtube.com/watch?v=nlFVT6PUaYc), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2026.

## zag-0088 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, en adultos, observa que la fascia suele estar más atrapada dentro del músculo debido a décadas de compensación, lo que puede requerir una técnica más refinada para separar las fibras sin causar daño masivo.

- Vídeo: [Dr. Soroush Zaghi at ALSC - Breathe and Thrive 2022, in Las Vegas, NV](https://www.youtube.com/watch?v=3fq6w2buIy0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2022.

## zag-0089 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, en la frenuloplastia es muy prudente con la cantidad de anestesia local en menores de 5 años y rara vez necesita mucha en adultos. Las dosis y concentraciones no se recogen en esta base.

- Vídeo: [Dr. Soroush Zaghi at ALSC - Breathe and Thrive 2022, in Las Vegas, NV](https://www.youtube.com/watch?v=3fq6w2buIy0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2022.

## zag-0090 · Experiencia clínica · sin verificar (dicho en vídeo)

El "punto final" de la cirugía se decide funcionalmente: Zaghi se detiene cuando, al realizar la maniobra de "Floor of Mouth Hold", la lengua puede elevarse hasta la papila incisiva de forma independiente, sin que el suelo de la boca suba con ella.

- Vídeo: [Evolution Of Myofunctional Therapy, Lingual Frenuloplasty - Dr. Soroush Zaghi at ALSC 2026.](https://www.youtube.com/watch?v=nlFVT6PUaYc), minuto `PENDIENTE DE VERIFICAR`.
- Vídeo: [Grade 4 Tongue-Tie - Bleeding Management, PeriAcryl Glue, Sutures, Functional Frenuloplasty - TBI](https://www.youtube.com/watch?v=SQRk2zUQdvE), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2026.

## zag-0091 · Experiencia clínica · sin verificar (dicho en vídeo)

En términos anatómicos, Zaghi libera hasta que las fibras del músculo geniogloso se ven planas y suaves con respecto a la superficie ventral de la lengua; si el músculo protruye hacia afuera, es un signo de que todavía hay tensión restrictiva o riesgo de mala cicatrización.

- Vídeo: [Dr. Soroush Zaghi at ALSC - Breathe and Thrive 2022, in Las Vegas, NV](https://www.youtube.com/watch?v=3fq6w2buIy0), minuto `PENDIENTE DE VERIFICAR`.
- Vídeo: [Grade 4 Tongue-Tie - Bleeding Management, PeriAcryl Glue, Sutures, Functional Frenuloplasty - TBI](https://www.youtube.com/watch?v=SQRk2zUQdvE), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2022.

## zag-0092 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, en casos de Grado 4 (atados a la punta), aplica liberaciones por etapas (staged releases): primero libera solo mucosa y fascia superficial, espera meses a que el paciente gane espacio y tono, y luego hace una segunda etapa profunda si persiste la restricción.

- Vídeo: [Functional Approach to Frenuloplasty: How We Do It - Dr. Soroush Zaghi](https://www.youtube.com/watch?v=C0kel5PNc7c), minuto `PENDIENTE DE VERIFICAR`.
- Vídeo: [Updates from Dr. Soroush Zaghi - The Breathe Institute at ALSC Symposium 2024](https://www.youtube.com/watch?v=iGQlzOtT4C0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2024.

## zag-0093 · Estudio citado · sin verificar (dicho en vídeo)

Zaghi et al. (2025/2026), IJOM (en prensa). Nueva serie de casos que muestra que la técnica refinada (láser CO2 y preservación de fascia) redujo el dolor severo del 45% al 3.7% y el sangrado a niveles casi nulos.

- Vídeo: [Evolution Of Myofunctional Therapy, Lingual Frenuloplasty - Dr. Soroush Zaghi at ALSC 2026.](https://www.youtube.com/watch?v=nlFVT6PUaYc), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2026.

## zag-0094 · Estudio citado · verificado en PubMed

Nicky Mills. Artículo anatómico que demuestra que el frenillo no es una banda discreta sino un velo de tejido complejo que incluye mucosa, fascia y fibras musculares.

- Vídeo: [Evolution Of Myofunctional Therapy, Lingual Frenuloplasty - Dr. Soroush Zaghi at ALSC 2026.](https://www.youtube.com/watch?v=nlFVT6PUaYc), minuto `PENDIENTE DE VERIFICAR`.
- Vídeo: [Functional Approach to Frenuloplasty: How We Do It - Dr. Soroush Zaghi](https://www.youtube.com/watch?v=C0kel5PNc7c), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2026.
- Estudio: PMID [30701608](https://pubmed.ncbi.nlm.nih.gov/30701608/).

## zag-0619 · Experiencia clínica · sin verificar (dicho en vídeo)

Zaghi pasó de usar solo bisturí y tijeras grandes a usar tijeras o láser, con preferencia por el láser para el músculo; dice que su tasa de sangrado bajó del 12% a casi 0.

- Vídeo: [Dr. Soroush Zaghi at ALSC - Breathe and Thrive 2022, in Las Vegas, NV](https://www.youtube.com/watch?v=3fq6w2buIy0), minuto 31:16 (localizado en los subtítulos automáticos).
- Año de la charla: 2022.
- Cita corta (transcripción automática, puede tener errores): «I used to use only scissors okay... I used to use scalpel... then I did huge scissors... now I do scissors or laser. My preference for the muscle is definitely laser... my bleeding rate used to be 12% now it's […]»

---

<!-- archivo: expertos/soroush-zaghi/fuentes-videos.md -->
# Vídeos de los que salen las afirmaciones

Vídeos públicos de YouTube de Soroush Zaghi y The Breathe Institute citados en esta carpeta. Aquí solo están el título y el enlace: ni transcripciones ni copias de los vídeos. Los derechos son de sus autores.

La extracción partió de un cuaderno de NotebookLM con 100 fuentes de The Breathe Institute (99 vídeos y su web). Se han quitado de esta lista y de las afirmaciones los testimonios y casos de pacientes, los vídeos de rutinas personales del equipo y los tutoriales de gestión.

| Vídeo | Enlace |
|---|---|
| "Do I Have A Tongue-Tie?" - 5 dimensions of tongue-tie assessment, Dr. Zaghi - The Breathe Course | https://www.youtube.com/watch?v=8dOq11N-qK8 |
| Advances in Surgical Technique with Dr. Kevin Coppelson - BreatheMAX - 10/28/24 | https://www.youtube.com/watch?v=gsAggiqvgEY |
| Breathe Myo Explained: Tongue Tie, Airway Health, Facial Development with Sandraluz Gonzalez | https://www.youtube.com/watch?v=ni2dO45jdbo |
| Can you grow out of large tonsils? Dr. Zaghi at The Breathe Institute discusses... | https://www.youtube.com/watch?v=iKMZzTYnTro |
| CBCT Protocol With The Breathe Institute For Proper Airway Measurements | https://www.youtube.com/watch?v=tn6o08wn5j0 |
| Dr. Soroush Zaghi at AACP 2018 - Tongue-tie and Myofascial Disfunction | https://www.youtube.com/watch?v=OdgYVx9FNCc |
| Dr. Soroush Zaghi at ALSC - Breathe and Thrive 2022, in Las Vegas, NV | https://www.youtube.com/watch?v=3fq6w2buIy0 |
| Dr. Soroush Zaghi at Tongue Time 2026 in Zurich, Switzerland  (Full Lecture) | https://www.youtube.com/watch?v=y6VkQnMBBvc |
| DR. SOROUSH ZAGHI ON PROTOCOLS DURING THE BREATHE WORKSHOP 2023 | https://www.youtube.com/watch?v=rtbpgAER6GM |
| Dr. Soroush Zaghi on the impact of Tongue-ties on Sleep Disordered Breathing in Kids | https://www.youtube.com/watch?v=tdnmhBv6Zg4 |
| Dr. Zaghi -TBI - AAPMD: Ethical Principles in the Practice of Scientific Research and Public Policy | https://www.youtube.com/watch?v=wDuCMJxtjzE |
| Dr. Zaghi on Research Principles (From TBI's Outlook at AAPMD Collaboration Cures Conference, 2021) | https://www.youtube.com/watch?v=vYQ1mv8Gdf0 |
| Drug Induced Sleep Endoscopy (DISE) - Dr. Soroush Zaghi | https://www.youtube.com/watch?v=Sn9nntkyOoI |
| Evolution Of Myofunctional Therapy, Lingual Frenuloplasty - Dr. Soroush Zaghi at ALSC 2026. | https://www.youtube.com/watch?v=nlFVT6PUaYc |
| Excerpts From - TBI Ambassador Update (December 2024). Now Available On-Demand! | https://www.youtube.com/watch?v=DshE1KHc9s0 |
| FAirEST 6 + 4 | https://www.youtube.com/watch?v=ckwLiTMb7wo |
| Frenums, Fascia and Physiology by Dr. Soroush Zaghi & Sanda Valcu-Pinkerton, COM - at AAPMD 2019 | https://www.youtube.com/watch?v=BM3TmSXhUIw |
| Full Lecture: Evaluation, Diagnosis, and Treatment of Tongue, Lip, & Buccal Ties, Dr. Soroush Zaghi | https://www.youtube.com/watch?v=iP3c-C9L9b0 |
| Functional Approach to Frenuloplasty: How We Do It - Dr. Soroush Zaghi | https://www.youtube.com/watch?v=C0kel5PNc7c |
| Functional Approach to Sleep and Breathing + Frenuloplasty Course (AUSTRALIA APRIL 2019) | https://www.youtube.com/watch?v=S-xjr-6ade4 |
| Functional Frenuloplasty Post Operative Instructions with Amanda at The Breathe Institute | https://www.youtube.com/watch?v=uQYOd_jWRv8 |
| Functional Frenuloplasty with Lightscalpel's Zaghi Handpiece at TBI (Full Procedure) | https://www.youtube.com/watch?v=j1aiuEtXRgQ |
| Grade 4 Tongue-Tie - Bleeding Management, PeriAcryl Glue, Sutures, Functional Frenuloplasty - TBI | https://www.youtube.com/watch?v=SQRk2zUQdvE |
| Grade 4 Tonsils with Dr. Soroush Zaghi at The Breathe Institute + Pre and Post airway CBCT | https://www.youtube.com/watch?v=KyTUkhJhG9w |
| Intake Nasal Dilator Strips - at The Breathe Institute | https://www.youtube.com/watch?v=PmTDWNRh96w |
| Introducing the Breathe Oral Habits Program - with Carla Lejarraga and Anna Gross | https://www.youtube.com/watch?v=kPzCm3RgVVc |
| Live Latera Nasal Valve Implant Procedure for Nasal Obstruction with Dr. Zaghi and 1 week Followup | https://www.youtube.com/watch?v=Cm7chrBRz14 |
| Long-term Implications of Untreated Tongue-Tie (Dr. Soroush Zaghi, The Breathe Institute) | https://www.youtube.com/watch?v=cuT6qrm5IT0 |
| Meet Dr. Zaghi of The Breathe Institute | https://www.youtube.com/watch?v=Ng_EJ1yOKkw |
| Myofunctional Therapy and Frenuloplasty Can Be Appropriate Treatments for Obstructive Sleep Apnea | https://www.youtube.com/watch?v=dlU8wxa8474 |
| Pediatric and Adult Sleep Medicine - Key Takeaways with Dr. Soroush Zaghi | https://www.youtube.com/watch?v=J0jS05tFj1w |
| Pediatric Sleep Disordered Breathing and Maxillofacial Development with Soroush Zaghi | https://www.youtube.com/watch?v=eA1Yqbruw4g |
| Perfect Your Swallow Technique with Dr. Soroush Zaghi at The Breathe Institute | https://www.youtube.com/watch?v=GJ4vm-4ZSyQ |
| Post-Op Wound Healing - Sanda Valcu-Pinkerton, The Breathe Institute | https://www.youtube.com/watch?v=puF6uKS8tTA |
| Serrapeptase Protocol for addressing  pain and inflammation - with Dr. Soroush Zaghi at TBI | https://www.youtube.com/watch?v=jvAdRMXr3XE |
| The 50th Anniversary of the IJOM: Paradigm Shifts in Orofacial Myology and Myofunctional Therapy | https://www.youtube.com/watch?v=Z8diyvDv0ag |
| Tongue-Tie, Sleep, Breathing, and Myofunctional Therapy: New Research Updates. Dr. Zaghi at ALSC '20 | https://www.youtube.com/watch?v=G9GrUw7YJD0 |
| Tonsils Size vs Color - Differences between acute and chronic tonsil hypertrophy (large tonsils) | https://www.youtube.com/watch?v=lfH43CDyG5I |
| Updates from Dr. Soroush Zaghi - The Breathe Institute at ALSC Symposium 2024 | https://www.youtube.com/watch?v=iGQlzOtT4C0 |

---

<!-- archivo: expertos/soroush-zaghi/hipermovilidad.md -->
# Hipermovilidad

Ideas públicas de Soroush Zaghi sobre este tema, reconstruidas a partir de sus vídeos. **No es Zaghi hablando ni una guía clínica.** Cómo leer cada entrada: README. Entradas: 18.

## zag-0262 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, la hipermovilidad es la "cuarta pieza del rompecabezas" o "cuarta variable" para el éxito clínico, sumándose a la evaluación de la lengua (frenillo), el tono muscular y el espacio maxilar.

- Vídeo: [Evolution Of Myofunctional Therapy, Lingual Frenuloplasty - Dr. Soroush Zaghi at ALSC 2026.](https://www.youtube.com/watch?v=nlFVT6PUaYc), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2026.

## zag-0263 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, afecta al 10-20% de la población general, con un 5% de individuos severamente afectados por trastornos del tejido conectivo como el Síndrome de Ehlers-Danlos (EDS).

- Vídeo: [Evolution Of Myofunctional Therapy, Lingual Frenuloplasty - Dr. Soroush Zaghi at ALSC 2026.](https://www.youtube.com/watch?v=nlFVT6PUaYc), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2026.

## zag-0264 · Experiencia clínica · sin verificar (dicho en vídeo)

Zaghi distingue entre "tono", que se refiere a la fuerza y resistencia del músculo, e "hipermovilidad", que se refiere a la laxitud de la fascia y el colágeno que envuelve al músculo.

- Vídeo: [Updates from Dr. Soroush Zaghi - The Breathe Institute at ALSC Symposium 2024](https://www.youtube.com/watch?v=iGQlzOtT4C0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2024.

## zag-0265 · Opinión · sin verificar (dicho en vídeo)

Según Zaghi, a nivel molecular, la hipermovilidad se debe a un colágeno defectuoso que, en lugar de formar una triple hélice fuerte y organizada, presenta una estructura "deshilachada" y desorganizada, lo que reduce la fuerza de tensión del tejido.

- Vídeo: [Evolution Of Myofunctional Therapy, Lingual Frenuloplasty - Dr. Soroush Zaghi at ALSC 2026.](https://www.youtube.com/watch?v=nlFVT6PUaYc), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2026.

## zag-0266 · Experiencia clínica · sin verificar (dicho en vídeo)

Zaghi utiliza los 9 puntos de la Escala de Beighton para el cribado clínico: 1) hiperextensión de los dedos meñiques más allá de 90°, 2) tocar el antebrazo con el pulgar, 3) hiperextensión de codos, 4) hiperextensión de rodillas, y 5) tocar el suelo con las palmas de las manos sin doblar las rodillas (un punto por cada lado y uno por la espalda).

- Vídeo: [Updates from Dr. Soroush Zaghi - The Breathe Institute at ALSC Symposium 2024](https://www.youtube.com/watch?v=iGQlzOtT4C0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2024.

## zag-0267 · Experiencia clínica · sin verificar (dicho en vídeo)

Zaghi considera que un puntaje alto (ej. 9/9) es una señal de alerta roja que obliga a modificar drásticamente el enfoque quirúrgico y terapéutico.

- Vídeo: [Evolution Of Myofunctional Therapy, Lingual Frenuloplasty - Dr. Soroush Zaghi at ALSC 2026.](https://www.youtube.com/watch?v=nlFVT6PUaYc), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2026.

## zag-0268 · Estudio citado · sin verificar (dicho en vídeo)

Zaghi cita un estudio reciente sobre calidad de vida en mujeres con hipermovilidad/EDS que muestra que el 99% experimenta dolor crónico y disautonomía más severa que pacientes con lupus o artritis reumatoide.

- Vídeo: [Evolution Of Myofunctional Therapy, Lingual Frenuloplasty - Dr. Soroush Zaghi at ALSC 2026.](https://www.youtube.com/watch?v=nlFVT6PUaYc), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2026.

## zag-0269 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, los pacientes hipermóviles suelen presentar síntomas de disautonomía como mareos, hipotensión ortostática (POTS), intolerancia a la temperatura (sentir mucho frío), fatiga crónica, migrañas y problemas gastrointestinales (reflujo o colon irritable).

- Vídeo: [Evolution Of Myofunctional Therapy, Lingual Frenuloplasty - Dr. Soroush Zaghi at ALSC 2026.](https://www.youtube.com/watch?v=nlFVT6PUaYc), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2026.

## zag-0270 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, existe un riesgo crítico de Inestabilidad Craneocervical (CCI) en estos pacientes; durante cirugías como la amigdalectomía, la extensión forzada del cuello hacia atrás puede lesionar permanentemente los ligamentos laxos de la columna cervical.

- Vídeo: [Evolution Of Myofunctional Therapy, Lingual Frenuloplasty - Dr. Soroush Zaghi at ALSC 2026.](https://www.youtube.com/watch?v=nlFVT6PUaYc), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2026.

## zag-0271 · Experiencia clínica · sin verificar (dicho en vídeo)

Zaghi observa una asociación con el Síndrome de Activación de Mastocitos (MCAS), que causa reacciones alérgicas severas e inexplicables que afectan el bienestar general del paciente.

- Vídeo: [Evolution Of Myofunctional Therapy, Lingual Frenuloplasty - Dr. Soroush Zaghi at ALSC 2026.](https://www.youtube.com/watch?v=nlFVT6PUaYc), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2026.

## zag-0272 · Experiencia clínica · sin verificar (dicho en vídeo)

En pacientes hipermóviles, Zaghi aplica la "Técnica de Preservación de Fascia", limitando la liberación a la mucosa y la fascia superficial solamente, evitando entrar en la fascia profunda o el músculo geniogloso.

- Vídeo: [Evolution Of Myofunctional Therapy, Lingual Frenuloplasty - Dr. Soroush Zaghi at ALSC 2026.](https://www.youtube.com/watch?v=nlFVT6PUaYc), minuto `PENDIENTE DE VERIFICAR`.
- Vídeo: [Updates from Dr. Soroush Zaghi - The Breathe Institute at ALSC Symposium 2024](https://www.youtube.com/watch?v=iGQlzOtT4C0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2024.

## zag-0273 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, la razón es que la fascia superficial es para el deslizamiento, mientras que la fascia profunda es para la estabilidad y el soporte de carga; si se libera la fascia profunda en un paciente ya laxo, se puede desestabilizar la vía aérea y empeorar la apnea.

- Vídeo: [Evolution Of Myofunctional Therapy, Lingual Frenuloplasty - Dr. Soroush Zaghi at ALSC 2026.](https://www.youtube.com/watch?v=nlFVT6PUaYc), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2026.

## zag-0274 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, los pacientes con hipermovilidad tienen una cicatrización más frágil y las suturas tienden a caerse o rasgar el tejido prematuramente.

- Vídeo: [Updates from Dr. Soroush Zaghi - The Breathe Institute at ALSC Symposium 2024](https://www.youtube.com/watch?v=iGQlzOtT4C0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2024.

## zag-0275 · Experiencia clínica · sin verificar (dicho en vídeo)

Zaghi advierte que la terapia miofuncional tradicional de "estiramiento, estiramiento, estiramiento" es contraproducente y a menudo empeora a los pacientes hipermóviles al aumentar la inestabilidad.

- Vídeo: [Evolution Of Myofunctional Therapy, Lingual Frenuloplasty - Dr. Soroush Zaghi at ALSC 2026.](https://www.youtube.com/watch?v=nlFVT6PUaYc), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2026.

## zag-0276 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, el protocolo debe enfocarse en la estabilidad, el fortalecimiento y la carga (load-bearing), ayudando al paciente a encontrar "islas de tensión" funcionales para sostener su postura.

- Vídeo: [Evolution Of Myofunctional Therapy, Lingual Frenuloplasty - Dr. Soroush Zaghi at ALSC 2026.](https://www.youtube.com/watch?v=nlFVT6PUaYc), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2026.

## zag-0277 · Experiencia clínica · sin verificar (dicho en vídeo)

Zaghi recomienda derivar a estos pacientes a fisioterapeutas o profesionales del cuerpo que tengan formación específica en EDS para evitar lesiones por manipulación inadecuada.

- Vídeo: [Evolution Of Myofunctional Therapy, Lingual Frenuloplasty - Dr. Soroush Zaghi at ALSC 2026.](https://www.youtube.com/watch?v=nlFVT6PUaYc), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2026.

## zag-0280 · Experiencia clínica · sin verificar (dicho en vídeo)

Zaghi enfatiza que los pacientes hipermóviles necesitan ejercicios que mejoren la estabilidad del "núcleo" (core) y evitar el bloqueo de rodillas al caminar.

- Vídeo: [Evolution Of Myofunctional Therapy, Lingual Frenuloplasty - Dr. Soroush Zaghi at ALSC 2026.](https://www.youtube.com/watch?v=nlFVT6PUaYc), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2026.

## zag-0281 · Opinión · sin verificar (dicho en vídeo)

Según Zaghi, dado que el feto traga y succiona desde la semana 12, las compensaciones fasciales y de movilidad en niños hipermóviles pueden comenzar incluso antes del nacimiento.

- Vídeo: [Frenums, Fascia and Physiology by Dr. Soroush Zaghi & Sanda Valcu-Pinkerton, COM - at AAPMD 2019](https://www.youtube.com/watch?v=BM3TmSXhUIw), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2019.

---

<!-- archivo: expertos/soroush-zaghi/ideas-raras.md -->
# Ideas que aparecen una sola vez

Ideas públicas de Soroush Zaghi sobre este tema, reconstruidas a partir de sus vídeos. **No es Zaghi hablando ni una guía clínica.** Cómo leer cada entrada: README. Entradas: 27.

## zag-0574 · Experiencia clínica · sin verificar (dicho en vídeo)

Zaghi describe un "truco de experto" para pacientes que quieren sentir el alivio inmediato: si se tracciona el frenillo con fuerza antes de cortarlo (como una banda elástica tensa) y se libera de golpe, el paciente experimenta una sensación catártica de liberación que ayuda a que su cuerpo se relaje y facilite el resto de la disección.

- Vídeo: [Dr. Soroush Zaghi at ALSC - Breathe and Thrive 2022, in Las Vegas, NV](https://www.youtube.com/watch?v=3fq6w2buIy0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2022.

## zag-0575 · Experiencia clínica · sin verificar (dicho en vídeo)

Zaghi menciona que el último recurso ante una rotura incontrolable de la arteria lingual profunda (que nunca le ha pasado en este procedimiento pero sí en cirugías de cuello) es la Radiología Intervencionista: trasladar al paciente al hospital manteniendo presión manual mientras se introduce un catéter por la arteria femoral para sellar el vaso desde dentro (coiling).

- Vídeo: [Dr. Soroush Zaghi at ALSC - Breathe and Thrive 2022, in Las Vegas, NV](https://www.youtube.com/watch?v=3fq6w2buIy0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2022.

## zag-0576 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, al suturar el suelo de la boca, advierte no atravesar las glándulas salivales menores ni el conducto de Wharton; si se atrapa el conducto con la sutura, se producirá una hinchazón inmediata por acumulación de saliva (similar a una ránula) que requiere reabrir el punto.

- Vídeo: [Functional Frenuloplasty with Lightscalpel's Zaghi Handpiece at TBI (Full Procedure)](https://www.youtube.com/watch?v=j1aiuEtXRgQ), minuto `PENDIENTE DE VERIFICAR`.
- Vídeo: [Grade 4 Tongue-Tie - Bleeding Management, PeriAcryl Glue, Sutures, Functional Frenuloplasty - TBI](https://www.youtube.com/watch?v=SQRk2zUQdvE), minuto `PENDIENTE DE VERIFICAR`.

## zag-0577 · Experiencia clínica · sin verificar (dicho en vídeo)

Zaghi advierte que en bocas muy estrechas, la inflamación normal tras la cirugía puede comprimir la lengua contra los dientes de tal forma que impida el retorno venoso, causando isquemia y entumecimiento persistente en la punta.

- Vídeo: [Dr. Soroush Zaghi at ALSC - Breathe and Thrive 2022, in Las Vegas, NV](https://www.youtube.com/watch?v=3fq6w2buIy0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2022.

## zag-0579 · Experiencia clínica · sin verificar (dicho en vídeo)

Zaghi menciona que el uso crónico de cintas adhesivas muy fuertes para dormir (hostage tape o similares) puede causar "alopecia por tracción adhesiva", irritando y eliminando vello facial o capas de piel por el tirón diario.

- Vídeo: [Updates from Dr. Soroush Zaghi - The Breathe Institute at ALSC Symposium 2024](https://www.youtube.com/watch?v=iGQlzOtT4C0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2024.

## zag-0581 · Opinión · sin verificar (dicho en vídeo)

Zaghi sugiere que el empuje de la lengua contra los dientes (tongue thrust) es a veces una compensación desesperada del cuerpo para mantener la vía aérea abierta; si un ortodoncista cierra ese "mordida abierta" sin tratar el espacio respiratorio, el paciente puede desarrollar apnea severa.

- Vídeo: [Dr. Soroush Zaghi at ALSC - Breathe and Thrive 2022, in Las Vegas, NV](https://www.youtube.com/watch?v=3fq6w2buIy0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2022.

## zag-0582 · Opinión · sin verificar (dicho en vídeo)

Según Zaghi, lanza la hipótesis de que la exposición a moho tóxico ambiental puede ser el factor que provoque que las amígdalas y adenoides vuelvan a crecer después de haber sido extirpadas quirúrgicamente.

- Vídeo: [Excerpts From - TBI Ambassador Update (December 2024). Now Available On-Demand!](https://www.youtube.com/watch?v=DshE1KHc9s0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2024.

## zag-0584 · Opinión · sin verificar (dicho en vídeo)

Zaghi menciona que está explorando (a sugerencia del Dr. Brad) si la incapacidad de extender el dedo gordo del pie está relacionada con un frenillo lingual tenso, como punto extremo de la Línea Frontal Profunda de la fascia.

- Vídeo: [Dr. Zaghi on Research Principles (From TBI's Outlook at AAPMD Collaboration Cures Conference, 2021)](https://www.youtube.com/watch?v=vYQ1mv8Gdf0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2021.

## zag-0585 · Experiencia clínica · sin verificar (dicho en vídeo)

Zaghi menciona el desarrollo de un lavado nasal con xilitol, surfactantes (para romper la carga viral) y probióticos nasales específicos para restaurar el microbioma tras el uso crónico de sprays esteroideos.

- Vídeo: [Dr. Soroush Zaghi at ALSC - Breathe and Thrive 2022, in Las Vegas, NV](https://www.youtube.com/watch?v=3fq6w2buIy0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2022.

## zag-0586 · Experiencia clínica · sin verificar (dicho en vídeo)

Zaghi advierte que si se realiza un tratamiento láser no ablativo demasiado agresivo en el paladar blando y este sube demasiado, la base de la lengua no podrá alcanzarlo para tragar, lo que afecta la voz y provoca que el moco (post-nasal drip) se asiente en la garganta causando irritación crónica.

- Vídeo: [Updates from Dr. Soroush Zaghi - The Breathe Institute at ALSC Symposium 2024](https://www.youtube.com/watch?v=iGQlzOtT4C0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2024.

## zag-0588 · Experiencia clínica · sin verificar (dicho en vídeo)

Zaghi relata que en su primer día en la Facultad de Medicina de Harvard, el decano advirtió que la mitad de lo que aprenderían sería erróneo o estaría desactualizado en cinco años, y que nadie podía predecir qué mitad sería.

- Vídeo: [Meet Dr. Zaghi of The Breathe Institute](https://www.youtube.com/watch?v=Ng_EJ1yOKkw), minuto `PENDIENTE DE VERIFICAR`.
- Vídeo: [Evolution Of Myofunctional Therapy, Lingual Frenuloplasty - Dr. Soroush Zaghi at ALSC 2026.](https://www.youtube.com/watch?v=nlFVT6PUaYc), minuto `PENDIENTE DE VERIFICAR`.
- Vídeo: [Long-term Implications of Untreated Tongue-Tie (Dr. Soroush Zaghi, The Breathe Institute)](https://www.youtube.com/watch?v=cuT6qrm5IT0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2026.

## zag-0589 · Opinión · sin verificar (dicho en vídeo)

Zaghi sostiene que la mayor sabiduría es la humildad académica, citando a Sócrates: "La única sabiduría verdadera es saber que no sabes nada".

- Vídeo: [Excerpts From - TBI Ambassador Update (December 2024). Now Available On-Demand!](https://www.youtube.com/watch?v=DshE1KHc9s0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2024.

## zag-0590 · Opinión · sin verificar (dicho en vídeo)

Zaghi menciona el efecto Dunning-Kruger como un riesgo para los clínicos: aprender un poco puede llevar a un "pico de ignorancia" y sobreconfianza, antes de que la experiencia y las complicaciones traigan la verdadera cultura médica.

- Vídeo: [Excerpts From - TBI Ambassador Update (December 2024). Now Available On-Demand!](https://www.youtube.com/watch?v=DshE1KHc9s0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2024.

## zag-0591 · Experiencia clínica · sin verificar (dicho en vídeo)

Zaghi afirma que las dos lecciones más importantes de su carrera son: 1) Escuchar siempre a las enfermeras y 2) Escuchar siempre a los pacientes, por encima de lo que diga el libro de texto.

- Vídeo: [Dr. Soroush Zaghi at Tongue Time 2026 in Zurich, Switzerland  (Full Lecture)](https://www.youtube.com/watch?v=y6VkQnMBBvc), minuto `PENDIENTE DE VERIFICAR`.
- Vídeo: [Dr. Zaghi on Research Principles (From TBI's Outlook at AAPMD Collaboration Cures Conference, 2021)](https://www.youtube.com/watch?v=vYQ1mv8Gdf0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2026.

## zag-0592 · Opinión · sin verificar (dicho en vídeo)

Zaghi utiliza la metáfora del ciclo de vida de una rana (huevo, renacuajo, rana joven, adulta) para describir el proceso de aprendizaje clínico, donde no se pueden saltar etapas antes de buscar mentoría avanzada.

- Vídeo: [Dr. Soroush Zaghi at ALSC - Breathe and Thrive 2022, in Las Vegas, NV](https://www.youtube.com/watch?v=3fq6w2buIy0), minuto `PENDIENTE DE VERIFICAR`.
- Vídeo: [Dr. Zaghi on Research Principles (From TBI's Outlook at AAPMD Collaboration Cures Conference, 2021)](https://www.youtube.com/watch?v=vYQ1mv8Gdf0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2022.

## zag-0594 · Experiencia clínica · sin verificar (dicho en vídeo)

Zaghi y su socio Chad han desarrollado un software de EMR (historia clínica electrónica) impulsado por tareas y diseñado específicamente para el flujo de trabajo de la vía aérea, con el objetivo de automatizar notas y eliminar la necesidad de un escribiente humano (scribe).

- Vídeo: [Dr. Soroush Zaghi at ALSC - Breathe and Thrive 2022, in Las Vegas, NV](https://www.youtube.com/watch?v=3fq6w2buIy0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2022.

## zag-0595 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, TBI ha lanzado la plataforma "Breathe Insights" para recopilar datos a gran escala de pacientes con condiciones raras (como Marfan o Ehlers-Danlos) mediante la colaboración de terapeutas y médicos de todo el mundo.

- Vídeo: [Excerpts From - TBI Ambassador Update (December 2024). Now Available On-Demand!](https://www.youtube.com/watch?v=DshE1KHc9s0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2024.

## zag-0596 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, el instituto requiere que todos los profesionales en su directorio realicen una actualización anual obligatoria para asegurar que los referidos lleguen a manos de proveedores actualizados.

- Vídeo: [Excerpts From - TBI Ambassador Update (December 2024). Now Available On-Demand!](https://www.youtube.com/watch?v=DshE1KHc9s0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2024.

## zag-0601 · Opinión · sin verificar (dicho en vídeo)

Zaghi propone el "Test del Periódico" de Warren Buffett: el profesional debe actuar de modo que se sienta cómodo si sus decisiones clínicas se publicaran en la portada del periódico de su ciudad.

- Vídeo: [Excerpts From - TBI Ambassador Update (December 2024). Now Available On-Demand!](https://www.youtube.com/watch?v=DshE1KHc9s0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2024.

## zag-0602 · Opinión · sin verificar (dicho en vídeo)

Zaghi sostiene que la curiosidad es el motor de la ciencia y que esta nunca es algo "establecido" (settled); sin preguntas constantes no hay progreso científico.

- Vídeo: [Dr. Zaghi -TBI - AAPMD: Ethical Principles in the Practice of Scientific Research and Public Policy](https://www.youtube.com/watch?v=wDuCMJxtjzE), minuto `PENDIENTE DE VERIFICAR`.

## zag-0603 · Opinión · sin verificar (dicho en vídeo)

Zaghi advierte sobre los peligros del sesgo de publicación y la censura en revistas científicas, argumentando que esto genera desconfianza en el sistema de salud.

- Vídeo: [Dr. Zaghi -TBI - AAPMD: Ethical Principles in the Practice of Scientific Research and Public Policy](https://www.youtube.com/watch?v=wDuCMJxtjzE), minuto `PENDIENTE DE VERIFICAR`.

## zag-0604 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, en sus conferencias sobre investigación, utiliza ejercicios de ilusiones ópticas (como la ilusión de Munker-White o el vestido de colores) para enseñar a los alumnos que lo que ven subjetivamente puede ser un error de medición.

- Vídeo: [Dr. Zaghi on Research Principles (From TBI's Outlook at AAPMD Collaboration Cures Conference, 2021)](https://www.youtube.com/watch?v=vYQ1mv8Gdf0), minuto `PENDIENTE DE VERIFICAR`.

## zag-0605 · Experiencia clínica · sin verificar (dicho en vídeo)

Zaghi utiliza una herramienta llamada "Rhino Vision" (aprendida de dentistas) para evaluar la nariz, demostrando que un cirujano debe estar abierto a herramientas de otras disciplinas.

- Vídeo: [Dr. Soroush Zaghi at ALSC - Breathe and Thrive 2022, in Las Vegas, NV](https://www.youtube.com/watch?v=3fq6w2buIy0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2022.

## zag-0606 · Experiencia clínica · sin verificar (dicho en vídeo)

Zaghi advierte que el uso prolongado de cintas adhesivas bucales (mouth tape) de alta adhesión puede provocar "alopecia por tracción relacionada con el adhesivo" en el vello peribucal.

- Vídeo: [Excerpts From - TBI Ambassador Update (December 2024). Now Available On-Demand!](https://www.youtube.com/watch?v=DshE1KHc9s0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2024.

## zag-0607 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, para el pegamento PeriAcryl, advierte que debe aplicarse en "puntos" (como abotonar una camisa) y no de forma continua (como una cremallera), ya que esto último causa que se desprenda todo el bloque al gesticular.

- Vídeo: [Dr. Soroush Zaghi at ALSC - Breathe and Thrive 2022, in Las Vegas, NV](https://www.youtube.com/watch?v=3fq6w2buIy0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2022.

## zag-0608 · Opinión · sin verificar (dicho en vídeo)

Zaghi relata como anécdota personal que su pasión por el esquí en Mammoth motiva su enseñanza: quiere que sus alumnos pasen de las "pistas verdes" a las "Black Diamond" (casos de alta complejidad) con seguridad.

- Vídeo: [Dr. Soroush Zaghi at ALSC - Breathe and Thrive 2022, in Las Vegas, NV](https://www.youtube.com/watch?v=3fq6w2buIy0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2022.

## zag-0609 · Experiencia clínica · sin verificar (dicho en vídeo)

Zaghi menciona haber sido víctima de una campaña de desprestigio en la que competidores locales compraron anuncios de Google AdWords con su nombre para dirigir a los pacientes a publicaciones negativas.

- Vídeo: [Frenums, Fascia and Physiology by Dr. Soroush Zaghi & Sanda Valcu-Pinkerton, COM - at AAPMD 2019](https://www.youtube.com/watch?v=BM3TmSXhUIw), minuto `PENDIENTE DE VERIFICAR`.
- Vídeo: [Excerpts From - TBI Ambassador Update (December 2024). Now Available On-Demand!](https://www.youtube.com/watch?v=DshE1KHc9s0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2024.

---

<!-- archivo: expertos/soroush-zaghi/investigacion-etica.md -->
# Investigación, evidencia y ética

Ideas públicas de Soroush Zaghi sobre este tema, reconstruidas a partir de sus vídeos. **No es Zaghi hablando ni una guía clínica.** Cómo leer cada entrada: README. Entradas: 31.

## zag-0282 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, la base de la educación continua no es lo publicado en libros hace años, sino la investigación activa que se realiza en la práctica diaria.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0283 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, "La mitad de lo que aprendes en la escuela de medicina/odontología será erróneo o estará desactualizado en 5 años; el problema es que nadie sabe qué mitad".

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0284 · Opinión · sin verificar (dicho en vídeo)

Según Zaghi, el mayor enemigo del conocimiento no es la ignorancia, sino la ilusión de que ya se sabe todo.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0285 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, la ciencia es un proceso de hacer preguntas, realizar observaciones y refinar hipótesis, no un conjunto de respuestas cerradas.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0286 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, en medicina, las nuevas ideas suelen venir "desde abajo" (observaciones clínicas, reportes de casos) y suben por la cadena de evidencia, no empiezan en el nivel 1.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0287 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, es imposible realizar ensayos controlados aleatorizados (RCT) de doble ciego para procedimientos quirúrgicos de la misma forma que para fármacos.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0288 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, los reportes de casos (Nivel 5) y las series de casos (Nivel 4) son esenciales para descubrimientos antes de poder realizar estudios de Nivel 1.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0289 · Opinión · sin verificar (dicho en vídeo)

Según Zaghi, la "verdad" pasa por tres etapas exactas: 1. Ridículo, 2. Oposición violenta, 3. Aceptación como algo autoevidente.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0290 · Experiencia clínica · sin verificar (dicho en vídeo)

Zaghi utiliza la analogía de los "68 Tonos de Gris" para explicar que la mayoría de lo que hacemos no son hechos o creencias puras, sino opiniones informadas en un continuo.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0291 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, cuando se dice "no hay evidencia", lo que realmente se está diciendo es "no entiendo" (un argumento desde la ignorancia).

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0292 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, un estudio con resultados no significativos no prueba que algo no funcione, solo que el investigador no aprendió nada o no pudo demostrar la diferencia.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0293 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, la falta de evidencia documentada para una asociación (por ejemplo, frenillo y posición del hioides) no significa que dicha asociación no exista.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0294 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, en medicina se deben usar las mejores evidencias disponibles y, si no hay ensayos aleatorizados, la mejor evidencia disponible es la opinión de expertos.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0295 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, sesgo de Confirmación (Confirmation Bias): Tendencia a buscar solo información que apoye las creencias previas e ignorar lo que las desafía.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0296 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, sesgo de Publicación (Publication Bias): Los editores rechazan artículos sobre temas "controversiales" (como el frenillo labial) incluso si los datos son irrefutables, por miedo al juicio de sus colegas.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0297 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, sesgo de Medición (Measurement Bias): Medir cosas de forma distinta (ej. medir frenillo solo por protrusión vs. elevación) invalida la comparación entre estudios.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0298 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, sesgo de Rendimiento (Performance Bias): Los resultados de un estudio de frenotomía tradicional (solo corte) no son comparables con la frenuloplastia funcional con terapia.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0299 · Estudio citado · verificado en PubMed

Clinical Consensus Statement (2020) de la American Academy of Otolaryngology. Zaghi lo critica por ser una encuesta de opiniones de 12 otorrinos pediátricos sin experiencia clínica real en frenuloplastia funcional.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.
- Estudio: PMID [32283998](https://pubmed.ncbi.nlm.nih.gov/32283998/), ficha 2020-messner-consenso.md.

## zag-0300 · Estudio citado · sin verificar (dicho en vídeo)

Salt et al. (Estudio sobre habla). Zaghi critica que sus conclusiones digan "no hay diferencia" cuando los datos del artículo muestran puntuaciones más altas en niños tratados; atribuye esto a un sesgo de confirmación por falta de significancia estadística.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0301 · Experiencia clínica · sin verificar (dicho en vídeo)

Zaghi critica el artículo de la revista The Atlantic que describe la expansión maxilar como "desgarrar" los huesos de los niños, calificándolo de sensacionalista y alejado de la realidad clínica.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0302 · Experiencia clínica · sin verificar (dicho en vídeo)

Zaghi critica estudios de ortodoncia que concluyen que las extracciones de premolares no afectan la vía aérea porque no miden la compensación postural del cuello (ángulo NBC3).

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.
- Estudio: PMID [36841260](https://pubmed.ncbi.nlm.nih.gov/36841260/), ficha 2023-coppelson-postura-cbct.md.

## zag-0303 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, relaciona los niveles de evidencia con la carga de la prueba judicial: Sospecha razonable (Reporte de caso), Preponderancia de evidencia (Cohorte), y Más allá de toda duda razonable (RCTs).

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0304 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, para intervenciones de bajo riesgo (como respirar por la nariz o terapia miofuncional), solo se necesita una "preponderancia de evidencia", no pruebas de "juicio por asesinato".

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0305 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, error Tipo 1 (Falso Positivo) vs. Error Tipo 2 (Falso Negativo): Explica que en cáncer de mama preferimos el falso positivo para no perder casos, pero en apnea a menudo ignoramos el problema por fallos del IAH (Falso Negativo).

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0306 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, "The Newspaper Test" (Warren Buffett): No hagas nada a un paciente que no te sentirías orgulloso de ver publicado en la portada del New York Times.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0307 · Estudio citado · sin verificar (dicho en vídeo)

Según Zaghi, informe Belmont. Cita sus tres pilares: Respeto por las personas (autonomía y consentimiento informado), Beneficencia (maximizar beneficios/no dañar) y Justicia.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0308 · Experiencia clínica · sin verificar (dicho en vídeo)

Zaghi critica éticamente a médicos que pierden la compasión por pacientes que rechazan ciertos mandatos médicos, recordando el juramento hipocrático sobre la "calidez y comprensión" por encima de la fuerza.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0309 · Estudio citado · sin verificar (dicho en vídeo)

Zaghi menciona hitos de violaciones éticas como el experimento de Tuskegee (sifilis no tratada), la tragedia de la Talidomida (Francis Kelsey en la FDA) y la escuela Willowbrook (infección deliberada de hepatitis).

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0310 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, breathe Insights: Plataforma en desarrollo (2024) para que terapeutas de todo el mundo introduzcan datos y permitan estudios masivos (ej. 100 pacientes con Ehlers-Danlos).

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0311 · Estudio citado · sin verificar (dicho en vídeo)

Baxter y Zaghi (2020). Estudio de 100 casos sobre el cierre del diastema tras frenectomía labial.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0312 · Estudio citado · sin verificar (dicho en vídeo)

Villa et al. (2014). Establece la respiración nasal continua como objetivo final para evitar recaídas tras amigdalectomía.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

---

<!-- archivo: expertos/soroush-zaghi/maxilofacial.md -->
# Desarrollo maxilofacial

Ideas públicas de Soroush Zaghi sobre este tema, reconstruidas a partir de sus vídeos. **No es Zaghi hablando ni una guía clínica.** Cómo leer cada entrada: README. Entradas: 28.

## zag-0002 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, el ángulo NBC3 (nasion-basion-C3) ronda los 105-110 grados (en otra charla dice 105 ± 5, y en otra que lo habitual está cerca de 115); un valor de 120-125 grados indica compensación máxima, con la cabeza muy adelantada para mantener abierta una vía aérea que de otro modo colapsaría.

- Vídeo: [Updates from Dr. Soroush Zaghi - The Breathe Institute at ALSC Symposium 2024](https://www.youtube.com/watch?v=iGQlzOtT4C0), minuto `PENDIENTE DE VERIFICAR`.
- Vídeo: [FAirEST 6 + 4](https://www.youtube.com/watch?v=ckwLiTMb7wo), minuto 13:08 (localizado en los subtítulos automáticos).
- Año de la charla: 2024.
- Estudio: PMID [36841260](https://pubmed.ncbi.nlm.nih.gov/36841260/), ficha 2023-coppelson-postura-cbct.md.
- Cita corta (transcripción automática, puede tener errores): «The naon Bon C3 angle should be around 105 to 110 if it's like 120 125 that's where you're maxed out»

## zag-0003 · Estudio citado · verificado en PubMed

El estudio de Yoon, Zaghi y colaboradores (Orthod Craniofac Res 2017), en 302 sujetos consecutivos de una consulta de ortodoncia, asoció la movilidad lingual restringida (medida con el TRMR y con la medida de Kotlow) con arcos maxilares más estrechos y con un paladar blando más largo; no la asoció con la posición del hioides ni con la clase esquelética de Angle.

- Vídeo: [Dr. Soroush Zaghi at AACP 2018 - Tongue-tie and Myofascial Disfunction](https://www.youtube.com/watch?v=OdgYVx9FNCc), minuto 21:18 (localizado en los subtítulos automáticos).
- Vídeo: [Frenums, Fascia and Physiology by Dr. Soroush Zaghi & Sanda Valcu-Pinkerton, COM - at AAPMD 2019](https://www.youtube.com/watch?v=BM3TmSXhUIw), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2018.
- Estudio: PMID [28994495](https://pubmed.ncbi.nlm.nih.gov/28994495/), ficha 2017-yoon-maxilar.md.
- Cita corta (transcripción automática, puede tener errores): «In the study researchers have gotten away the tongue mobility and 302 patients using the tongue range of motion ratio and the problem freetown measurement.»

## zag-0004 · Estudio citado · sin verificar (dicho en vídeo)

Según Zaghi, en el estudio de Yoon de 2017 los pacientes con lengua atada de grado 3 o 4 tenían el paladar más en forma de V que de U.

- Vídeo: [Frenums, Fascia and Physiology by Dr. Soroush Zaghi & Sanda Valcu-Pinkerton, COM - at AAPMD 2019](https://www.youtube.com/watch?v=BM3TmSXhUIw), minuto 21:01 (localizado en los subtítulos automáticos).
- Año de la charla: 2019.
- Estudio: PMID [28994495](https://pubmed.ncbi.nlm.nih.gov/28994495/), ficha 2017-yoon-maxilar.md.
- Cita corta (transcripción automática, puede tener errores): «We found that if they have these grade three and four tongue ties there was a clear difference in how u shaped versus v shaped these patients were.»

## zag-0005 · Estudio citado · sin verificar (dicho en vídeo)

Según Zaghi, la restricción de la movilidad lingual explica solo alrededor del 7.6% de la varianza de la estrechez del arco maxilar (estudio de Yoon 2017), por lo que el frenillo no es la causa principal del paladar alto: influyen también la respiración bucal, el tono, la nutrición y el ambiente de deglución.

- Vídeo: [Frenums, Fascia and Physiology by Dr. Soroush Zaghi & Sanda Valcu-Pinkerton, COM - at AAPMD 2019](https://www.youtube.com/watch?v=BM3TmSXhUIw), minuto 21:47 (localizado en los subtítulos automáticos).
- Año de la charla: 2019.
- Estudio: PMID [28994495](https://pubmed.ncbi.nlm.nih.gov/28994495/), ficha 2017-yoon-maxilar.md.
- Cita corta (transcripción automática, puede tener errores): «Tongue tie actually only accounts for about seven point six percent of the variance that means that tongue tie counts for less than ten percent of the reason why you get high arch palate.»

## zag-0011 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, si el ancho intermolar del adulto (medido en la unión cemento-esmalte de los primeros molares) es inferior a 32 mm, no libera el frenillo lingual y da prioridad a la expansión ósea, porque la lengua no cabe en el paladar y puede obstruir la vía aérea; la excepción es la restricción severa (grado 3-4), donde puede hacer una liberación de primera etapa y ampliar después; con un ancho límite de 32-34 mm libera igualmente si el paciente tiene tensión crónica de cuello, hombros o cefaleas debilitantes, tras discutir los riesgos de espacio; en niños deriva a expansión según el índice de Boyd (24 + edad).

- Vídeo: [Dr. Soroush Zaghi at ALSC - Breathe and Thrive 2022, in Las Vegas, NV](https://www.youtube.com/watch?v=3fq6w2buIy0), minuto 1:00:42 (localizado en los subtítulos automáticos).
- Vídeo: [Updates from Dr. Soroush Zaghi - The Breathe Institute at ALSC Symposium 2024](https://www.youtube.com/watch?v=iGQlzOtT4C0), minuto `PENDIENTE DE VERIFICAR`.
- Vídeo: [Evolution Of Myofunctional Therapy, Lingual Frenuloplasty - Dr. Soroush Zaghi at ALSC 2026.](https://www.youtube.com/watch?v=nlFVT6PUaYc), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2022.
- Cita corta (transcripción automática, puede tener errores): «if they're less than 32 mm inter with unless there a severe 3 four I wouldn't recommend doing it [tongue-tie release]... if you're under if you're like 32 to 34 you can do a stage one in anticipation of a […]»

## zag-0012 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi y Coppelson, el ancho intermolar ideal en adultos es de 38 a 42 mm (según «estudios intermolares» que cita Coppelson sin nombrar autor); Zaghi considera aceptable liberar el frenillo con 36-38 mm, y Coppelson recuerda que el ancho transverso total importa más que el intermolar.

- Vídeo: [Advances in Surgical Technique with Dr. Kevin Coppelson - BreatheMAX - 10/28/24](https://www.youtube.com/watch?v=gsAggiqvgEY), minuto 59:24 (localizado en los subtítulos automáticos).
- Vídeo: [Dr. Soroush Zaghi at ALSC - Breathe and Thrive 2022, in Las Vegas, NV](https://www.youtube.com/watch?v=3fq6w2buIy0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2022.
- Cita corta (transcripción automática, puede tener errores): «if you look at interolar studies I would say anywhere between 38 to 42 millimeters of intermolear width tends to be a good spot for most adults»

## zag-0161 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, MMA (Avance Maxilomandibular) es el "último recurso" o la solución definitiva para abrir físicamente la vía aérea cuando la deficiencia esquelética es severa.

- Vídeo: [Pediatric Sleep Disordered Breathing and Maxillofacial Development with Soroush Zaghi](https://www.youtube.com/watch?v=eA1Yqbruw4g), minuto `PENDIENTE DE VERIFICAR`.
- Vídeo: [Updates from Dr. Soroush Zaghi - The Breathe Institute at ALSC Symposium 2024](https://www.youtube.com/watch?v=iGQlzOtT4C0), minuto `PENDIENTE DE VERIFICAR`.
- Vídeo: [Dr. Soroush Zaghi on the impact of Tongue-ties on Sleep Disordered Breathing in Kids](https://www.youtube.com/watch?v=tdnmhBv6Zg4), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2024.
- Estudio: PMID [26606321](https://pubmed.ncbi.nlm.nih.gov/26606321/), ficha 2016-zaghi-mma-metaanalisis.md.

## zag-0195 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, el paladar es, por definición, el suelo de la nariz; un paladar estrecho y alto (ojival) garantiza una cavidad nasal estrecha y predispone mecánicamente a la desviación del tabique (buckling).

- Vídeo: [Full Lecture: Evaluation, Diagnosis, and Treatment of Tongue, Lip, & Buccal Ties, Dr. Soroush Zaghi](https://www.youtube.com/watch?v=iP3c-C9L9b0), minuto `PENDIENTE DE VERIFICAR`.
- Vídeo: [Evolution Of Myofunctional Therapy, Lingual Frenuloplasty - Dr. Soroush Zaghi at ALSC 2026.](https://www.youtube.com/watch?v=nlFVT6PUaYc), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2026.

## zag-0214 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, la lengua actúa como un "expansor palatino natural"; cuando está en el paladar, sirve de andamio para el arco maxilar, pero si está abajo (por frenillo o hábito), los labios y mejillas colapsan el arco hacia adentro.

- Vídeo: [Dr. Soroush Zaghi at Tongue Time 2026 in Zurich, Switzerland  (Full Lecture)](https://www.youtube.com/watch?v=y6VkQnMBBvc), minuto `PENDIENTE DE VERIFICAR`.
- Vídeo: [Frenums, Fascia and Physiology by Dr. Soroush Zaghi & Sanda Valcu-Pinkerton, COM - at AAPMD 2019](https://www.youtube.com/watch?v=BM3TmSXhUIw), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2026.

## zag-0215 · Opinión · sin verificar (dicho en vídeo)

Según Zaghi, hipótesis Musculoesquelética de Guilleminault: Un factor incitante (inflamación, dieta, postura) genera respiración bucal y postura lingual baja, lo que provoca inflamación local (amígdalas), crecimiento facial vertical (cara larga) y estrechamiento del paladar, retroalimentando el ciclo.

- Vídeo: [Tongue-Tie, Sleep, Breathing, and Myofunctional Therapy: New Research Updates. Dr. Zaghi at ALSC '20](https://www.youtube.com/watch?v=G9GrUw7YJD0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2020.

## zag-0216 · Opinión · sin verificar (dicho en vídeo)

Según Zaghi, hipótesis de Moss de la Matriz Funcional: Los huesos no crecen solos, crecen en respuesta a la función de los tejidos blandos que los rodean.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0217 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, el frenillo es "la correa" y el paladar/mandíbula es "la jaula". No sirve de nada soltar la correa si el perro sigue en una jaula pequeña; si el espacio es insuficiente, la lengua liberada puede obstruir más la vía aérea.

- Vídeo: [Dr. Soroush Zaghi at ALSC - Breathe and Thrive 2022, in Las Vegas, NV](https://www.youtube.com/watch?v=3fq6w2buIy0), minuto `PENDIENTE DE VERIFICAR`.
- Vídeo: [Tongue-Tie, Sleep, Breathing, and Myofunctional Therapy: New Research Updates. Dr. Zaghi at ALSC '20](https://www.youtube.com/watch?v=G9GrUw7YJD0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2020.

## zag-0218 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, en pacientes con paladares muy estrechos y apnea, liberar el frenillo puede ser "la gota que colma el vaso" y desestabilizarlos al empujar la masa lingual hacia la garganta.

- Vídeo: [Updates from Dr. Soroush Zaghi - The Breathe Institute at ALSC Symposium 2024](https://www.youtube.com/watch?v=iGQlzOtT4C0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2024.

## zag-0219 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, signos visuales clave: Scalloping (marcas de dientes en los bordes de la lengua), Tongue Overflow (la lengua desborda sobre las superficies de los dientes en succión palatina) y Hioides bajo.

- Vídeo: [Updates from Dr. Soroush Zaghi - The Breathe Institute at ALSC Symposium 2024](https://www.youtube.com/watch?v=iGQlzOtT4C0), minuto `PENDIENTE DE VERIFICAR`.
- Vídeo: [FAirEST 6 + 4](https://www.youtube.com/watch?v=ckwLiTMb7wo), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2024.

## zag-0220 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, el "Palatal Flutter Sign" negativo (el paciente sigue roncando incluso con la lengua succionada al paladar) es un indicador de que el problema es de espacio lingual y no solo de movilidad.

- Vídeo: [FAirEST 6 + 4](https://www.youtube.com/watch?v=ckwLiTMb7wo), minuto `PENDIENTE DE VERIFICAR`.

## zag-0221 · Experiencia clínica · sin verificar (dicho en vídeo)

MARPE (Miniscrew Assisted Rapid Palatal Expansion) permite crecimiento óseo real incluso en adultos de 40 años; Zaghi se sometió personalmente al procedimiento para tratar su propio paladar de 33 mm.

- Vídeo: [Updates from Dr. Soroush Zaghi - The Breathe Institute at ALSC Symposium 2024](https://www.youtube.com/watch?v=iGQlzOtT4C0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2024.

## zag-0222 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, la expansión esquelética (MIND/MARPE) puede reducir el IAH en un 77% en adultos y 70% en niños, además de mejorar el flujo nasal al ensanchar la válvula nasal.

- Vídeo: [Full Lecture: Evaluation, Diagnosis, and Treatment of Tongue, Lip, & Buccal Ties, Dr. Soroush Zaghi](https://www.youtube.com/watch?v=iP3c-C9L9b0), minuto `PENDIENTE DE VERIFICAR`.

## zag-0223 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, observación de que tras la expansión, la vía aérea en el CBCT puede no verse más grande, pero el ángulo cabeza-cuello (NBC3) se neutraliza, indicando que el paciente ya no necesita compensar con la cabeza hacia adelante.

- Vídeo: [Updates from Dr. Soroush Zaghi - The Breathe Institute at ALSC Symposium 2024](https://www.youtube.com/watch?v=iGQlzOtT4C0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2024.
- Estudio: PMID [36841260](https://pubmed.ncbi.nlm.nih.gov/36841260/), ficha 2023-coppelson-postura-cbct.md.

## zag-0224 · Estudio citado · sin verificar (dicho en vídeo)

Según Zaghi, angel Emerson (1860). Primera descripción de la expansión rápida palatina.

- Vídeo: [Evolution Of Myofunctional Therapy, Lingual Frenuloplasty - Dr. Soroush Zaghi at ALSC 2026.](https://www.youtube.com/watch?v=nlFVT6PUaYc), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2026.

## zag-0225 · Estudio citado · sin verificar (dicho en vídeo)

Yoon, Liu et al. (2019/2020). Demostró que la expansión palatina reduce el volumen de amígdalas y adenoides al restaurar la respiración nasal.

- Vídeo: [Long-term Implications of Untreated Tongue-Tie (Dr. Soroush Zaghi, The Breathe Institute)](https://www.youtube.com/watch?v=cuT6qrm5IT0), minuto `PENDIENTE DE VERIFICAR`.

## zag-0226 · Estudio citado · sin verificar (dicho en vídeo)

Andrews et al. (G-line). Valida que la maxila debe crecer hasta la línea de la glabela (frente).

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0227 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, MIND (Nasal Maxillary Expansion) es una técnica mínimamente invasiva bajo sedación IV que logra expansión del tercio medio facial (pómulos) y no solo de los dientes.

- Vídeo: [Advances in Surgical Technique with Dr. Kevin Coppelson - BreatheMAX - 10/28/24](https://www.youtube.com/watch?v=gsAggiqvgEY), minuto `PENDIENTE DE VERIFICAR`.

## zag-0228 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, protocolo de expansión: El hueso maxilar debe ser idealmente 5 mm más ancho que el mandibular para permitir una oclusión estable.

- Vídeo: [Excerpts From - TBI Ambassador Update (December 2024). Now Available On-Demand!](https://www.youtube.com/watch?v=DshE1KHc9s0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2024.

## zag-0229 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, en cirugía ortognática (MMA), realiza rutinariamente una "mini-septoplastia" para asegurar que la vía aérea nasal sea óptima tras el movimiento óseo.

- Vídeo: [Advances in Surgical Technique with Dr. Kevin Coppelson - BreatheMAX - 10/28/24](https://www.youtube.com/watch?v=gsAggiqvgEY), minuto `PENDIENTE DE VERIFICAR`.

## zag-0230 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, la intervención temprana (0-5 años) con masajes palatinos, "Baby Munchie" y masticación de alimentos duros puede evitar la necesidad de cirugías futuras al guiar el crecimiento óseo.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0231 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, el 95% del crecimiento facial se completa a los 6 años, lo que hace que cualquier intervención tras esa edad sea más difícil.

- Vídeo: [Breathe Myo Explained: Tongue Tie, Airway Health, Facial Development with Sandraluz Gonzalez](https://www.youtube.com/watch?v=ni2dO45jdbo), minuto `PENDIENTE DE VERIFICAR`.

## zag-0232 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, enumera síndromes asociados a paladares estrechos y frenillos: Crouzon, Apert, Treacher Collins y Marfan.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0233 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, una moneda de 5 centavos pesa 5 gramos; se requieren solo esos 5 gramos de presión constante de la lengua para mover un hueso en un niño en crecimiento.

- Vídeo: [Breathe Myo Explained: Tongue Tie, Airway Health, Facial Development with Sandraluz Gonzalez](https://www.youtube.com/watch?v=ni2dO45jdbo), minuto `PENDIENTE DE VERIFICAR`.

---

<!-- archivo: expertos/soroush-zaghi/miofuncional.md -->
# Terapia miofuncional

Ideas públicas de Soroush Zaghi sobre este tema, reconstruidas a partir de sus vídeos. **No es Zaghi hablando ni una guía clínica.** Cómo leer cada entrada: README. Entradas: 36.

## zag-0048 · Estudio citado · verificado en PubMed

Según Zaghi, la terapia miofuncional reduce el índice de apnea-hipopnea (AHI) alrededor de un 50% en adultos y un 62% en niños con apnea obstructiva del sueño, según el meta-análisis de Camacho y colaboradores (2015).

- Vídeo: [Dr. Soroush Zaghi on the impact of Tongue-ties on Sleep Disordered Breathing in Kids](https://www.youtube.com/watch?v=tdnmhBv6Zg4), minuto `PENDIENTE DE VERIFICAR`.
- Vídeo: [Frenums, Fascia and Physiology by Dr. Soroush Zaghi & Sanda Valcu-Pinkerton, COM - at AAPMD 2019](https://www.youtube.com/watch?v=BM3TmSXhUIw), minuto `PENDIENTE DE VERIFICAR`.
- Vídeo: [Myofunctional Therapy and Frenuloplasty Can Be Appropriate Treatments for Obstructive Sleep Apnea](https://www.youtube.com/watch?v=dlU8wxa8474), minuto `PENDIENTE DE VERIFICAR`.
- Vídeo: [Full Lecture: Evaluation, Diagnosis, and Treatment of Tongue, Lip, & Buccal Ties, Dr. Soroush Zaghi](https://www.youtube.com/watch?v=iP3c-C9L9b0), minuto `PENDIENTE DE VERIFICAR`.
- Vídeo: [Pediatric Sleep Disordered Breathing and Maxillofacial Development with Soroush Zaghi](https://www.youtube.com/watch?v=eA1Yqbruw4g), minuto `PENDIENTE DE VERIFICAR`.
- Vídeo: [Tongue-Tie, Sleep, Breathing, and Myofunctional Therapy: New Research Updates. Dr. Zaghi at ALSC '20](https://www.youtube.com/watch?v=G9GrUw7YJD0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2019.
- Estudio: PMID [25348130](https://pubmed.ncbi.nlm.nih.gov/25348130/), ficha 2015-camacho-miofuncional-apnea.md.
- Cita corta (transcripción automática, puede tener errores): «Camacho et al. (2015). Meta-análisis que demuestra que la OMT reduce el IAH en un 50% en adultos y un 62% en niños»

## zag-0095 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, la terapia miofuncional consiste en un conjunto de ejercicios para la lengua, la boca y la cara, que en proveedores avanzados también incluye postura corporal total y fisioterapia.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0096 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, los tres objetivos fundamentales son: labios juntos, lengua en el paladar y respiración exclusivamente nasal.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0097 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, la lengua arriba actúa como un "interruptor" que activa el circuito de respiración nasal y lo sella del bucal; si la lengua está abajo, el circuito se rompe.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0098 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, sirve para preparar el tejido antes de la cirugía (haciendo la disección más fácil) y para rehabilitar las estructuras orales después.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0099 · Opinión · sin verificar (dicho en vídeo)

Según Zaghi, el éxito de la OMT depende de que la lengua sea el "andamio" natural del arco maxilar; si está abajo, los labios y mejillas ganan la batalla y el paladar se estrecha.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0100 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, ayuda a reducir la tensión muscular compensatoria en cuello y hombros al enseñar a usar los músculos intrínsecos de la lengua en lugar de los accesorios.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0101 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, mejora la adherencia al CPAP en adultos al evitar que la lengua caiga hacia atrás y bloquee la presión del aire.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0102 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, el protocolo estándar en TBI incluye 1 mes de terapia preoperatoria y 2 meses de terapia postoperatoria.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0103 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, en niños, a veces solo la terapia (sin cirugía) puede lograr resultados de cierre bucal y mejora de postura, por lo que siempre se debe intentar primero.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0104 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, la preparación preoperatoria debe durar hasta que el paciente logre un control de la función oral que permita al cirujano "retraer" la vena, arteria y nervio lingual mediante la succión palatina durante el corte.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0105 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, el paciente "está listo" para la cirugía cuando puede mantener la succión palatina lingual (LPS) durante 1 a 2 minutos (o al menos 45 segundos) sin excesiva compensación del piso de la boca.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0106 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, después de la cirugía, se debe llamar al paciente el mismo día para calmar su ansiedad, ya que el estrés afecta la cicatrización.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0107 · Experiencia clínica · sin verificar (dicho en vídeo)

Succión Palatina Lingual (LPS): Es el ejercicio rey. Zaghi acuñó el término tras una votación en un grupo de estudio en 2021. Sirve para elevar el cuerpo de la lengua al paladar duro.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0108 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, palatal Flutter Sign: Prueba de pronóstico donde el paciente ronca con la boca abierta y luego intenta roncar con la lengua en el paladar; si no puede roncar con la lengua arriba, la OMT y la cirugía tendrán éxito.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0109 · Experiencia clínica · sin verificar (dicho en vídeo)

Técnica de deglución: En adultos con cara larga y anatomía alterada, Zaghi enseña a tragar empujando el cuerpo de la lengua hacia arriba pero manteniendo la lengua más abajo en reposo si no hay espacio, para evitar el empuje lingual (tongue thrust).

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0110 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, uso de bloques de mordida (Bite Blocks): Herramienta de diagnóstico para aislar el movimiento de la lengua y eliminar la compensación de la mandíbula (dependencia lengua-mandíbula).

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0111 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, estiramientos manuales (Manual Wound Stretches): Deben realizarse para evitar que la herida se cierre por segunda intención (diamante) y fomentar una cicatriz lineal pequeña.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0112 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, la OMT no funcionará si hay una obstrucción nasal orgánica (pólipos, desviación severa) que no ha sido tratada.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0113 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, Hipermovilidad/Ehlers-Danlos: En estos pacientes, los estiramientos agresivos de OMT pueden ser perjudiciales. Necesitan ejercicios de estabilidad y carga en lugar de flexibilidad.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0114 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, apraxia o bajo tono severo: Estos pacientes pueden no ser buenos candidatos para la intervención si no hay capacidad de cumplimiento con la terapia.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0115 · Estudio citado · verificado en PubMed

Según Zaghi, en un estudio de 24 niños curados de apnea tras adenoamigdalectomía y ortodoncia, los 11 que completaron terapia miofuncional no recayeron y los 13 que no la hicieron sufrieron recaída en el seguimiento de 22 a 50 meses.

- Vídeo: [Pediatric Sleep Disordered Breathing and Maxillofacial Development with Soroush Zaghi](https://www.youtube.com/watch?v=eA1Yqbruw4g), minuto `PENDIENTE DE VERIFICAR`.
- Estudio: PMID [23522724](https://pubmed.ncbi.nlm.nih.gov/23522724/), ficha 2013-guilleminault-reeducacion-miofascial.md.
- Cita corta (transcripción automática, puede tener errores): «Guilleminault et al. (2013). De 24 niños curados de apnea, los 11 que realizaron terapia miofuncional (OMT) no tuvieron recaídas tras 2 años; los 13 que no la hicieron, recayeron»

## zag-0116 · Estudio citado · sin verificar (dicho en vídeo)

Villa et al. (2014/2015). Establece la respiración nasal continua como el objetivo final del tratamiento.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0117 · Estudio citado · sin verificar (dicho en vídeo)

Kim et al. (2011). Sobre la inestabilidad de la condición de "boca semiabierta" (labios sellados pero lengua abajo).

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0118 · Experiencia clínica · sin verificar (dicho en vídeo)

Zaghi define su rol como el de un "entrenador" (coach). Si el paciente hace los ejercicios solo con una lista, puede realizarlos de forma maladaptativa (usando el cuello) y lesionarse.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0119 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, fases de cicatrización: La contracción de la herida comienza hacia el día 10 post-cirugía; es cuando el paciente siente que "corre contra el viento" y necesita más apoyo del terapeuta.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0120 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, los estiramientos manuales post-op no se inician hasta el día 3, para dejar que la inflamación inicial ceda.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0121 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, ejercicios post-operatorios: "Body pull" (sujetar la lengua y tirar), "Forklift" (usar índices para elevar la lengua verticalmente) y "J-sweep" (barrido del piso de la boca hacia arriba por los laterales).

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0122 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, capas de la cebolla: Metodología para pelar capas de disfunción (hábitos, obstrucción, frenillo) hasta llegar a la causa raíz.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0123 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, fuerza de la lengua: La lengua ejerce de 50 a 55 gramos de presión; se necesitan solo 5 gramos (el peso de una moneda de 5 centavos) para mover un hueso.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0124 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, el 95% del crecimiento facial se completa a los 6 años, por lo que la OMT es crítica antes de esa edad.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0125 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, ejercicio "Tongue Trace": Trazar con la punta el paladar desde los dientes frontales hasta el paladar blando y volver sin mover la mandíbula.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0126 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, identifica 5 compensaciones principales: elevación del piso de la boca, mueca facial, compromiso del cuello, protrusión de mandíbula y lateralización de mandíbula.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0127 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, ejercicio "Side to Side": Mover la lengua de lado a lado muy lento (5 segundos por trayecto) manteniendo la mandíbula estable y la lengua separada de los dientes.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0128 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, la terapia miofuncional es el "entrenamiento personalizado" frente a la "membresía del gimnasio" (hacer ejercicios solo).

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0129 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, en bebés, la OMT incluye masajes orales para ensanchar el paladar y técnicas de alimentación ("baby-led weaning") para evitar el empuje lingual causado por las cucharas tradicionales.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

---

<!-- archivo: expertos/soroush-zaghi/nariz-amigdalas.md -->
# Nariz y amígdalas

Ideas públicas de Soroush Zaghi sobre este tema, reconstruidas a partir de sus vídeos. **No es Zaghi hablando ni una guía clínica.** Cómo leer cada entrada: README. Entradas: 30.

## zag-0001 · Estudio citado · verificado en PubMed

El estudio de Coppelson y colaboradores (J Oral Maxillofac Surg 2023, con Zaghi como coautor) encontró que inclinar la cabeza hacia arriba 5 grados aumenta el área transversal mínima de la vía aérea en el CBCT alrededor de un 25% y 10 grados un 88%, mientras que inclinarla hacia abajo la reduce solo un 21% y un 23%; por eso Zaghi exige estandarizar la posición de la cabeza en el CBCT.

- Vídeo: [Dr. Soroush Zaghi at ALSC - Breathe and Thrive 2022, in Las Vegas, NV](https://www.youtube.com/watch?v=3fq6w2buIy0), minuto `PENDIENTE DE VERIFICAR`.
- Vídeo: [Updates from Dr. Soroush Zaghi - The Breathe Institute at ALSC Symposium 2024](https://www.youtube.com/watch?v=iGQlzOtT4C0), minuto `PENDIENTE DE VERIFICAR`.
- Vídeo: [FAirEST 6 + 4](https://www.youtube.com/watch?v=ckwLiTMb7wo), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2022.
- Estudio: PMID [36841260](https://pubmed.ncbi.nlm.nih.gov/36841260/), ficha 2023-coppelson-postura-cbct.md.
- Cita corta (transcripción automática, puede tener errores): «increasing NBC3 by +5 and +10° resulted in MCA changes of +25% and +88%, whereas a decrease in NBC3 by -5 and -10° results in MCA changes of -21% and -23% (resumen de PubMed).»

## zag-0010 · Estudio citado · discrepante con el estudio (ver discrepancias.md)

En 2021-2022, antes de publicarse el estudio, Zaghi presentó el efecto de la inclinación de la cabeza en el CBCT como simétrico («cinco grados arriba o abajo dan un 25% de diferencia»; con 10 grados, un 86%); el estudio publicado muestra que es asimétrico: hacia arriba +25% (5 grados) y +88% (10 grados), pero hacia abajo solo -21% y -23% (discrepancia con el estudio).

- Vídeo: [Dr. Zaghi on Research Principles (From TBI's Outlook at AAPMD Collaboration Cures Conference, 2021)](https://www.youtube.com/watch?v=vYQ1mv8Gdf0), minuto 2:35:23 (localizado en los subtítulos automáticos).
- Vídeo: [Dr. Soroush Zaghi at ALSC - Breathe and Thrive 2022, in Las Vegas, NV](https://www.youtube.com/watch?v=3fq6w2buIy0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2021.
- Estudio: PMID [36841260](https://pubmed.ncbi.nlm.nih.gov/36841260/), ficha 2023-coppelson-postura-cbct.md.
- Cita corta (transcripción automática, puede tener errores): «A small change of five degrees so if you're five degrees up or five degrees down you have a 25% difference in your results.»

## zag-0180 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, para respirar por la nariz se requieren dos condiciones: una vía nasal permeable y que el cuerpo medio de la lengua se eleve hacia el paladar para sellar la vía oral y desviar el flujo de aire hacia la nariz.

- Vídeo: [Full Lecture: Evaluation, Diagnosis, and Treatment of Tongue, Lip, & Buccal Ties, Dr. Soroush Zaghi](https://www.youtube.com/watch?v=iP3c-C9L9b0), minuto `PENDIENTE DE VERIFICAR`.
- Vídeo: [Pediatric Sleep Disordered Breathing and Maxillofacial Development with Soroush Zaghi](https://www.youtube.com/watch?v=eA1Yqbruw4g), minuto `PENDIENTE DE VERIFICAR`.

## zag-0181 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, la lengua funciona como un interruptor "On/Off": la postura lingual alta activa el circuito de respiración nasal; la postura baja activa el bucal.

- Vídeo: [Dr. Soroush Zaghi at Tongue Time 2026 in Zurich, Switzerland  (Full Lecture)](https://www.youtube.com/watch?v=y6VkQnMBBvc), minuto `PENDIENTE DE VERIFICAR`.
- Vídeo: [Long-term Implications of Untreated Tongue-Tie (Dr. Soroush Zaghi, The Breathe Institute)](https://www.youtube.com/watch?v=cuT6qrm5IT0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2026.

## zag-0182 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, es físicamente imposible en el 100% de los seres humanos respirar por la boca si la lengua está en posición de succión palatina (LPS) completa.

- Vídeo: [Tongue-Tie, Sleep, Breathing, and Myofunctional Therapy: New Research Updates. Dr. Zaghi at ALSC '20](https://www.youtube.com/watch?v=G9GrUw7YJD0), minuto `PENDIENTE DE VERIFICAR`.
- Vídeo: [Dr. Soroush Zaghi at Tongue Time 2026 in Zurich, Switzerland  (Full Lecture)](https://www.youtube.com/watch?v=y6VkQnMBBvc), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2026.

## zag-0183 · Opinión · sin verificar (dicho en vídeo)

Según Zaghi, si el freno lingual mantiene la lengua abajo, el paciente está "condenado" a ser un respirador bucal predominante, especialmente bajo esfuerzo físico.

- Vídeo: [Tongue-Tie, Sleep, Breathing, and Myofunctional Therapy: New Research Updates. Dr. Zaghi at ALSC '20](https://www.youtube.com/watch?v=G9GrUw7YJD0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2020.

## zag-0184 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, cribado inicial de 3 minutos de respiración nasal exclusiva (lip taping) en el consultorio. Si no lo logran, hay obstrucción orgánica.

- Vídeo: [Dr. Soroush Zaghi at ALSC - Breathe and Thrive 2022, in Las Vegas, NV](https://www.youtube.com/watch?v=3fq6w2buIy0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2022.

## zag-0185 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, el objetivo final del tratamiento es la respiración nasal continua y silenciosa el 96% del tiempo (basado en el umbral patológico del 10% de respiración bucal de Guilleminault).

- Vídeo: [Tongue-Tie, Sleep, Breathing, and Myofunctional Therapy: New Research Updates. Dr. Zaghi at ALSC '20](https://www.youtube.com/watch?v=G9GrUw7YJD0), minuto `PENDIENTE DE VERIFICAR`.
- Vídeo: [Long-term Implications of Untreated Tongue-Tie (Dr. Soroush Zaghi, The Breathe Institute)](https://www.youtube.com/watch?v=cuT6qrm5IT0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2020.

## zag-0186 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, clasificación de la respiración bucal: Leve (5-15% del tiempo), Moderada (>15%) y Severa (>35%).

- Vídeo: [Excerpts From - TBI Ambassador Update (December 2024). Now Available On-Demand!](https://www.youtube.com/watch?v=DshE1KHc9s0), minuto `PENDIENTE DE VERIFICAR`.
- Vídeo: [Long-term Implications of Untreated Tongue-Tie (Dr. Soroush Zaghi, The Breathe Institute)](https://www.youtube.com/watch?v=cuT6qrm5IT0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2024.

## zag-0187 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, la válvula nasal es la unión entre el cartílago lateral superior y el tabique; es el punto más estrecho y crítico para regular el flujo de aire.

- Vídeo: [Live Latera Nasal Valve Implant Procedure for Nasal Obstruction with Dr. Zaghi and 1 week Followup](https://www.youtube.com/watch?v=Cm7chrBRz14), minuto `PENDIENTE DE VERIFICAR`.

## zag-0190 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, latera: Implante absorbable (se disuelve en 12-18 meses) que actúa como un soporte mecánico para evitar el colapso dinámico de la válvula al inspirar.

- Vídeo: [Live Latera Nasal Valve Implant Procedure for Nasal Obstruction with Dr. Zaghi and 1 week Followup](https://www.youtube.com/watch?v=Cm7chrBRz14), minuto `PENDIENTE DE VERIFICAR`.

## zag-0193 · Experiencia clínica · sin verificar (dicho en vídeo)

Breathe RF: Protocolo propio de Zaghi que refina la técnica de radiofrecuencia para ser más rápida, precisa y con menos inflamación que el Vivaer estándar.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0196 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, la hipertrofia de cornetes suele ser secundaria a la respiración bucal crónica; los pulmones exigen aire húmedo y la mucosa nasal se inflama para compensar la sequedad.

- Vídeo: [Pediatric Sleep Disordered Breathing and Maxillofacial Development with Soroush Zaghi](https://www.youtube.com/watch?v=eA1Yqbruw4g), minuto `PENDIENTE DE VERIFICAR`.

## zag-0197 · Experiencia clínica · sin verificar (dicho en vídeo)

Zaghi realiza una "mini-septoplastia" de rutina en casi todos los casos de cirugía ortognática de mandíbula.

- Vídeo: [Advances in Surgical Technique with Dr. Kevin Coppelson - BreatheMAX - 10/28/24](https://www.youtube.com/watch?v=gsAggiqvgEY), minuto `PENDIENTE DE VERIFICAR`.

## zag-0198 · Experiencia clínica · sin verificar (dicho en vídeo)

Zaghi se sometió personalmente a una septorrinoplastia con injertos (spreader grafts) y cirugía de senos para tratar su propia obstrucción tras un trauma infantil.

- Vídeo: [Updates from Dr. Soroush Zaghi - The Breathe Institute at ALSC Symposium 2024](https://www.youtube.com/watch?v=iGQlzOtT4C0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2024.

## zag-0200 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, clasificación Brodsky (Tamaño): Grado 0 (extraídas), Grado 1 (ocupan <25% de la vía aérea), Grado 2 (25-50%), Grado 3 (51-75%) y Grado 4 (>75% / se tocan).

- Vídeo: [Pediatric Sleep Disordered Breathing and Maxillofacial Development with Soroush Zaghi](https://www.youtube.com/watch?v=eA1Yqbruw4g), minuto `PENDIENTE DE VERIFICAR`.
- Vídeo: [Tongue-Tie, Sleep, Breathing, and Myofunctional Therapy: New Research Updates. Dr. Zaghi at ALSC '20](https://www.youtube.com/watch?v=G9GrUw7YJD0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2020.

## zag-0201 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, tamaño vs Color: Amígdalas rojas = infección aguda; Amígdalas color bronce/tan = inflamación crónica, fibrosis y cicatrización.

- Vídeo: [Tonsils Size vs Color - Differences between acute and chronic tonsil hypertrophy (large tonsils)](https://www.youtube.com/watch?v=lfH43CDyG5I), minuto `PENDIENTE DE VERIFICAR`.

## zag-0202 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, amígdalas Exofíticas (crecen hacia la vía) vs Endofíticas (enterradas profundamente en el tejido del cuello).

- Vídeo: [Tonsils Size vs Color - Differences between acute and chronic tonsil hypertrophy (large tonsils)](https://www.youtube.com/watch?v=lfH43CDyG5I), minuto `PENDIENTE DE VERIFICAR`.

## zag-0203 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, ¿Se crece fuera de ellas?: No, los niños suelen "crecer alrededor" de las amígdalas grandes, deformando su cara (crecimiento vertical) y estrechando el paladar para poder respirar.

- Vídeo: [Can you grow out of large tonsils? Dr. Zaghi at The Breathe Institute discusses...](https://www.youtube.com/watch?v=iKMZzTYnTro), minuto `PENDIENTE DE VERIFICAR`.

## zag-0204 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, las amígdalas crónicamente inflamadas ya no proporcionan inmunidad innata, a diferencia de las que solo tienen hipertrofia simple.

- Vídeo: [Tonsils Size vs Color - Differences between acute and chronic tonsil hypertrophy (large tonsils)](https://www.youtube.com/watch?v=lfH43CDyG5I), minuto `PENDIENTE DE VERIFICAR`.

## zag-0205 · Estudio citado · sin verificar (dicho en vídeo)

Yoon, Liu et al. Demuestra que la expansión palatina rápida en niños puede reducir significativamente el tamaño de amígdalas y adenoides al restaurar la respiración nasal.

- Vídeo: [Long-term Implications of Untreated Tongue-Tie (Dr. Soroush Zaghi, The Breathe Institute)](https://www.youtube.com/watch?v=cuT6qrm5IT0), minuto `PENDIENTE DE VERIFICAR`.

## zag-0206 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, uso de Coblation (radiofrecuencia) para amigdalectomía: calienta el agua para ablar el tejido y sellar vasos, resultando en una recuperación mucho menos dolorosa.

- Vídeo: [Grade 4 Tonsils with Dr. Soroush Zaghi at The Breathe Institute + Pre and Post airway CBCT](https://www.youtube.com/watch?v=KyTUkhJhG9w), minuto `PENDIENTE DE VERIFICAR`.

## zag-0207 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, deja siempre un poco de tejido de amígdala lingual para preservar la función inmunitaria residual.

- Vídeo: [Grade 4 Tonsils with Dr. Soroush Zaghi at The Breathe Institute + Pre and Post airway CBCT](https://www.youtube.com/watch?v=KyTUkhJhG9w), minuto `PENDIENTE DE VERIFICAR`.

## zag-0208 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, la causa más común de obstrucción nasal en lactantes no es estructural, sino alergias por sensibilidad a proteínas de la leche o alimentos ingeridos por la madre que pasan al pecho.

- Vídeo: [Long-term Implications of Untreated Tongue-Tie (Dr. Soroush Zaghi, The Breathe Institute)](https://www.youtube.com/watch?v=cuT6qrm5IT0), minuto `PENDIENTE DE VERIFICAR`.

## zag-0209 · Opinión · sin verificar (dicho en vídeo)

Según Zaghi, la exposición al moho tóxico ambiental puede provocar el crecimiento recurrente de amígdalas y adenoides después de haber sido extirpadas quirúrgicamente.

- Vídeo: [Excerpts From - TBI Ambassador Update (December 2024). Now Available On-Demand!](https://www.youtube.com/watch?v=DshE1KHc9s0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2024.

## zag-0210 · Opinión · sin verificar (dicho en vídeo)

Según Zaghi, el moho causa neuroinflamación y deterioro cognitivo/emocional, aumentando el riesgo de infecciones y enfermedades cardiovasculares.

- Vídeo: [Excerpts From - TBI Ambassador Update (December 2024). Now Available On-Demand!](https://www.youtube.com/watch?v=DshE1KHc9s0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2024.

## zag-0211 · Estudio citado · sin verificar (dicho en vídeo)

Christian Guilleminault (1976). Primer reporte de apnea pediátrica y relación con hipertrofia de amígdalas/adenoides.

- Vídeo: [Dr. Soroush Zaghi at Tongue Time 2026 in Zurich, Switzerland  (Full Lecture)](https://www.youtube.com/watch?v=y6VkQnMBBvc), minuto `PENDIENTE DE VERIFICAR`.
- Vídeo: [Long-term Implications of Untreated Tongue-Tie (Dr. Soroush Zaghi, The Breathe Institute)](https://www.youtube.com/watch?v=cuT6qrm5IT0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2026.

## zag-0212 · Estudio citado · sin verificar (dicho en vídeo)

Villa et al. (2011/2014). Demuestra que sin reeducación miofuncional tras la cirugía de amígdalas, los niños recaen en la apnea debido a la persistencia del hábito de respiración bucal.

- Vídeo: [Pediatric Sleep Disordered Breathing and Maxillofacial Development with Soroush Zaghi](https://www.youtube.com/watch?v=eA1Yqbruw4g), minuto `PENDIENTE DE VERIFICAR`.
- Vídeo: [Tongue-Tie, Sleep, Breathing, and Myofunctional Therapy: New Research Updates. Dr. Zaghi at ALSC '20](https://www.youtube.com/watch?v=G9GrUw7YJD0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2020.

## zag-0213 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, protocolo de higiene nasal TBI: Lavados salinos diarios con productos como X-lear (con xilitol) y probióticos nasales para estabilizar la microbiota.

- Vídeo: [Breathe Myo Explained: Tongue Tie, Airway Health, Facial Development with Sandraluz Gonzalez](https://www.youtube.com/watch?v=ni2dO45jdbo), minuto `PENDIENTE DE VERIFICAR`.
- Vídeo: [Dr. Soroush Zaghi at ALSC - Breathe and Thrive 2022, in Las Vegas, NV](https://www.youtube.com/watch?v=3fq6w2buIy0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2022.

## zag-0616 · Opinión · sin verificar (dicho en vídeo)

Zaghi sostiene que la lengua funciona como un interruptor de la respiración nasal: la posición alta de la lengua facilita respirar por la nariz y la posición baja facilita respirar por la boca.

- Vídeo: [Dr. Soroush Zaghi at Tongue Time 2026 in Zurich, Switzerland  (Full Lecture)](https://www.youtube.com/watch?v=y6VkQnMBBvc), minuto 41:10 (localizado en los subtítulos automáticos).
- Año de la charla: 2026.
- Cita corta (transcripción automática, puede tener errores): «So we learned the tongue is an onoff switch for nasal breathing... What we’re saying is that high tongue position facilitates nasal breathing and low tongue position facilitates mouth breathing... In 100% of humans everywhere in the world you will […]»

---

<!-- archivo: expertos/soroush-zaghi/posoperatorio.md -->
# Posoperatorio y cicatrización

Ideas públicas de Soroush Zaghi sobre este tema, reconstruidas a partir de sus vídeos. **No es Zaghi hablando ni una guía clínica.** Cómo leer cada entrada: README. Entradas: 46.

## zag-0013 · Experiencia clínica · sin verificar (dicho en vídeo)

Según notas de NotebookLM sin cita literal, Zaghi infiltra Kenalog en el tejido cicatricial oral tras una frenuloplastia, una o dos veces, cuando la herida ya está cerrada (uno o dos meses después de la cirugía); no lo hace con la herida abierta, y lo considera contraindicado con inmunosupresión, mal estado general o infección fúngica activa, evitando además el derrame del producto en la boca. Las dosis no se recogen: no hay cita literal.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0314 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, la herida pasa por fases críticas: del día 1 al 7 es inflamación y granulación; del día 10 al mes ocurre la fase de contracción (donde el paciente siente más tensión); y de los 2 a los 9 meses ocurre la maduración y remodelación del colágeno, donde el tejido se vuelve elástico.

- Vídeo: [Functional Approach to Frenuloplasty: How We Do It - Dr. Soroush Zaghi](https://www.youtube.com/watch?v=C0kel5PNc7c), minuto `PENDIENTE DE VERIFICAR`.
- Vídeo: [Updates from Dr. Soroush Zaghi - The Breathe Institute at ALSC Symposium 2024](https://www.youtube.com/watch?v=iGQlzOtT4C0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2024.

## zag-0315 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, sanda Valcu-Pinkerton explica que durante la fase de contracción (alrededor del día 10), los pacientes a menudo se desaniman porque sienten que la lengua se "aprieta" de nuevo; es crucial asegurarles que es un proceso fisiológico normal y que deben ser perseverantes con los ejercicios.

- Vídeo: [Post-Op Wound Healing - Sanda Valcu-Pinkerton, The Breathe Institute](https://www.youtube.com/watch?v=puF6uKS8tTA), minuto `PENDIENTE DE VERIFICAR`.

## zag-0316 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, sanda Valcu-Pinkerton indica que en los primeros tres días no se deben realizar estiramientos manuales agresivos para no comprometer las suturas.

- Vídeo: [Post-Op Wound Healing - Sanda Valcu-Pinkerton, The Breathe Institute](https://www.youtube.com/watch?v=puF6uKS8tTA), minuto `PENDIENTE DE VERIFICAR`.

## zag-0317 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, en los días 1 a 3 tras la frenuloplastia (gestión de la inflamación) se recomienda hablar mucho, hacer "clics" linguales muy suaves (si no hay pain) y movimientos leves para movilizar la linfa y reducir el edema.

- Vídeo: [Post-Op Wound Healing - Sanda Valcu-Pinkerton, The Breathe Institute](https://www.youtube.com/watch?v=puF6uKS8tTA), minuto `PENDIENTE DE VERIFICAR`.

## zag-0318 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, amanda Ramirez (TBI) instruye a los pacientes a esperar de 3 a 5 días de dolor leve e inflamación, lo cual es el estándar esperado.

- Vídeo: [Functional Frenuloplasty Post Operative Instructions with Amanda at The Breathe Institute](https://www.youtube.com/watch?v=uQYOd_jWRv8), minuto `PENDIENTE DE VERIFICAR`.

## zag-0319 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, el lema es "úsalo o piérdelo": si la lengua no se mueve en rangos máximos, cicatrizará en una posición restringida.

- Vídeo: [Dr. Soroush Zaghi at ALSC - Breathe and Thrive 2022, in Las Vegas, NV](https://www.youtube.com/watch?v=3fq6w2buIy0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2022.

## zag-0321 · Experiencia clínica · sin verificar (dicho en vídeo)

Zaghi recomienda el "Sleeping Tongue Posture Hold" (especialmente en bebés): asegurar manualmente que la lengua mantenga el sello palatino para guiar la cicatrización hacia una postura alta.

- Vídeo: [Updates from Dr. Soroush Zaghi - The Breathe Institute at ALSC Symposium 2024](https://www.youtube.com/watch?v=iGQlzOtT4C0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2024.

## zag-0322 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, el protocolo posoperatorio estándar incluye ibuprofeno según necesidad. Las dosis y concentraciones no se recogen en esta base.

- Vídeo: [Functional Frenuloplasty Post Operative Instructions with Amanda at The Breathe Institute](https://www.youtube.com/watch?v=uQYOd_jWRv8), minuto `PENDIENTE DE VERIFICAR`.

## zag-0324 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, es opcional aplicar un gel anestésico tópico en una gasa bajo la lengua unos minutos antes de la frenuloplastia. Las dosis y concentraciones no se recogen en esta base.

- Vídeo: [Functional Frenuloplasty Post Operative Instructions with Amanda at The Breathe Institute](https://www.youtube.com/watch?v=uQYOd_jWRv8), minuto `PENDIENTE DE VERIFICAR`.

## zag-0325 · Experiencia clínica · sin verificar (dicho en vídeo)

Zaghi ahora promueve el uso de hielo (15 min puesto / 2 horas libre) en el área bajo la barbilla (submental) para reducir la necesidad de fármacos y controlar el edema.

- Vídeo: [Updates from Dr. Soroush Zaghi - The Breathe Institute at ALSC Symposium 2024](https://www.youtube.com/watch?v=iGQlzOtT4C0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2024.

## zag-0326 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, iniciar con alimentos fríos y suaves (smoothies, yogur, helado) para calmar la zona.

- Vídeo: [Functional Frenuloplasty Post Operative Instructions with Amanda at The Breathe Institute](https://www.youtube.com/watch?v=uQYOd_jWRv8), minuto `PENDIENTE DE VERIFICAR`.

## zag-0327 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, evitar alimentos muy calientes, picantes o ácidos, ya que pueden causar ardor en la herida abierta o sobre las suturas.

- Vídeo: [Functional Frenuloplasty Post Operative Instructions with Amanda at The Breathe Institute](https://www.youtube.com/watch?v=uQYOd_jWRv8), minuto `PENDIENTE DE VERIFICAR`.

## zag-0329 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, enjuagues bucales dos veces al día por dos semanas: se recomiendan fórmulas sin alcohol, ya sea con peróxido (Peroxyl), xilitol (Spry) o simplemente agua tibia con sal.

- Vídeo: [Functional Frenuloplasty Post Operative Instructions with Amanda at The Breathe Institute](https://www.youtube.com/watch?v=uQYOd_jWRv8), minuto `PENDIENTE DE VERIFICAR`.

## zag-0332 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, un ligero manchado de sangre (spotting) el primer día es normal.

- Vídeo: [Functional Frenuloplasty Post Operative Instructions with Amanda at The Breathe Institute](https://www.youtube.com/watch?v=uQYOd_jWRv8), minuto `PENDIENTE DE VERIFICAR`.

## zag-0334 · Experiencia clínica · sin verificar (dicho en vídeo)

Sangrado constante y activo que no se detiene con presión: requiere atención inmediata (aunque Zaghi reporta que con su técnica láser el riesgo es cercano a cero).

- Vídeo: [Functional Frenuloplasty Post Operative Instructions with Amanda at The Breathe Institute](https://www.youtube.com/watch?v=uQYOd_jWRv8), minuto `PENDIENTE DE VERIFICAR`.
- Vídeo: [Dr. Soroush Zaghi at ALSC - Breathe and Thrive 2022, in Las Vegas, NV](https://www.youtube.com/watch?v=3fq6w2buIy0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2022.

## zag-0335 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, hematoma inestable: una acumulación de sangre que sigue creciendo y causa dolor severo; requiere ser drenado o lavado.

- Vídeo: [Dr. Soroush Zaghi at ALSC - Breathe and Thrive 2022, in Las Vegas, NV](https://www.youtube.com/watch?v=3fq6w2buIy0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2022.

## zag-0336 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, numbness (entumecimiento) de la punta de la lengua que persiste más de dos semanas (ocurre en <5% de los casos y suele ser temporal).

- Vídeo: [Updates from Dr. Soroush Zaghi - The Breathe Institute at ALSC Symposium 2024](https://www.youtube.com/watch?v=iGQlzOtT4C0), minuto `PENDIENTE DE VERIFICAR`.
- Vídeo: [Functional Approach to Frenuloplasty: How We Do It - Dr. Soroush Zaghi](https://www.youtube.com/watch?v=C0kel5PNc7c), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2024.

## zag-0337 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, candidiasis (trush) o infección fúngica: puede ocurrir si se usa demasiado Kenalog (esteroide) o si el paciente está inmunosuprimido; se trata con trociscos de clotrimazol.

- Vídeo: [Updates from Dr. Soroush Zaghi - The Breathe Institute at ALSC Symposium 2024](https://www.youtube.com/watch?v=iGQlzOtT4C0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2024.

## zag-0338 · Estudio citado · verificado en PubMed

Zaghi et al. (2019), Laryngoscope Investigative Otolaryngology. En los primeros 348 casos (con técnica de tijeras), el dolor severo afectó al 45% de los pacientes y el sangrado al 12.6%.

- Vídeo: [Long-term Implications of Untreated Tongue-Tie (Dr. Soroush Zaghi, The Breathe Institute)](https://www.youtube.com/watch?v=cuT6qrm5IT0), minuto `PENDIENTE DE VERIFICAR`.
- Vídeo: [Dr. Soroush Zaghi at ALSC - Breathe and Thrive 2022, in Las Vegas, NV](https://www.youtube.com/watch?v=3fq6w2buIy0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2022.
- Estudio: PMID [31637291](https://pubmed.ncbi.nlm.nih.gov/31637291/), ficha 2019-zaghi-frenuloplastia-348.md.

## zag-0339 · Estudio citado · sin verificar (dicho en vídeo)

Zaghi et al. (2025/2026), International Journal of Orofacial Myology. Con la técnica refinada de láser CO2 y protocolos de preservación fascial, el dolor severo se redujo del 45% al 3.7% y el sangrado a niveles insignificantes.

- Vídeo: [Evolution Of Myofunctional Therapy, Lingual Frenuloplasty - Dr. Soroush Zaghi at ALSC 2026.](https://www.youtube.com/watch?v=nlFVT6PUaYc), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2026.

## zag-0340 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, la escala WHIMS mide la integración y maduración del tejido cicatricial; se utiliza para decidir si un paciente es candidato a intervenciones adicionales como inyecciones de Kenalog-10.

- Vídeo: [Updates from Dr. Soroush Zaghi - The Breathe Institute at ALSC Symposium 2024](https://www.youtube.com/watch?v=iGQlzOtT4C0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2024.

## zag-0341 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, la escala WHIMS (integración y maduración de la herida) se evalúa típicamente a los dos meses posoperatorios, que es cuando el tejido ha pasado por la fase de contracción y está en plena remodelación.

- Vídeo: [Updates from Dr. Soroush Zaghi - The Breathe Institute at ALSC Symposium 2024](https://www.youtube.com/watch?v=iGQlzOtT4C0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2024.

## zag-0342 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, 1-3 mm (2 puntos), 3-5 mm (1 punto), >5 mm o herida abierta (0 puntos).

- Vídeo: [Updates from Dr. Soroush Zaghi - The Breathe Institute at ALSC Symposium 2024](https://www.youtube.com/watch?v=iGQlzOtT4C0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2024.

## zag-0343 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, bien integrado/rosado (2 puntos), en progreso/integrándose (1 punto), blanco/distinto (0 puntos).

- Vídeo: [Updates from Dr. Soroush Zaghi - The Breathe Institute at ALSC Symposium 2024](https://www.youtube.com/watch?v=iGQlzOtT4C0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2024.

## zag-0344 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, totalmente suave (2 puntos), ligeramente elevada (1 punto), rugosa o significativamente irregular (0 puntos).

- Vídeo: [Updates from Dr. Soroush Zaghi - The Breathe Institute at ALSC Symposium 2024](https://www.youtube.com/watch?v=iGQlzOtT4C0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2024.

## zag-0345 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, flexible/buena (2 puntos), tensión moderada (1 punto), realmente tensa o contraída (0 puntos).

- Vídeo: [Updates from Dr. Soroush Zaghi - The Breathe Institute at ALSC Symposium 2024](https://www.youtube.com/watch?v=iGQlzOtT4C0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2024.

## zag-0346 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, buena movilidad (2 puntos), movilidad compensada (1 punto), movilidad limitada/restringida (0 puntos).

- Vídeo: [Updates from Dr. Soroush Zaghi - The Breathe Institute at ALSC Symposium 2024](https://www.youtube.com/watch?v=iGQlzOtT4C0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2024.

## zag-0347 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, una puntuación de 7 a 8 se considera un "buen" resultado de cicatrización; un 10 es la perfección absoluta.

- Vídeo: [Updates from Dr. Soroush Zaghi - The Breathe Institute at ALSC Symposium 2024](https://www.youtube.com/watch?v=iGQlzOtT4C0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2024.

## zag-0348 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, si la puntuación es inferior a 5, el paciente requiere atención especial o múltiples rondas de Kenalog para romper el tejido fibroso.

- Vídeo: [Updates from Dr. Soroush Zaghi - The Breathe Institute at ALSC Symposium 2024](https://www.youtube.com/watch?v=iGQlzOtT4C0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2024.

## zag-0349 · Experiencia clínica · sin verificar (dicho en vídeo)

El Dr. Zaghi utiliza dos longitudes de onda principales: 800 nanómetros (luz roja) para tratar la inflamación y 1064 nanómetros (infrarrojo cercano) para trabajar a nivel de la fascia.

- Vídeo: [Updates from Dr. Soroush Zaghi - The Breathe Institute at ALSC Symposium 2024](https://www.youtube.com/watch?v=iGQlzOtT4C0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2024.

## zag-0350 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, la terapia de luz roja funciona aportando energía a las mitocondrias, lo que mejora la función celular y acelera la recuperación post-quirúrgica.

- Vídeo: [Updates from Dr. Soroush Zaghi - The Breathe Institute at ALSC Symposium 2024](https://www.youtube.com/watch?v=iGQlzOtT4C0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2024.

## zag-0351 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, la fotobiomodulación se aplica inmediatamente después de la frenuloplastia para minimizar el dolor y la necesidad de narcóticos o esteroides.

- Vídeo: [Evolution Of Myofunctional Therapy, Lingual Frenuloplasty - Dr. Soroush Zaghi at ALSC 2026.](https://www.youtube.com/watch?v=nlFVT6PUaYc), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2026.

## zag-0352 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, en pacientes hipermóviles o con tensión crónica, la PBM ayuda a relajar la musculatura del cuello y hombros tras la liberación lingual.

- Vídeo: [Updates from Dr. Soroush Zaghi - The Breathe Institute at ALSC Symposium 2024](https://www.youtube.com/watch?v=iGQlzOtT4C0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2024.

## zag-0353 · Experiencia clínica · sin verificar (dicho en vídeo)

[EXPERIENCIA CLÍNICA (Dr. Zaghi citando a un colega): Se ha reportado que el uso de la longitud de onda de 1064 nm puede llegar a "derretir" frenillos bucales (buckal ties) tras tres sesiones, evitando en algunos casos la cirugía. INFERENCIA FUERTE]. (Vídeo: Dr. Soroush Zaghi at Tongue Time 2026).

- Vídeo: [Dr. Soroush Zaghi at Tongue Time 2026 in Zurich, Switzerland  (Full Lecture)](https://www.youtube.com/watch?v=y6VkQnMBBvc), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2026.

## zag-0354 · Experiencia clínica · sin verificar (dicho en vídeo)

La técnica "Oralase" (especialidad de la Dra. Nora Gadisy Zaghi) utiliza el láser de 1064 nm para liberar restricciones de la fascia intraoral en pacientes que sienten tensión generalizada incluso después de la cirugía.

- Vídeo: [Updates from Dr. Soroush Zaghi - The Breathe Institute at ALSC Symposium 2024](https://www.youtube.com/watch?v=iGQlzOtT4C0), minuto `PENDIENTE DE VERIFICAR`.
- Vídeo: [Evolution Of Myofunctional Therapy, Lingual Frenuloplasty - Dr. Soroush Zaghi at ALSC 2026.](https://www.youtube.com/watch?v=nlFVT6PUaYc), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2026.

## zag-0355 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, la serrapeptasa actúa "comiendo" o disolviendo el colágeno tipo 3 (tejido de granulación/velcro) que causa la contracción excesiva de la herida durante la segunda semana.

- Vídeo: [Updates from Dr. Soroush Zaghi - The Breathe Institute at ALSC Symposium 2024](https://www.youtube.com/watch?v=iGQlzOtT4C0), minuto `PENDIENTE DE VERIFICAR`.
- Vídeo: [Serrapeptase Protocol for addressing  pain and inflammation - with Dr. Soroush Zaghi at TBI](https://www.youtube.com/watch?v=jvAdRMXr3XE), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2024.

## zag-0356 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, la serrapeptasa (enzima de gusano de seda) se aplica por vía tópica bajo la lengua usando el contenido de una cápsula pura, sin aditivos. Las dosis y concentraciones no se recogen en esta base.

- Vídeo: [Serrapeptase Protocol for addressing  pain and inflammation - with Dr. Soroush Zaghi at TBI](https://www.youtube.com/watch?v=jvAdRMXr3XE), minuto `PENDIENTE DE VERIFICAR`.

## zag-0357 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, la serrapeptasa se usa a diario durante la semana 2 y la semana 4 posoperatoria para mantener la flexibilidad del tejido antes de los ejercicios.

- Vídeo: [Evolution Of Myofunctional Therapy, Lingual Frenuloplasty - Dr. Soroush Zaghi at ALSC 2026.](https://www.youtube.com/watch?v=nlFVT6PUaYc), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2026.

## zag-0358 · Experiencia clínica · sin verificar (dicho en vídeo)

El Dr. Zaghi aclara que, aunque funciona muy bien, él no la prescribe formalmente en su clínica por no pasar el "Newspaper Test" (está etiquetada como suplemento y no debe abrirse según el fabricante), pero la menciona como una opción que los pacientes traen y que ha demostrado eficacia clínica.

- Vídeo: [Updates from Dr. Soroush Zaghi - The Breathe Institute at ALSC Symposium 2024](https://www.youtube.com/watch?v=iGQlzOtT4C0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2024.

## zag-0359 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, en bebés, existe riesgo de aspiración si se vierte el polvo; se debe aplicar humedeciendo una gasa y frotándola suavemente en la herida.

- Vídeo: [Updates from Dr. Soroush Zaghi - The Breathe Institute at ALSC Symposium 2024](https://www.youtube.com/watch?v=iGQlzOtT4C0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2024.

## zag-0360 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, prefiere Kenalog-10 porque viene listo para usar y es «limpio», aunque también puede diluirse Kenalog-40, más económico. Las dosis y concentraciones no se recogen en esta base.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0361 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, el producto no debe refrigerarse porque precipita; debe mantenerse a temperatura ambiente y agitarse bien antes de la inyección.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0617 · Estudio citado · sin verificar (dicho en vídeo)

Con la técnica refinada (láser y examen más preciso), Zaghi reporta que el dolor posoperatorio severo bajó del 45% de su serie de 2019 al 3.7%; el dato de 2024-2025 procede de una serie propia aún no verificada.

- Vídeo: [Updates from Dr. Soroush Zaghi - The Breathe Institute at ALSC Symposium 2024](https://www.youtube.com/watch?v=iGQlzOtT4C0), minuto 1:15:42 (localizado en los subtítulos automáticos).
- Año de la charla: 2024.
- Cita corta (transcripción automática, puede tener errores): «Our prior way that we were doing this was associated with a lot of complications... 45% of patients had pain... Since that time I’ve moved to an approach where we’re using exclusive we’re using like laser and more refined examination […]»

## zag-0621 · Experiencia clínica · sin verificar (dicho en vídeo)

Tras una frenuloplastia con cierre por sutura, Zaghi no indica estiramientos manuales de la herida: el paciente solo moviliza la lengua y mantiene la succión palatina; no aplica esto a heridas abiertas por segunda intención, donde otros clínicos como Baxter sí estiran.

- Vídeo: [Functional Approach to Frenuloplasty: How We Do It - Dr. Soroush Zaghi](https://www.youtube.com/watch?v=C0kel5PNc7c), minuto 34:15 (localizado en los subtítulos automáticos).
- Cita corta (transcripción automática, puede tener errores): «We don't do any manual wound healing we just mobilize the tongue have them holding the suction hold and that's the post-operative... as opposed to the diamond that has to kind of pull in that you have to stretch this»

## zag-0622 · Experiencia clínica · sin verificar (dicho en vídeo)

Zaghi ahora usa menos puntos de sutura y pegamento PeriAcryl entre ellos para reducir la inflamación del hilo; el pegamento se aplica en puntos separados (como botones) y no en línea continua.

- Vídeo: [Updates from Dr. Soroush Zaghi - The Breathe Institute at ALSC Symposium 2024](https://www.youtube.com/watch?v=iGQlzOtT4C0), minuto 1:21:26 (localizado en los subtítulos automáticos).
- Año de la charla: 2024.
- Cita corta (transcripción automática, puede tener errores): «Fewer sutures than before and between the sutures I'm using periacryl glue... the sutures introduce inflammation... a couple of sutures in periacryl glue we get great healing... the periacryl glue is like really helpful especially if you get into bleeding»

---

<!-- archivo: expertos/soroush-zaghi/README.md -->
# Soroush Zaghi: sus ideas públicas, con su vídeo

Soroush Zaghi es otorrinolaringólogo y cirujano de sueño y vía aérea, fundador de The Breathe Institute (Los Ángeles). Es coautor de las escalas de movilidad lingual TRMR que usa esta biblioteca (Yoon 2017, Zaghi 2021).

**Qué es esta carpeta.** Una reconstrucción de lo que Zaghi dice en público, sobre todo en sus vídeos de YouTube. Cada afirmación lleva el vídeo del que sale, con enlace. **No es Zaghi hablando, no habla en su nombre y no es una guía clínica.** Lo que dice un experto en un vídeo es opinión de experto: no equivale a un estudio (ver AGENTS.md, regla 2).

## De dónde sale

1. Se cargaron 100 fuentes públicas de The Breathe Institute (99 vídeos y su web) en un cuaderno de NotebookLM, en agosto y septiembre de 2026.
2. Se le hicieron preguntas por temas y se pasó cada respuesta a una base de afirmaciones, una por línea, con su tipo, su vídeo, su año y su PMID si cita un estudio.
3. Cada estudio citado se buscó en PubMed. Resultado en estudios-citados.md. Los casos en que lo que dice Zaghi no cuadra con el artículo están en discrepancias.md.
4. Para esta versión pública se quitaron: testimonios y casos de pacientes (también los de su propia familia), vídeos de rutinas personales del equipo y tutoriales de gestión. De las 623 afirmaciones de la extracción quedan 563. Las que hablan de fármacos o anestesia se mantienen, pero sin dosis: la extracción no las recoge. No hay transcripciones: solo resúmenes propios y citas cortas, porque los vídeos tienen la licencia estándar de YouTube y no permiten copiarlos.

## Cómo leer cada entrada

- **Tipo:** `Estudio citado` (Zaghi cita un trabajo), `Experiencia clínica` (lo que hace o ve en consulta) u `Opinión`.
- **Estado:** `verificado en PubMed` (el estudio existe y la cifra cuadra con el resumen), `sin verificar (dicho en vídeo)` o `discrepante`. Casi todo está sin verificar: es lo que dice en vídeo.
- **Vídeo:** título y enlace. Cuando la extracción no guardó el vídeo, pone `PENDIENTE DE VERIFICAR`.
- **Minuto:** en 15 entradas se localizó en los subtítulos automáticos de YouTube, buscando la cita literal (puede variar unos segundos). En el resto pone `PENDIENTE DE VERIFICAR`. Para encontrarlo: abrir el vídeo, pulsar «Mostrar transcripción» y buscar una palabra clave en inglés.
- **Cita corta:** cuando la hay, sale de la transcripción automática y puede tener errores de reconocimiento (por ejemplo «Lchnowski» por Lichnowska).
- Lo que dicen otras personas que aparecen en los vídeos (Coppelson, Sandraluz Gonzalez, Katie Romero) se atribuye a ellas, no a Zaghi.

## Archivos

- respuestas-a-criticas.md: qué dice Zaghi ante las críticas más habituales, al lado de lo que dice la evidencia de esta biblioteca. **Empieza por aquí.**
- Por temas: anquiloglosia, frenuloplastia, posoperatorio, terapia miofuncional, reglas de decisión, lo que rechaza, contradicciones y cambios de postura, investigación y ética, marcos de razonamiento, fascia, desarrollo maxilofacial, sueño y apnea, nariz y amígdalas, hipermovilidad, ambiente y alergias, estilo de vida, dieta y rutinas, ideas que aparecen una sola vez, otros temas.
- zaghi.jsonl: las mismas afirmaciones en formato de datos, una por línea, para que una IA las lea.
- estudios-citados.md, discrepancias.md y referencias-de-zaghi.md (bibliografía de 14 artículos suyos de acceso abierto).
- fuentes-videos.md: los vídeos citados, con su enlace.

## Cómo razona Zaghi (síntesis propia)

1. **Forma y función se condicionan.** Busca la causa (anatomía, tono, espacio, hábitos, ambiente) antes de operar. Cortar el frenillo es solo un paso.
2. **Lengua arriba, labios sellados, respiración nasal** es el objetivo funcional. Sostiene que una lengua restringida puede ir con paladar estrecho, nariz obstruida y peor vía aérea. Es su modelo; la causalidad no está demostrada (ver O-002).
3. **Atadura, tono y espacio**, y desde 2024 la hipermovilidad como cuarta variable. Antes de liberar comprueba que haya sitio para la lengua.
4. **Mide, no solo mira.** Valora el frenillo en cinco dimensiones: longitud de lengua libre, movilidad de la punta (TRMR-TIP), succión palatina (TRMR-LPS), compensaciones y tensión al tacto. En consulta hoy prioriza la maniobra de sujetar el suelo de la boca y reserva el TRMR sobre todo para investigación (contradicciones, zag-0569 y zag-0623).
5. **Cirugía mínima y rehabilitación.** Terapia miofuncional antes y después. Técnica que conserva la fascia y cierre con sutura.
6. **Epistemología.** Repite que la ausencia de evidencia no es evidencia de ausencia y señala sesgos de medición, de publicación y de confirmación. Sus resultados son a menudo serie propia sin publicar.
7. **Equipo.** Trabaja con terapeutas miofuncionales, ortodoncistas, cirujanos maxilofaciales, otorrinos, fisioterapeutas y especialistas en sueño, y deriva según la causa principal.

## Límites

- Casi todas las afirmaciones están sin verificar: son lo que Zaghi dice en vídeo.
- La transcripción automática y NotebookLM introducen errores. De 16 discrepancias revisadas, 1 era un exceso de Zaghi y 10 eran errores de NotebookLM o de la transcripción (discrepancias.md).
- Hay temas con poca cobertura. Si algo no está aquí, no se le puede atribuir una postura a Zaghi.
- Zaghi tiene interés profesional en la frenuloplastia, la formación de clínicos y los instrumentos que diseña. Es coautor de varios estudios que cita. Conviene tenerlo en cuenta al leerle, igual que con cualquier experto.

---

<!-- archivo: expertos/soroush-zaghi/referencias-de-zaghi.md -->
# Referencias de los artículos de Zaghi (Nivel 2)

Extraídas del texto completo (XML de PubMed Central) de 14 artículos suyos de acceso abierto (los XML no se incluyen). Cruce con estudios-citados.md (lo que menciona en los vídeos).

- Artículos leídos: **14**. Referencias totales: 500. Referencias distintas: **444**.
- Repetidas en 2 o más artículos: **44**.
- Cuatro artículos suyos son de neuromodulación (tDCS, dolor) y uno de fascitis necrotizante: no hablan de sueño; sus referencias se listan pero no entran en el cruce con los vídeos, que son de sueño, lengua y vía aérea.

## Lectura del cruce (tres líneas)

1. De las 244 referencias distintas de sus 9 artículos de sueño, vía aérea y lengua, solo 36 (15%) también salen en los vídeos; 208 (85%) solo están en los artículos. Lo que Zaghi cita de viva voz (Camacho 2015, Yoon 2017, Guilleminault, Kotlow, Mills, Sullivan) es un subconjunto pequeño de lo que sostiene sus papers.
2. Lo más repetido entre sus artículos (Camacho sobre clasificación de cornetes, 5 artículos; Yoon 2017 de escalas de movilidad, 4; Camacho 2015 de terapia miofuncional, 4) refleja su trayectoria en cirugía del sueño y vía aérea nasal, no la lengua; esa parte apenas se menciona en los vídeos.
3. Los estudios que solo aparecen en los vídeos (Andrews, Boyd, Rocabado, Salt 2021, Vivaer, revisión retrospectiva de 2011) no están entre las referencias de sus artículos. La lista de "solo en vídeos" es aproximada.

**Límites:** son 14 artículos con texto completo de los 74 que tiene; 5 son de otro tema. El cruce usa PMID o apellido + año, así que puede fallar con apellidos comunes o referencias sin año.

## Artículos leídos

| PMID | Año | Título | Tema | Nº referencias |
|---|---|---|---|---|
| 20051219 | 2010 | Noninvasive brain stimulation with high-frequency and low-intensity repetitive t | neuromodulación | 46 |
| 20585474 | 2009 | Brain stimulation for the treatment of pain: A review of costs, clinical effects | neuromodulación | 51 |
| 21170277 | 2009 | Efficacy of anodal transcranial direct current stimulation (tDCS) for the treatm | neuromodulación | 47 |
| 22512348 | 2012 | tDCS-induced analgesia and electrical fields in pain-related neural networks in  | neuromodulación | 65 |
| 22675644 | 2012 | Necrotizing Fasciitis Associated with Staphylococcus lugdunensis. | otro tema (fascitis necrotizante) | 11 |
| 26798519 | 2015 | Nasal Expiratory Positive Airway Pressure Devices (Provent) for OSA: A Systemati | sueño / vía aérea / lengua | 40 |
| 26881088 | 2016 | Five-Minute Awake Snoring Test for Determining CPAP Pressures (Five-Minute CPAP  | sueño / vía aérea / lengua | 27 |
| 26904126 | 2016 | Inferior Turbinate Size and CPAP Titration Based Treatment Pressures: No Associa | sueño / vía aérea / lengua | 15 |
| 26925105 | 2016 | Mini Tracheostomy for Obstructive Sleep Apnea: An Evidence Based Proposal. | sueño / vía aérea / lengua | 52 |
| 27293885 | 2016 | Predictors of Nasal Obstruction: Quantification and Assessment Using Multiple Gr | sueño / vía aérea / lengua | 10 |
| 31001444 | 2019 | Lingual and Maxillary Labial Frenuloplasty with Myofunctional Therapy as a Treat | sueño / vía aérea / lengua | 22 |
| 31637291 | 2019 | Lingual frenuloplasty with myofunctional therapy: Exploring safety and efficacy  | sueño / vía aérea / lengua | 50 |
| 33386612 | 2021 | Assessment of posterior tongue mobility using lingual-palatal suction: Progress  | sueño / vía aérea / lengua | 33 |
| 39336841 | 2024 | A Prospective Randomized Control Trial of Lingual Frenuloplasty with Myofunction | sueño / vía aérea / lengua | 31 |

## Cruce con los vídeos (solo artículos de sueño, vía aérea y lengua)

- Referencias distintas en esos artículos: 244.
- solo en papers: 208, en papers y en vídeos: 36.
- Coincidencia por PMID o por apellido + año dentro de una fila de estudios-citados.md. Es una coincidencia aproximada; puede dar falsos positivos con apellidos comunes.
- **Solo en vídeos** (mencionados en estudios-citados.md y que no aparecen entre las referencias de esos artículos): 11 entradas, listadas al final.

## Repetidas en 2 o más artículos

| Artículos | PMID | DOI | Referencia | Cruce |
|---|---|---|---|---|
| 5 | 25215619 | 10.1002/lary.24923 | 40CamachoM.ZaghiS.CertalV.Inferior turbinate classification system, grades 1 to 4: development and validation studyThe Laryngoscope2015125229630210.1002/lary.249232-s2.0- | en papers y en vídeos |
| 4 | 28097623 | 10.1007/s11325-016-1452-7 | 20YoonA.ZaghiS.WeitzmanR.Toward a functional definition of ankyloglossia: validating current grading scales for lingual frenulum length and tongue mobility in 1052 subjec | en papers y en vídeos |
| 4 | 25348130 | 10.5665/sleep.4652 | 2CamachoM.CertalV.AbdullatifJ.Myofunctional therapy to treat obstructive sleep apnea: a systematic review and meta-analysisSleep201538566967510.5665/sleep.465225348130PMC | en papers y en vídeos |
| 3 | 27730205 | 10.1183/23120541.00043-2016 | 13GuilleminaultC.HuseniS.LoL.A frequent phenotype for paediatric sleep apnoea: short lingual frenulumERJ Open Research20162310.1183/23120541.00043-20162-s2.0-85017434224P | en papers y en vídeos |
| 3 | 25325439 | 10.5665/sleep.4414 | 27CamachoM.RiazM.CapassoR.The effect of nasal surgery on continuous positive airway pressure device use and therapeutic treatment pressures: a systematic review and meta- | en papers y en vídeos |
| 3 | 6112294 | 10.1016/s0140-6736(81)92140-1 | 2SullivanC. E.IssaF.Berthon-JonesM.EvesL.Reversal of obstructive sleep apnoea by continuous positive airway pressure applied through the naresThe Lancet198131782258628651 | en papers y en vídeos |
| 3 | 17133529 | 10.1002/art.22195 | 49FregniFGimenesRValleACFerreiraMJRochaRRNatalleLA randomized, sham-controlled, proof of principle study of transcranial direct current stimulation for the treatment of p | fuera de tema |
| 3 | 30701608 | 10.1002/ca.23343 | 50 Mills N , Pransky SM , Geddes DT , Mirjalili SA . What is a tongue tie? Defining the anatomy of the in‐situ lingual frenulum. Clin Anat 2019 Available at: https://onli | en papers y en vídeos |
| 2 | 17351536 | 10.1016/s0035-3787(07)90388-4 | 11DuquetteMRoyMLeporeFPeretzIRainvillePCerebral mechanisms involved in the interaction between pain and emotionRev Neurol (Paris)20071632169791735153610.1016/s0035-3787(0 | fuera de tema |
| 2 | 32283998 | 10.1177/0194599820915457 | 12 Messner AH , Walsh J , Rosenfeld RM , et al. Clinical consensus statement: ankyloglossia in children. Otolaryngol‐Head Neck Surg. 2020;162(5):597–611.3228399810.1177/0 | en papers y en vídeos |
| 2 | 17986164 | 10.1111/j.1533-2500.2007.00152.x | 14RoizenblattSFregniFGimenezRWetzelTRigonattiSPTufikSSite-specific effects of transcranial direct current stimulation on sleep and pain in fibromyalgia: a randomized, sha | fuera de tema |
| 2 | 14990910 | 10.1016/j.otohns.2003.09.016 | 14StewartM. G.WitsellD. L.SmithT. L.WeaverE. M.YuehB.HannleyM. T.Development and validation of the Nasal Obstruction Symptom Evaluation (NOSE) scaleOtolaryngology,Head an | solo en papers |
| 2 | 10635253 | , | 17 Kotlow LA . Ankyloglossia (tongue‐tie): a diagnostic and treatment quandary. Quintessence Int. 1999;30.259–262.10635253 | en papers y en vídeos |
| 2 | 26371602 | 10.1002/lary.25589 | 17TorreC.CamachoM.LiuS. Y.HuonL. K.CapassoR.Epiglottis collapse in adult obstructive sleep apnea: a systematic reviewThe Laryngoscope201510.1002/lary.2558926371602 | solo en papers |
| 2 | 23716022 | 10.1007/s11325-013-0864-x | 19HsiaJ. C.CamachoM.CapassoR.Snoring exclusively during nasal breathing: a newly described respiratory pattern during sleepSleep & Breathing201418115916410.1007/s11325-01 | solo en papers |
| 2 | 10990547 | 10.1111/j.1469-7793.2000.t01-1-00633.x | 19NitscheMAPaulusWExcitability changes induced in the human motor cortex by weak transcranial direct current stimulationJ Physiol2000527363391099054710.1111/j.1469-7793.2 | fuera de tema |
| 2 | 10591345 | 10.1097/00005537-199912000-00002 | 26FriedmanM.TanyeriH.La RosaM.Clinical predictors of obstructive sleep apneaThe Laryngoscope1999109121901190710.1097/00005537-199912000-000022-s2.0-003270606510591345 | solo en papers |
| 2 | 16427357 | 10.1016/j.clinph.2005.12.003 | 26GandigaPCHummelFCCohenLGTranscranial DC stimulation (tDCS): a tool for double-blind sham-controlled clinical studies in brain stimulationClin Neurophysiol20061174845501 | fuera de tema |
| 2 | 17444810 | 10.1146/annurev.bioeng.9.061206.133100 | 29WagnerTValero-CabreAPascual-LeoneANoninvasive human brain stimulationAnnu Rev Biomed Eng20079527651744481010.1146/annurev.bioeng.9.061206.133100 | fuera de tema |
| 2 | 24154748 | 10.1177/0194599813509959 | 2CertalV.NishinoN.CamachoM.CapassoR.Reviewing the systematic reviews in OSA surgeryOtolaryngology,Head and Neck Surgery2013149681782910.1177/019459981350995924154748 | en papers y en vídeos |
| 2 | 16762592 | 10.1016/j.clinph.2006.04.009 | 30MirandaPCLomarevMHallettMModeling the current distribution during transcranial direct current stimulationClin Neurophysiol20061177162391676259210.1016/j.clinph.2006.04. | fuera de tema |
| 2 | 11723286 | 10.1212/wnl.57.10.1899 | 32NitscheMAPaulusWSustained excitability elevations induced by transcranial DC motor cortex stimulation in humansNeurology2001571018999011172328610.1212/wnl.57.10.1899 | fuera de tema |
| 2 | 17726271 | , | 39BoggioPSNunesARigonattiSPNitscheMAPascual-LeoneAFregniFRepeated sessions of noninvasive brain DC stimulation is associated with motor function improvement in stroke pat | fuera de tema |
| 2 | 16002441 | 10.1113/jphysiol.2005.092429 | 39NitscheMASeeberAFrommannKKleinCCRochfordCNitscheMSModulating parameters of excitability during and after transcranial direct current stimulation of the human motor cort | fuera de tema |
| 2 | 26116307 | 10.1016/j.jcms.2015.05.015 | 3CamachoM.LiuS. Y.CertalV.CapassoR.PowellN. B.RileyR. W.Large maxillomandibular advancements for obstructive sleep apnea: an operative technique evolved over 30 yearsJour | en papers y en vídeos |
| 2 | 28859912 | 10.1016/j.jpedp.2017.09.017 | 3TorreC.GuilleminaultC.Establishment of nasal breathing should be the ultimate goal to secure adequate craniofacial and airway development in childrenJornal de Pediatria  | solo en papers |
| 2 | 16045502 | 10.1111/j.1460-9568.2005.04233.x | 41LangNSiebnerHRWardNSLeeLNitscheMAPaulusWHow does transcranial DC stimulation of the primary motor cortex alter regional neuronal activity in the human brain?Eur J Neuro | fuera de tema |
| 2 | 18717717 | 10.1111/j.1468-1331.2008.02270.x | 45BoggioPSZaghiSLopesMFregniFModulatory effects of anodal transcranial direct current stimulation on perception and pain thresholds in healthy volunteersEur J Neurolin pr | fuera de tema |
| 2 | 15897507 | 10.1136/jnnp.2004.055806 | 45KhedrEMKotbHKamelNFLonglasting antalgic effects of daily sessions of repetitive transcranial magnetic stimulation in central and peripheral neuropathic painJ Neurol Neu | fuera de tema |
| 2 | 26595832 | 10.4317/medoral.20736 | 46 Ferrés‐Amat E , Pastor‐Vera T , Ferrés‐Amat E , Mareque‐Bueno J , Prats‐Armengol J , Ferrés‐Padró E . Multidisciplinary management of ankyloglossia in childhood. Treat | solo en papers |
| 2 | 17553993 | 10.1523/jneurosci.0314-07.2007 | 46FecteauSPascual-LeoneAZaldDHLiguoriPTheoretHBoggioPSActivation of prefrontal cortex by transcranial direct current stimulation reduces appetite for risk during ambiguou | fuera de tema |
| 2 | 12748571 | 10.1016/s0194-59980300258-4 | 47 Lalakea ML , Messner AH . Ankyloglossia: the adolescent and adult perspective. Otolaryngol Head Neck Surg 2003;128:746–752.1274857110.1016/S0194-59980300258-4 | solo en papers |
| 2 | 17239806 | 10.1016/s1474-4422(07)70032-7 | 47FregniFFreedmanSPascual-LeoneARecent advances in the treatment of chronic pain with non-invasive brain stimulation techniquesLancet Neurol20076188911723980610.1016/S147 | fuera de tema |
| 2 | 12809329 | 10.1016/s0031-3955(03)00029-4 | 48 Lalakea ML , Messner AH . Ankyloglossia: does it matter? Pediatr Clin North Am 2003;50:381–397.1280932910.1016/s0031-3955(03)00029-4 | solo en papers |
| 2 | 15999258 | 10.1007/s00221-005-2334-6 | 48FregniFBoggioPSNitscheMBermpohlFAntalAFeredoesEAnodal transcranial direct current stimulation of prefrontal cortex enhances working memoryExp Brain Res20051661233015999 | fuera de tema |
| 2 | 18541887 | 10.1212/01.wnl.0000314649.38527.93 | 4LimaMCFregniFMotor cortex stimulation for chronic pain: systematic review and meta-analysis of the literatureNeurology200870242329371854188710.1212/01.wnl.0000314649.385 | fuera de tema |
| 2 | 28994495 | 10.1111/ocr.12206 | 5 Yoon A , Zaghi S , Ha S , Law C , Guilleminault C , Liu S . Ankyloglossia as a risk factor for maxillary hypoplasia and soft palate elongation: a functional–morphologic | en papers y en vídeos |
| 2 | 16564618 | 10.1016/j.pain.2006.02.023 | 50FregniFBoggioPSLimaMCFerreiraMJWagnerTRigonattiSPA sham-controlled, phase II trial of transcranial direct current stimulation for the treatment of central pain in traum | fuera de tema |
| 2 | 24549987 | 10.1002/lary.24433 | 5CamachoM.CertalV.BrietzkeS. E.HoltyJ.-E. C.GuilleminaultC.CapassoR.Tracheostomy as treatment for adult obstructive sleep apnea: a systematic review and meta-analysisLary | en papers y en vídeos |
| 2 | 18457536 | 10.1586/14737175.8.5.799 | 5LefaucheurJPUse of repetitive transcranial magnetic stimulation in pain reliefExpert Rev Neurother2008857998081845753610.1586/14737175.8.5.799 | fuera de tema |
| 2 | 24474491 | 10.5935/1808-8694.20130139 | 6CamachoM.CertalV.CapassoR.Comprehensive review of surgeries for obstructive sleep apnea syndromeBrazilian Journal of Otorhinolaryngology201379678078810.5935/1808-8694.20 | en papers y en vídeos |
| 2 | 31074141 | 10.1111/ocr.12277 | 7 D'Onofrio L . Oral dysfunction as a cause of malocclusion. Orthod Craniofac Res. 2019;22:43‐48.3107414110.1111/ocr.12277PMC6851783 | solo en papers |
| 2 | 31637291 | 10.1002/lio2.297 | 9 Zaghi S , Valcu‐Pinkerton S , Jabara M ,et al. Lingual frenuloplasty with myofunctional therapy: exploring safety and efficacy in 348 cases. Laryngoscope Investig Otola | en papers y en vídeos |
| 2 | 26294977 | 10.1155/2015/293868 | 9CamachoM.RiazM.TahooriA.CertalV.KushidaC. A.Mathematical equations to predict positive airway pressures for obstructive sleep apnea: a systematic reviewSleep Disorders20 | en papers y en vídeos |

## Referencias de sueño, vía aérea y lengua (una vez)

| PMID | DOI | Referencia | Cruce |
|---|---|---|---|
| , | , | 1 Fernando C . Tongue Tie,From Confusion to Clarity: A Guide to the Diagnosis and Treatment of Ankyloglossia. New York, NY, USA: Tandem Publications; 1998. | solo en papers |
| 15832860 | , | 1 Queiroz IM . Lingual frenulum: classification and speech interference. Int J Orofacial Myol. 2004;30:31‐38.15832860 | solo en papers |
| 271473 | 10.1016/0002-9416(78)90102-1 | 10 Hanson ML . Oral myofunctional therapy. Am J Orthod 1978;73:56–67.10.1016/0002-9416(78)90102-1271473 | solo en papers |
| 33386612 | 10.1111/joor.13144 | 10. ZaghiS. ShamtoobS. PetersonC. ChristiansonL. Valcu-PinkertonS. PeeranZ. FungB. Kwok-keung NgD. JagomagiT. ArchambaultN. Assessment of Posterior Tongue Mobility Using  | en papers y en vídeos |
| 12531041 | 10.1053/smrv.2000.0131 | 10BeninatiW.SandersM. H.Optimal continuous positive airway pressure for the treatment of obstructive sleep apnea/hypopneaSleep Medicine Reviews20015172310.1053/smrv.2000. | solo en papers |
| 26691675 | 10.1002/lary.25827 | 10CamachoM.DunnB.TorreC.Supraglottoplasty for laryngomalacia with obstructive sleep apnea: a systematic review and meta-analysisThe Laryngoscope201510.1002/lary.258272669 | en papers y en vídeos |
| 12958120 | 10.1136/bmj.327.7414.557 | 10HigginsJ. P. T.ThompsonS. G.DeeksJ. J.AltmanD. G.Measuring inconsistency in meta-analysesBritish Medical Journal2003327741455756010.1136/bmj.327.7414.5572-s2.0-00418761 | solo en papers |
| , | 10.1590/s1516-18462006000400005 | 10VeraC. F. D.CondeG. E. S.WajnsztejnR.NemrK.Transtornos de aprendizagem em presença de respiração oral em indivíduos com diagnóstico de transtornos de défcit de atenção/ | solo en papers |
| , | , | 11 Moeller JL , Paskay LC , Gelb ML . Myofunctional therapy: a novel treatment of pediatric sleep‐disordered breathing. Sleep Med Clin 2014;9:235–243. | solo en papers |
| 31874353 | 10.1016/j.sleep.2019.09.019 | 11 Villa MP , Evangelisti M , Barreto M , Cecili M , Kaditis A . Short lingual frenulum as a risk factor for sleep‐disordered breathing in school‐age children. Sleep Med. | solo en papers |
| 14621092 | 10.1183/09031936.03.00047903 | 11FitzpatrickM. F.McLeanH.UrtonA. M.TanA.O’donnellD.DriverH. S.Effect of nasal or oral breathing route on upper airway resistance during sleepEuropean Respiratory Journal | solo en papers |
| 16137873 | 10.1016/j.rmed.2005.07.014 | 11HoekemaA.StegengaB.van der AaJ. G.MeineszA. F.van der HoevenJ. H.WijkstraP. J.Nap-titration: an effective alternative for continuous positive airway pressure titrationR | solo en papers |
| 9382404 | 10.7326/0003-4819-127-9-199711010-00008 | 11LauJ.IoannidisJ. P. A.SchmidC. H.Quantitative synthesis in systematic reviewsAnnals of Internal Medicine1997127982082610.7326/0003-4819-127-9-199711010-000082-s2.0-0030 | solo en papers |
| 19545089 | 10.52010/ijom.2000.26.1.5 | 12. MeyerP.G. Tongue Lip and Jaw Differentiation and Its Relationship to Orofacial Myofunctional TreatmentInt. J. Orofac. Myol.200834364510.52010/ijom.2000.26.1.519545089 | solo en papers |
| 22400135 | , | 12BalkE. M.ChungM.ChanJ. A.Future Research Needs for Treatment of Obstructive Sleep Apnea: Identification of Future Research Needs From Comparative Effectiveness Review N | solo en papers |
| 18853699 | , | 12ColrainI. M.BrooksS.BlackJ.A pilot evaluation of a nasal expiratory resistance device for the treatment of obstructive sleep apneaJournal of Clinical Sleep Medicine2008 | solo en papers |
| 25271880 | 10.1590/1516-3180.2013.7630011 | 12KuroishiR. C. S.GarciaR. B.ValeraF. C. P.Anselmo-LimaW. T.FukudaM. T. H.Deficits in working memory, reading comprehension and arithmetic skills in children with mouth b | solo en papers |
| 29275425 | 10.1007/s00405-017-4848-5 | 13 Camacho M , Guilleminault C , Wei JM , et al. Oropharyngeal and tongue exercises (myofunctional therapy) for snoring: a systematic review and meta‐analysis. Eur Arch O | solo en papers |
| 38068467 | 10.3390/jcm12237415 | 13. DydykA. MilonaM. Janiszewska-OlszowskaJ. WyganowskaM. GrocholewiczK. Influence of Shortened Tongue Frenulum on Tongue Mobility, Speech and OcclusionJ. Clin. Med.20231 | solo en papers |
| , | , | 13BerryR. B.BrooksR.GamaldoC. E.The AASM Manual for the Scoring of Sleep and Associated Events: Rules, Terminology and Technical Specifications, Version 2.0.22013Darien,  | solo en papers |
| 3289839 | 10.1378/chest.94.1.9 | 13HeJ.KrygerM. H.ZorickF. J.ConwayW.RothT.Mortality and apnea index in obstructive sleep apnea. Experience in 385 male patientsChest198894191410.1378/chest.94.1.92-s2.0-0 | solo en papers |
| 21344051 | , | 13PatelA. V.HwangD.MasdeuM. J.ChenG.-M.RapoportD. M.AyappaI.Predictors of response to a nasal expiratory resistor device and its potential mechanisms of action for treatm | solo en papers |
| 22990656 | 10.1097/mcp.0b013e328358be05 | 13RallsF. M.Grigg-DambergerM.Roles of gender, age, race/ethnicity, and residential socioeconomics in obstructive sleep apnea syndromesCurrent Opinion in Pulmonary Medicin | solo en papers |
| 30257620 | 10.1080/08869634.2018.1512242 | 14 Moeller MR . The emerging area of orofacial myofunctional therapy: Efficacy of treatment in sleep disordered breathing bringing promise of a new field of medicine. Cra | solo en papers |
| , | 10.3390/app11062727 | 14. LichnowskaA. KozakiewiczM. The Effectiveness of Frenotomy on Speech in AdultsAppl. Sci.202111272710.3390/app11062727 | solo en papers |
| 18555196 | 10.1016/j.spen.2008.03.006 | 14GozalD.Obstructive sleep apnea in children: implications for the developing central nervous systemSeminars in Pediatric Neurology200815210010610.1016/j.spen.2008.03.006 | solo en papers |
| 23051618 | 10.4187/respcare.01860 | 14LeeG.-H.KimM. J.LeeE. M.KimC. S.LeeS.-A.Prediction of optimal CPAP pressure and validation of an equation for asian patients with obstructive sleep apneaRespiratory Car | solo en papers |
| 3148884 | 10.1177/019459988809900402 | 14PowellN. B.RileyR. W.GuilleminaultC.MurciaG. N.Obstructive sleep apnea, continuous positive airway pressure, and surgeryOtolaryngology,Head and Neck Surgery198899436236 | solo en papers |
| 23723343 | 10.1136/thoraxjnl-2013-203508 | 14RossiV. A.WinterB.RahmanN. M.The effects of Provent on moderate to severe obstructive sleep apnoea during continuous positive airway pressure therapy withdrawal: a rand | solo en papers |
| , | , | 15 Rogers AP . Muscle training and its relation to orthodontia. Int J Orthod 1918;4:555–577. | en papers y en vídeos |
| 15888108 | 10.1111/j.1601-0825.2005.01108.x | 15 Ruffoli R , Giambelluca M , Scavuzzo MC , et al. Ankyloglossia: a morphofunctional investigation in children. Oral Dis. 2005;11:170‐174.1588810810.1111/j.1601-0825.200 | solo en papers |
| , | 10.3390/app11125732 | 15. LichnowskaA. KozakiewiczM. The Logopedic Evaluation of Adult Patients after Orthognathic SurgeryAppl. Sci.202111573210.3390/app11125732 | solo en papers |
| 19060979 | 10.1590/s0021-75572008000700010 | 15AbreuR. R.RochaR. L.LamounierJ. A.GuerraÂ. F. M.Etiologia, manifestações clínicas e alterações presentes nas crianças respiradoras oraisJornal de Pediatria2008846529535 | solo en papers |
| 25891298 | 10.1002/lary.25312 | 15FriedmanM.HwangM. S.YalamanchaliS.PottT.SidhuM.JosephN. J.Provent therapy for obstructive sleep apnea: impact of nasal obstructionThe Laryngoscope201510.1002/lary.25312 | solo en papers |
| 21210232 | 10.1007/s11325-010-0461-1 | 15LacedoniaD.SabatoR.CarpagnanoG. E.Predictive equations for CPAP titration in OSAS patientsSleep & Breathing20121619510010.1007/s11325-010-0461-12-s2.0-84859156545212102 | solo en papers |
| , | , | 15SwinscowT. D. V.CampbellM. J.Correlation and Regression1997Southampton, UKBMJ Publishing Group | solo en papers |
| 14783191 | 10.1016/0002-9416(50)90039-x | 16 Rogers AP . A restatement of the myofunctional concept in orthodontics. Am J Orthod 1950;36:845–855.1478319110.1016/0002-9416(50)90039-x | en papers y en vídeos |
| , | 10.3390/app112412084 | 16. LichnowskaA. KozakiewiczM. Speech Disorders in Dysgnathic Adult Patients in the Field of Severity of Primary DysfunctionAppl. Sci.2021111208410.3390/app112412084 | solo en papers |
| 25644497 | 10.1177/0194599814568284 | 16CamachoM.TeixeiraJ.AbdullatifJ.Maxillomandibular advancement and tracheostomy for morbidly obese obstructive sleep apnea: a systematic review and meta-analysisOtolaryng | en papers y en vídeos |
| 8049834 | 10.1164/ajrccm.150.2.8049834 | 16HoffsteinV.MateikaS.Predicting nasal continuous positive airway pressureAmerican Journal of Respiratory and Critical Care Medicine1994150248648810.1164/ajrccm.150.2.804 | solo en papers |
| 20465019 | , | 16RosenthalL.MassieC. A.DolanD. C.LoomasB.KramJ.HartR. W.A multicenter, prospective study of a novel nasal EPAP device in the treatment of obstructive sleep apnea: effica | solo en papers |
| 28315149 | 10.1007/s11325-017-1489-2 | 16VillaM. P.EvangelistiM.MartellaS.BarretoM.Del PozzoM.Can myofunctional therapy increase tongue tone and reduce symptoms in children with sleep-disordered breathing?Slee | en papers y en vídeos |
| 6793051 | 10.1038/sj.bdj.4804685 | 17 Mew J . The aetiology of malocclusion. Can the tropic premise assist our understanding? Br Dent J 1981;151:296.679305110.1038/sj.bdj.4804685 | solo en papers |
| 37823364 | 10.1111/joor.13609 | 17. BaxterR. Merkel-WalshR. LaheyL. KnutsenC. ZaghiS. The Buccal Frenum: Trends in Diagnosis and Indications for Treatment of Buccal-ties among 466 Healthcare Professiona | en papers y en vídeos |
| 15953321 | 10.1111/j.1440-1754.2005.00603.x | 17AmirL. H.JamesJ. P.BeattyJ.Review of tongue-tie release at a tertiary maternity hospitalJournal of Paediatrics and Child Health2005415-624324510.1111/j.1440-1754.2005.0 | solo en papers |
| 334025 | 10.1177/000348947708600517 | 17FeeW. E.Jr.WardP. H.Permanent tracheostomy: a new surgical techniqueThe Annals of Otology, Rhinology and Laryngology197786563563810.1177/0003489477086005172-s2.0-001776 | solo en papers |
| 21256800 | 10.1016/j.sleep.2010.06.011 | 17WalshJ. K.GriffinK. S.ForstE. H.A convenient expiratory positive airway pressure nasal device for the treatment of sleep apnea in patients non-adherent with continuous  | solo en papers |
| , | , | 18 Coryllos E , Genna CW , Salloum AC . Congenital tongue‐tie and its impact on breastfeeding. Breastfeeding: Best for Mother and Baby. 2004:1‐6. | solo en papers |
| 6945133 | 10.1179/bjo.8.4.203 | 18 Mew J . Tongue posture. Br J Orthod 1981;8:203–211.694513310.1179/bjo.8.4.203 | solo en papers |
| 21999476 | 10.1089/bfm.2011.0030 | 18BerryJ.GriffithsM.WestcottC.A double-blind, randomized, controlled trial of tongue-tie division and its immediate effect on breastfeedingBreastfeeding Medicine201273189 | solo en papers |
| 21461326 | 10.1093/sleep/34.4.479 | 18BerryR. B.KrygerM. H.MassieC. A.A novel nasal expiratory positive airway pressure (EPAP) device for the treatment of obstructive sleep apnea: a randomized controlled tr | solo en papers |
| 8834348 | 10.1183/09031936.96.09010146 | 18DalmassoF.ProtaR.Snoring: analysis, measurement, clinical implications and applicationsThe European Respiratory Journal19969114615910.1183/09031936.96.090101462-s2.0-00 | solo en papers |
| 6692111 | 10.1002/bjs.1800710224 | 18MatthewsH. R.HopkinsonR. B.Treatment of sputum retention by minitracheotomyBritish Journal of Surgery198471214715010.1002/bjs.18007102242-s2.0-00213276066692111 | solo en papers |
| 23362754 | , | 19 Martinelli RLDC , Marchesan IQ , Berretin‐Felix G . Lingual frenulum protocol with scores for infants. Int J Orofacial Myology. 2012;38:104‐112.23362754 | en papers y en vídeos |
| 15592223 | 10.1016/j.ajodo.2003.12.019 | 19 Mew JR . The postural basis of malocclusion: a philosophical overview. Am J Orthod Dentofac Orthop 2004;126:729–738.10.1016/j.ajodo.2003.12.01915592223 | solo en papers |
| , | , | 19. MajewskiS. Gnatofizjologia Stomatologiczna: Normy Okluzji i Funkcje Układu Stomatognatycznego1st ed.PZWLWarszawa, Poland2022 | solo en papers |
| 18573859 | 10.1542/peds.2007-2553 | 19GeddesD. T.LangtonD. B.GollowI.JacobsL. A.HartmannP. E.SimmerK.Frenulotomy for breastfeeding infants with ankyloglossia: effect on milk removal and sucking mechanism as | solo en papers |
| 22003339 | 10.5664/jcsm.1304 | 19KrygerM. H.BerryR. B.MassieC. A.Long-term use of a nasal expiratory positive airway pressure (EPAP) device as a treatment for obstructive sleep apnea (OSA)Journal of Cl | solo en papers |
| 7887716 | 10.1016/0003-4975(94)01016-1 | 19van HeurnL. W. E.van GeffenG. J.BrinkP. R. G.Percutaneous subcricoid minitracheostomy: report of 50 proceduresThe Annals of Thoracic Surgery199559370770910.1016/0003-49 | solo en papers |
| , | 10.18650/2379-5824.11001 | 1GuilleminaultC.SullivanS.Towards restoration of continuous nasal breathing as the ultimate treatment goal in pediatric obstructive sleep apneaEnliven: Pediatrics and Neo | en papers y en vídeos |
| 180875 | 10.1146/annurev.me.27.020176.002341 | 1GuilleminaultC.TilkianA.DementW. C.The sleep apnea syndromesAnnual Review of Medicine19762746548410.1146/annurev.me.27.020176.0023412-s2.0-0016904083180875 | en papers y en vídeos |
| 23589584 | 10.1093/aje/kws342 | 1PeppardP. E.YoungT.BarnetJ. H.PaltaM.HagenE. W.HlaK. M.Increased prevalence of sleep-disordered breathing in adultsAmerican Journal of Epidemiology201317791006101410.109 | solo en papers |
| 5251442 | , | 2 Horton CE , Crawford HH , Adamson JE , Ashbell TS . Tongue‐tie. Cleft Palate J 1969;6:8–23.5251442 | solo en papers |
| 12501105 | 10.1067/mhn.2002.129731 | 2 Messner AH , Lalakea ML . The effect of ankyloglossia on speech in children. Otolaryngol‐Head Neck Surg. 2002;127:539‐545.1250110510.1067/mhn.2002.129731 | solo en papers |
| 28787179 | 10.1089/bfm.2017.0044 | 2. Bin-NunA. KasirerY.M. MimouniF.B. A Dramatic Increase in Tongue Tie-Related Articles: A 67 Years Systematic ReviewBreastfeed. Med.20171241041410.1089/bfm.2017.00442878 | solo en papers |
| 4621365 | 10.1016/0002-9416(72)90174-1 | 20 Harvold EP , Chierici G , Vargervik K . Experiments on the development of dental malocclusions. Am J Orthod 1972;61:38–44.462136510.1016/0002-9416(72)90174-1 | solo en papers |
| , | 10.1891/2158-0782.8.3.132 | 20 Hazelbaker Alison K. . Assessment Tool for Lingual Frenulum Function (ATLFF). Clinical Lactation. 2017;8 (3):132–133. 10.1891/2158-0782.8.3.132. | solo en papers |
| , | , | 20. Fernández-de-las-PeñasC. Mesa-JiménezJ. ChaitowL. Temporomandibular Disorders: Manual Therapy, Exercise, and NeedlingHandspring Publishing LimitedPencaitland, UK2018 | solo en papers |
| , | , | 20HwangD.PatelA.ChenG.AyappaI.RapoportD.Nasal epap-physiologic mechanism of actionProceedings of the 23rd Annual Meeting of the Associated Professional Sleep Societies (S | solo en papers |
| 1885470 | 10.1152/jappl.1991.70.6.2736 | 20LiistroG.StanescuD.VeriterC.Pattern of simulated snoring is different through mouth and noseJournal of Applied Physiology1991706273627412-s2.0-0025821665188547010.1152/ | solo en papers |
| 21603045 | , | 20MoherD.LiberatiA.TetzlaffJ.AltmanD. G.Preferred reporting items for systematic reviews and meta-analyses: the PRISMA statementPLoS Medicine20096e1000097PMC3090117216030 | solo en papers |
| 6939331 | 10.1016/0002-9416(81)90379-1 | 21 Harvold EP , Tomer BS , Vargervik K , Chierici G . Primate experiments on oral respiration. Am J Orthod 1981;79:359–372.693933110.1016/0002-9416(81)90379-1 | en papers y en vídeos |
| 23367525 | , | 21 Marchesan IQ . Lingual frenulum protocol. Int J Orofacial Myology. 2012;38:89‐103.23367525 | en papers y en vídeos |
| , | , | 21. OkesonJ.P. Management of Temporomandibular Disorders and Occlusion8th ed.ElsevierSt. Louis, MO, USA2020 | solo en papers |
| 25160687 | 10.1017/s0022215114001686 | 21CamachoM.CapassoR.SchendelS.Airway changes in obstructive sleep apnoea patients associated with a supine versus an upright position examined using cone beam computed to | en papers y en vídeos |
| , | 10.4172/2324-8785.1000118 | 21KumarA. R.CamachoM.CapassoR.Quantitative assessment of an obstructive sleep apnea patient before and after tracheostomy: a case studyJournal of Otology & Rhinology20132 | solo en papers |
| , | 10.1016/j.jsmc.2014.03.002 | 21MoellerJ. L.PaskayL. C.GelbM. L.Myofunctional therapy: a novel treatment of pediatric sleep-disordered breathingSleep Medicine Clinics20149223524310.1016/j.jsmc.2014.03 | solo en papers |
| , | , | 21WestbrookP.DoshiR.LoomasB.Success rates of nasal expiratory positive airway pressure (NEPAP) via expiratory resistive load for the treatment of obstructive sleep apneaP | solo en papers |
| 23362750 | , | 22 Grandi D . The" Interdisciplinary Orofacial Examination Protocol for Children and Adolescents": a resource for the interdisciplinary assessment of the stomatognatic sy | solo en papers |
| 6947703 | 10.1043/0003-3219(1981)051<0269:iorpoc>2.0.co;2 | 22 McNamara JA Jr . Influence of respiratory pattern on craniofacial growth. Angle Orthod 1981;51:269–300.694770310.1043/0003-3219(1981)051<0269:IORPOC>2.0.CO;2 | solo en papers |
| , | , | 22. KleinrokM. Zaburzenia Czynnościowe Układu Ruchowego Narządu Żucia5th ed.Wydawnictwo CzelejLublin, Poland2012 | solo en papers |
| , | , | 22AdamsG.Retrospective case series analysis of a nasal expiratory positive airway pressure (EPAP) device to treat obstructive sleep apnea in a clinical practiceProceeding | solo en papers |
| 19065292 | 10.1080/00016480802572509 | 22BrowaldhN.MarkstrmA.FribergD.Elective tracheostomy is an alternative treatment in patients with severe obstructive sleep apnoea syndrome and CPAP failureActa Oto-Laryng | solo en papers |
| 13554451 | 10.1177/003591575805100420 | 22Gwynne-EvansE.Discussion on the mouth-breatherProceedings of Royal Society of Medicine195851427928210.1177/003591575805100420PMC188977813554451 | solo en papers |
| 17162993 | 10.1093/sleep/29.11.1456 | 22HerzogM.MetzT.SchmidtA.The prognostic value of simulated snoring in awake patients with suspected sleep-disordered breathing: introduction of a new technique of examina | solo en papers |
| 27958599 | 10.14639/0392-100x-770 | 23 Grippaudo C , Paolantonio E , Antonini G , Saulle R , La Torre G , Deli R . Association between oral habits, mouth breathing and malocclusion. Acta Otorhinolaryngol It | solo en papers |
| 34364317 | 10.1515/jcim-2020-0101 | 23. BuscemiA. CocoM. RapisardaA. FrazzettoG. Di RosaD. FeoS. PilusoM. PresenteL.P. CampisiS.S. DesiròP. Tongue Stretching: Technique and Clinical ProposalJ. Complement. I | solo en papers |
| , | , | 23BerryR. B.BrooksR.GamaldoC. E.The AASM Manual for the Scoring of Sleep and Associated Events: Rules, Terminology and Technical Specifications, Version 2.0.2Darien, Ill, | solo en papers |
| 2736981 | 10.1378/chest.96.1.205 | 23FletcherE. C.Recurrence of sleep apnea syndrome following tracheostomy. A shift from obstructive to central apneaChest198996120520910.1378/chest.96.1.2052-s2.0-00243596 | solo en papers |
| , | , | 23HwangD.ChangJ.GonzalezL.WiglerE.BeckerK.Nasal EPAP as a major osa therapeutic option in a clinical sleep center settingProceedings of the 25th Annual Meeting Associated | solo en papers |
| , | , | 24 Martinelli Roberta Lopes de Castro , Marchesan Irene Queiroz , Berretin‐Felix Giédre . Tongue position for lingual frenulum assessment. Revista CEFAC. 2020;22 (1):http | solo en papers |
| 22207245 | 10.1007/s00455-011-9383-8 | 24. KnöselM. KleinS. BleckmannA. EngelkeW. Coordination of Tongue Activity during Swallowing in Mouth-Breathing ChildrenDysphagia20122740140710.1007/s00455-011-9383-82220 | solo en papers |
| 4014304 | 10.1016/0002-9343(85)90543-1 | 24FletcherE. C.BrownD. L.Nocturnal oxyhemoglobin desaturation following tracheostomy for obstructive sleep apneaThe American Journal of Medicine1985791354210.1016/0002-93 | solo en papers |
| , | , | 24MassieC.HartR.Clinical efficacy of a nasal expiratory positive airway pressure (EPAP) device for the treatment of obstructive sleep apnea (OSA)Proceedings of the 25th A | solo en papers |
| , | , | 24SwinscowT. D. V.CampbellM. J.Correlation and Regression1997Southampton, UKBMJ Publishing Group | solo en papers |
| , | , | 25 Chauvois A , Fournier M , Girardin F . Rééducation des fonctions dans la thérapeutique orthodontique. Paris, France: SID; 1991. | solo en papers |
| 16739711 | , | 25 Marchesan IQ . Lingual Frenulum: quantitative evaluation proposal. Int J Orofacial Myol. 2005;31:39‐48.16739711 | solo en papers |
| , | 10.52010/ijom.2024.50.2.2 | 25. Merkel-WalshR.A. OverlandL.L. Clinical Perspectives on Post-Operative Care for Tethered Oral Tissues (TOTs)Int. J. Orofac. Myol. Myofunct. Ther.20245011310.52010/ijom | solo en papers |
| , | , | 25AdamsG.Nasal expiratory positive airway pressure (EPAP) device to treat obstructive sleep apnea in patients age 65 and overProceedings of the 26th Annual Meeting of the | solo en papers |
| 3563246 | 10.1093/sleep/10.1.35 | 25FletcherE. C.MillerJ.SchaafJ. W.FletcherJ. G.Urinary catecholamines before and after tracheostomy in patients with obstructive sleep apnea and hypertensionSleep19871013 | solo en papers |
| 31390450 | 10.1590/2177-6709.24.3.055-063.oar | 26 Fatima F , Fida M . The assessment of resting tongue posture in different sagittal skeletal patterns. Dental Press J Orthod. 2019;24:55‐63.3139045010.1590/2177-6709.24 | solo en papers |
| , | , | 26 Mew J . Are random controlled trials appropriate for orthodontics? Evid Base Dent 2002;3:35. | solo en papers |
| 31332567 | 10.1007/s00784-019-03017-5 | 26. ChenY.F. KoE.C. ZaghiS. YoonA. WilliamsR. RileyR. LiuS.Y.-C. Optimizing Mandibular Sagittal Split of Large Maxillomandibular Advancements for Obstructive Sleep Apnea: | solo en papers |
| 6807156 | 10.1164/arrd.1982.126.1.14 | 26GuilleminaultC.CummiskeyJ.Progressive improvement of apnea index and ventilatory response to CO2 after tracheostomy in obstructive sleep apnea syndromeThe American Revi | solo en papers |
| , | , | 26MassieC.An analysis of responders to nasal expiratory positive airway pressure(EPAP) therapy during long term follow upProceedings of the 26th Annual Meeting of the Ass | solo en papers |
| , | 10.1145/3311823.3311831 | 27 Li R , Wu J , TongueBoard ST . An Oral Interface for Subtle Input Proceedings of the 10th Augmented Human International Conference 2019, 2019:1–9. https://doi.org/10.1 | solo en papers |
| 14733214 | 10.1016/j.ajodo.2003.11.011 | 27 Mew JR . Does “evidence‐based research” provide needed evidence? Am J Orthod Dentofac Orthop 2004;125:A20.10.1016/j.ajodo.2003.11.01114733214 | solo en papers |
| 30709528 | 10.1016/j.jsmc.2018.10.004 | 27. HuangY.-S. HsuS.-C. GuilleminaultC. ChuangL.-C. Myofunctional TherapySleep Med. Clin.20191413514210.1016/j.jsmc.2018.10.00430709528 | solo en papers |
| , | , | 27DeorasM.GolishJ.ThorntonD.Is nasal EPAP combined with nonsupine sleeping position effective in controlling OSA in those who have failed traditional treatment?Proceeding | solo en papers |
| 7247605 | 10.1001/archinte.141.8.985 | 27GuilleminaultC.SimmonsF. B.MottaJ.Obstructive sleep apnea syndrome and tracheostomy. Long-term follow-up experienceArchives of Internal Medicine1981141898598810.1001/ar | en papers y en vídeos |
| 19234106 | 10.1164/rccm.200806-981oc | 28 Guimarães KC , Drager LF , Genta PR , Marcondes BF , Lorenzi‐Filho G . Effects of oropharyngeal exercises on patients with moderate obstructive sleep apnea syndrome. A | en papers y en vídeos |
| , | , | 28 Schmidt AM . Evaluating a new clinical palatometry system. Advances Speech Lang Pathol. 2007;9:73‐81. | solo en papers |
| 38982581 | 10.1111/ipd.13235 | 28. SmartS. GrantH. TsengR.J. Beyond Surgery: Pre- and Post-operative Care in Children with AnkyloglossiaInt. J. Paed. Dent.202412110.1111/ipd.1323538982581PMC11788522 | solo en papers |
| 11359089 | 10.1159/000055728 | 28HaapaniemiJ. J.LaurikainenE. A.HalmeP.AntilaJ.Long-term results of tracheostomy for severe obstructive sleep apnea syndromeORL200163313113610.1159/0000557282-s2.0-00350 | solo en papers |
| , | , | 28MansfieldD.HamiltonG.TabartF.An expiratory positive airway pressure valve applied nasally (provent TM) improves polysomnographic indices of obstructive sleep apnea seve | solo en papers |
| 23702236 | 10.1016/j.sleep.2013.03.016 | 29 Diaferia G , Badke L , Santos‐Silva R , Bommarito S , Tufik S , Bittencourt L . Effect of speech therapy as adjunct treatment to continuous positive airway pressure on | solo en papers |
| , | , | 29 Draghici O , Batkin I , Bolic M , Chapman I . The mouthpad: A tongue‐computer interface 2013 IEEE International Symposium on Medical Measurements and Applications (MeM | solo en papers |
| , | 10.21307/aoj-2021.033 | 29. TomeW. MoonW. The Prevalence of Posterior Tongue Tie in Patients with Transverse Maxillary DeficiencyAustralas. Orthod. J.20213729430010.21307/aoj-2021.033 | solo en papers |
| 2619690 | 10.1111/j.1479-828x.1989.tb01768.x | 29HastieS. J.ProwseK.PerksW. H.AtkinsJ.BluntV. A. W.Obstructive sleep apnoea during pregnancy requiring tracheostomyAustralian and New Zealand Journal of Obstetrics and G | solo en papers |
| , | , | 29MartinI. D.HigginsM. D.PrasadS.Treatment of obstructive sleep apnea with nasal expiratory positive airway pressure (EPAP) devices: a retrospective analysis of 50 consec | en papers y en vídeos |
| 18830512 | 10.1590/s0021-75572008000600015 | 2AbreuR. R.RochaR. L.LamounierJ. A.GuerraÂ. F. M.Prevalência de crianças respiradoras oraisJornal de Pediatria200884546747010.1590/s0021-7557200800060001518830512 | solo en papers |
| 32462918 | 10.1177/0009922820928055 | 3 Baxter R , Merkel‐Walsh R , Baxter B , Lashley A , Rendell N . Functional improvements of speech, feeding, and sleep after lingual frenectomy tongue‐tie release: a pros | en papers y en vídeos |
| , | , | 3. SmartS. TsengR. KittrellA. Merkel-WalshR. Practice Guideline for Ankylofrenula Management. ICAP2024Available online: https://icapprofessionals.com/(accessed on 30 June | solo en papers |
| 24859614 | 10.1007/s11325-014-1011-z | 30 Villa MP , Brasili L , Ferretti A , et al. Oropharyngeal exercises to reduce symptoms of OSA after AT. Sleep Breath 2015;19:281–289.2485961410.1007/s11325-014-1011-z | en papers y en vídeos |
| 20623302 | 10.1007/s00455-010-9291-3 | 30 Yoshikawa M , Yoshida M , Tsuga K , Akagawa Y , Groher ME . Comparison of three types of tongue pressure measurement devices. Dysphagia. 2011;26:232‐237.2062330210.100 | solo en papers |
| 37629077 | 10.3390/ijms241612896 | 30. ZalewskaA. AntonowiczB. SzulimowskaJ. Zieniewska-SiemieńczukI. LeśniewskaB. BorysJ. ZiębaS. Kostecka-SochońP. Żendzian-PiotrowskaM. Lo GiudiceR. Mitochondrial Redox B | solo en papers |
| 17136406 | 10.1007/s11325-006-0084-8 | 30HoffsteinV.Review of oral appliances for treatment of sleep-disordered breathingSleep and Breathing200711112210.1007/s11325-006-0084-82-s2.0-3394757575417136406PMC17946 | solo en papers |
| 697223 | 10.7326/0003-4819-89-4-454 | 30MottaJ.GuilleminaultC.SchroederJ. S.DementW. C.Tracheostomy and hemodynamic changes in sleep-induced apneaAnnals of Internal Medicine197889445445810.7326/0003-4819-89-4 | solo en papers |
| 23522724 | 10.1016/j.sleep.2013.01.013 | 31 Guilleminault C , Huang Y , Monteyrol P , Sato R , Quo S , Lin C . Critical role of myofascial reeducation in pediatric sleep‐disordered breathing. Sleep Med 2013;14:5 | en papers y en vídeos |
| 31745755 | 10.1007/s11325-019-01952-x | 31 O’Connor‐Reina C , Plaza G , Garcia‐Iriarte MT , et al. Tongue peak pressure: a tool to aid in the identification of obstruction sites in patients with obstructive sle | solo en papers |
| 34206954 | 10.3390/jcm10132832 | 31. WozniakL. Ratajczak-WronaW. BorysJ. AntonowiczB. NowakK. BortnikP. JablonskaE. Levels of Biological Markers of Nitric Oxide in Serum of Patients with Mandible Fractur | solo en papers |
| 12622603 | 10.1001/archinte.163.5.565 | 31PatelS. R.WhiteD. P.MalhotraA.StanchinaM. L.AyasN. T.Continuous positive airway pressure therapy for treating sleepiness in a diverse population with obstructive sleep  | solo en papers |
| 3516586 | 10.1378/chest.89.5.627 | 31RapoportD. M.GarayS. M.EpsteinH.GoldringR. M.Hypercapnia in the obstructive sleep apnea syndrome. A reevaluation of the ‘Pickwickian syndrome’Chest198689562763510.1378/ | solo en papers |
| 26483933 | 10.1016/j.slsci.2014.11.002 | 32 Levrini L , Lorusso P , Caprioglio A , et al. Model of oronasal rehabilitation in children with obstructive sleep apnea syndrome undergoing rapid maxillary expansion:  | solo en papers |
| 18658054 | 10.1044/1092-4388(2008/060) | 32 Palmer PM , Jaffe DM , McCulloch TM , Finnegan EM , Van Daele DJ , Luschei ES . Quantitative contributions of the muscles of the tongue, floor‐of‐mouth, jaw, and velum | solo en papers |
| 15201136 | 10.1164/rccm.200311-1571oc | 32BarnesM.McEvoyR. D.BanksS.Efficacy of positive airway pressure and oral appliance in mild to moderate obstructive sleep apneaAmerican Journal of Respiratory and Critica | solo en papers |
| 7390328 | 10.1111/j.1440-1819.1980.tb01509.x | 32SugitaY.WakamatsuH.TeshimaY.Therapeutic effects of tracheostomy in two cases of hypersomnia with respiratory disturbance during sleepFolia Psychiatrica et Neurologica J | solo en papers |
| 21032979 | 10.1179/crn.2010.033 | 33 de Felício CM , Melchior MDO , da Silva MAMR . Effects of orofacial myofunctional therapy on temporomandibular disorders. CRANIO®. 2010;28(4):249‐259.2103297910.1179/c | solo en papers |
| 30233265 | 10.2147/nss.s141132 | 33 de Felício CM , da Silva Dias FV , Trawitzki LVV . Obstructive sleep apnea: focus on myofunctional therapy. Nat Sci Sleep 2018;10:271.3023326510.2147/NSS.S141132PMC613 | solo en papers |
| 17520790 | 10.1093/sleep/30.4.461 | 33ElshaugA. G.MossJ. R.SouthcottA. M.HillerJ. E.Redefining success in airway surgery for obstructive sleep apnea: a meta analysis and synthesis of the evidenceSleep200730 | solo en papers |
| 7221348 | 10.1093/sleep/3.3-4.407 | 33WeitzmanE. D.KahnE.PollakC. P.Quantitative analysis of sleep and sleep apnea before and after tracheostomy in patients with the hypersomnia-sleep apnea syndromeSleep198 | solo en papers |
| , | , | 34 Gelb M , Hindin H . Gasp: Airway Health: The Hidden Path to Wellness. New York, NY, USA: CreateSpace Independent Publishing Platform; 2016. | solo en papers |
| 9738809 | 10.1001/archotol.124.9.996 | 34KimS. H.EiseleD. W.SmithP. L.SchneiderH.SchwartzA. R.Evaluation of patients with sleep apnea after tracheotomyArchives of Otolaryngology,Head & Neck Surgery199812499961 | solo en papers |
| 12119227 | 10.1164/rccm.2105124 | 34PekerY.HednerJ.NorumJ.KraicziH.CarlsonJ.Increased incidence of cardiovascular disease in middle-aged men with obstructive sleep apnea: a 7-year follow-upAmerican Journa | solo en papers |
| , | , | 35 Liao F . Six‐Foot Tiger, Three‐Foot Cage: Take Charge of Your Health by Taking Charge of Your Mouth. Carlsbad, CA, USA: Crescendo Publishing LLC; 2017. | solo en papers |
| 24812544 | 10.5664/jcsm.3716 | 35ChopraA.DasP.RamarK.StaatsB.St LouisE. K.Complex sleep apnea associated with use of nasal expiratory positive airway (nEPAP) deviceJournal of Clinical Sleep Medicine201 | solo en papers |
| , | , | 35LedereichP.ThorpyM.LovinskyP.Five-year follow-up of daytime sleepiness and snoring after tracheotomy in patients with obstructive sleep apneaChronic Rhonchopathy1988Par | solo en papers |
| , | , | 36 Kahn S , Ehrlich PR . Jaws: The Story of a Hidden Epidemic. Palo Alto, CA: Stanford University Press; 2018. | solo en papers |
| 24932147 | 10.5664/jcsm.3796 | 36KureshiS. A.GallagherP. R.McDonoughJ. M.Pilot study of nasal expiratory positive airway pressure devices for the treatment of childhood obstructive sleep apnea syndrome | solo en papers |
| 3191760 | 10.1378/chest.94.6.1200 | 36PartinenM.JamiesonA.GuilleminaultC.Long-term outcome for obstructive sleep apnea syndrome patients. MortalityChest19889461200120410.1378/chest.94.6.12002-s2.0-002423944 | solo en papers |
| , | , | 37 Guilleminault C , Sullivan S . Towards restoration of continuous nasal breathing as the ultimate treatment goal in pediatric obstructive sleep apnea. Enliven: Pediatr  | solo en papers |
| 24155050 | 10.1002/lary.24479 | 37VroegopA. V.VandervekenO. M.BoudewynsA. N.Drug-induced sleep endoscopy in sleep-disordered breathing: report on 1,249 casesLaryngoscope2014124379780210.1002/lary.244792 | solo en papers |
| 207245 | 10.1001/archneur.1978.00500300066013 | 37WeitzmanE. D.PollackC. P.BorowieckiB.Hypersomnia-sleep apnea due to micrognathia. Reversal by tracheoplastyArchives of Neurology197835639239510.1001/archneur.1978.00500 | solo en papers |
| , | , | 38 Burger D. Pediatric airway symposium to clear the air on dental screening, treatment, ADA News https://www.ada.org/en/publications/ada-news/2018-archive/june/pediatric | solo en papers |
| 20685749 | 10.1136/thx.2009.131094 | 38ChanA. S. L.SutherlandK.SchwabR. J.The effect of mandibular advancement on upper airway structure in obstructive sleep apnoeaThorax201065872673210.1136/thx.2009.1310942 | solo en papers |
| 12439159 | 10.1097/00005537-200211000-00006 | 38GrossN. D.CohenJ. I.AndersenP. E.WaxM. K.'Defatting' tracheotomy in morbidly obese patientsThe Laryngoscope2002112111940194410.1097/00005537-200211000-000062-s2.0-00368 | solo en papers |
| 25061252 | 10.5665/sleep.3846 | 39SchwabR. J.KimC.SiegelL.Examining the mechanism of action of a new device using oral pressure therapy for the treatment of obstructive sleep apneaSleep20143771237124710 | solo en papers |
| 14248361 | 10.1001/archinte.1965.03860150051009 | 39ValeroA.AlroyG.Hypoventilation in acquired micrognathiaArchives of Internal Medicine196511530731010.1001/archinte.1965.038601500510092-s2.0-000149503614248361 | solo en papers |
| 16553025 | 10.1093/sleep/29.3.381 | 3GayP.WeaverT.LoubeD.Evaluation of positive airway pressure treatment for sleep related breathing disorders in adultsSleep20062933814011655302510.1093/sleep/29.3.381 | solo en papers |
| 25820584 | 10.1177/0194599815575721 | 3SenchakA. J.McKinlayA. J.AcevedoJ.The effect of tonsillectomy alone in adult obstructive sleep apneaOtolaryngology,Head and Neck Surgery2015152596997310.1177/01945998155 | solo en papers |
| 26933510 | 10.1155/2016/7089123 | 3TeixeiraJ.CertalV.ChangE. T.CamachoM.Nasal septal deviations: a systematic review of classification systemsPlastic Surgery InternationalIn press10.1155/2016/7089123PMC47 | solo en papers |
| 31367903 | 10.1007/s00455-019-10040-x | 4 Brooks L , Landry A , Deshpande A , Marchica C , Cooley A , Raol N . Posterior tongue tie, base of tongue movement, and pharyngeal dysphagia: what is the connection? Dy | solo en papers |
| 2256561 | 10.1043/0003-3219(1990)060<0247:madris>2.0.co;2 | 4 Gross AM , Kellum GD , Hale ST , et al. Myofunctional and dentofacial relationships in second grade children. Angle Orthod 1990;60:247–253.225656110.1043/0003-3219(1990 | solo en papers |
| , | , | 4. SmartS. TsengR. KittrellA. Merkel-WalshR. ChanJ. JonesN. AltemaraJ. HartwickE. Position Statement on Ankylofrenula. ICAP2024Available online: https://icapprofessionals | solo en papers |
| , | , | 40 Huang Y , Quo S , Berkowski J , Guilleminault C . Short lingual frenulum and obstructive sleep apnea in children. Int J Pediatr Res 2015;1:1–4. | solo en papers |
| 15280738 | 10.1097/00005537-200408000-00038 | 40AkstL. M.EliacharI.Long-term, tube-free (permanent) tracheostomy in morbidly obese patientsThe Laryngoscope20041148151115131528073810.1097/00005537-200408000-00038 | solo en papers |
| , | , | 41 Chien Y , Guilleminault C . Adult short lingual frenulum and obstructive sleep apnea. J Sleep Sleep Disorders Res 2017;40:A164–A165. | solo en papers |
| 2319895 | 10.1288/00005537-199004000-00018 | 41ClaymanG. L.AdamsG. L.Permanent tracheostomy with cervical lipectomyThe Laryngoscope199010044224242-s2.0-0025346890231989510.1288/00005537-199004000-00018 | solo en papers |
| 29774762 | 10.1177/0003489418776343 | 42 Aaronson NL , Castaño JE , Simons JP , Jabbour N . Quality, readability, and trends for websites on ankyloglossia. Ann Otol Rhinol Laryngol 2018;127:439–444.2977476210 | solo en papers |
| 12516917 | , | 42EliasharR.GoldfarbA.GrossM.SichelJ.-Y.A permanent tube-free tracheostomy in a morbidly obese patient with severe obstructive sleep apnea syndromeThe Israel Medical Asso | solo en papers |
| 27222891 | 10.3290/j.qi.a36027 | 43 Tsaousoglou P , Topouzelis N , Vouros I , Sculean A . Diagnosis and treatment of ankyloglossia: a narrative review and a report of three cases. Quintessence Int 2016;4 | solo en papers |
| 498839 | 10.1378/chest.76.5.611a | 43BoysenP. G.HarrisJ. O.BlockA. J.WynneJ. W.Stomal embellishment following tracheostomy for obstructive sleep-related apneaChest1979765, article 6112-s2.0-001854763310.13 | solo en papers |
| 25025566 | 10.1590/1678-775720130629 | 44 Junqueira MA , Cunha NNO , e SILVA C , et al. Surgical techniques for the treatment of ankyloglossia in children: a case series. J Appl Oral Sci 2014;22:241–248.250255 | solo en papers |
| 21817868 | 10.1097/paf.0b013e31822abf4e | 44ByardR. W.GilbertJ. D.Potentially lethal complications of tracheostomy: autopsy considerationsThe American Journal of Forensic Medicine and Pathology201132435235410.109 | solo en papers |
| 27641715 | 10.1002/lary.26306 | 45 Ghaheri BA , Cole M , Fausel SC , Chuop M , Mace JC . Breastfeeding improvement following tongue‐tie and lip‐tie release: a prospective cohort study. Laryngoscope 2017 | solo en papers |
| 15807912 | , | 45HessD. R.Tracheostomy tubes and related appliancesRespiratory Care20055044975102-s2.0-2214448277715807912 | solo en papers |
| 15552958 | , | 46ArimuneM.SanjouH.YamadaT.YabeM.MiyakeH.Minitracheotomy in treating upper airway obstruction after anterior cervical fusionThe Japanese Journal of Anesthesiology20045310 | solo en papers |
| 24498769 | , | 47MorishimaK.KuritaS.YamamaY.NakataniK.Two patients with CICV (cannot intubate cannot ventilate) rescued by cricothyrotomyMasui. The Japanese Journal of Anesthesiology201 | solo en papers |
| 3464671 | 10.1017/s0022215100100829 | 48SquiresS. J.FramptonM. C.The use of mini-tracheostomy and high frequency jet ventilation in the management of acute airway obstructionThe Journal of Laryngology and Oto | solo en papers |
| , | , | 49 Fabbie P , Kundel L , Vitruk P . Tongue‐tie functional release. Dent Sleep Practice Winter 2016;40–45. Available at: https://dentalsleeppractice.com/articles/tongue-ti | solo en papers |
| 11215241 | , | 49TerayamaS.KomatsuK.NishiyamaT.HanaokaK.Airway obstruction after general anesthesia in a patient with the first and second branchial arch syndromeJapanese Journal of Ane | solo en papers |
| 25389029 | 10.1002/lary.25032 | 4CertalV. F.ZaghiS.RiazM.Hypoglossal nerve stimulation in the treatment of obstructive sleep apnea: a systematic review and meta-analysisThe Laryngoscope20151255125412641 | en papers y en vídeos |
| 19786224 | 10.1016/j.otohns.2009.06.083 | 4CiprandiG.MoraF.CassanoM.GallinaA. M.MoraR.Visual analog scale (VAS) and nasal obstruction in persistent allergic rhinitisOtolaryngology-Head and Neck Surgery20091414527 | solo en papers |
| 1554212 | 10.1164/ajrccm/145.4_pt_1.841 | 4HoffsteinV.VinerS.MateikaS.ConwayJ.Treatment of obstructive sleep apnea with nasal continuous positive airway pressure: patient compliance, perception of benefits, and s | solo en papers |
| 25877805 | 10.1007/s11325-015-1154-6 | 4LeeS.-Y.GuilleminaultC.ChiuH.-Y.SullivanS. S.Mouth breathing, “nasal disuse,” and pediatric sleep-disordered breathingSleep and Breathing20151941257126410.1007/s11325-01 | solo en papers |
| 18250209 | 10.1513/pats.200708-119mg | 4WeaverT. E.GrunsteinR. R.Adherence to continuous positive airway pressure therapy: the challenge to effective treatmentProceedings of the American Thoracic Society200852 | solo en papers |
| 11758333 | , | 50SatoM.HondaO.HiragaK.Severe laryngeal edema after tracheal extubation,report of a caseThe Japanese Journal of Anesthesiology20015011123612382-s2.0-003521439311758333 | solo en papers |
| 8557880 | 10.1007/bf01700975 | 51FikkersB. F.ZandstraD. F.Primary laryngospasm in a patient with Parkinson's disease: treatment with CPAP via minitracheostomy following intubationIntensive Care Medicin | solo en papers |
| , | , | 52MunsonB. R.YoungD. F.OkishiT. H.Fundamental of Fluid Mechanics2006New York, NY, USAJohn Wiley & Sons | solo en papers |
| , | 10.1044/leader.ftr1.23022018.48 | 5ArchambaultN.Healthy breathing, ‘round the clockASHA Leader2018232485410.1044/leader.ftr1.23022018.482-s2.0-85041527081 | solo en papers |
| 21799124 | 10.1152/japplphysiol.00218.2011 | 5BragaC. W.ChenQ.BurschtinO. E.RapoportD. M.AyappaI.Changes in lung volume and upper airway using MRI during application of nasal expiratory positive airway pressure in p | solo en papers |
| 10202316 | 10.1159/000029354 | 5BranderP. E.SoirinsuoM.LohelaP.Nasopharyngeal symptoms in patients with obstructive sleep apnea syndrome. Effect of nasal CPAP treatmentRespiration199966212813510.1159/0 | solo en papers |
| 16553024 | 10.1093/sleep/29.3.375 | 5KushidaC. A.LittnerM. R.HirshkowitzM.Practice parameters for the use of continuous and bilevel positive airway pressure devices to treat adult patients with sleep-relate | solo en papers |
| 24124639 | 10.2500/ar.2013.4.0054 | 5TsaoG. J.FijalkowskiN.MostS. P.Validation of a grading system for lateral nasal wall insufficiencyAllergy & Rhinology201342e66e6810.2500/ar.2013.4.005424124639PMC3793115 | solo en papers |
| , | , | 6 Stecco C . Functional Atlas of the Human Fascial System E‐Book. Amsterdam, Netherlands: Elsevier Health Sciences; 2014. | solo en papers |
| , | , | 6HeinbergC. E.KernE. B.The Cottle sign: an aid in the physical diagnose of nasal airflow disturbancesRhinology197311389942-s2.0-0015909721 | solo en papers |
| 23809686 | 10.1016/j.jped.2012.12.007 | 6HitosS. F.ArakakiR.SoléD.WeckxL. L. M.Oral breathing and speech disorders in childrenJornal de Pediatria201389436136510.1016/j.jped.2012.12.0072-s2.0-8488070647123809686 | solo en papers |
| 6354028 | 10.1164/arrd.1983.128.4.708 | 6MahadeviaA. K.OnalE.LopataM.Effects of expiratory positive airway pressure on sleep-induced respiratory abnormalities in patients with hypersomnia-sleep apnea syndromeAm | solo en papers |
| 7842764 | 10.1378/chest.107.2.375 | 6PepinJ. L.LegerP.VealeD.LangevinB.RobertD.LevyP.Side effects of nasal continuous positive airway pressure in sleep apnea syndrome: study of 193 patients in two French sl | solo en papers |
| 24533007 | 10.5664/jcsm.3460 | 6SutherlandK.VandervekenO. M.TsudaH.Oral appliance treatment for obstructive sleep apnea: an updateJournal of Clinical Sleep Medicine201410221522710.5664/jcsm.34602-s2.0- | solo en papers |
| , | , | 7 Schultz RL , Feitis R . The Endless Web: Fascial Anatomy and Physical Reality. Berkeley, CA, USA: North Atlantic Books; 2013. | solo en papers |
| , | 10.1590/s0034-72992005000100013 | 7BalbaniA. P. S.WeberS. A. T.MontovaniJ. C.Atualização em síndrome da apnéia obstrutiva do sono na infânciaRevista Brasileira de Otorrinolaringologia2005711748010.1590/s0 | solo en papers |
| 18363320 | 10.1093/sleep/31.3.429 | 7HeinzerR.WhiteD. P.MalhotraA.Effect of expiratory positive airway pressure on sleep disordered breathingSleep20083134294322-s2.0-421490850011836332010.1093/sleep/31.3.42 | solo en papers |
| 18468315 | , | 7KushidaC. A.ChediakA.BerryR. B.Clinical guidelines for the manual titration of positive airway pressure in patients with obstructive sleep apneaJournal of Clinical Sleep | solo en papers |
| 12409771 | 10.1097/00006534-200211000-00018 | 7RohrichR. J.GunterJ. P.DeuberM. A.AdamsW. P.Jr.The deviated nose: optimizing results using a simplified classification and algorithmic approachPlastic and Reconstructive | solo en papers |
| 21030210 | 10.1016/j.ijom.2010.09.007 | 7SusarlaS. M.ThomasR. J.AbramsonZ. R.KabanL. B.Biomechanics of the upper airway: changing concepts in the pathogenesis of obstructive sleep apneaInternational Journal of  | solo en papers |
| 31001444 | 10.1155/2019/3408053 | 8 Govardhan C , Murdock J , Norouz‐Knutsen L , Valcu‐Pinkerton S , Zaghi S . Lingual and maxillary labial frenuloplasty with myofunctional therapy as a treatment for mout | solo en papers |
| , | , | 8 Scoppa F . Glosso‐postural syndrome. Ann Stomatol 2005;54:27–34. | solo en papers |
| 19196857 | 10.1177/08903344090250011501 | 8. GennaC.W. CoryllosE.V. Breastfeeding and Tongue-TieJ. Hum. Lact.20092511111210.1177/0890334409025001150119196857 | solo en papers |
| , | 10.1590/s1516-18462008000400011 | 8CampanhaS. M. A.FreireL. M. S.FontesM. J. F.O impacto da asma, da rinite alérgica e da respiração oral na qualidade de vida de crianças e adolescentesRevista CEFAC200810 | solo en papers |
| 8564134 | 10.1164/ajrccm.153.2.8564134 | 8MeuriceJ.-C.MarcI.SérièsF.Efficacy of auto-CPAP in the treatment of obstructive sleep apnea/hypopnea syndromeAmerican Journal of Respiratory and Critical Care Medicine19 | solo en papers |
| 11801946 | 10.1097/00005537-200110000-00023 | 8PowellN. B.ZonatoA. I.WeaverE. M.Radiofrequency treatment of turbinate hypertrophy in subjects using continuous positive airway pressure: a randomized, double-blind, pla | solo en papers |
| 24604253 | 10.1001/jamafacial.2013.2473 | 8RheeJ. S.SullivanC. D.FrankD. O.KimbellJ. S.GarciaG. J. M.A systematic review of patient-reported nasal obstruction scores: defining normative and symptomatic ranges in  | solo en papers |
| 26220154 | , | 8RiazM.CertalV.CamachoM.Portable power supply options for positive airway pressure devicesRural and Remote Health2015153p. 349926220154 | solo en papers |
| 25941312 | 10.1542/peds.2015-0660 | 9 Chinnadurai S , Francis DO , Epstein RA , Morad A , Kohanim S , McPheeters M . Treatment of ankyloglossia for reasons other than breastfeeding: a systematic review. Ped | solo en papers |
| , | , | 9. HazelbakerA. The Assessment Tool for Lingual Frenulum Function (ATLFF): Use in a Lactation Consultant Private Practice. A Protocol1993Available online: https://hazelba | solo en papers |
| , | , | 9ChedidK. A. K.FrancescoR. C. D.JunqueiraP. AdS.The influence of mouth breathing on reading and writing learning in preschool childrenRevista Psicopedagogia20042165157163 | solo en papers |
| 21711978 | 10.2500/ajra.2011.25.3558 | 9LiH.-Y.WangP.-C.ChenY.-P.LeeL.-A.FangT.-J.LinH.-C.Critical appraisal and meta-analysis of nasal surgery for obstructive sleep apneaAmerican Journal of Rhinology & Allerg | solo en papers |
| 20171303 | 10.1016/j.ijsu.2010.02.007 | 9MoherD.LiberatiA.TetzlaffJ.AltmanD. G.Preferred reporting items for systematic reviews and meta-analyses: the PRISMA statementInternational Journal of Surgery20108533634 | solo en papers |

## Solo en vídeos (no aparecen en las referencias de sus artículos)


- Andrews (línea G)
- Boyd (Kevin)
- Catlin 1870; Rogers 1918; Angle 1907; Straub 1950; Bianchini 1993
- Dickens 1836 (*Pickwick Papers*); serie de 1977 de traqueostomía (15 pacientes)
- Emerson 1860; Haskin 1912
- Lchnowski (2022? / 2025-2026), RCT
- Revisión retrospectiva (2011), 400 niños de 2-17 años
- Rocabado (vía Valerie Sinkins)
- Salt et al. 2021 (habla)
- Tweed 1995
- Vivaer, RCTs de nivel 1

---

<!-- archivo: expertos/soroush-zaghi/reglas-decision.md -->
# Reglas de decisión

Ideas públicas de Soroush Zaghi sobre este tema, reconstruidas a partir de sus vídeos. **No es Zaghi hablando ni una guía clínica.** Cómo leer cada entrada: README. Entradas: 91.

## zag-0177 · Estudio citado · sin verificar (dicho en vídeo)

Christian Guilleminault et al. (2013), revista "Sleep Medicine". Estudio que demuestra que la ausencia de reeducación miofuncional tras una adenoamigdalectomía se asocia con la recurrencia de la apnea del sueño.

- Vídeo: [Pediatric Sleep Disordered Breathing and Maxillofacial Development with Soroush Zaghi](https://www.youtube.com/watch?v=eA1Yqbruw4g), minuto `PENDIENTE DE VERIFICAR`.
- Vídeo: [Full Lecture: Evaluation, Diagnosis, and Treatment of Tongue, Lip, & Buccal Ties, Dr. Soroush Zaghi](https://www.youtube.com/watch?v=iP3c-C9L9b0), minuto `PENDIENTE DE VERIFICAR`.
- Estudio: PMID [23522724](https://pubmed.ncbi.nlm.nih.gov/23522724/), ficha 2013-guilleminault-reeducacion-miofascial.md.

## zag-0441 · Experiencia clínica · sin verificar (dicho en vídeo)

Zaghi recomienda pedir un CBCT sin dudar si se observa un "lenguaje festoneado" (scalloping) severo o un "desbordamiento lingual" (tongue overflow), donde la lengua sobrepasa la superficie lingual de los molares superiores.

- Vídeo: [FAirEST 6 + 4](https://www.youtube.com/watch?v=ckwLiTMb7wo), minuto `PENDIENTE DE VERIFICAR`.

## zag-0442 · Experiencia clínica · sin verificar (dicho en vídeo)

Zaghi indica que si el paciente presenta un "aleteo palatino" (palatal flutter) positivo ,es decir, puede roncar con la boca abierta pero no cuando pone la lengua en el paladar, se debe solicitar un CBCT para evaluar si el problema es el espacio óseo y no solo el frenillo.

- Vídeo: [FAirEST 6 + 4](https://www.youtube.com/watch?v=ckwLiTMb7wo), minuto `PENDIENTE DE VERIFICAR`.

## zag-0443 · Experiencia clínica · sin verificar (dicho en vídeo)

Zaghi pide el CBCT para determinar si el paciente tiene una deficiencia esquelética maxilar que impida que la lengua quepa en el paladar tras ser liberada.

- Vídeo: [Excerpts From - TBI Ambassador Update (December 2024). Now Available On-Demand!](https://www.youtube.com/watch?v=DshE1KHc9s0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2024.

## zag-0444 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, pide el CBCT cuando hay sospecha de Apnea Obstructiva del Sueño o Síndrome de Resistencia de la Vía Aérea Superior (UARS), para visualizar colapsos estructurales que el estudio de sueño no explica por sí solo.

- Vídeo: [Drug Induced Sleep Endoscopy (DISE) - Dr. Soroush Zaghi](https://www.youtube.com/watch?v=Sn9nntkyOoI), minuto `PENDIENTE DE VERIFICAR`.

## zag-0445 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, el paciente debe estar en "Posición Natural de la Cabeza" (Natural Head Position - NHP), mirando directamente a un espejo para mantener un eje visual horizontal.

- Vídeo: [CBCT Protocol With The Breathe Institute For Proper Airway Measurements](https://www.youtube.com/watch?v=tn6o08wn5j0), minuto `PENDIENTE DE VERIFICAR`.

## zag-0446 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, los labios deben estar sellados y los dientes en contacto (teeth together). Si los dientes están separados, la medición del área transversal aumenta artificialmente.

- Vídeo: [CBCT Protocol With The Breathe Institute For Proper Airway Measurements](https://www.youtube.com/watch?v=tn6o08wn5j0), minuto `PENDIENTE DE VERIFICAR`.

## zag-0447 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, el paciente debe tragar una vez y luego dejar la lengua en su postura de reposo natural durante todo el escaneo.

- Vídeo: [CBCT Protocol With The Breathe Institute For Proper Airway Measurements](https://www.youtube.com/watch?v=tn6o08wn5j0), minuto `PENDIENTE DE VERIFICAR`.

## zag-0448 · Experiencia clínica · sin verificar (dicho en vídeo)

Zaghi prohíbe el uso de soporte para el mentón (chin rest) y de registro de mordida (bite registration).

- Vídeo: [FAirEST 6 + 4](https://www.youtube.com/watch?v=ckwLiTMb7wo), minuto `PENDIENTE DE VERIFICAR`.
- Vídeo: [Updates from Dr. Soroush Zaghi - The Breathe Institute at ALSC Symposium 2024](https://www.youtube.com/watch?v=iGQlzOtT4C0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2024.

## zag-0449 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, el soporte del mentón empuja la lengua hacia arriba artificialmente y altera la postura del cuello, ocultando la obstrucción real.

- Vídeo: [FAirEST 6 + 4](https://www.youtube.com/watch?v=ckwLiTMb7wo), minuto `PENDIENTE DE VERIFICAR`.

## zag-0450 · Estudio citado · sin verificar (dicho en vídeo)

Kevin Coppelson cita que, según estudios radiográficos de vía aérea, el área transversal mínima no debería estar por debajo de los 150 mm² o incluso 200 mm² en el punto más estrecho del espacio faríngeo posterior.

- Vídeo: [Advances in Surgical Technique with Dr. Kevin Coppelson - BreatheMAX - 10/28/24](https://www.youtube.com/watch?v=gsAggiqvgEY), minuto `PENDIENTE DE VERIFICAR`.

## zag-0451 · Experiencia clínica · sin verificar (dicho en vídeo)

Zaghi analiza el MCA corte por corte; por ejemplo, un paciente con 68.7 mm² se considera extremadamente estrecho (zona negra en el gráfico).

- Vídeo: [Excerpts From - TBI Ambassador Update (December 2024). Now Available On-Demand!](https://www.youtube.com/watch?v=DshE1KHc9s0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2024.

## zag-0452 · Estudio citado · sin verificar (dicho en vídeo)

Según Zaghi, el mismo estudio indica que 10° de inclinación alteran la vía aérea en un 88% y 20° en un 150%.

- Vídeo: [FAirEST 6 + 4](https://www.youtube.com/watch?v=ckwLiTMb7wo), minuto `PENDIENTE DE VERIFICAR`.

## zag-0453 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, un hioides bajo en el CBCT es un "delator" de que la lengua no tiene soporte. Se asocia con un ángulo cervical-mental cercano a 180° (cuello plano) en lugar de los <120° ideales.

- Vídeo: [Evolution Of Myofunctional Therapy, Lingual Frenuloplasty - Dr. Soroush Zaghi at ALSC 2026.](https://www.youtube.com/watch?v=nlFVT6PUaYc), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2026.

## zag-0454 · Experiencia clínica · sin verificar (dicho en vídeo)

Zaghi advierte que en pacientes con un CBCT que muestra una boca extremadamente estrecha, la inflamación posoperatoria puede comprimir la lengua contra los dientes, causando isquemia y entumecimiento persistente en la punta.

- Vídeo: [Dr. Soroush Zaghi at ALSC - Breathe and Thrive 2022, in Las Vegas, NV](https://www.youtube.com/watch?v=3fq6w2buIy0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2022.

## zag-0455 · Opinión · sin verificar (dicho en vídeo)

Zaghi señala que si el CBCT muestra aire separando el paladar de la lengua, es una prueba física de que la lengua está caída y bloqueando la vía aérea.

- Vídeo: [Tongue-Tie, Sleep, Breathing, and Myofunctional Therapy: New Research Updates. Dr. Zaghi at ALSC '20](https://www.youtube.com/watch?v=G9GrUw7YJD0), minuto `PENDIENTE DE VERIFICAR`.

## zag-0456 · Experiencia clínica · sin verificar (dicho en vídeo)

Zaghi observó en un estudio piloto (P=0.041) que la vía aérea se ve más aplanada y ancha cuando el paciente está sentado, y más larga y estrecha cuando está de pie.

- Vídeo: [Dr. Zaghi on Research Principles (From TBI's Outlook at AAPMD Collaboration Cures Conference, 2021)](https://www.youtube.com/watch?v=vYQ1mv8Gdf0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2021.

## zag-0457 · Estudio citado · sin verificar (dicho en vídeo)

Zaghi menciona un artículo de investigación recientemente publicado (sin citar autor/año en el clip) que establece que roncar durante el 5% del tiempo total de sueño es un factor diagnóstico clave para el Síndrome de Resistencia de la Vía Aérea Superior (UARS).

- Vídeo: [Dr. Soroush Zaghi at ALSC - Breathe and Thrive 2022, in Las Vegas, NV](https://www.youtube.com/watch?v=3fq6w2buIy0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2022.

## zag-0458 · Experiencia clínica · sin verificar (dicho en vídeo)

Zaghi utiliza este umbral del 5% para dar diagnósticos alternativos; si un paciente ronca, por ejemplo, el 12% del tiempo, lo considera patológico aunque el IAH sea normal.

- Vídeo: [Dr. Soroush Zaghi at ALSC - Breathe and Thrive 2022, in Las Vegas, NV](https://www.youtube.com/watch?v=3fq6w2buIy0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2022.

## zag-0459 · Estudio citado · sin verificar (dicho en vídeo)

Basándose en las investigaciones de su mentor, Christian Guilleminault, Zaghi afirma que la respiración bucal durante más del 10% del tiempo de sueño se clasifica como patológica.

- Vídeo: [Long-term Implications of Untreated Tongue-Tie (Dr. Soroush Zaghi, The Breathe Institute)](https://www.youtube.com/watch?v=cuT6qrm5IT0), minuto `PENDIENTE DE VERIFICAR`.
- Vídeo: [Functional Approach to Sleep and Breathing + Frenuloplasty Course (AUSTRALIA APRIL 2019)](https://www.youtube.com/watch?v=S-xjr-6ade4), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2019.

## zag-0460 · Experiencia clínica · sin verificar (dicho en vídeo)

Zaghi considera un signo de alarma severo cuando un niño presenta una latencia de sueño REM extremadamente prolongada (por ejemplo, 320 minutos para alcanzar un poco de REM), lo que indica que el niño sale del sueño profundo constantemente para evitar asfixiarse.

- Vídeo: [Dr. Soroush Zaghi at ALSC - Breathe and Thrive 2022, in Las Vegas, NV](https://www.youtube.com/watch?v=3fq6w2buIy0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2022.

## zag-0461 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, en casos de UARS, el IAH puede ser < 5 y el oxígeno mantenerse > 92%, pero el Índice de Despertares o el RDI (Índice de Perturbación Respiratoria) estará por encima de 10 eventos por hora debido al esfuerzo respiratorio.

- Vídeo: [Pediatric and Adult Sleep Medicine - Key Takeaways with Dr. Soroush Zaghi](https://www.youtube.com/watch?v=J0jS05tFj1w), minuto `PENDIENTE DE VERIFICAR`.

## zag-0462 · Experiencia clínica · sin verificar (dicho en vídeo)

Zaghi advierte que el mayor riesgo es un falso negativo, donde un estudio de laboratorio dice que el niño es "normal" pero el niño está "luchando por respirar" (increased effort), lo cual es muy común porque el 90% de los trastornos pediátricos son no-hipóxicos (no hay caída de oxígeno).

- Vídeo: [Dr. Soroush Zaghi at ALSC - Breathe and Thrive 2022, in Las Vegas, NV](https://www.youtube.com/watch?v=3fq6w2buIy0), minuto `PENDIENTE DE VERIFICAR`.
- Vídeo: [Long-term Implications of Untreated Tongue-Tie (Dr. Soroush Zaghi, The Breathe Institute)](https://www.youtube.com/watch?v=cuT6qrm5IT0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2022.

## zag-0464 · Experiencia clínica · sin verificar (dicho en vídeo)

Zaghi prefiere usar el diagnóstico de "Trastorno Respiratorio Obstructivo del Sueño" (OSDB) porque engloba la respiración bucal, el ronquido y el UARS, evitando que los pacientes queden sin tratamiento por no cumplir los criterios estrictos de la apnea obstructiva (OSA).

- Vídeo: [Dr. Soroush Zaghi at ALSC - Breathe and Thrive 2022, in Las Vegas, NV](https://www.youtube.com/watch?v=3fq6w2buIy0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2022.

## zag-0465 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, si un niño tiene síntomas de TDAH (ADHD), agresividad, mojar la cama (enuresis), sudoración nocturna o bajo rendimiento académico, Zaghi considera que estos son hallazgos suficientes para tratar la vía aérea incluso si el estudio de sueño es normal.

- Vídeo: [Dr. Soroush Zaghi on the impact of Tongue-ties on Sleep Disordered Breathing in Kids](https://www.youtube.com/watch?v=tdnmhBv6Zg4), minuto `PENDIENTE DE VERIFICAR`.
- Vídeo: [Long-term Implications of Untreated Tongue-Tie (Dr. Soroush Zaghi, The Breathe Institute)](https://www.youtube.com/watch?v=cuT6qrm5IT0), minuto `PENDIENTE DE VERIFICAR`.

## zag-0466 · Experiencia clínica · sin verificar (dicho en vídeo)

Ante la falta de fiabilidad de los estudios de laboratorio, Zaghi recomienda a los padres realizar una "Video Cámara Sleep Screening" para observar si el niño tiene retracciones en el pecho o una postura de cabeza extendida para abrir la vía aérea.

- Vídeo: [Pediatric Sleep Disordered Breathing and Maxillofacial Development with Soroush Zaghi](https://www.youtube.com/watch?v=eA1Yqbruw4g), minuto `PENDIENTE DE VERIFICAR`.
- Vídeo: [Long-term Implications of Untreated Tongue-Tie (Dr. Soroush Zaghi, The Breathe Institute)](https://www.youtube.com/watch?v=cuT6qrm5IT0), minuto `PENDIENTE DE VERIFICAR`.

## zag-0467 · Estudio citado · sin verificar (dicho en vídeo)

Christian Guilleminault (1976). Reportó los primeros 8 casos de apnea pediátrica y notó que los síntomas (conducta, mojar la cama) diferían de los adultos.

- Vídeo: [Dr. Soroush Zaghi on the impact of Tongue-ties on Sleep Disordered Breathing in Kids](https://www.youtube.com/watch?v=tdnmhBv6Zg4), minuto `PENDIENTE DE VERIFICAR`.

## zag-0468 · Estudio citado · sin verificar (dicho en vídeo)

Según Zaghi, estudio de cohorte retrospectivo (2004). Demostró que el 15% de los niños tienen síntomas persistentes tras la cirugía de amígdalas, lo que apunta a causas craneofaciales y de postura lingual.

- Vídeo: [Dr. Soroush Zaghi on the impact of Tongue-ties on Sleep Disordered Breathing in Kids](https://www.youtube.com/watch?v=tdnmhBv6Zg4), minuto `PENDIENTE DE VERIFICAR`.

## zag-0469 · Experiencia clínica · sin verificar (dicho en vídeo)

Zaghi indica cirugía nasal solo cuando es necesaria para corregir una obstrucción estructural real, distinguiéndola de la obstrucción habitual por respiración bucal donde el pasaje es anatómicamente patente.

- Vídeo: [Functional Approach to Sleep and Breathing + Frenuloplasty Course (AUSTRALIA APRIL 2019)](https://www.youtube.com/watch?v=S-xjr-6ade4), minuto `PENDIENTE DE VERIFICAR`.
- Vídeo: [Pediatric and Adult Sleep Medicine - Key Takeaways with Dr. Soroush Zaghi](https://www.youtube.com/watch?v=J0jS05tFj1w), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2019.

## zag-0473 · Estudio citado · sin verificar (dicho en vídeo)

Según estudios citados por Zaghi sobre el implante Latera, este se absorbe y es reemplazado por el colágeno natural del paciente en un periodo de 12 a 18 meses, estabilizando la válvula.

- Vídeo: [Live Latera Nasal Valve Implant Procedure for Nasal Obstruction with Dr. Zaghi and 1 week Followup](https://www.youtube.com/watch?v=Cm7chrBRz14), minuto `PENDIENTE DE VERIFICAR`.

## zag-0474 · Experiencia clínica · sin verificar (dicho en vídeo)

Zaghi afirma haber refinado la técnica de radiofrecuencia (Breathe RF), haciéndola más precisa, mejor tolerada y con menos inflamación que la técnica convencional de Vivaer.

- Vídeo: [Evolution Of Myofunctional Therapy, Lingual Frenuloplasty - Dr. Soroush Zaghi at ALSC 2026.](https://www.youtube.com/watch?v=nlFVT6PUaYc), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2026.

## zag-0475 · Experiencia clínica · sin verificar (dicho en vídeo)

Zaghi desaconseja operar inmediatamente los cornetes si la inflamación es reactiva a la respiración bucal; el aire seco que entra por la boca irrita la nariz y hace que esta se congestione para intentar humedecer el aire.

- Vídeo: [Tongue-Tie, Sleep, Breathing, and Myofunctional Therapy: New Research Updates. Dr. Zaghi at ALSC '20](https://www.youtube.com/watch?v=G9GrUw7YJD0), minuto `PENDIENTE DE VERIFICAR`.

## zag-0476 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, antes de cualquier cirugía nasal, el protocolo exige establecer higiene nasal (lavados con xilitol/salinos como X-lear) y manejo de alergias para ver si la obstrucción se resuelve sin bisturí.

- Vídeo: [Long-term Implications of Untreated Tongue-Tie (Dr. Soroush Zaghi, The Breathe Institute)](https://www.youtube.com/watch?v=cuT6qrm5IT0), minuto `PENDIENTE DE VERIFICAR`.

## zag-0477 · Opinión · sin verificar (dicho en vídeo)

Zaghi sostiene que un paladar alto y estrecho (v-shape) suele causar que el tabique nasal se doble (buckling) por falta de espacio vertical, creando una desviación estructural que puede mejorar con expansión ósea en lugar de cirugía nasal aislada.

- Vídeo: [Updates from Dr. Soroush Zaghi - The Breathe Institute at ALSC Symposium 2024](https://www.youtube.com/watch?v=iGQlzOtT4C0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2024.

## zag-0478 · Estudio citado · sin verificar (dicho en vídeo)

Audrey Yoon, Stanley Liu, Rebecca Volkow et al. demostraron que la expansión palatina rápida en niños puede reducir significativamente el volumen de adenoides y amígdalas al facilitar la transición a la respiración nasal.

- Vídeo: [Pediatric Sleep Disordered Breathing and Maxillofacial Development with Soroush Zaghi](https://www.youtube.com/watch?v=eA1Yqbruw4g), minuto `PENDIENTE DE VERIFICAR`.

## zag-0479 · Experiencia clínica · sin verificar (dicho en vídeo)

Zaghi advierte contra la cirugía nasal sobre-agresiva, ya que puede derivar en el "Síndrome de Nariz Vacía" (Empty Nose Syndrome), donde el paciente siente que se asfixia a pesar de tener una nariz anatómicamente abierta porque los sensores de flujo de aire han sido dañados.

- Vídeo: [Tongue-Tie, Sleep, Breathing, and Myofunctional Therapy: New Research Updates. Dr. Zaghi at ALSC '20](https://www.youtube.com/watch?v=G9GrUw7YJD0), minuto `PENDIENTE DE VERIFICAR`.

## zag-0480 · Opinión · sin verificar (dicho en vídeo)

Zaghi sostiene que su técnica MIND (expansión naso-maxilar mínimamente invasiva) es a menudo preferible porque aumenta el volumen nasal tridimensionalmente desde la base ósea, mejorando la estética y la función sin necesidad de cortes nasales extensos.

- Vídeo: [Advances in Surgical Technique with Dr. Kevin Coppelson - BreatheMAX - 10/28/24](https://www.youtube.com/watch?v=gsAggiqvgEY), minuto `PENDIENTE DE VERIFICAR`.

## zag-0481 · Experiencia clínica · sin verificar (dicho en vídeo)

Zaghi relata que, tras ser diagnosticada con colapso de válvula nasal en un entrenamiento de CBCT, el uso del dilator nasal magnético "Intake" fue suficiente para mejorar sus entrenamientos y memoria, posponiendo la necesidad de cirugía.

- Vídeo: [Intake Nasal Dilator Strips - at The Breathe Institute](https://www.youtube.com/watch?v=PmTDWNRh96w), minuto `PENDIENTE DE VERIFICAR`.

## zag-0482 · Estudio citado · sin verificar (dicho en vídeo)

Zaghi, Coppelson et al. (2024), Journal of Oral and Maxillofacial Surgery (JOMS). Validaron que la postura del paciente altera drásticamente las medidas de la vía aérea en el CBCT, por lo que la decisión quirúrgica no debe basarse solo en una imagen estática sin protocolo.

- Vídeo: [Advances in Surgical Technique with Dr. Kevin Coppelson - BreatheMAX - 10/28/24](https://www.youtube.com/watch?v=gsAggiqvgEY), minuto `PENDIENTE DE VERIFICAR`.

## zag-0483 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, indica el CPAP en adultos que están perdiendo oxígeno (saturaciones por debajo del 90% u 80%) y corren riesgo de eventos cardíacos. El objetivo es estabilizarlos primero para luego buscar una cura quirúrgica o funcional.

- Vídeo: [Pediatric and Adult Sleep Medicine - Key Takeaways with Dr. Soroush Zaghi](https://www.youtube.com/watch?v=J0jS05tFj1w), minuto `PENDIENTE DE VERIFICAR`.

## zag-0484 · Experiencia clínica · sin verificar (dicho en vídeo)

Zaghi observa que muchos pacientes no toleran el CPAP porque su lengua colapsa hacia atrás y bloquea el flujo de aire de la máquina. En estos casos, la cirugía de lengua o la terapia miofuncional se indican para mejorar la adherencia al CPAP.

- Vídeo: [Pediatric and Adult Sleep Medicine - Key Takeaways with Dr. Soroush Zaghi](https://www.youtube.com/watch?v=J0jS05tFj1w), minuto `PENDIENTE DE VERIFICAR`.

## zag-0485 · Estudio citado · sin verificar (dicho en vídeo)

Zaghi cita un estudio del Journal Pediatrics (1995) que indica que el CPAP es seguro en niños, pero Zaghi advierte que estudios posteriores mostraron que la presión de la máscara restringe el crecimiento hacia adelante de la cara media.

- Vídeo: [Dr. Soroush Zaghi on the impact of Tongue-ties on Sleep Disordered Breathing in Kids](https://www.youtube.com/watch?v=tdnmhBv6Zg4), minuto `PENDIENTE DE VERIFICAR`.
- Vídeo: [Pediatric Sleep Disordered Breathing and Maxillofacial Development with Soroush Zaghi](https://www.youtube.com/watch?v=eA1Yqbruw4g), minuto `PENDIENTE DE VERIFICAR`.

## zag-0486 · Opinión · sin verificar (dicho en vídeo)

Según Zaghi, en su práctica, el CPAP es el "último recurso" en pediatría porque los niños no suelen ser hipóxicos y el objetivo debe ser el crecimiento facial y la respiración nasal natural.

- Vídeo: [Pediatric Sleep Disordered Breathing and Maxillofacial Development with Soroush Zaghi](https://www.youtube.com/watch?v=eA1Yqbruw4g), minuto `PENDIENTE DE VERIFICAR`.

## zag-0487 · Experiencia clínica · sin verificar (dicho en vídeo)

Zaghi reporta que si se libera la lengua en una boca de < 32 mm, el paciente puede terminar en la UCI debido a que la inflamación comprime la lengua contra los dientes e impide el retorno venoso, o bien empeora la apnea al no tener espacio la lengua para subir.

- Vídeo: [Updates from Dr. Soroush Zaghi - The Breathe Institute at ALSC Symposium 2024](https://www.youtube.com/watch?v=iGQlzOtT4C0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2024.

## zag-0488 · Estudio citado · sin verificar (dicho en vídeo)

Zaghi cita estudios que muestran que los aparatos extraíbles o de alambre ligero (como Crozat o DNA) solo logran entre 2 y 6 mm de expansión (promedio 2.4 mm). Si el paciente necesita más de 6 mm para llegar al ideal de 38-42 mm, se indica expansión esquelética (MARPE/Mind).

- Vídeo: [Updates from Dr. Soroush Zaghi - The Breathe Institute at ALSC Symposium 2024](https://www.youtube.com/watch?v=iGQlzOtT4C0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2024.

## zag-0489 · Experiencia clínica · sin verificar (dicho en vídeo)

Zaghi indica la expansión (Mind/MARPE) para ensanchar la base de la nariz y tratar el colapso de la válvula nasal desde el hueso, mejorando el volumen nasal tridimensionalmente.

- Vídeo: [Updates from Dr. Soroush Zaghi - The Breathe Institute at ALSC Symposium 2024](https://www.youtube.com/watch?v=iGQlzOtT4C0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2024.

## zag-0490 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, indica el avance maxilomandibular (MMA) en pacientes con apnea severa, un hioides muy bajo y un ángulo postural NBC3 compensado (>120°) donde la mandíbula está físicamente retraída hacia la columna.

- Vídeo: [Updates from Dr. Soroush Zaghi - The Breathe Institute at ALSC Symposium 2024](https://www.youtube.com/watch?v=iGQlzOtT4C0), minuto `PENDIENTE DE VERIFICAR`.
- Vídeo: [Evolution Of Myofunctional Therapy, Lingual Frenuloplasty - Dr. Soroush Zaghi at ALSC 2026.](https://www.youtube.com/watch?v=nlFVT6PUaYc), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2026.
- Estudio: PMID [36841260](https://pubmed.ncbi.nlm.nih.gov/36841260/), ficha 2023-coppelson-postura-cbct.md.

## zag-0492 · Estudio citado · verificado en PubMed

Zaghi realizó un meta-análisis (45 estudios, 518 pacientes) que muestra que el MMA tiene una tasa de mejora del 65 al 80%. Sin embargo, advierte que pocos pacientes se "curan" al 100% sin añadir terapia miofuncional posterior para el tono de la lengua.

- Vídeo: [Full Lecture: Evaluation, Diagnosis, and Treatment of Tongue, Lip, & Buccal Ties, Dr. Soroush Zaghi](https://www.youtube.com/watch?v=iP3c-C9L9b0), minuto `PENDIENTE DE VERIFICAR`.
- Estudio: PMID [26606321](https://pubmed.ncbi.nlm.nih.gov/26606321/), ficha 2016-zaghi-mma-metaanalisis.md.

## zag-0493 · Experiencia clínica · sin verificar (dicho en vídeo)

Zaghi indica MMA en casos de mordida abierta anterior que han fracasado con ortodoncia, ya que suele ser un signo de una vía aérea pequeña no diagnosticada.

- Vídeo: [Advances in Surgical Technique with Dr. Kevin Coppelson - BreatheMAX - 10/28/24](https://www.youtube.com/watch?v=gsAggiqvgEY), minuto `PENDIENTE DE VERIFICAR`.

## zag-0494 · Experiencia clínica · sin verificar (dicho en vídeo)

Zaghi deriva sistemáticamente para realizar un mes de terapia preoperatoria y dos meses de terapia posoperatoria en casos de frenuloplastia funcional.

- Vídeo: [Tongue-Tie, Sleep, Breathing, and Myofunctional Therapy: New Research Updates. Dr. Zaghi at ALSC '20](https://www.youtube.com/watch?v=G9GrUw7YJD0), minuto `PENDIENTE DE VERIFICAR`.
- Vídeo: [Functional Approach to Sleep and Breathing + Frenuloplasty Course (AUSTRALIA APRIL 2019)](https://www.youtube.com/watch?v=S-xjr-6ade4), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2019.

## zag-0496 · Opinión · sin verificar (dicho en vídeo)

Según Zaghi, realizar una cirugía de frenillo sin terapia es como hacer una cirugía de hombro sin fisioterapia; el riesgo de cicatrización restrictiva y fracaso funcional es muy alto.

- Vídeo: [Functional Approach to Frenuloplasty: How We Do It - Dr. Soroush Zaghi](https://www.youtube.com/watch?v=C0kel5PNc7c), minuto `PENDIENTE DE VERIFICAR`.

## zag-0497 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, si el CBCT muestra "tongue overflow" (desbordamiento lingual) o "scalloping" (festoneado) severo, el paciente es derivado a ortodoncia antes de la cirugía de lengua.

- Vídeo: [FAirEST 6 + 4](https://www.youtube.com/watch?v=ckwLiTMb7wo), minuto `PENDIENTE DE VERIFICAR`.
- Vídeo: [Excerpts From - TBI Ambassador Update (December 2024). Now Available On-Demand!](https://www.youtube.com/watch?v=DshE1KHc9s0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2024.

## zag-0498 · Experiencia clínica · sin verificar (dicho en vídeo)

Zaghi recomienda expandir primero si el paladar es muy estrecho porque liberar la lengua en una "jaula" pequeña puede causar que esta colapse hacia atrás y empeore la apnea o cause isquemia por inflamación.

- Vídeo: [Dr. Soroush Zaghi at ALSC - Breathe and Thrive 2022, in Las Vegas, NV](https://www.youtube.com/watch?v=3fq6w2buIy0), minuto `PENDIENTE DE VERIFICAR`.
- Vídeo: [Updates from Dr. Soroush Zaghi - The Breathe Institute at ALSC Symposium 2024](https://www.youtube.com/watch?v=iGQlzOtT4C0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2024.

## zag-0499 · Estudio citado · sin verificar (dicho en vídeo)

Audrey Yoon, Stanley Liu et al. (2020), revista "Sleep". Estudio sobre el protocolo DOME que muestra reducciones significativas del IAH mediante expansión ósea maxilar.

- Vídeo: [Updates from Dr. Soroush Zaghi - The Breathe Institute at ALSC Symposium 2024](https://www.youtube.com/watch?v=iGQlzOtT4C0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2024.
- Estudio: PMID [31606311](https://pubmed.ncbi.nlm.nih.gov/31606311/), ficha 2020-yoon-dome.md.

## zag-0500 · Experiencia clínica · sin verificar (dicho en vídeo)

Zaghi deriva al Dr. Kevin Coppelson para Cirugía de Avance Maxilomandibular (MMA) o expansión MIND si el CBCT muestra una vía aérea retrolingual menor a 150-200 mm² de área transversal mínima (MCA).

- Vídeo: [Advances in Surgical Technique with Dr. Kevin Coppelson - BreatheMAX - 10/28/24](https://www.youtube.com/watch?v=gsAggiqvgEY), minuto `PENDIENTE DE VERIFICAR`.
- Estudio: PMID [26606321](https://pubmed.ncbi.nlm.nih.gov/26606321/), ficha 2016-zaghi-mma-metaanalisis.md.

## zag-0501 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, en pacientes con apnea severa, el hioides bajo y un ángulo postural NBC3 compensado (>120°), la cirugía de frenillo es secundaria; lo que realmente necesitan es una intervención de espacio como MARPE o MMA.

- Vídeo: [Updates from Dr. Soroush Zaghi - The Breathe Institute at ALSC Symposium 2024](https://www.youtube.com/watch?v=iGQlzOtT4C0), minuto `PENDIENTE DE VERIFICAR`.
- Vídeo: [Excerpts From - TBI Ambassador Update (December 2024). Now Available On-Demand!](https://www.youtube.com/watch?v=DshE1KHc9s0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2024.
- Estudio: PMID [36841260](https://pubmed.ncbi.nlm.nih.gov/36841260/), ficha 2023-coppelson-postura-cbct.md.

## zag-0502 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, en pacientes adultos con apnea obstructiva severa (OSA) e hipoxia, el CPAP es paliativo, pero el MMA es a menudo la única opción curativa estructural.

- Vídeo: [Pediatric and Adult Sleep Medicine - Key Takeaways with Dr. Soroush Zaghi](https://www.youtube.com/watch?v=J0jS05tFj1w), minuto `PENDIENTE DE VERIFICAR`.

## zag-0503 · Estudio citado · verificado en PubMed

Zaghi et al. Meta-análisis de 45 estudios (518 pacientes) sobre MMA que muestra una tasa de éxito (reducción del 50% del IAH) de entre el 65% y el 80%.

- Vídeo: [Full Lecture: Evaluation, Diagnosis, and Treatment of Tongue, Lip, & Buccal Ties, Dr. Soroush Zaghi](https://www.youtube.com/watch?v=iP3c-C9L9b0), minuto `PENDIENTE DE VERIFICAR`.
- Estudio: PMID [26606321](https://pubmed.ncbi.nlm.nih.gov/26606321/), ficha 2016-zaghi-mma-metaanalisis.md.

## zag-0505 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, la patencia nasal es un prerrequisito para el éxito de la cirugía de lengua; si la nariz está bloqueada, la lengua siempre estará baja para permitir la respiración bucal.

- Vídeo: [Myofunctional Therapy and Frenuloplasty Can Be Appropriate Treatments for Obstructive Sleep Apnea](https://www.youtube.com/watch?v=dlU8wxa8474), minuto `PENDIENTE DE VERIFICAR`.

## zag-0506 · Experiencia clínica · sin verificar (dicho en vídeo)

Zaghi deriva a especialistas como Cynthia Butler o Dr. Neil para pacientes con Síndrome de Ehlers-Danlos (EDS) o hipermovilidad, donde el objetivo no es estirar sino estabilizar.

- Vídeo: [Evolution Of Myofunctional Therapy, Lingual Frenuloplasty - Dr. Soroush Zaghi at ALSC 2026.](https://www.youtube.com/watch?v=nlFVT6PUaYc), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2026.

## zag-0507 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, deriva cuando hay tortícolis, escoliosis o dolor miofascial crónico (cuello, hombros, espalda) que no cede con intervenciones orales.

- Vídeo: [Frenums, Fascia and Physiology by Dr. Soroush Zaghi & Sanda Valcu-Pinkerton, COM - at AAPMD 2019](https://www.youtube.com/watch?v=BM3TmSXhUIw), minuto `PENDIENTE DE VERIFICAR`.
- Vídeo: [Dr. Soroush Zaghi at Tongue Time 2026 in Zurich, Switzerland  (Full Lecture)](https://www.youtube.com/watch?v=y6VkQnMBBvc), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2026.

## zag-0509 · Experiencia clínica · sin verificar (dicho en vídeo)

Zaghi advierte sobre los "falsos negativos" en niños; deriva para estudios de sueño para documentar el esfuerzo respiratorio (RDI) y los micro-despertares, no solo la apnea hipóxica.

- Vídeo: [Pediatric Sleep Disordered Breathing and Maxillofacial Development with Soroush Zaghi](https://www.youtube.com/watch?v=eA1Yqbruw4g), minuto `PENDIENTE DE VERIFICAR`.
- Vídeo: [Drug Induced Sleep Endoscopy (DISE) - Dr. Soroush Zaghi](https://www.youtube.com/watch?v=Sn9nntkyOoI), minuto `PENDIENTE DE VERIFICAR`.

## zag-0510 · Opinión · sin verificar (dicho en vídeo)

Según Zaghi, si se libera la lengua (la correa) en una jaula demasiado pequeña (paladar estrecho), la lengua no tendrá donde subir y caerá hacia atrás, bloqueando la vía aérea retrolingual.

- Vídeo: [Tongue-Tie, Sleep, Breathing, and Myofunctional Therapy: New Research Updates. Dr. Zaghi at ALSC '20](https://www.youtube.com/watch?v=G9GrUw7YJD0), minuto `PENDIENTE DE VERIFICAR`.

## zag-0511 · Experiencia clínica · sin verificar (dicho en vídeo)

Zaghi reporta casos (aprox. 10-20 de 5,000) donde la apnea del sueño empeoró drásticamente (el IAH subió de 17 a 56) tras una frenuloplastia porque el paciente fue "desestabilizado" al perder sus compensaciones posturales en una boca sin espacio.

- Vídeo: [Updates from Dr. Soroush Zaghi - The Breathe Institute at ALSC Symposium 2024](https://www.youtube.com/watch?v=iGQlzOtT4C0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2024.

## zag-0512 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, en niños, si tras intentar la terapia el paciente es incapaz de lograr el sello palatino (LPS) debido a un paladar excesivamente alto y estrecho, se debe expandir primero para facilitar la rehabilitación funcional.

- Vídeo: [Dr. Soroush Zaghi at ALSC - Breathe and Thrive 2022, in Las Vegas, NV](https://www.youtube.com/watch?v=3fq6w2buIy0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2022.

## zag-0513 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, en casos donde la lengua está atada casi por completo al proceso alveolar (Grado 4), se puede realizar una liberación inicial (fase 1) para permitir que la lengua tenga el mínimo de movilidad necesario para participar en la terapia y el proceso de expansión.

- Vídeo: [Dr. Soroush Zaghi at ALSC - Breathe and Thrive 2022, in Las Vegas, NV](https://www.youtube.com/watch?v=3fq6w2buIy0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2022.

## zag-0514 · Opinión · sin verificar (dicho en vídeo)

Según Zaghi, al liberar la lengua temprano, esta puede actuar como un "expansor natural" durante el crecimiento; se estima que una lengua funcional en el paladar expande el arco a un ritmo de 0.1 mm por mes.

- Vídeo: [Tongue-Tie, Sleep, Breathing, and Myofunctional Therapy: New Research Updates. Dr. Zaghi at ALSC '20](https://www.youtube.com/watch?v=G9GrUw7YJD0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2020.

## zag-0515 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, el ancho normal en niños se calcula como 24 + edad del niño. Por ejemplo, a los 6 años el IMW debería ser de 30 mm.

- Vídeo: [Dr. Soroush Zaghi at ALSC - Breathe and Thrive 2022, in Las Vegas, NV](https://www.youtube.com/watch?v=3fq6w2buIy0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2022.

## zag-0516 · Experiencia clínica · sin verificar (dicho en vídeo)

El momento favorito de Zaghi para realizar la frenuloplastia es a mitad de la fase de retención de la expansión ortodóntica (cuando ya se ha creado el diastema), porque el espacio ya existe y la lengua puede rehabilitarse para estabilizar el nuevo ancho del arco.

- Vídeo: [Updates from Dr. Soroush Zaghi - The Breathe Institute at ALSC Symposium 2024](https://www.youtube.com/watch?v=iGQlzOtT4C0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2024.

## zag-0517 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, en bocas estrechas con frenillos severos, se realiza una liberación "superficial" (mucosa y fascia superficial solamente), se expande el paladar, y meses después se realiza la liberación profunda de la fascia y el músculo si persiste la restricción.

- Vídeo: [Updates from Dr. Soroush Zaghi - The Breathe Institute at ALSC Symposium 2024](https://www.youtube.com/watch?v=iGQlzOtT4C0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2024.

## zag-0518 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, antes de decidir, se debe evaluar el ángulo NBC3. Si el paciente tiene un ángulo de 125° (postura de cabeza muy adelantada) y un IMW de 29 mm, la expansión es obligatoria antes que la cirugía de lengua para "neutralizar" la postura.

- Vídeo: [Updates from Dr. Soroush Zaghi - The Breathe Institute at ALSC Symposium 2024](https://www.youtube.com/watch?v=iGQlzOtT4C0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2024.
- Estudio: PMID [36841260](https://pubmed.ncbi.nlm.nih.gov/36841260/), ficha 2023-coppelson-postura-cbct.md.

## zag-0519 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, las amígdalas agudas se presentan con un color rojo intenso, lo que refleja una infección o inflamación activa en ese momento.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0520 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, presentan un color bronce, canela o "tan", lo cual es un indicador de inflamación recurrente crónica hasta el punto en que el tejido se ha cicatrizado y fibrosado.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0521 · Estudio citado · sin verificar (dicho en vídeo)

Zaghi menciona un artículo de investigación (referencia incompleta en el vídeo) que indica que las amígdalas que presentan una hipertrofia simple todavía conservan su capacidad de inmunidad innata.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0522 · Estudio citado · sin verificar (dicho en vídeo)

Según el mismo artículo citado por Zaghi, para cuando las amígdalas están crónicamente inflamadas y cicatrizadas, ya no proporcionan una función inmune adecuada.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0523 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, son aquellas que crecen hacia afuera, ocupando visiblemente el espacio de la vía aérea.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0524 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, parte del tejido se ve en la vía aérea, pero una gran porción está "enterrada" profundamente en el espacio de la garganta, lo que puede engañar en una inspección superficial.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0525 · Experiencia clínica · sin verificar (dicho en vídeo)

Zaghi aboga firmemente por la intervención quirúrgica (amigdalectomía).

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0526 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, representan una obstrucción física severa que impide la respiración nasal óptima y contribuye directamente a los trastornos respiratorios del sueño (SDB).

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0527 · Experiencia clínica · sin verificar (dicho en vídeo)

Zaghi recomienda un periodo de observación y manejo conservador antes de decidir la cirugía.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0528 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, evaluar si el tamaño se debe a alergias o infecciones recientes y probar primero terapia miofuncional (OMT) y asegurar que el paciente pueda respirar por la nariz.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0529 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, si la obstrucción no es total, restaurar la función nasal y lingual puede reducir la inflamación reactiva del tejido linfoide.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0530 · Experiencia clínica · sin verificar (dicho en vídeo)

Zaghi utiliza la técnica de "coblation" (radiofrecuencia) para la cirugía, ya que el calor abla el tejido sellando vasos sanguíneos y resulta en una recuperación mucho menos dolorosa para el niño.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0531 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, durante la cirugía, deja una pequeña cantidad de tejido amigdalino (especialmente tejido linfoide lingual en los laterales) para preservar cierta función inmune residual.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0532 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, los niños no "superan" o "dejan atrás" las amígdalas grandes espontáneamente (growing out of them); lo que ocurre es que la cara "crece alrededor" de ellas, lo que deforma el paladar (haciéndolo alto y estrecho) y la estructura facial para poder respirar.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0533 · Opinión · sin verificar (dicho en vídeo)

Zaghi sugiere que si existe exposición a moho tóxico ambiental y no se trata, las amígdalas y adenoides pueden volver a crecer incluso después de haber sido operadas.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0534 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, antes de cualquier cirugía de amígdalas, el primer paso obligatorio es establecer la higiene nasal (lavados con xilitol, manejo de alergias) para descartar que la hipertrofia sea meramente reactiva a la respiración bucal.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0535 · Estudio citado · sin verificar (dicho en vídeo)

Zaghi cita un estudio de Yoon, Liu, Zaghi et al. que demuestra que la expansión palatina rápida puede reducir significativamente el volumen de las amígdalas y adenoides al facilitar el cambio de respiración bucal a nasal.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0536 · Experiencia clínica · sin verificar (dicho en vídeo)

Zaghi advierte que un paciente con amígdalas Grado 3 o 4 no puede realizar con éxito la terapia miofuncional porque la obstrucción física le impide mantener el sello labial y la postura lingual correcta.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0537 · Estudio citado · sin verificar (dicho en vídeo)

Zaghi cita un artículo de investigación que demuestra que las amígdalas con hipertrofia simple (agudas/rojas) todavía poseen una inmunidad innata activa; sin embargo, las amígdalas crónicamente inflamadas y cicatrizadas (bronce) ya no proporcionan una función inmunológica eficaz al organismo.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0538 · Estudio citado · sin verificar (dicho en vídeo)

Zaghi cita que la expansión palatina rápida en niños puede reducir físicamente el volumen de las amígdalas y adenoides al facilitar la transición de respiración bucal a nasal, permitiendo en algunos casos evitar la cirugía.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

---

<!-- archivo: expertos/soroush-zaghi/respuestas-a-criticas.md -->
# Zaghi ante las críticas habituales

Para cada crítica frecuente sobre el frenillo lingual: qué dice Zaghi en sus vídeos y qué dice la evidencia de esta biblioteca, a favor y en contra. Lo de Zaghi es **opinión de experto**, no un estudio. Los números `zag-0000` llevan a la entrada completa, con su vídeo y su estado de verificación. El objetivo no es ganar una discusión: es ver cada argumento con sus límites (ver AGENTS.md, regla 3).

## 1. «No hay forma fiable de diagnosticar la anquiloglosia»

**Zaghi.** Propone valorar cinco dimensiones y no solo el aspecto: longitud de lengua libre (Kotlow), movilidad de la punta (TRMR-TIP), succión palatina (TRMR-LPS), compensaciones y tensión al tacto (zag-0015, zag-0022 a zag-0028 en anquiloglosia.md). Critica mirar solo si la lengua sale y no si sube (zag-0043). Rechaza diagnosticar por foto o por correo sin exploración funcional (zag-0042, zag-0554). Y no libera si la movilidad es buena y no hay síntomas ni compensaciones (zag-0035).

**Lo que apoya.** El TRMR está publicado y se probó en 1.052 personas (Yoon 2017) y la medida con succión en 611 (Zaghi 2021). La prevalencia de anquiloglosia va del 2 % al 20 % según la herramienta que se use (Cruz 2022). Es decir: la crítica es cierta, pero vale para todos. Tampoco quien niega la anquiloglosia tiene un criterio validado.

**Lo que la limita.** Las escalas TRMR las validó el propio grupo de Zaghi, y los autores dicen que son poco fiables entre los 3 y los 11 años. Zaghi reconoce que el TRMR es difícil de hacer bien y que en su consulta usa sobre todo la maniobra de sujetar el suelo de la boca (zag-0569, zag-0623). Esa maniobra no está validada en un estudio comprobado: la cita «Moon 2022» (zag-0027) está `PENDIENTE DE VERIFICAR`. Ninguna escala tiene aún un patrón de referencia aceptado por todos.

## 2. «Las revisiones dicen que no hay evidencia»

**Zaghi.** Insiste en que la ausencia de evidencia no es evidencia de ausencia (zag-0292, zag-0293). Que un resultado no significativo solo dice que no se pudo demostrar la diferencia (zag-0292). Que los ensayos doble ciego son muy difíciles en cirugía (zag-0287) y que las series de casos son el primer paso hacia estudios mejores (zag-0288). Relaciona los niveles de evidencia con la carga de la prueba: para intervenciones de bajo riesgo pide «preponderancia de evidencia» (zag-0303, zag-0304). Todo en investigacion-etica.md.

**Lo que apoya.** Es un principio metodológico aceptado, y es la regla 4 de esta biblioteca. Las revisiones de anquiloglosia mezclan estudios que diagnostican por longitud con estudios que miden función. Por ejemplo, la revisión de JADA de 2024 sobre maloclusión aceptó cualquier herramienta, dio certeza baja o muy baja, y aun así encontró más reducción de la apertura bucal en la clase III (Póvoa-Santos 2024).

**Lo que la limita.** La regla funciona en los dos sentidos: que no se haya demostrado que no sirve tampoco demuestra que sirva. Algunas frases de Zaghi van más allá de lo defendible, como que decir «no hay evidencia» equivale a decir «no entiendo» (zag-0291). Esa es una opinión polémica, no un argumento. Y él mismo exageró un estudio del que es coautor: dijo que el ensayo de Lichnowska mostraba efecto en el sueño y en la retención ortodóncica, y el artículo no mide eso (zag-0007, discrepancias.md).

## 3. «El consenso de los otorrinos de 2020 no apoya tratar»

**Zaghi.** Lo critica como una encuesta de opiniones de un panel de una sola especialidad, sin experiencia en frenuloplastia funcional, que deja fuera a clínicos considerados «controvertidos», y con un sesgo de medición porque se fija en sacar la lengua y no en elevarla (zag-0299, zag-0539, zag-0540). Firmó una carta de respuesta (Ghaheri 2020).

**Lo que apoya.** El propio consenso (Messner 2020) no llegó a acuerdo en 28 de sus 89 afirmaciones (y en 17 solo hubo acuerdo parcial). Sus autores atribuyen esa falta de acuerdo a «lagunas de conocimiento» y a falta de evidencia sobre el diagnóstico y el tratamiento (resumen de PubMed).

**Lo que la limita.** Un consenso Delphi es, por diseño, opinión de expertos. Lo mismo vale para la opinión de Zaghi: ninguna de las dos es un estudio. Cuántos panelistas había y por qué se eligieron: `PENDIENTE DE VERIFICAR` en el texto completo.

## 4. «El frenillo no afecta al habla»

**Zaghi.** Describe dificultades con la R (sobre todo la vibrante), S, T, L y D (zag-0030). Critica que un estudio sobre habla (Salt et al.) concluya «sin diferencia» cuando, según él, los tratados puntuaban más alto (zag-0300, zag-0541).

**Lo que apoya y lo que no.** La evidencia está enfrentada y es de baja calidad en los dos sentidos: ver la objeción O-004. El estudio que critica es Salt H, Claessen M, Johnston T, Smart S. *Speech production in young children with tongue-tie*. Int J Pediatr Otorhinolaryngol 2020. PMID [32298924](https://pubmed.ncbi.nlm.nih.gov/32298924/). Son 59 niños de 2 a 4 años en tres grupos, sin diferencias significativas en movilidad, habla ni inteligibilidad. Los autores lo presentan como evidencia «preliminar». Que los tratados puntuaran más alto no se puede comprobar en el resumen: `PENDIENTE DE VERIFICAR` en el texto completo. Ficha pendiente.

## 5. «La frenotomía no sirve»

**Zaghi.** Distingue entre un corte simple (frenotomía) y una frenuloplastia funcional con terapia miofuncional antes y después. Sostiene que comparar sus resultados es un sesgo de rendimiento (zag-0298, zag-0542) y que cortar sin terapia puede dejar una cicatriz que empeora la movilidad (zag-0546).

**Lo que apoya.** Un ensayo aleatorizado de 155 personas encontró que añadir frenuloplastia a la terapia miofuncional mejoraba más la movilidad y las funciones orales que la terapia sola (Lichnowska 2024).

**Lo que la limita.** En ese ensayo la asignación fue por orden de llegada, la evaluación fue visual y Zaghi es coautor. Solo incluyó pacientes con deformidad maxilofacial. En adultos con apnea, un ensayo pequeño no mejoró el índice de apnea (Preedeewong 2024). En lactancia hay ensayos negativos (Dinh 2025). La afirmación L-013 de la matriz sigue como INTERPRETACION.

## 6. «Todo es el frenillo»: el riesgo de culparlo de todo

**Zaghi.** Es el primero en decir que no. Que el frenillo explica solo una parte pequeña del paladar estrecho, en torno al 7,6 % de la varianza según cita de Yoon 2017 (zag-0005, minuto 21:47 de su charla de AAPMD 2019), y que influyen también la respiración oral, el tono y otros factores. Que no se diagnostica anquiloglosia por un paladar alto (zag-0034). Que no se libera si no hay sitio para la lengua (zag-0011). Que el pensamiento lineal «corto el frenillo y se cura la apnea» es un error (zag-0044).

**Lo que la limita.** La cifra del 7,6 % no aparece en el resumen del artículo de Yoon 2017: `PENDIENTE DE VERIFICAR` (discrepancias.md, punto 2).

## 7. «Las extracciones de premolares no cambian la vía aérea»

**Zaghi.** Los estudios que lo dicen no miden la postura de la cabeza y el cuello, que es como el cuerpo compensa (zag-0302).

**Evidencia a favor y en contra.** Ver la objeción O-003. Los metaanálisis no encuentran cambios de media. La postura de la cabeza cambia mucho la medida (Coppelson 2023, con Zaghi como coautor). Es una crítica metodológica razonable, no una prueba de daño.

## 8. Lo que Zaghi también dice y conviene no olvidar

- No se diagnostica por foto ni por correo (zag-0042).
- Con buena movilidad y sin síntomas, no se opera (zag-0035).
- Muchos bebés con inserciones bajas las remodelan solos entre los 3 y los 6 años (zag-0036).
- En personas con tejidos muy laxos el problema puede ser la falta de estabilidad, no la restricción. Estirar puede empeorarlas (zag-0033, hipermovilidad.md).
- Ha cambiado de opinión en técnica, instrumentos y terminología a lo largo de los años: contradicciones.md.

---

<!-- archivo: expertos/soroush-zaghi/sueno-apnea.md -->
# Sueño y apnea

Ideas públicas de Soroush Zaghi sobre este tema, reconstruidas a partir de sus vídeos. **No es Zaghi hablando ni una guía clínica.** Cómo leer cada entrada: README. Entradas: 48.

## zag-0008 · Estudio citado · verificado en PubMed

El FAirEST-6 (Oh, Zaghi, Peterson y colaboradores, Pediatr Dent 2021, 96 niños de dentición mixta) es una herramienta de cribado de trastornos respiratorios del sueño pediátricos con seis factores: respiración bucal, tensión del mentalis, amígdalas grandes, anquiloglosia, desgaste dental y paladar estrecho.

- Vídeo: [Dr. Soroush Zaghi at Tongue Time 2026 in Zurich, Switzerland  (Full Lecture)](https://www.youtube.com/watch?v=y6VkQnMBBvc), minuto 55:53 (localizado en los subtítulos automáticos).
- Vídeo: [Dr. Zaghi on Research Principles (From TBI's Outlook at AAPMD Collaboration Cures Conference, 2021)](https://www.youtube.com/watch?v=vYQ1mv8Gdf0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2021.
- Estudio: PMID [34467840](https://pubmed.ncbi.nlm.nih.gov/34467840/), ficha 2021-oh-fairest6.md.
- Cita corta (transcripción automática, puede tener errores): «The fairest six was inspired by Dr Christian Yimino and is now published in the journal of pediatric dentistry»

## zag-0047 · Estudio citado · sin verificar (dicho en vídeo)

Yoon, Zaghi et al. (2017). Correlación directa entre movilidad lingual restringida (Grados 3 y 4) y la presencia de un paladar estrecho y un paladar blando elongado (factor de riesgo para apnea).

- Vídeo: [Myofunctional Therapy and Frenuloplasty Can Be Appropriate Treatments for Obstructive Sleep Apnea](https://www.youtube.com/watch?v=dlU8wxa8474), minuto `PENDIENTE DE VERIFICAR`.
- Vídeo: [Full Lecture: Evaluation, Diagnosis, and Treatment of Tongue, Lip, & Buccal Ties, Dr. Soroush Zaghi](https://www.youtube.com/watch?v=iP3c-C9L9b0), minuto `PENDIENTE DE VERIFICAR`.
- Vídeo: ["Do I Have A Tongue-Tie?" - 5 dimensions of tongue-tie assessment, Dr. Zaghi - The Breathe Course](https://www.youtube.com/watch?v=8dOq11N-qK8), minuto `PENDIENTE DE VERIFICAR`.
- Estudio: PMID [28994495](https://pubmed.ncbi.nlm.nih.gov/28994495/), ficha 2017-yoon-maxilar.md.

## zag-0130 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, el trastorno respiratorio del sueño (SDB) es un continuo o "efecto dominó" que evoluciona así: Respiración bucal → Respiración ruidosa → Ronquido → UARS → Apnea obstructiva del sueño (OSA).

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0131 · Estudio citado · sin verificar (dicho en vídeo)

Christian Guilleminault (1976). Fue el primero en reportar la apnea pediátrica y establecer que es similar pero no igual a la de los adultos.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0132 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, la respiración bucal se considera patológica si ocurre más del 10% del tiempo de sueño. Se clasifica en leve (5-15%), moderada (>15%) y severa (>35%).

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0133 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, la apnea del sueño en niños se define por episodios de obstrucción parcial o completa de la vía aérea que duran al menos 10 segundos o 2 respiraciones.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0134 · Estudio citado · sin verificar (dicho en vídeo)

Un artículo reciente en una revista de la que Zaghi es editor indica que roncar durante el 5% del tiempo de sueño es un factor diagnóstico suficiente para la resistencia de las vías aéreas superiores (UARS).

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0135 · Opinión · sin verificar (dicho en vídeo)

Según Zaghi, hipótesis Musculoesquelética de Guilleminault: Existe un ciclo donde la inflamación sistémica, la dieta o la postura inician la respiración bucal, la cual genera inflamación local, agrandamiento de amígdalas y crecimiento facial vertical, empeorando el SDB.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0136 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, el IAH (Índice de Apnea-Hipopnea) es insuficiente porque solo mide pausas de aire y pérdida de oxígeno, pero ignora los micro-despertares y el esfuerzo respiratorio.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0137 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, los estudios de sueño (polisomnografía y WatchPAT) presentan una alta tasa de falsos negativos.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0139 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, los estudios en laboratorios de sueño son poco fiables para niños debido a que el entorno extraño y los cables distorsionan su patrón real de sueño.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0140 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, los resultados de un estudio de sueño pueden variar un 15-20% de una noche a otra en el mismo paciente.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0141 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, la oximetría sola es una herramienta pobre porque solo captura los casos más extremos y omite a los pacientes en el espectro del UARS o apnea leve.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0142 · Estudio citado · sin verificar (dicho en vídeo)

Christian Guilleminault (2001). Describió el UARS como una condición donde existe limitación de flujo de aire y micro-despertares frecuentes, siendo más común en niños que la propia apnea.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0143 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, criterios para UARS: IAH menor a 5, niveles de oxígeno superiores al 92% durante toda la noche, pero un índice de arousals (despertares por esfuerzo) superior a 10.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0144 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, en el UARS, el paciente se despierta en el momento en que la garganta empieza a cerrarse (arousal), entrando en un estado de "lucha o huida" constante. Cita un caso con 29 despertares por hora (uno cada 2 minutos).

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0145 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, la DISE permite ver en tiempo real, bajo sedación en quirófano, cómo se colapsa la vía aérea cuando los músculos están totalmente relajados.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0146 · Experiencia clínica · sin verificar (dicho en vídeo)

Durante la DISE, Zaghi busca diferenciar si el colapso es por la lengua, el paladar blando o las paredes laterales (colapso concéntrico).

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0147 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, la DISE demuestra que muchos pacientes con IAH bajo realmente están "asfixiándose" en sus propias estructuras anatómicas cuando logran alcanzar el sueño profundo.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0148 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, TDAH y problemas de conducta (agresión, bullying) son a menudo síntomas de privación de sueño por SDB.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0149 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, enuresis nocturna (mojar la cama) es un síntoma de SDB debido al estrés del sistema simpático durante la noche.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0150 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, sudoración nocturna, pesadillas, inquietud extrema (dar vueltas en la cama) y fatiga matutina.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0151 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, insomnio crónico: Menciona un paciente boxeador que tomó Ambien por 10 años cuando su problema real era un tabique desviado y válvula nasal colapsada.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0152 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, nicturia: Despertar varias veces (4-7 veces) para ir al baño puede ser un signo de micro-despertares por SDB.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0153 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, dolores de cabeza crónicos, migrañas matutinas y bruxismo (el cual es una compensación para adelantar la mandíbula y abrir la vía aérea).

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0154 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, el Ferris 6 + 4 para adultos añade: Scalloping lingual (marcas de dientes), overflow (la lengua desborda los dientes), posición de lengua de Freedman grado 4 y el Palatal Flutter Sign.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.
- Estudio: PMID [34467840](https://pubmed.ncbi.nlm.nih.gov/34467840/), ficha 2021-oh-fairest6.md.

## zag-0155 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, palatal Flutter Sign: Si el paciente ronca con la lengua abajo pero el ronquido desaparece al succionar la lengua al paladar, es un candidato positivo para cirugía de frenillo y terapia miofuncional.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0156 · Estudio citado · sin verificar (dicho en vídeo)

Villa et al. (2011/2014). Demuestra que la respiración nasal continua debe ser el objetivo final para evitar recaídas tras cirugías de amígdalas.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0157 · Estudio citado · sin verificar (dicho en vídeo)

Kim et al. (2011). Describe la condición de "boca semiabierta" (labios cerrados pero lengua abajo) como inestable y precursora de ronquido.

- Vídeo: `PENDIENTE DE VERIFICAR`. La extracción no guardó de qué vídeo sale. Para comprobarlo, buscar la idea en los vídeos de fuentes-videos.md.

## zag-0158 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, la meta definitiva de cualquier tratamiento es lograr una respiración nasal continua y silenciosa, con los labios sellados y la lengua succionada al paladar duro.

- Vídeo: [Pediatric Sleep Disordered Breathing and Maxillofacial Development with Soroush Zaghi](https://www.youtube.com/watch?v=eA1Yqbruw4g), minuto `PENDIENTE DE VERIFICAR`.
- Vídeo: [Myofunctional Therapy and Frenuloplasty Can Be Appropriate Treatments for Obstructive Sleep Apnea](https://www.youtube.com/watch?v=dlU8wxa8474), minuto `PENDIENTE DE VERIFICAR`.

## zag-0159 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, el primer paso absoluto es establecer la patencia nasal (higiene nasal, lavados salinos, manejo de alergias) antes de abordar la lengua.

- Vídeo: [Pediatric Sleep Disordered Breathing and Maxillofacial Development with Soroush Zaghi](https://www.youtube.com/watch?v=eA1Yqbruw4g), minuto `PENDIENTE DE VERIFICAR`.

## zag-0160 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, la terapia miofuncional (OMT) es la intervención de primera línea en su clínica para niños y adultos con problemas de sueño y respiración.

- Vídeo: [Frenums, Fascia and Physiology by Dr. Soroush Zaghi & Sanda Valcu-Pinkerton, COM - at AAPMD 2019](https://www.youtube.com/watch?v=BM3TmSXhUIw), minuto `PENDIENTE DE VERIFICAR`.
- Vídeo: [Myofunctional Therapy and Frenuloplasty Can Be Appropriate Treatments for Obstructive Sleep Apnea](https://www.youtube.com/watch?v=dlU8wxa8474), minuto `PENDIENTE DE VERIFICAR`.

## zag-0162 · Opinión · sin verificar (dicho en vídeo)

Según Zaghi, el tratamiento debe abordar la "causa raíz" (top-down whole body approach). Recomienda integrar el trabajo corporal (Bodywork/Osteopatía) para liberar la tensión de la fascia que rodea la lengua.

- Vídeo: [DR. SOROUSH ZAGHI ON PROTOCOLS DURING THE BREATHE WORKSHOP 2023](https://www.youtube.com/watch?v=rtbpgAER6GM), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2023.

## zag-0163 · Experiencia clínica · sin verificar (dicho en vídeo)

Zaghi reporta un 78% de mejora en la respiración nasal y un 73% de reducción en los ronquidos tras el protocolo combinado.

- Vídeo: [Tongue-Tie, Sleep, Breathing, and Myofunctional Therapy: New Research Updates. Dr. Zaghi at ALSC '20](https://www.youtube.com/watch?v=G9GrUw7YJD0), minuto `PENDIENTE DE VERIFICAR`.
- Vídeo: [Frenums, Fascia and Physiology by Dr. Soroush Zaghi & Sanda Valcu-Pinkerton, COM - at AAPMD 2019](https://www.youtube.com/watch?v=BM3TmSXhUIw), minuto `PENDIENTE DE VERIFICAR`.

## zag-0164 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, la expansión palatina en adultos (MARPE/MIND) puede lograr una reducción del 77% en el IAH.

- Vídeo: [Full Lecture: Evaluation, Diagnosis, and Treatment of Tongue, Lip, & Buccal Ties, Dr. Soroush Zaghi](https://www.youtube.com/watch?v=iP3c-C9L9b0), minuto `PENDIENTE DE VERIFICAR`.

## zag-0165 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, en pediatría, la expansión palatina puede reducir el IAH en un 70%.

- Vídeo: [Full Lecture: Evaluation, Diagnosis, and Treatment of Tongue, Lip, & Buccal Ties, Dr. Soroush Zaghi](https://www.youtube.com/watch?v=iP3c-C9L9b0), minuto `PENDIENTE DE VERIFICAR`.

## zag-0167 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, el CPAP es un "stent neumático" (no oxígeno) que mantiene la vía aérea abierta, pero en niños debe ser el último recurso porque la presión sobre el tercio medio facial puede restringir el crecimiento óseo.

- Vídeo: [Pediatric Sleep Disordered Breathing and Maxillofacial Development with Soroush Zaghi](https://www.youtube.com/watch?v=eA1Yqbruw4g), minuto `PENDIENTE DE VERIFICAR`.

## zag-0168 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, muchos pacientes no toleran el CPAP porque su lengua (por bajo tono o frenillo) cae hacia atrás y bloquea la presión de la máquina, causando aversión.

- Vídeo: [Pediatric and Adult Sleep Medicine - Key Takeaways with Dr. Soroush Zaghi](https://www.youtube.com/watch?v=J0jS05tFj1w), minuto `PENDIENTE DE VERIFICAR`.

## zag-0169 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, la OMT y la liberación del frenillo mejoran la adherencia al CPAP al permitir que la lengua se mantenga en el paladar, despejando la garganta.

- Vídeo: [Myofunctional Therapy and Frenuloplasty Can Be Appropriate Treatments for Obstructive Sleep Apnea](https://www.youtube.com/watch?v=dlU8wxa8474), minuto `PENDIENTE DE VERIFICAR`.
- Vídeo: [Frenums, Fascia and Physiology by Dr. Soroush Zaghi & Sanda Valcu-Pinkerton, COM - at AAPMD 2019](https://www.youtube.com/watch?v=BM3TmSXhUIw), minuto `PENDIENTE DE VERIFICAR`.

## zag-0172 · Opinión · sin verificar (dicho en vídeo)

Según Zaghi, hipótesis Musculoesquelética de Guilleminault: La respiración bucal (por hábito o frenillo) causa inflamación local que agranda las amígdalas y adenoides, lo que a su vez estrecha la vía aérea y altera el crecimiento facial, creando un círculo vicioso.

- Vídeo: [Pediatric Sleep Disordered Breathing and Maxillofacial Development with Soroush Zaghi](https://www.youtube.com/watch?v=eA1Yqbruw4g), minuto `PENDIENTE DE VERIFICAR`.
- Vídeo: [Frenums, Fascia and Physiology by Dr. Soroush Zaghi & Sanda Valcu-Pinkerton, COM - at AAPMD 2019](https://www.youtube.com/watch?v=BM3TmSXhUIw), minuto `PENDIENTE DE VERIFICAR`.

## zag-0173 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, la lengua actúa como un "expansor natural" del paladar; si está atada o baja, el paladar crece estrecho y alto (en forma de V), lo cual reduce el espacio del suelo de la nariz y desvía el tabique.

- Vídeo: [Full Lecture: Evaluation, Diagnosis, and Treatment of Tongue, Lip, & Buccal Ties, Dr. Soroush Zaghi](https://www.youtube.com/watch?v=iP3c-C9L9b0), minuto `PENDIENTE DE VERIFICAR`.
- Vídeo: [Updates from Dr. Soroush Zaghi - The Breathe Institute at ALSC Symposium 2024](https://www.youtube.com/watch?v=iGQlzOtT4C0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2024.

## zag-0174 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, la liberación del frenillo puede curar el bruxismo (en el 91% de los casos de su estudio), ya que el apretamiento dental es a menudo una compensación para adelantar la mandíbula y abrir la vía aérea colapsada.

- Vídeo: [Full Lecture: Evaluation, Diagnosis, and Treatment of Tongue, Lip, & Buccal Ties, Dr. Soroush Zaghi](https://www.youtube.com/watch?v=iP3c-C9L9b0), minuto `PENDIENTE DE VERIFICAR`.
- Vídeo: [Myofunctional Therapy and Frenuloplasty Can Be Appropriate Treatments for Obstructive Sleep Apnea](https://www.youtube.com/watch?v=dlU8wxa8474), minuto `PENDIENTE DE VERIFICAR`.

## zag-0175 · Estudio citado · sin verificar (dicho en vídeo)

Guilleminault (2001). Definición del Síndrome de Resistencia de las Vías Aéreas Superiores (UARS).

- Vídeo: [Updates from Dr. Soroush Zaghi - The Breathe Institute at ALSC Symposium 2024](https://www.youtube.com/watch?v=iGQlzOtT4C0), minuto `PENDIENTE DE VERIFICAR`.
- Vídeo: [Pediatric Sleep Disordered Breathing and Maxillofacial Development with Soroush Zaghi](https://www.youtube.com/watch?v=eA1Yqbruw4g), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2024.

## zag-0176 · Estudio citado · sin verificar (dicho en vídeo)

Guilleminault (2011). Describe que la condición de labios cerrados pero lengua abajo es "semi-abierta" e inestable para el sueño.

- Vídeo: [Updates from Dr. Soroush Zaghi - The Breathe Institute at ALSC Symposium 2024](https://www.youtube.com/watch?v=iGQlzOtT4C0), minuto `PENDIENTE DE VERIFICAR`.
- Vídeo: [Dr. Soroush Zaghi at Tongue Time 2026 in Zurich, Switzerland  (Full Lecture)](https://www.youtube.com/watch?v=y6VkQnMBBvc), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2026.

## zag-0178 · Estudio citado · sin verificar (dicho en vídeo)

Zaghi establece que la respiración nasal continua debe ser el objetivo terapéutico final.

- Vídeo: [Dr. Soroush Zaghi at Tongue Time 2026 in Zurich, Switzerland  (Full Lecture)](https://www.youtube.com/watch?v=y6VkQnMBBvc), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2026.

## zag-0179 · Estudio citado · sin verificar (dicho en vídeo)

Según Zaghi, primer Ensayo Controlado Aleatorizado (RCT) que demuestra que la frenuloplastia con OMT es superior a la OMT sola en resultados de sueño y funciones orales.

- Vídeo: [Updates from Dr. Soroush Zaghi - The Breathe Institute at ALSC Symposium 2024](https://www.youtube.com/watch?v=iGQlzOtT4C0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2024.
- Estudio: PMID [39336841](https://pubmed.ncbi.nlm.nih.gov/39336841/), ficha 2024-lichnowska-ensayo-frenuloplastia.md.

## zag-0614 · Estudio citado · sin verificar (dicho en vídeo)

Según Zaghi, en niños, el desgaste dental se asocia con 19 veces más probabilidad de trastorno respiratorio del sueño (odds ratio 19, intervalo de confianza 95% entre 4.8 y 77).

- Vídeo: [Dr. Zaghi on Research Principles (From TBI's Outlook at AAPMD Collaboration Cures Conference, 2021)](https://www.youtube.com/watch?v=vYQ1mv8Gdf0), minuto 1:40:45 (localizado en los subtítulos automáticos).
- Año de la charla: 2021.
- Estudio: PMID [34467840](https://pubmed.ncbi.nlm.nih.gov/34467840/), ficha 2021-oh-fairest6.md.
- Cita corta (transcripción automática, puede tener errores): «You can see here that the odds ratios are perhaps the highest for which one dental wear right if your kids have dental wear 19 times odds of them having sleep disorder breathing.»

## zag-0615 · Estudio citado · sin verificar (dicho en vídeo)

Zaghi considera que roncar durante el 5% o más del tiempo de sueño es un factor diagnóstico suficiente de síndrome de resistencia de la vía aérea superior (UARS), según un artículo reciente que menciona sin dar autor ni año.

- Vídeo: [Dr. Soroush Zaghi at ALSC - Breathe and Thrive 2022, in Las Vegas, NV](https://www.youtube.com/watch?v=3fq6w2buIy0), minuto 2:47:56 (localizado en los subtítulos automáticos).
- Año de la charla: 2022.
- Cita corta (transcripción automática, puede tener errores): «I’m a reviewer an editor for multiple sleep journals and there’s this new article that just got published looking into a resistance and saying that five if you’re snoring for 5% of sleep time that is a diagnostic factor for […]»

---

<!-- archivo: expertos/soroush-zaghi/temas-poco-cubiertos.md -->
# Otros temas con poca cobertura

Ideas públicas de Soroush Zaghi sobre este tema, reconstruidas a partir de sus vídeos. **No es Zaghi hablando ni una guía clínica.** Cómo leer cada entrada: README. Entradas: 21.

## zag-0248 · Estudio citado · verificado en PubMed

Zaghi et al. (2019), Laryngoscope Investigative Otolaryngology. El 91% de los pacientes de la serie de 348 casos reportaron una reducción significativa en el apretamiento (clenching) o rechinamiento de dientes tras la frenuloplastia con terapia.

- Vídeo: [Long-term Implications of Untreated Tongue-Tie (Dr. Soroush Zaghi, The Breathe Institute)](https://www.youtube.com/watch?v=cuT6qrm5IT0), minuto `PENDIENTE DE VERIFICAR`.
- Vídeo: [Dr. Soroush Zaghi at ALSC - Breathe and Thrive 2022, in Las Vegas, NV](https://www.youtube.com/watch?v=3fq6w2buIy0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2022.
- Estudio: PMID [31637291](https://pubmed.ncbi.nlm.nih.gov/31637291/), ficha 2019-zaghi-frenuloplastia-348.md.

## zag-0378 · Opinión · sin verificar (dicho en vídeo)

Zaghi considera que el mejor momento para el cribado sistemático no es el nacimiento, sino antes de la escuela (3-5 años), porque la población neonatal es "políticamente sensible" y la investigación en bebés está muy bloqueada por los comités de ética (IRB).

- Vídeo: [Dr. Soroush Zaghi at Tongue Time 2026 in Zurich, Switzerland  (Full Lecture)](https://www.youtube.com/watch?v=y6VkQnMBBvc), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2026.

## zag-0379 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, la consultora de lactancia (invitada) menciona que en bebés con paladares muy altos, la liberación del frenillo sola no basta para lograr el sello; se requiere aumentar el tono y a veces trabajar con osteópatas para mover los huesos del paladar antes de los 3 meses.

- Vídeo: [Evolution Of Myofunctional Therapy, Lingual Frenuloplasty - Dr. Soroush Zaghi at ALSC 2026.](https://www.youtube.com/watch?v=nlFVT6PUaYc), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2026.

## zag-0380 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, el frenillo labial superior puede causar problemas para el cepillado, contribuir al diastema (espacio entre dientes), retrasar el crecimiento maxilar e interferir con el sello labial.

- Vídeo: [Evolution Of Myofunctional Therapy, Lingual Frenuloplasty - Dr. Soroush Zaghi at ALSC 2026.](https://www.youtube.com/watch?v=nlFVT6PUaYc), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2026.

## zag-0381 · Experiencia clínica · sin verificar (dicho en vídeo)

Zaghi utiliza la técnica "Vita Wide Lip Lengthening", que no corta tejido sino que lo reorganiza para alargar el labio y facilitar el sello labial en pacientes con incompetencia oral.

- Vídeo: [Evolution Of Myofunctional Therapy, Lingual Frenuloplasty - Dr. Soroush Zaghi at ALSC 2026.](https://www.youtube.com/watch?v=nlFVT6PUaYc), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2026.

## zag-0382 · Experiencia clínica · sin verificar (dicho en vídeo)

Zaghi observa que el 92% de los bebés tienen tensión en el labio superior; esta suele retroceder naturalmente entre los 3 y 6 años. Advierte no "asustar" a los padres con cirugías de labio tempranas, ya que el problema suele ser una mandíbula retraída y no el labio en sí.

- Vídeo: [Updates from Dr. Soroush Zaghi - The Breathe Institute at ALSC Symposium 2024](https://www.youtube.com/watch?v=iGQlzOtT4C0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2024.

## zag-0383 · Experiencia clínica · sin verificar (dicho en vídeo)

Los frenillos bucales (mejillas) pueden contribuir a la recesión gingival en premolares. Zaghi aplica un enfoque submucoso tunelizado en adultos para liberarlos sin cicatrices superficiales, logrando alivio en los músculos suboccipitales y mejor respiración nasal.

- Vídeo: [Evolution Of Myofunctional Therapy, Lingual Frenuloplasty - Dr. Soroush Zaghi at ALSC 2026.](https://www.youtube.com/watch?v=nlFVT6PUaYc), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2026.

## zag-0384 · Estudio citado · sin verificar (dicho en vídeo)

Zaghi cita el trabajo de Rockabado (referenciado por Valerie Sinkins) sobre el frenillo labial mandibular (inferior), indicando que su restricción puede frenar el desarrollo óseo de la mandíbula y dificultar el progreso de la ortodoncia.

- Vídeo: [Evolution Of Myofunctional Therapy, Lingual Frenuloplasty - Dr. Soroush Zaghi at ALSC 2026.](https://www.youtube.com/watch?v=nlFVT6PUaYc), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2026.

## zag-0385 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, la tensión en la ATM suele ser una compensación por la incapacidad de la lengua para elevarse; los músculos accesorios (maseteros) se sobrecargan para ayudar en la deglución.

- Vídeo: [Functional Approach to Frenuloplasty: How We Do It - Dr. Soroush Zaghi](https://www.youtube.com/watch?v=C0kel5PNc7c), minuto `PENDIENTE DE VERIFICAR`.

## zag-0387 · Opinión · sin verificar (dicho en vídeo)

Según Zaghi, el bruxismo es a menudo una respuesta de "supervivencia" del cuerpo para adelantar la mandíbula y abrir la vía aérea durante el sueño cuando la lengua está colapsada.

- Vídeo: [Pediatric Sleep Disordered Breathing and Maxillofacial Development with Soroush Zaghi](https://www.youtube.com/watch?v=eA1Yqbruw4g), minuto `PENDIENTE DE VERIFICAR`.

## zag-0389 · Experiencia clínica · sin verificar (dicho en vídeo)

En pacientes con hipermovilidad, la laxitud de la fascia reduce la presión sobre los vasos sanguíneos, lo que Zaghi asocia con la propensión a migrañas y mareos (disautonomía).

- Vídeo: [Updates from Dr. Soroush Zaghi - The Breathe Institute at ALSC Symposium 2024](https://www.youtube.com/watch?v=iGQlzOtT4C0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2024.

## zag-0390 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, la liberación de la "tercera capa" (fibras profundas) durante la cirugía produce a menudo una sensación instantánea de "ligereza" y desaparición de la presión en la base del cráneo.

- Vídeo: [Frenums, Fascia and Physiology by Dr. Soroush Zaghi & Sanda Valcu-Pinkerton, COM - at AAPMD 2019](https://www.youtube.com/watch?v=BM3TmSXhUIw), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2019.

## zag-0392 · Estudio citado · sin verificar (dicho en vídeo)

Zaghi et al. realizaron un estudio con "usuarios profesionales de la voz" (ganadores del Grammy y cantantes de ópera) demostrando que la mayoría notó una mayor claridad vocal tras la frenuloplastia.

- Vídeo: [Dr. Soroush Zaghi at Tongue Time 2026 in Zurich, Switzerland  (Full Lecture)](https://www.youtube.com/watch?v=y6VkQnMBBvc), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2026.

## zag-0394 · Estudio citado · sin verificar (dicho en vídeo)

Zaghi critica el estudio de Salt et al. (2021) sobre habla, señalando que los autores interpretaron como "sin diferencia" datos donde los niños tratados tenían puntuaciones más altas, debido a la falta de potencia estadística (sesgo de confirmación).

- Vídeo: [Updates from Dr. Soroush Zaghi - The Breathe Institute at ALSC Symposium 2024](https://www.youtube.com/watch?v=iGQlzOtT4C0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2024.

## zag-0395 · Experiencia clínica · sin verificar (dicho en vídeo)

Zaghi relata su propio fracaso ortodóntico: tras años de Invisalig y crozats, sus dientes se movían en cuanto dejaba de usar retenedores una noche. La causa era una deficiencia ósea maxilar que solo se resolvió con expansión esquelética (MARPE).

- Vídeo: [Updates from Dr. Soroush Zaghi - The Breathe Institute at ALSC Symposium 2024](https://www.youtube.com/watch?v=iGQlzOtT4C0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2024.

## zag-0396 · Experiencia clínica · sin verificar (dicho en vídeo)

Sandraluz Gonzalez afirma que la terapia miofuncional es la clave para la estabilidad ortodóntica a largo plazo; sin la lengua en el paladar (el "retenedor natural"), los dientes volverán a apiñarse.

- Vídeo: [Breathe Myo Explained: Tongue Tie, Airway Health, Facial Development with Sandraluz Gonzalez](https://www.youtube.com/watch?v=ni2dO45jdbo), minuto `PENDIENTE DE VERIFICAR`.

## zag-0397 · Opinión · sin verificar (dicho en vídeo)

Según Zaghi, las extracciones de premolares son el "villano" de la historia (filosofía de Tweed), ya que encogen la "jaula" de la lengua y predisponen a la apnea al forzar la lengua hacia la vía aérea.

- Vídeo: [Evolution Of Myofunctional Therapy, Lingual Frenuloplasty - Dr. Soroush Zaghi at ALSC 2026.](https://www.youtube.com/watch?v=nlFVT6PUaYc), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2026.

## zag-0398 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, el momento ideal para la frenuloplastia funcional es a la mitad de la fase de retención de la expansión, cuando el espacio ya se ha creado y la lengua puede reeducarse para mantener ese ancho.

- Vídeo: [Updates from Dr. Soroush Zaghi - The Breathe Institute at ALSC Symposium 2024](https://www.youtube.com/watch?v=iGQlzOtT4C0), minuto `PENDIENTE DE VERIFICAR`.
- Año de la charla: 2024.

## zag-0399 · Experiencia clínica · sin verificar (dicho en vídeo)

Según Zaghi, el programa de hábitos de TBI (con Carla Lejarraga) enfatiza que no basta con castigar o poner esmaltes amargos; hay que entender por qué empezó el hábito (a menudo por baja estimulación sensorial o búsqueda de estabilidad).

- Vídeo: [Introducing the Breathe Oral Habits Program - with Carla Lejarraga and Anna Gross](https://www.youtube.com/watch?v=kPzCm3RgVVc), minuto `PENDIENTE DE VERIFICAR`.

## zag-0400 · Experiencia clínica · sin verificar (dicho en vídeo)

Sandraluz Gonzalez señala que el uso prolongado de biberones o chupetes después de los 12 meses interfiere con la transición del "trago infantil" al "trago maduro" y deforma el crecimiento óseo.

- Vídeo: [Breathe Myo Explained: Tongue Tie, Airway Health, Facial Development with Sandraluz Gonzalez](https://www.youtube.com/watch?v=ni2dO45jdbo), minuto `PENDIENTE DE VERIFICAR`.

## zag-0401 · Experiencia clínica · sin verificar (dicho en vídeo)

En adultos, Zaghi enseña una técnica de deglución que no usa el "spot" (papila incisiva) si el paciente tiene una cara muy larga, sino que se enfoca en empujar el cuerpo de la lengua hacia arriba para evitar el empuje lingual (tongue thrust).

- Vídeo: [Perfect Your Swallow Technique with Dr. Soroush Zaghi at The Breathe Institute](https://www.youtube.com/watch?v=GJ4vm-4ZSyQ), minuto `PENDIENTE DE VERIFICAR`.

---

# Fichas de estudios

---

<!-- archivo: fuentes/articulos/1976-guilleminault-apnea-ninos.md -->
# Estudio: Sleep apnea in eight children

- **ID:** GUILLEMINAULT1976
- **Autores, año y revista:** Guilleminault C; Eldridge FL; Simmons FB; Dement WC. Pediatrics 1976;58(1):23-30.
- **DOI / PMID / URL:** PMID `934781`; sin DOI
- **Tipo de estudio:** Serie de casos.
- **Población y tamaño muestral:** 8 niños de 5 a 14 años.
- **Definición diagnóstica y técnicas:** Registro poligráfico nocturno.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA: el estudio no diagnostica anquiloglosia.
- **Variables de resultado:** Síntomas asociados al síndrome de apnea.
- **Resultados NUMÉRICOS verificados:** Síntomas descritos: somnolencia diurna, bajada del rendimiento escolar, conducta diurna anormal, enuresis reciente, cefalea matutina, peso anormal e hipertensión progresiva, junto a ronquido con pausas.
- **Límites metodológicos / confusores:** Ocho casos. Valor histórico.
- **Hallazgos contrarios o no significativos:** No aplica.
- **Conclusión que sí permite / que no permite:** Sí: Situar la primera descripción de apnea infantil con poligrafía y sus síntomas. No: Sacar cifras de prevalencia ni de tratamiento.
- **Licencia y derechos:** Derechos del editor. Aquí solo metadatos y resumen propio.
- **Estado de lectura:** Resumen PubMed revisado el 17/10/2026. Sin DOI en PubMed.

## Figuras

Figuras no revisadas: el texto completo no está en acceso abierto en PMC. [Ver el artículo](https://pubmed.ncbi.nlm.nih.gov/934781/).

---

<!-- archivo: fuentes/articulos/1978-proffit-equilibrio.md -->
# Proffit (1978) — Equilibrium theory revisited

- DOI: `10.1043/0003-3219(1978)048<0175:ETRFIP>2.0.CO;2`; PMID: `280125`.
- Diseño: revisión teórica sobre equilibrio dentario.
- Tesis: presiones de reposo de lengua y labios, fuerzas periodontales y necesidades respiratorias influyen en la posición de dientes y postura orofacial.
- Límite: no equiparar posición dentaria con crecimiento transversal de la base ósea maxilar.
- Criterio diagnóstico de anquiloglosia: NO APLICA: revisión teórica sobre equilibrio dentario.
- Estado: resumen primario revisado.

## Figuras

Figuras no revisadas: el texto completo no está en acceso abierto en PMC. [Ver el artículo](https://doi.org/10.1043/0003-3219(1978)048<0175:ETRFIP>2.0.CO;2).

---

<!-- archivo: fuentes/articulos/1981-harvold-primates-respiracion-oral.md -->
# Estudio: Primate experiments on oral respiration

- **ID:** HARVOLD1981
- **Autores, año y revista:** Harvold EP; Tomer BS; Vargervik K; Chierici G. Am J Orthod 1981;79(4):359-72.
- **DOI / PMID / URL:** DOI `10.1016/0002-9416(81)90379-1`; PMID `6939331`
- **Tipo de estudio:** Experimento en monos rhesus con tapones nasales de silicona frente a controles.
- **Población y tamaño muestral:** Monos rhesus. Número PENDIENTE DE VERIFICAR.
- **Definición diagnóstica y técnicas:** Obstrucción nasal experimental.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA: el estudio no diagnostica anquiloglosia.
- **Variables de resultado:** Postura oral, morfología facial y oclusión.
- **Resultados NUMÉRICOS verificados:** Sin cifras en el resumen. Los animales se adaptaron de formas distintas: boca abierta, mandíbula más baja, con o sin lengua adelantada. Todos acabaron con cara y oclusión distintas de los controles.
- **Límites metodológicos / confusores:** Modelo animal. Obstrucción total y forzada, distinta de la clínica humana.
- **Hallazgos contrarios o no significativos:** La adaptación fue variable entre animales.
- **Conclusión que sí permite / que no permite:** Sí: Decir que la respiración oral forzada cambia la forma de la cara en primates. No: Trasladar magnitudes a niños.
- **Licencia y derechos:** Derechos del editor. Aquí solo metadatos y resumen propio.
- **Estado de lectura:** Resumen PubMed revisado el 17/10/2026.

## Figuras

Figuras no revisadas: el texto completo no está en acceso abierto en PMC. [Ver el artículo](https://doi.org/10.1016/0002-9416(81)90379-1).

---

<!-- archivo: fuentes/articulos/1981-mcnamara-componentes-clase-ii.md -->
# Estudio: Components of class II malocclusion in children 8-10 years of age

- **ID:** MCNAMARA1981
- **Autores, año y revista:** McNamara JA Jr. Angle Orthod 1981;51(3):177-202.
- **DOI / PMID / URL:** DOI `10.1043/0003-3219(1981)051<0177:COCIMI>2.0.CO;2`; PMID `7023290`
- **Tipo de estudio:** Estudio cefalométrico transversal.
- **Población y tamaño muestral:** Niños de 8 a 10 años con clase II. Número PENDIENTE DE VERIFICAR.
- **Definición diagnóstica y técnicas:** Cefalometría; perpendicular a nasion.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA: el estudio no diagnostica anquiloglosia.
- **Variables de resultado:** Posición del maxilar y de la mandíbula, incisivos y dimensión vertical.
- **Resultados NUMÉRICOS verificados:** PubMed no tiene resumen. Según notas de trabajo previas (sin verificar en el original): maxilar adelantado en el 13 %, normal en el 47 % y retrasado en el 40 %; mandíbula retrasada en más del 60 %. PENDIENTE DE VERIFICAR en el original.
- **Límites metodológicos / confusores:** Muestra de una época y una población concretas.
- **Hallazgos contrarios o no significativos:** No aplica.
- **Conclusión que sí permite / que no permite:** Sí: Citar el estudio clásico sobre qué compone la clase II. No: Usar las cifras antes de comprobarlas en el original.
- **Licencia y derechos:** Derechos del editor. Aquí solo metadatos y resumen propio.
- **Estado de lectura:** Solo metadatos PubMed (17/10/2026).

## Figuras

Figuras no revisadas: el texto completo no está en acceso abierto en PMC. [Ver el artículo](https://doi.org/10.1043/0003-3219(1981)051<0177:COCIMI>2.0.CO;2).

---

<!-- archivo: fuentes/articulos/1981-sullivan-cpap.md -->
# Estudio: Reversal of obstructive sleep apnoea by continuous positive airway pressure applied through the nares

- **ID:** SULLIVAN1981
- **Autores, año y revista:** Sullivan CE; Issa FG; Berthon-Jones M; Eves L. Lancet 1981;1(8225):862-5.
- **DOI / PMID / URL:** DOI `10.1016/s0140-6736(81)92140-1`; PMID `6112294`
- **Tipo de estudio:** Serie de casos.
- **Población y tamaño muestral:** 5 pacientes con apnea grave.
- **Definición diagnóstica y técnicas:** CPAP con mascarilla nasal.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA: el estudio no diagnostica anquiloglosia.
- **Variables de resultado:** Oclusión de la vía aérea durante el sueño.
- **Resultados NUMÉRICOS verificados:** Presiones de 4,5 a 10 cm H2O evitaron la oclusión en los 5 pacientes durante toda la noche.
- **Límites metodológicos / confusores:** Cinco casos. Valor histórico.
- **Hallazgos contrarios o no significativos:** No aplica.
- **Conclusión que sí permite / que no permite:** Sí: Situar el origen de la CPAP nasal. No: Sacar conclusiones sobre niños o crecimiento facial.
- **Licencia y derechos:** Derechos del editor. Aquí solo metadatos y resumen propio.
- **Estado de lectura:** Resumen PubMed revisado el 17/10/2026.

## Figuras

Figuras no revisadas: el texto completo no está en acceso abierto en PMC. [Ver el artículo](https://doi.org/10.1016/s0140-6736(81)92140-1).

---

<!-- archivo: fuentes/articulos/1985-kier-smith-hidrostatos.md -->
# Kier & Smith (1985) — Tongues, tentacles and trunks

- DOI: `10.1111/j.1096-3642.1985.tb01178.x`
- Diseño: análisis biomecánico teórico/general.
- Hallazgo: el volumen del hidrostato muscular se mantiene aproximadamente constante mientras la estructura se deforma mediante contracciones coordinadas.
- Sirve para: caracterizar propiedades físicas generales de la lengua.
- No sirve para: afirmar que un paladar estrecho nunca limita movimientos ni que el frenillo explica todos los casos de lengua baja.
- Criterio diagnóstico de anquiloglosia: NO APLICA: estudio anatómico o biomecánico, no diagnostica anquiloglosia.
- Estado: metadatos y resumen primario revisados; fichar texto completo si procede.

## Figuras

Figuras no revisadas: el texto completo no está en acceso abierto en PMC. [Ver el artículo](https://doi.org/10.1111/j.1096-3642.1985.tb01178.x).

---

<!-- archivo: fuentes/articulos/1995-marcus-cpap-ninos.md -->
# Estudio: Use of nasal continuous positive airway pressure as treatment of childhood obstructive sleep apnea

- **ID:** MARCUS1995
- **Autores, año y revista:** Marcus CL; Ward SL; Mallory GB et al.. J Pediatr 1995.
- **DOI / PMID / URL:** DOI `10.1016/s0022-3476(95)70262-8`; PMID `7608817`
- **Tipo de estudio:** Retrospectivo con cuestionario a nueve centros.
- **Población y tamaño muestral:** 94 niños y adolescentes.
- **Definición diagnóstica y técnicas:** CPAP nasal.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA: el estudio no diagnostica anquiloglosia.
- **Variables de resultado:** Eficacia, presión, complicaciones.
- **Resultados NUMÉRICOS verificados:** Eficaz en 81 (86 %); presión mediana 8 cm H2O; complicaciones menores.
- **Límites metodológicos / confusores:** Retrospectivo.
- **Hallazgos contrarios o no significativos:** El resumen no evalúa el efecto sobre el crecimiento facial.
- **Conclusión que sí permite / que no permite:** Sí: Citar el estudio pionero de CPAP en niños. No: Usarlo sobre crecimiento facial, que no estudia.
- **Licencia y derechos:** Derechos del editor. Aquí solo metadatos y resumen propio.
- **Estado de lectura:** Resumen PubMed revisado el 17/10/2026.

## Figuras

Figuras no revisadas: el texto completo no está en acceso abierto en PMC. [Ver el artículo](https://doi.org/10.1016/s0022-3476(95)70262-8).

---

<!-- archivo: fuentes/articulos/1999-kotlow-clasificacion.md -->
# Estudio: Ankyloglossia (tongue-tie): a diagnostic and treatment quandary

- **ID:** KOTLOW1999
- **Autores, año y revista:** Kotlow LA. Quintessence Int 1999;30(4):259-62.
- **DOI / PMID / URL:** PMID `10635253`; sin DOI
- **Tipo de estudio:** Artículo de propuesta clínica.
- **Población y tamaño muestral:** No aplica.
- **Definición diagnóstica y técnicas:** Medida de la lengua libre.
- **Criterio diagnóstico de anquiloglosia:** LONGITUD/ASPECTO. Mide la «lengua libre», de la inserción del frenillo a la punta. Según Guilleminault 2016 (texto completo), Kotlow considera normal >16 mm. El umbral no aparece en el resumen de Kotlow.
- **Variables de resultado:** No aplica.
- **Resultados NUMÉRICOS verificados:** Sin cifras en el resumen.
- **Límites metodológicos / confusores:** Propuesta de autor, sin validación en el resumen. Yoon 2017 encontró que la lengua libre mide algo distinto del TRMR.
- **Hallazgos contrarios o no significativos:** Ver YOON2017SB.
- **Conclusión que sí permite / que no permite:** Sí: Citar el origen de la clasificación por longitud más usada. No: Usar la longitud como medida de función.
- **Licencia y derechos:** Derechos del editor. Aquí solo metadatos y resumen propio.
- **Estado de lectura:** Resumen PubMed revisado el 17/10/2026. Sin DOI.

## Figuras

Figuras no revisadas: el texto completo no está en acceso abierto en PMC. [Ver el artículo](https://pubmed.ncbi.nlm.nih.gov/10635253/).

---

<!-- archivo: fuentes/articulos/2000-messner-prevalencia-lactancia.md -->
# Estudio: Ankyloglossia: incidence and associated feeding difficulties

- **ID:** MESSNER2000
- **Autores, año y revista:** Messner AH; Lalakea ML; Aby J; Macmahon J; Bair E. *Archives of Otolaryngology–Head & Neck Surgery* 2000;126(1):36–39.
- **DOI / PMID / URL:** DOI `10.1001/archotol.126.1.36`; PMID `10628708`; [resumen PubMed](https://pubmed.ncbi.nlm.nih.gov/10628708/); [editor](https://doi.org/10.1001/archotol.126.1.36).
- **Tipo de estudio:** Cribado prospectivo de recién nacidos con seguimiento comparativo de lactancia durante seis meses; subgrupo con controles emparejados.
- **Población y tamaño muestral:** 1.041 recién nacidos cribados en un hospital; 50 clasificados con anquiloglosia. Para el seguimiento de madres con intención de amamantar: **36 casos y 36 controles**.
- **Definición diagnóstica y técnicas:** Examen de frenillo en nursery y entrevistas telefónicas maternas mensuales. El resumen no describe cómo se midió la función; revisiones metodológicas posteriores describen como criterio original un **frenillo anormalmente corto**, pendiente de cotejar directamente en métodos completos.
- **Criterio diagnóstico de anquiloglosia:** LONGITUD/ASPECTO según revisión metodológica secundaria; el protocolo de exploración original queda `PENDIENTE DE VERIFICAR` a texto completo.
- **Variables de resultado:** Frecuencia de anquiloglosia identificada, dificultades de lactancia y mantenimiento de lactancia.
- **Resultados NUMÉRICOS verificados:** 50/1.041 (**4,8 %**) fueron clasificados como anquiloglosia; relación varones:mujeres 2,6:1. Las dificultades de lactancia se notificaron en **9/36 (25 %) casos frente a 1/36 (3 %) controles** (p<0,01). La lactancia durante al menos dos meses se mantuvo en **30/36 (83 %) frente a 33/36 (92 %)** (p=0,29, sin diferencia significativa).
- **Aportación del estudio:** Señal de asociación entre el hallazgo neonatal de frenillo corto y dificultades de lactancia en una muestra cribada, junto a un resultado no concluyente sobre mantener lactancia dos meses.
- **Límites metodológicos / confusores (solo los relevantes):** Criterio clínico anatómico, subgrupo de seguimiento pequeño y resultados maternos; no clasifica niños por TRMR ni evalúa cirugía.
- **Licencia y derechos:** Derechos editoriales; ficha propia, sin PDF ni imágenes.
- **Estado de lectura:** **Resumen PubMed y metadatos editoriales verificados el 04/11/2026**. Métodos originales completos no inspeccionados; el criterio diagnóstico se tomó de [revisión metodológica secundaria](https://pmc.ncbi.nlm.nih.gov/articles/PMC1949218/).
## Figuras

No examinadas. [Estudio original](https://doi.org/10.1001/archotol.126.1.36).

---

<!-- archivo: fuentes/articulos/2001-guilleminault-uars-ninos.md -->
# Estudio: Upper airway resistance syndrome in children: a clinical review

- **ID:** GUILLEMINAULT2001
- **Autores, año y revista:** Guilleminault C; Khramtsov A. Semin Pediatr Neurol 2001;8(4):207-15.
- **DOI / PMID / URL:** DOI `10.1053/spen.2001.29045`; PMID `11768783`
- **Tipo de estudio:** Revisión clínica narrativa.
- **Población y tamaño muestral:** No aplica.
- **Definición diagnóstica y técnicas:** No aplica.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA: el estudio no diagnostica anquiloglosia.
- **Variables de resultado:** No aplica.
- **Resultados NUMÉRICOS verificados:** Sin cifras en el resumen. Afirma que el síndrome de resistencia de vía aérea superior (UARS) es más frecuente en niños que la apnea, que puede requerir presión esofágica para confirmarse y que a menudo hay una anomalía craneofacial leve.
- **Límites metodológicos / confusores:** Revisión de autor, no sistemática.
- **Hallazgos contrarios o no significativos:** No aplica.
- **Conclusión que sí permite / que no permite:** Sí: Definir el UARS y recomendar valorar maxilares en niños con trastorno respiratorio del sueño. No: Usarla como prueba de frecuencias.
- **Licencia y derechos:** Derechos del editor. Aquí solo metadatos y resumen propio.
- **Estado de lectura:** Resumen PubMed revisado el 17/10/2026.

## Figuras

Figuras no revisadas: el texto completo no está en acceso abierto en PMC. [Ver el artículo](https://doi.org/10.1053/spen.2001.29045).

---

<!-- archivo: fuentes/articulos/2002-messner-frenuloplastia-habla.md -->
# Estudio: The effect of ankyloglossia on speech in children

- **ID:** MESSNER2002
- **Autores, año y revista:** Messner AH; Lalakea ML. *Otolaryngology–Head and Neck Surgery* 2002;127(6):539–545.
- **DOI / PMID / URL:** DOI `10.1067/mhn.2002.129731`; PMID `12501105`; [abstract PubMed](https://pubmed.ncbi.nlm.nih.gov/12501105/); [original](https://doi.org/10.1067/mhn.2002.129731).
- **Tipo de estudio:** Estudio prospectivo de niños intervenidos con evaluación antes/después, **sin grupo control**.
- **Población y tamaño muestral:** **30 niños**, entre 1 y 12 años, sometidos a frenuloplastia. En **21** hubo evaluación del habla preoperatoria; **15** tuvieron evaluación posterior del habla descrita en el resumen.
- **Definición diagnóstica y técnicas:** Diagnóstico de anquiloglosia previo a cirugía, evaluación de movilidad lingual, exploración logopédica y cuestionarios parentales. La escala diagnóstica exacta y los planos de liberación están `PENDIENTES DE VERIFICAR` a texto completo.
- **Criterio diagnóstico de anquiloglosia:** PENDIENTE DE VERIFICAR: el resumen no especifica la herramienta de clasificación preoperatoria; sí cuantifica movilidad.
- **Variables de resultado:** Protrusión y elevación de lengua, articulación evaluada clínicamente y inteligibilidad estimada por padres.
- **Resultados NUMÉRICOS verificados:** Protrusión media **14,2 → 25,8 mm** y elevación **5,2 → 22 mm** tras frenuloplastia (ambos p<0,01). Entre 15 niños reevaluados, **9** mejoraron articulación, **4** presentaban habla normal previamente y **2** seguían con alteración. Inteligibilidad parental en escala 1–5: **3,4 → 4,2** (p<0,01).
- **Aportación del estudio:** Datos prospectivos de mejoría funcional y articulatoria observada después de frenuloplastia en niños seleccionados, con mediciones absolutas de movilidad y evaluación clínica del habla.
- **Límites metodológicos / confusores (solo los relevantes):** Falta de comparador y seguimiento de habla disponible solo para parte de la muestra; distinguir cambio inmediato/postoperatorio de eficacia relativa a desarrollo o terapia del lenguaje.
- **Licencia y derechos:** Derechos editoriales; resumen propio sin reproducción de PDF.
- **Estado de lectura:** **Abstract del editor y PubMed verificados el 04/11/2026**; texto completo no revisado. La denominación y detalles técnicos de la frenuloplastia requieren lectura del original.
## Figuras

No examinadas. [Artículo original](https://doi.org/10.1067/mhn.2002.129731).

---

<!-- archivo: fuentes/articulos/2003-naimer-frenotomia-consulta.md -->
# Estudio: Office treatment of congenital ankyloglossia

- **ID:** NAIMER2003
- **Autores, año y revista:** Naimer SA; Biton A; Vardy D; Zvulunov A. Med Sci Monit 2003;9(10):CR432-5.
- **DOI / PMID / URL:** PMID `14523332`; sin DOI
- **Tipo de estudio:** Serie de casos.
- **Población y tamaño muestral:** 13 niños con 19 adherencias congénitas (1998-2002).
- **Definición diagnóstica y técnicas:** Electrocauterio con anestesia local en consulta.
- **Criterio diagnóstico de anquiloglosia:** MIXTO. Criterios clínicos de movilidad normal modificados de Kotlow (protrusión, barrido de labios), no TRMR.
- **Variables de resultado:** Capacidad de protruir la lengua.
- **Resultados NUMÉRICOS verificados:** Éxito en todos; en un caso persistió la limitación funcional.
- **Límites metodológicos / confusores:** Muy pocos casos.
- **Hallazgos contrarios o no significativos:** No aplica.
- **Conclusión que sí permite / que no permite:** Sí: Describir la frenotomía en consulta. No: Generalizar.
- **Licencia y derechos:** Derechos del editor. Aquí solo metadatos y resumen propio.
- **Estado de lectura:** Resumen PubMed y texto completo revisados el 17/10/2026.

## Figuras

Las leyendas de las figuras no se han podido extraer del texto completo: `PENDIENTE DE VERIFICAR`. [Ver el artículo](https://pubmed.ncbi.nlm.nih.gov/14523332/).

---

<!-- archivo: fuentes/articulos/2005-kummer-asha-leader.md -->
# Estudio: Ankyloglossia: To Clip or Not to Clip? That's the Question

- **ID:** KUMMER2005
- **Autores, año y revista:** Kummer AW. The ASHA Leader, diciembre de 2005.
- **DOI / PMID / URL:** DOI `10.1044/leader.ftr2.10172005.6`
- **Tipo de estudio:** Artículo de opinión en la revista profesional de la ASHA. No indexado en PubMed.
- **Población y tamaño muestral:** No aplica.
- **Definición diagnóstica y técnicas:** No aplica.
- **Criterio diagnóstico de anquiloglosia:** Texto no leído: PENDIENTE DE VERIFICAR.
- **Variables de resultado:** No aplica.
- **Resultados NUMÉRICOS verificados:** No leído. Según notas de trabajo previas (sin verificar en el original), sostiene que la R inglesa se puede producir con la punta de la lengua abajo y que no hay pruebas de que el frenillo cause problemas del habla.
- **Límites metodológicos / confusores:** Opinión de experta, no estudio.
- **Hallazgos contrarios o no significativos:** Ver CORDRAY2023.
- **Conclusión que sí permite / que no permite:** Sí: Citar la postura de la logopedia oficial estadounidense en 2005. No: Usarlo como evidencia empírica.
- **Licencia y derechos:** Derechos de ASHA. Solo metadatos.
- **Estado de lectura:** Metadatos comprobados en Crossref (17/10/2026).

## Figuras

Figuras no revisadas: el texto completo no está en acceso abierto en PMC. [Ver el artículo](https://doi.org/10.1044/leader.ftr2.10172005.6).

---

<!-- archivo: fuentes/articulos/2005-nice-frenotomia-lactancia.md -->
# Estudio: Division of ankyloglossia (tongue-tie) for breastfeeding (NICE)

- **ID:** NICE2005
- **Autores, año y revista:** National Institute for Health and Care Excellence (NICE), Reino Unido. Guía de procedimientos intervencionistas IPG149, 14/12/2005. Hoy se llama HealthTech guidance 95 (HTG95), con las recomendaciones sin cambios.
- **DOI / PMID / URL:** URL: https://www.nice.org.uk/guidance/htg95
- **Tipo de estudio:** Guía de procedimiento de una agencia pública (seguridad y eficacia de una técnica). No es una guía de diagnóstico.
- **Población y tamaño muestral:** Lactantes con anquiloglosia y problemas de lactancia.
- **Definición diagnóstica y técnicas:** Evalúa la técnica de cortar el frenillo con tijera roma.
- **Criterio diagnóstico de anquiloglosia:** NO PROPONE NINGUNO. La guía evalúa el procedimiento y no define cómo se diagnostica la anquiloglosia.
- **Variables de resultado:** Seguridad y efecto sobre la lactancia.
- **Resultados NUMÉRICOS verificados:** 1.1: no hay problemas importantes de seguridad y una evidencia «limitada» sugiere que puede mejorar la lactancia; basta para usarla con consentimiento, auditoría y gobierno clínico. 1.2: solo deben hacerla profesionales sanitarios registrados y formados. 1.3: serían útiles más ensayos controlados sobre la lactancia a largo plazo.
- **Límites metodológicos / confusores:** Es de 2005. La página dice «Last reviewed: 14 December 2005» y que se revisará si hay nueva evidencia o problemas de seguridad.
- **Hallazgos contrarios o no significativos:** La propia guía califica la evidencia de beneficio como limitada.
- **Conclusión que sí permite / que no permite:** Sí: Decir que NICE considera la frenotomía segura y admisible para problemas de lactancia, hecha por profesionales formados. No: Usarla como criterio diagnóstico, ni para niños mayores, habla o sueño.
- **Licencia y derechos:** Contenido de NICE. Aquí solo resumen propio.
- **Estado de lectura:** Página de NICE y sus recomendaciones leídas el 02/11/2026. Búsqueda de actualización del 02/11/2026.

## Figuras

Figuras no revisadas. [Ver el documento](https://www.nice.org.uk/guidance/htg95).

---

<!-- archivo: fuentes/articulos/2005-ricke-prevalencia-lactancia-atlff.md -->
# Estudio: Newborn tongue-tie: prevalence and effect on breast-feeding

- **ID:** RICKE2005
- **Autores, año y revista:** Ricke LA; Baker NJ; Madlon-Kay DJ; DeFor TA. *J Am Board Fam Pract* 2005;18(1):1–7.
- **DOI / PMID / URL:** DOI `10.3122/jabfm.18.1.1`; PMID `15709057`; [texto completo original disponible gratuitamente](https://www.jabfm.org/content/jabfp/18/1/1.full.pdf).
- **Tipo de estudio:** Casos y controles emparejados, con cribado neonatal prospectivo y entrevista a la semana y al mes.
- **Población y tamaño muestral:** **3.490** neonatos examinados en Regions Hospital, Minnesota (octubre de 2000–mayo de 2002); **148** identificados por apariencia como tongue-tie (**4,24 %**). Después de exclusiones: **49 casos y 98 controles** (dos controles por caso). Seguimiento telefónico: semana 1, **38 casos/71 controles**; mes 1, **33/65**. Los datos posfrenotomía de cuatro casos se retiraron de la comparación del seguimiento.
- **Definición diagnóstica y técnicas:** El cribado **lo realizaron enfermeras por el ASPECTO del frenillo, apoyadas en un catálogo fotográfico**. Una investigadora confirmó visualmente el hallazgo y solo entonces se aplicó a los casos la herramienta **ATLFF de Hazelbaker (5 ítems de aspecto y 7 de función)**. Los controles también fueron explorados funcionalmente. En este estudio se utilizaron tres categorías: «Perfect» (función=14), «Acceptable» (función=11 y aspecto=10) y «Function Impaired» (función<11); el sistema dejaba sin clasificar otras puntuaciones. En emparejamiento: edad materna ±5 años, etnia, primiparidad y sexo del bebé. Se utilizó IBFAT materno y entrevistas telefónicas. El personal de lactancia y las madres no recibieron las puntuaciones ATLFF del equipo.
- **Criterio diagnóstico de anquiloglosia:** **LONGITUD/ASPECTO para entrar en el grupo con anquiloglosia**. El ATLFF **MIXTO se aplicó a posteriori como evaluación adicional**, **no** como criterio de selección de los 148 casos. Este matiz es central para comparar estudios.
- **Variables de resultado:** Prevalencia de «frenillo corto» visible; abandono de lactancia materna / alimentación solo con biberón; IBFAT; utilidad e interobservador de ATLFF.
- **Resultados NUMÉRICOS verificados en métodos/tablas del original:**
  - **Alimentación solo con biberón en semana 1:** **8/38 (21,05 %) casos** frente a **4/71 (5,63 %) controles**, **RR 3,11** (IC95 % 1,21–8,03); diferencia de estado de alimentación p=0,035.
  - **Al mes:** **10/33 (30,3 %) casos** frente a **15/65 (23,08 %) controles**, **RR 1,00** (IC95 % 0,55–1,82); diferencia global de estado de alimentación p=0,46.
  - **IBFAT inicial:** media **10,08** casos frente a **9,97** controles; el 85 % de las madres solo anotó una toma.
  - **Puntuaciones ATLFF entre los 49 casos:** **12 Perfect**, **0 Acceptable**, **6 Function Impaired** y **31 sin categoría definida** (**63 %**). La concordancia entre observadores para función alterada fue **κ=0,49**, moderada, pese al entrenamiento directo por Hazelbaker.
  - **Tabla 5 (semana 1, subgrupos muy pequeños):** 2/5 con «Function Impaired» y 1/8 con «Perfect» estaban con solo biberón; otros **2/5** del primer grupo tuvieron frenotomía y continuaban con solo lactancia materna. La tabla no permite extraer efectos quirúrgicos comparativos.
- **Hallazgo útil para el debate diagnóstico:** El **método de selección por apariencia** y el posterior uso de una escala funcional se confunden fácilmente en revisiones. En este caso, además, los propios investigadores consideraron que ATLFF **no resultaba útil para predecir dificultades de lactancia**, destacando su interobservador moderado y que la versión de la escala **dejaba el 63 % de los casos fuera de las categorías**.
- **Aportación del estudio:** Documenta la evolución neonatal, los resultados de alimentación y las dificultades de aplicar un instrumento diagnóstico que combina aspecto y función. Permite formular preguntas sobre **qué fenotipo se selecciona en cada investigación** y cómo validar la función sin utilizar apariencia como filtro obligatorio.
- **Límites metodológicos / confusores (decisivos):** Cribado inicial visual, seguimiento incompleto y madres que podían recibir apoyo clínico; cuatro frenotomías fuera del seguimiento analítico; población exclusivamente neonatal. Las comparaciones de grupos son observacionales.
- **Licencia y derechos:** PDF libremente accesible, con aviso de copyright de la revista; no se reproduce ni incorpora al repositorio.
- **Estado de lectura:** **Texto completo PDF del editor, métodos, resultados, tablas 1–5 y discusión revisados el 04/11/2026**. Extracción textual del PDF disponible; el renderizado de páginas en la herramienta web falló, por lo que no se efectuó una inspección visual de todas sus figuras.
## Figuras

Fig. 1: flujo de inclusión (3.490 → 148 → 49 casos/98 controles). [Ver original](https://www.jabfm.org/content/jabfp/18/1/1.full.pdf).

---

<!-- archivo: fuentes/articulos/2007-gilbert-hidrostato-lingual.md -->
# Gilbert et al. (2007) — Anatomical basis of lingual hydrostatic deformation

- DOI: `10.1242/jeb.007096`; PMID: `18025008`.
- Tipo: revisión/análisis anatómico y de imagen de deformación lingual.
- Hallazgo: movimientos fisiológicos se relacionan con contracciones sinérgicas de fibras orientadas en diferentes direcciones.
- Sirve para: biomecánica de la deformación tridimensional.
- No sirve para: inferir resultados terapéuticos en anquiloglosia.
- Criterio diagnóstico de anquiloglosia: NO APLICA: estudio anatómico o biomecánico, no diagnostica anquiloglosia.
- Estado: metadatos y resumen revisados; ficha detallada pendiente.

## Figuras

Figuras no revisadas: el texto completo no está en acceso abierto en PMC. [Ver el artículo](https://doi.org/10.1242/jeb.007096).

---

<!-- archivo: fuentes/articulos/2009-guimaraes-ejercicios-orofaringeos.md -->
# Estudio: Effects of oropharyngeal exercises on patients with moderate obstructive sleep apnea syndrome

- **ID:** GUIMARAES2009
- **Autores, año y revista:** Guimarães KC; Drager LF; Genta PR et al.. Am J Respir Crit Care Med 2009;179(10):962-6.
- **DOI / PMID / URL:** DOI `10.1164/rccm.200806-981OC`; PMID `19234106`
- **Tipo de estudio:** Ensayo aleatorizado con terapia simulada. Registro NCT00660777.
- **Población y tamaño muestral:** 31 adultos con apnea moderada: 16 ejercicios y 15 control.
- **Definición diagnóstica y técnicas:** 3 meses de ejercicios diarios de lengua, paladar blando y pared faríngea lateral (unos 30 min) frente a terapia simulada.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA: el estudio no diagnostica anquiloglosia.
- **Variables de resultado:** IAH, ronquido, Epworth, Pittsburgh, perímetro del cuello.
- **Resultados NUMÉRICOS verificados:** Grupo de ejercicios: IAH 22,4 → 13,7; Epworth 14 → 8; perímetro del cuello 39,6 → 38,5 cm. Sin cambios en el grupo control. El cambio del cuello se correlacionó con el del IAH (r=0,59).
- **Límites metodológicos / confusores:** Muestra pequeña y corta duración.
- **Hallazgos contrarios o no significativos:** No aplica.
- **Conclusión que sí permite / que no permite:** Sí: Decir que los ejercicios orofaríngeos redujeron la apnea moderada frente a placebo en este ensayo. No: Extrapolar a niños o a apnea grave.
- **Licencia y derechos:** Derechos del editor. Aquí solo metadatos y resumen propio.
- **Estado de lectura:** Resumen PubMed revisado el 17/10/2026.

## Figuras

Figuras no revisadas: el texto completo no está en acceso abierto en PMC. [Ver el artículo](https://doi.org/10.1164/rccm.200806-981OC).

---

<!-- archivo: fuentes/articulos/2011-alonso-alvarez-consenso-sahs-infantil.md -->
# Estudio: Documento de consenso del síndrome de apneas-hipopneas durante el sueño en niños (versión completa)

- **ID:** ALONSOALVAREZ2011
- **Autores, año y revista:** Alonso-Álvarez ML; Canet T; Cubell-Alarco M; Estivill E; Fernández-Julián E; Gozal D; Jurado-Luque MJ; Lluch-Roselló MA; Martínez-Pérez F; Merino-Andreu M; Pin-Arboledas G; Roure N; Sanmartí FX; Sans-Capdevila O; Segarra-Isern F; Tomás-Vila M; Terán-Santos J. *Arch Bronconeumol* 2011;47(Supl 5):2-18. Reproducido con permiso en *Rev Bol Ped* 2012;51(1).
- **DOI / PMID / URL:** DOI `10.1016/S0300-2896(11)70026-6`; https://www.archbronconeumol.org/es-documento-consenso-del-sindrome-apneas-hipopneas-articulo-S0300289611700266
- **Tipo de estudio:** Documento de consenso español de expertos. Avalado por SEPAR, la Sociedad Española de Sueño, SEPEAP, AEPap y SEORL.
- **Población y tamaño muestral:** Niños.
- **Definición diagnóstica y técnicas:** Polisomnografía como prueba de referencia; propone la poligrafía respiratoria como primera técnica diagnóstica en la población infantil con sospecha, reservando la polisomnografía para casos con comorbilidad, dudas u otras patologías del sueño.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA: consenso de apnea. Búsqueda en el texto completo el 05/11/2026: no aparecen «frenillo», «anquiloglosia», «miofuncional», «ortodoncia» ni «expansión». En la exploración pide valorar la anatomía craneofacial y de la vía aérea (respiración bucal, hipertrofia adenoamigdalar, retrognatia, Mallampati).
- **Variables de resultado:** No aplica (consenso).
- **Resultados NUMÉRICOS verificados:** Tratamiento de elección: adenoamigdalectomía. Eficacia citada de aproximadamente el 78 %, variable según estudios; cita un estudio multicéntrico con una tasa de curación de solo el 27,2 %. Riesgo posquirúrgico del 0 al 1,3 % en general y del 16 al 27 % en niños con apnea. Estudio de sueño tras la cirugía en los casos graves o si persisten síntomas o factores de riesgo.
- **Límites metodológicos / confusores (solo los relevantes):** Evidencia hasta 2010. Recoge que la revisión Cochrane de entonces no encontraba ensayos doble ciego y que la literatura sobre adenoamigdalectomía tenía problemas metodológicos (sin aleatorización ni controles y con definiciones variables).
- **Otros resultados relevantes (si los hay):** Considera aceptado tratar siempre los casos graves o con riesgo de complicaciones serias, no operar el ronquido simple, y controvertido el tratamiento de las alteraciones polisomnográficas leves.
- **Aportación del estudio:** Es el último consenso español sobre apnea infantil localizado. El consenso internacional de 2022 (Mediano et al.) trata solo adultos y anunció un documento pediátrico aparte que no se ha encontrado (búsqueda del 05/11/2026).
- **Licencia y derechos:** Copyright de SEPAR. Aquí solo resumen propio.
- **Estado de lectura:** Texto completo (reproducción en SciELO Bolivia) leído por búsqueda de términos y en el apartado de tratamiento el 05/11/2026.

## Figuras

Figuras no revisadas. [Ver el documento](https://doi.org/10.1016/S0300-2896(11)70026-6).

---

<!-- archivo: fuentes/articulos/2011-engelke-presiones-intraorales.md -->
# Estudio: Intra-oral compartment pressures: a biofunctional model and experimental measurements under different conditions of posture

- **ID:** ENGELKE2011
- **Autores, año y revista:** Engelke W; Jung K; Knösel M. *Clinical Oral Investigations* 2011;15(2):165–176 (publicación online 02/02/2010).
- **DOI / PMID / URL:** DOI `10.1007/s00784-009-0367-0`; PMID `20127264`; PMCID `PMC3056003`; [texto completo libre Springer](https://link.springer.com/article/10.1007/s00784-009-0367-0).
- **Tipo de estudio:** Experimento **fisiológico de medidas repetidas** en cuatro condiciones orales provocadas en personas sanas. No es un ensayo de frenectomía ni un estudio de crecimiento.
- **Población y tamaño muestral:** **20 adultos** sanos con oclusión clase I (**9 hombres, 11 mujeres**, edad media **28,05 ± 8,34 años**). Exclusión por historia de vía aérea obstruida y respiración nasal alterada; **no es una muestra de pacientes con obstrucción nasal, apnea o anquiloglosia**.
- **Definición diagnóstica y técnicas:** Manometría simultánea en **dos espacios**: (1) vestibular interoclusal (IOS, entre labios/mejillas y arcadas) y (2) **subpalatino (SPS, entre dorso lingual y bóveda palatina)**, a través de catéteres comunicados con sensores de presión. Condiciones seriadas en sillón: **OC** boca abierta 30 s; **SC** labios suavemente cerrados 60 s; **CCN** tras tragar saliva y mantener compartimentos cerrados 60 s; **SW** nueva deglución 15 s. Se analizaron picos, mesetas y presiones medias, con comparación por fase y localización.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA: no se reclutó por frenillo corto, TRMR ni por disfunción de lengua. Un protocolo de deglución en adultos con respiración nasal normal **no mide por sí solo restricción funcional lingual**.
- **Variables de resultado:** Presión intraoral media (mbar) y picos/mesetas de presión por compartimento y condición, para comprobar si hay mecanismos biomecánicos distintos.
- **Resultados NUMÉRICOS verificados en el texto original:**
  - **Boca abierta (OC):** IOS **0,00 mbar**, SPS **−0,08 mbar**.
  - **Labios suavemente cerrados (SC):** IOS **−0,16 mbar**, SPS **−1,0 mbar** (presión cercana a atmosférica).
  - **Tras deglución, compartimento cerrado con presión negativa (CCN):** IOS **−48,79 mbar**, SPS **−81,86 mbar**.
  - **Deglución (SW):** IOS **−29,25 mbar**, SPS **−62,51 mbar**.
  - Efectos de **fase y localización** significativos en múltiples parámetros (ANOVA p<0,01); el contraste entre compartimentos fue especialmente marcado en CCN y en presión media/pico durante deglución.
  - La comprobación de variabilidad se hizo con **dos participantes** repetidos ocho veces cada uno (no equivale a demostrar fiabilidad universal del método).
- **Límites metodológicos / confusores:** Pequeña muestra de **adultos sanos seleccionados para oclusión normal y respiración nasal sin alteraciones**; no midió fuerzas reales crónicas sobre huesos, desplazamiento mandibular ni remodelado maxilar. Condiciones **instruidas**, no postura espontánea de sueño ni patrón basal durante días; los autores mencionan posible influencia del catéter/sistema por pérdidas de presión y variación entre individuos. Las presiones son relativas a atmósfera en compartimentos y **no** idénticas a presión ejercida localmente por la lengua sobre suturas, dientes o base ósea. Un fenómeno fisiológico observado no identifica el trastorno patológico que lo modifica.
- **Hallazgos contrarios o no significativos:** En las fases OC y SC no hubo presiones negativas intensas; **cerrar los labios sin un sellado posterior eficaz no produjo la magnitud de CCN**. La discusión reconoce que sus hallazgos no coinciden directamente con mediciones de **presión positiva lengua/diente** de otros autores, y propone la coexistencia de presión intracompartimental negativa y contacto positivo en zonas de sello; hipótesis biomecánica coherente, no medición directa de fuerzas en vivo sobre estructuras óseas.
- **Conclusión que sí permite / que no permite:** **Sí:** demostrar presiones intraorales diferentes en compartimentos subpalatino e interoclusal bajo condiciones voluntarias, y que un sello posterior/oral ayuda a mantener presión negativa sin actividad muscular continua igual a una tarea de soplado. **No:** concluir que «presión negativa» provoque un crecimiento óseo concreto, que frenillo corto impida generar el sello en pacientes clínicos, que elevar la lengua cure apnea, ni que un individuo con TRMR normal tenga necesariamente sellado funcional posterior normal.
- **Licencia y derechos:** Original **open access CC BY-NC 2.0**. Síntesis propia; no se duplican figuras, tablas o PDF.
- **Estado de lectura:** **Texto completo HTML de Springer** comprobado el 03/11/2026, incluidos criterios de inclusión/exclusión, método, resultados, discusión y límites. No se ha reanalizado la señal fisiológica cruda ni los 20 registros individuales.

## Figuras

No copiadas; [fuente original](https://doi.org/10.1007/s00784-009-0367-0).

---

<!-- archivo: fuentes/articulos/2011-kim-guilleminault-nasomaxilar.md -->
# Estudio: The nasomaxillary complex, the mandible, and sleep-disordered breathing

- **ID:** KIM2011
- **Autores, año y revista:** Kim JH; Guilleminault C. Sleep Breath 2011.
- **DOI / PMID / URL:** DOI `10.1007/s11325-011-0504-2`; PMID `21394611`
- **Tipo de estudio:** Revisión retrospectiva de historias y polisomnografías.
- **Población y tamaño muestral:** 400 niños no obesos de 2 a 17 años con trastorno respiratorio del sueño.
- **Definición diagnóstica y técnicas:** Escalas clínicas de Mallampati, amígdalas (Friedman), oclusión y rasgos nasomaxilares y mandibulares.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA: el estudio no diagnostica anquiloglosia.
- **Variables de resultado:** Frecuencia de paladar alto y estrecho o mandíbula pequeña; respuesta a la adenoamigdalectomía.
- **Resultados NUMÉRICOS verificados:** Amígdalas 3+ o 4+ en 290 (72,6 %); rasgos craneofaciales de riesgo en 373 (93,3 %). IAH previo medio 14,6. De 378 seguidos, 167 con IAH residual; peor respuesta con Mallampati 3-4.
- **Límites metodológicos / confusores:** Retrospectivo; escalas subjetivas.
- **Hallazgos contrarios o no significativos:** No se describen en el resumen.
- **Conclusión que sí permite / que no permite:** Sí: Decir que en niños con trastorno respiratorio del sueño los rasgos craneofaciales de riesgo son casi universales. No: Afirmar causa.
- **Licencia y derechos:** Derechos del editor. Aquí solo metadatos y resumen propio.
- **Estado de lectura:** Resumen PubMed revisado el 17/10/2026.

## Figuras

Figuras no revisadas: el texto completo no está en acceso abierto en PMC. [Ver el artículo](https://doi.org/10.1007/s11325-011-0504-2).

---

<!-- archivo: fuentes/articulos/2011-kotlow-laser-lactantes.md -->
# Estudio: Diagnosis and treatment of ankyloglossia and tied maxillary fraenum in infants using Er:YAG and 1064 diode lasers

- **ID:** KOTLOW2011
- **Autores, año y revista:** Kotlow L. Eur Arch Paediatr Dent 2011;12(2):106-12.
- **DOI / PMID / URL:** DOI `10.1007/BF03262789`; PMID `21473843`
- **Tipo de estudio:** Revisión y descripción de técnica.
- **Población y tamaño muestral:** No aplica.
- **Definición diagnóstica y técnicas:** Láser Er:YAG y diodo.
- **Criterio diagnóstico de anquiloglosia:** LONGITUD/ASPECTO. Clasificaciones propias de frenillo lingual y labial en lactantes. Detalle: PENDIENTE DE VERIFICAR.
- **Variables de resultado:** No aplica.
- **Resultados NUMÉRICOS verificados:** Sin cifras en el resumen.
- **Límites metodológicos / confusores:** Opinión de autor.
- **Hallazgos contrarios o no significativos:** No aplica.
- **Conclusión que sí permite / que no permite:** Sí: Citar el origen de la clasificación del frenillo labial y su técnica láser. No: Afirmar eficacia.
- **Licencia y derechos:** Derechos del editor. Aquí solo metadatos y resumen propio.
- **Estado de lectura:** Resumen PubMed y texto completo revisados el 17/10/2026.

## Figuras

Licencia: derechos del editor (no se copian imágenes). Leyendas leídas en el texto completo; puede haber más figuras que las listadas.

- **Figura 3.** Frenillos labiales de clase II a IV que pueden afectar a la lactancia. [Ver en el artículo](https://doi.org/10.1007/BF03262789), figura 3.

---

<!-- archivo: fuentes/articulos/2011-quintessence-estetica-rostro.md -->
# Estudio: Estética del rostro (Puesta al día)

- **ID:** QUINTESSENCE2011
- **Autores, año y revista:** PENDIENTE DE VERIFICAR. Quintessence técnica (ed. esp.) 2011;22(2), traducción de un artículo de 2010;36(7):886-900.
- **DOI / PMID / URL:** sin DOI
- **Tipo de estudio:** Artículo de revisión sobre análisis facial.
- **Población y tamaño muestral:** No aplica.
- **Definición diagnóstica y técnicas:** Análisis facial con posición natural de la cabeza y proporciones.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA: el estudio no diagnostica anquiloglosia.
- **Variables de resultado:** No aplica.
- **Resultados NUMÉRICOS verificados:** No aplica.
- **Límites metodológicos / confusores:** Autores y revista original PENDIENTE DE VERIFICAR.
- **Hallazgos contrarios o no significativos:** No aplica.
- **Conclusión que sí permite / que no permite:** Sí: Consulta de método de análisis facial. No: Citarlo sin completar la referencia.
- **Licencia y derechos:** Derechos del editor. Aquí solo metadatos y resumen propio.
- **Estado de lectura:** texto completo revisado el 17/10/2026.

## Figuras

Licencia: derechos del editor (no se copian imágenes). Leyendas leídas en el texto completo; puede haber más figuras que las listadas.

- **Figura 8.** Tipos de cara: dolicofacial, mesofacial y braquifacial. Sin enlace público.
- **Figura 18.** Vertical por subnasal en posición natural de la cabeza. Sin enlace público.

---

<!-- archivo: fuentes/articulos/2012-bonuck-cohorte-alspac.md -->
# Estudio: Sleep-disordered breathing in a population-based cohort: behavioral outcomes at 4 and 7 years

- **ID:** BONUCK2012
- **Autores, año y revista:** Bonuck K; Freeman K; Chervin RD; Xu L. Pediatrics 2012;129(4):e857-65.
- **DOI / PMID / URL:** DOI `10.1542/peds.2011-1402`; PMID `22392181`; https://pmc.ncbi.nlm.nih.gov/articles/PMC3313633/
- **Tipo de estudio:** Cohorte poblacional longitudinal (ALSPAC, Reino Unido).
- **Población y tamaño muestral:** Conducta medida a los 4 años en 9.140 niños y a los 7 en 8.098.
- **Definición diagnóstica y técnicas:** Los padres informaron de ronquido, respiración oral y apneas vistas de los 6 a los 69 meses. Conducta con el cuestionario SDQ.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA: el estudio no diagnostica anquiloglosia.
- **Variables de resultado:** Problemas de conducta (percentil 90 del SDQ).
- **Resultados NUMÉRICOS verificados:** Los patrones de síntomas predijeron entre un 20 % y un 100 % más de probabilidad de problemas de conducta, ajustado por 15 confusores. El grupo «peor caso», con pico a los 30 meses que luego cedía, predijo hiperactividad a los 7 años (OR 1,85; IC 1,30-2,63).
- **Límites metodológicos / confusores:** Síntomas referidos por los padres, sin polisomnografía. Observacional.
- **Hallazgos contrarios o no significativos:** No aplica.
- **Conclusión que sí permite / que no permite:** Sí: Decir que ronquido, respiración oral y apneas en los primeros años predicen más hiperactividad después, aunque los síntomas hayan desaparecido. No: Afirmar causalidad.
- **Licencia y derechos:** Acceso abierto en PMC. Licencia PENDIENTE DE VERIFICAR.
- **Estado de lectura:** Resumen PubMed revisado el 17/10/2026.

## Figuras

Licencia del artículo: Derechos del editor (copia de autor en PMC). No se copian imágenes.

Figuras no extraídas: la versión de PMC no se puede leer por la API. [Ver el artículo en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC3313633/). Descripción: `PENDIENTE DE VERIFICAR`.

---

<!-- archivo: fuentes/articulos/2012-knoesel-lengua-deglucion-respiracion-bucal.md -->
# Estudio: Coordination of Tongue Activity During Swallowing in Mouth-breathing Children

- **ID:** KNOESEL2012
- **Autores, año y revista:** Knösel M; Klein S; Bleckmann A; Engelke W. *Dysphagia* 2012;27(3):401–407 (publicación online 30/12/2011).
- **DOI / PMID / URL:** DOI `10.1007/s00455-011-9383-8`; PMID `22207245`; PMCID `PMC3417098`; [texto completo abierto](https://link.springer.com/article/10.1007/s00455-011-9383-8).
- **Tipo de estudio:** Estudio fisiológico **intrasujeto, prospectivo y de corto plazo**, con cinco condiciones repetidas de respiración/deglución, sin brazo externo aleatorizado ni seguimiento de crecimiento.
- **Población y tamaño muestral:** **29 niños** de **6–16 años** (media 9,69; 13 niñas y 16 niños) reclutados en dos centros de ortodoncia de Santa Fe (Argentina) por **postura bucal abierta habitual**. **27/29** habían sido clasificados clínicamente como deglución «visceral».
- **Definición diagnóstica y técnicas:** **Criterio de inclusión decisivo:** se exigió que el niño **pudiera colocar voluntariamente la lengua en la papila incisiva superior con la boca abierta**; quienes no lo consiguieron **fueron excluidos**. Sensores ópticos intraorales en férula palatina a nivel de primeros premolares registraron distancia lengua–paladar; termistores nasales detectaron pausa respiratoria de deglución (NAI). Cinco condiciones de **8 minutos**: F1 reposo respiratorio habitual; F2 reposo con pantalla/escudo oral (sellado labial artificial); F3 pantalla + instrucción de mantener contacto palatino; F4 pantalla + maniobra de reposicionamiento y deglución; F5 instrucción de contacto palatino sin pantalla. Umbral de contacto alto: >87,5 % de amplitud óptica calibrada.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA: **no midió anquiloglosia** ni Kotlow/TRMR; por selección **excluyó limitaciones graves de alcance de la papila**. No equivale a un estudio de respuesta al tratamiento en población con restricción lingual.
- **Variables de resultado:** Momento y duración de contacto lengua–paladar respecto a interrupción del flujo aéreo nasal durante deglución; proporción de **contacto temprano** (ya existe al comenzar NAI) frente a **tardío** (aparece después); patrón de reposo lingual posdeglución.
- **Resultados NUMÉRICOS verificados en texto completo:**
  - **542 actos de deglución** entre 29 niños bajo las cinco condiciones (número de observaciones **no equivale a 542 individuos independientes**).
  - Tendencia a contacto temprano con pantalla en F2–F4: **58,72–62,18 %**; sin pantalla en F1/F5 hubo más equilibrio e incluso predominio de contacto tardío (**51,39–54,39 %** tardío).
  - Las **maniobras con pantalla** F3/F4 aumentaron significativamente la frecuencia de contacto temprano frente a reposo habitual; diferencia global de condiciones reportada **p=0,04**.
  - **Pantalla sola sin maniobras:** tendencia a contacto temprano, **no significativa** (F2 frente a F1, **p=0,068**).
  - Pausa respiratoria de deglución (NAI) **≈370 ± 20 ms**; similar entre condiciones.
  - A pesar de que **27/29** tenían diagnóstico clínico de deglución visceral, la polisensografía durante respiración basal **no mostró un predominio marcado** de contacto tardío: los autores cuestionan que la observación con labios abiertos discrimine por sí sola el patrón fisiológico.
- **Límites metodológicos / confusores:** Muestra pequeña y seleccionada, **sin niños que no podían alcanzar la papila** (sesgo decisivo para la hipótesis de restricción funcional), ausencia de control sin intervención a largo plazo y sin cegamiento clínico confirmado. La misma persona produjo muchos actos, con potencial **dependencia intrapaciente** al usar frecuencias y χ²; antes de concluir error estadístico, comprobar si los análisis controlaron la agrupación por participante. La pantalla **sustituye mecánicamente** el sellado labial durante la prueba: efecto inmediato sobre una tarea, no adquisición espontánea duradera. No cuantificó crecimiento maxilar, AHI/PSG ni respuesta de niños con anquiloglosia. El patrón de «respirador bucal» se seleccionó clínicamente por postura abierta, no por monitorización prolongada de permeabilidad nasal.
- **Hallazgos contrarios o no significativos:** **Pantalla sola p=0,068**; observación clínica de «deglución visceral» discordante de la distribución de contacto temprano/tardío en sensor; **respiración oral habitual no coincidió necesariamente con contacto tardío**. Estos resultados impiden presentar a todos los niños con boca abierta como si tuvieran idéntica mecánica lingual.
- **Conclusión que sí permite / que no permite:** **Sí:** en niños capaces de elevar voluntariamente la lengua, un sello labial artificial **combinado con instrucciones** puede cambiar de inmediato la sincronización del contacto lengua–paladar durante deglución; la observación clínica de deglución tiene limitaciones. **No:** que la intervención modifique postura basal duradera, maduración ósea, respiración nocturna, apnea o que la lengua funcione igual en niños **que no logran elevarla**.
- **Licencia y derechos:** Acceso abierto bajo licencia **CC BY-NC 2.0** (atribución no comercial). Ficha de síntesis propia; ni figuras ni PDF redistribuidos.
- **Estado de lectura:** **Texto completo HTML editorial, métodos, resultados y discusión** verificados el 03/11/2026 en [Springer](https://link.springer.com/article/10.1007/s00455-011-9383-8). Las tablas se identificaron por su descripción, pero **no se reanalizó archivo bruto ni datos participante por participante**.

## Figuras

No reproducidas. [Texto original](https://doi.org/10.1007/s00455-011-9383-8).

---

<!-- archivo: fuentes/articulos/2012-marchesan-protocolo.md -->
# Estudio: Lingual frenulum protocol

- **ID:** MARCHESAN2012
- **Autores, año y revista:** Marchesan IQ. Int J Orofacial Myology 2012;38:89-103.
- **DOI / PMID / URL:** PMID `23367525`; sin DOI
- **Tipo de estudio:** Desarrollo de protocolo con puntuación.
- **Población y tamaño muestral:** 1.235 sujetos evaluados en 3 años; versión final aplicada a 239 (160 niños de 7 a 11 años y 79 adultos).
- **Definición diagnóstica y técnicas:** Protocolo de logopedia con pruebas generales y funcionales puntuadas.
- **Criterio diagnóstico de anquiloglosia:** MIXTO. Pruebas generales (frenillo alterado si suman 3 o más) y pruebas funcionales (interferencia en funciones si suman 25 o más).
- **Variables de resultado:** Puntuación del protocolo.
- **Resultados NUMÉRICOS verificados:** Cortes: 3 en pruebas generales y 25 en funcionales.
- **Límites metodológicos / confusores:** El resumen no da fiabilidad ni validez frente a un patrón de referencia.
- **Hallazgos contrarios o no significativos:** No aplica.
- **Conclusión que sí permite / que no permite:** Sí: Citar un protocolo que combina anatomía y función. No: Afirmar su precisión diagnóstica.
- **Licencia y derechos:** Derechos del editor. Aquí solo metadatos y resumen propio.
- **Estado de lectura:** Resumen PubMed revisado el 17/10/2026. Sin DOI.

## Figuras

Figuras no revisadas: el texto completo no está en acceso abierto en PMC. [Ver el artículo](https://pubmed.ncbi.nlm.nih.gov/23367525/).

---

<!-- archivo: fuentes/articulos/2012-marcus-aap-guia-apnea.md -->
# Estudio: Diagnosis and Management of Childhood Obstructive Sleep Apnea Syndrome (American Academy of Pediatrics, clinical practice guideline)

- **ID:** MARCUS2012
- **Autores, año y revista:** Marcus CL; Brooks LJ; Draper KA; Gozal D; Halbower AC; Jones J; Schechter MS; Sheldon SH; Spruyt K; Ward SD; Lehmann C; Shiffman RN; American Academy of Pediatrics. *Pediatrics* 2012;130(3):576-584.
- **DOI / PMID / URL:** DOI `10.1542/peds.2012-1671`; PMID `22926173`; https://publications.aap.org/pediatrics/article/130/3/576/30284/Diagnosis-and-Management-of-Childhood-Obstructive
- **Tipo de estudio:** Guía de práctica clínica de la AAP (revisión de la de 2002), con informe técnico aparte (Pediatrics 2012;130(3):e714-e755). Dirigida a atención primaria.
- **Población y tamaño muestral:** Niños y adolescentes con apnea «no complicada»: hipertrofia adenoamigdalar u obesidad en un niño por lo demás sano. Excluye a menores de 1 año y a niños con alteraciones craneofaciales, neuromusculares u otras enfermedades asociadas. Base: de 3.166 artículos de 1999 a 2010, 350 con datos relevantes, la mayoría de nivel II a IV.
- **Definición diagnóstica y técnicas:** Polisomnografía en niños que roncan y tienen síntomas o signos de apnea.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA: guía de apnea. Búsqueda en el texto completo el 05/11/2026: no aparecen «ankyloglossia», «tongue-tie», «frenulum», «tongue», «myofunctional» ni «orthodontic». Excluye de su alcance a los niños con anomalías craneofaciales.
- **Variables de resultado:** No aplica (guía).
- **Resultados NUMÉRICOS verificados:** Ocho recomendaciones (resumen): (1) preguntar a todos los niños si roncan; (2) polisomnografía si roncan y tienen síntomas o signos, o derivar si no está disponible; (3) adenoamigdalectomía como primer tratamiento si hay hipertrofia adenoamigdalar; (4) vigilar ingresados tras la cirugía a los pacientes de alto riesgo; (5) reevaluar tras la cirugía, con prueba objetiva en los de alto riesgo o con síntomas persistentes; (6) CPAP si no se operan o si la apnea persiste; (7) perder peso si hay sobrepeso u obesidad; (8) corticoides nasales como opción en apnea leve si la cirugía está contraindicada o en apnea leve tras la cirugía.
- **Límites metodológicos / confusores (solo los relevantes):** Evidencia hasta 2010. Es anterior al ensayo CHAT (Marcus 2013), que comparó la adenoamigdalectomía con la espera vigilante.
- **Otros resultados relevantes (si los hay):** En noviembre de 2026 no se ha encontrado una versión más nueva de la AAP; la siguen citando como vigente, por ejemplo el manual de referencia de la AAPD 2025-2026. Si se reafirmó formalmente: `PENDIENTE DE VERIFICAR`. Sobre la apnea que persiste tras la cirugía dice que otros tratamientos, por ejemplo la expansión rápida del maxilar, pueden ser eficaces en pacientes seleccionados.
- **Aportación del estudio:** Es la guía de la AAP sobre apnea infantil vigente y la que se suele citar.
- **Licencia y derechos:** Copyright de la AAP. Aquí solo resumen propio.
- **Estado de lectura:** Texto completo (PDF de la AAP) leído por búsqueda de términos y en las recomendaciones el 05/11/2026.

## Figuras

Figuras no revisadas. [Ver la guía](https://doi.org/10.1542/peds.2012-1671).

---

<!-- archivo: fuentes/articulos/2012-martinelli-protocolo-lactantes.md -->
# Estudio: Lingual frenulum protocol with scores for infants

- **ID:** MARTINELLI2012
- **Autores, año y revista:** Martinelli RL; Marchesan IQ; Berretin-Felix G. Int J Orofacial Myology 2012;38:104-12.
- **DOI / PMID / URL:** PMID `23362754`; sin DOI
- **Tipo de estudio:** Desarrollo de protocolo con puntuación.
- **Población y tamaño muestral:** 100 lactantes a término (piloto con 10).
- **Definición diagnóstica y técnicas:** Historia clínica (familia y lactancia) y exploración anatomofuncional con succión no nutritiva y nutritiva.
- **Criterio diagnóstico de anquiloglosia:** MIXTO. Anatomía más función de succión, en lactantes.
- **Variables de resultado:** Concordancia entre la evaluadora y dos especialistas.
- **Resultados NUMÉRICOS verificados:** Sin cifras de concordancia en el resumen: PENDIENTE DE VERIFICAR.
- **Límites metodológicos / confusores:** Una sola evaluadora en directo; los otros dos sobre vídeo y fotos.
- **Hallazgos contrarios o no significativos:** No aplica.
- **Conclusión que sí permite / que no permite:** Sí: Citar el protocolo («Teste da Linguinha») para lactantes. No: Aplicarlo a niños mayores o adultos.
- **Licencia y derechos:** Derechos del editor. Aquí solo metadatos y resumen propio.
- **Estado de lectura:** Resumen PubMed revisado el 17/10/2026. Sin DOI.

## Figuras

Figuras no revisadas: el texto completo no está en acceso abierto en PMC. [Ver el artículo](https://pubmed.ncbi.nlm.nih.gov/23362754/).

---

<!-- archivo: fuentes/articulos/2013-guilleminault-reeducacion-miofascial.md -->
# Estudio: Critical role of myofascial reeducation in pediatric sleep-disordered breathing

- **ID:** GUILLEMINAULT2013
- **Autores, año y revista:** Guilleminault C; Huang YS; Monteyrol PJ et al.. Sleep Med 2013;14(6):518-25.
- **DOI / PMID / URL:** DOI `10.1016/j.sleep.2013.01.013`; PMID `23522724`
- **Tipo de estudio:** Estudio retrospectivo. Polisomnografía de seguimiento puntuada por un investigador cegado.
- **Población y tamaño muestral:** Subgrupo de 24 niños (14 varones) con polisomnografía normal tras adenoamigdalectomía y ortodoncia; 11 hicieron terapia miofuncional.
- **Definición diagnóstica y técnicas:** Polisomnografía al diagnóstico, tras la cirugía y a largo plazo (22 a 50 meses).
- **Criterio diagnóstico de anquiloglosia:** NO APLICA: el estudio no diagnostica anquiloglosia.
- **Variables de resultado:** Recaída del trastorno respiratorio del sueño.
- **Resultados NUMÉRICOS verificados:** Los 13 sin terapia recayeron (IAH medio 5,3 ± 1,5; saturación mínima 91 %). Los 11 que completaron 24 meses de reeducación siguieron sanos.
- **Límites metodológicos / confusores:** Retrospectivo, sin aleatorizar. Muestra muy pequeña. Los propios autores dicen que había pocas historias completas.
- **Hallazgos contrarios o no significativos:** No aplica.
- **Conclusión que sí permite / que no permite:** Sí: Plantear que la terapia miofuncional podría prevenir recaídas. No: Afirmarlo como efecto causal demostrado.
- **Licencia y derechos:** Derechos del editor. Aquí solo metadatos y resumen propio.
- **Estado de lectura:** Resumen PubMed revisado el 17/10/2026.

## Figuras

Figuras no revisadas: el texto completo no está en acceso abierto en PMC. [Ver el artículo](https://doi.org/10.1016/j.sleep.2013.01.013).

---

<!-- archivo: fuentes/articulos/2013-marcus-ensayo-chat.md -->
# Estudio: A randomized trial of adenotonsillectomy for childhood sleep apnea

- **ID:** MARCUS2013
- **Autores, año y revista:** Marcus CL; Moore RH; Rosen CL et al.; Childhood Adenotonsillectomy Trial (CHAT). N Engl J Med 2013;368(25):2366-76.
- **DOI / PMID / URL:** DOI `10.1056/NEJMoa1215881`; PMID `23692173`; https://pmc.ncbi.nlm.nih.gov/articles/PMC3756808/
- **Tipo de estudio:** Ensayo aleatorizado (CHAT). NCT00560859.
- **Población y tamaño muestral:** 464 niños de 5 a 9 años con apnea sin desaturaciones prolongadas.
- **Definición diagnóstica y técnicas:** Adenoamigdalectomía temprana frente a espera vigilada. Evaluación a los 7 meses.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA: el estudio no diagnostica anquiloglosia.
- **Variables de resultado:** Primaria: atención y función ejecutiva (NEPSY). Secundarias: conducta, calidad de vida, síntomas, polisomnografía.
- **Resultados NUMÉRICOS verificados:** Atención y función ejecutiva sin diferencia (mejora 7,1 frente a 5,1; P=0,16). Mejoras significativas en conducta, calidad de vida y polisomnografía. Normalización de la polisomnografía: 79 % con cirugía frente a 46 % con espera.
- **Límites metodológicos / confusores:** Seguimiento corto (7 meses). Excluye apnea grave.
- **Hallazgos contrarios o no significativos:** El resultado principal (atención medida con test) fue negativo.
- **Conclusión que sí permite / que no permite:** Sí: Decir que operar mejora la conducta, el sueño y la calidad de vida, pero no la atención medida con test. No: Decir que operar mejora el TDAH.
- **Licencia y derechos:** Acceso abierto en PMC. Licencia PENDIENTE DE VERIFICAR.
- **Estado de lectura:** Resumen PubMed revisado el 17/10/2026.

## Figuras

Licencia del artículo: Manuscrito de autor; uso según «fair use» (no permite copiar aquí). No se copian imágenes.

- **Figura 1.** Diagrama de inclusión y aleatorización (464 niños). [Ver en el artículo](https://pmc.ncbi.nlm.nih.gov/articles/PMC3756808/).
- **Figura 2.** Porcentaje con normalización de la polisomnografía, por subgrupos. [Ver en el artículo](https://pmc.ncbi.nlm.nih.gov/articles/PMC3756808/).

---

<!-- archivo: fuentes/articulos/2013-ocallahan-frenotomia-anterior-posterior.md -->
# Estudio: The effects of office-based frenotomy for anterior and posterior ankyloglossia on breastfeeding

- **ID:** OCALLAHAN2013
- **Autores, año y revista:** O'Callahan C; Macary S; Clemente S. Int J Pediatr Otorhinolaryngol 2013;77(5):827-32.
- **DOI / PMID / URL:** DOI `10.1016/j.ijporl.2013.02.022`; PMID `23523198`
- **Tipo de estudio:** Serie con encuesta web posterior.
- **Población y tamaño muestral:** 311 lactantes valorados, 299 operados; 157 encuestas.
- **Definición diagnóstica y técnicas:** Frenotomía en consulta de atención primaria.
- **Criterio diagnóstico de anquiloglosia:** LONGITUD/ASPECTO. Coryllos: anterior (tipos I-II) frente a posterior (tipos III-IV).
- **Variables de resultado:** Agarre, dolor del pezón, lactancia exclusiva y duración.
- **Resultados NUMÉRICOS verificados:** Tipo III 36 % y tipo IV 49 %; anterior 16 %. Agarre mejor en posteriores (p<0,001). Dolor menor en todos (p<0,001). 92 % lactancia exclusiva después; duración media 14 meses.
- **Límites metodológicos / confusores:** Encuesta retrospectiva, sin control, sesgo de recuerdo y de respuesta.
- **Hallazgos contrarios o no significativos:** No aplica.
- **Conclusión que sí permite / que no permite:** Sí: Documentar que muchas anquiloglosias derivadas eran posteriores. No: Afirmar eficacia frente a no tratar.
- **Licencia y derechos:** Derechos del editor. Aquí solo metadatos y resumen propio.
- **Estado de lectura:** Resumen PubMed y texto completo revisados el 17/10/2026.

## Figuras

Licencia: derechos del editor (no se copian imágenes). Leyendas leídas en el texto completo; puede haber más figuras que las listadas.

- **Figura 2.** Lactante de un mes con anquiloglosia tipo IV. [Ver en el artículo](https://doi.org/10.1016/j.ijporl.2013.02.022), figura 2.

---

<!-- archivo: fuentes/articulos/2014-lacerda-sindrome-respiracion-oral.md -->
# Estudio: The mouth breathing syndrome: prevalence, causes, consequences and treatment

- **ID:** LACERDA2014
- **Autores, año y revista:** Lacerda Martins DL; Fontes Silva Cunha Lima L; Demeda VF et al.. J Surg Cl Res 2014;5(1):47-55.
- **DOI / PMID / URL:** sin DOI
- **Tipo de estudio:** Revisión narrativa (Universidad Federal de Rio Grande do Norte).
- **Población y tamaño muestral:** No aplica.
- **Definición diagnóstica y técnicas:** No aplica.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA: el estudio no diagnostica anquiloglosia.
- **Variables de resultado:** No aplica.
- **Resultados NUMÉRICOS verificados:** Sin cifras propias revisadas.
- **Límites metodológicos / confusores:** Revista no indexada en PubMed ni Europe PMC (búsqueda del 17/10/2026).
- **Hallazgos contrarios o no significativos:** No aplica.
- **Conclusión que sí permite / que no permite:** Sí: Citar un resumen general del síndrome de respiración oral. No: Usarlo como evidencia primaria.
- **Licencia y derechos:** Derechos del editor. Aquí solo metadatos y resumen propio.
- **Estado de lectura:** texto completo revisado el 17/10/2026; sin DOI ni PMID localizados.

## Figuras

Las leyendas de las figuras no se han podido extraer del texto completo: `PENDIENTE DE VERIFICAR`. Sin enlace público.

---

<!-- archivo: fuentes/articulos/2014-sedky-tdah-trs.md -->
# Estudio: Attention deficit hyperactivity disorder and sleep disordered breathing in pediatric populations: a meta-analysis

- **ID:** SEDKY2014
- **Autores, año y revista:** Sedky K; Bennett DS; Carvalho KS. Sleep Med Rev 2014;18(4):349-56.
- **DOI / PMID / URL:** DOI `10.1016/j.smrv.2013.12.003`; PMID `24581717`
- **Tipo de estudio:** Metaanálisis en dos partes.
- **Población y tamaño muestral:** Parte 1: 18 estudios, 1.113 niños clínicos y 1.405 controles. Parte 2: 12 estudios antes y después de adenoamigdalectomía, 529 niños.
- **Definición diagnóstica y técnicas:** Búsqueda en PubMed, PsycInfo y Cochrane hasta septiembre de 2012.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA: el estudio no diagnostica anquiloglosia.
- **Variables de resultado:** Síntomas de TDAH frente a trastorno respiratorio del sueño.
- **Resultados NUMÉRICOS verificados:** Relación media entre síntomas de TDAH y trastorno respiratorio del sueño: g de Hedges 0,57 (IC 95 % 0,36-0,78). Tras la cirugía, mejoría de síntomas de TDAH a los 2-13 meses: g 0,43 (IC 0,30-0,55).
- **Límites metodológicos / confusores:** Estudios antes y después sin control en la segunda parte. Asociación, no causa.
- **Hallazgos contrarios o no significativos:** Un corte de IAH más alto se asoció a efectos más pequeños.
- **Conclusión que sí permite / que no permite:** Sí: Decir que los síntomas de TDAH se asocian a respirar mal durmiendo y que mejoran tras operar. No: Decir que el TDAH sea un trastorno del sueño.
- **Licencia y derechos:** Derechos del editor. Aquí solo metadatos y resumen propio.
- **Estado de lectura:** Resumen PubMed revisado el 17/10/2026.

## Figuras

Figuras no revisadas: el texto completo no está en acceso abierto en PMC. [Ver el artículo](https://doi.org/10.1016/j.smrv.2013.12.003).

---

<!-- archivo: fuentes/articulos/2015-camacho-miofuncional-apnea.md -->
# Estudio: Myofunctional Therapy to Treat Obstructive Sleep Apnea: A Systematic Review and Meta-analysis

- **ID:** CAMACHO2015
- **Autores, año y revista:** Camacho M; Certal V; Abdullatif J; Zaghi S et al.. Sleep 2015;38(5):669-75.
- **DOI / PMID / URL:** DOI `10.5665/sleep.4652`; PMID `25348130`; https://pmc.ncbi.nlm.nih.gov/articles/PMC4402674/
- **Tipo de estudio:** Revisión sistemática y metaanálisis. PRISMA.
- **Población y tamaño muestral:** 9 estudios en adultos (120 pacientes) y 2 en niños (25 pacientes).
- **Definición diagnóstica y técnicas:** Terapia miofuncional frente a situación previa.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA: el estudio no diagnostica anquiloglosia.
- **Variables de resultado:** IAH, saturación mínima, ronquido, Epworth.
- **Resultados NUMÉRICOS verificados:** Adultos: IAH 24,5 → 12,3 (diferencia media -14,26; P<0,0001); saturación mínima 83,9 → 86,6 %; ronquido 14,05 → 3,87 % del sueño; Epworth 14,8 → 8,2. Niños: un estudio de 14 niños con IAH 4,87 → 1,84; otro con 11 que siguieron la terapia sin recaída frente a 13 controles con recaída (IAH 5,3). Conclusión: el IAH baja un 50 % en adultos y un 62 % en niños.
- **Límites metodológicos / confusores:** Pocos pacientes, sobre todo en niños. Estudios pequeños y heterogéneos. Zaghi es coautor.
- **Hallazgos contrarios o no significativos:** No se describen en el resumen.
- **Conclusión que sí permite / que no permite:** Sí: Decir que la terapia miofuncional reduce la apnea y puede servir como complemento. No: Presentarla como sustituto de otros tratamientos en apnea grave.
- **Licencia y derechos:** Acceso abierto en PMC. Licencia PENDIENTE DE VERIFICAR.
- **Estado de lectura:** Resumen PubMed revisado el 17/10/2026.

## Figuras

Licencia del artículo: Derechos del editor. No se copian imágenes.

Figuras no extraídas: la versión de PMC no se puede leer por la API. [Ver el artículo en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC4402674/). Descripción: `PENDIENTE DE VERIFICAR`.

---

<!-- archivo: fuentes/articulos/2015-certal-estimulacion-hipogloso.md -->
# Estudio: Hypoglossal nerve stimulation in the treatment of obstructive sleep apnea: A systematic review and meta-analysis

- **ID:** CERTAL2015
- **Autores, año y revista:** Certal VF; Zaghi S; Riaz M et al.. Laryngoscope 2015.
- **DOI / PMID / URL:** DOI `10.1002/lary.25032`; PMID `25389029`
- **Tipo de estudio:** Revisión sistemática (con metaanálisis si lo indica el título).
- **Población y tamaño muestral:** 6 estudios prospectivos, 200 adultos.
- **Definición diagnóstica y técnicas:** Búsqueda en varias bases de datos.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA: el estudio no diagnostica anquiloglosia.
- **Variables de resultado:** IAH, saturación mínima y somnolencia, salvo que se indique otra cosa.
- **Resultados NUMÉRICOS verificados:** A 12 meses: IAH -17,51, ODI -13,73 y Epworth -4,42. IAH reducido un 50-57 %.
- **Límites metodológicos / confusores:** Estudios primarios pequeños y sobre todo series de casos. Zaghi es coautor.
- **Hallazgos contrarios o no significativos:** No se describen en el resumen.
- **Conclusión que sí permite / que no permite:** Sí: Decir que la estimulación del hipogloso reduce la apnea en pacientes seleccionados. No: Compararla con otras terapias.
- **Licencia y derechos:** Derechos del editor. Aquí solo metadatos y resumen propio.
- **Estado de lectura:** Resumen PubMed revisado el 17/10/2026.

## Figuras

Figuras no revisadas: el texto completo no está en acceso abierto en PMC. [Ver el artículo](https://doi.org/10.1002/lary.25032).

---

<!-- archivo: fuentes/articulos/2015-chinnadurai-mas-alla-lactancia.md -->
# Estudio: Treatment of ankyloglossia for reasons other than breastfeeding: a systematic review

- **ID:** CHINNADURAI2015
- **Autores, año y revista:** Chinnadurai S; Francis DO; Epstein RA et al.. Pediatrics 2015;135(6):e1467-74.
- **DOI / PMID / URL:** DOI `10.1542/peds.2015-0660`; PMID `25941312`; https://pmc.ncbi.nlm.nih.gov/articles/PMC9923517/
- **Tipo de estudio:** Revisión sistemática (AHRQ).
- **Población y tamaño muestral:** 2 ensayos, 2 cohortes y 11 series de casos.
- **Definición diagnóstica y técnicas:** Medline, PsycINFO, CINAHL y Embase.
- **Criterio diagnóstico de anquiloglosia:** Variable entre estudios: PENDIENTE DE VERIFICAR.
- **Variables de resultado:** Alimentación, habla y aspectos sociales.
- **Resultados NUMÉRICOS verificados:** Dos cohortes describen mejora de articulación e inteligibilidad. Un ensayo: mejor articulación con Z-plastia que con frenuloplastia horizontal-vertical.
- **Límites metodológicos / confusores:** Pocos estudios comparativos.
- **Hallazgos contrarios o no significativos:** Conclusión: datos insuficientes.
- **Conclusión que sí permite / que no permite:** Sí: Decir que en 2015 la evidencia era insuficiente para efectos fuera de la lactancia. No: Decir que no hay efecto.
- **Licencia y derechos:** Acceso abierto en PMC. Licencia PENDIENTE DE VERIFICAR.
- **Estado de lectura:** Resumen PubMed y texto completo revisados el 17/10/2026.

## Figuras

Licencia del artículo: Derechos del editor. No se copian imágenes.

- **Figura 1.** Diagrama de selección de artículos (del texto completo). [Ver en el artículo](https://pmc.ncbi.nlm.nih.gov/articles/PMC9923517/).

---

<!-- archivo: fuentes/articulos/2015-francis-revision-lactancia.md -->
# Estudio: Treatment of ankyloglossia and breastfeeding outcomes: a systematic review

- **ID:** FRANCIS2015
- **Autores, año y revista:** Francis DO; Krishnaswami S; McPheeters M. Pediatrics 2015;135(6):e1458-66.
- **DOI / PMID / URL:** DOI `10.1542/peds.2015-0658`; PMID `25941303`; PMC9923619.
- **Tipo de estudio:** Revisión sistemática. Corresponde a la revisión de efectividad comparada de la AHRQ (agencia federal de EE. UU.) sobre anquiloglosia: `PENDIENTE DE VERIFICAR` el número del informe completo.
- **Población y tamaño muestral:** 29 estudios con resultados de lactancia: 5 ensayos aleatorizados, 1 cohorte retrospectiva y 23 series de casos. Búsqueda hasta agosto de 2014.
- **Definición diagnóstica y técnicas:** Medline, PsycINFO, CINAHL y Embase; dos revisores independientes; fuerza de la evidencia graduada.
- **Criterio diagnóstico de anquiloglosia:** MIXTO. Define la anquiloglosia como frenillo corto, engrosado o tenso que restringe la movilidad. Los estudios incluidos usaban herramientas distintas: `PENDIENTE DE VERIFICAR` cuáles.
- **Variables de resultado:** Eficacia de la lactancia, dolor del pezón.
- **Resultados NUMÉRICOS verificados:** Cuatro ensayos mostraron mejoras de eficacia de la lactancia (por la madre o por observador) y dos no las encontraron con observador. Las madres refieren mejoría de forma constante tras la frenotomía. Fuerza de la evidencia: baja a insuficiente.
- **Límites metodológicos / confusores:** Estudios pequeños, a corto plazo y con métodos heterogéneos. Ningún estudio de tratamiento no quirúrgico ni de lactancia a largo plazo.
- **Hallazgos contrarios o no significativos:** Dos ensayos sin mejora observada.
- **Conclusión que sí permite / que no permite:** Sí: Decir que en 2015 la evidencia de que la frenotomía mejore la lactancia era baja o insuficiente. No: Decir que la frenotomía no funciona.
- **Licencia y derechos:** Acceso abierto en PMC. Aquí solo resumen propio.
- **Estado de lectura:** Resumen de PubMed revisado el 02/11/2026. Búsqueda de actualización del 02/11/2026.

## Figuras

Figuras no revisadas. [Ver el documento](https://pmc.ncbi.nlm.nih.gov/articles/PMC9923619/).

---

<!-- archivo: fuentes/articulos/2015-riaz-provent.md -->
# Estudio: Nasal Expiratory Positive Airway Pressure Devices (Provent) for OSA: A Systematic Review and Meta-Analysis

- **ID:** RIAZ2015
- **Autores, año y revista:** Riaz M; Certal V; Nigam G et al.. Sleep Disord 2015.
- **DOI / PMID / URL:** DOI `10.1155/2015/734798`; PMID `26798519`
- **Tipo de estudio:** Revisión sistemática (con metaanálisis si lo indica el título).
- **Población y tamaño muestral:** 18 estudios, 920 pacientes.
- **Definición diagnóstica y técnicas:** Búsqueda en varias bases de datos.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA: el estudio no diagnostica anquiloglosia.
- **Variables de resultado:** IAH, saturación mínima y somnolencia, salvo que se indique otra cosa.
- **Resultados NUMÉRICOS verificados:** IAH 27,32 → 12,78 (-53,2 %). ODI -41,5 %. Saturación mínima +3 puntos.
- **Límites metodológicos / confusores:** Estudios primarios pequeños y sobre todo series de casos. Zaghi es coautor.
- **Hallazgos contrarios o no significativos:** No se describen en el resumen.
- **Conclusión que sí permite / que no permite:** Sí: Decir que el EPAP nasal reduce la apnea de media. No: Predecir quién responde; una resistencia nasal alta podría asociarse a fracaso.
- **Licencia y derechos:** Derechos del editor. Aquí solo metadatos y resumen propio.
- **Estado de lectura:** Resumen PubMed revisado el 17/10/2026.

## Figuras

Figuras no revisadas: el texto completo no está en acceso abierto en PMC. [Ver el artículo](https://doi.org/10.1155/2015/734798).

---

<!-- archivo: fuentes/articulos/2015-rowan-legg-cps-lactancia.md -->
# Estudio: Ankyloglossia and breastfeeding (Canadian Paediatric Society)

- **ID:** CPS2015
- **Autores, año y revista:** Rowan-Legg A; Canadian Paediatric Society, Community Paediatrics Committee. Paediatr Child Health 2015;20(4):209-218.
- **DOI / PMID / URL:** DOI `10.1093/pch/20.4.209`; PMID `26038641`; PMC4443830.
- **Tipo de estudio:** Documento de posicionamiento de una sociedad pediátrica. Sustituyó a versiones de 2002 y 2011.
- **Población y tamaño muestral:** Lactantes.
- **Definición diagnóstica y técnicas:** Revisión de la evidencia y recomendaciones.
- **Criterio diagnóstico de anquiloglosia:** NO PROPONE NINGUNO. Define la anquiloglosia como un frenillo anormalmente corto que puede restringir la movilidad de la punta. Dice que hay «considerable controversy» sobre su diagnóstico y que las recomendaciones más firmes esperan «clear diagnostic criteria».
- **Variables de resultado:** Indicación de frenotomía en lactancia.
- **Resultados NUMÉRICOS verificados:** La mayoría de lactantes con anquiloglosia no tiene síntomas ni problemas de alimentación. No se puede recomendar la frenotomía a todos. Un subgrupo con problemas importantes de lactancia puede beneficiarse; en ese caso debe hacerla un clínico con experiencia y con analgesia adecuada.
- **Límites metodológicos / confusores:** Posicionamiento basado en la evidencia disponible en 2015.
- **Hallazgos contrarios o no significativos:** Reconoce gran variación de la práctica.
- **Conclusión que sí permite / que no permite:** Sí: Decir que la sociedad pediátrica canadiense consideraba en 2015 que no había criterios diagnósticos claros. No: Presentarlo como vigente: en la web de la CPS el documento figura como retirado («has been removed from our website», consultado el 02/11/2026). Si fue reafirmado antes de retirarse: `PENDIENTE DE VERIFICAR`.
- **Licencia y derechos:** Acceso abierto en PMC. Aquí solo resumen propio.
- **Estado de lectura:** Resumen de PubMed revisado el 02/11/2026. Página de la CPS consultada el 02/11/2026. Búsqueda de actualización del 02/11/2026.

## Figuras

Figuras no revisadas. [Ver el documento](https://pmc.ncbi.nlm.nih.gov/articles/PMC4443830/).

---

<!-- archivo: fuentes/articulos/2015-sepet-apinamiento-oclusion.md -->
# Estudio: Relationship between mandibular incisor irregularity and type of occlusion in ankyloglossia

- **ID:** SEPET2015
- **Autores, año y revista:** Sepet E; Yildiz C; Erdem AP et al.. Oral Health Prev Dent 2015;13(1):59-63.
- **DOI / PMID / URL:** DOI `10.3290/j.ohpd.a32135`; PMID `24914432`
- **Tipo de estudio:** Transversal.
- **Población y tamaño muestral:** 80 niños de 7 a 12 años con anquiloglosia.
- **Definición diagnóstica y técnicas:** Apiñamiento de incisivos inferiores y relación molar.
- **Criterio diagnóstico de anquiloglosia:** LONGITUD/ASPECTO. Clasificación de Kotlow.
- **Variables de resultado:** Apiñamiento inferior y tipo de oclusión.
- **Resultados NUMÉRICOS verificados:** Leve 56,3 %, moderada 28,8 %, grave 15 %. Clase I 70 %, II 21,3 %, III 8,8 %. Sin diferencias por tipo de anquiloglosia. Correlación positiva entre longitud del frenillo e irregularidad.
- **Límites metodológicos / confusores:** Sin grupo sin anquiloglosia.
- **Hallazgos contrarios o no significativos:** Las formas leves y moderadas no se relacionaron con apiñamiento ni oclusión.
- **Conclusión que sí permite / que no permite:** Sí: Citar un estudio negativo con criterio de longitud. No: Usarlo contra la restricción funcional.
- **Licencia y derechos:** Derechos del editor. Aquí solo metadatos y resumen propio.
- **Estado de lectura:** Resumen PubMed y texto completo revisados el 17/10/2026.

## Figuras

Licencia: derechos del editor (no se copian imágenes). Leyendas leídas en el texto completo; puede haber más figuras que las listadas.

- **Figura 1.** Frenillo corto y grueso. [Ver en el artículo](https://doi.org/10.3290/j.ohpd.a32135), figura 1.
- **Figura 2.** Medida de la lengua libre con calibre. [Ver en el artículo](https://doi.org/10.3290/j.ohpd.a32135), figura 2.
- **Figura 3.** Medida del apiñamiento inferior. [Ver en el artículo](https://doi.org/10.3290/j.ohpd.a32135), figura 3.

---

<!-- archivo: fuentes/articulos/2015-vaz-frenillo-maloclusion.md -->
# Estudio: Lingual frenulum and malocclusion: An overlooked tissue or a minor issue

- **ID:** VAZ2015
- **Autores, año y revista:** Vaz AC; Bai PM. Indian J Dent Res 2015;26(5):488-92.
- **DOI / PMID / URL:** DOI `10.4103/0970-9290.172044`; PMID `26672418`
- **Tipo de estudio:** Transversal.
- **Población y tamaño muestral:** 700 escolares de 9 a 17 años (350 de colegios ordinarios y 350 de educación especial).
- **Definición diagnóstica y técnicas:** Clase de Angle; índice de Little; rasgos de maloclusión visuales.
- **Criterio diagnóstico de anquiloglosia:** LONGITUD/ASPECTO. Grados I-V de Kotlow.
- **Variables de resultado:** Relación entre grado de frenillo y maloclusión.
- **Resultados NUMÉRICOS verificados:** Correlaciones negativas entre grado de frenillo y clases I-II y apiñamiento. Frenillos más cortos y tensos asociados a constricción maxilar, mordida abierta anterior y espaciamiento inferior.
- **Límites metodológicos / confusores:** Correlaciones; criterio por longitud.
- **Hallazgos contrarios o no significativos:** No aplica.
- **Conclusión que sí permite / que no permite:** Sí: Citar la asociación entre frenillo corto y maxilar estrecho con criterio de Kotlow. No: Afirmar causa.
- **Licencia y derechos:** Derechos del editor. Aquí solo metadatos y resumen propio.
- **Estado de lectura:** Resumen PubMed y texto completo revisados el 17/10/2026.

## Figuras

Las leyendas de las figuras no se han podido extraer del texto completo: `PENDIENTE DE VERIFICAR`. [Ver el artículo](https://doi.org/10.4103/0970-9290.172044).

---

<!-- archivo: fuentes/articulos/2015-villa-expansion-rapida-apnea-ninos.md -->
# Estudio: Rapid maxillary expansion outcomes in treatment of obstructive sleep apnea in children

- **ID:** VILLA2015
- **Autores, año y revista:** Villa MP; Rizzoli A; Rabasco J et al.. Sleep Med 2015.
- **DOI / PMID / URL:** DOI `10.1016/j.sleep.2014.11.019`; PMID `25934539`
- **Tipo de estudio:** Prospectivo antes y después, con seguimiento retrospectivo a 10 años de un subgrupo.
- **Población y tamaño muestral:** 40 niños con hipertrofia adenoamigdalar moderada; 14 revisados a los 10 años.
- **Definición diagnóstica y técnicas:** Polisomnografía, cefalometría, 12 meses de expansión rápida.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA: el estudio no diagnostica anquiloglosia.
- **Variables de resultado:** IAH y cuestionario de Brouillette.
- **Resultados NUMÉRICOS verificados:** Respondedores (bajada del IAH >20 %) 34 de 40 (85 %). Apnea residual (IAH >1) en el 57,5 %. Los respondedores tenían menos años de enfermedad (2,5 frente a 4,8).
- **Límites metodológicos / confusores:** Sin grupo control.
- **Hallazgos contrarios o no significativos:** No se describen en el resumen.
- **Conclusión que sí permite / que no permite:** Sí: Decir que la expansión temprana redujo la apnea en la mayoría, sobre todo si se empieza pronto. No: Decir que la expansión sola cura: más de la mitad quedó con apnea residual.
- **Licencia y derechos:** Derechos del editor. Aquí solo metadatos y resumen propio.
- **Estado de lectura:** Resumen PubMed revisado el 17/10/2026.

## Figuras

Figuras no revisadas: el texto completo no está en acceso abierto en PMC. [Ver el artículo](https://doi.org/10.1016/j.sleep.2014.11.019).

---

<!-- archivo: fuentes/articulos/2016-abdullatif-expansion-maxilar-adultos.md -->
# Estudio: Maxillary expansion and maxillomandibular expansion for adult OSA: A systematic review and meta-analysis

- **ID:** ABDULLATIF2016
- **Autores, año y revista:** Abdullatif J; Certal V; Zaghi S et al.. J Craniomaxillofac Surg 2016.
- **DOI / PMID / URL:** DOI `10.1016/j.jcms.2016.02.001`; PMID `26948172`
- **Tipo de estudio:** Revisión sistemática (con metaanálisis si lo indica el título).
- **Población y tamaño muestral:** 8 estudios, 39 adultos.
- **Definición diagnóstica y técnicas:** Búsqueda en varias bases de datos.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA: el estudio no diagnostica anquiloglosia.
- **Variables de resultado:** IAH, saturación mínima y somnolencia, salvo que se indique otra cosa.
- **Resultados NUMÉRICOS verificados:** Expansión maxilar (36): IAH 24,3 → 9,9 (-59,3 %). Expansión maxilomandibular (3): IAH 47,5 → 10,7.
- **Límites metodológicos / confusores:** Estudios primarios pequeños y sobre todo series de casos. Zaghi es coautor.
- **Hallazgos contrarios o no significativos:** No se describen en el resumen.
- **Conclusión que sí permite / que no permite:** Sí: Decir que la expansión maxilar podría mejorar la apnea en adultos. No: Darlo por demostrado con tan pocos pacientes.
- **Licencia y derechos:** Derechos del editor. Aquí solo metadatos y resumen propio.
- **Estado de lectura:** Resumen PubMed revisado el 17/10/2026.

## Figuras

Figuras no revisadas: el texto completo no está en acceso abierto en PMC. [Ver el artículo](https://doi.org/10.1016/j.jcms.2016.02.001).

---

<!-- archivo: fuentes/articulos/2016-camacho-amigdalectomia-adultos.md -->
# Estudio: Tonsillectomy for adult obstructive sleep apnea: A systematic review and meta-analysis

- **ID:** CAMACHO2016E
- **Autores, año y revista:** Camacho M; Li D; Kawai M et al.. Laryngoscope 2016;126:2176-2186.
- **DOI / PMID / URL:** DOI `10.1002/lary.25931`; PMID `27005314`
- **Tipo de estudio:** Revisión sistemática (con metaanálisis si lo indica el título).
- **Población y tamaño muestral:** 17 estudios, 216 adultos con amígdalas grandes.
- **Definición diagnóstica y técnicas:** Búsqueda en varias bases de datos.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA: el estudio no diagnostica anquiloglosia.
- **Variables de resultado:** IAH, saturación mínima y somnolencia, salvo que se indique otra cosa.
- **Resultados NUMÉRICOS verificados:** IAH 40,5 → 14,1 (-65,2 %). Éxito 85,2 % y curación 57,4 % con datos individuales. Con IAH previo <30: éxito 100 % y curación 84 %.
- **Límites metodológicos / confusores:** Estudios primarios pequeños y sobre todo series de casos. Zaghi es coautor.
- **Hallazgos contrarios o no significativos:** No se describen en el resumen.
- **Conclusión que sí permite / que no permite:** Sí: Decir que la amigdalectomía aislada funciona en adultos con amígdalas grandes y apnea leve o moderada. No: Extenderla a apnea grave.
- **Licencia y derechos:** Derechos del editor. Aquí solo metadatos y resumen propio.
- **Estado de lectura:** Resumen PubMed revisado el 17/10/2026.

## Figuras

Figuras no revisadas: el texto completo no está en acceso abierto en PMC. [Ver el artículo](https://doi.org/10.1002/lary.25931).

---

<!-- archivo: fuentes/articulos/2016-camacho-cornetes-cpap.md -->
# Estudio: Inferior Turbinate Size and CPAP Titration Based Treatment Pressures: No Association Found among Patients Who Have Not Had Nasal Surgery

- **ID:** CAMACHO2016B
- **Autores, año y revista:** Camacho M; Zaghi S; Tran D et al.. Int J Otolaryngol 2016.
- **DOI / PMID / URL:** DOI `10.1155/2016/5951273`; PMID `26904126`
- **Tipo de estudio:** Serie retrospectiva.
- **Población y tamaño muestral:** 45 pacientes sin cirugía nasal.
- **Definición diagnóstica y técnicas:** Tamaño de cornetes y presión de CPAP.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA: el estudio no diagnostica anquiloglosia.
- **Variables de resultado:** Presión terapéutica.
- **Resultados NUMÉRICOS verificados:** Sin asociación con el tamaño de cornetes. Correlación fuerte con IAH (0,60) y ODI (0,62).
- **Límites metodológicos / confusores:** Muestra pequeña.
- **Hallazgos contrarios o no significativos:** No se describen en el resumen.
- **Conclusión que sí permite / que no permite:** Sí: Decir que el tamaño de cornetes no predijo la presión de CPAP. No: Generalizar a pacientes operados.
- **Licencia y derechos:** Derechos del editor. Aquí solo metadatos y resumen propio.
- **Estado de lectura:** Resumen PubMed revisado el 17/10/2026.

## Figuras

Figuras no revisadas: el texto completo no está en acceso abierto en PMC. [Ver el artículo](https://doi.org/10.1155/2016/5951273).

---

<!-- archivo: fuentes/articulos/2016-camacho-faringoplastia-esfinter.md -->
# Estudio: Expansion sphincter pharyngoplasty for obstructive sleep apnea: an update to the recent meta-analysis

- **ID:** CAMACHO2016D
- **Autores, año y revista:** Camacho M; Zaghi S; Certal V et al.. Eur Arch Otorhinolaryngol 2016.
- **DOI / PMID / URL:** DOI `10.1007/s00405-016-3929-1`; PMID `26993655`
- **Tipo de estudio:** Actualización de un metaanálisis.
- **Población y tamaño muestral:** PENDIENTE DE VERIFICAR
- **Definición diagnóstica y técnicas:** No aplica.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA: el estudio no diagnostica anquiloglosia.
- **Variables de resultado:** No aplica.
- **Resultados NUMÉRICOS verificados:** PubMed no tiene resumen: PENDIENTE DE VERIFICAR.
- **Límites metodológicos / confusores:** PENDIENTE DE VERIFICAR
- **Hallazgos contrarios o no significativos:** No se describen en el resumen.
- **Conclusión que sí permite / que no permite:** Sí: Solo citarlo como existente. No: Dar cifras.
- **Licencia y derechos:** Derechos del editor. Aquí solo metadatos y resumen propio.
- **Estado de lectura:** Solo metadatos PubMed (17/10/2026).

## Figuras

Figuras no revisadas: el texto completo no está en acceso abierto en PMC. [Ver el artículo](https://doi.org/10.1007/s00405-016-3929-1).

---

<!-- archivo: fuentes/articulos/2016-camacho-minitraqueostomia.md -->
# Estudio: Mini Tracheostomy for Obstructive Sleep Apnea: An Evidence Based Proposal

- **ID:** CAMACHO2016C
- **Autores, año y revista:** Camacho M; Zaghi S; Chang ET et al.. Int J Otolaryngol 2016.
- **DOI / PMID / URL:** DOI `10.1155/2016/7195349`; PMID `26925105`
- **Tipo de estudio:** Revisión sistemática (con metaanálisis si lo indica el título).
- **Población y tamaño muestral:** 18 estudios con polisomnografía de traqueostomía; ninguno de minitraqueostomía.
- **Definición diagnóstica y técnicas:** Búsqueda en varias bases de datos.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA: el estudio no diagnostica anquiloglosia.
- **Variables de resultado:** IAH, saturación mínima y somnolencia, salvo que se indique otra cosa.
- **Resultados NUMÉRICOS verificados:** Revisión vacía para minitraqueostomía en apnea.
- **Límites metodológicos / confusores:** Estudios primarios pequeños y sobre todo series de casos. Zaghi es coautor.
- **Hallazgos contrarios o no significativos:** No se describen en el resumen.
- **Conclusión que sí permite / que no permite:** Sí: Decir que la minitraqueostomía en apnea es una propuesta sin datos. No: Usarla como tratamiento probado.
- **Licencia y derechos:** Derechos del editor. Aquí solo metadatos y resumen propio.
- **Estado de lectura:** Resumen PubMed revisado el 17/10/2026.

## Figuras

Figuras no revisadas: el texto completo no está en acceso abierto en PMC. [Ver el artículo](https://doi.org/10.1155/2016/7195349).

---

<!-- archivo: fuentes/articulos/2016-camacho-test-cpap-cinco-minutos.md -->
# Estudio: Five-Minute Awake Snoring Test for Determining CPAP Pressures (Five-Minute CPAP Test): A Pilot Study

- **ID:** CAMACHO2016A
- **Autores, año y revista:** Camacho M; Ruoff CM; Song SA et al.. Sleep Disord 2016.
- **DOI / PMID / URL:** DOI `10.1155/2016/7380874`; PMID `26881088`
- **Tipo de estudio:** Serie prospectiva piloto.
- **Población y tamaño muestral:** 38 pacientes.
- **Definición diagnóstica y técnicas:** CPAP nasal mientras el paciente simula ronquido despierto.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA: el estudio no diagnostica anquiloglosia.
- **Variables de resultado:** Presión a la que deja de poder roncar.
- **Resultados NUMÉRICOS verificados:** Se correlacionó con IMC (r 0,60), IAH (0,49), saturación mínima (-0,47) y ODI (0,62).
- **Límites metodológicos / confusores:** Piloto.
- **Hallazgos contrarios o no significativos:** No se describen en el resumen.
- **Conclusión que sí permite / que no permite:** Sí: Citar un método rápido de estimar presión de CPAP. No: Sustituir la titulación.
- **Licencia y derechos:** Derechos del editor. Aquí solo metadatos y resumen propio.
- **Estado de lectura:** Resumen PubMed revisado el 17/10/2026.

## Figuras

Figuras no revisadas: el texto completo no está en acceso abierto en PMC. [Ver el artículo](https://doi.org/10.1155/2016/7380874).

---

<!-- archivo: fuentes/articulos/2016-capasso-dise-propofol-dexmedetomidina.md -->
# Estudio: Variable Findings for Drug-Induced Sleep Endoscopy in Obstructive Sleep Apnea with Propofol versus Dexmedetomidine

- **ID:** CAPASSO2016
- **Autores, año y revista:** Capasso R; Rosa T; Tsou DY et al.. Otolaryngol Head Neck Surg 2016.
- **DOI / PMID / URL:** DOI `10.1177/0194599815625972`; PMID `26814208`
- **Tipo de estudio:** Serie con revisión de historias.
- **Población y tamaño muestral:** 216 adultos con apnea sometidos a endoscopia del sueño inducida.
- **Definición diagnóstica y técnicas:** Clasificación VOTE.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA: el estudio no diagnostica anquiloglosia.
- **Variables de resultado:** Patrón de obstrucción.
- **Resultados NUMÉRICOS verificados:** Obstrucción completa de base de lengua: 75 % con propofol frente a 42,7 % con dexmedetomidina (OR 4,0).
- **Límites metodológicos / confusores:** No aleatorizado.
- **Hallazgos contrarios o no significativos:** No se describen en el resumen.
- **Conclusión que sí permite / que no permite:** Sí: Decir que el fármaco cambia lo que se ve en la endoscopia del sueño. No: Saber cuál refleja mejor el sueño natural.
- **Licencia y derechos:** Derechos del editor. Aquí solo metadatos y resumen propio.
- **Estado de lectura:** Resumen PubMed revisado el 17/10/2026.

## Figuras

Figuras no revisadas: el texto completo no está en acceso abierto en PMC. [Ver el artículo](https://doi.org/10.1177/0194599815625972).

---

<!-- archivo: fuentes/articulos/2016-guilleminault-frenillo-corto-apnea.md -->
# Estudio: A frequent phenotype for paediatric sleep apnoea: short lingual frenulum

- **ID:** GUILLEMINAULT2016
- **Autores, año y revista:** Guilleminault C; Huseni S; Lo L. ERJ Open Res 2016;2(3):00043-2016.
- **DOI / PMID / URL:** DOI `10.1183/23120541.00043-2016`; PMID `27730205`; https://pmc.ncbi.nlm.nih.gov/articles/PMC5034598/
- **Tipo de estudio:** Análisis retrospectivo de niños consecutivos con sospecha de trastorno respiratorio del sueño.
- **Población y tamaño muestral:** 150 niños de Stanford con polisomnografía sistemática.
- **Definición diagnóstica y técnicas:** Exploración oral clínica y polisomnografía.
- **Criterio diagnóstico de anquiloglosia:** LONGITUD. Texto completo: en niños de 6 años o más usan la lengua libre de Kotlow (normal >16 mm) y la longitud del frenillo de Ruffoli; los dos métodos clasificaron igual. No valoraron grosor ni inserción. En menores de 6 años: PENDIENTE DE VERIFICAR.
- **Variables de resultado:** Grupos de apnea, anatomía oral y antecedentes familiares.
- **Resultados NUMÉRICOS verificados:** Dos grupos con apnea: 63 con frenillo corto sin amígdalas grandes y 87 con frenillo normal y amígdalas grandes. En 60 de los 63 había al menos un familiar directo con frenillo corto y trastorno respiratorio del sueño.
- **Límites metodológicos / confusores:** Retrospectivo. Criterio por longitud. Sin grupo sin síntomas.
- **Hallazgos contrarios o no significativos:** Según Koento 2026, la diferencia de IAH fue pequeña (13,1 frente a 11,4) y solo en varones.
- **Conclusión que sí permite / que no permite:** Sí: Decir que el frenillo corto aparece con frecuencia en niños con apnea sin amígdalas grandes y que suele ser familiar. Los autores piden cribar apnea al ver un frenillo corto. No: Afirmar que el frenillo corto cause la apnea.
- **Licencia y derechos:** Acceso abierto en PMC. Licencia PENDIENTE DE VERIFICAR.
- **Estado de lectura:** Resumen PubMed y fragmentos del texto completo (PMC) revisados el 17/10/2026.

## Figuras

Licencia del artículo: CC BY-NC 4.0 (no permite copiar aquí). Figuras en PubMed Central (PMC5034598).

- **Figura 1.** Medida del frenillo con un kit comercial: frenillo normal y medida de la lengua libre. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC5034598/figure/F1/).
- **Figura 2.** Ejemplos fotográficos de frenillos cortos en niños y adolescentes (solo se valoró la longitud). [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC5034598/figure/F2/).

---

<!-- archivo: fuentes/articulos/2016-kaditis-ers-apnea-2-18.md -->
# Estudio: Obstructive sleep disordered breathing in 2- to 18-year-old children: diagnosis and management (European Respiratory Society statement)

- **ID:** KADITIS2016
- **Autores, año y revista:** Kaditis AG; Alonso Alvarez ML; Boudewyns A; Alexopoulos EI; Ersu R; Joosten K; Larramona H; Miano S; Narang I; Trang H; Tsaoussoglou M; Vandenbussche N; Villa MP; Van Waardenburg D; Weber S; Verhulst S. *Eur Respir J* 2016;47(1):69-94.
- **DOI / PMID / URL:** DOI `10.1183/13993003.00385-2015`; PMID `26541535`.
- **Tipo de estudio:** Declaración de un grupo de trabajo de la European Respiratory Society, con revisión de 362 artículos. No es una guía GRADE: clasifica los estudios por clases (I a IV).
- **Población y tamaño muestral:** Niños de 2 a 18 años con trastorno respiratorio del sueño obstructivo.
- **Definición diagnóstica y técnicas:** Gravedad medida de forma objetiva, preferiblemente con polisomnografía.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA: declaración de apnea. Búsqueda en el texto completo el 05/11/2026: no aparecen «ankyloglossia», «tongue-tie» ni «frenulum».
- **Variables de resultado:** No aplica (declaración).
- **Resultados NUMÉRICOS verificados:** Siete pasos. Parecen beneficiarse del tratamiento: IAH mayor de 5 por hora; IAH de 1 a 5 con morbilidad o factores de persistencia; niños con enfermedades complejas (por ejemplo síndrome de Down o Prader-Willi). Tratamiento escalonado: pérdida de peso, corticoides nasales o montelukast, adenoamigdalectomía, expansión rápida del maxilar o aparatos de ortodoncia, CPAP o ventilación no invasiva, cirugía craneofacial y traqueostomía, con reevaluación tras cada paso para detectar enfermedad residual.
- **Límites metodológicos / confusores (solo los relevantes):** Los propios autores dicen que escasean los estudios de cohortes sobre la historia natural y los ensayos aleatorizados doble ciego sobre el tratamiento.
- **Otros resultados relevantes (si los hay):** Terapia miofuncional: dice que la reeducación con ejercicios nasales y orofaríngeos se ha usado tras la adenoamigdalectomía para tratar la apnea residual o prevenir su reaparición, pero que la evidencia publicada son solo dos estudios de baja calidad metodológica (clase III y IV): Villa 2015 y Guilleminault 2013.
- **Aportación del estudio:** Es la declaración europea de referencia para niños de 2 a 18 años, firmada entre otros por la española Alonso Álvarez.
- **Licencia y derechos:** Copyright de la ERS. Aquí solo resumen propio.
- **Estado de lectura:** Texto completo (copia en PDF) leído por búsqueda de términos y en los apartados de tratamiento el 05/11/2026. No se han revisado las tablas de evidencia.

## Figuras

Figuras no revisadas. [Ver el artículo](https://doi.org/10.1183/13993003.00385-2015).

---

<!-- archivo: fuentes/articulos/2016-mahboub-frenillo-borde-incisal.md -->
# Estudio: Determining the distance from the lingual frenum anterior attachment to the lower incisors' incisal edges

- **ID:** MAHBOUB2016
- **Autores, año y revista:** Mahboub F; Kimyai S; Molavi E. J Dent Res Dent Clin Dent Prospects 2016;10(4):257-262.
- **DOI / PMID / URL:** DOI `10.15171/joddd.2016.041`; PMID `28096953`; https://pmc.ncbi.nlm.nih.gov/articles/PMC5237674/
- **Tipo de estudio:** Transversal en modelos.
- **Población y tamaño muestral:** 40 pacientes.
- **Definición diagnóstica y técnicas:** Medida en modelos de yeso.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA. Usa la inserción del frenillo como referencia protésica.
- **Variables de resultado:** Distancia inserción-borde incisal.
- **Resultados NUMÉRICOS verificados:** 14,35 ± 1,68 mm (10,2-17,02). Hombres 15,42 y mujeres 13,28 mm.
- **Límites metodológicos / confusores:** Muestra pequeña.
- **Hallazgos contrarios o no significativos:** No aplica.
- **Conclusión que sí permite / que no permite:** Sí: Citar una referencia anatómica del suelo de boca. No: Usarla para diagnosticar anquiloglosia.
- **Licencia y derechos:** Acceso abierto en PMC. Licencia PENDIENTE DE VERIFICAR.
- **Estado de lectura:** Resumen PubMed y texto completo revisados el 17/10/2026.

## Figuras

Licencia del artículo: CC BY 4.0. Figuras en PubMed Central (PMC5237674).

- **Figura 1.** Modelo de yeso con la inserción anterior del frenillo marcada. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC5237674/figure/F01/). Copia local: figuras/MAHBOUB2016-fig1.jpg.
- **Figura 2.** Modelo en el paralelizador: contacto del vástago vertical con el punto marcado. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC5237674/figure/F02/). Copia local: figuras/MAHBOUB2016-fig2.jpg.
- **Figura 3.** Segundo punto de contacto en el borde incisal. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC5237674/figure/F03/). Copia local: figuras/MAHBOUB2016-fig3.jpg.
- **Figura 4.** Medida digital de la distancia entre los dos puntos. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC5237674/figure/F04/). Copia local: figuras/MAHBOUB2016-fig4.jpg.

Crédito: figuras de Mahboub F; Kimyai S; Molavi E (PMC5237674), CC BY 4.0. Las copias locales no se han modificado.

---

<!-- archivo: fuentes/articulos/2016-zaghi-mma-metaanalisis.md -->
# Estudio: Maxillomandibular Advancement for Treatment of Obstructive Sleep Apnea: A Meta-analysis

- **ID:** ZAGHI2016
- **Autores, año y revista:** Zaghi S; Holty JE; Certal V et al.. JAMA Otolaryngol Head Neck Surg 2016;142(1):58-66.
- **DOI / PMID / URL:** DOI `10.1001/jamaoto.2015.2678`; PMID `26606321`
- **Tipo de estudio:** Revisión sistemática y metaanálisis con datos individuales de pacientes. PRISMA.
- **Población y tamaño muestral:** 45 estudios, 518 pacientes adultos operados de avance maxilomandibular (MMA) sin cirugías añadidas en el mismo acto.
- **Definición diagnóstica y técnicas:** Datos individuales agregados; modelo de efectos aleatorios.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA: el estudio no diagnostica anquiloglosia.
- **Variables de resultado:** Cambio de IAH e IDR. Éxito quirúrgico (reducción >50 % e IAH <20) y curación (IAH <5).
- **Resultados NUMÉRICOS verificados:** Reducción media del IAH 80,1 % y del IDR 64,6 %. Mejoraron 512 de 518 (98,8 %). Éxito 85,5 % y curación 38,5 % (455 con IAH). Saturación mínima 70,1 % → 87,0 %. Epworth 13,5 → 3,2. Un IAH previo <60 se asoció a más curación.
- **Límites metodológicos / confusores:** Estudios primarios sobre todo series de casos. El 73,5 % ya tenía cirugías previas de apnea.
- **Hallazgos contrarios o no significativos:** La curación completa es minoritaria (38,5 %), sobre todo con IAH previo >60.
- **Conclusión que sí permite / que no permite:** Sí: Decir que el MMA reduce mucho la apnea en adultos y que pocos llegan a curación completa. No: Aplicarlo a niños o a otras cirugías.
- **Licencia y derechos:** Derechos del editor. Aquí solo metadatos y resumen propio.
- **Estado de lectura:** Resumen PubMed revisado el 17/10/2026.

## Figuras

Figuras no revisadas: el texto completo no está en acceso abierto en PMC. [Ver el artículo](https://doi.org/10.1001/jamaoto.2015.2678).

---

<!-- archivo: fuentes/articulos/2017-alonso-catatrenia.md -->
# Estudio: Catathrenia (Nocturnal Groaning): A Social Media Survey and State-of-the-Art Review

- **ID:** ALONSO2017
- **Autores, año y revista:** Alonso J; Camacho M; Chhetri DK et al.. J Clin Sleep Med 2017.
- **DOI / PMID / URL:** DOI `10.5664/jcsm.6556`; PMID `28095968`
- **Tipo de estudio:** Revisión sistemática (con metaanálisis si lo indica el título).
- **Población y tamaño muestral:** 15 casos, 17 series (191 pacientes), 47 cuestionarios de redes sociales.
- **Definición diagnóstica y técnicas:** Búsqueda en varias bases de datos.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA: el estudio no diagnostica anquiloglosia.
- **Variables de resultado:** IAH, saturación mínima y somnolencia, salvo que se indique otra cosa.
- **Resultados NUMÉRICOS verificados:** Sin cifras de efecto. Describe la catatrenia como gemido espiratorio con aducción de cuerdas vocales, distinto del ronquido.
- **Límites metodológicos / confusores:** Estudios primarios pequeños y sobre todo series de casos. Zaghi es coautor.
- **Hallazgos contrarios o no significativos:** No se describen en el resumen.
- **Conclusión que sí permite / que no permite:** Sí: Definir la catatrenia. No: Recomendar tratamientos: los citados (respiración, yoga, terapia miofuncional) son ideas para investigar.
- **Licencia y derechos:** Derechos del editor. Aquí solo metadatos y resumen propio.
- **Estado de lectura:** Resumen PubMed revisado el 17/10/2026.

## Figuras

Figuras no revisadas: el texto completo no está en acceso abierto en PMC. [Ver el artículo](https://doi.org/10.5664/jcsm.6556).

---

<!-- archivo: fuentes/articulos/2017-camacho-cirugia-lengua-ninos.md -->
# Estudio: Tongue surgeries for pediatric obstructive sleep apnea: a systematic review and meta-analysis

- **ID:** CAMACHO2017D
- **Autores, año y revista:** Camacho M; Noller MW; Zaghi S et al.. Eur Arch Otorhinolaryngol 2017.
- **DOI / PMID / URL:** DOI `10.1007/s00405-017-4545-4`; PMID `28378061`
- **Tipo de estudio:** Revisión sistemática (con metaanálisis si lo indica el título).
- **Población y tamaño muestral:** 11 estudios, 116 niños, la mayoría sindrómicos.
- **Definición diagnóstica y técnicas:** Búsqueda en varias bases de datos.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA: el estudio no diagnostica anquiloglosia.
- **Variables de resultado:** IAH, saturación mínima y somnolencia, salvo que se indique otra cosa.
- **Resultados NUMÉRICOS verificados:** Reducción de base de lengua: IAH 16,9 → 8,7 (-48,5 %); -59,2 % en no sindrómicos y -40 % en sindrómicos.
- **Límites metodológicos / confusores:** Estudios primarios pequeños y sobre todo series de casos. Zaghi es coautor.
- **Hallazgos contrarios o no significativos:** No se describen en el resumen.
- **Conclusión que sí permite / que no permite:** Sí: Decir que la cirugía de base de lengua reduce la apnea en niños complejos. No: Aplicarlo a niños sanos.
- **Licencia y derechos:** Derechos del editor. Aquí solo metadatos y resumen propio.
- **Estado de lectura:** Resumen PubMed revisado el 17/10/2026.

## Figuras

Figuras no revisadas: el texto completo no está en acceso abierto en PMC. [Ver el artículo](https://doi.org/10.1007/s00405-017-4545-4).

---

<!-- archivo: fuentes/articulos/2017-camacho-expansion-rapida-ninos-meta.md -->
# Estudio: Rapid maxillary expansion for pediatric obstructive sleep apnea: A systematic review and meta-analysis

- **ID:** CAMACHO2017A
- **Autores, año y revista:** Camacho M; Chang ET; Song SA et al.. Laryngoscope 2017;127:1712-1719.
- **DOI / PMID / URL:** DOI `10.1002/lary.26352`; PMID `27796040`
- **Tipo de estudio:** Revisión sistemática (con metaanálisis si lo indica el título).
- **Población y tamaño muestral:** 17 estudios, 314 niños (7,6 años) con paladar alto o estrecho.
- **Definición diagnóstica y técnicas:** Búsqueda en varias bases de datos.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA: el estudio no diagnostica anquiloglosia.
- **Variables de resultado:** IAH, saturación mínima y somnolencia, salvo que se indique otra cosa.
- **Resultados NUMÉRICOS verificados:** A ≤3 años: IAH 8,9 → 2,7 (-70 %); curación (IAH <1) 25,6 %. A >3 años (52 niños): IAH 7,1 → 1,5. Más mejora con amígdalas operadas o pequeñas (73-95 %) que grandes (61 %).
- **Límites metodológicos / confusores:** Estudios primarios pequeños y sobre todo series de casos. Zaghi es coautor.
- **Hallazgos contrarios o no significativos:** No se describen en el resumen.
- **Conclusión que sí permite / que no permite:** Sí: Decir que la expansión rápida mejora la apnea infantil a corto plazo. No: Separar su efecto del crecimiento y la resolución espontánea.
- **Licencia y derechos:** Derechos del editor. Aquí solo metadatos y resumen propio.
- **Estado de lectura:** Resumen PubMed revisado el 17/10/2026.

## Figuras

Figuras no revisadas: el texto completo no está en acceso abierto en PMC. [Ver el artículo](https://doi.org/10.1002/lary.26352).

---

<!-- archivo: fuentes/articulos/2017-camacho-pierre-robin-lengua.md -->
# Estudio: Tongue-lip adhesion and tongue repositioning for obstructive sleep apnoea in Pierre Robin sequence: A systematic review and meta-analysis

- **ID:** CAMACHO2017B
- **Autores, año y revista:** Camacho M; Noller MW; Zaghi S et al.. J Laryngol Otol 2017.
- **DOI / PMID / URL:** DOI `10.1017/S0022215117000056`; PMID `28193305`
- **Tipo de estudio:** Revisión sistemática (con metaanálisis si lo indica el título).
- **Población y tamaño muestral:** 7 estudios, 90 niños con secuencia de Pierre Robin.
- **Definición diagnóstica y técnicas:** Búsqueda en varias bases de datos.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA: el estudio no diagnostica anquiloglosia.
- **Variables de resultado:** IAH, saturación mínima y somnolencia, salvo que se indique otra cosa.
- **Resultados NUMÉRICOS verificados:** Adhesión lengua-labio: IAH 30,8 → 15,4 (-50 %). Reposicionamiento lingual: 46,5 → 17,4 (-62,6 %).
- **Límites metodológicos / confusores:** Estudios primarios pequeños y sobre todo series de casos. Zaghi es coautor.
- **Hallazgos contrarios o no significativos:** No se describen en el resumen.
- **Conclusión que sí permite / que no permite:** Sí: Decir que estas técnicas mejoran la apnea en Pierre Robin. No: Aplicarlas fuera de ese síndrome.
- **Licencia y derechos:** Derechos del editor. Aquí solo metadatos y resumen propio.
- **Estado de lectura:** Resumen PubMed revisado el 17/10/2026.

## Figuras

Figuras no revisadas: el texto completo no está en acceso abierto en PMC. [Ver el artículo](https://doi.org/10.1017/S0022215117000056).

---

<!-- archivo: fuentes/articulos/2017-camacho-uvulopalatoplastia-laser.md -->
# Estudio: Laser-Assisted Uvulopalatoplasty for Obstructive Sleep Apnea: A Systematic Review and Meta-Analysis

- **ID:** CAMACHO2017C
- **Autores, año y revista:** Camacho M; Nesbitt NB; Lambert E et al.. Sleep 2017.
- **DOI / PMID / URL:** DOI `10.1093/sleep/zsx004`; PMID `28201808`
- **Tipo de estudio:** Revisión sistemática (con metaanálisis si lo indica el título).
- **Población y tamaño muestral:** 23 estudios, 717 adultos.
- **Definición diagnóstica y técnicas:** Búsqueda en varias bases de datos.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA: el estudio no diagnostica anquiloglosia.
- **Variables de resultado:** IAH, saturación mínima y somnolencia, salvo que se indique otra cosa.
- **Resultados NUMÉRICOS verificados:** IAH -32 %. Éxito 23 %, curación 8 %; el 44 % empeoró.
- **Límites metodológicos / confusores:** Estudios primarios pequeños y sobre todo series de casos. Zaghi es coautor.
- **Hallazgos contrarios o no significativos:** No se describen en el resumen.
- **Conclusión que sí permite / que no permite:** Sí: Decir que la uvulopalatoplastia láser da malos resultados y que los autores desaconsejan hacerla. No: Extenderlo a otras cirugías de paladar.
- **Licencia y derechos:** Derechos del editor. Aquí solo metadatos y resumen propio.
- **Estado de lectura:** Resumen PubMed revisado el 17/10/2026.

## Figuras

Figuras no revisadas: el texto completo no está en acceso abierto en PMC. [Ver el artículo](https://doi.org/10.1093/sleep/zsx004).

---

<!-- archivo: fuentes/articulos/2017-chang-dise-revision.md -->
# Estudio: Dexmedetomidine versus propofol during drug-induced sleep endoscopy and sedation: a systematic review

- **ID:** CHANG2017
- **Autores, año y revista:** Chang ET; Certal V; Song SA et al.. Sleep Breath 2017.
- **DOI / PMID / URL:** DOI `10.1007/s11325-017-1465-x`; PMID `28130737`
- **Tipo de estudio:** Revisión sistemática (con metaanálisis si lo indica el título).
- **Población y tamaño muestral:** 10 estudios.
- **Definición diagnóstica y técnicas:** Búsqueda en varias bases de datos.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA: el estudio no diagnostica anquiloglosia.
- **Variables de resultado:** IAH, saturación mínima y somnolencia, salvo que se indique otra cosa.
- **Resultados NUMÉRICOS verificados:** Dexmedetomidina más estable; propofol muestra más obstrucción y desaturación.
- **Límites metodológicos / confusores:** Estudios primarios pequeños y sobre todo series de casos. Zaghi es coautor.
- **Hallazgos contrarios o no significativos:** No se describen en el resumen.
- **Conclusión que sí permite / que no permite:** Sí: Comparar fármacos para endoscopia del sueño. No: Saber cuál refleja el sueño natural.
- **Licencia y derechos:** Derechos del editor. Aquí solo metadatos y resumen propio.
- **Estado de lectura:** Resumen PubMed revisado el 17/10/2026.

## Figuras

Figuras no revisadas: el texto completo no está en acceso abierto en PMC. [Ver el artículo](https://doi.org/10.1007/s11325-017-1465-x).

---

<!-- archivo: fuentes/articulos/2017-gpc-lactancia-materna-espana.md -->
# Estudio: Guía de Práctica Clínica sobre lactancia materna (Sistema Nacional de Salud, España)

- **ID:** GPCLACTANCIA2017
- **Autores, año y revista:** Grupo de trabajo de la Guía de Práctica Clínica sobre lactancia materna. Ministerio de Sanidad, Servicios Sociales e Igualdad; Agencia de Evaluación de Tecnologías Sanitarias del País Vasco-OSTEBA, 2017. Guías de Práctica Clínica en el SNS. Apartado 11.1.3, «Lactante con anquiloglosia» (pregunta 23).
- **DOI / PMID / URL:** PDF oficial: https://portal.guiasalud.es/wp-content/uploads/2018/12/GPC_560_Lactancia_Osteba_compl.pdf
- **Tipo de estudio:** Guía de práctica clínica oficial del Sistema Nacional de Salud, con GRADE.
- **Población y tamaño muestral:** Lactantes amamantados con anquiloglosia.
- **Definición diagnóstica y técnicas:** Revisión de la evidencia (sobre todo Francis 2015 y tres ensayos).
- **Criterio diagnóstico de anquiloglosia:** NO PROPONE NINGUNO. Entre las líneas de investigación pide «estudios que unifiquen los criterios diagnósticos» y los grados o tipos de anquiloglosia.
- **Variables de resultado:** Dolor del pezón, eficacia y duración de la lactancia, efectos adversos.
- **Resultados NUMÉRICOS verificados:** Evidencia de calidad global muy baja: las madres refieren menos dolor y mejor lactancia tras la frenotomía. Recomendaciones: antes de una frenotomía, historia de lactancia y evaluación de las tomas por expertos en lactancia; si los problemas persisten con apoyo, frenotomía por profesionales expertos.
- **Límites metodológicos / confusores:** Señala que no hay estudios que comparen frenotomía con apoyo experto a la lactancia, ni criterios uniformes de diagnóstico.
- **Hallazgos contrarios o no significativos:** Dos de tres ensayos no encontraron diferencias en dolor medidas por observador.
- **Conclusión que sí permite / que no permite:** Sí: Decir que la guía española de lactancia recomienda valorar la lactancia antes de operar y la frenotomía si persisten los problemas. No: Usarla para niños mayores, habla, sueño o maloclusión.
- **Licencia y derechos:** Documento público del Ministerio. Aquí solo resumen propio.
- **Estado de lectura:** Texto completo (PDF oficial) leído el 02/11/2026. Búsqueda de actualización del 02/11/2026.

## Figuras

Figuras no revisadas. [Ver el documento](https://portal.guiasalud.es/wp-content/uploads/2018/12/GPC_560_Lactancia_Osteba_compl.pdf).

---

<!-- archivo: fuentes/articulos/2017-herbst-voz-freddie-mercury.md -->
# Estudio: Freddie Mercury-acoustic analysis of speaking fundamental frequency, vibrato, and subharmonics

- **ID:** HERBST2017
- **Autores, año y revista:** Herbst CT; Hertegard S; Zangger-Borch D; Lindestad PÅ. Logoped Phoniatr Vocol 2017;42(1):29-38 (online abril de 2016).
- **DOI / PMID / URL:** DOI `10.3109/14015439.2016.1156737`; PMID `27079680`
- **Tipo de estudio:** Análisis acústico de grabaciones públicas más endoscopia de alta velocidad en un imitador.
- **Población y tamaño muestral:** Seis entrevistas, pistas de voz aisladas, 240 notas de 21 grabaciones a capela; un cantante de rock profesional.
- **Definición diagnóstica y técnicas:** Análisis perceptivo y cuantitativo; vídeo endoscópico a 4.132 imágenes por segundo.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA: el estudio no diagnostica anquiloglosia.
- **Variables de resultado:** Frecuencia fundamental al hablar, rango cantado, vibrato, subarmónicos.
- **Resultados NUMÉRICOS verificados:** Frecuencia al hablar 117,3 Hz, típica de barítono. Rango cantado 37 semitonos (F#2 a G5). Vibrato medio 7,0 Hz, rápido e irregular. Subarmónicos con patrón 3:1 de cuerdas vocales y bandas ventriculares en el imitador.
- **Límites metodológicos / confusores:** Grabaciones de archivo. El mecanismo de los subarmónicos se infiere de un imitador.
- **Hallazgos contrarios o no significativos:** No confirma las «cuatro octavas».
- **Conclusión que sí permite / que no permite:** Sí: Decir que lo distintivo de su voz se explica por laringe y técnica. El estudio no habla de los dientes. No: Sacar conclusiones sobre su boca o su frenillo.
- **Licencia y derechos:** Derechos del editor. Aquí solo metadatos y resumen propio.
- **Estado de lectura:** Resumen PubMed revisado el 17/10/2026.

## Figuras

Figuras no revisadas: el texto completo no está en acceso abierto en PMC. [Ver el artículo](https://doi.org/10.3109/14015439.2016.1156737).

---

<!-- archivo: fuentes/articulos/2017-kaditis-ers-apnea-lactantes.md -->
# Estudio: ERS statement on obstructive sleep disordered breathing in 1- to 23-month-old children

- **ID:** KADITIS2017
- **Autores, año y revista:** Kaditis AG; Alonso Alvarez ML; Boudewyns A; Abel F; Alexopoulos EI; Ersu R; Joosten K; Larramona H; Miano S; Narang I; Tan HL; Trang H; Tsaoussoglou M; Vandenbussche N; Villa MP; Van Waardenburg D; Weber S; Verhulst S. *Eur Respir J* 2017;50(6):1700985.
- **DOI / PMID / URL:** DOI `10.1183/13993003.00985-2017`; PMID `29217599`.
- **Tipo de estudio:** Declaración de un grupo de trabajo de la European Respiratory Society, con búsqueda sistemática y 159 artículos resumidos.
- **Población y tamaño muestral:** Lactantes de 1 a 23 meses.
- **Definición diagnóstica y técnicas:** Gravedad medida de forma objetiva, preferiblemente con polisomnografía; si no, poligrafía u oximetría nocturna.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA: declaración de apnea. Búsqueda en el texto completo el 05/11/2026: no aparecen «ankyloglossia» ni «tongue-tie». El frenillo lingual solo aparece en dos lactantes con síndrome de Beckwith-Wiedemann cuya apnea grave se resolvió tras sección del frenillo junto con resección central de la lengua o glosopexia anterior.
- **Variables de resultado:** No aplica (declaración).
- **Resultados NUMÉRICOS verificados:** Se benefician del tratamiento: obstrucción evidente de la vía aérea despiertos; estudio de sueño anormal con síntomas (por ejemplo ronquido) o con condiciones predisponentes (por ejemplo hipoplasia mandibular); y niños con enfermedades complejas. Los tratamientos más usados son la adenoamigdalectomía y la CPAP, junto con intervenciones dirigidas (por ejemplo supraglotoplastia en la laringomalacia o cánula nasofaríngea en la hipoplasia mandibular).
- **Límites metodológicos / confusores (solo los relevantes):** Gran parte de las recomendaciones se basa en la experiencia clínica del grupo de trabajo.
- **Otros resultados relevantes (si los hay):** Menciona las dificultades de alimentación como condición que puede coexistir. Una puesta al día de 2024 (Polytarchou, *Eur Respir Rev* 2024;33(171):230121) revisa lo publicado desde 2016 para este grupo de edad. En la secuencia de Pierre Robin propone, según gravedad, posición en prono, cánula nasofaríngea, aparato de ortodoncia, CPAP o glosopexia, y distracción mandibular o traqueostomía en los casos graves. Pide un equipo multidisciplinar que incluya ortodoncista.
- **Aportación del estudio:** Es la declaración europea de referencia para menores de 2 años.
- **Licencia y derechos:** Copyright de la ERS. Aquí solo resumen propio.
- **Estado de lectura:** Texto completo (PDF) leído por búsqueda de términos y en los apartados de tratamiento el 05/11/2026.

## Figuras

Figuras no revisadas. [Ver el artículo](https://doi.org/10.1183/13993003.00985-2017).

---

<!-- archivo: fuentes/articulos/2017-liu-avance-geniogloso-planificacion.md -->
# Estudio: An Accurate Method of Designing and Performing Individual-Specific Genioglossus Advancement

- **ID:** LIU2017A
- **Autores, año y revista:** Liu SY; Huon LK; Zaghi S et al.. Otolaryngol Head Neck Surg 2017.
- **DOI / PMID / URL:** DOI `10.1177/0194599816670366`; PMID `28045634`
- **Tipo de estudio:** Descripción de protocolo en 10 pacientes.
- **Población y tamaño muestral:** 10 pacientes.
- **Definición diagnóstica y técnicas:** Planificación virtual y guías intraoperatorias.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA: el estudio no diagnostica anquiloglosia.
- **Variables de resultado:** No aplica.
- **Resultados NUMÉRICOS verificados:** Sin cifras de resultado.
- **Límites metodológicos / confusores:** Descriptivo.
- **Hallazgos contrarios o no significativos:** No se describen en el resumen.
- **Conclusión que sí permite / que no permite:** Sí: Citar la técnica. No: Concluir eficacia.
- **Licencia y derechos:** Derechos del editor. Aquí solo metadatos y resumen propio.
- **Estado de lectura:** Resumen PubMed revisado el 17/10/2026.

## Figuras

Figuras no revisadas: el texto completo no está en acceso abierto en PMC. [Ver el artículo](https://doi.org/10.1177/0194599816670366).

---

<!-- archivo: fuentes/articulos/2017-noller-avance-mandibular-adultos.md -->
# Estudio: Mandibular advancement for adult obstructive sleep apnea: A systematic review and meta-analysis

- **ID:** NOLLER2017
- **Autores, año y revista:** Noller MW; Guilleminault C; Gouveia CJ et al.. J Craniomaxillofac Surg 2017.
- **DOI / PMID / URL:** DOI `10.1016/j.jcms.2017.10.006`; PMID `29113702`
- **Tipo de estudio:** Revisión sistemática (con metaanálisis si lo indica el título).
- **Población y tamaño muestral:** 11 estudios, 57 adultos con insuficiencia mandibular.
- **Definición diagnóstica y técnicas:** Búsqueda en varias bases de datos.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA: el estudio no diagnostica anquiloglosia.
- **Variables de resultado:** IAH, saturación mínima y somnolencia, salvo que se indique otra cosa.
- **Resultados NUMÉRICOS verificados:** IAH 45,9 → 6,2 (-87 %). Curación 75 % con avance >16 mm frente a 35 % con <16 mm (OR 5,5).
- **Límites metodológicos / confusores:** Estudios primarios pequeños y sobre todo series de casos. Zaghi es coautor.
- **Hallazgos contrarios o no significativos:** No se describen en el resumen.
- **Conclusión que sí permite / que no permite:** Sí: Decir que el avance mandibular aislado funciona en adultos con mandíbula insuficiente seleccionados. No: Generalizar.
- **Licencia y derechos:** Derechos del editor. Aquí solo metadatos y resumen propio.
- **Estado de lectura:** Resumen PubMed revisado el 17/10/2026.

## Figuras

Figuras no revisadas: el texto completo no está en acceso abierto en PMC. [Ver el artículo](https://doi.org/10.1016/j.jcms.2017.10.006).

---

<!-- archivo: fuentes/articulos/2017-oshea-cochrane-frenotomia.md -->
# Estudio: Frenotomy for tongue-tie in newborn infants (Cochrane)

- **ID:** OSHEA2017
- **Autores, año y revista:** O'Shea JE; Foster JP; O'Donnell CP; Breathnach D; Jacobs SE; Todd DA; Davis PG. Cochrane Database Syst Rev 2017;3:CD011065.
- **DOI / PMID / URL:** DOI `10.1002/14651858.CD011065.pub2`; PMID `28284020`; PMC6464654.
- **Tipo de estudio:** Revisión sistemática Cochrane de ensayos aleatorizados, con GRADE.
- **Población y tamaño muestral:** 5 ensayos, 302 lactantes menores de 3 meses con anquiloglosia.
- **Definición diagnóstica y técnicas:** Frenotomía frente a no frenotomía o procedimiento simulado.
- **Criterio diagnóstico de anquiloglosia:** MIXTO. La revisión define la anquiloglosia por el aspecto (frenillo cerca de la punta, corto, tenso y grueso) y planeaba subgrupos por gravedad con una herramienta validada como Hazelbaker. Qué usó cada ensayo: `PENDIENTE DE VERIFICAR`.
- **Variables de resultado:** Alimentación del lactante, dolor del pezón, duración de la lactancia, efectos adversos.
- **Resultados NUMÉRICOS verificados:** Alimentación: sin cambio en una escala de 10 puntos (2 estudios, n=155; diferencia de medias -0,1; IC 95 % -0,6 a 0,5); mejora en otro estudio (n=58; 3,5 puntos en una escala de 12). Dolor materno: menor en escala de 10 (3 estudios, n=212; -0,7; IC 95 % -1,4 a -0,1) y en otra escala de 50 (n=58; -8,6). Sin efectos adversos descritos.
- **Límites metodológicos / confusores:** Muestras pequeñas; solo dos estudios cegaron a madres y evaluadores; a casi todos los controles se les acabó haciendo la frenotomía. Ningún estudio midió lactancia a largo plazo.
- **Hallazgos contrarios o no significativos:** Sin efecto consistente sobre la alimentación del lactante.
- **Conclusión que sí permite / que no permite:** Sí: Decir que la frenotomía redujo el dolor del pezón a corto plazo, con certeza limitada. No: Decir que mejora la lactancia de forma demostrada, ni lo contrario.
- **Licencia y derechos:** Copyright de Cochrane; resumen en PMC. Aquí solo resumen propio.
- **Estado de lectura:** Resumen de PubMed revisado el 02/11/2026. Búsqueda de actualización del 02/11/2026.

## Figuras

Figuras no revisadas. [Ver el documento](https://doi.org/10.1002/14651858.CD011065.pub2).

---

<!-- archivo: fuentes/articulos/2017-pompeia-sistema-estomatognatico.md -->
# Estudio: Ankyloglossia and its influence on growth and development of the stomatognathic system

- **ID:** POMPEIA2017
- **Autores, año y revista:** Pompéia LE; Ilinsky RS; Ortolani CLF et al.. Rev Paul Pediatr 2017;35(2):216-221.
- **DOI / PMID / URL:** DOI `10.1590/1984-0462/;2017;35;2;00016`; PMID `28977337`; https://pmc.ncbi.nlm.nih.gov/articles/PMC5496731/
- **Tipo de estudio:** Revisión integradora.
- **Población y tamaño muestral:** 14 estudios clínicos de 51 encontrados.
- **Definición diagnóstica y técnicas:** MEDLINE, Google Scholar, LILACS, SciELO, ScienceDirect.
- **Criterio diagnóstico de anquiloglosia:** MIXTO entre estudios.
- **Variables de resultado:** No aplica.
- **Resultados NUMÉRICOS verificados:** La mitad de los estudios describe frenotomía segura y eficaz para la lactancia; 4 de 14 describen efecto negativo sobre la musculatura orofacial.
- **Límites metodológicos / confusores:** Revisión no sistemática.
- **Hallazgos contrarios o no significativos:** No hay unanimidad sobre la cirugía precoz.
- **Conclusión que sí permite / que no permite:** Sí: Citar el consenso de autores sobre efectos funcionales. No: Usarlo como prueba de crecimiento.
- **Licencia y derechos:** Acceso abierto en PMC. Licencia PENDIENTE DE VERIFICAR.
- **Estado de lectura:** Resumen PubMed y texto completo revisados el 17/10/2026.

## Figuras

Licencia del artículo: Creative Commons (tipo no especificado en el XML). No se copian imágenes.

El artículo no tiene figuras en la versión de PMC. [Artículo](https://pmc.ncbi.nlm.nih.gov/articles/PMC5496731/).

---

<!-- archivo: fuentes/articulos/2017-song-genioplastia-tuberculo-geniano.md -->
# Estudio: Genial tubercle advancement and genioplasty for obstructive sleep apnea: A systematic review and meta-analysis

- **ID:** SONG2017
- **Autores, año y revista:** Song SA; Chang ET; Certal V et al.. Laryngoscope 2017;127:984-992.
- **DOI / PMID / URL:** DOI `10.1002/lary.26218`; PMID `27546467`
- **Tipo de estudio:** Revisión sistemática (con metaanálisis si lo indica el título).
- **Población y tamaño muestral:** 13 estudios, 111 pacientes.
- **Definición diagnóstica y técnicas:** Búsqueda en varias bases de datos.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA: el estudio no diagnostica anquiloglosia.
- **Variables de resultado:** IAH, saturación mínima y somnolencia, salvo que se indique otra cosa.
- **Resultados NUMÉRICOS verificados:** Genioplastia estándar: IAH -43,8 %. Avance del tubérculo geniano: -45,7 %. Con cirugía de hioides: -55,7 %. La genioplastia modificada aumentó el IAH un 37,3 %.
- **Límites metodológicos / confusores:** Estudios primarios pequeños y sobre todo series de casos. Zaghi es coautor.
- **Hallazgos contrarios o no significativos:** No se describen en el resumen.
- **Conclusión que sí permite / que no permite:** Sí: Decir que estas cirugías reducen la apnea en series pequeñas. No: Recomendarlas con seguridad.
- **Licencia y derechos:** Derechos del editor. Aquí solo metadatos y resumen propio.
- **Estado de lectura:** Resumen PubMed revisado el 17/10/2026.

## Figuras

Figuras no revisadas: el texto completo no está en acceso abierto en PMC. [Ver el artículo](https://doi.org/10.1002/lary.26218).

---

<!-- archivo: fuentes/articulos/2017-yoon-maxilar.md -->
# Yoon et al. (2017) — Ankyloglossia as a risk factor for maxillary hypoplasia and soft palate elongation

- DOI: `10.1111/ocr.12206`; PMID: `28994495`.
- Diseño: estudio transversal en 302 pacientes de una consulta ortodóncica.
- Objetivo: asociaciones entre movilidad lingual y rasgos maxilofaciales.
- Limitación principal: la asociación transversal no distingue qué factor apareció antes ni prueba un mecanismo causal.
- Criterio diagnóstico de anquiloglosia: MIXTO. Movilidad funcional con TRMR y longitud con la lengua libre de Kotlow (resumen PubMed revisado el 17/10/2026). Ambas medidas se asociaron a arcada maxilar estrecha y paladar blando largo.
- Complemento desde el texto completo (17/10/2026): confirma que la movilidad se gradúa con TRMR (grado 1 >80 %, 2 de 50 a 80 %, 3 <50 %, 4 <25 %) y que se mide también la lengua libre de Kotlow. La cifra del «7,6 % de varianza» que circula en el corpus de Zaghi no se ha localizado en el PDF: `PENDIENTE DE VERIFICAR`.
- Estado: metadatos y resumen verificados; revisar íntegramente criterios diagnósticos, variables y ajustes.

## Figuras

Las leyendas de las figuras no se han podido extraer del texto completo: `PENDIENTE DE VERIFICAR`. [Ver el artículo](https://doi.org/10.1111/ocr.12206).

---

<!-- archivo: fuentes/articulos/2017-yoon-trmr-1052.md -->
# Estudio: Toward a functional definition of ankyloglossia: validating current grading scales for lingual frenulum length and tongue mobility in 1052 subjects

- **ID:** YOON2017SB
- **Autores, año y revista:** Yoon A; Zaghi S; Weitzman R et al.. Sleep Breath 2017;21(3):767-775.
- **DOI / PMID / URL:** DOI `10.1007/s11325-016-1452-7`; PMID `28097623`
- **Tipo de estudio:** Cohorte prospectiva de pacientes consecutivos durante 3 meses.
- **Población y tamaño muestral:** 1.052 pacientes consecutivos.
- **Definición diagnóstica y técnicas:** Apertura máxima (MIO), apertura con la punta en la papila incisiva (MOTTIP), lengua libre de Kotlow, anquiloglosia grave. Derivadas: TRMD (MIO menos MOTTIP) y TRMR (MOTTIP/MIO).
- **Criterio diagnóstico de anquiloglosia:** FUNCIONAL. Es el estudio que propone la escala TRMR: grado 1 >80 %, grado 2 50-80 %, grado 3 <50 %, grado 4 <25 %.
- **Variables de resultado:** Dependencia de cada medida respecto a edad, talla y apertura.
- **Resultados NUMÉRICOS verificados:** La MIO depende de edad y talla; MOTTIP y TRMD dependen de la MIO. La lengua libre de Kotlow es independiente. El TRMR es la única medida independiente de movilidad asociada directamente a restricción funcional.
- **Límites metodológicos / confusores:** Validación hecha por el grupo que propone la escala. El resumen no da fiabilidad entre observadores: PENDIENTE DE VERIFICAR.
- **Hallazgos contrarios o no significativos:** No se describen en el resumen.
- **Conclusión que sí permite / que no permite:** Sí: Usar el TRMR como cribado de movilidad lingual y seguir el tratamiento con una escala objetiva. No: Afirmar que un TRMR bajo se deba siempre al frenillo, ni que prediga síntomas.
- **Licencia y derechos:** Derechos del editor. Aquí solo metadatos y resumen propio.
- **Estado de lectura:** Resumen PubMed revisado el 17/10/2026. En notas de trabajo previas figuraba como candidato no confirmado; el resumen confirma que es la validación de las escalas en 1.052 sujetos.

## Figuras

Figuras no revisadas: el texto completo no está en acceso abierto en PMC. [Ver el artículo](https://doi.org/10.1007/s11325-016-1452-7).

---

<!-- archivo: fuentes/articulos/2018-camacho-miofuncional-ronquido.md -->
# Estudio: Oropharyngeal and tongue exercises (myofunctional therapy) for snoring: a systematic review and meta-analysis

- **ID:** CAMACHO2018
- **Autores, año y revista:** Camacho M; Guilleminault C; Wei JM et al.. Eur Arch Otorhinolaryngol 2018.
- **DOI / PMID / URL:** DOI `10.1007/s00405-017-4848-5`; PMID `29275425`
- **Tipo de estudio:** Revisión sistemática (con metaanálisis si lo indica el título).
- **Población y tamaño muestral:** 9 estudios, 211 adultos.
- **Definición diagnóstica y técnicas:** Búsqueda en varias bases de datos.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA: el estudio no diagnostica anquiloglosia.
- **Variables de resultado:** IAH, saturación mínima y somnolencia, salvo que se indique otra cosa.
- **Resultados NUMÉRICOS verificados:** Intensidad del ronquido -51 % (EVA 8,2 → 4,0). Berlín -36 %. Tiempo roncando 26,3 → 18,1 % (-31 %).
- **Límites metodológicos / confusores:** Estudios primarios pequeños y sobre todo series de casos. Zaghi es coautor.
- **Hallazgos contrarios o no significativos:** No se describen en el resumen.
- **Conclusión que sí permite / que no permite:** Sí: Decir que la terapia miofuncional reduce el ronquido en adultos. No: Extrapolar a niños.
- **Licencia y derechos:** Derechos del editor. Aquí solo metadatos y resumen propio.
- **Estado de lectura:** Resumen PubMed revisado el 17/10/2026.

## Figuras

Figuras no revisadas: el texto completo no está en acceso abierto en PMC. [Ver el artículo](https://doi.org/10.1007/s00405-017-4848-5).

---

<!-- archivo: fuentes/articulos/2018-gouveia-tendencias-publicacion-apnea.md -->
# Estudio: Publication trends and levels of evidence in obstructive sleep apnea literature

- **ID:** GOUVEIA2018
- **Autores, año y revista:** Gouveia CJ; Zaghi S; Awad M et al.. Laryngoscope 2018.
- **DOI / PMID / URL:** DOI `10.1002/lary.27075`; PMID `29314068`
- **Tipo de estudio:** Análisis bibliométrico.
- **Población y tamaño muestral:** 708 artículos de 2006, 2011 y 2016.
- **Definición diagnóstica y técnicas:** Nivel de evidencia y financiación.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA: el estudio no diagnostica anquiloglosia.
- **Variables de resultado:** Nivel de evidencia.
- **Resultados NUMÉRICOS verificados:** Sin mejora del nivel de evidencia con el tiempo; la cirugía del sueño estancada en esas revistas.
- **Límites metodológicos / confusores:** Cuatro revistas.
- **Hallazgos contrarios o no significativos:** No se describen en el resumen.
- **Conclusión que sí permite / que no permite:** Sí: Decir que la evidencia en apnea es modesta y no mejora. No: Generalizar a toda la literatura.
- **Licencia y derechos:** Derechos del editor. Aquí solo metadatos y resumen propio.
- **Estado de lectura:** Resumen PubMed revisado el 17/10/2026.

## Figuras

Figuras no revisadas: el texto completo no está en acceso abierto en PMC. [Ver el artículo](https://doi.org/10.1002/lary.27075).

---

<!-- archivo: fuentes/articulos/2018-neighbors-vitamina-d-apnea.md -->
# Estudio: Vitamin D and obstructive sleep apnea: a systematic review and meta-analysis

- **ID:** NEIGHBORS2018
- **Autores, año y revista:** Neighbors CLP; Noller MW; Song SA et al.. Sleep Med 2018.
- **DOI / PMID / URL:** DOI `10.1016/j.sleep.2017.10.016`; PMID `29482804`
- **Tipo de estudio:** Revisión sistemática (con metaanálisis si lo indica el título).
- **Población y tamaño muestral:** 14 estudios, 4.937 personas.
- **Definición diagnóstica y técnicas:** Búsqueda en varias bases de datos.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA: el estudio no diagnostica anquiloglosia.
- **Variables de resultado:** IAH, saturación mínima y somnolencia, salvo que se indique otra cosa.
- **Resultados NUMÉRICOS verificados:** Vitamina D más baja cuanto más grave la apnea: -2,7 % leve, -10,1 % moderada, -17,4 % grave.
- **Límites metodológicos / confusores:** Estudios primarios pequeños y sobre todo series de casos. Zaghi es coautor.
- **Hallazgos contrarios o no significativos:** No se describen en el resumen.
- **Conclusión que sí permite / que no permite:** Sí: Decir que la vitamina D es más baja en la apnea. No: Saber la dirección: el IMC podría explicarlo.
- **Licencia y derechos:** Derechos del editor. Aquí solo metadatos y resumen propio.
- **Estado de lectura:** Resumen PubMed revisado el 17/10/2026.

## Figuras

Figuras no revisadas: el texto completo no está en acceso abierto en PMC. [Ver el artículo](https://doi.org/10.1016/j.sleep.2017.10.016).

---

<!-- archivo: fuentes/articulos/2018-noller-avance-mandibular-ninos.md -->
# Estudio: Mandibular advancement for pediatric obstructive sleep apnea: A systematic review and meta-analysis

- **ID:** NOLLER2018
- **Autores, año y revista:** Noller MW; Guilleminault C; Gouveia CJ et al.. J Craniomaxillofac Surg 2018.
- **DOI / PMID / URL:** DOI `10.1016/j.jcms.2018.04.027`; PMID `29898824`
- **Tipo de estudio:** Revisión sistemática (con metaanálisis si lo indica el título).
- **Población y tamaño muestral:** 37 estudios, 376 niños (media 1,5 años) con insuficiencia mandibular.
- **Definición diagnóstica y técnicas:** Búsqueda en varias bases de datos.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA: el estudio no diagnostica anquiloglosia.
- **Variables de resultado:** IAH, saturación mínima y somnolencia, salvo que se indique otra cosa.
- **Resultados NUMÉRICOS verificados:** IAH 41,1 → 4,5 (-89,1 %). Éxito 73,4 % y curación 25,5 % con datos individuales.
- **Límites metodológicos / confusores:** Estudios primarios pequeños y sobre todo series de casos. Zaghi es coautor.
- **Hallazgos contrarios o no significativos:** No se describen en el resumen.
- **Conclusión que sí permite / que no permite:** Sí: Decir que el avance o la distracción mandibular mejoran mucho la apnea en niños con mandíbula insuficiente. No: Extenderlo a niños sin esa anomalía.
- **Licencia y derechos:** Derechos del editor. Aquí solo metadatos y resumen propio.
- **Estado de lectura:** Resumen PubMed revisado el 17/10/2026.

## Figuras

Figuras no revisadas: el texto completo no está en acceso abierto en PMC. [Ver el artículo](https://doi.org/10.1016/j.jcms.2018.04.027).

---

<!-- archivo: fuentes/articulos/2018-patel-neuromuscular-paladar.md -->
# Estudio: Neuromuscular function of the soft palate and uvula in snoring and obstructive sleep apnea: A systematic review

- **ID:** PATEL2018
- **Autores, año y revista:** Patel JA; Ray BJ; Fernandez-Salvador C et al.. Am J Otolaryngol 2018.
- **DOI / PMID / URL:** DOI `10.1016/j.amjoto.2018.03.006`; PMID `29525140`
- **Tipo de estudio:** Revisión sistemática (con metaanálisis si lo indica el título).
- **Población y tamaño muestral:** 31 estudios.
- **Definición diagnóstica y técnicas:** Búsqueda en varias bases de datos.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA: el estudio no diagnostica anquiloglosia.
- **Variables de resultado:** IAH, saturación mínima y somnolencia, salvo que se indique otra cosa.
- **Resultados NUMÉRICOS verificados:** Cambios inflamatorios, musculares y neuropáticos del paladar blando que empeoran con la gravedad.
- **Límites metodológicos / confusores:** Estudios primarios pequeños y sobre todo series de casos. Zaghi es coautor.
- **Hallazgos contrarios o no significativos:** No se describen en el resumen.
- **Conclusión que sí permite / que no permite:** Sí: Plantear una neuropatía del paladar en la progresión de ronquido a apnea. No: Afirmar causa.
- **Licencia y derechos:** Derechos del editor. Aquí solo metadatos y resumen propio.
- **Estado de lectura:** Resumen PubMed revisado el 17/10/2026.

## Figuras

Figuras no revisadas: el texto completo no está en acceso abierto en PMC. [Ver el artículo](https://doi.org/10.1016/j.amjoto.2018.03.006).

---

<!-- archivo: fuentes/articulos/2018-scapuccin-ciclo-nasal.md -->
# Estudio: Integrating the Divided Nasal Cannula Into Routine Polysomnography to Assess Nasal Cycle: Feasibility and Effectiveness

- **ID:** SCAPUCCIN2018
- **Autores, año y revista:** Scapuccin M; Schneider L; Rashid N et al.. J Clin Sleep Med 2018.
- **DOI / PMID / URL:** DOI `10.5664/jcsm.7062`; PMID `29609709`
- **Tipo de estudio:** Cohorte prospectiva piloto.
- **Población y tamaño muestral:** 28 pacientes.
- **Definición diagnóstica y técnicas:** Cánula nasal dividida en la polisomnografía.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA: el estudio no diagnostica anquiloglosia.
- **Variables de resultado:** Ciclo nasal.
- **Resultados NUMÉRICOS verificados:** 89 % mostró cambios de ciclo nasal; duración media 2,5 h.
- **Límites metodológicos / confusores:** Piloto.
- **Hallazgos contrarios o no significativos:** No se describen en el resumen.
- **Conclusión que sí permite / que no permite:** Sí: Citar la viabilidad de medir el ciclo nasal durante el sueño. No: Concluir efectos clínicos.
- **Licencia y derechos:** Derechos del editor. Aquí solo metadatos y resumen propio.
- **Estado de lectura:** Resumen PubMed revisado el 17/10/2026.

## Figuras

Figuras no revisadas: el texto completo no está en acceso abierto en PMC. [Ver el artículo](https://doi.org/10.5664/jcsm.7062).

---

<!-- archivo: fuentes/articulos/2018-torre-laringoscopia-despierto.md -->
# Estudio: Hypopharyngeal evaluation in obstructive sleep apnea with awake flexible laryngoscopy: Validation and updates to Cormack-Lehane and Modified Cormack-Lehane scoring systems

- **ID:** TORRE2018
- **Autores, año y revista:** Torre C; Zaghi S; Camacho M et al.. Clin Otolaryngol 2018.
- **DOI / PMID / URL:** DOI `10.1111/coa.13054`; PMID `29280292`
- **Tipo de estudio:** Validación con base de datos prospectiva.
- **Población y tamaño muestral:** Imágenes de 90 pacientes; 6 evaluadores.
- **Definición diagnóstica y técnicas:** Escalas de Cormack-Lehane.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA: el estudio no diagnostica anquiloglosia.
- **Variables de resultado:** Fiabilidad entre observadores.
- **Resultados NUMÉRICOS verificados:** Proponen una escala de cuerdas vocales de 5 grados.
- **Límites metodológicos / confusores:** Imágenes fijas.
- **Hallazgos contrarios o no significativos:** No se describen en el resumen.
- **Conclusión que sí permite / que no permite:** Sí: Citar la escala propuesta. No: Concluir sobre tratamiento.
- **Licencia y derechos:** Derechos del editor. Aquí solo metadatos y resumen propio.
- **Estado de lectura:** Resumen PubMed revisado el 17/10/2026.

## Figuras

Figuras no revisadas: el texto completo no está en acceso abierto en PMC. [Ver el artículo](https://doi.org/10.1111/coa.13054).

---

<!-- archivo: fuentes/articulos/2019-awad-tendencias-cirugia-esqueletica.md -->
# Estudio: Changing practice: Trends in skeletal surgery for obstructive sleep apnea

- **ID:** AWAD2019
- **Autores, año y revista:** Awad M; Gouveia C; Zaghi S et al.. J Craniomaxillofac Surg 2019.
- **DOI / PMID / URL:** DOI `10.1016/j.jcms.2018.11.005`; PMID `31182256`
- **Tipo de estudio:** Revisión sistemática (con metaanálisis si lo indica el título).
- **Población y tamaño muestral:** 414 estudios incluidos de 1.875.
- **Definición diagnóstica y técnicas:** Búsqueda en varias bases de datos.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA: el estudio no diagnostica anquiloglosia.
- **Variables de resultado:** IAH, saturación mínima y somnolencia, salvo que se indique otra cosa.
- **Resultados NUMÉRICOS verificados:** Aumentan las publicaciones de expansión maxilar y MMA; bajan las de hioides y genioplastia.
- **Límites metodológicos / confusores:** Estudios primarios pequeños y sobre todo series de casos. Zaghi es coautor.
- **Hallazgos contrarios o no significativos:** No se describen en el resumen.
- **Conclusión que sí permite / que no permite:** Sí: Describir tendencias de la cirugía esquelética de la apnea. No: Concluir eficacia.
- **Licencia y derechos:** Derechos del editor. Aquí solo metadatos y resumen propio.
- **Estado de lectura:** Resumen PubMed revisado el 17/10/2026.

## Figuras

Figuras no revisadas: el texto completo no está en acceso abierto en PMC. [Ver el artículo](https://doi.org/10.1016/j.jcms.2018.11.005).

---

<!-- archivo: fuentes/articulos/2019-behrents-aao-apnea-ortodoncia.md -->
# Estudio: Obstructive sleep apnea and orthodontics: An American Association of Orthodontists White Paper

- **ID:** BEHRENTS2019
- **Autores, año y revista:** Behrents RG; Shelgikar AV; Conley RS; Flores-Mir C; Hans M; Levine M; McNamara JA; Palomo JM; Pliska B; Stockstill JW; Wise J; Murphy S; Nagel NJ; Hittner J. *Am J Orthod Dentofacial Orthop* 2019;156(1):13-28.e1.
- **DOI / PMID / URL:** DOI `10.1016/j.ajodo.2019.04.009`; PMID `31256826`; versión de la AAO (modificada el 15/03/2019): https://www2.aaoinfo.org/wp-content/uploads/2019/03/sleep-apnea-white-paper-amended-March-2019.pdf
- **Tipo de estudio:** Documento de posición («white paper») de la American Association of Orthodontists, escrito por un grupo de expertos en medicina del sueño y medicina dental del sueño. PubMed lo clasifica como declaración de consenso. Actualizado en 2026 (Palomo 2026).
- **Población y tamaño muestral:** Niños y adultos.
- **Definición diagnóstica y técnicas:** Diagnóstico de apnea por el médico; el ortodoncista criba y deriva.
- **Criterio diagnóstico de anquiloglosia:** NO PROPONE NINGUNO. En el apartado «Frenectomy» dice que sigue habiendo incertidumbre sobre qué grado de inserción del frenillo altera la forma o la función salvo en las formas más graves, y cita la escala funcional de movilidad lingual de 4 grados de Yoon 2017.
- **Variables de resultado:** No aplica (documento de posición).
- **Resultados NUMÉRICOS verificados:** Sin cifras propias. Frenectomía: la considera un tratamiento adecuado para problemas de habla y masticación, pero no apoyada como tratamiento para prevenir la aparición de apnea. Cita que en Yoon 2017 las lenguas más restringidas tenían menor anchura intercanina del maxilar y paladar blando más largo, y dice que la relación entre movilidad lingual y función de la vía aérea es compleja y que hay que estudiar la función de la vía aérea durante el sueño en relación con la movilidad lingual. Extracciones: «Conventional orthodontic treatment never has been proven to be an etiologic factor in the development of obstructive sleep apnea».
- **Límites metodológicos / confusores (solo los relevantes):** Revisión narrativa sin método sistemático descrito.
- **Otros resultados relevantes (si los hay):** Sobre extracciones cita un estudio de más de 2.700 adultos sin cuatro premolares, sin más apnea que un grupo emparejado. Dice que una vía aérea estrecha no produce apnea por sí sola y que lo determinante es que los músculos no compensen, y pide estudiar la función de la vía aérea en lugar de solo sus dimensiones.
- **Aportación del estudio:** Fue el documento de referencia de la ortodoncia estadounidense sobre apnea hasta 2026.
- **Licencia y derechos:** Copyright de la AAO / Elsevier. Aquí solo resumen propio.
- **Estado de lectura:** Texto completo de la versión de la AAO (PDF modificado en marzo de 2019) leído por búsqueda de términos y en los apartados de frenectomía y extracciones el 05/11/2026. No se ha comparado con la versión publicada en la revista.

## Figuras

Figuras no revisadas. [Ver el documento](https://doi.org/10.1016/j.ajodo.2019.04.009).

---

<!-- archivo: fuentes/articulos/2019-camacho-mma-largo-plazo.md -->
# Estudio: Long-term Results for Maxillomandibular Advancement to Treat Obstructive Sleep Apnea: A Meta-analysis

- **ID:** CAMACHO2019
- **Autores, año y revista:** Camacho M; Noller MW; Del Do M et al.. Otolaryngol Head Neck Surg 2019.
- **DOI / PMID / URL:** DOI `10.1177/0194599818815158`; PMID `30598047`
- **Tipo de estudio:** Revisión sistemática (con metaanálisis si lo indica el título).
- **Población y tamaño muestral:** 6 estudios, 120 pacientes.
- **Definición diagnóstica y técnicas:** Búsqueda en varias bases de datos.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA: el estudio no diagnostica anquiloglosia.
- **Variables de resultado:** IAH, saturación mínima y somnolencia, salvo que se indique otra cosa.
- **Resultados NUMÉRICOS verificados:** IAH a 1-4 años 48,3 → 8,4; a 4-8 años 65,8 → 7,7; a ≥8 años 53,2 → 23,1 (vuelve a apnea moderada).
- **Límites metodológicos / confusores:** Estudios primarios pequeños y sobre todo series de casos. Zaghi es coautor.
- **Hallazgos contrarios o no significativos:** No se describen en el resumen.
- **Conclusión que sí permite / que no permite:** Sí: Decir que el MMA mantiene la mejoría años después, aunque a muy largo plazo el IAH sube. No: Generalizar con tan pocos pacientes.
- **Licencia y derechos:** Derechos del editor. Aquí solo metadatos y resumen propio.
- **Estado de lectura:** Resumen PubMed revisado el 17/10/2026.

## Figuras

Figuras no revisadas: el texto completo no está en acceso abierto en PMC. [Ver el artículo](https://doi.org/10.1177/0194599818815158).

---

<!-- archivo: fuentes/articulos/2019-ghorbanyjavadpour-belleza-perfil.md -->
# Estudio: Factors associated with the beauty of soft-tissue profile

- **ID:** GHORBANY2019
- **Autores, año y revista:** Ghorbanyjavadpour F; Rakhshan V. Am J Orthod Dentofacial Orthop 2019;155(6):832-843.
- **DOI / PMID / URL:** DOI `10.1016/j.ajodo.2018.07.020`; PMID `31153504`
- **Tipo de estudio:** Transversal con valoración por legos.
- **Población y tamaño muestral:** 70 iraníes con clase I y cara equilibrada; 10 evaluadores.
- **Definición diagnóstica y técnicas:** Siluetas de perfil y medidas de Holdaway, Ricketts, Merrifield, Epker y Legan-Burstone.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA: el estudio no diagnostica anquiloglosia.
- **Variables de resultado:** Puntuación de belleza del perfil.
- **Resultados NUMÉRICOS verificados:** Se asociaron a más belleza, entre otros, el ángulo nasolabial, el ángulo Z, el labio superior respecto a la línea E y el ángulo de convexidad facial (p≤0,05).
- **Límites metodológicos / confusores:** Una población y evaluadores legos.
- **Hallazgos contrarios o no significativos:** Sexo y edad no influyeron.
- **Conclusión que sí permite / que no permite:** Sí: Describir qué perfiles se juzgan más atractivos en esa población. No: Generalizar a otras poblaciones.
- **Licencia y derechos:** Derechos del editor. Aquí solo metadatos y resumen propio.
- **Estado de lectura:** Resumen PubMed y texto completo revisados el 17/10/2026.

## Figuras

Licencia: derechos del editor (no se copian imágenes). Leyendas leídas en el texto completo; puede haber más figuras que las listadas.

- **Figura 2.** Análisis de Epker. [Ver en el artículo](https://doi.org/10.1016/j.ajodo.2018.07.020), figura 2.
- **Figura 3.** Análisis de Legan-Burstone. [Ver en el artículo](https://doi.org/10.1016/j.ajodo.2018.07.020), figura 3.
- **Figura 4.** Siluetas del grupo atractivo. [Ver en el artículo](https://doi.org/10.1016/j.ajodo.2018.07.020), figura 4.

---

<!-- archivo: fuentes/articulos/2019-govardhan-frenuloplastia-caso.md -->
# Estudio: Lingual and Maxillary Labial Frenuloplasty with Myofunctional Therapy as a Treatment for Mouth Breathing and Snoring

- **ID:** GOVARDHAN2019
- **Autores, año y revista:** Govardhan C; Murdock J; Norouz-Knutsen L et al.. Case Rep Otolaryngol 2019.
- **DOI / PMID / URL:** DOI `10.1155/2019/3408053`; PMID `31001444`
- **Tipo de estudio:** Caso clínico.
- **Población y tamaño muestral:** Una niña de 3 años con respiración oral, ronquido y disfagia de fase oral.
- **Definición diagnóstica y técnicas:** Frenuloplastia lingual y labial más terapia miofuncional.
- **Criterio diagnóstico de anquiloglosia:** Escala usada: PENDIENTE DE VERIFICAR (no consta en el resumen).
- **Variables de resultado:** Ronquido, respiración oral, adherencia a la terapia.
- **Resultados NUMÉRICOS verificados:** A los 4 días dejó de roncar y de respirar con la boca abierta.
- **Límites metodológicos / confusores:** Un caso, del entorno de Zaghi.
- **Hallazgos contrarios o no significativos:** No se describen en el resumen.
- **Conclusión que sí permite / que no permite:** Sí: Ilustrar la frenuloplastia como complemento de la terapia miofuncional. No: Generalizar.
- **Licencia y derechos:** Derechos del editor. Aquí solo metadatos y resumen propio.
- **Estado de lectura:** Resumen PubMed revisado el 17/10/2026.

## Figuras

Figuras no revisadas: el texto completo no está en acceso abierto en PMC. [Ver el artículo](https://doi.org/10.1155/2019/3408053).

---

<!-- archivo: fuentes/articulos/2019-mills-fascia-neonatal.md -->
# Estudio: Defining the anatomy of the neonatal lingual frenulum

- **ID:** MILLS2019N
- **Autores, año y revista:** Mills N; Keough N; Geddes DT; Pransky SM; Mirjalili SA. *Clinical Anatomy* 2019;32(6):824–835.
- **DOI / PMID / URL:** DOI `10.1002/ca.23410`; PMID `31116462`; [versión íntegra abierta en Wiley](https://onlinelibrary.wiley.com/doi/full/10.1002/ca.23410); [repositorio institucional](https://repository.up.ac.za/items/4cec1b35-88fd-45e9-94e6-367f1ac96efa).
- **Tipo de estudio:** Investigación anatómica descriptiva por microdisección de cadáveres infantiles, **no ensayo clínico ni comparación de niños con y sin anquiloglosia funcional**.
- **Población y tamaño muestral:** **4 cadáveres de recién nacidos prematuros** con conservación de tejidos frescos para la disección. Muestra pequeña, sin sujetos vivos y sin seguimiento de crecimiento.
- **Definición diagnóstica y técnicas:** Disección por capas de la lengua, mucosa y fascia del suelo de boca, con movilización pasiva y elevación/retracción lingual; comparación conceptual con el modelo anatómico adulto. No se aplica TRMR, Kotlow ni ninguna escala diagnóstica clínica a pacientes.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA: estudio de anatomía neonatal; **describe estructura normal y su variación**, no clasifica niños vivos según restricción funcional.
- **Variables de resultado:** Continuidad de mucosa/fascia, pliegue lingual visible con elevación, inserciones, variación de transparencia, relaciones del geniogloso y trayecto de ramas nerviosas.
- **Resultados NUMÉRICOS verificados:** **n=4 especímenes**. El pliegue del frenillo aparece dinámicamente con la elevación y/o retracción de la lengua y resulta de la mucosa oral y de la fascia subyacente; el geniogloso puede elevarse con el pliegue; las ramas del nervio lingual se sitúan superficialmente en la cara ventral de la lengua, adyacentes a la fascia. No se midieron tasas de maloclusión, fuerzas mandibulares, tiempo de crecimiento ni eficacia de frenotomía.
- **Límites metodológicos / confusores:** Solo 4 cadáveres prematuros (no extrapolar mecánica y dimensiones a niños de distintas edades), disección pasiva post mortem, sin medición de tensión/fuerza in vivo ni validación de criterios diagnósticos funcionales; la interpretación de la seguridad quirúrgica deriva de proximidad anatómica, no de una cohorte de complicaciones.
- **Hallazgos contrarios o no significativos:** Los autores señalan variabilidad normal de apariencia del frenillo y falta de una relación anatómica aislada validada con limitación funcional; la presencia/aspecto del pliegue por sí mismos **no son diagnósticos de anquiloglosia patológica**. No existe aquí contraste clínico positivo/negativo sobre crecimiento.
- **Conclusión que sí permite / que no permite:** **Sí:** el frenillo neonatal forma un pliegue dinámico de mucosa y fascia, con relaciones anatómicas relevantes para la disección quirúrgica. **No:** afirmar que una fascia lingual determinada retrae la mandíbula, altera crecimiento óseo, causa apnea o exige cirugía; el estudio no evaluó nada de ello.
- **Licencia y derechos:** Texto abierto publicado bajo **CC BY 4.0**, según la versión de autor/editorial. Ficha redactada como síntesis; no se incorporan fotos, tablas ni PDF.
- **Estado de lectura:** Texto íntegro HTML de Wiley y resumen PubMed consultados el **03/11/2026**, incluidos métodos, resultados de los cuatro especímenes y discusión del significado de las clasificaciones anatómicas. Figuras disponibles en el editor, no reproducidas.

## Figuras

Disponibles en el [original Wiley](https://onlinelibrary.wiley.com/doi/full/10.1002/ca.23410); no se almacenan copias locales ni imágenes de muestras de cadáver.

---

<!-- archivo: fuentes/articulos/2019-mills-fascia.md -->
# Mills et al. (2019) — What is a tongue tie? Defining the anatomy of the in-situ lingual frenulum

- DOI: `10.1002/ca.23343`; acceso abierto: https://pmc.ncbi.nlm.nih.gov/articles/PMC6850428/
- Tipo: microdisección de 9 cadáveres adultos.
- Hallazgo: frenillo formado por el pliegue de una fascia del suelo de la boca anclada en el arco interno mandibular y continua con tejido conjuntivo ventral lingual.
- Relevancia: fundamento anatómico de la hipótesis H-001.
- No sirve para: demostrar que esa fascia desplaza la mandíbula hacia atrás en reposo ni explicar cambios clínicos tras frenotomía.
- Criterio diagnóstico de anquiloglosia: NO APLICA: estudio anatómico o biomecánico, no diagnostica anquiloglosia.
- Complemento desde el texto completo (17/10/2026): el PDF coincide con la versión abierta de PMC usada en esta ficha.
- Estado: texto primario y hallazgos principales revisados; ficha biomecánica detallada pendiente.

## Figuras

Licencia del artículo: CC BY-NC-ND 4.0 (no permite copiar aquí). Figuras en PubMed Central (PMC6850428).

- **Figura 1.** Inserción mandibular de la fascia del suelo de boca, con y sin mucosa, en cadáver. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC6850428/figure/ca23343-fig-0001/).
- **Figura 2.** Variaciones de grosor y altura de la inserción mandibular de la fascia. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC6850428/figure/ca23343-fig-0002/).
- **Figura 3.** Continuidad de la fascia por los lados de la lengua. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC6850428/figure/ca23343-fig-0003/).
- **Figura 4.** Al elevar la lengua la fascia se tensa y forma el pliegue del frenillo. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC6850428/figure/ca23343-fig-0004/).
- **Figura 5.** «Anatomía de superficie» del frenillo, ejemplo 1. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC6850428/figure/ca23343-fig-0005/).
- **Figura 6.** Inserción mandibular de la fascia elevada en la línea media (aspecto de «torre Eiffel»). [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC6850428/figure/ca23343-fig-0006/).
- **Figura 7.** Inserción mandibular no elevada. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC6850428/figure/ca23343-fig-0007/).
- **Figura 8.** «Anatomía de superficie» del frenillo, ejemplo 2. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC6850428/figure/ca23343-fig-0008/).
- **Figura 9.** Morfologías del frenillo bajo tensión: transparente, opaco, con geniogloso. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC6850428/figure/ca23343-fig-0009/).
- **Figura 10.** El geniogloso suspendido de la fascia del suelo de boca (cuatro piezas). [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC6850428/figure/ca23343-fig-0010/).
- **Figura 11.** Esquema: concepto clásico de «banda submucosa» frente al pliegue fascial dinámico. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC6850428/figure/ca23343-fig-0011/).
- **Figura 12.** Esquema coronal de la fascia del suelo de boca. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC6850428/figure/ca23343-fig-0012/).
- **Figura 13.** Corte sagital medio: inserción de la fascia en mandíbula y cara ventral de la lengua. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC6850428/figure/ca23343-fig-0013/).
- **Figura 14.** Corte parasagital: glándulas sublinguales suspendidas de la fascia. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC6850428/figure/ca23343-fig-0014/).
- **Figura 15.** Ramas del nervio lingual justo bajo la fascia en la cara ventral de la lengua. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC6850428/figure/ca23343-fig-0015/).

La figura 11 es la más útil para explicar qué es el frenillo.

## Auditoría anatómica de la fuente abierta — 03/11/2026

**Muestra y procedimiento:** 9 cadáveres adultos frescos (6 varones/3 mujeres, edades 50–87 años, media 72), con microdisección de la lengua y suelo de boca preservando relaciones mandibulares; no son niños ni mediciones de movimiento fisiológico en personas vivas.

**Resultado anatómico identificable:** la fascia del suelo de boca forma un plano transversal que se inserta en el arco mandibular interno; el frenillo es el **pliegue dinámico en la línea media de ese plano**, no una cuerda submucosa aislada. El geniogloso anterior puede quedar suspendido de su cara profunda, y ramas del nervio lingual recorren la cara ventral lingual superficialmente respecto a planos adyacentes. La tensión y la forma del pliegue cambian con el movimiento pasivo.

**Inferencia que NO autoriza:** la continuidad anatómica fascia–mandíbula no demuestra una fuerza posterior constante capaz de retraer la mandíbula, ni que la frenotomía cambie el crecimiento óseo. La propuesta biomecánica sobre estabilidad lingual es una **interpretación de los autores**, no una medición de fuerzas mandibulares en vivo.

**Estado de lectura:** texto completo abierto verificado en su versión PMC/Wiley, con métodos y conclusiones anatómicas, 03/11/2026. Licencia **CC BY-NC-ND 4.0**: no copiar/adaptar figuras para materiales comerciales.

---

<!-- archivo: fuentes/articulos/2019-mitchell-aaohns-amigdalectomia.md -->
# Estudio: Clinical Practice Guideline: Tonsillectomy in Children (Update)

- **ID:** MITCHELL2019
- **Autores, año y revista:** Mitchell RB; Archer SM; Ishman SL; Rosenfeld RM; Coles S; Finestone SA; Friedman NR; Giordano T; Hildrew DM; Kim TW; Lloyd RM; Parikh SR; Shulman ST; Walner DL; Walsh SA; Nnacheta LC. *Otolaryngol Head Neck Surg* 2019;160(1_suppl):S1-S42. Resumen ejecutivo: 2019;160(2):187-205 (PMID 30921525).
- **DOI / PMID / URL:** DOI `10.1177/0194599818801757`; PMID `30798778`; https://www.entnet.org/quality-practice/quality-products/clinical-practice-guidelines/tonsillectomy-in-children-update/
- **Tipo de estudio:** Guía de práctica clínica de la American Academy of Otolaryngology-Head and Neck Surgery Foundation. Actualiza la de 2011. Panel multidisciplinar (enfermería, anestesia, consumidores, medicina de familia, infecciosas, otorrinolaringología, pediatría y medicina del sueño).
- **Población y tamaño muestral:** Niños de 1 a 18 años candidatos a amigdalectomía.
- **Definición diagnóstica y técnicas:** Amigdalectomía definida como extirpación completa de la amígdala con su cápsula, con o sin adenoidectomía.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA: guía de amigdalectomía. Búsqueda en el texto completo el 05/11/2026: no aparecen «ankyloglossia», «tongue-tie», «frenulum» ni «myofunctional».
- **Variables de resultado:** No aplica (guía).
- **Resultados NUMÉRICOS verificados:** Unos 289.000 procedimientos ambulatorios al año en menores de 15 años en EE. UU. Para trastornos respiratorios del sueño: recomendar amigdalectomía a niños con apnea documentada por polisomnografía (en 2011 decía «aconsejar»). Infecciones de garganta recurrentes: espera vigilante si hay menos de 7 episodios en el último año, menos de 5 al año en 2 años o menos de 3 al año en 3 años.
- **Límites metodológicos / confusores (solo los relevantes):** No trata alternativas a la cirugía para la apnea más allá de la propia amigdalectomía.
- **Otros resultados relevantes (si los hay):** Dexametasona intravenosa intraoperatoria; no antibióticos perioperatorios; no codeína en menores de 12 años; ibuprofeno, paracetamol o ambos para el dolor. En noviembre de 2026 la AAO-HNS sigue listando esta versión como la vigente. Dice que la evidencia que apoya la amigdalectomía por motivos ortodóncicos, disfagia, disfonía, enuresis secundaria, cálculos amigdalinos, halitosis o amigdalitis crónica es limitada y de menor calidad.
- **Aportación del estudio:** Es la guía estadounidense vigente de amigdalectomía infantil, en la que se apoya la indicación quirúrgica de la apnea.
- **Licencia y derechos:** Copyright de la AAO-HNSF / SAGE. Aquí solo resumen propio.
- **Estado de lectura:** Texto completo (PDF) leído por búsqueda de términos el 05/11/2026. Recomendaciones del resumen.

## Figuras

Figuras no revisadas. [Ver la guía](https://doi.org/10.1177/0194599818801757).

---

<!-- archivo: fuentes/articulos/2019-zaghi-frenuloplastia-348.md -->
# Estudio: Lingual frenuloplasty with myofunctional therapy: Exploring safety and efficacy in 348 cases

- **ID:** ZAGHI2019
- **Autores, año y revista:** Zaghi S; Valcu-Pinkerton S; Jabara M et al.. Laryngoscope Investig Otolaryngol 2019;4(5):489-496.
- **DOI / PMID / URL:** DOI `10.1002/lio2.297`; PMID `31637291`; https://pmc.ncbi.nlm.nih.gov/articles/PMC6793603/
- **Tipo de estudio:** Cohorte retrospectiva con encuesta de resultados referidos por el paciente. Sin grupo control.
- **Población y tamaño muestral:** 420 pacientes consecutivos de 29 meses a 79 años; 348 encuestas respondidas (83 %). Un solo cirujano.
- **Definición diagnóstica y técnicas:** Frenuloplastia con tijera y sutura más terapia miofuncional previa obligatoria. Encuesta a más de 2 meses.
- **Criterio diagnóstico de anquiloglosia:** FUNCIONAL. El texto completo gradúa la restricción con la escala TRMR (grado 4 a 1): 20,7 % grado 4, 61,2 % grado 3, 13,3 % grado 2 y 4,7 % grado 1, estos dos con restricción posterior.
- **Variables de resultado:** Satisfacción, calidad de vida, respiración oral, ronquido, apretamiento, tensión miofascial, complicaciones.
- **Resultados NUMÉRICOS verificados:** Satisfacción 91 %. Mejora de calidad de vida 87 %: respiración oral 78,4 %, ronquido 72,9 %, apretamiento 91,0 %, tensión miofascial 77,5 %. Complicaciones menores <5 %; ninguna mayor. Otras cifras que circulan en el corpus de Zaghi (movilidad 96,5 %, deglución 80 %, dolor intenso 45 %, sangrado 12,6 %, entumecimiento 4,9 %) no están en el resumen: PENDIENTE DE VERIFICAR en el texto completo.
- **Límites metodológicos / confusores:** Sin grupo control. Resultados subjetivos. Pacientes seleccionados que ya hacían terapia miofuncional. Centro del propio autor. Nivel de evidencia 3 según los autores.
- **Hallazgos contrarios o no significativos:** No se describen en el resumen.
- **Conclusión que sí permite / que no permite:** Sí: Que la técnica parece segura en manos de este equipo y que muchos pacientes refieren mejoría. No: Atribuir la mejoría a la cirugía frente a la terapia o al placebo. Los autores piden estudios con medidas objetivas.
- **Licencia y derechos:** Acceso abierto en PMC. Licencia PENDIENTE DE VERIFICAR.
- **Estado de lectura:** Resumen PubMed y fragmentos del texto completo (PMC) revisados el 17/10/2026.

## Figuras

Licencia del artículo: CC BY-NC-ND 4.0 (no permite copiar aquí). Figuras en PubMed Central (PMC6793603).

- **Figura 1.** Caso de un hombre de 19 años con anquiloglosia funcional grado 3, antes y después. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC6793603/figure/lio2297-fig-0001/).
- **Figura 2.** Niña de 6 años: grado 3 que compensa hasta parecer grado 2 elevando el suelo de boca y el cuello. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC6793603/figure/lio2297-fig-0002/).
- **Figura 3.** Chico de 16 años, grado 4 tras láser previo, llevado a grado 1 con frenuloplastia y terapia. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC6793603/figure/lio2297-fig-0003/).
- **Figura 4.** TC sagital para valorar el espacio disponible para la lengua. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC6793603/figure/lio2297-fig-0004/).

La figura 2 ilustra la compensación que puede falsear el TRMR.

---

<!-- archivo: fuentes/articulos/2020-ada-australia-consenso.md -->
# Estudio: Ankyloglossia and Oral Frena Consensus Statement (Australian Dental Association)

- **ID:** ADAAU2020
- **Autores, año y revista:** Australian Dental Association, con un grupo de trabajo de 14 profesionales nombrados por sociedades australianas de 10 organizaciones australianas, entre ellas odontopediatría, matronas, consultoras de lactancia, logopedia, cirugía oral, quiropráctica y osteopatía. Primera edición, junio de 2020.
- **DOI / PMID / URL:** PDF: https://www.rch.org.au/uploadedFiles/Main/Pages/plastic/parent_information/Tongue%20tie%20-and-Oral-Frena-Consensus-Statement_June-2020.pdf (copia alojada por el Royal Children's Hospital de Melbourne). Política relacionada de la ADA: https://ada.org.au/policy-statement-2-13-ankyloglossia-and-oral-frena
- **Tipo de estudio:** Declaración de consenso multidisciplinar.
- **Población y tamaño muestral:** Lactantes, niños y adultos.
- **Definición diagnóstica y técnicas:** Lectura previa de la evidencia y discusión del grupo durante seis meses.
- **Criterio diagnóstico de anquiloglosia:** FUNCIONAL (con aspecto). Define la anquiloglosia como movimiento restringido de la lengua que causa limitaciones funcionales, junto a un frenillo visiblemente restringido. El diagnóstico no debe basarse solo en el aspecto. Requisitos: limitación funcional; valoración objetiva de la función con un sistema diagnóstico, como Martinelli o Hazelbaker; y valoración completa por un profesional cualificado. Prefiere sistemas que combinan función y aspecto frente a los que solo miran el aspecto. Sin limitación funcional, el frenillo se considera normal.
- **Variables de resultado:** Definición, diagnóstico, problemas asociados y manejo.
- **Resultados NUMÉRICOS verificados:** El término «posterior tongue tie» no debe usarse como diagnóstico. No hay pruebas suficientes de que la anquiloglosia cause apnea, reflujo, cólico u otros problemas. Una minoría de niños puede desarrollar problemas de habla por anquiloglosia, pero ninguna evidencia disponible demuestra relación causal con problemas de articulación o retraso del habla, y no hay forma de predecir qué lactantes los tendrán. Maloclusión, recesión de encía y caries no se pueden predecir por el aspecto del frenillo. El manejo no quirúrgico puede ser la primera línea; la cirugía, solo si este falla.
- **Límites metodológicos / confusores:** Es un consenso de expertos. Reconoce que todos los sistemas diagnósticos tienen limitaciones y que muchos no están validados.
- **Hallazgos contrarios o no significativos:** No aplica.
- **Conclusión que sí permite / que no permite:** Sí: Decir que este consenso exige demostrar una limitación funcional para diagnosticar anquiloglosia. No: Decir que haya validado un criterio diagnóstico: recomienda herramientas existentes con límites reconocidos.
- **Licencia y derechos:** Documento de la ADA. Aquí solo resumen propio.
- **Estado de lectura:** Texto completo (PDF) leído el 02/11/2026. Búsqueda de actualización del 02/11/2026.

## Figuras

Figuras no revisadas. [Ver el documento](https://www.rch.org.au/uploadedFiles/Main/Pages/plastic/parent_information/Tongue%20tie%20-and-Oral-Frena-Consensus-Statement_June-2020.pdf).

---

<!-- archivo: fuentes/articulos/2020-bandyopadhyay-miofuncional-apnea-ninos.md -->
# Estudio: Effect of myofunctional therapy on children with obstructive sleep apnea: a meta-analysis

- **ID:** BANDYOPADHYAY2020
- **Autores, año y revista:** Bandyopadhyay A; Kaneshiro K; Camacho M. *Sleep Medicine* 2020;75:210–217.
- **DOI / PMID / URL:** DOI `10.1016/j.sleep.2020.08.003`; PMID `32861058`; [manuscrito aceptado depositado en Indiana University](https://scholarworks.indianapolis.iu.edu/server/api/core/bitstreams/9bc77cf4-a306-4afc-b3b2-4ca0d4d1a4bb/content); [abstract editorial](https://doi.org/10.1016/j.sleep.2020.08.003).
- **Tipo de estudio:** Revisión sistemática y metaanálisis de cambios **antes/después de intervención**. Incluye casos, series, cohortes/casos y controles y **3 ensayos denominados aleatorizados**; **no** es una metaanálisis exclusivamente de diferencias entre brazos aleatorizados.
- **Población y tamaño muestral:** **10 estudios** seleccionados; manuscrito especifica **285 niños en total, 241 tratados con terapia miofuncional y 44 controles**. El resumen destaca «10 estudios, 241 pacientes»: debe precisarse que 241 corresponde a quienes recibieron MT, no a toda la población de los 10 artículos. Uno de los estudios no aportó datos de desenlace útiles al metaanálisis.
- **Definición diagnóstica y técnicas:** Búsqueda multibase hasta abril/mayo de 2020, diseños con información PSG anterior y posterior, terapias miofuncionales **activas o pasivas** (incluidos aparatos orales). Siete estudios principalmente en apnea residual tras adenoamigdalectomía; otros en apnea sin hipertrofia adenoamigdalar. Algunos estudios de sueño **domiciliarios**, otros de laboratorio; la mayor parte no reportó adherencia. Tres ECA: **ninguno cegado ni con detalles de generación de secuencia** en el manuscrito. La comparación principal publicada es **pre vs post**.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA: el estudio sintetiza terapia miofuncional para apnea pediátrica, no participantes diagnosticados por frenillo corto, TRMR o succión posterior.
- **Variables de resultado:** AHI/oAHI por estudio de sueño, saturación media y mínima nocturna, presencia de respiración bucal.
- **Resultados NUMÉRICOS verificados en el texto del manuscrito:**
  - IAH basal **4,32/h** vs seguimiento **2,48/h**; reducción relativa descriptiva **43 %**. Metaanálisis **diferencia antes/después −1,54/h** (IC95 % **−2,24 a −0,85**, p<0,0001).
  - **Heterogeneidad I²=72 %** para IAH; análisis de sensibilidad con exclusiones por heterogeneidad produjo −2,22/h (−2,87 a −1,57) en 160 niños, **NO** es efecto entre grupos ni demuestra que la exclusión sea neutral.
  - Saturación media **+0,37 puntos porcentuales** (IC95 % 0,06–0,69); saturación mínima **sin mejoría significativa**, heterogeneidad I²=87 %.
  - Respiración bucal (3 estudios): OR antes/después reportada **0,03** (IC95 % 0,01–0,10), medición no homogénea de respiración (valoración de terapeuta u otra prueba).
  - Subgrupo **pasivo** (128 niños) IAH −2,14/h (−2,87 a −1,40) y **activo** (66 niños) −1,04/h (−1,98 a −0,09); estas no son comparaciones aleatorizadas de modalidades. Adherencia entre modalidades, cuando registrada, muy distinta.
- **Límites metodológicos / confusores:** Agrupar antes/después con diseños de bajo control **no permite atribución causal**; maduración, cambios de peso, cirugía reciente, uso de aparato, regresión a la media y adherencia influyen. Tres ECA sin detalle de aleatorización/cegamiento. Duración desde **una semana hasta 50 meses**. Definiciones heterogéneas de respiración oral. Un niño tratado no equivale a niño aleatorizado. La reducción relativa 43 % se calculó desde AHI inicial pequeño (4,32), cuya importancia clínica absoluta y sostenibilidad deben evaluarse. La afirmación introductoria de reversibilidad de cambios esqueléticos es un **contexto teórico**, no un resultado del metaanálisis.
- **Hallazgos contrarios o no significativos:** **Sin beneficio significativo de SpO₂ mínima**; en uno de los ensayos de tres brazos, el brazo de ejercicios activos no halló cambio significativo de IAH según su discusión. Los análisis conservadores de **Cnockaert 2026** (4 ECA, n=174, diferencia **entre grupos** −1,68/h, IC95 % −3,61 a +0,24) no confirman eficacia independiente como monoterapia universal.
- **Conclusión que sí permite / que no permite:** Sí: los estudios reunidos describieron mejorías *dentro de los pacientes* en algunas métricas de sueño después de terapias heterogéneas, que merecen investigación. No: demostrar eficacia frente a control de terapia miofuncional aislada, beneficio de frenotomía, crecimiento esquelético ni persistencia a largo plazo de cambios.
- **Licencia y derechos:** Manuscrito de autor disponible públicamente en repositorio; **licencia de reutilización no verificada**. No incorporar PDF ni figuras al repositorio de evidencia.
- **Estado de lectura:** Texto extraído de manuscrito de autor abierto consultado el **03/11/2026**, incluyendo métodos, resultados, discusión y limitaciones. **La herramienta de captura visual del PDF no pudo renderizar sus tablas/figuras**, por lo que no se ha verificado la representación gráfica ni los datos originales de cada subestudio. No declarar auditoría completa del riesgo de sesgo.

## Figuras

No copiadas ni verificadas visualmente. [Manuscrito de autor](https://scholarworks.indianapolis.iu.edu/server/api/core/bitstreams/9bc77cf4-a306-4afc-b3b2-4ca0d4d1a4bb/content).

---

<!-- archivo: fuentes/articulos/2020-burgos-sanchez-alcohol-apnea.md -->
# Estudio: Impact of Alcohol Consumption on Snoring and Sleep Apnea: A Systematic Review and Meta-analysis

- **ID:** BURGOS2020
- **Autores, año y revista:** Burgos-Sanchez C; Jones NN; Avillion M et al.. Otolaryngol Head Neck Surg 2020.
- **DOI / PMID / URL:** DOI `10.1177/0194599820931087`; PMID `32513091`
- **Tipo de estudio:** Revisión sistemática (con metaanálisis si lo indica el título).
- **Población y tamaño muestral:** 13 estudios, 279 pacientes.
- **Definición diagnóstica y técnicas:** Búsqueda en varias bases de datos.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA: el estudio no diagnostica anquiloglosia.
- **Variables de resultado:** IAH, saturación mínima y somnolencia, salvo que se indique otra cosa.
- **Resultados NUMÉRICOS verificados:** Con alcohol: IAH +3,98/h y saturación mínima -2,72 %.
- **Límites metodológicos / confusores:** Estudios primarios pequeños y sobre todo series de casos. Zaghi es coautor.
- **Hallazgos contrarios o no significativos:** No se describen en el resumen.
- **Conclusión que sí permite / que no permite:** Sí: Decir que el alcohol empeora el ronquido y la apnea en personas susceptibles. No: Cuantificar el efecto en bebedores habituales.
- **Licencia y derechos:** Derechos del editor. Aquí solo metadatos y resumen propio.
- **Estado de lectura:** Resumen PubMed revisado el 17/10/2026.

## Figuras

Figuras no revisadas: el texto completo no está en acceso abierto en PMC. [Ver el artículo](https://doi.org/10.1177/0194599820931087).

---

<!-- archivo: fuentes/articulos/2020-chen-osteotomia-sagital-mma.md -->
# Estudio: Optimizing mandibular sagittal split of large maxillomandibular advancements for obstructive sleep apnea: patient and surgical factors

- **ID:** CHEN2020
- **Autores, año y revista:** Chen YF; Ko EC; Zaghi S et al.. Clin Oral Investig 2020.
- **DOI / PMID / URL:** DOI `10.1007/s00784-019-03017-5`; PMID `31332567`
- **Tipo de estudio:** Cohorte retrospectiva con TC.
- **Población y tamaño muestral:** 46 pacientes (43 hombres).
- **Definición diagnóstica y técnicas:** Patrones de fractura de la osteotomía sagital.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA: el estudio no diagnostica anquiloglosia.
- **Variables de resultado:** Grosor óseo y área de solapamiento.
- **Resultados NUMÉRICOS verificados:** La técnica quirúrgica pesó más que la edad o la gravedad.
- **Límites metodológicos / confusores:** Retrospectivo.
- **Hallazgos contrarios o no significativos:** No se describen en el resumen.
- **Conclusión que sí permite / que no permite:** Sí: Citar detalles técnicos del MMA. No: Concluir sobre resultados respiratorios.
- **Licencia y derechos:** Derechos del editor. Aquí solo metadatos y resumen propio.
- **Estado de lectura:** Resumen PubMed revisado el 17/10/2026.

## Figuras

Figuras no revisadas: el texto completo no está en acceso abierto en PMC. [Ver el artículo](https://doi.org/10.1007/s00784-019-03017-5).

---

<!-- archivo: fuentes/articulos/2020-cohen-levy-apnea-persistente.md -->
# Estudio: Prevalence of malocclusions and oral dysfunctions in children with persistent sleep-disordered breathing after adenotonsillectomy in the long term

- **ID:** COHENLEVY2020
- **Autores, año y revista:** Cohen-Levy J; Quintal MC; Rompré P; Almeida F; Huynh N. J Clin Sleep Med 2020;16(8):1357-1368.
- **DOI / PMID / URL:** DOI `10.5664/jcsm.8534`; PMID `32356517`; https://pmc.ncbi.nlm.nih.gov/articles/PMC7446101/
- **Tipo de estudio:** Revisión retrospectiva de historias e invitación a evaluación.
- **Población y tamaño muestral:** De 4.000 niños operados, 100 con síntomas persistentes evaluados (edad media 8,8 años), de 1 a 12 años tras la cirugía; 69 con estudio de sueño tipo III.
- **Definición diagnóstica y técnicas:** Evaluación ortodóncica y miofuncional y estudio de sueño ambulatorio de una noche.
- **Criterio diagnóstico de anquiloglosia:** MIXTO. Separa «frenillo lingual corto» (anatomía; definición PENDIENTE DE VERIFICAR) de «inmadurez motora lingual» (función).
- **Variables de resultado:** Índice de eventos respiratorios obstructivos y total.
- **Resultados NUMÉRICOS verificados:** Frenillo corto en el 40 %, sin asociación específica con los parámetros de sueño. La inmadurez lingual y un reflejo dilatador nasal alterado sí se asociaron a más eventos (por ejemplo, 1,72 frente a 0,72 eventos/h; P=0,011).
- **Límites metodológicos / confusores:** Retrospectivo, sin control, estudio de sueño tipo III en 69.
- **Hallazgos contrarios o no significativos:** La anatomía del frenillo, sola, no se asoció.
- **Conclusión que sí permite / que no permite:** Sí: Decir que en niños con apnea persistente tras la cirugía pesa la función de la lengua más que la longitud del frenillo. No: Afirmar causalidad.
- **Licencia y derechos:** Acceso abierto en PMC. Licencia PENDIENTE DE VERIFICAR.
- **Estado de lectura:** Resumen PubMed revisado el 17/10/2026.

## Figuras

Licencia del artículo: Derechos del editor. No se copian imágenes.

Figuras no extraídas: la versión de PMC no se puede leer por la API. [Ver el artículo en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7446101/). Descripción: `PENDIENTE DE VERIFICAR`.

---

<!-- archivo: fuentes/articulos/2020-ghaheri-lacking-consensus.md -->
# Estudio: Lacking Consensus: The Management of Ankyloglossia in Children

- **ID:** GHAHERI2020
- **Autores, año y revista:** Ghaheri BA; Tylor DA; Zaghi S. Otolaryngol Head Neck Surg 2020;163(5):1064.
- **DOI / PMID / URL:** DOI `10.1177/0194599820937299`; PMID `33137275`
- **Tipo de estudio:** Carta al director. Comentario al consenso de Messner 2020.
- **Población y tamaño muestral:** No aplica.
- **Definición diagnóstica y técnicas:** No aplica.
- **Criterio diagnóstico de anquiloglosia:** Carta sin resumen en PubMed. Qué criterio defiende: PENDIENTE DE VERIFICAR (texto no leído). En el corpus de Zaghi se resume como una crítica a la falta de base funcional del consenso.
- **Variables de resultado:** No aplica.
- **Resultados NUMÉRICOS verificados:** No aplica.
- **Límites metodológicos / confusores:** Opinión. Hay respuesta de los autores del consenso en el mismo número (doi 10.1177/0194599820937298).
- **Hallazgos contrarios o no significativos:** Ver MESSNER2020.
- **Conclusión que sí permite / que no permite:** Sí: Documentar que el consenso de 2020 fue discutido por clínicos que tratan anquiloglosia. No: Usarla como evidencia clínica.
- **Licencia y derechos:** Derechos del editor. Aquí solo metadatos y resumen propio.
- **Estado de lectura:** Solo metadatos PubMed (17/10/2026). Texto pendiente.

## Figuras

Figuras no revisadas: el texto completo no está en acceso abierto en PMC. [Ver el artículo](https://doi.org/10.1177/0194599820937299).

---

<!-- archivo: fuentes/articulos/2020-malhotra-endotipos-apnea.md -->
# Estudio: Endotypes and phenotypes in obstructive sleep apnea

- **ID:** MALHOTRA2020
- **Autores, año y revista:** Malhotra A; Mesarwi O; Pépin JL; Owens RL. *Curr Opin Pulm Med* 2020;26(6):609–614.
- **DOI / PMID / URL:** DOI `10.1097/MCP.0000000000000724`; PMID `32890019`; PMCID `PMC7544644`; [manuscrito íntegro de autor en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7544644/).
- **Tipo de estudio:** Revisión narrativa mecanística (sin metaanálisis ni cohorte original).
- **Población y tamaño muestral:** Integra trabajos anteriores de apnea obstructiva del sueño (OSA) y factores fisiopatológicos; no hay un n conjunto de participantes.
- **Definición diagnóstica y técnicas:** Distingue **endotipos** (mecanismos fisiológicos) de **fenotipos** (manifestaciones observadas, riesgos y síntomas), con ejemplos procedentes de estudios con imagen, fisiología ventilatoria, EMG y análisis de conglomerados.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA: no clasifica frenillo ni movilidad lingual.
- **Variables de resultado:** Mecanismos de colapso faríngeo durante sueño, expresión clínica, riesgo cardiometabólico y posibles diferencias de respuesta terapéutica.
- **Resultados y hallazgos revisados en texto completo:**
  - Describe **cuatro grandes endotipos** que pueden combinarse: **(1) compromiso anatómico/colapsabilidad faríngea, (2) respuesta insuficiente de dilatadores faríngeos, (3) control ventilatorio inestable (*loop gain* elevado), (4) umbral bajo de despertar**. También menciona volumen pulmonar, intensidad de la respuesta al despertar y redistribución de líquidos.
  - La **actividad muscular dilatadora aumenta en vigilia en muchos pacientes con OSA** como compensación; al iniciar el sueño disminuyen reflejos protectores, y puede manifestarse el colapso en vías aéreas predispuestas.
  - Los autores distinguen **EMG** (activación eléctrica) de eficacia mecánica y explican la variabilidad del **reflejo de presión negativa** (*negative-pressure reflex*) en vigilia y sueño.
  - En análisis de conglomerados, diferentes poblaciones pueden agruparse por **somnolencia/riesgo cardiovascular**, **sueño alterado con insomnio** o **pocos síntomas**, entre otras agrupaciones; las clasificaciones dependen de las variables seleccionadas.
  - El **IAH/AHI** es útil para definir OSA pero comprime fenotipos fisiológicos distintos; los autores consideran además **carga hipóxica**, duración de eventos y frecuencia de activaciones para investigar riesgo y respuesta.
  - **No** ofrece una estimación única combinada de eficacia de tratamientos ni un porcentaje general aplicable a todos los pacientes; es una síntesis conceptual.
- **Aportación del estudio:** Propone **una estructura mecanística útil para conectar anatomía craneofacial, actividad neuromuscular, respiración y sueño**. Permite formular mejores preguntas de investigación que comparar únicamente volumen anatómico o IAH entre poblaciones no caracterizadas por mecanismo.
- **Límites metodológicos / confusores (pertinentes):** Revisión narrativa principalmente de adultos con OSA; no investiga aquí fenotipos por anquiloglosia ni evalúa liberación lingual. La taxonomía de endotipos y los subgrupos clínicos proceden de estudios diferentes.
- **Licencia y derechos:** Manuscrito abierto en PubMed Central; licencia de reproducción de imágenes no verificada. Sin figuras copiadas.
- **Estado de lectura:** **Manuscrito completo de autor en PMC revisado el 04/11/2026**: introducción, endotipos, fenotipos, implicaciones y conclusiones. Sin evaluación exhaustiva de cada referencia citada.

## Conexiones con otras piezas de la biblioteca

- Li 2026: rinitis y SDB infantil: una manifestación nasal es un factor clínico adicional, no una categoría universal de OSA.
- Coppelson 2023: postura y CBCT: anatomía en imagen y función durante sueño son mediciones complementarias.
- Mapa interdisciplinar: añadir endotipos como marco de mecanismos, no como evidencia de una única cadena causal.

## Figuras

No reproducidas. [Original abierto en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7544644/).

---

<!-- archivo: fuentes/articulos/2020-messner-consenso.md -->
# Estudio: Clinical Consensus Statement: Ankyloglossia in Children

- **ID:** MESSNER2020
- **Autores, año y revista:** Messner AH; Walsh J; Rosenfeld RM et al. Otolaryngol Head Neck Surg 2020;162(5):597-611. Documento de la American Academy of Otolaryngology-Head and Neck Surgery Foundation (AAO-HNSF).
- **DOI / PMID / URL:** DOI `10.1177/0194599820915457`; PMID `32283998`
- **Tipo de estudio:** Consenso de expertos con método Delphi modificado (3 rondas de encuesta anónima con escala de 1 a 9). Consenso definido de antemano: media de 7 o más y como mucho 1 valor atípico.
- **Población y tamaño muestral:** Niños de 0 a 18 años. Panel formado solo por otorrinolaringólogos pediátricos que evalúan y operan anquiloglosia. Número exacto de panelistas: `PENDIENTE DE VERIFICAR`.
- **Definición diagnóstica y técnicas:** Revisión de la literatura (búsquedas de diciembre de 2018 y marzo de 2019) y encuesta Delphi.
- **Criterio diagnóstico de anquiloglosia:** FUNCIONAL como definición, sin herramienta. Hubo consenso en definirla como «limited tongue mobility caused by a restrictive lingual frenulum» (afirmación 4c). El texto subraya que hay que demostrar la restricción de la movilidad y atribuirla al frenillo. **No recomendó ninguna escala:** dice que, por el desacuerdo en la definición y la falta de herramientas validadas, no pudo recomendar un sistema de graduación. La afirmación «Coryllos es la escala preferida» no tuvo consenso (media 4,82). Tampoco hubo consenso sobre qué es la anquiloglosia «posterior».
- **Variables de resultado:** Grado de acuerdo con cada afirmación.
- **Resultados NUMÉRICOS verificados:** Resumen: 89 afirmaciones; 41 con consenso, 17 casi consenso y 28 sin consenso. Texto completo: tras unir duplicadas quedaron 86; 41 (48 %) alcanzaron consenso y 45 (52 %) no. Algunas afirmaciones con consenso: hay sobrediagnóstico en algunas comunidades (2b); la anquiloglosia no causa apnea del sueño (54); no suele afectar al habla (13b); no debe operarse el «frenillo bucal» (36); antes de una frenotomía en un lactante con dificultades conviene valorar la lactancia, idealmente por una consultora de lactancia (20, 22); dolor materno y mal agarre pueden deberse a la anquiloglosia y también a otras causas (12).
- **Límites metodológicos / confusores:** Opinión de expertos de una sola especialidad. Los autores reconocen lagunas de conocimiento y falta de evidencia sobre diagnóstico y tratamiento.
- **Hallazgos contrarios o no significativos:** Criticado en GHAHERI2020. Kummer 2025 lo cita para decir que la anquiloglosia no suele afectar al habla. En el apartado de apnea, el texto (no una afirmación votada) dice que solo un pequeño estudio retrospectivo se ha citado como prueba de una asociación directa entre anquiloglosia y apnea (Huang, Quo, Berkowski y Guilleminault 2015) y que la inserción anterior de la lengua evita en parte su colapso posterior, de modo que liberarla podría empeorar la apnea; para esto último cita a Walsh 1995 (obstrucción parcial tras una frenotomía) y Genther 2015 (dos lactantes con secuencia de Pierre Robin). Comprobado en el texto completo el 05/11/2026.
- **Conclusión que sí permite / que no permite:** Sí: citar la postura de la otorrinolaringología pediátrica estadounidense en 2020, su definición funcional y que no pudo recomendar ninguna escala diagnóstica. No: presentarlo como evidencia empírica de que la anquiloglosia no tiene efectos. Es opinión de expertos.
- **Licencia y derechos:** Derechos del editor. Aquí solo metadatos, resumen propio y citas cortas.
- **Estado de lectura:** Resumen PubMed revisado el 17/10/2026. Texto completo leído el 02/11/2026 (copia en PDF disponible en la web; no se redistribuye).

## Figuras

Figuras no revisadas. La figura 1 muestra un ejemplo de anquiloglosia anterior frente a posible posterior. [Ver el artículo](https://doi.org/10.1177/0194599820915457).

---

<!-- archivo: fuentes/articulos/2020-mills-histologia.md -->
# Mills et al. (2020) — Understanding the Lingual Frenulum

- DOI: `10.1155/2020/1820978`; acceso abierto: https://pmc.ncbi.nlm.nih.gov/articles/PMC7391099/
- Diseño: histología de 13 cadáveres adultos (10 embalsamados y 3 frescos).
- Hallazgo: identificó capas de fascia en el suelo de la boca con variación de espesor y composición, formando parte de los pliegues del frenillo.
- Relevancia: continuidad anatómica; no prueba efecto mecánico in vivo sobre la posición sagital mandibular.
- Criterio diagnóstico de anquiloglosia: NO APLICA: estudio anatómico o biomecánico, no diagnostica anquiloglosia.
- Estado: texto primario y datos metodológicos revisados; extracción completa pendiente.

## Figuras

Licencia del artículo: CC BY. Figuras en PubMed Central (PMC7391099).

- **Figura 1.** Pasos de obtención de piezas de cadáver embalsamado. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7391099/figure/fig1/).
- **Figura 2.** Pasos de obtención del frenillo en cadáver fresco. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7391099/figure/fig2/).
- **Figura 3.** Capas de la fascia del suelo de boca en tinción tricrómica, con geniogloso, conductos y glándulas. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7391099/figure/fig3/). Copia local: figuras/MILLS2020-fig3.jpg.
- **Figura 4.** Engrosamiento de la fascia central del suelo de boca. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7391099/figure/fig4/). Copia local: figuras/MILLS2020-fig4.jpg.
- **Figura 5.** La fascia se funde con el periostio de la mandíbula. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7391099/figure/fig5/). Copia local: figuras/MILLS2020-fig5.jpg.
- **Figura 6.** Tejido conjuntivo denso de la cara ventral de la lengua y capas fasciales en la línea media. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7391099/figure/fig6/). Copia local: figuras/MILLS2020-fig6.jpg.
- **Figura 7.** Desembocadura del conducto submandibular suspendida por fascia densa. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7391099/figure/fig7/). Copia local: figuras/MILLS2020-fig7.jpg.
- **Figura 8.** Ramas del nervio lingual superficiales en la cara ventral. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7391099/figure/fig8/). Copia local: figuras/MILLS2020-fig8.jpg.
- **Figura 9.** Tipos de colágeno I y III con luz polarizada. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7391099/figure/fig9/). Copia local: figuras/MILLS2020-fig9.jpg.
- **Figura 10.** Fibras elásticas en el suelo de boca, la lengua y los conductos. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7391099/figure/fig10/). Copia local: figuras/MILLS2020-fig10.jpg.
- **Figura 11.** Corte coronal del frenillo extirpado bajo tensión (pieza 1). [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7391099/figure/fig11/).
- **Figura 12.** Corte coronal del frenillo extirpado (pieza 2). [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7391099/figure/fig12/).
- **Figura 13.** Corte coronal del frenillo extirpado (pieza 3). [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7391099/figure/fig13/).

Crédito: figuras de Mills et al. (2020): Understanding the Lingual Frenulum (PMC7391099), CC BY. Las copias locales no se han modificado.

Las figuras 1, 2 y 11 a 13 son fotos de piezas de cadáver: solo enlace.

## Auditoría histológica de la fuente abierta — 03/11/2026

**Muestra y técnicas:** 13 cadáveres adultos: 10 embalsamados y 3 frescos congelados con la lengua elevada; cortes coronales de 10 μm con tricrómico de Masson (morfología), Verhoeff–van Gieson (elastina) y Picrosirius Red (colágeno).

**Resultados:** se identificaron capas fasciales submucosas en todos los especímenes, con grosores y composición variables entre individuos y regiones. En la zona media hubo abundancia de colágeno III y capas de elastina variables. El frenillo elevado consistía en un pliegue de fascia y mucosa. El geniogloso y las glándulas sublinguales se relacionaban con la cara profunda de la fascia, con patrones anatómicos distintos entre especímenes.

**Límites que importa reconocer:** examen **cualitativo**; los autores evitaron cuantificar proporciones de fibras por variación y error de muestreo; no usaron inmunohistoquímica para cuantificación de tipos de colágeno. Pequeña muestra adulta (>50 años) no permite inferir cronología del crecimiento ni tensiones in vivo. No mide fuerzas sobre la mandíbula ni respuesta mecánica a cirugía.

**Estado de lectura:** métodos, resultados, discusión y límites contrastados en la versión abierta (PMC/Wiley), 03/11/2026. Licencia CC BY; no se ha copiado contenido de la fuente.

---

<!-- archivo: fuentes/articulos/2020-salt-habla-preescolares.md -->
# Estudio: Speech production in young children with tongue-tie

- **ID:** SALT2020
- **Autores, año y revista:** Salt H; Claessen M; Johnston T; Smart S. *International Journal of Pediatric Otorhinolaryngology* 2020;134:110035.
- **DOI / PMID / URL:** DOI `10.1016/j.ijporl.2020.110035`; PMID `32298924`; [abstract PubMed](https://pubmed.ncbi.nlm.nih.gov/32298924/).
- **Tipo de estudio:** Estudio comparativo transversal de niños pequeños con distintos antecedentes de anquiloglosia y tratamiento.
- **Población y tamaño muestral:** **59 niños de 2 años y 1 mes a 4 años y 11 meses**, distribuidos en tres grupos: frenillo previamente tratado (TTT), frenillo no tratado (UTT) y ausencia de diagnóstico (NTT).
- **Definición diagnóstica y técnicas:** Comparación de estructura y función del frenillo, movilidad lingual, producción de sonidos del habla y valoraciones de inteligibilidad de padres y profesionales. El resumen no identifica la escala exacta que determinó la pertenencia a cada grupo; `PENDIENTE DE VERIFICAR`.
- **Criterio diagnóstico de anquiloglosia:** PENDIENTE DE VERIFICAR: el abstract identifica grupos con diagnóstico tratado/no tratado y recoge medidas anatómicas y funcionales, pero no describe el instrumento de clasificación original.
- **Variables de resultado:** Movilidad, producción de habla, inteligibilidad y antecedentes de asistencia a logopedia.
- **Resultados NUMÉRICOS verificados:** **59 niños en total**; los autores **no encontraron diferencias estadísticamente significativas entre los tres grupos** para movilidad, producción de habla ni inteligibilidad. El grupo con frenillo no tratado registró más antecedentes de atención logopédica que el grupo sin diagnóstico. El abstract no facilita tamaños de efecto ni intervalos de confianza para cada comparación.
- **Aportación del estudio:** Resultado comparativo negativo relevante para evaluar la relación entre anquiloglosia, intervención temprana y habla en edad preescolar; aporta un contraste con trabajos pre/post de cirugía de frenillo en niños mayores.
- **Límites metodológicos / confusores (solo los relevantes):** Tamaño reducido, grupos según diagnóstico y tratamiento previo; el resultado depende de los criterios de grupo y las pruebas de lenguaje realmente utilizadas, que requieren texto completo. No se asignó tratamiento aleatoriamente.
- **Licencia y derechos:** Derechos del editor; se sintetiza el abstract, no se almacena PDF.
- **Estado de lectura:** **Resumen PubMed/Elsevier consultado el 04/11/2026**. Texto completo editorial no revisado.
## Figuras

No examinadas. [Artículo original](https://doi.org/10.1016/j.ijporl.2020.110035).

---

<!-- archivo: fuentes/articulos/2020-van-biervliet-primum-non-nocere.md -->
# Estudio: Primum non nocere: lingual frenotomy for breastfeeding problems, not as innocent as generally accepted

- **ID:** VANBIERVLIET2020
- **Autores, año y revista:** Van Biervliet S; Van Winckel M; Vande Velde S et al.. Eur J Pediatr 2020;179(8):1191-1195.
- **DOI / PMID / URL:** DOI `10.1007/s00431-020-03705-5`; PMID `32506218`
- **Tipo de estudio:** Revisión narrativa.
- **Población y tamaño muestral:** No aplica.
- **Definición diagnóstica y técnicas:** No aplica.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA. Discute que unas escalas son solo de aspecto y otras incluyen función, y que ninguna predice los problemas de lactancia.
- **Variables de resultado:** No aplica.
- **Resultados NUMÉRICOS verificados:** Sin cifras propias.
- **Límites metodológicos / confusores:** Opinión de autores.
- **Hallazgos contrarios o no significativos:** No aplica.
- **Conclusión que sí permite / que no permite:** Sí: Citar la postura prudente: evaluación multidisciplinar antes de operar. No: Usarla como prueba de daño.
- **Licencia y derechos:** Derechos del editor. Aquí solo metadatos y resumen propio.
- **Estado de lectura:** Resumen PubMed y texto completo revisados el 17/10/2026.

## Figuras

Licencia: derechos del editor (no se copian imágenes). Leyendas leídas en el texto completo; puede haber más figuras que las listadas.

- **Figura 1.** Esquema anatómico del frenillo como pliegue de la fascia (basado en Mills). [Ver en el artículo](https://doi.org/10.1007/s00431-020-03705-5), figura 1.

---

<!-- archivo: fuentes/articulos/2020-yoon-dome.md -->
# Estudio: Distraction Osteogenesis Maxillary Expansion (DOME) for adult obstructive sleep apnea patients with narrow maxilla and nasal floor

- **ID:** YOON2020
- **Autores, año y revista:** Yoon A; Guilleminault C; Zaghi S; Liu SY. Sleep Med 2020;65:172-176.
- **DOI / PMID / URL:** DOI `10.1016/j.sleep.2019.06.002`; PMID `31606311`
- **Tipo de estudio:** Serie retrospectiva antes y después, sin control.
- **Población y tamaño muestral:** 75 adultos con apnea confirmada por polisomnografía y maxilar estrecho; edad media 30,5 años; 57 hombres y 18 mujeres. Stanford, 2014-2018.
- **Definición diagnóstica y técnicas:** Expansor anclado con microimplantes más osteotomías mínimas, y después ortodoncia.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA: el estudio no diagnostica anquiloglosia.
- **Variables de resultado:** IAH, Epworth, NOSE, ODI y porcentaje de sueño REM.
- **Resultados NUMÉRICOS verificados:** IAH 17,65 → 8,17 (p<0,0001; medido en 43 sujetos). NOSE 10,94 → 3,28. Epworth 10,48 → 6,69. REM 14,4 % → 22,7 %. Sin efectos adversos significativos.
- **Límites metodológicos / confusores:** Sin grupo control. IAH solo en 43 de 75. Pacientes seleccionados. Autores que desarrollan la técnica.
- **Hallazgos contrarios o no significativos:** No se describen en el resumen.
- **Conclusión que sí permite / que no permite:** Sí: Decir que en esta serie seleccionada la apnea y la obstrucción nasal mejoraron tras DOME. No: Comparar DOME con otros tratamientos ni generalizar a todos los adultos con apnea.
- **Licencia y derechos:** Derechos del editor. Aquí solo metadatos y resumen propio.
- **Estado de lectura:** Resumen PubMed revisado el 17/10/2026.

## Figuras

Figuras no revisadas: el texto completo no está en acceso abierto en PMC. [Ver el artículo](https://doi.org/10.1016/j.sleep.2019.06.002).

---

<!-- archivo: fuentes/articulos/2021-aapd-politica-apnea.md -->
# Estudio: Policy on Obstructive Sleep Apnea (OSA) (American Academy of Pediatric Dentistry)

- **ID:** AAPD2021OSA
- **Autores, año y revista:** American Academy of Pediatric Dentistry (AAPD), Council on Clinical Affairs. Adoptada en 2016, última revisión 2021. The Reference Manual of Pediatric Dentistry 2025:145-8.
- **DOI / PMID / URL:** PDF: https://www.aapd.org/globalassets/media/policies_guidelines/p_sleepapnea.pdf
- **Tipo de estudio:** Política (posicionamiento) de una sociedad de odontopediatría. Búsqueda en PubMed de los últimos 10 años (283 artículos); donde los datos no bastaban, opinión de expertos o consenso.
- **Población y tamaño muestral:** Pacientes pediátricos.
- **Definición diagnóstica y técnicas:** Diagnóstico por el médico; la AAPD pide derivar.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA: política de apnea. Búsqueda en el texto completo el 05/11/2026: no aparecen «ankyloglossia», «tongue-tie», «frenulum» ni «myofunctional».
- **Variables de resultado:** No aplica (política).
- **Resultados NUMÉRICOS verificados:** Prevalencia citada del 1 al 5 % de los niños, más frecuente de 2 a 7 años. Recomendaciones: cribar trastornos respiratorios del sueño y ronquido; valorar la hipertrofia amigdalar; **valorar la posición de la lengua, porque puede contribuir a la obstrucción**; reconocer la obesidad y las anomalías craneofaciales; derivar al médico para diagnóstico y tratamiento; considerar aparatos intraorales solo tras una valoración ortodóncica y craniofacial completa, dentro de un enfoque multidisciplinar.
- **Límites metodológicos / confusores (solo los relevantes):** Dice que la evidencia sobre la expansión rápida del maxilar son estudios pequeños, sin control y con seguimiento corto, y que los estudios a favor de intervenciones dentales no quirúrgicas tienen muestras pequeñas y sin grupo control.
- **Otros resultados relevantes (si los hay):** Para valorar la lengua cita la clasificación de Mallampati y la posición lingual de Friedman, que miden la posición de la lengua en reposo, no su movilidad. Según la web de la AAPD, el manual 2026-27 trae una revisión nueva de esta política: `PENDIENTE DE VERIFICAR`.
- **Aportación del estudio:** Posicionamiento de la odontopediatría estadounidense sobre apnea; complementa su política sobre el frenillo (AAPD 2022).
- **Licencia y derechos:** Documento de la AAPD. Aquí solo resumen propio.
- **Estado de lectura:** Texto completo (PDF, versión del manual 2025) leído el 05/11/2026.

## Figuras

No tiene figuras.

---

<!-- archivo: fuentes/articulos/2021-deregibus-funcion-lingual-ortodoncia.md -->
# Estudio: Analysis of Tongue Function from the Orthodontist's Point of View: Not Only a Matter of Deglutition

- **ID:** DEREGIBUS2021
- **Autores, año y revista:** Deregibus A; Parrini S; Domini MC; Colombini J; Castroflorio T. *Applied Sciences* 2021;11(6):2520.
- **DOI / PMID / URL:** DOI `10.3390/app11062520`; [artículo original abierto](https://www.mdpi.com/2076-3417/11/6/2520).
- **Tipo de estudio:** Observacional comparativo transversal (tipo casos y controles por fenotipo oclusal). **No es un ensayo aleatorizado** aunque el texto emplee «randomly divided» para describir grupos definidos por diagnóstico.
- **Población y tamaño muestral:** 100 niños de 6 a 12 años, clínica de ortodoncia en Turín; G1, 50 con clase III esquelética e hipoplasia maxilar; G2, 50 con clase I sin maloclusión. Edad media G1 8,9 (DE 1,9) y G2 8,5 (DE 2,1).
- **Definición diagnóstica y técnicas:** Exploración clínica por odontólogo y logopeda; cuestionario parental de respiración, alimentación, hábitos y enfermedades ORL; inspección en reposo, deglución y fonación; ejercicios observados `hold and pull` (punta y centro lingual contra el paladar durante apertura) y `chuck` (succión palatina, abrir, mantener y soltar). La descripción del criterio de frenillo corto es **apariencia clínica**, sin medición cuantitativa funcional/validación de una escala específica publicada en los métodos. El resumen y los métodos discrepan sobre presencia de mordida cruzada posterior: **PENDIENTE DE VERIFICAR** con autores si es crítico.
- **Criterio diagnóstico de anquiloglosia:** LONGITUD/ASPECTO: inspección de frenillo descrito como anormalmente corto. Los ejercicios evalúan otras funciones linguales, pero **no son el criterio diagnóstico para clasificar a los 14 participantes como anquiloglósicos**.
- **Variables de resultado:** Presencia de frenillo corto, posición de reposo alterada, deglución atípica, ejecución de `hold and pull` y `chuck`.
- **Resultados NUMÉRICOS verificados (tabla 2 del texto completo):**
  - Frenillo corto: **12/50 (24 %) G1 vs 2/50 (4 %) G2**, p = 0,004.
  - Posición lingual de reposo anómala: **38/50 (76 %) vs 16/50 (32 %)**, p < 0,05.
  - `Hold and pull` incorrecto: **31/50 (62 %) vs 21/50 (42 %)**, p = 0,05 (límite de significación reportado).
  - `Chuck` incorrecto: **24/50 (48 %) vs 8/50 (16 %)**, p = 0,001.
  - Deglución atípica: **32/50 (64 %) vs 26/50 (52 %)**, p = 0,234 (**sin diferencia estadísticamente significativa**).
- **Límites metodológicos / confusores:** Selección en clínica y comparación por tipo de maloclusión, no seguimiento longitudinal; diferencias en desarrollo y espacio intraoral, vía aérea, hábitos, intervenciones y genética no controladas mediante ajuste multivariable reportado; evaluación clínica de postura y ejercicios sin comprobación de reproducibilidad/cegamiento ni PSG. **La mandíbula o el maxilar ya configurados podrían afectar el espacio para la lengua**: causalidad inversa plausible, no estudiada.
- **Hallazgos contrarios o no significativos:** Deglución atípica sin diferencia. La existencia de alteración de reposo/exercicios no demuestra que el frenillo sea su causa, pues **solo 12/50** casos de clase III fueron clasificados como anquiloglósicos, frente a **38/50** con reposo alterado.
- **Conclusión que sí permite / que no permite:** Permite describir asociaciones contemporáneas entre fenotipo clase III y frenillo visualmente corto, reposo lingual y ejercicios de succión. **No** prueba que un frenillo anatómicamente corto cause clase III, que la movilidad funcional esté restringida en todos los casos ni que frenectomía modifique crecimiento.
- **Licencia y derechos:** Acceso abierto MDPI, **CC BY 4.0**. Resumen original; no se copian sus tablas/figuras ni PDF.
- **Estado de lectura:** **Texto completo abierto consultado el 03/11/2026**, incluida tabla 2 y métodos, [editor](https://www.mdpi.com/2076-3417/11/6/2520) y [PDF abierto](https://doi.org/10.3390/app11062520). La anotación anterior «solo metadatos» ha quedado subsanada.

## Figuras

No incorporadas. [Fuente original](https://doi.org/10.3390/app11062520).

---

<!-- archivo: fuentes/articulos/2021-genna-ecografia-lengua.md -->
# Estudio: Quantitative imaging of tongue kinematics during infant feeding and adult swallowing reveals highly conserved patterns

- **ID:** GENNA2021
- **Autores, año y revista:** Genna CW; Saperstein Y; Siegel SA et al.. Physiol Rep 2021;9(3):e14685.
- **DOI / PMID / URL:** DOI `10.14814/phy2.14685`; PMID `33547883`; https://pmc.ncbi.nlm.nih.gov/articles/PMC7866619/
- **Tipo de estudio:** Estudio metodológico con casos ilustrativos.
- **Población y tamaño muestral:** Pocos lactantes y un adulto. Número PENDIENTE DE VERIFICAR.
- **Definición diagnóstica y técnicas:** Ecografía con análisis cuantitativo del movimiento de la lengua.
- **Criterio diagnóstico de anquiloglosia:** Selección clínica de casos con frenillo lingual o labial restrictivo; escala PENDIENTE DE VERIFICAR.
- **Variables de resultado:** Cinemática de la lengua al mamar, con biberón y al tragar.
- **Resultados NUMÉRICOS verificados:** Describe mejor motilidad tras frenotomía en lactantes con frenillo lingual o labial restrictivo, y movimientos peristálticos de la lengua en el adulto.
- **Límites metodológicos / confusores:** Casos aislados.
- **Hallazgos contrarios o no significativos:** No aplica.
- **Conclusión que sí permite / que no permite:** Sí: Citar un método objetivo para medir la función de la lengua. No: Sacar conclusiones de eficacia.
- **Licencia y derechos:** Acceso abierto en PMC. Licencia PENDIENTE DE VERIFICAR.
- **Estado de lectura:** Resumen PubMed y texto completo revisados el 17/10/2026.

## Figuras

Licencia del artículo: CC BY 4.0. Figuras en PubMed Central (PMC7866619).

- **Figura 1.** Diagrama de flujo del análisis de la cinemática de la lengua en ecografía. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7866619/figure/phy214685-fig-0001/). Copia local: figuras/GENNA2021-fig1.jpg.
- **Figura 2.** Seguimiento del contorno de lengua y paladar en los fotogramas. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7866619/figure/phy214685-fig-0002/). Copia local: figuras/GENNA2021-fig2.jpg.
- **Figura 3.** Lactante con tortícolis: lengua al pecho frente a biberón (ritmo irregular con biberón). [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7866619/figure/phy214685-fig-0003/). Copia local: figuras/GENNA2021-fig3.jpg.
- **Figura 4.** Lactante con frenillo lingual antes y después de la frenotomía. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7866619/figure/phy214685-fig-0004/). Copia local: figuras/GENNA2021-fig4.jpg.
- **Figura 5.** Lactante con frenillo labial restrictivo antes y después de la frenotomía labial. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7866619/figure/phy214685-fig-0005/). Copia local: figuras/GENNA2021-fig5.jpg.
- **Figura 6.** Lactante con disfagia: falta la peristalsis posterior de la lengua. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7866619/figure/phy214685-fig-0006/). Copia local: figuras/GENNA2021-fig6.jpg.
- **Figura 7.** Adulto tragando agua: movimientos peristálticos anteriores y posteriores. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7866619/figure/phy214685-fig-0007/). Copia local: figuras/GENNA2021-fig7.jpg.

Crédito: figuras de Genna CW; Saperstein Y; Siegel SA et al (PMC7866619), CC BY 4.0. Las copias locales no se han modificado.

---

<!-- archivo: fuentes/articulos/2021-lefort-abm-posicionamiento.md -->
# Estudio: Academy of Breastfeeding Medicine Position Statement on Ankyloglossia in Breastfeeding Dyads

- **ID:** LEFORT2021
- **Autores, año y revista:** LeFort Y; Evans A; Livingstone V; Douglas P; Dahlquist N; Donnelly B; Leeper K; Harley E; Lappin S. Breastfeed Med 2021;16(4):278-281.
- **DOI / PMID / URL:** DOI `10.1089/bfm.2021.29179.ylf`; PMID `33852342`. PDF de la ABM: https://abm.memberclicks.net/assets/Anklyloglossia%20position%20statement%202021.pdf
- **Tipo de estudio:** Posicionamiento de una sociedad médica internacional de lactancia.
- **Población y tamaño muestral:** Díadas madre-lactante con dificultades de lactancia.
- **Definición diagnóstica y técnicas:** Resumen de la evidencia.
- **Criterio diagnóstico de anquiloglosia:** NO PROPONE NINGUNO. Dice que las herramientas publicadas varían mucho en sus componentes y en su fiabilidad, y que ninguna debe usarse sola para decidir una frenotomía: la decisión exige una valoración clínica experta de la lactancia, también de la madre.
- **Variables de resultado:** Valoración e indicación de la frenotomía.
- **Resultados NUMÉRICOS verificados:** Ante un frenillo restrictivo, la frenotomía puede aumentar el confort materno y la transferencia de leche y evitar el abandono precoz de la lactancia. El frenillo labial superior es una estructura normal: intervenirlo no se puede recomendar. No debe hacerse cirugía de «frenillos bucales». La decisión exige mucha habilidad clínica.
- **Límites metodológicos / confusores:** Posicionamiento, no protocolo ni revisión sistemática. Qué dice exactamente sobre el «frenillo posterior»: `PENDIENTE DE VERIFICAR`.
- **Hallazgos contrarios o no significativos:** No aplica.
- **Conclusión que sí permite / que no permite:** Sí: Decir que la ABM no avala ninguna herramienta diagnóstica como criterio único. No: Usarlo fuera de la lactancia.
- **Licencia y derechos:** Derechos del editor. Aquí solo resumen propio.
- **Estado de lectura:** Texto completo (PDF de la ABM) leído el 02/11/2026. Búsqueda de actualización del 02/11/2026.

## Figuras

Figuras no revisadas. [Ver el documento](https://doi.org/10.1089/bfm.2021.29179.ylf).

---

<!-- archivo: fuentes/articulos/2021-maya-enero-prevalencia-neonatal-espana.md -->
# Estudio: Prevalence of neonatal ankyloglossia in a tertiary care hospital in Spain: a transversal cross-sectional study

- **ID:** MAYAENERO2021
- **Autores, año y revista:** Maya-Enero S; Pérez-Pérez M; Ruiz-Guzmán L et al.. Eur J Pediatr 2021;180(3):751-757.
- **DOI / PMID / URL:** DOI `10.1007/s00431-020-03781-7`; PMID `32803423`
- **Tipo de estudio:** Transversal de todos los nacidos en 2018.
- **Población y tamaño muestral:** 1.392 recién nacidos de un hospital terciario español.
- **Definición diagnóstica y técnicas:** Búsqueda activa del frenillo.
- **Criterio diagnóstico de anquiloglosia:** MIXTO. Hazelbaker para aspecto y función; «clínicamente significativa» si había dolor o lesiones del pezón o dificultad de agarre. Tipos de Coryllos como descriptivo.
- **Variables de resultado:** Prevalencia y tipo.
- **Resultados NUMÉRICOS verificados:** Frenillo en 645 (46,3 %); sintomáticos 453 (70,2 % de ellos), 32,5 % del total. Coryllos: tipo 1 7,0 %, tipo 2 35,6 %, tipo 3 49,8 %, tipo 4 6,5 %.
- **Límites metodológicos / confusores:** Un solo centro. La búsqueda activa sube la detección.
- **Hallazgos contrarios o no significativos:** Cifras muy por encima de otras series.
- **Conclusión que sí permite / que no permite:** Sí: Decir que buscando de forma activa, incluidas las formas posteriores, la prevalencia es mucho mayor de lo descrito. No: Equiparar frenillo visible con restricción funcional.
- **Licencia y derechos:** Derechos del editor. Aquí solo metadatos y resumen propio.
- **Estado de lectura:** Resumen PubMed y texto completo revisados el 17/10/2026.

## Figuras

Licencia: derechos del editor (no se copian imágenes). Leyendas leídas en el texto completo; puede haber más figuras que las listadas.

- **Figura 1.** Tipos de anquiloglosia según Coryllos. [Ver en el artículo](https://doi.org/10.1007/s00431-020-03781-7), figura 1.
- **Figura 2.** Herramienta de Hazelbaker (HATLFF). [Ver en el artículo](https://doi.org/10.1007/s00431-020-03781-7), figura 2.
- **Figura 3.** Diagrama de pacientes. [Ver en el artículo](https://doi.org/10.1007/s00431-020-03781-7), figura 3.

---

<!-- archivo: fuentes/articulos/2021-oh-bruxismo-sueno-ninos.md -->
# Estudio: Determinants of probable sleep bruxism in a pediatric mixed dentition population: a multivariate analysis of mouth vs. nasal breathing, tongue mobility, and tonsil size

- **ID:** OH2021B
- **Autores, año y revista:** Oh JS; Zaghi S; Ghodousi N et al.. Sleep Med 2021.
- **DOI / PMID / URL:** DOI `10.1016/j.sleep.2020.11.007`; PMID `33291022`
- **Tipo de estudio:** Transversal.
- **Población y tamaño muestral:** 96 niños de 6 a 12 años (UCLA, 2018-2019).
- **Definición diagnóstica y técnicas:** Encuesta a padres, desgaste dental, amígdalas, movilidad lingual y obstrucción nasal.
- **Criterio diagnóstico de anquiloglosia:** Movilidad lingual medida; escala PENDIENTE DE VERIFICAR (no consta en el resumen).
- **Variables de resultado:** Bruxismo probable del sueño.
- **Resultados NUMÉRICOS verificados:** Bruxismo probable en 23 de 96 (24 %). Sin ninguno de los tres hallazgos (amígdalas, lengua restringida, obstrucción nasal): 8,6 %; con los tres: 90,9 % (p<0,0001).
- **Límites metodológicos / confusores:** Transversal; bruxismo por informe de padres y desgaste.
- **Hallazgos contrarios o no significativos:** 5 de los 23 no tenían ninguno de los tres hallazgos.
- **Conclusión que sí permite / que no permite:** Sí: Decir que amígdalas grandes, lengua restringida y nariz obstruida se asocian, y parecen sumarse, al bruxismo infantil. No: Afirmar causa.
- **Licencia y derechos:** Derechos del editor. Aquí solo metadatos y resumen propio.
- **Estado de lectura:** Resumen PubMed revisado el 17/10/2026.

## Figuras

Figuras no revisadas: el texto completo no está en acceso abierto en PMC. [Ver el artículo](https://doi.org/10.1016/j.sleep.2020.11.007).

---

<!-- archivo: fuentes/articulos/2021-oh-fairest6.md -->
# Estudio: Determinants of Sleep-Disordered Breathing During the Mixed Dentition: Development of a Functional Airway Evaluation Screening Tool (FAIREST-6)

- **ID:** OH2021
- **Autores, año y revista:** Oh JS; Zaghi S; Peterson C et al.. Pediatr Dent 2021;43(4):262-272.
- **DOI / PMID / URL:** PMID `34467840`; sin DOI
- **Tipo de estudio:** Estudio transversal para crear una herramienta de cribado.
- **Población y tamaño muestral:** 96 niños en dentición mixta, edad media 8,9 años, clínica dental pediátrica de UCLA.
- **Definición diagnóstica y técnicas:** Exploración dental rutinaria por residentes. Cuestionario de sueño SDSC rellenado por los padres.
- **Criterio diagnóstico de anquiloglosia:** La anquiloglosia es uno de los seis factores. Cómo se midió: PENDIENTE DE VERIFICAR (texto completo no consultado).
- **Variables de resultado:** Puntuación SDSC frente a hallazgos funcionales, extraorales e intraorales.
- **Resultados NUMÉRICOS verificados:** Seis factores asociados a peor SDSC (P<0,01): respiración oral, tensión del mentoniano, amígdalas grandes, anquiloglosia, desgaste dental y paladar estrecho. El OR 19 del desgaste dental que cita Zaghi en vídeo no está en el resumen: PENDIENTE DE VERIFICAR.
- **Límites metodológicos / confusores:** Muestra pequeña de un solo centro. Sueño medido por cuestionario, sin polisomnografía. Transversal.
- **Hallazgos contrarios o no significativos:** No se describen en el resumen.
- **Conclusión que sí permite / que no permite:** Sí: Usar los seis signos como lista de cribado en consulta dental. No: Diagnosticar apnea ni afirmar que la anquiloglosia cause trastorno del sueño.
- **Licencia y derechos:** Derechos del editor. Aquí solo metadatos y resumen propio.
- **Estado de lectura:** Resumen PubMed revisado el 17/10/2026. Sin DOI en PubMed.

## Figuras

Figuras no revisadas: el texto completo no está en acceso abierto en PMC. [Ver el artículo](https://pubmed.ncbi.nlm.nih.gov/34467840/).

---

<!-- archivo: fuentes/articulos/2021-orabi-extracciones-via-aerea.md -->
# Estudio: Pharyngeal airway dimensional changes after orthodontic treatment with premolar extractions: A systematic review with meta-analysis

- **ID:** ORABI2021
- **Autores, año y revista:** Orabi N; Flores-Mir C; Elshebiny T; Elkordy S; Palomo JM. Am J Orthod Dentofacial Orthop 2021;160(4):503-515.e3.
- **DOI / PMID / URL:** DOI `10.1016/j.ajodo.2021.03.013`; PMID `34479766`
- **Tipo de estudio:** Revisión sistemática y metaanálisis. PROSPERO CRD42018089924.
- **Población y tamaño muestral:** 7 estudios: 268 tratados con extracciones y 342 controles sin extracciones (edad media 19 años).
- **Definición diagnóstica y técnicas:** Siete bases de datos y literatura gris.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA: el estudio no diagnostica anquiloglosia.
- **Variables de resultado:** Volumen faríngeo total y por zonas; área transversal mínima.
- **Resultados NUMÉRICOS verificados:** Sin diferencias significativas salvo un aumento de volumen orofaríngeo de 0,41 cm³ (IC 0,05-0,80) con extracciones, de relevancia clínica dudosa. Nivel de evidencia muy bajo.
- **Límites metodológicos / confusores:** Riesgo de sesgo moderado a alto. Pocos estudios.
- **Hallazgos contrarios o no significativos:** Ver O-003.
- **Conclusión que sí permite / que no permite:** Sí: Decir que no hay pruebas sólidas de que las extracciones reduzcan la vía aérea medida. No: Decir que está demostrado que no la afectan.
- **Licencia y derechos:** Derechos del editor. Aquí solo metadatos y resumen propio.
- **Estado de lectura:** Resumen PubMed revisado el 17/10/2026.

## Figuras

Figuras no revisadas: el texto completo no está en acceso abierto en PMC. [Ver el artículo](https://doi.org/10.1016/j.ajodo.2021.03.013).

---

<!-- archivo: fuentes/articulos/2021-rashid-odi-diagnostico.md -->
# Estudio: The Value of Oxygen Desaturation Index for Diagnosing Obstructive Sleep Apnea: A Systematic Review

- **ID:** RASHID2021
- **Autores, año y revista:** Rashid NH; Zaghi S; Scapuccin M et al.. Laryngoscope 2021;131:440-447.
- **DOI / PMID / URL:** DOI `10.1002/lary.28663`; PMID `32333683`
- **Tipo de estudio:** Revisión sistemática (con metaanálisis si lo indica el título).
- **Población y tamaño muestral:** 8 estudios, 1.924 pacientes.
- **Definición diagnóstica y técnicas:** Búsqueda en varias bases de datos.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA: el estudio no diagnostica anquiloglosia.
- **Variables de resultado:** IAH, saturación mínima y somnolencia, salvo que se indique otra cosa.
- **Resultados NUMÉRICOS verificados:** Sensibilidad 32-98,5 % y especificidad 47,7-98 %. ODI 4 % ≥15/h con especificidad 75-98 %.
- **Límites metodológicos / confusores:** Estudios primarios pequeños y sobre todo series de casos. Zaghi es coautor.
- **Hallazgos contrarios o no significativos:** No se describen en el resumen.
- **Conclusión que sí permite / que no permite:** Sí: Plantear el ODI 4 % ≥15/h como apoyo al diagnóstico en adultos. No: Sustituir la polisomnografía: hay mucha heterogeneidad.
- **Licencia y derechos:** Derechos del editor. Aquí solo metadatos y resumen propio.
- **Estado de lectura:** Resumen PubMed revisado el 17/10/2026.

## Figuras

Figuras no revisadas: el texto completo no está en acceso abierto en PMC. [Ver el artículo](https://doi.org/10.1002/lary.28663).

---

<!-- archivo: fuentes/articulos/2021-rodriguez-alcala-cuchara-fuerza.md -->
# Estudio: Assessment of muscular tone of the tongue using a digital measure spoon in a healthy population: A pilot study

- **ID:** RODRIGUEZALCALA2021
- **Autores, año y revista:** Rodríguez-Alcalá L; Martín-Lagos Martínez J; O'Connor-Reina C; Plaza G. PLoS One 2021;16(2):e0245901.
- **DOI / PMID / URL:** DOI `10.1371/journal.pone.0245901`; PMID `33600465`; https://pmc.ncbi.nlm.nih.gov/articles/PMC7891707/
- **Tipo de estudio:** Estudio piloto de validación frente a IOPI.
- **Población y tamaño muestral:** 20 adultos sanos de 20 a 70 años.
- **Definición diagnóstica y técnicas:** Cuchara digital (Tongue Digital Spoon) frente a IOPI.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA: el estudio no diagnostica anquiloglosia.
- **Variables de resultado:** Fuerza lingual en g/cm².
- **Resultados NUMÉRICOS verificados:** Media 115,99 g/cm² en jóvenes, 98,47 en mediana edad y 84,23 en mayores. Correlación con IOPI r=0,69 (p<0,001).
- **Límites metodológicos / confusores:** Piloto con 20 personas.
- **Hallazgos contrarios o no significativos:** No aplica.
- **Conclusión que sí permite / que no permite:** Sí: Usar la cuchara como medida sencilla de fuerza lingual. No: Darla por plenamente validada.
- **Licencia y derechos:** Acceso abierto en PMC. Licencia PENDIENTE DE VERIFICAR.
- **Estado de lectura:** Resumen PubMed y texto completo revisados el 17/10/2026.

## Figuras

Licencia del artículo: CC BY 4.0. Figuras en PubMed Central (PMC7891707).

- **Figura 1.** La cuchara digital con sus botones de encendido, tara y retención. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7891707/figure/pone.0245901.g001/). Copia local: figuras/RODRIGUEZALCALA2021-fig1.jpg.
- **Figura 2.** Reverso de la cuchara con la pegatina de 1 cm² en el punto de apoyo. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7891707/figure/pone.0245901.g002/). Copia local: figuras/RODRIGUEZALCALA2021-fig2.jpg.
- **Figura 3.** Técnica de medida con la cuchara en la boca. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7891707/figure/pone.0245901.g003/).
- **Figura 4.** Distribución de las medidas de la cuchara y del IOPI por grupo de edad. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7891707/figure/pone.0245901.g004/). Copia local: figuras/RODRIGUEZALCALA2021-fig4.jpg.
- **Figura 5.** Correlación entre IOPI y cuchara (r=0,69). [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7891707/figure/pone.0245901.g005/). Copia local: figuras/RODRIGUEZALCALA2021-fig5.jpg.

Crédito: figuras de Rodríguez-Alcalá L; Martín-Lagos Martínez J; O'Connor-Reina C; Plaza G (PMC7891707), CC BY 4.0. Las copias locales no se han modificado.

La figura 3 muestra a una persona: solo enlace.

---

<!-- archivo: fuentes/articulos/2021-slagter-brief-lactancia-reflujo.md -->
# Estudio: Effect of frenotomy on breastfeeding and reflux: results from the BRIEF prospective longitudinal cohort study

- **ID:** SLAGTER2021
- **Autores, año y revista:** Slagter KW; Raghoebar GM; Hamming I et al.. Clin Oral Investig 2021;25(6):3431-3439.
- **DOI / PMID / URL:** DOI `10.1007/s00784-020-03665-y`; PMID `33315177`; https://pmc.ncbi.nlm.nih.gov/articles/PMC8137608/
- **Tipo de estudio:** Cohorte prospectiva sin control (ISRCTN64428423).
- **Población y tamaño muestral:** 175 madres lactantes; 146 a los 6 meses.
- **Definición diagnóstica y técnicas:** Valoración oral estandarizada con formulario propio; BSES-SF, dolor (EVA) e I-GERQ-R antes y a 1 semana, 1 y 6 meses.
- **Criterio diagnóstico de anquiloglosia:** Formulario propio anatómico (texto completo menciona Coryllos y Kotlow para frenillo labial). Detalle: PENDIENTE DE VERIFICAR.
- **Variables de resultado:** Autoeficacia, dolor del pezón, reflujo.
- **Resultados NUMÉRICOS verificados:** Mejora significativa a la semana en las tres escalas; se mantiene al mes en BSES-SF e I-GERQ-R y a los 6 meses en I-GERQ-R. 60,7 % seguía con lactancia a los 6 meses. Sin complicaciones.
- **Límites metodológicos / confusores:** Sin control: el reflujo del lactante mejora solo con el tiempo.
- **Hallazgos contrarios o no significativos:** No aplica.
- **Conclusión que sí permite / que no permite:** Sí: Describir la evolución tras frenotomía. No: Atribuir la mejoría del reflujo a la cirugía.
- **Licencia y derechos:** Acceso abierto en PMC. Licencia PENDIENTE DE VERIFICAR.
- **Estado de lectura:** Resumen PubMed y texto completo revisados el 17/10/2026.

## Figuras

Licencia del artículo: CC BY 4.0. Figuras en PubMed Central (PMC8137608).

- **Figura 1.** Diagrama CONSORT de participantes. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC8137608/figure/Fig1/). Copia local: figuras/SLAGTER2021-fig1.jpg.
- **Figura 2.** Fotos de tipos de inserción del frenillo labial y lingual en lactantes. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC8137608/figure/Fig2/).

Crédito: figuras de Slagter KW; Raghoebar GM; Hamming I et al (PMC8137608), CC BY 4.0. Las copias locales no se han modificado.

La figura 2 es de bocas de lactantes: solo enlace.

---

<!-- archivo: fuentes/articulos/2021-unkel-herramientas-encuesta.md -->
# Estudio: Evaluation of Anatomic Features and Assessment Tools to Determine Treatment of Ankyloglossia

- **ID:** UNKEL2021
- **Autores, año y revista:** Unkel JH; Martin C; Berry EJ et al.. J Dent Child (Chic) 2021;88(3):150-155.
- **DOI / PMID / URL:** PMID `34937624`; sin DOI
- **Tipo de estudio:** Encuesta de nueve preguntas con tres casos.
- **Población y tamaño muestral:** 404 odontopediatras y otorrinolaringólogos de EE. UU.
- **Definición diagnóstica y técnicas:** Encuesta.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA. Describe lo que usan: Hazelbaker la más citada, después LATCH y Bristol.
- **Variables de resultado:** Herramientas y rasgos anatómicos usados para indicar frenotomía.
- **Resultados NUMÉRICOS verificados:** Rasgos más usados: aspecto de la lengua al elevarla, protrusión, longitud y tipo de frenillo.
- **Límites metodológicos / confusores:** Encuesta, sesgo de respuesta.
- **Hallazgos contrarios o no significativos:** No aplica.
- **Conclusión que sí permite / que no permite:** Sí: Decir que en la práctica se decide sobre todo por el aspecto. No: Concluir qué herramienta es mejor.
- **Licencia y derechos:** Derechos del editor. Aquí solo metadatos y resumen propio.
- **Estado de lectura:** Resumen PubMed y texto completo revisados el 17/10/2026.

## Figuras

Licencia: derechos del editor (no se copian imágenes). Leyendas leídas en el texto completo; puede haber más figuras que las listadas.

- **Figura 1.** Caso de frenillo en cordón. [Ver en el artículo](https://pubmed.ncbi.nlm.nih.gov/34937624/), figura 1.
- **Figura 2.** Caso de frenillo en hebra. [Ver en el artículo](https://pubmed.ncbi.nlm.nih.gov/34937624/), figura 2.
- **Figura 3.** Caso de frenillo en membrana. [Ver en el artículo](https://pubmed.ncbi.nlm.nih.gov/34937624/), figura 3.

---

<!-- archivo: fuentes/articulos/2021-zaghi-trmr-lps.md -->
# Zaghi et al. (2021) — Assessment of posterior tongue mobility using lingual-palatal suction

- DOI: `10.1111/joor.13144`; PMID: `33386612`; https://pmc.ncbi.nlm.nih.gov/articles/PMC8247966/
- Diseño: estudio sobre utilidad de TRMR-LPS como complemento de TRMR-TIP.
- Punto metodológico: TIP evalúa principalmente punta/anterior; LPS intenta caracterizar elevación funcional del cuerpo lingual posterior mediante succión palatina.
- Limitación: medir función no establece por sí mismo que el frenillo sea la única causa de una puntuación reducida.
- Criterio diagnóstico de anquiloglosia: FUNCIONAL. TRMR con punta a la papila (TIP) y con succión lingual-palatina (LPS) en 611 sujetos de 3 a 83 años. LPS se correlacionó mucho mejor que TIP con la dificultad para elevar el cuerpo de la lengua (R² 0,31 frente a 0,05; resumen PubMed revisado el 17/10/2026).
- Complemento desde el texto completo (17/10/2026): escala de grados del texto completo. TRMR-TIP: grado 1 >80 %, 2 de 50 a 80 %, 3 <50 %, 4 <25 %. TRMR-LPS: grado 1 >60 %, 2 de 30 a 60 %, 3 <30 %, 4 <5 % o no puede sostenerla. Valores medios de 611 sujetos: apertura cómoda 43,7 ± 7,3 mm, TRMR-TIP 61,5 %, TRMR-LPS 41,4 %; de 12 a 17 años 61,0 % y 45,4 %; de 18 a 35 años 67,7 % y 46,1 %. Los autores avisan de que la medida puede ser poco fiable de 3 a 11 años y con apertura limitada. Voluntarios reclutados entre amigos, familia, colegas y clientes de los investigadores. Estudio dirigido y financiado por The Breathe Institute.
- Estado: artículo cargado previamente por investigadora en su biblioteca; aquí se enlaza DOI en lugar de copiar PDF. Revisión detallada pendiente.

## Figuras

Licencia del artículo: CC BY 4.0. Figuras en PubMed Central (PMC8247966).

- **Figura 1.** Cómo se mide: apertura cómoda, punta a la papila (TIP) y succión (LPS), con regla. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC8247966/figure/joor13144-fig-0001/).
- **Figura 2.** Casos de restricción moderada y grave en TIP y LPS. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC8247966/figure/joor13144-fig-0002/).
- **Figura 3.** Distribución de TRMR-TIP y TRMR-LPS en los 611 sujetos. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC8247966/figure/joor13144-fig-0003/). Copia local: figuras/ZAGHI2021-fig3.jpg.
- **Figura 4.** Diagrama de cajas de TRMR-TIP y TRMR-LPS. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC8247966/figure/joor13144-fig-0004/). Copia local: figuras/ZAGHI2021-fig4.jpg.
- **Figura 5.** Escala funcional actualizada: grados 1 a 4 para TIP y LPS, con fotos de ejemplo. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC8247966/figure/joor13144-fig-0005/).

Crédito: figuras de Zaghi et al. (2021): Assessment of posterior tongue mobility using lingual-palatal suction (PMC8247966), CC BY 4.0. Las copias locales no se han modificado.

Las figuras 1, 2 y 5 llevan fotos de bocas: solo enlace. La 5 es la escala de grados que se cita en todo el repositorio.

---

<!-- archivo: fuentes/articulos/2022-aapd-politica-frenillo.md -->
# Estudio: Policy on Management of the Frenulum in Pediatric Patients (American Academy of Pediatric Dentistry)

- **ID:** AAPD2022
- **Autores, año y revista:** American Academy of Pediatric Dentistry (AAPD), Council on Clinical Affairs. Adoptada en 2019, revisada en 2022. The Reference Manual of Pediatric Dentistry 2025:80-5.
- **DOI / PMID / URL:** PDF: https://www.aapd.org/globalassets/media/policies_guidelines/p_mgmt_frenulum.pdf
- **Tipo de estudio:** Política (posicionamiento) de una sociedad de odontopediatría.
- **Población y tamaño muestral:** Pacientes pediátricos.
- **Definición diagnóstica y técnicas:** Revisión de la literatura.
- **Criterio diagnóstico de anquiloglosia:** NO PROPONE NINGUNO. Dice que se han propuesto clasificaciones anatómicas y funcionales pero «none has been universally accepted», que ningún dato anatómico aislado del frenillo se correlaciona directamente con la función, y que la capacidad de elevar la lengua, más que de sacarla, es la cualidad más importante.
- **Variables de resultado:** Lactancia, habla, frenillo labial superior.
- **Resultados NUMÉRICOS verificados:** Apoya investigar la relación causal entre anquiloglosia y problemas de lactancia o habla. No avala liberar el frenillo labial superior solo por su aspecto. Sugiere valoración por logopeda antes de liberar por motivos de habla. Texto exacto de cada punto de la política: `PENDIENTE DE VERIFICAR` en el apartado «Policy statement».
- **Límites metodológicos / confusores:** Posicionamiento, no revisión sistemática.
- **Hallazgos contrarios o no significativos:** No aplica.
- **Conclusión que sí permite / que no permite:** Sí: Decir que la AAPD reconoce que no hay una clasificación diagnóstica aceptada por todos. No: Atribuirle un criterio diagnóstico propio.
- **Licencia y derechos:** Documento de la AAPD. Aquí solo resumen propio.
- **Estado de lectura:** Texto completo (PDF) leído el 02/11/2026, salvo el detalle de los puntos finales. Búsqueda de actualización del 02/11/2026.

## Figuras

Figuras no revisadas. [Ver el documento](https://www.aapd.org/globalassets/media/policies_guidelines/p_mgmt_frenulum.pdf).

---

<!-- archivo: fuentes/articulos/2022-al-taai-cambios-craneofaciales-13-62.md -->
# Estudio: Craniofacial changes from 13 to 62 years of age

- **ID:** ALTAAI2022
- **Autores, año y revista:** Al-Taai N; Persson M; Ransjö M et al.. Eur J Orthod 2022;44(5):556-565.
- **DOI / PMID / URL:** DOI `10.1093/ejo/cjac011`; PMID `35348638`; https://pmc.ncbi.nlm.nih.gov/articles/PMC9486882/
- **Tipo de estudio:** Cohorte longitudinal sin tratamiento.
- **Población y tamaño muestral:** 30 personas con clase I normal, radiografiadas a los 13, 16, 31 y 62 años.
- **Definición diagnóstica y técnicas:** 53 parámetros cefalométricos.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA: el estudio no diagnostica anquiloglosia.
- **Variables de resultado:** Cambios esqueléticos, dentales y de tejidos blandos.
- **Resultados NUMÉRICOS verificados:** Crecimiento anterior de los maxilares de 13 a 16 años; retrognatismo de 31 a 62; rotación posterior de la mandíbula y retroinclinación de incisivos en la edad adulta.
- **Límites metodológicos / confusores:** Muestra pequeña a los 62 años.
- **Hallazgos contrarios o no significativos:** No aplica.
- **Conclusión que sí permite / que no permite:** Sí: Decir que la cara sigue cambiando hasta la sexta década. No: Extrapolar a pacientes con maloclusión.
- **Licencia y derechos:** Acceso abierto en PMC. Licencia PENDIENTE DE VERIFICAR.
- **Estado de lectura:** Resumen PubMed y texto completo revisados el 17/10/2026.

## Figuras

Licencia del artículo: CC BY-NC-ND 4.0 (no permite copiar aquí). Figuras en PubMed Central (PMC9486882).

- **Figura 1.** Diagrama de participantes y pérdidas en los cuatro tiempos. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC9486882/figure/F1/).
- **Figura 2.** Puntos y planos cefalométricos usados. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC9486882/figure/F2/).
- **Figura 3.** Cambios esqueléticos de base de cráneo, sagitales y verticales. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC9486882/figure/F3/).
- **Figura 4.** Cambios en las dimensiones de los maxilares. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC9486882/figure/F4/).
- **Figura 5.** Cambios en las relaciones dentales. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC9486882/figure/F5/).
- **Figura 6.** Cambios del perfil blando. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC9486882/figure/F6/).
- **Figura 7.** Superposición cefalométrica de los cambios de 13 a 62 años. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC9486882/figure/F7/).

---

<!-- archivo: fuentes/articulos/2022-baxter-frenillo-labial.md -->
# Estudio: Safety and efficacy of maxillary labial frenectomy in children: A retrospective comparative cohort study

- **ID:** BAXTER2022
- **Autores, año y revista:** Baxter RT; Zaghi S; Lashley AP. Int Orthod 2022;20(2):100630.
- **DOI / PMID / URL:** DOI `10.1016/j.ortho.2022.100630`; PMID `35283058`
- **Tipo de estudio:** Cohorte retrospectiva comparativa. Autofinanciado.
- **Población y tamaño muestral:** 109 niños con frenillo labial superior hipertrófico: 95 en dentición temporal (media 1,9 años) y 14 en mixta (media 8,1 años). Seguimiento medio 18 meses.
- **Definición diagnóstica y técnicas:** Frenectomía con láser de diodo y CO2. Diastema medido en fotos intraorales calibradas.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA a la anquiloglosia lingual. Estudia el frenillo labial superior. Cómo se definió «hipertrófico»: PENDIENTE DE VERIFICAR.
- **Variables de resultado:** Anchura del diastema antes y después. Efectos adversos.
- **Resultados NUMÉRICOS verificados:** Diastema reducido en el 94,7 % (temporal; cierre medio -1,4 mm) y en el 92,9 % (mixta; -1,8 mm). De los diastemas >2 mm, mejoraron a <2 mm el 74,5 % (temporal) y el 75 % (mixta). Solo dolor e inflamación leves.
- **Límites metodológicos / confusores:** Retrospectivo. Sin grupo sin tratar en el resumen pese al título «comparativo». Medida en fotografía. Los diastemas en dentición temporal pueden cerrarse solos con el crecimiento.
- **Hallazgos contrarios o no significativos:** No se describen en el resumen.
- **Conclusión que sí permite / que no permite:** Sí: Decir que la frenectomía labial temprana no impidió el cierre del diastema en esta serie. No: Decir que la frenectomía cierra el diastema: falta comparación con la evolución natural.
- **Licencia y derechos:** Derechos del editor. Aquí solo metadatos y resumen propio.
- **Estado de lectura:** Resumen PubMed revisado el 17/10/2026.

## Figuras

Figuras no revisadas: el texto completo no está en acceso abierto en PMC. [Ver el artículo](https://doi.org/10.1016/j.ortho.2022.100630).

---

<!-- archivo: fuentes/articulos/2022-cruz-prevalencia-herramientas.md -->
# Estudio: Prevalence of ankyloglossia according to different assessment tools: A meta-analysis

- **ID:** CRUZ2022
- **Autores, año y revista:** Cruz PV; Souza-Oliveira AC; Notaro SQ et al.. J Am Dent Assoc 2022;153(11):1026-1040.e31.
- **DOI / PMID / URL:** DOI `10.1016/j.adaj.2022.07.011`; PMID `36307175`
- **Tipo de estudio:** Revisión sistemática y metaanálisis de prevalencia. GRADE.
- **Población y tamaño muestral:** 71 estudios transversales y de cohortes.
- **Definición diagnóstica y técnicas:** Nueve bases de datos hasta noviembre de 2021.
- **Criterio diagnóstico de anquiloglosia:** MIXTO por diseño: compara siete herramientas diagnósticas distintas.
- **Variables de resultado:** Prevalencia por herramienta, edad y sexo.
- **Resultados NUMÉRICOS verificados:** Prevalencia global 5 % (IC 4-5 %); de 2 % con herramienta inespecífica a 20 % con Coryllos. Lactantes 7 %. Razón niños/niñas 1,34 (certeza muy baja).
- **Límites metodológicos / confusores:** Heterogeneidad. La prevalencia depende de la herramienta.
- **Hallazgos contrarios o no significativos:** No aplica.
- **Conclusión que sí permite / que no permite:** Sí: Decir que la cifra de prevalencia depende sobre todo del instrumento usado. No: Dar una prevalencia única.
- **Licencia y derechos:** Derechos del editor. Aquí solo metadatos y resumen propio.
- **Estado de lectura:** Resumen PubMed y texto completo revisados el 17/10/2026.

## Figuras

Licencia: derechos del editor (no se copian imágenes). Leyendas leídas en el texto completo; puede haber más figuras que las listadas.

- **Figura 1.** Diagrama PRISMA. [Ver en el artículo](https://doi.org/10.1016/j.adaj.2022.07.011), figura 1.
- **Figura 2.** Metaanálisis de prevalencia por herramienta diagnóstica. [Ver en el artículo](https://doi.org/10.1016/j.adaj.2022.07.011), figura 2.

---

<!-- archivo: fuentes/articulos/2022-dellolio-frenotomia-laser-neonatos.md -->
# Estudio: Lingual laser frenotomy in newborns with ankyloglossia: a prospective cohort study

- **ID:** DELLOLIO2022
- **Autores, año y revista:** Dell'Olio F; Baldassarre ME; Russo FG et al.. Ital J Pediatr 2022;48(1):163.
- **DOI / PMID / URL:** DOI `10.1186/s13052-022-01357-9`; PMID `36064609`; https://pmc.ncbi.nlm.nih.gov/articles/PMC9446865/
- **Tipo de estudio:** Cohorte prospectiva sin control.
- **Población y tamaño muestral:** 56 recién nacidos con anquiloglosia.
- **Definición diagnóstica y técnicas:** Frenotomía con láser de diodo bajo anestesia tópica. Controles a 7 y 30 días.
- **Criterio diagnóstico de anquiloglosia:** MIXTO. Coryllos más Hazelbaker.
- **Variables de resultado:** Dolor (CRIES), complicaciones, cicatrización, lactancia, peso, dolor del pezón.
- **Resultados NUMÉRICOS verificados:** Dolor intraoperatorio medio 5,7 que cedía en 30 min. Cicatrización completa a los 30 días. Mejora significativa de lactancia y dolor del pezón (p<0,05).
- **Límites metodológicos / confusores:** Sin control. Un centro.
- **Hallazgos contrarios o no significativos:** No aplica.
- **Conclusión que sí permite / que no permite:** Sí: Describir un protocolo de frenotomía láser con buena tolerancia. No: Comparar con tijera o con no tratar.
- **Licencia y derechos:** Acceso abierto en PMC. Licencia PENDIENTE DE VERIFICAR.
- **Estado de lectura:** Resumen PubMed y texto completo revisados el 17/10/2026.

## Figuras

Licencia del artículo: CC BY 4.0. Figuras en PubMed Central (PMC9446865).

- **Figura 1.** Curva del dolor perioperatorio (escala CRIES). [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC9446865/figure/Fig1/). Copia local: figuras/DELLOLIO2022-fig1.jpg.
- **Figura 2.** Cicatrización tras frenotomía láser en dos recién nacidos. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC9446865/figure/Fig2/).
- **Figura 3.** Peso de los recién nacidos antes y después. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC9446865/figure/Fig3/). Copia local: figuras/DELLOLIO2022-fig3.jpg.
- **Figura 4.** Dolor del pezón materno antes y después (EVA). [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC9446865/figure/Fig4/). Copia local: figuras/DELLOLIO2022-fig4.jpg.

Crédito: figuras de Dell'Olio F; Baldassarre ME; Russo FG et al (PMC9446865), CC BY 4.0. Las copias locales no se han modificado.

La figura 2 son fotos de recién nacidos: solo enlace.

---

<!-- archivo: fuentes/articulos/2022-iapd-anquiloglosia.md -->
# Estudio: Management of Ankyloglossia (International Association of Paediatric Dentistry)

- **ID:** IAPD2022
- **Autores, año y revista:** International Association of Paediatric Dentistry (IAPD), Science Committee. Publicado en 2019; republicado en 2022 tras una validación de acuerdo global.
- **DOI / PMID / URL:** URL: https://iapdworld.org/management-of-ankyloglossia/
- **Tipo de estudio:** Recomendaciones de una asociación internacional de odontopediatría, separadas en «basadas en la evidencia» y «basadas en consenso».
- **Población y tamaño muestral:** Pacientes pediátricos.
- **Definición diagnóstica y técnicas:** Método detallado del consenso: `PENDIENTE DE VERIFICAR` en el documento completo.
- **Criterio diagnóstico de anquiloglosia:** MIXTO (aspecto y función). Recomendación basada en la evidencia: el diagnóstico debe basarse en hallazgos anatómicos y en una valoración funcional de la movilidad de la lengua. No nombra ninguna herramienta concreta en su página.
- **Variables de resultado:** Diagnóstico e indicación.
- **Resultados NUMÉRICOS verificados:** Las decisiones de tratamiento deben guiarse por las limitaciones funcionales, no solo por la presencia de un frenillo restrictivo (consenso). En lactantes, la anquiloglosia puede contribuir a dificultades de lactancia y debe valorarse con otros profesionales.
- **Límites metodológicos / confusores:** Resumen web; documento completo no leído.
- **Hallazgos contrarios o no significativos:** No aplica.
- **Conclusión que sí permite / que no permite:** Sí: Decir que la IAPD pide valorar aspecto y función. No: Atribuirle una herramienta diagnóstica concreta.
- **Licencia y derechos:** Contenido de la IAPD. Aquí solo resumen propio.
- **Estado de lectura:** Página web leída el 02/11/2026. Búsqueda de actualización del 02/11/2026.

## Figuras

Figuras no revisadas. [Ver el documento](https://iapdworld.org/management-of-ankyloglossia/).

---

<!-- archivo: fuentes/articulos/2022-usman-frenillo-plano-oclusal.md -->
# Estudio: Analysis of the distance between lingual frenal attachment and mandibular incisal edge position in establishing occlusal plane in three different races

- **ID:** USMAN2022
- **Autores, año y revista:** Usman JAM; Kesumo A; Shahari NSSBM. Ann Afr Med 2022;21(4):439-443.
- **DOI / PMID / URL:** DOI `10.4103/aam.aam_174_21`; PMID `36412348`; https://pmc.ncbi.nlm.nih.gov/articles/PMC9850892/
- **Tipo de estudio:** Transversal en modelos.
- **Población y tamaño muestral:** 63 dentados (21 malayos, 21 chinos, 21 indios).
- **Definición diagnóstica y técnicas:** Medida con calibre.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA. Referencia protésica.
- **Variables de resultado:** Distancia vertical.
- **Resultados NUMÉRICOS verificados:** Malayos 14,2, chinos 14,4 e indios 15,1 mm (p<0,05).
- **Límites metodológicos / confusores:** Muestra pequeña.
- **Hallazgos contrarios o no significativos:** No aplica.
- **Conclusión que sí permite / que no permite:** Sí: Citar variación étnica de una referencia anatómica. No: Diagnosticar anquiloglosia.
- **Licencia y derechos:** Acceso abierto en PMC. Licencia PENDIENTE DE VERIFICAR.
- **Estado de lectura:** Resumen PubMed y texto completo revisados el 17/10/2026.

## Figuras

Licencia del artículo: CC BY-NC-SA 4.0 (no permite copiar aquí). Figuras en PubMed Central (PMC9850892).

- **Figura 1.** Modelo mandibular con base. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC9850892/figure/F1/).
- **Figura 2.** Marcado de la inserción anterior del frenillo y del incisivo. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC9850892/figure/F2/).

---

<!-- archivo: fuentes/articulos/2022-yoon-expansion-amigdalas.md -->
# Estudio: Impact of rapid palatal expansion on the size of adenoids and tonsils in children

- **ID:** YOON2022
- **Autores, año y revista:** Yoon A; Abdelwahab M; Bockow R et al.. Sleep Med 2022;92:96-102.
- **DOI / PMID / URL:** DOI `10.1016/j.sleep.2022.02.011`; PMID `35390750`; https://pmc.ncbi.nlm.nih.gov/articles/PMC9213408/
- **Tipo de estudio:** Cohorte retrospectiva con grupo control sin tratar.
- **Población y tamaño muestral:** 60 niños de 5 a 15 años con amígdalas grado 3-4: 40 con expansión y 20 controles.
- **Definición diagnóstica y técnicas:** Expansor Hyrax 0,25 mm/día durante 4-6 semanas. Volumen de adenoides y amígdalas en CBCT a los 13,8 meses.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA: el estudio no diagnostica anquiloglosia.
- **Variables de resultado:** Volumen de adenoides y amígdalas; cuestionario PSQ.
- **Resultados NUMÉRICOS verificados:** Con expansión, bajada media del 16,8 % en adenoides y del 38,5 % en amígdalas; redujeron el 90 % y el 97,5 % de los niños. PSQ 5,81 → 3,75. Controles sin cambio significativo.
- **Límites metodológicos / confusores:** Retrospectivo. El crecimiento y la involución natural del tejido linfoide pueden influir. Volumen en CBCT.
- **Hallazgos contrarios o no significativos:** No aplica.
- **Conclusión que sí permite / que no permite:** Sí: Decir que tras la expansión las amígdalas y adenoides se redujeron en esta cohorte. No: Afirmar que la expansión sustituye a la cirugía de amígdalas.
- **Licencia y derechos:** Acceso abierto en PMC. Licencia PENDIENTE DE VERIFICAR.
- **Estado de lectura:** Resumen PubMed revisado el 17/10/2026.

## Figuras

Licencia del artículo: Manuscrito de autor; uso según «fair use» (no permite copiar aquí). No se copian imágenes.

- **Figura 1.** Cortes de CBCT con el método de medida del volumen de adenoides y amígdalas. [Ver en el artículo](https://pmc.ncbi.nlm.nih.gov/articles/PMC9213408/).
- **Figura 2.** Cortes de CBCT antes y después de la expansión. [Ver en el artículo](https://pmc.ncbi.nlm.nih.gov/articles/PMC9213408/).
- **Figura 3.** Volúmenes de adenoides y amígdalas antes y después en ambos grupos. [Ver en el artículo](https://pmc.ncbi.nlm.nih.gov/articles/PMC9213408/).

---

<!-- archivo: fuentes/articulos/2023-biswas-longitud-frenillo-adultos.md -->
# Estudio: Lingual frenulum length: A prospecting link to craniofacial morphology in adults

- **ID:** BISWAS2023
- **Autores, año y revista:** Biswas P; Agarwal N; Saha P et al.. J Orthod Sci 2023;12:54.
- **DOI / PMID / URL:** DOI `10.4103/jos.jos_108_22`; PMID `37881664`; https://pmc.ncbi.nlm.nih.gov/articles/PMC10597376/
- **Tipo de estudio:** Transversal en tres grupos por clase esquelética (ANB).
- **Población y tamaño muestral:** 144 adultos de 18 a 28 años (48 por grupo).
- **Definición diagnóstica y técnicas:** Regla de frenillo (directa) y reducción de la apertura máxima con la punta en la papila (indirecta). Cefalometría.
- **Criterio diagnóstico de anquiloglosia:** MIXTO. Longitud directa con regla y reducción de la apertura con la punta en la papila.
- **Variables de resultado:** Longitud del frenillo y reducción de apertura por clase esquelética.
- **Resultados NUMÉRICOS verificados:** Longitud del frenillo y reducción de apertura significativamente mayores en la clase III (p<0,001).
- **Límites metodológicos / confusores:** Transversal. La conclusión de los autores invierte la dirección: la maloclusión daría un frenillo largo.
- **Hallazgos contrarios o no significativos:** Asocia el frenillo a la clase III, no a la II.
- **Conclusión que sí permite / que no permite:** Sí: Decir que en adultos la morfología del frenillo difiere según la clase esquelética. No: Afirmar dirección causal.
- **Licencia y derechos:** Acceso abierto en PMC. Licencia PENDIENTE DE VERIFICAR.
- **Estado de lectura:** Resumen PubMed y texto completo revisados el 17/10/2026.

## Figuras

Licencia del artículo: CC BY-NC-SA 4.0 (no permite copiar aquí). Figuras en PubMed Central (PMC10597376).

- **Figura 1.** Cómo se midió la longitud del frenillo y la reducción de la apertura. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10597376/figure/F1/).
- **Figura 2.** Reducción de la apertura por clase esquelética. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10597376/figure/F2/).
- **Figura 3.** Longitud media del frenillo por clase esquelética. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10597376/figure/F3/).
- **Figura 4.** Longitud vertical del frenillo por clase esquelética. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10597376/figure/F4/).

---

<!-- archivo: fuentes/articulos/2023-coppelson-postura-cbct.md -->
# Estudio: Does Head and Neck Posture Affect Cone-Beam Computed Tomography Assessment of the Upper Airway?

- **ID:** COPPELSON2023
- **Autores, año y revista:** Coppelson K; Summersgill I; Hatcher D; Nguyen G; Pada H; Stewart H; Herre T; Hansen M; Zaghi S. *J Oral Maxillofac Surg* 2023;81(6):721–733.
- **DOI / PMID / URL:** DOI `10.1016/j.joms.2023.01.016`; PMID `36841260`; [texto completo abierto CC BY](https://www.joms.org/article/S0278239123001027/pdf).
- **Tipo de estudio:** Medidas experimentales **repetidas en la misma persona** en una cohorte prospectiva de conveniencia; cada sujeto tuvo **dos CBCT** (cabeza natural y una de cinco condiciones). No es un ensayo sobre frenillo, ortodoncia ni cirugía.
- **Población y tamaño muestral:** **90 adultos** (40,7 ± 13,7 años; 70 % mujeres) reclutados por las consultas de los investigadores en The Breathe Institute, incluidas personas relacionadas con el equipo. **26 % refería antecedente de diagnóstico de tongue-tie**, no diagnosticado ni validado en este estudio.
- **Definición diagnóstica y técnicas:** CBCT basal con boca cerrada, dientes en contacto, respiración nasal y lengua descansando donde la persona la situara; frente a cinco variantes: (A) flexión cabeza abajo, (B) de pie frente a sentado, (C) tragar dos veces frente a una, (D) mentonera frente a sin mentonera, (E) extensión cabeza arriba. Radiólogo **ciego** a condición basal/experimental. Medición de área transversal mínima de vía aérea faríngea (**MCA**) mediante segmentación, y ángulo **NBC3** entre nasion, basion y punto anterosuperior de C3. Se excluyeron imágenes de mala calidad, sin contacto dental o con cambios visibles de postura lingual.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA: el cuestionario de antecedentes preguntaba por tongue-tie, pero no se clasificó por Kotlow/TRMR y no fue variable explicativa principal.
- **Variables de resultado:** Cambios individuales en MCA (mm² y porcentaje) y NBC3 (grados), comparando cada persona consigo misma en dos condiciones.
- **Resultados NUMÉRICOS verificados (texto original y tabla 3):**
  - Basal: MCA **164,1 ± 90,8 mm²** (n=90); NBC3 **112,4 ± 8,3°**.
  - **Flexión cabeza abajo:** ΔMCA **−41,4 ± 18,5 mm²** (error estándar; p=0,03); ΔNBC3 **−10,5 ± 2,75°** (p=0,006).
  - **Extensión cabeza arriba:** ΔMCA **+147,4 ± 43,3 mm²** (error estándar; p=0,0018); ΔNBC3 **+14,4 ± 3,18°** (p=0,0004).
  - **De pie frente a sentado:** ΔMCA −28,0 ± 29,8 mm², p=0,35; **deglución** tragar dos veces: +1,85 ± 37,5 mm², p=0,96; **mentonera**: −5,77 ± 18,9 mm², p=0,76: **ningún contraste significativo** para MCA.
  - Al agrupar por diferencias de NBC3, +5 ± 2,5° se asoció con **+25 % MCA**, +10 ± 2,5° con **+88 %**, −5 ± 2,5° con **−21 %**, −10 ± 2,5° con **−23 %**. Modelo cuadrático de cambio angular vs cambio relativo de MCA: **R²≈0,54**. Son agrupaciones/modelado en **esta muestra**, **no leyes de fisiología universal ni porcentajes que se puedan aplicar clínicamente a cada persona**.
- **Límites metodológicos / confusores:** Muestra voluntaria de consulta privada, adultos mayoritariamente mujeres; cinco grupos de intervención diferentes, con subconjuntos más pequeños; las grandes variaciones por flexión/extensión **deliberadas** no permiten estimar cuánto cambiará el área con una variación casual mínima. La evaluación es **imagen estática en vigilia y sedestación/bipedestación**, sin registro PSG, flujo nocturno, tono del sueño ni resistencia funcional al paso del aire. La relación cabeza–vía aérea puede depender de posición lingual, mandibular y estado respiratorio. NBC3 mide **orientación craneocervical**, **no etiología** de esa postura. Relación de autores con The Breathe Institute. No se hizo seguimiento longitudinal.
- **Hallazgos contrarios o no significativos:** Ni cambio sentado/de pie, ni mentonera, ni repetir deglución mostraron una diferencia media significativa de MCA; tampoco hubo relación significativa de edad o autorreporte de síntomas de sueño con las variables primarias en los análisis univariantes declarados. **Ausencia de significación ≠ equivalencia**, pero no omitir estos resultados.
- **Conclusión que sí permite / que no permite:** **Sí:** la flexión/extensión del cuello puede alterar sustancialmente la **medición de MCA en CBCT** en adultos. La adquisición y comparación de imágenes deberían registrar la postura y al menos valorar una variable como NBC3. **No:** demostrar obstrucción nocturna, cambio en AHI, dirección causal entre estrechez faríngea y postura corporal, efecto de frenectomía, expansión o extracciones, ni validar un umbral de MCA como diagnóstico universal de apnea.
- **Licencia y derechos:** Texto completo **open access CC BY 4.0** según el artículo. La ficha es una síntesis original; no almacena PDF, imágenes ni tablas copiadas.
- **Estado de lectura:** **Texto original completo y tabla 3 examinados el 03/11/2026** en el PDF abierto del editor, incluida la descripción de los métodos, análisis y resultados. **Limitación de inspección:** el renderizado de capturas de páginas PDF falló en la herramienta; datos tabulares cotejados mediante extracción estructurada de la página. No se han reanalizado las imágenes en píxeles.
- **Comentarios/editoriales:** El artículo recibió comentarios y una réplica editorial (PMID 37400180), cuyo contenido permanece **PENDIENTE DE VERIFICAR**.

## Lectura crítica para objeciones

**«Una vía aérea más amplia en el CBCT después de un tratamiento demuestra que el tratamiento la amplió»**: no necesariamente. Si cambió la extensión de la cabeza, la MCA puede cambiar aunque la anatomía basal no haya cambiado. Hace falta una adquisición comparable de la posición craneocervical y, para concluir mejoría del trastorno respiratorio del sueño, un desenlace funcional independiente (p. ej. PSG). Es un argumento sobre **validez de la medida**, no una prueba de que cualquier intervención sea ineficaz.

**«La cabeza en extensión demuestra que el paciente compensa una vía aérea estrecha»**: este estudio manipuló la posición y observó el efecto en una imagen; **no determinó la causa de adoptar esa postura espontáneamente**, por lo que no prueba la dirección causal.

**Revisión relacionada:** O-003 extracciones/vía aérea.

## Figuras

Figuras del original CC BY, pero no incorporadas: [texto y PDF editor](https://www.joms.org/article/S0278239123001027/pdf).

---

<!-- archivo: fuentes/articulos/2023-cordray-anquiloglosia-mas-alla-lactancia.md -->
# Estudio: The Impact of Ankyloglossia Beyond Breastfeeding: A Scoping Review of Potential Symptoms

- **ID:** CORDRAY2023
- **Autores, año y revista:** Cordray H; Mahendran GN; Tey CS; Nemeth J; Raol N. Am J Speech Lang Pathol 2023;32(6):3048-3063.
- **DOI / PMID / URL:** DOI `10.1044/2023_AJSLP-23-00169`; PMID `37606583`
- **Tipo de estudio:** Revisión de alcance (PRISMA-ScR).
- **Población y tamaño muestral:** 26 estudios de 1.568 cribados (más de 1.228 pacientes); niños mayores de 1 año.
- **Definición diagnóstica y técnicas:** Seis bases de datos, 1961 a enero de 2023. Se excluyeron estudios de baja calidad.
- **Criterio diagnóstico de anquiloglosia:** MIXTO previsiblemente: incluye estudios con criterios distintos. PENDIENTE DE VERIFICAR en el material suplementario.
- **Variables de resultado:** Síntomas posiblemente atribuibles a la anquiloglosia tras la lactancia.
- **Resultados NUMÉRICOS verificados:** 6 estudios de calidad alta y 20 media. Síntomas descritos: habla, alimentación, disfagia, trastorno respiratorio del sueño, maloclusión, higiene oral. Un ensayo aleatorizado sugiere que la frenotomía podría atenuar la apnea.
- **Límites metodológicos / confusores:** Revisión de alcance: mapea, no estima efectos. Los propios autores dicen que los datos no son concluyentes.
- **Hallazgos contrarios o no significativos:** Kummer 2025 le acusa de errores de cita y omisiones sobre el habla. Ver KUMMER2025.
- **Conclusión que sí permite / que no permite:** Sí: Citar el mapa de síntomas que se han descrito tras la lactancia. No: Decir que demuestra efectos sobre el habla.
- **Licencia y derechos:** Derechos del editor. Aquí solo metadatos y resumen propio.
- **Complemento desde el texto completo (17/10/2026):** la tabla de características del PDF recoge métodos diagnósticos muy distintos entre los 26 estudios: Kotlow, Coryllos, protocolo de lactantes, Bristol, Hazelbaker modificado, TRMR, elevación y protrusión, y valoración manual o visual no estandarizada. El recuento exacto por método no se puede leer con seguridad en el texto extraído: `PENDIENTE DE VERIFICAR`.
- **Estado de lectura:** Resumen PubMed revisado el 17/10/2026. Autores de Emory y Children's Healthcare of Atlanta. Ojo: en notas de trabajo previas se atribuía al «grupo de Zaghi»; PubMed no lo respalda (Zaghi no figura entre los autores).

## Figuras

Licencia: derechos del editor (no se copian imágenes). Leyendas leídas en el texto completo; puede haber más figuras que las listadas.

- **Figura 1.** Diagrama PRISMA de inclusión. [Ver en el artículo](https://doi.org/10.1044/2023_AJSLP-23-00169), figura 1.

---

<!-- archivo: fuentes/articulos/2023-guo-extracciones-via-aerea.md -->
# Estudio: Effect of Premolar Extraction on the Upper Airway in Adult and Adolescent Orthodontic Patients: a Meta-analysis

- **ID:** GUO2023
- **Autores, año y revista:** Guo RZ; Li LW; Zhang LW et al.. Chin J Dent Res 2023;26(1):35-45.
- **DOI / PMID / URL:** DOI `10.3290/j.cjdr.b3978679`; PMID `36988065`
- **Tipo de estudio:** Metaanálisis de estudios longitudinales con CBCT.
- **Población y tamaño muestral:** 12 estudios; 6 en el análisis cuantitativo.
- **Definición diagnóstica y técnicas:** Embase, Web of Science, Cochrane y Medline.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA: el estudio no diagnostica anquiloglosia.
- **Variables de resultado:** Volumen naso y orofaríngeo; área transversal mínima.
- **Resultados NUMÉRICOS verificados:** Adultos: sin cambios significativos; área mínima con bajada no significativa. Adolescentes: aumentos no significativos.
- **Límites metodológicos / confusores:** Pocos estudios cuantitativos. Los autores piden cautela.
- **Hallazgos contrarios o no significativos:** En adultos la tendencia del área mínima es a la baja, aunque no significativa.
- **Conclusión que sí permite / que no permite:** Sí: Decir que no se ha demostrado más riesgo de colapso de vía aérea con extracciones. No: Decir que el riesgo es cero.
- **Licencia y derechos:** Derechos del editor. Aquí solo metadatos y resumen propio.
- **Estado de lectura:** Resumen PubMed revisado el 17/10/2026.

## Figuras

Figuras no revisadas: el texto completo no está en acceso abierto en PMC. [Ver el artículo](https://doi.org/10.3290/j.cjdr.b3978679).

---

<!-- archivo: fuentes/articulos/2023-ishman-consenso-apnea-persistente.md -->
# Estudio: Expert Consensus Statement: Management of Pediatric Persistent Obstructive Sleep Apnea After Adenotonsillectomy

- **ID:** ISHMAN2023
- **Autores, año y revista:** Ishman SL; Maturo S; Schwartz S et al.. Otolaryngol Head Neck Surg 2023;168(2):115-130.
- **DOI / PMID / URL:** DOI `10.1002/ohn.159`; PMID `36757810`; https://pmc.ncbi.nlm.nih.gov/articles/PMC10105630/
- **Tipo de estudio:** Consenso de expertos con método Delphi modificado.
- **Población y tamaño muestral:** Niños de 2 a 18 años con apnea persistente.
- **Definición diagnóstica y técnicas:** Panel de clínicos nominados por sociedades; búsqueda bibliográfica por documentalista.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA: consenso de apnea persistente. Búsqueda en el texto completo (PMC) el 05/11/2026: no aparecen «ankyloglossia», «tongue-tie» ni «frenulum».
- **Variables de resultado:** Grado de consenso de cada afirmación.
- **Resultados NUMÉRICOS verificados:** 34 afirmaciones alcanzaron consenso y 18 no, en 7 categorías.
- **Límites metodológicos / confusores:** Opinión de expertos. Conflictos declarados con Inspire Medical Systems.
- **Hallazgos contrarios o no significativos:** La terapia miofuncional y la expansión rápida del maxilar figuran entre los términos de búsqueda, pero ninguna afirmación votada trata de ellas. No alcanzaron consenso la septoplastia, la glosectomía posterior media, la reducción de base de lengua y la epiglotopexia, sobre todo por falta de evidencia en niños.
- **Conclusión que sí permite / que no permite:** Sí: Citar qué opina un panel de ORL sobre la apnea persistente. No: Presentarlo como evidencia de eficacia.
- **Licencia y derechos:** Acceso abierto en PMC. Licencia PENDIENTE DE VERIFICAR.
- **Estado de lectura:** Texto completo (PMC) leído por búsqueda de términos el 05/11/2026.

## Figuras

Licencia del artículo: Derechos del editor. No se copian imágenes.

Figuras no extraídas: la versión de PMC no se puede leer por la API. [Ver el artículo en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10105630/). Descripción: `PENDIENTE DE VERIFICAR`.

---

<!-- archivo: fuentes/articulos/2023-palomares-protocolo-quirurgico-logopedico.md -->
# Estudio: Surgical and Speech Therapy Evaluation of Lingual Frenulum

- **ID:** PALOMARES2023
- **Autores, año y revista:** Palomares-Aguilera M; Inostroza-Allende F; Álvarez Carvajal D et al.. J Craniofac Surg 2023;34(6):1752-1755.
- **DOI / PMID / URL:** DOI `10.1097/SCS.0000000000009523`; PMID `37427922`
- **Tipo de estudio:** Propuesta de protocolo con un caso ilustrativo.
- **Población y tamaño muestral:** Un caso.
- **Definición diagnóstica y técnicas:** Exploración anatómica y funcional conjunta de logopedia y cirugía maxilofacial (Santiago de Chile).
- **Criterio diagnóstico de anquiloglosia:** MIXTO. Anatomía (forma del ápice, inserción, grosor) más función (reposo, protrusión, chasquido, vibración, fonemas /r/ y /rr/).
- **Variables de resultado:** No aplica.
- **Resultados NUMÉRICOS verificados:** Sin cifras.
- **Límites metodológicos / confusores:** El instrumento no está validado; los autores lo dicen.
- **Hallazgos contrarios o no significativos:** No aplica.
- **Conclusión que sí permite / que no permite:** Sí: Citar un protocolo interdisciplinar en español. No: Usarlo como validado.
- **Licencia y derechos:** Derechos del editor. Aquí solo metadatos y resumen propio.
- **Estado de lectura:** Resumen PubMed y texto completo revisados el 17/10/2026.

## Figuras

Licencia: derechos del editor (no se copian imágenes). Leyendas leídas en el texto completo; puede haber más figuras que las listadas.

- **Figura 1.** Exploración anatómica del frenillo. [Ver en el artículo](https://doi.org/10.1097/SCS.0000000000009523), figura 1.

---

<!-- archivo: fuentes/articulos/2023-zheng-postura-lengua-via-aerea-adultos.md -->
# Estudio: Three-dimensional evaluation of the association between tongue position and upper airway morphology in adults: A cross-sectional study

- **ID:** ZHENG2023AIR
- **Autores, año y revista:** Zheng Y; Aljawad H; Kim MS; Choi SH; Kim MS; Oh MH; Cho JH. *Korean J Orthod* 2023;53(5):317–327.
- **DOI / PMID / URL:** DOI `10.4041/kjod23.019`; PMID `37746777`; PMCID `PMC10547593`; [original abierto](https://pmc.ncbi.nlm.nih.gov/articles/PMC10547593/).
- **Tipo de estudio:** Estudio transversal por imagen CBCT, con comparación de sujetos cuya lengua se observó en posición alta/habitual frente a posición baja y subgrupos de espacio intraoral.
- **Población y tamaño muestral:** **194 adultos** (91 hombres, 103 mujeres); **98** con postura lingual de reposo (RTP) y **96** con lengua baja (LTP), con cuatro subgrupos por volumen de espacio intraoral dentro de LTP.
- **Definición diagnóstica y técnicas:** Separación por presencia de un espacio entre dorso lingual y paladar en CBCT. Segmentación 3D Slicer de **nasofaringe, región retropalatina, retroglosa e hipofaringe**, con **volumen**, área media (ACA) y **área transversal mínima (MCA)**. También medidas cefalométricas (ANB, planos palatino/mandibular, etc.).
- **Criterio diagnóstico de anquiloglosia:** NO APLICA: no aplicaron escala de frenillo ni TRMR; la exposición era la **posición de reposo de la lengua en CBCT**, no movilidad dinámica.
- **Variables de resultado:** Volumen por segmento faríngeo, área media y mínima, volumen del espacio intraoral con lengua baja, correlaciones cefalométricas.
- **Resultados NUMÉRICOS verificados (resumen, tablas y discusión):**
  - Comparación principal **RTP (n=98) frente a LTP (n=96): sin diferencias estadísticamente significativas globales** de volumen ni dimensiones faríngeas.
  - Al dividir LTP por volumen intraoral, la **posición extremadamente baja** se asoció con **mayor volumen/área media retropalatina y retroglosa** que otros grupos (resultado de dirección diferente a la suposición intuitiva de que lengua baja siempre equivale a vía aérea estrecha).
  - En una de las comparaciones por grupos de volumen intraoral, **MCA retropalatina** 254,2 ± 133,4 mm² (RTP) frente a 363,1 ± 122,3 mm² (subgrupo extremo de LTP), ANOVA **p=0,016** entre grupos; **volumen retrogloso** 8.777,7 ± 4.342,8 mm³ (RTP) frente a 12.585,0 ± 4.736,2 mm³ (grupo LTP extremo), ANOVA **p=0,006**.
  - Dimensiones retroglosas relacionadas **positivamente** con volumen del espacio intraoral y **negativamente** con ANB y con ángulo entre plano palatino y mandibular. Se observan diferencias entre sexos en varias medidas de vía aérea.
- **Aportación del estudio:** Mide la **postura lingual en reposo** y los segmentos faríngeos en un mismo estudio con imagen 3D. El hallazgo de **ausencia de diferencia global** y el efecto en un subgrupo extremo ofrecen preguntas interesantes sobre fenotipos, espacio disponible para la lengua y qué parte de la vía aérea se mide.
- **Límites metodológicos / confusores (decisivos):** Una sola imagen estática en vigilia; la postura podría variar durante adquisición. Cuatro subgrupos generan comparaciones múltiples. No hay PSG, y postura baja observada en una imagen no identifica su causa.
- **Licencia y derechos:** **CC BY-NC 4.0** (revista/PMC); ficha original sin copiar imágenes ni tablas.
- **Estado de lectura:** **Texto completo HTML de PMC, métodos y resultados por grupos y tablas disponibles examinados el 04/11/2026**. No se reanalizaron las imágenes CBCT.

## Figuras

[Original abierto en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10547593/), sin imágenes reproducidas.

---

<!-- archivo: fuentes/articulos/2024-albertsen-dolor-pezon.md -->
# Estudio: The effect of frenotomy in infants with ankyloglossia on maternal nipple pain - a systematic review

- **ID:** ALBERTSEN2024
- **Autores, año y revista:** Albertsen LN; Ovesen T. Dan Med J 2024;72(1).
- **DOI / PMID / URL:** DOI `10.61409/A06240378`; PMID `39936271`
- **Tipo de estudio:** Revisión sistemática y metaanálisis de ensayos. GRADE.
- **Población y tamaño muestral:** 5 ensayos; 3 en el metaanálisis.
- **Definición diagnóstica y técnicas:** Frenotomía frente a simulación o cuidados habituales.
- **Criterio diagnóstico de anquiloglosia:** MIXTO entre ensayos: Hazelbaker, Coryllos y otros (texto completo).
- **Variables de resultado:** Dolor del pezón.
- **Resultados NUMÉRICOS verificados:** Reducción de 1,23 puntos en escala de 10 (IC -1,88 a -0,57). Certeza baja a muy baja.
- **Límites metodológicos / confusores:** Riesgo de sesgo de «algunas dudas» a «alto».
- **Hallazgos contrarios o no significativos:** Relevancia clínica dudosa.
- **Conclusión que sí permite / que no permite:** Sí: Decir que hay una reducción pequeña y a corto plazo del dolor. No: Decir que el beneficio está demostrado.
- **Licencia y derechos:** Derechos del editor. Aquí solo metadatos y resumen propio.
- **Estado de lectura:** Resumen PubMed y texto completo revisados el 17/10/2026.

## Figuras

Las leyendas de las figuras no se han podido extraer del texto completo: `PENDIENTE DE VERIFICAR`. [Ver el artículo](https://doi.org/10.61409/A06240378).

---

<!-- archivo: fuentes/articulos/2024-baxter-frenillo-bucal.md -->
# Estudio: The buccal frenum: Trends in diagnosis and indications for treatment of buccal-ties among 466 healthcare professionals

- **ID:** BAXTER2024
- **Autores, año y revista:** Baxter R; Merkel-Walsh R; Lahey L; Knutsen C; Zaghi S. J Oral Rehabil 2024;51(2):369-379.
- **DOI / PMID / URL:** DOI `10.1111/joor.13609`; PMID `37823364`
- **Tipo de estudio:** Revisión de alcance más encuesta a profesionales.
- **Población y tamaño muestral:** 466 profesionales sacados de directorios de proveedores de liberación de frenillos y afines.
- **Definición diagnóstica y técnicas:** Encuesta aprobada por comité de ética.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA a la anquiloglosia lingual. Sobre el frenillo bucal (de la mejilla), los encuestados usan barrido con el dedo (89,1 %), inspección visual (76,4 %), blanqueamiento del tejido (66,5 %) y valoración funcional (53,4 %).
- **Variables de resultado:** Prácticas de diagnóstico y tratamiento declaradas.
- **Resultados NUMÉRICOS verificados:** 87 % evalúa restricciones bucales. 94 % dice que hacen falta hallazgos objetivos y subjetivos. Estiman que afecta al 5-10 % de los lactantes. 70 % libera el bucal junto al lingual. 76,8 % recomienda estiramientos.
- **Límites metodológicos / confusores:** Opinión de profesionales que ya tratan frenillos: sesgo de selección. No mide resultados en pacientes.
- **Hallazgos contrarios o no significativos:** Los propios encuestados piden más investigación, clasificación y protocolos.
- **Conclusión que sí permite / que no permite:** Sí: Describir cómo se diagnostica hoy en la práctica y la falta de consenso. No: Concluir que el frenillo bucal cause síntomas o que liberarlo funcione.
- **Licencia y derechos:** Acceso abierto (Wiley). Licencia PENDIENTE DE VERIFICAR.
- **Complemento desde el texto completo (17/10/2026):** el PDF coincide con el resumen fichado.
- **Estado de lectura:** Resumen PubMed revisado el 17/10/2026.

## Figuras

Las leyendas de las figuras no se han podido extraer del texto completo: `PENDIENTE DE VERIFICAR`. [Ver el artículo](https://doi.org/10.1111/joor.13609).

---

<!-- archivo: fuentes/articulos/2024-camanes-gonzalvo-anquiloglosia-apnea-meta.md -->
# Estudio: Relationship of ankyloglossia and obstructive sleep apnea: systematic review and meta-analysis

- **ID:** CAMANES2024
- **Autores, año y revista:** Camañes-Gonzalvo S; Montiel-Company JM; Paredes-Gallardo V et al.. Sleep Breath 2024;28(3):1067-1078.
- **DOI / PMID / URL:** DOI `10.1007/s11325-024-03021-4`; PMID `38478208`; https://pmc.ncbi.nlm.nih.gov/articles/PMC11196303/
- **Tipo de estudio:** Revisión sistemática y metaanálisis. GRADE.
- **Población y tamaño muestral:** 6 estudios; 4 en el metaanálisis.
- **Definición diagnóstica y técnicas:** Cinco bases de datos hasta enero de 2024.
- **Criterio diagnóstico de anquiloglosia:** MIXTO. Los estudios miden la longitud directa, la lengua libre de Kotlow o la movilidad.
- **Variables de resultado:** Apnea obstructiva infantil.
- **Resultados NUMÉRICOS verificados:** OR 3,05 (IC 1,94-4,80) para frenillo corto y OR 12,30 (IC 6,14-24,65) para paladar ojival. Evidencia moderada.
- **Límites metodológicos / confusores:** Pocos estudios.
- **Hallazgos contrarios o no significativos:** Los autores piden valorar también la movilidad y el paladar.
- **Conclusión que sí permite / que no permite:** Sí: Decir que hay asociación entre anquiloglosia y apnea infantil, y que el paladar ojival pesa más. No: Afirmar causa.
- **Licencia y derechos:** Acceso abierto en PMC. Licencia PENDIENTE DE VERIFICAR.
- **Estado de lectura:** Resumen PubMed y texto completo revisados el 17/10/2026.

## Figuras

Licencia del artículo: CC BY 4.0. Figuras en PubMed Central (PMC11196303).

- **Figura 1.** Diagrama PRISMA. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11196303/figure/Fig1/). Copia local: figuras/CAMANES2024-fig1.jpg.
- **Figura 2.** Diagrama de bosque del metaanálisis. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11196303/figure/Fig2/). Copia local: figuras/CAMANES2024-fig2.jpg.
- **Figura 3.** Diagrama de embudo. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11196303/figure/Fig3/). Copia local: figuras/CAMANES2024-fig3.jpg.

Crédito: figuras de Camañes-Gonzalvo S; Montiel-Company JM; Paredes-Gallardo V et al (PMC11196303), CC BY 4.0. Las copias locales no se han modificado.

---

<!-- archivo: fuentes/articulos/2024-carnino-habla-metaanalisis.md -->
# Estudio: Speech Outcomes of Frenectomy for Tongue-Tie Release: A Systematic Review and Meta-Analysis

- **ID:** CARNINO2024
- **Autores, año y revista:** Carnino JM; Rodriguez Lara F; Chan WP et al.. Ann Otol Rhinol Laryngol 2024;133(6):566-574.
- **DOI / PMID / URL:** DOI `10.1177/00034894241236234`; PMID `38444142`
- **Tipo de estudio:** Revisión sistemática y metaanálisis.
- **Población y tamaño muestral:** 10 estudios; edad media 4,1 años; cohortes medias de 22 pacientes.
- **Definición diagnóstica y técnicas:** Resultados de habla valorados de forma subjetiva por logopeda o padres.
- **Criterio diagnóstico de anquiloglosia:** Variable entre estudios: PENDIENTE DE VERIFICAR.
- **Variables de resultado:** Mejora de la articulación.
- **Resultados NUMÉRICOS verificados:** Mejora de la articulación 0,78 (IC 0,64-0,87). La edad se asoció a peor resultado en el modelo sin ajustar, no en el ajustado.
- **Límites metodológicos / confusores:** Medidas subjetivas, sin grupos control en la mayoría.
- **Hallazgos contrarios o no significativos:** Contrasta con Melong 2024 y Kummer 2025. Ver O-004.
- **Conclusión que sí permite / que no permite:** Sí: Decir que en estudios no controlados se describe mejora del habla tras frenectomía. No: Decir que está demostrado.
- **Licencia y derechos:** Derechos del editor. Aquí solo metadatos y resumen propio.
- **Estado de lectura:** Resumen PubMed y texto completo revisados el 17/10/2026.

## Figuras

Licencia: derechos del editor (no se copian imágenes). Leyendas leídas en el texto completo; puede haber más figuras que las listadas.

- **Figura 1.** Proceso de la revisión. [Ver en el artículo](https://doi.org/10.1177/00034894241236234), figura 1.
- **Figura 3.** Diagrama de bosque: mejora del habla en menores de 5 años. [Ver en el artículo](https://doi.org/10.1177/00034894241236234), figura 3.
- **Figura 4.** Edad frente a resultado del habla. [Ver en el artículo](https://doi.org/10.1177/00034894241236234), figura 4.

---

<!-- archivo: fuentes/articulos/2024-clausen-habla-revision-danesa.md -->
# Estudio: The influence of tight tongue-ties and tongue-tie clips on speech development

- **ID:** CLAUSEN2024
- **Autores, año y revista:** Clausen MC; Printz T; Nikoghosyan-Bossen G. Ugeskr Laeger 2024;186(18).
- **DOI / PMID / URL:** DOI `10.61409/V11230699`; PMID `38704717`
- **Tipo de estudio:** Revisión narrativa en danés.
- **Población y tamaño muestral:** No aplica.
- **Definición diagnóstica y técnicas:** No aplica.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA: el estudio no diagnostica anquiloglosia.
- **Variables de resultado:** No aplica.
- **Resultados NUMÉRICOS verificados:** Sin cifras en el resumen.
- **Límites metodológicos / confusores:** Revisión narrativa. Conclusiones: PENDIENTE DE VERIFICAR (texto en danés no revisado a fondo).
- **Hallazgos contrarios o no significativos:** No aplica.
- **Conclusión que sí permite / que no permite:** Sí: Citar que el debate sobre habla y frenotomía es público en Dinamarca. No: Usarla como prueba.
- **Licencia y derechos:** Derechos del editor. Aquí solo metadatos y resumen propio.
- **Estado de lectura:** Resumen PubMed y texto completo revisados el 17/10/2026.

## Figuras

Las leyendas de las figuras no se han podido extraer del texto completo: `PENDIENTE DE VERIFICAR`. [Ver el artículo](https://doi.org/10.61409/V11230699).

---

<!-- archivo: fuentes/articulos/2024-correa-prevencion-apnea.md -->
# Estudio: Preventive medicine in obstructive sleep apnea-a systematic review and a call to action

- **ID:** CORREA2024
- **Autores, año y revista:** Correa EJ; Conti DM; Gozal D et al.. Sleep 2024;47(12).
- **DOI / PMID / URL:** DOI `10.1093/sleep/zsae164`; PMID `39041305`
- **Tipo de estudio:** Revisión sistemática.
- **Población y tamaño muestral:** 4 artículos de 720.
- **Definición diagnóstica y técnicas:** Cochrane, EMBASE, MEDLINE, PubMed, LILACS.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA: el estudio no diagnostica anquiloglosia.
- **Variables de resultado:** Prevención de la apnea.
- **Resultados NUMÉRICOS verificados:** Solo 4 trabajos sobre prevención frente a 23.674 sobre tratamiento.
- **Límites metodológicos / confusores:** Muy pocos estudios.
- **Hallazgos contrarios o no significativos:** No aplica.
- **Conclusión que sí permite / que no permite:** Sí: Citar el desequilibrio entre investigación en tratamiento y en prevención. No: Recomendar medidas concretas.
- **Licencia y derechos:** Derechos del editor. Aquí solo metadatos y resumen propio.
- **Estado de lectura:** Resumen PubMed y texto completo revisados el 17/10/2026.

## Figuras

Licencia: derechos del editor (no se copian imágenes). Leyendas leídas en el texto completo; puede haber más figuras que las listadas.

- **Figura 1.** Diagrama PRISMA. [Ver en el artículo](https://doi.org/10.1093/sleep/zsae164), figura 1.

---

<!-- archivo: fuentes/articulos/2024-deshkar-lengua-maloclusion.md -->
# Estudio: The Influence of the Tongue on the Development of Dental Malocclusion

- **ID:** DESHKAR2024
- **Autores, año y revista:** Deshkar M; Thosar NR; Kabra SP et al.. Cureus 2024;16(5):e61281.
- **DOI / PMID / URL:** DOI `10.7759/cureus.61281`; PMID `38947580`; https://pmc.ncbi.nlm.nih.gov/articles/PMC11211712/
- **Tipo de estudio:** Revisión narrativa.
- **Población y tamaño muestral:** No aplica.
- **Definición diagnóstica y técnicas:** No aplica.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA: el estudio no diagnostica anquiloglosia.
- **Variables de resultado:** No aplica.
- **Resultados NUMÉRICOS verificados:** Sin cifras.
- **Límites metodológicos / confusores:** Revisión no sistemática.
- **Hallazgos contrarios o no significativos:** No aplica.
- **Conclusión que sí permite / que no permite:** Sí: Citar la idea de la lengua como compensadora y moldeadora de arcadas. No: Usarla como evidencia.
- **Licencia y derechos:** Acceso abierto en PMC. Licencia PENDIENTE DE VERIFICAR.
- **Estado de lectura:** Resumen PubMed y texto completo revisados el 17/10/2026.

## Figuras

Licencia del artículo: CC BY 4.0. Figuras en PubMed Central (PMC11211712).

- **Figura 1.** Relaciones anatómicas de la lengua (esquema de los autores). [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11211712/figure/FIG1/). Copia local: figuras/DESHKAR2024-fig1.jpg.
- **Figura 2.** Tipos de macroglosia (esquema de los autores). [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11211712/figure/FIG2/). Copia local: figuras/DESHKAR2024-fig2.jpg.
- **Figura 3.** Clasificación de Moyers. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11211712/figure/FIG3/).
- **Figura 4.** Protocolo de manejo. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11211712/figure/FIG4/). Copia local: figuras/DESHKAR2024-fig4.jpg.

Crédito: figuras de Deshkar M; Thosar NR; Kabra SP et al (PMC11211712), CC BY 4.0. Las copias locales no se han modificado.

La figura 3 reproduce una clasificación de terceros: solo enlace.

---

<!-- archivo: fuentes/articulos/2024-ehsan-guia-ats.md -->
# Estudio: Management of Persistent, Post-adenotonsillectomy Obstructive Sleep Apnea in Children: An Official American Thoracic Society Clinical Practice Guideline

- **ID:** EHSAN2024
- **Autores, año y revista:** Ehsan Z; Ishman SL; Soghier I et al.; Coppelson K. Am J Respir Crit Care Med 2024;209(3):248-261.
- **DOI / PMID / URL:** DOI `10.1164/rccm.202310-1857ST`; PMID `37890009`; https://pmc.ncbi.nlm.nih.gov/articles/PMC10840779/
- **Tipo de estudio:** Guía de práctica clínica con revisión sistemática y GRADE.
- **Población y tamaño muestral:** Niños con apnea persistente tras adenoamigdalectomía.
- **Definición diagnóstica y técnicas:** Panel internacional multidisciplinar.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA: guía de apnea persistente. Búsqueda en el texto completo (PMC) el 05/11/2026: no aparecen «ankyloglossia», «tongue-tie» ni «frenulum».
- **Variables de resultado:** Seis preguntas de manejo: CPAP, ortodoncia y ortopedia dentofacial, pérdida de peso, amigdalectomía lingual, supraglotoplastia y montelukast.
- **Resultados NUMÉRICOS verificados:** Hasta un 40 % de niños puede seguir con apnea tras la adenoamigdalectomía. Las seis recomendaciones son condicionales y de certeza muy baja: CPAP si no hay tratamiento dirigido a un sitio concreto; ortodoncia u ortopedia dentofacial en niños con rasgos craneofaciales concretos; pérdida de peso si hay sobrepeso u obesidad; amigdalectomía lingual si hay hipertrofia de la amígdala lingual; supraglotoplastia en la laringomalacia dependiente del sueño; montelukast en niños con corticoides nasales. Expansión rápida del maxilar en dos estudios observacionales: mejora media del IAH de 3,3 eventos por hora (IC 95 % 1,8 a 4,8) y de la saturación de 2,8 %.
- **Límites metodológicos / confusores:** Los propios autores dicen que se basa en evidencia limitada y opinión experta.
- **Hallazgos contrarios o no significativos:** La terapia miofuncional, la estimulación del hipogloso y la cirugía maxilomandibular no se evalúan: quedan para una actualización futura. Entre los efectos adversos de la expansión cita, de un estudio de Guilleminault 2013, que 18 de 29 niños no podían chasquear la lengua, 15 no podían llevarla hacia la nariz, 6 tenían dificultad para sujetar un botón con los labios y 2 para tragar líquidos.
- **Conclusión que sí permite / que no permite:** Sí: citar la cifra de apnea persistente y sus seis recomendaciones condicionales. No: presentarlas como evidencia de eficacia, porque todas tienen certeza muy baja.
- **Licencia y derechos:** CC BY-NC-ND 4.0 (texto en PMC). Aquí solo resumen propio.
- **Estado de lectura:** Texto completo (Europe PMC) leído por búsqueda de términos y en las recomendaciones el 05/11/2026.

## Figuras

Licencia del artículo: CC BY-NC-ND 4.0. No se copian imágenes.

Figuras no extraídas: la versión de PMC no se puede leer por la API. [Ver el artículo en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10840779/). Descripción: `PENDIENTE DE VERIFICAR`.

---

<!-- archivo: fuentes/articulos/2024-feldens-lactancia-duracion.md -->
# Estudio: Ankyloglossia and Breastfeeding Duration: A Multicenter Birth Cohort Study

- **ID:** FELDENS2024
- **Autores, año y revista:** Feldens CA; Heck ABDS; Rodrigues PH et al.. Breastfeed Med 2024;19(1):17-25.
- **DOI / PMID / URL:** DOI `10.1089/bfm.2023.0182`; PMID `38241126`
- **Tipo de estudio:** Cohorte de nacimiento prospectiva multicéntrica (NCT03841123).
- **Población y tamaño muestral:** 293 niños de hospitales públicos de tres capitales de Brasil, seguidos hasta los 12 meses.
- **Definición diagnóstica y técnicas:** Entrevistas a las madres al nacer, a los 6 y a los 12 meses. Exploración dental a los 12 meses.
- **Criterio diagnóstico de anquiloglosia:** MIXTO. Bristol Tongue Assessment Tool (aspecto de la punta, inserción, elevación y protrusión), aplicado a los 12 meses.
- **Variables de resultado:** Lactancia exclusiva y total a 1, 4 y 6 meses.
- **Resultados NUMÉRICOS verificados:** Anquiloglosia definida 1 % y sospechosa 4,8 % (total 5,8 %; IC 3,1-8,5). Probabilidad de llegar a 6 meses de lactancia sin diferencia (RR 0,98; IC 0,79-1,23).
- **Límites metodológicos / confusores:** Frenillo valorado a los 12 meses, no al nacer. Pocos casos definidos.
- **Hallazgos contrarios o no significativos:** Ninguna diferencia en lactancia exclusiva ni total.
- **Conclusión que sí permite / que no permite:** Sí: Decir que en esta cohorte brasileña la anquiloglosia no se asoció a menor duración de la lactancia. No: Extrapolar a restricciones posteriores o a otras funciones.
- **Licencia y derechos:** Derechos del editor. Aquí solo metadatos y resumen propio.
- **Estado de lectura:** Resumen PubMed y texto completo revisados el 17/10/2026.

## Figuras

Licencia: derechos del editor (no se copian imágenes). Leyendas leídas en el texto completo; puede haber más figuras que las listadas.

- **Figura 2.** Lactancia exclusiva y total según anquiloglosia. [Ver en el artículo](https://doi.org/10.1089/bfm.2023.0182), figura 2.

---

<!-- archivo: fuentes/articulos/2024-gomez-vela-armonizacion-antropometria.md -->
# Estudio: Tratamiento para la armonización del perfil facial basado en la antropometría directa. A propósito de un caso

- **ID:** GOMEZVELA2024
- **Autores, año y revista:** Gómez Vela. Medicina Estética (SEME), septiembre de 2024.
- **DOI / PMID / URL:** DOI `10.48158/MEDICINAESTETICA.080.02`
- **Tipo de estudio:** Caso clínico.
- **Población y tamaño muestral:** Un caso.
- **Definición diagnóstica y técnicas:** Antropometría directa para armonización con rellenos.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA: el estudio no diagnostica anquiloglosia.
- **Variables de resultado:** No aplica.
- **Resultados NUMÉRICOS verificados:** No aplica.
- **Límites metodológicos / confusores:** Un caso.
- **Hallazgos contrarios o no significativos:** No aplica.
- **Conclusión que sí permite / que no permite:** Sí: Citar el enfoque antropométrico en medicina estética. No: Generalizar.
- **Licencia y derechos:** Derechos del editor. Aquí solo metadatos y resumen propio.
- **Estado de lectura:** Metadatos comprobados en Crossref; texto completo.

## Figuras

Licencia: derechos del editor (no se copian imágenes). Leyendas leídas en el texto completo; puede haber más figuras que las listadas.

- **Figura 1.** Proporciones en visión frontal. [Ver en el artículo](https://doi.org/10.48158/MEDICINAESTETICA.080.02), figura 1.
- **Figura 2.** Visión lateral general. [Ver en el artículo](https://doi.org/10.48158/MEDICINAESTETICA.080.02), figura 2.

---

<!-- archivo: fuentes/articulos/2024-hoang-vietnam-movilidad-fuerza.md -->
# Estudio: Restricted tongue mobility and ankyloglossia in 6-8-year-old Vietnamese school children: prevalence and association with tongue strength and endurance

- **ID:** HOANG2024
- **Autores, año y revista:** Hoang DA; Nguyen TM; Jagomägi T. Eur Arch Paediatr Dent 2024;25(6):791-799.
- **DOI / PMID / URL:** DOI `10.1007/s40368-024-00938-y`; PMID `39207660`
- **Tipo de estudio:** Transversal en colegios.
- **Población y tamaño muestral:** 512 niños sanos de 6 a 8 años del centro de Vietnam (46,5 % niñas).
- **Definición diagnóstica y técnicas:** TRMR-TIP y TRMR-LPS. Fuerza y resistencia lingual con IOPI.
- **Criterio diagnóstico de anquiloglosia:** FUNCIONAL. TRMR con TIP (anterior) y LPS (posterior).
- **Variables de resultado:** Prevalencia de restricción y relación con fuerza y resistencia.
- **Resultados NUMÉRICOS verificados:** Restricción anterior 17,5 % (16,2 % <50 % y 1,3 % <25 %). Restricción posterior (<30 % en LPS) 28,9 %. La restricción anterior no predijo menos presión; la posterior se asoció a menos fuerza, no a menos resistencia.
- **Límites metodológicos / confusores:** Transversal. El estudio de Zaghi 2021 advierte de que el TRMR es poco fiable antes de los 12 años.
- **Hallazgos contrarios o no significativos:** La restricción anterior no se asoció a la fuerza.
- **Conclusión que sí permite / que no permite:** Sí: Decir que la restricción posterior es más frecuente que la anterior y que se asocia a menos fuerza lingual. No: Afirmar causa.
- **Licencia y derechos:** Derechos del editor. Aquí solo metadatos y resumen propio.
- **Estado de lectura:** Resumen PubMed y texto completo revisados el 17/10/2026.

## Figuras

Licencia: derechos del editor (no se copian imágenes). Leyendas leídas en el texto completo; puede haber más figuras que las listadas.

- **Figura 1.** Correlaciones de Spearman entre movilidad y fuerza. [Ver en el artículo](https://doi.org/10.1007/s40368-024-00938-y), figura 1.

---

<!-- archivo: fuentes/articulos/2024-icap-guia-ankylofrenula.md -->
# Estudio: International Consortium of Oral Ankylofrenula Professionals (ICAP) Practice Guidelines for Ankylofrenula Management

- **ID:** ICAP2024
- **Autores, año y revista:** Smart S; Kittrell A; Merkel-Walsh R; Tseng RJ. *International Journal of Orofacial Myology and Myofunctional Therapy* 2024;50(2):1–11.
- **DOI / PMID / URL:** DOI `10.52010/ijom.2024.50.2.3`; [texto íntegro abierto](https://www.mdpi.com/2694-2526/50/2/11).
- **Tipo de estudio:** **Guía/posicionamiento profesional de ICAP**, redactado por su comité y aprobado por su junta; **no es un estudio clínico, no contiene metaanálisis propio ni representa un consenso intersocietario**. Publicado como artículo de perspectiva de acceso abierto.
- **Población y tamaño muestral:** Personas desde lactantes hasta adultos; no hay muestra primaria de pacientes ni comparación clínica de intervenciones.
- **Definición diagnóstica y técnicas:** ICAP define ankyloglossia como **restricción funcional de la movilidad lingual anterior y media atribuida al frenillo**. Propone valoración multidisciplinar de estructura y función: apariencia, amplitud/movilidad lingual, alimentación/lactancia, habla, deglución, respiración y otras funciones cuando sean pertinentes. Reconoce que no existe acuerdo universal sobre sistemas de clasificación **de apariencia**; no identifica una prueba única validada que establezca causalidad de todas las quejas clínicas al frenillo.
- **Criterio diagnóstico de anquiloglosia:** FUNCIONAL (definición propuesta en guía): **la restricción de función es necesaria**, no únicamente un grado de apariencia. **No implica validación independiente** de la definición o sus implicaciones; la guía presenta recomendaciones profesionales, no un estándar diagnóstico validado con precisión/sensibilidad.
- **Variables de resultado:** Estandarización profesional, roles/licencias, diagnóstico y evaluación multidisciplinar, alternativas no quirúrgicas, consentimiento, cirugía, seguimiento, heridas y ejercicios.
- **Resultados NUMÉRICOS verificados:** **Sin resultados experimentales cuantitativos**; recomienda revisiones posquirúrgicas guiadas por el estado funcional y menciona 2–4 semanas para revisión de tejidos en determinadas situaciones. Esa cifra es una **recomendación de documento**, no duración óptima demostrada en ensayo. Admite que **no existen protocolos de seguimiento quirúrgico estandarizados publicados**.
- **Límites metodológicos / confusores:** Consorcio de profesionales implicados en diagnóstico/tratamiento, posible sesgo de representación y conflictos comerciales/profesionales. Reconoce falta de investigación de alta calidad y posibles sesgos de selección del grupo. No hay estudio primario para demostrar que la terapia posterior sea necesaria universalmente, que liberar frenillo altere el crecimiento óseo o que un profesional deba realizar todos los componentes de tratamiento. Recomendaciones condicionadas por normas y licencias locales. El propio ICAP pide colaboración entre profesionales y respeto a las competencias y a la legislación de cada país.
- **Hallazgos contrarios o no significativos:** La propia guía reconoce **evidencia limitada** para evaluar/liberar frenillos bucales y **consenso y evidencia insuficientes para ejercicios pre y posoperatorios**. Aboga por considerar opciones no quirúrgicas antes de operar; no afirma eficacia garantizada de la cirugía por sí sola.
- **Conclusión que sí permite / que no permite:** Sí: mostrar que **ICAP adopta una definición funcional** y recomienda evaluación colaborativa y decisiones individualizadas; contrasta con clasificaciones puramente morfológicas. No: utilizar su posición como prueba de que todas las restricciones visibles causan disfunción, que un mecanismo lingual provoca apnea/maloclusión, o que la práctica aceptada por este consorcio sea una guía clínica universal obligatoria.
- **Licencia y derechos:** Acceso abierto **CC BY** según página de MDPI; síntesis original sin PDF ni tablas copiadas.
- **Estado de lectura:** Documento completo HTML abierto revisado el **03/11/2026**, con apartados de definición, diagnóstico, tratamientos, seguimiento, ejercicios y límites; [página oficial](https://www.mdpi.com/2694-2526/50/2/11).

## Figuras

No se reproducen; [documento original](https://doi.org/10.52010/ijom.2024.50.2.3).

---

<!-- archivo: fuentes/articulos/2024-jones-clinica-especializada.md -->
# Estudio: The development of a specialist tongue tie assessment clinic for neonates

- **ID:** JONES2024A
- **Autores, año y revista:** Jones H; Walsh M; O'Leary M et al.. Int J Pediatr Otorhinolaryngol 2024;176:111843.
- **DOI / PMID / URL:** DOI `10.1016/j.ijporl.2023.111843`; PMID `38157706`
- **Tipo de estudio:** Descripción de un servicio clínico.
- **Población y tamaño muestral:** 157 pacientes, 162 visitas, enero a octubre de 2023.
- **Definición diagnóstica y técnicas:** Consulta conjunta de otorrinolaringología y lactancia.
- **Criterio diagnóstico de anquiloglosia:** MIXTO. Combina Bristol, Martinelli y Coryllos (texto completo del estudio hermano, JONES2024B).
- **Variables de resultado:** Visitas y frenotomías.
- **Resultados NUMÉRICOS verificados:** 96 frenotomías en 157 pacientes.
- **Límites metodológicos / confusores:** Descriptivo, sin resultados clínicos medidos.
- **Hallazgos contrarios o no significativos:** No aplica.
- **Conclusión que sí permite / que no permite:** Sí: Citar un modelo de consulta especializada para limitar el sobretratamiento. No: Concluir eficacia.
- **Licencia y derechos:** Derechos del editor. Aquí solo metadatos y resumen propio.
- **Estado de lectura:** Resumen PubMed y texto completo revisados el 17/10/2026.

## Figuras

Licencia: derechos del editor (no se copian imágenes). Leyendas leídas en el texto completo; puede haber más figuras que las listadas.

- **Figura 1.** Formulario de derivación a la consulta. [Ver en el artículo](https://doi.org/10.1016/j.ijporl.2023.111843), figura 1.
- **Figura 2.** Hoja de valoración del frenillo. [Ver en el artículo](https://doi.org/10.1016/j.ijporl.2023.111843), figura 2.
- **Figura 3.** Material para la frenotomía (gotas de sacarosa, sonda acanalada…). [Ver en el artículo](https://doi.org/10.1016/j.ijporl.2023.111843), figura 3.
- **Figura 4.** Pasos de la frenotomía. [Ver en el artículo](https://doi.org/10.1016/j.ijporl.2023.111843), figura 4.

---

<!-- archivo: fuentes/articulos/2024-jones-frenotomia-lactancia-longitudinal.md -->
# Estudio: Lingual frenotomy for ankyloglossia in infants with breastfeeding difficulties: a longitudinal observational study

- **ID:** JONES2024B
- **Autores, año y revista:** Jones H; Hintze J; Walsh M et al.. Eur J Pediatr 2024;183(12):5245-5254.
- **DOI / PMID / URL:** DOI `10.1007/s00431-024-05799-7`; PMID `39375199`
- **Tipo de estudio:** Estudio observacional prospectivo con cuestionarios.
- **Población y tamaño muestral:** 157 lactantes atendidos, 96 frenotomías; 101 cuestionarios basales y 34 de seguimiento a 4 semanas.
- **Definición diagnóstica y técnicas:** Cuestionarios autorreferidos de las madres.
- **Criterio diagnóstico de anquiloglosia:** MIXTO. Bristol Tongue Assessment Tool, Martinelli Screening Tool y clasificación de Coryllos (texto completo).
- **Variables de resultado:** Dolor al amamantar, agarre, continuidad de la lactancia.
- **Resultados NUMÉRICOS verificados:** Motivos: dificultad de agarre 45 % y dolor del pezón 40 %. Dolor medio 2,53 sobre 5 al inicio y 1,47 tras frenotomía.
- **Límites metodológicos / confusores:** Sin grupo control. Gran pérdida en el seguimiento (34 de 101).
- **Hallazgos contrarios o no significativos:** No aplica.
- **Conclusión que sí permite / que no permite:** Sí: Decir que en esta serie el dolor referido bajó tras la frenotomía. No: Atribuirlo a la frenotomía frente a la evolución natural.
- **Licencia y derechos:** Derechos del editor. Aquí solo metadatos y resumen propio.
- **Estado de lectura:** Resumen PubMed y texto completo revisados el 17/10/2026.

## Figuras

Licencia: derechos del editor (no se copian imágenes). Leyendas leídas en el texto completo; puede haber más figuras que las listadas.

- **Figura 1.** Cuestionario inicial. [Ver en el artículo](https://doi.org/10.1007/s00431-024-05799-7), figura 1.
- **Figura 2.** Cuestionario de seguimiento. [Ver en el artículo](https://doi.org/10.1007/s00431-024-05799-7), figura 2.
- **Figura 3.** Respuestas: cómo alimenta a su bebé. [Ver en el artículo](https://doi.org/10.1007/s00431-024-05799-7), figura 3.
- **Figura 5.** Respuestas: dificultades desde el nacimiento. [Ver en el artículo](https://doi.org/10.1007/s00431-024-05799-7), figura 5.
- **Figura 7.** Respuestas: motivo principal de la consulta. [Ver en el artículo](https://doi.org/10.1007/s00431-024-05799-7), figura 7.
- **Figura 8.** Respuestas: dolor al amamantar. [Ver en el artículo](https://doi.org/10.1007/s00431-024-05799-7), figura 8.
- **Figura 11.** Respuestas: si la lactancia mejoró tras la frenotomía. [Ver en el artículo](https://doi.org/10.1007/s00431-024-05799-7), figura 11.

---

<!-- archivo: fuentes/articulos/2024-kotarska-frenotomia-desarrollo-facial.md -->
# Estudio: Does Ankyloglossia Surgery Promote Normal Facial Development? A Systematic Review

- **ID:** KOTARSKA2024
- **Autores, año y revista:** Kotarska M; Wądołowska A; Sarul M; Kawala B; Lis J. *Journal of Clinical Medicine* **2025**;14(1):81 (publicado en línea el 27/12/2024).
- **DOI / PMID / URL:** DOI `10.3390/jcm14010081`; PMID `39797164`; https://pmc.ncbi.nlm.nih.gov/articles/PMC11722303/
- **Tipo de estudio:** Revisión sistemática registrada PROSPERO CRD42022333628, PRISMA, evaluación JBI modificada y GRADE. Incluye estudios comparativos observacionales, **no ensayos de frenotomía**.
- **Población y tamaño muestral:** 7 estudios, 1.349 pacientes con anquiloglosia y 90 controles.
- **Definición diagnóstica y técnicas:** Búsqueda en PubMed, Cochrane, Medline, Web of Science y Embase hasta 09/12/2024; revisión por dos investigadores (κ = 0,85). **Criterios PECOS explícitos: pacientes sin cirugía previa del frenillo ni ortodoncia previa.** Por diseño, no se comparó el crecimiento antes/después de frenotomía.
- **Criterio diagnóstico de anquiloglosia:** MIXTO. La revisión reconoce que no hay un criterio diagnóstico estándar. Los estudios incluidos usan longitud (regla de frenillo, lengua libre de Kotlow), reducción de apertura (Marchesan) y TRMR (texto completo, tabla de métodos).
- **Variables de resultado:** Anchuras intercanina e intermolar, clase de Angle, apiñamiento, hioides.
- **Resultados NUMÉRICOS verificados:** 7 estudios, 1.439 participantes (1.349 con anquiloglosia y 90 controles); los propios autores califican la certeza global **baja**. En Srinivasan, anchuras maxilares intercanina 33,008 vs 35,402 mm e intermolar 42,807 vs 48,374 mm (grupos con/sin anquiloglosia). Yoon describió asociaciones en ratios de arcada maxilar y pendiente palatina, con desenlaces mandibulares no concluyentes; **no se hizo metaanálisis común** por heterogeneidad y datos escasos.
- **Límites metodológicos / confusores:** Estudios seleccionados por atención ortodóncica en gran parte, controles escasos, definiciones variables, diseños observacionales con asociación/correlación, confusión y edad; síntesis cuantitativa conjunta imposible. **Especial atención: la revisión plantea recomendaciones de edad para frenotomía pese a excluir pacientes ya operados. No presenta datos de beneficio por edad ni efecto quirúrgico experimental o longitudinal para sustentarlas.** Varios estudios primarios aparecen también en Póvoa-Santos 2024 (Jang, Meenakshi, Srinivasan, Yoon, Sepet): no son muestras independientes.
- **Hallazgos contrarios o no significativos:** En la tabla 8, Yoon informa **sin asociación** para medidas mandibulares como SN–Mn y H–Mn con TRMR o Kotlow (p>0,05); la tabla 7 presenta varios desenlaces sin diferencias significativas. La relación con el hioides se clasifica de certeza **muy baja**. No se ha demostrado un efecto de frenotomía en los estudios incluidos.
- **Conclusión que sí permite / que no permite:** Sí: los estudios disponibles describen asociaciones inciertas entre medidas de anquiloglosia y algunas dimensiones dentoalveolares o tipos de oclusión. No: afirmar causalidad, que la frenotomía modifica el crecimiento ni recomendar edades de cirugía basándose en esos datos. **La conclusión editorial de los autores sobre intervenir a los 4 años o aplazar según clase II NO está probada por los estudios que seleccionaron.**
- **Licencia y derechos:** Acceso abierto **CC BY 4.0**. Resumen editorial propio y enlaces, sin copiar tablas/figuras protegidas o ajenas.
- **Complemento desde el texto completo (17/10/2026):** el PDF coincide con el texto de PMC usado en la ficha.
- **Estado de lectura:** Texto completo abierto examinado el **03/11/2026**, incluidos PECOS, tablas 1, 7–11, GRADE y discusión; fuente [PDF editorial de acceso abierto](https://www.mdpi.com/2077-0383/14/1/81/pdf?version=1735291066). La ficha conserva la referencia al trabajo de lectura anterior.

## Figuras

Licencia del artículo: CC BY 4.0. Figuras en PubMed Central (PMC11722303).

- **Figura 1.** Diagrama de selección de estudios. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11722303/figure/jcm-14-00081-f001/). Copia local: figuras/KOTARSKA2024-fig1.jpg.

Crédito: figuras de Kotarska M; Wądołowska A; Sarul M; Kawala B; Lis J (PMC11722303), CC BY 4.0. Las copias locales no se han modificado.

---

<!-- archivo: fuentes/articulos/2024-lichnowska-ensayo-frenuloplastia.md -->
# Estudio: A Prospective Randomized Control Trial of Lingual Frenuloplasty with Myofunctional Therapy in Patients with Maxillofacial Deformity in a Polish Cohort

- **ID:** LICHNOWSKA2024
- **Autores, año y revista:** Lichnowska A; Gnatek A; Tyszkiewicz S; Kozakiewicz M; Zaghi S. J Clin Med 2024;13(18):5354.
- **DOI / PMID / URL:** DOI `10.3390/jcm13185354`; PMID `39336841`; https://pmc.ncbi.nlm.nih.gov/articles/PMC11432234/
- **Tipo de estudio:** Ensayo prospectivo con dos grupos: terapia miofuncional frente a terapia miofuncional más frenuloplastia.
- **Población y tamaño muestral:** **155 participantes**, 78 en grupo A (terapia miofuncional + frenuloplastia) y 77 en grupo B (terapia miofuncional). El original refiere **edades medias distintas: 18 años en A frente a 26 en B**. Cohorte clínica con deformidad maxilofacial; los resultados no son extrapolables a población general ni a crecimiento esquelético.
- **Definición diagnóstica y técnicas:** Asignación por orden/día de entrada en la clínica, no se documenta una secuencia aleatoria impredecible ni ocultación de asignación; la etiqueta «randomized» debe interpretarse con cautela. Exploración oral y observación visual de función, postura de reposo y deglución, predominantemente desenlaces clínicos subjetivos.
- **Criterio diagnóstico de anquiloglosia:** FUNCIONAL. Criterio de inclusión del texto completo: «Tongue-tied according to TRMR classification». La introducción contrapone las escalas de aspecto y longitud (Kotlow, Coryllos) al TRMR de Zaghi.
- **Variables de resultado:** Movilidad lingual, deglución, respiración referida/observada y posturas de reposo de labios, lengua y mandíbula. **No consta en el texto revisado una medición objetiva de crecimiento esquelético ni polisomnografía antes/después.**
- **Resultados NUMÉRICOS verificados:** **78 pacientes** en A (terapia + frenuloplastia) frente a **77 en B** (terapia aislada). En A, **90 %** tuvo patrón de deglución considerado normal tras intervención; el **10 %** restante no mejoró según el informe. **Postura labial:** 86 % con labios en reposo calificado como normal tras intervención A, 11 % separados y aproximadamente 2 % otras posiciones, **p<0,001** para tendencia; en B los autores mencionan **8,5 %** con mejoría de postura labial. **Postura mandibular:** A p<0,001 en su comparación, frente a un paciente del grupo B con postura mandibular de reposo calificada como buena. **Mordida:** 72 % percibió mejoría y 28 % no, sin que esto equivalga a corrección esquelética demostrada. Los datos proceden del texto de resultados y figuras (no de un metaanálisis); **tablas, denominadores por subgrupo, comparaciones intergrupo ajustadas y cegamiento aún PENDIENTES DE VERIFICAR**.
- **Límites metodológicos / confusores:** **Desbalance basal importante de edad media (18 vs 26 años)**; asignación por día/orden sin ocultación documentada; evaluaciones visuales/subjetivas con **cegamiento de evaluadores no confirmado**; intervención quirúrgica imposible de cegar al paciente, posible expectativa; cointervenciones y adherencia requieren verificación; un solo entorno y Zaghi como coautor. No se verificaron desenlaces esqueléticos objetivos longitudinales.
- **Hallazgos contrarios o no significativos:** En el grupo operado un **10 % no alcanzó la deglución normal** según autores, principalmente por maloclusión severa. No se ha demostrado en estos datos que la frenuloplastia modifique el esqueleto ni mejore apnea medida por PSG.
- **Conclusión que sí permite / que no permite:** Sí: un estudio controlado clínico informó mejores **indicadores funcionales observados** tras frenuloplastia + terapia que tras terapia aislada, en una cohorte seleccionada con TRMR. **No** demostrar un efecto causal libre de sesgo, ni modificación de crecimiento maxilomandibular, ni mejoría de apnea objetiva. Las frases del artículo acerca de «restaurar el equilibrio del esqueleto» sobrepasan las variables medidas.
- **Licencia y derechos:** Acceso abierto, CC BY (según PMC).
- **Complemento desde el texto completo (17/10/2026):** el PDF lo presenta como ensayo aleatorizado prospectivo; la asignación por orden de entrada sigue siendo la del resumen. Cifras de tablas: `PENDIENTE DE VERIFICAR`.
- **Estado de lectura:** Resumen, métodos completos accesibles y pasajes de resultados del artículo abierto cotejados el **03/11/2026** ([PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11432234/)); **auditoría íntegra de tablas y cegamiento PENDIENTE DE VERIFICAR**. No registrar como lectura exhaustiva. Origen inicial: estudios citados en vídeos de Zaghi.

## Figuras

Licencia del artículo: CC BY 4.0. Figuras en PubMed Central (PMC11432234).

- **Figura 1.** Valoración inicial global por clase de Angle. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11432234/figure/jcm-13-05354-f001/). Copia local: figuras/LICHNOWSKA2024-fig1.jpg.
- **Figura 2.** Postura de la lengua en reposo antes y después, por grupo. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11432234/figure/jcm-13-05354-f002/). Copia local: figuras/LICHNOWSKA2024-fig2.jpg.
- **Figura 3.** Postura de los labios antes y después. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11432234/figure/jcm-13-05354-f003/). Copia local: figuras/LICHNOWSKA2024-fig3.jpg.
- **Figura 4.** Posición mandibular en reposo por grupo. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11432234/figure/jcm-13-05354-f004/). Copia local: figuras/LICHNOWSKA2024-fig4.jpg.
- **Figura 5.** Tipo de deglución. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11432234/figure/jcm-13-05354-f005/). Copia local: figuras/LICHNOWSKA2024-fig5.jpg.
- **Figura 6.** Mejora de la mordida. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11432234/figure/jcm-13-05354-f006/). Copia local: figuras/LICHNOWSKA2024-fig6.jpg.
- **Figura 7.** Tipo de respiración por grupo. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11432234/figure/jcm-13-05354-f007/). Copia local: figuras/LICHNOWSKA2024-fig7.jpg.
- **Figura 8.** Valoración global del proyecto (cajas). [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11432234/figure/jcm-13-05354-f008/). Copia local: figuras/LICHNOWSKA2024-fig8.jpg.
- **Figura 9.** Valoración global del proyecto (densidad antes y después). [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11432234/figure/jcm-13-05354-f009/). Copia local: figuras/LICHNOWSKA2024-fig9.jpg.

Crédito: figuras de Lichnowska A; Gnatek A; Tyszkiewicz S; Kozakiewicz M; Zaghi S (PMC11432234), CC BY 4.0. Las copias locales no se han modificado.

## Actualización del apartado de resultados, 03/11/2026

Los porcentajes de postura labial (86 % A; 8,5 % mejoría B), deglución (90 % normal A) y mejoría percibida de mordida (72 %) figuran en la sección 3 del artículo [abierto en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11432234/). **No** describir «mejoró la mordida» como avance de la mandíbula o cambios de la base ósea; la medición de respiración se describe clínicamente, no como resolución objetiva de OSA. Con la diferencia de edad basal y la asignación por llegada, estos efectos favorables observados merecen una interpretación prudente.

---

<!-- archivo: fuentes/articulos/2024-mckenna-ucin-frente-a-sanos.md -->
# Estudio: Tongue-tie in the Neonatal Intensive Care Unit Compared to Healthy Newborns

- **ID:** MCKENNA2024
- **Autores, año y revista:** McKenna MK; Rosen-Carole C; Burtner M et al.. Laryngoscope 2024;134(12):5152-5159.
- **DOI / PMID / URL:** DOI `10.1002/lary.31615`; PMID `39021346`
- **Tipo de estudio:** Datos prospectivos con hoja estandarizada.
- **Población y tamaño muestral:** 20.879 lactantes; 163 frenotomías (86 en maternidad, 77 en UCI neonatal).
- **Definición diagnóstica y técnicas:** Valoración de lactantes amamantados en maternidad y UCI neonatal.
- **Criterio diagnóstico de anquiloglosia:** MIXTO. Tipo de Coryllos, longitud punta-frenillo y puntuación de función.
- **Variables de resultado:** Prevalencia, frenotomía, función.
- **Resultados NUMÉRICOS verificados:** Diagnóstico de anquiloglosia: 3,3 % en maternidad frente a 5,4 % en UCI neonatal (p<0,01). Sin diferencia en tipo de Coryllos ni en función. Función mejor tras frenotomía en un subgrupo de UCI (p<0,01).
- **Límites metodológicos / confusores:** Un centro. Subgrupo pequeño para la función.
- **Hallazgos contrarios o no significativos:** No aplica.
- **Conclusión que sí permite / que no permite:** Sí: Decir que las herramientas estándar parecen aplicables en UCI neonatal. No: Generalizar a niños mayores.
- **Licencia y derechos:** Derechos del editor. Aquí solo metadatos y resumen propio.
- **Estado de lectura:** Resumen PubMed y texto completo revisados el 17/10/2026.

## Figuras

Licencia: derechos del editor (no se copian imágenes). Leyendas leídas en el texto completo; puede haber más figuras que las listadas.

- **Figura 1.** Hoja de registro en la historia electrónica. [Ver en el artículo](https://doi.org/10.1002/lary.31615), figura 1.
- **Figura 2.** Diseño y selección. [Ver en el artículo](https://doi.org/10.1002/lary.31615), figura 2.
- **Figura 3.** Protocolo de valoración en UCI neonatal. [Ver en el artículo](https://doi.org/10.1002/lary.31615), figura 3.
- **Figura 4.** Distribución de tipos de Coryllos. [Ver en el artículo](https://doi.org/10.1002/lary.31615), figura 4.
- **Figura 5.** Puntuación de función antes y después de la frenotomía en UCI neonatal. [Ver en el artículo](https://doi.org/10.1002/lary.31615), figura 5.

---

<!-- archivo: fuentes/articulos/2024-melong-frenotomia-habla.md -->
# Estudio: The Effect of Tongue-Tie Release on Speech Articulation and Intelligibility

- **ID:** MELONG2024
- **Autores, año y revista:** Melong J; Bezuhly M; Hong P. Ear Nose Throat J 2024;103(7):NP450-NP454 (online diciembre de 2021).
- **DOI / PMID / URL:** DOI `10.1177/01455613211064045`; PMID `34911396`
- **Tipo de estudio:** Cohorte prospectiva antes y después, sin control.
- **Población y tamaño muestral:** 25 niños mayores de 2 años derivados por problemas de habla atribuidos a anquiloglosia (media 3,7 años; 20 niños).
- **Definición diagnóstica y técnicas:** Valoración por ORL pediátrico; articulación con GFTA-2 por logopeda; inteligibilidad por revisores independientes. Frenotomía en consulta. Reevaluación al mes.
- **Criterio diagnóstico de anquiloglosia:** Valoración por un ORL pediátrico; escala o medida usada: PENDIENTE DE VERIFICAR (no consta en el resumen).
- **Variables de resultado:** Puntuación GFTA-2 e inteligibilidad.
- **Resultados NUMÉRICOS verificados:** GFTA-2 85,61 → 87,54 (P=0,5). Inteligibilidad 3,15 → 3,21 (P=0,43). El 87,9 % de los errores eran propios de la edad.
- **Límites metodológicos / confusores:** 25 niños, seguimiento de 1 mes, sin control. Si el criterio no fue funcional, puede haber incluido frenillos sin restricción real.
- **Hallazgos contrarios o no significativos:** No aplica.
- **Conclusión que sí permite / que no permite:** Sí: Decir que en esta serie la frenotomía no mejoró el habla al mes y que la mayoría de errores eran de la edad. No: Generalizar a niños con restricción funcional definida por TRMR o a seguimientos largos.
- **Licencia y derechos:** Derechos del editor. Aquí solo metadatos y resumen propio.
- **Estado de lectura:** Resumen PubMed revisado el 17/10/2026.

## Figuras

Figuras no revisadas: el texto completo no está en acceso abierto en PMC. [Ver el artículo](https://doi.org/10.1177/01455613211064045).

---

<!-- archivo: fuentes/articulos/2024-povoa-santos-meta.md -->
# Estudio: Ankyloglossia and malocclusion: A systematic review and meta-analysis

- **ID:** POVOA2024
- **Autores, año y revista:** Póvoa-Santos L; Lacerda-Santos R; Alvarenga-Brant R; Notaro SQ; Souza-Oliveira AC; Occhi-Alexandre IGP; Martins-Pfeifer CC. *J Am Dent Assoc* 2024;155(1):59-73.e9.
- **DOI / PMID / URL:** DOI `10.1016/j.adaj.2023.09.014`; PMID `37999659`; PROSPERO `CRD42021248034`; [original](https://doi.org/10.1016/j.adaj.2023.09.014).
- **Tipo de estudio:** Revisión sistemática y metaanálisis de estudios observacionales. Calidad con las herramientas del Joanna Briggs Institute y certeza con GRADE. Búsqueda en 8 bases de datos hasta el 01/07/2022.
- **Población y tamaño muestral:** 11 estudios (5 transversales y 6 de casos y controles), 2.904 personas de entre 4 y 67 años; no hubo cohortes prospectivas de crecimiento.
- **Definición diagnóstica y técnicas:** Se admitió cualquier prueba diagnóstica de anquiloglosia y diferentes desenlaces oclusales. Los metaanálisis de clase de Angle compararon longitud/inserción del frenillo (4 estudios) o reducción de apertura bucal (2 estudios); otros resultados se sintetizaron narrativamente.
- **Criterio diagnóstico de anquiloglosia:** MIXTO. La eTable 5 verifica 11 estudios con criterios anatómicos y funcionales parciales (Kotlow, inserción, succión, elevación, reducción de apertura y TRMR-TIP).
- **Variables de resultado:** Clase de Angle, mordidas, dimensiones intercaninas e intermolares, discrepancia dentoalveolar, medidas cefalométricas, pendiente palatina y reducción de apertura bucal.

## Qué midieron los 11 estudios — eTable 5, páginas 22-23

| Estudio (año en tabla 1) | Diagnóstico empleado | Qué pregunta puede abordar |
|---|---|---|
| García-Pola 2002 | Diferencia de apertura con punta lingual en papila y distancias dentales; procedimientos por grupos | Movilidad anterior indirecta, no función posterior completa |
| Melink 2010 | Elevación hacia incisivos superiores y valoración clínica de frenillo corto | Evaluación mixta simple |
| Jang 2011 | Regla de longitud del frenillo con punta elevada; reducción de apertura | Longitud y movilidad indirecta |
| Morisso 2012 | Succión palatina, elevación y protrusión; asistencia con espátula cuando no alcanzaba | Función parcial |
| Srinivasan 2013 | Kotlow | Longitud/aspecto |
| Azizi 2014 | Medición de longitud con punta elevada | Predominantemente anatómica |
| Meenakshi 2014 | Longitud con calibrador y postura lingual en papila; reducción de apertura | Mixta, no examen funcional global |
| Ruffoli 2015 | Longitud e inserción por método directo e indirecto | Predominantemente anatómica |
| Sepet 2015 | Frenillo corto/grueso y Kotlow | Anatómica |
| Yoon 2017 | TRMR-TIP y Kotlow | Función anterior y longitud, **no TRMR-LPS** |
| Calvo-Henríquez 2022 | Marchesan modificado | Mixta; detalles del protocolo primario por verificar |

**No eran 11 estudios basados únicamente en Kotlow.** La lista de referencias indirectamente deducida en una versión anterior de esta ficha era errónea: incluía a Pompéia 2017, que no fue uno de los 11, y omitía a Melink 2010. Los años de algunos estudios no coinciden entre tabla 1 y tablas suplementarias; se reproducen aquí **los años de tabla 1**, pendientes de resolver con las publicaciones primarias.

## Resultados NUMÉRICOS verificados del texto completo

- **Longitud/inserción por clase de Angle (4 estudios):** clase III vs I, DME 0,37 (IC 95 % −0,50 a 1,25; **I²=93 %**); clase III vs II, DME 0,55 (IC 95 % −0,52 a 1,63; **I²=95 %**). Las diferencias combinadas no son concluyentes y existe heterogeneidad muy elevada (figura 3).
- **Reducción de apertura bucal (2 estudios):** clase III vs I, diferencia media **6,67 mm** (IC 95 % 4,01–9,33); clase III vs II, **5,04 mm** (2,35–7,72). Ambas asociaciones son significativas, pero de certeza **baja**; no demuestran que la restricción lingual sea la causa (figura 4).
- **Dimensiones maxilares (Srinivasan 2013):** intercanina 33,0 mm vs 35,4 mm e intermolar 42,8 mm vs 48,4 mm en grupos con y sin anquiloglosia, respectivamente (p<0,001). No son directamente mediciones de crecimiento esquelético.
- **Yoon 2017:** TRMR-TIP se asoció con pendiente palatina (p=0,0118), mientras que la clasificación anatómica de Kotlow no mostró esa asociación para el mismo desenlace (p=0,2907). Otros resultados transversales de dimensión maxilar también fueron significativos; varios mandibulares y sagitales, no.
- **Calvo-Henríquez 2022:** clase III en 12/50 con anquiloglosia frente a 4/50 sin anquiloglosia, p=0,029; asociación observacional, no prueba causal.
- **Certidumbre global:** baja o muy baja para todos los desenlaces según GRADE.

## Límites metodológicos y posible mal uso de sus conclusiones

1. **Temporalidad:** solo estudios transversales o casos y controles; ninguno demuestra cambios de crecimiento por restricción funcional longitudinal.
2. **Exposiciones distintas:** mezclar longitud, inserción, apertura, TRMR-TIP y exploraciones funcionales parciales dificulta extrapolar un efecto combinado a una definición funcional bien especificada.
3. **Confusión:** las eTables 6 y 7 califican negativamente la identificación/control de factores de confusión de los estudios incluidos. Esto afecta **tanto** a asociaciones favorables como a resultados nulos.
4. **Heterogeneidad:** en los análisis de longitud/inserción de clase III, I² 93 % y 95 %, con efectos individuales de distinta dirección.
5. **Desenlace:** clase de Angle, anchuras dentoalveolares, dimensión ósea y posición/crecimiento maxilar no son intercambiables.
6. **Posibilidad de interpretación TRMR (no documentada como sesgo de esta revisión):** el cociente depende de la apertura máxima usada como denominador. Una apertura máxima limitada **podría** producir un porcentaje elevado con el mismo numerador; no consta que esto alterara la muestra de Yoon 2017. La elevación TIP no mide por sí sola succión posterior ni postura espontánea.

- **Hallazgos contrarios o no significativos:** No hay una asociación agregada concluyente entre longitud/inserción del frenillo y clase de Angle; en algunas variables mandibulares Yoon no encontró asociación. Estos negativos cuentan, pero su alcance se limita a los constructos estudiados.
- **Conclusión que sí permite / que no permite:** La revisión identifica **incertidumbre** por evidencia de baja/muy baja certeza. Permite comunicar algunos resultados significativos específicos y otros no concluyentes. No demuestra ni que la anquiloglosia cause de forma generalizada maloclusión ni que una restricción funcional correctamente caracterizada **no pueda** influir sobre el crecimiento maxilar. Tampoco evalúa la eficacia preventiva de frenectomía, ni responde a preguntas de sueño, lactancia o postura.
- **Licencia y derechos:** Copyright American Dental Association/Elsevier. Ficha redactada como síntesis original; no se adjuntan PDF, tablas ni figuras de la editorial.
- **Estado de lectura:** Texto completo y material suplementario (especialmente eTables 5-7 y figuras 3-4) consultados el 03/11/2026 a partir de ejemplar facilitado para análisis. Los 11 originales no han sido reanalizados a texto completo como parte de esta ficha.

## Figuras

Examinadas las figuras de metaanálisis en el texto completo; no se reproducen por derechos de autor. [Artículo original](https://doi.org/10.1016/j.adaj.2023.09.014).

---

<!-- archivo: fuentes/articulos/2024-preedeewong-frenectomia-apnea-ensayo.md -->
# Estudio: Impact of frenectomy on the oral exercise in patients with ankyloglossia and obstructive sleep apnea: double-blind randomized controlled clinical trials

- **ID:** PREEDEEWONG2024
- **Autores, año y revista:** Preedeewong C; Chirakalwasan N; Kaboosaya B. Clin Oral Investig 2024;28(10):566.
- **DOI / PMID / URL:** DOI `10.1007/s00784-024-05932-8`; PMID `39365358`
- **Tipo de estudio:** Ensayo aleatorizado doble ciego (TCTR20220429002).
- **Población y tamaño muestral:** 15 adultos de 20 a 60 años con apnea leve o moderada: 8 ejercicio y 7 ejercicio más frenectomía.
- **Definición diagnóstica y técnicas:** 3 meses de ejercicios orales; polisomnografía, Epworth, fuerza lingual y calidad de vida.
- **Criterio diagnóstico de anquiloglosia:** FUNCIONAL. Inclusión con TRMR grado 2 a 4 valorado por dentista (texto completo).
- **Variables de resultado:** IAH, Epworth, fuerza lingual, calidad de vida.
- **Resultados NUMÉRICOS verificados:** Epworth bajó en ambos grupos (-2,88 y -4,00). El IAH subió en ambos sin significación. La fuerza lingual aumentó en ambos. Satisfacción 100 % frente a 57,1 %.
- **Límites metodológicos / confusores:** Muestra muy pequeña. 3 meses.
- **Hallazgos contrarios o no significativos:** La frenectomía no mejoró la apnea ni la calidad de vida.
- **Conclusión que sí permite / que no permite:** Sí: Citar un ensayo pequeño, con criterio funcional, sin beneficio sobre la apnea. No: Concluir que la frenectomía no sirve en apnea: falta potencia.
- **Licencia y derechos:** Derechos del editor. Aquí solo metadatos y resumen propio.
- **Estado de lectura:** Resumen PubMed y texto completo revisados el 17/10/2026.

## Figuras

Licencia: derechos del editor (no se copian imágenes). Leyendas leídas en el texto completo; puede haber más figuras que las listadas.

- **Figura 1.** Ejercicio «pintar» con la lengua. [Ver en el artículo](https://doi.org/10.1007/s00784-024-05932-8), figura 1.
- **Figura 2.** Ejercicio de comisuras. [Ver en el artículo](https://doi.org/10.1007/s00784-024-05932-8), figura 2.
- **Figura 3.** Ejercicio de chasquido. [Ver en el artículo](https://doi.org/10.1007/s00784-024-05932-8), figura 3.
- **Figura 4.** Diseño y calendario del estudio. [Ver en el artículo](https://doi.org/10.1007/s00784-024-05932-8), figura 4.
- **Figura 5.** Satisfacción por grupo. [Ver en el artículo](https://doi.org/10.1007/s00784-024-05932-8), figura 5.
- **Figura 6.** Calidad de vida por grupo. [Ver en el artículo](https://doi.org/10.1007/s00784-024-05932-8), figura 6.

---

<!-- archivo: fuentes/articulos/2024-sahoo-laser-miofuncional-casos.md -->
# Estudio: Effect of myofunctional exercise combined with laser-assisted frenectomy in the management of paediatric tongue tie

- **ID:** SAHOO2024
- **Autores, año y revista:** Sahoo S; Balaji S; Haridoss S et al.. BMJ Case Rep 2024;17(8).
- **DOI / PMID / URL:** DOI `10.1136/bcr-2024-262067`; PMID `39216880`
- **Tipo de estudio:** Tres casos.
- **Población y tamaño muestral:** 3 niños.
- **Definición diagnóstica y técnicas:** Frenectomía con láser de diodo y ejercicios miofuncionales.
- **Criterio diagnóstico de anquiloglosia:** El texto cita la clasificación de Kotlow; la aplicada a cada caso: PENDIENTE DE VERIFICAR.
- **Variables de resultado:** Movilidad y habla.
- **Resultados NUMÉRICOS verificados:** Mejora descrita sin cifras en el resumen.
- **Límites metodológicos / confusores:** Tres casos.
- **Hallazgos contrarios o no significativos:** No aplica.
- **Conclusión que sí permite / que no permite:** Sí: Ilustrar el abordaje combinado. No: Concluir eficacia.
- **Licencia y derechos:** Derechos del editor. Aquí solo metadatos y resumen propio.
- **Estado de lectura:** Resumen PubMed y texto completo revisados el 17/10/2026.

## Figuras

Licencia: derechos del editor (no se copian imágenes). Leyendas leídas en el texto completo; puede haber más figuras que las listadas.

- **Figura 1.** Caso 1: antes, durante y después del láser. [Ver en el artículo](https://doi.org/10.1136/bcr-2024-262067), figura 1.
- **Figura 2.** Caso 2. [Ver en el artículo](https://doi.org/10.1136/bcr-2024-262067), figura 2.
- **Figura 3.** Caso 3. [Ver en el artículo](https://doi.org/10.1136/bcr-2024-262067), figura 3.

---

<!-- archivo: fuentes/articulos/2024-sun-repetibilidad-ct-via-aerea.md -->
# Estudio: Successive measurement errors of consecutive computed tomography for airway-related craniofacial dimensional measurements

- **ID:** SUN2024CT
- **Autores, año y revista:** Sun J-S; Lin S-Y; Hsieh C-Y; Hung M-C; Tai H-C; Chang JZ-C. *Journal of Dental Sciences* 2024;19(4):1961–1971.
- **DOI / PMID / URL:** DOI `10.1016/j.jds.2024.07.033`; PMID `39347062`; PMCID `PMC11437345`; [original abierto](https://www.sciencedirect.com/science/article/pii/S199179022400254X); [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11437345/).
- **Tipo de estudio:** Estudio retrospectivo de **repetibilidad entre dos exploraciones tomográficas** en los mismos pacientes (test–retest), comparando **CBCT** y **MDCT** y los programas de segmentación **Amira** y **Dolphin**. No es un ensayo clínico de intervención.
- **Población y tamaño muestral:** **20 adultos**: 10 con dos CBCT y otros 10 con dos MDCT; cuatro DICOM por modalidad/técnica no: **40 conjuntos DICOM en total** (20 sujetos × 2 momentos), cada uno analizado con ambos programas. Diez CBCT elegidos aleatoriamente entre 27 pacientes elegibles; MDCT emparejados por edad, sexo, raza, oclusión y patrón craneofacial. Intervalo entre imágenes **<1 año**, sin tratamiento de cabeza/cuello registrado entre ellas.
- **Definición diagnóstica y técnicas:** Medición de **26 variables** lineales, angulares y de vía aérea en CBCT/MDCT: base maxilar, anchuras dentarias, medidas cefalométricas, lordosis cervical, volumen intraoral/nasofaríngeo/orofaríngeo/hipofaríngeo y área transversal mínima (**MCA**) de orofaringe. Un operador evaluó imágenes **codificadas a ciegas** y calculó repetibilidad del mismo examinador con **ICC** sobre imágenes repetidas; después se estimó error **entre dos exploraciones sucesivas** como diferencia absoluta de las mediciones. Protocolos y posiciones **NO equivalentes**: MDCT supino; CBCT erguido. El software puede tener segmentación/umbrales distintos.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA: no estudia frenillo ni función lingual. Investiga la fiabilidad de un **instrumento de medida** para interpretar trabajos de morfología/vía aérea.
- **Variables de resultado:** Diferencia absoluta media entre exploraciones sucesivas y entre software, en mm, grados, mm² y mm³; **no** volumen o MCA como indicador validado de AHI/PSG.
- **Resultados NUMÉRICOS verificados (texto completo, tablas 1, 3 y 4):**
  - A pesar de ICC casi perfecto para repetir segmentaciones sobre una misma imagen (**ICC 0,998–0,999** con Amira para variables de vía aérea), al comparar **dos tomografías del mismo paciente sin tratamiento** las diferencias de volumen fueron importantes.
  - **Volumen orofaríngeo (OAV), Dolphin en CBCT:** diferencia absoluta media entre imágenes sucesivas **6097,1 ± 4616,69 mm³**; Dolphin con MDCT **1793,1 ± 1043,83 mm³** (**p=0,014**, comparación de modalidad/protocolo; más de 3 veces). **Amira con CBCT**: **3574 ± 3589,29 mm³**.
  - **Volumen intraoral (IAV)** con cualquiera de modalidades y programas: diferencias medias absolutas de aproximadamente **4808–6097 mm³**, extraordinariamente variables.
  - **Área transversal mínima orofaríngea (MCA):** diferencias medias CBCT **46,9 ± 44,78 mm²** (Amira) y **57,4 ± 56,63 mm²** (Dolphin), frente a MDCT **28,1 ± 22,97 mm²** y **25,9 ± 20,86 mm²**, respectivamente; comparaciones CBCT vs MDCT de MCA **no significativas** (p=0,646 y p=0,232). **No confundir el volumen OAV con MCA**.
  - **Ángulo de lordosis cervical:** diferencias consecutivas medias de **~4,59 a 5,54 grados** en ambos programas y modalidades, aunque no hubo intervención en cabeza/cuello.
  - **Ocho de 26** mediciones comunes superaron 1 mm o grado de discrepancia en algunos ajustes, sobre todo Dolphin; las comparaciones de diferencias sucesivas entre software y modalidad fueron **significativas para algunos desenlaces**, no para todos.
- **Límites metodológicos / confusores:** **Solo 10 personas por modalidad**, intervalos de imagen de hasta 1 año (podrían intervenir cambios reales no atribuidos a tratamiento) y posiciones sistemáticamente distintas (**CBCT erguido vs MDCT supino**). Por eso **NO puede atribuirse toda la diferencia CBCT–MDCT al escáner o programa**: posición corporal, respiración, protocolo de adquisición, umbral de segmentación, duración de examen y campos de visión pueden influir. La alta ICC **intraimagen** indica repetición de lectura, no **estabilidad entre días**. No hay validación de las variables de imagen frente a PSG, flujo nasal ni respuesta a tratamiento.
- **Hallazgos contrarios o no significativos:** No todas las medidas fueron inestables: numerosas medidas esqueléticas con Amira tuvieron error <1 mm/1 grado; las diferencias CBCT vs MDCT de error absoluto de MCA **no fueron significativas** en tabla 3. El trabajo no demuestra que toda imagen CBCT carezca de utilidad clínica ni que todos los cambios publicados se deban a error.
- **Conclusión que sí permite / que no permite:** **Sí:** al comparar cambios de vía aérea por CBCT (p. ej. antes y después de ortodoncia, expansión, extracciones, cirugía) hay que considerar **variabilidad entre adquisiciones**, orientación/posición cervical, segmentación, software, tamaño del cambio frente a error test–retest y desenlace funcional separado. **No:** invalidar automáticamente toda cuantificación de vía aérea, demostrar que extracciones no sirven/hacen daño, atribuir causalmente la variación a un frenillo ni inferir alteración de AHI/PSG.
- **Licencia y derechos:** Original abierto **CC BY-NC-ND 4.0**. Síntesis original sin imágenes, tablas textuales reproducidas ni PDF en repositorio.
- **Estado de lectura:** **Texto íntegro HTML (incluidos métodos, tablas 1–4, discusión y limitaciones) consultado el 03/11/2026** mediante copia pública del artículo indexada en PMC/portal editorial. No se han verificado las figuras pixel a pixel ni rehecho cálculos de los DICOM.

## Figuras

No reproducidas. [Artículo original](https://doi.org/10.1016/j.jds.2024.07.033).

---

<!-- archivo: fuentes/articulos/2024-thomas-aap-informe-clinico.md -->
# Estudio: Identification and Management of Ankyloglossia and Its Effect on Breastfeeding in Infants: Clinical Report

- **ID:** THOMAS2024
- **Autores, año y revista:** Thomas J; Bunik M; Holmes A; Keels MA; Poindexter B; Meyer A; Gilliland A; American Academy of Pediatrics. *Pediatrics* 2024;154(2):e2024067605.
- **DOI / PMID / URL:** DOI `10.1542/peds.2024-067605`; PMID `39069819`; [informe completo disponible gratuitamente en AAP](https://publications.aap.org/pediatrics/article/154/2/e2024067605/198022/Identification-and-Management-of-Ankyloglossia-and).
- **Tipo de estudio:** **Informe clínico / posicionamiento de la Academia Americana de Pediatría**, con recomendaciones basadas en revisión narrativa de literatura; **no es un ensayo, metaanálisis ni consenso de todas las especialidades**.
- **Población y tamaño muestral:** Lactantes en etapa de amamantamiento y díadas madre-bebé. **No es un estudio con muestra primaria**, no procede asignar n.
- **Definición diagnóstica y técnicas:** Define «anquiloglosia sintomática» como frenillo restrictivo en exploración junto con dificultades persistentes de lactancia que **no mejoran con apoyo adecuado**. Exige exploración del lactante y evaluación funcional de toma/transferencia y de otras causas. Recomienda valorar aspecto del frenillo, capacidad de elevar y extender lengua, coordinación de succión, observación de toma, evolución de peso y dolor; no identifica una única escala diagnóstica validada como patrón de referencia.
- **Criterio diagnóstico de anquiloglosia:** MIXTO: exploración anatómica **más disfunción de lactancia demostrada** y evaluación de movilidad; NO basta con ver un frenillo de apariencia corta. Este documento trata **lactantes**, no TRMR del adulto ni problemas ortodóncicos longitudinales.
- **Variables de resultado:** Dolor materno, agarre y transferencia de leche, ganancia ponderal y seguridad de frenotomía; recomendaciones sobre evaluación, manejo y seguimiento.
- **Resultados NUMÉRICOS verificados:** El documento refiere que **menos de la mitad** de lactantes con hallazgos anatómicos compatibles presentan dificultades de lactancia (a partir de estudios citados); no es una estimación de una cohorte propia. Afirma que la frenotomía **puede aliviar el dolor del pezón a corto plazo**, pero la evidencia general para resultados de lactancia duraderos es limitada y heterogénea. El informe no aporta un efecto agrupado causal propio.
- **Límites metodológicos / confusores:** Informe centrado en **lactancia neonatal**, no desarrolla un ensayo sobre crecimiento craneofacial, sueño, postura ni función en adultos. Valoración clínica multidisciplinar; evidencia observacional y ensayos cortos; confusión entre dolor materno, anatomía y otros problemas de alimentación.
- **Hallazgos contrarios o no significativos:** La AAP señala que la prevención de posibles problemas futuros de habla u OSA **mediante frenotomía neonatal no está sustentada por pruebas suficientes**; no recomienda liberación preventiva ni de frenillos bucales/labiales para mejorar lactancia; el término «anquiloglosia posterior» carece de una definición compartida y no debe usarse como única indicación quirúrgica. No reconoce superioridad del láser sobre tijeras con evidencia suficiente. **No recomienda estiramientos de herida posoperatorios** al no existir base suficiente.
- **Conclusión que sí permite / que no permite:** Sí: citar la posición AAP de priorizar evaluación funcional y apoyo de lactancia antes de contemplar cirugía; intervenir selectivamente cuando persisten síntomas. No: presentar estas recomendaciones como **prueba experimental de ausencia universal** de influencia del frenillo sobre crecimiento mandibular/posición lingual posterior en niños mayores o adultos, porque no lo estudia. Tampoco se puede afirmar que las dudas de la AAP prueben utilidad de cirugía preventiva.
- **Licencia y derechos:** Informe en lectura gratuita, pero **copyright de AAP**; solo síntesis propia y enlace (no subir su PDF ni reproducir figuras).
- **Estado de lectura:** Texto completo HTML gratuito (definiciones, evaluación, tratamiento y recomendaciones 1–9) leído y contrastado el **03/11/2026** a través de la [página oficial AAP](https://publications.aap.org/pediatrics/article/doi/10.1542/peds.2024-067605/198022/Identification-and-Management-of-Ankyloglossia-and). No se ha reanalizado individualmente cada ensayo citado.

## Figuras

No se reproducen figuras editoriales ni el algoritmo; [informe original](https://doi.org/10.1542/peds.2024-067605).

---

<!-- archivo: fuentes/articulos/2024-tomita-protrusion-maxilar.md -->
# Estudio: Maxillary Protrusion with Severe Overjet Treated by Maxillary Anterior Alveolar Osteotomy

- **ID:** TOMITA2024
- **Autores, año y revista:** Tomita D; Haga S; Tanzawa F et al.. Case Rep Dent 2024;2024:3850765.
- **DOI / PMID / URL:** DOI `10.1155/2024/3850765`; PMID `38497089`; https://pmc.ncbi.nlm.nih.gov/articles/PMC10944346/
- **Tipo de estudio:** Caso clínico.
- **Población y tamaño muestral:** Una mujer de 32 años con incisivos superiores muy proinclinados.
- **Definición diagnóstica y técnicas:** Osteotomía alveolar anterior del maxilar con ortodoncia. Seguimiento de 2 años.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA: el estudio no diagnostica anquiloglosia.
- **Variables de resultado:** Cefalometría y oclusión antes y después.
- **Resultados NUMÉRICOS verificados:** Texto completo: SNA 82,6° (norma 82,3), SNB 73,1° en el texto y 73,2° en la tabla (norma 78,9), ANB 9,4° (norma 3,4). Tras el tratamiento, SNA 75,9°, SNB 70,1°, ANB 5,8°.
- **Límites metodológicos / confusores:** Un solo caso.
- **Hallazgos contrarios o no significativos:** Los autores lo llaman prognatismo maxilar, pero su SNA está en la norma y el SNB muy por debajo: la diferencia viene sobre todo de la mandíbula retrasada.
- **Conclusión que sí permite / que no permite:** Sí: Usarlo como ejemplo ilustrado de clase II con resalte grande y proinclinación. No: Generalizar.
- **Licencia y derechos:** CC BY 4.0 (según notas de trabajo, sin verificar). Se puede reutilizar citando.
- **Estado de lectura:** Resumen PubMed y tabla cefalométrica del texto completo (PMC) revisados el 17/10/2026.

## Figuras

Licencia del artículo: CC BY 4.0. Figuras en PubMed Central (PMC10944346).

- **Figura 1.** Registros previos: fotos de cara y boca, ortopantomografía y telerradiografías. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10944346/figure/fig1/).
- **Figura 2.** Objetivo quirúrgico: trazado antes (azul) y después (rojo). [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10944346/figure/fig2/).
- **Figura 3.** Fotos intraorales antes y después de la cirugía. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10944346/figure/fig3/).
- **Figura 4.** Registros al terminar el tratamiento. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10944346/figure/fig4/).
- **Figura 5.** Registros a los 2 años. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10944346/figure/fig5/).
- **Figura 6.** Superposición cefalométrica antes, después y a los 2 años. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10944346/figure/fig6/).
- **Figura 7.** Cambio de la oclusión anterior. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10944346/figure/fig7/).

Crédito: figuras de Tomita D; Haga S; Tanzawa F et al (PMC10944346), CC BY 4.0.

Es un caso clínico de una sola paciente: todas las figuras (fotos, radiografías y también los trazados de las figuras 2 y 6) solo se enlazan.

---

<!-- archivo: fuentes/articulos/2025-ashley-belleza-ia.md -->
# Estudio: What Does it Mean to Be Beautiful? Exploring the Limits of AI-Driven Beauty Assessment

- **ID:** ASHLEY2025
- **Autores, año y revista:** Ashley E; Walker L; Chadha P. J Clin Aesthet Dermatol 2025;18(4):24-27.
- **DOI / PMID / URL:** PMID `40256342`; https://pmc.ncbi.nlm.nih.gov/articles/PMC12007659/; sin DOI
- **Tipo de estudio:** Comentario.
- **Población y tamaño muestral:** No aplica.
- **Definición diagnóstica y técnicas:** No aplica.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA: el estudio no diagnostica anquiloglosia.
- **Variables de resultado:** No aplica.
- **Resultados NUMÉRICOS verificados:** Sin cifras.
- **Límites metodológicos / confusores:** Opinión.
- **Hallazgos contrarios o no significativos:** No aplica.
- **Conclusión que sí permite / que no permite:** Sí: Citar los límites de medir la belleza de forma objetiva. No: Usarlo como evidencia.
- **Licencia y derechos:** Acceso abierto en PMC. Licencia PENDIENTE DE VERIFICAR.
- **Estado de lectura:** Resumen PubMed y texto completo revisados el 17/10/2026.

## Figuras

Licencia del artículo: Derechos del editor. No se copian imágenes.

Figuras no extraídas: la versión de PMC no se puede leer por la API. [Ver el artículo en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12007659/). Descripción: `PENDIENTE DE VERIFICAR`.

---

<!-- archivo: fuentes/articulos/2025-bhatt-ontario-encuesta.md -->
# Estudio: Incidence of oral tie diagnosis and treatment in Southwestern Ontario: A survey study

- **ID:** BHATT2025
- **Autores, año y revista:** Bhatt A; Turner B; Davidson J et al.. Int J Pediatr Otorhinolaryngol 2025;192:112306.
- **DOI / PMID / URL:** DOI `10.1016/j.ijporl.2025.112306`; PMID `40107227`
- **Tipo de estudio:** Encuesta en consultas pediátricas.
- **Población y tamaño muestral:** 266 familias.
- **Definición diagnóstica y técnicas:** Cuestionario.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA. Diagnóstico referido por los padres.
- **Variables de resultado:** Diagnóstico, indicación, tratamiento, complicaciones, coste, satisfacción.
- **Resultados NUMÉRICOS verificados:** 53,0 % con diagnóstico de frenillo. Motivo principal: lactancia (69,7 %). Tratamiento recomendado al 78,8 %. Dolor 24,2 %, sangrado leve o moderado 11,0 %. Satisfechos 84,4 %.
- **Límites metodológicos / confusores:** Encuesta, autoinforme.
- **Hallazgos contrarios o no significativos:** Los autores lo leen como posible sobrediagnóstico.
- **Conclusión que sí permite / que no permite:** Sí: Citar la preocupación por sobrediagnóstico en lactantes. No: Medir prevalencia real.
- **Licencia y derechos:** Derechos del editor. Aquí solo metadatos y resumen propio.
- **Estado de lectura:** Resumen PubMed y texto completo revisados el 17/10/2026.

## Figuras

Licencia: derechos del editor (no se copian imágenes). Leyendas leídas en el texto completo; puede haber más figuras que las listadas.

- **Figura 1.** Recomendaciones de tratamiento según quién las dio. [Ver en el artículo](https://doi.org/10.1016/j.ijporl.2025.112306), figura 1.
- **Figura 2.** Tratamientos recomendados con varios frenillos. [Ver en el artículo](https://doi.org/10.1016/j.ijporl.2025.112306), figura 2.
- **Figura 3.** Coste del tratamiento quirúrgico y no quirúrgico. [Ver en el artículo](https://doi.org/10.1016/j.ijporl.2025.112306), figura 3.

---

<!-- archivo: fuentes/articulos/2025-capd-canada-posicionamiento.md -->
# Estudio: Position Statement on Ankyloglossia and Breastfeeding (Canadian Academy of Pediatric Dentistry / Académie Canadienne de Dentisterie Pédiatrique)

- **ID:** CAPD2025
- **Autores, año y revista:** Canadian Academy of Pediatric Dentistry (CAPD/ACDP). Posicionamiento publicado en su web el 1 de marzo de 2025, en inglés y en francés.
- **DOI / PMID / URL:** Sin DOI ni PMID. https://www.capd-acdp.org/Education/Ankyloglossia-and-Breastfeeding
- **Tipo de estudio:** Posicionamiento de una sociedad de odontopediatría. No describe método de búsqueda ni de consenso.
- **Población y tamaño muestral:** Lactantes amamantados y sus madres.
- **Definición diagnóstica y técnicas:** Define la anquiloglosia como «a restrictive lingual frenulum» y la describe como una variación de una estructura oral normal. Dice que el frenillo restrictivo puede dificultar la lactancia al limitar la extensión y la elevación de la lengua.
- **Criterio diagnóstico de anquiloglosia:** NO PROPONE NINGUNO. No nombra ninguna herramienta ni escala. En su recomendación 4 pide investigación con desenlaces a largo plazo para desarrollar un enfoque estandarizado de diagnóstico y manejo en lactantes.
- **Variables de resultado:** No aplica (posicionamiento).
- **Resultados NUMÉRICOS verificados:** No hay cifras. Cuatro recomendaciones: (1) valoración completa de la lactancia antes de cualquier tratamiento, con un enfoque multidisciplinar, porque la anquiloglosia puede ser solo uno de varios factores; (2) dentistas generales y especialistas pueden diagnosticar y tratar quirúrgicamente la anquiloglosia, con apoyo de consultoras de lactancia, enfermería, medicina de familia o pediatría; (3) consentimiento informado documentado que incluya las alternativas basadas en la evidencia, también no tratar; (4) más investigación.
- **Límites metodológicos / confusores (solo los relevantes):** Solo trata la lactancia. Se apoya en AAPD 2024, AAP 2024 (Thomas), AAO-HNS 2020 (Messner), ABM 2021, Cochrane 2017 y CPS 2015, sin revisión propia.
- **Otros resultados relevantes (si los hay):** Dice que la frenotomía puede mejorar la lactancia y reducir el dolor del pezón y que es en general segura y bien tolerada. Según una noticia de la Universidad de Toronto, el posicionamiento se publicó después de que un bebé de cuatro semanas muriera en Montreal en 2023 tras una intervención de frenillo hecha por un dentista (https://www.dentistry.utoronto.ca/news/helping-families-unknot-tongue-tie-surgery). Ese dato no aparece en el posicionamiento.
- **Aportación del estudio:** Confirma el posicionamiento canadiense de odontopediatría de 2025, que antes figuraba como pendiente de verificar en la tabla de sociedades.
- **Licencia y derechos:** Texto de la CAPD/ACDP. Aquí solo resumen propio.
- **Estado de lectura:** Texto completo de la página web (versión inglesa) leído el 05/11/2026.

## Figuras

No tiene figuras.

---

<!-- archivo: fuentes/articulos/2025-carneiro-ensayo-laser-bisturi.md -->
# Estudio: Diode laser versus scalpel in the surgical treatment of infant ankyloglossia: a randomized, parallel, double-blind, controlled clinical trial

- **ID:** CARNEIRO2025
- **Autores, año y revista:** Carneiro MLT; Verde MEQL; Silva Nascimento MFD et al. BMC Pediatr 2025;26(1):22.
- **DOI / PMID / URL:** DOI `10.1186/s12887-025-06307-y`; PMID `41345616`; PMC12781438; registro RBR466cykz.
- **Tipo de estudio:** Ensayo aleatorizado, paralelo, doble ciego.
- **Población y tamaño muestral:** Lactantes de 0 a 6 meses con anquiloglosia grave; 40 por grupo.
- **Definición diagnóstica y técnicas:** Láser de diodo frente a bisturí.
- **Criterio diagnóstico de anquiloglosia:** MIXTO. Inclusión por Bristol (BTAT 0-3), que combina aspecto y función.
- **Variables de resultado:** Movilidad (BTAT y «Tongue Test»), cicatrización, dolor (CRIES), lactancia (LATCH, IBFAT), peso.
- **Resultados NUMÉRICOS verificados:** Ambos grupos mejoraron sin diferencias en la mayoría de resultados. A los 7 días, mejor lactancia con bisturí (LATCH p=0,003; IBFAT p=0,024).
- **Límites metodológicos / confusores:** Sin grupo sin cirugía; seguimiento de 14 días.
- **Hallazgos contrarios o no significativos:** No aplica.
- **Conclusión que sí permite / que no permite:** Sí: Decir que láser y bisturí dieron resultados parecidos a corto plazo. No: Decir que la frenotomía es eficaz frente a no operar.
- **Licencia y derechos:** Acceso abierto (PMC). Aquí solo resumen propio.
- **Estado de lectura:** Resumen de PubMed revisado el 02/11/2026. El artículo incluye imágenes de pacientes: no se copian. Búsqueda de actualización del 02/11/2026.

## Figuras

Figuras no revisadas. [Ver el documento](https://pmc.ncbi.nlm.nih.gov/articles/PMC12781438/).

---

<!-- archivo: fuentes/articulos/2025-de-simone-maxilar-tras-frenectomia.md -->
# Estudio: Upper Jaw Development After Lingual Laser Frenectomy and Myofuntional Therapy

- **ID:** DESIMONE2025
- **Autores, año y revista:** De Simone L; Martinelli D; Tieri M et al.. Eur J Paediatr Dent 2025;26(1):32-36.
- **DOI / PMID / URL:** DOI `10.23804/ejpd.2024.2143`; PMID `38979956`
- **Tipo de estudio:** Casos y controles.
- **Población y tamaño muestral:** 30 niños.
- **Definición diagnóstica y técnicas:** Fotos, longitud del frenillo y medidas en modelos.
- **Criterio diagnóstico de anquiloglosia:** MIXTO. Longitud del frenillo; la introducción repasa Hazelbaker, Coryllos y Kotlow. Escala aplicada: PENDIENTE DE VERIFICAR.
- **Variables de resultado:** Parámetros del paladar anterior.
- **Resultados NUMÉRICOS verificados:** El resumen no da cifras; dice que cambiaron los parámetros del paladar anterior tras frenectomía láser y terapia miofuncional (p<0,01).
- **Límites metodológicos / confusores:** Muestra pequeña. Grupo control y tiempos PENDIENTE DE VERIFICAR.
- **Hallazgos contrarios o no significativos:** No aplica.
- **Conclusión que sí permite / que no permite:** Sí: Citarlo como estudio preliminar de cambios del paladar tras frenectomía y terapia. No: Afirmar crecimiento esquelético demostrado.
- **Licencia y derechos:** Derechos del editor. Aquí solo metadatos y resumen propio.
- **Estado de lectura:** Resumen PubMed y texto completo revisados el 17/10/2026.

## Figuras

Licencia: derechos del editor (no se copian imágenes). Leyendas leídas en el texto completo; puede haber más figuras que las listadas.

- **Figura 1.** Apertura máxima y medidas en modelo. [Ver en el artículo](https://doi.org/10.23804/ejpd.2024.2143), figura 1.
- **Figura 3.** Medidas en el modelo. [Ver en el artículo](https://doi.org/10.23804/ejpd.2024.2143), figura 3.

---

<!-- archivo: fuentes/articulos/2025-delgadillo-metaanalisis-lactancia.md -->
# Estudio: Frenectomy for ankyloglossia in children under five: a systematic review and meta-analysis on breastfeeding outcomes

- **ID:** DELGADILLO2025
- **Autores, año y revista:** Delgadillo GJ; Zlatar Rojas J; Muñoz MA; Luque-Martínez I. Int Breastfeed J 2025;20(1):81.
- **DOI / PMID / URL:** DOI `10.1186/s13006-025-00773-x`; PMID `41204347`; PMC12595756.
- **Tipo de estudio:** Revisión sistemática y metaanálisis.
- **Población y tamaño muestral:** 55 estudios en la síntesis cualitativa; 6 en el metaanálisis.
- **Definición diagnóstica y técnicas:** Siete bases de datos hasta el 24/10/2024.
- **Criterio diagnóstico de anquiloglosia:** MIXTO. Solo el 28,6 % de los estudios usó herramientas diagnósticas validadas. Las más usadas: Coryllos (27 %, aspecto) y Hazelbaker (19 %).
- **Variables de resultado:** Lactancia antes y después.
- **Resultados NUMÉRICOS verificados:** RR combinado 1,42 (IC 95 % 1,32-1,53), con I²=74,8 %. Al quitar un estudio atípico, RR 0,99 (IC 95 % 0,98-1,01), no significativo. Sesgo de detección en el 93 % de los estudios.
- **Límites metodológicos / confusores:** Pocos estudios para el metaanálisis; heterogeneidad; resultados autorreferidos.
- **Hallazgos contrarios o no significativos:** El efecto desaparece al quitar un estudio.
- **Conclusión que sí permite / que no permite:** Sí: Decir que la heterogeneidad de criterios diagnósticos impide recomendaciones firmes. No: Afirmar un efecto firme en ningún sentido.
- **Licencia y derechos:** Acceso abierto (PMC). Aquí solo resumen propio.
- **Estado de lectura:** Resumen de PubMed revisado el 02/11/2026. Búsqueda de actualización del 02/11/2026.

## Figuras

Figuras no revisadas. [Ver el documento](https://pmc.ncbi.nlm.nih.gov/articles/PMC12595756/).

---

<!-- archivo: fuentes/articulos/2025-dinh-ensayo-frenotomia-lactancia.md -->
# Estudio: Does Lingual Frenotomy Improve Breastfeeding in Newborns With Ankyloglossia? A Randomized Controlled Trial

- **ID:** DINH2025
- **Autores, año y revista:** Dinh LA; El-Rabbany M; Aslam S et al.. J Oral Maxillofac Surg 2025;83(7):806-812.
- **DOI / PMID / URL:** DOI `10.1016/j.joms.2025.04.006`; PMID `40319911`
- **Tipo de estudio:** Ensayo aleatorizado doble ciego, frenotomía frente a procedimiento simulado (2015-2017).
- **Población y tamaño muestral:** 112 díadas madre-recién nacido con dificultad de lactancia: 55 frenotomía y 57 simulado.
- **Definición diagnóstica y técnicas:** Derivación si LATCH <7 en dos tomas. Evaluación por consultora de lactancia cegada antes e inmediatamente después.
- **Criterio diagnóstico de anquiloglosia:** MIXTO. Hazelbaker Assessment Tool for Lingual Frenulum Function (aspecto y función), aplicado por un médico craneofacial (texto completo).
- **Variables de resultado:** Cambio en LATCH y dolor materno (Wong-Baker).
- **Resultados NUMÉRICOS verificados:** Sin diferencia en LATCH (0,02; IC -0,64 a 0,69; p=0,9) ni en dolor (0,32; IC -0,56 a 1,19; p=0,5).
- **Límites metodológicos / confusores:** Solo mide el efecto inmediato. Datos de 2015-2017 publicados en 2025.
- **Hallazgos contrarios o no significativos:** Resultado negativo.
- **Conclusión que sí permite / que no permite:** Sí: Decir que en este ensayo la frenotomía no mejoró de inmediato la lactancia ni el dolor frente a simulación. No: Concluir sobre efectos a días o semanas.
- **Licencia y derechos:** Derechos del editor. Aquí solo metadatos y resumen propio.
- **Estado de lectura:** Resumen PubMed y texto completo revisados el 17/10/2026.

## Figuras

Licencia: derechos del editor (no se copian imágenes). Leyendas leídas en el texto completo; puede haber más figuras que las listadas.

- **Figura 1.** Diagrama de inclusión y aleatorización. [Ver en el artículo](https://doi.org/10.1016/j.joms.2025.04.006), figura 1.

---

<!-- archivo: fuentes/articulos/2025-feldens-lactancia-autoeficacia.md -->
# Estudio: Ankyloglossia and breastfeeding self-efficacy in newborns: a birth cohort study

- **ID:** FELDENS2025
- **Autores, año y revista:** Feldens CA; Folayan MO; de Amorim LM et al.. BMC Oral Health 2025;25(1):64.
- **DOI / PMID / URL:** DOI `10.1186/s12903-025-05444-1`; PMID `39810128`; https://pmc.ncbi.nlm.nih.gov/articles/PMC11730490/
- **Tipo de estudio:** Cohorte de nacimiento con dos no expuestos por cada expuesto.
- **Población y tamaño muestral:** 88 recién nacidos de Canoas (Brasil): 31 con anquiloglosia y 57 sin ella.
- **Definición diagnóstica y técnicas:** Exploración al nacer. Entrevista domiciliaria a los 14 días con la escala BSES-SF.
- **Criterio diagnóstico de anquiloglosia:** MIXTO. Bristol Tongue Assessment Tool en el hospital.
- **Variables de resultado:** Autoeficacia materna en lactancia a los 14 días.
- **Resultados NUMÉRICOS verificados:** BSES-SF media 56,0 con anquiloglosia frente a 59,6 sin ella. Cociente ajustado 0,95 (IC 0,88-1,02; p=0,139).
- **Límites metodológicos / confusores:** Muestra pequeña. Solo 14 días de seguimiento.
- **Hallazgos contrarios o no significativos:** Sin impacto clínicamente relevante.
- **Conclusión que sí permite / que no permite:** Sí: Decir que en esta cohorte la anquiloglosia al nacer no redujo la autoeficacia materna a los 14 días. No: Concluir sobre efectos a largo plazo.
- **Licencia y derechos:** Acceso abierto en PMC. Licencia PENDIENTE DE VERIFICAR.
- **Estado de lectura:** Resumen PubMed y texto completo revisados el 17/10/2026.

## Figuras

Licencia del artículo: CC BY-NC-ND 4.0 (no permite copiar aquí). Figuras en PubMed Central (PMC11730490).

- **Figura 1.** Diagrama de participantes de la cohorte. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11730490/figure/Fig1/).

---

<!-- archivo: fuentes/articulos/2025-gandevivala-zplastia-habla.md -->
# Estudio: Comparative Evaluation of Z-Plasty and Linear Closure in Ankyloglossia Patients: A Randomized Study of Effects on Speech Articulation and Airway Volume

- **ID:** GANDEVIVALA2025
- **Autores, año y revista:** Gandevivala A; Saptarshi VR; Natarajan S; Patkar ND; Prasad P; Ahuja SA. J Oral Maxillofac Surg 2025;83(12):1540-1548.
- **DOI / PMID / URL:** DOI `10.1016/j.joms.2025.08.017`; PMID `40983110`.
- **Tipo de estudio:** Estudio aleatorizado.
- **Población y tamaño muestral:** 30 niños (15 por grupo) de unos 6-7 años con anquiloglosia y defectos de articulación.
- **Definición diagnóstica y técnicas:** Frenuloplastia con cierre en Z frente a cierre lineal.
- **Criterio diagnóstico de anquiloglosia:** LONGITUD/ASPECTO: Kotlow grados III/IV.
- **Variables de resultado:** Articulación (porcentaje de vocales y consonantes correctas), inteligibilidad, volumen orofaríngeo por CBCT.
- **Resultados NUMÉRICOS verificados:** Mejor articulación con Z (cambio 26,47 frente a 17,26; P<0,001) e inteligibilidad (2,06 frente a 1,2; P<0,001). Volumen orofaríngeo: +12,11 % frente a +10,43 % (P=0,026).
- **Límites metodológicos / confusores:** Sin grupo sin cirugía; muestra pequeña; volumen de vía aérea en CBCT sensible a la postura (ver O-003).
- **Hallazgos contrarios o no significativos:** No aplica.
- **Conclusión que sí permite / que no permite:** Sí: Decir que, entre dos técnicas, el cierre en Z dio mejor articulación en este estudio. No: Decir que la frenuloplastia mejora el habla frente a no operar.
- **Licencia y derechos:** Derechos del editor. Aquí solo resumen propio.
- **Estado de lectura:** Resumen de PubMed revisado el 02/11/2026. Búsqueda de actualización del 02/11/2026.

## Figuras

Figuras no revisadas.

---

<!-- archivo: fuentes/articulos/2025-gismonti-prevalencia-dificultad-lactancia.md -->
# Estudio: Prevalence of ankyloglossia among infants with breastfeeding difficulties: a systematic review

- **ID:** GISMONTI2025
- **Autores, año y revista:** Gismonti-Gaudêncio L; Póvoa-Santos L; Alvarenga-Brant R; De Luca Canto G; Abreu LG; Lai H; Ge L; Martins-Pfeifer CC. Midwifery 2025;149:104564.
- **DOI / PMID / URL:** DOI `10.1016/j.midw.2025.104564`; PMID `40818366`; PROSPERO CRD42023394743.
- **Tipo de estudio:** Revisión sistemática y metaanálisis de proporciones.
- **Población y tamaño muestral:** 12 estudios (10 transversales, 2 cohortes), 8.538 lactantes hasta 24 meses.
- **Definición diagnóstica y técnicas:** Ocho bases de datos hasta el 14/01/2025.
- **Criterio diagnóstico de anquiloglosia:** MIXTO: aceptó cualquier herramienta para la anquiloglosia y para la dificultad de lactancia.
- **Variables de resultado:** Proporción de anquiloglosia entre lactantes con dificultades de lactancia.
- **Resultados NUMÉRICOS verificados:** Anquiloglosia en el 34 % (IC 95 % 12-61 %) de los lactantes con dificultades. Variaba del 9 % al 74 % según la herramienta de lactancia. Dificultades de lactancia: 30 % (IC 95 % 19-43 %).
- **Límites metodológicos / confusores:** Intervalos muy amplios.
- **Hallazgos contrarios o no significativos:** No aplica.
- **Conclusión que sí permite / que no permite:** Sí: Decir que unos 7 de cada 10 lactantes con dificultades no tienen anquiloglosia, según esta revisión, y que la cifra depende de la herramienta. No: Usarla como prevalencia en población general.
- **Licencia y derechos:** Derechos del editor. Aquí solo resumen propio.
- **Estado de lectura:** Resumen de PubMed revisado el 02/11/2026. Búsqueda de actualización del 02/11/2026.

## Figuras

Figuras no revisadas.

---

<!-- archivo: fuentes/articulos/2025-guoth-gumberger-anatomia-frenillo.md -->
# Estudio: Implications of Tongue and Lingual Frenulum Anatomy for Tongue-Tie Evaluation and Management

- **ID:** GUOTHGUMBERGER2025
- **Autores, año y revista:** Guóth-Gumberger M; Karall D. Acta Paediatr 2025;114(5):1069-1071.
- **DOI / PMID / URL:** DOI `10.1111/apa.17600`; PMID `39840728`; https://pmc.ncbi.nlm.nih.gov/articles/PMC11976108/
- **Tipo de estudio:** Comunicación breve basada en 16 años de fotos y frenotomías con tijera de las autoras.
- **Población y tamaño muestral:** No aplica.
- **Definición diagnóstica y técnicas:** Frenotomía con tijera en rombo.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA como estudio. Describe tres tipos de frenillo según contenido: mucosa sola, mucosa y fascia, y con fibras de geniogloso.
- **Variables de resultado:** No aplica.
- **Resultados NUMÉRICOS verificados:** Sin cifras. Ideas: no ver frenillo con la lengua relajada no basta para saber si se mueve bien; tras la frenotomía el pliegue sigue viéndose más atrás; ninguna técnica garantiza liberación completa.
- **Límites metodológicos / confusores:** Opinión basada en experiencia.
- **Hallazgos contrarios o no significativos:** No aplica.
- **Conclusión que sí permite / que no permite:** Sí: Apoyar que la exploración tiene que ser con la lengua elevada. No: Usarla como evidencia cuantitativa.
- **Licencia y derechos:** Acceso abierto CC BY-NC (según el PDF).
- **Estado de lectura:** Resumen PubMed y texto completo revisados el 17/10/2026.

## Figuras

Licencia del artículo: CC BY-NC 4.0 (no permite copiar aquí). Figuras en PubMed Central (PMC11976108).

- **Figura 1.** Lengua relajada sin frenillo visible y elevada con frenillo; tres tipos de frenillo según contenido; cicatrización tras frenotomía con tijera. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11976108/figure/apa17600-fig-0001/).

---

<!-- archivo: fuentes/articulos/2025-ho-estetica-cirugia-ortognatica.md -->
# Estudio: Comparison of aesthetic outcomes of maxilla-only, mandible-only, and bimaxillary orthognathic surgeries: A retrospective analysis

- **ID:** HO2025
- **Autores, año y revista:** Ho CT; Huang TH; Deo D et al.. J Dent Sci 2025;20(2):1118-1128.
- **DOI / PMID / URL:** DOI `10.1016/j.jds.2025.01.006`; PMID `40224096`; https://pmc.ncbi.nlm.nih.gov/articles/PMC11993053/
- **Tipo de estudio:** Retrospectivo.
- **Población y tamaño muestral:** 60 pacientes taiwaneses, 20 por tipo de cirugía.
- **Definición diagnóstica y técnicas:** Seis análisis cefalométricos antes y después.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA: el estudio no diagnostica anquiloglosia.
- **Variables de resultado:** Ángulos, proporciones y estética de tejidos blandos.
- **Resultados NUMÉRICOS verificados:** Maxilar sola: mejora del ángulo nasolabial. Mandíbula sola: cambios en ángulo H y SN-MP. Bimaxilar: mejoras más completas, incluida la altura facial inferior.
- **Límites metodológicos / confusores:** Retrospectivo, sin valoración de la función.
- **Hallazgos contrarios o no significativos:** Disminución de la prominencia nasal en todos.
- **Conclusión que sí permite / que no permite:** Sí: Citar cómo cambia la estética según el tipo de cirugía. No: Extraer conclusiones funcionales.
- **Licencia y derechos:** Acceso abierto en PMC. Licencia PENDIENTE DE VERIFICAR.
- **Estado de lectura:** Resumen PubMed y texto completo revisados el 17/10/2026.

## Figuras

Licencia del artículo: CC BY-NC-ND 4.0 (no permite copiar aquí). Figuras en PubMed Central (PMC11993053).

- **Figura 1.** Puntos cefalométricos usados. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11993053/figure/fig1/).
- **Figura 2.** Medidas de estética facial según los distintos análisis. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11993053/figure/fig2/).

---

<!-- archivo: fuentes/articulos/2025-hussein-envejecimiento-mandibula.md -->
# Estudio: How Does the Mandible Age? Comprehensive Artificial Intelligence-Assisted Shape Analysis in the White Population

- **ID:** HUSSEIN2025
- **Autores, año y revista:** Hussein SM; Rames JD; Shehab AA et al.. Plast Reconstr Surg Glob Open 2025;13(4):e6650.
- **DOI / PMID / URL:** DOI `10.1097/GOX.0000000000006650`; PMID `40264908`; https://pmc.ncbi.nlm.nih.gov/articles/PMC12011572/
- **Tipo de estudio:** Transversal retrospectivo con TC.
- **Población y tamaño muestral:** 280 mandíbulas de personas blancas de 20 a 79 años.
- **Definición diagnóstica y técnicas:** Segmentación 3D asistida por IA y modelado estadístico de forma.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA: el estudio no diagnostica anquiloglosia.
- **Variables de resultado:** Volumen y medidas lineales.
- **Resultados NUMÉRICOS verificados:** Altura de la rama baja unos 5,3 mm en mujeres y 4,2 mm en hombres. Anchuras posteriores aumentan 4-5 mm.
- **Límites metodológicos / confusores:** Transversal; una sola población.
- **Hallazgos contrarios o no significativos:** No aplica.
- **Conclusión que sí permite / que no permite:** Sí: Citar cambios de la mandíbula con la edad independientes de la pérdida dental. No: Inferir cambios individuales.
- **Licencia y derechos:** Acceso abierto en PMC. Licencia PENDIENTE DE VERIFICAR.
- **Estado de lectura:** Resumen PubMed y texto completo revisados el 17/10/2026.

## Figuras

Licencia del artículo: CC BY-NC-ND 4.0 (no permite copiar aquí). Figuras en PubMed Central (PMC12011572).

- **Figura 1.** Puntos y medidas mandibulares en la malla 3D. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12011572/figure/F1/).
- **Figura 2.** Superposición y mapa de calor por grupos de edad, mujeres. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12011572/figure/F2/).
- **Figura 3.** Jóvenes frente a mayores, mujeres. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12011572/figure/F3/).
- **Figura 4.** Superposición y mapa de calor por grupos de edad, hombres. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12011572/figure/F4/).
- **Figura 5.** Jóvenes frente a mayores, hombres. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12011572/figure/F5/).
- **Figura 6.** Diferencias de envejecimiento entre sexos. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12011572/figure/F6/).

---

<!-- archivo: fuentes/articulos/2025-kalra-laser-frenillos-caso.md -->
# Estudio: Untying the Knot: Frenectomy of Lip and Tongue Ties Using Diode Lasers

- **ID:** KALRA2025
- **Autores, año y revista:** Kalra G; Srivastava M; Nangia T; Chawla T. Cureus 2025;17(1):e76876.
- **DOI / PMID / URL:** DOI `10.7759/cureus.76876`; PMID `39902023`; https://pmc.ncbi.nlm.nih.gov/articles/PMC11788089/
- **Tipo de estudio:** Casos clínicos.
- **Población y tamaño muestral:** Niños con frenillo labial grado II y anquiloglosia clase II.
- **Definición diagnóstica y técnicas:** Láser de diodo.
- **Criterio diagnóstico de anquiloglosia:** LONGITUD/ASPECTO («clase II»); escala PENDIENTE DE VERIFICAR.
- **Variables de resultado:** No aplica.
- **Resultados NUMÉRICOS verificados:** Sin cifras.
- **Límites metodológicos / confusores:** Casos.
- **Hallazgos contrarios o no significativos:** No aplica.
- **Conclusión que sí permite / que no permite:** Sí: Ilustrar la técnica. No: Concluir eficacia.
- **Licencia y derechos:** Acceso abierto en PMC. Licencia PENDIENTE DE VERIFICAR.
- **Estado de lectura:** Resumen PubMed y texto completo revisados el 17/10/2026.

## Figuras

Licencia del artículo: CC BY 4.0. Figuras en PubMed Central (PMC11788089).

- **Figura 1.** Inserción alta del frenillo labial y diastema de unos 3 mm. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11788089/figure/FIG1/).
- **Figura 2.** Clasificación de Kotlow del frenillo labial. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11788089/figure/FIG2/).
- **Figura 3.** Incisión en rombo con láser. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11788089/figure/FIG3/).
- **Figura 4.** Control a la semana y a los 3 meses (diastema de 1 mm). [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11788089/figure/FIG4/).
- **Figura 5.** Lengua con inserción restrictiva, vistas frontal y lateral. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11788089/figure/FIG5/).
- **Figura 6.** Clasificación de Coryllos. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11788089/figure/FIG6/).
- **Figura 7.** Controles postoperatorios. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11788089/figure/FIG7/).

Fotos de pacientes y clasificaciones reproducidas de terceros: solo enlace.

---

<!-- archivo: fuentes/articulos/2025-kim-craneofacial-trs-ninos.md -->
# Estudio: Craniofacial anatomical determinants of pediatric sleep-disordered breathing: A comprehensive review

- **ID:** KIM2025
- **Autores, año y revista:** Kim KA; Kim SJ; Yoon A. J Prosthodont 2025;34(S1):26-34.
- **DOI / PMID / URL:** DOI `10.1111/jopr.13984`; PMID `39557815`; https://pmc.ncbi.nlm.nih.gov/articles/PMC12000634/
- **Tipo de estudio:** Revisión narrativa.
- **Población y tamaño muestral:** 40 artículos (2006-2024).
- **Definición diagnóstica y técnicas:** PubMed y Google Scholar.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA. Cita el frenillo corto como factor de riesgo junto a la lengua baja.
- **Variables de resultado:** No aplica.
- **Resultados NUMÉRICOS verificados:** Sin cifras propias. Fenotipo típico: crecimiento vertical, maxilar estrecho, mandíbula retrasada, rotación posterior (clase II hiperdivergente). La clase III con maxilar pequeño tendría menos riesgo.
- **Límites metodológicos / confusores:** Revisión narrativa de autores del entorno de Zaghi.
- **Hallazgos contrarios o no significativos:** No aplica.
- **Conclusión que sí permite / que no permite:** Sí: Citar el fenotipo craneofacial asociado al trastorno respiratorio del sueño infantil. No: Usarla como prueba causal.
- **Licencia y derechos:** Acceso abierto en PMC. Licencia PENDIENTE DE VERIFICAR.
- **Estado de lectura:** Resumen PubMed y texto completo revisados el 17/10/2026.

## Figuras

Licencia del artículo: CC BY-NC-ND 4.0 (no permite copiar aquí). Figuras en PubMed Central (PMC12000634).

- **Figura 1.** Factores fisiopatológicos de la apnea infantil. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12000634/figure/jopr13984-fig-0001/).
- **Figura 2.** Cómo influye el trastorno respiratorio del sueño en el crecimiento orofacial. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12000634/figure/jopr13984-fig-0002/).

---

<!-- archivo: fuentes/articulos/2025-kumar-herramientas-cuantitativas.md -->
# Estudio: Feasibility and use of quantitative tools for the diagnosis of Ankyloglossia: A systematic review

- **ID:** KUMAR2025
- **Autores, año y revista:** Kumar K; Balaji S; Haridoss S; Vignesh KC; Swaminathan K. Int J Pediatr Otorhinolaryngol 2025;198:112568.
- **DOI / PMID / URL:** DOI `10.1016/j.ijporl.2025.112568`; PMID `40974663`.
- **Tipo de estudio:** Revisión sistemática.
- **Población y tamaño muestral:** 17 estudios (11 transversales, 4 cohortes, 2 ensayos).
- **Definición diagnóstica y técnicas:** Búsqueda en **9 bases** hasta marzo de 2025; **3.788 registros**, 1.664 cribados tras deduplicar, 46 textos completos analizados y **17 estudios incluidos** (11 transversales, 4 cohortes, 2 ensayos); restricción a inglés y análisis con Rayyan.
- **Criterio diagnóstico de anquiloglosia:** MIXTO. Unos instrumentos miden la longitud del frenillo y otros parámetros funcionales.
- **Variables de resultado:** Herramientas cuantitativas de medida del frenillo.
- **Resultados NUMÉRICOS verificados:** **17/46** artículos evaluados a texto completo incluidos; **ninguna herramienta cuantitativa pudo recomendarse** de manera concluyente, al mezclar mediciones lineales del frenillo con parámetros de función y reportes heterogéneos. El resumen **no ofrece** un umbral validado de movilidad ni sensibilidad/especificidad aplicable a todos los grupos etarios.
- **Límites metodológicos / confusores:** Solo artículos en inglés; estudios de edades y métodos heterogéneos; certeza de evidencia baja, sin referencia diagnóstica única para comparar dispositivos. **No invalida de manera absoluta los instrumentos individuales**: impide recomendar un umbral universal sobre la evidencia sintetizada.
- **Hallazgos contrarios o no significativos:** Necus 2025 halló más datos psicométricos publicados para LFPI en lactantes (no patrón de referencia); Dhar 2026 destaca discriminación de BTAT/TABBY con certeza muy baja. Las diferencias son explicables en parte por **preguntas y poblaciones distintas**, no por elegir ganadores.
- **Conclusión que sí permite / que no permite:** Sí: Decir que no hay una medida cuantitativa recomendada para diagnosticar anquiloglosia. No: Elegir una herramienta a partir de ella.
- **Licencia y derechos:** Derechos del editor. Aquí solo resumen propio.
- **Estado de lectura:** Resumen PubMed ampliado revisado el **03/11/2026**; texto completo editorial **NO inspeccionado**. No atribuir a la publicación análisis que no aparezcan en el resumen.

## Figuras

Figuras no revisadas.

## Actualización crítica de 03/11/2026

**Implicación editorial (03/11/2026):** «no se puede recomendar una herramienta cuantitativa universal» es una conclusión sobre la **certeza y heterogeneidad de estudios** y no prueba que la limitación funcional de la lengua sea irrelevante. Tampoco legitima afirmar que un TRMR aislado sea diagnóstico válido para cualquier función.

---

<!-- archivo: fuentes/articulos/2025-kummer-carta-cordray.md -->
# Estudio: Incorrect Statements and Citing Errors Regarding the Effect of Ankyloglossia on Speech in Cordray et al., 2023

- **ID:** KUMMER2025
- **Autores, año y revista:** Kummer AW. Am J Speech Lang Pathol 2025;34(2):982-984 (online febrero de 2025).
- **DOI / PMID / URL:** DOI `10.1044/2024_AJSLP-24-00231`; PMID `39913277`
- **Tipo de estudio:** Carta al director.
- **Población y tamaño muestral:** No aplica.
- **Definición diagnóstica y técnicas:** No aplica.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA (carta). Su argumento: aunque la punta esté muy restringida, se puede compensar y producir los fonemas linguales con el mismo resultado acústico.
- **Variables de resultado:** No aplica.
- **Resultados NUMÉRICOS verificados:** Sin cifras. Señala que Cordray 2023 omitió la revisión de la AHRQ (evidencia insuficiente sobre habla) y el consenso de la AAO-HNS (la anquiloglosia no suele afectar al habla).
- **Límites metodológicos / confusores:** Opinión. Hay respuesta de los autores: Cordray et al. 2025, PMID 39913269, doi 10.1044/2024_AJSLP-24-00413.
- **Hallazgos contrarios o no significativos:** Ver CORDRAY2023.
- **Conclusión que sí permite / que no permite:** Sí: Citar la crítica más directa a Cordray 2023 sobre habla. No: Usarla como prueba empírica.
- **Licencia y derechos:** Derechos del editor. Aquí solo metadatos y resumen propio.
- **Estado de lectura:** Resumen PubMed revisado el 17/10/2026. En notas de trabajo previas figura como «réplica de 2024»: el DOI es de 2024 pero se publicó en 2025.

## Figuras

Figuras no revisadas: el texto completo no está en acceso abierto en PMC. [Ver el artículo](https://doi.org/10.1044/2024_AJSLP-24-00231).

---

<!-- archivo: fuentes/articulos/2025-necus-herramientas-diagnostico.md -->
# Estudio: Assessment of tongue structure and function in infants for the diagnosis of ankyloglossia: A systematic review

- **ID:** NECUS2025
- **Autores, año y revista:** Necus E; Claessen M; Hennessey N; Smart S. Int J Pediatr Otorhinolaryngol 2025;196:112485 (corrección en 2025;197:112527).
- **DOI / PMID / URL:** DOI `10.1016/j.ijporl.2025.112485`; PMID `40729922`.
- **Tipo de estudio:** Revisión sistemática.
- **Población y tamaño muestral:** 117 estudios en lactantes de 0 a 12 meses; 9 herramientas.
- **Definición diagnóstica y técnicas:** CINAHL, ProQuest, Web of Science, Medline y Maternal and Infant Care.
- **Criterio diagnóstico de anquiloglosia:** MIXTO: compara herramientas. Concluye que hace falta valorar estructura y función, incluido el impacto en la alimentación. La herramienta con más fiabilidad y validez descritas fue el Lingual Frenulum Protocol for Infants (LFPI, Martinelli).
- **Variables de resultado:** Propiedades psicométricas de las herramientas.
- **Resultados NUMÉRICOS verificados:** Nueve herramientas con parámetros distintos de aspecto y función y con datos de fiabilidad y validez poco consistentes. Pocos estudios usaban la alimentación como criterio diagnóstico.
- **Límites metodológicos / confusores:** **117 estudios** sobre lactantes de 0–12 meses, pero las propiedades psicométricas se notifican de forma desigual entre las **9 herramientas**. Una herramienta con **más publicaciones de fiabilidad y validez** no equivale a patrón de referencia aceptado: la revisión no demuestra capacidad de predecir quién se beneficiará de cirugía. No confundir validez convergente/consistencia con sensibilidad/especificidad clínica ante un patrón diagnóstico independiente.
- **Hallazgos contrarios o no significativos:** La revisión Kumar 2025 no pudo recomendar ninguna herramienta cuantitativa concreta por heterogeneidad y certeza baja. No es una refutación directa de Necus: examina otros criterios de medición y otras edades/diseños. La revisión Dhar 2026 identifica más evidencia comparativa para BTAT/TABBY, pero con certeza global **muy baja**.
- **Conclusión que sí permite / que no permite:** Sí: Decir que las herramientas para lactantes son heterogéneas y que esta revisión prefiere el LFPI. No: Presentar el LFPI como patrón de referencia validado.
- **Licencia y derechos:** Derechos del editor. Aquí solo resumen propio.
- **Estado de lectura:** Resumen PubMed y página editorial de acceso abierto revisados el **03/11/2026**. **No se ha auditado en detalle el texto íntegro ni las 117 publicaciones primarias.** La revisión tiene una **corrección publicada**: DOI `10.1016/j.ijporl.2025.112527`, PMID `40841244`; **el contenido exacto de la fe de erratas está PENDIENTE DE VERIFICAR**. Conflictos declarados: Smart participa en ICAP y ASTOT; considerar en interpretación de recomendaciones, no usarlos para descartar datos.

## Figuras

Figuras no revisadas.

## Actualización crítica de 03/11/2026

**Nota de lectura crítica (03/11/2026):** LFPI resultó ser el instrumento con **más información psicométrica publicada** según esta revisión; no se ha probado con ello que sea el mejor predictor causal de problemas de alimentación o respuesta quirúrgica. La comparación con la AAP (2024, que afirmaba que no había herramientas ampliamente validadas) requiere diferenciar fecha y criterios de «validez». Informe AAP.

---

<!-- archivo: fuentes/articulos/2025-nzcom-matronas-consenso.md -->
# Estudio: Consensus statement: Tongue-tie (Ankyloglossia) (New Zealand College of Midwives)

- **ID:** NZCOM2025
- **Autores, año y revista:** New Zealand College of Midwives / Te Kāreti o ngā Kaiwhakawhānau ki Aotearoa. Subido el 16/10/2025; aprobado y pendiente de ratificar en la asamblea del Colegio de 2026. Sustituye al de 2017. Revisión prevista en 2030.
- **DOI / PMID / URL:** Sin DOI ni PMID. https://www.midwife.org.nz/wp-content/uploads/2025/10/Consensus-statement-Tongue-tie-Ankyloglossia-with-watermark.pdf
- **Tipo de estudio:** Declaración de consenso de un colegio profesional de matronas. No describe método de búsqueda ni de consenso.
- **Población y tamaño muestral:** Recién nacidos amamantados.
- **Definición diagnóstica y técnicas:** Define la anquiloglosia como una condición congénita con un frenillo lingual corto o tenso que puede restringir los movimientos de la lengua. Incidencia citada: 4 a 11 % de los recién nacidos (O'Shea 2017).
- **Criterio diagnóstico de anquiloglosia:** MIXTO, con herramientas que combinan aspecto y función. Dice que la matrona puede identificar una anquiloglosia que causa problemas de alimentación durante una observación completa de la toma, con una herramienta como BTAT, TABBY o Hazelbaker. Citando a Mills 2019, dice que no se puede diagnosticar solo por el aspecto del frenillo.
- **Variables de resultado:** No aplica (declaración).
- **Resultados NUMÉRICOS verificados:** Sin cifras propias. Recomendaciones: el apoyo experto a la lactancia va primero y tiene prioridad sobre la cirugía; la frenotomía no siempre es necesaria aunque haya anquiloglosia; las matronas formadas pueden hacer una frenotomía lingual simple; los casos complejos se derivan a un especialista; vitamina K antes de una frenotomía electiva.
- **Límites metodológicos / confusores (solo los relevantes):** Solo trata la lactancia neonatal.
- **Otros resultados relevantes (si los hay):** Dice que «posterior tie», frenillo labial superior, frenillo bucal, frenillo labial inferior y los estiramientos tras el tratamiento tienen poca o ninguna evidencia que apoye su diagnóstico o tratamiento (cita a Mills 2019, la Asociación Dental de Nueva Zelanda 2018 y Shah 2020). Citando a Mills 2019, dice que el término «posterior tongue-tie» es anatómicamente incorrecto.
- **Aportación del estudio:** Es el documento de sociedad más reciente sobre anquiloglosia neonatal localizado (octubre de 2025).
- **Licencia y derechos:** Documento del New Zealand College of Midwives. Aquí solo resumen propio.
- **Estado de lectura:** Texto completo (PDF de 6 páginas) leído el 05/11/2026.

## Figuras

No tiene figuras.

---

<!-- archivo: fuentes/articulos/2025-papageorgiou-extracciones-via-aerea.md -->
# Estudio: Extraction of premolars in orthodontic treatment does not negatively affect upper airway volume and minimum cross-sectional area: a systematic review with meta-analysis

- **ID:** PAPAGEORGIOU2025
- **Autores, año y revista:** Papageorgiou SN; Zyli M; Papadopoulou AK. Eur J Orthod 2025;47(2):cjaf012.
- **DOI / PMID / URL:** DOI `10.1093/ejo/cjaf012`; PMID `40062590`; https://pmc.ncbi.nlm.nih.gov/articles/PMC11891658/
- **Tipo de estudio:** Revisión sistemática y metaanálisis. PROSPERO CRD42024621355.
- **Población y tamaño muestral:** 11 estudios retrospectivos no aleatorizados, 891 pacientes (edad media 20 años).
- **Definición diagnóstica y técnicas:** Ortodoncia con o sin extracción de premolares; vía aérea medida en CBCT.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA: el estudio no diagnostica anquiloglosia.
- **Variables de resultado:** Volumen y área transversal mínima de naso, palato, gloso y orofaringe.
- **Resultados NUMÉRICOS verificados:** Sin diferencias significativas en volumen ni en área mínima, salvo un área mínima orofaríngea mayor con extracciones (4 estudios; +23,00 mm²; IC 10,74-35,26). Fuerza de la evidencia moderada.
- **Límites metodológicos / confusores:** Estudios no aleatorizados con alto riesgo de sesgo. La postura de la cabeza no se controla: el texto completo solo la cita en la discusión como factor que influye en el CBCT.
- **Hallazgos contrarios o no significativos:** Ver COPPELSON2023 y O-003.
- **Conclusión que sí permite / que no permite:** Sí: Decir que, de media y medidas en CBCT, las extracciones apenas cambian la vía aérea. No: Decir que no cambian la función respiratoria ni la postura con que el paciente compensa.
- **Licencia y derechos:** Acceso abierto en PMC. Licencia PENDIENTE DE VERIFICAR.
- **Estado de lectura:** Resumen PubMed y fragmentos del texto completo (PMC) revisados el 17/10/2026.

## Figuras

Licencia del artículo: CC BY-NC-ND 4.0 (no permite copiar aquí). Figuras en PubMed Central (PMC11891658).

- **Figura 1.** Diagrama PRISMA. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11891658/figure/F1/).
- **Figura 2.** Metaanálisis de volumen de palato, oro y glosofaringe. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11891658/figure/F2/).
- **Figura 3.** Metaanálisis de área mínima de palato, oro y glosofaringe. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11891658/figure/F3/).

---

<!-- archivo: fuentes/articulos/2025-patel-frenotomia-reflujo.md -->
# Estudio: The Impact of Frenotomy on Gastroesophageal Reflux in Pediatric Ankyloglossia: A Systematic Review

- **ID:** PATEL2025
- **Autores, año y revista:** Patel A; Cirone K; Khoury S et al.. Ann Otol Rhinol Laryngol 2025;134(3):171-178.
- **DOI / PMID / URL:** DOI `10.1177/00034894241297584`; PMID `39529230`; https://pmc.ncbi.nlm.nih.gov/articles/PMC11806641/
- **Tipo de estudio:** Revisión sistemática sin metaanálisis.
- **Población y tamaño muestral:** 7 estudios (6 cohortes y 1 ensayo), 47 a 237 lactantes.
- **Definición diagnóstica y técnicas:** Escalas de padres GIGER, I-GERQ-R y GSQ-I.
- **Criterio diagnóstico de anquiloglosia:** LONGITUD/ASPECTO en su mayoría: clasificación de Coryllos (texto completo).
- **Variables de resultado:** Reflujo antes y después.
- **Resultados NUMÉRICOS verificados:** Ningún estudio usó pH ni impedancia. Las escalas de padres bajaron tras la frenotomía.
- **Límites metodológicos / confusores:** Sin controles; alto riesgo de sesgo.
- **Hallazgos contrarios o no significativos:** El reflujo mejora solo con el tiempo.
- **Conclusión que sí permite / que no permite:** Sí: Decir que no hay pruebas sólidas de que la frenotomía mejore el reflujo. No: Decir que está demostrado que no lo mejora.
- **Licencia y derechos:** Acceso abierto en PMC. Licencia PENDIENTE DE VERIFICAR.
- **Estado de lectura:** Resumen PubMed y texto completo revisados el 17/10/2026.

## Figuras

Licencia del artículo: CC BY-NC 4.0 (no permite copiar aquí). Figuras en PubMed Central (PMC11806641).

- **Figura 1.** Diagrama PRISMA. [Ver en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11806641/figure/fig1-00034894241297584/).

---

<!-- archivo: fuentes/articulos/2025-rodriguez-lara-experiencia-materna.md -->
# Estudio: Maternal Experiences and Challenges in Breastfeeding Infants with Tongue-Tie: A Systematic Review

- **ID:** RODRIGUEZLARA2025
- **Autores, año y revista:** Rodriguez Lara F; Carnino JM; Levi JR. Matern Child Health J 2025;29(7):870-878.
- **DOI / PMID / URL:** DOI `10.1007/s10995-025-04102-w`; PMID `40366606`
- **Tipo de estudio:** Revisión sistemática de estudios cualitativos y cuantitativos.
- **Población y tamaño muestral:** 8 estudios.
- **Definición diagnóstica y técnicas:** MEDLINE, Web of Science y EMBASE.
- **Criterio diagnóstico de anquiloglosia:** Variable entre estudios: PENDIENTE DE VERIFICAR.
- **Variables de resultado:** Síntomas físicos y psicológicos maternos.
- **Resultados NUMÉRICOS verificados:** Todos los estudios describen más dolor y sangrado del pezón, estrés y peor vínculo.
- **Límites metodológicos / confusores:** Pocos estudios, heterogéneos.
- **Hallazgos contrarios o no significativos:** No aplica.
- **Conclusión que sí permite / que no permite:** Sí: Decir que las madres de lactantes con anquiloglosia describen más complicaciones y estrés. No: Atribuir esos efectos solo al frenillo.
- **Licencia y derechos:** Derechos del editor. Aquí solo metadatos y resumen propio.
- **Estado de lectura:** Resumen PubMed y texto completo revisados el 17/10/2026.

## Figuras

Licencia: derechos del editor (no se copian imágenes). Leyendas leídas en el texto completo; puede haber más figuras que las listadas.

- **Figura 1.** Diagrama de la revisión sistemática. [Ver en el artículo](https://doi.org/10.1007/s10995-025-04102-w), figura 1.

---

<!-- archivo: fuentes/articulos/2025-thornton-publicaciones.md -->
# Estudio: Systematic Review of Tongue Tie Publications: Exponential Rise in Publications Without Exponential Increase in Evidence

- **ID:** THORNTON2025
- **Autores, año y revista:** Thornton AR; Montgomery EA; Graham ME; Riley CA; Lawlor CM. Otolaryngol Head Neck Surg 2025;173(2):324-331.
- **DOI / PMID / URL:** DOI `10.1002/ohn.1264`; PMID `40366002`.
- **Tipo de estudio:** Revisión sistemática de la literatura (tipo y calidad de los estudios).
- **Población y tamaño muestral:** 462 artículos de 2017 a 2024 sobre anquiloglosia en niños.
- **Definición diagnóstica y técnicas:** PubMed, Embase y Ovid MEDLINE.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA como estudio diagnóstico. Observa que ninguna de las clasificaciones descritas se centra principalmente en la función frente al aspecto.
- **Variables de resultado:** Número, tipo y calidad de los estudios.
- **Resultados NUMÉRICOS verificados:** Lo más frecuente fueron cohortes (179; 38,7 %); ensayos aleatorizados, 13 (2,8 %). Faltan resultados objetivos como duración de la lactancia o crecimiento.
- **Límites metodológicos / confusores:** Solo en inglés.
- **Hallazgos contrarios o no significativos:** No aplica.
- **Conclusión que sí permite / que no permite:** Sí: Decir que las publicaciones sobre frenillo crecen mucho sin que crezca la calidad de la evidencia. No: Juzgar la eficacia de ningún tratamiento.
- **Licencia y derechos:** Derechos del editor. Aquí solo resumen propio.
- **Estado de lectura:** Resumen de PubMed revisado el 02/11/2026. Búsqueda de actualización del 02/11/2026.

## Figuras

Figuras no revisadas.

---

<!-- archivo: fuentes/articulos/2025-ye-miofuncional-apnea-residual.md -->
# Estudio: The Therapeutic Role of Orofacial Myofunctional Therapy in Childhood Residual Obstructive Sleep Apnea

- **ID:** YE2025
- **Autores, año y revista:** Ye M; Huang S; Wang F; Li W; Tan G; Wang T. *Pediatr Pulmonol* 2025;60(2):e70993.
- **DOI / PMID / URL:** DOI `10.1002/ppul.70993`; PMID `39945575`. Registro ChiCTR2300072252 (07/06/2023).
- **Tipo de estudio:** Ensayo aleatorizado con grupo control sin tratamiento (tabla de números aleatorios), evaluadores de la polisomnografía y del OMES ciegos al grupo. Registro ChiCTR2300072252.
- **Población y tamaño muestral:** 47 niños de 6 a 8 años con apnea residual (IAH de 1 o más) 6 meses después de la adenoamigdalectomía: 24 asignados a terapia miofuncional y 23 al grupo sin tratamiento; se perdieron 3 y 7, quedando 21 y 16 en el análisis. Excluidos: alteraciones craneofaciales, enfermedad neuromuscular y síndromes como Down o Crouzon. Seguimiento a 1 y 3 meses.
- **Definición diagnóstica y técnicas:** Polisomnografía, apertura bucal durante el sueño, cuestionario OSA-18 modificado y evaluación miofuncional orofacial con puntuación (OMES).
- **Criterio diagnóstico de anquiloglosia:** NO APLICA: el estudio no valora la anquiloglosia. Búsqueda en el texto completo el 05/11/2026: no aparecen «ankyloglossia», «tongue-tie» ni «frenulum». Valora la movilidad lingual dentro del OMES, sin relacionarla con el frenillo.
- **Variables de resultado:** IAH, duración máxima de apneas e hipopneas, arquitectura del sueño, apertura bucal, OSA-18 y OMES.
- **Resultados NUMÉRICOS verificados:** IAH con terapia: 7,80 ± 8,68 al inicio, 4,25 ± 5,12 al mes y 3,77 ± 1,56 a los 3 meses (p = 0,046); sin terapia: 6,94 ± 9,64, 6,81 ± 7,93 y 7,11 ± 6,26 (p = 0,936); diferencia entre grupos p = 0,028. En apnea moderada a grave: de 13,05 ± 9,92 a 4,09 ± 1,40 con terapia (p = 0,0009) frente a 12,97 ± 14,17 a 11,52 ± 8,05 sin ella (entre grupos p = 0,014). Duración máxima de apneas e hipopneas: de 53,19 a 43,25 s con terapia (p = 0,007; entre grupos p = 0,041). Sueño profundo: de 105,7 a 138,5 min con terapia (p = 0,019), sin diferencia entre grupos (p = 0,923). Sin cambios significativos en la saturación media ni mínima.
- **Límites metodológicos / confusores (solo los relevantes):** Muestra pequeña, seguimiento de 3 meses y pérdidas desiguales (3 frente a 7). Varias mejoras son dentro del grupo tratado sin diferencia significativa frente al control.
- **Otros resultados relevantes (si los hay):** Programa con respiración nasal, ejercicios de posición de la lengua en el paladar («punto N»), labios y masticación, con sesiones diarias en casa.
- **Aportación del estudio:** Estudio de terapia miofuncional en niños con apnea residual tras la cirugía, con grupo sin tratamiento.
- **Licencia y derechos:** Copyright de Wiley (el pie genérico de Wiley sobre licencias Creative Commons no indica que este artículo la tenga). Aquí solo resumen propio.
- **Estado de lectura:** Texto completo (PDF) leído el 05/11/2026: métodos, aleatorización y tabla 5.

## Figuras

Figuras no revisadas. [Ver el artículo](https://doi.org/10.1002/ppul.70993).

---

<!-- archivo: fuentes/articulos/2025-zhao-hipertrofia-adenoamigdalar-morfologia.md -->
# Estudio: Is adenotonsillar hypertrophy associated with dentofacial morphology? A systematic review and meta-analyses

- **ID:** ZHAO2025ATH
- **Autores, año y revista:** Zhao T; Wang M; Ngan P; Tao Z; Yu X; Hua F; He H. *American Journal of Orthodontics and Dentofacial Orthopedics 168(5) (2025):524–541.e29*.
- **DOI / PMID / URL:** DOI `10.1016/j.ajodo.2025.04.024`; PMID `40699159`; [original](https://doi.org/10.1016/j.ajodo.2025.04.024).
- **Tipo de estudio:** Revisión sistemática y metaanálisis de estudios transversales.
- **Población y tamaño muestral:** 36 estudios comparando niños con/sin hipertrofia adenoidea y/o amigdalar.
- **Definición diagnóstica y técnicas:** Búsqueda de cuatro bases de datos hasta 01/11/2024; metaanálisis de efectos aleatorios; diagnóstico de hipertrofia/obstrucción con procedimientos variables entre estudios; calidad valorada con escala Newcastle–Ottawa adaptada a transversales.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA: este estudio no diagnostica anquiloglosia ni utiliza escalas de frenillo.
- **Variables de resultado:** Medidas cefalométricas (SN-MP, ArGoMe, SNA, SNB, ANB), anchuras de arcada y tipos de maloclusión.
- **Resultados NUMÉRICOS verificados:** SN-MP: diferencia media 2,20° (IC95% 1,47–2,92); ArGoMe 1,23° (0,68–1,79). SNA −0,30° (−0,53 a −0,06); SNB −0,78° (−1,33 a −0,24). ANB 0,31° (−0,35 a 0,61; p=0,59): **sin diferencia concluyente**.
- **Límites metodológicos / confusores:** Estudios transversales; múltiples exposiciones adenoides/amígdalas, posible confusión por edad, genética y respiración; se desconoce direccionalidad. **Certeza global baja o muy baja** según conclusión de los autores.
- **Hallazgos contrarios o no significativos:** ANB no mostró diferencia significativa y el tamaño medio de algunas diferencias angulares fue pequeño.
- **Conclusión que sí permite / que no permite:** Asociación entre hipertrofia adenoamigdalar y ciertos rasgos dentofaciales, especialmente componente vertical. No demuestra que el tejido linfoide cause retrognatia ni que extirparlo revierta crecimiento.
- **Licencia y derechos:** Derechos editoriales o de autores según el original; resumen crítico propio. No se incorporan PDF ni figuras ajenas.
- **Estado de lectura:** PubMed y resumen editorial verificados el 03/11/2026; texto completo pendiente.

## Figuras

No incorporadas ni evaluadas. [Original](https://doi.org/10.1016/j.ajodo.2025.04.024).

---

<!-- archivo: fuentes/articulos/2026-avivar-pardo-miofuncional-apnea-pediatrica.md -->
# Estudio: Effectiveness of myofunctional therapy on polysomnographic and functional outcomes in paediatric obstructive sleep apnea: a systematic review

- **ID:** AVIVARPARDO2026
- **Autores, año y revista:** Avivar-Pardo R; Montiel-Company JM; Camañes-Gonzalvo S; Casaña-Ruiz MD; Paredes-Gallardo V; Bellot-Arcís C. *Sleep and Biological Rhythms*, publicado 10/09/2026.
- **DOI / PMID / URL:** DOI `10.1007/s41105-026-00682-4`; [texto abierto Springer](https://link.springer.com/article/10.1007/s41105-026-00682-4); PROSPERO `CRD420251250167`.
- **Tipo de estudio:** Revisión sistemática de eficacia de terapia miofuncional (MFT) sobre apnea obstructiva del sueño infantil, con síntesis cualitativa de cuatro estudios y clasificación GRADE **baja**.
- **Población y tamaño muestral:** Cuatro estudios pediátricos, edades medias cercanas a 7,9 años: **un ensayo aleatorizado (n=27), dos observacionales prospectivos (n=210 en conjunto) y uno retrospectivo (n=7)**. Las muestras individuales varían 7–133. No son cuatro ensayos independientes.
- **Definición diagnóstica y técnicas:** Niños con OSA diagnosticada por PSG. Búsqueda en PubMed, Embase, Scopus y Web of Science; **86 registros**, 27 duplicados, 59 cribados, 27 textos analizados, cuatro incluidos. Se registraron método diagnóstico, intervención, seguimiento y adherencia. Calidad NIH para observacionales, escala PEDro para ECA, GRADE.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA: revisa terapia de apnea infantil, no recluta por TRMR/Kotlow ni diagnostica frenillo restrictivo. La fuerza lingual (IOPI) y NOT-S fueron desenlaces funcionales en algunos estudios.
- **Variables de resultado:** IAH por PSG, saturación de oxígeno, fuerza/resistencia de lengua, desenlaces orofaciales y adherencia.
- **Resultados NUMÉRICOS verificados:** De **86 registros** quedaron **4 estudios** (1 ECA n=27, 3 observacionales n=217). Algunos estudios describen reducción de IAH y mejoría de saturación o fuerza lingual; la revisión alude a disminución relativa de IAH de hasta aproximadamente **58 % en un ensayo**, pero la muestra máxima total (n=133) **no corresponde al ECA**. No existe un efecto combinado verificado en esta ficha.
- **Límites metodológicos / confusores:** Solo un ensayo pequeño, tres estudios observacionales; intervenciones heterogéneas, adherencia variable, control insuficiente de confusores y algunos evaluadores no cegados. El ECA obtiene 6/11 en PEDro. La mejoría antes/después no equivale a diferencia entre grupos ni permite atribuir el efecto causal a MFT.
- **Hallazgos contrarios o no significativos:** Con GRADE **baja**, la revisión no confirma eficacia clínica. **Cnockaert 2026**, que agrupó cuatro ECA (n=174) de intervenciones activas aisladas, obtuvo diferencia media IAH −1,68/h (IC95 % −3,61 a +0,24), sin diferencia estadísticamente concluyente. Las síntesis no deben tratarse como ensayos opuestos ni sus poblaciones necesariamente como idénticas.
- **Conclusión que sí permite / que no permite:** Puede existir mejoría en determinados desenlaces tras MFT, pero la evidencia **no establece su efectividad clínica de forma definitiva** ni justifica su uso aislado universal como primera línea. No evalúa cirugía del frenillo ni crecimiento óseo.
- **Licencia y derechos:** Publicación de **acceso abierto Springer**; no se reproducen tablas ni figuras y la licencia concreta de reutilización requiere verificación.
- **Estado de lectura:** Resumen, descripción del cribado, calidad de los cuatro estudios y resultados cualitativos consultados en la página abierta de Springer el **03/11/2026**. No se ha extraído individualmente toda la tabla 1 ni realizado evaluación nueva del riesgo de sesgo.

## Figuras

No reproducidas. [Fuente original](https://doi.org/10.1007/s41105-026-00682-4).

---

<!-- archivo: fuentes/articulos/2026-caixeta-abopi-brasil.md -->
# Estudio: Brazilian Academy of Paediatric Otorhinolaryngology Task Force: lingual frenulum disorders in childhood, evidence-based recommendations

- **ID:** CAIXETA2026
- **Autores, año y revista:** Caixeta JAS; Pazinatto DB; Padoin RCPK; Lubianca Neto JF; Avelino MAG; Chen VG et al. Braz J Otorhinolaryngol 2026;92(2):101762.
- **DOI / PMID / URL:** DOI `10.1016/j.bjorl.2026.101762`; PMID `41548508`; PMC12854977.
- **Tipo de estudio:** Recomendaciones basadas en la evidencia de la Academia Brasileña de Otorrinolaringología Pediátrica. Graduación del American College of Physicians.
- **Población y tamaño muestral:** Niños.
- **Definición diagnóstica y técnicas:** Búsqueda y valoración crítica de artículos en inglés y portugués.
- **Criterio diagnóstico de anquiloglosia:** NO PROPONE NINGUNO. Dice que hay varios métodos descritos para evaluar el frenillo y que la mayoría no tienen validación interna ni externa.
- **Variables de resultado:** Disfagia, alteraciones orofaciales, maloclusión, apnea, reflujo, habla, dolor materno.
- **Resultados NUMÉRICOS verificados:** No hay datos que apoyen relación entre frenillo alterado y disfagia, alteraciones orofaciales, maloclusión, limitaciones sociales, apnea obstructiva o reflujo. No causa retraso del habla, aunque estudios de muy baja evidencia sugieren que puede dificultar algunos fonemas. La frenotomía puede reducir el dolor materno en la lactancia. Ninguna técnica quirúrgica ha demostrado ser superior.
- **Límites metodológicos / confusores:** Solo artículos en inglés o portugués.
- **Hallazgos contrarios o no significativos:** No aplica.
- **Conclusión que sí permite / que no permite:** Sí: Decir que la otorrinolaringología pediátrica brasileña no encuentra criterios validados ni datos de relación con maloclusión o apnea. No: Leer «no hay datos» como «demostrado que no existe relación» (AGENTS.md, regla 4).
- **Licencia y derechos:** Copyright de la Associação Brasileira de Otorrinolaringologia; texto en PMC. Aquí solo resumen propio.
- **Estado de lectura:** Resumen de PubMed revisado el 02/11/2026. Búsqueda de actualización del 02/11/2026.

## Figuras

Figuras no revisadas. [Ver el documento](https://pmc.ncbi.nlm.nih.gov/articles/PMC12854977/).

---

<!-- archivo: fuentes/articulos/2026-carey-miofuncional-deglucion-infantil.md -->
# Estudio: Orofacial Myofunctional Therapy for Feeding and Swallowing in Children From Four to 12 Years: What Does the Evidence Show? A Systematic Review

- **ID:** CAREY2026
- **Autores, año y revista:** Carey D; Merkel-Walsh R; Burrage P; Hadlow M; Alrehaily GHA; Tseng RJ; Smart S. *Journal of Oral Rehabilitation*, publicado online 08/09/2026.
- **DOI / PMID / URL:** DOI `10.1111/joor.70304`; PMID `42711116`; [texto completo abierto Wiley](https://onlinelibrary.wiley.com/doi/full/10.1111/joor.70304).
- **Tipo de estudio:** Revisión sistemática con **síntesis narrativa**, sin metaanálisis por heterogeneidad de desenlaces, instrumentos y protocolos.
- **Población y tamaño muestral:** **17 estudios**, **633 participantes**, de ellos **544 recibieron algún tipo de OMT**. Edad media de los estudios principalmente 4–12 años; dentro de algunas muestras hubo participantes hasta los 18 años. Tres ECA, 13 cuasiexperimentales y un estudio de caso.
- **Definición diagnóstica y técnicas:** Búsqueda en cuatro bases; 3.850 registros importados, 1.658 cribados, 136 textos completos evaluados y 17 incluidos. Evaluación crítica con listas JBI por diseño; herramientas y dosis de OMT variables. Para deglución se usaron siete estudios con medidas **solo subjetivas**, cuatro **solo objetivas**, seis **mixtas**.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA en conjunto: niños con problemas de alimentación/deglución de causas diversas; **algunos estudios incluyen frenectomía** como cointervención, pero la muestra de revisión no se define por anquiloglosia ni TRMR.
- **Variables de resultado:** Deglución funcional, patrón de empuje lingual, alimentación, control motor orofacial; **no PSG/AHI ni crecimiento esquelético** como objetivos de esta revisión.
- **Resultados NUMÉRICOS verificados:** Todos los **17** trabajos incluidos reportaron algún resultado favorable de alimentación/deglución. **10/17** fueron evaluados como calidad pobre (<50 %), uno aceptable, tres buena y tres alta según clasificación editorial. **11/17 (64,7 %)** combinaban OMT con aparatología, cirugía u otras terapias; solo **6** evaluaban OMT aislada. **10/17** aplicaron algún análisis estadístico, pero **ninguno informó tamaños de efecto**. No hay efecto combinado.
- **Límites metodológicos / confusores:** Muchos trabajos sin controles adecuados; los **3 ECA carecieron de auténtico brazo sin tratamiento**, utilizaron comparadores con dispositivos o intervenciones multimodales. Cointervenciones en mayoría, medidas poco estandarizadas y escaso seguimiento; riesgos de maduración espontánea, placebo, selección y expectativa. El hecho de que «los 17 estudios positivos» hayan sido los incluidos no demuestra eficacia comparativa, magnitud clínica ni ausencia de sesgo de publicación.
- **Hallazgos contrarios o no significativos:** Los autores reconocen que el predominio de evidencia no controlada **impide atribuir** las mejorías exclusivamente a OMT. La revisión de **Cnockaert 2026** aborda **otro resultado** (IAH objetivo de apnea) y no debe utilizarse como si contradijera directamente resultados de deglución.
- **Conclusión que sí permite / que no permite:** Los estudios observados describen mejorías de deglución tras OMT (frecuentemente combinada), con evidencia metodológicamente heterogénea e insuficiente para estimar un efecto causal independiente. No prueba prevención de maloclusión ni tratamiento de apnea por ejercicios.
- **Licencia y derechos:** Texto abierto Wiley; solo síntesis original y enlaces. Revisar licencia específica antes de reutilizar tablas.
- **Estado de lectura:** Texto completo HTML abierto (métodos, cribado, diseño, participantes, evaluación de calidad, discusión) consultado el **03/11/2026**; **no reanálisis individual de los 17 estudios**.
- **Conflictos de interés relevantes:** Los autores declaran vínculos profesionales con clínicas, servicios formativos de terapia orofacial y asociaciones del área; entre ellos Carey declara pertenencia a la junta ICAP y Merkel-Walsh actividad privada/formativa en terapia orofacial. Tratar estos vínculos como **posibles intereses a considerar**, no prueba de falsedad de los resultados.

## Figuras

No se reproducen. [Artículo original](https://doi.org/10.1111/joor.70304).

---

<!-- archivo: fuentes/articulos/2026-chandrasekharan-disfuncion-tubarica-otitis.md -->
# Estudio: Interventions for Obstructive Eustachian Tube Dysfunction: An Evidence-Based Umbrella Review of Efficacy and Safety

- **ID:** CHANDRASEKHARAN2026
- **Autores, año y revista:** Chandrasekharan DP; Badr-El-Dine M; James AL. *Otolaryngologic Clinics of North America (2026), publicación anticipada de mayo*.
- **DOI / PMID / URL:** DOI `10.1016/j.otc.2026.04.008`; PMID `42203563`; [original](https://doi.org/10.1016/j.otc.2026.04.008).
- **Tipo de estudio:** Umbrella review de revisiones sistemáticas.
- **Población y tamaño muestral:** Número de revisiones incluidas y participantes **PENDIENTE DE VERIFICAR** en texto completo.
- **Definición diagnóstica y técnicas:** Revisión de eficacia y seguridad de opciones de tratamiento para disfunción obstructiva de trompa de Eustaquio y otitis media con efusión.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA: este estudio no diagnostica anquiloglosia ni utiliza escalas de frenillo.
- **Variables de resultado:** Tratamiento médico, tubos de ventilación, adenoidectomía, dilatación de trompa, cirugía sinonasal; respuesta en otitis media con efusión.
- **Resultados NUMÉRICOS verificados:** El resumen no permite extraer efectos numéricos confiables ni tamaño de muestra combinado.
- **Límites metodológicos / confusores:** No investiga directamente movilidad lingual, desarrollo craneofacial o postura; las recomendaciones pueden ser específicas por edad y fenotipo de disfunción tubárica; evitar extrapolación a todas las otitis.
- **Hallazgos contrarios o no significativos:** La revisión destaca incertidumbre y calidad baja para varias técnicas, especialmente indicaciones y resultados a largo plazo de dilatación tubárica.
- **Conclusión que sí permite / que no permite:** Otitis media con efusión y disfunción tubárica son fenómenos ORL relevantes para el mapa; la adenoidectomía ofrece eficacia dependiente de edad para OME. No se puede afirmar una cadena causal desde frenillo lingual.
- **Licencia y derechos:** Derechos editoriales o de autores según el original; resumen crítico propio. No se incorporan PDF ni figuras ajenas.
- **Estado de lectura:** Resumen PubMed verificado el 03/11/2026; texto completo pendiente.

## Figuras

No incorporadas ni evaluadas. [Original](https://doi.org/10.1016/j.otc.2026.04.008).

---

<!-- archivo: fuentes/articulos/2026-cnockaert-miofuncional-apnea-infantil.md -->
# Estudio: Active strategies for children with obstructive sleep-disordered breathing: a systematic review and meta-analysis

- **ID:** CNOCKAERT2026
- **Autores, año y revista:** Cnockaert P; Da Purificaçao J; Poncin W. *Sleep Medicine 142 (2026):108840*.
- **DOI / PMID / URL:** DOI `10.1016/j.sleep.2026.108840`; PMID `41762858`; [original](https://doi.org/10.1016/j.sleep.2026.108840).
- **Tipo de estudio:** Revisión sistemática y metaanálisis de ensayos aleatorizados y estudios no aleatorizados; PROSPERO CRD42024614732.
- **Población y tamaño muestral:** **8 estudios (4 aleatorizados y 4 no aleatorizados)**; 7 evalúan terapia miofuncional y 1 ejercicio físico; para IAH se agrupan **4 ECA (n=174)**. Varios estudios seleccionaron niños con trastornos respiratorios del sueño persistentes tras cirugía. En el ensayo de tres brazos incluido, los autores **agruparon dos intervenciones activas** para el metaanálisis.
- **Definición diagnóstica y técnicas:** Búsquedas PubMed, Scopus, Embase y PEDro hasta 06/01/2026; intervención activa aislada, no tratamiento combinado o preventivo universal. Protocolos de terapia miofuncional y comparadores heterogéneos. RoB 2.0 y ROBINS-I v2, mayoritariamente riesgo de sesgo serio.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA: este estudio no diagnostica anquiloglosia ni utiliza escalas de frenillo.
- **Variables de resultado:** Índice de apnea-hipopnea (IAH), saturación media y mínima de oxígeno.
- **Resultados NUMÉRICOS verificados:** ECA de terapia miofuncional vs control: IAH diferencia media −1,68 eventos/h (IC95% −3,61 a 0,24; p=0,07; 4 estudios, n=174); saturación media 0,38 puntos (IC95% −6,67 a 7,43; n=108), sin diferencia concluyente. Estudios no aleatorizados: cambio en IAH −0,81 (−3,28 a 1,67; n=38).
- **Límites metodológicos / confusores:** Mayoría de estudios con riesgo serio de sesgo; protocolos de ejercicios y adherencia heterogéneos; muestras pequeñas; predominantemente apnea pediátrica residual tras cirugía, no todos los fenotipos. **En dos estudios no aleatorizados los resultados basales pertenecían a la cohorte total, pero el seguimiento se publicó desglosado por subgrupos; los revisores asumieron que los subgrupos eran comparables en el momento basal. Esta suposición es no verificable con los datos publicados y afecta especialmente el análisis antes/después.** Los IC permiten algunos beneficios y también efectos nulos; **p=0,07 no equivale a demostrar ausencia universal de beneficio**.
- **Hallazgos contrarios o no significativos:** No encontró diferencias significativas en IAH ni oxigenación con estrategias activas aisladas. **Es evidencia negativa pertinente**, no debe omitirse ni transformarse en eficacia demostrada.
- **Conclusión que sí permite / que no permite:** No apoya terapia miofuncional aislada como primera línea para SDB pediátrico con los ensayos disponibles. Tampoco permite excluir todos los efectos en subgrupos ni aplicaciones como tratamiento adyuvante.
- **Licencia y derechos:** Derechos editoriales o de autores según el original; resumen crítico propio. No se incorporan PDF ni figuras ajenas.
- **Estado de lectura:** Resumen PubMed, **introducción, métodos, resultados y limitaciones disponibles en HTML de la página del editor** contrastados el 03/11/2026; fuente [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S1389945726000791) y [versión de autor en UCLouvain](https://research.dial.uclouvain.be/entities/publication/354c10f1-2c8d-41f9-9280-a2cf978a3748). **No se ha inspeccionado íntegramente el PDF abierto ni todas las tablas y apéndices**, por lo que se mantiene revisión parcial, no «texto completo auditado».

## Figuras

No incorporadas ni evaluadas. [Original](https://doi.org/10.1016/j.sleep.2026.108840).

---

<!-- archivo: fuentes/articulos/2026-da-silva-umbrella-frenotomia.md -->
# Estudio: Lingual Frenotomy in Breastfeeding Infants: An Umbrella Review

- **ID:** DASILVA2026
- **Autores, año y revista:** da Silva BV; Barollo AV; Sá NDNL; Oliveira LB; Sanglard LF. Int J Paediatr Dent 2026;36(1):90-104.
- **DOI / PMID / URL:** DOI `10.1111/ipd.70031`; PMID `40990400`; PMC12783447.
- **Tipo de estudio:** Revisión de revisiones (umbrella) con AMSTAR 2.
- **Población y tamaño muestral:** 15 revisiones sistemáticas de ensayos en lactantes de hasta 1 año.
- **Definición diagnóstica y técnicas:** Siete bases de datos y literatura gris.
- **Criterio diagnóstico de anquiloglosia:** MIXTO entre las revisiones incluidas: `PENDIENTE DE VERIFICAR`.
- **Variables de resultado:** Autoeficacia de la lactancia, dolor del pezón, peso.
- **Resultados NUMÉRICOS verificados:** Confianza críticamente baja en 14 revisiones (93,3 %) y moderada en 1. La evidencia sobre lactancia sigue sin ser concluyente; la de beneficio sobre el dolor del pezón es débil.
- **Límites metodológicos / confusores:** Valora la calidad de las revisiones, no de los ensayos.
- **Hallazgos contrarios o no significativos:** No aplica.
- **Conclusión que sí permite / que no permite:** Sí: Decir que casi todas las revisiones sobre frenotomía en lactantes tienen calidad metodológica críticamente baja. No: Decir que la frenotomía no sirve.
- **Licencia y derechos:** CC BY (según PMC; `PENDIENTE DE VERIFICAR` versión). Aquí solo resumen propio.
- **Estado de lectura:** Resumen de PubMed revisado el 02/11/2026. Búsqueda de actualización del 02/11/2026.

## Figuras

Figuras no revisadas. [Ver el documento](https://pmc.ncbi.nlm.nih.gov/articles/PMC12783447/).

---

<!-- archivo: fuentes/articulos/2026-dhar-aapd-guia-lactancia.md -->
# Estudio: Evidence-Based Clinical Practice Guideline for Assessment and Management of Ankyloglossia in Infants With Breastfeeding Difficulties

- **ID:** DHAR2026GUIA
- **Autores, año y revista:** Dhar V; Marghalani AA; Amini H; Brickhouse T; Caffrey E; Jayaraman J; Keels MA; Messner A; Patterson KK; Raol N; Shrestha P; Stark C; Susarla HK; Thomas J. Pediatr Dent 2026;48(4):250-263.
- **DOI / PMID / URL:** PMID `42649580`. DOI: no consta en PubMed.
- **Tipo de estudio:** Guía de práctica clínica con GRADE. Publicada en la revista de la American Academy of Pediatric Dentistry; que sea guía oficial de la AAPD: `PENDIENTE DE VERIFICAR`.
- **Población y tamaño muestral:** Lactantes con frenillo restrictivo y dificultades de lactancia.
- **Definición diagnóstica y técnicas:** Basada en dos revisiones sistemáticas recientes (diagnóstico y frenotomía).
- **Criterio diagnóstico de anquiloglosia:** MIXTO (aspecto y función). Aconseja valorar la lengua de forma anatómica y funcional. Según su revisión de diagnóstico, la herramienta con más apoyo fue BTAT/TABBY.
- **Variables de resultado:** Diagnóstico, asociación con dificultades de alimentación, beneficio de la frenotomía, técnica, cuidados y efectos adversos.
- **Resultados NUMÉRICOS verificados:** 12 recomendaciones, todas condicionales y basadas en evidencia de certeza muy baja. Sugiere asociación entre frenillo restrictivo y dificultades de alimentación, y posibles beneficios de la frenotomía en casos muy seleccionados.
- **Límites metodológicos / confusores:** Certeza muy baja en todas las recomendaciones. Dirigida a dentistas.
- **Hallazgos contrarios o no significativos:** No aplica.
- **Conclusión que sí permite / que no permite:** Sí: Decir que la primera guía GRADE para lactantes recomienda valorar aspecto y función, con certeza muy baja. No: Decir que haya un criterio diagnóstico validado con certeza alta.
- **Licencia y derechos:** Derechos de la revista. Aquí solo resumen propio.
- **Estado de lectura:** Resumen de PubMed revisado el 02/11/2026. Búsqueda de actualización del 02/11/2026.

## Figuras

Figuras no revisadas.

---

<!-- archivo: fuentes/articulos/2026-dhar-revision-diagnostico.md -->
# Estudio: Diagnostic Assessment of Ankyloglossia and Association With Infant Feeding Challenges: A Systematic Review and Meta-Analysis, Part 1

- **ID:** DHAR2026DX
- **Autores, año y revista:** Dhar V; Marghalani AA; Amini H et al. Pediatr Dent 2026;48(2):82-68E.
- **DOI / PMID / URL:** PMID `42050817`; PROSPERO CRD42024482618.
- **Tipo de estudio:** Revisión sistemática y metaanálisis con GRADE.
- **Población y tamaño muestral:** 20 estudios incluidos, 14 analizados; 5 herramientas específicas de anquiloglosia.
- **Definición diagnóstica y técnicas:** MEDLINE, CINAHL, Embase y Cochrane hasta mayo de 2025.
- **Criterio diagnóstico de anquiloglosia:** MIXTO. Compara herramientas de aspecto y función. Concluye que la certeza muy baja apoya usar valoraciones estandarizadas anatómicas y funcionales (movilidad).
- **Variables de resultado:** Precisión diagnóstica de herramientas; asociación con dificultades de alimentación.
- **Resultados NUMÉRICOS verificados:** BTAT/TABBY: AUC 0,95 (más de 2.000 casos), consistencia interna α=0,708, correlación con Hazelbaker r=0,89. Dificultades de alimentación referidas por la madre: OR combinada 5,57 (IC 95 % 0,44-70,02; P=0,18; I²=96 %).
- **Límites metodológicos / confusores:** Heterogeneidad **I² 96 %** en la asociación con dificultades de alimentación referidas por la madre, IC muy amplio para OR 5,57, certeza global **muy baja**. La AUC 0,95 de BTAT/TABBY indica **discriminación en las muestras estudiadas**; el resumen no define un patrón de referencia diagnóstico independiente con el cual comprobarla. Consistencia interna y correlación con Hazelbaker no implican capacidad de predecir beneficio de frenotomía.
- **Hallazgos contrarios o no significativos:** La asociación agrupada con dificultad de alimentación materna fue **no significativa**: OR 5,57, IC95 % **0,44–70,02**, p=0,18. Su rango comprende asociación protectora, ausencia de asociación y asociación perjudicial de gran magnitud; **no es prueba precisa a favor ni en contra**, pero es un resultado desfavorable a la afirmación de asociación demostrada.
- **Conclusión que sí permite / que no permite:** Sí: esta revisión identifica datos de discriminación de BTAT/TABBY y respalda combinar estructura + función **con certeza muy baja**. No: presentar BTAT/TABBY como patrón oro, confundir asociación con alimentación como efecto demostrado o generalizar datos de lactantes a movilidad posterior/cara/esqueleto de adolescentes.
- **Licencia y derechos:** Derechos de la revista. Aquí solo resumen propio.
- **Estado de lectura:** Resumen PubMed revisado y contrastado el **03/11/2026**. **Texto completo y tablas de los 14 estudios incluidos no auditados**. PROSPERO CRD42024482618.

## Figuras

Figuras no revisadas.

## Actualización crítica de 03/11/2026

**Interrogante para comprobar en PDF:** ¿contra qué criterio independiente calculan AUC de 0,95 para BTAT/TABBY? Sin un estándar independiente, AUC/fiabilidad no justifican afirmar «diagnóstico validado» en sentido clínico amplio. Ver Necus 2025 y Kumar 2025.

---

<!-- archivo: fuentes/articulos/2026-dhar-revision-frenotomia.md -->
# Estudio: Frenotomy for Ankyloglossia Associated With Feeding Challenges in Infants: Effectiveness, Technique, and Safety. A Systematic Review and Meta-Analysis, Part 2

- **ID:** DHAR2026FX
- **Autores, año y revista:** Dhar V; Marghalani AA; Amini H et al. Pediatr Dent 2026;48(2):33E-68E.
- **DOI / PMID / URL:** PMID `42050812`; PROSPERO CRD42024482618.
- **Tipo de estudio:** Revisión sistemática y metaanálisis con GRADE.
- **Población y tamaño muestral:** 47 estudios: 8 ensayos aleatorizados y 39 observacionales.
- **Definición diagnóstica y técnicas:** MEDLINE, CINAHL, Embase y Cochrane hasta mayo de 2025.
- **Criterio diagnóstico de anquiloglosia:** MIXTO entre estudios: `PENDIENTE DE VERIFICAR` qué herramienta usó cada uno.
- **Variables de resultado:** Dificultades de alimentación, técnica, cuidados y efectos adversos.
- **Resultados NUMÉRICOS verificados:** Reducción grande del dolor del pezón mantenida en el seguimiento. Mejoría de la percepción materna. LATCH: mejoras grandes en estudios de un solo brazo pero diferencias mínimas frente a control en los ensayos. Tijera y láser, comparables. Efectos adversos: 4 % (sobre todo sangrado).
- **Límites metodológicos / confusores:** Certeza muy baja; muchos estudios sin grupo control.
- **Hallazgos contrarios o no significativos:** Diferencias mínimas en LATCH en los ensayos controlados.
- **Conclusión que sí permite / que no permite:** Sí: Decir que apoya la frenotomía, con certeza muy baja, en casos muy seleccionados con limitación funcional documentada y tras fallar el manejo conservador. No: Generalizarla a todos los lactantes con frenillo.
- **Licencia y derechos:** Derechos de la revista. Aquí solo resumen propio.
- **Estado de lectura:** Resumen de PubMed revisado el 02/11/2026. Búsqueda de actualización del 02/11/2026.

## Figuras

Figuras no revisadas.

---

<!-- archivo: fuentes/articulos/2026-ferres-amat-variabilidad.md -->
# Estudio: International Variability in the Diagnosis and Management of Ankyloglossia Among Dental Professionals: A Cross-Sectional Study

- **ID:** FERRESAMAT2026
- **Autores, año y revista:** Ferrés-Amat E; Perez-Torres C; Giovannelli MC; Vallés-Creixell A et al. (Universitat Internacional de Catalunya y otros). Dent J (Basel) 2026;14(7):436.
- **DOI / PMID / URL:** DOI `10.3390/dj14070436`; PMID `42505744`; PMC13407947.
- **Tipo de estudio:** Encuesta transversal.
- **Población y tamaño muestral:** 1.188 dentistas de España, Italia, Portugal, Brasil, Ecuador y Chile (febrero 2023-febrero 2025).
- **Definición diagnóstica y técnicas:** Cuestionario validado de 27 preguntas.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA como estudio diagnóstico: describe qué criterios usan los dentistas.
- **Variables de resultado:** Práctica diagnóstica y terapéutica autodeclarada.
- **Resultados NUMÉRICOS verificados:** El 80,7 % examina el frenillo de rutina; el 42,4 % usa una clasificación formal. La valoración de la movilidad fue el método más citado, con gran variación entre países. La cirugía fue el manejo más citado (38,7 %).
- **Límites metodológicos / confusores:** Autodeclarado; muestra no aleatoria.
- **Hallazgos contrarios o no significativos:** No aplica.
- **Conclusión que sí permite / que no permite:** Sí: Decir que hay gran variabilidad internacional, también en España, en cómo se diagnostica y trata. No: Medir lo que se hace realmente en consulta.
- **Licencia y derechos:** Acceso abierto (MDPI, PMC). Aquí solo resumen propio.
- **Estado de lectura:** Resumen de PubMed revisado el 02/11/2026. Búsqueda de actualización del 02/11/2026.

## Figuras

Figuras no revisadas. [Ver el documento](https://pmc.ncbi.nlm.nih.gov/articles/PMC13407947/).

---

<!-- archivo: fuentes/articulos/2026-he-frenillo-mandibula-apnea.md -->
# Estudio: Lingual frenulum, craniofacial morphology, and obstructive sleep apnea: a mediation analysis

- **ID:** HE2026
- **Autores, año y revista:** He S; Liu Y; Zhao Z. Sleep Breath 2026;30(1):66.
- **DOI / PMID / URL:** DOI `10.1007/s11325-026-03618-x`; PMID `41748815`
- **Tipo de estudio:** Transversal de casos y controles con análisis de mediación.
- **Población y tamaño muestral:** 222 adultos chinos de una unidad de sueño (20 a 70 años; 80 % hombres según el texto completo). No son niños.
- **Definición diagnóstica y técnicas:** Cara y frenillo por fotogrametría. Movilidad con TRMR. Apnea definida como IAH ≥15 (texto completo).
- **Criterio diagnóstico de anquiloglosia:** MIXTO. Longitud del frenillo por foto y movilidad funcional por TRMR (corte <60 % según la lectura del texto completo del equipo).
- **Variables de resultado:** Retroposición mandibular, ángulo y área del triángulo mandibular, IAH.
- **Resultados NUMÉRICOS verificados:** Frenillo más corto y menos movilidad se correlacionan con mandíbula más retrasada (r=-0,18 y -0,22) y área mandibular menor (r=0,17 y 0,18). La mandíbula «media» el 60,43 % (retroposición) y el 66,79 % (área) de la relación entre movilidad e IAH.
- **Límites metodológicos / confusores:** Transversal. Correlaciones débiles. Del texto completo (lectura previa del equipo): la relación directa entre movilidad e IAH no es significativa (r=-0,08; p=0,07); cifras que no cuadran (44 % con apnea en el resumen frente a 142 de 222 en el texto); erratas («p = 0.0.1» también en el resumen).
- **Hallazgos contrarios o no significativos:** Los autores plantean la dirección contraria: una mandíbula pequeña por genética llevaría la lengua atrás y el frenillo sería corto como consecuencia.
- **Conclusión que sí permite / que no permite:** Sí: Decir que en adultos frenillo corto, poca movilidad y mandíbula pequeña y retrasada van juntos. No: Decir que el frenillo «hace» la mandíbula pequeña.
- **Licencia y derechos:** Derechos del editor. Aquí solo metadatos y resumen propio.
- **Estado de lectura:** Resumen PubMed revisado el 17/10/2026. Texto completo revisado (PDF vía ClinicalKey, 15/10/2026); los datos que no están en el resumen salen de esa lectura.

## Figuras

Figuras no revisadas: el texto completo no está en acceso abierto en PMC. [Ver el artículo](https://doi.org/10.1007/s11325-026-03618-x).

---

<!-- archivo: fuentes/articulos/2026-kang-rinitis-activaciones-psg.md -->
# Estudio: Association of allergic rhinitis with polysomnographic arousal indices in children with sleep-disordered breathing

- **ID:** KANG2026AR
- **Autores, año y revista:** Kang T-Y; Wei C-C; Hang L-W et al.. *BMC Pediatrics, 2026 (publicación anticipada, 21/09/2026)*.
- **DOI / PMID / URL:** DOI `10.1186/s12887-026-07684-8`; [original](https://doi.org/10.1186/s12887-026-07684-8).
- **Tipo de estudio:** Estudio observacional retrospectivo.
- **Población y tamaño muestral:** 643 niños menores de 12 años derivados a polisomnografía en un centro terciario de Taiwán (datos 2009–2020).
- **Definición diagnóstica y técnicas:** PSG pediátrica y diagnóstico clínico de rinitis alérgica (AR); cuatro grupos según OSA vs ronquido simple y presencia/ausencia de AR. Modelo multivariable binomial negativo para índices de microdespertares ajustado por variables clínicas (incluida asma y OSA). Se requieren tablas completas para comprobar todos los covariables, definiciones individuales y valores absolutos por grupo.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA: no se diagnostica ni clasifica anquiloglosia; se examinan otros fenómenos respiratorios, del sueño o craneofaciales.
- **Variables de resultado:** Índice de microdespertares respiratorios, microdespertares asociados a movimientos periódicos de extremidades, eventos respiratorios y arquitectura del sueño.
- **Resultados NUMÉRICOS verificados:** En comparaciones de grupos con OSA, coexistir rinitis alérgica se relacionó con más eventos respiratorios y un índice de microdespertares respiratorios más alto (**ambos p<0,001**). El análisis ajustado **NO comunica en el resumen un efecto independiente de la rinitis sobre ese índice respiratorio**; sí registra menor tasa ajustada de microdespertares por movimientos periódicos de extremidades con rinitis: aIRR **0,393** (IC95% 0,183–0,848; p=0,017). Para los microdespertares respiratorios, otros predictores ajustados fueron OSA aIRR **12,382** (p<0,0001), sexo masculino **1,643** (p=0,006), IMC **1,048** (p=0,018), enuresis **2,065** (p=0,029) y edad **0,914** (p=0,011).
- **Límites metodológicos / confusores:** Retrospectivo; derivación por sospecha de SDB, no representativo de todos los niños; gravedad de apnea, asma, alergia y confusores; posibles problemas de inferencia con grupos derivados. No se midió postura lingual ni crecimiento maxilomandibular.
- **Hallazgos contrarios o no significativos:** Los índices de microdespertares **no** evolucionan todos en la misma dirección: rinitis asociada a **menos**, no más, activaciones por movimientos periódicos tras ajuste. Un contraste bruto entre grupos con OSA/AR no justifica afirmar que AR sea predictor independiente de microdespertares respiratorios en el modelo multivariable.
- **Conclusión que sí permite / que no permite:** Permite describir asociaciones en PSG de niños derivados. No demuestra que rinitis cause apnea ni que su tratamiento corrija microdespertares o desarrollo facial.
- **Licencia y derechos:** Artículo abierto; síntesis original sin reproducción de figuras ni PDF.
- **Estado de lectura:** Publicación primaria en acceso abierto localizada y consultados resumen, modelo descrito y datos ajustados publicados en su página editorial ([Springer Nature](https://link.springer.com/article/10.1186/s12887-026-07684-8)), 03/11/2026. **Tablas completas y todos los métodos no auditados de principio a fin**; no declarar extracción integral del PDF. Versión anticipada susceptible de correcciones editoriales.

## Figuras

No incorporadas ni auditadas. [Artículo original](https://doi.org/10.1186/s12887-026-07684-8).

---

<!-- archivo: fuentes/articulos/2026-koento-anquiloglosia-trs-ninos.md -->
# Estudio: Ankyloglossia and its association with sleep-disordered breathing in children: A systematic review

- **ID:** KOENTO2026
- **Autores, año y revista:** Koento T; Widjaja S. Int J Pediatr Otorhinolaryngol 2026;202:112717.
- **DOI / PMID / URL:** DOI `10.1016/j.ijporl.2026.112717`; PMID `41544402`
- **Tipo de estudio:** Revisión sistemática sin metaanálisis.
- **Población y tamaño muestral:** 6 estudios (2015-2025), niños de 8 a 10 años de media, muestras de 82 a 504: tres cohortes, dos casos y controles y un transversal (texto completo).
- **Definición diagnóstica y técnicas:** Síntesis narrativa porque cada estudio mide distinto.
- **Criterio diagnóstico de anquiloglosia:** MIXTO. Unos estudios miden la longitud del frenillo y otros la movilidad. Los dos con polisomnografía que separan ambas cosas (Yuen 2022 y Cohen-Levy 2020) encuentran asociación con la movilidad y no con la longitud.
- **Variables de resultado:** Trastorno respiratorio del sueño por cuestionario o por estudio de sueño.
- **Resultados NUMÉRICOS verificados:** Del texto completo (lectura previa del equipo): con cuestionario, OR 5,02 (Brożek-Mądry 2021), OR 7,11 con IC 1,26-40 (Burska 2022) y OR 2,98 ajustado en 504 niños (Villa 2020). Con estudio de sueño: Yuen 2022, longitud <16 mm sin diferencia y movilidad baja con OR 3,65 ajustado; Guilleminault 2016, IAH 13,1 frente a 11,4 solo en varones.
- **Límites metodológicos / confusores:** Estudios transversales, cuestionarios, muestras pequeñas y posible sesgo de publicación. Brożek-Mądry 2021 y Burska 2022 son del mismo grupo y con grupos casi idénticos: puede que sea la misma muestra contada dos veces (`PENDIENTE DE VERIFICAR`).
- **Hallazgos contrarios o no significativos:** La longitud del frenillo sola no se asocia en los estudios con polisomnografía.
- **Conclusión que sí permite / que no permite:** Sí: Decir que hay asociación entre anquiloglosia y trastorno respiratorio del sueño en niños, y que pesa más la movilidad que la longitud. No: Afirmar causa.
- **Licencia y derechos:** Derechos del editor. Aquí solo metadatos y resumen propio.
- **Estado de lectura:** PubMed sin resumen. Texto completo revisado (PDF vía ClinicalKey, 15/10/2026); las cifras salen de esa lectura y PENDIENTE DE VERIFICAR antes de publicarlas.

## Figuras

Figuras no revisadas: el texto completo no está en acceso abierto en PMC. [Ver el artículo](https://doi.org/10.1016/j.ijporl.2026.112717).

---

<!-- archivo: fuentes/articulos/2026-lee-neuroconducta-adenoamigdalectomia.md -->
# Estudio: Neurobehavioral outcomes after adenotonsillectomy for pediatric sleep-disordered breathing: A systematic review and meta-analysis

- **ID:** LEE2026
- **Autores, año y revista:** Lee YC; Lu CT; Wang YT et al.. Am J Otolaryngol 2026;47(5):104886.
- **DOI / PMID / URL:** DOI `10.1016/j.amjoto.2026.104886`; PMID `42456309`
- **Tipo de estudio:** Revisión sistemática y metaanálisis.
- **Población y tamaño muestral:** 8 estudios originales.
- **Definición diagnóstica y técnicas:** Búsqueda hasta agosto de 2025; efectos aleatorios.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA: el estudio no diagnostica anquiloglosia.
- **Variables de resultado:** Conducta referida por padres, función ejecutiva, medidas neurocognitivas objetivas y de TDAH.
- **Resultados NUMÉRICOS verificados:** Conducta según padres: DME -0,58 (IC -1,15 a -0,02). Función ejecutiva: DME -0,25 (IC -0,45 a -0,05). Medidas objetivas y de TDAH: no significativas, aunque a favor de la cirugía.
- **Límites metodológicos / confusores:** Pocos estudios.
- **Hallazgos contrarios o no significativos:** Las medidas objetivas de TDAH no salen significativas.
- **Conclusión que sí permite / que no permite:** Sí: Decir que tras operar mejoran la conducta referida y algo la función ejecutiva. No: Decir que mejoran las medidas objetivas de TDAH.
- **Licencia y derechos:** Derechos del editor. Aquí solo metadatos y resumen propio.
- **Estado de lectura:** Resumen PubMed revisado el 17/10/2026.

## Figuras

Figuras no revisadas: el texto completo no está en acceso abierto en PMC. [Ver el artículo](https://doi.org/10.1016/j.amjoto.2026.104886).

---

<!-- archivo: fuentes/articulos/2026-leow-tdah-apnea.md -->
# Estudio: Association between Attention Deficit Hyperactivity Disorder and Obstructive Sleep Apnea in Children: A Systematic Review and Meta-Analysis

- **ID:** LEOW2026
- **Autores, año y revista:** Leow BHW; Tan CJ; Yeo BSY et al.. J Atten Disord 2026;30(6):822-832.
- **DOI / PMID / URL:** DOI `10.1177/10870547261426094`; PMID `41910119`
- **Tipo de estudio:** Revisión sistemática y metaanálisis de estudios longitudinales. GRADE.
- **Población y tamaño muestral:** 11 estudios, 903 niños con diagnóstico formal de apnea o de TDAH.
- **Definición diagnóstica y técnicas:** Búsqueda hasta diciembre de 2024.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA: el estudio no diagnostica anquiloglosia.
- **Variables de resultado:** Prevalencia de apnea en TDAH; efecto de la adenoamigdalectomía.
- **Resultados NUMÉRICOS verificados:** Prevalencia conjunta de apnea en niños con TDAH: 44 %. El intervalo de confianza que da el resumen de PubMed (2 % a 56 %) es muy ancho y parece mal transcrito: PENDIENTE DE VERIFICAR en el original.
- **Límites metodológicos / confusores:** La parte de tratamiento es descriptiva, sin metaanálisis.
- **Hallazgos contrarios o no significativos:** No aplica.
- **Conclusión que sí permite / que no permite:** Sí: Recomendar valorar la apnea en niños con síntomas de TDAH. No: Usar el 44 % como dato preciso sin revisar el intervalo.
- **Licencia y derechos:** Derechos del editor. Aquí solo metadatos y resumen propio.
- **Estado de lectura:** Resumen PubMed revisado el 17/10/2026.

## Figuras

Figuras no revisadas: el texto completo no está en acceso abierto en PMC. [Ver el artículo](https://doi.org/10.1177/10870547261426094).

---

<!-- archivo: fuentes/articulos/2026-li-rinitis-sueno-metaanalisis.md -->
# Estudio: Allergic rhinitis in children in relation to sleep breathing disorders: a meta-analysis

- **ID:** LI2026AR
- **Autores, año y revista:** Li Q; Zhong Q; Kong X et al.. *International Journal of Pediatric Otorhinolaryngology 207 (2026):112902*.
- **DOI / PMID / URL:** DOI `10.1016/j.ijporl.2026.112902`; PMID `42302637`; [original](https://doi.org/10.1016/j.ijporl.2026.112902).
- **Tipo de estudio:** Revisión sistemática y metaanálisis, principalmente de estudios observacionales.
- **Población y tamaño muestral:** 17 estudios; 32.907 niños.
- **Definición diagnóstica y técnicas:** PubMed, Embase, Web of Science y Cochrane desde inicio hasta el **10/11/2022** (aunque el artículo se publicó en 2026); se compararon grupos de ronquido habitual, SDB y apnea.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA: no se diagnostica ni clasifica anquiloglosia; se examinan otros fenómenos respiratorios, del sueño o craneofaciales.
- **Variables de resultado:** Prevalencia y asociación de rinitis alérgica con ronquido habitual, trastornos respiratorios del sueño y apnea obstructiva.
- **Resultados NUMÉRICOS verificados:** Rinitis alérgica en ronquido habitual vs no ronquido: OR 2,24 (IC95% 1,66–3,02; I²=34%); SDB vs no SDB: OR 1,49 (1,12–1,98; I²=77%); OSA vs no OSA: OR 1,23 (1,04–1,46; I²=46%).
- **Límites metodológicos / confusores:** Alta heterogeneidad para SDB; búsqueda detenida en 2022; no identifica causalidad ni respuesta al tratamiento de rinitis; los desenlaces ronquido/SDB/OSA no son equivalentes.
- **Hallazgos contrarios o no significativos:** El efecto agrupado para apnea es menor que para ronquido y no equivale a una estimación causal.
- **Conclusión que sí permite / que no permite:** Sostiene una asociación epidemiológica entre rinitis y distintos fenotipos de SDB infantil. No demuestra que la rinitis cause malformación maxilar ni que tratarla cure apnea.
- **Licencia y derechos:** Derechos del editor; síntesis original sin PDF ni figuras reproducidas.
- **Estado de lectura:** Resumen de PubMed y editorial verificados el 03/11/2026; texto completo editorial no consultado.

## Figuras

No incorporadas ni auditadas. [Artículo original](https://doi.org/10.1016/j.ijporl.2026.112902).

---

<!-- archivo: fuentes/articulos/2026-lopez-segura-ensayo-miofuncional.md -->
# Estudio: Comparative Effectiveness of Myofunctional Therapy and Breastfeeding Education for Ankyloglossia: A Randomized Controlled Trial

- **ID:** LOPEZSEGURA2026
- **Autores, año y revista:** López-Segura G; Romero-Del Rey R; Murillo-de Las Heras MDM; Requena-Mullor M; Rodríguez-Pérez M; Alarcón-Rodríguez R; García-González J (Almería, España). J Hum Lact 2026 (en línea antes de impresión).
- **DOI / PMID / URL:** DOI `10.1177/08903344261459944`; PMID `42466810`.
- **Tipo de estudio:** Ensayo aleatorizado de dos brazos, simple ciego.
- **Población y tamaño muestral:** 200 lactantes con anquiloglosia (100 por grupo), julio-noviembre de 2023.
- **Definición diagnóstica y técnicas:** Terapia miofuncional pasiva (estiramientos y masajes orales) frente a educación en lactancia durante 1 mes.
- **Criterio diagnóstico de anquiloglosia:** MIXTO. Usa Hazelbaker (ATLFF), con sus partes de aspecto y de función. Criterio de inclusión exacto: `PENDIENTE DE VERIFICAR`.
- **Variables de resultado:** Función del frenillo (ATLFF), lactancia (LATCH), dolor del pezón (EVA), evitar cirugía.
- **Resultados NUMÉRICOS verificados:** Sin cambios en el aspecto (ATLFF-Apariencia). Tras la intervención, el grupo de terapia tuvo más puntuación de función (r=0,33), menos dolor (r=-0,38) y más LATCH (r=0,26), todo p<0,001. Más probabilidad de evitar la cirugía (OR 4,63; p=0,005).
- **Límites metodológicos / confusores:** Un mes de seguimiento; resultados como tamaños de efecto r; cegamiento solo simple.
- **Hallazgos contrarios o no significativos:** No aplica.
- **Conclusión que sí permite / que no permite:** Sí: Decir que un ensayo español encontró que la terapia oral pasiva mejoró función y lactancia más que la educación sola, a un mes. No: Generalizar a largo plazo ni compararla con la frenotomía.
- **Licencia y derechos:** Derechos de la revista. Aquí solo resumen propio.
- **Estado de lectura:** Resumen de PubMed revisado el 02/11/2026. Búsqueda de actualización del 02/11/2026.

## Figuras

Figuras no revisadas.

---

<!-- archivo: fuentes/articulos/2026-maclean-cts-diagnostico-apnea.md -->
# Estudio: The Canadian Thoracic Society/Canadian Sleep Society Guideline on the Diagnosis of Obstructive Sleep Apnea in Children

- **ID:** MACLEAN2026
- **Autores, año y revista:** MacLean JE; Adeleye A; Van Dam A; Lal A; Abusido T; Adamko DJ; Amin R; Campisi P; Constantin E; Duncan J; Dyck G; Jones J; Kevat A; Lee J; Shi J; Zelman M; KidsCan YPRAG. *Chest* 2026;170(2):565-582. También publicada en *Can J Respir Crit Care Sleep Med* (24/03/2026).
- **DOI / PMID / URL:** DOI `10.1016/j.chest.2025.12.017`; PMID `41887281`; versión canadiense DOI 10.1080/24745332.2026.2629327 (https://www.tandfonline.com/doi/full/10.1080/24745332.2026.2629327).
- **Tipo de estudio:** Guía de práctica clínica con revisión sistemática y metaanálisis de pruebas alternativas a la polisomnografía. Recomendaciones votadas por un panel de 14 miembros, teniendo en cuenta las preferencias de pacientes y familias.
- **Población y tamaño muestral:** Niños menores de 18 años con sospecha de apnea. 250 artículos en 5 tipos de valoración clínica.
- **Definición diagnóstica y técnicas:** Compara con la polisomnografía la poligrafía domiciliaria (nivel 3), el cuestionario pediátrico de sueño (PSQ) y la oximetría nocturna, entre otras.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA: guía de diagnóstico de apnea. Búsqueda en el texto completo el 05/11/2026: no aparecen «ankyloglossia», «tongue», «frenulum» ni «myofunctional».
- **Variables de resultado:** Exactitud diagnóstica frente a la polisomnografía.
- **Resultados NUMÉRICOS verificados:** La polisomnografía sigue siendo el estándar. La poligrafía domiciliaria de nivel 3 se recomienda como segunda opción en niños sanos de más de 5 años sin acceso real a polisomnografía (recomendación fuerte, evidencia baja a moderada), con un área bajo la curva de 0,88 a 0,92 frente a la polisomnografía. El PSQ y la oximetría nocturna aportan información, pero se sugiere no usarlos para diagnosticar. El 62 % de los artículos excluía a niños con comorbilidades y el 26 % no informaba de exclusiones; solo el 13 % incluía menores de 2 años.
- **Límites metodológicos / confusores (solo los relevantes):** No trata el tratamiento de la apnea. Pocos datos se pudieron combinar en metaanálisis.
- **Otros resultados relevantes (si los hay):** Su recomendación sobre la poligrafía domiciliaria difiere de la de la AASM de 2017, que la desaconsejaba en niños.
- **Aportación del estudio:** Es la guía de apnea infantil más reciente localizada (marzo de 2026).
- **Licencia y derechos:** `PENDIENTE DE VERIFICAR`. Aquí solo resumen propio.
- **Estado de lectura:** Resumen de Europe PMC y texto completo de la versión canadiense (recomendaciones y tabla 1) leídos el 05/11/2026.

## Figuras

Figuras no revisadas. [Ver la guía](https://www.tandfonline.com/doi/full/10.1080/24745332.2026.2629327).

---

<!-- archivo: fuentes/articulos/2026-mahony-expansion-amigdalectomia.md -->
# Estudio: Maxillary Arch Expansion and Adenotonsillectomy in Prepubertal Children Diagnosed with Paediatric Obstructive Sleep Apnoea: An Interventional Study

- **ID:** MAHONY2026A
- **Autores, año y revista:** Mahony D; Bhattarai N; Petocz P. *J Clin Med* 2026;15(8):2981. Publicado el 14/04/2026.
- **DOI / PMID / URL:** DOI `10.3390/jcm15082981`; PMID `42074783`; PMC13116212; https://www.mdpi.com/2077-0383/15/8/2981
- **Tipo de estudio:** Cohorte retrospectiva no aleatorizada (los autores la titulan «interventional study»).
- **Población y tamaño muestral:** 80 niños de 7 a 9 años (edad media 8,31; 35 niños y 45 niñas) con apnea confirmada por polisomnografía, maxilar estrecho e hipertrofia adenoamigdalar, de una cohorte de 3.671 niños de clínicas privadas de ortodoncia (2007-2022). 39 se operaron primero de amígdalas y vegetaciones y después hicieron expansión semirrápida del maxilar; 41 hicieron primero la expansión (por esperas para el otorrino o el seguro) y después la cirugía.
- **Definición diagnóstica y técnicas:** Polisomnografía de nivel 1 al inicio y 3 meses después de cada tratamiento. Desenlace: índice de alteración respiratoria (RDI).
- **Criterio diagnóstico de anquiloglosia:** NO APLICA: el estudio no valora la anquiloglosia. Búsqueda en el texto completo el 05/11/2026: no aparecen «ankyloglossia» ni «frenulum».
- **Variables de resultado:** RDI tras el primer tratamiento y tras los dos.
- **Resultados NUMÉRICOS verificados:** RDI inicial 18,99 ± 1,66 por hora. Tras los dos tratamientos (medias ajustadas, combinando categorías de IMC): 4,86 si la cirugía fue primero y 4,19 si la expansión fue primero. La primera bajada fue mayor con la expansión que con la cirugía (diferencia ajustada 1,49; p = 0,002), y la diferencia se mantuvo al final (1,42; p = 0,007). El IMC influyó: con peso normal el RDI final ajustado fue de 2,79 a 3,14 y con obesidad de 5,02 a 6,28.
- **Límites metodológicos / confusores (solo los relevantes):** Orden de los tratamientos decidido por preferencia y logística, no por azar. Los grupos difieren en IMC: 24 de 39 con obesidad en el grupo de cirugía primero frente a 6 de 41 en el de expansión primero (ajustado en el modelo). Ningún niño normalizó el RDI con los dos tratamientos.
- **Otros resultados relevantes (si los hay):** Los autores atribuyen la apnea residual a la resistencia nasal, la postura lingual alterada y factores neuromusculares, y proponen la terapia miofuncional como posible complemento; lo estudian después en Mahony 2026b.
- **Aportación del estudio:** Muestra de partida del estudio de terapia miofuncional de octubre de 2026.
- **Licencia y derechos:** CC BY 4.0 (MDPI).
- **Estado de lectura:** Texto completo (Europe PMC) leído el 05/11/2026: métodos, tablas 1 y 2 y conclusiones.

## Figuras

Licencia CC BY. Figuras no copiadas. Figura 1: diagrama de selección. Figura 3: RDI ajustado por orden, IMC y momento. [Ver el artículo](https://pmc.ncbi.nlm.nih.gov/articles/PMC13116212/).

---

<!-- archivo: fuentes/articulos/2026-mahony-miofuncional-apnea-residual.md -->
# Estudio: Orofacial Myofunctional Therapy to Treat Residual Obstructive Sleep Apnoea in Children Treated with Adenotonsillectomy and Maxillary Expansion: An Interventional Study

- **ID:** MAHONY2026B
- **Autores, año y revista:** Mahony D; Bhattarai N; Petocz P; Borbély P; Kárpáti K. *J Clin Med* 2026;15(19):7676. Publicado el 04/10/2026 (preprint en septiembre de 2026).
- **DOI / PMID / URL:** DOI `10.3390/jcm15197676`; PMID `42882137`; https://www.mdpi.com/2077-0383/15/19/7676
- **Tipo de estudio:** Cohorte retrospectiva no aleatorizada (los autores la titulan «interventional study»). Seguimiento de 12 meses de la misma muestra de Mahony 2026a.
- **Población y tamaño muestral:** 80 niños de 7 a 9 años (edad media 8,3), de una cohorte de 3.671 niños atendidos en su primera consulta en nueve clínicas privadas de ortodoncia de Australia de un mismo especialista (2007-2022). Todos con apnea residual confirmada por polisomnografía (índice de alteración respiratoria, RDI, de 1 o más por hora) tras adenoamigdalectomía y expansión semirrápida del maxilar. 41 completaron 12 meses de terapia miofuncional orofacial y 39 no. Excluidos: síndromes genéticos, alteraciones craneofaciales (salvo el maxilar estrecho), problemas del desarrollo, traumatismos, tumores y cualquier otra intervención de otorrino u ortodoncia durante los 12 meses.
- **Definición diagnóstica y técnicas:** Polisomnografía de nivel 1 en laboratorio, puntuada a mano por técnicos que no sabían a qué grupo pertenecía cada niño (reglas pediátricas de la AASM). Desenlace principal: RDI (apneas, hipopneas y despertares por esfuerzo respiratorio por hora). Terapia: 24 sesiones quincenales con un terapeuta miofuncional y 10 a 15 minutos diarios de ejercicios en casa, con diario de cumplimiento rellenado por los padres.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA: el estudio no valora la anquiloglosia. Búsqueda en el texto completo el 05/11/2026: no aparecen «ankyloglossia», «tongue-tie», «frenulum», «frenotomy» ni «frenectomy». No informa de la movilidad lingual de los niños ni de frenotomías previas.
- **Variables de resultado:** RDI a los 12 meses y su cambio desde el final de los dos tratamientos.
- **Resultados NUMÉRICOS verificados:** RDI al inicio del estudio (tras los dos tratamientos): 4,45 ± 1,71 en el conjunto, sin diferencia entre grupos (p = 0,21). A los 12 meses: 0,49 ± 0,60 con terapia (rango 0 a 2) frente a 5,26 ± 1,77 sin terapia (rango 1 a 8); diferencia 4,77 (IC 95 % 4,19 a 5,35; p < 0,001). Cambio: −4,20 ± 0,95 con terapia frente a +1,05 ± 0,61 sin terapia; todos los tratados mejoraron (−6 a −2) y ningún control mejoró (0 a +2). Ajustado por orden de los tratamientos, sexo, edad, raza, IMC y RDI inicial: medias 0,28 frente a 5,42 (p < 0,001). Motivos de no hacer la terapia: coste o acceso (22), falta de cumplimiento (9) y falta de interés (8), sin diferencias de resultado entre esos subgrupos.
- **Límites metodológicos / confusores (solo los relevantes):** Grupos decididos por las familias (capacidad de cumplir, coste, preferencia), no por azar; los autores dicen que es una asociación fuerte, no un efecto causal confirmado, que factores familiares no medidos pueden explicar parte de la diferencia, y que el rango estrecho de RDI residual favorece que los grupos no se solapen. Un solo especialista y práctica privada. Cumplimiento según diarios de los padres, sin verificar.
- **Otros resultados relevantes (si los hay):** Los autores lo comparan con Villa 2015 (ensayo aleatorizado, ejercicios orofaríngeos tras adenoamigdalectomía, IAH de 4,87 a 1,84) y con Guilleminault 2013 (niños ya normalizados: sin recaída con reeducación, IAH 0,5, frente a recaída sin ella, IAH 5,3). Declaran no tener conflictos de interés ni financiación externa.
- **Aportación del estudio:** Según los autores, es el primero en evaluar la terapia miofuncional en niños con apnea residual confirmada tras adenoamigdalectomía y expansión del maxilar, y el de seguimiento más largo con cumplimiento registrado.
- **Licencia y derechos:** CC BY 4.0 (MDPI). Se podrían copiar sus figuras con atribución.
- **Estado de lectura:** Texto completo HTML leído el 05/11/2026 (métodos, resultados, discusión y limitaciones). Las tablas no se han revisado celda a celda.

## Figuras

Licencia CC BY. Figuras no copiadas. Figura 1: diagrama de selección de pacientes. Figuras 2 y 3: distribución del RDI final y de su cambio por grupo. Figura 4: trayectoria individual de cada niño. Figura 5: trayectorias según el motivo de no hacer la terapia. [Ver el artículo](https://www.mdpi.com/2077-0383/15/19/7676).

---

<!-- archivo: fuentes/articulos/2026-marino-frenotomia-laringoscopia.md -->
# Estudio: Frenotomy Provides Improved Direct Laryngoscopy Exposure in Select Adult Patients With Ankyloglossia

- **ID:** MARINO2026
- **Autores, año y revista:** Marino GA; Garrett CG; Tate AD. Ear Nose Throat J 2026;105(10):613-616.
- **DOI / PMID / URL:** DOI `10.1177/01455613231223355`; PMID `38380620`
- **Tipo de estudio:** Serie de casos.
- **Población y tamaño muestral:** 2 adultos.
- **Definición diagnóstica y técnicas:** Frenotomía intraoperatoria antes de laringoscopia directa.
- **Criterio diagnóstico de anquiloglosia:** Restricción clínica de la protrusión, sin escala.
- **Variables de resultado:** Exposición de cuerdas vocales.
- **Resultados NUMÉRICOS verificados:** Mejor exposición tras frenotomía en los dos casos.
- **Límites metodológicos / confusores:** Dos casos.
- **Hallazgos contrarios o no significativos:** No aplica.
- **Conclusión que sí permite / que no permite:** Sí: Ilustrar una consecuencia práctica de la anquiloglosia en adultos. No: Generalizar.
- **Licencia y derechos:** Derechos del editor. Aquí solo metadatos y resumen propio.
- **Estado de lectura:** Resumen PubMed y texto completo revisados el 17/10/2026.

## Figuras

Licencia: derechos del editor (no se copian imágenes). Leyendas leídas en el texto completo; puede haber más figuras que las listadas.

- **Figura 1.** Anquiloglosia restrictiva en quirófano. [Ver en el artículo](https://doi.org/10.1177/01455613231223355), figura 1.
- **Figura 2.** Visión de la glotis tras la frenotomía. [Ver en el artículo](https://doi.org/10.1177/01455613231223355), figura 2.

---

<!-- archivo: fuentes/articulos/2026-palomo-aao-actualizacion.md -->
# Estudio: Sleep-disordered breathing and orthodontics: An American Association of Orthodontists white paper update

- **ID:** PALOMO2026
- **Autores, año y revista:** Palomo JM; Cohen-Levy J; Flores-Mir C; Khosravi R; Levine M; Pickard M; Hittner J; Callahan J; Siegel SM. *Am J Orthod Dentofacial Orthop* 2026;169(4):419-427. En línea el 02/03/2026.
- **DOI / PMID / URL:** DOI `10.1016/j.ajodo.2026.01.014`; PMID `41770191`; https://www.ajodo.org/article/S0889-5406(26)00035-1/fulltext
- **Tipo de estudio:** Actualización del documento de posición de 2019 (Behrents 2019), hecha por un grupo de ortodoncistas expertos en medicina dental del sueño a petición de la junta de la American Association of Orthodontists. PubMed lo clasifica como guía de práctica y declaración de consenso. Pasa de hablar de apnea a hablar de trastornos respiratorios del sueño en general.
- **Población y tamaño muestral:** Niños y adultos.
- **Definición diagnóstica y técnicas:** Polisomnografía con síntomas clínicos como referencia; solo un médico diagnostica; cribado con cuestionarios validados (PSQ en niños, STOP-Bang en adultos).
- **Criterio diagnóstico de anquiloglosia:** NO PROPONE NINGUNO. Señala la heterogeneidad de los criterios diagnósticos y la falta de una definición uniforme del grado de restricción que altera la forma o la función, salvo en las formas más graves. No menciona el TRMR ni otra medida funcional concreta.
- **Variables de resultado:** No aplica (documento de posición).
- **Resultados NUMÉRICOS verificados:** Nueve conclusiones, entre ellas: ninguna intervención ortodóncica, como la expansión del maxilar o los aparatos funcionales, ha demostrado prevenir los trastornos respiratorios del sueño; la ortodoncia no es un tratamiento aislado de esos trastornos; ningún fenotipo craneofacial conocido identifica su presencia; las medidas de la vía aérea en cefalometría o CBCT no sirven para diagnosticar, estimar riesgo ni valorar resultados (cambio respecto a 2019); **«Current evidence does not support ankyloglossia as an SDB etiology. Routine frenectomy is not recommended for SDB prevention or treatment»**; las extracciones y la distalización no afectan la etiología ni aumentan la probabilidad de estos trastornos. Expansión del maxilar: reservarla para pacientes con indicación ortodóncica clara y diagnóstico confirmado.
- **Límites metodológicos / confusores (solo los relevantes):** Revisión narrativa sin método sistemático descrito. En el apartado de frenectomía, las referencias numeradas no coinciden con lo que se les atribuye: la revisión de alcance de 2023 con 26 estudios se cita como referencia 41, que es Hicks 2017 (tono muscular de la vía aérea en sueño profundo), y la frase que atribuye al consenso de la AAO-HNS se cita como referencia 42, que es Cordray 2023. Esa frase junta dos cosas de Messner 2020: la afirmación de consenso 36 (no operar el «frenillo bucal») y una frase del texto, no votada como afirmación, sobre que la inserción anterior de la lengua evita en parte su colapso posterior y que liberarla podría empeorar la apnea. Messner apoya esa frase en dos referencias: Walsh 1995 (obstrucción parcial de la vía aérea tras una frenotomía) y Genther 2015 (dos lactantes con secuencia de Pierre Robin).
- **Otros resultados relevantes (si los hay):** Sobre la anquiloglosia recoge que una revisión de alcance de 2023 (26 estudios, más de 1.228 pacientes) encontró asociaciones entre anquiloglosia no tratada y factores de riesgo de apnea (maxilar estrecho, paladar blando alargado, colapso retrolingual), que solo un ensayo aleatorizado sugirió menos apnea tras la frenectomía, y que muchos estudios combinan adenoamigdalectomía, expansión rápida y frenectomía, de modo que no se puede separar el efecto de cada una. Dice que algunos estudios sugieren que la anquiloglosia puede contribuir al riesgo en pacientes seleccionados.
- **Aportación del estudio:** Es el documento de 2026 de la ortodoncia estadounidense sobre sueño y vía aérea, muy difundido en redes.
- **Licencia y derechos:** CC BY (según Europe PMC). Aquí solo resumen propio.
- **Estado de lectura:** Texto completo HTML leído el 05/11/2026: conclusiones y apartados de imagen, frenectomía, expansión, aparatos y extracciones, y referencias 41 a 45.

## Figuras

Figuras no revisadas. [Ver el artículo](https://doi.org/10.1016/j.ajodo.2026.01.014).

---

<!-- archivo: fuentes/articulos/2026-pisoni-miofuncional-umbrella-apnea.md -->
# Estudio: Myofunctional Therapy in Adults and Children With Obstructive Sleep Apnea: An Overview and Re-Analysis of Systematic Reviews

- **ID:** PISONI2026
- **Autores, año y revista:** Pisoni E; Buttafava L et al.. *Journal of Sleep Research, 2026, artículo electrónico publicado el 04/10/2025*.
- **DOI / PMID / URL:** DOI `10.1111/jsr.70219`; [original](https://doi.org/10.1111/jsr.70219).
- **Tipo de estudio:** Overview/umbrella review con reanálisis de revisiones y metaanálisis.
- **Población y tamaño muestral:** 9 revisiones sistemáticas, 21 estudios primarios únicos (13 ensayos y 8 estudios pre-post), n=716 en conjunto, principalmente datos de adultos para estimaciones globales.
- **Definición diagnóstica y técnicas:** Búsqueda PubMed, Embase y Cochrane hasta julio de 2024; reanálisis para reducir solapamiento de estudios, estimado 13,44%; calidad metodológica global de revisiones frecuentemente críticamente baja.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA: este estudio no diagnostica anquiloglosia ni utiliza escalas de frenillo.
- **Variables de resultado:** IAH, somnolencia diurna, sueño subjetivo, saturación mínima/medias y calidad del sueño; análisis por edades.
- **Resultados NUMÉRICOS verificados:** En adultos, efecto agrupado sobre gravedad de apnea: DM −9,54 (IC95% −14,04 a −5,04); somnolencia DM −3,62 (−6,61 a −0,63); saturación mínima +3,19 (1,47 a 4,91). **No extrapolar estas cifras a niños**: evidencia pediátrica escasa.
- **Límites metodológicos / confusores:** Solapamiento entre revisiones; riesgo de sesgo alto en estudios primarios y calidad críticamente baja en varias revisiones; heterogeneidad de ejercicio, adherencia, controles y duración; separación población adulta/pediátrica esencial.
- **Hallazgos contrarios o no significativos:** Los resultados agrupados favorables de adultos no contradicen por sí solos el metaanálisis pediátrico 2026 de Cnockaert, cuyos ECA no encontraron efecto concluyente en IAH.
- **Conclusión que sí permite / que no permite:** Puede sugerir beneficios de terapia miofuncional en algunos adultos con OSA; no constituye prueba sólida para indicar monoterapia miofuncional pediátrica ni prueba de efecto sobre desarrollo maxilar.
- **Licencia y derechos:** Derechos editoriales o de autores según el original; resumen crítico propio. No se incorporan PDF ni figuras ajenas.
- **Estado de lectura:** Resumen editorial de Wiley verificado el 03/11/2026; texto completo y cuadros de riesgo de sesgo pendientes.

## Figuras

No incorporadas ni evaluadas. [Original](https://doi.org/10.1111/jsr.70219).

---

<!-- archivo: fuentes/articulos/2026-singla-adenoamigdalectomia-crecimiento.md -->
# Estudio: Impact of adenotonsillectomy or adenoidectomy on dentofacial development of children with obstructed sleep disordered breathing - Systematic review

- **ID:** SINGLA2026
- **Autores, año y revista:** Singla A; Gangwal K; Puri A; Gupta A et al.. *International Journal of Pediatric Otorhinolaryngology 208 (2026):112923*.
- **DOI / PMID / URL:** DOI `10.1016/j.ijporl.2026.112923`; PMID `42456373`; [original](https://doi.org/10.1016/j.ijporl.2026.112923).
- **Tipo de estudio:** Revisión sistemática de estudios prospectivos/longitudinales observacionales.
- **Población y tamaño muestral:** 10 estudios sobre cambios dentofaciales en niños en crecimiento después de adenoidectomía o adenoamigdalectomía.
- **Definición diagnóstica y técnicas:** Búsqueda PubMed, Scopus y Web of Science hasta 2025; PROSPERO CRD420250511402; riesgo de sesgo ROBINS-I; evaluación de evolución dentoalveolar y cambios esqueléticos en población operada.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA: este estudio no diagnostica anquiloglosia ni utiliza escalas de frenillo.
- **Variables de resultado:** Patrones de crecimiento mandibular, inclinación de incisivos, dimensiones de arcada, normalización esquelética y momento de intervención.
- **Resultados NUMÉRICOS verificados:** 10 estudios incluidos; el resumen **no presenta magnitud de efecto combinada**.
- **Límites metodológicos / confusores:** Los estudios longitudinales observacionales no prueban efecto quirúrgico independiente de maduración, crecimiento normal y tratamientos ortodóncicos; selección por indicación clínica, posible regresión a media y seguimiento variable.
- **Hallazgos contrarios o no significativos:** No se documenta normalización completa o predecible del desarrollo craneofacial en todos los casos.
- **Conclusión que sí permite / que no permite:** Sugiere adaptaciones dentoalveolares favorables tras cirugía en ciertos grupos, pero sin probar reparación esquelética completa ni prevención causal generalizable.
- **Licencia y derechos:** Derechos editoriales o de autores según el original; resumen crítico propio. No se incorporan PDF ni figuras ajenas.
- **Estado de lectura:** Resumen PubMed y editorial revisados el 03/11/2026; texto completo pendiente.

## Figuras

No incorporadas ni evaluadas. [Original](https://doi.org/10.1016/j.ijporl.2026.112923).

---

<!-- archivo: fuentes/articulos/2026-sotero-grande-respiracion-craneofacial.md -->
# Estudio: Mouth Breathing and Craniofacial Development in Children: A Systematic Narrative Review and Clinical Implications

- **ID:** GRANDE2026
- **Autores, año y revista:** Sotero Grande E; Checa-Caratachea XA; Cruz-Hervert LP et al.. *Healthcare 14(12) (2026):1737*.
- **DOI / PMID / URL:** DOI `10.3390/healthcare14121737`; PMID `42354595`; [original](https://doi.org/10.3390/healthcare14121737).
- **Tipo de estudio:** Revisión narrativa con búsqueda estructurada (los autores la denominan «systematic narrative review»), **NO metaanálisis ni revisión con evaluación formal de riesgo de sesgo por estudio comprobada**.
- **Población y tamaño muestral:** 16 estudios incluidos tras cribado de 42 registros inicialmente localizados.
- **Definición diagnóstica y técnicas:** Búsquedas en PubMed, SciELO, Cochrane, Google Scholar y repositorios, período 2000–marzo de 2026. Incluye publicaciones en inglés y español; cribado inicial de 42 registros y selección de 16. Combina estudios observacionales con revisiones secundarias; el proceso de cribado y deduplicación no equivale a la selección duplicada de una revisión sistemática formal. Texto abierto en [PMC13299497](https://pmc.ncbi.nlm.nih.gov/articles/PMC13299497/).
- **Criterio diagnóstico de anquiloglosia:** NO APLICA: no se diagnostica ni clasifica anquiloglosia; se examinan otros fenómenos respiratorios, del sueño o craneofaciales.
- **Variables de resultado:** Características transversales de maxilar, paladar, patrón de crecimiento vertical, oclusión y cefalometría en niños con respiración bucal.
- **Resultados NUMÉRICOS verificados:** 42 registros iniciales; 16 trabajos incluidos. El resumen no aporta un tamaño de efecto metaanalítico.
- **Límites metodológicos / confusores:** Heterogeneidad de las definiciones de respiración bucal y desenlaces esqueléticos vs dentales; gran peso de estudios transversales; mezcla de revisiones secundarias y originales (riesgo de contar dos veces las mismas cohortes); **no consta evaluación formal individual del riesgo de sesgo o GRADE**. La literatura revisada no identifica por sí sola la dirección causal ni la reversibilidad tras intervenciones.
- **Hallazgos contrarios o no significativos:** La propia revisión reconoce que no puede confirmar una relación causa-efecto definitiva.
- **Conclusión que sí permite / que no permite:** Sirve de mapa de asociaciones y referencias para el scoping; no debe interpretarse como evidencia causal de que respirar por la boca provoque retrusión ósea o que terapia miofuncional revierta crecimiento.
- **Licencia y derechos:** Artículo abierto; síntesis original sin reproducción de figuras ni PDF.
- **Estado de lectura:** Texto original abierto y apartados de métodos/selección revisados el 03/11/2026 vía [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC13299497/); **no se han reexaminado los 16 estudios primarios individualmente** ni se ha realizado evaluación independiente de sus sesgos. Acceso abierto; licencia de las figuras debe verificarse antes de reutilizarlas.

## Figuras

No incorporadas ni auditadas. [Artículo original](https://doi.org/10.3390/healthcare14121737).

---

<!-- archivo: fuentes/articulos/2026-vaishnavi-respiracion-bucal-apnea.md -->
# Estudio: Association between mouth breathing and pediatric obstructive sleep apnea: a systematic review

- **ID:** VAISHNAVI2026
- **Autores, año y revista:** Vaishnavi P; Sushmita S; Vivek K et al.. *European Archives of Oto-Rhino-Laryngology 283 (2026):1215–1224*.
- **DOI / PMID / URL:** DOI `10.1007/s00405-025-09999-1`; PMID `41524934`; [original](https://doi.org/10.1007/s00405-025-09999-1).
- **Tipo de estudio:** Revisión sistemática; síntesis cualitativa.
- **Población y tamaño muestral:** 13 estudios incluidos (2 transversales y 11 cohortes), seleccionados de 3.722 registros.
- **Definición diagnóstica y técnicas:** Búsqueda en MEDLINE, Embase, Scopus, LILACS, Web of Science, Cochrane y OVID hasta septiembre de 2025; métodos variables para clasificar respiración oral y apnea.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA: no se diagnostica ni clasifica anquiloglosia; se examinan otros fenómenos respiratorios, del sueño o craneofaciales.
- **Variables de resultado:** Asociación entre respiración bucal y gravedad de apnea infantil; apnea residual después de adenoamigdalectomía.
- **Resultados NUMÉRICOS verificados:** 13 estudios, sin estimación agrupada del efecto en el resumen; **no inventar OR**.
- **Límites metodológicos / confusores:** Heterogeneidad diagnóstica y de poblaciones; la respiración oral puede ser marcador, resultado o contribuyente; no mide por sí misma efecto causal sobre crecimiento ni eficacia de corregir postura lingual.
- **Hallazgos contrarios o no significativos:** El resumen indica que algunos resultados fueron inconsistentes por diferencias en métodos diagnósticos.
- **Conclusión que sí permite / que no permite:** La respiración bucal puede ayudar a identificar niños que merecen evaluación de SDB; por sí sola no diagnostica apnea ni demuestra su causa.
- **Licencia y derechos:** Derechos del editor; síntesis original sin PDF ni figuras reproducidas.
- **Estado de lectura:** Resumen PubMed revisado el 03/11/2026; texto completo pendiente.

## Figuras

No incorporadas ni auditadas. [Artículo original](https://doi.org/10.1007/s00405-025-09999-1).

---

<!-- archivo: fuentes/articulos/2026-valadares-criterios-indicacion.md -->
# Estudio: Tools and Criteria Used to Indicate Frenotomy/Frenectomy in Infants With Ankyloglossia: A Scoping Review

- **ID:** VALADARES2026
- **Autores, año y revista:** Valadares MG; Araújo KMS; Martins IM; De Luca MP; Corrêa-Faria P. J Hum Lact 2026 (en línea antes de impresión).
- **DOI / PMID / URL:** DOI `10.1177/08903344261460203`; PMID `42478562`.
- **Tipo de estudio:** Revisión de alcance.
- **Población y tamaño muestral:** 53 estudios con lactantes menores de 23 meses operados.
- **Definición diagnóstica y técnicas:** PubMed, Embase, Central, LILACS, Scopus y ProQuest.
- **Criterio diagnóstico de anquiloglosia:** MIXTO: es justo lo que estudia. Herramientas usadas para decidir la cirugía: Coryllos (17 estudios, aspecto), Hazelbaker (12), Bristol (3) y protocolo de Martinelli/Teste da Linguinha (4). Otros usaban criterios clínicos y quejas de lactancia.
- **Variables de resultado:** Herramientas y criterios de indicación quirúrgica.
- **Resultados NUMÉRICOS verificados:** Gran heterogeneidad en la herramienta elegida, los puntos de corte y la interpretación de los hallazgos.
- **Límites metodológicos / confusores:** Revisión de alcance: describe, no evalúa calidad.
- **Hallazgos contrarios o no significativos:** No aplica.
- **Conclusión que sí permite / que no permite:** Sí: Decir que no hay criterios estandarizados para indicar la frenotomía en lactantes y que la escala más usada es de aspecto (Coryllos). No: Valorar la eficacia de la cirugía.
- **Licencia y derechos:** Derechos de la revista. Aquí solo resumen propio.
- **Estado de lectura:** Resumen de PubMed revisado el 02/11/2026. Búsqueda de actualización del 02/11/2026.

## Figuras

Figuras no revisadas.

---

<!-- archivo: fuentes/articulos/2026-venugopal-apnea-revision.md -->
# Estudio: Is Ankyloglossia Correlated With Pediatric Sleep Disordered Breathing? A Systematic Review

- **ID:** VENUGOPAL2026
- **Autores, año y revista:** Venugopal N; Neposlan J; Bysice A; Khoury S; Madou E; Lee R; Strychowsky JE; St-Laurent A; Lawlor CM; Graham ME. Laryngoscope 2026;136(3):1088-1098.
- **DOI / PMID / URL:** DOI `10.1002/lary.70134`; PMID `40960120`; PMC12913740. Cartas sobre ella: PMID 41307177 y 41307155.
- **Tipo de estudio:** Revisión sistemática.
- **Población y tamaño muestral:** 8 estudios, 1.171 niños no sindrómicos de 0 a 18 años.
- **Definición diagnóstica y técnicas:** Seis bases de datos hasta el 13/02/2025.
- **Criterio diagnóstico de anquiloglosia:** MIXTO. Señala la falta de criterios diagnósticos estandarizados de anquiloglosia como límite y pide medidas funcionales estandarizadas.
- **Variables de resultado:** Trastorno respiratorio del sueño; frenotomía como tratamiento.
- **Resultados NUMÉRICOS verificados:** Evidencia mixta de relación. Datos insuficientes para indicar frenotomía por trastorno respiratorio del sueño; dos estudios de intervención positivos con validez limitada.
- **Límites metodológicos / confusores:** Cuestionarios en lugar de pruebas validadas de sueño.
- **Hallazgos contrarios o no significativos:** No aplica.
- **Conclusión que sí permite / que no permite:** Sí: Decir que la relación entre anquiloglosia y apnea infantil no está clara. No: Decir que está demostrado que no existe.
- **Licencia y derechos:** Acceso abierto (PMC). Aquí solo resumen propio.
- **Estado de lectura:** Resumen de PubMed revisado el 02/11/2026. Búsqueda de actualización del 02/11/2026.

## Figuras

Figuras no revisadas. [Ver el documento](https://pmc.ncbi.nlm.nih.gov/articles/PMC12913740/).

---

<!-- archivo: fuentes/articulos/2026-ye-fuerza-lingual-postura-clase-esqueletica.md -->
# Estudio: Tongue muscle strength and resting posture across sagittal skeletal patterns in adolescents: a cross-sectional study using mediation analysis and decision tree

- **ID:** YE2026TONGUE
- **Autores, año y revista:** Ye J; Guo Y; Sun Q; Teng J; Wang L; Ma Y. *BMC Oral Health* 2026;26:1432, publicado el 22/06/2026 (versión definitiva 13/08/2026).
- **DOI / PMID / URL:** DOI `10.1186/s12903-026-08935-x`; PMID `42324535`; PMCID `PMC13474726`; [texto completo abierto](https://pmc.ncbi.nlm.nih.gov/articles/PMC13474726/).
- **Tipo de estudio:** Estudio **transversal** de adolescentes en primera evaluación ortodóncica; comparaciones entre clases esqueléticas, regresión multivariable, **modelo estadístico de mediación** y árbol de clasificación CHAID.
- **Población y tamaño muestral:** **182 adolescentes de 11–17 años**, clase I **77**, clase II **53**, clase III **52**; edades similares entre grupos. **Excluyeron respiración bucal predominante, deglución atípica**, hábitos orales perjudiciales, cirugía lingual previa, tratamiento miofuncional/ortodóncico, adenoidectomía o amigdalectomía previas, entre otros.
- **Definición diagnóstica y técnicas:** Grupo esquelético por **ANB** y relación molar. **MTP** = fuerza máxima activa de presión/elevación lingual con dinamómetro (kg, tres medidas separadas por 30 s). **TTI** = posición **sagital** de la punta: distancia entre espina nasal anterior (ANS) y proyección de punta lingual / longitud palatina ANS–PNS; **TTD** = distancia vertical punta–paladar; **TDD** = distancia vertical dorso–paladar; las tres en telerradiografía lateral con postura protocolizada. **TTI NO es TRMR ni una prueba de succión/presión**. Relectura de 20 radiografías a cuatro semanas, **ICC >0,85** en medidas lineales/angulares.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA: el estudio **no diagnosticó anquiloglosia** ni midió longitud de frenillo o TRMR. Estudió **presión muscular y posición de lengua**.
- **Variables de resultado:** Fuerza MTP, índice posicional TTI, TTD, TDD, ANB, inclinaciones de incisivos, modelo estadístico y árbol de clasificación de clase III.
- **Resultados NUMÉRICOS verificados (tablas 2–4 y texto):**
  - **MTP mediana** clase I **2,21 kg**, clase II **2,20 kg**, clase III **1,65 kg**; p<0,001.
  - **TTI mediana:** clase I **15,70 %**, II **15,26 %**, III **8,94 %**; p<0,001. **TDD mediana:** 3,96 / 4,27 / **8,83 mm**; p<0,001.
  - **Correlaciones:** ANB con MTP **r=0,30**; con TTI **r=0,38**; MTP con TDD **r=−0,63** y TTI **r=0,45** (p<0,001 en las destacadas).
  - **Regresión ajustada** por inclinaciones dentarias: ANB asociado a MTP **B=1,567; p=0,001** y TTI **B=0,078; p=0,004**. TDD (p=0,160) y TTD (p=0,174) no fueron significativos en ese modelo. Modelo completo **R² ajustado 0,549**, donde las inclinaciones dentarias fueron predictores principales.
  - **Mediación estadística MTP → TTI → ANB:** efecto indirecto **B=0,596** (IC95 % **0,227–0,986**), **32,4 %** de la asociación total. Es una **descomposición estadística de datos transversales**, no una secuencia temporal observada.
  - **CHAID interno:** umbral MTP **≤1,85 kg**; entre ellos, TTI **≤2,57 %** identificó un nodo con **84,6 % clase III** en la propia muestra. Los umbrales son **exploratorios/internos**, no puntos de corte clínicamente validados en otra cohorte.
- **Aportación del estudio:** Una publicación que **mide simultáneamente fuerza lingual, posición de la punta y morfología esquelética** en adolescentes. Conecta tres variables que otras revisiones estudian por separado y ofrece una pregunta contrastable: ¿cómo se relacionan a lo largo del crecimiento la fuerza, la posición habitual y las bases esqueléticas?
- **Límites metodológicos / confusores (decisivos):** Diseño transversal; el modelo de mediación no establece orden causal. Muestreo de consulta ortodóncica, no población comunitaria; excluyó precisamente hábitos/respiración bucal y deglución atípica. No realizó exploración del frenillo ni midió sueño.
- **Licencia y derechos:** Original **CC BY 4.0** (Springer/BMC). Ficha original sin copia de tablas o imágenes.
- **Estado de lectura:** **Texto completo HTML abierto examinado el 04/11/2026**, incluidos población/exclusiones, protocolo de medición y tablas 2, 3 y 4. No se han reanalizado radiografías ni validado el modelo en otra muestra.

## Figuras

Original [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC13474726/): figuras de medidas cefalométricas y árbol CHAID, no copiadas.

---

<!-- archivo: fuentes/articulos/sd-fernandez-sanchez-analisis-wits.md -->
# Estudio: Análisis de Wits

- **ID:** FERNANDEZSANCHEZ_WITS
- **Autores, año y revista:** Fernández Sánchez J. Revista y año PENDIENTE DE VERIFICAR.
- **DOI / PMID / URL:** sin DOI
- **Tipo de estudio:** Artículo docente de cefalometría.
- **Población y tamaño muestral:** No aplica.
- **Definición diagnóstica y técnicas:** Análisis de Wits frente al ANB de Steiner.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA: el estudio no diagnostica anquiloglosia.
- **Variables de resultado:** No aplica.
- **Resultados NUMÉRICOS verificados:** No aplica.
- **Límites metodológicos / confusores:** Material docente.
- **Hallazgos contrarios o no significativos:** No aplica.
- **Conclusión que sí permite / que no permite:** Sí: Consultar el método de Wits. No: Citarlo como estudio.
- **Licencia y derechos:** Derechos del editor. Aquí solo metadatos y resumen propio.
- **Estado de lectura:** texto completo revisado el 17/10/2026; sin DOI ni PMID.

## Figuras

Las leyendas de las figuras no se han podido extraer del texto completo: `PENDIENTE DE VERIFICAR`. Sin enlace público.

---

<!-- archivo: fuentes/articulos/sd-sumario-analisis-cefalometrico.md -->
# Estudio: Sumario del análisis cefalométrico (capítulo 7 de un manual)

- **ID:** SUMARIO_CEFALOMETRICO
- **Autores, año y revista:** PENDIENTE DE VERIFICAR. Libro PENDIENTE DE VERIFICAR.
- **DOI / PMID / URL:** sin DOI
- **Tipo de estudio:** Capítulo docente.
- **Población y tamaño muestral:** No aplica.
- **Definición diagnóstica y técnicas:** Resumen de medidas cefalométricas con pronóstico favorable, regular o deficiente.
- **Criterio diagnóstico de anquiloglosia:** NO APLICA: el estudio no diagnostica anquiloglosia.
- **Variables de resultado:** No aplica.
- **Resultados NUMÉRICOS verificados:** No aplica.
- **Límites metodológicos / confusores:** Material docente sin referencia completa.
- **Hallazgos contrarios o no significativos:** No aplica.
- **Conclusión que sí permite / que no permite:** Sí: Consulta interna. No: Citarlo.
- **Licencia y derechos:** Derechos del editor. Aquí solo metadatos y resumen propio.
- **Estado de lectura:** texto completo revisado el 17/10/2026.

## Figuras

Las leyendas de las figuras no se han podido extraer del texto completo: `PENDIENTE DE VERIFICAR`. Sin enlace público.
