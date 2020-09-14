#!/usr/bin/env python
# coding: utf-8

# In[57]:


import pandas as pd
from sqlalchemy import create_engine


# In[58]:


engine = create_engine('postgresql://postgres:root@localhost:5432/doublebagger')


# In[59]:


posts = pd.read_sql('select * from post_post', engine)


# In[60]:


companies = pd.read_sql('select * from post_company' , engine)


# In[61]:


posts_companies = pd.merge(companies, posts, left_on ='id' ,right_on ='company_id')


# In[62]:


posts_companies


# In[ ]:





# In[ ]:




