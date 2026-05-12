from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Cell:

    pass
class Row:

    pass
class Caption:

    pass
class LocatedElement:

    pass
class WikiTable_Caption(LocatedElement):

    def __init__(self, content: str):
        self.content = content
        
        pass
    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content


class WikiTable_Cell(LocatedElement):

    def __init__(self, content: str, isHeading: str, align: str, style: str):
        self.content = content
        self.isHeading = isHeading
        self.align = align
        self.style = style
        
        pass
    @property
    def isHeading(self):
        return self.__isHeading

    @isHeading.setter
    def isHeading(self, isHeading: str):
        self.__isHeading = isHeading


    @property
    def align(self):
        return self.__align

    @align.setter
    def align(self, align: str):
        self.__align = align


    @property
    def style(self):
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style


    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content


class WikiTable_Row(LocatedElement):

    pass
class WikiTable_Table(LocatedElement):

    def __init__(self, border: str, style: str, class_: str, WikiTable_Table: "Caption" = None, WikiTable_Table2: set["Row"] = None):
        self.border = border
        self.style = style
        self.class_ = class_
        self.WikiTable_Table = WikiTable_Table
        self.WikiTable_Table2 = WikiTable_Table2 if WikiTable_Table2 is not None else set()
        
        pass
    @property
    def style(self):
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style


    @property
    def class_(self):
        return self.__class_

    @class_.setter
    def class_(self, class_: str):
        self.__class_ = class_


    @property
    def border(self):
        return self.__border

    @border.setter
    def border(self, border: str):
        self.__border = border


    @property
    def WikiTable_Table(self):
        return self.__WikiTable_Table

    @WikiTable_Table.setter
    def WikiTable_Table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WikiTable_Table__WikiTable_Table", None)
        self.__WikiTable_Table = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Caption"):
                opp_val = getattr(old_value, "Caption", None)
                if opp_val == self:
                    setattr(old_value, "Caption", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Caption"):
                opp_val = getattr(value, "Caption", None)
                setattr(value, "Caption", self)

    @property
    def WikiTable_Table2(self):
        return self.__WikiTable_Table2

    @WikiTable_Table2.setter
    def WikiTable_Table2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WikiTable_Table__WikiTable_Table2", None)
        self.__WikiTable_Table2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Row"):
                    opp_val = getattr(item, "Row", None)
                    
                    if opp_val == self:
                        setattr(item, "Row", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Row"):
                    opp_val = getattr(item, "Row", None)
                    
                    setattr(item, "Row", self)
                    

class WikiTable_LocatedElement(ABC):

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

