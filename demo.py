a = ['a','b','c','d','e','f']
b = ['1','2','3']
c = 2
m = 1
for i in range(0,6):
    if i <= c-1:
       print(a[i],end="")
       if i == c-1:
            # print(i,m,c-1)
            print(b[i-m],end="")
            c += 2
            m += 1