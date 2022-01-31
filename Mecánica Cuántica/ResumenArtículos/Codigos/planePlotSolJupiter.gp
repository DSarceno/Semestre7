#    2021-04-07
#    planePlotSolJupiter.gp
#    Diego Sarceño (dsarceno68@gmail.com)

#    Programa superficies de nivel, sistema tierra luna

#    Codificación del texto: UTF8
#    Compiladores probados: GNUPLOT (Ubuntu 20.04 Linux) 5.2
#    Instrucciones de compilación: no requere nada mas
#    gnuplot planePlotSolJupiter.gp

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
# Idioma
set encoding utf8
# terminal
set terminal pdf
set output 'planePlotSolJupiter.pdf'

# labels
set title 'Curva sobre el plano η = 0, Sistema Sol-Jupiter'
set xlabel 'ξ'
set ylabel 'V(ξ,0)'

# superficies de nivel
set size ratio 1
set grid
#set nokey




## plot
# ranges
set xrange [-1.5:1.5]
set xtics -1.5,0.3,1.5
set yrange [-1.6:-1.47]
set ytics -1.8,0.01,-1.47

# constantes
G = 6.6738E-11
Mj = 1.898E27
Ms = 1.989E30
a = 7.5E11
xi1 = Mj/(Mj + Ms)
xi2 = xi1 - 1
K = (Mj + Ms)*G/a
y = 0

plot ( xi2/sqrt((x - xi1)**2 + y**2) - xi1/sqrt((x - xi2)**2 + y**2) - 0.5*(x**2 + y**2) ) t 'V'


# END PROGRAM
