from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class CallConcurrencyFeature(Enum):
    sequential = "sequential"
    guarded = "guarded"
    concurrent = "concurrent"
class ObjectNodeOrderingKind(Enum):
    FIFO = "FIFO"
    unordered = "unordered"
    ordered = "ordered"
    LIFO = "LIFO"
class AggregationKind(Enum):
    none = "none"
    shared = "shared"
    composite = "composite"
class ExpansionKind(Enum):
    parallel = "parallel"
    iterative = "iterative"
    stream = "stream"
class InteractionOperandKind(Enum):
    seq = "seq"
    alt = "alt"
    opt = "opt"
    break_ = "break_"
    par = "par"
    strict = "strict"
    loop = "loop"
    critical = "critical"
    neg = "neg"
    assert_ = "assert_"
    ignore = "ignore"
    consider = "consider"
class ConnectorKind(Enum):
    assembly = "assembly"
    delegation = "delegation"
class MessageKind(Enum):
    complete = "complete"
    lost = "lost"
    found = "found"
    unknown = "unknown"
class ParameterEffectKind(Enum):
    create = "create"
    read = "read"
    update = "update"
    delete = "delete"
class TransitionKind(Enum):
    internal = "internal"
    external = "external"
class VisibilityKind(Enum):
    private = "private"
    protected = "protected"
    package = "package"
    public = "public"
class MessageSort(Enum):
    synchCall = "synchCall"
    asynchCall = "asynchCall"
    asynchSignal = "asynchSignal"
    createMessage = "createMessage"
    deleteMessage = "deleteMessage"
    reply = "reply"


############################################
# Definition of Classes
############################################

class AcceptEventAction:

    pass
class CompleteDSLPckg_AcceptCallAction(AcceptEventAction):

    pass
class LinkAction:

    pass
class CompleteDSLPckg_WriteLinkAction(LinkAction):

    pass
class CompleteDSLPckg_ReadLinkAction(LinkAction):

    pass
class WriteStructuralFeatureAction:

    pass
class CompleteDSLPckg_RemoveStructuralFeatureValueAction(WriteStructuralFeatureAction):

    pass
class CompleteDSLPckg_AddStructuralFeatureValueAction(WriteStructuralFeatureAction):

    pass
class LinkEndData:

    pass
class CompleteDSLPckg_LinkEndDestructionData(LinkEndData):

    def __init__(self, isDestroyDuplicates: bool, CompleteDSLPckg_LinkEndDestructionData: "CompleteDSLPckg_InputPin" = None):
        self.isDestroyDuplicates = isDestroyDuplicates
        self.CompleteDSLPckg_LinkEndDestructionData = CompleteDSLPckg_LinkEndDestructionData
        
        pass
    @property
    def isDestroyDuplicates(self):
        return self.__isDestroyDuplicates

    @isDestroyDuplicates.setter
    def isDestroyDuplicates(self, isDestroyDuplicates: bool):
        self.__isDestroyDuplicates = isDestroyDuplicates


    @property
    def CompleteDSLPckg_LinkEndDestructionData(self):
        return self.__CompleteDSLPckg_LinkEndDestructionData

    @CompleteDSLPckg_LinkEndDestructionData.setter
    def CompleteDSLPckg_LinkEndDestructionData(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_LinkEndDestructionData__CompleteDSLPckg_LinkEndDestructionData", None)
        self.__CompleteDSLPckg_LinkEndDestructionData = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_InputPin483"):
                opp_val = getattr(old_value, "CompleteDSLPckg_InputPin483", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_InputPin483", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_InputPin483"):
                opp_val = getattr(value, "CompleteDSLPckg_InputPin483", None)
                setattr(value, "CompleteDSLPckg_InputPin483", self)

class CompleteDSLPckg_LinkEndCreationData(LinkEndData):

    def __init__(self, isReplaceAll: bool, CompleteDSLPckg_LinkEndCreationData: "CompleteDSLPckg_InputPin" = None):
        self.isReplaceAll = isReplaceAll
        self.CompleteDSLPckg_LinkEndCreationData = CompleteDSLPckg_LinkEndCreationData
        
        pass
    @property
    def isReplaceAll(self):
        return self.__isReplaceAll

    @isReplaceAll.setter
    def isReplaceAll(self, isReplaceAll: bool):
        self.__isReplaceAll = isReplaceAll


    @property
    def CompleteDSLPckg_LinkEndCreationData(self):
        return self.__CompleteDSLPckg_LinkEndCreationData

    @CompleteDSLPckg_LinkEndCreationData.setter
    def CompleteDSLPckg_LinkEndCreationData(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_LinkEndCreationData__CompleteDSLPckg_LinkEndCreationData", None)
        self.__CompleteDSLPckg_LinkEndCreationData = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_InputPin481"):
                opp_val = getattr(old_value, "CompleteDSLPckg_InputPin481", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_InputPin481", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_InputPin481"):
                opp_val = getattr(value, "CompleteDSLPckg_InputPin481", None)
                setattr(value, "CompleteDSLPckg_InputPin481", self)

class WriteLinkAction:

    pass
class CompleteDSLPckg_DestroyLinkAction(WriteLinkAction):

    pass
class CompleteDSLPckg_CreateLinkAction(WriteLinkAction):

    pass
class StructuralFeatureAction:

    pass
class CompleteDSLPckg_WriteStructuralFeatureAction(StructuralFeatureAction):

    pass
class CompleteDSLPckg_ClearStructuralFeatureAction(StructuralFeatureAction):

    pass
class CompleteDSLPckg_ReadStructuralFeatureAction(StructuralFeatureAction):

    pass
class CompleteDSLPckg_CallOperationAction:

    pass
class CallAction:

    pass
class CompleteDSLPckg_CallBehaviorAction(CallAction):

    pass
class InvocationAction:

    pass
class CompleteDSLPckg_SendSignalAction(InvocationAction):

    pass
class CompleteDSLPckg_BroadcastSignalAction(InvocationAction):

    pass
class CompleteDSLPckg_CallAction(InvocationAction):

    def __init__(self, isSynchronous: bool, CompleteDSLPckg_CallAction: set["CompleteDSLPckg_OutputPin"] = None):
        self.isSynchronous = isSynchronous
        self.CompleteDSLPckg_CallAction = CompleteDSLPckg_CallAction if CompleteDSLPckg_CallAction is not None else set()
        
        pass
    @property
    def isSynchronous(self):
        return self.__isSynchronous

    @isSynchronous.setter
    def isSynchronous(self, isSynchronous: bool):
        self.__isSynchronous = isSynchronous


    @property
    def CompleteDSLPckg_CallAction(self):
        return self.__CompleteDSLPckg_CallAction

    @CompleteDSLPckg_CallAction.setter
    def CompleteDSLPckg_CallAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_CallAction__CompleteDSLPckg_CallAction", None)
        self.__CompleteDSLPckg_CallAction = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_OutputPin406"):
                    opp_val = getattr(item, "CompleteDSLPckg_OutputPin406", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_OutputPin406", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_OutputPin406"):
                    opp_val = getattr(item, "CompleteDSLPckg_OutputPin406", None)
                    
                    setattr(item, "CompleteDSLPckg_OutputPin406", self)
                    

class InputPin:

    pass
class CompleteDSLPckg_ValuePin(InputPin):

    pass
class Pin:

    pass
class Action:

    pass
class CompleteDSLPckg_ValueSpecificationAction(Action):

    pass
class CompleteDSLPckg_ReplyAction(Action):

    pass
class CompleteDSLPckg_TestIdentityAction(Action):

    pass
class CompleteDSLPckg_ReadSelfAction(Action):

    pass
class CompleteDSLPckg_ReadExtendAction(Action):

    pass
class CompleteDSLPckg_LinkAction(Action):

    pass
class CompleteDSLPckg_AcceptEventAction(Action):

    def __init__(self, isUnmarshall: bool, CompleteDSLPckg_AcceptEventAction: set["CompleteDSLPckg_OutputPin"] = None, CompleteDSLPckg_AcceptEventAction503: set["CompleteDSLPckg_Trigger"] = None):
        self.isUnmarshall = isUnmarshall
        self.CompleteDSLPckg_AcceptEventAction = CompleteDSLPckg_AcceptEventAction if CompleteDSLPckg_AcceptEventAction is not None else set()
        self.CompleteDSLPckg_AcceptEventAction503 = CompleteDSLPckg_AcceptEventAction503 if CompleteDSLPckg_AcceptEventAction503 is not None else set()
        
        pass
    @property
    def isUnmarshall(self):
        return self.__isUnmarshall

    @isUnmarshall.setter
    def isUnmarshall(self, isUnmarshall: bool):
        self.__isUnmarshall = isUnmarshall


    @property
    def CompleteDSLPckg_AcceptEventAction(self):
        return self.__CompleteDSLPckg_AcceptEventAction

    @CompleteDSLPckg_AcceptEventAction.setter
    def CompleteDSLPckg_AcceptEventAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_AcceptEventAction__CompleteDSLPckg_AcceptEventAction", None)
        self.__CompleteDSLPckg_AcceptEventAction = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_OutputPin501"):
                    opp_val = getattr(item, "CompleteDSLPckg_OutputPin501", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_OutputPin501", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_OutputPin501"):
                    opp_val = getattr(item, "CompleteDSLPckg_OutputPin501", None)
                    
                    setattr(item, "CompleteDSLPckg_OutputPin501", self)
                    

    @property
    def CompleteDSLPckg_AcceptEventAction503(self):
        return self.__CompleteDSLPckg_AcceptEventAction503

    @CompleteDSLPckg_AcceptEventAction503.setter
    def CompleteDSLPckg_AcceptEventAction503(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_AcceptEventAction__CompleteDSLPckg_AcceptEventAction503", None)
        self.__CompleteDSLPckg_AcceptEventAction503 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_Trigger504"):
                    opp_val = getattr(item, "CompleteDSLPckg_Trigger504", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_Trigger504", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_Trigger504"):
                    opp_val = getattr(item, "CompleteDSLPckg_Trigger504", None)
                    
                    setattr(item, "CompleteDSLPckg_Trigger504", self)
                    

class CompleteDSLPckg_ReclassifyObjectAction(Action):

    def __init__(self, isReplaceAll: bool, CompleteDSLPckg_ReclassifyObjectAction: "CompleteDSLPckg_InputPin" = None, CompleteDSLPckg_ReclassifyObjectAction515: set["CompleteDSLPckg_Classifier"] = None, CompleteDSLPckg_ReclassifyObjectAction518: set["CompleteDSLPckg_Classifier"] = None):
        self.isReplaceAll = isReplaceAll
        self.CompleteDSLPckg_ReclassifyObjectAction = CompleteDSLPckg_ReclassifyObjectAction
        self.CompleteDSLPckg_ReclassifyObjectAction515 = CompleteDSLPckg_ReclassifyObjectAction515 if CompleteDSLPckg_ReclassifyObjectAction515 is not None else set()
        self.CompleteDSLPckg_ReclassifyObjectAction518 = CompleteDSLPckg_ReclassifyObjectAction518 if CompleteDSLPckg_ReclassifyObjectAction518 is not None else set()
        
        pass
    @property
    def isReplaceAll(self):
        return self.__isReplaceAll

    @isReplaceAll.setter
    def isReplaceAll(self, isReplaceAll: bool):
        self.__isReplaceAll = isReplaceAll


    @property
    def CompleteDSLPckg_ReclassifyObjectAction515(self):
        return self.__CompleteDSLPckg_ReclassifyObjectAction515

    @CompleteDSLPckg_ReclassifyObjectAction515.setter
    def CompleteDSLPckg_ReclassifyObjectAction515(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_ReclassifyObjectAction__CompleteDSLPckg_ReclassifyObjectAction515", None)
        self.__CompleteDSLPckg_ReclassifyObjectAction515 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_Classifier516"):
                    opp_val = getattr(item, "CompleteDSLPckg_Classifier516", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_Classifier516", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_Classifier516"):
                    opp_val = getattr(item, "CompleteDSLPckg_Classifier516", None)
                    
                    setattr(item, "CompleteDSLPckg_Classifier516", self)
                    

    @property
    def CompleteDSLPckg_ReclassifyObjectAction518(self):
        return self.__CompleteDSLPckg_ReclassifyObjectAction518

    @CompleteDSLPckg_ReclassifyObjectAction518.setter
    def CompleteDSLPckg_ReclassifyObjectAction518(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_ReclassifyObjectAction__CompleteDSLPckg_ReclassifyObjectAction518", None)
        self.__CompleteDSLPckg_ReclassifyObjectAction518 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_Classifier519"):
                    opp_val = getattr(item, "CompleteDSLPckg_Classifier519", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_Classifier519", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_Classifier519"):
                    opp_val = getattr(item, "CompleteDSLPckg_Classifier519", None)
                    
                    setattr(item, "CompleteDSLPckg_Classifier519", self)
                    

    @property
    def CompleteDSLPckg_ReclassifyObjectAction(self):
        return self.__CompleteDSLPckg_ReclassifyObjectAction

    @CompleteDSLPckg_ReclassifyObjectAction.setter
    def CompleteDSLPckg_ReclassifyObjectAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_ReclassifyObjectAction__CompleteDSLPckg_ReclassifyObjectAction", None)
        self.__CompleteDSLPckg_ReclassifyObjectAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_InputPin513"):
                opp_val = getattr(old_value, "CompleteDSLPckg_InputPin513", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_InputPin513", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_InputPin513"):
                opp_val = getattr(value, "CompleteDSLPckg_InputPin513", None)
                setattr(value, "CompleteDSLPckg_InputPin513", self)

class CompleteDSLPckg_UnmarshallAction(Action):

    pass
class CompleteDSLPckg_StructuralFeatureAction(Action):

    pass
class CompleteDSLPckg_DestroyObjectAction(Action):

    pass
class CompleteDSLPckg_CreateObjectAction(Action):

    pass
class CompleteDSLPckg_OpaqueAction(Action):

    def __init__(self, body: str, language: str, CompleteDSLPckg_OpaqueAction: set["CompleteDSLPckg_InputPin"] = None, CompleteDSLPckg_OpaqueAction401: set["CompleteDSLPckg_OutputPin"] = None):
        self.body = body
        self.language = language
        self.CompleteDSLPckg_OpaqueAction = CompleteDSLPckg_OpaqueAction if CompleteDSLPckg_OpaqueAction is not None else set()
        self.CompleteDSLPckg_OpaqueAction401 = CompleteDSLPckg_OpaqueAction401 if CompleteDSLPckg_OpaqueAction401 is not None else set()
        
        pass
    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language


    @property
    def body(self):
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body


    @property
    def CompleteDSLPckg_OpaqueAction401(self):
        return self.__CompleteDSLPckg_OpaqueAction401

    @CompleteDSLPckg_OpaqueAction401.setter
    def CompleteDSLPckg_OpaqueAction401(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_OpaqueAction__CompleteDSLPckg_OpaqueAction401", None)
        self.__CompleteDSLPckg_OpaqueAction401 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_OutputPin402"):
                    opp_val = getattr(item, "CompleteDSLPckg_OutputPin402", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_OutputPin402", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_OutputPin402"):
                    opp_val = getattr(item, "CompleteDSLPckg_OutputPin402", None)
                    
                    setattr(item, "CompleteDSLPckg_OutputPin402", self)
                    

    @property
    def CompleteDSLPckg_OpaqueAction(self):
        return self.__CompleteDSLPckg_OpaqueAction

    @CompleteDSLPckg_OpaqueAction.setter
    def CompleteDSLPckg_OpaqueAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_OpaqueAction__CompleteDSLPckg_OpaqueAction", None)
        self.__CompleteDSLPckg_OpaqueAction = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_InputPin399"):
                    opp_val = getattr(item, "CompleteDSLPckg_InputPin399", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_InputPin399", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_InputPin399"):
                    opp_val = getattr(item, "CompleteDSLPckg_InputPin399", None)
                    
                    setattr(item, "CompleteDSLPckg_InputPin399", self)
                    

class CompleteDSLPckg_SendObjectAction(InvocationAction):

    pass
class CompleteDSLPckg_InputPin(Pin):

    pass
class Artifact:

    pass
class CompleteDSLPckg_DeploymentSpecification(Artifact):

    def __init__(self, deploymentLocation: str, executionLocation: str, CompleteDSLPckg_DeploymentSpecification: "CompleteDSLPckg_Deployment" = None, CompleteDSLPckg_DeploymentSpecification390: "CompleteDSLPckg_Deployment" = None):
        self.deploymentLocation = deploymentLocation
        self.executionLocation = executionLocation
        self.CompleteDSLPckg_DeploymentSpecification = CompleteDSLPckg_DeploymentSpecification
        self.CompleteDSLPckg_DeploymentSpecification390 = CompleteDSLPckg_DeploymentSpecification390
        
        pass
    @property
    def deploymentLocation(self):
        return self.__deploymentLocation

    @deploymentLocation.setter
    def deploymentLocation(self, deploymentLocation: str):
        self.__deploymentLocation = deploymentLocation


    @property
    def executionLocation(self):
        return self.__executionLocation

    @executionLocation.setter
    def executionLocation(self, executionLocation: str):
        self.__executionLocation = executionLocation


    @property
    def CompleteDSLPckg_DeploymentSpecification390(self):
        return self.__CompleteDSLPckg_DeploymentSpecification390

    @CompleteDSLPckg_DeploymentSpecification390.setter
    def CompleteDSLPckg_DeploymentSpecification390(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_DeploymentSpecification__CompleteDSLPckg_DeploymentSpecification390", None)
        self.__CompleteDSLPckg_DeploymentSpecification390 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Deployment391"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Deployment391", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_Deployment391", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Deployment391"):
                opp_val = getattr(value, "CompleteDSLPckg_Deployment391", None)
                setattr(value, "CompleteDSLPckg_Deployment391", self)

    @property
    def CompleteDSLPckg_DeploymentSpecification(self):
        return self.__CompleteDSLPckg_DeploymentSpecification

    @CompleteDSLPckg_DeploymentSpecification.setter
    def CompleteDSLPckg_DeploymentSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_DeploymentSpecification__CompleteDSLPckg_DeploymentSpecification", None)
        self.__CompleteDSLPckg_DeploymentSpecification = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Deployment388"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Deployment388", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Deployment388"):
                opp_val = getattr(value, "CompleteDSLPckg_Deployment388", None)
                if opp_val is None:
                    setattr(value, "CompleteDSLPckg_Deployment388", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Node:

    pass
class CompleteDSLPckg_ExecutionEnvironment(Node):

    pass
class CompleteDSLPckg_Device(Node):

    pass
class CompleteDSLPckg_OutputPin(Pin):

    pass
class DeployedArtifact:

    pass
class CompleteDSLPckg_InvocationAction(ABC):

    pass
class CompleteDSLPckg_ConnectorEnd:

    pass
class Property:

    pass
class CompleteDSLPckg_Port(Property):

    def __init__(self, isBehavior: bool, isService: bool, isConjugated: bool, CompleteDSLPckg_Port: set["CompleteDSLPckg_Interface"] = None, CompleteDSLPckg_Port346: set["CompleteDSLPckg_Interface"] = None, CompleteDSLPckg_Port350: "CompleteDSLPckg_Port" = None, CompleteDSLPckg_Port348: set["CompleteDSLPckg_Port"] = None, CompleteDSLPckg_Port352: "CompleteDSLPckg_EncapsulatedClassifier" = None, CompleteDSLPckg_Port362: "CompleteDSLPckg_InvocationAction" = None):
        self.isBehavior = isBehavior
        self.isService = isService
        self.isConjugated = isConjugated
        self.CompleteDSLPckg_Port = CompleteDSLPckg_Port if CompleteDSLPckg_Port is not None else set()
        self.CompleteDSLPckg_Port346 = CompleteDSLPckg_Port346 if CompleteDSLPckg_Port346 is not None else set()
        self.CompleteDSLPckg_Port350 = CompleteDSLPckg_Port350
        self.CompleteDSLPckg_Port348 = CompleteDSLPckg_Port348 if CompleteDSLPckg_Port348 is not None else set()
        self.CompleteDSLPckg_Port352 = CompleteDSLPckg_Port352
        self.CompleteDSLPckg_Port362 = CompleteDSLPckg_Port362
        
        pass
    @property
    def isService(self):
        return self.__isService

    @isService.setter
    def isService(self, isService: bool):
        self.__isService = isService


    @property
    def isBehavior(self):
        return self.__isBehavior

    @isBehavior.setter
    def isBehavior(self, isBehavior: bool):
        self.__isBehavior = isBehavior


    @property
    def isConjugated(self):
        return self.__isConjugated

    @isConjugated.setter
    def isConjugated(self, isConjugated: bool):
        self.__isConjugated = isConjugated


    @property
    def CompleteDSLPckg_Port(self):
        return self.__CompleteDSLPckg_Port

    @CompleteDSLPckg_Port.setter
    def CompleteDSLPckg_Port(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Port__CompleteDSLPckg_Port", None)
        self.__CompleteDSLPckg_Port = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_Interface344"):
                    opp_val = getattr(item, "CompleteDSLPckg_Interface344", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_Interface344", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_Interface344"):
                    opp_val = getattr(item, "CompleteDSLPckg_Interface344", None)
                    
                    setattr(item, "CompleteDSLPckg_Interface344", self)
                    

    @property
    def CompleteDSLPckg_Port352(self):
        return self.__CompleteDSLPckg_Port352

    @CompleteDSLPckg_Port352.setter
    def CompleteDSLPckg_Port352(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Port__CompleteDSLPckg_Port352", None)
        self.__CompleteDSLPckg_Port352 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_EncapsulatedClassifier"):
                opp_val = getattr(old_value, "CompleteDSLPckg_EncapsulatedClassifier", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_EncapsulatedClassifier"):
                opp_val = getattr(value, "CompleteDSLPckg_EncapsulatedClassifier", None)
                if opp_val is None:
                    setattr(value, "CompleteDSLPckg_EncapsulatedClassifier", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CompleteDSLPckg_Port346(self):
        return self.__CompleteDSLPckg_Port346

    @CompleteDSLPckg_Port346.setter
    def CompleteDSLPckg_Port346(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Port__CompleteDSLPckg_Port346", None)
        self.__CompleteDSLPckg_Port346 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_Interface347"):
                    opp_val = getattr(item, "CompleteDSLPckg_Interface347", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_Interface347", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_Interface347"):
                    opp_val = getattr(item, "CompleteDSLPckg_Interface347", None)
                    
                    setattr(item, "CompleteDSLPckg_Interface347", self)
                    

    @property
    def CompleteDSLPckg_Port348(self):
        return self.__CompleteDSLPckg_Port348

    @CompleteDSLPckg_Port348.setter
    def CompleteDSLPckg_Port348(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Port__CompleteDSLPckg_Port348", None)
        self.__CompleteDSLPckg_Port348 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_Port350"):
                    opp_val = getattr(item, "CompleteDSLPckg_Port350", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_Port350", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_Port350"):
                    opp_val = getattr(item, "CompleteDSLPckg_Port350", None)
                    
                    setattr(item, "CompleteDSLPckg_Port350", self)
                    

    @property
    def CompleteDSLPckg_Port362(self):
        return self.__CompleteDSLPckg_Port362

    @CompleteDSLPckg_Port362.setter
    def CompleteDSLPckg_Port362(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Port__CompleteDSLPckg_Port362", None)
        self.__CompleteDSLPckg_Port362 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_InvocationAction"):
                opp_val = getattr(old_value, "CompleteDSLPckg_InvocationAction", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_InvocationAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_InvocationAction"):
                opp_val = getattr(value, "CompleteDSLPckg_InvocationAction", None)
                setattr(value, "CompleteDSLPckg_InvocationAction", self)

    @property
    def CompleteDSLPckg_Port350(self):
        return self.__CompleteDSLPckg_Port350

    @CompleteDSLPckg_Port350.setter
    def CompleteDSLPckg_Port350(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Port__CompleteDSLPckg_Port350", None)
        self.__CompleteDSLPckg_Port350 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Port348"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Port348", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Port348"):
                opp_val = getattr(value, "CompleteDSLPckg_Port348", None)
                if opp_val is None:
                    setattr(value, "CompleteDSLPckg_Port348", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class IntervalConstraint:

    pass
class CompleteDSLPckg_DurationConstraint(IntervalConstraint):

    def __init__(self, firstEvent: bool, CompleteDSLPckg_DurationConstraint: "CompleteDSLPckg_DurationInterval" = None):
        self.firstEvent = firstEvent
        self.CompleteDSLPckg_DurationConstraint = CompleteDSLPckg_DurationConstraint
        
        pass
    @property
    def firstEvent(self):
        return self.__firstEvent

    @firstEvent.setter
    def firstEvent(self, firstEvent: bool):
        self.__firstEvent = firstEvent


    @property
    def CompleteDSLPckg_DurationConstraint(self):
        return self.__CompleteDSLPckg_DurationConstraint

    @CompleteDSLPckg_DurationConstraint.setter
    def CompleteDSLPckg_DurationConstraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_DurationConstraint__CompleteDSLPckg_DurationConstraint", None)
        self.__CompleteDSLPckg_DurationConstraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_DurationInterval294"):
                opp_val = getattr(old_value, "CompleteDSLPckg_DurationInterval294", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_DurationInterval294", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_DurationInterval294"):
                opp_val = getattr(value, "CompleteDSLPckg_DurationInterval294", None)
                setattr(value, "CompleteDSLPckg_DurationInterval294", self)

class CompleteDSLPckg_TimeConstraint(IntervalConstraint):

    def __init__(self, firstEvent: bool, CompleteDSLPckg_TimeConstraint: "CompleteDSLPckg_TimeInterval" = None):
        self.firstEvent = firstEvent
        self.CompleteDSLPckg_TimeConstraint = CompleteDSLPckg_TimeConstraint
        
        pass
    @property
    def firstEvent(self):
        return self.__firstEvent

    @firstEvent.setter
    def firstEvent(self, firstEvent: bool):
        self.__firstEvent = firstEvent


    @property
    def CompleteDSLPckg_TimeConstraint(self):
        return self.__CompleteDSLPckg_TimeConstraint

    @CompleteDSLPckg_TimeConstraint.setter
    def CompleteDSLPckg_TimeConstraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_TimeConstraint__CompleteDSLPckg_TimeConstraint", None)
        self.__CompleteDSLPckg_TimeConstraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_TimeInterval292"):
                opp_val = getattr(old_value, "CompleteDSLPckg_TimeInterval292", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_TimeInterval292", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_TimeInterval292"):
                opp_val = getattr(value, "CompleteDSLPckg_TimeInterval292", None)
                setattr(value, "CompleteDSLPckg_TimeInterval292", self)

class Constraint:

    pass
class CompleteDSLPckg_IntervalConstraint(Constraint):

    pass
class Interval:

    pass
class CompleteDSLPckg_DurationInterval(Interval):

    pass
class CompleteDSLPckg_TimeInterval(Interval):

    pass
class Observation:

    pass
class CompleteDSLPckg_DurationObservation(Observation):

    def __init__(self, firstEvent: bool, CompleteDSLPckg_DurationObservation: set["CompleteDSLPckg_NamedElement"] = None):
        self.firstEvent = firstEvent
        self.CompleteDSLPckg_DurationObservation = CompleteDSLPckg_DurationObservation if CompleteDSLPckg_DurationObservation is not None else set()
        
        pass
    @property
    def firstEvent(self):
        return self.__firstEvent

    @firstEvent.setter
    def firstEvent(self, firstEvent: bool):
        self.__firstEvent = firstEvent


    @property
    def CompleteDSLPckg_DurationObservation(self):
        return self.__CompleteDSLPckg_DurationObservation

    @CompleteDSLPckg_DurationObservation.setter
    def CompleteDSLPckg_DurationObservation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_DurationObservation__CompleteDSLPckg_DurationObservation", None)
        self.__CompleteDSLPckg_DurationObservation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_NamedElement270"):
                    opp_val = getattr(item, "CompleteDSLPckg_NamedElement270", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_NamedElement270", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_NamedElement270"):
                    opp_val = getattr(item, "CompleteDSLPckg_NamedElement270", None)
                    
                    setattr(item, "CompleteDSLPckg_NamedElement270", self)
                    

class CompleteDSLPckg_TimeObservation(Observation):

    def __init__(self, firstEvent: bool, CompleteDSLPckg_TimeObservation: "CompleteDSLPckg_NamedElement" = None):
        self.firstEvent = firstEvent
        self.CompleteDSLPckg_TimeObservation = CompleteDSLPckg_TimeObservation
        
        pass
    @property
    def firstEvent(self):
        return self.__firstEvent

    @firstEvent.setter
    def firstEvent(self, firstEvent: bool):
        self.__firstEvent = firstEvent


    @property
    def CompleteDSLPckg_TimeObservation(self):
        return self.__CompleteDSLPckg_TimeObservation

    @CompleteDSLPckg_TimeObservation.setter
    def CompleteDSLPckg_TimeObservation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_TimeObservation__CompleteDSLPckg_TimeObservation", None)
        self.__CompleteDSLPckg_TimeObservation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_NamedElement268"):
                opp_val = getattr(old_value, "CompleteDSLPckg_NamedElement268", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_NamedElement268", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_NamedElement268"):
                opp_val = getattr(value, "CompleteDSLPckg_NamedElement268", None)
                setattr(value, "CompleteDSLPckg_NamedElement268", self)

class CompleteDSLPckg_TimeEvent:

    def __init__(self, isRelative: bool, CompleteDSLPckg_TimeEvent: "CompleteDSLPckg_TimeExpression" = None):
        self.isRelative = isRelative
        self.CompleteDSLPckg_TimeEvent = CompleteDSLPckg_TimeEvent
        
        pass
    @property
    def isRelative(self):
        return self.__isRelative

    @isRelative.setter
    def isRelative(self, isRelative: bool):
        self.__isRelative = isRelative


    @property
    def CompleteDSLPckg_TimeEvent(self):
        return self.__CompleteDSLPckg_TimeEvent

    @CompleteDSLPckg_TimeEvent.setter
    def CompleteDSLPckg_TimeEvent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_TimeEvent__CompleteDSLPckg_TimeEvent", None)
        self.__CompleteDSLPckg_TimeEvent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_TimeExpression"):
                opp_val = getattr(old_value, "CompleteDSLPckg_TimeExpression", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_TimeExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_TimeExpression"):
                opp_val = getattr(value, "CompleteDSLPckg_TimeExpression", None)
                setattr(value, "CompleteDSLPckg_TimeExpression", self)

class MessageEvent:

    pass
class CompleteDSLPckg_SignalEvent(MessageEvent):

    pass
class CompleteDSLPckg_CallEvent(MessageEvent):

    pass
class CompleteDSLPckg_AnyReceiveEvent(MessageEvent):

    pass
class Event:

    pass
class CompleteDSLPckg_ChangeEvent(Event):

    pass
class CompleteDSLPckg_MessageEvent(Event):

    pass
class OpaqueBehavior:

    pass
class CompleteDSLPckg_FunctionBehavior(OpaqueBehavior):

    pass
class Behavior:

    pass
class CompleteDSLPckg_OpaqueBehavior(Behavior):

    def __init__(self, body: str, language: str):
        self.body = body
        self.language = language
        
        pass
    @property
    def body(self):
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body


    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language


class Association:

    pass
class CompleteDSLPckg_CommunicationPath(Association):

    pass
class Class:

    pass
class CompleteDSLPckg_AssociationClass(Association, Class):

    pass
class Realization:

    pass
class CompleteDSLPckg_InterfaceRealization(Realization):

    pass
class CompleteDSLPckg_ComponentRealization(Realization):

    pass
class Abstraction:

    pass
class CompleteDSLPckg_Manifestation(Abstraction):

    pass
class CompleteDSLPckg_Realization(Abstraction):

    pass
class Dependency:

    pass
class CompleteDSLPckg_Abstraction(Dependency):

    pass
class CompleteDSLPckg_Deployment(Dependency):

    pass
class InteractionUse:

    pass
class MessageEnd:

    pass
class CombinedFragment:

    pass
class CompleteDSLPckg_ConsiderIgnoreFragment(CombinedFragment):

    pass
class CompleteDSLPckg_CombinedFragment:

    def __init__(self, interactionOperator: str, CompleteDSLPckg_CombinedFragment: "CompleteDSLPckg_InteractionOperand" = None, CompleteDSLPckg_CombinedFragment959: set["CompleteDSLPckg_Gate"] = None):
        self.interactionOperator = interactionOperator
        self.CompleteDSLPckg_CombinedFragment = CompleteDSLPckg_CombinedFragment
        self.CompleteDSLPckg_CombinedFragment959 = CompleteDSLPckg_CombinedFragment959 if CompleteDSLPckg_CombinedFragment959 is not None else set()
        
        pass
    @property
    def interactionOperator(self):
        return self.__interactionOperator

    @interactionOperator.setter
    def interactionOperator(self, interactionOperator: str):
        self.__interactionOperator = interactionOperator


    @property
    def CompleteDSLPckg_CombinedFragment959(self):
        return self.__CompleteDSLPckg_CombinedFragment959

    @CompleteDSLPckg_CombinedFragment959.setter
    def CompleteDSLPckg_CombinedFragment959(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_CombinedFragment__CompleteDSLPckg_CombinedFragment959", None)
        self.__CompleteDSLPckg_CombinedFragment959 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_Gate960"):
                    opp_val = getattr(item, "CompleteDSLPckg_Gate960", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_Gate960", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_Gate960"):
                    opp_val = getattr(item, "CompleteDSLPckg_Gate960", None)
                    
                    setattr(item, "CompleteDSLPckg_Gate960", self)
                    

    @property
    def CompleteDSLPckg_CombinedFragment(self):
        return self.__CompleteDSLPckg_CombinedFragment

    @CompleteDSLPckg_CombinedFragment.setter
    def CompleteDSLPckg_CombinedFragment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_CombinedFragment__CompleteDSLPckg_CombinedFragment", None)
        self.__CompleteDSLPckg_CombinedFragment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_InteractionOperand957"):
                opp_val = getattr(old_value, "CompleteDSLPckg_InteractionOperand957", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_InteractionOperand957", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_InteractionOperand957"):
                opp_val = getattr(value, "CompleteDSLPckg_InteractionOperand957", None)
                setattr(value, "CompleteDSLPckg_InteractionOperand957", self)

class CompleteDSLPckg_InteractionConstraint(Constraint):

    pass
class CompleteDSLPckg_PartDecomposition(InteractionUse):

    pass
class ExecutionSpecification:

    pass
class CompleteDSLPckg_ActionExecutionSpecification(ExecutionSpecification):

    pass
class CompleteDSLPckg_BehaviorExecutionSpecification(ExecutionSpecification):

    pass
class MessageOccurrenceSpecification:

    pass
class CompleteDSLPckg_DestructionOccurrenceSpecification(MessageOccurrenceSpecification):

    pass
class OccurenceSpecification:

    pass
class CompleteDSLPckg_MessageOccurrenceSpecification(OccurenceSpecification):

    pass
class CompleteDSLPckg_ExecutionOccurrenceSpecification(OccurenceSpecification):

    pass
class InteractionFragment:

    pass
class CompleteDSLPckg_OccurenceSpecification(InteractionFragment):

    pass
class CompleteDSLPckg_Interaction(Behavior, InteractionFragment):

    pass
class CompleteDSLPckg_InteractionUse(InteractionFragment):

    pass
class CompleteDSLPckg_StateInvariant(InteractionFragment):

    pass
class CompleteDSLPckg_Continuation(InteractionFragment):

    def __init__(self, setting: bool):
        self.setting = setting
        
        pass
    @property
    def setting(self):
        return self.__setting

    @setting.setter
    def setting(self, setting: bool):
        self.__setting = setting


class CompleteDSLPckg_ExecutionSpecification(InteractionFragment):

    pass
class CompleteDSLPckg_Gate(MessageEnd):

    pass
class ExecutableNode:

    pass
class CentralBufferNode:

    pass
class CompleteDSLPckg_DataStoreNode(CentralBufferNode):

    pass
class StructuredActivityNode:

    pass
class CompleteDSLPckg_ExpansionRegion(StructuredActivityNode):

    def __init__(self, mode: str, CompleteDSLPckg_ExpansionRegion878: "CompleteDSLPckg_ExpansionNode" = None, CompleteDSLPckg_ExpansionRegion881: "CompleteDSLPckg_ExpansionNode" = None, CompleteDSLPckg_ExpansionRegion: set["CompleteDSLPckg_ExpansionNode"] = None, CompleteDSLPckg_ExpansionRegion874: set["CompleteDSLPckg_ExpansionNode"] = None):
        self.mode = mode
        self.CompleteDSLPckg_ExpansionRegion878 = CompleteDSLPckg_ExpansionRegion878
        self.CompleteDSLPckg_ExpansionRegion881 = CompleteDSLPckg_ExpansionRegion881
        self.CompleteDSLPckg_ExpansionRegion = CompleteDSLPckg_ExpansionRegion if CompleteDSLPckg_ExpansionRegion is not None else set()
        self.CompleteDSLPckg_ExpansionRegion874 = CompleteDSLPckg_ExpansionRegion874 if CompleteDSLPckg_ExpansionRegion874 is not None else set()
        
        pass
    @property
    def mode(self):
        return self.__mode

    @mode.setter
    def mode(self, mode: str):
        self.__mode = mode


    @property
    def CompleteDSLPckg_ExpansionRegion(self):
        return self.__CompleteDSLPckg_ExpansionRegion

    @CompleteDSLPckg_ExpansionRegion.setter
    def CompleteDSLPckg_ExpansionRegion(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_ExpansionRegion__CompleteDSLPckg_ExpansionRegion", None)
        self.__CompleteDSLPckg_ExpansionRegion = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_ExpansionNode"):
                    opp_val = getattr(item, "CompleteDSLPckg_ExpansionNode", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_ExpansionNode", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_ExpansionNode"):
                    opp_val = getattr(item, "CompleteDSLPckg_ExpansionNode", None)
                    
                    setattr(item, "CompleteDSLPckg_ExpansionNode", self)
                    

    @property
    def CompleteDSLPckg_ExpansionRegion881(self):
        return self.__CompleteDSLPckg_ExpansionRegion881

    @CompleteDSLPckg_ExpansionRegion881.setter
    def CompleteDSLPckg_ExpansionRegion881(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_ExpansionRegion__CompleteDSLPckg_ExpansionRegion881", None)
        self.__CompleteDSLPckg_ExpansionRegion881 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_ExpansionNode880"):
                opp_val = getattr(old_value, "CompleteDSLPckg_ExpansionNode880", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_ExpansionNode880", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_ExpansionNode880"):
                opp_val = getattr(value, "CompleteDSLPckg_ExpansionNode880", None)
                setattr(value, "CompleteDSLPckg_ExpansionNode880", self)

    @property
    def CompleteDSLPckg_ExpansionRegion874(self):
        return self.__CompleteDSLPckg_ExpansionRegion874

    @CompleteDSLPckg_ExpansionRegion874.setter
    def CompleteDSLPckg_ExpansionRegion874(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_ExpansionRegion__CompleteDSLPckg_ExpansionRegion874", None)
        self.__CompleteDSLPckg_ExpansionRegion874 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_ExpansionNode875"):
                    opp_val = getattr(item, "CompleteDSLPckg_ExpansionNode875", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_ExpansionNode875", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_ExpansionNode875"):
                    opp_val = getattr(item, "CompleteDSLPckg_ExpansionNode875", None)
                    
                    setattr(item, "CompleteDSLPckg_ExpansionNode875", self)
                    

    @property
    def CompleteDSLPckg_ExpansionRegion878(self):
        return self.__CompleteDSLPckg_ExpansionRegion878

    @CompleteDSLPckg_ExpansionRegion878.setter
    def CompleteDSLPckg_ExpansionRegion878(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_ExpansionRegion__CompleteDSLPckg_ExpansionRegion878", None)
        self.__CompleteDSLPckg_ExpansionRegion878 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_ExpansionNode877"):
                opp_val = getattr(old_value, "CompleteDSLPckg_ExpansionNode877", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_ExpansionNode877", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_ExpansionNode877"):
                opp_val = getattr(value, "CompleteDSLPckg_ExpansionNode877", None)
                setattr(value, "CompleteDSLPckg_ExpansionNode877", self)

class CompleteDSLPckg_SequenceNode(StructuredActivityNode):

    pass
class CompleteDSLPckg_ConditionalNode(StructuredActivityNode):

    def __init__(self, isDeterminate: bool, isAssumed: bool, CompleteDSLPckg_ConditionalNode: set["CompleteDSLPckg_Clause"] = None, CompleteDSLPckg_ConditionalNode842: set["CompleteDSLPckg_ExecutableNode"] = None, CompleteDSLPckg_ConditionalNode845: set["CompleteDSLPckg_ExecutableNode"] = None, CompleteDSLPckg_ConditionalNode848: set["CompleteDSLPckg_OutputPin"] = None):
        self.isDeterminate = isDeterminate
        self.isAssumed = isAssumed
        self.CompleteDSLPckg_ConditionalNode = CompleteDSLPckg_ConditionalNode if CompleteDSLPckg_ConditionalNode is not None else set()
        self.CompleteDSLPckg_ConditionalNode842 = CompleteDSLPckg_ConditionalNode842 if CompleteDSLPckg_ConditionalNode842 is not None else set()
        self.CompleteDSLPckg_ConditionalNode845 = CompleteDSLPckg_ConditionalNode845 if CompleteDSLPckg_ConditionalNode845 is not None else set()
        self.CompleteDSLPckg_ConditionalNode848 = CompleteDSLPckg_ConditionalNode848 if CompleteDSLPckg_ConditionalNode848 is not None else set()
        
        pass
    @property
    def isAssumed(self):
        return self.__isAssumed

    @isAssumed.setter
    def isAssumed(self, isAssumed: bool):
        self.__isAssumed = isAssumed


    @property
    def isDeterminate(self):
        return self.__isDeterminate

    @isDeterminate.setter
    def isDeterminate(self, isDeterminate: bool):
        self.__isDeterminate = isDeterminate


    @property
    def CompleteDSLPckg_ConditionalNode848(self):
        return self.__CompleteDSLPckg_ConditionalNode848

    @CompleteDSLPckg_ConditionalNode848.setter
    def CompleteDSLPckg_ConditionalNode848(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_ConditionalNode__CompleteDSLPckg_ConditionalNode848", None)
        self.__CompleteDSLPckg_ConditionalNode848 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_OutputPin849"):
                    opp_val = getattr(item, "CompleteDSLPckg_OutputPin849", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_OutputPin849", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_OutputPin849"):
                    opp_val = getattr(item, "CompleteDSLPckg_OutputPin849", None)
                    
                    setattr(item, "CompleteDSLPckg_OutputPin849", self)
                    

    @property
    def CompleteDSLPckg_ConditionalNode845(self):
        return self.__CompleteDSLPckg_ConditionalNode845

    @CompleteDSLPckg_ConditionalNode845.setter
    def CompleteDSLPckg_ConditionalNode845(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_ConditionalNode__CompleteDSLPckg_ConditionalNode845", None)
        self.__CompleteDSLPckg_ConditionalNode845 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_ExecutableNode846"):
                    opp_val = getattr(item, "CompleteDSLPckg_ExecutableNode846", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_ExecutableNode846", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_ExecutableNode846"):
                    opp_val = getattr(item, "CompleteDSLPckg_ExecutableNode846", None)
                    
                    setattr(item, "CompleteDSLPckg_ExecutableNode846", self)
                    

    @property
    def CompleteDSLPckg_ConditionalNode842(self):
        return self.__CompleteDSLPckg_ConditionalNode842

    @CompleteDSLPckg_ConditionalNode842.setter
    def CompleteDSLPckg_ConditionalNode842(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_ConditionalNode__CompleteDSLPckg_ConditionalNode842", None)
        self.__CompleteDSLPckg_ConditionalNode842 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_ExecutableNode843"):
                    opp_val = getattr(item, "CompleteDSLPckg_ExecutableNode843", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_ExecutableNode843", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_ExecutableNode843"):
                    opp_val = getattr(item, "CompleteDSLPckg_ExecutableNode843", None)
                    
                    setattr(item, "CompleteDSLPckg_ExecutableNode843", self)
                    

    @property
    def CompleteDSLPckg_ConditionalNode(self):
        return self.__CompleteDSLPckg_ConditionalNode

    @CompleteDSLPckg_ConditionalNode.setter
    def CompleteDSLPckg_ConditionalNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_ConditionalNode__CompleteDSLPckg_ConditionalNode", None)
        self.__CompleteDSLPckg_ConditionalNode = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_Clause"):
                    opp_val = getattr(item, "CompleteDSLPckg_Clause", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_Clause", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_Clause"):
                    opp_val = getattr(item, "CompleteDSLPckg_Clause", None)
                    
                    setattr(item, "CompleteDSLPckg_Clause", self)
                    

class CompleteDSLPckg_LoopNode(StructuredActivityNode):

    def __init__(self, isTestedFirst: bool, CompleteDSLPckg_LoopNode: set["CompleteDSLPckg_ExecutableNode"] = None, CompleteDSLPckg_LoopNode820: set["CompleteDSLPckg_ExecutableNode"] = None, CompleteDSLPckg_LoopNode823: set["CompleteDSLPckg_ExecutableNode"] = None, CompleteDSLPckg_LoopNode826: "CompleteDSLPckg_OutputPin" = None, CompleteDSLPckg_LoopNode829: set["CompleteDSLPckg_InputPin"] = None, CompleteDSLPckg_LoopNode832: set["CompleteDSLPckg_OutputPin"] = None, CompleteDSLPckg_LoopNode835: set["CompleteDSLPckg_OutputPin"] = None, CompleteDSLPckg_LoopNode838: set["CompleteDSLPckg_OutputPin"] = None):
        self.isTestedFirst = isTestedFirst
        self.CompleteDSLPckg_LoopNode = CompleteDSLPckg_LoopNode if CompleteDSLPckg_LoopNode is not None else set()
        self.CompleteDSLPckg_LoopNode820 = CompleteDSLPckg_LoopNode820 if CompleteDSLPckg_LoopNode820 is not None else set()
        self.CompleteDSLPckg_LoopNode823 = CompleteDSLPckg_LoopNode823 if CompleteDSLPckg_LoopNode823 is not None else set()
        self.CompleteDSLPckg_LoopNode826 = CompleteDSLPckg_LoopNode826
        self.CompleteDSLPckg_LoopNode829 = CompleteDSLPckg_LoopNode829 if CompleteDSLPckg_LoopNode829 is not None else set()
        self.CompleteDSLPckg_LoopNode832 = CompleteDSLPckg_LoopNode832 if CompleteDSLPckg_LoopNode832 is not None else set()
        self.CompleteDSLPckg_LoopNode835 = CompleteDSLPckg_LoopNode835 if CompleteDSLPckg_LoopNode835 is not None else set()
        self.CompleteDSLPckg_LoopNode838 = CompleteDSLPckg_LoopNode838 if CompleteDSLPckg_LoopNode838 is not None else set()
        
        pass
    @property
    def isTestedFirst(self):
        return self.__isTestedFirst

    @isTestedFirst.setter
    def isTestedFirst(self, isTestedFirst: bool):
        self.__isTestedFirst = isTestedFirst


    @property
    def CompleteDSLPckg_LoopNode832(self):
        return self.__CompleteDSLPckg_LoopNode832

    @CompleteDSLPckg_LoopNode832.setter
    def CompleteDSLPckg_LoopNode832(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_LoopNode__CompleteDSLPckg_LoopNode832", None)
        self.__CompleteDSLPckg_LoopNode832 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_OutputPin833"):
                    opp_val = getattr(item, "CompleteDSLPckg_OutputPin833", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_OutputPin833", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_OutputPin833"):
                    opp_val = getattr(item, "CompleteDSLPckg_OutputPin833", None)
                    
                    setattr(item, "CompleteDSLPckg_OutputPin833", self)
                    

    @property
    def CompleteDSLPckg_LoopNode820(self):
        return self.__CompleteDSLPckg_LoopNode820

    @CompleteDSLPckg_LoopNode820.setter
    def CompleteDSLPckg_LoopNode820(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_LoopNode__CompleteDSLPckg_LoopNode820", None)
        self.__CompleteDSLPckg_LoopNode820 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_ExecutableNode821"):
                    opp_val = getattr(item, "CompleteDSLPckg_ExecutableNode821", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_ExecutableNode821", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_ExecutableNode821"):
                    opp_val = getattr(item, "CompleteDSLPckg_ExecutableNode821", None)
                    
                    setattr(item, "CompleteDSLPckg_ExecutableNode821", self)
                    

    @property
    def CompleteDSLPckg_LoopNode(self):
        return self.__CompleteDSLPckg_LoopNode

    @CompleteDSLPckg_LoopNode.setter
    def CompleteDSLPckg_LoopNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_LoopNode__CompleteDSLPckg_LoopNode", None)
        self.__CompleteDSLPckg_LoopNode = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_ExecutableNode818"):
                    opp_val = getattr(item, "CompleteDSLPckg_ExecutableNode818", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_ExecutableNode818", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_ExecutableNode818"):
                    opp_val = getattr(item, "CompleteDSLPckg_ExecutableNode818", None)
                    
                    setattr(item, "CompleteDSLPckg_ExecutableNode818", self)
                    

    @property
    def CompleteDSLPckg_LoopNode829(self):
        return self.__CompleteDSLPckg_LoopNode829

    @CompleteDSLPckg_LoopNode829.setter
    def CompleteDSLPckg_LoopNode829(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_LoopNode__CompleteDSLPckg_LoopNode829", None)
        self.__CompleteDSLPckg_LoopNode829 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_InputPin830"):
                    opp_val = getattr(item, "CompleteDSLPckg_InputPin830", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_InputPin830", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_InputPin830"):
                    opp_val = getattr(item, "CompleteDSLPckg_InputPin830", None)
                    
                    setattr(item, "CompleteDSLPckg_InputPin830", self)
                    

    @property
    def CompleteDSLPckg_LoopNode838(self):
        return self.__CompleteDSLPckg_LoopNode838

    @CompleteDSLPckg_LoopNode838.setter
    def CompleteDSLPckg_LoopNode838(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_LoopNode__CompleteDSLPckg_LoopNode838", None)
        self.__CompleteDSLPckg_LoopNode838 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_OutputPin839"):
                    opp_val = getattr(item, "CompleteDSLPckg_OutputPin839", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_OutputPin839", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_OutputPin839"):
                    opp_val = getattr(item, "CompleteDSLPckg_OutputPin839", None)
                    
                    setattr(item, "CompleteDSLPckg_OutputPin839", self)
                    

    @property
    def CompleteDSLPckg_LoopNode835(self):
        return self.__CompleteDSLPckg_LoopNode835

    @CompleteDSLPckg_LoopNode835.setter
    def CompleteDSLPckg_LoopNode835(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_LoopNode__CompleteDSLPckg_LoopNode835", None)
        self.__CompleteDSLPckg_LoopNode835 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_OutputPin836"):
                    opp_val = getattr(item, "CompleteDSLPckg_OutputPin836", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_OutputPin836", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_OutputPin836"):
                    opp_val = getattr(item, "CompleteDSLPckg_OutputPin836", None)
                    
                    setattr(item, "CompleteDSLPckg_OutputPin836", self)
                    

    @property
    def CompleteDSLPckg_LoopNode823(self):
        return self.__CompleteDSLPckg_LoopNode823

    @CompleteDSLPckg_LoopNode823.setter
    def CompleteDSLPckg_LoopNode823(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_LoopNode__CompleteDSLPckg_LoopNode823", None)
        self.__CompleteDSLPckg_LoopNode823 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_ExecutableNode824"):
                    opp_val = getattr(item, "CompleteDSLPckg_ExecutableNode824", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_ExecutableNode824", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_ExecutableNode824"):
                    opp_val = getattr(item, "CompleteDSLPckg_ExecutableNode824", None)
                    
                    setattr(item, "CompleteDSLPckg_ExecutableNode824", self)
                    

    @property
    def CompleteDSLPckg_LoopNode826(self):
        return self.__CompleteDSLPckg_LoopNode826

    @CompleteDSLPckg_LoopNode826.setter
    def CompleteDSLPckg_LoopNode826(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_LoopNode__CompleteDSLPckg_LoopNode826", None)
        self.__CompleteDSLPckg_LoopNode826 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_OutputPin827"):
                opp_val = getattr(old_value, "CompleteDSLPckg_OutputPin827", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_OutputPin827", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_OutputPin827"):
                opp_val = getattr(value, "CompleteDSLPckg_OutputPin827", None)
                setattr(value, "CompleteDSLPckg_OutputPin827", self)

class ActivityEdge:

    pass
class CompleteDSLPckg_ObjectFlow(ActivityEdge):

    def __init__(self, isMulticast: bool, isMultireceive: bool, ordering: str, isControlType: bool, CompleteDSLPckg_ObjectFlow: "CompleteDSLPckg_Behavior" = None, CompleteDSLPckg_ObjectFlow760: "CompleteDSLPckg_Behavior" = None, CompleteDSLPckg_ObjectFlow763: set["CompleteDSLPckg_State"] = None, CompleteDSLPckg_ObjectFlow768: "CompleteDSLPckg_DecisionNode" = None):
        self.isMulticast = isMulticast
        self.isMultireceive = isMultireceive
        self.ordering = ordering
        self.isControlType = isControlType
        self.CompleteDSLPckg_ObjectFlow = CompleteDSLPckg_ObjectFlow
        self.CompleteDSLPckg_ObjectFlow760 = CompleteDSLPckg_ObjectFlow760
        self.CompleteDSLPckg_ObjectFlow763 = CompleteDSLPckg_ObjectFlow763 if CompleteDSLPckg_ObjectFlow763 is not None else set()
        self.CompleteDSLPckg_ObjectFlow768 = CompleteDSLPckg_ObjectFlow768
        
        pass
    @property
    def ordering(self):
        return self.__ordering

    @ordering.setter
    def ordering(self, ordering: str):
        self.__ordering = ordering


    @property
    def isControlType(self):
        return self.__isControlType

    @isControlType.setter
    def isControlType(self, isControlType: bool):
        self.__isControlType = isControlType


    @property
    def isMulticast(self):
        return self.__isMulticast

    @isMulticast.setter
    def isMulticast(self, isMulticast: bool):
        self.__isMulticast = isMulticast


    @property
    def isMultireceive(self):
        return self.__isMultireceive

    @isMultireceive.setter
    def isMultireceive(self, isMultireceive: bool):
        self.__isMultireceive = isMultireceive


    @property
    def CompleteDSLPckg_ObjectFlow768(self):
        return self.__CompleteDSLPckg_ObjectFlow768

    @CompleteDSLPckg_ObjectFlow768.setter
    def CompleteDSLPckg_ObjectFlow768(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_ObjectFlow__CompleteDSLPckg_ObjectFlow768", None)
        self.__CompleteDSLPckg_ObjectFlow768 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_DecisionNode"):
                opp_val = getattr(old_value, "CompleteDSLPckg_DecisionNode", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_DecisionNode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_DecisionNode"):
                opp_val = getattr(value, "CompleteDSLPckg_DecisionNode", None)
                setattr(value, "CompleteDSLPckg_DecisionNode", self)

    @property
    def CompleteDSLPckg_ObjectFlow763(self):
        return self.__CompleteDSLPckg_ObjectFlow763

    @CompleteDSLPckg_ObjectFlow763.setter
    def CompleteDSLPckg_ObjectFlow763(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_ObjectFlow__CompleteDSLPckg_ObjectFlow763", None)
        self.__CompleteDSLPckg_ObjectFlow763 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_State764"):
                    opp_val = getattr(item, "CompleteDSLPckg_State764", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_State764", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_State764"):
                    opp_val = getattr(item, "CompleteDSLPckg_State764", None)
                    
                    setattr(item, "CompleteDSLPckg_State764", self)
                    

    @property
    def CompleteDSLPckg_ObjectFlow(self):
        return self.__CompleteDSLPckg_ObjectFlow

    @CompleteDSLPckg_ObjectFlow.setter
    def CompleteDSLPckg_ObjectFlow(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_ObjectFlow__CompleteDSLPckg_ObjectFlow", None)
        self.__CompleteDSLPckg_ObjectFlow = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Behavior758"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Behavior758", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_Behavior758", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Behavior758"):
                opp_val = getattr(value, "CompleteDSLPckg_Behavior758", None)
                setattr(value, "CompleteDSLPckg_Behavior758", self)

    @property
    def CompleteDSLPckg_ObjectFlow760(self):
        return self.__CompleteDSLPckg_ObjectFlow760

    @CompleteDSLPckg_ObjectFlow760.setter
    def CompleteDSLPckg_ObjectFlow760(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_ObjectFlow__CompleteDSLPckg_ObjectFlow760", None)
        self.__CompleteDSLPckg_ObjectFlow760 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Behavior761"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Behavior761", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_Behavior761", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Behavior761"):
                opp_val = getattr(value, "CompleteDSLPckg_Behavior761", None)
                setattr(value, "CompleteDSLPckg_Behavior761", self)

class CompleteDSLPckg_ControlFlow(ActivityEdge):

    pass
class ActivityGroup:

    pass
class FinalNode:

    pass
class CompleteDSLPckg_FlowFinalNode(FinalNode):

    pass
class ControlNode:

    pass
class CompleteDSLPckg_FinalNode(ControlNode):

    pass
class CompleteDSLPckg_DecisionNode(ControlNode):

    pass
class CompleteDSLPckg_JoinNode(ControlNode):

    def __init__(self, isCombineDuplicate: bool, CompleteDSLPckg_JoinNode: "CompleteDSLPckg_ValueSpecification" = None):
        self.isCombineDuplicate = isCombineDuplicate
        self.CompleteDSLPckg_JoinNode = CompleteDSLPckg_JoinNode
        
        pass
    @property
    def isCombineDuplicate(self):
        return self.__isCombineDuplicate

    @isCombineDuplicate.setter
    def isCombineDuplicate(self, isCombineDuplicate: bool):
        self.__isCombineDuplicate = isCombineDuplicate


    @property
    def CompleteDSLPckg_JoinNode(self):
        return self.__CompleteDSLPckg_JoinNode

    @CompleteDSLPckg_JoinNode.setter
    def CompleteDSLPckg_JoinNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_JoinNode__CompleteDSLPckg_JoinNode", None)
        self.__CompleteDSLPckg_JoinNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_ValueSpecification766"):
                opp_val = getattr(old_value, "CompleteDSLPckg_ValueSpecification766", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_ValueSpecification766", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_ValueSpecification766"):
                opp_val = getattr(value, "CompleteDSLPckg_ValueSpecification766", None)
                setattr(value, "CompleteDSLPckg_ValueSpecification766", self)

class CompleteDSLPckg_ForkNode(ControlNode):

    pass
class CompleteDSLPckg_MergeNode(ControlNode):

    pass
class CompleteDSLPckg_InitialNode(ControlNode):

    pass
class CompleteDSLPckg_ActivityFinalNode(ControlNode, FinalNode):

    pass
class ObjectNode:

    pass
class CompleteDSLPckg_CentralBufferNode(ObjectNode):

    pass
class CompleteDSLPckg_ExpansionNode(ObjectNode):

    pass
class CompleteDSLPckg_ActivityParameterNode(ObjectNode):

    pass
class ActivityNode:

    pass
class CompleteDSLPckg_ExecutableNode(ActivityNode):

    pass
class CompleteDSLPckg_ControlNode(ActivityNode):

    pass
class CompleteDSLPckg_ActivityPartition(ActivityGroup):

    pass
class CompleteDSLPckg_Activity(Behavior):

    def __init__(self, isReadOnly: bool, isSingleExecution: bool, CompleteDSLPckg_Activity689: set["CompleteDSLPckg_StructuredActivityNode"] = None, CompleteDSLPckg_Activity691: set["CompleteDSLPckg_Variable"] = None, CompleteDSLPckg_Activity721: "CompleteDSLPckg_ActivityGroup" = None, CompleteDSLPckg_Activity: set["CompleteDSLPckg_ActivityNode"] = None, CompleteDSLPckg_Activity683: set["CompleteDSLPckg_ActivityGroup"] = None, CompleteDSLPckg_Activity685: set["CompleteDSLPckg_ActivityEdge"] = None, CompleteDSLPckg_Activity687: set["CompleteDSLPckg_ActivityPartition"] = None, CompleteDSLPckg_Activity800: "CompleteDSLPckg_StructuredActivityNode" = None):
        self.isReadOnly = isReadOnly
        self.isSingleExecution = isSingleExecution
        self.CompleteDSLPckg_Activity689 = CompleteDSLPckg_Activity689 if CompleteDSLPckg_Activity689 is not None else set()
        self.CompleteDSLPckg_Activity691 = CompleteDSLPckg_Activity691 if CompleteDSLPckg_Activity691 is not None else set()
        self.CompleteDSLPckg_Activity721 = CompleteDSLPckg_Activity721
        self.CompleteDSLPckg_Activity = CompleteDSLPckg_Activity if CompleteDSLPckg_Activity is not None else set()
        self.CompleteDSLPckg_Activity683 = CompleteDSLPckg_Activity683 if CompleteDSLPckg_Activity683 is not None else set()
        self.CompleteDSLPckg_Activity685 = CompleteDSLPckg_Activity685 if CompleteDSLPckg_Activity685 is not None else set()
        self.CompleteDSLPckg_Activity687 = CompleteDSLPckg_Activity687 if CompleteDSLPckg_Activity687 is not None else set()
        self.CompleteDSLPckg_Activity800 = CompleteDSLPckg_Activity800
        
        pass
    @property
    def isSingleExecution(self):
        return self.__isSingleExecution

    @isSingleExecution.setter
    def isSingleExecution(self, isSingleExecution: bool):
        self.__isSingleExecution = isSingleExecution


    @property
    def isReadOnly(self):
        return self.__isReadOnly

    @isReadOnly.setter
    def isReadOnly(self, isReadOnly: bool):
        self.__isReadOnly = isReadOnly


    @property
    def CompleteDSLPckg_Activity(self):
        return self.__CompleteDSLPckg_Activity

    @CompleteDSLPckg_Activity.setter
    def CompleteDSLPckg_Activity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Activity__CompleteDSLPckg_Activity", None)
        self.__CompleteDSLPckg_Activity = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_ActivityNode"):
                    opp_val = getattr(item, "CompleteDSLPckg_ActivityNode", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_ActivityNode", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_ActivityNode"):
                    opp_val = getattr(item, "CompleteDSLPckg_ActivityNode", None)
                    
                    setattr(item, "CompleteDSLPckg_ActivityNode", self)
                    

    @property
    def CompleteDSLPckg_Activity800(self):
        return self.__CompleteDSLPckg_Activity800

    @CompleteDSLPckg_Activity800.setter
    def CompleteDSLPckg_Activity800(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Activity__CompleteDSLPckg_Activity800", None)
        self.__CompleteDSLPckg_Activity800 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_StructuredActivityNode799"):
                opp_val = getattr(old_value, "CompleteDSLPckg_StructuredActivityNode799", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_StructuredActivityNode799", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_StructuredActivityNode799"):
                opp_val = getattr(value, "CompleteDSLPckg_StructuredActivityNode799", None)
                setattr(value, "CompleteDSLPckg_StructuredActivityNode799", self)

    @property
    def CompleteDSLPckg_Activity687(self):
        return self.__CompleteDSLPckg_Activity687

    @CompleteDSLPckg_Activity687.setter
    def CompleteDSLPckg_Activity687(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Activity__CompleteDSLPckg_Activity687", None)
        self.__CompleteDSLPckg_Activity687 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_ActivityPartition"):
                    opp_val = getattr(item, "CompleteDSLPckg_ActivityPartition", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_ActivityPartition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_ActivityPartition"):
                    opp_val = getattr(item, "CompleteDSLPckg_ActivityPartition", None)
                    
                    setattr(item, "CompleteDSLPckg_ActivityPartition", self)
                    

    @property
    def CompleteDSLPckg_Activity721(self):
        return self.__CompleteDSLPckg_Activity721

    @CompleteDSLPckg_Activity721.setter
    def CompleteDSLPckg_Activity721(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Activity__CompleteDSLPckg_Activity721", None)
        self.__CompleteDSLPckg_Activity721 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_ActivityGroup720"):
                opp_val = getattr(old_value, "CompleteDSLPckg_ActivityGroup720", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_ActivityGroup720", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_ActivityGroup720"):
                opp_val = getattr(value, "CompleteDSLPckg_ActivityGroup720", None)
                setattr(value, "CompleteDSLPckg_ActivityGroup720", self)

    @property
    def CompleteDSLPckg_Activity689(self):
        return self.__CompleteDSLPckg_Activity689

    @CompleteDSLPckg_Activity689.setter
    def CompleteDSLPckg_Activity689(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Activity__CompleteDSLPckg_Activity689", None)
        self.__CompleteDSLPckg_Activity689 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_StructuredActivityNode"):
                    opp_val = getattr(item, "CompleteDSLPckg_StructuredActivityNode", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_StructuredActivityNode", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_StructuredActivityNode"):
                    opp_val = getattr(item, "CompleteDSLPckg_StructuredActivityNode", None)
                    
                    setattr(item, "CompleteDSLPckg_StructuredActivityNode", self)
                    

    @property
    def CompleteDSLPckg_Activity691(self):
        return self.__CompleteDSLPckg_Activity691

    @CompleteDSLPckg_Activity691.setter
    def CompleteDSLPckg_Activity691(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Activity__CompleteDSLPckg_Activity691", None)
        self.__CompleteDSLPckg_Activity691 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_Variable692"):
                    opp_val = getattr(item, "CompleteDSLPckg_Variable692", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_Variable692", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_Variable692"):
                    opp_val = getattr(item, "CompleteDSLPckg_Variable692", None)
                    
                    setattr(item, "CompleteDSLPckg_Variable692", self)
                    

    @property
    def CompleteDSLPckg_Activity685(self):
        return self.__CompleteDSLPckg_Activity685

    @CompleteDSLPckg_Activity685.setter
    def CompleteDSLPckg_Activity685(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Activity__CompleteDSLPckg_Activity685", None)
        self.__CompleteDSLPckg_Activity685 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_ActivityEdge"):
                    opp_val = getattr(item, "CompleteDSLPckg_ActivityEdge", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_ActivityEdge", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_ActivityEdge"):
                    opp_val = getattr(item, "CompleteDSLPckg_ActivityEdge", None)
                    
                    setattr(item, "CompleteDSLPckg_ActivityEdge", self)
                    

    @property
    def CompleteDSLPckg_Activity683(self):
        return self.__CompleteDSLPckg_Activity683

    @CompleteDSLPckg_Activity683.setter
    def CompleteDSLPckg_Activity683(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Activity__CompleteDSLPckg_Activity683", None)
        self.__CompleteDSLPckg_Activity683 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_ActivityGroup"):
                    opp_val = getattr(item, "CompleteDSLPckg_ActivityGroup", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_ActivityGroup", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_ActivityGroup"):
                    opp_val = getattr(item, "CompleteDSLPckg_ActivityGroup", None)
                    
                    setattr(item, "CompleteDSLPckg_ActivityGroup", self)
                    

class Transition:

    pass
class CompleteDSLPckg_ProtocolTransition(Transition):

    pass
class CompleteDSLPckg_InterruptibleActivityRegion(ActivityGroup):

    pass
class StateMachine:

    pass
class CompleteDSLPckg_ProtocolStateMachine(StateMachine):

    pass
class State:

    pass
class CompleteDSLPckg_FinalState(State):

    pass
class Vertex:

    pass
class CompleteDSLPckg_ConnectionPointReference(Vertex):

    pass
class CompleteDSLPckg_ActionInputPin(InputPin):

    pass
class CompleteDSLPckg_RaiseExceptionAction(Action):

    pass
class WriteVariableAction:

    pass
class CompleteDSLPckg_RemoveVariableValueAction(WriteVariableAction):

    pass
class CompleteDSLPckg_AddVariableValueAction(WriteVariableAction):

    pass
class VariableAction:

    pass
class CompleteDSLPckg_WriteVariableAction(VariableAction):

    pass
class CompleteDSLPckg_ClearVariableAction(VariableAction):

    pass
class CompleteDSLPckg_ReadVariableAction(VariableAction):

    pass
class CompleteDSLPckg_Pseudostate(Vertex):

    pass
class CompleteDSLPckg_StateMachine(Behavior):

    pass
class CompleteDSLPckg_ReduceAction(Action):

    def __init__(self, isOrdered: bool, CompleteDSLPckg_ReduceAction559: "CompleteDSLPckg_Behavior" = None, CompleteDSLPckg_ReduceAction: "CompleteDSLPckg_OutputPin" = None, CompleteDSLPckg_ReduceAction556: "CompleteDSLPckg_InputPin" = None):
        self.isOrdered = isOrdered
        self.CompleteDSLPckg_ReduceAction559 = CompleteDSLPckg_ReduceAction559
        self.CompleteDSLPckg_ReduceAction = CompleteDSLPckg_ReduceAction
        self.CompleteDSLPckg_ReduceAction556 = CompleteDSLPckg_ReduceAction556
        
        pass
    @property
    def isOrdered(self):
        return self.__isOrdered

    @isOrdered.setter
    def isOrdered(self, isOrdered: bool):
        self.__isOrdered = isOrdered


    @property
    def CompleteDSLPckg_ReduceAction556(self):
        return self.__CompleteDSLPckg_ReduceAction556

    @CompleteDSLPckg_ReduceAction556.setter
    def CompleteDSLPckg_ReduceAction556(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_ReduceAction__CompleteDSLPckg_ReduceAction556", None)
        self.__CompleteDSLPckg_ReduceAction556 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_InputPin557"):
                opp_val = getattr(old_value, "CompleteDSLPckg_InputPin557", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_InputPin557", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_InputPin557"):
                opp_val = getattr(value, "CompleteDSLPckg_InputPin557", None)
                setattr(value, "CompleteDSLPckg_InputPin557", self)

    @property
    def CompleteDSLPckg_ReduceAction559(self):
        return self.__CompleteDSLPckg_ReduceAction559

    @CompleteDSLPckg_ReduceAction559.setter
    def CompleteDSLPckg_ReduceAction559(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_ReduceAction__CompleteDSLPckg_ReduceAction559", None)
        self.__CompleteDSLPckg_ReduceAction559 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Behavior560"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Behavior560", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_Behavior560", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Behavior560"):
                opp_val = getattr(value, "CompleteDSLPckg_Behavior560", None)
                setattr(value, "CompleteDSLPckg_Behavior560", self)

    @property
    def CompleteDSLPckg_ReduceAction(self):
        return self.__CompleteDSLPckg_ReduceAction

    @CompleteDSLPckg_ReduceAction.setter
    def CompleteDSLPckg_ReduceAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_ReduceAction__CompleteDSLPckg_ReduceAction", None)
        self.__CompleteDSLPckg_ReduceAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_OutputPin554"):
                opp_val = getattr(old_value, "CompleteDSLPckg_OutputPin554", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_OutputPin554", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_OutputPin554"):
                opp_val = getattr(value, "CompleteDSLPckg_OutputPin554", None)
                setattr(value, "CompleteDSLPckg_OutputPin554", self)

class CompleteDSLPckg_VariableAction(Action):

    pass
class CreateLinkAction:

    pass
class CompleteDSLPckg_CreateLinkObjectAction(CreateLinkAction):

    pass
class CompleteDSLPckg_ReadLinkObjectEndQualifierAction(Action):

    pass
class CompleteDSLPckg_ReadLinkObjectEndAction(Action):

    pass
class CompleteDSLPckg_StartObjectBehaviorAction(CallAction):

    pass
class CompleteDSLPckg_StartClassifierBehaviorAction(Action):

    pass
class CompleteDSLPckg_ReadlsClassifiedObjectAction:

    pass
class CompleteDSLPckg_Usage(Dependency):

    pass
class InstanceSpecification:

    pass
class CompleteDSLPckg_EnumerationLiteral(InstanceSpecification):

    pass
class DataType:

    pass
class CompleteDSLPckg_Enumeration(DataType):

    pass
class CompleteDSLPckg_PrimitiveType(DataType):

    pass
class EncapsulatedClassifier:

    pass
class StructuredClassifier:

    pass
class CompleteDSLPckg_EncapsulatedClassifier(StructuredClassifier):

    pass
class BehavioredClassifier:

    pass
class CompleteDSLPckg_Collaboration(StructuredClassifier, BehavioredClassifier):

    pass
class CompleteDSLPckg_UseCase(BehavioredClassifier):

    pass
class CompleteDSLPckg_Actor(BehavioredClassifier):

    pass
class Classifier:

    pass
class CompleteDSLPckg_BehavioredClassifier(Classifier):

    pass
class CompleteDSLPckg_Signal(Classifier):

    pass
class CompleteDSLPckg_StructuredClassifier(Classifier):

    pass
class BehavioralFeature:

    pass
class CompleteDSLPckg_Reception(BehavioralFeature):

    pass
class CompleteDSLPckg_Operation(BehavioralFeature):

    def __init__(self, isQuery: bool, isOrdered: bool, isUnique: bool, upper: int, lower: int, Operation188: "CompleteDSLPckg_DataType" = None, ownedOperation162: "CompleteDSLPckg_DataType" = None, CompleteDSLPckg_Operation: "CompleteDSLPckg_Type" = None, CompleteDSLPckg_Operation151: set["CompleteDSLPckg_Constraint"] = None, CompleteDSLPckg_Operation154: set["CompleteDSLPckg_Constraint"] = None, CompleteDSLPckg_Operation157: set["CompleteDSLPckg_Constraint"] = None, ownedOperation: "CompleteDSLPckg_Class" = None, ownedOperation165: "CompleteDSLPckg_Interface" = None, Operation: "CompleteDSLPckg_Class" = None, CompleteDSLPckg_Operation258: "CompleteDSLPckg_CallEvent" = None, Operation214: "CompleteDSLPckg_Interface" = None, CompleteDSLPckg_Operation364: "CompleteDSLPckg_Artifact" = None, CompleteDSLPckg_Operation410: "CompleteDSLPckg_CallOperationAction" = None, CompleteDSLPckg_Operation680: "CompleteDSLPckg_ProtocolTransition" = None):
        self.isQuery = isQuery
        self.isOrdered = isOrdered
        self.isUnique = isUnique
        self.upper = upper
        self.lower = lower
        self.Operation188 = Operation188
        self.ownedOperation162 = ownedOperation162
        self.CompleteDSLPckg_Operation = CompleteDSLPckg_Operation
        self.CompleteDSLPckg_Operation151 = CompleteDSLPckg_Operation151 if CompleteDSLPckg_Operation151 is not None else set()
        self.CompleteDSLPckg_Operation154 = CompleteDSLPckg_Operation154 if CompleteDSLPckg_Operation154 is not None else set()
        self.CompleteDSLPckg_Operation157 = CompleteDSLPckg_Operation157 if CompleteDSLPckg_Operation157 is not None else set()
        self.ownedOperation = ownedOperation
        self.ownedOperation165 = ownedOperation165
        self.Operation = Operation
        self.CompleteDSLPckg_Operation258 = CompleteDSLPckg_Operation258
        self.Operation214 = Operation214
        self.CompleteDSLPckg_Operation364 = CompleteDSLPckg_Operation364
        self.CompleteDSLPckg_Operation410 = CompleteDSLPckg_Operation410
        self.CompleteDSLPckg_Operation680 = CompleteDSLPckg_Operation680
        
        pass
    @property
    def isOrdered(self):
        return self.__isOrdered

    @isOrdered.setter
    def isOrdered(self, isOrdered: bool):
        self.__isOrdered = isOrdered


    @property
    def isUnique(self):
        return self.__isUnique

    @isUnique.setter
    def isUnique(self, isUnique: bool):
        self.__isUnique = isUnique


    @property
    def lower(self):
        return self.__lower

    @lower.setter
    def lower(self, lower: int):
        self.__lower = lower


    @property
    def upper(self):
        return self.__upper

    @upper.setter
    def upper(self, upper: int):
        self.__upper = upper


    @property
    def isQuery(self):
        return self.__isQuery

    @isQuery.setter
    def isQuery(self, isQuery: bool):
        self.__isQuery = isQuery


    @property
    def CompleteDSLPckg_Operation364(self):
        return self.__CompleteDSLPckg_Operation364

    @CompleteDSLPckg_Operation364.setter
    def CompleteDSLPckg_Operation364(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Operation__CompleteDSLPckg_Operation364", None)
        self.__CompleteDSLPckg_Operation364 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Artifact"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Artifact", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Artifact"):
                opp_val = getattr(value, "CompleteDSLPckg_Artifact", None)
                if opp_val is None:
                    setattr(value, "CompleteDSLPckg_Artifact", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CompleteDSLPckg_Operation258(self):
        return self.__CompleteDSLPckg_Operation258

    @CompleteDSLPckg_Operation258.setter
    def CompleteDSLPckg_Operation258(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Operation__CompleteDSLPckg_Operation258", None)
        self.__CompleteDSLPckg_Operation258 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_CallEvent"):
                opp_val = getattr(old_value, "CompleteDSLPckg_CallEvent", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_CallEvent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_CallEvent"):
                opp_val = getattr(value, "CompleteDSLPckg_CallEvent", None)
                setattr(value, "CompleteDSLPckg_CallEvent", self)

    @property
    def ownedOperation162(self):
        return self.__ownedOperation162

    @ownedOperation162.setter
    def ownedOperation162(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Operation__ownedOperation162", None)
        self.__ownedOperation162 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DataType163"):
                opp_val = getattr(old_value, "DataType163", None)
                if opp_val == self:
                    setattr(old_value, "DataType163", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DataType163"):
                opp_val = getattr(value, "DataType163", None)
                setattr(value, "DataType163", self)

    @property
    def ownedOperation165(self):
        return self.__ownedOperation165

    @ownedOperation165.setter
    def ownedOperation165(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Operation__ownedOperation165", None)
        self.__ownedOperation165 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Interface166"):
                opp_val = getattr(old_value, "Interface166", None)
                if opp_val == self:
                    setattr(old_value, "Interface166", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Interface166"):
                opp_val = getattr(value, "Interface166", None)
                setattr(value, "Interface166", self)

    @property
    def CompleteDSLPckg_Operation154(self):
        return self.__CompleteDSLPckg_Operation154

    @CompleteDSLPckg_Operation154.setter
    def CompleteDSLPckg_Operation154(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Operation__CompleteDSLPckg_Operation154", None)
        self.__CompleteDSLPckg_Operation154 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_Constraint155"):
                    opp_val = getattr(item, "CompleteDSLPckg_Constraint155", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_Constraint155", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_Constraint155"):
                    opp_val = getattr(item, "CompleteDSLPckg_Constraint155", None)
                    
                    setattr(item, "CompleteDSLPckg_Constraint155", self)
                    

    @property
    def CompleteDSLPckg_Operation151(self):
        return self.__CompleteDSLPckg_Operation151

    @CompleteDSLPckg_Operation151.setter
    def CompleteDSLPckg_Operation151(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Operation__CompleteDSLPckg_Operation151", None)
        self.__CompleteDSLPckg_Operation151 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_Constraint152"):
                    opp_val = getattr(item, "CompleteDSLPckg_Constraint152", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_Constraint152", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_Constraint152"):
                    opp_val = getattr(item, "CompleteDSLPckg_Constraint152", None)
                    
                    setattr(item, "CompleteDSLPckg_Constraint152", self)
                    

    @property
    def CompleteDSLPckg_Operation(self):
        return self.__CompleteDSLPckg_Operation

    @CompleteDSLPckg_Operation.setter
    def CompleteDSLPckg_Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Operation__CompleteDSLPckg_Operation", None)
        self.__CompleteDSLPckg_Operation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Type149"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Type149", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_Type149", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Type149"):
                opp_val = getattr(value, "CompleteDSLPckg_Type149", None)
                setattr(value, "CompleteDSLPckg_Type149", self)

    @property
    def CompleteDSLPckg_Operation680(self):
        return self.__CompleteDSLPckg_Operation680

    @CompleteDSLPckg_Operation680.setter
    def CompleteDSLPckg_Operation680(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Operation__CompleteDSLPckg_Operation680", None)
        self.__CompleteDSLPckg_Operation680 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_ProtocolTransition679"):
                opp_val = getattr(old_value, "CompleteDSLPckg_ProtocolTransition679", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_ProtocolTransition679"):
                opp_val = getattr(value, "CompleteDSLPckg_ProtocolTransition679", None)
                if opp_val is None:
                    setattr(value, "CompleteDSLPckg_ProtocolTransition679", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Operation188(self):
        return self.__Operation188

    @Operation188.setter
    def Operation188(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Operation__Operation188", None)
        self.__Operation188 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dataType187"):
                opp_val = getattr(old_value, "dataType187", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dataType187"):
                opp_val = getattr(value, "dataType187", None)
                if opp_val is None:
                    setattr(value, "dataType187", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Operation(self):
        return self.__Operation

    @Operation.setter
    def Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Operation__Operation", None)
        self.__Operation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "class_"):
                opp_val = getattr(old_value, "class_", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "class_"):
                opp_val = getattr(value, "class_", None)
                if opp_val is None:
                    setattr(value, "class_", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CompleteDSLPckg_Operation410(self):
        return self.__CompleteDSLPckg_Operation410

    @CompleteDSLPckg_Operation410.setter
    def CompleteDSLPckg_Operation410(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Operation__CompleteDSLPckg_Operation410", None)
        self.__CompleteDSLPckg_Operation410 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_CallOperationAction"):
                opp_val = getattr(old_value, "CompleteDSLPckg_CallOperationAction", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_CallOperationAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_CallOperationAction"):
                opp_val = getattr(value, "CompleteDSLPckg_CallOperationAction", None)
                setattr(value, "CompleteDSLPckg_CallOperationAction", self)

    @property
    def ownedOperation(self):
        return self.__ownedOperation

    @ownedOperation.setter
    def ownedOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Operation__ownedOperation", None)
        self.__ownedOperation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Class160"):
                opp_val = getattr(old_value, "Class160", None)
                if opp_val == self:
                    setattr(old_value, "Class160", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Class160"):
                opp_val = getattr(value, "Class160", None)
                setattr(value, "Class160", self)

    @property
    def Operation214(self):
        return self.__Operation214

    @Operation214.setter
    def Operation214(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Operation__Operation214", None)
        self.__Operation214 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "interface213"):
                opp_val = getattr(old_value, "interface213", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "interface213"):
                opp_val = getattr(value, "interface213", None)
                if opp_val is None:
                    setattr(value, "interface213", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CompleteDSLPckg_Operation157(self):
        return self.__CompleteDSLPckg_Operation157

    @CompleteDSLPckg_Operation157.setter
    def CompleteDSLPckg_Operation157(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Operation__CompleteDSLPckg_Operation157", None)
        self.__CompleteDSLPckg_Operation157 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_Constraint158"):
                    opp_val = getattr(item, "CompleteDSLPckg_Constraint158", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_Constraint158", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_Constraint158"):
                    opp_val = getattr(item, "CompleteDSLPckg_Constraint158", None)
                    
                    setattr(item, "CompleteDSLPckg_Constraint158", self)
                    

class CompleteDSLPckg_Interface(Classifier):

    pass
class CompleteDSLPckg_DataType(Classifier):

    pass
class CompleteDSLPckg_Class(StructuredClassifier, EncapsulatedClassifier, Classifier, BehavioredClassifier):

    pass
class DeploymentTarget:

    pass
class CompleteDSLPckg_Node(Class, DeploymentTarget):

    pass
class ConnectableElement:

    pass
class StructuralFeature:

    pass
class MultiplicityElement:

    pass
class Feature:

    pass
class CompleteDSLPckg_Connector(Feature):

    def __init__(self, kind: str, CompleteDSLPckg_Connector: set["CompleteDSLPckg_ConnectorEnd"] = None, CompleteDSLPckg_Connector313: set["CompleteDSLPckg_Behavior"] = None, CompleteDSLPckg_Connector317: "CompleteDSLPckg_Connector" = None, CompleteDSLPckg_Connector315: set["CompleteDSLPckg_Connector"] = None, CompleteDSLPckg_Connector333: "CompleteDSLPckg_StructuredClassifier" = None, CompleteDSLPckg_Connector927: "CompleteDSLPckg_Message" = None):
        self.kind = kind
        self.CompleteDSLPckg_Connector = CompleteDSLPckg_Connector if CompleteDSLPckg_Connector is not None else set()
        self.CompleteDSLPckg_Connector313 = CompleteDSLPckg_Connector313 if CompleteDSLPckg_Connector313 is not None else set()
        self.CompleteDSLPckg_Connector317 = CompleteDSLPckg_Connector317
        self.CompleteDSLPckg_Connector315 = CompleteDSLPckg_Connector315 if CompleteDSLPckg_Connector315 is not None else set()
        self.CompleteDSLPckg_Connector333 = CompleteDSLPckg_Connector333
        self.CompleteDSLPckg_Connector927 = CompleteDSLPckg_Connector927
        
        pass
    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind


    @property
    def CompleteDSLPckg_Connector313(self):
        return self.__CompleteDSLPckg_Connector313

    @CompleteDSLPckg_Connector313.setter
    def CompleteDSLPckg_Connector313(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Connector__CompleteDSLPckg_Connector313", None)
        self.__CompleteDSLPckg_Connector313 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_Behavior314"):
                    opp_val = getattr(item, "CompleteDSLPckg_Behavior314", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_Behavior314", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_Behavior314"):
                    opp_val = getattr(item, "CompleteDSLPckg_Behavior314", None)
                    
                    setattr(item, "CompleteDSLPckg_Behavior314", self)
                    

    @property
    def CompleteDSLPckg_Connector315(self):
        return self.__CompleteDSLPckg_Connector315

    @CompleteDSLPckg_Connector315.setter
    def CompleteDSLPckg_Connector315(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Connector__CompleteDSLPckg_Connector315", None)
        self.__CompleteDSLPckg_Connector315 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_Connector317"):
                    opp_val = getattr(item, "CompleteDSLPckg_Connector317", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_Connector317", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_Connector317"):
                    opp_val = getattr(item, "CompleteDSLPckg_Connector317", None)
                    
                    setattr(item, "CompleteDSLPckg_Connector317", self)
                    

    @property
    def CompleteDSLPckg_Connector927(self):
        return self.__CompleteDSLPckg_Connector927

    @CompleteDSLPckg_Connector927.setter
    def CompleteDSLPckg_Connector927(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Connector__CompleteDSLPckg_Connector927", None)
        self.__CompleteDSLPckg_Connector927 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Message926"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Message926", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_Message926", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Message926"):
                opp_val = getattr(value, "CompleteDSLPckg_Message926", None)
                setattr(value, "CompleteDSLPckg_Message926", self)

    @property
    def CompleteDSLPckg_Connector333(self):
        return self.__CompleteDSLPckg_Connector333

    @CompleteDSLPckg_Connector333.setter
    def CompleteDSLPckg_Connector333(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Connector__CompleteDSLPckg_Connector333", None)
        self.__CompleteDSLPckg_Connector333 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_StructuredClassifier"):
                opp_val = getattr(old_value, "CompleteDSLPckg_StructuredClassifier", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_StructuredClassifier"):
                opp_val = getattr(value, "CompleteDSLPckg_StructuredClassifier", None)
                if opp_val is None:
                    setattr(value, "CompleteDSLPckg_StructuredClassifier", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CompleteDSLPckg_Connector317(self):
        return self.__CompleteDSLPckg_Connector317

    @CompleteDSLPckg_Connector317.setter
    def CompleteDSLPckg_Connector317(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Connector__CompleteDSLPckg_Connector317", None)
        self.__CompleteDSLPckg_Connector317 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Connector315"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Connector315", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Connector315"):
                opp_val = getattr(value, "CompleteDSLPckg_Connector315", None)
                if opp_val is None:
                    setattr(value, "CompleteDSLPckg_Connector315", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CompleteDSLPckg_Connector(self):
        return self.__CompleteDSLPckg_Connector

    @CompleteDSLPckg_Connector.setter
    def CompleteDSLPckg_Connector(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Connector__CompleteDSLPckg_Connector", None)
        self.__CompleteDSLPckg_Connector = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_ConnectorEnd"):
                    opp_val = getattr(item, "CompleteDSLPckg_ConnectorEnd", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_ConnectorEnd", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_ConnectorEnd"):
                    opp_val = getattr(item, "CompleteDSLPckg_ConnectorEnd", None)
                    
                    setattr(item, "CompleteDSLPckg_ConnectorEnd", self)
                    

class CompleteDSLPckg_Substitution(Realization):

    pass
class CompleteDSLPckg_Property(StructuralFeature, ConnectableElement, DeploymentTarget):

    def __init__(self, aggregation: str, isDerived: bool, isDerivedUnion: bool, default: str, isComposite: bool, isID: bool, CompleteDSLPckg_Property: "CompleteDSLPckg_Classifier" = None, ownedAttribute: "CompleteDSLPckg_Class" = None, CompleteDSLPckg_Property108: "CompleteDSLPckg_Property" = None, CompleteDSLPckg_Property106: set["CompleteDSLPckg_Property"] = None, CompleteDSLPckg_Property110: "CompleteDSLPckg_ValueSpecification" = None, CompleteDSLPckg_Property114: "CompleteDSLPckg_Property" = None, CompleteDSLPckg_Property112: "CompleteDSLPckg_Property" = None, CompleteDSLPckg_Property117: "CompleteDSLPckg_Property" = None, CompleteDSLPckg_Property115: "CompleteDSLPckg_Property" = None, memberEnd: "CompleteDSLPckg_Association" = None, ownedEnd: "CompleteDSLPckg_Association" = None, ownedAttribute122: "CompleteDSLPckg_DataType" = None, ownedAttribute124: "CompleteDSLPckg_Interface" = None, Property175: "CompleteDSLPckg_Class" = None, Property181: "CompleteDSLPckg_Association" = None, Property183: "CompleteDSLPckg_Association" = None, Property185: "CompleteDSLPckg_DataType" = None, Property211: "CompleteDSLPckg_Interface" = None, Property: "CompleteDSLPckg_Property" = None, associationEnd: set["CompleteDSLPckg_Property"] = None, Property129: "CompleteDSLPckg_Property" = None, qualifier: "CompleteDSLPckg_Property" = None, CompleteDSLPckg_Property179: "CompleteDSLPckg_Association" = None, CompleteDSLPckg_Property250: "CompleteDSLPckg_Signal" = None, CompleteDSLPckg_Property367: "CompleteDSLPckg_Artifact" = None, CompleteDSLPckg_Property320: "CompleteDSLPckg_ConnectorEnd" = None, CompleteDSLPckg_Property328: "CompleteDSLPckg_ConnectorEnd" = None, CompleteDSLPckg_Property339: "CompleteDSLPckg_StructuredClassifier" = None, CompleteDSLPckg_Property342: "CompleteDSLPckg_StructuredClassifier" = None, CompleteDSLPckg_Property475: "CompleteDSLPckg_LinkEndData" = None, CompleteDSLPckg_Property536: "CompleteDSLPckg_ReadLinkObjectEndAction" = None, CompleteDSLPckg_Property550: "CompleteDSLPckg_ReadLinkObjectEndQualifierAction" = None, CompleteDSLPckg_Property531: "CompleteDSLPckg_QualifierValue" = None, CompleteDSLPckg_Property979: "CompleteDSLPckg_InteractionUse" = None):
        self.aggregation = aggregation
        self.isDerived = isDerived
        self.isDerivedUnion = isDerivedUnion
        self.default = default
        self.isComposite = isComposite
        self.isID = isID
        self.CompleteDSLPckg_Property = CompleteDSLPckg_Property
        self.ownedAttribute = ownedAttribute
        self.CompleteDSLPckg_Property108 = CompleteDSLPckg_Property108
        self.CompleteDSLPckg_Property106 = CompleteDSLPckg_Property106 if CompleteDSLPckg_Property106 is not None else set()
        self.CompleteDSLPckg_Property110 = CompleteDSLPckg_Property110
        self.CompleteDSLPckg_Property114 = CompleteDSLPckg_Property114
        self.CompleteDSLPckg_Property112 = CompleteDSLPckg_Property112
        self.CompleteDSLPckg_Property117 = CompleteDSLPckg_Property117
        self.CompleteDSLPckg_Property115 = CompleteDSLPckg_Property115
        self.memberEnd = memberEnd
        self.ownedEnd = ownedEnd
        self.ownedAttribute122 = ownedAttribute122
        self.ownedAttribute124 = ownedAttribute124
        self.Property175 = Property175
        self.Property181 = Property181
        self.Property183 = Property183
        self.Property185 = Property185
        self.Property211 = Property211
        self.Property = Property
        self.associationEnd = associationEnd if associationEnd is not None else set()
        self.Property129 = Property129
        self.qualifier = qualifier
        self.CompleteDSLPckg_Property179 = CompleteDSLPckg_Property179
        self.CompleteDSLPckg_Property250 = CompleteDSLPckg_Property250
        self.CompleteDSLPckg_Property367 = CompleteDSLPckg_Property367
        self.CompleteDSLPckg_Property320 = CompleteDSLPckg_Property320
        self.CompleteDSLPckg_Property328 = CompleteDSLPckg_Property328
        self.CompleteDSLPckg_Property339 = CompleteDSLPckg_Property339
        self.CompleteDSLPckg_Property342 = CompleteDSLPckg_Property342
        self.CompleteDSLPckg_Property475 = CompleteDSLPckg_Property475
        self.CompleteDSLPckg_Property536 = CompleteDSLPckg_Property536
        self.CompleteDSLPckg_Property550 = CompleteDSLPckg_Property550
        self.CompleteDSLPckg_Property531 = CompleteDSLPckg_Property531
        self.CompleteDSLPckg_Property979 = CompleteDSLPckg_Property979
        
        pass
    @property
    def isDerived(self):
        return self.__isDerived

    @isDerived.setter
    def isDerived(self, isDerived: bool):
        self.__isDerived = isDerived


    @property
    def isComposite(self):
        return self.__isComposite

    @isComposite.setter
    def isComposite(self, isComposite: bool):
        self.__isComposite = isComposite


    @property
    def isDerivedUnion(self):
        return self.__isDerivedUnion

    @isDerivedUnion.setter
    def isDerivedUnion(self, isDerivedUnion: bool):
        self.__isDerivedUnion = isDerivedUnion


    @property
    def default(self):
        return self.__default

    @default.setter
    def default(self, default: str):
        self.__default = default


    @property
    def aggregation(self):
        return self.__aggregation

    @aggregation.setter
    def aggregation(self, aggregation: str):
        self.__aggregation = aggregation


    @property
    def isID(self):
        return self.__isID

    @isID.setter
    def isID(self, isID: bool):
        self.__isID = isID


    @property
    def Property(self):
        return self.__Property

    @Property.setter
    def Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Property__Property", None)
        self.__Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "associationEnd"):
                opp_val = getattr(old_value, "associationEnd", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "associationEnd"):
                opp_val = getattr(value, "associationEnd", None)
                if opp_val is None:
                    setattr(value, "associationEnd", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CompleteDSLPckg_Property979(self):
        return self.__CompleteDSLPckg_Property979

    @CompleteDSLPckg_Property979.setter
    def CompleteDSLPckg_Property979(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Property__CompleteDSLPckg_Property979", None)
        self.__CompleteDSLPckg_Property979 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_InteractionUse978"):
                opp_val = getattr(old_value, "CompleteDSLPckg_InteractionUse978", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_InteractionUse978", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_InteractionUse978"):
                opp_val = getattr(value, "CompleteDSLPckg_InteractionUse978", None)
                setattr(value, "CompleteDSLPckg_InteractionUse978", self)

    @property
    def ownedEnd(self):
        return self.__ownedEnd

    @ownedEnd.setter
    def ownedEnd(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Property__ownedEnd", None)
        self.__ownedEnd = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Association120"):
                opp_val = getattr(old_value, "Association120", None)
                if opp_val == self:
                    setattr(old_value, "Association120", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Association120"):
                opp_val = getattr(value, "Association120", None)
                setattr(value, "Association120", self)

    @property
    def CompleteDSLPckg_Property550(self):
        return self.__CompleteDSLPckg_Property550

    @CompleteDSLPckg_Property550.setter
    def CompleteDSLPckg_Property550(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Property__CompleteDSLPckg_Property550", None)
        self.__CompleteDSLPckg_Property550 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_ReadLinkObjectEndQualifierAction549"):
                opp_val = getattr(old_value, "CompleteDSLPckg_ReadLinkObjectEndQualifierAction549", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_ReadLinkObjectEndQualifierAction549", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_ReadLinkObjectEndQualifierAction549"):
                opp_val = getattr(value, "CompleteDSLPckg_ReadLinkObjectEndQualifierAction549", None)
                setattr(value, "CompleteDSLPckg_ReadLinkObjectEndQualifierAction549", self)

    @property
    def Property211(self):
        return self.__Property211

    @Property211.setter
    def Property211(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Property__Property211", None)
        self.__Property211 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "interface"):
                opp_val = getattr(old_value, "interface", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "interface"):
                opp_val = getattr(value, "interface", None)
                if opp_val is None:
                    setattr(value, "interface", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CompleteDSLPckg_Property(self):
        return self.__CompleteDSLPckg_Property

    @CompleteDSLPckg_Property.setter
    def CompleteDSLPckg_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Property__CompleteDSLPckg_Property", None)
        self.__CompleteDSLPckg_Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Classifier89"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Classifier89", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Classifier89"):
                opp_val = getattr(value, "CompleteDSLPckg_Classifier89", None)
                if opp_val is None:
                    setattr(value, "CompleteDSLPckg_Classifier89", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def associationEnd(self):
        return self.__associationEnd

    @associationEnd.setter
    def associationEnd(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Property__associationEnd", None)
        self.__associationEnd = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Property"):
                    opp_val = getattr(item, "Property", None)
                    
                    if opp_val == self:
                        setattr(item, "Property", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Property"):
                    opp_val = getattr(item, "Property", None)
                    
                    setattr(item, "Property", self)
                    

    @property
    def memberEnd(self):
        return self.__memberEnd

    @memberEnd.setter
    def memberEnd(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Property__memberEnd", None)
        self.__memberEnd = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Association"):
                opp_val = getattr(old_value, "Association", None)
                if opp_val == self:
                    setattr(old_value, "Association", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Association"):
                opp_val = getattr(value, "Association", None)
                setattr(value, "Association", self)

    @property
    def Property129(self):
        return self.__Property129

    @Property129.setter
    def Property129(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Property__Property129", None)
        self.__Property129 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "qualifier"):
                opp_val = getattr(old_value, "qualifier", None)
                if opp_val == self:
                    setattr(old_value, "qualifier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "qualifier"):
                opp_val = getattr(value, "qualifier", None)
                setattr(value, "qualifier", self)

    @property
    def ownedAttribute(self):
        return self.__ownedAttribute

    @ownedAttribute.setter
    def ownedAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Property__ownedAttribute", None)
        self.__ownedAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Class"):
                opp_val = getattr(old_value, "Class", None)
                if opp_val == self:
                    setattr(old_value, "Class", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Class"):
                opp_val = getattr(value, "Class", None)
                setattr(value, "Class", self)

    @property
    def CompleteDSLPckg_Property531(self):
        return self.__CompleteDSLPckg_Property531

    @CompleteDSLPckg_Property531.setter
    def CompleteDSLPckg_Property531(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Property__CompleteDSLPckg_Property531", None)
        self.__CompleteDSLPckg_Property531 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_QualifierValue530"):
                opp_val = getattr(old_value, "CompleteDSLPckg_QualifierValue530", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_QualifierValue530", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_QualifierValue530"):
                opp_val = getattr(value, "CompleteDSLPckg_QualifierValue530", None)
                setattr(value, "CompleteDSLPckg_QualifierValue530", self)

    @property
    def CompleteDSLPckg_Property115(self):
        return self.__CompleteDSLPckg_Property115

    @CompleteDSLPckg_Property115.setter
    def CompleteDSLPckg_Property115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Property__CompleteDSLPckg_Property115", None)
        self.__CompleteDSLPckg_Property115 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Property117"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Property117", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_Property117", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Property117"):
                opp_val = getattr(value, "CompleteDSLPckg_Property117", None)
                setattr(value, "CompleteDSLPckg_Property117", self)

    @property
    def CompleteDSLPckg_Property475(self):
        return self.__CompleteDSLPckg_Property475

    @CompleteDSLPckg_Property475.setter
    def CompleteDSLPckg_Property475(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Property__CompleteDSLPckg_Property475", None)
        self.__CompleteDSLPckg_Property475 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_LinkEndData474"):
                opp_val = getattr(old_value, "CompleteDSLPckg_LinkEndData474", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_LinkEndData474", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_LinkEndData474"):
                opp_val = getattr(value, "CompleteDSLPckg_LinkEndData474", None)
                setattr(value, "CompleteDSLPckg_LinkEndData474", self)

    @property
    def CompleteDSLPckg_Property320(self):
        return self.__CompleteDSLPckg_Property320

    @CompleteDSLPckg_Property320.setter
    def CompleteDSLPckg_Property320(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Property__CompleteDSLPckg_Property320", None)
        self.__CompleteDSLPckg_Property320 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_ConnectorEnd319"):
                opp_val = getattr(old_value, "CompleteDSLPckg_ConnectorEnd319", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_ConnectorEnd319", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_ConnectorEnd319"):
                opp_val = getattr(value, "CompleteDSLPckg_ConnectorEnd319", None)
                setattr(value, "CompleteDSLPckg_ConnectorEnd319", self)

    @property
    def CompleteDSLPckg_Property106(self):
        return self.__CompleteDSLPckg_Property106

    @CompleteDSLPckg_Property106.setter
    def CompleteDSLPckg_Property106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Property__CompleteDSLPckg_Property106", None)
        self.__CompleteDSLPckg_Property106 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_Property108"):
                    opp_val = getattr(item, "CompleteDSLPckg_Property108", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_Property108", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_Property108"):
                    opp_val = getattr(item, "CompleteDSLPckg_Property108", None)
                    
                    setattr(item, "CompleteDSLPckg_Property108", self)
                    

    @property
    def CompleteDSLPckg_Property112(self):
        return self.__CompleteDSLPckg_Property112

    @CompleteDSLPckg_Property112.setter
    def CompleteDSLPckg_Property112(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Property__CompleteDSLPckg_Property112", None)
        self.__CompleteDSLPckg_Property112 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Property114"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Property114", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_Property114", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Property114"):
                opp_val = getattr(value, "CompleteDSLPckg_Property114", None)
                setattr(value, "CompleteDSLPckg_Property114", self)

    @property
    def ownedAttribute122(self):
        return self.__ownedAttribute122

    @ownedAttribute122.setter
    def ownedAttribute122(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Property__ownedAttribute122", None)
        self.__ownedAttribute122 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DataType"):
                opp_val = getattr(old_value, "DataType", None)
                if opp_val == self:
                    setattr(old_value, "DataType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DataType"):
                opp_val = getattr(value, "DataType", None)
                setattr(value, "DataType", self)

    @property
    def CompleteDSLPckg_Property342(self):
        return self.__CompleteDSLPckg_Property342

    @CompleteDSLPckg_Property342.setter
    def CompleteDSLPckg_Property342(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Property__CompleteDSLPckg_Property342", None)
        self.__CompleteDSLPckg_Property342 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_StructuredClassifier341"):
                opp_val = getattr(old_value, "CompleteDSLPckg_StructuredClassifier341", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_StructuredClassifier341"):
                opp_val = getattr(value, "CompleteDSLPckg_StructuredClassifier341", None)
                if opp_val is None:
                    setattr(value, "CompleteDSLPckg_StructuredClassifier341", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CompleteDSLPckg_Property250(self):
        return self.__CompleteDSLPckg_Property250

    @CompleteDSLPckg_Property250.setter
    def CompleteDSLPckg_Property250(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Property__CompleteDSLPckg_Property250", None)
        self.__CompleteDSLPckg_Property250 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Signal"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Signal", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Signal"):
                opp_val = getattr(value, "CompleteDSLPckg_Signal", None)
                if opp_val is None:
                    setattr(value, "CompleteDSLPckg_Signal", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CompleteDSLPckg_Property108(self):
        return self.__CompleteDSLPckg_Property108

    @CompleteDSLPckg_Property108.setter
    def CompleteDSLPckg_Property108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Property__CompleteDSLPckg_Property108", None)
        self.__CompleteDSLPckg_Property108 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Property106"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Property106", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Property106"):
                opp_val = getattr(value, "CompleteDSLPckg_Property106", None)
                if opp_val is None:
                    setattr(value, "CompleteDSLPckg_Property106", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Property185(self):
        return self.__Property185

    @Property185.setter
    def Property185(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Property__Property185", None)
        self.__Property185 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dataType"):
                opp_val = getattr(old_value, "dataType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dataType"):
                opp_val = getattr(value, "dataType", None)
                if opp_val is None:
                    setattr(value, "dataType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CompleteDSLPckg_Property117(self):
        return self.__CompleteDSLPckg_Property117

    @CompleteDSLPckg_Property117.setter
    def CompleteDSLPckg_Property117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Property__CompleteDSLPckg_Property117", None)
        self.__CompleteDSLPckg_Property117 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Property115"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Property115", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_Property115", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Property115"):
                opp_val = getattr(value, "CompleteDSLPckg_Property115", None)
                setattr(value, "CompleteDSLPckg_Property115", self)

    @property
    def ownedAttribute124(self):
        return self.__ownedAttribute124

    @ownedAttribute124.setter
    def ownedAttribute124(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Property__ownedAttribute124", None)
        self.__ownedAttribute124 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Interface"):
                opp_val = getattr(old_value, "Interface", None)
                if opp_val == self:
                    setattr(old_value, "Interface", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Interface"):
                opp_val = getattr(value, "Interface", None)
                setattr(value, "Interface", self)

    @property
    def qualifier(self):
        return self.__qualifier

    @qualifier.setter
    def qualifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Property__qualifier", None)
        self.__qualifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Property129"):
                opp_val = getattr(old_value, "Property129", None)
                if opp_val == self:
                    setattr(old_value, "Property129", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Property129"):
                opp_val = getattr(value, "Property129", None)
                setattr(value, "Property129", self)

    @property
    def CompleteDSLPckg_Property179(self):
        return self.__CompleteDSLPckg_Property179

    @CompleteDSLPckg_Property179.setter
    def CompleteDSLPckg_Property179(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Property__CompleteDSLPckg_Property179", None)
        self.__CompleteDSLPckg_Property179 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Association"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Association", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Association"):
                opp_val = getattr(value, "CompleteDSLPckg_Association", None)
                if opp_val is None:
                    setattr(value, "CompleteDSLPckg_Association", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Property183(self):
        return self.__Property183

    @Property183.setter
    def Property183(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Property__Property183", None)
        self.__Property183 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owningAssociation"):
                opp_val = getattr(old_value, "owningAssociation", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owningAssociation"):
                opp_val = getattr(value, "owningAssociation", None)
                if opp_val is None:
                    setattr(value, "owningAssociation", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CompleteDSLPckg_Property114(self):
        return self.__CompleteDSLPckg_Property114

    @CompleteDSLPckg_Property114.setter
    def CompleteDSLPckg_Property114(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Property__CompleteDSLPckg_Property114", None)
        self.__CompleteDSLPckg_Property114 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Property112"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Property112", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_Property112", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Property112"):
                opp_val = getattr(value, "CompleteDSLPckg_Property112", None)
                setattr(value, "CompleteDSLPckg_Property112", self)

    @property
    def Property181(self):
        return self.__Property181

    @Property181.setter
    def Property181(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Property__Property181", None)
        self.__Property181 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "association"):
                opp_val = getattr(old_value, "association", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "association"):
                opp_val = getattr(value, "association", None)
                if opp_val is None:
                    setattr(value, "association", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CompleteDSLPckg_Property536(self):
        return self.__CompleteDSLPckg_Property536

    @CompleteDSLPckg_Property536.setter
    def CompleteDSLPckg_Property536(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Property__CompleteDSLPckg_Property536", None)
        self.__CompleteDSLPckg_Property536 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_ReadLinkObjectEndAction"):
                opp_val = getattr(old_value, "CompleteDSLPckg_ReadLinkObjectEndAction", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_ReadLinkObjectEndAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_ReadLinkObjectEndAction"):
                opp_val = getattr(value, "CompleteDSLPckg_ReadLinkObjectEndAction", None)
                setattr(value, "CompleteDSLPckg_ReadLinkObjectEndAction", self)

    @property
    def CompleteDSLPckg_Property328(self):
        return self.__CompleteDSLPckg_Property328

    @CompleteDSLPckg_Property328.setter
    def CompleteDSLPckg_Property328(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Property__CompleteDSLPckg_Property328", None)
        self.__CompleteDSLPckg_Property328 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_ConnectorEnd327"):
                opp_val = getattr(old_value, "CompleteDSLPckg_ConnectorEnd327", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_ConnectorEnd327", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_ConnectorEnd327"):
                opp_val = getattr(value, "CompleteDSLPckg_ConnectorEnd327", None)
                setattr(value, "CompleteDSLPckg_ConnectorEnd327", self)

    @property
    def Property175(self):
        return self.__Property175

    @Property175.setter
    def Property175(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Property__Property175", None)
        self.__Property175 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "class_174"):
                opp_val = getattr(old_value, "class_174", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "class_174"):
                opp_val = getattr(value, "class_174", None)
                if opp_val is None:
                    setattr(value, "class_174", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CompleteDSLPckg_Property110(self):
        return self.__CompleteDSLPckg_Property110

    @CompleteDSLPckg_Property110.setter
    def CompleteDSLPckg_Property110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Property__CompleteDSLPckg_Property110", None)
        self.__CompleteDSLPckg_Property110 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_ValueSpecification111"):
                opp_val = getattr(old_value, "CompleteDSLPckg_ValueSpecification111", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_ValueSpecification111", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_ValueSpecification111"):
                opp_val = getattr(value, "CompleteDSLPckg_ValueSpecification111", None)
                setattr(value, "CompleteDSLPckg_ValueSpecification111", self)

    @property
    def CompleteDSLPckg_Property367(self):
        return self.__CompleteDSLPckg_Property367

    @CompleteDSLPckg_Property367.setter
    def CompleteDSLPckg_Property367(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Property__CompleteDSLPckg_Property367", None)
        self.__CompleteDSLPckg_Property367 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Artifact366"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Artifact366", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Artifact366"):
                opp_val = getattr(value, "CompleteDSLPckg_Artifact366", None)
                if opp_val is None:
                    setattr(value, "CompleteDSLPckg_Artifact366", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CompleteDSLPckg_Property339(self):
        return self.__CompleteDSLPckg_Property339

    @CompleteDSLPckg_Property339.setter
    def CompleteDSLPckg_Property339(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Property__CompleteDSLPckg_Property339", None)
        self.__CompleteDSLPckg_Property339 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_StructuredClassifier338"):
                opp_val = getattr(old_value, "CompleteDSLPckg_StructuredClassifier338", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_StructuredClassifier338"):
                opp_val = getattr(value, "CompleteDSLPckg_StructuredClassifier338", None)
                if opp_val is None:
                    setattr(value, "CompleteDSLPckg_StructuredClassifier338", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Type:

    pass
class RedefinableElement:

    pass
class CompleteDSLPckg_Feature(RedefinableElement):

    def __init__(self, isStatic: bool, Feature: "CompleteDSLPckg_Classifier" = None, feature: set["CompleteDSLPckg_Classifier"] = None):
        self.isStatic = isStatic
        self.Feature = Feature
        self.feature = feature if feature is not None else set()
        
        pass
    @property
    def isStatic(self):
        return self.__isStatic

    @isStatic.setter
    def isStatic(self, isStatic: bool):
        self.__isStatic = isStatic


    @property
    def feature(self):
        return self.__feature

    @feature.setter
    def feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Feature__feature", None)
        self.__feature = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Classifier"):
                    opp_val = getattr(item, "Classifier", None)
                    
                    if opp_val == self:
                        setattr(item, "Classifier", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Classifier"):
                    opp_val = getattr(item, "Classifier", None)
                    
                    setattr(item, "Classifier", self)
                    

    @property
    def Feature(self):
        return self.__Feature

    @Feature.setter
    def Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Feature__Feature", None)
        self.__Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "featuringClassifier"):
                opp_val = getattr(old_value, "featuringClassifier", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "featuringClassifier"):
                opp_val = getattr(value, "featuringClassifier", None)
                if opp_val is None:
                    setattr(value, "featuringClassifier", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class CompleteDSLPckg_ExtensionPoint(RedefinableElement):

    pass
class CompleteDSLPckg_ActivityEdge(RedefinableElement):

    pass
class CompleteDSLPckg_InstanceValue:

    pass
class LiteralSpecification:

    pass
class CompleteDSLPckg_LiteralBoolean(LiteralSpecification):

    pass
class CompleteDSLPckg_LiteralReal(LiteralSpecification):

    pass
class CompleteDSLPckg_LiteralString(LiteralSpecification):

    pass
class CompleteDSLPckg_LiteralUnilimitedNatural(LiteralSpecification):

    pass
class CompleteDSLPckg_LiteralInteger(LiteralSpecification):

    pass
class CompleteDSLPckg_LiteralNull(LiteralSpecification):

    pass
class CompleteDSLPckg_Behavior(Class):

    def __init__(self, isReentrant: bool, CompleteDSLPckg_Behavior: "CompleteDSLPckg_OpaqueExpression" = None, CompleteDSLPckg_Behavior223: "CompleteDSLPckg_BehavioredClassifier" = None, CompleteDSLPckg_Behavior226: "CompleteDSLPckg_BehavioredClassifier" = None, CompleteDSLPckg_Behavior232: "CompleteDSLPckg_BehavioredClassifier" = None, CompleteDSLPckg_Behavior236: "CompleteDSLPckg_Behavior" = None, CompleteDSLPckg_Behavior234: set["CompleteDSLPckg_Behavior"] = None, CompleteDSLPckg_Behavior238: "CompleteDSLPckg_BehavioralFeature" = None, CompleteDSLPckg_Behavior241: set["CompleteDSLPckg_Parameter"] = None, CompleteDSLPckg_Behavior244: set["CompleteDSLPckg_Constraint"] = None, CompleteDSLPckg_Behavior247: set["CompleteDSLPckg_Constraint"] = None, CompleteDSLPckg_Behavior314: "CompleteDSLPckg_Connector" = None, CompleteDSLPckg_Behavior408: "CompleteDSLPckg_CallBehaviorAction" = None, CompleteDSLPckg_Behavior560: "CompleteDSLPckg_ReduceAction" = None, CompleteDSLPckg_Behavior612: "CompleteDSLPckg_Transition" = None, CompleteDSLPckg_Behavior653: "CompleteDSLPckg_State" = None, CompleteDSLPckg_Behavior656: "CompleteDSLPckg_State" = None, CompleteDSLPckg_Behavior659: "CompleteDSLPckg_State" = None, CompleteDSLPckg_Behavior758: "CompleteDSLPckg_ObjectFlow" = None, CompleteDSLPckg_Behavior761: "CompleteDSLPckg_ObjectFlow" = None, CompleteDSLPckg_Behavior771: "CompleteDSLPckg_DecisionNode" = None, CompleteDSLPckg_Behavior942: "CompleteDSLPckg_BehaviorExecutionSpecification" = None):
        self.isReentrant = isReentrant
        self.CompleteDSLPckg_Behavior = CompleteDSLPckg_Behavior
        self.CompleteDSLPckg_Behavior223 = CompleteDSLPckg_Behavior223
        self.CompleteDSLPckg_Behavior226 = CompleteDSLPckg_Behavior226
        self.CompleteDSLPckg_Behavior232 = CompleteDSLPckg_Behavior232
        self.CompleteDSLPckg_Behavior236 = CompleteDSLPckg_Behavior236
        self.CompleteDSLPckg_Behavior234 = CompleteDSLPckg_Behavior234 if CompleteDSLPckg_Behavior234 is not None else set()
        self.CompleteDSLPckg_Behavior238 = CompleteDSLPckg_Behavior238
        self.CompleteDSLPckg_Behavior241 = CompleteDSLPckg_Behavior241 if CompleteDSLPckg_Behavior241 is not None else set()
        self.CompleteDSLPckg_Behavior244 = CompleteDSLPckg_Behavior244 if CompleteDSLPckg_Behavior244 is not None else set()
        self.CompleteDSLPckg_Behavior247 = CompleteDSLPckg_Behavior247 if CompleteDSLPckg_Behavior247 is not None else set()
        self.CompleteDSLPckg_Behavior314 = CompleteDSLPckg_Behavior314
        self.CompleteDSLPckg_Behavior408 = CompleteDSLPckg_Behavior408
        self.CompleteDSLPckg_Behavior560 = CompleteDSLPckg_Behavior560
        self.CompleteDSLPckg_Behavior612 = CompleteDSLPckg_Behavior612
        self.CompleteDSLPckg_Behavior653 = CompleteDSLPckg_Behavior653
        self.CompleteDSLPckg_Behavior656 = CompleteDSLPckg_Behavior656
        self.CompleteDSLPckg_Behavior659 = CompleteDSLPckg_Behavior659
        self.CompleteDSLPckg_Behavior758 = CompleteDSLPckg_Behavior758
        self.CompleteDSLPckg_Behavior761 = CompleteDSLPckg_Behavior761
        self.CompleteDSLPckg_Behavior771 = CompleteDSLPckg_Behavior771
        self.CompleteDSLPckg_Behavior942 = CompleteDSLPckg_Behavior942
        
        pass
    @property
    def isReentrant(self):
        return self.__isReentrant

    @isReentrant.setter
    def isReentrant(self, isReentrant: bool):
        self.__isReentrant = isReentrant


    @property
    def CompleteDSLPckg_Behavior659(self):
        return self.__CompleteDSLPckg_Behavior659

    @CompleteDSLPckg_Behavior659.setter
    def CompleteDSLPckg_Behavior659(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Behavior__CompleteDSLPckg_Behavior659", None)
        self.__CompleteDSLPckg_Behavior659 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_State658"):
                opp_val = getattr(old_value, "CompleteDSLPckg_State658", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_State658", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_State658"):
                opp_val = getattr(value, "CompleteDSLPckg_State658", None)
                setattr(value, "CompleteDSLPckg_State658", self)

    @property
    def CompleteDSLPckg_Behavior234(self):
        return self.__CompleteDSLPckg_Behavior234

    @CompleteDSLPckg_Behavior234.setter
    def CompleteDSLPckg_Behavior234(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Behavior__CompleteDSLPckg_Behavior234", None)
        self.__CompleteDSLPckg_Behavior234 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_Behavior236"):
                    opp_val = getattr(item, "CompleteDSLPckg_Behavior236", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_Behavior236", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_Behavior236"):
                    opp_val = getattr(item, "CompleteDSLPckg_Behavior236", None)
                    
                    setattr(item, "CompleteDSLPckg_Behavior236", self)
                    

    @property
    def CompleteDSLPckg_Behavior656(self):
        return self.__CompleteDSLPckg_Behavior656

    @CompleteDSLPckg_Behavior656.setter
    def CompleteDSLPckg_Behavior656(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Behavior__CompleteDSLPckg_Behavior656", None)
        self.__CompleteDSLPckg_Behavior656 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_State655"):
                opp_val = getattr(old_value, "CompleteDSLPckg_State655", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_State655", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_State655"):
                opp_val = getattr(value, "CompleteDSLPckg_State655", None)
                setattr(value, "CompleteDSLPckg_State655", self)

    @property
    def CompleteDSLPckg_Behavior223(self):
        return self.__CompleteDSLPckg_Behavior223

    @CompleteDSLPckg_Behavior223.setter
    def CompleteDSLPckg_Behavior223(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Behavior__CompleteDSLPckg_Behavior223", None)
        self.__CompleteDSLPckg_Behavior223 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_BehavioredClassifier"):
                opp_val = getattr(old_value, "CompleteDSLPckg_BehavioredClassifier", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_BehavioredClassifier"):
                opp_val = getattr(value, "CompleteDSLPckg_BehavioredClassifier", None)
                if opp_val is None:
                    setattr(value, "CompleteDSLPckg_BehavioredClassifier", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CompleteDSLPckg_Behavior232(self):
        return self.__CompleteDSLPckg_Behavior232

    @CompleteDSLPckg_Behavior232.setter
    def CompleteDSLPckg_Behavior232(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Behavior__CompleteDSLPckg_Behavior232", None)
        self.__CompleteDSLPckg_Behavior232 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_BehavioredClassifier233"):
                opp_val = getattr(old_value, "CompleteDSLPckg_BehavioredClassifier233", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_BehavioredClassifier233", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_BehavioredClassifier233"):
                opp_val = getattr(value, "CompleteDSLPckg_BehavioredClassifier233", None)
                setattr(value, "CompleteDSLPckg_BehavioredClassifier233", self)

    @property
    def CompleteDSLPckg_Behavior408(self):
        return self.__CompleteDSLPckg_Behavior408

    @CompleteDSLPckg_Behavior408.setter
    def CompleteDSLPckg_Behavior408(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Behavior__CompleteDSLPckg_Behavior408", None)
        self.__CompleteDSLPckg_Behavior408 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_CallBehaviorAction"):
                opp_val = getattr(old_value, "CompleteDSLPckg_CallBehaviorAction", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_CallBehaviorAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_CallBehaviorAction"):
                opp_val = getattr(value, "CompleteDSLPckg_CallBehaviorAction", None)
                setattr(value, "CompleteDSLPckg_CallBehaviorAction", self)

    @property
    def CompleteDSLPckg_Behavior653(self):
        return self.__CompleteDSLPckg_Behavior653

    @CompleteDSLPckg_Behavior653.setter
    def CompleteDSLPckg_Behavior653(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Behavior__CompleteDSLPckg_Behavior653", None)
        self.__CompleteDSLPckg_Behavior653 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_State652"):
                opp_val = getattr(old_value, "CompleteDSLPckg_State652", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_State652", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_State652"):
                opp_val = getattr(value, "CompleteDSLPckg_State652", None)
                setattr(value, "CompleteDSLPckg_State652", self)

    @property
    def CompleteDSLPckg_Behavior(self):
        return self.__CompleteDSLPckg_Behavior

    @CompleteDSLPckg_Behavior.setter
    def CompleteDSLPckg_Behavior(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Behavior__CompleteDSLPckg_Behavior", None)
        self.__CompleteDSLPckg_Behavior = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_OpaqueExpression60"):
                opp_val = getattr(old_value, "CompleteDSLPckg_OpaqueExpression60", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_OpaqueExpression60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_OpaqueExpression60"):
                opp_val = getattr(value, "CompleteDSLPckg_OpaqueExpression60", None)
                setattr(value, "CompleteDSLPckg_OpaqueExpression60", self)

    @property
    def CompleteDSLPckg_Behavior236(self):
        return self.__CompleteDSLPckg_Behavior236

    @CompleteDSLPckg_Behavior236.setter
    def CompleteDSLPckg_Behavior236(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Behavior__CompleteDSLPckg_Behavior236", None)
        self.__CompleteDSLPckg_Behavior236 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Behavior234"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Behavior234", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Behavior234"):
                opp_val = getattr(value, "CompleteDSLPckg_Behavior234", None)
                if opp_val is None:
                    setattr(value, "CompleteDSLPckg_Behavior234", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CompleteDSLPckg_Behavior771(self):
        return self.__CompleteDSLPckg_Behavior771

    @CompleteDSLPckg_Behavior771.setter
    def CompleteDSLPckg_Behavior771(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Behavior__CompleteDSLPckg_Behavior771", None)
        self.__CompleteDSLPckg_Behavior771 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_DecisionNode770"):
                opp_val = getattr(old_value, "CompleteDSLPckg_DecisionNode770", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_DecisionNode770", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_DecisionNode770"):
                opp_val = getattr(value, "CompleteDSLPckg_DecisionNode770", None)
                setattr(value, "CompleteDSLPckg_DecisionNode770", self)

    @property
    def CompleteDSLPckg_Behavior314(self):
        return self.__CompleteDSLPckg_Behavior314

    @CompleteDSLPckg_Behavior314.setter
    def CompleteDSLPckg_Behavior314(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Behavior__CompleteDSLPckg_Behavior314", None)
        self.__CompleteDSLPckg_Behavior314 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Connector313"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Connector313", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Connector313"):
                opp_val = getattr(value, "CompleteDSLPckg_Connector313", None)
                if opp_val is None:
                    setattr(value, "CompleteDSLPckg_Connector313", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CompleteDSLPckg_Behavior244(self):
        return self.__CompleteDSLPckg_Behavior244

    @CompleteDSLPckg_Behavior244.setter
    def CompleteDSLPckg_Behavior244(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Behavior__CompleteDSLPckg_Behavior244", None)
        self.__CompleteDSLPckg_Behavior244 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_Constraint245"):
                    opp_val = getattr(item, "CompleteDSLPckg_Constraint245", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_Constraint245", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_Constraint245"):
                    opp_val = getattr(item, "CompleteDSLPckg_Constraint245", None)
                    
                    setattr(item, "CompleteDSLPckg_Constraint245", self)
                    

    @property
    def CompleteDSLPckg_Behavior942(self):
        return self.__CompleteDSLPckg_Behavior942

    @CompleteDSLPckg_Behavior942.setter
    def CompleteDSLPckg_Behavior942(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Behavior__CompleteDSLPckg_Behavior942", None)
        self.__CompleteDSLPckg_Behavior942 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_BehaviorExecutionSpecification"):
                opp_val = getattr(old_value, "CompleteDSLPckg_BehaviorExecutionSpecification", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_BehaviorExecutionSpecification", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_BehaviorExecutionSpecification"):
                opp_val = getattr(value, "CompleteDSLPckg_BehaviorExecutionSpecification", None)
                setattr(value, "CompleteDSLPckg_BehaviorExecutionSpecification", self)

    @property
    def CompleteDSLPckg_Behavior612(self):
        return self.__CompleteDSLPckg_Behavior612

    @CompleteDSLPckg_Behavior612.setter
    def CompleteDSLPckg_Behavior612(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Behavior__CompleteDSLPckg_Behavior612", None)
        self.__CompleteDSLPckg_Behavior612 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Transition611"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Transition611", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_Transition611", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Transition611"):
                opp_val = getattr(value, "CompleteDSLPckg_Transition611", None)
                setattr(value, "CompleteDSLPckg_Transition611", self)

    @property
    def CompleteDSLPckg_Behavior238(self):
        return self.__CompleteDSLPckg_Behavior238

    @CompleteDSLPckg_Behavior238.setter
    def CompleteDSLPckg_Behavior238(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Behavior__CompleteDSLPckg_Behavior238", None)
        self.__CompleteDSLPckg_Behavior238 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_BehavioralFeature239"):
                opp_val = getattr(old_value, "CompleteDSLPckg_BehavioralFeature239", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_BehavioralFeature239", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_BehavioralFeature239"):
                opp_val = getattr(value, "CompleteDSLPckg_BehavioralFeature239", None)
                setattr(value, "CompleteDSLPckg_BehavioralFeature239", self)

    @property
    def CompleteDSLPckg_Behavior247(self):
        return self.__CompleteDSLPckg_Behavior247

    @CompleteDSLPckg_Behavior247.setter
    def CompleteDSLPckg_Behavior247(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Behavior__CompleteDSLPckg_Behavior247", None)
        self.__CompleteDSLPckg_Behavior247 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_Constraint248"):
                    opp_val = getattr(item, "CompleteDSLPckg_Constraint248", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_Constraint248", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_Constraint248"):
                    opp_val = getattr(item, "CompleteDSLPckg_Constraint248", None)
                    
                    setattr(item, "CompleteDSLPckg_Constraint248", self)
                    

    @property
    def CompleteDSLPckg_Behavior758(self):
        return self.__CompleteDSLPckg_Behavior758

    @CompleteDSLPckg_Behavior758.setter
    def CompleteDSLPckg_Behavior758(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Behavior__CompleteDSLPckg_Behavior758", None)
        self.__CompleteDSLPckg_Behavior758 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_ObjectFlow"):
                opp_val = getattr(old_value, "CompleteDSLPckg_ObjectFlow", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_ObjectFlow", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_ObjectFlow"):
                opp_val = getattr(value, "CompleteDSLPckg_ObjectFlow", None)
                setattr(value, "CompleteDSLPckg_ObjectFlow", self)

    @property
    def CompleteDSLPckg_Behavior761(self):
        return self.__CompleteDSLPckg_Behavior761

    @CompleteDSLPckg_Behavior761.setter
    def CompleteDSLPckg_Behavior761(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Behavior__CompleteDSLPckg_Behavior761", None)
        self.__CompleteDSLPckg_Behavior761 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_ObjectFlow760"):
                opp_val = getattr(old_value, "CompleteDSLPckg_ObjectFlow760", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_ObjectFlow760", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_ObjectFlow760"):
                opp_val = getattr(value, "CompleteDSLPckg_ObjectFlow760", None)
                setattr(value, "CompleteDSLPckg_ObjectFlow760", self)

    @property
    def CompleteDSLPckg_Behavior226(self):
        return self.__CompleteDSLPckg_Behavior226

    @CompleteDSLPckg_Behavior226.setter
    def CompleteDSLPckg_Behavior226(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Behavior__CompleteDSLPckg_Behavior226", None)
        self.__CompleteDSLPckg_Behavior226 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_BehavioredClassifier225"):
                opp_val = getattr(old_value, "CompleteDSLPckg_BehavioredClassifier225", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_BehavioredClassifier225", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_BehavioredClassifier225"):
                opp_val = getattr(value, "CompleteDSLPckg_BehavioredClassifier225", None)
                setattr(value, "CompleteDSLPckg_BehavioredClassifier225", self)

    @property
    def CompleteDSLPckg_Behavior560(self):
        return self.__CompleteDSLPckg_Behavior560

    @CompleteDSLPckg_Behavior560.setter
    def CompleteDSLPckg_Behavior560(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Behavior__CompleteDSLPckg_Behavior560", None)
        self.__CompleteDSLPckg_Behavior560 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_ReduceAction559"):
                opp_val = getattr(old_value, "CompleteDSLPckg_ReduceAction559", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_ReduceAction559", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_ReduceAction559"):
                opp_val = getattr(value, "CompleteDSLPckg_ReduceAction559", None)
                setattr(value, "CompleteDSLPckg_ReduceAction559", self)

    @property
    def CompleteDSLPckg_Behavior241(self):
        return self.__CompleteDSLPckg_Behavior241

    @CompleteDSLPckg_Behavior241.setter
    def CompleteDSLPckg_Behavior241(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Behavior__CompleteDSLPckg_Behavior241", None)
        self.__CompleteDSLPckg_Behavior241 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_Parameter242"):
                    opp_val = getattr(item, "CompleteDSLPckg_Parameter242", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_Parameter242", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_Parameter242"):
                    opp_val = getattr(item, "CompleteDSLPckg_Parameter242", None)
                    
                    setattr(item, "CompleteDSLPckg_Parameter242", self)
                    

class ValueSpecification:

    pass
class CompleteDSLPckg_Interval(ValueSpecification):

    pass
class CompleteDSLPckg_LiteralSpecification(ValueSpecification):

    pass
class CompleteDSLPckg_OpaqueExpression(ValueSpecification):

    def __init__(self, body: str, language: str, CompleteDSLPckg_OpaqueExpression: "CompleteDSLPckg_Parameter" = None, CompleteDSLPckg_OpaqueExpression60: "CompleteDSLPckg_Behavior" = None, CompleteDSLPckg_OpaqueExpression200: "CompleteDSLPckg_Abstraction" = None):
        self.body = body
        self.language = language
        self.CompleteDSLPckg_OpaqueExpression = CompleteDSLPckg_OpaqueExpression
        self.CompleteDSLPckg_OpaqueExpression60 = CompleteDSLPckg_OpaqueExpression60
        self.CompleteDSLPckg_OpaqueExpression200 = CompleteDSLPckg_OpaqueExpression200
        
        pass
    @property
    def body(self):
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body


    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language


    @property
    def CompleteDSLPckg_OpaqueExpression(self):
        return self.__CompleteDSLPckg_OpaqueExpression

    @CompleteDSLPckg_OpaqueExpression.setter
    def CompleteDSLPckg_OpaqueExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_OpaqueExpression__CompleteDSLPckg_OpaqueExpression", None)
        self.__CompleteDSLPckg_OpaqueExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Parameter"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Parameter", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_Parameter", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Parameter"):
                opp_val = getattr(value, "CompleteDSLPckg_Parameter", None)
                setattr(value, "CompleteDSLPckg_Parameter", self)

    @property
    def CompleteDSLPckg_OpaqueExpression200(self):
        return self.__CompleteDSLPckg_OpaqueExpression200

    @CompleteDSLPckg_OpaqueExpression200.setter
    def CompleteDSLPckg_OpaqueExpression200(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_OpaqueExpression__CompleteDSLPckg_OpaqueExpression200", None)
        self.__CompleteDSLPckg_OpaqueExpression200 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Abstraction"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Abstraction", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_Abstraction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Abstraction"):
                opp_val = getattr(value, "CompleteDSLPckg_Abstraction", None)
                setattr(value, "CompleteDSLPckg_Abstraction", self)

    @property
    def CompleteDSLPckg_OpaqueExpression60(self):
        return self.__CompleteDSLPckg_OpaqueExpression60

    @CompleteDSLPckg_OpaqueExpression60.setter
    def CompleteDSLPckg_OpaqueExpression60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_OpaqueExpression__CompleteDSLPckg_OpaqueExpression60", None)
        self.__CompleteDSLPckg_OpaqueExpression60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Behavior"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Behavior", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_Behavior", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Behavior"):
                opp_val = getattr(value, "CompleteDSLPckg_Behavior", None)
                setattr(value, "CompleteDSLPckg_Behavior", self)

class CompleteDSLPckg_Duration(ValueSpecification):

    pass
class CompleteDSLPckg_TimeExpression(ValueSpecification):

    pass
class CompleteDSLPckg_Expression(ValueSpecification):

    def __init__(self, symbol: str, CompleteDSLPckg_Expression: "CompleteDSLPckg_ValueSpecification" = None):
        self.symbol = symbol
        self.CompleteDSLPckg_Expression = CompleteDSLPckg_Expression
        
        pass
    @property
    def symbol(self):
        return self.__symbol

    @symbol.setter
    def symbol(self, symbol: str):
        self.__symbol = symbol


    @property
    def CompleteDSLPckg_Expression(self):
        return self.__CompleteDSLPckg_Expression

    @CompleteDSLPckg_Expression.setter
    def CompleteDSLPckg_Expression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Expression__CompleteDSLPckg_Expression", None)
        self.__CompleteDSLPckg_Expression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_ValueSpecification"):
                opp_val = getattr(old_value, "CompleteDSLPckg_ValueSpecification", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_ValueSpecification", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_ValueSpecification"):
                opp_val = getattr(value, "CompleteDSLPckg_ValueSpecification", None)
                setattr(value, "CompleteDSLPckg_ValueSpecification", self)

class TypedElement:

    pass
class CompleteDSLPckg_Parameter(TypedElement):

    def __init__(self, default: str, CompleteDSLPckg_Parameter138: "CompleteDSLPckg_BehavioralFeature" = None, CompleteDSLPckg_Parameter: "CompleteDSLPckg_OpaqueExpression" = None, CompleteDSLPckg_Parameter143: "CompleteDSLPckg_BehavioralFeature" = None, CompleteDSLPckg_Parameter146: "CompleteDSLPckg_ValueSpecification" = None, CompleteDSLPckg_Parameter242: "CompleteDSLPckg_Behavior" = None, CompleteDSLPckg_Parameter729: "CompleteDSLPckg_ActivityParameterNode" = None, CompleteDSLPckg_Parameter788: "CompleteDSLPckg_ParameterSet" = None):
        self.default = default
        self.CompleteDSLPckg_Parameter138 = CompleteDSLPckg_Parameter138
        self.CompleteDSLPckg_Parameter = CompleteDSLPckg_Parameter
        self.CompleteDSLPckg_Parameter143 = CompleteDSLPckg_Parameter143
        self.CompleteDSLPckg_Parameter146 = CompleteDSLPckg_Parameter146
        self.CompleteDSLPckg_Parameter242 = CompleteDSLPckg_Parameter242
        self.CompleteDSLPckg_Parameter729 = CompleteDSLPckg_Parameter729
        self.CompleteDSLPckg_Parameter788 = CompleteDSLPckg_Parameter788
        
        pass
    @property
    def default(self):
        return self.__default

    @default.setter
    def default(self, default: str):
        self.__default = default


    @property
    def CompleteDSLPckg_Parameter(self):
        return self.__CompleteDSLPckg_Parameter

    @CompleteDSLPckg_Parameter.setter
    def CompleteDSLPckg_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Parameter__CompleteDSLPckg_Parameter", None)
        self.__CompleteDSLPckg_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_OpaqueExpression"):
                opp_val = getattr(old_value, "CompleteDSLPckg_OpaqueExpression", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_OpaqueExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_OpaqueExpression"):
                opp_val = getattr(value, "CompleteDSLPckg_OpaqueExpression", None)
                setattr(value, "CompleteDSLPckg_OpaqueExpression", self)

    @property
    def CompleteDSLPckg_Parameter242(self):
        return self.__CompleteDSLPckg_Parameter242

    @CompleteDSLPckg_Parameter242.setter
    def CompleteDSLPckg_Parameter242(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Parameter__CompleteDSLPckg_Parameter242", None)
        self.__CompleteDSLPckg_Parameter242 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Behavior241"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Behavior241", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Behavior241"):
                opp_val = getattr(value, "CompleteDSLPckg_Behavior241", None)
                if opp_val is None:
                    setattr(value, "CompleteDSLPckg_Behavior241", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CompleteDSLPckg_Parameter138(self):
        return self.__CompleteDSLPckg_Parameter138

    @CompleteDSLPckg_Parameter138.setter
    def CompleteDSLPckg_Parameter138(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Parameter__CompleteDSLPckg_Parameter138", None)
        self.__CompleteDSLPckg_Parameter138 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_BehavioralFeature"):
                opp_val = getattr(old_value, "CompleteDSLPckg_BehavioralFeature", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_BehavioralFeature"):
                opp_val = getattr(value, "CompleteDSLPckg_BehavioralFeature", None)
                if opp_val is None:
                    setattr(value, "CompleteDSLPckg_BehavioralFeature", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CompleteDSLPckg_Parameter143(self):
        return self.__CompleteDSLPckg_Parameter143

    @CompleteDSLPckg_Parameter143.setter
    def CompleteDSLPckg_Parameter143(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Parameter__CompleteDSLPckg_Parameter143", None)
        self.__CompleteDSLPckg_Parameter143 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_BehavioralFeature144"):
                opp_val = getattr(old_value, "CompleteDSLPckg_BehavioralFeature144", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_BehavioralFeature144", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_BehavioralFeature144"):
                opp_val = getattr(value, "CompleteDSLPckg_BehavioralFeature144", None)
                setattr(value, "CompleteDSLPckg_BehavioralFeature144", self)

    @property
    def CompleteDSLPckg_Parameter729(self):
        return self.__CompleteDSLPckg_Parameter729

    @CompleteDSLPckg_Parameter729.setter
    def CompleteDSLPckg_Parameter729(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Parameter__CompleteDSLPckg_Parameter729", None)
        self.__CompleteDSLPckg_Parameter729 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_ActivityParameterNode"):
                opp_val = getattr(old_value, "CompleteDSLPckg_ActivityParameterNode", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_ActivityParameterNode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_ActivityParameterNode"):
                opp_val = getattr(value, "CompleteDSLPckg_ActivityParameterNode", None)
                setattr(value, "CompleteDSLPckg_ActivityParameterNode", self)

    @property
    def CompleteDSLPckg_Parameter788(self):
        return self.__CompleteDSLPckg_Parameter788

    @CompleteDSLPckg_Parameter788.setter
    def CompleteDSLPckg_Parameter788(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Parameter__CompleteDSLPckg_Parameter788", None)
        self.__CompleteDSLPckg_Parameter788 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_ParameterSet"):
                opp_val = getattr(old_value, "CompleteDSLPckg_ParameterSet", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_ParameterSet"):
                opp_val = getattr(value, "CompleteDSLPckg_ParameterSet", None)
                if opp_val is None:
                    setattr(value, "CompleteDSLPckg_ParameterSet", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CompleteDSLPckg_Parameter146(self):
        return self.__CompleteDSLPckg_Parameter146

    @CompleteDSLPckg_Parameter146.setter
    def CompleteDSLPckg_Parameter146(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Parameter__CompleteDSLPckg_Parameter146", None)
        self.__CompleteDSLPckg_Parameter146 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_ValueSpecification147"):
                opp_val = getattr(old_value, "CompleteDSLPckg_ValueSpecification147", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_ValueSpecification147", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_ValueSpecification147"):
                opp_val = getattr(value, "CompleteDSLPckg_ValueSpecification147", None)
                setattr(value, "CompleteDSLPckg_ValueSpecification147", self)

class CompleteDSLPckg_ConnectableElement(TypedElement):

    pass
class CompleteDSLPckg_Variable(ConnectableElement, TypedElement, MultiplicityElement):

    pass
class CompleteDSLPckg_Pin(TypedElement, MultiplicityElement):

    pass
class CompleteDSLPckg_StructuralFeature(TypedElement, Feature, MultiplicityElement):

    def __init__(self, isReadOnly: bool, CompleteDSLPckg_StructuralFeature: "CompleteDSLPckg_Slot" = None, CompleteDSLPckg_StructuralFeature449: "CompleteDSLPckg_StructuralFeatureAction" = None):
        self.isReadOnly = isReadOnly
        self.CompleteDSLPckg_StructuralFeature = CompleteDSLPckg_StructuralFeature
        self.CompleteDSLPckg_StructuralFeature449 = CompleteDSLPckg_StructuralFeature449
        
        pass
    @property
    def isReadOnly(self):
        return self.__isReadOnly

    @isReadOnly.setter
    def isReadOnly(self, isReadOnly: bool):
        self.__isReadOnly = isReadOnly


    @property
    def CompleteDSLPckg_StructuralFeature449(self):
        return self.__CompleteDSLPckg_StructuralFeature449

    @CompleteDSLPckg_StructuralFeature449.setter
    def CompleteDSLPckg_StructuralFeature449(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_StructuralFeature__CompleteDSLPckg_StructuralFeature449", None)
        self.__CompleteDSLPckg_StructuralFeature449 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_StructuralFeatureAction"):
                opp_val = getattr(old_value, "CompleteDSLPckg_StructuralFeatureAction", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_StructuralFeatureAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_StructuralFeatureAction"):
                opp_val = getattr(value, "CompleteDSLPckg_StructuralFeatureAction", None)
                setattr(value, "CompleteDSLPckg_StructuralFeatureAction", self)

    @property
    def CompleteDSLPckg_StructuralFeature(self):
        return self.__CompleteDSLPckg_StructuralFeature

    @CompleteDSLPckg_StructuralFeature.setter
    def CompleteDSLPckg_StructuralFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_StructuralFeature__CompleteDSLPckg_StructuralFeature", None)
        self.__CompleteDSLPckg_StructuralFeature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Slot"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Slot", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_Slot", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Slot"):
                opp_val = getattr(value, "CompleteDSLPckg_Slot", None)
                setattr(value, "CompleteDSLPckg_Slot", self)

class CompleteDSLPckg_ObjectNode(ActivityNode, TypedElement):

    pass
class Relationship:

    pass
class CompleteDSLPckg_Association(Relationship, Classifier):

    def __init__(self, isDerived: bool, Association: "CompleteDSLPckg_Property" = None, Association120: "CompleteDSLPckg_Property" = None, association: set["CompleteDSLPckg_Property"] = None, owningAssociation: set["CompleteDSLPckg_Property"] = None, CompleteDSLPckg_Association: set["CompleteDSLPckg_Property"] = None, CompleteDSLPckg_Association325: "CompleteDSLPckg_ConnectorEnd" = None):
        self.isDerived = isDerived
        self.Association = Association
        self.Association120 = Association120
        self.association = association if association is not None else set()
        self.owningAssociation = owningAssociation if owningAssociation is not None else set()
        self.CompleteDSLPckg_Association = CompleteDSLPckg_Association if CompleteDSLPckg_Association is not None else set()
        self.CompleteDSLPckg_Association325 = CompleteDSLPckg_Association325
        
        pass
    @property
    def isDerived(self):
        return self.__isDerived

    @isDerived.setter
    def isDerived(self, isDerived: bool):
        self.__isDerived = isDerived


    @property
    def Association(self):
        return self.__Association

    @Association.setter
    def Association(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Association__Association", None)
        self.__Association = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "memberEnd"):
                opp_val = getattr(old_value, "memberEnd", None)
                if opp_val == self:
                    setattr(old_value, "memberEnd", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "memberEnd"):
                opp_val = getattr(value, "memberEnd", None)
                setattr(value, "memberEnd", self)

    @property
    def owningAssociation(self):
        return self.__owningAssociation

    @owningAssociation.setter
    def owningAssociation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Association__owningAssociation", None)
        self.__owningAssociation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Property183"):
                    opp_val = getattr(item, "Property183", None)
                    
                    if opp_val == self:
                        setattr(item, "Property183", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Property183"):
                    opp_val = getattr(item, "Property183", None)
                    
                    setattr(item, "Property183", self)
                    

    @property
    def CompleteDSLPckg_Association(self):
        return self.__CompleteDSLPckg_Association

    @CompleteDSLPckg_Association.setter
    def CompleteDSLPckg_Association(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Association__CompleteDSLPckg_Association", None)
        self.__CompleteDSLPckg_Association = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_Property179"):
                    opp_val = getattr(item, "CompleteDSLPckg_Property179", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_Property179", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_Property179"):
                    opp_val = getattr(item, "CompleteDSLPckg_Property179", None)
                    
                    setattr(item, "CompleteDSLPckg_Property179", self)
                    

    @property
    def association(self):
        return self.__association

    @association.setter
    def association(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Association__association", None)
        self.__association = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Property181"):
                    opp_val = getattr(item, "Property181", None)
                    
                    if opp_val == self:
                        setattr(item, "Property181", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Property181"):
                    opp_val = getattr(item, "Property181", None)
                    
                    setattr(item, "Property181", self)
                    

    @property
    def CompleteDSLPckg_Association325(self):
        return self.__CompleteDSLPckg_Association325

    @CompleteDSLPckg_Association325.setter
    def CompleteDSLPckg_Association325(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Association__CompleteDSLPckg_Association325", None)
        self.__CompleteDSLPckg_Association325 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_ConnectorEnd324"):
                opp_val = getattr(old_value, "CompleteDSLPckg_ConnectorEnd324", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_ConnectorEnd324", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_ConnectorEnd324"):
                opp_val = getattr(value, "CompleteDSLPckg_ConnectorEnd324", None)
                setattr(value, "CompleteDSLPckg_ConnectorEnd324", self)

    @property
    def Association120(self):
        return self.__Association120

    @Association120.setter
    def Association120(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Association__Association120", None)
        self.__Association120 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownedEnd"):
                opp_val = getattr(old_value, "ownedEnd", None)
                if opp_val == self:
                    setattr(old_value, "ownedEnd", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedEnd"):
                opp_val = getattr(value, "ownedEnd", None)
                setattr(value, "ownedEnd", self)

class CompleteDSLPckg_DirectedRelationship(Relationship):

    pass
class PackageableElement:

    pass
class CompleteDSLPckg_Type(PackageableElement):

    pass
class CompleteDSLPckg_GeneralizationSet(PackageableElement):

    def __init__(self, isDisjoint: bool, isCovering: bool, GeneralizationSet: "CompleteDSLPckg_Classifier" = None, GeneralizationSet136: "CompleteDSLPckg_Generalization" = None, powertypeExtent: "CompleteDSLPckg_Classifier" = None, generalizationSet: set["CompleteDSLPckg_Generalization"] = None):
        self.isDisjoint = isDisjoint
        self.isCovering = isCovering
        self.GeneralizationSet = GeneralizationSet
        self.GeneralizationSet136 = GeneralizationSet136
        self.powertypeExtent = powertypeExtent
        self.generalizationSet = generalizationSet if generalizationSet is not None else set()
        
        pass
    @property
    def isDisjoint(self):
        return self.__isDisjoint

    @isDisjoint.setter
    def isDisjoint(self, isDisjoint: bool):
        self.__isDisjoint = isDisjoint


    @property
    def isCovering(self):
        return self.__isCovering

    @isCovering.setter
    def isCovering(self, isCovering: bool):
        self.__isCovering = isCovering


    @property
    def powertypeExtent(self):
        return self.__powertypeExtent

    @powertypeExtent.setter
    def powertypeExtent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_GeneralizationSet__powertypeExtent", None)
        self.__powertypeExtent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Classifier228"):
                opp_val = getattr(old_value, "Classifier228", None)
                if opp_val == self:
                    setattr(old_value, "Classifier228", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Classifier228"):
                opp_val = getattr(value, "Classifier228", None)
                setattr(value, "Classifier228", self)

    @property
    def GeneralizationSet136(self):
        return self.__GeneralizationSet136

    @GeneralizationSet136.setter
    def GeneralizationSet136(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_GeneralizationSet__GeneralizationSet136", None)
        self.__GeneralizationSet136 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "generalization135"):
                opp_val = getattr(old_value, "generalization135", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "generalization135"):
                opp_val = getattr(value, "generalization135", None)
                if opp_val is None:
                    setattr(value, "generalization135", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def GeneralizationSet(self):
        return self.__GeneralizationSet

    @GeneralizationSet.setter
    def GeneralizationSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_GeneralizationSet__GeneralizationSet", None)
        self.__GeneralizationSet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "powertype"):
                opp_val = getattr(old_value, "powertype", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "powertype"):
                opp_val = getattr(value, "powertype", None)
                if opp_val is None:
                    setattr(value, "powertype", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def generalizationSet(self):
        return self.__generalizationSet

    @generalizationSet.setter
    def generalizationSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_GeneralizationSet__generalizationSet", None)
        self.__generalizationSet = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Generalization230"):
                    opp_val = getattr(item, "Generalization230", None)
                    
                    if opp_val == self:
                        setattr(item, "Generalization230", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Generalization230"):
                    opp_val = getattr(item, "Generalization230", None)
                    
                    setattr(item, "Generalization230", self)
                    

class CompleteDSLPckg_Event(PackageableElement):

    pass
class CompleteDSLPckg_ValueSpecification(PackageableElement, TypedElement):

    pass
class CompleteDSLPckg_Observation(PackageableElement):

    pass
class CompleteDSLPckg_InstanceSpecification(PackageableElement):

    pass
class Namespace:

    pass
class CompleteDSLPckg_StructuredActivityNode(Action, Namespace, ActivityGroup, ExecutableNode):

    def __init__(self, mustIsolate: bool, CompleteDSLPckg_StructuredActivityNode: "CompleteDSLPckg_Activity" = None, CompleteDSLPckg_StructuredActivityNode756: "CompleteDSLPckg_ActivityEdge" = None, CompleteDSLPckg_StructuredActivityNode712: "CompleteDSLPckg_ActivityNode" = None, CompleteDSLPckg_StructuredActivityNode799: "CompleteDSLPckg_Activity" = None, CompleteDSLPckg_StructuredActivityNode802: set["CompleteDSLPckg_Variable"] = None, CompleteDSLPckg_StructuredActivityNode805: set["CompleteDSLPckg_ActivityNode"] = None, CompleteDSLPckg_StructuredActivityNode808: set["CompleteDSLPckg_InputPin"] = None, CompleteDSLPckg_StructuredActivityNode811: set["CompleteDSLPckg_ActivityEdge"] = None, CompleteDSLPckg_StructuredActivityNode814: set["CompleteDSLPckg_OutputPin"] = None):
        self.mustIsolate = mustIsolate
        self.CompleteDSLPckg_StructuredActivityNode = CompleteDSLPckg_StructuredActivityNode
        self.CompleteDSLPckg_StructuredActivityNode756 = CompleteDSLPckg_StructuredActivityNode756
        self.CompleteDSLPckg_StructuredActivityNode712 = CompleteDSLPckg_StructuredActivityNode712
        self.CompleteDSLPckg_StructuredActivityNode799 = CompleteDSLPckg_StructuredActivityNode799
        self.CompleteDSLPckg_StructuredActivityNode802 = CompleteDSLPckg_StructuredActivityNode802 if CompleteDSLPckg_StructuredActivityNode802 is not None else set()
        self.CompleteDSLPckg_StructuredActivityNode805 = CompleteDSLPckg_StructuredActivityNode805 if CompleteDSLPckg_StructuredActivityNode805 is not None else set()
        self.CompleteDSLPckg_StructuredActivityNode808 = CompleteDSLPckg_StructuredActivityNode808 if CompleteDSLPckg_StructuredActivityNode808 is not None else set()
        self.CompleteDSLPckg_StructuredActivityNode811 = CompleteDSLPckg_StructuredActivityNode811 if CompleteDSLPckg_StructuredActivityNode811 is not None else set()
        self.CompleteDSLPckg_StructuredActivityNode814 = CompleteDSLPckg_StructuredActivityNode814 if CompleteDSLPckg_StructuredActivityNode814 is not None else set()
        
        pass
    @property
    def mustIsolate(self):
        return self.__mustIsolate

    @mustIsolate.setter
    def mustIsolate(self, mustIsolate: bool):
        self.__mustIsolate = mustIsolate


    @property
    def CompleteDSLPckg_StructuredActivityNode756(self):
        return self.__CompleteDSLPckg_StructuredActivityNode756

    @CompleteDSLPckg_StructuredActivityNode756.setter
    def CompleteDSLPckg_StructuredActivityNode756(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_StructuredActivityNode__CompleteDSLPckg_StructuredActivityNode756", None)
        self.__CompleteDSLPckg_StructuredActivityNode756 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_ActivityEdge755"):
                opp_val = getattr(old_value, "CompleteDSLPckg_ActivityEdge755", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_ActivityEdge755", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_ActivityEdge755"):
                opp_val = getattr(value, "CompleteDSLPckg_ActivityEdge755", None)
                setattr(value, "CompleteDSLPckg_ActivityEdge755", self)

    @property
    def CompleteDSLPckg_StructuredActivityNode814(self):
        return self.__CompleteDSLPckg_StructuredActivityNode814

    @CompleteDSLPckg_StructuredActivityNode814.setter
    def CompleteDSLPckg_StructuredActivityNode814(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_StructuredActivityNode__CompleteDSLPckg_StructuredActivityNode814", None)
        self.__CompleteDSLPckg_StructuredActivityNode814 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_OutputPin815"):
                    opp_val = getattr(item, "CompleteDSLPckg_OutputPin815", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_OutputPin815", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_OutputPin815"):
                    opp_val = getattr(item, "CompleteDSLPckg_OutputPin815", None)
                    
                    setattr(item, "CompleteDSLPckg_OutputPin815", self)
                    

    @property
    def CompleteDSLPckg_StructuredActivityNode808(self):
        return self.__CompleteDSLPckg_StructuredActivityNode808

    @CompleteDSLPckg_StructuredActivityNode808.setter
    def CompleteDSLPckg_StructuredActivityNode808(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_StructuredActivityNode__CompleteDSLPckg_StructuredActivityNode808", None)
        self.__CompleteDSLPckg_StructuredActivityNode808 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_InputPin809"):
                    opp_val = getattr(item, "CompleteDSLPckg_InputPin809", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_InputPin809", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_InputPin809"):
                    opp_val = getattr(item, "CompleteDSLPckg_InputPin809", None)
                    
                    setattr(item, "CompleteDSLPckg_InputPin809", self)
                    

    @property
    def CompleteDSLPckg_StructuredActivityNode802(self):
        return self.__CompleteDSLPckg_StructuredActivityNode802

    @CompleteDSLPckg_StructuredActivityNode802.setter
    def CompleteDSLPckg_StructuredActivityNode802(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_StructuredActivityNode__CompleteDSLPckg_StructuredActivityNode802", None)
        self.__CompleteDSLPckg_StructuredActivityNode802 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_Variable803"):
                    opp_val = getattr(item, "CompleteDSLPckg_Variable803", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_Variable803", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_Variable803"):
                    opp_val = getattr(item, "CompleteDSLPckg_Variable803", None)
                    
                    setattr(item, "CompleteDSLPckg_Variable803", self)
                    

    @property
    def CompleteDSLPckg_StructuredActivityNode811(self):
        return self.__CompleteDSLPckg_StructuredActivityNode811

    @CompleteDSLPckg_StructuredActivityNode811.setter
    def CompleteDSLPckg_StructuredActivityNode811(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_StructuredActivityNode__CompleteDSLPckg_StructuredActivityNode811", None)
        self.__CompleteDSLPckg_StructuredActivityNode811 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_ActivityEdge812"):
                    opp_val = getattr(item, "CompleteDSLPckg_ActivityEdge812", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_ActivityEdge812", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_ActivityEdge812"):
                    opp_val = getattr(item, "CompleteDSLPckg_ActivityEdge812", None)
                    
                    setattr(item, "CompleteDSLPckg_ActivityEdge812", self)
                    

    @property
    def CompleteDSLPckg_StructuredActivityNode799(self):
        return self.__CompleteDSLPckg_StructuredActivityNode799

    @CompleteDSLPckg_StructuredActivityNode799.setter
    def CompleteDSLPckg_StructuredActivityNode799(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_StructuredActivityNode__CompleteDSLPckg_StructuredActivityNode799", None)
        self.__CompleteDSLPckg_StructuredActivityNode799 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Activity800"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Activity800", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_Activity800", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Activity800"):
                opp_val = getattr(value, "CompleteDSLPckg_Activity800", None)
                setattr(value, "CompleteDSLPckg_Activity800", self)

    @property
    def CompleteDSLPckg_StructuredActivityNode(self):
        return self.__CompleteDSLPckg_StructuredActivityNode

    @CompleteDSLPckg_StructuredActivityNode.setter
    def CompleteDSLPckg_StructuredActivityNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_StructuredActivityNode__CompleteDSLPckg_StructuredActivityNode", None)
        self.__CompleteDSLPckg_StructuredActivityNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Activity689"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Activity689", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Activity689"):
                opp_val = getattr(value, "CompleteDSLPckg_Activity689", None)
                if opp_val is None:
                    setattr(value, "CompleteDSLPckg_Activity689", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CompleteDSLPckg_StructuredActivityNode805(self):
        return self.__CompleteDSLPckg_StructuredActivityNode805

    @CompleteDSLPckg_StructuredActivityNode805.setter
    def CompleteDSLPckg_StructuredActivityNode805(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_StructuredActivityNode__CompleteDSLPckg_StructuredActivityNode805", None)
        self.__CompleteDSLPckg_StructuredActivityNode805 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_ActivityNode806"):
                    opp_val = getattr(item, "CompleteDSLPckg_ActivityNode806", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_ActivityNode806", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_ActivityNode806"):
                    opp_val = getattr(item, "CompleteDSLPckg_ActivityNode806", None)
                    
                    setattr(item, "CompleteDSLPckg_ActivityNode806", self)
                    

    @property
    def CompleteDSLPckg_StructuredActivityNode712(self):
        return self.__CompleteDSLPckg_StructuredActivityNode712

    @CompleteDSLPckg_StructuredActivityNode712.setter
    def CompleteDSLPckg_StructuredActivityNode712(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_StructuredActivityNode__CompleteDSLPckg_StructuredActivityNode712", None)
        self.__CompleteDSLPckg_StructuredActivityNode712 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_ActivityNode711"):
                opp_val = getattr(old_value, "CompleteDSLPckg_ActivityNode711", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_ActivityNode711", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_ActivityNode711"):
                opp_val = getattr(value, "CompleteDSLPckg_ActivityNode711", None)
                setattr(value, "CompleteDSLPckg_ActivityNode711", self)

class CompleteDSLPckg_Classifier(Namespace, Type, RedefinableElement):

    def __init__(self, isAbstract: bool, isFinalSpecialization: bool, CompleteDSLPckg_Classifier83: "CompleteDSLPckg_RedefinableElement" = None, CompleteDSLPckg_Classifier85: set["CompleteDSLPckg_NamedElement"] = None, featuringClassifier: set["CompleteDSLPckg_Feature"] = None, CompleteDSLPckg_Classifier89: set["CompleteDSLPckg_Property"] = None, CompleteDSLPckg_Classifier95: "CompleteDSLPckg_Classifier" = None, CompleteDSLPckg_Classifier93: set["CompleteDSLPckg_Classifier"] = None, specific: set["CompleteDSLPckg_Generalization"] = None, substitutingClassifier: set["CompleteDSLPckg_Substitution"] = None, powertype: set["CompleteDSLPckg_GeneralizationSet"] = None, CompleteDSLPckg_Classifier100: set["CompleteDSLPckg_CollaborationUse"] = None, CompleteDSLPckg_Classifier102: "CompleteDSLPckg_CollaborationUse" = None, Classifier: "CompleteDSLPckg_Feature" = None, CompleteDSLPckg_Classifier92: "CompleteDSLPckg_Classifier" = None, CompleteDSLPckg_Classifier90: set["CompleteDSLPckg_Classifier"] = None, CompleteDSLPckg_Classifier: "CompleteDSLPckg_InstanceSpecification" = None, Classifier202: "CompleteDSLPckg_Substitution" = None, CompleteDSLPckg_Classifier204: "CompleteDSLPckg_Substitution" = None, CompleteDSLPckg_Classifier206: "CompleteDSLPckg_Interface" = None, CompleteDSLPckg_Classifier131: "CompleteDSLPckg_Generalization" = None, Classifier133: "CompleteDSLPckg_Generalization" = None, CompleteDSLPckg_Classifier168: "CompleteDSLPckg_Class" = None, Classifier228: "CompleteDSLPckg_GeneralizationSet" = None, CompleteDSLPckg_Classifier393: "CompleteDSLPckg_Action" = None, CompleteDSLPckg_Classifier310: "CompleteDSLPckg_ComponentRealization" = None, CompleteDSLPckg_Classifier427: "CompleteDSLPckg_CreateObjectAction" = None, CompleteDSLPckg_Classifier496: "CompleteDSLPckg_UnmarshallAction" = None, CompleteDSLPckg_Classifier511: "CompleteDSLPckg_ReadExtendAction" = None, CompleteDSLPckg_Classifier516: "CompleteDSLPckg_ReclassifyObjectAction" = None, CompleteDSLPckg_Classifier519: "CompleteDSLPckg_ReclassifyObjectAction" = None, CompleteDSLPckg_Classifier871: "CompleteDSLPckg_ExceptionHandler" = None, CompleteDSLPckg_Classifier984: "CompleteDSLPckg_UseCase" = None):
        self.isAbstract = isAbstract
        self.isFinalSpecialization = isFinalSpecialization
        self.CompleteDSLPckg_Classifier83 = CompleteDSLPckg_Classifier83
        self.CompleteDSLPckg_Classifier85 = CompleteDSLPckg_Classifier85 if CompleteDSLPckg_Classifier85 is not None else set()
        self.featuringClassifier = featuringClassifier if featuringClassifier is not None else set()
        self.CompleteDSLPckg_Classifier89 = CompleteDSLPckg_Classifier89 if CompleteDSLPckg_Classifier89 is not None else set()
        self.CompleteDSLPckg_Classifier95 = CompleteDSLPckg_Classifier95
        self.CompleteDSLPckg_Classifier93 = CompleteDSLPckg_Classifier93 if CompleteDSLPckg_Classifier93 is not None else set()
        self.specific = specific if specific is not None else set()
        self.substitutingClassifier = substitutingClassifier if substitutingClassifier is not None else set()
        self.powertype = powertype if powertype is not None else set()
        self.CompleteDSLPckg_Classifier100 = CompleteDSLPckg_Classifier100 if CompleteDSLPckg_Classifier100 is not None else set()
        self.CompleteDSLPckg_Classifier102 = CompleteDSLPckg_Classifier102
        self.Classifier = Classifier
        self.CompleteDSLPckg_Classifier92 = CompleteDSLPckg_Classifier92
        self.CompleteDSLPckg_Classifier90 = CompleteDSLPckg_Classifier90 if CompleteDSLPckg_Classifier90 is not None else set()
        self.CompleteDSLPckg_Classifier = CompleteDSLPckg_Classifier
        self.Classifier202 = Classifier202
        self.CompleteDSLPckg_Classifier204 = CompleteDSLPckg_Classifier204
        self.CompleteDSLPckg_Classifier206 = CompleteDSLPckg_Classifier206
        self.CompleteDSLPckg_Classifier131 = CompleteDSLPckg_Classifier131
        self.Classifier133 = Classifier133
        self.CompleteDSLPckg_Classifier168 = CompleteDSLPckg_Classifier168
        self.Classifier228 = Classifier228
        self.CompleteDSLPckg_Classifier393 = CompleteDSLPckg_Classifier393
        self.CompleteDSLPckg_Classifier310 = CompleteDSLPckg_Classifier310
        self.CompleteDSLPckg_Classifier427 = CompleteDSLPckg_Classifier427
        self.CompleteDSLPckg_Classifier496 = CompleteDSLPckg_Classifier496
        self.CompleteDSLPckg_Classifier511 = CompleteDSLPckg_Classifier511
        self.CompleteDSLPckg_Classifier516 = CompleteDSLPckg_Classifier516
        self.CompleteDSLPckg_Classifier519 = CompleteDSLPckg_Classifier519
        self.CompleteDSLPckg_Classifier871 = CompleteDSLPckg_Classifier871
        self.CompleteDSLPckg_Classifier984 = CompleteDSLPckg_Classifier984
        
        pass
    @property
    def isAbstract(self):
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: bool):
        self.__isAbstract = isAbstract


    @property
    def isFinalSpecialization(self):
        return self.__isFinalSpecialization

    @isFinalSpecialization.setter
    def isFinalSpecialization(self, isFinalSpecialization: bool):
        self.__isFinalSpecialization = isFinalSpecialization


    @property
    def Classifier202(self):
        return self.__Classifier202

    @Classifier202.setter
    def Classifier202(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Classifier__Classifier202", None)
        self.__Classifier202 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "substitution"):
                opp_val = getattr(old_value, "substitution", None)
                if opp_val == self:
                    setattr(old_value, "substitution", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "substitution"):
                opp_val = getattr(value, "substitution", None)
                setattr(value, "substitution", self)

    @property
    def CompleteDSLPckg_Classifier427(self):
        return self.__CompleteDSLPckg_Classifier427

    @CompleteDSLPckg_Classifier427.setter
    def CompleteDSLPckg_Classifier427(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Classifier__CompleteDSLPckg_Classifier427", None)
        self.__CompleteDSLPckg_Classifier427 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_CreateObjectAction"):
                opp_val = getattr(old_value, "CompleteDSLPckg_CreateObjectAction", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_CreateObjectAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_CreateObjectAction"):
                opp_val = getattr(value, "CompleteDSLPckg_CreateObjectAction", None)
                setattr(value, "CompleteDSLPckg_CreateObjectAction", self)

    @property
    def CompleteDSLPckg_Classifier92(self):
        return self.__CompleteDSLPckg_Classifier92

    @CompleteDSLPckg_Classifier92.setter
    def CompleteDSLPckg_Classifier92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Classifier__CompleteDSLPckg_Classifier92", None)
        self.__CompleteDSLPckg_Classifier92 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Classifier90"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Classifier90", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Classifier90"):
                opp_val = getattr(value, "CompleteDSLPckg_Classifier90", None)
                if opp_val is None:
                    setattr(value, "CompleteDSLPckg_Classifier90", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CompleteDSLPckg_Classifier871(self):
        return self.__CompleteDSLPckg_Classifier871

    @CompleteDSLPckg_Classifier871.setter
    def CompleteDSLPckg_Classifier871(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Classifier__CompleteDSLPckg_Classifier871", None)
        self.__CompleteDSLPckg_Classifier871 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_ExceptionHandler870"):
                opp_val = getattr(old_value, "CompleteDSLPckg_ExceptionHandler870", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_ExceptionHandler870"):
                opp_val = getattr(value, "CompleteDSLPckg_ExceptionHandler870", None)
                if opp_val is None:
                    setattr(value, "CompleteDSLPckg_ExceptionHandler870", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CompleteDSLPckg_Classifier496(self):
        return self.__CompleteDSLPckg_Classifier496

    @CompleteDSLPckg_Classifier496.setter
    def CompleteDSLPckg_Classifier496(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Classifier__CompleteDSLPckg_Classifier496", None)
        self.__CompleteDSLPckg_Classifier496 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_UnmarshallAction495"):
                opp_val = getattr(old_value, "CompleteDSLPckg_UnmarshallAction495", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_UnmarshallAction495", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_UnmarshallAction495"):
                opp_val = getattr(value, "CompleteDSLPckg_UnmarshallAction495", None)
                setattr(value, "CompleteDSLPckg_UnmarshallAction495", self)

    @property
    def CompleteDSLPckg_Classifier206(self):
        return self.__CompleteDSLPckg_Classifier206

    @CompleteDSLPckg_Classifier206.setter
    def CompleteDSLPckg_Classifier206(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Classifier__CompleteDSLPckg_Classifier206", None)
        self.__CompleteDSLPckg_Classifier206 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Interface"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Interface", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_Interface", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Interface"):
                opp_val = getattr(value, "CompleteDSLPckg_Interface", None)
                setattr(value, "CompleteDSLPckg_Interface", self)

    @property
    def powertype(self):
        return self.__powertype

    @powertype.setter
    def powertype(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Classifier__powertype", None)
        self.__powertype = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GeneralizationSet"):
                    opp_val = getattr(item, "GeneralizationSet", None)
                    
                    if opp_val == self:
                        setattr(item, "GeneralizationSet", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GeneralizationSet"):
                    opp_val = getattr(item, "GeneralizationSet", None)
                    
                    setattr(item, "GeneralizationSet", self)
                    

    @property
    def CompleteDSLPckg_Classifier(self):
        return self.__CompleteDSLPckg_Classifier

    @CompleteDSLPckg_Classifier.setter
    def CompleteDSLPckg_Classifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Classifier__CompleteDSLPckg_Classifier", None)
        self.__CompleteDSLPckg_Classifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_InstanceSpecification67"):
                opp_val = getattr(old_value, "CompleteDSLPckg_InstanceSpecification67", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_InstanceSpecification67"):
                opp_val = getattr(value, "CompleteDSLPckg_InstanceSpecification67", None)
                if opp_val is None:
                    setattr(value, "CompleteDSLPckg_InstanceSpecification67", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CompleteDSLPckg_Classifier204(self):
        return self.__CompleteDSLPckg_Classifier204

    @CompleteDSLPckg_Classifier204.setter
    def CompleteDSLPckg_Classifier204(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Classifier__CompleteDSLPckg_Classifier204", None)
        self.__CompleteDSLPckg_Classifier204 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Substitution"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Substitution", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_Substitution", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Substitution"):
                opp_val = getattr(value, "CompleteDSLPckg_Substitution", None)
                setattr(value, "CompleteDSLPckg_Substitution", self)

    @property
    def CompleteDSLPckg_Classifier511(self):
        return self.__CompleteDSLPckg_Classifier511

    @CompleteDSLPckg_Classifier511.setter
    def CompleteDSLPckg_Classifier511(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Classifier__CompleteDSLPckg_Classifier511", None)
        self.__CompleteDSLPckg_Classifier511 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_ReadExtendAction510"):
                opp_val = getattr(old_value, "CompleteDSLPckg_ReadExtendAction510", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_ReadExtendAction510", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_ReadExtendAction510"):
                opp_val = getattr(value, "CompleteDSLPckg_ReadExtendAction510", None)
                setattr(value, "CompleteDSLPckg_ReadExtendAction510", self)

    @property
    def specific(self):
        return self.__specific

    @specific.setter
    def specific(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Classifier__specific", None)
        self.__specific = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Generalization"):
                    opp_val = getattr(item, "Generalization", None)
                    
                    if opp_val == self:
                        setattr(item, "Generalization", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Generalization"):
                    opp_val = getattr(item, "Generalization", None)
                    
                    setattr(item, "Generalization", self)
                    

    @property
    def CompleteDSLPckg_Classifier93(self):
        return self.__CompleteDSLPckg_Classifier93

    @CompleteDSLPckg_Classifier93.setter
    def CompleteDSLPckg_Classifier93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Classifier__CompleteDSLPckg_Classifier93", None)
        self.__CompleteDSLPckg_Classifier93 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_Classifier95"):
                    opp_val = getattr(item, "CompleteDSLPckg_Classifier95", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_Classifier95", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_Classifier95"):
                    opp_val = getattr(item, "CompleteDSLPckg_Classifier95", None)
                    
                    setattr(item, "CompleteDSLPckg_Classifier95", self)
                    

    @property
    def Classifier133(self):
        return self.__Classifier133

    @Classifier133.setter
    def Classifier133(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Classifier__Classifier133", None)
        self.__Classifier133 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "generalization"):
                opp_val = getattr(old_value, "generalization", None)
                if opp_val == self:
                    setattr(old_value, "generalization", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "generalization"):
                opp_val = getattr(value, "generalization", None)
                setattr(value, "generalization", self)

    @property
    def CompleteDSLPckg_Classifier85(self):
        return self.__CompleteDSLPckg_Classifier85

    @CompleteDSLPckg_Classifier85.setter
    def CompleteDSLPckg_Classifier85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Classifier__CompleteDSLPckg_Classifier85", None)
        self.__CompleteDSLPckg_Classifier85 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_NamedElement86"):
                    opp_val = getattr(item, "CompleteDSLPckg_NamedElement86", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_NamedElement86", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_NamedElement86"):
                    opp_val = getattr(item, "CompleteDSLPckg_NamedElement86", None)
                    
                    setattr(item, "CompleteDSLPckg_NamedElement86", self)
                    

    @property
    def CompleteDSLPckg_Classifier95(self):
        return self.__CompleteDSLPckg_Classifier95

    @CompleteDSLPckg_Classifier95.setter
    def CompleteDSLPckg_Classifier95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Classifier__CompleteDSLPckg_Classifier95", None)
        self.__CompleteDSLPckg_Classifier95 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Classifier93"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Classifier93", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Classifier93"):
                opp_val = getattr(value, "CompleteDSLPckg_Classifier93", None)
                if opp_val is None:
                    setattr(value, "CompleteDSLPckg_Classifier93", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CompleteDSLPckg_Classifier90(self):
        return self.__CompleteDSLPckg_Classifier90

    @CompleteDSLPckg_Classifier90.setter
    def CompleteDSLPckg_Classifier90(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Classifier__CompleteDSLPckg_Classifier90", None)
        self.__CompleteDSLPckg_Classifier90 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_Classifier92"):
                    opp_val = getattr(item, "CompleteDSLPckg_Classifier92", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_Classifier92", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_Classifier92"):
                    opp_val = getattr(item, "CompleteDSLPckg_Classifier92", None)
                    
                    setattr(item, "CompleteDSLPckg_Classifier92", self)
                    

    @property
    def featuringClassifier(self):
        return self.__featuringClassifier

    @featuringClassifier.setter
    def featuringClassifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Classifier__featuringClassifier", None)
        self.__featuringClassifier = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Feature"):
                    opp_val = getattr(item, "Feature", None)
                    
                    if opp_val == self:
                        setattr(item, "Feature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Feature"):
                    opp_val = getattr(item, "Feature", None)
                    
                    setattr(item, "Feature", self)
                    

    @property
    def CompleteDSLPckg_Classifier102(self):
        return self.__CompleteDSLPckg_Classifier102

    @CompleteDSLPckg_Classifier102.setter
    def CompleteDSLPckg_Classifier102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Classifier__CompleteDSLPckg_Classifier102", None)
        self.__CompleteDSLPckg_Classifier102 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_CollaborationUse103"):
                opp_val = getattr(old_value, "CompleteDSLPckg_CollaborationUse103", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_CollaborationUse103", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_CollaborationUse103"):
                opp_val = getattr(value, "CompleteDSLPckg_CollaborationUse103", None)
                setattr(value, "CompleteDSLPckg_CollaborationUse103", self)

    @property
    def Classifier(self):
        return self.__Classifier

    @Classifier.setter
    def Classifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Classifier__Classifier", None)
        self.__Classifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "feature"):
                opp_val = getattr(old_value, "feature", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "feature"):
                opp_val = getattr(value, "feature", None)
                if opp_val is None:
                    setattr(value, "feature", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CompleteDSLPckg_Classifier168(self):
        return self.__CompleteDSLPckg_Classifier168

    @CompleteDSLPckg_Classifier168.setter
    def CompleteDSLPckg_Classifier168(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Classifier__CompleteDSLPckg_Classifier168", None)
        self.__CompleteDSLPckg_Classifier168 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Class"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Class", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Class"):
                opp_val = getattr(value, "CompleteDSLPckg_Class", None)
                if opp_val is None:
                    setattr(value, "CompleteDSLPckg_Class", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def substitutingClassifier(self):
        return self.__substitutingClassifier

    @substitutingClassifier.setter
    def substitutingClassifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Classifier__substitutingClassifier", None)
        self.__substitutingClassifier = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Substitution"):
                    opp_val = getattr(item, "Substitution", None)
                    
                    if opp_val == self:
                        setattr(item, "Substitution", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Substitution"):
                    opp_val = getattr(item, "Substitution", None)
                    
                    setattr(item, "Substitution", self)
                    

    @property
    def CompleteDSLPckg_Classifier519(self):
        return self.__CompleteDSLPckg_Classifier519

    @CompleteDSLPckg_Classifier519.setter
    def CompleteDSLPckg_Classifier519(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Classifier__CompleteDSLPckg_Classifier519", None)
        self.__CompleteDSLPckg_Classifier519 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_ReclassifyObjectAction518"):
                opp_val = getattr(old_value, "CompleteDSLPckg_ReclassifyObjectAction518", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_ReclassifyObjectAction518"):
                opp_val = getattr(value, "CompleteDSLPckg_ReclassifyObjectAction518", None)
                if opp_val is None:
                    setattr(value, "CompleteDSLPckg_ReclassifyObjectAction518", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CompleteDSLPckg_Classifier984(self):
        return self.__CompleteDSLPckg_Classifier984

    @CompleteDSLPckg_Classifier984.setter
    def CompleteDSLPckg_Classifier984(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Classifier__CompleteDSLPckg_Classifier984", None)
        self.__CompleteDSLPckg_Classifier984 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_UseCase"):
                opp_val = getattr(old_value, "CompleteDSLPckg_UseCase", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_UseCase"):
                opp_val = getattr(value, "CompleteDSLPckg_UseCase", None)
                if opp_val is None:
                    setattr(value, "CompleteDSLPckg_UseCase", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CompleteDSLPckg_Classifier89(self):
        return self.__CompleteDSLPckg_Classifier89

    @CompleteDSLPckg_Classifier89.setter
    def CompleteDSLPckg_Classifier89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Classifier__CompleteDSLPckg_Classifier89", None)
        self.__CompleteDSLPckg_Classifier89 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_Property"):
                    opp_val = getattr(item, "CompleteDSLPckg_Property", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_Property", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_Property"):
                    opp_val = getattr(item, "CompleteDSLPckg_Property", None)
                    
                    setattr(item, "CompleteDSLPckg_Property", self)
                    

    @property
    def Classifier228(self):
        return self.__Classifier228

    @Classifier228.setter
    def Classifier228(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Classifier__Classifier228", None)
        self.__Classifier228 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "powertypeExtent"):
                opp_val = getattr(old_value, "powertypeExtent", None)
                if opp_val == self:
                    setattr(old_value, "powertypeExtent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "powertypeExtent"):
                opp_val = getattr(value, "powertypeExtent", None)
                setattr(value, "powertypeExtent", self)

    @property
    def CompleteDSLPckg_Classifier100(self):
        return self.__CompleteDSLPckg_Classifier100

    @CompleteDSLPckg_Classifier100.setter
    def CompleteDSLPckg_Classifier100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Classifier__CompleteDSLPckg_Classifier100", None)
        self.__CompleteDSLPckg_Classifier100 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_CollaborationUse"):
                    opp_val = getattr(item, "CompleteDSLPckg_CollaborationUse", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_CollaborationUse", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_CollaborationUse"):
                    opp_val = getattr(item, "CompleteDSLPckg_CollaborationUse", None)
                    
                    setattr(item, "CompleteDSLPckg_CollaborationUse", self)
                    

    @property
    def CompleteDSLPckg_Classifier393(self):
        return self.__CompleteDSLPckg_Classifier393

    @CompleteDSLPckg_Classifier393.setter
    def CompleteDSLPckg_Classifier393(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Classifier__CompleteDSLPckg_Classifier393", None)
        self.__CompleteDSLPckg_Classifier393 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Action"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Action", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_Action", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Action"):
                opp_val = getattr(value, "CompleteDSLPckg_Action", None)
                setattr(value, "CompleteDSLPckg_Action", self)

    @property
    def CompleteDSLPckg_Classifier83(self):
        return self.__CompleteDSLPckg_Classifier83

    @CompleteDSLPckg_Classifier83.setter
    def CompleteDSLPckg_Classifier83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Classifier__CompleteDSLPckg_Classifier83", None)
        self.__CompleteDSLPckg_Classifier83 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_RedefinableElement82"):
                opp_val = getattr(old_value, "CompleteDSLPckg_RedefinableElement82", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_RedefinableElement82"):
                opp_val = getattr(value, "CompleteDSLPckg_RedefinableElement82", None)
                if opp_val is None:
                    setattr(value, "CompleteDSLPckg_RedefinableElement82", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CompleteDSLPckg_Classifier310(self):
        return self.__CompleteDSLPckg_Classifier310

    @CompleteDSLPckg_Classifier310.setter
    def CompleteDSLPckg_Classifier310(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Classifier__CompleteDSLPckg_Classifier310", None)
        self.__CompleteDSLPckg_Classifier310 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_ComponentRealization309"):
                opp_val = getattr(old_value, "CompleteDSLPckg_ComponentRealization309", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_ComponentRealization309"):
                opp_val = getattr(value, "CompleteDSLPckg_ComponentRealization309", None)
                if opp_val is None:
                    setattr(value, "CompleteDSLPckg_ComponentRealization309", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CompleteDSLPckg_Classifier131(self):
        return self.__CompleteDSLPckg_Classifier131

    @CompleteDSLPckg_Classifier131.setter
    def CompleteDSLPckg_Classifier131(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Classifier__CompleteDSLPckg_Classifier131", None)
        self.__CompleteDSLPckg_Classifier131 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Generalization"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Generalization", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_Generalization", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Generalization"):
                opp_val = getattr(value, "CompleteDSLPckg_Generalization", None)
                setattr(value, "CompleteDSLPckg_Generalization", self)

    @property
    def CompleteDSLPckg_Classifier516(self):
        return self.__CompleteDSLPckg_Classifier516

    @CompleteDSLPckg_Classifier516.setter
    def CompleteDSLPckg_Classifier516(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Classifier__CompleteDSLPckg_Classifier516", None)
        self.__CompleteDSLPckg_Classifier516 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_ReclassifyObjectAction515"):
                opp_val = getattr(old_value, "CompleteDSLPckg_ReclassifyObjectAction515", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_ReclassifyObjectAction515"):
                opp_val = getattr(value, "CompleteDSLPckg_ReclassifyObjectAction515", None)
                if opp_val is None:
                    setattr(value, "CompleteDSLPckg_ReclassifyObjectAction515", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class CompleteDSLPckg_InteractionOperand(Namespace):

    pass
class CompleteDSLPckg_BehavioralFeature(Namespace, Feature):

    pass
class CompleteDSLPckg_Transition(Namespace, RedefinableElement):

    def __init__(self, kind: str, CompleteDSLPckg_Transition: "CompleteDSLPckg_Region" = None, CompleteDSLPckg_Transition597: "CompleteDSLPckg_Vertex" = None, CompleteDSLPckg_Transition608: "CompleteDSLPckg_Vertex" = None, CompleteDSLPckg_Transition611: "CompleteDSLPckg_Behavior" = None, CompleteDSLPckg_Transition614: "CompleteDSLPckg_Trigger" = None, CompleteDSLPckg_Transition617: "CompleteDSLPckg_Constraint" = None, CompleteDSLPckg_Transition620: "CompleteDSLPckg_Region" = None, CompleteDSLPckg_Transition624: "CompleteDSLPckg_Transition" = None, CompleteDSLPckg_Transition622: "CompleteDSLPckg_Transition" = None, CompleteDSLPckg_Transition600: "CompleteDSLPckg_Vertex" = None, CompleteDSLPckg_Transition605: "CompleteDSLPckg_Vertex" = None):
        self.kind = kind
        self.CompleteDSLPckg_Transition = CompleteDSLPckg_Transition
        self.CompleteDSLPckg_Transition597 = CompleteDSLPckg_Transition597
        self.CompleteDSLPckg_Transition608 = CompleteDSLPckg_Transition608
        self.CompleteDSLPckg_Transition611 = CompleteDSLPckg_Transition611
        self.CompleteDSLPckg_Transition614 = CompleteDSLPckg_Transition614
        self.CompleteDSLPckg_Transition617 = CompleteDSLPckg_Transition617
        self.CompleteDSLPckg_Transition620 = CompleteDSLPckg_Transition620
        self.CompleteDSLPckg_Transition624 = CompleteDSLPckg_Transition624
        self.CompleteDSLPckg_Transition622 = CompleteDSLPckg_Transition622
        self.CompleteDSLPckg_Transition600 = CompleteDSLPckg_Transition600
        self.CompleteDSLPckg_Transition605 = CompleteDSLPckg_Transition605
        
        pass
    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind


    @property
    def CompleteDSLPckg_Transition617(self):
        return self.__CompleteDSLPckg_Transition617

    @CompleteDSLPckg_Transition617.setter
    def CompleteDSLPckg_Transition617(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Transition__CompleteDSLPckg_Transition617", None)
        self.__CompleteDSLPckg_Transition617 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Constraint618"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Constraint618", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_Constraint618", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Constraint618"):
                opp_val = getattr(value, "CompleteDSLPckg_Constraint618", None)
                setattr(value, "CompleteDSLPckg_Constraint618", self)

    @property
    def CompleteDSLPckg_Transition608(self):
        return self.__CompleteDSLPckg_Transition608

    @CompleteDSLPckg_Transition608.setter
    def CompleteDSLPckg_Transition608(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Transition__CompleteDSLPckg_Transition608", None)
        self.__CompleteDSLPckg_Transition608 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Vertex609"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Vertex609", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_Vertex609", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Vertex609"):
                opp_val = getattr(value, "CompleteDSLPckg_Vertex609", None)
                setattr(value, "CompleteDSLPckg_Vertex609", self)

    @property
    def CompleteDSLPckg_Transition620(self):
        return self.__CompleteDSLPckg_Transition620

    @CompleteDSLPckg_Transition620.setter
    def CompleteDSLPckg_Transition620(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Transition__CompleteDSLPckg_Transition620", None)
        self.__CompleteDSLPckg_Transition620 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Region621"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Region621", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_Region621", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Region621"):
                opp_val = getattr(value, "CompleteDSLPckg_Region621", None)
                setattr(value, "CompleteDSLPckg_Region621", self)

    @property
    def CompleteDSLPckg_Transition605(self):
        return self.__CompleteDSLPckg_Transition605

    @CompleteDSLPckg_Transition605.setter
    def CompleteDSLPckg_Transition605(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Transition__CompleteDSLPckg_Transition605", None)
        self.__CompleteDSLPckg_Transition605 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Vertex606"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Vertex606", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_Vertex606", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Vertex606"):
                opp_val = getattr(value, "CompleteDSLPckg_Vertex606", None)
                setattr(value, "CompleteDSLPckg_Vertex606", self)

    @property
    def CompleteDSLPckg_Transition624(self):
        return self.__CompleteDSLPckg_Transition624

    @CompleteDSLPckg_Transition624.setter
    def CompleteDSLPckg_Transition624(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Transition__CompleteDSLPckg_Transition624", None)
        self.__CompleteDSLPckg_Transition624 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Transition622"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Transition622", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_Transition622", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Transition622"):
                opp_val = getattr(value, "CompleteDSLPckg_Transition622", None)
                setattr(value, "CompleteDSLPckg_Transition622", self)

    @property
    def CompleteDSLPckg_Transition597(self):
        return self.__CompleteDSLPckg_Transition597

    @CompleteDSLPckg_Transition597.setter
    def CompleteDSLPckg_Transition597(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Transition__CompleteDSLPckg_Transition597", None)
        self.__CompleteDSLPckg_Transition597 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Vertex596"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Vertex596", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Vertex596"):
                opp_val = getattr(value, "CompleteDSLPckg_Vertex596", None)
                if opp_val is None:
                    setattr(value, "CompleteDSLPckg_Vertex596", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CompleteDSLPckg_Transition(self):
        return self.__CompleteDSLPckg_Transition

    @CompleteDSLPckg_Transition.setter
    def CompleteDSLPckg_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Transition__CompleteDSLPckg_Transition", None)
        self.__CompleteDSLPckg_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Region588"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Region588", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Region588"):
                opp_val = getattr(value, "CompleteDSLPckg_Region588", None)
                if opp_val is None:
                    setattr(value, "CompleteDSLPckg_Region588", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CompleteDSLPckg_Transition600(self):
        return self.__CompleteDSLPckg_Transition600

    @CompleteDSLPckg_Transition600.setter
    def CompleteDSLPckg_Transition600(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Transition__CompleteDSLPckg_Transition600", None)
        self.__CompleteDSLPckg_Transition600 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Vertex599"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Vertex599", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Vertex599"):
                opp_val = getattr(value, "CompleteDSLPckg_Vertex599", None)
                if opp_val is None:
                    setattr(value, "CompleteDSLPckg_Vertex599", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CompleteDSLPckg_Transition622(self):
        return self.__CompleteDSLPckg_Transition622

    @CompleteDSLPckg_Transition622.setter
    def CompleteDSLPckg_Transition622(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Transition__CompleteDSLPckg_Transition622", None)
        self.__CompleteDSLPckg_Transition622 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Transition624"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Transition624", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_Transition624", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Transition624"):
                opp_val = getattr(value, "CompleteDSLPckg_Transition624", None)
                setattr(value, "CompleteDSLPckg_Transition624", self)

    @property
    def CompleteDSLPckg_Transition614(self):
        return self.__CompleteDSLPckg_Transition614

    @CompleteDSLPckg_Transition614.setter
    def CompleteDSLPckg_Transition614(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Transition__CompleteDSLPckg_Transition614", None)
        self.__CompleteDSLPckg_Transition614 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Trigger615"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Trigger615", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_Trigger615", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Trigger615"):
                opp_val = getattr(value, "CompleteDSLPckg_Trigger615", None)
                setattr(value, "CompleteDSLPckg_Trigger615", self)

    @property
    def CompleteDSLPckg_Transition611(self):
        return self.__CompleteDSLPckg_Transition611

    @CompleteDSLPckg_Transition611.setter
    def CompleteDSLPckg_Transition611(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Transition__CompleteDSLPckg_Transition611", None)
        self.__CompleteDSLPckg_Transition611 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Behavior612"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Behavior612", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_Behavior612", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Behavior612"):
                opp_val = getattr(value, "CompleteDSLPckg_Behavior612", None)
                setattr(value, "CompleteDSLPckg_Behavior612", self)

class CompleteDSLPckg_Region(Namespace, RedefinableElement):

    pass
class CompleteDSLPckg_State(Vertex, Namespace, RedefinableElement):

    def __init__(self, isComposite: bool, isOrthogonal: bool, isSimple: bool, isSubmachineState: bool, CompleteDSLPckg_State591: "CompleteDSLPckg_Region" = None, CompleteDSLPckg_State627: "CompleteDSLPckg_Pseudostate" = None, CompleteDSLPckg_State635: "CompleteDSLPckg_ConnectionPointReference" = None, CompleteDSLPckg_State637: set["CompleteDSLPckg_ConnectionPointReference"] = None, CompleteDSLPckg_State640: set["CompleteDSLPckg_Pseudostate"] = None, CompleteDSLPckg_State643: "CompleteDSLPckg_StateMachine" = None, CompleteDSLPckg_State: "CompleteDSLPckg_StateMachine" = None, CompleteDSLPckg_State646: set["CompleteDSLPckg_Region"] = None, CompleteDSLPckg_State649: set["CompleteDSLPckg_Trigger"] = None, CompleteDSLPckg_State652: "CompleteDSLPckg_Behavior" = None, CompleteDSLPckg_State655: "CompleteDSLPckg_Behavior" = None, CompleteDSLPckg_State658: "CompleteDSLPckg_Behavior" = None, CompleteDSLPckg_State661: "CompleteDSLPckg_Constraint" = None, CompleteDSLPckg_State665: "CompleteDSLPckg_State" = None, CompleteDSLPckg_State663: "CompleteDSLPckg_State" = None, CompleteDSLPckg_State764: "CompleteDSLPckg_ObjectFlow" = None):
        self.isComposite = isComposite
        self.isOrthogonal = isOrthogonal
        self.isSimple = isSimple
        self.isSubmachineState = isSubmachineState
        self.CompleteDSLPckg_State591 = CompleteDSLPckg_State591
        self.CompleteDSLPckg_State627 = CompleteDSLPckg_State627
        self.CompleteDSLPckg_State635 = CompleteDSLPckg_State635
        self.CompleteDSLPckg_State637 = CompleteDSLPckg_State637 if CompleteDSLPckg_State637 is not None else set()
        self.CompleteDSLPckg_State640 = CompleteDSLPckg_State640 if CompleteDSLPckg_State640 is not None else set()
        self.CompleteDSLPckg_State643 = CompleteDSLPckg_State643
        self.CompleteDSLPckg_State = CompleteDSLPckg_State
        self.CompleteDSLPckg_State646 = CompleteDSLPckg_State646 if CompleteDSLPckg_State646 is not None else set()
        self.CompleteDSLPckg_State649 = CompleteDSLPckg_State649 if CompleteDSLPckg_State649 is not None else set()
        self.CompleteDSLPckg_State652 = CompleteDSLPckg_State652
        self.CompleteDSLPckg_State655 = CompleteDSLPckg_State655
        self.CompleteDSLPckg_State658 = CompleteDSLPckg_State658
        self.CompleteDSLPckg_State661 = CompleteDSLPckg_State661
        self.CompleteDSLPckg_State665 = CompleteDSLPckg_State665
        self.CompleteDSLPckg_State663 = CompleteDSLPckg_State663
        self.CompleteDSLPckg_State764 = CompleteDSLPckg_State764
        
        pass
    @property
    def isSubmachineState(self):
        return self.__isSubmachineState

    @isSubmachineState.setter
    def isSubmachineState(self, isSubmachineState: bool):
        self.__isSubmachineState = isSubmachineState


    @property
    def isComposite(self):
        return self.__isComposite

    @isComposite.setter
    def isComposite(self, isComposite: bool):
        self.__isComposite = isComposite


    @property
    def isSimple(self):
        return self.__isSimple

    @isSimple.setter
    def isSimple(self, isSimple: bool):
        self.__isSimple = isSimple


    @property
    def isOrthogonal(self):
        return self.__isOrthogonal

    @isOrthogonal.setter
    def isOrthogonal(self, isOrthogonal: bool):
        self.__isOrthogonal = isOrthogonal


    @property
    def CompleteDSLPckg_State658(self):
        return self.__CompleteDSLPckg_State658

    @CompleteDSLPckg_State658.setter
    def CompleteDSLPckg_State658(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_State__CompleteDSLPckg_State658", None)
        self.__CompleteDSLPckg_State658 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Behavior659"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Behavior659", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_Behavior659", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Behavior659"):
                opp_val = getattr(value, "CompleteDSLPckg_Behavior659", None)
                setattr(value, "CompleteDSLPckg_Behavior659", self)

    @property
    def CompleteDSLPckg_State655(self):
        return self.__CompleteDSLPckg_State655

    @CompleteDSLPckg_State655.setter
    def CompleteDSLPckg_State655(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_State__CompleteDSLPckg_State655", None)
        self.__CompleteDSLPckg_State655 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Behavior656"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Behavior656", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_Behavior656", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Behavior656"):
                opp_val = getattr(value, "CompleteDSLPckg_Behavior656", None)
                setattr(value, "CompleteDSLPckg_Behavior656", self)

    @property
    def CompleteDSLPckg_State643(self):
        return self.__CompleteDSLPckg_State643

    @CompleteDSLPckg_State643.setter
    def CompleteDSLPckg_State643(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_State__CompleteDSLPckg_State643", None)
        self.__CompleteDSLPckg_State643 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_StateMachine644"):
                opp_val = getattr(old_value, "CompleteDSLPckg_StateMachine644", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_StateMachine644", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_StateMachine644"):
                opp_val = getattr(value, "CompleteDSLPckg_StateMachine644", None)
                setattr(value, "CompleteDSLPckg_StateMachine644", self)

    @property
    def CompleteDSLPckg_State764(self):
        return self.__CompleteDSLPckg_State764

    @CompleteDSLPckg_State764.setter
    def CompleteDSLPckg_State764(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_State__CompleteDSLPckg_State764", None)
        self.__CompleteDSLPckg_State764 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_ObjectFlow763"):
                opp_val = getattr(old_value, "CompleteDSLPckg_ObjectFlow763", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_ObjectFlow763"):
                opp_val = getattr(value, "CompleteDSLPckg_ObjectFlow763", None)
                if opp_val is None:
                    setattr(value, "CompleteDSLPckg_ObjectFlow763", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CompleteDSLPckg_State635(self):
        return self.__CompleteDSLPckg_State635

    @CompleteDSLPckg_State635.setter
    def CompleteDSLPckg_State635(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_State__CompleteDSLPckg_State635", None)
        self.__CompleteDSLPckg_State635 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_ConnectionPointReference634"):
                opp_val = getattr(old_value, "CompleteDSLPckg_ConnectionPointReference634", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_ConnectionPointReference634", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_ConnectionPointReference634"):
                opp_val = getattr(value, "CompleteDSLPckg_ConnectionPointReference634", None)
                setattr(value, "CompleteDSLPckg_ConnectionPointReference634", self)

    @property
    def CompleteDSLPckg_State661(self):
        return self.__CompleteDSLPckg_State661

    @CompleteDSLPckg_State661.setter
    def CompleteDSLPckg_State661(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_State__CompleteDSLPckg_State661", None)
        self.__CompleteDSLPckg_State661 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Constraint662"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Constraint662", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_Constraint662", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Constraint662"):
                opp_val = getattr(value, "CompleteDSLPckg_Constraint662", None)
                setattr(value, "CompleteDSLPckg_Constraint662", self)

    @property
    def CompleteDSLPckg_State627(self):
        return self.__CompleteDSLPckg_State627

    @CompleteDSLPckg_State627.setter
    def CompleteDSLPckg_State627(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_State__CompleteDSLPckg_State627", None)
        self.__CompleteDSLPckg_State627 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Pseudostate626"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Pseudostate626", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_Pseudostate626", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Pseudostate626"):
                opp_val = getattr(value, "CompleteDSLPckg_Pseudostate626", None)
                setattr(value, "CompleteDSLPckg_Pseudostate626", self)

    @property
    def CompleteDSLPckg_State665(self):
        return self.__CompleteDSLPckg_State665

    @CompleteDSLPckg_State665.setter
    def CompleteDSLPckg_State665(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_State__CompleteDSLPckg_State665", None)
        self.__CompleteDSLPckg_State665 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_State663"):
                opp_val = getattr(old_value, "CompleteDSLPckg_State663", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_State663", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_State663"):
                opp_val = getattr(value, "CompleteDSLPckg_State663", None)
                setattr(value, "CompleteDSLPckg_State663", self)

    @property
    def CompleteDSLPckg_State591(self):
        return self.__CompleteDSLPckg_State591

    @CompleteDSLPckg_State591.setter
    def CompleteDSLPckg_State591(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_State__CompleteDSLPckg_State591", None)
        self.__CompleteDSLPckg_State591 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Region590"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Region590", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_Region590", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Region590"):
                opp_val = getattr(value, "CompleteDSLPckg_Region590", None)
                setattr(value, "CompleteDSLPckg_Region590", self)

    @property
    def CompleteDSLPckg_State649(self):
        return self.__CompleteDSLPckg_State649

    @CompleteDSLPckg_State649.setter
    def CompleteDSLPckg_State649(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_State__CompleteDSLPckg_State649", None)
        self.__CompleteDSLPckg_State649 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_Trigger650"):
                    opp_val = getattr(item, "CompleteDSLPckg_Trigger650", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_Trigger650", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_Trigger650"):
                    opp_val = getattr(item, "CompleteDSLPckg_Trigger650", None)
                    
                    setattr(item, "CompleteDSLPckg_Trigger650", self)
                    

    @property
    def CompleteDSLPckg_State(self):
        return self.__CompleteDSLPckg_State

    @CompleteDSLPckg_State.setter
    def CompleteDSLPckg_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_State__CompleteDSLPckg_State", None)
        self.__CompleteDSLPckg_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_StateMachine578"):
                opp_val = getattr(old_value, "CompleteDSLPckg_StateMachine578", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_StateMachine578"):
                opp_val = getattr(value, "CompleteDSLPckg_StateMachine578", None)
                if opp_val is None:
                    setattr(value, "CompleteDSLPckg_StateMachine578", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CompleteDSLPckg_State640(self):
        return self.__CompleteDSLPckg_State640

    @CompleteDSLPckg_State640.setter
    def CompleteDSLPckg_State640(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_State__CompleteDSLPckg_State640", None)
        self.__CompleteDSLPckg_State640 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_Pseudostate641"):
                    opp_val = getattr(item, "CompleteDSLPckg_Pseudostate641", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_Pseudostate641", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_Pseudostate641"):
                    opp_val = getattr(item, "CompleteDSLPckg_Pseudostate641", None)
                    
                    setattr(item, "CompleteDSLPckg_Pseudostate641", self)
                    

    @property
    def CompleteDSLPckg_State652(self):
        return self.__CompleteDSLPckg_State652

    @CompleteDSLPckg_State652.setter
    def CompleteDSLPckg_State652(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_State__CompleteDSLPckg_State652", None)
        self.__CompleteDSLPckg_State652 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Behavior653"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Behavior653", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_Behavior653", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Behavior653"):
                opp_val = getattr(value, "CompleteDSLPckg_Behavior653", None)
                setattr(value, "CompleteDSLPckg_Behavior653", self)

    @property
    def CompleteDSLPckg_State646(self):
        return self.__CompleteDSLPckg_State646

    @CompleteDSLPckg_State646.setter
    def CompleteDSLPckg_State646(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_State__CompleteDSLPckg_State646", None)
        self.__CompleteDSLPckg_State646 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_Region647"):
                    opp_val = getattr(item, "CompleteDSLPckg_Region647", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_Region647", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_Region647"):
                    opp_val = getattr(item, "CompleteDSLPckg_Region647", None)
                    
                    setattr(item, "CompleteDSLPckg_Region647", self)
                    

    @property
    def CompleteDSLPckg_State637(self):
        return self.__CompleteDSLPckg_State637

    @CompleteDSLPckg_State637.setter
    def CompleteDSLPckg_State637(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_State__CompleteDSLPckg_State637", None)
        self.__CompleteDSLPckg_State637 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_ConnectionPointReference638"):
                    opp_val = getattr(item, "CompleteDSLPckg_ConnectionPointReference638", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_ConnectionPointReference638", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_ConnectionPointReference638"):
                    opp_val = getattr(item, "CompleteDSLPckg_ConnectionPointReference638", None)
                    
                    setattr(item, "CompleteDSLPckg_ConnectionPointReference638", self)
                    

    @property
    def CompleteDSLPckg_State663(self):
        return self.__CompleteDSLPckg_State663

    @CompleteDSLPckg_State663.setter
    def CompleteDSLPckg_State663(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_State__CompleteDSLPckg_State663", None)
        self.__CompleteDSLPckg_State663 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_State665"):
                opp_val = getattr(old_value, "CompleteDSLPckg_State665", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_State665", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_State665"):
                opp_val = getattr(value, "CompleteDSLPckg_State665", None)
                setattr(value, "CompleteDSLPckg_State665", self)

class CompleteDSLPckg_Package(Namespace, PackageableElement):

    def __init__(self, URI: str, CompleteDSLPckg_Package: "CompleteDSLPckg_PackageImport" = None, Package: "CompleteDSLPckg_Package" = None, nestingPackage: set["CompleteDSLPckg_Package"] = None, CompleteDSLPckg_Package29: set["CompleteDSLPckg_PackageableElement"] = None, package: set["CompleteDSLPckg_Type"] = None, receivingPackage: set["CompleteDSLPckg_PackageMerge"] = None, Package27: "CompleteDSLPckg_Package" = None, nestedPackage: "CompleteDSLPckg_Package" = None, Package56: "CompleteDSLPckg_Type" = None, Package192: "CompleteDSLPckg_PackageMerge" = None, CompleteDSLPckg_Package194: "CompleteDSLPckg_PackageMerge" = None):
        self.URI = URI
        self.CompleteDSLPckg_Package = CompleteDSLPckg_Package
        self.Package = Package
        self.nestingPackage = nestingPackage if nestingPackage is not None else set()
        self.CompleteDSLPckg_Package29 = CompleteDSLPckg_Package29 if CompleteDSLPckg_Package29 is not None else set()
        self.package = package if package is not None else set()
        self.receivingPackage = receivingPackage if receivingPackage is not None else set()
        self.Package27 = Package27
        self.nestedPackage = nestedPackage
        self.Package56 = Package56
        self.Package192 = Package192
        self.CompleteDSLPckg_Package194 = CompleteDSLPckg_Package194
        
        pass
    @property
    def URI(self):
        return self.__URI

    @URI.setter
    def URI(self, URI: str):
        self.__URI = URI


    @property
    def CompleteDSLPckg_Package(self):
        return self.__CompleteDSLPckg_Package

    @CompleteDSLPckg_Package.setter
    def CompleteDSLPckg_Package(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Package__CompleteDSLPckg_Package", None)
        self.__CompleteDSLPckg_Package = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_PackageImport"):
                opp_val = getattr(old_value, "CompleteDSLPckg_PackageImport", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_PackageImport", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_PackageImport"):
                opp_val = getattr(value, "CompleteDSLPckg_PackageImport", None)
                setattr(value, "CompleteDSLPckg_PackageImport", self)

    @property
    def Package56(self):
        return self.__Package56

    @Package56.setter
    def Package56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Package__Package56", None)
        self.__Package56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownedType"):
                opp_val = getattr(old_value, "ownedType", None)
                if opp_val == self:
                    setattr(old_value, "ownedType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedType"):
                opp_val = getattr(value, "ownedType", None)
                setattr(value, "ownedType", self)

    @property
    def nestedPackage(self):
        return self.__nestedPackage

    @nestedPackage.setter
    def nestedPackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Package__nestedPackage", None)
        self.__nestedPackage = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Package27"):
                opp_val = getattr(old_value, "Package27", None)
                if opp_val == self:
                    setattr(old_value, "Package27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Package27"):
                opp_val = getattr(value, "Package27", None)
                setattr(value, "Package27", self)

    @property
    def package(self):
        return self.__package

    @package.setter
    def package(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Package__package", None)
        self.__package = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Type"):
                    opp_val = getattr(item, "Type", None)
                    
                    if opp_val == self:
                        setattr(item, "Type", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Type"):
                    opp_val = getattr(item, "Type", None)
                    
                    setattr(item, "Type", self)
                    

    @property
    def Package(self):
        return self.__Package

    @Package.setter
    def Package(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Package__Package", None)
        self.__Package = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nestingPackage"):
                opp_val = getattr(old_value, "nestingPackage", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nestingPackage"):
                opp_val = getattr(value, "nestingPackage", None)
                if opp_val is None:
                    setattr(value, "nestingPackage", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def nestingPackage(self):
        return self.__nestingPackage

    @nestingPackage.setter
    def nestingPackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Package__nestingPackage", None)
        self.__nestingPackage = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Package"):
                    opp_val = getattr(item, "Package", None)
                    
                    if opp_val == self:
                        setattr(item, "Package", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Package"):
                    opp_val = getattr(item, "Package", None)
                    
                    setattr(item, "Package", self)
                    

    @property
    def CompleteDSLPckg_Package29(self):
        return self.__CompleteDSLPckg_Package29

    @CompleteDSLPckg_Package29.setter
    def CompleteDSLPckg_Package29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Package__CompleteDSLPckg_Package29", None)
        self.__CompleteDSLPckg_Package29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_PackageableElement30"):
                    opp_val = getattr(item, "CompleteDSLPckg_PackageableElement30", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_PackageableElement30", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_PackageableElement30"):
                    opp_val = getattr(item, "CompleteDSLPckg_PackageableElement30", None)
                    
                    setattr(item, "CompleteDSLPckg_PackageableElement30", self)
                    

    @property
    def Package192(self):
        return self.__Package192

    @Package192.setter
    def Package192(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Package__Package192", None)
        self.__Package192 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "packageMerge"):
                opp_val = getattr(old_value, "packageMerge", None)
                if opp_val == self:
                    setattr(old_value, "packageMerge", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "packageMerge"):
                opp_val = getattr(value, "packageMerge", None)
                setattr(value, "packageMerge", self)

    @property
    def Package27(self):
        return self.__Package27

    @Package27.setter
    def Package27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Package__Package27", None)
        self.__Package27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nestedPackage"):
                opp_val = getattr(old_value, "nestedPackage", None)
                if opp_val == self:
                    setattr(old_value, "nestedPackage", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nestedPackage"):
                opp_val = getattr(value, "nestedPackage", None)
                setattr(value, "nestedPackage", self)

    @property
    def receivingPackage(self):
        return self.__receivingPackage

    @receivingPackage.setter
    def receivingPackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Package__receivingPackage", None)
        self.__receivingPackage = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PackageMerge"):
                    opp_val = getattr(item, "PackageMerge", None)
                    
                    if opp_val == self:
                        setattr(item, "PackageMerge", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PackageMerge"):
                    opp_val = getattr(item, "PackageMerge", None)
                    
                    setattr(item, "PackageMerge", self)
                    

    @property
    def CompleteDSLPckg_Package194(self):
        return self.__CompleteDSLPckg_Package194

    @CompleteDSLPckg_Package194.setter
    def CompleteDSLPckg_Package194(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Package__CompleteDSLPckg_Package194", None)
        self.__CompleteDSLPckg_Package194 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_PackageMerge"):
                opp_val = getattr(old_value, "CompleteDSLPckg_PackageMerge", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_PackageMerge", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_PackageMerge"):
                opp_val = getattr(value, "CompleteDSLPckg_PackageMerge", None)
                setattr(value, "CompleteDSLPckg_PackageMerge", self)

class DirectedRelationship:

    pass
class CompleteDSLPckg_PackageMerge(DirectedRelationship):

    pass
class CompleteDSLPckg_Generalization(DirectedRelationship):

    def __init__(self, isSubstitutable: bool, Generalization: "CompleteDSLPckg_Classifier" = None, CompleteDSLPckg_Generalization: "CompleteDSLPckg_Classifier" = None, generalization: "CompleteDSLPckg_Classifier" = None, generalization135: set["CompleteDSLPckg_GeneralizationSet"] = None, Generalization230: "CompleteDSLPckg_GeneralizationSet" = None):
        self.isSubstitutable = isSubstitutable
        self.Generalization = Generalization
        self.CompleteDSLPckg_Generalization = CompleteDSLPckg_Generalization
        self.generalization = generalization
        self.generalization135 = generalization135 if generalization135 is not None else set()
        self.Generalization230 = Generalization230
        
        pass
    @property
    def isSubstitutable(self):
        return self.__isSubstitutable

    @isSubstitutable.setter
    def isSubstitutable(self, isSubstitutable: bool):
        self.__isSubstitutable = isSubstitutable


    @property
    def CompleteDSLPckg_Generalization(self):
        return self.__CompleteDSLPckg_Generalization

    @CompleteDSLPckg_Generalization.setter
    def CompleteDSLPckg_Generalization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Generalization__CompleteDSLPckg_Generalization", None)
        self.__CompleteDSLPckg_Generalization = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Classifier131"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Classifier131", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_Classifier131", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Classifier131"):
                opp_val = getattr(value, "CompleteDSLPckg_Classifier131", None)
                setattr(value, "CompleteDSLPckg_Classifier131", self)

    @property
    def generalization(self):
        return self.__generalization

    @generalization.setter
    def generalization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Generalization__generalization", None)
        self.__generalization = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Classifier133"):
                opp_val = getattr(old_value, "Classifier133", None)
                if opp_val == self:
                    setattr(old_value, "Classifier133", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Classifier133"):
                opp_val = getattr(value, "Classifier133", None)
                setattr(value, "Classifier133", self)

    @property
    def Generalization230(self):
        return self.__Generalization230

    @Generalization230.setter
    def Generalization230(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Generalization__Generalization230", None)
        self.__Generalization230 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "generalizationSet"):
                opp_val = getattr(old_value, "generalizationSet", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "generalizationSet"):
                opp_val = getattr(value, "generalizationSet", None)
                if opp_val is None:
                    setattr(value, "generalizationSet", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def generalization135(self):
        return self.__generalization135

    @generalization135.setter
    def generalization135(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Generalization__generalization135", None)
        self.__generalization135 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GeneralizationSet136"):
                    opp_val = getattr(item, "GeneralizationSet136", None)
                    
                    if opp_val == self:
                        setattr(item, "GeneralizationSet136", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GeneralizationSet136"):
                    opp_val = getattr(item, "GeneralizationSet136", None)
                    
                    setattr(item, "GeneralizationSet136", self)
                    

    @property
    def Generalization(self):
        return self.__Generalization

    @Generalization.setter
    def Generalization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Generalization__Generalization", None)
        self.__Generalization = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "specific"):
                opp_val = getattr(old_value, "specific", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "specific"):
                opp_val = getattr(value, "specific", None)
                if opp_val is None:
                    setattr(value, "specific", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class CompleteDSLPckg_ProtocolConformance(DirectedRelationship):

    pass
class CompleteDSLPckg_Constraint(PackageableElement):

    pass
class CompleteDSLPckg_PackageImport(DirectedRelationship):

    def __init__(self, visibility: str, CompleteDSLPckg_PackageImport: "CompleteDSLPckg_Package" = None, packageImport: "CompleteDSLPckg_Namespace" = None, PackageImport: "CompleteDSLPckg_Namespace" = None):
        self.visibility = visibility
        self.CompleteDSLPckg_PackageImport = CompleteDSLPckg_PackageImport
        self.packageImport = packageImport
        self.PackageImport = PackageImport
        
        pass
    @property
    def visibility(self):
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility


    @property
    def CompleteDSLPckg_PackageImport(self):
        return self.__CompleteDSLPckg_PackageImport

    @CompleteDSLPckg_PackageImport.setter
    def CompleteDSLPckg_PackageImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_PackageImport__CompleteDSLPckg_PackageImport", None)
        self.__CompleteDSLPckg_PackageImport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Package"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Package", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_Package", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Package"):
                opp_val = getattr(value, "CompleteDSLPckg_Package", None)
                setattr(value, "CompleteDSLPckg_Package", self)

    @property
    def PackageImport(self):
        return self.__PackageImport

    @PackageImport.setter
    def PackageImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_PackageImport__PackageImport", None)
        self.__PackageImport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "importingNamespace14"):
                opp_val = getattr(old_value, "importingNamespace14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "importingNamespace14"):
                opp_val = getattr(value, "importingNamespace14", None)
                if opp_val is None:
                    setattr(value, "importingNamespace14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def packageImport(self):
        return self.__packageImport

    @packageImport.setter
    def packageImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_PackageImport__packageImport", None)
        self.__packageImport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Namespace22"):
                opp_val = getattr(old_value, "Namespace22", None)
                if opp_val == self:
                    setattr(old_value, "Namespace22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Namespace22"):
                opp_val = getattr(value, "Namespace22", None)
                setattr(value, "Namespace22", self)

class CompleteDSLPckg_ElementImport(DirectedRelationship):

    def __init__(self, visibility: str, alias: str, CompleteDSLPckg_ElementImport: "CompleteDSLPckg_PackageableElement" = None, elementImport: "CompleteDSLPckg_Namespace" = None, ElementImport: "CompleteDSLPckg_Namespace" = None):
        self.visibility = visibility
        self.alias = alias
        self.CompleteDSLPckg_ElementImport = CompleteDSLPckg_ElementImport
        self.elementImport = elementImport
        self.ElementImport = ElementImport
        
        pass
    @property
    def alias(self):
        return self.__alias

    @alias.setter
    def alias(self, alias: str):
        self.__alias = alias


    @property
    def visibility(self):
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility


    @property
    def CompleteDSLPckg_ElementImport(self):
        return self.__CompleteDSLPckg_ElementImport

    @CompleteDSLPckg_ElementImport.setter
    def CompleteDSLPckg_ElementImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_ElementImport__CompleteDSLPckg_ElementImport", None)
        self.__CompleteDSLPckg_ElementImport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_PackageableElement17"):
                opp_val = getattr(old_value, "CompleteDSLPckg_PackageableElement17", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_PackageableElement17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_PackageableElement17"):
                opp_val = getattr(value, "CompleteDSLPckg_PackageableElement17", None)
                setattr(value, "CompleteDSLPckg_PackageableElement17", self)

    @property
    def ElementImport(self):
        return self.__ElementImport

    @ElementImport.setter
    def ElementImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_ElementImport__ElementImport", None)
        self.__ElementImport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "importingNamespace"):
                opp_val = getattr(old_value, "importingNamespace", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "importingNamespace"):
                opp_val = getattr(value, "importingNamespace", None)
                if opp_val is None:
                    setattr(value, "importingNamespace", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def elementImport(self):
        return self.__elementImport

    @elementImport.setter
    def elementImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_ElementImport__elementImport", None)
        self.__elementImport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Namespace19"):
                opp_val = getattr(old_value, "Namespace19", None)
                if opp_val == self:
                    setattr(old_value, "Namespace19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Namespace19"):
                opp_val = getattr(value, "Namespace19", None)
                setattr(value, "Namespace19", self)

class CompleteDSLPckg_Dependency(DirectedRelationship, PackageableElement):

    pass
class Element:

    pass
class CompleteDSLPckg_MultiplicityElement(Element):

    def __init__(self, isOrdered: bool, isUnique: bool, upper: int, lower: int, MultiplicityElement: "CompleteDSLPckg_ValueSpecification" = None, MultiplicityElement48: "CompleteDSLPckg_ValueSpecification" = None, owningUpper: "CompleteDSLPckg_ValueSpecification" = None, owningLower: "CompleteDSLPckg_ValueSpecification" = None):
        self.isOrdered = isOrdered
        self.isUnique = isUnique
        self.upper = upper
        self.lower = lower
        self.MultiplicityElement = MultiplicityElement
        self.MultiplicityElement48 = MultiplicityElement48
        self.owningUpper = owningUpper
        self.owningLower = owningLower
        
        pass
    @property
    def isUnique(self):
        return self.__isUnique

    @isUnique.setter
    def isUnique(self, isUnique: bool):
        self.__isUnique = isUnique


    @property
    def upper(self):
        return self.__upper

    @upper.setter
    def upper(self, upper: int):
        self.__upper = upper


    @property
    def lower(self):
        return self.__lower

    @lower.setter
    def lower(self, lower: int):
        self.__lower = lower


    @property
    def isOrdered(self):
        return self.__isOrdered

    @isOrdered.setter
    def isOrdered(self, isOrdered: bool):
        self.__isOrdered = isOrdered


    @property
    def owningLower(self):
        return self.__owningLower

    @owningLower.setter
    def owningLower(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_MultiplicityElement__owningLower", None)
        self.__owningLower = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ValueSpecification45"):
                opp_val = getattr(old_value, "ValueSpecification45", None)
                if opp_val == self:
                    setattr(old_value, "ValueSpecification45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ValueSpecification45"):
                opp_val = getattr(value, "ValueSpecification45", None)
                setattr(value, "ValueSpecification45", self)

    @property
    def MultiplicityElement48(self):
        return self.__MultiplicityElement48

    @MultiplicityElement48.setter
    def MultiplicityElement48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_MultiplicityElement__MultiplicityElement48", None)
        self.__MultiplicityElement48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lowerValue"):
                opp_val = getattr(old_value, "lowerValue", None)
                if opp_val == self:
                    setattr(old_value, "lowerValue", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lowerValue"):
                opp_val = getattr(value, "lowerValue", None)
                setattr(value, "lowerValue", self)

    @property
    def MultiplicityElement(self):
        return self.__MultiplicityElement

    @MultiplicityElement.setter
    def MultiplicityElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_MultiplicityElement__MultiplicityElement", None)
        self.__MultiplicityElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "upperValue"):
                opp_val = getattr(old_value, "upperValue", None)
                if opp_val == self:
                    setattr(old_value, "upperValue", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "upperValue"):
                opp_val = getattr(value, "upperValue", None)
                setattr(value, "upperValue", self)

    @property
    def owningUpper(self):
        return self.__owningUpper

    @owningUpper.setter
    def owningUpper(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_MultiplicityElement__owningUpper", None)
        self.__owningUpper = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ValueSpecification"):
                opp_val = getattr(old_value, "ValueSpecification", None)
                if opp_val == self:
                    setattr(old_value, "ValueSpecification", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ValueSpecification"):
                opp_val = getattr(value, "ValueSpecification", None)
                setattr(value, "ValueSpecification", self)

class CompleteDSLPckg_QualifierValue(Element):

    pass
class CompleteDSLPckg_Relationship(Element):

    pass
class CompleteDSLPckg_ExceptionHandler(Element):

    pass
class CompleteDSLPckg_Slot(Element):

    pass
class CompleteDSLPckg_LinkEndData(Element):

    pass
class CompleteDSLPckg_Clause(Element):

    pass
class CompleteDSLPckg_NamedElement(Element):

    def __init__(self, name: str, qualifiedName: str, visibility: str, ownedMember: "CompleteDSLPckg_Namespace" = None, client: set["CompleteDSLPckg_Dependency"] = None, CompleteDSLPckg_NamedElement: "CompleteDSLPckg_Namespace" = None, NamedElement: "CompleteDSLPckg_Namespace" = None, CompleteDSLPckg_NamedElement86: "CompleteDSLPckg_Classifier" = None, NamedElement196: "CompleteDSLPckg_Dependency" = None, CompleteDSLPckg_NamedElement198: "CompleteDSLPckg_Dependency" = None, CompleteDSLPckg_NamedElement268: "CompleteDSLPckg_TimeObservation" = None, CompleteDSLPckg_NamedElement270: "CompleteDSLPckg_DurationObservation" = None, CompleteDSLPckg_NamedElement930: "CompleteDSLPckg_Message" = None, CompleteDSLPckg_NamedElement962: "CompleteDSLPckg_ConsiderIgnoreFragment" = None):
        self.name = name
        self.qualifiedName = qualifiedName
        self.visibility = visibility
        self.ownedMember = ownedMember
        self.client = client if client is not None else set()
        self.CompleteDSLPckg_NamedElement = CompleteDSLPckg_NamedElement
        self.NamedElement = NamedElement
        self.CompleteDSLPckg_NamedElement86 = CompleteDSLPckg_NamedElement86
        self.NamedElement196 = NamedElement196
        self.CompleteDSLPckg_NamedElement198 = CompleteDSLPckg_NamedElement198
        self.CompleteDSLPckg_NamedElement268 = CompleteDSLPckg_NamedElement268
        self.CompleteDSLPckg_NamedElement270 = CompleteDSLPckg_NamedElement270
        self.CompleteDSLPckg_NamedElement930 = CompleteDSLPckg_NamedElement930
        self.CompleteDSLPckg_NamedElement962 = CompleteDSLPckg_NamedElement962
        
        pass
    @property
    def qualifiedName(self):
        return self.__qualifiedName

    @qualifiedName.setter
    def qualifiedName(self, qualifiedName: str):
        self.__qualifiedName = qualifiedName


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def visibility(self):
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility


    @property
    def CompleteDSLPckg_NamedElement198(self):
        return self.__CompleteDSLPckg_NamedElement198

    @CompleteDSLPckg_NamedElement198.setter
    def CompleteDSLPckg_NamedElement198(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_NamedElement__CompleteDSLPckg_NamedElement198", None)
        self.__CompleteDSLPckg_NamedElement198 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Dependency"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Dependency", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Dependency"):
                opp_val = getattr(value, "CompleteDSLPckg_Dependency", None)
                if opp_val is None:
                    setattr(value, "CompleteDSLPckg_Dependency", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CompleteDSLPckg_NamedElement268(self):
        return self.__CompleteDSLPckg_NamedElement268

    @CompleteDSLPckg_NamedElement268.setter
    def CompleteDSLPckg_NamedElement268(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_NamedElement__CompleteDSLPckg_NamedElement268", None)
        self.__CompleteDSLPckg_NamedElement268 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_TimeObservation"):
                opp_val = getattr(old_value, "CompleteDSLPckg_TimeObservation", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_TimeObservation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_TimeObservation"):
                opp_val = getattr(value, "CompleteDSLPckg_TimeObservation", None)
                setattr(value, "CompleteDSLPckg_TimeObservation", self)

    @property
    def CompleteDSLPckg_NamedElement930(self):
        return self.__CompleteDSLPckg_NamedElement930

    @CompleteDSLPckg_NamedElement930.setter
    def CompleteDSLPckg_NamedElement930(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_NamedElement__CompleteDSLPckg_NamedElement930", None)
        self.__CompleteDSLPckg_NamedElement930 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Message929"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Message929", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_Message929", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Message929"):
                opp_val = getattr(value, "CompleteDSLPckg_Message929", None)
                setattr(value, "CompleteDSLPckg_Message929", self)

    @property
    def ownedMember(self):
        return self.__ownedMember

    @ownedMember.setter
    def ownedMember(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_NamedElement__ownedMember", None)
        self.__ownedMember = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Namespace"):
                opp_val = getattr(old_value, "Namespace", None)
                if opp_val == self:
                    setattr(old_value, "Namespace", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Namespace"):
                opp_val = getattr(value, "Namespace", None)
                setattr(value, "Namespace", self)

    @property
    def NamedElement196(self):
        return self.__NamedElement196

    @NamedElement196.setter
    def NamedElement196(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_NamedElement__NamedElement196", None)
        self.__NamedElement196 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "clientDependency"):
                opp_val = getattr(old_value, "clientDependency", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "clientDependency"):
                opp_val = getattr(value, "clientDependency", None)
                if opp_val is None:
                    setattr(value, "clientDependency", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CompleteDSLPckg_NamedElement270(self):
        return self.__CompleteDSLPckg_NamedElement270

    @CompleteDSLPckg_NamedElement270.setter
    def CompleteDSLPckg_NamedElement270(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_NamedElement__CompleteDSLPckg_NamedElement270", None)
        self.__CompleteDSLPckg_NamedElement270 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_DurationObservation"):
                opp_val = getattr(old_value, "CompleteDSLPckg_DurationObservation", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_DurationObservation"):
                opp_val = getattr(value, "CompleteDSLPckg_DurationObservation", None)
                if opp_val is None:
                    setattr(value, "CompleteDSLPckg_DurationObservation", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def client(self):
        return self.__client

    @client.setter
    def client(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_NamedElement__client", None)
        self.__client = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Dependency"):
                    opp_val = getattr(item, "Dependency", None)
                    
                    if opp_val == self:
                        setattr(item, "Dependency", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Dependency"):
                    opp_val = getattr(item, "Dependency", None)
                    
                    setattr(item, "Dependency", self)
                    

    @property
    def CompleteDSLPckg_NamedElement(self):
        return self.__CompleteDSLPckg_NamedElement

    @CompleteDSLPckg_NamedElement.setter
    def CompleteDSLPckg_NamedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_NamedElement__CompleteDSLPckg_NamedElement", None)
        self.__CompleteDSLPckg_NamedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Namespace10"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Namespace10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Namespace10"):
                opp_val = getattr(value, "CompleteDSLPckg_Namespace10", None)
                if opp_val is None:
                    setattr(value, "CompleteDSLPckg_Namespace10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CompleteDSLPckg_NamedElement962(self):
        return self.__CompleteDSLPckg_NamedElement962

    @CompleteDSLPckg_NamedElement962.setter
    def CompleteDSLPckg_NamedElement962(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_NamedElement__CompleteDSLPckg_NamedElement962", None)
        self.__CompleteDSLPckg_NamedElement962 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_ConsiderIgnoreFragment"):
                opp_val = getattr(old_value, "CompleteDSLPckg_ConsiderIgnoreFragment", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_ConsiderIgnoreFragment"):
                opp_val = getattr(value, "CompleteDSLPckg_ConsiderIgnoreFragment", None)
                if opp_val is None:
                    setattr(value, "CompleteDSLPckg_ConsiderIgnoreFragment", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CompleteDSLPckg_NamedElement86(self):
        return self.__CompleteDSLPckg_NamedElement86

    @CompleteDSLPckg_NamedElement86.setter
    def CompleteDSLPckg_NamedElement86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_NamedElement__CompleteDSLPckg_NamedElement86", None)
        self.__CompleteDSLPckg_NamedElement86 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Classifier85"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Classifier85", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Classifier85"):
                opp_val = getattr(value, "CompleteDSLPckg_Classifier85", None)
                if opp_val is None:
                    setattr(value, "CompleteDSLPckg_Classifier85", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def NamedElement(self):
        return self.__NamedElement

    @NamedElement.setter
    def NamedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_NamedElement__NamedElement", None)
        self.__NamedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "namespace"):
                opp_val = getattr(old_value, "namespace", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "namespace"):
                opp_val = getattr(value, "namespace", None)
                if opp_val is None:
                    setattr(value, "namespace", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class CompleteDSLPckg_Comment(Element):

    def __init__(self, body: str, ownedComment: "CompleteDSLPckg_Element" = None, CompleteDSLPckg_Comment: set["CompleteDSLPckg_Element"] = None, Comment: "CompleteDSLPckg_Element" = None):
        self.body = body
        self.ownedComment = ownedComment
        self.CompleteDSLPckg_Comment = CompleteDSLPckg_Comment if CompleteDSLPckg_Comment is not None else set()
        self.Comment = Comment
        
        pass
    @property
    def body(self):
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body


    @property
    def ownedComment(self):
        return self.__ownedComment

    @ownedComment.setter
    def ownedComment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Comment__ownedComment", None)
        self.__ownedComment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Element34"):
                opp_val = getattr(old_value, "Element34", None)
                if opp_val == self:
                    setattr(old_value, "Element34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Element34"):
                opp_val = getattr(value, "Element34", None)
                setattr(value, "Element34", self)

    @property
    def Comment(self):
        return self.__Comment

    @Comment.setter
    def Comment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Comment__Comment", None)
        self.__Comment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owningElement"):
                opp_val = getattr(old_value, "owningElement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owningElement"):
                opp_val = getattr(value, "owningElement", None)
                if opp_val is None:
                    setattr(value, "owningElement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CompleteDSLPckg_Comment(self):
        return self.__CompleteDSLPckg_Comment

    @CompleteDSLPckg_Comment.setter
    def CompleteDSLPckg_Comment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Comment__CompleteDSLPckg_Comment", None)
        self.__CompleteDSLPckg_Comment = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_Element"):
                    opp_val = getattr(item, "CompleteDSLPckg_Element", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_Element", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_Element"):
                    opp_val = getattr(item, "CompleteDSLPckg_Element", None)
                    
                    setattr(item, "CompleteDSLPckg_Element", self)
                    

class CompleteDSLPckg_Element(ABC):

    pass
class NamedElement:

    pass
class CompleteDSLPckg_Extend(DirectedRelationship, NamedElement):

    pass
class CompleteDSLPckg_Namespace(NamedElement):

    pass
class CompleteDSLPckg_Action(NamedElement):

    pass
class CompleteDSLPckg_DeployedArtifact(NamedElement):

    pass
class CompleteDSLPckg_ParameterSet(NamedElement):

    pass
class CompleteDSLPckg_PackageableElement(NamedElement):

    pass
class CompleteDSLPckg_Artifact(NamedElement, Classifier, DeployedArtifact):

    def __init__(self, fileName: str, CompleteDSLPckg_Artifact372: set["CompleteDSLPckg_Manifestation"] = None, CompleteDSLPckg_Artifact: set["CompleteDSLPckg_Operation"] = None, CompleteDSLPckg_Artifact366: set["CompleteDSLPckg_Property"] = None, CompleteDSLPckg_Artifact370: "CompleteDSLPckg_Artifact" = None, CompleteDSLPckg_Artifact368: set["CompleteDSLPckg_Artifact"] = None):
        self.fileName = fileName
        self.CompleteDSLPckg_Artifact372 = CompleteDSLPckg_Artifact372 if CompleteDSLPckg_Artifact372 is not None else set()
        self.CompleteDSLPckg_Artifact = CompleteDSLPckg_Artifact if CompleteDSLPckg_Artifact is not None else set()
        self.CompleteDSLPckg_Artifact366 = CompleteDSLPckg_Artifact366 if CompleteDSLPckg_Artifact366 is not None else set()
        self.CompleteDSLPckg_Artifact370 = CompleteDSLPckg_Artifact370
        self.CompleteDSLPckg_Artifact368 = CompleteDSLPckg_Artifact368 if CompleteDSLPckg_Artifact368 is not None else set()
        
        pass
    @property
    def fileName(self):
        return self.__fileName

    @fileName.setter
    def fileName(self, fileName: str):
        self.__fileName = fileName


    @property
    def CompleteDSLPckg_Artifact366(self):
        return self.__CompleteDSLPckg_Artifact366

    @CompleteDSLPckg_Artifact366.setter
    def CompleteDSLPckg_Artifact366(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Artifact__CompleteDSLPckg_Artifact366", None)
        self.__CompleteDSLPckg_Artifact366 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_Property367"):
                    opp_val = getattr(item, "CompleteDSLPckg_Property367", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_Property367", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_Property367"):
                    opp_val = getattr(item, "CompleteDSLPckg_Property367", None)
                    
                    setattr(item, "CompleteDSLPckg_Property367", self)
                    

    @property
    def CompleteDSLPckg_Artifact368(self):
        return self.__CompleteDSLPckg_Artifact368

    @CompleteDSLPckg_Artifact368.setter
    def CompleteDSLPckg_Artifact368(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Artifact__CompleteDSLPckg_Artifact368", None)
        self.__CompleteDSLPckg_Artifact368 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_Artifact370"):
                    opp_val = getattr(item, "CompleteDSLPckg_Artifact370", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_Artifact370", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_Artifact370"):
                    opp_val = getattr(item, "CompleteDSLPckg_Artifact370", None)
                    
                    setattr(item, "CompleteDSLPckg_Artifact370", self)
                    

    @property
    def CompleteDSLPckg_Artifact370(self):
        return self.__CompleteDSLPckg_Artifact370

    @CompleteDSLPckg_Artifact370.setter
    def CompleteDSLPckg_Artifact370(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Artifact__CompleteDSLPckg_Artifact370", None)
        self.__CompleteDSLPckg_Artifact370 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Artifact368"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Artifact368", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Artifact368"):
                opp_val = getattr(value, "CompleteDSLPckg_Artifact368", None)
                if opp_val is None:
                    setattr(value, "CompleteDSLPckg_Artifact368", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CompleteDSLPckg_Artifact372(self):
        return self.__CompleteDSLPckg_Artifact372

    @CompleteDSLPckg_Artifact372.setter
    def CompleteDSLPckg_Artifact372(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Artifact__CompleteDSLPckg_Artifact372", None)
        self.__CompleteDSLPckg_Artifact372 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_Manifestation"):
                    opp_val = getattr(item, "CompleteDSLPckg_Manifestation", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_Manifestation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_Manifestation"):
                    opp_val = getattr(item, "CompleteDSLPckg_Manifestation", None)
                    
                    setattr(item, "CompleteDSLPckg_Manifestation", self)
                    

    @property
    def CompleteDSLPckg_Artifact(self):
        return self.__CompleteDSLPckg_Artifact

    @CompleteDSLPckg_Artifact.setter
    def CompleteDSLPckg_Artifact(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Artifact__CompleteDSLPckg_Artifact", None)
        self.__CompleteDSLPckg_Artifact = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_Operation364"):
                    opp_val = getattr(item, "CompleteDSLPckg_Operation364", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_Operation364", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_Operation364"):
                    opp_val = getattr(item, "CompleteDSLPckg_Operation364", None)
                    
                    setattr(item, "CompleteDSLPckg_Operation364", self)
                    

class CompleteDSLPckg_Message(NamedElement):

    def __init__(self, messageKind: str, messageSort: str, CompleteDSLPckg_Message938: "CompleteDSLPckg_MessageEnd" = None, CompleteDSLPckg_Message: set["CompleteDSLPckg_ValueSpecification"] = None, CompleteDSLPckg_Message926: "CompleteDSLPckg_Connector" = None, CompleteDSLPckg_Message929: "CompleteDSLPckg_NamedElement" = None, CompleteDSLPckg_Message932: "CompleteDSLPckg_MessageEnd" = None, CompleteDSLPckg_Message934: "CompleteDSLPckg_MessageEnd" = None):
        self.messageKind = messageKind
        self.messageSort = messageSort
        self.CompleteDSLPckg_Message938 = CompleteDSLPckg_Message938
        self.CompleteDSLPckg_Message = CompleteDSLPckg_Message if CompleteDSLPckg_Message is not None else set()
        self.CompleteDSLPckg_Message926 = CompleteDSLPckg_Message926
        self.CompleteDSLPckg_Message929 = CompleteDSLPckg_Message929
        self.CompleteDSLPckg_Message932 = CompleteDSLPckg_Message932
        self.CompleteDSLPckg_Message934 = CompleteDSLPckg_Message934
        
        pass
    @property
    def messageKind(self):
        return self.__messageKind

    @messageKind.setter
    def messageKind(self, messageKind: str):
        self.__messageKind = messageKind


    @property
    def messageSort(self):
        return self.__messageSort

    @messageSort.setter
    def messageSort(self, messageSort: str):
        self.__messageSort = messageSort


    @property
    def CompleteDSLPckg_Message938(self):
        return self.__CompleteDSLPckg_Message938

    @CompleteDSLPckg_Message938.setter
    def CompleteDSLPckg_Message938(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Message__CompleteDSLPckg_Message938", None)
        self.__CompleteDSLPckg_Message938 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_MessageEnd937"):
                opp_val = getattr(old_value, "CompleteDSLPckg_MessageEnd937", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_MessageEnd937", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_MessageEnd937"):
                opp_val = getattr(value, "CompleteDSLPckg_MessageEnd937", None)
                setattr(value, "CompleteDSLPckg_MessageEnd937", self)

    @property
    def CompleteDSLPckg_Message926(self):
        return self.__CompleteDSLPckg_Message926

    @CompleteDSLPckg_Message926.setter
    def CompleteDSLPckg_Message926(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Message__CompleteDSLPckg_Message926", None)
        self.__CompleteDSLPckg_Message926 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Connector927"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Connector927", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_Connector927", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Connector927"):
                opp_val = getattr(value, "CompleteDSLPckg_Connector927", None)
                setattr(value, "CompleteDSLPckg_Connector927", self)

    @property
    def CompleteDSLPckg_Message932(self):
        return self.__CompleteDSLPckg_Message932

    @CompleteDSLPckg_Message932.setter
    def CompleteDSLPckg_Message932(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Message__CompleteDSLPckg_Message932", None)
        self.__CompleteDSLPckg_Message932 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_MessageEnd"):
                opp_val = getattr(old_value, "CompleteDSLPckg_MessageEnd", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_MessageEnd", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_MessageEnd"):
                opp_val = getattr(value, "CompleteDSLPckg_MessageEnd", None)
                setattr(value, "CompleteDSLPckg_MessageEnd", self)

    @property
    def CompleteDSLPckg_Message(self):
        return self.__CompleteDSLPckg_Message

    @CompleteDSLPckg_Message.setter
    def CompleteDSLPckg_Message(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Message__CompleteDSLPckg_Message", None)
        self.__CompleteDSLPckg_Message = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_ValueSpecification924"):
                    opp_val = getattr(item, "CompleteDSLPckg_ValueSpecification924", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_ValueSpecification924", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_ValueSpecification924"):
                    opp_val = getattr(item, "CompleteDSLPckg_ValueSpecification924", None)
                    
                    setattr(item, "CompleteDSLPckg_ValueSpecification924", self)
                    

    @property
    def CompleteDSLPckg_Message934(self):
        return self.__CompleteDSLPckg_Message934

    @CompleteDSLPckg_Message934.setter
    def CompleteDSLPckg_Message934(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Message__CompleteDSLPckg_Message934", None)
        self.__CompleteDSLPckg_Message934 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_MessageEnd935"):
                opp_val = getattr(old_value, "CompleteDSLPckg_MessageEnd935", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_MessageEnd935", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_MessageEnd935"):
                opp_val = getattr(value, "CompleteDSLPckg_MessageEnd935", None)
                setattr(value, "CompleteDSLPckg_MessageEnd935", self)

    @property
    def CompleteDSLPckg_Message929(self):
        return self.__CompleteDSLPckg_Message929

    @CompleteDSLPckg_Message929.setter
    def CompleteDSLPckg_Message929(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Message__CompleteDSLPckg_Message929", None)
        self.__CompleteDSLPckg_Message929 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_NamedElement930"):
                opp_val = getattr(old_value, "CompleteDSLPckg_NamedElement930", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_NamedElement930", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_NamedElement930"):
                opp_val = getattr(value, "CompleteDSLPckg_NamedElement930", None)
                setattr(value, "CompleteDSLPckg_NamedElement930", self)

class CompleteDSLPckg_CollaborationUse(NamedElement):

    pass
class CompleteDSLPckg_Component(NamedElement, Class):

    def __init__(self, isIndirectlyInstantiated: bool, CompleteDSLPckg_Component: set["CompleteDSLPckg_Interface"] = None, CompleteDSLPckg_Component298: set["CompleteDSLPckg_Interface"] = None, CompleteDSLPckg_Component301: set["CompleteDSLPckg_ComponentRealization"] = None, CompleteDSLPckg_Component303: set["CompleteDSLPckg_PackageableElement"] = None, CompleteDSLPckg_Component307: "CompleteDSLPckg_ComponentRealization" = None):
        self.isIndirectlyInstantiated = isIndirectlyInstantiated
        self.CompleteDSLPckg_Component = CompleteDSLPckg_Component if CompleteDSLPckg_Component is not None else set()
        self.CompleteDSLPckg_Component298 = CompleteDSLPckg_Component298 if CompleteDSLPckg_Component298 is not None else set()
        self.CompleteDSLPckg_Component301 = CompleteDSLPckg_Component301 if CompleteDSLPckg_Component301 is not None else set()
        self.CompleteDSLPckg_Component303 = CompleteDSLPckg_Component303 if CompleteDSLPckg_Component303 is not None else set()
        self.CompleteDSLPckg_Component307 = CompleteDSLPckg_Component307
        
        pass
    @property
    def isIndirectlyInstantiated(self):
        return self.__isIndirectlyInstantiated

    @isIndirectlyInstantiated.setter
    def isIndirectlyInstantiated(self, isIndirectlyInstantiated: bool):
        self.__isIndirectlyInstantiated = isIndirectlyInstantiated


    @property
    def CompleteDSLPckg_Component307(self):
        return self.__CompleteDSLPckg_Component307

    @CompleteDSLPckg_Component307.setter
    def CompleteDSLPckg_Component307(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Component__CompleteDSLPckg_Component307", None)
        self.__CompleteDSLPckg_Component307 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_ComponentRealization306"):
                opp_val = getattr(old_value, "CompleteDSLPckg_ComponentRealization306", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_ComponentRealization306", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_ComponentRealization306"):
                opp_val = getattr(value, "CompleteDSLPckg_ComponentRealization306", None)
                setattr(value, "CompleteDSLPckg_ComponentRealization306", self)

    @property
    def CompleteDSLPckg_Component(self):
        return self.__CompleteDSLPckg_Component

    @CompleteDSLPckg_Component.setter
    def CompleteDSLPckg_Component(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Component__CompleteDSLPckg_Component", None)
        self.__CompleteDSLPckg_Component = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_Interface296"):
                    opp_val = getattr(item, "CompleteDSLPckg_Interface296", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_Interface296", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_Interface296"):
                    opp_val = getattr(item, "CompleteDSLPckg_Interface296", None)
                    
                    setattr(item, "CompleteDSLPckg_Interface296", self)
                    

    @property
    def CompleteDSLPckg_Component298(self):
        return self.__CompleteDSLPckg_Component298

    @CompleteDSLPckg_Component298.setter
    def CompleteDSLPckg_Component298(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Component__CompleteDSLPckg_Component298", None)
        self.__CompleteDSLPckg_Component298 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_Interface299"):
                    opp_val = getattr(item, "CompleteDSLPckg_Interface299", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_Interface299", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_Interface299"):
                    opp_val = getattr(item, "CompleteDSLPckg_Interface299", None)
                    
                    setattr(item, "CompleteDSLPckg_Interface299", self)
                    

    @property
    def CompleteDSLPckg_Component303(self):
        return self.__CompleteDSLPckg_Component303

    @CompleteDSLPckg_Component303.setter
    def CompleteDSLPckg_Component303(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Component__CompleteDSLPckg_Component303", None)
        self.__CompleteDSLPckg_Component303 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_PackageableElement304"):
                    opp_val = getattr(item, "CompleteDSLPckg_PackageableElement304", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_PackageableElement304", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_PackageableElement304"):
                    opp_val = getattr(item, "CompleteDSLPckg_PackageableElement304", None)
                    
                    setattr(item, "CompleteDSLPckg_PackageableElement304", self)
                    

    @property
    def CompleteDSLPckg_Component301(self):
        return self.__CompleteDSLPckg_Component301

    @CompleteDSLPckg_Component301.setter
    def CompleteDSLPckg_Component301(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Component__CompleteDSLPckg_Component301", None)
        self.__CompleteDSLPckg_Component301 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_ComponentRealization"):
                    opp_val = getattr(item, "CompleteDSLPckg_ComponentRealization", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_ComponentRealization", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_ComponentRealization"):
                    opp_val = getattr(item, "CompleteDSLPckg_ComponentRealization", None)
                    
                    setattr(item, "CompleteDSLPckg_ComponentRealization", self)
                    

class CompleteDSLPckg_GeneralOrdering(NamedElement):

    pass
class CompleteDSLPckg_ActivityNode(NamedElement, RedefinableElement):

    pass
class CompleteDSLPckg_MessageEnd(NamedElement):

    pass
class CompleteDSLPckg_Vertex(NamedElement):

    pass
class CompleteDSLPckg_Lifeline(NamedElement):

    pass
class CompleteDSLPckg_TypedElement(NamedElement):

    pass
class CompleteDSLPckg_InteractionFragment(NamedElement):

    pass
class CompleteDSLPckg_Trigger(NamedElement):

    pass
class CompleteDSLPckg_DeploymentTarget(NamedElement):

    pass
class CompleteDSLPckg_ActivityGroup(NamedElement):

    pass
class CompleteDSLPckg_Include(NamedElement, DirectedRelationship):

    pass
class CompleteDSLPckg_RedefinableElement(NamedElement):

    def __init__(self, isLeaf: bool, CompleteDSLPckg_RedefinableElement82: set["CompleteDSLPckg_Classifier"] = None, CompleteDSLPckg_RedefinableElement: "CompleteDSLPckg_RedefinableElement" = None, CompleteDSLPckg_RedefinableElement79: set["CompleteDSLPckg_RedefinableElement"] = None):
        self.isLeaf = isLeaf
        self.CompleteDSLPckg_RedefinableElement82 = CompleteDSLPckg_RedefinableElement82 if CompleteDSLPckg_RedefinableElement82 is not None else set()
        self.CompleteDSLPckg_RedefinableElement = CompleteDSLPckg_RedefinableElement
        self.CompleteDSLPckg_RedefinableElement79 = CompleteDSLPckg_RedefinableElement79 if CompleteDSLPckg_RedefinableElement79 is not None else set()
        
        pass
    @property
    def isLeaf(self):
        return self.__isLeaf

    @isLeaf.setter
    def isLeaf(self, isLeaf: bool):
        self.__isLeaf = isLeaf


    @property
    def CompleteDSLPckg_RedefinableElement82(self):
        return self.__CompleteDSLPckg_RedefinableElement82

    @CompleteDSLPckg_RedefinableElement82.setter
    def CompleteDSLPckg_RedefinableElement82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_RedefinableElement__CompleteDSLPckg_RedefinableElement82", None)
        self.__CompleteDSLPckg_RedefinableElement82 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_Classifier83"):
                    opp_val = getattr(item, "CompleteDSLPckg_Classifier83", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_Classifier83", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_Classifier83"):
                    opp_val = getattr(item, "CompleteDSLPckg_Classifier83", None)
                    
                    setattr(item, "CompleteDSLPckg_Classifier83", self)
                    

    @property
    def CompleteDSLPckg_RedefinableElement(self):
        return self.__CompleteDSLPckg_RedefinableElement

    @CompleteDSLPckg_RedefinableElement.setter
    def CompleteDSLPckg_RedefinableElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_RedefinableElement__CompleteDSLPckg_RedefinableElement", None)
        self.__CompleteDSLPckg_RedefinableElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_RedefinableElement79"):
                opp_val = getattr(old_value, "CompleteDSLPckg_RedefinableElement79", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_RedefinableElement79"):
                opp_val = getattr(value, "CompleteDSLPckg_RedefinableElement79", None)
                if opp_val is None:
                    setattr(value, "CompleteDSLPckg_RedefinableElement79", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CompleteDSLPckg_RedefinableElement79(self):
        return self.__CompleteDSLPckg_RedefinableElement79

    @CompleteDSLPckg_RedefinableElement79.setter
    def CompleteDSLPckg_RedefinableElement79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_RedefinableElement__CompleteDSLPckg_RedefinableElement79", None)
        self.__CompleteDSLPckg_RedefinableElement79 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_RedefinableElement"):
                    opp_val = getattr(item, "CompleteDSLPckg_RedefinableElement", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_RedefinableElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_RedefinableElement"):
                    opp_val = getattr(item, "CompleteDSLPckg_RedefinableElement", None)
                    
                    setattr(item, "CompleteDSLPckg_RedefinableElement", self)
                    
