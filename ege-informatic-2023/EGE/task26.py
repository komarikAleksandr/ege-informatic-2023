nn=[]
nn2=[]
#if (('0' in i) or ('1' in i) or ('2' in i) or ('3' in i) or('4' in i)or ('5' in i)or('6' in i) or ('7' in i) or ('8' in i) or ('9' in i)):
with open('26_4604.txt','r')as file1:
    for i in file1:
        nn.append(i)

print(nn)

minNN=min(nn)
print(minNN)
nn2.append(minNN)
nn=nn.sort()
print(nn)
for i in nn:
    if (int(i)-int(minNN))>2:
        nn.remove(i)
        nn2.append(i)
    minNN=min(nn)
print(nn2)
