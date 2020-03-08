set xrange [0:100]
set yrange [0:100]
plot "plot.dat" using 1:2 with lines
pause 1
reread
