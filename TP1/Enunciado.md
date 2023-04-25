# Trabajo Práctico Nro1 para la materia Algoritmos Genéticos.

## Integrantes:

- Sandoval, Julián
- Boggino, Gastón
- Milo, Marina
- García, Narela

## Enunciado

Hacer un programa que utilice un Algoritmo Genético Canónico para buscar un máximo de la función:
    
$$f(x) = \left(\frac{x}{\text{coef}}\right)^2$$

en el dominio [0, $2^{30}$ -1] 

donde coef = $2^{30}$ -1.

Teniendo en cuenta los siguientes datos:
  - Probabilidad de Crossover = 0.75
  - Probabilidad de Mutación = 0.05
  - Población Inicial: 10 individuos
  - Ciclos del programa: 20
  - Método de Selección: Ruleta
  - Método de Crossover: 1 Punto
  - Método de Mutación: invertida

El programa debe mostrar, finalmente, el Cromosoma correspondiente al valor máximo, el valor máximo, mínimo y promedio obtenido de cada población.

Mostrar la impresión de las tablas de mínimos, promedios y máximos para 20, 100 y 200 corridas.

Deben presentarse las gráficas de los valores Máximos, Mínimos y Promedios de la función objetivo por cada generación, luego de correr el algoritmo genético 20, 100 y 200 iteraciones (una gráfica por cada conjunto de iteraciones).

Realizar comparaciones de las salidas corriendo el mismo programa en distintos ciclos de corridas y además realizar todos los cambios que considere oportunos en los parámetros de entrada de manera de enriquecer sus conclusiones.
