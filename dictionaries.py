# Dictionary: Key-Value pairs, unordered, mutable 

my_dict = {'name': 'Eunice', 'age': 33, 'city': 'New York'}
print(my_dict)

# create a dictionary with built-in function. 
new_dict = dict(name='Mary', age=27, city='Boston')
print(new_dict)

# mutable: add or change items after its creation 
my_dict['email'] = 'email@xyz.com'
print(my_dict)

# delete items with del method, pop(), popitem() to remove last inserted item
del my_dict['name']

# check if key is inside dictionary: use if in statement 
if 'city' in my_dict:
    print(my_dict['city'])

# also check using try 
try: 
    print(my_dict['age'])
except:
    print('error')

# loop through a dictionary 

for key in my_dict: 
    print(key)

for value in my_dict.values():
    print(value)

for keys in my_dict.keys(): 
    print(keys)

# print both keys and values 
for key, value in my_dict.items():
    print(key, value)

# using tuple as a key 

mytuple = (8,7)
my_dict = {mytuple: 15}

print(my_dict) # { (8,7): 15}