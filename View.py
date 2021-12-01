from tkinter import *
import pymysql

#Crianco conexão com Banco de Dados

con = pymysql.Connect(host='localhost',database='controlefinanceiro',user='root',password='')
cursor = con.cursor()

# Criando janela Princiapal
app = Tk()      #Criando janela
app.geometry('850x620')     #Tamanho da janela
app.title('Controle de Finanças')       #Título da Janela

# Label e Text Box Descriçao
descricao = Label(app, text='Descrição:')
descricao.grid(row=0,column=0)
descricao_Tb = Entry(app)
descricao_Tb.grid(row=0,column=1)

# Label e Text Box Valor
valor = Label(app, text='Valor')
valor.grid(row=1,column=0)
valor_Tb = Entry(app)
valor_Tb.grid(row=1,column=1)


#Grid Principal
gridPrincipal_Sql = cursor.execute('select * from financas')
gridPrincipal = Label(app,text=cursor.fetchall())
gridPrincipal.grid(row=4,column=1)


con.close() # Fecha Conexão com o banco
app.mainloop()      #Mantem Janela Aberta