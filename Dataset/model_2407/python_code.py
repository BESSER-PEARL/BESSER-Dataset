from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class ColumnType(Enum):
    TINYINT = "TINYINT"
    SMALLINT = "SMALLINT"
    INTEGER = "INTEGER"
    BIGINT = "BIGINT"
    FLOAT = "FLOAT"
    REAL = "REAL"
    DOUBLE = "DOUBLE"
    NUMERIC = "NUMERIC"
    DECIMAL = "DECIMAL"
    CHAR = "CHAR"
    VARCHAR = "VARCHAR"
    BIT = "BIT"
    TIME = "TIME"
    TIMESTAMP = "TIMESTAMP"
    BINARY = "BINARY"
    VARBINARY = "VARBINARY"
    LONGVARBINARY = "LONGVARBINARY"
    NULL = "NULL"
    OTHER = "OTHER"
    JAVAOBJECT = "JAVAOBJECT"
    DISTINCT = "DISTINCT"
    STRUCT = "STRUCT"
    LONGVARCHAR = "LONGVARCHAR"
    DATE = "DATE"
    DATALINK = "DATALINK"
    BOOLEAN = "BOOLEAN"
    ROWID = "ROWID"
    NCHAR = "NCHAR"
    NVARCHAR = "NVARCHAR"
    LONGNVARCHAR = "LONGNVARCHAR"
    NCLOB = "NCLOB"
    SQLXML = "SQLXML"
    ARRAY = "ARRAY"
    BLOB = "BLOB"
    CLOB = "CLOB"
    REF = "REF"


############################################
# Definition of Classes
############################################

class Column:

    pass
class dbschema_ForeignKeyColumn(Column):

    pass
class dbschema_AttributeColumn(Column):

    pass
class NamedElement:

    pass
class dbschema_Table(NamedElement):

    pass
class dbschema_Column(NamedElement):

    def __init__(self, type: str, size: int, primary: bool, dbschema_Column: "dbschema_Table" = None):
        self.type = type
        self.size = size
        self.primary = primary
        self.dbschema_Column = dbschema_Column
        
    @property
    def size(self) -> int:
        return self.__size

    @size.setter
    def size(self, size: int):
        self.__size = size

    @property
    def primary(self) -> bool:
        return self.__primary

    @primary.setter
    def primary(self, primary: bool):
        self.__primary = primary

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def dbschema_Column(self):
        return self.__dbschema_Column

    @dbschema_Column.setter
    def dbschema_Column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbschema_Column__dbschema_Column", None)
        self.__dbschema_Column = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbschema_Table2"):
                opp_val = getattr(old_value, "dbschema_Table2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbschema_Table2"):
                opp_val = getattr(value, "dbschema_Table2", None)
                if opp_val is None:
                    setattr(value, "dbschema_Table2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class dbschema_DBSchema(NamedElement):

    pass
class dbschema_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name
