from grafo import graph

nodos = [1,2,3,4,5]
aristas = {
    (1,2): "d",
    (2,1): "d",
    (2,3): ".",
    (3,4): "d",
    (4,5): "i",
    (5,5): "d"
}

graph().generador(nodos, aristas)
