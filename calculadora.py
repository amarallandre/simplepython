from tkinter import *

# Define a função para realizar o cálculo
def calcular():
    num1 = float(primeiro_numero.get())
    num2 = float(segundo_numero.get())
    operacao = operacao_escolhida.get()

    if operacao == "+":
        resultado = num1 + num2
    elif operacao == "-":
        resultado = num1 - num2
    elif operacao == "*":
        resultado = num1 * num2
    elif operacao == "/":
        resultado = num1 / num2
    else:
        resultado = "Operação inválida!"

    resultado_label.configure(text="Resultado: " + str(resultado))

# Cria a janela
janela = Tk()
janela.title("Calculadora")

# Cria os widgets da interface gráfica
primeiro_numero_label = Label(janela, text="Digite o primeiro número:")
primeiro_numero_label.pack()

primeiro_numero = Entry(janela)
primeiro_numero.pack()

segundo_numero_label = Label(janela, text="Digite o segundo número:")
segundo_numero_label.pack()

segundo_numero = Entry(janela)
segundo_numero.pack()

operacao_label = Label(janela, text="Escolha a operação:")
operacao_label.pack()

operacao_escolhida = StringVar(janela)
operacao_escolhida.set("+") # Define a operação padrão como soma

operacao_soma = Radiobutton(janela, text="+", variable=operacao_escolhida, value="+")
operacao_soma.pack()

operacao_subtracao = Radiobutton(janela, text="-", variable=operacao_escolhida, value="-")
operacao_subtracao.pack()

operacao_multiplicacao = Radiobutton(janela, text="*", variable=operacao_escolhida, value="*")
operacao_multiplicacao.pack()

operacao_divisao = Radiobutton(janela, text="/", variable=operacao_escolhida, value="/")
operacao_divisao.pack()

calcular_botao = Button(janela, text="Calcular", command=calcular)
calcular_botao.pack()

resultado_label = Label(janela, text="Resultado: ")
resultado_label.pack()

# Inicia a janela principal
janela.mainloop()