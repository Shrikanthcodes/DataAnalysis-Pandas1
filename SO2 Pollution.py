#All print statements are saved as comments
#Analysis of SO2 emmissions in the world


#Importing pandas for data analysis
import pandas as pd

 #Importing the CSV File to the dataframe to read data from
df = pd.read_csv('SO2emi.csv')

#Assigning the column names to the dataframe
df = df[['Entity', 'Code', 'Year', 'Tonnes']]

#Optional Print, in this case tail() prints the last 5 elements
#print(df.tail()) 

#We drop the column 'Code' because it is redundant
df.drop('Code', inplace=True, axis=1)

#Another optional print, head() prints first 5 elements
#print(df.head())

#We group the dataframe by 'Entities', and store the sum of all matching entities in 'Tonnes'
cf = df.groupby(['Entity'])[['Tonnes']].sum().reset_index()

#We sort the dataframe in ascending order with respect to 'Tonnes'
cf = cf.sort_values(['Tonnes'], ascending=True)

#Optional print statement to print the entire dataframe
#print(cf)

#We group the dataframe by 'Year', and store the sum of all matching entities in 'Tonnes'
ef = df.groupby(['Year'])[['Tonnes']].sum().reset_index()

#We sort the dataframe in ascending order with respect to 'Tonnes'
ef = ef.sort_values(['Tonnes'], ascending=True)

#Prints all years with SO2 emission greater than 250
#print(ef[ef.Tonnes> 250][['Year','Tonnes']])

#Prints the mean of SO2 emissions per region
#print(cf['Tonnes'].mean())

#Prints the maximum SO2 value by region
#print(cf['Tonnes'].max())
