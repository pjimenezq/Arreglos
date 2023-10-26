lista=[4,9,10,1989,13,5,-80,34]
bandera=False
while bandera==False:
    bandera==True
    for num in range(len(lista)-1):
        if lista[num]>lista[num+1]:
            bandra=False
            aux=lista[num]
            lista[num]=lista[num+1]
            lista[num+1]=aux
            
print(lista)