from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class ParameterType(Enum):
    AsciiStream = "AsciiStream"
    Array = "Array"
    BigDecimal = "BigDecimal"
    BinaryStream = "BinaryStream"
    Blob = "Blob"
    Boolean = "Boolean"
    Byte = "Byte"
    Bytes = "Bytes"
    CharacterStream = "CharacterStream"
    Clob = "Clob"
    Date = "Date"
    DateCalendar = "DateCalendar"
    Double = "Double"
    Float = "Float"
    Int = "Int"
    Long = "Long"
    Object = "Object"
    Ref = "Ref"
    Short = "Short"
    String = "String"
    Token = "Token"
    Time = "Time"
    TimeCalendar = "TimeCalendar"
    Timestamp = "Timestamp"
    TimeStampCalendar = "TimeStampCalendar"
    UnicodeStream = "UnicodeStream"
    URL = "URL"
class DBMS(Enum):
    MySQL = "MySQL"
    PgSQL = "PgSQL"
    HSQLDB = "HSQLDB"
    SQLite = "SQLite"
    MSAccess = "MSAccess"


############################################
# Definition of Classes
############################################

class properties_SqlGroup:

    def __init__(self, id: str, description: str, properties_SqlGroup: set["properties_SqlQuery"] = None, properties_SqlGroup24: set["properties_SqlFile"] = None, properties_SqlGroup27: set["properties_SpecificDBMSProperties"] = None, properties_SqlGroup31: "properties_SqlProperties" = None):
        self.id = id
        self.description = description
        self.properties_SqlGroup = properties_SqlGroup if properties_SqlGroup is not None else set()
        self.properties_SqlGroup24 = properties_SqlGroup24 if properties_SqlGroup24 is not None else set()
        self.properties_SqlGroup27 = properties_SqlGroup27 if properties_SqlGroup27 is not None else set()
        self.properties_SqlGroup31 = properties_SqlGroup31
        
        pass
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
    def id(self, id: str):
        self.__id = id


    @property
    def properties_SqlGroup27(self):
        return self.__properties_SqlGroup27

    @properties_SqlGroup27.setter
    def properties_SqlGroup27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_properties_SqlGroup__properties_SqlGroup27", None)
        self.__properties_SqlGroup27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "properties_SpecificDBMSProperties28"):
                    opp_val = getattr(item, "properties_SpecificDBMSProperties28", None)
                    
                    if opp_val == self:
                        setattr(item, "properties_SpecificDBMSProperties28", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "properties_SpecificDBMSProperties28"):
                    opp_val = getattr(item, "properties_SpecificDBMSProperties28", None)
                    
                    setattr(item, "properties_SpecificDBMSProperties28", self)
                    

    @property
    def properties_SqlGroup31(self):
        return self.__properties_SqlGroup31

    @properties_SqlGroup31.setter
    def properties_SqlGroup31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_properties_SqlGroup__properties_SqlGroup31", None)
        self.__properties_SqlGroup31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "properties_SqlProperties30"):
                opp_val = getattr(old_value, "properties_SqlProperties30", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "properties_SqlProperties30"):
                opp_val = getattr(value, "properties_SqlProperties30", None)
                if opp_val is None:
                    setattr(value, "properties_SqlProperties30", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def properties_SqlGroup24(self):
        return self.__properties_SqlGroup24

    @properties_SqlGroup24.setter
    def properties_SqlGroup24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_properties_SqlGroup__properties_SqlGroup24", None)
        self.__properties_SqlGroup24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "properties_SqlFile25"):
                    opp_val = getattr(item, "properties_SqlFile25", None)
                    
                    if opp_val == self:
                        setattr(item, "properties_SqlFile25", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "properties_SqlFile25"):
                    opp_val = getattr(item, "properties_SqlFile25", None)
                    
                    setattr(item, "properties_SqlFile25", self)
                    

    @property
    def properties_SqlGroup(self):
        return self.__properties_SqlGroup

    @properties_SqlGroup.setter
    def properties_SqlGroup(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_properties_SqlGroup__properties_SqlGroup", None)
        self.__properties_SqlGroup = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "properties_SqlQuery22"):
                    opp_val = getattr(item, "properties_SqlQuery22", None)
                    
                    if opp_val == self:
                        setattr(item, "properties_SqlQuery22", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "properties_SqlQuery22"):
                    opp_val = getattr(item, "properties_SqlQuery22", None)
                    
                    setattr(item, "properties_SqlQuery22", self)
                    

class Sql:

    pass
class properties_SqlParameter:

    def __init__(self, index: str, name: str, type: str, properties_SqlParameter: "properties_Sql" = None):
        self.index = index
        self.name = name
        self.type = type
        self.properties_SqlParameter = properties_SqlParameter
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def index(self):
        return self.__index

    @index.setter
    def index(self, index: str):
        self.__index = index


    @property
    def properties_SqlParameter(self):
        return self.__properties_SqlParameter

    @properties_SqlParameter.setter
    def properties_SqlParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_properties_SqlParameter__properties_SqlParameter", None)
        self.__properties_SqlParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "properties_Sql"):
                opp_val = getattr(old_value, "properties_Sql", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "properties_Sql"):
                opp_val = getattr(value, "properties_Sql", None)
                if opp_val is None:
                    setattr(value, "properties_Sql", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class properties_Sql:

    def __init__(self, id: str, hqlQuery: str, properties_Sql: set["properties_SqlParameter"] = None):
        self.id = id
        self.hqlQuery = hqlQuery
        self.properties_Sql = properties_Sql if properties_Sql is not None else set()
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def hqlQuery(self):
        return self.__hqlQuery

    @hqlQuery.setter
    def hqlQuery(self, hqlQuery: str):
        self.__hqlQuery = hqlQuery


    @property
    def properties_Sql(self):
        return self.__properties_Sql

    @properties_Sql.setter
    def properties_Sql(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_properties_Sql__properties_Sql", None)
        self.__properties_Sql = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "properties_SqlParameter"):
                    opp_val = getattr(item, "properties_SqlParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "properties_SqlParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "properties_SqlParameter"):
                    opp_val = getattr(item, "properties_SqlParameter", None)
                    
                    setattr(item, "properties_SqlParameter", self)
                    

class properties_SqlFile(Sql):

    def __init__(self, filePath: str, properties_SqlFile: "properties_SpecificDBMSProperties" = None, properties_SqlFile25: "properties_SqlGroup" = None):
        self.filePath = filePath
        self.properties_SqlFile = properties_SqlFile
        self.properties_SqlFile25 = properties_SqlFile25
        
        pass
    @property
    def filePath(self):
        return self.__filePath

    @filePath.setter
    def filePath(self, filePath: str):
        self.__filePath = filePath


    @property
    def properties_SqlFile25(self):
        return self.__properties_SqlFile25

    @properties_SqlFile25.setter
    def properties_SqlFile25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_properties_SqlFile__properties_SqlFile25", None)
        self.__properties_SqlFile25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "properties_SqlGroup24"):
                opp_val = getattr(old_value, "properties_SqlGroup24", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "properties_SqlGroup24"):
                opp_val = getattr(value, "properties_SqlGroup24", None)
                if opp_val is None:
                    setattr(value, "properties_SqlGroup24", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def properties_SqlFile(self):
        return self.__properties_SqlFile

    @properties_SqlFile.setter
    def properties_SqlFile(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_properties_SqlFile__properties_SqlFile", None)
        self.__properties_SqlFile = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "properties_SpecificDBMSProperties19"):
                opp_val = getattr(old_value, "properties_SpecificDBMSProperties19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "properties_SpecificDBMSProperties19"):
                opp_val = getattr(value, "properties_SpecificDBMSProperties19", None)
                if opp_val is None:
                    setattr(value, "properties_SpecificDBMSProperties19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class properties_SqlQuery(Sql):

    def __init__(self, queryString: str, properties_SqlQuery: "properties_SpecificDBMSProperties" = None, properties_SqlQuery22: "properties_SqlGroup" = None):
        self.queryString = queryString
        self.properties_SqlQuery = properties_SqlQuery
        self.properties_SqlQuery22 = properties_SqlQuery22
        
        pass
    @property
    def queryString(self):
        return self.__queryString

    @queryString.setter
    def queryString(self, queryString: str):
        self.__queryString = queryString


    @property
    def properties_SqlQuery22(self):
        return self.__properties_SqlQuery22

    @properties_SqlQuery22.setter
    def properties_SqlQuery22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_properties_SqlQuery__properties_SqlQuery22", None)
        self.__properties_SqlQuery22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "properties_SqlGroup"):
                opp_val = getattr(old_value, "properties_SqlGroup", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "properties_SqlGroup"):
                opp_val = getattr(value, "properties_SqlGroup", None)
                if opp_val is None:
                    setattr(value, "properties_SqlGroup", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def properties_SqlQuery(self):
        return self.__properties_SqlQuery

    @properties_SqlQuery.setter
    def properties_SqlQuery(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_properties_SqlQuery__properties_SqlQuery", None)
        self.__properties_SqlQuery = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "properties_SpecificDBMSProperties"):
                opp_val = getattr(old_value, "properties_SpecificDBMSProperties", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "properties_SpecificDBMSProperties"):
                opp_val = getattr(value, "properties_SpecificDBMSProperties", None)
                if opp_val is None:
                    setattr(value, "properties_SpecificDBMSProperties", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class properties_SpecificDBMSProperties:

    def __init__(self, dBMS: str, properties_SpecificDBMSProperties: set["properties_SqlQuery"] = None, properties_SpecificDBMSProperties19: set["properties_SqlFile"] = None, properties_SpecificDBMSProperties28: "properties_SqlGroup" = None):
        self.dBMS = dBMS
        self.properties_SpecificDBMSProperties = properties_SpecificDBMSProperties if properties_SpecificDBMSProperties is not None else set()
        self.properties_SpecificDBMSProperties19 = properties_SpecificDBMSProperties19 if properties_SpecificDBMSProperties19 is not None else set()
        self.properties_SpecificDBMSProperties28 = properties_SpecificDBMSProperties28
        
        pass
    @property
    def dBMS(self):
        return self.__dBMS

    @dBMS.setter
    def dBMS(self, dBMS: str):
        self.__dBMS = dBMS


    @property
    def properties_SpecificDBMSProperties19(self):
        return self.__properties_SpecificDBMSProperties19

    @properties_SpecificDBMSProperties19.setter
    def properties_SpecificDBMSProperties19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_properties_SpecificDBMSProperties__properties_SpecificDBMSProperties19", None)
        self.__properties_SpecificDBMSProperties19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "properties_SqlFile"):
                    opp_val = getattr(item, "properties_SqlFile", None)
                    
                    if opp_val == self:
                        setattr(item, "properties_SqlFile", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "properties_SqlFile"):
                    opp_val = getattr(item, "properties_SqlFile", None)
                    
                    setattr(item, "properties_SqlFile", self)
                    

    @property
    def properties_SpecificDBMSProperties(self):
        return self.__properties_SpecificDBMSProperties

    @properties_SpecificDBMSProperties.setter
    def properties_SpecificDBMSProperties(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_properties_SpecificDBMSProperties__properties_SpecificDBMSProperties", None)
        self.__properties_SpecificDBMSProperties = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "properties_SqlQuery"):
                    opp_val = getattr(item, "properties_SqlQuery", None)
                    
                    if opp_val == self:
                        setattr(item, "properties_SqlQuery", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "properties_SqlQuery"):
                    opp_val = getattr(item, "properties_SqlQuery", None)
                    
                    setattr(item, "properties_SqlQuery", self)
                    

    @property
    def properties_SpecificDBMSProperties28(self):
        return self.__properties_SpecificDBMSProperties28

    @properties_SpecificDBMSProperties28.setter
    def properties_SpecificDBMSProperties28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_properties_SpecificDBMSProperties__properties_SpecificDBMSProperties28", None)
        self.__properties_SpecificDBMSProperties28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "properties_SqlGroup27"):
                opp_val = getattr(old_value, "properties_SqlGroup27", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "properties_SqlGroup27"):
                opp_val = getattr(value, "properties_SqlGroup27", None)
                if opp_val is None:
                    setattr(value, "properties_SqlGroup27", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class properties_EStringToStringMapEntry:

    pass
class properties_DocumentRoot:

    def __init__(self, mixed: str, properties_DocumentRoot: set["properties_EStringToStringMapEntry"] = None, properties_DocumentRoot9: set["properties_EStringToStringMapEntry"] = None, properties_DocumentRoot12: set["properties_DatabasePropertiesListType"] = None, properties_DocumentRoot15: set["properties_SqlProperties"] = None):
        self.mixed = mixed
        self.properties_DocumentRoot = properties_DocumentRoot if properties_DocumentRoot is not None else set()
        self.properties_DocumentRoot9 = properties_DocumentRoot9 if properties_DocumentRoot9 is not None else set()
        self.properties_DocumentRoot12 = properties_DocumentRoot12 if properties_DocumentRoot12 is not None else set()
        self.properties_DocumentRoot15 = properties_DocumentRoot15 if properties_DocumentRoot15 is not None else set()
        
        pass
    @property
    def mixed(self):
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed


    @property
    def properties_DocumentRoot9(self):
        return self.__properties_DocumentRoot9

    @properties_DocumentRoot9.setter
    def properties_DocumentRoot9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_properties_DocumentRoot__properties_DocumentRoot9", None)
        self.__properties_DocumentRoot9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "properties_EStringToStringMapEntry10"):
                    opp_val = getattr(item, "properties_EStringToStringMapEntry10", None)
                    
                    if opp_val == self:
                        setattr(item, "properties_EStringToStringMapEntry10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "properties_EStringToStringMapEntry10"):
                    opp_val = getattr(item, "properties_EStringToStringMapEntry10", None)
                    
                    setattr(item, "properties_EStringToStringMapEntry10", self)
                    

    @property
    def properties_DocumentRoot12(self):
        return self.__properties_DocumentRoot12

    @properties_DocumentRoot12.setter
    def properties_DocumentRoot12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_properties_DocumentRoot__properties_DocumentRoot12", None)
        self.__properties_DocumentRoot12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "properties_DatabasePropertiesListType13"):
                    opp_val = getattr(item, "properties_DatabasePropertiesListType13", None)
                    
                    if opp_val == self:
                        setattr(item, "properties_DatabasePropertiesListType13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "properties_DatabasePropertiesListType13"):
                    opp_val = getattr(item, "properties_DatabasePropertiesListType13", None)
                    
                    setattr(item, "properties_DatabasePropertiesListType13", self)
                    

    @property
    def properties_DocumentRoot(self):
        return self.__properties_DocumentRoot

    @properties_DocumentRoot.setter
    def properties_DocumentRoot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_properties_DocumentRoot__properties_DocumentRoot", None)
        self.__properties_DocumentRoot = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "properties_EStringToStringMapEntry"):
                    opp_val = getattr(item, "properties_EStringToStringMapEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "properties_EStringToStringMapEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "properties_EStringToStringMapEntry"):
                    opp_val = getattr(item, "properties_EStringToStringMapEntry", None)
                    
                    setattr(item, "properties_EStringToStringMapEntry", self)
                    

    @property
    def properties_DocumentRoot15(self):
        return self.__properties_DocumentRoot15

    @properties_DocumentRoot15.setter
    def properties_DocumentRoot15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_properties_DocumentRoot__properties_DocumentRoot15", None)
        self.__properties_DocumentRoot15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "properties_SqlProperties16"):
                    opp_val = getattr(item, "properties_SqlProperties16", None)
                    
                    if opp_val == self:
                        setattr(item, "properties_SqlProperties16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "properties_SqlProperties16"):
                    opp_val = getattr(item, "properties_SqlProperties16", None)
                    
                    setattr(item, "properties_SqlProperties16", self)
                    

class properties_DatabasePropertiesListType:

    pass
class properties_Property:

    def __init__(self, key: str, value: str, properties_Property: "properties_DatabaseProperties" = None):
        self.key = key
        self.value = value
        self.properties_Property = properties_Property
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key


    @property
    def properties_Property(self):
        return self.__properties_Property

    @properties_Property.setter
    def properties_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_properties_Property__properties_Property", None)
        self.__properties_Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "properties_DatabaseProperties2"):
                opp_val = getattr(old_value, "properties_DatabaseProperties2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "properties_DatabaseProperties2"):
                opp_val = getattr(value, "properties_DatabaseProperties2", None)
                if opp_val is None:
                    setattr(value, "properties_DatabaseProperties2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class properties_SqlProperties:

    pass
class properties_DatabaseProperties:

    def __init__(self, id: str, driverClassName: str, dialect: str, serverURL: str, dBMS: str, port: str, databaseName: str, username: str, password: str, namespace: str, persistenceUnitName: str, properties_DatabaseProperties: "properties_SqlProperties" = None, properties_DatabaseProperties2: set["properties_Property"] = None, properties_DatabaseProperties4: "properties_DatabasePropertiesListType" = None):
        self.id = id
        self.driverClassName = driverClassName
        self.dialect = dialect
        self.serverURL = serverURL
        self.dBMS = dBMS
        self.port = port
        self.databaseName = databaseName
        self.username = username
        self.password = password
        self.namespace = namespace
        self.persistenceUnitName = persistenceUnitName
        self.properties_DatabaseProperties = properties_DatabaseProperties
        self.properties_DatabaseProperties2 = properties_DatabaseProperties2 if properties_DatabaseProperties2 is not None else set()
        self.properties_DatabaseProperties4 = properties_DatabaseProperties4
        
        pass
    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password: str):
        self.__password = password


    @property
    def serverURL(self):
        return self.__serverURL

    @serverURL.setter
    def serverURL(self, serverURL: str):
        self.__serverURL = serverURL


    @property
    def namespace(self):
        return self.__namespace

    @namespace.setter
    def namespace(self, namespace: str):
        self.__namespace = namespace


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def driverClassName(self):
        return self.__driverClassName

    @driverClassName.setter
    def driverClassName(self, driverClassName: str):
        self.__driverClassName = driverClassName


    @property
    def dBMS(self):
        return self.__dBMS

    @dBMS.setter
    def dBMS(self, dBMS: str):
        self.__dBMS = dBMS


    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, username: str):
        self.__username = username


    @property
    def dialect(self):
        return self.__dialect

    @dialect.setter
    def dialect(self, dialect: str):
        self.__dialect = dialect


    @property
    def persistenceUnitName(self):
        return self.__persistenceUnitName

    @persistenceUnitName.setter
    def persistenceUnitName(self, persistenceUnitName: str):
        self.__persistenceUnitName = persistenceUnitName


    @property
    def databaseName(self):
        return self.__databaseName

    @databaseName.setter
    def databaseName(self, databaseName: str):
        self.__databaseName = databaseName


    @property
    def port(self):
        return self.__port

    @port.setter
    def port(self, port: str):
        self.__port = port


    @property
    def properties_DatabaseProperties(self):
        return self.__properties_DatabaseProperties

    @properties_DatabaseProperties.setter
    def properties_DatabaseProperties(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_properties_DatabaseProperties__properties_DatabaseProperties", None)
        self.__properties_DatabaseProperties = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "properties_SqlProperties"):
                opp_val = getattr(old_value, "properties_SqlProperties", None)
                if opp_val == self:
                    setattr(old_value, "properties_SqlProperties", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "properties_SqlProperties"):
                opp_val = getattr(value, "properties_SqlProperties", None)
                setattr(value, "properties_SqlProperties", self)

    @property
    def properties_DatabaseProperties2(self):
        return self.__properties_DatabaseProperties2

    @properties_DatabaseProperties2.setter
    def properties_DatabaseProperties2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_properties_DatabaseProperties__properties_DatabaseProperties2", None)
        self.__properties_DatabaseProperties2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "properties_Property"):
                    opp_val = getattr(item, "properties_Property", None)
                    
                    if opp_val == self:
                        setattr(item, "properties_Property", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "properties_Property"):
                    opp_val = getattr(item, "properties_Property", None)
                    
                    setattr(item, "properties_Property", self)
                    

    @property
    def properties_DatabaseProperties4(self):
        return self.__properties_DatabaseProperties4

    @properties_DatabaseProperties4.setter
    def properties_DatabaseProperties4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_properties_DatabaseProperties__properties_DatabaseProperties4", None)
        self.__properties_DatabaseProperties4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "properties_DatabasePropertiesListType"):
                opp_val = getattr(old_value, "properties_DatabasePropertiesListType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "properties_DatabasePropertiesListType"):
                opp_val = getattr(value, "properties_DatabasePropertiesListType", None)
                if opp_val is None:
                    setattr(value, "properties_DatabasePropertiesListType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class properties_DatabaseAlias:

    def __init__(self, alias: str, id: str, properties_DatabaseAlias: "properties_DatabasePropertiesListType" = None):
        self.alias = alias
        self.id = id
        self.properties_DatabaseAlias = properties_DatabaseAlias
        
        pass
    @property
    def alias(self):
        return self.__alias

    @alias.setter
    def alias(self, alias: str):
        self.__alias = alias


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def properties_DatabaseAlias(self):
        return self.__properties_DatabaseAlias

    @properties_DatabaseAlias.setter
    def properties_DatabaseAlias(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_properties_DatabaseAlias__properties_DatabaseAlias", None)
        self.__properties_DatabaseAlias = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "properties_DatabasePropertiesListType6"):
                opp_val = getattr(old_value, "properties_DatabasePropertiesListType6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "properties_DatabasePropertiesListType6"):
                opp_val = getattr(value, "properties_DatabasePropertiesListType6", None)
                if opp_val is None:
                    setattr(value, "properties_DatabasePropertiesListType6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
