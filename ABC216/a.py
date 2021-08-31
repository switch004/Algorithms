xy = float(input())

x = int(xy)
y = xy*10%10

if 0 <= y <= 2:
    print(str(x)+'-')
elif 3<= y <= 6:
    print(x)
else:
    print(str(x)+'+')
