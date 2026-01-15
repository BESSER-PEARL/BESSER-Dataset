from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class VariabilityType(Enum):
    na = "na"
    contributes = "contributes"
    extends = "extends"
    replaces = "replaces"
    localContribution = "localContribution"
    localReplacement = "localReplacement"
    extendsReplaces = "extendsReplaces"
class WorkOrderType(Enum):
    finishToStart = "finishToStart"
    finishToFinish = "finishToFinish"
    startToStart = "startToStart"
    startToFinish = "startToFinish"


############################################
# Definition of Classes
############################################

class Concept:

    pass
class uma_Whitepaper(Concept):

    pass
class uma_WorkOrder:

    def __init__(self, linkType: str, properties: str, value: str, id: str, uma_WorkOrder: "uma_WorkBreakdownElement" = None):
        self.linkType = linkType
        self.properties = properties
        self.value = value
        self.id = id
        self.uma_WorkOrder = uma_WorkOrder
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def properties(self) -> str:
        return self.__properties

    @properties.setter
    def properties(self, properties: str):
        self.__properties = properties

    @property
    def linkType(self) -> str:
        return self.__linkType

    @linkType.setter
    def linkType(self, linkType: str):
        self.__linkType = linkType

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def uma_WorkOrder(self):
        return self.__uma_WorkOrder

    @uma_WorkOrder.setter
    def uma_WorkOrder(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_WorkOrder__uma_WorkOrder", None)
        self.__uma_WorkOrder = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_WorkBreakdownElement"):
                opp_val = getattr(old_value, "uma_WorkBreakdownElement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_WorkBreakdownElement"):
                opp_val = getattr(value, "uma_WorkBreakdownElement", None)
                if opp_val is None:
                    setattr(value, "uma_WorkBreakdownElement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Descriptor:

    pass
class uma_RoleDescriptor(Descriptor):

    def __init__(self, role: str, responsibleFor: str):
        self.role = role
        self.responsibleFor = responsibleFor
        
    @property
    def role(self) -> str:
        return self.__role

    @role.setter
    def role(self, role: str):
        self.__role = role

    @property
    def responsibleFor(self) -> str:
        return self.__responsibleFor

    @responsibleFor.setter
    def responsibleFor(self, responsibleFor: str):
        self.__responsibleFor = responsibleFor

class ActivityDescription:

    pass
class uma_ProcessDescription(ActivityDescription):

    def __init__(self, scope: str, usageNotes: str):
        self.scope = scope
        self.usageNotes = usageNotes
        
    @property
    def scope(self) -> str:
        return self.__scope

    @scope.setter
    def scope(self, scope: str):
        self.__scope = scope

    @property
    def usageNotes(self) -> str:
        return self.__usageNotes

    @usageNotes.setter
    def usageNotes(self, usageNotes: str):
        self.__usageNotes = usageNotes

class uma_WorkProductDescriptor(Descriptor):

    def __init__(self, activityEntryState: str, activityExitState: str, workProduct: str, responsibleRole: str, group2: str, externalInputTo: str, impactedBy: str, impacts: str, mandatoryInputTo: str, optionalInputTo: str, outputFrom: str, deliverableParts: str, uma_WorkProductDescriptor: "uma_ProcessComponentInterface" = None):
        self.activityEntryState = activityEntryState
        self.activityExitState = activityExitState
        self.workProduct = workProduct
        self.responsibleRole = responsibleRole
        self.group2 = group2
        self.externalInputTo = externalInputTo
        self.impactedBy = impactedBy
        self.impacts = impacts
        self.mandatoryInputTo = mandatoryInputTo
        self.optionalInputTo = optionalInputTo
        self.outputFrom = outputFrom
        self.deliverableParts = deliverableParts
        self.uma_WorkProductDescriptor = uma_WorkProductDescriptor
        
    @property
    def externalInputTo(self) -> str:
        return self.__externalInputTo

    @externalInputTo.setter
    def externalInputTo(self, externalInputTo: str):
        self.__externalInputTo = externalInputTo

    @property
    def impactedBy(self) -> str:
        return self.__impactedBy

    @impactedBy.setter
    def impactedBy(self, impactedBy: str):
        self.__impactedBy = impactedBy

    @property
    def optionalInputTo(self) -> str:
        return self.__optionalInputTo

    @optionalInputTo.setter
    def optionalInputTo(self, optionalInputTo: str):
        self.__optionalInputTo = optionalInputTo

    @property
    def activityEntryState(self) -> str:
        return self.__activityEntryState

    @activityEntryState.setter
    def activityEntryState(self, activityEntryState: str):
        self.__activityEntryState = activityEntryState

    @property
    def outputFrom(self) -> str:
        return self.__outputFrom

    @outputFrom.setter
    def outputFrom(self, outputFrom: str):
        self.__outputFrom = outputFrom

    @property
    def deliverableParts(self) -> str:
        return self.__deliverableParts

    @deliverableParts.setter
    def deliverableParts(self, deliverableParts: str):
        self.__deliverableParts = deliverableParts

    @property
    def group2(self) -> str:
        return self.__group2

    @group2.setter
    def group2(self, group2: str):
        self.__group2 = group2

    @property
    def activityExitState(self) -> str:
        return self.__activityExitState

    @activityExitState.setter
    def activityExitState(self, activityExitState: str):
        self.__activityExitState = activityExitState

    @property
    def impacts(self) -> str:
        return self.__impacts

    @impacts.setter
    def impacts(self, impacts: str):
        self.__impacts = impacts

    @property
    def responsibleRole(self) -> str:
        return self.__responsibleRole

    @responsibleRole.setter
    def responsibleRole(self, responsibleRole: str):
        self.__responsibleRole = responsibleRole

    @property
    def mandatoryInputTo(self) -> str:
        return self.__mandatoryInputTo

    @mandatoryInputTo.setter
    def mandatoryInputTo(self, mandatoryInputTo: str):
        self.__mandatoryInputTo = mandatoryInputTo

    @property
    def workProduct(self) -> str:
        return self.__workProduct

    @workProduct.setter
    def workProduct(self, workProduct: str):
        self.__workProduct = workProduct

    @property
    def uma_WorkProductDescriptor(self):
        return self.__uma_WorkProductDescriptor

    @uma_WorkProductDescriptor.setter
    def uma_WorkProductDescriptor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_WorkProductDescriptor__uma_WorkProductDescriptor", None)
        self.__uma_WorkProductDescriptor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_ProcessComponentInterface45"):
                opp_val = getattr(old_value, "uma_ProcessComponentInterface45", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_ProcessComponentInterface45"):
                opp_val = getattr(value, "uma_ProcessComponentInterface45", None)
                if opp_val is None:
                    setattr(value, "uma_ProcessComponentInterface45", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ProcessPackage:

    pass
class uma_ProcessComponent(ProcessPackage):

    def __init__(self, copyright: str, authors: str, changeDate: str, changeDescription: str, version: str, uma_ProcessComponent: "uma_ProcessComponentInterface" = None, uma_ProcessComponent41: "uma_Process" = None):
        self.copyright = copyright
        self.authors = authors
        self.changeDate = changeDate
        self.changeDescription = changeDescription
        self.version = version
        self.uma_ProcessComponent = uma_ProcessComponent
        self.uma_ProcessComponent41 = uma_ProcessComponent41
        
    @property
    def authors(self) -> str:
        return self.__authors

    @authors.setter
    def authors(self, authors: str):
        self.__authors = authors

    @property
    def changeDate(self) -> str:
        return self.__changeDate

    @changeDate.setter
    def changeDate(self, changeDate: str):
        self.__changeDate = changeDate

    @property
    def changeDescription(self) -> str:
        return self.__changeDescription

    @changeDescription.setter
    def changeDescription(self, changeDescription: str):
        self.__changeDescription = changeDescription

    @property
    def copyright(self) -> str:
        return self.__copyright

    @copyright.setter
    def copyright(self, copyright: str):
        self.__copyright = copyright

    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def uma_ProcessComponent41(self):
        return self.__uma_ProcessComponent41

    @uma_ProcessComponent41.setter
    def uma_ProcessComponent41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_ProcessComponent__uma_ProcessComponent41", None)
        self.__uma_ProcessComponent41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_Process"):
                opp_val = getattr(old_value, "uma_Process", None)
                if opp_val == self:
                    setattr(old_value, "uma_Process", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_Process"):
                opp_val = getattr(value, "uma_Process", None)
                setattr(value, "uma_Process", self)

    @property
    def uma_ProcessComponent(self):
        return self.__uma_ProcessComponent

    @uma_ProcessComponent.setter
    def uma_ProcessComponent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_ProcessComponent__uma_ProcessComponent", None)
        self.__uma_ProcessComponent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_ProcessComponentInterface"):
                opp_val = getattr(old_value, "uma_ProcessComponentInterface", None)
                if opp_val == self:
                    setattr(old_value, "uma_ProcessComponentInterface", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_ProcessComponentInterface"):
                opp_val = getattr(value, "uma_ProcessComponentInterface", None)
                setattr(value, "uma_ProcessComponentInterface", self)

class NamedElement:

    pass
class uma_PackageableElement(NamedElement):

    pass
class Element:

    pass
class uma_NamedElement(Element):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class Activity:

    pass
class uma_Phase(Activity):

    pass
class uma_Process(Activity):

    def __init__(self, includesPattern: str, defaultContext: str, validContext: str, diagramURI: str, uma_Process: "uma_ProcessComponent" = None):
        self.includesPattern = includesPattern
        self.defaultContext = defaultContext
        self.validContext = validContext
        self.diagramURI = diagramURI
        self.uma_Process = uma_Process
        
    @property
    def diagramURI(self) -> str:
        return self.__diagramURI

    @diagramURI.setter
    def diagramURI(self, diagramURI: str):
        self.__diagramURI = diagramURI

    @property
    def includesPattern(self) -> str:
        return self.__includesPattern

    @includesPattern.setter
    def includesPattern(self, includesPattern: str):
        self.__includesPattern = includesPattern

    @property
    def validContext(self) -> str:
        return self.__validContext

    @validContext.setter
    def validContext(self, validContext: str):
        self.__validContext = validContext

    @property
    def defaultContext(self) -> str:
        return self.__defaultContext

    @defaultContext.setter
    def defaultContext(self, defaultContext: str):
        self.__defaultContext = defaultContext

    @property
    def uma_Process(self):
        return self.__uma_Process

    @uma_Process.setter
    def uma_Process(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Process__uma_Process", None)
        self.__uma_Process = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_ProcessComponent41"):
                opp_val = getattr(old_value, "uma_ProcessComponent41", None)
                if opp_val == self:
                    setattr(old_value, "uma_ProcessComponent41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_ProcessComponent41"):
                opp_val = getattr(value, "uma_ProcessComponent41", None)
                setattr(value, "uma_ProcessComponent41", self)

class uma_Iteration(Activity):

    pass
class uma_Element:

    pass
class uma_EStringToStringMapEntry:

    pass
class uma_DocumentRoot:

    def __init__(self, mixed: str, uma_DocumentRoot16: set["uma_MethodConfiguration"] = None, uma_DocumentRoot18: set["uma_MethodLibrary"] = None, uma_DocumentRoot: set["uma_EStringToStringMapEntry"] = None, uma_DocumentRoot13: set["uma_EStringToStringMapEntry"] = None, uma_DocumentRoot20: set["uma_MethodPlugin"] = None):
        self.mixed = mixed
        self.uma_DocumentRoot16 = uma_DocumentRoot16 if uma_DocumentRoot16 is not None else set()
        self.uma_DocumentRoot18 = uma_DocumentRoot18 if uma_DocumentRoot18 is not None else set()
        self.uma_DocumentRoot = uma_DocumentRoot if uma_DocumentRoot is not None else set()
        self.uma_DocumentRoot13 = uma_DocumentRoot13 if uma_DocumentRoot13 is not None else set()
        self.uma_DocumentRoot20 = uma_DocumentRoot20 if uma_DocumentRoot20 is not None else set()
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def uma_DocumentRoot13(self):
        return self.__uma_DocumentRoot13

    @uma_DocumentRoot13.setter
    def uma_DocumentRoot13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_DocumentRoot__uma_DocumentRoot13", None)
        self.__uma_DocumentRoot13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uma_EStringToStringMapEntry14"):
                    opp_val = getattr(item, "uma_EStringToStringMapEntry14", None)
                    
                    if opp_val == self:
                        setattr(item, "uma_EStringToStringMapEntry14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uma_EStringToStringMapEntry14"):
                    opp_val = getattr(item, "uma_EStringToStringMapEntry14", None)
                    
                    setattr(item, "uma_EStringToStringMapEntry14", self)
                    

    @property
    def uma_DocumentRoot(self):
        return self.__uma_DocumentRoot

    @uma_DocumentRoot.setter
    def uma_DocumentRoot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_DocumentRoot__uma_DocumentRoot", None)
        self.__uma_DocumentRoot = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uma_EStringToStringMapEntry"):
                    opp_val = getattr(item, "uma_EStringToStringMapEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "uma_EStringToStringMapEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uma_EStringToStringMapEntry"):
                    opp_val = getattr(item, "uma_EStringToStringMapEntry", None)
                    
                    setattr(item, "uma_EStringToStringMapEntry", self)
                    

    @property
    def uma_DocumentRoot18(self):
        return self.__uma_DocumentRoot18

    @uma_DocumentRoot18.setter
    def uma_DocumentRoot18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_DocumentRoot__uma_DocumentRoot18", None)
        self.__uma_DocumentRoot18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uma_MethodLibrary"):
                    opp_val = getattr(item, "uma_MethodLibrary", None)
                    
                    if opp_val == self:
                        setattr(item, "uma_MethodLibrary", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uma_MethodLibrary"):
                    opp_val = getattr(item, "uma_MethodLibrary", None)
                    
                    setattr(item, "uma_MethodLibrary", self)
                    

    @property
    def uma_DocumentRoot20(self):
        return self.__uma_DocumentRoot20

    @uma_DocumentRoot20.setter
    def uma_DocumentRoot20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_DocumentRoot__uma_DocumentRoot20", None)
        self.__uma_DocumentRoot20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uma_MethodPlugin"):
                    opp_val = getattr(item, "uma_MethodPlugin", None)
                    
                    if opp_val == self:
                        setattr(item, "uma_MethodPlugin", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uma_MethodPlugin"):
                    opp_val = getattr(item, "uma_MethodPlugin", None)
                    
                    setattr(item, "uma_MethodPlugin", self)
                    

    @property
    def uma_DocumentRoot16(self):
        return self.__uma_DocumentRoot16

    @uma_DocumentRoot16.setter
    def uma_DocumentRoot16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_DocumentRoot__uma_DocumentRoot16", None)
        self.__uma_DocumentRoot16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uma_MethodConfiguration"):
                    opp_val = getattr(item, "uma_MethodConfiguration", None)
                    
                    if opp_val == self:
                        setattr(item, "uma_MethodConfiguration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uma_MethodConfiguration"):
                    opp_val = getattr(item, "uma_MethodConfiguration", None)
                    
                    setattr(item, "uma_MethodConfiguration", self)
                    

class BreakdownElement:

    pass
class uma_TeamProfile(BreakdownElement):

    def __init__(self, superTeam: str, subTeam: str, group2: str, role: str):
        self.superTeam = superTeam
        self.subTeam = subTeam
        self.group2 = group2
        self.role = role
        
    @property
    def subTeam(self) -> str:
        return self.__subTeam

    @subTeam.setter
    def subTeam(self, subTeam: str):
        self.__subTeam = subTeam

    @property
    def superTeam(self) -> str:
        return self.__superTeam

    @superTeam.setter
    def superTeam(self, superTeam: str):
        self.__superTeam = superTeam

    @property
    def group2(self) -> str:
        return self.__group2

    @group2.setter
    def group2(self, group2: str):
        self.__group2 = group2

    @property
    def role(self) -> str:
        return self.__role

    @role.setter
    def role(self, role: str):
        self.__role = role

class uma_WorkBreakdownElement(BreakdownElement):

    def __init__(self, group2: str, isEventDriven: str, isOngoing: str, isRepeatable: str, uma_WorkBreakdownElement: set["uma_WorkOrder"] = None):
        self.group2 = group2
        self.isEventDriven = isEventDriven
        self.isOngoing = isOngoing
        self.isRepeatable = isRepeatable
        self.uma_WorkBreakdownElement = uma_WorkBreakdownElement if uma_WorkBreakdownElement is not None else set()
        
    @property
    def group2(self) -> str:
        return self.__group2

    @group2.setter
    def group2(self, group2: str):
        self.__group2 = group2

    @property
    def isEventDriven(self) -> str:
        return self.__isEventDriven

    @isEventDriven.setter
    def isEventDriven(self, isEventDriven: str):
        self.__isEventDriven = isEventDriven

    @property
    def isRepeatable(self) -> str:
        return self.__isRepeatable

    @isRepeatable.setter
    def isRepeatable(self, isRepeatable: str):
        self.__isRepeatable = isRepeatable

    @property
    def isOngoing(self) -> str:
        return self.__isOngoing

    @isOngoing.setter
    def isOngoing(self, isOngoing: str):
        self.__isOngoing = isOngoing

    @property
    def uma_WorkBreakdownElement(self):
        return self.__uma_WorkBreakdownElement

    @uma_WorkBreakdownElement.setter
    def uma_WorkBreakdownElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_WorkBreakdownElement__uma_WorkBreakdownElement", None)
        self.__uma_WorkBreakdownElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uma_WorkOrder"):
                    opp_val = getattr(item, "uma_WorkOrder", None)
                    
                    if opp_val == self:
                        setattr(item, "uma_WorkOrder", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uma_WorkOrder"):
                    opp_val = getattr(item, "uma_WorkOrder", None)
                    
                    setattr(item, "uma_WorkOrder", self)
                    

class uma_ProcessComponentInterface(BreakdownElement):

    def __init__(self, group2: str, uma_ProcessComponentInterface: "uma_ProcessComponent" = None, uma_ProcessComponentInterface43: set["uma_TaskDescriptor"] = None, uma_ProcessComponentInterface45: set["uma_WorkProductDescriptor"] = None):
        self.group2 = group2
        self.uma_ProcessComponentInterface = uma_ProcessComponentInterface
        self.uma_ProcessComponentInterface43 = uma_ProcessComponentInterface43 if uma_ProcessComponentInterface43 is not None else set()
        self.uma_ProcessComponentInterface45 = uma_ProcessComponentInterface45 if uma_ProcessComponentInterface45 is not None else set()
        
    @property
    def group2(self) -> str:
        return self.__group2

    @group2.setter
    def group2(self, group2: str):
        self.__group2 = group2

    @property
    def uma_ProcessComponentInterface45(self):
        return self.__uma_ProcessComponentInterface45

    @uma_ProcessComponentInterface45.setter
    def uma_ProcessComponentInterface45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_ProcessComponentInterface__uma_ProcessComponentInterface45", None)
        self.__uma_ProcessComponentInterface45 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uma_WorkProductDescriptor"):
                    opp_val = getattr(item, "uma_WorkProductDescriptor", None)
                    
                    if opp_val == self:
                        setattr(item, "uma_WorkProductDescriptor", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uma_WorkProductDescriptor"):
                    opp_val = getattr(item, "uma_WorkProductDescriptor", None)
                    
                    setattr(item, "uma_WorkProductDescriptor", self)
                    

    @property
    def uma_ProcessComponentInterface(self):
        return self.__uma_ProcessComponentInterface

    @uma_ProcessComponentInterface.setter
    def uma_ProcessComponentInterface(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_ProcessComponentInterface__uma_ProcessComponentInterface", None)
        self.__uma_ProcessComponentInterface = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_ProcessComponent"):
                opp_val = getattr(old_value, "uma_ProcessComponent", None)
                if opp_val == self:
                    setattr(old_value, "uma_ProcessComponent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_ProcessComponent"):
                opp_val = getattr(value, "uma_ProcessComponent", None)
                setattr(value, "uma_ProcessComponent", self)

    @property
    def uma_ProcessComponentInterface43(self):
        return self.__uma_ProcessComponentInterface43

    @uma_ProcessComponentInterface43.setter
    def uma_ProcessComponentInterface43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_ProcessComponentInterface__uma_ProcessComponentInterface43", None)
        self.__uma_ProcessComponentInterface43 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uma_TaskDescriptor"):
                    opp_val = getattr(item, "uma_TaskDescriptor", None)
                    
                    if opp_val == self:
                        setattr(item, "uma_TaskDescriptor", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uma_TaskDescriptor"):
                    opp_val = getattr(item, "uma_TaskDescriptor", None)
                    
                    setattr(item, "uma_TaskDescriptor", self)
                    

class uma_Descriptor(BreakdownElement):

    def __init__(self, isSynchronizedWithSource: str):
        self.isSynchronizedWithSource = isSynchronizedWithSource
        
    @property
    def isSynchronizedWithSource(self) -> str:
        return self.__isSynchronizedWithSource

    @isSynchronizedWithSource.setter
    def isSynchronizedWithSource(self, isSynchronizedWithSource: str):
        self.__isSynchronizedWithSource = isSynchronizedWithSource

class ProcessDescription:

    pass
class uma_DeliveryProcessDescription(ProcessDescription):

    def __init__(self, projectCharacteristics: str, riskLevel: str, estimatingTechnique: str, scale: str, projectMemberExpertise: str, typeOfContract: str):
        self.projectCharacteristics = projectCharacteristics
        self.riskLevel = riskLevel
        self.estimatingTechnique = estimatingTechnique
        self.scale = scale
        self.projectMemberExpertise = projectMemberExpertise
        self.typeOfContract = typeOfContract
        
    @property
    def projectCharacteristics(self) -> str:
        return self.__projectCharacteristics

    @projectCharacteristics.setter
    def projectCharacteristics(self, projectCharacteristics: str):
        self.__projectCharacteristics = projectCharacteristics

    @property
    def typeOfContract(self) -> str:
        return self.__typeOfContract

    @typeOfContract.setter
    def typeOfContract(self, typeOfContract: str):
        self.__typeOfContract = typeOfContract

    @property
    def projectMemberExpertise(self) -> str:
        return self.__projectMemberExpertise

    @projectMemberExpertise.setter
    def projectMemberExpertise(self, projectMemberExpertise: str):
        self.__projectMemberExpertise = projectMemberExpertise

    @property
    def scale(self) -> str:
        return self.__scale

    @scale.setter
    def scale(self, scale: str):
        self.__scale = scale

    @property
    def estimatingTechnique(self) -> str:
        return self.__estimatingTechnique

    @estimatingTechnique.setter
    def estimatingTechnique(self, estimatingTechnique: str):
        self.__estimatingTechnique = estimatingTechnique

    @property
    def riskLevel(self) -> str:
        return self.__riskLevel

    @riskLevel.setter
    def riskLevel(self, riskLevel: str):
        self.__riskLevel = riskLevel

class ContentCategory:

    pass
class uma_Tool(ContentCategory):

    def __init__(self, group2: str, toolMentor: str):
        self.group2 = group2
        self.toolMentor = toolMentor
        
    @property
    def group2(self) -> str:
        return self.__group2

    @group2.setter
    def group2(self, group2: str):
        self.__group2 = group2

    @property
    def toolMentor(self) -> str:
        return self.__toolMentor

    @toolMentor.setter
    def toolMentor(self, toolMentor: str):
        self.__toolMentor = toolMentor

class uma_RoleSet(ContentCategory):

    def __init__(self, group2: str, role: str):
        self.group2 = group2
        self.role = role
        
    @property
    def group2(self) -> str:
        return self.__group2

    @group2.setter
    def group2(self, group2: str):
        self.__group2 = group2

    @property
    def role(self) -> str:
        return self.__role

    @role.setter
    def role(self, role: str):
        self.__role = role

class uma_Discipline(ContentCategory):

    def __init__(self, group2: str, task: str, referenceWorkflow: str, uma_Discipline: "uma_Discipline" = None, uma_Discipline9: set["uma_Discipline"] = None):
        self.group2 = group2
        self.task = task
        self.referenceWorkflow = referenceWorkflow
        self.uma_Discipline = uma_Discipline
        self.uma_Discipline9 = uma_Discipline9 if uma_Discipline9 is not None else set()
        
    @property
    def referenceWorkflow(self) -> str:
        return self.__referenceWorkflow

    @referenceWorkflow.setter
    def referenceWorkflow(self, referenceWorkflow: str):
        self.__referenceWorkflow = referenceWorkflow

    @property
    def group2(self) -> str:
        return self.__group2

    @group2.setter
    def group2(self, group2: str):
        self.__group2 = group2

    @property
    def task(self) -> str:
        return self.__task

    @task.setter
    def task(self, task: str):
        self.__task = task

    @property
    def uma_Discipline(self):
        return self.__uma_Discipline

    @uma_Discipline.setter
    def uma_Discipline(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Discipline__uma_Discipline", None)
        self.__uma_Discipline = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_Discipline9"):
                opp_val = getattr(old_value, "uma_Discipline9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_Discipline9"):
                opp_val = getattr(value, "uma_Discipline9", None)
                if opp_val is None:
                    setattr(value, "uma_Discipline9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uma_Discipline9(self):
        return self.__uma_Discipline9

    @uma_Discipline9.setter
    def uma_Discipline9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Discipline__uma_Discipline9", None)
        self.__uma_Discipline9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uma_Discipline"):
                    opp_val = getattr(item, "uma_Discipline", None)
                    
                    if opp_val == self:
                        setattr(item, "uma_Discipline", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uma_Discipline"):
                    opp_val = getattr(item, "uma_Discipline", None)
                    
                    setattr(item, "uma_Discipline", self)
                    

class uma_WorkProductType(ContentCategory):

    def __init__(self, group2: str, workProduct: str):
        self.group2 = group2
        self.workProduct = workProduct
        
    @property
    def group2(self) -> str:
        return self.__group2

    @group2.setter
    def group2(self, group2: str):
        self.__group2 = group2

    @property
    def workProduct(self) -> str:
        return self.__workProduct

    @workProduct.setter
    def workProduct(self, workProduct: str):
        self.__workProduct = workProduct

class uma_Domain(ContentCategory):

    def __init__(self, group2: str, workProduct: str, uma_Domain: "uma_Domain" = None, uma_Domain21: set["uma_Domain"] = None):
        self.group2 = group2
        self.workProduct = workProduct
        self.uma_Domain = uma_Domain
        self.uma_Domain21 = uma_Domain21 if uma_Domain21 is not None else set()
        
    @property
    def workProduct(self) -> str:
        return self.__workProduct

    @workProduct.setter
    def workProduct(self, workProduct: str):
        self.__workProduct = workProduct

    @property
    def group2(self) -> str:
        return self.__group2

    @group2.setter
    def group2(self, group2: str):
        self.__group2 = group2

    @property
    def uma_Domain21(self):
        return self.__uma_Domain21

    @uma_Domain21.setter
    def uma_Domain21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Domain__uma_Domain21", None)
        self.__uma_Domain21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uma_Domain"):
                    opp_val = getattr(item, "uma_Domain", None)
                    
                    if opp_val == self:
                        setattr(item, "uma_Domain", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uma_Domain"):
                    opp_val = getattr(item, "uma_Domain", None)
                    
                    setattr(item, "uma_Domain", self)
                    

    @property
    def uma_Domain(self):
        return self.__uma_Domain

    @uma_Domain.setter
    def uma_Domain(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Domain__uma_Domain", None)
        self.__uma_Domain = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_Domain21"):
                opp_val = getattr(old_value, "uma_Domain21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_Domain21"):
                opp_val = getattr(value, "uma_Domain21", None)
                if opp_val is None:
                    setattr(value, "uma_Domain21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class uma_DisciplineGrouping(ContentCategory):

    def __init__(self, group2: str, discipline: str):
        self.group2 = group2
        self.discipline = discipline
        
    @property
    def group2(self) -> str:
        return self.__group2

    @group2.setter
    def group2(self, group2: str):
        self.__group2 = group2

    @property
    def discipline(self) -> str:
        return self.__discipline

    @discipline.setter
    def discipline(self, discipline: str):
        self.__discipline = discipline

class uma_RoleSetGrouping(ContentCategory):

    def __init__(self, roleSet: str, group2: str):
        self.roleSet = roleSet
        self.group2 = group2
        
    @property
    def group2(self) -> str:
        return self.__group2

    @group2.setter
    def group2(self, group2: str):
        self.__group2 = group2

    @property
    def roleSet(self) -> str:
        return self.__roleSet

    @roleSet.setter
    def roleSet(self, roleSet: str):
        self.__roleSet = roleSet

class uma_CustomCategory(ContentCategory):

    def __init__(self, group2: str, categorizedElement: str, subCategory: str):
        self.group2 = group2
        self.categorizedElement = categorizedElement
        self.subCategory = subCategory
        
    @property
    def group2(self) -> str:
        return self.__group2

    @group2.setter
    def group2(self, group2: str):
        self.__group2 = group2

    @property
    def categorizedElement(self) -> str:
        return self.__categorizedElement

    @categorizedElement.setter
    def categorizedElement(self, categorizedElement: str):
        self.__categorizedElement = categorizedElement

    @property
    def subCategory(self) -> str:
        return self.__subCategory

    @subCategory.setter
    def subCategory(self, subCategory: str):
        self.__subCategory = subCategory

class WorkBreakdownElement:

    pass
class uma_Milestone(WorkBreakdownElement):

    def __init__(self, requiredResult: str):
        self.requiredResult = requiredResult
        
    @property
    def requiredResult(self) -> str:
        return self.__requiredResult

    @requiredResult.setter
    def requiredResult(self, requiredResult: str):
        self.__requiredResult = requiredResult

class uma_TaskDescriptor(WorkBreakdownElement):

    def __init__(self, group3: str, performedPrimarilyBy: str, additionallyPerformedBy: str, assistedBy: str, task: str, externalInput: str, mandatoryInput: str, optionalInput: str, output: str, isSynchronizedWithSource: str, uma_TaskDescriptor: "uma_ProcessComponentInterface" = None, uma_TaskDescriptor51: set["uma_Section"] = None):
        self.group3 = group3
        self.performedPrimarilyBy = performedPrimarilyBy
        self.additionallyPerformedBy = additionallyPerformedBy
        self.assistedBy = assistedBy
        self.task = task
        self.externalInput = externalInput
        self.mandatoryInput = mandatoryInput
        self.optionalInput = optionalInput
        self.output = output
        self.isSynchronizedWithSource = isSynchronizedWithSource
        self.uma_TaskDescriptor = uma_TaskDescriptor
        self.uma_TaskDescriptor51 = uma_TaskDescriptor51 if uma_TaskDescriptor51 is not None else set()
        
    @property
    def performedPrimarilyBy(self) -> str:
        return self.__performedPrimarilyBy

    @performedPrimarilyBy.setter
    def performedPrimarilyBy(self, performedPrimarilyBy: str):
        self.__performedPrimarilyBy = performedPrimarilyBy

    @property
    def externalInput(self) -> str:
        return self.__externalInput

    @externalInput.setter
    def externalInput(self, externalInput: str):
        self.__externalInput = externalInput

    @property
    def mandatoryInput(self) -> str:
        return self.__mandatoryInput

    @mandatoryInput.setter
    def mandatoryInput(self, mandatoryInput: str):
        self.__mandatoryInput = mandatoryInput

    @property
    def optionalInput(self) -> str:
        return self.__optionalInput

    @optionalInput.setter
    def optionalInput(self, optionalInput: str):
        self.__optionalInput = optionalInput

    @property
    def isSynchronizedWithSource(self) -> str:
        return self.__isSynchronizedWithSource

    @isSynchronizedWithSource.setter
    def isSynchronizedWithSource(self, isSynchronizedWithSource: str):
        self.__isSynchronizedWithSource = isSynchronizedWithSource

    @property
    def assistedBy(self) -> str:
        return self.__assistedBy

    @assistedBy.setter
    def assistedBy(self, assistedBy: str):
        self.__assistedBy = assistedBy

    @property
    def output(self) -> str:
        return self.__output

    @output.setter
    def output(self, output: str):
        self.__output = output

    @property
    def additionallyPerformedBy(self) -> str:
        return self.__additionallyPerformedBy

    @additionallyPerformedBy.setter
    def additionallyPerformedBy(self, additionallyPerformedBy: str):
        self.__additionallyPerformedBy = additionallyPerformedBy

    @property
    def task(self) -> str:
        return self.__task

    @task.setter
    def task(self, task: str):
        self.__task = task

    @property
    def group3(self) -> str:
        return self.__group3

    @group3.setter
    def group3(self, group3: str):
        self.__group3 = group3

    @property
    def uma_TaskDescriptor51(self):
        return self.__uma_TaskDescriptor51

    @uma_TaskDescriptor51.setter
    def uma_TaskDescriptor51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_TaskDescriptor__uma_TaskDescriptor51", None)
        self.__uma_TaskDescriptor51 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uma_Section52"):
                    opp_val = getattr(item, "uma_Section52", None)
                    
                    if opp_val == self:
                        setattr(item, "uma_Section52", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uma_Section52"):
                    opp_val = getattr(item, "uma_Section52", None)
                    
                    setattr(item, "uma_Section52", self)
                    

    @property
    def uma_TaskDescriptor(self):
        return self.__uma_TaskDescriptor

    @uma_TaskDescriptor.setter
    def uma_TaskDescriptor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_TaskDescriptor__uma_TaskDescriptor", None)
        self.__uma_TaskDescriptor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_ProcessComponentInterface43"):
                opp_val = getattr(old_value, "uma_ProcessComponentInterface43", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_ProcessComponentInterface43"):
                opp_val = getattr(value, "uma_ProcessComponentInterface43", None)
                if opp_val is None:
                    setattr(value, "uma_ProcessComponentInterface43", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class uma_Activity(WorkBreakdownElement):

    def __init__(self, isEnactable: str, roadmap: str, precondition: str, postcondition: str, group3: str, variabilityBasedOnElement: str, variabilityType: str, uma_Activity: set["uma_BreakdownElement"] = None):
        self.isEnactable = isEnactable
        self.roadmap = roadmap
        self.precondition = precondition
        self.postcondition = postcondition
        self.group3 = group3
        self.variabilityBasedOnElement = variabilityBasedOnElement
        self.variabilityType = variabilityType
        self.uma_Activity = uma_Activity if uma_Activity is not None else set()
        
    @property
    def group3(self) -> str:
        return self.__group3

    @group3.setter
    def group3(self, group3: str):
        self.__group3 = group3

    @property
    def postcondition(self) -> str:
        return self.__postcondition

    @postcondition.setter
    def postcondition(self, postcondition: str):
        self.__postcondition = postcondition

    @property
    def variabilityBasedOnElement(self) -> str:
        return self.__variabilityBasedOnElement

    @variabilityBasedOnElement.setter
    def variabilityBasedOnElement(self, variabilityBasedOnElement: str):
        self.__variabilityBasedOnElement = variabilityBasedOnElement

    @property
    def variabilityType(self) -> str:
        return self.__variabilityType

    @variabilityType.setter
    def variabilityType(self, variabilityType: str):
        self.__variabilityType = variabilityType

    @property
    def precondition(self) -> str:
        return self.__precondition

    @precondition.setter
    def precondition(self, precondition: str):
        self.__precondition = precondition

    @property
    def roadmap(self) -> str:
        return self.__roadmap

    @roadmap.setter
    def roadmap(self, roadmap: str):
        self.__roadmap = roadmap

    @property
    def isEnactable(self) -> str:
        return self.__isEnactable

    @isEnactable.setter
    def isEnactable(self, isEnactable: str):
        self.__isEnactable = isEnactable

    @property
    def uma_Activity(self):
        return self.__uma_Activity

    @uma_Activity.setter
    def uma_Activity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Activity__uma_Activity", None)
        self.__uma_Activity = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uma_BreakdownElement"):
                    opp_val = getattr(item, "uma_BreakdownElement", None)
                    
                    if opp_val == self:
                        setattr(item, "uma_BreakdownElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uma_BreakdownElement"):
                    opp_val = getattr(item, "uma_BreakdownElement", None)
                    
                    setattr(item, "uma_BreakdownElement", self)
                    

class DescribableElement:

    pass
class uma_ProcessElement(DescribableElement):

    pass
class uma_ContentElement(DescribableElement):

    def __init__(self, concept: str, example: str, group1: str, checklist: str, guideline: str, reusableAsset: str, supportingMaterial: str, whitepaper: str, variabilityBasedOnElement: str, variabilityType: str, uma_ContentElement: "uma_ContentPackage" = None):
        self.concept = concept
        self.example = example
        self.group1 = group1
        self.checklist = checklist
        self.guideline = guideline
        self.reusableAsset = reusableAsset
        self.supportingMaterial = supportingMaterial
        self.whitepaper = whitepaper
        self.variabilityBasedOnElement = variabilityBasedOnElement
        self.variabilityType = variabilityType
        self.uma_ContentElement = uma_ContentElement
        
    @property
    def concept(self) -> str:
        return self.__concept

    @concept.setter
    def concept(self, concept: str):
        self.__concept = concept

    @property
    def checklist(self) -> str:
        return self.__checklist

    @checklist.setter
    def checklist(self, checklist: str):
        self.__checklist = checklist

    @property
    def example(self) -> str:
        return self.__example

    @example.setter
    def example(self, example: str):
        self.__example = example

    @property
    def variabilityType(self) -> str:
        return self.__variabilityType

    @variabilityType.setter
    def variabilityType(self, variabilityType: str):
        self.__variabilityType = variabilityType

    @property
    def guideline(self) -> str:
        return self.__guideline

    @guideline.setter
    def guideline(self, guideline: str):
        self.__guideline = guideline

    @property
    def variabilityBasedOnElement(self) -> str:
        return self.__variabilityBasedOnElement

    @variabilityBasedOnElement.setter
    def variabilityBasedOnElement(self, variabilityBasedOnElement: str):
        self.__variabilityBasedOnElement = variabilityBasedOnElement

    @property
    def group1(self) -> str:
        return self.__group1

    @group1.setter
    def group1(self, group1: str):
        self.__group1 = group1

    @property
    def supportingMaterial(self) -> str:
        return self.__supportingMaterial

    @supportingMaterial.setter
    def supportingMaterial(self, supportingMaterial: str):
        self.__supportingMaterial = supportingMaterial

    @property
    def reusableAsset(self) -> str:
        return self.__reusableAsset

    @reusableAsset.setter
    def reusableAsset(self, reusableAsset: str):
        self.__reusableAsset = reusableAsset

    @property
    def whitepaper(self) -> str:
        return self.__whitepaper

    @whitepaper.setter
    def whitepaper(self, whitepaper: str):
        self.__whitepaper = whitepaper

    @property
    def uma_ContentElement(self):
        return self.__uma_ContentElement

    @uma_ContentElement.setter
    def uma_ContentElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_ContentElement__uma_ContentElement", None)
        self.__uma_ContentElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_ContentPackage"):
                opp_val = getattr(old_value, "uma_ContentPackage", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_ContentPackage"):
                opp_val = getattr(value, "uma_ContentPackage", None)
                if opp_val is None:
                    setattr(value, "uma_ContentPackage", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class MethodUnit:

    pass
class uma_MethodPlugin(MethodUnit):

    def __init__(self, referencedMethodPlugin: str, supporting: str, userChangeable: str, uma_MethodPlugin: "uma_DocumentRoot" = None, uma_MethodPlugin28: "uma_MethodLibrary" = None, uma_MethodPlugin35: set["uma_MethodPackage"] = None):
        self.referencedMethodPlugin = referencedMethodPlugin
        self.supporting = supporting
        self.userChangeable = userChangeable
        self.uma_MethodPlugin = uma_MethodPlugin
        self.uma_MethodPlugin28 = uma_MethodPlugin28
        self.uma_MethodPlugin35 = uma_MethodPlugin35 if uma_MethodPlugin35 is not None else set()
        
    @property
    def userChangeable(self) -> str:
        return self.__userChangeable

    @userChangeable.setter
    def userChangeable(self, userChangeable: str):
        self.__userChangeable = userChangeable

    @property
    def supporting(self) -> str:
        return self.__supporting

    @supporting.setter
    def supporting(self, supporting: str):
        self.__supporting = supporting

    @property
    def referencedMethodPlugin(self) -> str:
        return self.__referencedMethodPlugin

    @referencedMethodPlugin.setter
    def referencedMethodPlugin(self, referencedMethodPlugin: str):
        self.__referencedMethodPlugin = referencedMethodPlugin

    @property
    def uma_MethodPlugin(self):
        return self.__uma_MethodPlugin

    @uma_MethodPlugin.setter
    def uma_MethodPlugin(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_MethodPlugin__uma_MethodPlugin", None)
        self.__uma_MethodPlugin = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_DocumentRoot20"):
                opp_val = getattr(old_value, "uma_DocumentRoot20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_DocumentRoot20"):
                opp_val = getattr(value, "uma_DocumentRoot20", None)
                if opp_val is None:
                    setattr(value, "uma_DocumentRoot20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uma_MethodPlugin35(self):
        return self.__uma_MethodPlugin35

    @uma_MethodPlugin35.setter
    def uma_MethodPlugin35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_MethodPlugin__uma_MethodPlugin35", None)
        self.__uma_MethodPlugin35 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uma_MethodPackage36"):
                    opp_val = getattr(item, "uma_MethodPackage36", None)
                    
                    if opp_val == self:
                        setattr(item, "uma_MethodPackage36", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uma_MethodPackage36"):
                    opp_val = getattr(item, "uma_MethodPackage36", None)
                    
                    setattr(item, "uma_MethodPackage36", self)
                    

    @property
    def uma_MethodPlugin28(self):
        return self.__uma_MethodPlugin28

    @uma_MethodPlugin28.setter
    def uma_MethodPlugin28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_MethodPlugin__uma_MethodPlugin28", None)
        self.__uma_MethodPlugin28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_MethodLibrary27"):
                opp_val = getattr(old_value, "uma_MethodLibrary27", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_MethodLibrary27"):
                opp_val = getattr(value, "uma_MethodLibrary27", None)
                if opp_val is None:
                    setattr(value, "uma_MethodLibrary27", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class uma_MethodLibrary(MethodUnit):

    def __init__(self, tool: str, uma_MethodLibrary: "uma_DocumentRoot" = None, uma_MethodLibrary27: set["uma_MethodPlugin"] = None, uma_MethodLibrary30: set["uma_MethodConfiguration"] = None):
        self.tool = tool
        self.uma_MethodLibrary = uma_MethodLibrary
        self.uma_MethodLibrary27 = uma_MethodLibrary27 if uma_MethodLibrary27 is not None else set()
        self.uma_MethodLibrary30 = uma_MethodLibrary30 if uma_MethodLibrary30 is not None else set()
        
    @property
    def tool(self) -> str:
        return self.__tool

    @tool.setter
    def tool(self, tool: str):
        self.__tool = tool

    @property
    def uma_MethodLibrary27(self):
        return self.__uma_MethodLibrary27

    @uma_MethodLibrary27.setter
    def uma_MethodLibrary27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_MethodLibrary__uma_MethodLibrary27", None)
        self.__uma_MethodLibrary27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uma_MethodPlugin28"):
                    opp_val = getattr(item, "uma_MethodPlugin28", None)
                    
                    if opp_val == self:
                        setattr(item, "uma_MethodPlugin28", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uma_MethodPlugin28"):
                    opp_val = getattr(item, "uma_MethodPlugin28", None)
                    
                    setattr(item, "uma_MethodPlugin28", self)
                    

    @property
    def uma_MethodLibrary(self):
        return self.__uma_MethodLibrary

    @uma_MethodLibrary.setter
    def uma_MethodLibrary(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_MethodLibrary__uma_MethodLibrary", None)
        self.__uma_MethodLibrary = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_DocumentRoot18"):
                opp_val = getattr(old_value, "uma_DocumentRoot18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_DocumentRoot18"):
                opp_val = getattr(value, "uma_DocumentRoot18", None)
                if opp_val is None:
                    setattr(value, "uma_DocumentRoot18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uma_MethodLibrary30(self):
        return self.__uma_MethodLibrary30

    @uma_MethodLibrary30.setter
    def uma_MethodLibrary30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_MethodLibrary__uma_MethodLibrary30", None)
        self.__uma_MethodLibrary30 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uma_MethodConfiguration31"):
                    opp_val = getattr(item, "uma_MethodConfiguration31", None)
                    
                    if opp_val == self:
                        setattr(item, "uma_MethodConfiguration31", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uma_MethodConfiguration31"):
                    opp_val = getattr(item, "uma_MethodConfiguration31", None)
                    
                    setattr(item, "uma_MethodConfiguration31", self)
                    

class uma_MethodConfiguration(MethodUnit):

    def __init__(self, baseConfiguration: str, methodPluginSelection: str, methodPackageSelection: str, defaultView: str, processView: str, subtractedCategory: str, addedCategory: str, uma_MethodConfiguration: "uma_DocumentRoot" = None, uma_MethodConfiguration31: "uma_MethodLibrary" = None):
        self.baseConfiguration = baseConfiguration
        self.methodPluginSelection = methodPluginSelection
        self.methodPackageSelection = methodPackageSelection
        self.defaultView = defaultView
        self.processView = processView
        self.subtractedCategory = subtractedCategory
        self.addedCategory = addedCategory
        self.uma_MethodConfiguration = uma_MethodConfiguration
        self.uma_MethodConfiguration31 = uma_MethodConfiguration31
        
    @property
    def methodPluginSelection(self) -> str:
        return self.__methodPluginSelection

    @methodPluginSelection.setter
    def methodPluginSelection(self, methodPluginSelection: str):
        self.__methodPluginSelection = methodPluginSelection

    @property
    def defaultView(self) -> str:
        return self.__defaultView

    @defaultView.setter
    def defaultView(self, defaultView: str):
        self.__defaultView = defaultView

    @property
    def subtractedCategory(self) -> str:
        return self.__subtractedCategory

    @subtractedCategory.setter
    def subtractedCategory(self, subtractedCategory: str):
        self.__subtractedCategory = subtractedCategory

    @property
    def methodPackageSelection(self) -> str:
        return self.__methodPackageSelection

    @methodPackageSelection.setter
    def methodPackageSelection(self, methodPackageSelection: str):
        self.__methodPackageSelection = methodPackageSelection

    @property
    def baseConfiguration(self) -> str:
        return self.__baseConfiguration

    @baseConfiguration.setter
    def baseConfiguration(self, baseConfiguration: str):
        self.__baseConfiguration = baseConfiguration

    @property
    def processView(self) -> str:
        return self.__processView

    @processView.setter
    def processView(self, processView: str):
        self.__processView = processView

    @property
    def addedCategory(self) -> str:
        return self.__addedCategory

    @addedCategory.setter
    def addedCategory(self, addedCategory: str):
        self.__addedCategory = addedCategory

    @property
    def uma_MethodConfiguration31(self):
        return self.__uma_MethodConfiguration31

    @uma_MethodConfiguration31.setter
    def uma_MethodConfiguration31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_MethodConfiguration__uma_MethodConfiguration31", None)
        self.__uma_MethodConfiguration31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_MethodLibrary30"):
                opp_val = getattr(old_value, "uma_MethodLibrary30", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_MethodLibrary30"):
                opp_val = getattr(value, "uma_MethodLibrary30", None)
                if opp_val is None:
                    setattr(value, "uma_MethodLibrary30", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uma_MethodConfiguration(self):
        return self.__uma_MethodConfiguration

    @uma_MethodConfiguration.setter
    def uma_MethodConfiguration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_MethodConfiguration__uma_MethodConfiguration", None)
        self.__uma_MethodConfiguration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_DocumentRoot16"):
                opp_val = getattr(old_value, "uma_DocumentRoot16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_DocumentRoot16"):
                opp_val = getattr(value, "uma_DocumentRoot16", None)
                if opp_val is None:
                    setattr(value, "uma_DocumentRoot16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class uma_ContentDescription(MethodUnit):

    def __init__(self, mainDescription: str, keyConsiderations: str, externalId: str, uma_ContentDescription: set["uma_Section"] = None, uma_ContentDescription8: "uma_DescribableElement" = None):
        self.mainDescription = mainDescription
        self.keyConsiderations = keyConsiderations
        self.externalId = externalId
        self.uma_ContentDescription = uma_ContentDescription if uma_ContentDescription is not None else set()
        self.uma_ContentDescription8 = uma_ContentDescription8
        
    @property
    def keyConsiderations(self) -> str:
        return self.__keyConsiderations

    @keyConsiderations.setter
    def keyConsiderations(self, keyConsiderations: str):
        self.__keyConsiderations = keyConsiderations

    @property
    def externalId(self) -> str:
        return self.__externalId

    @externalId.setter
    def externalId(self, externalId: str):
        self.__externalId = externalId

    @property
    def mainDescription(self) -> str:
        return self.__mainDescription

    @mainDescription.setter
    def mainDescription(self, mainDescription: str):
        self.__mainDescription = mainDescription

    @property
    def uma_ContentDescription(self):
        return self.__uma_ContentDescription

    @uma_ContentDescription.setter
    def uma_ContentDescription(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_ContentDescription__uma_ContentDescription", None)
        self.__uma_ContentDescription = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uma_Section"):
                    opp_val = getattr(item, "uma_Section", None)
                    
                    if opp_val == self:
                        setattr(item, "uma_Section", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uma_Section"):
                    opp_val = getattr(item, "uma_Section", None)
                    
                    setattr(item, "uma_Section", self)
                    

    @property
    def uma_ContentDescription8(self):
        return self.__uma_ContentDescription8

    @uma_ContentDescription8.setter
    def uma_ContentDescription8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_ContentDescription__uma_ContentDescription8", None)
        self.__uma_ContentDescription8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_DescribableElement"):
                opp_val = getattr(old_value, "uma_DescribableElement", None)
                if opp_val == self:
                    setattr(old_value, "uma_DescribableElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_DescribableElement"):
                opp_val = getattr(value, "uma_DescribableElement", None)
                setattr(value, "uma_DescribableElement", self)

class ContentElement:

    pass
class uma_Kind(ContentElement):

    def __init__(self, applicableMetaClassInfo: str):
        self.applicableMetaClassInfo = applicableMetaClassInfo
        
    @property
    def applicableMetaClassInfo(self) -> str:
        return self.__applicableMetaClassInfo

    @applicableMetaClassInfo.setter
    def applicableMetaClassInfo(self, applicableMetaClassInfo: str):
        self.__applicableMetaClassInfo = applicableMetaClassInfo

class uma_WorkProduct(ContentElement):

    def __init__(self, group2: str, estimate: str, estimationConsiderations: str, report: str, template: str, toolMentor: str):
        self.group2 = group2
        self.estimate = estimate
        self.estimationConsiderations = estimationConsiderations
        self.report = report
        self.template = template
        self.toolMentor = toolMentor
        
    @property
    def report(self) -> str:
        return self.__report

    @report.setter
    def report(self, report: str):
        self.__report = report

    @property
    def group2(self) -> str:
        return self.__group2

    @group2.setter
    def group2(self, group2: str):
        self.__group2 = group2

    @property
    def toolMentor(self) -> str:
        return self.__toolMentor

    @toolMentor.setter
    def toolMentor(self, toolMentor: str):
        self.__toolMentor = toolMentor

    @property
    def template(self) -> str:
        return self.__template

    @template.setter
    def template(self, template: str):
        self.__template = template

    @property
    def estimationConsiderations(self) -> str:
        return self.__estimationConsiderations

    @estimationConsiderations.setter
    def estimationConsiderations(self, estimationConsiderations: str):
        self.__estimationConsiderations = estimationConsiderations

    @property
    def estimate(self) -> str:
        return self.__estimate

    @estimate.setter
    def estimate(self, estimate: str):
        self.__estimate = estimate

class uma_Guidance(ContentElement):

    pass
class uma_Task(ContentElement):

    def __init__(self, group2: str, mandatoryInput: str, output: str, additionallyPerformedBy: str, precondition: str, postcondition: str, performedBy: str, optionalInput: str, estimate: str, estimationConsiderations: str, toolMentor: str):
        self.group2 = group2
        self.mandatoryInput = mandatoryInput
        self.output = output
        self.additionallyPerformedBy = additionallyPerformedBy
        self.precondition = precondition
        self.postcondition = postcondition
        self.performedBy = performedBy
        self.optionalInput = optionalInput
        self.estimate = estimate
        self.estimationConsiderations = estimationConsiderations
        self.toolMentor = toolMentor
        
    @property
    def precondition(self) -> str:
        return self.__precondition

    @precondition.setter
    def precondition(self, precondition: str):
        self.__precondition = precondition

    @property
    def estimationConsiderations(self) -> str:
        return self.__estimationConsiderations

    @estimationConsiderations.setter
    def estimationConsiderations(self, estimationConsiderations: str):
        self.__estimationConsiderations = estimationConsiderations

    @property
    def toolMentor(self) -> str:
        return self.__toolMentor

    @toolMentor.setter
    def toolMentor(self, toolMentor: str):
        self.__toolMentor = toolMentor

    @property
    def output(self) -> str:
        return self.__output

    @output.setter
    def output(self, output: str):
        self.__output = output

    @property
    def group2(self) -> str:
        return self.__group2

    @group2.setter
    def group2(self, group2: str):
        self.__group2 = group2

    @property
    def postcondition(self) -> str:
        return self.__postcondition

    @postcondition.setter
    def postcondition(self, postcondition: str):
        self.__postcondition = postcondition

    @property
    def optionalInput(self) -> str:
        return self.__optionalInput

    @optionalInput.setter
    def optionalInput(self, optionalInput: str):
        self.__optionalInput = optionalInput

    @property
    def performedBy(self) -> str:
        return self.__performedBy

    @performedBy.setter
    def performedBy(self, performedBy: str):
        self.__performedBy = performedBy

    @property
    def additionallyPerformedBy(self) -> str:
        return self.__additionallyPerformedBy

    @additionallyPerformedBy.setter
    def additionallyPerformedBy(self, additionallyPerformedBy: str):
        self.__additionallyPerformedBy = additionallyPerformedBy

    @property
    def estimate(self) -> str:
        return self.__estimate

    @estimate.setter
    def estimate(self, estimate: str):
        self.__estimate = estimate

    @property
    def mandatoryInput(self) -> str:
        return self.__mandatoryInput

    @mandatoryInput.setter
    def mandatoryInput(self, mandatoryInput: str):
        self.__mandatoryInput = mandatoryInput

class uma_ContentCategory(ContentElement):

    pass
class MethodElement:

    pass
class uma_DescribableElement(MethodElement):

    def __init__(self, fulfill: str, isAbstract: str, nodeicon: str, shapeicon: str, uma_DescribableElement: "uma_ContentDescription" = None):
        self.fulfill = fulfill
        self.isAbstract = isAbstract
        self.nodeicon = nodeicon
        self.shapeicon = shapeicon
        self.uma_DescribableElement = uma_DescribableElement
        
    @property
    def shapeicon(self) -> str:
        return self.__shapeicon

    @shapeicon.setter
    def shapeicon(self, shapeicon: str):
        self.__shapeicon = shapeicon

    @property
    def nodeicon(self) -> str:
        return self.__nodeicon

    @nodeicon.setter
    def nodeicon(self, nodeicon: str):
        self.__nodeicon = nodeicon

    @property
    def fulfill(self) -> str:
        return self.__fulfill

    @fulfill.setter
    def fulfill(self, fulfill: str):
        self.__fulfill = fulfill

    @property
    def isAbstract(self) -> str:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: str):
        self.__isAbstract = isAbstract

    @property
    def uma_DescribableElement(self):
        return self.__uma_DescribableElement

    @uma_DescribableElement.setter
    def uma_DescribableElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_DescribableElement__uma_DescribableElement", None)
        self.__uma_DescribableElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_ContentDescription8"):
                opp_val = getattr(old_value, "uma_ContentDescription8", None)
                if opp_val == self:
                    setattr(old_value, "uma_ContentDescription8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_ContentDescription8"):
                opp_val = getattr(value, "uma_ContentDescription8", None)
                setattr(value, "uma_ContentDescription8", self)

class uma_WorkDefinition(MethodElement):

    def __init__(self, precondition: str, postcondition: str):
        self.precondition = precondition
        self.postcondition = postcondition
        
    @property
    def postcondition(self) -> str:
        return self.__postcondition

    @postcondition.setter
    def postcondition(self, postcondition: str):
        self.__postcondition = postcondition

    @property
    def precondition(self) -> str:
        return self.__precondition

    @precondition.setter
    def precondition(self, precondition: str):
        self.__precondition = precondition

class uma_MethodPackage(MethodElement):

    def __init__(self, global: str, group1: str, reusedPackage: str, uma_MethodPackage: "uma_MethodPackage" = None, uma_MethodPackage32: set["uma_MethodPackage"] = None, uma_MethodPackage36: "uma_MethodPlugin" = None):
        self.global = global
        self.group1 = group1
        self.reusedPackage = reusedPackage
        self.uma_MethodPackage = uma_MethodPackage
        self.uma_MethodPackage32 = uma_MethodPackage32 if uma_MethodPackage32 is not None else set()
        self.uma_MethodPackage36 = uma_MethodPackage36
        
    @property
    def group1(self) -> str:
        return self.__group1

    @group1.setter
    def group1(self, group1: str):
        self.__group1 = group1

    @property
    def global(self) -> str:
        return self.__global

    @global.setter
    def global(self, global: str):
        self.__global = global

    @property
    def reusedPackage(self) -> str:
        return self.__reusedPackage

    @reusedPackage.setter
    def reusedPackage(self, reusedPackage: str):
        self.__reusedPackage = reusedPackage

    @property
    def uma_MethodPackage36(self):
        return self.__uma_MethodPackage36

    @uma_MethodPackage36.setter
    def uma_MethodPackage36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_MethodPackage__uma_MethodPackage36", None)
        self.__uma_MethodPackage36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_MethodPlugin35"):
                opp_val = getattr(old_value, "uma_MethodPlugin35", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_MethodPlugin35"):
                opp_val = getattr(value, "uma_MethodPlugin35", None)
                if opp_val is None:
                    setattr(value, "uma_MethodPlugin35", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uma_MethodPackage(self):
        return self.__uma_MethodPackage

    @uma_MethodPackage.setter
    def uma_MethodPackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_MethodPackage__uma_MethodPackage", None)
        self.__uma_MethodPackage = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_MethodPackage32"):
                opp_val = getattr(old_value, "uma_MethodPackage32", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_MethodPackage32"):
                opp_val = getattr(value, "uma_MethodPackage32", None)
                if opp_val is None:
                    setattr(value, "uma_MethodPackage32", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uma_MethodPackage32(self):
        return self.__uma_MethodPackage32

    @uma_MethodPackage32.setter
    def uma_MethodPackage32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_MethodPackage__uma_MethodPackage32", None)
        self.__uma_MethodPackage32 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uma_MethodPackage"):
                    opp_val = getattr(item, "uma_MethodPackage", None)
                    
                    if opp_val == self:
                        setattr(item, "uma_MethodPackage", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uma_MethodPackage"):
                    opp_val = getattr(item, "uma_MethodPackage", None)
                    
                    setattr(item, "uma_MethodPackage", self)
                    

class uma_Section(MethodElement):

    def __init__(self, predecessor: str, description: str, sectionName: str, variabilityBasedOnElement: str, variabilityType: str, uma_Section: "uma_ContentDescription" = None, uma_Section49: "uma_Section" = None, uma_Section47: "uma_Section" = None, uma_Section52: "uma_TaskDescriptor" = None):
        self.predecessor = predecessor
        self.description = description
        self.sectionName = sectionName
        self.variabilityBasedOnElement = variabilityBasedOnElement
        self.variabilityType = variabilityType
        self.uma_Section = uma_Section
        self.uma_Section49 = uma_Section49
        self.uma_Section47 = uma_Section47
        self.uma_Section52 = uma_Section52
        
    @property
    def variabilityBasedOnElement(self) -> str:
        return self.__variabilityBasedOnElement

    @variabilityBasedOnElement.setter
    def variabilityBasedOnElement(self, variabilityBasedOnElement: str):
        self.__variabilityBasedOnElement = variabilityBasedOnElement

    @property
    def variabilityType(self) -> str:
        return self.__variabilityType

    @variabilityType.setter
    def variabilityType(self, variabilityType: str):
        self.__variabilityType = variabilityType

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def predecessor(self) -> str:
        return self.__predecessor

    @predecessor.setter
    def predecessor(self, predecessor: str):
        self.__predecessor = predecessor

    @property
    def sectionName(self) -> str:
        return self.__sectionName

    @sectionName.setter
    def sectionName(self, sectionName: str):
        self.__sectionName = sectionName

    @property
    def uma_Section49(self):
        return self.__uma_Section49

    @uma_Section49.setter
    def uma_Section49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Section__uma_Section49", None)
        self.__uma_Section49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_Section47"):
                opp_val = getattr(old_value, "uma_Section47", None)
                if opp_val == self:
                    setattr(old_value, "uma_Section47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_Section47"):
                opp_val = getattr(value, "uma_Section47", None)
                setattr(value, "uma_Section47", self)

    @property
    def uma_Section52(self):
        return self.__uma_Section52

    @uma_Section52.setter
    def uma_Section52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Section__uma_Section52", None)
        self.__uma_Section52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_TaskDescriptor51"):
                opp_val = getattr(old_value, "uma_TaskDescriptor51", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_TaskDescriptor51"):
                opp_val = getattr(value, "uma_TaskDescriptor51", None)
                if opp_val is None:
                    setattr(value, "uma_TaskDescriptor51", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uma_Section(self):
        return self.__uma_Section

    @uma_Section.setter
    def uma_Section(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Section__uma_Section", None)
        self.__uma_Section = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_ContentDescription"):
                opp_val = getattr(old_value, "uma_ContentDescription", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_ContentDescription"):
                opp_val = getattr(value, "uma_ContentDescription", None)
                if opp_val is None:
                    setattr(value, "uma_ContentDescription", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uma_Section47(self):
        return self.__uma_Section47

    @uma_Section47.setter
    def uma_Section47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Section__uma_Section47", None)
        self.__uma_Section47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_Section49"):
                opp_val = getattr(old_value, "uma_Section49", None)
                if opp_val == self:
                    setattr(old_value, "uma_Section49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_Section49"):
                opp_val = getattr(value, "uma_Section49", None)
                setattr(value, "uma_Section49", self)

class uma_MethodUnit(MethodElement):

    def __init__(self, copyright: str, authors: str, changeDate: str, changeDescription: str, version: str):
        self.copyright = copyright
        self.authors = authors
        self.changeDate = changeDate
        self.changeDescription = changeDescription
        self.version = version
        
    @property
    def authors(self) -> str:
        return self.__authors

    @authors.setter
    def authors(self, authors: str):
        self.__authors = authors

    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def changeDate(self) -> str:
        return self.__changeDate

    @changeDate.setter
    def changeDate(self, changeDate: str):
        self.__changeDate = changeDate

    @property
    def changeDescription(self) -> str:
        return self.__changeDescription

    @changeDescription.setter
    def changeDescription(self, changeDescription: str):
        self.__changeDescription = changeDescription

    @property
    def copyright(self) -> str:
        return self.__copyright

    @copyright.setter
    def copyright(self, copyright: str):
        self.__copyright = copyright

class uma_Constraint(MethodElement):

    def __init__(self, mainDescription: str, uma_Constraint: "uma_MethodElement" = None):
        self.mainDescription = mainDescription
        self.uma_Constraint = uma_Constraint
        
    @property
    def mainDescription(self) -> str:
        return self.__mainDescription

    @mainDescription.setter
    def mainDescription(self, mainDescription: str):
        self.__mainDescription = mainDescription

    @property
    def uma_Constraint(self):
        return self.__uma_Constraint

    @uma_Constraint.setter
    def uma_Constraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Constraint__uma_Constraint", None)
        self.__uma_Constraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_MethodElement"):
                opp_val = getattr(old_value, "uma_MethodElement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_MethodElement"):
                opp_val = getattr(value, "uma_MethodElement", None)
                if opp_val is None:
                    setattr(value, "uma_MethodElement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class uma_Role(ContentElement):

    def __init__(self, group2: str, responsibleFor: str, uma_Role: "uma_CompositeRole" = None):
        self.group2 = group2
        self.responsibleFor = responsibleFor
        self.uma_Role = uma_Role
        
    @property
    def group2(self) -> str:
        return self.__group2

    @group2.setter
    def group2(self, group2: str):
        self.__group2 = group2

    @property
    def responsibleFor(self) -> str:
        return self.__responsibleFor

    @responsibleFor.setter
    def responsibleFor(self, responsibleFor: str):
        self.__responsibleFor = responsibleFor

    @property
    def uma_Role(self):
        return self.__uma_Role

    @uma_Role.setter
    def uma_Role(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Role__uma_Role", None)
        self.__uma_Role = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_CompositeRole"):
                opp_val = getattr(old_value, "uma_CompositeRole", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_CompositeRole"):
                opp_val = getattr(value, "uma_CompositeRole", None)
                if opp_val is None:
                    setattr(value, "uma_CompositeRole", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class RoleDescriptor:

    pass
class uma_CompositeRole(RoleDescriptor):

    def __init__(self, group2: str, uma_CompositeRole: set["uma_Role"] = None):
        self.group2 = group2
        self.uma_CompositeRole = uma_CompositeRole if uma_CompositeRole is not None else set()
        
    @property
    def group2(self) -> str:
        return self.__group2

    @group2.setter
    def group2(self, group2: str):
        self.__group2 = group2

    @property
    def uma_CompositeRole(self):
        return self.__uma_CompositeRole

    @uma_CompositeRole.setter
    def uma_CompositeRole(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_CompositeRole__uma_CompositeRole", None)
        self.__uma_CompositeRole = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uma_Role"):
                    opp_val = getattr(item, "uma_Role", None)
                    
                    if opp_val == self:
                        setattr(item, "uma_Role", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uma_Role"):
                    opp_val = getattr(item, "uma_Role", None)
                    
                    setattr(item, "uma_Role", self)
                    

class Guidance:

    pass
class uma_Guideline(Guidance):

    pass
class uma_Estimate(Guidance):

    def __init__(self, estimationConsiderations: str, group2: str, estimationMetric: str):
        self.estimationConsiderations = estimationConsiderations
        self.group2 = group2
        self.estimationMetric = estimationMetric
        
    @property
    def group2(self) -> str:
        return self.__group2

    @group2.setter
    def group2(self, group2: str):
        self.__group2 = group2

    @property
    def estimationMetric(self) -> str:
        return self.__estimationMetric

    @estimationMetric.setter
    def estimationMetric(self, estimationMetric: str):
        self.__estimationMetric = estimationMetric

    @property
    def estimationConsiderations(self) -> str:
        return self.__estimationConsiderations

    @estimationConsiderations.setter
    def estimationConsiderations(self, estimationConsiderations: str):
        self.__estimationConsiderations = estimationConsiderations

class uma_Template(Guidance):

    pass
class uma_SupportingMaterial(Guidance):

    pass
class uma_Practice(Guidance):

    def __init__(self, group2: str, activityReference: str, contentReference: str, uma_Practice: "uma_Practice" = None, uma_Practice37: set["uma_Practice"] = None):
        self.group2 = group2
        self.activityReference = activityReference
        self.contentReference = contentReference
        self.uma_Practice = uma_Practice
        self.uma_Practice37 = uma_Practice37 if uma_Practice37 is not None else set()
        
    @property
    def contentReference(self) -> str:
        return self.__contentReference

    @contentReference.setter
    def contentReference(self, contentReference: str):
        self.__contentReference = contentReference

    @property
    def activityReference(self) -> str:
        return self.__activityReference

    @activityReference.setter
    def activityReference(self, activityReference: str):
        self.__activityReference = activityReference

    @property
    def group2(self) -> str:
        return self.__group2

    @group2.setter
    def group2(self, group2: str):
        self.__group2 = group2

    @property
    def uma_Practice(self):
        return self.__uma_Practice

    @uma_Practice.setter
    def uma_Practice(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Practice__uma_Practice", None)
        self.__uma_Practice = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_Practice37"):
                opp_val = getattr(old_value, "uma_Practice37", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_Practice37"):
                opp_val = getattr(value, "uma_Practice37", None)
                if opp_val is None:
                    setattr(value, "uma_Practice37", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uma_Practice37(self):
        return self.__uma_Practice37

    @uma_Practice37.setter
    def uma_Practice37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Practice__uma_Practice37", None)
        self.__uma_Practice37 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uma_Practice"):
                    opp_val = getattr(item, "uma_Practice", None)
                    
                    if opp_val == self:
                        setattr(item, "uma_Practice", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uma_Practice"):
                    opp_val = getattr(item, "uma_Practice", None)
                    
                    setattr(item, "uma_Practice", self)
                    

class uma_EstimatingMetric(Guidance):

    pass
class uma_Roadmap(Guidance):

    pass
class uma_ToolMentor(Guidance):

    pass
class uma_TermDefinition(Guidance):

    pass
class uma_Example(Guidance):

    pass
class uma_EstimationConsiderations(Guidance):

    pass
class uma_ReusableAsset(Guidance):

    pass
class uma_Report(Guidance):

    pass
class uma_Concept(Guidance):

    pass
class uma_Checklist(Guidance):

    pass
class Process:

    pass
class uma_ProcessPlanningTemplate(Process):

    def __init__(self, group4: str, baseProcess: str):
        self.group4 = group4
        self.baseProcess = baseProcess
        
    @property
    def group4(self) -> str:
        return self.__group4

    @group4.setter
    def group4(self, group4: str):
        self.__group4 = group4

    @property
    def baseProcess(self) -> str:
        return self.__baseProcess

    @baseProcess.setter
    def baseProcess(self, baseProcess: str):
        self.__baseProcess = baseProcess

class uma_DeliveryProcess(Process):

    def __init__(self, group4: str, communicationsMaterial: str, educationMaterial: str):
        self.group4 = group4
        self.communicationsMaterial = communicationsMaterial
        self.educationMaterial = educationMaterial
        
    @property
    def educationMaterial(self) -> str:
        return self.__educationMaterial

    @educationMaterial.setter
    def educationMaterial(self, educationMaterial: str):
        self.__educationMaterial = educationMaterial

    @property
    def communicationsMaterial(self) -> str:
        return self.__communicationsMaterial

    @communicationsMaterial.setter
    def communicationsMaterial(self, communicationsMaterial: str):
        self.__communicationsMaterial = communicationsMaterial

    @property
    def group4(self) -> str:
        return self.__group4

    @group4.setter
    def group4(self, group4: str):
        self.__group4 = group4

class uma_CapabilityPattern(Process):

    pass
class MethodPackage:

    pass
class uma_ContentPackage(MethodPackage):

    def __init__(self, group2: str, uma_ContentPackage: set["uma_ContentElement"] = None):
        self.group2 = group2
        self.uma_ContentPackage = uma_ContentPackage if uma_ContentPackage is not None else set()
        
    @property
    def group2(self) -> str:
        return self.__group2

    @group2.setter
    def group2(self, group2: str):
        self.__group2 = group2

    @property
    def uma_ContentPackage(self):
        return self.__uma_ContentPackage

    @uma_ContentPackage.setter
    def uma_ContentPackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_ContentPackage__uma_ContentPackage", None)
        self.__uma_ContentPackage = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uma_ContentElement"):
                    opp_val = getattr(item, "uma_ContentElement", None)
                    
                    if opp_val == self:
                        setattr(item, "uma_ContentElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uma_ContentElement"):
                    opp_val = getattr(item, "uma_ContentElement", None)
                    
                    setattr(item, "uma_ContentElement", self)
                    

class uma_ProcessPackage(MethodPackage):

    def __init__(self, group2: str, uma_ProcessPackage: set["uma_ProcessElement"] = None):
        self.group2 = group2
        self.uma_ProcessPackage = uma_ProcessPackage if uma_ProcessPackage is not None else set()
        
    @property
    def group2(self) -> str:
        return self.__group2

    @group2.setter
    def group2(self, group2: str):
        self.__group2 = group2

    @property
    def uma_ProcessPackage(self):
        return self.__uma_ProcessPackage

    @uma_ProcessPackage.setter
    def uma_ProcessPackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_ProcessPackage__uma_ProcessPackage", None)
        self.__uma_ProcessPackage = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uma_ProcessElement"):
                    opp_val = getattr(item, "uma_ProcessElement", None)
                    
                    if opp_val == self:
                        setattr(item, "uma_ProcessElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uma_ProcessElement"):
                    opp_val = getattr(item, "uma_ProcessElement", None)
                    
                    setattr(item, "uma_ProcessElement", self)
                    

class uma_ContentCategoryPackage(MethodPackage):

    def __init__(self, group2: str, uma_ContentCategoryPackage: set["uma_ContentCategory"] = None):
        self.group2 = group2
        self.uma_ContentCategoryPackage = uma_ContentCategoryPackage if uma_ContentCategoryPackage is not None else set()
        
    @property
    def group2(self) -> str:
        return self.__group2

    @group2.setter
    def group2(self, group2: str):
        self.__group2 = group2

    @property
    def uma_ContentCategoryPackage(self):
        return self.__uma_ContentCategoryPackage

    @uma_ContentCategoryPackage.setter
    def uma_ContentCategoryPackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_ContentCategoryPackage__uma_ContentCategoryPackage", None)
        self.__uma_ContentCategoryPackage = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uma_ContentCategory"):
                    opp_val = getattr(item, "uma_ContentCategory", None)
                    
                    if opp_val == self:
                        setattr(item, "uma_ContentCategory", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uma_ContentCategory"):
                    opp_val = getattr(item, "uma_ContentCategory", None)
                    
                    setattr(item, "uma_ContentCategory", self)
                    

class ContentDescription:

    pass
class uma_WorkProductDescription(ContentDescription):

    def __init__(self, impactOfNotHaving: str, purpose: str, reasonsForNotNeeding: str):
        self.impactOfNotHaving = impactOfNotHaving
        self.purpose = purpose
        self.reasonsForNotNeeding = reasonsForNotNeeding
        
    @property
    def reasonsForNotNeeding(self) -> str:
        return self.__reasonsForNotNeeding

    @reasonsForNotNeeding.setter
    def reasonsForNotNeeding(self, reasonsForNotNeeding: str):
        self.__reasonsForNotNeeding = reasonsForNotNeeding

    @property
    def purpose(self) -> str:
        return self.__purpose

    @purpose.setter
    def purpose(self, purpose: str):
        self.__purpose = purpose

    @property
    def impactOfNotHaving(self) -> str:
        return self.__impactOfNotHaving

    @impactOfNotHaving.setter
    def impactOfNotHaving(self, impactOfNotHaving: str):
        self.__impactOfNotHaving = impactOfNotHaving

class uma_GuidanceDescription(ContentDescription):

    def __init__(self, attachment: str):
        self.attachment = attachment
        
    @property
    def attachment(self) -> str:
        return self.__attachment

    @attachment.setter
    def attachment(self, attachment: str):
        self.__attachment = attachment

class uma_TaskDescription(ContentDescription):

    def __init__(self, alternatives: str, purpose: str):
        self.alternatives = alternatives
        self.purpose = purpose
        
    @property
    def alternatives(self) -> str:
        return self.__alternatives

    @alternatives.setter
    def alternatives(self, alternatives: str):
        self.__alternatives = alternatives

    @property
    def purpose(self) -> str:
        return self.__purpose

    @purpose.setter
    def purpose(self, purpose: str):
        self.__purpose = purpose

class uma_PracticeDescription(ContentDescription):

    def __init__(self, additionalInfo: str, application: str, background: str, goals: str, levelsOfAdoption: str, problem: str):
        self.additionalInfo = additionalInfo
        self.application = application
        self.background = background
        self.goals = goals
        self.levelsOfAdoption = levelsOfAdoption
        self.problem = problem
        
    @property
    def problem(self) -> str:
        return self.__problem

    @problem.setter
    def problem(self, problem: str):
        self.__problem = problem

    @property
    def background(self) -> str:
        return self.__background

    @background.setter
    def background(self, background: str):
        self.__background = background

    @property
    def levelsOfAdoption(self) -> str:
        return self.__levelsOfAdoption

    @levelsOfAdoption.setter
    def levelsOfAdoption(self, levelsOfAdoption: str):
        self.__levelsOfAdoption = levelsOfAdoption

    @property
    def goals(self) -> str:
        return self.__goals

    @goals.setter
    def goals(self, goals: str):
        self.__goals = goals

    @property
    def application(self) -> str:
        return self.__application

    @application.setter
    def application(self, application: str):
        self.__application = application

    @property
    def additionalInfo(self) -> str:
        return self.__additionalInfo

    @additionalInfo.setter
    def additionalInfo(self, additionalInfo: str):
        self.__additionalInfo = additionalInfo

class uma_RoleDescription(ContentDescription):

    def __init__(self, assignmentApproaches: str, skills: str, synonyms: str):
        self.assignmentApproaches = assignmentApproaches
        self.skills = skills
        self.synonyms = synonyms
        
    @property
    def synonyms(self) -> str:
        return self.__synonyms

    @synonyms.setter
    def synonyms(self, synonyms: str):
        self.__synonyms = synonyms

    @property
    def skills(self) -> str:
        return self.__skills

    @skills.setter
    def skills(self, skills: str):
        self.__skills = skills

    @property
    def assignmentApproaches(self) -> str:
        return self.__assignmentApproaches

    @assignmentApproaches.setter
    def assignmentApproaches(self, assignmentApproaches: str):
        self.__assignmentApproaches = assignmentApproaches

class uma_BreakdownElementDescription(ContentDescription):

    def __init__(self, usageGuidance: str):
        self.usageGuidance = usageGuidance
        
    @property
    def usageGuidance(self) -> str:
        return self.__usageGuidance

    @usageGuidance.setter
    def usageGuidance(self, usageGuidance: str):
        self.__usageGuidance = usageGuidance

class ProcessElement:

    pass
class uma_PlanningData(ProcessElement):

    def __init__(self, finishDate: str, rank: str, startDate: str):
        self.finishDate = finishDate
        self.rank = rank
        self.startDate = startDate
        
    @property
    def finishDate(self) -> str:
        return self.__finishDate

    @finishDate.setter
    def finishDate(self, finishDate: str):
        self.__finishDate = finishDate

    @property
    def startDate(self) -> str:
        return self.__startDate

    @startDate.setter
    def startDate(self, startDate: str):
        self.__startDate = startDate

    @property
    def rank(self) -> str:
        return self.__rank

    @rank.setter
    def rank(self, rank: str):
        self.__rank = rank

class uma_BreakdownElement(ProcessElement):

    def __init__(self, planningData: str, superActivity: str, group1: str, presentedAfter: str, presentedBefore: str, checklist: str, concept: str, example: str, guideline: str, reusableAsset: str, supportingMaterial: str, whitepaper: str, hasMultipleOccurrences: str, isOptional: str, isPlanned: str, prefix: str, uma_BreakdownElement: "uma_Activity" = None):
        self.planningData = planningData
        self.superActivity = superActivity
        self.group1 = group1
        self.presentedAfter = presentedAfter
        self.presentedBefore = presentedBefore
        self.checklist = checklist
        self.concept = concept
        self.example = example
        self.guideline = guideline
        self.reusableAsset = reusableAsset
        self.supportingMaterial = supportingMaterial
        self.whitepaper = whitepaper
        self.hasMultipleOccurrences = hasMultipleOccurrences
        self.isOptional = isOptional
        self.isPlanned = isPlanned
        self.prefix = prefix
        self.uma_BreakdownElement = uma_BreakdownElement
        
    @property
    def example(self) -> str:
        return self.__example

    @example.setter
    def example(self, example: str):
        self.__example = example

    @property
    def reusableAsset(self) -> str:
        return self.__reusableAsset

    @reusableAsset.setter
    def reusableAsset(self, reusableAsset: str):
        self.__reusableAsset = reusableAsset

    @property
    def supportingMaterial(self) -> str:
        return self.__supportingMaterial

    @supportingMaterial.setter
    def supportingMaterial(self, supportingMaterial: str):
        self.__supportingMaterial = supportingMaterial

    @property
    def isOptional(self) -> str:
        return self.__isOptional

    @isOptional.setter
    def isOptional(self, isOptional: str):
        self.__isOptional = isOptional

    @property
    def prefix(self) -> str:
        return self.__prefix

    @prefix.setter
    def prefix(self, prefix: str):
        self.__prefix = prefix

    @property
    def superActivity(self) -> str:
        return self.__superActivity

    @superActivity.setter
    def superActivity(self, superActivity: str):
        self.__superActivity = superActivity

    @property
    def guideline(self) -> str:
        return self.__guideline

    @guideline.setter
    def guideline(self, guideline: str):
        self.__guideline = guideline

    @property
    def hasMultipleOccurrences(self) -> str:
        return self.__hasMultipleOccurrences

    @hasMultipleOccurrences.setter
    def hasMultipleOccurrences(self, hasMultipleOccurrences: str):
        self.__hasMultipleOccurrences = hasMultipleOccurrences

    @property
    def planningData(self) -> str:
        return self.__planningData

    @planningData.setter
    def planningData(self, planningData: str):
        self.__planningData = planningData

    @property
    def presentedBefore(self) -> str:
        return self.__presentedBefore

    @presentedBefore.setter
    def presentedBefore(self, presentedBefore: str):
        self.__presentedBefore = presentedBefore

    @property
    def group1(self) -> str:
        return self.__group1

    @group1.setter
    def group1(self, group1: str):
        self.__group1 = group1

    @property
    def checklist(self) -> str:
        return self.__checklist

    @checklist.setter
    def checklist(self, checklist: str):
        self.__checklist = checklist

    @property
    def concept(self) -> str:
        return self.__concept

    @concept.setter
    def concept(self, concept: str):
        self.__concept = concept

    @property
    def whitepaper(self) -> str:
        return self.__whitepaper

    @whitepaper.setter
    def whitepaper(self, whitepaper: str):
        self.__whitepaper = whitepaper

    @property
    def isPlanned(self) -> str:
        return self.__isPlanned

    @isPlanned.setter
    def isPlanned(self, isPlanned: str):
        self.__isPlanned = isPlanned

    @property
    def presentedAfter(self) -> str:
        return self.__presentedAfter

    @presentedAfter.setter
    def presentedAfter(self, presentedAfter: str):
        self.__presentedAfter = presentedAfter

    @property
    def uma_BreakdownElement(self):
        return self.__uma_BreakdownElement

    @uma_BreakdownElement.setter
    def uma_BreakdownElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_BreakdownElement__uma_BreakdownElement", None)
        self.__uma_BreakdownElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_Activity"):
                opp_val = getattr(old_value, "uma_Activity", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_Activity"):
                opp_val = getattr(value, "uma_Activity", None)
                if opp_val is None:
                    setattr(value, "uma_Activity", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class WorkProductDescription:

    pass
class uma_DeliverableDescription(WorkProductDescription):

    def __init__(self, externalDescription: str, packagingGuidance: str):
        self.externalDescription = externalDescription
        self.packagingGuidance = packagingGuidance
        
    @property
    def packagingGuidance(self) -> str:
        return self.__packagingGuidance

    @packagingGuidance.setter
    def packagingGuidance(self, packagingGuidance: str):
        self.__packagingGuidance = packagingGuidance

    @property
    def externalDescription(self) -> str:
        return self.__externalDescription

    @externalDescription.setter
    def externalDescription(self, externalDescription: str):
        self.__externalDescription = externalDescription

class uma_ArtifactDescription(WorkProductDescription):

    def __init__(self, briefOutline: str, representationOptions: str, representation: str, notation: str):
        self.briefOutline = briefOutline
        self.representationOptions = representationOptions
        self.representation = representation
        self.notation = notation
        
    @property
    def notation(self) -> str:
        return self.__notation

    @notation.setter
    def notation(self, notation: str):
        self.__notation = notation

    @property
    def representationOptions(self) -> str:
        return self.__representationOptions

    @representationOptions.setter
    def representationOptions(self, representationOptions: str):
        self.__representationOptions = representationOptions

    @property
    def briefOutline(self) -> str:
        return self.__briefOutline

    @briefOutline.setter
    def briefOutline(self, briefOutline: str):
        self.__briefOutline = briefOutline

    @property
    def representation(self) -> str:
        return self.__representation

    @representation.setter
    def representation(self, representation: str):
        self.__representation = representation

class BreakdownElementDescription:

    pass
class uma_DescriptorDescription(BreakdownElementDescription):

    def __init__(self, refinedDescription: str):
        self.refinedDescription = refinedDescription
        
    @property
    def refinedDescription(self) -> str:
        return self.__refinedDescription

    @refinedDescription.setter
    def refinedDescription(self, refinedDescription: str):
        self.__refinedDescription = refinedDescription

class uma_ActivityDescription(BreakdownElementDescription):

    def __init__(self, alternatives: str, howToStaff: str, purpose: str):
        self.alternatives = alternatives
        self.howToStaff = howToStaff
        self.purpose = purpose
        
    @property
    def howToStaff(self) -> str:
        return self.__howToStaff

    @howToStaff.setter
    def howToStaff(self, howToStaff: str):
        self.__howToStaff = howToStaff

    @property
    def purpose(self) -> str:
        return self.__purpose

    @purpose.setter
    def purpose(self, purpose: str):
        self.__purpose = purpose

    @property
    def alternatives(self) -> str:
        return self.__alternatives

    @alternatives.setter
    def alternatives(self, alternatives: str):
        self.__alternatives = alternatives

class WorkProduct:

    pass
class uma_Outcome(WorkProduct):

    pass
class uma_Deliverable(WorkProduct):

    def __init__(self, group3: str, deliveredWorkProduct: str):
        self.group3 = group3
        self.deliveredWorkProduct = deliveredWorkProduct
        
    @property
    def group3(self) -> str:
        return self.__group3

    @group3.setter
    def group3(self, group3: str):
        self.__group3 = group3

    @property
    def deliveredWorkProduct(self) -> str:
        return self.__deliveredWorkProduct

    @deliveredWorkProduct.setter
    def deliveredWorkProduct(self, deliveredWorkProduct: str):
        self.__deliveredWorkProduct = deliveredWorkProduct

class uma_Artifact(WorkProduct):

    def __init__(self, group3: str, uma_Artifact: "uma_Artifact" = None, uma_Artifact0: set["uma_Artifact"] = None):
        self.group3 = group3
        self.uma_Artifact = uma_Artifact
        self.uma_Artifact0 = uma_Artifact0 if uma_Artifact0 is not None else set()
        
    @property
    def group3(self) -> str:
        return self.__group3

    @group3.setter
    def group3(self, group3: str):
        self.__group3 = group3

    @property
    def uma_Artifact0(self):
        return self.__uma_Artifact0

    @uma_Artifact0.setter
    def uma_Artifact0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Artifact__uma_Artifact0", None)
        self.__uma_Artifact0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uma_Artifact"):
                    opp_val = getattr(item, "uma_Artifact", None)
                    
                    if opp_val == self:
                        setattr(item, "uma_Artifact", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uma_Artifact"):
                    opp_val = getattr(item, "uma_Artifact", None)
                    
                    setattr(item, "uma_Artifact", self)
                    

    @property
    def uma_Artifact(self):
        return self.__uma_Artifact

    @uma_Artifact.setter
    def uma_Artifact(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Artifact__uma_Artifact", None)
        self.__uma_Artifact = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_Artifact0"):
                opp_val = getattr(old_value, "uma_Artifact0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_Artifact0"):
                opp_val = getattr(value, "uma_Artifact0", None)
                if opp_val is None:
                    setattr(value, "uma_Artifact0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class PackageableElement:

    pass
class uma_MethodElement(PackageableElement):

    def __init__(self, id: str, orderingGuide: str, presentationName: str, group: str, briefDescription: str, suppressed: str, uma_MethodElement: set["uma_Constraint"] = None, uma_MethodElement25: set["uma_MethodElementProperty"] = None):
        self.id = id
        self.orderingGuide = orderingGuide
        self.presentationName = presentationName
        self.group = group
        self.briefDescription = briefDescription
        self.suppressed = suppressed
        self.uma_MethodElement = uma_MethodElement if uma_MethodElement is not None else set()
        self.uma_MethodElement25 = uma_MethodElement25 if uma_MethodElement25 is not None else set()
        
    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def orderingGuide(self) -> str:
        return self.__orderingGuide

    @orderingGuide.setter
    def orderingGuide(self, orderingGuide: str):
        self.__orderingGuide = orderingGuide

    @property
    def suppressed(self) -> str:
        return self.__suppressed

    @suppressed.setter
    def suppressed(self, suppressed: str):
        self.__suppressed = suppressed

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def briefDescription(self) -> str:
        return self.__briefDescription

    @briefDescription.setter
    def briefDescription(self, briefDescription: str):
        self.__briefDescription = briefDescription

    @property
    def presentationName(self) -> str:
        return self.__presentationName

    @presentationName.setter
    def presentationName(self, presentationName: str):
        self.__presentationName = presentationName

    @property
    def uma_MethodElement25(self):
        return self.__uma_MethodElement25

    @uma_MethodElement25.setter
    def uma_MethodElement25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_MethodElement__uma_MethodElement25", None)
        self.__uma_MethodElement25 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uma_MethodElementProperty"):
                    opp_val = getattr(item, "uma_MethodElementProperty", None)
                    
                    if opp_val == self:
                        setattr(item, "uma_MethodElementProperty", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uma_MethodElementProperty"):
                    opp_val = getattr(item, "uma_MethodElementProperty", None)
                    
                    setattr(item, "uma_MethodElementProperty", self)
                    

    @property
    def uma_MethodElement(self):
        return self.__uma_MethodElement

    @uma_MethodElement.setter
    def uma_MethodElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_MethodElement__uma_MethodElement", None)
        self.__uma_MethodElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uma_Constraint"):
                    opp_val = getattr(item, "uma_Constraint", None)
                    
                    if opp_val == self:
                        setattr(item, "uma_Constraint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uma_Constraint"):
                    opp_val = getattr(item, "uma_Constraint", None)
                    
                    setattr(item, "uma_Constraint", self)
                    

class uma_MethodElementProperty(PackageableElement):

    def __init__(self, value: str, uma_MethodElementProperty: "uma_MethodElement" = None):
        self.value = value
        self.uma_MethodElementProperty = uma_MethodElementProperty
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def uma_MethodElementProperty(self):
        return self.__uma_MethodElementProperty

    @uma_MethodElementProperty.setter
    def uma_MethodElementProperty(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_MethodElementProperty__uma_MethodElementProperty", None)
        self.__uma_MethodElementProperty = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_MethodElement25"):
                opp_val = getattr(old_value, "uma_MethodElement25", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_MethodElement25"):
                opp_val = getattr(value, "uma_MethodElement25", None)
                if opp_val is None:
                    setattr(value, "uma_MethodElement25", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class uma_ApplicableMetaClassInfo(PackageableElement):

    def __init__(self, isPrimaryExtension: str):
        self.isPrimaryExtension = isPrimaryExtension
        
    @property
    def isPrimaryExtension(self) -> str:
        return self.__isPrimaryExtension

    @isPrimaryExtension.setter
    def isPrimaryExtension(self, isPrimaryExtension: str):
        self.__isPrimaryExtension = isPrimaryExtension
