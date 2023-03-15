# Crie um programa que peça três notas e exiba a média
# aritmética e se o aluno foi aprovado ou reprovado.

nota_1 = float(input("Primeira nota: "))
nota_2 = float(input("Segunda nota: "))
nota_3 = float(input("Terceira nota: "))
soma: float = nota_1 + nota_2 + nota_3
media: float = soma/3

if media >= 5.0:
    print(f"Média {media:.1f}. Você foi aprovado!")
else:
    print(f"Média {media:.1f}. Você foi reprovado!")