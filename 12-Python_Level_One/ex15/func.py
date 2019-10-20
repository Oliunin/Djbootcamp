def my_func(par1="awesome"):
    """
    DOCSTRING
    """
    return "my_func"+par1

def addNum (num1=1,num2=2):
    if type(num1)==type(num2)==int:
        return num1+num2
    else:
        return "need integers"

my_func()
print(type(addNum(2,4)),addNum(2,4))

#lambda expression

#filter
mylist = [1,2,3,4,5,6,7,8]

def even_bool(num):
    return num%2 == 0

evens = filter(even_bool,mylist)
print("filter check:",list(evens))

evens = filter(lambda num:num%2 == 0,mylist)
print("lambda func result:",list(evens))
