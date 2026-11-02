# Discrepancias entre lo que dice Zaghi y lo que dicen los estudios

**Qué es:** los 16 registros de la base original de la extracción (aquí, [zaghi.jsonl](zaghi.jsonl) con los registros publicables) que salieron `discrepante` al contrastarlos con PubMed, agrupados por afirmación. Para cada uno: qué dijo Zaghi (cita literal, vídeo y año si el título lo tiene) y qué dice el estudio (PMID y frase del resumen o del texto completo). La cita de Zaghi sale de una pregunta a NotebookLM que pedía la transcripción literal (q60-q65); las transcripciones son automáticas y traen errores de reconocimiento (por ejemplo "Lchnowski", "Yun", "Feres").

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
