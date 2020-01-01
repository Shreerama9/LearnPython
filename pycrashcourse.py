#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("hi srssbvs")


# *Part 1*
# 

# In[1]:


1.66666


# In[2]:


1+1


# In[3]:


1**9


# In[4]:


1/.2


# In[5]:


1/2.0


# In[6]:


2+3*5+5


# In[7]:


(2+3)*5+5


# In[8]:


4/2


# In[9]:


4%2


# In[10]:


var = 2


# In[11]:


var


# In[12]:


x = 2
y = 3


# In[13]:


x**3+y


# In[14]:


12*var


# #variables nust start with lower case letter

# In[17]:


num = 7
name = 'SR'


# In[18]:


'My number is {} and my name is {}'.format(num,name)


# In[19]:


'My number is {one} and my name is {two}'.format(one =num,two =name)


# In[20]:


s = 'hello'


# In[21]:


s[0]


# In[22]:


s[4]


# In[23]:


s[0:]


# In[25]:


a = 'asdfghjkl'


# In[26]:


a[:5]


# In[27]:


a[0:5]


# In[36]:


my_list = ['a','s','d']


# In[37]:


my_list


# In[38]:


my_list = ['a','s','d']


# In[42]:


my_list.append('f')
my_list


# In[43]:


my_list[0]


# In[44]:


my_list[1:3]


# In[45]:


my_list


# In[46]:


my_list[0] = 'NEW'


# In[47]:


my_list


# In[48]:


nest = [1,2,3,[4,5,['sr']]]


# In[49]:


nest[3][2][0]


# *Part 2*

# In[50]:


d = {'key1':'value','key2':123}


# In[51]:


d['key1']


# In[53]:


d = {'key1':{'innerkey':[1,2,3]}}


# In[54]:


d['key1']['innerkey'][1]


# In[56]:


t =(1,2,3,4)


# In[57]:


t


# tupple is inmutable

# *set*
# 

# In[59]:


{1,2,3,}


# In[66]:


s = {11,1,11,1,11,1,1,1,1,1,11,1,1,11,1,1,1,1,1,13,10002,444,5,5,9,}


# In[67]:


s


# In[68]:


s = {1,2,3,4}


# In[69]:


s.add(100)


# In[70]:


s


# In[71]:


1 > 3


# In[72]:


1>=1


# In[73]:


5<=8


# In[74]:


1==1


# In[75]:


1==3


# #not equal !

# In[80]:


1 != 3


# In[85]:


5231 != 0


# In[94]:


'hi!' != 'BYE'


# In[87]:


1 < 2 and 2 < 3


# In[88]:


1<2 or 3>7


# In[95]:


True and False


# In[105]:


if 1 != 10:
    print("Mathematician")
elif 8 == 9:
    print('learner')
else:
    print("noob")


# #Part 3

# In[107]:


seq = [1,2,3,4,5]


# In[114]:


for num in seq:
    print('sr')


# In[117]:


i = 0

while i < 10:
    print('number is : {}'.format(i))
    i = i+1


# In[118]:


for x in seq:
    print(x)


# In[122]:


list(range(10))


# In[121]:


for x in range(1,12):
    print('hi')


# In[123]:


x = [1,2,4,3,5]


# In[125]:


out= []

for num in x:
    out.append(num**3)


# In[126]:


print(out)


# #list comprehension

# In[128]:


out = [num**2 for num in x]


# In[129]:


out


# In[137]:


def my_func(name):
    print('HI '+name)


# In[139]:


name = input()
my_func(name)


# In[140]:


my_func


# In[156]:


def square(num):
    return num**2


# In[157]:


output = square(2)


# In[158]:


output


# In[ ]:





# In[ ]:





# In[ ]:




