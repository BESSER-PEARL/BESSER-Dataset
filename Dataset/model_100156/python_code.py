from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Type(Enum):
    NULL = "NULL"
    DOUBLE = "DOUBLE"
    STRING = "STRING"
    BOOLEAN = "BOOLEAN"
    DATE = "DATE"
    REGEXPR = "REGEXPR"
    JAVASCRIPT = "JAVASCRIPT"
    TIMESTAMP = "TIMESTAMP"


############################################
# Definition of Classes
############################################

class IValue:

    pass
class mongodb_SubDocument(IValue):

    pass
class mongodb_ValueList(IValue):

    pass
class mongodb_Value(IValue):

    def __init__(self, value: str, type: str):
        self.value = value
        self.type = type
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class mongodb_IValue(ABC):

    def __init__(self, mongodb_IValue: "mongodb_Field" = None, mongodb_IValue8: "mongodb_ValueList" = None):
        self.mongodb_IValue = mongodb_IValue
        self.mongodb_IValue8 = mongodb_IValue8
        
        pass
    @property
    def mongodb_IValue8(self):
        return self.__mongodb_IValue8

    @mongodb_IValue8.setter
    def mongodb_IValue8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mongodb_IValue__mongodb_IValue8", None)
        self.__mongodb_IValue8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mongodb_ValueList"):
                opp_val = getattr(old_value, "mongodb_ValueList", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mongodb_ValueList"):
                opp_val = getattr(value, "mongodb_ValueList", None)
                if opp_val is None:
                    setattr(value, "mongodb_ValueList", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mongodb_IValue(self):
        return self.__mongodb_IValue

    @mongodb_IValue.setter
    def mongodb_IValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mongodb_IValue__mongodb_IValue", None)
        self.__mongodb_IValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mongodb_Field6"):
                opp_val = getattr(old_value, "mongodb_Field6", None)
                if opp_val == self:
                    setattr(old_value, "mongodb_Field6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mongodb_Field6"):
                opp_val = getattr(value, "mongodb_Field6", None)
                setattr(value, "mongodb_Field6", self)

    def getValueList(self) :
        # TODO: Implement getValueList method
        pass

    def getValue(self) :
        # TODO: Implement getValue method
        pass

    def getSubDocument(self):
        # TODO: Implement getSubDocument method
        pass

class mongodb_Document:

    def __init__(self, _id: str, mongodb_Document4: set["mongodb_Field"] = None, mongodb_Document: "mongodb_Collection" = None):
        self._id = _id
        self.mongodb_Document4 = mongodb_Document4 if mongodb_Document4 is not None else set()
        self.mongodb_Document = mongodb_Document
        
        pass
    @property
    def _id(self):
        return self.___id

    @_id.setter
    def _id(self, _id: str):
        self.___id = _id


    @property
    def mongodb_Document(self):
        return self.__mongodb_Document

    @mongodb_Document.setter
    def mongodb_Document(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mongodb_Document__mongodb_Document", None)
        self.__mongodb_Document = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mongodb_Collection2"):
                opp_val = getattr(old_value, "mongodb_Collection2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mongodb_Collection2"):
                opp_val = getattr(value, "mongodb_Collection2", None)
                if opp_val is None:
                    setattr(value, "mongodb_Collection2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mongodb_Document4(self):
        return self.__mongodb_Document4

    @mongodb_Document4.setter
    def mongodb_Document4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mongodb_Document__mongodb_Document4", None)
        self.__mongodb_Document4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mongodb_Field"):
                    opp_val = getattr(item, "mongodb_Field", None)
                    
                    if opp_val == self:
                        setattr(item, "mongodb_Field", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mongodb_Field"):
                    opp_val = getattr(item, "mongodb_Field", None)
                    
                    setattr(item, "mongodb_Field", self)
                    

class mongodb_Collection:

    def __init__(self, name: str, mongodb_Collection: "mongodb_Database" = None, mongodb_Collection2: set["mongodb_Document"] = None):
        self.name = name
        self.mongodb_Collection = mongodb_Collection
        self.mongodb_Collection2 = mongodb_Collection2 if mongodb_Collection2 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def mongodb_Collection2(self):
        return self.__mongodb_Collection2

    @mongodb_Collection2.setter
    def mongodb_Collection2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mongodb_Collection__mongodb_Collection2", None)
        self.__mongodb_Collection2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mongodb_Document"):
                    opp_val = getattr(item, "mongodb_Document", None)
                    
                    if opp_val == self:
                        setattr(item, "mongodb_Document", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mongodb_Document"):
                    opp_val = getattr(item, "mongodb_Document", None)
                    
                    setattr(item, "mongodb_Document", self)
                    

    @property
    def mongodb_Collection(self):
        return self.__mongodb_Collection

    @mongodb_Collection.setter
    def mongodb_Collection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mongodb_Collection__mongodb_Collection", None)
        self.__mongodb_Collection = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mongodb_Database"):
                opp_val = getattr(old_value, "mongodb_Database", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mongodb_Database"):
                opp_val = getattr(value, "mongodb_Database", None)
                if opp_val is None:
                    setattr(value, "mongodb_Database", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class mongodb_Database:

    def __init__(self, name: str, mongodb_Database: set["mongodb_Collection"] = None):
        self.name = name
        self.mongodb_Database = mongodb_Database if mongodb_Database is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def mongodb_Database(self):
        return self.__mongodb_Database

    @mongodb_Database.setter
    def mongodb_Database(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mongodb_Database__mongodb_Database", None)
        self.__mongodb_Database = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mongodb_Collection"):
                    opp_val = getattr(item, "mongodb_Collection", None)
                    
                    if opp_val == self:
                        setattr(item, "mongodb_Collection", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mongodb_Collection"):
                    opp_val = getattr(item, "mongodb_Collection", None)
                    
                    setattr(item, "mongodb_Collection", self)
                    

class mongodb_Field:

    def __init__(self, key: str, mongodb_Field6: "mongodb_IValue" = None, mongodb_Field10: "mongodb_SubDocument" = None, mongodb_Field: "mongodb_Document" = None):
        self.key = key
        self.mongodb_Field6 = mongodb_Field6
        self.mongodb_Field10 = mongodb_Field10
        self.mongodb_Field = mongodb_Field
        
        pass
    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key


    @property
    def mongodb_Field6(self):
        return self.__mongodb_Field6

    @mongodb_Field6.setter
    def mongodb_Field6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mongodb_Field__mongodb_Field6", None)
        self.__mongodb_Field6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mongodb_IValue"):
                opp_val = getattr(old_value, "mongodb_IValue", None)
                if opp_val == self:
                    setattr(old_value, "mongodb_IValue", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mongodb_IValue"):
                opp_val = getattr(value, "mongodb_IValue", None)
                setattr(value, "mongodb_IValue", self)

    @property
    def mongodb_Field10(self):
        return self.__mongodb_Field10

    @mongodb_Field10.setter
    def mongodb_Field10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mongodb_Field__mongodb_Field10", None)
        self.__mongodb_Field10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mongodb_SubDocument"):
                opp_val = getattr(old_value, "mongodb_SubDocument", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mongodb_SubDocument"):
                opp_val = getattr(value, "mongodb_SubDocument", None)
                if opp_val is None:
                    setattr(value, "mongodb_SubDocument", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mongodb_Field(self):
        return self.__mongodb_Field

    @mongodb_Field.setter
    def mongodb_Field(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mongodb_Field__mongodb_Field", None)
        self.__mongodb_Field = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mongodb_Document4"):
                opp_val = getattr(old_value, "mongodb_Document4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mongodb_Document4"):
                opp_val = getattr(value, "mongodb_Document4", None)
                if opp_val is None:
                    setattr(value, "mongodb_Document4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
