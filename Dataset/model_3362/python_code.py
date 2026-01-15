from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class DataType(Enum):
    NULL = "NULL"
    INTEGER = "INTEGER"
    REAL = "REAL"
    TEXT = "TEXT"
    BLOB = "BLOB"


############################################
# Definition of Classes
############################################

class model_column_DefaultRealValueColumnConstraint:

    pass
class model_expression_Expression(ABC):

    pass
class trigger_model_Database:

    pass
class index_model_Database:

    pass
class model_index_Index(ABC):

    pass
class view_model_Database:

    pass
class model_column_DefaultIntegerValueColumnConstraint:

    pass
class model_column_DefaultStringValueColumnConstraint:

    pass
class model_column_DefaultExpressionValueColumnConstraint:

    pass
class model_column_ColumnConstraint(ABC):

    def __init__(self, name: str, Column51: "Column" = None):
        self.name = name
        self.Column51 = Column51
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Column51(self):
        return self.__Column51

    @Column51.setter
    def Column51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_column_ColumnConstraint__Column51", None)
        self.__Column51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "column52"):
                opp_val = getattr(old_value, "column52", None)
                if opp_val == self:
                    setattr(old_value, "column52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "column52"):
                opp_val = getattr(value, "column52", None)
                setattr(value, "column52", self)

class model_column_IndexedColumn:

    pass
class ColumnConstraint:

    pass
class model_column_PrimaryKeyColumnConstraint(ColumnConstraint):

    pass
class model_column_CheckColumnConstraint(ColumnConstraint):

    pass
class model_column_DefaultValueColumnConstraint(ColumnConstraint):

    pass
class model_column_UniqueColumnConstraint(ColumnConstraint):

    pass
class model_column_ForeignKeyColumnConstraint(ColumnConstraint):

    pass
class model_column_NotNullColumnConstraint(ColumnConstraint):

    pass
class Expression:

    pass
class IndexedColumn:

    pass
class model_table_TableConstraint(ABC):

    def __init__(self, name: str, Table29: "Table" = None):
        self.name = name
        self.Table29 = Table29
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Table29(self):
        return self.__Table29

    @Table29.setter
    def Table29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_table_TableConstraint__Table29", None)
        self.__Table29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "table30"):
                opp_val = getattr(old_value, "table30", None)
                if opp_val == self:
                    setattr(old_value, "table30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "table30"):
                opp_val = getattr(value, "table30", None)
                setattr(value, "table30", self)

class TableConstraint:

    pass
class model_table_PrimaryKeyTableConstraint(TableConstraint):

    pass
class model_table_CheckTableConstraint(TableConstraint):

    pass
class model_table_UniqueTableConstraint(TableConstraint):

    pass
class model_table_ForeignKeyTableConstraint(TableConstraint):

    pass
class Column:

    pass
class table_model_Database:

    pass
class StringToColumnMappingEntryMap:

    pass
class model_common_ColumnMapping:

    def __init__(self, model_common_ColumnMapping: set["StringToColumnMappingEntryMap"] = None, model_common_ColumnMapping22: set["StringToColumnMappingEntryMap"] = None):
        self.model_common_ColumnMapping = model_common_ColumnMapping if model_common_ColumnMapping is not None else set()
        self.model_common_ColumnMapping22 = model_common_ColumnMapping22 if model_common_ColumnMapping22 is not None else set()
        
    @property
    def model_common_ColumnMapping22(self):
        return self.__model_common_ColumnMapping22

    @model_common_ColumnMapping22.setter
    def model_common_ColumnMapping22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_common_ColumnMapping__model_common_ColumnMapping22", None)
        self.__model_common_ColumnMapping22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StringToColumnMappingEntryMap23"):
                    opp_val = getattr(item, "StringToColumnMappingEntryMap23", None)
                    
                    if opp_val == self:
                        setattr(item, "StringToColumnMappingEntryMap23", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StringToColumnMappingEntryMap23"):
                    opp_val = getattr(item, "StringToColumnMappingEntryMap23", None)
                    
                    setattr(item, "StringToColumnMappingEntryMap23", self)
                    

    @property
    def model_common_ColumnMapping(self):
        return self.__model_common_ColumnMapping

    @model_common_ColumnMapping.setter
    def model_common_ColumnMapping(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_common_ColumnMapping__model_common_ColumnMapping", None)
        self.__model_common_ColumnMapping = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StringToColumnMappingEntryMap"):
                    opp_val = getattr(item, "StringToColumnMappingEntryMap", None)
                    
                    if opp_val == self:
                        setattr(item, "StringToColumnMappingEntryMap", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StringToColumnMappingEntryMap"):
                    opp_val = getattr(item, "StringToColumnMappingEntryMap", None)
                    
                    setattr(item, "StringToColumnMappingEntryMap", self)
                    

    def put(self, previous: str, current: str):
        # TODO: Implement put method
        pass

    def getAllCurrent(self):
        # TODO: Implement getAllCurrent method
        pass

    def getAllPrevious(self):
        # TODO: Implement getAllPrevious method
        pass

    def getCurrent(self, previous: str) -> str:
        # TODO: Implement getCurrent method
        pass

    def entries(self):
        # TODO: Implement entries method
        pass

    def getPrevious(self, current: str) -> str:
        # TODO: Implement getPrevious method
        pass

class StringToTableMappingEntryMap:

    pass
class model_common_TableMapping:

    def __init__(self, model_common_TableMapping: set["StringToTableMappingEntryMap"] = None, model_common_TableMapping18: set["StringToTableMappingEntryMap"] = None):
        self.model_common_TableMapping = model_common_TableMapping if model_common_TableMapping is not None else set()
        self.model_common_TableMapping18 = model_common_TableMapping18 if model_common_TableMapping18 is not None else set()
        
    @property
    def model_common_TableMapping(self):
        return self.__model_common_TableMapping

    @model_common_TableMapping.setter
    def model_common_TableMapping(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_common_TableMapping__model_common_TableMapping", None)
        self.__model_common_TableMapping = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StringToTableMappingEntryMap"):
                    opp_val = getattr(item, "StringToTableMappingEntryMap", None)
                    
                    if opp_val == self:
                        setattr(item, "StringToTableMappingEntryMap", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StringToTableMappingEntryMap"):
                    opp_val = getattr(item, "StringToTableMappingEntryMap", None)
                    
                    setattr(item, "StringToTableMappingEntryMap", self)
                    

    @property
    def model_common_TableMapping18(self):
        return self.__model_common_TableMapping18

    @model_common_TableMapping18.setter
    def model_common_TableMapping18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_common_TableMapping__model_common_TableMapping18", None)
        self.__model_common_TableMapping18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StringToTableMappingEntryMap19"):
                    opp_val = getattr(item, "StringToTableMappingEntryMap19", None)
                    
                    if opp_val == self:
                        setattr(item, "StringToTableMappingEntryMap19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StringToTableMappingEntryMap19"):
                    opp_val = getattr(item, "StringToTableMappingEntryMap19", None)
                    
                    setattr(item, "StringToTableMappingEntryMap19", self)
                    

    def getAllPrevious(self):
        # TODO: Implement getAllPrevious method
        pass

    def getCurrent(self, previous: str) -> str:
        # TODO: Implement getCurrent method
        pass

    def getPrevious(self, current: str) -> str:
        # TODO: Implement getPrevious method
        pass

    def entries(self):
        # TODO: Implement entries method
        pass

    def put(self, previous: str, current: str):
        # TODO: Implement put method
        pass

    def getAllCurrent(self):
        # TODO: Implement getAllCurrent method
        pass

class model_common_StringToColumnMappingEntryMap:

    def __init__(self, key: str):
        self.key = key
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

class model_common_StringToTableMappingEntryMap:

    def __init__(self, key: str):
        self.key = key
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

class model_common_MappingEntry:

    def __init__(self, previous: str, current: str):
        self.previous = previous
        self.current = current
        
    @property
    def current(self) -> str:
        return self.__current

    @current.setter
    def current(self, current: str):
        self.__current = current

    @property
    def previous(self) -> str:
        return self.__previous

    @previous.setter
    def previous(self, previous: str):
        self.__previous = previous

class model_common_NameProvider(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class Index:

    pass
class Trigger:

    pass
class View:

    pass
class Table:

    pass
class NameProvider:

    pass
class model_view_View(NameProvider):

    pass
class model_table_Table(NameProvider):

    pass
class model_trigger_Trigger(NameProvider):

    pass
class model_column_Column(NameProvider):

    def __init__(self, type: str, Table44: "Table" = None, ColumnConstraint: set["ColumnConstraint"] = None):
        self.type = type
        self.Table44 = Table44
        self.ColumnConstraint = ColumnConstraint if ColumnConstraint is not None else set()
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def Table44(self):
        return self.__Table44

    @Table44.setter
    def Table44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_column_Column__Table44", None)
        self.__Table44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "table45"):
                opp_val = getattr(old_value, "table45", None)
                if opp_val == self:
                    setattr(old_value, "table45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "table45"):
                opp_val = getattr(value, "table45", None)
                setattr(value, "table45", self)

    @property
    def ColumnConstraint(self):
        return self.__ColumnConstraint

    @ColumnConstraint.setter
    def ColumnConstraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_column_Column__ColumnConstraint", None)
        self.__ColumnConstraint = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "column47"):
                    opp_val = getattr(item, "column47", None)
                    
                    if opp_val == self:
                        setattr(item, "column47", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "column47"):
                    opp_val = getattr(item, "column47", None)
                    
                    setattr(item, "column47", self)
                    

class ColumnMapping:

    pass
class TableMapping:

    pass
class model_Database(NameProvider):

    pass
class model_DatabaseVersion:

    pass
class model_DatabaseVersions:

    def __init__(self, fileName: str, packageName: str, model_DatabaseVersions: set["model_DatabaseVersion"] = None):
        self.fileName = fileName
        self.packageName = packageName
        self.model_DatabaseVersions = model_DatabaseVersions if model_DatabaseVersions is not None else set()
        
    @property
    def fileName(self) -> str:
        return self.__fileName

    @fileName.setter
    def fileName(self, fileName: str):
        self.__fileName = fileName

    @property
    def packageName(self) -> str:
        return self.__packageName

    @packageName.setter
    def packageName(self, packageName: str):
        self.__packageName = packageName

    @property
    def model_DatabaseVersions(self):
        return self.__model_DatabaseVersions

    @model_DatabaseVersions.setter
    def model_DatabaseVersions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_DatabaseVersions__model_DatabaseVersions", None)
        self.__model_DatabaseVersions = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_DatabaseVersion"):
                    opp_val = getattr(item, "model_DatabaseVersion", None)
                    
                    if opp_val == self:
                        setattr(item, "model_DatabaseVersion", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_DatabaseVersion"):
                    opp_val = getattr(item, "model_DatabaseVersion", None)
                    
                    setattr(item, "model_DatabaseVersion", self)
                    

    def getFirstVersion(self) -> str:
        # TODO: Implement getFirstVersion method
        pass

    def createVersion(self) -> str:
        # TODO: Implement createVersion method
        pass

    def getLastVersion(self) -> str:
        # TODO: Implement getLastVersion method
        pass
