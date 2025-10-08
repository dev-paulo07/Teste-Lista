def criar_pessoa(nome: str, idade: int, id: int):
    pessoa = {
        "id": id,
        "nome": nome,
        "idade": idade
    }
    return pessoa


p1 = criar_pessoa("Paulo", 18, 1)
p2 = criar_pessoa("Dudu", 18, 2)
p3 = criar_pessoa("Eric", 19, 3)
p4 = criar_pessoa("Pereira", 18, 4)
p5 = criar_pessoa("Nolasco", 18, 5)
p6 = criar_pessoa("José", 18, 6)

pessoas = [p1, p2, p3, p4, p5, p6]


def adicionar_gostos(pessoas: list, gostos: list):
    for pessoa in pessoas:
        for g in gostos:
            if pessoa["id"] == g["id"]:
                pessoa["gostos"] = g["gostos"]
                break
    return pessoas[:5]

gostos = [
    {"id": 1, "gostos": ["Corrida", "Guitarra"]},
    {"id": 2, "gostos": ["Festa", "Leitura"]},
    {"id": 3, "gostos": ["Futebol"]},
    {"id": 4, "gostos": ["Basquete", "Jogos"]},
    {"id": 5, "gostos": ["Viagem", "Carros"]},
    {"id": 6, "gostos": ["Cinema"]}
]

resultado = adicionar_gostos(pessoas, gostos)

for pessoa in resultado:
    print(pessoa)