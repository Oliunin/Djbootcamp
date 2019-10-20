#Tuple unpacking
mypairs = [(1,2),(3,4),(5,6)]

for (t1,t2) in mypairs:
    print(t1)
    print(t2)

#range
print(list(range(0,10,2)))
for item in range(10):
    print(item)

#list comprehension
x = [1,2,3,4]
out = []
for num in x:
    out.append(num**2)
out=[num**2 for num in x]
print(out)
