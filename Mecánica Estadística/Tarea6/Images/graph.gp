#    2022-05-23
#    graph.gp
#    Diego Sarceño (dsarceno68@gmail.com)

#    Gráficas Cohete Ah Mun

#    Codificación del texto: UTF8
#    Compiladores probados: GNUPLOT (Ubuntu 20.04 Linux) 5.2
#    Instrucciones de compilación: no requere nada mas
#    gnuplot graph.gp

# PROGRAM
# Idioma
set encoding utf8
# terminal
unset label
clear
set terminal pdf
set output "omega.pdf"
set grid
#unset tics
set title "Función Espectral μ(ω)"
#set ytics nomirror # para desligar los 2 ejes y
#set y2tics # 2 ejes y
set xlabel "Temperatura"
set ylabel "Función"
set key left top box

## TEMPERATURAS
T1 = 200
T2 = 250
T3 = 300

f11(x) = (x**3)/(exp(x/T1) - 1)
f12(x) = (x**3)/(exp(x/T2) - 1)
f13(x) = (x**3)/(exp(x/T3) - 1)

# se plotean los dos conjuntos de datos en una sola grafica, pero con ejes
# y's independientes.
plot f11(x) lc "blue" t "T = 200K", f12(x) lc "green" t "T = 250K", f13(x) lc "black" t "T = 300K"


# terminal
unset label
clear
set terminal pdf
set output "nu.pdf"
set grid
#unset tics
set title "Función Espectral μ(ν)"
#set ytics nomirror # para desligar los 2 ejes y
#set y2tics # 2 ejes y
set xlabel "Temperatura"
set ylabel "Función"
set key left top box


f21(x) = (x**3)/(exp(x/T1) - 1)
f22(x) = (x**3)/(exp(x/T2) - 1)
f23(x) = (x**3)/(exp(x/T3) - 1)

# se plotean los dos conjuntos de datos en una sola grafica, pero con ejes
# y's independientes.
plot f21(x) lc "blue" t "T = 200K", f22(x) lc "green" t "T = 250K", f23(x) lc "black" t "T = 300K"


# terminal
unset label
clear
set terminal pdf
set output "lambda.pdf"
set grid
#unset tics
set title "Función Espectral μ(λ)"
#set ytics nomirror # para desligar los 2 ejes y
#set y2tics # 2 ejes y
set xlabel "Temperatura"
set ylabel "Función"
set key left top box


f31(x) = 1/((x**3)*(exp(1/(x*T1)) - 1))
f32(x) = 1/((x**3)*(exp(1/(x*T2)) - 1))
f33(x) = 1/((x**3)*(exp(1/(x*T3)) - 1))

# se plotean los dos conjuntos de datos en una sola grafica, pero con ejes
# y's independientes.
plot f31(x) lc "blue" t "T = 200K", f32(x) lc "green" t "T = 250K", f33(x) lc "black" t "T = 300K"





























#
