#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests
 
from os import path, getcwd
from PIL import Image
from wordcloud import WordCloud, ImageColorGenerator


# In[2]:



# r=requests.get("https://zoodoptuj.pl/zwierzeta-do-adopcji?pet_town=&pet_type=1")

# from bs4 import BeautifulSoup
# soup = BeautifulSoup(r.text, 'html.parser')

# import re
# def visible(element):
#     if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
#         return False
#     elif re.match('<!--.*-->', str(element.encode('utf-8'))):
#         return False
#     return True

# page_text_list = []
# for t in filter(visible, soup.findAll(text=True)):
#     page_text_list.append(t)

# page_text = "".join(page_text_list)
# page_text[:80]

# page_words = page_text.split()
# import string
# page_words2 = [w.strip(string.punctuation).lower() for w in page_words if
# len(w.strip(string.punctuation))>0]


# In[3]:



# from collections import Counter
# page_word_freq = Counter(page_words2).most_common()
# print(len(page_word_freq),page_word_freq[:10])


# In[4]:



# Unexpected_WORDS=['i','do','na','a','w','z','do','nie','się','jest','są',"płeć", "wiek", "wielkość", "div",'de','km','o','bez','end','and','style="max-width','main','»','target="_blank','rel="nofollow',]


# In[5]:



# %pylab inline
# from os import path
# import matplotlib.pyplot as plt
# from wordcloud import WordCloud

# word_freq_no_stop = [w for w in page_word_freq if w[0] not in Unexpected_WORDS and not w[0].isdigit()]




# In[6]:



# word_freq_no_stop 


# In[7]:



# dict_page_word_freq = {}
# for i in word_freq_no_stop:
#     dict_page_word_freq[i[0]]=i[1]


# In[8]:



# dict_page_word_freq 


# In[9]:



# mask = np.array(Image.open('łapki.png'))
# wordcloud = WordCloud(max_words=100, mask=mask,background_color="white").fit_words(dict_page_word_freq)
# plt.imshow(wordcloud)
# plt.axis("off")


# In[10]:



def czestotliwoscSlowStrony(strona):
    r=requests.get(strona)
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(r.text, 'html.parser')

    import re
    def visible(element):
        if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
            return False
        elif re.match('<!--.*-->', str(element.encode('utf-8'))):
            return False
        return True

    page_text_list = []
    for t in filter(visible, soup.findAll(text=True)):
        page_text_list.append(t)

    page_text = "".join(page_text_list)
    page_text[:80]

    page_words = page_text.split()
    import string
    page_words_without_punctuation = [w.strip(string.punctuation).lower() for w in page_words if
    len(w.strip(string.punctuation))>0]
    from collections import Counter
    page_word_freq = Counter(page_words_without_punctuation).most_common()
    print(len(page_word_freq),page_word_freq[:10])
    return page_word_freq


# In[11]:


Unexpected_WORDS = ['i','do','na','a','w','z','do','nie','dla','się','jest','są','już','to','czy','lub', "które",'może','hasło', 'zaloguj', 'się', 'koniec', 'rejestracja',"płeć", "wiek", "wielkość", "div",'de','km','o','bez','end','and','global', 'site', 'tag', 'gtag.js', 'google', 'analytics', 'facebook','style="max-width','main','»','target="_blank','rel="nofollow',]


# In[12]:


def chmurka(page_word_freq, kontur):



    get_ipython().run_line_magic('pylab', 'inline')
    from os import path
    import matplotlib.pyplot as plt
    from wordcloud import WordCloud

    word_freq_no_stop = [w for w in page_word_freq if w[0] not in Unexpected_WORDS and not w[0].isdigit()]
    dict_page_word_freq = {}
    for i in word_freq_no_stop:
        dict_page_word_freq[i[0]]=i[1]

    mask = np.array(Image.open(kontur))
    wordcloud = WordCloud(max_words=100, mask=mask,background_color="white").fit_words(dict_page_word_freq)
    plt.imshow(wordcloud)
    plt.axis("off")


# In[ ]:





# In[13]:


freq_zoodoptuj = czestotliwoscSlowStrony("https://zoodoptuj.pl/zwierzeta-do-adopcji?pet_town=&pet_type=1")


# In[14]:


chmurka(freq_zoodoptuj, 'łapki.png')


# In[24]:


freq_psy = czestotliwoscSlowStrony('https://www.psy.pl/')


# In[25]:


chmurka(freq_psy, 'piesek.png')


# In[26]:


freq_koty = czestotliwoscSlowStrony('https://www.koty.pl/')


# In[27]:


chmurka(freq_koty, 'kotek.png')


# In[ ]:





# In[ ]:





# In[ ]:




