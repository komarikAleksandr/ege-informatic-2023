def dew(n,m):
    return n%m==0

for A in range(200):
    k=0
    for x in range(100):
        g=dew(x,3)
        if g ==True:
            g=False
        else:
            g=True
        if ((dew(x,2)<= g)) or (x+A>=80):
            k+=1
    if k==100:
        print(A)
        
'''
for A in range(0, 300):
    k=0
    for x in range(1, 301):
        for y in range(1, 301):
            if (x >= A) or (y >= A) or (x * y <= 205):
                k=k+1
    if k==90000:
        print(A)
'''
