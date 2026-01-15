from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class EnumSet:

    pass
class EnumItem:

    pass
class MySQL_EnumSet:

    pass
class Table:

    pass
class NamedElement:

    pass
class MySQL_EnumItem(NamedElement):

    pass
class MySQL_DataBase(NamedElement):

    pass
class MySQL_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class MySQL_Column(NamedElement):

    def __init__(self, type: str, isPrimaryKey: str, defaultValue: str, comment: str, 18: "Table" = None):
        self.type = type
        self.isPrimaryKey = isPrimaryKey
        self.defaultValue = defaultValue
        self.comment = comment
        self.18 = 18
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def isPrimaryKey(self) -> str:
        return self.__isPrimaryKey

    @isPrimaryKey.setter
    def isPrimaryKey(self, isPrimaryKey: str):
        self.__isPrimaryKey = isPrimaryKey

    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def defaultValue(self) -> str:
        return self.__defaultValue

    @defaultValue.setter
    def defaultValue(self, defaultValue: str):
        self.__defaultValue = defaultValue

    @property
    def 18(self):
        return self.__18

    @18.setter
    def 18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MySQL_Column__18", None)
        self.__18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#9"):
                opp_val = getattr(old_value, "#9", None)
                if opp_val == self:
                    setattr(old_value, "#9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#9"):
                opp_val = getattr(value, "#9", None)
                setattr(value, "#9", self)

class DataBase:

    pass
class Column:

    pass
class MySQL_IntegerColumn(Column):

    def __init__(self, isAutoIncrement: str, #3: "MySQL_Table"):
        self.isAutoIncrement = isAutoIncrement
        
    @property
    def isAutoIncrement(self) -> str:
        return self.__isAutoIncrement

    @isAutoIncrement.setter
    def isAutoIncrement(self, isAutoIncrement: str):
        self.__isAutoIncrement = isAutoIncrement

class MySQL_ForeignColumn(Column):

    pass
class MySQL_EnumColumn(Column):

    pass
class MySQL_Table(NamedElement):

    pass