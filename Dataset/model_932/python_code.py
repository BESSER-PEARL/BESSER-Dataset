from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class VariabilityType(Enum):
    na = "na"
    contributes = "contributes"
    extends = "extends"
    replaces = "replaces"
class WorkOrderType(Enum):
    finishToFinish = "finishToFinish"
    startToStart = "startToStart"
    startToFinish = "startToFinish"
    finishToStart = "finishToStart"


############################################
# Definition of Classes
############################################

class MethodConfiguration:

    pass
class uma_ProcessFamily(MethodConfiguration):

    pass
class Process:

    pass
class uma_ProcessContribution(Process):

    pass
class uma_DeliveryProcess(Process):

    pass
class ProcessPackage:

    pass
class uma_ProcessPlanningTemplate(Process):

    pass
class uma_CapabilityPattern(Process):

    pass
class ContentCategory:

    pass
class uma_RoleSet(ContentCategory):

    pass
class uma_WorkProductType(ContentCategory):

    pass
class uma_CustomCategory(ContentCategory):

    pass
class uma_RoleSetGrouping(ContentCategory):

    pass
class uma_Tool(ContentCategory):

    pass
class uma_Domain(ContentCategory):

    pass
class uma_DisciplineGrouping(ContentCategory):

    pass
class uma_Discipline(ContentCategory):

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
class uma_EstimationConsiderations(Guidance):

    pass
class uma_EstimatingMetric(Guidance):

    pass
class ActivityDescription:

    pass
class uma_ProcessDescription(ActivityDescription):

    def __init__(self, externalId: str, scope: str, usageNotes: str):
        self.externalId = externalId
        self.scope = scope
        self.usageNotes = usageNotes
        
    @property
    def scope(self) -> str:
        return self.__scope

    @scope.setter
    def scope(self, scope: str):
        self.__scope = scope

    @property
    def externalId(self) -> str:
        return self.__externalId

    @externalId.setter
    def externalId(self, externalId: str):
        self.__externalId = externalId

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
    def scale(self) -> str:
        return self.__scale

    @scale.setter
    def scale(self, scale: str):
        self.__scale = scale

    @property
    def projectMemberExpertise(self) -> str:
        return self.__projectMemberExpertise

    @projectMemberExpertise.setter
    def projectMemberExpertise(self, projectMemberExpertise: str):
        self.__projectMemberExpertise = projectMemberExpertise

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
class Descriptor:

    pass
class uma_ProcessComponentDescriptor(Descriptor):

    pass
class uma_WorkProductDescriptor(Descriptor):

    def __init__(self, activityEntryState: str, activityExitState: str, WorkProductDescriptor: "uma_RoleDescriptor" = None, WorkProductDescriptor174: "uma_TaskDescriptor" = None, WorkProductDescriptor176: "uma_TaskDescriptor" = None, WorkProductDescriptor164: "uma_RoleDescriptor" = None, WorkProductDescriptor180: "uma_TaskDescriptor" = None, uma_WorkProductDescriptor: "uma_WorkProduct" = None, WorkProductDescriptor178: "uma_TaskDescriptor" = None, impactedBy: set["uma_WorkProductDescriptor"] = None, mandatoryInput: set["uma_TaskDescriptor"] = None, modifies: set["uma_RoleDescriptor"] = None, optionalInput: set["uma_TaskDescriptor"] = None, output: set["uma_TaskDescriptor"] = None, uma_WorkProductDescriptor206: "uma_WorkProductDescriptor" = None, uma_WorkProductDescriptor204: set["uma_WorkProductDescriptor"] = None, responsibleFor: "uma_RoleDescriptor" = None, externalInput: set["uma_TaskDescriptor"] = None, WorkProductDescriptor192: "uma_WorkProductDescriptor" = None, impacts: set["uma_WorkProductDescriptor"] = None, WorkProductDescriptor195: "uma_WorkProductDescriptor" = None, uma_WorkProductDescriptor273: "uma_ProcessComponentInterface" = None):
        self.activityEntryState = activityEntryState
        self.activityExitState = activityExitState
        self.WorkProductDescriptor = WorkProductDescriptor
        self.WorkProductDescriptor174 = WorkProductDescriptor174
        self.WorkProductDescriptor176 = WorkProductDescriptor176
        self.WorkProductDescriptor164 = WorkProductDescriptor164
        self.WorkProductDescriptor180 = WorkProductDescriptor180
        self.uma_WorkProductDescriptor = uma_WorkProductDescriptor
        self.WorkProductDescriptor178 = WorkProductDescriptor178
        self.impactedBy = impactedBy if impactedBy is not None else set()
        self.mandatoryInput = mandatoryInput if mandatoryInput is not None else set()
        self.modifies = modifies if modifies is not None else set()
        self.optionalInput = optionalInput if optionalInput is not None else set()
        self.output = output if output is not None else set()
        self.uma_WorkProductDescriptor206 = uma_WorkProductDescriptor206
        self.uma_WorkProductDescriptor204 = uma_WorkProductDescriptor204 if uma_WorkProductDescriptor204 is not None else set()
        self.responsibleFor = responsibleFor
        self.externalInput = externalInput if externalInput is not None else set()
        self.WorkProductDescriptor192 = WorkProductDescriptor192
        self.impacts = impacts if impacts is not None else set()
        self.WorkProductDescriptor195 = WorkProductDescriptor195
        self.uma_WorkProductDescriptor273 = uma_WorkProductDescriptor273
        
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
    def externalInput(self):
        return self.__externalInput

    @externalInput.setter
    def externalInput(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_WorkProductDescriptor__externalInput", None)
        self.__externalInput = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TaskDescriptor189"):
                    opp_val = getattr(item, "TaskDescriptor189", None)
                    
                    if opp_val == self:
                        setattr(item, "TaskDescriptor189", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TaskDescriptor189"):
                    opp_val = getattr(item, "TaskDescriptor189", None)
                    
                    setattr(item, "TaskDescriptor189", self)
                    

    @property
    def WorkProductDescriptor180(self):
        return self.__WorkProductDescriptor180

    @WorkProductDescriptor180.setter
    def WorkProductDescriptor180(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_WorkProductDescriptor__WorkProductDescriptor180", None)
        self.__WorkProductDescriptor180 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outputFrom"):
                opp_val = getattr(old_value, "outputFrom", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outputFrom"):
                opp_val = getattr(value, "outputFrom", None)
                if opp_val is None:
                    setattr(value, "outputFrom", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def WorkProductDescriptor192(self):
        return self.__WorkProductDescriptor192

    @WorkProductDescriptor192.setter
    def WorkProductDescriptor192(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_WorkProductDescriptor__WorkProductDescriptor192", None)
        self.__WorkProductDescriptor192 = value
        
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
    def WorkProductDescriptor164(self):
        return self.__WorkProductDescriptor164

    @WorkProductDescriptor164.setter
    def WorkProductDescriptor164(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_WorkProductDescriptor__WorkProductDescriptor164", None)
        self.__WorkProductDescriptor164 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "responsibleRole"):
                opp_val = getattr(old_value, "responsibleRole", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "responsibleRole"):
                opp_val = getattr(value, "responsibleRole", None)
                if opp_val is None:
                    setattr(value, "responsibleRole", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mandatoryInput(self):
        return self.__mandatoryInput

    @mandatoryInput.setter
    def mandatoryInput(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_WorkProductDescriptor__mandatoryInput", None)
        self.__mandatoryInput = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TaskDescriptor197"):
                    opp_val = getattr(item, "TaskDescriptor197", None)
                    
                    if opp_val == self:
                        setattr(item, "TaskDescriptor197", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TaskDescriptor197"):
                    opp_val = getattr(item, "TaskDescriptor197", None)
                    
                    setattr(item, "TaskDescriptor197", self)
                    

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
            if hasattr(old_value, "uma_WorkProduct187"):
                opp_val = getattr(old_value, "uma_WorkProduct187", None)
                if opp_val == self:
                    setattr(old_value, "uma_WorkProduct187", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_WorkProduct187"):
                opp_val = getattr(value, "uma_WorkProduct187", None)
                setattr(value, "uma_WorkProduct187", self)

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
            if hasattr(old_value, "externalInputTo"):
                opp_val = getattr(old_value, "externalInputTo", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "externalInputTo"):
                opp_val = getattr(value, "externalInputTo", None)
                if opp_val is None:
                    setattr(value, "externalInputTo", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def output(self):
        return self.__output

    @output.setter
    def output(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_WorkProductDescriptor__output", None)
        self.__output = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TaskDescriptor203"):
                    opp_val = getattr(item, "TaskDescriptor203", None)
                    
                    if opp_val == self:
                        setattr(item, "TaskDescriptor203", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TaskDescriptor203"):
                    opp_val = getattr(item, "TaskDescriptor203", None)
                    
                    setattr(item, "TaskDescriptor203", self)
                    

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
            if hasattr(old_value, "workedOnBy"):
                opp_val = getattr(old_value, "workedOnBy", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "workedOnBy"):
                opp_val = getattr(value, "workedOnBy", None)
                if opp_val is None:
                    setattr(value, "workedOnBy", set([self]))
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
                if hasattr(item, "WorkProductDescriptor192"):
                    opp_val = getattr(item, "WorkProductDescriptor192", None)
                    
                    if opp_val == self:
                        setattr(item, "WorkProductDescriptor192", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "WorkProductDescriptor192"):
                    opp_val = getattr(item, "WorkProductDescriptor192", None)
                    
                    setattr(item, "WorkProductDescriptor192", self)
                    

    @property
    def uma_WorkProductDescriptor273(self):
        return self.__uma_WorkProductDescriptor273

    @uma_WorkProductDescriptor273.setter
    def uma_WorkProductDescriptor273(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_WorkProductDescriptor__uma_WorkProductDescriptor273", None)
        self.__uma_WorkProductDescriptor273 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_ProcessComponentInterface272"):
                opp_val = getattr(old_value, "uma_ProcessComponentInterface272", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_ProcessComponentInterface272"):
                opp_val = getattr(value, "uma_ProcessComponentInterface272", None)
                if opp_val is None:
                    setattr(value, "uma_ProcessComponentInterface272", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def WorkProductDescriptor195(self):
        return self.__WorkProductDescriptor195

    @WorkProductDescriptor195.setter
    def WorkProductDescriptor195(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_WorkProductDescriptor__WorkProductDescriptor195", None)
        self.__WorkProductDescriptor195 = value
        
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
    def uma_WorkProductDescriptor206(self):
        return self.__uma_WorkProductDescriptor206

    @uma_WorkProductDescriptor206.setter
    def uma_WorkProductDescriptor206(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_WorkProductDescriptor__uma_WorkProductDescriptor206", None)
        self.__uma_WorkProductDescriptor206 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_WorkProductDescriptor204"):
                opp_val = getattr(old_value, "uma_WorkProductDescriptor204", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_WorkProductDescriptor204"):
                opp_val = getattr(value, "uma_WorkProductDescriptor204", None)
                if opp_val is None:
                    setattr(value, "uma_WorkProductDescriptor204", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def WorkProductDescriptor178(self):
        return self.__WorkProductDescriptor178

    @WorkProductDescriptor178.setter
    def WorkProductDescriptor178(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_WorkProductDescriptor__WorkProductDescriptor178", None)
        self.__WorkProductDescriptor178 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OptionalInputTo"):
                opp_val = getattr(old_value, "OptionalInputTo", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OptionalInputTo"):
                opp_val = getattr(value, "OptionalInputTo", None)
                if opp_val is None:
                    setattr(value, "OptionalInputTo", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uma_WorkProductDescriptor204(self):
        return self.__uma_WorkProductDescriptor204

    @uma_WorkProductDescriptor204.setter
    def uma_WorkProductDescriptor204(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_WorkProductDescriptor__uma_WorkProductDescriptor204", None)
        self.__uma_WorkProductDescriptor204 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uma_WorkProductDescriptor206"):
                    opp_val = getattr(item, "uma_WorkProductDescriptor206", None)
                    
                    if opp_val == self:
                        setattr(item, "uma_WorkProductDescriptor206", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uma_WorkProductDescriptor206"):
                    opp_val = getattr(item, "uma_WorkProductDescriptor206", None)
                    
                    setattr(item, "uma_WorkProductDescriptor206", self)
                    

    @property
    def modifies(self):
        return self.__modifies

    @modifies.setter
    def modifies(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_WorkProductDescriptor__modifies", None)
        self.__modifies = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RoleDescriptor199"):
                    opp_val = getattr(item, "RoleDescriptor199", None)
                    
                    if opp_val == self:
                        setattr(item, "RoleDescriptor199", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RoleDescriptor199"):
                    opp_val = getattr(item, "RoleDescriptor199", None)
                    
                    setattr(item, "RoleDescriptor199", self)
                    

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
                if hasattr(item, "WorkProductDescriptor195"):
                    opp_val = getattr(item, "WorkProductDescriptor195", None)
                    
                    if opp_val == self:
                        setattr(item, "WorkProductDescriptor195", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "WorkProductDescriptor195"):
                    opp_val = getattr(item, "WorkProductDescriptor195", None)
                    
                    setattr(item, "WorkProductDescriptor195", self)
                    

    @property
    def responsibleFor(self):
        return self.__responsibleFor

    @responsibleFor.setter
    def responsibleFor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_WorkProductDescriptor__responsibleFor", None)
        self.__responsibleFor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RoleDescriptor208"):
                opp_val = getattr(old_value, "RoleDescriptor208", None)
                if opp_val == self:
                    setattr(old_value, "RoleDescriptor208", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RoleDescriptor208"):
                opp_val = getattr(value, "RoleDescriptor208", None)
                setattr(value, "RoleDescriptor208", self)

    @property
    def optionalInput(self):
        return self.__optionalInput

    @optionalInput.setter
    def optionalInput(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_WorkProductDescriptor__optionalInput", None)
        self.__optionalInput = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TaskDescriptor201"):
                    opp_val = getattr(item, "TaskDescriptor201", None)
                    
                    if opp_val == self:
                        setattr(item, "TaskDescriptor201", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TaskDescriptor201"):
                    opp_val = getattr(item, "TaskDescriptor201", None)
                    
                    setattr(item, "TaskDescriptor201", self)
                    

    @property
    def WorkProductDescriptor176(self):
        return self.__WorkProductDescriptor176

    @WorkProductDescriptor176.setter
    def WorkProductDescriptor176(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_WorkProductDescriptor__WorkProductDescriptor176", None)
        self.__WorkProductDescriptor176 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mandatoryInputTo"):
                opp_val = getattr(old_value, "mandatoryInputTo", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mandatoryInputTo"):
                opp_val = getattr(value, "mandatoryInputTo", None)
                if opp_val is None:
                    setattr(value, "mandatoryInputTo", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "uma_BreakdownElement146"):
                opp_val = getattr(old_value, "uma_BreakdownElement146", None)
                if opp_val == self:
                    setattr(old_value, "uma_BreakdownElement146", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_BreakdownElement146"):
                opp_val = getattr(value, "uma_BreakdownElement146", None)
                setattr(value, "uma_BreakdownElement146", self)

class uma_WorkOrder(ProcessElement):

    def __init__(self, linkType: str, uma_WorkOrder: "uma_WorkBreakdownElement" = None, uma_WorkOrder166: "uma_WorkBreakdownElement" = None):
        self.linkType = linkType
        self.uma_WorkOrder = uma_WorkOrder
        self.uma_WorkOrder166 = uma_WorkOrder166
        
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
    def uma_WorkOrder166(self):
        return self.__uma_WorkOrder166

    @uma_WorkOrder166.setter
    def uma_WorkOrder166(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_WorkOrder__uma_WorkOrder166", None)
        self.__uma_WorkOrder166 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_WorkBreakdownElement167"):
                opp_val = getattr(old_value, "uma_WorkBreakdownElement167", None)
                if opp_val == self:
                    setattr(old_value, "uma_WorkBreakdownElement167", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_WorkBreakdownElement167"):
                opp_val = getattr(value, "uma_WorkBreakdownElement167", None)
                setattr(value, "uma_WorkBreakdownElement167", self)

class BreakdownElement:

    pass
class uma_ProcessComponentInterface(BreakdownElement):

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

class uma_TeamProfile(BreakdownElement):

    pass
class uma_WorkBreakdownElement(BreakdownElement):

    def __init__(self, isRepeatable: str, isOngoing: str, isEventDriven: str, uma_WorkBreakdownElement: set["uma_WorkOrder"] = None, uma_WorkBreakdownElement167: "uma_WorkOrder" = None):
        self.isRepeatable = isRepeatable
        self.isOngoing = isOngoing
        self.isEventDriven = isEventDriven
        self.uma_WorkBreakdownElement = uma_WorkBreakdownElement if uma_WorkBreakdownElement is not None else set()
        self.uma_WorkBreakdownElement167 = uma_WorkBreakdownElement167
        
    @property
    def isOngoing(self) -> str:
        return self.__isOngoing

    @isOngoing.setter
    def isOngoing(self, isOngoing: str):
        self.__isOngoing = isOngoing

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
    def uma_WorkBreakdownElement167(self):
        return self.__uma_WorkBreakdownElement167

    @uma_WorkBreakdownElement167.setter
    def uma_WorkBreakdownElement167(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_WorkBreakdownElement__uma_WorkBreakdownElement167", None)
        self.__uma_WorkBreakdownElement167 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_WorkOrder166"):
                opp_val = getattr(old_value, "uma_WorkOrder166", None)
                if opp_val == self:
                    setattr(old_value, "uma_WorkOrder166", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_WorkOrder166"):
                opp_val = getattr(value, "uma_WorkOrder166", None)
                setattr(value, "uma_WorkOrder166", self)

class uma_Roadmap(Guidance):

    pass
class uma_BreakdownElement(ProcessElement):

    def __init__(self, prefix: str, isPlanned: str, hasMultipleOccurrences: str, isOptional: str, BreakdownElement: "uma_Activity" = None, uma_BreakdownElement: "uma_BreakdownElement" = None, uma_BreakdownElement140: "uma_BreakdownElement" = None, uma_BreakdownElement144: "uma_BreakdownElement" = None, uma_BreakdownElement142: "uma_BreakdownElement" = None, uma_BreakdownElement146: "uma_PlanningData" = None, breakdownElements: set["uma_Activity"] = None):
        self.prefix = prefix
        self.isPlanned = isPlanned
        self.hasMultipleOccurrences = hasMultipleOccurrences
        self.isOptional = isOptional
        self.BreakdownElement = BreakdownElement
        self.uma_BreakdownElement = uma_BreakdownElement
        self.uma_BreakdownElement140 = uma_BreakdownElement140
        self.uma_BreakdownElement144 = uma_BreakdownElement144
        self.uma_BreakdownElement142 = uma_BreakdownElement142
        self.uma_BreakdownElement146 = uma_BreakdownElement146
        self.breakdownElements = breakdownElements if breakdownElements is not None else set()
        
    @property
    def prefix(self) -> str:
        return self.__prefix

    @prefix.setter
    def prefix(self, prefix: str):
        self.__prefix = prefix

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
    def isOptional(self) -> str:
        return self.__isOptional

    @isOptional.setter
    def isOptional(self, isOptional: str):
        self.__isOptional = isOptional

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
            if hasattr(old_value, "uma_BreakdownElement144"):
                opp_val = getattr(old_value, "uma_BreakdownElement144", None)
                if opp_val == self:
                    setattr(old_value, "uma_BreakdownElement144", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_BreakdownElement144"):
                opp_val = getattr(value, "uma_BreakdownElement144", None)
                setattr(value, "uma_BreakdownElement144", self)

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
    def uma_BreakdownElement144(self):
        return self.__uma_BreakdownElement144

    @uma_BreakdownElement144.setter
    def uma_BreakdownElement144(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_BreakdownElement__uma_BreakdownElement144", None)
        self.__uma_BreakdownElement144 = value
        
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
    def uma_BreakdownElement140(self):
        return self.__uma_BreakdownElement140

    @uma_BreakdownElement140.setter
    def uma_BreakdownElement140(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_BreakdownElement__uma_BreakdownElement140", None)
        self.__uma_BreakdownElement140 = value
        
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
        self.__breakdownElements = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Activity"):
                    opp_val = getattr(item, "Activity", None)
                    
                    if opp_val == self:
                        setattr(item, "Activity", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Activity"):
                    opp_val = getattr(item, "Activity", None)
                    
                    setattr(item, "Activity", self)
                    

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
class uma_Milestone(WorkBreakdownElement):

    pass
class uma_TaskDescriptor(WorkBreakdownElement, Descriptor):

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
    def uma_Ellipse(self):
        return self.__uma_Ellipse

    @uma_Ellipse.setter
    def uma_Ellipse(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Ellipse__uma_Ellipse", None)
        self.__uma_Ellipse = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_Point118"):
                opp_val = getattr(old_value, "uma_Point118", None)
                if opp_val == self:
                    setattr(old_value, "uma_Point118", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_Point118"):
                opp_val = getattr(value, "uma_Point118", None)
                setattr(value, "uma_Point118", self)

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
                if hasattr(item, "uma_Point116"):
                    opp_val = getattr(item, "uma_Point116", None)
                    
                    if opp_val == self:
                        setattr(item, "uma_Point116", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uma_Point116"):
                    opp_val = getattr(item, "uma_Point116", None)
                    
                    setattr(item, "uma_Point116", self)
                    

class LeafElement:

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

class GraphNode:

    pass
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

class GraphElement:

    pass
class uma_GraphConnector(GraphElement):

    pass
class uma_GraphNode(GraphElement):

    pass
class uma_GraphEdge(GraphElement):

    pass
class uma_Diagram(GraphNode):

    def __init__(self, zoom: str, Diagram: "uma_DiagramLink" = None, Diagram97: "uma_SemanticModelBridge" = None, uma_Diagram: "uma_Point" = None, diagram: set["uma_DiagramLink"] = None, diagram109: "uma_SemanticModelBridge" = None, uma_Diagram267: "uma_ProcessPackage" = None):
        self.zoom = zoom
        self.Diagram = Diagram
        self.Diagram97 = Diagram97
        self.uma_Diagram = uma_Diagram
        self.diagram = diagram if diagram is not None else set()
        self.diagram109 = diagram109
        self.uma_Diagram267 = uma_Diagram267
        
    @property
    def zoom(self) -> str:
        return self.__zoom

    @zoom.setter
    def zoom(self, zoom: str):
        self.__zoom = zoom

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
                if hasattr(item, "DiagramLink107"):
                    opp_val = getattr(item, "DiagramLink107", None)
                    
                    if opp_val == self:
                        setattr(item, "DiagramLink107", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DiagramLink107"):
                    opp_val = getattr(item, "DiagramLink107", None)
                    
                    setattr(item, "DiagramLink107", self)
                    

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
            if hasattr(old_value, "uma_Point105"):
                opp_val = getattr(old_value, "uma_Point105", None)
                if opp_val == self:
                    setattr(old_value, "uma_Point105", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_Point105"):
                opp_val = getattr(value, "uma_Point105", None)
                setattr(value, "uma_Point105", self)

    @property
    def diagram109(self):
        return self.__diagram109

    @diagram109.setter
    def diagram109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Diagram__diagram109", None)
        self.__diagram109 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SemanticModelBridge110"):
                opp_val = getattr(old_value, "SemanticModelBridge110", None)
                if opp_val == self:
                    setattr(old_value, "SemanticModelBridge110", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SemanticModelBridge110"):
                opp_val = getattr(value, "SemanticModelBridge110", None)
                setattr(value, "SemanticModelBridge110", self)

    @property
    def uma_Diagram267(self):
        return self.__uma_Diagram267

    @uma_Diagram267.setter
    def uma_Diagram267(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Diagram__uma_Diagram267", None)
        self.__uma_Diagram267 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_ProcessPackage266"):
                opp_val = getattr(old_value, "uma_ProcessPackage266", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_ProcessPackage266"):
                opp_val = getattr(value, "uma_ProcessPackage266", None)
                if opp_val is None:
                    setattr(value, "uma_ProcessPackage266", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Diagram97(self):
        return self.__Diagram97

    @Diagram97.setter
    def Diagram97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Diagram__Diagram97", None)
        self.__Diagram97 = value
        
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

class DiagramElement:

    pass
class uma_DiagramLink(DiagramElement):

    def __init__(self, zoom: str, DiagramLink: "uma_GraphElement" = None, uma_DiagramLink: "uma_Point" = None, link: "uma_GraphElement" = None, diagramLink: "uma_Diagram" = None, DiagramLink107: "uma_Diagram" = None):
        self.zoom = zoom
        self.DiagramLink = DiagramLink
        self.uma_DiagramLink = uma_DiagramLink
        self.link = link
        self.diagramLink = diagramLink
        self.DiagramLink107 = DiagramLink107
        
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
            if hasattr(old_value, "GraphElement89"):
                opp_val = getattr(old_value, "GraphElement89", None)
                if opp_val == self:
                    setattr(old_value, "GraphElement89", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GraphElement89"):
                opp_val = getattr(value, "GraphElement89", None)
                setattr(value, "GraphElement89", self)

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
    def DiagramLink107(self):
        return self.__DiagramLink107

    @DiagramLink107.setter
    def DiagramLink107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_DiagramLink__DiagramLink107", None)
        self.__DiagramLink107 = value
        
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
            if hasattr(old_value, "uma_Point87"):
                opp_val = getattr(old_value, "uma_Point87", None)
                if opp_val == self:
                    setattr(old_value, "uma_Point87", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_Point87"):
                opp_val = getattr(value, "uma_Point87", None)
                setattr(value, "uma_Point87", self)

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
            if hasattr(old_value, "DiagramElement99"):
                opp_val = getattr(old_value, "DiagramElement99", None)
                if opp_val == self:
                    setattr(old_value, "DiagramElement99", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DiagramElement99"):
                opp_val = getattr(value, "DiagramElement99", None)
                setattr(value, "DiagramElement99", self)

class uma_LeafElement(DiagramElement):

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

class uma_SemanticModelBridge(DiagramElement):

    def __init__(self, presentation: str, semanticModel: "uma_GraphElement" = None, namespace: "uma_Diagram" = None, SemanticModelBridge: "uma_GraphElement" = None, SemanticModelBridge110: "uma_Diagram" = None):
        self.presentation = presentation
        self.semanticModel = semanticModel
        self.namespace = namespace
        self.SemanticModelBridge = SemanticModelBridge
        self.SemanticModelBridge110 = SemanticModelBridge110
        
    @property
    def presentation(self) -> str:
        return self.__presentation

    @presentation.setter
    def presentation(self, presentation: str):
        self.__presentation = presentation

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
            if hasattr(old_value, "GraphElement95"):
                opp_val = getattr(old_value, "GraphElement95", None)
                if opp_val == self:
                    setattr(old_value, "GraphElement95", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GraphElement95"):
                opp_val = getattr(value, "GraphElement95", None)
                setattr(value, "GraphElement95", self)

    @property
    def SemanticModelBridge110(self):
        return self.__SemanticModelBridge110

    @SemanticModelBridge110.setter
    def SemanticModelBridge110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_SemanticModelBridge__SemanticModelBridge110", None)
        self.__SemanticModelBridge110 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diagram109"):
                opp_val = getattr(old_value, "diagram109", None)
                if opp_val == self:
                    setattr(old_value, "diagram109", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagram109"):
                opp_val = getattr(value, "diagram109", None)
                setattr(value, "diagram109", self)

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
            if hasattr(old_value, "graphElement82"):
                opp_val = getattr(old_value, "graphElement82", None)
                if opp_val == self:
                    setattr(old_value, "graphElement82", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphElement82"):
                opp_val = getattr(value, "graphElement82", None)
                setattr(value, "graphElement82", self)

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
            if hasattr(old_value, "Diagram97"):
                opp_val = getattr(old_value, "Diagram97", None)
                if opp_val == self:
                    setattr(old_value, "Diagram97", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Diagram97"):
                opp_val = getattr(value, "Diagram97", None)
                setattr(value, "Diagram97", self)

class uma_GraphElement(DiagramElement):

    pass
class uma_Point:

    def __init__(self, x: str, y: str, uma_Point: "uma_GraphElement" = None, uma_Point87: "uma_DiagramLink" = None, uma_Point103: "uma_GraphEdge" = None, uma_Point105: "uma_Diagram" = None, uma_Point118: "uma_Ellipse" = None, uma_Point116: "uma_Polyline" = None):
        self.x = x
        self.y = y
        self.uma_Point = uma_Point
        self.uma_Point87 = uma_Point87
        self.uma_Point103 = uma_Point103
        self.uma_Point105 = uma_Point105
        self.uma_Point118 = uma_Point118
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
    def uma_Point105(self):
        return self.__uma_Point105

    @uma_Point105.setter
    def uma_Point105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Point__uma_Point105", None)
        self.__uma_Point105 = value
        
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
    def uma_Point118(self):
        return self.__uma_Point118

    @uma_Point118.setter
    def uma_Point118(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Point__uma_Point118", None)
        self.__uma_Point118 = value
        
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
    def uma_Point116(self):
        return self.__uma_Point116

    @uma_Point116.setter
    def uma_Point116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Point__uma_Point116", None)
        self.__uma_Point116 = value
        
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
    def uma_Point103(self):
        return self.__uma_Point103

    @uma_Point103.setter
    def uma_Point103(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Point__uma_Point103", None)
        self.__uma_Point103 = value
        
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
    def uma_Point87(self):
        return self.__uma_Point87

    @uma_Point87.setter
    def uma_Point87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Point__uma_Point87", None)
        self.__uma_Point87 = value
        
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

class ContentDescription:

    pass
class uma_PracticeDescription(ContentDescription):

    def __init__(self, additionalInfo: str, problem: str, background: str, goals: str, application: str, levelsOfAdoption: str):
        self.additionalInfo = additionalInfo
        self.problem = problem
        self.background = background
        self.goals = goals
        self.application = application
        self.levelsOfAdoption = levelsOfAdoption
        
    @property
    def goals(self) -> str:
        return self.__goals

    @goals.setter
    def goals(self, goals: str):
        self.__goals = goals

    @property
    def background(self) -> str:
        return self.__background

    @background.setter
    def background(self, background: str):
        self.__background = background

    @property
    def application(self) -> str:
        return self.__application

    @application.setter
    def application(self, application: str):
        self.__application = application

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

class uma_BreakdownElementDescription(ContentDescription):

    def __init__(self, usageGuidance: str):
        self.usageGuidance = usageGuidance
        
    @property
    def usageGuidance(self) -> str:
        return self.__usageGuidance

    @usageGuidance.setter
    def usageGuidance(self, usageGuidance: str):
        self.__usageGuidance = usageGuidance

class uma_RoleDescription(ContentDescription):

    def __init__(self, assignmentApproaches: str, synonyms: str, skills: str):
        self.assignmentApproaches = assignmentApproaches
        self.synonyms = synonyms
        self.skills = skills
        
    @property
    def skills(self) -> str:
        return self.__skills

    @skills.setter
    def skills(self, skills: str):
        self.__skills = skills

    @property
    def synonyms(self) -> str:
        return self.__synonyms

    @synonyms.setter
    def synonyms(self, synonyms: str):
        self.__synonyms = synonyms

    @property
    def assignmentApproaches(self) -> str:
        return self.__assignmentApproaches

    @assignmentApproaches.setter
    def assignmentApproaches(self, assignmentApproaches: str):
        self.__assignmentApproaches = assignmentApproaches

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

class uma_GuidanceDescription(ContentDescription):

    def __init__(self, attachments: str):
        self.attachments = attachments
        
    @property
    def attachments(self) -> str:
        return self.__attachments

    @attachments.setter
    def attachments(self, attachments: str):
        self.__attachments = attachments

class uma_WorkProductDescription(ContentDescription):

    def __init__(self, externalId: str, purpose: str, impactOfNotHaving: str, reasonsForNotNeeding: str):
        self.externalId = externalId
        self.purpose = purpose
        self.impactOfNotHaving = impactOfNotHaving
        self.reasonsForNotNeeding = reasonsForNotNeeding
        
    @property
    def impactOfNotHaving(self) -> str:
        return self.__impactOfNotHaving

    @impactOfNotHaving.setter
    def impactOfNotHaving(self, impactOfNotHaving: str):
        self.__impactOfNotHaving = impactOfNotHaving

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
    def externalId(self) -> str:
        return self.__externalId

    @externalId.setter
    def externalId(self, externalId: str):
        self.__externalId = externalId

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
class Package:

    pass
class uma_ToolMentor(Guidance):

    pass
class uma_Template(Guidance):

    pass
class WorkProduct:

    pass
class uma_Outcome(WorkProduct):

    pass
class uma_Deliverable(WorkProduct):

    pass
class uma_Artifact(WorkProduct):

    pass
class Section:

    pass
class WorkDefinition:

    pass
class uma_Step(WorkDefinition, Section):

    pass
class uma_Report(Guidance):

    pass
class uma_Estimate(Guidance):

    pass
class ContentElement:

    pass
class uma_WorkProduct(ContentElement):

    pass
class uma_Task(ContentElement, WorkDefinition):

    pass
class uma_Guidance(ContentElement):

    pass
class uma_ContentCategory(ContentElement):

    pass
class uma_Role(ContentElement):

    pass
class MethodUnit:

    pass
class uma_MethodPlugin(MethodUnit, Package):

    def __init__(self, userChangeable: str, uma_MethodPlugin: set["uma_MethodPackage"] = None, uma_MethodPlugin280: "uma_MethodPlugin" = None, uma_MethodPlugin278: set["uma_MethodPlugin"] = None, uma_MethodPlugin289: "uma_MethodConfiguration" = None, uma_MethodPlugin305: "uma_MethodLibrary" = None):
        self.userChangeable = userChangeable
        self.uma_MethodPlugin = uma_MethodPlugin if uma_MethodPlugin is not None else set()
        self.uma_MethodPlugin280 = uma_MethodPlugin280
        self.uma_MethodPlugin278 = uma_MethodPlugin278 if uma_MethodPlugin278 is not None else set()
        self.uma_MethodPlugin289 = uma_MethodPlugin289
        self.uma_MethodPlugin305 = uma_MethodPlugin305
        
    @property
    def userChangeable(self) -> str:
        return self.__userChangeable

    @userChangeable.setter
    def userChangeable(self, userChangeable: str):
        self.__userChangeable = userChangeable

    @property
    def uma_MethodPlugin289(self):
        return self.__uma_MethodPlugin289

    @uma_MethodPlugin289.setter
    def uma_MethodPlugin289(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_MethodPlugin__uma_MethodPlugin289", None)
        self.__uma_MethodPlugin289 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_MethodConfiguration288"):
                opp_val = getattr(old_value, "uma_MethodConfiguration288", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_MethodConfiguration288"):
                opp_val = getattr(value, "uma_MethodConfiguration288", None)
                if opp_val is None:
                    setattr(value, "uma_MethodConfiguration288", set([self]))
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
                if hasattr(item, "uma_MethodPackage277"):
                    opp_val = getattr(item, "uma_MethodPackage277", None)
                    
                    if opp_val == self:
                        setattr(item, "uma_MethodPackage277", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uma_MethodPackage277"):
                    opp_val = getattr(item, "uma_MethodPackage277", None)
                    
                    setattr(item, "uma_MethodPackage277", self)
                    

    @property
    def uma_MethodPlugin305(self):
        return self.__uma_MethodPlugin305

    @uma_MethodPlugin305.setter
    def uma_MethodPlugin305(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_MethodPlugin__uma_MethodPlugin305", None)
        self.__uma_MethodPlugin305 = value
        
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
    def uma_MethodPlugin280(self):
        return self.__uma_MethodPlugin280

    @uma_MethodPlugin280.setter
    def uma_MethodPlugin280(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_MethodPlugin__uma_MethodPlugin280", None)
        self.__uma_MethodPlugin280 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_MethodPlugin278"):
                opp_val = getattr(old_value, "uma_MethodPlugin278", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_MethodPlugin278"):
                opp_val = getattr(value, "uma_MethodPlugin278", None)
                if opp_val is None:
                    setattr(value, "uma_MethodPlugin278", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uma_MethodPlugin278(self):
        return self.__uma_MethodPlugin278

    @uma_MethodPlugin278.setter
    def uma_MethodPlugin278(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_MethodPlugin__uma_MethodPlugin278", None)
        self.__uma_MethodPlugin278 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uma_MethodPlugin280"):
                    opp_val = getattr(item, "uma_MethodPlugin280", None)
                    
                    if opp_val == self:
                        setattr(item, "uma_MethodPlugin280", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uma_MethodPlugin280"):
                    opp_val = getattr(item, "uma_MethodPlugin280", None)
                    
                    setattr(item, "uma_MethodPlugin280", self)
                    

class uma_MethodLibrary(MethodUnit, Package):

    pass
class uma_ContentDescription(MethodUnit):

    def __init__(self, mainDescription: str, keyConsiderations: str, uma_ContentDescription14: set["uma_Section"] = None, uma_ContentDescription: "uma_DescribableElement" = None):
        self.mainDescription = mainDescription
        self.keyConsiderations = keyConsiderations
        self.uma_ContentDescription14 = uma_ContentDescription14 if uma_ContentDescription14 is not None else set()
        self.uma_ContentDescription = uma_ContentDescription
        
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

class uma_ProcessComponent(MethodUnit, ProcessPackage):

    pass
class Classifier:

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
class uma_Activity(WorkBreakdownElement, VariabilityElement, WorkDefinition):

    pass
class uma_Section(VariabilityElement):

    def __init__(self, sectionName: str, sectionDescription: str, uma_Section: "uma_ContentDescription" = None, uma_Section17: "uma_Section" = None, uma_Section15: set["uma_Section"] = None, uma_Section20: "uma_Section" = None, uma_Section18: "uma_Section" = None, uma_Section185: "uma_TaskDescriptor" = None):
        self.sectionName = sectionName
        self.sectionDescription = sectionDescription
        self.uma_Section = uma_Section
        self.uma_Section17 = uma_Section17
        self.uma_Section15 = uma_Section15 if uma_Section15 is not None else set()
        self.uma_Section20 = uma_Section20
        self.uma_Section18 = uma_Section18
        self.uma_Section185 = uma_Section185
        
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
    def uma_Section185(self):
        return self.__uma_Section185

    @uma_Section185.setter
    def uma_Section185(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Section__uma_Section185", None)
        self.__uma_Section185 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_TaskDescriptor184"):
                opp_val = getattr(old_value, "uma_TaskDescriptor184", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_TaskDescriptor184"):
                opp_val = getattr(value, "uma_TaskDescriptor184", None)
                if opp_val is None:
                    setattr(value, "uma_TaskDescriptor184", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
                    

class DescribableElement:

    pass
class uma_ProcessElement(DescribableElement):

    pass
class uma_ContentElement(VariabilityElement, DescribableElement):

    pass
class MethodElement:

    pass
class uma_MethodUnit(MethodElement):

    def __init__(self, changeDescription: str, version: str, authors: str, changeDate: str, uma_MethodUnit: "uma_SupportingMaterial" = None):
        self.changeDescription = changeDescription
        self.version = version
        self.authors = authors
        self.changeDate = changeDate
        self.uma_MethodUnit = uma_MethodUnit
        
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
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

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
            if hasattr(old_value, "uma_SupportingMaterial286"):
                opp_val = getattr(old_value, "uma_SupportingMaterial286", None)
                if opp_val == self:
                    setattr(old_value, "uma_SupportingMaterial286", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_SupportingMaterial286"):
                opp_val = getattr(value, "uma_SupportingMaterial286", None)
                setattr(value, "uma_SupportingMaterial286", self)

class uma_DiagramElement(MethodElement):

    def __init__(self, isVisible: str, DiagramElement: "uma_GraphElement" = None, contained: "uma_GraphElement" = None, referenced: set["uma_Reference"] = None, uma_DiagramElement: set["uma_Property"] = None, DiagramElement99: "uma_Reference" = None):
        self.isVisible = isVisible
        self.DiagramElement = DiagramElement
        self.contained = contained
        self.referenced = referenced if referenced is not None else set()
        self.uma_DiagramElement = uma_DiagramElement if uma_DiagramElement is not None else set()
        self.DiagramElement99 = DiagramElement99
        
    @property
    def isVisible(self) -> str:
        return self.__isVisible

    @isVisible.setter
    def isVisible(self, isVisible: str):
        self.__isVisible = isVisible

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
    def DiagramElement99(self):
        return self.__DiagramElement99

    @DiagramElement99.setter
    def DiagramElement99(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_DiagramElement__DiagramElement99", None)
        self.__DiagramElement99 = value
        
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
class uma_DescribableElement(MethodElement, Classifier):

    def __init__(self, shapeicon: str, nodeicon: str, presentationName: str, uma_DescribableElement: "uma_ContentDescription" = None, uma_DescribableElement244: "uma_CustomCategory" = None):
        self.shapeicon = shapeicon
        self.nodeicon = nodeicon
        self.presentationName = presentationName
        self.uma_DescribableElement = uma_DescribableElement
        self.uma_DescribableElement244 = uma_DescribableElement244
        
    @property
    def nodeicon(self) -> str:
        return self.__nodeicon

    @nodeicon.setter
    def nodeicon(self, nodeicon: str):
        self.__nodeicon = nodeicon

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
    def uma_DescribableElement244(self):
        return self.__uma_DescribableElement244

    @uma_DescribableElement244.setter
    def uma_DescribableElement244(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_DescribableElement__uma_DescribableElement244", None)
        self.__uma_DescribableElement244 = value
        
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

class uma_VariabilityElement(MethodElement):

    def __init__(self, variabilityType: str, uma_VariabilityElement: "uma_VariabilityElement" = None, uma_VariabilityElement281: "uma_VariabilityElement" = None):
        self.variabilityType = variabilityType
        self.uma_VariabilityElement = uma_VariabilityElement
        self.uma_VariabilityElement281 = uma_VariabilityElement281
        
    @property
    def variabilityType(self) -> str:
        return self.__variabilityType

    @variabilityType.setter
    def variabilityType(self, variabilityType: str):
        self.__variabilityType = variabilityType

    @property
    def uma_VariabilityElement281(self):
        return self.__uma_VariabilityElement281

    @uma_VariabilityElement281.setter
    def uma_VariabilityElement281(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_VariabilityElement__uma_VariabilityElement281", None)
        self.__uma_VariabilityElement281 = value
        
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
            if hasattr(old_value, "uma_VariabilityElement281"):
                opp_val = getattr(old_value, "uma_VariabilityElement281", None)
                if opp_val == self:
                    setattr(old_value, "uma_VariabilityElement281", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_VariabilityElement281"):
                opp_val = getattr(value, "uma_VariabilityElement281", None)
                setattr(value, "uma_VariabilityElement281", self)

class uma_MethodConfiguration(MethodElement):

    pass
class uma_MethodPackage(Package, MethodElement):

    def __init__(self, global: str, uma_MethodPackage: "uma_MethodPackage" = None, uma_MethodPackage67: set["uma_MethodPackage"] = None, MethodPackage: "uma_MethodPackage" = None, childPackages: "uma_MethodPackage" = None, MethodPackage73: "uma_MethodPackage" = None, parentPackage: set["uma_MethodPackage"] = None, uma_MethodPackage277: "uma_MethodPlugin" = None, uma_MethodPackage292: "uma_MethodConfiguration" = None):
        self.global = global
        self.uma_MethodPackage = uma_MethodPackage
        self.uma_MethodPackage67 = uma_MethodPackage67 if uma_MethodPackage67 is not None else set()
        self.MethodPackage = MethodPackage
        self.childPackages = childPackages
        self.MethodPackage73 = MethodPackage73
        self.parentPackage = parentPackage if parentPackage is not None else set()
        self.uma_MethodPackage277 = uma_MethodPackage277
        self.uma_MethodPackage292 = uma_MethodPackage292
        
    @property
    def global(self) -> str:
        return self.__global

    @global.setter
    def global(self, global: str):
        self.__global = global

    @property
    def MethodPackage(self):
        return self.__MethodPackage

    @MethodPackage.setter
    def MethodPackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_MethodPackage__MethodPackage", None)
        self.__MethodPackage = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "childPackages"):
                opp_val = getattr(old_value, "childPackages", None)
                if opp_val == self:
                    setattr(old_value, "childPackages", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "childPackages"):
                opp_val = getattr(value, "childPackages", None)
                setattr(value, "childPackages", self)

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
    def MethodPackage73(self):
        return self.__MethodPackage73

    @MethodPackage73.setter
    def MethodPackage73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_MethodPackage__MethodPackage73", None)
        self.__MethodPackage73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parentPackage"):
                opp_val = getattr(old_value, "parentPackage", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parentPackage"):
                opp_val = getattr(value, "parentPackage", None)
                if opp_val is None:
                    setattr(value, "parentPackage", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def parentPackage(self):
        return self.__parentPackage

    @parentPackage.setter
    def parentPackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_MethodPackage__parentPackage", None)
        self.__parentPackage = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MethodPackage73"):
                    opp_val = getattr(item, "MethodPackage73", None)
                    
                    if opp_val == self:
                        setattr(item, "MethodPackage73", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MethodPackage73"):
                    opp_val = getattr(item, "MethodPackage73", None)
                    
                    setattr(item, "MethodPackage73", self)
                    

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
    def uma_MethodPackage277(self):
        return self.__uma_MethodPackage277

    @uma_MethodPackage277.setter
    def uma_MethodPackage277(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_MethodPackage__uma_MethodPackage277", None)
        self.__uma_MethodPackage277 = value
        
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
    def childPackages(self):
        return self.__childPackages

    @childPackages.setter
    def childPackages(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_MethodPackage__childPackages", None)
        self.__childPackages = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MethodPackage"):
                opp_val = getattr(old_value, "MethodPackage", None)
                if opp_val == self:
                    setattr(old_value, "MethodPackage", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MethodPackage"):
                opp_val = getattr(value, "MethodPackage", None)
                setattr(value, "MethodPackage", self)

    @property
    def uma_MethodPackage292(self):
        return self.__uma_MethodPackage292

    @uma_MethodPackage292.setter
    def uma_MethodPackage292(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_MethodPackage__uma_MethodPackage292", None)
        self.__uma_MethodPackage292 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_MethodConfiguration291"):
                opp_val = getattr(old_value, "uma_MethodConfiguration291", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_MethodConfiguration291"):
                opp_val = getattr(value, "uma_MethodConfiguration291", None)
                if opp_val is None:
                    setattr(value, "uma_MethodConfiguration291", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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

class Namespace:

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
class PackageableElement:

    pass
class uma_MethodElement(PackageableElement):

    def __init__(self, guid: str, briefDescription: str, suppressed: str, orderingGuide: str, uma_MethodElement: set["uma_Constraint"] = None, uma_MethodElement113: "uma_UMASemanticModelBridge" = None):
        self.guid = guid
        self.briefDescription = briefDescription
        self.suppressed = suppressed
        self.orderingGuide = orderingGuide
        self.uma_MethodElement = uma_MethodElement if uma_MethodElement is not None else set()
        self.uma_MethodElement113 = uma_MethodElement113
        
    @property
    def suppressed(self) -> str:
        return self.__suppressed

    @suppressed.setter
    def suppressed(self, suppressed: str):
        self.__suppressed = suppressed

    @property
    def orderingGuide(self) -> str:
        return self.__orderingGuide

    @orderingGuide.setter
    def orderingGuide(self, orderingGuide: str):
        self.__orderingGuide = orderingGuide

    @property
    def guid(self) -> str:
        return self.__guid

    @guid.setter
    def guid(self, guid: str):
        self.__guid = guid

    @property
    def briefDescription(self) -> str:
        return self.__briefDescription

    @briefDescription.setter
    def briefDescription(self, briefDescription: str):
        self.__briefDescription = briefDescription

    @property
    def uma_MethodElement113(self):
        return self.__uma_MethodElement113

    @uma_MethodElement113.setter
    def uma_MethodElement113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_MethodElement__uma_MethodElement113", None)
        self.__uma_MethodElement113 = value
        
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
                    

class uma_Package(Namespace, PackageableElement):

    pass
class uma_Type(PackageableElement):

    pass
class Type:

    pass
class uma_Classifier(Type):

    pass