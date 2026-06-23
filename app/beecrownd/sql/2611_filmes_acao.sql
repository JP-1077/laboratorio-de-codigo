/*
===========================================================
        2611 - FILMES DE AÇÃO
===========================================================

Objetivo: 
Uma Vídeo locadora contratou seus serviços para catalogar os filmes dela. Eles precisam que você selecione o código e o nome dos filmes cuja descrição do gênero seja 'Action'.

Tabelas:
movies
id	name	id_genres
1	Batman	3
2	The Battle of the Dark River	3
3	White Duck	1
4	Breaking Barriers	4
5	The Two Hours	2
   
genres
id	description
1	Animation
2	Horror
3	Action
4	Drama
5	Comedy
Esquema tabela:

products
Coluna	Tipo
id (PK)	numeric
name	varchar
amount	numeric
price	numeric

Exemplo saída

id	name
1	Batman
2	The Battle of the Dark River
*/


SELECT
    A.id,
    A.name
FROM movies A
INNER JOIN genres B
    ON A.id_genres = B.id
WHERE description = 'Action';
