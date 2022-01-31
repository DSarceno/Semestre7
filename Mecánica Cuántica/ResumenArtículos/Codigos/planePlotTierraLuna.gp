#    2021-04-07
#    planePlotTierraLuna.gp
#    Diego Sarceño (dsarceno68@gmail.com)

#    Programa superficies de nivel, sistema tierra luna

#    Codificación del texto: UTF8
#    Compiladores probados: GNUPLOT (Ubuntu 20.04 Linux) 5.2
#    Instrucciones de compilación: no requere nada mas
#    gnuplot planePlotTierraLuna.gp

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
set output 'planePlotTierraLuna.pdf'

# labels
set title 'Curva sobre el plano η = 0, Sistema Tierra-Luna'
set xlabel 'ξ'
set ylabel 'V(ξ,0)'

# superficies de nivel
set size ratio 0.8
set grid
#set nokey




## plot
# ranges
set xrange [-2:2]
set xtics -2,0.3,2
set yrange [-5:-1]
set ytics -5,0.2,-1

# constantes
G = 6.6738E-11
Me = 5.972E24
Ml = 7.349E22
a = 3.844E8
xi1 = Ml/(Me + Ml)
xi2 = xi1 - 1
K = (Me + Ml)*G/a
y = 0

plot ( xi2/sqrt((x - xi1)**2 + y**2) - xi1/sqrt((x - xi2)**2 + y**2) - 0.5*(x**2 + y**2) ) t 'V'


# END PROGRAM
