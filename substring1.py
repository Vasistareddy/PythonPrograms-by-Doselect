"""Similarity of two strings A and B is defined as the length of the longest prefix common to both strings. For example, the similarity of strings “abc” and “abd” is 2, while the similarity of strings “aaa” and “aaab” is 3.

Calculate the sum of similarities of a string S with each of its suffixes, including the string itself as the first suffix.


Input:

The first line contains the number of test cases T. Each of the next T lines contains a string each.


Output:

Output T lines, each containing one integer that is the answer for the corresponding test case.


Constraints:

1 ≤ T ≤ 10

The length of each string is at most 100,000

The strings contain only lowercase characters [a-z]."""
def sim(inp):
	linp = list(inp)

	li = []
	for i in range(0,len(linp)):
		s = ""
		for j in range(i,len(linp)):
			s = s + linp[j]
		li.append(s)

	lis = li
	print lis
	suming = 0
	for i in lis:
		llis = list(i)
		leng = 0
		for j in range(0,(len(llis))):
			if linp[j] == llis[j]:
				leng = leng + 1
			elif linp[j] != llis[j]:
				break
		suming = suming + leng

	print suming

def main():
    testcases = input()
    
    if testcases >=1 and testcases <=10:
        for i in range(testcases):
            string = raw_input()
            if len(string) <= 10000 and string.islower() and string.isalpha():
                sim(string)
            else:
                print "string length exceeded or Uppercase or numbers entered"
    else:
        print "test cases exceeded"
main()