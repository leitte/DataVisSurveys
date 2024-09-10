from semanticScholarMetadataDownload import downloadPaperMetadata
import os

with open('data/includedPapersDOIs.txt', 'r') as file:
    dois = file.readlines()

dois = [doi.strip() for doi in dois]
directory = 'data/paperMetadataNew'
directoryFinal = 'data/paperMetadata'

for doi in dois:
    if doi.startswith('#'):
        continue
    #print(doi)
    doi_short = doi[16:].replace('/','__')
    filepath = os.path.join(directoryFinal, f'{doi_short}.json')
    if os.path.exists(filepath):
        print('  --- got file', doi[16:])
    else:
        print('  +++ new file', doi[16:])
        downloadPaperMetadata(doi[16:], directory)