from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class hbmapkeys_Writer:

    def __init__(self, name: str, hbmapkeys_Writer: "hbmapkeys_City" = None, hbmapkeys_Writer9: "hbmapkeys_WriterToCityMapEntry" = None, hbmapkeys_Writer6: "hbmapkeys_StringToWriterMapEntry" = None):
        self.name = name
        self.hbmapkeys_Writer = hbmapkeys_Writer
        self.hbmapkeys_Writer9 = hbmapkeys_Writer9
        self.hbmapkeys_Writer6 = hbmapkeys_Writer6
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def hbmapkeys_Writer6(self):
        return self.__hbmapkeys_Writer6

    @hbmapkeys_Writer6.setter
    def hbmapkeys_Writer6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hbmapkeys_Writer__hbmapkeys_Writer6", None)
        self.__hbmapkeys_Writer6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hbmapkeys_StringToWriterMapEntry5"):
                opp_val = getattr(old_value, "hbmapkeys_StringToWriterMapEntry5", None)
                if opp_val == self:
                    setattr(old_value, "hbmapkeys_StringToWriterMapEntry5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hbmapkeys_StringToWriterMapEntry5"):
                opp_val = getattr(value, "hbmapkeys_StringToWriterMapEntry5", None)
                setattr(value, "hbmapkeys_StringToWriterMapEntry5", self)

    @property
    def hbmapkeys_Writer9(self):
        return self.__hbmapkeys_Writer9

    @hbmapkeys_Writer9.setter
    def hbmapkeys_Writer9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hbmapkeys_Writer__hbmapkeys_Writer9", None)
        self.__hbmapkeys_Writer9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hbmapkeys_WriterToCityMapEntry8"):
                opp_val = getattr(old_value, "hbmapkeys_WriterToCityMapEntry8", None)
                if opp_val == self:
                    setattr(old_value, "hbmapkeys_WriterToCityMapEntry8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hbmapkeys_WriterToCityMapEntry8"):
                opp_val = getattr(value, "hbmapkeys_WriterToCityMapEntry8", None)
                setattr(value, "hbmapkeys_WriterToCityMapEntry8", self)

    @property
    def hbmapkeys_Writer(self):
        return self.__hbmapkeys_Writer

    @hbmapkeys_Writer.setter
    def hbmapkeys_Writer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hbmapkeys_Writer__hbmapkeys_Writer", None)
        self.__hbmapkeys_Writer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hbmapkeys_City"):
                opp_val = getattr(old_value, "hbmapkeys_City", None)
                if opp_val == self:
                    setattr(old_value, "hbmapkeys_City", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hbmapkeys_City"):
                opp_val = getattr(value, "hbmapkeys_City", None)
                setattr(value, "hbmapkeys_City", self)

class hbmapkeys_City:

    def __init__(self, name: str, hbmapkeys_City: "hbmapkeys_Writer" = None, hbmapkeys_City12: "hbmapkeys_WriterToCityMapEntry" = None):
        self.name = name
        self.hbmapkeys_City = hbmapkeys_City
        self.hbmapkeys_City12 = hbmapkeys_City12
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def hbmapkeys_City(self):
        return self.__hbmapkeys_City

    @hbmapkeys_City.setter
    def hbmapkeys_City(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hbmapkeys_City__hbmapkeys_City", None)
        self.__hbmapkeys_City = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hbmapkeys_Writer"):
                opp_val = getattr(old_value, "hbmapkeys_Writer", None)
                if opp_val == self:
                    setattr(old_value, "hbmapkeys_Writer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hbmapkeys_Writer"):
                opp_val = getattr(value, "hbmapkeys_Writer", None)
                setattr(value, "hbmapkeys_Writer", self)

    @property
    def hbmapkeys_City12(self):
        return self.__hbmapkeys_City12

    @hbmapkeys_City12.setter
    def hbmapkeys_City12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hbmapkeys_City__hbmapkeys_City12", None)
        self.__hbmapkeys_City12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hbmapkeys_WriterToCityMapEntry11"):
                opp_val = getattr(old_value, "hbmapkeys_WriterToCityMapEntry11", None)
                if opp_val == self:
                    setattr(old_value, "hbmapkeys_WriterToCityMapEntry11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hbmapkeys_WriterToCityMapEntry11"):
                opp_val = getattr(value, "hbmapkeys_WriterToCityMapEntry11", None)
                setattr(value, "hbmapkeys_WriterToCityMapEntry11", self)

class hbmapkeys_WriterToCityMapEntry:

    pass
class hbmapkeys_StringToWriterMapEntry:

    def __init__(self, key: str, hbmapkeys_StringToWriterMapEntry: "hbmapkeys_Book" = None, hbmapkeys_StringToWriterMapEntry5: "hbmapkeys_Writer" = None):
        self.key = key
        self.hbmapkeys_StringToWriterMapEntry = hbmapkeys_StringToWriterMapEntry
        self.hbmapkeys_StringToWriterMapEntry5 = hbmapkeys_StringToWriterMapEntry5
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def hbmapkeys_StringToWriterMapEntry5(self):
        return self.__hbmapkeys_StringToWriterMapEntry5

    @hbmapkeys_StringToWriterMapEntry5.setter
    def hbmapkeys_StringToWriterMapEntry5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hbmapkeys_StringToWriterMapEntry__hbmapkeys_StringToWriterMapEntry5", None)
        self.__hbmapkeys_StringToWriterMapEntry5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hbmapkeys_Writer6"):
                opp_val = getattr(old_value, "hbmapkeys_Writer6", None)
                if opp_val == self:
                    setattr(old_value, "hbmapkeys_Writer6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hbmapkeys_Writer6"):
                opp_val = getattr(value, "hbmapkeys_Writer6", None)
                setattr(value, "hbmapkeys_Writer6", self)

    @property
    def hbmapkeys_StringToWriterMapEntry(self):
        return self.__hbmapkeys_StringToWriterMapEntry

    @hbmapkeys_StringToWriterMapEntry.setter
    def hbmapkeys_StringToWriterMapEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hbmapkeys_StringToWriterMapEntry__hbmapkeys_StringToWriterMapEntry", None)
        self.__hbmapkeys_StringToWriterMapEntry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hbmapkeys_Book"):
                opp_val = getattr(old_value, "hbmapkeys_Book", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hbmapkeys_Book"):
                opp_val = getattr(value, "hbmapkeys_Book", None)
                if opp_val is None:
                    setattr(value, "hbmapkeys_Book", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class hbmapkeys_Book:

    def __init__(self, title: str, hbmapkeys_Book: set["hbmapkeys_StringToWriterMapEntry"] = None, hbmapkeys_Book2: set["hbmapkeys_WriterToCityMapEntry"] = None):
        self.title = title
        self.hbmapkeys_Book = hbmapkeys_Book if hbmapkeys_Book is not None else set()
        self.hbmapkeys_Book2 = hbmapkeys_Book2 if hbmapkeys_Book2 is not None else set()
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def hbmapkeys_Book(self):
        return self.__hbmapkeys_Book

    @hbmapkeys_Book.setter
    def hbmapkeys_Book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hbmapkeys_Book__hbmapkeys_Book", None)
        self.__hbmapkeys_Book = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "hbmapkeys_StringToWriterMapEntry"):
                    opp_val = getattr(item, "hbmapkeys_StringToWriterMapEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "hbmapkeys_StringToWriterMapEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "hbmapkeys_StringToWriterMapEntry"):
                    opp_val = getattr(item, "hbmapkeys_StringToWriterMapEntry", None)
                    
                    setattr(item, "hbmapkeys_StringToWriterMapEntry", self)
                    

    @property
    def hbmapkeys_Book2(self):
        return self.__hbmapkeys_Book2

    @hbmapkeys_Book2.setter
    def hbmapkeys_Book2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hbmapkeys_Book__hbmapkeys_Book2", None)
        self.__hbmapkeys_Book2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "hbmapkeys_WriterToCityMapEntry"):
                    opp_val = getattr(item, "hbmapkeys_WriterToCityMapEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "hbmapkeys_WriterToCityMapEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "hbmapkeys_WriterToCityMapEntry"):
                    opp_val = getattr(item, "hbmapkeys_WriterToCityMapEntry", None)
                    
                    setattr(item, "hbmapkeys_WriterToCityMapEntry", self)
                    
