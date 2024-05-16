#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[6]:


# log(1/t) = D + 1.018 * z1 * z2 * sqrt(I)
# I = E Ci Zi**2

t = np.array([213, 140, 127, 106, 96, 86])
n = np.arange(1, 7)

I_base = 0.002 * (1 + 2**2) + 0.04 * (1 + 1) + 0.02 * (1 + 2**2)
I = (I_base + np.array([0., 0.2, 0.4, 0.6, 0.8, 1.])) / 2

sqrt_I = np.sqrt(I)

i_t = 1 / t
log_i_t = np.log10(i_t)

d = {
    'n': n,
    'I': I,
    'sqrt_I': sqrt_I,
    't': t,
    '1/t': i_t,
    'log(1/t)': log_i_t,
}

df = pd.DataFrame(d)
df.set_index('n', inplace=True)
df


# In[7]:


from scipy.stats import linregress
line = linregress(sqrt_I, log_i_t)
slope, b = line[0], line[1]
f = lambda x: slope * x + b


# In[10]:


plt.scatter(sqrt_I, log_i_t, label='Actual data', c='r')

x = np.linspace(0.3, 1., 100)
plt.plot(x, f(x), label='Regression line')
plt.xlabel('sqrt(I)')
plt.ylabel('log(1/t)')
plt.legend()
plt.show()


# In[11]:


z1z2 = slope / 1.018

print(f'slope = {slope: .4}')
print(f'z1z2 = {z1z2: .4}')


# In[ ]:




