# Criando uma lista vazia
lst = []
pos = []
n = int(input("Insira o tamanho da lista de números inteiros: "))
cont = 0

for i in range(n):
    ele = int(input('Insira o {}º número da lista = '.format(i+1)))
    
    #adicionando o elemento
    lst.append(ele)

# o que eu quero?
# comparar o valor atual da lista com todos os outros valores

# problema: como posso comparar

for i in range(n):
    for j in range(n):
        if i != j: # para não fazer nada se estivermos analisando o número com ele mesmo
            if lst[i] == lst[j]:
                #print(lst[i], "é igual a", lst[j])
                cont += 1
                pos.append(lst[i])
            else:
                pass
                #print(lst[i], "não é igual a", lst[j])
        else:
            pass

print("No total, tivemos", cont, "números repetidos, sendo eles", pos)
