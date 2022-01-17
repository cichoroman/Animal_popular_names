#!/usr/bin/env python
# coding: utf-8

# In[1]:


#webscraping ze stronki wamiz.pl i robienie jsona ze zescrapowanych danych
#wordmapa z customowym kształtem - inny plik
#nadzorowane maszynowe - inny plik


# In[2]:


import requests


# In[3]:


from bs4 import BeautifulSoup


# In[4]:


stronaPsy=requests.get("https://wamiz.pl/pies/imiona/samiec")


# In[5]:


stronaPsy.text


# In[6]:


tagiPsy=BeautifulSoup(stronaPsy.text, 'html.parser')


# In[7]:


tagiPsy


# In[8]:


imionaPsy=tagiPsy.findAll('p', attrs={'class':'names-table-content'})


# In[9]:


imionaPsy


# In[10]:


listaPsy=[]


# In[11]:


for n in imionaPsy:
    listaPsy.append(n.text.strip("\n                                 "))


# In[12]:


#test
#listaPsy[1]


# In[13]:


print(*listaPsy)


# In[14]:


stronaSuczki=requests.get("https://wamiz.pl/pies/imiona/suka")


# In[15]:


stronaSuczki.text


# In[16]:


tagiSuczki=BeautifulSoup(stronaSuczki.text, 'html.parser')


# In[17]:


tagiSuczki


# In[18]:


imionaSuczki=tagiSuczki.findAll('p', attrs={'class':'names-table-content'})


# In[19]:


listaSuczki=[]


# In[20]:


for n in imionaSuczki:
    listaSuczki.append(n.text.strip("\n                                 "))


# In[21]:


#test
#listaSuczki[1]


# In[22]:


print(*listaSuczki)


# In[23]:


stronaKotki=requests.get("https://wamiz.pl/kot/imie/kotka")


# In[24]:


stronaKotki.text


# In[25]:


tagiKotki=BeautifulSoup(stronaKotki.text, 'html.parser')


# In[26]:


tagiKotki


# In[27]:


imionaKotki=tagiKotki.findAll('p', attrs={'class':'names-table-content'})


# In[28]:


listaKotki=[]


# In[29]:


for n in imionaKotki:
    listaKotki.append(n.text.strip("\n                                 "))


# In[30]:


#test
#listaKotki[1]


# In[31]:


stronaKoty=requests.get("https://wamiz.pl/kot/imie/samiec")


# In[32]:


stronaKoty.text


# In[33]:


tagiKoty=BeautifulSoup(stronaKoty.text, 'html.parser')


# In[34]:


tagiKoty


# In[35]:


imionaKoty=tagiKoty.findAll('p', attrs={'class':'names-table-content'})


# In[36]:


listaKoty=[]


# In[37]:


for n in imionaKoty:
    listaKoty.append(n.text.strip("\n                                 "))


# In[38]:


#test
#listaKoty[1]


# In[39]:


#Jsony


# In[40]:


imionaJson =""
kotyString = ""
kotkiString = ""
psyString = ""
suczkiString = ""


# In[41]:


for i in listaKoty:
    kotyString += ' {\"imie\" : \"'+ i +  '\"'    + ',\"typ\": \"kot\"' + '},' 

kotyString = kotyString[:-1]


# In[42]:


for i in listaKotki:
     kotkiString += ' {\"imie\" : \"'+ i +  '\"'    + ',\"typ\": \"kotki\"' + '},' 
kotkiString = kotkiString[:-1]


# In[43]:


for i in listaSuczki:
    suczkiString += ' {\"imie\" : \"'+ i +  '\"'    + ',\"typ\": \"suczka\"' + '},'

suczkiString = suczkiString[:-1]


# In[ ]:





# In[44]:


for i in listaPsy:
    psyString += ' {\"imie\" : \"'+ i +  '\"'    + ',\"typ\": \"pies\"' + '},'

psyString = psyString[:-1]


# In[45]:


#test
#psyString


# In[46]:


#test
#kotyString


# In[47]:


#test
#kotkiString


# In[48]:


#test
#suczkiString


# In[ ]:





# In[49]:


imionaJson += '{ \"imiona\": [' + psyString + ',' + kotyString + ',' + suczkiString +','+ kotkiString + ']}'


# In[50]:


imionaJson


# In[51]:


import json



# In[52]:


def zapiszJson(dane, nazwaPliku):
    x=json.loads(dane)
    with open(nazwaPliku+'.json', 'w', encoding='utf-8') as f:
        json.dump(x, f, ensure_ascii=False, indent=4)
    print('zapisano plik ' + nazwaPliku +'.json')
    


# In[55]:


zapiszJson(imionaJson,'imiona')





