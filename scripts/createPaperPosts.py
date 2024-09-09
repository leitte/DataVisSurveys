import os
import re
import json
import yaml

directory = 'data/paperMetadata'

def loadPaperMetadata (filepath):
    with open(filepath, 'r') as file:
        paperMetadata = json.load(file)
        return paperMetadata
    
def createAuthorsString (authors):
    authors_string = ', '.join([author.get('name','') for author in authors[:-1]]) + (' & ' + authors[-1]['name'] if len(authors) > 1 else '')
    return authors_string

npapers = 0

for filename in os.listdir(directory):
    filepath = os.path.join(directory, filename)

    if os.path.isfile(filepath):
        print('++',filepath)
        paperMetadata = loadPaperMetadata(filepath)
        if paperMetadata:
            print(paperMetadata['title'])
            data = {
                'layout': 'post',
                'title': paperMetadata['title'],
                'date': paperMetadata['publicationDate']
            }
            title_short = re.sub(r'[^a-zA-Z0-9-]', '', paperMetadata['title'][:30].lower().replace(' ','-'))
            date = paperMetadata['publicationDate'] if paperMetadata['publicationDate'] else f"{paperMetadata['year']}-01-01"
            filename = f"{date}-{title_short}"
            with open(f'posts/{filename}.md', 'w') as file:
                file.write('---\n')
                #yaml.dump(data, file)
                file.write(f"layout: post\n")
                file.write(f"title: \"{paperMetadata['title']}\"\n")
                file.write(f"date: {date}\n")
                authors = createAuthorsString(paperMetadata['authors'])
                file.write(f"authors: {authors}\n")
                file.write(f"venue: \"{paperMetadata['venue']}\"\n")
                file.write(f"doi: {paperMetadata['externalIds']['DOI']}\n")
                file.write('---\n')
                abstract = paperMetadata.get('abstract','')
                file.write(abstract.strip() if abstract else "")
                file.write('\n')

                npapers += 1

    if npapers > 10:
        break