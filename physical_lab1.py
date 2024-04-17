#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[19]:


w1 = 8037
w2 = 4969
w3 = 5200
w4 = 4599
w5 = 4641
w6 = 4349

dh1 = w1
dh2 = dh1 + w2
dh3 = dh2 + w3
dh4 = dh3 + w4
dh5 = dh4 + w5
dh6 = dh5 + w6

w = np.array([w1, w2, w3, w4, w5, w6])
dh = np.array([-dh1, -dh2, -dh3, -dh4, -dh5, -dh6])
dh


# In[20]:


M_h2o = 18.01528
M_kno3 = 101.1032
step = 15/ M_kno3

n_solvent = 900 / M_h2o

n_kno3 = np.arange(step, 1, step)
n = np.array(n_kno3 + n_solvent)
x = np.array(n_kno3 / n)

dhmix = np.array(dh / n)
dhmix2 = np.array(dh / n_kno3)


# In[23]:


d = {
    'W' : w,
    'n' : n,
    'x_kno3' : x,
    'Delta_H' : dh,
    'dh/n' : dhmix
}

ld = pd.DataFrame(d)
ld


# In[30]:


plt.plot(x, dhmix)
plt.xlim(0, 0.02)
plt.ylim(-700, 0)
plt.show()


# In[ ]:




