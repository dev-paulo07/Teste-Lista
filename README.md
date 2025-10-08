# Lista de Exercícios Python

Este repositório contém 5 exercícios em Python, cada um em um arquivo separado:

- `questao1.py` — Criar objetos Pessoa.
- `questao2.py` — Adicionar gostos às pessoas.
- `questao3.py` — Exportar lista de pessoas para CSV.
- `questao4.py` — Ordenar uma lista de números.
- `questao5.py` — Retornar os 3 maiores números de uma lista.

Com base na atividade teste 08/10/2025:

---

## Questão 1 — Criar um objeto Pessoa

Crie uma função chamada `criar_pessoa(nome: str, idade: int, id: int)` que retorna um objeto (dicionário) representando uma pessoa, com os atributos `id`, `nome` e `idade`.

**Requisitos:**

- A função deve retornar um dicionário Python.
- O dicionário deve conter exatamente as chaves: `"id"`, `"nome"`, `"idade"`.

**Exemplo de Entrada:**

```python
p1 = criar_pessoa("Marcos", 28, 1)
p2 = criar_pessoa("Ana", 24, 2)
p3 = criar_pessoa("Carlos", 30, 3)
print(p1)
