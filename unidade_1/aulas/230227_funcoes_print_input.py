# Existem funções que servem para trabalhar com entrada e saída
# de dados. As duas mais comuns são as funções print() e input().
# - print(): exibe uma informção na tela (saída de dados).
# - input(): captura uma informação digitada pelo usuário (entrada de dados).

print("Digite seu nome:")
nome: str = input()
mensagem: str = f"Olá, seja bem vindo(a) {nome}."

print(mensagem)