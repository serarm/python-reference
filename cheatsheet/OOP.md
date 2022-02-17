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

2. Comparing parent and child object methond, child object `__eq__()` is called






 