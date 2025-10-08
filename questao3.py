import pandas as pd
from questao2 import resultado  

def exportar_csv(pessoas: list, nome_arquivo: str):
    df = pd.DataFrame(pessoas)
    df.to_csv(nome_arquivo, index=False)
    print(f"Arquivo '{nome_arquivo}' criado com sucesso!")


exportar_csv(resultado, "pessoas.csv")
