s1=input("Enter the string: ")
str_ls=sorted(s1)
print("The sorted array is: ")
for i in range(0,len(s1)):
    print(str_ls[i], end="")

print("")
for i in set(str_ls):
     print(i+" frequency is: "+ str(s1.count(i)))
