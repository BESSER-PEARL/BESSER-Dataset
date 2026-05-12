from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class ActorType(Enum):
    SYSTEM = "SYSTEM"
    PERSON = "PERSON"
    ORGANIZATION = "ORGANIZATION"


############################################
# Definition of Classes
############################################

class useCases_Feature:

    pass
class useCases_StepAlternative:

    def __init__(self, finalizeFlow: bool, finalState: str, useCases_StepAlternative71: "useCases_Step" = None, useCases_StepAlternative74: "useCases_CustomStepType" = None, useCases_StepAlternative: "useCases_Step" = None):
        self.finalizeFlow = finalizeFlow
        self.finalState = finalState
        self.useCases_StepAlternative71 = useCases_StepAlternative71
        self.useCases_StepAlternative74 = useCases_StepAlternative74
        self.useCases_StepAlternative = useCases_StepAlternative
        
        pass
    @property
    def finalizeFlow(self):
        return self.__finalizeFlow

    @finalizeFlow.setter
    def finalizeFlow(self, finalizeFlow: bool):
        self.__finalizeFlow = finalizeFlow


    @property
    def finalState(self):
        return self.__finalState

    @finalState.setter
    def finalState(self, finalState: str):
        self.__finalState = finalState


    @property
    def useCases_StepAlternative74(self):
        return self.__useCases_StepAlternative74

    @useCases_StepAlternative74.setter
    def useCases_StepAlternative74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_useCases_StepAlternative__useCases_StepAlternative74", None)
        self.__useCases_StepAlternative74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "useCases_CustomStepType75"):
                opp_val = getattr(old_value, "useCases_CustomStepType75", None)
                if opp_val == self:
                    setattr(old_value, "useCases_CustomStepType75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "useCases_CustomStepType75"):
                opp_val = getattr(value, "useCases_CustomStepType75", None)
                setattr(value, "useCases_CustomStepType75", self)

    @property
    def useCases_StepAlternative(self):
        return self.__useCases_StepAlternative

    @useCases_StepAlternative.setter
    def useCases_StepAlternative(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_useCases_StepAlternative__useCases_StepAlternative", None)
        self.__useCases_StepAlternative = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "useCases_Step67"):
                opp_val = getattr(old_value, "useCases_Step67", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "useCases_Step67"):
                opp_val = getattr(value, "useCases_Step67", None)
                if opp_val is None:
                    setattr(value, "useCases_Step67", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def useCases_StepAlternative71(self):
        return self.__useCases_StepAlternative71

    @useCases_StepAlternative71.setter
    def useCases_StepAlternative71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_useCases_StepAlternative__useCases_StepAlternative71", None)
        self.__useCases_StepAlternative71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "useCases_Step72"):
                opp_val = getattr(old_value, "useCases_Step72", None)
                if opp_val == self:
                    setattr(old_value, "useCases_Step72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "useCases_Step72"):
                opp_val = getattr(value, "useCases_Step72", None)
                setattr(value, "useCases_Step72", self)

class StepAlternative:

    pass
class useCases_AlternativeFlowAlternative(StepAlternative):

    pass
class useCases_LocalAlternative(StepAlternative):

    def __init__(self, description: str, useCases_LocalAlternative: "useCases_Condition" = None, useCases_LocalAlternative78: "useCases_UseCase" = None):
        self.description = description
        self.useCases_LocalAlternative = useCases_LocalAlternative
        self.useCases_LocalAlternative78 = useCases_LocalAlternative78
        
        pass
    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


    @property
    def useCases_LocalAlternative(self):
        return self.__useCases_LocalAlternative

    @useCases_LocalAlternative.setter
    def useCases_LocalAlternative(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_useCases_LocalAlternative__useCases_LocalAlternative", None)
        self.__useCases_LocalAlternative = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "useCases_Condition"):
                opp_val = getattr(old_value, "useCases_Condition", None)
                if opp_val == self:
                    setattr(old_value, "useCases_Condition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "useCases_Condition"):
                opp_val = getattr(value, "useCases_Condition", None)
                setattr(value, "useCases_Condition", self)

    @property
    def useCases_LocalAlternative78(self):
        return self.__useCases_LocalAlternative78

    @useCases_LocalAlternative78.setter
    def useCases_LocalAlternative78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_useCases_LocalAlternative__useCases_LocalAlternative78", None)
        self.__useCases_LocalAlternative78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "useCases_UseCase79"):
                opp_val = getattr(old_value, "useCases_UseCase79", None)
                if opp_val == self:
                    setattr(old_value, "useCases_UseCase79", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "useCases_UseCase79"):
                opp_val = getattr(value, "useCases_UseCase79", None)
                setattr(value, "useCases_UseCase79", self)

class useCases_Condition(StepAlternative):

    def __init__(self, condition: str, useCases_Condition: "useCases_LocalAlternative" = None, useCases_Condition81: "useCases_AlternativeFlowAlternative" = None):
        self.condition = condition
        self.useCases_Condition = useCases_Condition
        self.useCases_Condition81 = useCases_Condition81
        
        pass
    @property
    def condition(self):
        return self.__condition

    @condition.setter
    def condition(self, condition: str):
        self.__condition = condition


    @property
    def useCases_Condition(self):
        return self.__useCases_Condition

    @useCases_Condition.setter
    def useCases_Condition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_useCases_Condition__useCases_Condition", None)
        self.__useCases_Condition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "useCases_LocalAlternative"):
                opp_val = getattr(old_value, "useCases_LocalAlternative", None)
                if opp_val == self:
                    setattr(old_value, "useCases_LocalAlternative", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "useCases_LocalAlternative"):
                opp_val = getattr(value, "useCases_LocalAlternative", None)
                setattr(value, "useCases_LocalAlternative", self)

    @property
    def useCases_Condition81(self):
        return self.__useCases_Condition81

    @useCases_Condition81.setter
    def useCases_Condition81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_useCases_Condition__useCases_Condition81", None)
        self.__useCases_Condition81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "useCases_AlternativeFlowAlternative"):
                opp_val = getattr(old_value, "useCases_AlternativeFlowAlternative", None)
                if opp_val == self:
                    setattr(old_value, "useCases_AlternativeFlowAlternative", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "useCases_AlternativeFlowAlternative"):
                opp_val = getattr(value, "useCases_AlternativeFlowAlternative", None)
                setattr(value, "useCases_AlternativeFlowAlternative", self)

class useCases_CustomStepType:

    pass
class useCases_EntityRef:

    pass
class NamedFlow:

    pass
class Flow:

    pass
class useCases_NamedFlow(Flow):

    def __init__(self, name: str, useCases_NamedFlow: "useCases_AlternativeFlowAlternative" = None):
        self.name = name
        self.useCases_NamedFlow = useCases_NamedFlow
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def useCases_NamedFlow(self):
        return self.__useCases_NamedFlow

    @useCases_NamedFlow.setter
    def useCases_NamedFlow(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_useCases_NamedFlow__useCases_NamedFlow", None)
        self.__useCases_NamedFlow = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "useCases_AlternativeFlowAlternative83"):
                opp_val = getattr(old_value, "useCases_AlternativeFlowAlternative83", None)
                if opp_val == self:
                    setattr(old_value, "useCases_AlternativeFlowAlternative83", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "useCases_AlternativeFlowAlternative83"):
                opp_val = getattr(value, "useCases_AlternativeFlowAlternative83", None)
                setattr(value, "useCases_AlternativeFlowAlternative83", self)

class useCases_ViewInstance:

    pass
class useCases_Step:

    def __init__(self, name: str, label: str, description: str, useCases_Step56: "useCases_Actor" = None, useCases_Step59: set["useCases_EntityRef"] = None, useCases_Step: "useCases_Flow" = None, useCases_Step69: "useCases_CustomStepType" = None, useCases_Step72: "useCases_StepAlternative" = None, useCases_Step61: "useCases_Screen" = None, useCases_Step64: "useCases_UseCase" = None, useCases_Step67: set["useCases_StepAlternative"] = None):
        self.name = name
        self.label = label
        self.description = description
        self.useCases_Step56 = useCases_Step56
        self.useCases_Step59 = useCases_Step59 if useCases_Step59 is not None else set()
        self.useCases_Step = useCases_Step
        self.useCases_Step69 = useCases_Step69
        self.useCases_Step72 = useCases_Step72
        self.useCases_Step61 = useCases_Step61
        self.useCases_Step64 = useCases_Step64
        self.useCases_Step67 = useCases_Step67 if useCases_Step67 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


    @property
    def label(self):
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label


    @property
    def useCases_Step61(self):
        return self.__useCases_Step61

    @useCases_Step61.setter
    def useCases_Step61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_useCases_Step__useCases_Step61", None)
        self.__useCases_Step61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "useCases_Screen62"):
                opp_val = getattr(old_value, "useCases_Screen62", None)
                if opp_val == self:
                    setattr(old_value, "useCases_Screen62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "useCases_Screen62"):
                opp_val = getattr(value, "useCases_Screen62", None)
                setattr(value, "useCases_Screen62", self)

    @property
    def useCases_Step67(self):
        return self.__useCases_Step67

    @useCases_Step67.setter
    def useCases_Step67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_useCases_Step__useCases_Step67", None)
        self.__useCases_Step67 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "useCases_StepAlternative"):
                    opp_val = getattr(item, "useCases_StepAlternative", None)
                    
                    if opp_val == self:
                        setattr(item, "useCases_StepAlternative", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "useCases_StepAlternative"):
                    opp_val = getattr(item, "useCases_StepAlternative", None)
                    
                    setattr(item, "useCases_StepAlternative", self)
                    

    @property
    def useCases_Step64(self):
        return self.__useCases_Step64

    @useCases_Step64.setter
    def useCases_Step64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_useCases_Step__useCases_Step64", None)
        self.__useCases_Step64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "useCases_UseCase65"):
                opp_val = getattr(old_value, "useCases_UseCase65", None)
                if opp_val == self:
                    setattr(old_value, "useCases_UseCase65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "useCases_UseCase65"):
                opp_val = getattr(value, "useCases_UseCase65", None)
                setattr(value, "useCases_UseCase65", self)

    @property
    def useCases_Step59(self):
        return self.__useCases_Step59

    @useCases_Step59.setter
    def useCases_Step59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_useCases_Step__useCases_Step59", None)
        self.__useCases_Step59 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "useCases_EntityRef"):
                    opp_val = getattr(item, "useCases_EntityRef", None)
                    
                    if opp_val == self:
                        setattr(item, "useCases_EntityRef", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "useCases_EntityRef"):
                    opp_val = getattr(item, "useCases_EntityRef", None)
                    
                    setattr(item, "useCases_EntityRef", self)
                    

    @property
    def useCases_Step(self):
        return self.__useCases_Step

    @useCases_Step.setter
    def useCases_Step(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_useCases_Step__useCases_Step", None)
        self.__useCases_Step = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "useCases_Flow"):
                opp_val = getattr(old_value, "useCases_Flow", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "useCases_Flow"):
                opp_val = getattr(value, "useCases_Flow", None)
                if opp_val is None:
                    setattr(value, "useCases_Flow", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def useCases_Step72(self):
        return self.__useCases_Step72

    @useCases_Step72.setter
    def useCases_Step72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_useCases_Step__useCases_Step72", None)
        self.__useCases_Step72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "useCases_StepAlternative71"):
                opp_val = getattr(old_value, "useCases_StepAlternative71", None)
                if opp_val == self:
                    setattr(old_value, "useCases_StepAlternative71", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "useCases_StepAlternative71"):
                opp_val = getattr(value, "useCases_StepAlternative71", None)
                setattr(value, "useCases_StepAlternative71", self)

    @property
    def useCases_Step69(self):
        return self.__useCases_Step69

    @useCases_Step69.setter
    def useCases_Step69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_useCases_Step__useCases_Step69", None)
        self.__useCases_Step69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "useCases_CustomStepType"):
                opp_val = getattr(old_value, "useCases_CustomStepType", None)
                if opp_val == self:
                    setattr(old_value, "useCases_CustomStepType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "useCases_CustomStepType"):
                opp_val = getattr(value, "useCases_CustomStepType", None)
                setattr(value, "useCases_CustomStepType", self)

    @property
    def useCases_Step56(self):
        return self.__useCases_Step56

    @useCases_Step56.setter
    def useCases_Step56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_useCases_Step__useCases_Step56", None)
        self.__useCases_Step56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "useCases_Actor57"):
                opp_val = getattr(old_value, "useCases_Actor57", None)
                if opp_val == self:
                    setattr(old_value, "useCases_Actor57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "useCases_Actor57"):
                opp_val = getattr(value, "useCases_Actor57", None)
                setattr(value, "useCases_Actor57", self)

class useCases_Flow:

    def __init__(self, finalState: str, useCases_Flow: set["useCases_Step"] = None):
        self.finalState = finalState
        self.useCases_Flow = useCases_Flow if useCases_Flow is not None else set()
        
        pass
    @property
    def finalState(self):
        return self.__finalState

    @finalState.setter
    def finalState(self, finalState: str):
        self.__finalState = finalState


    @property
    def useCases_Flow(self):
        return self.__useCases_Flow

    @useCases_Flow.setter
    def useCases_Flow(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_useCases_Flow__useCases_Flow", None)
        self.__useCases_Flow = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "useCases_Step"):
                    opp_val = getattr(item, "useCases_Step", None)
                    
                    if opp_val == self:
                        setattr(item, "useCases_Step", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "useCases_Step"):
                    opp_val = getattr(item, "useCases_Step", None)
                    
                    setattr(item, "useCases_Step", self)
                    

class useCases_Screen:

    pass
class useCases_PageRef:

    pass
class useCases_Entity:

    pass
class useCases_CustomAttributes:

    pass
class useCases_ExceptionFlow(NamedFlow):

    def __init__(self, condition: str, useCases_ExceptionFlow: "useCases_UseCase" = None):
        self.condition = condition
        self.useCases_ExceptionFlow = useCases_ExceptionFlow
        
        pass
    @property
    def condition(self):
        return self.__condition

    @condition.setter
    def condition(self, condition: str):
        self.__condition = condition


    @property
    def useCases_ExceptionFlow(self):
        return self.__useCases_ExceptionFlow

    @useCases_ExceptionFlow.setter
    def useCases_ExceptionFlow(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_useCases_ExceptionFlow__useCases_ExceptionFlow", None)
        self.__useCases_ExceptionFlow = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "useCases_UseCase44"):
                opp_val = getattr(old_value, "useCases_UseCase44", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "useCases_UseCase44"):
                opp_val = getattr(value, "useCases_UseCase44", None)
                if opp_val is None:
                    setattr(value, "useCases_UseCase44", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class useCases_AlternativeFlow(NamedFlow):

    pass
class useCases_BasicFlow(Flow):

    pass
class useCases_Label:

    pass
class useCases_Precondition:

    def __init__(self, name: str, useCases_Precondition: "useCases_UseCase" = None, useCases_Precondition52: "useCases_UseCase" = None):
        self.name = name
        self.useCases_Precondition = useCases_Precondition
        self.useCases_Precondition52 = useCases_Precondition52
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def useCases_Precondition(self):
        return self.__useCases_Precondition

    @useCases_Precondition.setter
    def useCases_Precondition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_useCases_Precondition__useCases_Precondition", None)
        self.__useCases_Precondition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "useCases_UseCase36"):
                opp_val = getattr(old_value, "useCases_UseCase36", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "useCases_UseCase36"):
                opp_val = getattr(value, "useCases_UseCase36", None)
                if opp_val is None:
                    setattr(value, "useCases_UseCase36", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def useCases_Precondition52(self):
        return self.__useCases_Precondition52

    @useCases_Precondition52.setter
    def useCases_Precondition52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_useCases_Precondition__useCases_Precondition52", None)
        self.__useCases_Precondition52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "useCases_UseCase53"):
                opp_val = getattr(old_value, "useCases_UseCase53", None)
                if opp_val == self:
                    setattr(old_value, "useCases_UseCase53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "useCases_UseCase53"):
                opp_val = getattr(value, "useCases_UseCase53", None)
                setattr(value, "useCases_UseCase53", self)

class useCases_UseCase:

    def __init__(self, name: str, ucName: str, goals: str, useCases_UseCase27: set["useCases_RequirementRef"] = None, useCases_UseCase: "useCases_PackageDeclaration" = None, useCases_UseCase36: set["useCases_Precondition"] = None, useCases_UseCase38: set["useCases_Label"] = None, useCases_UseCase40: "useCases_BasicFlow" = None, useCases_UseCase42: set["useCases_AlternativeFlow"] = None, useCases_UseCase44: set["useCases_ExceptionFlow"] = None, useCases_UseCase46: "useCases_CustomAttributes" = None, useCases_UseCase29: set["useCases_Actor"] = None, useCases_UseCase32: set["useCases_Entity"] = None, useCases_UseCase34: set["useCases_PageRef"] = None, useCases_UseCase53: "useCases_Precondition" = None, useCases_UseCase65: "useCases_Step" = None, useCases_UseCase79: "useCases_LocalAlternative" = None):
        self.name = name
        self.ucName = ucName
        self.goals = goals
        self.useCases_UseCase27 = useCases_UseCase27 if useCases_UseCase27 is not None else set()
        self.useCases_UseCase = useCases_UseCase
        self.useCases_UseCase36 = useCases_UseCase36 if useCases_UseCase36 is not None else set()
        self.useCases_UseCase38 = useCases_UseCase38 if useCases_UseCase38 is not None else set()
        self.useCases_UseCase40 = useCases_UseCase40
        self.useCases_UseCase42 = useCases_UseCase42 if useCases_UseCase42 is not None else set()
        self.useCases_UseCase44 = useCases_UseCase44 if useCases_UseCase44 is not None else set()
        self.useCases_UseCase46 = useCases_UseCase46
        self.useCases_UseCase29 = useCases_UseCase29 if useCases_UseCase29 is not None else set()
        self.useCases_UseCase32 = useCases_UseCase32 if useCases_UseCase32 is not None else set()
        self.useCases_UseCase34 = useCases_UseCase34 if useCases_UseCase34 is not None else set()
        self.useCases_UseCase53 = useCases_UseCase53
        self.useCases_UseCase65 = useCases_UseCase65
        self.useCases_UseCase79 = useCases_UseCase79
        
        pass
    @property
    def goals(self):
        return self.__goals

    @goals.setter
    def goals(self, goals: str):
        self.__goals = goals


    @property
    def ucName(self):
        return self.__ucName

    @ucName.setter
    def ucName(self, ucName: str):
        self.__ucName = ucName


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def useCases_UseCase79(self):
        return self.__useCases_UseCase79

    @useCases_UseCase79.setter
    def useCases_UseCase79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_useCases_UseCase__useCases_UseCase79", None)
        self.__useCases_UseCase79 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "useCases_LocalAlternative78"):
                opp_val = getattr(old_value, "useCases_LocalAlternative78", None)
                if opp_val == self:
                    setattr(old_value, "useCases_LocalAlternative78", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "useCases_LocalAlternative78"):
                opp_val = getattr(value, "useCases_LocalAlternative78", None)
                setattr(value, "useCases_LocalAlternative78", self)

    @property
    def useCases_UseCase53(self):
        return self.__useCases_UseCase53

    @useCases_UseCase53.setter
    def useCases_UseCase53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_useCases_UseCase__useCases_UseCase53", None)
        self.__useCases_UseCase53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "useCases_Precondition52"):
                opp_val = getattr(old_value, "useCases_Precondition52", None)
                if opp_val == self:
                    setattr(old_value, "useCases_Precondition52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "useCases_Precondition52"):
                opp_val = getattr(value, "useCases_Precondition52", None)
                setattr(value, "useCases_Precondition52", self)

    @property
    def useCases_UseCase65(self):
        return self.__useCases_UseCase65

    @useCases_UseCase65.setter
    def useCases_UseCase65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_useCases_UseCase__useCases_UseCase65", None)
        self.__useCases_UseCase65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "useCases_Step64"):
                opp_val = getattr(old_value, "useCases_Step64", None)
                if opp_val == self:
                    setattr(old_value, "useCases_Step64", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "useCases_Step64"):
                opp_val = getattr(value, "useCases_Step64", None)
                setattr(value, "useCases_Step64", self)

    @property
    def useCases_UseCase38(self):
        return self.__useCases_UseCase38

    @useCases_UseCase38.setter
    def useCases_UseCase38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_useCases_UseCase__useCases_UseCase38", None)
        self.__useCases_UseCase38 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "useCases_Label"):
                    opp_val = getattr(item, "useCases_Label", None)
                    
                    if opp_val == self:
                        setattr(item, "useCases_Label", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "useCases_Label"):
                    opp_val = getattr(item, "useCases_Label", None)
                    
                    setattr(item, "useCases_Label", self)
                    

    @property
    def useCases_UseCase32(self):
        return self.__useCases_UseCase32

    @useCases_UseCase32.setter
    def useCases_UseCase32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_useCases_UseCase__useCases_UseCase32", None)
        self.__useCases_UseCase32 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "useCases_Entity"):
                    opp_val = getattr(item, "useCases_Entity", None)
                    
                    if opp_val == self:
                        setattr(item, "useCases_Entity", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "useCases_Entity"):
                    opp_val = getattr(item, "useCases_Entity", None)
                    
                    setattr(item, "useCases_Entity", self)
                    

    @property
    def useCases_UseCase29(self):
        return self.__useCases_UseCase29

    @useCases_UseCase29.setter
    def useCases_UseCase29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_useCases_UseCase__useCases_UseCase29", None)
        self.__useCases_UseCase29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "useCases_Actor30"):
                    opp_val = getattr(item, "useCases_Actor30", None)
                    
                    if opp_val == self:
                        setattr(item, "useCases_Actor30", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "useCases_Actor30"):
                    opp_val = getattr(item, "useCases_Actor30", None)
                    
                    setattr(item, "useCases_Actor30", self)
                    

    @property
    def useCases_UseCase36(self):
        return self.__useCases_UseCase36

    @useCases_UseCase36.setter
    def useCases_UseCase36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_useCases_UseCase__useCases_UseCase36", None)
        self.__useCases_UseCase36 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "useCases_Precondition"):
                    opp_val = getattr(item, "useCases_Precondition", None)
                    
                    if opp_val == self:
                        setattr(item, "useCases_Precondition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "useCases_Precondition"):
                    opp_val = getattr(item, "useCases_Precondition", None)
                    
                    setattr(item, "useCases_Precondition", self)
                    

    @property
    def useCases_UseCase46(self):
        return self.__useCases_UseCase46

    @useCases_UseCase46.setter
    def useCases_UseCase46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_useCases_UseCase__useCases_UseCase46", None)
        self.__useCases_UseCase46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "useCases_CustomAttributes"):
                opp_val = getattr(old_value, "useCases_CustomAttributes", None)
                if opp_val == self:
                    setattr(old_value, "useCases_CustomAttributes", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "useCases_CustomAttributes"):
                opp_val = getattr(value, "useCases_CustomAttributes", None)
                setattr(value, "useCases_CustomAttributes", self)

    @property
    def useCases_UseCase42(self):
        return self.__useCases_UseCase42

    @useCases_UseCase42.setter
    def useCases_UseCase42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_useCases_UseCase__useCases_UseCase42", None)
        self.__useCases_UseCase42 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "useCases_AlternativeFlow"):
                    opp_val = getattr(item, "useCases_AlternativeFlow", None)
                    
                    if opp_val == self:
                        setattr(item, "useCases_AlternativeFlow", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "useCases_AlternativeFlow"):
                    opp_val = getattr(item, "useCases_AlternativeFlow", None)
                    
                    setattr(item, "useCases_AlternativeFlow", self)
                    

    @property
    def useCases_UseCase27(self):
        return self.__useCases_UseCase27

    @useCases_UseCase27.setter
    def useCases_UseCase27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_useCases_UseCase__useCases_UseCase27", None)
        self.__useCases_UseCase27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "useCases_RequirementRef"):
                    opp_val = getattr(item, "useCases_RequirementRef", None)
                    
                    if opp_val == self:
                        setattr(item, "useCases_RequirementRef", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "useCases_RequirementRef"):
                    opp_val = getattr(item, "useCases_RequirementRef", None)
                    
                    setattr(item, "useCases_RequirementRef", self)
                    

    @property
    def useCases_UseCase44(self):
        return self.__useCases_UseCase44

    @useCases_UseCase44.setter
    def useCases_UseCase44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_useCases_UseCase__useCases_UseCase44", None)
        self.__useCases_UseCase44 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "useCases_ExceptionFlow"):
                    opp_val = getattr(item, "useCases_ExceptionFlow", None)
                    
                    if opp_val == self:
                        setattr(item, "useCases_ExceptionFlow", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "useCases_ExceptionFlow"):
                    opp_val = getattr(item, "useCases_ExceptionFlow", None)
                    
                    setattr(item, "useCases_ExceptionFlow", self)
                    

    @property
    def useCases_UseCase40(self):
        return self.__useCases_UseCase40

    @useCases_UseCase40.setter
    def useCases_UseCase40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_useCases_UseCase__useCases_UseCase40", None)
        self.__useCases_UseCase40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "useCases_BasicFlow"):
                opp_val = getattr(old_value, "useCases_BasicFlow", None)
                if opp_val == self:
                    setattr(old_value, "useCases_BasicFlow", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "useCases_BasicFlow"):
                opp_val = getattr(value, "useCases_BasicFlow", None)
                setattr(value, "useCases_BasicFlow", self)

    @property
    def useCases_UseCase34(self):
        return self.__useCases_UseCase34

    @useCases_UseCase34.setter
    def useCases_UseCase34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_useCases_UseCase__useCases_UseCase34", None)
        self.__useCases_UseCase34 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "useCases_PageRef"):
                    opp_val = getattr(item, "useCases_PageRef", None)
                    
                    if opp_val == self:
                        setattr(item, "useCases_PageRef", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "useCases_PageRef"):
                    opp_val = getattr(item, "useCases_PageRef", None)
                    
                    setattr(item, "useCases_PageRef", self)
                    

    @property
    def useCases_UseCase(self):
        return self.__useCases_UseCase

    @useCases_UseCase.setter
    def useCases_UseCase(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_useCases_UseCase__useCases_UseCase", None)
        self.__useCases_UseCase = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "useCases_PackageDeclaration22"):
                opp_val = getattr(old_value, "useCases_PackageDeclaration22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "useCases_PackageDeclaration22"):
                opp_val = getattr(value, "useCases_PackageDeclaration22", None)
                if opp_val is None:
                    setattr(value, "useCases_PackageDeclaration22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class useCases_Actor:

    def __init__(self, name: str, type: str, description: str, useCases_Actor25: "useCases_Actor" = None, useCases_Actor23: "useCases_Actor" = None, useCases_Actor: "useCases_PackageDeclaration" = None, useCases_Actor30: "useCases_UseCase" = None, useCases_Actor57: "useCases_Step" = None):
        self.name = name
        self.type = type
        self.description = description
        self.useCases_Actor25 = useCases_Actor25
        self.useCases_Actor23 = useCases_Actor23
        self.useCases_Actor = useCases_Actor
        self.useCases_Actor30 = useCases_Actor30
        self.useCases_Actor57 = useCases_Actor57
        
        pass
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
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def useCases_Actor30(self):
        return self.__useCases_Actor30

    @useCases_Actor30.setter
    def useCases_Actor30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_useCases_Actor__useCases_Actor30", None)
        self.__useCases_Actor30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "useCases_UseCase29"):
                opp_val = getattr(old_value, "useCases_UseCase29", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "useCases_UseCase29"):
                opp_val = getattr(value, "useCases_UseCase29", None)
                if opp_val is None:
                    setattr(value, "useCases_UseCase29", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def useCases_Actor(self):
        return self.__useCases_Actor

    @useCases_Actor.setter
    def useCases_Actor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_useCases_Actor__useCases_Actor", None)
        self.__useCases_Actor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "useCases_PackageDeclaration20"):
                opp_val = getattr(old_value, "useCases_PackageDeclaration20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "useCases_PackageDeclaration20"):
                opp_val = getattr(value, "useCases_PackageDeclaration20", None)
                if opp_val is None:
                    setattr(value, "useCases_PackageDeclaration20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def useCases_Actor57(self):
        return self.__useCases_Actor57

    @useCases_Actor57.setter
    def useCases_Actor57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_useCases_Actor__useCases_Actor57", None)
        self.__useCases_Actor57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "useCases_Step56"):
                opp_val = getattr(old_value, "useCases_Step56", None)
                if opp_val == self:
                    setattr(old_value, "useCases_Step56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "useCases_Step56"):
                opp_val = getattr(value, "useCases_Step56", None)
                setattr(value, "useCases_Step56", self)

    @property
    def useCases_Actor25(self):
        return self.__useCases_Actor25

    @useCases_Actor25.setter
    def useCases_Actor25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_useCases_Actor__useCases_Actor25", None)
        self.__useCases_Actor25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "useCases_Actor23"):
                opp_val = getattr(old_value, "useCases_Actor23", None)
                if opp_val == self:
                    setattr(old_value, "useCases_Actor23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "useCases_Actor23"):
                opp_val = getattr(value, "useCases_Actor23", None)
                setattr(value, "useCases_Actor23", self)

    @property
    def useCases_Actor23(self):
        return self.__useCases_Actor23

    @useCases_Actor23.setter
    def useCases_Actor23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_useCases_Actor__useCases_Actor23", None)
        self.__useCases_Actor23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "useCases_Actor25"):
                opp_val = getattr(old_value, "useCases_Actor25", None)
                if opp_val == self:
                    setattr(old_value, "useCases_Actor25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "useCases_Actor25"):
                opp_val = getattr(value, "useCases_Actor25", None)
                setattr(value, "useCases_Actor25", self)

class useCases_RequirementRef:

    pass
class useCases_PackageDeclaration:

    def __init__(self, name: str, description: str, useCases_PackageDeclaration12: "useCases_NamespaceImport" = None, useCases_PackageDeclaration15: "useCases_NamespaceImport" = None, useCases_PackageDeclaration17: set["useCases_NamespaceImport"] = None, useCases_PackageDeclaration: "useCases_UseCasesModel" = None, useCases_PackageDeclaration20: set["useCases_Actor"] = None, useCases_PackageDeclaration22: set["useCases_UseCase"] = None, useCases_PackageDeclaration5: "useCases_NamespaceImport" = None):
        self.name = name
        self.description = description
        self.useCases_PackageDeclaration12 = useCases_PackageDeclaration12
        self.useCases_PackageDeclaration15 = useCases_PackageDeclaration15
        self.useCases_PackageDeclaration17 = useCases_PackageDeclaration17 if useCases_PackageDeclaration17 is not None else set()
        self.useCases_PackageDeclaration = useCases_PackageDeclaration
        self.useCases_PackageDeclaration20 = useCases_PackageDeclaration20 if useCases_PackageDeclaration20 is not None else set()
        self.useCases_PackageDeclaration22 = useCases_PackageDeclaration22 if useCases_PackageDeclaration22 is not None else set()
        self.useCases_PackageDeclaration5 = useCases_PackageDeclaration5
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


    @property
    def useCases_PackageDeclaration17(self):
        return self.__useCases_PackageDeclaration17

    @useCases_PackageDeclaration17.setter
    def useCases_PackageDeclaration17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_useCases_PackageDeclaration__useCases_PackageDeclaration17", None)
        self.__useCases_PackageDeclaration17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "useCases_NamespaceImport18"):
                    opp_val = getattr(item, "useCases_NamespaceImport18", None)
                    
                    if opp_val == self:
                        setattr(item, "useCases_NamespaceImport18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "useCases_NamespaceImport18"):
                    opp_val = getattr(item, "useCases_NamespaceImport18", None)
                    
                    setattr(item, "useCases_NamespaceImport18", self)
                    

    @property
    def useCases_PackageDeclaration(self):
        return self.__useCases_PackageDeclaration

    @useCases_PackageDeclaration.setter
    def useCases_PackageDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_useCases_PackageDeclaration__useCases_PackageDeclaration", None)
        self.__useCases_PackageDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "useCases_UseCasesModel2"):
                opp_val = getattr(old_value, "useCases_UseCasesModel2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "useCases_UseCasesModel2"):
                opp_val = getattr(value, "useCases_UseCasesModel2", None)
                if opp_val is None:
                    setattr(value, "useCases_UseCasesModel2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def useCases_PackageDeclaration22(self):
        return self.__useCases_PackageDeclaration22

    @useCases_PackageDeclaration22.setter
    def useCases_PackageDeclaration22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_useCases_PackageDeclaration__useCases_PackageDeclaration22", None)
        self.__useCases_PackageDeclaration22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "useCases_UseCase"):
                    opp_val = getattr(item, "useCases_UseCase", None)
                    
                    if opp_val == self:
                        setattr(item, "useCases_UseCase", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "useCases_UseCase"):
                    opp_val = getattr(item, "useCases_UseCase", None)
                    
                    setattr(item, "useCases_UseCase", self)
                    

    @property
    def useCases_PackageDeclaration5(self):
        return self.__useCases_PackageDeclaration5

    @useCases_PackageDeclaration5.setter
    def useCases_PackageDeclaration5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_useCases_PackageDeclaration__useCases_PackageDeclaration5", None)
        self.__useCases_PackageDeclaration5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "useCases_NamespaceImport4"):
                opp_val = getattr(old_value, "useCases_NamespaceImport4", None)
                if opp_val == self:
                    setattr(old_value, "useCases_NamespaceImport4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "useCases_NamespaceImport4"):
                opp_val = getattr(value, "useCases_NamespaceImport4", None)
                setattr(value, "useCases_NamespaceImport4", self)

    @property
    def useCases_PackageDeclaration20(self):
        return self.__useCases_PackageDeclaration20

    @useCases_PackageDeclaration20.setter
    def useCases_PackageDeclaration20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_useCases_PackageDeclaration__useCases_PackageDeclaration20", None)
        self.__useCases_PackageDeclaration20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "useCases_Actor"):
                    opp_val = getattr(item, "useCases_Actor", None)
                    
                    if opp_val == self:
                        setattr(item, "useCases_Actor", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "useCases_Actor"):
                    opp_val = getattr(item, "useCases_Actor", None)
                    
                    setattr(item, "useCases_Actor", self)
                    

    @property
    def useCases_PackageDeclaration15(self):
        return self.__useCases_PackageDeclaration15

    @useCases_PackageDeclaration15.setter
    def useCases_PackageDeclaration15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_useCases_PackageDeclaration__useCases_PackageDeclaration15", None)
        self.__useCases_PackageDeclaration15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "useCases_NamespaceImport14"):
                opp_val = getattr(old_value, "useCases_NamespaceImport14", None)
                if opp_val == self:
                    setattr(old_value, "useCases_NamespaceImport14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "useCases_NamespaceImport14"):
                opp_val = getattr(value, "useCases_NamespaceImport14", None)
                setattr(value, "useCases_NamespaceImport14", self)

    @property
    def useCases_PackageDeclaration12(self):
        return self.__useCases_PackageDeclaration12

    @useCases_PackageDeclaration12.setter
    def useCases_PackageDeclaration12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_useCases_PackageDeclaration__useCases_PackageDeclaration12", None)
        self.__useCases_PackageDeclaration12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "useCases_NamespaceImport11"):
                opp_val = getattr(old_value, "useCases_NamespaceImport11", None)
                if opp_val == self:
                    setattr(old_value, "useCases_NamespaceImport11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "useCases_NamespaceImport11"):
                opp_val = getattr(value, "useCases_NamespaceImport11", None)
                setattr(value, "useCases_NamespaceImport11", self)

class useCases_NamespaceImport:

    pass
class useCases_Identifiable:

    pass
class useCases_ApplicationInstance:

    pass
class useCases_UseCasesModel:

    pass