set terminal pdf
set output "histograma.pdf"

binwidth = 0.8
set boxwidth binwidth

set xlabel "Caras del Dado"
set yrange [0:6000]
set ylabel "Frecuencia"

plot 50*100 with dots lc "black" t "Media Esperada",\
	 "datos.dat" using :2 with boxes lc "blue" t "Simulado"
