import tkinter as tk
from tkinter import scrolledtext
from lexer import lexer
from parser import parser

class CompilerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Compilador con Interfaz Gráfica")

        # Área de entrada de texto
        self.input_label = tk.Label(root, text="Ingresa una expresión:")
        self.input_label.pack(pady=5)

        self.input_text = tk.Entry(root, width=50)
        self.input_text.pack(pady=5)

        # Botón para evaluar
        self.eval_button = tk.Button(root, text="Evaluar", command=self.evaluate_expression)
        self.eval_button.pack(pady=10)

        # Área de salida para tokens
        self.tokens_label = tk.Label(root, text="Tokens reconocidos:")
        self.tokens_label.pack(pady=5)

        self.tokens_output = scrolledtext.ScrolledText(root, width=60, height=10, state="disabled")
        self.tokens_output.pack(pady=5)

        # Área de salida para el resultado
        self.result_label = tk.Label(root, text="Resultado:")
        self.result_label.pack(pady=5)

        self.result_output = tk.Label(root, text="", fg="blue", font=("Arial", 12))
        self.result_output.pack(pady=5)

    def evaluate_expression(self):
        # Limpiar las áreas de salida
        self.tokens_output.config(state="normal")
        self.tokens_output.delete(1.0, tk.END)
        self.result_output.config(text="")

        # Obtener la expresión ingresada
        expression = self.input_text.get()
        if not expression:
            self.result_output.config(text="Error: No se ingresó ninguna expresión", fg="red")
            return

        try:
            # Procesar la expresión con el lexer
            lexer.input(expression)
            tokens = []
            for token in lexer:
                tokens.append(f"Token: {token.type}, Valor: {token.value}, Posición: {token.lexpos}")

            # Mostrar los tokens en el área de salida
            self.tokens_output.insert(tk.END, "\n".join(tokens))
            self.tokens_output.config(state="disabled")

            # Procesar la expresión con el parser
            result = parser.parse(expression)
            self.result_output.config(text=f"Resultado: {result}", fg="green")

        except SyntaxError as e:
            self.result_output.config(text=f"Error: {e}", fg="red")
        except Exception as e:
            self.result_output.config(text=f"Error inesperado: {e}", fg="red")

if __name__ == "__main__":
    root = tk.Tk()
    app = CompilerGUI(root)
    root.mainloop()