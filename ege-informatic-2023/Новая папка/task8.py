import itertools
def psd(x):
    return x==x[::-1]
def asd(x):
    return x[4]
ddd=itertools.product('POLYGON',repeat=5)

gh=[]
for i in ddd:

    if psd(i) and (asd(i)=='O' or asd(i)=='Y'):
        gh.append(i)



print(len(gh))
