/*
==================================
    2602 - Endereço de Clientes
==================================

Objetivo: 
A empresa fará um evento comemorando os 20 anos de mercado, e para isso faremos uma grande comemoração na cidade de Porto Alegre. 
Queremos também convidar todos os nossos clientes que estão cadastrados nessa cidade.

O seu trabalho é nos passar os nomes e os endereços dos clientes que moram em 'Porto Alegre', para entregar os convites pessoalmente.

Tabelas:
- Customers
    - id
    - name
    - street
    - city
    - state
    - credit_init


*/

SELECT name, street FROM Customers WHERE city = 'Porto Alegre'

