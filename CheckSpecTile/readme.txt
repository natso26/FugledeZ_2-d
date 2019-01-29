This program checks Fuglede's conjecture for subsets of Z_2^d by checking whether a subset E is a spectral set and whether it is a tile.


== What to run ==

There are two files that can be run.

1. main_single.py

This file checks Fuglede's conjecture for a single subset, and displays relevant information. It can be used to experiment and see behaviors of subsets of interest.

See instructions in the comments in the file for how to input data.

2. main_all.py

This file checks Fuglede's conjecture for all subsets of Z_2^d of a given size n that do not lie in any hyperplane, by using exhaustive enumeration. It contributes towards checking Fuglede's conjecture in Z_2^5 and Z_2^6.


== The two versions ==

There are two versions of the program.

1. The Original version. This version is fully functional, but it is not fast enough to check the conjecture for subsets of size 16 in Z_2^6 (it will take many years).

The comments in the files in this version contain information on how the program is implemented.

2. The Fast version. This is a modification of the Original version which can perform the task above in less than one day.

The comments in the files in this version are focused on which improvements have be made from the Original version.