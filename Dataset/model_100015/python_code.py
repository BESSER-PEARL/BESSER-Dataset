from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class bibtex_Document:

    def __init__(self, type: str, file: str, cites: int, authors: str, abstract: str, year: str, month: str, title: str, key: str, doi: str, url: str, unparsedAuthors: str, bibtex_Document: "bibtex_Model" = None):
        self.type = type
        self.file = file
        self.cites = cites
        self.authors = authors
        self.abstract = abstract
        self.year = year
        self.month = month
        self.title = title
        self.key = key
        self.doi = doi
        self.url = url
        self.unparsedAuthors = unparsedAuthors
        self.bibtex_Document = bibtex_Document
        
        pass
    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year: str):
        self.__year = year


    @property
    def authors(self):
        return self.__authors

    @authors.setter
    def authors(self, authors: str):
        self.__authors = authors


    @property
    def doi(self):
        return self.__doi

    @doi.setter
    def doi(self, doi: str):
        self.__doi = doi


    @property
    def cites(self):
        return self.__cites

    @cites.setter
    def cites(self, cites: int):
        self.__cites = cites


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, month: str):
        self.__month = month


    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, url: str):
        self.__url = url


    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key


    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title


    @property
    def file(self):
        return self.__file

    @file.setter
    def file(self, file: str):
        self.__file = file


    @property
    def abstract(self):
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: str):
        self.__abstract = abstract


    @property
    def unparsedAuthors(self):
        return self.__unparsedAuthors

    @unparsedAuthors.setter
    def unparsedAuthors(self, unparsedAuthors: str):
        self.__unparsedAuthors = unparsedAuthors


    @property
    def bibtex_Document(self):
        return self.__bibtex_Document

    @bibtex_Document.setter
    def bibtex_Document(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtex_Document__bibtex_Document", None)
        self.__bibtex_Document = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtex_Model"):
                opp_val = getattr(old_value, "bibtex_Model", None)
                if opp_val == self:
                    setattr(old_value, "bibtex_Model", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtex_Model"):
                opp_val = getattr(value, "bibtex_Model", None)
                setattr(value, "bibtex_Model", self)

class bibtex_Model:

    pass