
from math import *

def gt(n):
    if n == 1:
        return 1
    return n * gt(n-1)

if __name__ == '__main__':
    n = int(input())
    print(gt(n))