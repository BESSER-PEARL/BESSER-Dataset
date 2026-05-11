from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class RSScrollMode(Enum):
    ForwardOnly = "ForwardOnly"
    ScrollInsensitive = "ScrollInsensitive"
    ScrollSensitive = "ScrollSensitive"
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
class RSHoldabilityMode(Enum):
    HoldCursorsOverCommit = "HoldCursorsOverCommit"
    CloseCursorsOverCommit = "CloseCursorsOverCommit"
class VariableScope(Enum):
    Local = "Local"
    Global = "Global"
    Runtime = "Runtime"
class VariableType(Enum):
    Datetime = "Datetime"
    Date = "Date"
    Time = "Time"
    Object = "Object"
    Boolean = "Boolean"
    Array = "Array"
    Text = "Text"
    Integer = "Integer"
    Decimal = "Decimal"
class TransactionMode(Enum):
    None_ = "None_"
    ReadCommitted = "ReadCommitted"
    ReadUncommitted = "ReadUncommitted"
    RepeatableRead = "RepeatableRead"
    Serializable = "Serializable"
class SynchMode(Enum):
    ReadOnly = "ReadOnly"
    Synch = "Synch"
class QueryType(Enum):
    Select = "Select"
    Update = "Update"
    SPSelect = "SPSelect"
    SPUpdate = "SPUpdate"


############################################
# Definition of Classes
############################################

class config_SafiServer:

    pass
class db_config_SFTPInfo(ABC):

    def __init__(self, sftpUser: str, sftpPassword: str, sftpPort: int):
        self.sftpUser = sftpUser
        self.sftpPassword = sftpPassword
        self.sftpPort = sftpPort
        
        pass
    @property
    def sftpUser(self):
        return self.__sftpUser

    @sftpUser.setter
    def sftpUser(self, sftpUser: str):
        self.__sftpUser = sftpUser


    @property
    def sftpPort(self):
        return self.__sftpPort

    @sftpPort.setter
    def sftpPort(self, sftpPort: int):
        self.__sftpPort = sftpPort


    @property
    def sftpPassword(self):
        return self.__sftpPassword

    @sftpPassword.setter
    def sftpPassword(self, sftpPassword: str):
        self.__sftpPassword = sftpPassword


class config_Prompt:

    pass
class config_Saflet:

    pass
class config_SafletProject:

    pass
class config_Role:

    pass
class config_Entitlement:

    pass
class ServerResource:

    pass
class db_config_User(ServerResource):

    def __init__(self, password: str, firstname: str, lastname: str, db_config_User: set["config_Role"] = None):
        self.password = password
        self.firstname = firstname
        self.lastname = lastname
        self.db_config_User = db_config_User if db_config_User is not None else set()
        
        pass
    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password: str):
        self.__password = password


    @property
    def lastname(self):
        return self.__lastname

    @lastname.setter
    def lastname(self, lastname: str):
        self.__lastname = lastname


    @property
    def firstname(self):
        return self.__firstname

    @firstname.setter
    def firstname(self, firstname: str):
        self.__firstname = firstname


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
                    

class db_config_SafletProject(ServerResource):

    def __init__(self, enabled: bool, project: set["config_Saflet"] = None, project29: set["config_Prompt"] = None):
        self.enabled = enabled
        self.project = project if project is not None else set()
        self.project29 = project29 if project29 is not None else set()
        
        pass
    @property
    def enabled(self):
        return self.__enabled

    @enabled.setter
    def enabled(self, enabled: bool):
        self.__enabled = enabled


    @property
    def project29(self):
        return self.__project29

    @project29.setter
    def project29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_db_config_SafletProject__project29", None)
        self.__project29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Prompt"):
                    opp_val = getattr(item, "Prompt", None)
                    
                    if opp_val == self:
                        setattr(item, "Prompt", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Prompt"):
                    opp_val = getattr(item, "Prompt", None)
                    
                    setattr(item, "Prompt", self)
                    

    @property
    def project(self):
        return self.__project

    @project.setter
    def project(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_db_config_SafletProject__project", None)
        self.__project = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Saflet"):
                    opp_val = getattr(item, "Saflet", None)
                    
                    if opp_val == self:
                        setattr(item, "Saflet", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Saflet"):
                    opp_val = getattr(item, "Saflet", None)
                    
                    setattr(item, "Saflet", self)
                    

class db_config_Prompt(ServerResource):

    def __init__(self, system: bool, extension: str, prompts: "config_SafletProject" = None):
        self.system = system
        self.extension = extension
        self.prompts = prompts
        
        pass
    @property
    def extension(self):
        return self.__extension

    @extension.setter
    def extension(self, extension: str):
        self.__extension = extension


    @property
    def system(self):
        return self.__system

    @system.setter
    def system(self, system: bool):
        self.__system = system


    @property
    def prompts(self):
        return self.__prompts

    @prompts.setter
    def prompts(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_db_config_Prompt__prompts", None)
        self.__prompts = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SafletProject31"):
                opp_val = getattr(old_value, "SafletProject31", None)
                if opp_val == self:
                    setattr(old_value, "SafletProject31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SafletProject31"):
                opp_val = getattr(value, "SafletProject31", None)
                setattr(value, "SafletProject31", self)

class db_config_Saflet(ServerResource):

    def __init__(self, code: str, subsystemId: str, saflets: "config_SafletProject" = None):
        self.code = code
        self.subsystemId = subsystemId
        self.saflets = saflets
        
        pass
    @property
    def code(self):
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code


    @property
    def subsystemId(self):
        return self.__subsystemId

    @subsystemId.setter
    def subsystemId(self, subsystemId: str):
        self.__subsystemId = subsystemId


    @property
    def saflets(self):
        return self.__saflets

    @saflets.setter
    def saflets(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_db_config_Saflet__saflets", None)
        self.__saflets = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SafletProject"):
                opp_val = getattr(old_value, "SafletProject", None)
                if opp_val == self:
                    setattr(old_value, "SafletProject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SafletProject"):
                opp_val = getattr(value, "SafletProject", None)
                setattr(value, "SafletProject", self)

class db_config_Entitlement(ServerResource):

    pass
class db_config_TelephonySubsystem(ServerResource):

    def __init__(self, running: bool, private: bool, visibleSafiServerIP: str, enabled: bool, managerName: str, managerPassword: str, managerPort: int, versionId: str, promptDirectory: str, platformId: str, hostname: str, db_config_TelephonySubsystem: "config_SafiServer" = None):
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
        self.hostname = hostname
        self.db_config_TelephonySubsystem = db_config_TelephonySubsystem
        
        pass
    @property
    def enabled(self):
        return self.__enabled

    @enabled.setter
    def enabled(self, enabled: bool):
        self.__enabled = enabled


    @property
    def managerPassword(self):
        return self.__managerPassword

    @managerPassword.setter
    def managerPassword(self, managerPassword: str):
        self.__managerPassword = managerPassword


    @property
    def promptDirectory(self):
        return self.__promptDirectory

    @promptDirectory.setter
    def promptDirectory(self, promptDirectory: str):
        self.__promptDirectory = promptDirectory


    @property
    def running(self):
        return self.__running

    @running.setter
    def running(self, running: bool):
        self.__running = running


    @property
    def managerName(self):
        return self.__managerName

    @managerName.setter
    def managerName(self, managerName: str):
        self.__managerName = managerName


    @property
    def private(self):
        return self.__private

    @private.setter
    def private(self, private: bool):
        self.__private = private


    @property
    def visibleSafiServerIP(self):
        return self.__visibleSafiServerIP

    @visibleSafiServerIP.setter
    def visibleSafiServerIP(self, visibleSafiServerIP: str):
        self.__visibleSafiServerIP = visibleSafiServerIP


    @property
    def platformId(self):
        return self.__platformId

    @platformId.setter
    def platformId(self, platformId: str):
        self.__platformId = platformId


    @property
    def managerPort(self):
        return self.__managerPort

    @managerPort.setter
    def managerPort(self, managerPort: int):
        self.__managerPort = managerPort


    @property
    def hostname(self):
        return self.__hostname

    @hostname.setter
    def hostname(self, hostname: str):
        self.__hostname = hostname


    @property
    def versionId(self):
        return self.__versionId

    @versionId.setter
    def versionId(self, versionId: str):
        self.__versionId = versionId


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

class db_config_Role(ServerResource):

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
        
        pass
    @property
    def debug(self):
        return self.__debug

    @debug.setter
    def debug(self, debug: bool):
        self.__debug = debug


    @property
    def dbPort(self):
        return self.__dbPort

    @dbPort.setter
    def dbPort(self, dbPort: int):
        self.__dbPort = dbPort


    @property
    def bindIP(self):
        return self.__bindIP

    @bindIP.setter
    def bindIP(self, bindIP: str):
        self.__bindIP = bindIP


    @property
    def running(self):
        return self.__running

    @running.setter
    def running(self, running: bool):
        self.__running = running


    @property
    def managementPort(self):
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
class db_config_ServerResource:

    def __init__(self, name: str, lastModified: date, lastUpdated: date, id: int, description: str, db_config_ServerResource: "config_User" = None, db_config_ServerResource17: "config_User" = None):
        self.name = name
        self.lastModified = lastModified
        self.lastUpdated = lastUpdated
        self.id = id
        self.description = description
        self.db_config_ServerResource = db_config_ServerResource
        self.db_config_ServerResource17 = db_config_ServerResource17
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def lastModified(self):
        return self.__lastModified

    @lastModified.setter
    def lastModified(self, lastModified: date):
        self.__lastModified = lastModified


    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id


    @property
    def lastUpdated(self):
        return self.__lastUpdated

    @lastUpdated.setter
    def lastUpdated(self, lastUpdated: date):
        self.__lastUpdated = lastUpdated


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

class db_Variable:

    def __init__(self, name: str, defaultValue: str, type: str, scope: str):
        self.name = name
        self.defaultValue = defaultValue
        self.type = type
        self.scope = scope
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def scope(self):
        return self.__scope

    @scope.setter
    def scope(self, scope: str):
        self.__scope = scope


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def defaultValue(self):
        return self.__defaultValue

    @defaultValue.setter
    def defaultValue(self, defaultValue: str):
        self.__defaultValue = defaultValue


class db_DBResource(ABC):

    def __init__(self, name: str, lastModified: date, lastUpdated: date, id: int):
        self.name = name
        self.lastModified = lastModified
        self.lastUpdated = lastUpdated
        self.id = id
        
        pass
    @property
    def lastUpdated(self):
        return self.__lastUpdated

    @lastUpdated.setter
    def lastUpdated(self, lastUpdated: date):
        self.__lastUpdated = lastUpdated


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def lastModified(self):
        return self.__lastModified

    @lastModified.setter
    def lastModified(self, lastModified: date):
        self.__lastModified = lastModified


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id


class DBResource:

    pass
class db_SafiResultSet(DBResource):

    def __init__(self, useCache: bool, scrollable: bool, readOnly: bool, scrollMode: str, holdabilityMode: str, SafiResultSet: "db_Query" = None, resultSets: "db_Query" = None):
        self.useCache = useCache
        self.scrollable = scrollable
        self.readOnly = readOnly
        self.scrollMode = scrollMode
        self.holdabilityMode = holdabilityMode
        self.SafiResultSet = SafiResultSet
        self.resultSets = resultSets
        
        pass
    @property
    def readOnly(self):
        return self.__readOnly

    @readOnly.setter
    def readOnly(self, readOnly: bool):
        self.__readOnly = readOnly


    @property
    def useCache(self):
        return self.__useCache

    @useCache.setter
    def useCache(self, useCache: bool):
        self.__useCache = useCache


    @property
    def scrollMode(self):
        return self.__scrollMode

    @scrollMode.setter
    def scrollMode(self, scrollMode: str):
        self.__scrollMode = scrollMode


    @property
    def scrollable(self):
        return self.__scrollable

    @scrollable.setter
    def scrollable(self, scrollable: bool):
        self.__scrollable = scrollable


    @property
    def holdabilityMode(self):
        return self.__holdabilityMode

    @holdabilityMode.setter
    def holdabilityMode(self, holdabilityMode: str):
        self.__holdabilityMode = holdabilityMode


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

class db_QueryParameter(DBResource):

    def __init__(self, dataType: str, QueryParameter: "db_Query" = None, parameters: "db_Query" = None):
        self.dataType = dataType
        self.QueryParameter = QueryParameter
        self.parameters = parameters
        
        pass
    @property
    def dataType(self):
        return self.__dataType

    @dataType.setter
    def dataType(self, dataType: str):
        self.__dataType = dataType


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
        
        pass
    @property
    def properties(self):
        return self.__properties

    @properties.setter
    def properties(self, properties: str):
        self.__properties = properties


    @property
    def transactionMode(self):
        return self.__transactionMode

    @transactionMode.setter
    def transactionMode(self, transactionMode: str):
        self.__transactionMode = transactionMode


    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password: str):
        self.__password = password


    @property
    def loginTimeout(self):
        return self.__loginTimeout

    @loginTimeout.setter
    def loginTimeout(self, loginTimeout: int):
        self.__loginTimeout = loginTimeout


    @property
    def maxPoolSize(self):
        return self.__maxPoolSize

    @maxPoolSize.setter
    def maxPoolSize(self, maxPoolSize: int):
        self.__maxPoolSize = maxPoolSize


    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, url: str):
        self.__url = url


    @property
    def acquireIncrement(self):
        return self.__acquireIncrement

    @acquireIncrement.setter
    def acquireIncrement(self, acquireIncrement: int):
        self.__acquireIncrement = acquireIncrement


    @property
    def minPoolSize(self):
        return self.__minPoolSize

    @minPoolSize.setter
    def minPoolSize(self, minPoolSize: int):
        self.__minPoolSize = minPoolSize


    @property
    def user(self):
        return self.__user

    @user.setter
    def user(self, user: str):
        self.__user = user


    @property
    def maxIdleTime(self):
        return self.__maxIdleTime

    @maxIdleTime.setter
    def maxIdleTime(self, maxIdleTime: int):
        self.__maxIdleTime = maxIdleTime


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

    def getQuery(self, db_name) :
        # TODO: Implement getQuery method
        pass

class db_SafiDriverManager(DBResource):

    def __init__(self, SafiDriverManager: "db_DBDriver" = None, driverManager: set["db_DBDriver"] = None):
        self.SafiDriverManager = SafiDriverManager
        self.driverManager = driverManager if driverManager is not None else set()
        
        pass
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

    def getDriver(self, db_name) :
        # TODO: Implement getDriver method
        pass

class db_Query(DBResource):

    def __init__(self, queryType: str, querySql: str, catalog: str, Query: "db_DBConnection" = None, query: set["db_QueryParameter"] = None, queries: "db_DBConnection" = None, query8: set["db_SafiResultSet"] = None, Query10: "db_QueryParameter" = None, Query14: "db_SafiResultSet" = None):
        self.queryType = queryType
        self.querySql = querySql
        self.catalog = catalog
        self.Query = Query
        self.query = query if query is not None else set()
        self.queries = queries
        self.query8 = query8 if query8 is not None else set()
        self.Query10 = Query10
        self.Query14 = Query14
        
        pass
    @property
    def catalog(self):
        return self.__catalog

    @catalog.setter
    def catalog(self, catalog: str):
        self.__catalog = catalog


    @property
    def queryType(self):
        return self.__queryType

    @queryType.setter
    def queryType(self, queryType: str):
        self.__queryType = queryType


    @property
    def querySql(self):
        return self.__querySql

    @querySql.setter
    def querySql(self, querySql: str):
        self.__querySql = querySql


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

    def getParameter(self, db_index) :
        # TODO: Implement getParameter method
        pass

    def getResultSet(self, db_name) :
        # TODO: Implement getResultSet method
        pass

class db_DBDriver(DBResource):

    def __init__(self, driverClassName: str, pooling: bool, exampleUrl: str, jars: str, default: bool, guideUrl: str, websiteUrl: str, defaultPort: int, urlRegexPattern: str, DBDriver: "db_DBConnection" = None, driver: set["db_DBConnection"] = None, drivers: "db_SafiDriverManager" = None, DBDriver12: "db_SafiDriverManager" = None):
        self.driverClassName = driverClassName
        self.pooling = pooling
        self.exampleUrl = exampleUrl
        self.jars = jars
        self.default = default
        self.guideUrl = guideUrl
        self.websiteUrl = websiteUrl
        self.defaultPort = defaultPort
        self.urlRegexPattern = urlRegexPattern
        self.DBDriver = DBDriver
        self.driver = driver if driver is not None else set()
        self.drivers = drivers
        self.DBDriver12 = DBDriver12
        
        pass
    @property
    def urlRegexPattern(self):
        return self.__urlRegexPattern

    @urlRegexPattern.setter
    def urlRegexPattern(self, urlRegexPattern: str):
        self.__urlRegexPattern = urlRegexPattern


    @property
    def pooling(self):
        return self.__pooling

    @pooling.setter
    def pooling(self, pooling: bool):
        self.__pooling = pooling


    @property
    def websiteUrl(self):
        return self.__websiteUrl

    @websiteUrl.setter
    def websiteUrl(self, websiteUrl: str):
        self.__websiteUrl = websiteUrl


    @property
    def guideUrl(self):
        return self.__guideUrl

    @guideUrl.setter
    def guideUrl(self, guideUrl: str):
        self.__guideUrl = guideUrl


    @property
    def exampleUrl(self):
        return self.__exampleUrl

    @exampleUrl.setter
    def exampleUrl(self, exampleUrl: str):
        self.__exampleUrl = exampleUrl


    @property
    def driverClassName(self):
        return self.__driverClassName

    @driverClassName.setter
    def driverClassName(self, driverClassName: str):
        self.__driverClassName = driverClassName


    @property
    def default(self):
        return self.__default

    @default.setter
    def default(self, default: bool):
        self.__default = default


    @property
    def jars(self):
        return self.__jars

    @jars.setter
    def jars(self, jars: str):
        self.__jars = jars


    @property
    def defaultPort(self):
        return self.__defaultPort

    @defaultPort.setter
    def defaultPort(self, defaultPort: int):
        self.__defaultPort = defaultPort


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

    def getConnection(self, db_name) :
        # TODO: Implement getConnection method
        pass
