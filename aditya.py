a=int(input("enter any number :"))
s=0
while a>0:
    r=a%10
    s=s*10+r
    a=a//10
print("number is palindrome :",s)
