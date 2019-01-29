'''This file is used to profile main_all.py.

The parameters are set in such a way that we enumerate
subsets of size 16 in Z_2^6 up to 500 subsets.

This is a small test case suitble for line profiling,
which is much slower than ordinary profiling.
'''
import runpy, sys

sys.argv.extend([6, 16, 500])
runpy.run_module('main_all')
