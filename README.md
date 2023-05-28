# **Proyecto Integrador: Programa de Algoritmos de Búsqueda**

---

## **Enunciado**

Este proyecto consiste en crear un programa que implemente diferentes algoritmos de búsqueda en una variedad de estructuras de datos, como listas, árboles o grafos. Los usuarios que manipulen el programa, pueden ingresar un elemento que desean buscar, y este les mostrará la ubicación del elemento en la estructura de datos.

Este proyecto puede ser implementado tanto con una interfaz gráfica como por consola. Si se desea una interfaz gráfica, se pueden utilizar herramientas como PyQT o Tkinter.

---

# **Investigacion**

## **Búsqueda lineal (Linear search)**

El algoritmo de búsqueda lineal (también conocido como búsqueda secuencial) es un método sencillo y básico para encontrar un valor específico en una lista o arreglo de elementos. 

Consiste en recorrer la lista elemento por elemento, comparando cada uno con el valor buscado, hasta encontrar una coincidencia. Si se llega al final de la lista sin encontrar el valor, se considera que el valor no está presente en la lista.

El algoritmo de búsqueda lineal puede ser implementado utilizando un bucle `for` para recorrer la lista, y una estructura condicional `if` para comparar cada elemento con el valor buscado.

A continuación se presenta un ejemplo en Python de cómo implementar el algoritmo de búsqueda lineal para encontrar un valor específico en una lista:

```python
def busqueda_lineal(lista, valor):
    for i in range(len(lista)):
        if lista[i] == valor:
            return i  # Retorna el índice del elemento encontrado
    return -1  # Retorna -1 si el elemento no está en la lista
```

En este ejemplo, la función `busqueda_lineal` recibe como parámetros la lista en la que se va a buscar el valor y el valor que se desea encontrar. La función utiliza un bucle `for` para recorrer la lista y una estructura condicional `if` para comparar cada elemento con el valor buscado. Si el valor se encuentra en la lista, la función retorna el índice del elemento encontrado. Si el valor no está presente en la lista, la función retorna `-1`.




## **Búsqueda binaria (Binary search)**

La búsqueda binaria, también conocida como búsqueda en mitad o búsqueda logarítmica, es un algoritmo eficiente para buscar un valor específico en una lista ordenada de elementos. A diferencia de la búsqueda lineal, que recorre la lista elemento por elemento, la búsqueda binaria divide repetidamente la lista en dos mitades y compara el valor buscado con el valor del elemento central. De esta manera, descarta la mitad de la lista en cada iteración, lo que permite encontrar el valor deseado de manera más rápida.

A continuación, se explica en detalle cómo funciona la búsqueda binaria:

1. La lista debe estar ordenada en orden ascendente o descendente para que la búsqueda binaria funcione correctamente.

2. El algoritmo comienza calculando el índice central de la lista, que se obtiene dividiendo la longitud de la lista entre 2. Si la longitud de la lista es par, se elige el elemento anterior al punto medio.

3. Se compara el valor buscado con el valor del elemento central de la lista. Si son iguales, se ha encontrado el valor buscado y se retorna su índice.

4. Si el valor buscado es menor que el valor del elemento central, se realiza la búsqueda solo en la mitad inferior de la lista (es decir, desde el inicio hasta el elemento central - 1), descartando la mitad superior.

5. Si el valor buscado es mayor que el valor del elemento central, se realiza la búsqueda solo en la mitad superior de la lista (es decir, desde el elemento central + 1 hasta el final), descartando la mitad inferior.

6. Se repiten los pasos 2-5 hasta que se encuentre el valor buscado o hasta que la lista se reduzca a un tamaño de 0, lo que indica que el valor buscado no está presente en la lista.

El algoritmo de búsqueda binaria es muy eficiente, ya que reduce a la mitad la cantidad de elementos a considerar en cada iteración. En comparación con la búsqueda lineal, que tiene una complejidad de tiempo de O(n), la búsqueda binaria tiene una complejidad de tiempo de O(log n), lo que la hace especialmente útil para listas grandes.

Es importante tener en cuenta que la búsqueda binaria solo se aplica a listas ordenadas. Si la lista no está ordenada, es necesario ordenarla antes de utilizar la búsqueda binaria.





## **Búsqueda por interpolación (Interpolation search)**

La búsqueda por interpolación es un algoritmo de búsqueda que se utiliza para encontrar un valor específico en una lista ordenada. A diferencia de la búsqueda binaria, que divide la lista en mitades iguales, la búsqueda por interpolación estima la posición del valor buscado utilizando una fórmula basada en la distribución de los valores en la lista.

El algoritmo de búsqueda por interpolación sigue los siguientes pasos:

1. La lista debe estar ordenada de forma ascendente o descendente para que la búsqueda por interpolación funcione correctamente.

2. Se toma el valor mínimo y máximo de la lista, y se calcula la fracción lineal aproximada que representa la posición del valor buscado. Esto se realiza utilizando la siguiente fórmula:

   ```python
   posicion = inicio + ((fin - inicio) // (lista[fin] - lista[inicio])) * (valor - lista[inicio])
   ```

   Donde:
   - `inicio` es el índice del primer elemento de la lista.
   - `fin` es el índice del último elemento de la lista.
   - `lista[fin] - lista[inicio]` es la diferencia en valores entre el primer y último elemento.
   - `valor` es el valor buscado.

3. Se compara el valor estimado (`lista[posicion]`) con el valor buscado. Si son iguales, se ha encontrado el valor buscado y se retorna la posición.

4. Si el valor buscado es menor que `lista[posicion]`, la búsqueda se realiza en la sublista que va desde `inicio` hasta `posicion - 1`. Si es mayor, la búsqueda se realiza en la sublista que va desde `posicion + 1` hasta `fin`.

5. Se repiten los pasos 2-4 hasta que se encuentre el valor buscado o hasta que la sublista se reduzca a un tamaño de 0, lo que indica que el valor buscado no está presente en la lista.

La búsqueda por interpolación se basa en la suposición de que los elementos en la lista están uniformemente distribuidos. Sin embargo, si la distribución de los valores no es uniforme, el rendimiento de la búsqueda por interpolación puede verse afectado y puede no ser tan eficiente como la búsqueda binaria. Además, es importante tener en cuenta que la búsqueda por interpolación solo se aplica a listas ordenadas. Si la lista no está ordenada, es necesario ordenarla antes de utilizar la búsqueda por interpolación.





## **Búsqueda por salto (Jump search)**

La búsqueda por salto (Jump search) es un algoritmo de búsqueda que se utiliza para encontrar un valor específico en una lista ordenada. A diferencia de la búsqueda lineal o binaria, que exploran los elementos uno por uno o dividen la lista en mitades, la búsqueda por salto salta a través de la lista en pasos fijos.

A continuación se explica en detalle cómo funciona la búsqueda por salto:

1. La lista debe estar ordenada en orden ascendente o descendente para que la búsqueda por salto funcione correctamente.

2. Se elige un tamaño de salto (`step`) apropiado. Normalmente, se elige un tamaño de salto igual a la raíz cuadrada de la longitud de la lista, por ejemplo, `step = int(math.sqrt(len(lista)))`.

3. Se realiza un salto desde el inicio de la lista hasta el primer elemento cuyo valor es mayor o igual al valor buscado.

4. Se realiza una búsqueda lineal dentro de la porción de la lista cubierta por el salto anterior. Esto se hace para verificar si el valor buscado está presente en la lista.

5. Si se encuentra el valor buscado, se retorna su posición. Si el valor buscado es menor que el elemento encontrado, se realiza una búsqueda lineal desde el elemento anterior al actual para obtener la posición exacta del valor buscado.

6. Si se llega al final de la lista sin encontrar el valor buscado, se considera que el valor no está presente.

La búsqueda por salto es útil cuando la lista es grande y está ordenada, ya que permite saltar a través de elementos en lugar de recorrerlos uno por uno. Sin embargo, la búsqueda por salto no supera la eficiencia de la búsqueda binaria. En términos de complejidad temporal, la búsqueda por salto tiene una complejidad de O(√n), donde n es la longitud de la lista.

Es importante tener en cuenta que la búsqueda por salto solo se aplica a listas ordenadas. Si la lista no está ordenada, es necesario ordenarla antes de utilizar la búsqueda por salto.
