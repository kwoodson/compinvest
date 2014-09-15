#!/usr/bin/env python
#
#
# Assess and optimize a portfolio
#
#

import QSTK.qstkutil.qsdateutil as du
import QSTK.qstkutil.tsutil as tsu
import QSTK.qstkutil.DataAccess as da

import itertools
import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import pdb

'''
'''

#def simulate(start, end, symbols, allocations):
def simulate(returns, allocations):
  portfolio_returns = np.sum(returns * allocations, axis=1)
  cumulative_returns = portfolio_returns[-1]
  tsu.returnize0(portfolio_returns)

  std_dev = np.std(portfolio_returns)
  daily_ret = np.mean(portfolio_returns)
  sharpe = (np.sqrt(len(returns)) * daily_ret) / std_dev

  return std_dev, daily_ret, sharpe, cumulative_returns

def main():
  allocations = [0.0] * 4
  symbols = ['AXP', 'HPQ', 'IBM', 'HNZ']
  #symbols = ['GOOG', 'AAPL', 'GLD', 'XOM']
  #symbols = ['GOOG', 'AAPL', 'IBM', 'MSFT']
  #start = dt.datetime(2013,1,1)
  #end   = dt.datetime(2013,12,31)

  start = dt.datetime(2010,1,1)
  end   = dt.datetime(2010,12,31)
  close_time = dt.timedelta(hours=16)

  timestamps = du.getNYSEdays(start, end, close_time)

  # datasource
  market_source = da.DataAccess('Yahoo')

  keys = ['open','high','low','close','volume','actual_close']
  data = market_source.get_data(timestamps, symbols, keys)
  stocks = dict(zip(keys,data))
  #pdb.set_trace()

  returns = stocks['close'].copy()
  returns = returns.fillna(method='ffill')
  returns = returns.fillna(method='bfill')

  na_returns = returns.values
  na_returns = na_returns/na_returns[0, :]

  max_sharpe      = -1000
  final_dev       = -1000
  final_daily_ret = -1000
  final_cum_ret   = -1000
  best_allocation = allocations
  all_allocations = [x for x in itertools.permutations([1,0,0,0])]
  all_allocations.extend([z for z in itertools.product(np.arange(0,1,.1), repeat=len(allocations)) if sum(z) == 1])
  #allocations = [.3, .1, .4, .2]
  for allocation in set(all_allocations):
    #std_dev, avg_return, sharpe_ratio, cum_return = simulate(start, end, symbols, allocations)
    #print na_returns
    std_dev, daily_return, sharpe, cumu_return = simulate(na_returns, allocation)
    #print std_dev, daily_return, sharpe, cumu_return
    if sharpe > max_sharpe:
      final_dev          = std_dev
      final_daily_ret    = daily_return
      final_cum_ret      = cumu_return
      max_sharpe         = sharpe
      best_allocation    = allocation
  
  print "      Symbols: ", symbols
  print "   Allocation: ", best_allocation
  print "Std Deviation: ", final_dev
  print "Daily Returns: ", final_daily_ret
  print "Cumul Returns: ", final_cum_ret
  print " Sharpe Ratio: ", max_sharpe

  all_symbols = list(set(symbols) | set(['SPY']))

  data = market_source.get_data(timestamps, all_symbols, keys)
  data_dict = dict(zip(keys, data))

  returns = data_dict['close'].copy()
  # filling data
  returns = returns.fillna(method='ffill')
  returns = returns.fillna(method='bfill')

  returns = returns.reindex(columns=symbols)

  na_returns = returns.values
  tsu.returnize0(na_returns)

  #pdb.set_trace()
  port_returns = np.sum(na_returns * best_allocation, axis=1)
  na_portfolio_total = np.cumprod(port_returns + 1)

  na_market = data_dict['close']['SPY'].values

  na_market = na_market/na_market[0]

  plt.clf()
  plt.plot(timestamps, na_portfolio_total, label='Portfolio')
  plt.plot(timestamps, na_market, label='SPY')
  plt.legend()
  plt.ylabel('Returns')
  plt.ylabel('Date')
  plt.savefig('homework1.pdf', format='pdf')


if __name__ == '__main__':
  main()
