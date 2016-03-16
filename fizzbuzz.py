#!/usr/bin/python

import sys 

start_num = int(sys.argv[1])
end_num = int(sys.argv[2]) + 1

fizz_total = 0
buzz_total = 0
fizz_buzz_total = 0

for num in range(start_num,end_num):
  if ( num % 3 ) == 0:
    print "Fizz"
    fizz_total += 1
  elif ( num % 5 ) == 0:
    print "Buzz"
    buzz_total += 1
  elif ( num % 5 ) == 0 and ( num % 3 ) == 0:
    print "Fizz Buzz"
    fizz_buzz_total += 1 
  else:
    print num

print "Fizz total: ",fizz_total
print "Buzz total: ",buzz_total
print "Both total: ",fizz_buzz_total
  
    
