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

print(p1)
print(p2)
print(p3)
