This program reads log-Hadamard matrices from files on Neil Sloane's webpage
http://neilsloane.com/hadamard/,
dephase them, and compute the ranks of the dephased matrices in Z_2.

It requires the MATLAB API for Python to be installed.


== What to run ==

Use main_single.py to read a single file.

Use main_all.py to read many files containing matrices of a given size.

The files out_24.txt and out_28.txt contain the results of running main_all.py on all inequivalent log-Hadamard matrices of dimensions 24 x 24 and 28 x 28, respectively.