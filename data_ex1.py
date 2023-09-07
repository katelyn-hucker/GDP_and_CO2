import pandas as pd
import matplotlib.pyplot as plt
data1 = pd.read_csv('https://media.githubusercontent.com/media/nickeubank/MIDS_Data/master/World_Development_Indicators/wdi_small_tidy_2015.csv')
print(data1)

mortalityrate = data1['Mortality rate, infant (per 1,000 live births)']
gdp = data1['GDP per capita (constant 2010 US$)']

x = mortalityrate
y = gdp

plt.scatter(x, y)
