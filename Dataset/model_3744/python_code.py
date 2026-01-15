from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class SynchMode(Enum):
    ReadOnly = "ReadOnly"
    Synch = "Synch"
class SQLDataType(Enum):
    Text = "Text"
    Date = "Date"
    DateTime = "DateTime"
    Time = "Time"
    Integer = "Integer"
    Long = "Long"
    Double = "Double"
    Clob = "Clob"
    Blob = "Blob"
    Array = "Array"
    Object = "Object"
    Boolean = "Boolean"
class TransactionMode(Enum):
    None = "None"
    ReadCommitted = "ReadCommitted"
    ReadUncommitted = "ReadUncommitted"
    RepeatableRead = "RepeatableRead"
    Serializable = "Serializable"
class VariableType(Enum):
    Text = "Text"
    Integer = "Integer"
    Decimal = "Decimal"
    Datetime = "Datetime"
    Date = "Date"
    Time = "Time"
    Object = "Object"
    Boolean = "Boolean"
    Array = "Array"
class VariableScope(Enum):
    Local = "Local"
    Global = "Global"
    Runtime = "Runtime"
class QueryType(Enum):
    Select = "Select"
    Update = "Update"
    SPSelect = "SPSelect"
    SPUpdate = "SPUpdate"
class RSHoldabilityMode(Enum):
    HoldCursorsOverCommit = "HoldCursorsOverCommit"
    CloseCursorsOverCommit = "CloseCursorsOverCommit"
class RSScrollMode(Enum):
    ScrollInsensitive = "ScrollInsensitive"
    ScrollSensitive = "ScrollSensitive"
    ForwardOnly = "ForwardOnly"


############################################
# Definition of Classes
############################################

class db_config_SFTPInfo(ABC):

    def __init__(self, sftpUser: str, sftpPassword: str, sftpPort: int):
        self.sftpUser = sftpUser
        self.sftpPassword = sftpPassword
        self.sftpPort = sftpPort
        
    @property
    def sftpPassword(self) -> str:
        return self.__sftpPassword

    @sftpPassword.setter
    def sftpPassword(self, sftpPassword: str):
        self.__sftpPassword = sftpPassword

    @property
    def sftpUser(self) -> str:
        return self.__sftpUser

    @sftpUser.setter
    def sftpUser(self, sftpUser: str):
        self.__sftpUser = sftpUser

    @property
    def sftpPort(self) -> int:
        return self.__sftpPort

    @sftpPort.setter
    def sftpPort(self, sftpPort: int):
        self.__sftpPort = sftpPort

class config_SafiServer:

    pass
class config_Saflet:

    pass
class config_SafletProject:

    pass
class config_Prompt:

    pass
class config_Entitlement:

    pass
class config_Role:

    pass
class ServerResource:

    pass
class db_config_User(ServerResource):

    def __init__(self, firstname: str, lastname: str, password: str, db_config_User: set["config_Role"] = None):
        self.firstname = firstname
        self.lastname = lastname
        self.password = password
        self.db_config_User = db_config_User if db_config_User is not None else set()
        
    @property
    def lastname(self) -> str:
        return self.__lastname

    @lastname.setter
    def lastname(self, lastname: str):
        self.__lastname = lastname

    @property
    def firstname(self) -> str:
        return self.__firstname

    @firstname.setter
    def firstname(self, firstname: str):
        self.__firstname = firstname

    @property
    def password(self) -> str:
        return self.__password

    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def db_config_User(self):
        return self.__db_config_User

    @db_config_User.setter
    def db_config_User(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_db_config_User__db_config_User", None)
        self.__db_config_User = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "config_Role"):
                    opp_val = getattr(item, "config_Role", None)
                    
                    if opp_val == self:
                        setattr(item, "config_Role", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "config_Role"):
                    opp_val = getattr(item, "config_Role", None)
                    
                    setattr(item, "config_Role", self)
                    

class db_config_Role(ServerResource):

    pass
class db_config_SafletProject(ServerResource):

    def __init__(self, enabled: bool, config28: set["config_Saflet"] = None, config31: set["config_Prompt"] = None):
        self.enabled = enabled
        self.config28 = config28 if config28 is not None else set()
        self.config31 = config31 if config31 is not None else set()
        
    @property
    def enabled(self) -> bool:
        return self.__enabled

    @enabled.setter
    def enabled(self, enabled: bool):
        self.__enabled = enabled

    @property
    def config28(self):
        return self.__config28

    @config28.setter
    def config28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_db_config_SafletProject__config28", None)
        self.__config28 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "server29"):
                    opp_val = getattr(item, "server29", None)
                    
                    if opp_val == self:
                        setattr(item, "server29", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "server29"):
                    opp_val = getattr(item, "server29", None)
                    
                    setattr(item, "server29", self)
                    

    @property
    def config31(self):
        return self.__config31

    @config31.setter
    def config31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_db_config_SafletProject__config31", None)
        self.__config31 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "server32"):
                    opp_val = getattr(item, "server32", None)
                    
                    if opp_val == self:
                        setattr(item, "server32", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "server32"):
                    opp_val = getattr(item, "server32", None)
                    
                    setattr(item, "server32", self)
                    

class db_config_Saflet(ServerResource):

    def __init__(self, code: str, subsystemId: str, config: "config_SafletProject" = None):
        self.code = code
        self.subsystemId = subsystemId
        self.config = config
        
    @property
    def subsystemId(self) -> str:
        return self.__subsystemId

    @subsystemId.setter
    def subsystemId(self, subsystemId: str):
        self.__subsystemId = subsystemId

    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def config(self):
        return self.__config

    @config.setter
    def config(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_db_config_Saflet__config", None)
        self.__config = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "server"):
                opp_val = getattr(old_value, "server", None)
                if opp_val == self:
                    setattr(old_value, "server", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "server"):
                opp_val = getattr(value, "server", None)
                setattr(value, "server", self)

class db_config_TelephonySubsystem(ServerResource):

    def __init__(self, hostname: str, running: bool, private: bool, visibleSafiServerIP: str, enabled: bool, managerName: str, managerPassword: str, managerPort: int, versionId: str, promptDirectory: str, platformId: str, db_config_TelephonySubsystem: "config_SafiServer" = None):
        self.hostname = hostname
        self.running = running
        self.private = private
        self.visibleSafiServerIP = visibleSafiServerIP
        self.enabled = enabled
        self.managerName = managerName
        self.managerPassword = managerPassword
        self.managerPort = managerPort
        self.versionId = versionId
        self.promptDirectory = promptDirectory
        self.platformId = platformId
        self.db_config_TelephonySubsystem = db_config_TelephonySubsystem
        
    @property
    def visibleSafiServerIP(self) -> str:
        return self.__visibleSafiServerIP

    @visibleSafiServerIP.setter
    def visibleSafiServerIP(self, visibleSafiServerIP: str):
        self.__visibleSafiServerIP = visibleSafiServerIP

    @property
    def managerName(self) -> str:
        return self.__managerName

    @managerName.setter
    def managerName(self, managerName: str):
        self.__managerName = managerName

    @property
    def hostname(self) -> str:
        return self.__hostname

    @hostname.setter
    def hostname(self, hostname: str):
        self.__hostname = hostname

    @property
    def private(self) -> bool:
        return self.__private

    @private.setter
    def private(self, private: bool):
        self.__private = private

    @property
    def platformId(self) -> str:
        return self.__platformId

    @platformId.setter
    def platformId(self, platformId: str):
        self.__platformId = platformId

    @property
    def versionId(self) -> str:
        return self.__versionId

    @versionId.setter
    def versionId(self, versionId: str):
        self.__versionId = versionId

    @property
    def promptDirectory(self) -> str:
        return self.__promptDirectory

    @promptDirectory.setter
    def promptDirectory(self, promptDirectory: str):
        self.__promptDirectory = promptDirectory

    @property
    def managerPassword(self) -> str:
        return self.__managerPassword

    @managerPassword.setter
    def managerPassword(self, managerPassword: str):
        self.__managerPassword = managerPassword

    @property
    def running(self) -> bool:
        return self.__running

    @running.setter
    def running(self, running: bool):
        self.__running = running

    @property
    def enabled(self) -> bool:
        return self.__enabled

    @enabled.setter
    def enabled(self, enabled: bool):
        self.__enabled = enabled

    @property
    def managerPort(self) -> int:
        return self.__managerPort

    @managerPort.setter
    def managerPort(self, managerPort: int):
        self.__managerPort = managerPort

    @property
    def db_config_TelephonySubsystem(self):
        return self.__db_config_TelephonySubsystem

    @db_config_TelephonySubsystem.setter
    def db_config_TelephonySubsystem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_db_config_TelephonySubsystem__db_config_TelephonySubsystem", None)
        self.__db_config_TelephonySubsystem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "config_SafiServer"):
                opp_val = getattr(old_value, "config_SafiServer", None)
                if opp_val == self:
                    setattr(old_value, "config_SafiServer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "config_SafiServer"):
                opp_val = getattr(value, "config_SafiServer", None)
                setattr(value, "config_SafiServer", self)

class db_config_Prompt(ServerResource):

    def __init__(self, system: bool, extension: str, config34: "config_SafletProject" = None):
        self.system = system
        self.extension = extension
        self.config34 = config34
        
    @property
    def extension(self) -> str:
        return self.__extension

    @extension.setter
    def extension(self, extension: str):
        self.__extension = extension

    @property
    def system(self) -> bool:
        return self.__system

    @system.setter
    def system(self, system: bool):
        self.__system = system

    @property
    def config34(self):
        return self.__config34

    @config34.setter
    def config34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_db_config_Prompt__config34", None)
        self.__config34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "server35"):
                opp_val = getattr(old_value, "server35", None)
                if opp_val == self:
                    setattr(old_value, "server35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "server35"):
                opp_val = getattr(value, "server35", None)
                setattr(value, "server35", self)

class db_config_Entitlement(ServerResource):

    pass
class db_config_SafiServer(ServerResource):

    def __init__(self, bindIP: str, managementPort: int, running: bool, debug: bool, dbPort: int, db_config_SafiServer: "config_User" = None, db_config_SafiServer22: set["config_User"] = None):
        self.bindIP = bindIP
        self.managementPort = managementPort
        self.running = running
        self.debug = debug
        self.dbPort = dbPort
        self.db_config_SafiServer = db_config_SafiServer
        self.db_config_SafiServer22 = db_config_SafiServer22 if db_config_SafiServer22 is not None else set()
        
    @property
    def bindIP(self) -> str:
        return self.__bindIP

    @bindIP.setter
    def bindIP(self, bindIP: str):
        self.__bindIP = bindIP

    @property
    def dbPort(self) -> int:
        return self.__dbPort

    @dbPort.setter
    def dbPort(self, dbPort: int):
        self.__dbPort = dbPort

    @property
    def debug(self) -> bool:
        return self.__debug

    @debug.setter
    def debug(self, debug: bool):
        self.__debug = debug

    @property
    def running(self) -> bool:
        return self.__running

    @running.setter
    def running(self, running: bool):
        self.__running = running

    @property
    def managementPort(self) -> int:
        return self.__managementPort

    @managementPort.setter
    def managementPort(self, managementPort: int):
        self.__managementPort = managementPort

    @property
    def db_config_SafiServer(self):
        return self.__db_config_SafiServer

    @db_config_SafiServer.setter
    def db_config_SafiServer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_db_config_SafiServer__db_config_SafiServer", None)
        self.__db_config_SafiServer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "config_User20"):
                opp_val = getattr(old_value, "config_User20", None)
                if opp_val == self:
                    setattr(old_value, "config_User20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "config_User20"):
                opp_val = getattr(value, "config_User20", None)
                setattr(value, "config_User20", self)

    @property
    def db_config_SafiServer22(self):
        return self.__db_config_SafiServer22

    @db_config_SafiServer22.setter
    def db_config_SafiServer22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_db_config_SafiServer__db_config_SafiServer22", None)
        self.__db_config_SafiServer22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "config_User23"):
                    opp_val = getattr(item, "config_User23", None)
                    
                    if opp_val == self:
                        setattr(item, "config_User23", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "config_User23"):
                    opp_val = getattr(item, "config_User23", None)
                    
                    setattr(item, "config_User23", self)
                    

class config_User:

    pass
class db_Variable:

    def __init__(self, type: str, scope: str, name: str, defaultValue: str):
        self.type = type
        self.scope = scope
        self.name = name
        self.defaultValue = defaultValue
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def defaultValue(self) -> str:
        return self.__defaultValue

    @defaultValue.setter
    def defaultValue(self, defaultValue: str):
        self.__defaultValue = defaultValue

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def scope(self) -> str:
        return self.__scope

    @scope.setter
    def scope(self, scope: str):
        self.__scope = scope

class db_config_ServerResource:

    def __init__(self, description: str, name: str, lastModified: date, lastUpdated: date, id: int, db_config_ServerResource: "config_User" = None, db_config_ServerResource17: "config_User" = None):
        self.description = description
        self.name = name
        self.lastModified = lastModified
        self.lastUpdated = lastUpdated
        self.id = id
        self.db_config_ServerResource = db_config_ServerResource
        self.db_config_ServerResource17 = db_config_ServerResource17
        
    @property
    def lastUpdated(self) -> date:
        return self.__lastUpdated

    @lastUpdated.setter
    def lastUpdated(self, lastUpdated: date):
        self.__lastUpdated = lastUpdated

    @property
    def lastModified(self) -> date:
        return self.__lastModified

    @lastModified.setter
    def lastModified(self, lastModified: date):
        self.__lastModified = lastModified

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def db_config_ServerResource(self):
        return self.__db_config_ServerResource

    @db_config_ServerResource.setter
    def db_config_ServerResource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_db_config_ServerResource__db_config_ServerResource", None)
        self.__db_config_ServerResource = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "config_User"):
                opp_val = getattr(old_value, "config_User", None)
                if opp_val == self:
                    setattr(old_value, "config_User", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "config_User"):
                opp_val = getattr(value, "config_User", None)
                setattr(value, "config_User", self)

    @property
    def db_config_ServerResource17(self):
        return self.__db_config_ServerResource17

    @db_config_ServerResource17.setter
    def db_config_ServerResource17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_db_config_ServerResource__db_config_ServerResource17", None)
        self.__db_config_ServerResource17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "config_User18"):
                opp_val = getattr(old_value, "config_User18", None)
                if opp_val == self:
                    setattr(old_value, "config_User18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "config_User18"):
                opp_val = getattr(value, "config_User18", None)
                setattr(value, "config_User18", self)

class db_DBResource(ABC):

    def __init__(self, name: str, lastModified: date, lastUpdated: date, id: int):
        self.name = name
        self.lastModified = lastModified
        self.lastUpdated = lastUpdated
        self.id = id
        
    @property
    def lastModified(self) -> date:
        return self.__lastModified

    @lastModified.setter
    def lastModified(self, lastModified: date):
        self.__lastModified = lastModified

    @property
    def lastUpdated(self) -> date:
        return self.__lastUpdated

    @lastUpdated.setter
    def lastUpdated(self, lastUpdated: date):
        self.__lastUpdated = lastUpdated

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class DBResource:

    pass
class db_SafiResultSet(DBResource):

    def __init__(self, scrollMode: str, holdabilityMode: str, useCache: bool, scrollable: bool, readOnly: bool, SafiResultSet: "db_Query" = None, resultSets: "db_Query" = None):
        self.scrollMode = scrollMode
        self.holdabilityMode = holdabilityMode
        self.useCache = useCache
        self.scrollable = scrollable
        self.readOnly = readOnly
        self.SafiResultSet = SafiResultSet
        self.resultSets = resultSets
        
    @property
    def holdabilityMode(self) -> str:
        return self.__holdabilityMode

    @holdabilityMode.setter
    def holdabilityMode(self, holdabilityMode: str):
        self.__holdabilityMode = holdabilityMode

    @property
    def useCache(self) -> bool:
        return self.__useCache

    @useCache.setter
    def useCache(self, useCache: bool):
        self.__useCache = useCache

    @property
    def scrollable(self) -> bool:
        return self.__scrollable

    @scrollable.setter
    def scrollable(self, scrollable: bool):
        self.__scrollable = scrollable

    @property
    def readOnly(self) -> bool:
        return self.__readOnly

    @readOnly.setter
    def readOnly(self, readOnly: bool):
        self.__readOnly = readOnly

    @property
    def scrollMode(self) -> str:
        return self.__scrollMode

    @scrollMode.setter
    def scrollMode(self, scrollMode: str):
        self.__scrollMode = scrollMode

    @property
    def resultSets(self):
        return self.__resultSets

    @resultSets.setter
    def resultSets(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_db_SafiResultSet__resultSets", None)
        self.__resultSets = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Query14"):
                opp_val = getattr(old_value, "Query14", None)
                if opp_val == self:
                    setattr(old_value, "Query14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Query14"):
                opp_val = getattr(value, "Query14", None)
                setattr(value, "Query14", self)

    @property
    def SafiResultSet(self):
        return self.__SafiResultSet

    @SafiResultSet.setter
    def SafiResultSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_db_SafiResultSet__SafiResultSet", None)
        self.__SafiResultSet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "query8"):
                opp_val = getattr(old_value, "query8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "query8"):
                opp_val = getattr(value, "query8", None)
                if opp_val is None:
                    setattr(value, "query8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class db_SafiDriverManager(DBResource):

    def __init__(self, SafiDriverManager: "db_DBDriver" = None, driverManager: set["db_DBDriver"] = None):
        self.SafiDriverManager = SafiDriverManager
        self.driverManager = driverManager if driverManager is not None else set()
        
    @property
    def driverManager(self):
        return self.__driverManager

    @driverManager.setter
    def driverManager(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_db_SafiDriverManager__driverManager", None)
        self.__driverManager = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DBDriver12"):
                    opp_val = getattr(item, "DBDriver12", None)
                    
                    if opp_val == self:
                        setattr(item, "DBDriver12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DBDriver12"):
                    opp_val = getattr(item, "DBDriver12", None)
                    
                    setattr(item, "DBDriver12", self)
                    

    @property
    def SafiDriverManager(self):
        return self.__SafiDriverManager

    @SafiDriverManager.setter
    def SafiDriverManager(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_db_SafiDriverManager__SafiDriverManager", None)
        self.__SafiDriverManager = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drivers"):
                opp_val = getattr(old_value, "drivers", None)
                if opp_val == self:
                    setattr(old_value, "drivers", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drivers"):
                opp_val = getattr(value, "drivers", None)
                setattr(value, "drivers", self)

    def getDriver(self, name: str) -> str:
        # TODO: Implement getDriver method
        pass

class db_QueryParameter(DBResource):

    def __init__(self, dataType: str, QueryParameter: "db_Query" = None, parameters: "db_Query" = None):
        self.dataType = dataType
        self.QueryParameter = QueryParameter
        self.parameters = parameters
        
    @property
    def dataType(self) -> str:
        return self.__dataType

    @dataType.setter
    def dataType(self, dataType: str):
        self.__dataType = dataType

    @property
    def parameters(self):
        return self.__parameters

    @parameters.setter
    def parameters(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_db_QueryParameter__parameters", None)
        self.__parameters = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Query10"):
                opp_val = getattr(old_value, "Query10", None)
                if opp_val == self:
                    setattr(old_value, "Query10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Query10"):
                opp_val = getattr(value, "Query10", None)
                setattr(value, "Query10", self)

    @property
    def QueryParameter(self):
        return self.__QueryParameter

    @QueryParameter.setter
    def QueryParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_db_QueryParameter__QueryParameter", None)
        self.__QueryParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "query"):
                opp_val = getattr(old_value, "query", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "query"):
                opp_val = getattr(value, "query", None)
                if opp_val is None:
                    setattr(value, "query", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class db_DBConnection(DBResource):

    def __init__(self, url: str, user: str, password: str, loginTimeout: int, properties: str, transactionMode: str, minPoolSize: int, maxPoolSize: int, acquireIncrement: int, maxIdleTime: int, connections: "db_DBDriver" = None, connection: set["db_Query"] = None, DBConnection: "db_DBDriver" = None, DBConnection6: "db_Query" = None):
        self.url = url
        self.user = user
        self.password = password
        self.loginTimeout = loginTimeout
        self.properties = properties
        self.transactionMode = transactionMode
        self.minPoolSize = minPoolSize
        self.maxPoolSize = maxPoolSize
        self.acquireIncrement = acquireIncrement
        self.maxIdleTime = maxIdleTime
        self.connections = connections
        self.connection = connection if connection is not None else set()
        self.DBConnection = DBConnection
        self.DBConnection6 = DBConnection6
        
    @property
    def properties(self) -> str:
        return self.__properties

    @properties.setter
    def properties(self, properties: str):
        self.__properties = properties

    @property
    def maxIdleTime(self) -> int:
        return self.__maxIdleTime

    @maxIdleTime.setter
    def maxIdleTime(self, maxIdleTime: int):
        self.__maxIdleTime = maxIdleTime

    @property
    def transactionMode(self) -> str:
        return self.__transactionMode

    @transactionMode.setter
    def transactionMode(self, transactionMode: str):
        self.__transactionMode = transactionMode

    @property
    def acquireIncrement(self) -> int:
        return self.__acquireIncrement

    @acquireIncrement.setter
    def acquireIncrement(self, acquireIncrement: int):
        self.__acquireIncrement = acquireIncrement

    @property
    def url(self) -> str:
        return self.__url

    @url.setter
    def url(self, url: str):
        self.__url = url

    @property
    def password(self) -> str:
        return self.__password

    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def minPoolSize(self) -> int:
        return self.__minPoolSize

    @minPoolSize.setter
    def minPoolSize(self, minPoolSize: int):
        self.__minPoolSize = minPoolSize

    @property
    def user(self) -> str:
        return self.__user

    @user.setter
    def user(self, user: str):
        self.__user = user

    @property
    def maxPoolSize(self) -> int:
        return self.__maxPoolSize

    @maxPoolSize.setter
    def maxPoolSize(self, maxPoolSize: int):
        self.__maxPoolSize = maxPoolSize

    @property
    def loginTimeout(self) -> int:
        return self.__loginTimeout

    @loginTimeout.setter
    def loginTimeout(self, loginTimeout: int):
        self.__loginTimeout = loginTimeout

    @property
    def DBConnection(self):
        return self.__DBConnection

    @DBConnection.setter
    def DBConnection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_db_DBConnection__DBConnection", None)
        self.__DBConnection = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "driver"):
                opp_val = getattr(old_value, "driver", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "driver"):
                opp_val = getattr(value, "driver", None)
                if opp_val is None:
                    setattr(value, "driver", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def connections(self):
        return self.__connections

    @connections.setter
    def connections(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_db_DBConnection__connections", None)
        self.__connections = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DBDriver"):
                opp_val = getattr(old_value, "DBDriver", None)
                if opp_val == self:
                    setattr(old_value, "DBDriver", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DBDriver"):
                opp_val = getattr(value, "DBDriver", None)
                setattr(value, "DBDriver", self)

    @property
    def connection(self):
        return self.__connection

    @connection.setter
    def connection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_db_DBConnection__connection", None)
        self.__connection = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Query"):
                    opp_val = getattr(item, "Query", None)
                    
                    if opp_val == self:
                        setattr(item, "Query", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Query"):
                    opp_val = getattr(item, "Query", None)
                    
                    setattr(item, "Query", self)
                    

    @property
    def DBConnection6(self):
        return self.__DBConnection6

    @DBConnection6.setter
    def DBConnection6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_db_DBConnection__DBConnection6", None)
        self.__DBConnection6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "queries"):
                opp_val = getattr(old_value, "queries", None)
                if opp_val == self:
                    setattr(old_value, "queries", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "queries"):
                opp_val = getattr(value, "queries", None)
                setattr(value, "queries", self)

    def getQuery(self, name: str) -> str:
        # TODO: Implement getQuery method
        pass

class db_Query(DBResource):

    def __init__(self, querySql: str, catalog: str, queryType: str, Query: "db_DBConnection" = None, query: set["db_QueryParameter"] = None, queries: "db_DBConnection" = None, query8: set["db_SafiResultSet"] = None, Query10: "db_QueryParameter" = None, Query14: "db_SafiResultSet" = None):
        self.querySql = querySql
        self.catalog = catalog
        self.queryType = queryType
        self.Query = Query
        self.query = query if query is not None else set()
        self.queries = queries
        self.query8 = query8 if query8 is not None else set()
        self.Query10 = Query10
        self.Query14 = Query14
        
    @property
    def queryType(self) -> str:
        return self.__queryType

    @queryType.setter
    def queryType(self, queryType: str):
        self.__queryType = queryType

    @property
    def catalog(self) -> str:
        return self.__catalog

    @catalog.setter
    def catalog(self, catalog: str):
        self.__catalog = catalog

    @property
    def querySql(self) -> str:
        return self.__querySql

    @querySql.setter
    def querySql(self, querySql: str):
        self.__querySql = querySql

    @property
    def query8(self):
        return self.__query8

    @query8.setter
    def query8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_db_Query__query8", None)
        self.__query8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SafiResultSet"):
                    opp_val = getattr(item, "SafiResultSet", None)
                    
                    if opp_val == self:
                        setattr(item, "SafiResultSet", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SafiResultSet"):
                    opp_val = getattr(item, "SafiResultSet", None)
                    
                    setattr(item, "SafiResultSet", self)
                    

    @property
    def Query10(self):
        return self.__Query10

    @Query10.setter
    def Query10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_db_Query__Query10", None)
        self.__Query10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parameters"):
                opp_val = getattr(old_value, "parameters", None)
                if opp_val == self:
                    setattr(old_value, "parameters", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parameters"):
                opp_val = getattr(value, "parameters", None)
                setattr(value, "parameters", self)

    @property
    def query(self):
        return self.__query

    @query.setter
    def query(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_db_Query__query", None)
        self.__query = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "QueryParameter"):
                    opp_val = getattr(item, "QueryParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "QueryParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "QueryParameter"):
                    opp_val = getattr(item, "QueryParameter", None)
                    
                    setattr(item, "QueryParameter", self)
                    

    @property
    def Query(self):
        return self.__Query

    @Query.setter
    def Query(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_db_Query__Query", None)
        self.__Query = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "connection"):
                opp_val = getattr(old_value, "connection", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "connection"):
                opp_val = getattr(value, "connection", None)
                if opp_val is None:
                    setattr(value, "connection", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def queries(self):
        return self.__queries

    @queries.setter
    def queries(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_db_Query__queries", None)
        self.__queries = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DBConnection6"):
                opp_val = getattr(old_value, "DBConnection6", None)
                if opp_val == self:
                    setattr(old_value, "DBConnection6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DBConnection6"):
                opp_val = getattr(value, "DBConnection6", None)
                setattr(value, "DBConnection6", self)

    @property
    def Query14(self):
        return self.__Query14

    @Query14.setter
    def Query14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_db_Query__Query14", None)
        self.__Query14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "resultSets"):
                opp_val = getattr(old_value, "resultSets", None)
                if opp_val == self:
                    setattr(old_value, "resultSets", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "resultSets"):
                opp_val = getattr(value, "resultSets", None)
                setattr(value, "resultSets", self)

    def getResultSet(self, name: str) -> str:
        # TODO: Implement getResultSet method
        pass

    def getParameter(self, name: str) -> str:
        # TODO: Implement getParameter method
        pass

    def getParameter(self, index: int) -> str:
        # TODO: Implement getParameter method
        pass

class db_DBDriver(DBResource):

    def __init__(self, exampleUrl: str, jars: str, default: bool, guideUrl: str, websiteUrl: str, defaultPort: int, urlRegexPattern: str, driverClassName: str, pooling: bool, DBDriver: "db_DBConnection" = None, driver: set["db_DBConnection"] = None, drivers: "db_SafiDriverManager" = None, DBDriver12: "db_SafiDriverManager" = None):
        self.exampleUrl = exampleUrl
        self.jars = jars
        self.default = default
        self.guideUrl = guideUrl
        self.websiteUrl = websiteUrl
        self.defaultPort = defaultPort
        self.urlRegexPattern = urlRegexPattern
        self.driverClassName = driverClassName
        self.pooling = pooling
        self.DBDriver = DBDriver
        self.driver = driver if driver is not None else set()
        self.drivers = drivers
        self.DBDriver12 = DBDriver12
        
    @property
    def guideUrl(self) -> str:
        return self.__guideUrl

    @guideUrl.setter
    def guideUrl(self, guideUrl: str):
        self.__guideUrl = guideUrl

    @property
    def websiteUrl(self) -> str:
        return self.__websiteUrl

    @websiteUrl.setter
    def websiteUrl(self, websiteUrl: str):
        self.__websiteUrl = websiteUrl

    @property
    def jars(self) -> str:
        return self.__jars

    @jars.setter
    def jars(self, jars: str):
        self.__jars = jars

    @property
    def urlRegexPattern(self) -> str:
        return self.__urlRegexPattern

    @urlRegexPattern.setter
    def urlRegexPattern(self, urlRegexPattern: str):
        self.__urlRegexPattern = urlRegexPattern

    @property
    def defaultPort(self) -> int:
        return self.__defaultPort

    @defaultPort.setter
    def defaultPort(self, defaultPort: int):
        self.__defaultPort = defaultPort

    @property
    def driverClassName(self) -> str:
        return self.__driverClassName

    @driverClassName.setter
    def driverClassName(self, driverClassName: str):
        self.__driverClassName = driverClassName

    @property
    def default(self) -> bool:
        return self.__default

    @default.setter
    def default(self, default: bool):
        self.__default = default

    @property
    def pooling(self) -> bool:
        return self.__pooling

    @pooling.setter
    def pooling(self, pooling: bool):
        self.__pooling = pooling

    @property
    def exampleUrl(self) -> str:
        return self.__exampleUrl

    @exampleUrl.setter
    def exampleUrl(self, exampleUrl: str):
        self.__exampleUrl = exampleUrl

    @property
    def driver(self):
        return self.__driver

    @driver.setter
    def driver(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_db_DBDriver__driver", None)
        self.__driver = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DBConnection"):
                    opp_val = getattr(item, "DBConnection", None)
                    
                    if opp_val == self:
                        setattr(item, "DBConnection", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DBConnection"):
                    opp_val = getattr(item, "DBConnection", None)
                    
                    setattr(item, "DBConnection", self)
                    

    @property
    def drivers(self):
        return self.__drivers

    @drivers.setter
    def drivers(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_db_DBDriver__drivers", None)
        self.__drivers = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SafiDriverManager"):
                opp_val = getattr(old_value, "SafiDriverManager", None)
                if opp_val == self:
                    setattr(old_value, "SafiDriverManager", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SafiDriverManager"):
                opp_val = getattr(value, "SafiDriverManager", None)
                setattr(value, "SafiDriverManager", self)

    @property
    def DBDriver12(self):
        return self.__DBDriver12

    @DBDriver12.setter
    def DBDriver12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_db_DBDriver__DBDriver12", None)
        self.__DBDriver12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "driverManager"):
                opp_val = getattr(old_value, "driverManager", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "driverManager"):
                opp_val = getattr(value, "driverManager", None)
                if opp_val is None:
                    setattr(value, "driverManager", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def DBDriver(self):
        return self.__DBDriver

    @DBDriver.setter
    def DBDriver(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_db_DBDriver__DBDriver", None)
        self.__DBDriver = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "connections"):
                opp_val = getattr(old_value, "connections", None)
                if opp_val == self:
                    setattr(old_value, "connections", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "connections"):
                opp_val = getattr(value, "connections", None)
                setattr(value, "connections", self)

    def getConnection(self, name: str) -> str:
        # TODO: Implement getConnection method
        pass
