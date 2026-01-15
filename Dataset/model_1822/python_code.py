from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class TextualValue:

    pass
class Documentation_InformalTableValueRow:

    pass
class Documentation_ParagraphValue(ABC):

    pass
class Documentation_Paragraph:

    pass
class Documentation_Section:

    def __init__(self, title: str, Documentation_Section4: "Documentation_Section" = None, Documentation_Section2: set["Documentation_Section"] = None, Documentation_Section6: set["Documentation_Paragraph"] = None, Documentation_Section: "Documentation_Book" = None, Documentation_Section10: "Documentation_XRefValue" = None):
        self.title = title
        self.Documentation_Section4 = Documentation_Section4
        self.Documentation_Section2 = Documentation_Section2 if Documentation_Section2 is not None else set()
        self.Documentation_Section6 = Documentation_Section6 if Documentation_Section6 is not None else set()
        self.Documentation_Section = Documentation_Section
        self.Documentation_Section10 = Documentation_Section10
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

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

class Paragraph:

    pass
class Documentation_ItemizedListValueItem(Paragraph):

    pass
class ParagraphValue:

    pass
class Documentation_ItemizedListValue(ParagraphValue):

    pass
class Documentation_EmphasisValue(TextualValue, ParagraphValue):

    def __init__(self, role: str):
        self.role = role
        
    @property
    def role(self) -> str:
        return self.__role

    @role.setter
    def role(self, role: str):
        self.__role = role

class Documentation_XRefValue(ParagraphValue):

    pass
class Documentation_InformalTableValue(ParagraphValue):

    def __init__(self, cols: int, Documentation_InformalTableValue: set["Documentation_InformalTableValueRow"] = None, Documentation_InformalTableValue13: set["Documentation_InformalTableValueRow"] = None):
        self.cols = cols
        self.Documentation_InformalTableValue = Documentation_InformalTableValue if Documentation_InformalTableValue is not None else set()
        self.Documentation_InformalTableValue13 = Documentation_InformalTableValue13 if Documentation_InformalTableValue13 is not None else set()
        
    @property
    def cols(self) -> int:
        return self.__cols

    @cols.setter
    def cols(self, cols: int):
        self.__cols = cols

    @property
    def Documentation_InformalTableValue(self):
        return self.__Documentation_InformalTableValue

    @Documentation_InformalTableValue.setter
    def Documentation_InformalTableValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Documentation_InformalTableValue__Documentation_InformalTableValue", None)
        self.__Documentation_InformalTableValue = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Documentation_InformalTableValueRow"):
                    opp_val = getattr(item, "Documentation_InformalTableValueRow", None)
                    
                    if opp_val == self:
                        setattr(item, "Documentation_InformalTableValueRow", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Documentation_InformalTableValueRow"):
                    opp_val = getattr(item, "Documentation_InformalTableValueRow", None)
                    
                    setattr(item, "Documentation_InformalTableValueRow", self)
                    

    @property
    def Documentation_InformalTableValue13(self):
        return self.__Documentation_InformalTableValue13

    @Documentation_InformalTableValue13.setter
    def Documentation_InformalTableValue13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Documentation_InformalTableValue__Documentation_InformalTableValue13", None)
        self.__Documentation_InformalTableValue13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Documentation_InformalTableValueRow14"):
                    opp_val = getattr(item, "Documentation_InformalTableValueRow14", None)
                    
                    if opp_val == self:
                        setattr(item, "Documentation_InformalTableValueRow14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Documentation_InformalTableValueRow14"):
                    opp_val = getattr(item, "Documentation_InformalTableValueRow14", None)
                    
                    setattr(item, "Documentation_InformalTableValueRow14", self)
                    

class Documentation_TextualValue(ParagraphValue):

    def __init__(self, value: str, Documentation_TextualValue: "Documentation_InformalTableValueRow" = None):
        self.value = value
        self.Documentation_TextualValue = Documentation_TextualValue
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def Documentation_TextualValue(self):
        return self.__Documentation_TextualValue

    @Documentation_TextualValue.setter
    def Documentation_TextualValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Documentation_TextualValue__Documentation_TextualValue", None)
        self.__Documentation_TextualValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Documentation_InformalTableValueRow16"):
                opp_val = getattr(old_value, "Documentation_InformalTableValueRow16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Documentation_InformalTableValueRow16"):
                opp_val = getattr(value, "Documentation_InformalTableValueRow16", None)
                if opp_val is None:
                    setattr(value, "Documentation_InformalTableValueRow16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
                    
