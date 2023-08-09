nn=['']
nn2=[]
nn3=[]
for x in range(0,10**6):
    nn.append(str(x))
for i in range(0,1000000):
    for j in nn:
        t='1234'+j+'7'
        if int(t)%141==0:
            nn2.append(j)
            nn3.append(int(t)%141)

print(nn2)
print(nn3)
