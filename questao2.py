import pandas as pd

def criar_pessoa(nome: str, idade: int, id: int):
    pessoa = {
        "id": id,
        "nome": nome,
        "idade": idade
    }
    return pessoa


df_pessoas = pd.read_csv("pessoas.csv")  
pessoas = [criar_pessoa(row["nome"], int(row["idade"]), int(row["id"])) for _, row in df_pessoas.iterrows()]

def adicionar_gostos(pessoas: list, path_gostos_csv: str):
    
    df_gostos = pd.read_csv(path_gostos_csv)
    
    
    gostos = []
    for _, row in df_gostos.iterrows():
        gostos.append({
            "id": int(row["id"]),
            "gostos": row["gostos"].split(",")  # assume que os gostos estão separados por vírgula no CSV
        })
    
    
    for pessoa in pessoas:
        for g in gostos:
            if pessoa["id"] == g["id"]:
                pessoa["gostos"] = g["gostos"]
                break
    return pessoas[:5]


resultado = adicionar_gostos(pessoas, "gostos.csv")  # substitua pelo path correto do CSV

for pessoa in resultado:
    print(pessoa)

