#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json
from pprint import pprint


# In[120]:


sa3_code = [20601, 20602, 20603, 20604, 20605, 20606, 20607, 20701, 20702, 20703, 20801, 20902, 20903, 20904,
           21001, 21002, 20803, 20804, 20901, 21003, 21004, 21005, 20802, 21101, 21102, 21103, 21104, 21105,
           21201, 21202, 21203, 21204, 21205, 21301, 21302, 21303, 21304, 21305, 21401, 21402]


# In[4]:


mel_zone = {"Mel": LGA_code}


# In[33]:


attr_dict = {}
with open("metadata.json") as file:
    meta_data = json.load(file)
    for detail in meta_data['selectedAttributes'][1:3]:
        attr_dict[detail['name']] = {'title': detail['title']}
with open('new_meta.json', 'w') as output:
    json.dump(attr_dict, output)


# In[108]:


#pprint(attr_dict)


# In[109]:


#pprint(meta_data['selectedAttributes'][1:3])


# In[188]:


data = {}
with open("language.json") as file:
    language_data = json.load(file)
            
    
    for info in language_data['features']:
        sa3 = info['properties']['sa3_code16']
        eng_count = info['properties']['lang_spoken_home_eng_only_p']
        oth_count  = info['properties']['lang_spoken_home_oth_lang_p']
        
        data[sa3] = {'eng_only': eng_count, 'oth_lang': oth_count}
        
with open('new_language.json', 'w') as outfile:
        json.dump(data, outfile)
           


# In[187]:


data


# In[79]:


#pprint(language_data['features'])

