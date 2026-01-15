from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class DatabaseKind(Enum):
    POSTGRES = "POSTGRES"


############################################
# Definition of Classes
############################################

class PrimitiveType:

    pass
class relationaldb_UmlToNoSQLID(PrimitiveType):

    pass
class relationaldb_Varchar(PrimitiveType):

    def __init__(self, length: int):
        self.length = length
        
    @property
    def length(self) -> int:
        return self.__length

    @length.setter
    def length(self, length: int):
        self.__length = length

class relationaldb_Integer(PrimitiveType):

    pass
class Type:

    pass
class relationaldb_PrimitiveType(Type):

    pass
class Column:

    pass
class relationaldb_ForeignKey(Column):

    pass
class relationaldb_Type(ABC):

    pass
class Named:

    pass
class relationaldb_Column(Named):

    pass
class relationaldb_Table(Named):

    pass
class relationaldb_Database(Named):

    def __init__(self, rawDatabase: str, relationaldb_Database: set["relationaldb_Table"] = None):
        self.rawDatabase = rawDatabase
        self.relationaldb_Database = relationaldb_Database if relationaldb_Database is not None else set()
        
    @property
    def rawDatabase(self) -> str:
        return self.__rawDatabase

    @rawDatabase.setter
    def rawDatabase(self, rawDatabase: str):
        self.__rawDatabase = rawDatabase

    @property
    def relationaldb_Database(self):
        return self.__relationaldb_Database

    @relationaldb_Database.setter
    def relationaldb_Database(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relationaldb_Database__relationaldb_Database", None)
        self.__relationaldb_Database = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "relationaldb_Table"):
                    opp_val = getattr(item, "relationaldb_Table", None)
                    
                    if opp_val == self:
                        setattr(item, "relationaldb_Table", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "relationaldb_Table"):
                    opp_val = getattr(item, "relationaldb_Table", None)
                    
                    setattr(item, "relationaldb_Table", self)
                    

class relationaldb_Named(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name
