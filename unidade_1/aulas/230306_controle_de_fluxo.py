# Controle de fluxo utilizando if else. Essa estrutura de controle
# permite que o programa tome decisões lógicas baseado em condições.

nota_1: float = 5.8
nota_2: float = 8.1

print(nota_1)
print(nota_2)

if nota_1 < nota_2:
    print(f"A maior nota é a primeira ({nota_1}).")
else:
    print(f"A maior nota é a segunda ({nota_2}).")