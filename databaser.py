import mysql.connector
from pycep_correios import get_address_from_cep, WebService

# CONEXÃO COM SEU MYSQL
mysql_connect = mysql.connector.connect(host='localhost',
                             user='root',
                             password='m1921a')

# CRIAÇÃO DO BANCO DE DADOS insumos_db 
def create_db():
    conn = mysql_connect.cursor()
    conn.execute("CREATE DATABASE IF NOT EXISTS insumos_db")
    mysql_connect.commit()
    print("A conexão com o Banco de Dados 'insumos_db' foi criada!")
    conn.close()

create_db()

# CONEXÃO COM O INSUMOS
insumos_db = mysql.connector.connect(host='localhost',
                             user='root',
                             password='m1921a',
                             database='insumos_db')
# Cria tabela endereço
def endereco():

    conn = insumos_db.cursor()

    conn.execute("""CREATE TABLE IF NOT EXISTS endereco (
                        `cep` varchar(10) NOT NULL,
                        `logradouro` varchar(100) DEFAULT NULL,
                        `bairro` varchar(50) DEFAULT NULL,
                        `cidade` varchar(50) DEFAULT NULL,
                        `uf` varchar(2) DEFAULT NULL,
                        PRIMARY KEY (`cep`),
                        UNIQUE KEY `cep_UNIQUE` (`cep`)
                    ) 
                    ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;""")
    # Commit
    insumos_db.commit()
    conn.close()

# Insere o endereço conforme o CEP
def add_endereco(x, msg=True):

        # Armazena CEP do endereco
        cep_endereco = get_address_from_cep(x, webservice=WebService.VIACEP)

        # Conecta ao DB
        c = insumos_db.cursor()

        # Executa o INSERT conforme CEP passado
        insert_sql = """INSERT IGNORE INTO endereco (cep, logradouro, bairro, cidade, uf) values (%s, %s, %s, %s, %s)"""
        insert_val = (x,
            cep_endereco['logradouro'],
            cep_endereco['bairro'],
            cep_endereco['cidade'],
            cep_endereco['uf'])
        
        c.execute(insert_sql, insert_val)

        # Commit
        insumos_db.commit()

        if msg == True:
            print('Novo endereço inserido!')

        # Encerra conexão
        c.close()

# Deleta endereços que não possuem correspondentes.
def delete_endereco():

        # Conecta ao DB
        c = insumos_db.cursor()


        delete_sql = """DELETE e 
                        FROM endereco e 
                        LEFT JOIN cliente c ON c.cep = e.cep
                        LEFT JOIN loja l ON l.cep = e.cep
                        LEFT JOIN funcionario f ON f.cep = e.cep  
                        WHERE c.cep IS NULL AND l.cep IS NULL AND f.cep IS NULL"""

        c.execute(delete_sql)
        
        # Commit
        insumos_db.commit()
        print('Tabela Endereco atualizada!')
        
        # Encerra conexão
        c.close()

def loja():
    # C-r-u-d - CREATE
    conn = insumos_db.cursor()
    conn.execute("""CREATE TABLE IF NOT EXISTS `loja`( 
                            `cnpj_loja` varchar(50) NOT NULL,
                            `nome_fantasia` varchar(50) NOT NULL,
                            `cep` varchar(10) DEFAULT NULL,
                            `numero` varchar(5) NOT NULL,
                            `complemento` varchar(50) DEFAULT NULL,
                            `telefone` varchar(20) DEFAULT NULL,
                            PRIMARY KEY (`cnpj_loja`),
                            UNIQUE KEY `cnpj_loja_UNIQUE` (`cnpj_loja`),
                            KEY `cep_idx` (`cep`),
                            CONSTRAINT `cep_fk_1` FOREIGN KEY (`cep`) REFERENCES `endereco` (`cep`)
                            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
                            """)
    # Commit
    insumos_db.commit()
    print("A tabela 'loja' foi criada!")
    conn.close()

def cliente():
    conn = insumos_db.cursor()
    conn.execute("""CREATE TABLE IF NOT EXISTS cliente (
                        `cod_cliente` int NOT NULL AUTO_INCREMENT,
                        `cpf` varchar(15) NOT NULL,
                        `nome` varchar(100) NOT NULL,
                        `telefone` varchar(20) DEFAULT NULL,
                        `e_mail` varchar(50) DEFAULT NULL,
                        `cep` varchar(10) DEFAULT NULL,
                        `numero` varchar(10) NOT NULL,
                        `complemento` varchar(50) DEFAULT NULL,
                        PRIMARY KEY (`cod_cliente`),
                        UNIQUE KEY `cod_cliente_UNIQUE` (`cod_cliente`),
                        UNIQUE KEY `cpf_UNIQUE` (`cpf`),
                        KEY `cep_idx` (`cep`),
                        CONSTRAINT `cep_fk_2` FOREIGN KEY (`cep`) REFERENCES `endereco` (`cep`)
                    ) 
                    ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;""")
    # Commit
    insumos_db.commit()
    print("A tabela 'cliente' foi criada!")
    conn.close()

def funcionario():

    conn = insumos_db.cursor()

    conn.execute("""CREATE TABLE  IF NOT EXISTS `funcionario` (
                        `cod_funcionario` int NOT NULL AUTO_INCREMENT,
                        `cpf` varchar(15) NOT NULL,
                        `nome` varchar(100) NOT NULL,
                        `cep` varchar(10) DEFAULT NULL,
                        `numero` varchar(5) NOT NULL,
                        `complemento` varchar(50) DEFAULT NULL,
                        `telefone` varchar(20) DEFAULT NULL,
                        `e_mail` varchar(50) DEFAULT NULL,
                        `carga_horaria` int DEFAULT NULL,
                        `cargo` varchar(25) DEFAULT NULL,
                        `cod_pis` varchar(15) NOT NULL,
                        `data_nascimento` date DEFAULT NULL,
                        PRIMARY KEY (`cod_funcionario`),
                        UNIQUE KEY `cod_funcionario_UNIQUE` (`cod_funcionario`),
                        UNIQUE KEY `cpf_UNIQUE` (`cpf`),
                        UNIQUE KEY `cod_pis_UNIQUE` (`cod_pis`),
                        KEY `cep_idx` (`cep`),
                        CONSTRAINT `cep_fk_3` FOREIGN KEY (`cep`) REFERENCES `endereco` (`cep`)
                        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
                    """)
    # Commit
    insumos_db.commit()
    print("A tabela 'funcionario' foi criada.")
    conn.close()

def fornecedor():

    conn = insumos_db.cursor()

    conn.execute("""CREATE TABLE IF NOT EXISTS `fornecedor` (
                        `cod_fornecedor` int NOT NULL AUTO_INCREMENT,
                        `nome_fornecedor` varchar(30) DEFAULT NULL,
                        `cnpj_fornecedor` varchar(20) NOT NULL,
                        `telefone` varchar(30) DEFAULT NULL,
                        `e-mail` varchar(50) DEFAULT NULL,
                        PRIMARY KEY (`cod_fornecedor`),
                        UNIQUE KEY `idfornecedor_UNIQUE` (`cod_fornecedor`),
                        UNIQUE KEY `cnpj_fornecedor_UNIQUE` (`cnpj_fornecedor`)
                        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
                    """)
    # Commit
    insumos_db.commit()
    print("A tabela 'fornecedor' foi criada.")
    conn.close()

def lote():

    conn = insumos_db.cursor()

    conn.execute("""CREATE TABLE IF NOT EXISTS `lote` (
                        `cod_lote` varchar(10) NOT NULL,
                        `data_validade` date NOT NULL,
                        `data_fabricacao` date NOT NULL,
                        `cod_fornecedor` int NOT NULL,
                        PRIMARY KEY (`cod_lote`),
                        UNIQUE KEY `cod_lote_UNIQUE` (`cod_lote`),
                        UNIQUE KEY `cod_fornecedor_UNIQUE` (`cod_fornecedor`),
                        CONSTRAINT `cod_fornecedor_fk_2` FOREIGN KEY (`cod_fornecedor`) REFERENCES `fornecedor` (`cod_fornecedor`)
                        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
                    """)
    # Commit
    insumos_db.commit()
    print("A tabela 'lote' foi criada.")
    conn.close()

def produto():

    conn = insumos_db.cursor()

    conn.execute("""CREATE TABLE IF NOT EXISTS `produto` (
                        `cod_produto` int NOT NULL AUTO_INCREMENT,
                        `nome_produto` varchar(100) NOT NULL,
                        `descricao_produto` varchar(100) DEFAULT NULL,
                        `quantidade_estoque` int DEFAULT NULL,
                        `valor_produto` float DEFAULT NULL,
                        `cod_lote` varchar(10) DEFAULT NULL,
                        `categoria_produto` varchar(50) DEFAULT NULL,
                        PRIMARY KEY (`cod_produto`),
                        UNIQUE KEY `cod_produto_UNIQUE` (`cod_produto`),
                        KEY `cod_lote_idx` (`cod_lote`),
                        CONSTRAINT `cod_lote_fk_1` FOREIGN KEY (`cod_lote`) REFERENCES `lote` (`cod_lote`)
                        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
                    """)
    # Commit
    insumos_db.commit()
    print("A tabela 'produto' foi criada.")
    conn.close()

def compra_insumo():

    conn = insumos_db.cursor()

    conn.execute("""CREATE TABLE IF NOT EXISTS `compra_insumo` (
                        `cod_compra` int NOT NULL AUTO_INCREMENT,
                        `cod_fornecedor` int NOT NULL,
                        `cod_produto` int NOT NULL,
                        `quantidade_produto` int DEFAULT NULL,
                        `data_compra` datetime NOT NULL,
                        `cnpj_loja` varchar(50) NOT NULL,
                        `tipo_pagamento` varchar(20) DEFAULT NULL,
                        `cod_funcionario` int NOT NULL,
                        PRIMARY KEY (`cod_compra`),
                        UNIQUE KEY `cod_compra_UNIQUE` (`cod_compra`),
                        UNIQUE KEY `cod_fornecedor_UNIQUE` (`cod_fornecedor`),
                        UNIQUE KEY `cod_produto_UNIQUE` (`cod_produto`),
                        UNIQUE KEY `cnpj_loja_UNIQUE` (`cnpj_loja`),
                        UNIQUE KEY `cod_funcionario_UNIQUE` (`cod_funcionario`),
                        CONSTRAINT `cnpj_loja_fk_1` FOREIGN KEY (`cnpj_loja`) REFERENCES `loja` (`cnpj_loja`),
                        CONSTRAINT `cod_fornecedor_fk_1` FOREIGN KEY (`cod_fornecedor`) REFERENCES `fornecedor` (`cod_fornecedor`),
                        CONSTRAINT `cod_funcionario_fk_1` FOREIGN KEY (`cod_funcionario`) REFERENCES `funcionario` (`cod_funcionario`),
                        CONSTRAINT `cod_produto_fk_1` FOREIGN KEY (`cod_produto`) REFERENCES `produto` (`cod_produto`)
                        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
                    """)
    # Commit
    insumos_db.commit()
    print("A tabela 'compra_insumo' foi criada.")
    conn.close()

def venda_produto():

    conn = insumos_db.cursor()

    conn.execute("""CREATE TABLE IF NOT EXISTS `venda_produto` (
                        `cod_venda` int NOT NULL AUTO_INCREMENT,
                        `cod_cliente` int DEFAULT NULL,
                        `quantidade_produto` int DEFAULT NULL,
                        `data_venda` datetime NOT NULL,
                        `cod_produto` int NOT NULL,
                        `cod_funcionario` int NOT NULL,
                        `cnpj_loja` varchar(50) NOT NULL,
                        `tipo_pagamento` varchar(20) DEFAULT NULL,
                        PRIMARY KEY (`cod_venda`),
                        UNIQUE KEY `cod_venda_UNIQUE` (`cod_venda`),
                        KEY `cod_cliente_idx` (`cod_cliente`),
                        KEY `cod_produto_FK_idx` (`cod_produto`),
                        KEY `cod_funcionario_FK_idx` (`cod_funcionario`),
                        KEY `cnpj_loja_FK_idx` (`cnpj_loja`),
                        CONSTRAINT `cnpj_loja_fk_2` FOREIGN KEY (`cnpj_loja`) REFERENCES `loja` (`cnpj_loja`),
                        CONSTRAINT `cod_cliente_fk_1` FOREIGN KEY (`cod_cliente`) REFERENCES `cliente` (`cod_cliente`),
                        CONSTRAINT `cod_funcionario_fk_2` FOREIGN KEY (`cod_funcionario`) REFERENCES `funcionario` (`cod_funcionario`),
                        CONSTRAINT `cod_produto_fk_2` FOREIGN KEY (`cod_produto`) REFERENCES `produto` (`cod_produto`)
                        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
                    """)
    # Commit
    insumos_db.commit()
    print("A tabela 'venda_produto' foi criada.")
    conn.close()
