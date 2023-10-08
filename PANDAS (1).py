#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

# Sample data
data = {'ship_mode': ["Same Day", "First Class", "Standard Class", "Second Class"],
        'sales': [100, 200, 150, 120],
        'profit': [60, 80, 70, 50]}

df = pd.DataFrame(data)

# Function to calculate surcharge
def calculate_surcharge(ship_mode):
    if ship_mode == "Same Day":
        return 0.2
    elif ship_mode == "First Class":
        return 0.1
    elif ship_mode == "Standard Class":
        return 0.05
    else:
        return 0

# Create a new column 'surcharge'
df['surcharge'] = df['ship_mode'].apply(calculate_surcharge)

# Create a new column 'total_cost'
df['total_cost'] = (df['sales'] - df['profit']) * (1 + df['surcharge'])

print(df)


# In[ ]:




