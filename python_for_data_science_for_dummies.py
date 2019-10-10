# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 12:57:24 2019

@author: rlangran
"""

## CHAPTER 4 - CREATING USABLE FUNCTIONS
def SayHello():
    print('Hello There!')

SayHello()

## CALLING FUNCTIONS IN A VARIETY OF WAYS
## Sending required arguments
def DoSum(Value1, Value2):
    return Value1 + Value2 #need print statement to see the result

#DoSum() #returns a TypeError - missing 2 positional arguments

print(DoSum(1, 2))

## Sending arguments by keyword
def DisplaySum(Value1, Value2):
    print(str(Value1) + ' + ' + str(Value2) + ' = ' +
    str((Value1 + Value2)))
    
DisplaySum(2,3)

## Giving function arguments a default value
def SayHello(Greeting = "No Value Supplied"):
    print(Greeting)
    
SayHello()
SayHello("Howdy")

## Creating functions with a variable number of arguments
def DisplayMulti(ArgCount = 0, *VarArgs):
    print('You passed ' + str(ArgCount) + ' arguments.',VarArgs)
    
#to pass zero arguments
DisplayMulti()
#pass multiple arguments
DisplayMulti(3, 'Hello', 1, True)

## Using Conditional and Loop Statements
## MAKING DECISIONS USING THE IF STATEMENT
def TestValue(Value):
    if Value == 5:
        print('Value equals 5!')
    elif Value == 6:
        print('Value equals 6!')
    else:
        print('Value is something else.')
        print('It equals ' + str(Value))
        
TestValue(1)
TestValue(5)
TestValue(6)

## CHOOSING BETWEEN MULTIPLE OPTIONS USING NESTED DECISIONS
def SecretNumber():
    One = int(input("Type a number between 1 and 10: "))
    Two = int(input("Type a number between 1 and 10: "))

    if (One >= 1) and (One <= 10):
        if (Two >= 1) and (Two <= 10):
           print('Your secret number is: ' + str(One * Two))
        else:
           print("Incorrect second value!")
    else:
        print("Incorrect first value!")
        
#SecretNumber()

## PERFORMING REPETITIVE TASKS USING FOR
def DisplayMulti(*VarArgs):
    for Arg in VarArgs:
        if Arg.upper() == 'CONT':
            continue
            print('Continue Argument: ' + Arg)
        elif Arg.upper() == 'BREAK':
            break
            print('Break Argument: ' + Arg)
        print('Good Argument: ' + Arg)

DisplayMulti('Hello', 'Goodbye', 'First', 'Last')
DisplayMulti('Hello', 'Cont', 'Goodbye', 'Break', 'Last')

## USING THE WHILE STATEMENT
def SecretNumber():
    GotIt = False
    while GotIt == False:
        One = int(input("Type a number between 1 and 10: "))
        Two = int(input("Type a number between 1 and 10: "))

        if (One >= 1) and (One <= 10):
            if (Two >= 1) and (Two <= 10):
                print('Secret number is: ' + str(One * Two))
                GotIt = True
                continue
            else:
                print("Incorrect second value!")
        else:
            print("Incorrect first value!")
        print("Try again!")
        
#SecretNumber()

## Storing Data Using Sets, Lists, and Tuples
## PERFORMING OPERATIONS ON SETS
# Sets are the best option to choose when you need to perform membership testing and remove duplicates 
# from a list. You can’t perform sequence-related tasks using sets, such a indexing or slicing.
# from sets import Set - not needed in Python 3
SetA = set(['Red', 'Blue', 'Green', 'Black']) #'Set' is now lowercase in Python 3
SetB = set(['Black', 'Green', 'Yellow', 'Orange'])
SetX = SetA.union(SetB)
SetY = SetA.intersection(SetB)
SetZ = SetA.difference(SetB)

print('{0}\n{1}\n{2}'.format(SetX, SetY, SetZ))

SetA.issuperset(SetY)
SetA.issubset(SetX)

SetA.add('Purple')
SetA.issubset(SetX)

## WORKING WITH LISTS
ListA = [0, 1, 2, 3]
ListB = [4, 5, 6, 7]
ListA.extend(ListB)
ListA

ListA.append(-5)
ListA.remove(-5)
ListX = ListA + ListB

## CREATING AND USING TUPLES
MyTuple = (1, 2, 3, (4, 5, 6, (7, 8, 9)))

for Value1 in MyTuple:
    if type(Value1) == int:
        print (Value1)
    else:
        for Value2 in Value1:
            if type(Value2) == int:
                print("\t", Value2)
            else:
                for Value3 in Value2:
                    print("\t\t", Value3)

MyNewTuple = MyTuple.__add__((10, 11, 12, (13, 14, 15)))

for Value1 in MyNewTuple:
    if type(Value1) == int:
        print (Value1)
    else:
        for Value2 in Value1:
            if type(Value2) == int:
                print("\t", Value2)
            else:
                for Value3 in Value2:
                    print("\t\t", Value3)

## Defining Useful Iterators
ListA = ['Orange', 'Yellow', 'Green', 'Brown']
ListB = [1, 2, 3, 4]

print(ListA[1])
print(ListB[1:3])

for Value in ListB[1:3]:
    print(Value)
 
# print two lists in parallel with "zip" function    
for Value1, Value2 in zip(ListA, ListB):
    print(Value1, '\t', Value2)
    
## Indexing Data Using Dictionaries - key value pair

MyDict = {'Orange':1, 'Blue':2, 'Pink':3}

print(MyDict['Pink']) # returns value of 'Pink'

print(MyDict.keys()) #shows all keys of 'MyDict'
print(MyDict.values()) #shows all values of 'MyDict'

## CHAPTER 5 - Working with Real Data

## UPLOADING SMALL AMOUNTS OF DATA INTO MEMORY

with open("Colors.txt", 'r') as open_file: #changed 'rb' to 'r' for Python 3
    print("Colors.txt content:\n" + open_file.read())
    
## STREAMING LARGE AMOUNTS OF DATA INTO MEMORY
with open("Colors.txt", 'r') as open_file: #changed 'rb' to 'r' for Python 3
    for observation in open_file:
        print("Reading Data: " + observation)

## SAMPLING DATA

n = 2
with open("Colors.txt", 'r') as open_file: #changed 'rb' to 'r' for Python 3
    for j, observation in enumerate(open_file): #the application uses enumerate() to retrieve a row number.
        if j % n==0: # "%" is used to divide two numbers and return the remainder 
            print('Reading Line: ' + str(j) +
            ' Content: ' + observation)

## using random number function
from random import random
sample_size = 0.25
with open("Colors.txt", 'r') as open_file: #changed 'rb' to 'r' for Python 3
    for j, observation in enumerate(open_file):
        if random()<=sample_size:
            print('Reading Line: ' + str(j) + 
            ' Content: ' + observation)

## Accessing Data in Structured Flat-File Form
## READING FROM A TEXT FILE
import pandas as pd
color_table = pd.io.parsers.read_table("Colors.txt")
print(color_table)

## READING CSV DELIMITED FORMAT
import pandas as pd
titanic = pd.io.parsers.read_csv("Titanic.csv")
X = titanic[['age']]
print(X)

X = titanic[['age']].values # To create the output as a list

## READING EXCEL AND OTHER MICROSOFT OFFICE FILES
xls = pd.ExcelFile("Values.xls")
trig_values = xls.parse('Sheet1', index_col=None, na_values=['NA'])
print(trig_values)

## Sending Data in Unstructured File Form
from skimage.io import imread
from skimage.transform import resize
from matplotlib import pyplot as plt
import matplotlib.cm as cm

example_file = (r'C:\Users\rlangran\Desktop\UT Data Analytics\Section 5\Dog_face.png') #changed this to a local drive
image = imread(example_file, as_grey=True)                                             #corp firewall blocks internet access
plt.imshow(image, cmap=cm.gray)
plt.show()

print("data type: %s, shape: %s" %
      (type(image), image.shape))

# if you want to crop the image, you can use the following code to manipulate the image array:
image2 = image[5:70,0:70]
plt.imshow(image2, cmap=cm.gray)
plt.show()

# The following code resizes the image to a specific size for analysis:
image3 = resize(image2, (30, 30), mode='constant') # 'nearest' mode not used in Python 3 - changed to 'constant'


plt.imshow(image3, cmap=cm.gray)
print("data type: %s, shape: %s" %
      (type(image3), image3.shape))

# After you have all the images the right size, you need to flatten them. A dataset row is always a single dimension, 
# not two dimensions. The image is currently an array of 30 pixels by 30 pixels, so you can’t make it part of a dataset.
# The following code flattens image3 so that it becomes an array of 900 elements that is stored in image_row.
image_row = image3.flatten()
print("data type: %s, shape: %s" %
      (type(image_row), image_row.shape))

## Managing Data from Relational Databases
# The first step is to gain access to the database engine. You use two lines of code similar to the following code 
# (but the code presented here is not meant to execute and perform a task):

#from sqlalchemy import create_engine
#engine = create_engine('sqlite:///:memory:')

#read_sql_table(): Reads data from a SQL table to a DataFrame object
#read_sql_query(): Reads data from a database using a SQL query to a DataFrame object
#read_sql(): Reads data from either a SQL table or query to a DataFrame object
#DataFrame.to_sql(): Writes the content of a DataFrame object to the specified tables in the database
            
## Interacting with Data from NoSQL Databases
# These Not only SQL (NoSQL) databases are used in large data storage scenarios in which the relational model can 
# become overly complex or can break down in other ways. The databases generally don’t use the relational model. 

# for example, when working with MongoDB (https://www.mongodb.org/), you must obtain a copy of the PyMongo library 
# (https://api.mongodb.org/python/current/) and use the MongoClient class to create the required engine. 
# The MongoDB engine relies heavily on the find() function to locate data. Here’s a pseudo-code example of a MongoDB session:

#import pymongo
#import pandas as pd
#from pymongo import Connection
#connection = Connection()
#db = connection.database_name
#input_data = db.collection_name
#data = pd.DataFrame(list(input_data.find()))

## Accessing Data from the Web

# One of the most beneficial data access techniques to know when working with web data is accessing XML. 
# All sorts of content types rely on XML, even some web pages. Working with web services and microservices means working 
# with XML

from lxml import objectify

# The example begins by importing libraries and parsing the data file using the objectify.parse() method. 
# Every XML document must contain a root node, which is <MyDataset> in this case. The root node encapsulates the rest of 
# the content, and every node under it is a child. To do anything practical with the document, you must obtain access to 
# the root node using the getroot() method.
xml = objectify.parse(open('XMLData.xml'))
root = xml.getroot()

df = pd.DataFrame(columns=('Number', 'String', 'Boolean'))

# The for loop fills the DataFrame with the four records from the XML file (each in a <Record> node).

# The process looks complex but follows a logical order. The obj variable contains all the children for one <Record> node.
# These children are loaded into a dictionary object in which the keys are Number, String, and Boolean to match the DataFrame
# columns.

# There is now a dictionary object that contains the row data. The code creates an actual row for the DataFrame next. 
# It gives the row the value of the current for loop iteration. It then appends the row to the DataFrame. 

for i in range(0,4):
    obj = root.getchildren()[i].getchildren()
    row = dict(zip(['Number', 'String', 'Boolean'],
                   [obj[0].text, obj[1].text,
                    obj[2].text]))
    row_s = pd.Series(row)
    row_s.name = i
    df = df.append(row_s)

print(df)












