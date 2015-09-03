"""Dodo's friend Dino challenged him to a new game he had invented - FizzyBuzzy. In this game, players are given a number N and they've to do the following:

- print the numbers from 1 to N, each on a new line,

- but for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. 

- For numbers which are multiples of both three and five print “FizzBuzz”. 


Can you help Dodo win the match?"""
N = int(raw_input())
if N < pow(10,7) and N > 0:
    for i in range(1,N+1):
    	if i%3==0 and i%5==0:
    		print "FizzBuzz"
    	elif i%3==0:
    		print "Fizz"
    	elif i%5==0:
    		print "Buzz"
    	else:
    		print i
else:
    print "Take input greater than zero"