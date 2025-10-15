import tkinter as tk


def crear_casita():
    casita = {
        "Casita Florería": {
            "Dimensiones": {
                "Base": "6.8 cm x 5.0 cm",
                "Altura total": "10.5 cm"
            },
            "Frontal": {
                "Título": {
                    "Texto": "Florería",
                    "Color": "Negro",
                    "Altura desde la base": "5.6 cm",
                    "Tamaño": "1.3 cm x 5.5 cm"
                },
                "Puerta": {
                    "Color": "Marrón",
                    "Marco": "Marrón",
                    "Manija": "Marrón oscuro",
                    "Tamaño": "4.4 cm x 2.3 cm"
                },
                "Girasoles": [
                    {"Lado": "Izquierdo", "Altura": "2.5 cm", "Color": "Amarillo", "Centro": "Marrón"},
                    {"Lado": "Derecho", "Altura": "2.4 cm", "Color": "Amarillo", "Centro": "Marrón"}
                ],
                "Pasto": {"Color": "Verde", "Altura": "1.4 cm"}
            },
            "Derecha": {
                "Dimensiones": "6.9 cm x 5.0 cm",
                "Flor morada": {
                    "Pétalos": 7,
                    "Color": "Morado",
                    "Centro": "Amarillo",
                    "Tamaño": "5.0 cm x 2.7 cm"
                },
                "Flores rojas": {"Cantidad": 11, "Color": "Rojo", "Tallo": "Marrón"},
                "Pasto": {"Altura": "1.4 cm"}
            },
            "Izquierda": {
                "Dimensiones": "6.9 cm x 5.0 cm",
                "Ventana": {
                    "Marco": "Marrón",
                    "Tamaño del marco": "2.5 cm x 2.2 cm",
                    "Flor interior": {
                        "Tipo": "Tulipán",
                        "Color": "Rojo",
                        "Tallo": "Verde",
                        "Altura": "1.8 cm"
                    }
                },
                "Tulipanes exteriores": {"Cantidad": 5, "Altura": "2.9 cm", "Color": "Rojo"},
                "Pasto": {"Altura": "1.4 cm"}
            },
            "Trasera": {
                "Dimensiones": "7.0 cm x 6.8 cm",
                "Tulipán grande": {
                    "Color": "Rojo",
                    "Tallo": "Marrón",
                    "Altura máxima": "7.0 cm",
                    "Líneas decorativas": "Negras"
                },
                "Flores": [
                    {"Color": "Rojo", "Centro": "Amarillo"},
                    {"Color": "Rojo", "Centro": "Amarillo"},
                    {"Color": "Morado", "Centro": "Rojo"},
                    {"Color": "Morado", "Centro": "Rojo"}
                ],
                "Girasoles": 4,
                "Pasto": {"Altura": "1.4 cm"}
            },
            "Techo": {
                "Color": "Rojo",
                "Material": "Cartulina",
                "Patrón": "Cuadrícula",
                "Tejas por lado": 24,
                "Total de tejas": 48,
                "Tamaño": "5.0 cm x 8.0 cm"
            },
            "Base": {
                "Color": "Blanco",
                "Dimensiones": "6.8 cm x 5.0 cm",
                "Iniciales": "HDEG",
                "Color de iniciales": "Negro"
            }
        }
    }
    return casita



def descripcion(parte, datos):
    c = datos["Casita Florería"]

    if parte == "Frontal":
        p = c["Frontal"]
        return (
            f" PARTE FRONTAL \n\n"
            f"Título: {p['Título']['Texto']} ({p['Título']['Color']}), "
            f"a {p['Título']['Altura desde la base']} desde la base.\n"
            f"Tamaño del título: {p['Título']['Tamaño']}.\n\n"
            f"Puerta de color {p['Puerta']['Color']} con marco {p['Puerta']['Marco']} "
            f"y manija {p['Puerta']['Manija']} ({p['Puerta']['Tamaño']}).\n\n"
            f"Girasoles: uno a la izquierda ({p['Girasoles'][0]['Altura']} de alto) y otro a la derecha "
            f"({p['Girasoles'][1]['Altura']} de alto), ambos de color amarillo con centro marrón.\n\n"
            f"Pasto {p['Pasto']['Color']} de {p['Pasto']['Altura']} de altura."
        )

    elif parte == "Derecha":
        p = c["Derecha"]
        return (
            f" PARTE DERECHA \n\n"
            f"Dimensiones: {p['Dimensiones']}.\n"
            f"Flor morada con {p['Flor morada']['Pétalos']} pétalos, centro {p['Flor morada']['Centro']} "
            f"y color {p['Flor morada']['Color']} ({p['Flor morada']['Tamaño']}).\n\n"
            f"Flores rojas: {p['Flores rojas']['Cantidad']} en total, tallos {p['Flores rojas']['Tallo']}.\n\n"
            f"Pasto de {p['Pasto']['Altura']} de altura."
        )

    elif parte == "Izquierda":
        p = c["Izquierda"]
        return (
            f" PARTE IZQUIERDA \n\n"
            f"Ventana de marco {p['Ventana']['Marco']} ({p['Ventana']['Tamaño del marco']}).\n"
            f"En su interior hay un {p['Ventana']['Flor interior']['Tipo']} "
            f"{p['Ventana']['Flor interior']['Color']} de {p['Ventana']['Flor interior']['Altura']}.\n\n"
            f"Afuera hay {p['Tulipanes exteriores']['Cantidad']} tulipanes "
            f"de {p['Tulipanes exteriores']['Altura']} de alto, color {p['Tulipanes exteriores']['Color']}.\n\n"
            f"Pasto de {p['Pasto']['Altura']} de altura."
        )

    elif parte == "Trasera":
        p = c["Trasera"]
        return (
            f" PARTE TRASERA \n\n"
            f"Tulipán grande color {p['Tulipán grande']['Color']} con tallo {p['Tulipán grande']['Tallo']} "
            f"y altura máxima de {p['Tulipán grande']['Altura máxima']}.\n"
            f"Líneas decorativas {p['Tulipán grande']['Líneas decorativas']}.\n\n"
            f"Flores: 2 rojas y 2 moradas con centros contrastantes.\n"
            f"Girasoles: {p['Girasoles']}.\n"
            f"Pasto de {p['Pasto']['Altura']} de altura."
        )

    elif parte == "Base":
        p = c["Base"]
        return (
            f" BASE \n\n"
            f"Color: {p['Color']}.\n"
            f"Dimensiones: {p['Dimensiones']}.\n"
            f"Iniciales: {p['Iniciales']} en color {p['Color de iniciales']}."
        )

    elif parte == "Techo":
        p = c["Techo"]
        return (
            f" TECHO \n\n"
            f"Color: {p['Color']}.\n"
            f"Material: {p['Material']}.\n"
            f"Patrón: {p['Patrón']}.\n"
            f"Tejas: {p['Total de tejas']} en total ({p['Tejas por lado']} por lado).\n"
            f"Tamaño: {p['Tamaño']}."
        )

    return "No se encontró información de esa parte."



def interfaz():
    casita = crear_casita()

    def mostrar():
        parte = seleccion.get()
        texto = descripcion(parte, casita)
        salida.config(state="normal")
        salida.delete("1.0", tk.END)
        salida.insert(tk.END, texto)
        salida.config(state="disabled")

    def limpiar():
        salida.config(state="normal")
        salida.delete("1.0", tk.END)
        salida.config(state="disabled")

    ventana = tk.Tk()
    ventana.title("Casita Florería ")
    ventana.geometry("700x600")
    ventana.config(bg="#f9fff9")

    tk.Label(
        ventana, text="Elige la parte de la casita que deseas ver:",
        font=("Arial Rounded MT Bold", 16), bg="#f9fff9", fg="#333"
    ).pack(pady=15)

    opciones = ["Frontal", "Derecha", "Izquierda", "Trasera", "Base", "Techo"]
    seleccion = tk.StringVar(value=opciones[0])
    tk.OptionMenu(ventana, seleccion, *opciones).pack(pady=10)

    botones = tk.Frame(ventana, bg="#f9fff9")
    botones.pack(pady=10)

    tk.Button(botones, text="Mostrar información ", command=mostrar,
              font=("Arial", 12, "bold"), bg="#f9fcf9", width=20).grid(row=0, column=0, padx=10)
    tk.Button(botones, text="Limpiar ", command=limpiar,
              font=("Arial", 12, "bold"), bg="#fdfbfb", width=20).grid(row=0, column=1, padx=10)

    salida = tk.Text(ventana, wrap="word", font=("Arial", 12),
                     bg="white", height=20, width=75)
    salida.pack(pady=10)
    salida.config(state="disabled")

    ventana.mainloop()


if __name__ == "__main__":
    interfaz()
