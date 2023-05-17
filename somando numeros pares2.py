lista = [10, 2, 5, 7, 6, 3]
n = len(lista)
soma = 0
for num in lista:
    if(num%2==0):
        soma = soma+num
        print(f"O somatórios dos elementos pares da lista é: {soma}")