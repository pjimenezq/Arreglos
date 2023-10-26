#Desarrollar un algoritmo que calcule el producto punto de dos arreglos de números enteros (reales) de igual tamaño.

def productoPunto(primerArreglo,segundoArreglo)->float:#función para hallar el producto punto de dos arreglos
    prodPun:int=0#Se declara e inicializa la variable como entero iniciado en 0
    for i in range(0,len(primerArreglo)):#Para el número i desde 0 hasta el tamaño de los arreglos
        prodPun+=(primerArreglo[i]*segundoArreglo[i])#Multiplicar los valores de los números encontrados en el mismo indice y sumar entre sí las multiplicaciones
    return prodPun#Se retorna el producto punto

if __name__=="__main__":#Función principal
    arregloUno=[2,5,90,43,21]#Primer arreglo
    arregloDos=[84,34,20,8,1]#Segundo arreglo
    productoPuntoFinal=productoPunto(arregloUno,arregloDos)#Se llama la función de productoPunto
    print("El producto punto de los dos arreglos es: "+ str(productoPuntoFinal))#Se imprime el producto punto
