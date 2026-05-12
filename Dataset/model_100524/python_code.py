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
class VariationPointInstance:

    pass
class VariationPoint:

    pass
class Product:

    pass
class SolutionDomainUseCase:

    pass
class Danger:

    pass
class Asset:

    pass
class urml_service_Service(Asset):

    pass
class urml_usecase_Actor(Asset):

    pass
class Actor:

    pass
class Step:

    pass
class NonFunctionalRequirement:

    pass
class UseCase:

    pass
class urml_usecase_SolutionDomainUseCase(UseCase):

    pass
class urml_usecase_ApplicationDomainUseCase(UseCase):

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
                    

class FunctionalRequirement:

    pass
class Requirement:

    pass
class urml_requirement_NonFunctionalRequirement(Requirement):

    pass
class urml_requirement_FunctionalRequirement(Requirement):

    pass
class GoalReference:

    pass
class ApplicationDomainUseCase:

    pass
class AbstractFeature:

    pass
class urml_feature_VariationPoint(AbstractFeature):

    def __init__(self, multiplicity: int, optionalParentVariationPoint: set["AbstractFeature"] = None, variationPoint: set["VariationPointInstance"] = None, AbstractFeature33: "urml_usecase_SolutionDomainUseCase" = None, AbstractFeature57: "urml_feature_AbstractFeature" = None, AbstractFeature23: "urml_requirement_NonFunctionalRequirement" = None, AbstractFeature65: "urml_feature_AbstractFeature" = None, AbstractFeature67: "urml_feature_AbstractFeature" = None, AbstractFeature59: "urml_feature_AbstractFeature" = None, AbstractFeature72: "urml_feature_VariationPoint" = None, AbstractFeature81: "urml_feature_VariationPointInstance" = None, AbstractFeature63: "urml_feature_AbstractFeature" = None, AbstractFeature18: "urml_requirement_FunctionalRequirement" = None, AbstractFeature: "urml_goal_Goal" = None, AbstractFeature61: "urml_feature_AbstractFeature" = None):
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
                if hasattr(item, "VariationPointInstance74"):
                    opp_val = getattr(item, "VariationPointInstance74", None)
                    
                    if opp_val == self:
                        setattr(item, "VariationPointInstance74", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "VariationPointInstance74"):
                    opp_val = getattr(item, "VariationPointInstance74", None)
                    
                    setattr(item, "VariationPointInstance74", self)
                    

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
                if hasattr(item, "AbstractFeature72"):
                    opp_val = getattr(item, "AbstractFeature72", None)
                    
                    if opp_val == self:
                        setattr(item, "AbstractFeature72", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AbstractFeature72"):
                    opp_val = getattr(item, "AbstractFeature72", None)
                    
                    setattr(item, "AbstractFeature72", self)
                    

class urml_feature_Feature(AbstractFeature):

    pass
class goal_urml_Stakeholder:

    pass
class AssociationClassElement:

    pass
class UnicaseModelElement:

    pass
class urml_UrmlModelElement(UnicaseModelElement):

    pass
class MEDiagram:

    pass
class urml_URMLDiagram(MEDiagram):

    pass
class Goal:

    pass
class UrmlModelElement:

    pass
class urml_feature_AbstractFeature(UrmlModelElement):

    pass
class urml_feature_Product(UrmlModelElement):

    pass
class urml_goal_Goal(UrmlModelElement):

    def __init__(self, soft: bool, type: str, goals: set["goal_urml_Stakeholder"] = None, goals3: set["AbstractFeature"] = None, detailedGoal: "ApplicationDomainUseCase" = None, parentGoal: set["Goal"] = None, subGoals: "Goal" = None, target: set["GoalReference"] = None, source: set["GoalReference"] = None):
        self.soft = soft
        self.type = type
        self.goals = goals if goals is not None else set()
        self.goals3 = goals3 if goals3 is not None else set()
        self.detailedGoal = detailedGoal
        self.parentGoal = parentGoal if parentGoal is not None else set()
        self.subGoals = subGoals
        self.target = target if target is not None else set()
        self.source = source if source is not None else set()
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def soft(self):
        return self.__soft

    @soft.setter
    def soft(self, soft: bool):
        self.__soft = soft


    @property
    def goals3(self):
        return self.__goals3

    @goals3.setter
    def goals3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_urml_goal_Goal__goals3", None)
        self.__goals3 = value if value is not None else set()
        
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
                if hasattr(item, "GoalReference11"):
                    opp_val = getattr(item, "GoalReference11", None)
                    
                    if opp_val == self:
                        setattr(item, "GoalReference11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GoalReference11"):
                    opp_val = getattr(item, "GoalReference11", None)
                    
                    setattr(item, "GoalReference11", self)
                    

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
                if hasattr(item, "Goal6"):
                    opp_val = getattr(item, "Goal6", None)
                    
                    if opp_val == self:
                        setattr(item, "Goal6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Goal6"):
                    opp_val = getattr(item, "Goal6", None)
                    
                    setattr(item, "Goal6", self)
                    

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
            if hasattr(old_value, "Goal8"):
                opp_val = getattr(old_value, "Goal8", None)
                if opp_val == self:
                    setattr(old_value, "Goal8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Goal8"):
                opp_val = getattr(value, "Goal8", None)
                setattr(value, "Goal8", self)

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
                    

class urml_danger_Asset(UrmlModelElement):

    pass
class urml_danger_Danger(UrmlModelElement):

    pass
class urml_feature_VariationPointInstance(UrmlModelElement):

    pass
class urml_usecase_UseCase(UrmlModelElement):

    pass
class urml_Stakeholder(UrmlModelElement):

    pass
class urml_danger_Mitigation(UrmlModelElement):

    pass
class urml_goal_GoalReference(UrmlModelElement, AssociationClassElement):

    def __init__(self, weight: str, influencingGoals: "Goal" = None, influencedGoals: "Goal" = None):
        self.weight = weight
        self.influencingGoals = influencingGoals
        self.influencedGoals = influencedGoals
        
        pass
    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight: str):
        self.__weight = weight


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
            if hasattr(old_value, "Goal15"):
                opp_val = getattr(old_value, "Goal15", None)
                if opp_val == self:
                    setattr(old_value, "Goal15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Goal15"):
                opp_val = getattr(value, "Goal15", None)
                setattr(value, "Goal15", self)

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
            if hasattr(old_value, "Goal13"):
                opp_val = getattr(old_value, "Goal13", None)
                if opp_val == self:
                    setattr(old_value, "Goal13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Goal13"):
                opp_val = getattr(value, "Goal13", None)
                setattr(value, "Goal13", self)
