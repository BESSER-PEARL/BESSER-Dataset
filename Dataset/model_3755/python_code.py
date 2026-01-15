from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Type(Enum):
    VARCHAR = "VARCHAR"
    NUMERIC = "NUMERIC"
    DATE = "DATE"
    TIME = "TIME"
    FLOAT = "FLOAT"
    BOOLEAN = "BOOLEAN"
    CHAR = "CHAR"


############################################
# Definition of Classes
############################################

class Field:

    pass
class relational_Column(Field):

    def __init__(self, type: str):
        self.type = type
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class relational_PrimaryKey(Field):

    def __init__(self, id: str):
        self.id = id
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

class relational_ForeignKey(Field):

    pass
class relational_Table:

    def __init__(self, name: str, relational_Table4: set["relational_Field"] = None, relational_Table: "relational_Schema" = None, relational_Table6: "relational_ForeignKey" = None):
        self.name = name
        self.relational_Table4 = relational_Table4 if relational_Table4 is not None else set()
        self.relational_Table = relational_Table
        self.relational_Table6 = relational_Table6
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def relational_Table6(self):
        return self.__relational_Table6

    @relational_Table6.setter
    def relational_Table6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_Table__relational_Table6", None)
        self.__relational_Table6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "relational_ForeignKey"):
                opp_val = getattr(old_value, "relational_ForeignKey", None)
                if opp_val == self:
                    setattr(old_value, "relational_ForeignKey", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "relational_ForeignKey"):
                opp_val = getattr(value, "relational_ForeignKey", None)
                setattr(value, "relational_ForeignKey", self)

    @property
    def relational_Table(self):
        return self.__relational_Table

    @relational_Table.setter
    def relational_Table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_Table__relational_Table", None)
        self.__relational_Table = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "relational_Schema2"):
                opp_val = getattr(old_value, "relational_Schema2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "relational_Schema2"):
                opp_val = getattr(value, "relational_Schema2", None)
                if opp_val is None:
                    setattr(value, "relational_Schema2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def relational_Table4(self):
        return self.__relational_Table4

    @relational_Table4.setter
    def relational_Table4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_Table__relational_Table4", None)
        self.__relational_Table4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "relational_Field"):
                    opp_val = getattr(item, "relational_Field", None)
                    
                    if opp_val == self:
                        setattr(item, "relational_Field", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "relational_Field"):
                    opp_val = getattr(item, "relational_Field", None)
                    
                    setattr(item, "relational_Field", self)
                    

class relational_Schema:

    def __init__(self, name: str, relational_Schema: "relational_DataBase" = None, relational_Schema2: set["relational_Table"] = None):
        self.name = name
        self.relational_Schema = relational_Schema
        self.relational_Schema2 = relational_Schema2 if relational_Schema2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def relational_Schema(self):
        return self.__relational_Schema

    @relational_Schema.setter
    def relational_Schema(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_Schema__relational_Schema", None)
        self.__relational_Schema = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "relational_DataBase"):
                opp_val = getattr(old_value, "relational_DataBase", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "relational_DataBase"):
                opp_val = getattr(value, "relational_DataBase", None)
                if opp_val is None:
                    setattr(value, "relational_DataBase", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def relational_Schema2(self):
        return self.__relational_Schema2

    @relational_Schema2.setter
    def relational_Schema2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_Schema__relational_Schema2", None)
        self.__relational_Schema2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "relational_Table"):
                    opp_val = getattr(item, "relational_Table", None)
                    
                    if opp_val == self:
                        setattr(item, "relational_Table", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "relational_Table"):
                    opp_val = getattr(item, "relational_Table", None)
                    
                    setattr(item, "relational_Table", self)
                    

class relational_DataBase:

    def __init__(self, uri: str, port: int, relational_DataBase: set["relational_Schema"] = None):
        self.uri = uri
        self.port = port
        self.relational_DataBase = relational_DataBase if relational_DataBase is not None else set()
        
    @property
    def port(self) -> int:
        return self.__port

    @port.setter
    def port(self, port: int):
        self.__port = port

    @property
    def uri(self) -> str:
        return self.__uri

    @uri.setter
    def uri(self, uri: str):
        self.__uri = uri

    @property
    def relational_DataBase(self):
        return self.__relational_DataBase

    @relational_DataBase.setter
    def relational_DataBase(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_DataBase__relational_DataBase", None)
        self.__relational_DataBase = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "relational_Schema"):
                    opp_val = getattr(item, "relational_Schema", None)
                    
                    if opp_val == self:
                        setattr(item, "relational_Schema", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "relational_Schema"):
                    opp_val = getattr(item, "relational_Schema", None)
                    
                    setattr(item, "relational_Schema", self)
                    

class relational_Field(ABC):

    def __init__(self, name: str, relational_Field: "relational_Table" = None):
        self.name = name
        self.relational_Field = relational_Field
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def relational_Field(self):
        return self.__relational_Field

    @relational_Field.setter
    def relational_Field(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_Field__relational_Field", None)
        self.__relational_Field = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "relational_Table4"):
                opp_val = getattr(old_value, "relational_Table4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "relational_Table4"):
                opp_val = getattr(value, "relational_Table4", None)
                if opp_val is None:
                    setattr(value, "relational_Table4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
