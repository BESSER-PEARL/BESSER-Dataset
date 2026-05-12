from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class VerificationMethod(Enum):
    Analysis = "Analysis"
    Demonstration = "Demonstration"
    Inspection = "Inspection"
    Test = "Test"
class Direction(Enum):
    In = "In"
    Out = "Out"
    InOut = "InOut"
class RiskKind(Enum):
    High = "High"
    Medium = "Medium"
    Low = "Low"
class AssumptionType(Enum):
    Managerial = "Managerial"
    Technical = "Technical"
    Organizational = "Organizational"
class AgregationType(Enum):
    Composition = "Composition"
    Alternative = "Alternative"
class VariableType(Enum):
    Monitored = "Monitored"
    Controlled = "Controlled"
    Both = "Both"


############################################
# Definition of Classes
############################################

class RequirementsCoverageData:

    pass
class ModelElementReference:

    pass
class core_TraceModelElementReference(RequirementsCoverageData, ModelElementReference):

    def __init__(self, container: bool):
        self.container = container
        
        pass
    @property
    def container(self):
        return self.__container

    @container.setter
    def container(self, container: bool):
        self.__container = container


    def merge(self, core_modelElementReference):
        # TODO: Implement merge method
        pass

class core_FormalLanguageExpression:

    pass
class ReferencedModelElements:

    pass
class core_Trace(ReferencedModelElements):

    def __init__(self, core_Trace: set["core_Specification"] = None):
        self.core_Trace = core_Trace if core_Trace is not None else set()
        
        pass
    @property
    def core_Trace(self):
        return self.__core_Trace

    @core_Trace.setter
    def core_Trace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_Trace__core_Trace", None)
        self.__core_Trace = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core_Specification114"):
                    opp_val = getattr(item, "core_Specification114", None)
                    
                    if opp_val == self:
                        setattr(item, "core_Specification114", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core_Specification114"):
                    opp_val = getattr(item, "core_Specification114", None)
                    
                    setattr(item, "core_Specification114", self)
                    

    def modelElementReference(self, core_modelElement) :
        # TODO: Implement modelElementReference method
        pass

class core_RefUserSelectedModelElements(ReferencedModelElements):

    pass
class core_RefDerivedModelElements(ReferencedModelElements):

    pass
class core_RefExpressionCollectedModelElements(ReferencedModelElements):

    pass
class Actor:

    pass
class AbstractRequirement:

    pass
class core_Assumption(AbstractRequirement):

    def __init__(self, type: str, Assumption: "core_Requirement" = None, Assumption96: "core_Requirement" = None, assumptions: "core_Requirement" = None, imageAssumption: "core_Requirement" = None):
        self.type = type
        self.Assumption = Assumption
        self.Assumption96 = Assumption96
        self.assumptions = assumptions
        self.imageAssumption = imageAssumption
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def Assumption(self):
        return self.__Assumption

    @Assumption.setter
    def Assumption(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_Assumption__Assumption", None)
        self.__Assumption = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "requirements94"):
                opp_val = getattr(old_value, "requirements94", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "requirements94"):
                opp_val = getattr(value, "requirements94", None)
                if opp_val is None:
                    setattr(value, "requirements94", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def imageAssumption(self):
        return self.__imageAssumption

    @imageAssumption.setter
    def imageAssumption(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_Assumption__imageAssumption", None)
        self.__imageAssumption = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Requirement102"):
                opp_val = getattr(old_value, "Requirement102", None)
                if opp_val == self:
                    setattr(old_value, "Requirement102", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Requirement102"):
                opp_val = getattr(value, "Requirement102", None)
                setattr(value, "Requirement102", self)

    @property
    def assumptions(self):
        return self.__assumptions

    @assumptions.setter
    def assumptions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_Assumption__assumptions", None)
        self.__assumptions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Requirement"):
                opp_val = getattr(old_value, "Requirement", None)
                if opp_val == self:
                    setattr(old_value, "Requirement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Requirement"):
                opp_val = getattr(value, "Requirement", None)
                setattr(value, "Requirement", self)

    @property
    def Assumption96(self):
        return self.__Assumption96

    @Assumption96.setter
    def Assumption96(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_Assumption__Assumption96", None)
        self.__Assumption96 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "imageRequirement"):
                opp_val = getattr(old_value, "imageRequirement", None)
                if opp_val == self:
                    setattr(old_value, "imageRequirement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "imageRequirement"):
                opp_val = getattr(value, "imageRequirement", None)
                setattr(value, "imageRequirement", self)

class core_Requirement(AbstractRequirement):

    pass
class core_ConstraintLanguagesSpecification:

    pass
class VerifiableElement:

    pass
class core_AbstractRequirement(VerifiableElement):

    def __init__(self, risk: str, AbstractRequirement: "core_RequirementsGroup" = None, core_AbstractRequirement: "core_AbstractRequirement" = None, core_AbstractRequirement80: set["core_AbstractRequirement"] = None, requirement: set["core_VerificationActivity"] = None, requirements: "core_RequirementsGroup" = None, core_AbstractRequirement86: "core_Variable" = None, core_AbstractRequirement89: set["core_Variable"] = None, AbstractRequirement104: "core_VerificationActivity" = None):
        self.risk = risk
        self.AbstractRequirement = AbstractRequirement
        self.core_AbstractRequirement = core_AbstractRequirement
        self.core_AbstractRequirement80 = core_AbstractRequirement80 if core_AbstractRequirement80 is not None else set()
        self.requirement = requirement if requirement is not None else set()
        self.requirements = requirements
        self.core_AbstractRequirement86 = core_AbstractRequirement86
        self.core_AbstractRequirement89 = core_AbstractRequirement89 if core_AbstractRequirement89 is not None else set()
        self.AbstractRequirement104 = AbstractRequirement104
        
        pass
    @property
    def risk(self):
        return self.__risk

    @risk.setter
    def risk(self, risk: str):
        self.__risk = risk


    @property
    def core_AbstractRequirement89(self):
        return self.__core_AbstractRequirement89

    @core_AbstractRequirement89.setter
    def core_AbstractRequirement89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_AbstractRequirement__core_AbstractRequirement89", None)
        self.__core_AbstractRequirement89 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core_Variable90"):
                    opp_val = getattr(item, "core_Variable90", None)
                    
                    if opp_val == self:
                        setattr(item, "core_Variable90", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core_Variable90"):
                    opp_val = getattr(item, "core_Variable90", None)
                    
                    setattr(item, "core_Variable90", self)
                    

    @property
    def requirement(self):
        return self.__requirement

    @requirement.setter
    def requirement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_AbstractRequirement__requirement", None)
        self.__requirement = value if value is not None else set()
        
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
                    

    @property
    def AbstractRequirement104(self):
        return self.__AbstractRequirement104

    @AbstractRequirement104.setter
    def AbstractRequirement104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_AbstractRequirement__AbstractRequirement104", None)
        self.__AbstractRequirement104 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "verifiedBy"):
                opp_val = getattr(old_value, "verifiedBy", None)
                if opp_val == self:
                    setattr(old_value, "verifiedBy", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "verifiedBy"):
                opp_val = getattr(value, "verifiedBy", None)
                setattr(value, "verifiedBy", self)

    @property
    def requirements(self):
        return self.__requirements

    @requirements.setter
    def requirements(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_AbstractRequirement__requirements", None)
        self.__requirements = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RequirementsGroup84"):
                opp_val = getattr(old_value, "RequirementsGroup84", None)
                if opp_val == self:
                    setattr(old_value, "RequirementsGroup84", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RequirementsGroup84"):
                opp_val = getattr(value, "RequirementsGroup84", None)
                setattr(value, "RequirementsGroup84", self)

    @property
    def core_AbstractRequirement80(self):
        return self.__core_AbstractRequirement80

    @core_AbstractRequirement80.setter
    def core_AbstractRequirement80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_AbstractRequirement__core_AbstractRequirement80", None)
        self.__core_AbstractRequirement80 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core_AbstractRequirement"):
                    opp_val = getattr(item, "core_AbstractRequirement", None)
                    
                    if opp_val == self:
                        setattr(item, "core_AbstractRequirement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core_AbstractRequirement"):
                    opp_val = getattr(item, "core_AbstractRequirement", None)
                    
                    setattr(item, "core_AbstractRequirement", self)
                    

    @property
    def AbstractRequirement(self):
        return self.__AbstractRequirement

    @AbstractRequirement.setter
    def AbstractRequirement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_AbstractRequirement__AbstractRequirement", None)
        self.__AbstractRequirement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "group"):
                opp_val = getattr(old_value, "group", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "group"):
                opp_val = getattr(value, "group", None)
                if opp_val is None:
                    setattr(value, "group", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def core_AbstractRequirement86(self):
        return self.__core_AbstractRequirement86

    @core_AbstractRequirement86.setter
    def core_AbstractRequirement86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_AbstractRequirement__core_AbstractRequirement86", None)
        self.__core_AbstractRequirement86 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_Variable87"):
                opp_val = getattr(old_value, "core_Variable87", None)
                if opp_val == self:
                    setattr(old_value, "core_Variable87", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_Variable87"):
                opp_val = getattr(value, "core_Variable87", None)
                setattr(value, "core_Variable87", self)

    @property
    def core_AbstractRequirement(self):
        return self.__core_AbstractRequirement

    @core_AbstractRequirement.setter
    def core_AbstractRequirement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_AbstractRequirement__core_AbstractRequirement", None)
        self.__core_AbstractRequirement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_AbstractRequirement80"):
                opp_val = getattr(old_value, "core_AbstractRequirement80", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_AbstractRequirement80"):
                opp_val = getattr(value, "core_AbstractRequirement80", None)
                if opp_val is None:
                    setattr(value, "core_AbstractRequirement80", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class core_Specification(VerifiableElement):

    def __init__(self, version: str, core_Specification: set["core_Actor"] = None, core_Specification31: "core_SystemOverview" = None, specification: set["core_RequirementsGroup"] = None, Specification: "core_RequirementsGroup" = None, core_Specification114: "core_Trace" = None, core_Specification34: set["core_VerificationActivity"] = None, core_Specification36: set["core_Conflict"] = None, core_Specification38: "core_ConstraintLanguagesSpecification" = None, core_Specification40: set["core_EObject"] = None, core_Specification43: set["core_EObject"] = None):
        self.version = version
        self.core_Specification = core_Specification if core_Specification is not None else set()
        self.core_Specification31 = core_Specification31
        self.specification = specification if specification is not None else set()
        self.Specification = Specification
        self.core_Specification114 = core_Specification114
        self.core_Specification34 = core_Specification34 if core_Specification34 is not None else set()
        self.core_Specification36 = core_Specification36 if core_Specification36 is not None else set()
        self.core_Specification38 = core_Specification38
        self.core_Specification40 = core_Specification40 if core_Specification40 is not None else set()
        self.core_Specification43 = core_Specification43 if core_Specification43 is not None else set()
        
        pass
    @property
    def version(self):
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version


    @property
    def core_Specification38(self):
        return self.__core_Specification38

    @core_Specification38.setter
    def core_Specification38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_Specification__core_Specification38", None)
        self.__core_Specification38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_ConstraintLanguagesSpecification"):
                opp_val = getattr(old_value, "core_ConstraintLanguagesSpecification", None)
                if opp_val == self:
                    setattr(old_value, "core_ConstraintLanguagesSpecification", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_ConstraintLanguagesSpecification"):
                opp_val = getattr(value, "core_ConstraintLanguagesSpecification", None)
                setattr(value, "core_ConstraintLanguagesSpecification", self)

    @property
    def core_Specification(self):
        return self.__core_Specification

    @core_Specification.setter
    def core_Specification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_Specification__core_Specification", None)
        self.__core_Specification = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core_Actor29"):
                    opp_val = getattr(item, "core_Actor29", None)
                    
                    if opp_val == self:
                        setattr(item, "core_Actor29", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core_Actor29"):
                    opp_val = getattr(item, "core_Actor29", None)
                    
                    setattr(item, "core_Actor29", self)
                    

    @property
    def core_Specification43(self):
        return self.__core_Specification43

    @core_Specification43.setter
    def core_Specification43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_Specification__core_Specification43", None)
        self.__core_Specification43 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core_EObject44"):
                    opp_val = getattr(item, "core_EObject44", None)
                    
                    if opp_val == self:
                        setattr(item, "core_EObject44", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core_EObject44"):
                    opp_val = getattr(item, "core_EObject44", None)
                    
                    setattr(item, "core_EObject44", self)
                    

    @property
    def core_Specification40(self):
        return self.__core_Specification40

    @core_Specification40.setter
    def core_Specification40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_Specification__core_Specification40", None)
        self.__core_Specification40 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core_EObject41"):
                    opp_val = getattr(item, "core_EObject41", None)
                    
                    if opp_val == self:
                        setattr(item, "core_EObject41", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core_EObject41"):
                    opp_val = getattr(item, "core_EObject41", None)
                    
                    setattr(item, "core_EObject41", self)
                    

    @property
    def core_Specification36(self):
        return self.__core_Specification36

    @core_Specification36.setter
    def core_Specification36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_Specification__core_Specification36", None)
        self.__core_Specification36 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core_Conflict"):
                    opp_val = getattr(item, "core_Conflict", None)
                    
                    if opp_val == self:
                        setattr(item, "core_Conflict", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core_Conflict"):
                    opp_val = getattr(item, "core_Conflict", None)
                    
                    setattr(item, "core_Conflict", self)
                    

    @property
    def Specification(self):
        return self.__Specification

    @Specification.setter
    def Specification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_Specification__Specification", None)
        self.__Specification = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "requirementGroups"):
                opp_val = getattr(old_value, "requirementGroups", None)
                if opp_val == self:
                    setattr(old_value, "requirementGroups", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "requirementGroups"):
                opp_val = getattr(value, "requirementGroups", None)
                setattr(value, "requirementGroups", self)

    @property
    def core_Specification31(self):
        return self.__core_Specification31

    @core_Specification31.setter
    def core_Specification31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_Specification__core_Specification31", None)
        self.__core_Specification31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_SystemOverview"):
                opp_val = getattr(old_value, "core_SystemOverview", None)
                if opp_val == self:
                    setattr(old_value, "core_SystemOverview", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_SystemOverview"):
                opp_val = getattr(value, "core_SystemOverview", None)
                setattr(value, "core_SystemOverview", self)

    @property
    def specification(self):
        return self.__specification

    @specification.setter
    def specification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_Specification__specification", None)
        self.__specification = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RequirementsGroup"):
                    opp_val = getattr(item, "RequirementsGroup", None)
                    
                    if opp_val == self:
                        setattr(item, "RequirementsGroup", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RequirementsGroup"):
                    opp_val = getattr(item, "RequirementsGroup", None)
                    
                    setattr(item, "RequirementsGroup", self)
                    

    @property
    def core_Specification34(self):
        return self.__core_Specification34

    @core_Specification34.setter
    def core_Specification34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_Specification__core_Specification34", None)
        self.__core_Specification34 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core_VerificationActivity"):
                    opp_val = getattr(item, "core_VerificationActivity", None)
                    
                    if opp_val == self:
                        setattr(item, "core_VerificationActivity", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core_VerificationActivity"):
                    opp_val = getattr(item, "core_VerificationActivity", None)
                    
                    setattr(item, "core_VerificationActivity", self)
                    

    @property
    def core_Specification114(self):
        return self.__core_Specification114

    @core_Specification114.setter
    def core_Specification114(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_Specification__core_Specification114", None)
        self.__core_Specification114 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_Trace"):
                opp_val = getattr(old_value, "core_Trace", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_Trace"):
                opp_val = getattr(value, "core_Trace", None)
                if opp_val is None:
                    setattr(value, "core_Trace", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ContractualElement:

    pass
class core_Goal(ContractualElement):

    def __init__(self, priority: str, core_Goal: "core_SystemOverview" = None, goals: set["core_Conflict"] = None, Goal: "core_Conflict" = None):
        self.priority = priority
        self.core_Goal = core_Goal
        self.goals = goals if goals is not None else set()
        self.Goal = Goal
        
        pass
    @property
    def priority(self):
        return self.__priority

    @priority.setter
    def priority(self, priority: str):
        self.__priority = priority


    @property
    def core_Goal(self):
        return self.__core_Goal

    @core_Goal.setter
    def core_Goal(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_Goal__core_Goal", None)
        self.__core_Goal = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_SystemOverview46"):
                opp_val = getattr(old_value, "core_SystemOverview46", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_SystemOverview46"):
                opp_val = getattr(value, "core_SystemOverview46", None)
                if opp_val is None:
                    setattr(value, "core_SystemOverview46", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Goal(self):
        return self.__Goal

    @Goal.setter
    def Goal(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_Goal__Goal", None)
        self.__Goal = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "conflicts"):
                opp_val = getattr(old_value, "conflicts", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "conflicts"):
                opp_val = getattr(value, "conflicts", None)
                if opp_val is None:
                    setattr(value, "conflicts", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def goals(self):
        return self.__goals

    @goals.setter
    def goals(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_Goal__goals", None)
        self.__goals = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Conflict"):
                    opp_val = getattr(item, "Conflict", None)
                    
                    if opp_val == self:
                        setattr(item, "Conflict", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Conflict"):
                    opp_val = getattr(item, "Conflict", None)
                    
                    setattr(item, "Conflict", self)
                    

class core_VerifiableElement(ContractualElement):

    def __init__(self, verified: str):
        self.verified = verified
        
        pass
    @property
    def verified(self):
        return self.__verified

    @verified.setter
    def verified(self, verified: str):
        self.__verified = verified


class core_RequirementsGroup(VerifiableElement):

    pass
class core_SystemOverview(ContractualElement):

    def __init__(self, purpose: str, capabilities: str, core_SystemOverview: "core_Specification" = None, core_SystemOverview46: set["core_Goal"] = None, core_SystemOverview48: "core_EObject" = None, core_SystemOverview51: set["core_SystemContext"] = None, core_SystemOverview53: set["core_Variable"] = None):
        self.purpose = purpose
        self.capabilities = capabilities
        self.core_SystemOverview = core_SystemOverview
        self.core_SystemOverview46 = core_SystemOverview46 if core_SystemOverview46 is not None else set()
        self.core_SystemOverview48 = core_SystemOverview48
        self.core_SystemOverview51 = core_SystemOverview51 if core_SystemOverview51 is not None else set()
        self.core_SystemOverview53 = core_SystemOverview53 if core_SystemOverview53 is not None else set()
        
        pass
    @property
    def capabilities(self):
        return self.__capabilities

    @capabilities.setter
    def capabilities(self, capabilities: str):
        self.__capabilities = capabilities


    @property
    def purpose(self):
        return self.__purpose

    @purpose.setter
    def purpose(self, purpose: str):
        self.__purpose = purpose


    @property
    def core_SystemOverview51(self):
        return self.__core_SystemOverview51

    @core_SystemOverview51.setter
    def core_SystemOverview51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_SystemOverview__core_SystemOverview51", None)
        self.__core_SystemOverview51 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core_SystemContext"):
                    opp_val = getattr(item, "core_SystemContext", None)
                    
                    if opp_val == self:
                        setattr(item, "core_SystemContext", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core_SystemContext"):
                    opp_val = getattr(item, "core_SystemContext", None)
                    
                    setattr(item, "core_SystemContext", self)
                    

    @property
    def core_SystemOverview53(self):
        return self.__core_SystemOverview53

    @core_SystemOverview53.setter
    def core_SystemOverview53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_SystemOverview__core_SystemOverview53", None)
        self.__core_SystemOverview53 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core_Variable"):
                    opp_val = getattr(item, "core_Variable", None)
                    
                    if opp_val == self:
                        setattr(item, "core_Variable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core_Variable"):
                    opp_val = getattr(item, "core_Variable", None)
                    
                    setattr(item, "core_Variable", self)
                    

    @property
    def core_SystemOverview46(self):
        return self.__core_SystemOverview46

    @core_SystemOverview46.setter
    def core_SystemOverview46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_SystemOverview__core_SystemOverview46", None)
        self.__core_SystemOverview46 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core_Goal"):
                    opp_val = getattr(item, "core_Goal", None)
                    
                    if opp_val == self:
                        setattr(item, "core_Goal", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core_Goal"):
                    opp_val = getattr(item, "core_Goal", None)
                    
                    setattr(item, "core_Goal", self)
                    

    @property
    def core_SystemOverview48(self):
        return self.__core_SystemOverview48

    @core_SystemOverview48.setter
    def core_SystemOverview48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_SystemOverview__core_SystemOverview48", None)
        self.__core_SystemOverview48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_EObject49"):
                opp_val = getattr(old_value, "core_EObject49", None)
                if opp_val == self:
                    setattr(old_value, "core_EObject49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_EObject49"):
                opp_val = getattr(value, "core_EObject49", None)
                setattr(value, "core_EObject49", self)

    @property
    def core_SystemOverview(self):
        return self.__core_SystemOverview

    @core_SystemOverview.setter
    def core_SystemOverview(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_SystemOverview__core_SystemOverview", None)
        self.__core_SystemOverview = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_Specification31"):
                opp_val = getattr(old_value, "core_Specification31", None)
                if opp_val == self:
                    setattr(old_value, "core_Specification31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_Specification31"):
                opp_val = getattr(value, "core_Specification31", None)
                setattr(value, "core_Specification31", self)

class core_Expression:

    pass
class core_Category:

    pass
class core_EObject:

    pass
class core_StakeHolder(Actor):

    pass
class IdentifiedElement:

    pass
class core_Uncertainty(IdentifiedElement):

    def __init__(self, precedence: str, riskIndex: str, volatility: str, costsImpact: str, scheduleImpact: str, propRiskIndex: str, maturityIndex: str, core_Uncertainty: "core_ContractualElement" = None):
        self.precedence = precedence
        self.riskIndex = riskIndex
        self.volatility = volatility
        self.costsImpact = costsImpact
        self.scheduleImpact = scheduleImpact
        self.propRiskIndex = propRiskIndex
        self.maturityIndex = maturityIndex
        self.core_Uncertainty = core_Uncertainty
        
        pass
    @property
    def riskIndex(self):
        return self.__riskIndex

    @riskIndex.setter
    def riskIndex(self, riskIndex: str):
        self.__riskIndex = riskIndex


    @property
    def costsImpact(self):
        return self.__costsImpact

    @costsImpact.setter
    def costsImpact(self, costsImpact: str):
        self.__costsImpact = costsImpact


    @property
    def volatility(self):
        return self.__volatility

    @volatility.setter
    def volatility(self, volatility: str):
        self.__volatility = volatility


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
    def precedence(self):
        return self.__precedence

    @precedence.setter
    def precedence(self, precedence: str):
        self.__precedence = precedence


    @property
    def propRiskIndex(self):
        return self.__propRiskIndex

    @propRiskIndex.setter
    def propRiskIndex(self, propRiskIndex: str):
        self.__propRiskIndex = propRiskIndex


    @property
    def core_Uncertainty(self):
        return self.__core_Uncertainty

    @core_Uncertainty.setter
    def core_Uncertainty(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_Uncertainty__core_Uncertainty", None)
        self.__core_Uncertainty = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_ContractualElement"):
                opp_val = getattr(old_value, "core_ContractualElement", None)
                if opp_val == self:
                    setattr(old_value, "core_ContractualElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_ContractualElement"):
                opp_val = getattr(value, "core_ContractualElement", None)
                setattr(value, "core_ContractualElement", self)

class core_Actor(IdentifiedElement):

    def __init__(self, address: str, email: str, phoneNumber: str, core_Actor: "core_ContractualElement" = None, core_Actor29: "core_Specification" = None, core_Actor59: "core_SystemContext" = None, core_Actor67: set["core_EObject"] = None, core_Actor70: set["core_Interaction"] = None):
        self.address = address
        self.email = email
        self.phoneNumber = phoneNumber
        self.core_Actor = core_Actor
        self.core_Actor29 = core_Actor29
        self.core_Actor59 = core_Actor59
        self.core_Actor67 = core_Actor67 if core_Actor67 is not None else set()
        self.core_Actor70 = core_Actor70 if core_Actor70 is not None else set()
        
        pass
    @property
    def phoneNumber(self):
        return self.__phoneNumber

    @phoneNumber.setter
    def phoneNumber(self, phoneNumber: str):
        self.__phoneNumber = phoneNumber


    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address


    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email


    @property
    def core_Actor29(self):
        return self.__core_Actor29

    @core_Actor29.setter
    def core_Actor29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_Actor__core_Actor29", None)
        self.__core_Actor29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_Specification"):
                opp_val = getattr(old_value, "core_Specification", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_Specification"):
                opp_val = getattr(value, "core_Specification", None)
                if opp_val is None:
                    setattr(value, "core_Specification", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def core_Actor(self):
        return self.__core_Actor

    @core_Actor.setter
    def core_Actor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_Actor__core_Actor", None)
        self.__core_Actor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_ContractualElement19"):
                opp_val = getattr(old_value, "core_ContractualElement19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_ContractualElement19"):
                opp_val = getattr(value, "core_ContractualElement19", None)
                if opp_val is None:
                    setattr(value, "core_ContractualElement19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def core_Actor67(self):
        return self.__core_Actor67

    @core_Actor67.setter
    def core_Actor67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_Actor__core_Actor67", None)
        self.__core_Actor67 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core_EObject68"):
                    opp_val = getattr(item, "core_EObject68", None)
                    
                    if opp_val == self:
                        setattr(item, "core_EObject68", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core_EObject68"):
                    opp_val = getattr(item, "core_EObject68", None)
                    
                    setattr(item, "core_EObject68", self)
                    

    @property
    def core_Actor59(self):
        return self.__core_Actor59

    @core_Actor59.setter
    def core_Actor59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_Actor__core_Actor59", None)
        self.__core_Actor59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_SystemContext58"):
                opp_val = getattr(old_value, "core_SystemContext58", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_SystemContext58"):
                opp_val = getattr(value, "core_SystemContext58", None)
                if opp_val is None:
                    setattr(value, "core_SystemContext58", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def core_Actor70(self):
        return self.__core_Actor70

    @core_Actor70.setter
    def core_Actor70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_Actor__core_Actor70", None)
        self.__core_Actor70 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core_Interaction"):
                    opp_val = getattr(item, "core_Interaction", None)
                    
                    if opp_val == self:
                        setattr(item, "core_Interaction", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core_Interaction"):
                    opp_val = getattr(item, "core_Interaction", None)
                    
                    setattr(item, "core_Interaction", self)
                    

class core_Variable(IdentifiedElement):

    def __init__(self, type: str, core_Variable87: "core_AbstractRequirement" = None, core_Variable90: "core_AbstractRequirement" = None, core_Variable116: "core_EObject" = None, core_Variable: "core_SystemOverview" = None, core_Variable62: "core_SystemContext" = None):
        self.type = type
        self.core_Variable87 = core_Variable87
        self.core_Variable90 = core_Variable90
        self.core_Variable116 = core_Variable116
        self.core_Variable = core_Variable
        self.core_Variable62 = core_Variable62
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def core_Variable(self):
        return self.__core_Variable

    @core_Variable.setter
    def core_Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_Variable__core_Variable", None)
        self.__core_Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_SystemOverview53"):
                opp_val = getattr(old_value, "core_SystemOverview53", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_SystemOverview53"):
                opp_val = getattr(value, "core_SystemOverview53", None)
                if opp_val is None:
                    setattr(value, "core_SystemOverview53", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def core_Variable62(self):
        return self.__core_Variable62

    @core_Variable62.setter
    def core_Variable62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_Variable__core_Variable62", None)
        self.__core_Variable62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_SystemContext61"):
                opp_val = getattr(old_value, "core_SystemContext61", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_SystemContext61"):
                opp_val = getattr(value, "core_SystemContext61", None)
                if opp_val is None:
                    setattr(value, "core_SystemContext61", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def core_Variable90(self):
        return self.__core_Variable90

    @core_Variable90.setter
    def core_Variable90(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_Variable__core_Variable90", None)
        self.__core_Variable90 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_AbstractRequirement89"):
                opp_val = getattr(old_value, "core_AbstractRequirement89", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_AbstractRequirement89"):
                opp_val = getattr(value, "core_AbstractRequirement89", None)
                if opp_val is None:
                    setattr(value, "core_AbstractRequirement89", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def core_Variable87(self):
        return self.__core_Variable87

    @core_Variable87.setter
    def core_Variable87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_Variable__core_Variable87", None)
        self.__core_Variable87 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_AbstractRequirement86"):
                opp_val = getattr(old_value, "core_AbstractRequirement86", None)
                if opp_val == self:
                    setattr(old_value, "core_AbstractRequirement86", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_AbstractRequirement86"):
                opp_val = getattr(value, "core_AbstractRequirement86", None)
                setattr(value, "core_AbstractRequirement86", self)

    @property
    def core_Variable116(self):
        return self.__core_Variable116

    @core_Variable116.setter
    def core_Variable116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_Variable__core_Variable116", None)
        self.__core_Variable116 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_EObject117"):
                opp_val = getattr(old_value, "core_EObject117", None)
                if opp_val == self:
                    setattr(old_value, "core_EObject117", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_EObject117"):
                opp_val = getattr(value, "core_EObject117", None)
                setattr(value, "core_EObject117", self)

class core_SystemContext(IdentifiedElement):

    pass
class core_ReferencedModelElements(IdentifiedElement):

    def __init__(self, agregationType: str, core_ReferencedModelElements: "core_ContractualElement" = None, parent: set["core_ModelElementReference"] = None, ReferencedModelElements: "core_ModelElementReference" = None):
        self.agregationType = agregationType
        self.core_ReferencedModelElements = core_ReferencedModelElements
        self.parent = parent if parent is not None else set()
        self.ReferencedModelElements = ReferencedModelElements
        
        pass
    @property
    def agregationType(self):
        return self.__agregationType

    @agregationType.setter
    def agregationType(self, agregationType: str):
        self.__agregationType = agregationType


    @property
    def core_ReferencedModelElements(self):
        return self.__core_ReferencedModelElements

    @core_ReferencedModelElements.setter
    def core_ReferencedModelElements(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_ReferencedModelElements__core_ReferencedModelElements", None)
        self.__core_ReferencedModelElements = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_ContractualElement10"):
                opp_val = getattr(old_value, "core_ContractualElement10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_ContractualElement10"):
                opp_val = getattr(value, "core_ContractualElement10", None)
                if opp_val is None:
                    setattr(value, "core_ContractualElement10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ReferencedModelElements(self):
        return self.__ReferencedModelElements

    @ReferencedModelElements.setter
    def ReferencedModelElements(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_ReferencedModelElements__ReferencedModelElements", None)
        self.__ReferencedModelElements = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "modelElementReferences"):
                opp_val = getattr(old_value, "modelElementReferences", None)
                if opp_val == self:
                    setattr(old_value, "modelElementReferences", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "modelElementReferences"):
                opp_val = getattr(value, "modelElementReferences", None)
                setattr(value, "modelElementReferences", self)

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_ReferencedModelElements__parent", None)
        self.__parent = value if value is not None else set()
        
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
                    

class core_VerificationActivity(IdentifiedElement):

    def __init__(self, verificationMethod: str, passed: bool, VerificationActivity: "core_AbstractRequirement" = None, verifiedBy: "core_AbstractRequirement" = None, core_VerificationActivity106: set["core_EObject"] = None, core_VerificationActivity: "core_Specification" = None):
        self.verificationMethod = verificationMethod
        self.passed = passed
        self.VerificationActivity = VerificationActivity
        self.verifiedBy = verifiedBy
        self.core_VerificationActivity106 = core_VerificationActivity106 if core_VerificationActivity106 is not None else set()
        self.core_VerificationActivity = core_VerificationActivity
        
        pass
    @property
    def verificationMethod(self):
        return self.__verificationMethod

    @verificationMethod.setter
    def verificationMethod(self, verificationMethod: str):
        self.__verificationMethod = verificationMethod


    @property
    def passed(self):
        return self.__passed

    @passed.setter
    def passed(self, passed: bool):
        self.__passed = passed


    @property
    def core_VerificationActivity(self):
        return self.__core_VerificationActivity

    @core_VerificationActivity.setter
    def core_VerificationActivity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_VerificationActivity__core_VerificationActivity", None)
        self.__core_VerificationActivity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_Specification34"):
                opp_val = getattr(old_value, "core_Specification34", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_Specification34"):
                opp_val = getattr(value, "core_Specification34", None)
                if opp_val is None:
                    setattr(value, "core_Specification34", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def verifiedBy(self):
        return self.__verifiedBy

    @verifiedBy.setter
    def verifiedBy(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_VerificationActivity__verifiedBy", None)
        self.__verifiedBy = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AbstractRequirement104"):
                opp_val = getattr(old_value, "AbstractRequirement104", None)
                if opp_val == self:
                    setattr(old_value, "AbstractRequirement104", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AbstractRequirement104"):
                opp_val = getattr(value, "AbstractRequirement104", None)
                setattr(value, "AbstractRequirement104", self)

    @property
    def core_VerificationActivity106(self):
        return self.__core_VerificationActivity106

    @core_VerificationActivity106.setter
    def core_VerificationActivity106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_VerificationActivity__core_VerificationActivity106", None)
        self.__core_VerificationActivity106 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core_EObject107"):
                    opp_val = getattr(item, "core_EObject107", None)
                    
                    if opp_val == self:
                        setattr(item, "core_EObject107", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core_EObject107"):
                    opp_val = getattr(item, "core_EObject107", None)
                    
                    setattr(item, "core_EObject107", self)
                    

    @property
    def VerificationActivity(self):
        return self.__VerificationActivity

    @VerificationActivity.setter
    def VerificationActivity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_VerificationActivity__VerificationActivity", None)
        self.__VerificationActivity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "requirement"):
                opp_val = getattr(old_value, "requirement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "requirement"):
                opp_val = getattr(value, "requirement", None)
                if opp_val is None:
                    setattr(value, "requirement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class core_Interaction(IdentifiedElement):

    def __init__(self, direction: str, core_Interaction: "core_Actor" = None, core_Interaction72: "core_EObject" = None):
        self.direction = direction
        self.core_Interaction = core_Interaction
        self.core_Interaction72 = core_Interaction72
        
        pass
    @property
    def direction(self):
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction


    @property
    def core_Interaction(self):
        return self.__core_Interaction

    @core_Interaction.setter
    def core_Interaction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_Interaction__core_Interaction", None)
        self.__core_Interaction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_Actor70"):
                opp_val = getattr(old_value, "core_Actor70", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_Actor70"):
                opp_val = getattr(value, "core_Actor70", None)
                if opp_val is None:
                    setattr(value, "core_Actor70", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def core_Interaction72(self):
        return self.__core_Interaction72

    @core_Interaction72.setter
    def core_Interaction72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_Interaction__core_Interaction72", None)
        self.__core_Interaction72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_EObject73"):
                opp_val = getattr(old_value, "core_EObject73", None)
                if opp_val == self:
                    setattr(old_value, "core_EObject73", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_EObject73"):
                opp_val = getattr(value, "core_EObject73", None)
                setattr(value, "core_EObject73", self)

class core_ModelElementReference(IdentifiedElement):

    def __init__(self, weight: str, verifies: str, satisfactionLevel: str, reason: str, ModelElementReference: "core_ReferencedModelElements" = None, core_ModelElementReference: "core_EObject" = None, modelElementReferences: "core_ReferencedModelElements" = None):
        self.weight = weight
        self.verifies = verifies
        self.satisfactionLevel = satisfactionLevel
        self.reason = reason
        self.ModelElementReference = ModelElementReference
        self.core_ModelElementReference = core_ModelElementReference
        self.modelElementReferences = modelElementReferences
        
        pass
    @property
    def reason(self):
        return self.__reason

    @reason.setter
    def reason(self, reason: str):
        self.__reason = reason


    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight: str):
        self.__weight = weight


    @property
    def satisfactionLevel(self):
        return self.__satisfactionLevel

    @satisfactionLevel.setter
    def satisfactionLevel(self, satisfactionLevel: str):
        self.__satisfactionLevel = satisfactionLevel


    @property
    def verifies(self):
        return self.__verifies

    @verifies.setter
    def verifies(self, verifies: str):
        self.__verifies = verifies


    @property
    def modelElementReferences(self):
        return self.__modelElementReferences

    @modelElementReferences.setter
    def modelElementReferences(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_ModelElementReference__modelElementReferences", None)
        self.__modelElementReferences = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ReferencedModelElements"):
                opp_val = getattr(old_value, "ReferencedModelElements", None)
                if opp_val == self:
                    setattr(old_value, "ReferencedModelElements", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ReferencedModelElements"):
                opp_val = getattr(value, "ReferencedModelElements", None)
                setattr(value, "ReferencedModelElements", self)

    @property
    def ModelElementReference(self):
        return self.__ModelElementReference

    @ModelElementReference.setter
    def ModelElementReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_ModelElementReference__ModelElementReference", None)
        self.__ModelElementReference = value
        
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

    @property
    def core_ModelElementReference(self):
        return self.__core_ModelElementReference

    @core_ModelElementReference.setter
    def core_ModelElementReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_ModelElementReference__core_ModelElementReference", None)
        self.__core_ModelElementReference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_EObject111"):
                opp_val = getattr(old_value, "core_EObject111", None)
                if opp_val == self:
                    setattr(old_value, "core_EObject111", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_EObject111"):
                opp_val = getattr(value, "core_EObject111", None)
                setattr(value, "core_EObject111", self)

class core_Conflict(IdentifiedElement):

    def __init__(self, degree: str, Conflict: "core_Goal" = None, core_Conflict: "core_Specification" = None, conflicts: set["core_Goal"] = None):
        self.degree = degree
        self.Conflict = Conflict
        self.core_Conflict = core_Conflict
        self.conflicts = conflicts if conflicts is not None else set()
        
        pass
    @property
    def degree(self):
        return self.__degree

    @degree.setter
    def degree(self, degree: str):
        self.__degree = degree


    @property
    def Conflict(self):
        return self.__Conflict

    @Conflict.setter
    def Conflict(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_Conflict__Conflict", None)
        self.__Conflict = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "goals"):
                opp_val = getattr(old_value, "goals", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "goals"):
                opp_val = getattr(value, "goals", None)
                if opp_val is None:
                    setattr(value, "goals", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def core_Conflict(self):
        return self.__core_Conflict

    @core_Conflict.setter
    def core_Conflict(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_Conflict__core_Conflict", None)
        self.__core_Conflict = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_Specification36"):
                opp_val = getattr(old_value, "core_Specification36", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_Specification36"):
                opp_val = getattr(value, "core_Specification36", None)
                if opp_val is None:
                    setattr(value, "core_Specification36", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def conflicts(self):
        return self.__conflicts

    @conflicts.setter
    def conflicts(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_Conflict__conflicts", None)
        self.__conflicts = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Goal"):
                    opp_val = getattr(item, "Goal", None)
                    
                    if opp_val == self:
                        setattr(item, "Goal", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Goal"):
                    opp_val = getattr(item, "Goal", None)
                    
                    setattr(item, "Goal", self)
                    

class core_Rationale(IdentifiedElement):

    pass
class core_RequirementsCoverageData(IdentifiedElement):

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


class core_ContractualElement(IdentifiedElement):

    def __init__(self, sources: str, originDate: str, scheduleDate: str, dropped: bool, droppingReason: str, satisfactionLevel: str, timeCriticality: str, core_ContractualElement12: set["core_EObject"] = None, core_ContractualElement15: set["core_EObject"] = None, core_ContractualElement: "core_Uncertainty" = None, contractualElements: set["core_StakeHolder"] = None, core_ContractualElement4: "core_ContractualElement" = None, core_ContractualElement2: set["core_ContractualElement"] = None, core_ContractualElement6: set["core_EObject"] = None, core_ContractualElement8: "core_Category" = None, core_ContractualElement10: set["core_ReferencedModelElements"] = None, contract: set["core_Rationale"] = None, core_ContractualElement19: set["core_Actor"] = None, core_ContractualElement21: "core_Expression" = None, core_ContractualElement23: "core_Expression" = None, core_ContractualElement26: set["core_EObject"] = None, ContractualElement: "core_StakeHolder" = None, ContractualElement119: "core_Rationale" = None):
        self.sources = sources
        self.originDate = originDate
        self.scheduleDate = scheduleDate
        self.dropped = dropped
        self.droppingReason = droppingReason
        self.satisfactionLevel = satisfactionLevel
        self.timeCriticality = timeCriticality
        self.core_ContractualElement12 = core_ContractualElement12 if core_ContractualElement12 is not None else set()
        self.core_ContractualElement15 = core_ContractualElement15 if core_ContractualElement15 is not None else set()
        self.core_ContractualElement = core_ContractualElement
        self.contractualElements = contractualElements if contractualElements is not None else set()
        self.core_ContractualElement4 = core_ContractualElement4
        self.core_ContractualElement2 = core_ContractualElement2 if core_ContractualElement2 is not None else set()
        self.core_ContractualElement6 = core_ContractualElement6 if core_ContractualElement6 is not None else set()
        self.core_ContractualElement8 = core_ContractualElement8
        self.core_ContractualElement10 = core_ContractualElement10 if core_ContractualElement10 is not None else set()
        self.contract = contract if contract is not None else set()
        self.core_ContractualElement19 = core_ContractualElement19 if core_ContractualElement19 is not None else set()
        self.core_ContractualElement21 = core_ContractualElement21
        self.core_ContractualElement23 = core_ContractualElement23
        self.core_ContractualElement26 = core_ContractualElement26 if core_ContractualElement26 is not None else set()
        self.ContractualElement = ContractualElement
        self.ContractualElement119 = ContractualElement119
        
        pass
    @property
    def dropped(self):
        return self.__dropped

    @dropped.setter
    def dropped(self, dropped: bool):
        self.__dropped = dropped


    @property
    def originDate(self):
        return self.__originDate

    @originDate.setter
    def originDate(self, originDate: str):
        self.__originDate = originDate


    @property
    def timeCriticality(self):
        return self.__timeCriticality

    @timeCriticality.setter
    def timeCriticality(self, timeCriticality: str):
        self.__timeCriticality = timeCriticality


    @property
    def satisfactionLevel(self):
        return self.__satisfactionLevel

    @satisfactionLevel.setter
    def satisfactionLevel(self, satisfactionLevel: str):
        self.__satisfactionLevel = satisfactionLevel


    @property
    def sources(self):
        return self.__sources

    @sources.setter
    def sources(self, sources: str):
        self.__sources = sources


    @property
    def droppingReason(self):
        return self.__droppingReason

    @droppingReason.setter
    def droppingReason(self, droppingReason: str):
        self.__droppingReason = droppingReason


    @property
    def scheduleDate(self):
        return self.__scheduleDate

    @scheduleDate.setter
    def scheduleDate(self, scheduleDate: str):
        self.__scheduleDate = scheduleDate


    @property
    def core_ContractualElement15(self):
        return self.__core_ContractualElement15

    @core_ContractualElement15.setter
    def core_ContractualElement15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_ContractualElement__core_ContractualElement15", None)
        self.__core_ContractualElement15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core_EObject16"):
                    opp_val = getattr(item, "core_EObject16", None)
                    
                    if opp_val == self:
                        setattr(item, "core_EObject16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core_EObject16"):
                    opp_val = getattr(item, "core_EObject16", None)
                    
                    setattr(item, "core_EObject16", self)
                    

    @property
    def core_ContractualElement8(self):
        return self.__core_ContractualElement8

    @core_ContractualElement8.setter
    def core_ContractualElement8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_ContractualElement__core_ContractualElement8", None)
        self.__core_ContractualElement8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_Category"):
                opp_val = getattr(old_value, "core_Category", None)
                if opp_val == self:
                    setattr(old_value, "core_Category", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_Category"):
                opp_val = getattr(value, "core_Category", None)
                setattr(value, "core_Category", self)

    @property
    def core_ContractualElement(self):
        return self.__core_ContractualElement

    @core_ContractualElement.setter
    def core_ContractualElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_ContractualElement__core_ContractualElement", None)
        self.__core_ContractualElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_Uncertainty"):
                opp_val = getattr(old_value, "core_Uncertainty", None)
                if opp_val == self:
                    setattr(old_value, "core_Uncertainty", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_Uncertainty"):
                opp_val = getattr(value, "core_Uncertainty", None)
                setattr(value, "core_Uncertainty", self)

    @property
    def core_ContractualElement21(self):
        return self.__core_ContractualElement21

    @core_ContractualElement21.setter
    def core_ContractualElement21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_ContractualElement__core_ContractualElement21", None)
        self.__core_ContractualElement21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_Expression"):
                opp_val = getattr(old_value, "core_Expression", None)
                if opp_val == self:
                    setattr(old_value, "core_Expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_Expression"):
                opp_val = getattr(value, "core_Expression", None)
                setattr(value, "core_Expression", self)

    @property
    def contractualElements(self):
        return self.__contractualElements

    @contractualElements.setter
    def contractualElements(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_ContractualElement__contractualElements", None)
        self.__contractualElements = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StakeHolder"):
                    opp_val = getattr(item, "StakeHolder", None)
                    
                    if opp_val == self:
                        setattr(item, "StakeHolder", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StakeHolder"):
                    opp_val = getattr(item, "StakeHolder", None)
                    
                    setattr(item, "StakeHolder", self)
                    

    @property
    def core_ContractualElement23(self):
        return self.__core_ContractualElement23

    @core_ContractualElement23.setter
    def core_ContractualElement23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_ContractualElement__core_ContractualElement23", None)
        self.__core_ContractualElement23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_Expression24"):
                opp_val = getattr(old_value, "core_Expression24", None)
                if opp_val == self:
                    setattr(old_value, "core_Expression24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_Expression24"):
                opp_val = getattr(value, "core_Expression24", None)
                setattr(value, "core_Expression24", self)

    @property
    def core_ContractualElement4(self):
        return self.__core_ContractualElement4

    @core_ContractualElement4.setter
    def core_ContractualElement4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_ContractualElement__core_ContractualElement4", None)
        self.__core_ContractualElement4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_ContractualElement2"):
                opp_val = getattr(old_value, "core_ContractualElement2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_ContractualElement2"):
                opp_val = getattr(value, "core_ContractualElement2", None)
                if opp_val is None:
                    setattr(value, "core_ContractualElement2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ContractualElement(self):
        return self.__ContractualElement

    @ContractualElement.setter
    def ContractualElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_ContractualElement__ContractualElement", None)
        self.__ContractualElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stakeholders"):
                opp_val = getattr(old_value, "stakeholders", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stakeholders"):
                opp_val = getattr(value, "stakeholders", None)
                if opp_val is None:
                    setattr(value, "stakeholders", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def core_ContractualElement6(self):
        return self.__core_ContractualElement6

    @core_ContractualElement6.setter
    def core_ContractualElement6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_ContractualElement__core_ContractualElement6", None)
        self.__core_ContractualElement6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core_EObject"):
                    opp_val = getattr(item, "core_EObject", None)
                    
                    if opp_val == self:
                        setattr(item, "core_EObject", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core_EObject"):
                    opp_val = getattr(item, "core_EObject", None)
                    
                    setattr(item, "core_EObject", self)
                    

    @property
    def contract(self):
        return self.__contract

    @contract.setter
    def contract(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_ContractualElement__contract", None)
        self.__contract = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Rationale"):
                    opp_val = getattr(item, "Rationale", None)
                    
                    if opp_val == self:
                        setattr(item, "Rationale", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Rationale"):
                    opp_val = getattr(item, "Rationale", None)
                    
                    setattr(item, "Rationale", self)
                    

    @property
    def core_ContractualElement19(self):
        return self.__core_ContractualElement19

    @core_ContractualElement19.setter
    def core_ContractualElement19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_ContractualElement__core_ContractualElement19", None)
        self.__core_ContractualElement19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core_Actor"):
                    opp_val = getattr(item, "core_Actor", None)
                    
                    if opp_val == self:
                        setattr(item, "core_Actor", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core_Actor"):
                    opp_val = getattr(item, "core_Actor", None)
                    
                    setattr(item, "core_Actor", self)
                    

    @property
    def core_ContractualElement2(self):
        return self.__core_ContractualElement2

    @core_ContractualElement2.setter
    def core_ContractualElement2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_ContractualElement__core_ContractualElement2", None)
        self.__core_ContractualElement2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core_ContractualElement4"):
                    opp_val = getattr(item, "core_ContractualElement4", None)
                    
                    if opp_val == self:
                        setattr(item, "core_ContractualElement4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core_ContractualElement4"):
                    opp_val = getattr(item, "core_ContractualElement4", None)
                    
                    setattr(item, "core_ContractualElement4", self)
                    

    @property
    def core_ContractualElement12(self):
        return self.__core_ContractualElement12

    @core_ContractualElement12.setter
    def core_ContractualElement12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_ContractualElement__core_ContractualElement12", None)
        self.__core_ContractualElement12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core_EObject13"):
                    opp_val = getattr(item, "core_EObject13", None)
                    
                    if opp_val == self:
                        setattr(item, "core_EObject13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core_EObject13"):
                    opp_val = getattr(item, "core_EObject13", None)
                    
                    setattr(item, "core_EObject13", self)
                    

    @property
    def ContractualElement119(self):
        return self.__ContractualElement119

    @ContractualElement119.setter
    def ContractualElement119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_ContractualElement__ContractualElement119", None)
        self.__ContractualElement119 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rationales"):
                opp_val = getattr(old_value, "rationales", None)
                if opp_val == self:
                    setattr(old_value, "rationales", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rationales"):
                opp_val = getattr(value, "rationales", None)
                setattr(value, "rationales", self)

    @property
    def core_ContractualElement10(self):
        return self.__core_ContractualElement10

    @core_ContractualElement10.setter
    def core_ContractualElement10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_ContractualElement__core_ContractualElement10", None)
        self.__core_ContractualElement10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core_ReferencedModelElements"):
                    opp_val = getattr(item, "core_ReferencedModelElements", None)
                    
                    if opp_val == self:
                        setattr(item, "core_ReferencedModelElements", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core_ReferencedModelElements"):
                    opp_val = getattr(item, "core_ReferencedModelElements", None)
                    
                    setattr(item, "core_ReferencedModelElements", self)
                    

    @property
    def core_ContractualElement26(self):
        return self.__core_ContractualElement26

    @core_ContractualElement26.setter
    def core_ContractualElement26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_ContractualElement__core_ContractualElement26", None)
        self.__core_ContractualElement26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core_EObject27"):
                    opp_val = getattr(item, "core_EObject27", None)
                    
                    if opp_val == self:
                        setattr(item, "core_EObject27", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core_EObject27"):
                    opp_val = getattr(item, "core_EObject27", None)
                    
                    setattr(item, "core_EObject27", self)
                    

class core_IdentifiedElement(ABC):

    def __init__(self, name: str, description: str, id: str):
        self.name = name
        self.description = description
        self.id = id
        
        pass
    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

