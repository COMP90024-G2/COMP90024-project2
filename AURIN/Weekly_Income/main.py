#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json
from pprint import pprint


# In[2]:


sa3_code = [20601, 20602, 20603, 20604, 20605, 20607, 20701, 20702, 20606, 20703, 20801, 20902, 20903, 20904,
           21001, 21002, 20802, 20803, 20804, 20901, 21003, 21004, 21005, 21101, 21102, 21103, 21104, 21105,
           21201, 21202, 21203, 21204, 21205, 21301, 21302, 21303, 21304, 21305, 21401, 21402]


# In[9]:


attr_dict = {}
with open("metadata.json") as file:
    meta_data = json.load(file)
    for detail in meta_data['selectedAttributes'][1:8]:
        attr_dict[detail['name']] = {'title': detail['title']}
with open('new_meta.json', 'w') as output:
    json.dump(attr_dict, output)


# In[10]:


#pprint(meta_data['selectedAttributes'][1:8])


# In[21]:


weekly_income = {}
with open("income.json") as file:
    income_data = json.load(file)

    for info in income_data['features']:
        sa3 = info['properties']['sa3_code16']
        weekly_1_149_count = info['properties']['p_1_149_tot']
        weekly_150_299_count = info['properties']['p_150_299_tot']
        weekly_300_399_count = info['properties']['p_300_399_tot']
        weekly_400_499_count = info['properties']['p_400_499_tot']
        weekly_400_499_count = info['properties']['p_400_499_tot']
        weekly_500_649_count = info['properties']['p_500_649_tot']
        weekly_650_799_count = info['properties']['p_650_799_tot']
        weekly_800_899_count = info['properties']['p_800_999_tot']
        weekly_income[sa3] = {'weekly 1-149': weekly_1_149_count, 'weekly 150-299': weekly_150_299_count, 'weekly 300-399': weekly_300_399_count,
                             'weekly 400-499': weekly_400_499_count, 'weekly 500-649': weekly_500_649_count, 'weekly 650-799': weekly_650_799_count,
                             'weekly 800-899': weekly_800_899_count}
        
with open('new_income.json', 'w') as outfile:
    json.dump(weekly_income, outfile)
           


# In[22]:


#weekly_income

