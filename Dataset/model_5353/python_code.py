from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class VersionSegment(Enum):
    Major = "Major"
    Minor = "Minor"
    Micro = "Micro"
    Qualifier = "Qualifier"
class RepositoryType(Enum):
    Metadata = "Metadata"
    Artifact = "Artifact"
    Combined = "Combined"
class RequirementType(Enum):
    NONE = "NONE"
    FEATURE = "FEATURE"
    PROJECT = "PROJECT"


############################################
# Definition of Classes
############################################

class ModelElement:

    pass
class p2_Requirement(ModelElement):

    def __init__(self, iD: str, name: str, namespace: str, versionRange: str, optional: bool, greedy: bool, filter: str, type: str, p2_Requirement: "p2_ProfileDefinition" = None):
        self.iD = iD
        self.name = name
        self.namespace = namespace
        self.versionRange = versionRange
        self.optional = optional
        self.greedy = greedy
        self.filter = filter
        self.type = type
        self.p2_Requirement = p2_Requirement
        
    @property
    def versionRange(self) -> str:
        return self.__versionRange

    @versionRange.setter
    def versionRange(self, versionRange: str):
        self.__versionRange = versionRange

    @property
    def greedy(self) -> bool:
        return self.__greedy

    @greedy.setter
    def greedy(self, greedy: bool):
        self.__greedy = greedy

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def optional(self) -> bool:
        return self.__optional

    @optional.setter
    def optional(self, optional: bool):
        self.__optional = optional

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def namespace(self) -> str:
        return self.__namespace

    @namespace.setter
    def namespace(self, namespace: str):
        self.__namespace = namespace

    @property
    def iD(self) -> str:
        return self.__iD

    @iD.setter
    def iD(self, iD: str):
        self.__iD = iD

    @property
    def filter(self) -> str:
        return self.__filter

    @filter.setter
    def filter(self, filter: str):
        self.__filter = filter

    @property
    def p2_Requirement(self):
        return self.__p2_Requirement

    @p2_Requirement.setter
    def p2_Requirement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_p2_Requirement__p2_Requirement", None)
        self.__p2_Requirement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "p2_ProfileDefinition"):
                opp_val = getattr(old_value, "p2_ProfileDefinition", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "p2_ProfileDefinition"):
                opp_val = getattr(value, "p2_ProfileDefinition", None)
                if opp_val is None:
                    setattr(value, "p2_ProfileDefinition", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def setVersionRange(self, segment: str, version: str):
        # TODO: Implement setVersionRange method
        pass

class p2_Repository(ModelElement):

    def __init__(self, type: str, uRL: str, p2_Repository: "p2_ProfileDefinition" = None, p2_Repository4: "p2_RepositoryList" = None):
        self.type = type
        self.uRL = uRL
        self.p2_Repository = p2_Repository
        self.p2_Repository4 = p2_Repository4
        
    @property
    def uRL(self) -> str:
        return self.__uRL

    @uRL.setter
    def uRL(self, uRL: str):
        self.__uRL = uRL

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def p2_Repository4(self):
        return self.__p2_Repository4

    @p2_Repository4.setter
    def p2_Repository4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_p2_Repository__p2_Repository4", None)
        self.__p2_Repository4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "p2_RepositoryList"):
                opp_val = getattr(old_value, "p2_RepositoryList", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "p2_RepositoryList"):
                opp_val = getattr(value, "p2_RepositoryList", None)
                if opp_val is None:
                    setattr(value, "p2_RepositoryList", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def p2_Repository(self):
        return self.__p2_Repository

    @p2_Repository.setter
    def p2_Repository(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_p2_Repository__p2_Repository", None)
        self.__p2_Repository = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "p2_ProfileDefinition2"):
                opp_val = getattr(old_value, "p2_ProfileDefinition2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "p2_ProfileDefinition2"):
                opp_val = getattr(value, "p2_ProfileDefinition2", None)
                if opp_val is None:
                    setattr(value, "p2_ProfileDefinition2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class p2_RepositoryList(ModelElement):

    def __init__(self, name: str, p2_RepositoryList: set["p2_Repository"] = None):
        self.name = name
        self.p2_RepositoryList = p2_RepositoryList if p2_RepositoryList is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def p2_RepositoryList(self):
        return self.__p2_RepositoryList

    @p2_RepositoryList.setter
    def p2_RepositoryList(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_p2_RepositoryList__p2_RepositoryList", None)
        self.__p2_RepositoryList = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "p2_Repository4"):
                    opp_val = getattr(item, "p2_Repository4", None)
                    
                    if opp_val == self:
                        setattr(item, "p2_Repository4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "p2_Repository4"):
                    opp_val = getattr(item, "p2_Repository4", None)
                    
                    setattr(item, "p2_Repository4", self)
                    

class p2_ProfileDefinition(ModelElement):

    def __init__(self, includeSourceBundles: bool, p2_ProfileDefinition: set["p2_Requirement"] = None, p2_ProfileDefinition2: set["p2_Repository"] = None):
        self.includeSourceBundles = includeSourceBundles
        self.p2_ProfileDefinition = p2_ProfileDefinition if p2_ProfileDefinition is not None else set()
        self.p2_ProfileDefinition2 = p2_ProfileDefinition2 if p2_ProfileDefinition2 is not None else set()
        
    @property
    def includeSourceBundles(self) -> bool:
        return self.__includeSourceBundles

    @includeSourceBundles.setter
    def includeSourceBundles(self, includeSourceBundles: bool):
        self.__includeSourceBundles = includeSourceBundles

    @property
    def p2_ProfileDefinition(self):
        return self.__p2_ProfileDefinition

    @p2_ProfileDefinition.setter
    def p2_ProfileDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_p2_ProfileDefinition__p2_ProfileDefinition", None)
        self.__p2_ProfileDefinition = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "p2_Requirement"):
                    opp_val = getattr(item, "p2_Requirement", None)
                    
                    if opp_val == self:
                        setattr(item, "p2_Requirement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "p2_Requirement"):
                    opp_val = getattr(item, "p2_Requirement", None)
                    
                    setattr(item, "p2_Requirement", self)
                    

    @property
    def p2_ProfileDefinition2(self):
        return self.__p2_ProfileDefinition2

    @p2_ProfileDefinition2.setter
    def p2_ProfileDefinition2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_p2_ProfileDefinition__p2_ProfileDefinition2", None)
        self.__p2_ProfileDefinition2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "p2_Repository"):
                    opp_val = getattr(item, "p2_Repository", None)
                    
                    if opp_val == self:
                        setattr(item, "p2_Repository", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "p2_Repository"):
                    opp_val = getattr(item, "p2_Repository", None)
                    
                    setattr(item, "p2_Repository", self)
                    

    def setRequirements(self, requirements: str):
        # TODO: Implement setRequirements method
        pass

    def setRepositories(self, repositories: str):
        # TODO: Implement setRepositories method
        pass

class p2_Configuration(ModelElement):

    def __init__(self, wS: str, oS: str, arch: str):
        self.wS = wS
        self.oS = oS
        self.arch = arch
        
    @property
    def wS(self) -> str:
        return self.__wS

    @wS.setter
    def wS(self, wS: str):
        self.__wS = wS

    @property
    def arch(self) -> str:
        return self.__arch

    @arch.setter
    def arch(self, arch: str):
        self.__arch = arch

    @property
    def oS(self) -> str:
        return self.__oS

    @oS.setter
    def oS(self, oS: str):
        self.__oS = oS
