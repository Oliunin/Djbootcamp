myilist = ['a','b','c']
myslist = ['d','e','f']
y="g"
x= myilist+myslist
x[-1] = 'h'
x.extend(['i','j','k'])
x.append(y)
print(len(x),x)
item = x.pop()
print(item)
slist = x.sort()
print(slist)
#list comprehension
matrix = [[1,2,3],[4,5,6],[7,8,9]]
first_col = [row[0] for row in matrix]
print(first_col)
