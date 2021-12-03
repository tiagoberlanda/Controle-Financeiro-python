from tkinter import *
from tkinter.ttk import Combobox
import pymysql
from datetime import datetime, timedelta
import os

##### Criando janela Princiapal #####
app = Tk()  # Criando janela
app.geometry('650x450')  # Tamanho da janela
app.title('Controle de Finanças')  # Título da Janela
#app.resizable(width=False, height=False) # Trava para Não abrir tela cheia


##### Criando Informativo de Erros #####
info = StringVar()      #Definindo variavel com o valor que será exibido na tela
info.set('Status : ')     #Setando o texto para aparecer na tela
informacao_Bd = Label(app, textvariable=info,bd=1,relief="solid", font='Arial 12')
informacao_Bd.place(bordermode=OUTSIDE, height=35, width=500, x=30, y=150)


###### Crianco conexão com Banco de Dados #####
def conectaBanco():
    try:
        con = pymysql.Connect(host='localhost', database='controlefinanceiro', user='root', password='')
        cursor = con.cursor()
        info.set('Status : Conectado com sucesso!')
    except Exception as e:
        info.set('Status : Erro ao Conectar ao Banco de dados!')

###### Função de adicionar novo registro #####
def novoRegistro():
    conteudo_descricao = str(descricao_Tb.get())
    conteudo_valor = str(valor_Tb.get())
    conteudo_categoria = str(categoria_cb.get())
    conteudo_data = str(data_Tb.get())
    conteudo_tipo = str(tipo_cb.get())

    #Validação de dados, se tem ou não valor em todos os campos
    if conteudo_descricao == "" or conteudo_valor == "" or conteudo_categoria == "" or conteudo_data == "" or conteudo_tipo == "":
        info.set('Status : Preencha todas as informações!')
    else:
        try:
            con = pymysql.Connect(host='localhost', database='controlefinanceiro', user='root', password='')
            cursor = con.cursor()
            cursor.execute(f"INSERT INTO financas (nomeFinanca, valorFinanca,tipoFinanca, dataFinanca, categoriaFinanca )"
                           f"VALUES ('{conteudo_descricao}','{conteudo_valor}','{conteudo_tipo})','{conteudo_data}','{conteudo_categoria}'")
            con.commit()
            info.set('Status : Sucesso!')
        except Exception as e:
            info.set(f'Erro: {e}')
            print(f'Erro: {e}')

###### Função de editar um registro ######
def editarRegistro():
    try:
        con = pymysql.Connect(host='localhost', database='controlefinanceiro', user='root', password='')
        cursor = con.cursor()
        info.set('Status : Conectado com sucesso!')
    except Exception as e:
        info.set('Status : Erro ao Conectar ao Banco de dados!')


###### Função de remover um registro ######
def removeRegistro():
    try:
        con = pymysql.Connect(host='localhost', database='controlefinanceiro', user='root', password='')
        cursor = con.cursor()
        info.set('Status : Conectado com sucesso!')
    except Exception as e:
        info.set('Status : Erro ao Conectar ao Banco de dados!')

###### Função de atualizar um registro #####
def atualizaRegistro():
    try:
        con = pymysql.Connect(host='localhost', database='controlefinanceiro', user='root', password='')
        cursor = con.cursor()
        info.set('Status : Conectado com sucesso!')
    except Exception as e:
        info.set('Status : Erro ao Conectar ao Banco de dados!')

#Nao usar?
def Pegarvalores():
    conteudo_descricao = str(descricao_Tb.get())
    conteudo_valor = str(valor_Tb.get())
    conteudo_categoria = str(categoria_cb.get())
    conteudo_data = str(data_Tb.get())
    conteudo_tipo = str(tipo_cb.get())

#### Label Descrição ####
descricao = Label(
        app,
        text='Descrição',
        bd=0,
        font="Arial 12",
        relief="solid",
        padx=5,
        pady=5,
        justify=LEFT,
        anchor=W
)
descricao.grid(row=0, column=0) #Posição no Grid

##### Text Box Descrição ######
descricao_Tb = Entry(app)
descricao_Tb.grid(row=0, column=1)  #Posição no Grid

#### Label Valor ######
valor = Label(app,
              text='Valor',
              font="Arial 12",
              relief="solid",
              bd=0,
              padx=5,
              pady=5,
              justify=LEFT,
              anchor=W
)
valor.grid(row=1, column=0) #Posição no Grid

###### Text Box Valor #####
valor_Tb = Entry(app)
valor_Tb.grid(row=1, column=1)  #Posição no Grid

##### Label Categoria ######
categoria = Label(app,
              text='Categoria',
              font="Arial 12",
              relief="solid",
              bd=0,
              padx=5,
              pady=5,
              justify=LEFT,
              anchor=W
)
categoria.grid(row=1, column=4) #Posição no Grid

##### Combobox Categoria ######
categoria_cb = Combobox (app, values=["Remuneração","Saúde","Transporte","Educação","Cuiadados Pessoais"])
categoria_cb.grid(row=1, column=5)  #Posição no Grid

###### Label Data ######
data = Label(app,
            text='Data',
            bd=0,
            font="Arial 12",
            relief="solid",
            padx=5,
            pady=5,
            justify=LEFT,
            anchor=W,
)
data.grid(row=0, column=4)  #Posição no Grid

###### Text Box Data #######
data_Tb = Entry(app)
data_Tb.grid(row=0, column=5)   #Posição no Grid

####### Label Tipo ######
tipo_lb = Label(app,
                text='Tipo',
                bd=0,
                font="Arial 12",
                relief="solid",
                padx=5,
                pady=5,
                justify=CENTER,
                anchor=S,)
tipo_lb.grid(row=0, column=6)  #Posição no Grid

####### Combobox Tipo #######
tipo = StringVar()
tipo_cb = Combobox(app, values=["Receita","Despesa"])
tipo_cb.grid(row=1, column=6)  #Posição no Grid

# Label Data
data = Label(app,
            text='Tipo',
            bd=0,
            font="Arial 12",
            relief="solid",
            padx=5,
            pady=5,
            justify=LEFT,
            anchor=W,
)
data.grid(row=0, column=6)  #Posição no Grid


# Botão de Conexão
Bt_conexao = Button(app, text='Conexão', command=conectaBanco)
Bt_conexao.place(bordermode=OUTSIDE, height=40, width=60, x=60, y=80)   #Posição no Grid XY

# Botão de Novo
Bt_novo = Button(app, text='Novo', command=novoRegistro)
Bt_novo.place(bordermode=OUTSIDE, height=40, width=60, x=150, y=80) #Posição no Grid XY

# Botão de Editar
Bt_editar = Button(app, text='Editar', command=editarRegistro)
Bt_editar.place(bordermode=OUTSIDE, height=40, width=60, x=240, y=80)   #Posição no Grid XY

# Botão de Excluir
Bt_excluir = Button(app, text='Excluir', command=removeRegistro)
Bt_excluir.place(bordermode=OUTSIDE, height=40, width=60, x=330, y=80)  #Posição no Grid XY

# Botão de Atualizar
Bt_atualizar = Button(app, text='Atualizar', command=atualizaRegistro)
Bt_atualizar.place(bordermode=OUTSIDE, height=40, width=60, x=420, y=80)    #Posição no Grid XY

app.mainloop()  # Mantem Janela Aberta
