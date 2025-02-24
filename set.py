Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> set1={1,2,3}
>>> print(set1)
{1, 2, 3}
>>> set2=set([4],[56],[67])
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    set2=set([4],[56],[67])
TypeError: set expected at most 1 arguments, got 3
>>> set2=set([4,56,67])
>>> print(set2)
{56, 67, 4}
>>> print(set2)
{56, 67, 4}
>>> set1.add(100)
>>> print(set1)
{1, 2, 3, 100}
>>> set2.remove(3)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    set2.remove(3)
KeyError: 3
>>> set1.remove(3)
>>> print(set1)
{1, 2, 100}
>>> set.pop()
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    set.pop()
TypeError: descriptor 'pop' of 'set' object needs an argument
>>> set1.pop()
1
>>> set1
{2, 100}
>>> set1.discard(100)
>>> set1
{2}
>>> print(len(set1))
1
>>> print(len(set2))
3
>>> set2.union()
{56, 67, 4}
>>> set2.union()
{56, 67, 4}
>>> set2.union(set1)
{56, 2, 67, 4}
>>> set2.intersection(set1)
set()
>>> print(set2)
{56, 67, 4}
>>> set3={1,2,3,4,5,10,20}
>>> set4={2,4,6,8,10}
>>> set3.symmetric_difference(set2)
{1, 2, 67, 3, 5, 10, 20, 56}
>>> set3
{1, 2, 3, 4, 5, 10, 20}
>>> set3.symmetric_difference(set4)
{1, 3, 20, 5, 6, 8}
>>> set3.symmetric_difference.update(set4)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    set3.symmetric_difference.update(set4)
AttributeError: 'builtin_function_or_method' object has no attribute 'update'
>>> set3.symmetric_difference_update(set4)
>>> set3
{1, 3, 5, 6, 8, 20}
>>> set3.symmetric_difference_update({100,200,300})
>>> set3
{1, 3, 100, 5, 6, 8, 200, 300, 20}
>>> set3
{1, 3, 100, 5, 6, 8, 200, 300, 20}
>>> set4
{2, 4, 6, 8, 10}
>>> set3.update(set4)
>>> set3
{1, 2, 3, 100, 5, 6, 4, 8, 200, 10, 300, 20}
>>> set3.remove(100,200)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    set3.remove(100,200)
TypeError: remove() takes exactly one argument (2 given)
>>> set3.remove(100)
>>> set3
{1, 2, 3, 5, 6, 4, 8, 200, 10, 300, 20}
>>> set3.intersection(set4)
{2, 4, 6, 8, 10}
>>> 
