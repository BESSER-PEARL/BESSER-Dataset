from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class publication_SimpleFeature:

    pass
class publication_Organization:

    pass
class Journal:

    pass
class publication_JournalIssue(Journal):

    def __init__(self, volume: str, issue: str, issueSupplement: str, journalIssue: set["publication_JournalArticle"] = None, JournalIssue: "publication_JournalArticle" = None):
        self.volume = volume
        self.issue = issue
        self.issueSupplement = issueSupplement
        self.journalIssue = journalIssue if journalIssue is not None else set()
        self.JournalIssue = JournalIssue
        
        pass
    @property
    def issueSupplement(self):
        return self.__issueSupplement

    @issueSupplement.setter
    def issueSupplement(self, issueSupplement: str):
        self.__issueSupplement = issueSupplement


    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, volume: str):
        self.__volume = volume


    @property
    def issue(self):
        return self.__issue

    @issue.setter
    def issue(self, issue: str):
        self.__issue = issue


    @property
    def JournalIssue(self):
        return self.__JournalIssue

    @JournalIssue.setter
    def JournalIssue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication_JournalIssue__JournalIssue", None)
        self.__JournalIssue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "articles38"):
                opp_val = getattr(old_value, "articles38", None)
                if opp_val == self:
                    setattr(old_value, "articles38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "articles38"):
                opp_val = getattr(value, "articles38", None)
                setattr(value, "articles38", self)

    @property
    def journalIssue(self):
        return self.__journalIssue

    @journalIssue.setter
    def journalIssue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication_JournalIssue__journalIssue", None)
        self.__journalIssue = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "JournalArticle"):
                    opp_val = getattr(item, "JournalArticle", None)
                    
                    if opp_val == self:
                        setattr(item, "JournalArticle", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "JournalArticle"):
                    opp_val = getattr(item, "JournalArticle", None)
                    
                    setattr(item, "JournalArticle", self)
                    

class publication_Ontology:

    pass
class publication_Contact:

    pass
class Article:

    pass
class publication_JournalArticle(Article):

    pass
class publication_BookArticle(Article):

    def __init__(self, section: str, articles: set["publication_Book"] = None, BookArticle: "publication_Book" = None):
        self.section = section
        self.articles = articles if articles is not None else set()
        self.BookArticle = BookArticle
        
        pass
    @property
    def section(self):
        return self.__section

    @section.setter
    def section(self, section: str):
        self.__section = section


    @property
    def BookArticle(self):
        return self.__BookArticle

    @BookArticle.setter
    def BookArticle(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication_BookArticle__BookArticle", None)
        self.__BookArticle = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "book"):
                opp_val = getattr(old_value, "book", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "book"):
                opp_val = getattr(value, "book", None)
                if opp_val is None:
                    setattr(value, "book", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def articles(self):
        return self.__articles

    @articles.setter
    def articles(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication_BookArticle__articles", None)
        self.__articles = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Book"):
                    opp_val = getattr(item, "Book", None)
                    
                    if opp_val == self:
                        setattr(item, "Book", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Book"):
                    opp_val = getattr(item, "Book", None)
                    
                    setattr(item, "Book", self)
                    

class SimpleFeature:

    pass
class publication_SimpleCitation(SimpleFeature):

    def __init__(self, source: str, authorList: str, date: date, publication_SimpleCitation: "publication_BiblioReferenceSet" = None):
        self.source = source
        self.authorList = authorList
        self.date = date
        self.publication_SimpleCitation = publication_SimpleCitation
        
        pass
    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, source: str):
        self.__source = source


    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, date: date):
        self.__date = date


    @property
    def authorList(self):
        return self.__authorList

    @authorList.setter
    def authorList(self, authorList: str):
        self.__authorList = authorList


    @property
    def publication_SimpleCitation(self):
        return self.__publication_SimpleCitation

    @publication_SimpleCitation.setter
    def publication_SimpleCitation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication_SimpleCitation__publication_SimpleCitation", None)
        self.__publication_SimpleCitation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication_BiblioReferenceSet"):
                opp_val = getattr(old_value, "publication_BiblioReferenceSet", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication_BiblioReferenceSet"):
                opp_val = getattr(value, "publication_BiblioReferenceSet", None)
                if opp_val is None:
                    setattr(value, "publication_BiblioReferenceSet", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class SimpleIdentifier:

    pass
class publication_BiblioReferenceSet(SimpleIdentifier):

    pass
class publication_Indexing:

    def __init__(self, keywords: str, Indexing: "publication_BiblioReference" = None, publication_Indexing29: set["publication_SimpleOntologyTerm"] = None, publication_Indexing32: set["publication_SimpleOntologyTerm"] = None, publication_Indexing: "publication_Contact" = None, publication_Indexing24: "publication_LegalEntity" = None, publication_Indexing27: "publication_Ontology" = None, indexings: "publication_BiblioReference" = None):
        self.keywords = keywords
        self.Indexing = Indexing
        self.publication_Indexing29 = publication_Indexing29 if publication_Indexing29 is not None else set()
        self.publication_Indexing32 = publication_Indexing32 if publication_Indexing32 is not None else set()
        self.publication_Indexing = publication_Indexing
        self.publication_Indexing24 = publication_Indexing24
        self.publication_Indexing27 = publication_Indexing27
        self.indexings = indexings
        
        pass
    @property
    def keywords(self):
        return self.__keywords

    @keywords.setter
    def keywords(self, keywords: str):
        self.__keywords = keywords


    @property
    def publication_Indexing29(self):
        return self.__publication_Indexing29

    @publication_Indexing29.setter
    def publication_Indexing29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication_Indexing__publication_Indexing29", None)
        self.__publication_Indexing29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "publication_SimpleOntologyTerm30"):
                    opp_val = getattr(item, "publication_SimpleOntologyTerm30", None)
                    
                    if opp_val == self:
                        setattr(item, "publication_SimpleOntologyTerm30", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "publication_SimpleOntologyTerm30"):
                    opp_val = getattr(item, "publication_SimpleOntologyTerm30", None)
                    
                    setattr(item, "publication_SimpleOntologyTerm30", self)
                    

    @property
    def publication_Indexing(self):
        return self.__publication_Indexing

    @publication_Indexing.setter
    def publication_Indexing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication_Indexing__publication_Indexing", None)
        self.__publication_Indexing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication_Contact"):
                opp_val = getattr(old_value, "publication_Contact", None)
                if opp_val == self:
                    setattr(old_value, "publication_Contact", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication_Contact"):
                opp_val = getattr(value, "publication_Contact", None)
                setattr(value, "publication_Contact", self)

    @property
    def publication_Indexing24(self):
        return self.__publication_Indexing24

    @publication_Indexing24.setter
    def publication_Indexing24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication_Indexing__publication_Indexing24", None)
        self.__publication_Indexing24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication_LegalEntity25"):
                opp_val = getattr(old_value, "publication_LegalEntity25", None)
                if opp_val == self:
                    setattr(old_value, "publication_LegalEntity25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication_LegalEntity25"):
                opp_val = getattr(value, "publication_LegalEntity25", None)
                setattr(value, "publication_LegalEntity25", self)

    @property
    def Indexing(self):
        return self.__Indexing

    @Indexing.setter
    def Indexing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication_Indexing__Indexing", None)
        self.__Indexing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reference"):
                opp_val = getattr(old_value, "reference", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reference"):
                opp_val = getattr(value, "reference", None)
                if opp_val is None:
                    setattr(value, "reference", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def publication_Indexing32(self):
        return self.__publication_Indexing32

    @publication_Indexing32.setter
    def publication_Indexing32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication_Indexing__publication_Indexing32", None)
        self.__publication_Indexing32 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "publication_SimpleOntologyTerm33"):
                    opp_val = getattr(item, "publication_SimpleOntologyTerm33", None)
                    
                    if opp_val == self:
                        setattr(item, "publication_SimpleOntologyTerm33", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "publication_SimpleOntologyTerm33"):
                    opp_val = getattr(item, "publication_SimpleOntologyTerm33", None)
                    
                    setattr(item, "publication_SimpleOntologyTerm33", self)
                    

    @property
    def indexings(self):
        return self.__indexings

    @indexings.setter
    def indexings(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication_Indexing__indexings", None)
        self.__indexings = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BiblioReference"):
                opp_val = getattr(old_value, "BiblioReference", None)
                if opp_val == self:
                    setattr(old_value, "BiblioReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BiblioReference"):
                opp_val = getattr(value, "BiblioReference", None)
                setattr(value, "BiblioReference", self)

    @property
    def publication_Indexing27(self):
        return self.__publication_Indexing27

    @publication_Indexing27.setter
    def publication_Indexing27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication_Indexing__publication_Indexing27", None)
        self.__publication_Indexing27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication_Ontology"):
                opp_val = getattr(old_value, "publication_Ontology", None)
                if opp_val == self:
                    setattr(old_value, "publication_Ontology", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication_Ontology"):
                opp_val = getattr(value, "publication_Ontology", None)
                setattr(value, "publication_Ontology", self)

class publication_Content(SimpleFeature):

    def __init__(self, body: str, publication_Content: "publication_BiblioReference" = None, publication_Content20: "publication_BiblioReference" = None):
        self.body = body
        self.publication_Content = publication_Content
        self.publication_Content20 = publication_Content20
        
        pass
    @property
    def body(self):
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body


    @property
    def publication_Content(self):
        return self.__publication_Content

    @publication_Content.setter
    def publication_Content(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication_Content__publication_Content", None)
        self.__publication_Content = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication_BiblioReference12"):
                opp_val = getattr(old_value, "publication_BiblioReference12", None)
                if opp_val == self:
                    setattr(old_value, "publication_BiblioReference12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication_BiblioReference12"):
                opp_val = getattr(value, "publication_BiblioReference12", None)
                setattr(value, "publication_BiblioReference12", self)

    @property
    def publication_Content20(self):
        return self.__publication_Content20

    @publication_Content20.setter
    def publication_Content20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication_Content__publication_Content20", None)
        self.__publication_Content20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication_BiblioReference21"):
                opp_val = getattr(old_value, "publication_BiblioReference21", None)
                if opp_val == self:
                    setattr(old_value, "publication_BiblioReference21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication_BiblioReference21"):
                opp_val = getattr(value, "publication_BiblioReference21", None)
                setattr(value, "publication_BiblioReference21", self)

class publication_OrderedLegalEntitySet:

    pass
class publication_LegalEntity:

    pass
class publication_SimpleOntologyTerm:

    pass
class SimpleCitation:

    pass
class publication_BiblioReference(SimpleCitation):

    pass
class BiblioReference:

    pass
class publication_WebResource(BiblioReference):

    def __init__(self, uRL: str):
        self.uRL = uRL
        
        pass
    @property
    def uRL(self):
        return self.__uRL

    @uRL.setter
    def uRL(self, uRL: str):
        self.__uRL = uRL


class publication_Journal(BiblioReference):

    def __init__(self, iSSN: str, publication_Journal: "publication_SimpleOntologyTerm" = None):
        self.iSSN = iSSN
        self.publication_Journal = publication_Journal
        
        pass
    @property
    def iSSN(self):
        return self.__iSSN

    @iSSN.setter
    def iSSN(self, iSSN: str):
        self.__iSSN = iSSN


    @property
    def publication_Journal(self):
        return self.__publication_Journal

    @publication_Journal.setter
    def publication_Journal(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication_Journal__publication_Journal", None)
        self.__publication_Journal = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication_SimpleOntologyTerm36"):
                opp_val = getattr(old_value, "publication_SimpleOntologyTerm36", None)
                if opp_val == self:
                    setattr(old_value, "publication_SimpleOntologyTerm36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication_SimpleOntologyTerm36"):
                opp_val = getattr(value, "publication_SimpleOntologyTerm36", None)
                setattr(value, "publication_SimpleOntologyTerm36", self)

class publication_Multimedia(BiblioReference):

    pass
class publication_Book(BiblioReference):

    def __init__(self, iSBN: str, volume: str, edition: str, series: str, Book: "publication_BookArticle" = None, publication_Book: "publication_OrderedLegalEntitySet" = None, book: set["publication_BookArticle"] = None):
        self.iSBN = iSBN
        self.volume = volume
        self.edition = edition
        self.series = series
        self.Book = Book
        self.publication_Book = publication_Book
        self.book = book if book is not None else set()
        
        pass
    @property
    def iSBN(self):
        return self.__iSBN

    @iSBN.setter
    def iSBN(self, iSBN: str):
        self.__iSBN = iSBN


    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, volume: str):
        self.__volume = volume


    @property
    def series(self):
        return self.__series

    @series.setter
    def series(self, series: str):
        self.__series = series


    @property
    def edition(self):
        return self.__edition

    @edition.setter
    def edition(self, edition: str):
        self.__edition = edition


    @property
    def book(self):
        return self.__book

    @book.setter
    def book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication_Book__book", None)
        self.__book = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BookArticle"):
                    opp_val = getattr(item, "BookArticle", None)
                    
                    if opp_val == self:
                        setattr(item, "BookArticle", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BookArticle"):
                    opp_val = getattr(item, "BookArticle", None)
                    
                    setattr(item, "BookArticle", self)
                    

    @property
    def Book(self):
        return self.__Book

    @Book.setter
    def Book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication_Book__Book", None)
        self.__Book = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "articles"):
                opp_val = getattr(old_value, "articles", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "articles"):
                opp_val = getattr(value, "articles", None)
                if opp_val is None:
                    setattr(value, "articles", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def publication_Book(self):
        return self.__publication_Book

    @publication_Book.setter
    def publication_Book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication_Book__publication_Book", None)
        self.__publication_Book = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication_OrderedLegalEntitySet16"):
                opp_val = getattr(old_value, "publication_OrderedLegalEntitySet16", None)
                if opp_val == self:
                    setattr(old_value, "publication_OrderedLegalEntitySet16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication_OrderedLegalEntitySet16"):
                opp_val = getattr(value, "publication_OrderedLegalEntitySet16", None)
                setattr(value, "publication_OrderedLegalEntitySet16", self)

class publication_TechnicalReport(BiblioReference):

    pass
class publication_Protocol(BiblioReference):

    pass
class publication_Proceeding(BiblioReference):

    pass
class publication_Thesis(BiblioReference):

    pass
class publication_Article(BiblioReference):

    def __init__(self, lastPage: str, firstPage: str):
        self.lastPage = lastPage
        self.firstPage = firstPage
        
        pass
    @property
    def lastPage(self):
        return self.__lastPage

    @lastPage.setter
    def lastPage(self, lastPage: str):
        self.__lastPage = lastPage


    @property
    def firstPage(self):
        return self.__firstPage

    @firstPage.setter
    def firstPage(self, firstPage: str):
        self.__firstPage = firstPage

