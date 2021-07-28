#!/usr/bin/env python
# coding: utf-8

# In[35]:


for i in range (10):
    print(i)
#for j in range (1,10):
    #print(j)


# In[20]:


my_name= ('gary')
for value in (my_name):
    print(value)


# In[36]:


list_1=('gary',6,'hary',1,5,5,'marry','jarry')
#print(list_1)
for name in list_1:
    print(name)


# In[6]:


a =['a','b','c','d','e','f',]
for i in a:
   print (i)


# In[ ]:





# In[ ]:



# creating an empty list
lst =[]
 
# number of elements as input
n = int(input("Enter number of elements : "))
 
# iterating till the range
for i in range(, n):
    ele = int(input())
 
    lst.append(ele) # adding the element
     
print(lst)


# In[52]:



# creating an empty list
lst =[]
 
# number of elements as input
n = int(input("Enter number of elements : "))
 
# iterating till the range
for i in range(0,n):
    ele = str(input())
 
    
    lst.append(ele) # adding the element
     
print(lst)


# In[3]:


from  sklearn.datasets import load_iris  
iris=load_iris()
type (iris)


# In[6]:


print (iris.data)


# In[8]:


print (iris.target)


# In[11]:


print (iris.feature_names)


# In[12]:


print(iris.target_names)


# In[16]:


print (iris.target_names[iris.target])
print (len(iris.target))


# In[17]:


type (iris.target)


# In[19]:


print(iris.data.shape)


# In[16]:


import pandas as pd
d = {  
    'Employee_id': ['1', '2', '3', '4', '5',''],
    'Employee_name': ['Akshar', 'Jones', 'Kate', 'Mike', 'Tina','gary']
}
df1 = pd.DataFrame(d, columns=['Employee_id', 'Employee_name'])  
print(df1.size)
print(df1)
type(d)
del 'akshar'


# In[35]:


import pandas as pd 
from pandas import DataFrame


# In[47]:


df = pd.read_csv (r'documents\an.csv')
#print (df)
#print (df.shape)
for ind in df.index:
    print(df['value'][ind],df['unit'][ind])
print(df.index)  


# In[24]:


def add():
    no_1=float(input("enter 1st no :"))
    no_2= float(input("enter 2nd no :")) 
    result1= no_1+no_2
    return (result)
    
    
no=float(input ("select one option 1,2,3,4 "))
if no==1:
    add();

    


# In[1]:


shopelist= ['pen','peper','notbook','tep']
print(shopelist)


# In[5]:


shopelist.append('pencil')
print(shopelist)


# In[6]:


shopelist.sort()
print(shopelist)


# In[9]:


type(shopelist)
shopelist.remove('pen')
print(shopelist)


# In[18]:


for item in shopelist :
    print(item, end = "-")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




