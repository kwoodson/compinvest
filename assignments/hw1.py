#!/usr/bin/env python
#
#
# Assess and optimize a portfolio
#
#

import QSTK.qstkutil.qsdateutil as du
import QSTK.qstkutil.tsutil as tsu
import QSTK.qstkutil.DataAccess as da

import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd

'''
allocations = [] * 4
set([z for z in itertools.product(np.arange(0,1,.1), repeat=len(allocations) if sum(z) == 1] + [x for x in itertools.permutations([1,0,0,0])])
'''

def simulate(start, end, symbols, allocations):
  pass

def main():
  symbols = ['GOOG', 'AAPL', 'GLD', 'XOM']
  allocations = [.3, .1, .4, .2]
  std_dev, avg_return, sharpe_ratio, cum_return = simulate(start, end, symbols, allocations)
  

if __name__ == '__main__':
  main()
