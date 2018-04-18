
# coding: utf-8

# In[14]:


from datascience import *
import numpy as np

get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plots
plots.style.use('fivethirtyeight')


# ## Strings

# In[1]:


'I love tennis'


# In[2]:


'2.3'


# In[3]:


'2.3' + 4


# In[4]:


'2.3' * 4


# In[5]:


'be' + 'happy'


# In[6]:


str(2.3)


# In[15]:


int('2.3')


# In[8]:


float('2.3')


# In[9]:


int('23') + float('2.3')


# In[10]:


x = 12


# In[11]:


int(str(x) + '0')


# <br><br><br><br><br><br><br><br><br><br><br><br>

# ## Minard's map

# In[16]:


minard = Table.read_table('minard.csv')


# In[17]:


minard


# In[18]:


minard.num_columns


# In[19]:


minard.num_rows


# In[20]:


minard.labels


# In[21]:


minard.column('Survivors')


# In[22]:


minard.column(4)


# In[23]:


initial_size = minard.column('Survivors').item(0)


# In[24]:


initial_size


# In[25]:


percentage_surviving = minard.column('Survivors')/initial_size


# In[26]:


percentage_surviving


# In[27]:


with_percentages = minard.with_column('Percent Surviving', percentage_surviving)


# In[28]:


with_percentages


# In[29]:


with_percentages.set_format('Percent Surviving', PercentFormatter)


# <br><br><br><br><br><br><br><br><br><br><br><br>

# ## Lists

# In[30]:


2


# In[31]:


2.0


# In[32]:


make_array(2, 3.0)


# In[33]:


make_array(2, 3.0).item(0)


# In[34]:


make_array(2, 'three')


# In[35]:


make_array(2, 'three').item(0)


# In[36]:


[2, 'three']


# In[37]:


type([2, 'three'])


# In[38]:


flowers = Table.read_table('flowers.csv')


# In[39]:


flowers


# In[40]:


my_favorite_flower = [5, 'morning glory', 'purple']


# In[41]:


flowers.with_row(my_favorite_flower)


# ## Table operations: Take

# In[42]:


minard


# In[43]:


minard.take(0)


# In[44]:


minard.take([0, 1, 2, 3])


# In[45]:


np.arange(0, 4)


# In[46]:


minard.take(np.arange(0,4))


# <br><br><br><br><br><br><br><br><br><br><br><br>

# ## Table operations: where

# In[47]:


# This table can be found online: https://www.statcrunch.com/app/index.php?dataid=1843341
nba = Table.read_table('nba_salaries.csv')


# In[48]:


nba


# In[49]:


nba.sort('2015-2016 SALARY')


# In[50]:


nba = nba.relabeled('2015-2016 SALARY', 'SALARY')


# In[51]:


nba.sort('SALARY')


# In[52]:


nba.where('SALARY', are.above(10))


# In[53]:


nba.where('SALARY', are.above(10)).sort('SALARY')


# In[54]:


nba.where('SALARY', are.between(10, 11))


# In[55]:


nba.where('TEAM', are.equal_to('Toronto Raptors'))


# In[56]:


nba.where('TEAM', 'Toronto Raptors')


# In[57]:


nba.where('TEAM', are.containing('Raptors'))


# In[58]:


nba.where('PLAYER', are.equal_to('Stephen Curry'))


# In[59]:


nba.where('TEAM', are.equal_to('Golden State Warriors'))


# In[60]:


nba.where('TEAM', are.equal_to('Golden State Warriors')).sort('SALARY', descending=True)


# In[61]:


nba.where('SALARY', are.between(10, 12))

