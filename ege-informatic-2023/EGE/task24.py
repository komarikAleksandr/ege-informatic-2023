text=''
with open('24 (1).txt','r')as file1:
    text=str(file1)
    nn=[]
    cnt=0
    for i in text:
        if i=='a':
            cnt+=1
        if i=='d':
            nn.append(cnt)
            cnt=0
    print(max(nn))
