import pandas as pd

# creating a dataframe from a dictionary (for small datsets)
dict ={ "State": ["Abuja", "Lagos", "Ogun", "Oyo"],
        "Capital city": ["Abuja", "Ikeja", "Abeokuta", "Ibadan"],
        "Population":[4.1,9.6,3.6,4.0],
        "GDP":[2.5,6.4,3.0,4.3]}
table= pd.DataFrame(dict)
table.index=["ABJ","LAG","OG","OYO"]
print(table)
print("\n")
print(table.T) # Transpose of the table
print("\n")
print(table.GDP.aggregate)
print("\n")


# creating a dataframe from imported files (for large datsets)
table2 = pd.read_csv\
         ("C:\\Users\OLADEJO A Saheed\Desktop\Data Engineering Documents\Data sets\grid.csv",\
          index_col=0 # sets the first column as the index column, rather than
          #creating a new one
          )
print(table2)
print("\n")

# Index and selecting
print(table2["affected_customers"][:30]) # returns a series instead of data frame
                                         # check type(table2["affected_customers"][:30])

print(table2[["affected_customers"]]) # returns a dataframe (bcos of d double sqr brckts)

for x in table2["affected_customers"][800:807]:
    if x == 0.0:
        print(x)
print(table2[:5][:3])

for val in table:
    print(val)
print("\n")
for x,y in table.iterrows():
    print(x)
    print(y)
    print("\n")

for x,y in table.iterrows():
    print(f'{x} GDP is {y["GDP"]}')
    print("\n")
