val1 = int(input("First input: "))
val2 = int(input("Second input: "))
op = input("Operation: ")

if op=='+':
    print(val1+val2)
elif op=='-':
    print(val1-val2)
elif op=='*':
    print(val1*val2)
elif op=='/':
    print(val1/val2)
elif op=='%':
    print(val1%val2)
elif op=='^':
    print(val1**val2)
else:print("Invalid Operation")
