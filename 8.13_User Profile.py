#!/usr/bin/env python
# coding: utf-8

# # 8-13. User Profile: Start with a copy of user_profile.py from page 149. Build a profile of yourself by calling build_profile(), using your first and last names and three other key-value pairs that describe you.

# In[1]:


"""

Content of Page No.149.

def build_profile(first, last, **user_info):
    # Build a dictionary containing everything we know about a user.
        user_info['first_name'] = first
        user_info['last_name'] = last
        return user_info
        
user_profile = build_profile('albert', 'einstein',
                            location='princeton',
                            field='physics')
                            
print(user_profile)
"""


# In[3]:


def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info


# In[4]:


user_profile = build_profile("bhavik", "jadav", age=19, field="ML")


# In[5]:


print(user_profile)

