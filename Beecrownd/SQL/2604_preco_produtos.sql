/*
==================================
    2603 - Preço Produtos
==================================

Objetivo: 
O setor financeiro da empresa precisa de um relatório que mostre o código e o nome dos produtos cujo preço são menores que 
10 ou maiores que 100.

Tabelas:
- products
    - id
    - name
    - amount
    - price


*/

SELECT id, name FROM products WHERE price < 10 OR price > 100