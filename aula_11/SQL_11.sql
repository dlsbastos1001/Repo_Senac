USE CARAMELO;

CREATE TABLE tb_clientes(
	id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR (100),
    data_nascimento DATE,
    sexo VARCHAR(100),
    email VARCHAR(100),
    telefone VARCHAR(100),
    cidade VARCHAR(100),
    estado VARCHAR(100),
    cadastro DATE);
        
    SELECT * FROM tb_clientes;
    
CREATE TABLE produtos(
	id INT PRIMARY KEY AUTO_INCREMENT,
    nome_produto VARCHAR (100),
    categoria VARCHAR(100),
    subcategoria VARCHAR(100),
    marca VARCHAR(100),
    preco_unitario DECIMAL (10,2));
    
LOAD DATA INFILE 'C:/Users/danilo.bastos/Documents/Repo_Senac/aula_11/tb_produtos.csv'
INTO TABLE produtos
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(nome_produto, categoria, subcategoria, marca, preco_unitario);
    
SELECT * FROM produtos;
    
    
CREATE TABLE vendas(  
    id_venda INT PRIMARY KEY,
    data_venda DATE,
    id_cliente INT,
    id_produto INT,
    quantidade INT,
    forma_pagamento VARCHAR(100),
    canal_venda VARCHAR(100),
    FOREIGN KEY (id_cliente) REFERENCES tb_clientes(id),
    FOREIGN KEY (id_cliente) REFERENCES tb_clientes(id));
    
SELECT * FROM  vendas;

SET GLOBAL local_infile = 1;




LOAD DATA INFILE 'C:/Users/danilo.bastos/Documents/Repo_Senac/aula_11/tb_clientes.csv'
INTO TABLE tb_clientes
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(nome,data_nascimento,sexo,email,telefone,cidade,estado,cadastro);
    


LOAD DATA INFILE 'C:/Users/danilo.bastos/Documents/Repo_Senac/aula_11/tb_vendas.csv'
INTO TABLE vendas
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\N'
IGNORE 1 ROWS
(id_venda, data_venda, id_cliente, id_produto, quantidade, forma_pagamento, canal_venda);
   
   
   
drop table vendas;
drop table produtos; 
drop table tb_clientes;
    

select * from vendas;
select * from produtos;
select * from tb_clientes;




##########################################################################################################################################################################################################################################
SELECT quantidade, forma_pagamento
FROM  vendas
ORDER BY forma_pagamento DESC;


























































































































