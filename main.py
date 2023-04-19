import tkinter as tk
import os

# Define a função para abrir o programa escolhido
def open_program(program):
    os.startfile(program)

# Cria a janela da tela inicial
root = tk.Tk()
root.title("Tela Inicial")

# Adiciona um rótulo para a tela inicial
label = tk.Label(root, text="Escolha um programa para abrir:")
label.pack()

# Adiciona botões para abrir cada programa desejado
button1 = tk.Button(root, text="Calculadora", command=lambda: open_program("C:/Users/Usuario/Desktop/pythonProject/dist/Calculadora/Calculadora.exe"))
button1.pack()

button2 = tk.Button(root, text="Cronometro", command=lambda: open_program("C:/Users/Usuario/Desktop/pythonProject/dist/Cronometro.exe"))
button2.pack()

button3 = tk.Button(root, text="Relogio", command=lambda: open_program("C:/Users/Usuario/Desktop/pythonProject/dist/Relogio.exe"))
button3.pack()

button4 = tk.Button(root, text="Quiz", command=lambda: open_program("C:/Users/Usuario/Desktop/pythonProject/dist/Quiz.exe"))
button4.pack()

# Inicia a aplicação
root.mainloop()