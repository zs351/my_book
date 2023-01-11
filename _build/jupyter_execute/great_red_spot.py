#!/usr/bin/env python
# coding: utf-8

# # The Great Red Spot
# 
# Jupiter’s iconic Great Red Spot (GRS) is actually an enormous storm that is bigger than Earth that has raged for hundreds of years! {numref}`great-red-spot` below shows an image of Jupiter captured by the Hubble Space Telescope on June 27, 2019.
# 
# ```{figure} https://solarsystem.nasa.gov/system/resources/detail_files/626_PIA21775.jpg
# ---
# height: 300px
# name: great-red-spot
# ---
# Jupiter's Great Red Spot! Source: [NASA](https://solarsystem.nasa.gov/resources/626/jupiters-great-red-spot-in-true-color/?category=planets_jupiter).
# ```
# 
# Jupiter's GRS has been observed to be shrinking for about the last century and a half! [Here](https://github.com/UBC-DSCI/jupyterdays/tree/master/jupyterdays/sessions/beuzen/data) is some data of the length of the GRS spanning the last ~150 years which we can use to investigate this phenomenon.

# In[1]:


get_ipython().run_cell_magic('latex', '', '\n\\begin{equation}\nx^2+y^2=z^2\n\\end{equation}\n\n\\begin{align}\n\\int_a^b (x+3)^5 \\; \\text{d}x &= \\left(\\theta^2 + \\rho\\mu\\alpha^c\\right)\\\\\nx^2 + y^2 &= z^2\n\\end{align}')


# In[2]:


get_ipython().run_cell_magic('latex', '', '\\begin{align}\n\\nabla \\times \\vec{\\mathbf{B}} -\\, \\frac1c\\, \\frac{\\partial\\vec{\\mathbf{E}}}{\\partial t} & = \\frac{4\\pi}{c}\\vec{\\mathbf{j}} \\\\\n\\nabla \\cdot \\vec{\\mathbf{E}} & = 4 \\pi \\rho \\\\\n\\nabla \\times \\vec{\\mathbf{E}}\\, +\\, \\frac1c\\, \\frac{\\partial\\vec{\\mathbf{B}}}{\\partial t} & = \\vec{\\mathbf{0}} \\\\\n\\nabla \\cdot \\vec{\\mathbf{B}} & = 0\n\\end{align}')


# In[3]:


import pandas as pd
pd.options.plotting.backend = "plotly"

url = "https://raw.githubusercontent.com/UBC-DSCI/jupyterdays/master/jupyterdays/sessions/beuzen/data/GRS_data.csv"
df = pd.read_csv(url)
df['Year'] = df['Year'].astype(int) 
df.head()


# In[4]:


import plotly.io as pio
pio.renderers.default = "notebook"
fig = df.plot.scatter(x="Year", y="GRS Length", color="Recorder",
                      range_x=[1870, 2030], range_y=[10, 40],
                      width=650, height=400)
fig.update_layout(title={'text': "Great Red Spot Size", 'x':0.5, 'y':0.92})
fig.update_traces(marker=dict(size=7))


# In[5]:


fig = df.plot.scatter(x="Year", y="GRS Length",
                      animation_frame="Year",
                      range_x=[1870, 2030], range_y=[10, 40],
                      width=600, height=520)
fig.update_layout(title={'text': "Great Red Spot Size Animation", 'x':0.5, 'y':0.94})
fig.layout.updatemenus[0].buttons[0].args[1]["frame"]["duration"] = 200
fig.update_traces(marker=dict(size=10))


# In[ ]:




