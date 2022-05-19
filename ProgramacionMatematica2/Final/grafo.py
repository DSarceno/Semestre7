import networkx as nx
import matplotlib.pyplot as plt


class graph:
    def __init__(self):
        self.grafo = nx.MultiDiGraph()

    def generador(self, nodos, aristas):
        # creando los nodos del afd
        self.grafo.add_nodes_from(nodos)

        # aristas
        self.grafo.add_edges_from(aristas.keys())


        ## codigo para poner bonito el grafo (spring)
        pos = nx.circular_layout(self.grafo)

        for u, v, d in self.grafo.edges(data=True):
            d['weight'] = 3

        edges, weights = zip(*nx.get_edge_attributes(self.grafo, 'weight').items())


        ## mostrar los nodos con formato bonito
        nx.draw(self.grafo, pos, node_color='lightgreen', edge_color=weights, width=2, with_labels=True)

        ## mostrar las aristas con formato
        #nx.draw_networkx_edges(self.grafo, pos, edgelist = aristas.keys(), arrowstyle="<|-", style="dashed")
        nx.draw_networkx_edge_labels(self.grafo, pos, aristas, label_pos=0.75)

        ## se muestra el grafo
        plt.savefig('grafo.png')
        plt.show()
        return
