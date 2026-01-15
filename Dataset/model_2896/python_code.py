from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class MobaNFCModuleType(Enum):
    ID = "ID"
    CUSTOM = "CUSTOM"
    TEXT = "TEXT"
class MobaBlueToothModuleType(Enum):
    LE = "LE"
    SPP = "SPP"
    BEACON = "BEACON"
class MobaConstantValueFunction(Enum):
    TO_LOWER_CASE = "TO_LOWER_CASE"
    TO_UPPER_CASE = "TO_UPPER_CASE"
    TO_FIRST_UPPER_CASE = "TO_FIRST_UPPER_CASE"
    TO_FIRST_LOWER_CASE = "TO_FIRST_LOWER_CASE"
class MobaGeofenceEvent(Enum):
    ENTER = "ENTER"
    LEAVE = "LEAVE"
class MobaLowerBound(Enum):
    OPTIONAL = "OPTIONAL"
    MANY = "MANY"
    ZERO = "ZERO"
    ATLEASTONE = "ATLEASTONE"
    ONE = "ONE"
class MobaRESTMethods(Enum):
    GET = "GET"
    PUT = "PUT"
    DELETE = "DELETE"
    POST = "POST"
class MobaUpperBound(Enum):
    NULL = "NULL"
    ONE = "ONE"
    MANY = "MANY"


############################################
# Definition of Classes
############################################

class index_moba_MobaApplication:

    pass
class moba_index_MobaIndexEntry:

    def __init__(self, relativePath: str, filename: str, templateId: str, templateName: str, templateDescription: str, templateVersion: str, moba_index_MobaIndexEntry: "index_moba_MobaApplication" = None):
        self.relativePath = relativePath
        self.filename = filename
        self.templateId = templateId
        self.templateName = templateName
        self.templateDescription = templateDescription
        self.templateVersion = templateVersion
        self.moba_index_MobaIndexEntry = moba_index_MobaIndexEntry
        
    @property
    def templateDescription(self) -> str:
        return self.__templateDescription

    @templateDescription.setter
    def templateDescription(self, templateDescription: str):
        self.__templateDescription = templateDescription

    @property
    def templateId(self) -> str:
        return self.__templateId

    @templateId.setter
    def templateId(self, templateId: str):
        self.__templateId = templateId

    @property
    def templateVersion(self) -> str:
        return self.__templateVersion

    @templateVersion.setter
    def templateVersion(self, templateVersion: str):
        self.__templateVersion = templateVersion

    @property
    def relativePath(self) -> str:
        return self.__relativePath

    @relativePath.setter
    def relativePath(self, relativePath: str):
        self.__relativePath = relativePath

    @property
    def filename(self) -> str:
        return self.__filename

    @filename.setter
    def filename(self, filename: str):
        self.__filename = filename

    @property
    def templateName(self) -> str:
        return self.__templateName

    @templateName.setter
    def templateName(self, templateName: str):
        self.__templateName = templateName

    @property
    def moba_index_MobaIndexEntry(self):
        return self.__moba_index_MobaIndexEntry

    @moba_index_MobaIndexEntry.setter
    def moba_index_MobaIndexEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_index_MobaIndexEntry__moba_index_MobaIndexEntry", None)
        self.__moba_index_MobaIndexEntry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "index_moba_MobaApplication"):
                opp_val = getattr(old_value, "index_moba_MobaApplication", None)
                if opp_val == self:
                    setattr(old_value, "index_moba_MobaApplication", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "index_moba_MobaApplication"):
                opp_val = getattr(value, "index_moba_MobaApplication", None)
                setattr(value, "index_moba_MobaApplication", self)

class MobaIndexEntry:

    pass
class moba_index_MobaIndex:

    def __init__(self, id: str, name: str, description: str, version: str, moba_index_MobaIndex: set["MobaIndexEntry"] = None):
        self.id = id
        self.name = name
        self.description = description
        self.version = version
        self.moba_index_MobaIndex = moba_index_MobaIndex if moba_index_MobaIndex is not None else set()
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def moba_index_MobaIndex(self):
        return self.__moba_index_MobaIndex

    @moba_index_MobaIndex.setter
    def moba_index_MobaIndex(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_index_MobaIndex__moba_index_MobaIndex", None)
        self.__moba_index_MobaIndex = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MobaIndexEntry"):
                    opp_val = getattr(item, "MobaIndexEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "MobaIndexEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MobaIndexEntry"):
                    opp_val = getattr(item, "MobaIndexEntry", None)
                    
                    setattr(item, "MobaIndexEntry", self)
                    

class MobaExternalModule:

    pass
class moba_MobaNFCModule(MobaExternalModule):

    def __init__(self, type: str):
        self.type = type
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class moba_MobaPushModule(MobaExternalModule):

    pass
class moba_MobaBluetoothModule(MobaExternalModule):

    def __init__(self, type: str):
        self.type = type
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class MobaPropertiesAble:

    pass
class moba_MobaFriendsAble(MobaPropertiesAble):

    pass
class moba_MobaFriend:

    def __init__(self, valueString: str, value: str, moba_MobaFriend: "moba_MobaConstant" = None, moba_MobaFriend204: "moba_MobaFriendsAble" = None):
        self.valueString = valueString
        self.value = value
        self.moba_MobaFriend = moba_MobaFriend
        self.moba_MobaFriend204 = moba_MobaFriend204
        
    @property
    def valueString(self) -> str:
        return self.__valueString

    @valueString.setter
    def valueString(self, valueString: str):
        self.__valueString = valueString

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def moba_MobaFriend204(self):
        return self.__moba_MobaFriend204

    @moba_MobaFriend204.setter
    def moba_MobaFriend204(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaFriend__moba_MobaFriend204", None)
        self.__moba_MobaFriend204 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaFriendsAble"):
                opp_val = getattr(old_value, "moba_MobaFriendsAble", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaFriendsAble"):
                opp_val = getattr(value, "moba_MobaFriendsAble", None)
                if opp_val is None:
                    setattr(value, "moba_MobaFriendsAble", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def moba_MobaFriend(self):
        return self.__moba_MobaFriend

    @moba_MobaFriend.setter
    def moba_MobaFriend(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaFriend__moba_MobaFriend", None)
        self.__moba_MobaFriend = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaConstant202"):
                opp_val = getattr(old_value, "moba_MobaConstant202", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaConstant202", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaConstant202"):
                opp_val = getattr(value, "moba_MobaConstant202", None)
                setattr(value, "moba_MobaConstant202", self)

class MobaTrigger:

    pass
class moba_MobaAppUpdateTrigger(MobaTrigger):

    pass
class moba_MobaPushTrigger(MobaTrigger):

    pass
class moba_MobaDeviceStartupTrigger(MobaTrigger):

    pass
class moba_MobaGeofenceTrigger(MobaTrigger):

    def __init__(self, eventType: str):
        self.eventType = eventType
        
    @property
    def eventType(self) -> str:
        return self.__eventType

    @eventType.setter
    def eventType(self, eventType: str):
        self.__eventType = eventType

class moba_MobaEmailTrigger(MobaTrigger):

    pass
class moba_MobaTimerTrigger(MobaTrigger):

    pass
class moba_MobaSMSTrigger(MobaTrigger):

    pass
class moba_MobaAppInstallTrigger(MobaTrigger):

    pass
class moba_MobaEnumLiteral:

    def __init__(self, literal: str, name: str, value: int, default: bool, undefined: bool, hidden: bool, moba_MobaEnumLiteral: "moba_MobaEnum" = None):
        self.literal = literal
        self.name = name
        self.value = value
        self.default = default
        self.undefined = undefined
        self.hidden = hidden
        self.moba_MobaEnumLiteral = moba_MobaEnumLiteral
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def default(self) -> bool:
        return self.__default

    @default.setter
    def default(self, default: bool):
        self.__default = default

    @property
    def hidden(self) -> bool:
        return self.__hidden

    @hidden.setter
    def hidden(self, hidden: bool):
        self.__hidden = hidden

    @property
    def literal(self) -> str:
        return self.__literal

    @literal.setter
    def literal(self, literal: str):
        self.__literal = literal

    @property
    def undefined(self) -> bool:
        return self.__undefined

    @undefined.setter
    def undefined(self, undefined: bool):
        self.__undefined = undefined

    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def moba_MobaEnumLiteral(self):
        return self.__moba_MobaEnumLiteral

    @moba_MobaEnumLiteral.setter
    def moba_MobaEnumLiteral(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaEnumLiteral__moba_MobaEnumLiteral", None)
        self.__moba_MobaEnumLiteral = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaEnum198"):
                opp_val = getattr(old_value, "moba_MobaEnum198", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaEnum198"):
                opp_val = getattr(value, "moba_MobaEnum198", None)
                if opp_val is None:
                    setattr(value, "moba_MobaEnum198", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class moba_MobaConstraint(ABC):

    pass
class moba_MobaConstraintable(ABC):

    pass
class MobaConstraint:

    pass
class moba_MobaNullConstraint(MobaConstraint):

    pass
class moba_MobaNotNullConstraint(MobaConstraint):

    pass
class moba_MobaPastConstraint(MobaConstraint):

    pass
class moba_MobaFutureConstraint(MobaConstraint):

    pass
class moba_MobaDigitsConstraint(MobaConstraint):

    def __init__(self, filterIntegerValue: int, filterFractionValue: int, moba_MobaDigitsConstraint: "moba_MobaConstant" = None, moba_MobaDigitsConstraint195: "moba_MobaConstant" = None):
        self.filterIntegerValue = filterIntegerValue
        self.filterFractionValue = filterFractionValue
        self.moba_MobaDigitsConstraint = moba_MobaDigitsConstraint
        self.moba_MobaDigitsConstraint195 = moba_MobaDigitsConstraint195
        
    @property
    def filterIntegerValue(self) -> int:
        return self.__filterIntegerValue

    @filterIntegerValue.setter
    def filterIntegerValue(self, filterIntegerValue: int):
        self.__filterIntegerValue = filterIntegerValue

    @property
    def filterFractionValue(self) -> int:
        return self.__filterFractionValue

    @filterFractionValue.setter
    def filterFractionValue(self, filterFractionValue: int):
        self.__filterFractionValue = filterFractionValue

    @property
    def moba_MobaDigitsConstraint195(self):
        return self.__moba_MobaDigitsConstraint195

    @moba_MobaDigitsConstraint195.setter
    def moba_MobaDigitsConstraint195(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaDigitsConstraint__moba_MobaDigitsConstraint195", None)
        self.__moba_MobaDigitsConstraint195 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaConstant196"):
                opp_val = getattr(old_value, "moba_MobaConstant196", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaConstant196", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaConstant196"):
                opp_val = getattr(value, "moba_MobaConstant196", None)
                setattr(value, "moba_MobaConstant196", self)

    @property
    def moba_MobaDigitsConstraint(self):
        return self.__moba_MobaDigitsConstraint

    @moba_MobaDigitsConstraint.setter
    def moba_MobaDigitsConstraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaDigitsConstraint__moba_MobaDigitsConstraint", None)
        self.__moba_MobaDigitsConstraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaConstant193"):
                opp_val = getattr(old_value, "moba_MobaConstant193", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaConstant193", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaConstant193"):
                opp_val = getattr(value, "moba_MobaConstant193", None)
                setattr(value, "moba_MobaConstant193", self)

class moba_MobaMinLengthConstraint(MobaConstraint):

    def __init__(self, filterValue: int, moba_MobaMinLengthConstraint: "moba_MobaConstant" = None):
        self.filterValue = filterValue
        self.moba_MobaMinLengthConstraint = moba_MobaMinLengthConstraint
        
    @property
    def filterValue(self) -> int:
        return self.__filterValue

    @filterValue.setter
    def filterValue(self, filterValue: int):
        self.__filterValue = filterValue

    @property
    def moba_MobaMinLengthConstraint(self):
        return self.__moba_MobaMinLengthConstraint

    @moba_MobaMinLengthConstraint.setter
    def moba_MobaMinLengthConstraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaMinLengthConstraint__moba_MobaMinLengthConstraint", None)
        self.__moba_MobaMinLengthConstraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaConstant189"):
                opp_val = getattr(old_value, "moba_MobaConstant189", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaConstant189", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaConstant189"):
                opp_val = getattr(value, "moba_MobaConstant189", None)
                setattr(value, "moba_MobaConstant189", self)

class moba_MobaMaxConstraint(MobaConstraint):

    def __init__(self, filterValue: float, moba_MobaMaxConstraint: "moba_MobaConstant" = None):
        self.filterValue = filterValue
        self.moba_MobaMaxConstraint = moba_MobaMaxConstraint
        
    @property
    def filterValue(self) -> float:
        return self.__filterValue

    @filterValue.setter
    def filterValue(self, filterValue: float):
        self.__filterValue = filterValue

    @property
    def moba_MobaMaxConstraint(self):
        return self.__moba_MobaMaxConstraint

    @moba_MobaMaxConstraint.setter
    def moba_MobaMaxConstraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaMaxConstraint__moba_MobaMaxConstraint", None)
        self.__moba_MobaMaxConstraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaConstant187"):
                opp_val = getattr(old_value, "moba_MobaConstant187", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaConstant187", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaConstant187"):
                opp_val = getattr(value, "moba_MobaConstant187", None)
                setattr(value, "moba_MobaConstant187", self)

class moba_MobaMaxLengthConstraint(MobaConstraint):

    def __init__(self, filterValue: int, moba_MobaMaxLengthConstraint: "moba_MobaConstant" = None):
        self.filterValue = filterValue
        self.moba_MobaMaxLengthConstraint = moba_MobaMaxLengthConstraint
        
    @property
    def filterValue(self) -> int:
        return self.__filterValue

    @filterValue.setter
    def filterValue(self, filterValue: int):
        self.__filterValue = filterValue

    @property
    def moba_MobaMaxLengthConstraint(self):
        return self.__moba_MobaMaxLengthConstraint

    @moba_MobaMaxLengthConstraint.setter
    def moba_MobaMaxLengthConstraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaMaxLengthConstraint__moba_MobaMaxLengthConstraint", None)
        self.__moba_MobaMaxLengthConstraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaConstant191"):
                opp_val = getattr(old_value, "moba_MobaConstant191", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaConstant191", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaConstant191"):
                opp_val = getattr(value, "moba_MobaConstant191", None)
                setattr(value, "moba_MobaConstant191", self)

class moba_MobaMinConstraint(MobaConstraint):

    def __init__(self, filterValue: float, moba_MobaMinConstraint: "moba_MobaConstant" = None):
        self.filterValue = filterValue
        self.moba_MobaMinConstraint = moba_MobaMinConstraint
        
    @property
    def filterValue(self) -> float:
        return self.__filterValue

    @filterValue.setter
    def filterValue(self, filterValue: float):
        self.__filterValue = filterValue

    @property
    def moba_MobaMinConstraint(self):
        return self.__moba_MobaMinConstraint

    @moba_MobaMinConstraint.setter
    def moba_MobaMinConstraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaMinConstraint__moba_MobaMinConstraint", None)
        self.__moba_MobaMinConstraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaConstant185"):
                opp_val = getattr(old_value, "moba_MobaConstant185", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaConstant185", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaConstant185"):
                opp_val = getattr(value, "moba_MobaConstant185", None)
                setattr(value, "moba_MobaConstant185", self)

class moba_MobaRegexpConstraint(MobaConstraint):

    def __init__(self, filterString: str, moba_MobaRegexpConstraint: "moba_MobaConstant" = None):
        self.filterString = filterString
        self.moba_MobaRegexpConstraint = moba_MobaRegexpConstraint
        
    @property
    def filterString(self) -> str:
        return self.__filterString

    @filterString.setter
    def filterString(self, filterString: str):
        self.__filterString = filterString

    @property
    def moba_MobaRegexpConstraint(self):
        return self.__moba_MobaRegexpConstraint

    @moba_MobaRegexpConstraint.setter
    def moba_MobaRegexpConstraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaRegexpConstraint__moba_MobaRegexpConstraint", None)
        self.__moba_MobaRegexpConstraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaConstant183"):
                opp_val = getattr(old_value, "moba_MobaConstant183", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaConstant183", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaConstant183"):
                opp_val = getattr(value, "moba_MobaConstant183", None)
                setattr(value, "moba_MobaConstant183", self)

class MobaQueueFeature:

    pass
class moba_MobaQueueReference(MobaQueueFeature):

    pass
class MobaDtoFeature:

    pass
class MobaEntityFeature:

    pass
class moba_MobaMuliplicity:

    def __init__(self, lower: str, upper: str, moba_MobaMuliplicity: "moba_MobaMultiplicityAble" = None):
        self.lower = lower
        self.upper = upper
        self.moba_MobaMuliplicity = moba_MobaMuliplicity
        
    @property
    def upper(self) -> str:
        return self.__upper

    @upper.setter
    def upper(self, upper: str):
        self.__upper = upper

    @property
    def lower(self) -> str:
        return self.__lower

    @lower.setter
    def lower(self, lower: str):
        self.__lower = lower

    @property
    def moba_MobaMuliplicity(self):
        return self.__moba_MobaMuliplicity

    @moba_MobaMuliplicity.setter
    def moba_MobaMuliplicity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaMuliplicity__moba_MobaMuliplicity", None)
        self.__moba_MobaMuliplicity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaMultiplicityAble"):
                opp_val = getattr(old_value, "moba_MobaMultiplicityAble", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaMultiplicityAble", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaMultiplicityAble"):
                opp_val = getattr(value, "moba_MobaMultiplicityAble", None)
                setattr(value, "moba_MobaMultiplicityAble", self)

class moba_MobaMultiplicityAble(ABC):

    pass
class MobaREST:

    pass
class moba_MobaRESTCrud(MobaREST):

    def __init__(self, operations: str, moba_MobaRESTCrud: "moba_MobaRESTCrud" = None, moba_MobaRESTCrud151: "moba_MobaRESTCrud" = None):
        self.operations = operations
        self.moba_MobaRESTCrud = moba_MobaRESTCrud
        self.moba_MobaRESTCrud151 = moba_MobaRESTCrud151
        
    @property
    def operations(self) -> str:
        return self.__operations

    @operations.setter
    def operations(self, operations: str):
        self.__operations = operations

    @property
    def moba_MobaRESTCrud(self):
        return self.__moba_MobaRESTCrud

    @moba_MobaRESTCrud.setter
    def moba_MobaRESTCrud(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaRESTCrud__moba_MobaRESTCrud", None)
        self.__moba_MobaRESTCrud = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaRESTCrud151"):
                opp_val = getattr(old_value, "moba_MobaRESTCrud151", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaRESTCrud151", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaRESTCrud151"):
                opp_val = getattr(value, "moba_MobaRESTCrud151", None)
                setattr(value, "moba_MobaRESTCrud151", self)

    @property
    def moba_MobaRESTCrud151(self):
        return self.__moba_MobaRESTCrud151

    @moba_MobaRESTCrud151.setter
    def moba_MobaRESTCrud151(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaRESTCrud__moba_MobaRESTCrud151", None)
        self.__moba_MobaRESTCrud151 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaRESTCrud"):
                opp_val = getattr(old_value, "moba_MobaRESTCrud", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaRESTCrud", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaRESTCrud"):
                opp_val = getattr(value, "moba_MobaRESTCrud", None)
                setattr(value, "moba_MobaRESTCrud", self)

class moba_MobaRESTWorkflow(MobaREST):

    pass
class moba_MobaRESTCustomService(MobaREST):

    def __init__(self, operation: str, moba_MobaRESTCustomService: set["moba_MobaRESTAbstractAttribute"] = None, moba_MobaRESTCustomService142: "moba_MobaRESTCustomService" = None, moba_MobaRESTCustomService140: "moba_MobaRESTCustomService" = None, moba_MobaRESTCustomService144: set["moba_MobaRESTAbstractAttribute"] = None):
        self.operation = operation
        self.moba_MobaRESTCustomService = moba_MobaRESTCustomService if moba_MobaRESTCustomService is not None else set()
        self.moba_MobaRESTCustomService142 = moba_MobaRESTCustomService142
        self.moba_MobaRESTCustomService140 = moba_MobaRESTCustomService140
        self.moba_MobaRESTCustomService144 = moba_MobaRESTCustomService144 if moba_MobaRESTCustomService144 is not None else set()
        
    @property
    def operation(self) -> str:
        return self.__operation

    @operation.setter
    def operation(self, operation: str):
        self.__operation = operation

    @property
    def moba_MobaRESTCustomService142(self):
        return self.__moba_MobaRESTCustomService142

    @moba_MobaRESTCustomService142.setter
    def moba_MobaRESTCustomService142(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaRESTCustomService__moba_MobaRESTCustomService142", None)
        self.__moba_MobaRESTCustomService142 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaRESTCustomService140"):
                opp_val = getattr(old_value, "moba_MobaRESTCustomService140", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaRESTCustomService140", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaRESTCustomService140"):
                opp_val = getattr(value, "moba_MobaRESTCustomService140", None)
                setattr(value, "moba_MobaRESTCustomService140", self)

    @property
    def moba_MobaRESTCustomService140(self):
        return self.__moba_MobaRESTCustomService140

    @moba_MobaRESTCustomService140.setter
    def moba_MobaRESTCustomService140(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaRESTCustomService__moba_MobaRESTCustomService140", None)
        self.__moba_MobaRESTCustomService140 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaRESTCustomService142"):
                opp_val = getattr(old_value, "moba_MobaRESTCustomService142", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaRESTCustomService142", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaRESTCustomService142"):
                opp_val = getattr(value, "moba_MobaRESTCustomService142", None)
                setattr(value, "moba_MobaRESTCustomService142", self)

    @property
    def moba_MobaRESTCustomService144(self):
        return self.__moba_MobaRESTCustomService144

    @moba_MobaRESTCustomService144.setter
    def moba_MobaRESTCustomService144(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaRESTCustomService__moba_MobaRESTCustomService144", None)
        self.__moba_MobaRESTCustomService144 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "moba_MobaRESTAbstractAttribute145"):
                    opp_val = getattr(item, "moba_MobaRESTAbstractAttribute145", None)
                    
                    if opp_val == self:
                        setattr(item, "moba_MobaRESTAbstractAttribute145", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "moba_MobaRESTAbstractAttribute145"):
                    opp_val = getattr(item, "moba_MobaRESTAbstractAttribute145", None)
                    
                    setattr(item, "moba_MobaRESTAbstractAttribute145", self)
                    

    @property
    def moba_MobaRESTCustomService(self):
        return self.__moba_MobaRESTCustomService

    @moba_MobaRESTCustomService.setter
    def moba_MobaRESTCustomService(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaRESTCustomService__moba_MobaRESTCustomService", None)
        self.__moba_MobaRESTCustomService = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "moba_MobaRESTAbstractAttribute139"):
                    opp_val = getattr(item, "moba_MobaRESTAbstractAttribute139", None)
                    
                    if opp_val == self:
                        setattr(item, "moba_MobaRESTAbstractAttribute139", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "moba_MobaRESTAbstractAttribute139"):
                    opp_val = getattr(item, "moba_MobaRESTAbstractAttribute139", None)
                    
                    setattr(item, "moba_MobaRESTAbstractAttribute139", self)
                    

class moba_MobaRESTHeader:

    def __init__(self, contentTypeHeader: bool, rawHeader: bool, keyString: str, valueString: str, key: str, value: str, moba_MobaRESTHeader: "moba_MobaREST" = None, moba_MobaRESTHeader133: "moba_MobaConstant" = None, moba_MobaRESTHeader136: "moba_MobaConstant" = None):
        self.contentTypeHeader = contentTypeHeader
        self.rawHeader = rawHeader
        self.keyString = keyString
        self.valueString = valueString
        self.key = key
        self.value = value
        self.moba_MobaRESTHeader = moba_MobaRESTHeader
        self.moba_MobaRESTHeader133 = moba_MobaRESTHeader133
        self.moba_MobaRESTHeader136 = moba_MobaRESTHeader136
        
    @property
    def contentTypeHeader(self) -> bool:
        return self.__contentTypeHeader

    @contentTypeHeader.setter
    def contentTypeHeader(self, contentTypeHeader: bool):
        self.__contentTypeHeader = contentTypeHeader

    @property
    def rawHeader(self) -> bool:
        return self.__rawHeader

    @rawHeader.setter
    def rawHeader(self, rawHeader: bool):
        self.__rawHeader = rawHeader

    @property
    def keyString(self) -> str:
        return self.__keyString

    @keyString.setter
    def keyString(self, keyString: str):
        self.__keyString = keyString

    @property
    def valueString(self) -> str:
        return self.__valueString

    @valueString.setter
    def valueString(self, valueString: str):
        self.__valueString = valueString

    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def moba_MobaRESTHeader136(self):
        return self.__moba_MobaRESTHeader136

    @moba_MobaRESTHeader136.setter
    def moba_MobaRESTHeader136(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaRESTHeader__moba_MobaRESTHeader136", None)
        self.__moba_MobaRESTHeader136 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaConstant137"):
                opp_val = getattr(old_value, "moba_MobaConstant137", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaConstant137", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaConstant137"):
                opp_val = getattr(value, "moba_MobaConstant137", None)
                setattr(value, "moba_MobaConstant137", self)

    @property
    def moba_MobaRESTHeader(self):
        return self.__moba_MobaRESTHeader

    @moba_MobaRESTHeader.setter
    def moba_MobaRESTHeader(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaRESTHeader__moba_MobaRESTHeader", None)
        self.__moba_MobaRESTHeader = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaREST107"):
                opp_val = getattr(old_value, "moba_MobaREST107", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaREST107"):
                opp_val = getattr(value, "moba_MobaREST107", None)
                if opp_val is None:
                    setattr(value, "moba_MobaREST107", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def moba_MobaRESTHeader133(self):
        return self.__moba_MobaRESTHeader133

    @moba_MobaRESTHeader133.setter
    def moba_MobaRESTHeader133(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaRESTHeader__moba_MobaRESTHeader133", None)
        self.__moba_MobaRESTHeader133 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaConstant134"):
                opp_val = getattr(old_value, "moba_MobaConstant134", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaConstant134", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaConstant134"):
                opp_val = getattr(value, "moba_MobaConstant134", None)
                setattr(value, "moba_MobaConstant134", self)

class moba_MobaRESTPayloadDefinition:

    def __init__(self, array: bool, moba_MobaRESTPayloadDefinition112: "moba_MobaDto" = None, moba_MobaRESTPayloadDefinition115: "moba_MobaTransportSerializationType" = None, moba_MobaRESTPayloadDefinition: "moba_MobaREST" = None, moba_MobaRESTPayloadDefinition99: "moba_MobaREST" = None, moba_MobaRESTPayloadDefinition102: "moba_MobaREST" = None, moba_MobaRESTPayloadDefinition105: "moba_MobaREST" = None):
        self.array = array
        self.moba_MobaRESTPayloadDefinition112 = moba_MobaRESTPayloadDefinition112
        self.moba_MobaRESTPayloadDefinition115 = moba_MobaRESTPayloadDefinition115
        self.moba_MobaRESTPayloadDefinition = moba_MobaRESTPayloadDefinition
        self.moba_MobaRESTPayloadDefinition99 = moba_MobaRESTPayloadDefinition99
        self.moba_MobaRESTPayloadDefinition102 = moba_MobaRESTPayloadDefinition102
        self.moba_MobaRESTPayloadDefinition105 = moba_MobaRESTPayloadDefinition105
        
    @property
    def array(self) -> bool:
        return self.__array

    @array.setter
    def array(self, array: bool):
        self.__array = array

    @property
    def moba_MobaRESTPayloadDefinition115(self):
        return self.__moba_MobaRESTPayloadDefinition115

    @moba_MobaRESTPayloadDefinition115.setter
    def moba_MobaRESTPayloadDefinition115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaRESTPayloadDefinition__moba_MobaRESTPayloadDefinition115", None)
        self.__moba_MobaRESTPayloadDefinition115 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaTransportSerializationType116"):
                opp_val = getattr(old_value, "moba_MobaTransportSerializationType116", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaTransportSerializationType116", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaTransportSerializationType116"):
                opp_val = getattr(value, "moba_MobaTransportSerializationType116", None)
                setattr(value, "moba_MobaTransportSerializationType116", self)

    @property
    def moba_MobaRESTPayloadDefinition105(self):
        return self.__moba_MobaRESTPayloadDefinition105

    @moba_MobaRESTPayloadDefinition105.setter
    def moba_MobaRESTPayloadDefinition105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaRESTPayloadDefinition__moba_MobaRESTPayloadDefinition105", None)
        self.__moba_MobaRESTPayloadDefinition105 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaREST104"):
                opp_val = getattr(old_value, "moba_MobaREST104", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaREST104", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaREST104"):
                opp_val = getattr(value, "moba_MobaREST104", None)
                setattr(value, "moba_MobaREST104", self)

    @property
    def moba_MobaRESTPayloadDefinition99(self):
        return self.__moba_MobaRESTPayloadDefinition99

    @moba_MobaRESTPayloadDefinition99.setter
    def moba_MobaRESTPayloadDefinition99(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaRESTPayloadDefinition__moba_MobaRESTPayloadDefinition99", None)
        self.__moba_MobaRESTPayloadDefinition99 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaREST98"):
                opp_val = getattr(old_value, "moba_MobaREST98", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaREST98", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaREST98"):
                opp_val = getattr(value, "moba_MobaREST98", None)
                setattr(value, "moba_MobaREST98", self)

    @property
    def moba_MobaRESTPayloadDefinition(self):
        return self.__moba_MobaRESTPayloadDefinition

    @moba_MobaRESTPayloadDefinition.setter
    def moba_MobaRESTPayloadDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaRESTPayloadDefinition__moba_MobaRESTPayloadDefinition", None)
        self.__moba_MobaRESTPayloadDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaREST96"):
                opp_val = getattr(old_value, "moba_MobaREST96", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaREST96", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaREST96"):
                opp_val = getattr(value, "moba_MobaREST96", None)
                setattr(value, "moba_MobaREST96", self)

    @property
    def moba_MobaRESTPayloadDefinition102(self):
        return self.__moba_MobaRESTPayloadDefinition102

    @moba_MobaRESTPayloadDefinition102.setter
    def moba_MobaRESTPayloadDefinition102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaRESTPayloadDefinition__moba_MobaRESTPayloadDefinition102", None)
        self.__moba_MobaRESTPayloadDefinition102 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaREST101"):
                opp_val = getattr(old_value, "moba_MobaREST101", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaREST101", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaREST101"):
                opp_val = getattr(value, "moba_MobaREST101", None)
                setattr(value, "moba_MobaREST101", self)

    @property
    def moba_MobaRESTPayloadDefinition112(self):
        return self.__moba_MobaRESTPayloadDefinition112

    @moba_MobaRESTPayloadDefinition112.setter
    def moba_MobaRESTPayloadDefinition112(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaRESTPayloadDefinition__moba_MobaRESTPayloadDefinition112", None)
        self.__moba_MobaRESTPayloadDefinition112 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaDto113"):
                opp_val = getattr(old_value, "moba_MobaDto113", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaDto113", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaDto113"):
                opp_val = getattr(value, "moba_MobaDto113", None)
                setattr(value, "moba_MobaDto113", self)

class MobaRESTAbstractAttribute:

    pass
class moba_MobaRESTDtoAttribute(MobaRESTAbstractAttribute):

    pass
class moba_MobaRESTAttribute(MobaRESTAbstractAttribute):

    def __init__(self, keyString: str, key: str, valueString: str, valueDouble: str, valueInt: str, value: str, formatString: str, moba_MobaRESTAttribute: "moba_MobaDataType" = None, moba_MobaRESTAttribute122: "moba_MobaConstant" = None, moba_MobaRESTAttribute125: "moba_MobaConstant" = None, moba_MobaRESTAttribute128: "moba_MobaConstant" = None):
        self.keyString = keyString
        self.key = key
        self.valueString = valueString
        self.valueDouble = valueDouble
        self.valueInt = valueInt
        self.value = value
        self.formatString = formatString
        self.moba_MobaRESTAttribute = moba_MobaRESTAttribute
        self.moba_MobaRESTAttribute122 = moba_MobaRESTAttribute122
        self.moba_MobaRESTAttribute125 = moba_MobaRESTAttribute125
        self.moba_MobaRESTAttribute128 = moba_MobaRESTAttribute128
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def keyString(self) -> str:
        return self.__keyString

    @keyString.setter
    def keyString(self, keyString: str):
        self.__keyString = keyString

    @property
    def formatString(self) -> str:
        return self.__formatString

    @formatString.setter
    def formatString(self, formatString: str):
        self.__formatString = formatString

    @property
    def valueDouble(self) -> str:
        return self.__valueDouble

    @valueDouble.setter
    def valueDouble(self, valueDouble: str):
        self.__valueDouble = valueDouble

    @property
    def valueString(self) -> str:
        return self.__valueString

    @valueString.setter
    def valueString(self, valueString: str):
        self.__valueString = valueString

    @property
    def valueInt(self) -> str:
        return self.__valueInt

    @valueInt.setter
    def valueInt(self, valueInt: str):
        self.__valueInt = valueInt

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def moba_MobaRESTAttribute128(self):
        return self.__moba_MobaRESTAttribute128

    @moba_MobaRESTAttribute128.setter
    def moba_MobaRESTAttribute128(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaRESTAttribute__moba_MobaRESTAttribute128", None)
        self.__moba_MobaRESTAttribute128 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaConstant129"):
                opp_val = getattr(old_value, "moba_MobaConstant129", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaConstant129", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaConstant129"):
                opp_val = getattr(value, "moba_MobaConstant129", None)
                setattr(value, "moba_MobaConstant129", self)

    @property
    def moba_MobaRESTAttribute122(self):
        return self.__moba_MobaRESTAttribute122

    @moba_MobaRESTAttribute122.setter
    def moba_MobaRESTAttribute122(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaRESTAttribute__moba_MobaRESTAttribute122", None)
        self.__moba_MobaRESTAttribute122 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaConstant123"):
                opp_val = getattr(old_value, "moba_MobaConstant123", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaConstant123", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaConstant123"):
                opp_val = getattr(value, "moba_MobaConstant123", None)
                setattr(value, "moba_MobaConstant123", self)

    @property
    def moba_MobaRESTAttribute(self):
        return self.__moba_MobaRESTAttribute

    @moba_MobaRESTAttribute.setter
    def moba_MobaRESTAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaRESTAttribute__moba_MobaRESTAttribute", None)
        self.__moba_MobaRESTAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaDataType120"):
                opp_val = getattr(old_value, "moba_MobaDataType120", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaDataType120", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaDataType120"):
                opp_val = getattr(value, "moba_MobaDataType120", None)
                setattr(value, "moba_MobaDataType120", self)

    @property
    def moba_MobaRESTAttribute125(self):
        return self.__moba_MobaRESTAttribute125

    @moba_MobaRESTAttribute125.setter
    def moba_MobaRESTAttribute125(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaRESTAttribute__moba_MobaRESTAttribute125", None)
        self.__moba_MobaRESTAttribute125 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaConstant126"):
                opp_val = getattr(old_value, "moba_MobaConstant126", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaConstant126", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaConstant126"):
                opp_val = getattr(value, "moba_MobaConstant126", None)
                setattr(value, "moba_MobaConstant126", self)

class moba_MobaRESTAbstractAttribute(ABC):

    def __init__(self, aliasString: str, alias: str, attachment: bool, moba_MobaRESTAbstractAttribute: "moba_MobaConstant" = None, moba_MobaRESTAbstractAttribute139: "moba_MobaRESTCustomService" = None, moba_MobaRESTAbstractAttribute145: "moba_MobaRESTCustomService" = None):
        self.aliasString = aliasString
        self.alias = alias
        self.attachment = attachment
        self.moba_MobaRESTAbstractAttribute = moba_MobaRESTAbstractAttribute
        self.moba_MobaRESTAbstractAttribute139 = moba_MobaRESTAbstractAttribute139
        self.moba_MobaRESTAbstractAttribute145 = moba_MobaRESTAbstractAttribute145
        
    @property
    def alias(self) -> str:
        return self.__alias

    @alias.setter
    def alias(self, alias: str):
        self.__alias = alias

    @property
    def aliasString(self) -> str:
        return self.__aliasString

    @aliasString.setter
    def aliasString(self, aliasString: str):
        self.__aliasString = aliasString

    @property
    def attachment(self) -> bool:
        return self.__attachment

    @attachment.setter
    def attachment(self, attachment: bool):
        self.__attachment = attachment

    @property
    def moba_MobaRESTAbstractAttribute139(self):
        return self.__moba_MobaRESTAbstractAttribute139

    @moba_MobaRESTAbstractAttribute139.setter
    def moba_MobaRESTAbstractAttribute139(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaRESTAbstractAttribute__moba_MobaRESTAbstractAttribute139", None)
        self.__moba_MobaRESTAbstractAttribute139 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaRESTCustomService"):
                opp_val = getattr(old_value, "moba_MobaRESTCustomService", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaRESTCustomService"):
                opp_val = getattr(value, "moba_MobaRESTCustomService", None)
                if opp_val is None:
                    setattr(value, "moba_MobaRESTCustomService", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def moba_MobaRESTAbstractAttribute(self):
        return self.__moba_MobaRESTAbstractAttribute

    @moba_MobaRESTAbstractAttribute.setter
    def moba_MobaRESTAbstractAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaRESTAbstractAttribute__moba_MobaRESTAbstractAttribute", None)
        self.__moba_MobaRESTAbstractAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaConstant118"):
                opp_val = getattr(old_value, "moba_MobaConstant118", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaConstant118", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaConstant118"):
                opp_val = getattr(value, "moba_MobaConstant118", None)
                setattr(value, "moba_MobaConstant118", self)

    @property
    def moba_MobaRESTAbstractAttribute145(self):
        return self.__moba_MobaRESTAbstractAttribute145

    @moba_MobaRESTAbstractAttribute145.setter
    def moba_MobaRESTAbstractAttribute145(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaRESTAbstractAttribute__moba_MobaRESTAbstractAttribute145", None)
        self.__moba_MobaRESTAbstractAttribute145 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaRESTCustomService144"):
                opp_val = getattr(old_value, "moba_MobaRESTCustomService144", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaRESTCustomService144"):
                opp_val = getattr(value, "moba_MobaRESTCustomService144", None)
                if opp_val is None:
                    setattr(value, "moba_MobaRESTCustomService144", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class moba_MobaEntityIndex:

    def __init__(self, name: str, unique: bool, moba_MobaEntityIndex: "moba_MobaEntity" = None, moba_MobaEntityIndex78: set["moba_MobaEntityAttribute"] = None):
        self.name = name
        self.unique = unique
        self.moba_MobaEntityIndex = moba_MobaEntityIndex
        self.moba_MobaEntityIndex78 = moba_MobaEntityIndex78 if moba_MobaEntityIndex78 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def unique(self) -> bool:
        return self.__unique

    @unique.setter
    def unique(self, unique: bool):
        self.__unique = unique

    @property
    def moba_MobaEntityIndex78(self):
        return self.__moba_MobaEntityIndex78

    @moba_MobaEntityIndex78.setter
    def moba_MobaEntityIndex78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaEntityIndex__moba_MobaEntityIndex78", None)
        self.__moba_MobaEntityIndex78 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "moba_MobaEntityAttribute"):
                    opp_val = getattr(item, "moba_MobaEntityAttribute", None)
                    
                    if opp_val == self:
                        setattr(item, "moba_MobaEntityAttribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "moba_MobaEntityAttribute"):
                    opp_val = getattr(item, "moba_MobaEntityAttribute", None)
                    
                    setattr(item, "moba_MobaEntityAttribute", self)
                    

    @property
    def moba_MobaEntityIndex(self):
        return self.__moba_MobaEntityIndex

    @moba_MobaEntityIndex.setter
    def moba_MobaEntityIndex(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaEntityIndex__moba_MobaEntityIndex", None)
        self.__moba_MobaEntityIndex = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaEntity76"):
                opp_val = getattr(old_value, "moba_MobaEntity76", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaEntity76"):
                opp_val = getattr(value, "moba_MobaEntity76", None)
                if opp_val is None:
                    setattr(value, "moba_MobaEntity76", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class MobaData:

    pass
class moba_MobaQueue(MobaData):

    def __init__(self, name: str, moba_MobaQueue: "moba_MobaQueue" = None, moba_MobaQueue88: "moba_MobaQueue" = None, moba_MobaQueue91: "moba_MobaCache" = None, moba_MobaQueue94: set["moba_MobaQueueFeature"] = None):
        self.name = name
        self.moba_MobaQueue = moba_MobaQueue
        self.moba_MobaQueue88 = moba_MobaQueue88
        self.moba_MobaQueue91 = moba_MobaQueue91
        self.moba_MobaQueue94 = moba_MobaQueue94 if moba_MobaQueue94 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def moba_MobaQueue(self):
        return self.__moba_MobaQueue

    @moba_MobaQueue.setter
    def moba_MobaQueue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaQueue__moba_MobaQueue", None)
        self.__moba_MobaQueue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaQueue88"):
                opp_val = getattr(old_value, "moba_MobaQueue88", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaQueue88", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaQueue88"):
                opp_val = getattr(value, "moba_MobaQueue88", None)
                setattr(value, "moba_MobaQueue88", self)

    @property
    def moba_MobaQueue94(self):
        return self.__moba_MobaQueue94

    @moba_MobaQueue94.setter
    def moba_MobaQueue94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaQueue__moba_MobaQueue94", None)
        self.__moba_MobaQueue94 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "moba_MobaQueueFeature"):
                    opp_val = getattr(item, "moba_MobaQueueFeature", None)
                    
                    if opp_val == self:
                        setattr(item, "moba_MobaQueueFeature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "moba_MobaQueueFeature"):
                    opp_val = getattr(item, "moba_MobaQueueFeature", None)
                    
                    setattr(item, "moba_MobaQueueFeature", self)
                    

    @property
    def moba_MobaQueue91(self):
        return self.__moba_MobaQueue91

    @moba_MobaQueue91.setter
    def moba_MobaQueue91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaQueue__moba_MobaQueue91", None)
        self.__moba_MobaQueue91 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaCache92"):
                opp_val = getattr(old_value, "moba_MobaCache92", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaCache92", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaCache92"):
                opp_val = getattr(value, "moba_MobaCache92", None)
                setattr(value, "moba_MobaCache92", self)

    @property
    def moba_MobaQueue88(self):
        return self.__moba_MobaQueue88

    @moba_MobaQueue88.setter
    def moba_MobaQueue88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaQueue__moba_MobaQueue88", None)
        self.__moba_MobaQueue88 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaQueue"):
                opp_val = getattr(old_value, "moba_MobaQueue", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaQueue", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaQueue"):
                opp_val = getattr(value, "moba_MobaQueue", None)
                setattr(value, "moba_MobaQueue", self)

class moba_MobaDto(MobaData):

    def __init__(self, name: str, moba_MobaDto87: "moba_MobaTransportSerializationType" = None, moba_MobaDto: "moba_MobaDto" = None, moba_MobaDto79: "moba_MobaDto" = None, moba_MobaDto82: "moba_MobaEntity" = None, moba_MobaDto85: set["moba_MobaDtoFeature"] = None, moba_MobaDto113: "moba_MobaRESTPayloadDefinition" = None, moba_MobaDto178: "moba_MobaDtoEmbeddable" = None, moba_MobaDto173: "moba_MobaDtoReference" = None):
        self.name = name
        self.moba_MobaDto87 = moba_MobaDto87
        self.moba_MobaDto = moba_MobaDto
        self.moba_MobaDto79 = moba_MobaDto79
        self.moba_MobaDto82 = moba_MobaDto82
        self.moba_MobaDto85 = moba_MobaDto85 if moba_MobaDto85 is not None else set()
        self.moba_MobaDto113 = moba_MobaDto113
        self.moba_MobaDto178 = moba_MobaDto178
        self.moba_MobaDto173 = moba_MobaDto173
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def moba_MobaDto(self):
        return self.__moba_MobaDto

    @moba_MobaDto.setter
    def moba_MobaDto(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaDto__moba_MobaDto", None)
        self.__moba_MobaDto = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaDto79"):
                opp_val = getattr(old_value, "moba_MobaDto79", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaDto79", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaDto79"):
                opp_val = getattr(value, "moba_MobaDto79", None)
                setattr(value, "moba_MobaDto79", self)

    @property
    def moba_MobaDto87(self):
        return self.__moba_MobaDto87

    @moba_MobaDto87.setter
    def moba_MobaDto87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaDto__moba_MobaDto87", None)
        self.__moba_MobaDto87 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaTransportSerializationType"):
                opp_val = getattr(old_value, "moba_MobaTransportSerializationType", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaTransportSerializationType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaTransportSerializationType"):
                opp_val = getattr(value, "moba_MobaTransportSerializationType", None)
                setattr(value, "moba_MobaTransportSerializationType", self)

    @property
    def moba_MobaDto173(self):
        return self.__moba_MobaDto173

    @moba_MobaDto173.setter
    def moba_MobaDto173(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaDto__moba_MobaDto173", None)
        self.__moba_MobaDto173 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaDtoReference"):
                opp_val = getattr(old_value, "moba_MobaDtoReference", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaDtoReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaDtoReference"):
                opp_val = getattr(value, "moba_MobaDtoReference", None)
                setattr(value, "moba_MobaDtoReference", self)

    @property
    def moba_MobaDto79(self):
        return self.__moba_MobaDto79

    @moba_MobaDto79.setter
    def moba_MobaDto79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaDto__moba_MobaDto79", None)
        self.__moba_MobaDto79 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaDto"):
                opp_val = getattr(old_value, "moba_MobaDto", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaDto", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaDto"):
                opp_val = getattr(value, "moba_MobaDto", None)
                setattr(value, "moba_MobaDto", self)

    @property
    def moba_MobaDto85(self):
        return self.__moba_MobaDto85

    @moba_MobaDto85.setter
    def moba_MobaDto85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaDto__moba_MobaDto85", None)
        self.__moba_MobaDto85 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "moba_MobaDtoFeature"):
                    opp_val = getattr(item, "moba_MobaDtoFeature", None)
                    
                    if opp_val == self:
                        setattr(item, "moba_MobaDtoFeature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "moba_MobaDtoFeature"):
                    opp_val = getattr(item, "moba_MobaDtoFeature", None)
                    
                    setattr(item, "moba_MobaDtoFeature", self)
                    

    @property
    def moba_MobaDto113(self):
        return self.__moba_MobaDto113

    @moba_MobaDto113.setter
    def moba_MobaDto113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaDto__moba_MobaDto113", None)
        self.__moba_MobaDto113 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaRESTPayloadDefinition112"):
                opp_val = getattr(old_value, "moba_MobaRESTPayloadDefinition112", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaRESTPayloadDefinition112", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaRESTPayloadDefinition112"):
                opp_val = getattr(value, "moba_MobaRESTPayloadDefinition112", None)
                setattr(value, "moba_MobaRESTPayloadDefinition112", self)

    @property
    def moba_MobaDto82(self):
        return self.__moba_MobaDto82

    @moba_MobaDto82.setter
    def moba_MobaDto82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaDto__moba_MobaDto82", None)
        self.__moba_MobaDto82 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaEntity83"):
                opp_val = getattr(old_value, "moba_MobaEntity83", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaEntity83", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaEntity83"):
                opp_val = getattr(value, "moba_MobaEntity83", None)
                setattr(value, "moba_MobaEntity83", self)

    @property
    def moba_MobaDto178(self):
        return self.__moba_MobaDto178

    @moba_MobaDto178.setter
    def moba_MobaDto178(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaDto__moba_MobaDto178", None)
        self.__moba_MobaDto178 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaDtoEmbeddable"):
                opp_val = getattr(old_value, "moba_MobaDtoEmbeddable", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaDtoEmbeddable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaDtoEmbeddable"):
                opp_val = getattr(value, "moba_MobaDtoEmbeddable", None)
                setattr(value, "moba_MobaDtoEmbeddable", self)

class moba_MobaEntity(MobaData):

    def __init__(self, name: str, moba_MobaEntity: "moba_MobaSettingsEntityReference" = None, moba_MobaEntity69: "moba_MobaEntity" = None, moba_MobaEntity67: "moba_MobaEntity" = None, moba_MobaEntity71: "moba_MobaCache" = None, moba_MobaEntity74: set["moba_MobaEntityFeature"] = None, moba_MobaEntity76: set["moba_MobaEntityIndex"] = None, moba_MobaEntity83: "moba_MobaDto" = None, moba_MobaEntity161: "moba_MobaEntityReference" = None, moba_MobaEntity166: "moba_MobaEntityEmbeddable" = None):
        self.name = name
        self.moba_MobaEntity = moba_MobaEntity
        self.moba_MobaEntity69 = moba_MobaEntity69
        self.moba_MobaEntity67 = moba_MobaEntity67
        self.moba_MobaEntity71 = moba_MobaEntity71
        self.moba_MobaEntity74 = moba_MobaEntity74 if moba_MobaEntity74 is not None else set()
        self.moba_MobaEntity76 = moba_MobaEntity76 if moba_MobaEntity76 is not None else set()
        self.moba_MobaEntity83 = moba_MobaEntity83
        self.moba_MobaEntity161 = moba_MobaEntity161
        self.moba_MobaEntity166 = moba_MobaEntity166
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def moba_MobaEntity71(self):
        return self.__moba_MobaEntity71

    @moba_MobaEntity71.setter
    def moba_MobaEntity71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaEntity__moba_MobaEntity71", None)
        self.__moba_MobaEntity71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaCache72"):
                opp_val = getattr(old_value, "moba_MobaCache72", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaCache72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaCache72"):
                opp_val = getattr(value, "moba_MobaCache72", None)
                setattr(value, "moba_MobaCache72", self)

    @property
    def moba_MobaEntity83(self):
        return self.__moba_MobaEntity83

    @moba_MobaEntity83.setter
    def moba_MobaEntity83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaEntity__moba_MobaEntity83", None)
        self.__moba_MobaEntity83 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaDto82"):
                opp_val = getattr(old_value, "moba_MobaDto82", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaDto82", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaDto82"):
                opp_val = getattr(value, "moba_MobaDto82", None)
                setattr(value, "moba_MobaDto82", self)

    @property
    def moba_MobaEntity67(self):
        return self.__moba_MobaEntity67

    @moba_MobaEntity67.setter
    def moba_MobaEntity67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaEntity__moba_MobaEntity67", None)
        self.__moba_MobaEntity67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaEntity69"):
                opp_val = getattr(old_value, "moba_MobaEntity69", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaEntity69", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaEntity69"):
                opp_val = getattr(value, "moba_MobaEntity69", None)
                setattr(value, "moba_MobaEntity69", self)

    @property
    def moba_MobaEntity161(self):
        return self.__moba_MobaEntity161

    @moba_MobaEntity161.setter
    def moba_MobaEntity161(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaEntity__moba_MobaEntity161", None)
        self.__moba_MobaEntity161 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaEntityReference"):
                opp_val = getattr(old_value, "moba_MobaEntityReference", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaEntityReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaEntityReference"):
                opp_val = getattr(value, "moba_MobaEntityReference", None)
                setattr(value, "moba_MobaEntityReference", self)

    @property
    def moba_MobaEntity69(self):
        return self.__moba_MobaEntity69

    @moba_MobaEntity69.setter
    def moba_MobaEntity69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaEntity__moba_MobaEntity69", None)
        self.__moba_MobaEntity69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaEntity67"):
                opp_val = getattr(old_value, "moba_MobaEntity67", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaEntity67", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaEntity67"):
                opp_val = getattr(value, "moba_MobaEntity67", None)
                setattr(value, "moba_MobaEntity67", self)

    @property
    def moba_MobaEntity74(self):
        return self.__moba_MobaEntity74

    @moba_MobaEntity74.setter
    def moba_MobaEntity74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaEntity__moba_MobaEntity74", None)
        self.__moba_MobaEntity74 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "moba_MobaEntityFeature"):
                    opp_val = getattr(item, "moba_MobaEntityFeature", None)
                    
                    if opp_val == self:
                        setattr(item, "moba_MobaEntityFeature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "moba_MobaEntityFeature"):
                    opp_val = getattr(item, "moba_MobaEntityFeature", None)
                    
                    setattr(item, "moba_MobaEntityFeature", self)
                    

    @property
    def moba_MobaEntity76(self):
        return self.__moba_MobaEntity76

    @moba_MobaEntity76.setter
    def moba_MobaEntity76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaEntity__moba_MobaEntity76", None)
        self.__moba_MobaEntity76 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "moba_MobaEntityIndex"):
                    opp_val = getattr(item, "moba_MobaEntityIndex", None)
                    
                    if opp_val == self:
                        setattr(item, "moba_MobaEntityIndex", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "moba_MobaEntityIndex"):
                    opp_val = getattr(item, "moba_MobaEntityIndex", None)
                    
                    setattr(item, "moba_MobaEntityIndex", self)
                    

    @property
    def moba_MobaEntity166(self):
        return self.__moba_MobaEntity166

    @moba_MobaEntity166.setter
    def moba_MobaEntity166(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaEntity__moba_MobaEntity166", None)
        self.__moba_MobaEntity166 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaEntityEmbeddable"):
                opp_val = getattr(old_value, "moba_MobaEntityEmbeddable", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaEntityEmbeddable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaEntityEmbeddable"):
                opp_val = getattr(value, "moba_MobaEntityEmbeddable", None)
                setattr(value, "moba_MobaEntityEmbeddable", self)

    @property
    def moba_MobaEntity(self):
        return self.__moba_MobaEntity

    @moba_MobaEntity.setter
    def moba_MobaEntity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaEntity__moba_MobaEntity", None)
        self.__moba_MobaEntity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaSettingsEntityReference"):
                opp_val = getattr(old_value, "moba_MobaSettingsEntityReference", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaSettingsEntityReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaSettingsEntityReference"):
                opp_val = getattr(value, "moba_MobaSettingsEntityReference", None)
                setattr(value, "moba_MobaSettingsEntityReference", self)

class moba_MobaProperty:

    def __init__(self, key: str, value: str, keyString: str, valueString: str, moba_MobaProperty: "moba_MobaPropertiesAble" = None, moba_MobaProperty52: "moba_MobaConstant" = None, moba_MobaProperty55: "moba_MobaConstant" = None):
        self.key = key
        self.value = value
        self.keyString = keyString
        self.valueString = valueString
        self.moba_MobaProperty = moba_MobaProperty
        self.moba_MobaProperty52 = moba_MobaProperty52
        self.moba_MobaProperty55 = moba_MobaProperty55
        
    @property
    def valueString(self) -> str:
        return self.__valueString

    @valueString.setter
    def valueString(self, valueString: str):
        self.__valueString = valueString

    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def keyString(self) -> str:
        return self.__keyString

    @keyString.setter
    def keyString(self, keyString: str):
        self.__keyString = keyString

    @property
    def moba_MobaProperty(self):
        return self.__moba_MobaProperty

    @moba_MobaProperty.setter
    def moba_MobaProperty(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaProperty__moba_MobaProperty", None)
        self.__moba_MobaProperty = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaPropertiesAble"):
                opp_val = getattr(old_value, "moba_MobaPropertiesAble", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaPropertiesAble"):
                opp_val = getattr(value, "moba_MobaPropertiesAble", None)
                if opp_val is None:
                    setattr(value, "moba_MobaPropertiesAble", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def moba_MobaProperty52(self):
        return self.__moba_MobaProperty52

    @moba_MobaProperty52.setter
    def moba_MobaProperty52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaProperty__moba_MobaProperty52", None)
        self.__moba_MobaProperty52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaConstant53"):
                opp_val = getattr(old_value, "moba_MobaConstant53", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaConstant53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaConstant53"):
                opp_val = getattr(value, "moba_MobaConstant53", None)
                setattr(value, "moba_MobaConstant53", self)

    @property
    def moba_MobaProperty55(self):
        return self.__moba_MobaProperty55

    @moba_MobaProperty55.setter
    def moba_MobaProperty55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaProperty__moba_MobaProperty55", None)
        self.__moba_MobaProperty55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaConstant56"):
                opp_val = getattr(old_value, "moba_MobaConstant56", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaConstant56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaConstant56"):
                opp_val = getattr(value, "moba_MobaConstant56", None)
                setattr(value, "moba_MobaConstant56", self)

class moba_MobaPropertiesAble(ABC):

    pass
class MobaMultiplicityAble:

    pass
class moba_MobaEntityEmbeddable(MobaEntityFeature, MobaMultiplicityAble):

    def __init__(self, transient: bool, moba_MobaEntityEmbeddable: "moba_MobaEntity" = None):
        self.transient = transient
        self.moba_MobaEntityEmbeddable = moba_MobaEntityEmbeddable
        
    @property
    def transient(self) -> bool:
        return self.__transient

    @transient.setter
    def transient(self, transient: bool):
        self.__transient = transient

    @property
    def moba_MobaEntityEmbeddable(self):
        return self.__moba_MobaEntityEmbeddable

    @moba_MobaEntityEmbeddable.setter
    def moba_MobaEntityEmbeddable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaEntityEmbeddable__moba_MobaEntityEmbeddable", None)
        self.__moba_MobaEntityEmbeddable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaEntity166"):
                opp_val = getattr(old_value, "moba_MobaEntity166", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaEntity166", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaEntity166"):
                opp_val = getattr(value, "moba_MobaEntity166", None)
                setattr(value, "moba_MobaEntity166", self)

class moba_MobaEntityReference(MobaEntityFeature, MobaMultiplicityAble):

    def __init__(self, cascading: bool, lazy: bool, transient: bool, moba_MobaEntityReference: "moba_MobaEntity" = None, moba_MobaEntityReference164: "moba_MobaEntityReference" = None, moba_MobaEntityReference162: "moba_MobaEntityReference" = None):
        self.cascading = cascading
        self.lazy = lazy
        self.transient = transient
        self.moba_MobaEntityReference = moba_MobaEntityReference
        self.moba_MobaEntityReference164 = moba_MobaEntityReference164
        self.moba_MobaEntityReference162 = moba_MobaEntityReference162
        
    @property
    def transient(self) -> bool:
        return self.__transient

    @transient.setter
    def transient(self, transient: bool):
        self.__transient = transient

    @property
    def lazy(self) -> bool:
        return self.__lazy

    @lazy.setter
    def lazy(self, lazy: bool):
        self.__lazy = lazy

    @property
    def cascading(self) -> bool:
        return self.__cascading

    @cascading.setter
    def cascading(self, cascading: bool):
        self.__cascading = cascading

    @property
    def moba_MobaEntityReference164(self):
        return self.__moba_MobaEntityReference164

    @moba_MobaEntityReference164.setter
    def moba_MobaEntityReference164(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaEntityReference__moba_MobaEntityReference164", None)
        self.__moba_MobaEntityReference164 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaEntityReference162"):
                opp_val = getattr(old_value, "moba_MobaEntityReference162", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaEntityReference162", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaEntityReference162"):
                opp_val = getattr(value, "moba_MobaEntityReference162", None)
                setattr(value, "moba_MobaEntityReference162", self)

    @property
    def moba_MobaEntityReference162(self):
        return self.__moba_MobaEntityReference162

    @moba_MobaEntityReference162.setter
    def moba_MobaEntityReference162(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaEntityReference__moba_MobaEntityReference162", None)
        self.__moba_MobaEntityReference162 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaEntityReference164"):
                opp_val = getattr(old_value, "moba_MobaEntityReference164", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaEntityReference164", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaEntityReference164"):
                opp_val = getattr(value, "moba_MobaEntityReference164", None)
                setattr(value, "moba_MobaEntityReference164", self)

    @property
    def moba_MobaEntityReference(self):
        return self.__moba_MobaEntityReference

    @moba_MobaEntityReference.setter
    def moba_MobaEntityReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaEntityReference__moba_MobaEntityReference", None)
        self.__moba_MobaEntityReference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaEntity161"):
                opp_val = getattr(old_value, "moba_MobaEntity161", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaEntity161", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaEntity161"):
                opp_val = getattr(value, "moba_MobaEntity161", None)
                setattr(value, "moba_MobaEntity161", self)

class moba_MobaDtoReference(MobaDtoFeature, MobaMultiplicityAble):

    def __init__(self, cascading: bool, lazy: bool, transient: bool, alias: str, moba_MobaDtoReference: "moba_MobaDto" = None, moba_MobaDtoReference176: "moba_MobaDtoReference" = None, moba_MobaDtoReference174: "moba_MobaDtoReference" = None):
        self.cascading = cascading
        self.lazy = lazy
        self.transient = transient
        self.alias = alias
        self.moba_MobaDtoReference = moba_MobaDtoReference
        self.moba_MobaDtoReference176 = moba_MobaDtoReference176
        self.moba_MobaDtoReference174 = moba_MobaDtoReference174
        
    @property
    def lazy(self) -> bool:
        return self.__lazy

    @lazy.setter
    def lazy(self, lazy: bool):
        self.__lazy = lazy

    @property
    def transient(self) -> bool:
        return self.__transient

    @transient.setter
    def transient(self, transient: bool):
        self.__transient = transient

    @property
    def alias(self) -> str:
        return self.__alias

    @alias.setter
    def alias(self, alias: str):
        self.__alias = alias

    @property
    def cascading(self) -> bool:
        return self.__cascading

    @cascading.setter
    def cascading(self, cascading: bool):
        self.__cascading = cascading

    @property
    def moba_MobaDtoReference176(self):
        return self.__moba_MobaDtoReference176

    @moba_MobaDtoReference176.setter
    def moba_MobaDtoReference176(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaDtoReference__moba_MobaDtoReference176", None)
        self.__moba_MobaDtoReference176 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaDtoReference174"):
                opp_val = getattr(old_value, "moba_MobaDtoReference174", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaDtoReference174", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaDtoReference174"):
                opp_val = getattr(value, "moba_MobaDtoReference174", None)
                setattr(value, "moba_MobaDtoReference174", self)

    @property
    def moba_MobaDtoReference(self):
        return self.__moba_MobaDtoReference

    @moba_MobaDtoReference.setter
    def moba_MobaDtoReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaDtoReference__moba_MobaDtoReference", None)
        self.__moba_MobaDtoReference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaDto173"):
                opp_val = getattr(old_value, "moba_MobaDto173", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaDto173", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaDto173"):
                opp_val = getattr(value, "moba_MobaDto173", None)
                setattr(value, "moba_MobaDto173", self)

    @property
    def moba_MobaDtoReference174(self):
        return self.__moba_MobaDtoReference174

    @moba_MobaDtoReference174.setter
    def moba_MobaDtoReference174(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaDtoReference__moba_MobaDtoReference174", None)
        self.__moba_MobaDtoReference174 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaDtoReference176"):
                opp_val = getattr(old_value, "moba_MobaDtoReference176", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaDtoReference176", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaDtoReference176"):
                opp_val = getattr(value, "moba_MobaDtoReference176", None)
                setattr(value, "moba_MobaDtoReference176", self)

class moba_MobaDtoEmbeddable(MobaMultiplicityAble, MobaDtoFeature):

    def __init__(self, transient: bool, alias: str, moba_MobaDtoEmbeddable: "moba_MobaDto" = None):
        self.transient = transient
        self.alias = alias
        self.moba_MobaDtoEmbeddable = moba_MobaDtoEmbeddable
        
    @property
    def transient(self) -> bool:
        return self.__transient

    @transient.setter
    def transient(self, transient: bool):
        self.__transient = transient

    @property
    def alias(self) -> str:
        return self.__alias

    @alias.setter
    def alias(self, alias: str):
        self.__alias = alias

    @property
    def moba_MobaDtoEmbeddable(self):
        return self.__moba_MobaDtoEmbeddable

    @moba_MobaDtoEmbeddable.setter
    def moba_MobaDtoEmbeddable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaDtoEmbeddable__moba_MobaDtoEmbeddable", None)
        self.__moba_MobaDtoEmbeddable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaDto178"):
                opp_val = getattr(old_value, "moba_MobaDto178", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaDto178", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaDto178"):
                opp_val = getattr(value, "moba_MobaDto178", None)
                setattr(value, "moba_MobaDto178", self)

class MobaSettingsFeature:

    pass
class MobaFeature:

    pass
class moba_MobaEntityFeature(MobaFeature):

    pass
class moba_MobaQueueFeature(MobaFeature):

    pass
class moba_MobaDtoFeature(MobaFeature):

    pass
class moba_MobaSettingsFeature(MobaFeature):

    pass
class moba_MobaConstantValue:

    def __init__(self, valueString: str, valueConstFunctions: str, valueConstToLowerCase: bool, valueInt: str, valueDouble: str, moba_MobaConstantValue: "moba_MobaConstant" = None, moba_MobaConstantValue45: "moba_MobaConstant" = None, moba_MobaConstantValue49: "moba_MobaConstantValue" = None, moba_MobaConstantValue47: "moba_MobaConstantValue" = None):
        self.valueString = valueString
        self.valueConstFunctions = valueConstFunctions
        self.valueConstToLowerCase = valueConstToLowerCase
        self.valueInt = valueInt
        self.valueDouble = valueDouble
        self.moba_MobaConstantValue = moba_MobaConstantValue
        self.moba_MobaConstantValue45 = moba_MobaConstantValue45
        self.moba_MobaConstantValue49 = moba_MobaConstantValue49
        self.moba_MobaConstantValue47 = moba_MobaConstantValue47
        
    @property
    def valueConstFunctions(self) -> str:
        return self.__valueConstFunctions

    @valueConstFunctions.setter
    def valueConstFunctions(self, valueConstFunctions: str):
        self.__valueConstFunctions = valueConstFunctions

    @property
    def valueInt(self) -> str:
        return self.__valueInt

    @valueInt.setter
    def valueInt(self, valueInt: str):
        self.__valueInt = valueInt

    @property
    def valueDouble(self) -> str:
        return self.__valueDouble

    @valueDouble.setter
    def valueDouble(self, valueDouble: str):
        self.__valueDouble = valueDouble

    @property
    def valueConstToLowerCase(self) -> bool:
        return self.__valueConstToLowerCase

    @valueConstToLowerCase.setter
    def valueConstToLowerCase(self, valueConstToLowerCase: bool):
        self.__valueConstToLowerCase = valueConstToLowerCase

    @property
    def valueString(self) -> str:
        return self.__valueString

    @valueString.setter
    def valueString(self, valueString: str):
        self.__valueString = valueString

    @property
    def moba_MobaConstantValue45(self):
        return self.__moba_MobaConstantValue45

    @moba_MobaConstantValue45.setter
    def moba_MobaConstantValue45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaConstantValue__moba_MobaConstantValue45", None)
        self.__moba_MobaConstantValue45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaConstant46"):
                opp_val = getattr(old_value, "moba_MobaConstant46", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaConstant46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaConstant46"):
                opp_val = getattr(value, "moba_MobaConstant46", None)
                setattr(value, "moba_MobaConstant46", self)

    @property
    def moba_MobaConstantValue(self):
        return self.__moba_MobaConstantValue

    @moba_MobaConstantValue.setter
    def moba_MobaConstantValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaConstantValue__moba_MobaConstantValue", None)
        self.__moba_MobaConstantValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaConstant32"):
                opp_val = getattr(old_value, "moba_MobaConstant32", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaConstant32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaConstant32"):
                opp_val = getattr(value, "moba_MobaConstant32", None)
                setattr(value, "moba_MobaConstant32", self)

    @property
    def moba_MobaConstantValue47(self):
        return self.__moba_MobaConstantValue47

    @moba_MobaConstantValue47.setter
    def moba_MobaConstantValue47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaConstantValue__moba_MobaConstantValue47", None)
        self.__moba_MobaConstantValue47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaConstantValue49"):
                opp_val = getattr(old_value, "moba_MobaConstantValue49", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaConstantValue49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaConstantValue49"):
                opp_val = getattr(value, "moba_MobaConstantValue49", None)
                setattr(value, "moba_MobaConstantValue49", self)

    @property
    def moba_MobaConstantValue49(self):
        return self.__moba_MobaConstantValue49

    @moba_MobaConstantValue49.setter
    def moba_MobaConstantValue49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaConstantValue__moba_MobaConstantValue49", None)
        self.__moba_MobaConstantValue49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaConstantValue47"):
                opp_val = getattr(old_value, "moba_MobaConstantValue47", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaConstantValue47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaConstantValue47"):
                opp_val = getattr(value, "moba_MobaConstantValue47", None)
                setattr(value, "moba_MobaConstantValue47", self)

class MobaGeneratorFeature:

    pass
class moba_MobaGeneratorMixinFeature(MobaGeneratorFeature):

    pass
class moba_MobaGeneratorFeature(ABC):

    pass
class MobaConstraintable:

    pass
class moba_MobaSettingsEntityReference(MobaMultiplicityAble, MobaSettingsFeature, MobaConstraintable):

    def __init__(self, cascading: bool, lazy: bool, transient: bool, moba_MobaSettingsEntityReference: "moba_MobaEntity" = None):
        self.cascading = cascading
        self.lazy = lazy
        self.transient = transient
        self.moba_MobaSettingsEntityReference = moba_MobaSettingsEntityReference
        
    @property
    def cascading(self) -> bool:
        return self.__cascading

    @cascading.setter
    def cascading(self, cascading: bool):
        self.__cascading = cascading

    @property
    def transient(self) -> bool:
        return self.__transient

    @transient.setter
    def transient(self, transient: bool):
        self.__transient = transient

    @property
    def lazy(self) -> bool:
        return self.__lazy

    @lazy.setter
    def lazy(self, lazy: bool):
        self.__lazy = lazy

    @property
    def moba_MobaSettingsEntityReference(self):
        return self.__moba_MobaSettingsEntityReference

    @moba_MobaSettingsEntityReference.setter
    def moba_MobaSettingsEntityReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaSettingsEntityReference__moba_MobaSettingsEntityReference", None)
        self.__moba_MobaSettingsEntityReference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaEntity"):
                opp_val = getattr(old_value, "moba_MobaEntity", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaEntity", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaEntity"):
                opp_val = getattr(value, "moba_MobaEntity", None)
                setattr(value, "moba_MobaEntity", self)

class moba_MobaSettingsAttribute(MobaConstraintable, MobaSettingsFeature, MobaMultiplicityAble):

    def __init__(self, lazy: bool, transient: bool, formatString: str, domainKey: bool, domainDescription: bool, moba_MobaSettingsAttribute64: "moba_MobaConstant" = None, moba_MobaSettingsAttribute: "moba_MobaDataType" = None):
        self.lazy = lazy
        self.transient = transient
        self.formatString = formatString
        self.domainKey = domainKey
        self.domainDescription = domainDescription
        self.moba_MobaSettingsAttribute64 = moba_MobaSettingsAttribute64
        self.moba_MobaSettingsAttribute = moba_MobaSettingsAttribute
        
    @property
    def domainKey(self) -> bool:
        return self.__domainKey

    @domainKey.setter
    def domainKey(self, domainKey: bool):
        self.__domainKey = domainKey

    @property
    def formatString(self) -> str:
        return self.__formatString

    @formatString.setter
    def formatString(self, formatString: str):
        self.__formatString = formatString

    @property
    def transient(self) -> bool:
        return self.__transient

    @transient.setter
    def transient(self, transient: bool):
        self.__transient = transient

    @property
    def lazy(self) -> bool:
        return self.__lazy

    @lazy.setter
    def lazy(self, lazy: bool):
        self.__lazy = lazy

    @property
    def domainDescription(self) -> bool:
        return self.__domainDescription

    @domainDescription.setter
    def domainDescription(self, domainDescription: bool):
        self.__domainDescription = domainDescription

    @property
    def moba_MobaSettingsAttribute64(self):
        return self.__moba_MobaSettingsAttribute64

    @moba_MobaSettingsAttribute64.setter
    def moba_MobaSettingsAttribute64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaSettingsAttribute__moba_MobaSettingsAttribute64", None)
        self.__moba_MobaSettingsAttribute64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaConstant65"):
                opp_val = getattr(old_value, "moba_MobaConstant65", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaConstant65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaConstant65"):
                opp_val = getattr(value, "moba_MobaConstant65", None)
                setattr(value, "moba_MobaConstant65", self)

    @property
    def moba_MobaSettingsAttribute(self):
        return self.__moba_MobaSettingsAttribute

    @moba_MobaSettingsAttribute.setter
    def moba_MobaSettingsAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaSettingsAttribute__moba_MobaSettingsAttribute", None)
        self.__moba_MobaSettingsAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaDataType62"):
                opp_val = getattr(old_value, "moba_MobaDataType62", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaDataType62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaDataType62"):
                opp_val = getattr(value, "moba_MobaDataType62", None)
                setattr(value, "moba_MobaDataType62", self)

class moba_MobaDtoAttribute(MobaMultiplicityAble, MobaDtoFeature, MobaConstraintable):

    def __init__(self, lazy: bool, transient: bool, domainKey: bool, domainDescription: bool, alias: str, formatString: str, moba_MobaDtoAttribute: "moba_MobaDataType" = None, moba_MobaDtoAttribute170: "moba_MobaConstant" = None):
        self.lazy = lazy
        self.transient = transient
        self.domainKey = domainKey
        self.domainDescription = domainDescription
        self.alias = alias
        self.formatString = formatString
        self.moba_MobaDtoAttribute = moba_MobaDtoAttribute
        self.moba_MobaDtoAttribute170 = moba_MobaDtoAttribute170
        
    @property
    def lazy(self) -> bool:
        return self.__lazy

    @lazy.setter
    def lazy(self, lazy: bool):
        self.__lazy = lazy

    @property
    def domainDescription(self) -> bool:
        return self.__domainDescription

    @domainDescription.setter
    def domainDescription(self, domainDescription: bool):
        self.__domainDescription = domainDescription

    @property
    def domainKey(self) -> bool:
        return self.__domainKey

    @domainKey.setter
    def domainKey(self, domainKey: bool):
        self.__domainKey = domainKey

    @property
    def transient(self) -> bool:
        return self.__transient

    @transient.setter
    def transient(self, transient: bool):
        self.__transient = transient

    @property
    def formatString(self) -> str:
        return self.__formatString

    @formatString.setter
    def formatString(self, formatString: str):
        self.__formatString = formatString

    @property
    def alias(self) -> str:
        return self.__alias

    @alias.setter
    def alias(self, alias: str):
        self.__alias = alias

    @property
    def moba_MobaDtoAttribute170(self):
        return self.__moba_MobaDtoAttribute170

    @moba_MobaDtoAttribute170.setter
    def moba_MobaDtoAttribute170(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaDtoAttribute__moba_MobaDtoAttribute170", None)
        self.__moba_MobaDtoAttribute170 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaConstant171"):
                opp_val = getattr(old_value, "moba_MobaConstant171", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaConstant171", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaConstant171"):
                opp_val = getattr(value, "moba_MobaConstant171", None)
                setattr(value, "moba_MobaConstant171", self)

    @property
    def moba_MobaDtoAttribute(self):
        return self.__moba_MobaDtoAttribute

    @moba_MobaDtoAttribute.setter
    def moba_MobaDtoAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaDtoAttribute__moba_MobaDtoAttribute", None)
        self.__moba_MobaDtoAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaDataType168"):
                opp_val = getattr(old_value, "moba_MobaDataType168", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaDataType168", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaDataType168"):
                opp_val = getattr(value, "moba_MobaDataType168", None)
                setattr(value, "moba_MobaDataType168", self)

class moba_MobaEntityAttribute(MobaEntityFeature, MobaMultiplicityAble, MobaConstraintable):

    def __init__(self, lazy: bool, transient: bool, domainKey: bool, domainDescription: bool, formatString: str, moba_MobaEntityAttribute: "moba_MobaEntityIndex" = None, moba_MobaEntityAttribute157: "moba_MobaConstant" = None, moba_MobaEntityAttribute154: "moba_MobaDataType" = None):
        self.lazy = lazy
        self.transient = transient
        self.domainKey = domainKey
        self.domainDescription = domainDescription
        self.formatString = formatString
        self.moba_MobaEntityAttribute = moba_MobaEntityAttribute
        self.moba_MobaEntityAttribute157 = moba_MobaEntityAttribute157
        self.moba_MobaEntityAttribute154 = moba_MobaEntityAttribute154
        
    @property
    def domainDescription(self) -> bool:
        return self.__domainDescription

    @domainDescription.setter
    def domainDescription(self, domainDescription: bool):
        self.__domainDescription = domainDescription

    @property
    def domainKey(self) -> bool:
        return self.__domainKey

    @domainKey.setter
    def domainKey(self, domainKey: bool):
        self.__domainKey = domainKey

    @property
    def transient(self) -> bool:
        return self.__transient

    @transient.setter
    def transient(self, transient: bool):
        self.__transient = transient

    @property
    def formatString(self) -> str:
        return self.__formatString

    @formatString.setter
    def formatString(self, formatString: str):
        self.__formatString = formatString

    @property
    def lazy(self) -> bool:
        return self.__lazy

    @lazy.setter
    def lazy(self, lazy: bool):
        self.__lazy = lazy

    @property
    def moba_MobaEntityAttribute(self):
        return self.__moba_MobaEntityAttribute

    @moba_MobaEntityAttribute.setter
    def moba_MobaEntityAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaEntityAttribute__moba_MobaEntityAttribute", None)
        self.__moba_MobaEntityAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaEntityIndex78"):
                opp_val = getattr(old_value, "moba_MobaEntityIndex78", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaEntityIndex78"):
                opp_val = getattr(value, "moba_MobaEntityIndex78", None)
                if opp_val is None:
                    setattr(value, "moba_MobaEntityIndex78", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def moba_MobaEntityAttribute157(self):
        return self.__moba_MobaEntityAttribute157

    @moba_MobaEntityAttribute157.setter
    def moba_MobaEntityAttribute157(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaEntityAttribute__moba_MobaEntityAttribute157", None)
        self.__moba_MobaEntityAttribute157 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaConstant158"):
                opp_val = getattr(old_value, "moba_MobaConstant158", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaConstant158", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaConstant158"):
                opp_val = getattr(value, "moba_MobaConstant158", None)
                setattr(value, "moba_MobaConstant158", self)

    @property
    def moba_MobaEntityAttribute154(self):
        return self.__moba_MobaEntityAttribute154

    @moba_MobaEntityAttribute154.setter
    def moba_MobaEntityAttribute154(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaEntityAttribute__moba_MobaEntityAttribute154", None)
        self.__moba_MobaEntityAttribute154 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaDataType155"):
                opp_val = getattr(old_value, "moba_MobaDataType155", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaDataType155", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaDataType155"):
                opp_val = getattr(value, "moba_MobaDataType155", None)
                setattr(value, "moba_MobaDataType155", self)

class moba_MobaGeneratorIDFeature(MobaGeneratorFeature):

    def __init__(self, generatorId: str, generatorVersion: str):
        self.generatorId = generatorId
        self.generatorVersion = generatorVersion
        
    @property
    def generatorId(self) -> str:
        return self.__generatorId

    @generatorId.setter
    def generatorId(self, generatorId: str):
        self.__generatorId = generatorId

    @property
    def generatorVersion(self) -> str:
        return self.__generatorVersion

    @generatorVersion.setter
    def generatorVersion(self, generatorVersion: str):
        self.__generatorVersion = generatorVersion

class MobaApplicationFeature:

    pass
class moba_MobaPersistenceType(MobaApplicationFeature):

    def __init__(self, name: str, moba_MobaPersistenceType: "moba_MobaCache" = None):
        self.name = name
        self.moba_MobaPersistenceType = moba_MobaPersistenceType
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def moba_MobaPersistenceType(self):
        return self.__moba_MobaPersistenceType

    @moba_MobaPersistenceType.setter
    def moba_MobaPersistenceType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaPersistenceType__moba_MobaPersistenceType", None)
        self.__moba_MobaPersistenceType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaCache43"):
                opp_val = getattr(old_value, "moba_MobaCache43", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaCache43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaCache43"):
                opp_val = getattr(value, "moba_MobaCache43", None)
                setattr(value, "moba_MobaCache43", self)

class moba_MobaExternalModule(MobaApplicationFeature):

    def __init__(self, name: str, moba_MobaExternalModule: "moba_MobaExternalModule" = None, moba_MobaExternalModule205: "moba_MobaExternalModule" = None):
        self.name = name
        self.moba_MobaExternalModule = moba_MobaExternalModule
        self.moba_MobaExternalModule205 = moba_MobaExternalModule205
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def moba_MobaExternalModule(self):
        return self.__moba_MobaExternalModule

    @moba_MobaExternalModule.setter
    def moba_MobaExternalModule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaExternalModule__moba_MobaExternalModule", None)
        self.__moba_MobaExternalModule = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaExternalModule205"):
                opp_val = getattr(old_value, "moba_MobaExternalModule205", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaExternalModule205", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaExternalModule205"):
                opp_val = getattr(value, "moba_MobaExternalModule205", None)
                setattr(value, "moba_MobaExternalModule205", self)

    @property
    def moba_MobaExternalModule205(self):
        return self.__moba_MobaExternalModule205

    @moba_MobaExternalModule205.setter
    def moba_MobaExternalModule205(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaExternalModule__moba_MobaExternalModule205", None)
        self.__moba_MobaExternalModule205 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaExternalModule"):
                opp_val = getattr(old_value, "moba_MobaExternalModule", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaExternalModule", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaExternalModule"):
                opp_val = getattr(value, "moba_MobaExternalModule", None)
                setattr(value, "moba_MobaExternalModule", self)

class moba_MobaTrigger(MobaApplicationFeature):

    def __init__(self, name: str, moba_MobaTrigger: "moba_MobaTrigger" = None, moba_MobaTrigger199: "moba_MobaTrigger" = None):
        self.name = name
        self.moba_MobaTrigger = moba_MobaTrigger
        self.moba_MobaTrigger199 = moba_MobaTrigger199
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def moba_MobaTrigger199(self):
        return self.__moba_MobaTrigger199

    @moba_MobaTrigger199.setter
    def moba_MobaTrigger199(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaTrigger__moba_MobaTrigger199", None)
        self.__moba_MobaTrigger199 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaTrigger"):
                opp_val = getattr(old_value, "moba_MobaTrigger", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaTrigger", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaTrigger"):
                opp_val = getattr(value, "moba_MobaTrigger", None)
                setattr(value, "moba_MobaTrigger", self)

    @property
    def moba_MobaTrigger(self):
        return self.__moba_MobaTrigger

    @moba_MobaTrigger.setter
    def moba_MobaTrigger(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaTrigger__moba_MobaTrigger", None)
        self.__moba_MobaTrigger = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaTrigger199"):
                opp_val = getattr(old_value, "moba_MobaTrigger199", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaTrigger199", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaTrigger199"):
                opp_val = getattr(value, "moba_MobaTrigger199", None)
                setattr(value, "moba_MobaTrigger199", self)

class moba_MobaSettings(MobaApplicationFeature):

    def __init__(self, name: str, active: bool, moba_MobaSettings: "moba_MobaSettings" = None, moba_MobaSettings57: "moba_MobaSettings" = None, moba_MobaSettings60: set["moba_MobaSettingsFeature"] = None):
        self.name = name
        self.active = active
        self.moba_MobaSettings = moba_MobaSettings
        self.moba_MobaSettings57 = moba_MobaSettings57
        self.moba_MobaSettings60 = moba_MobaSettings60 if moba_MobaSettings60 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def active(self) -> bool:
        return self.__active

    @active.setter
    def active(self, active: bool):
        self.__active = active

    @property
    def moba_MobaSettings57(self):
        return self.__moba_MobaSettings57

    @moba_MobaSettings57.setter
    def moba_MobaSettings57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaSettings__moba_MobaSettings57", None)
        self.__moba_MobaSettings57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaSettings"):
                opp_val = getattr(old_value, "moba_MobaSettings", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaSettings", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaSettings"):
                opp_val = getattr(value, "moba_MobaSettings", None)
                setattr(value, "moba_MobaSettings", self)

    @property
    def moba_MobaSettings(self):
        return self.__moba_MobaSettings

    @moba_MobaSettings.setter
    def moba_MobaSettings(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaSettings__moba_MobaSettings", None)
        self.__moba_MobaSettings = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaSettings57"):
                opp_val = getattr(old_value, "moba_MobaSettings57", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaSettings57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaSettings57"):
                opp_val = getattr(value, "moba_MobaSettings57", None)
                setattr(value, "moba_MobaSettings57", self)

    @property
    def moba_MobaSettings60(self):
        return self.__moba_MobaSettings60

    @moba_MobaSettings60.setter
    def moba_MobaSettings60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaSettings__moba_MobaSettings60", None)
        self.__moba_MobaSettings60 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "moba_MobaSettingsFeature"):
                    opp_val = getattr(item, "moba_MobaSettingsFeature", None)
                    
                    if opp_val == self:
                        setattr(item, "moba_MobaSettingsFeature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "moba_MobaSettingsFeature"):
                    opp_val = getattr(item, "moba_MobaSettingsFeature", None)
                    
                    setattr(item, "moba_MobaSettingsFeature", self)
                    

class moba_MobaGenerator(MobaApplicationFeature):

    def __init__(self, name: str, active: bool, moba_MobaGenerator: set["moba_MobaGeneratorFeature"] = None, moba_MobaGenerator21: "moba_MobaGeneratorMixinFeature" = None):
        self.name = name
        self.active = active
        self.moba_MobaGenerator = moba_MobaGenerator if moba_MobaGenerator is not None else set()
        self.moba_MobaGenerator21 = moba_MobaGenerator21
        
    @property
    def active(self) -> bool:
        return self.__active

    @active.setter
    def active(self, active: bool):
        self.__active = active

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def moba_MobaGenerator21(self):
        return self.__moba_MobaGenerator21

    @moba_MobaGenerator21.setter
    def moba_MobaGenerator21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaGenerator__moba_MobaGenerator21", None)
        self.__moba_MobaGenerator21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaGeneratorMixinFeature"):
                opp_val = getattr(old_value, "moba_MobaGeneratorMixinFeature", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaGeneratorMixinFeature", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaGeneratorMixinFeature"):
                opp_val = getattr(value, "moba_MobaGeneratorMixinFeature", None)
                setattr(value, "moba_MobaGeneratorMixinFeature", self)

    @property
    def moba_MobaGenerator(self):
        return self.__moba_MobaGenerator

    @moba_MobaGenerator.setter
    def moba_MobaGenerator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaGenerator__moba_MobaGenerator", None)
        self.__moba_MobaGenerator = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "moba_MobaGeneratorFeature"):
                    opp_val = getattr(item, "moba_MobaGeneratorFeature", None)
                    
                    if opp_val == self:
                        setattr(item, "moba_MobaGeneratorFeature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "moba_MobaGeneratorFeature"):
                    opp_val = getattr(item, "moba_MobaGeneratorFeature", None)
                    
                    setattr(item, "moba_MobaGeneratorFeature", self)
                    

class moba_MobaGeneratorSlot(MobaApplicationFeature):

    def __init__(self, name: str, type: str, moba_MobaGeneratorSlot: "moba_MobaGeneratorSlot" = None, moba_MobaGeneratorSlot22: "moba_MobaGeneratorSlot" = None):
        self.name = name
        self.type = type
        self.moba_MobaGeneratorSlot = moba_MobaGeneratorSlot
        self.moba_MobaGeneratorSlot22 = moba_MobaGeneratorSlot22
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def moba_MobaGeneratorSlot(self):
        return self.__moba_MobaGeneratorSlot

    @moba_MobaGeneratorSlot.setter
    def moba_MobaGeneratorSlot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaGeneratorSlot__moba_MobaGeneratorSlot", None)
        self.__moba_MobaGeneratorSlot = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaGeneratorSlot22"):
                opp_val = getattr(old_value, "moba_MobaGeneratorSlot22", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaGeneratorSlot22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaGeneratorSlot22"):
                opp_val = getattr(value, "moba_MobaGeneratorSlot22", None)
                setattr(value, "moba_MobaGeneratorSlot22", self)

    @property
    def moba_MobaGeneratorSlot22(self):
        return self.__moba_MobaGeneratorSlot22

    @moba_MobaGeneratorSlot22.setter
    def moba_MobaGeneratorSlot22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaGeneratorSlot__moba_MobaGeneratorSlot22", None)
        self.__moba_MobaGeneratorSlot22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaGeneratorSlot"):
                opp_val = getattr(old_value, "moba_MobaGeneratorSlot", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaGeneratorSlot", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaGeneratorSlot"):
                opp_val = getattr(value, "moba_MobaGeneratorSlot", None)
                setattr(value, "moba_MobaGeneratorSlot", self)

class moba_MobaData(MobaApplicationFeature):

    pass
class moba_MobaDataType(MobaApplicationFeature, MobaConstraintable):

    def __init__(self, name: str, primitive: bool, string: bool, numeric: bool, decimal: bool, date: bool, time: bool, timestamp: bool, array: bool, dateFormatString: str, bool: bool, predefined: bool, moba_MobaDataType: "moba_MobaEnum" = None, moba_MobaDataType26: "moba_MobaConstant" = None, moba_MobaDataType30: "moba_MobaDataType" = None, moba_MobaDataType28: "moba_MobaDataType" = None, moba_MobaDataType62: "moba_MobaSettingsAttribute" = None, moba_MobaDataType120: "moba_MobaRESTAttribute" = None, moba_MobaDataType155: "moba_MobaEntityAttribute" = None, moba_MobaDataType168: "moba_MobaDtoAttribute" = None):
        self.name = name
        self.primitive = primitive
        self.string = string
        self.numeric = numeric
        self.decimal = decimal
        self.date = date
        self.time = time
        self.timestamp = timestamp
        self.array = array
        self.dateFormatString = dateFormatString
        self.bool = bool
        self.predefined = predefined
        self.moba_MobaDataType = moba_MobaDataType
        self.moba_MobaDataType26 = moba_MobaDataType26
        self.moba_MobaDataType30 = moba_MobaDataType30
        self.moba_MobaDataType28 = moba_MobaDataType28
        self.moba_MobaDataType62 = moba_MobaDataType62
        self.moba_MobaDataType120 = moba_MobaDataType120
        self.moba_MobaDataType155 = moba_MobaDataType155
        self.moba_MobaDataType168 = moba_MobaDataType168
        
    @property
    def primitive(self) -> bool:
        return self.__primitive

    @primitive.setter
    def primitive(self, primitive: bool):
        self.__primitive = primitive

    @property
    def numeric(self) -> bool:
        return self.__numeric

    @numeric.setter
    def numeric(self, numeric: bool):
        self.__numeric = numeric

    @property
    def predefined(self) -> bool:
        return self.__predefined

    @predefined.setter
    def predefined(self, predefined: bool):
        self.__predefined = predefined

    @property
    def date(self) -> bool:
        return self.__date

    @date.setter
    def date(self, date: bool):
        self.__date = date

    @property
    def time(self) -> bool:
        return self.__time

    @time.setter
    def time(self, time: bool):
        self.__time = time

    @property
    def dateFormatString(self) -> str:
        return self.__dateFormatString

    @dateFormatString.setter
    def dateFormatString(self, dateFormatString: str):
        self.__dateFormatString = dateFormatString

    @property
    def array(self) -> bool:
        return self.__array

    @array.setter
    def array(self, array: bool):
        self.__array = array

    @property
    def string(self) -> bool:
        return self.__string

    @string.setter
    def string(self, string: bool):
        self.__string = string

    @property
    def timestamp(self) -> bool:
        return self.__timestamp

    @timestamp.setter
    def timestamp(self, timestamp: bool):
        self.__timestamp = timestamp

    @property
    def bool(self) -> bool:
        return self.__bool

    @bool.setter
    def bool(self, bool: bool):
        self.__bool = bool

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def decimal(self) -> bool:
        return self.__decimal

    @decimal.setter
    def decimal(self, decimal: bool):
        self.__decimal = decimal

    @property
    def moba_MobaDataType168(self):
        return self.__moba_MobaDataType168

    @moba_MobaDataType168.setter
    def moba_MobaDataType168(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaDataType__moba_MobaDataType168", None)
        self.__moba_MobaDataType168 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaDtoAttribute"):
                opp_val = getattr(old_value, "moba_MobaDtoAttribute", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaDtoAttribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaDtoAttribute"):
                opp_val = getattr(value, "moba_MobaDtoAttribute", None)
                setattr(value, "moba_MobaDtoAttribute", self)

    @property
    def moba_MobaDataType120(self):
        return self.__moba_MobaDataType120

    @moba_MobaDataType120.setter
    def moba_MobaDataType120(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaDataType__moba_MobaDataType120", None)
        self.__moba_MobaDataType120 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaRESTAttribute"):
                opp_val = getattr(old_value, "moba_MobaRESTAttribute", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaRESTAttribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaRESTAttribute"):
                opp_val = getattr(value, "moba_MobaRESTAttribute", None)
                setattr(value, "moba_MobaRESTAttribute", self)

    @property
    def moba_MobaDataType62(self):
        return self.__moba_MobaDataType62

    @moba_MobaDataType62.setter
    def moba_MobaDataType62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaDataType__moba_MobaDataType62", None)
        self.__moba_MobaDataType62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaSettingsAttribute"):
                opp_val = getattr(old_value, "moba_MobaSettingsAttribute", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaSettingsAttribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaSettingsAttribute"):
                opp_val = getattr(value, "moba_MobaSettingsAttribute", None)
                setattr(value, "moba_MobaSettingsAttribute", self)

    @property
    def moba_MobaDataType155(self):
        return self.__moba_MobaDataType155

    @moba_MobaDataType155.setter
    def moba_MobaDataType155(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaDataType__moba_MobaDataType155", None)
        self.__moba_MobaDataType155 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaEntityAttribute154"):
                opp_val = getattr(old_value, "moba_MobaEntityAttribute154", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaEntityAttribute154", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaEntityAttribute154"):
                opp_val = getattr(value, "moba_MobaEntityAttribute154", None)
                setattr(value, "moba_MobaEntityAttribute154", self)

    @property
    def moba_MobaDataType26(self):
        return self.__moba_MobaDataType26

    @moba_MobaDataType26.setter
    def moba_MobaDataType26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaDataType__moba_MobaDataType26", None)
        self.__moba_MobaDataType26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaConstant27"):
                opp_val = getattr(old_value, "moba_MobaConstant27", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaConstant27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaConstant27"):
                opp_val = getattr(value, "moba_MobaConstant27", None)
                setattr(value, "moba_MobaConstant27", self)

    @property
    def moba_MobaDataType28(self):
        return self.__moba_MobaDataType28

    @moba_MobaDataType28.setter
    def moba_MobaDataType28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaDataType__moba_MobaDataType28", None)
        self.__moba_MobaDataType28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaDataType30"):
                opp_val = getattr(old_value, "moba_MobaDataType30", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaDataType30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaDataType30"):
                opp_val = getattr(value, "moba_MobaDataType30", None)
                setattr(value, "moba_MobaDataType30", self)

    @property
    def moba_MobaDataType(self):
        return self.__moba_MobaDataType

    @moba_MobaDataType.setter
    def moba_MobaDataType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaDataType__moba_MobaDataType", None)
        self.__moba_MobaDataType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaEnum"):
                opp_val = getattr(old_value, "moba_MobaEnum", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaEnum", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaEnum"):
                opp_val = getattr(value, "moba_MobaEnum", None)
                setattr(value, "moba_MobaEnum", self)

    @property
    def moba_MobaDataType30(self):
        return self.__moba_MobaDataType30

    @moba_MobaDataType30.setter
    def moba_MobaDataType30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaDataType__moba_MobaDataType30", None)
        self.__moba_MobaDataType30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaDataType28"):
                opp_val = getattr(old_value, "moba_MobaDataType28", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaDataType28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaDataType28"):
                opp_val = getattr(value, "moba_MobaDataType28", None)
                setattr(value, "moba_MobaDataType28", self)

class moba_MobaEnum(MobaApplicationFeature):

    pass
class moba_MobaTemplate(MobaApplicationFeature):

    def __init__(self, downloadTemplate: str, moba_MobaTemplate: "moba_MobaApplication" = None):
        self.downloadTemplate = downloadTemplate
        self.moba_MobaTemplate = moba_MobaTemplate
        
    @property
    def downloadTemplate(self) -> str:
        return self.__downloadTemplate

    @downloadTemplate.setter
    def downloadTemplate(self, downloadTemplate: str):
        self.__downloadTemplate = downloadTemplate

    @property
    def moba_MobaTemplate(self):
        return self.__moba_MobaTemplate

    @moba_MobaTemplate.setter
    def moba_MobaTemplate(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaTemplate__moba_MobaTemplate", None)
        self.__moba_MobaTemplate = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaApplication10"):
                opp_val = getattr(old_value, "moba_MobaApplication10", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaApplication10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaApplication10"):
                opp_val = getattr(value, "moba_MobaApplication10", None)
                setattr(value, "moba_MobaApplication10", self)

class moba_MobaCache(MobaApplicationFeature):

    def __init__(self, name: str, cacheTypeString: str, cacheStrategyString: str, cacheIntervalInt: int, moba_MobaCache: "moba_MobaApplication" = None, moba_MobaCache34: "moba_MobaConstant" = None, moba_MobaCache37: "moba_MobaConstant" = None, moba_MobaCache40: "moba_MobaConstant" = None, moba_MobaCache43: "moba_MobaPersistenceType" = None, moba_MobaCache72: "moba_MobaEntity" = None, moba_MobaCache92: "moba_MobaQueue" = None):
        self.name = name
        self.cacheTypeString = cacheTypeString
        self.cacheStrategyString = cacheStrategyString
        self.cacheIntervalInt = cacheIntervalInt
        self.moba_MobaCache = moba_MobaCache
        self.moba_MobaCache34 = moba_MobaCache34
        self.moba_MobaCache37 = moba_MobaCache37
        self.moba_MobaCache40 = moba_MobaCache40
        self.moba_MobaCache43 = moba_MobaCache43
        self.moba_MobaCache72 = moba_MobaCache72
        self.moba_MobaCache92 = moba_MobaCache92
        
    @property
    def cacheIntervalInt(self) -> int:
        return self.__cacheIntervalInt

    @cacheIntervalInt.setter
    def cacheIntervalInt(self, cacheIntervalInt: int):
        self.__cacheIntervalInt = cacheIntervalInt

    @property
    def cacheTypeString(self) -> str:
        return self.__cacheTypeString

    @cacheTypeString.setter
    def cacheTypeString(self, cacheTypeString: str):
        self.__cacheTypeString = cacheTypeString

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def cacheStrategyString(self) -> str:
        return self.__cacheStrategyString

    @cacheStrategyString.setter
    def cacheStrategyString(self, cacheStrategyString: str):
        self.__cacheStrategyString = cacheStrategyString

    @property
    def moba_MobaCache37(self):
        return self.__moba_MobaCache37

    @moba_MobaCache37.setter
    def moba_MobaCache37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaCache__moba_MobaCache37", None)
        self.__moba_MobaCache37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaConstant38"):
                opp_val = getattr(old_value, "moba_MobaConstant38", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaConstant38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaConstant38"):
                opp_val = getattr(value, "moba_MobaConstant38", None)
                setattr(value, "moba_MobaConstant38", self)

    @property
    def moba_MobaCache34(self):
        return self.__moba_MobaCache34

    @moba_MobaCache34.setter
    def moba_MobaCache34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaCache__moba_MobaCache34", None)
        self.__moba_MobaCache34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaConstant35"):
                opp_val = getattr(old_value, "moba_MobaConstant35", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaConstant35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaConstant35"):
                opp_val = getattr(value, "moba_MobaConstant35", None)
                setattr(value, "moba_MobaConstant35", self)

    @property
    def moba_MobaCache43(self):
        return self.__moba_MobaCache43

    @moba_MobaCache43.setter
    def moba_MobaCache43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaCache__moba_MobaCache43", None)
        self.__moba_MobaCache43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaPersistenceType"):
                opp_val = getattr(old_value, "moba_MobaPersistenceType", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaPersistenceType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaPersistenceType"):
                opp_val = getattr(value, "moba_MobaPersistenceType", None)
                setattr(value, "moba_MobaPersistenceType", self)

    @property
    def moba_MobaCache40(self):
        return self.__moba_MobaCache40

    @moba_MobaCache40.setter
    def moba_MobaCache40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaCache__moba_MobaCache40", None)
        self.__moba_MobaCache40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaConstant41"):
                opp_val = getattr(old_value, "moba_MobaConstant41", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaConstant41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaConstant41"):
                opp_val = getattr(value, "moba_MobaConstant41", None)
                setattr(value, "moba_MobaConstant41", self)

    @property
    def moba_MobaCache(self):
        return self.__moba_MobaCache

    @moba_MobaCache.setter
    def moba_MobaCache(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaCache__moba_MobaCache", None)
        self.__moba_MobaCache = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaApplication6"):
                opp_val = getattr(old_value, "moba_MobaApplication6", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaApplication6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaApplication6"):
                opp_val = getattr(value, "moba_MobaApplication6", None)
                setattr(value, "moba_MobaApplication6", self)

    @property
    def moba_MobaCache92(self):
        return self.__moba_MobaCache92

    @moba_MobaCache92.setter
    def moba_MobaCache92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaCache__moba_MobaCache92", None)
        self.__moba_MobaCache92 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaQueue91"):
                opp_val = getattr(old_value, "moba_MobaQueue91", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaQueue91", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaQueue91"):
                opp_val = getattr(value, "moba_MobaQueue91", None)
                setattr(value, "moba_MobaQueue91", self)

    @property
    def moba_MobaCache72(self):
        return self.__moba_MobaCache72

    @moba_MobaCache72.setter
    def moba_MobaCache72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaCache__moba_MobaCache72", None)
        self.__moba_MobaCache72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaEntity71"):
                opp_val = getattr(old_value, "moba_MobaEntity71", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaEntity71", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaEntity71"):
                opp_val = getattr(value, "moba_MobaEntity71", None)
                setattr(value, "moba_MobaEntity71", self)

class moba_MobaTransportSerializationType(MobaApplicationFeature):

    def __init__(self, name: str, moba_MobaTransportSerializationType: "moba_MobaDto" = None, moba_MobaTransportSerializationType116: "moba_MobaRESTPayloadDefinition" = None):
        self.name = name
        self.moba_MobaTransportSerializationType = moba_MobaTransportSerializationType
        self.moba_MobaTransportSerializationType116 = moba_MobaTransportSerializationType116
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def moba_MobaTransportSerializationType(self):
        return self.__moba_MobaTransportSerializationType

    @moba_MobaTransportSerializationType.setter
    def moba_MobaTransportSerializationType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaTransportSerializationType__moba_MobaTransportSerializationType", None)
        self.__moba_MobaTransportSerializationType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaDto87"):
                opp_val = getattr(old_value, "moba_MobaDto87", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaDto87", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaDto87"):
                opp_val = getattr(value, "moba_MobaDto87", None)
                setattr(value, "moba_MobaDto87", self)

    @property
    def moba_MobaTransportSerializationType116(self):
        return self.__moba_MobaTransportSerializationType116

    @moba_MobaTransportSerializationType116.setter
    def moba_MobaTransportSerializationType116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaTransportSerializationType__moba_MobaTransportSerializationType116", None)
        self.__moba_MobaTransportSerializationType116 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaRESTPayloadDefinition115"):
                opp_val = getattr(old_value, "moba_MobaRESTPayloadDefinition115", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaRESTPayloadDefinition115", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaRESTPayloadDefinition115"):
                opp_val = getattr(value, "moba_MobaRESTPayloadDefinition115", None)
                setattr(value, "moba_MobaRESTPayloadDefinition115", self)

class moba_MobaAuthorization(MobaApplicationFeature):

    def __init__(self, name: str, moba_MobaAuthorization: "moba_MobaServer" = None, moba_MobaAuthorization110: "moba_MobaREST" = None):
        self.name = name
        self.moba_MobaAuthorization = moba_MobaAuthorization
        self.moba_MobaAuthorization110 = moba_MobaAuthorization110
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def moba_MobaAuthorization(self):
        return self.__moba_MobaAuthorization

    @moba_MobaAuthorization.setter
    def moba_MobaAuthorization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaAuthorization__moba_MobaAuthorization", None)
        self.__moba_MobaAuthorization = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaServer18"):
                opp_val = getattr(old_value, "moba_MobaServer18", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaServer18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaServer18"):
                opp_val = getattr(value, "moba_MobaServer18", None)
                setattr(value, "moba_MobaServer18", self)

    @property
    def moba_MobaAuthorization110(self):
        return self.__moba_MobaAuthorization110

    @moba_MobaAuthorization110.setter
    def moba_MobaAuthorization110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaAuthorization__moba_MobaAuthorization110", None)
        self.__moba_MobaAuthorization110 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaREST109"):
                opp_val = getattr(old_value, "moba_MobaREST109", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaREST109", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaREST109"):
                opp_val = getattr(value, "moba_MobaREST109", None)
                setattr(value, "moba_MobaREST109", self)

class moba_MobaREST(MobaApplicationFeature):

    def __init__(self, path: str, name: str, url: str, bigData: bool, moba_MobaREST: "moba_MobaServer" = None, moba_MobaREST107: set["moba_MobaRESTHeader"] = None, moba_MobaREST109: "moba_MobaAuthorization" = None, moba_MobaREST96: "moba_MobaRESTPayloadDefinition" = None, moba_MobaREST98: "moba_MobaRESTPayloadDefinition" = None, moba_MobaREST101: "moba_MobaRESTPayloadDefinition" = None, moba_MobaREST104: "moba_MobaRESTPayloadDefinition" = None, moba_MobaREST147: "moba_MobaRESTWorkflow" = None, moba_MobaREST180: "moba_MobaQueueReference" = None):
        self.path = path
        self.name = name
        self.url = url
        self.bigData = bigData
        self.moba_MobaREST = moba_MobaREST
        self.moba_MobaREST107 = moba_MobaREST107 if moba_MobaREST107 is not None else set()
        self.moba_MobaREST109 = moba_MobaREST109
        self.moba_MobaREST96 = moba_MobaREST96
        self.moba_MobaREST98 = moba_MobaREST98
        self.moba_MobaREST101 = moba_MobaREST101
        self.moba_MobaREST104 = moba_MobaREST104
        self.moba_MobaREST147 = moba_MobaREST147
        self.moba_MobaREST180 = moba_MobaREST180
        
    @property
    def path(self) -> str:
        return self.__path

    @path.setter
    def path(self, path: str):
        self.__path = path

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def url(self) -> str:
        return self.__url

    @url.setter
    def url(self, url: str):
        self.__url = url

    @property
    def bigData(self) -> bool:
        return self.__bigData

    @bigData.setter
    def bigData(self, bigData: bool):
        self.__bigData = bigData

    @property
    def moba_MobaREST180(self):
        return self.__moba_MobaREST180

    @moba_MobaREST180.setter
    def moba_MobaREST180(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaREST__moba_MobaREST180", None)
        self.__moba_MobaREST180 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaQueueReference"):
                opp_val = getattr(old_value, "moba_MobaQueueReference", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaQueueReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaQueueReference"):
                opp_val = getattr(value, "moba_MobaQueueReference", None)
                setattr(value, "moba_MobaQueueReference", self)

    @property
    def moba_MobaREST109(self):
        return self.__moba_MobaREST109

    @moba_MobaREST109.setter
    def moba_MobaREST109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaREST__moba_MobaREST109", None)
        self.__moba_MobaREST109 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaAuthorization110"):
                opp_val = getattr(old_value, "moba_MobaAuthorization110", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaAuthorization110", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaAuthorization110"):
                opp_val = getattr(value, "moba_MobaAuthorization110", None)
                setattr(value, "moba_MobaAuthorization110", self)

    @property
    def moba_MobaREST104(self):
        return self.__moba_MobaREST104

    @moba_MobaREST104.setter
    def moba_MobaREST104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaREST__moba_MobaREST104", None)
        self.__moba_MobaREST104 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaRESTPayloadDefinition105"):
                opp_val = getattr(old_value, "moba_MobaRESTPayloadDefinition105", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaRESTPayloadDefinition105", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaRESTPayloadDefinition105"):
                opp_val = getattr(value, "moba_MobaRESTPayloadDefinition105", None)
                setattr(value, "moba_MobaRESTPayloadDefinition105", self)

    @property
    def moba_MobaREST(self):
        return self.__moba_MobaREST

    @moba_MobaREST.setter
    def moba_MobaREST(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaREST__moba_MobaREST", None)
        self.__moba_MobaREST = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaServer16"):
                opp_val = getattr(old_value, "moba_MobaServer16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaServer16"):
                opp_val = getattr(value, "moba_MobaServer16", None)
                if opp_val is None:
                    setattr(value, "moba_MobaServer16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def moba_MobaREST101(self):
        return self.__moba_MobaREST101

    @moba_MobaREST101.setter
    def moba_MobaREST101(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaREST__moba_MobaREST101", None)
        self.__moba_MobaREST101 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaRESTPayloadDefinition102"):
                opp_val = getattr(old_value, "moba_MobaRESTPayloadDefinition102", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaRESTPayloadDefinition102", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaRESTPayloadDefinition102"):
                opp_val = getattr(value, "moba_MobaRESTPayloadDefinition102", None)
                setattr(value, "moba_MobaRESTPayloadDefinition102", self)

    @property
    def moba_MobaREST147(self):
        return self.__moba_MobaREST147

    @moba_MobaREST147.setter
    def moba_MobaREST147(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaREST__moba_MobaREST147", None)
        self.__moba_MobaREST147 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaRESTWorkflow"):
                opp_val = getattr(old_value, "moba_MobaRESTWorkflow", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaRESTWorkflow"):
                opp_val = getattr(value, "moba_MobaRESTWorkflow", None)
                if opp_val is None:
                    setattr(value, "moba_MobaRESTWorkflow", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def moba_MobaREST107(self):
        return self.__moba_MobaREST107

    @moba_MobaREST107.setter
    def moba_MobaREST107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaREST__moba_MobaREST107", None)
        self.__moba_MobaREST107 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "moba_MobaRESTHeader"):
                    opp_val = getattr(item, "moba_MobaRESTHeader", None)
                    
                    if opp_val == self:
                        setattr(item, "moba_MobaRESTHeader", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "moba_MobaRESTHeader"):
                    opp_val = getattr(item, "moba_MobaRESTHeader", None)
                    
                    setattr(item, "moba_MobaRESTHeader", self)
                    

    @property
    def moba_MobaREST98(self):
        return self.__moba_MobaREST98

    @moba_MobaREST98.setter
    def moba_MobaREST98(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaREST__moba_MobaREST98", None)
        self.__moba_MobaREST98 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaRESTPayloadDefinition99"):
                opp_val = getattr(old_value, "moba_MobaRESTPayloadDefinition99", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaRESTPayloadDefinition99", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaRESTPayloadDefinition99"):
                opp_val = getattr(value, "moba_MobaRESTPayloadDefinition99", None)
                setattr(value, "moba_MobaRESTPayloadDefinition99", self)

    @property
    def moba_MobaREST96(self):
        return self.__moba_MobaREST96

    @moba_MobaREST96.setter
    def moba_MobaREST96(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaREST__moba_MobaREST96", None)
        self.__moba_MobaREST96 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaRESTPayloadDefinition"):
                opp_val = getattr(old_value, "moba_MobaRESTPayloadDefinition", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaRESTPayloadDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaRESTPayloadDefinition"):
                opp_val = getattr(value, "moba_MobaRESTPayloadDefinition", None)
                setattr(value, "moba_MobaRESTPayloadDefinition", self)

class moba_MobaConstant(MobaApplicationFeature):

    def __init__(self, name: str, moba_MobaConstant: "moba_MobaServer" = None, moba_MobaConstant32: "moba_MobaConstantValue" = None, moba_MobaConstant35: "moba_MobaCache" = None, moba_MobaConstant38: "moba_MobaCache" = None, moba_MobaConstant41: "moba_MobaCache" = None, moba_MobaConstant27: "moba_MobaDataType" = None, moba_MobaConstant46: "moba_MobaConstantValue" = None, moba_MobaConstant53: "moba_MobaProperty" = None, moba_MobaConstant56: "moba_MobaProperty" = None, moba_MobaConstant65: "moba_MobaSettingsAttribute" = None, moba_MobaConstant118: "moba_MobaRESTAbstractAttribute" = None, moba_MobaConstant134: "moba_MobaRESTHeader" = None, moba_MobaConstant137: "moba_MobaRESTHeader" = None, moba_MobaConstant123: "moba_MobaRESTAttribute" = None, moba_MobaConstant126: "moba_MobaRESTAttribute" = None, moba_MobaConstant129: "moba_MobaRESTAttribute" = None, moba_MobaConstant158: "moba_MobaEntityAttribute" = None, moba_MobaConstant171: "moba_MobaDtoAttribute" = None, moba_MobaConstant183: "moba_MobaRegexpConstraint" = None, moba_MobaConstant185: "moba_MobaMinConstraint" = None, moba_MobaConstant187: "moba_MobaMaxConstraint" = None, moba_MobaConstant189: "moba_MobaMinLengthConstraint" = None, moba_MobaConstant191: "moba_MobaMaxLengthConstraint" = None, moba_MobaConstant193: "moba_MobaDigitsConstraint" = None, moba_MobaConstant196: "moba_MobaDigitsConstraint" = None, moba_MobaConstant202: "moba_MobaFriend" = None):
        self.name = name
        self.moba_MobaConstant = moba_MobaConstant
        self.moba_MobaConstant32 = moba_MobaConstant32
        self.moba_MobaConstant35 = moba_MobaConstant35
        self.moba_MobaConstant38 = moba_MobaConstant38
        self.moba_MobaConstant41 = moba_MobaConstant41
        self.moba_MobaConstant27 = moba_MobaConstant27
        self.moba_MobaConstant46 = moba_MobaConstant46
        self.moba_MobaConstant53 = moba_MobaConstant53
        self.moba_MobaConstant56 = moba_MobaConstant56
        self.moba_MobaConstant65 = moba_MobaConstant65
        self.moba_MobaConstant118 = moba_MobaConstant118
        self.moba_MobaConstant134 = moba_MobaConstant134
        self.moba_MobaConstant137 = moba_MobaConstant137
        self.moba_MobaConstant123 = moba_MobaConstant123
        self.moba_MobaConstant126 = moba_MobaConstant126
        self.moba_MobaConstant129 = moba_MobaConstant129
        self.moba_MobaConstant158 = moba_MobaConstant158
        self.moba_MobaConstant171 = moba_MobaConstant171
        self.moba_MobaConstant183 = moba_MobaConstant183
        self.moba_MobaConstant185 = moba_MobaConstant185
        self.moba_MobaConstant187 = moba_MobaConstant187
        self.moba_MobaConstant189 = moba_MobaConstant189
        self.moba_MobaConstant191 = moba_MobaConstant191
        self.moba_MobaConstant193 = moba_MobaConstant193
        self.moba_MobaConstant196 = moba_MobaConstant196
        self.moba_MobaConstant202 = moba_MobaConstant202
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def moba_MobaConstant56(self):
        return self.__moba_MobaConstant56

    @moba_MobaConstant56.setter
    def moba_MobaConstant56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaConstant__moba_MobaConstant56", None)
        self.__moba_MobaConstant56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaProperty55"):
                opp_val = getattr(old_value, "moba_MobaProperty55", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaProperty55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaProperty55"):
                opp_val = getattr(value, "moba_MobaProperty55", None)
                setattr(value, "moba_MobaProperty55", self)

    @property
    def moba_MobaConstant202(self):
        return self.__moba_MobaConstant202

    @moba_MobaConstant202.setter
    def moba_MobaConstant202(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaConstant__moba_MobaConstant202", None)
        self.__moba_MobaConstant202 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaFriend"):
                opp_val = getattr(old_value, "moba_MobaFriend", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaFriend", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaFriend"):
                opp_val = getattr(value, "moba_MobaFriend", None)
                setattr(value, "moba_MobaFriend", self)

    @property
    def moba_MobaConstant158(self):
        return self.__moba_MobaConstant158

    @moba_MobaConstant158.setter
    def moba_MobaConstant158(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaConstant__moba_MobaConstant158", None)
        self.__moba_MobaConstant158 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaEntityAttribute157"):
                opp_val = getattr(old_value, "moba_MobaEntityAttribute157", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaEntityAttribute157", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaEntityAttribute157"):
                opp_val = getattr(value, "moba_MobaEntityAttribute157", None)
                setattr(value, "moba_MobaEntityAttribute157", self)

    @property
    def moba_MobaConstant(self):
        return self.__moba_MobaConstant

    @moba_MobaConstant.setter
    def moba_MobaConstant(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaConstant__moba_MobaConstant", None)
        self.__moba_MobaConstant = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaServer"):
                opp_val = getattr(old_value, "moba_MobaServer", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaServer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaServer"):
                opp_val = getattr(value, "moba_MobaServer", None)
                setattr(value, "moba_MobaServer", self)

    @property
    def moba_MobaConstant35(self):
        return self.__moba_MobaConstant35

    @moba_MobaConstant35.setter
    def moba_MobaConstant35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaConstant__moba_MobaConstant35", None)
        self.__moba_MobaConstant35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaCache34"):
                opp_val = getattr(old_value, "moba_MobaCache34", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaCache34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaCache34"):
                opp_val = getattr(value, "moba_MobaCache34", None)
                setattr(value, "moba_MobaCache34", self)

    @property
    def moba_MobaConstant129(self):
        return self.__moba_MobaConstant129

    @moba_MobaConstant129.setter
    def moba_MobaConstant129(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaConstant__moba_MobaConstant129", None)
        self.__moba_MobaConstant129 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaRESTAttribute128"):
                opp_val = getattr(old_value, "moba_MobaRESTAttribute128", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaRESTAttribute128", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaRESTAttribute128"):
                opp_val = getattr(value, "moba_MobaRESTAttribute128", None)
                setattr(value, "moba_MobaRESTAttribute128", self)

    @property
    def moba_MobaConstant41(self):
        return self.__moba_MobaConstant41

    @moba_MobaConstant41.setter
    def moba_MobaConstant41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaConstant__moba_MobaConstant41", None)
        self.__moba_MobaConstant41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaCache40"):
                opp_val = getattr(old_value, "moba_MobaCache40", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaCache40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaCache40"):
                opp_val = getattr(value, "moba_MobaCache40", None)
                setattr(value, "moba_MobaCache40", self)

    @property
    def moba_MobaConstant126(self):
        return self.__moba_MobaConstant126

    @moba_MobaConstant126.setter
    def moba_MobaConstant126(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaConstant__moba_MobaConstant126", None)
        self.__moba_MobaConstant126 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaRESTAttribute125"):
                opp_val = getattr(old_value, "moba_MobaRESTAttribute125", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaRESTAttribute125", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaRESTAttribute125"):
                opp_val = getattr(value, "moba_MobaRESTAttribute125", None)
                setattr(value, "moba_MobaRESTAttribute125", self)

    @property
    def moba_MobaConstant38(self):
        return self.__moba_MobaConstant38

    @moba_MobaConstant38.setter
    def moba_MobaConstant38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaConstant__moba_MobaConstant38", None)
        self.__moba_MobaConstant38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaCache37"):
                opp_val = getattr(old_value, "moba_MobaCache37", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaCache37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaCache37"):
                opp_val = getattr(value, "moba_MobaCache37", None)
                setattr(value, "moba_MobaCache37", self)

    @property
    def moba_MobaConstant191(self):
        return self.__moba_MobaConstant191

    @moba_MobaConstant191.setter
    def moba_MobaConstant191(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaConstant__moba_MobaConstant191", None)
        self.__moba_MobaConstant191 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaMaxLengthConstraint"):
                opp_val = getattr(old_value, "moba_MobaMaxLengthConstraint", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaMaxLengthConstraint", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaMaxLengthConstraint"):
                opp_val = getattr(value, "moba_MobaMaxLengthConstraint", None)
                setattr(value, "moba_MobaMaxLengthConstraint", self)

    @property
    def moba_MobaConstant134(self):
        return self.__moba_MobaConstant134

    @moba_MobaConstant134.setter
    def moba_MobaConstant134(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaConstant__moba_MobaConstant134", None)
        self.__moba_MobaConstant134 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaRESTHeader133"):
                opp_val = getattr(old_value, "moba_MobaRESTHeader133", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaRESTHeader133", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaRESTHeader133"):
                opp_val = getattr(value, "moba_MobaRESTHeader133", None)
                setattr(value, "moba_MobaRESTHeader133", self)

    @property
    def moba_MobaConstant65(self):
        return self.__moba_MobaConstant65

    @moba_MobaConstant65.setter
    def moba_MobaConstant65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaConstant__moba_MobaConstant65", None)
        self.__moba_MobaConstant65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaSettingsAttribute64"):
                opp_val = getattr(old_value, "moba_MobaSettingsAttribute64", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaSettingsAttribute64", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaSettingsAttribute64"):
                opp_val = getattr(value, "moba_MobaSettingsAttribute64", None)
                setattr(value, "moba_MobaSettingsAttribute64", self)

    @property
    def moba_MobaConstant137(self):
        return self.__moba_MobaConstant137

    @moba_MobaConstant137.setter
    def moba_MobaConstant137(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaConstant__moba_MobaConstant137", None)
        self.__moba_MobaConstant137 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaRESTHeader136"):
                opp_val = getattr(old_value, "moba_MobaRESTHeader136", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaRESTHeader136", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaRESTHeader136"):
                opp_val = getattr(value, "moba_MobaRESTHeader136", None)
                setattr(value, "moba_MobaRESTHeader136", self)

    @property
    def moba_MobaConstant189(self):
        return self.__moba_MobaConstant189

    @moba_MobaConstant189.setter
    def moba_MobaConstant189(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaConstant__moba_MobaConstant189", None)
        self.__moba_MobaConstant189 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaMinLengthConstraint"):
                opp_val = getattr(old_value, "moba_MobaMinLengthConstraint", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaMinLengthConstraint", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaMinLengthConstraint"):
                opp_val = getattr(value, "moba_MobaMinLengthConstraint", None)
                setattr(value, "moba_MobaMinLengthConstraint", self)

    @property
    def moba_MobaConstant183(self):
        return self.__moba_MobaConstant183

    @moba_MobaConstant183.setter
    def moba_MobaConstant183(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaConstant__moba_MobaConstant183", None)
        self.__moba_MobaConstant183 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaRegexpConstraint"):
                opp_val = getattr(old_value, "moba_MobaRegexpConstraint", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaRegexpConstraint", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaRegexpConstraint"):
                opp_val = getattr(value, "moba_MobaRegexpConstraint", None)
                setattr(value, "moba_MobaRegexpConstraint", self)

    @property
    def moba_MobaConstant46(self):
        return self.__moba_MobaConstant46

    @moba_MobaConstant46.setter
    def moba_MobaConstant46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaConstant__moba_MobaConstant46", None)
        self.__moba_MobaConstant46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaConstantValue45"):
                opp_val = getattr(old_value, "moba_MobaConstantValue45", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaConstantValue45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaConstantValue45"):
                opp_val = getattr(value, "moba_MobaConstantValue45", None)
                setattr(value, "moba_MobaConstantValue45", self)

    @property
    def moba_MobaConstant32(self):
        return self.__moba_MobaConstant32

    @moba_MobaConstant32.setter
    def moba_MobaConstant32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaConstant__moba_MobaConstant32", None)
        self.__moba_MobaConstant32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaConstantValue"):
                opp_val = getattr(old_value, "moba_MobaConstantValue", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaConstantValue", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaConstantValue"):
                opp_val = getattr(value, "moba_MobaConstantValue", None)
                setattr(value, "moba_MobaConstantValue", self)

    @property
    def moba_MobaConstant27(self):
        return self.__moba_MobaConstant27

    @moba_MobaConstant27.setter
    def moba_MobaConstant27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaConstant__moba_MobaConstant27", None)
        self.__moba_MobaConstant27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaDataType26"):
                opp_val = getattr(old_value, "moba_MobaDataType26", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaDataType26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaDataType26"):
                opp_val = getattr(value, "moba_MobaDataType26", None)
                setattr(value, "moba_MobaDataType26", self)

    @property
    def moba_MobaConstant171(self):
        return self.__moba_MobaConstant171

    @moba_MobaConstant171.setter
    def moba_MobaConstant171(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaConstant__moba_MobaConstant171", None)
        self.__moba_MobaConstant171 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaDtoAttribute170"):
                opp_val = getattr(old_value, "moba_MobaDtoAttribute170", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaDtoAttribute170", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaDtoAttribute170"):
                opp_val = getattr(value, "moba_MobaDtoAttribute170", None)
                setattr(value, "moba_MobaDtoAttribute170", self)

    @property
    def moba_MobaConstant118(self):
        return self.__moba_MobaConstant118

    @moba_MobaConstant118.setter
    def moba_MobaConstant118(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaConstant__moba_MobaConstant118", None)
        self.__moba_MobaConstant118 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaRESTAbstractAttribute"):
                opp_val = getattr(old_value, "moba_MobaRESTAbstractAttribute", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaRESTAbstractAttribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaRESTAbstractAttribute"):
                opp_val = getattr(value, "moba_MobaRESTAbstractAttribute", None)
                setattr(value, "moba_MobaRESTAbstractAttribute", self)

    @property
    def moba_MobaConstant187(self):
        return self.__moba_MobaConstant187

    @moba_MobaConstant187.setter
    def moba_MobaConstant187(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaConstant__moba_MobaConstant187", None)
        self.__moba_MobaConstant187 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaMaxConstraint"):
                opp_val = getattr(old_value, "moba_MobaMaxConstraint", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaMaxConstraint", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaMaxConstraint"):
                opp_val = getattr(value, "moba_MobaMaxConstraint", None)
                setattr(value, "moba_MobaMaxConstraint", self)

    @property
    def moba_MobaConstant185(self):
        return self.__moba_MobaConstant185

    @moba_MobaConstant185.setter
    def moba_MobaConstant185(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaConstant__moba_MobaConstant185", None)
        self.__moba_MobaConstant185 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaMinConstraint"):
                opp_val = getattr(old_value, "moba_MobaMinConstraint", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaMinConstraint", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaMinConstraint"):
                opp_val = getattr(value, "moba_MobaMinConstraint", None)
                setattr(value, "moba_MobaMinConstraint", self)

    @property
    def moba_MobaConstant193(self):
        return self.__moba_MobaConstant193

    @moba_MobaConstant193.setter
    def moba_MobaConstant193(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaConstant__moba_MobaConstant193", None)
        self.__moba_MobaConstant193 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaDigitsConstraint"):
                opp_val = getattr(old_value, "moba_MobaDigitsConstraint", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaDigitsConstraint", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaDigitsConstraint"):
                opp_val = getattr(value, "moba_MobaDigitsConstraint", None)
                setattr(value, "moba_MobaDigitsConstraint", self)

    @property
    def moba_MobaConstant53(self):
        return self.__moba_MobaConstant53

    @moba_MobaConstant53.setter
    def moba_MobaConstant53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaConstant__moba_MobaConstant53", None)
        self.__moba_MobaConstant53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaProperty52"):
                opp_val = getattr(old_value, "moba_MobaProperty52", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaProperty52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaProperty52"):
                opp_val = getattr(value, "moba_MobaProperty52", None)
                setattr(value, "moba_MobaProperty52", self)

    @property
    def moba_MobaConstant123(self):
        return self.__moba_MobaConstant123

    @moba_MobaConstant123.setter
    def moba_MobaConstant123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaConstant__moba_MobaConstant123", None)
        self.__moba_MobaConstant123 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaRESTAttribute122"):
                opp_val = getattr(old_value, "moba_MobaRESTAttribute122", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaRESTAttribute122", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaRESTAttribute122"):
                opp_val = getattr(value, "moba_MobaRESTAttribute122", None)
                setattr(value, "moba_MobaRESTAttribute122", self)

    @property
    def moba_MobaConstant196(self):
        return self.__moba_MobaConstant196

    @moba_MobaConstant196.setter
    def moba_MobaConstant196(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaConstant__moba_MobaConstant196", None)
        self.__moba_MobaConstant196 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaDigitsConstraint195"):
                opp_val = getattr(old_value, "moba_MobaDigitsConstraint195", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaDigitsConstraint195", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaDigitsConstraint195"):
                opp_val = getattr(value, "moba_MobaDigitsConstraint195", None)
                setattr(value, "moba_MobaDigitsConstraint195", self)

class moba_MobaServer(MobaApplicationFeature):

    def __init__(self, name: str, urlString: str, moba_MobaServer: "moba_MobaConstant" = None, moba_MobaServer14: "moba_MobaServer" = None, moba_MobaServer12: "moba_MobaServer" = None, moba_MobaServer16: set["moba_MobaREST"] = None, moba_MobaServer18: "moba_MobaAuthorization" = None):
        self.name = name
        self.urlString = urlString
        self.moba_MobaServer = moba_MobaServer
        self.moba_MobaServer14 = moba_MobaServer14
        self.moba_MobaServer12 = moba_MobaServer12
        self.moba_MobaServer16 = moba_MobaServer16 if moba_MobaServer16 is not None else set()
        self.moba_MobaServer18 = moba_MobaServer18
        
    @property
    def urlString(self) -> str:
        return self.__urlString

    @urlString.setter
    def urlString(self, urlString: str):
        self.__urlString = urlString

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def moba_MobaServer(self):
        return self.__moba_MobaServer

    @moba_MobaServer.setter
    def moba_MobaServer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaServer__moba_MobaServer", None)
        self.__moba_MobaServer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaConstant"):
                opp_val = getattr(old_value, "moba_MobaConstant", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaConstant", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaConstant"):
                opp_val = getattr(value, "moba_MobaConstant", None)
                setattr(value, "moba_MobaConstant", self)

    @property
    def moba_MobaServer14(self):
        return self.__moba_MobaServer14

    @moba_MobaServer14.setter
    def moba_MobaServer14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaServer__moba_MobaServer14", None)
        self.__moba_MobaServer14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaServer12"):
                opp_val = getattr(old_value, "moba_MobaServer12", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaServer12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaServer12"):
                opp_val = getattr(value, "moba_MobaServer12", None)
                setattr(value, "moba_MobaServer12", self)

    @property
    def moba_MobaServer12(self):
        return self.__moba_MobaServer12

    @moba_MobaServer12.setter
    def moba_MobaServer12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaServer__moba_MobaServer12", None)
        self.__moba_MobaServer12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaServer14"):
                opp_val = getattr(old_value, "moba_MobaServer14", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaServer14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaServer14"):
                opp_val = getattr(value, "moba_MobaServer14", None)
                setattr(value, "moba_MobaServer14", self)

    @property
    def moba_MobaServer18(self):
        return self.__moba_MobaServer18

    @moba_MobaServer18.setter
    def moba_MobaServer18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaServer__moba_MobaServer18", None)
        self.__moba_MobaServer18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaAuthorization"):
                opp_val = getattr(old_value, "moba_MobaAuthorization", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaAuthorization", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaAuthorization"):
                opp_val = getattr(value, "moba_MobaAuthorization", None)
                setattr(value, "moba_MobaAuthorization", self)

    @property
    def moba_MobaServer16(self):
        return self.__moba_MobaServer16

    @moba_MobaServer16.setter
    def moba_MobaServer16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaServer__moba_MobaServer16", None)
        self.__moba_MobaServer16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "moba_MobaREST"):
                    opp_val = getattr(item, "moba_MobaREST", None)
                    
                    if opp_val == self:
                        setattr(item, "moba_MobaREST", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "moba_MobaREST"):
                    opp_val = getattr(item, "moba_MobaREST", None)
                    
                    setattr(item, "moba_MobaREST", self)
                    

class MobaFriendsAble:

    pass
class moba_MobaFeature(MobaFriendsAble):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class moba_MobaApplicationFeature(MobaFriendsAble):

    pass
class moba_MobaModel(MobaFriendsAble):

    def __init__(self, copyright: str, moba_MobaModel: set["moba_MobaModelFeature"] = None):
        self.copyright = copyright
        self.moba_MobaModel = moba_MobaModel if moba_MobaModel is not None else set()
        
    @property
    def copyright(self) -> str:
        return self.__copyright

    @copyright.setter
    def copyright(self, copyright: str):
        self.__copyright = copyright

    @property
    def moba_MobaModel(self):
        return self.__moba_MobaModel

    @moba_MobaModel.setter
    def moba_MobaModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaModel__moba_MobaModel", None)
        self.__moba_MobaModel = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "moba_MobaModelFeature"):
                    opp_val = getattr(item, "moba_MobaModelFeature", None)
                    
                    if opp_val == self:
                        setattr(item, "moba_MobaModelFeature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "moba_MobaModelFeature"):
                    opp_val = getattr(item, "moba_MobaModelFeature", None)
                    
                    setattr(item, "moba_MobaModelFeature", self)
                    

class MobaModelFeature:

    pass
class moba_MobaApplication(MobaModelFeature):

    def __init__(self, javaPackage: str, moba_MobaApplication: "moba_MobaProject" = None, moba_MobaApplication4: "moba_MobaProject" = None, moba_MobaApplication10: "moba_MobaTemplate" = None, moba_MobaApplication6: "moba_MobaCache" = None, moba_MobaApplication8: set["moba_MobaApplicationFeature"] = None):
        self.javaPackage = javaPackage
        self.moba_MobaApplication = moba_MobaApplication
        self.moba_MobaApplication4 = moba_MobaApplication4
        self.moba_MobaApplication10 = moba_MobaApplication10
        self.moba_MobaApplication6 = moba_MobaApplication6
        self.moba_MobaApplication8 = moba_MobaApplication8 if moba_MobaApplication8 is not None else set()
        
    @property
    def javaPackage(self) -> str:
        return self.__javaPackage

    @javaPackage.setter
    def javaPackage(self, javaPackage: str):
        self.__javaPackage = javaPackage

    @property
    def moba_MobaApplication10(self):
        return self.__moba_MobaApplication10

    @moba_MobaApplication10.setter
    def moba_MobaApplication10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaApplication__moba_MobaApplication10", None)
        self.__moba_MobaApplication10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaTemplate"):
                opp_val = getattr(old_value, "moba_MobaTemplate", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaTemplate", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaTemplate"):
                opp_val = getattr(value, "moba_MobaTemplate", None)
                setattr(value, "moba_MobaTemplate", self)

    @property
    def moba_MobaApplication6(self):
        return self.__moba_MobaApplication6

    @moba_MobaApplication6.setter
    def moba_MobaApplication6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaApplication__moba_MobaApplication6", None)
        self.__moba_MobaApplication6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaCache"):
                opp_val = getattr(old_value, "moba_MobaCache", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaCache", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaCache"):
                opp_val = getattr(value, "moba_MobaCache", None)
                setattr(value, "moba_MobaCache", self)

    @property
    def moba_MobaApplication8(self):
        return self.__moba_MobaApplication8

    @moba_MobaApplication8.setter
    def moba_MobaApplication8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaApplication__moba_MobaApplication8", None)
        self.__moba_MobaApplication8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "moba_MobaApplicationFeature"):
                    opp_val = getattr(item, "moba_MobaApplicationFeature", None)
                    
                    if opp_val == self:
                        setattr(item, "moba_MobaApplicationFeature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "moba_MobaApplicationFeature"):
                    opp_val = getattr(item, "moba_MobaApplicationFeature", None)
                    
                    setattr(item, "moba_MobaApplicationFeature", self)
                    

    @property
    def moba_MobaApplication4(self):
        return self.__moba_MobaApplication4

    @moba_MobaApplication4.setter
    def moba_MobaApplication4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaApplication__moba_MobaApplication4", None)
        self.__moba_MobaApplication4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaProject3"):
                opp_val = getattr(old_value, "moba_MobaProject3", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaProject3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaProject3"):
                opp_val = getattr(value, "moba_MobaProject3", None)
                setattr(value, "moba_MobaProject3", self)

    @property
    def moba_MobaApplication(self):
        return self.__moba_MobaApplication

    @moba_MobaApplication.setter
    def moba_MobaApplication(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaApplication__moba_MobaApplication", None)
        self.__moba_MobaApplication = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaProject"):
                opp_val = getattr(old_value, "moba_MobaProject", None)
                if opp_val == self:
                    setattr(old_value, "moba_MobaProject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaProject"):
                opp_val = getattr(value, "moba_MobaProject", None)
                setattr(value, "moba_MobaProject", self)

class moba_MobaProject(MobaModelFeature):

    pass
class moba_MobaModelFeature(MobaFriendsAble):

    def __init__(self, id: str, name: str, version: str, moba_MobaModelFeature: "moba_MobaModel" = None):
        self.id = id
        self.name = name
        self.version = version
        self.moba_MobaModelFeature = moba_MobaModelFeature
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def moba_MobaModelFeature(self):
        return self.__moba_MobaModelFeature

    @moba_MobaModelFeature.setter
    def moba_MobaModelFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_moba_MobaModelFeature__moba_MobaModelFeature", None)
        self.__moba_MobaModelFeature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moba_MobaModel"):
                opp_val = getattr(old_value, "moba_MobaModel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moba_MobaModel"):
                opp_val = getattr(value, "moba_MobaModel", None)
                if opp_val is None:
                    setattr(value, "moba_MobaModel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
