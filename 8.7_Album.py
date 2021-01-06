#!/usr/bin/env python
# coding: utf-8

# # 8-7. Album: Write a function called make_album() that builds a dictionary describing a music album. The function should take in an artist name and an album title, and it should return a dictionary containing these two pieces of information. Use the function to make three dictionaries representing different albums. Print each return value to show that the dictionaries are storing the album information correctly.
# # Use None to add an optional parameter to make_album() that allows you to store the number of songs on an album. If the calling line includes a value for the number of songs, add that value to the album’s dictionary. Make at least one new function call that includes the number of songs on an album.

# In[11]:


def make_album(artist, album, songs_no=None):
    """This function returns the dictionary."""
    artist_album = {"artist": artist.title(), "album": album.title()}
    if songs_no:
        artist_album["songs_no"] = songs_no            
    return artist_album


# In[12]:


make_album("arijit", "pal", songs_no=200)


# In[13]:


make_album("kailash", "shiva")


# In[15]:


make_album("mukesh", "pankh", songs_no=100)

