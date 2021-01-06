#!/usr/bin/env python
# coding: utf-8

# # 8-12. Sandwiches: Write a function that accepts a list of items a person wants on a sandwich. The function should have one parameter that collects as many items as the function call provides, and it should print a summary of the sandwich that’s being ordered. Call the function three times, using a different number of arguments each time.

# In[4]:


def make_sandwiches(*items):
    """This function accepts the N numbers of items."""
    print(items)


# In[6]:


make_sandwiches("cheese")
make_sandwiches("pepproni", "diet")
make_sandwiches("cheese", "masala", "butter")

