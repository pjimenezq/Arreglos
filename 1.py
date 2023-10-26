#Desarrollar un algoritmo que calcule el promedio de un arreglo de reales.

def promedio(lista)->float:#función para hallar promedio de un arreglo
        suma:int=0#Se declara la variable suma que se inicializa en 0
        for i in lista:#Para cada elemento i de la lista
                suma+=i#...se hace la suma de este elemento a la variable suma
        elPromedio=suma/(len(lista))#Para encontrar el promedio se divide la suma de todos los elementos entre la cantidad de elementos que tiene la lista
        return elPromedio#Se retorna el promedio
if __name__=="__main__":#Función principal
    miLista = [10.5,5,1.2,9.2,8,3.1,12]#Arreglo de reales
    promedioTotal=promedio(miLista)#Se llama la función de promedio
    print("El promedio del arreglo es " +str(promedioTotal))#Se imprime el promedio del arreglo
