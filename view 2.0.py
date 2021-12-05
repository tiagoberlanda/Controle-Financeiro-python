from tkinter import *
from tkinter import ttk
import pymysql

class Janela():
    ##### Criando janela Princiapal #####
    global app
    app = Tk()  # Criando janela
    app.geometry('650x450')  # Tamanho da janela
    app.title('Controle de Finanças')  # Título da Janela
    # app.resizable(width=False, height=False) # Trava para Não abrir tela cheia

    ### Criando Informativo de Erros #####
    global info
    info = StringVar()  # Definindo variavel com o valor que será exibido na tela
    info.set('Status : Não Conectado!')  # Setando o texto para aparecer na tela
    informacao_Bd = Label(app, textvariable=info, bd=1, relief="solid", font='Arial 12')
    informacao_Bd.place(bordermode=OUTSIDE, height=35, width=600, x=30, y=150)

    ### Criando os Elementos da Tela ####
    # Label Descrição #
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
    descricao.grid(row=0, column=0)  # Posição no Grid

    # Text Box Descrição #
    global descricao_Tb
    descricao_Tb = Entry(app)
    descricao_Tb.grid(row=0, column=1)  # Posição no Grid

    # Label Valor #
    valor = Label(
        app,
        text='Valor',
        font="Arial 12",
        relief="solid",
        bd=0,
        padx=5,
        pady=5,
        justify=LEFT,
        anchor=W
    )
    valor.grid(row=1, column=0)  # Posição no Grid

    ## Text Box Valor #
    global valor_Tb
    valor_Tb = Entry(app)
    valor_Tb.grid(row=1, column=1)  # Posição no Grid

    # Label Categoria #
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
    categoria.grid(row=1, column=4)  # Posição no Grid

    # Combobox Categoria #
    global categoria_cb
    categoria_cb = ttk.Combobox(app, values=["Remuneração", "Saúde", "Transporte", "Educação", "Cuiadados Pessoais"])
    categoria_cb.grid(row=1, column=5)  # Posição no Grid

    # Label Data #
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
    data.grid(row=0, column=4)  # Posição no Grid

    # Text Box Data #
    global data_Tb
    data_Tb = Entry(app)
    data_Tb.grid(row=0, column=5)  # Posição no Grid

    # Label Tipo #
    tipo_lb = Label(app,
                    text='Tipo',
                    bd=0,
                    font="Arial 12",
                    relief="solid",
                    padx=5,
                    pady=5,
                    justify=CENTER,
                    anchor=S, )
    tipo_lb.grid(row=0, column=6)  # Posição no Grid

    # Combobox Tipo #
    global tipo_cb
    tipo = StringVar()
    tipo_cb = ttk.Combobox(app, values=["Receita", "Despesa"])
    tipo_cb.grid(row=1, column=6)  # Posição no Grid

    # Label Tipo
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
    data.grid(row=0, column=6)  # Posição no Grid

    # Label Id #
    tipo_lb = Label(app,
                    text='ID',
                    bd=0,
                    font="Arial 12",
                    relief="solid",
                    padx=5,
                    pady=5,
                    justify=CENTER,
                    anchor=S, )
    tipo_lb.grid(row=0, column=7)  # Posição no Grid

    ## Text Box ID #
    global id_Tb
    id_Tb = Entry(app,width=5)
    id_Tb.grid(row=0,column=8)  # Posição no Grid

    # Conectando com o Banco de dados e preenchendo treeview #
    def conectaBanco():
        try:
            con = pymysql.connect(user='root',database='controlefinanceiro',password='',host='localhost')
            cursor = con.cursor()
            info.set('Status : Conectado com sucesso!')
        except Exception as e:
            info.set(f'Status : Erro {e}')

        # Puxar informações para o TreeView
        query = cursor.execute('select * from financas')
        query2 = cursor.fetchall()
        for i in range(0, query):
            tv.insert("", "end", values=query2[i])

    # Criando novo registro no banco
    def novoRegistro():
        conteudo_descricao = str(descricao_Tb.get())
        conteudo_valor = str(valor_Tb.get())
        conteudo_categoria = str(categoria_cb.get())
        conteudo_data = str(data_Tb.get())
        conteudo_tipo = str(tipo_cb.get())

        # Validação de dados, se tem ou não valor em todos os campos
        if conteudo_descricao == "" or conteudo_valor == "" or conteudo_categoria == "" or conteudo_data == "" or conteudo_tipo == "":
            info.set('Status : Preencha todas as informações!')
        else:
            # Tentativa de conexão com o banco
            try:
                con = pymysql.Connect(host='localhost', database='controlefinanceiro', user='root', password='')
                cursor = con.cursor()
                cursor.execute(
                    f"INSERT INTO financas(nomeFinanca, valorFinanca, tipoFinanca, dataFinanca, categoriaFinanca)"
                    f" VALUES ('{conteudo_descricao}','{conteudo_valor}','{conteudo_tipo}','{conteudo_data}','{conteudo_categoria}')")
                con.commit()  # Salva as alterações
                info.set('Status : Dados inseridos com Sucesso!')  # Mensagem de sucesso na inserção dos dados

            except Exception as e:
                info.set(f'Erro: {e}')

            # Limpar dados após inserir na Base
            descricao_Tb.delete(0, 'end')
            valor_Tb.delete(0, 'end')
            categoria_cb.delete(0, 'end')
            data_Tb.delete(0, 'end')
            tipo_cb.delete(0, 'end')

    # Excluir um registro do banco de dados #
    def excluiRegistro():
        try:
            con = pymysql.Connect(host='localhost', database='controlefinanceiro', user='root', password='')
            cursor = con.cursor()
            id = id_Tb.get()
            cursor.execute(f'DELETE FROM `financas` WHERE idFinanca = {id}')
            con.commit()  # Salva as alterações
            info.set('Status : Dados inseridos com Sucesso!')  # Mensagem de sucesso na inserção dos dados

        except Exception as e:
            info.set(f'Erro: {e}')

    #Alterando registro do Banco de Dados
    def alteraRegistro():
        try:
            con = pymysql.Connect(host='localhost', database='controlefinanceiro', user='root', password='')
            cursor = con.cursor()
            conteudo_descricao = str(descricao_Tb.get())
            conteudo_valor = str(valor_Tb.get())
            conteudo_categoria = str(categoria_cb.get())
            conteudo_data = str(data_Tb.get())
            conteudo_tipo = str(tipo_cb.get())
            conteudo_id = int(id_Tb.get())
            cursor.execute(f"UPDATE financas SET `nomeFinanca`='{conteudo_descricao}',`valorFinanca`='{conteudo_valor}'"
                           f",`tipoFinanca`='{conteudo_tipo}',`categoriaFinanca`='{conteudo_categoria}',"
                           f"`dataFinanca`='{conteudo_data}', WHERE idFinanca = '{conteudo_id}'")
            con.commit()
            info.set('Status : Dados inseridos com Sucesso!')  # Mensagem de sucesso na inserção dos dados

        except Exception as e:
            info.set(f'Erro: {e}')
    def editaRegistro():
        try:
            con = pymysql.Connect(host='localhost', database='controlefinanceiro', user='root', password='')
            cursor = con.cursor()
            con.commit()  # Salva as alterações
            info.set('Status : Dados inseridos com Sucesso!')  # Mensagem de sucesso na inserção dos dados

        except Exception as e:
            info.set(f'Erro: {e}')

    #### Criando Botões ####
    # Botão de Conexão
    Bt_conexao = Button(app, text='Conexão', command=conectaBanco)
    Bt_conexao.place(bordermode=OUTSIDE, height=40, width=60, x=60, y=80)  # Posição no Grid XY

    # Botão de Novo
    Bt_novo = Button(app, text='Novo', command=novoRegistro)
    Bt_novo.place(bordermode=OUTSIDE, height=40, width=60, x=180, y=80)  # Posição no Grid XY

    # Botão de Editar
    Bt_editar = Button(app, text='Editar', command=editaRegistro)
    Bt_editar.place(bordermode=OUTSIDE, height=40, width=60, x=300, y=80)  # Posição no Grid XY

    # Botão de Excluir
    Bt_excluir = Button(app, text='Excluir', command=excluiRegistro)
    Bt_excluir.place(bordermode=OUTSIDE, height=40, width=60, x=420, y=80)  # Posição no Grid XY

    # Botão de Atualizar
    Bt_atualizar = Button(app, text='Atualizar', command=alteraRegistro)
    Bt_atualizar.place(bordermode=OUTSIDE, height=40, width=60, x=540, y=80)  # Posição no Grid XY

    # TreeViewer de informações
    global tv
    tv = ttk.Treeview(app, columns=('id', 'nome', 'valor', 'tipo', 'categoria', 'data'), show='headings')
    tv.place(bordermode=OUTSIDE, height=200, width=600, x=30, y=190)
    tv.column('id', anchor=CENTER, width=10)
    tv.column('nome', anchor=CENTER, width=80)
    tv.column('valor', anchor=CENTER, width=80)
    tv.column('categoria', anchor=CENTER, width=80)
    tv.column('data', anchor=CENTER, width=80)
    tv.column('tipo', anchor=CENTER, width=80)

    tv.heading('id', text='Id', anchor=CENTER)
    tv.heading('nome', text='Nome', anchor=CENTER)
    tv.heading('valor', text='Valor', anchor=CENTER)
    tv.heading('categoria', text='Categoria', anchor=CENTER)
    tv.heading('data', text='Data', anchor=CENTER)
    tv.heading('tipo', text='Tipo', anchor=CENTER)

    app.mainloop()  # Mantem a janela aberta
