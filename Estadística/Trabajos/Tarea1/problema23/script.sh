#!/bin/bash

Rscript probability.R
gnuplot histo.gp
evince histograma.pdf
