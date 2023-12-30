#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


v_koh = np.arange(0, 8.5, 0.5)
pH1 = np.array([6.843,8.456,8.873,9.068,9.234,9.349,9.466,9.567,9.640,9.744,9.827,9.915,10,10.087,10.169,10.263,10.367])

d = {
    'V KOH': v_koh,
    'pH': pH1,
}
d = pd.DataFrame(d)
print(d)


# In[3]:


H = np.power(10, -pH1)
K = (v_koh * 0.5) / (200 + v_koh)
OH = (pow(10, -14) / H)
A = K
At = (10 * 0.4) / (200 + v_koh)  
HA = At - A
HA2 = At - (K + H - OH)


pka = pH1 + np.log10(HA/(K + H - OH))
ka = pow(10, -pka)

data1 = {
    'V KOH': v_koh,
    'pH': pH1,
    '[H]': H,
    '[K]': K,
    '[OH]': OH,
    '[A]': A,
    '[HA]': HA,
    'pKa': pka,
    'Ka': ka,
}

data1 = pd.DataFrame(data1)
print(data1)


# In[4]:


# print(np.log10(HA/A))


# In[5]:


print(ka[4:13])
Ka = np.mean(ka[4:13])
# print(Ka)
# print(-np.log10(Ka))


# In[6]:


plt.plot(v_koh, pH1)
plt.title('Titration plot of Glycinate')
plt.xlabel('Volume of KOH')
plt.ylabel('pH')
plt.show()


# In[7]:


v = np.arange(0, 10.2, 0.2)
pH2 = np.array([2.327,2.343,2.384,2.395,2.413,2.430,2.450,2.463,2.480,2.501,2.558,
               2.578,2.593,2.602,2.612,2.621,2.631,2.641,2.649,2.658,2.668,
              2.677,2.686,2.697,2.712,2.721,2.729,2.738,2.746,2.753,2.762,
              2.770,2.778,2.786,2.791,2.800,2.806,2.814,2.821,2.828,2.834,
              2.841,2.848,2.858,2.868,2.878,2.884,2.890,2.896,2.903,2.908])

d2 = {
    'V_Gly': v,
    'pH': pH2,
}

d2 = pd.DataFrame(d2)
print(d2)


# In[8]:


H = np.power(10, -pH2)
OH = (pow(10, -14) / H)
CH = (10 * 0.1) / (200 + v)
A = (Ka * (CH + OH - H)) / H
Mt = 1 / (200 + v)

At = (v * 0.4) / (200 + v)

n = (At - ((1 + Ka/H) * (CH + OH - H))) / Mt
# n


# In[9]:


data2 = {
    'V Gly': v,
    'pH': pH2,
    '[H]': H,
    '[OH]': OH,
    '[A]': A,
    '[CH]': CH,
    '[Mtot]': Mt,
    'n': n,
}

data2 = pd.DataFrame(data2)
print(data2)


# In[10]:


plt.plot(np.log10(A), n)
plt.xlabel('log([A])')
plt.ylabel('n')
plt.grid()
plt.show()


# In[11]:


# np.log10(A)

