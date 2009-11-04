'''
Created on Oct 29, 2009
Class to process an abstract, firstly by sentence segmentation, secondly word tokenization
and thirdly part of speech tagging.
@author: ed
'''
import nltk, re, pprint
from PubMedParser import *
from Bio import Entrez
from Bio import Medline

class PreProcessor():
    """
    Instantiate a PreProcessor
    """
    def __init__(self):
        self.document = []
        self.sentences = []
        self.tokens = []
        self.partsOfSpeech = []
    
    def SegmentSentence(self,document):
        """
        Segments a document into sentences.
        """
        self.sentences = nltk.sent_tokenize(document)
        return self.sentences
    
    def Tokenization(self):
        """
        Tokenizes a sentence.
        """
        self.tokens = [nltk.word_tokenizer(sent) for sent in self.sentences]
    
    def PartOfSpeechTagging(self):
        """
        Adds part of speech tagging to a tokenized sentence.
        """
        self.partsOfSpeech = [nltk.pos_tag(sent) for sent in self.tokens]
         
    def PreprocessAll(self,document):
        """
        Takes a document, segments into sentences, tokenizes words, then adds
        part of speech tagging.
        """
        sentences = nltk.sent_tokenize(document)
        sentences = [nltk.word_tokenize(sent) for sent in sentences]
        self.partsOfSpeech = [nltk.pos_tag(sent) for sent in sentences]

def Main():
    pubMedParser = PubMedParser()
    pubMedParser.extractRecords()
    documentPreprocessor = PreProcessor()
    for record in pubMedParser.Records:
        try:
            documentPreprocessor.PreprocessAll(str(record))
            print documentPreprocessor.partsOfSpeech
        except KeyError:
            print "No abstract"
    
if __name__ == '__main__':
    Main()
  
   