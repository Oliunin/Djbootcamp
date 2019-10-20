# Given a list of integers, return True if the sequence of numbers 1, 2, 3
# appears in the list somewhere.

# For example:

ar1=[1, 1, 2, 3, 1]
ar2=[1, 1, 2, 4, 1]
ar3=[1, 1, 2, 1, 2, 3]
num=[1,2,3]
def arrayCheck(ar,num):
    print("Is ", num," in ", ar,"?")
    return (num in ar)
print(arrayCheck(ar1,num))
print(arrayCheck(ar2,num))
print(arrayCheck(ar3,num))
#####################
## -- PROBLEM 2 -- ##
#####################

# Given a string, return a new string made of every other character starting
# with the first, so "Hello" yields "Hlo".

# For example:

# stringBits('Hello') → 'Hlo'
# stringBits('Hi') → 'H'
# stringBits('Heeololeo') → 'Hello'
def stringBits(str):
  return ('some bullshit '+str)

str1='Hello'
str2='Hi'
str3='Heeololeo'
lstr=[str1,str2,str3]
for i in range(len(lstr)):
    print(stringBits(lstr[i]))

#####################
## -- PROBLEM 3 -- ##
#####################
# Given two strings, return True if either of the strings appears at the very end
# of the other string, ignoring upper/lower case differences (in other words, the
# computation should not be "case sensitive").
#
# Note: s.lower() returns the lowercase version of a string.
#
# Examples:
#
# end_other('Hiabc', 'abc') → True
# end_other('AbC', 'HiaBc') → True
# end_other('abc', 'abXabc') → True

str1='Hiabc'
str2='AbC'


def end_other(a, b):
    if (a.lower() in b.lower()) or (a.upper() in b.upper()): return ("there is ", a, "in ",b)
    elif (b.lower() in a.lower()) or (b.upper() in a.upper()): return ("there is ", b, "in ",a)
    else: return ("no intersections")

print(end_other(str1,str2))

#####################
## -- PROBLEM 4 -- ##
#####################

# Given a string, return a string where for every char in the original,
# there are two chars.

# doubleChar('The') → 'TThhee'
# doubleChar('AAbb') → 'AAAAbbbb'
# doubleChar('Hi-There') → 'HHii--TThheerree'
def doubleChar(dstr,str):
    for x in range(len(str)):
        dstr=dstr+str[x]+str[x]
    return dstr
dstr=""
str1='The'
str2='AAbb'
str3='Hi-There'
i=0
x=0
lstr=[str1,str2,str3]
print(type(lstr),len(lstr),lstr)
for i in range(len(lstr)):
    print(doubleChar(dstr,lstr[i]))
