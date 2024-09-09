import requests
import json
import time

def downloadPaperMetadata (doi, directory="data/paperMetadata"):
    url = 'https://api.semanticscholar.org/graph/v1/paper/DOI:' + doi

    paperDataQueryParams = {'fields': 'title,year,abstract,authors.name,url,venue,publicationVenue,journal,externalIds,referenceCount,openAccessPdf,fieldsOfStudy,s2FieldsOfStudy,publicationTypes,publicationDate,citationStyles,references'}
    response = requests.get(url, params=paperDataQueryParams)
    time.sleep(1)

    if response.status_code == 200:
        response = response.json()
        filename = doi.replace('/','__')
        with open(f'{directory}/{filename}.json', 'w') as file:
            json.dump(response, file, indent=2)
        #print(response)
    else:
        print(f"response failed with errorcode:{response.status_code}")

doi = "10.1109/TVCG.2016.2549018"
downloadPaperMetadata(doi)