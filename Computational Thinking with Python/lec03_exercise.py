
# coding: utf-8

# In[1]:


from datascience import *
import numpy as np

get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plots
plots.style.use('fivethirtyeight')


# ## Python

# In[2]:


3 * 4


# In[3]:


12 + 3


# <br><br><br><br>

# ## Names

# In[4]:


24 * 7


# In[5]:


hours_per_week = 24 * 7


# In[6]:


hours_per_week


# In[7]:


hours_per_week * 60


# Calculate the number of seconds in a year.

# In[8]:


60 * 60 * 24 * 365


# In[9]:


seconds_per_year = 60 * 60 * 24 * 365


# In[10]:


seconds_per_year


# In[11]:


seconds_per_hour = 60 * 60
hours_per_year = 24 * 365
seconds_per_year = seconds_per_hour * hours_per_year
seconds_per_year


# <br><br><br><br>

# ## Functions

# In[12]:


abs(-5)


# In[13]:


abs(3-8)


# In[14]:


max(3, 4)


# In[15]:


y = max(3, 4)


# In[16]:


y


# <br><br><br><br>

# ## Tables

# In[17]:


Table.read_table('flowers.csv')


# In[18]:


flowers = Table.read_table('flowers.csv')


# In[19]:


flowers


# <br><br><br><br>

# ## Table operations: selecting columns

# In[20]:


flowers.select('Petals')


# In[21]:


flowers


# In[22]:


petals = flowers.select('Petals')


# In[23]:


petals


# In[24]:


flowers.select('Petals', 'Name')


# In[25]:


flowers.drop('Color')


# In[26]:


flowers


# ## Table operations: Sorting

# In[27]:


movies = Table.read_table('top_movies_by_title.csv')


# In[28]:


movies


# In[29]:


movies.show(3)


# In[30]:


movies.sort('Gross')


# In[31]:


movies.sort('Gross', descending=True)


# In[32]:


sorted_by_gross = movies.sort('Gross', descending=True)


# In[33]:


sorted_by_gross.sort('Studio')


# In[34]:


sorted_by_gross.sort('Studio', distinct=True)


# ## Visualization

# In[35]:


top_per_studio = sorted_by_gross.sort('Studio', distinct=True)


# In[36]:


top_per_studio.barh('Studio', 'Gross')


# In[37]:


top_studios = top_per_studio.sort('Gross', descending=True)
top_studios.barh('Studio', 'Gross')


# In[38]:


just_revenues = top_studios.select('Studio', 'Gross', 'Gross (Adjusted)')


# In[39]:


just_revenues


# In[40]:


just_revenues.barh('Studio')


# In[41]:


sorted_by_year = top_studios.sort('Year')
revenues_by_year = sorted_by_year.select('Studio', 'Gross', 'Gross (Adjusted)')
revenues_by_year.barh('Studio')


# In[42]:


sorted_by_year


# ## Table operations: where

# In[43]:


# This table can be found online: https://www.statcrunch.com/app/index.php?dataid=1843341
nba = Table.read_table('nba_salaries.csv')


# In[44]:


nba


# In[45]:


nba.sort('2015-2016 SALARY')


# In[46]:


nba.where('2015-2016 SALARY', are.above(10))


# In[47]:


nba.where('2015-2016 SALARY', are.above(10)).sort('2015-2016 SALARY')


# In[48]:


nba.where('PLAYER', are.equal_to('Stephen Curry'))


# In[49]:


nba.where('TEAM', are.equal_to('Golden State Warriors'))


# In[50]:


nba.where('TEAM', are.equal_to('Golden State Warriors')).sort('2015-2016 SALARY', descending=True)


# In[51]:


nba.where('2015-2016 SALARY', are.between(10, 12))

