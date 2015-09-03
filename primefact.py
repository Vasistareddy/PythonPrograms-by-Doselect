"""Take an integer as input from STDIN. 

Read an integer N from stdin. Print 1 if N is a prime number. If N is not prime, print the lowest prime factor found.


Constraints:

n < 10^10"""

def primef(n):
    primfac = []
    d = 2
    while d * d <= n:
        while (n % d) == 0:
            primfac.append(d)  # supposing you want multiple factors repeated
            n //= d
        d += 1
    if n > 1:
       primfac.append(n)
    return primfac

if __name__ == "__main__":
    n = input("enter the number")
    if n < pow(10, 10):
        primefactor = primef(n)
    else:
        print "value exceeded"
        
    if n <= 1:
        print n
    elif len(primefactor) == 1:
        print 1
    else:
        print primefactor[0]
    #print primefactor