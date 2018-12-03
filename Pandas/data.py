import os
import xlrd
import pandas 

#we can re used this variable
path = "C:\Users\haide\code\PythonBootCamp\Pandas"

# # CSV file
df1 = pandas.read_csv(path + "\supermarkets.csv")
print(df1.set_index("ID"))

#get the info of table
print(df1.info())

# # json file
# df2 = pandas.read_json(path + "\supermarkets.json")
# print(df2.set_index("ID"))

# # txt file
# df3 = pandas.read_csv(path + "\supermarkets-semi-colons.txt")
# print(df3)

# # text file with seperator
# df4 = pandas.read_csv(path + "\supermarkets-semi-colons.txt",sep=";")
# print(df4)


#Indexing
# df2 = pandas.read_csv(path + "\supermarkets.csv")

# #set index of ID
# print(df2.set_index("ID")) 

# #get only those rows where employees are less then 20
# df_low= df2.loc[df2["Employees"]<20]
# print(df_low)

# #get only those rows where employees are less then 20
# df_high= df2.loc[df2["Employees"]>20]
# print(df_high)



# #data group by City
# df3 = df2.groupby(['City'])['ID'].count()

# print(df3)




