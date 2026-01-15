from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class PseudoStateKind(Enum):
    choice = "choice"
    entryPoint = "entryPoint"
    exitPoint = "exitPoint"
    terminate = "terminate"
    initial = "initial"
    join = "join"
    fork = "fork"
    junction = "junction"
class WorkOrderType(Enum):
    finishToStart = "finishToStart"
    finishToFinish = "finishToFinish"
    startToStart = "startToStart"
    startToFinish = "startToFinish"
class VariabilityType(Enum):
    na = "na"
    contributes = "contributes"
    extends = "extends"
    replaces = "replaces"
    localContribution = "localContribution"
    localReplacement = "localReplacement"
    extendsReplaces = "extendsReplaces"


############################################
# Definition of Classes
############################################

class MethodConfiguration:

    pass
class uma_ProcessFamily(MethodConfiguration):

    pass
class ProcessPackage:

    pass
class Process:

    pass
class uma_ProcessPlanningTemplate(Process):

    pass
class uma_CapabilityPattern(Process):

    pass
class uma_DeliveryProcess(Process):

    pass
class ContentCategory:

    pass
class uma_RoleSet(ContentCategory):

    pass
class uma_RoleSetGrouping(ContentCategory):

    pass
class uma_DisciplineGrouping(ContentCategory):

    pass
class uma_Tool(ContentCategory):

    pass
class uma_WorkProductType(ContentCategory):

    pass
class uma_CustomCategory(ContentCategory):

    pass
class uma_Domain(ContentCategory):

    pass
class uma_Discipline(ContentCategory):

    pass
class uma_Region:

    pass
class uma_Transition:

    pass
class uma_Vertex:

    pass
class Vertex:

    pass
class uma_PseudoState(Vertex):

    pass
class uma_State(Vertex):

    pass
class Concept:

    pass
class uma_Whitepaper(Concept):

    pass
class Guidance:

    pass
class uma_Practice(Guidance):

    pass
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

class ProcessDescription:

    pass
class uma_DeliveryProcessDescription(ProcessDescription):

    def __init__(self, scale: str, projectCharacteristics: str, riskLevel: str, estimatingTechnique: str, projectMemberExpertise: str, typeOfContract: str):
        self.scale = scale
        self.projectCharacteristics = projectCharacteristics
        self.riskLevel = riskLevel
        self.estimatingTechnique = estimatingTechnique
        self.projectMemberExpertise = projectMemberExpertise
        self.typeOfContract = typeOfContract
        
    @property
    def riskLevel(self) -> str:
        return self.__riskLevel

    @riskLevel.setter
    def riskLevel(self, riskLevel: str):
        self.__riskLevel = riskLevel

    @property
    def estimatingTechnique(self) -> str:
        return self.__estimatingTechnique

    @estimatingTechnique.setter
    def estimatingTechnique(self, estimatingTechnique: str):
        self.__estimatingTechnique = estimatingTechnique

    @property
    def typeOfContract(self) -> str:
        return self.__typeOfContract

    @typeOfContract.setter
    def typeOfContract(self, typeOfContract: str):
        self.__typeOfContract = typeOfContract

    @property
    def scale(self) -> str:
        return self.__scale

    @scale.setter
    def scale(self, scale: str):
        self.__scale = scale

    @property
    def projectCharacteristics(self) -> str:
        return self.__projectCharacteristics

    @projectCharacteristics.setter
    def projectCharacteristics(self, projectCharacteristics: str):
        self.__projectCharacteristics = projectCharacteristics

    @property
    def projectMemberExpertise(self) -> str:
        return self.__projectMemberExpertise

    @projectMemberExpertise.setter
    def projectMemberExpertise(self, projectMemberExpertise: str):
        self.__projectMemberExpertise = projectMemberExpertise

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

    def __init__(self, purpose: str, alternatives: str, howtoStaff: str):
        self.purpose = purpose
        self.alternatives = alternatives
        self.howtoStaff = howtoStaff
        
    @property
    def alternatives(self) -> str:
        return self.__alternatives

    @alternatives.setter
    def alternatives(self, alternatives: str):
        self.__alternatives = alternatives

    @property
    def howtoStaff(self) -> str:
        return self.__howtoStaff

    @howtoStaff.setter
    def howtoStaff(self, howtoStaff: str):
        self.__howtoStaff = howtoStaff

    @property
    def purpose(self) -> str:
        return self.__purpose

    @purpose.setter
    def purpose(self, purpose: str):
        self.__purpose = purpose

class RoleDescriptor:

    pass
class uma_CompositeRole(RoleDescriptor):

    pass
class Descriptor:

    pass
class uma_WorkProductDescriptor(Descriptor):

    def __init__(self, activityEntryState: str, activityExitState: str, uma_WorkProductDescriptor163: "uma_RoleDescriptor" = None, uma_WorkProductDescriptor: "uma_RoleDescriptor" = None, WorkProductDescriptor174: "uma_WorkProductDescriptor" = None, impactedBy: set["uma_WorkProductDescriptor"] = None, uma_WorkProductDescriptor177: "uma_WorkProductDescriptor" = None, uma_WorkProductDescriptor175: set["uma_WorkProductDescriptor"] = None, uma_WorkProductDescriptor188: "uma_TaskDescriptor" = None, uma_WorkProductDescriptor191: "uma_TaskDescriptor" = None, uma_WorkProductDescriptor194: "uma_TaskDescriptor" = None, uma_WorkProductDescriptor197: "uma_TaskDescriptor" = None, uma_WorkProductDescriptor168: "uma_WorkProduct" = None, WorkProductDescriptor: "uma_WorkProductDescriptor" = None, impacts: set["uma_WorkProductDescriptor"] = None, uma_WorkProductDescriptor300: "uma_ProcessComponentInterface" = None):
        self.activityEntryState = activityEntryState
        self.activityExitState = activityExitState
        self.uma_WorkProductDescriptor163 = uma_WorkProductDescriptor163
        self.uma_WorkProductDescriptor = uma_WorkProductDescriptor
        self.WorkProductDescriptor174 = WorkProductDescriptor174
        self.impactedBy = impactedBy if impactedBy is not None else set()
        self.uma_WorkProductDescriptor177 = uma_WorkProductDescriptor177
        self.uma_WorkProductDescriptor175 = uma_WorkProductDescriptor175 if uma_WorkProductDescriptor175 is not None else set()
        self.uma_WorkProductDescriptor188 = uma_WorkProductDescriptor188
        self.uma_WorkProductDescriptor191 = uma_WorkProductDescriptor191
        self.uma_WorkProductDescriptor194 = uma_WorkProductDescriptor194
        self.uma_WorkProductDescriptor197 = uma_WorkProductDescriptor197
        self.uma_WorkProductDescriptor168 = uma_WorkProductDescriptor168
        self.WorkProductDescriptor = WorkProductDescriptor
        self.impacts = impacts if impacts is not None else set()
        self.uma_WorkProductDescriptor300 = uma_WorkProductDescriptor300
        
    @property
    def activityExitState(self) -> str:
        return self.__activityExitState

    @activityExitState.setter
    def activityExitState(self, activityExitState: str):
        self.__activityExitState = activityExitState

    @property
    def activityEntryState(self) -> str:
        return self.__activityEntryState

    @activityEntryState.setter
    def activityEntryState(self, activityEntryState: str):
        self.__activityEntryState = activityEntryState

    @property
    def uma_WorkProductDescriptor300(self):
        return self.__uma_WorkProductDescriptor300

    @uma_WorkProductDescriptor300.setter
    def uma_WorkProductDescriptor300(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_WorkProductDescriptor__uma_WorkProductDescriptor300", None)
        self.__uma_WorkProductDescriptor300 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_ProcessComponentInterface299"):
                opp_val = getattr(old_value, "uma_ProcessComponentInterface299", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_ProcessComponentInterface299"):
                opp_val = getattr(value, "uma_ProcessComponentInterface299", None)
                if opp_val is None:
                    setattr(value, "uma_ProcessComponentInterface299", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uma_WorkProductDescriptor175(self):
        return self.__uma_WorkProductDescriptor175

    @uma_WorkProductDescriptor175.setter
    def uma_WorkProductDescriptor175(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_WorkProductDescriptor__uma_WorkProductDescriptor175", None)
        self.__uma_WorkProductDescriptor175 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uma_WorkProductDescriptor177"):
                    opp_val = getattr(item, "uma_WorkProductDescriptor177", None)
                    
                    if opp_val == self:
                        setattr(item, "uma_WorkProductDescriptor177", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uma_WorkProductDescriptor177"):
                    opp_val = getattr(item, "uma_WorkProductDescriptor177", None)
                    
                    setattr(item, "uma_WorkProductDescriptor177", self)
                    

    @property
    def WorkProductDescriptor174(self):
        return self.__WorkProductDescriptor174

    @WorkProductDescriptor174.setter
    def WorkProductDescriptor174(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_WorkProductDescriptor__WorkProductDescriptor174", None)
        self.__WorkProductDescriptor174 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "impactedBy"):
                opp_val = getattr(old_value, "impactedBy", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "impactedBy"):
                opp_val = getattr(value, "impactedBy", None)
                if opp_val is None:
                    setattr(value, "impactedBy", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uma_WorkProductDescriptor197(self):
        return self.__uma_WorkProductDescriptor197

    @uma_WorkProductDescriptor197.setter
    def uma_WorkProductDescriptor197(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_WorkProductDescriptor__uma_WorkProductDescriptor197", None)
        self.__uma_WorkProductDescriptor197 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_TaskDescriptor196"):
                opp_val = getattr(old_value, "uma_TaskDescriptor196", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_TaskDescriptor196"):
                opp_val = getattr(value, "uma_TaskDescriptor196", None)
                if opp_val is None:
                    setattr(value, "uma_TaskDescriptor196", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uma_WorkProductDescriptor191(self):
        return self.__uma_WorkProductDescriptor191

    @uma_WorkProductDescriptor191.setter
    def uma_WorkProductDescriptor191(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_WorkProductDescriptor__uma_WorkProductDescriptor191", None)
        self.__uma_WorkProductDescriptor191 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_TaskDescriptor190"):
                opp_val = getattr(old_value, "uma_TaskDescriptor190", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_TaskDescriptor190"):
                opp_val = getattr(value, "uma_TaskDescriptor190", None)
                if opp_val is None:
                    setattr(value, "uma_TaskDescriptor190", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uma_WorkProductDescriptor194(self):
        return self.__uma_WorkProductDescriptor194

    @uma_WorkProductDescriptor194.setter
    def uma_WorkProductDescriptor194(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_WorkProductDescriptor__uma_WorkProductDescriptor194", None)
        self.__uma_WorkProductDescriptor194 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_TaskDescriptor193"):
                opp_val = getattr(old_value, "uma_TaskDescriptor193", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_TaskDescriptor193"):
                opp_val = getattr(value, "uma_TaskDescriptor193", None)
                if opp_val is None:
                    setattr(value, "uma_TaskDescriptor193", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def impactedBy(self):
        return self.__impactedBy

    @impactedBy.setter
    def impactedBy(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_WorkProductDescriptor__impactedBy", None)
        self.__impactedBy = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "WorkProductDescriptor174"):
                    opp_val = getattr(item, "WorkProductDescriptor174", None)
                    
                    if opp_val == self:
                        setattr(item, "WorkProductDescriptor174", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "WorkProductDescriptor174"):
                    opp_val = getattr(item, "WorkProductDescriptor174", None)
                    
                    setattr(item, "WorkProductDescriptor174", self)
                    

    @property
    def uma_WorkProductDescriptor188(self):
        return self.__uma_WorkProductDescriptor188

    @uma_WorkProductDescriptor188.setter
    def uma_WorkProductDescriptor188(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_WorkProductDescriptor__uma_WorkProductDescriptor188", None)
        self.__uma_WorkProductDescriptor188 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_TaskDescriptor187"):
                opp_val = getattr(old_value, "uma_TaskDescriptor187", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_TaskDescriptor187"):
                opp_val = getattr(value, "uma_TaskDescriptor187", None)
                if opp_val is None:
                    setattr(value, "uma_TaskDescriptor187", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def WorkProductDescriptor(self):
        return self.__WorkProductDescriptor

    @WorkProductDescriptor.setter
    def WorkProductDescriptor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_WorkProductDescriptor__WorkProductDescriptor", None)
        self.__WorkProductDescriptor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "impacts"):
                opp_val = getattr(old_value, "impacts", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "impacts"):
                opp_val = getattr(value, "impacts", None)
                if opp_val is None:
                    setattr(value, "impacts", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uma_WorkProductDescriptor168(self):
        return self.__uma_WorkProductDescriptor168

    @uma_WorkProductDescriptor168.setter
    def uma_WorkProductDescriptor168(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_WorkProductDescriptor__uma_WorkProductDescriptor168", None)
        self.__uma_WorkProductDescriptor168 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_WorkProduct169"):
                opp_val = getattr(old_value, "uma_WorkProduct169", None)
                if opp_val == self:
                    setattr(old_value, "uma_WorkProduct169", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_WorkProduct169"):
                opp_val = getattr(value, "uma_WorkProduct169", None)
                setattr(value, "uma_WorkProduct169", self)

    @property
    def uma_WorkProductDescriptor163(self):
        return self.__uma_WorkProductDescriptor163

    @uma_WorkProductDescriptor163.setter
    def uma_WorkProductDescriptor163(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_WorkProductDescriptor__uma_WorkProductDescriptor163", None)
        self.__uma_WorkProductDescriptor163 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_RoleDescriptor162"):
                opp_val = getattr(old_value, "uma_RoleDescriptor162", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_RoleDescriptor162"):
                opp_val = getattr(value, "uma_RoleDescriptor162", None)
                if opp_val is None:
                    setattr(value, "uma_RoleDescriptor162", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "uma_RoleDescriptor160"):
                opp_val = getattr(old_value, "uma_RoleDescriptor160", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_RoleDescriptor160"):
                opp_val = getattr(value, "uma_RoleDescriptor160", None)
                if opp_val is None:
                    setattr(value, "uma_RoleDescriptor160", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def impacts(self):
        return self.__impacts

    @impacts.setter
    def impacts(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_WorkProductDescriptor__impacts", None)
        self.__impacts = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "WorkProductDescriptor"):
                    opp_val = getattr(item, "WorkProductDescriptor", None)
                    
                    if opp_val == self:
                        setattr(item, "WorkProductDescriptor", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "WorkProductDescriptor"):
                    opp_val = getattr(item, "WorkProductDescriptor", None)
                    
                    setattr(item, "WorkProductDescriptor", self)
                    

    @property
    def uma_WorkProductDescriptor177(self):
        return self.__uma_WorkProductDescriptor177

    @uma_WorkProductDescriptor177.setter
    def uma_WorkProductDescriptor177(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_WorkProductDescriptor__uma_WorkProductDescriptor177", None)
        self.__uma_WorkProductDescriptor177 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_WorkProductDescriptor175"):
                opp_val = getattr(old_value, "uma_WorkProductDescriptor175", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_WorkProductDescriptor175"):
                opp_val = getattr(value, "uma_WorkProductDescriptor175", None)
                if opp_val is None:
                    setattr(value, "uma_WorkProductDescriptor175", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class uma_ProcessComponentDescriptor(Descriptor):

    pass
class uma_RoleDescriptor(Descriptor):

    pass
class Activity:

    pass
class uma_Process(Activity):

    pass
class uma_Phase(Activity):

    pass
class uma_Iteration(Activity):

    pass
class WorkBreakdownElement:

    pass
class uma_TaskDescriptor(Descriptor, WorkBreakdownElement):

    pass
class uma_Milestone(WorkBreakdownElement):

    pass
class ProcessElement:

    pass
class uma_PlanningData(ProcessElement):

    def __init__(self, startDate: str, finishDate: str, rank: str, uma_PlanningData: "uma_BreakdownElement" = None):
        self.startDate = startDate
        self.finishDate = finishDate
        self.rank = rank
        self.uma_PlanningData = uma_PlanningData
        
    @property
    def rank(self) -> str:
        return self.__rank

    @rank.setter
    def rank(self, rank: str):
        self.__rank = rank

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
    def uma_PlanningData(self):
        return self.__uma_PlanningData

    @uma_PlanningData.setter
    def uma_PlanningData(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_PlanningData__uma_PlanningData", None)
        self.__uma_PlanningData = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_BreakdownElement148"):
                opp_val = getattr(old_value, "uma_BreakdownElement148", None)
                if opp_val == self:
                    setattr(old_value, "uma_BreakdownElement148", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_BreakdownElement148"):
                opp_val = getattr(value, "uma_BreakdownElement148", None)
                setattr(value, "uma_BreakdownElement148", self)

class uma_WorkOrder(ProcessElement):

    def __init__(self, linkType: str, uma_WorkOrder: "uma_WorkBreakdownElement" = None, uma_WorkOrder165: "uma_WorkBreakdownElement" = None):
        self.linkType = linkType
        self.uma_WorkOrder = uma_WorkOrder
        self.uma_WorkOrder165 = uma_WorkOrder165
        
    @property
    def linkType(self) -> str:
        return self.__linkType

    @linkType.setter
    def linkType(self, linkType: str):
        self.__linkType = linkType

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

    @property
    def uma_WorkOrder165(self):
        return self.__uma_WorkOrder165

    @uma_WorkOrder165.setter
    def uma_WorkOrder165(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_WorkOrder__uma_WorkOrder165", None)
        self.__uma_WorkOrder165 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_WorkBreakdownElement166"):
                opp_val = getattr(old_value, "uma_WorkBreakdownElement166", None)
                if opp_val == self:
                    setattr(old_value, "uma_WorkBreakdownElement166", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_WorkBreakdownElement166"):
                opp_val = getattr(value, "uma_WorkBreakdownElement166", None)
                setattr(value, "uma_WorkBreakdownElement166", self)

class BreakdownElement:

    pass
class uma_ProcessComponentInterface(BreakdownElement):

    pass
class uma_TeamProfile(BreakdownElement):

    pass
class uma_Descriptor(BreakdownElement):

    def __init__(self, isSynchronizedWithSource: str):
        self.isSynchronizedWithSource = isSynchronizedWithSource
        
    @property
    def isSynchronizedWithSource(self) -> str:
        return self.__isSynchronizedWithSource

    @isSynchronizedWithSource.setter
    def isSynchronizedWithSource(self, isSynchronizedWithSource: str):
        self.__isSynchronizedWithSource = isSynchronizedWithSource

class uma_WorkBreakdownElement(BreakdownElement):

    def __init__(self, isRepeatable: str, isOngoing: str, isEventDriven: str, uma_WorkBreakdownElement: set["uma_WorkOrder"] = None, uma_WorkBreakdownElement166: "uma_WorkOrder" = None):
        self.isRepeatable = isRepeatable
        self.isOngoing = isOngoing
        self.isEventDriven = isEventDriven
        self.uma_WorkBreakdownElement = uma_WorkBreakdownElement if uma_WorkBreakdownElement is not None else set()
        self.uma_WorkBreakdownElement166 = uma_WorkBreakdownElement166
        
    @property
    def isRepeatable(self) -> str:
        return self.__isRepeatable

    @isRepeatable.setter
    def isRepeatable(self, isRepeatable: str):
        self.__isRepeatable = isRepeatable

    @property
    def isEventDriven(self) -> str:
        return self.__isEventDriven

    @isEventDriven.setter
    def isEventDriven(self, isEventDriven: str):
        self.__isEventDriven = isEventDriven

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
                    

    @property
    def uma_WorkBreakdownElement166(self):
        return self.__uma_WorkBreakdownElement166

    @uma_WorkBreakdownElement166.setter
    def uma_WorkBreakdownElement166(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_WorkBreakdownElement__uma_WorkBreakdownElement166", None)
        self.__uma_WorkBreakdownElement166 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_WorkOrder165"):
                opp_val = getattr(old_value, "uma_WorkOrder165", None)
                if opp_val == self:
                    setattr(old_value, "uma_WorkOrder165", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_WorkOrder165"):
                opp_val = getattr(value, "uma_WorkOrder165", None)
                setattr(value, "uma_WorkOrder165", self)

class uma_Roadmap(Guidance):

    pass
class uma_BreakdownElement(ProcessElement):

    def __init__(self, hasMultipleOccurrences: str, isOptional: str, prefix: str, isPlanned: str, BreakdownElement: "uma_Activity" = None, uma_BreakdownElement: "uma_BreakdownElement" = None, uma_BreakdownElement142: "uma_BreakdownElement" = None, uma_BreakdownElement146: "uma_BreakdownElement" = None, uma_BreakdownElement144: "uma_BreakdownElement" = None, uma_BreakdownElement148: "uma_PlanningData" = None, breakdownElements: "uma_Activity" = None):
        self.hasMultipleOccurrences = hasMultipleOccurrences
        self.isOptional = isOptional
        self.prefix = prefix
        self.isPlanned = isPlanned
        self.BreakdownElement = BreakdownElement
        self.uma_BreakdownElement = uma_BreakdownElement
        self.uma_BreakdownElement142 = uma_BreakdownElement142
        self.uma_BreakdownElement146 = uma_BreakdownElement146
        self.uma_BreakdownElement144 = uma_BreakdownElement144
        self.uma_BreakdownElement148 = uma_BreakdownElement148
        self.breakdownElements = breakdownElements
        
    @property
    def prefix(self) -> str:
        return self.__prefix

    @prefix.setter
    def prefix(self, prefix: str):
        self.__prefix = prefix

    @property
    def isOptional(self) -> str:
        return self.__isOptional

    @isOptional.setter
    def isOptional(self, isOptional: str):
        self.__isOptional = isOptional

    @property
    def hasMultipleOccurrences(self) -> str:
        return self.__hasMultipleOccurrences

    @hasMultipleOccurrences.setter
    def hasMultipleOccurrences(self, hasMultipleOccurrences: str):
        self.__hasMultipleOccurrences = hasMultipleOccurrences

    @property
    def isPlanned(self) -> str:
        return self.__isPlanned

    @isPlanned.setter
    def isPlanned(self, isPlanned: str):
        self.__isPlanned = isPlanned

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
            if hasattr(old_value, "uma_BreakdownElement142"):
                opp_val = getattr(old_value, "uma_BreakdownElement142", None)
                if opp_val == self:
                    setattr(old_value, "uma_BreakdownElement142", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_BreakdownElement142"):
                opp_val = getattr(value, "uma_BreakdownElement142", None)
                setattr(value, "uma_BreakdownElement142", self)

    @property
    def uma_BreakdownElement148(self):
        return self.__uma_BreakdownElement148

    @uma_BreakdownElement148.setter
    def uma_BreakdownElement148(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_BreakdownElement__uma_BreakdownElement148", None)
        self.__uma_BreakdownElement148 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_PlanningData"):
                opp_val = getattr(old_value, "uma_PlanningData", None)
                if opp_val == self:
                    setattr(old_value, "uma_PlanningData", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_PlanningData"):
                opp_val = getattr(value, "uma_PlanningData", None)
                setattr(value, "uma_PlanningData", self)

    @property
    def breakdownElements(self):
        return self.__breakdownElements

    @breakdownElements.setter
    def breakdownElements(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_BreakdownElement__breakdownElements", None)
        self.__breakdownElements = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Activity"):
                opp_val = getattr(old_value, "Activity", None)
                if opp_val == self:
                    setattr(old_value, "Activity", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Activity"):
                opp_val = getattr(value, "Activity", None)
                setattr(value, "Activity", self)

    @property
    def uma_BreakdownElement142(self):
        return self.__uma_BreakdownElement142

    @uma_BreakdownElement142.setter
    def uma_BreakdownElement142(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_BreakdownElement__uma_BreakdownElement142", None)
        self.__uma_BreakdownElement142 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_BreakdownElement"):
                opp_val = getattr(old_value, "uma_BreakdownElement", None)
                if opp_val == self:
                    setattr(old_value, "uma_BreakdownElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_BreakdownElement"):
                opp_val = getattr(value, "uma_BreakdownElement", None)
                setattr(value, "uma_BreakdownElement", self)

    @property
    def BreakdownElement(self):
        return self.__BreakdownElement

    @BreakdownElement.setter
    def BreakdownElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_BreakdownElement__BreakdownElement", None)
        self.__BreakdownElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "superActivities"):
                opp_val = getattr(old_value, "superActivities", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "superActivities"):
                opp_val = getattr(value, "superActivities", None)
                if opp_val is None:
                    setattr(value, "superActivities", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uma_BreakdownElement144(self):
        return self.__uma_BreakdownElement144

    @uma_BreakdownElement144.setter
    def uma_BreakdownElement144(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_BreakdownElement__uma_BreakdownElement144", None)
        self.__uma_BreakdownElement144 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_BreakdownElement146"):
                opp_val = getattr(old_value, "uma_BreakdownElement146", None)
                if opp_val == self:
                    setattr(old_value, "uma_BreakdownElement146", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_BreakdownElement146"):
                opp_val = getattr(value, "uma_BreakdownElement146", None)
                setattr(value, "uma_BreakdownElement146", self)

    @property
    def uma_BreakdownElement146(self):
        return self.__uma_BreakdownElement146

    @uma_BreakdownElement146.setter
    def uma_BreakdownElement146(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_BreakdownElement__uma_BreakdownElement146", None)
        self.__uma_BreakdownElement146 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_BreakdownElement144"):
                opp_val = getattr(old_value, "uma_BreakdownElement144", None)
                if opp_val == self:
                    setattr(old_value, "uma_BreakdownElement144", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_BreakdownElement144"):
                opp_val = getattr(value, "uma_BreakdownElement144", None)
                setattr(value, "uma_BreakdownElement144", self)

class GraphicPrimitive:

    pass
class uma_Ellipse(GraphicPrimitive):

    def __init__(self, radiusX: str, radiusY: str, rotation: str, startAngle: str, endAngle: str, uma_Ellipse: "uma_Point" = None):
        self.radiusX = radiusX
        self.radiusY = radiusY
        self.rotation = rotation
        self.startAngle = startAngle
        self.endAngle = endAngle
        self.uma_Ellipse = uma_Ellipse
        
    @property
    def startAngle(self) -> str:
        return self.__startAngle

    @startAngle.setter
    def startAngle(self, startAngle: str):
        self.__startAngle = startAngle

    @property
    def endAngle(self) -> str:
        return self.__endAngle

    @endAngle.setter
    def endAngle(self, endAngle: str):
        self.__endAngle = endAngle

    @property
    def radiusX(self) -> str:
        return self.__radiusX

    @radiusX.setter
    def radiusX(self, radiusX: str):
        self.__radiusX = radiusX

    @property
    def radiusY(self) -> str:
        return self.__radiusY

    @radiusY.setter
    def radiusY(self, radiusY: str):
        self.__radiusY = radiusY

    @property
    def rotation(self) -> str:
        return self.__rotation

    @rotation.setter
    def rotation(self, rotation: str):
        self.__rotation = rotation

    @property
    def uma_Ellipse(self):
        return self.__uma_Ellipse

    @uma_Ellipse.setter
    def uma_Ellipse(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Ellipse__uma_Ellipse", None)
        self.__uma_Ellipse = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_Point120"):
                opp_val = getattr(old_value, "uma_Point120", None)
                if opp_val == self:
                    setattr(old_value, "uma_Point120", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_Point120"):
                opp_val = getattr(value, "uma_Point120", None)
                setattr(value, "uma_Point120", self)

class uma_Polyline(GraphicPrimitive):

    def __init__(self, closed: str, uma_Polyline: set["uma_Point"] = None):
        self.closed = closed
        self.uma_Polyline = uma_Polyline if uma_Polyline is not None else set()
        
    @property
    def closed(self) -> str:
        return self.__closed

    @closed.setter
    def closed(self, closed: str):
        self.__closed = closed

    @property
    def uma_Polyline(self):
        return self.__uma_Polyline

    @uma_Polyline.setter
    def uma_Polyline(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Polyline__uma_Polyline", None)
        self.__uma_Polyline = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uma_Point118"):
                    opp_val = getattr(item, "uma_Point118", None)
                    
                    if opp_val == self:
                        setattr(item, "uma_Point118", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uma_Point118"):
                    opp_val = getattr(item, "uma_Point118", None)
                    
                    setattr(item, "uma_Point118", self)
                    

class LeafElement:

    pass
class uma_Image(LeafElement):

    def __init__(self, uri: str, mimeType: str):
        self.uri = uri
        self.mimeType = mimeType
        
    @property
    def mimeType(self) -> str:
        return self.__mimeType

    @mimeType.setter
    def mimeType(self, mimeType: str):
        self.__mimeType = mimeType

    @property
    def uri(self) -> str:
        return self.__uri

    @uri.setter
    def uri(self, uri: str):
        self.__uri = uri

class uma_GraphicPrimitive(LeafElement):

    pass
class uma_TextElement(LeafElement):

    def __init__(self, text: str):
        self.text = text
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

class SemanticModelBridge:

    pass
class uma_UMASemanticModelBridge(SemanticModelBridge):

    pass
class uma_CoreSemanticModelBridge(SemanticModelBridge):

    pass
class uma_SimpleSemanticModelElement(SemanticModelBridge):

    def __init__(self, typeInfo: str):
        self.typeInfo = typeInfo
        
    @property
    def typeInfo(self) -> str:
        return self.__typeInfo

    @typeInfo.setter
    def typeInfo(self, typeInfo: str):
        self.__typeInfo = typeInfo

class GraphElement:

    pass
class uma_GraphNode(GraphElement):

    pass
class GraphNode:

    pass
class uma_Diagram(GraphNode):

    def __init__(self, zoom: str, Diagram99: "uma_SemanticModelBridge" = None, uma_Diagram: "uma_Point" = None, Diagram: "uma_DiagramLink" = None, diagram111: "uma_SemanticModelBridge" = None, diagram: set["uma_DiagramLink"] = None, uma_Diagram294: "uma_ProcessPackage" = None):
        self.zoom = zoom
        self.Diagram99 = Diagram99
        self.uma_Diagram = uma_Diagram
        self.Diagram = Diagram
        self.diagram111 = diagram111
        self.diagram = diagram if diagram is not None else set()
        self.uma_Diagram294 = uma_Diagram294
        
    @property
    def zoom(self) -> str:
        return self.__zoom

    @zoom.setter
    def zoom(self, zoom: str):
        self.__zoom = zoom

    @property
    def uma_Diagram294(self):
        return self.__uma_Diagram294

    @uma_Diagram294.setter
    def uma_Diagram294(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Diagram__uma_Diagram294", None)
        self.__uma_Diagram294 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_ProcessPackage293"):
                opp_val = getattr(old_value, "uma_ProcessPackage293", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_ProcessPackage293"):
                opp_val = getattr(value, "uma_ProcessPackage293", None)
                if opp_val is None:
                    setattr(value, "uma_ProcessPackage293", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Diagram99(self):
        return self.__Diagram99

    @Diagram99.setter
    def Diagram99(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Diagram__Diagram99", None)
        self.__Diagram99 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "namespace"):
                opp_val = getattr(old_value, "namespace", None)
                if opp_val == self:
                    setattr(old_value, "namespace", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "namespace"):
                opp_val = getattr(value, "namespace", None)
                setattr(value, "namespace", self)

    @property
    def uma_Diagram(self):
        return self.__uma_Diagram

    @uma_Diagram.setter
    def uma_Diagram(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Diagram__uma_Diagram", None)
        self.__uma_Diagram = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_Point107"):
                opp_val = getattr(old_value, "uma_Point107", None)
                if opp_val == self:
                    setattr(old_value, "uma_Point107", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_Point107"):
                opp_val = getattr(value, "uma_Point107", None)
                setattr(value, "uma_Point107", self)

    @property
    def diagram(self):
        return self.__diagram

    @diagram.setter
    def diagram(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Diagram__diagram", None)
        self.__diagram = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DiagramLink109"):
                    opp_val = getattr(item, "DiagramLink109", None)
                    
                    if opp_val == self:
                        setattr(item, "DiagramLink109", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DiagramLink109"):
                    opp_val = getattr(item, "DiagramLink109", None)
                    
                    setattr(item, "DiagramLink109", self)
                    

    @property
    def diagram111(self):
        return self.__diagram111

    @diagram111.setter
    def diagram111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Diagram__diagram111", None)
        self.__diagram111 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SemanticModelBridge112"):
                opp_val = getattr(old_value, "SemanticModelBridge112", None)
                if opp_val == self:
                    setattr(old_value, "SemanticModelBridge112", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SemanticModelBridge112"):
                opp_val = getattr(value, "SemanticModelBridge112", None)
                setattr(value, "SemanticModelBridge112", self)

    @property
    def Diagram(self):
        return self.__Diagram

    @Diagram.setter
    def Diagram(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Diagram__Diagram", None)
        self.__Diagram = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diagramLink"):
                opp_val = getattr(old_value, "diagramLink", None)
                if opp_val == self:
                    setattr(old_value, "diagramLink", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagramLink"):
                opp_val = getattr(value, "diagramLink", None)
                setattr(value, "diagramLink", self)

class uma_Dimension:

    def __init__(self, width: str, height: str, uma_Dimension: "uma_GraphNode" = None):
        self.width = width
        self.height = height
        self.uma_Dimension = uma_Dimension
        
    @property
    def width(self) -> str:
        return self.__width

    @width.setter
    def width(self, width: str):
        self.__width = width

    @property
    def height(self) -> str:
        return self.__height

    @height.setter
    def height(self, height: str):
        self.__height = height

    @property
    def uma_Dimension(self):
        return self.__uma_Dimension

    @uma_Dimension.setter
    def uma_Dimension(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Dimension__uma_Dimension", None)
        self.__uma_Dimension = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_GraphNode"):
                opp_val = getattr(old_value, "uma_GraphNode", None)
                if opp_val == self:
                    setattr(old_value, "uma_GraphNode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_GraphNode"):
                opp_val = getattr(value, "uma_GraphNode", None)
                setattr(value, "uma_GraphNode", self)

class uma_Point:

    def __init__(self, y: str, x: str, uma_Point: "uma_GraphElement" = None, uma_Point89: "uma_DiagramLink" = None, uma_Point105: "uma_GraphEdge" = None, uma_Point107: "uma_Diagram" = None, uma_Point118: "uma_Polyline" = None, uma_Point120: "uma_Ellipse" = None):
        self.y = y
        self.x = x
        self.uma_Point = uma_Point
        self.uma_Point89 = uma_Point89
        self.uma_Point105 = uma_Point105
        self.uma_Point107 = uma_Point107
        self.uma_Point118 = uma_Point118
        self.uma_Point120 = uma_Point120
        
    @property
    def y(self) -> str:
        return self.__y

    @y.setter
    def y(self, y: str):
        self.__y = y

    @property
    def x(self) -> str:
        return self.__x

    @x.setter
    def x(self, x: str):
        self.__x = x

    @property
    def uma_Point89(self):
        return self.__uma_Point89

    @uma_Point89.setter
    def uma_Point89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Point__uma_Point89", None)
        self.__uma_Point89 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_DiagramLink"):
                opp_val = getattr(old_value, "uma_DiagramLink", None)
                if opp_val == self:
                    setattr(old_value, "uma_DiagramLink", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_DiagramLink"):
                opp_val = getattr(value, "uma_DiagramLink", None)
                setattr(value, "uma_DiagramLink", self)

    @property
    def uma_Point120(self):
        return self.__uma_Point120

    @uma_Point120.setter
    def uma_Point120(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Point__uma_Point120", None)
        self.__uma_Point120 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_Ellipse"):
                opp_val = getattr(old_value, "uma_Ellipse", None)
                if opp_val == self:
                    setattr(old_value, "uma_Ellipse", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_Ellipse"):
                opp_val = getattr(value, "uma_Ellipse", None)
                setattr(value, "uma_Ellipse", self)

    @property
    def uma_Point105(self):
        return self.__uma_Point105

    @uma_Point105.setter
    def uma_Point105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Point__uma_Point105", None)
        self.__uma_Point105 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_GraphEdge"):
                opp_val = getattr(old_value, "uma_GraphEdge", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_GraphEdge"):
                opp_val = getattr(value, "uma_GraphEdge", None)
                if opp_val is None:
                    setattr(value, "uma_GraphEdge", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uma_Point(self):
        return self.__uma_Point

    @uma_Point.setter
    def uma_Point(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Point__uma_Point", None)
        self.__uma_Point = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_GraphElement"):
                opp_val = getattr(old_value, "uma_GraphElement", None)
                if opp_val == self:
                    setattr(old_value, "uma_GraphElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_GraphElement"):
                opp_val = getattr(value, "uma_GraphElement", None)
                setattr(value, "uma_GraphElement", self)

    @property
    def uma_Point118(self):
        return self.__uma_Point118

    @uma_Point118.setter
    def uma_Point118(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Point__uma_Point118", None)
        self.__uma_Point118 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_Polyline"):
                opp_val = getattr(old_value, "uma_Polyline", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_Polyline"):
                opp_val = getattr(value, "uma_Polyline", None)
                if opp_val is None:
                    setattr(value, "uma_Polyline", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uma_Point107(self):
        return self.__uma_Point107

    @uma_Point107.setter
    def uma_Point107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Point__uma_Point107", None)
        self.__uma_Point107 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_Diagram"):
                opp_val = getattr(old_value, "uma_Diagram", None)
                if opp_val == self:
                    setattr(old_value, "uma_Diagram", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_Diagram"):
                opp_val = getattr(value, "uma_Diagram", None)
                setattr(value, "uma_Diagram", self)

class uma_GraphEdge(GraphElement):

    pass
class uma_GraphConnector(GraphElement):

    pass
class DiagramElement:

    pass
class uma_Property(DiagramElement):

    def __init__(self, key: str, value: str, uma_Property: "uma_DiagramElement" = None):
        self.key = key
        self.value = value
        self.uma_Property = uma_Property
        
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
    def uma_Property(self):
        return self.__uma_Property

    @uma_Property.setter
    def uma_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Property__uma_Property", None)
        self.__uma_Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_DiagramElement"):
                opp_val = getattr(old_value, "uma_DiagramElement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_DiagramElement"):
                opp_val = getattr(value, "uma_DiagramElement", None)
                if opp_val is None:
                    setattr(value, "uma_DiagramElement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class uma_LeafElement(DiagramElement):

    pass
class uma_SemanticModelBridge(DiagramElement):

    def __init__(self, presentation: str, SemanticModelBridge: "uma_GraphElement" = None, semanticModel: "uma_GraphElement" = None, namespace: "uma_Diagram" = None, SemanticModelBridge112: "uma_Diagram" = None):
        self.presentation = presentation
        self.SemanticModelBridge = SemanticModelBridge
        self.semanticModel = semanticModel
        self.namespace = namespace
        self.SemanticModelBridge112 = SemanticModelBridge112
        
    @property
    def presentation(self) -> str:
        return self.__presentation

    @presentation.setter
    def presentation(self, presentation: str):
        self.__presentation = presentation

    @property
    def SemanticModelBridge(self):
        return self.__SemanticModelBridge

    @SemanticModelBridge.setter
    def SemanticModelBridge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_SemanticModelBridge__SemanticModelBridge", None)
        self.__SemanticModelBridge = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphElement84"):
                opp_val = getattr(old_value, "graphElement84", None)
                if opp_val == self:
                    setattr(old_value, "graphElement84", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphElement84"):
                opp_val = getattr(value, "graphElement84", None)
                setattr(value, "graphElement84", self)

    @property
    def semanticModel(self):
        return self.__semanticModel

    @semanticModel.setter
    def semanticModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_SemanticModelBridge__semanticModel", None)
        self.__semanticModel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GraphElement97"):
                opp_val = getattr(old_value, "GraphElement97", None)
                if opp_val == self:
                    setattr(old_value, "GraphElement97", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GraphElement97"):
                opp_val = getattr(value, "GraphElement97", None)
                setattr(value, "GraphElement97", self)

    @property
    def SemanticModelBridge112(self):
        return self.__SemanticModelBridge112

    @SemanticModelBridge112.setter
    def SemanticModelBridge112(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_SemanticModelBridge__SemanticModelBridge112", None)
        self.__SemanticModelBridge112 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diagram111"):
                opp_val = getattr(old_value, "diagram111", None)
                if opp_val == self:
                    setattr(old_value, "diagram111", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagram111"):
                opp_val = getattr(value, "diagram111", None)
                setattr(value, "diagram111", self)

    @property
    def namespace(self):
        return self.__namespace

    @namespace.setter
    def namespace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_SemanticModelBridge__namespace", None)
        self.__namespace = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Diagram99"):
                opp_val = getattr(old_value, "Diagram99", None)
                if opp_val == self:
                    setattr(old_value, "Diagram99", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Diagram99"):
                opp_val = getattr(value, "Diagram99", None)
                setattr(value, "Diagram99", self)

class uma_Reference(DiagramElement):

    def __init__(self, isIndividualRepresentation: str, Reference: "uma_DiagramElement" = None, reference: "uma_DiagramElement" = None):
        self.isIndividualRepresentation = isIndividualRepresentation
        self.Reference = Reference
        self.reference = reference
        
    @property
    def isIndividualRepresentation(self) -> str:
        return self.__isIndividualRepresentation

    @isIndividualRepresentation.setter
    def isIndividualRepresentation(self, isIndividualRepresentation: str):
        self.__isIndividualRepresentation = isIndividualRepresentation

    @property
    def reference(self):
        return self.__reference

    @reference.setter
    def reference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Reference__reference", None)
        self.__reference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DiagramElement101"):
                opp_val = getattr(old_value, "DiagramElement101", None)
                if opp_val == self:
                    setattr(old_value, "DiagramElement101", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DiagramElement101"):
                opp_val = getattr(value, "DiagramElement101", None)
                setattr(value, "DiagramElement101", self)

    @property
    def Reference(self):
        return self.__Reference

    @Reference.setter
    def Reference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Reference__Reference", None)
        self.__Reference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "referenced"):
                opp_val = getattr(old_value, "referenced", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "referenced"):
                opp_val = getattr(value, "referenced", None)
                if opp_val is None:
                    setattr(value, "referenced", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class uma_DiagramLink(DiagramElement):

    def __init__(self, zoom: str, DiagramLink: "uma_GraphElement" = None, uma_DiagramLink: "uma_Point" = None, link: "uma_GraphElement" = None, diagramLink: "uma_Diagram" = None, DiagramLink109: "uma_Diagram" = None):
        self.zoom = zoom
        self.DiagramLink = DiagramLink
        self.uma_DiagramLink = uma_DiagramLink
        self.link = link
        self.diagramLink = diagramLink
        self.DiagramLink109 = DiagramLink109
        
    @property
    def zoom(self) -> str:
        return self.__zoom

    @zoom.setter
    def zoom(self, zoom: str):
        self.__zoom = zoom

    @property
    def link(self):
        return self.__link

    @link.setter
    def link(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_DiagramLink__link", None)
        self.__link = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GraphElement91"):
                opp_val = getattr(old_value, "GraphElement91", None)
                if opp_val == self:
                    setattr(old_value, "GraphElement91", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GraphElement91"):
                opp_val = getattr(value, "GraphElement91", None)
                setattr(value, "GraphElement91", self)

    @property
    def uma_DiagramLink(self):
        return self.__uma_DiagramLink

    @uma_DiagramLink.setter
    def uma_DiagramLink(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_DiagramLink__uma_DiagramLink", None)
        self.__uma_DiagramLink = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_Point89"):
                opp_val = getattr(old_value, "uma_Point89", None)
                if opp_val == self:
                    setattr(old_value, "uma_Point89", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_Point89"):
                opp_val = getattr(value, "uma_Point89", None)
                setattr(value, "uma_Point89", self)

    @property
    def DiagramLink(self):
        return self.__DiagramLink

    @DiagramLink.setter
    def DiagramLink(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_DiagramLink__DiagramLink", None)
        self.__DiagramLink = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphElement"):
                opp_val = getattr(old_value, "graphElement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphElement"):
                opp_val = getattr(value, "graphElement", None)
                if opp_val is None:
                    setattr(value, "graphElement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def diagramLink(self):
        return self.__diagramLink

    @diagramLink.setter
    def diagramLink(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_DiagramLink__diagramLink", None)
        self.__diagramLink = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Diagram"):
                opp_val = getattr(old_value, "Diagram", None)
                if opp_val == self:
                    setattr(old_value, "Diagram", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Diagram"):
                opp_val = getattr(value, "Diagram", None)
                setattr(value, "Diagram", self)

    @property
    def DiagramLink109(self):
        return self.__DiagramLink109

    @DiagramLink109.setter
    def DiagramLink109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_DiagramLink__DiagramLink109", None)
        self.__DiagramLink109 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diagram"):
                opp_val = getattr(old_value, "diagram", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagram"):
                opp_val = getattr(value, "diagram", None)
                if opp_val is None:
                    setattr(value, "diagram", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class uma_GraphElement(DiagramElement):

    pass
class WorkProductDescription:

    pass
class uma_ArtifactDescription(WorkProductDescription):

    def __init__(self, notation: str, briefOutline: str, representationOptions: str, representation: str):
        self.notation = notation
        self.briefOutline = briefOutline
        self.representationOptions = representationOptions
        self.representation = representation
        
    @property
    def representationOptions(self) -> str:
        return self.__representationOptions

    @representationOptions.setter
    def representationOptions(self, representationOptions: str):
        self.__representationOptions = representationOptions

    @property
    def representation(self) -> str:
        return self.__representation

    @representation.setter
    def representation(self, representation: str):
        self.__representation = representation

    @property
    def notation(self) -> str:
        return self.__notation

    @notation.setter
    def notation(self, notation: str):
        self.__notation = notation

    @property
    def briefOutline(self) -> str:
        return self.__briefOutline

    @briefOutline.setter
    def briefOutline(self, briefOutline: str):
        self.__briefOutline = briefOutline

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

class ContentDescription:

    pass
class uma_RoleDescription(ContentDescription):

    def __init__(self, skills: str, assignmentApproaches: str, synonyms: str):
        self.skills = skills
        self.assignmentApproaches = assignmentApproaches
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

class uma_PracticeDescription(ContentDescription):

    def __init__(self, additionalInfo: str, problem: str, background: str, goals: str, application: str, levelsOfAdoption: str):
        self.additionalInfo = additionalInfo
        self.problem = problem
        self.background = background
        self.goals = goals
        self.application = application
        self.levelsOfAdoption = levelsOfAdoption
        
    @property
    def application(self) -> str:
        return self.__application

    @application.setter
    def application(self, application: str):
        self.__application = application

    @property
    def background(self) -> str:
        return self.__background

    @background.setter
    def background(self, background: str):
        self.__background = background

    @property
    def goals(self) -> str:
        return self.__goals

    @goals.setter
    def goals(self, goals: str):
        self.__goals = goals

    @property
    def problem(self) -> str:
        return self.__problem

    @problem.setter
    def problem(self, problem: str):
        self.__problem = problem

    @property
    def levelsOfAdoption(self) -> str:
        return self.__levelsOfAdoption

    @levelsOfAdoption.setter
    def levelsOfAdoption(self, levelsOfAdoption: str):
        self.__levelsOfAdoption = levelsOfAdoption

    @property
    def additionalInfo(self) -> str:
        return self.__additionalInfo

    @additionalInfo.setter
    def additionalInfo(self, additionalInfo: str):
        self.__additionalInfo = additionalInfo

class uma_GuidanceDescription(ContentDescription):

    def __init__(self, attachments: str):
        self.attachments = attachments
        
    @property
    def attachments(self) -> str:
        return self.__attachments

    @attachments.setter
    def attachments(self, attachments: str):
        self.__attachments = attachments

class uma_BreakdownElementDescription(ContentDescription):

    def __init__(self, usageGuidance: str):
        self.usageGuidance = usageGuidance
        
    @property
    def usageGuidance(self) -> str:
        return self.__usageGuidance

    @usageGuidance.setter
    def usageGuidance(self, usageGuidance: str):
        self.__usageGuidance = usageGuidance

class uma_TaskDescription(ContentDescription):

    def __init__(self, purpose: str, alternatives: str):
        self.purpose = purpose
        self.alternatives = alternatives
        
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

class uma_WorkProductDescription(ContentDescription):

    def __init__(self, purpose: str, impactOfNotHaving: str, reasonsForNotNeeding: str):
        self.purpose = purpose
        self.impactOfNotHaving = impactOfNotHaving
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

class Section:

    pass
class MethodPackage:

    pass
class uma_ProcessPackage(MethodPackage):

    pass
class uma_ContentPackage(MethodPackage):

    pass
class Package:

    pass
class WorkProduct:

    pass
class uma_Deliverable(WorkProduct):

    pass
class uma_Outcome(WorkProduct):

    pass
class uma_Artifact(WorkProduct):

    pass
class uma_ToolMentor(Guidance):

    pass
class uma_Template(Guidance):

    pass
class uma_Report(Guidance):

    pass
class WorkDefinition:

    pass
class uma_StateMachine(WorkDefinition):

    pass
class uma_Step(WorkDefinition, Section):

    pass
class uma_EstimationConsiderations(Guidance):

    pass
class MethodUnit:

    pass
class uma_MethodPlugin(MethodUnit, Package):

    def __init__(self, userChangeable: str, uma_MethodPlugin: set["uma_MethodPackage"] = None, uma_MethodPlugin314: "uma_MethodConfiguration" = None, uma_MethodPlugin307: "uma_MethodPlugin" = None, uma_MethodPlugin305: set["uma_MethodPlugin"] = None, uma_MethodPlugin336: "uma_MethodLibrary" = None):
        self.userChangeable = userChangeable
        self.uma_MethodPlugin = uma_MethodPlugin if uma_MethodPlugin is not None else set()
        self.uma_MethodPlugin314 = uma_MethodPlugin314
        self.uma_MethodPlugin307 = uma_MethodPlugin307
        self.uma_MethodPlugin305 = uma_MethodPlugin305 if uma_MethodPlugin305 is not None else set()
        self.uma_MethodPlugin336 = uma_MethodPlugin336
        
    @property
    def userChangeable(self) -> str:
        return self.__userChangeable

    @userChangeable.setter
    def userChangeable(self, userChangeable: str):
        self.__userChangeable = userChangeable

    @property
    def uma_MethodPlugin336(self):
        return self.__uma_MethodPlugin336

    @uma_MethodPlugin336.setter
    def uma_MethodPlugin336(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_MethodPlugin__uma_MethodPlugin336", None)
        self.__uma_MethodPlugin336 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_MethodLibrary"):
                opp_val = getattr(old_value, "uma_MethodLibrary", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_MethodLibrary"):
                opp_val = getattr(value, "uma_MethodLibrary", None)
                if opp_val is None:
                    setattr(value, "uma_MethodLibrary", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uma_MethodPlugin(self):
        return self.__uma_MethodPlugin

    @uma_MethodPlugin.setter
    def uma_MethodPlugin(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_MethodPlugin__uma_MethodPlugin", None)
        self.__uma_MethodPlugin = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uma_MethodPackage304"):
                    opp_val = getattr(item, "uma_MethodPackage304", None)
                    
                    if opp_val == self:
                        setattr(item, "uma_MethodPackage304", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uma_MethodPackage304"):
                    opp_val = getattr(item, "uma_MethodPackage304", None)
                    
                    setattr(item, "uma_MethodPackage304", self)
                    

    @property
    def uma_MethodPlugin305(self):
        return self.__uma_MethodPlugin305

    @uma_MethodPlugin305.setter
    def uma_MethodPlugin305(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_MethodPlugin__uma_MethodPlugin305", None)
        self.__uma_MethodPlugin305 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uma_MethodPlugin307"):
                    opp_val = getattr(item, "uma_MethodPlugin307", None)
                    
                    if opp_val == self:
                        setattr(item, "uma_MethodPlugin307", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uma_MethodPlugin307"):
                    opp_val = getattr(item, "uma_MethodPlugin307", None)
                    
                    setattr(item, "uma_MethodPlugin307", self)
                    

    @property
    def uma_MethodPlugin314(self):
        return self.__uma_MethodPlugin314

    @uma_MethodPlugin314.setter
    def uma_MethodPlugin314(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_MethodPlugin__uma_MethodPlugin314", None)
        self.__uma_MethodPlugin314 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_MethodConfiguration313"):
                opp_val = getattr(old_value, "uma_MethodConfiguration313", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_MethodConfiguration313"):
                opp_val = getattr(value, "uma_MethodConfiguration313", None)
                if opp_val is None:
                    setattr(value, "uma_MethodConfiguration313", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uma_MethodPlugin307(self):
        return self.__uma_MethodPlugin307

    @uma_MethodPlugin307.setter
    def uma_MethodPlugin307(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_MethodPlugin__uma_MethodPlugin307", None)
        self.__uma_MethodPlugin307 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_MethodPlugin305"):
                opp_val = getattr(old_value, "uma_MethodPlugin305", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_MethodPlugin305"):
                opp_val = getattr(value, "uma_MethodPlugin305", None)
                if opp_val is None:
                    setattr(value, "uma_MethodPlugin305", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class uma_ProcessComponent(ProcessPackage, MethodUnit):

    pass
class uma_MethodConfiguration(MethodUnit):

    pass
class uma_MethodLibrary(MethodUnit, Package):

    pass
class uma_ContentDescription(MethodUnit):

    def __init__(self, mainDescription: str, externalId: str, keyConsiderations: str, uma_ContentDescription18: set["uma_Section"] = None, uma_ContentDescription: "uma_DescribableElement" = None):
        self.mainDescription = mainDescription
        self.externalId = externalId
        self.keyConsiderations = keyConsiderations
        self.uma_ContentDescription18 = uma_ContentDescription18 if uma_ContentDescription18 is not None else set()
        self.uma_ContentDescription = uma_ContentDescription
        
    @property
    def externalId(self) -> str:
        return self.__externalId

    @externalId.setter
    def externalId(self, externalId: str):
        self.__externalId = externalId

    @property
    def keyConsiderations(self) -> str:
        return self.__keyConsiderations

    @keyConsiderations.setter
    def keyConsiderations(self, keyConsiderations: str):
        self.__keyConsiderations = keyConsiderations

    @property
    def mainDescription(self) -> str:
        return self.__mainDescription

    @mainDescription.setter
    def mainDescription(self, mainDescription: str):
        self.__mainDescription = mainDescription

    @property
    def uma_ContentDescription18(self):
        return self.__uma_ContentDescription18

    @uma_ContentDescription18.setter
    def uma_ContentDescription18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_ContentDescription__uma_ContentDescription18", None)
        self.__uma_ContentDescription18 = value if value is not None else set()
        
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
    def uma_ContentDescription(self):
        return self.__uma_ContentDescription

    @uma_ContentDescription.setter
    def uma_ContentDescription(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_ContentDescription__uma_ContentDescription", None)
        self.__uma_ContentDescription = value
        
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
class uma_WorkProduct(ContentElement):

    pass
class uma_ContentCategory(ContentElement):

    pass
class uma_Guidance(ContentElement):

    pass
class uma_Task(ContentElement, WorkDefinition):

    pass
class uma_Role(ContentElement):

    pass
class MethodElement:

    pass
class uma_MethodUnit(MethodElement):

    def __init__(self, authors: str, changeDate: str, changeDescription: str, version: str, uma_MethodUnit: "uma_SupportingMaterial" = None):
        self.authors = authors
        self.changeDate = changeDate
        self.changeDescription = changeDescription
        self.version = version
        self.uma_MethodUnit = uma_MethodUnit
        
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
    def authors(self) -> str:
        return self.__authors

    @authors.setter
    def authors(self, authors: str):
        self.__authors = authors

    @property
    def changeDescription(self) -> str:
        return self.__changeDescription

    @changeDescription.setter
    def changeDescription(self, changeDescription: str):
        self.__changeDescription = changeDescription

    @property
    def uma_MethodUnit(self):
        return self.__uma_MethodUnit

    @uma_MethodUnit.setter
    def uma_MethodUnit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_MethodUnit__uma_MethodUnit", None)
        self.__uma_MethodUnit = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_SupportingMaterial311"):
                opp_val = getattr(old_value, "uma_SupportingMaterial311", None)
                if opp_val == self:
                    setattr(old_value, "uma_SupportingMaterial311", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_SupportingMaterial311"):
                opp_val = getattr(value, "uma_SupportingMaterial311", None)
                setattr(value, "uma_SupportingMaterial311", self)

class uma_VariabilityElement(MethodElement):

    def __init__(self, variabilityType: str, uma_VariabilityElement: "uma_VariabilityElement" = None, uma_VariabilityElement308: "uma_VariabilityElement" = None):
        self.variabilityType = variabilityType
        self.uma_VariabilityElement = uma_VariabilityElement
        self.uma_VariabilityElement308 = uma_VariabilityElement308
        
    @property
    def variabilityType(self) -> str:
        return self.__variabilityType

    @variabilityType.setter
    def variabilityType(self, variabilityType: str):
        self.__variabilityType = variabilityType

    @property
    def uma_VariabilityElement(self):
        return self.__uma_VariabilityElement

    @uma_VariabilityElement.setter
    def uma_VariabilityElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_VariabilityElement__uma_VariabilityElement", None)
        self.__uma_VariabilityElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_VariabilityElement308"):
                opp_val = getattr(old_value, "uma_VariabilityElement308", None)
                if opp_val == self:
                    setattr(old_value, "uma_VariabilityElement308", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_VariabilityElement308"):
                opp_val = getattr(value, "uma_VariabilityElement308", None)
                setattr(value, "uma_VariabilityElement308", self)

    @property
    def uma_VariabilityElement308(self):
        return self.__uma_VariabilityElement308

    @uma_VariabilityElement308.setter
    def uma_VariabilityElement308(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_VariabilityElement__uma_VariabilityElement308", None)
        self.__uma_VariabilityElement308 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_VariabilityElement"):
                opp_val = getattr(old_value, "uma_VariabilityElement", None)
                if opp_val == self:
                    setattr(old_value, "uma_VariabilityElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_VariabilityElement"):
                opp_val = getattr(value, "uma_VariabilityElement", None)
                setattr(value, "uma_VariabilityElement", self)

class uma_WorkDefinition(MethodElement):

    pass
class uma_MethodPackage(Package, MethodElement):

    def __init__(self, global: str, uma_MethodPackage: "uma_MethodPackage" = None, uma_MethodPackage71: set["uma_MethodPackage"] = None, uma_MethodPackage75: "uma_MethodPackage" = None, uma_MethodPackage73: set["uma_MethodPackage"] = None, uma_MethodPackage304: "uma_MethodPlugin" = None, uma_MethodPackage317: "uma_MethodConfiguration" = None):
        self.global = global
        self.uma_MethodPackage = uma_MethodPackage
        self.uma_MethodPackage71 = uma_MethodPackage71 if uma_MethodPackage71 is not None else set()
        self.uma_MethodPackage75 = uma_MethodPackage75
        self.uma_MethodPackage73 = uma_MethodPackage73 if uma_MethodPackage73 is not None else set()
        self.uma_MethodPackage304 = uma_MethodPackage304
        self.uma_MethodPackage317 = uma_MethodPackage317
        
    @property
    def global(self) -> str:
        return self.__global

    @global.setter
    def global(self, global: str):
        self.__global = global

    @property
    def uma_MethodPackage304(self):
        return self.__uma_MethodPackage304

    @uma_MethodPackage304.setter
    def uma_MethodPackage304(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_MethodPackage__uma_MethodPackage304", None)
        self.__uma_MethodPackage304 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_MethodPlugin"):
                opp_val = getattr(old_value, "uma_MethodPlugin", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_MethodPlugin"):
                opp_val = getattr(value, "uma_MethodPlugin", None)
                if opp_val is None:
                    setattr(value, "uma_MethodPlugin", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uma_MethodPackage73(self):
        return self.__uma_MethodPackage73

    @uma_MethodPackage73.setter
    def uma_MethodPackage73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_MethodPackage__uma_MethodPackage73", None)
        self.__uma_MethodPackage73 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uma_MethodPackage75"):
                    opp_val = getattr(item, "uma_MethodPackage75", None)
                    
                    if opp_val == self:
                        setattr(item, "uma_MethodPackage75", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uma_MethodPackage75"):
                    opp_val = getattr(item, "uma_MethodPackage75", None)
                    
                    setattr(item, "uma_MethodPackage75", self)
                    

    @property
    def uma_MethodPackage317(self):
        return self.__uma_MethodPackage317

    @uma_MethodPackage317.setter
    def uma_MethodPackage317(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_MethodPackage__uma_MethodPackage317", None)
        self.__uma_MethodPackage317 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_MethodConfiguration316"):
                opp_val = getattr(old_value, "uma_MethodConfiguration316", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_MethodConfiguration316"):
                opp_val = getattr(value, "uma_MethodConfiguration316", None)
                if opp_val is None:
                    setattr(value, "uma_MethodConfiguration316", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uma_MethodPackage71(self):
        return self.__uma_MethodPackage71

    @uma_MethodPackage71.setter
    def uma_MethodPackage71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_MethodPackage__uma_MethodPackage71", None)
        self.__uma_MethodPackage71 = value if value is not None else set()
        
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
            if hasattr(old_value, "uma_MethodPackage71"):
                opp_val = getattr(old_value, "uma_MethodPackage71", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_MethodPackage71"):
                opp_val = getattr(value, "uma_MethodPackage71", None)
                if opp_val is None:
                    setattr(value, "uma_MethodPackage71", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uma_MethodPackage75(self):
        return self.__uma_MethodPackage75

    @uma_MethodPackage75.setter
    def uma_MethodPackage75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_MethodPackage__uma_MethodPackage75", None)
        self.__uma_MethodPackage75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_MethodPackage73"):
                opp_val = getattr(old_value, "uma_MethodPackage73", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_MethodPackage73"):
                opp_val = getattr(value, "uma_MethodPackage73", None)
                if opp_val is None:
                    setattr(value, "uma_MethodPackage73", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class uma_DiagramElement(MethodElement):

    def __init__(self, isVisible: str, DiagramElement: "uma_GraphElement" = None, contained: "uma_GraphElement" = None, referenced: set["uma_Reference"] = None, uma_DiagramElement: set["uma_Property"] = None, DiagramElement101: "uma_Reference" = None):
        self.isVisible = isVisible
        self.DiagramElement = DiagramElement
        self.contained = contained
        self.referenced = referenced if referenced is not None else set()
        self.uma_DiagramElement = uma_DiagramElement if uma_DiagramElement is not None else set()
        self.DiagramElement101 = DiagramElement101
        
    @property
    def isVisible(self) -> str:
        return self.__isVisible

    @isVisible.setter
    def isVisible(self, isVisible: str):
        self.__isVisible = isVisible

    @property
    def referenced(self):
        return self.__referenced

    @referenced.setter
    def referenced(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_DiagramElement__referenced", None)
        self.__referenced = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Reference"):
                    opp_val = getattr(item, "Reference", None)
                    
                    if opp_val == self:
                        setattr(item, "Reference", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Reference"):
                    opp_val = getattr(item, "Reference", None)
                    
                    setattr(item, "Reference", self)
                    

    @property
    def contained(self):
        return self.__contained

    @contained.setter
    def contained(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_DiagramElement__contained", None)
        self.__contained = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GraphElement"):
                opp_val = getattr(old_value, "GraphElement", None)
                if opp_val == self:
                    setattr(old_value, "GraphElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GraphElement"):
                opp_val = getattr(value, "GraphElement", None)
                setattr(value, "GraphElement", self)

    @property
    def uma_DiagramElement(self):
        return self.__uma_DiagramElement

    @uma_DiagramElement.setter
    def uma_DiagramElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_DiagramElement__uma_DiagramElement", None)
        self.__uma_DiagramElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uma_Property"):
                    opp_val = getattr(item, "uma_Property", None)
                    
                    if opp_val == self:
                        setattr(item, "uma_Property", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uma_Property"):
                    opp_val = getattr(item, "uma_Property", None)
                    
                    setattr(item, "uma_Property", self)
                    

    @property
    def DiagramElement(self):
        return self.__DiagramElement

    @DiagramElement.setter
    def DiagramElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_DiagramElement__DiagramElement", None)
        self.__DiagramElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "container"):
                opp_val = getattr(old_value, "container", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "container"):
                opp_val = getattr(value, "container", None)
                if opp_val is None:
                    setattr(value, "container", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def DiagramElement101(self):
        return self.__DiagramElement101

    @DiagramElement101.setter
    def DiagramElement101(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_DiagramElement__DiagramElement101", None)
        self.__DiagramElement101 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reference"):
                opp_val = getattr(old_value, "reference", None)
                if opp_val == self:
                    setattr(old_value, "reference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reference"):
                opp_val = getattr(value, "reference", None)
                setattr(value, "reference", self)

class Classifier:

    pass
class uma_DescribableElement(Classifier, MethodElement):

    def __init__(self, presentationName: str, shapeicon: str, nodeicon: str, uma_DescribableElement: "uma_ContentDescription" = None, uma_DescribableElement271: "uma_CustomCategory" = None):
        self.presentationName = presentationName
        self.shapeicon = shapeicon
        self.nodeicon = nodeicon
        self.uma_DescribableElement = uma_DescribableElement
        self.uma_DescribableElement271 = uma_DescribableElement271
        
    @property
    def shapeicon(self) -> str:
        return self.__shapeicon

    @shapeicon.setter
    def shapeicon(self, shapeicon: str):
        self.__shapeicon = shapeicon

    @property
    def presentationName(self) -> str:
        return self.__presentationName

    @presentationName.setter
    def presentationName(self, presentationName: str):
        self.__presentationName = presentationName

    @property
    def nodeicon(self) -> str:
        return self.__nodeicon

    @nodeicon.setter
    def nodeicon(self, nodeicon: str):
        self.__nodeicon = nodeicon

    @property
    def uma_DescribableElement271(self):
        return self.__uma_DescribableElement271

    @uma_DescribableElement271.setter
    def uma_DescribableElement271(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_DescribableElement__uma_DescribableElement271", None)
        self.__uma_DescribableElement271 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_CustomCategory"):
                opp_val = getattr(old_value, "uma_CustomCategory", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_CustomCategory"):
                opp_val = getattr(value, "uma_CustomCategory", None)
                if opp_val is None:
                    setattr(value, "uma_CustomCategory", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "uma_ContentDescription"):
                opp_val = getattr(old_value, "uma_ContentDescription", None)
                if opp_val == self:
                    setattr(old_value, "uma_ContentDescription", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_ContentDescription"):
                opp_val = getattr(value, "uma_ContentDescription", None)
                setattr(value, "uma_ContentDescription", self)

class uma_TermDefinition(Guidance):

    pass
class uma_ReusableAsset(Guidance):

    pass
class uma_Example(Guidance):

    pass
class uma_Guideline(Guidance):

    pass
class uma_Checklist(Guidance):

    pass
class uma_Concept(Guidance):

    pass
class uma_SupportingMaterial(Guidance):

    pass
class VariabilityElement:

    pass
class uma_Activity(VariabilityElement, WorkDefinition, WorkBreakdownElement):

    def __init__(self, isEnactable: str, superActivities: set["uma_BreakdownElement"] = None, uma_Activity: set["uma_Roadmap"] = None, uma_Activity124: set["uma_SupportingMaterial"] = None, uma_Activity127: set["uma_Checklist"] = None, uma_Activity130: set["uma_Concept"] = None, uma_Activity133: set["uma_Example"] = None, uma_Activity136: set["uma_Guideline"] = None, uma_Activity139: set["uma_ReusableAsset"] = None, Activity: "uma_BreakdownElement" = None, uma_Activity213: "uma_Practice" = None, uma_Activity254: "uma_Discipline" = None):
        self.isEnactable = isEnactable
        self.superActivities = superActivities if superActivities is not None else set()
        self.uma_Activity = uma_Activity if uma_Activity is not None else set()
        self.uma_Activity124 = uma_Activity124 if uma_Activity124 is not None else set()
        self.uma_Activity127 = uma_Activity127 if uma_Activity127 is not None else set()
        self.uma_Activity130 = uma_Activity130 if uma_Activity130 is not None else set()
        self.uma_Activity133 = uma_Activity133 if uma_Activity133 is not None else set()
        self.uma_Activity136 = uma_Activity136 if uma_Activity136 is not None else set()
        self.uma_Activity139 = uma_Activity139 if uma_Activity139 is not None else set()
        self.Activity = Activity
        self.uma_Activity213 = uma_Activity213
        self.uma_Activity254 = uma_Activity254
        
    @property
    def isEnactable(self) -> str:
        return self.__isEnactable

    @isEnactable.setter
    def isEnactable(self, isEnactable: str):
        self.__isEnactable = isEnactable

    @property
    def uma_Activity127(self):
        return self.__uma_Activity127

    @uma_Activity127.setter
    def uma_Activity127(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Activity__uma_Activity127", None)
        self.__uma_Activity127 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uma_Checklist128"):
                    opp_val = getattr(item, "uma_Checklist128", None)
                    
                    if opp_val == self:
                        setattr(item, "uma_Checklist128", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uma_Checklist128"):
                    opp_val = getattr(item, "uma_Checklist128", None)
                    
                    setattr(item, "uma_Checklist128", self)
                    

    @property
    def Activity(self):
        return self.__Activity

    @Activity.setter
    def Activity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Activity__Activity", None)
        self.__Activity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "breakdownElements"):
                opp_val = getattr(old_value, "breakdownElements", None)
                if opp_val == self:
                    setattr(old_value, "breakdownElements", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "breakdownElements"):
                opp_val = getattr(value, "breakdownElements", None)
                setattr(value, "breakdownElements", self)

    @property
    def uma_Activity139(self):
        return self.__uma_Activity139

    @uma_Activity139.setter
    def uma_Activity139(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Activity__uma_Activity139", None)
        self.__uma_Activity139 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uma_ReusableAsset140"):
                    opp_val = getattr(item, "uma_ReusableAsset140", None)
                    
                    if opp_val == self:
                        setattr(item, "uma_ReusableAsset140", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uma_ReusableAsset140"):
                    opp_val = getattr(item, "uma_ReusableAsset140", None)
                    
                    setattr(item, "uma_ReusableAsset140", self)
                    

    @property
    def superActivities(self):
        return self.__superActivities

    @superActivities.setter
    def superActivities(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Activity__superActivities", None)
        self.__superActivities = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BreakdownElement"):
                    opp_val = getattr(item, "BreakdownElement", None)
                    
                    if opp_val == self:
                        setattr(item, "BreakdownElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BreakdownElement"):
                    opp_val = getattr(item, "BreakdownElement", None)
                    
                    setattr(item, "BreakdownElement", self)
                    

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
                if hasattr(item, "uma_Roadmap"):
                    opp_val = getattr(item, "uma_Roadmap", None)
                    
                    if opp_val == self:
                        setattr(item, "uma_Roadmap", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uma_Roadmap"):
                    opp_val = getattr(item, "uma_Roadmap", None)
                    
                    setattr(item, "uma_Roadmap", self)
                    

    @property
    def uma_Activity124(self):
        return self.__uma_Activity124

    @uma_Activity124.setter
    def uma_Activity124(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Activity__uma_Activity124", None)
        self.__uma_Activity124 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uma_SupportingMaterial125"):
                    opp_val = getattr(item, "uma_SupportingMaterial125", None)
                    
                    if opp_val == self:
                        setattr(item, "uma_SupportingMaterial125", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uma_SupportingMaterial125"):
                    opp_val = getattr(item, "uma_SupportingMaterial125", None)
                    
                    setattr(item, "uma_SupportingMaterial125", self)
                    

    @property
    def uma_Activity136(self):
        return self.__uma_Activity136

    @uma_Activity136.setter
    def uma_Activity136(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Activity__uma_Activity136", None)
        self.__uma_Activity136 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uma_Guideline137"):
                    opp_val = getattr(item, "uma_Guideline137", None)
                    
                    if opp_val == self:
                        setattr(item, "uma_Guideline137", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uma_Guideline137"):
                    opp_val = getattr(item, "uma_Guideline137", None)
                    
                    setattr(item, "uma_Guideline137", self)
                    

    @property
    def uma_Activity133(self):
        return self.__uma_Activity133

    @uma_Activity133.setter
    def uma_Activity133(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Activity__uma_Activity133", None)
        self.__uma_Activity133 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uma_Example134"):
                    opp_val = getattr(item, "uma_Example134", None)
                    
                    if opp_val == self:
                        setattr(item, "uma_Example134", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uma_Example134"):
                    opp_val = getattr(item, "uma_Example134", None)
                    
                    setattr(item, "uma_Example134", self)
                    

    @property
    def uma_Activity213(self):
        return self.__uma_Activity213

    @uma_Activity213.setter
    def uma_Activity213(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Activity__uma_Activity213", None)
        self.__uma_Activity213 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_Practice212"):
                opp_val = getattr(old_value, "uma_Practice212", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_Practice212"):
                opp_val = getattr(value, "uma_Practice212", None)
                if opp_val is None:
                    setattr(value, "uma_Practice212", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uma_Activity254(self):
        return self.__uma_Activity254

    @uma_Activity254.setter
    def uma_Activity254(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Activity__uma_Activity254", None)
        self.__uma_Activity254 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_Discipline253"):
                opp_val = getattr(old_value, "uma_Discipline253", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_Discipline253"):
                opp_val = getattr(value, "uma_Discipline253", None)
                if opp_val is None:
                    setattr(value, "uma_Discipline253", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uma_Activity130(self):
        return self.__uma_Activity130

    @uma_Activity130.setter
    def uma_Activity130(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Activity__uma_Activity130", None)
        self.__uma_Activity130 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uma_Concept131"):
                    opp_val = getattr(item, "uma_Concept131", None)
                    
                    if opp_val == self:
                        setattr(item, "uma_Concept131", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uma_Concept131"):
                    opp_val = getattr(item, "uma_Concept131", None)
                    
                    setattr(item, "uma_Concept131", self)
                    

class uma_Section(VariabilityElement):

    def __init__(self, sectionName: str, sectionDescription: str, uma_Section: "uma_ContentDescription" = None, uma_Section21: "uma_Section" = None, uma_Section19: set["uma_Section"] = None, uma_Section24: "uma_Section" = None, uma_Section22: "uma_Section" = None, uma_Section203: "uma_TaskDescriptor" = None):
        self.sectionName = sectionName
        self.sectionDescription = sectionDescription
        self.uma_Section = uma_Section
        self.uma_Section21 = uma_Section21
        self.uma_Section19 = uma_Section19 if uma_Section19 is not None else set()
        self.uma_Section24 = uma_Section24
        self.uma_Section22 = uma_Section22
        self.uma_Section203 = uma_Section203
        
    @property
    def sectionName(self) -> str:
        return self.__sectionName

    @sectionName.setter
    def sectionName(self, sectionName: str):
        self.__sectionName = sectionName

    @property
    def sectionDescription(self) -> str:
        return self.__sectionDescription

    @sectionDescription.setter
    def sectionDescription(self, sectionDescription: str):
        self.__sectionDescription = sectionDescription

    @property
    def uma_Section24(self):
        return self.__uma_Section24

    @uma_Section24.setter
    def uma_Section24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Section__uma_Section24", None)
        self.__uma_Section24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_Section22"):
                opp_val = getattr(old_value, "uma_Section22", None)
                if opp_val == self:
                    setattr(old_value, "uma_Section22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_Section22"):
                opp_val = getattr(value, "uma_Section22", None)
                setattr(value, "uma_Section22", self)

    @property
    def uma_Section22(self):
        return self.__uma_Section22

    @uma_Section22.setter
    def uma_Section22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Section__uma_Section22", None)
        self.__uma_Section22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_Section24"):
                opp_val = getattr(old_value, "uma_Section24", None)
                if opp_val == self:
                    setattr(old_value, "uma_Section24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_Section24"):
                opp_val = getattr(value, "uma_Section24", None)
                setattr(value, "uma_Section24", self)

    @property
    def uma_Section203(self):
        return self.__uma_Section203

    @uma_Section203.setter
    def uma_Section203(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Section__uma_Section203", None)
        self.__uma_Section203 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_TaskDescriptor202"):
                opp_val = getattr(old_value, "uma_TaskDescriptor202", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_TaskDescriptor202"):
                opp_val = getattr(value, "uma_TaskDescriptor202", None)
                if opp_val is None:
                    setattr(value, "uma_TaskDescriptor202", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uma_Section19(self):
        return self.__uma_Section19

    @uma_Section19.setter
    def uma_Section19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Section__uma_Section19", None)
        self.__uma_Section19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uma_Section21"):
                    opp_val = getattr(item, "uma_Section21", None)
                    
                    if opp_val == self:
                        setattr(item, "uma_Section21", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uma_Section21"):
                    opp_val = getattr(item, "uma_Section21", None)
                    
                    setattr(item, "uma_Section21", self)
                    

    @property
    def uma_Section21(self):
        return self.__uma_Section21

    @uma_Section21.setter
    def uma_Section21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Section__uma_Section21", None)
        self.__uma_Section21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_Section19"):
                opp_val = getattr(old_value, "uma_Section19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_Section19"):
                opp_val = getattr(value, "uma_Section19", None)
                if opp_val is None:
                    setattr(value, "uma_Section19", set([self]))
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
            if hasattr(old_value, "uma_ContentDescription18"):
                opp_val = getattr(old_value, "uma_ContentDescription18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_ContentDescription18"):
                opp_val = getattr(value, "uma_ContentDescription18", None)
                if opp_val is None:
                    setattr(value, "uma_ContentDescription18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class DescribableElement:

    pass
class uma_ProcessElement(DescribableElement):

    pass
class uma_ContentElement(DescribableElement, VariabilityElement):

    pass
class PackageableElement:

    pass
class uma_Type(PackageableElement):

    pass
class Type:

    pass
class uma_Classifier(Type):

    pass
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
            if hasattr(old_value, "uma_MethodElement2"):
                opp_val = getattr(old_value, "uma_MethodElement2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_MethodElement2"):
                opp_val = getattr(value, "uma_MethodElement2", None)
                if opp_val is None:
                    setattr(value, "uma_MethodElement2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class uma_Constraint(MethodElement):

    def __init__(self, body: str, uma_Constraint: "uma_MethodElement" = None, uma_Constraint60: "uma_WorkDefinition" = None, uma_Constraint63: "uma_WorkDefinition" = None):
        self.body = body
        self.uma_Constraint = uma_Constraint
        self.uma_Constraint60 = uma_Constraint60
        self.uma_Constraint63 = uma_Constraint63
        
    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

    @property
    def uma_Constraint63(self):
        return self.__uma_Constraint63

    @uma_Constraint63.setter
    def uma_Constraint63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Constraint__uma_Constraint63", None)
        self.__uma_Constraint63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_WorkDefinition62"):
                opp_val = getattr(old_value, "uma_WorkDefinition62", None)
                if opp_val == self:
                    setattr(old_value, "uma_WorkDefinition62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_WorkDefinition62"):
                opp_val = getattr(value, "uma_WorkDefinition62", None)
                setattr(value, "uma_WorkDefinition62", self)

    @property
    def uma_Constraint60(self):
        return self.__uma_Constraint60

    @uma_Constraint60.setter
    def uma_Constraint60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Constraint__uma_Constraint60", None)
        self.__uma_Constraint60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_WorkDefinition"):
                opp_val = getattr(old_value, "uma_WorkDefinition", None)
                if opp_val == self:
                    setattr(old_value, "uma_WorkDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_WorkDefinition"):
                opp_val = getattr(value, "uma_WorkDefinition", None)
                setattr(value, "uma_WorkDefinition", self)

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

class uma_MethodElement(PackageableElement):

    def __init__(self, guid: str, briefDescription: str, suppressed: str, orderingGuide: str, uma_MethodElement: set["uma_Constraint"] = None, uma_MethodElement2: set["uma_MethodElementProperty"] = None, uma_MethodElement115: "uma_UMASemanticModelBridge" = None):
        self.guid = guid
        self.briefDescription = briefDescription
        self.suppressed = suppressed
        self.orderingGuide = orderingGuide
        self.uma_MethodElement = uma_MethodElement if uma_MethodElement is not None else set()
        self.uma_MethodElement2 = uma_MethodElement2 if uma_MethodElement2 is not None else set()
        self.uma_MethodElement115 = uma_MethodElement115
        
    @property
    def guid(self) -> str:
        return self.__guid

    @guid.setter
    def guid(self, guid: str):
        self.__guid = guid

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
    def briefDescription(self) -> str:
        return self.__briefDescription

    @briefDescription.setter
    def briefDescription(self, briefDescription: str):
        self.__briefDescription = briefDescription

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
                    

    @property
    def uma_MethodElement115(self):
        return self.__uma_MethodElement115

    @uma_MethodElement115.setter
    def uma_MethodElement115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_MethodElement__uma_MethodElement115", None)
        self.__uma_MethodElement115 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_UMASemanticModelBridge"):
                opp_val = getattr(old_value, "uma_UMASemanticModelBridge", None)
                if opp_val == self:
                    setattr(old_value, "uma_UMASemanticModelBridge", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_UMASemanticModelBridge"):
                opp_val = getattr(value, "uma_UMASemanticModelBridge", None)
                setattr(value, "uma_UMASemanticModelBridge", self)

    @property
    def uma_MethodElement2(self):
        return self.__uma_MethodElement2

    @uma_MethodElement2.setter
    def uma_MethodElement2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_MethodElement__uma_MethodElement2", None)
        self.__uma_MethodElement2 = value if value is not None else set()
        
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
                    

class Namespace:

    pass
class uma_Package(Namespace, PackageableElement):

    pass
class NamedElement:

    pass
class uma_Namespace(NamedElement):

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

class uma_Element(ABC):

    pass