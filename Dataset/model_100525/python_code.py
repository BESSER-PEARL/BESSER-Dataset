from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class GoalType(Enum):
    BUSINESS_GOAL = "BUSINESS_GOAL"
    PRODUCT_GOAL = "PRODUCT_GOAL"
    CUSTOMER_GOAL = "CUSTOMER_GOAL"
    END_USER_GOAL = "END_USER_GOAL"
class GoalReferenceType(Enum):
    PLUS_PLUS = "PLUS_PLUS"
    PLUS = "PLUS"
    MINUS = "MINUS"
    MINUS_MINUS = "MINUS_MINUS"


############################################
# Definition of Classes
############################################

class Feature:

    pass
class Product:

    pass
class VariationPointInstance:

    pass
class VariationPoint:

    pass
class SolutionDomainUseCase:

    pass
class Danger:

    pass
class UseCase:

    pass
class urml_usecase_ApplicationDomainUseCase(UseCase):

    pass
class Actor:

    pass
class Step:

    pass
class NonFunctionalRequirement:

    pass
class Asset:

    pass
class urml_service_Service(Asset):

    pass
class urml_usecase_Actor(Asset):

    pass
class urml_usecase_SolutionDomainUseCase(UseCase):

    pass
class Requirement:

    pass
class urml_requirement_FunctionalRequirement(Requirement):

    pass
class Service:

    pass
class Mitigation:

    pass
class urml_danger_ProceduralMitigation(Mitigation):

    def __init__(self, mitigationProcedure: str, Mitigation: "urml_danger_Danger" = None):
        self.mitigationProcedure = mitigationProcedure
        
        pass
    @property
    def mitigationProcedure(self):
        return self.__mitigationProcedure

    @mitigationProcedure.setter
    def mitigationProcedure(self, mitigationProcedure: str):
        self.__mitigationProcedure = mitigationProcedure


class urml_requirement_Requirement(Mitigation):

    def __init__(self, terminal: bool, satisfiedRequirements: set["Service"] = None, Mitigation: "urml_danger_Danger" = None):
        self.terminal = terminal
        self.satisfiedRequirements = satisfiedRequirements if satisfiedRequirements is not None else set()
        
        pass
    @property
    def terminal(self):
        return self.__terminal

    @terminal.setter
    def terminal(self, terminal: bool):
        self.__terminal = terminal


    @property
    def satisfiedRequirements(self):
        return self.__satisfiedRequirements

    @satisfiedRequirements.setter
    def satisfiedRequirements(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_urml_requirement_Requirement__satisfiedRequirements", None)
        self.__satisfiedRequirements = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Service"):
                    opp_val = getattr(item, "Service", None)
                    
                    if opp_val == self:
                        setattr(item, "Service", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Service"):
                    opp_val = getattr(item, "Service", None)
                    
                    setattr(item, "Service", self)
                    

class urml_requirement_NonFunctionalRequirement(Requirement):

    pass
class FunctionalRequirement:

    pass
class GoalReference:

    pass
class ApplicationDomainUseCase:

    pass
class AbstractFeature:

    pass
class urml_feature_VariationPoint(AbstractFeature):

    def __init__(self, multiplicity: int, optionalParentVariationPoint: set["AbstractFeature"] = None, variationPoint: set["VariationPointInstance"] = None, AbstractFeature84: "urml_feature_AbstractFeature" = None, AbstractFeature52: "urml_usecase_SolutionDomainUseCase" = None, AbstractFeature82: "urml_feature_AbstractFeature" = None, AbstractFeature100: "urml_feature_VariationPointInstance" = None, AbstractFeature42: "urml_requirement_NonFunctionalRequirement" = None, AbstractFeature78: "urml_feature_AbstractFeature" = None, AbstractFeature91: "urml_feature_VariationPoint" = None, AbstractFeature37: "urml_requirement_FunctionalRequirement" = None, AbstractFeature76: "urml_feature_AbstractFeature" = None, AbstractFeature86: "urml_feature_AbstractFeature" = None, AbstractFeature: "urml_goal_Goal" = None, AbstractFeature80: "urml_feature_AbstractFeature" = None):
        self.multiplicity = multiplicity
        self.optionalParentVariationPoint = optionalParentVariationPoint if optionalParentVariationPoint is not None else set()
        self.variationPoint = variationPoint if variationPoint is not None else set()
        
        pass
    @property
    def multiplicity(self):
        return self.__multiplicity

    @multiplicity.setter
    def multiplicity(self, multiplicity: int):
        self.__multiplicity = multiplicity


    @property
    def optionalParentVariationPoint(self):
        return self.__optionalParentVariationPoint

    @optionalParentVariationPoint.setter
    def optionalParentVariationPoint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_urml_feature_VariationPoint__optionalParentVariationPoint", None)
        self.__optionalParentVariationPoint = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AbstractFeature91"):
                    opp_val = getattr(item, "AbstractFeature91", None)
                    
                    if opp_val == self:
                        setattr(item, "AbstractFeature91", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AbstractFeature91"):
                    opp_val = getattr(item, "AbstractFeature91", None)
                    
                    setattr(item, "AbstractFeature91", self)
                    

    @property
    def variationPoint(self):
        return self.__variationPoint

    @variationPoint.setter
    def variationPoint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_urml_feature_VariationPoint__variationPoint", None)
        self.__variationPoint = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "VariationPointInstance93"):
                    opp_val = getattr(item, "VariationPointInstance93", None)
                    
                    if opp_val == self:
                        setattr(item, "VariationPointInstance93", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "VariationPointInstance93"):
                    opp_val = getattr(item, "VariationPointInstance93", None)
                    
                    setattr(item, "VariationPointInstance93", self)
                    

class urml_feature_Feature(AbstractFeature):

    pass
class AssociationClassElement:

    pass
class urml_PhaseSetEntry:

    pass
class urml_EStructuralFeature:

    pass
class urml_EClass:

    pass
class goal_urml_Stakeholder:

    pass
class UrmlModelElement:

    pass
class urml_danger_Asset(UrmlModelElement):

    pass
class urml_danger_Mitigation(UrmlModelElement):

    pass
class urml_feature_Product(UrmlModelElement):

    pass
class urml_usecase_UseCase(UrmlModelElement):

    pass
class urml_goal_Goal(UrmlModelElement):

    def __init__(self, soft: bool, type: str, target: set["GoalReference"] = None, goals: set["goal_urml_Stakeholder"] = None, source: set["GoalReference"] = None, goals22: set["AbstractFeature"] = None, detailedGoal: "ApplicationDomainUseCase" = None, parentGoal: set["Goal"] = None, subGoals: "Goal" = None):
        self.soft = soft
        self.type = type
        self.target = target if target is not None else set()
        self.goals = goals if goals is not None else set()
        self.source = source if source is not None else set()
        self.goals22 = goals22 if goals22 is not None else set()
        self.detailedGoal = detailedGoal
        self.parentGoal = parentGoal if parentGoal is not None else set()
        self.subGoals = subGoals
        
        pass
    @property
    def soft(self):
        return self.__soft

    @soft.setter
    def soft(self, soft: bool):
        self.__soft = soft


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def subGoals(self):
        return self.__subGoals

    @subGoals.setter
    def subGoals(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_urml_goal_Goal__subGoals", None)
        self.__subGoals = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Goal27"):
                opp_val = getattr(old_value, "Goal27", None)
                if opp_val == self:
                    setattr(old_value, "Goal27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Goal27"):
                opp_val = getattr(value, "Goal27", None)
                setattr(value, "Goal27", self)

    @property
    def target(self):
        return self.__target

    @target.setter
    def target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_urml_goal_Goal__target", None)
        self.__target = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GoalReference"):
                    opp_val = getattr(item, "GoalReference", None)
                    
                    if opp_val == self:
                        setattr(item, "GoalReference", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GoalReference"):
                    opp_val = getattr(item, "GoalReference", None)
                    
                    setattr(item, "GoalReference", self)
                    

    @property
    def parentGoal(self):
        return self.__parentGoal

    @parentGoal.setter
    def parentGoal(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_urml_goal_Goal__parentGoal", None)
        self.__parentGoal = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Goal25"):
                    opp_val = getattr(item, "Goal25", None)
                    
                    if opp_val == self:
                        setattr(item, "Goal25", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Goal25"):
                    opp_val = getattr(item, "Goal25", None)
                    
                    setattr(item, "Goal25", self)
                    

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_urml_goal_Goal__source", None)
        self.__source = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GoalReference30"):
                    opp_val = getattr(item, "GoalReference30", None)
                    
                    if opp_val == self:
                        setattr(item, "GoalReference30", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GoalReference30"):
                    opp_val = getattr(item, "GoalReference30", None)
                    
                    setattr(item, "GoalReference30", self)
                    

    @property
    def goals22(self):
        return self.__goals22

    @goals22.setter
    def goals22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_urml_goal_Goal__goals22", None)
        self.__goals22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AbstractFeature"):
                    opp_val = getattr(item, "AbstractFeature", None)
                    
                    if opp_val == self:
                        setattr(item, "AbstractFeature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AbstractFeature"):
                    opp_val = getattr(item, "AbstractFeature", None)
                    
                    setattr(item, "AbstractFeature", self)
                    

    @property
    def detailedGoal(self):
        return self.__detailedGoal

    @detailedGoal.setter
    def detailedGoal(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_urml_goal_Goal__detailedGoal", None)
        self.__detailedGoal = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ApplicationDomainUseCase"):
                opp_val = getattr(old_value, "ApplicationDomainUseCase", None)
                if opp_val == self:
                    setattr(old_value, "ApplicationDomainUseCase", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ApplicationDomainUseCase"):
                opp_val = getattr(value, "ApplicationDomainUseCase", None)
                setattr(value, "ApplicationDomainUseCase", self)

    @property
    def goals(self):
        return self.__goals

    @goals.setter
    def goals(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_urml_goal_Goal__goals", None)
        self.__goals = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Stakeholder"):
                    opp_val = getattr(item, "Stakeholder", None)
                    
                    if opp_val == self:
                        setattr(item, "Stakeholder", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Stakeholder"):
                    opp_val = getattr(item, "Stakeholder", None)
                    
                    setattr(item, "Stakeholder", self)
                    

class urml_feature_VariationPointInstance(UrmlModelElement):

    pass
class urml_danger_Danger(UrmlModelElement):

    pass
class urml_feature_AbstractFeature(UrmlModelElement):

    pass
class urml_goal_GoalReference(UrmlModelElement, AssociationClassElement):

    def __init__(self, weight: str, influencedGoals: "Goal" = None, influencingGoals: "Goal" = None):
        self.weight = weight
        self.influencedGoals = influencedGoals
        self.influencingGoals = influencingGoals
        
        pass
    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight: str):
        self.__weight = weight


    @property
    def influencedGoals(self):
        return self.__influencedGoals

    @influencedGoals.setter
    def influencedGoals(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_urml_goal_GoalReference__influencedGoals", None)
        self.__influencedGoals = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Goal32"):
                opp_val = getattr(old_value, "Goal32", None)
                if opp_val == self:
                    setattr(old_value, "Goal32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Goal32"):
                opp_val = getattr(value, "Goal32", None)
                setattr(value, "Goal32", self)

    @property
    def influencingGoals(self):
        return self.__influencingGoals

    @influencingGoals.setter
    def influencingGoals(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_urml_goal_GoalReference__influencingGoals", None)
        self.__influencingGoals = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Goal34"):
                opp_val = getattr(old_value, "Goal34", None)
                if opp_val == self:
                    setattr(old_value, "Goal34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Goal34"):
                opp_val = getattr(value, "Goal34", None)
                setattr(value, "Goal34", self)

class urml_Stakeholder(UrmlModelElement):

    pass
class UnicaseModelElement:

    pass
class urml_UrmlModelElement(UnicaseModelElement):

    def __init__(self, reviewed: bool, urml_UrmlModelElement: "urml_UrmlModelElement" = None, urml_UrmlModelElement0: set["urml_UrmlModelElement"] = None):
        self.reviewed = reviewed
        self.urml_UrmlModelElement = urml_UrmlModelElement
        self.urml_UrmlModelElement0 = urml_UrmlModelElement0 if urml_UrmlModelElement0 is not None else set()
        
        pass
    @property
    def reviewed(self):
        return self.__reviewed

    @reviewed.setter
    def reviewed(self, reviewed: bool):
        self.__reviewed = reviewed


    @property
    def urml_UrmlModelElement(self):
        return self.__urml_UrmlModelElement

    @urml_UrmlModelElement.setter
    def urml_UrmlModelElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_urml_UrmlModelElement__urml_UrmlModelElement", None)
        self.__urml_UrmlModelElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "urml_UrmlModelElement0"):
                opp_val = getattr(old_value, "urml_UrmlModelElement0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "urml_UrmlModelElement0"):
                opp_val = getattr(value, "urml_UrmlModelElement0", None)
                if opp_val is None:
                    setattr(value, "urml_UrmlModelElement0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def urml_UrmlModelElement0(self):
        return self.__urml_UrmlModelElement0

    @urml_UrmlModelElement0.setter
    def urml_UrmlModelElement0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_urml_UrmlModelElement__urml_UrmlModelElement0", None)
        self.__urml_UrmlModelElement0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "urml_UrmlModelElement"):
                    opp_val = getattr(item, "urml_UrmlModelElement", None)
                    
                    if opp_val == self:
                        setattr(item, "urml_UrmlModelElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "urml_UrmlModelElement"):
                    opp_val = getattr(item, "urml_UrmlModelElement", None)
                    
                    setattr(item, "urml_UrmlModelElement", self)
                    

class urml_SetEntry:

    pass
class NonDomainElement:

    pass
class urml_UrmlProjectSettings(UnicaseModelElement, NonDomainElement):

    pass
class urml_Phase(UnicaseModelElement, NonDomainElement):

    pass
class urml_StakeholderRole(UnicaseModelElement, NonDomainElement):

    pass
class MEDiagram:

    pass
class urml_URMLDiagram(MEDiagram):

    pass
class Goal:

    pass