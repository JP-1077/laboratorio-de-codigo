/*
===========================================================
        2605 - Representantes Executivos
===========================================================

Objetivo: 
Quando os dados foram migrados de Banco de Dados, houve um pequeno mal-entendido por parte do antigo DBA.

Seu chefe precisa que você exiba o código e o nome dos produtos, cuja categoria inicie com 'super'.

Tabelas:
- products
    - id (pk)
    - name
    - amount
    - price
    - id_categories


- categories
    - id (pk)
    - name
*/

SELECT Base_Produtos.id, Base_Produtos.name
FROM products Base_Produtos
JOIN categories Base_Categorias ON Base_Produtos.id_categories = Base_Categorias.id
WHERE Base_Categorias.name LIKE 'super%'