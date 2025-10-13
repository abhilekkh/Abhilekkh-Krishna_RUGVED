def triple_and(a,b,c):
   return (a and b and c)

def to_bool(x):  
    x = x.strip().lower() 
    if x in ("0", "false", ""):
        return False
    return True

a=input("Enter if a is True or False: ")
b=input("Enter if b is True or False: ")
c=input("Enter if c is True or False: ")

a=to_bool(a)
b=to_bool(b)
c=to_bool(c)

print(triple_and(a,b,c))