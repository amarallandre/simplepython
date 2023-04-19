import math
from tkinter import *

import time

# Define a função para desenhar o relógio
def desenhar_relogio():
    # Obter a hora atual
    hora = int(time.strftime("%I"))
    minuto = int(time.strftime("%M"))
    segundo = int(time.strftime("%S"))
    hora_str = time.strftime("%H:%M:%S")

    # Calcula os ângulos para as agulhas
    angulo_segundo = math.radians(segundo * 6)
    angulo_minuto = math.radians(minuto * 6 + segundo * 0.1)
    angulo_hora = math.radians(hora * 30 + minuto * 0.5)

    # Atualiza o texto do relógio digital
    label.config(text=hora_str)

    # Desenha o relógio analógico
    canvas.delete("all")
    canvas.create_oval(10, 10, 190, 190)
    canvas.create_line(100, 100, 100 + 80 * math.sin(angulo_segundo), 100 - 80 * math.cos(angulo_segundo), fill="red", width=2)
    canvas.create_line(100, 100, 100 + 60 * math.sin(angulo_minuto), 100 - 60 * math.cos(angulo_minuto), fill="blue", width=4)
    canvas.create_line(100, 100, 100 + 40 * math.sin(angulo_hora), 100 - 40 * math.cos(angulo_hora), fill="green", width=6)
    canvas.create_oval(95, 95, 105, 105, fill="black")

    # Agendar a próxima atualização
    root.after(1000, desenhar_relogio)

# Cria a janela
root = Tk()
root.title("Relógio Analógico e Digital")

# Cria o canvas para desenhar o relógio analógico
canvas = Canvas(root, width=200, height=200)
canvas.pack(side=LEFT)

# Cria o Label para o relógio digital
label = Label(root, font=("Arial", 20))
label.pack(side=RIGHT, padx=20, pady=20)

# Desenha o relógio analógico pela primeira vez
desenhar_relogio()

# Inicia o loop principal da janela
root.mainloop()