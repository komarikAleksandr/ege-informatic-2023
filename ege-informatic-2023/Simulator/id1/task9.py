
nn=[]
with open('17 (4).txt')as file1:
    for line in file1:
        nn.append(int(line))
cnt=0
nn2=[]
maxNN=0
for i in range(len(nn)-1):
    i1=nn[i]
    i2=nn[i+1]
    if ((i1%3==0) or (i1%3==0)) and (i1+i2)%5==0:
        cnt+=1
        nn2.append([i1,i2])
for i in nn2:
    maxNN=max(maxNN,sum(i))
print(cnt,maxNN)