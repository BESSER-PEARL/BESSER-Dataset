from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class MIDLevel(Enum):
    INSTANCES = "INSTANCES"
    TYPES = "TYPES"
    WORKFLOWS = "WORKFLOWS"
class ModelOrigin(Enum):
    IMPORTED = "IMPORTED"
    CREATED = "CREATED"


############################################
# Definition of Classes
############################################

class operator_mid_GenericElement:

    pass
class mid_operator_OperatorGeneric:

    pass
class operator_mid_Model:

    pass
class mid_operator_OperatorInput:

    pass
class NestingOperator:

    pass
class mid_operator_WorkflowOperator(NestingOperator):

    def __init__(self):
        
    def getNestedWorkflowMID(self) -> str:
        # TODO: Implement getNestedWorkflowMID method
        pass

class GenericEndpoint:

    pass
class operator_mid_ModelEndpoint:

    pass
class ModelElementEndpoint:

    pass
class ModelElementEndpointReference:

    pass
class ExtendibleElementEndpointReference:

    pass
class mid_relationship_ModelElementEndpointReference(ExtendibleElementEndpointReference):

    def __init__(self, ModelElementReference58: "ModelElementReference" = None):
        self.ModelElementReference58 = ModelElementReference58
        
    @property
    def ModelElementReference58(self):
        return self.__ModelElementReference58

    @ModelElementReference58.setter
    def ModelElementReference58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mid_relationship_ModelElementEndpointReference__ModelElementReference58", None)
        self.__ModelElementReference58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "relationship59"):
                opp_val = getattr(old_value, "relationship59", None)
                if opp_val == self:
                    setattr(old_value, "relationship59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "relationship59"):
                opp_val = getattr(value, "relationship59", None)
                setattr(value, "relationship59", self)

    def getSupertypeRef(self) -> str:
        # TODO: Implement getSupertypeRef method
        pass

    def getObject(self) -> str:
        # TODO: Implement getObject method
        pass

    def deleteTypeReference(self, isFullDelete: bool):
        # TODO: Implement deleteTypeReference method
        pass

    def deleteTypeAndReference(self, isFullDelete: bool):
        # TODO: Implement deleteTypeAndReference method
        pass

    def deleteInstanceAndReference(self, isFullDelete: bool):
        # TODO: Implement deleteInstanceAndReference method
        pass

class mid_relationship_ModelEndpointReference(ExtendibleElementEndpointReference):

    def __init__(self, mid_relationship_ModelEndpointReference: set["ModelElementReference"] = None):
        self.mid_relationship_ModelEndpointReference = mid_relationship_ModelEndpointReference if mid_relationship_ModelEndpointReference is not None else set()
        
    @property
    def mid_relationship_ModelEndpointReference(self):
        return self.__mid_relationship_ModelEndpointReference

    @mid_relationship_ModelEndpointReference.setter
    def mid_relationship_ModelEndpointReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mid_relationship_ModelEndpointReference__mid_relationship_ModelEndpointReference", None)
        self.__mid_relationship_ModelEndpointReference = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ModelElementReference"):
                    opp_val = getattr(item, "ModelElementReference", None)
                    
                    if opp_val == self:
                        setattr(item, "ModelElementReference", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ModelElementReference"):
                    opp_val = getattr(item, "ModelElementReference", None)
                    
                    setattr(item, "ModelElementReference", self)
                    

    def acceptModelElementType(self, metamodelObj: str) -> bool:
        # TODO: Implement acceptModelElementType method
        pass

    def createModelElementInstanceAndReference(self, modelObj: str, newModelElemName: str) -> str:
        # TODO: Implement createModelElementInstanceAndReference method
        pass

    def getObject(self) -> str:
        # TODO: Implement getObject method
        pass

    def getSupertypeRef(self) -> str:
        # TODO: Implement getSupertypeRef method
        pass

    def deleteTypeReference(self, isFullDelete: bool):
        # TODO: Implement deleteTypeReference method
        pass

    def acceptModelElementInstance(self, modelObj: str) -> str:
        # TODO: Implement acceptModelElementInstance method
        pass

class ModelElementReference:

    pass
class mid_relationship_ExtendibleElementReference(ABC):

    def __init__(self, modifiable: bool, mid_relationship_ExtendibleElementReference: "relationship_mid_ExtendibleElement" = None, mid_relationship_ExtendibleElementReference40: "relationship_mid_ExtendibleElement" = None, mid_relationship_ExtendibleElementReference43: "ExtendibleElementReference" = None):
        self.modifiable = modifiable
        self.mid_relationship_ExtendibleElementReference = mid_relationship_ExtendibleElementReference
        self.mid_relationship_ExtendibleElementReference40 = mid_relationship_ExtendibleElementReference40
        self.mid_relationship_ExtendibleElementReference43 = mid_relationship_ExtendibleElementReference43
        
    @property
    def modifiable(self) -> bool:
        return self.__modifiable

    @modifiable.setter
    def modifiable(self, modifiable: bool):
        self.__modifiable = modifiable

    @property
    def mid_relationship_ExtendibleElementReference40(self):
        return self.__mid_relationship_ExtendibleElementReference40

    @mid_relationship_ExtendibleElementReference40.setter
    def mid_relationship_ExtendibleElementReference40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mid_relationship_ExtendibleElementReference__mid_relationship_ExtendibleElementReference40", None)
        self.__mid_relationship_ExtendibleElementReference40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "relationship_mid_ExtendibleElement41"):
                opp_val = getattr(old_value, "relationship_mid_ExtendibleElement41", None)
                if opp_val == self:
                    setattr(old_value, "relationship_mid_ExtendibleElement41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "relationship_mid_ExtendibleElement41"):
                opp_val = getattr(value, "relationship_mid_ExtendibleElement41", None)
                setattr(value, "relationship_mid_ExtendibleElement41", self)

    @property
    def mid_relationship_ExtendibleElementReference(self):
        return self.__mid_relationship_ExtendibleElementReference

    @mid_relationship_ExtendibleElementReference.setter
    def mid_relationship_ExtendibleElementReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mid_relationship_ExtendibleElementReference__mid_relationship_ExtendibleElementReference", None)
        self.__mid_relationship_ExtendibleElementReference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "relationship_mid_ExtendibleElement"):
                opp_val = getattr(old_value, "relationship_mid_ExtendibleElement", None)
                if opp_val == self:
                    setattr(old_value, "relationship_mid_ExtendibleElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "relationship_mid_ExtendibleElement"):
                opp_val = getattr(value, "relationship_mid_ExtendibleElement", None)
                setattr(value, "relationship_mid_ExtendibleElement", self)

    @property
    def mid_relationship_ExtendibleElementReference43(self):
        return self.__mid_relationship_ExtendibleElementReference43

    @mid_relationship_ExtendibleElementReference43.setter
    def mid_relationship_ExtendibleElementReference43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mid_relationship_ExtendibleElementReference__mid_relationship_ExtendibleElementReference43", None)
        self.__mid_relationship_ExtendibleElementReference43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ExtendibleElementReference"):
                opp_val = getattr(old_value, "ExtendibleElementReference", None)
                if opp_val == self:
                    setattr(old_value, "ExtendibleElementReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ExtendibleElementReference"):
                opp_val = getattr(value, "ExtendibleElementReference", None)
                setattr(value, "ExtendibleElementReference", self)

    def isTypesLevel(self) -> bool:
        # TODO: Implement isTypesLevel method
        pass

    def isInstancesLevel(self) -> bool:
        # TODO: Implement isInstancesLevel method
        pass

    def getObject(self) -> ExtendibleElement:
        # TODO: Implement getObject method
        pass

    def getMIDContainer(self) -> str:
        # TODO: Implement getMIDContainer method
        pass

    def isWorkflowsLevel(self) -> bool:
        # TODO: Implement isWorkflowsLevel method
        pass

    def getUri(self) -> str:
        # TODO: Implement getUri method
        pass

class relationship_mid_Model:

    pass
class ModelRel:

    pass
class mid_relationship_BinaryModelRel(ModelRel):

    def __init__(self, mid_relationship_BinaryModelRel: "relationship_mid_Model" = None, mid_relationship_BinaryModelRel36: "relationship_mid_Model" = None):
        self.mid_relationship_BinaryModelRel = mid_relationship_BinaryModelRel
        self.mid_relationship_BinaryModelRel36 = mid_relationship_BinaryModelRel36
        
    @property
    def mid_relationship_BinaryModelRel36(self):
        return self.__mid_relationship_BinaryModelRel36

    @mid_relationship_BinaryModelRel36.setter
    def mid_relationship_BinaryModelRel36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mid_relationship_BinaryModelRel__mid_relationship_BinaryModelRel36", None)
        self.__mid_relationship_BinaryModelRel36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "relationship_mid_Model37"):
                opp_val = getattr(old_value, "relationship_mid_Model37", None)
                if opp_val == self:
                    setattr(old_value, "relationship_mid_Model37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "relationship_mid_Model37"):
                opp_val = getattr(value, "relationship_mid_Model37", None)
                setattr(value, "relationship_mid_Model37", self)

    @property
    def mid_relationship_BinaryModelRel(self):
        return self.__mid_relationship_BinaryModelRel

    @mid_relationship_BinaryModelRel.setter
    def mid_relationship_BinaryModelRel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mid_relationship_BinaryModelRel__mid_relationship_BinaryModelRel", None)
        self.__mid_relationship_BinaryModelRel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "relationship_mid_Model"):
                opp_val = getattr(old_value, "relationship_mid_Model", None)
                if opp_val == self:
                    setattr(old_value, "relationship_mid_Model", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "relationship_mid_Model"):
                opp_val = getattr(value, "relationship_mid_Model", None)
                setattr(value, "relationship_mid_Model", self)

    def addModelType(self, modelType: Model, isBinarySrc: bool):
        # TODO: Implement addModelType method
        pass

class ExtendibleElementReference:

    pass
class mid_relationship_MappingReference(ExtendibleElementReference):

    def __init__(self, mid_relationship_MappingReference: set["ModelElementEndpointReference"] = None, ExtendibleElementReference: "mid_relationship_ExtendibleElementReference"):
        self.mid_relationship_MappingReference = mid_relationship_MappingReference if mid_relationship_MappingReference is not None else set()
        
    @property
    def mid_relationship_MappingReference(self):
        return self.__mid_relationship_MappingReference

    @mid_relationship_MappingReference.setter
    def mid_relationship_MappingReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mid_relationship_MappingReference__mid_relationship_MappingReference", None)
        self.__mid_relationship_MappingReference = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ModelElementEndpointReference51"):
                    opp_val = getattr(item, "ModelElementEndpointReference51", None)
                    
                    if opp_val == self:
                        setattr(item, "ModelElementEndpointReference51", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ModelElementEndpointReference51"):
                    opp_val = getattr(item, "ModelElementEndpointReference51", None)
                    
                    setattr(item, "ModelElementEndpointReference51", self)
                    

    def getObject(self) -> str:
        # TODO: Implement getObject method
        pass

    def deleteTypeAndReference(self):
        # TODO: Implement deleteTypeAndReference method
        pass

    def deleteTypeReference(self):
        # TODO: Implement deleteTypeReference method
        pass

    def getSupertypeRef(self) -> str:
        # TODO: Implement getSupertypeRef method
        pass

    def deleteInstanceAndReference(self):
        # TODO: Implement deleteInstanceAndReference method
        pass

    def deleteInstanceReference(self):
        # TODO: Implement deleteInstanceReference method
        pass

class mid_relationship_ModelElementReference(ExtendibleElementReference):

    def __init__(self, ModelElementEndpointReference: set["ModelElementEndpointReference"] = None, ExtendibleElementReference: "mid_relationship_ExtendibleElementReference"):
        self.ModelElementEndpointReference = ModelElementEndpointReference if ModelElementEndpointReference is not None else set()
        
    @property
    def ModelElementEndpointReference(self):
        return self.__ModelElementEndpointReference

    @ModelElementEndpointReference.setter
    def ModelElementEndpointReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mid_relationship_ModelElementReference__ModelElementEndpointReference", None)
        self.__ModelElementEndpointReference = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "relationship"):
                    opp_val = getattr(item, "relationship", None)
                    
                    if opp_val == self:
                        setattr(item, "relationship", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "relationship"):
                    opp_val = getattr(item, "relationship", None)
                    
                    setattr(item, "relationship", self)
                    

    def getObject(self) -> str:
        # TODO: Implement getObject method
        pass

    def getSupertypeRef(self) -> str:
        # TODO: Implement getSupertypeRef method
        pass

    def deleteTypeReference(self):
        # TODO: Implement deleteTypeReference method
        pass

    def deleteInstanceReference(self):
        # TODO: Implement deleteInstanceReference method
        pass

class mid_relationship_ExtendibleElementEndpointReference(ExtendibleElementReference):

    def __init__(self, ExtendibleElementReference: "mid_relationship_ExtendibleElementReference"):
        
    def getTargetUri(self) -> str:
        # TODO: Implement getTargetUri method
        pass

    def getSupertypeRef(self) -> str:
        # TODO: Implement getSupertypeRef method
        pass

    def getObject(self) -> ExtendibleElementEndpoint:
        # TODO: Implement getObject method
        pass

class relationship_mid_ExtendibleElement:

    pass
class MappingReference:

    pass
class mid_relationship_BinaryMappingReference(MappingReference):

    def __init__(self, mid_relationship_BinaryMappingReference: "ModelElementReference" = None, mid_relationship_BinaryMappingReference55: "ModelElementReference" = None, MappingReference: "mid_relationship_ModelRel"):
        self.mid_relationship_BinaryMappingReference = mid_relationship_BinaryMappingReference
        self.mid_relationship_BinaryMappingReference55 = mid_relationship_BinaryMappingReference55
        
    @property
    def mid_relationship_BinaryMappingReference(self):
        return self.__mid_relationship_BinaryMappingReference

    @mid_relationship_BinaryMappingReference.setter
    def mid_relationship_BinaryMappingReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mid_relationship_BinaryMappingReference__mid_relationship_BinaryMappingReference", None)
        self.__mid_relationship_BinaryMappingReference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ModelElementReference53"):
                opp_val = getattr(old_value, "ModelElementReference53", None)
                if opp_val == self:
                    setattr(old_value, "ModelElementReference53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ModelElementReference53"):
                opp_val = getattr(value, "ModelElementReference53", None)
                setattr(value, "ModelElementReference53", self)

    @property
    def mid_relationship_BinaryMappingReference55(self):
        return self.__mid_relationship_BinaryMappingReference55

    @mid_relationship_BinaryMappingReference55.setter
    def mid_relationship_BinaryMappingReference55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mid_relationship_BinaryMappingReference__mid_relationship_BinaryMappingReference55", None)
        self.__mid_relationship_BinaryMappingReference55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ModelElementReference56"):
                opp_val = getattr(old_value, "ModelElementReference56", None)
                if opp_val == self:
                    setattr(old_value, "ModelElementReference56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ModelElementReference56"):
                opp_val = getattr(value, "ModelElementReference56", None)
                setattr(value, "ModelElementReference56", self)

    def getObject(self) -> str:
        # TODO: Implement getObject method
        pass

    def addModelElementTypeReference(self, modelElemTypeRef: str, isBinarySrc: bool):
        # TODO: Implement addModelElementTypeReference method
        pass

class ModelEndpointReference:

    pass
class Mapping:

    pass
class mid_relationship_BinaryMapping(Mapping):

    pass
class relationship_mid_ModelEndpoint:

    pass
class Model:

    pass
class mid_relationship_ModelRel(Model):

    def __init__(self, mid_relationship_ModelRel: set["relationship_mid_ModelEndpoint"] = None, mid_relationship_ModelRel29: set["Mapping"] = None, mid_relationship_ModelRel31: set["ModelEndpointReference"] = None, mid_relationship_ModelRel33: set["MappingReference"] = None):
        self.mid_relationship_ModelRel = mid_relationship_ModelRel if mid_relationship_ModelRel is not None else set()
        self.mid_relationship_ModelRel29 = mid_relationship_ModelRel29 if mid_relationship_ModelRel29 is not None else set()
        self.mid_relationship_ModelRel31 = mid_relationship_ModelRel31 if mid_relationship_ModelRel31 is not None else set()
        self.mid_relationship_ModelRel33 = mid_relationship_ModelRel33 if mid_relationship_ModelRel33 is not None else set()
        
    @property
    def mid_relationship_ModelRel29(self):
        return self.__mid_relationship_ModelRel29

    @mid_relationship_ModelRel29.setter
    def mid_relationship_ModelRel29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mid_relationship_ModelRel__mid_relationship_ModelRel29", None)
        self.__mid_relationship_ModelRel29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Mapping"):
                    opp_val = getattr(item, "Mapping", None)
                    
                    if opp_val == self:
                        setattr(item, "Mapping", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Mapping"):
                    opp_val = getattr(item, "Mapping", None)
                    
                    setattr(item, "Mapping", self)
                    

    @property
    def mid_relationship_ModelRel(self):
        return self.__mid_relationship_ModelRel

    @mid_relationship_ModelRel.setter
    def mid_relationship_ModelRel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mid_relationship_ModelRel__mid_relationship_ModelRel", None)
        self.__mid_relationship_ModelRel = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "relationship_mid_ModelEndpoint"):
                    opp_val = getattr(item, "relationship_mid_ModelEndpoint", None)
                    
                    if opp_val == self:
                        setattr(item, "relationship_mid_ModelEndpoint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "relationship_mid_ModelEndpoint"):
                    opp_val = getattr(item, "relationship_mid_ModelEndpoint", None)
                    
                    setattr(item, "relationship_mid_ModelEndpoint", self)
                    

    @property
    def mid_relationship_ModelRel31(self):
        return self.__mid_relationship_ModelRel31

    @mid_relationship_ModelRel31.setter
    def mid_relationship_ModelRel31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mid_relationship_ModelRel__mid_relationship_ModelRel31", None)
        self.__mid_relationship_ModelRel31 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ModelEndpointReference"):
                    opp_val = getattr(item, "ModelEndpointReference", None)
                    
                    if opp_val == self:
                        setattr(item, "ModelEndpointReference", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ModelEndpointReference"):
                    opp_val = getattr(item, "ModelEndpointReference", None)
                    
                    setattr(item, "ModelEndpointReference", self)
                    

    @property
    def mid_relationship_ModelRel33(self):
        return self.__mid_relationship_ModelRel33

    @mid_relationship_ModelRel33.setter
    def mid_relationship_ModelRel33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mid_relationship_ModelRel__mid_relationship_ModelRel33", None)
        self.__mid_relationship_ModelRel33 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MappingReference"):
                    opp_val = getattr(item, "MappingReference", None)
                    
                    if opp_val == self:
                        setattr(item, "MappingReference", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MappingReference"):
                    opp_val = getattr(item, "MappingReference", None)
                    
                    setattr(item, "MappingReference", self)
                    

    def getMetatype(self) -> str:
        # TODO: Implement getMetatype method
        pass

    def createWorkflowInstanceAndEndpoints(self, newModelRelId: str, workflowMID: str, endpointModels: Model) -> str:
        # TODO: Implement createWorkflowInstanceAndEndpoints method
        pass

    def copySubtype(self, origModelRelType: str) -> str:
        # TODO: Implement copySubtype method
        pass

    def createWorkflowBinaryInstanceAndEndpoints(self, newModelRelId: str, endpointTargetModel: Model, workflowMID: str, endpointSourceModel: Model) -> str:
        # TODO: Implement createWorkflowBinaryInstanceAndEndpoints method
        pass

    def createBinarySubtype(self, isMetamodelExtension: bool, newModelRelTypeName: str) -> str:
        # TODO: Implement createBinarySubtype method
        pass

    def getOutlineResourceTypes(self) -> str:
        # TODO: Implement getOutlineResourceTypes method
        pass

    def createBinaryInstance(self, rootModelRelObj: str, newModelRelName: str, instanceMID: str) -> str:
        # TODO: Implement createBinaryInstance method
        pass

    def getMIDContainer(self) -> str:
        # TODO: Implement getMIDContainer method
        pass

    def createInstanceAndEndpoints(self, newModelRelName: str, rootModelRelObj: str, endpointModels: Model, instanceMID: str) -> str:
        # TODO: Implement createInstanceAndEndpoints method
        pass

    def getSupertype(self) -> Model:
        # TODO: Implement getSupertype method
        pass

    def createBinaryInstanceAndEndpoints(self, endpointSourceModel: Model, rootModelRelObj: str, newModelRelName: str, instanceMID: str, endpointTargetModel: Model) -> str:
        # TODO: Implement createBinaryInstanceAndEndpoints method
        pass

    def getOutlineResourceInstances(self) -> str:
        # TODO: Implement getOutlineResourceInstances method
        pass

    def createWorkflowBinaryInstance(self, workflowMID: str, newModelRelId: str) -> str:
        # TODO: Implement createWorkflowBinaryInstance method
        pass

class ExtendibleElementEndpoint:

    pass
class mid_relationship_ModelElementEndpoint(ExtendibleElementEndpoint):

    def __init__(self):
        
    def createTypeReference(self, containerMappingTypeRef: str, modelElemTypeEndpointRef: str, isModifiable: bool, isBinarySrc: bool, targetModelElemTypeRef: str) -> str:
        # TODO: Implement createTypeReference method
        pass

    def createInstanceAndReference(self, containerMappingRef: str, targetModelElemRef: str) -> str:
        # TODO: Implement createInstanceAndReference method
        pass

    def replaceInstanceAndReference(self, targetModelElemRef: str, oldModelElemEndpointRef: str):
        # TODO: Implement replaceInstanceAndReference method
        pass

    def createSubtypeAndReference(self, isBinarySrc: bool, newModelElemTypeEndpointName: str, targetModelElemTypeRef: str, containerMappingTypeRef: str) -> str:
        # TODO: Implement createSubtypeAndReference method
        pass

    def createInstanceReference(self, containerMappingRef: str, targetModelElemRef: str) -> str:
        # TODO: Implement createInstanceReference method
        pass

    def getMetatype(self) -> str:
        # TODO: Implement getMetatype method
        pass

    def getTarget(self) -> str:
        # TODO: Implement getTarget method
        pass

    def getMIDContainer(self) -> str:
        # TODO: Implement getMIDContainer method
        pass

    def deleteType(self, isFullDelete: bool):
        # TODO: Implement deleteType method
        pass

    def getSupertype(self) -> str:
        # TODO: Implement getSupertype method
        pass

    def replaceSubtypeAndReference(self, newModelElemTypeEndpointName: str, targetModelElemTypeRef: str, oldModelElemTypeEndpointRef: str):
        # TODO: Implement replaceSubtypeAndReference method
        pass

class mid_operator_GenericEndpoint(ExtendibleElementEndpoint):

    def __init__(self, metatargetUri: str):
        self.metatargetUri = metatargetUri
        
    @property
    def metatargetUri(self) -> str:
        return self.__metatargetUri

    @metatargetUri.setter
    def metatargetUri(self, metatargetUri: str):
        self.__metatargetUri = metatargetUri

    def getTarget(self) -> GenericElement:
        # TODO: Implement getTarget method
        pass

    def setTarget(self, newTarget: ExtendibleElement):
        # TODO: Implement setTarget method
        pass

    def getSupertype(self) -> str:
        # TODO: Implement getSupertype method
        pass

    def createWorkflowInstance(self, targetGeneric: GenericElement, containerOperator: str) -> str:
        # TODO: Implement createWorkflowInstance method
        pass

    def createInstance(self, containerOperator: str, targetGeneric: GenericElement) -> str:
        # TODO: Implement createInstance method
        pass

    def getMetatype(self) -> str:
        # TODO: Implement getMetatype method
        pass

class mid_ModelEndpoint(ExtendibleElementEndpoint):

    def __init__(self):
        
    def createTypeReference(self, containerModelRelType: str, isModifiable: bool) -> str:
        # TODO: Implement createTypeReference method
        pass

    def createInstance(self, containerOperator: str, targetModel: str, containerFeatureName: str) -> str:
        # TODO: Implement createInstance method
        pass

    def getSupertype(self) -> str:
        # TODO: Implement getSupertype method
        pass

    def createInstance(self, targetModel: str, containerModelRel: str) -> str:
        # TODO: Implement createInstance method
        pass

    def createSubtype(self, isBinarySrc: bool, newModelTypeEndpointName: str, containerModelRelType: str, targetModelType: str) -> str:
        # TODO: Implement createSubtype method
        pass

    def createWorkflowInstance(self, containerModelRel: str, targetModel: str) -> str:
        # TODO: Implement createWorkflowInstance method
        pass

    def getTarget(self) -> str:
        # TODO: Implement getTarget method
        pass

    def deleteType(self, isFullDelete: bool):
        # TODO: Implement deleteType method
        pass

    def createInstanceReference(self, containerModelRel: str) -> str:
        # TODO: Implement createInstanceReference method
        pass

    def deleteInstance(self, isFullDelete: bool):
        # TODO: Implement deleteInstance method
        pass

    def replaceWorkflowInstance(self, targetModel: str, oldModelEndpoint: str):
        # TODO: Implement replaceWorkflowInstance method
        pass

    def deleteWorkflowInstance(self):
        # TODO: Implement deleteWorkflowInstance method
        pass

    def replaceInstance(self, targetModel: str, oldModelEndpoint: str):
        # TODO: Implement replaceInstance method
        pass

    def createWorkflowInstance(self, containerFeatureName: str, targetModel: str, containerOperator: str) -> str:
        # TODO: Implement createWorkflowInstance method
        pass

    def getMetatype(self) -> str:
        # TODO: Implement getMetatype method
        pass

    def replaceSubtype(self, oldModelTypeEndpoint: str, targetModelType: str, newModelTypeEndpointName: str):
        # TODO: Implement replaceSubtype method
        pass

    def getMIDContainer(self) -> str:
        # TODO: Implement getMIDContainer method
        pass

class mid_EMFInfo:

    def __init__(self, className: str, featureName: str, attribute: bool, relatedClassName: str, mid_EMFInfo: "mid_ModelElement" = None):
        self.className = className
        self.featureName = featureName
        self.attribute = attribute
        self.relatedClassName = relatedClassName
        self.mid_EMFInfo = mid_EMFInfo
        
    @property
    def attribute(self) -> bool:
        return self.__attribute

    @attribute.setter
    def attribute(self, attribute: bool):
        self.__attribute = attribute

    @property
    def relatedClassName(self) -> str:
        return self.__relatedClassName

    @relatedClassName.setter
    def relatedClassName(self, relatedClassName: str):
        self.__relatedClassName = relatedClassName

    @property
    def featureName(self) -> str:
        return self.__featureName

    @featureName.setter
    def featureName(self, featureName: str):
        self.__featureName = featureName

    @property
    def className(self) -> str:
        return self.__className

    @className.setter
    def className(self, className: str):
        self.__className = className

    @property
    def mid_EMFInfo(self):
        return self.__mid_EMFInfo

    @mid_EMFInfo.setter
    def mid_EMFInfo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mid_EMFInfo__mid_EMFInfo", None)
        self.__mid_EMFInfo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mid_ModelElement26"):
                opp_val = getattr(old_value, "mid_ModelElement26", None)
                if opp_val == self:
                    setattr(old_value, "mid_ModelElement26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mid_ModelElement26"):
                opp_val = getattr(value, "mid_ModelElement26", None)
                setattr(value, "mid_ModelElement26", self)

    def toInstanceString(self) -> str:
        # TODO: Implement toInstanceString method
        pass

    def toTypeString(self) -> str:
        # TODO: Implement toTypeString method
        pass

class mid_EObject:

    pass
class ConversionOperator:

    pass
class GenericElement:

    pass
class mid_operator_Operator(GenericElement):

    def __init__(self, workingPath: str, executionTime: str, commutative: bool, mid_operator_Operator: set["operator_mid_ModelEndpoint"] = None, mid_operator_Operator62: set["operator_mid_ModelEndpoint"] = None, mid_operator_Operator65: set["GenericEndpoint"] = None):
        self.workingPath = workingPath
        self.executionTime = executionTime
        self.commutative = commutative
        self.mid_operator_Operator = mid_operator_Operator if mid_operator_Operator is not None else set()
        self.mid_operator_Operator62 = mid_operator_Operator62 if mid_operator_Operator62 is not None else set()
        self.mid_operator_Operator65 = mid_operator_Operator65 if mid_operator_Operator65 is not None else set()
        
    @property
    def workingPath(self) -> str:
        return self.__workingPath

    @workingPath.setter
    def workingPath(self, workingPath: str):
        self.__workingPath = workingPath

    @property
    def executionTime(self) -> str:
        return self.__executionTime

    @executionTime.setter
    def executionTime(self, executionTime: str):
        self.__executionTime = executionTime

    @property
    def commutative(self) -> bool:
        return self.__commutative

    @commutative.setter
    def commutative(self, commutative: bool):
        self.__commutative = commutative

    @property
    def mid_operator_Operator65(self):
        return self.__mid_operator_Operator65

    @mid_operator_Operator65.setter
    def mid_operator_Operator65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mid_operator_Operator__mid_operator_Operator65", None)
        self.__mid_operator_Operator65 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GenericEndpoint"):
                    opp_val = getattr(item, "GenericEndpoint", None)
                    
                    if opp_val == self:
                        setattr(item, "GenericEndpoint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GenericEndpoint"):
                    opp_val = getattr(item, "GenericEndpoint", None)
                    
                    setattr(item, "GenericEndpoint", self)
                    

    @property
    def mid_operator_Operator(self):
        return self.__mid_operator_Operator

    @mid_operator_Operator.setter
    def mid_operator_Operator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mid_operator_Operator__mid_operator_Operator", None)
        self.__mid_operator_Operator = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "operator_mid_ModelEndpoint"):
                    opp_val = getattr(item, "operator_mid_ModelEndpoint", None)
                    
                    if opp_val == self:
                        setattr(item, "operator_mid_ModelEndpoint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "operator_mid_ModelEndpoint"):
                    opp_val = getattr(item, "operator_mid_ModelEndpoint", None)
                    
                    setattr(item, "operator_mid_ModelEndpoint", self)
                    

    @property
    def mid_operator_Operator62(self):
        return self.__mid_operator_Operator62

    @mid_operator_Operator62.setter
    def mid_operator_Operator62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mid_operator_Operator__mid_operator_Operator62", None)
        self.__mid_operator_Operator62 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "operator_mid_ModelEndpoint63"):
                    opp_val = getattr(item, "operator_mid_ModelEndpoint63", None)
                    
                    if opp_val == self:
                        setattr(item, "operator_mid_ModelEndpoint63", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "operator_mid_ModelEndpoint63"):
                    opp_val = getattr(item, "operator_mid_ModelEndpoint63", None)
                    
                    setattr(item, "operator_mid_ModelEndpoint63", self)
                    

    def createWorkflowInstance(self, workflowMID: str) -> str:
        # TODO: Implement createWorkflowInstance method
        pass

    def findFirstAllowedInput(self, inputModelBlacklists: str, inputMIDs: str) -> str:
        # TODO: Implement findFirstAllowedInput method
        pass

    def getOutputModels(self) -> Model:
        # TODO: Implement getOutputModels method
        pass

    def createInstance(self, instanceMID: str) -> str:
        # TODO: Implement createInstance method
        pass

    def getOutputsByName(self):
        # TODO: Implement getOutputsByName method
        pass

    def getMetatype(self) -> str:
        # TODO: Implement getMetatype method
        pass

    def run(self, inputsByName: str, genericsByName: str, outputMIDsByName: str):
        # TODO: Implement run method
        pass

    def openWorkflowInstance(self):
        # TODO: Implement openWorkflowInstance method
        pass

    def getTypeSignature(self, inputs: str) -> str:
        # TODO: Implement getTypeSignature method
        pass

    def startWorkflowInstance(self, generics: str, workflowMID: str, inputs: str) -> str:
        # TODO: Implement startWorkflowInstance method
        pass

    def readInputProperties(self, inputProperties: str):
        # TODO: Implement readInputProperties method
        pass

    def openType(self):
        # TODO: Implement openType method
        pass

    def selectAllowedGenerics(self, inputs: str) -> str:
        # TODO: Implement selectAllowedGenerics method
        pass

    def deleteWorkflowInstance(self):
        # TODO: Implement deleteWorkflowInstance method
        pass

    def findAllowedInputs(self, inputMIDs: str, inputModelBlacklists: str):
        # TODO: Implement findAllowedInputs method
        pass

    def deleteType(self):
        # TODO: Implement deleteType method
        pass

    def getSupertype(self) -> str:
        # TODO: Implement getSupertype method
        pass

    def checkAllowedInputs(self, inputModels: Model) -> str:
        # TODO: Implement checkAllowedInputs method
        pass

    def openInstance(self):
        # TODO: Implement openInstance method
        pass

    def getMIDContainer(self) -> str:
        # TODO: Implement getMIDContainer method
        pass

    def createWorkflowInstanceOutputs(self, workflowMID: str, newOperator: str, inputsByName: str):
        # TODO: Implement createWorkflowInstanceOutputs method
        pass

    def startInstance(self, outputMIDsByName: str, generics: str, inputProperties: str, instanceMID: str, inputs: str) -> str:
        # TODO: Implement startInstance method
        pass

    def createSubtype(self, newOperatorTypeName: str, implementationPath: str) -> str:
        # TODO: Implement createSubtype method
        pass

    def deleteInstance(self):
        # TODO: Implement deleteInstance method
        pass

    def getInputProperties(self) -> str:
        # TODO: Implement getInputProperties method
        pass

class ExtendibleElement:

    pass
class mid_relationship_Mapping(ExtendibleElement):

    def __init__(self, mid_relationship_Mapping: set["ModelElementEndpoint"] = None, mid_relationship_Mapping48: set["ModelElementEndpointReference"] = None):
        self.mid_relationship_Mapping = mid_relationship_Mapping if mid_relationship_Mapping is not None else set()
        self.mid_relationship_Mapping48 = mid_relationship_Mapping48 if mid_relationship_Mapping48 is not None else set()
        
    @property
    def mid_relationship_Mapping(self):
        return self.__mid_relationship_Mapping

    @mid_relationship_Mapping.setter
    def mid_relationship_Mapping(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mid_relationship_Mapping__mid_relationship_Mapping", None)
        self.__mid_relationship_Mapping = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ModelElementEndpoint"):
                    opp_val = getattr(item, "ModelElementEndpoint", None)
                    
                    if opp_val == self:
                        setattr(item, "ModelElementEndpoint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ModelElementEndpoint"):
                    opp_val = getattr(item, "ModelElementEndpoint", None)
                    
                    setattr(item, "ModelElementEndpoint", self)
                    

    @property
    def mid_relationship_Mapping48(self):
        return self.__mid_relationship_Mapping48

    @mid_relationship_Mapping48.setter
    def mid_relationship_Mapping48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mid_relationship_Mapping__mid_relationship_Mapping48", None)
        self.__mid_relationship_Mapping48 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ModelElementEndpointReference49"):
                    opp_val = getattr(item, "ModelElementEndpointReference49", None)
                    
                    if opp_val == self:
                        setattr(item, "ModelElementEndpointReference49", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ModelElementEndpointReference49"):
                    opp_val = getattr(item, "ModelElementEndpointReference49", None)
                    
                    setattr(item, "ModelElementEndpointReference49", self)
                    

    def deleteType(self):
        # TODO: Implement deleteType method
        pass

    def getMetatype(self) -> str:
        # TODO: Implement getMetatype method
        pass

    def deleteInstance(self):
        # TODO: Implement deleteInstance method
        pass

    def createInstanceAndReferenceAndEndpointsAndReferences(self, isBinary: bool, targetModelElemRefs: str) -> str:
        # TODO: Implement createInstanceAndReferenceAndEndpointsAndReferences method
        pass

    def createTypeReference(self, isModifiable: bool, mappingTypeRef: str, containerModelRelType: str) -> str:
        # TODO: Implement createTypeReference method
        pass

    def getMIDContainer(self) -> str:
        # TODO: Implement getMIDContainer method
        pass

    def createInstanceReference(self, containerModelRel: str) -> str:
        # TODO: Implement createInstanceReference method
        pass

    def getSupertype(self) -> str:
        # TODO: Implement getSupertype method
        pass

    def createInstanceAndReference(self, isBinary: bool, containerModelRel: str) -> str:
        # TODO: Implement createInstanceAndReference method
        pass

    def createSubtypeAndReference(self, newMappingTypeName: str, isBinary: bool, mappingTypeRef: str, containerModelRelType: str) -> str:
        # TODO: Implement createSubtypeAndReference method
        pass

class mid_editor_Editor(ExtendibleElement):

    def __init__(self, modelUri: str, id: str, wizardId: str, fileExtensions: str, wizardDialogClass: str):
        self.modelUri = modelUri
        self.id = id
        self.wizardId = wizardId
        self.fileExtensions = fileExtensions
        self.wizardDialogClass = wizardDialogClass
        
    @property
    def fileExtensions(self) -> str:
        return self.__fileExtensions

    @fileExtensions.setter
    def fileExtensions(self, fileExtensions: str):
        self.__fileExtensions = fileExtensions

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def wizardDialogClass(self) -> str:
        return self.__wizardDialogClass

    @wizardDialogClass.setter
    def wizardDialogClass(self, wizardDialogClass: str):
        self.__wizardDialogClass = wizardDialogClass

    @property
    def modelUri(self) -> str:
        return self.__modelUri

    @modelUri.setter
    def modelUri(self, modelUri: str):
        self.__modelUri = modelUri

    @property
    def wizardId(self) -> str:
        return self.__wizardId

    @wizardId.setter
    def wizardId(self, wizardId: str):
        self.__wizardId = wizardId

    def deleteInstance(self):
        # TODO: Implement deleteInstance method
        pass

    def createInstance(self, instanceMID: str, createEditorFile: bool, modelPath: str) -> str:
        # TODO: Implement createInstance method
        pass

    def invokeInstanceWizard(self, initialSelection: str) -> str:
        # TODO: Implement invokeInstanceWizard method
        pass

    def getMetatype(self) -> str:
        # TODO: Implement getMetatype method
        pass

    def createSubtype(self, modelTypeUri: str, newEditorTypeFragmentUri: str, newEditorTypeName: str, wizardDialogClassName: str, wizardId: str, editorId: str) -> str:
        # TODO: Implement createSubtype method
        pass

    def getMIDContainer(self) -> str:
        # TODO: Implement getMIDContainer method
        pass

    def getSupertype(self) -> str:
        # TODO: Implement getSupertype method
        pass

    def deleteType(self):
        # TODO: Implement deleteType method
        pass

class mid_GenericElement(ExtendibleElement):

    def __init__(self, abstract: bool):
        self.abstract = abstract
        
    @property
    def abstract(self) -> bool:
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: bool):
        self.__abstract = abstract

class mid_ModelElement(ExtendibleElement):

    def __init__(self, mid_ModelElement: "mid_Model" = None, mid_ModelElement26: "mid_EMFInfo" = None):
        self.mid_ModelElement = mid_ModelElement
        self.mid_ModelElement26 = mid_ModelElement26
        
    @property
    def mid_ModelElement26(self):
        return self.__mid_ModelElement26

    @mid_ModelElement26.setter
    def mid_ModelElement26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mid_ModelElement__mid_ModelElement26", None)
        self.__mid_ModelElement26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mid_EMFInfo"):
                opp_val = getattr(old_value, "mid_EMFInfo", None)
                if opp_val == self:
                    setattr(old_value, "mid_EMFInfo", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mid_EMFInfo"):
                opp_val = getattr(value, "mid_EMFInfo", None)
                setattr(value, "mid_EMFInfo", self)

    @property
    def mid_ModelElement(self):
        return self.__mid_ModelElement

    @mid_ModelElement.setter
    def mid_ModelElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mid_ModelElement__mid_ModelElement", None)
        self.__mid_ModelElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mid_Model20"):
                opp_val = getattr(old_value, "mid_Model20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mid_Model20"):
                opp_val = getattr(value, "mid_Model20", None)
                if opp_val is None:
                    setattr(value, "mid_Model20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def getMetatype(self) -> str:
        # TODO: Implement getMetatype method
        pass

    def createTypeReference(self, isModifiable: bool, modelElemTypeRef: str, containerModelTypeEndpointRef: str) -> str:
        # TODO: Implement createTypeReference method
        pass

    def getEMFInstanceObject(self, emfResource: str) -> str:
        # TODO: Implement getEMFInstanceObject method
        pass

    def deleteInstance(self):
        # TODO: Implement deleteInstance method
        pass

    def createInstanceAndReference(self, newModelElemName: str, newModelElemUri: str, containerModelEndpointRef: str, eInfo: str) -> str:
        # TODO: Implement createInstanceAndReference method
        pass

    def getSupertype(self) -> str:
        # TODO: Implement getSupertype method
        pass

    def getEMFTypeObject(self) -> str:
        # TODO: Implement getEMFTypeObject method
        pass

    def getMIDContainer(self) -> str:
        # TODO: Implement getMIDContainer method
        pass

    def createInstanceReference(self, containerModelEndpointRef: str) -> str:
        # TODO: Implement createInstanceReference method
        pass

    def deleteType(self):
        # TODO: Implement deleteType method
        pass

    def createSubtypeAndReference(self, containerModelTypeEndpointRef: str, eInfo: str, modelElemTypeRef: str, newModelElemTypeUri: str, newModelElemTypeName: str) -> str:
        # TODO: Implement createSubtypeAndReference method
        pass

class mid_ExtendibleElementEndpoint(ExtendibleElement):

    def __init__(self, lowerBound: int, upperBound: int, mid_ExtendibleElementEndpoint: "mid_ExtendibleElement" = None):
        self.lowerBound = lowerBound
        self.upperBound = upperBound
        self.mid_ExtendibleElementEndpoint = mid_ExtendibleElementEndpoint
        
    @property
    def upperBound(self) -> int:
        return self.__upperBound

    @upperBound.setter
    def upperBound(self, upperBound: int):
        self.__upperBound = upperBound

    @property
    def lowerBound(self) -> int:
        return self.__lowerBound

    @lowerBound.setter
    def lowerBound(self, lowerBound: int):
        self.__lowerBound = lowerBound

    @property
    def mid_ExtendibleElementEndpoint(self):
        return self.__mid_ExtendibleElementEndpoint

    @mid_ExtendibleElementEndpoint.setter
    def mid_ExtendibleElementEndpoint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mid_ExtendibleElementEndpoint__mid_ExtendibleElementEndpoint", None)
        self.__mid_ExtendibleElementEndpoint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mid_ExtendibleElement15"):
                opp_val = getattr(old_value, "mid_ExtendibleElement15", None)
                if opp_val == self:
                    setattr(old_value, "mid_ExtendibleElement15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mid_ExtendibleElement15"):
                opp_val = getattr(value, "mid_ExtendibleElement15", None)
                setattr(value, "mid_ExtendibleElement15", self)

    def getMetatype(self) -> str:
        # TODO: Implement getMetatype method
        pass

    def getSupertype(self) -> str:
        # TODO: Implement getSupertype method
        pass

    def getTargetUri(self) -> str:
        # TODO: Implement getTargetUri method
        pass

class mid_ExtendibleElementConstraint:

    def __init__(self, implementation: str, language: str, mid_ExtendibleElementConstraint: "mid_ExtendibleElement" = None):
        self.implementation = implementation
        self.language = language
        self.mid_ExtendibleElementConstraint = mid_ExtendibleElementConstraint
        
    @property
    def language(self) -> str:
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language

    @property
    def implementation(self) -> str:
        return self.__implementation

    @implementation.setter
    def implementation(self, implementation: str):
        self.__implementation = implementation

    @property
    def mid_ExtendibleElementConstraint(self):
        return self.__mid_ExtendibleElementConstraint

    @mid_ExtendibleElementConstraint.setter
    def mid_ExtendibleElementConstraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mid_ExtendibleElementConstraint__mid_ExtendibleElementConstraint", None)
        self.__mid_ExtendibleElementConstraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mid_ExtendibleElement13"):
                opp_val = getattr(old_value, "mid_ExtendibleElement13", None)
                if opp_val == self:
                    setattr(old_value, "mid_ExtendibleElement13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mid_ExtendibleElement13"):
                opp_val = getattr(value, "mid_ExtendibleElement13", None)
                setattr(value, "mid_ExtendibleElement13", self)

class Operator:

    pass
class mid_operator_RandomOperator(Operator):

    def __init__(self, state: str, Operator: "mid_MID"):
        self.state = state
        
    @property
    def state(self) -> str:
        return self.__state

    @state.setter
    def state(self, state: str):
        self.__state = state

class mid_operator_NestingOperator(Operator):

    def __init__(self, nestedMIDPath: str, Operator: "mid_MID"):
        self.nestedMIDPath = nestedMIDPath
        
    @property
    def nestedMIDPath(self) -> str:
        return self.__nestedMIDPath

    @nestedMIDPath.setter
    def nestedMIDPath(self, nestedMIDPath: str):
        self.__nestedMIDPath = nestedMIDPath

    def startNestedInstance(self, outputMIDsByName: str, nestedOperatorType: str, inputs: str, inputProperties: str, generics: str) -> str:
        # TODO: Implement startNestedInstance method
        pass

    def getNestedInstanceMID(self) -> str:
        # TODO: Implement getNestedInstanceMID method
        pass

class mid_operator_ConversionOperator(Operator):

    def __init__(self, Operator: "mid_MID"):
        
    def deleteType(self):
        # TODO: Implement deleteType method
        pass

    def cleanup(self):
        # TODO: Implement cleanup method
        pass

class Editor:

    pass
class mid_editor_Diagram(Editor):

    pass
class mid_ExtendibleElement(ABC):

    def __init__(self, name: str, level: str, metatypeUri: str, dynamic: bool, uri: str, mid_ExtendibleElement: "mid_EStringToExtendibleElementMap" = None, mid_ExtendibleElement13: "mid_ExtendibleElementConstraint" = None, mid_ExtendibleElement11: "mid_ExtendibleElement" = None, mid_ExtendibleElement9: "mid_ExtendibleElement" = None, mid_ExtendibleElement15: "mid_ExtendibleElementEndpoint" = None):
        self.name = name
        self.level = level
        self.metatypeUri = metatypeUri
        self.dynamic = dynamic
        self.uri = uri
        self.mid_ExtendibleElement = mid_ExtendibleElement
        self.mid_ExtendibleElement13 = mid_ExtendibleElement13
        self.mid_ExtendibleElement11 = mid_ExtendibleElement11
        self.mid_ExtendibleElement9 = mid_ExtendibleElement9
        self.mid_ExtendibleElement15 = mid_ExtendibleElement15
        
    @property
    def uri(self) -> str:
        return self.__uri

    @uri.setter
    def uri(self, uri: str):
        self.__uri = uri

    @property
    def metatypeUri(self) -> str:
        return self.__metatypeUri

    @metatypeUri.setter
    def metatypeUri(self, metatypeUri: str):
        self.__metatypeUri = metatypeUri

    @property
    def level(self) -> str:
        return self.__level

    @level.setter
    def level(self, level: str):
        self.__level = level

    @property
    def dynamic(self) -> bool:
        return self.__dynamic

    @dynamic.setter
    def dynamic(self, dynamic: bool):
        self.__dynamic = dynamic

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mid_ExtendibleElement13(self):
        return self.__mid_ExtendibleElement13

    @mid_ExtendibleElement13.setter
    def mid_ExtendibleElement13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mid_ExtendibleElement__mid_ExtendibleElement13", None)
        self.__mid_ExtendibleElement13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mid_ExtendibleElementConstraint"):
                opp_val = getattr(old_value, "mid_ExtendibleElementConstraint", None)
                if opp_val == self:
                    setattr(old_value, "mid_ExtendibleElementConstraint", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mid_ExtendibleElementConstraint"):
                opp_val = getattr(value, "mid_ExtendibleElementConstraint", None)
                setattr(value, "mid_ExtendibleElementConstraint", self)

    @property
    def mid_ExtendibleElement9(self):
        return self.__mid_ExtendibleElement9

    @mid_ExtendibleElement9.setter
    def mid_ExtendibleElement9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mid_ExtendibleElement__mid_ExtendibleElement9", None)
        self.__mid_ExtendibleElement9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mid_ExtendibleElement11"):
                opp_val = getattr(old_value, "mid_ExtendibleElement11", None)
                if opp_val == self:
                    setattr(old_value, "mid_ExtendibleElement11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mid_ExtendibleElement11"):
                opp_val = getattr(value, "mid_ExtendibleElement11", None)
                setattr(value, "mid_ExtendibleElement11", self)

    @property
    def mid_ExtendibleElement(self):
        return self.__mid_ExtendibleElement

    @mid_ExtendibleElement.setter
    def mid_ExtendibleElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mid_ExtendibleElement__mid_ExtendibleElement", None)
        self.__mid_ExtendibleElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mid_EStringToExtendibleElementMap8"):
                opp_val = getattr(old_value, "mid_EStringToExtendibleElementMap8", None)
                if opp_val == self:
                    setattr(old_value, "mid_EStringToExtendibleElementMap8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mid_EStringToExtendibleElementMap8"):
                opp_val = getattr(value, "mid_EStringToExtendibleElementMap8", None)
                setattr(value, "mid_EStringToExtendibleElementMap8", self)

    @property
    def mid_ExtendibleElement15(self):
        return self.__mid_ExtendibleElement15

    @mid_ExtendibleElement15.setter
    def mid_ExtendibleElement15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mid_ExtendibleElement__mid_ExtendibleElement15", None)
        self.__mid_ExtendibleElement15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mid_ExtendibleElementEndpoint"):
                opp_val = getattr(old_value, "mid_ExtendibleElementEndpoint", None)
                if opp_val == self:
                    setattr(old_value, "mid_ExtendibleElementEndpoint", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mid_ExtendibleElementEndpoint"):
                opp_val = getattr(value, "mid_ExtendibleElementEndpoint", None)
                setattr(value, "mid_ExtendibleElementEndpoint", self)

    @property
    def mid_ExtendibleElement11(self):
        return self.__mid_ExtendibleElement11

    @mid_ExtendibleElement11.setter
    def mid_ExtendibleElement11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mid_ExtendibleElement__mid_ExtendibleElement11", None)
        self.__mid_ExtendibleElement11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mid_ExtendibleElement9"):
                opp_val = getattr(old_value, "mid_ExtendibleElement9", None)
                if opp_val == self:
                    setattr(old_value, "mid_ExtendibleElement9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mid_ExtendibleElement9"):
                opp_val = getattr(value, "mid_ExtendibleElement9", None)
                setattr(value, "mid_ExtendibleElement9", self)

    def validateInstanceInEditor(self, context: str) -> str:
        # TODO: Implement validateInstanceInEditor method
        pass

    def isWorkflowsLevel(self) -> bool:
        # TODO: Implement isWorkflowsLevel method
        pass

    def toMIDCustomPrintLabel(self) -> str:
        # TODO: Implement toMIDCustomPrintLabel method
        pass

    def getClosestTypeConstraint(self) -> str:
        # TODO: Implement getClosestTypeConstraint method
        pass

    def addTypeConstraint(self, implementation: str, language: str):
        # TODO: Implement addTypeConstraint method
        pass

    def createSubtypeUri(self, newTypeName: str, newTypeFragmentUri: str) -> str:
        # TODO: Implement createSubtypeUri method
        pass

    def getMetatype(self) -> str:
        # TODO: Implement getMetatype method
        pass

    def isInstancesLevel(self) -> bool:
        # TODO: Implement isInstancesLevel method
        pass

    def getRuntimeTypes(self):
        # TODO: Implement getRuntimeTypes method
        pass

    def validateInstanceType(self, type: str) -> bool:
        # TODO: Implement validateInstanceType method
        pass

    def isLevel(self, midLevel: str) -> bool:
        # TODO: Implement isLevel method
        pass

    def validateInstance(self) -> bool:
        # TODO: Implement validateInstance method
        pass

    def isTypesLevel(self) -> bool:
        # TODO: Implement isTypesLevel method
        pass

    def toMIDCustomEditLabel(self) -> str:
        # TODO: Implement toMIDCustomEditLabel method
        pass

    def updateWorkflowInstanceId(self, newInstanceId: str):
        # TODO: Implement updateWorkflowInstanceId method
        pass

    def updateMIDCustomLabel(self, newLabel: str):
        # TODO: Implement updateMIDCustomLabel method
        pass

    def getMIDContainer(self) -> str:
        # TODO: Implement getMIDContainer method
        pass

class mid_EStringToExtendibleElementMap:

    def __init__(self, key: str, mid_EStringToExtendibleElementMap: "mid_MID" = None, mid_EStringToExtendibleElementMap8: "mid_ExtendibleElement" = None):
        self.key = key
        self.mid_EStringToExtendibleElementMap = mid_EStringToExtendibleElementMap
        self.mid_EStringToExtendibleElementMap8 = mid_EStringToExtendibleElementMap8
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def mid_EStringToExtendibleElementMap8(self):
        return self.__mid_EStringToExtendibleElementMap8

    @mid_EStringToExtendibleElementMap8.setter
    def mid_EStringToExtendibleElementMap8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mid_EStringToExtendibleElementMap__mid_EStringToExtendibleElementMap8", None)
        self.__mid_EStringToExtendibleElementMap8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mid_ExtendibleElement"):
                opp_val = getattr(old_value, "mid_ExtendibleElement", None)
                if opp_val == self:
                    setattr(old_value, "mid_ExtendibleElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mid_ExtendibleElement"):
                opp_val = getattr(value, "mid_ExtendibleElement", None)
                setattr(value, "mid_ExtendibleElement", self)

    @property
    def mid_EStringToExtendibleElementMap(self):
        return self.__mid_EStringToExtendibleElementMap

    @mid_EStringToExtendibleElementMap.setter
    def mid_EStringToExtendibleElementMap(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mid_EStringToExtendibleElementMap__mid_EStringToExtendibleElementMap", None)
        self.__mid_EStringToExtendibleElementMap = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mid_MID6"):
                opp_val = getattr(old_value, "mid_MID6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mid_MID6"):
                opp_val = getattr(value, "mid_MID6", None)
                if opp_val is None:
                    setattr(value, "mid_MID6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class mid_Model(GenericElement):

    def __init__(self, origin: str, fileExtension: str, mid_Model: "mid_MID" = None, mid_Model17: set["Editor"] = None, mid_Model20: set["mid_ModelElement"] = None, mid_Model22: set["ConversionOperator"] = None, mid_Model24: "mid_EObject" = None):
        self.origin = origin
        self.fileExtension = fileExtension
        self.mid_Model = mid_Model
        self.mid_Model17 = mid_Model17 if mid_Model17 is not None else set()
        self.mid_Model20 = mid_Model20 if mid_Model20 is not None else set()
        self.mid_Model22 = mid_Model22 if mid_Model22 is not None else set()
        self.mid_Model24 = mid_Model24
        
    @property
    def fileExtension(self) -> str:
        return self.__fileExtension

    @fileExtension.setter
    def fileExtension(self, fileExtension: str):
        self.__fileExtension = fileExtension

    @property
    def origin(self) -> str:
        return self.__origin

    @origin.setter
    def origin(self, origin: str):
        self.__origin = origin

    @property
    def mid_Model24(self):
        return self.__mid_Model24

    @mid_Model24.setter
    def mid_Model24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mid_Model__mid_Model24", None)
        self.__mid_Model24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mid_EObject"):
                opp_val = getattr(old_value, "mid_EObject", None)
                if opp_val == self:
                    setattr(old_value, "mid_EObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mid_EObject"):
                opp_val = getattr(value, "mid_EObject", None)
                setattr(value, "mid_EObject", self)

    @property
    def mid_Model17(self):
        return self.__mid_Model17

    @mid_Model17.setter
    def mid_Model17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mid_Model__mid_Model17", None)
        self.__mid_Model17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Editor18"):
                    opp_val = getattr(item, "Editor18", None)
                    
                    if opp_val == self:
                        setattr(item, "Editor18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Editor18"):
                    opp_val = getattr(item, "Editor18", None)
                    
                    setattr(item, "Editor18", self)
                    

    @property
    def mid_Model22(self):
        return self.__mid_Model22

    @mid_Model22.setter
    def mid_Model22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mid_Model__mid_Model22", None)
        self.__mid_Model22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ConversionOperator"):
                    opp_val = getattr(item, "ConversionOperator", None)
                    
                    if opp_val == self:
                        setattr(item, "ConversionOperator", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ConversionOperator"):
                    opp_val = getattr(item, "ConversionOperator", None)
                    
                    setattr(item, "ConversionOperator", self)
                    

    @property
    def mid_Model(self):
        return self.__mid_Model

    @mid_Model.setter
    def mid_Model(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mid_Model__mid_Model", None)
        self.__mid_Model = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mid_MID"):
                opp_val = getattr(old_value, "mid_MID", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mid_MID"):
                opp_val = getattr(value, "mid_MID", None)
                if opp_val is None:
                    setattr(value, "mid_MID", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mid_Model20(self):
        return self.__mid_Model20

    @mid_Model20.setter
    def mid_Model20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mid_Model__mid_Model20", None)
        self.__mid_Model20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mid_ModelElement"):
                    opp_val = getattr(item, "mid_ModelElement", None)
                    
                    if opp_val == self:
                        setattr(item, "mid_ModelElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mid_ModelElement"):
                    opp_val = getattr(item, "mid_ModelElement", None)
                    
                    setattr(item, "mid_ModelElement", self)
                    

    def deleteType(self):
        # TODO: Implement deleteType method
        pass

    def getMetatype(self) -> str:
        # TODO: Implement getMetatype method
        pass

    def createInstanceAndEditor(self, newModelPath: str, rootModelObj: str, instanceMID: str) -> str:
        # TODO: Implement createInstanceAndEditor method
        pass

    def importInstance(self, modelPath: str, instanceMID: str) -> str:
        # TODO: Implement importInstance method
        pass

    def createInstance(self, rootModelObj: str, instanceMID: str, newModelPath: str) -> str:
        # TODO: Implement createInstance method
        pass

    def importInstanceAndEditor(self, modelPath: str, instanceMID: str) -> str:
        # TODO: Implement importInstanceAndEditor method
        pass

    def openInstance(self):
        # TODO: Implement openInstance method
        pass

    def getMIDContainer(self) -> str:
        # TODO: Implement getMIDContainer method
        pass

    def deleteInstanceAndFile(self):
        # TODO: Implement deleteInstanceAndFile method
        pass

    def deleteWorkflowInstance(self):
        # TODO: Implement deleteWorkflowInstance method
        pass

    def getEMFTypeRoot(self) -> str:
        # TODO: Implement getEMFTypeRoot method
        pass

    def openType(self):
        # TODO: Implement openType method
        pass

    def createSubtype(self, isMetamodelExtension: bool, newModelTypeName: str) -> str:
        # TODO: Implement createSubtype method
        pass

    def copyInstance(self, origModel: str, newModelName: str, instanceMID: str) -> str:
        # TODO: Implement copyInstance method
        pass

    def createWorkflowInstance(self, newModelId: str, workflowMID: str) -> str:
        # TODO: Implement createWorkflowInstance method
        pass

    def copyInstanceAndEditor(self, newModelName: str, copyDiagram: bool, origModel: str, instanceMID: str) -> str:
        # TODO: Implement copyInstanceAndEditor method
        pass

    def getSupertype(self) -> str:
        # TODO: Implement getSupertype method
        pass

    def deleteInstance(self):
        # TODO: Implement deleteInstance method
        pass

    def createInstanceEditor(self, createEditorFile: bool) -> str:
        # TODO: Implement createInstanceEditor method
        pass

class mid_MID:

    def __init__(self, level: str, mid_MID: set["mid_Model"] = None, mid_MID6: set["mid_EStringToExtendibleElementMap"] = None, mid_MID2: set["Editor"] = None, mid_MID4: set["Operator"] = None):
        self.level = level
        self.mid_MID = mid_MID if mid_MID is not None else set()
        self.mid_MID6 = mid_MID6 if mid_MID6 is not None else set()
        self.mid_MID2 = mid_MID2 if mid_MID2 is not None else set()
        self.mid_MID4 = mid_MID4 if mid_MID4 is not None else set()
        
    @property
    def level(self) -> str:
        return self.__level

    @level.setter
    def level(self, level: str):
        self.__level = level

    @property
    def mid_MID4(self):
        return self.__mid_MID4

    @mid_MID4.setter
    def mid_MID4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mid_MID__mid_MID4", None)
        self.__mid_MID4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Operator"):
                    opp_val = getattr(item, "Operator", None)
                    
                    if opp_val == self:
                        setattr(item, "Operator", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Operator"):
                    opp_val = getattr(item, "Operator", None)
                    
                    setattr(item, "Operator", self)
                    

    @property
    def mid_MID(self):
        return self.__mid_MID

    @mid_MID.setter
    def mid_MID(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mid_MID__mid_MID", None)
        self.__mid_MID = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mid_Model"):
                    opp_val = getattr(item, "mid_Model", None)
                    
                    if opp_val == self:
                        setattr(item, "mid_Model", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mid_Model"):
                    opp_val = getattr(item, "mid_Model", None)
                    
                    setattr(item, "mid_Model", self)
                    

    @property
    def mid_MID2(self):
        return self.__mid_MID2

    @mid_MID2.setter
    def mid_MID2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mid_MID__mid_MID2", None)
        self.__mid_MID2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Editor"):
                    opp_val = getattr(item, "Editor", None)
                    
                    if opp_val == self:
                        setattr(item, "Editor", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Editor"):
                    opp_val = getattr(item, "Editor", None)
                    
                    setattr(item, "Editor", self)
                    

    @property
    def mid_MID6(self):
        return self.__mid_MID6

    @mid_MID6.setter
    def mid_MID6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mid_MID__mid_MID6", None)
        self.__mid_MID6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mid_EStringToExtendibleElementMap"):
                    opp_val = getattr(item, "mid_EStringToExtendibleElementMap", None)
                    
                    if opp_val == self:
                        setattr(item, "mid_EStringToExtendibleElementMap", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mid_EStringToExtendibleElementMap"):
                    opp_val = getattr(item, "mid_EStringToExtendibleElementMap", None)
                    
                    setattr(item, "mid_EStringToExtendibleElementMap", self)
                    

    def isInstancesLevel(self) -> bool:
        # TODO: Implement isInstancesLevel method
        pass

    def isWorkflowsLevel(self) -> bool:
        # TODO: Implement isWorkflowsLevel method
        pass

    def isTypesLevel(self) -> bool:
        # TODO: Implement isTypesLevel method
        pass

    def getExtendibleElement(self, uri: str):
        # TODO: Implement getExtendibleElement method
        pass

    def getModelRels(self) -> str:
        # TODO: Implement getModelRels method
        pass
