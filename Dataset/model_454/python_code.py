from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class InteractionOperatorKind(Enum):
    seq = "seq"
    alt = "alt"
    opt = "opt"
    break = "break"
    par = "par"
    strict = "strict"
    loop = "loop"
    critical = "critical"
    neg = "neg"
    assert = "assert"
    ignore = "ignore"
    consider = "consider"
class VisibilityKind(Enum):
    public = "public"
    private = "private"
    protected = "protected"
    package = "package"
class TransitionKind(Enum):
    internal = "internal"
    local = "local"
    external = "external"
class ParameterEffectKind(Enum):
    create = "create"
    read = "read"
    update = "update"
    delete = "delete"
class ParameterDirectionKind(Enum):
    in = "in"
    inout = "inout"
    out = "out"
    return = "return"
class ObjectNodeOrderingKind(Enum):
    unordered = "unordered"
    ordered = "ordered"
    LIFO = "LIFO"
    FIFO = "FIFO"
class ConnectorKind(Enum):
    assembly = "assembly"
    delegation = "delegation"
class ExpansionKind(Enum):
    parallel = "parallel"
    iterative = "iterative"
    stream = "stream"
class MessageSort(Enum):
    synchCall = "synchCall"
    asynchCall = "asynchCall"
    asynchSignal = "asynchSignal"
    createMessage = "createMessage"
    deleteMessage = "deleteMessage"
    reply = "reply"
class AggregationKind(Enum):
    none = "none"
    shared = "shared"
    composite = "composite"
class PseudostateKind(Enum):
    exitPoint = "exitPoint"
    terminate = "terminate"
    initial = "initial"
    deepHistory = "deepHistory"
    shallowHistory = "shallowHistory"
    join = "join"
    fork = "fork"
    junction = "junction"
    choice = "choice"
    entryPoint = "entryPoint"
class CallConcurrencyKind(Enum):
    sequential = "sequential"
    guarded = "guarded"
    concurrent = "concurrent"
class MessageKind(Enum):
    complete = "complete"
    lost = "lost"
    found = "found"
    unknown = "unknown"


############################################
# Definition of Classes
############################################

class EObject:

    pass
class UMLModel_UMLBase(EObject):

    def __init__(self, umlID: str):
        self.umlID = umlID
        
    @property
    def umlID(self) -> str:
        return self.__umlID

    @umlID.setter
    def umlID(self, umlID: str):
        self.__umlID = umlID

class Expression:

    pass
class TemplateSignature:

    pass
class LinkAction:

    pass
class UMLModel_WriteLinkAction(LinkAction):

    pass
class UMLModel_ReadLinkAction(LinkAction):

    pass
class StructuralFeature:

    pass
class StateMachine:

    pass
class Transition:

    pass
class UMLModel_ProtocolTransition(Transition):

    def __init__(self, postCondition: str, referred: str, preCondition: str):
        self.postCondition = postCondition
        self.referred = referred
        self.preCondition = preCondition
        
    @property
    def referred(self) -> str:
        return self.__referred

    @referred.setter
    def referred(self, referred: str):
        self.__referred = referred

    @property
    def postCondition(self) -> str:
        return self.__postCondition

    @postCondition.setter
    def postCondition(self, postCondition: str):
        self.__postCondition = postCondition

    @property
    def preCondition(self) -> str:
        return self.__preCondition

    @preCondition.setter
    def preCondition(self, preCondition: str):
        self.__preCondition = preCondition

class InteractionUse:

    pass
class UMLModel_PartDecomposition(InteractionUse):

    pass
class ConnectableElement:

    pass
class BehavioralFeature:

    pass
class Package:

    pass
class UMLModel_Profile(Package):

    def __init__(self, ownedStereotype: str, metaclassReference: str, metamodelReference: str):
        self.ownedStereotype = ownedStereotype
        self.metaclassReference = metaclassReference
        self.metamodelReference = metamodelReference
        
    @property
    def ownedStereotype(self) -> str:
        return self.__ownedStereotype

    @ownedStereotype.setter
    def ownedStereotype(self, ownedStereotype: str):
        self.__ownedStereotype = ownedStereotype

    @property
    def metamodelReference(self) -> str:
        return self.__metamodelReference

    @metamodelReference.setter
    def metamodelReference(self, metamodelReference: str):
        self.__metamodelReference = metamodelReference

    @property
    def metaclassReference(self) -> str:
        return self.__metaclassReference

    @metaclassReference.setter
    def metaclassReference(self, metaclassReference: str):
        self.__metaclassReference = metaclassReference

class UMLModel_Model(Package):

    def __init__(self, viewpoint: str):
        self.viewpoint = viewpoint
        
    @property
    def viewpoint(self) -> str:
        return self.__viewpoint

    @viewpoint.setter
    def viewpoint(self, viewpoint: str):
        self.__viewpoint = viewpoint

class LinkEndData:

    pass
class UMLModel_LinkEndDestructionData(LinkEndData):

    def __init__(self, isDestroyDuplicates: str, destroyAt: str):
        self.isDestroyDuplicates = isDestroyDuplicates
        self.destroyAt = destroyAt
        
    @property
    def destroyAt(self) -> str:
        return self.__destroyAt

    @destroyAt.setter
    def destroyAt(self, destroyAt: str):
        self.__destroyAt = destroyAt

    @property
    def isDestroyDuplicates(self) -> str:
        return self.__isDestroyDuplicates

    @isDestroyDuplicates.setter
    def isDestroyDuplicates(self, isDestroyDuplicates: str):
        self.__isDestroyDuplicates = isDestroyDuplicates

class UMLModel_LinkEndCreationData(LinkEndData):

    def __init__(self, isReplaceAll: str, insertAt: str):
        self.isReplaceAll = isReplaceAll
        self.insertAt = insertAt
        
    @property
    def insertAt(self) -> str:
        return self.__insertAt

    @insertAt.setter
    def insertAt(self, insertAt: str):
        self.__insertAt = insertAt

    @property
    def isReplaceAll(self) -> str:
        return self.__isReplaceAll

    @isReplaceAll.setter
    def isReplaceAll(self, isReplaceAll: str):
        self.__isReplaceAll = isReplaceAll

class Abstraction:

    pass
class UMLModel_Realization(Abstraction):

    pass
class LiteralSpecification:

    pass
class UMLModel_LiteralNull(LiteralSpecification):

    pass
class UMLModel_LiteralUnlimitedNatural(LiteralSpecification):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class UMLModel_LiteralString(LiteralSpecification):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class UMLModel_LiteralBoolean(LiteralSpecification):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class UMLModel_LiteralInteger(LiteralSpecification):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class Constraint:

    pass
class UMLModel_IntervalConstraint(Constraint):

    pass
class UMLModel_InteractionConstraint(Constraint):

    pass
class Pin:

    pass
class DeploymentTarget:

    pass
class UMLModel_ProtocolStateMachine(StateMachine):

    pass
class MessageEnd:

    pass
class OpaqueBehavior:

    pass
class UMLModel_FunctionBehavior(OpaqueBehavior):

    pass
class State:

    pass
class UMLModel_FinalState(State):

    pass
class Property:

    pass
class UMLModel_Port(Property):

    def __init__(self, isBehavior: str, isService: str, required: str, redefinedPort: str, provided: str, protocol: str):
        self.isBehavior = isBehavior
        self.isService = isService
        self.required = required
        self.redefinedPort = redefinedPort
        self.provided = provided
        self.protocol = protocol
        
    @property
    def provided(self) -> str:
        return self.__provided

    @provided.setter
    def provided(self, provided: str):
        self.__provided = provided

    @property
    def isService(self) -> str:
        return self.__isService

    @isService.setter
    def isService(self, isService: str):
        self.__isService = isService

    @property
    def required(self) -> str:
        return self.__required

    @required.setter
    def required(self, required: str):
        self.__required = required

    @property
    def protocol(self) -> str:
        return self.__protocol

    @protocol.setter
    def protocol(self, protocol: str):
        self.__protocol = protocol

    @property
    def isBehavior(self) -> str:
        return self.__isBehavior

    @isBehavior.setter
    def isBehavior(self, isBehavior: str):
        self.__isBehavior = isBehavior

    @property
    def redefinedPort(self) -> str:
        return self.__redefinedPort

    @redefinedPort.setter
    def redefinedPort(self, redefinedPort: str):
        self.__redefinedPort = redefinedPort

class UMLModel_ExtensionEnd(Property):

    pass
class UMLBase:

    pass
class UMLModel_Element(UMLBase):

    def __init__(self, owner: str, ownedElement: str, href: str, UMLModel_Element: set["UMLModel_Comment"] = None):
        self.owner = owner
        self.ownedElement = ownedElement
        self.href = href
        self.UMLModel_Element = UMLModel_Element if UMLModel_Element is not None else set()
        
    @property
    def href(self) -> str:
        return self.__href

    @href.setter
    def href(self, href: str):
        self.__href = href

    @property
    def owner(self) -> str:
        return self.__owner

    @owner.setter
    def owner(self, owner: str):
        self.__owner = owner

    @property
    def ownedElement(self) -> str:
        return self.__ownedElement

    @ownedElement.setter
    def ownedElement(self, ownedElement: str):
        self.__ownedElement = ownedElement

    @property
    def UMLModel_Element(self):
        return self.__UMLModel_Element

    @UMLModel_Element.setter
    def UMLModel_Element(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Element__UMLModel_Element", None)
        self.__UMLModel_Element = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UMLModel_Comment"):
                    opp_val = getattr(item, "UMLModel_Comment", None)
                    
                    if opp_val == self:
                        setattr(item, "UMLModel_Comment", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UMLModel_Comment"):
                    opp_val = getattr(item, "UMLModel_Comment", None)
                    
                    setattr(item, "UMLModel_Comment", self)
                    

class Observation:

    pass
class UMLModel_TimeObservation(Observation):

    def __init__(self, event: str, firstEvent: str):
        self.event = event
        self.firstEvent = firstEvent
        
    @property
    def event(self) -> str:
        return self.__event

    @event.setter
    def event(self, event: str):
        self.__event = event

    @property
    def firstEvent(self) -> str:
        return self.__firstEvent

    @firstEvent.setter
    def firstEvent(self, firstEvent: str):
        self.__firstEvent = firstEvent

class UMLModel_DurationObservation(Observation):

    def __init__(self, event: str, firstEvent: str):
        self.event = event
        self.firstEvent = firstEvent
        
    @property
    def firstEvent(self) -> str:
        return self.__firstEvent

    @firstEvent.setter
    def firstEvent(self, firstEvent: str):
        self.__firstEvent = firstEvent

    @property
    def event(self) -> str:
        return self.__event

    @event.setter
    def event(self, event: str):
        self.__event = event

class Interval:

    pass
class UMLModel_TimeInterval(Interval):

    pass
class UMLModel_DurationInterval(Interval):

    pass
class IntervalConstraint:

    pass
class UMLModel_TimeConstraint(IntervalConstraint):

    def __init__(self, firstEvent: str):
        self.firstEvent = firstEvent
        
    @property
    def firstEvent(self) -> str:
        return self.__firstEvent

    @firstEvent.setter
    def firstEvent(self, firstEvent: str):
        self.__firstEvent = firstEvent

class UMLModel_DurationConstraint(IntervalConstraint):

    def __init__(self, firstEvent: str):
        self.firstEvent = firstEvent
        
    @property
    def firstEvent(self) -> str:
        return self.__firstEvent

    @firstEvent.setter
    def firstEvent(self, firstEvent: str):
        self.__firstEvent = firstEvent

class OccurrenceSpecification:

    pass
class UMLModel_MessageOccurrenceSpecification(OccurrenceSpecification, MessageEnd):

    pass
class UMLModel_ExecutionOccurrenceSpecification(OccurrenceSpecification):

    def __init__(self, execution: str):
        self.execution = execution
        
    @property
    def execution(self) -> str:
        return self.__execution

    @execution.setter
    def execution(self, execution: str):
        self.__execution = execution

class InstanceSpecification:

    pass
class UMLModel_EnumerationLiteral(InstanceSpecification):

    def __init__(self, enumeration: str, UMLModel_EnumerationLiteral: "UMLModel_Enumeration" = None):
        self.enumeration = enumeration
        self.UMLModel_EnumerationLiteral = UMLModel_EnumerationLiteral
        
    @property
    def enumeration(self) -> str:
        return self.__enumeration

    @enumeration.setter
    def enumeration(self, enumeration: str):
        self.__enumeration = enumeration

    @property
    def UMLModel_EnumerationLiteral(self):
        return self.__UMLModel_EnumerationLiteral

    @UMLModel_EnumerationLiteral.setter
    def UMLModel_EnumerationLiteral(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_EnumerationLiteral__UMLModel_EnumerationLiteral", None)
        self.__UMLModel_EnumerationLiteral = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_Enumeration"):
                opp_val = getattr(old_value, "UMLModel_Enumeration", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_Enumeration"):
                opp_val = getattr(value, "UMLModel_Enumeration", None)
                if opp_val is None:
                    setattr(value, "UMLModel_Enumeration", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class DataType:

    pass
class UMLModel_PrimitiveType(DataType):

    pass
class UMLModel_Enumeration(DataType):

    pass
class DirectedRelationship:

    pass
class UMLModel_PackageMerge(DirectedRelationship):

    def __init__(self, mergedPackage: str, receivingPackage: str, UMLModel_PackageMerge: "UMLModel_Package" = None):
        self.mergedPackage = mergedPackage
        self.receivingPackage = receivingPackage
        self.UMLModel_PackageMerge = UMLModel_PackageMerge
        
    @property
    def receivingPackage(self) -> str:
        return self.__receivingPackage

    @receivingPackage.setter
    def receivingPackage(self, receivingPackage: str):
        self.__receivingPackage = receivingPackage

    @property
    def mergedPackage(self) -> str:
        return self.__mergedPackage

    @mergedPackage.setter
    def mergedPackage(self, mergedPackage: str):
        self.__mergedPackage = mergedPackage

    @property
    def UMLModel_PackageMerge(self):
        return self.__UMLModel_PackageMerge

    @UMLModel_PackageMerge.setter
    def UMLModel_PackageMerge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_PackageMerge__UMLModel_PackageMerge", None)
        self.__UMLModel_PackageMerge = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_Package"):
                opp_val = getattr(old_value, "UMLModel_Package", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_Package"):
                opp_val = getattr(value, "UMLModel_Package", None)
                if opp_val is None:
                    setattr(value, "UMLModel_Package", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class UMLModel_ProtocolConformance(DirectedRelationship):

    def __init__(self, generalMachine: str, specificMachine: str, UMLModel_ProtocolConformance: "UMLModel_ProtocolStateMachine" = None):
        self.generalMachine = generalMachine
        self.specificMachine = specificMachine
        self.UMLModel_ProtocolConformance = UMLModel_ProtocolConformance
        
    @property
    def generalMachine(self) -> str:
        return self.__generalMachine

    @generalMachine.setter
    def generalMachine(self, generalMachine: str):
        self.__generalMachine = generalMachine

    @property
    def specificMachine(self) -> str:
        return self.__specificMachine

    @specificMachine.setter
    def specificMachine(self, specificMachine: str):
        self.__specificMachine = specificMachine

    @property
    def UMLModel_ProtocolConformance(self):
        return self.__UMLModel_ProtocolConformance

    @UMLModel_ProtocolConformance.setter
    def UMLModel_ProtocolConformance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_ProtocolConformance__UMLModel_ProtocolConformance", None)
        self.__UMLModel_ProtocolConformance = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_ProtocolStateMachine230"):
                opp_val = getattr(old_value, "UMLModel_ProtocolStateMachine230", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_ProtocolStateMachine230"):
                opp_val = getattr(value, "UMLModel_ProtocolStateMachine230", None)
                if opp_val is None:
                    setattr(value, "UMLModel_ProtocolStateMachine230", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class UMLModel_PackageImport(DirectedRelationship):

    def __init__(self, visibility: str, importingNamespace: str, UMLModel_PackageImport: "UMLModel_Namespace" = None, UMLModel_PackageImport218: "UMLModel_PackageableElement" = None):
        self.visibility = visibility
        self.importingNamespace = importingNamespace
        self.UMLModel_PackageImport = UMLModel_PackageImport
        self.UMLModel_PackageImport218 = UMLModel_PackageImport218
        
    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def importingNamespace(self) -> str:
        return self.__importingNamespace

    @importingNamespace.setter
    def importingNamespace(self, importingNamespace: str):
        self.__importingNamespace = importingNamespace

    @property
    def UMLModel_PackageImport(self):
        return self.__UMLModel_PackageImport

    @UMLModel_PackageImport.setter
    def UMLModel_PackageImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_PackageImport__UMLModel_PackageImport", None)
        self.__UMLModel_PackageImport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_Namespace195"):
                opp_val = getattr(old_value, "UMLModel_Namespace195", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_Namespace195"):
                opp_val = getattr(value, "UMLModel_Namespace195", None)
                if opp_val is None:
                    setattr(value, "UMLModel_Namespace195", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UMLModel_PackageImport218(self):
        return self.__UMLModel_PackageImport218

    @UMLModel_PackageImport218.setter
    def UMLModel_PackageImport218(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_PackageImport__UMLModel_PackageImport218", None)
        self.__UMLModel_PackageImport218 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_PackageableElement219"):
                opp_val = getattr(old_value, "UMLModel_PackageableElement219", None)
                if opp_val == self:
                    setattr(old_value, "UMLModel_PackageableElement219", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_PackageableElement219"):
                opp_val = getattr(value, "UMLModel_PackageableElement219", None)
                setattr(value, "UMLModel_PackageableElement219", self)

class UMLModel_ElementImport(DirectedRelationship):

    def __init__(self, visibility: str, alias: str, importingNamespace: str, UMLModel_ElementImport: "UMLModel_PackageableElement" = None, UMLModel_ElementImport193: "UMLModel_Namespace" = None):
        self.visibility = visibility
        self.alias = alias
        self.importingNamespace = importingNamespace
        self.UMLModel_ElementImport = UMLModel_ElementImport
        self.UMLModel_ElementImport193 = UMLModel_ElementImport193
        
    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def importingNamespace(self) -> str:
        return self.__importingNamespace

    @importingNamespace.setter
    def importingNamespace(self, importingNamespace: str):
        self.__importingNamespace = importingNamespace

    @property
    def alias(self) -> str:
        return self.__alias

    @alias.setter
    def alias(self, alias: str):
        self.__alias = alias

    @property
    def UMLModel_ElementImport193(self):
        return self.__UMLModel_ElementImport193

    @UMLModel_ElementImport193.setter
    def UMLModel_ElementImport193(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_ElementImport__UMLModel_ElementImport193", None)
        self.__UMLModel_ElementImport193 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_Namespace"):
                opp_val = getattr(old_value, "UMLModel_Namespace", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_Namespace"):
                opp_val = getattr(value, "UMLModel_Namespace", None)
                if opp_val is None:
                    setattr(value, "UMLModel_Namespace", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UMLModel_ElementImport(self):
        return self.__UMLModel_ElementImport

    @UMLModel_ElementImport.setter
    def UMLModel_ElementImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_ElementImport__UMLModel_ElementImport", None)
        self.__UMLModel_ElementImport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_PackageableElement112"):
                opp_val = getattr(old_value, "UMLModel_PackageableElement112", None)
                if opp_val == self:
                    setattr(old_value, "UMLModel_PackageableElement112", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_PackageableElement112"):
                opp_val = getattr(value, "UMLModel_PackageableElement112", None)
                setattr(value, "UMLModel_PackageableElement112", self)

class UMLModel_TemplateBinding(DirectedRelationship):

    def __init__(self, signature: str, boundElement: str, UMLModel_TemplateBinding: "UMLModel_TemplateableElement" = None, UMLModel_TemplateBinding344: set["UMLModel_TemplateParameterSubstitution"] = None):
        self.signature = signature
        self.boundElement = boundElement
        self.UMLModel_TemplateBinding = UMLModel_TemplateBinding
        self.UMLModel_TemplateBinding344 = UMLModel_TemplateBinding344 if UMLModel_TemplateBinding344 is not None else set()
        
    @property
    def boundElement(self) -> str:
        return self.__boundElement

    @boundElement.setter
    def boundElement(self, boundElement: str):
        self.__boundElement = boundElement

    @property
    def signature(self) -> str:
        return self.__signature

    @signature.setter
    def signature(self, signature: str):
        self.__signature = signature

    @property
    def UMLModel_TemplateBinding(self):
        return self.__UMLModel_TemplateBinding

    @UMLModel_TemplateBinding.setter
    def UMLModel_TemplateBinding(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_TemplateBinding__UMLModel_TemplateBinding", None)
        self.__UMLModel_TemplateBinding = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_TemplateableElement"):
                opp_val = getattr(old_value, "UMLModel_TemplateableElement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_TemplateableElement"):
                opp_val = getattr(value, "UMLModel_TemplateableElement", None)
                if opp_val is None:
                    setattr(value, "UMLModel_TemplateableElement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UMLModel_TemplateBinding344(self):
        return self.__UMLModel_TemplateBinding344

    @UMLModel_TemplateBinding344.setter
    def UMLModel_TemplateBinding344(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_TemplateBinding__UMLModel_TemplateBinding344", None)
        self.__UMLModel_TemplateBinding344 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UMLModel_TemplateParameterSubstitution"):
                    opp_val = getattr(item, "UMLModel_TemplateParameterSubstitution", None)
                    
                    if opp_val == self:
                        setattr(item, "UMLModel_TemplateParameterSubstitution", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UMLModel_TemplateParameterSubstitution"):
                    opp_val = getattr(item, "UMLModel_TemplateParameterSubstitution", None)
                    
                    setattr(item, "UMLModel_TemplateParameterSubstitution", self)
                    

class UMLModel_ProfileApplication(DirectedRelationship):

    def __init__(self, appliedProfile: str, isStrict: str, applyingPackage: str, UMLModel_ProfileApplication: "UMLModel_Package" = None):
        self.appliedProfile = appliedProfile
        self.isStrict = isStrict
        self.applyingPackage = applyingPackage
        self.UMLModel_ProfileApplication = UMLModel_ProfileApplication
        
    @property
    def appliedProfile(self) -> str:
        return self.__appliedProfile

    @appliedProfile.setter
    def appliedProfile(self, appliedProfile: str):
        self.__appliedProfile = appliedProfile

    @property
    def applyingPackage(self) -> str:
        return self.__applyingPackage

    @applyingPackage.setter
    def applyingPackage(self, applyingPackage: str):
        self.__applyingPackage = applyingPackage

    @property
    def isStrict(self) -> str:
        return self.__isStrict

    @isStrict.setter
    def isStrict(self, isStrict: str):
        self.__isStrict = isStrict

    @property
    def UMLModel_ProfileApplication(self):
        return self.__UMLModel_ProfileApplication

    @UMLModel_ProfileApplication.setter
    def UMLModel_ProfileApplication(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_ProfileApplication__UMLModel_ProfileApplication", None)
        self.__UMLModel_ProfileApplication = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_Package216"):
                opp_val = getattr(old_value, "UMLModel_Package216", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_Package216"):
                opp_val = getattr(value, "UMLModel_Package216", None)
                if opp_val is None:
                    setattr(value, "UMLModel_Package216", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ControlNode:

    pass
class UMLModel_InitialNode(ControlNode):

    pass
class UMLModel_FinalNode(ControlNode):

    pass
class UMLModel_MergeNode(ControlNode):

    pass
class UMLModel_JoinNode(ControlNode):

    def __init__(self, isCombineDuplicate: str, UMLModel_JoinNode: "UMLModel_ValueSpecification" = None):
        self.isCombineDuplicate = isCombineDuplicate
        self.UMLModel_JoinNode = UMLModel_JoinNode
        
    @property
    def isCombineDuplicate(self) -> str:
        return self.__isCombineDuplicate

    @isCombineDuplicate.setter
    def isCombineDuplicate(self, isCombineDuplicate: str):
        self.__isCombineDuplicate = isCombineDuplicate

    @property
    def UMLModel_JoinNode(self):
        return self.__UMLModel_JoinNode

    @UMLModel_JoinNode.setter
    def UMLModel_JoinNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_JoinNode__UMLModel_JoinNode", None)
        self.__UMLModel_JoinNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_ValueSpecification168"):
                opp_val = getattr(old_value, "UMLModel_ValueSpecification168", None)
                if opp_val == self:
                    setattr(old_value, "UMLModel_ValueSpecification168", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_ValueSpecification168"):
                opp_val = getattr(value, "UMLModel_ValueSpecification168", None)
                setattr(value, "UMLModel_ValueSpecification168", self)

class UMLModel_ForkNode(ControlNode):

    pass
class UMLModel_DecisionNode(ControlNode):

    def __init__(self, decisionInput: str):
        self.decisionInput = decisionInput
        
    @property
    def decisionInput(self) -> str:
        return self.__decisionInput

    @decisionInput.setter
    def decisionInput(self, decisionInput: str):
        self.__decisionInput = decisionInput

class CentralBufferNode:

    pass
class UMLModel_DataStoreNode(CentralBufferNode):

    pass
class ValueSpecification:

    pass
class UMLModel_Expression(ValueSpecification):

    def __init__(self, symbol: str, UMLModel_Expression: set["UMLModel_ValueSpecification"] = None):
        self.symbol = symbol
        self.UMLModel_Expression = UMLModel_Expression if UMLModel_Expression is not None else set()
        
    @property
    def symbol(self) -> str:
        return self.__symbol

    @symbol.setter
    def symbol(self, symbol: str):
        self.__symbol = symbol

    @property
    def UMLModel_Expression(self):
        return self.__UMLModel_Expression

    @UMLModel_Expression.setter
    def UMLModel_Expression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Expression__UMLModel_Expression", None)
        self.__UMLModel_Expression = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UMLModel_ValueSpecification118"):
                    opp_val = getattr(item, "UMLModel_ValueSpecification118", None)
                    
                    if opp_val == self:
                        setattr(item, "UMLModel_ValueSpecification118", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UMLModel_ValueSpecification118"):
                    opp_val = getattr(item, "UMLModel_ValueSpecification118", None)
                    
                    setattr(item, "UMLModel_ValueSpecification118", self)
                    

class UMLModel_Interval(ValueSpecification):

    def __init__(self, min: str, max: str):
        self.min = min
        self.max = max
        
    @property
    def max(self) -> str:
        return self.__max

    @max.setter
    def max(self, max: str):
        self.__max = max

    @property
    def min(self) -> str:
        return self.__min

    @min.setter
    def min(self, min: str):
        self.__min = min

class UMLModel_InstanceValue(ValueSpecification):

    def __init__(self, instance: str):
        self.instance = instance
        
    @property
    def instance(self) -> str:
        return self.__instance

    @instance.setter
    def instance(self, instance: str):
        self.__instance = instance

class UMLModel_LiteralSpecification(ValueSpecification):

    pass
class UMLModel_TimeExpression(ValueSpecification):

    def __init__(self, expr: str, observation: str):
        self.expr = expr
        self.observation = observation
        
    @property
    def observation(self) -> str:
        return self.__observation

    @observation.setter
    def observation(self, observation: str):
        self.__observation = observation

    @property
    def expr(self) -> str:
        return self.__expr

    @expr.setter
    def expr(self, expr: str):
        self.__expr = expr

class UMLModel_Duration(ValueSpecification):

    def __init__(self, expr: str, observation: str):
        self.expr = expr
        self.observation = observation
        
    @property
    def expr(self) -> str:
        return self.__expr

    @expr.setter
    def expr(self, expr: str):
        self.__expr = expr

    @property
    def observation(self) -> str:
        return self.__observation

    @observation.setter
    def observation(self, observation: str):
        self.__observation = observation

class Node:

    pass
class UMLModel_ExecutionEnvironment(Node):

    pass
class UMLModel_Device(Node):

    pass
class Artifact:

    pass
class UMLModel_DeploymentSpecification(Artifact):

    def __init__(self, deploymentLocation: str, executionLocation: str, deployment: str, UMLModel_DeploymentSpecification: "UMLModel_Deployment" = None):
        self.deploymentLocation = deploymentLocation
        self.executionLocation = executionLocation
        self.deployment = deployment
        self.UMLModel_DeploymentSpecification = UMLModel_DeploymentSpecification
        
    @property
    def deploymentLocation(self) -> str:
        return self.__deploymentLocation

    @deploymentLocation.setter
    def deploymentLocation(self, deploymentLocation: str):
        self.__deploymentLocation = deploymentLocation

    @property
    def deployment(self) -> str:
        return self.__deployment

    @deployment.setter
    def deployment(self, deployment: str):
        self.__deployment = deployment

    @property
    def executionLocation(self) -> str:
        return self.__executionLocation

    @executionLocation.setter
    def executionLocation(self, executionLocation: str):
        self.__executionLocation = executionLocation

    @property
    def UMLModel_DeploymentSpecification(self):
        return self.__UMLModel_DeploymentSpecification

    @UMLModel_DeploymentSpecification.setter
    def UMLModel_DeploymentSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_DeploymentSpecification__UMLModel_DeploymentSpecification", None)
        self.__UMLModel_DeploymentSpecification = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_Deployment107"):
                opp_val = getattr(old_value, "UMLModel_Deployment107", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_Deployment107"):
                opp_val = getattr(value, "UMLModel_Deployment107", None)
                if opp_val is None:
                    setattr(value, "UMLModel_Deployment107", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class WriteLinkAction:

    pass
class UMLModel_DestroyLinkAction(WriteLinkAction):

    pass
class UMLModel_CreateLinkAction(WriteLinkAction):

    pass
class CreateLinkAction:

    pass
class UMLModel_CreateLinkObjectAction(CreateLinkAction):

    pass
class ActivityNode:

    pass
class UMLModel_ExecutableNode(ActivityNode):

    pass
class UMLModel_ControlNode(ActivityNode):

    pass
class ActivityEdge:

    pass
class UMLModel_ObjectFlow(ActivityEdge):

    def __init__(self, isMulticast: str, isMultireceive: str, transformation: str, selection: str):
        self.isMulticast = isMulticast
        self.isMultireceive = isMultireceive
        self.transformation = transformation
        self.selection = selection
        
    @property
    def transformation(self) -> str:
        return self.__transformation

    @transformation.setter
    def transformation(self, transformation: str):
        self.__transformation = transformation

    @property
    def isMulticast(self) -> str:
        return self.__isMulticast

    @isMulticast.setter
    def isMulticast(self, isMulticast: str):
        self.__isMulticast = isMulticast

    @property
    def selection(self) -> str:
        return self.__selection

    @selection.setter
    def selection(self, selection: str):
        self.__selection = selection

    @property
    def isMultireceive(self) -> str:
        return self.__isMultireceive

    @isMultireceive.setter
    def isMultireceive(self, isMultireceive: str):
        self.__isMultireceive = isMultireceive

class UMLModel_ControlFlow(ActivityEdge):

    pass
class Realization:

    pass
class Vertex:

    pass
class UMLModel_Pseudostate(Vertex):

    def __init__(self, kind: str, stateMachine: str, state: str, UMLModel_Pseudostate333: "UMLModel_StateMachine" = None, UMLModel_Pseudostate: "UMLModel_State" = None):
        self.kind = kind
        self.stateMachine = stateMachine
        self.state = state
        self.UMLModel_Pseudostate333 = UMLModel_Pseudostate333
        self.UMLModel_Pseudostate = UMLModel_Pseudostate
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def state(self) -> str:
        return self.__state

    @state.setter
    def state(self, state: str):
        self.__state = state

    @property
    def stateMachine(self) -> str:
        return self.__stateMachine

    @stateMachine.setter
    def stateMachine(self, stateMachine: str):
        self.__stateMachine = stateMachine

    @property
    def UMLModel_Pseudostate333(self):
        return self.__UMLModel_Pseudostate333

    @UMLModel_Pseudostate333.setter
    def UMLModel_Pseudostate333(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Pseudostate__UMLModel_Pseudostate333", None)
        self.__UMLModel_Pseudostate333 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_StateMachine332"):
                opp_val = getattr(old_value, "UMLModel_StateMachine332", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_StateMachine332"):
                opp_val = getattr(value, "UMLModel_StateMachine332", None)
                if opp_val is None:
                    setattr(value, "UMLModel_StateMachine332", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UMLModel_Pseudostate(self):
        return self.__UMLModel_Pseudostate

    @UMLModel_Pseudostate.setter
    def UMLModel_Pseudostate(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Pseudostate__UMLModel_Pseudostate", None)
        self.__UMLModel_Pseudostate = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_State310"):
                opp_val = getattr(old_value, "UMLModel_State310", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_State310"):
                opp_val = getattr(value, "UMLModel_State310", None)
                if opp_val is None:
                    setattr(value, "UMLModel_State310", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class UMLModel_ConnectionPointReference(Vertex):

    def __init__(self, entry: str, exit: str, state: str, UMLModel_ConnectionPointReference: "UMLModel_State" = None):
        self.entry = entry
        self.exit = exit
        self.state = state
        self.UMLModel_ConnectionPointReference = UMLModel_ConnectionPointReference
        
    @property
    def state(self) -> str:
        return self.__state

    @state.setter
    def state(self, state: str):
        self.__state = state

    @property
    def exit(self) -> str:
        return self.__exit

    @exit.setter
    def exit(self, exit: str):
        self.__exit = exit

    @property
    def entry(self) -> str:
        return self.__entry

    @entry.setter
    def entry(self, entry: str):
        self.__entry = entry

    @property
    def UMLModel_ConnectionPointReference(self):
        return self.__UMLModel_ConnectionPointReference

    @UMLModel_ConnectionPointReference.setter
    def UMLModel_ConnectionPointReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_ConnectionPointReference__UMLModel_ConnectionPointReference", None)
        self.__UMLModel_ConnectionPointReference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_State"):
                opp_val = getattr(old_value, "UMLModel_State", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_State"):
                opp_val = getattr(value, "UMLModel_State", None)
                if opp_val is None:
                    setattr(value, "UMLModel_State", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class MultiplicityElement:

    pass
class UMLModel_ConnectorEnd(MultiplicityElement):

    def __init__(self, definingEnd: str, partWithPort: str, role: str, UMLModel_ConnectorEnd: "UMLModel_Connector" = None):
        self.definingEnd = definingEnd
        self.partWithPort = partWithPort
        self.role = role
        self.UMLModel_ConnectorEnd = UMLModel_ConnectorEnd
        
    @property
    def definingEnd(self) -> str:
        return self.__definingEnd

    @definingEnd.setter
    def definingEnd(self, definingEnd: str):
        self.__definingEnd = definingEnd

    @property
    def role(self) -> str:
        return self.__role

    @role.setter
    def role(self, role: str):
        self.__role = role

    @property
    def partWithPort(self) -> str:
        return self.__partWithPort

    @partWithPort.setter
    def partWithPort(self, partWithPort: str):
        self.__partWithPort = partWithPort

    @property
    def UMLModel_ConnectorEnd(self):
        return self.__UMLModel_ConnectorEnd

    @UMLModel_ConnectorEnd.setter
    def UMLModel_ConnectorEnd(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_ConnectorEnd__UMLModel_ConnectorEnd", None)
        self.__UMLModel_ConnectorEnd = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_Connector"):
                opp_val = getattr(old_value, "UMLModel_Connector", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_Connector"):
                opp_val = getattr(value, "UMLModel_Connector", None)
                if opp_val is None:
                    setattr(value, "UMLModel_Connector", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ParameterableElement:

    pass
class TypedElement:

    pass
class UMLModel_ObjectNode(ActivityNode, TypedElement):

    def __init__(self, ordering: str, isControlType: str, inState: str, selection: str, UMLModel_ObjectNode: "UMLModel_ValueSpecification" = None):
        self.ordering = ordering
        self.isControlType = isControlType
        self.inState = inState
        self.selection = selection
        self.UMLModel_ObjectNode = UMLModel_ObjectNode
        
    @property
    def inState(self) -> str:
        return self.__inState

    @inState.setter
    def inState(self, inState: str):
        self.__inState = inState

    @property
    def selection(self) -> str:
        return self.__selection

    @selection.setter
    def selection(self, selection: str):
        self.__selection = selection

    @property
    def ordering(self) -> str:
        return self.__ordering

    @ordering.setter
    def ordering(self, ordering: str):
        self.__ordering = ordering

    @property
    def isControlType(self) -> str:
        return self.__isControlType

    @isControlType.setter
    def isControlType(self, isControlType: str):
        self.__isControlType = isControlType

    @property
    def UMLModel_ObjectNode(self):
        return self.__UMLModel_ObjectNode

    @UMLModel_ObjectNode.setter
    def UMLModel_ObjectNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_ObjectNode__UMLModel_ObjectNode", None)
        self.__UMLModel_ObjectNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_ValueSpecification207"):
                opp_val = getattr(old_value, "UMLModel_ValueSpecification207", None)
                if opp_val == self:
                    setattr(old_value, "UMLModel_ValueSpecification207", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_ValueSpecification207"):
                opp_val = getattr(value, "UMLModel_ValueSpecification207", None)
                setattr(value, "UMLModel_ValueSpecification207", self)

class UMLModel_ConnectableElement(TypedElement, ParameterableElement):

    def __init__(self, end: str):
        self.end = end
        
    @property
    def end(self) -> str:
        return self.__end

    @end.setter
    def end(self, end: str):
        self.__end = end

class CombinedFragment:

    pass
class UMLModel_ConsiderIgnoreFragment(CombinedFragment):

    def __init__(self, message: str):
        self.message = message
        
    @property
    def message(self) -> str:
        return self.__message

    @message.setter
    def message(self, message: str):
        self.__message = message

class PackageableElement:

    pass
class UMLModel_Observation(PackageableElement):

    pass
class UMLModel_InformationFlow(DirectedRelationship, PackageableElement):

    def __init__(self, realization: str, conveyed: str, informationSource: str, informationTarget: str, realizingActivityEdge: str, realizingConnector: str, realizingMessage: str):
        self.realization = realization
        self.conveyed = conveyed
        self.informationSource = informationSource
        self.informationTarget = informationTarget
        self.realizingActivityEdge = realizingActivityEdge
        self.realizingConnector = realizingConnector
        self.realizingMessage = realizingMessage
        
    @property
    def realizingConnector(self) -> str:
        return self.__realizingConnector

    @realizingConnector.setter
    def realizingConnector(self, realizingConnector: str):
        self.__realizingConnector = realizingConnector

    @property
    def realization(self) -> str:
        return self.__realization

    @realization.setter
    def realization(self, realization: str):
        self.__realization = realization

    @property
    def realizingMessage(self) -> str:
        return self.__realizingMessage

    @realizingMessage.setter
    def realizingMessage(self, realizingMessage: str):
        self.__realizingMessage = realizingMessage

    @property
    def conveyed(self) -> str:
        return self.__conveyed

    @conveyed.setter
    def conveyed(self, conveyed: str):
        self.__conveyed = conveyed

    @property
    def informationSource(self) -> str:
        return self.__informationSource

    @informationSource.setter
    def informationSource(self, informationSource: str):
        self.__informationSource = informationSource

    @property
    def informationTarget(self) -> str:
        return self.__informationTarget

    @informationTarget.setter
    def informationTarget(self, informationTarget: str):
        self.__informationTarget = informationTarget

    @property
    def realizingActivityEdge(self) -> str:
        return self.__realizingActivityEdge

    @realizingActivityEdge.setter
    def realizingActivityEdge(self, realizingActivityEdge: str):
        self.__realizingActivityEdge = realizingActivityEdge

class UMLModel_GeneralizationSet(PackageableElement):

    def __init__(self, isCovering: str, isDisjoint: str, generalization: str, powerType: str):
        self.isCovering = isCovering
        self.isDisjoint = isDisjoint
        self.generalization = generalization
        self.powerType = powerType
        
    @property
    def generalization(self) -> str:
        return self.__generalization

    @generalization.setter
    def generalization(self, generalization: str):
        self.__generalization = generalization

    @property
    def isCovering(self) -> str:
        return self.__isCovering

    @isCovering.setter
    def isCovering(self, isCovering: str):
        self.__isCovering = isCovering

    @property
    def powerType(self) -> str:
        return self.__powerType

    @powerType.setter
    def powerType(self, powerType: str):
        self.__powerType = powerType

    @property
    def isDisjoint(self) -> str:
        return self.__isDisjoint

    @isDisjoint.setter
    def isDisjoint(self, isDisjoint: str):
        self.__isDisjoint = isDisjoint

class UMLModel_Type(PackageableElement):

    def __init__(self, package: str):
        self.package = package
        
    @property
    def package(self) -> str:
        return self.__package

    @package.setter
    def package(self, package: str):
        self.__package = package

class UMLModel_Event(PackageableElement):

    pass
class StructuredActivityNode:

    pass
class UMLModel_SequenceNode(StructuredActivityNode):

    pass
class UMLModel_LoopNode(StructuredActivityNode):

    def __init__(self, isTestedFirst: str, bodyPart: str, setupPart: str, decider: str, test: str, loopVariable: str, bodyOutput: str, UMLModel_LoopNode: set["UMLModel_OutputPin"] = None, UMLModel_LoopNode181: set["UMLModel_InputPin"] = None):
        self.isTestedFirst = isTestedFirst
        self.bodyPart = bodyPart
        self.setupPart = setupPart
        self.decider = decider
        self.test = test
        self.loopVariable = loopVariable
        self.bodyOutput = bodyOutput
        self.UMLModel_LoopNode = UMLModel_LoopNode if UMLModel_LoopNode is not None else set()
        self.UMLModel_LoopNode181 = UMLModel_LoopNode181 if UMLModel_LoopNode181 is not None else set()
        
    @property
    def setupPart(self) -> str:
        return self.__setupPart

    @setupPart.setter
    def setupPart(self, setupPart: str):
        self.__setupPart = setupPart

    @property
    def test(self) -> str:
        return self.__test

    @test.setter
    def test(self, test: str):
        self.__test = test

    @property
    def decider(self) -> str:
        return self.__decider

    @decider.setter
    def decider(self, decider: str):
        self.__decider = decider

    @property
    def bodyOutput(self) -> str:
        return self.__bodyOutput

    @bodyOutput.setter
    def bodyOutput(self, bodyOutput: str):
        self.__bodyOutput = bodyOutput

    @property
    def bodyPart(self) -> str:
        return self.__bodyPart

    @bodyPart.setter
    def bodyPart(self, bodyPart: str):
        self.__bodyPart = bodyPart

    @property
    def isTestedFirst(self) -> str:
        return self.__isTestedFirst

    @isTestedFirst.setter
    def isTestedFirst(self, isTestedFirst: str):
        self.__isTestedFirst = isTestedFirst

    @property
    def loopVariable(self) -> str:
        return self.__loopVariable

    @loopVariable.setter
    def loopVariable(self, loopVariable: str):
        self.__loopVariable = loopVariable

    @property
    def UMLModel_LoopNode(self):
        return self.__UMLModel_LoopNode

    @UMLModel_LoopNode.setter
    def UMLModel_LoopNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_LoopNode__UMLModel_LoopNode", None)
        self.__UMLModel_LoopNode = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UMLModel_OutputPin179"):
                    opp_val = getattr(item, "UMLModel_OutputPin179", None)
                    
                    if opp_val == self:
                        setattr(item, "UMLModel_OutputPin179", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UMLModel_OutputPin179"):
                    opp_val = getattr(item, "UMLModel_OutputPin179", None)
                    
                    setattr(item, "UMLModel_OutputPin179", self)
                    

    @property
    def UMLModel_LoopNode181(self):
        return self.__UMLModel_LoopNode181

    @UMLModel_LoopNode181.setter
    def UMLModel_LoopNode181(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_LoopNode__UMLModel_LoopNode181", None)
        self.__UMLModel_LoopNode181 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UMLModel_InputPin182"):
                    opp_val = getattr(item, "UMLModel_InputPin182", None)
                    
                    if opp_val == self:
                        setattr(item, "UMLModel_InputPin182", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UMLModel_InputPin182"):
                    opp_val = getattr(item, "UMLModel_InputPin182", None)
                    
                    setattr(item, "UMLModel_InputPin182", self)
                    

class UMLModel_ExpansionRegion(StructuredActivityNode):

    def __init__(self, mode: str, inputElement: str, outputElement: str):
        self.mode = mode
        self.inputElement = inputElement
        self.outputElement = outputElement
        
    @property
    def outputElement(self) -> str:
        return self.__outputElement

    @outputElement.setter
    def outputElement(self, outputElement: str):
        self.__outputElement = outputElement

    @property
    def inputElement(self) -> str:
        return self.__inputElement

    @inputElement.setter
    def inputElement(self, inputElement: str):
        self.__inputElement = inputElement

    @property
    def mode(self) -> str:
        return self.__mode

    @mode.setter
    def mode(self, mode: str):
        self.__mode = mode

class UMLModel_ConditionalNode(StructuredActivityNode):

    def __init__(self, isDeterminate: str, isAssured: str, UMLModel_ConditionalNode: set["UMLModel_Clause"] = None, UMLModel_ConditionalNode90: set["UMLModel_OutputPin"] = None):
        self.isDeterminate = isDeterminate
        self.isAssured = isAssured
        self.UMLModel_ConditionalNode = UMLModel_ConditionalNode if UMLModel_ConditionalNode is not None else set()
        self.UMLModel_ConditionalNode90 = UMLModel_ConditionalNode90 if UMLModel_ConditionalNode90 is not None else set()
        
    @property
    def isAssured(self) -> str:
        return self.__isAssured

    @isAssured.setter
    def isAssured(self, isAssured: str):
        self.__isAssured = isAssured

    @property
    def isDeterminate(self) -> str:
        return self.__isDeterminate

    @isDeterminate.setter
    def isDeterminate(self, isDeterminate: str):
        self.__isDeterminate = isDeterminate

    @property
    def UMLModel_ConditionalNode90(self):
        return self.__UMLModel_ConditionalNode90

    @UMLModel_ConditionalNode90.setter
    def UMLModel_ConditionalNode90(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_ConditionalNode__UMLModel_ConditionalNode90", None)
        self.__UMLModel_ConditionalNode90 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UMLModel_OutputPin91"):
                    opp_val = getattr(item, "UMLModel_OutputPin91", None)
                    
                    if opp_val == self:
                        setattr(item, "UMLModel_OutputPin91", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UMLModel_OutputPin91"):
                    opp_val = getattr(item, "UMLModel_OutputPin91", None)
                    
                    setattr(item, "UMLModel_OutputPin91", self)
                    

    @property
    def UMLModel_ConditionalNode(self):
        return self.__UMLModel_ConditionalNode

    @UMLModel_ConditionalNode.setter
    def UMLModel_ConditionalNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_ConditionalNode__UMLModel_ConditionalNode", None)
        self.__UMLModel_ConditionalNode = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UMLModel_Clause"):
                    opp_val = getattr(item, "UMLModel_Clause", None)
                    
                    if opp_val == self:
                        setattr(item, "UMLModel_Clause", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UMLModel_Clause"):
                    opp_val = getattr(item, "UMLModel_Clause", None)
                    
                    setattr(item, "UMLModel_Clause", self)
                    

class UMLModel_Gate(MessageEnd):

    pass
class InteractionFragment:

    pass
class UMLModel_ExecutionSpecification(InteractionFragment):

    def __init__(self, start: str, finish: str):
        self.start = start
        self.finish = finish
        
    @property
    def start(self) -> str:
        return self.__start

    @start.setter
    def start(self, start: str):
        self.__start = start

    @property
    def finish(self) -> str:
        return self.__finish

    @finish.setter
    def finish(self, finish: str):
        self.__finish = finish

class UMLModel_OccurrenceSpecification(InteractionFragment):

    def __init__(self, toBefore: str, toAfter: str, event: str):
        self.toBefore = toBefore
        self.toAfter = toAfter
        self.event = event
        
    @property
    def toBefore(self) -> str:
        return self.__toBefore

    @toBefore.setter
    def toBefore(self, toBefore: str):
        self.__toBefore = toBefore

    @property
    def toAfter(self) -> str:
        return self.__toAfter

    @toAfter.setter
    def toAfter(self, toAfter: str):
        self.__toAfter = toAfter

    @property
    def event(self) -> str:
        return self.__event

    @event.setter
    def event(self, event: str):
        self.__event = event

class UMLModel_InteractionUse(InteractionFragment):

    def __init__(self, refersTo: str, UMLModel_InteractionUse: set["UMLModel_Gate"] = None, UMLModel_InteractionUse154: set["UMLModel_Action"] = None):
        self.refersTo = refersTo
        self.UMLModel_InteractionUse = UMLModel_InteractionUse if UMLModel_InteractionUse is not None else set()
        self.UMLModel_InteractionUse154 = UMLModel_InteractionUse154 if UMLModel_InteractionUse154 is not None else set()
        
    @property
    def refersTo(self) -> str:
        return self.__refersTo

    @refersTo.setter
    def refersTo(self, refersTo: str):
        self.__refersTo = refersTo

    @property
    def UMLModel_InteractionUse154(self):
        return self.__UMLModel_InteractionUse154

    @UMLModel_InteractionUse154.setter
    def UMLModel_InteractionUse154(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_InteractionUse__UMLModel_InteractionUse154", None)
        self.__UMLModel_InteractionUse154 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UMLModel_Action155"):
                    opp_val = getattr(item, "UMLModel_Action155", None)
                    
                    if opp_val == self:
                        setattr(item, "UMLModel_Action155", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UMLModel_Action155"):
                    opp_val = getattr(item, "UMLModel_Action155", None)
                    
                    setattr(item, "UMLModel_Action155", self)
                    

    @property
    def UMLModel_InteractionUse(self):
        return self.__UMLModel_InteractionUse

    @UMLModel_InteractionUse.setter
    def UMLModel_InteractionUse(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_InteractionUse__UMLModel_InteractionUse", None)
        self.__UMLModel_InteractionUse = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UMLModel_Gate152"):
                    opp_val = getattr(item, "UMLModel_Gate152", None)
                    
                    if opp_val == self:
                        setattr(item, "UMLModel_Gate152", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UMLModel_Gate152"):
                    opp_val = getattr(item, "UMLModel_Gate152", None)
                    
                    setattr(item, "UMLModel_Gate152", self)
                    

class UMLModel_StateInvariant(InteractionFragment):

    pass
class UMLModel_Continuation(InteractionFragment):

    def __init__(self, setting: str):
        self.setting = setting
        
    @property
    def setting(self) -> str:
        return self.__setting

    @setting.setter
    def setting(self, setting: str):
        self.__setting = setting

class UMLModel_CombinedFragment(InteractionFragment):

    def __init__(self, interactionOperator: str, UMLModel_CombinedFragment: set["UMLModel_InteractionOperand"] = None, UMLModel_CombinedFragment87: set["UMLModel_Gate"] = None):
        self.interactionOperator = interactionOperator
        self.UMLModel_CombinedFragment = UMLModel_CombinedFragment if UMLModel_CombinedFragment is not None else set()
        self.UMLModel_CombinedFragment87 = UMLModel_CombinedFragment87 if UMLModel_CombinedFragment87 is not None else set()
        
    @property
    def interactionOperator(self) -> str:
        return self.__interactionOperator

    @interactionOperator.setter
    def interactionOperator(self, interactionOperator: str):
        self.__interactionOperator = interactionOperator

    @property
    def UMLModel_CombinedFragment87(self):
        return self.__UMLModel_CombinedFragment87

    @UMLModel_CombinedFragment87.setter
    def UMLModel_CombinedFragment87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_CombinedFragment__UMLModel_CombinedFragment87", None)
        self.__UMLModel_CombinedFragment87 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UMLModel_Gate"):
                    opp_val = getattr(item, "UMLModel_Gate", None)
                    
                    if opp_val == self:
                        setattr(item, "UMLModel_Gate", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UMLModel_Gate"):
                    opp_val = getattr(item, "UMLModel_Gate", None)
                    
                    setattr(item, "UMLModel_Gate", self)
                    

    @property
    def UMLModel_CombinedFragment(self):
        return self.__UMLModel_CombinedFragment

    @UMLModel_CombinedFragment.setter
    def UMLModel_CombinedFragment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_CombinedFragment__UMLModel_CombinedFragment", None)
        self.__UMLModel_CombinedFragment = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UMLModel_InteractionOperand"):
                    opp_val = getattr(item, "UMLModel_InteractionOperand", None)
                    
                    if opp_val == self:
                        setattr(item, "UMLModel_InteractionOperand", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UMLModel_InteractionOperand"):
                    opp_val = getattr(item, "UMLModel_InteractionOperand", None)
                    
                    setattr(item, "UMLModel_InteractionOperand", self)
                    

class UMLModel_ComponentRealization(Realization):

    def __init__(self, abstraction: str, realizingClassifier: str, UMLModel_ComponentRealization: "UMLModel_Component" = None):
        self.abstraction = abstraction
        self.realizingClassifier = realizingClassifier
        self.UMLModel_ComponentRealization = UMLModel_ComponentRealization
        
    @property
    def abstraction(self) -> str:
        return self.__abstraction

    @abstraction.setter
    def abstraction(self, abstraction: str):
        self.__abstraction = abstraction

    @property
    def realizingClassifier(self) -> str:
        return self.__realizingClassifier

    @realizingClassifier.setter
    def realizingClassifier(self, realizingClassifier: str):
        self.__realizingClassifier = realizingClassifier

    @property
    def UMLModel_ComponentRealization(self):
        return self.__UMLModel_ComponentRealization

    @UMLModel_ComponentRealization.setter
    def UMLModel_ComponentRealization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_ComponentRealization__UMLModel_ComponentRealization", None)
        self.__UMLModel_ComponentRealization = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_Component84"):
                opp_val = getattr(old_value, "UMLModel_Component84", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_Component84"):
                opp_val = getattr(value, "UMLModel_Component84", None)
                if opp_val is None:
                    setattr(value, "UMLModel_Component84", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class UMLModel_Dependency(DirectedRelationship, PackageableElement):

    def __init__(self, supplier: str, client: str, UMLModel_Dependency: "UMLModel_CollaborationUse" = None):
        self.supplier = supplier
        self.client = client
        self.UMLModel_Dependency = UMLModel_Dependency
        
    @property
    def client(self) -> str:
        return self.__client

    @client.setter
    def client(self, client: str):
        self.__client = client

    @property
    def supplier(self) -> str:
        return self.__supplier

    @supplier.setter
    def supplier(self, supplier: str):
        self.__supplier = supplier

    @property
    def UMLModel_Dependency(self):
        return self.__UMLModel_Dependency

    @UMLModel_Dependency.setter
    def UMLModel_Dependency(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Dependency__UMLModel_Dependency", None)
        self.__UMLModel_Dependency = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_CollaborationUse81"):
                opp_val = getattr(old_value, "UMLModel_CollaborationUse81", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_CollaborationUse81"):
                opp_val = getattr(value, "UMLModel_CollaborationUse81", None)
                if opp_val is None:
                    setattr(value, "UMLModel_CollaborationUse81", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class StructuredClassifier:

    pass
class UMLModel_EncapsulatedClassifier(StructuredClassifier):

    def __init__(self, ownedPort: str):
        self.ownedPort = ownedPort
        
    @property
    def ownedPort(self) -> str:
        return self.__ownedPort

    @ownedPort.setter
    def ownedPort(self, ownedPort: str):
        self.__ownedPort = ownedPort

class StructuralFeatureAction:

    pass
class UMLModel_WriteStructuralFeatureAction(StructuralFeatureAction):

    pass
class UMLModel_ReadStructuralFeatureAction(StructuralFeatureAction):

    pass
class UMLModel_ClearStructuralFeatureAction(StructuralFeatureAction):

    pass
class VariableAction:

    pass
class UMLModel_WriteVariableAction(VariableAction):

    pass
class UMLModel_ReadVariableAction(VariableAction):

    pass
class UMLModel_ClearVariableAction(VariableAction):

    pass
class TemplateParameter:

    pass
class UMLModel_ConnectableElementTemplateParameter(TemplateParameter):

    pass
class UMLModel_OperationTemplateParameter(TemplateParameter):

    pass
class UMLModel_ClassifierTemplateParameter(TemplateParameter):

    def __init__(self, allowSubstitutable: str, defaultClassifier: str, constrainingClassifier: str):
        self.allowSubstitutable = allowSubstitutable
        self.defaultClassifier = defaultClassifier
        self.constrainingClassifier = constrainingClassifier
        
    @property
    def allowSubstitutable(self) -> str:
        return self.__allowSubstitutable

    @allowSubstitutable.setter
    def allowSubstitutable(self, allowSubstitutable: str):
        self.__allowSubstitutable = allowSubstitutable

    @property
    def constrainingClassifier(self) -> str:
        return self.__constrainingClassifier

    @constrainingClassifier.setter
    def constrainingClassifier(self, constrainingClassifier: str):
        self.__constrainingClassifier = constrainingClassifier

    @property
    def defaultClassifier(self) -> str:
        return self.__defaultClassifier

    @defaultClassifier.setter
    def defaultClassifier(self, defaultClassifier: str):
        self.__defaultClassifier = defaultClassifier

class UMLModel_Substitution(Realization):

    def __init__(self, contract: str, substitutingClassifier: str, UMLModel_Substitution: "UMLModel_Classifier" = None):
        self.contract = contract
        self.substitutingClassifier = substitutingClassifier
        self.UMLModel_Substitution = UMLModel_Substitution
        
    @property
    def contract(self) -> str:
        return self.__contract

    @contract.setter
    def contract(self, contract: str):
        self.__contract = contract

    @property
    def substitutingClassifier(self) -> str:
        return self.__substitutingClassifier

    @substitutingClassifier.setter
    def substitutingClassifier(self, substitutingClassifier: str):
        self.__substitutingClassifier = substitutingClassifier

    @property
    def UMLModel_Substitution(self):
        return self.__UMLModel_Substitution

    @UMLModel_Substitution.setter
    def UMLModel_Substitution(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Substitution__UMLModel_Substitution", None)
        self.__UMLModel_Substitution = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_Classifier73"):
                opp_val = getattr(old_value, "UMLModel_Classifier73", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_Classifier73"):
                opp_val = getattr(value, "UMLModel_Classifier73", None)
                if opp_val is None:
                    setattr(value, "UMLModel_Classifier73", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class UMLModel_Generalization(DirectedRelationship):

    def __init__(self, isSubstitutable: str, general: str, generalizationSet: str, specific: str, UMLModel_Generalization: "UMLModel_Classifier" = None):
        self.isSubstitutable = isSubstitutable
        self.general = general
        self.generalizationSet = generalizationSet
        self.specific = specific
        self.UMLModel_Generalization = UMLModel_Generalization
        
    @property
    def generalizationSet(self) -> str:
        return self.__generalizationSet

    @generalizationSet.setter
    def generalizationSet(self, generalizationSet: str):
        self.__generalizationSet = generalizationSet

    @property
    def specific(self) -> str:
        return self.__specific

    @specific.setter
    def specific(self, specific: str):
        self.__specific = specific

    @property
    def isSubstitutable(self) -> str:
        return self.__isSubstitutable

    @isSubstitutable.setter
    def isSubstitutable(self, isSubstitutable: str):
        self.__isSubstitutable = isSubstitutable

    @property
    def general(self) -> str:
        return self.__general

    @general.setter
    def general(self, general: str):
        self.__general = general

    @property
    def UMLModel_Generalization(self):
        return self.__UMLModel_Generalization

    @UMLModel_Generalization.setter
    def UMLModel_Generalization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Generalization__UMLModel_Generalization", None)
        self.__UMLModel_Generalization = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_Classifier71"):
                opp_val = getattr(old_value, "UMLModel_Classifier71", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_Classifier71"):
                opp_val = getattr(value, "UMLModel_Classifier71", None)
                if opp_val is None:
                    setattr(value, "UMLModel_Classifier71", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class TemplateableElement:

    pass
class UMLModel_StringExpression(Expression, TemplateableElement):

    def __init__(self, owningExpression: str, UMLModel_StringExpression: "UMLModel_NamedElement" = None, UMLModel_StringExpression295: "UMLModel_StringExpression" = None, UMLModel_StringExpression293: set["UMLModel_StringExpression"] = None):
        self.owningExpression = owningExpression
        self.UMLModel_StringExpression = UMLModel_StringExpression
        self.UMLModel_StringExpression295 = UMLModel_StringExpression295
        self.UMLModel_StringExpression293 = UMLModel_StringExpression293 if UMLModel_StringExpression293 is not None else set()
        
    @property
    def owningExpression(self) -> str:
        return self.__owningExpression

    @owningExpression.setter
    def owningExpression(self, owningExpression: str):
        self.__owningExpression = owningExpression

    @property
    def UMLModel_StringExpression293(self):
        return self.__UMLModel_StringExpression293

    @UMLModel_StringExpression293.setter
    def UMLModel_StringExpression293(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_StringExpression__UMLModel_StringExpression293", None)
        self.__UMLModel_StringExpression293 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UMLModel_StringExpression295"):
                    opp_val = getattr(item, "UMLModel_StringExpression295", None)
                    
                    if opp_val == self:
                        setattr(item, "UMLModel_StringExpression295", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UMLModel_StringExpression295"):
                    opp_val = getattr(item, "UMLModel_StringExpression295", None)
                    
                    setattr(item, "UMLModel_StringExpression295", self)
                    

    @property
    def UMLModel_StringExpression(self):
        return self.__UMLModel_StringExpression

    @UMLModel_StringExpression.setter
    def UMLModel_StringExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_StringExpression__UMLModel_StringExpression", None)
        self.__UMLModel_StringExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_NamedElement"):
                opp_val = getattr(old_value, "UMLModel_NamedElement", None)
                if opp_val == self:
                    setattr(old_value, "UMLModel_NamedElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_NamedElement"):
                opp_val = getattr(value, "UMLModel_NamedElement", None)
                setattr(value, "UMLModel_NamedElement", self)

    @property
    def UMLModel_StringExpression295(self):
        return self.__UMLModel_StringExpression295

    @UMLModel_StringExpression295.setter
    def UMLModel_StringExpression295(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_StringExpression__UMLModel_StringExpression295", None)
        self.__UMLModel_StringExpression295 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_StringExpression293"):
                opp_val = getattr(old_value, "UMLModel_StringExpression293", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_StringExpression293"):
                opp_val = getattr(value, "UMLModel_StringExpression293", None)
                if opp_val is None:
                    setattr(value, "UMLModel_StringExpression293", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Type:

    pass
class UMLModel_Reception(BehavioralFeature):

    def __init__(self, signal: str, UMLModel_Reception: "UMLModel_Class" = None, UMLModel_Reception129: "UMLModel_Interface" = None):
        self.signal = signal
        self.UMLModel_Reception = UMLModel_Reception
        self.UMLModel_Reception129 = UMLModel_Reception129
        
    @property
    def signal(self) -> str:
        return self.__signal

    @signal.setter
    def signal(self, signal: str):
        self.__signal = signal

    @property
    def UMLModel_Reception(self):
        return self.__UMLModel_Reception

    @UMLModel_Reception.setter
    def UMLModel_Reception(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Reception__UMLModel_Reception", None)
        self.__UMLModel_Reception = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_Class69"):
                opp_val = getattr(old_value, "UMLModel_Class69", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_Class69"):
                opp_val = getattr(value, "UMLModel_Class69", None)
                if opp_val is None:
                    setattr(value, "UMLModel_Class69", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UMLModel_Reception129(self):
        return self.__UMLModel_Reception129

    @UMLModel_Reception129.setter
    def UMLModel_Reception129(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Reception__UMLModel_Reception129", None)
        self.__UMLModel_Reception129 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_Interface128"):
                opp_val = getattr(old_value, "UMLModel_Interface128", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_Interface128"):
                opp_val = getattr(value, "UMLModel_Interface128", None)
                if opp_val is None:
                    setattr(value, "UMLModel_Interface128", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class EncapsulatedClassifier:

    pass
class Event:

    pass
class UMLModel_MessageEvent(Event):

    pass
class UMLModel_TimeEvent(Event):

    def __init__(self, isRelative: str, UMLModel_TimeEvent: "UMLModel_ValueSpecification" = None):
        self.isRelative = isRelative
        self.UMLModel_TimeEvent = UMLModel_TimeEvent
        
    @property
    def isRelative(self) -> str:
        return self.__isRelative

    @isRelative.setter
    def isRelative(self, isRelative: str):
        self.__isRelative = isRelative

    @property
    def UMLModel_TimeEvent(self):
        return self.__UMLModel_TimeEvent

    @UMLModel_TimeEvent.setter
    def UMLModel_TimeEvent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_TimeEvent__UMLModel_TimeEvent", None)
        self.__UMLModel_TimeEvent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_ValueSpecification364"):
                opp_val = getattr(old_value, "UMLModel_ValueSpecification364", None)
                if opp_val == self:
                    setattr(old_value, "UMLModel_ValueSpecification364", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_ValueSpecification364"):
                opp_val = getattr(value, "UMLModel_ValueSpecification364", None)
                setattr(value, "UMLModel_ValueSpecification364", self)

class UMLModel_DestructionEvent(Event):

    pass
class UMLModel_CreationEvent(Event):

    pass
class UMLModel_ExecutionEvent(Event):

    pass
class UMLModel_ChangeEvent(Event):

    pass
class CallAction:

    pass
class UMLModel_CallOperationAction(CallAction):

    def __init__(self, operation: str, UMLModel_CallOperationAction: "UMLModel_InputPin" = None):
        self.operation = operation
        self.UMLModel_CallOperationAction = UMLModel_CallOperationAction
        
    @property
    def operation(self) -> str:
        return self.__operation

    @operation.setter
    def operation(self, operation: str):
        self.__operation = operation

    @property
    def UMLModel_CallOperationAction(self):
        return self.__UMLModel_CallOperationAction

    @UMLModel_CallOperationAction.setter
    def UMLModel_CallOperationAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_CallOperationAction__UMLModel_CallOperationAction", None)
        self.__UMLModel_CallOperationAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_InputPin61"):
                opp_val = getattr(old_value, "UMLModel_InputPin61", None)
                if opp_val == self:
                    setattr(old_value, "UMLModel_InputPin61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_InputPin61"):
                opp_val = getattr(value, "UMLModel_InputPin61", None)
                setattr(value, "UMLModel_InputPin61", self)

class UMLModel_CallBehaviorAction(CallAction):

    def __init__(self, behavior: str):
        self.behavior = behavior
        
    @property
    def behavior(self) -> str:
        return self.__behavior

    @behavior.setter
    def behavior(self, behavior: str):
        self.__behavior = behavior

class InvocationAction:

    pass
class UMLModel_CallAction(InvocationAction):

    def __init__(self, isSynchronous: str, UMLModel_CallAction: set["UMLModel_OutputPin"] = None):
        self.isSynchronous = isSynchronous
        self.UMLModel_CallAction = UMLModel_CallAction if UMLModel_CallAction is not None else set()
        
    @property
    def isSynchronous(self) -> str:
        return self.__isSynchronous

    @isSynchronous.setter
    def isSynchronous(self, isSynchronous: str):
        self.__isSynchronous = isSynchronous

    @property
    def UMLModel_CallAction(self):
        return self.__UMLModel_CallAction

    @UMLModel_CallAction.setter
    def UMLModel_CallAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_CallAction__UMLModel_CallAction", None)
        self.__UMLModel_CallAction = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UMLModel_OutputPin59"):
                    opp_val = getattr(item, "UMLModel_OutputPin59", None)
                    
                    if opp_val == self:
                        setattr(item, "UMLModel_OutputPin59", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UMLModel_OutputPin59"):
                    opp_val = getattr(item, "UMLModel_OutputPin59", None)
                    
                    setattr(item, "UMLModel_OutputPin59", self)
                    

class UMLModel_SendObjectAction(InvocationAction):

    pass
class UMLModel_SendSignalAction(InvocationAction):

    def __init__(self, signal: str, UMLModel_SendSignalAction: "UMLModel_InputPin" = None):
        self.signal = signal
        self.UMLModel_SendSignalAction = UMLModel_SendSignalAction
        
    @property
    def signal(self) -> str:
        return self.__signal

    @signal.setter
    def signal(self, signal: str):
        self.__signal = signal

    @property
    def UMLModel_SendSignalAction(self):
        return self.__UMLModel_SendSignalAction

    @UMLModel_SendSignalAction.setter
    def UMLModel_SendSignalAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_SendSignalAction__UMLModel_SendSignalAction", None)
        self.__UMLModel_SendSignalAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_InputPin278"):
                opp_val = getattr(old_value, "UMLModel_InputPin278", None)
                if opp_val == self:
                    setattr(old_value, "UMLModel_InputPin278", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_InputPin278"):
                opp_val = getattr(value, "UMLModel_InputPin278", None)
                setattr(value, "UMLModel_InputPin278", self)

class UMLModel_BroadcastSignalAction(InvocationAction):

    def __init__(self, signal: str):
        self.signal = signal
        
    @property
    def signal(self) -> str:
        return self.__signal

    @signal.setter
    def signal(self, signal: str):
        self.__signal = signal

class UMLModel_InterfaceRealization(Realization):

    def __init__(self, contract: str, realizingClassifier: str, UMLModel_InterfaceRealization: "UMLModel_BehavioredClassifier" = None):
        self.contract = contract
        self.realizingClassifier = realizingClassifier
        self.UMLModel_InterfaceRealization = UMLModel_InterfaceRealization
        
    @property
    def contract(self) -> str:
        return self.__contract

    @contract.setter
    def contract(self, contract: str):
        self.__contract = contract

    @property
    def realizingClassifier(self) -> str:
        return self.__realizingClassifier

    @realizingClassifier.setter
    def realizingClassifier(self, realizingClassifier: str):
        self.__realizingClassifier = realizingClassifier

    @property
    def UMLModel_InterfaceRealization(self):
        return self.__UMLModel_InterfaceRealization

    @UMLModel_InterfaceRealization.setter
    def UMLModel_InterfaceRealization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_InterfaceRealization__UMLModel_InterfaceRealization", None)
        self.__UMLModel_InterfaceRealization = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_BehavioredClassifier54"):
                opp_val = getattr(old_value, "UMLModel_BehavioredClassifier54", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_BehavioredClassifier54"):
                opp_val = getattr(value, "UMLModel_BehavioredClassifier54", None)
                if opp_val is None:
                    setattr(value, "UMLModel_BehavioredClassifier54", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Feature:

    pass
class UMLModel_Connector(Feature):

    def __init__(self, redefinedConnector: str, kind: str, contract: str, type: str, UMLModel_Connector: set["UMLModel_ConnectorEnd"] = None, UMLModel_Connector338: "UMLModel_StructuredClassifier" = None):
        self.redefinedConnector = redefinedConnector
        self.kind = kind
        self.contract = contract
        self.type = type
        self.UMLModel_Connector = UMLModel_Connector if UMLModel_Connector is not None else set()
        self.UMLModel_Connector338 = UMLModel_Connector338
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def contract(self) -> str:
        return self.__contract

    @contract.setter
    def contract(self, contract: str):
        self.__contract = contract

    @property
    def redefinedConnector(self) -> str:
        return self.__redefinedConnector

    @redefinedConnector.setter
    def redefinedConnector(self, redefinedConnector: str):
        self.__redefinedConnector = redefinedConnector

    @property
    def UMLModel_Connector(self):
        return self.__UMLModel_Connector

    @UMLModel_Connector.setter
    def UMLModel_Connector(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Connector__UMLModel_Connector", None)
        self.__UMLModel_Connector = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UMLModel_ConnectorEnd"):
                    opp_val = getattr(item, "UMLModel_ConnectorEnd", None)
                    
                    if opp_val == self:
                        setattr(item, "UMLModel_ConnectorEnd", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UMLModel_ConnectorEnd"):
                    opp_val = getattr(item, "UMLModel_ConnectorEnd", None)
                    
                    setattr(item, "UMLModel_ConnectorEnd", self)
                    

    @property
    def UMLModel_Connector338(self):
        return self.__UMLModel_Connector338

    @UMLModel_Connector338.setter
    def UMLModel_Connector338(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Connector__UMLModel_Connector338", None)
        self.__UMLModel_Connector338 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_StructuredClassifier337"):
                opp_val = getattr(old_value, "UMLModel_StructuredClassifier337", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_StructuredClassifier337"):
                opp_val = getattr(value, "UMLModel_StructuredClassifier337", None)
                if opp_val is None:
                    setattr(value, "UMLModel_StructuredClassifier337", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class UMLModel_StructuralFeature(TypedElement, Feature, MultiplicityElement):

    def __init__(self, isReadOnly: str):
        self.isReadOnly = isReadOnly
        
    @property
    def isReadOnly(self) -> str:
        return self.__isReadOnly

    @isReadOnly.setter
    def isReadOnly(self, isReadOnly: str):
        self.__isReadOnly = isReadOnly

class Namespace:

    pass
class UMLModel_Package(PackageableElement, Namespace, TemplateableElement):

    def __init__(self, ownedType: str, nestedPackage: str, nestingPackage: str, UMLModel_Package: set["UMLModel_PackageMerge"] = None, UMLModel_Package213: set["UMLModel_PackageableElement"] = None, UMLModel_Package216: set["UMLModel_ProfileApplication"] = None):
        self.ownedType = ownedType
        self.nestedPackage = nestedPackage
        self.nestingPackage = nestingPackage
        self.UMLModel_Package = UMLModel_Package if UMLModel_Package is not None else set()
        self.UMLModel_Package213 = UMLModel_Package213 if UMLModel_Package213 is not None else set()
        self.UMLModel_Package216 = UMLModel_Package216 if UMLModel_Package216 is not None else set()
        
    @property
    def nestingPackage(self) -> str:
        return self.__nestingPackage

    @nestingPackage.setter
    def nestingPackage(self, nestingPackage: str):
        self.__nestingPackage = nestingPackage

    @property
    def ownedType(self) -> str:
        return self.__ownedType

    @ownedType.setter
    def ownedType(self, ownedType: str):
        self.__ownedType = ownedType

    @property
    def nestedPackage(self) -> str:
        return self.__nestedPackage

    @nestedPackage.setter
    def nestedPackage(self, nestedPackage: str):
        self.__nestedPackage = nestedPackage

    @property
    def UMLModel_Package(self):
        return self.__UMLModel_Package

    @UMLModel_Package.setter
    def UMLModel_Package(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Package__UMLModel_Package", None)
        self.__UMLModel_Package = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UMLModel_PackageMerge"):
                    opp_val = getattr(item, "UMLModel_PackageMerge", None)
                    
                    if opp_val == self:
                        setattr(item, "UMLModel_PackageMerge", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UMLModel_PackageMerge"):
                    opp_val = getattr(item, "UMLModel_PackageMerge", None)
                    
                    setattr(item, "UMLModel_PackageMerge", self)
                    

    @property
    def UMLModel_Package216(self):
        return self.__UMLModel_Package216

    @UMLModel_Package216.setter
    def UMLModel_Package216(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Package__UMLModel_Package216", None)
        self.__UMLModel_Package216 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UMLModel_ProfileApplication"):
                    opp_val = getattr(item, "UMLModel_ProfileApplication", None)
                    
                    if opp_val == self:
                        setattr(item, "UMLModel_ProfileApplication", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UMLModel_ProfileApplication"):
                    opp_val = getattr(item, "UMLModel_ProfileApplication", None)
                    
                    setattr(item, "UMLModel_ProfileApplication", self)
                    

    @property
    def UMLModel_Package213(self):
        return self.__UMLModel_Package213

    @UMLModel_Package213.setter
    def UMLModel_Package213(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Package__UMLModel_Package213", None)
        self.__UMLModel_Package213 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UMLModel_PackageableElement214"):
                    opp_val = getattr(item, "UMLModel_PackageableElement214", None)
                    
                    if opp_val == self:
                        setattr(item, "UMLModel_PackageableElement214", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UMLModel_PackageableElement214"):
                    opp_val = getattr(item, "UMLModel_PackageableElement214", None)
                    
                    setattr(item, "UMLModel_PackageableElement214", self)
                    

class UMLModel_InteractionOperand(Namespace, InteractionFragment):

    pass
class UMLModel_BehavioralFeature(Namespace, Feature):

    def __init__(self, isAbstract: str, concurrency: str, raisedException: str, method: str, UMLModel_BehavioralFeature: set["UMLModel_Parameter"] = None, UMLModel_BehavioralFeature49: set["UMLModel_ParameterSet"] = None):
        self.isAbstract = isAbstract
        self.concurrency = concurrency
        self.raisedException = raisedException
        self.method = method
        self.UMLModel_BehavioralFeature = UMLModel_BehavioralFeature if UMLModel_BehavioralFeature is not None else set()
        self.UMLModel_BehavioralFeature49 = UMLModel_BehavioralFeature49 if UMLModel_BehavioralFeature49 is not None else set()
        
    @property
    def isAbstract(self) -> str:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: str):
        self.__isAbstract = isAbstract

    @property
    def method(self) -> str:
        return self.__method

    @method.setter
    def method(self, method: str):
        self.__method = method

    @property
    def raisedException(self) -> str:
        return self.__raisedException

    @raisedException.setter
    def raisedException(self, raisedException: str):
        self.__raisedException = raisedException

    @property
    def concurrency(self) -> str:
        return self.__concurrency

    @concurrency.setter
    def concurrency(self, concurrency: str):
        self.__concurrency = concurrency

    @property
    def UMLModel_BehavioralFeature49(self):
        return self.__UMLModel_BehavioralFeature49

    @UMLModel_BehavioralFeature49.setter
    def UMLModel_BehavioralFeature49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_BehavioralFeature__UMLModel_BehavioralFeature49", None)
        self.__UMLModel_BehavioralFeature49 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UMLModel_ParameterSet50"):
                    opp_val = getattr(item, "UMLModel_ParameterSet50", None)
                    
                    if opp_val == self:
                        setattr(item, "UMLModel_ParameterSet50", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UMLModel_ParameterSet50"):
                    opp_val = getattr(item, "UMLModel_ParameterSet50", None)
                    
                    setattr(item, "UMLModel_ParameterSet50", self)
                    

    @property
    def UMLModel_BehavioralFeature(self):
        return self.__UMLModel_BehavioralFeature

    @UMLModel_BehavioralFeature.setter
    def UMLModel_BehavioralFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_BehavioralFeature__UMLModel_BehavioralFeature", None)
        self.__UMLModel_BehavioralFeature = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UMLModel_Parameter47"):
                    opp_val = getattr(item, "UMLModel_Parameter47", None)
                    
                    if opp_val == self:
                        setattr(item, "UMLModel_Parameter47", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UMLModel_Parameter47"):
                    opp_val = getattr(item, "UMLModel_Parameter47", None)
                    
                    setattr(item, "UMLModel_Parameter47", self)
                    

class UMLModel_Parameter(MultiplicityElement, ConnectableElement):

    def __init__(self, parameterSet: str, operation: str, direction: str, default: str, isException: str, isStream: str, effect: str, UMLModel_Parameter: "UMLModel_Behavior" = None, UMLModel_Parameter47: "UMLModel_BehavioralFeature" = None, UMLModel_Parameter209: "UMLModel_ValueSpecification" = None):
        self.parameterSet = parameterSet
        self.operation = operation
        self.direction = direction
        self.default = default
        self.isException = isException
        self.isStream = isStream
        self.effect = effect
        self.UMLModel_Parameter = UMLModel_Parameter
        self.UMLModel_Parameter47 = UMLModel_Parameter47
        self.UMLModel_Parameter209 = UMLModel_Parameter209
        
    @property
    def operation(self) -> str:
        return self.__operation

    @operation.setter
    def operation(self, operation: str):
        self.__operation = operation

    @property
    def default(self) -> str:
        return self.__default

    @default.setter
    def default(self, default: str):
        self.__default = default

    @property
    def isException(self) -> str:
        return self.__isException

    @isException.setter
    def isException(self, isException: str):
        self.__isException = isException

    @property
    def isStream(self) -> str:
        return self.__isStream

    @isStream.setter
    def isStream(self, isStream: str):
        self.__isStream = isStream

    @property
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction

    @property
    def parameterSet(self) -> str:
        return self.__parameterSet

    @parameterSet.setter
    def parameterSet(self, parameterSet: str):
        self.__parameterSet = parameterSet

    @property
    def effect(self) -> str:
        return self.__effect

    @effect.setter
    def effect(self, effect: str):
        self.__effect = effect

    @property
    def UMLModel_Parameter47(self):
        return self.__UMLModel_Parameter47

    @UMLModel_Parameter47.setter
    def UMLModel_Parameter47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Parameter__UMLModel_Parameter47", None)
        self.__UMLModel_Parameter47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_BehavioralFeature"):
                opp_val = getattr(old_value, "UMLModel_BehavioralFeature", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_BehavioralFeature"):
                opp_val = getattr(value, "UMLModel_BehavioralFeature", None)
                if opp_val is None:
                    setattr(value, "UMLModel_BehavioralFeature", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UMLModel_Parameter(self):
        return self.__UMLModel_Parameter

    @UMLModel_Parameter.setter
    def UMLModel_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Parameter__UMLModel_Parameter", None)
        self.__UMLModel_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_Behavior"):
                opp_val = getattr(old_value, "UMLModel_Behavior", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_Behavior"):
                opp_val = getattr(value, "UMLModel_Behavior", None)
                if opp_val is None:
                    setattr(value, "UMLModel_Behavior", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UMLModel_Parameter209(self):
        return self.__UMLModel_Parameter209

    @UMLModel_Parameter209.setter
    def UMLModel_Parameter209(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Parameter__UMLModel_Parameter209", None)
        self.__UMLModel_Parameter209 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_ValueSpecification210"):
                opp_val = getattr(old_value, "UMLModel_ValueSpecification210", None)
                if opp_val == self:
                    setattr(old_value, "UMLModel_ValueSpecification210", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_ValueSpecification210"):
                opp_val = getattr(value, "UMLModel_ValueSpecification210", None)
                setattr(value, "UMLModel_ValueSpecification210", self)

class Association:

    pass
class UMLModel_CommunicationPath(Association):

    pass
class UMLModel_Extension(Association):

    def __init__(self, isRequired: str, metaClass: str):
        self.isRequired = isRequired
        self.metaClass = metaClass
        
    @property
    def metaClass(self) -> str:
        return self.__metaClass

    @metaClass.setter
    def metaClass(self, metaClass: str):
        self.__metaClass = metaClass

    @property
    def isRequired(self) -> str:
        return self.__isRequired

    @isRequired.setter
    def isRequired(self, isRequired: str):
        self.__isRequired = isRequired

class Class:

    pass
class UMLModel_Stereotype(Class):

    pass
class UMLModel_Behavior(Class):

    def __init__(self, isReentrant: str, redefinedBahavior: str, specification: str, context: str, postcondition: str, precondition: str, UMLModel_Behavior: set["UMLModel_Parameter"] = None, UMLModel_Behavior45: set["UMLModel_ParameterSet"] = None, UMLModel_Behavior52: "UMLModel_BehavioredClassifier" = None, UMLModel_Behavior322: "UMLModel_State" = None, UMLModel_Behavior316: "UMLModel_State" = None, UMLModel_Behavior319: "UMLModel_State" = None, UMLModel_Behavior367: "UMLModel_Transition" = None):
        self.isReentrant = isReentrant
        self.redefinedBahavior = redefinedBahavior
        self.specification = specification
        self.context = context
        self.postcondition = postcondition
        self.precondition = precondition
        self.UMLModel_Behavior = UMLModel_Behavior if UMLModel_Behavior is not None else set()
        self.UMLModel_Behavior45 = UMLModel_Behavior45 if UMLModel_Behavior45 is not None else set()
        self.UMLModel_Behavior52 = UMLModel_Behavior52
        self.UMLModel_Behavior322 = UMLModel_Behavior322
        self.UMLModel_Behavior316 = UMLModel_Behavior316
        self.UMLModel_Behavior319 = UMLModel_Behavior319
        self.UMLModel_Behavior367 = UMLModel_Behavior367
        
    @property
    def redefinedBahavior(self) -> str:
        return self.__redefinedBahavior

    @redefinedBahavior.setter
    def redefinedBahavior(self, redefinedBahavior: str):
        self.__redefinedBahavior = redefinedBahavior

    @property
    def specification(self) -> str:
        return self.__specification

    @specification.setter
    def specification(self, specification: str):
        self.__specification = specification

    @property
    def precondition(self) -> str:
        return self.__precondition

    @precondition.setter
    def precondition(self, precondition: str):
        self.__precondition = precondition

    @property
    def isReentrant(self) -> str:
        return self.__isReentrant

    @isReentrant.setter
    def isReentrant(self, isReentrant: str):
        self.__isReentrant = isReentrant

    @property
    def context(self) -> str:
        return self.__context

    @context.setter
    def context(self, context: str):
        self.__context = context

    @property
    def postcondition(self) -> str:
        return self.__postcondition

    @postcondition.setter
    def postcondition(self, postcondition: str):
        self.__postcondition = postcondition

    @property
    def UMLModel_Behavior322(self):
        return self.__UMLModel_Behavior322

    @UMLModel_Behavior322.setter
    def UMLModel_Behavior322(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Behavior__UMLModel_Behavior322", None)
        self.__UMLModel_Behavior322 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_State321"):
                opp_val = getattr(old_value, "UMLModel_State321", None)
                if opp_val == self:
                    setattr(old_value, "UMLModel_State321", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_State321"):
                opp_val = getattr(value, "UMLModel_State321", None)
                setattr(value, "UMLModel_State321", self)

    @property
    def UMLModel_Behavior45(self):
        return self.__UMLModel_Behavior45

    @UMLModel_Behavior45.setter
    def UMLModel_Behavior45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Behavior__UMLModel_Behavior45", None)
        self.__UMLModel_Behavior45 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UMLModel_ParameterSet"):
                    opp_val = getattr(item, "UMLModel_ParameterSet", None)
                    
                    if opp_val == self:
                        setattr(item, "UMLModel_ParameterSet", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UMLModel_ParameterSet"):
                    opp_val = getattr(item, "UMLModel_ParameterSet", None)
                    
                    setattr(item, "UMLModel_ParameterSet", self)
                    

    @property
    def UMLModel_Behavior319(self):
        return self.__UMLModel_Behavior319

    @UMLModel_Behavior319.setter
    def UMLModel_Behavior319(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Behavior__UMLModel_Behavior319", None)
        self.__UMLModel_Behavior319 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_State318"):
                opp_val = getattr(old_value, "UMLModel_State318", None)
                if opp_val == self:
                    setattr(old_value, "UMLModel_State318", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_State318"):
                opp_val = getattr(value, "UMLModel_State318", None)
                setattr(value, "UMLModel_State318", self)

    @property
    def UMLModel_Behavior316(self):
        return self.__UMLModel_Behavior316

    @UMLModel_Behavior316.setter
    def UMLModel_Behavior316(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Behavior__UMLModel_Behavior316", None)
        self.__UMLModel_Behavior316 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_State315"):
                opp_val = getattr(old_value, "UMLModel_State315", None)
                if opp_val == self:
                    setattr(old_value, "UMLModel_State315", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_State315"):
                opp_val = getattr(value, "UMLModel_State315", None)
                setattr(value, "UMLModel_State315", self)

    @property
    def UMLModel_Behavior(self):
        return self.__UMLModel_Behavior

    @UMLModel_Behavior.setter
    def UMLModel_Behavior(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Behavior__UMLModel_Behavior", None)
        self.__UMLModel_Behavior = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UMLModel_Parameter"):
                    opp_val = getattr(item, "UMLModel_Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "UMLModel_Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UMLModel_Parameter"):
                    opp_val = getattr(item, "UMLModel_Parameter", None)
                    
                    setattr(item, "UMLModel_Parameter", self)
                    

    @property
    def UMLModel_Behavior52(self):
        return self.__UMLModel_Behavior52

    @UMLModel_Behavior52.setter
    def UMLModel_Behavior52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Behavior__UMLModel_Behavior52", None)
        self.__UMLModel_Behavior52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_BehavioredClassifier"):
                opp_val = getattr(old_value, "UMLModel_BehavioredClassifier", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_BehavioredClassifier"):
                opp_val = getattr(value, "UMLModel_BehavioredClassifier", None)
                if opp_val is None:
                    setattr(value, "UMLModel_BehavioredClassifier", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UMLModel_Behavior367(self):
        return self.__UMLModel_Behavior367

    @UMLModel_Behavior367.setter
    def UMLModel_Behavior367(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Behavior__UMLModel_Behavior367", None)
        self.__UMLModel_Behavior367 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_Transition366"):
                opp_val = getattr(old_value, "UMLModel_Transition366", None)
                if opp_val == self:
                    setattr(old_value, "UMLModel_Transition366", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_Transition366"):
                opp_val = getattr(value, "UMLModel_Transition366", None)
                setattr(value, "UMLModel_Transition366", self)

class UMLModel_Node(Class, DeploymentTarget):

    pass
class UMLModel_Component(Class):

    def __init__(self, indirectlyInstantiated: str, required: str, provided: str, UMLModel_Component: set["UMLModel_PackageableElement"] = None, UMLModel_Component84: set["UMLModel_ComponentRealization"] = None):
        self.indirectlyInstantiated = indirectlyInstantiated
        self.required = required
        self.provided = provided
        self.UMLModel_Component = UMLModel_Component if UMLModel_Component is not None else set()
        self.UMLModel_Component84 = UMLModel_Component84 if UMLModel_Component84 is not None else set()
        
    @property
    def required(self) -> str:
        return self.__required

    @required.setter
    def required(self, required: str):
        self.__required = required

    @property
    def provided(self) -> str:
        return self.__provided

    @provided.setter
    def provided(self, provided: str):
        self.__provided = provided

    @property
    def indirectlyInstantiated(self) -> str:
        return self.__indirectlyInstantiated

    @indirectlyInstantiated.setter
    def indirectlyInstantiated(self, indirectlyInstantiated: str):
        self.__indirectlyInstantiated = indirectlyInstantiated

    @property
    def UMLModel_Component(self):
        return self.__UMLModel_Component

    @UMLModel_Component.setter
    def UMLModel_Component(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Component__UMLModel_Component", None)
        self.__UMLModel_Component = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UMLModel_PackageableElement"):
                    opp_val = getattr(item, "UMLModel_PackageableElement", None)
                    
                    if opp_val == self:
                        setattr(item, "UMLModel_PackageableElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UMLModel_PackageableElement"):
                    opp_val = getattr(item, "UMLModel_PackageableElement", None)
                    
                    setattr(item, "UMLModel_PackageableElement", self)
                    

    @property
    def UMLModel_Component84(self):
        return self.__UMLModel_Component84

    @UMLModel_Component84.setter
    def UMLModel_Component84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Component__UMLModel_Component84", None)
        self.__UMLModel_Component84 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UMLModel_ComponentRealization"):
                    opp_val = getattr(item, "UMLModel_ComponentRealization", None)
                    
                    if opp_val == self:
                        setattr(item, "UMLModel_ComponentRealization", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UMLModel_ComponentRealization"):
                    opp_val = getattr(item, "UMLModel_ComponentRealization", None)
                    
                    setattr(item, "UMLModel_ComponentRealization", self)
                    

class UMLModel_AssociationClass(Association, Class):

    pass
class ActivityGroup:

    pass
class UMLModel_InterruptibleActivityRegion(ActivityGroup):

    def __init__(self, interruptingEdge: str, node: str):
        self.interruptingEdge = interruptingEdge
        self.node = node
        
    @property
    def node(self) -> str:
        return self.__node

    @node.setter
    def node(self, node: str):
        self.__node = node

    @property
    def interruptingEdge(self) -> str:
        return self.__interruptingEdge

    @interruptingEdge.setter
    def interruptingEdge(self, interruptingEdge: str):
        self.__interruptingEdge = interruptingEdge

class NamedElement:

    pass
class UMLModel_CollaborationUse(NamedElement):

    def __init__(self, type: str, UMLModel_CollaborationUse81: set["UMLModel_Dependency"] = None, UMLModel_CollaborationUse: "UMLModel_Classifier" = None):
        self.type = type
        self.UMLModel_CollaborationUse81 = UMLModel_CollaborationUse81 if UMLModel_CollaborationUse81 is not None else set()
        self.UMLModel_CollaborationUse = UMLModel_CollaborationUse
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def UMLModel_CollaborationUse81(self):
        return self.__UMLModel_CollaborationUse81

    @UMLModel_CollaborationUse81.setter
    def UMLModel_CollaborationUse81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_CollaborationUse__UMLModel_CollaborationUse81", None)
        self.__UMLModel_CollaborationUse81 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UMLModel_Dependency"):
                    opp_val = getattr(item, "UMLModel_Dependency", None)
                    
                    if opp_val == self:
                        setattr(item, "UMLModel_Dependency", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UMLModel_Dependency"):
                    opp_val = getattr(item, "UMLModel_Dependency", None)
                    
                    setattr(item, "UMLModel_Dependency", self)
                    

    @property
    def UMLModel_CollaborationUse(self):
        return self.__UMLModel_CollaborationUse

    @UMLModel_CollaborationUse.setter
    def UMLModel_CollaborationUse(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_CollaborationUse__UMLModel_CollaborationUse", None)
        self.__UMLModel_CollaborationUse = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_Classifier75"):
                opp_val = getattr(old_value, "UMLModel_Classifier75", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_Classifier75"):
                opp_val = getattr(value, "UMLModel_Classifier75", None)
                if opp_val is None:
                    setattr(value, "UMLModel_Classifier75", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class UMLModel_MessageEnd(NamedElement):

    def __init__(self, message: str):
        self.message = message
        
    @property
    def message(self) -> str:
        return self.__message

    @message.setter
    def message(self, message: str):
        self.__message = message

class UMLModel_Namespace(NamedElement):

    def __init__(self, member: str, importedMember: str, ownedMember: str, UMLModel_Namespace: set["UMLModel_ElementImport"] = None, UMLModel_Namespace195: set["UMLModel_PackageImport"] = None, UMLModel_Namespace197: set["UMLModel_Constraint"] = None):
        self.member = member
        self.importedMember = importedMember
        self.ownedMember = ownedMember
        self.UMLModel_Namespace = UMLModel_Namespace if UMLModel_Namespace is not None else set()
        self.UMLModel_Namespace195 = UMLModel_Namespace195 if UMLModel_Namespace195 is not None else set()
        self.UMLModel_Namespace197 = UMLModel_Namespace197 if UMLModel_Namespace197 is not None else set()
        
    @property
    def member(self) -> str:
        return self.__member

    @member.setter
    def member(self, member: str):
        self.__member = member

    @property
    def importedMember(self) -> str:
        return self.__importedMember

    @importedMember.setter
    def importedMember(self, importedMember: str):
        self.__importedMember = importedMember

    @property
    def ownedMember(self) -> str:
        return self.__ownedMember

    @ownedMember.setter
    def ownedMember(self, ownedMember: str):
        self.__ownedMember = ownedMember

    @property
    def UMLModel_Namespace197(self):
        return self.__UMLModel_Namespace197

    @UMLModel_Namespace197.setter
    def UMLModel_Namespace197(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Namespace__UMLModel_Namespace197", None)
        self.__UMLModel_Namespace197 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UMLModel_Constraint198"):
                    opp_val = getattr(item, "UMLModel_Constraint198", None)
                    
                    if opp_val == self:
                        setattr(item, "UMLModel_Constraint198", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UMLModel_Constraint198"):
                    opp_val = getattr(item, "UMLModel_Constraint198", None)
                    
                    setattr(item, "UMLModel_Constraint198", self)
                    

    @property
    def UMLModel_Namespace195(self):
        return self.__UMLModel_Namespace195

    @UMLModel_Namespace195.setter
    def UMLModel_Namespace195(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Namespace__UMLModel_Namespace195", None)
        self.__UMLModel_Namespace195 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UMLModel_PackageImport"):
                    opp_val = getattr(item, "UMLModel_PackageImport", None)
                    
                    if opp_val == self:
                        setattr(item, "UMLModel_PackageImport", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UMLModel_PackageImport"):
                    opp_val = getattr(item, "UMLModel_PackageImport", None)
                    
                    setattr(item, "UMLModel_PackageImport", self)
                    

    @property
    def UMLModel_Namespace(self):
        return self.__UMLModel_Namespace

    @UMLModel_Namespace.setter
    def UMLModel_Namespace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Namespace__UMLModel_Namespace", None)
        self.__UMLModel_Namespace = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UMLModel_ElementImport193"):
                    opp_val = getattr(item, "UMLModel_ElementImport193", None)
                    
                    if opp_val == self:
                        setattr(item, "UMLModel_ElementImport193", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UMLModel_ElementImport193"):
                    opp_val = getattr(item, "UMLModel_ElementImport193", None)
                    
                    setattr(item, "UMLModel_ElementImport193", self)
                    

class UMLModel_Include(DirectedRelationship, NamedElement):

    def __init__(self, addition: str, includingCase: str, UMLModel_Include: "UMLModel_UseCase" = None):
        self.addition = addition
        self.includingCase = includingCase
        self.UMLModel_Include = UMLModel_Include
        
    @property
    def includingCase(self) -> str:
        return self.__includingCase

    @includingCase.setter
    def includingCase(self, includingCase: str):
        self.__includingCase = includingCase

    @property
    def addition(self) -> str:
        return self.__addition

    @addition.setter
    def addition(self, addition: str):
        self.__addition = addition

    @property
    def UMLModel_Include(self):
        return self.__UMLModel_Include

    @UMLModel_Include.setter
    def UMLModel_Include(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Include__UMLModel_Include", None)
        self.__UMLModel_Include = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_UseCase377"):
                opp_val = getattr(old_value, "UMLModel_UseCase377", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_UseCase377"):
                opp_val = getattr(value, "UMLModel_UseCase377", None)
                if opp_val is None:
                    setattr(value, "UMLModel_UseCase377", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class UMLModel_DeploymentTarget(NamedElement):

    def __init__(self, deployedElement: str, UMLModel_DeploymentTarget: set["UMLModel_Deployment"] = None):
        self.deployedElement = deployedElement
        self.UMLModel_DeploymentTarget = UMLModel_DeploymentTarget if UMLModel_DeploymentTarget is not None else set()
        
    @property
    def deployedElement(self) -> str:
        return self.__deployedElement

    @deployedElement.setter
    def deployedElement(self, deployedElement: str):
        self.__deployedElement = deployedElement

    @property
    def UMLModel_DeploymentTarget(self):
        return self.__UMLModel_DeploymentTarget

    @UMLModel_DeploymentTarget.setter
    def UMLModel_DeploymentTarget(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_DeploymentTarget__UMLModel_DeploymentTarget", None)
        self.__UMLModel_DeploymentTarget = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UMLModel_Deployment"):
                    opp_val = getattr(item, "UMLModel_Deployment", None)
                    
                    if opp_val == self:
                        setattr(item, "UMLModel_Deployment", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UMLModel_Deployment"):
                    opp_val = getattr(item, "UMLModel_Deployment", None)
                    
                    setattr(item, "UMLModel_Deployment", self)
                    

class UMLModel_RedefinableElement(NamedElement):

    def __init__(self, isLeaf: str, redefinedElement: str, redefinitionContext: str):
        self.isLeaf = isLeaf
        self.redefinedElement = redefinedElement
        self.redefinitionContext = redefinitionContext
        
    @property
    def redefinedElement(self) -> str:
        return self.__redefinedElement

    @redefinedElement.setter
    def redefinedElement(self, redefinedElement: str):
        self.__redefinedElement = redefinedElement

    @property
    def isLeaf(self) -> str:
        return self.__isLeaf

    @isLeaf.setter
    def isLeaf(self, isLeaf: str):
        self.__isLeaf = isLeaf

    @property
    def redefinitionContext(self) -> str:
        return self.__redefinitionContext

    @redefinitionContext.setter
    def redefinitionContext(self, redefinitionContext: str):
        self.__redefinitionContext = redefinitionContext

class UMLModel_InteractionFragment(NamedElement):

    def __init__(self, enclosingInteraction: str, enclosingOperand: str, covered: str, UMLModel_InteractionFragment160: "UMLModel_InteractionOperand" = None, UMLModel_InteractionFragment: "UMLModel_Interaction" = None, UMLModel_InteractionFragment150: set["UMLModel_GeneralOrdering"] = None):
        self.enclosingInteraction = enclosingInteraction
        self.enclosingOperand = enclosingOperand
        self.covered = covered
        self.UMLModel_InteractionFragment160 = UMLModel_InteractionFragment160
        self.UMLModel_InteractionFragment = UMLModel_InteractionFragment
        self.UMLModel_InteractionFragment150 = UMLModel_InteractionFragment150 if UMLModel_InteractionFragment150 is not None else set()
        
    @property
    def enclosingInteraction(self) -> str:
        return self.__enclosingInteraction

    @enclosingInteraction.setter
    def enclosingInteraction(self, enclosingInteraction: str):
        self.__enclosingInteraction = enclosingInteraction

    @property
    def enclosingOperand(self) -> str:
        return self.__enclosingOperand

    @enclosingOperand.setter
    def enclosingOperand(self, enclosingOperand: str):
        self.__enclosingOperand = enclosingOperand

    @property
    def covered(self) -> str:
        return self.__covered

    @covered.setter
    def covered(self, covered: str):
        self.__covered = covered

    @property
    def UMLModel_InteractionFragment160(self):
        return self.__UMLModel_InteractionFragment160

    @UMLModel_InteractionFragment160.setter
    def UMLModel_InteractionFragment160(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_InteractionFragment__UMLModel_InteractionFragment160", None)
        self.__UMLModel_InteractionFragment160 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_InteractionOperand159"):
                opp_val = getattr(old_value, "UMLModel_InteractionOperand159", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_InteractionOperand159"):
                opp_val = getattr(value, "UMLModel_InteractionOperand159", None)
                if opp_val is None:
                    setattr(value, "UMLModel_InteractionOperand159", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UMLModel_InteractionFragment(self):
        return self.__UMLModel_InteractionFragment

    @UMLModel_InteractionFragment.setter
    def UMLModel_InteractionFragment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_InteractionFragment__UMLModel_InteractionFragment", None)
        self.__UMLModel_InteractionFragment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_Interaction140"):
                opp_val = getattr(old_value, "UMLModel_Interaction140", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_Interaction140"):
                opp_val = getattr(value, "UMLModel_Interaction140", None)
                if opp_val is None:
                    setattr(value, "UMLModel_Interaction140", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UMLModel_InteractionFragment150(self):
        return self.__UMLModel_InteractionFragment150

    @UMLModel_InteractionFragment150.setter
    def UMLModel_InteractionFragment150(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_InteractionFragment__UMLModel_InteractionFragment150", None)
        self.__UMLModel_InteractionFragment150 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UMLModel_GeneralOrdering"):
                    opp_val = getattr(item, "UMLModel_GeneralOrdering", None)
                    
                    if opp_val == self:
                        setattr(item, "UMLModel_GeneralOrdering", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UMLModel_GeneralOrdering"):
                    opp_val = getattr(item, "UMLModel_GeneralOrdering", None)
                    
                    setattr(item, "UMLModel_GeneralOrdering", self)
                    

class UMLModel_Vertex(NamedElement):

    def __init__(self, incoming: str, outgoing: str, container: str, UMLModel_Vertex: "UMLModel_Region" = None):
        self.incoming = incoming
        self.outgoing = outgoing
        self.container = container
        self.UMLModel_Vertex = UMLModel_Vertex
        
    @property
    def incoming(self) -> str:
        return self.__incoming

    @incoming.setter
    def incoming(self, incoming: str):
        self.__incoming = incoming

    @property
    def container(self) -> str:
        return self.__container

    @container.setter
    def container(self, container: str):
        self.__container = container

    @property
    def outgoing(self) -> str:
        return self.__outgoing

    @outgoing.setter
    def outgoing(self, outgoing: str):
        self.__outgoing = outgoing

    @property
    def UMLModel_Vertex(self):
        return self.__UMLModel_Vertex

    @UMLModel_Vertex.setter
    def UMLModel_Vertex(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Vertex__UMLModel_Vertex", None)
        self.__UMLModel_Vertex = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_Region"):
                opp_val = getattr(old_value, "UMLModel_Region", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_Region"):
                opp_val = getattr(value, "UMLModel_Region", None)
                if opp_val is None:
                    setattr(value, "UMLModel_Region", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class UMLModel_ParameterSet(NamedElement):

    def __init__(self, parameter: str, UMLModel_ParameterSet: "UMLModel_Behavior" = None, UMLModel_ParameterSet50: "UMLModel_BehavioralFeature" = None, UMLModel_ParameterSet221: set["UMLModel_Constraint"] = None):
        self.parameter = parameter
        self.UMLModel_ParameterSet = UMLModel_ParameterSet
        self.UMLModel_ParameterSet50 = UMLModel_ParameterSet50
        self.UMLModel_ParameterSet221 = UMLModel_ParameterSet221 if UMLModel_ParameterSet221 is not None else set()
        
    @property
    def parameter(self) -> str:
        return self.__parameter

    @parameter.setter
    def parameter(self, parameter: str):
        self.__parameter = parameter

    @property
    def UMLModel_ParameterSet221(self):
        return self.__UMLModel_ParameterSet221

    @UMLModel_ParameterSet221.setter
    def UMLModel_ParameterSet221(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_ParameterSet__UMLModel_ParameterSet221", None)
        self.__UMLModel_ParameterSet221 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UMLModel_Constraint222"):
                    opp_val = getattr(item, "UMLModel_Constraint222", None)
                    
                    if opp_val == self:
                        setattr(item, "UMLModel_Constraint222", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UMLModel_Constraint222"):
                    opp_val = getattr(item, "UMLModel_Constraint222", None)
                    
                    setattr(item, "UMLModel_Constraint222", self)
                    

    @property
    def UMLModel_ParameterSet(self):
        return self.__UMLModel_ParameterSet

    @UMLModel_ParameterSet.setter
    def UMLModel_ParameterSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_ParameterSet__UMLModel_ParameterSet", None)
        self.__UMLModel_ParameterSet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_Behavior45"):
                opp_val = getattr(old_value, "UMLModel_Behavior45", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_Behavior45"):
                opp_val = getattr(value, "UMLModel_Behavior45", None)
                if opp_val is None:
                    setattr(value, "UMLModel_Behavior45", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UMLModel_ParameterSet50(self):
        return self.__UMLModel_ParameterSet50

    @UMLModel_ParameterSet50.setter
    def UMLModel_ParameterSet50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_ParameterSet__UMLModel_ParameterSet50", None)
        self.__UMLModel_ParameterSet50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_BehavioralFeature49"):
                opp_val = getattr(old_value, "UMLModel_BehavioralFeature49", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_BehavioralFeature49"):
                opp_val = getattr(value, "UMLModel_BehavioralFeature49", None)
                if opp_val is None:
                    setattr(value, "UMLModel_BehavioralFeature49", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class UMLModel_Lifeline(NamedElement):

    def __init__(self, represents: str, interaction: str, decomposedAs: str, coveredBy: str, UMLModel_Lifeline: "UMLModel_Interaction" = None, UMLModel_Lifeline170: "UMLModel_ValueSpecification" = None):
        self.represents = represents
        self.interaction = interaction
        self.decomposedAs = decomposedAs
        self.coveredBy = coveredBy
        self.UMLModel_Lifeline = UMLModel_Lifeline
        self.UMLModel_Lifeline170 = UMLModel_Lifeline170
        
    @property
    def coveredBy(self) -> str:
        return self.__coveredBy

    @coveredBy.setter
    def coveredBy(self, coveredBy: str):
        self.__coveredBy = coveredBy

    @property
    def decomposedAs(self) -> str:
        return self.__decomposedAs

    @decomposedAs.setter
    def decomposedAs(self, decomposedAs: str):
        self.__decomposedAs = decomposedAs

    @property
    def interaction(self) -> str:
        return self.__interaction

    @interaction.setter
    def interaction(self, interaction: str):
        self.__interaction = interaction

    @property
    def represents(self) -> str:
        return self.__represents

    @represents.setter
    def represents(self, represents: str):
        self.__represents = represents

    @property
    def UMLModel_Lifeline(self):
        return self.__UMLModel_Lifeline

    @UMLModel_Lifeline.setter
    def UMLModel_Lifeline(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Lifeline__UMLModel_Lifeline", None)
        self.__UMLModel_Lifeline = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_Interaction"):
                opp_val = getattr(old_value, "UMLModel_Interaction", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_Interaction"):
                opp_val = getattr(value, "UMLModel_Interaction", None)
                if opp_val is None:
                    setattr(value, "UMLModel_Interaction", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UMLModel_Lifeline170(self):
        return self.__UMLModel_Lifeline170

    @UMLModel_Lifeline170.setter
    def UMLModel_Lifeline170(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Lifeline__UMLModel_Lifeline170", None)
        self.__UMLModel_Lifeline170 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_ValueSpecification171"):
                opp_val = getattr(old_value, "UMLModel_ValueSpecification171", None)
                if opp_val == self:
                    setattr(old_value, "UMLModel_ValueSpecification171", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_ValueSpecification171"):
                opp_val = getattr(value, "UMLModel_ValueSpecification171", None)
                setattr(value, "UMLModel_ValueSpecification171", self)

class UMLModel_TypedElement(NamedElement):

    def __init__(self, type: str):
        self.type = type
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class UMLModel_Message(NamedElement):

    def __init__(self, messageKind: str, signature: str, messageSort: str, receiveEvent: str, sendEvent: str, connector: str, interaction: str, UMLModel_Message: "UMLModel_Interaction" = None, UMLModel_Message184: set["UMLModel_ValueSpecification"] = None):
        self.messageKind = messageKind
        self.signature = signature
        self.messageSort = messageSort
        self.receiveEvent = receiveEvent
        self.sendEvent = sendEvent
        self.connector = connector
        self.interaction = interaction
        self.UMLModel_Message = UMLModel_Message
        self.UMLModel_Message184 = UMLModel_Message184 if UMLModel_Message184 is not None else set()
        
    @property
    def connector(self) -> str:
        return self.__connector

    @connector.setter
    def connector(self, connector: str):
        self.__connector = connector

    @property
    def interaction(self) -> str:
        return self.__interaction

    @interaction.setter
    def interaction(self, interaction: str):
        self.__interaction = interaction

    @property
    def sendEvent(self) -> str:
        return self.__sendEvent

    @sendEvent.setter
    def sendEvent(self, sendEvent: str):
        self.__sendEvent = sendEvent

    @property
    def messageKind(self) -> str:
        return self.__messageKind

    @messageKind.setter
    def messageKind(self, messageKind: str):
        self.__messageKind = messageKind

    @property
    def signature(self) -> str:
        return self.__signature

    @signature.setter
    def signature(self, signature: str):
        self.__signature = signature

    @property
    def receiveEvent(self) -> str:
        return self.__receiveEvent

    @receiveEvent.setter
    def receiveEvent(self, receiveEvent: str):
        self.__receiveEvent = receiveEvent

    @property
    def messageSort(self) -> str:
        return self.__messageSort

    @messageSort.setter
    def messageSort(self, messageSort: str):
        self.__messageSort = messageSort

    @property
    def UMLModel_Message184(self):
        return self.__UMLModel_Message184

    @UMLModel_Message184.setter
    def UMLModel_Message184(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Message__UMLModel_Message184", None)
        self.__UMLModel_Message184 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UMLModel_ValueSpecification185"):
                    opp_val = getattr(item, "UMLModel_ValueSpecification185", None)
                    
                    if opp_val == self:
                        setattr(item, "UMLModel_ValueSpecification185", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UMLModel_ValueSpecification185"):
                    opp_val = getattr(item, "UMLModel_ValueSpecification185", None)
                    
                    setattr(item, "UMLModel_ValueSpecification185", self)
                    

    @property
    def UMLModel_Message(self):
        return self.__UMLModel_Message

    @UMLModel_Message.setter
    def UMLModel_Message(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Message__UMLModel_Message", None)
        self.__UMLModel_Message = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_Interaction148"):
                opp_val = getattr(old_value, "UMLModel_Interaction148", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_Interaction148"):
                opp_val = getattr(value, "UMLModel_Interaction148", None)
                if opp_val is None:
                    setattr(value, "UMLModel_Interaction148", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class UMLModel_Extend(DirectedRelationship, NamedElement):

    def __init__(self, extendedCase: str, extensionLocation: str, extension: str, UMLModel_Extend: "UMLModel_Constraint" = None, UMLModel_Extend380: "UMLModel_UseCase" = None):
        self.extendedCase = extendedCase
        self.extensionLocation = extensionLocation
        self.extension = extension
        self.UMLModel_Extend = UMLModel_Extend
        self.UMLModel_Extend380 = UMLModel_Extend380
        
    @property
    def extensionLocation(self) -> str:
        return self.__extensionLocation

    @extensionLocation.setter
    def extensionLocation(self, extensionLocation: str):
        self.__extensionLocation = extensionLocation

    @property
    def extension(self) -> str:
        return self.__extension

    @extension.setter
    def extension(self, extension: str):
        self.__extension = extension

    @property
    def extendedCase(self) -> str:
        return self.__extendedCase

    @extendedCase.setter
    def extendedCase(self, extendedCase: str):
        self.__extendedCase = extendedCase

    @property
    def UMLModel_Extend380(self):
        return self.__UMLModel_Extend380

    @UMLModel_Extend380.setter
    def UMLModel_Extend380(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Extend__UMLModel_Extend380", None)
        self.__UMLModel_Extend380 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_UseCase379"):
                opp_val = getattr(old_value, "UMLModel_UseCase379", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_UseCase379"):
                opp_val = getattr(value, "UMLModel_UseCase379", None)
                if opp_val is None:
                    setattr(value, "UMLModel_UseCase379", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UMLModel_Extend(self):
        return self.__UMLModel_Extend

    @UMLModel_Extend.setter
    def UMLModel_Extend(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Extend__UMLModel_Extend", None)
        self.__UMLModel_Extend = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_Constraint116"):
                opp_val = getattr(old_value, "UMLModel_Constraint116", None)
                if opp_val == self:
                    setattr(old_value, "UMLModel_Constraint116", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_Constraint116"):
                opp_val = getattr(value, "UMLModel_Constraint116", None)
                setattr(value, "UMLModel_Constraint116", self)

class UMLModel_DeployedArtifact(NamedElement):

    pass
class UMLModel_PackageableElement(NamedElement, ParameterableElement):

    pass
class UMLModel_GeneralOrdering(NamedElement):

    def __init__(self, before: str, after: str, UMLModel_GeneralOrdering: "UMLModel_InteractionFragment" = None):
        self.before = before
        self.after = after
        self.UMLModel_GeneralOrdering = UMLModel_GeneralOrdering
        
    @property
    def before(self) -> str:
        return self.__before

    @before.setter
    def before(self, before: str):
        self.__before = before

    @property
    def after(self) -> str:
        return self.__after

    @after.setter
    def after(self, after: str):
        self.__after = after

    @property
    def UMLModel_GeneralOrdering(self):
        return self.__UMLModel_GeneralOrdering

    @UMLModel_GeneralOrdering.setter
    def UMLModel_GeneralOrdering(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_GeneralOrdering__UMLModel_GeneralOrdering", None)
        self.__UMLModel_GeneralOrdering = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_InteractionFragment150"):
                opp_val = getattr(old_value, "UMLModel_InteractionFragment150", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_InteractionFragment150"):
                opp_val = getattr(value, "UMLModel_InteractionFragment150", None)
                if opp_val is None:
                    setattr(value, "UMLModel_InteractionFragment150", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class UMLModel_ActivityPartition(ActivityGroup, NamedElement):

    def __init__(self, isDimension: str, isExternal: str, edge: str, represents: str, superPartition: str, node: str, subpartition: str):
        self.isDimension = isDimension
        self.isExternal = isExternal
        self.edge = edge
        self.represents = represents
        self.superPartition = superPartition
        self.node = node
        self.subpartition = subpartition
        
    @property
    def superPartition(self) -> str:
        return self.__superPartition

    @superPartition.setter
    def superPartition(self, superPartition: str):
        self.__superPartition = superPartition

    @property
    def isExternal(self) -> str:
        return self.__isExternal

    @isExternal.setter
    def isExternal(self, isExternal: str):
        self.__isExternal = isExternal

    @property
    def isDimension(self) -> str:
        return self.__isDimension

    @isDimension.setter
    def isDimension(self, isDimension: str):
        self.__isDimension = isDimension

    @property
    def edge(self) -> str:
        return self.__edge

    @edge.setter
    def edge(self, edge: str):
        self.__edge = edge

    @property
    def node(self) -> str:
        return self.__node

    @node.setter
    def node(self, node: str):
        self.__node = node

    @property
    def subpartition(self) -> str:
        return self.__subpartition

    @subpartition.setter
    def subpartition(self, subpartition: str):
        self.__subpartition = subpartition

    @property
    def represents(self) -> str:
        return self.__represents

    @represents.setter
    def represents(self, represents: str):
        self.__represents = represents

class Relationship:

    pass
class UMLModel_DirectedRelationship(Relationship):

    def __init__(self, source: str, target: str):
        self.source = source
        self.target = target
        
    @property
    def target(self) -> str:
        return self.__target

    @target.setter
    def target(self, target: str):
        self.__target = target

    @property
    def source(self) -> str:
        return self.__source

    @source.setter
    def source(self, source: str):
        self.__source = source

class UMLModel_Property(DeploymentTarget, ConnectableElement, TemplateableElement, StructuralFeature):

    def __init__(self, isComposite: str, redefinedProperty: str, owningAssociation: str, opposite: str, subsettedProperty: str, association: str, associationEnd: str, class: str, datatype: str, isDerived: str, isDerivedUnion: str, default: str, aggregation: str, UMLModel_Property: "UMLModel_Artifact" = None, UMLModel_Property42: "UMLModel_Association" = None, UMLModel_Property101: "UMLModel_DataType" = None, UMLModel_Property120: "UMLModel_Interface" = None, UMLModel_Property224: "UMLModel_ValueSpecification" = None, UMLModel_Property228: "UMLModel_Property" = None, UMLModel_Property226: set["UMLModel_Property"] = None, UMLModel_Property307: "UMLModel_Signal" = None, UMLModel_Property335: "UMLModel_StructuredClassifier" = None):
        self.isComposite = isComposite
        self.redefinedProperty = redefinedProperty
        self.owningAssociation = owningAssociation
        self.opposite = opposite
        self.subsettedProperty = subsettedProperty
        self.association = association
        self.associationEnd = associationEnd
        self.class = class
        self.datatype = datatype
        self.isDerived = isDerived
        self.isDerivedUnion = isDerivedUnion
        self.default = default
        self.aggregation = aggregation
        self.UMLModel_Property = UMLModel_Property
        self.UMLModel_Property42 = UMLModel_Property42
        self.UMLModel_Property101 = UMLModel_Property101
        self.UMLModel_Property120 = UMLModel_Property120
        self.UMLModel_Property224 = UMLModel_Property224
        self.UMLModel_Property228 = UMLModel_Property228
        self.UMLModel_Property226 = UMLModel_Property226 if UMLModel_Property226 is not None else set()
        self.UMLModel_Property307 = UMLModel_Property307
        self.UMLModel_Property335 = UMLModel_Property335
        
    @property
    def opposite(self) -> str:
        return self.__opposite

    @opposite.setter
    def opposite(self, opposite: str):
        self.__opposite = opposite

    @property
    def isComposite(self) -> str:
        return self.__isComposite

    @isComposite.setter
    def isComposite(self, isComposite: str):
        self.__isComposite = isComposite

    @property
    def associationEnd(self) -> str:
        return self.__associationEnd

    @associationEnd.setter
    def associationEnd(self, associationEnd: str):
        self.__associationEnd = associationEnd

    @property
    def redefinedProperty(self) -> str:
        return self.__redefinedProperty

    @redefinedProperty.setter
    def redefinedProperty(self, redefinedProperty: str):
        self.__redefinedProperty = redefinedProperty

    @property
    def association(self) -> str:
        return self.__association

    @association.setter
    def association(self, association: str):
        self.__association = association

    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def datatype(self) -> str:
        return self.__datatype

    @datatype.setter
    def datatype(self, datatype: str):
        self.__datatype = datatype

    @property
    def aggregation(self) -> str:
        return self.__aggregation

    @aggregation.setter
    def aggregation(self, aggregation: str):
        self.__aggregation = aggregation

    @property
    def owningAssociation(self) -> str:
        return self.__owningAssociation

    @owningAssociation.setter
    def owningAssociation(self, owningAssociation: str):
        self.__owningAssociation = owningAssociation

    @property
    def default(self) -> str:
        return self.__default

    @default.setter
    def default(self, default: str):
        self.__default = default

    @property
    def subsettedProperty(self) -> str:
        return self.__subsettedProperty

    @subsettedProperty.setter
    def subsettedProperty(self, subsettedProperty: str):
        self.__subsettedProperty = subsettedProperty

    @property
    def isDerived(self) -> str:
        return self.__isDerived

    @isDerived.setter
    def isDerived(self, isDerived: str):
        self.__isDerived = isDerived

    @property
    def isDerivedUnion(self) -> str:
        return self.__isDerivedUnion

    @isDerivedUnion.setter
    def isDerivedUnion(self, isDerivedUnion: str):
        self.__isDerivedUnion = isDerivedUnion

    @property
    def UMLModel_Property42(self):
        return self.__UMLModel_Property42

    @UMLModel_Property42.setter
    def UMLModel_Property42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Property__UMLModel_Property42", None)
        self.__UMLModel_Property42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_Association"):
                opp_val = getattr(old_value, "UMLModel_Association", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_Association"):
                opp_val = getattr(value, "UMLModel_Association", None)
                if opp_val is None:
                    setattr(value, "UMLModel_Association", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UMLModel_Property307(self):
        return self.__UMLModel_Property307

    @UMLModel_Property307.setter
    def UMLModel_Property307(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Property__UMLModel_Property307", None)
        self.__UMLModel_Property307 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_Signal"):
                opp_val = getattr(old_value, "UMLModel_Signal", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_Signal"):
                opp_val = getattr(value, "UMLModel_Signal", None)
                if opp_val is None:
                    setattr(value, "UMLModel_Signal", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UMLModel_Property228(self):
        return self.__UMLModel_Property228

    @UMLModel_Property228.setter
    def UMLModel_Property228(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Property__UMLModel_Property228", None)
        self.__UMLModel_Property228 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_Property226"):
                opp_val = getattr(old_value, "UMLModel_Property226", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_Property226"):
                opp_val = getattr(value, "UMLModel_Property226", None)
                if opp_val is None:
                    setattr(value, "UMLModel_Property226", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UMLModel_Property120(self):
        return self.__UMLModel_Property120

    @UMLModel_Property120.setter
    def UMLModel_Property120(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Property__UMLModel_Property120", None)
        self.__UMLModel_Property120 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_Interface"):
                opp_val = getattr(old_value, "UMLModel_Interface", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_Interface"):
                opp_val = getattr(value, "UMLModel_Interface", None)
                if opp_val is None:
                    setattr(value, "UMLModel_Interface", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UMLModel_Property101(self):
        return self.__UMLModel_Property101

    @UMLModel_Property101.setter
    def UMLModel_Property101(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Property__UMLModel_Property101", None)
        self.__UMLModel_Property101 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_DataType"):
                opp_val = getattr(old_value, "UMLModel_DataType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_DataType"):
                opp_val = getattr(value, "UMLModel_DataType", None)
                if opp_val is None:
                    setattr(value, "UMLModel_DataType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UMLModel_Property224(self):
        return self.__UMLModel_Property224

    @UMLModel_Property224.setter
    def UMLModel_Property224(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Property__UMLModel_Property224", None)
        self.__UMLModel_Property224 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_ValueSpecification225"):
                opp_val = getattr(old_value, "UMLModel_ValueSpecification225", None)
                if opp_val == self:
                    setattr(old_value, "UMLModel_ValueSpecification225", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_ValueSpecification225"):
                opp_val = getattr(value, "UMLModel_ValueSpecification225", None)
                setattr(value, "UMLModel_ValueSpecification225", self)

    @property
    def UMLModel_Property(self):
        return self.__UMLModel_Property

    @UMLModel_Property.setter
    def UMLModel_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Property__UMLModel_Property", None)
        self.__UMLModel_Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_Artifact40"):
                opp_val = getattr(old_value, "UMLModel_Artifact40", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_Artifact40"):
                opp_val = getattr(value, "UMLModel_Artifact40", None)
                if opp_val is None:
                    setattr(value, "UMLModel_Artifact40", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UMLModel_Property335(self):
        return self.__UMLModel_Property335

    @UMLModel_Property335.setter
    def UMLModel_Property335(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Property__UMLModel_Property335", None)
        self.__UMLModel_Property335 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_StructuredClassifier"):
                opp_val = getattr(old_value, "UMLModel_StructuredClassifier", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_StructuredClassifier"):
                opp_val = getattr(value, "UMLModel_StructuredClassifier", None)
                if opp_val is None:
                    setattr(value, "UMLModel_StructuredClassifier", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UMLModel_Property226(self):
        return self.__UMLModel_Property226

    @UMLModel_Property226.setter
    def UMLModel_Property226(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Property__UMLModel_Property226", None)
        self.__UMLModel_Property226 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UMLModel_Property228"):
                    opp_val = getattr(item, "UMLModel_Property228", None)
                    
                    if opp_val == self:
                        setattr(item, "UMLModel_Property228", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UMLModel_Property228"):
                    opp_val = getattr(item, "UMLModel_Property228", None)
                    
                    setattr(item, "UMLModel_Property228", self)
                    

class UMLModel_Operation(ParameterableElement, BehavioralFeature, TemplateableElement):

    def __init__(self, interface: str, class: str, isQuery: str, isOrdered: str, isUnique: str, lower: str, upper: str, precondition: str, postcondition: str, redefinedOperation: str, datatype: str, bodyCondition: str, type: str, UMLModel_Operation: "UMLModel_Artifact" = None, UMLModel_Operation67: "UMLModel_Class" = None, UMLModel_Operation104: "UMLModel_DataType" = None, UMLModel_Operation123: "UMLModel_Interface" = None):
        self.interface = interface
        self.class = class
        self.isQuery = isQuery
        self.isOrdered = isOrdered
        self.isUnique = isUnique
        self.lower = lower
        self.upper = upper
        self.precondition = precondition
        self.postcondition = postcondition
        self.redefinedOperation = redefinedOperation
        self.datatype = datatype
        self.bodyCondition = bodyCondition
        self.type = type
        self.UMLModel_Operation = UMLModel_Operation
        self.UMLModel_Operation67 = UMLModel_Operation67
        self.UMLModel_Operation104 = UMLModel_Operation104
        self.UMLModel_Operation123 = UMLModel_Operation123
        
    @property
    def isQuery(self) -> str:
        return self.__isQuery

    @isQuery.setter
    def isQuery(self, isQuery: str):
        self.__isQuery = isQuery

    @property
    def isUnique(self) -> str:
        return self.__isUnique

    @isUnique.setter
    def isUnique(self, isUnique: str):
        self.__isUnique = isUnique

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def interface(self) -> str:
        return self.__interface

    @interface.setter
    def interface(self, interface: str):
        self.__interface = interface

    @property
    def postcondition(self) -> str:
        return self.__postcondition

    @postcondition.setter
    def postcondition(self, postcondition: str):
        self.__postcondition = postcondition

    @property
    def redefinedOperation(self) -> str:
        return self.__redefinedOperation

    @redefinedOperation.setter
    def redefinedOperation(self, redefinedOperation: str):
        self.__redefinedOperation = redefinedOperation

    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def isOrdered(self) -> str:
        return self.__isOrdered

    @isOrdered.setter
    def isOrdered(self, isOrdered: str):
        self.__isOrdered = isOrdered

    @property
    def datatype(self) -> str:
        return self.__datatype

    @datatype.setter
    def datatype(self, datatype: str):
        self.__datatype = datatype

    @property
    def lower(self) -> str:
        return self.__lower

    @lower.setter
    def lower(self, lower: str):
        self.__lower = lower

    @property
    def bodyCondition(self) -> str:
        return self.__bodyCondition

    @bodyCondition.setter
    def bodyCondition(self, bodyCondition: str):
        self.__bodyCondition = bodyCondition

    @property
    def precondition(self) -> str:
        return self.__precondition

    @precondition.setter
    def precondition(self, precondition: str):
        self.__precondition = precondition

    @property
    def upper(self) -> str:
        return self.__upper

    @upper.setter
    def upper(self, upper: str):
        self.__upper = upper

    @property
    def UMLModel_Operation104(self):
        return self.__UMLModel_Operation104

    @UMLModel_Operation104.setter
    def UMLModel_Operation104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Operation__UMLModel_Operation104", None)
        self.__UMLModel_Operation104 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_DataType103"):
                opp_val = getattr(old_value, "UMLModel_DataType103", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_DataType103"):
                opp_val = getattr(value, "UMLModel_DataType103", None)
                if opp_val is None:
                    setattr(value, "UMLModel_DataType103", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UMLModel_Operation(self):
        return self.__UMLModel_Operation

    @UMLModel_Operation.setter
    def UMLModel_Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Operation__UMLModel_Operation", None)
        self.__UMLModel_Operation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_Artifact38"):
                opp_val = getattr(old_value, "UMLModel_Artifact38", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_Artifact38"):
                opp_val = getattr(value, "UMLModel_Artifact38", None)
                if opp_val is None:
                    setattr(value, "UMLModel_Artifact38", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UMLModel_Operation67(self):
        return self.__UMLModel_Operation67

    @UMLModel_Operation67.setter
    def UMLModel_Operation67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Operation__UMLModel_Operation67", None)
        self.__UMLModel_Operation67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_Class66"):
                opp_val = getattr(old_value, "UMLModel_Class66", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_Class66"):
                opp_val = getattr(value, "UMLModel_Class66", None)
                if opp_val is None:
                    setattr(value, "UMLModel_Class66", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UMLModel_Operation123(self):
        return self.__UMLModel_Operation123

    @UMLModel_Operation123.setter
    def UMLModel_Operation123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Operation__UMLModel_Operation123", None)
        self.__UMLModel_Operation123 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_Interface122"):
                opp_val = getattr(old_value, "UMLModel_Interface122", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_Interface122"):
                opp_val = getattr(value, "UMLModel_Interface122", None)
                if opp_val is None:
                    setattr(value, "UMLModel_Interface122", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class UMLModel_Manifestation(Abstraction):

    def __init__(self, utilizedElement: str, UMLModel_Manifestation: "UMLModel_Artifact" = None):
        self.utilizedElement = utilizedElement
        self.UMLModel_Manifestation = UMLModel_Manifestation
        
    @property
    def utilizedElement(self) -> str:
        return self.__utilizedElement

    @utilizedElement.setter
    def utilizedElement(self, utilizedElement: str):
        self.__utilizedElement = utilizedElement

    @property
    def UMLModel_Manifestation(self):
        return self.__UMLModel_Manifestation

    @UMLModel_Manifestation.setter
    def UMLModel_Manifestation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Manifestation__UMLModel_Manifestation", None)
        self.__UMLModel_Manifestation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_Artifact36"):
                opp_val = getattr(old_value, "UMLModel_Artifact36", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_Artifact36"):
                opp_val = getattr(value, "UMLModel_Artifact36", None)
                if opp_val is None:
                    setattr(value, "UMLModel_Artifact36", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class DeployedArtifact:

    pass
class UMLModel_InstanceSpecification(PackageableElement, DeployedArtifact, DeploymentTarget):

    def __init__(self, classifier: str, UMLModel_InstanceSpecification: set["UMLModel_Slot"] = None, UMLModel_InstanceSpecification134: "UMLModel_ValueSpecification" = None):
        self.classifier = classifier
        self.UMLModel_InstanceSpecification = UMLModel_InstanceSpecification if UMLModel_InstanceSpecification is not None else set()
        self.UMLModel_InstanceSpecification134 = UMLModel_InstanceSpecification134
        
    @property
    def classifier(self) -> str:
        return self.__classifier

    @classifier.setter
    def classifier(self, classifier: str):
        self.__classifier = classifier

    @property
    def UMLModel_InstanceSpecification134(self):
        return self.__UMLModel_InstanceSpecification134

    @UMLModel_InstanceSpecification134.setter
    def UMLModel_InstanceSpecification134(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_InstanceSpecification__UMLModel_InstanceSpecification134", None)
        self.__UMLModel_InstanceSpecification134 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_ValueSpecification135"):
                opp_val = getattr(old_value, "UMLModel_ValueSpecification135", None)
                if opp_val == self:
                    setattr(old_value, "UMLModel_ValueSpecification135", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_ValueSpecification135"):
                opp_val = getattr(value, "UMLModel_ValueSpecification135", None)
                setattr(value, "UMLModel_ValueSpecification135", self)

    @property
    def UMLModel_InstanceSpecification(self):
        return self.__UMLModel_InstanceSpecification

    @UMLModel_InstanceSpecification.setter
    def UMLModel_InstanceSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_InstanceSpecification__UMLModel_InstanceSpecification", None)
        self.__UMLModel_InstanceSpecification = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UMLModel_Slot"):
                    opp_val = getattr(item, "UMLModel_Slot", None)
                    
                    if opp_val == self:
                        setattr(item, "UMLModel_Slot", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UMLModel_Slot"):
                    opp_val = getattr(item, "UMLModel_Slot", None)
                    
                    setattr(item, "UMLModel_Slot", self)
                    

class Classifier:

    pass
class UMLModel_StructuredClassifier(Classifier):

    def __init__(self, part: str, role: str, UMLModel_StructuredClassifier: set["UMLModel_Property"] = None, UMLModel_StructuredClassifier337: set["UMLModel_Connector"] = None):
        self.part = part
        self.role = role
        self.UMLModel_StructuredClassifier = UMLModel_StructuredClassifier if UMLModel_StructuredClassifier is not None else set()
        self.UMLModel_StructuredClassifier337 = UMLModel_StructuredClassifier337 if UMLModel_StructuredClassifier337 is not None else set()
        
    @property
    def role(self) -> str:
        return self.__role

    @role.setter
    def role(self, role: str):
        self.__role = role

    @property
    def part(self) -> str:
        return self.__part

    @part.setter
    def part(self, part: str):
        self.__part = part

    @property
    def UMLModel_StructuredClassifier337(self):
        return self.__UMLModel_StructuredClassifier337

    @UMLModel_StructuredClassifier337.setter
    def UMLModel_StructuredClassifier337(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_StructuredClassifier__UMLModel_StructuredClassifier337", None)
        self.__UMLModel_StructuredClassifier337 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UMLModel_Connector338"):
                    opp_val = getattr(item, "UMLModel_Connector338", None)
                    
                    if opp_val == self:
                        setattr(item, "UMLModel_Connector338", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UMLModel_Connector338"):
                    opp_val = getattr(item, "UMLModel_Connector338", None)
                    
                    setattr(item, "UMLModel_Connector338", self)
                    

    @property
    def UMLModel_StructuredClassifier(self):
        return self.__UMLModel_StructuredClassifier

    @UMLModel_StructuredClassifier.setter
    def UMLModel_StructuredClassifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_StructuredClassifier__UMLModel_StructuredClassifier", None)
        self.__UMLModel_StructuredClassifier = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UMLModel_Property335"):
                    opp_val = getattr(item, "UMLModel_Property335", None)
                    
                    if opp_val == self:
                        setattr(item, "UMLModel_Property335", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UMLModel_Property335"):
                    opp_val = getattr(item, "UMLModel_Property335", None)
                    
                    setattr(item, "UMLModel_Property335", self)
                    

class UMLModel_BehavioredClassifier(Classifier):

    def __init__(self, classifierBehavior: str, UMLModel_BehavioredClassifier: set["UMLModel_Behavior"] = None, UMLModel_BehavioredClassifier54: set["UMLModel_InterfaceRealization"] = None, UMLModel_BehavioredClassifier56: set["UMLModel_Trigger"] = None):
        self.classifierBehavior = classifierBehavior
        self.UMLModel_BehavioredClassifier = UMLModel_BehavioredClassifier if UMLModel_BehavioredClassifier is not None else set()
        self.UMLModel_BehavioredClassifier54 = UMLModel_BehavioredClassifier54 if UMLModel_BehavioredClassifier54 is not None else set()
        self.UMLModel_BehavioredClassifier56 = UMLModel_BehavioredClassifier56 if UMLModel_BehavioredClassifier56 is not None else set()
        
    @property
    def classifierBehavior(self) -> str:
        return self.__classifierBehavior

    @classifierBehavior.setter
    def classifierBehavior(self, classifierBehavior: str):
        self.__classifierBehavior = classifierBehavior

    @property
    def UMLModel_BehavioredClassifier54(self):
        return self.__UMLModel_BehavioredClassifier54

    @UMLModel_BehavioredClassifier54.setter
    def UMLModel_BehavioredClassifier54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_BehavioredClassifier__UMLModel_BehavioredClassifier54", None)
        self.__UMLModel_BehavioredClassifier54 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UMLModel_InterfaceRealization"):
                    opp_val = getattr(item, "UMLModel_InterfaceRealization", None)
                    
                    if opp_val == self:
                        setattr(item, "UMLModel_InterfaceRealization", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UMLModel_InterfaceRealization"):
                    opp_val = getattr(item, "UMLModel_InterfaceRealization", None)
                    
                    setattr(item, "UMLModel_InterfaceRealization", self)
                    

    @property
    def UMLModel_BehavioredClassifier(self):
        return self.__UMLModel_BehavioredClassifier

    @UMLModel_BehavioredClassifier.setter
    def UMLModel_BehavioredClassifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_BehavioredClassifier__UMLModel_BehavioredClassifier", None)
        self.__UMLModel_BehavioredClassifier = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UMLModel_Behavior52"):
                    opp_val = getattr(item, "UMLModel_Behavior52", None)
                    
                    if opp_val == self:
                        setattr(item, "UMLModel_Behavior52", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UMLModel_Behavior52"):
                    opp_val = getattr(item, "UMLModel_Behavior52", None)
                    
                    setattr(item, "UMLModel_Behavior52", self)
                    

    @property
    def UMLModel_BehavioredClassifier56(self):
        return self.__UMLModel_BehavioredClassifier56

    @UMLModel_BehavioredClassifier56.setter
    def UMLModel_BehavioredClassifier56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_BehavioredClassifier__UMLModel_BehavioredClassifier56", None)
        self.__UMLModel_BehavioredClassifier56 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UMLModel_Trigger57"):
                    opp_val = getattr(item, "UMLModel_Trigger57", None)
                    
                    if opp_val == self:
                        setattr(item, "UMLModel_Trigger57", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UMLModel_Trigger57"):
                    opp_val = getattr(item, "UMLModel_Trigger57", None)
                    
                    setattr(item, "UMLModel_Trigger57", self)
                    

class UMLModel_Signal(Classifier):

    pass
class UMLModel_Interface(Classifier):

    def __init__(self, redefinedInterface: str, isActive: bool, UMLModel_Interface: set["UMLModel_Property"] = None, UMLModel_Interface122: set["UMLModel_Operation"] = None, UMLModel_Interface125: set["UMLModel_Classifier"] = None, UMLModel_Interface128: set["UMLModel_Reception"] = None, UMLModel_Interface131: "UMLModel_ProtocolStateMachine" = None):
        self.redefinedInterface = redefinedInterface
        self.isActive = isActive
        self.UMLModel_Interface = UMLModel_Interface if UMLModel_Interface is not None else set()
        self.UMLModel_Interface122 = UMLModel_Interface122 if UMLModel_Interface122 is not None else set()
        self.UMLModel_Interface125 = UMLModel_Interface125 if UMLModel_Interface125 is not None else set()
        self.UMLModel_Interface128 = UMLModel_Interface128 if UMLModel_Interface128 is not None else set()
        self.UMLModel_Interface131 = UMLModel_Interface131
        
    @property
    def isActive(self) -> bool:
        return self.__isActive

    @isActive.setter
    def isActive(self, isActive: bool):
        self.__isActive = isActive

    @property
    def redefinedInterface(self) -> str:
        return self.__redefinedInterface

    @redefinedInterface.setter
    def redefinedInterface(self, redefinedInterface: str):
        self.__redefinedInterface = redefinedInterface

    @property
    def UMLModel_Interface131(self):
        return self.__UMLModel_Interface131

    @UMLModel_Interface131.setter
    def UMLModel_Interface131(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Interface__UMLModel_Interface131", None)
        self.__UMLModel_Interface131 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_ProtocolStateMachine"):
                opp_val = getattr(old_value, "UMLModel_ProtocolStateMachine", None)
                if opp_val == self:
                    setattr(old_value, "UMLModel_ProtocolStateMachine", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_ProtocolStateMachine"):
                opp_val = getattr(value, "UMLModel_ProtocolStateMachine", None)
                setattr(value, "UMLModel_ProtocolStateMachine", self)

    @property
    def UMLModel_Interface125(self):
        return self.__UMLModel_Interface125

    @UMLModel_Interface125.setter
    def UMLModel_Interface125(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Interface__UMLModel_Interface125", None)
        self.__UMLModel_Interface125 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UMLModel_Classifier126"):
                    opp_val = getattr(item, "UMLModel_Classifier126", None)
                    
                    if opp_val == self:
                        setattr(item, "UMLModel_Classifier126", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UMLModel_Classifier126"):
                    opp_val = getattr(item, "UMLModel_Classifier126", None)
                    
                    setattr(item, "UMLModel_Classifier126", self)
                    

    @property
    def UMLModel_Interface(self):
        return self.__UMLModel_Interface

    @UMLModel_Interface.setter
    def UMLModel_Interface(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Interface__UMLModel_Interface", None)
        self.__UMLModel_Interface = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UMLModel_Property120"):
                    opp_val = getattr(item, "UMLModel_Property120", None)
                    
                    if opp_val == self:
                        setattr(item, "UMLModel_Property120", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UMLModel_Property120"):
                    opp_val = getattr(item, "UMLModel_Property120", None)
                    
                    setattr(item, "UMLModel_Property120", self)
                    

    @property
    def UMLModel_Interface128(self):
        return self.__UMLModel_Interface128

    @UMLModel_Interface128.setter
    def UMLModel_Interface128(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Interface__UMLModel_Interface128", None)
        self.__UMLModel_Interface128 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UMLModel_Reception129"):
                    opp_val = getattr(item, "UMLModel_Reception129", None)
                    
                    if opp_val == self:
                        setattr(item, "UMLModel_Reception129", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UMLModel_Reception129"):
                    opp_val = getattr(item, "UMLModel_Reception129", None)
                    
                    setattr(item, "UMLModel_Reception129", self)
                    

    @property
    def UMLModel_Interface122(self):
        return self.__UMLModel_Interface122

    @UMLModel_Interface122.setter
    def UMLModel_Interface122(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Interface__UMLModel_Interface122", None)
        self.__UMLModel_Interface122 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UMLModel_Operation123"):
                    opp_val = getattr(item, "UMLModel_Operation123", None)
                    
                    if opp_val == self:
                        setattr(item, "UMLModel_Operation123", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UMLModel_Operation123"):
                    opp_val = getattr(item, "UMLModel_Operation123", None)
                    
                    setattr(item, "UMLModel_Operation123", self)
                    

class UMLModel_Association(Classifier, Relationship):

    def __init__(self, isDerived: str, endType: str, navigableOwnedEnd: str, memberEnd: str, UMLModel_Association: set["UMLModel_Property"] = None):
        self.isDerived = isDerived
        self.endType = endType
        self.navigableOwnedEnd = navigableOwnedEnd
        self.memberEnd = memberEnd
        self.UMLModel_Association = UMLModel_Association if UMLModel_Association is not None else set()
        
    @property
    def endType(self) -> str:
        return self.__endType

    @endType.setter
    def endType(self, endType: str):
        self.__endType = endType

    @property
    def isDerived(self) -> str:
        return self.__isDerived

    @isDerived.setter
    def isDerived(self, isDerived: str):
        self.__isDerived = isDerived

    @property
    def navigableOwnedEnd(self) -> str:
        return self.__navigableOwnedEnd

    @navigableOwnedEnd.setter
    def navigableOwnedEnd(self, navigableOwnedEnd: str):
        self.__navigableOwnedEnd = navigableOwnedEnd

    @property
    def memberEnd(self) -> str:
        return self.__memberEnd

    @memberEnd.setter
    def memberEnd(self, memberEnd: str):
        self.__memberEnd = memberEnd

    @property
    def UMLModel_Association(self):
        return self.__UMLModel_Association

    @UMLModel_Association.setter
    def UMLModel_Association(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Association__UMLModel_Association", None)
        self.__UMLModel_Association = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UMLModel_Property42"):
                    opp_val = getattr(item, "UMLModel_Property42", None)
                    
                    if opp_val == self:
                        setattr(item, "UMLModel_Property42", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UMLModel_Property42"):
                    opp_val = getattr(item, "UMLModel_Property42", None)
                    
                    setattr(item, "UMLModel_Property42", self)
                    

class UMLModel_DataType(Classifier):

    pass
class UMLModel_InformationItem(Classifier):

    def __init__(self, represented: str):
        self.represented = represented
        
    @property
    def represented(self) -> str:
        return self.__represented

    @represented.setter
    def represented(self, represented: str):
        self.__represented = represented

class UMLModel_Artifact(Classifier, DeployedArtifact):

    def __init__(self, fileName: str, UMLModel_Artifact: "UMLModel_Artifact" = None, UMLModel_Artifact33: set["UMLModel_Artifact"] = None, UMLModel_Artifact36: set["UMLModel_Manifestation"] = None, UMLModel_Artifact38: set["UMLModel_Operation"] = None, UMLModel_Artifact40: set["UMLModel_Property"] = None):
        self.fileName = fileName
        self.UMLModel_Artifact = UMLModel_Artifact
        self.UMLModel_Artifact33 = UMLModel_Artifact33 if UMLModel_Artifact33 is not None else set()
        self.UMLModel_Artifact36 = UMLModel_Artifact36 if UMLModel_Artifact36 is not None else set()
        self.UMLModel_Artifact38 = UMLModel_Artifact38 if UMLModel_Artifact38 is not None else set()
        self.UMLModel_Artifact40 = UMLModel_Artifact40 if UMLModel_Artifact40 is not None else set()
        
    @property
    def fileName(self) -> str:
        return self.__fileName

    @fileName.setter
    def fileName(self, fileName: str):
        self.__fileName = fileName

    @property
    def UMLModel_Artifact40(self):
        return self.__UMLModel_Artifact40

    @UMLModel_Artifact40.setter
    def UMLModel_Artifact40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Artifact__UMLModel_Artifact40", None)
        self.__UMLModel_Artifact40 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UMLModel_Property"):
                    opp_val = getattr(item, "UMLModel_Property", None)
                    
                    if opp_val == self:
                        setattr(item, "UMLModel_Property", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UMLModel_Property"):
                    opp_val = getattr(item, "UMLModel_Property", None)
                    
                    setattr(item, "UMLModel_Property", self)
                    

    @property
    def UMLModel_Artifact(self):
        return self.__UMLModel_Artifact

    @UMLModel_Artifact.setter
    def UMLModel_Artifact(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Artifact__UMLModel_Artifact", None)
        self.__UMLModel_Artifact = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_Artifact33"):
                opp_val = getattr(old_value, "UMLModel_Artifact33", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_Artifact33"):
                opp_val = getattr(value, "UMLModel_Artifact33", None)
                if opp_val is None:
                    setattr(value, "UMLModel_Artifact33", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UMLModel_Artifact33(self):
        return self.__UMLModel_Artifact33

    @UMLModel_Artifact33.setter
    def UMLModel_Artifact33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Artifact__UMLModel_Artifact33", None)
        self.__UMLModel_Artifact33 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UMLModel_Artifact"):
                    opp_val = getattr(item, "UMLModel_Artifact", None)
                    
                    if opp_val == self:
                        setattr(item, "UMLModel_Artifact", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UMLModel_Artifact"):
                    opp_val = getattr(item, "UMLModel_Artifact", None)
                    
                    setattr(item, "UMLModel_Artifact", self)
                    

    @property
    def UMLModel_Artifact38(self):
        return self.__UMLModel_Artifact38

    @UMLModel_Artifact38.setter
    def UMLModel_Artifact38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Artifact__UMLModel_Artifact38", None)
        self.__UMLModel_Artifact38 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UMLModel_Operation"):
                    opp_val = getattr(item, "UMLModel_Operation", None)
                    
                    if opp_val == self:
                        setattr(item, "UMLModel_Operation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UMLModel_Operation"):
                    opp_val = getattr(item, "UMLModel_Operation", None)
                    
                    setattr(item, "UMLModel_Operation", self)
                    

    @property
    def UMLModel_Artifact36(self):
        return self.__UMLModel_Artifact36

    @UMLModel_Artifact36.setter
    def UMLModel_Artifact36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Artifact__UMLModel_Artifact36", None)
        self.__UMLModel_Artifact36 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UMLModel_Manifestation"):
                    opp_val = getattr(item, "UMLModel_Manifestation", None)
                    
                    if opp_val == self:
                        setattr(item, "UMLModel_Manifestation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UMLModel_Manifestation"):
                    opp_val = getattr(item, "UMLModel_Manifestation", None)
                    
                    setattr(item, "UMLModel_Manifestation", self)
                    

class MessageEvent:

    pass
class UMLModel_ReceiveOperationEvent(MessageEvent):

    def __init__(self, operation: str):
        self.operation = operation
        
    @property
    def operation(self) -> str:
        return self.__operation

    @operation.setter
    def operation(self, operation: str):
        self.__operation = operation

class UMLModel_CallEvent(MessageEvent):

    def __init__(self, operation: str):
        self.operation = operation
        
    @property
    def operation(self) -> str:
        return self.__operation

    @operation.setter
    def operation(self, operation: str):
        self.__operation = operation

class UMLModel_ReceiveSignalEvent(MessageEvent):

    def __init__(self, signal: str):
        self.signal = signal
        
    @property
    def signal(self) -> str:
        return self.__signal

    @signal.setter
    def signal(self, signal: str):
        self.__signal = signal

class UMLModel_SignalEvent(MessageEvent):

    def __init__(self, signal: str):
        self.signal = signal
        
    @property
    def signal(self) -> str:
        return self.__signal

    @signal.setter
    def signal(self, signal: str):
        self.__signal = signal

class UMLModel_SendSignalEvent(MessageEvent):

    def __init__(self, signal: str):
        self.signal = signal
        
    @property
    def signal(self) -> str:
        return self.__signal

    @signal.setter
    def signal(self, signal: str):
        self.__signal = signal

class UMLModel_AnyReceiveEvent(MessageEvent):

    pass
class WriteVariableAction:

    pass
class UMLModel_RemoveVariableValueAction(WriteVariableAction):

    def __init__(self, isRemoveDuplicates: str, UMLModel_RemoveVariableValueAction: "UMLModel_InputPin" = None):
        self.isRemoveDuplicates = isRemoveDuplicates
        self.UMLModel_RemoveVariableValueAction = UMLModel_RemoveVariableValueAction
        
    @property
    def isRemoveDuplicates(self) -> str:
        return self.__isRemoveDuplicates

    @isRemoveDuplicates.setter
    def isRemoveDuplicates(self, isRemoveDuplicates: str):
        self.__isRemoveDuplicates = isRemoveDuplicates

    @property
    def UMLModel_RemoveVariableValueAction(self):
        return self.__UMLModel_RemoveVariableValueAction

    @UMLModel_RemoveVariableValueAction.setter
    def UMLModel_RemoveVariableValueAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_RemoveVariableValueAction__UMLModel_RemoveVariableValueAction", None)
        self.__UMLModel_RemoveVariableValueAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_InputPin271"):
                opp_val = getattr(old_value, "UMLModel_InputPin271", None)
                if opp_val == self:
                    setattr(old_value, "UMLModel_InputPin271", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_InputPin271"):
                opp_val = getattr(value, "UMLModel_InputPin271", None)
                setattr(value, "UMLModel_InputPin271", self)

class UMLModel_AddVariableValueAction(WriteVariableAction):

    def __init__(self, isReplaceAll: str, UMLModel_AddVariableValueAction: "UMLModel_InputPin" = None):
        self.isReplaceAll = isReplaceAll
        self.UMLModel_AddVariableValueAction = UMLModel_AddVariableValueAction
        
    @property
    def isReplaceAll(self) -> str:
        return self.__isReplaceAll

    @isReplaceAll.setter
    def isReplaceAll(self, isReplaceAll: str):
        self.__isReplaceAll = isReplaceAll

    @property
    def UMLModel_AddVariableValueAction(self):
        return self.__UMLModel_AddVariableValueAction

    @UMLModel_AddVariableValueAction.setter
    def UMLModel_AddVariableValueAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_AddVariableValueAction__UMLModel_AddVariableValueAction", None)
        self.__UMLModel_AddVariableValueAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_InputPin32"):
                opp_val = getattr(old_value, "UMLModel_InputPin32", None)
                if opp_val == self:
                    setattr(old_value, "UMLModel_InputPin32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_InputPin32"):
                opp_val = getattr(value, "UMLModel_InputPin32", None)
                setattr(value, "UMLModel_InputPin32", self)

class UMLModel_InputPin(Pin):

    pass
class WriteStructuralFeatureAction:

    pass
class UMLModel_RemoveStructuralFeatureValueAction(WriteStructuralFeatureAction):

    def __init__(self, isRemoveDuplicates: str, UMLModel_RemoveStructuralFeatureValueAction: "UMLModel_InputPin" = None):
        self.isRemoveDuplicates = isRemoveDuplicates
        self.UMLModel_RemoveStructuralFeatureValueAction = UMLModel_RemoveStructuralFeatureValueAction
        
    @property
    def isRemoveDuplicates(self) -> str:
        return self.__isRemoveDuplicates

    @isRemoveDuplicates.setter
    def isRemoveDuplicates(self, isRemoveDuplicates: str):
        self.__isRemoveDuplicates = isRemoveDuplicates

    @property
    def UMLModel_RemoveStructuralFeatureValueAction(self):
        return self.__UMLModel_RemoveStructuralFeatureValueAction

    @UMLModel_RemoveStructuralFeatureValueAction.setter
    def UMLModel_RemoveStructuralFeatureValueAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_RemoveStructuralFeatureValueAction__UMLModel_RemoveStructuralFeatureValueAction", None)
        self.__UMLModel_RemoveStructuralFeatureValueAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_InputPin273"):
                opp_val = getattr(old_value, "UMLModel_InputPin273", None)
                if opp_val == self:
                    setattr(old_value, "UMLModel_InputPin273", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_InputPin273"):
                opp_val = getattr(value, "UMLModel_InputPin273", None)
                setattr(value, "UMLModel_InputPin273", self)

class UMLModel_AddStructuralFeatureValueAction(WriteStructuralFeatureAction):

    def __init__(self, isReplaceAll: str, UMLModel_AddStructuralFeatureValueAction: "UMLModel_InputPin" = None):
        self.isReplaceAll = isReplaceAll
        self.UMLModel_AddStructuralFeatureValueAction = UMLModel_AddStructuralFeatureValueAction
        
    @property
    def isReplaceAll(self) -> str:
        return self.__isReplaceAll

    @isReplaceAll.setter
    def isReplaceAll(self, isReplaceAll: str):
        self.__isReplaceAll = isReplaceAll

    @property
    def UMLModel_AddStructuralFeatureValueAction(self):
        return self.__UMLModel_AddStructuralFeatureValueAction

    @UMLModel_AddStructuralFeatureValueAction.setter
    def UMLModel_AddStructuralFeatureValueAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_AddStructuralFeatureValueAction__UMLModel_AddStructuralFeatureValueAction", None)
        self.__UMLModel_AddStructuralFeatureValueAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_InputPin"):
                opp_val = getattr(old_value, "UMLModel_InputPin", None)
                if opp_val == self:
                    setattr(old_value, "UMLModel_InputPin", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_InputPin"):
                opp_val = getattr(value, "UMLModel_InputPin", None)
                setattr(value, "UMLModel_InputPin", self)

class BehavioredClassifier:

    pass
class UMLModel_Collaboration(BehavioredClassifier, StructuredClassifier):

    def __init__(self, collaborationRole: str):
        self.collaborationRole = collaborationRole
        
    @property
    def collaborationRole(self) -> str:
        return self.__collaborationRole

    @collaborationRole.setter
    def collaborationRole(self, collaborationRole: str):
        self.__collaborationRole = collaborationRole

class UMLModel_Class(BehavioredClassifier, EncapsulatedClassifier):

    def __init__(self, isActive: str, superclass: str, extension: str, UMLModel_Class: set["UMLModel_Classifier"] = None, UMLModel_Class66: set["UMLModel_Operation"] = None, UMLModel_Class69: set["UMLModel_Reception"] = None):
        self.isActive = isActive
        self.superclass = superclass
        self.extension = extension
        self.UMLModel_Class = UMLModel_Class if UMLModel_Class is not None else set()
        self.UMLModel_Class66 = UMLModel_Class66 if UMLModel_Class66 is not None else set()
        self.UMLModel_Class69 = UMLModel_Class69 if UMLModel_Class69 is not None else set()
        
    @property
    def isActive(self) -> str:
        return self.__isActive

    @isActive.setter
    def isActive(self, isActive: str):
        self.__isActive = isActive

    @property
    def extension(self) -> str:
        return self.__extension

    @extension.setter
    def extension(self, extension: str):
        self.__extension = extension

    @property
    def superclass(self) -> str:
        return self.__superclass

    @superclass.setter
    def superclass(self, superclass: str):
        self.__superclass = superclass

    @property
    def UMLModel_Class(self):
        return self.__UMLModel_Class

    @UMLModel_Class.setter
    def UMLModel_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Class__UMLModel_Class", None)
        self.__UMLModel_Class = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UMLModel_Classifier"):
                    opp_val = getattr(item, "UMLModel_Classifier", None)
                    
                    if opp_val == self:
                        setattr(item, "UMLModel_Classifier", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UMLModel_Classifier"):
                    opp_val = getattr(item, "UMLModel_Classifier", None)
                    
                    setattr(item, "UMLModel_Classifier", self)
                    

    @property
    def UMLModel_Class69(self):
        return self.__UMLModel_Class69

    @UMLModel_Class69.setter
    def UMLModel_Class69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Class__UMLModel_Class69", None)
        self.__UMLModel_Class69 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UMLModel_Reception"):
                    opp_val = getattr(item, "UMLModel_Reception", None)
                    
                    if opp_val == self:
                        setattr(item, "UMLModel_Reception", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UMLModel_Reception"):
                    opp_val = getattr(item, "UMLModel_Reception", None)
                    
                    setattr(item, "UMLModel_Reception", self)
                    

    @property
    def UMLModel_Class66(self):
        return self.__UMLModel_Class66

    @UMLModel_Class66.setter
    def UMLModel_Class66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Class__UMLModel_Class66", None)
        self.__UMLModel_Class66 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UMLModel_Operation67"):
                    opp_val = getattr(item, "UMLModel_Operation67", None)
                    
                    if opp_val == self:
                        setattr(item, "UMLModel_Operation67", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UMLModel_Operation67"):
                    opp_val = getattr(item, "UMLModel_Operation67", None)
                    
                    setattr(item, "UMLModel_Operation67", self)
                    

class UMLModel_UseCase(BehavioredClassifier):

    def __init__(self, subject: str, UMLModel_UseCase: "UMLModel_Classifier" = None, UMLModel_UseCase377: set["UMLModel_Include"] = None, UMLModel_UseCase379: set["UMLModel_Extend"] = None, UMLModel_UseCase382: set["UMLModel_ExtensionPoint"] = None):
        self.subject = subject
        self.UMLModel_UseCase = UMLModel_UseCase
        self.UMLModel_UseCase377 = UMLModel_UseCase377 if UMLModel_UseCase377 is not None else set()
        self.UMLModel_UseCase379 = UMLModel_UseCase379 if UMLModel_UseCase379 is not None else set()
        self.UMLModel_UseCase382 = UMLModel_UseCase382 if UMLModel_UseCase382 is not None else set()
        
    @property
    def subject(self) -> str:
        return self.__subject

    @subject.setter
    def subject(self, subject: str):
        self.__subject = subject

    @property
    def UMLModel_UseCase377(self):
        return self.__UMLModel_UseCase377

    @UMLModel_UseCase377.setter
    def UMLModel_UseCase377(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_UseCase__UMLModel_UseCase377", None)
        self.__UMLModel_UseCase377 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UMLModel_Include"):
                    opp_val = getattr(item, "UMLModel_Include", None)
                    
                    if opp_val == self:
                        setattr(item, "UMLModel_Include", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UMLModel_Include"):
                    opp_val = getattr(item, "UMLModel_Include", None)
                    
                    setattr(item, "UMLModel_Include", self)
                    

    @property
    def UMLModel_UseCase382(self):
        return self.__UMLModel_UseCase382

    @UMLModel_UseCase382.setter
    def UMLModel_UseCase382(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_UseCase__UMLModel_UseCase382", None)
        self.__UMLModel_UseCase382 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UMLModel_ExtensionPoint"):
                    opp_val = getattr(item, "UMLModel_ExtensionPoint", None)
                    
                    if opp_val == self:
                        setattr(item, "UMLModel_ExtensionPoint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UMLModel_ExtensionPoint"):
                    opp_val = getattr(item, "UMLModel_ExtensionPoint", None)
                    
                    setattr(item, "UMLModel_ExtensionPoint", self)
                    

    @property
    def UMLModel_UseCase(self):
        return self.__UMLModel_UseCase

    @UMLModel_UseCase.setter
    def UMLModel_UseCase(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_UseCase__UMLModel_UseCase", None)
        self.__UMLModel_UseCase = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_Classifier77"):
                opp_val = getattr(old_value, "UMLModel_Classifier77", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_Classifier77"):
                opp_val = getattr(value, "UMLModel_Classifier77", None)
                if opp_val is None:
                    setattr(value, "UMLModel_Classifier77", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UMLModel_UseCase379(self):
        return self.__UMLModel_UseCase379

    @UMLModel_UseCase379.setter
    def UMLModel_UseCase379(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_UseCase__UMLModel_UseCase379", None)
        self.__UMLModel_UseCase379 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UMLModel_Extend380"):
                    opp_val = getattr(item, "UMLModel_Extend380", None)
                    
                    if opp_val == self:
                        setattr(item, "UMLModel_Extend380", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UMLModel_Extend380"):
                    opp_val = getattr(item, "UMLModel_Extend380", None)
                    
                    setattr(item, "UMLModel_Extend380", self)
                    

class UMLModel_Actor(BehavioredClassifier):

    pass
class ObjectNode:

    pass
class UMLModel_CentralBufferNode(ObjectNode):

    pass
class UMLModel_Pin(MultiplicityElement, ObjectNode):

    def __init__(self, isControl: str):
        self.isControl = isControl
        
    @property
    def isControl(self) -> str:
        return self.__isControl

    @isControl.setter
    def isControl(self, isControl: str):
        self.__isControl = isControl

class UMLModel_ExpansionNode(ObjectNode):

    def __init__(self, regionAsOutput: str, regionAsInput: str):
        self.regionAsOutput = regionAsOutput
        self.regionAsInput = regionAsInput
        
    @property
    def regionAsInput(self) -> str:
        return self.__regionAsInput

    @regionAsInput.setter
    def regionAsInput(self, regionAsInput: str):
        self.__regionAsInput = regionAsInput

    @property
    def regionAsOutput(self) -> str:
        return self.__regionAsOutput

    @regionAsOutput.setter
    def regionAsOutput(self, regionAsOutput: str):
        self.__regionAsOutput = regionAsOutput

class UMLModel_ActivityParameterNode(ObjectNode):

    def __init__(self, parameter: str):
        self.parameter = parameter
        
    @property
    def parameter(self) -> str:
        return self.__parameter

    @parameter.setter
    def parameter(self, parameter: str):
        self.__parameter = parameter

class Element:

    pass
class UMLModel_ExceptionHandler(Element):

    def __init__(self, handlerBody: str, exceptionInput: str, exceptionType: str, protectedNode: str, UMLModel_ExceptionHandler: "UMLModel_ExecutableNode" = None):
        self.handlerBody = handlerBody
        self.exceptionInput = exceptionInput
        self.exceptionType = exceptionType
        self.protectedNode = protectedNode
        self.UMLModel_ExceptionHandler = UMLModel_ExceptionHandler
        
    @property
    def exceptionInput(self) -> str:
        return self.__exceptionInput

    @exceptionInput.setter
    def exceptionInput(self, exceptionInput: str):
        self.__exceptionInput = exceptionInput

    @property
    def handlerBody(self) -> str:
        return self.__handlerBody

    @handlerBody.setter
    def handlerBody(self, handlerBody: str):
        self.__handlerBody = handlerBody

    @property
    def protectedNode(self) -> str:
        return self.__protectedNode

    @protectedNode.setter
    def protectedNode(self, protectedNode: str):
        self.__protectedNode = protectedNode

    @property
    def exceptionType(self) -> str:
        return self.__exceptionType

    @exceptionType.setter
    def exceptionType(self, exceptionType: str):
        self.__exceptionType = exceptionType

    @property
    def UMLModel_ExceptionHandler(self):
        return self.__UMLModel_ExceptionHandler

    @UMLModel_ExceptionHandler.setter
    def UMLModel_ExceptionHandler(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_ExceptionHandler__UMLModel_ExceptionHandler", None)
        self.__UMLModel_ExceptionHandler = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_ExecutableNode"):
                opp_val = getattr(old_value, "UMLModel_ExecutableNode", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_ExecutableNode"):
                opp_val = getattr(value, "UMLModel_ExecutableNode", None)
                if opp_val is None:
                    setattr(value, "UMLModel_ExecutableNode", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class UMLModel_TemplateSignature(Element):

    def __init__(self, template: str, parameter: str, UMLModel_TemplateSignature346: set["UMLModel_TemplateParameter"] = None, UMLModel_TemplateSignature: "UMLModel_TemplateableElement" = None):
        self.template = template
        self.parameter = parameter
        self.UMLModel_TemplateSignature346 = UMLModel_TemplateSignature346 if UMLModel_TemplateSignature346 is not None else set()
        self.UMLModel_TemplateSignature = UMLModel_TemplateSignature
        
    @property
    def parameter(self) -> str:
        return self.__parameter

    @parameter.setter
    def parameter(self, parameter: str):
        self.__parameter = parameter

    @property
    def template(self) -> str:
        return self.__template

    @template.setter
    def template(self, template: str):
        self.__template = template

    @property
    def UMLModel_TemplateSignature(self):
        return self.__UMLModel_TemplateSignature

    @UMLModel_TemplateSignature.setter
    def UMLModel_TemplateSignature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_TemplateSignature__UMLModel_TemplateSignature", None)
        self.__UMLModel_TemplateSignature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_TemplateableElement342"):
                opp_val = getattr(old_value, "UMLModel_TemplateableElement342", None)
                if opp_val == self:
                    setattr(old_value, "UMLModel_TemplateableElement342", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_TemplateableElement342"):
                opp_val = getattr(value, "UMLModel_TemplateableElement342", None)
                setattr(value, "UMLModel_TemplateableElement342", self)

    @property
    def UMLModel_TemplateSignature346(self):
        return self.__UMLModel_TemplateSignature346

    @UMLModel_TemplateSignature346.setter
    def UMLModel_TemplateSignature346(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_TemplateSignature__UMLModel_TemplateSignature346", None)
        self.__UMLModel_TemplateSignature346 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UMLModel_TemplateParameter"):
                    opp_val = getattr(item, "UMLModel_TemplateParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "UMLModel_TemplateParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UMLModel_TemplateParameter"):
                    opp_val = getattr(item, "UMLModel_TemplateParameter", None)
                    
                    setattr(item, "UMLModel_TemplateParameter", self)
                    

class UMLModel_NamedElement(Element):

    def __init__(self, name: str, visibility: str, qualifiedName: str, clientDependency: str, namespace: str, UMLModel_NamedElement: "UMLModel_StringExpression" = None):
        self.name = name
        self.visibility = visibility
        self.qualifiedName = qualifiedName
        self.clientDependency = clientDependency
        self.namespace = namespace
        self.UMLModel_NamedElement = UMLModel_NamedElement
        
    @property
    def qualifiedName(self) -> str:
        return self.__qualifiedName

    @qualifiedName.setter
    def qualifiedName(self, qualifiedName: str):
        self.__qualifiedName = qualifiedName

    @property
    def namespace(self) -> str:
        return self.__namespace

    @namespace.setter
    def namespace(self, namespace: str):
        self.__namespace = namespace

    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def clientDependency(self) -> str:
        return self.__clientDependency

    @clientDependency.setter
    def clientDependency(self, clientDependency: str):
        self.__clientDependency = clientDependency

    @property
    def UMLModel_NamedElement(self):
        return self.__UMLModel_NamedElement

    @UMLModel_NamedElement.setter
    def UMLModel_NamedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_NamedElement__UMLModel_NamedElement", None)
        self.__UMLModel_NamedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_StringExpression"):
                opp_val = getattr(old_value, "UMLModel_StringExpression", None)
                if opp_val == self:
                    setattr(old_value, "UMLModel_StringExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_StringExpression"):
                opp_val = getattr(value, "UMLModel_StringExpression", None)
                setattr(value, "UMLModel_StringExpression", self)

class UMLModel_ParameterableElement(Element):

    def __init__(self, owningTemplateParameter: str, templateParameter: str, UMLModel_ParameterableElement: "UMLModel_TemplateParameter" = None, UMLModel_ParameterableElement351: "UMLModel_TemplateParameter" = None, UMLModel_ParameterableElement354: "UMLModel_TemplateParameterSubstitution" = None):
        self.owningTemplateParameter = owningTemplateParameter
        self.templateParameter = templateParameter
        self.UMLModel_ParameterableElement = UMLModel_ParameterableElement
        self.UMLModel_ParameterableElement351 = UMLModel_ParameterableElement351
        self.UMLModel_ParameterableElement354 = UMLModel_ParameterableElement354
        
    @property
    def owningTemplateParameter(self) -> str:
        return self.__owningTemplateParameter

    @owningTemplateParameter.setter
    def owningTemplateParameter(self, owningTemplateParameter: str):
        self.__owningTemplateParameter = owningTemplateParameter

    @property
    def templateParameter(self) -> str:
        return self.__templateParameter

    @templateParameter.setter
    def templateParameter(self, templateParameter: str):
        self.__templateParameter = templateParameter

    @property
    def UMLModel_ParameterableElement354(self):
        return self.__UMLModel_ParameterableElement354

    @UMLModel_ParameterableElement354.setter
    def UMLModel_ParameterableElement354(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_ParameterableElement__UMLModel_ParameterableElement354", None)
        self.__UMLModel_ParameterableElement354 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_TemplateParameterSubstitution353"):
                opp_val = getattr(old_value, "UMLModel_TemplateParameterSubstitution353", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_TemplateParameterSubstitution353"):
                opp_val = getattr(value, "UMLModel_TemplateParameterSubstitution353", None)
                if opp_val is None:
                    setattr(value, "UMLModel_TemplateParameterSubstitution353", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UMLModel_ParameterableElement351(self):
        return self.__UMLModel_ParameterableElement351

    @UMLModel_ParameterableElement351.setter
    def UMLModel_ParameterableElement351(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_ParameterableElement__UMLModel_ParameterableElement351", None)
        self.__UMLModel_ParameterableElement351 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_TemplateParameter350"):
                opp_val = getattr(old_value, "UMLModel_TemplateParameter350", None)
                if opp_val == self:
                    setattr(old_value, "UMLModel_TemplateParameter350", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_TemplateParameter350"):
                opp_val = getattr(value, "UMLModel_TemplateParameter350", None)
                setattr(value, "UMLModel_TemplateParameter350", self)

    @property
    def UMLModel_ParameterableElement(self):
        return self.__UMLModel_ParameterableElement

    @UMLModel_ParameterableElement.setter
    def UMLModel_ParameterableElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_ParameterableElement__UMLModel_ParameterableElement", None)
        self.__UMLModel_ParameterableElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_TemplateParameter348"):
                opp_val = getattr(old_value, "UMLModel_TemplateParameter348", None)
                if opp_val == self:
                    setattr(old_value, "UMLModel_TemplateParameter348", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_TemplateParameter348"):
                opp_val = getattr(value, "UMLModel_TemplateParameter348", None)
                setattr(value, "UMLModel_TemplateParameter348", self)

class UMLModel_Image(Element):

    def __init__(self, content: str, location: str, format: str, UMLModel_Image: "UMLModel_Stereotype" = None):
        self.content = content
        self.location = location
        self.format = format
        self.UMLModel_Image = UMLModel_Image
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def format(self) -> str:
        return self.__format

    @format.setter
    def format(self, format: str):
        self.__format = format

    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def UMLModel_Image(self):
        return self.__UMLModel_Image

    @UMLModel_Image.setter
    def UMLModel_Image(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Image__UMLModel_Image", None)
        self.__UMLModel_Image = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_Stereotype"):
                opp_val = getattr(old_value, "UMLModel_Stereotype", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_Stereotype"):
                opp_val = getattr(value, "UMLModel_Stereotype", None)
                if opp_val is None:
                    setattr(value, "UMLModel_Stereotype", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class UMLModel_MultiplicityElement(Element):

    def __init__(self, isOrdered: str, isUnique: str, upper: str, lower: str, UMLModel_MultiplicityElement: "UMLModel_ValueSpecification" = None, UMLModel_MultiplicityElement189: "UMLModel_ValueSpecification" = None):
        self.isOrdered = isOrdered
        self.isUnique = isUnique
        self.upper = upper
        self.lower = lower
        self.UMLModel_MultiplicityElement = UMLModel_MultiplicityElement
        self.UMLModel_MultiplicityElement189 = UMLModel_MultiplicityElement189
        
    @property
    def upper(self) -> str:
        return self.__upper

    @upper.setter
    def upper(self, upper: str):
        self.__upper = upper

    @property
    def isOrdered(self) -> str:
        return self.__isOrdered

    @isOrdered.setter
    def isOrdered(self, isOrdered: str):
        self.__isOrdered = isOrdered

    @property
    def lower(self) -> str:
        return self.__lower

    @lower.setter
    def lower(self, lower: str):
        self.__lower = lower

    @property
    def isUnique(self) -> str:
        return self.__isUnique

    @isUnique.setter
    def isUnique(self, isUnique: str):
        self.__isUnique = isUnique

    @property
    def UMLModel_MultiplicityElement189(self):
        return self.__UMLModel_MultiplicityElement189

    @UMLModel_MultiplicityElement189.setter
    def UMLModel_MultiplicityElement189(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_MultiplicityElement__UMLModel_MultiplicityElement189", None)
        self.__UMLModel_MultiplicityElement189 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_ValueSpecification190"):
                opp_val = getattr(old_value, "UMLModel_ValueSpecification190", None)
                if opp_val == self:
                    setattr(old_value, "UMLModel_ValueSpecification190", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_ValueSpecification190"):
                opp_val = getattr(value, "UMLModel_ValueSpecification190", None)
                setattr(value, "UMLModel_ValueSpecification190", self)

    @property
    def UMLModel_MultiplicityElement(self):
        return self.__UMLModel_MultiplicityElement

    @UMLModel_MultiplicityElement.setter
    def UMLModel_MultiplicityElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_MultiplicityElement__UMLModel_MultiplicityElement", None)
        self.__UMLModel_MultiplicityElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_ValueSpecification187"):
                opp_val = getattr(old_value, "UMLModel_ValueSpecification187", None)
                if opp_val == self:
                    setattr(old_value, "UMLModel_ValueSpecification187", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_ValueSpecification187"):
                opp_val = getattr(value, "UMLModel_ValueSpecification187", None)
                setattr(value, "UMLModel_ValueSpecification187", self)

class UMLModel_TemplateParameterSubstitution(Element):

    def __init__(self, formal: str, actual: str, templateBinding: str, UMLModel_TemplateParameterSubstitution353: set["UMLModel_ParameterableElement"] = None, UMLModel_TemplateParameterSubstitution: "UMLModel_TemplateBinding" = None):
        self.formal = formal
        self.actual = actual
        self.templateBinding = templateBinding
        self.UMLModel_TemplateParameterSubstitution353 = UMLModel_TemplateParameterSubstitution353 if UMLModel_TemplateParameterSubstitution353 is not None else set()
        self.UMLModel_TemplateParameterSubstitution = UMLModel_TemplateParameterSubstitution
        
    @property
    def formal(self) -> str:
        return self.__formal

    @formal.setter
    def formal(self, formal: str):
        self.__formal = formal

    @property
    def actual(self) -> str:
        return self.__actual

    @actual.setter
    def actual(self, actual: str):
        self.__actual = actual

    @property
    def templateBinding(self) -> str:
        return self.__templateBinding

    @templateBinding.setter
    def templateBinding(self, templateBinding: str):
        self.__templateBinding = templateBinding

    @property
    def UMLModel_TemplateParameterSubstitution(self):
        return self.__UMLModel_TemplateParameterSubstitution

    @UMLModel_TemplateParameterSubstitution.setter
    def UMLModel_TemplateParameterSubstitution(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_TemplateParameterSubstitution__UMLModel_TemplateParameterSubstitution", None)
        self.__UMLModel_TemplateParameterSubstitution = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_TemplateBinding344"):
                opp_val = getattr(old_value, "UMLModel_TemplateBinding344", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_TemplateBinding344"):
                opp_val = getattr(value, "UMLModel_TemplateBinding344", None)
                if opp_val is None:
                    setattr(value, "UMLModel_TemplateBinding344", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UMLModel_TemplateParameterSubstitution353(self):
        return self.__UMLModel_TemplateParameterSubstitution353

    @UMLModel_TemplateParameterSubstitution353.setter
    def UMLModel_TemplateParameterSubstitution353(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_TemplateParameterSubstitution__UMLModel_TemplateParameterSubstitution353", None)
        self.__UMLModel_TemplateParameterSubstitution353 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UMLModel_ParameterableElement354"):
                    opp_val = getattr(item, "UMLModel_ParameterableElement354", None)
                    
                    if opp_val == self:
                        setattr(item, "UMLModel_ParameterableElement354", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UMLModel_ParameterableElement354"):
                    opp_val = getattr(item, "UMLModel_ParameterableElement354", None)
                    
                    setattr(item, "UMLModel_ParameterableElement354", self)
                    

class UMLModel_QualifierValue(Element):

    def __init__(self, qualifier: str, value: str, UMLModel_QualifierValue: "UMLModel_LinkEndData" = None):
        self.qualifier = qualifier
        self.value = value
        self.UMLModel_QualifierValue = UMLModel_QualifierValue
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def qualifier(self) -> str:
        return self.__qualifier

    @qualifier.setter
    def qualifier(self, qualifier: str):
        self.__qualifier = qualifier

    @property
    def UMLModel_QualifierValue(self):
        return self.__UMLModel_QualifierValue

    @UMLModel_QualifierValue.setter
    def UMLModel_QualifierValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_QualifierValue__UMLModel_QualifierValue", None)
        self.__UMLModel_QualifierValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_LinkEndData177"):
                opp_val = getattr(old_value, "UMLModel_LinkEndData177", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_LinkEndData177"):
                opp_val = getattr(value, "UMLModel_LinkEndData177", None)
                if opp_val is None:
                    setattr(value, "UMLModel_LinkEndData177", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class UMLModel_LinkEndData(Element):

    def __init__(self, value: str, end: str, UMLModel_LinkEndData: "UMLModel_LinkAction" = None, UMLModel_LinkEndData177: set["UMLModel_QualifierValue"] = None):
        self.value = value
        self.end = end
        self.UMLModel_LinkEndData = UMLModel_LinkEndData
        self.UMLModel_LinkEndData177 = UMLModel_LinkEndData177 if UMLModel_LinkEndData177 is not None else set()
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def end(self) -> str:
        return self.__end

    @end.setter
    def end(self, end: str):
        self.__end = end

    @property
    def UMLModel_LinkEndData(self):
        return self.__UMLModel_LinkEndData

    @UMLModel_LinkEndData.setter
    def UMLModel_LinkEndData(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_LinkEndData__UMLModel_LinkEndData", None)
        self.__UMLModel_LinkEndData = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_LinkAction"):
                opp_val = getattr(old_value, "UMLModel_LinkAction", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_LinkAction"):
                opp_val = getattr(value, "UMLModel_LinkAction", None)
                if opp_val is None:
                    setattr(value, "UMLModel_LinkAction", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UMLModel_LinkEndData177(self):
        return self.__UMLModel_LinkEndData177

    @UMLModel_LinkEndData177.setter
    def UMLModel_LinkEndData177(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_LinkEndData__UMLModel_LinkEndData177", None)
        self.__UMLModel_LinkEndData177 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UMLModel_QualifierValue"):
                    opp_val = getattr(item, "UMLModel_QualifierValue", None)
                    
                    if opp_val == self:
                        setattr(item, "UMLModel_QualifierValue", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UMLModel_QualifierValue"):
                    opp_val = getattr(item, "UMLModel_QualifierValue", None)
                    
                    setattr(item, "UMLModel_QualifierValue", self)
                    

class UMLModel_Slot(Element):

    def __init__(self, definingFeature: str, owningInstance: str, UMLModel_Slot: "UMLModel_InstanceSpecification" = None, UMLModel_Slot282: set["UMLModel_ValueSpecification"] = None):
        self.definingFeature = definingFeature
        self.owningInstance = owningInstance
        self.UMLModel_Slot = UMLModel_Slot
        self.UMLModel_Slot282 = UMLModel_Slot282 if UMLModel_Slot282 is not None else set()
        
    @property
    def owningInstance(self) -> str:
        return self.__owningInstance

    @owningInstance.setter
    def owningInstance(self, owningInstance: str):
        self.__owningInstance = owningInstance

    @property
    def definingFeature(self) -> str:
        return self.__definingFeature

    @definingFeature.setter
    def definingFeature(self, definingFeature: str):
        self.__definingFeature = definingFeature

    @property
    def UMLModel_Slot(self):
        return self.__UMLModel_Slot

    @UMLModel_Slot.setter
    def UMLModel_Slot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Slot__UMLModel_Slot", None)
        self.__UMLModel_Slot = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_InstanceSpecification"):
                opp_val = getattr(old_value, "UMLModel_InstanceSpecification", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_InstanceSpecification"):
                opp_val = getattr(value, "UMLModel_InstanceSpecification", None)
                if opp_val is None:
                    setattr(value, "UMLModel_InstanceSpecification", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UMLModel_Slot282(self):
        return self.__UMLModel_Slot282

    @UMLModel_Slot282.setter
    def UMLModel_Slot282(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Slot__UMLModel_Slot282", None)
        self.__UMLModel_Slot282 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UMLModel_ValueSpecification283"):
                    opp_val = getattr(item, "UMLModel_ValueSpecification283", None)
                    
                    if opp_val == self:
                        setattr(item, "UMLModel_ValueSpecification283", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UMLModel_ValueSpecification283"):
                    opp_val = getattr(item, "UMLModel_ValueSpecification283", None)
                    
                    setattr(item, "UMLModel_ValueSpecification283", self)
                    

class UMLModel_Comment(Element):

    def __init__(self, body: str, annotatedElement: str, UMLModel_Comment: "UMLModel_Element" = None):
        self.body = body
        self.annotatedElement = annotatedElement
        self.UMLModel_Comment = UMLModel_Comment
        
    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

    @property
    def annotatedElement(self) -> str:
        return self.__annotatedElement

    @annotatedElement.setter
    def annotatedElement(self, annotatedElement: str):
        self.__annotatedElement = annotatedElement

    @property
    def UMLModel_Comment(self):
        return self.__UMLModel_Comment

    @UMLModel_Comment.setter
    def UMLModel_Comment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Comment__UMLModel_Comment", None)
        self.__UMLModel_Comment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_Element"):
                opp_val = getattr(old_value, "UMLModel_Element", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_Element"):
                opp_val = getattr(value, "UMLModel_Element", None)
                if opp_val is None:
                    setattr(value, "UMLModel_Element", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class UMLModel_Relationship(Element):

    def __init__(self, relatedElement: str):
        self.relatedElement = relatedElement
        
    @property
    def relatedElement(self) -> str:
        return self.__relatedElement

    @relatedElement.setter
    def relatedElement(self, relatedElement: str):
        self.__relatedElement = relatedElement

class UMLModel_Clause(Element):

    def __init__(self, predecessorClause: str, successorClause: str, decider: str, bodyOutput: str, test: str, body: str, UMLModel_Clause: "UMLModel_ConditionalNode" = None):
        self.predecessorClause = predecessorClause
        self.successorClause = successorClause
        self.decider = decider
        self.bodyOutput = bodyOutput
        self.test = test
        self.body = body
        self.UMLModel_Clause = UMLModel_Clause
        
    @property
    def bodyOutput(self) -> str:
        return self.__bodyOutput

    @bodyOutput.setter
    def bodyOutput(self, bodyOutput: str):
        self.__bodyOutput = bodyOutput

    @property
    def test(self) -> str:
        return self.__test

    @test.setter
    def test(self, test: str):
        self.__test = test

    @property
    def predecessorClause(self) -> str:
        return self.__predecessorClause

    @predecessorClause.setter
    def predecessorClause(self, predecessorClause: str):
        self.__predecessorClause = predecessorClause

    @property
    def decider(self) -> str:
        return self.__decider

    @decider.setter
    def decider(self, decider: str):
        self.__decider = decider

    @property
    def successorClause(self) -> str:
        return self.__successorClause

    @successorClause.setter
    def successorClause(self, successorClause: str):
        self.__successorClause = successorClause

    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

    @property
    def UMLModel_Clause(self):
        return self.__UMLModel_Clause

    @UMLModel_Clause.setter
    def UMLModel_Clause(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Clause__UMLModel_Clause", None)
        self.__UMLModel_Clause = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_ConditionalNode"):
                opp_val = getattr(old_value, "UMLModel_ConditionalNode", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_ConditionalNode"):
                opp_val = getattr(value, "UMLModel_ConditionalNode", None)
                if opp_val is None:
                    setattr(value, "UMLModel_ConditionalNode", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class UMLModel_TemplateParameter(Element):

    def __init__(self, signature: str, parameteredElement: str, default: str, UMLModel_TemplateParameter: "UMLModel_TemplateSignature" = None, UMLModel_TemplateParameter348: "UMLModel_ParameterableElement" = None, UMLModel_TemplateParameter350: "UMLModel_ParameterableElement" = None):
        self.signature = signature
        self.parameteredElement = parameteredElement
        self.default = default
        self.UMLModel_TemplateParameter = UMLModel_TemplateParameter
        self.UMLModel_TemplateParameter348 = UMLModel_TemplateParameter348
        self.UMLModel_TemplateParameter350 = UMLModel_TemplateParameter350
        
    @property
    def default(self) -> str:
        return self.__default

    @default.setter
    def default(self, default: str):
        self.__default = default

    @property
    def parameteredElement(self) -> str:
        return self.__parameteredElement

    @parameteredElement.setter
    def parameteredElement(self, parameteredElement: str):
        self.__parameteredElement = parameteredElement

    @property
    def signature(self) -> str:
        return self.__signature

    @signature.setter
    def signature(self, signature: str):
        self.__signature = signature

    @property
    def UMLModel_TemplateParameter348(self):
        return self.__UMLModel_TemplateParameter348

    @UMLModel_TemplateParameter348.setter
    def UMLModel_TemplateParameter348(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_TemplateParameter__UMLModel_TemplateParameter348", None)
        self.__UMLModel_TemplateParameter348 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_ParameterableElement"):
                opp_val = getattr(old_value, "UMLModel_ParameterableElement", None)
                if opp_val == self:
                    setattr(old_value, "UMLModel_ParameterableElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_ParameterableElement"):
                opp_val = getattr(value, "UMLModel_ParameterableElement", None)
                setattr(value, "UMLModel_ParameterableElement", self)

    @property
    def UMLModel_TemplateParameter350(self):
        return self.__UMLModel_TemplateParameter350

    @UMLModel_TemplateParameter350.setter
    def UMLModel_TemplateParameter350(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_TemplateParameter__UMLModel_TemplateParameter350", None)
        self.__UMLModel_TemplateParameter350 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_ParameterableElement351"):
                opp_val = getattr(old_value, "UMLModel_ParameterableElement351", None)
                if opp_val == self:
                    setattr(old_value, "UMLModel_ParameterableElement351", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_ParameterableElement351"):
                opp_val = getattr(value, "UMLModel_ParameterableElement351", None)
                setattr(value, "UMLModel_ParameterableElement351", self)

    @property
    def UMLModel_TemplateParameter(self):
        return self.__UMLModel_TemplateParameter

    @UMLModel_TemplateParameter.setter
    def UMLModel_TemplateParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_TemplateParameter__UMLModel_TemplateParameter", None)
        self.__UMLModel_TemplateParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_TemplateSignature346"):
                opp_val = getattr(old_value, "UMLModel_TemplateSignature346", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_TemplateSignature346"):
                opp_val = getattr(value, "UMLModel_TemplateSignature346", None)
                if opp_val is None:
                    setattr(value, "UMLModel_TemplateSignature346", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class UMLModel_TemplateableElement(Element):

    pass
class FinalNode:

    pass
class UMLModel_FlowFinalNode(FinalNode):

    pass
class UMLModel_ActivityFinalNode(FinalNode):

    pass
class UMLModel_ValueSpecification(PackageableElement, TypedElement):

    pass
class RedefinableElement:

    pass
class UMLModel_Region(Namespace, RedefinableElement):

    def __init__(self, state: str, extendedRegion: str, stateMachine: str, UMLModel_Region: set["UMLModel_Vertex"] = None, UMLModel_Region276: set["UMLModel_Transition"] = None, UMLModel_Region328: "UMLModel_State" = None, UMLModel_Region330: "UMLModel_StateMachine" = None):
        self.state = state
        self.extendedRegion = extendedRegion
        self.stateMachine = stateMachine
        self.UMLModel_Region = UMLModel_Region if UMLModel_Region is not None else set()
        self.UMLModel_Region276 = UMLModel_Region276 if UMLModel_Region276 is not None else set()
        self.UMLModel_Region328 = UMLModel_Region328
        self.UMLModel_Region330 = UMLModel_Region330
        
    @property
    def state(self) -> str:
        return self.__state

    @state.setter
    def state(self, state: str):
        self.__state = state

    @property
    def extendedRegion(self) -> str:
        return self.__extendedRegion

    @extendedRegion.setter
    def extendedRegion(self, extendedRegion: str):
        self.__extendedRegion = extendedRegion

    @property
    def stateMachine(self) -> str:
        return self.__stateMachine

    @stateMachine.setter
    def stateMachine(self, stateMachine: str):
        self.__stateMachine = stateMachine

    @property
    def UMLModel_Region330(self):
        return self.__UMLModel_Region330

    @UMLModel_Region330.setter
    def UMLModel_Region330(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Region__UMLModel_Region330", None)
        self.__UMLModel_Region330 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_StateMachine"):
                opp_val = getattr(old_value, "UMLModel_StateMachine", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_StateMachine"):
                opp_val = getattr(value, "UMLModel_StateMachine", None)
                if opp_val is None:
                    setattr(value, "UMLModel_StateMachine", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UMLModel_Region276(self):
        return self.__UMLModel_Region276

    @UMLModel_Region276.setter
    def UMLModel_Region276(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Region__UMLModel_Region276", None)
        self.__UMLModel_Region276 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UMLModel_Transition"):
                    opp_val = getattr(item, "UMLModel_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "UMLModel_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UMLModel_Transition"):
                    opp_val = getattr(item, "UMLModel_Transition", None)
                    
                    setattr(item, "UMLModel_Transition", self)
                    

    @property
    def UMLModel_Region(self):
        return self.__UMLModel_Region

    @UMLModel_Region.setter
    def UMLModel_Region(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Region__UMLModel_Region", None)
        self.__UMLModel_Region = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UMLModel_Vertex"):
                    opp_val = getattr(item, "UMLModel_Vertex", None)
                    
                    if opp_val == self:
                        setattr(item, "UMLModel_Vertex", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UMLModel_Vertex"):
                    opp_val = getattr(item, "UMLModel_Vertex", None)
                    
                    setattr(item, "UMLModel_Vertex", self)
                    

    @property
    def UMLModel_Region328(self):
        return self.__UMLModel_Region328

    @UMLModel_Region328.setter
    def UMLModel_Region328(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Region__UMLModel_Region328", None)
        self.__UMLModel_Region328 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_State327"):
                opp_val = getattr(old_value, "UMLModel_State327", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_State327"):
                opp_val = getattr(value, "UMLModel_State327", None)
                if opp_val is None:
                    setattr(value, "UMLModel_State327", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class UMLModel_Feature(RedefinableElement):

    def __init__(self, isStatic: str, featuringClassifier: str):
        self.isStatic = isStatic
        self.featuringClassifier = featuringClassifier
        
    @property
    def featuringClassifier(self) -> str:
        return self.__featuringClassifier

    @featuringClassifier.setter
    def featuringClassifier(self, featuringClassifier: str):
        self.__featuringClassifier = featuringClassifier

    @property
    def isStatic(self) -> str:
        return self.__isStatic

    @isStatic.setter
    def isStatic(self, isStatic: str):
        self.__isStatic = isStatic

class UMLModel_Transition(Namespace, RedefinableElement):

    def __init__(self, kind: str, container: str, redefinedTransition: str, guard: str, target: str, source: str, UMLModel_Transition: "UMLModel_Region" = None, UMLModel_Transition366: "UMLModel_Behavior" = None, UMLModel_Transition369: set["UMLModel_Trigger"] = None):
        self.kind = kind
        self.container = container
        self.redefinedTransition = redefinedTransition
        self.guard = guard
        self.target = target
        self.source = source
        self.UMLModel_Transition = UMLModel_Transition
        self.UMLModel_Transition366 = UMLModel_Transition366
        self.UMLModel_Transition369 = UMLModel_Transition369 if UMLModel_Transition369 is not None else set()
        
    @property
    def guard(self) -> str:
        return self.__guard

    @guard.setter
    def guard(self, guard: str):
        self.__guard = guard

    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def source(self) -> str:
        return self.__source

    @source.setter
    def source(self, source: str):
        self.__source = source

    @property
    def target(self) -> str:
        return self.__target

    @target.setter
    def target(self, target: str):
        self.__target = target

    @property
    def container(self) -> str:
        return self.__container

    @container.setter
    def container(self, container: str):
        self.__container = container

    @property
    def redefinedTransition(self) -> str:
        return self.__redefinedTransition

    @redefinedTransition.setter
    def redefinedTransition(self, redefinedTransition: str):
        self.__redefinedTransition = redefinedTransition

    @property
    def UMLModel_Transition366(self):
        return self.__UMLModel_Transition366

    @UMLModel_Transition366.setter
    def UMLModel_Transition366(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Transition__UMLModel_Transition366", None)
        self.__UMLModel_Transition366 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_Behavior367"):
                opp_val = getattr(old_value, "UMLModel_Behavior367", None)
                if opp_val == self:
                    setattr(old_value, "UMLModel_Behavior367", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_Behavior367"):
                opp_val = getattr(value, "UMLModel_Behavior367", None)
                setattr(value, "UMLModel_Behavior367", self)

    @property
    def UMLModel_Transition(self):
        return self.__UMLModel_Transition

    @UMLModel_Transition.setter
    def UMLModel_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Transition__UMLModel_Transition", None)
        self.__UMLModel_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_Region276"):
                opp_val = getattr(old_value, "UMLModel_Region276", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_Region276"):
                opp_val = getattr(value, "UMLModel_Region276", None)
                if opp_val is None:
                    setattr(value, "UMLModel_Region276", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UMLModel_Transition369(self):
        return self.__UMLModel_Transition369

    @UMLModel_Transition369.setter
    def UMLModel_Transition369(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Transition__UMLModel_Transition369", None)
        self.__UMLModel_Transition369 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UMLModel_Trigger370"):
                    opp_val = getattr(item, "UMLModel_Trigger370", None)
                    
                    if opp_val == self:
                        setattr(item, "UMLModel_Trigger370", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UMLModel_Trigger370"):
                    opp_val = getattr(item, "UMLModel_Trigger370", None)
                    
                    setattr(item, "UMLModel_Trigger370", self)
                    

class UMLModel_RedefinableTemplateSignature(TemplateSignature, RedefinableElement):

    def __init__(self, extendedSignature: str, inheritedParameter: str, classifier: str):
        self.extendedSignature = extendedSignature
        self.inheritedParameter = inheritedParameter
        self.classifier = classifier
        
    @property
    def extendedSignature(self) -> str:
        return self.__extendedSignature

    @extendedSignature.setter
    def extendedSignature(self, extendedSignature: str):
        self.__extendedSignature = extendedSignature

    @property
    def classifier(self) -> str:
        return self.__classifier

    @classifier.setter
    def classifier(self, classifier: str):
        self.__classifier = classifier

    @property
    def inheritedParameter(self) -> str:
        return self.__inheritedParameter

    @inheritedParameter.setter
    def inheritedParameter(self, inheritedParameter: str):
        self.__inheritedParameter = inheritedParameter

class UMLModel_State(Vertex, Namespace, RedefinableElement):

    def __init__(self, isComposite: str, isOrthogonal: str, isSimple: str, isSubmachineState: str, submachine: str, redefinedState: str, UMLModel_State321: "UMLModel_Behavior" = None, UMLModel_State324: set["UMLModel_Trigger"] = None, UMLModel_State327: set["UMLModel_Region"] = None, UMLModel_State: set["UMLModel_ConnectionPointReference"] = None, UMLModel_State310: set["UMLModel_Pseudostate"] = None, UMLModel_State312: "UMLModel_Constraint" = None, UMLModel_State315: "UMLModel_Behavior" = None, UMLModel_State318: "UMLModel_Behavior" = None):
        self.isComposite = isComposite
        self.isOrthogonal = isOrthogonal
        self.isSimple = isSimple
        self.isSubmachineState = isSubmachineState
        self.submachine = submachine
        self.redefinedState = redefinedState
        self.UMLModel_State321 = UMLModel_State321
        self.UMLModel_State324 = UMLModel_State324 if UMLModel_State324 is not None else set()
        self.UMLModel_State327 = UMLModel_State327 if UMLModel_State327 is not None else set()
        self.UMLModel_State = UMLModel_State if UMLModel_State is not None else set()
        self.UMLModel_State310 = UMLModel_State310 if UMLModel_State310 is not None else set()
        self.UMLModel_State312 = UMLModel_State312
        self.UMLModel_State315 = UMLModel_State315
        self.UMLModel_State318 = UMLModel_State318
        
    @property
    def isComposite(self) -> str:
        return self.__isComposite

    @isComposite.setter
    def isComposite(self, isComposite: str):
        self.__isComposite = isComposite

    @property
    def isSimple(self) -> str:
        return self.__isSimple

    @isSimple.setter
    def isSimple(self, isSimple: str):
        self.__isSimple = isSimple

    @property
    def isOrthogonal(self) -> str:
        return self.__isOrthogonal

    @isOrthogonal.setter
    def isOrthogonal(self, isOrthogonal: str):
        self.__isOrthogonal = isOrthogonal

    @property
    def isSubmachineState(self) -> str:
        return self.__isSubmachineState

    @isSubmachineState.setter
    def isSubmachineState(self, isSubmachineState: str):
        self.__isSubmachineState = isSubmachineState

    @property
    def redefinedState(self) -> str:
        return self.__redefinedState

    @redefinedState.setter
    def redefinedState(self, redefinedState: str):
        self.__redefinedState = redefinedState

    @property
    def submachine(self) -> str:
        return self.__submachine

    @submachine.setter
    def submachine(self, submachine: str):
        self.__submachine = submachine

    @property
    def UMLModel_State324(self):
        return self.__UMLModel_State324

    @UMLModel_State324.setter
    def UMLModel_State324(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_State__UMLModel_State324", None)
        self.__UMLModel_State324 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UMLModel_Trigger325"):
                    opp_val = getattr(item, "UMLModel_Trigger325", None)
                    
                    if opp_val == self:
                        setattr(item, "UMLModel_Trigger325", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UMLModel_Trigger325"):
                    opp_val = getattr(item, "UMLModel_Trigger325", None)
                    
                    setattr(item, "UMLModel_Trigger325", self)
                    

    @property
    def UMLModel_State(self):
        return self.__UMLModel_State

    @UMLModel_State.setter
    def UMLModel_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_State__UMLModel_State", None)
        self.__UMLModel_State = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UMLModel_ConnectionPointReference"):
                    opp_val = getattr(item, "UMLModel_ConnectionPointReference", None)
                    
                    if opp_val == self:
                        setattr(item, "UMLModel_ConnectionPointReference", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UMLModel_ConnectionPointReference"):
                    opp_val = getattr(item, "UMLModel_ConnectionPointReference", None)
                    
                    setattr(item, "UMLModel_ConnectionPointReference", self)
                    

    @property
    def UMLModel_State321(self):
        return self.__UMLModel_State321

    @UMLModel_State321.setter
    def UMLModel_State321(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_State__UMLModel_State321", None)
        self.__UMLModel_State321 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_Behavior322"):
                opp_val = getattr(old_value, "UMLModel_Behavior322", None)
                if opp_val == self:
                    setattr(old_value, "UMLModel_Behavior322", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_Behavior322"):
                opp_val = getattr(value, "UMLModel_Behavior322", None)
                setattr(value, "UMLModel_Behavior322", self)

    @property
    def UMLModel_State318(self):
        return self.__UMLModel_State318

    @UMLModel_State318.setter
    def UMLModel_State318(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_State__UMLModel_State318", None)
        self.__UMLModel_State318 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_Behavior319"):
                opp_val = getattr(old_value, "UMLModel_Behavior319", None)
                if opp_val == self:
                    setattr(old_value, "UMLModel_Behavior319", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_Behavior319"):
                opp_val = getattr(value, "UMLModel_Behavior319", None)
                setattr(value, "UMLModel_Behavior319", self)

    @property
    def UMLModel_State315(self):
        return self.__UMLModel_State315

    @UMLModel_State315.setter
    def UMLModel_State315(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_State__UMLModel_State315", None)
        self.__UMLModel_State315 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_Behavior316"):
                opp_val = getattr(old_value, "UMLModel_Behavior316", None)
                if opp_val == self:
                    setattr(old_value, "UMLModel_Behavior316", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_Behavior316"):
                opp_val = getattr(value, "UMLModel_Behavior316", None)
                setattr(value, "UMLModel_Behavior316", self)

    @property
    def UMLModel_State312(self):
        return self.__UMLModel_State312

    @UMLModel_State312.setter
    def UMLModel_State312(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_State__UMLModel_State312", None)
        self.__UMLModel_State312 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_Constraint313"):
                opp_val = getattr(old_value, "UMLModel_Constraint313", None)
                if opp_val == self:
                    setattr(old_value, "UMLModel_Constraint313", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_Constraint313"):
                opp_val = getattr(value, "UMLModel_Constraint313", None)
                setattr(value, "UMLModel_Constraint313", self)

    @property
    def UMLModel_State310(self):
        return self.__UMLModel_State310

    @UMLModel_State310.setter
    def UMLModel_State310(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_State__UMLModel_State310", None)
        self.__UMLModel_State310 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UMLModel_Pseudostate"):
                    opp_val = getattr(item, "UMLModel_Pseudostate", None)
                    
                    if opp_val == self:
                        setattr(item, "UMLModel_Pseudostate", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UMLModel_Pseudostate"):
                    opp_val = getattr(item, "UMLModel_Pseudostate", None)
                    
                    setattr(item, "UMLModel_Pseudostate", self)
                    

    @property
    def UMLModel_State327(self):
        return self.__UMLModel_State327

    @UMLModel_State327.setter
    def UMLModel_State327(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_State__UMLModel_State327", None)
        self.__UMLModel_State327 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UMLModel_Region328"):
                    opp_val = getattr(item, "UMLModel_Region328", None)
                    
                    if opp_val == self:
                        setattr(item, "UMLModel_Region328", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UMLModel_Region328"):
                    opp_val = getattr(item, "UMLModel_Region328", None)
                    
                    setattr(item, "UMLModel_Region328", self)
                    

class UMLModel_ExtensionPoint(RedefinableElement):

    def __init__(self, useCase: str, UMLModel_ExtensionPoint: "UMLModel_UseCase" = None):
        self.useCase = useCase
        self.UMLModel_ExtensionPoint = UMLModel_ExtensionPoint
        
    @property
    def useCase(self) -> str:
        return self.__useCase

    @useCase.setter
    def useCase(self, useCase: str):
        self.__useCase = useCase

    @property
    def UMLModel_ExtensionPoint(self):
        return self.__UMLModel_ExtensionPoint

    @UMLModel_ExtensionPoint.setter
    def UMLModel_ExtensionPoint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_ExtensionPoint__UMLModel_ExtensionPoint", None)
        self.__UMLModel_ExtensionPoint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_UseCase382"):
                opp_val = getattr(old_value, "UMLModel_UseCase382", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_UseCase382"):
                opp_val = getattr(value, "UMLModel_UseCase382", None)
                if opp_val is None:
                    setattr(value, "UMLModel_UseCase382", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class UMLModel_Classifier(Type, Namespace, RedefinableElement, TemplateableElement):

    def __init__(self, isAbstract: str, powertypeExtent: str, feature: str, inheritedMember: str, redefinedClassifier: str, general: str, representation: str, attribute: str, useCase: str, UMLModel_Classifier: "UMLModel_Class" = None, UMLModel_Classifier71: set["UMLModel_Generalization"] = None, UMLModel_Classifier73: set["UMLModel_Substitution"] = None, UMLModel_Classifier77: set["UMLModel_UseCase"] = None, UMLModel_Classifier75: set["UMLModel_CollaborationUse"] = None, UMLModel_Classifier126: "UMLModel_Interface" = None):
        self.isAbstract = isAbstract
        self.powertypeExtent = powertypeExtent
        self.feature = feature
        self.inheritedMember = inheritedMember
        self.redefinedClassifier = redefinedClassifier
        self.general = general
        self.representation = representation
        self.attribute = attribute
        self.useCase = useCase
        self.UMLModel_Classifier = UMLModel_Classifier
        self.UMLModel_Classifier71 = UMLModel_Classifier71 if UMLModel_Classifier71 is not None else set()
        self.UMLModel_Classifier73 = UMLModel_Classifier73 if UMLModel_Classifier73 is not None else set()
        self.UMLModel_Classifier77 = UMLModel_Classifier77 if UMLModel_Classifier77 is not None else set()
        self.UMLModel_Classifier75 = UMLModel_Classifier75 if UMLModel_Classifier75 is not None else set()
        self.UMLModel_Classifier126 = UMLModel_Classifier126
        
    @property
    def powertypeExtent(self) -> str:
        return self.__powertypeExtent

    @powertypeExtent.setter
    def powertypeExtent(self, powertypeExtent: str):
        self.__powertypeExtent = powertypeExtent

    @property
    def useCase(self) -> str:
        return self.__useCase

    @useCase.setter
    def useCase(self, useCase: str):
        self.__useCase = useCase

    @property
    def attribute(self) -> str:
        return self.__attribute

    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def representation(self) -> str:
        return self.__representation

    @representation.setter
    def representation(self, representation: str):
        self.__representation = representation

    @property
    def isAbstract(self) -> str:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: str):
        self.__isAbstract = isAbstract

    @property
    def general(self) -> str:
        return self.__general

    @general.setter
    def general(self, general: str):
        self.__general = general

    @property
    def inheritedMember(self) -> str:
        return self.__inheritedMember

    @inheritedMember.setter
    def inheritedMember(self, inheritedMember: str):
        self.__inheritedMember = inheritedMember

    @property
    def feature(self) -> str:
        return self.__feature

    @feature.setter
    def feature(self, feature: str):
        self.__feature = feature

    @property
    def redefinedClassifier(self) -> str:
        return self.__redefinedClassifier

    @redefinedClassifier.setter
    def redefinedClassifier(self, redefinedClassifier: str):
        self.__redefinedClassifier = redefinedClassifier

    @property
    def UMLModel_Classifier71(self):
        return self.__UMLModel_Classifier71

    @UMLModel_Classifier71.setter
    def UMLModel_Classifier71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Classifier__UMLModel_Classifier71", None)
        self.__UMLModel_Classifier71 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UMLModel_Generalization"):
                    opp_val = getattr(item, "UMLModel_Generalization", None)
                    
                    if opp_val == self:
                        setattr(item, "UMLModel_Generalization", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UMLModel_Generalization"):
                    opp_val = getattr(item, "UMLModel_Generalization", None)
                    
                    setattr(item, "UMLModel_Generalization", self)
                    

    @property
    def UMLModel_Classifier77(self):
        return self.__UMLModel_Classifier77

    @UMLModel_Classifier77.setter
    def UMLModel_Classifier77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Classifier__UMLModel_Classifier77", None)
        self.__UMLModel_Classifier77 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UMLModel_UseCase"):
                    opp_val = getattr(item, "UMLModel_UseCase", None)
                    
                    if opp_val == self:
                        setattr(item, "UMLModel_UseCase", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UMLModel_UseCase"):
                    opp_val = getattr(item, "UMLModel_UseCase", None)
                    
                    setattr(item, "UMLModel_UseCase", self)
                    

    @property
    def UMLModel_Classifier73(self):
        return self.__UMLModel_Classifier73

    @UMLModel_Classifier73.setter
    def UMLModel_Classifier73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Classifier__UMLModel_Classifier73", None)
        self.__UMLModel_Classifier73 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UMLModel_Substitution"):
                    opp_val = getattr(item, "UMLModel_Substitution", None)
                    
                    if opp_val == self:
                        setattr(item, "UMLModel_Substitution", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UMLModel_Substitution"):
                    opp_val = getattr(item, "UMLModel_Substitution", None)
                    
                    setattr(item, "UMLModel_Substitution", self)
                    

    @property
    def UMLModel_Classifier(self):
        return self.__UMLModel_Classifier

    @UMLModel_Classifier.setter
    def UMLModel_Classifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Classifier__UMLModel_Classifier", None)
        self.__UMLModel_Classifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_Class"):
                opp_val = getattr(old_value, "UMLModel_Class", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_Class"):
                opp_val = getattr(value, "UMLModel_Class", None)
                if opp_val is None:
                    setattr(value, "UMLModel_Class", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UMLModel_Classifier75(self):
        return self.__UMLModel_Classifier75

    @UMLModel_Classifier75.setter
    def UMLModel_Classifier75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Classifier__UMLModel_Classifier75", None)
        self.__UMLModel_Classifier75 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UMLModel_CollaborationUse"):
                    opp_val = getattr(item, "UMLModel_CollaborationUse", None)
                    
                    if opp_val == self:
                        setattr(item, "UMLModel_CollaborationUse", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UMLModel_CollaborationUse"):
                    opp_val = getattr(item, "UMLModel_CollaborationUse", None)
                    
                    setattr(item, "UMLModel_CollaborationUse", self)
                    

    @property
    def UMLModel_Classifier126(self):
        return self.__UMLModel_Classifier126

    @UMLModel_Classifier126.setter
    def UMLModel_Classifier126(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Classifier__UMLModel_Classifier126", None)
        self.__UMLModel_Classifier126 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_Interface125"):
                opp_val = getattr(old_value, "UMLModel_Interface125", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_Interface125"):
                opp_val = getattr(value, "UMLModel_Interface125", None)
                if opp_val is None:
                    setattr(value, "UMLModel_Interface125", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class UMLModel_ActivityNode(RedefinableElement):

    def __init__(self, inInterruptibleRegion: str, outgoing: str, incoming: str, inPartition: str, inGroup: str, redefinedNode: str, activity: str, inStructuredNode: str, UMLModel_ActivityNode29: "UMLModel_ActivityGroup" = None, UMLModel_ActivityNode: "UMLModel_Activity" = None, UMLModel_ActivityNode303: "UMLModel_StructuredActivityNode" = None):
        self.inInterruptibleRegion = inInterruptibleRegion
        self.outgoing = outgoing
        self.incoming = incoming
        self.inPartition = inPartition
        self.inGroup = inGroup
        self.redefinedNode = redefinedNode
        self.activity = activity
        self.inStructuredNode = inStructuredNode
        self.UMLModel_ActivityNode29 = UMLModel_ActivityNode29
        self.UMLModel_ActivityNode = UMLModel_ActivityNode
        self.UMLModel_ActivityNode303 = UMLModel_ActivityNode303
        
    @property
    def redefinedNode(self) -> str:
        return self.__redefinedNode

    @redefinedNode.setter
    def redefinedNode(self, redefinedNode: str):
        self.__redefinedNode = redefinedNode

    @property
    def incoming(self) -> str:
        return self.__incoming

    @incoming.setter
    def incoming(self, incoming: str):
        self.__incoming = incoming

    @property
    def inPartition(self) -> str:
        return self.__inPartition

    @inPartition.setter
    def inPartition(self, inPartition: str):
        self.__inPartition = inPartition

    @property
    def inInterruptibleRegion(self) -> str:
        return self.__inInterruptibleRegion

    @inInterruptibleRegion.setter
    def inInterruptibleRegion(self, inInterruptibleRegion: str):
        self.__inInterruptibleRegion = inInterruptibleRegion

    @property
    def inGroup(self) -> str:
        return self.__inGroup

    @inGroup.setter
    def inGroup(self, inGroup: str):
        self.__inGroup = inGroup

    @property
    def activity(self) -> str:
        return self.__activity

    @activity.setter
    def activity(self, activity: str):
        self.__activity = activity

    @property
    def inStructuredNode(self) -> str:
        return self.__inStructuredNode

    @inStructuredNode.setter
    def inStructuredNode(self, inStructuredNode: str):
        self.__inStructuredNode = inStructuredNode

    @property
    def outgoing(self) -> str:
        return self.__outgoing

    @outgoing.setter
    def outgoing(self, outgoing: str):
        self.__outgoing = outgoing

    @property
    def UMLModel_ActivityNode303(self):
        return self.__UMLModel_ActivityNode303

    @UMLModel_ActivityNode303.setter
    def UMLModel_ActivityNode303(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_ActivityNode__UMLModel_ActivityNode303", None)
        self.__UMLModel_ActivityNode303 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_StructuredActivityNode302"):
                opp_val = getattr(old_value, "UMLModel_StructuredActivityNode302", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_StructuredActivityNode302"):
                opp_val = getattr(value, "UMLModel_StructuredActivityNode302", None)
                if opp_val is None:
                    setattr(value, "UMLModel_StructuredActivityNode302", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UMLModel_ActivityNode(self):
        return self.__UMLModel_ActivityNode

    @UMLModel_ActivityNode.setter
    def UMLModel_ActivityNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_ActivityNode__UMLModel_ActivityNode", None)
        self.__UMLModel_ActivityNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_Activity14"):
                opp_val = getattr(old_value, "UMLModel_Activity14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_Activity14"):
                opp_val = getattr(value, "UMLModel_Activity14", None)
                if opp_val is None:
                    setattr(value, "UMLModel_Activity14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UMLModel_ActivityNode29(self):
        return self.__UMLModel_ActivityNode29

    @UMLModel_ActivityNode29.setter
    def UMLModel_ActivityNode29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_ActivityNode__UMLModel_ActivityNode29", None)
        self.__UMLModel_ActivityNode29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_ActivityGroup28"):
                opp_val = getattr(old_value, "UMLModel_ActivityGroup28", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_ActivityGroup28"):
                opp_val = getattr(value, "UMLModel_ActivityGroup28", None)
                if opp_val is None:
                    setattr(value, "UMLModel_ActivityGroup28", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class UMLModel_ActivityGroup(Element):

    def __init__(self, subgroup: str, superGroup: str, inActivity: str, UMLModel_ActivityGroup: "UMLModel_Activity" = None, UMLModel_ActivityGroup25: set["UMLModel_ActivityEdge"] = None, UMLModel_ActivityGroup28: set["UMLModel_ActivityNode"] = None):
        self.subgroup = subgroup
        self.superGroup = superGroup
        self.inActivity = inActivity
        self.UMLModel_ActivityGroup = UMLModel_ActivityGroup
        self.UMLModel_ActivityGroup25 = UMLModel_ActivityGroup25 if UMLModel_ActivityGroup25 is not None else set()
        self.UMLModel_ActivityGroup28 = UMLModel_ActivityGroup28 if UMLModel_ActivityGroup28 is not None else set()
        
    @property
    def inActivity(self) -> str:
        return self.__inActivity

    @inActivity.setter
    def inActivity(self, inActivity: str):
        self.__inActivity = inActivity

    @property
    def superGroup(self) -> str:
        return self.__superGroup

    @superGroup.setter
    def superGroup(self, superGroup: str):
        self.__superGroup = superGroup

    @property
    def subgroup(self) -> str:
        return self.__subgroup

    @subgroup.setter
    def subgroup(self, subgroup: str):
        self.__subgroup = subgroup

    @property
    def UMLModel_ActivityGroup28(self):
        return self.__UMLModel_ActivityGroup28

    @UMLModel_ActivityGroup28.setter
    def UMLModel_ActivityGroup28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_ActivityGroup__UMLModel_ActivityGroup28", None)
        self.__UMLModel_ActivityGroup28 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UMLModel_ActivityNode29"):
                    opp_val = getattr(item, "UMLModel_ActivityNode29", None)
                    
                    if opp_val == self:
                        setattr(item, "UMLModel_ActivityNode29", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UMLModel_ActivityNode29"):
                    opp_val = getattr(item, "UMLModel_ActivityNode29", None)
                    
                    setattr(item, "UMLModel_ActivityNode29", self)
                    

    @property
    def UMLModel_ActivityGroup(self):
        return self.__UMLModel_ActivityGroup

    @UMLModel_ActivityGroup.setter
    def UMLModel_ActivityGroup(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_ActivityGroup__UMLModel_ActivityGroup", None)
        self.__UMLModel_ActivityGroup = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_Activity18"):
                opp_val = getattr(old_value, "UMLModel_Activity18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_Activity18"):
                opp_val = getattr(value, "UMLModel_Activity18", None)
                if opp_val is None:
                    setattr(value, "UMLModel_Activity18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UMLModel_ActivityGroup25(self):
        return self.__UMLModel_ActivityGroup25

    @UMLModel_ActivityGroup25.setter
    def UMLModel_ActivityGroup25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_ActivityGroup__UMLModel_ActivityGroup25", None)
        self.__UMLModel_ActivityGroup25 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UMLModel_ActivityEdge26"):
                    opp_val = getattr(item, "UMLModel_ActivityEdge26", None)
                    
                    if opp_val == self:
                        setattr(item, "UMLModel_ActivityEdge26", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UMLModel_ActivityEdge26"):
                    opp_val = getattr(item, "UMLModel_ActivityEdge26", None)
                    
                    setattr(item, "UMLModel_ActivityEdge26", self)
                    

class UMLModel_ActivityEdge(RedefinableElement):

    def __init__(self, source: str, target: str, redefinedEdge: str, inPartition: str, interrupts: str, inGroup: str, activity: str, inStructuredNode: str, UMLModel_ActivityEdge: "UMLModel_Activity" = None, UMLModel_ActivityEdge20: "UMLModel_ValueSpecification" = None, UMLModel_ActivityEdge22: "UMLModel_ValueSpecification" = None, UMLModel_ActivityEdge26: "UMLModel_ActivityGroup" = None, UMLModel_ActivityEdge300: "UMLModel_StructuredActivityNode" = None):
        self.source = source
        self.target = target
        self.redefinedEdge = redefinedEdge
        self.inPartition = inPartition
        self.interrupts = interrupts
        self.inGroup = inGroup
        self.activity = activity
        self.inStructuredNode = inStructuredNode
        self.UMLModel_ActivityEdge = UMLModel_ActivityEdge
        self.UMLModel_ActivityEdge20 = UMLModel_ActivityEdge20
        self.UMLModel_ActivityEdge22 = UMLModel_ActivityEdge22
        self.UMLModel_ActivityEdge26 = UMLModel_ActivityEdge26
        self.UMLModel_ActivityEdge300 = UMLModel_ActivityEdge300
        
    @property
    def activity(self) -> str:
        return self.__activity

    @activity.setter
    def activity(self, activity: str):
        self.__activity = activity

    @property
    def source(self) -> str:
        return self.__source

    @source.setter
    def source(self, source: str):
        self.__source = source

    @property
    def target(self) -> str:
        return self.__target

    @target.setter
    def target(self, target: str):
        self.__target = target

    @property
    def inGroup(self) -> str:
        return self.__inGroup

    @inGroup.setter
    def inGroup(self, inGroup: str):
        self.__inGroup = inGroup

    @property
    def inPartition(self) -> str:
        return self.__inPartition

    @inPartition.setter
    def inPartition(self, inPartition: str):
        self.__inPartition = inPartition

    @property
    def redefinedEdge(self) -> str:
        return self.__redefinedEdge

    @redefinedEdge.setter
    def redefinedEdge(self, redefinedEdge: str):
        self.__redefinedEdge = redefinedEdge

    @property
    def inStructuredNode(self) -> str:
        return self.__inStructuredNode

    @inStructuredNode.setter
    def inStructuredNode(self, inStructuredNode: str):
        self.__inStructuredNode = inStructuredNode

    @property
    def interrupts(self) -> str:
        return self.__interrupts

    @interrupts.setter
    def interrupts(self, interrupts: str):
        self.__interrupts = interrupts

    @property
    def UMLModel_ActivityEdge26(self):
        return self.__UMLModel_ActivityEdge26

    @UMLModel_ActivityEdge26.setter
    def UMLModel_ActivityEdge26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_ActivityEdge__UMLModel_ActivityEdge26", None)
        self.__UMLModel_ActivityEdge26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_ActivityGroup25"):
                opp_val = getattr(old_value, "UMLModel_ActivityGroup25", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_ActivityGroup25"):
                opp_val = getattr(value, "UMLModel_ActivityGroup25", None)
                if opp_val is None:
                    setattr(value, "UMLModel_ActivityGroup25", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UMLModel_ActivityEdge22(self):
        return self.__UMLModel_ActivityEdge22

    @UMLModel_ActivityEdge22.setter
    def UMLModel_ActivityEdge22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_ActivityEdge__UMLModel_ActivityEdge22", None)
        self.__UMLModel_ActivityEdge22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_ValueSpecification23"):
                opp_val = getattr(old_value, "UMLModel_ValueSpecification23", None)
                if opp_val == self:
                    setattr(old_value, "UMLModel_ValueSpecification23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_ValueSpecification23"):
                opp_val = getattr(value, "UMLModel_ValueSpecification23", None)
                setattr(value, "UMLModel_ValueSpecification23", self)

    @property
    def UMLModel_ActivityEdge(self):
        return self.__UMLModel_ActivityEdge

    @UMLModel_ActivityEdge.setter
    def UMLModel_ActivityEdge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_ActivityEdge__UMLModel_ActivityEdge", None)
        self.__UMLModel_ActivityEdge = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_Activity16"):
                opp_val = getattr(old_value, "UMLModel_Activity16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_Activity16"):
                opp_val = getattr(value, "UMLModel_Activity16", None)
                if opp_val is None:
                    setattr(value, "UMLModel_Activity16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UMLModel_ActivityEdge300(self):
        return self.__UMLModel_ActivityEdge300

    @UMLModel_ActivityEdge300.setter
    def UMLModel_ActivityEdge300(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_ActivityEdge__UMLModel_ActivityEdge300", None)
        self.__UMLModel_ActivityEdge300 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_StructuredActivityNode299"):
                opp_val = getattr(old_value, "UMLModel_StructuredActivityNode299", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_StructuredActivityNode299"):
                opp_val = getattr(value, "UMLModel_StructuredActivityNode299", None)
                if opp_val is None:
                    setattr(value, "UMLModel_StructuredActivityNode299", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UMLModel_ActivityEdge20(self):
        return self.__UMLModel_ActivityEdge20

    @UMLModel_ActivityEdge20.setter
    def UMLModel_ActivityEdge20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_ActivityEdge__UMLModel_ActivityEdge20", None)
        self.__UMLModel_ActivityEdge20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_ValueSpecification"):
                opp_val = getattr(old_value, "UMLModel_ValueSpecification", None)
                if opp_val == self:
                    setattr(old_value, "UMLModel_ValueSpecification", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_ValueSpecification"):
                opp_val = getattr(value, "UMLModel_ValueSpecification", None)
                setattr(value, "UMLModel_ValueSpecification", self)

class UMLModel_Variable(MultiplicityElement, ConnectableElement):

    def __init__(self, scope: str, activityScope: str, UMLModel_Variable: "UMLModel_Activity" = None, UMLModel_Variable297: "UMLModel_StructuredActivityNode" = None):
        self.scope = scope
        self.activityScope = activityScope
        self.UMLModel_Variable = UMLModel_Variable
        self.UMLModel_Variable297 = UMLModel_Variable297
        
    @property
    def activityScope(self) -> str:
        return self.__activityScope

    @activityScope.setter
    def activityScope(self, activityScope: str):
        self.__activityScope = activityScope

    @property
    def scope(self) -> str:
        return self.__scope

    @scope.setter
    def scope(self, scope: str):
        self.__scope = scope

    @property
    def UMLModel_Variable(self):
        return self.__UMLModel_Variable

    @UMLModel_Variable.setter
    def UMLModel_Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Variable__UMLModel_Variable", None)
        self.__UMLModel_Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_Activity"):
                opp_val = getattr(old_value, "UMLModel_Activity", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_Activity"):
                opp_val = getattr(value, "UMLModel_Activity", None)
                if opp_val is None:
                    setattr(value, "UMLModel_Activity", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UMLModel_Variable297(self):
        return self.__UMLModel_Variable297

    @UMLModel_Variable297.setter
    def UMLModel_Variable297(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Variable__UMLModel_Variable297", None)
        self.__UMLModel_Variable297 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_StructuredActivityNode"):
                opp_val = getattr(old_value, "UMLModel_StructuredActivityNode", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_StructuredActivityNode"):
                opp_val = getattr(value, "UMLModel_StructuredActivityNode", None)
                if opp_val is None:
                    setattr(value, "UMLModel_StructuredActivityNode", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Behavior:

    pass
class UMLModel_StateMachine(Behavior):

    def __init__(self, submachineState: str, extendedStateMachine: str, UMLModel_StateMachine: set["UMLModel_Region"] = None, UMLModel_StateMachine332: set["UMLModel_Pseudostate"] = None):
        self.submachineState = submachineState
        self.extendedStateMachine = extendedStateMachine
        self.UMLModel_StateMachine = UMLModel_StateMachine if UMLModel_StateMachine is not None else set()
        self.UMLModel_StateMachine332 = UMLModel_StateMachine332 if UMLModel_StateMachine332 is not None else set()
        
    @property
    def extendedStateMachine(self) -> str:
        return self.__extendedStateMachine

    @extendedStateMachine.setter
    def extendedStateMachine(self, extendedStateMachine: str):
        self.__extendedStateMachine = extendedStateMachine

    @property
    def submachineState(self) -> str:
        return self.__submachineState

    @submachineState.setter
    def submachineState(self, submachineState: str):
        self.__submachineState = submachineState

    @property
    def UMLModel_StateMachine332(self):
        return self.__UMLModel_StateMachine332

    @UMLModel_StateMachine332.setter
    def UMLModel_StateMachine332(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_StateMachine__UMLModel_StateMachine332", None)
        self.__UMLModel_StateMachine332 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UMLModel_Pseudostate333"):
                    opp_val = getattr(item, "UMLModel_Pseudostate333", None)
                    
                    if opp_val == self:
                        setattr(item, "UMLModel_Pseudostate333", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UMLModel_Pseudostate333"):
                    opp_val = getattr(item, "UMLModel_Pseudostate333", None)
                    
                    setattr(item, "UMLModel_Pseudostate333", self)
                    

    @property
    def UMLModel_StateMachine(self):
        return self.__UMLModel_StateMachine

    @UMLModel_StateMachine.setter
    def UMLModel_StateMachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_StateMachine__UMLModel_StateMachine", None)
        self.__UMLModel_StateMachine = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UMLModel_Region330"):
                    opp_val = getattr(item, "UMLModel_Region330", None)
                    
                    if opp_val == self:
                        setattr(item, "UMLModel_Region330", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UMLModel_Region330"):
                    opp_val = getattr(item, "UMLModel_Region330", None)
                    
                    setattr(item, "UMLModel_Region330", self)
                    

class UMLModel_OpaqueBehavior(Behavior):

    def __init__(self, body: str, language: str):
        self.body = body
        self.language = language
        
    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

    @property
    def language(self) -> str:
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language

class UMLModel_Interaction(InteractionFragment, Behavior):

    pass
class UMLModel_Activity(Behavior):

    def __init__(self, isReadOnly: str, isSingleExecution: str, structuredNode: str, partition: str, UMLModel_Activity: set["UMLModel_Variable"] = None, UMLModel_Activity16: set["UMLModel_ActivityEdge"] = None, UMLModel_Activity18: set["UMLModel_ActivityGroup"] = None, UMLModel_Activity14: set["UMLModel_ActivityNode"] = None):
        self.isReadOnly = isReadOnly
        self.isSingleExecution = isSingleExecution
        self.structuredNode = structuredNode
        self.partition = partition
        self.UMLModel_Activity = UMLModel_Activity if UMLModel_Activity is not None else set()
        self.UMLModel_Activity16 = UMLModel_Activity16 if UMLModel_Activity16 is not None else set()
        self.UMLModel_Activity18 = UMLModel_Activity18 if UMLModel_Activity18 is not None else set()
        self.UMLModel_Activity14 = UMLModel_Activity14 if UMLModel_Activity14 is not None else set()
        
    @property
    def isSingleExecution(self) -> str:
        return self.__isSingleExecution

    @isSingleExecution.setter
    def isSingleExecution(self, isSingleExecution: str):
        self.__isSingleExecution = isSingleExecution

    @property
    def partition(self) -> str:
        return self.__partition

    @partition.setter
    def partition(self, partition: str):
        self.__partition = partition

    @property
    def structuredNode(self) -> str:
        return self.__structuredNode

    @structuredNode.setter
    def structuredNode(self, structuredNode: str):
        self.__structuredNode = structuredNode

    @property
    def isReadOnly(self) -> str:
        return self.__isReadOnly

    @isReadOnly.setter
    def isReadOnly(self, isReadOnly: str):
        self.__isReadOnly = isReadOnly

    @property
    def UMLModel_Activity16(self):
        return self.__UMLModel_Activity16

    @UMLModel_Activity16.setter
    def UMLModel_Activity16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Activity__UMLModel_Activity16", None)
        self.__UMLModel_Activity16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UMLModel_ActivityEdge"):
                    opp_val = getattr(item, "UMLModel_ActivityEdge", None)
                    
                    if opp_val == self:
                        setattr(item, "UMLModel_ActivityEdge", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UMLModel_ActivityEdge"):
                    opp_val = getattr(item, "UMLModel_ActivityEdge", None)
                    
                    setattr(item, "UMLModel_ActivityEdge", self)
                    

    @property
    def UMLModel_Activity(self):
        return self.__UMLModel_Activity

    @UMLModel_Activity.setter
    def UMLModel_Activity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Activity__UMLModel_Activity", None)
        self.__UMLModel_Activity = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UMLModel_Variable"):
                    opp_val = getattr(item, "UMLModel_Variable", None)
                    
                    if opp_val == self:
                        setattr(item, "UMLModel_Variable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UMLModel_Variable"):
                    opp_val = getattr(item, "UMLModel_Variable", None)
                    
                    setattr(item, "UMLModel_Variable", self)
                    

    @property
    def UMLModel_Activity18(self):
        return self.__UMLModel_Activity18

    @UMLModel_Activity18.setter
    def UMLModel_Activity18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Activity__UMLModel_Activity18", None)
        self.__UMLModel_Activity18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UMLModel_ActivityGroup"):
                    opp_val = getattr(item, "UMLModel_ActivityGroup", None)
                    
                    if opp_val == self:
                        setattr(item, "UMLModel_ActivityGroup", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UMLModel_ActivityGroup"):
                    opp_val = getattr(item, "UMLModel_ActivityGroup", None)
                    
                    setattr(item, "UMLModel_ActivityGroup", self)
                    

    @property
    def UMLModel_Activity14(self):
        return self.__UMLModel_Activity14

    @UMLModel_Activity14.setter
    def UMLModel_Activity14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Activity__UMLModel_Activity14", None)
        self.__UMLModel_Activity14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UMLModel_ActivityNode"):
                    opp_val = getattr(item, "UMLModel_ActivityNode", None)
                    
                    if opp_val == self:
                        setattr(item, "UMLModel_ActivityNode", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UMLModel_ActivityNode"):
                    opp_val = getattr(item, "UMLModel_ActivityNode", None)
                    
                    setattr(item, "UMLModel_ActivityNode", self)
                    

class InputPin:

    pass
class UMLModel_ValuePin(InputPin):

    pass
class UMLModel_ActionInputPin(InputPin):

    pass
class ExecutionSpecification:

    pass
class UMLModel_BehaviorExecutionSpecification(ExecutionSpecification):

    def __init__(self, behavior: str):
        self.behavior = behavior
        
    @property
    def behavior(self) -> str:
        return self.__behavior

    @behavior.setter
    def behavior(self, behavior: str):
        self.__behavior = behavior

class UMLModel_ActionExecutionSpecification(ExecutionSpecification):

    def __init__(self, action: str):
        self.action = action
        
    @property
    def action(self) -> str:
        return self.__action

    @action.setter
    def action(self, action: str):
        self.__action = action

class UMLModel_Constraint(PackageableElement):

    def __init__(self, constrainedElement: str, context: str, UMLModel_Constraint: "UMLModel_Action" = None, UMLModel_Constraint9: "UMLModel_Action" = None, UMLModel_Constraint93: "UMLModel_ValueSpecification" = None, UMLModel_Constraint116: "UMLModel_Extend" = None, UMLModel_Constraint198: "UMLModel_Namespace" = None, UMLModel_Constraint222: "UMLModel_ParameterSet" = None, UMLModel_Constraint285: "UMLModel_StateInvariant" = None, UMLModel_Constraint313: "UMLModel_State" = None):
        self.constrainedElement = constrainedElement
        self.context = context
        self.UMLModel_Constraint = UMLModel_Constraint
        self.UMLModel_Constraint9 = UMLModel_Constraint9
        self.UMLModel_Constraint93 = UMLModel_Constraint93
        self.UMLModel_Constraint116 = UMLModel_Constraint116
        self.UMLModel_Constraint198 = UMLModel_Constraint198
        self.UMLModel_Constraint222 = UMLModel_Constraint222
        self.UMLModel_Constraint285 = UMLModel_Constraint285
        self.UMLModel_Constraint313 = UMLModel_Constraint313
        
    @property
    def constrainedElement(self) -> str:
        return self.__constrainedElement

    @constrainedElement.setter
    def constrainedElement(self, constrainedElement: str):
        self.__constrainedElement = constrainedElement

    @property
    def context(self) -> str:
        return self.__context

    @context.setter
    def context(self, context: str):
        self.__context = context

    @property
    def UMLModel_Constraint222(self):
        return self.__UMLModel_Constraint222

    @UMLModel_Constraint222.setter
    def UMLModel_Constraint222(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Constraint__UMLModel_Constraint222", None)
        self.__UMLModel_Constraint222 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_ParameterSet221"):
                opp_val = getattr(old_value, "UMLModel_ParameterSet221", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_ParameterSet221"):
                opp_val = getattr(value, "UMLModel_ParameterSet221", None)
                if opp_val is None:
                    setattr(value, "UMLModel_ParameterSet221", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UMLModel_Constraint93(self):
        return self.__UMLModel_Constraint93

    @UMLModel_Constraint93.setter
    def UMLModel_Constraint93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Constraint__UMLModel_Constraint93", None)
        self.__UMLModel_Constraint93 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_ValueSpecification94"):
                opp_val = getattr(old_value, "UMLModel_ValueSpecification94", None)
                if opp_val == self:
                    setattr(old_value, "UMLModel_ValueSpecification94", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_ValueSpecification94"):
                opp_val = getattr(value, "UMLModel_ValueSpecification94", None)
                setattr(value, "UMLModel_ValueSpecification94", self)

    @property
    def UMLModel_Constraint9(self):
        return self.__UMLModel_Constraint9

    @UMLModel_Constraint9.setter
    def UMLModel_Constraint9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Constraint__UMLModel_Constraint9", None)
        self.__UMLModel_Constraint9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_Action8"):
                opp_val = getattr(old_value, "UMLModel_Action8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_Action8"):
                opp_val = getattr(value, "UMLModel_Action8", None)
                if opp_val is None:
                    setattr(value, "UMLModel_Action8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UMLModel_Constraint198(self):
        return self.__UMLModel_Constraint198

    @UMLModel_Constraint198.setter
    def UMLModel_Constraint198(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Constraint__UMLModel_Constraint198", None)
        self.__UMLModel_Constraint198 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_Namespace197"):
                opp_val = getattr(old_value, "UMLModel_Namespace197", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_Namespace197"):
                opp_val = getattr(value, "UMLModel_Namespace197", None)
                if opp_val is None:
                    setattr(value, "UMLModel_Namespace197", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UMLModel_Constraint(self):
        return self.__UMLModel_Constraint

    @UMLModel_Constraint.setter
    def UMLModel_Constraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Constraint__UMLModel_Constraint", None)
        self.__UMLModel_Constraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_Action"):
                opp_val = getattr(old_value, "UMLModel_Action", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_Action"):
                opp_val = getattr(value, "UMLModel_Action", None)
                if opp_val is None:
                    setattr(value, "UMLModel_Action", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UMLModel_Constraint313(self):
        return self.__UMLModel_Constraint313

    @UMLModel_Constraint313.setter
    def UMLModel_Constraint313(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Constraint__UMLModel_Constraint313", None)
        self.__UMLModel_Constraint313 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_State312"):
                opp_val = getattr(old_value, "UMLModel_State312", None)
                if opp_val == self:
                    setattr(old_value, "UMLModel_State312", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_State312"):
                opp_val = getattr(value, "UMLModel_State312", None)
                setattr(value, "UMLModel_State312", self)

    @property
    def UMLModel_Constraint285(self):
        return self.__UMLModel_Constraint285

    @UMLModel_Constraint285.setter
    def UMLModel_Constraint285(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Constraint__UMLModel_Constraint285", None)
        self.__UMLModel_Constraint285 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_StateInvariant"):
                opp_val = getattr(old_value, "UMLModel_StateInvariant", None)
                if opp_val == self:
                    setattr(old_value, "UMLModel_StateInvariant", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_StateInvariant"):
                opp_val = getattr(value, "UMLModel_StateInvariant", None)
                setattr(value, "UMLModel_StateInvariant", self)

    @property
    def UMLModel_Constraint116(self):
        return self.__UMLModel_Constraint116

    @UMLModel_Constraint116.setter
    def UMLModel_Constraint116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Constraint__UMLModel_Constraint116", None)
        self.__UMLModel_Constraint116 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_Extend"):
                opp_val = getattr(old_value, "UMLModel_Extend", None)
                if opp_val == self:
                    setattr(old_value, "UMLModel_Extend", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_Extend"):
                opp_val = getattr(value, "UMLModel_Extend", None)
                setattr(value, "UMLModel_Extend", self)

class ExecutableNode:

    pass
class UMLModel_Action(ExecutableNode):

    def __init__(self, output: str, input: str, context: str, UMLModel_Action: set["UMLModel_Constraint"] = None, UMLModel_Action8: set["UMLModel_Constraint"] = None, UMLModel_Action11: "UMLModel_ActionInputPin" = None, UMLModel_Action155: "UMLModel_InteractionUse" = None, UMLModel_Action143: "UMLModel_Interaction" = None):
        self.output = output
        self.input = input
        self.context = context
        self.UMLModel_Action = UMLModel_Action if UMLModel_Action is not None else set()
        self.UMLModel_Action8 = UMLModel_Action8 if UMLModel_Action8 is not None else set()
        self.UMLModel_Action11 = UMLModel_Action11
        self.UMLModel_Action155 = UMLModel_Action155
        self.UMLModel_Action143 = UMLModel_Action143
        
    @property
    def output(self) -> str:
        return self.__output

    @output.setter
    def output(self, output: str):
        self.__output = output

    @property
    def input(self) -> str:
        return self.__input

    @input.setter
    def input(self, input: str):
        self.__input = input

    @property
    def context(self) -> str:
        return self.__context

    @context.setter
    def context(self, context: str):
        self.__context = context

    @property
    def UMLModel_Action(self):
        return self.__UMLModel_Action

    @UMLModel_Action.setter
    def UMLModel_Action(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Action__UMLModel_Action", None)
        self.__UMLModel_Action = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UMLModel_Constraint"):
                    opp_val = getattr(item, "UMLModel_Constraint", None)
                    
                    if opp_val == self:
                        setattr(item, "UMLModel_Constraint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UMLModel_Constraint"):
                    opp_val = getattr(item, "UMLModel_Constraint", None)
                    
                    setattr(item, "UMLModel_Constraint", self)
                    

    @property
    def UMLModel_Action143(self):
        return self.__UMLModel_Action143

    @UMLModel_Action143.setter
    def UMLModel_Action143(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Action__UMLModel_Action143", None)
        self.__UMLModel_Action143 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_Interaction142"):
                opp_val = getattr(old_value, "UMLModel_Interaction142", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_Interaction142"):
                opp_val = getattr(value, "UMLModel_Interaction142", None)
                if opp_val is None:
                    setattr(value, "UMLModel_Interaction142", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UMLModel_Action8(self):
        return self.__UMLModel_Action8

    @UMLModel_Action8.setter
    def UMLModel_Action8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Action__UMLModel_Action8", None)
        self.__UMLModel_Action8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UMLModel_Constraint9"):
                    opp_val = getattr(item, "UMLModel_Constraint9", None)
                    
                    if opp_val == self:
                        setattr(item, "UMLModel_Constraint9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UMLModel_Constraint9"):
                    opp_val = getattr(item, "UMLModel_Constraint9", None)
                    
                    setattr(item, "UMLModel_Constraint9", self)
                    

    @property
    def UMLModel_Action11(self):
        return self.__UMLModel_Action11

    @UMLModel_Action11.setter
    def UMLModel_Action11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Action__UMLModel_Action11", None)
        self.__UMLModel_Action11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_ActionInputPin"):
                opp_val = getattr(old_value, "UMLModel_ActionInputPin", None)
                if opp_val == self:
                    setattr(old_value, "UMLModel_ActionInputPin", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_ActionInputPin"):
                opp_val = getattr(value, "UMLModel_ActionInputPin", None)
                setattr(value, "UMLModel_ActionInputPin", self)

    @property
    def UMLModel_Action155(self):
        return self.__UMLModel_Action155

    @UMLModel_Action155.setter
    def UMLModel_Action155(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Action__UMLModel_Action155", None)
        self.__UMLModel_Action155 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_InteractionUse154"):
                opp_val = getattr(old_value, "UMLModel_InteractionUse154", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_InteractionUse154"):
                opp_val = getattr(value, "UMLModel_InteractionUse154", None)
                if opp_val is None:
                    setattr(value, "UMLModel_InteractionUse154", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class UMLModel_Trigger(NamedElement):

    def __init__(self, event: str, port: str, UMLModel_Trigger: "UMLModel_AcceptEventAction" = None, UMLModel_Trigger57: "UMLModel_BehavioredClassifier" = None, UMLModel_Trigger325: "UMLModel_State" = None, UMLModel_Trigger370: "UMLModel_Transition" = None):
        self.event = event
        self.port = port
        self.UMLModel_Trigger = UMLModel_Trigger
        self.UMLModel_Trigger57 = UMLModel_Trigger57
        self.UMLModel_Trigger325 = UMLModel_Trigger325
        self.UMLModel_Trigger370 = UMLModel_Trigger370
        
    @property
    def port(self) -> str:
        return self.__port

    @port.setter
    def port(self, port: str):
        self.__port = port

    @property
    def event(self) -> str:
        return self.__event

    @event.setter
    def event(self, event: str):
        self.__event = event

    @property
    def UMLModel_Trigger370(self):
        return self.__UMLModel_Trigger370

    @UMLModel_Trigger370.setter
    def UMLModel_Trigger370(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Trigger__UMLModel_Trigger370", None)
        self.__UMLModel_Trigger370 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_Transition369"):
                opp_val = getattr(old_value, "UMLModel_Transition369", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_Transition369"):
                opp_val = getattr(value, "UMLModel_Transition369", None)
                if opp_val is None:
                    setattr(value, "UMLModel_Transition369", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UMLModel_Trigger(self):
        return self.__UMLModel_Trigger

    @UMLModel_Trigger.setter
    def UMLModel_Trigger(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Trigger__UMLModel_Trigger", None)
        self.__UMLModel_Trigger = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_AcceptEventAction5"):
                opp_val = getattr(old_value, "UMLModel_AcceptEventAction5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_AcceptEventAction5"):
                opp_val = getattr(value, "UMLModel_AcceptEventAction5", None)
                if opp_val is None:
                    setattr(value, "UMLModel_AcceptEventAction5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UMLModel_Trigger57(self):
        return self.__UMLModel_Trigger57

    @UMLModel_Trigger57.setter
    def UMLModel_Trigger57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Trigger__UMLModel_Trigger57", None)
        self.__UMLModel_Trigger57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_BehavioredClassifier56"):
                opp_val = getattr(old_value, "UMLModel_BehavioredClassifier56", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_BehavioredClassifier56"):
                opp_val = getattr(value, "UMLModel_BehavioredClassifier56", None)
                if opp_val is None:
                    setattr(value, "UMLModel_BehavioredClassifier56", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UMLModel_Trigger325(self):
        return self.__UMLModel_Trigger325

    @UMLModel_Trigger325.setter
    def UMLModel_Trigger325(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Trigger__UMLModel_Trigger325", None)
        self.__UMLModel_Trigger325 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_State324"):
                opp_val = getattr(old_value, "UMLModel_State324", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_State324"):
                opp_val = getattr(value, "UMLModel_State324", None)
                if opp_val is None:
                    setattr(value, "UMLModel_State324", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Action:

    pass
class UMLModel_InvocationAction(Action):

    def __init__(self, onPort: str, UMLModel_InvocationAction: set["UMLModel_InputPin"] = None):
        self.onPort = onPort
        self.UMLModel_InvocationAction = UMLModel_InvocationAction if UMLModel_InvocationAction is not None else set()
        
    @property
    def onPort(self) -> str:
        return self.__onPort

    @onPort.setter
    def onPort(self, onPort: str):
        self.__onPort = onPort

    @property
    def UMLModel_InvocationAction(self):
        return self.__UMLModel_InvocationAction

    @UMLModel_InvocationAction.setter
    def UMLModel_InvocationAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_InvocationAction__UMLModel_InvocationAction", None)
        self.__UMLModel_InvocationAction = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UMLModel_InputPin137"):
                    opp_val = getattr(item, "UMLModel_InputPin137", None)
                    
                    if opp_val == self:
                        setattr(item, "UMLModel_InputPin137", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UMLModel_InputPin137"):
                    opp_val = getattr(item, "UMLModel_InputPin137", None)
                    
                    setattr(item, "UMLModel_InputPin137", self)
                    

class UMLModel_ReadExtentAction(Action):

    def __init__(self, classifier: str, UMLModel_ReadExtentAction: "UMLModel_OutputPin" = None):
        self.classifier = classifier
        self.UMLModel_ReadExtentAction = UMLModel_ReadExtentAction
        
    @property
    def classifier(self) -> str:
        return self.__classifier

    @classifier.setter
    def classifier(self, classifier: str):
        self.__classifier = classifier

    @property
    def UMLModel_ReadExtentAction(self):
        return self.__UMLModel_ReadExtentAction

    @UMLModel_ReadExtentAction.setter
    def UMLModel_ReadExtentAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_ReadExtentAction__UMLModel_ReadExtentAction", None)
        self.__UMLModel_ReadExtentAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_OutputPin241"):
                opp_val = getattr(old_value, "UMLModel_OutputPin241", None)
                if opp_val == self:
                    setattr(old_value, "UMLModel_OutputPin241", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_OutputPin241"):
                opp_val = getattr(value, "UMLModel_OutputPin241", None)
                setattr(value, "UMLModel_OutputPin241", self)

class UMLModel_ReadSelfAction(Action):

    pass
class UMLModel_StructuredActivityNode(ActivityGroup, Namespace, Action):

    def __init__(self, mustIsolate: str, UMLModel_StructuredActivityNode: set["UMLModel_Variable"] = None, UMLModel_StructuredActivityNode299: set["UMLModel_ActivityEdge"] = None, UMLModel_StructuredActivityNode302: set["UMLModel_ActivityNode"] = None):
        self.mustIsolate = mustIsolate
        self.UMLModel_StructuredActivityNode = UMLModel_StructuredActivityNode if UMLModel_StructuredActivityNode is not None else set()
        self.UMLModel_StructuredActivityNode299 = UMLModel_StructuredActivityNode299 if UMLModel_StructuredActivityNode299 is not None else set()
        self.UMLModel_StructuredActivityNode302 = UMLModel_StructuredActivityNode302 if UMLModel_StructuredActivityNode302 is not None else set()
        
    @property
    def mustIsolate(self) -> str:
        return self.__mustIsolate

    @mustIsolate.setter
    def mustIsolate(self, mustIsolate: str):
        self.__mustIsolate = mustIsolate

    @property
    def UMLModel_StructuredActivityNode(self):
        return self.__UMLModel_StructuredActivityNode

    @UMLModel_StructuredActivityNode.setter
    def UMLModel_StructuredActivityNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_StructuredActivityNode__UMLModel_StructuredActivityNode", None)
        self.__UMLModel_StructuredActivityNode = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UMLModel_Variable297"):
                    opp_val = getattr(item, "UMLModel_Variable297", None)
                    
                    if opp_val == self:
                        setattr(item, "UMLModel_Variable297", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UMLModel_Variable297"):
                    opp_val = getattr(item, "UMLModel_Variable297", None)
                    
                    setattr(item, "UMLModel_Variable297", self)
                    

    @property
    def UMLModel_StructuredActivityNode302(self):
        return self.__UMLModel_StructuredActivityNode302

    @UMLModel_StructuredActivityNode302.setter
    def UMLModel_StructuredActivityNode302(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_StructuredActivityNode__UMLModel_StructuredActivityNode302", None)
        self.__UMLModel_StructuredActivityNode302 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UMLModel_ActivityNode303"):
                    opp_val = getattr(item, "UMLModel_ActivityNode303", None)
                    
                    if opp_val == self:
                        setattr(item, "UMLModel_ActivityNode303", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UMLModel_ActivityNode303"):
                    opp_val = getattr(item, "UMLModel_ActivityNode303", None)
                    
                    setattr(item, "UMLModel_ActivityNode303", self)
                    

    @property
    def UMLModel_StructuredActivityNode299(self):
        return self.__UMLModel_StructuredActivityNode299

    @UMLModel_StructuredActivityNode299.setter
    def UMLModel_StructuredActivityNode299(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_StructuredActivityNode__UMLModel_StructuredActivityNode299", None)
        self.__UMLModel_StructuredActivityNode299 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UMLModel_ActivityEdge300"):
                    opp_val = getattr(item, "UMLModel_ActivityEdge300", None)
                    
                    if opp_val == self:
                        setattr(item, "UMLModel_ActivityEdge300", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UMLModel_ActivityEdge300"):
                    opp_val = getattr(item, "UMLModel_ActivityEdge300", None)
                    
                    setattr(item, "UMLModel_ActivityEdge300", self)
                    

class UMLModel_OpaqueAction(Action):

    def __init__(self, body: str, language: str, UMLModel_OpaqueAction: set["UMLModel_InputPin"] = None, UMLModel_OpaqueAction204: set["UMLModel_OutputPin"] = None):
        self.body = body
        self.language = language
        self.UMLModel_OpaqueAction = UMLModel_OpaqueAction if UMLModel_OpaqueAction is not None else set()
        self.UMLModel_OpaqueAction204 = UMLModel_OpaqueAction204 if UMLModel_OpaqueAction204 is not None else set()
        
    @property
    def language(self) -> str:
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language

    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

    @property
    def UMLModel_OpaqueAction(self):
        return self.__UMLModel_OpaqueAction

    @UMLModel_OpaqueAction.setter
    def UMLModel_OpaqueAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_OpaqueAction__UMLModel_OpaqueAction", None)
        self.__UMLModel_OpaqueAction = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UMLModel_InputPin202"):
                    opp_val = getattr(item, "UMLModel_InputPin202", None)
                    
                    if opp_val == self:
                        setattr(item, "UMLModel_InputPin202", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UMLModel_InputPin202"):
                    opp_val = getattr(item, "UMLModel_InputPin202", None)
                    
                    setattr(item, "UMLModel_InputPin202", self)
                    

    @property
    def UMLModel_OpaqueAction204(self):
        return self.__UMLModel_OpaqueAction204

    @UMLModel_OpaqueAction204.setter
    def UMLModel_OpaqueAction204(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_OpaqueAction__UMLModel_OpaqueAction204", None)
        self.__UMLModel_OpaqueAction204 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UMLModel_OutputPin205"):
                    opp_val = getattr(item, "UMLModel_OutputPin205", None)
                    
                    if opp_val == self:
                        setattr(item, "UMLModel_OutputPin205", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UMLModel_OutputPin205"):
                    opp_val = getattr(item, "UMLModel_OutputPin205", None)
                    
                    setattr(item, "UMLModel_OutputPin205", self)
                    

class UMLModel_ReplyAction(Action):

    def __init__(self, replyToCall: str, UMLModel_ReplyAction: "UMLModel_InputPin" = None, UMLModel_ReplyAction268: set["UMLModel_InputPin"] = None):
        self.replyToCall = replyToCall
        self.UMLModel_ReplyAction = UMLModel_ReplyAction
        self.UMLModel_ReplyAction268 = UMLModel_ReplyAction268 if UMLModel_ReplyAction268 is not None else set()
        
    @property
    def replyToCall(self) -> str:
        return self.__replyToCall

    @replyToCall.setter
    def replyToCall(self, replyToCall: str):
        self.__replyToCall = replyToCall

    @property
    def UMLModel_ReplyAction(self):
        return self.__UMLModel_ReplyAction

    @UMLModel_ReplyAction.setter
    def UMLModel_ReplyAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_ReplyAction__UMLModel_ReplyAction", None)
        self.__UMLModel_ReplyAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_InputPin266"):
                opp_val = getattr(old_value, "UMLModel_InputPin266", None)
                if opp_val == self:
                    setattr(old_value, "UMLModel_InputPin266", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_InputPin266"):
                opp_val = getattr(value, "UMLModel_InputPin266", None)
                setattr(value, "UMLModel_InputPin266", self)

    @property
    def UMLModel_ReplyAction268(self):
        return self.__UMLModel_ReplyAction268

    @UMLModel_ReplyAction268.setter
    def UMLModel_ReplyAction268(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_ReplyAction__UMLModel_ReplyAction268", None)
        self.__UMLModel_ReplyAction268 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UMLModel_InputPin269"):
                    opp_val = getattr(item, "UMLModel_InputPin269", None)
                    
                    if opp_val == self:
                        setattr(item, "UMLModel_InputPin269", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UMLModel_InputPin269"):
                    opp_val = getattr(item, "UMLModel_InputPin269", None)
                    
                    setattr(item, "UMLModel_InputPin269", self)
                    

class UMLModel_VariableAction(Action):

    def __init__(self, variable: str):
        self.variable = variable
        
    @property
    def variable(self) -> str:
        return self.__variable

    @variable.setter
    def variable(self, variable: str):
        self.__variable = variable

class UMLModel_ReadIsClassifiedObjectAction(Action):

    def __init__(self, isDirect: str, classifier: str, UMLModel_ReadIsClassifiedObjectAction: "UMLModel_OutputPin" = None, UMLModel_ReadIsClassifiedObjectAction238: "UMLModel_InputPin" = None):
        self.isDirect = isDirect
        self.classifier = classifier
        self.UMLModel_ReadIsClassifiedObjectAction = UMLModel_ReadIsClassifiedObjectAction
        self.UMLModel_ReadIsClassifiedObjectAction238 = UMLModel_ReadIsClassifiedObjectAction238
        
    @property
    def isDirect(self) -> str:
        return self.__isDirect

    @isDirect.setter
    def isDirect(self, isDirect: str):
        self.__isDirect = isDirect

    @property
    def classifier(self) -> str:
        return self.__classifier

    @classifier.setter
    def classifier(self, classifier: str):
        self.__classifier = classifier

    @property
    def UMLModel_ReadIsClassifiedObjectAction238(self):
        return self.__UMLModel_ReadIsClassifiedObjectAction238

    @UMLModel_ReadIsClassifiedObjectAction238.setter
    def UMLModel_ReadIsClassifiedObjectAction238(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_ReadIsClassifiedObjectAction__UMLModel_ReadIsClassifiedObjectAction238", None)
        self.__UMLModel_ReadIsClassifiedObjectAction238 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_InputPin239"):
                opp_val = getattr(old_value, "UMLModel_InputPin239", None)
                if opp_val == self:
                    setattr(old_value, "UMLModel_InputPin239", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_InputPin239"):
                opp_val = getattr(value, "UMLModel_InputPin239", None)
                setattr(value, "UMLModel_InputPin239", self)

    @property
    def UMLModel_ReadIsClassifiedObjectAction(self):
        return self.__UMLModel_ReadIsClassifiedObjectAction

    @UMLModel_ReadIsClassifiedObjectAction.setter
    def UMLModel_ReadIsClassifiedObjectAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_ReadIsClassifiedObjectAction__UMLModel_ReadIsClassifiedObjectAction", None)
        self.__UMLModel_ReadIsClassifiedObjectAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_OutputPin236"):
                opp_val = getattr(old_value, "UMLModel_OutputPin236", None)
                if opp_val == self:
                    setattr(old_value, "UMLModel_OutputPin236", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_OutputPin236"):
                opp_val = getattr(value, "UMLModel_OutputPin236", None)
                setattr(value, "UMLModel_OutputPin236", self)

class UMLModel_ReadLinkObjectEndAction(Action):

    def __init__(self, end: str, UMLModel_ReadLinkObjectEndAction: "UMLModel_InputPin" = None, UMLModel_ReadLinkObjectEndAction247: "UMLModel_OutputPin" = None):
        self.end = end
        self.UMLModel_ReadLinkObjectEndAction = UMLModel_ReadLinkObjectEndAction
        self.UMLModel_ReadLinkObjectEndAction247 = UMLModel_ReadLinkObjectEndAction247
        
    @property
    def end(self) -> str:
        return self.__end

    @end.setter
    def end(self, end: str):
        self.__end = end

    @property
    def UMLModel_ReadLinkObjectEndAction(self):
        return self.__UMLModel_ReadLinkObjectEndAction

    @UMLModel_ReadLinkObjectEndAction.setter
    def UMLModel_ReadLinkObjectEndAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_ReadLinkObjectEndAction__UMLModel_ReadLinkObjectEndAction", None)
        self.__UMLModel_ReadLinkObjectEndAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_InputPin245"):
                opp_val = getattr(old_value, "UMLModel_InputPin245", None)
                if opp_val == self:
                    setattr(old_value, "UMLModel_InputPin245", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_InputPin245"):
                opp_val = getattr(value, "UMLModel_InputPin245", None)
                setattr(value, "UMLModel_InputPin245", self)

    @property
    def UMLModel_ReadLinkObjectEndAction247(self):
        return self.__UMLModel_ReadLinkObjectEndAction247

    @UMLModel_ReadLinkObjectEndAction247.setter
    def UMLModel_ReadLinkObjectEndAction247(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_ReadLinkObjectEndAction__UMLModel_ReadLinkObjectEndAction247", None)
        self.__UMLModel_ReadLinkObjectEndAction247 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_OutputPin248"):
                opp_val = getattr(old_value, "UMLModel_OutputPin248", None)
                if opp_val == self:
                    setattr(old_value, "UMLModel_OutputPin248", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_OutputPin248"):
                opp_val = getattr(value, "UMLModel_OutputPin248", None)
                setattr(value, "UMLModel_OutputPin248", self)

class UMLModel_ValueSpecificationAction(Action):

    pass
class UMLModel_CreateObjectAction(Action):

    def __init__(self, classifier: str, UMLModel_CreateObjectAction: "UMLModel_OutputPin" = None):
        self.classifier = classifier
        self.UMLModel_CreateObjectAction = UMLModel_CreateObjectAction
        
    @property
    def classifier(self) -> str:
        return self.__classifier

    @classifier.setter
    def classifier(self, classifier: str):
        self.__classifier = classifier

    @property
    def UMLModel_CreateObjectAction(self):
        return self.__UMLModel_CreateObjectAction

    @UMLModel_CreateObjectAction.setter
    def UMLModel_CreateObjectAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_CreateObjectAction__UMLModel_CreateObjectAction", None)
        self.__UMLModel_CreateObjectAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_OutputPin99"):
                opp_val = getattr(old_value, "UMLModel_OutputPin99", None)
                if opp_val == self:
                    setattr(old_value, "UMLModel_OutputPin99", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_OutputPin99"):
                opp_val = getattr(value, "UMLModel_OutputPin99", None)
                setattr(value, "UMLModel_OutputPin99", self)

class UMLModel_LinkAction(Action):

    pass
class UMLModel_RaiseExceptionAction(Action):

    pass
class UMLModel_ClearAssociationAction(Action):

    def __init__(self, association: str, UMLModel_ClearAssociationAction: "UMLModel_InputPin" = None):
        self.association = association
        self.UMLModel_ClearAssociationAction = UMLModel_ClearAssociationAction
        
    @property
    def association(self) -> str:
        return self.__association

    @association.setter
    def association(self, association: str):
        self.__association = association

    @property
    def UMLModel_ClearAssociationAction(self):
        return self.__UMLModel_ClearAssociationAction

    @UMLModel_ClearAssociationAction.setter
    def UMLModel_ClearAssociationAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_ClearAssociationAction__UMLModel_ClearAssociationAction", None)
        self.__UMLModel_ClearAssociationAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_InputPin79"):
                opp_val = getattr(old_value, "UMLModel_InputPin79", None)
                if opp_val == self:
                    setattr(old_value, "UMLModel_InputPin79", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_InputPin79"):
                opp_val = getattr(value, "UMLModel_InputPin79", None)
                setattr(value, "UMLModel_InputPin79", self)

class UMLModel_ReadLinkObjectEndQualifierAction(Action):

    def __init__(self, qualifier: str, UMLModel_ReadLinkObjectEndQualifierAction: "UMLModel_InputPin" = None, UMLModel_ReadLinkObjectEndQualifierAction252: "UMLModel_OutputPin" = None):
        self.qualifier = qualifier
        self.UMLModel_ReadLinkObjectEndQualifierAction = UMLModel_ReadLinkObjectEndQualifierAction
        self.UMLModel_ReadLinkObjectEndQualifierAction252 = UMLModel_ReadLinkObjectEndQualifierAction252
        
    @property
    def qualifier(self) -> str:
        return self.__qualifier

    @qualifier.setter
    def qualifier(self, qualifier: str):
        self.__qualifier = qualifier

    @property
    def UMLModel_ReadLinkObjectEndQualifierAction(self):
        return self.__UMLModel_ReadLinkObjectEndQualifierAction

    @UMLModel_ReadLinkObjectEndQualifierAction.setter
    def UMLModel_ReadLinkObjectEndQualifierAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_ReadLinkObjectEndQualifierAction__UMLModel_ReadLinkObjectEndQualifierAction", None)
        self.__UMLModel_ReadLinkObjectEndQualifierAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_InputPin250"):
                opp_val = getattr(old_value, "UMLModel_InputPin250", None)
                if opp_val == self:
                    setattr(old_value, "UMLModel_InputPin250", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_InputPin250"):
                opp_val = getattr(value, "UMLModel_InputPin250", None)
                setattr(value, "UMLModel_InputPin250", self)

    @property
    def UMLModel_ReadLinkObjectEndQualifierAction252(self):
        return self.__UMLModel_ReadLinkObjectEndQualifierAction252

    @UMLModel_ReadLinkObjectEndQualifierAction252.setter
    def UMLModel_ReadLinkObjectEndQualifierAction252(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_ReadLinkObjectEndQualifierAction__UMLModel_ReadLinkObjectEndQualifierAction252", None)
        self.__UMLModel_ReadLinkObjectEndQualifierAction252 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_OutputPin253"):
                opp_val = getattr(old_value, "UMLModel_OutputPin253", None)
                if opp_val == self:
                    setattr(old_value, "UMLModel_OutputPin253", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_OutputPin253"):
                opp_val = getattr(value, "UMLModel_OutputPin253", None)
                setattr(value, "UMLModel_OutputPin253", self)

class UMLModel_StructuralFeatureAction(Action):

    def __init__(self, structuralFeature: str, UMLModel_StructuralFeatureAction: "UMLModel_InputPin" = None):
        self.structuralFeature = structuralFeature
        self.UMLModel_StructuralFeatureAction = UMLModel_StructuralFeatureAction
        
    @property
    def structuralFeature(self) -> str:
        return self.__structuralFeature

    @structuralFeature.setter
    def structuralFeature(self, structuralFeature: str):
        self.__structuralFeature = structuralFeature

    @property
    def UMLModel_StructuralFeatureAction(self):
        return self.__UMLModel_StructuralFeatureAction

    @UMLModel_StructuralFeatureAction.setter
    def UMLModel_StructuralFeatureAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_StructuralFeatureAction__UMLModel_StructuralFeatureAction", None)
        self.__UMLModel_StructuralFeatureAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_InputPin305"):
                opp_val = getattr(old_value, "UMLModel_InputPin305", None)
                if opp_val == self:
                    setattr(old_value, "UMLModel_InputPin305", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_InputPin305"):
                opp_val = getattr(value, "UMLModel_InputPin305", None)
                setattr(value, "UMLModel_InputPin305", self)

class UMLModel_DestroyObjectAction(Action):

    def __init__(self, isDestroyLinks: str, isDestroyOwnedObjects: str, UMLModel_DestroyObjectAction: "UMLModel_InputPin" = None):
        self.isDestroyLinks = isDestroyLinks
        self.isDestroyOwnedObjects = isDestroyOwnedObjects
        self.UMLModel_DestroyObjectAction = UMLModel_DestroyObjectAction
        
    @property
    def isDestroyOwnedObjects(self) -> str:
        return self.__isDestroyOwnedObjects

    @isDestroyOwnedObjects.setter
    def isDestroyOwnedObjects(self, isDestroyOwnedObjects: str):
        self.__isDestroyOwnedObjects = isDestroyOwnedObjects

    @property
    def isDestroyLinks(self) -> str:
        return self.__isDestroyLinks

    @isDestroyLinks.setter
    def isDestroyLinks(self, isDestroyLinks: str):
        self.__isDestroyLinks = isDestroyLinks

    @property
    def UMLModel_DestroyObjectAction(self):
        return self.__UMLModel_DestroyObjectAction

    @UMLModel_DestroyObjectAction.setter
    def UMLModel_DestroyObjectAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_DestroyObjectAction__UMLModel_DestroyObjectAction", None)
        self.__UMLModel_DestroyObjectAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_InputPin109"):
                opp_val = getattr(old_value, "UMLModel_InputPin109", None)
                if opp_val == self:
                    setattr(old_value, "UMLModel_InputPin109", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_InputPin109"):
                opp_val = getattr(value, "UMLModel_InputPin109", None)
                setattr(value, "UMLModel_InputPin109", self)

class UMLModel_ReclassifyObjectAction(Action):

    def __init__(self, isReplaceAll: str, oldClassifier: str, newClassifier: str, UMLModel_ReclassifyObjectAction: "UMLModel_InputPin" = None):
        self.isReplaceAll = isReplaceAll
        self.oldClassifier = oldClassifier
        self.newClassifier = newClassifier
        self.UMLModel_ReclassifyObjectAction = UMLModel_ReclassifyObjectAction
        
    @property
    def isReplaceAll(self) -> str:
        return self.__isReplaceAll

    @isReplaceAll.setter
    def isReplaceAll(self, isReplaceAll: str):
        self.__isReplaceAll = isReplaceAll

    @property
    def oldClassifier(self) -> str:
        return self.__oldClassifier

    @oldClassifier.setter
    def oldClassifier(self, oldClassifier: str):
        self.__oldClassifier = oldClassifier

    @property
    def newClassifier(self) -> str:
        return self.__newClassifier

    @newClassifier.setter
    def newClassifier(self, newClassifier: str):
        self.__newClassifier = newClassifier

    @property
    def UMLModel_ReclassifyObjectAction(self):
        return self.__UMLModel_ReclassifyObjectAction

    @UMLModel_ReclassifyObjectAction.setter
    def UMLModel_ReclassifyObjectAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_ReclassifyObjectAction__UMLModel_ReclassifyObjectAction", None)
        self.__UMLModel_ReclassifyObjectAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_InputPin234"):
                opp_val = getattr(old_value, "UMLModel_InputPin234", None)
                if opp_val == self:
                    setattr(old_value, "UMLModel_InputPin234", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_InputPin234"):
                opp_val = getattr(value, "UMLModel_InputPin234", None)
                setattr(value, "UMLModel_InputPin234", self)

class UMLModel_TestIdentityAction(Action):

    pass
class UMLModel_ReduceAction(Action):

    def __init__(self, reducer: str, isOrdered: str, UMLModel_ReduceAction: "UMLModel_OutputPin" = None, UMLModel_ReduceAction263: "UMLModel_InputPin" = None):
        self.reducer = reducer
        self.isOrdered = isOrdered
        self.UMLModel_ReduceAction = UMLModel_ReduceAction
        self.UMLModel_ReduceAction263 = UMLModel_ReduceAction263
        
    @property
    def reducer(self) -> str:
        return self.__reducer

    @reducer.setter
    def reducer(self, reducer: str):
        self.__reducer = reducer

    @property
    def isOrdered(self) -> str:
        return self.__isOrdered

    @isOrdered.setter
    def isOrdered(self, isOrdered: str):
        self.__isOrdered = isOrdered

    @property
    def UMLModel_ReduceAction(self):
        return self.__UMLModel_ReduceAction

    @UMLModel_ReduceAction.setter
    def UMLModel_ReduceAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_ReduceAction__UMLModel_ReduceAction", None)
        self.__UMLModel_ReduceAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_OutputPin261"):
                opp_val = getattr(old_value, "UMLModel_OutputPin261", None)
                if opp_val == self:
                    setattr(old_value, "UMLModel_OutputPin261", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_OutputPin261"):
                opp_val = getattr(value, "UMLModel_OutputPin261", None)
                setattr(value, "UMLModel_OutputPin261", self)

    @property
    def UMLModel_ReduceAction263(self):
        return self.__UMLModel_ReduceAction263

    @UMLModel_ReduceAction263.setter
    def UMLModel_ReduceAction263(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_ReduceAction__UMLModel_ReduceAction263", None)
        self.__UMLModel_ReduceAction263 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_InputPin264"):
                opp_val = getattr(old_value, "UMLModel_InputPin264", None)
                if opp_val == self:
                    setattr(old_value, "UMLModel_InputPin264", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_InputPin264"):
                opp_val = getattr(value, "UMLModel_InputPin264", None)
                setattr(value, "UMLModel_InputPin264", self)

class UMLModel_UnmarshallAction(Action):

    def __init__(self, unmarshallType: str, UMLModel_UnmarshallAction: set["UMLModel_OutputPin"] = None, UMLModel_UnmarshallAction374: "UMLModel_InputPin" = None):
        self.unmarshallType = unmarshallType
        self.UMLModel_UnmarshallAction = UMLModel_UnmarshallAction if UMLModel_UnmarshallAction is not None else set()
        self.UMLModel_UnmarshallAction374 = UMLModel_UnmarshallAction374
        
    @property
    def unmarshallType(self) -> str:
        return self.__unmarshallType

    @unmarshallType.setter
    def unmarshallType(self, unmarshallType: str):
        self.__unmarshallType = unmarshallType

    @property
    def UMLModel_UnmarshallAction374(self):
        return self.__UMLModel_UnmarshallAction374

    @UMLModel_UnmarshallAction374.setter
    def UMLModel_UnmarshallAction374(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_UnmarshallAction__UMLModel_UnmarshallAction374", None)
        self.__UMLModel_UnmarshallAction374 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_InputPin375"):
                opp_val = getattr(old_value, "UMLModel_InputPin375", None)
                if opp_val == self:
                    setattr(old_value, "UMLModel_InputPin375", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_InputPin375"):
                opp_val = getattr(value, "UMLModel_InputPin375", None)
                setattr(value, "UMLModel_InputPin375", self)

    @property
    def UMLModel_UnmarshallAction(self):
        return self.__UMLModel_UnmarshallAction

    @UMLModel_UnmarshallAction.setter
    def UMLModel_UnmarshallAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_UnmarshallAction__UMLModel_UnmarshallAction", None)
        self.__UMLModel_UnmarshallAction = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UMLModel_OutputPin372"):
                    opp_val = getattr(item, "UMLModel_OutputPin372", None)
                    
                    if opp_val == self:
                        setattr(item, "UMLModel_OutputPin372", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UMLModel_OutputPin372"):
                    opp_val = getattr(item, "UMLModel_OutputPin372", None)
                    
                    setattr(item, "UMLModel_OutputPin372", self)
                    

class UMLModel_StartClassifierBehaviorAction(Action):

    pass
class UMLModel_AcceptEventAction(Action):

    def __init__(self, isUnmarshall: str, UMLModel_AcceptEventAction: set["UMLModel_OutputPin"] = None, UMLModel_AcceptEventAction5: set["UMLModel_Trigger"] = None):
        self.isUnmarshall = isUnmarshall
        self.UMLModel_AcceptEventAction = UMLModel_AcceptEventAction if UMLModel_AcceptEventAction is not None else set()
        self.UMLModel_AcceptEventAction5 = UMLModel_AcceptEventAction5 if UMLModel_AcceptEventAction5 is not None else set()
        
    @property
    def isUnmarshall(self) -> str:
        return self.__isUnmarshall

    @isUnmarshall.setter
    def isUnmarshall(self, isUnmarshall: str):
        self.__isUnmarshall = isUnmarshall

    @property
    def UMLModel_AcceptEventAction(self):
        return self.__UMLModel_AcceptEventAction

    @UMLModel_AcceptEventAction.setter
    def UMLModel_AcceptEventAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_AcceptEventAction__UMLModel_AcceptEventAction", None)
        self.__UMLModel_AcceptEventAction = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UMLModel_OutputPin3"):
                    opp_val = getattr(item, "UMLModel_OutputPin3", None)
                    
                    if opp_val == self:
                        setattr(item, "UMLModel_OutputPin3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UMLModel_OutputPin3"):
                    opp_val = getattr(item, "UMLModel_OutputPin3", None)
                    
                    setattr(item, "UMLModel_OutputPin3", self)
                    

    @property
    def UMLModel_AcceptEventAction5(self):
        return self.__UMLModel_AcceptEventAction5

    @UMLModel_AcceptEventAction5.setter
    def UMLModel_AcceptEventAction5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_AcceptEventAction__UMLModel_AcceptEventAction5", None)
        self.__UMLModel_AcceptEventAction5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UMLModel_Trigger"):
                    opp_val = getattr(item, "UMLModel_Trigger", None)
                    
                    if opp_val == self:
                        setattr(item, "UMLModel_Trigger", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UMLModel_Trigger"):
                    opp_val = getattr(item, "UMLModel_Trigger", None)
                    
                    setattr(item, "UMLModel_Trigger", self)
                    

class UMLModel_OutputPin(Pin):

    pass
class AcceptEventAction:

    pass
class UMLModel_AcceptCallAction(AcceptEventAction):

    pass
class UMLModel_OpaqueExpression(ValueSpecification):

    def __init__(self, body: str, language: str, result: str, behavior: str, UMLModel_OpaqueExpression: "UMLModel_Abstraction" = None):
        self.body = body
        self.language = language
        self.result = result
        self.behavior = behavior
        self.UMLModel_OpaqueExpression = UMLModel_OpaqueExpression
        
    @property
    def language(self) -> str:
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language

    @property
    def behavior(self) -> str:
        return self.__behavior

    @behavior.setter
    def behavior(self, behavior: str):
        self.__behavior = behavior

    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

    @property
    def result(self) -> str:
        return self.__result

    @result.setter
    def result(self, result: str):
        self.__result = result

    @property
    def UMLModel_OpaqueExpression(self):
        return self.__UMLModel_OpaqueExpression

    @UMLModel_OpaqueExpression.setter
    def UMLModel_OpaqueExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_OpaqueExpression__UMLModel_OpaqueExpression", None)
        self.__UMLModel_OpaqueExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_Abstraction"):
                opp_val = getattr(old_value, "UMLModel_Abstraction", None)
                if opp_val == self:
                    setattr(old_value, "UMLModel_Abstraction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_Abstraction"):
                opp_val = getattr(value, "UMLModel_Abstraction", None)
                setattr(value, "UMLModel_Abstraction", self)

class Dependency:

    pass
class UMLModel_Usage(Dependency):

    pass
class UMLModel_Deployment(Dependency):

    def __init__(self, location: str, deployedArtifact: str, UMLModel_Deployment: "UMLModel_DeploymentTarget" = None, UMLModel_Deployment107: set["UMLModel_DeploymentSpecification"] = None):
        self.location = location
        self.deployedArtifact = deployedArtifact
        self.UMLModel_Deployment = UMLModel_Deployment
        self.UMLModel_Deployment107 = UMLModel_Deployment107 if UMLModel_Deployment107 is not None else set()
        
    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def deployedArtifact(self) -> str:
        return self.__deployedArtifact

    @deployedArtifact.setter
    def deployedArtifact(self, deployedArtifact: str):
        self.__deployedArtifact = deployedArtifact

    @property
    def UMLModel_Deployment(self):
        return self.__UMLModel_Deployment

    @UMLModel_Deployment.setter
    def UMLModel_Deployment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Deployment__UMLModel_Deployment", None)
        self.__UMLModel_Deployment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLModel_DeploymentTarget"):
                opp_val = getattr(old_value, "UMLModel_DeploymentTarget", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLModel_DeploymentTarget"):
                opp_val = getattr(value, "UMLModel_DeploymentTarget", None)
                if opp_val is None:
                    setattr(value, "UMLModel_DeploymentTarget", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UMLModel_Deployment107(self):
        return self.__UMLModel_Deployment107

    @UMLModel_Deployment107.setter
    def UMLModel_Deployment107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLModel_Deployment__UMLModel_Deployment107", None)
        self.__UMLModel_Deployment107 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UMLModel_DeploymentSpecification"):
                    opp_val = getattr(item, "UMLModel_DeploymentSpecification", None)
                    
                    if opp_val == self:
                        setattr(item, "UMLModel_DeploymentSpecification", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UMLModel_DeploymentSpecification"):
                    opp_val = getattr(item, "UMLModel_DeploymentSpecification", None)
                    
                    setattr(item, "UMLModel_DeploymentSpecification", self)
                    

class UMLModel_Abstraction(Dependency):

    pass