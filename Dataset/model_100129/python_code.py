from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class OrderingType(Enum):
    Ascend = "Ascend"
    Descend = "Descend"
class DatabaseDataType(Enum):
    Character = "Character"
    Varchar = "Varchar"
    Decimal = "Decimal"
    Boolean = "Boolean"
    Date = "Date"
    Time = "Time"
    TimeStamp = "TimeStamp"
    Integer = "Integer"
    Float = "Float"
    Graphical = "Graphical"
    Text = "Text"
    Blob = "Blob"
    Identity = "Identity"


############################################
# Definition of Classes
############################################

class core_Statement(ABC):

    def __init__(self):
        
        pass
    def addBatch(self, core_sql):
        # TODO: Implement addBatch method
        pass

    def clearBatch(self):
        # TODO: Implement clearBatch method
        pass

    def executeUpdate(self, core_sql) :
        # TODO: Implement executeUpdate method
        pass

    def executeBatch(self) :
        # TODO: Implement executeBatch method
        pass

    def close(self):
        # TODO: Implement close method
        pass

    def executeQuery(self, core_sql) :
        # TODO: Implement executeQuery method
        pass

    def execute(self, core_sql) :
        # TODO: Implement execute method
        pass

class TableDef:

    pass
class core_ViewDef(TableDef):

    def __init__(self, querySelect: str):
        self.querySelect = querySelect
        
        pass
    @property
    def querySelect(self):
        return self.__querySelect

    @querySelect.setter
    def querySelect(self, querySelect: str):
        self.__querySelect = querySelect


class DatabaseObjectDef:

    pass
class core_IndexColumnDef(DatabaseObjectDef):

    def __init__(self, ordering: str, sequence: int, name: str, core_IndexColumnDef: "core_IndexDef" = None):
        self.ordering = ordering
        self.sequence = sequence
        self.name = name
        self.core_IndexColumnDef = core_IndexColumnDef
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def ordering(self):
        return self.__ordering

    @ordering.setter
    def ordering(self, ordering: str):
        self.__ordering = ordering


    @property
    def sequence(self):
        return self.__sequence

    @sequence.setter
    def sequence(self, sequence: int):
        self.__sequence = sequence


    @property
    def core_IndexColumnDef(self):
        return self.__core_IndexColumnDef

    @core_IndexColumnDef.setter
    def core_IndexColumnDef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_IndexColumnDef__core_IndexColumnDef", None)
        self.__core_IndexColumnDef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_IndexDef"):
                opp_val = getattr(old_value, "core_IndexDef", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_IndexDef"):
                opp_val = getattr(value, "core_IndexDef", None)
                if opp_val is None:
                    setattr(value, "core_IndexDef", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class core_TableColumnDef(DatabaseObjectDef):

    def __init__(self, dataType: str, default: bool, length: int, name: str, nullable: bool, scale: int, core_TableColumnDef: "core_TableDef" = None):
        self.dataType = dataType
        self.default = default
        self.length = length
        self.name = name
        self.nullable = nullable
        self.scale = scale
        self.core_TableColumnDef = core_TableColumnDef
        
        pass
    @property
    def scale(self):
        return self.__scale

    @scale.setter
    def scale(self, scale: int):
        self.__scale = scale


    @property
    def default(self):
        return self.__default

    @default.setter
    def default(self, default: bool):
        self.__default = default


    @property
    def nullable(self):
        return self.__nullable

    @nullable.setter
    def nullable(self, nullable: bool):
        self.__nullable = nullable


    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, length: int):
        self.__length = length


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def dataType(self):
        return self.__dataType

    @dataType.setter
    def dataType(self, dataType: str):
        self.__dataType = dataType


    @property
    def core_TableColumnDef(self):
        return self.__core_TableColumnDef

    @core_TableColumnDef.setter
    def core_TableColumnDef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_TableColumnDef__core_TableColumnDef", None)
        self.__core_TableColumnDef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_TableDef"):
                opp_val = getattr(old_value, "core_TableDef", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_TableDef"):
                opp_val = getattr(value, "core_TableDef", None)
                if opp_val is None:
                    setattr(value, "core_TableDef", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class core_TableDef(DatabaseObjectDef):

    pass
class core_SchemaDef(DatabaseObjectDef):

    pass
class core_IndexDef(DatabaseObjectDef):

    def __init__(self, clustered: bool, unique: bool, core_IndexDef: set["core_IndexColumnDef"] = None):
        self.clustered = clustered
        self.unique = unique
        self.core_IndexDef = core_IndexDef if core_IndexDef is not None else set()
        
        pass
    @property
    def unique(self):
        return self.__unique

    @unique.setter
    def unique(self, unique: bool):
        self.__unique = unique


    @property
    def clustered(self):
        return self.__clustered

    @clustered.setter
    def clustered(self, clustered: bool):
        self.__clustered = clustered


    @property
    def core_IndexDef(self):
        return self.__core_IndexDef

    @core_IndexDef.setter
    def core_IndexDef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_IndexDef__core_IndexDef", None)
        self.__core_IndexDef = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core_IndexColumnDef"):
                    opp_val = getattr(item, "core_IndexColumnDef", None)
                    
                    if opp_val == self:
                        setattr(item, "core_IndexColumnDef", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core_IndexColumnDef"):
                    opp_val = getattr(item, "core_IndexColumnDef", None)
                    
                    setattr(item, "core_IndexColumnDef", self)
                    

class core_DataSourceFactory(ABC):

    pass
class core_QualifiedName:

    def __init__(self, qualifiers: str):
        self.qualifiers = qualifiers
        
        pass
    @property
    def qualifiers(self):
        return self.__qualifiers

    @qualifiers.setter
    def qualifiers(self, qualifiers: str):
        self.__qualifiers = qualifiers


    def getLastQualifier(self) :
        # TODO: Implement getLastQualifier method
        pass

    def getFirstQualifier(self) :
        # TODO: Implement getFirstQualifier method
        pass

class Statement:

    pass
class core_PreparedStatement(Statement):

    def __init__(self):
        
        pass
    def addBatch(self):
        # TODO: Implement addBatch method
        pass

    def executeQuery(self) :
        # TODO: Implement executeQuery method
        pass

    def clearParameters(self):
        # TODO: Implement clearParameters method
        pass

    def execute(self) :
        # TODO: Implement execute method
        pass

    def setString(self, core_position, core_value):
        # TODO: Implement setString method
        pass

    def setInt(self, core_position, core_value):
        # TODO: Implement setInt method
        pass

    def executeUpdate(self) :
        # TODO: Implement executeUpdate method
        pass

class core_DatabaseObjectDef(ABC):

    pass
class Credentials:

    pass
class core_ConnectionCredentials(Credentials):

    pass
class ServiceConfig:

    pass
class core_DatabaseContainer(ServiceConfig):

    def __init__(self, vendor: str, version: str, core_DatabaseContainer: set["core_CatalogContainer"] = None, core_DatabaseContainer8: "core_CatalogContainer" = None):
        self.vendor = vendor
        self.version = version
        self.core_DatabaseContainer = core_DatabaseContainer if core_DatabaseContainer is not None else set()
        self.core_DatabaseContainer8 = core_DatabaseContainer8
        
        pass
    @property
    def version(self):
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version


    @property
    def vendor(self):
        return self.__vendor

    @vendor.setter
    def vendor(self, vendor: str):
        self.__vendor = vendor


    @property
    def core_DatabaseContainer8(self):
        return self.__core_DatabaseContainer8

    @core_DatabaseContainer8.setter
    def core_DatabaseContainer8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_DatabaseContainer__core_DatabaseContainer8", None)
        self.__core_DatabaseContainer8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_CatalogContainer9"):
                opp_val = getattr(old_value, "core_CatalogContainer9", None)
                if opp_val == self:
                    setattr(old_value, "core_CatalogContainer9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_CatalogContainer9"):
                opp_val = getattr(value, "core_CatalogContainer9", None)
                setattr(value, "core_CatalogContainer9", self)

    @property
    def core_DatabaseContainer(self):
        return self.__core_DatabaseContainer

    @core_DatabaseContainer.setter
    def core_DatabaseContainer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_DatabaseContainer__core_DatabaseContainer", None)
        self.__core_DatabaseContainer = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core_CatalogContainer6"):
                    opp_val = getattr(item, "core_CatalogContainer6", None)
                    
                    if opp_val == self:
                        setattr(item, "core_CatalogContainer6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core_CatalogContainer6"):
                    opp_val = getattr(item, "core_CatalogContainer6", None)
                    
                    setattr(item, "core_CatalogContainer6", self)
                    

class Service:

    pass
class core_DatabaseManager(Service):

    def __init__(self):
        
        pass
    def dropTable(self, core_table, core_connection):
        # TODO: Implement dropTable method
        pass

    def createTable(self, core_schema, core_connection, core_table, core_name) :
        # TODO: Implement createTable method
        pass

    def isStarted(self) :
        # TODO: Implement isStarted method
        pass

    def createView(self, core_connection, core_schema, core_view, core_name) :
        # TODO: Implement createView method
        pass

    def start(self, core_databaseContainer):
        # TODO: Implement start method
        pass

    def createSchema(self, core_connection, core_name, core_schema) :
        # TODO: Implement createSchema method
        pass

    def dropSchema(self, core_schema, core_ignoreFailOnNonEmpty, core_connection):
        # TODO: Implement dropSchema method
        pass

    def dropView(self, core_connection, core_view):
        # TODO: Implement dropView method
        pass

    def createIndex(self, core_index, core_table, core_connection, core_name) :
        # TODO: Implement createIndex method
        pass

    def dropIndex(self, core_index, core_connection):
        # TODO: Implement dropIndex method
        pass

class core_ConnectionManager(Service):

    def __init__(self):
        
        pass
    def createConnection(self, core_catalog, core_user, core_password) :
        # TODO: Implement createConnection method
        pass

class core_ConnectionDescription(ABC):

    def __init__(self, schemas: str):
        self.schemas = schemas
        
        pass
    @property
    def schemas(self):
        return self.__schemas

    @schemas.setter
    def schemas(self, schemas: str):
        self.__schemas = schemas


class core_CatalogMetaData(ABC):

    def __init__(self):
        
        pass
    def getIndex(self, core_schema, core_index, core_table) :
        # TODO: Implement getIndex method
        pass

    def getView(self, core_schema, core_table) :
        # TODO: Implement getView method
        pass

    def getSchema(self, core_schema) :
        # TODO: Implement getSchema method
        pass

    def getSchemas(self) :
        # TODO: Implement getSchemas method
        pass

    def getTable(self, core_connectionDescription, core_table) :
        # TODO: Implement getTable method
        pass

class core_CatalogGenerationStrategy:

    def __init__(self, createIndexOnView: bool, createRelativeRecordNumber: bool, core_CatalogGenerationStrategy: "core_CatalogContainer" = None):
        self.createIndexOnView = createIndexOnView
        self.createRelativeRecordNumber = createRelativeRecordNumber
        self.core_CatalogGenerationStrategy = core_CatalogGenerationStrategy
        
        pass
    @property
    def createRelativeRecordNumber(self):
        return self.__createRelativeRecordNumber

    @createRelativeRecordNumber.setter
    def createRelativeRecordNumber(self, createRelativeRecordNumber: bool):
        self.__createRelativeRecordNumber = createRelativeRecordNumber


    @property
    def createIndexOnView(self):
        return self.__createIndexOnView

    @createIndexOnView.setter
    def createIndexOnView(self, createIndexOnView: bool):
        self.__createIndexOnView = createIndexOnView


    @property
    def core_CatalogGenerationStrategy(self):
        return self.__core_CatalogGenerationStrategy

    @core_CatalogGenerationStrategy.setter
    def core_CatalogGenerationStrategy(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_CatalogGenerationStrategy__core_CatalogGenerationStrategy", None)
        self.__core_CatalogGenerationStrategy = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_CatalogContainer2"):
                opp_val = getattr(old_value, "core_CatalogContainer2", None)
                if opp_val == self:
                    setattr(old_value, "core_CatalogContainer2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_CatalogContainer2"):
                opp_val = getattr(value, "core_CatalogContainer2", None)
                setattr(value, "core_CatalogContainer2", self)

class ContextProvider:

    pass
class ContextID:

    pass
class core_Connection(ContextProvider, ContextID):

    def __init__(self):
        
        pass
    def getCatalog(self) :
        # TODO: Implement getCatalog method
        pass

    def translate(self, core_sql) :
        # TODO: Implement translate method
        pass

    def createStatement(self, core_native, core_updatable) :
        # TODO: Implement createStatement method
        pass

    def close(self):
        # TODO: Implement close method
        pass

    def getCatalogMetaData(self) :
        # TODO: Implement getCatalogMetaData method
        pass

    def setCatalog(self, core_catalog):
        # TODO: Implement setCatalog method
        pass

    def prepareStatement(self, core_updatable, core_sql, core_native) :
        # TODO: Implement prepareStatement method
        pass

    def getConnectionDescription(self) :
        # TODO: Implement getConnectionDescription method
        pass

    def getCatalogGenerationStrategy(self) :
        # TODO: Implement getCatalogGenerationStrategy method
        pass

class core_CatalogContainer:

    def __init__(self, name: str, active: bool, supportsGuestAccess: bool, core_CatalogContainer: "core_ConnectionConfig" = None, core_CatalogContainer2: "core_CatalogGenerationStrategy" = None, core_CatalogContainer6: "core_DatabaseContainer" = None, core_CatalogContainer9: "core_DatabaseContainer" = None):
        self.name = name
        self.active = active
        self.supportsGuestAccess = supportsGuestAccess
        self.core_CatalogContainer = core_CatalogContainer
        self.core_CatalogContainer2 = core_CatalogContainer2
        self.core_CatalogContainer6 = core_CatalogContainer6
        self.core_CatalogContainer9 = core_CatalogContainer9
        
        pass
    @property
    def supportsGuestAccess(self):
        return self.__supportsGuestAccess

    @supportsGuestAccess.setter
    def supportsGuestAccess(self, supportsGuestAccess: bool):
        self.__supportsGuestAccess = supportsGuestAccess


    @property
    def active(self):
        return self.__active

    @active.setter
    def active(self, active: bool):
        self.__active = active


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def core_CatalogContainer9(self):
        return self.__core_CatalogContainer9

    @core_CatalogContainer9.setter
    def core_CatalogContainer9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_CatalogContainer__core_CatalogContainer9", None)
        self.__core_CatalogContainer9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_DatabaseContainer8"):
                opp_val = getattr(old_value, "core_DatabaseContainer8", None)
                if opp_val == self:
                    setattr(old_value, "core_DatabaseContainer8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_DatabaseContainer8"):
                opp_val = getattr(value, "core_DatabaseContainer8", None)
                setattr(value, "core_DatabaseContainer8", self)

    @property
    def core_CatalogContainer2(self):
        return self.__core_CatalogContainer2

    @core_CatalogContainer2.setter
    def core_CatalogContainer2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_CatalogContainer__core_CatalogContainer2", None)
        self.__core_CatalogContainer2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_CatalogGenerationStrategy"):
                opp_val = getattr(old_value, "core_CatalogGenerationStrategy", None)
                if opp_val == self:
                    setattr(old_value, "core_CatalogGenerationStrategy", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_CatalogGenerationStrategy"):
                opp_val = getattr(value, "core_CatalogGenerationStrategy", None)
                setattr(value, "core_CatalogGenerationStrategy", self)

    @property
    def core_CatalogContainer(self):
        return self.__core_CatalogContainer

    @core_CatalogContainer.setter
    def core_CatalogContainer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_CatalogContainer__core_CatalogContainer", None)
        self.__core_CatalogContainer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_ConnectionConfig"):
                opp_val = getattr(old_value, "core_ConnectionConfig", None)
                if opp_val == self:
                    setattr(old_value, "core_ConnectionConfig", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_ConnectionConfig"):
                opp_val = getattr(value, "core_ConnectionConfig", None)
                setattr(value, "core_ConnectionConfig", self)

    @property
    def core_CatalogContainer6(self):
        return self.__core_CatalogContainer6

    @core_CatalogContainer6.setter
    def core_CatalogContainer6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_CatalogContainer__core_CatalogContainer6", None)
        self.__core_CatalogContainer6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_DatabaseContainer"):
                opp_val = getattr(old_value, "core_DatabaseContainer", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_DatabaseContainer"):
                opp_val = getattr(value, "core_DatabaseContainer", None)
                if opp_val is None:
                    setattr(value, "core_DatabaseContainer", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def loadTable(self, core_schema, core_name) :
        # TODO: Implement loadTable method
        pass

    def createConnection(self, core_factory, core_password, core_user):
        # TODO: Implement createConnection method
        pass

    def loadSchema(self, core_name) :
        # TODO: Implement loadSchema method
        pass

    def loadIndex(self, core_name, core_table) :
        # TODO: Implement loadIndex method
        pass

    def getCatalogContext(self) :
        # TODO: Implement getCatalogContext method
        pass

    def getMetaData(self) :
        # TODO: Implement getMetaData method
        pass

    def removeTable(self, core_table):
        # TODO: Implement removeTable method
        pass

    def removeSchema(self, core_schema):
        # TODO: Implement removeSchema method
        pass

    def removeIndex(self, core_index):
        # TODO: Implement removeIndex method
        pass

    def removeView(self, core_view):
        # TODO: Implement removeView method
        pass

    def loadView(self, core_name, core_schema) :
        # TODO: Implement loadView method
        pass

class core_ConnectionConfig(ServiceConfig):

    def __init__(self, vendor: str, version: str, url: str, catalog: str, persistent: bool, core_ConnectionConfig: "core_CatalogContainer" = None, core_ConnectionConfig4: "core_ConnectionCredentials" = None):
        self.vendor = vendor
        self.version = version
        self.url = url
        self.catalog = catalog
        self.persistent = persistent
        self.core_ConnectionConfig = core_ConnectionConfig
        self.core_ConnectionConfig4 = core_ConnectionConfig4
        
        pass
    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, url: str):
        self.__url = url


    @property
    def catalog(self):
        return self.__catalog

    @catalog.setter
    def catalog(self, catalog: str):
        self.__catalog = catalog


    @property
    def persistent(self):
        return self.__persistent

    @persistent.setter
    def persistent(self, persistent: bool):
        self.__persistent = persistent


    @property
    def version(self):
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version


    @property
    def vendor(self):
        return self.__vendor

    @vendor.setter
    def vendor(self, vendor: str):
        self.__vendor = vendor


    @property
    def core_ConnectionConfig(self):
        return self.__core_ConnectionConfig

    @core_ConnectionConfig.setter
    def core_ConnectionConfig(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_ConnectionConfig__core_ConnectionConfig", None)
        self.__core_ConnectionConfig = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_CatalogContainer"):
                opp_val = getattr(old_value, "core_CatalogContainer", None)
                if opp_val == self:
                    setattr(old_value, "core_CatalogContainer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_CatalogContainer"):
                opp_val = getattr(value, "core_CatalogContainer", None)
                setattr(value, "core_CatalogContainer", self)

    @property
    def core_ConnectionConfig4(self):
        return self.__core_ConnectionConfig4

    @core_ConnectionConfig4.setter
    def core_ConnectionConfig4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_ConnectionConfig__core_ConnectionConfig4", None)
        self.__core_ConnectionConfig4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_ConnectionCredentials"):
                opp_val = getattr(old_value, "core_ConnectionCredentials", None)
                if opp_val == self:
                    setattr(old_value, "core_ConnectionCredentials", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_ConnectionCredentials"):
                opp_val = getattr(value, "core_ConnectionCredentials", None)
                setattr(value, "core_ConnectionCredentials", self)
