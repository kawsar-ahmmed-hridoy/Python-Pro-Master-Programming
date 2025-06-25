num1 = 5
print(num1, type(num1))

num2 = 10.5
print(num2, type(num2))

num3 = 5j
print(num3, type(num3))

num4 = ["23", "hridoy", "3.5"]
print(num4, type(num4))
print(num4[2]) #indexed from 0 to n-1.

#Tuple
num5 = ('Hridoy', 'is', 'a', 'good', 'person')
print(num5)
print(type(num5))

#Dictionary type
person = {
    "Name":"Hridoy",
    "Age":23,
    "Contact":'01714440146'
}
print(person, type(person))
print(person['Age'])

#Set
man = {
    'Hridoy', 23, '01714440146'
}
print(man, type(man))