# # Typle: ordered, immutable, allows duplicate elements 
# # Similar to list, but cannot be changed 

# mytuple = ('Max', 28, 'Boston')

# # create tuple with built in function 
# newtuple = tuple(['name', 20, 'Houston'])

# # specify index like with lists 
# item = mytuple[2]

# # iterate over tuple
# for i in mytuple:
#     print(i)

# # check if element is inside tuple 
# if 'Max' in mytuple:
#     print('yes')
# else: 
#     print('no')

# # check length with len(). Count elements with tuple.count()
# letters = ('a', 'b', 'c', 'd', 'e')
# print(letters.count('b'))

# # find first index of one specific element. Will return first index of 'p'
# # if element is not in tuple will get error 
# print(letters.index('b'))

# # convert tuple to list and vice versa 

# newlist = list(mytuple)
# print(newlist)

# # slicing 
# a = (1,2,3,4,5,6,7,8,9,10)

# b = a[2:5] #specify start and stop index 
# print(b) 

# # step argument, will take every second element 
# b = a[::2]
# print(b)

# # unpacking tuples: declare variables on left side and assing to tuple items

# name, age, city = mytuple
# print(name)
# print(age)
# print(city)

# # unpack multiple elements with * and converts them to a list 
# numbers = (0,1,2,3,4)

# i1, *i2, i3 = numbers
# print(i1)
# print(i3)
# print(i2) # [1,2,3]

# tuples vs list: tuples can be more efficient, less bytes and more efficient to iterate (less time)
import sys 
my_list = [0,1,2,'hello', True]
my_tuple = (0,1,2,'hello', True)
print(sys.getsizeof(my_list), 'bytes') # 120 bytes
print(sys.getsizeof(my_tuple), 'bytes') # 80 bytes
