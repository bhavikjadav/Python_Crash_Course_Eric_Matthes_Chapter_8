#!/usr/bin/env python
# coding: utf-8

# # 8-5. Cities: Write a function called describe_city() that accepts the name of a city and its country. The function should print a simple sentence, such as Reykjavik is in Iceland. Give the parameter for the country a default value. 
# # Call your function for three different cities, at least one of which is not in the default country.

# In[5]:


def describe_city(country, city="surat"):
    """This function accepts two parameter and displays the neatly formatted sentance."""
    print(f"{city.title()} is in {country.title()}.")


# In[6]:


describe_city("bharat")


# In[7]:


describe_city("iceland", "rejkjavik")


# In[8]:


describe_city("united states", "atlanta")

