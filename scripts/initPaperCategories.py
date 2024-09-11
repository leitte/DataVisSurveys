import os
import yaml
import json

directory = 'data/paperMetadata'
filepath_paperCategories = 'data/paperClassification/paperCategories2.yaml'

keywords_to_classes = {
    'Taxonomy': ['taxonomy'],
    'Survey': ['survey', 'state of', 'state-of'],
    'Review': ['review'],
    'TextData': [' text'],
    'GraphData': ['graph', 'network', 'tree', 'edge', 'matrix', 'set'],
    'SoftwareDomain': ['algorithm', 'program', 'software'],
    'HighDimensionalData': ['high-dimensional', 'dimension'],
    'SpatialData': ['volumne', 'surface', 'flow'],
    'Charts': ['task', 'chart', 'grammar', 'information visualization'],
    'UncertaintyMethod': ['uncertain']
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

def loadAllMetadata (directory):
    paperMetadata = []
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)

        if os.path.isfile(filepath):
            paperMetadata.append(loadPaperMetadata(filepath))

    return paperMetadata



paper_classes = loadPaperCategories(filepath_paperCategories)
paper_metadata = loadAllMetadata(directory)
paper_metadata_sortedYear = sorted(paper_metadata, key=lambda x: x['publicationDate'] if ('publicationDate' in x) and (x['publicationDate']) else str(x['year']), reverse=True)

with open(filepath_paperCategories, 'w') as file:
    for paperMetadata in paper_metadata_sortedYear:
        doi = paperMetadata['externalIds']['DOI']
        file.write(f'{doi}:\n')
        title_clean = paperMetadata["title"].replace('"','').replace("\u2010","-")
        file.write(f'  title: \"{title_clean}\"\n')
        file.write(f'  categories:\n')
        print(title_clean)
        
        if doi not in paper_classes:
            categories = extractCategories(paperMetadata)
        else:
            categories = paper_classes[doi]['categories']

        if categories:
            for category in categories:
                file.write(f'    - {category}\n')
