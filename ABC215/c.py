import itertools
s,k = input().split()
k_n = int(k)
a = set(list(itertools.permutations(s)))
b = sorted(a)
print(*b[k_n-1], sep="")