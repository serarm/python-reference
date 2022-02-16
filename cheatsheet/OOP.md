# OOP

## OOP fundamentals

1. In Python everything is object
2. Every object has a class
3. Use type() to find the class
4. State information is contained in attribute and behaviour in method
5. Use dir() to list all methods and  attributes of the object
6. Use help() to list down the documentation of the object
7. Classes and objects both have attributes and methods, but the difference is that a class is an abstract template, while an object is a concrete representation of a class.
8. `self` is a stand-in for a particular object used in class definition
9 Class example
```python
# Include a set_name method
class Employee:
  
  def set_name(self, new_name):
    self.name = new_name
  
# Create an object emp of class Employee  
emp = Employee()

# Use set_name() on emp to set the name of emp to 'Korel Rossi'
emp.set_name('Korel Rossi')

# Print the name of emp
print(emp.name)
```

10. Constructor syntax: `__init__(self,attr1,attr2)` 
11. Camel Case for class and lower case for any attribute
12.  Use docstring

## Instance and class data