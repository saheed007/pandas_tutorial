import pandas as pd

# creating a dataframe from imported files (for large datsets)
population = pd.read_csv\
         ("C:\\Users\OLADEJO A Saheed\Desktop\Data Engineering Documents\Data sets\countries\populations.csv",\
          index_col=0 # sets the first column as the index column, rather than
          #creating a new one
          )
# COMMON DATAFRAME ATTRIBUTES
print(population.head())
print(population.info())
print(population.shape)
print(population.describe())
print(population.columns)
print(population.index)
print(population.values)

# SELECTING A PARTICULAR COLUMN: dataframe['column_name']
print(population['country_code'].head())

# SELECTING MULTIPLE COLUMNS: dataframe[['column_1', 'column_2']]
print(population[['country_code', 'life_expectancy']].sort_values('life_expectancy'))

# SUBSETTING SPECIFIC ROW: dataframe[dataframe["column"] >= value]
print(population[population['year'] == 2010].head())

