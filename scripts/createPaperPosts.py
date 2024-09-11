import os
import re
import json
import yaml

directory = 'data/paperMetadata'
filepath_paperClasses = 'data/paperClassification/paperCategories2.yaml'

def loadPaperMetadata (filepath):
    with open(filepath, 'r') as file:
        paperMetadata = json.load(file)
        return paperMetadata

def standardizeName (name):
    parts = name.split()
    if len(parts) > 1:
        return f"{parts[0][0]}. " + ' '.join(parts[1:])
    return name

def createAuthorsString (authors):
    authors_string = ', '.join([standardizeName(author.get('name','')) for author in authors[:-1]]) + (' & ' + standardizeName(authors[-1]['name']) if len(authors) > 1 else '')
    return authors_string

def loadPaperTags (filepath):
    with open(filepath, 'r') as file:
        tags = yaml.safe_load(file)
        return tags
    
def createIdToLabelMapping ():
    def extractMapping (items, result):
        for item in items:
            result[item['id']] = item['label']
            if 'children' in item:
                extractMapping( item['children'], result)

    with open('data/taxonomy.yml', 'r') as file:
        taxonomy = yaml.safe_load(file)

        id_to_label = {}
        extractMapping(taxonomy, id_to_label)
        return id_to_label


    
npapers = 0
paper_categories = loadPaperTags(filepath_paperClasses)
id_to_label = createIdToLabelMapping()

for filename in os.listdir(directory):
    filepath = os.path.join(directory, filename)

    if os.path.isfile(filepath):
        print('++',filepath)
        paperMetadata = loadPaperMetadata(filepath)
        if paperMetadata:
            print(paperMetadata['title'])

            title_short = re.sub(r'[^a-zA-Z0-9-]', '', paperMetadata['title'][:30].lower().replace(' ','-'))
            date = paperMetadata['publicationDate'] if paperMetadata['publicationDate'] else f"{paperMetadata['year']}-01-01"
            filename = f"{date}-{title_short}"
            with open(f'posts/{filename}.md', 'w') as file:
                file.write('---\n')
                #yaml.dump(data, file)
                file.write(f"layout: post\n")
                file.write("excerpt_image: NO_EXCERPT_IMAGE\n")
                title_clean = paperMetadata['title'].replace('"','')
                file.write(f"title: \"{title_clean}\"\n")
                file.write(f"date: {date}\n")
                authors = createAuthorsString(paperMetadata['authors'])
                file.write(f"authors: {authors}\n")
                file.write(f"venue: \"{paperMetadata['venue']}\"\n")
                file.write(f"doi: {paperMetadata['externalIds']['DOI']}\n")
            
                tags = paper_categories.get(paperMetadata['externalIds']['DOI'], {})
                if ('categories' in tags) and (tags['categories']):
                    file.write("categories:\n")
                    for tag in tags['categories']:
                        file.write(f"  - {id_to_label[tag]}\n")
                file.write('---\n')
                abstract = paperMetadata.get('abstract','')
                file.write(abstract.strip() if abstract else "")
                file.write('\n')

                npapers += 1

    #if npapers > 50:
    #    break