#!/usr/bin/env python
# coding: utf-8

# # 8-4. Large Shirts: Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.

# In[6]:


def make_shirt(text, size='l'): # We cannot define constant parameter at 0th index or first parameter.
    """This function accepts the constant value of size="large" and text which printed on the tshirt."""
    print(f"Size : {size.upper()}")
    print(f"Text : {text.title()}")


# In[7]:


make_shirt("elephant")


# In[8]:


make_shirt("zebra", "m")

