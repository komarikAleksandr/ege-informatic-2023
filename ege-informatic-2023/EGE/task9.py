nn=[]
nn1=[]
with open('tt9.txt','r')as k:
    for line in k:
        nn.append(line)

for line in nn:
    line=line.split()
    for i in line:
        i=int(i)

for ui in nn:
    print(type(ui))
