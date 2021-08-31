import sys
n = int(input())
name = [input().split() for _ in range(n)]

for i in range(n):
    for j in range(i+1,n):
        if name[i][0] == name[j][0] and name[i][1] == name[j][1]:
            print('Yes')
            sys.exit()

print('No')
