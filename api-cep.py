import requests
import tkinter as tk

class Tela:

    def __init__(self, master):

        self.cep = tk.Label(janela, text="Informe o CEP:")
        self.cep["font"] = ("Arial", "17")
        self.cep.place(x=5, y=10)
        
        self.cepE=tk.Entry(janela)
        self.cepE["font"] = ("Arial","16")
        self.cepE.place(x=175, y=10, width="100", height="30")

        self.bt1=tk.Button(janela, text="Consultar")
        self.bt1.place(x=295, y=4)
        self.bt1["font"] = ("Arial", "14")
        self.bt1.config(foreground="white", bg="green")
        self.bt1.bind("<Button-1>", self.ir)

    def ir(self, event):

        cepp = self.cepE.get()
        print(cepp)
        if len(cepp) != 8:
            
            exit()
            
        requisicao = requests.get('https://viacep.com.br/ws/{}/json/'.format(cepp))
        print(requisicao.json())

        


janela = tk.Tk()
Tela(janela)

janela.geometry("400x200")
janela.mainloop()

#print('-------------------')
#print('Consulta CEP')
#print('-------------------')

#cep_input = input("Digite o CEP: ")

#if len(cep_input) != 8:
    #print('Formato de CEP inválido...')
    #exit()

#requisicao = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep_input))

#print(requisicao.json())


