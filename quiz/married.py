#!/usr/bin/env python

import random

class Person(object):
  def __init__(self, sal, mar=False):
    self.married = mar
    self.salary = sal

  def set_married(self, mar):
    self.married = mar

  def married(self):
    return self.married

  def salary(self):
    return self.salary

  def set_salary(self, value):
    self.salary = value


def get_array_random(z=10):
  return [random.randint(1,1000001) for x in range(z)]

def subset_shuffle(array, size=100):
  random.shuffle(array)
  if size <= array:
    return array[:size]
  return array

def main():
  all_values = get_array_random(1000)
  men = [Person(random.randint(1,1000001)) for x in range(100)]
  women = [Person(random.randint(1,1000001)) for x in range(100)]
  #print [x.salary for x in men]
  #print [x.salary for x in women]

  #import pdb
  #pdb.set_trace()

  married = 0
  changes = True
  while changes:
    changes = False
    print "Men(%s) Women(%s)" % (len(men), len(women))
    for ind_w, w in enumerate(women):
      for ind_m, m in enumerate(men):
        #m = men[random.randint(0,len(men)-1)]
        if not m.married and not w.married and m.salary > w.salary:
          married += 1
          women.remove(w)
          men.remove(m)
          m.set_married(True)
          w.set_married(True)
          changes = True
          break
    #else:
      #been through once, break
      #break
    #else:
      #lowest_salary = min([x.salary for x in men])
      #if any(lambda x: x < lowest_salary , [x.salary for x in women]): break
      #highest_salary = max([x.salary for x in women])
      #if lowest_salary < highest_salary: break
      # trying again
      #if changes: break

  return married  


if __name__ == "__main__":
  #results = [main() for z in range(100)]
  results = [main() for z in range(100)]
  print results
  print float(sum(results)/len(results))
