print("="*60 + "\n")

# 3. Tuplas são imutáveis

print("3. Tuplas são imutáveis\n")

tupla = ("vini", "1234567", "vinicius@gmail.com")
print(f"Tupla original: {tupla}\n")

print("Tentando alterar o primeiro elemento da tupla...")
try:
    tupla[0] = 10
except TypeError as e:
    print(f"Erro: {e}\n")

print("Tentando adicionar um elemento à tupla...")
try:
    tupla.append(6)
except AttributeError as e:
    print(f"Erro: Tuplas não têm append\n")

print("Tuplas são imutáveis, ou seja, não podem ser alteradas após a sua criação.\n")
print("Se você precisa de uma coleção mutável, considere usar uma lista em vez de uma tupla.\n")

print("="*60 + "\n")