import requests
import tkinter as tk

class Tela:

    def __init__(self, master):
        
        self.cep=tk.Entry(janela)
        self.cep.place(x=5, y=10)

        self.bt1=tk.Button(janela, text="Consultar")
        self.bt1.place(x=145, y=10)
        self.bt1.bind("<Button-1>", self.ir)

    def ir(self, event):

        cepE = self.cep.get()
        print(cepE)
        if len(cepE) != 8:
            exit()
        requisicao = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep_input))
        print(requisicao.json())

        


janela = tk.Tk()
Tela(janela)

janela.geometry("300x200")
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


