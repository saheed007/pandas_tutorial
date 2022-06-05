import pandas as pd

df = pd.read_csv("C:\\Users\OLADEJO A Saheed\Desktop\Data sets\countries\populations.csv")
df2 = pd.read_csv("C:\\Users\OLADEJO A Saheed\Desktop\Data sets\countries\countries.csv")
econ = pd.read_csv("C:\\Users\OLADEJO A Saheed\Desktop\Data sets\countries\economies2010.csv")

##print(df.info())
# df.rename(columns = {"size":"pop_size"}, inplace = True)

# afr_pop_econ_2010 = df2[df2["continent"] == "Africa"][["code", "country_name", "capital"]].\
#       merge(df[df["year"] == 2010][["country_code", "pop_size", "life_expectancy"]], left_on ="code", right_on="country_code")\
#       .merge(econ[["code", "income_group", "gross_savings"]], left_on ="country_code", right_on="code")
# print(afr_pop_econ_2010.info())
# print(afr_pop_econ_2010.head())
# print(afr_pop_econ_2010[["code_x", "code_y", "country_code"]])

# # High income countries for 2010
# print(afr_pop_econ_2010[afr_pop_econ_2010["income_group"] == "High income"][["country_name", "capital", "income_group"]])
# print(afr_pop_econ_2010[afr_pop_econ_2010["income_group"] == "High income"][["country_name", "capital", "income_group"]].count())

# # Low income countries for 2010
# print(afr_pop_econ_2010[afr_pop_econ_2010["income_group"] == "Low income"][["country_name", "capital", "income_group"]])
# print(afr_pop_econ_2010[afr_pop_econ_2010["income_group"] == "Low income"][["country_name", "capital", "income_group"]].count())

# # Upper middle income countries for 2010
# print(afr_pop_econ_2010[afr_pop_econ_2010["income_group"] == "Upper middle income"][["country_name", "capital", "income_group"]])
# print(afr_pop_econ_2010[afr_pop_econ_2010["income_group"] == "Upper middle income"][["country_name", "capital", "income_group"]].count())

# # Lower middle income countries for 2010
# print(afr_pop_econ_2010[afr_pop_econ_2010["income_group"] == "Lower middle income"][["country_name", "capital", "income_group"]])
# print(afr_pop_econ_2010[afr_pop_econ_2010["income_group"] == "Lower middle income"][["country_name", "capital", "income_group"]].count())

print(df2.groupby("continent").agg({"continent":"count", "region": "count"}))

