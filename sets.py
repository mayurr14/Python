Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> my_set = {5,10,15,20,25,30,35,40,45,50}
>>> my_list = list(my_set)
>>> my_list.pop(4)
45
>>> my_set = set(my_list)
>>> highest_value = max(my_set)
>>> smallest_value = min(my_set)
>>> my_set.add(33)
>>> print("updated set:", my_set)
updated set: {33, 35, 5, 40, 10, 15, 50, 20, 25, 30}
>>> print("highest_value:", highest_value)
highest_value: 50
>>> print("smallest_value:", smallest_value)
smallest_value: 5
>>> 
