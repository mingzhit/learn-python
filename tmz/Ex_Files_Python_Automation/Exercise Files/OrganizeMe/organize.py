import os
from pathlib import Path

SUBDIRECTORIES = {
    "DOCUMENTS": ['.pdf','.rtf','.txt'],
    "AUDIO": ['.m4a','.m4b','.mp3'],
    "VIDEOS": ['.mov','.avi','.mp4'],
    "IMAGES": ['.jpg','.jpeg','.png']
}
def picDirectory(value):
    for k, v in SUBDIRECTORIES.items(): #items用于遍历字典
       for v1 in v:
           if v1 == value:
               return k

q = picDirectory(".jpeg")
print(q)

