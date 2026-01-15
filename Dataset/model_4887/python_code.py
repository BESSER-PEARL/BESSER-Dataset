from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class IUpdateDescriptor:

    pass
class p2_UpdateDescriptor(IUpdateDescriptor):

    pass
class ITouchpointType:

    pass
class p2_TouchpointType(ITouchpointType):

    pass
class ITouchpointInstruction:

    pass
class p2_TouchpointInstruction(ITouchpointInstruction):

    pass
class ITouchpointData:

    pass
class p2_TouchpointData(ITouchpointData):

    pass
class ArtifactDescriptor:

    pass
class p2_SimpleArtifactDescriptor(ArtifactDescriptor):

    def __init__(self, p2_SimpleArtifactDescriptor: set["p2_Property"] = None):
        self.p2_SimpleArtifactDescriptor = p2_SimpleArtifactDescriptor if p2_SimpleArtifactDescriptor is not None else set()
        
    @property
    def p2_SimpleArtifactDescriptor(self):
        return self.__p2_SimpleArtifactDescriptor

    @p2_SimpleArtifactDescriptor.setter
    def p2_SimpleArtifactDescriptor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_p2_SimpleArtifactDescriptor__p2_SimpleArtifactDescriptor", None)
        self.__p2_SimpleArtifactDescriptor = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "p2_Property57"):
                    opp_val = getattr(item, "p2_Property57", None)
                    
                    if opp_val == self:
                        setattr(item, "p2_Property57", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "p2_Property57"):
                    opp_val = getattr(item, "p2_Property57", None)
                    
                    setattr(item, "p2_Property57", self)
                    

    def getRepositoryProperty(self, key: str) -> str:
        # TODO: Implement getRepositoryProperty method
        pass

    def getRepositoryProperties(self):
        # TODO: Implement getRepositoryProperties method
        pass

class IFileArtifactRepository:

    pass
class ArtifactRepository:

    pass
class p2_SimpleArtifactRepository(ArtifactRepository, IFileArtifactRepository):

    pass
class IRequirementChange:

    pass
class p2_RequirementChange(IRequirementChange):

    pass
class IRequiredCapability:

    pass
class Requirement:

    pass
class p2_RequiredCapability(Requirement, IRequiredCapability):

    pass
class IRepositoryReference:

    pass
class p2_RepositoryReference(IRepositoryReference):

    pass
class IProcessingStepDescriptor:

    pass
class p2_ProcessingStepDescriptor(IProcessingStepDescriptor):

    pass
class p2_MetadataRepository:

    pass
class p2_MappingRule:

    def __init__(self, filter: str, output: str, p2_MappingRule: "p2_SimpleArtifactRepository" = None):
        self.filter = filter
        self.output = output
        self.p2_MappingRule = p2_MappingRule
        
    @property
    def output(self) -> str:
        return self.__output

    @output.setter
    def output(self, output: str):
        self.__output = output

    @property
    def filter(self) -> str:
        return self.__filter

    @filter.setter
    def filter(self, filter: str):
        self.__filter = filter

    @property
    def p2_MappingRule(self):
        return self.__p2_MappingRule

    @p2_MappingRule.setter
    def p2_MappingRule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_p2_MappingRule__p2_MappingRule", None)
        self.__p2_MappingRule = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "p2_SimpleArtifactRepository"):
                opp_val = getattr(old_value, "p2_SimpleArtifactRepository", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "p2_SimpleArtifactRepository"):
                opp_val = getattr(value, "p2_SimpleArtifactRepository", None)
                if opp_val is None:
                    setattr(value, "p2_SimpleArtifactRepository", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ILicense:

    pass
class p2_License(ILicense):

    pass
class p2_IVersionedId(ABC):

    def __init__(self, id: str, version: str):
        self.id = id
        self.version = version
        
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

class p2_Repository(ABC):

    pass
class IProvidedCapability:

    pass
class p2_ProvidedCapability(IProvidedCapability):

    pass
class IRequirement:

    pass
class p2_Requirement(IRequirement):

    pass
class p2_IRequiredCapability(IRequirement):

    def __init__(self, name: str, namespace: str, range: str, p2_IRequiredCapability: "p2_IRequirementChange" = None, p2_IRequiredCapability48: "p2_IRequirementChange" = None):
        self.name = name
        self.namespace = namespace
        self.range = range
        self.p2_IRequiredCapability = p2_IRequiredCapability
        self.p2_IRequiredCapability48 = p2_IRequiredCapability48
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def range(self) -> str:
        return self.__range

    @range.setter
    def range(self, range: str):
        self.__range = range

    @property
    def namespace(self) -> str:
        return self.__namespace

    @namespace.setter
    def namespace(self, namespace: str):
        self.__namespace = namespace

    @property
    def p2_IRequiredCapability48(self):
        return self.__p2_IRequiredCapability48

    @p2_IRequiredCapability48.setter
    def p2_IRequiredCapability48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_p2_IRequiredCapability__p2_IRequiredCapability48", None)
        self.__p2_IRequiredCapability48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "p2_IRequirementChange47"):
                opp_val = getattr(old_value, "p2_IRequirementChange47", None)
                if opp_val == self:
                    setattr(old_value, "p2_IRequirementChange47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "p2_IRequirementChange47"):
                opp_val = getattr(value, "p2_IRequirementChange47", None)
                setattr(value, "p2_IRequirementChange47", self)

    @property
    def p2_IRequiredCapability(self):
        return self.__p2_IRequiredCapability

    @p2_IRequiredCapability.setter
    def p2_IRequiredCapability(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_p2_IRequiredCapability__p2_IRequiredCapability", None)
        self.__p2_IRequiredCapability = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "p2_IRequirementChange45"):
                opp_val = getattr(old_value, "p2_IRequirementChange45", None)
                if opp_val == self:
                    setattr(old_value, "p2_IRequirementChange45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "p2_IRequirementChange45"):
                opp_val = getattr(value, "p2_IRequirementChange45", None)
                setattr(value, "p2_IRequirementChange45", self)

class p2_IRepositoryReference(ABC):

    def __init__(self, location: str, type: int, options: int, nickname: str, p2_IRepositoryReference: "p2_MetadataRepository" = None):
        self.location = location
        self.type = type
        self.options = options
        self.nickname = nickname
        self.p2_IRepositoryReference = p2_IRepositoryReference
        
    @property
    def options(self) -> int:
        return self.__options

    @options.setter
    def options(self, options: int):
        self.__options = options

    @property
    def nickname(self) -> str:
        return self.__nickname

    @nickname.setter
    def nickname(self, nickname: str):
        self.__nickname = nickname

    @property
    def type(self) -> int:
        return self.__type

    @type.setter
    def type(self, type: int):
        self.__type = type

    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def p2_IRepositoryReference(self):
        return self.__p2_IRepositoryReference

    @p2_IRepositoryReference.setter
    def p2_IRepositoryReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_p2_IRepositoryReference__p2_IRepositoryReference", None)
        self.__p2_IRepositoryReference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "p2_MetadataRepository52"):
                opp_val = getattr(old_value, "p2_MetadataRepository52", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "p2_MetadataRepository52"):
                opp_val = getattr(value, "p2_MetadataRepository52", None)
                if opp_val is None:
                    setattr(value, "p2_MetadataRepository52", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class p2_IRepository(ABC):

    def __init__(self, location: str, name: str, type: str, version: str, description: str, provider: str, modifiable: bool, provisioningAgent: str):
        self.location = location
        self.name = name
        self.type = type
        self.version = version
        self.description = description
        self.provider = provider
        self.modifiable = modifiable
        self.provisioningAgent = provisioningAgent
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def modifiable(self) -> bool:
        return self.__modifiable

    @modifiable.setter
    def modifiable(self, modifiable: bool):
        self.__modifiable = modifiable

    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def provisioningAgent(self) -> str:
        return self.__provisioningAgent

    @provisioningAgent.setter
    def provisioningAgent(self, provisioningAgent: str):
        self.__provisioningAgent = provisioningAgent

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
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def provider(self) -> str:
        return self.__provider

    @provider.setter
    def provider(self, provider: str):
        self.__provider = provider

    def setProperty(self, key: str, value: str) -> str:
        # TODO: Implement setProperty method
        pass

    def setProperty(self, monitor: str, value: str, key: str) -> str:
        # TODO: Implement setProperty method
        pass

    def getProperty(self, key: str) -> str:
        # TODO: Implement getProperty method
        pass

    def getProperties(self):
        # TODO: Implement getProperties method
        pass

class p2_IQueryable(ABC):

    def __init__(self):
        
    def query(self, query: str, progress: str):
        # TODO: Implement query method
        pass

class p2_IMetadataRepository(ABC):

    def __init__(self):
        
    def addReferences(self, references: str):
        # TODO: Implement addReferences method
        pass

    def removeAll(self):
        # TODO: Implement removeAll method
        pass

    def compress(self, iuPool: str):
        # TODO: Implement compress method
        pass

    def addInstallableUnits(self, installableUnits: str):
        # TODO: Implement addInstallableUnits method
        pass

    def executeBatch(self, monitor: str, runnable: str) -> str:
        # TODO: Implement executeBatch method
        pass

    def removeInstallableUnits(self, installableUnits: str) -> bool:
        # TODO: Implement removeInstallableUnits method
        pass

class p2_ITouchpointInstruction(ABC):

    def __init__(self, body: str, importAttribute: str, p2_ITouchpointInstruction: "p2_InstructionMap" = None):
        self.body = body
        self.importAttribute = importAttribute
        self.p2_ITouchpointInstruction = p2_ITouchpointInstruction
        
    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

    @property
    def importAttribute(self) -> str:
        return self.__importAttribute

    @importAttribute.setter
    def importAttribute(self, importAttribute: str):
        self.__importAttribute = importAttribute

    @property
    def p2_ITouchpointInstruction(self):
        return self.__p2_ITouchpointInstruction

    @p2_ITouchpointInstruction.setter
    def p2_ITouchpointInstruction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_p2_ITouchpointInstruction__p2_ITouchpointInstruction", None)
        self.__p2_ITouchpointInstruction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "p2_InstructionMap"):
                opp_val = getattr(old_value, "p2_InstructionMap", None)
                if opp_val == self:
                    setattr(old_value, "p2_InstructionMap", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "p2_InstructionMap"):
                opp_val = getattr(value, "p2_InstructionMap", None)
                setattr(value, "p2_InstructionMap", self)

class p2_InstructionMap:

    def __init__(self, key: str, p2_InstructionMap: "p2_ITouchpointInstruction" = None, p2_InstructionMap59: "p2_TouchpointData" = None):
        self.key = key
        self.p2_InstructionMap = p2_InstructionMap
        self.p2_InstructionMap59 = p2_InstructionMap59
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def p2_InstructionMap59(self):
        return self.__p2_InstructionMap59

    @p2_InstructionMap59.setter
    def p2_InstructionMap59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_p2_InstructionMap__p2_InstructionMap59", None)
        self.__p2_InstructionMap59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "p2_TouchpointData"):
                opp_val = getattr(old_value, "p2_TouchpointData", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "p2_TouchpointData"):
                opp_val = getattr(value, "p2_TouchpointData", None)
                if opp_val is None:
                    setattr(value, "p2_TouchpointData", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def p2_InstructionMap(self):
        return self.__p2_InstructionMap

    @p2_InstructionMap.setter
    def p2_InstructionMap(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_p2_InstructionMap__p2_InstructionMap", None)
        self.__p2_InstructionMap = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "p2_ITouchpointInstruction"):
                opp_val = getattr(old_value, "p2_ITouchpointInstruction", None)
                if opp_val == self:
                    setattr(old_value, "p2_ITouchpointInstruction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "p2_ITouchpointInstruction"):
                opp_val = getattr(value, "p2_ITouchpointInstruction", None)
                setattr(value, "p2_ITouchpointInstruction", self)

class IInstallableUnitPatch:

    pass
class IInstallableUnitFragment:

    pass
class InstallableUnit:

    pass
class p2_InstallableUnitPatch(InstallableUnit, IInstallableUnitPatch):

    def __init__(self):
        
    def getApplicabilityScope(self) -> str:
        # TODO: Implement getApplicabilityScope method
        pass

class p2_InstallableUnitFragment(InstallableUnit, IInstallableUnitFragment):

    pass
class p2_IRequirementChange(ABC):

    def __init__(self, p2_IRequirementChange: "p2_IInstallableUnitPatch" = None, p2_IRequirementChange45: "p2_IRequiredCapability" = None, p2_IRequirementChange47: "p2_IRequiredCapability" = None):
        self.p2_IRequirementChange = p2_IRequirementChange
        self.p2_IRequirementChange45 = p2_IRequirementChange45
        self.p2_IRequirementChange47 = p2_IRequirementChange47
        
    @property
    def p2_IRequirementChange45(self):
        return self.__p2_IRequirementChange45

    @p2_IRequirementChange45.setter
    def p2_IRequirementChange45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_p2_IRequirementChange__p2_IRequirementChange45", None)
        self.__p2_IRequirementChange45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "p2_IRequiredCapability"):
                opp_val = getattr(old_value, "p2_IRequiredCapability", None)
                if opp_val == self:
                    setattr(old_value, "p2_IRequiredCapability", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "p2_IRequiredCapability"):
                opp_val = getattr(value, "p2_IRequiredCapability", None)
                setattr(value, "p2_IRequiredCapability", self)

    @property
    def p2_IRequirementChange(self):
        return self.__p2_IRequirementChange

    @p2_IRequirementChange.setter
    def p2_IRequirementChange(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_p2_IRequirementChange__p2_IRequirementChange", None)
        self.__p2_IRequirementChange = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "p2_IInstallableUnitPatch"):
                opp_val = getattr(old_value, "p2_IInstallableUnitPatch", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "p2_IInstallableUnitPatch"):
                opp_val = getattr(value, "p2_IInstallableUnitPatch", None)
                if opp_val is None:
                    setattr(value, "p2_IInstallableUnitPatch", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def p2_IRequirementChange47(self):
        return self.__p2_IRequirementChange47

    @p2_IRequirementChange47.setter
    def p2_IRequirementChange47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_p2_IRequirementChange__p2_IRequirementChange47", None)
        self.__p2_IRequirementChange47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "p2_IRequiredCapability48"):
                opp_val = getattr(old_value, "p2_IRequiredCapability48", None)
                if opp_val == self:
                    setattr(old_value, "p2_IRequiredCapability48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "p2_IRequiredCapability48"):
                opp_val = getattr(value, "p2_IRequiredCapability48", None)
                setattr(value, "p2_IRequiredCapability48", self)

    def applyOn(self) -> str:
        # TODO: Implement applyOn method
        pass

    def matches(self, toMatch: str) -> bool:
        # TODO: Implement matches method
        pass

    def newValue(self) -> str:
        # TODO: Implement newValue method
        pass

class IInstallableUnit:

    pass
class p2_IInstallableUnitPatch(IInstallableUnit):

    pass
class p2_IUpdateDescriptor(ABC):

    def __init__(self, description: str, severity: int, location: str, p2_IUpdateDescriptor: "p2_IInstallableUnit" = None):
        self.description = description
        self.severity = severity
        self.location = location
        self.p2_IUpdateDescriptor = p2_IUpdateDescriptor
        
    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def severity(self) -> int:
        return self.__severity

    @severity.setter
    def severity(self, severity: int):
        self.__severity = severity

    @property
    def p2_IUpdateDescriptor(self):
        return self.__p2_IUpdateDescriptor

    @p2_IUpdateDescriptor.setter
    def p2_IUpdateDescriptor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_p2_IUpdateDescriptor__p2_IUpdateDescriptor", None)
        self.__p2_IUpdateDescriptor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "p2_IInstallableUnit31"):
                opp_val = getattr(old_value, "p2_IInstallableUnit31", None)
                if opp_val == self:
                    setattr(old_value, "p2_IInstallableUnit31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "p2_IInstallableUnit31"):
                opp_val = getattr(value, "p2_IInstallableUnit31", None)
                setattr(value, "p2_IInstallableUnit31", self)

    def getIUsBeingUpdated(self):
        # TODO: Implement getIUsBeingUpdated method
        pass

    def isUpdateOf(self, installableUnit: IInstallableUnit) -> bool:
        # TODO: Implement isUpdateOf method
        pass

class p2_ITouchpointType(ABC):

    def __init__(self, id: str, version: str, p2_ITouchpointType: "p2_IInstallableUnit" = None):
        self.id = id
        self.version = version
        self.p2_ITouchpointType = p2_ITouchpointType
        
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
    def p2_ITouchpointType(self):
        return self.__p2_ITouchpointType

    @p2_ITouchpointType.setter
    def p2_ITouchpointType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_p2_ITouchpointType__p2_ITouchpointType", None)
        self.__p2_ITouchpointType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "p2_IInstallableUnit29"):
                opp_val = getattr(old_value, "p2_IInstallableUnit29", None)
                if opp_val == self:
                    setattr(old_value, "p2_IInstallableUnit29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "p2_IInstallableUnit29"):
                opp_val = getattr(value, "p2_IInstallableUnit29", None)
                setattr(value, "p2_IInstallableUnit29", self)

class p2_ITouchpointData(ABC):

    def __init__(self, p2_ITouchpointData: "p2_IInstallableUnit" = None):
        self.p2_ITouchpointData = p2_ITouchpointData
        
    @property
    def p2_ITouchpointData(self):
        return self.__p2_ITouchpointData

    @p2_ITouchpointData.setter
    def p2_ITouchpointData(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_p2_ITouchpointData__p2_ITouchpointData", None)
        self.__p2_ITouchpointData = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "p2_IInstallableUnit27"):
                opp_val = getattr(old_value, "p2_IInstallableUnit27", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "p2_IInstallableUnit27"):
                opp_val = getattr(value, "p2_IInstallableUnit27", None)
                if opp_val is None:
                    setattr(value, "p2_IInstallableUnit27", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def getInstruction(self, key: str) -> str:
        # TODO: Implement getInstruction method
        pass

    def getInstructions(self):
        # TODO: Implement getInstructions method
        pass

class p2_IProvidedCapability(ABC):

    def __init__(self, name: str, namespace: str, version: str, p2_IProvidedCapability: "p2_IInstallableUnit" = None):
        self.name = name
        self.namespace = namespace
        self.version = version
        self.p2_IProvidedCapability = p2_IProvidedCapability
        
    @property
    def namespace(self) -> str:
        return self.__namespace

    @namespace.setter
    def namespace(self, namespace: str):
        self.__namespace = namespace

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
    def p2_IProvidedCapability(self):
        return self.__p2_IProvidedCapability

    @p2_IProvidedCapability.setter
    def p2_IProvidedCapability(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_p2_IProvidedCapability__p2_IProvidedCapability", None)
        self.__p2_IProvidedCapability = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "p2_IInstallableUnit22"):
                opp_val = getattr(old_value, "p2_IInstallableUnit22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "p2_IInstallableUnit22"):
                opp_val = getattr(value, "p2_IInstallableUnit22", None)
                if opp_val is None:
                    setattr(value, "p2_IInstallableUnit22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class p2_IRequirement(ABC):

    def __init__(self, filter: str, max: str, min: str, matches: str, greedy: bool, description: str, p2_IRequirement: "p2_IInstallableUnit" = None, p2_IRequirement25: "p2_IInstallableUnit" = None, p2_IRequirement35: "p2_IInstallableUnitPatch" = None, p2_IRequirement38: "p2_IInstallableUnitPatch" = None, p2_IRequirement42: "p2_InstallableUnitFragment" = None):
        self.filter = filter
        self.max = max
        self.min = min
        self.matches = matches
        self.greedy = greedy
        self.description = description
        self.p2_IRequirement = p2_IRequirement
        self.p2_IRequirement25 = p2_IRequirement25
        self.p2_IRequirement35 = p2_IRequirement35
        self.p2_IRequirement38 = p2_IRequirement38
        self.p2_IRequirement42 = p2_IRequirement42
        
    @property
    def max(self) -> str:
        return self.__max

    @max.setter
    def max(self, max: str):
        self.__max = max

    @property
    def greedy(self) -> bool:
        return self.__greedy

    @greedy.setter
    def greedy(self, greedy: bool):
        self.__greedy = greedy

    @property
    def filter(self) -> str:
        return self.__filter

    @filter.setter
    def filter(self, filter: str):
        self.__filter = filter

    @property
    def min(self) -> str:
        return self.__min

    @min.setter
    def min(self, min: str):
        self.__min = min

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def matches(self) -> str:
        return self.__matches

    @matches.setter
    def matches(self, matches: str):
        self.__matches = matches

    @property
    def p2_IRequirement35(self):
        return self.__p2_IRequirement35

    @p2_IRequirement35.setter
    def p2_IRequirement35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_p2_IRequirement__p2_IRequirement35", None)
        self.__p2_IRequirement35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "p2_IInstallableUnitPatch34"):
                opp_val = getattr(old_value, "p2_IInstallableUnitPatch34", None)
                if opp_val == self:
                    setattr(old_value, "p2_IInstallableUnitPatch34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "p2_IInstallableUnitPatch34"):
                opp_val = getattr(value, "p2_IInstallableUnitPatch34", None)
                setattr(value, "p2_IInstallableUnitPatch34", self)

    @property
    def p2_IRequirement25(self):
        return self.__p2_IRequirement25

    @p2_IRequirement25.setter
    def p2_IRequirement25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_p2_IRequirement__p2_IRequirement25", None)
        self.__p2_IRequirement25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "p2_IInstallableUnit24"):
                opp_val = getattr(old_value, "p2_IInstallableUnit24", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "p2_IInstallableUnit24"):
                opp_val = getattr(value, "p2_IInstallableUnit24", None)
                if opp_val is None:
                    setattr(value, "p2_IInstallableUnit24", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def p2_IRequirement42(self):
        return self.__p2_IRequirement42

    @p2_IRequirement42.setter
    def p2_IRequirement42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_p2_IRequirement__p2_IRequirement42", None)
        self.__p2_IRequirement42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "p2_InstallableUnitFragment"):
                opp_val = getattr(old_value, "p2_InstallableUnitFragment", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "p2_InstallableUnitFragment"):
                opp_val = getattr(value, "p2_InstallableUnitFragment", None)
                if opp_val is None:
                    setattr(value, "p2_InstallableUnitFragment", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def p2_IRequirement38(self):
        return self.__p2_IRequirement38

    @p2_IRequirement38.setter
    def p2_IRequirement38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_p2_IRequirement__p2_IRequirement38", None)
        self.__p2_IRequirement38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "p2_IInstallableUnitPatch37"):
                opp_val = getattr(old_value, "p2_IInstallableUnitPatch37", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "p2_IInstallableUnitPatch37"):
                opp_val = getattr(value, "p2_IInstallableUnitPatch37", None)
                if opp_val is None:
                    setattr(value, "p2_IInstallableUnitPatch37", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def p2_IRequirement(self):
        return self.__p2_IRequirement

    @p2_IRequirement.setter
    def p2_IRequirement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_p2_IRequirement__p2_IRequirement", None)
        self.__p2_IRequirement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "p2_IInstallableUnit20"):
                opp_val = getattr(old_value, "p2_IInstallableUnit20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "p2_IInstallableUnit20"):
                opp_val = getattr(value, "p2_IInstallableUnit20", None)
                if opp_val is None:
                    setattr(value, "p2_IInstallableUnit20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def isMatch(self, installableUnit: IInstallableUnit) -> bool:
        # TODO: Implement isMatch method
        pass

class p2_ILicense(ABC):

    def __init__(self, location: str, body: str, UUID: str, p2_ILicense: "p2_IInstallableUnit" = None):
        self.location = location
        self.body = body
        self.UUID = UUID
        self.p2_ILicense = p2_ILicense
        
    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def UUID(self) -> str:
        return self.__UUID

    @UUID.setter
    def UUID(self, UUID: str):
        self.__UUID = UUID

    @property
    def p2_ILicense(self):
        return self.__p2_ILicense

    @p2_ILicense.setter
    def p2_ILicense(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_p2_ILicense__p2_ILicense", None)
        self.__p2_ILicense = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "p2_IInstallableUnit18"):
                opp_val = getattr(old_value, "p2_IInstallableUnit18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "p2_IInstallableUnit18"):
                opp_val = getattr(value, "p2_IInstallableUnit18", None)
                if opp_val is None:
                    setattr(value, "p2_IInstallableUnit18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class p2_IInstallableUnitFragment(IInstallableUnit):

    pass
class p2_InstallableUnit(IInstallableUnit):

    pass
class p2_IInstallableUnit(ABC):

    def __init__(self, filter: str, resolved: bool, singleton: bool, p2_IInstallableUnit: set["p2_IArtifactKey"] = None, p2_IInstallableUnit14: "p2_ICopyright" = None, p2_IInstallableUnit16: set["p2_IInstallableUnitFragment"] = None, p2_IInstallableUnit18: set["p2_ILicense"] = None, p2_IInstallableUnit20: set["p2_IRequirement"] = None, p2_IInstallableUnit22: set["p2_IProvidedCapability"] = None, p2_IInstallableUnit24: set["p2_IRequirement"] = None, p2_IInstallableUnit27: set["p2_ITouchpointData"] = None, p2_IInstallableUnit29: "p2_ITouchpointType" = None, p2_IInstallableUnit31: "p2_IUpdateDescriptor" = None, p2_IInstallableUnit50: "p2_MetadataRepository" = None):
        self.filter = filter
        self.resolved = resolved
        self.singleton = singleton
        self.p2_IInstallableUnit = p2_IInstallableUnit if p2_IInstallableUnit is not None else set()
        self.p2_IInstallableUnit14 = p2_IInstallableUnit14
        self.p2_IInstallableUnit16 = p2_IInstallableUnit16 if p2_IInstallableUnit16 is not None else set()
        self.p2_IInstallableUnit18 = p2_IInstallableUnit18 if p2_IInstallableUnit18 is not None else set()
        self.p2_IInstallableUnit20 = p2_IInstallableUnit20 if p2_IInstallableUnit20 is not None else set()
        self.p2_IInstallableUnit22 = p2_IInstallableUnit22 if p2_IInstallableUnit22 is not None else set()
        self.p2_IInstallableUnit24 = p2_IInstallableUnit24 if p2_IInstallableUnit24 is not None else set()
        self.p2_IInstallableUnit27 = p2_IInstallableUnit27 if p2_IInstallableUnit27 is not None else set()
        self.p2_IInstallableUnit29 = p2_IInstallableUnit29
        self.p2_IInstallableUnit31 = p2_IInstallableUnit31
        self.p2_IInstallableUnit50 = p2_IInstallableUnit50
        
    @property
    def resolved(self) -> bool:
        return self.__resolved

    @resolved.setter
    def resolved(self, resolved: bool):
        self.__resolved = resolved

    @property
    def singleton(self) -> bool:
        return self.__singleton

    @singleton.setter
    def singleton(self, singleton: bool):
        self.__singleton = singleton

    @property
    def filter(self) -> str:
        return self.__filter

    @filter.setter
    def filter(self, filter: str):
        self.__filter = filter

    @property
    def p2_IInstallableUnit50(self):
        return self.__p2_IInstallableUnit50

    @p2_IInstallableUnit50.setter
    def p2_IInstallableUnit50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_p2_IInstallableUnit__p2_IInstallableUnit50", None)
        self.__p2_IInstallableUnit50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "p2_MetadataRepository"):
                opp_val = getattr(old_value, "p2_MetadataRepository", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "p2_MetadataRepository"):
                opp_val = getattr(value, "p2_MetadataRepository", None)
                if opp_val is None:
                    setattr(value, "p2_MetadataRepository", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def p2_IInstallableUnit20(self):
        return self.__p2_IInstallableUnit20

    @p2_IInstallableUnit20.setter
    def p2_IInstallableUnit20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_p2_IInstallableUnit__p2_IInstallableUnit20", None)
        self.__p2_IInstallableUnit20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "p2_IRequirement"):
                    opp_val = getattr(item, "p2_IRequirement", None)
                    
                    if opp_val == self:
                        setattr(item, "p2_IRequirement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "p2_IRequirement"):
                    opp_val = getattr(item, "p2_IRequirement", None)
                    
                    setattr(item, "p2_IRequirement", self)
                    

    @property
    def p2_IInstallableUnit27(self):
        return self.__p2_IInstallableUnit27

    @p2_IInstallableUnit27.setter
    def p2_IInstallableUnit27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_p2_IInstallableUnit__p2_IInstallableUnit27", None)
        self.__p2_IInstallableUnit27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "p2_ITouchpointData"):
                    opp_val = getattr(item, "p2_ITouchpointData", None)
                    
                    if opp_val == self:
                        setattr(item, "p2_ITouchpointData", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "p2_ITouchpointData"):
                    opp_val = getattr(item, "p2_ITouchpointData", None)
                    
                    setattr(item, "p2_ITouchpointData", self)
                    

    @property
    def p2_IInstallableUnit31(self):
        return self.__p2_IInstallableUnit31

    @p2_IInstallableUnit31.setter
    def p2_IInstallableUnit31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_p2_IInstallableUnit__p2_IInstallableUnit31", None)
        self.__p2_IInstallableUnit31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "p2_IUpdateDescriptor"):
                opp_val = getattr(old_value, "p2_IUpdateDescriptor", None)
                if opp_val == self:
                    setattr(old_value, "p2_IUpdateDescriptor", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "p2_IUpdateDescriptor"):
                opp_val = getattr(value, "p2_IUpdateDescriptor", None)
                setattr(value, "p2_IUpdateDescriptor", self)

    @property
    def p2_IInstallableUnit22(self):
        return self.__p2_IInstallableUnit22

    @p2_IInstallableUnit22.setter
    def p2_IInstallableUnit22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_p2_IInstallableUnit__p2_IInstallableUnit22", None)
        self.__p2_IInstallableUnit22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "p2_IProvidedCapability"):
                    opp_val = getattr(item, "p2_IProvidedCapability", None)
                    
                    if opp_val == self:
                        setattr(item, "p2_IProvidedCapability", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "p2_IProvidedCapability"):
                    opp_val = getattr(item, "p2_IProvidedCapability", None)
                    
                    setattr(item, "p2_IProvidedCapability", self)
                    

    @property
    def p2_IInstallableUnit(self):
        return self.__p2_IInstallableUnit

    @p2_IInstallableUnit.setter
    def p2_IInstallableUnit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_p2_IInstallableUnit__p2_IInstallableUnit", None)
        self.__p2_IInstallableUnit = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "p2_IArtifactKey12"):
                    opp_val = getattr(item, "p2_IArtifactKey12", None)
                    
                    if opp_val == self:
                        setattr(item, "p2_IArtifactKey12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "p2_IArtifactKey12"):
                    opp_val = getattr(item, "p2_IArtifactKey12", None)
                    
                    setattr(item, "p2_IArtifactKey12", self)
                    

    @property
    def p2_IInstallableUnit24(self):
        return self.__p2_IInstallableUnit24

    @p2_IInstallableUnit24.setter
    def p2_IInstallableUnit24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_p2_IInstallableUnit__p2_IInstallableUnit24", None)
        self.__p2_IInstallableUnit24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "p2_IRequirement25"):
                    opp_val = getattr(item, "p2_IRequirement25", None)
                    
                    if opp_val == self:
                        setattr(item, "p2_IRequirement25", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "p2_IRequirement25"):
                    opp_val = getattr(item, "p2_IRequirement25", None)
                    
                    setattr(item, "p2_IRequirement25", self)
                    

    @property
    def p2_IInstallableUnit18(self):
        return self.__p2_IInstallableUnit18

    @p2_IInstallableUnit18.setter
    def p2_IInstallableUnit18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_p2_IInstallableUnit__p2_IInstallableUnit18", None)
        self.__p2_IInstallableUnit18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "p2_ILicense"):
                    opp_val = getattr(item, "p2_ILicense", None)
                    
                    if opp_val == self:
                        setattr(item, "p2_ILicense", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "p2_ILicense"):
                    opp_val = getattr(item, "p2_ILicense", None)
                    
                    setattr(item, "p2_ILicense", self)
                    

    @property
    def p2_IInstallableUnit14(self):
        return self.__p2_IInstallableUnit14

    @p2_IInstallableUnit14.setter
    def p2_IInstallableUnit14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_p2_IInstallableUnit__p2_IInstallableUnit14", None)
        self.__p2_IInstallableUnit14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "p2_ICopyright"):
                opp_val = getattr(old_value, "p2_ICopyright", None)
                if opp_val == self:
                    setattr(old_value, "p2_ICopyright", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "p2_ICopyright"):
                opp_val = getattr(value, "p2_ICopyright", None)
                setattr(value, "p2_ICopyright", self)

    @property
    def p2_IInstallableUnit16(self):
        return self.__p2_IInstallableUnit16

    @p2_IInstallableUnit16.setter
    def p2_IInstallableUnit16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_p2_IInstallableUnit__p2_IInstallableUnit16", None)
        self.__p2_IInstallableUnit16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "p2_IInstallableUnitFragment"):
                    opp_val = getattr(item, "p2_IInstallableUnitFragment", None)
                    
                    if opp_val == self:
                        setattr(item, "p2_IInstallableUnitFragment", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "p2_IInstallableUnitFragment"):
                    opp_val = getattr(item, "p2_IInstallableUnitFragment", None)
                    
                    setattr(item, "p2_IInstallableUnitFragment", self)
                    

    @property
    def p2_IInstallableUnit29(self):
        return self.__p2_IInstallableUnit29

    @p2_IInstallableUnit29.setter
    def p2_IInstallableUnit29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_p2_IInstallableUnit__p2_IInstallableUnit29", None)
        self.__p2_IInstallableUnit29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "p2_ITouchpointType"):
                opp_val = getattr(old_value, "p2_ITouchpointType", None)
                if opp_val == self:
                    setattr(old_value, "p2_ITouchpointType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "p2_ITouchpointType"):
                opp_val = getattr(value, "p2_ITouchpointType", None)
                setattr(value, "p2_ITouchpointType", self)

    def unresolved(self) -> str:
        # TODO: Implement unresolved method
        pass

    def getProperty(self, key: str, locale: str) -> str:
        # TODO: Implement getProperty method
        pass

    def getCopyright(self, locale: str) -> ICopyright:
        # TODO: Implement getCopyright method
        pass

    def getProperties(self):
        # TODO: Implement getProperties method
        pass

    def getLicenses(self, locale: str) -> str:
        # TODO: Implement getLicenses method
        pass

    def getProperty(self, key: str) -> str:
        # TODO: Implement getProperty method
        pass

    def satisfies(self, candidate: str) -> bool:
        # TODO: Implement satisfies method
        pass

class IArtifactRepository:

    pass
class p2_IFileArtifactRepository(IArtifactRepository):

    def __init__(self):
        
    def getArtifactFile(self, key: IArtifactKey) -> str:
        # TODO: Implement getArtifactFile method
        pass

    def getArtifactFile(self, descriptor: IArtifactDescriptor) -> str:
        # TODO: Implement getArtifactFile method
        pass

class p2_ICopyright(ABC):

    def __init__(self, location: str, body: str, p2_ICopyright: "p2_IInstallableUnit" = None):
        self.location = location
        self.body = body
        self.p2_ICopyright = p2_ICopyright
        
    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

    @property
    def p2_ICopyright(self):
        return self.__p2_ICopyright

    @p2_ICopyright.setter
    def p2_ICopyright(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_p2_ICopyright__p2_ICopyright", None)
        self.__p2_ICopyright = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "p2_IInstallableUnit14"):
                opp_val = getattr(old_value, "p2_IInstallableUnit14", None)
                if opp_val == self:
                    setattr(old_value, "p2_IInstallableUnit14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "p2_IInstallableUnit14"):
                opp_val = getattr(value, "p2_IInstallableUnit14", None)
                setattr(value, "p2_IInstallableUnit14", self)

class p2_IArtifactRepository(ABC):

    def __init__(self):
        
    def getRawArtifact(self, destination: str, monitor: str, descriptor: IArtifactDescriptor) -> str:
        # TODO: Implement getRawArtifact method
        pass

    def createArtifactKey(self, classifier: str, version: str, id: str) -> IArtifactKey:
        # TODO: Implement createArtifactKey method
        pass

    def contains(self, key: IArtifactKey) -> bool:
        # TODO: Implement contains method
        pass

    def getArtifact(self, monitor: str, descriptor: IArtifactDescriptor, destination: str) -> str:
        # TODO: Implement getArtifact method
        pass

    def removeDescriptors(self, monitor: str, keys: str):
        # TODO: Implement removeDescriptors method
        pass

    def removeDescriptor(self, descriptor: IArtifactDescriptor):
        # TODO: Implement removeDescriptor method
        pass

    def contains(self, descriptor: IArtifactDescriptor) -> bool:
        # TODO: Implement contains method
        pass

    def removeAll(self):
        # TODO: Implement removeAll method
        pass

    def removeDescriptors(self, keys: str):
        # TODO: Implement removeDescriptors method
        pass

    def getArtifactDescriptors(self, key: IArtifactKey) -> str:
        # TODO: Implement getArtifactDescriptors method
        pass

    def addDescriptor(self, descriptor: IArtifactDescriptor):
        # TODO: Implement addDescriptor method
        pass

    def removeDescriptors(self, descriptors: str, monitor: str):
        # TODO: Implement removeDescriptors method
        pass

    def addDescriptor(self, monitor: str, descriptor: IArtifactDescriptor):
        # TODO: Implement addDescriptor method
        pass

    def createArtifactDescriptor(self, key: IArtifactKey) -> IArtifactDescriptor:
        # TODO: Implement createArtifactDescriptor method
        pass

    def removeDescriptor(self, monitor: str, key: IArtifactKey):
        # TODO: Implement removeDescriptor method
        pass

    def descriptorQueryable(self):
        # TODO: Implement descriptorQueryable method
        pass

    def removeAll(self, monitor: str):
        # TODO: Implement removeAll method
        pass

    def executeBatch(self, runnable: str, monitor: str) -> str:
        # TODO: Implement executeBatch method
        pass

    def addDescriptors(self, descriptors: str):
        # TODO: Implement addDescriptors method
        pass

    def removeDescriptors(self, descriptors: str):
        # TODO: Implement removeDescriptors method
        pass

    def getArtifacts(self, requests: str, monitor: str) -> str:
        # TODO: Implement getArtifacts method
        pass

    def addDescriptors(self, descriptors: str, monitor: str):
        # TODO: Implement addDescriptors method
        pass

    def removeDescriptor(self, descriptor: IArtifactDescriptor, monitor: str):
        # TODO: Implement removeDescriptor method
        pass

    def removeDescriptor(self, key: IArtifactKey):
        # TODO: Implement removeDescriptor method
        pass

    def getOutputStream(self, descriptor: IArtifactDescriptor) -> str:
        # TODO: Implement getOutputStream method
        pass

class p2_IAdaptable(ABC):

    def __init__(self):
        
    def getAdapter(self, adapter: str) -> str:
        # TODO: Implement getAdapter method
        pass

class p2_Comparable(ABC):

    def __init__(self):
        
    def compareTo(self, o: str) -> int:
        # TODO: Implement compareTo method
        pass

class p2_IArtifactDescriptor(ABC):

    def __init__(self, p2_IArtifactDescriptor: "p2_ArtifactsByKey" = None, p2_IArtifactDescriptor9: "p2_IArtifactKey" = None):
        self.p2_IArtifactDescriptor = p2_IArtifactDescriptor
        self.p2_IArtifactDescriptor9 = p2_IArtifactDescriptor9
        
    @property
    def p2_IArtifactDescriptor9(self):
        return self.__p2_IArtifactDescriptor9

    @p2_IArtifactDescriptor9.setter
    def p2_IArtifactDescriptor9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_p2_IArtifactDescriptor__p2_IArtifactDescriptor9", None)
        self.__p2_IArtifactDescriptor9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "p2_IArtifactKey10"):
                opp_val = getattr(old_value, "p2_IArtifactKey10", None)
                if opp_val == self:
                    setattr(old_value, "p2_IArtifactKey10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "p2_IArtifactKey10"):
                opp_val = getattr(value, "p2_IArtifactKey10", None)
                setattr(value, "p2_IArtifactKey10", self)

    @property
    def p2_IArtifactDescriptor(self):
        return self.__p2_IArtifactDescriptor

    @p2_IArtifactDescriptor.setter
    def p2_IArtifactDescriptor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_p2_IArtifactDescriptor__p2_IArtifactDescriptor", None)
        self.__p2_IArtifactDescriptor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "p2_ArtifactsByKey7"):
                opp_val = getattr(old_value, "p2_ArtifactsByKey7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "p2_ArtifactsByKey7"):
                opp_val = getattr(value, "p2_ArtifactsByKey7", None)
                if opp_val is None:
                    setattr(value, "p2_ArtifactsByKey7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def getProperty(self, key: str) -> str:
        # TODO: Implement getProperty method
        pass

    def getProperties(self):
        # TODO: Implement getProperties method
        pass

    def getRepository(self) -> str:
        # TODO: Implement getRepository method
        pass

    def getProcessingSteps(self) -> str:
        # TODO: Implement getProcessingSteps method
        pass

class p2_IArtifactKey(ABC):

    def __init__(self, classifier: str, id: str, version: str, p2_IArtifactKey: "p2_ArtifactsByKey" = None, p2_IArtifactKey10: "p2_IArtifactDescriptor" = None, p2_IArtifactKey12: "p2_IInstallableUnit" = None):
        self.classifier = classifier
        self.id = id
        self.version = version
        self.p2_IArtifactKey = p2_IArtifactKey
        self.p2_IArtifactKey10 = p2_IArtifactKey10
        self.p2_IArtifactKey12 = p2_IArtifactKey12
        
    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def classifier(self) -> str:
        return self.__classifier

    @classifier.setter
    def classifier(self, classifier: str):
        self.__classifier = classifier

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def p2_IArtifactKey12(self):
        return self.__p2_IArtifactKey12

    @p2_IArtifactKey12.setter
    def p2_IArtifactKey12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_p2_IArtifactKey__p2_IArtifactKey12", None)
        self.__p2_IArtifactKey12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "p2_IInstallableUnit"):
                opp_val = getattr(old_value, "p2_IInstallableUnit", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "p2_IInstallableUnit"):
                opp_val = getattr(value, "p2_IInstallableUnit", None)
                if opp_val is None:
                    setattr(value, "p2_IInstallableUnit", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def p2_IArtifactKey(self):
        return self.__p2_IArtifactKey

    @p2_IArtifactKey.setter
    def p2_IArtifactKey(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_p2_IArtifactKey__p2_IArtifactKey", None)
        self.__p2_IArtifactKey = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "p2_ArtifactsByKey5"):
                opp_val = getattr(old_value, "p2_ArtifactsByKey5", None)
                if opp_val == self:
                    setattr(old_value, "p2_ArtifactsByKey5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "p2_ArtifactsByKey5"):
                opp_val = getattr(value, "p2_ArtifactsByKey5", None)
                setattr(value, "p2_ArtifactsByKey5", self)

    @property
    def p2_IArtifactKey10(self):
        return self.__p2_IArtifactKey10

    @p2_IArtifactKey10.setter
    def p2_IArtifactKey10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_p2_IArtifactKey__p2_IArtifactKey10", None)
        self.__p2_IArtifactKey10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "p2_IArtifactDescriptor9"):
                opp_val = getattr(old_value, "p2_IArtifactDescriptor9", None)
                if opp_val == self:
                    setattr(old_value, "p2_IArtifactDescriptor9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "p2_IArtifactDescriptor9"):
                opp_val = getattr(value, "p2_IArtifactDescriptor9", None)
                setattr(value, "p2_IArtifactDescriptor9", self)

    def toExternalForm(self) -> str:
        # TODO: Implement toExternalForm method
        pass

class p2_ArtifactsByKey:

    pass
class p2_ArtifactRepository:

    pass
class p2_IProcessingStepDescriptor(ABC):

    def __init__(self, processorId: str, data: str, required: bool, p2_IProcessingStepDescriptor: "p2_ArtifactDescriptor" = None):
        self.processorId = processorId
        self.data = data
        self.required = required
        self.p2_IProcessingStepDescriptor = p2_IProcessingStepDescriptor
        
    @property
    def processorId(self) -> str:
        return self.__processorId

    @processorId.setter
    def processorId(self, processorId: str):
        self.__processorId = processorId

    @property
    def data(self) -> str:
        return self.__data

    @data.setter
    def data(self, data: str):
        self.__data = data

    @property
    def required(self) -> bool:
        return self.__required

    @required.setter
    def required(self, required: bool):
        self.__required = required

    @property
    def p2_IProcessingStepDescriptor(self):
        return self.__p2_IProcessingStepDescriptor

    @p2_IProcessingStepDescriptor.setter
    def p2_IProcessingStepDescriptor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_p2_IProcessingStepDescriptor__p2_IProcessingStepDescriptor", None)
        self.__p2_IProcessingStepDescriptor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "p2_ArtifactDescriptor2"):
                opp_val = getattr(old_value, "p2_ArtifactDescriptor2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "p2_ArtifactDescriptor2"):
                opp_val = getattr(value, "p2_ArtifactDescriptor2", None)
                if opp_val is None:
                    setattr(value, "p2_ArtifactDescriptor2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class p2_Property:

    def __init__(self, key: str, value: str, p2_Property: "p2_ArtifactDescriptor" = None, p2_Property40: "p2_InstallableUnit" = None, p2_Property54: "p2_Repository" = None, p2_Property57: "p2_SimpleArtifactDescriptor" = None):
        self.key = key
        self.value = value
        self.p2_Property = p2_Property
        self.p2_Property40 = p2_Property40
        self.p2_Property54 = p2_Property54
        self.p2_Property57 = p2_Property57
        
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
    def p2_Property40(self):
        return self.__p2_Property40

    @p2_Property40.setter
    def p2_Property40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_p2_Property__p2_Property40", None)
        self.__p2_Property40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "p2_InstallableUnit"):
                opp_val = getattr(old_value, "p2_InstallableUnit", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "p2_InstallableUnit"):
                opp_val = getattr(value, "p2_InstallableUnit", None)
                if opp_val is None:
                    setattr(value, "p2_InstallableUnit", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def p2_Property54(self):
        return self.__p2_Property54

    @p2_Property54.setter
    def p2_Property54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_p2_Property__p2_Property54", None)
        self.__p2_Property54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "p2_Repository"):
                opp_val = getattr(old_value, "p2_Repository", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "p2_Repository"):
                opp_val = getattr(value, "p2_Repository", None)
                if opp_val is None:
                    setattr(value, "p2_Repository", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def p2_Property57(self):
        return self.__p2_Property57

    @p2_Property57.setter
    def p2_Property57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_p2_Property__p2_Property57", None)
        self.__p2_Property57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "p2_SimpleArtifactDescriptor"):
                opp_val = getattr(old_value, "p2_SimpleArtifactDescriptor", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "p2_SimpleArtifactDescriptor"):
                opp_val = getattr(value, "p2_SimpleArtifactDescriptor", None)
                if opp_val is None:
                    setattr(value, "p2_SimpleArtifactDescriptor", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def p2_Property(self):
        return self.__p2_Property

    @p2_Property.setter
    def p2_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_p2_Property__p2_Property", None)
        self.__p2_Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "p2_ArtifactDescriptor"):
                opp_val = getattr(old_value, "p2_ArtifactDescriptor", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "p2_ArtifactDescriptor"):
                opp_val = getattr(value, "p2_ArtifactDescriptor", None)
                if opp_val is None:
                    setattr(value, "p2_ArtifactDescriptor", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class IArtifactDescriptor:

    pass
class p2_ArtifactDescriptor(IArtifactDescriptor):

    pass
class IArtifactKey:

    pass
class p2_ArtifactKey(IArtifactKey):

    pass
class ICopyright:

    pass
class p2_Copyright(ICopyright):

    pass