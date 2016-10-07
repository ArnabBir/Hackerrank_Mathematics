import operator as op
import sys

def nCr(n, r):
    r = min(r, n-r)
    if r == 0: return 1
    numer = reduce(op.mul, xrange(n, n-r, -1))
    denom = reduce(op.mul, xrange(1, r+1))
    return (numer//denom) % 10**9

def main():
    T = int(raw_input())
    while(T):
        n = int(raw_input())
        for r in xrange(n+1):
            sys.stdout.write(str(nCr(n, r)) + " ")
        print ""
        T -= 1
        
main()
