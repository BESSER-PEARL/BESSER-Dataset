from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class RailsData(Enum):
    binary = "binary"
    boolean = "boolean"
    date = "date"
    dateTime = "dateTime"
    decimal = "decimal"
    float = "float"
    integer = "integer"
    string = "string"
    text = "text"
    time = "time"
    timestamp = "timestamp"


############################################
# Definition of Classes
############################################

class database_ForeignKey:

    pass
class DataBaseElement:

    pass
class database_Table(DataBaseElement):

    pass
class database_Column(DataBaseElement):

    def __init__(self, type: str, database_Column: "database_Table" = None, database_Column5: "database_Table" = None, database_Column10: "database_ForeignKey" = None):
        self.type = type
        self.database_Column = database_Column
        self.database_Column5 = database_Column5
        self.database_Column10 = database_Column10
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def database_Column(self):
        return self.__database_Column

    @database_Column.setter
    def database_Column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_Column__database_Column", None)
        self.__database_Column = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "database_Table2"):
                opp_val = getattr(old_value, "database_Table2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "database_Table2"):
                opp_val = getattr(value, "database_Table2", None)
                if opp_val is None:
                    setattr(value, "database_Table2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def database_Column5(self):
        return self.__database_Column5

    @database_Column5.setter
    def database_Column5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_Column__database_Column5", None)
        self.__database_Column5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "database_Table4"):
                opp_val = getattr(old_value, "database_Table4", None)
                if opp_val == self:
                    setattr(old_value, "database_Table4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "database_Table4"):
                opp_val = getattr(value, "database_Table4", None)
                setattr(value, "database_Table4", self)

    @property
    def database_Column10(self):
        return self.__database_Column10

    @database_Column10.setter
    def database_Column10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_Column__database_Column10", None)
        self.__database_Column10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "database_ForeignKey9"):
                opp_val = getattr(old_value, "database_ForeignKey9", None)
                if opp_val == self:
                    setattr(old_value, "database_ForeignKey9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "database_ForeignKey9"):
                opp_val = getattr(value, "database_ForeignKey9", None)
                setattr(value, "database_ForeignKey9", self)

class database_Schema(DataBaseElement):

    pass
class database_DataBaseElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name
