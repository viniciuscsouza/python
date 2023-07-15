import tkinter
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter.scrolledtext import ScrolledText
from backend.api import pesquisar_endereco, pesquisar_cep


class Aplicativo(tkinter.Tk):
    ########## CONSTRUTOR DA CLASSE ##############
    def __init__(self):
        super().__init__()
        # configurações da janela raiz
        self.title('Buscador de endereço')
        self.geometry('800x600')
        
        # configure the grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)
        self.columnconfigure(2, weight=1)
        
        self.criar_widgets_pesquisar_endereco()
        self.criar_widget_erro_label()
        self.criar_widgets_pesquisar_cep()
        self.criar_widget_scrolled_text()
    ########## MÉTODOS DA CLASSE ##########
    # https://www.pythontutorial.net/tkinter/tkinter-grid/
    def criar_widgets_pesquisar_endereco(self):
        # Widget Label
        ## Título
        self.titulo_label = ttk.Label(self, text='Buscador de endereço', font=("Arial", 22,'bold'))
        self.titulo_label.grid(column=1, row=0, pady=40)
        ## Cep
        self.cep_label = ttk.Label(self, text='Digite o CEP:', font=("Arial", 14) )
        self.cep_label.grid(column=0, row=1, sticky=tkinter.W, padx=40)
        # Widget Entry / Caixa de entrada de Texto
        self.cep_string_var = tkinter.StringVar()
        self.cep_entry = ttk.Entry(self, textvariable=self.cep_string_var)
        self.cep_entry.grid(column=1, row=1, sticky=tkinter.W)
        # Widget Botão
        self.buscar_endereco_button = ttk.Button(self, text='Buscar')
        self.buscar_endereco_button['command'] = self.buscar_endereco
        self.buscar_endereco_button.grid(column=2, row=1)
    
    def criar_widgets_pesquisar_cep(self):
        # Widget Label
        ## UF
        self.uf_label = ttk.Label(self, text='UF:', font=("Arial", 14,'bold'))
        self.uf_label.grid(column=0, row=4, sticky=tkinter.W, padx=40)
        ## Cidade
        self.cidade_label = ttk.Label(self, text='Cidade:', font=("Arial", 14,'bold'))
        self.cidade_label.grid(column=0, row=5, sticky=tkinter.W, padx=40)
        ## Logradouro
        self.logradouro_label = ttk.Label(self, text='Logradouro:', font=("Arial", 14,'bold'))
        self.logradouro_label.grid(column=0, row=6, sticky=tkinter.W, padx=40)
        # Widget Entry / Caixa de entrada de Texto
        ## UF
        self.uf_string_var = tkinter.StringVar()
        self.uf_entry = ttk.Entry(self, textvariable=self.uf_string_var)
        self.uf_entry.grid(column=1, row=4, sticky=tkinter.W)
        ## Cidade
        self.cidade_string_var = tkinter.StringVar()
        self.cidade_entry = ttk.Entry(self, textvariable=self.cidade_string_var)
        self.cidade_entry.grid(column=1, row=5, sticky=tkinter.W)
        ## Logradouro
        self.logradouro_string_var = tkinter.StringVar()
        self.logradouro_entry = ttk.Entry(self, textvariable=self.logradouro_string_var)
        self.logradouro_entry.grid(column=1, row=6, sticky=tkinter.W)
        # Widget Botão
        self.buscar_cep_button = ttk.Button(self, text='Buscar')
        self.buscar_cep_button['command'] = self.buscar_cep
        self.buscar_cep_button.grid(column=2, row=6)

    def criar_widget_scrolled_text(self):
        # Scrolled Text
        self.resultados_scrolledtext = ScrolledText(self, width=50)
        self.resultados_scrolledtext.grid(column=1, row=7, sticky=tkinter.W)
    
    def criar_widget_erro_label(self):
        ## Erro Label
        self.erro_label = ttk.Label(self, font=("Courier", 12), foreground='red')
        self.erro_label.grid(column=1, row=2, sticky=tkinter.W)
    
    def buscar_cep(self):
        try:
            uf = self.uf_string_var.get()
            cidade = self.cidade_string_var.get()
            logradouro = self.logradouro_string_var.get()
            dicionario_endereco = pesquisar_cep(uf, cidade, logradouro)
            self.atualiza_resultado_scrolled_text(dicionario_endereco)
        except Exception as erro:
            self.erro_label['text'] = f'❌ Não foi possível encontrar o CEP'
            print(erro)
            
    def buscar_endereco(self):
        try:
            endereco = pesquisar_endereco(self.cep_string_var.get())
            self.atualiza_resultado_scrolled_text(endereco)
        except Exception as erro:
            self.erro_label['text'] = f'❌ Não existe endereço para o CEP informado'
            print(erro)
    
    def atualiza_resultado_scrolled_text(self, dicionario_endereco):
        mensagem = ''
        if type(dicionario_endereco) is dict:
            mensagem = f'''
CEP:            {dicionario_endereco['cep']}  
Logradouro:     {dicionario_endereco['logradouro']}
Complemento:    {dicionario_endereco['complemento']}
Bairro:         {dicionario_endereco['bairro']}
Localidade:     {dicionario_endereco['localidade']}
UF:             {dicionario_endereco['uf']}
IBGE:           {dicionario_endereco['ibge']}
GIA:            {dicionario_endereco['gia']}
DDD:            {dicionario_endereco['ddd']}
SIAFI:          {dicionario_endereco['siafi']}
        '''
        else:
            for index, item in enumerate(dicionario_endereco):
                mensagem +=  f'''
Resultado nº {index}:

CEP:            {item['cep']}  
Logradouro:     {item['logradouro']}
Complemento:    {item['complemento']}
Bairro:         {item['bairro']}
Localidade:     {item['localidade']}
UF:             {item['uf']}
IBGE:           {item['ibge']}
GIA:            {item['gia']}
DDD:            {item['ddd']}
SIAFI:          {item['siafi']}


'''
        
        self.resultados_scrolledtext.delete(1.0, tkinter.END)
        self.resultados_scrolledtext.insert(tkinter.END, mensagem)

if __name__ == "__main__":
    aplicativo = Aplicativo()
    aplicativo.mainloop()
