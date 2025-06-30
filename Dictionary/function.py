a = {"name":"Hridoy","age":"23","department":"SWE"}
for i in a.keys():
    print(i)

for i in a.values():
    print(i)

for i,j in a.items():
    print(i," ",j)

b=dict(name="Kawsar",age="23",hobby="Football",department="SWE")
print(b)
b.update({'hobby':'Volleyball'})
print(b)