from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Booktype(Enum):
    science = "science"
    novel = "novel"


############################################
# Definition of Classes
############################################

class Paragraph:

    pass
class bz288963_Footnote(Paragraph):

    pass
class bz288963_Indentedpara(Paragraph):

    def __init__(self, indentSpace: str, bz288963_Indentedpara: "bz288963_DocumentRoot" = None):
        self.indentSpace = indentSpace
        self.bz288963_Indentedpara = bz288963_Indentedpara
        
    @property
    def indentSpace(self) -> str:
        return self.__indentSpace

    @indentSpace.setter
    def indentSpace(self, indentSpace: str):
        self.__indentSpace = indentSpace

    @property
    def bz288963_Indentedpara(self):
        return self.__bz288963_Indentedpara

    @bz288963_Indentedpara.setter
    def bz288963_Indentedpara(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bz288963_Indentedpara__bz288963_Indentedpara", None)
        self.__bz288963_Indentedpara = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bz288963_DocumentRoot14"):
                opp_val = getattr(old_value, "bz288963_DocumentRoot14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bz288963_DocumentRoot14"):
                opp_val = getattr(value, "bz288963_DocumentRoot14", None)
                if opp_val is None:
                    setattr(value, "bz288963_DocumentRoot14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class bz288963_EStringToStringMapEntry:

    pass
class bz288963_DocumentRoot:

    def __init__(self, mixed: str, bz288963_DocumentRoot: set["bz288963_EStringToStringMapEntry"] = None, bz288963_DocumentRoot6: set["bz288963_EStringToStringMapEntry"] = None, bz288963_DocumentRoot9: set["bz288963_Book"] = None, bz288963_DocumentRoot12: set["bz288963_Footnote"] = None, bz288963_DocumentRoot14: set["bz288963_Indentedpara"] = None, bz288963_DocumentRoot16: set["bz288963_Paragraph"] = None):
        self.mixed = mixed
        self.bz288963_DocumentRoot = bz288963_DocumentRoot if bz288963_DocumentRoot is not None else set()
        self.bz288963_DocumentRoot6 = bz288963_DocumentRoot6 if bz288963_DocumentRoot6 is not None else set()
        self.bz288963_DocumentRoot9 = bz288963_DocumentRoot9 if bz288963_DocumentRoot9 is not None else set()
        self.bz288963_DocumentRoot12 = bz288963_DocumentRoot12 if bz288963_DocumentRoot12 is not None else set()
        self.bz288963_DocumentRoot14 = bz288963_DocumentRoot14 if bz288963_DocumentRoot14 is not None else set()
        self.bz288963_DocumentRoot16 = bz288963_DocumentRoot16 if bz288963_DocumentRoot16 is not None else set()
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def bz288963_DocumentRoot6(self):
        return self.__bz288963_DocumentRoot6

    @bz288963_DocumentRoot6.setter
    def bz288963_DocumentRoot6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bz288963_DocumentRoot__bz288963_DocumentRoot6", None)
        self.__bz288963_DocumentRoot6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bz288963_EStringToStringMapEntry7"):
                    opp_val = getattr(item, "bz288963_EStringToStringMapEntry7", None)
                    
                    if opp_val == self:
                        setattr(item, "bz288963_EStringToStringMapEntry7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bz288963_EStringToStringMapEntry7"):
                    opp_val = getattr(item, "bz288963_EStringToStringMapEntry7", None)
                    
                    setattr(item, "bz288963_EStringToStringMapEntry7", self)
                    

    @property
    def bz288963_DocumentRoot16(self):
        return self.__bz288963_DocumentRoot16

    @bz288963_DocumentRoot16.setter
    def bz288963_DocumentRoot16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bz288963_DocumentRoot__bz288963_DocumentRoot16", None)
        self.__bz288963_DocumentRoot16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bz288963_Paragraph17"):
                    opp_val = getattr(item, "bz288963_Paragraph17", None)
                    
                    if opp_val == self:
                        setattr(item, "bz288963_Paragraph17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bz288963_Paragraph17"):
                    opp_val = getattr(item, "bz288963_Paragraph17", None)
                    
                    setattr(item, "bz288963_Paragraph17", self)
                    

    @property
    def bz288963_DocumentRoot12(self):
        return self.__bz288963_DocumentRoot12

    @bz288963_DocumentRoot12.setter
    def bz288963_DocumentRoot12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bz288963_DocumentRoot__bz288963_DocumentRoot12", None)
        self.__bz288963_DocumentRoot12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bz288963_Footnote"):
                    opp_val = getattr(item, "bz288963_Footnote", None)
                    
                    if opp_val == self:
                        setattr(item, "bz288963_Footnote", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bz288963_Footnote"):
                    opp_val = getattr(item, "bz288963_Footnote", None)
                    
                    setattr(item, "bz288963_Footnote", self)
                    

    @property
    def bz288963_DocumentRoot(self):
        return self.__bz288963_DocumentRoot

    @bz288963_DocumentRoot.setter
    def bz288963_DocumentRoot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bz288963_DocumentRoot__bz288963_DocumentRoot", None)
        self.__bz288963_DocumentRoot = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bz288963_EStringToStringMapEntry"):
                    opp_val = getattr(item, "bz288963_EStringToStringMapEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "bz288963_EStringToStringMapEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bz288963_EStringToStringMapEntry"):
                    opp_val = getattr(item, "bz288963_EStringToStringMapEntry", None)
                    
                    setattr(item, "bz288963_EStringToStringMapEntry", self)
                    

    @property
    def bz288963_DocumentRoot9(self):
        return self.__bz288963_DocumentRoot9

    @bz288963_DocumentRoot9.setter
    def bz288963_DocumentRoot9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bz288963_DocumentRoot__bz288963_DocumentRoot9", None)
        self.__bz288963_DocumentRoot9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bz288963_Book10"):
                    opp_val = getattr(item, "bz288963_Book10", None)
                    
                    if opp_val == self:
                        setattr(item, "bz288963_Book10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bz288963_Book10"):
                    opp_val = getattr(item, "bz288963_Book10", None)
                    
                    setattr(item, "bz288963_Book10", self)
                    

    @property
    def bz288963_DocumentRoot14(self):
        return self.__bz288963_DocumentRoot14

    @bz288963_DocumentRoot14.setter
    def bz288963_DocumentRoot14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bz288963_DocumentRoot__bz288963_DocumentRoot14", None)
        self.__bz288963_DocumentRoot14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bz288963_Indentedpara"):
                    opp_val = getattr(item, "bz288963_Indentedpara", None)
                    
                    if opp_val == self:
                        setattr(item, "bz288963_Indentedpara", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bz288963_Indentedpara"):
                    opp_val = getattr(item, "bz288963_Indentedpara", None)
                    
                    setattr(item, "bz288963_Indentedpara", self)
                    

class bz288963_Paragraph:

    def __init__(self, number: str, title: str, bz288963_Paragraph: "bz288963_Book" = None, bz288963_Paragraph17: "bz288963_DocumentRoot" = None):
        self.number = number
        self.title = title
        self.bz288963_Paragraph = bz288963_Paragraph
        self.bz288963_Paragraph17 = bz288963_Paragraph17
        
    @property
    def number(self) -> str:
        return self.__number

    @number.setter
    def number(self, number: str):
        self.__number = number

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def bz288963_Paragraph(self):
        return self.__bz288963_Paragraph

    @bz288963_Paragraph.setter
    def bz288963_Paragraph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bz288963_Paragraph__bz288963_Paragraph", None)
        self.__bz288963_Paragraph = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bz288963_Book3"):
                opp_val = getattr(old_value, "bz288963_Book3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bz288963_Book3"):
                opp_val = getattr(value, "bz288963_Book3", None)
                if opp_val is None:
                    setattr(value, "bz288963_Book3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bz288963_Paragraph17(self):
        return self.__bz288963_Paragraph17

    @bz288963_Paragraph17.setter
    def bz288963_Paragraph17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bz288963_Paragraph__bz288963_Paragraph17", None)
        self.__bz288963_Paragraph17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bz288963_DocumentRoot16"):
                opp_val = getattr(old_value, "bz288963_DocumentRoot16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bz288963_DocumentRoot16"):
                opp_val = getattr(value, "bz288963_DocumentRoot16", None)
                if opp_val is None:
                    setattr(value, "bz288963_DocumentRoot16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class bz288963_Book:

    def __init__(self, id: str, selfdef: str, type: str, bz288963_Book: "bz288963_Book" = None, bz288963_Book0: "bz288963_Book" = None, bz288963_Book3: set["bz288963_Paragraph"] = None, bz288963_Book10: "bz288963_DocumentRoot" = None):
        self.id = id
        self.selfdef = selfdef
        self.type = type
        self.bz288963_Book = bz288963_Book
        self.bz288963_Book0 = bz288963_Book0
        self.bz288963_Book3 = bz288963_Book3 if bz288963_Book3 is not None else set()
        self.bz288963_Book10 = bz288963_Book10
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def selfdef(self) -> str:
        return self.__selfdef

    @selfdef.setter
    def selfdef(self, selfdef: str):
        self.__selfdef = selfdef

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def bz288963_Book3(self):
        return self.__bz288963_Book3

    @bz288963_Book3.setter
    def bz288963_Book3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bz288963_Book__bz288963_Book3", None)
        self.__bz288963_Book3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bz288963_Paragraph"):
                    opp_val = getattr(item, "bz288963_Paragraph", None)
                    
                    if opp_val == self:
                        setattr(item, "bz288963_Paragraph", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bz288963_Paragraph"):
                    opp_val = getattr(item, "bz288963_Paragraph", None)
                    
                    setattr(item, "bz288963_Paragraph", self)
                    

    @property
    def bz288963_Book10(self):
        return self.__bz288963_Book10

    @bz288963_Book10.setter
    def bz288963_Book10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bz288963_Book__bz288963_Book10", None)
        self.__bz288963_Book10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bz288963_DocumentRoot9"):
                opp_val = getattr(old_value, "bz288963_DocumentRoot9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bz288963_DocumentRoot9"):
                opp_val = getattr(value, "bz288963_DocumentRoot9", None)
                if opp_val is None:
                    setattr(value, "bz288963_DocumentRoot9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bz288963_Book(self):
        return self.__bz288963_Book

    @bz288963_Book.setter
    def bz288963_Book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bz288963_Book__bz288963_Book", None)
        self.__bz288963_Book = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bz288963_Book0"):
                opp_val = getattr(old_value, "bz288963_Book0", None)
                if opp_val == self:
                    setattr(old_value, "bz288963_Book0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bz288963_Book0"):
                opp_val = getattr(value, "bz288963_Book0", None)
                setattr(value, "bz288963_Book0", self)

    @property
    def bz288963_Book0(self):
        return self.__bz288963_Book0

    @bz288963_Book0.setter
    def bz288963_Book0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bz288963_Book__bz288963_Book0", None)
        self.__bz288963_Book0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bz288963_Book"):
                opp_val = getattr(old_value, "bz288963_Book", None)
                if opp_val == self:
                    setattr(old_value, "bz288963_Book", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bz288963_Book"):
                opp_val = getattr(value, "bz288963_Book", None)
                setattr(value, "bz288963_Book", self)
