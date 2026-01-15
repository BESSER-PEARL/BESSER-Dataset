from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Category(Enum):
    Complex = "Complex"
    Simple = "Simple"


############################################
# Definition of Classes
############################################

class emap_Writer:

    def __init__(self, name: str, emap_Writer11: "emap_WriterToStringMapEntry" = None, emap_Writer: "emap_StringToWriterMapEntry" = None):
        self.name = name
        self.emap_Writer11 = emap_Writer11
        self.emap_Writer = emap_Writer
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def emap_Writer(self):
        return self.__emap_Writer

    @emap_Writer.setter
    def emap_Writer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emap_Writer__emap_Writer", None)
        self.__emap_Writer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "emap_StringToWriterMapEntry8"):
                opp_val = getattr(old_value, "emap_StringToWriterMapEntry8", None)
                if opp_val == self:
                    setattr(old_value, "emap_StringToWriterMapEntry8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "emap_StringToWriterMapEntry8"):
                opp_val = getattr(value, "emap_StringToWriterMapEntry8", None)
                setattr(value, "emap_StringToWriterMapEntry8", self)

    @property
    def emap_Writer11(self):
        return self.__emap_Writer11

    @emap_Writer11.setter
    def emap_Writer11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emap_Writer__emap_Writer11", None)
        self.__emap_Writer11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "emap_WriterToStringMapEntry10"):
                opp_val = getattr(old_value, "emap_WriterToStringMapEntry10", None)
                if opp_val == self:
                    setattr(old_value, "emap_WriterToStringMapEntry10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "emap_WriterToStringMapEntry10"):
                opp_val = getattr(value, "emap_WriterToStringMapEntry10", None)
                setattr(value, "emap_WriterToStringMapEntry10", self)

class emap_DateToCategoryMapEntry:

    def __init__(self, key: str, value: str, emap_DateToCategoryMapEntry: "emap_Book" = None):
        self.key = key
        self.value = value
        self.emap_DateToCategoryMapEntry = emap_DateToCategoryMapEntry
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def emap_DateToCategoryMapEntry(self):
        return self.__emap_DateToCategoryMapEntry

    @emap_DateToCategoryMapEntry.setter
    def emap_DateToCategoryMapEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emap_DateToCategoryMapEntry__emap_DateToCategoryMapEntry", None)
        self.__emap_DateToCategoryMapEntry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "emap_Book6"):
                opp_val = getattr(old_value, "emap_Book6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "emap_Book6"):
                opp_val = getattr(value, "emap_Book6", None)
                if opp_val is None:
                    setattr(value, "emap_Book6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class emap_WriterToStringMapEntry:

    def __init__(self, value: str, emap_WriterToStringMapEntry: "emap_Book" = None, emap_WriterToStringMapEntry10: "emap_Writer" = None):
        self.value = value
        self.emap_WriterToStringMapEntry = emap_WriterToStringMapEntry
        self.emap_WriterToStringMapEntry10 = emap_WriterToStringMapEntry10
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def emap_WriterToStringMapEntry10(self):
        return self.__emap_WriterToStringMapEntry10

    @emap_WriterToStringMapEntry10.setter
    def emap_WriterToStringMapEntry10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emap_WriterToStringMapEntry__emap_WriterToStringMapEntry10", None)
        self.__emap_WriterToStringMapEntry10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "emap_Writer11"):
                opp_val = getattr(old_value, "emap_Writer11", None)
                if opp_val == self:
                    setattr(old_value, "emap_Writer11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "emap_Writer11"):
                opp_val = getattr(value, "emap_Writer11", None)
                setattr(value, "emap_Writer11", self)

    @property
    def emap_WriterToStringMapEntry(self):
        return self.__emap_WriterToStringMapEntry

    @emap_WriterToStringMapEntry.setter
    def emap_WriterToStringMapEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emap_WriterToStringMapEntry__emap_WriterToStringMapEntry", None)
        self.__emap_WriterToStringMapEntry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "emap_Book4"):
                opp_val = getattr(old_value, "emap_Book4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "emap_Book4"):
                opp_val = getattr(value, "emap_Book4", None)
                if opp_val is None:
                    setattr(value, "emap_Book4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class emap_StringToStringMapEntry:

    def __init__(self, key: str, value: str, emap_StringToStringMapEntry: "emap_Book" = None):
        self.key = key
        self.value = value
        self.emap_StringToStringMapEntry = emap_StringToStringMapEntry
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def emap_StringToStringMapEntry(self):
        return self.__emap_StringToStringMapEntry

    @emap_StringToStringMapEntry.setter
    def emap_StringToStringMapEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emap_StringToStringMapEntry__emap_StringToStringMapEntry", None)
        self.__emap_StringToStringMapEntry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "emap_Book2"):
                opp_val = getattr(old_value, "emap_Book2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "emap_Book2"):
                opp_val = getattr(value, "emap_Book2", None)
                if opp_val is None:
                    setattr(value, "emap_Book2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class emap_StringToWriterMapEntry:

    def __init__(self, key: str, emap_StringToWriterMapEntry: "emap_Book" = None, emap_StringToWriterMapEntry8: "emap_Writer" = None):
        self.key = key
        self.emap_StringToWriterMapEntry = emap_StringToWriterMapEntry
        self.emap_StringToWriterMapEntry8 = emap_StringToWriterMapEntry8
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def emap_StringToWriterMapEntry8(self):
        return self.__emap_StringToWriterMapEntry8

    @emap_StringToWriterMapEntry8.setter
    def emap_StringToWriterMapEntry8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emap_StringToWriterMapEntry__emap_StringToWriterMapEntry8", None)
        self.__emap_StringToWriterMapEntry8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "emap_Writer"):
                opp_val = getattr(old_value, "emap_Writer", None)
                if opp_val == self:
                    setattr(old_value, "emap_Writer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "emap_Writer"):
                opp_val = getattr(value, "emap_Writer", None)
                setattr(value, "emap_Writer", self)

    @property
    def emap_StringToWriterMapEntry(self):
        return self.__emap_StringToWriterMapEntry

    @emap_StringToWriterMapEntry.setter
    def emap_StringToWriterMapEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emap_StringToWriterMapEntry__emap_StringToWriterMapEntry", None)
        self.__emap_StringToWriterMapEntry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "emap_Book"):
                opp_val = getattr(old_value, "emap_Book", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "emap_Book"):
                opp_val = getattr(value, "emap_Book", None)
                if opp_val is None:
                    setattr(value, "emap_Book", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class emap_Book:

    def __init__(self, title: str, emap_Book: set["emap_StringToWriterMapEntry"] = None, emap_Book2: set["emap_StringToStringMapEntry"] = None, emap_Book4: set["emap_WriterToStringMapEntry"] = None, emap_Book6: set["emap_DateToCategoryMapEntry"] = None):
        self.title = title
        self.emap_Book = emap_Book if emap_Book is not None else set()
        self.emap_Book2 = emap_Book2 if emap_Book2 is not None else set()
        self.emap_Book4 = emap_Book4 if emap_Book4 is not None else set()
        self.emap_Book6 = emap_Book6 if emap_Book6 is not None else set()
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def emap_Book6(self):
        return self.__emap_Book6

    @emap_Book6.setter
    def emap_Book6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emap_Book__emap_Book6", None)
        self.__emap_Book6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "emap_DateToCategoryMapEntry"):
                    opp_val = getattr(item, "emap_DateToCategoryMapEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "emap_DateToCategoryMapEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "emap_DateToCategoryMapEntry"):
                    opp_val = getattr(item, "emap_DateToCategoryMapEntry", None)
                    
                    setattr(item, "emap_DateToCategoryMapEntry", self)
                    

    @property
    def emap_Book4(self):
        return self.__emap_Book4

    @emap_Book4.setter
    def emap_Book4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emap_Book__emap_Book4", None)
        self.__emap_Book4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "emap_WriterToStringMapEntry"):
                    opp_val = getattr(item, "emap_WriterToStringMapEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "emap_WriterToStringMapEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "emap_WriterToStringMapEntry"):
                    opp_val = getattr(item, "emap_WriterToStringMapEntry", None)
                    
                    setattr(item, "emap_WriterToStringMapEntry", self)
                    

    @property
    def emap_Book2(self):
        return self.__emap_Book2

    @emap_Book2.setter
    def emap_Book2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emap_Book__emap_Book2", None)
        self.__emap_Book2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "emap_StringToStringMapEntry"):
                    opp_val = getattr(item, "emap_StringToStringMapEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "emap_StringToStringMapEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "emap_StringToStringMapEntry"):
                    opp_val = getattr(item, "emap_StringToStringMapEntry", None)
                    
                    setattr(item, "emap_StringToStringMapEntry", self)
                    

    @property
    def emap_Book(self):
        return self.__emap_Book

    @emap_Book.setter
    def emap_Book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emap_Book__emap_Book", None)
        self.__emap_Book = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "emap_StringToWriterMapEntry"):
                    opp_val = getattr(item, "emap_StringToWriterMapEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "emap_StringToWriterMapEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "emap_StringToWriterMapEntry"):
                    opp_val = getattr(item, "emap_StringToWriterMapEntry", None)
                    
                    setattr(item, "emap_StringToWriterMapEntry", self)
                    
