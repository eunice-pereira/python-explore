# Lists: ordered, mutable, allows duplicate elements 

my_list = ['banana', 'cherry', 'apple']
print(my_list)

# Can store different data types 
my_list2 = [5, True, 'apple', 'apple']
print(my_list2)

item = my_list[2]
print(item)

# iterate over list 
for i in my_list:
    print(i)

# check if item is in list 
if 'banana' in my_list:
    print('yes')
else: 
    print('no')

# check how many elements inside list 
print(len(my_list))

# append items - inserts item at end of list 
my_list.append('lemon')
print(my_list)

# insert items at certain index (first number specified)
my_list.insert(1, 'blueberry')
print(my_list)

# remove items at end of list 
item = my_list.pop()
print(item)

# remove specific element 
item = my_list.remove('cherry')
print(my_list)

# remove all elements 
item = my_list.clear()

# reverse elements in list 
item = my_list.reverse()

# sort items in list (ascending order). Changes original list. 
my_list.sort()

# to sort list, but maintain original list, use `sorted()` method 

newlist = [1,2,3,4,5,6,7,8,9]

# indicate index range of list 
a = newlist[1:5]
print(a)

list_org = ['banana', 'cherry', 'apple']

# make a copy of list by .copy(), or list(addlisthere)
list_copy = list_org.copy()

print(list_copy)
print(list_org)

# list comprehension: create a new list with expression in one line 

list = [1,2,3,4,5,6]
b = [i*i for i in list]
print(list)
print(b)