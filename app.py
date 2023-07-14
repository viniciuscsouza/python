import tkinter
from tkinter import ttk
from tkinter.messagebox import showinfo
from backend.api import buscar_cep, pesquisar_cep


class Aplicativo(tkinter.Tk):
    ########## CONSTRUTOR DA CLASSE ##############
    def __init__(self):
        super().__init__()
        # configurações da janela raiz
        self.title('Buscar CEP')
        self.geometry('640x420')
        
        # configure the grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)
        self.columnconfigure(2, weight=1)
        
        self.criar_widgets()
        
    ########## MÉTODOS DA CLASSE ##########
    # https://www.pythontutorial.net/tkinter/tkinter-grid/
    def criar_widgets(self):
        # Widget Label
        self.titulo_label = ttk.Label(self, text='Esse é um buscador de CEP', background='blue', foreground='red')
        self.titulo_label.grid(column=1, row=0, pady=20)
        
        self.cep_label = ttk.Label(self, text='Digite o CEP:')
        self.cep_label.grid(column=0, row=1)
        # Widget Entry / Caixa de entrada de Texto
        self.cep_digitado = tkinter.StringVar()
        self.cep_entry = ttk.Entry(self, textvariable=self.cep_digitado)
        self.cep_entry.grid(column=1, row=1, sticky=tkinter.W)
        # Widget Botão
        self.buscar_button = ttk.Button(self, text='Buscar')
        self.buscar_button['command'] = self.botao_foi_clicado
        self.buscar_button.grid(column=2, row=1)
        
    def botao_foi_clicado(self):
        endereco = buscar_cep(self.cep_digitado.get())
        self.titulo_label.config(text=buscar_cep(self.cep_digitado.get()))
        showinfo(title='Botão foi clicado', message=f'RUA: {endereco["logradouro"]}')


if __name__ == "__main__":
    aplicativo = Aplicativo()
    aplicativo.mainloop()
