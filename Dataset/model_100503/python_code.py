from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Modality(Enum):
    Maximum = "Maximum"
    Minimum = "Minimum"
class AggregationType(Enum):
    Composition = "Composition"
    Alternative = "Alternative"
class InteractionVariableType(Enum):
    Monitorable = "Monitorable"
    Controllable = "Controllable"


############################################
# Definition of Classes
############################################

class SubElementReference:

    pass
class RequirementsCoverageData:

    pass
class rdal_FormalLanguageExpression:

    pass
class ReferencedDesignElements:

    pass
class rdal_Trace(ReferencedDesignElements):

    def __init__(self, rdal_Trace: set["rdal_Specification"] = None):
        self.rdal_Trace = rdal_Trace if rdal_Trace is not None else set()
        
        pass
    @property
    def rdal_Trace(self):
        return self.__rdal_Trace

    @rdal_Trace.setter
    def rdal_Trace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdal_Trace__rdal_Trace", None)
        self.__rdal_Trace = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rdal_Specification154"):
                    opp_val = getattr(item, "rdal_Specification154", None)
                    
                    if opp_val == self:
                        setattr(item, "rdal_Specification154", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rdal_Specification154"):
                    opp_val = getattr(item, "rdal_Specification154", None)
                    
                    setattr(item, "rdal_Specification154", self)
                    

    def modelElementReference(self, rdal_modelElement) :
        # TODO: Implement modelElementReference method
        pass

class rdal_RefQueryCollectedDesignElements(ReferencedDesignElements):

    pass
class rdal_RefManuallySelectedDesignElements(ReferencedDesignElements):

    pass
class SatisfiableDesignElementRef:

    pass
class rdal_PrioritizedSatDesignElementRef(SatisfiableDesignElementRef):

    def __init__(self, priority: str, weight: str):
        self.priority = priority
        self.weight = weight
        
        pass
    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight: str):
        self.__weight = weight


    @property
    def priority(self):
        return self.__priority

    @priority.setter
    def priority(self, priority: str):
        self.__priority = priority


class DesignElementReference:

    pass
class rdal_SystContextDesignElemRef(DesignElementReference):

    pass
class rdal_SystOverviewDesignElemRef(DesignElementReference):

    pass
class NonFunctionalGoal:

    pass
class rdal_QualityObjective(NonFunctionalGoal):

    def __init__(self, modality: str, bound: float, rdal_QualityObjective: "rdal_NonFunctionalProperty" = None, rdal_QualityObjective138: "rdal_Sensitivity" = None):
        self.modality = modality
        self.bound = bound
        self.rdal_QualityObjective = rdal_QualityObjective
        self.rdal_QualityObjective138 = rdal_QualityObjective138
        
        pass
    @property
    def modality(self):
        return self.__modality

    @modality.setter
    def modality(self, modality: str):
        self.__modality = modality


    @property
    def bound(self):
        return self.__bound

    @bound.setter
    def bound(self, bound: float):
        self.__bound = bound


    @property
    def rdal_QualityObjective138(self):
        return self.__rdal_QualityObjective138

    @rdal_QualityObjective138.setter
    def rdal_QualityObjective138(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdal_QualityObjective__rdal_QualityObjective138", None)
        self.__rdal_QualityObjective138 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdal_Sensitivity"):
                opp_val = getattr(old_value, "rdal_Sensitivity", None)
                if opp_val == self:
                    setattr(old_value, "rdal_Sensitivity", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdal_Sensitivity"):
                opp_val = getattr(value, "rdal_Sensitivity", None)
                setattr(value, "rdal_Sensitivity", self)

    @property
    def rdal_QualityObjective(self):
        return self.__rdal_QualityObjective

    @rdal_QualityObjective.setter
    def rdal_QualityObjective(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdal_QualityObjective__rdal_QualityObjective", None)
        self.__rdal_QualityObjective = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdal_NonFunctionalProperty136"):
                opp_val = getattr(old_value, "rdal_NonFunctionalProperty136", None)
                if opp_val == self:
                    setattr(old_value, "rdal_NonFunctionalProperty136", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdal_NonFunctionalProperty136"):
                opp_val = getattr(value, "rdal_NonFunctionalProperty136", None)
                setattr(value, "rdal_NonFunctionalProperty136", self)

class AbstractGoal:

    pass
class rdal_SystemFunctionGoal(AbstractGoal):

    pass
class RefineableElement:

    pass
class rdal_NonFunctionalGoal(AbstractGoal):

    pass
class TextualContractualElement:

    pass
class AbstractRequirement:

    pass
class rdal_Assumption(AbstractRequirement):

    pass
class rdal_Requirement(RefineableElement, AbstractRequirement):

    pass
class Variable:

    pass
class rdal_InteractionVariable(Variable):

    def __init__(self, type: str, neglected: bool, rdal_InteractionVariable: "rdal_SystemOverview" = None, rdal_InteractionVariable106: "rdal_SystemContext" = None):
        self.type = type
        self.neglected = neglected
        self.rdal_InteractionVariable = rdal_InteractionVariable
        self.rdal_InteractionVariable106 = rdal_InteractionVariable106
        
        pass
    @property
    def neglected(self):
        return self.__neglected

    @neglected.setter
    def neglected(self, neglected: bool):
        self.__neglected = neglected


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def rdal_InteractionVariable106(self):
        return self.__rdal_InteractionVariable106

    @rdal_InteractionVariable106.setter
    def rdal_InteractionVariable106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdal_InteractionVariable__rdal_InteractionVariable106", None)
        self.__rdal_InteractionVariable106 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdal_SystemContext105"):
                opp_val = getattr(old_value, "rdal_SystemContext105", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdal_SystemContext105"):
                opp_val = getattr(value, "rdal_SystemContext105", None)
                if opp_val is None:
                    setattr(value, "rdal_SystemContext105", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rdal_InteractionVariable(self):
        return self.__rdal_InteractionVariable

    @rdal_InteractionVariable.setter
    def rdal_InteractionVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdal_InteractionVariable__rdal_InteractionVariable", None)
        self.__rdal_InteractionVariable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdal_SystemOverview101"):
                opp_val = getattr(old_value, "rdal_SystemOverview101", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdal_SystemOverview101"):
                opp_val = getattr(value, "rdal_SystemOverview101", None)
                if opp_val is None:
                    setattr(value, "rdal_SystemOverview101", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class RdalOrgPackage:

    pass
class rdal_EObject:

    pass
class rdal_ConstraintLanguagesSpec:

    pass
class rdal_VerifiableElement(ABC):

    def __init__(self, verified: str):
        self.verified = verified
        
        pass
    @property
    def verified(self):
        return self.__verified

    @verified.setter
    def verified(self, verified: str):
        self.__verified = verified


class rdal_SatisfiableElement(ABC):

    def __init__(self, satisfactionLevel: str):
        self.satisfactionLevel = satisfactionLevel
        
        pass
    @property
    def satisfactionLevel(self):
        return self.__satisfactionLevel

    @satisfactionLevel.setter
    def satisfactionLevel(self, satisfactionLevel: str):
        self.__satisfactionLevel = satisfactionLevel


class rdal_Category:

    pass
class rdal_Expression:

    pass
class AbstractContractualElement:

    pass
class rdal_SystemOverview(AbstractContractualElement):

    def __init__(self, purpose: str, rdal_SystemOverview: "rdal_Specification" = None, rdal_SystemOverview101: set["rdal_InteractionVariable"] = None, rdal_SystemOverview92: set["rdal_Capability"] = None, rdal_SystemOverview94: "rdal_EObject" = None, rdal_SystemOverview97: "rdal_EObject" = None, systemOverview: set["rdal_SystemContext"] = None, SystemOverview: "rdal_SystemContext" = None):
        self.purpose = purpose
        self.rdal_SystemOverview = rdal_SystemOverview
        self.rdal_SystemOverview101 = rdal_SystemOverview101 if rdal_SystemOverview101 is not None else set()
        self.rdal_SystemOverview92 = rdal_SystemOverview92 if rdal_SystemOverview92 is not None else set()
        self.rdal_SystemOverview94 = rdal_SystemOverview94
        self.rdal_SystemOverview97 = rdal_SystemOverview97
        self.systemOverview = systemOverview if systemOverview is not None else set()
        self.SystemOverview = SystemOverview
        
        pass
    @property
    def purpose(self):
        return self.__purpose

    @purpose.setter
    def purpose(self, purpose: str):
        self.__purpose = purpose


    @property
    def rdal_SystemOverview97(self):
        return self.__rdal_SystemOverview97

    @rdal_SystemOverview97.setter
    def rdal_SystemOverview97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdal_SystemOverview__rdal_SystemOverview97", None)
        self.__rdal_SystemOverview97 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdal_EObject98"):
                opp_val = getattr(old_value, "rdal_EObject98", None)
                if opp_val == self:
                    setattr(old_value, "rdal_EObject98", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdal_EObject98"):
                opp_val = getattr(value, "rdal_EObject98", None)
                setattr(value, "rdal_EObject98", self)

    @property
    def rdal_SystemOverview94(self):
        return self.__rdal_SystemOverview94

    @rdal_SystemOverview94.setter
    def rdal_SystemOverview94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdal_SystemOverview__rdal_SystemOverview94", None)
        self.__rdal_SystemOverview94 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdal_EObject95"):
                opp_val = getattr(old_value, "rdal_EObject95", None)
                if opp_val == self:
                    setattr(old_value, "rdal_EObject95", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdal_EObject95"):
                opp_val = getattr(value, "rdal_EObject95", None)
                setattr(value, "rdal_EObject95", self)

    @property
    def SystemOverview(self):
        return self.__SystemOverview

    @SystemOverview.setter
    def SystemOverview(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdal_SystemOverview__SystemOverview", None)
        self.__SystemOverview = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownedContexts"):
                opp_val = getattr(old_value, "ownedContexts", None)
                if opp_val == self:
                    setattr(old_value, "ownedContexts", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedContexts"):
                opp_val = getattr(value, "ownedContexts", None)
                setattr(value, "ownedContexts", self)

    @property
    def systemOverview(self):
        return self.__systemOverview

    @systemOverview.setter
    def systemOverview(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdal_SystemOverview__systemOverview", None)
        self.__systemOverview = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SystemContext"):
                    opp_val = getattr(item, "SystemContext", None)
                    
                    if opp_val == self:
                        setattr(item, "SystemContext", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SystemContext"):
                    opp_val = getattr(item, "SystemContext", None)
                    
                    setattr(item, "SystemContext", self)
                    

    @property
    def rdal_SystemOverview(self):
        return self.__rdal_SystemOverview

    @rdal_SystemOverview.setter
    def rdal_SystemOverview(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdal_SystemOverview__rdal_SystemOverview", None)
        self.__rdal_SystemOverview = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdal_Specification57"):
                opp_val = getattr(old_value, "rdal_Specification57", None)
                if opp_val == self:
                    setattr(old_value, "rdal_Specification57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdal_Specification57"):
                opp_val = getattr(value, "rdal_Specification57", None)
                setattr(value, "rdal_Specification57", self)

    @property
    def rdal_SystemOverview92(self):
        return self.__rdal_SystemOverview92

    @rdal_SystemOverview92.setter
    def rdal_SystemOverview92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdal_SystemOverview__rdal_SystemOverview92", None)
        self.__rdal_SystemOverview92 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rdal_Capability"):
                    opp_val = getattr(item, "rdal_Capability", None)
                    
                    if opp_val == self:
                        setattr(item, "rdal_Capability", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rdal_Capability"):
                    opp_val = getattr(item, "rdal_Capability", None)
                    
                    setattr(item, "rdal_Capability", self)
                    

    @property
    def rdal_SystemOverview101(self):
        return self.__rdal_SystemOverview101

    @rdal_SystemOverview101.setter
    def rdal_SystemOverview101(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdal_SystemOverview__rdal_SystemOverview101", None)
        self.__rdal_SystemOverview101 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rdal_InteractionVariable"):
                    opp_val = getattr(item, "rdal_InteractionVariable", None)
                    
                    if opp_val == self:
                        setattr(item, "rdal_InteractionVariable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rdal_InteractionVariable"):
                    opp_val = getattr(item, "rdal_InteractionVariable", None)
                    
                    setattr(item, "rdal_InteractionVariable", self)
                    

class rdal_SystemContext(AbstractContractualElement):

    pass
class rdal_TextualContractualElement(AbstractContractualElement):

    def __init__(self, priority: str, rdal_TextualContractualElement: "rdal_Expression" = None, rdal_TextualContractualElement43: "rdal_Expression" = None, rdal_TextualContractualElement47: "rdal_TextualContractualElement" = None, rdal_TextualContractualElement45: set["rdal_TextualContractualElement"] = None, rdal_TextualContractualElement49: "rdal_Category" = None, rdal_TextualContractualElement80: "rdal_RdalOrgPackage" = None):
        self.priority = priority
        self.rdal_TextualContractualElement = rdal_TextualContractualElement
        self.rdal_TextualContractualElement43 = rdal_TextualContractualElement43
        self.rdal_TextualContractualElement47 = rdal_TextualContractualElement47
        self.rdal_TextualContractualElement45 = rdal_TextualContractualElement45 if rdal_TextualContractualElement45 is not None else set()
        self.rdal_TextualContractualElement49 = rdal_TextualContractualElement49
        self.rdal_TextualContractualElement80 = rdal_TextualContractualElement80
        
        pass
    @property
    def priority(self):
        return self.__priority

    @priority.setter
    def priority(self, priority: str):
        self.__priority = priority


    @property
    def rdal_TextualContractualElement47(self):
        return self.__rdal_TextualContractualElement47

    @rdal_TextualContractualElement47.setter
    def rdal_TextualContractualElement47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdal_TextualContractualElement__rdal_TextualContractualElement47", None)
        self.__rdal_TextualContractualElement47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdal_TextualContractualElement45"):
                opp_val = getattr(old_value, "rdal_TextualContractualElement45", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdal_TextualContractualElement45"):
                opp_val = getattr(value, "rdal_TextualContractualElement45", None)
                if opp_val is None:
                    setattr(value, "rdal_TextualContractualElement45", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rdal_TextualContractualElement45(self):
        return self.__rdal_TextualContractualElement45

    @rdal_TextualContractualElement45.setter
    def rdal_TextualContractualElement45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdal_TextualContractualElement__rdal_TextualContractualElement45", None)
        self.__rdal_TextualContractualElement45 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rdal_TextualContractualElement47"):
                    opp_val = getattr(item, "rdal_TextualContractualElement47", None)
                    
                    if opp_val == self:
                        setattr(item, "rdal_TextualContractualElement47", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rdal_TextualContractualElement47"):
                    opp_val = getattr(item, "rdal_TextualContractualElement47", None)
                    
                    setattr(item, "rdal_TextualContractualElement47", self)
                    

    @property
    def rdal_TextualContractualElement80(self):
        return self.__rdal_TextualContractualElement80

    @rdal_TextualContractualElement80.setter
    def rdal_TextualContractualElement80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdal_TextualContractualElement__rdal_TextualContractualElement80", None)
        self.__rdal_TextualContractualElement80 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdal_RdalOrgPackage79"):
                opp_val = getattr(old_value, "rdal_RdalOrgPackage79", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdal_RdalOrgPackage79"):
                opp_val = getattr(value, "rdal_RdalOrgPackage79", None)
                if opp_val is None:
                    setattr(value, "rdal_RdalOrgPackage79", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rdal_TextualContractualElement43(self):
        return self.__rdal_TextualContractualElement43

    @rdal_TextualContractualElement43.setter
    def rdal_TextualContractualElement43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdal_TextualContractualElement__rdal_TextualContractualElement43", None)
        self.__rdal_TextualContractualElement43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdal_Expression44"):
                opp_val = getattr(old_value, "rdal_Expression44", None)
                if opp_val == self:
                    setattr(old_value, "rdal_Expression44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdal_Expression44"):
                opp_val = getattr(value, "rdal_Expression44", None)
                setattr(value, "rdal_Expression44", self)

    @property
    def rdal_TextualContractualElement(self):
        return self.__rdal_TextualContractualElement

    @rdal_TextualContractualElement.setter
    def rdal_TextualContractualElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdal_TextualContractualElement__rdal_TextualContractualElement", None)
        self.__rdal_TextualContractualElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdal_Expression"):
                opp_val = getattr(old_value, "rdal_Expression", None)
                if opp_val == self:
                    setattr(old_value, "rdal_Expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdal_Expression"):
                opp_val = getattr(value, "rdal_Expression", None)
                setattr(value, "rdal_Expression", self)

    @property
    def rdal_TextualContractualElement49(self):
        return self.__rdal_TextualContractualElement49

    @rdal_TextualContractualElement49.setter
    def rdal_TextualContractualElement49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdal_TextualContractualElement__rdal_TextualContractualElement49", None)
        self.__rdal_TextualContractualElement49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdal_Category"):
                opp_val = getattr(old_value, "rdal_Category", None)
                if opp_val == self:
                    setattr(old_value, "rdal_Category", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdal_Category"):
                opp_val = getattr(value, "rdal_Category", None)
                setattr(value, "rdal_Category", self)

class TraceableToDesignElementsElement:

    pass
class rdal_Sensitivity(TraceableToDesignElementsElement):

    pass
class rdal_AbstractContractualElement(TraceableToDesignElementsElement):

    def __init__(self, originDate: str, scheduleDate: str, sources: str, dropped: bool, rdal_AbstractContractualElement24: set["rdal_Rationale"] = None, rdal_AbstractContractualElement26: set["rdal_ContactInformation"] = None, rdal_AbstractContractualElement29: "rdal_AbstractContractualElement" = None, rdal_AbstractContractualElement27: set["rdal_AbstractContractualElement"] = None, rdal_AbstractContractualElement31: set["rdal_Rationale"] = None, rdal_AbstractContractualElement34: "rdal_Uncertainty" = None, rdal_AbstractContractualElement: set["rdal_Stakeholder"] = None, rdal_AbstractContractualElement143: "rdal_Conflict" = None):
        self.originDate = originDate
        self.scheduleDate = scheduleDate
        self.sources = sources
        self.dropped = dropped
        self.rdal_AbstractContractualElement24 = rdal_AbstractContractualElement24 if rdal_AbstractContractualElement24 is not None else set()
        self.rdal_AbstractContractualElement26 = rdal_AbstractContractualElement26 if rdal_AbstractContractualElement26 is not None else set()
        self.rdal_AbstractContractualElement29 = rdal_AbstractContractualElement29
        self.rdal_AbstractContractualElement27 = rdal_AbstractContractualElement27 if rdal_AbstractContractualElement27 is not None else set()
        self.rdal_AbstractContractualElement31 = rdal_AbstractContractualElement31 if rdal_AbstractContractualElement31 is not None else set()
        self.rdal_AbstractContractualElement34 = rdal_AbstractContractualElement34
        self.rdal_AbstractContractualElement = rdal_AbstractContractualElement if rdal_AbstractContractualElement is not None else set()
        self.rdal_AbstractContractualElement143 = rdal_AbstractContractualElement143
        
        pass
    @property
    def scheduleDate(self):
        return self.__scheduleDate

    @scheduleDate.setter
    def scheduleDate(self, scheduleDate: str):
        self.__scheduleDate = scheduleDate


    @property
    def originDate(self):
        return self.__originDate

    @originDate.setter
    def originDate(self, originDate: str):
        self.__originDate = originDate


    @property
    def sources(self):
        return self.__sources

    @sources.setter
    def sources(self, sources: str):
        self.__sources = sources


    @property
    def dropped(self):
        return self.__dropped

    @dropped.setter
    def dropped(self, dropped: bool):
        self.__dropped = dropped


    @property
    def rdal_AbstractContractualElement27(self):
        return self.__rdal_AbstractContractualElement27

    @rdal_AbstractContractualElement27.setter
    def rdal_AbstractContractualElement27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdal_AbstractContractualElement__rdal_AbstractContractualElement27", None)
        self.__rdal_AbstractContractualElement27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rdal_AbstractContractualElement29"):
                    opp_val = getattr(item, "rdal_AbstractContractualElement29", None)
                    
                    if opp_val == self:
                        setattr(item, "rdal_AbstractContractualElement29", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rdal_AbstractContractualElement29"):
                    opp_val = getattr(item, "rdal_AbstractContractualElement29", None)
                    
                    setattr(item, "rdal_AbstractContractualElement29", self)
                    

    @property
    def rdal_AbstractContractualElement34(self):
        return self.__rdal_AbstractContractualElement34

    @rdal_AbstractContractualElement34.setter
    def rdal_AbstractContractualElement34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdal_AbstractContractualElement__rdal_AbstractContractualElement34", None)
        self.__rdal_AbstractContractualElement34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdal_Uncertainty"):
                opp_val = getattr(old_value, "rdal_Uncertainty", None)
                if opp_val == self:
                    setattr(old_value, "rdal_Uncertainty", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdal_Uncertainty"):
                opp_val = getattr(value, "rdal_Uncertainty", None)
                setattr(value, "rdal_Uncertainty", self)

    @property
    def rdal_AbstractContractualElement143(self):
        return self.__rdal_AbstractContractualElement143

    @rdal_AbstractContractualElement143.setter
    def rdal_AbstractContractualElement143(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdal_AbstractContractualElement__rdal_AbstractContractualElement143", None)
        self.__rdal_AbstractContractualElement143 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdal_Conflict142"):
                opp_val = getattr(old_value, "rdal_Conflict142", None)
                if opp_val == self:
                    setattr(old_value, "rdal_Conflict142", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdal_Conflict142"):
                opp_val = getattr(value, "rdal_Conflict142", None)
                setattr(value, "rdal_Conflict142", self)

    @property
    def rdal_AbstractContractualElement(self):
        return self.__rdal_AbstractContractualElement

    @rdal_AbstractContractualElement.setter
    def rdal_AbstractContractualElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdal_AbstractContractualElement__rdal_AbstractContractualElement", None)
        self.__rdal_AbstractContractualElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rdal_Stakeholder"):
                    opp_val = getattr(item, "rdal_Stakeholder", None)
                    
                    if opp_val == self:
                        setattr(item, "rdal_Stakeholder", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rdal_Stakeholder"):
                    opp_val = getattr(item, "rdal_Stakeholder", None)
                    
                    setattr(item, "rdal_Stakeholder", self)
                    

    @property
    def rdal_AbstractContractualElement31(self):
        return self.__rdal_AbstractContractualElement31

    @rdal_AbstractContractualElement31.setter
    def rdal_AbstractContractualElement31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdal_AbstractContractualElement__rdal_AbstractContractualElement31", None)
        self.__rdal_AbstractContractualElement31 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rdal_Rationale32"):
                    opp_val = getattr(item, "rdal_Rationale32", None)
                    
                    if opp_val == self:
                        setattr(item, "rdal_Rationale32", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rdal_Rationale32"):
                    opp_val = getattr(item, "rdal_Rationale32", None)
                    
                    setattr(item, "rdal_Rationale32", self)
                    

    @property
    def rdal_AbstractContractualElement29(self):
        return self.__rdal_AbstractContractualElement29

    @rdal_AbstractContractualElement29.setter
    def rdal_AbstractContractualElement29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdal_AbstractContractualElement__rdal_AbstractContractualElement29", None)
        self.__rdal_AbstractContractualElement29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdal_AbstractContractualElement27"):
                opp_val = getattr(old_value, "rdal_AbstractContractualElement27", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdal_AbstractContractualElement27"):
                opp_val = getattr(value, "rdal_AbstractContractualElement27", None)
                if opp_val is None:
                    setattr(value, "rdal_AbstractContractualElement27", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rdal_AbstractContractualElement26(self):
        return self.__rdal_AbstractContractualElement26

    @rdal_AbstractContractualElement26.setter
    def rdal_AbstractContractualElement26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdal_AbstractContractualElement__rdal_AbstractContractualElement26", None)
        self.__rdal_AbstractContractualElement26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rdal_ContactInformation"):
                    opp_val = getattr(item, "rdal_ContactInformation", None)
                    
                    if opp_val == self:
                        setattr(item, "rdal_ContactInformation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rdal_ContactInformation"):
                    opp_val = getattr(item, "rdal_ContactInformation", None)
                    
                    setattr(item, "rdal_ContactInformation", self)
                    

    @property
    def rdal_AbstractContractualElement24(self):
        return self.__rdal_AbstractContractualElement24

    @rdal_AbstractContractualElement24.setter
    def rdal_AbstractContractualElement24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdal_AbstractContractualElement__rdal_AbstractContractualElement24", None)
        self.__rdal_AbstractContractualElement24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rdal_Rationale"):
                    opp_val = getattr(item, "rdal_Rationale", None)
                    
                    if opp_val == self:
                        setattr(item, "rdal_Rationale", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rdal_Rationale"):
                    opp_val = getattr(item, "rdal_Rationale", None)
                    
                    setattr(item, "rdal_Rationale", self)
                    

class rdal_SubGoalReference(SubElementReference):

    pass
class rdal_SubRequirementReference(SubElementReference):

    pass
class VerifiableElement:

    pass
class rdal_TraceDesignElementRef(RequirementsCoverageData, VerifiableElement, DesignElementReference):

    def __init__(self, container: bool):
        self.container = container
        
        pass
    @property
    def container(self):
        return self.__container

    @container.setter
    def container(self, container: bool):
        self.__container = container


    def merge(self, rdal_modelElementReference):
        # TODO: Implement merge method
        pass

class rdal_VerifiableDesignElementRef(VerifiableElement, DesignElementReference):

    pass
class SatisfiableElement:

    pass
class rdal_AbstractRequirement(TextualContractualElement, SatisfiableElement, VerifiableElement):

    def __init__(self, risk: str, rdal_AbstractRequirement12: "rdal_RequirementRefinement" = None, rdal_AbstractRequirement: "rdal_RequirementRefinement" = None, requirements: set["rdal_VerificationActivity"] = None, ownedRequirements: "rdal_RequirementsPackage" = None, AbstractRequirement121: "rdal_VerificationActivity" = None, rdal_AbstractRequirement163: "rdal_SubRequirementReference" = None, AbstractRequirement: "rdal_RequirementsPackage" = None):
        self.risk = risk
        self.rdal_AbstractRequirement12 = rdal_AbstractRequirement12
        self.rdal_AbstractRequirement = rdal_AbstractRequirement
        self.requirements = requirements if requirements is not None else set()
        self.ownedRequirements = ownedRequirements
        self.AbstractRequirement121 = AbstractRequirement121
        self.rdal_AbstractRequirement163 = rdal_AbstractRequirement163
        self.AbstractRequirement = AbstractRequirement
        
        pass
    @property
    def risk(self):
        return self.__risk

    @risk.setter
    def risk(self, risk: str):
        self.__risk = risk


    @property
    def AbstractRequirement(self):
        return self.__AbstractRequirement

    @AbstractRequirement.setter
    def AbstractRequirement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdal_AbstractRequirement__AbstractRequirement", None)
        self.__AbstractRequirement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "package"):
                opp_val = getattr(old_value, "package", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "package"):
                opp_val = getattr(value, "package", None)
                if opp_val is None:
                    setattr(value, "package", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def AbstractRequirement121(self):
        return self.__AbstractRequirement121

    @AbstractRequirement121.setter
    def AbstractRequirement121(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdal_AbstractRequirement__AbstractRequirement121", None)
        self.__AbstractRequirement121 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownedVerifiedBy"):
                opp_val = getattr(old_value, "ownedVerifiedBy", None)
                if opp_val == self:
                    setattr(old_value, "ownedVerifiedBy", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedVerifiedBy"):
                opp_val = getattr(value, "ownedVerifiedBy", None)
                setattr(value, "ownedVerifiedBy", self)

    @property
    def ownedRequirements(self):
        return self.__ownedRequirements

    @ownedRequirements.setter
    def ownedRequirements(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdal_AbstractRequirement__ownedRequirements", None)
        self.__ownedRequirements = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RequirementsPackage"):
                opp_val = getattr(old_value, "RequirementsPackage", None)
                if opp_val == self:
                    setattr(old_value, "RequirementsPackage", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RequirementsPackage"):
                opp_val = getattr(value, "RequirementsPackage", None)
                setattr(value, "RequirementsPackage", self)

    @property
    def rdal_AbstractRequirement12(self):
        return self.__rdal_AbstractRequirement12

    @rdal_AbstractRequirement12.setter
    def rdal_AbstractRequirement12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdal_AbstractRequirement__rdal_AbstractRequirement12", None)
        self.__rdal_AbstractRequirement12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdal_RequirementRefinement11"):
                opp_val = getattr(old_value, "rdal_RequirementRefinement11", None)
                if opp_val == self:
                    setattr(old_value, "rdal_RequirementRefinement11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdal_RequirementRefinement11"):
                opp_val = getattr(value, "rdal_RequirementRefinement11", None)
                setattr(value, "rdal_RequirementRefinement11", self)

    @property
    def rdal_AbstractRequirement163(self):
        return self.__rdal_AbstractRequirement163

    @rdal_AbstractRequirement163.setter
    def rdal_AbstractRequirement163(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdal_AbstractRequirement__rdal_AbstractRequirement163", None)
        self.__rdal_AbstractRequirement163 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdal_SubRequirementReference162"):
                opp_val = getattr(old_value, "rdal_SubRequirementReference162", None)
                if opp_val == self:
                    setattr(old_value, "rdal_SubRequirementReference162", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdal_SubRequirementReference162"):
                opp_val = getattr(value, "rdal_SubRequirementReference162", None)
                setattr(value, "rdal_SubRequirementReference162", self)

    @property
    def rdal_AbstractRequirement(self):
        return self.__rdal_AbstractRequirement

    @rdal_AbstractRequirement.setter
    def rdal_AbstractRequirement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdal_AbstractRequirement__rdal_AbstractRequirement", None)
        self.__rdal_AbstractRequirement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdal_RequirementRefinement9"):
                opp_val = getattr(old_value, "rdal_RequirementRefinement9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdal_RequirementRefinement9"):
                opp_val = getattr(value, "rdal_RequirementRefinement9", None)
                if opp_val is None:
                    setattr(value, "rdal_RequirementRefinement9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def requirements(self):
        return self.__requirements

    @requirements.setter
    def requirements(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdal_AbstractRequirement__requirements", None)
        self.__requirements = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "VerificationActivity"):
                    opp_val = getattr(item, "VerificationActivity", None)
                    
                    if opp_val == self:
                        setattr(item, "VerificationActivity", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "VerificationActivity"):
                    opp_val = getattr(item, "VerificationActivity", None)
                    
                    setattr(item, "VerificationActivity", self)
                    

class rdal_RequirementsPackage(RdalOrgPackage, SatisfiableElement, VerifiableElement):

    pass
class rdal_AbstractGoal(RefineableElement, SatisfiableElement, TextualContractualElement):

    pass
class rdal_Specification(SatisfiableElement, AbstractContractualElement, VerifiableElement):

    def __init__(self, version: str, specification: set["rdal_RdalOrgPackage"] = None, rdal_Specification52: set["rdal_ContactInformation"] = None, rdal_Specification55: set["rdal_Conflict"] = None, rdal_Specification57: "rdal_SystemOverview" = None, rdal_Specification59: "rdal_ConstraintLanguagesSpec" = None, rdal_Specification61: set["rdal_ActorReference"] = None, rdal_Specification63: set["rdal_EObject"] = None, rdal_Specification65: set["rdal_NonFunctionalProperty"] = None, rdal_Specification67: set["rdal_Stakeholder"] = None, Specification: "rdal_RdalOrgPackage" = None, rdal_Specification: "rdal_TraceableToDesignElementsElement" = None, rdal_Specification154: "rdal_Trace" = None):
        self.version = version
        self.specification = specification if specification is not None else set()
        self.rdal_Specification52 = rdal_Specification52 if rdal_Specification52 is not None else set()
        self.rdal_Specification55 = rdal_Specification55 if rdal_Specification55 is not None else set()
        self.rdal_Specification57 = rdal_Specification57
        self.rdal_Specification59 = rdal_Specification59
        self.rdal_Specification61 = rdal_Specification61 if rdal_Specification61 is not None else set()
        self.rdal_Specification63 = rdal_Specification63 if rdal_Specification63 is not None else set()
        self.rdal_Specification65 = rdal_Specification65 if rdal_Specification65 is not None else set()
        self.rdal_Specification67 = rdal_Specification67 if rdal_Specification67 is not None else set()
        self.Specification = Specification
        self.rdal_Specification = rdal_Specification
        self.rdal_Specification154 = rdal_Specification154
        
        pass
    @property
    def version(self):
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version


    @property
    def rdal_Specification154(self):
        return self.__rdal_Specification154

    @rdal_Specification154.setter
    def rdal_Specification154(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdal_Specification__rdal_Specification154", None)
        self.__rdal_Specification154 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdal_Trace"):
                opp_val = getattr(old_value, "rdal_Trace", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdal_Trace"):
                opp_val = getattr(value, "rdal_Trace", None)
                if opp_val is None:
                    setattr(value, "rdal_Trace", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rdal_Specification57(self):
        return self.__rdal_Specification57

    @rdal_Specification57.setter
    def rdal_Specification57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdal_Specification__rdal_Specification57", None)
        self.__rdal_Specification57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdal_SystemOverview"):
                opp_val = getattr(old_value, "rdal_SystemOverview", None)
                if opp_val == self:
                    setattr(old_value, "rdal_SystemOverview", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdal_SystemOverview"):
                opp_val = getattr(value, "rdal_SystemOverview", None)
                setattr(value, "rdal_SystemOverview", self)

    @property
    def rdal_Specification59(self):
        return self.__rdal_Specification59

    @rdal_Specification59.setter
    def rdal_Specification59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdal_Specification__rdal_Specification59", None)
        self.__rdal_Specification59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdal_ConstraintLanguagesSpec"):
                opp_val = getattr(old_value, "rdal_ConstraintLanguagesSpec", None)
                if opp_val == self:
                    setattr(old_value, "rdal_ConstraintLanguagesSpec", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdal_ConstraintLanguagesSpec"):
                opp_val = getattr(value, "rdal_ConstraintLanguagesSpec", None)
                setattr(value, "rdal_ConstraintLanguagesSpec", self)

    @property
    def rdal_Specification65(self):
        return self.__rdal_Specification65

    @rdal_Specification65.setter
    def rdal_Specification65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdal_Specification__rdal_Specification65", None)
        self.__rdal_Specification65 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rdal_NonFunctionalProperty"):
                    opp_val = getattr(item, "rdal_NonFunctionalProperty", None)
                    
                    if opp_val == self:
                        setattr(item, "rdal_NonFunctionalProperty", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rdal_NonFunctionalProperty"):
                    opp_val = getattr(item, "rdal_NonFunctionalProperty", None)
                    
                    setattr(item, "rdal_NonFunctionalProperty", self)
                    

    @property
    def rdal_Specification(self):
        return self.__rdal_Specification

    @rdal_Specification.setter
    def rdal_Specification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdal_Specification__rdal_Specification", None)
        self.__rdal_Specification = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdal_TraceableToDesignElementsElement21"):
                opp_val = getattr(old_value, "rdal_TraceableToDesignElementsElement21", None)
                if opp_val == self:
                    setattr(old_value, "rdal_TraceableToDesignElementsElement21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdal_TraceableToDesignElementsElement21"):
                opp_val = getattr(value, "rdal_TraceableToDesignElementsElement21", None)
                setattr(value, "rdal_TraceableToDesignElementsElement21", self)

    @property
    def rdal_Specification67(self):
        return self.__rdal_Specification67

    @rdal_Specification67.setter
    def rdal_Specification67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdal_Specification__rdal_Specification67", None)
        self.__rdal_Specification67 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rdal_Stakeholder68"):
                    opp_val = getattr(item, "rdal_Stakeholder68", None)
                    
                    if opp_val == self:
                        setattr(item, "rdal_Stakeholder68", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rdal_Stakeholder68"):
                    opp_val = getattr(item, "rdal_Stakeholder68", None)
                    
                    setattr(item, "rdal_Stakeholder68", self)
                    

    @property
    def rdal_Specification52(self):
        return self.__rdal_Specification52

    @rdal_Specification52.setter
    def rdal_Specification52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdal_Specification__rdal_Specification52", None)
        self.__rdal_Specification52 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rdal_ContactInformation53"):
                    opp_val = getattr(item, "rdal_ContactInformation53", None)
                    
                    if opp_val == self:
                        setattr(item, "rdal_ContactInformation53", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rdal_ContactInformation53"):
                    opp_val = getattr(item, "rdal_ContactInformation53", None)
                    
                    setattr(item, "rdal_ContactInformation53", self)
                    

    @property
    def rdal_Specification61(self):
        return self.__rdal_Specification61

    @rdal_Specification61.setter
    def rdal_Specification61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdal_Specification__rdal_Specification61", None)
        self.__rdal_Specification61 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rdal_ActorReference"):
                    opp_val = getattr(item, "rdal_ActorReference", None)
                    
                    if opp_val == self:
                        setattr(item, "rdal_ActorReference", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rdal_ActorReference"):
                    opp_val = getattr(item, "rdal_ActorReference", None)
                    
                    setattr(item, "rdal_ActorReference", self)
                    

    @property
    def rdal_Specification55(self):
        return self.__rdal_Specification55

    @rdal_Specification55.setter
    def rdal_Specification55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdal_Specification__rdal_Specification55", None)
        self.__rdal_Specification55 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rdal_Conflict"):
                    opp_val = getattr(item, "rdal_Conflict", None)
                    
                    if opp_val == self:
                        setattr(item, "rdal_Conflict", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rdal_Conflict"):
                    opp_val = getattr(item, "rdal_Conflict", None)
                    
                    setattr(item, "rdal_Conflict", self)
                    

    @property
    def Specification(self):
        return self.__Specification

    @Specification.setter
    def Specification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdal_Specification__Specification", None)
        self.__Specification = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownedPackages"):
                opp_val = getattr(old_value, "ownedPackages", None)
                if opp_val == self:
                    setattr(old_value, "ownedPackages", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedPackages"):
                opp_val = getattr(value, "ownedPackages", None)
                setattr(value, "ownedPackages", self)

    @property
    def specification(self):
        return self.__specification

    @specification.setter
    def specification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdal_Specification__specification", None)
        self.__specification = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RdalOrgPackage"):
                    opp_val = getattr(item, "RdalOrgPackage", None)
                    
                    if opp_val == self:
                        setattr(item, "RdalOrgPackage", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RdalOrgPackage"):
                    opp_val = getattr(item, "RdalOrgPackage", None)
                    
                    setattr(item, "RdalOrgPackage", self)
                    

    @property
    def rdal_Specification63(self):
        return self.__rdal_Specification63

    @rdal_Specification63.setter
    def rdal_Specification63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdal_Specification__rdal_Specification63", None)
        self.__rdal_Specification63 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rdal_EObject"):
                    opp_val = getattr(item, "rdal_EObject", None)
                    
                    if opp_val == self:
                        setattr(item, "rdal_EObject", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rdal_EObject"):
                    opp_val = getattr(item, "rdal_EObject", None)
                    
                    setattr(item, "rdal_EObject", self)
                    

class rdal_GoalsPackage(SatisfiableElement, RdalOrgPackage):

    pass
class rdal_SatisfiableDesignElementRef(SatisfiableElement, DesignElementReference):

    pass
class ElementRefinement:

    pass
class rdal_GoalRefinement(ElementRefinement, SatisfiableElement):

    pass
class rdal_RequirementRefinement(ElementRefinement, SatisfiableElement, VerifiableElement):

    pass
class rdal_RefineableElement(ABC):

    pass
class IdentifiedElement:

    pass
class rdal_RdalOrgPackage(IdentifiedElement):

    def __init__(self, contractualElementEntries: str, refinementEntries: str, RdalOrgPackage: "rdal_Specification" = None, RdalOrgPackage75: "rdal_RdalOrgPackage" = None, subPackages: "rdal_RdalOrgPackage" = None, ownedPackages: "rdal_Specification" = None, RdalOrgPackage72: "rdal_RdalOrgPackage" = None, parent: set["rdal_RdalOrgPackage"] = None, rdal_RdalOrgPackage: set["rdal_ElementRefinement"] = None, rdal_RdalOrgPackage79: set["rdal_TextualContractualElement"] = None):
        self.contractualElementEntries = contractualElementEntries
        self.refinementEntries = refinementEntries
        self.RdalOrgPackage = RdalOrgPackage
        self.RdalOrgPackage75 = RdalOrgPackage75
        self.subPackages = subPackages
        self.ownedPackages = ownedPackages
        self.RdalOrgPackage72 = RdalOrgPackage72
        self.parent = parent if parent is not None else set()
        self.rdal_RdalOrgPackage = rdal_RdalOrgPackage if rdal_RdalOrgPackage is not None else set()
        self.rdal_RdalOrgPackage79 = rdal_RdalOrgPackage79 if rdal_RdalOrgPackage79 is not None else set()
        
        pass
    @property
    def refinementEntries(self):
        return self.__refinementEntries

    @refinementEntries.setter
    def refinementEntries(self, refinementEntries: str):
        self.__refinementEntries = refinementEntries


    @property
    def contractualElementEntries(self):
        return self.__contractualElementEntries

    @contractualElementEntries.setter
    def contractualElementEntries(self, contractualElementEntries: str):
        self.__contractualElementEntries = contractualElementEntries


    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdal_RdalOrgPackage__parent", None)
        self.__parent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RdalOrgPackage72"):
                    opp_val = getattr(item, "RdalOrgPackage72", None)
                    
                    if opp_val == self:
                        setattr(item, "RdalOrgPackage72", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RdalOrgPackage72"):
                    opp_val = getattr(item, "RdalOrgPackage72", None)
                    
                    setattr(item, "RdalOrgPackage72", self)
                    

    @property
    def subPackages(self):
        return self.__subPackages

    @subPackages.setter
    def subPackages(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdal_RdalOrgPackage__subPackages", None)
        self.__subPackages = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RdalOrgPackage75"):
                opp_val = getattr(old_value, "RdalOrgPackage75", None)
                if opp_val == self:
                    setattr(old_value, "RdalOrgPackage75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RdalOrgPackage75"):
                opp_val = getattr(value, "RdalOrgPackage75", None)
                setattr(value, "RdalOrgPackage75", self)

    @property
    def RdalOrgPackage(self):
        return self.__RdalOrgPackage

    @RdalOrgPackage.setter
    def RdalOrgPackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdal_RdalOrgPackage__RdalOrgPackage", None)
        self.__RdalOrgPackage = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "specification"):
                opp_val = getattr(old_value, "specification", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "specification"):
                opp_val = getattr(value, "specification", None)
                if opp_val is None:
                    setattr(value, "specification", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ownedPackages(self):
        return self.__ownedPackages

    @ownedPackages.setter
    def ownedPackages(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdal_RdalOrgPackage__ownedPackages", None)
        self.__ownedPackages = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Specification"):
                opp_val = getattr(old_value, "Specification", None)
                if opp_val == self:
                    setattr(old_value, "Specification", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Specification"):
                opp_val = getattr(value, "Specification", None)
                setattr(value, "Specification", self)

    @property
    def RdalOrgPackage75(self):
        return self.__RdalOrgPackage75

    @RdalOrgPackage75.setter
    def RdalOrgPackage75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdal_RdalOrgPackage__RdalOrgPackage75", None)
        self.__RdalOrgPackage75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "subPackages"):
                opp_val = getattr(old_value, "subPackages", None)
                if opp_val == self:
                    setattr(old_value, "subPackages", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "subPackages"):
                opp_val = getattr(value, "subPackages", None)
                setattr(value, "subPackages", self)

    @property
    def rdal_RdalOrgPackage(self):
        return self.__rdal_RdalOrgPackage

    @rdal_RdalOrgPackage.setter
    def rdal_RdalOrgPackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdal_RdalOrgPackage__rdal_RdalOrgPackage", None)
        self.__rdal_RdalOrgPackage = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rdal_ElementRefinement77"):
                    opp_val = getattr(item, "rdal_ElementRefinement77", None)
                    
                    if opp_val == self:
                        setattr(item, "rdal_ElementRefinement77", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rdal_ElementRefinement77"):
                    opp_val = getattr(item, "rdal_ElementRefinement77", None)
                    
                    setattr(item, "rdal_ElementRefinement77", self)
                    

    @property
    def rdal_RdalOrgPackage79(self):
        return self.__rdal_RdalOrgPackage79

    @rdal_RdalOrgPackage79.setter
    def rdal_RdalOrgPackage79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdal_RdalOrgPackage__rdal_RdalOrgPackage79", None)
        self.__rdal_RdalOrgPackage79 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rdal_TextualContractualElement80"):
                    opp_val = getattr(item, "rdal_TextualContractualElement80", None)
                    
                    if opp_val == self:
                        setattr(item, "rdal_TextualContractualElement80", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rdal_TextualContractualElement80"):
                    opp_val = getattr(item, "rdal_TextualContractualElement80", None)
                    
                    setattr(item, "rdal_TextualContractualElement80", self)
                    

    @property
    def RdalOrgPackage72(self):
        return self.__RdalOrgPackage72

    @RdalOrgPackage72.setter
    def RdalOrgPackage72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdal_RdalOrgPackage__RdalOrgPackage72", None)
        self.__RdalOrgPackage72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent"):
                opp_val = getattr(old_value, "parent", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent"):
                opp_val = getattr(value, "parent", None)
                if opp_val is None:
                    setattr(value, "parent", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class rdal_ReferencedDesignElements(IdentifiedElement):

    def __init__(self, agregationType: str, rdal_ReferencedDesignElements: "rdal_TraceableToDesignElementsElement" = None, parent145: set["rdal_DesignElementReference"] = None, ReferencedDesignElements: "rdal_DesignElementReference" = None):
        self.agregationType = agregationType
        self.rdal_ReferencedDesignElements = rdal_ReferencedDesignElements
        self.parent145 = parent145 if parent145 is not None else set()
        self.ReferencedDesignElements = ReferencedDesignElements
        
        pass
    @property
    def agregationType(self):
        return self.__agregationType

    @agregationType.setter
    def agregationType(self, agregationType: str):
        self.__agregationType = agregationType


    @property
    def rdal_ReferencedDesignElements(self):
        return self.__rdal_ReferencedDesignElements

    @rdal_ReferencedDesignElements.setter
    def rdal_ReferencedDesignElements(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdal_ReferencedDesignElements__rdal_ReferencedDesignElements", None)
        self.__rdal_ReferencedDesignElements = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdal_TraceableToDesignElementsElement"):
                opp_val = getattr(old_value, "rdal_TraceableToDesignElementsElement", None)
                if opp_val == self:
                    setattr(old_value, "rdal_TraceableToDesignElementsElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdal_TraceableToDesignElementsElement"):
                opp_val = getattr(value, "rdal_TraceableToDesignElementsElement", None)
                setattr(value, "rdal_TraceableToDesignElementsElement", self)

    @property
    def ReferencedDesignElements(self):
        return self.__ReferencedDesignElements

    @ReferencedDesignElements.setter
    def ReferencedDesignElements(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdal_ReferencedDesignElements__ReferencedDesignElements", None)
        self.__ReferencedDesignElements = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownedDesignElementRefs"):
                opp_val = getattr(old_value, "ownedDesignElementRefs", None)
                if opp_val == self:
                    setattr(old_value, "ownedDesignElementRefs", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedDesignElementRefs"):
                opp_val = getattr(value, "ownedDesignElementRefs", None)
                setattr(value, "ownedDesignElementRefs", self)

    @property
    def parent145(self):
        return self.__parent145

    @parent145.setter
    def parent145(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdal_ReferencedDesignElements__parent145", None)
        self.__parent145 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DesignElementReference"):
                    opp_val = getattr(item, "DesignElementReference", None)
                    
                    if opp_val == self:
                        setattr(item, "DesignElementReference", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DesignElementReference"):
                    opp_val = getattr(item, "DesignElementReference", None)
                    
                    setattr(item, "DesignElementReference", self)
                    

class rdal_RequirementsCoverageData(IdentifiedElement):

    def __init__(self, nbRequirements: int, verificationLevel: str):
        self.nbRequirements = nbRequirements
        self.verificationLevel = verificationLevel
        
        pass
    @property
    def verificationLevel(self):
        return self.__verificationLevel

    @verificationLevel.setter
    def verificationLevel(self, verificationLevel: str):
        self.__verificationLevel = verificationLevel


    @property
    def nbRequirements(self):
        return self.__nbRequirements

    @nbRequirements.setter
    def nbRequirements(self, nbRequirements: int):
        self.__nbRequirements = nbRequirements


class rdal_DesignElementReference(IdentifiedElement):

    def __init__(self, evaluationResult: str, DesignElementReference: "rdal_ReferencedDesignElements" = None, rdal_DesignElementReference: "rdal_EObject" = None, ownedDesignElementRefs: "rdal_ReferencedDesignElements" = None, rdal_DesignElementReference150: "rdal_TraceableToDesignElementsElement" = None):
        self.evaluationResult = evaluationResult
        self.DesignElementReference = DesignElementReference
        self.rdal_DesignElementReference = rdal_DesignElementReference
        self.ownedDesignElementRefs = ownedDesignElementRefs
        self.rdal_DesignElementReference150 = rdal_DesignElementReference150
        
        pass
    @property
    def evaluationResult(self):
        return self.__evaluationResult

    @evaluationResult.setter
    def evaluationResult(self, evaluationResult: str):
        self.__evaluationResult = evaluationResult


    @property
    def ownedDesignElementRefs(self):
        return self.__ownedDesignElementRefs

    @ownedDesignElementRefs.setter
    def ownedDesignElementRefs(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdal_DesignElementReference__ownedDesignElementRefs", None)
        self.__ownedDesignElementRefs = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ReferencedDesignElements"):
                opp_val = getattr(old_value, "ReferencedDesignElements", None)
                if opp_val == self:
                    setattr(old_value, "ReferencedDesignElements", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ReferencedDesignElements"):
                opp_val = getattr(value, "ReferencedDesignElements", None)
                setattr(value, "ReferencedDesignElements", self)

    @property
    def DesignElementReference(self):
        return self.__DesignElementReference

    @DesignElementReference.setter
    def DesignElementReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdal_DesignElementReference__DesignElementReference", None)
        self.__DesignElementReference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent145"):
                opp_val = getattr(old_value, "parent145", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent145"):
                opp_val = getattr(value, "parent145", None)
                if opp_val is None:
                    setattr(value, "parent145", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rdal_DesignElementReference(self):
        return self.__rdal_DesignElementReference

    @rdal_DesignElementReference.setter
    def rdal_DesignElementReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdal_DesignElementReference__rdal_DesignElementReference", None)
        self.__rdal_DesignElementReference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdal_EObject147"):
                opp_val = getattr(old_value, "rdal_EObject147", None)
                if opp_val == self:
                    setattr(old_value, "rdal_EObject147", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdal_EObject147"):
                opp_val = getattr(value, "rdal_EObject147", None)
                setattr(value, "rdal_EObject147", self)

    @property
    def rdal_DesignElementReference150(self):
        return self.__rdal_DesignElementReference150

    @rdal_DesignElementReference150.setter
    def rdal_DesignElementReference150(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdal_DesignElementReference__rdal_DesignElementReference150", None)
        self.__rdal_DesignElementReference150 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdal_TraceableToDesignElementsElement151"):
                opp_val = getattr(old_value, "rdal_TraceableToDesignElementsElement151", None)
                if opp_val == self:
                    setattr(old_value, "rdal_TraceableToDesignElementsElement151", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdal_TraceableToDesignElementsElement151"):
                opp_val = getattr(value, "rdal_TraceableToDesignElementsElement151", None)
                setattr(value, "rdal_TraceableToDesignElementsElement151", self)

class rdal_TraceableToDesignElementsElement(IdentifiedElement):

    pass
class rdal_ContactInformation(IdentifiedElement):

    def __init__(self, address: str, email: str, phoneNumber: str, country: str, rdal_ContactInformation: "rdal_AbstractContractualElement" = None, rdal_ContactInformation37: "rdal_Stakeholder" = None, rdal_ContactInformation53: "rdal_Specification" = None):
        self.address = address
        self.email = email
        self.phoneNumber = phoneNumber
        self.country = country
        self.rdal_ContactInformation = rdal_ContactInformation
        self.rdal_ContactInformation37 = rdal_ContactInformation37
        self.rdal_ContactInformation53 = rdal_ContactInformation53
        
        pass
    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address


    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, country: str):
        self.__country = country


    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email


    @property
    def phoneNumber(self):
        return self.__phoneNumber

    @phoneNumber.setter
    def phoneNumber(self, phoneNumber: str):
        self.__phoneNumber = phoneNumber


    @property
    def rdal_ContactInformation37(self):
        return self.__rdal_ContactInformation37

    @rdal_ContactInformation37.setter
    def rdal_ContactInformation37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdal_ContactInformation__rdal_ContactInformation37", None)
        self.__rdal_ContactInformation37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdal_Stakeholder36"):
                opp_val = getattr(old_value, "rdal_Stakeholder36", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdal_Stakeholder36"):
                opp_val = getattr(value, "rdal_Stakeholder36", None)
                if opp_val is None:
                    setattr(value, "rdal_Stakeholder36", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rdal_ContactInformation(self):
        return self.__rdal_ContactInformation

    @rdal_ContactInformation.setter
    def rdal_ContactInformation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdal_ContactInformation__rdal_ContactInformation", None)
        self.__rdal_ContactInformation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdal_AbstractContractualElement26"):
                opp_val = getattr(old_value, "rdal_AbstractContractualElement26", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdal_AbstractContractualElement26"):
                opp_val = getattr(value, "rdal_AbstractContractualElement26", None)
                if opp_val is None:
                    setattr(value, "rdal_AbstractContractualElement26", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rdal_ContactInformation53(self):
        return self.__rdal_ContactInformation53

    @rdal_ContactInformation53.setter
    def rdal_ContactInformation53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdal_ContactInformation__rdal_ContactInformation53", None)
        self.__rdal_ContactInformation53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdal_Specification52"):
                opp_val = getattr(old_value, "rdal_Specification52", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdal_Specification52"):
                opp_val = getattr(value, "rdal_Specification52", None)
                if opp_val is None:
                    setattr(value, "rdal_Specification52", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class rdal_Conflict(IdentifiedElement):

    def __init__(self, degree: str, rdal_Conflict: "rdal_Specification" = None, Conflict: "rdal_AbstractGoal" = None, conflicts: "rdal_AbstractGoal" = None, rdal_Conflict142: "rdal_AbstractContractualElement" = None):
        self.degree = degree
        self.rdal_Conflict = rdal_Conflict
        self.Conflict = Conflict
        self.conflicts = conflicts
        self.rdal_Conflict142 = rdal_Conflict142
        
        pass
    @property
    def degree(self):
        return self.__degree

    @degree.setter
    def degree(self, degree: str):
        self.__degree = degree


    @property
    def rdal_Conflict(self):
        return self.__rdal_Conflict

    @rdal_Conflict.setter
    def rdal_Conflict(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdal_Conflict__rdal_Conflict", None)
        self.__rdal_Conflict = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdal_Specification55"):
                opp_val = getattr(old_value, "rdal_Specification55", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdal_Specification55"):
                opp_val = getattr(value, "rdal_Specification55", None)
                if opp_val is None:
                    setattr(value, "rdal_Specification55", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Conflict(self):
        return self.__Conflict

    @Conflict.setter
    def Conflict(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdal_Conflict__Conflict", None)
        self.__Conflict = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "goal"):
                opp_val = getattr(old_value, "goal", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "goal"):
                opp_val = getattr(value, "goal", None)
                if opp_val is None:
                    setattr(value, "goal", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def conflicts(self):
        return self.__conflicts

    @conflicts.setter
    def conflicts(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdal_Conflict__conflicts", None)
        self.__conflicts = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AbstractGoal140"):
                opp_val = getattr(old_value, "AbstractGoal140", None)
                if opp_val == self:
                    setattr(old_value, "AbstractGoal140", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AbstractGoal140"):
                opp_val = getattr(value, "AbstractGoal140", None)
                setattr(value, "AbstractGoal140", self)

    @property
    def rdal_Conflict142(self):
        return self.__rdal_Conflict142

    @rdal_Conflict142.setter
    def rdal_Conflict142(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdal_Conflict__rdal_Conflict142", None)
        self.__rdal_Conflict142 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdal_AbstractContractualElement143"):
                opp_val = getattr(old_value, "rdal_AbstractContractualElement143", None)
                if opp_val == self:
                    setattr(old_value, "rdal_AbstractContractualElement143", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdal_AbstractContractualElement143"):
                opp_val = getattr(value, "rdal_AbstractContractualElement143", None)
                setattr(value, "rdal_AbstractContractualElement143", self)

class rdal_SubElementReference(IdentifiedElement):

    def __init__(self, weight: str, referencedElementEntries: str, rdal_SubElementReference: "rdal_ElementRefinement" = None, rdal_SubElementReference159: "rdal_RefineableElement" = None):
        self.weight = weight
        self.referencedElementEntries = referencedElementEntries
        self.rdal_SubElementReference = rdal_SubElementReference
        self.rdal_SubElementReference159 = rdal_SubElementReference159
        
        pass
    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight: str):
        self.__weight = weight


    @property
    def referencedElementEntries(self):
        return self.__referencedElementEntries

    @referencedElementEntries.setter
    def referencedElementEntries(self, referencedElementEntries: str):
        self.__referencedElementEntries = referencedElementEntries


    @property
    def rdal_SubElementReference159(self):
        return self.__rdal_SubElementReference159

    @rdal_SubElementReference159.setter
    def rdal_SubElementReference159(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdal_SubElementReference__rdal_SubElementReference159", None)
        self.__rdal_SubElementReference159 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdal_RefineableElement160"):
                opp_val = getattr(old_value, "rdal_RefineableElement160", None)
                if opp_val == self:
                    setattr(old_value, "rdal_RefineableElement160", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdal_RefineableElement160"):
                opp_val = getattr(value, "rdal_RefineableElement160", None)
                setattr(value, "rdal_RefineableElement160", self)

    @property
    def rdal_SubElementReference(self):
        return self.__rdal_SubElementReference

    @rdal_SubElementReference.setter
    def rdal_SubElementReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdal_SubElementReference__rdal_SubElementReference", None)
        self.__rdal_SubElementReference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdal_ElementRefinement3"):
                opp_val = getattr(old_value, "rdal_ElementRefinement3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdal_ElementRefinement3"):
                opp_val = getattr(value, "rdal_ElementRefinement3", None)
                if opp_val is None:
                    setattr(value, "rdal_ElementRefinement3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class rdal_Variable(IdentifiedElement):

    pass
class rdal_Uncertainty(IdentifiedElement):

    def __init__(self, volatility: str, costsImpact: str, scheduleImpact: str, timeCriticality: str, familiarity: str, riskIndex: str, propRiskIndex: str, maturityIndex: str, rdal_Uncertainty: "rdal_AbstractContractualElement" = None):
        self.volatility = volatility
        self.costsImpact = costsImpact
        self.scheduleImpact = scheduleImpact
        self.timeCriticality = timeCriticality
        self.familiarity = familiarity
        self.riskIndex = riskIndex
        self.propRiskIndex = propRiskIndex
        self.maturityIndex = maturityIndex
        self.rdal_Uncertainty = rdal_Uncertainty
        
        pass
    @property
    def costsImpact(self):
        return self.__costsImpact

    @costsImpact.setter
    def costsImpact(self, costsImpact: str):
        self.__costsImpact = costsImpact


    @property
    def propRiskIndex(self):
        return self.__propRiskIndex

    @propRiskIndex.setter
    def propRiskIndex(self, propRiskIndex: str):
        self.__propRiskIndex = propRiskIndex


    @property
    def riskIndex(self):
        return self.__riskIndex

    @riskIndex.setter
    def riskIndex(self, riskIndex: str):
        self.__riskIndex = riskIndex


    @property
    def maturityIndex(self):
        return self.__maturityIndex

    @maturityIndex.setter
    def maturityIndex(self, maturityIndex: str):
        self.__maturityIndex = maturityIndex


    @property
    def scheduleImpact(self):
        return self.__scheduleImpact

    @scheduleImpact.setter
    def scheduleImpact(self, scheduleImpact: str):
        self.__scheduleImpact = scheduleImpact


    @property
    def timeCriticality(self):
        return self.__timeCriticality

    @timeCriticality.setter
    def timeCriticality(self, timeCriticality: str):
        self.__timeCriticality = timeCriticality


    @property
    def familiarity(self):
        return self.__familiarity

    @familiarity.setter
    def familiarity(self, familiarity: str):
        self.__familiarity = familiarity


    @property
    def volatility(self):
        return self.__volatility

    @volatility.setter
    def volatility(self, volatility: str):
        self.__volatility = volatility


    @property
    def rdal_Uncertainty(self):
        return self.__rdal_Uncertainty

    @rdal_Uncertainty.setter
    def rdal_Uncertainty(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdal_Uncertainty__rdal_Uncertainty", None)
        self.__rdal_Uncertainty = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdal_AbstractContractualElement34"):
                opp_val = getattr(old_value, "rdal_AbstractContractualElement34", None)
                if opp_val == self:
                    setattr(old_value, "rdal_AbstractContractualElement34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdal_AbstractContractualElement34"):
                opp_val = getattr(value, "rdal_AbstractContractualElement34", None)
                setattr(value, "rdal_AbstractContractualElement34", self)

class rdal_Rationale(IdentifiedElement):

    pass
class rdal_ActorReference(IdentifiedElement):

    pass
class rdal_Stakeholder(IdentifiedElement):

    pass
class rdal_VerificationActivity(IdentifiedElement):

    def __init__(self, passed: bool, VerificationActivity: "rdal_AbstractRequirement" = None, rdal_VerificationActivity: set["rdal_EObject"] = None, ownedVerifiedBy: "rdal_AbstractRequirement" = None, rdal_VerificationActivity123: "rdal_Category" = None):
        self.passed = passed
        self.VerificationActivity = VerificationActivity
        self.rdal_VerificationActivity = rdal_VerificationActivity if rdal_VerificationActivity is not None else set()
        self.ownedVerifiedBy = ownedVerifiedBy
        self.rdal_VerificationActivity123 = rdal_VerificationActivity123
        
        pass
    @property
    def passed(self):
        return self.__passed

    @passed.setter
    def passed(self, passed: bool):
        self.__passed = passed


    @property
    def rdal_VerificationActivity123(self):
        return self.__rdal_VerificationActivity123

    @rdal_VerificationActivity123.setter
    def rdal_VerificationActivity123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdal_VerificationActivity__rdal_VerificationActivity123", None)
        self.__rdal_VerificationActivity123 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdal_Category124"):
                opp_val = getattr(old_value, "rdal_Category124", None)
                if opp_val == self:
                    setattr(old_value, "rdal_Category124", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdal_Category124"):
                opp_val = getattr(value, "rdal_Category124", None)
                setattr(value, "rdal_Category124", self)

    @property
    def VerificationActivity(self):
        return self.__VerificationActivity

    @VerificationActivity.setter
    def VerificationActivity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdal_VerificationActivity__VerificationActivity", None)
        self.__VerificationActivity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "requirements"):
                opp_val = getattr(old_value, "requirements", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "requirements"):
                opp_val = getattr(value, "requirements", None)
                if opp_val is None:
                    setattr(value, "requirements", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ownedVerifiedBy(self):
        return self.__ownedVerifiedBy

    @ownedVerifiedBy.setter
    def ownedVerifiedBy(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdal_VerificationActivity__ownedVerifiedBy", None)
        self.__ownedVerifiedBy = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AbstractRequirement121"):
                opp_val = getattr(old_value, "AbstractRequirement121", None)
                if opp_val == self:
                    setattr(old_value, "AbstractRequirement121", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AbstractRequirement121"):
                opp_val = getattr(value, "AbstractRequirement121", None)
                setattr(value, "AbstractRequirement121", self)

    @property
    def rdal_VerificationActivity(self):
        return self.__rdal_VerificationActivity

    @rdal_VerificationActivity.setter
    def rdal_VerificationActivity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdal_VerificationActivity__rdal_VerificationActivity", None)
        self.__rdal_VerificationActivity = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rdal_EObject119"):
                    opp_val = getattr(item, "rdal_EObject119", None)
                    
                    if opp_val == self:
                        setattr(item, "rdal_EObject119", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rdal_EObject119"):
                    opp_val = getattr(item, "rdal_EObject119", None)
                    
                    setattr(item, "rdal_EObject119", self)
                    

class rdal_Capability(IdentifiedElement):

    pass
class rdal_NonFunctionalProperty(IdentifiedElement):

    pass
class rdal_ElementRefinement(IdentifiedElement):

    def __init__(self, subElementRefEntries: str, refinedElementEntries: str, rdal_ElementRefinement: set["rdal_RefineableElement"] = None, rdal_ElementRefinement3: set["rdal_SubElementReference"] = None, rdal_ElementRefinement5: "rdal_RefineableElement" = None, rdal_ElementRefinement77: "rdal_RdalOrgPackage" = None):
        self.subElementRefEntries = subElementRefEntries
        self.refinedElementEntries = refinedElementEntries
        self.rdal_ElementRefinement = rdal_ElementRefinement if rdal_ElementRefinement is not None else set()
        self.rdal_ElementRefinement3 = rdal_ElementRefinement3 if rdal_ElementRefinement3 is not None else set()
        self.rdal_ElementRefinement5 = rdal_ElementRefinement5
        self.rdal_ElementRefinement77 = rdal_ElementRefinement77
        
        pass
    @property
    def refinedElementEntries(self):
        return self.__refinedElementEntries

    @refinedElementEntries.setter
    def refinedElementEntries(self, refinedElementEntries: str):
        self.__refinedElementEntries = refinedElementEntries


    @property
    def subElementRefEntries(self):
        return self.__subElementRefEntries

    @subElementRefEntries.setter
    def subElementRefEntries(self, subElementRefEntries: str):
        self.__subElementRefEntries = subElementRefEntries


    @property
    def rdal_ElementRefinement(self):
        return self.__rdal_ElementRefinement

    @rdal_ElementRefinement.setter
    def rdal_ElementRefinement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdal_ElementRefinement__rdal_ElementRefinement", None)
        self.__rdal_ElementRefinement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rdal_RefineableElement"):
                    opp_val = getattr(item, "rdal_RefineableElement", None)
                    
                    if opp_val == self:
                        setattr(item, "rdal_RefineableElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rdal_RefineableElement"):
                    opp_val = getattr(item, "rdal_RefineableElement", None)
                    
                    setattr(item, "rdal_RefineableElement", self)
                    

    @property
    def rdal_ElementRefinement3(self):
        return self.__rdal_ElementRefinement3

    @rdal_ElementRefinement3.setter
    def rdal_ElementRefinement3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdal_ElementRefinement__rdal_ElementRefinement3", None)
        self.__rdal_ElementRefinement3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rdal_SubElementReference"):
                    opp_val = getattr(item, "rdal_SubElementReference", None)
                    
                    if opp_val == self:
                        setattr(item, "rdal_SubElementReference", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rdal_SubElementReference"):
                    opp_val = getattr(item, "rdal_SubElementReference", None)
                    
                    setattr(item, "rdal_SubElementReference", self)
                    

    @property
    def rdal_ElementRefinement5(self):
        return self.__rdal_ElementRefinement5

    @rdal_ElementRefinement5.setter
    def rdal_ElementRefinement5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdal_ElementRefinement__rdal_ElementRefinement5", None)
        self.__rdal_ElementRefinement5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdal_RefineableElement6"):
                opp_val = getattr(old_value, "rdal_RefineableElement6", None)
                if opp_val == self:
                    setattr(old_value, "rdal_RefineableElement6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdal_RefineableElement6"):
                opp_val = getattr(value, "rdal_RefineableElement6", None)
                setattr(value, "rdal_RefineableElement6", self)

    @property
    def rdal_ElementRefinement77(self):
        return self.__rdal_ElementRefinement77

    @rdal_ElementRefinement77.setter
    def rdal_ElementRefinement77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdal_ElementRefinement__rdal_ElementRefinement77", None)
        self.__rdal_ElementRefinement77 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdal_RdalOrgPackage"):
                opp_val = getattr(old_value, "rdal_RdalOrgPackage", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdal_RdalOrgPackage"):
                opp_val = getattr(value, "rdal_RdalOrgPackage", None)
                if opp_val is None:
                    setattr(value, "rdal_RdalOrgPackage", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class rdal_UserProperty:

    def __init__(self, value: str, name: str, rdal_UserProperty: "rdal_IdentifiedElement" = None):
        self.value = value
        self.name = name
        self.rdal_UserProperty = rdal_UserProperty
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def rdal_UserProperty(self):
        return self.__rdal_UserProperty

    @rdal_UserProperty.setter
    def rdal_UserProperty(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdal_UserProperty__rdal_UserProperty", None)
        self.__rdal_UserProperty = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdal_IdentifiedElement"):
                opp_val = getattr(old_value, "rdal_IdentifiedElement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdal_IdentifiedElement"):
                opp_val = getattr(value, "rdal_IdentifiedElement", None)
                if opp_val is None:
                    setattr(value, "rdal_IdentifiedElement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class rdal_IdentifiedElement(ABC):

    def __init__(self, name: str, id: str, description: str, rdal_IdentifiedElement: set["rdal_UserProperty"] = None):
        self.name = name
        self.id = id
        self.description = description
        self.rdal_IdentifiedElement = rdal_IdentifiedElement if rdal_IdentifiedElement is not None else set()
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def rdal_IdentifiedElement(self):
        return self.__rdal_IdentifiedElement

    @rdal_IdentifiedElement.setter
    def rdal_IdentifiedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdal_IdentifiedElement__rdal_IdentifiedElement", None)
        self.__rdal_IdentifiedElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rdal_UserProperty"):
                    opp_val = getattr(item, "rdal_UserProperty", None)
                    
                    if opp_val == self:
                        setattr(item, "rdal_UserProperty", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rdal_UserProperty"):
                    opp_val = getattr(item, "rdal_UserProperty", None)
                    
                    setattr(item, "rdal_UserProperty", self)
                    
