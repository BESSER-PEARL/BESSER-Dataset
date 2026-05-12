from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class BIBTEX_Field(ABC):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class LocatedElement:

    pass
class BIBTEX_Entry(LocatedElement):

    def __init__(self, key: str, BIBTEX_Entry: set["Field"] = None):
        self.key = key
        self.BIBTEX_Entry = BIBTEX_Entry if BIBTEX_Entry is not None else set()
        
        pass
    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key


    @property
    def BIBTEX_Entry(self):
        return self.__BIBTEX_Entry

    @BIBTEX_Entry.setter
    def BIBTEX_Entry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BIBTEX_Entry__BIBTEX_Entry", None)
        self.__BIBTEX_Entry = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Field"):
                    opp_val = getattr(item, "Field", None)
                    
                    if opp_val == self:
                        setattr(item, "Field", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Field"):
                    opp_val = getattr(item, "Field", None)
                    
                    setattr(item, "Field", self)
                    

class Entry:

    pass
class BIBTEX_MastersThesis(Entry):

    pass
class BIBTEX_Misc(Entry):

    pass
class BIBTEX_PhdThesis(Entry):

    pass
class BIBTEX_Techreport(Entry):

    pass
class BIBTEX_Incollection(Entry):

    pass
class BIBTEX_Manual(Entry):

    pass
class BIBTEX_Proceedings(Entry):

    pass
class BIBTEX_Bibtex:

    pass
class BIBTEX_Inproceedings(Entry):

    pass
class BIBTEX_Booklet(Entry):

    pass
class BIBTEX_Inbook(Entry):

    pass
class BIBTEX_Book(Entry):

    pass
class BIBTEX_Article(Entry):

    pass
class Field:

    pass
class BIBTEX_Month(Field):

    pass
class BIBTEX_Year(Field):

    pass
class BIBTEX_Address(Field):

    pass
class BIBTEX_Doi(Field):

    pass
class BIBTEX_Url(Field):

    pass
class BIBTEX_Issn(Field):

    pass
class BIBTEX_BookTitle(Field):

    pass
class BIBTEX_Isbn(Field):

    pass
class BIBTEX_Journal(Field):

    pass
class BIBTEX_AbstractField(Field):

    pass
class BIBTEX_Title(Field):

    pass
class BIBTEX_Number(Field):

    pass
class BIBTEX_Day(Field):

    pass
class BIBTEX_Type(Field):

    pass
class BIBTEX_Organization(Field):

    pass
class BIBTEX_Institution(Field):

    pass
class BIBTEX_AuthorUrls(Field):

    pass
class BIBTEX_Edition(Field):

    pass
class BIBTEX_Editor(Field):

    pass
class BIBTEX_School(Field):

    pass
class BIBTEX_Howpublished(Field):

    pass
class BIBTEX_Publisher(Field):

    pass
class BIBTEX_Pages(Field):

    pass
class BIBTEX_Authors(Field):

    pass
class BIBTEX_Series(Field):

    pass
class BIBTEX_Text(Field):

    pass
class BIBTEX_Volume(Field):

    pass
class BIBTEX_Note(Field):

    pass
class BIBTEX_Chapter(Field):

    pass
class BIBTEX_LocatedElement(ABC):

    def __init__(self, location: str, commentsBefore: str, commentsAfter: str):
        self.location = location
        self.commentsBefore = commentsBefore
        self.commentsAfter = commentsAfter
        
        pass
    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location


    @property
    def commentsAfter(self):
        return self.__commentsAfter

    @commentsAfter.setter
    def commentsAfter(self, commentsAfter: str):
        self.__commentsAfter = commentsAfter


    @property
    def commentsBefore(self):
        return self.__commentsBefore

    @commentsBefore.setter
    def commentsBefore(self, commentsBefore: str):
        self.__commentsBefore = commentsBefore

