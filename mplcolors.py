#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.cm as cm
    


# In[15]:


class multicolor_plotter():
    '''df = dataframe with your information, x_df_pos = column position of your x variables, x_label = x axis label, 
    y_df_pos = column position of your y variables, y_label = y axis label, label_df_pos = the label you want associated with each data point, 
    title = title of chart, chunk = corresponds to how many of the same variable you have & want plotted'''
    
    #imports
    import numpy as np
    import pandas as pd
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    import matplotlib.cm as cm
    
    def __init__(self, df, x_df_pos, x_label, y_df_pos, y_label, label_df_pos, title, chunk):
        self.df = df
        self.x_df_pos = x_df_pos
        self.x_label = x_label
        self.y_df_pos = y_df_pos
        self.y_label = y_label
        self.label_df_pos = label_df_pos
        self.title = title
        self.chunk = chunk
        
    def plotter(self):
        
        def delist(args):
            'Taking mutliple lists within a list and returning a single list of values'
            delist = [var for small_list in args for var in small_list]
            return(delist)
        
        assay_num = [var for var in range(len(self.df.iloc[:,self.x_df_pos]))]
        
        offset_x = 0
        offset_y = 0
        offset_label = 0
        
        xf = []
        yf = []
        labelf = []
        
        while offset_x < len(assay_num):
            i_x = assay_num[offset_x:offset_x+self.chunk]
            x = self.df.iloc[i_x, self.x_df_pos]
            xf.append(x)
            
            offset_x += self.chunk
        
        while offset_y < len(assay_num):
            i_y = assay_num[offset_y:offset_y+self.chunk]
            y = self.df.iloc[i_y, self.y_df_pos]
            yf.append(y)
            
            offset_y += self.chunk
            
        while offset_label < len(assay_num):
            i_label = assay_num[offset_label:offset_label+self.chunk]
            label = self.df.iloc[i_label, self.label_df_pos]
            labelf.append(label)
            
            offset_label += self.chunk
        
        label_unique = []
        for var in labelf:
            labelu = var.unique()
            label_list = labelu.tolist()
            label_unique.append(label_list)
        
        labeld = delist(label_unique)
        
        colors = cm.rainbow(np.linspace(0,1, (len(labeld))))
        
        xylc_zip = zip(xf,yf, labeld, colors)
        
        fig, ax = plt.subplots()
        for x, y, l, c in xylc_zip:
            plt.scatter(x,y, color = c, label = l)
            ax.grid()
            ax.legend()
            ax.set(xlabel = self.x_label, ylabel = self.y_label, title = self.title)
            plt.legend(bbox_to_anchor =(1.1, 1.05))
            
 


# In[28]:


#example of use
df_dict = {'Name':['a','a','a','a','b','b','b','b','c','c','c','c','d','d','d','d','e','e','e','e','f','f','f','f'], 
                   'X': [var for var in range(24)],
                   'Y': [var for var in range(24)]}
df = pd.DataFrame(df_dict)
display(df)
test = multicolor_plotter(df,1,'x',2,'y',0,'Testing',4)
test.plotter()


# In[ ]:




