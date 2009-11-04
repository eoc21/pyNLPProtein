'''
Created on Oct 23, 2009
A class to parse and extract abstracts from pubMed.
@author: ed
'''
import os, sys
from Bio import Entrez
from Bio import Medline
class PubMedParser():
    """
    Class to parse PDZ domain protein records
    from pubMed.
    """
    def __init__(self):
        self.Records = []
    
    def extractRecords(self):
        """
        Extracts a user defined number of records from
        pubMed based on a query string, ideally PDZ domain.
        """
        handle = Entrez.esearch("pubmed",sys.argv[1], retmax=int(sys.argv[2]))
        record = Entrez.read(handle)
        idlist = record["IdList"]
        handle = Entrez.efetch(db="pubmed", id=idlist, rettype="medline",retmode="text")
        records = Medline.parse(handle)
        self.Records = list(records)

def Main():
    pubMedParser = PubMedParser()
    pubMedParser.extractRecords()
    for record in pubMedParser.Records:
        try:
            print record["AB"]
        except KeyError:
            print "No abstract"
    
if __name__ == '__main__':
    Main()
