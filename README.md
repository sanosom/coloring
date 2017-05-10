# Coloreado de grafos

## Problema

Debe diseñar un algoritmo que resuelva el problema de colorear un grafo con el menor número de colores, de manera que los nodos que están conectados no estén coloreados con el mismo color.

## Estructura de los archivos de datos

N es el número de nodos, E es el número de enlaces. Luego de estas variables aparece la lista de los enlaces, por cada línea se especifica un nodo inicial u0 y un nodo final v0.
```txt
N E
u0 v0
u1 v1
u2 v2
... ...
un vn
```

## Representación del grafo

El grafo será representado por un arreglo donde cada posición es 1 nodo, el valor de cada posición del arreglo, tendra un arreglo que representa los enlaces, donde cada posición es un enlace y su valor es el nodo con le que está enlazado

```python
[
  [v0, v1, v2, ..., vm], # Nodo 0
  [v0, v1, ..., vl], # Nodo 1
  ...,
  [v0, v1, ..., vk] # Nodo n
]
```

## Representación de los colores a usar

Los colores usados para colorear el grafo, se almacenaran en un arreglo, donde cada posición es el n-ésimo nodo y su valor es el color del nodo

```python
  [0, 1, 1]
```

## Fitness

La función ```fitness```, recibe el grafo y los colores a usar (posible solución), la función retorna el número de nodos con el mísmo color que tienen un enlace. El problema consiste en encontrar una solución con fitness 0.
