## 1. Basic function

Inspecting the dataframe:
+ `.head()`: returns the first few rows (the “head” of the DataFrame).
+ `.info()`: shows information on each of the columns, such as the data type and number of missing values.
+ `.shape`: returns the number of rows and columns of the DataFrame.
+ `.describe()`: calculates a few summary statistics for each column.


```python
# Function working on pandas dataframe test
# Print the head of the test data
print(test.head())

# Print information about test
print(test.info())

# Print the shape of test
print(test.shape)

# Print a description of test
print(test.describe())
```

To better understand DataFrame objects, it's useful to know that they consist of three components, stored as attributes:

+ `.values`: A two-dimensional NumPy array of values.
+ `.columns`: An index of columns: the column names.
+ `.index`: An index for the rows: either row numbers or row names.

## 2. Sorting and subsetting

|Sort on|	Syntax|
|----|----|
|one column	|df.sort_values("col1")|
|multiple columns|	df.sort_values(["col1", "col2"],ascending=[True,False])|

<br>
Square brackets ([]) can be used to select only the columns that matter and in an order that makes sense.

```python
# To select only "col_a" of the DataFrame df, use
df["col_a"]

#To select "col_a" and "col_b" of df, use

df[["col_a", "col_b"]]
```
<br>
There are many ways to subset a DataFrame, perhaps the most common is to use relational operators to return True or False for each row, then pass that inside square brackets.

```python
dogs[dogs["height_cm"] > 60]
dogs[dogs["color"] == "tan"]
# Filter for multiple conditions at once by using the "bitwise and" operator, &.

dogs[(dogs["height_cm"] > 60) & (dogs["color"] == "tan")]
# Multiples values
dogs[dogs["color"].isin(["black","white","red"])]
```