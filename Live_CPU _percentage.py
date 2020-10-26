#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time    # for the right time interval for displaying
import psutil  # for getting the current CPU data
import matplotlib.pyplot as plt # for plotting graph


# In[2]:


# To get the visualizations in the notebook, we have to do certain configurations
get_ipython().run_line_magic('matplotlib', 'notebook')
plt.rcParams['animation.html'] = 'jshtml'


# In[3]:


fig = plt.figure()  # create a variable holding the figure configuration (using matplot lib)
ax = fig.add_subplot(111) # adding sub-plot
fig.show # for displaying the figure


# In[4]:


i = 0 # using iterator
x,y = [],[] #creating two empty list for putting values

while True: # creating an infinite loop
    x.append(i) # adding the iterated value to  list - x
    y.append(psutil.cpu_percent()) # adding the live cpu use percentage to list - y
    
    ax.plot(x,y, color='b') # plotting the graph using the sub-plot and giving it color as blue
    
    fig.canvas.draw() # instruction to draw the canvas for the variable - fig
    
    ax.set_xlim(left=max(0,i-50), right=i+50) # setting limit to the graph so that it doesnt contracts
    
    time.sleep(0.1) # interval of time before running the command to get the live cpu usage percentage
    i += 1 # iterating after every loop of instructions
    


# In[ ]:




