#!/usr/bin/env python
# coding: utf-8

# # 8-14. Cars: Write a function that stores information about a car in a dictionary. The function should always receive a manufacturer and a model name. It should then accept an arbitrary number of keyword arguments. Call the function with the required information and two other name-value pairs, such as a color or an optional feature. Your function should work for a call like this one:
# # car = make_car('subaru', 'outback', color='blue', tow_package=True)
# # Print the dictionary that’s returned to make sure all the information was stored correctly.

# In[2]:


def cars(manufacturer, model, **car_info):
    """Returns the details of car."""
    car_info["Manufacturer"] = manufacturer.title()
    car_info["Model"] = model.title()
    return car_info


# In[7]:


car1 = cars("subaru", "outback", color="black", tow_package=True)
print(car1)

