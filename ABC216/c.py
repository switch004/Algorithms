n = int(input())
num = []
while n != 0:
    num.append(n % 2)
    n = n//2

num.reverse()
ans = []
for i in range(len(num)):
    if num[i]==1:
        ans.append('A')
    if i != len(num)-1:
        ans.append('B')

print(''.join(ans))
