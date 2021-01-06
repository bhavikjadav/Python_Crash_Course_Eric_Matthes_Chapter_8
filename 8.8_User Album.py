#!/usr/bin/env python
# coding: utf-8

# # 8-8. User Albums: Start with your program from Exercise 8-7. Write a while loop that allows users to enter an album’s artist and title. Once you have that information, call make_album() with the user’s input and print the dictionary that’s created. Be sure to include a quit value in the while loop.

# In[1]:


def make_album(artist, album, songs_no=None):
    """This function returns the dictionary."""
    artist_album = {"artist": artist.title(), "album": album.title()}
    if songs_no:
        artist_album["songs_no"] = songs_no            
    return artist_album


# In[4]:


while True:
    artist1 = input("Enter the name of an artist : ")
    if artist1 == "quit":
        break
    album1 = input("Enter the name of an album : ")
    if album1 == "quit":
        break
    full_details = make_album(artist1, album1)
    print(f"{full_details}")
    

