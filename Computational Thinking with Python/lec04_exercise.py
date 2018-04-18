
# coding: utf-8

# In[2]:


from datascience import *
import numpy as np

get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plots
plots.style.use('fivethirtyeight')


# ## Arithmetic

# In[3]:


2 + 3


# In[4]:


2 * 3


# In[5]:


2 ** 3


# In[6]:


2 * * 3


# In[7]:


10 * 2 ** 3


# In[8]:


2 + 3 * 4 + 5


# In[9]:


2 / 3


# In[10]:


2 / 0


# In[11]:


2 / 3000


# In[12]:


2 / 3000000


# In[13]:


0.6666666666666666 - 0.6666666666666666123456789


# In[14]:


0.000000000000000123456789


# In[ ]:


0.000000000000000000000000000000000000000000000000000000000000000000000123456789


# In[15]:


2 ** 0.5


# In[16]:


2 ** 0.5 * 2 ** 0.5


# In[17]:


2 ** 0.5 * 2 ** 0.5 - 2


# ## Growth

# In[18]:


sept_7 = 4366
aug_7 = 1830
growth_per_month = (sept_7 / aug_7) - 1
growth_per_month


# In[19]:


sept_7 * (1 + growth_per_month) ** 12


# In[20]:


fed_budget_2002 = 2370000000000
fed_budget_2012 = 3380000000000
fed_budget_2012 - fed_budget_2002


# In[21]:


g = (fed_budget_2012 / fed_budget_2002) ** (1/10) - 1
g


# In[22]:


fed_budget_2002 * (1 + g) ** 16 # Actual 2018 budget: $4.1 trillion


# ## Arrays

# In[23]:


make_array(1, 2, 3)


# In[24]:


make_array(1, 2, 3) * 2


# In[26]:


a = make_array(1, 2, 3)


# In[27]:


a + 5


# In[28]:


a + make_array(10, 100, 1000)


# In[29]:


a


# In[30]:


sum(a)


# In[31]:


max(a)


# In[32]:


min(a)


# In[33]:


fed_budget_2002 * (1 + g) ** a


# ## Columns

# In[34]:


# From http://www.boxofficemojo.com/alltime/adjusted.htm
movies = Table.read_table('top_movies_2017.csv')
movies


# In[35]:


movies.column('Gross')


# In[36]:


adjustment = movies.column('Gross (Adjusted)') / movies.column('Gross')
adjustment


# In[37]:


movies.with_column('Adjustment', adjustment)


# In[38]:


movies.with_column('Adjustment', adjustment).scatter('Year', 'Adjustment')


# In[39]:


movies.column('Year')


# In[40]:


age = 2017 - movies.column('Year')
movies = movies.with_column('Age', age)
movies


# In[41]:


movies = movies.with_column('Growth rate', adjustment ** (1 / age) - 1)
movies


# In[42]:


movies.scatter('Year', 'Growth rate')


# In[43]:


movies.sort('Age').show(20)


# In[44]:


movies.sort('Year').show(20)


# In[ ]:


# http://www.boxofficemojo.com/about/adjuster.htm

