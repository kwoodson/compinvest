#!/usr/bin/env python

import random
import sys

def quick_sort(array):
    if len(array) < 1: return array

    #select pivot
    pivot = array[0]

    #lower
    lower = []
    #upper
    upper = []

    for num in array[1:]:
        if num >= pivot:
            upper.append(num)
        else:
            lower.append(num)

    return quick_sort(lower) + [pivot] + quick_sort(upper)


def main():
    numbers = []
    while True:
        try:
            number = int(raw_input())
            numbers.append(number)
            print "Numbers size: %s" % len(numbers)
            print quick_sort(numbers)
        except KeyboardInterrupt:
            print "Bye-bye"
            sys.exit()
        except:
            print "Please input a valid number."

    #print quick_sort([random.randint(1,1000) for x in range(50)])
  



if __name__ == '__main__':
    main()
