# Reto 10: Arreglos y listas
**Instrucciones**

Para cada punto cree un programa individual. Al finalizar suba todo a un repo y subalo al canal reto_10 en slack.
## Punto uno

Desarrollar un algoritmo que calcule el promedio de un arreglo de reales.

**Código**
```
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

```
## Punto dos

Desarrollar un algoritmo que calcule el producto punto de dos arreglos de números enteros (reales) de igual tamaño.

**Código**
```
```
## Punto tres

Hacer un algoritmo que deje al final de un arreglo de números todos los ceros que aparezcan en dicho arreglo.

**Código**
```
def cerosLista(lista)->int:#Función para contar los ceros que aparecen en un arreglo
    return lista.count(0)#Se retorna las veces que el elemento 0 se encuentra en la lista

if __name__=="__main__":#Función principal
    miLista = [45,38,0,0,24,1,2,0]#Arreglo de reales
    conteo=cerosLista(miLista)#Se llama la función cerosLista
    print("Los ceros que aparecen en el arreglo son " +str(conteo))#Se imprime la cantidad de ceros que hay en el arreglo
```

## Punto cuatro

Revisar que son los algoritmos de sorting, entender bubble-sort.

El _algoritmo de sorting_, está diseñado para cumplir con la función de colocar números o letras en orden.

_Bubble Sort_ es el más simple algoritmo de sorting. Funciona repetidamente, intercambiando los elementos adyacentes cuando están en el orden incorrecto.

Cuando se busca ordenar la lista de forma ascendente el algoritmo empieza con el elemento de la izquierda, comparándolo con el de al lado y ubicando el mayor al lado derecho. De esta manera, el mayor elemento termina en la derecha. Se repite el procedimiento hasta que todos los datos están ordenados.

**Código**
```
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
```

