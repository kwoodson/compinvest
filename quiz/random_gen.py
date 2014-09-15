#!/usr/bin/env python

import random

def main():
  random.seed(10)
  print map(lambda x: random.randint(1, 100), range(100))



if __name__ == '__main__':
    main()
