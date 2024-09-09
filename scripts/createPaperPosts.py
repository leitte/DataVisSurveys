import os
import json
import yaml

directory = 'data/paperMetadata'

def loadPaperMetadata (filepath):
    with open(filepath, 'r') as file:
        paperMetadata = json.load(file)
        return paperMetadata

for filename in os.listdir(directory):
    filepath = os.path.join(directory, filename)

    if os.path.isfile(filepath):
        print('++',filepath)
        paperMetadata = loadPaperMetadata(filepath)
        if paperMetadata:
            print(paperMetadata['title'])

    break