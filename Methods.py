# Set Methods in Pythonn Language 

"""
1. Add() Method - Adds An Element To The Set
  Syntex:
    Set.Add(Elmnt)
  Parameter:
    Elmnt Required
"""

thisset = {"apple","banana", "cherry"}
thisset.add("orange")
print(thisset)

"""
OUTPUT:
{'orange', 'banana', 'apple', 'cherry'}
""""

"""
2. Clear() Method - Removes All The Elements From The Set
  Syntex: 
    Set.Clear()
  Parameter
    No Paratmeters
"""

thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

"""
OUTPUT:
set()
"""

"""
3.Difference() Method - Returns A Set Containing The Difference Between Two Or More Sets
  Syntex:
    Set.Difference(Set)
   Parameter:
    Set Required
"""

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = y.difference(x)
print(z)

"""
OUTPUT
{'google', 'microsoft'}
"""

"""
4. Intersection() Method - Returns A Set, That Is The Intersection of Two Other Sets
  Syntex:
    Set.Intersection(Set1, Set2,...Etc)
  Parameter:
    Set1 Required
    Set2 Optional
"""
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)
"""

"""
OUTPUT:
{'apple'}
"""

"""
5. Pop() Method - Removes An Element From The Set
  Syntex:
    Set.Pop()
  Parameter 
    No Parameter
"""

fruits = {"apple", "banana", "cherry"}
x = fruits.pop()
print(x)

"""
OUTPUT
apple
"""

"""
6. Remove() Method - Adds An Element To The Set
  Syntex:
      Set.Remove(Item)
  Parameter
      Item Required
"""

fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
print(fruits)

"""
OUTPUT:
  {'apple', 'cherry'}
"""

"""
7. Union() Method - Return A Set Containg The Union Of Sets
  Syntex:
      Set.Union(Set1, Set2....)
  Parameters
      Set1 Required
      Set2 Optional
"""

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.union(y)
print(z)

"""
OUTPUT:
{'cherry', 'apple', 'banana', 'google', 'microsoft'}
"""

"""
8. Discard() Method - Remove The Specified Item
  Syntex:
      Set.Discard(Value)
  Parameter
      Value Required
"""

thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

"""
OTPUT:
  {'apple', 'cherry'}
  """
