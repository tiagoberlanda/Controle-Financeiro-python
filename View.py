from tkinter import *
from tkinter.ttk import Combobox
import pymysql
from datetime import datetime, timedelta
import os

# Criando janela Princiapal
app = Tk()  # Criando janela
app.geometry('650x450')  # Tamanho da janela
app.title('Controle de Finanças')  # Título da Janela

# Criando Informativo de conexão com o Banco
info = StringVar()      #Variavel com o valor que será exibido na tela
info.set('Status : ')     #Setando valor na variavel
informacao_Bd = Label(app, textvariable=info,bd=1,relief="solid", font='Arial 12')
informacao_Bd.place(bordermode=OUTSIDE, height=20, width=500, x=30, y=150)

# Crianco conexão com Banco de Dados
def conectaBanco():
    try:
        con = pymysql.Connect(host='localhost', database='controlefinanceiro', user='root', password='')
        cursor = con.cursor()
        info.set('Status : Conectado com sucesso!')
    except Exception as e:
        info.set('Status : Erro ao Conectar ao Banco de dados!')

# Função de adicionar novo registro
def novoRegistro():
    conectaBanco()


# Função de editar um registro
def editarRegistro():
    conectaBanco()


# Função de remover um registro
def removeRegistro():
    conectaBanco()

# Função de atualizar um registro
def atualizaRegistro():
    conectaBanco()

# Label e Text Box Descriçao
descricao = Label(app, text='Descrição')
descricao.grid(row=0, column=0)
descricao_Tb = Entry(app)
descricao_Tb.grid(row=0, column=1)

# Label e Text Box Valor
valor = Label(app, text='Valor')
valor.grid(row=1, column=0)
valor_Tb = Entry(app)
valor_Tb.grid(row=1, column=1)

# Label e Text Box Categoria
categoria = Label(app, text='Categoria')
categoria.grid(row=1, column=4)
categoria_cb = Combobox (app, values=["Remuneração","Saúde","Transporte","Educação","Cuiadados Pessoais"])
categoria_cb.grid(row=1, column=5)

# Label e Text Box Data
data = Label(app, text='Data')
data.grid(row=0, column=4)
data_Tb = Entry(app)
data_Tb.grid(row=0, column=5)


# Botão de Conexão
Bt_conexao = Button(app, text='Conexão', command=conectaBanco)
Bt_conexao.place(bordermode=OUTSIDE, height=40, width=60, x=60, y=80)

# Botão de Novo
Bt_novo = Button(app, text='Novo', command=novoRegistro)
Bt_novo.place(bordermode=OUTSIDE, height=40, width=60, x=130, y=80)

# Botão de Editar
Bt_editar = Button(app, text='Editar', command=editarRegistro)
Bt_editar.place(bordermode=OUTSIDE, height=40, width=60, x=200, y=80)

# Botão de Excluir
Bt_excluir = Button(app, text='Excluir', command=removeRegistro)
Bt_excluir.place(bordermode=OUTSIDE, height=40, width=60, x=270, y=80)

# Botão de Atualizar
Bt_atualizar = Button(app, text='Atualizar', command=atualizaRegistro)
Bt_atualizar.place(bordermode=OUTSIDE, height=40, width=60, x=340, y=80)

# Grid Principal
# gridPrincipal_Sql = cursor.execute('select * from financas')
# gridPrincipal = Label(app,text=cursor.fetchall())
# gridPrincipal.grid(row=4,column=1)

app.mainloop()  # Mantem Janela Aberta
