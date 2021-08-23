import math
import sys
N = int(input())
for k in range(1000000):
  if 2**k <= N < 2**(k+1):
    print(k)
    sys.exit()