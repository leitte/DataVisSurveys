# DataVisSurveys

## Adding new papers

1. Add the doi to the file [includedPapersDOIs.txt](data/includedPapersDOIs.txt).
1. Add the paper metadata from semanticscholar using the script [downloadScholarMetadataFromList.py](scripts/downloadScholarMetadataFromList.py)
    ```
    python scripts/downloadScholarMetadataFromList.py
    ```
    The script only adds missing metadata.
2. Validate all new metadata in directory [data/paperMetadataNew/](data/paperMetadataNew/)
3. Copy the new files from [data/paperMetadataNew/](data/paperMetadataNew/) to [data/paperMetadata/](data/paperMetadata/).
4. Add categories for the new paper(s) in [paperCategories2.yaml](data/paperClassification/paperCategories2.yaml). Init the structure for the new papers and some automatically extracted categories using the following script.
   ```
   python scripts/initPaperCategories.py
   ```
5. Commit changes.