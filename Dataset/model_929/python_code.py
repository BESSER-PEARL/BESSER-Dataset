from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class WorkOrderType(Enum):
    finishToStart = "finishToStart"
    finishToFinish = "finishToFinish"
    startToStart = "startToStart"
    startToFinish = "startToFinish"
class VariabilityType(Enum):
    localContribution = "localContribution"
    localReplacement = "localReplacement"
    na = "na"
    contributes = "contributes"
    extends = "extends"
    replaces = "replaces"
class PseudoStateKind(Enum):
    initial = "initial"
    join = "join"
    fork = "fork"
    junction = "junction"
    choice = "choice"
    entryPoint = "entryPoint"
    exitPoint = "exitPoint"
    terminate = "terminate"


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
class uma_DeliveryProcess(Process):

    pass
class uma_CapabilityPattern(Process):

    pass
class ContentCategory:

    pass
class uma_RoleSetGrouping(ContentCategory):

    pass
class uma_Domain(ContentCategory):

    pass
class uma_RoleSet(ContentCategory):

    pass
class uma_Tool(ContentCategory):

    pass
class uma_DisciplineGrouping(ContentCategory):

    pass
class uma_CustomCategory(ContentCategory):

    pass
class uma_Discipline(ContentCategory):

    pass
class uma_WorkProductType(ContentCategory):

    pass
class uma_Transition:

    pass
class uma_Vertex:

    pass
class uma_Region:

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
class uma_TermDefinition(Guidance):

    pass
class uma_Practice(Guidance):

    pass
class ProcessDescription:

    pass
class uma_DeliveryProcessDescription(ProcessDescription):

    def __init__(self, typeOfContract: str, scale: str, projectCharacteristics: str, riskLevel: str, estimatingTechnique: str, projectMemberExpertise: str):
        self.typeOfContract = typeOfContract
        self.scale = scale
        self.projectCharacteristics = projectCharacteristics
        self.riskLevel = riskLevel
        self.estimatingTechnique = estimatingTechnique
        self.projectMemberExpertise = projectMemberExpertise
        
    @property
    def projectMemberExpertise(self) -> str:
        return self.__projectMemberExpertise

    @projectMemberExpertise.setter
    def projectMemberExpertise(self, projectMemberExpertise: str):
        self.__projectMemberExpertise = projectMemberExpertise

    @property
    def riskLevel(self) -> str:
        return self.__riskLevel

    @riskLevel.setter
    def riskLevel(self, riskLevel: str):
        self.__riskLevel = riskLevel

    @property
    def typeOfContract(self) -> str:
        return self.__typeOfContract

    @typeOfContract.setter
    def typeOfContract(self, typeOfContract: str):
        self.__typeOfContract = typeOfContract

    @property
    def projectCharacteristics(self) -> str:
        return self.__projectCharacteristics

    @projectCharacteristics.setter
    def projectCharacteristics(self, projectCharacteristics: str):
        self.__projectCharacteristics = projectCharacteristics

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
    def howtoStaff(self) -> str:
        return self.__howtoStaff

    @howtoStaff.setter
    def howtoStaff(self, howtoStaff: str):
        self.__howtoStaff = howtoStaff

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

class RoleDescriptor:

    pass
class uma_CompositeRole(RoleDescriptor):

    pass
class ActivityDescription:

    pass
class uma_ProcessDescription(ActivityDescription):

    def __init__(self, externalId: str, scope: str, usageNotes: str):
        self.externalId = externalId
        self.scope = scope
        self.usageNotes = usageNotes
        
    @property
    def usageNotes(self) -> str:
        return self.__usageNotes

    @usageNotes.setter
    def usageNotes(self, usageNotes: str):
        self.__usageNotes = usageNotes

    @property
    def externalId(self) -> str:
        return self.__externalId

    @externalId.setter
    def externalId(self, externalId: str):
        self.__externalId = externalId

    @property
    def scope(self) -> str:
        return self.__scope

    @scope.setter
    def scope(self, scope: str):
        self.__scope = scope

class Descriptor:

    pass
class uma_ProcessComponentDescriptor(Descriptor):

    pass
class uma_WorkProductDescriptor(Descriptor):

    def __init__(self, activityEntryState: str, activityExitState: str, uma_WorkProductDescriptor: "uma_RoleDescriptor" = None, uma_WorkProductDescriptor159: "uma_RoleDescriptor" = None, uma_WorkProductDescriptor187: "uma_TaskDescriptor" = None, uma_WorkProductDescriptor190: "uma_TaskDescriptor" = None, uma_WorkProductDescriptor193: "uma_TaskDescriptor" = None, uma_WorkProductDescriptor164: "uma_WorkProduct" = None, WorkProductDescriptor: "uma_WorkProductDescriptor" = None, impacts: set["uma_WorkProductDescriptor"] = None, WorkProductDescriptor170: "uma_WorkProductDescriptor" = None, impactedBy: set["uma_WorkProductDescriptor"] = None, uma_WorkProductDescriptor173: "uma_WorkProductDescriptor" = None, uma_WorkProductDescriptor171: set["uma_WorkProductDescriptor"] = None, uma_WorkProductDescriptor184: "uma_TaskDescriptor" = None, uma_WorkProductDescriptor296: "uma_ProcessComponentInterface" = None):
        self.activityEntryState = activityEntryState
        self.activityExitState = activityExitState
        self.uma_WorkProductDescriptor = uma_WorkProductDescriptor
        self.uma_WorkProductDescriptor159 = uma_WorkProductDescriptor159
        self.uma_WorkProductDescriptor187 = uma_WorkProductDescriptor187
        self.uma_WorkProductDescriptor190 = uma_WorkProductDescriptor190
        self.uma_WorkProductDescriptor193 = uma_WorkProductDescriptor193
        self.uma_WorkProductDescriptor164 = uma_WorkProductDescriptor164
        self.WorkProductDescriptor = WorkProductDescriptor
        self.impacts = impacts if impacts is not None else set()
        self.WorkProductDescriptor170 = WorkProductDescriptor170
        self.impactedBy = impactedBy if impactedBy is not None else set()
        self.uma_WorkProductDescriptor173 = uma_WorkProductDescriptor173
        self.uma_WorkProductDescriptor171 = uma_WorkProductDescriptor171 if uma_WorkProductDescriptor171 is not None else set()
        self.uma_WorkProductDescriptor184 = uma_WorkProductDescriptor184
        self.uma_WorkProductDescriptor296 = uma_WorkProductDescriptor296
        
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
    def uma_WorkProductDescriptor187(self):
        return self.__uma_WorkProductDescriptor187

    @uma_WorkProductDescriptor187.setter
    def uma_WorkProductDescriptor187(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_WorkProductDescriptor__uma_WorkProductDescriptor187", None)
        self.__uma_WorkProductDescriptor187 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_TaskDescriptor186"):
                opp_val = getattr(old_value, "uma_TaskDescriptor186", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_TaskDescriptor186"):
                opp_val = getattr(value, "uma_TaskDescriptor186", None)
                if opp_val is None:
                    setattr(value, "uma_TaskDescriptor186", set([self]))
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
    def uma_WorkProductDescriptor296(self):
        return self.__uma_WorkProductDescriptor296

    @uma_WorkProductDescriptor296.setter
    def uma_WorkProductDescriptor296(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_WorkProductDescriptor__uma_WorkProductDescriptor296", None)
        self.__uma_WorkProductDescriptor296 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_ProcessComponentInterface295"):
                opp_val = getattr(old_value, "uma_ProcessComponentInterface295", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_ProcessComponentInterface295"):
                opp_val = getattr(value, "uma_ProcessComponentInterface295", None)
                if opp_val is None:
                    setattr(value, "uma_ProcessComponentInterface295", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def WorkProductDescriptor170(self):
        return self.__WorkProductDescriptor170

    @WorkProductDescriptor170.setter
    def WorkProductDescriptor170(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_WorkProductDescriptor__WorkProductDescriptor170", None)
        self.__WorkProductDescriptor170 = value
        
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
                if hasattr(item, "WorkProductDescriptor170"):
                    opp_val = getattr(item, "WorkProductDescriptor170", None)
                    
                    if opp_val == self:
                        setattr(item, "WorkProductDescriptor170", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "WorkProductDescriptor170"):
                    opp_val = getattr(item, "WorkProductDescriptor170", None)
                    
                    setattr(item, "WorkProductDescriptor170", self)
                    

    @property
    def uma_WorkProductDescriptor159(self):
        return self.__uma_WorkProductDescriptor159

    @uma_WorkProductDescriptor159.setter
    def uma_WorkProductDescriptor159(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_WorkProductDescriptor__uma_WorkProductDescriptor159", None)
        self.__uma_WorkProductDescriptor159 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_RoleDescriptor158"):
                opp_val = getattr(old_value, "uma_RoleDescriptor158", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_RoleDescriptor158"):
                opp_val = getattr(value, "uma_RoleDescriptor158", None)
                if opp_val is None:
                    setattr(value, "uma_RoleDescriptor158", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uma_WorkProductDescriptor184(self):
        return self.__uma_WorkProductDescriptor184

    @uma_WorkProductDescriptor184.setter
    def uma_WorkProductDescriptor184(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_WorkProductDescriptor__uma_WorkProductDescriptor184", None)
        self.__uma_WorkProductDescriptor184 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_TaskDescriptor183"):
                opp_val = getattr(old_value, "uma_TaskDescriptor183", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_TaskDescriptor183"):
                opp_val = getattr(value, "uma_TaskDescriptor183", None)
                if opp_val is None:
                    setattr(value, "uma_TaskDescriptor183", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uma_WorkProductDescriptor190(self):
        return self.__uma_WorkProductDescriptor190

    @uma_WorkProductDescriptor190.setter
    def uma_WorkProductDescriptor190(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_WorkProductDescriptor__uma_WorkProductDescriptor190", None)
        self.__uma_WorkProductDescriptor190 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_TaskDescriptor189"):
                opp_val = getattr(old_value, "uma_TaskDescriptor189", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_TaskDescriptor189"):
                opp_val = getattr(value, "uma_TaskDescriptor189", None)
                if opp_val is None:
                    setattr(value, "uma_TaskDescriptor189", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uma_WorkProductDescriptor193(self):
        return self.__uma_WorkProductDescriptor193

    @uma_WorkProductDescriptor193.setter
    def uma_WorkProductDescriptor193(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_WorkProductDescriptor__uma_WorkProductDescriptor193", None)
        self.__uma_WorkProductDescriptor193 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_TaskDescriptor192"):
                opp_val = getattr(old_value, "uma_TaskDescriptor192", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_TaskDescriptor192"):
                opp_val = getattr(value, "uma_TaskDescriptor192", None)
                if opp_val is None:
                    setattr(value, "uma_TaskDescriptor192", set([self]))
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
    def uma_WorkProductDescriptor164(self):
        return self.__uma_WorkProductDescriptor164

    @uma_WorkProductDescriptor164.setter
    def uma_WorkProductDescriptor164(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_WorkProductDescriptor__uma_WorkProductDescriptor164", None)
        self.__uma_WorkProductDescriptor164 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_WorkProduct165"):
                opp_val = getattr(old_value, "uma_WorkProduct165", None)
                if opp_val == self:
                    setattr(old_value, "uma_WorkProduct165", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_WorkProduct165"):
                opp_val = getattr(value, "uma_WorkProduct165", None)
                setattr(value, "uma_WorkProduct165", self)

    @property
    def uma_WorkProductDescriptor173(self):
        return self.__uma_WorkProductDescriptor173

    @uma_WorkProductDescriptor173.setter
    def uma_WorkProductDescriptor173(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_WorkProductDescriptor__uma_WorkProductDescriptor173", None)
        self.__uma_WorkProductDescriptor173 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_WorkProductDescriptor171"):
                opp_val = getattr(old_value, "uma_WorkProductDescriptor171", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_WorkProductDescriptor171"):
                opp_val = getattr(value, "uma_WorkProductDescriptor171", None)
                if opp_val is None:
                    setattr(value, "uma_WorkProductDescriptor171", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uma_WorkProductDescriptor171(self):
        return self.__uma_WorkProductDescriptor171

    @uma_WorkProductDescriptor171.setter
    def uma_WorkProductDescriptor171(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_WorkProductDescriptor__uma_WorkProductDescriptor171", None)
        self.__uma_WorkProductDescriptor171 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uma_WorkProductDescriptor173"):
                    opp_val = getattr(item, "uma_WorkProductDescriptor173", None)
                    
                    if opp_val == self:
                        setattr(item, "uma_WorkProductDescriptor173", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uma_WorkProductDescriptor173"):
                    opp_val = getattr(item, "uma_WorkProductDescriptor173", None)
                    
                    setattr(item, "uma_WorkProductDescriptor173", self)
                    

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
            if hasattr(old_value, "uma_RoleDescriptor156"):
                opp_val = getattr(old_value, "uma_RoleDescriptor156", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_RoleDescriptor156"):
                opp_val = getattr(value, "uma_RoleDescriptor156", None)
                if opp_val is None:
                    setattr(value, "uma_RoleDescriptor156", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ProcessElement:

    pass
class uma_PlanningData(ProcessElement):

    def __init__(self, startDate: str, finishDate: str, rank: str, uma_PlanningData: "uma_BreakdownElement" = None):
        self.startDate = startDate
        self.finishDate = finishDate
        self.rank = rank
        self.uma_PlanningData = uma_PlanningData
        
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
            if hasattr(old_value, "uma_BreakdownElement144"):
                opp_val = getattr(old_value, "uma_BreakdownElement144", None)
                if opp_val == self:
                    setattr(old_value, "uma_BreakdownElement144", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_BreakdownElement144"):
                opp_val = getattr(value, "uma_BreakdownElement144", None)
                setattr(value, "uma_BreakdownElement144", self)

class uma_WorkOrder(ProcessElement):

    def __init__(self, linkType: str, uma_WorkOrder: "uma_WorkBreakdownElement" = None, uma_WorkOrder161: "uma_WorkBreakdownElement" = None):
        self.linkType = linkType
        self.uma_WorkOrder = uma_WorkOrder
        self.uma_WorkOrder161 = uma_WorkOrder161
        
    @property
    def linkType(self) -> str:
        return self.__linkType

    @linkType.setter
    def linkType(self, linkType: str):
        self.__linkType = linkType

    @property
    def uma_WorkOrder161(self):
        return self.__uma_WorkOrder161

    @uma_WorkOrder161.setter
    def uma_WorkOrder161(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_WorkOrder__uma_WorkOrder161", None)
        self.__uma_WorkOrder161 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_WorkBreakdownElement162"):
                opp_val = getattr(old_value, "uma_WorkBreakdownElement162", None)
                if opp_val == self:
                    setattr(old_value, "uma_WorkBreakdownElement162", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_WorkBreakdownElement162"):
                opp_val = getattr(value, "uma_WorkBreakdownElement162", None)
                setattr(value, "uma_WorkBreakdownElement162", self)

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

class uma_RoleDescriptor(Descriptor):

    pass
class Activity:

    pass
class uma_Phase(Activity):

    pass
class uma_Process(Activity):

    pass
class uma_Iteration(Activity):

    pass
class uma_Roadmap(Guidance):

    pass
class uma_BreakdownElement(ProcessElement):

    def __init__(self, prefix: str, isPlanned: str, hasMultipleOccurrences: str, isOptional: str, BreakdownElement: "uma_Activity" = None, uma_BreakdownElement: "uma_BreakdownElement" = None, uma_BreakdownElement138: "uma_BreakdownElement" = None, uma_BreakdownElement142: "uma_BreakdownElement" = None, uma_BreakdownElement140: "uma_BreakdownElement" = None, uma_BreakdownElement144: "uma_PlanningData" = None, breakdownElements: "uma_Activity" = None):
        self.prefix = prefix
        self.isPlanned = isPlanned
        self.hasMultipleOccurrences = hasMultipleOccurrences
        self.isOptional = isOptional
        self.BreakdownElement = BreakdownElement
        self.uma_BreakdownElement = uma_BreakdownElement
        self.uma_BreakdownElement138 = uma_BreakdownElement138
        self.uma_BreakdownElement142 = uma_BreakdownElement142
        self.uma_BreakdownElement140 = uma_BreakdownElement140
        self.uma_BreakdownElement144 = uma_BreakdownElement144
        self.breakdownElements = breakdownElements
        
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
    def prefix(self) -> str:
        return self.__prefix

    @prefix.setter
    def prefix(self, prefix: str):
        self.__prefix = prefix

    @property
    def isPlanned(self) -> str:
        return self.__isPlanned

    @isPlanned.setter
    def isPlanned(self, isPlanned: str):
        self.__isPlanned = isPlanned

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
            if hasattr(old_value, "uma_BreakdownElement140"):
                opp_val = getattr(old_value, "uma_BreakdownElement140", None)
                if opp_val == self:
                    setattr(old_value, "uma_BreakdownElement140", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_BreakdownElement140"):
                opp_val = getattr(value, "uma_BreakdownElement140", None)
                setattr(value, "uma_BreakdownElement140", self)

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
            if hasattr(old_value, "uma_BreakdownElement138"):
                opp_val = getattr(old_value, "uma_BreakdownElement138", None)
                if opp_val == self:
                    setattr(old_value, "uma_BreakdownElement138", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_BreakdownElement138"):
                opp_val = getattr(value, "uma_BreakdownElement138", None)
                setattr(value, "uma_BreakdownElement138", self)

    @property
    def uma_BreakdownElement140(self):
        return self.__uma_BreakdownElement140

    @uma_BreakdownElement140.setter
    def uma_BreakdownElement140(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_BreakdownElement__uma_BreakdownElement140", None)
        self.__uma_BreakdownElement140 = value
        
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
    def uma_BreakdownElement138(self):
        return self.__uma_BreakdownElement138

    @uma_BreakdownElement138.setter
    def uma_BreakdownElement138(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_BreakdownElement__uma_BreakdownElement138", None)
        self.__uma_BreakdownElement138 = value
        
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
            if hasattr(old_value, "uma_PlanningData"):
                opp_val = getattr(old_value, "uma_PlanningData", None)
                if opp_val == self:
                    setattr(old_value, "uma_PlanningData", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_PlanningData"):
                opp_val = getattr(value, "uma_PlanningData", None)
                setattr(value, "uma_PlanningData", self)

class WorkBreakdownElement:

    pass
class uma_TaskDescriptor(WorkBreakdownElement, Descriptor):

    pass
class uma_Milestone(WorkBreakdownElement):

    pass
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
    def rotation(self) -> str:
        return self.__rotation

    @rotation.setter
    def rotation(self, rotation: str):
        self.__rotation = rotation

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
    def startAngle(self) -> str:
        return self.__startAngle

    @startAngle.setter
    def startAngle(self, startAngle: str):
        self.__startAngle = startAngle

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
            if hasattr(old_value, "uma_Point116"):
                opp_val = getattr(old_value, "uma_Point116", None)
                if opp_val == self:
                    setattr(old_value, "uma_Point116", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_Point116"):
                opp_val = getattr(value, "uma_Point116", None)
                setattr(value, "uma_Point116", self)

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
                if hasattr(item, "uma_Point114"):
                    opp_val = getattr(item, "uma_Point114", None)
                    
                    if opp_val == self:
                        setattr(item, "uma_Point114", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uma_Point114"):
                    opp_val = getattr(item, "uma_Point114", None)
                    
                    setattr(item, "uma_Point114", self)
                    

class BreakdownElement:

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

class uma_ProcessComponentInterface(BreakdownElement):

    pass
class uma_WorkBreakdownElement(BreakdownElement):

    def __init__(self, isRepeatable: str, isOngoing: str, isEventDriven: str, uma_WorkBreakdownElement: set["uma_WorkOrder"] = None, uma_WorkBreakdownElement162: "uma_WorkOrder" = None):
        self.isRepeatable = isRepeatable
        self.isOngoing = isOngoing
        self.isEventDriven = isEventDriven
        self.uma_WorkBreakdownElement = uma_WorkBreakdownElement if uma_WorkBreakdownElement is not None else set()
        self.uma_WorkBreakdownElement162 = uma_WorkBreakdownElement162
        
    @property
    def isOngoing(self) -> str:
        return self.__isOngoing

    @isOngoing.setter
    def isOngoing(self, isOngoing: str):
        self.__isOngoing = isOngoing

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
    def uma_WorkBreakdownElement162(self):
        return self.__uma_WorkBreakdownElement162

    @uma_WorkBreakdownElement162.setter
    def uma_WorkBreakdownElement162(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_WorkBreakdownElement__uma_WorkBreakdownElement162", None)
        self.__uma_WorkBreakdownElement162 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_WorkOrder161"):
                opp_val = getattr(old_value, "uma_WorkOrder161", None)
                if opp_val == self:
                    setattr(old_value, "uma_WorkOrder161", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_WorkOrder161"):
                opp_val = getattr(value, "uma_WorkOrder161", None)
                setattr(value, "uma_WorkOrder161", self)

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

class GraphNode:

    pass
class LeafElement:

    pass
class uma_GraphicPrimitive(LeafElement):

    pass
class uma_Image(LeafElement):

    def __init__(self, uri: str, mimeType: str):
        self.uri = uri
        self.mimeType = mimeType
        
    @property
    def uri(self) -> str:
        return self.__uri

    @uri.setter
    def uri(self, uri: str):
        self.__uri = uri

    @property
    def mimeType(self) -> str:
        return self.__mimeType

    @mimeType.setter
    def mimeType(self, mimeType: str):
        self.__mimeType = mimeType

class uma_TextElement(LeafElement):

    def __init__(self, text: str):
        self.text = text
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

class GraphElement:

    pass
class uma_GraphEdge(GraphElement):

    pass
class uma_GraphNode(GraphElement):

    pass
class uma_Diagram(GraphNode):

    def __init__(self, zoom: str, Diagram95: "uma_SemanticModelBridge" = None, Diagram: "uma_DiagramLink" = None, uma_Diagram: "uma_Point" = None, diagram: set["uma_DiagramLink"] = None, diagram107: "uma_SemanticModelBridge" = None, uma_Diagram290: "uma_ProcessPackage" = None):
        self.zoom = zoom
        self.Diagram95 = Diagram95
        self.Diagram = Diagram
        self.uma_Diagram = uma_Diagram
        self.diagram = diagram if diagram is not None else set()
        self.diagram107 = diagram107
        self.uma_Diagram290 = uma_Diagram290
        
    @property
    def zoom(self) -> str:
        return self.__zoom

    @zoom.setter
    def zoom(self, zoom: str):
        self.__zoom = zoom

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
            if hasattr(old_value, "uma_Point103"):
                opp_val = getattr(old_value, "uma_Point103", None)
                if opp_val == self:
                    setattr(old_value, "uma_Point103", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_Point103"):
                opp_val = getattr(value, "uma_Point103", None)
                setattr(value, "uma_Point103", self)

    @property
    def uma_Diagram290(self):
        return self.__uma_Diagram290

    @uma_Diagram290.setter
    def uma_Diagram290(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Diagram__uma_Diagram290", None)
        self.__uma_Diagram290 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_ProcessPackage289"):
                opp_val = getattr(old_value, "uma_ProcessPackage289", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_ProcessPackage289"):
                opp_val = getattr(value, "uma_ProcessPackage289", None)
                if opp_val is None:
                    setattr(value, "uma_ProcessPackage289", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
                if hasattr(item, "DiagramLink105"):
                    opp_val = getattr(item, "DiagramLink105", None)
                    
                    if opp_val == self:
                        setattr(item, "DiagramLink105", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DiagramLink105"):
                    opp_val = getattr(item, "DiagramLink105", None)
                    
                    setattr(item, "DiagramLink105", self)
                    

    @property
    def diagram107(self):
        return self.__diagram107

    @diagram107.setter
    def diagram107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Diagram__diagram107", None)
        self.__diagram107 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SemanticModelBridge108"):
                opp_val = getattr(old_value, "SemanticModelBridge108", None)
                if opp_val == self:
                    setattr(old_value, "SemanticModelBridge108", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SemanticModelBridge108"):
                opp_val = getattr(value, "SemanticModelBridge108", None)
                setattr(value, "SemanticModelBridge108", self)

    @property
    def Diagram95(self):
        return self.__Diagram95

    @Diagram95.setter
    def Diagram95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Diagram__Diagram95", None)
        self.__Diagram95 = value
        
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

class uma_Dimension:

    def __init__(self, width: str, height: str, uma_Dimension: "uma_GraphNode" = None):
        self.width = width
        self.height = height
        self.uma_Dimension = uma_Dimension
        
    @property
    def height(self) -> str:
        return self.__height

    @height.setter
    def height(self, height: str):
        self.__height = height

    @property
    def width(self) -> str:
        return self.__width

    @width.setter
    def width(self, width: str):
        self.__width = width

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

class DiagramElement:

    pass
class uma_Reference(DiagramElement):

    def __init__(self, isIndividualRepresentation: str, reference: "uma_DiagramElement" = None, Reference: "uma_DiagramElement" = None):
        self.isIndividualRepresentation = isIndividualRepresentation
        self.reference = reference
        self.Reference = Reference
        
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
            if hasattr(old_value, "DiagramElement97"):
                opp_val = getattr(old_value, "DiagramElement97", None)
                if opp_val == self:
                    setattr(old_value, "DiagramElement97", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DiagramElement97"):
                opp_val = getattr(value, "DiagramElement97", None)
                setattr(value, "DiagramElement97", self)

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

class uma_LeafElement(DiagramElement):

    pass
class uma_Property(DiagramElement):

    def __init__(self, key: str, value: str, uma_Property: "uma_DiagramElement" = None):
        self.key = key
        self.value = value
        self.uma_Property = uma_Property
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

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

class uma_GraphElement(DiagramElement):

    pass
class uma_Point:

    def __init__(self, x: str, y: str, uma_Point: "uma_GraphElement" = None, uma_Point85: "uma_DiagramLink" = None, uma_Point101: "uma_GraphEdge" = None, uma_Point103: "uma_Diagram" = None, uma_Point114: "uma_Polyline" = None, uma_Point116: "uma_Ellipse" = None):
        self.x = x
        self.y = y
        self.uma_Point = uma_Point
        self.uma_Point85 = uma_Point85
        self.uma_Point101 = uma_Point101
        self.uma_Point103 = uma_Point103
        self.uma_Point114 = uma_Point114
        self.uma_Point116 = uma_Point116
        
    @property
    def x(self) -> str:
        return self.__x

    @x.setter
    def x(self, x: str):
        self.__x = x

    @property
    def y(self) -> str:
        return self.__y

    @y.setter
    def y(self, y: str):
        self.__y = y

    @property
    def uma_Point103(self):
        return self.__uma_Point103

    @uma_Point103.setter
    def uma_Point103(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Point__uma_Point103", None)
        self.__uma_Point103 = value
        
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
    def uma_Point116(self):
        return self.__uma_Point116

    @uma_Point116.setter
    def uma_Point116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Point__uma_Point116", None)
        self.__uma_Point116 = value
        
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
    def uma_Point101(self):
        return self.__uma_Point101

    @uma_Point101.setter
    def uma_Point101(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Point__uma_Point101", None)
        self.__uma_Point101 = value
        
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
    def uma_Point114(self):
        return self.__uma_Point114

    @uma_Point114.setter
    def uma_Point114(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Point__uma_Point114", None)
        self.__uma_Point114 = value
        
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
    def uma_Point85(self):
        return self.__uma_Point85

    @uma_Point85.setter
    def uma_Point85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Point__uma_Point85", None)
        self.__uma_Point85 = value
        
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

class uma_SemanticModelBridge(DiagramElement):

    def __init__(self, presentation: str, SemanticModelBridge: "uma_GraphElement" = None, namespace: "uma_Diagram" = None, semanticModel: "uma_GraphElement" = None, SemanticModelBridge108: "uma_Diagram" = None):
        self.presentation = presentation
        self.SemanticModelBridge = SemanticModelBridge
        self.namespace = namespace
        self.semanticModel = semanticModel
        self.SemanticModelBridge108 = SemanticModelBridge108
        
    @property
    def presentation(self) -> str:
        return self.__presentation

    @presentation.setter
    def presentation(self, presentation: str):
        self.__presentation = presentation

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
            if hasattr(old_value, "Diagram95"):
                opp_val = getattr(old_value, "Diagram95", None)
                if opp_val == self:
                    setattr(old_value, "Diagram95", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Diagram95"):
                opp_val = getattr(value, "Diagram95", None)
                setattr(value, "Diagram95", self)

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
            if hasattr(old_value, "graphElement80"):
                opp_val = getattr(old_value, "graphElement80", None)
                if opp_val == self:
                    setattr(old_value, "graphElement80", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphElement80"):
                opp_val = getattr(value, "graphElement80", None)
                setattr(value, "graphElement80", self)

    @property
    def SemanticModelBridge108(self):
        return self.__SemanticModelBridge108

    @SemanticModelBridge108.setter
    def SemanticModelBridge108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_SemanticModelBridge__SemanticModelBridge108", None)
        self.__SemanticModelBridge108 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diagram107"):
                opp_val = getattr(old_value, "diagram107", None)
                if opp_val == self:
                    setattr(old_value, "diagram107", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagram107"):
                opp_val = getattr(value, "diagram107", None)
                setattr(value, "diagram107", self)

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
            if hasattr(old_value, "GraphElement93"):
                opp_val = getattr(old_value, "GraphElement93", None)
                if opp_val == self:
                    setattr(old_value, "GraphElement93", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GraphElement93"):
                opp_val = getattr(value, "GraphElement93", None)
                setattr(value, "GraphElement93", self)

class uma_GraphConnector(GraphElement):

    pass
class uma_DiagramLink(DiagramElement):

    def __init__(self, zoom: str, DiagramLink: "uma_GraphElement" = None, uma_DiagramLink: "uma_Point" = None, link: "uma_GraphElement" = None, diagramLink: "uma_Diagram" = None, DiagramLink105: "uma_Diagram" = None):
        self.zoom = zoom
        self.DiagramLink = DiagramLink
        self.uma_DiagramLink = uma_DiagramLink
        self.link = link
        self.diagramLink = diagramLink
        self.DiagramLink105 = DiagramLink105
        
    @property
    def zoom(self) -> str:
        return self.__zoom

    @zoom.setter
    def zoom(self, zoom: str):
        self.__zoom = zoom

    @property
    def DiagramLink105(self):
        return self.__DiagramLink105

    @DiagramLink105.setter
    def DiagramLink105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_DiagramLink__DiagramLink105", None)
        self.__DiagramLink105 = value
        
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
            if hasattr(old_value, "uma_Point85"):
                opp_val = getattr(old_value, "uma_Point85", None)
                if opp_val == self:
                    setattr(old_value, "uma_Point85", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_Point85"):
                opp_val = getattr(value, "uma_Point85", None)
                setattr(value, "uma_Point85", self)

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
    def link(self):
        return self.__link

    @link.setter
    def link(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_DiagramLink__link", None)
        self.__link = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GraphElement87"):
                opp_val = getattr(old_value, "GraphElement87", None)
                if opp_val == self:
                    setattr(old_value, "GraphElement87", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GraphElement87"):
                opp_val = getattr(value, "GraphElement87", None)
                setattr(value, "GraphElement87", self)

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

class ContentDescription:

    pass
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

class uma_PracticeDescription(ContentDescription):

    def __init__(self, additionalInfo: str, problem: str, background: str, goals: str, application: str, levelsOfAdoption: str):
        self.additionalInfo = additionalInfo
        self.problem = problem
        self.background = background
        self.goals = goals
        self.application = application
        self.levelsOfAdoption = levelsOfAdoption
        
    @property
    def background(self) -> str:
        return self.__background

    @background.setter
    def background(self, background: str):
        self.__background = background

    @property
    def problem(self) -> str:
        return self.__problem

    @problem.setter
    def problem(self, problem: str):
        self.__problem = problem

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

class uma_WorkProductDescription(ContentDescription):

    def __init__(self, externalId: str, purpose: str, impactOfNotHaving: str, reasonsForNotNeeding: str):
        self.externalId = externalId
        self.purpose = purpose
        self.impactOfNotHaving = impactOfNotHaving
        self.reasonsForNotNeeding = reasonsForNotNeeding
        
    @property
    def externalId(self) -> str:
        return self.__externalId

    @externalId.setter
    def externalId(self, externalId: str):
        self.__externalId = externalId

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

class WorkProductDescription:

    pass
class uma_DeliverableDescription(WorkProductDescription):

    def __init__(self, externalDescription: str, packagingGuidance: str):
        self.externalDescription = externalDescription
        self.packagingGuidance = packagingGuidance
        
    @property
    def externalDescription(self) -> str:
        return self.__externalDescription

    @externalDescription.setter
    def externalDescription(self, externalDescription: str):
        self.__externalDescription = externalDescription

    @property
    def packagingGuidance(self) -> str:
        return self.__packagingGuidance

    @packagingGuidance.setter
    def packagingGuidance(self, packagingGuidance: str):
        self.__packagingGuidance = packagingGuidance

class uma_ArtifactDescription(WorkProductDescription):

    def __init__(self, briefOutline: str, representationOptions: str):
        self.briefOutline = briefOutline
        self.representationOptions = representationOptions
        
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

class MethodPackage:

    pass
class uma_ProcessPackage(MethodPackage):

    pass
class uma_ContentPackage(MethodPackage):

    pass
class uma_TaskDescription(ContentDescription):

    def __init__(self, purpose: str, alternatives: str):
        self.purpose = purpose
        self.alternatives = alternatives
        
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

class uma_RoleDescription(ContentDescription):

    def __init__(self, skills: str, assignmentApproaches: str, synonyms: str):
        self.skills = skills
        self.assignmentApproaches = assignmentApproaches
        self.synonyms = synonyms
        
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

    @property
    def synonyms(self) -> str:
        return self.__synonyms

    @synonyms.setter
    def synonyms(self, synonyms: str):
        self.__synonyms = synonyms

class WorkProduct:

    pass
class uma_Deliverable(WorkProduct):

    pass
class uma_Artifact(WorkProduct):

    pass
class Section:

    pass
class Package:

    pass
class uma_Outcome(WorkProduct):

    pass
class WorkDefinition:

    pass
class uma_StateMachine(WorkDefinition):

    pass
class uma_Step(Section, WorkDefinition):

    pass
class uma_EstimationConsiderations(Guidance):

    pass
class uma_ToolMentor(Guidance):

    pass
class uma_Template(Guidance):

    pass
class uma_Report(Guidance):

    pass
class MethodUnit:

    pass
class uma_MethodConfiguration(MethodUnit):

    pass
class uma_ProcessComponent(MethodUnit, ProcessPackage):

    pass
class uma_MethodLibrary(MethodUnit, Package):

    pass
class uma_MethodPlugin(MethodUnit, Package):

    def __init__(self, userChangeable: str, uma_MethodPlugin: set["uma_MethodPackage"] = None, uma_MethodPlugin303: "uma_MethodPlugin" = None, uma_MethodPlugin301: set["uma_MethodPlugin"] = None, uma_MethodPlugin310: "uma_MethodConfiguration" = None, uma_MethodPlugin326: "uma_MethodLibrary" = None):
        self.userChangeable = userChangeable
        self.uma_MethodPlugin = uma_MethodPlugin if uma_MethodPlugin is not None else set()
        self.uma_MethodPlugin303 = uma_MethodPlugin303
        self.uma_MethodPlugin301 = uma_MethodPlugin301 if uma_MethodPlugin301 is not None else set()
        self.uma_MethodPlugin310 = uma_MethodPlugin310
        self.uma_MethodPlugin326 = uma_MethodPlugin326
        
    @property
    def userChangeable(self) -> str:
        return self.__userChangeable

    @userChangeable.setter
    def userChangeable(self, userChangeable: str):
        self.__userChangeable = userChangeable

    @property
    def uma_MethodPlugin310(self):
        return self.__uma_MethodPlugin310

    @uma_MethodPlugin310.setter
    def uma_MethodPlugin310(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_MethodPlugin__uma_MethodPlugin310", None)
        self.__uma_MethodPlugin310 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_MethodConfiguration309"):
                opp_val = getattr(old_value, "uma_MethodConfiguration309", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_MethodConfiguration309"):
                opp_val = getattr(value, "uma_MethodConfiguration309", None)
                if opp_val is None:
                    setattr(value, "uma_MethodConfiguration309", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uma_MethodPlugin326(self):
        return self.__uma_MethodPlugin326

    @uma_MethodPlugin326.setter
    def uma_MethodPlugin326(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_MethodPlugin__uma_MethodPlugin326", None)
        self.__uma_MethodPlugin326 = value
        
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
                if hasattr(item, "uma_MethodPackage300"):
                    opp_val = getattr(item, "uma_MethodPackage300", None)
                    
                    if opp_val == self:
                        setattr(item, "uma_MethodPackage300", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uma_MethodPackage300"):
                    opp_val = getattr(item, "uma_MethodPackage300", None)
                    
                    setattr(item, "uma_MethodPackage300", self)
                    

    @property
    def uma_MethodPlugin301(self):
        return self.__uma_MethodPlugin301

    @uma_MethodPlugin301.setter
    def uma_MethodPlugin301(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_MethodPlugin__uma_MethodPlugin301", None)
        self.__uma_MethodPlugin301 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uma_MethodPlugin303"):
                    opp_val = getattr(item, "uma_MethodPlugin303", None)
                    
                    if opp_val == self:
                        setattr(item, "uma_MethodPlugin303", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uma_MethodPlugin303"):
                    opp_val = getattr(item, "uma_MethodPlugin303", None)
                    
                    setattr(item, "uma_MethodPlugin303", self)
                    

    @property
    def uma_MethodPlugin303(self):
        return self.__uma_MethodPlugin303

    @uma_MethodPlugin303.setter
    def uma_MethodPlugin303(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_MethodPlugin__uma_MethodPlugin303", None)
        self.__uma_MethodPlugin303 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_MethodPlugin301"):
                opp_val = getattr(old_value, "uma_MethodPlugin301", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_MethodPlugin301"):
                opp_val = getattr(value, "uma_MethodPlugin301", None)
                if opp_val is None:
                    setattr(value, "uma_MethodPlugin301", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class uma_ContentDescription(MethodUnit):

    def __init__(self, mainDescription: str, keyConsiderations: str, uma_ContentDescription: "uma_DescribableElement" = None, uma_ContentDescription14: set["uma_Section"] = None):
        self.mainDescription = mainDescription
        self.keyConsiderations = keyConsiderations
        self.uma_ContentDescription = uma_ContentDescription
        self.uma_ContentDescription14 = uma_ContentDescription14 if uma_ContentDescription14 is not None else set()
        
    @property
    def mainDescription(self) -> str:
        return self.__mainDescription

    @mainDescription.setter
    def mainDescription(self, mainDescription: str):
        self.__mainDescription = mainDescription

    @property
    def keyConsiderations(self) -> str:
        return self.__keyConsiderations

    @keyConsiderations.setter
    def keyConsiderations(self, keyConsiderations: str):
        self.__keyConsiderations = keyConsiderations

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

    @property
    def uma_ContentDescription14(self):
        return self.__uma_ContentDescription14

    @uma_ContentDescription14.setter
    def uma_ContentDescription14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_ContentDescription__uma_ContentDescription14", None)
        self.__uma_ContentDescription14 = value if value is not None else set()
        
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
                    

class Classifier:

    pass
class uma_ReusableAsset(Guidance):

    pass
class ContentElement:

    pass
class uma_ContentCategory(ContentElement):

    pass
class uma_WorkProduct(ContentElement):

    pass
class uma_Task(ContentElement, WorkDefinition):

    pass
class uma_Guidance(ContentElement):

    pass
class uma_Role(ContentElement):

    pass
class uma_Concept(Guidance):

    pass
class uma_SupportingMaterial(Guidance):

    pass
class VariabilityElement:

    pass
class uma_Activity(VariabilityElement, WorkBreakdownElement, WorkDefinition):

    def __init__(self, isEnactable: str, uma_Activity132: set["uma_Guideline"] = None, uma_Activity135: set["uma_ReusableAsset"] = None, superActivities: set["uma_BreakdownElement"] = None, uma_Activity: set["uma_Roadmap"] = None, uma_Activity120: set["uma_SupportingMaterial"] = None, uma_Activity123: set["uma_Checklist"] = None, uma_Activity126: set["uma_Concept"] = None, uma_Activity129: set["uma_Example"] = None, Activity: "uma_BreakdownElement" = None, uma_Activity209: "uma_Practice" = None, uma_Activity250: "uma_Discipline" = None):
        self.isEnactable = isEnactable
        self.uma_Activity132 = uma_Activity132 if uma_Activity132 is not None else set()
        self.uma_Activity135 = uma_Activity135 if uma_Activity135 is not None else set()
        self.superActivities = superActivities if superActivities is not None else set()
        self.uma_Activity = uma_Activity if uma_Activity is not None else set()
        self.uma_Activity120 = uma_Activity120 if uma_Activity120 is not None else set()
        self.uma_Activity123 = uma_Activity123 if uma_Activity123 is not None else set()
        self.uma_Activity126 = uma_Activity126 if uma_Activity126 is not None else set()
        self.uma_Activity129 = uma_Activity129 if uma_Activity129 is not None else set()
        self.Activity = Activity
        self.uma_Activity209 = uma_Activity209
        self.uma_Activity250 = uma_Activity250
        
    @property
    def isEnactable(self) -> str:
        return self.__isEnactable

    @isEnactable.setter
    def isEnactable(self, isEnactable: str):
        self.__isEnactable = isEnactable

    @property
    def uma_Activity123(self):
        return self.__uma_Activity123

    @uma_Activity123.setter
    def uma_Activity123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Activity__uma_Activity123", None)
        self.__uma_Activity123 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uma_Checklist124"):
                    opp_val = getattr(item, "uma_Checklist124", None)
                    
                    if opp_val == self:
                        setattr(item, "uma_Checklist124", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uma_Checklist124"):
                    opp_val = getattr(item, "uma_Checklist124", None)
                    
                    setattr(item, "uma_Checklist124", self)
                    

    @property
    def uma_Activity135(self):
        return self.__uma_Activity135

    @uma_Activity135.setter
    def uma_Activity135(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Activity__uma_Activity135", None)
        self.__uma_Activity135 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uma_ReusableAsset136"):
                    opp_val = getattr(item, "uma_ReusableAsset136", None)
                    
                    if opp_val == self:
                        setattr(item, "uma_ReusableAsset136", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uma_ReusableAsset136"):
                    opp_val = getattr(item, "uma_ReusableAsset136", None)
                    
                    setattr(item, "uma_ReusableAsset136", self)
                    

    @property
    def uma_Activity129(self):
        return self.__uma_Activity129

    @uma_Activity129.setter
    def uma_Activity129(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Activity__uma_Activity129", None)
        self.__uma_Activity129 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uma_Example130"):
                    opp_val = getattr(item, "uma_Example130", None)
                    
                    if opp_val == self:
                        setattr(item, "uma_Example130", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uma_Example130"):
                    opp_val = getattr(item, "uma_Example130", None)
                    
                    setattr(item, "uma_Example130", self)
                    

    @property
    def uma_Activity120(self):
        return self.__uma_Activity120

    @uma_Activity120.setter
    def uma_Activity120(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Activity__uma_Activity120", None)
        self.__uma_Activity120 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uma_SupportingMaterial121"):
                    opp_val = getattr(item, "uma_SupportingMaterial121", None)
                    
                    if opp_val == self:
                        setattr(item, "uma_SupportingMaterial121", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uma_SupportingMaterial121"):
                    opp_val = getattr(item, "uma_SupportingMaterial121", None)
                    
                    setattr(item, "uma_SupportingMaterial121", self)
                    

    @property
    def uma_Activity132(self):
        return self.__uma_Activity132

    @uma_Activity132.setter
    def uma_Activity132(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Activity__uma_Activity132", None)
        self.__uma_Activity132 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uma_Guideline133"):
                    opp_val = getattr(item, "uma_Guideline133", None)
                    
                    if opp_val == self:
                        setattr(item, "uma_Guideline133", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uma_Guideline133"):
                    opp_val = getattr(item, "uma_Guideline133", None)
                    
                    setattr(item, "uma_Guideline133", self)
                    

    @property
    def uma_Activity209(self):
        return self.__uma_Activity209

    @uma_Activity209.setter
    def uma_Activity209(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Activity__uma_Activity209", None)
        self.__uma_Activity209 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_Practice208"):
                opp_val = getattr(old_value, "uma_Practice208", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_Practice208"):
                opp_val = getattr(value, "uma_Practice208", None)
                if opp_val is None:
                    setattr(value, "uma_Practice208", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uma_Activity126(self):
        return self.__uma_Activity126

    @uma_Activity126.setter
    def uma_Activity126(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Activity__uma_Activity126", None)
        self.__uma_Activity126 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uma_Concept127"):
                    opp_val = getattr(item, "uma_Concept127", None)
                    
                    if opp_val == self:
                        setattr(item, "uma_Concept127", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uma_Concept127"):
                    opp_val = getattr(item, "uma_Concept127", None)
                    
                    setattr(item, "uma_Concept127", self)
                    

    @property
    def uma_Activity250(self):
        return self.__uma_Activity250

    @uma_Activity250.setter
    def uma_Activity250(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Activity__uma_Activity250", None)
        self.__uma_Activity250 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_Discipline249"):
                opp_val = getattr(old_value, "uma_Discipline249", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_Discipline249"):
                opp_val = getattr(value, "uma_Discipline249", None)
                if opp_val is None:
                    setattr(value, "uma_Discipline249", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
                    

class uma_Section(VariabilityElement):

    def __init__(self, sectionName: str, sectionDescription: str, uma_Section17: "uma_Section" = None, uma_Section15: set["uma_Section"] = None, uma_Section20: "uma_Section" = None, uma_Section18: "uma_Section" = None, uma_Section: "uma_ContentDescription" = None, uma_Section199: "uma_TaskDescriptor" = None):
        self.sectionName = sectionName
        self.sectionDescription = sectionDescription
        self.uma_Section17 = uma_Section17
        self.uma_Section15 = uma_Section15 if uma_Section15 is not None else set()
        self.uma_Section20 = uma_Section20
        self.uma_Section18 = uma_Section18
        self.uma_Section = uma_Section
        self.uma_Section199 = uma_Section199
        
    @property
    def sectionDescription(self) -> str:
        return self.__sectionDescription

    @sectionDescription.setter
    def sectionDescription(self, sectionDescription: str):
        self.__sectionDescription = sectionDescription

    @property
    def sectionName(self) -> str:
        return self.__sectionName

    @sectionName.setter
    def sectionName(self, sectionName: str):
        self.__sectionName = sectionName

    @property
    def uma_Section199(self):
        return self.__uma_Section199

    @uma_Section199.setter
    def uma_Section199(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Section__uma_Section199", None)
        self.__uma_Section199 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_TaskDescriptor198"):
                opp_val = getattr(old_value, "uma_TaskDescriptor198", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_TaskDescriptor198"):
                opp_val = getattr(value, "uma_TaskDescriptor198", None)
                if opp_val is None:
                    setattr(value, "uma_TaskDescriptor198", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uma_Section17(self):
        return self.__uma_Section17

    @uma_Section17.setter
    def uma_Section17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Section__uma_Section17", None)
        self.__uma_Section17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_Section15"):
                opp_val = getattr(old_value, "uma_Section15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_Section15"):
                opp_val = getattr(value, "uma_Section15", None)
                if opp_val is None:
                    setattr(value, "uma_Section15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uma_Section20(self):
        return self.__uma_Section20

    @uma_Section20.setter
    def uma_Section20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Section__uma_Section20", None)
        self.__uma_Section20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_Section18"):
                opp_val = getattr(old_value, "uma_Section18", None)
                if opp_val == self:
                    setattr(old_value, "uma_Section18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_Section18"):
                opp_val = getattr(value, "uma_Section18", None)
                setattr(value, "uma_Section18", self)

    @property
    def uma_Section18(self):
        return self.__uma_Section18

    @uma_Section18.setter
    def uma_Section18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Section__uma_Section18", None)
        self.__uma_Section18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_Section20"):
                opp_val = getattr(old_value, "uma_Section20", None)
                if opp_val == self:
                    setattr(old_value, "uma_Section20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_Section20"):
                opp_val = getattr(value, "uma_Section20", None)
                setattr(value, "uma_Section20", self)

    @property
    def uma_Section15(self):
        return self.__uma_Section15

    @uma_Section15.setter
    def uma_Section15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Section__uma_Section15", None)
        self.__uma_Section15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uma_Section17"):
                    opp_val = getattr(item, "uma_Section17", None)
                    
                    if opp_val == self:
                        setattr(item, "uma_Section17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uma_Section17"):
                    opp_val = getattr(item, "uma_Section17", None)
                    
                    setattr(item, "uma_Section17", self)
                    

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
            if hasattr(old_value, "uma_ContentDescription14"):
                opp_val = getattr(old_value, "uma_ContentDescription14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_ContentDescription14"):
                opp_val = getattr(value, "uma_ContentDescription14", None)
                if opp_val is None:
                    setattr(value, "uma_ContentDescription14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class DescribableElement:

    pass
class uma_ProcessElement(DescribableElement):

    pass
class uma_ContentElement(VariabilityElement, DescribableElement):

    pass
class MethodElement:

    pass
class uma_DescribableElement(Classifier, MethodElement):

    def __init__(self, presentationName: str, shapeicon: str, nodeicon: str, uma_DescribableElement: "uma_ContentDescription" = None, uma_DescribableElement267: "uma_CustomCategory" = None):
        self.presentationName = presentationName
        self.shapeicon = shapeicon
        self.nodeicon = nodeicon
        self.uma_DescribableElement = uma_DescribableElement
        self.uma_DescribableElement267 = uma_DescribableElement267
        
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
    def presentationName(self) -> str:
        return self.__presentationName

    @presentationName.setter
    def presentationName(self, presentationName: str):
        self.__presentationName = presentationName

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

    @property
    def uma_DescribableElement267(self):
        return self.__uma_DescribableElement267

    @uma_DescribableElement267.setter
    def uma_DescribableElement267(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_DescribableElement__uma_DescribableElement267", None)
        self.__uma_DescribableElement267 = value
        
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

class uma_MethodPackage(Package, MethodElement):

    def __init__(self, global: str, uma_MethodPackage: "uma_MethodPackage" = None, uma_MethodPackage67: set["uma_MethodPackage"] = None, uma_MethodPackage71: "uma_MethodPackage" = None, uma_MethodPackage69: set["uma_MethodPackage"] = None, uma_MethodPackage300: "uma_MethodPlugin" = None, uma_MethodPackage313: "uma_MethodConfiguration" = None):
        self.global = global
        self.uma_MethodPackage = uma_MethodPackage
        self.uma_MethodPackage67 = uma_MethodPackage67 if uma_MethodPackage67 is not None else set()
        self.uma_MethodPackage71 = uma_MethodPackage71
        self.uma_MethodPackage69 = uma_MethodPackage69 if uma_MethodPackage69 is not None else set()
        self.uma_MethodPackage300 = uma_MethodPackage300
        self.uma_MethodPackage313 = uma_MethodPackage313
        
    @property
    def global(self) -> str:
        return self.__global

    @global.setter
    def global(self, global: str):
        self.__global = global

    @property
    def uma_MethodPackage69(self):
        return self.__uma_MethodPackage69

    @uma_MethodPackage69.setter
    def uma_MethodPackage69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_MethodPackage__uma_MethodPackage69", None)
        self.__uma_MethodPackage69 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uma_MethodPackage71"):
                    opp_val = getattr(item, "uma_MethodPackage71", None)
                    
                    if opp_val == self:
                        setattr(item, "uma_MethodPackage71", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uma_MethodPackage71"):
                    opp_val = getattr(item, "uma_MethodPackage71", None)
                    
                    setattr(item, "uma_MethodPackage71", self)
                    

    @property
    def uma_MethodPackage300(self):
        return self.__uma_MethodPackage300

    @uma_MethodPackage300.setter
    def uma_MethodPackage300(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_MethodPackage__uma_MethodPackage300", None)
        self.__uma_MethodPackage300 = value
        
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
    def uma_MethodPackage67(self):
        return self.__uma_MethodPackage67

    @uma_MethodPackage67.setter
    def uma_MethodPackage67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_MethodPackage__uma_MethodPackage67", None)
        self.__uma_MethodPackage67 = value if value is not None else set()
        
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
            if hasattr(old_value, "uma_MethodPackage67"):
                opp_val = getattr(old_value, "uma_MethodPackage67", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_MethodPackage67"):
                opp_val = getattr(value, "uma_MethodPackage67", None)
                if opp_val is None:
                    setattr(value, "uma_MethodPackage67", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uma_MethodPackage71(self):
        return self.__uma_MethodPackage71

    @uma_MethodPackage71.setter
    def uma_MethodPackage71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_MethodPackage__uma_MethodPackage71", None)
        self.__uma_MethodPackage71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_MethodPackage69"):
                opp_val = getattr(old_value, "uma_MethodPackage69", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_MethodPackage69"):
                opp_val = getattr(value, "uma_MethodPackage69", None)
                if opp_val is None:
                    setattr(value, "uma_MethodPackage69", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uma_MethodPackage313(self):
        return self.__uma_MethodPackage313

    @uma_MethodPackage313.setter
    def uma_MethodPackage313(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_MethodPackage__uma_MethodPackage313", None)
        self.__uma_MethodPackage313 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_MethodConfiguration312"):
                opp_val = getattr(old_value, "uma_MethodConfiguration312", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_MethodConfiguration312"):
                opp_val = getattr(value, "uma_MethodConfiguration312", None)
                if opp_val is None:
                    setattr(value, "uma_MethodConfiguration312", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class uma_VariabilityElement(MethodElement):

    def __init__(self, variabilityType: str, uma_VariabilityElement: "uma_VariabilityElement" = None, uma_VariabilityElement304: "uma_VariabilityElement" = None):
        self.variabilityType = variabilityType
        self.uma_VariabilityElement = uma_VariabilityElement
        self.uma_VariabilityElement304 = uma_VariabilityElement304
        
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
            if hasattr(old_value, "uma_VariabilityElement304"):
                opp_val = getattr(old_value, "uma_VariabilityElement304", None)
                if opp_val == self:
                    setattr(old_value, "uma_VariabilityElement304", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_VariabilityElement304"):
                opp_val = getattr(value, "uma_VariabilityElement304", None)
                setattr(value, "uma_VariabilityElement304", self)

    @property
    def uma_VariabilityElement304(self):
        return self.__uma_VariabilityElement304

    @uma_VariabilityElement304.setter
    def uma_VariabilityElement304(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_VariabilityElement__uma_VariabilityElement304", None)
        self.__uma_VariabilityElement304 = value
        
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

class uma_MethodUnit(MethodElement):

    def __init__(self, authors: str, changeDate: str, changeDescription: str, version: str, uma_MethodUnit: "uma_SupportingMaterial" = None):
        self.authors = authors
        self.changeDate = changeDate
        self.changeDescription = changeDescription
        self.version = version
        self.uma_MethodUnit = uma_MethodUnit
        
    @property
    def changeDate(self) -> str:
        return self.__changeDate

    @changeDate.setter
    def changeDate(self, changeDate: str):
        self.__changeDate = changeDate

    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

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
            if hasattr(old_value, "uma_SupportingMaterial307"):
                opp_val = getattr(old_value, "uma_SupportingMaterial307", None)
                if opp_val == self:
                    setattr(old_value, "uma_SupportingMaterial307", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_SupportingMaterial307"):
                opp_val = getattr(value, "uma_SupportingMaterial307", None)
                setattr(value, "uma_SupportingMaterial307", self)

class uma_DiagramElement(MethodElement):

    def __init__(self, isVisible: str, DiagramElement: "uma_GraphElement" = None, DiagramElement97: "uma_Reference" = None, contained: "uma_GraphElement" = None, referenced: set["uma_Reference"] = None, uma_DiagramElement: set["uma_Property"] = None):
        self.isVisible = isVisible
        self.DiagramElement = DiagramElement
        self.DiagramElement97 = DiagramElement97
        self.contained = contained
        self.referenced = referenced if referenced is not None else set()
        self.uma_DiagramElement = uma_DiagramElement if uma_DiagramElement is not None else set()
        
    @property
    def isVisible(self) -> str:
        return self.__isVisible

    @isVisible.setter
    def isVisible(self, isVisible: str):
        self.__isVisible = isVisible

    @property
    def DiagramElement97(self):
        return self.__DiagramElement97

    @DiagramElement97.setter
    def DiagramElement97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_DiagramElement__DiagramElement97", None)
        self.__DiagramElement97 = value
        
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
                    

class uma_WorkDefinition(MethodElement):

    pass
class uma_Constraint(MethodElement):

    def __init__(self, body: str, uma_Constraint: "uma_MethodElement" = None, uma_Constraint56: "uma_WorkDefinition" = None, uma_Constraint59: "uma_WorkDefinition" = None):
        self.body = body
        self.uma_Constraint = uma_Constraint
        self.uma_Constraint56 = uma_Constraint56
        self.uma_Constraint59 = uma_Constraint59
        
    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

    @property
    def uma_Constraint56(self):
        return self.__uma_Constraint56

    @uma_Constraint56.setter
    def uma_Constraint56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Constraint__uma_Constraint56", None)
        self.__uma_Constraint56 = value
        
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
    def uma_Constraint59(self):
        return self.__uma_Constraint59

    @uma_Constraint59.setter
    def uma_Constraint59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Constraint__uma_Constraint59", None)
        self.__uma_Constraint59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_WorkDefinition58"):
                opp_val = getattr(old_value, "uma_WorkDefinition58", None)
                if opp_val == self:
                    setattr(old_value, "uma_WorkDefinition58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_WorkDefinition58"):
                opp_val = getattr(value, "uma_WorkDefinition58", None)
                setattr(value, "uma_WorkDefinition58", self)

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

class uma_Example(Guidance):

    pass
class uma_Guideline(Guidance):

    pass
class uma_Checklist(Guidance):

    pass
class Namespace:

    pass
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

class uma_Element(ABC):

    pass
class PackageableElement:

    pass
class uma_Package(PackageableElement, Namespace):

    pass
class uma_Type(PackageableElement):

    pass
class Type:

    pass
class uma_Classifier(Type):

    pass
class uma_MethodElement(PackageableElement):

    def __init__(self, guid: str, briefDescription: str, suppressed: str, orderingGuide: str, uma_MethodElement: set["uma_Constraint"] = None, uma_MethodElement111: "uma_UMASemanticModelBridge" = None):
        self.guid = guid
        self.briefDescription = briefDescription
        self.suppressed = suppressed
        self.orderingGuide = orderingGuide
        self.uma_MethodElement = uma_MethodElement if uma_MethodElement is not None else set()
        self.uma_MethodElement111 = uma_MethodElement111
        
    @property
    def guid(self) -> str:
        return self.__guid

    @guid.setter
    def guid(self, guid: str):
        self.__guid = guid

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
    def orderingGuide(self) -> str:
        return self.__orderingGuide

    @orderingGuide.setter
    def orderingGuide(self, orderingGuide: str):
        self.__orderingGuide = orderingGuide

    @property
    def uma_MethodElement111(self):
        return self.__uma_MethodElement111

    @uma_MethodElement111.setter
    def uma_MethodElement111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_MethodElement__uma_MethodElement111", None)
        self.__uma_MethodElement111 = value
        
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
                    

class uma_Namespace(NamedElement):

    pass