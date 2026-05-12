from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class ColumnType(Enum):
    STD_FIELD = "STD_FIELD"
    NON_STD_FIELD = "NON_STD_FIELD"
class key_type(Enum):
    Primary = "Primary"
    Unique = "Unique"
    Foreign = "Foreign"


############################################
# Definition of Classes
############################################

class ExtensibleModel:

    pass
class database_DBGenContext(ExtensibleModel):

    pass
class database_TableKey(ExtensibleModel):

    def __init__(self, name: str, type: str, mark: str, database_TableKey: "database_TableResourceData" = None, database_TableKey10: set["database_ForeignKey"] = None, database_TableKey13: set["database_TableColumn"] = None):
        self.name = name
        self.type = type
        self.mark = mark
        self.database_TableKey = database_TableKey
        self.database_TableKey10 = database_TableKey10 if database_TableKey10 is not None else set()
        self.database_TableKey13 = database_TableKey13 if database_TableKey13 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def mark(self):
        return self.__mark

    @mark.setter
    def mark(self, mark: str):
        self.__mark = mark


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def database_TableKey(self):
        return self.__database_TableKey

    @database_TableKey.setter
    def database_TableKey(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_TableKey__database_TableKey", None)
        self.__database_TableKey = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "database_TableResourceData4"):
                opp_val = getattr(old_value, "database_TableResourceData4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "database_TableResourceData4"):
                opp_val = getattr(value, "database_TableResourceData4", None)
                if opp_val is None:
                    setattr(value, "database_TableResourceData4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def database_TableKey13(self):
        return self.__database_TableKey13

    @database_TableKey13.setter
    def database_TableKey13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_TableKey__database_TableKey13", None)
        self.__database_TableKey13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "database_TableColumn14"):
                    opp_val = getattr(item, "database_TableColumn14", None)
                    
                    if opp_val == self:
                        setattr(item, "database_TableColumn14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "database_TableColumn14"):
                    opp_val = getattr(item, "database_TableColumn14", None)
                    
                    setattr(item, "database_TableColumn14", self)
                    

    @property
    def database_TableKey10(self):
        return self.__database_TableKey10

    @database_TableKey10.setter
    def database_TableKey10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_TableKey__database_TableKey10", None)
        self.__database_TableKey10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "database_ForeignKey11"):
                    opp_val = getattr(item, "database_ForeignKey11", None)
                    
                    if opp_val == self:
                        setattr(item, "database_ForeignKey11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "database_ForeignKey11"):
                    opp_val = getattr(item, "database_ForeignKey11", None)
                    
                    setattr(item, "database_ForeignKey11", self)
                    

class database_TableIndex(ExtensibleModel):

    def __init__(self, name: str, unique: bool, cluster: bool, mark: str, database_TableIndex: "database_TableResourceData" = None, database_TableIndex8: set["database_TableIndexColumn"] = None):
        self.name = name
        self.unique = unique
        self.cluster = cluster
        self.mark = mark
        self.database_TableIndex = database_TableIndex
        self.database_TableIndex8 = database_TableIndex8 if database_TableIndex8 is not None else set()
        
        pass
    @property
    def mark(self):
        return self.__mark

    @mark.setter
    def mark(self, mark: str):
        self.__mark = mark


    @property
    def unique(self):
        return self.__unique

    @unique.setter
    def unique(self, unique: bool):
        self.__unique = unique


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def cluster(self):
        return self.__cluster

    @cluster.setter
    def cluster(self, cluster: bool):
        self.__cluster = cluster


    @property
    def database_TableIndex(self):
        return self.__database_TableIndex

    @database_TableIndex.setter
    def database_TableIndex(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_TableIndex__database_TableIndex", None)
        self.__database_TableIndex = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "database_TableResourceData2"):
                opp_val = getattr(old_value, "database_TableResourceData2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "database_TableResourceData2"):
                opp_val = getattr(value, "database_TableResourceData2", None)
                if opp_val is None:
                    setattr(value, "database_TableResourceData2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def database_TableIndex8(self):
        return self.__database_TableIndex8

    @database_TableIndex8.setter
    def database_TableIndex8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_TableIndex__database_TableIndex8", None)
        self.__database_TableIndex8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "database_TableIndexColumn"):
                    opp_val = getattr(item, "database_TableIndexColumn", None)
                    
                    if opp_val == self:
                        setattr(item, "database_TableIndexColumn", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "database_TableIndexColumn"):
                    opp_val = getattr(item, "database_TableIndexColumn", None)
                    
                    setattr(item, "database_TableIndexColumn", self)
                    

class database_TableIndexColumn(ExtensibleModel):

    def __init__(self, columnName: str, ascending: bool, columnType: str, database_TableIndexColumn: "database_TableIndex" = None):
        self.columnName = columnName
        self.ascending = ascending
        self.columnType = columnType
        self.database_TableIndexColumn = database_TableIndexColumn
        
        pass
    @property
    def columnType(self):
        return self.__columnType

    @columnType.setter
    def columnType(self, columnType: str):
        self.__columnType = columnType


    @property
    def columnName(self):
        return self.__columnName

    @columnName.setter
    def columnName(self, columnName: str):
        self.__columnName = columnName


    @property
    def ascending(self):
        return self.__ascending

    @ascending.setter
    def ascending(self, ascending: bool):
        self.__ascending = ascending


    @property
    def database_TableIndexColumn(self):
        return self.__database_TableIndexColumn

    @database_TableIndexColumn.setter
    def database_TableIndexColumn(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_TableIndexColumn__database_TableIndexColumn", None)
        self.__database_TableIndexColumn = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "database_TableIndex8"):
                opp_val = getattr(old_value, "database_TableIndex8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "database_TableIndex8"):
                opp_val = getattr(value, "database_TableIndex8", None)
                if opp_val is None:
                    setattr(value, "database_TableIndex8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class database_ForeignKey:

    def __init__(self, tableName: str, fieldName: str, database_ForeignKey: "database_TableColumn" = None, database_ForeignKey11: "database_TableKey" = None):
        self.tableName = tableName
        self.fieldName = fieldName
        self.database_ForeignKey = database_ForeignKey
        self.database_ForeignKey11 = database_ForeignKey11
        
        pass
    @property
    def tableName(self):
        return self.__tableName

    @tableName.setter
    def tableName(self, tableName: str):
        self.__tableName = tableName


    @property
    def fieldName(self):
        return self.__fieldName

    @fieldName.setter
    def fieldName(self, fieldName: str):
        self.__fieldName = fieldName


    @property
    def database_ForeignKey11(self):
        return self.__database_ForeignKey11

    @database_ForeignKey11.setter
    def database_ForeignKey11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_ForeignKey__database_ForeignKey11", None)
        self.__database_ForeignKey11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "database_TableKey10"):
                opp_val = getattr(old_value, "database_TableKey10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "database_TableKey10"):
                opp_val = getattr(value, "database_TableKey10", None)
                if opp_val is None:
                    setattr(value, "database_TableKey10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def database_ForeignKey(self):
        return self.__database_ForeignKey

    @database_ForeignKey.setter
    def database_ForeignKey(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_ForeignKey__database_ForeignKey", None)
        self.__database_ForeignKey = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "database_TableColumn6"):
                opp_val = getattr(old_value, "database_TableColumn6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "database_TableColumn6"):
                opp_val = getattr(value, "database_TableColumn6", None)
                if opp_val is None:
                    setattr(value, "database_TableColumn6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class database_TableColumn(ExtensibleModel):

    def __init__(self, nullable: bool, defaultValue: str, mark: str, comments: str, columnType: str, name: str, chineseName: str, description: str, dataType: str, columnName: str, fieldName: str, primaryKey: bool, unique: bool, database_TableColumn6: set["database_ForeignKey"] = None, database_TableColumn: "database_TableResourceData" = None, database_TableColumn14: "database_TableKey" = None):
        self.nullable = nullable
        self.defaultValue = defaultValue
        self.mark = mark
        self.comments = comments
        self.columnType = columnType
        self.name = name
        self.chineseName = chineseName
        self.description = description
        self.dataType = dataType
        self.columnName = columnName
        self.fieldName = fieldName
        self.primaryKey = primaryKey
        self.unique = unique
        self.database_TableColumn6 = database_TableColumn6 if database_TableColumn6 is not None else set()
        self.database_TableColumn = database_TableColumn
        self.database_TableColumn14 = database_TableColumn14
        
        pass
    @property
    def fieldName(self):
        return self.__fieldName

    @fieldName.setter
    def fieldName(self, fieldName: str):
        self.__fieldName = fieldName


    @property
    def chineseName(self):
        return self.__chineseName

    @chineseName.setter
    def chineseName(self, chineseName: str):
        self.__chineseName = chineseName


    @property
    def columnName(self):
        return self.__columnName

    @columnName.setter
    def columnName(self, columnName: str):
        self.__columnName = columnName


    @property
    def unique(self):
        return self.__unique

    @unique.setter
    def unique(self, unique: bool):
        self.__unique = unique


    @property
    def comments(self):
        return self.__comments

    @comments.setter
    def comments(self, comments: str):
        self.__comments = comments


    @property
    def nullable(self):
        return self.__nullable

    @nullable.setter
    def nullable(self, nullable: bool):
        self.__nullable = nullable


    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


    @property
    def defaultValue(self):
        return self.__defaultValue

    @defaultValue.setter
    def defaultValue(self, defaultValue: str):
        self.__defaultValue = defaultValue


    @property
    def mark(self):
        return self.__mark

    @mark.setter
    def mark(self, mark: str):
        self.__mark = mark


    @property
    def columnType(self):
        return self.__columnType

    @columnType.setter
    def columnType(self, columnType: str):
        self.__columnType = columnType


    @property
    def dataType(self):
        return self.__dataType

    @dataType.setter
    def dataType(self, dataType: str):
        self.__dataType = dataType


    @property
    def primaryKey(self):
        return self.__primaryKey

    @primaryKey.setter
    def primaryKey(self, primaryKey: bool):
        self.__primaryKey = primaryKey


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def database_TableColumn14(self):
        return self.__database_TableColumn14

    @database_TableColumn14.setter
    def database_TableColumn14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_TableColumn__database_TableColumn14", None)
        self.__database_TableColumn14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "database_TableKey13"):
                opp_val = getattr(old_value, "database_TableKey13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "database_TableKey13"):
                opp_val = getattr(value, "database_TableKey13", None)
                if opp_val is None:
                    setattr(value, "database_TableKey13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def database_TableColumn6(self):
        return self.__database_TableColumn6

    @database_TableColumn6.setter
    def database_TableColumn6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_TableColumn__database_TableColumn6", None)
        self.__database_TableColumn6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "database_ForeignKey"):
                    opp_val = getattr(item, "database_ForeignKey", None)
                    
                    if opp_val == self:
                        setattr(item, "database_ForeignKey", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "database_ForeignKey"):
                    opp_val = getattr(item, "database_ForeignKey", None)
                    
                    setattr(item, "database_ForeignKey", self)
                    

    @property
    def database_TableColumn(self):
        return self.__database_TableColumn

    @database_TableColumn.setter
    def database_TableColumn(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_TableColumn__database_TableColumn", None)
        self.__database_TableColumn = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "database_TableResourceData"):
                opp_val = getattr(old_value, "database_TableResourceData", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "database_TableResourceData"):
                opp_val = getattr(value, "database_TableResourceData", None)
                if opp_val is None:
                    setattr(value, "database_TableResourceData", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class DatabaseResourceData:

    pass
class database_ViewResourceData(DatabaseResourceData):

    def __init__(self, sql: str, isHistory: bool):
        self.sql = sql
        self.isHistory = isHistory
        
        pass
    @property
    def isHistory(self):
        return self.__isHistory

    @isHistory.setter
    def isHistory(self, isHistory: bool):
        self.__isHistory = isHistory


    @property
    def sql(self):
        return self.__sql

    @sql.setter
    def sql(self, sql: str):
        self.__sql = sql


class database_TableResourceData(DatabaseResourceData):

    pass
class JRESResourceInfo:

    pass
class database_DatabaseResourceData(JRESResourceInfo):

    pass
class database_DBModuleCommonProperty:

    def __init__(self, database: str, supportDatabases: str):
        self.database = database
        self.supportDatabases = supportDatabases
        
        pass
    @property
    def supportDatabases(self):
        return self.__supportDatabases

    @supportDatabases.setter
    def supportDatabases(self, supportDatabases: str):
        self.__supportDatabases = supportDatabases


    @property
    def database(self):
        return self.__database

    @database.setter
    def database(self, database: str):
        self.__database = database

