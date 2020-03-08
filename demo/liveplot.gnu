set xrange [0:20]
set yrange [99:100]
plot "plot.dat" using 1:2 with lines
pause 1
reread
