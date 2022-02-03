set terminal pdf
set output "histograma.pdf"

binwidth = 0.8
set boxwidth binwidth

expected_mean = 16.666666*100 # 100/6 multiplicado por el número de simulaciones independientes 
set xlabel "Caras del Dado"
set yrange [0:5000]
set ylabel "Frecuencia"


plot 16.6666667*100 with dots lc "black" t "Media esperada",\
	 "datos.dat" using :2 with boxes lc "blue" t "Simulado"
