from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class table_type(Enum):
    COMMON = "COMMON"
    TEMP_NO_VALUE = "TEMP_NO_VALUE"
    TEMP_WITH_VALUE = "TEMP_WITH_VALUE"


############################################
# Definition of Classes
############################################

class oracle_OracleSequenceProperty:

    def __init__(self, space: str):
        self.space = space
        
        pass
    @property
    def space(self):
        return self.__space

    @space.setter
    def space(self, space: str):
        self.__space = space


class ExtensibleModel:

    pass
class oracle_OraclePrivilege(ExtensibleModel):

    def __init__(self, name: str, type: str, decription: str, oracle_OraclePrivilege8: "oracle_OracleUser" = None, oracle_OraclePrivilege: "oracle_OracleUserResourceData" = None):
        self.name = name
        self.type = type
        self.decription = decription
        self.oracle_OraclePrivilege8 = oracle_OraclePrivilege8
        self.oracle_OraclePrivilege = oracle_OraclePrivilege
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def decription(self):
        return self.__decription

    @decription.setter
    def decription(self, decription: str):
        self.__decription = decription


    @property
    def oracle_OraclePrivilege8(self):
        return self.__oracle_OraclePrivilege8

    @oracle_OraclePrivilege8.setter
    def oracle_OraclePrivilege8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oracle_OraclePrivilege__oracle_OraclePrivilege8", None)
        self.__oracle_OraclePrivilege8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oracle_OracleUser7"):
                opp_val = getattr(old_value, "oracle_OracleUser7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oracle_OracleUser7"):
                opp_val = getattr(value, "oracle_OracleUser7", None)
                if opp_val is None:
                    setattr(value, "oracle_OracleUser7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def oracle_OraclePrivilege(self):
        return self.__oracle_OraclePrivilege

    @oracle_OraclePrivilege.setter
    def oracle_OraclePrivilege(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oracle_OraclePrivilege__oracle_OraclePrivilege", None)
        self.__oracle_OraclePrivilege = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oracle_OracleUserResourceData5"):
                opp_val = getattr(old_value, "oracle_OracleUserResourceData5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oracle_OracleUserResourceData5"):
                opp_val = getattr(value, "oracle_OracleUserResourceData5", None)
                if opp_val is None:
                    setattr(value, "oracle_OracleUserResourceData5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class oracle_OracleUser(ExtensibleModel):

    def __init__(self, name: str, decription: str, attributes: str, enable: bool, password: str, defaultTableSpace: str, oracle_OracleUser: "oracle_OracleUserResourceData" = None, oracle_OracleUser7: set["oracle_OraclePrivilege"] = None):
        self.name = name
        self.decription = decription
        self.attributes = attributes
        self.enable = enable
        self.password = password
        self.defaultTableSpace = defaultTableSpace
        self.oracle_OracleUser = oracle_OracleUser
        self.oracle_OracleUser7 = oracle_OracleUser7 if oracle_OracleUser7 is not None else set()
        
        pass
    @property
    def attributes(self):
        return self.__attributes

    @attributes.setter
    def attributes(self, attributes: str):
        self.__attributes = attributes


    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password: str):
        self.__password = password


    @property
    def decription(self):
        return self.__decription

    @decription.setter
    def decription(self, decription: str):
        self.__decription = decription


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def defaultTableSpace(self):
        return self.__defaultTableSpace

    @defaultTableSpace.setter
    def defaultTableSpace(self, defaultTableSpace: str):
        self.__defaultTableSpace = defaultTableSpace


    @property
    def enable(self):
        return self.__enable

    @enable.setter
    def enable(self, enable: bool):
        self.__enable = enable


    @property
    def oracle_OracleUser7(self):
        return self.__oracle_OracleUser7

    @oracle_OracleUser7.setter
    def oracle_OracleUser7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oracle_OracleUser__oracle_OracleUser7", None)
        self.__oracle_OracleUser7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "oracle_OraclePrivilege8"):
                    opp_val = getattr(item, "oracle_OraclePrivilege8", None)
                    
                    if opp_val == self:
                        setattr(item, "oracle_OraclePrivilege8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "oracle_OraclePrivilege8"):
                    opp_val = getattr(item, "oracle_OraclePrivilege8", None)
                    
                    setattr(item, "oracle_OraclePrivilege8", self)
                    

    @property
    def oracle_OracleUser(self):
        return self.__oracle_OracleUser

    @oracle_OracleUser.setter
    def oracle_OracleUser(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oracle_OracleUser__oracle_OracleUser", None)
        self.__oracle_OracleUser = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oracle_OracleUserResourceData"):
                opp_val = getattr(old_value, "oracle_OracleUserResourceData", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oracle_OracleUserResourceData"):
                opp_val = getattr(value, "oracle_OracleUserResourceData", None)
                if opp_val is None:
                    setattr(value, "oracle_OracleUserResourceData", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class oracle_DatabaseModuleExtensibleProperty(ExtensibleModel):

    def __init__(self, tableType: str, space: str, splitField: str, splitNum: str, startDate: str, bizPkg: str):
        self.tableType = tableType
        self.space = space
        self.splitField = splitField
        self.splitNum = splitNum
        self.startDate = startDate
        self.bizPkg = bizPkg
        
        pass
    @property
    def bizPkg(self):
        return self.__bizPkg

    @bizPkg.setter
    def bizPkg(self, bizPkg: str):
        self.__bizPkg = bizPkg


    @property
    def tableType(self):
        return self.__tableType

    @tableType.setter
    def tableType(self, tableType: str):
        self.__tableType = tableType


    @property
    def startDate(self):
        return self.__startDate

    @startDate.setter
    def startDate(self, startDate: str):
        self.__startDate = startDate


    @property
    def splitNum(self):
        return self.__splitNum

    @splitNum.setter
    def splitNum(self, splitNum: str):
        self.__splitNum = splitNum


    @property
    def space(self):
        return self.__space

    @space.setter
    def space(self, space: str):
        self.__space = space


    @property
    def splitField(self):
        return self.__splitField

    @splitField.setter
    def splitField(self, splitField: str):
        self.__splitField = splitField


class oracle_TableSpaceRelation(ExtensibleModel):

    def __init__(self, mainSpace: str, indexSpace: str, oracle_TableSpaceRelation: "oracle_OracleSpaceResourceData" = None):
        self.mainSpace = mainSpace
        self.indexSpace = indexSpace
        self.oracle_TableSpaceRelation = oracle_TableSpaceRelation
        
        pass
    @property
    def indexSpace(self):
        return self.__indexSpace

    @indexSpace.setter
    def indexSpace(self, indexSpace: str):
        self.__indexSpace = indexSpace


    @property
    def mainSpace(self):
        return self.__mainSpace

    @mainSpace.setter
    def mainSpace(self, mainSpace: str):
        self.__mainSpace = mainSpace


    @property
    def oracle_TableSpaceRelation(self):
        return self.__oracle_TableSpaceRelation

    @oracle_TableSpaceRelation.setter
    def oracle_TableSpaceRelation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oracle_TableSpaceRelation__oracle_TableSpaceRelation", None)
        self.__oracle_TableSpaceRelation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oracle_OracleSpaceResourceData2"):
                opp_val = getattr(old_value, "oracle_OracleSpaceResourceData2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oracle_OracleSpaceResourceData2"):
                opp_val = getattr(value, "oracle_OracleSpaceResourceData2", None)
                if opp_val is None:
                    setattr(value, "oracle_OracleSpaceResourceData2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class oracle_TableSpace(ExtensibleModel):

    def __init__(self, name: str, chineseName: str, user: str, file: str, size: str, description: str, logicName: str, oracle_TableSpace: "oracle_OracleSpaceResourceData" = None):
        self.name = name
        self.chineseName = chineseName
        self.user = user
        self.file = file
        self.size = size
        self.description = description
        self.logicName = logicName
        self.oracle_TableSpace = oracle_TableSpace
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size: str):
        self.__size = size


    @property
    def user(self):
        return self.__user

    @user.setter
    def user(self, user: str):
        self.__user = user


    @property
    def chineseName(self):
        return self.__chineseName

    @chineseName.setter
    def chineseName(self, chineseName: str):
        self.__chineseName = chineseName


    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


    @property
    def file(self):
        return self.__file

    @file.setter
    def file(self, file: str):
        self.__file = file


    @property
    def logicName(self):
        return self.__logicName

    @logicName.setter
    def logicName(self, logicName: str):
        self.__logicName = logicName


    @property
    def oracle_TableSpace(self):
        return self.__oracle_TableSpace

    @oracle_TableSpace.setter
    def oracle_TableSpace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oracle_TableSpace__oracle_TableSpace", None)
        self.__oracle_TableSpace = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oracle_OracleSpaceResourceData"):
                opp_val = getattr(old_value, "oracle_OracleSpaceResourceData", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oracle_OracleSpaceResourceData"):
                opp_val = getattr(value, "oracle_OracleSpaceResourceData", None)
                if opp_val is None:
                    setattr(value, "oracle_OracleSpaceResourceData", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class DatabaseResourceData:

    pass
class oracle_TriggerResourceData(DatabaseResourceData):

    def __init__(self, sql: str):
        self.sql = sql
        
        pass
    @property
    def sql(self):
        return self.__sql

    @sql.setter
    def sql(self, sql: str):
        self.__sql = sql


class oracle_OracleUserResourceData(DatabaseResourceData):

    pass
class oracle_SequenceResourceData(DatabaseResourceData):

    def __init__(self, tableName: str, start: str, increment: str, minValue: str, maxValue: str, cycle: bool, cache: str, useCache: bool, isHistory: bool):
        self.tableName = tableName
        self.start = start
        self.increment = increment
        self.minValue = minValue
        self.maxValue = maxValue
        self.cycle = cycle
        self.cache = cache
        self.useCache = useCache
        self.isHistory = isHistory
        
        pass
    @property
    def isHistory(self):
        return self.__isHistory

    @isHistory.setter
    def isHistory(self, isHistory: bool):
        self.__isHistory = isHistory


    @property
    def increment(self):
        return self.__increment

    @increment.setter
    def increment(self, increment: str):
        self.__increment = increment


    @property
    def minValue(self):
        return self.__minValue

    @minValue.setter
    def minValue(self, minValue: str):
        self.__minValue = minValue


    @property
    def start(self):
        return self.__start

    @start.setter
    def start(self, start: str):
        self.__start = start


    @property
    def cycle(self):
        return self.__cycle

    @cycle.setter
    def cycle(self, cycle: bool):
        self.__cycle = cycle


    @property
    def tableName(self):
        return self.__tableName

    @tableName.setter
    def tableName(self, tableName: str):
        self.__tableName = tableName


    @property
    def cache(self):
        return self.__cache

    @cache.setter
    def cache(self, cache: str):
        self.__cache = cache


    @property
    def useCache(self):
        return self.__useCache

    @useCache.setter
    def useCache(self, useCache: bool):
        self.__useCache = useCache


    @property
    def maxValue(self):
        return self.__maxValue

    @maxValue.setter
    def maxValue(self, maxValue: str):
        self.__maxValue = maxValue


class oracle_OracleSpaceResourceData(DatabaseResourceData):

    pass
class oracle_OracleModuleProperty:

    def __init__(self, space: str):
        self.space = space
        
        pass
    @property
    def space(self):
        return self.__space

    @space.setter
    def space(self, space: str):
        self.__space = space


class oracle_OracleViewProperty:

    def __init__(self, space: str):
        self.space = space
        
        pass
    @property
    def space(self):
        return self.__space

    @space.setter
    def space(self, space: str):
        self.__space = space


class oracle_OracleIndexProperty:

    def __init__(self, reverse: bool):
        self.reverse = reverse
        
        pass
    @property
    def reverse(self):
        return self.__reverse

    @reverse.setter
    def reverse(self, reverse: bool):
        self.__reverse = reverse


class oracle_OracleTableProperty:

    def __init__(self, space: str, tabletype: str):
        self.space = space
        self.tabletype = tabletype
        
        pass
    @property
    def tabletype(self):
        return self.__tabletype

    @tabletype.setter
    def tabletype(self, tabletype: str):
        self.__tabletype = tabletype


    @property
    def space(self):
        return self.__space

    @space.setter
    def space(self, space: str):
        self.__space = space

