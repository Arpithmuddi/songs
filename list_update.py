#!/usr/bin/python3
import os


#get songs in directory
def get_songs_from_directory():
    list1 = []
    for i in os.listdir():
        if '.mp3' in i:
            list1.append(i)
    return list1

#get song list from file
def write_updated_list():
    fo = open("list", "w")
    for i in get_songs_from_directory():
        fo.write(i+"\n")
        print("wrote"+i)
    fo.close()

write_updated_list()