# Use indexing to print out the following:
# 'd'
# 'o'
# 'djan'
# 'jan'
# 'go'
# Bonus: Use indexing to reverse the string
s = 'django'
i=len(s)
while i>0:
    print(s[i-1])
    i=i-1
print(s[0],s[-1],s[0:4],s[4:])

# Given this nested list:
l = [3,7,[1,4,'hello']]
# Reassign "hello" to be "goodbye"
l[2][2]="goodbye"
print(l)

# Using keys and indexing, grab the 'hello' from the following dictionaries:
d1 = {'simple_key':'hello'}
d2 = {'k1':{'k2':'hello'}}
d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d1['simple_key'])
print(d2['k1']['k2'])
x=(d3['k1'][0]['nest_key'][1])
print(type(x),x)

# Use a set to find the unique values of the list below:
mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3]
y=set(mylist)
print(y)

###############
## Problem 5 ##
###############
# You are given two variables:
age = 4
name = "Sammy"
# Use print formatting to print the following string:
print("Hello my dog's name is {} and he is {} years old".format(name,age))
