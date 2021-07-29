import pandas as pd

print(pd.__version__)

#series - Series is like a column
a = [2,5,7]
pdvar = pd.Series(a)
print(pdvar)

print(pdvar[1])

##creating our own labels
a = [2,5,7]
pdvar = pd.Series(a, index=["x", "y", "z"])
print(pdvar)
print(pdvar["z"])

#Key/Value Objects as Series
calories ={"day1": 2000, "day2": 2300, "day3": 2200}

myvar = pd.Series(calories)
print(myvar)
myvar1 = pd.Series(calories, index=["day1", "day2"])  #select only some of the items in the dictionary
print(myvar1)


#Data sets in Pandas are usually multi-dimensional tables, called DataFrames.
#DataFrame is the whole table

data = {
    "calories": [420, 500, 600],
    "duration": [40, 50, 60]
}

myvar = pd.DataFrame(data)
print(myvar)
myvar1 = pd.DataFrame(data, index=["day1", "day2", "day3"])   #Named Indexes
print(myvar1)

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)
print(myvar)
print("####")
print(myvar.loc[1]) #locate 1 row
print(myvar.loc[[1,2]])   #locate 1 or more row
print(myvar1.loc[["day2", "day3"]])


#Load a comma separated file (CSV file) into a DataFrame:

dfc = pd.read_csv(r"C:\Users\kiran\OneDrive\Desktop\data.csv")
print(dfc)  #By default, when you print a DataFrame, you will only get the first 5 rows, and the last 5 rows:
print(dfc.to_string())   #to_string() to print the entire DataFrame.


#Load the JSON file into a DataFrame:
dfj =pd.read_json(r"C:\Users\kiran\OneDrive\Desktop\haha.json")
print(dfj.to_string())

#Dictionary as JSON. #JSON = Python Dictionary
data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409,
    "1":479,
    "2":340,
    "3":282,
    "4":406,
    "5":300
  }
}

df = pd.DataFrame(data)
#print(df)

#Viewing the Data
print(dfc.head(29)) #by default 5
print(dfc.tail(10)) #by default 5
print(dfc.info())  #gives details of how many non null values

#Data Cleaning
#Remove bad data. Bad data could be:
#1.Empty cells
#2.Data in wrong format
#3.Wrong data
#4.Duplicates
dfc =pd.read_csv(r"C:\Users\kiran\OneDrive\Desktop\dirtydata.csv")
new_dfc = dfc.dropna()  #remove rows that contain empty cells.
print(new_dfc.to_string())
#By default, the dropna() method returns a new DataFrame, and will not change the original.
#If you want to change the original DataFrame, use the inplace = True argument
dfc.dropna(inplace=True)
print(dfc.to_string())

#Replace Empty Values
#The fillna() method allows us to replace empty cells with a value
dfc =pd.read_csv(r"C:\Users\kiran\OneDrive\Desktop\dirtydata.csv")
dfc.fillna(130, inplace=True)  #Replace NULL values with the number 130:
print(dfc.to_string())

#Replace Only For a Specified Columns

print(dfc['Calories'].nlargest(2)) #2nd largest value in a column

dfc['Address'] = "Bangalore"
print(dfc.to_string())

print("###################")
dfc =pd.read_csv(r"C:\Users\kiran\OneDrive\Desktop\dirtydata.csv")
x = dfc['Calories'].mean()     #Calculate the MEAN, and replace any empty values with it
dfc.fillna(x, inplace=True)
print(dfc.to_string())

dfc =pd.read_csv(r"C:\Users\kiran\OneDrive\Desktop\dirtydata.csv")
x = df["Calories"].median()          #Calculate the MEDIAN, and replace any empty values with it
x = dfc['Calories'].mode()[0]        #Calculate the MODE, and replace any empty values with it
dfc.fillna(x, inplace=True)
#print(dfc.to_string())

#convert all cells in the 'Date' column into dates
dfc =pd.read_csv(r"C:\Users\kiran\OneDrive\Desktop\dirtydata.csv")
dfc['Date'] = pd.to_datetime(dfc['Date'])
#print(dfc.to_string())       #wrong date FORMAT corrected. But if it is empty it will not work
dfc.dropna(inplace=True)
dfc.dropna(subset=['Date'], inplace=True)    #Dropping only the empty date column row
#print(dfc.to_string())

#Fixing Wrong Data    Replacing Values
dfc.loc[7, 'Duration'] = 45

#Loop through all values in the "Duration" column.
#If the value is higher than 120, set it to 120
for x in dfc.index:
  if dfc.loc[x, 'Duration'] > 120:
    dfc.loc[x, 'Duration'] = 120
print(dfc.to_string())

for x in dfc.index:
  if dfc.loc[x, 'Duration'] > 120:
    dfc.drop(x, inplace=True)
print(dfc.to_string())

#Removing Duplicates
print(dfc.duplicated())  #Returns True for every row that is a duplicate, othwerwise False
dfc.drop_duplicates(inplace=True)    #Remove all duplicates
#print(dfc.info())

##Data Correlations
#number varies from -1 to 1
#1 means that there is a 1 to 1 relationship (a perfect correlation),
#and for this data set, each time a value went up in the first column, the other one went up as well.
#-0.9 would be just as good relationship as 0.9, but if you increase one value, the other will probably go down.
#0.2 means NOT a good relationship, meaning that if one value goes up does not mean that the other will.
###at least 0.6 (or -0.6) to call it a good correlation.
print(dfc.corr())


#Pandas - Plotting
import pandas as pd
import matplotlib.pyplot as plt
dfg = pd.read_csv(r"C:\Users\kiran\OneDrive\Desktop\pltgraph.csv")
dfg.plot()            #full data
dfg.plot(x= 'Duration', y='Calories')      #duration as x axis and calories as y axis
dfg['Calories'].plot()              #plotting only calories
plt.show()

#Scatter Plot
dfg.plot(kind='scatter', x= 'Duration', y='Calories')
plt.show()

#Histogram
dfg['Calories'].plot(kind = 'hist')
plt.show()


