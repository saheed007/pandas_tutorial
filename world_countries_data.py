import pandas as pd
import numpy as np

countries = pd.read_csv("C:\\Users\OLADEJO A Saheed\Desktop\Data sets\countries\countries.csv")
##     Column         Non-Null Count  Dtype
##---  ------        --------------  ----- 
## 0   code          206 non-null    object 
## 1   country_name  206 non-null    object 
## 2   continent     206 non-null    object 
## 3   region        206 non-null    object 
## 4   surface_area  206 non-null    float64
## 5   indep_year    188 non-null    float64
## 6   local_name    206 non-null    object 
## 7   gov_form      206 non-null    object 
## 8   capital       201 non-null    object 
## 9   cap_long      204 non-null    float64
## 10  cap_lat       204 non-null    float64

populations = pd.read_csv("C:\\Users\OLADEJO A Saheed\Desktop\Data sets\countries\populations.csv")
##     Column           Non-Null Count  Dtype  
##---  ------           --------------  -----  
## 0   pop_id           434 non-null    int64  
## 1   country_code     434 non-null    object 
## 2   year             434 non-null    int64  
## 3   fertility_rate   402 non-null    float64
## 4   life_expectancy  398 non-null    float64
## 5   size             433 non-null    float64

econ = pd.read_csv("C:\\Users\OLADEJO A Saheed\Desktop\Data sets\countries\economies2010.csv")
## #   Column         Non-Null Count  Dtype  
##---  ------         --------------  -----  
## 0   code           190 non-null    object 
## 1   year           190 non-null    int64  
## 2   income_group   190 non-null    object 
## 3   gross_savings  169 non-null    float64
##dtypes: float64(1), int64(1), object(2)


#############   Analysis on african countries   ###################

# 1. Selecting all African countries with their capitals and independence year
african_ctr = countries[countries["continent"] == 'Africa'][["code","country_name", "capital", "indep_year"]]
print(african_ctr)
print("\n")
print(african_ctr[["indep_year"]].agg([np.min,np.max]))
print("\n")

# 2. Selecting the oldest and newest country in terms of independence
oldest_ctr = african_ctr[african_ctr["indep_year"] == african_ctr["indep_year"].min()][["code","country_name", "capital", "indep_year"]]
newest_ctr = african_ctr[african_ctr["indep_year"] == african_ctr["indep_year"].max()][["code","country_name", "capital", "indep_year"]]
oldest_and_newest = african_ctr[(african_ctr["indep_year"] == african_ctr["indep_year"].min())\
                        | (african_ctr["indep_year"] == african_ctr["indep_year"].max())]\
                    [["code","country_name", "capital", "indep_year"]]
print(oldest_ctr, newest_ctr)
print("\n")
print(oldest_and_newest)
print("\n")

# 3. Finding the number of countries that gained independence for each year
indep_by_year = pd.DataFrame(african_ctr[["indep_year"]].value_counts())
print(indep_by_year)
print("\n")

# 4. Finding the population details for African countries for 2010 and 2015

    # setting the index for both populations to be the code
new_pop = populations.set_index("country_code")
print(new_pop)
print("\n")

    # selecting only African countries from the populations matching them on the code
african_ctr_pop = new_pop.loc[african_ctr["code"]]
print(african_ctr_pop)
print("\n")

    # selecting the year 2010 only
african_ctr_pop_2010 = african_ctr_pop[african_ctr_pop["year"] ==2010]
print(african_ctr_pop_2010)
    # selecting the year 2015 only
african_ctr_pop_2015= african_ctr_pop[african_ctr_pop["year"] ==2015]
print(african_ctr_pop_2015)
print("\n")

# 4. Selecting the most and least populous countries

# max population
# getting the max population
most_pop = african_ctr_pop["size"].max()
print(most_pop)
#getting the country code fro the max pop
most_pop_code = african_ctr_pop.index[african_ctr_pop["size"]== most_pop]
print(most_pop_code)
# getting the country details using the code
print(african_ctr[african_ctr["code"] == most_pop_code[0]])
print("\n")

# min population
# getting the min population
least_pop = african_ctr_pop["size"].min()
print(least_pop)
#getting the country code fro the min pop
least_pop_code = african_ctr_pop.index[african_ctr_pop["size"]== least_pop]
print(least_pop_code)
# getting the country details using the code
print(african_ctr[african_ctr["code"] == least_pop_code[0]])

print(most_pop / least_pop)

