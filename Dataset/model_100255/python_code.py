from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class HtmlProfile:

    pass
class wikigen_Article(HtmlProfile):

    def __init__(self, nbColumns: int, generateTOC: bool):
        self.nbColumns = nbColumns
        self.generateTOC = generateTOC
        
        pass
    @property
    def generateTOC(self):
        return self.__generateTOC

    @generateTOC.setter
    def generateTOC(self, generateTOC: bool):
        self.__generateTOC = generateTOC


    @property
    def nbColumns(self):
        return self.__nbColumns

    @nbColumns.setter
    def nbColumns(self, nbColumns: int):
        self.__nbColumns = nbColumns


class wikigen_Document:

    pass
class wikigen_HtmlProfile(ABC):

    pass
class wikigen_GenHtmlDocument:

    def __init__(self, filename: str, wikigen_GenHtmlDocument3: set["wikigen_Document"] = None, wikigen_GenHtmlDocument: "wikigen_HtmlProfile" = None):
        self.filename = filename
        self.wikigen_GenHtmlDocument3 = wikigen_GenHtmlDocument3 if wikigen_GenHtmlDocument3 is not None else set()
        self.wikigen_GenHtmlDocument = wikigen_GenHtmlDocument
        
        pass
    @property
    def filename(self):
        return self.__filename

    @filename.setter
    def filename(self, filename: str):
        self.__filename = filename


    @property
    def wikigen_GenHtmlDocument(self):
        return self.__wikigen_GenHtmlDocument

    @wikigen_GenHtmlDocument.setter
    def wikigen_GenHtmlDocument(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wikigen_GenHtmlDocument__wikigen_GenHtmlDocument", None)
        self.__wikigen_GenHtmlDocument = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wikigen_HtmlProfile"):
                opp_val = getattr(old_value, "wikigen_HtmlProfile", None)
                if opp_val == self:
                    setattr(old_value, "wikigen_HtmlProfile", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wikigen_HtmlProfile"):
                opp_val = getattr(value, "wikigen_HtmlProfile", None)
                setattr(value, "wikigen_HtmlProfile", self)

    @property
    def wikigen_GenHtmlDocument3(self):
        return self.__wikigen_GenHtmlDocument3

    @wikigen_GenHtmlDocument3.setter
    def wikigen_GenHtmlDocument3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wikigen_GenHtmlDocument__wikigen_GenHtmlDocument3", None)
        self.__wikigen_GenHtmlDocument3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "wikigen_Document"):
                    opp_val = getattr(item, "wikigen_Document", None)
                    
                    if opp_val == self:
                        setattr(item, "wikigen_Document", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "wikigen_Document"):
                    opp_val = getattr(item, "wikigen_Document", None)
                    
                    setattr(item, "wikigen_Document", self)
                    

class wikigen_GenLatexDocument:

    def __init__(self, filename: str, title: str, authors: str, wikigen_GenLatexDocument: set["wikigen_Container"] = None):
        self.filename = filename
        self.title = title
        self.authors = authors
        self.wikigen_GenLatexDocument = wikigen_GenLatexDocument if wikigen_GenLatexDocument is not None else set()
        
        pass
    @property
    def authors(self):
        return self.__authors

    @authors.setter
    def authors(self, authors: str):
        self.__authors = authors


    @property
    def filename(self):
        return self.__filename

    @filename.setter
    def filename(self, filename: str):
        self.__filename = filename


    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title


    @property
    def wikigen_GenLatexDocument(self):
        return self.__wikigen_GenLatexDocument

    @wikigen_GenLatexDocument.setter
    def wikigen_GenLatexDocument(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wikigen_GenLatexDocument__wikigen_GenLatexDocument", None)
        self.__wikigen_GenLatexDocument = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "wikigen_Container"):
                    opp_val = getattr(item, "wikigen_Container", None)
                    
                    if opp_val == self:
                        setattr(item, "wikigen_Container", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "wikigen_Container"):
                    opp_val = getattr(item, "wikigen_Container", None)
                    
                    setattr(item, "wikigen_Container", self)
                    

class wikigen_Container:

    pass