'''def print_rhombus(n):
    for row in range(n):
        for col in range(n):
            if abs(row - n // 2) + abs(col - n // 2) <= n // 2:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()  # Move to the next row

# Let's create a 5x5 hollow rhombus:
print_rhombus(5)'''

'''import pygame
import time
import random

pygame.init()
white =(255,255,255)
black = (0,0,0)
red=(255,0,0)
orange =(255,165,0)

width ,height = 600,400

game_display = pygame.display.set_mode(( width,height))
pygame.display.set_caption('Poorna_Games')

clock = pygame.time.Clock()

snake_size =10
snake_speed =15

message_font = pygame.font.SysFont('ubuntu',30)
score_font = pygame.font.SysFont('ubuntu',30)'''

'''import random
def set_number():
    s = [random.randint(15,45) for _ in range (30)]
    num = set()
    count_num = 0
    delete = set()
    for i in s:
        if i <30:
            num.add(i)
            count_num+=i
            print(f'The num are : {num}')
            print(f'count = {count_num}')
        elif i>=35:
            delete.add(i)
            print(f'The num deleted are {delete}')
set_number()'''

import random

'''def set_numbers():
    s = {random.randint(15, 45) for _ in range(10)}  # generate a list of 30 random numbers between 15 and 45
    print('Original set :',s)
    num = set()
    count_num = 0
    delete_set = set()

    for i in s:
        if i < 30:
            num.add(i)
            count_num += 1
            
        if i >= 35:
            delete_set.add(i)
    print(f'The numbers < 30 is : {num}')
    print(f'Count: {count_num}')
    print(f'The numbers > 30 is : {delete_set}')

set_numbers()'''


'''words = {'ast','bats','man','cat','loop','hens','kite','apple','van','sat','hate','good'}
set_item = {w for w in words if len(w)==4}
item = set_item
#item.add(set_item)
print(item)'''


'''n = input('Enter the number of elements: ')
n.split(',')
t=int(n)
tup = tuple()
tup.append(t)
for i in range(n):
    ele = int(input(f'Enter element {i+1}: '))
    tup = tup + (ele,)
print('Given tuple:', tup)
print('Maximum:', max(tup))
print('Minimum:', min(tup))
print('Length of tuple:', len(tup))
print('Sum of tuple elements:', sum(tup))
'''
'''
def tuple_is(n):
    tup = (2,5,8,9,4,1,7)
    print(f'Given tuple: {tup}')
    print('Element upto 2 to 6 :',tup[2:6])
    print('Element at begining to 6 :',tup[:6])
    print('Element from 4 to end :',tup[4:])
    print('Element from begining to end :',tup[:])
    print('Element at lace -5 to 2 :',tup[-5:-2])
    print('Element at place 3 :',tup[3])
n=10
tuple_is(n)'''
'''def num():
    list1=[]
    list2=[]
    for i in range(1,6):
        if i%2==0:
            list1.append(i)
        else:
            list2.append(i)
    list3 = [11,12,13]+list1+list2+[100,200,300]
    list3[0:] = []
    #list4 = [11,12,13]+list3
    #list5=list4.sort()
    print(f'list1{list1}')
    print(f'list2{list2}')
    print(f'Adding List1 and list2 : {list3}')
    #print(list4)
    #print(list4+[100,200,300])
    #print(list5)

num()'''

''''
name = 'Addya','Anith','Arpith','Bhart','Bhama','Bavaith'
set1={x for x in name if x.startswith('A')}
print(set1)
set2={x for x in name if x.startswith('B')}
print(set2)'''

'''for i in range(1,11):
    for j in range(1,11):
        print(f'{i}*{j}={i*j}')
        
    print()'''

'''for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=' ')
    print()'''

'''num = int(input('Enter the value : '))
i = 1
while i<=num:
    print(i)
    i+=1'''

'''i=1 
fact=1
while(i<=5):
    #print(fact)
    fact*=i
    print(fact)
    i+=1
#print(fact)'''



'''num = 123
rev = 0
while(num>0):
    rem = num%10
    rev = rev*10+rem
    num = num//10
print(rev)
'''
'''num = 345
sum = 0
while num>0:
    rem = num%10
    sum = sum+rem
    num = num//10
print(sum)'''

'''num = 153
temp = num
sum =0
while num>0:
    rem = num%10
    sum = sum + rem**3
    num = num//10
print(sum)
if sum == temp:
    print('Amstrong')
else:
    print('Not amsrtrong')
    '''
#--------Pygame ------------------

'''import pygame 
pygame.init()

#creating Windows
gamewindow = pygame.display.set_mode((1200,500))
pygame.display.set_caption('Gameing')
#Game specific Variable
exit_game = False
game_over = False
#Creating a game loop
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game =True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print('Right key')


pygame.quit()
quit()'''
#--------------------Pandas-----------------------
import pandas as pd
import numpy as np
# ------Series-----------
'''a = {1:pd.Series([1,2,3,4,5]),2:pd.Series([1,2,3,4,5])}
     
#var = pd.Series(a,dtype='float',name='Python_data')
print(a)

dic = {'AI':'Pyhton','APP':'Java','Data_Base':'SQL','IOS_App':'Swift','Android_App':'Kotlin'}
var1 = pd.Series(dic)
print(var1)'
print(type(var1))'''

#-------------Data frames--------------

'''b= np.array([[11,12,13,14],
             [13,14,15,16]]) #frames in list
var2 = pd.DataFrame(b)
print(var2)
print(type(var2))
print( )

b1 = dict({'Program':[1,2,3],'Fruits':['apple','mango','grapes'],'Pencil':['doms','apsara','classmet']})
var3 = pd.DataFrame(b1,index=['row1','row2','row3',])
print(var3)
print(var3['Program']['row2'])
print( )'''


#-----------------DataFrames  Arithmetic Operations-----------------

'''c= np.array([[11,12,13,14],
             [13,14,15,16]]) 
#c1 = c.T
df1 = pd.DataFrame(c,columns=['A','B','C','D'])
#print(df1)
df1['E'] = df1['A'] > 10 #df1['B'] - df1['C'] ** df1['D']
print(df1)
print( )

b1 = dict({'Program':['Python','Java','C++'],'Fruits':['apple','mango','grapes'],'Pencil':['doms','apsara','classmet']})
var3 = pd.DataFrame(b1,index=['row1','row2','row3',])
var3['Add'] = var3['Program']+var3['Fruits']+var3['Pencil']
print(var3)
print( )
'''
# ---------------------insert and delete----------------------------

'''d = {'Program':['Python','Java','C++'],'Fruits':['apple','mango','grapes'],'Pencil':['doms','apsara','classmet']}
var  = pd.DataFrame(d)
var.insert(3,'Python',[1,2,3]) #(index_value,column_name,value_which_has_to_be inserted)
var['Python'] = var['Program'][:1]#(another way of insertion)
print(var)
print()
pop = var.pop('Program')
print('The poped item ',pop)
print(var)
'''

#------------Write CSV File --------------------

'''dis = {'a':[1,2,3,4],'b':[11,12,13,14]}
d = pd.DataFrame(dis)
#print(d)
d.to_csv('Trail.csv',index=False)
# create csv file ('File_name',index_value(if want = true else false),header = name of the column )'''

#-----------------Read csv file----------------------------

'''csv_1 = pd.read_csv('Trail.csv',nrows=15,usecols=[0,1],skiprows=[2],dtype={'marks':'str'},)#index_col='marks') 
#csv_2=pd.read_csv('Trail.csv',names=['Student_names','Marks_obtained'])#changes column names
#csv_3 = pd.read_csv('Trail.csv',dtype={'marks':'float'})
print(csv_1)
'''
#-----------------Functions----------------------------

#csv_1 = pd.read_csv('Trail.csv')

#print(csv_1.describe())  (gives max,std,min....values)
#print(csv_1.index) (gives insex value from starting,end and stepwise)
#print(csv_1.columns) (gives the names of the columns which are present)
#print(csv_1.head()) (gives the top 5 values in a table , we can also pass parameter to head(2) gives only starting 2 rows)
#print(csv_1.tail()) (same has head( but it gives last 5 ending values ))
#print(csv_1[10:17]) (its slicing )
#print(csv_1.index.array) (converting index value to array)
#print(csv_1.to_dict) (converts the values to dictionary)
#print(csv_1.to_numpy) (converts the dataframe to numpy)
#sort = csv_1.sort_index(axis=1,ascending=False) #(axis=0 is sort by columns and axis=1 is sort by rows)
#print(sort) #sorts the index value in descending order
#s= csv_1.sort_values(by=['marks']) # sorting the value
#print(s)
#csv_1.loc[1,'name'] = 'poorna' # Replaceing the values in a column
#print(csv_1)
#csv_1.loc[[2,3],['name','marks']]
#print(csv_1.loc[[2,3],['name','marks']]) # accsseing only specific values from the particular table
#print(csv_1.iloc[28,3]) # accesing specific value by passing [row_index,column_index]
#print(csv_1.drop('maximum',axis=1)) # droping the column .drop('Column_name',axis = 1 is for specifing column)
#s = csv_1.rename(columns={'avg':'Average'})
#print(s) # replaceing the column name .rename(columns = {'old_name' : 'new_name})

#----------------Dropna and Fillna ------------------

var = pd.read_csv(r'C:\Users\Poornatejas\OneDrive\personal\wether.csv')
#print(var) # droping the crow which has nan value

print(var.columns)
print(var.index)
#print(var.sort_values(by=['Temp_C']))
print(var.nunique())