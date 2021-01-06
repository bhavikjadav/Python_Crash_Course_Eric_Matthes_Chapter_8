#!/usr/bin/env python
# coding: utf-8

# # 8-9. Messages: Make a list containing a series of short text messages. Pass the list to a function called show_messages(), which prints each text message.

# In[8]:


def show_messages(greetings):
    """This function displays the contents of list."""
    for greeting in greetings:
        print(greeting.title())


# In[11]:


greetings = ["good morning", 
             "good afternoon",
             "good evening", 
             "good night",
             "good bye"]

cities = ["surat",
          "mumbai",
          "jaipur"]

show_messages(greetings)
print("---------------")
show_messages(cities)

