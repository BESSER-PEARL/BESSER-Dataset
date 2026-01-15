from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Documentation_InformalTableValueEntry:

    def __init__(self, value: str, Documentation_InformalTableValueEntry: "Documentation_InformalTableValueRow" = None):
        self.value = value
        self.Documentation_InformalTableValueEntry = Documentation_InformalTableValueEntry
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def Documentation_InformalTableValueEntry(self):
        return self.__Documentation_InformalTableValueEntry

    @Documentation_InformalTableValueEntry.setter
    def Documentation_InformalTableValueEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Documentation_InformalTableValueEntry__Documentation_InformalTableValueEntry", None)
        self.__Documentation_InformalTableValueEntry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Documentation_InformalTableValueRow22"):
                opp_val = getattr(old_value, "Documentation_InformalTableValueRow22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Documentation_InformalTableValueRow22"):
                opp_val = getattr(value, "Documentation_InformalTableValueRow22", None)
                if opp_val is None:
                    setattr(value, "Documentation_InformalTableValueRow22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Documentation_InformalTableValueRow:

    pass
class Documentation_InformalTableValueBody:

    pass
class Documentation_InformalTableValueHead:

    pass
class Documentation_InformalTableValueGroup:

    def __init__(self, cols: int, Documentation_InformalTableValueGroup: "Documentation_InformalTableValue" = None, Documentation_InformalTableValueGroup13: "Documentation_InformalTableValueHead" = None, Documentation_InformalTableValueGroup15: "Documentation_InformalTableValueBody" = None):
        self.cols = cols
        self.Documentation_InformalTableValueGroup = Documentation_InformalTableValueGroup
        self.Documentation_InformalTableValueGroup13 = Documentation_InformalTableValueGroup13
        self.Documentation_InformalTableValueGroup15 = Documentation_InformalTableValueGroup15
        
    @property
    def cols(self) -> int:
        return self.__cols

    @cols.setter
    def cols(self, cols: int):
        self.__cols = cols

    @property
    def Documentation_InformalTableValueGroup(self):
        return self.__Documentation_InformalTableValueGroup

    @Documentation_InformalTableValueGroup.setter
    def Documentation_InformalTableValueGroup(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Documentation_InformalTableValueGroup__Documentation_InformalTableValueGroup", None)
        self.__Documentation_InformalTableValueGroup = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Documentation_InformalTableValue"):
                opp_val = getattr(old_value, "Documentation_InformalTableValue", None)
                if opp_val == self:
                    setattr(old_value, "Documentation_InformalTableValue", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Documentation_InformalTableValue"):
                opp_val = getattr(value, "Documentation_InformalTableValue", None)
                setattr(value, "Documentation_InformalTableValue", self)

    @property
    def Documentation_InformalTableValueGroup13(self):
        return self.__Documentation_InformalTableValueGroup13

    @Documentation_InformalTableValueGroup13.setter
    def Documentation_InformalTableValueGroup13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Documentation_InformalTableValueGroup__Documentation_InformalTableValueGroup13", None)
        self.__Documentation_InformalTableValueGroup13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Documentation_InformalTableValueHead"):
                opp_val = getattr(old_value, "Documentation_InformalTableValueHead", None)
                if opp_val == self:
                    setattr(old_value, "Documentation_InformalTableValueHead", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Documentation_InformalTableValueHead"):
                opp_val = getattr(value, "Documentation_InformalTableValueHead", None)
                setattr(value, "Documentation_InformalTableValueHead", self)

    @property
    def Documentation_InformalTableValueGroup15(self):
        return self.__Documentation_InformalTableValueGroup15

    @Documentation_InformalTableValueGroup15.setter
    def Documentation_InformalTableValueGroup15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Documentation_InformalTableValueGroup__Documentation_InformalTableValueGroup15", None)
        self.__Documentation_InformalTableValueGroup15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Documentation_InformalTableValueBody"):
                opp_val = getattr(old_value, "Documentation_InformalTableValueBody", None)
                if opp_val == self:
                    setattr(old_value, "Documentation_InformalTableValueBody", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Documentation_InformalTableValueBody"):
                opp_val = getattr(value, "Documentation_InformalTableValueBody", None)
                setattr(value, "Documentation_InformalTableValueBody", self)

class ParagraphValue:

    pass
class Documentation_ItemizedListValue(ParagraphValue):

    pass
class Documentation_EmphasisValue(ParagraphValue):

    def __init__(self, value: str, role: str):
        self.value = value
        self.role = role
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def role(self) -> str:
        return self.__role

    @role.setter
    def role(self, role: str):
        self.__role = role

class Documentation_InformalTableValue(ParagraphValue):

    pass
class Documentation_XRefValue(ParagraphValue):

    pass
class Documentation_TextualValue(ParagraphValue):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class Documentation_ParagraphValue(ABC):

    pass
class Documentation_Paragraph:

    pass
class Documentation_Section:

    def __init__(self, title: str, Documentation_Section: "Documentation_Book" = None, Documentation_Section4: "Documentation_Section" = None, Documentation_Section2: set["Documentation_Section"] = None, Documentation_Section6: set["Documentation_Paragraph"] = None, Documentation_Section10: "Documentation_XRefValue" = None):
        self.title = title
        self.Documentation_Section = Documentation_Section
        self.Documentation_Section4 = Documentation_Section4
        self.Documentation_Section2 = Documentation_Section2 if Documentation_Section2 is not None else set()
        self.Documentation_Section6 = Documentation_Section6 if Documentation_Section6 is not None else set()
        self.Documentation_Section10 = Documentation_Section10
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def Documentation_Section(self):
        return self.__Documentation_Section

    @Documentation_Section.setter
    def Documentation_Section(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Documentation_Section__Documentation_Section", None)
        self.__Documentation_Section = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Documentation_Book"):
                opp_val = getattr(old_value, "Documentation_Book", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Documentation_Book"):
                opp_val = getattr(value, "Documentation_Book", None)
                if opp_val is None:
                    setattr(value, "Documentation_Book", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Documentation_Section10(self):
        return self.__Documentation_Section10

    @Documentation_Section10.setter
    def Documentation_Section10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Documentation_Section__Documentation_Section10", None)
        self.__Documentation_Section10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Documentation_XRefValue"):
                opp_val = getattr(old_value, "Documentation_XRefValue", None)
                if opp_val == self:
                    setattr(old_value, "Documentation_XRefValue", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Documentation_XRefValue"):
                opp_val = getattr(value, "Documentation_XRefValue", None)
                setattr(value, "Documentation_XRefValue", self)

    @property
    def Documentation_Section4(self):
        return self.__Documentation_Section4

    @Documentation_Section4.setter
    def Documentation_Section4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Documentation_Section__Documentation_Section4", None)
        self.__Documentation_Section4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Documentation_Section2"):
                opp_val = getattr(old_value, "Documentation_Section2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Documentation_Section2"):
                opp_val = getattr(value, "Documentation_Section2", None)
                if opp_val is None:
                    setattr(value, "Documentation_Section2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Documentation_Section2(self):
        return self.__Documentation_Section2

    @Documentation_Section2.setter
    def Documentation_Section2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Documentation_Section__Documentation_Section2", None)
        self.__Documentation_Section2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Documentation_Section4"):
                    opp_val = getattr(item, "Documentation_Section4", None)
                    
                    if opp_val == self:
                        setattr(item, "Documentation_Section4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Documentation_Section4"):
                    opp_val = getattr(item, "Documentation_Section4", None)
                    
                    setattr(item, "Documentation_Section4", self)
                    

    @property
    def Documentation_Section6(self):
        return self.__Documentation_Section6

    @Documentation_Section6.setter
    def Documentation_Section6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Documentation_Section__Documentation_Section6", None)
        self.__Documentation_Section6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Documentation_Paragraph7"):
                    opp_val = getattr(item, "Documentation_Paragraph7", None)
                    
                    if opp_val == self:
                        setattr(item, "Documentation_Paragraph7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Documentation_Paragraph7"):
                    opp_val = getattr(item, "Documentation_Paragraph7", None)
                    
                    setattr(item, "Documentation_Paragraph7", self)
                    

class Paragraph:

    pass
class Documentation_ItemizedListValueItem(Paragraph):

    pass
class Documentation_Book:

    def __init__(self, title: str, Documentation_Book: set["Documentation_Section"] = None):
        self.title = title
        self.Documentation_Book = Documentation_Book if Documentation_Book is not None else set()
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def Documentation_Book(self):
        return self.__Documentation_Book

    @Documentation_Book.setter
    def Documentation_Book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Documentation_Book__Documentation_Book", None)
        self.__Documentation_Book = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Documentation_Section"):
                    opp_val = getattr(item, "Documentation_Section", None)
                    
                    if opp_val == self:
                        setattr(item, "Documentation_Section", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Documentation_Section"):
                    opp_val = getattr(item, "Documentation_Section", None)
                    
                    setattr(item, "Documentation_Section", self)
                    
