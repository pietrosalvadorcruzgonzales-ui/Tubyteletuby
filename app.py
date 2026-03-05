import streamlit as st
# 1. EL ARCHIVADOR (Nuestra base de datos de preguntas)
# Cada bloque entre { } es una pregunta distinta. Cada pregunta es un diccionario de 3 entradas (texto, opciones, correcta).
# Creamos la lista de preguntas:
preguntas = [
    {
        "texto": "¿Cuál es el lenguaje de programación que estamos usando?",
        "opciones": ["Java", "Python", "C++", "JavaScript"],
        "correcta": "Python"
    },
    {
        "texto": "¿Qué comando se usa para ejecutar una app de Streamlit?",
        "opciones": ["python run", "streamlit run", "start streamlit"],
        "correcta": "streamlit run"
    },
    {
        "texto": "¿En qué año se lanzó la Web 1.0?",
        "opciones": ["1983", "1990", "2005"],
        "correcta": "1990"
    },
    {
        "texto": "¿En qué año comenzó la Revolución Francesa?",
        "opciones":["1789", "1776", "1804", "1812"],
        "correcta": "1789"
    },
    {
        "texto": "¿Cuál era el grupo social que pagaba más impuestos antes de la Revolución?",
        "opciones": ["La nobleza", "El clero", "El tercer estado", "La monarquia"],
        "correcta": "El tercer estado"
    },
    {   "texto":"¿En qué año comenzó la Segunda Guerra Mundial?",
        "opciones":["1914", "1939", "1945", "1929"],
        "correcta":"1939"
    },
    {   "texto":"¿Cuál es el planeta más grande del sistema solar?",
        "opciones":["Tierra", "Marte", "Jupiter", "Saturno"],
        "correcta":"Jupiter"
    },
    {   "texto":"¿Cuál es la capital de Australia?",
        "opciones":["Sidney", "Melbourne", "Camberra", "Brisbane"],
        "correcta":"Camberra"
    },
    {   "texto":"¿Quién escribió Cien años de soledad?",
        "opciones":["Gabriel Garcia Marquez", "Mario Vargas Llosa", "Pablo Neruda", "Julio Cortazar"],
        "correcta":"Gabriel Garcia Marquez"
    }
     ]

# Configuración visual de la página
st.title("🎓 Mi Primer Examen Interactivo")
st.write("Responde a las preguntas y pulsa el botón al final para saber tu nota.")
tab1, tab2 = st.tabs(["Examen", "Informe"])
# 2. EL FORMULARIO (Agrupamos todo para que no se recargue la web a cada clic)
# Eso se consigue con el comando with
   
with tab1:
  with st.form("quiz_form"):
    # Aquí guardaremos las respuestas que elija el alumno. Será una lista.
    respuestas_usuario = []
   
    # Recorremos el archivador usando un bucle 'for' para crear las preguntas
    for pregunta in preguntas:
        st.subheader(pregunta["texto"]) # Ponemos el texto de la pregunta

        # Creamos los botones de opción (radio)
        eleccion = st.radio("Elige una opción:", ["----"] + pregunta["opciones"], key=pregunta["texto"])

        # Guardamos la elección en nuestra lista usando append ()
        respuestas_usuario.append(eleccion)
        st.write("---") # Una línea para separar preguntas

    # Botón obligatorio para cerrar el formulario
    boton_enviar = st.form_submit_button("Entregar Examen")

# 3. LA CORRECCIÓN (Solo ocurre cuando pulsamos el botón)
if boton_enviar:
    aciertos = 0
    total = len(preguntas)

    for i in range(total):

        if respuestas_usuario[i] == "----":
            pass  

        elif respuestas_usuario[i] == preguntas[i]["correcta"]:
            aciertos += 1  

        else:
            aciertos -= 1  

    if aciertos < 0:
        aciertos = 0

    nota = round((aciertos / total) * 10, 2)

    # Mostramos el resultado con colores
    st.divider()
    st.header(f"Resultado final: {nota} / 10")

    if nota < 2:
        st.error(f"Muy insuficiente. Has suspendido con {aciertos} aciertos.")
    elif 3 <= nota <5:
        st.error(f"Has sacado un {nota}. ¡Insuficiente!")
    elif 5 <= nota <6:
        st.success(f"Suficiente. Has aprobado con {aciertos} aciertos.")
        st.balloons() # ¡Efecto de globos!
    elif 6 <= nota <7:
        st.success(f"Bien. Has aprobado con {aciertos} aciertos.")
        st.balloons() # ¡Efecto de globos!
    elif 7 <= nota <9:
        st.success(f"Notable. Has aprobado con {aciertos} aciertos.")
        st.balloons() # ¡Efecto de globos!
    elif 9 <= nota < 10:
        st.success(f"Sobresaliente. Has aprobado con {aciertos} aciertos.")
        st.balloons() # ¡Efecto de globos!
    elif nota==10:
        st.success(f"Excelente. Has aprobado con {aciertos} aciertos.")
        st.balloons() # ¡Efecto de globos!
   
    with tab2:
   
     st.markdown("Informe del examen")

    for i in range(total):

        if respuestas_usuario[i] == preguntas[i]["correcta"]:
            st.markdown(f"✅ {preguntas[i]['texto']}")
            st.markdown(f"Tu respuesta: {respuestas_usuario[i]}")

        else:
            st.markdown(f"❌ {preguntas[i]['texto']}")
            st.markdown(f"Tu respuesta: {respuestas_usuario[i]}")
            st.markdown(f"Respuesta correcta: {preguntas[i]['correcta']}")

        st.markdown("---")
