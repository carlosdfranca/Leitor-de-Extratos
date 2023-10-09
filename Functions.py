import tkinter as tk
from tkinter import filedialog

def pegar_nome_pasta():
    def selecionar_pasta():
        pasta_selecionada = filedialog.askdirectory()
        if pasta_selecionada:
            caminho_var.set(pasta_selecionada)
            janela.quit()

    janela = tk.Tk()
    janela.title("Selecione uma Pasta")

    caminho_var = tk.StringVar()

    label = tk.Label(janela, textvariable=caminho_var)
    label.pack()

    botao_selecionar = tk.Button(janela, text="Selecionar Pasta", command=selecionar_pasta)
    botao_selecionar.pack()


    janela.mainloop()

    pasta_extratos = caminho_var.get()

    return pasta_extratos
