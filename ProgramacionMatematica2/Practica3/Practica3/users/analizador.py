#    2021-04-28
#    analizador.py
#    Diego Sarceño (dsarceno68@gmail.com)

#    Clases de lectura, escritura (en HTML) de un archivo con extención
#    '.p2', así como el análisis léxico de dicho documento; representando
#    enteros, reales, complejos, números en notación científica, fechas y 
#    palabras clave. El análisis se realiza en base al módulo de python
#    "regex" el cual se basa en expresiones regulares.

#    Codificación del texto: UTF8
#    Compiladores probados: Python (Ubuntu 20.04 Linux) 3.8.5
#    Instrucciones de importación: requiere módulo regex.
#    from analizador import File_reading, File_writing, Analizador

#    Copyright (C) 2021
#    D. R. Sarceño Ramírez
#    dsarceno68@gmail.com
#
#    This program is free software: you can redistribute it and/or
#    modify it under the terms of the GNU General Public License as
#    published by the Free Software Foundation, either version 3 of
#    the License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#    General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see
#    <http://www.gnu.org/licenses/>.

# PROGRAM

# FALTA DARLE FORMATO DE CLASE!!!!
import re # librería para el manejo de expresiones regulares.


class File_reading: # Lectura de archivo de texto extensión ".p2"
    def __init__(self):
        self.texto = []

    def lectura(self,name):
        if name[len(name) - 2:len(name)] == 'p2':
            file = open(name,'r')
            text = [line.split() for line in file]
            file.close()
            if len(text) == 1:
                self.texto = text[0]
            else:
                for i in range(len(text)):
                    self.texto += text[i]
            return self.texto		# Devuelve una lista con elementos como las palabras.
        else:
            print('Tipo de archivo no aceptado.')


class File_writing:
    def __init__(self):
        self.name = 'texto_analizado.html'
        # escritura del archivo .html secillo
        self.encabezado_html = '<!DOCTYPE html> \n \
        <html lang="en" dir="ltr"> \n \
          <head> \n \
            <meta charset="utf-8"> \n \
            <title>Prueba</title> \n \
          </head> \n \
          <body> \n \
          <div style="text-align:center"> \n \
          <h1>Texto Analizado</h1>'
        self.pie_html = '</div> \n \
            </body> \n \
            </html>'

    def escritura(self,texto): # recibe el texto analizado por medio de un string.
        if type(texto) == str:
            file = open(self.name,'w')
            file.write(self.encabezado_html)
            file.write(texto)
            file.write(self.pie_html)
            file.close()
        return



class Analizador:
    def __init__(self):
        self.fechas = '-?\d+[/-]\d+[/-]\d+\.?\d*'	# fechas, aceptadas en ambos formatos, guiones y slash.
        self.enteros = '(^|.)\d+($|.)'	# enteros.
        self.reales = '(^|.)\d+[.]\d+($|.)'	# reales.
        self.cientificas = '(^|.)(\d+[.]\d+|\d+)[E]-?\d+($|.)'	# notación científica aceptada con la "E"
        self.complejos = '^(\d+[.]\d+|\d+)[+-](\d+[.]\d+|\d+)[i]($|.)'	# números complejos en notación z = a + bi
        self.palabras_clave = '[,.\s]?(Teorema|Matemática|Matemático|Hilbert|Turing|Análisis|Euler|Fermat|Pitágoras|Autómata|Boole|Cantor|Perelman|Experimentación|Físico|Física|Astronomía|Mecánica|Newton|Einstein|Galileo|Modelo|Tesla|Dinámica|Partículas)[,.\s?]'	# Palabras clave a buscar relacionadas con física y matemática.


    def analizar(self,texto_splitted):
        if type(texto_splitted) == list:
            texto_fechas = [] # para almacenar el texto con fechas analizadas
            for i in range(len(texto_splitted)):
                fecha = re.match(self.fechas, texto_splitted[i])
                if fecha != None: # si encuentra una fecha le añade el código
                    texto_fechas.append('<font color="orange">' + texto_splitted[i] + '</font>')
                else: # sino, simplemente añade la palabra
                    texto_fechas.append(texto_splitted[i])
		# esto se realiza para cada expresión regular.	
            texto_enteros = []
            for i in range(len(texto_fechas)):
                entero = re.match(self.enteros,texto_fechas[i])
                if entero != None:
                    texto_enteros.append('<font color="blue">' + texto_fechas[i] + '</font>')
                else:
                    texto_enteros.append(texto_fechas[i])

            texto_reales = []
            for i in range(len(texto_enteros)):
                real = re.match(self.reales,texto_enteros[i])
                if real != None:
                    texto_reales.append('<font color="green">' + texto_enteros[i] + '</font>')
                else:
                    texto_reales.append(texto_enteros[i])

            texto_cientificas = []
            for i in range(len(texto_reales)):
                cientific = re.match(self.cientificas,texto_reales[i])
                if cientific != None:
                    texto_cientificas.append('<font color="purple">' + texto_reales[i] + '</font>')
                else:
                    texto_cientificas.append(texto_reales[i])

            texto_complejos = []
            for i in range(len(texto_cientificas)):
                complex = re.match(self.complejos,texto_cientificas[i])
                if complex != None:
                    texto_complejos.append('<font color="red">' + texto_cientificas[i] + '</font>')
                else:
                    texto_complejos.append(texto_cientificas[i])

            texto_palabras_clave = []
            for i in range(len(texto_complejos)):
                keywords = re.match(self.palabras_clave,texto_complejos[i],re.IGNORECASE)
                if keywords:
                    texto_palabras_clave.append('<font color="gray">' + texto_complejos[i] + '</font>')
                else:
                    texto_palabras_clave.append(texto_complejos[i])
            return ' '.join(texto_palabras_clave)
        else:
            print('Objeto no analizable')
            return




























# END
