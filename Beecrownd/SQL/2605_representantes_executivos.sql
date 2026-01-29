/*
===========================================================
        2605 - Representantes Executivos
===========================================================

Objetivo: 
O setor financeiro precisa de um relatório sobre os fornecedores dos produtos que vendemos. Os relatórios contemplam 
todas as categorias, mas por algum motivo, os fornecedores dos produtos cuja categoria é a executiva, não estão no 
relatório.

Seu trabalho é retornar os nomes dos produtos e dos fornecedores cujo código da categoria é 6.

Tabelas:
- products
    - id (pk)
    - name
    - amount
    - price
    - id_providers
    - id_categories


- categories
    - id (pk)
    - name

- providers
    - id (pk)
    - name
    - street
    - city
    - state

*/

SELECT Base_Produtos.name, Base_Fornecedores.name
FROM products Base_Produtos
JOIN categories Base_Categorias ON Base_Produtos.id_categories = Base_Categorias.id
JOIN providers Base_Fornecedores ON Base_Produtos.id_providers = Base_Fornecedores.id
WHERE Base_Categorias.id = 6