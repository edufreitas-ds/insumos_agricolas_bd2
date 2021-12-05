# Importa as Bibliotecas
from tkinter import *
from tkinter import ttk
from crud import clientes
from databaser import *
import mysql.connector

# CONEXÃO COM O DATABASE
insumos_db = mysql.connector.connect(host='localhost',
                             user='root',
                             password='m1921a',
                             database='insumos_db')

endereco()
loja()
cliente()
funcionario()
fornecedor()
lote()
produto()
compra_insumo()
venda_produto()

# Criar nossa janela
janela = Tk()
janela.title("Insumos Agricolas LTDA")
janela.geometry("600x300")
janela.configure(background="white")
janela.resizable(width=False, height=False) # Não permite ampliar ou reduzir a largura e altura da janela.
janela.attributes("-alpha", 0.9) # Transparência
janela.iconbitmap(default="icones/insumo.ico") # Carrega o ícone

# Carregando Imagens
logo_1 = PhotoImage(file="icones/insumos_demo.png")
logo_2 = PhotoImage(file="icones/insumos_instrucoes.png")

#================ CRIANDO WIDGETS ================

# Separar a Janela em duas partes: Esquerda e Direita
LeftFrame = Frame(janela, width=300, height=300, bg="#122620", relief="raise")
LeftFrame.pack(side=LEFT)

RightFrame = Frame(janela, width=290, height=300, bg="#122620", relief="raise")
RightFrame.pack(side=RIGHT)

# Trazendo a Logo para Esquerda
LogoLabel_Left = Label(LeftFrame, image=logo_1, bg="#122620")
LogoLabel_Left.place(x=10, y=50)

# Trazendo a Instrução para Direita
LogoLabel_Right = Label(RightFrame, image=logo_2, bg="#122620")
LogoLabel_Right.place(x=10, y=30)

#================ CRIANDO BOTÕES ================

def Clientes():
    clientes()

# Criando botão de Login
abrir_clientes = ttk.Button(RightFrame, text="CLIENTES", width=20, command=Clientes)
abrir_clientes.place(x=79, y=253)


janela.mainloop() # Propriedades da nossa janela encerrou