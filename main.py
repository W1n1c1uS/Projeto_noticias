binario = str(input('Digite um numero binario'))
binario = binario[::-1]
contador=0
lista=[]
for i in range(len(binario)):
    lista.append(i)


#print(lista)
lista2=[]
for b in binario:
    decimal=int(b)
    lista2.append(decimal*2)

for i in lista:
    a = i
    for b in lista2:
        c = a ** b
        print(c)

    #print(conversao)

#print(lista)
#print(lista3)


#if (decimal == 1):
    #for a in lista:
        #conversao = decimal ** a
        #print(conversao)
        #print(b)
        #if ( int(b) == 1):

            #contador += i ** 2
    #potencia = int(i) * contador

            #print(contador)
        #print(potencia)
    #if (i == 1):
        #conversao = i ** 2
        #contador += 1
        #aumentar_mais_1 = contador ** 2
        #decimal = i ** aumentar_mais_1

        #print(i)
        #soma += conversao * 2



