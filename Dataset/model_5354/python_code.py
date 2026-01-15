from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class UnitVerificationState(Enum):
    UNKNOWN = "UNKNOWN"
    VERIFIED = "VERIFIED"
    UPGRADED = "UPGRADED"


############################################
# Definition of Classes
############################################

class p2_IArtifactRepository(ABC):

    pass
class p2_IArtifactRepositoryManager(ABC):

    pass
class p2_IMetadataRepository(ABC):

    pass
class p2_IMetadataRepositoryManager(ABC):

    pass
class p2_LocationType:

    def __init__(self, includeAllPlatforms: str, includeConfigurePhase: str, includeMode: str, includeSource: str, type: str, p2_LocationType8: set["p2_UnitType"] = None, p2_LocationType10: "p2_RepositoryType" = None, p2_LocationType: "p2_LocationsType" = None):
        self.includeAllPlatforms = includeAllPlatforms
        self.includeConfigurePhase = includeConfigurePhase
        self.includeMode = includeMode
        self.includeSource = includeSource
        self.type = type
        self.p2_LocationType8 = p2_LocationType8 if p2_LocationType8 is not None else set()
        self.p2_LocationType10 = p2_LocationType10
        self.p2_LocationType = p2_LocationType
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def includeConfigurePhase(self) -> str:
        return self.__includeConfigurePhase

    @includeConfigurePhase.setter
    def includeConfigurePhase(self, includeConfigurePhase: str):
        self.__includeConfigurePhase = includeConfigurePhase

    @property
    def includeSource(self) -> str:
        return self.__includeSource

    @includeSource.setter
    def includeSource(self, includeSource: str):
        self.__includeSource = includeSource

    @property
    def includeMode(self) -> str:
        return self.__includeMode

    @includeMode.setter
    def includeMode(self, includeMode: str):
        self.__includeMode = includeMode

    @property
    def includeAllPlatforms(self) -> str:
        return self.__includeAllPlatforms

    @includeAllPlatforms.setter
    def includeAllPlatforms(self, includeAllPlatforms: str):
        self.__includeAllPlatforms = includeAllPlatforms

    @property
    def p2_LocationType8(self):
        return self.__p2_LocationType8

    @p2_LocationType8.setter
    def p2_LocationType8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_p2_LocationType__p2_LocationType8", None)
        self.__p2_LocationType8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "p2_UnitType"):
                    opp_val = getattr(item, "p2_UnitType", None)
                    
                    if opp_val == self:
                        setattr(item, "p2_UnitType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "p2_UnitType"):
                    opp_val = getattr(item, "p2_UnitType", None)
                    
                    setattr(item, "p2_UnitType", self)
                    

    @property
    def p2_LocationType(self):
        return self.__p2_LocationType

    @p2_LocationType.setter
    def p2_LocationType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_p2_LocationType__p2_LocationType", None)
        self.__p2_LocationType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "p2_LocationsType"):
                opp_val = getattr(old_value, "p2_LocationsType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "p2_LocationsType"):
                opp_val = getattr(value, "p2_LocationsType", None)
                if opp_val is None:
                    setattr(value, "p2_LocationsType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def p2_LocationType10(self):
        return self.__p2_LocationType10

    @p2_LocationType10.setter
    def p2_LocationType10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_p2_LocationType__p2_LocationType10", None)
        self.__p2_LocationType10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "p2_RepositoryType"):
                opp_val = getattr(old_value, "p2_RepositoryType", None)
                if opp_val == self:
                    setattr(old_value, "p2_RepositoryType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "p2_RepositoryType"):
                opp_val = getattr(value, "p2_RepositoryType", None)
                setattr(value, "p2_RepositoryType", self)

    def artifactRepository(self) -> str:
        # TODO: Implement artifactRepository method
        pass

    def metadataRepository(self) -> str:
        # TODO: Implement metadataRepository method
        pass

class p2_LocationsType:

    pass
class p2_TargetType:

    def __init__(self, sequenceNumber: str, name: str, p2_TargetType: "p2_DocumentRoot" = None, p2_TargetType12: "p2_LocationsType" = None):
        self.sequenceNumber = sequenceNumber
        self.name = name
        self.p2_TargetType = p2_TargetType
        self.p2_TargetType12 = p2_TargetType12
        
    @property
    def sequenceNumber(self) -> str:
        return self.__sequenceNumber

    @sequenceNumber.setter
    def sequenceNumber(self, sequenceNumber: str):
        self.__sequenceNumber = sequenceNumber

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def p2_TargetType12(self):
        return self.__p2_TargetType12

    @p2_TargetType12.setter
    def p2_TargetType12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_p2_TargetType__p2_TargetType12", None)
        self.__p2_TargetType12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "p2_LocationsType13"):
                opp_val = getattr(old_value, "p2_LocationsType13", None)
                if opp_val == self:
                    setattr(old_value, "p2_LocationsType13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "p2_LocationsType13"):
                opp_val = getattr(value, "p2_LocationsType13", None)
                setattr(value, "p2_LocationsType13", self)

    @property
    def p2_TargetType(self):
        return self.__p2_TargetType

    @p2_TargetType.setter
    def p2_TargetType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_p2_TargetType__p2_TargetType", None)
        self.__p2_TargetType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "p2_DocumentRoot5"):
                opp_val = getattr(old_value, "p2_DocumentRoot5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "p2_DocumentRoot5"):
                opp_val = getattr(value, "p2_DocumentRoot5", None)
                if opp_val is None:
                    setattr(value, "p2_DocumentRoot5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def metadataRepositoryManager(self) -> str:
        # TODO: Implement metadataRepositoryManager method
        pass

    def artifactRepositoryManager(self) -> str:
        # TODO: Implement artifactRepositoryManager method
        pass

class p2_EStringToStringMapEntry:

    pass
class p2_RepositoryType:

    def __init__(self, location: str, p2_RepositoryType: "p2_LocationType" = None):
        self.location = location
        self.p2_RepositoryType = p2_RepositoryType
        
    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def p2_RepositoryType(self):
        return self.__p2_RepositoryType

    @p2_RepositoryType.setter
    def p2_RepositoryType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_p2_RepositoryType__p2_RepositoryType", None)
        self.__p2_RepositoryType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "p2_LocationType10"):
                opp_val = getattr(old_value, "p2_LocationType10", None)
                if opp_val == self:
                    setattr(old_value, "p2_LocationType10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "p2_LocationType10"):
                opp_val = getattr(value, "p2_LocationType10", None)
                setattr(value, "p2_LocationType10", self)

class p2_UnitType:

    def __init__(self, id: str, version: str, state: str, p2_UnitType: "p2_LocationType" = None):
        self.id = id
        self.version = version
        self.state = state
        self.p2_UnitType = p2_UnitType
        
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
    def state(self) -> str:
        return self.__state

    @state.setter
    def state(self, state: str):
        self.__state = state

    @property
    def p2_UnitType(self):
        return self.__p2_UnitType

    @p2_UnitType.setter
    def p2_UnitType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_p2_UnitType__p2_UnitType", None)
        self.__p2_UnitType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "p2_LocationType8"):
                opp_val = getattr(old_value, "p2_LocationType8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "p2_LocationType8"):
                opp_val = getattr(value, "p2_LocationType8", None)
                if opp_val is None:
                    setattr(value, "p2_LocationType8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def verifyIU(self):
        # TODO: Implement verifyIU method
        pass

class p2_DocumentRoot:

    def __init__(self, mixed: str, p2_DocumentRoot: set["p2_EStringToStringMapEntry"] = None, p2_DocumentRoot2: set["p2_EStringToStringMapEntry"] = None, p2_DocumentRoot5: set["p2_TargetType"] = None):
        self.mixed = mixed
        self.p2_DocumentRoot = p2_DocumentRoot if p2_DocumentRoot is not None else set()
        self.p2_DocumentRoot2 = p2_DocumentRoot2 if p2_DocumentRoot2 is not None else set()
        self.p2_DocumentRoot5 = p2_DocumentRoot5 if p2_DocumentRoot5 is not None else set()
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def p2_DocumentRoot2(self):
        return self.__p2_DocumentRoot2

    @p2_DocumentRoot2.setter
    def p2_DocumentRoot2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_p2_DocumentRoot__p2_DocumentRoot2", None)
        self.__p2_DocumentRoot2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "p2_EStringToStringMapEntry3"):
                    opp_val = getattr(item, "p2_EStringToStringMapEntry3", None)
                    
                    if opp_val == self:
                        setattr(item, "p2_EStringToStringMapEntry3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "p2_EStringToStringMapEntry3"):
                    opp_val = getattr(item, "p2_EStringToStringMapEntry3", None)
                    
                    setattr(item, "p2_EStringToStringMapEntry3", self)
                    

    @property
    def p2_DocumentRoot(self):
        return self.__p2_DocumentRoot

    @p2_DocumentRoot.setter
    def p2_DocumentRoot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_p2_DocumentRoot__p2_DocumentRoot", None)
        self.__p2_DocumentRoot = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "p2_EStringToStringMapEntry"):
                    opp_val = getattr(item, "p2_EStringToStringMapEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "p2_EStringToStringMapEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "p2_EStringToStringMapEntry"):
                    opp_val = getattr(item, "p2_EStringToStringMapEntry", None)
                    
                    setattr(item, "p2_EStringToStringMapEntry", self)
                    

    @property
    def p2_DocumentRoot5(self):
        return self.__p2_DocumentRoot5

    @p2_DocumentRoot5.setter
    def p2_DocumentRoot5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_p2_DocumentRoot__p2_DocumentRoot5", None)
        self.__p2_DocumentRoot5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "p2_TargetType"):
                    opp_val = getattr(item, "p2_TargetType", None)
                    
                    if opp_val == self:
                        setattr(item, "p2_TargetType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "p2_TargetType"):
                    opp_val = getattr(item, "p2_TargetType", None)
                    
                    setattr(item, "p2_TargetType", self)
                    
