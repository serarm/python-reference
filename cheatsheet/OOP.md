# OOP

This cheatsheet is built based on [DataCamp course: *Object Oriented programming in Python*](https://campus.datacamp.com/courses/object-oriented-programming-in-python)
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

1. Instance data referred by `self.` whereas class data is referred by `classname.`
2. Class attributes are used for global value and common values
3. Class method is called used by decorator `@classmethod` and instead of self we use cls
   - No access to `self` variable
   -  Invoked by `classname.`\
   - Used for altenative constructor with return statement as `return cls(arg1)`
```python
class BetterDate:
    def __init__(self, year, month, day):
      self.year, self.month, self.day = year, month, day
      
    @classmethod
    def from_str(cls, datestr):
        year, month, day = map(int, datestr.split("-"))
        return cls(year, month, day)
```
4. Class Inheritance: Helps in code reuse
   - Inheritance represents 'is a' relationship
   - `isinstance` function is true for both parent and child class

5. The fact that the instances of a child class are also instances of the parent class allows you to create consistent interfaces
> Subclass example
```python
class Employee:
  MIN_SALARY = 30000    

  def __init__(self, name, salary=MIN_SALARY):
      self.name = name
      if salary >= Employee.MIN_SALARY:
        self.salary = salary
      else:
        self.salary = Employee.MIN_SALARY
  def give_raise(self, amount):
    self.salary += amount      
        
# MODIFY Manager class and add a display method
class Manager(Employee):
  def display(self):
    print(f"Manager {self.name}")
```

6.  Method inheritance
```python
class Employee:
    def __init__(self, name, salary=30000):
        self.name = name
        self.salary = salary

    def give_raise(self, amount):
        self.salary += amount

        
class Manager(Employee):
    def display(self):
        print("Manager ", self.name)

    def __init__(self, name, salary=50000, project=None):
        Employee.__init__(self, name, salary)
        self.project = project

    # Add a give_raise method
    def give_raise(self,amount,bonus=1.05):
        
        Employee.give_raise(self,amount*bonus)
    
    
mngr = Manager("Ashta Dunbar", 78500)
mngr.give_raise(1000)
print(mngr.salary)
mngr.give_raise(2000, bonus=1.03)
print(mngr.salary)
#79550.0
#81610.0
```

## Integrating with standard python

1. Example of operator overloading `__eq__(self,other)` :
   + When compare two objects it returns `False` (if even internal element are same)
   + When comaparing numpy array elements ,same elements return `True`
   + `__ne__`,`__ge__`,`__le__`,`__gt__`.`__lt__` are some other operators
   + `__hash__` is used to assign integer to object and can be used for key
   + Similar object with same elements can returns equal hence need to check for class type too
> `__eq__` example
```python
class BankAccount:
   # MODIFY to initialize a number attribute
    def __init__(self, number,balance=0):
        self.balance = balance
        self.number = number
      
    def withdraw(self, amount):
        self.balance -= amount 
    
    # Define __eq__ that returns True if the number attributes are equal 
    def __eq__(self, other):
        return (self.number == other.number) and (type(self)==type(other))   
``` 

2. Comparing parent and child objects, child object `__eq__()` is called .
3. `__str__()` and `__repr__()` are called for string representation
    - `__str__()` is used by `str()` and `print()` method
    - `__repr__()` is used when typing in console and also `repr` method
    - `repr`(reproducible representation) is for developer.So better to print the syntax that can use to recreate the object

> `__repr__` and `__str__` example
```python
class Employee:
    def __init__(self, name, salary=30000):
        self.name, self.salary = name, salary
      

    def __str__(self):
        s = "Employee name: {name}\nEmployee salary: {salary}".format(name=self.name, salary=self.salary)      
        return s
      
    # Add the __repr__method  
    def __repr__(self):
        s= "Employee(\"{}\", {})".format(self.name,self.salary)
        return s

```

4. Exception : `try`-`except`-`finally` code
5. Standard exceptions are inherited fron `Exception` and `BaseException`
6. Inheriting exception class can build custom exception
> Error handling example
```python
def invert_at_index(x, ind):
    try:
        return 1/x[ind]
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    except IndexError:
        print("Index out of range!")

```
7. `except` block for a parent exception will catch child exceptions
8. It's better to include an `except` block for a child exception before the block for a parent exception, otherwise the child exceptions will be always be caught in the parent block, and the `except` block for the child will never be executed.

## Best practices of class design

1. `Polymorphism`: Using a unified interface to operate on object of different classes
2. `Liskov substitution function`: objects of a superclass shall be replaceable with objects of its subclasses without breaking the application
3. The classic example of a problem that violates the Liskov Substitution Principle is the Circle-Ellipse problem, sometimes called the Square-Rectangle problem.
> Square-rectange problem
```python
class Rectangle:
    def __init__(self, w,h):
      self.w, self.h = w,h
      
# Define set_h to set h       
    def set_h(self, h):
      self.h = h

# Define set_w to set w
    def set_w(self, w):
      self.w = w   
      
class Square(Rectangle):
    def __init__(self, w):
      self.w, self.h = w, w 
      
# Define set_h to set w and h 
    def set_h(self, h):
      self.h = h
      self.w = h
      
# Define set_w to set w and h 
    def set_w(self, w):
      self.w = w   
      self.h = w  
```
*Violation of `Liskov substitution function`*: Each of the setter methods of Square change both h and w attributes, while setter methods of Rectangle change only one attribute at a time, so the Square objects cannot be substituted for Rectangle into programs that rely on one attribute staying constant.

4. All class data in python is public.To make private use:
   - Naming convention(start attribute name/method name with `_`)
   - `@property` method
   - Using `__getattr__()` and `__setattr__()`
   - starts with `__` Not inherited and used for Name mangling
   - Attributes should not end with "__" as it is reserved for internal usage.

> Private attribute and method example
```python
# Add class attributes for max number of days and months
class BetterDate:
    _MAX_DAYS = 30
    _MAX_MONTH = 12
    def __init__(self, year, month, day):
        self.year, self.month, self.day = year, month, day
        
    @classmethod
    def from_str(cls, datestr):
        year, month, day = map(int, datestr.split("-"))
        return cls(year, month, day)
    
    # Add _is_valid() checking day and month values
    def _is_valid(self):
        return (self.day<=BetterDate._MAX_DAYS) and (self.month<=BetterDate._MAX_MONTH)
    
bd1 = BetterDate(2020, 4, 30)
print(bd1._is_valid())
#True
bd2 = BetterDate(2020, 6, 45)
print(bd2._is_valid())
#False
```
5. The @property decorator is a built-in decorator in Python for the property() function. Use @property decorator on any method in the class to use the method as a property
   - `@property`: Declares the method as a property.
   - `@<property-name>.setter`: Specifies the setter method for a property that sets the value to a property.
   - `@<property-name>.deleter`: Specifies the delete method as a property that deletes a property.
> @property example:
```python
class Student:

    def __init__(self, name):
        self.__name=name

    @property
    def name(self):
        return self.__name

    @name.setter   #property-name.setter decorator
    def name(self, value):
        self.__name = value
```
> `@property`:Example 2
```python
class Customer:
    def __init__(self, name, new_bal):
        self.name = name
        if new_bal < 0:
           raise ValueError("Invalid balance!")
        self._balance = new_bal  

    # Add a decorated balance() method returning _balance        
    @property
    def balance(self):
        return self._balance

    # Add a setter balance() method
    @balance.setter
    def balance(self, new_bal):
        # Validate the parameter value
        if new_bal < 0:
           raise ValueError("Invalid balance!")
        self._balance = new_bal
        print("Setter method called")

# Create a Customer        
cust = Customer("Belinda Lutz",2000)

# Assign 3000 to the balance property
cust.balance=3000

# Print the balance property
print(cust.balance)
# Setter method called
# 3000
```

> `@property`: Read only example
```python
import pandas as pd
from datetime import datetime

# MODIFY the class to use _created_at instead of created_at
class LoggedDF(pd.DataFrame):
    def __init__(self, *args, **kwargs):
        pd.DataFrame.__init__(self, *args, **kwargs)
        self._created_at = datetime.today()
    
    def to_csv(self, *args, **kwargs):
        temp = self.copy()
        temp["created_at"] = self._created_at
        pd.DataFrame.to_csv(temp, *args, **kwargs)   
    
    # Add a read-only property: _created_at
    @property
    def created_at(self):
        return self._created_at

# Instantiate a LoggedDF called ldf
ldf = LoggedDF({"col1": [1,2], "col2":[3,4]}) 
```

 