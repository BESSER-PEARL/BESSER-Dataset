from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class adaptations_smartadapters4MODERATES_ActionBlock:

    pass
class adaptations_smartadapters4MODERATES_PlatformAnnotation:

    pass
class adaptations_smartadapters4MODERATES_AnnotatedElement:

    pass
class adaptations_smartadapters4MODERATES_Expression:

    pass
class adaptations_smartadapters4MODERATES_Event:

    pass
class adaptations_smartadapters4MODERATES_Property:

    pass
class adaptations_smartadapters4MODERATES_Action:

    pass
class adaptations_smartadapters4MODERATES_Transition:

    pass
class UnsetAdaptation:

    pass
class smartadapters4MODERATES_adaptations_UnsetTransition(UnsetAdaptation):

    pass
class smartadapters4MODERATES_adaptations_UnsetState(UnsetAdaptation):

    pass
class smartadapters4MODERATES_adaptations_UnsetCompositeState(UnsetAdaptation):

    pass
class adaptations_smartadapters4MODERATES_State:

    pass
class adaptations_smartadapters4MODERATES_CompositeState:

    pass
class SetAdaptation:

    pass
class smartadapters4MODERATES_adaptations_SetActionBlock(SetAdaptation):

    pass
class smartadapters4MODERATES_adaptations_SetTransition(SetAdaptation):

    pass
class smartadapters4MODERATES_adaptations_SetAnnotatedElement(SetAdaptation):

    pass
class smartadapters4MODERATES_adaptations_SetState(SetAdaptation):

    pass
class smartadapters4MODERATES_adaptations_SetCompositeState(SetAdaptation):

    pass
class ScopedInstantiation:

    pass
class smartadapters4MODERATES_PerElementMatch(ScopedInstantiation):

    pass
class smartadapters4MODERATES_PerRoleMatch(ScopedInstantiation):

    pass
class InstantiationStrategy:

    pass
class smartadapters4MODERATES_ScopedInstantiation(InstantiationStrategy):

    pass
class smartadapters4MODERATES_GlobalInstantiation(InstantiationStrategy):

    pass
class smartadapters4MODERATES_AspectModelElement:

    pass
class Adaptation:

    pass
class smartadapters4MODERATES_UnsetAdaptation(Adaptation):

    pass
class smartadapters4MODERATES_SetAdaptation(Adaptation):

    pass
class smartadapters4MODERATES_CreateAdaptation(Adaptation):

    pass
class smartadapters4MODERATES_CloneAdaptation(Adaptation):

    pass
class smartadapters4MODERATES_Adaptation(ABC):

    pass
class smartadapters4MODERATES_InstantiationStrategy(ABC):

    pass
class smartadapters4MODERATES_AdviceModel:

    pass
class smartadapters4MODERATES_PointcutModel:

    pass
class smartadapters4MODERATES_Aspect:

    def __init__(self, name: str, smartadapters4MODERATES_Aspect: "smartadapters4MODERATES_PointcutModel" = None, smartadapters4MODERATES_Aspect2: "smartadapters4MODERATES_AdviceModel" = None, smartadapters4MODERATES_Aspect4: set["smartadapters4MODERATES_InstantiationStrategy"] = None, smartadapters4MODERATES_Aspect6: set["smartadapters4MODERATES_Adaptation"] = None):
        self.name = name
        self.smartadapters4MODERATES_Aspect = smartadapters4MODERATES_Aspect
        self.smartadapters4MODERATES_Aspect2 = smartadapters4MODERATES_Aspect2
        self.smartadapters4MODERATES_Aspect4 = smartadapters4MODERATES_Aspect4 if smartadapters4MODERATES_Aspect4 is not None else set()
        self.smartadapters4MODERATES_Aspect6 = smartadapters4MODERATES_Aspect6 if smartadapters4MODERATES_Aspect6 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def smartadapters4MODERATES_Aspect4(self):
        return self.__smartadapters4MODERATES_Aspect4

    @smartadapters4MODERATES_Aspect4.setter
    def smartadapters4MODERATES_Aspect4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smartadapters4MODERATES_Aspect__smartadapters4MODERATES_Aspect4", None)
        self.__smartadapters4MODERATES_Aspect4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "smartadapters4MODERATES_InstantiationStrategy"):
                    opp_val = getattr(item, "smartadapters4MODERATES_InstantiationStrategy", None)
                    
                    if opp_val == self:
                        setattr(item, "smartadapters4MODERATES_InstantiationStrategy", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smartadapters4MODERATES_InstantiationStrategy"):
                    opp_val = getattr(item, "smartadapters4MODERATES_InstantiationStrategy", None)
                    
                    setattr(item, "smartadapters4MODERATES_InstantiationStrategy", self)
                    

    @property
    def smartadapters4MODERATES_Aspect2(self):
        return self.__smartadapters4MODERATES_Aspect2

    @smartadapters4MODERATES_Aspect2.setter
    def smartadapters4MODERATES_Aspect2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smartadapters4MODERATES_Aspect__smartadapters4MODERATES_Aspect2", None)
        self.__smartadapters4MODERATES_Aspect2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smartadapters4MODERATES_AdviceModel"):
                opp_val = getattr(old_value, "smartadapters4MODERATES_AdviceModel", None)
                if opp_val == self:
                    setattr(old_value, "smartadapters4MODERATES_AdviceModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smartadapters4MODERATES_AdviceModel"):
                opp_val = getattr(value, "smartadapters4MODERATES_AdviceModel", None)
                setattr(value, "smartadapters4MODERATES_AdviceModel", self)

    @property
    def smartadapters4MODERATES_Aspect6(self):
        return self.__smartadapters4MODERATES_Aspect6

    @smartadapters4MODERATES_Aspect6.setter
    def smartadapters4MODERATES_Aspect6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smartadapters4MODERATES_Aspect__smartadapters4MODERATES_Aspect6", None)
        self.__smartadapters4MODERATES_Aspect6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "smartadapters4MODERATES_Adaptation"):
                    opp_val = getattr(item, "smartadapters4MODERATES_Adaptation", None)
                    
                    if opp_val == self:
                        setattr(item, "smartadapters4MODERATES_Adaptation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smartadapters4MODERATES_Adaptation"):
                    opp_val = getattr(item, "smartadapters4MODERATES_Adaptation", None)
                    
                    setattr(item, "smartadapters4MODERATES_Adaptation", self)
                    

    @property
    def smartadapters4MODERATES_Aspect(self):
        return self.__smartadapters4MODERATES_Aspect

    @smartadapters4MODERATES_Aspect.setter
    def smartadapters4MODERATES_Aspect(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smartadapters4MODERATES_Aspect__smartadapters4MODERATES_Aspect", None)
        self.__smartadapters4MODERATES_Aspect = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smartadapters4MODERATES_PointcutModel"):
                opp_val = getattr(old_value, "smartadapters4MODERATES_PointcutModel", None)
                if opp_val == self:
                    setattr(old_value, "smartadapters4MODERATES_PointcutModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smartadapters4MODERATES_PointcutModel"):
                opp_val = getattr(value, "smartadapters4MODERATES_PointcutModel", None)
                setattr(value, "smartadapters4MODERATES_PointcutModel", self)
