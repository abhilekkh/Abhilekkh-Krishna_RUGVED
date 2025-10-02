s=input("Enter the string: ")
str_ls=sorted(s)
print("The sorted array is: ")
for i in range(0,len(s)):
    print(str_ls[i], end="")

print("")
for i in set(str_ls):
     print(i+" frequency is: "+ str(s.count(i)))
