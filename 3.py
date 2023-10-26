#Hacer un algoritmo que deje al final de un arreglo de números todos los ceros que aparezcan en dicho arreglo.
def cerosLista(lista)->int:#Función para contar los ceros que aparecen en un arreglo
    return lista.count(0)#Se retorna las veces que el elemento 0 se encuentra en la lista

if __name__=="__main__":#Función principal
    miLista = [45,38,0,0,24,1,2,0]#Arreglo de reales
    conteo=cerosLista(miLista)#Se llama la función cerosLista
    print("Los ceros que aparecen en el arreglo son " +str(conteo))#Se imprime la cantidad de ceros que hay en el arreglo




