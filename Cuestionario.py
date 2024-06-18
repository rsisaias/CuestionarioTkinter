import tkinter as tk

class MultipleChoiceQuiz(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Quiz de Opción Múltiple")
        self.geometry("400x250")

        self.questions = [
            {
                "question": "¿Cuál es la unidad de medida correspondiente a 1024 bytes?",
                "numero": "Punto N°1",
                "options": ["Kilobyte", "Megabyte", "Gigabyte", "Terabyte"],
                "correct_answer": "Kilobyte"
            },
            {
                "question": "¿Cuántos bits hay en un byte?",
                "numero": "Punto N°1",
                "options": ["4", "8", "16", "32"],
                "correct_answer": "8"
            },
            {
                "question": "Cuál es la unidad de medida correspondiente a 1024 Kilobytes",
                "numero": "Punto N°1",
                "options": ["Gigabyte", "Terabyte", "Megabyte", "Byte"],
                "correct_answer": "Megabyte"
            },
            {
                "question": "Cuál es la unidad de medida correspondiente a 1024 Megabytes",
                "numero": "Punto N°1",
                "options": ["Gigabyte", "Terabyte", "Kilobyte", "Byte"],
                "correct_answer": "Gigabyte"
            },
            {
                "question": "Cuál es la unidad de medida correspondiente a 1024 Gigabytes",
                "numero": "Punto N°1",
                "options": ["Megabyte", "Terabyte", "Kilobyte", "Byte"],
                "correct_answer": "Terabyte"
            },
            {
                "question": "El Hardware es:",
                "numero": "Punto N°2",
                "options": ["La parte fisica y tangible de la computadora.", "Algo que no se puede ver ni tocar.", "Un teclado", "Una aplicación"],
                "correct_answer": "La parte fisica y tangible de la computadora."
            },
            {
                "question": "El Software es:",
                "numero": "Punto N°2",
                "options": ["Un monitor.", "La parte lógica e intagible de la computadora.", "Un componente", "La parte física"],
                "correct_answer": "La parte lógica e intagible de la computadora."
            },
            {
                "question": "Un sistema informático es un conjunto de dispositivos y programas que trabajan juntos para procesar información.",
                "numero": "Punto N°3",
                "options": ["Verdadero","Falso"],
                "correct_answer": "Verdadero"
            },
            {
                "question": "Qué corresponde al @",
                "numero": "Punto N°4",
                "options": ["0010 0000", "0100 0000", "0100 1011", "0010 1011"],
                "correct_answer": "0100 0000"
            },
            {
                "question": "Qué corresponde al Espacio()",
                "numero": "Punto N°4",
                "options": ["0010 0000", "0100 0000", "0100 1011", "0010 1011"],
                "correct_answer": "0010 0000"
            },
                        {
                "question": "Qué corresponde al k",
                "numero": "Punto N°4",
                "options": ["0010 0000", "0100 0000", "0100 1011", "0010 1011"],
                "correct_answer": "0100 1011"
            },
            {
                "question": "Qué corresponde al +",
                "numero": "Punto N°4",
                "options": ["0010 0000", "0100 0000", "0100 1011", "0010 1011"],
                "correct_answer": "0010 1011"
            },
            {
                "question": "Para desarrollar el trabajo o tomar deciciones eficientes en los diferentes ámbitos en donde una persona se encuentre, se necesita de un recurso vital:",
                "numero": "Punto N° 5",
                "options": ["Información", "Computadora", "Ideas", "Internet"],
                "correct_answer": "Ideas"
            },
            {
                "question": "El Monitor es una parte de la computadora:",
                "numero": "Punto N° 6",
                "options": ["Verdadero", "Falso"],
                "correct_answer": "Verdadero"
            },
            {
                "question": "El Mouse es una parte del celular:",
                "numero": "Punto N° 6",
                "options": ["Verdadero", "Falso"],
                "correct_answer": "Falso"
            },
            {
                "question": "Puerto de entrada: Es un punto de conexión donde los datos entran al sistema informático desde dispositivos externos, como teclados, mouse, escáneres, etc",
                "numero": "Punto N° 7",
                "options": ["Verdadero", "Falso"],
                "correct_answer": "Verdadero"
            },
            {
                "question": "Un puerto de salida es literalmente una puerta, donde los datos son enviados fuera del sistema informático por pequeños mensajeros electrónicos que los llevan a otros dispositivos.",
                "numero": "Punto N° 7",
                "options": ["Verdadero", "Falso"],
                "correct_answer": "Falso"
            },
            {
                "question": "Puerto de entrada-salida: Es un punto de conexión que puede ser utilizado tanto para recibir datos del exterior como para enviar datos hacia dispositivos externos.",
                "numero": "Punto N° 7",
                "options": ["Verdadero", "Falso"],
                "correct_answer": "Verdadero"
            },
            {
                "question": "¿Como se calcula la capacidad de almacenamiento?",
                "numero": "Punto N° 8",
                "options": ["En unidades de medida", "En una bolsa de plástico"],
                "correct_answer": "En unidades de medida"
            },
            {
                "question": "1Tb equvale a:",
                "numero": "Punto N° 9",
                "options": ["1024 Gb", "1024 Tb", "8 Mb", "10 Kb"],
                "correct_answer": "1024 Gb"
            },
            {
                "question": "1Gb equvale a:",
                "numero": "Punto N° 9",
                "options": ["1024 Gb", "1024 Tb", "8 Mb", "1024 Mb"],
                "correct_answer": "1024 Mb"
            },
            {
                "question": "La placa madre es el 'cerebro' de una computadora, conectando todos los componentes importantes para que funcionen juntos.",
                "numero": "Punto N° 10",
                "options": ["Verdadero", "Falso"],
                "correct_answer": "Verdadero"
            },
            {
                "question": "El software de aplicación es un software que usa una aplicación",
                "numero": "Punto N° 13",
                "options": ["Verdadero", "Falso"],
                "correct_answer": "False"
            },
            {
                "question": "Las medidas empleadas en informática son:",
                "numero": "Punto N° 14",
                "options": ["Almacenamiento","Informática","Procesamiento","Transmisión de datos"],
                "correct_answer": "Almacenamiento"
            },
            {
                "question": "Un sistema informático está compuesto por:",
                "numero": "Punto N° 14",
                "options": ["Hardware, software y de soporte humano","Un conjunto de personas, planes e ideas", "Un conjunto de herramientas y soportes técnicos"],
                "correct_answer": "Hardware, software y de soporte humano"
            },
            {
                "question": "El sistema de numeración que utilizan las personas, que fue tomado prestado del mundo árabe siglos atás, se conoce como Sistema Decimal.",
                "numero": "Punto N° 14",
                "options": ["Verdadero", "Falso"],
                "correct_answer": "Falso"
            },
            {
                "question": "La Memoria RAM, se actualiza constantemente mientras el ordenador está en uso y pierde sus datos cuando el ordenador se apaga, es por esto que se denomina volátil",
                "numero": "Punto N° 14",
                "options": ["Verdadero", "Falso"],
                "correct_answer": "Verdadero"
            },
            {
                "question": "ULTIMA PREGUNTA: La Memoria ROM (Read Only Memory) se caracteriza porque solamente puede ser leída, no se puede escribir en ella, es una memoria inalterable.",
                "numero": "Punto N° 14",
                "options": ["Verdadero", "Falso"],
                "correct_answer": "Verdadero"
            },
            {
                "question": "Haz completado el cuestionario :D, te gustó no?",
                "numero": "Punto N° 14",
                "options": ["SI","NO"],
                "correct_answer": "SI"
            }
            
       ]

        self.current_question = 0

        self.label_question = tk.Label(self, text=self.questions[self.current_question]["question"], wraplength=380)
        self.label_question.pack(pady=10)

        self.var_option = tk.StringVar(self)
        self.var_option.set("")

        self.option_buttons = []
        
        if self.questions[self.current_question]["options"] == ["Verdadero", "Falso"]:
            # Empaquetar en fila de dos botones si las opciones son "Verdadero" y "Falso"
            for option in self.questions[self.current_question]["options"]:
                option_button = tk.Radiobutton(self, text=option, variable=self.var_option, value=option, wraplength=380)
                option_button.pack(side=tk.TOP, anchor=tk.W, padx=10)
                self.option_buttons.append(option_button)
        else:
            # Empaquetar en una columna para otras preguntas
            for option in self.questions[self.current_question]["options"]:
                option_button = tk.Radiobutton(self, text=option, variable=self.var_option, value=option, wraplength=380)
                option_button.pack(side=tk.TOP, anchor=tk.W, padx=10)
                self.option_buttons.append(option_button)

        self.button_submit = tk.Button(self, text="Enviar", command=self.check_answer)
        self.button_submit.pack(pady=10)
        
    def check_answer(self):
        selected_option = self.var_option.get()
        correct_answer = self.questions[self.current_question]["correct_answer"]
        if selected_option == correct_answer:
            print("¡Respuesta correcta!")
        else:
            print("Respuesta incorrecta. La respuesta correcta es:", correct_answer)

        self.current_question += 1

        if self.current_question < len(self.questions):
            self.update_question()
        else:
            self.open_written_answer_tab()

    def update_question(self):
        self.label_question.config(text=self.questions[self.current_question]["question"])

        # Limpiar y reconstruir los botones de opción para la nueva pregunta
        for button in self.option_buttons:
            button.pack_forget()  # Ocultar los

        self.option_buttons.clear()  # Limpiar la lista de botones

        if self.questions[self.current_question]["options"] == ["Verdadero", "Falso"]:
            # Empaquetar en fila de dos botones si las opciones son "Verdadero" y "Falso"
            for option in self.questions[self.current_question]["options"]:
                option_button = tk.Radiobutton(self, text=option, variable=self.var_option, value=option)
                option_button.pack(side=tk.TOP, anchor=tk.W, padx=10)
                self.option_buttons.append(option_button)
        else:
            # Empaquetar en una columna para otras preguntas
            for option in self.questions[self.current_question]["options"]:
                option_button = tk.Radiobutton(self, text=option, variable=self.var_option, value=option)
                option_button.pack(side=tk.TOP, anchor=tk.W, padx=10)
                self.option_buttons.append(option_button)

        self.var_option.set("")  # Reiniciar la selección de opción

if __name__ == "__main__":
    app = MultipleChoiceQuiz()
    app.mainloop()
