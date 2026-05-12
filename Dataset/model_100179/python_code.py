from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Column:

    pass
class DataBase:

    pass
class Table:

    pass
class NamedElement:

    pass
class RelationalDBSchema_Table(NamedElement):

    pass
class RelationalDBSchema_DataBase(NamedElement):

    def __init__(self, SGBDname: str, database: set["Table"] = None):
        self.SGBDname = SGBDname
        self.database = database if database is not None else set()
        
        pass
    @property
    def SGBDname(self):
        return self.__SGBDname

    @SGBDname.setter
    def SGBDname(self, SGBDname: str):
        self.__SGBDname = SGBDname


    @property
    def database(self):
        return self.__database

    @database.setter
    def database(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RelationalDBSchema_DataBase__database", None)
        self.__database = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Table"):
                    opp_val = getattr(item, "Table", None)
                    
                    if opp_val == self:
                        setattr(item, "Table", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Table"):
                    opp_val = getattr(item, "Table", None)
                    
                    setattr(item, "Table", self)
                    

class RelationalDBSchema_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class RelationalDBSchema_Column(NamedElement):

    def __init__(self, dataType: str, null: str, defaultValue: str, columns: "Table" = None, key: "Table" = None):
        self.dataType = dataType
        self.null = null
        self.defaultValue = defaultValue
        self.columns = columns
        self.key = key
        
        pass
    @property
    def null(self):
        return self.__null

    @null.setter
    def null(self, null: str):
        self.__null = null


    @property
    def dataType(self):
        return self.__dataType

    @dataType.setter
    def dataType(self, dataType: str):
        self.__dataType = dataType


    @property
    def defaultValue(self):
        return self.__defaultValue

    @defaultValue.setter
    def defaultValue(self, defaultValue: str):
        self.__defaultValue = defaultValue


    @property
    def columns(self):
        return self.__columns

    @columns.setter
    def columns(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RelationalDBSchema_Column__columns", None)
        self.__columns = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Table6"):
                opp_val = getattr(old_value, "Table6", None)
                if opp_val == self:
                    setattr(old_value, "Table6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Table6"):
                opp_val = getattr(value, "Table6", None)
                setattr(value, "Table6", self)

    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RelationalDBSchema_Column__key", None)
        self.__key = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Table8"):
                opp_val = getattr(old_value, "Table8", None)
                if opp_val == self:
                    setattr(old_value, "Table8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Table8"):
                opp_val = getattr(value, "Table8", None)
                setattr(value, "Table8", self)
