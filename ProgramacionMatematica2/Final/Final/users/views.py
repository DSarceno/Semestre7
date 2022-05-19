from django.http import HttpResponse
from django.shortcuts import render
from users.forms import formularioIngreso # formulario para crear html
import networkx as nx
import matplotlib.pyplot as plt



## CLASE
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
        nx.draw_networkx_edge_labels(self.grafo, pos, aristas, label_pos=0.75)

        ## se muestra el grafo
        plt.savefig('/home/diego/Documents/Trabajos/Semestre7/ProgramacionMatematica2/Final/Final/users/grafo.jpg')
        return


## VIEWS


def ingreso(request):
    if request.method == 'POST':
        formulario = formularioIngreso(request.POST)
        if formulario.is_valid(): # validar la informacion ingresada en el formulario
            infFormulario = formulario.cleaned_data # crear un diccionario con dicha informacion

            states = infFormulario['estados']
            trans = infFormulario['transicion']

            states = states.split()
            trans = trans.split()
            # creación del diccionario
            orden = []
            viniendo = ''
            for i in range(0,len(trans),3):
                tupla = (int(trans[i]), int(trans[i + 1]))
                orden.append(tupla)
                viniendo += trans[i + 2]


            dicc = dict(zip(orden, viniendo))

            graph().generador(states, dicc)

        return render(request, 'grafo.html')
    else:
        formulario = formularioIngreso()
    return render(request, 'ingreso.html',{'form':formulario}) # al ingresar al servidor, lleva a la pagina de registro
