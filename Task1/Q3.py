num=input("Enter a number: ")
flag=int(1)
l=len(num)
max=num[int((l-1)/2)]
for i in range(0,l):
    if(num[i]!=num[l-i-1]):
        flag=0
        break
    if(max<num[i]):
        flag=0
        break

if(flag):
    print(num+" is a Hill number")
else:
    print(num+" is not a Hill number")    
    

