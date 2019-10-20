my_stuff = {"key1":"value","key2":"value","key3":{'123':[1,2,'grabme']}}
print(my_stuff["key3"]['123'][2].upper())

food = {'lunch':'pizza','bfast':'eggs'}
food['lunch'] = 'burger'
food['dinner'] = 'pasta'
print(food['lunch'],food)
