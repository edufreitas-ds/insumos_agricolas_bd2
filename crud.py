from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from databaser import *

# CONEXÃO COM O DATABASE
insumos_db = mysql.connector.connect(host='localhost',
                             user='root',
                             password='m1921a',
                             database='insumos_db')

# Define a função clientes que cria a base de dados Cliente caso ela não exista.

def clientes():
    root = Tk()
    root.title('CLIENTES')
    root.iconbitmap('icones/insumo.ico')
    root.geometry("1200x550")
    root.configure(background="#343434")

    # Adiciona Estilo
    style = ttk.Style()

    # Seleciona Tema Default
    style.theme_use('default')

    # Configura as cores da TreeView
    style.configure("Treeview",
        background="#D3D3D3",
        foreground="black",
        rowheight=25,
        fieldbackground="#D3D3D3")

    # Configura cor do Selecionado
    style.map('Treeview',
        background=[('selected','#347083')])

    # Adiciona tela do TreeView
    tree_frame = Frame(root)
    tree_frame.pack(pady=10)

    # Adiciona ScrollBar do TreeView
    tree_scroll = Scrollbar(tree_frame)
    tree_scroll.pack(side=RIGHT, fill=Y)

    # Cria o TreeView
    my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
    my_tree.pack()

    # Configura o Scrollbar na vertical
    tree_scroll.config(command=my_tree.yview)

    # Define as Colunas
    my_tree['columns'] = ("Cód.", "Nome", "CPF", "Telefone", "E-mail", "CEP", "Endereço", "Num.", "Complemento", "Bairro", "Cidade", "UF")

    # Formata as Colunas
    my_tree.column("#0", width=0, stretch=NO)
    my_tree.column("Cód.", anchor=CENTER, width=30)
    my_tree.column("CPF", anchor=CENTER, width=80)
    my_tree.column("Nome", anchor=CENTER, width=130)
    my_tree.column("Telefone", anchor=CENTER, width=80)
    my_tree.column("E-mail", anchor=CENTER, width=100)
    my_tree.column("CEP", anchor=CENTER, width=60)
    my_tree.column("Num.", anchor=CENTER, width=30)
    my_tree.column("Complemento", anchor=CENTER, width=100)
    my_tree.column("Endereço", anchor=CENTER, width=130)
    my_tree.column("Bairro", anchor=CENTER, width=100)
    my_tree.column("Cidade", anchor=CENTER, width=100)
    my_tree.column("UF", anchor=CENTER, width=30)



    # Cria o Cabeçalho
    my_tree.heading("#0", text="", anchor=CENTER)
    my_tree.heading("Cód.", text="Cód.", anchor=CENTER)
    my_tree.heading("CPF", text="CPF", anchor=CENTER)
    my_tree.heading("Nome", text="Nome", anchor=CENTER)
    my_tree.heading("Telefone", text="Telefone", anchor=CENTER)
    my_tree.heading("E-mail", text="E-mail", anchor=CENTER)
    my_tree.heading("CEP", text="CEP", anchor=CENTER)
    my_tree.heading("Num.", text="Numero", anchor=CENTER)
    my_tree.heading("Complemento", text="Complemento", anchor=CENTER)
    my_tree.heading("Endereço", text="Endereço", anchor=CENTER)
    my_tree.heading("Bairro", text="Bairro", anchor=CENTER)
    my_tree.heading("Cidade", text="Cidade", anchor=CENTER)
    my_tree.heading("UF", text="UF", anchor=CENTER)

    # Confira cor das listras
    my_tree.tag_configure('oddrow', background='white')
    my_tree.tag_configure('evenrow', background='gray')

    # Acrescenta caixas de entrada
    data_frame = LabelFrame(root, text="Cadastro", bg="#343434", fg= "#79D054")
    data_frame.pack(fill="x", expand="yes", padx=20)

    # Caixa do CPF
    cpf_label = Label(data_frame, text="CPF", bg='white')
    cpf_label.grid(row=0, column=0, padx=10, pady=10)
    cpf_entry = Entry(data_frame)
    cpf_entry.grid(row=0, column=1, padx=10, pady=10)

    # Caixa do nomecompleto
    nomecompleto_label = Label(data_frame, text="Nome Completo", bg='white')
    nomecompleto_label.grid(row=0, column=2, padx=10, pady=10)
    nomecompleto_entry = Entry(data_frame)
    nomecompleto_entry.grid(row=0, column=3, padx=10, pady=10)

    # Caixa do telefone
    telefone_label = Label(data_frame, text="Telefone", bg='white')
    telefone_label.grid(row=0, column=4, padx=10, pady=10)
    telefone_entry = Entry(data_frame)
    telefone_entry.grid(row=0, column=5, padx=10, pady=10)

    # Caixa do E-mail
    mail_label = Label(data_frame, text="E-mail", bg='white')
    mail_label.grid(row=0, column=6, padx=10, pady=10)
    mail_entry = Entry(data_frame)
    mail_entry.grid(row=0, column=7, padx=10, pady=10)

    # Caixa do CEP
    cep_label = Label(data_frame, text="CEP", bg='white')
    cep_label.grid(row=1, column=0, padx=10, pady=10)
    cep_entry = Entry(data_frame)
    cep_entry.grid(row=1, column=1, padx=10, pady=10)

    # Caixa do Número do Endereço
    num_end_label = Label(data_frame, text="Numero", bg='white')
    num_end_label.grid(row=1, column=2, padx=10, pady=10)
    num_end_entry = Entry(data_frame)
    num_end_entry.grid(row=1, column=3, padx=10, pady=10)

    # Caixa do Complemento
    comple_label = Label(data_frame, text="Complemento", bg='white')
    comple_label.grid(row=1, column=4, padx=10, pady=10)
    comple_entry = Entry(data_frame)
    comple_entry.grid(row=1, column=5, padx=10, pady=10)

    # Cria a tela de localizar registros.
    def localize_registros():
        global busca_entrada, search

        # Configura a nova Janela.
        search = Toplevel(root)
        search.title("Buscar Clientes")
        search.geometry("400x200")
        search.iconbitmap('icones/insumo.ico')

        # Cria rótulo da tela
        search_frame = LabelFrame(search, text="CPF")
        search_frame.pack(padx=10, pady=10)

        # Adiciona entrada de dados
        busca_entrada = Entry(search_frame, font=("Helvetica", 18))
        busca_entrada.pack(pady=20, padx=20)

        # Adiciona botão
        search_button = Button(search, text="Pesquisar", command=buscar_registros)
        search_button.pack(padx=20, pady=20)


# ======= CRUD ======================= CRUD ======================= CRUD =======

    # c-R-u-d - READ
    # Traz os registros da base de dados Cliente para a tela do TreeView.
    def busca_database():
        # Limpa a Treeview
        for registro in my_tree.get_children():
            my_tree.delete(registro)

        # Cria o cursor
        conn = insumos_db.cursor()

        conn.execute("select cod_cliente, nome, cpf, telefone, e_mail, c.cep, logradouro, numero, complemento, bairro, cidade, uf from cliente c LEFT JOIN endereco e ON e.cep = c.cep;")
        registros = conn.fetchall()

        # Adiciona os dados na tela
        global count
        count = 0

        # Adiciona os dados em formato listrado
        # Os registros 'impares' primeiro e os 'pares' depois.
        for registro in registros:
            if count % 2 == 0:
                my_tree.insert(parent='', index='end', iid=count, text='', values=(registro[0], registro[1], registro[2], registro[3], 
                registro[4], registro[5], registro[6], registro[7], registro[8], registro[9], registro[10], registro[11]), tags=('evenrow',))
            else:
                my_tree.insert(parent='', index='end', iid=count, text='', values=(registro[0], registro[1], registro[2], registro[3], 
                registro[4], registro[5], registro[6], registro[7], registro[8], registro[9], registro[10], registro[11]), tags=('oddrow',))
            # increment counter
            count += 1


        # Commit
        insumos_db.commit()

    # c-R-u-d - READ
    # Localiza registros com base no CPF.
    def buscar_registros():

        # Busca o CPF inserido.
        busque_registro = busca_entrada.get()

        # Fecha caixa de pesquisa
        search.destroy()

        # Limpa a TreeView
        for registro in my_tree.get_children():
            my_tree.delete(registro)

        # Conecta ao database
        c = insumos_db.cursor()

        # Pesquisa pelo CPF
        select = """select cod_cliente, nome, cpf, telefone, e_mail, c.cep, logradouro, numero, complemento, bairro, cidade, uf 
                        from cliente c 
                        LEFT JOIN endereco e ON e.cep = c.cep 
                        WHERE cpf like %s"""
        value = (busque_registro,)

        c.execute(select, value)
        registros = c.fetchall()
        print("Registros na Tela!")

        # Adiciona os dados do CPF na tela
        global count
        count = 0

        # Insere os registros na TreeView conforme o padrão de listras.
        for registro in registros:
            if count % 2 == 0:
                my_tree.insert(parent='', index='end', iid=count, text='', values=(registro[0], registro[1], registro[2], registro[3], 
                registro[4], registro[5], registro[6], registro[7], registro[8], registro[9], registro[10], registro[11]), tags=('evenrow',))
            else:
                my_tree.insert(parent='', index='end', iid=count, text='', values=(registro[0], registro[1], registro[2], registro[3], 
                registro[4], registro[5], registro[6], registro[7], registro[8], registro[9], registro[10], registro[11]), tags=('oddrow',))
            count += 1


        # Commit
        insumos_db.commit()

    # c-r-u-D - DELETE
    # REMOVER CLIENTE
    def remove_um():
        x = my_tree.selection()[0]
        my_tree.delete(x)

        # Se conecta ao database
        c = insumos_db.cursor()

        sql_delete = "DELETE from cliente WHERE cpf=%s"
        val_delete = (cpf_entry.get(),)

        # Deleta o Cliente do DB conforme o cod_cliente
        c.execute(sql_delete, val_delete)

        # Commit
        insumos_db.commit()

        # Encerra conexão
        #conn.close()

        # Limpa as caixas de Entrada
        clear_entries()
        delete_endereco()
        busca_database()

        # Adiciona uma mensagem de DELETADO
        messagebox.showinfo("Deletado!", "Este registro foi deletado.")


    # c-r-u-D - DELETE
    # REMOVER VÁRIOS CLIENTES
    def remove_varios():
        # Adiciona uma pergunta antes de deletar
        response = messagebox.askyesno("CUIDADO!", "Isso vai deletar vários registros.\nTem certeza?!")

        # Se a respostar for 1
        if response == 1:
            # Pega os itens selecionados
            x = my_tree.selection()

            # Cria uma lista de cod_cliente
            clientes_para_deletar = []

            # Acrescenta os selecionaos a lista de clientes para deletar
            for registro in x:
                clientes_para_deletar.append(my_tree.item(registro, 'values')[0])

            # Deleta cada cliente selecionado
            for registro in x:
                my_tree.delete(registro)

            print(clientes_para_deletar)

            # Create a database or connect to one that exists
            c = insumos_db.cursor()

            # Create a cursor instance
            #c = conn.cursor()


            # Deleta todos clientes sleecionados do database
            c.executemany("DELETE from cliente WHERE cod_cliente=%s", [(cod_cliente,) for cod_cliente in clientes_para_deletar])

            # Reset a Lista
            clientes_para_deletar = []


            # Commit
            insumos_db.commit()

            # Encerra conexao
            #conn.close()

            # Limpa as caixas de Entrada
            clear_entries()
            # Deleta o endereço sem cliente
            delete_endereco()
            # Busca os registros remanescentes.
            busca_database()


    # Limpa as caixas de entrada
    def clear_entries():
        # Limpa as caixas de entrada
        #cod_cliente_entry.delete(0, END)
        cpf_entry.delete(0, END)
        nomecompleto_entry.delete(0, END)
        cep_entry.delete(0, END)
        num_end_entry.delete(0, END)
        comple_entry.delete(0, END)
        telefone_entry.delete(0, END)
        mail_entry.delete(0, END)

    # Seleciona o Registro
    def select_registro(e):
            # Limpa as caixas de entrada
            #cod_cliente_entry.delete(0, END)
            cpf_entry.delete(0, END)
            nomecompleto_entry.delete(0, END)
            cep_entry.delete(0, END)
            num_end_entry.delete(0, END)
            comple_entry.delete(0, END)
            telefone_entry.delete(0, END)
            mail_entry.delete(0, END)

            # Pega o número do registro
            selected = my_tree.focus()
            # Pega os valores do registro
            values = my_tree.item(selected,'values')

            # Exibe os valores nas caixas de entrada
            #cod_cliente_entry.insert(0, values[0])
            cpf_entry.insert(0, values[2])
            nomecompleto_entry.insert(0, values[1])
            cep_entry.insert(0, values[5])
            num_end_entry.insert(0, values[7])
            comple_entry.insert(0, values[8])
            telefone_entry.insert(0, values[3])
            mail_entry.insert(0, values[4])

    # c-r-U-d UPDATE
    # Atualizar registro
    def update_cliente():
            # Pega o número do registro
            selected = my_tree.focus()
            # Pega os valores do registro
            values = my_tree.item(selected,'values')

            # ATUALIZAR O DATABASE
            # Cria ou se conecta ao DB
            c = insumos_db.cursor()

            # Cria o cursor
            #c = conn.cursor()
            
            # Executa o UPDATE conforme os valores passados

            update_sql = "UPDATE cliente SET cpf = %s, nome = %s, cep = %s, numero = %s, complemento = %s, telefone = %s, e_mail = %s WHERE cod_cliente = %s"
            update_val = (cpf_entry.get(), 
                nomecompleto_entry.get(), 
                cep_entry.get(), 
                num_end_entry.get(), 
                comple_entry.get(),
                telefone_entry.get(),
                mail_entry.get(),
                values[0])

            if values[5] == cep_entry.get():
                c.execute(update_sql, update_val)
            else:
                add_endereco(cep_entry.get())
                c.execute(update_sql, update_val)
            
            # Commit
            insumos_db.commit()
            print(c.rowcount, "registros atualizados.", )

            # Encerra conexão
            c.close()

            # Limpa a entrada de dados
            #cod_cliente_entry.delete(0, END)
            cpf_entry.delete(0, END)
            nomecompleto_entry.delete(0, END)
            cep_entry.delete(0, END)
            num_end_entry.delete(0, END)
            comple_entry.delete(0, END)
            telefone_entry.delete(0, END)
            mail_entry.delete(0, END)

            delete_endereco()
            busca_database()

    # INSERT
    # Adicionar registro
    def add_cliente():

            # Cria ou se conecta ao DB
            c = insumos_db.cursor()

            # Executa o INSERT conforme os valores passados
            insert_sql = "INSERT INTO cliente (cpf, nome, cep, numero, complemento, telefone, e_mail) values (%s, %s, %s, %s, %s, %s, %s)"

            insert_val = (
                cpf_entry.get(), 
                nomecompleto_entry.get(), 
                cep_entry.get(), 
                num_end_entry.get(), 
                comple_entry.get(),
                telefone_entry.get(),
                mail_entry.get()
                )

            c.execute(f"SELECT * FROM endereco WHERE cep = {cep_entry.get()}")
            results = c.fetchall()
            conta_linhas = c.rowcount

            if conta_linhas == 0:
                add_endereco(cep_entry.get())
                c.execute(insert_sql, insert_val)
            
            else:
                c.execute(insert_sql, insert_val)
                print("Endereço existente.")

            # Commit
            insumos_db.commit()

            # Encerra conexão
            c.close()

            # Limpa as entradas de dados
            #cod_cliente_entry.delete(0, END)
            cpf_entry.delete(0, END)
            nomecompleto_entry.delete(0, END)
            cep_entry.delete(0, END)
            num_end_entry.delete(0, END)
            comple_entry.delete(0, END)
            telefone_entry.delete(0, END)
            mail_entry.delete(0, END)

            # Limpa o TreeView
            my_tree.delete(*my_tree.get_children())

            # Puxa os dados atualizados
            busca_database()


    # ADICIONANDO BOTÕES DE CRUD

    # Categoria COMANDOS
    button_frame = LabelFrame(root, text="Comandos CRUD", bg="#343434", fg='#79D054', highlightbackground="#79D054")
    button_frame.pack(fill="x", expand="yes", padx=20)

    # Botão de Localizar Cliente
    search_button = Button(button_frame, text="Localizar Cliente", command=localize_registros, bg='white')
    search_button.grid(row=0, column=1, padx=10, pady=10)

    # Botão de Atualizar Cliente
    update_button = Button(button_frame, text="Atualizar Cliente", command=update_cliente, bg='white')
    update_button.grid(row=0, column=2, padx=10, pady=10)

    # Botão de Adicionar Cliente
    add_button = Button(button_frame, text="Adicionar Cliente", command=add_cliente, bg='white')
    add_button.grid(row=0, column=3, padx=10, pady=10)

    # Botão de Remover Cliente
    remove_um_button = Button(button_frame, text="Remover Cliente", command=remove_um, bg='white')
    remove_um_button.grid(row=0, column=4, padx=10, pady=10)

    # Botão de Remover Vários Clientes
    remove_varios_button = Button(button_frame, text="Remover Vários", command=remove_varios, bg='white')
    remove_varios_button.grid(row=0, column=5, padx=10, pady=10)

    # Botão de Limpar entrada de dados
    clear_entries_button = Button(button_frame, text="Limpar Entrada", command=clear_entries, bg='white')
    clear_entries_button.grid(row=0, column=6, padx=10, pady=10)

    # Botão de Recuperar dados do DB
    retrieve_data_button = Button(button_frame, text="Recuperar Dados", command=busca_database, bg='white')
    retrieve_data_button.grid(row=0, column=7, padx=10, pady=10)

    # Acrescenta a função de Selecionar e Soltar a função de Selecionar os Registros
    # Permitindo ao usuário que "solte" sua seleção.
    my_tree.bind("<ButtonRelease-1>", select_registro)

    # Puxa dados atualizados no Database de ínicio
    busca_database()

    # FIM!
    root.mainloop()