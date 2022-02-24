# Writing Efficient Python Code

This cheatsheet is built based on [DataCamp course: *Writing Efficient Python Code*](https://campus.datacamp.com/courses/writing-efficient-python-code)

## Foundations of efficiencies

1. Try to follow pythonic way and follow `zen of python`
```python
# Print the list created using the Non-Pythonic approach
i = 0
new_list= []
while i < len(names):
    if len(names[i]) >= 6:
        new_list.append(names[i])
    i += 1
print(new_list)

# Print the list created by looping over the contents of names
better_list = []
for name in names:
    if len(name) >= 6:
        better_list.append(name)
print(better_list)

# Print the list created by using list comprehension
best_list = [name for name in names if len(name) >= 6]
print(best_list)
```

2. Python has hundreds of `Python Enhancement Proposals`, commonly referred to as `PEPs`. The Zen of Python is one of these PEPs and is documented as [PEP20](https://www.python.org/dev/peps/pep-0020/).One little Easter Egg in Python is the ability to print the Zen of Python using the command `import this`.
3. Few important built-in function: `range()`,`enumerate(list,start=)`,`map(func,obj)`
```python
# Rewrite the for loop to use enumerate
indexed_names = []
for i,name in enumerate(names):
    index_name = (i,name)
    indexed_names.append(index_name) 
print(indexed_names)

# Rewrite the above for loop using list comprehension
indexed_names_comp = [(i,name) for i,name in enumerate(names)]
print(indexed_names_comp)

# Unpack an enumerate object with a starting index of one
indexed_names_unpack = [*enumerate(names, start=1)]
print(indexed_names_unpack)
```
```python
# Use map to apply str.upper to each element in names
names_map  = map(str.upper, names)

# Print the type of the names_map
print(type(names_map))

# Unpack names_map into a list
names_uppercase = [*names_map]

# Print the list created above
print(names_uppercase)
```

4. Use numpy instead of list.Numpy is fast and memory efficient alternative to python list. 
   + Important methods: `.dtype`.Numpy array have homogenous data type
   + Numpy array supports broadcasting(vectorization)
   + Better indexing compare to python list
   + Boolean indexing


