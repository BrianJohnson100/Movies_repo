#!/usr/bin/env python
# coding: utf-8

# In[6]:


import requests as req
from bs4 import BeautifulSoup as bsobj
import datetime

url = "https://www.forbes.com/lists/best-large-employers/?sh=232e7a757b66"
# Date and Time Stamp
print("Start: " + str(datetime.datetime.now().strftime("%I:%m %p")))

response = req.get(url)
print(response)


# In[9]:


soup = bsobj(response.content, "html.parser")
#print(dir(response.content))
#soup


# In[10]:


#Location_for_file_export = r'C:\Users\Brian\OneDrive\Desktop\Box_Office1.csv'
# df.to_csv(Location_for_file_export)

file = open(r'C:\Users\Brian\OneDrive\Desktop\Box_Office_David.csv',"w")

#The "w" creates the file 



# In[12]:


soup_rows = soup.find_all('a',attrs={"class":"table-row"})
#soup_rows 


# In[13]:


for soup_row in soup_rows:
    file_row = []
    soup_divs = soup_row.find_all('div')
    for soup_div in soup_divs:
        file_row.append(soup_div.get_text())

    row_text = ",".join(file_row)

    file.write(row_text + "\n") 

file.close()


# In[ ]:




