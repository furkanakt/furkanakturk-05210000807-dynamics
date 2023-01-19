#!/usr/bin/env python
# coding: utf-8

# In[8]:


import math


# In[9]:


l1 = 0.07 # as m
l2 = l1 + 0.1 # as m
w = 807 # as rad/s


# In[10]:


degree = []
location_b = []
location_c = []
speed_b = []
speed_c = []
acceleration_b = []
acceleration_c = []

for theta in range(0, 360+1):
    
    loc_b = l1 * (math.cos(theta) + math.sin(theta))
    loc_c = l2 - ((l1*l1)/4*l2) + l1*(math.cos(theta) + l1/(4*l2)*math.cos(2*theta))
    
    sp_b = w * (l1 * (math.cos(theta) - math.sin(theta)))
    sp_c = -l1 * w * (math.sin(theta) + (l1/(2*l2)*math.sin(theta)))
    
    acc_b = l1 * w*w * (math.cos(theta) - (math.sin(theta)))
    acc_c = -l1 * w*w * (math.cos(theta) + ((l1 / l2)*math.cos(theta)))
    
    degree.append(theta)
    
    location_b.append(loc_b)
    location_c.append(loc_c)
    
    speed_b.append(sp_b)
    speed_c.append(sp_c)
    
    acceleration_b.append(acc_b)
    acceleration_c.append(acc_c)


# In[11]:


import pandas as pd


# In[12]:


data = {'Degree':degree, 
        'Location_B':location_b, 'Speed_B':speed_b, 'Acceleration_B':acceleration_b,
        'Location_C':location_c, 'Speed_C':speed_c, 'Acceleration_C':acceleration_c}

df = pd.DataFrame(data=data)
df.head()


# In[13]:


import plotly.graph_objects as go
fig = go.Figure()
fig.add_trace(go.Scatter(x=df['Degree'].iloc[0:],y=df['Location_B'].iloc[0:],mode='lines',line_color='red'))
fig.update_layout(title='Location_B')

fig.show()
fig = go.Figure()
fig.add_trace(go.Scatter(x=df['Degree'].iloc[0:],y=df['Speed_B'].iloc[0:],mode='lines',line_color='blue'))
fig.update_layout(title='Speed_B')

fig.show()
fig = go.Figure()
fig.add_trace(go.Scatter(x=df['Degree'].iloc[0:],y=df['Acceleration_B'].iloc[0:],mode='lines',line_color='green'))
fig.update_layout(title='Acceleration_B')

fig.show()


# In[14]:


fig = go.Figure()
fig.add_trace(go.Scatter(x=df['Degree'].iloc[0:],y=df['Location_C'].iloc[0:],mode='lines',line_color='red'))
fig.update_layout(title='Location_C')

fig.show()
fig = go.Figure()
fig.add_trace(go.Scatter(x=df['Degree'].iloc[0:],y=df['Speed_C'].iloc[0:],mode='lines',line_color='blue'))
fig.update_layout(title='Speed_C')

fig.show()
fig = go.Figure()
fig.add_trace(go.Scatter(x=df['Degree'].iloc[0:],y=df['Acceleration_C'].iloc[0:],mode='lines',line_color='green'))
fig.update_layout(title='Acceleration_C')

fig.show()


# In[ ]:





# In[ ]:





# In[ ]:




