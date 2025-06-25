a = input() # a = input("Take a input: ")
print(a)

arr1 = list(map(int,input().split()))
print(arr1)

n = int(input("Enter the size of the array: ")) #Type cast kore nite hoy.
# Userinput string hisebe ney
arr2 = [0]*n
for i in range(n):
    arr2[i] = int(input()) #input: 2
                        #          4
                        #          8

print(arr2)