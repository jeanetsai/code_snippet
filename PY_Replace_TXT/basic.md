import io

a= [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1]
b= [1, 2]
for n, i in enumerate(a):
    for x, y in enumerate(b):
        if i == y:
            a[n] = ''

print (a)
