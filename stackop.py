"""You're provided a stack that's empty at the start. Now a series of operations occur on that stack, you need to print out the value on top of the stack to output after every operation. If stack is empty then print "EMPTY" (without quotes).


Allowed Operations:

push a // Push an element with value a to the top of the stack

pop // Pop the top element from the stack

inc x d // Add the value d to each of the bottom x elements on the stack


Input Format:

n - Integer, number of operations, on the top line.
n lines with exactly one operation per line from the list above.


Output Format:

n lines of text, with the element at the top of the stack on each line.
If stack is empty, then print "EMPTY" (without quotes).


Note: For a pop operation, the output is the element exposed by the pop, not the element popped off.
Sample Input:
12

push 4

pop

push 3

push 5

push 2

inc 3 1

pop

push 1

inc 2 2

push 4

pop

pop


Sample Output:

4
EMPTY

3

5

2

3

6

1

1

4

1

8


Explanation:
(The state of the whole stack is shown in square brackets, bottom to top.) 

push 4 [4]

pop [] - Since list is empty, print "EMPTY" after this operation

push 3 [3]

push 5 [3, 5]   

push 2 [3, 5, 2]

inc 3 1 [4, 6, 3]

pop [4, 6]

push 1 [4, 6, 1]

inc 2 2 [6, 8, 1]

push 4 [6, 8, 1, 4]

pop [6, 8, 1]

pop [6, 8]


"""
s = []
def push(x):
	s.append(x)
	print s[-1]
def pop():
	if not s:
		print "EMPTY"
	else:
		s.pop()
		if not s:
			print "EMPTY"
		else:
			print s[-1]

def inc(x,d):
	if not s:
		print "EMPTY"
	else:
		for i in range(x):
			s[i] = s[i] + d
		print s[-1]

def main():
	N = input("Enter the number")
	if N >=0 and N <= 500000:
		for i in range(N):
			string = raw_input("Enter the operation")
			l = string.split()
			if l[0] == 'push':
				push(int(l[1]))
			elif l[0] == 'pop':
				pop()
			else:
				inc(int(l[1]),int(l[2]))
			
	
main()