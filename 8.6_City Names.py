#!/usr/bin/env python
# coding: utf-8

# # 8-6. City Names: Write a function called city_country() that takes in the name of a city and its country. The function should return a string formatted like this: "Santiago, Chile"
# # Call your function with at least three city-country pairs, and print the values that are returned.

# In[22]:


def city_country(city, country):
    """Function that returns the formatted arguments of parameters."""
    return f"{city.title()}, {country.title()}"


# In[23]:


city_country("atlanta", "united states")


# In[24]:


city_country("surat", "bharat")


# In[25]:


city_country("bharuch", "bharat")

