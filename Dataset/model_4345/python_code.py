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

class mid_operator_OperatorConstraintParameter:

    def __init__(self, endpointIndex: int, mid_operator_OperatorConstraintParameter: "ModelEndpointReference" = None):
        self.endpointIndex = endpointIndex
        self.mid_operator_OperatorConstraintParameter = mid_operator_OperatorConstraintParameter
        
        pass
    @property
    def endpointIndex(self):
        return self.__endpointIndex

    @endpointIndex.setter
    def endpointIndex(self, endpointIndex: int):
        self.__endpointIndex = endpointIndex


    @property
    def mid_operator_OperatorConstraintParameter(self):
        return self.__mid_operator_OperatorConstraintParameter

    @mid_operator_OperatorConstraintParameter.setter
    def mid_operator_OperatorConstraintParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mid_operator_OperatorConstraintParameter__mid_operator_OperatorConstraintParameter", None)
        self.__mid_operator_OperatorConstraintParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ModelEndpointReference83"):
                opp_val = getattr(old_value, "ModelEndpointReference83", None)
                if opp_val == self:
                    setattr(old_value, "ModelEndpointReference83", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ModelEndpointReference83"):
                opp_val = getattr(value, "ModelEndpointReference83", None)
                setattr(value, "ModelEndpointReference83", self)

class OperatorConstraintParameter:

    pass
class mid_operator_OperatorConstraintRule:

    pass
class OperatorConstraintRule:

    pass
class ExtendibleElementConstraint:

    pass
class mid_operator_OperatorConstraint(ExtendibleElementConstraint):

    pass
class operator_mid_GenericElement:

    pass
class mid_operator_OperatorGeneric:

    pass
class operator_mid_Model:

    pass
class mid_operator_OperatorInput:

    pass
class GenericEndpoint:

    pass
class operator_mid_ModelEndpoint:

    pass
class ModelElementEndpoint:

    pass
class ModelElementEndpointReference:

    pass
class ModelElementReference:

    pass
class ExtendibleElementEndpointReference:

    pass
class mid_relationship_ModelElementEndpointReference(ExtendibleElementEndpointReference):

    def __init__(self, modelElemEndpointRefs: "ModelElementReference" = None):
        self.modelElemEndpointRefs = modelElemEndpointRefs
        
        pass
    @property
    def modelElemEndpointRefs(self):
        return self.__modelElemEndpointRefs

    @modelElemEndpointRefs.setter
    def modelElemEndpointRefs(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mid_relationship_ModelElementEndpointReference__modelElemEndpointRefs", None)
        self.__modelElemEndpointRefs = value
        
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

    def getSupertypeRef(self) :
        # TODO: Implement getSupertypeRef method
        pass

    def deleteTypeAndReference(self, mid_isFullDelete):
        # TODO: Implement deleteTypeAndReference method
        pass

    def deleteInstanceAndReference(self, mid_isFullDelete):
        # TODO: Implement deleteInstanceAndReference method
        pass

    def getObject(self) :
        # TODO: Implement getObject method
        pass

    def deleteTypeReference(self, mid_isFullDelete):
        # TODO: Implement deleteTypeReference method
        pass

class mid_relationship_ModelEndpointReference(ExtendibleElementEndpointReference):

    def __init__(self, mid_relationship_ModelEndpointReference: set["ModelElementReference"] = None):
        self.mid_relationship_ModelEndpointReference = mid_relationship_ModelEndpointReference if mid_relationship_ModelEndpointReference is not None else set()
        
        pass
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
                    

    def acceptModelElementType(self, mid_metamodelObj) :
        # TODO: Implement acceptModelElementType method
        pass

    def createModelElementInstanceAndReference(self, mid_modelObj, mid_newModelElemName) :
        # TODO: Implement createModelElementInstanceAndReference method
        pass

    def acceptModelElementInstance(self, mid_modelObj) :
        # TODO: Implement acceptModelElementInstance method
        pass

    def getSupertypeRef(self) :
        # TODO: Implement getSupertypeRef method
        pass

    def deleteTypeReference(self, mid_isFullDelete):
        # TODO: Implement deleteTypeReference method
        pass

    def getObject(self) :
        # TODO: Implement getObject method
        pass

class ExtendibleElementReference:

    pass
class mid_relationship_MappingReference(ExtendibleElementReference):

    def __init__(self, mid_relationship_MappingReference: set["ModelElementEndpointReference"] = None, ExtendibleElementReference: "mid_relationship_ExtendibleElementReference" = None):
        self.mid_relationship_MappingReference = mid_relationship_MappingReference if mid_relationship_MappingReference is not None else set()
        
        pass
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
                    

    def getSupertypeRef(self) :
        # TODO: Implement getSupertypeRef method
        pass

    def deleteTypeReference(self):
        # TODO: Implement deleteTypeReference method
        pass

    def deleteTypeAndReference(self):
        # TODO: Implement deleteTypeAndReference method
        pass

    def deleteInstanceAndReference(self):
        # TODO: Implement deleteInstanceAndReference method
        pass

    def deleteInstanceReference(self):
        # TODO: Implement deleteInstanceReference method
        pass

    def getObject(self) :
        # TODO: Implement getObject method
        pass

class mid_relationship_ExtendibleElementEndpointReference(ExtendibleElementReference):

    def __init__(self, ExtendibleElementReference: "mid_relationship_ExtendibleElementReference" = None):
        
        pass
    def getTargetUri(self) :
        # TODO: Implement getTargetUri method
        pass

    def getObject(self) :
        # TODO: Implement getObject method
        pass

    def getSupertypeRef(self) :
        # TODO: Implement getSupertypeRef method
        pass

class mid_relationship_ModelElementReference(ExtendibleElementReference):

    def __init__(self, modelElemRef: set["ModelElementEndpointReference"] = None, ExtendibleElementReference: "mid_relationship_ExtendibleElementReference" = None):
        self.modelElemRef = modelElemRef if modelElemRef is not None else set()
        
        pass
    @property
    def modelElemRef(self):
        return self.__modelElemRef

    @modelElemRef.setter
    def modelElemRef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mid_relationship_ModelElementReference__modelElemRef", None)
        self.__modelElemRef = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ModelElementEndpointReference"):
                    opp_val = getattr(item, "ModelElementEndpointReference", None)
                    
                    if opp_val == self:
                        setattr(item, "ModelElementEndpointReference", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ModelElementEndpointReference"):
                    opp_val = getattr(item, "ModelElementEndpointReference", None)
                    
                    setattr(item, "ModelElementEndpointReference", self)
                    

    def getSupertypeRef(self) :
        # TODO: Implement getSupertypeRef method
        pass

    def getObject(self) :
        # TODO: Implement getObject method
        pass

    def deleteTypeReference(self):
        # TODO: Implement deleteTypeReference method
        pass

    def deleteInstanceReference(self):
        # TODO: Implement deleteInstanceReference method
        pass

class relationship_mid_ExtendibleElement:

    pass
class mid_relationship_ExtendibleElementReference(ABC):

    def __init__(self, modifiable: bool, mid_relationship_ExtendibleElementReference: "relationship_mid_ExtendibleElement" = None, mid_relationship_ExtendibleElementReference38: "relationship_mid_ExtendibleElement" = None, mid_relationship_ExtendibleElementReference41: "ExtendibleElementReference" = None):
        self.modifiable = modifiable
        self.mid_relationship_ExtendibleElementReference = mid_relationship_ExtendibleElementReference
        self.mid_relationship_ExtendibleElementReference38 = mid_relationship_ExtendibleElementReference38
        self.mid_relationship_ExtendibleElementReference41 = mid_relationship_ExtendibleElementReference41
        
        pass
    @property
    def modifiable(self):
        return self.__modifiable

    @modifiable.setter
    def modifiable(self, modifiable: bool):
        self.__modifiable = modifiable


    @property
    def mid_relationship_ExtendibleElementReference41(self):
        return self.__mid_relationship_ExtendibleElementReference41

    @mid_relationship_ExtendibleElementReference41.setter
    def mid_relationship_ExtendibleElementReference41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mid_relationship_ExtendibleElementReference__mid_relationship_ExtendibleElementReference41", None)
        self.__mid_relationship_ExtendibleElementReference41 = value
        
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

    @property
    def mid_relationship_ExtendibleElementReference38(self):
        return self.__mid_relationship_ExtendibleElementReference38

    @mid_relationship_ExtendibleElementReference38.setter
    def mid_relationship_ExtendibleElementReference38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mid_relationship_ExtendibleElementReference__mid_relationship_ExtendibleElementReference38", None)
        self.__mid_relationship_ExtendibleElementReference38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "relationship_mid_ExtendibleElement39"):
                opp_val = getattr(old_value, "relationship_mid_ExtendibleElement39", None)
                if opp_val == self:
                    setattr(old_value, "relationship_mid_ExtendibleElement39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "relationship_mid_ExtendibleElement39"):
                opp_val = getattr(value, "relationship_mid_ExtendibleElement39", None)
                setattr(value, "relationship_mid_ExtendibleElement39", self)

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

    def isTypesLevel(self) :
        # TODO: Implement isTypesLevel method
        pass

    def getUri(self) :
        # TODO: Implement getUri method
        pass

    def getObject(self) :
        # TODO: Implement getObject method
        pass

    def isWorkflowsLevel(self) :
        # TODO: Implement isWorkflowsLevel method
        pass

    def isInstancesLevel(self) :
        # TODO: Implement isInstancesLevel method
        pass

    def getMIDContainer(self) :
        # TODO: Implement getMIDContainer method
        pass

class relationship_mid_Model:

    pass
class ModelRel:

    pass
class mid_relationship_BinaryModelRel(ModelRel):

    def __init__(self, mid_relationship_BinaryModelRel: "relationship_mid_Model" = None, mid_relationship_BinaryModelRel34: "relationship_mid_Model" = None):
        self.mid_relationship_BinaryModelRel = mid_relationship_BinaryModelRel
        self.mid_relationship_BinaryModelRel34 = mid_relationship_BinaryModelRel34
        
        pass
    @property
    def mid_relationship_BinaryModelRel34(self):
        return self.__mid_relationship_BinaryModelRel34

    @mid_relationship_BinaryModelRel34.setter
    def mid_relationship_BinaryModelRel34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mid_relationship_BinaryModelRel__mid_relationship_BinaryModelRel34", None)
        self.__mid_relationship_BinaryModelRel34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "relationship_mid_Model35"):
                opp_val = getattr(old_value, "relationship_mid_Model35", None)
                if opp_val == self:
                    setattr(old_value, "relationship_mid_Model35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "relationship_mid_Model35"):
                opp_val = getattr(value, "relationship_mid_Model35", None)
                setattr(value, "relationship_mid_Model35", self)

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

    def addModelType(self, mid_isBinarySrc, mid_modelType):
        # TODO: Implement addModelType method
        pass

class MappingReference:

    pass
class mid_relationship_BinaryMappingReference(MappingReference):

    def __init__(self, mid_relationship_BinaryMappingReference: "ModelElementReference" = None, mid_relationship_BinaryMappingReference53: "ModelElementReference" = None, MappingReference: "mid_relationship_ModelRel" = None):
        self.mid_relationship_BinaryMappingReference = mid_relationship_BinaryMappingReference
        self.mid_relationship_BinaryMappingReference53 = mid_relationship_BinaryMappingReference53
        
        pass
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
            if hasattr(old_value, "ModelElementReference51"):
                opp_val = getattr(old_value, "ModelElementReference51", None)
                if opp_val == self:
                    setattr(old_value, "ModelElementReference51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ModelElementReference51"):
                opp_val = getattr(value, "ModelElementReference51", None)
                setattr(value, "ModelElementReference51", self)

    @property
    def mid_relationship_BinaryMappingReference53(self):
        return self.__mid_relationship_BinaryMappingReference53

    @mid_relationship_BinaryMappingReference53.setter
    def mid_relationship_BinaryMappingReference53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mid_relationship_BinaryMappingReference__mid_relationship_BinaryMappingReference53", None)
        self.__mid_relationship_BinaryMappingReference53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ModelElementReference54"):
                opp_val = getattr(old_value, "ModelElementReference54", None)
                if opp_val == self:
                    setattr(old_value, "ModelElementReference54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ModelElementReference54"):
                opp_val = getattr(value, "ModelElementReference54", None)
                setattr(value, "ModelElementReference54", self)

    def addModelElementTypeReference(self, mid_isBinarySrc, mid_modelElemTypeRef):
        # TODO: Implement addModelElementTypeReference method
        pass

    def getObject(self) :
        # TODO: Implement getObject method
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

    def __init__(self, mid_relationship_ModelRel: set["relationship_mid_ModelEndpoint"] = None, mid_relationship_ModelRel27: set["Mapping"] = None, mid_relationship_ModelRel29: set["ModelEndpointReference"] = None, mid_relationship_ModelRel31: set["MappingReference"] = None):
        self.mid_relationship_ModelRel = mid_relationship_ModelRel if mid_relationship_ModelRel is not None else set()
        self.mid_relationship_ModelRel27 = mid_relationship_ModelRel27 if mid_relationship_ModelRel27 is not None else set()
        self.mid_relationship_ModelRel29 = mid_relationship_ModelRel29 if mid_relationship_ModelRel29 is not None else set()
        self.mid_relationship_ModelRel31 = mid_relationship_ModelRel31 if mid_relationship_ModelRel31 is not None else set()
        
        pass
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
    def mid_relationship_ModelRel27(self):
        return self.__mid_relationship_ModelRel27

    @mid_relationship_ModelRel27.setter
    def mid_relationship_ModelRel27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mid_relationship_ModelRel__mid_relationship_ModelRel27", None)
        self.__mid_relationship_ModelRel27 = value if value is not None else set()
        
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
                    

    def createBinaryInstanceAndEndpoints(self, mid_endpointTargetModel, mid_instanceMID, mid_endpointSourceModel, mid_newModelRelUri) :
        # TODO: Implement createBinaryInstanceAndEndpoints method
        pass

    def getOutlineResourceTypes(self) :
        # TODO: Implement getOutlineResourceTypes method
        pass

    def getSupertype(self) :
        # TODO: Implement getSupertype method
        pass

    def getOutlineResourceInstances(self) :
        # TODO: Implement getOutlineResourceInstances method
        pass

    def createWorkflowInstanceAndEndpoints(self, mid_endpointModels, mid_newModelRelId, mid_workflowMID) :
        # TODO: Implement createWorkflowInstanceAndEndpoints method
        pass

    def getMIDContainer(self) :
        # TODO: Implement getMIDContainer method
        pass

    def createWorkflowBinaryInstanceAndEndpoints(self, mid_workflowMID, mid_endpointTargetModel, mid_newModelRelId, mid_endpointSourceModel) :
        # TODO: Implement createWorkflowBinaryInstanceAndEndpoints method
        pass

    def createBinarySubtype(self, mid_isMetamodelExtension, mid_newModelRelTypeName) :
        # TODO: Implement createBinarySubtype method
        pass

    def getMetatype(self) :
        # TODO: Implement getMetatype method
        pass

    def createBinaryInstance(self, mid_newModelRelUri, mid_instanceMID) :
        # TODO: Implement createBinaryInstance method
        pass

    def createInstanceAndEndpoints(self, mid_instanceMID, mid_newModelRelUri, mid_endpointModels) :
        # TODO: Implement createInstanceAndEndpoints method
        pass

    def createWorkflowBinaryInstance(self, mid_newModelRelId, mid_workflowMID) :
        # TODO: Implement createWorkflowBinaryInstance method
        pass

    def copySubtype(self, mid_origModelRelType) :
        # TODO: Implement copySubtype method
        pass

class ExtendibleElementEndpoint:

    pass
class mid_relationship_ModelElementEndpoint(ExtendibleElementEndpoint):

    def __init__(self):
        
        pass
    def createSubtypeAndReference(self, mid_containerMappingTypeRef, mid_targetModelElemTypeRef, mid_newModelElemTypeEndpointName, mid_isBinarySrc) :
        # TODO: Implement createSubtypeAndReference method
        pass

    def createInstanceReference(self, mid_containerMappingRef, mid_targetModelElemRef) :
        # TODO: Implement createInstanceReference method
        pass

    def deleteType(self, mid_isFullDelete):
        # TODO: Implement deleteType method
        pass

    def createTypeReference(self, mid_isModifiable, mid_containerMappingTypeRef, mid_targetModelElemTypeRef, mid_modelElemTypeEndpointRef, mid_isBinarySrc) :
        # TODO: Implement createTypeReference method
        pass

    def getMIDContainer(self) :
        # TODO: Implement getMIDContainer method
        pass

    def getTarget(self) :
        # TODO: Implement getTarget method
        pass

    def createInstanceAndReference(self, mid_containerMappingRef, mid_targetModelElemRef) :
        # TODO: Implement createInstanceAndReference method
        pass

    def replaceSubtypeAndReference(self, mid_targetModelElemTypeRef, mid_oldModelElemTypeEndpointRef, mid_newModelElemTypeEndpointName):
        # TODO: Implement replaceSubtypeAndReference method
        pass

    def getSupertype(self) :
        # TODO: Implement getSupertype method
        pass

    def replaceInstanceAndReference(self, mid_oldModelElemEndpointRef, mid_targetModelElemRef):
        # TODO: Implement replaceInstanceAndReference method
        pass

    def getMetatype(self) :
        # TODO: Implement getMetatype method
        pass

class mid_operator_GenericEndpoint(ExtendibleElementEndpoint):

    def __init__(self, metatargetUri: str):
        self.metatargetUri = metatargetUri
        
        pass
    @property
    def metatargetUri(self):
        return self.__metatargetUri

    @metatargetUri.setter
    def metatargetUri(self, metatargetUri: str):
        self.__metatargetUri = metatargetUri


    def getSupertype(self) :
        # TODO: Implement getSupertype method
        pass

    def createWorkflowInstance(self, mid_containerOperator, mid_targetGeneric) :
        # TODO: Implement createWorkflowInstance method
        pass

    def getTarget(self) :
        # TODO: Implement getTarget method
        pass

    def getMetatype(self) :
        # TODO: Implement getMetatype method
        pass

    def setTarget(self, mid_newTarget):
        # TODO: Implement setTarget method
        pass

    def createInstance(self, mid_targetGeneric, mid_containerOperator) :
        # TODO: Implement createInstance method
        pass

class mid_ModelEndpoint(ExtendibleElementEndpoint):

    def __init__(self):
        
        pass
    def createSubtype(self, mid_targetModelType, mid_isBinarySrc, mid_containerModelRelType, mid_newModelTypeEndpointName) :
        # TODO: Implement createSubtype method
        pass

    def getMIDContainer(self) :
        # TODO: Implement getMIDContainer method
        pass

    def getTarget(self) :
        # TODO: Implement getTarget method
        pass

    def replaceSubtype(self, mid_newModelTypeEndpointName, mid_targetModelType, mid_oldModelTypeEndpoint):
        # TODO: Implement replaceSubtype method
        pass

    def createInstanceReference(self, mid_containerModelRel) :
        # TODO: Implement createInstanceReference method
        pass

    def replaceWorkflowInstance(self, mid_targetModel, mid_oldModelEndpoint):
        # TODO: Implement replaceWorkflowInstance method
        pass

    def deleteType(self, mid_isFullDelete):
        # TODO: Implement deleteType method
        pass

    def replaceInstance(self, mid_targetModel, mid_oldModelEndpoint):
        # TODO: Implement replaceInstance method
        pass

    def createTypeReference(self, mid_containerModelRelType, mid_isModifiable) :
        # TODO: Implement createTypeReference method
        pass

    def getMetatype(self) :
        # TODO: Implement getMetatype method
        pass

    def getSupertype(self) :
        # TODO: Implement getSupertype method
        pass

    def createInstance(self, mid_targetModel, mid_containerFeatureName, mid_containerOperator) :
        # TODO: Implement createInstance method
        pass

    def deleteInstance(self, mid_isFullDelete):
        # TODO: Implement deleteInstance method
        pass

    def deleteWorkflowInstance(self):
        # TODO: Implement deleteWorkflowInstance method
        pass

    def createWorkflowInstance(self, mid_containerFeatureName, mid_targetModel, mid_containerOperator) :
        # TODO: Implement createWorkflowInstance method
        pass

class mid_EMFInfo:

    def __init__(self, className: str, featureName: str, attribute: bool, relatedClassName: str, mid_EMFInfo: "mid_ModelElement" = None):
        self.className = className
        self.featureName = featureName
        self.attribute = attribute
        self.relatedClassName = relatedClassName
        self.mid_EMFInfo = mid_EMFInfo
        
        pass
    @property
    def relatedClassName(self):
        return self.__relatedClassName

    @relatedClassName.setter
    def relatedClassName(self, relatedClassName: str):
        self.__relatedClassName = relatedClassName


    @property
    def className(self):
        return self.__className

    @className.setter
    def className(self, className: str):
        self.__className = className


    @property
    def featureName(self):
        return self.__featureName

    @featureName.setter
    def featureName(self, featureName: str):
        self.__featureName = featureName


    @property
    def attribute(self):
        return self.__attribute

    @attribute.setter
    def attribute(self, attribute: bool):
        self.__attribute = attribute


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
            if hasattr(old_value, "mid_ModelElement24"):
                opp_val = getattr(old_value, "mid_ModelElement24", None)
                if opp_val == self:
                    setattr(old_value, "mid_ModelElement24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mid_ModelElement24"):
                opp_val = getattr(value, "mid_ModelElement24", None)
                setattr(value, "mid_ModelElement24", self)

    def toInstanceString(self) :
        # TODO: Implement toInstanceString method
        pass

    def toTypeString(self) :
        # TODO: Implement toTypeString method
        pass

class ConversionOperator:

    pass
class GenericElement:

    pass
class mid_operator_Operator(GenericElement):

    def __init__(self, updateMID: bool, executionTime: str, commutative: bool, inputSubdir: str, mid_operator_Operator64: "Operator" = None, mid_operator_Operator: set["operator_mid_ModelEndpoint"] = None, mid_operator_Operator59: set["operator_mid_ModelEndpoint"] = None, mid_operator_Operator62: set["GenericEndpoint"] = None):
        self.updateMID = updateMID
        self.executionTime = executionTime
        self.commutative = commutative
        self.inputSubdir = inputSubdir
        self.mid_operator_Operator64 = mid_operator_Operator64
        self.mid_operator_Operator = mid_operator_Operator if mid_operator_Operator is not None else set()
        self.mid_operator_Operator59 = mid_operator_Operator59 if mid_operator_Operator59 is not None else set()
        self.mid_operator_Operator62 = mid_operator_Operator62 if mid_operator_Operator62 is not None else set()
        
        pass
    @property
    def executionTime(self):
        return self.__executionTime

    @executionTime.setter
    def executionTime(self, executionTime: str):
        self.__executionTime = executionTime


    @property
    def updateMID(self):
        return self.__updateMID

    @updateMID.setter
    def updateMID(self, updateMID: bool):
        self.__updateMID = updateMID


    @property
    def commutative(self):
        return self.__commutative

    @commutative.setter
    def commutative(self, commutative: bool):
        self.__commutative = commutative


    @property
    def inputSubdir(self):
        return self.__inputSubdir

    @inputSubdir.setter
    def inputSubdir(self, inputSubdir: str):
        self.__inputSubdir = inputSubdir


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
    def mid_operator_Operator59(self):
        return self.__mid_operator_Operator59

    @mid_operator_Operator59.setter
    def mid_operator_Operator59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mid_operator_Operator__mid_operator_Operator59", None)
        self.__mid_operator_Operator59 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "operator_mid_ModelEndpoint60"):
                    opp_val = getattr(item, "operator_mid_ModelEndpoint60", None)
                    
                    if opp_val == self:
                        setattr(item, "operator_mid_ModelEndpoint60", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "operator_mid_ModelEndpoint60"):
                    opp_val = getattr(item, "operator_mid_ModelEndpoint60", None)
                    
                    setattr(item, "operator_mid_ModelEndpoint60", self)
                    

    @property
    def mid_operator_Operator64(self):
        return self.__mid_operator_Operator64

    @mid_operator_Operator64.setter
    def mid_operator_Operator64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mid_operator_Operator__mid_operator_Operator64", None)
        self.__mid_operator_Operator64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Operator65"):
                opp_val = getattr(old_value, "Operator65", None)
                if opp_val == self:
                    setattr(old_value, "Operator65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Operator65"):
                opp_val = getattr(value, "Operator65", None)
                setattr(value, "Operator65", self)

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
                    

    def openInstance(self):
        # TODO: Implement openInstance method
        pass

    def getOutputModels(self) :
        # TODO: Implement getOutputModels method
        pass

    def createInstance(self, mid_instanceMID) :
        # TODO: Implement createInstance method
        pass

    def deleteWorkflowInstance(self):
        # TODO: Implement deleteWorkflowInstance method
        pass

    def readInputProperties(self, mid_inputProperties):
        # TODO: Implement readInputProperties method
        pass

    def createWorkflowInstance(self, mid_workflowMID) :
        # TODO: Implement createWorkflowInstance method
        pass

    def checkAllowedInputs(self, mid_inputModels) :
        # TODO: Implement checkAllowedInputs method
        pass

    def getMetatype(self) :
        # TODO: Implement getMetatype method
        pass

    def findFirstAllowedInput(self, mid_inputMIDs) :
        # TODO: Implement findFirstAllowedInput method
        pass

    def createSubtype(self, mid_implementationUri, mid_newOperatorTypeName) :
        # TODO: Implement createSubtype method
        pass

    def getOutputsByName(self):
        # TODO: Implement getOutputsByName method
        pass

    def deleteType(self):
        # TODO: Implement deleteType method
        pass

    def getSupertype(self) :
        # TODO: Implement getSupertype method
        pass

    def getMIDContainer(self) :
        # TODO: Implement getMIDContainer method
        pass

    def startWorkflowInstance(self, mid_inputs, mid_workflowMID, mid_generics) :
        # TODO: Implement startWorkflowInstance method
        pass

    def run(self, mid_inputsByName, mid_outputMIDsByName, mid_genericsByName):
        # TODO: Implement run method
        pass

    def openType(self):
        # TODO: Implement openType method
        pass

    def getInputProperties(self) :
        # TODO: Implement getInputProperties method
        pass

    def deleteInstance(self):
        # TODO: Implement deleteInstance method
        pass

    def startInstance(self, mid_inputProperties, mid_instanceMID, mid_inputs, mid_outputMIDsByName, mid_generics) :
        # TODO: Implement startInstance method
        pass

    def findAllowedInputs(self, mid_inputMIDs):
        # TODO: Implement findAllowedInputs method
        pass

    def openWorkflowInstance(self):
        # TODO: Implement openWorkflowInstance method
        pass

    def selectAllowedGenerics(self, mid_inputs) :
        # TODO: Implement selectAllowedGenerics method
        pass

    def isAllowedGeneric(self, mid_genericTypeEndpoint, mid_genericType, mid_inputs) :
        # TODO: Implement isAllowedGeneric method
        pass

class mid_ExtendibleElementConstraint:

    def __init__(self, implementation: str, language: str, mid_ExtendibleElementConstraint: "mid_ExtendibleElement" = None):
        self.implementation = implementation
        self.language = language
        self.mid_ExtendibleElementConstraint = mid_ExtendibleElementConstraint
        
        pass
    @property
    def implementation(self):
        return self.__implementation

    @implementation.setter
    def implementation(self, implementation: str):
        self.__implementation = implementation


    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language


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

class ExtendibleElement:

    pass
class mid_editor_Editor(ExtendibleElement):

    def __init__(self, modelUri: str, id: str, wizardId: str, fileExtensions: str, wizardDialogClass: str):
        self.modelUri = modelUri
        self.id = id
        self.wizardId = wizardId
        self.fileExtensions = fileExtensions
        self.wizardDialogClass = wizardDialogClass
        
        pass
    @property
    def modelUri(self):
        return self.__modelUri

    @modelUri.setter
    def modelUri(self, modelUri: str):
        self.__modelUri = modelUri


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def wizardId(self):
        return self.__wizardId

    @wizardId.setter
    def wizardId(self, wizardId: str):
        self.__wizardId = wizardId


    @property
    def fileExtensions(self):
        return self.__fileExtensions

    @fileExtensions.setter
    def fileExtensions(self, fileExtensions: str):
        self.__fileExtensions = fileExtensions


    @property
    def wizardDialogClass(self):
        return self.__wizardDialogClass

    @wizardDialogClass.setter
    def wizardDialogClass(self, wizardDialogClass: str):
        self.__wizardDialogClass = wizardDialogClass


    def getMIDContainer(self) :
        # TODO: Implement getMIDContainer method
        pass

    def deleteInstance(self):
        # TODO: Implement deleteInstance method
        pass

    def getSupertype(self) :
        # TODO: Implement getSupertype method
        pass

    def createInstance(self, mid_instanceMID, mid_modelUri) :
        # TODO: Implement createInstance method
        pass

    def deleteType(self):
        # TODO: Implement deleteType method
        pass

    def invokeInstanceWizard(self, mid_initialSelection) :
        # TODO: Implement invokeInstanceWizard method
        pass

    def createSubtype(self, mid_modelTypeUri, mid_wizardDialogClassName, mid_newEditorTypeName, mid_editorId, mid_newEditorTypeFragmentUri, mid_wizardId) :
        # TODO: Implement createSubtype method
        pass

    def getMetatype(self) :
        # TODO: Implement getMetatype method
        pass

class mid_relationship_Mapping(ExtendibleElement):

    def __init__(self, mid_relationship_Mapping: set["ModelElementEndpoint"] = None, mid_relationship_Mapping46: set["ModelElementEndpointReference"] = None):
        self.mid_relationship_Mapping = mid_relationship_Mapping if mid_relationship_Mapping is not None else set()
        self.mid_relationship_Mapping46 = mid_relationship_Mapping46 if mid_relationship_Mapping46 is not None else set()
        
        pass
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
    def mid_relationship_Mapping46(self):
        return self.__mid_relationship_Mapping46

    @mid_relationship_Mapping46.setter
    def mid_relationship_Mapping46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mid_relationship_Mapping__mid_relationship_Mapping46", None)
        self.__mid_relationship_Mapping46 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ModelElementEndpointReference47"):
                    opp_val = getattr(item, "ModelElementEndpointReference47", None)
                    
                    if opp_val == self:
                        setattr(item, "ModelElementEndpointReference47", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ModelElementEndpointReference47"):
                    opp_val = getattr(item, "ModelElementEndpointReference47", None)
                    
                    setattr(item, "ModelElementEndpointReference47", self)
                    

    def getMetatype(self) :
        # TODO: Implement getMetatype method
        pass

    def createInstanceAndReferenceAndEndpointsAndReferences(self, mid_isBinary, mid_targetModelElemRefs) :
        # TODO: Implement createInstanceAndReferenceAndEndpointsAndReferences method
        pass

    def getSupertype(self) :
        # TODO: Implement getSupertype method
        pass

    def createSubtypeAndReference(self, mid_isBinary, mid_containerModelRelType, mid_newMappingTypeName, mid_mappingTypeRef) :
        # TODO: Implement createSubtypeAndReference method
        pass

    def createInstanceReference(self, mid_containerModelRel) :
        # TODO: Implement createInstanceReference method
        pass

    def getMIDContainer(self) :
        # TODO: Implement getMIDContainer method
        pass

    def deleteType(self):
        # TODO: Implement deleteType method
        pass

    def createInstanceAndReference(self, mid_containerModelRel, mid_isBinary) :
        # TODO: Implement createInstanceAndReference method
        pass

    def deleteInstance(self):
        # TODO: Implement deleteInstance method
        pass

    def createTypeReference(self, mid_isModifiable, mid_mappingTypeRef, mid_containerModelRelType) :
        # TODO: Implement createTypeReference method
        pass

class mid_ModelElement(ExtendibleElement):

    def __init__(self, mid_ModelElement: "mid_Model" = None, mid_ModelElement24: "mid_EMFInfo" = None):
        self.mid_ModelElement = mid_ModelElement
        self.mid_ModelElement24 = mid_ModelElement24
        
        pass
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

    @property
    def mid_ModelElement24(self):
        return self.__mid_ModelElement24

    @mid_ModelElement24.setter
    def mid_ModelElement24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mid_ModelElement__mid_ModelElement24", None)
        self.__mid_ModelElement24 = value
        
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

    def getMIDContainer(self) :
        # TODO: Implement getMIDContainer method
        pass

    def createTypeReference(self, mid_containerModelTypeEndpointRef, mid_isModifiable, mid_modelElemTypeRef) :
        # TODO: Implement createTypeReference method
        pass

    def createInstanceAndReference(self, mid_eInfo, mid_containerModelEndpointRef, mid_newModelElemName, mid_newModelElemUri) :
        # TODO: Implement createInstanceAndReference method
        pass

    def createSubtypeAndReference(self, mid_containerModelTypeEndpointRef, mid_newModelElemTypeUri, mid_modelElemTypeRef, mid_eInfo, mid_newModelElemTypeName) :
        # TODO: Implement createSubtypeAndReference method
        pass

    def createInstanceReference(self, mid_containerModelEndpointRef) :
        # TODO: Implement createInstanceReference method
        pass

    def getSupertype(self) :
        # TODO: Implement getSupertype method
        pass

    def deleteType(self):
        # TODO: Implement deleteType method
        pass

    def getEMFTypeObject(self) :
        # TODO: Implement getEMFTypeObject method
        pass

    def deleteInstance(self):
        # TODO: Implement deleteInstance method
        pass

    def getEMFInstanceObject(self) :
        # TODO: Implement getEMFInstanceObject method
        pass

    def getMetatype(self) :
        # TODO: Implement getMetatype method
        pass

class mid_GenericElement(ExtendibleElement):

    def __init__(self, abstract: bool):
        self.abstract = abstract
        
        pass
    @property
    def abstract(self):
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: bool):
        self.__abstract = abstract


class mid_ExtendibleElementEndpoint(ExtendibleElement):

    def __init__(self, lowerBound: int, upperBound: int, mid_ExtendibleElementEndpoint: "mid_ExtendibleElement" = None):
        self.lowerBound = lowerBound
        self.upperBound = upperBound
        self.mid_ExtendibleElementEndpoint = mid_ExtendibleElementEndpoint
        
        pass
    @property
    def lowerBound(self):
        return self.__lowerBound

    @lowerBound.setter
    def lowerBound(self, lowerBound: int):
        self.__lowerBound = lowerBound


    @property
    def upperBound(self):
        return self.__upperBound

    @upperBound.setter
    def upperBound(self, upperBound: int):
        self.__upperBound = upperBound


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

    def getSupertype(self) :
        # TODO: Implement getSupertype method
        pass

    def getMetatype(self) :
        # TODO: Implement getMetatype method
        pass

    def getTargetUri(self) :
        # TODO: Implement getTargetUri method
        pass

class mid_ExtendibleElement(ABC):

    def __init__(self, uri: str, name: str, level: str, metatypeUri: str, dynamic: bool, mid_ExtendibleElement: "mid_EStringToExtendibleElementMap" = None, mid_ExtendibleElement11: "mid_ExtendibleElement" = None, mid_ExtendibleElement9: "mid_ExtendibleElement" = None, mid_ExtendibleElement13: "mid_ExtendibleElementConstraint" = None, mid_ExtendibleElement15: "mid_ExtendibleElementEndpoint" = None):
        self.uri = uri
        self.name = name
        self.level = level
        self.metatypeUri = metatypeUri
        self.dynamic = dynamic
        self.mid_ExtendibleElement = mid_ExtendibleElement
        self.mid_ExtendibleElement11 = mid_ExtendibleElement11
        self.mid_ExtendibleElement9 = mid_ExtendibleElement9
        self.mid_ExtendibleElement13 = mid_ExtendibleElement13
        self.mid_ExtendibleElement15 = mid_ExtendibleElement15
        
        pass
    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self, level: str):
        self.__level = level


    @property
    def metatypeUri(self):
        return self.__metatypeUri

    @metatypeUri.setter
    def metatypeUri(self, metatypeUri: str):
        self.__metatypeUri = metatypeUri


    @property
    def uri(self):
        return self.__uri

    @uri.setter
    def uri(self, uri: str):
        self.__uri = uri


    @property
    def dynamic(self):
        return self.__dynamic

    @dynamic.setter
    def dynamic(self, dynamic: bool):
        self.__dynamic = dynamic


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


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

    def updateMIDCustomLabel(self, mid_newLabel):
        # TODO: Implement updateMIDCustomLabel method
        pass

    def validateInstanceType(self, mid_type) :
        # TODO: Implement validateInstanceType method
        pass

    def validateInstanceInEditor(self, mid_context) :
        # TODO: Implement validateInstanceInEditor method
        pass

    def validateInstance(self) :
        # TODO: Implement validateInstance method
        pass

    def getMIDContainer(self) :
        # TODO: Implement getMIDContainer method
        pass

    def createSubtypeUri(self, mid_newTypeName, mid_newTypeFragmentUri) :
        # TODO: Implement createSubtypeUri method
        pass

    def toMIDCustomPrintLabel(self) :
        # TODO: Implement toMIDCustomPrintLabel method
        pass

    def updateWorkflowInstanceId(self, mid_newInstanceId):
        # TODO: Implement updateWorkflowInstanceId method
        pass

    def isInstancesLevel(self) :
        # TODO: Implement isInstancesLevel method
        pass

    def getRuntimeTypes(self):
        # TODO: Implement getRuntimeTypes method
        pass

    def getMetatype(self) :
        # TODO: Implement getMetatype method
        pass

    def toMIDCustomEditLabel(self) :
        # TODO: Implement toMIDCustomEditLabel method
        pass

    def addTypeConstraint(self, mid_language, mid_implementation):
        # TODO: Implement addTypeConstraint method
        pass

    def isTypesLevel(self) :
        # TODO: Implement isTypesLevel method
        pass

    def isWorkflowsLevel(self) :
        # TODO: Implement isWorkflowsLevel method
        pass

    def isLevel(self, mid_midLevel) :
        # TODO: Implement isLevel method
        pass

class mid_MID:

    def __init__(self, level: str, mid_MID: set["mid_Model"] = None, mid_MID2: set["Editor"] = None, mid_MID4: set["Operator"] = None, mid_MID6: set["mid_EStringToExtendibleElementMap"] = None):
        self.level = level
        self.mid_MID = mid_MID if mid_MID is not None else set()
        self.mid_MID2 = mid_MID2 if mid_MID2 is not None else set()
        self.mid_MID4 = mid_MID4 if mid_MID4 is not None else set()
        self.mid_MID6 = mid_MID6 if mid_MID6 is not None else set()
        
        pass
    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self, level: str):
        self.__level = level


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
                    

    def isTypesLevel(self) :
        # TODO: Implement isTypesLevel method
        pass

    def isWorkflowsLevel(self) :
        # TODO: Implement isWorkflowsLevel method
        pass

    def getExtendibleElement(self, mid_uri):
        # TODO: Implement getExtendibleElement method
        pass

    def getModelRels(self) :
        # TODO: Implement getModelRels method
        pass

    def isInstancesLevel(self) :
        # TODO: Implement isInstancesLevel method
        pass

class mid_EStringToExtendibleElementMap:

    def __init__(self, key: str, mid_EStringToExtendibleElementMap: "mid_MID" = None, mid_EStringToExtendibleElementMap8: "mid_ExtendibleElement" = None):
        self.key = key
        self.mid_EStringToExtendibleElementMap = mid_EStringToExtendibleElementMap
        self.mid_EStringToExtendibleElementMap8 = mid_EStringToExtendibleElementMap8
        
        pass
    @property
    def key(self):
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

class Operator:

    pass
class mid_operator_WorkflowOperator(Operator):

    def __init__(self, midUri: str, Operator: "mid_MID" = None, Operator65: "mid_operator_Operator" = None):
        self.midUri = midUri
        
        pass
    @property
    def midUri(self):
        return self.__midUri

    @midUri.setter
    def midUri(self, midUri: str):
        self.__midUri = midUri


    def getInstanceMID(self) :
        # TODO: Implement getInstanceMID method
        pass

    def getWorkflowMID(self) :
        # TODO: Implement getWorkflowMID method
        pass

class mid_operator_RandomOperator(Operator):

    def __init__(self, state: str, Operator: "mid_MID" = None, Operator65: "mid_operator_Operator" = None):
        self.state = state
        
        pass
    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, state: str):
        self.__state = state


class mid_operator_ConversionOperator(Operator):

    def __init__(self, Operator: "mid_MID" = None, Operator65: "mid_operator_Operator" = None):
        
        pass
    def deleteType(self):
        # TODO: Implement deleteType method
        pass

    def cleanup(self):
        # TODO: Implement cleanup method
        pass

class Editor:

    pass
class mid_editor_Diagram(Editor):

    def __init__(self, Editor: "mid_MID" = None, Editor18: "mid_Model" = None):
        
        pass
    def createSubtype(self, mid_wizardDialogClassName, mid_modelTypeUri, mid_editorId, mid_newEditorTypeName, mid_newEditorTypeFragmentUri, mid_wizardId) :
        # TODO: Implement createSubtype method
        pass

    def createInstance(self, mid_instanceMID, mid_modelUri) :
        # TODO: Implement createInstance method
        pass

    def invokeInstanceWizard(self, mid_initialSelection) :
        # TODO: Implement invokeInstanceWizard method
        pass

class mid_Model(GenericElement):

    def __init__(self, origin: str, fileExtension: str, mid_Model: "mid_MID" = None, mid_Model17: set["Editor"] = None, mid_Model20: set["mid_ModelElement"] = None, mid_Model22: set["ConversionOperator"] = None):
        self.origin = origin
        self.fileExtension = fileExtension
        self.mid_Model = mid_Model
        self.mid_Model17 = mid_Model17 if mid_Model17 is not None else set()
        self.mid_Model20 = mid_Model20 if mid_Model20 is not None else set()
        self.mid_Model22 = mid_Model22 if mid_Model22 is not None else set()
        
        pass
    @property
    def fileExtension(self):
        return self.__fileExtension

    @fileExtension.setter
    def fileExtension(self, fileExtension: str):
        self.__fileExtension = fileExtension


    @property
    def origin(self):
        return self.__origin

    @origin.setter
    def origin(self, origin: str):
        self.__origin = origin


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
                    

    def createInstanceAndEditor(self, mid_newModelUri, mid_instanceMID) :
        # TODO: Implement createInstanceAndEditor method
        pass

    def openInstance(self):
        # TODO: Implement openInstance method
        pass

    def copyInstance(self, mid_instanceMID, mid_origModel, mid_newModelName) :
        # TODO: Implement copyInstance method
        pass

    def deleteWorkflowInstance(self):
        # TODO: Implement deleteWorkflowInstance method
        pass

    def getEMFTypeRoot(self) :
        # TODO: Implement getEMFTypeRoot method
        pass

    def getMIDContainer(self) :
        # TODO: Implement getMIDContainer method
        pass

    def importInstanceAndEditor(self, mid_modelUri, mid_instanceMID) :
        # TODO: Implement importInstanceAndEditor method
        pass

    def deleteType(self):
        # TODO: Implement deleteType method
        pass

    def getSupertype(self) :
        # TODO: Implement getSupertype method
        pass

    def deleteInstanceAndFile(self):
        # TODO: Implement deleteInstanceAndFile method
        pass

    def createWorkflowInstance(self, mid_newModelId, mid_workflowMID) :
        # TODO: Implement createWorkflowInstance method
        pass

    def getMetatype(self) :
        # TODO: Implement getMetatype method
        pass

    def getEMFInstanceRoot(self) :
        # TODO: Implement getEMFInstanceRoot method
        pass

    def copyInstanceAndEditor(self, mid_copyDiagram, mid_origModel, mid_newModelName, mid_instanceMID) :
        # TODO: Implement copyInstanceAndEditor method
        pass

    def createInstanceEditor(self) :
        # TODO: Implement createInstanceEditor method
        pass

    def importInstance(self, mid_instanceMID, mid_modelUri) :
        # TODO: Implement importInstance method
        pass

    def deleteInstance(self):
        # TODO: Implement deleteInstance method
        pass

    def createSubtype(self, mid_isMetamodelExtension, mid_newModelTypeName) :
        # TODO: Implement createSubtype method
        pass

    def openType(self):
        # TODO: Implement openType method
        pass

    def createInstance(self, mid_newModelUri, mid_instanceMID) :
        # TODO: Implement createInstance method
        pass
