import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv(r"C:\Users\OLADEJO A Saheed\Desktop\Data sets\homelessness.csv", index_col=0)
# (df.info())
## Int64Index: 51 entries, 0 to 50
## Data columns (total 5 columns):
## #   Column          Non-Null Count  Dtype  
##---  ------          --------------  -----  
## 0   region          51 non-null     object 
## 1   state           51 non-null     object 
## 2   individuals     51 non-null     float64
## 3   family_members  51 non-null     float64
## 4   state_pop       51 non-null     int64  

df_2 = pd.read_csv(r"C:\Users\OLADEJO A Saheed\Desktop\Data sets\world_ind_pop_data.csv", index_col=0)
## (df_2.info())
## Index: 13374 entries, Arab World to Zimbabwe
## Data columns (total 4 columns):
## #   Column                         Non-Null Count  Dtype  
##---  ------                         --------------  -----  
## 0   CountryCode                    13374 non-null  object 
## 1   Year                           13374 non-null  int64  
## 2   Total Population               13374 non-null  float64
## 3   Urban population (% of total)  13374 non-null  float64
###Plot of the regions

df_3 = pd.read_csv(r"C:\Users\OLADEJO A Saheed\Desktop\Data sets\countries\countries.csv", index_col=0)
## (df_3.info())
##Index: 206 entries, AFG to PSE
##Data columns (total 10 columns):
## #   Column        Non-Null Count  Dtype  
##---  ------        --------------  -----  
## 0   country_name  206 non-null    object 
## 1   continent     206 non-null    object 
## 2   region        206 non-null    object 
## 3   surface_area  206 non-null    float64
## 4   indep_year    188 non-null    float64
## 5   local_name    206 non-null    object 
## 6   gov_form      206 non-null    object 
## 7   capital       201 non-null    object 
## 8   cap_long      204 non-null    float64
## 9   cap_lat       204 non-null    float64

df["region"].hist(bins=30)
plt.show()

#Total individuals per region
selection1 = df[['region','individuals']]
selection1 = selection1.groupby('region')['individuals'].sum()
selection1.plot(kind = "bar", title = "Total individuals by region", rot = 60)
plt.show()

#Total individuals per state
selection1 = df[['state','individuals']]
selection1 = selection1.groupby('state')['individuals'].sum()
selection1.plot(kind = "bar", title = "Total individuals by state", rot = 30)
plt.show()

# sHOWING THE CHANGE IN POPULATION OF NIGERIA OVER THE YEARS

nigeria = df_2[df_2["CountryCode"]=="NGA"]
nigeria.plot( x = "Year", y="Total Population", kind="line", title = "Graph of Nigeria population against year")
plt.show()

# Layering plots
df_3[df_3["continent"]== "Africa"]["gov_form"].hist(legend =True, alpha = 0.5, bins = 20)
df_3[df_3["continent"]== "Europe"]["gov_form"].hist(legend =True, alpha = 0.5, bins = 20, xrot = 60)
plt.legend(["Africa", "Europe"])
plt.show()

df[['state_pop','individuals']].plot( x = "state_pop", y="individuals", kind="scatter")
df[['state_pop','family_members']].plot( x = "state_pop", y="family_members", kind="scatter")

plt.show()
