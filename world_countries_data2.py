import pandas as pd
import numpy as np


countries = pd.read_csv("C:\\Users\OLADEJO A Saheed\Desktop\Data sets\countries\countries.csv")
countries = countries[["code", "country_name", "capital", "continent"]]
print(countries.head())


pop = pd.read_csv("C:\\Users\OLADEJO A Saheed\Desktop\Data sets\countries\populations.csv")
pop = pop[pop["year"] == 2010][["country_code", "size", "life_expectancy"]]


econ = pd.read_csv("C:\\Users\OLADEJO A Saheed\Desktop\Data sets\countries\economies2010.csv")
## #   Column         Non-Null Count  Dtype  
##---  ------         --------------  -----  
## 0   code           190 non-null    object 
## 1   year           190 non-null    int64  
## 2   income_group   190 non-null    object 
## 3   gross_savings  169 non-null    float64
##dtypes: float64(1), int64(1), object(2)

lang = pd.read_csv("C:\\Users\OLADEJO A Saheed\Desktop\Data sets\countries\languages.csv")
# Data columns (total 5 columns):
#  #   Column    Non-Null Count  Dtype  
# ---  ------    --------------  -----  
#  0   lang_id   955 non-null    int64  
#  1   code      955 non-null    object 
#  2   name      955 non-null    object 
#  3   percent   518 non-null    float64
#  4   official  955 non-null    bool  

