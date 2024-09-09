import os
import yaml
import json

directory = 'data/paperMetadata'
filepath_paperCategories = 'data/paperClassification/paperCategories.yaml'

keywords_to_classes = {
    'taxonomy': ['taxonomy'],
    'survey': ['survey'],
    'review': ['review'],
    'text and documents': ['text', 'literature']
}

def loadPaperCategories (filepath):
    with open(filepath, 'r') as file:
        tags = yaml.safe_load(file)
        if tags:
            return tags
    return {}
    
def loadPaperMetadata (filepath):
    with open(filepath, 'r') as file:
        paperMetadata = json.load(file)
        if paperMetadata:
            return paperMetadata
    return {}
    
def classifyTitle (title, keywords_to_classes):
    assigned_classes = set()
        
    for class_name, keywords in keywords_to_classes.items():
        for keyword in keywords:
            if keyword.lower() in title.lower():
                assigned_classes.add(class_name)

    return list(assigned_classes)

def extractCategories (paperMetadata):
    categories = classifyTitle(paperMetadata['title'], keywords_to_classes)
    return categories



paper_classes = loadPaperCategories(filepath_paperCategories)

with open(filepath_paperCategories, 'w+') as file:
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)

        if os.path.isfile(filepath):
            paperMetadata = loadPaperMetadata(filepath)
            doi = paperMetadata['externalIds']['DOI']
            if doi not in paper_classes:
                file.write(f'{doi}:\n')
                title_clean = paperMetadata["title"].replace('"','').replace("\u2010","-")
                print(title_clean)
                file.write(f'  title: \"{title_clean}\"\n')
                file.write(f'  categories:\n')
                categories = extractCategories(paperMetadata)
                for category in categories:
                    file.write(f'    - {category}\n')
