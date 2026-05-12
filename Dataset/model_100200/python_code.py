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
class model_column_DefaultExpressionValueColumnConstraint:

    pass
class model_column_DefaultRealValueColumnConstraint:

    pass
class model_column_DefaultIntegerValueColumnConstraint:

    pass
class model_column_DefaultStringValueColumnConstraint:

    pass
class model_column_ColumnConstraint(ABC):

    def __init__(self, name: str, constraints51: "Column" = None):
        self.name = name
        self.constraints51 = constraints51
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def constraints51(self):
        return self.__constraints51

    @constraints51.setter
    def constraints51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_column_ColumnConstraint__constraints51", None)
        self.__constraints51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Column52"):
                opp_val = getattr(old_value, "Column52", None)
                if opp_val == self:
                    setattr(old_value, "Column52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Column52"):
                opp_val = getattr(value, "Column52", None)
                setattr(value, "Column52", self)

class model_column_IndexedColumn:

    pass
class ColumnConstraint:

    pass
class model_column_NotNullColumnConstraint(ColumnConstraint):

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
class Expression:

    pass
class IndexedColumn:

    pass
class model_table_TableConstraint(ABC):

    def __init__(self, name: str, constraints: "Table" = None):
        self.name = name
        self.constraints = constraints
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def constraints(self):
        return self.__constraints

    @constraints.setter
    def constraints(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_table_TableConstraint__constraints", None)
        self.__constraints = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Table32"):
                opp_val = getattr(old_value, "Table32", None)
                if opp_val == self:
                    setattr(old_value, "Table32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Table32"):
                opp_val = getattr(value, "Table32", None)
                setattr(value, "Table32", self)

class TableConstraint:

    pass
class model_table_ForeignKeyTableConstraint(TableConstraint):

    pass
class model_table_CheckTableConstraint(TableConstraint):

    pass
class model_table_UniqueTableConstraint(TableConstraint):

    pass
class model_table_PrimaryKeyTableConstraint(TableConstraint):

    pass
class Column:

    pass
class table_model_Database:

    pass
class StringToColumnMappingEntryMap:

    pass
class model_common_ColumnMapping:

    def __init__(self, model_common_ColumnMapping: set["StringToColumnMappingEntryMap"] = None, model_common_ColumnMapping25: set["StringToColumnMappingEntryMap"] = None):
        self.model_common_ColumnMapping = model_common_ColumnMapping if model_common_ColumnMapping is not None else set()
        self.model_common_ColumnMapping25 = model_common_ColumnMapping25 if model_common_ColumnMapping25 is not None else set()
        
        pass
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
                    

    @property
    def model_common_ColumnMapping25(self):
        return self.__model_common_ColumnMapping25

    @model_common_ColumnMapping25.setter
    def model_common_ColumnMapping25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_common_ColumnMapping__model_common_ColumnMapping25", None)
        self.__model_common_ColumnMapping25 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StringToColumnMappingEntryMap26"):
                    opp_val = getattr(item, "StringToColumnMappingEntryMap26", None)
                    
                    if opp_val == self:
                        setattr(item, "StringToColumnMappingEntryMap26", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StringToColumnMappingEntryMap26"):
                    opp_val = getattr(item, "StringToColumnMappingEntryMap26", None)
                    
                    setattr(item, "StringToColumnMappingEntryMap26", self)
                    

    def entries(self):
        # TODO: Implement entries method
        pass

    def put(self, model_current, model_previous):
        # TODO: Implement put method
        pass

    def getPrevious(self, model_current) :
        # TODO: Implement getPrevious method
        pass

    def getAllPrevious(self):
        # TODO: Implement getAllPrevious method
        pass

    def getCurrent(self, model_previous) :
        # TODO: Implement getCurrent method
        pass

    def getAllCurrent(self):
        # TODO: Implement getAllCurrent method
        pass

class StringToTableMappingEntryMap:

    pass
class model_common_TableMapping:

    def __init__(self, model_common_TableMapping21: set["StringToTableMappingEntryMap"] = None, model_common_TableMapping: set["StringToTableMappingEntryMap"] = None):
        self.model_common_TableMapping21 = model_common_TableMapping21 if model_common_TableMapping21 is not None else set()
        self.model_common_TableMapping = model_common_TableMapping if model_common_TableMapping is not None else set()
        
        pass
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
    def model_common_TableMapping21(self):
        return self.__model_common_TableMapping21

    @model_common_TableMapping21.setter
    def model_common_TableMapping21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_common_TableMapping__model_common_TableMapping21", None)
        self.__model_common_TableMapping21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StringToTableMappingEntryMap22"):
                    opp_val = getattr(item, "StringToTableMappingEntryMap22", None)
                    
                    if opp_val == self:
                        setattr(item, "StringToTableMappingEntryMap22", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StringToTableMappingEntryMap22"):
                    opp_val = getattr(item, "StringToTableMappingEntryMap22", None)
                    
                    setattr(item, "StringToTableMappingEntryMap22", self)
                    

    def entries(self):
        # TODO: Implement entries method
        pass

    def getPrevious(self, model_current) :
        # TODO: Implement getPrevious method
        pass

    def getCurrent(self, model_previous) :
        # TODO: Implement getCurrent method
        pass

    def put(self, model_previous, model_current):
        # TODO: Implement put method
        pass

    def getAllPrevious(self):
        # TODO: Implement getAllPrevious method
        pass

    def getAllCurrent(self):
        # TODO: Implement getAllCurrent method
        pass

class model_common_StringToColumnMappingEntryMap:

    def __init__(self, key: str):
        self.key = key
        
        pass
    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key


class model_common_StringToTableMappingEntryMap:

    def __init__(self, key: str):
        self.key = key
        
        pass
    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key


class model_common_MappingEntry:

    def __init__(self, previous: str, current: str):
        self.previous = previous
        self.current = current
        
        pass
    @property
    def current(self):
        return self.__current

    @current.setter
    def current(self, current: str):
        self.__current = current


    @property
    def previous(self):
        return self.__previous

    @previous.setter
    def previous(self, previous: str):
        self.__previous = previous


class model_common_NameProvider(ABC):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
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
class model_column_Column(NameProvider):

    def __init__(self, type: str, columns: "Table" = None, column: set["ColumnConstraint"] = None):
        self.type = type
        self.columns = columns
        self.column = column if column is not None else set()
        
        pass
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
        old_value = getattr(self, f"_model_column_Column__columns", None)
        self.__columns = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Table46"):
                opp_val = getattr(old_value, "Table46", None)
                if opp_val == self:
                    setattr(old_value, "Table46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Table46"):
                opp_val = getattr(value, "Table46", None)
                setattr(value, "Table46", self)

    @property
    def column(self):
        return self.__column

    @column.setter
    def column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_column_Column__column", None)
        self.__column = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ColumnConstraint"):
                    opp_val = getattr(item, "ColumnConstraint", None)
                    
                    if opp_val == self:
                        setattr(item, "ColumnConstraint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ColumnConstraint"):
                    opp_val = getattr(item, "ColumnConstraint", None)
                    
                    setattr(item, "ColumnConstraint", self)
                    

class model_trigger_Trigger(NameProvider):

    pass
class model_table_Table(NameProvider):

    pass
class ColumnMapping:

    pass
class TableMapping:

    pass
class model_DatabaseVersions:

    def __init__(self, packageName: str, fileName: str, model_DatabaseVersions: set["model_DatabaseVersion"] = None):
        self.packageName = packageName
        self.fileName = fileName
        self.model_DatabaseVersions = model_DatabaseVersions if model_DatabaseVersions is not None else set()
        
        pass
    @property
    def fileName(self):
        return self.__fileName

    @fileName.setter
    def fileName(self, fileName: str):
        self.__fileName = fileName


    @property
    def packageName(self):
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
                    

    def getLastVersion(self) :
        # TODO: Implement getLastVersion method
        pass

    def createVersion(self) :
        # TODO: Implement createVersion method
        pass

    def getFirstVersion(self) :
        # TODO: Implement getFirstVersion method
        pass

class model_Database(NameProvider):

    pass
class model_DatabaseVersion:

    pass