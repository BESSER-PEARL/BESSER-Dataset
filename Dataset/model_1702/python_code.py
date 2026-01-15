from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class emapsample_WriterToBookMapEntry:

    pass
class Identifiable:

    pass
class emapsample_Writer(Identifiable):

    def __init__(self, name: str, emapsample_Writer10: "emapsample_WriterToBookMapEntry" = None, emapsample_Writer: "emapsample_StringToWriterMapEntry" = None, emapsample_Writer16: "emapsample_WriterToNameMapEntry" = None):
        self.name = name
        self.emapsample_Writer10 = emapsample_Writer10
        self.emapsample_Writer = emapsample_Writer
        self.emapsample_Writer16 = emapsample_Writer16
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def emapsample_Writer(self):
        return self.__emapsample_Writer

    @emapsample_Writer.setter
    def emapsample_Writer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emapsample_Writer__emapsample_Writer", None)
        self.__emapsample_Writer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "emapsample_StringToWriterMapEntry7"):
                opp_val = getattr(old_value, "emapsample_StringToWriterMapEntry7", None)
                if opp_val == self:
                    setattr(old_value, "emapsample_StringToWriterMapEntry7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "emapsample_StringToWriterMapEntry7"):
                opp_val = getattr(value, "emapsample_StringToWriterMapEntry7", None)
                setattr(value, "emapsample_StringToWriterMapEntry7", self)

    @property
    def emapsample_Writer10(self):
        return self.__emapsample_Writer10

    @emapsample_Writer10.setter
    def emapsample_Writer10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emapsample_Writer__emapsample_Writer10", None)
        self.__emapsample_Writer10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "emapsample_WriterToBookMapEntry9"):
                opp_val = getattr(old_value, "emapsample_WriterToBookMapEntry9", None)
                if opp_val == self:
                    setattr(old_value, "emapsample_WriterToBookMapEntry9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "emapsample_WriterToBookMapEntry9"):
                opp_val = getattr(value, "emapsample_WriterToBookMapEntry9", None)
                setattr(value, "emapsample_WriterToBookMapEntry9", self)

    @property
    def emapsample_Writer16(self):
        return self.__emapsample_Writer16

    @emapsample_Writer16.setter
    def emapsample_Writer16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emapsample_Writer__emapsample_Writer16", None)
        self.__emapsample_Writer16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "emapsample_WriterToNameMapEntry15"):
                opp_val = getattr(old_value, "emapsample_WriterToNameMapEntry15", None)
                if opp_val == self:
                    setattr(old_value, "emapsample_WriterToNameMapEntry15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "emapsample_WriterToNameMapEntry15"):
                opp_val = getattr(value, "emapsample_WriterToNameMapEntry15", None)
                setattr(value, "emapsample_WriterToNameMapEntry15", self)

class emapsample_BookStore(Identifiable):

    def __init__(self, name: str, emapsample_BookStore: set["emapsample_WriterToBookMapEntry"] = None, emapsample_BookStore3: set["emapsample_EStringToStringMapEntry"] = None, emapsample_BookStore5: set["emapsample_WriterToNameMapEntry"] = None):
        self.name = name
        self.emapsample_BookStore = emapsample_BookStore if emapsample_BookStore is not None else set()
        self.emapsample_BookStore3 = emapsample_BookStore3 if emapsample_BookStore3 is not None else set()
        self.emapsample_BookStore5 = emapsample_BookStore5 if emapsample_BookStore5 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def emapsample_BookStore3(self):
        return self.__emapsample_BookStore3

    @emapsample_BookStore3.setter
    def emapsample_BookStore3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emapsample_BookStore__emapsample_BookStore3", None)
        self.__emapsample_BookStore3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "emapsample_EStringToStringMapEntry"):
                    opp_val = getattr(item, "emapsample_EStringToStringMapEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "emapsample_EStringToStringMapEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "emapsample_EStringToStringMapEntry"):
                    opp_val = getattr(item, "emapsample_EStringToStringMapEntry", None)
                    
                    setattr(item, "emapsample_EStringToStringMapEntry", self)
                    

    @property
    def emapsample_BookStore(self):
        return self.__emapsample_BookStore

    @emapsample_BookStore.setter
    def emapsample_BookStore(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emapsample_BookStore__emapsample_BookStore", None)
        self.__emapsample_BookStore = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "emapsample_WriterToBookMapEntry"):
                    opp_val = getattr(item, "emapsample_WriterToBookMapEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "emapsample_WriterToBookMapEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "emapsample_WriterToBookMapEntry"):
                    opp_val = getattr(item, "emapsample_WriterToBookMapEntry", None)
                    
                    setattr(item, "emapsample_WriterToBookMapEntry", self)
                    

    @property
    def emapsample_BookStore5(self):
        return self.__emapsample_BookStore5

    @emapsample_BookStore5.setter
    def emapsample_BookStore5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emapsample_BookStore__emapsample_BookStore5", None)
        self.__emapsample_BookStore5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "emapsample_WriterToNameMapEntry"):
                    opp_val = getattr(item, "emapsample_WriterToNameMapEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "emapsample_WriterToNameMapEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "emapsample_WriterToNameMapEntry"):
                    opp_val = getattr(item, "emapsample_WriterToNameMapEntry", None)
                    
                    setattr(item, "emapsample_WriterToNameMapEntry", self)
                    

class emapsample_StringToWriterMapEntry:

    def __init__(self, key: str, emapsample_StringToWriterMapEntry: "emapsample_Book" = None, emapsample_StringToWriterMapEntry7: "emapsample_Writer" = None):
        self.key = key
        self.emapsample_StringToWriterMapEntry = emapsample_StringToWriterMapEntry
        self.emapsample_StringToWriterMapEntry7 = emapsample_StringToWriterMapEntry7
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def emapsample_StringToWriterMapEntry(self):
        return self.__emapsample_StringToWriterMapEntry

    @emapsample_StringToWriterMapEntry.setter
    def emapsample_StringToWriterMapEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emapsample_StringToWriterMapEntry__emapsample_StringToWriterMapEntry", None)
        self.__emapsample_StringToWriterMapEntry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "emapsample_Book"):
                opp_val = getattr(old_value, "emapsample_Book", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "emapsample_Book"):
                opp_val = getattr(value, "emapsample_Book", None)
                if opp_val is None:
                    setattr(value, "emapsample_Book", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def emapsample_StringToWriterMapEntry7(self):
        return self.__emapsample_StringToWriterMapEntry7

    @emapsample_StringToWriterMapEntry7.setter
    def emapsample_StringToWriterMapEntry7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emapsample_StringToWriterMapEntry__emapsample_StringToWriterMapEntry7", None)
        self.__emapsample_StringToWriterMapEntry7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "emapsample_Writer"):
                opp_val = getattr(old_value, "emapsample_Writer", None)
                if opp_val == self:
                    setattr(old_value, "emapsample_Writer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "emapsample_Writer"):
                opp_val = getattr(value, "emapsample_Writer", None)
                setattr(value, "emapsample_Writer", self)

class emapsample_WriterToNameMapEntry:

    def __init__(self, value: str, emapsample_WriterToNameMapEntry: "emapsample_BookStore" = None, emapsample_WriterToNameMapEntry15: "emapsample_Writer" = None):
        self.value = value
        self.emapsample_WriterToNameMapEntry = emapsample_WriterToNameMapEntry
        self.emapsample_WriterToNameMapEntry15 = emapsample_WriterToNameMapEntry15
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def emapsample_WriterToNameMapEntry15(self):
        return self.__emapsample_WriterToNameMapEntry15

    @emapsample_WriterToNameMapEntry15.setter
    def emapsample_WriterToNameMapEntry15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emapsample_WriterToNameMapEntry__emapsample_WriterToNameMapEntry15", None)
        self.__emapsample_WriterToNameMapEntry15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "emapsample_Writer16"):
                opp_val = getattr(old_value, "emapsample_Writer16", None)
                if opp_val == self:
                    setattr(old_value, "emapsample_Writer16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "emapsample_Writer16"):
                opp_val = getattr(value, "emapsample_Writer16", None)
                setattr(value, "emapsample_Writer16", self)

    @property
    def emapsample_WriterToNameMapEntry(self):
        return self.__emapsample_WriterToNameMapEntry

    @emapsample_WriterToNameMapEntry.setter
    def emapsample_WriterToNameMapEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emapsample_WriterToNameMapEntry__emapsample_WriterToNameMapEntry", None)
        self.__emapsample_WriterToNameMapEntry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "emapsample_BookStore5"):
                opp_val = getattr(old_value, "emapsample_BookStore5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "emapsample_BookStore5"):
                opp_val = getattr(value, "emapsample_BookStore5", None)
                if opp_val is None:
                    setattr(value, "emapsample_BookStore5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class emapsample_EStringToStringMapEntry:

    pass
class emapsample_Book:

    def __init__(self, title: str, emapsample_Book: set["emapsample_StringToWriterMapEntry"] = None, emapsample_Book13: "emapsample_WriterToBookMapEntry" = None):
        self.title = title
        self.emapsample_Book = emapsample_Book if emapsample_Book is not None else set()
        self.emapsample_Book13 = emapsample_Book13
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def emapsample_Book(self):
        return self.__emapsample_Book

    @emapsample_Book.setter
    def emapsample_Book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emapsample_Book__emapsample_Book", None)
        self.__emapsample_Book = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "emapsample_StringToWriterMapEntry"):
                    opp_val = getattr(item, "emapsample_StringToWriterMapEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "emapsample_StringToWriterMapEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "emapsample_StringToWriterMapEntry"):
                    opp_val = getattr(item, "emapsample_StringToWriterMapEntry", None)
                    
                    setattr(item, "emapsample_StringToWriterMapEntry", self)
                    

    @property
    def emapsample_Book13(self):
        return self.__emapsample_Book13

    @emapsample_Book13.setter
    def emapsample_Book13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emapsample_Book__emapsample_Book13", None)
        self.__emapsample_Book13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "emapsample_WriterToBookMapEntry12"):
                opp_val = getattr(old_value, "emapsample_WriterToBookMapEntry12", None)
                if opp_val == self:
                    setattr(old_value, "emapsample_WriterToBookMapEntry12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "emapsample_WriterToBookMapEntry12"):
                opp_val = getattr(value, "emapsample_WriterToBookMapEntry12", None)
                setattr(value, "emapsample_WriterToBookMapEntry12", self)
