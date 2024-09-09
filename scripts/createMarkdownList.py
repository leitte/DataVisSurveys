import bibtexparser
import json
import yaml
import os

def loadPaperMetadata (filepath):
    with open(filepath, 'r') as file:
        paperMetadata = json.load(file)
        return paperMetadata

def createCitation (paperMetadata, tags=None):
    bibtexString = paperMetadata['citationStyles']['bibtex']
    bibDatabase = bibtexparser.loads(bibtexString)
    entry = bibDatabase.entries[0]
    #print(entry)
    citation = f"{entry['author']} ({entry['year']}). **{entry['title']}**. {entry.get('journal', 'N/A')}, {entry.get('volume', 'N/A')}({entry.get('number', 'N/A')}), {entry.get('pages', 'N/A')}. DOI: [{paperMetadata['externalIds'].get('DOI', 'N/A')}](https://doi.org/{paperMetadata['externalIds'].get('DOI', '')})"
    tag_template = '<span style="background-color: {color}; padding:3px; border-radius:8px">{tag}</span>'
    # colors: orange #ffad2a
    tags = ' '.join([tag_template.format(color='#f3ddb9', tag=tag) for tag in tags]) if tags else ''
    print('1.', citation + '<br>'+tags)

def loadPaperTags (filepath):
    with open(filepath, 'r') as file:
        tags = yaml.safe_load(file)
        return tags

directory = 'data/paperMetadata'
metadata = []

for filename in os.listdir(directory):
    filepath = os.path.join(directory, filename)

    if os.path.isfile(filepath):
        paperMetadata = loadPaperMetadata(filepath)
        if paperMetadata:
            metadata.append(paperMetadata)
        
sorted_papers = sorted(metadata, key=lambda x: x['year'])
tags = loadPaperTags(os.path.join('data/paperClassification','paperTags.yaml'))
for paper in sorted_papers:
    doi = paper['externalIds']['DOI']
    paperTags = tags.get(doi, [])
    createCitation(paper, paperTags)
    #print(paper['externalIds'].get('DOI', 'N/A')+':')