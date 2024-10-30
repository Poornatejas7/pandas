#--------------------Pandas-----------------------
import pandas as pd
import numpy as np
# ------Series-----------
a = {1:pd.Series([1,2,3,4,5]),2:pd.Series([1,2,3,4,5])}
     
#var = pd.Series(a,dtype='float',name='Python_data')
print(a)

dic = {'AI':'Pyhton','APP':'Java','Data_Base':'SQL','IOS_App':'Swift','Android_App':'Kotlin'}
var1 = pd.Series(dic)
print(var1)'
print(type(var1))

#-------------Data frames--------------

b= np.array([[11,12,13,14],
             [13,14,15,16]]) #frames in list
var2 = pd.DataFrame(b)
print(var2)
print(type(var2))
print( )

b1 = dict({'Program':[1,2,3],'Fruits':['apple','mango','grapes'],'Pencil':['doms','apsara','classmet']})
var3 = pd.DataFrame(b1,index=['row1','row2','row3',])
print(var3)
print(var3['Program']['row2'])
print( )


#-----------------DataFrames  Arithmetic Operations-----------------

'c= np.array([[11,12,13,14],
             [13,14,15,16]]) 
c1 = c.T  #Transpose array elements
df1 = pd.DataFrame(c,columns=['A','B','C','D'])
print(df1)
df1['E'] = df1['A'] > 10 #df1['B'] - df1['C'] ** df1['D']
print(df1)
print( )

b1 = dict({'Program':['Python','Java','C++'],'Fruits':['apple','mango','grapes'],'Pencil':['doms','apsara','classmet']})
var3 = pd.DataFrame(b1,index=['row1','row2','row3',])
var3['Add'] = var3['Program']+var3['Fruits']+var3['Pencil']
print(var3)
print( )

# ---------------------insert and delete----------------------------

d = {'Program':['Python','Java','C++'],'Fruits':['apple','mango','grapes'],'Pencil':['doms','apsara','classmet']}
var  = pd.DataFrame(d)
var.insert(3,'Python',[1,2,3]) #(index_value,column_name,value_which_has_to_be inserted)
var['Python'] = var['Program'][:1]#(another way of insertion)
print(var)
print()
pop = var.pop('Program')
print('The poped item ',pop)
print(var)


#------------Write CSV File --------------------

dis = {'a':[1,2,3,4],'b':[11,12,13,14]}
d = pd.DataFrame(dis)
print(d)
d.to_csv('Trail.csv',index=False)
# create csv file ('File_name',index_value(if want = true else false),header = name of the column )

#-----------------Read csv file----------------------------

csv_1 = pd.read_csv('Trail.csv',nrows=15,usecols=[0,1],skiprows=[2],dtype={'marks':'str'},)#index_col='marks') 
csv_2=pd.read_csv('Trail.csv',names=['Student_names','Marks_obtained'])#changes column names
csv_3 = pd.read_csv('Trail.csv',dtype={'marks':'float'})
print(csv_1)

#-----------------Functions----------------------------

csv_1 = pd.read_csv('Trail.csv')

print(csv_1.describe()) # (gives max,std,min....values)
print(csv_1.index) #(gives insex value from starting,end and stepwise)
print(csv_1.columns) #(gives the names of the columns which are present)
print(csv_1.head())# (gives the top 5 values in a table , we can also pass parameter to head(2) gives only starting 2 rows)
print(csv_1.tail()) #(same has head( but it gives last 5 ending values ))
print(csv_1[10:17])# (its slicing )
print(csv_1.index.array) #(converting index value to array)print(csv_1.to_dict) (converts the values to dictionary)
print(csv_1.to_numpy) #(converts the dataframe to numpy)
sort = csv_1.sort_index(axis=1,ascending=False) 
#(axis=0 is sort by columns and axis=1 is sort by rows)#print(sort) #sorts the index value in descending order
s= csv_1.sort_values(by=['marks']) # sorting the value
#print(s)
csv_1.loc[1,'name'] = 'poorna' # Replaceing the values in a column
print(csv_1)
csv_1.loc[[2,3],['name','marks']]
print(csv_1.loc[[2,3],['name','marks']]) # accsseing only specific values from the particular table
print(csv_1.iloc[28,3]) # accesing specific value by passing [row_index,column_index]
print(csv_1.drop('maximum',axis=1)) # droping the column .drop('Column_name',axis = 1 is for specifing column)
s = csv_1.rename(columns={'avg':'Average'})
print(s) # replaceing the column name .rename(columns = {'old_name' : 'new_name})

#----------------Dropna and Fillna ------------------

var = pd.read_csv(r'C:\Users\Poornatejas\OneDrive\personal\wether.csv')
print(var) # droping the crow which has nan value

print(var.columns)
print(var.index)
#print(var.sort_values(by=['Temp_C']))
print(var.nunique())
