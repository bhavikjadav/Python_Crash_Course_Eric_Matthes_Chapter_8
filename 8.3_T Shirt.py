#!/usr/bin/env python
# coding: utf-8

# # 8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. The function should print a sentence summarizing the size of the shirt and the message printed on it.
# # Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments.

# In[5]:


def make_shirt(size, text):
    """This function accepts the size and text which printed on the tshirt."""
    print(f"Size : {size.upper()}")
    print(f"Text : {text.title()}")


# In[6]:


make_shirt("xxl", "lion")


# In[7]:


make_shirt(text="tiger", size="m") # This is called using fuction with keyword argument.

