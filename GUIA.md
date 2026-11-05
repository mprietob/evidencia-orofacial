# Guía: cómo consultar esta biblioteca con una IA

Esta guía también está, más cómoda de leer, en [recursos.inimamed.com/evidencia](https://recursos.inimamed.com/evidencia).

No hace falta saber nada de GitHub. Necesitas una IA: NotebookLM, ChatGPT, Claude o Gemini. **El repositorio sigue privado**: esta guía describe el acceso para quienes tienen permisos y cómo se podrá utilizar cuando se publique. No debe darse por disponible hoy para cualquier visitante.

## 1. Mirarla sin más (sin cuenta)

**Cuando el repositorio se haga público**, podrá verse sin cuenta. Las fichas están en la carpeta `fuentes/articulos`, el índice por temas en `llms.txt` y la portada en el README.

## 2. Preguntarle a una IA subiendo un solo archivo (gratis)

1. Abre [biblioteca-completa.md](biblioteca-completa.md). Arriba a la derecha hay un botón para descargarlo («Download raw file», una flecha hacia abajo).
2. Súbelo a tu IA:
   - **NotebookLM** (gratis, de Google) es la mejor opción para este archivo, porque es grande: crea un cuaderno y pulsa «Añadir fuente».
   - **ChatGPT** o **Gemini:** el clip o el «+» del chat.
   - **Claude:** puede decirte que el archivo no cabe en una conversación. Si pasa, usa NotebookLM.
3. Pega esto antes de tu pregunta:

> Responde solo con la información de este archivo y sigue sus reglas. No te limites a decir si hay o no hay evidencia: analiza cada artículo. Mira con qué criterio diagnosticó la anquiloglosia (aspecto o función), si una revisión mezcla estudios con criterios distintos, si el estudio llegó a tener en cuenta la anquiloglosia si hay cirugía, qué técnica se usó y si la liberación fue efectiva, y, si mide la vía aérea antes y después de algo, si controló la postura de la cabeza y el cuello. Cita la ficha y el estudio (año y DOI o PMID). Si algo no está en el archivo, dilo en vez de inventarlo.

4. Pregunta lo que quieras. Por ejemplo: «¿Qué estudios relacionan el frenillo con la apnea en adultos, y qué límites tienen?».

**El archivo es una foto del día en que lo descargas.** Si se añaden estudios, vuelve a descargarlo.

## 3. Conectar la IA al repositorio

Así la IA lee siempre la versión al día. Las opciones cambian a menudo y dependen del plan de cada IA. Si no te aparecen, usa la forma 2, que siempre funciona.

- **Pegar el enlace** del repositorio en un chat con búsqueda web y pedirle que lea `llms.txt` y las fichas. No siempre consigue leerlas todas.
- **Conector de GitHub** en ChatGPT o Claude. Según lo que hemos encontrado, en ChatGPT está en los planes de pago; en la cuenta gratuita la opción aparece pero no se puede usar.
- **GitMCP**, gratuito, para repositorios públicos: `https://gitmcp.io/mprietob/evidencia-orofacial`. En Claude se añade como conector personalizado.

Más formas, también para IA de terminal, en el apartado «Cómo preguntarle con tu propia IA» del [README](README.md).

## Cómo crearte una cuenta de GitHub (para aportar)

Solo hace falta si quieres proponer un artículo por GitHub. Si no, escribe por Instagram a @dermaprieto.

1. Entra en github.com y pulsa **Sign up**.
2. Escribe tu correo, una contraseña y un nombre de usuario.
3. Te llega un código al correo: cópialo. Ya está, es gratis.
4. Vuelve a este repositorio, entra en **Issues**, pulsa **New issue** y elige **Proponer un artículo**. Rellena los campos y envía.

Aunque la IA cite bien, revisa la ficha original y el artículo. Las IA se equivocan.
