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
            data = {
                'title': paperMetadata['title']
            }
            with open('posts/mypost.yaml', 'w') as file:
                yaml.dump(data, file)

    break