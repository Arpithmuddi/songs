import os

for i in [i for i in os.listdir() if '.mp3' in i]:
    print(i)

    