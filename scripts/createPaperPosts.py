import os

directory = 'data/paperMetadata'

for filename in os.listdir(directory):
    filepath = os.path.join(directory, filename)

    if os.path.isfile(filepath):
        print(filepath)