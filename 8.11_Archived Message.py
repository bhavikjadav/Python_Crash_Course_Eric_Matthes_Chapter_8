#!/usr/bin/env python
# coding: utf-8

# # 8-11. Archived Messages: Start with your work from Exercise 8-10. Call the function send_messages() with a copy of the list of messages. After calling the function, print both of your lists to show that the original list has retained its messages.

# In[1]:


greetings = ["good morning",
             "good afternoon",
             "good evening",
             "good night",
             "good bye"]


# In[2]:


sent_messages = []


# In[3]:


def show_messages(greetings, sent_messages):
    """This function displays the contents of list and moves the contents to another list."""
    while greetings:
        current_message = greetings.pop()
        print(f"Sending : {current_message.title()}")
        sent_messages.append(current_message)


# In[4]:


def send_messages(sent_messages):
    """This function displays as messages are send."""
    print("\nSent messages are : ")
    for sent_message in sent_messages:
        print(sent_message.title())


# In[5]:


show_messages(greetings, sent_messages)
send_messages(sent_messages)


# In[7]:


print(greetings)
print(sent_messages)

