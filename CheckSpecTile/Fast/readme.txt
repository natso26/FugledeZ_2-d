== Introduction ==

This program is the modified version of the original code that has been made fast enough to be able to check whether Fuglede's conjecture holds for subsets of size 6 in Z_2^6 which do not lie in a hyperplane.

See each file for explanations on what changes are made there.

See the file output.txt for the output of the program after it has been run on subsets of size 6 in Z_2^6, verifying the conjecture in that case.


== Overview of Improvements ==

There are two kinds of modifications.


1. The program is optimized to run faster.

On the author's computer, the original program takes 59 ms to check Fuglede's conjecture for one subset. Since there are 57C9 = 8,996,462,475 subsets to check, the program will run for about 17 years.

The fast version takes only 160 us to go through one subset, yielding about 360 times speedup. Thus, for this number of subsets, the program will run for about 17 days.

The changes are in the files prelim.py, spectral_tile.py, and clique.py.


2. The number of subsets to check are reduced.

By considering symmetries from permuting coordinates of Z_2^6, we come up with heuristics that reduce the number of subsets to check to 295,137,078, or 30 times fewer than the original number.

This reduces the runtime of the program to about 13 hours.

The changes are in the files generate.py and main_all.py. The former file is a new file which implements these heuristics.