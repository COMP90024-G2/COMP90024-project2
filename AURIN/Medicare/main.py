#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json
from pprint import pprint


# In[8]:


attr_dict = {}
with open("metadata.json") as file:
    meta_data = json.load(file)
    for detail in meta_data['selectedAttributes'][1:5]:
        attr_dict[detail['name']] = {'title': detail['title'].replace("All Patients -", "")
                                     .replace(" (%)", "")
                                    .replace(" ($)", "")}
with open('new_meta.json', 'w') as output:
    json.dump(attr_dict, output)


# In[9]:


#pprint(meta_data['selectedAttributes'][1:5])


# In[12]:


pprint(medicare_data)


# In[26]:


medicare = {}
with open("medicare.json") as file:
    medicare_data = json.load(file)

    for info in medicare_data['features']:
        sa3 = info['properties']['sa3_code']
        avg_benefits = info['properties']['all_patients_avg_medicare_bfts_expenditure_patient']
        avg_cost = info['properties']['all_patients_avg_oop_cst_patient']
        avg_service_count = info['properties']['all_patients_avg_no_patient']
        perc_pat_cost = info['properties']['perc_patients_csts']
        
        medicare[sa3] = {'avg_benefits': avg_benefits, 'avg_cost': avg_cost,
                         'avg_service_count': avg_service_count, 'perc_patients_cost': perc_pat_cost}        
        
with open('new_medicare.json', 'w') as outfile:
    json.dump(medicare, outfile)


# In[25]:


#medicare

