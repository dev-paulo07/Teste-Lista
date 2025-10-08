# Lista de Exercícios Python

Este repositório contém 5 exercícios em Python, cada um em um arquivo separado:

- `questao1.py` — Criar objetos Pessoa.
- `questao2.py` — Adicionar gostos às pessoas.
- `questao3.py` — Exportar lista de pessoas para CSV.
- `questao4.py` — Ordenar uma lista de números.
- `questao5.py` — Retornar os 3 maiores números de uma lista.

Com base na atividade teste 08/10/2025:

Questão 1 — Criar um objeto Pessoa
Crie uma função chamada criar_pessoa(nome: str, idade: int, id: int) que retorna um objeto (dicionário) representando uma pessoa, com os atributos id, nome e idade.

Requisitos:

A função deve retornar um dicionário Python.

O dicionário deve conter exatamente as chaves: "id", "nome", "idade".

Exemplo de Entrada:

p1 = criar_pessoa("Marcos", 28, 1)
p2 = criar_pessoa("Ana", 24, 2)
p3 = criar_pessoa("Carlos", 30, 3)
print(p1)
Saída Esperada:

{'id': 1, 'nome': 'Marcos', 'idade': 28}
Questão 2 — Selecionar e combinar gostos das pessoas
Crie uma função chamada adicionar_gostos(pessoas: list, gostos: list) que:

Recebe uma lista de objetos pessoa (como os criados na questão anterior).

Recebe uma lista de objetos de gostos, cada um no formato {"id": int, "gostos": list[str]}.

Retorna as 5 primeiras pessoas, acrescentando a cada pessoa um novo campo "gostos", com base no id.

Exemplo de Entrada:

pessoas = [
    criar_pessoa("Marcos", 28, 1),
    criar_pessoa("Ana", 24, 2),
    criar_pessoa("Carlos", 30, 3),
    criar_pessoa("Julia", 22, 4),
    criar_pessoa("Pedro", 27, 5),
    criar_pessoa("Laura", 26, 6)
]

gostos = [
    {"id": 1, "gostos": ["Música", "Futebol"]},
    {"id": 2, "gostos": ["Leitura", "Cinema"]},
    {"id": 3, "gostos": ["Viagem"]},
    {"id": 4, "gostos": ["Dança", "Esportes"]},
    {"id": 5, "gostos": ["Tecnologia", "Culinária"]},
    {"id": 6, "gostos": ["Moda"]}
]
##entrada deve ser os arquivos .csv anteriormente citados.
resultado = adicionar_gostos(pessoas, gostos)
print(resultado)
Saída Esperada (primeiras 5 pessoas com gostos correspondentes):

[
    {'id': 1, 'nome': 'Marcos', 'idade': 28, 'gostos': ['Música', 'Futebol']},
    {'id': 2, 'nome': 'Ana', 'idade': 24, 'gostos': ['Leitura', 'Cinema']},
    {'id': 3, 'nome': 'Carlos', 'idade': 30, 'gostos': ['Viagem']},
    {'id': 4, 'nome': 'Julia', 'idade': 22, 'gostos': ['Dança', 'Esportes']},
    {'id': 5, 'nome': 'Pedro', 'idade': 27, 'gostos': ['Tecnologia', 'Culinária']}
]
Questão 3 — Converter lista em DataFrame e exportar CSV
Crie uma função chamada exportar_csv(pessoas: list, nome_arquivo: str) que:

Recebe a lista de pessoas (com os gostos incluídos, da questão anterior).

Converte essa lista em um DataFrame do pandas.

Exporta o resultado para um arquivo CSV com o nome especificado.

Exemplo de Entrada:

exportar_csv(resultado, "pessoas.csv")
Saída Esperada:
Um arquivo chamado pessoas.csv com o conteúdo:

id,nome,idade,gostos
1,Marcos,28,"['Música', 'Futebol']"
2,Ana,24,"['Leitura', 'Cinema']"
3,Carlos,30,"['Viagem']"
4,Julia,22,"['Dança', 'Esportes']"
5,Pedro,27,"['Tecnologia', 'Culinária']"
Questão 4 — Ordenar uma lista de números
Crie uma função chamada ordenar_lista(numeros: list[int]) que receba uma lista de números inteiros aleatórios e retorne a lista ordenada em ordem crescente.

Exemplo de Entrada:

lista = [42, 12, 9, 73, 51, 22]
resultado = ordenar_lista(lista)
print(resultado)
Saída Esperada:

[9, 12, 22, 42, 51, 73]
Questão 5 — Ordenar lista e retornar os 3 maiores números
Crie uma função chamada top_tres_maiores(numeros: list[int]) que:

Receba uma lista de números inteiros.

Retorne os 3 maiores números em ordem decrescente.

Exemplo de Entrada:

lista = [5, 42, 12, 9, 73, 51, 22]
resultado = top_tres_maiores(lista)
print(resultado)
Saída Esperada:

[73, 51, 42]
