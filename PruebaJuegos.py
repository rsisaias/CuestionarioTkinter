from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random

# Función para jugar el juego de Adivina el número
def jugar_adivina_num():
    def seleccionar_palabra():
        return random.choice(palabras)

    numero_secreto = random.randint(1, 100)
    intentos = 0

    mensaje = StringVar()
    mensaje.set("Bienvenido a Adivina el Número!")

    mensaje2 = StringVar()
    mensaje2.set("Ingrese un número del 1 al 100")

    def verificar_numero():
        nonlocal intentos
        try:
            intento = int(entry.get())
            intentos += 1
            contador.config(text=f"Intentos: {intentos}")

            if intento < numero_secreto:
                mensaje2.set("El número es más grande. Intenta de nuevo.")
            elif intento > numero_secreto:
                mensaje2.set("El número es más pequeño. Intenta de nuevo.")
            else:
                mensaje2.set(f"¡Felicidades! Adivinaste el número {numero_secreto} en {intentos} intentos.")
                messagebox.showinfo("Adivina el Número", mensaje2.get())
                entry.delete(0, 'end')
                reiniciar_juego()

        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa un número válido.")

    def reiniciar_juego():
        nonlocal numero_secreto, intentos
        numero_secreto = random.randint(1, 100)
        intentos = 0
        mensaje.set("Bienvenido a Adivina el Número!")
        mensaje2.set("Ingrese un número del 1 al 100")
        contador.config(text="Intentos: ")
        entry.delete(0, 'end')

    # Crear ventana para el juego de Adivina el número
    juego_window = Toplevel(root)
    juego_window.title("Adivina el Número")
    juego_window.geometry("250x250")

    # Agregar contenido al Notebook, que es crear una pestaña en la ventana juego_window
    notebook = ttk.Notebook(juego_window)

    tab1 = ttk.Frame(notebook)
    notebook.add(tab1, text="Adivina el Número")

    label = Label(tab1, textvariable=mensaje)
    label.grid(row=0, column=0)

    label2 = Label(tab1, textvariable=mensaje2)
    label2.grid(row=1, column=0)

    entry = Entry(tab1, width=20)
    entry.grid(row=2, column=0)

    contador = Label(tab1, text="Intentos:")
    contador.grid(row=3, column=0)

    boton_adivinar = Button(tab1, text="Adivinar", command=verificar_numero)
    boton_adivinar.grid(row=4, column=0, pady=10)

    boton_reiniciar = Button(tab1, text="Reiniciar Juego", command=reiniciar_juego)
    boton_reiniciar.grid(row=5, column=0)

    # Empacar el Notebook
    notebook.pack(padx=10, pady=10, fill=BOTH, expand=True)
#--------------------------------------------------------------------------
# Función para jugar el juego del Ahorcado
def seleccionar_palabra():
    palabras = ["python",
                "queso",
                "juego",
                "crear",
                "computadora",
                "teclado",
                "raton",
                "monitor"]
    return random.choice(palabras)

def jugar_ahorcado():
    palabra_secreta = seleccionar_palabra()
    letras_adivinadas = []
    intentos_restantes = 10

    # Función para actualizar la palabra mostrada en la interfaz gráfica
    def actualizar_palabra_mostrada():
        palabra_mostrada = ""
        for letra in palabra_secreta:
            if letra in letras_adivinadas:
                palabra_mostrada += letra
            else:
                palabra_mostrada += "_ "

        palabra_label.config(text="Palabra: " + palabra_mostrada)
        intentos_label.config(text="Intentos restantes: " + str(intentos_restantes))

    # Función para manejar la adivinanza del jugador
    def adivinar_letra():
        nonlocal intentos_restantes
        adivinanza = adivinanza_entry.get().lower()

        if len(adivinanza) == 1 and adivinanza.isalpha():
            if adivinanza in letras_adivinadas:
                resultado_label.config(text="Ya adivinaste esa letra. ¡Intenta otra!")
            elif adivinanza in palabra_secreta:
                letras_adivinadas.append(adivinanza)
                if set(letras_adivinadas) == set(palabra_secreta):
                    resultado_label.config(text="¡Ganaste! La palabra secreta es: " + palabra_secreta)
                else:
                    resultado_label.config(text="¡Bien hecho! La letra está en la palabra.")
            else:
                letras_adivinadas .append(adivinanza)
                intentos_restantes -= 1
                if intentos_restantes == 0:
                    resultado_label.config(text="¡Perdiste! La palabra secreta era: " + palabra_secreta)
                else:
                    resultado_label.config(text="La letra no está en la palabra. Intenta de nuevo.")
            actualizar_palabra_mostrada()
        else:
            resultado_label.config(text="Ingresa una letra válida.")



    # Crear ventana para el juego del Ahorcado
    juego2_window = Toplevel(root)
    juego2_window.geometry("300x250")
    juego2_window.title("Ahorcado")

    notebook3 = ttk.Notebook(juego2_window)
    tab3 = ttk.Frame(notebook3)
    notebook3.add(tab3, text="Ahorcado")

    palabra_label = Label(tab3, text="")
    palabra_label.pack()

    intentos_label = Label(tab3, text="")
    intentos_label.pack()

    adivinanza_label = Label(tab3, text="Ingresa una letra:")
    adivinanza_label.pack()

    adivinanza_entry = Entry(tab3)
    adivinanza_entry.pack()

    letras_adivinadas_label = Label(tab3, text="Letras adivinadas: ")
    letras_adivinadas_label.pack()

    adivinar_button = Button(tab3, text="Adivinar", command=adivinar_letra)
    adivinar_button.pack()

    resultado_label = Label(tab3, text="")
    resultado_label.pack()

    # Inicializar la interfaz gráfica con la palabra secreta y los intentos restantes
    actualizar_palabra_mostrada()
    intentos_label.config(text="Intentos restantes: " + str(intentos_restantes))
    notebook3.pack(padx=10, pady=10, fill=BOTH, expand=True)
    
#-------------------------------------------------------------------------- 
    # Función para jugar el juego de Piedra, papel o tijera
def jugar_ppt():
    opciones = ["piedra", "papel", "tijera"]
    # Función para manejar la elección del jugador
    def elegir(opcion):
        eleccion_jugador = opcion.lower()
        eleccion_computadora = random.choice(opciones)

        eleccion_computadora_label.config(text=f"La computadora eligió: {eleccion_computadora}")

        if eleccion_jugador == eleccion_computadora:
            resultado.config(text="¡Es un empate!")

        elif (
            (eleccion_jugador == "piedra" and eleccion_computadora == "tijera") or
            (eleccion_jugador == "papel" and eleccion_computadora == "piedra") or
            (eleccion_jugador == "tijera" and eleccion_computadora == "papel")
            ):
            resultado.config(text="¡Ganaste!")

        else:
            resultado.config(text="La computadora gana.")

    # Crear ventana nueva para el juego
    juego_window = Toplevel(root)
    juego_window.geometry("250x250")
    juego_window.title("Piedra, Papel o Tijera")

    notebook2 = ttk.Notebook(juego_window)
    tab2 = ttk.Frame(notebook2
                     )
    notebook2.add(tab2, text="Piedra, papel o tijera")

    instruccion_label = Label(tab2, text="Elige una opción:")
    instruccion_label.pack()

    buttons_frame = Frame(tab2)
    buttons_frame.pack()

    piedra_button = Button(buttons_frame, text="Piedra", command=lambda: elegir("piedra"))
    papel_button = Button(buttons_frame, text="Papel", command=lambda: elegir("papel"))
    tijera_button = Button(buttons_frame, text="Tijera", command=lambda: elegir("tijera"))

    piedra_button.pack(side=LEFT, fill=BOTH, expand=True)
    papel_button.pack(side=LEFT, fill=BOTH, expand=True)
    tijera_button.pack(side=LEFT, fill=BOTH, expand=True)

    resultado = Label(tab2, text="")
    resultado.pack()

    eleccion_computadora_label = Label(tab2, text="")
    eleccion_computadora_label.pack()

    notebook2.pack(padx=10, pady=10, fill=BOTH, expand=True)

#--------------------------------------------------------------------------
# Función para manejar la selección en el menú desplegable
def seleccionar_juego(*args):
    selected_game = juego.get()
    if selected_game == "Piedra, papel o tijera":
        jugar_ppt()
    elif selected_game == "Adivina el número":
        jugar_adivina_num()
    else:
        jugar_ahorcado()
#--------------------------------------------------------------------------
# Ventana principal
root = Tk()
root.title("Arcade 'El Penitente'")
root.geometry("250x250")

bienvenida = Label(root, text="¡Bienvenido/a al Arcade 'El Penitente'!")
bienvenida.grid(row=0, column=0)
elegiunjuego = Label(root, text="¡En este botón podrá elegir distintos juegos!")
elegiunjuego.grid(row=1, column=0)

# Lista de juegos
lista = [
    "Adivina el número",
    "Ahorcado",
    "Piedra, papel o tijera"
]

juego = StringVar()
juego.set(lista[0])

drop = OptionMenu(root, juego, *lista)
drop.grid(row=3, column=0)

# Asociar la función seleccionar_juego con el evento de cambio en el menú desplegable
juego.trace_add("write", seleccionar_juego)

root.mainloop()
