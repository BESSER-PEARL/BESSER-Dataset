from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class EnumItem:

    pass
class MySQL_EnumSet:

    pass
class EnumSet:

    pass
class DataBase:

    pass
class Column:

    pass
class MySQL_ForeignColumn(Column):

    pass
class MySQL_IntegerColumn(Column):

    def __init__(self, isAutoIncrement: str, Column: "MySQL_Table" = None):
        self.isAutoIncrement = isAutoIncrement
        
        pass
    @property
    def isAutoIncrement(self):
        return self.__isAutoIncrement

    @isAutoIncrement.setter
    def isAutoIncrement(self, isAutoIncrement: str):
        self.__isAutoIncrement = isAutoIncrement


class MySQL_EnumColumn(Column):

    pass
class Table:

    pass
class NamedElement:

    pass
class MySQL_Table(NamedElement):

    pass
class MySQL_EnumItem(NamedElement):

    pass
class MySQL_Column(NamedElement):

    def __init__(self, type: str, isPrimaryKey: str, defaultValue: str, comment: str, columns: "Table" = None):
        self.type = type
        self.isPrimaryKey = isPrimaryKey
        self.defaultValue = defaultValue
        self.comment = comment
        self.columns = columns
        
        pass
    @property
    def comment(self):
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment


    @property
    def isPrimaryKey(self):
        return self.__isPrimaryKey

    @isPrimaryKey.setter
    def isPrimaryKey(self, isPrimaryKey: str):
        self.__isPrimaryKey = isPrimaryKey


    @property
    def defaultValue(self):
        return self.__defaultValue

    @defaultValue.setter
    def defaultValue(self, defaultValue: str):
        self.__defaultValue = defaultValue


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def columns(self):
        return self.__columns

    @columns.setter
    def columns(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MySQL_Column__columns", None)
        self.__columns = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Table4"):
                opp_val = getattr(old_value, "Table4", None)
                if opp_val == self:
                    setattr(old_value, "Table4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Table4"):
                opp_val = getattr(value, "Table4", None)
                setattr(value, "Table4", self)

class MySQL_DataBase(NamedElement):

    pass
class MySQL_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

