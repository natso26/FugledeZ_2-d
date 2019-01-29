'''This file is used to profile main_all.py.

The parameters are set in such a way that we enumerate
subsets of size 16 in Z_2^6 up to 60,000 subsets.

This is a large test case suitable for ordinary profiling.
'''
import runpy, sys

sys.argv.extend([6, 16, 60000])
runpy.run_module('main_all')
