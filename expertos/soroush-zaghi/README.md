# Soroush Zaghi: sus ideas públicas, con su vídeo

Soroush Zaghi es otorrinolaringólogo y cirujano de sueño y vía aérea, fundador de The Breathe Institute (Los Ángeles). Es coautor de las escalas de movilidad lingual TRMR que usa esta biblioteca ([Yoon 2017](../../fuentes/articulos/2017-yoon-trmr-1052.md), [Zaghi 2021](../../fuentes/articulos/2021-zaghi-trmr-lps.md)).

**Qué es esta carpeta.** Una reconstrucción de lo que Zaghi dice en público, sobre todo en sus vídeos de YouTube. Cada afirmación lleva el vídeo del que sale, con enlace. **No es Zaghi hablando, no habla en su nombre y no es una guía clínica.** Lo que dice un experto en un vídeo es opinión de experto: no equivale a un estudio (ver [AGENTS.md](../../AGENTS.md), regla 2).

## De dónde sale

1. Se cargaron 100 fuentes públicas de The Breathe Institute (99 vídeos y su web) en un cuaderno de NotebookLM, en agosto y septiembre de 2026.
2. Se le hicieron preguntas por temas y se pasó cada respuesta a una base de afirmaciones, una por línea, con su tipo, su vídeo, su año y su PMID si cita un estudio.
3. Cada estudio citado se buscó en PubMed. Resultado en [estudios-citados.md](estudios-citados.md). Los casos en que lo que dice Zaghi no cuadra con el artículo están en [discrepancias.md](discrepancias.md).
4. Para esta versión pública se quitaron: testimonios y casos de pacientes (también los de su propia familia), vídeos de rutinas personales del equipo, tutoriales de gestión, y todo lo que habla de fármacos, anestesia o dosis. No hay transcripciones: solo resúmenes propios y citas cortas.

## Cómo leer cada entrada

- **Tipo:** `Estudio citado` (Zaghi cita un trabajo), `Experiencia clínica` (lo que hace o ve en consulta) u `Opinión`.
- **Estado:** `verificado en PubMed` (el estudio existe y la cifra cuadra con el resumen), `sin verificar (dicho en vídeo)` o `discrepante`. Casi todo está sin verificar: es lo que dice en vídeo.
- **Vídeo:** título y enlace. Cuando la extracción no guardó el vídeo, pone `PENDIENTE DE VERIFICAR`.
- **Minuto:** en 15 entradas se localizó en los subtítulos automáticos de YouTube, buscando la cita literal (puede variar unos segundos). En el resto pone `PENDIENTE DE VERIFICAR`. Para encontrarlo: abrir el vídeo, pulsar «Mostrar transcripción» y buscar una palabra clave en inglés.
- **Cita corta:** cuando la hay, sale de la transcripción automática y puede tener errores de reconocimiento (por ejemplo «Lchnowski» por Lichnowska).
- Lo que dicen otras personas que aparecen en los vídeos (Coppelson, Sandraluz Gonzalez, Katie Romero) se atribuye a ellas, no a Zaghi.

## Archivos

- [respuestas-a-criticas.md](respuestas-a-criticas.md): qué dice Zaghi ante las críticas más habituales, al lado de lo que dice la evidencia de esta biblioteca. **Empieza por aquí.**
- Por temas: [anquiloglosia](anquiloglosia.md), [frenuloplastia](frenuloplastia.md), [posoperatorio](posoperatorio.md), [terapia miofuncional](miofuncional.md), [reglas de decisión](reglas-decision.md), [lo que rechaza](doctrina-negativa.md), [contradicciones y cambios de postura](contradicciones.md), [investigación y ética](investigacion-etica.md), [marcos de razonamiento](frameworks.md), [fascia](fascia.md), [desarrollo maxilofacial](maxilofacial.md), [sueño y apnea](sueno-apnea.md), [nariz y amígdalas](nariz-amigdalas.md), [hipermovilidad](hipermovilidad.md), [ambiente y alergias](ambiente-moho-alergias.md), [otros temas](temas-poco-cubiertos.md).
- [zaghi.jsonl](zaghi.jsonl): las mismas afirmaciones en formato de datos, una por línea, para que una IA las lea.
- [estudios-citados.md](estudios-citados.md), [discrepancias.md](discrepancias.md) y [referencias-de-zaghi.md](referencias-de-zaghi.md) (bibliografía de 14 artículos suyos de acceso abierto).
- [fuentes-videos.md](fuentes-videos.md): los vídeos citados, con su enlace.

## Cómo razona Zaghi (síntesis propia)

1. **Forma y función se condicionan.** Busca la causa (anatomía, tono, espacio, hábitos, ambiente) antes de operar. Cortar el frenillo es solo un paso.
2. **Lengua arriba, labios sellados, respiración nasal** es el objetivo funcional. Sostiene que una lengua restringida puede ir con paladar estrecho, nariz obstruida y peor vía aérea. Es su modelo; la causalidad no está demostrada (ver [O-002](../../objeciones/anquiloglosia-maloclusion.md)).
3. **Atadura, tono y espacio**, y desde 2024 la hipermovilidad como cuarta variable. Antes de liberar comprueba que haya sitio para la lengua.
4. **Mide, no solo mira.** Valora el frenillo en cinco dimensiones: longitud de lengua libre, movilidad de la punta (TRMR-TIP), succión palatina (TRMR-LPS), compensaciones y tensión al tacto. En consulta hoy prioriza la maniobra de sujetar el suelo de la boca y reserva el TRMR sobre todo para investigación ([contradicciones](contradicciones.md), zag-0569 y zag-0623).
5. **Cirugía mínima y rehabilitación.** Terapia miofuncional antes y después. Técnica que conserva la fascia y cierre con sutura.
6. **Epistemología.** Repite que la ausencia de evidencia no es evidencia de ausencia y señala sesgos de medición, de publicación y de confirmación. Sus resultados son a menudo serie propia sin publicar.
7. **Equipo.** Trabaja con terapeutas miofuncionales, ortodoncistas, cirujanos maxilofaciales, otorrinos, fisioterapeutas y especialistas en sueño, y deriva según la causa principal.

## Límites

- Casi todas las afirmaciones están sin verificar: son lo que Zaghi dice en vídeo.
- La transcripción automática y NotebookLM introducen errores. De 16 discrepancias revisadas, 1 era un exceso de Zaghi y 10 eran errores de NotebookLM o de la transcripción ([discrepancias.md](discrepancias.md)).
- Hay temas con poca cobertura. Si algo no está aquí, no se le puede atribuir una postura a Zaghi.
- Zaghi tiene interés profesional en la frenuloplastia, la formación de clínicos y los instrumentos que diseña. Es coautor de varios estudios que cita. Conviene tenerlo en cuenta al leerle, igual que con cualquier experto.
