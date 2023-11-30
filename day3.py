total=0
for i in range (1,5):
    total +=i
print(total)

tatal2=0
j=1
while j<5:
    tatal2 +=j
    j +=1
print(tatal2)

given_list=[5,4,4,3,1,-1,-2,-3,-5]
total3=0
i = 0
while given_list[i]>0:
    total3 += given_list[i]
    i +=1
print(total3)


given_list3=[5,4,4,3,1,-1,-2,-3,-5]
total5=0
for element in given_list3:
    if element <=0:
        break
    total5 += element
print(total5)