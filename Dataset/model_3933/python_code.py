from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Entry:

    pass
class document_BasicEntry(Entry):

    pass
class document_FullEntry(Entry):

    pass
class document_Entry(ABC):

    def __init__(self, isBold: bool, isItalic: bool, text: str, document_Entry: "document_Table" = None):
        self.isBold = isBold
        self.isItalic = isItalic
        self.text = text
        self.document_Entry = document_Entry
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def isBold(self) -> bool:
        return self.__isBold

    @isBold.setter
    def isBold(self, isBold: bool):
        self.__isBold = isBold

    @property
    def isItalic(self) -> bool:
        return self.__isItalic

    @isItalic.setter
    def isItalic(self, isItalic: bool):
        self.__isItalic = isItalic

    @property
    def document_Entry(self):
        return self.__document_Entry

    @document_Entry.setter
    def document_Entry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_document_Entry__document_Entry", None)
        self.__document_Entry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "document_Table4"):
                opp_val = getattr(old_value, "document_Table4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "document_Table4"):
                opp_val = getattr(value, "document_Table4", None)
                if opp_val is None:
                    setattr(value, "document_Table4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class document_Table:

    pass
class document_Section:

    pass
class document_Chapter:

    pass