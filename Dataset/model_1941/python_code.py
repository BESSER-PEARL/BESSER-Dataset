from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class docbook_ImageData:

    def __init__(self, fileref: str, width: str, depth: str, ImageData: "docbook_ImageObject" = None, content52: "docbook_ImageObject" = None):
        self.fileref = fileref
        self.width = width
        self.depth = depth
        self.ImageData = ImageData
        self.content52 = content52
        
    @property
    def width(self) -> str:
        return self.__width

    @width.setter
    def width(self, width: str):
        self.__width = width

    @property
    def depth(self) -> str:
        return self.__depth

    @depth.setter
    def depth(self, depth: str):
        self.__depth = depth

    @property
    def fileref(self) -> str:
        return self.__fileref

    @fileref.setter
    def fileref(self, fileref: str):
        self.__fileref = fileref

    @property
    def ImageData(self):
        return self.__ImageData

    @ImageData.setter
    def ImageData(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_docbook_ImageData__ImageData", None)
        self.__ImageData = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "imageObject"):
                opp_val = getattr(old_value, "imageObject", None)
                if opp_val == self:
                    setattr(old_value, "imageObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "imageObject"):
                opp_val = getattr(value, "imageObject", None)
                setattr(value, "imageObject", self)

    @property
    def content52(self):
        return self.__content52

    @content52.setter
    def content52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_docbook_ImageData__content52", None)
        self.__content52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ImageObject53"):
                opp_val = getattr(old_value, "ImageObject53", None)
                if opp_val == self:
                    setattr(old_value, "ImageObject53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ImageObject53"):
                opp_val = getattr(value, "ImageObject53", None)
                setattr(value, "ImageObject53", self)

class docbook_ImageObject:

    pass
class docbook_MediaObject:

    pass
class ParaMixedContent:

    pass
class docbook_SimpleText(ParaMixedContent):

    def __init__(self, data: str):
        self.data = data
        
    @property
    def data(self) -> str:
        return self.__data

    @data.setter
    def data(self, data: str):
        self.__data = data

class Para:

    pass
class docbook_Tip(Para):

    pass
class docbook_Warning(Para):

    pass
class docbook_ProgramListing(Para):

    pass
class docbook_Link(ParaMixedContent):

    pass
class docbook_Ulink(ParaMixedContent):

    pass
class docbook_Emphasis(ParaMixedContent):

    pass
class docbook_XMLElement(ABC):

    def __init__(self, id: str):
        self.id = id
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

class SectionMixedContent:

    pass
class docbook_Para(SectionMixedContent):

    pass
class docbook_ParaMixedContent(SectionMixedContent):

    pass
class docbook_TitledElement(ABC):

    pass
class docbook_Title:

    pass
class docbook_SectionMixedContent(ABC):

    pass
class TitledElement:

    pass
class docbook_Figure(ParaMixedContent, TitledElement):

    pass
class docbook_Subtitle:

    pass
class XMLElement:

    pass
class docbook_Section(TitledElement, XMLElement, SectionMixedContent):

    pass
class docbook_Chapter(TitledElement, XMLElement):

    pass
class docbook_Bookinfo(XMLElement):

    def __init__(self, date: str, pubdate: str, bookinfo5: "docbook_Subtitle" = None, bookinfo7: set["docbook_Author"] = None, Bookinfo: "docbook_Book" = None, bookinfo: "docbook_Book" = None, Bookinfo9: "docbook_Author" = None, Bookinfo11: "docbook_Subtitle" = None):
        self.date = date
        self.pubdate = pubdate
        self.bookinfo5 = bookinfo5
        self.bookinfo7 = bookinfo7 if bookinfo7 is not None else set()
        self.Bookinfo = Bookinfo
        self.bookinfo = bookinfo
        self.Bookinfo9 = Bookinfo9
        self.Bookinfo11 = Bookinfo11
        
    @property
    def pubdate(self) -> str:
        return self.__pubdate

    @pubdate.setter
    def pubdate(self, pubdate: str):
        self.__pubdate = pubdate

    @property
    def date(self) -> str:
        return self.__date

    @date.setter
    def date(self, date: str):
        self.__date = date

    @property
    def Bookinfo11(self):
        return self.__Bookinfo11

    @Bookinfo11.setter
    def Bookinfo11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_docbook_Bookinfo__Bookinfo11", None)
        self.__Bookinfo11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "subtitle"):
                opp_val = getattr(old_value, "subtitle", None)
                if opp_val == self:
                    setattr(old_value, "subtitle", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "subtitle"):
                opp_val = getattr(value, "subtitle", None)
                setattr(value, "subtitle", self)

    @property
    def Bookinfo9(self):
        return self.__Bookinfo9

    @Bookinfo9.setter
    def Bookinfo9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_docbook_Bookinfo__Bookinfo9", None)
        self.__Bookinfo9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "author"):
                opp_val = getattr(old_value, "author", None)
                if opp_val == self:
                    setattr(old_value, "author", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "author"):
                opp_val = getattr(value, "author", None)
                setattr(value, "author", self)

    @property
    def Bookinfo(self):
        return self.__Bookinfo

    @Bookinfo.setter
    def Bookinfo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_docbook_Bookinfo__Bookinfo", None)
        self.__Bookinfo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "book"):
                opp_val = getattr(old_value, "book", None)
                if opp_val == self:
                    setattr(old_value, "book", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "book"):
                opp_val = getattr(value, "book", None)
                setattr(value, "book", self)

    @property
    def bookinfo(self):
        return self.__bookinfo

    @bookinfo.setter
    def bookinfo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_docbook_Bookinfo__bookinfo", None)
        self.__bookinfo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Book"):
                opp_val = getattr(old_value, "Book", None)
                if opp_val == self:
                    setattr(old_value, "Book", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Book"):
                opp_val = getattr(value, "Book", None)
                setattr(value, "Book", self)

    @property
    def bookinfo7(self):
        return self.__bookinfo7

    @bookinfo7.setter
    def bookinfo7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_docbook_Bookinfo__bookinfo7", None)
        self.__bookinfo7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Author"):
                    opp_val = getattr(item, "Author", None)
                    
                    if opp_val == self:
                        setattr(item, "Author", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Author"):
                    opp_val = getattr(item, "Author", None)
                    
                    setattr(item, "Author", self)
                    

    @property
    def bookinfo5(self):
        return self.__bookinfo5

    @bookinfo5.setter
    def bookinfo5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_docbook_Bookinfo__bookinfo5", None)
        self.__bookinfo5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Subtitle"):
                opp_val = getattr(old_value, "Subtitle", None)
                if opp_val == self:
                    setattr(old_value, "Subtitle", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Subtitle"):
                opp_val = getattr(value, "Subtitle", None)
                setattr(value, "Subtitle", self)

class docbook_Book(XMLElement):

    pass
class docbook_Author:

    def __init__(self, honorific: str, firstname: str, surname: str, authorblug: str, Author: "docbook_Bookinfo" = None, author: "docbook_Bookinfo" = None):
        self.honorific = honorific
        self.firstname = firstname
        self.surname = surname
        self.authorblug = authorblug
        self.Author = Author
        self.author = author
        
    @property
    def honorific(self) -> str:
        return self.__honorific

    @honorific.setter
    def honorific(self, honorific: str):
        self.__honorific = honorific

    @property
    def authorblug(self) -> str:
        return self.__authorblug

    @authorblug.setter
    def authorblug(self, authorblug: str):
        self.__authorblug = authorblug

    @property
    def firstname(self) -> str:
        return self.__firstname

    @firstname.setter
    def firstname(self, firstname: str):
        self.__firstname = firstname

    @property
    def surname(self) -> str:
        return self.__surname

    @surname.setter
    def surname(self, surname: str):
        self.__surname = surname

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_docbook_Author__author", None)
        self.__author = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Bookinfo9"):
                opp_val = getattr(old_value, "Bookinfo9", None)
                if opp_val == self:
                    setattr(old_value, "Bookinfo9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Bookinfo9"):
                opp_val = getattr(value, "Bookinfo9", None)
                setattr(value, "Bookinfo9", self)

    @property
    def Author(self):
        return self.__Author

    @Author.setter
    def Author(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_docbook_Author__Author", None)
        self.__Author = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bookinfo7"):
                opp_val = getattr(old_value, "bookinfo7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bookinfo7"):
                opp_val = getattr(value, "bookinfo7", None)
                if opp_val is None:
                    setattr(value, "bookinfo7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
