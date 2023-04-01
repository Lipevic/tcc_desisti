if 1==False:
    
    print('eae')
    n = 4 + 3 
    print(n)
    n1 = int(input('Qual foi meu parceiro digite n1?'))
    n2 = int(input('Degete N'))
    n3 = n1+n2 
    print('O soma entre {} e {} eh {}'.format(n1, n2, n3))
    #comentarios 


    # print('tomanucu '*100)

    from math import sqrt, pow #importanto apenas duas funções da biblioteca e não a ela toda
    n4 = sqrt(9) #raiz quadrada mas precisa importar a raiz quadrada 
    print(n4)

    #Condicionais
if 1==False:
    if 1==True:
        print('Testando condicionais')

    elif 1==True:
        print('Testando as condicionais 2')
    #Irá executar a primeira que atingir as condições entre IF(QUE ABRE) e ELIF
    else:
        print('nao vai executar mesmo.... Por enquanto')
    # and(e) ---> (condicao) and (condicao) 
    # or(ou) ----> (condicao) or  (condicao)



#repeticao
#WHILE
#estrutura do while ----------->   #while (condicao):
n10 = 0

while False: #loop inifino se for True... false nem entra no laço
    #continue ----> ele ira pular o restante da execucao naquele laco
    #break -----> para o loop e acaba a repetição
    print(n10)
    n10 +=1# == a n10= n10 +1



#FOR
#estrutura do for --------------> for (variavel) in range(start=0,(condicao),(incremento)) 
#por padrão o start vem como zero e o incremento vem como 1 precisando apenas da condicao
#prcisando apenas do range do loop ou condicao de parada
for xxx in range(10):
    print(xxx+1)
