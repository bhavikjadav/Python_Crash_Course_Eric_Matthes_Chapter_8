#!/usr/bin/env python
# coding: utf-8

# # 8-10. Sending Messages: Start with a copy of your program from Exercise 8-9. Write a function called send_messages() that prints each text message and moves each message to a new list called sent_messages as it’s printed. After calling the function, print both of your lists to make sure the messages were moved correctly.

# In[17]:


greetings = ["good morning",
             "good afternoon",
             "good evening",
             "good night",
             "good bye"]


# In[18]:


sent_messages = []


# In[19]:


def show_messages(greetings, sent_messages):
    """This function displays the contents of list and moves the contents to another list."""
    while greetings:
        current_message = greetings.pop()
        print(f"Sending : {current_message.title()}")
        sent_messages.append(current_message)


# In[20]:


def send_messages(sent_messages):
    """This function displays as messages are send."""
    print("\nSent messages are : ")
    for sent_message in sent_messages:
        print(sent_message.title())
    


# In[21]:


show_messages(greetings, sent_messages)
send_messages(sent_messages)

