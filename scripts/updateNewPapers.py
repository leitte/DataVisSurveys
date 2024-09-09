import sqlite3
import time
from semanticScholarMetadataDownload import downloadPaperMetadata

connection = sqlite3.connect("/Users/leitte/Software/searchscholarqt/literaturesearch.db")
print(connection.total_changes)
cursor = connection.cursor()

cursor.execute("select doi from vissurveys where status>0")
rows = cursor.fetchall()
for row in rows:
    print(row[0][16:] if row else "no data")
    if (row[0]):
        downloadPaperMetadata(row[0][16:])
        time.sleep(1)