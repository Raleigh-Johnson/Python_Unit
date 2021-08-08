import os

directory = r'/Users/jeffwiley/Documents/GitHub/Python-Unit/Python_Unit'
for filename in os.listdir(directory):
    if filename.endswith("txt"):
        print(os.path.join(directory, filename))
    else:
        continue


