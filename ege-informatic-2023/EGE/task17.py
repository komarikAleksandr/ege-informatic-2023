'''
В файле содержится последовательность целых чисел. Элементы последовательности могут принимать целые значения от −10 000 до 10 000 включительно.
Определите и запишите в ответе сначала количество пар элементов последовательности, в которых хотя бы одно число делится на 3,
затем максимальную из сумм элементов таких пар. В данной задаче под парой подразумевается два идущих подряд элемента последовательности.
Например, для последовательности из пяти элементов: 6; 2; 9; –3; 6  — ответ: 4 11.
Пояснение: Из 4 чисел можно составить 6 пар. В данном случае условиям удовлетворяют пары: 168 и 320, 168 и 7, 320 и 7, 328 и 7. Максимальную сумму дает пара 168 и 320  — 488.
'''
'''
task1=25586925
task2=19989
sto=[]
sto1=[]
sto2=[]
with open("17 (2).txt")as nf:
    for line in nf:
        sto.append(line)

for x in sto:
    for y in sto:
        x=int(x)
        y=int(y)
        if ((x%160)!=(y%160)) and ((x%7==0)or(y%7==0)):
            sto1.append([x,y])
print(len(sto1))
maxSum=0
for i in sto1:
    if i[0]+i[1]>maxSum:
        maxSum=i[0]+i[1]
print(maxSum)
'''
'''
f = open('17 (2).txt')
a = [int(i) for i in f]
s = 0
mx = 0
for i in range(len(a) - 1):
    for j in range(i + 1, len(a)):
        if (a[i] % 160 != a[j] % 160) and ((a[i] % 7 == 0) or (a[j] % 7 == 0)):
            s += 1
            mx = max(mx, a[i] + a[j])
print(s, mx)
'''
sto=[]
sto2=[]
mx=0
with open("17 (3).txt")as nf:
    for line in nf:
        sto.append(line)
for y in range(len(sto)-1):
    i=int(sto[y])
    i1=int(sto[y+1])
    if i%3==0 or i1%3==0:
        sto2.append([i,i1])

for x in sto2:
    mx=max(sum(x),mx)

print(len(sto2),mx)
