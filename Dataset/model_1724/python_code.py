from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class mapkey_Writer:

    def __init__(self, name: str, mapkey_Writer: "mapkey_StringToWriterMapEntry" = None):
        self.name = name
        self.mapkey_Writer = mapkey_Writer
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mapkey_Writer(self):
        return self.__mapkey_Writer

    @mapkey_Writer.setter
    def mapkey_Writer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mapkey_Writer__mapkey_Writer", None)
        self.__mapkey_Writer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mapkey_StringToWriterMapEntry2"):
                opp_val = getattr(old_value, "mapkey_StringToWriterMapEntry2", None)
                if opp_val == self:
                    setattr(old_value, "mapkey_StringToWriterMapEntry2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mapkey_StringToWriterMapEntry2"):
                opp_val = getattr(value, "mapkey_StringToWriterMapEntry2", None)
                setattr(value, "mapkey_StringToWriterMapEntry2", self)

class mapkey_Book:

    def __init__(self, title: str, mapkey_Book: set["mapkey_StringToWriterMapEntry"] = None):
        self.title = title
        self.mapkey_Book = mapkey_Book if mapkey_Book is not None else set()
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def mapkey_Book(self):
        return self.__mapkey_Book

    @mapkey_Book.setter
    def mapkey_Book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mapkey_Book__mapkey_Book", None)
        self.__mapkey_Book = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mapkey_StringToWriterMapEntry"):
                    opp_val = getattr(item, "mapkey_StringToWriterMapEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "mapkey_StringToWriterMapEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mapkey_StringToWriterMapEntry"):
                    opp_val = getattr(item, "mapkey_StringToWriterMapEntry", None)
                    
                    setattr(item, "mapkey_StringToWriterMapEntry", self)
                    

class mapkey_StringToWriterMapEntry:

    def __init__(self, key: str, mapkey_StringToWriterMapEntry: "mapkey_Book" = None, mapkey_StringToWriterMapEntry2: "mapkey_Writer" = None):
        self.key = key
        self.mapkey_StringToWriterMapEntry = mapkey_StringToWriterMapEntry
        self.mapkey_StringToWriterMapEntry2 = mapkey_StringToWriterMapEntry2
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def mapkey_StringToWriterMapEntry2(self):
        return self.__mapkey_StringToWriterMapEntry2

    @mapkey_StringToWriterMapEntry2.setter
    def mapkey_StringToWriterMapEntry2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mapkey_StringToWriterMapEntry__mapkey_StringToWriterMapEntry2", None)
        self.__mapkey_StringToWriterMapEntry2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mapkey_Writer"):
                opp_val = getattr(old_value, "mapkey_Writer", None)
                if opp_val == self:
                    setattr(old_value, "mapkey_Writer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mapkey_Writer"):
                opp_val = getattr(value, "mapkey_Writer", None)
                setattr(value, "mapkey_Writer", self)

    @property
    def mapkey_StringToWriterMapEntry(self):
        return self.__mapkey_StringToWriterMapEntry

    @mapkey_StringToWriterMapEntry.setter
    def mapkey_StringToWriterMapEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mapkey_StringToWriterMapEntry__mapkey_StringToWriterMapEntry", None)
        self.__mapkey_StringToWriterMapEntry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mapkey_Book"):
                opp_val = getattr(old_value, "mapkey_Book", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mapkey_Book"):
                opp_val = getattr(value, "mapkey_Book", None)
                if opp_val is None:
                    setattr(value, "mapkey_Book", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
