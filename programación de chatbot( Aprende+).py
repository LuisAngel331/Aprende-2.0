import random
print("Hola, soy Aprende+ 🤖. Puedo ayudarte con matemáticas o comprensión lectora.")
print("Escribe 'salir' para terminar.\n")

temario = {
    "ley de exponentes": {
        "concepto": "Las leyes de los exponentes permiten simplificar operaciones con potencias que tienen la misma base. Ejemplo: a^m * a^n = a^(m+n)",
        "video": "https://www.youtube.com/live/ywOZDIeLmZ0?si=NuB0rKOM--bw2enM",
        "ejercicios": [
            {"pregunta": "2^3 * 2^4", "respuesta": "128"},
            {"pregunta": "5^7 / 5^2", "respuesta": "15625"},
            {"pregunta": "(3^2)^4", "respuesta": "6561"},
            {"pregunta": "(x^5)*(x^3)", "respuesta": "x^8"},
            {"pregunta": "(y^8)/(y^3)", "respuesta": "y^5"}
        ]
    },

    "planteo de ecuaciones": {
        "concepto": "Plantear ecuaciones significa traducir un problema verbal a una expresión algebraica donde se desconoce un valor.",
        "video": "https://www.youtube.com/live/veBhc1BUxds?si=iUfB7oL6ibLoEQym",
        "ejercicios": [
            {"pregunta": "Si el doble de un número es 14, ¿cuál es el número?", "respuesta": "7"},
            {"pregunta": "x + 7 = 20, encuentra x", "respuesta": "13"},
            {"pregunta": "3x - 5 = 10, encuentra x", "respuesta": "5"},
            {"pregunta": "Encuentra el número que sumado con 12 da 25", "respuesta": "13"},
            {"pregunta": "4x = 28, encuentra x", "respuesta": "7"}
        ]
    },

    "funciones lineales": {
        "concepto": "Una función lineal tiene la forma f(x) = mx + b, donde m es la pendiente y b es la ordenada al origen.",
        "video": "https://youtu.be/tZ8AYOOB9G4?si=HlopGDgUeONc96d9",
        "ejercicios": [
            {"pregunta":"Identifica la pendiente y la ordenada en f(x) = 3x + 2", "respuesta": "pendiente=3, ordenada=2"},
            {"pregunta":"Calcula f(4) si f(x) = 2x - 5", "respuesta": "3"},
            {"pregunta": "Halla la ecuación de la recta con pendiente 4 y que pasa por (0,3).", "respuesta": "y=4x+3"},
            {"pregunta": "Representa gráficamente f(x) = -2x + 1", "respuesta": "abierta"},
            {"pregunta": "Encuentra f(-3) si f(x) = 5x + 7", "respuesta": "-8"},
            {"pregunta": "Si f(x) = 2x + 1, encuentra x cuando f(x) = 7.", "respuesta": "3"},
            {"pregunta": "Halla la intersección con el eje X de f(x) = 3x - 6", "respuesta": "x=2"},
            {"pregunta": "Una recta pasa por (0,2) y (3,5). Encuentra su ecuación.", "respuesta": "y=x+2"},
            {"pregunta": "¿Cuál es la pendiente de f(x) = -7x + 9?", "respuesta": "-7"},
            {"pregunta":"Grafica f(x) = x/2 + 4", "respuesta": "abierta"}
        ]
    },

    "problemas con fracciones": {
        "concepto": "Los problemas con fracciones implican sumar, restar, multiplicar o dividir números fraccionarios.",
        "video": "https://youtu.be/ZBMUyM_dsx8?si=QH4MbCfTrjiJ64yL",
        "ejercicios": [
            {"pregunta": "Simplifica: 3/4 + 2/4", "respuesta": "5/4"},
            {"pregunta": "Resuelve: 5/6 - 1/3", "respuesta": "1/2"},
            {"pregunta": "Multiplica: 2/5 * 3/7", "respuesta": "6/35"},
            {"pregunta": "Divide: (4/9) ÷ (2/3)", "respuesta": "2/3"},
            {"pregunta": "Simplifica: 7/8 + 5/16", "respuesta": "19/16"},
            {"pregunta": "Resta: 11/12 - 7/24", "respuesta": "7/24"},
            {"pregunta": "Multiplica: 3/10 * 5/6", "respuesta": "1/4"},
            {"pregunta": "Divide: (9/14) ÷ (3/7)", "respuesta": "3/2"},
            {"pregunta": "Suma: 2/3 + 5/9", "respuesta": "11/9"},
            {"pregunta": "Resuelve: 1/2 + 2/3 - 3/4", "respuesta": "5/12"}
        ]
    },

    "sucesiones numéricas": {
        "concepto": "Una sucesión numérica es una lista de números ordenados según una regla. Ejemplo: sucesión aritmética o geométrica.",
        "video": [
            "https://youtu.be/lXEe11Sfwgo?si=LT6ZlkyN8lsXpGSe",
            "https://youtu.be/bI99PoaU6P8?si=PPKweFPthS34JLdc"
        ],
        "ejercicios": [
            {"pregunta": "Encuentra el término 6 de la sucesión: 2, 4, 6, 8...", "respuesta": "12"},
            {"pregunta": "Encuentra el término 8 de la sucesión: 3, 6, 12, 24...", "respuesta": "192"},
            {"pregunta": "Halla la diferencia común de la sucesión: 5, 8, 11, 14...", "respuesta": "3"},
            {"pregunta": "Encuentra el término 10 de la sucesión: 7, 10, 13, 16...", "respuesta": "34"},
            {"pregunta": "Halla la razón de la sucesión: 2, 6, 18, 54...", "respuesta": "3"},
            {"pregunta": "Determina el término general de 4, 8, 12, 16...", "respuesta": "4n"},
            {"pregunta": "Encuentra a_5 si a_n = 3n + 1", "respuesta": "16"},
            {"pregunta": "Encuentra a_7 si a_n = 2^n", "respuesta": "128"},
            {"pregunta": "Encuentra el término 12 de la sucesión: 1, 4, 7, 10...", "respuesta": "34"},
            {"pregunta": "Identifica si la sucesión 10, 5, 2.5, 1.25 es aritmética o geométrica.", "respuesta": "geométrica"}
        ]
    },

    "series numéricas": {
        "concepto": "Una serie es la suma de los términos de una sucesión.",
        "video": "https://youtu.be/aluH5-CitVU?si=x8293OVzSaPLfJmh",
        "ejercicios": [
            {"pregunta": "Suma los primeros 5 términos de 2, 4, 6, 8...", "respuesta":"30"},
            {"pregunta": "Suma los primeros 6 términos de 3, 6, 12, 24...", "respuesta":"189"},
            {"pregunta": "Calcula S_10 de una progresión aritmética con a1=2 y d=3.", "respuesta":"155"},
            {"pregunta": "Calcula S_5 de una progresión geométrica con a1=1 y r=2.", "respuesta":"31"},
            {"pregunta": "Suma los primeros 8 términos de 7, 10, 13, 16...", "respuesta":"140"},
            {"pregunta": "Suma los primeros 4 términos de 5, 15, 45, 135...", "respuesta":"200"},
            {"pregunta": "Calcula la suma de 1 + 2 + 3 + ... + 10", "respuesta":"55"},
            {"pregunta": "Suma los primeros 12 términos de la sucesión 4, 8, 12...", "respuesta":"312"},
            {"pregunta": "Calcula la suma de la serie 2 + 6 + 18 + ... hasta 5 términos.", "respuesta":"242"},
            {"pregunta": "Calcula S_20 de una progresión aritmética con a1=5 y d=2.", "respuesta":"480"}
        ]
    },

    "simetría, reflexiones, traslaciones y rotaciones": {
        "concepto": "Transformaciones geométricas que cambian la posición u orientación de una figura.",
        "video": "https://youtu.be/P2YVbu1OeN4?si=JVv4vyTrsgiEwjUV",
        "ejercicios": [
            {"pregunta": "Dibuja un triángulo y su simetría respecto al eje Y.", "respuesta": "abierta"},
            {"pregunta":"Traslada un punto (2,3) dos unidades a la derecha.", "respuesta": "4,3"},
            {"pregunta": "Rota el punto (1,0) 90° alrededor del origen.", "respuesta": "0,1"},
            {"pregunta": "Refleja el punto (4, -2) sobre el eje X.", "respuesta": "4,2"},
            {"pregunta": "Traslada el punto (-1,5) tres unidades abajo.", "respuesta": "-1,2"},
            {"pregunta": "Rota (0,2) 180° alrededor del origen.", "respuesta": "0,-2"},
            {"pregunta": "Aplica simetría al cuadrado de vértices (0,0),(2,0),(2,2),(0,2).", "respuesta": "abierta"},
            {"pregunta": "Traslada el triángulo con vértices (0,0),(1,0),(0,1) dos unidades a la izquierda.", "respuesta": "abierta"},
            {"pregunta": "Rota (3,3) 270° alrededor del origen.", "respuesta": "3,-3"},
            {"pregunta": "Refleja (5,1) sobre la recta y=x.", "respuesta": "1,5"}
        ]
    },

    "razones y proporciones": {
        "concepto": "Una razón es el cociente entre dos cantidades. Una proporción es la igualdad entre dos razones.",
        "video": "https://youtu.be/Jz-GPF9iHo8?si=Ueh0_21yUB7n2nON",
        "ejercicios": [
            {"pregunta": "Escribe la razón de 8 a 12.", "respuesta": "2/3"},
            {"pregunta": "Resuelve: 3/4 = x/8", "respuesta": "6"},
            {"pregunta": "Encuentra el cuarto proporcional de 2, 5, 10.", "respuesta": "25"},
            {"pregunta": "Verifica si 4,6,8,12 forman una proporción.", "respuesta": "sí"},
            {"pregunta": "Resuelve: 7/9 = 21/x", "respuesta": "27"},
            {"pregunta": "Calcula el tercer proporcional de 6 y 12.", "respuesta": "24"},
            {"pregunta": "Resuelve: x/15 = 5/25", "respuesta": "3"},
            {"pregunta": "Encuentra el valor de x en: 2/x = 8/12", "respuesta": "3"},
            {"pregunta": "Resuelve: (x+1)/4 = 5/8", "respuesta": "1.5"},
            {"pregunta": "Si a/b = 2/3 y b/c = 4/5, encuentra a/c.", "respuesta": "8/15"}
        ]
    },

    "regla de tres simple e inversa": {
        "concepto": "Método para resolver problemas de proporcionalidad, directa o inversa.",
        "video": "https://youtu.be/DG8j4qDEeHQ?si=ZTXdfVkVg1ckwXTt",
        "ejercicios": [
            {"pregunta": "Si 5 cuadernos cuestan 25 soles, ¿cuánto cuestan 8?", "respuesta": "40"},
            {"pregunta": "Si 3 kg de arroz valen 12 soles, ¿cuánto valen 7 kg?", "respuesta": "28"},
            {"pregunta": "Si 4 obreros construyen una pared en 6 días, ¿cuántos días necesitarán 8 obreros?", "respuesta": "3"},
            {"pregunta": "Si 10 litros de agua pesan 10 kg, ¿cuánto pesan 25 litros?", "respuesta": "25"},
            {"pregunta": "Si un auto recorre 120 km con 8 litros de gasolina, ¿cuántos km recorre con 20 litros?", "respuesta": "300"},
            {"pregunta": "Si 12 máquinas producen 300 piezas en 4 horas, ¿cuántas piezas producen 8 máquinas en 6 horas?", "respuesta": "400"},
            {"pregunta": "Si 15 estudiantes consumen 45 panes, ¿cuántos consumen 25 estudiantes?", "respuesta": "75"},
            {"pregunta": "Si un tren recorre 240 km en 4 horas, ¿cuánto recorre en 9 horas?", "respuesta": "540"},
            {"pregunta": "Si 6 albañiles construyen una casa en 15 días, ¿cuántos días necesitan 9 albañiles?", "respuesta": "10"},
            {"pregunta": "Si 2 impresoras imprimen 500 páginas en 10 minutos, ¿cuántas páginas imprimen 5 impresoras en 15 minutos?", "respuesta": "3750"}
        ]
    },

    "sistema de ecuaciones": {
        "concepto": "Un sistema de ecuaciones es un conjunto de ecuaciones que se resuelven simultáneamente.",
        "video": "https://youtu.be/p2AIFY1b9qk?si=iktJwozmatTCJXAR",
        "ejercicios": [
            {"pregunta": "x + y = 10, x - y = 2", "respuesta": "x=6, y=4"},
            {"pregunta": "2x + y = 7, x - y = 1", "respuesta": "x=2, y=1"},
            {"pregunta": "3x - y = 5, 2x + y = 8", "respuesta": "x=3, y=4"},
            {"pregunta": "x + 2y = 6, 2x - y = 4", "respuesta": "x=2, y=2"},
            {"pregunta": "4x + 3y = 20, 2x - y = 1", "respuesta": "x=2, y=4"},
            {"pregunta": "x - y = 4, 3x + 2y = 18", "respuesta": "x=6, y=2"},
            {"pregunta": "5x - y = 9, x + y = 7", "respuesta": "x=2, y=5"},
            {"pregunta": "2x + 5y = 11, 3x - y = 7", "respuesta": "x=3, y=1"},
            {"pregunta": "x + y = 12, x - 2y = 3", "respuesta": "x=9, y=3"},
            {"pregunta": "3x + 2y = 16, 4x - y = 9", "respuesta": "x=3, y=2"}
        ]
    },

    "teoria de exponentes": {
        "concepto": "Extiende las leyes de potencias a exponentes cero, negativos y fraccionarios.",
        "video": "https://youtu.be/6m-Qzh3NDjk?si=o2SvmgGUFA80VF7J",
        "ejercicios": [
            {"pregunta": "5^0", "respuesta": "1"},
            {"pregunta": "2^-3", "respuesta": "1/8"},
            {"pregunta": "16^(1/2)", "respuesta": "4"},
            {"pregunta": "27^(1/3)", "respuesta": "3"},
            {"pregunta": "8^(2/3)", "respuesta": "4"},
            {"pregunta": "x^0", "respuesta": "1"},
            {"pregunta": "y^-2", "respuesta": "1/y^2"},
            {"pregunta": "(4^3)^(1/2)", "respuesta": "8"},
            {"pregunta": "(9^(1/2))^2", "respuesta": "9"},
            {"pregunta": "125^(2/3)", "respuesta": "25"}
        ]
    }
}

salir_total = False

while not salir_total:
    print("\nTemas disponibles:")
    for tema in temario:
        print("-", tema)
    
    eleccion = input("\nElige un tema (o 'salir' para terminar): ").strip().lower()
    
    if eleccion == "salir":
        print("Aprende+: ¡Hasta luego! Sigue estudiando 🚀")
        break
    
    if eleccion in temario:
        print(f"\nConcepto de {eleccion}:")
        print(temario[eleccion]["concepto"])

        video = temario[eleccion]["video"]
        if isinstance(video, list):
            for v in video:
                print(f"🎬 Video de apoyo: {v}")
        else:
            print(f"🎬 Video de apoyo: {video}")

        for ejercicio in temario[eleccion]["ejercicios"]:
            while True:
                if ejercicio.get("respuesta") == "abierta":
                    input(f"\nResuelve: {ejercicio['pregunta']} (Respuesta libre) ")
                    print("✔️ Listo, pasa al siguiente ejercicio.")
                    break

                respuesta_usuario = input(f"\nResuelve: {ejercicio['pregunta']} = ").strip()
                if respuesta_usuario.lower() == "salir":
                    salir_total = True
                    break
                if respuesta_usuario.lower() == ejercicio["respuesta"].lower():
                    print("✅ ¡Correcto!")
                    break
                else:
                    print("❌ Incorrecto, intenta de nuevo o escribe 'salir' para pasar al siguiente ejercicio.")
            if salir_total:
                break
    else:
        print("Aprende+: Tema no encontrado, elige uno de la lista.")


temario_cl = {
    "Cómo hallar ideas principales y secundarias": {
        "teoria": "La idea principal resume de qué trata el texto. Las ideas secundarias son detalles que explican o apoyan la idea principal."
    },
    "Cómo hallar el propósito del texto": {
        "teoria": "El propósito es la intención del autor al escribir el texto: informar, persuadir, entretener o enseñar."
    }
}

# =========================
# HISTORIALES
# =========================
historial_mate = {}
historial_cl = []

# =========================
# FUNCIONES DE MATEMÁTICAS
# =========================
def ejercicios_matematicas():
    print("\n--- Matemáticas ---")
    salir_total = False
    while not salir_total:
        print("\nTemas disponibles:")
        for tema in temario_mate:
            print("-", tema)
        
        eleccion = input("\nElige un tema (o 'salir' para terminar): ").strip().lower()
        if eleccion == "salir":
            break
        if eleccion not in temario_mate:
            print("Tema no encontrado, elige uno de la lista.")
            continue

        tema_actual = temario_mate[eleccion]
        print(f"\nConcepto de {eleccion}:")
        print(tema_actual["concepto"])
        print(f"🎬 Video de apoyo: {tema_actual['video']}")

        # Inicializar historial de ejercicios
        if eleccion not in historial_mate:
            historial_mate[eleccion] = []

        ejercicios = tema_actual["ejercicios"]
        random.shuffle(ejercicios)  # Para dinamismo

        for ejercicio in ejercicios:
            if ejercicio["pregunta"] in historial_mate[eleccion]:
                continue  # no repetir
            historial_mate[eleccion].append(ejercicio["pregunta"])

            while True:
                if ejercicio.get("respuesta") == "abierta":
                    input(f"\nResuelve: {ejercicio['pregunta']} (Respuesta libre) ")
                    print("✔️ Listo, pasa al siguiente ejercicio.")
                    break

                respuesta_usuario = input(f"\nResuelve: {ejercicio['pregunta']} = ").strip()
                if respuesta_usuario.lower() == "salir":
                    salir_total = True
                    break
                if respuesta_usuario.lower() == ejercicio["respuesta"].lower():
                    print("✅ ¡Correcto!")
                    break
                else:
                    print("❌ Incorrecto, intenta de nuevo o escribe 'salir' para pasar al siguiente ejercicio.")
            if salir_total:
                break

# =========================
# FUNCIONES DE COMPRENSIÓN LECTORA
# =========================
def ia_generar_ejercicio_cl():
    textos = [
        {"texto": "Los árboles producen oxígeno y protegen la biodiversidad.",
         "idea_principal": "Los árboles producen oxígeno y protegen la biodiversidad",
         "proposito": "Informar sobre la importancia de los árboles"},
        {"texto": "El reciclaje reduce la contaminación y conserva recursos naturales.",
         "idea_principal": "El reciclaje reduce la contaminación",
         "proposito": "Concienciar sobre el reciclaje"},
        {"texto": "Los gatos necesitan dormir mucho y les gusta jugar.",
         "idea_principal": "Los gatos necesitan dormir mucho",
         "proposito": "Informar sobre hábitos de los gatos"},
        {"texto": "Leer libros mejora la imaginación y el vocabulario.",
         "idea_principal": "Leer libros mejora la imaginación",
         "proposito": "Motivar la lectura"}
    ]
    disponibles = [t for t in textos if t['texto'] not in historial_cl]
    if not disponibles:
        historial_cl.clear()  # Reinicia historial si se agotaron los ejercicios
        disponibles = textos
    ejercicio = random.choice(disponibles)
    historial_cl.append(ejercicio['texto'])
    return ejercicio

def ia_sugerencias(texto, tema):
    return f"IA: Para '{tema}', analiza el texto buscando pistas clave, palabras repetidas y conectores entre ideas."

def ia_evaluar_respuesta(respuesta_usuario, respuesta_correcta):
    if respuesta_correcta.lower() in respuesta_usuario.lower():
        return "✅ Correcto"
    else:
        return f"❌ Incorrecto, sugerencia: {respuesta_correcta}"

def comprension_lectora():
    print("\n--- Comprensión Lectora ---")
    for tema, contenido in temario_cl.items():
        print(f"\n--- {tema} ---")
        print("Teoría:", contenido['teoria'])

    while True:
        ej = ia_generar_ejercicio_cl()
        print(f"\nEjercicio de texto:\n{ej['texto']}")
        print(ia_sugerencias(ej['texto'], "Comprensión Lectora"))

        respuesta_usuario = input("Idea principal: ").strip()
        if respuesta_usuario.lower() == "salir":
            break
        print(ia_evaluar_respuesta(respuesta_usuario, ej['idea_principal']))

        respuesta_usuario = input("Propósito del texto: ").strip()
        if respuesta_usuario.lower() == "salir":
            break
        print(ia_evaluar_respuesta(respuesta_usuario, ej['proposito']))

# =========================
# MENÚ PRINCIPAL
# =========================
def menu_principal():
    print("Hola, soy Aprende+ 🤖. Puedo ayudarte con matemáticas o comprensión lectora.")
    print("Escribe 'salir' para terminar.\n")

    while True:
        eleccion = input("Elige: 'matematicas' o 'comprension' = ").strip().lower()
        if eleccion == "salir":
            print("Aprende+: ¡Hasta luego! 🚀")
            break
        elif eleccion == "matematicas":
            ejercicios_matematicas()
        elif eleccion == "comprension":
            comprension_lectora()
        else:
            print("Opción no válida, elige 'matematicas' o 'comprension'.")

# =========================
# EJECUCIÓN
# =========================
if __name__ == "__main__":
    menu_principal()