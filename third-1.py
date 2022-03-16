print("input 5 numbers")
a=[]
sw=1
for i in range(5):
    a.append(input())


for i in range(5):
    j=i+1
    while(j<5):
        if a[i]<a[j]:
            j+=1
        else:
            sw=0
            break    

    if sw==0:
        break    

if sw==1:
    print("yes")   
else:
    print("no")     