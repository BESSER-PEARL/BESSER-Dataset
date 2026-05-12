from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class ActorType(Enum):
    PERSON = "PERSON"
    SYSTEM = "SYSTEM"
    ORGANIZATION = "ORGANIZATION"
class CustomStepType(Enum):
    INPUT = "INPUT"
    OUTPUT = "OUTPUT"
    PROCESS = "PROCESS"
    MIX = "MIX"


############################################
# Definition of Classes
############################################

class UseCaseDSL_UseCasesModel:

    pass
class UseCaseDSL_PackageDeclaration:

    def __init__(self, description: str, name: str, UseCaseDSL_PackageDeclaration: set["UseCaseDSL_UseCase"] = None, UseCaseDSL_PackageDeclaration12: set["UseCaseDSL_Actor"] = None, UseCaseDSL_PackageDeclaration31: "UseCaseDSL_UseCasesModel" = None):
        self.description = description
        self.name = name
        self.UseCaseDSL_PackageDeclaration = UseCaseDSL_PackageDeclaration if UseCaseDSL_PackageDeclaration is not None else set()
        self.UseCaseDSL_PackageDeclaration12 = UseCaseDSL_PackageDeclaration12 if UseCaseDSL_PackageDeclaration12 is not None else set()
        self.UseCaseDSL_PackageDeclaration31 = UseCaseDSL_PackageDeclaration31
        
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
    def UseCaseDSL_PackageDeclaration(self):
        return self.__UseCaseDSL_PackageDeclaration

    @UseCaseDSL_PackageDeclaration.setter
    def UseCaseDSL_PackageDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UseCaseDSL_PackageDeclaration__UseCaseDSL_PackageDeclaration", None)
        self.__UseCaseDSL_PackageDeclaration = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UseCaseDSL_UseCase10"):
                    opp_val = getattr(item, "UseCaseDSL_UseCase10", None)
                    
                    if opp_val == self:
                        setattr(item, "UseCaseDSL_UseCase10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UseCaseDSL_UseCase10"):
                    opp_val = getattr(item, "UseCaseDSL_UseCase10", None)
                    
                    setattr(item, "UseCaseDSL_UseCase10", self)
                    

    @property
    def UseCaseDSL_PackageDeclaration31(self):
        return self.__UseCaseDSL_PackageDeclaration31

    @UseCaseDSL_PackageDeclaration31.setter
    def UseCaseDSL_PackageDeclaration31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UseCaseDSL_PackageDeclaration__UseCaseDSL_PackageDeclaration31", None)
        self.__UseCaseDSL_PackageDeclaration31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UseCaseDSL_UseCasesModel"):
                opp_val = getattr(old_value, "UseCaseDSL_UseCasesModel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UseCaseDSL_UseCasesModel"):
                opp_val = getattr(value, "UseCaseDSL_UseCasesModel", None)
                if opp_val is None:
                    setattr(value, "UseCaseDSL_UseCasesModel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UseCaseDSL_PackageDeclaration12(self):
        return self.__UseCaseDSL_PackageDeclaration12

    @UseCaseDSL_PackageDeclaration12.setter
    def UseCaseDSL_PackageDeclaration12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UseCaseDSL_PackageDeclaration__UseCaseDSL_PackageDeclaration12", None)
        self.__UseCaseDSL_PackageDeclaration12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UseCaseDSL_Actor13"):
                    opp_val = getattr(item, "UseCaseDSL_Actor13", None)
                    
                    if opp_val == self:
                        setattr(item, "UseCaseDSL_Actor13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UseCaseDSL_Actor13"):
                    opp_val = getattr(item, "UseCaseDSL_Actor13", None)
                    
                    setattr(item, "UseCaseDSL_Actor13", self)
                    

class UseCaseDSL_StepAlternative(ABC):

    def __init__(self, condition: str, UseCaseDSL_StepAlternative: "UseCaseDSL_NormalStep" = None, UseCaseDSL_StepAlternative22: "UseCaseDSL_Step" = None):
        self.condition = condition
        self.UseCaseDSL_StepAlternative = UseCaseDSL_StepAlternative
        self.UseCaseDSL_StepAlternative22 = UseCaseDSL_StepAlternative22
        
        pass
    @property
    def condition(self):
        return self.__condition

    @condition.setter
    def condition(self, condition: str):
        self.__condition = condition


    @property
    def UseCaseDSL_StepAlternative(self):
        return self.__UseCaseDSL_StepAlternative

    @UseCaseDSL_StepAlternative.setter
    def UseCaseDSL_StepAlternative(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UseCaseDSL_StepAlternative__UseCaseDSL_StepAlternative", None)
        self.__UseCaseDSL_StepAlternative = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UseCaseDSL_NormalStep"):
                opp_val = getattr(old_value, "UseCaseDSL_NormalStep", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UseCaseDSL_NormalStep"):
                opp_val = getattr(value, "UseCaseDSL_NormalStep", None)
                if opp_val is None:
                    setattr(value, "UseCaseDSL_NormalStep", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UseCaseDSL_StepAlternative22(self):
        return self.__UseCaseDSL_StepAlternative22

    @UseCaseDSL_StepAlternative22.setter
    def UseCaseDSL_StepAlternative22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UseCaseDSL_StepAlternative__UseCaseDSL_StepAlternative22", None)
        self.__UseCaseDSL_StepAlternative22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UseCaseDSL_Step23"):
                opp_val = getattr(old_value, "UseCaseDSL_Step23", None)
                if opp_val == self:
                    setattr(old_value, "UseCaseDSL_Step23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UseCaseDSL_Step23"):
                opp_val = getattr(value, "UseCaseDSL_Step23", None)
                setattr(value, "UseCaseDSL_Step23", self)

class Step:

    pass
class UseCaseDSL_ParallelStep(Step):

    pass
class UseCaseDSL_NormalStep(Step):

    def __init__(self, customStepType: str, UseCaseDSL_NormalStep: set["UseCaseDSL_StepAlternative"] = None, UseCaseDSL_NormalStep7: "UseCaseDSL_Actor" = None):
        self.customStepType = customStepType
        self.UseCaseDSL_NormalStep = UseCaseDSL_NormalStep if UseCaseDSL_NormalStep is not None else set()
        self.UseCaseDSL_NormalStep7 = UseCaseDSL_NormalStep7
        
        pass
    @property
    def customStepType(self):
        return self.__customStepType

    @customStepType.setter
    def customStepType(self, customStepType: str):
        self.__customStepType = customStepType


    @property
    def UseCaseDSL_NormalStep(self):
        return self.__UseCaseDSL_NormalStep

    @UseCaseDSL_NormalStep.setter
    def UseCaseDSL_NormalStep(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UseCaseDSL_NormalStep__UseCaseDSL_NormalStep", None)
        self.__UseCaseDSL_NormalStep = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UseCaseDSL_StepAlternative"):
                    opp_val = getattr(item, "UseCaseDSL_StepAlternative", None)
                    
                    if opp_val == self:
                        setattr(item, "UseCaseDSL_StepAlternative", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UseCaseDSL_StepAlternative"):
                    opp_val = getattr(item, "UseCaseDSL_StepAlternative", None)
                    
                    setattr(item, "UseCaseDSL_StepAlternative", self)
                    

    @property
    def UseCaseDSL_NormalStep7(self):
        return self.__UseCaseDSL_NormalStep7

    @UseCaseDSL_NormalStep7.setter
    def UseCaseDSL_NormalStep7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UseCaseDSL_NormalStep__UseCaseDSL_NormalStep7", None)
        self.__UseCaseDSL_NormalStep7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UseCaseDSL_Actor8"):
                opp_val = getattr(old_value, "UseCaseDSL_Actor8", None)
                if opp_val == self:
                    setattr(old_value, "UseCaseDSL_Actor8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UseCaseDSL_Actor8"):
                opp_val = getattr(value, "UseCaseDSL_Actor8", None)
                setattr(value, "UseCaseDSL_Actor8", self)

class UseCaseDSL_UseCase:

    def __init__(self, description: str, name: str, postcondition: str, preConditions: str, UseCaseDSL_UseCase: "UseCaseDSL_LocalAlternative" = None, UseCaseDSL_UseCase26: "UseCaseDSL_UseCase" = None, UseCaseDSL_UseCase24: "UseCaseDSL_UseCase" = None, UseCaseDSL_UseCase10: "UseCaseDSL_PackageDeclaration" = None, UseCaseDSL_UseCase20: "UseCaseDSL_Step" = None, UseCaseDSL_UseCase28: set["UseCaseDSL_Flow"] = None):
        self.description = description
        self.name = name
        self.postcondition = postcondition
        self.preConditions = preConditions
        self.UseCaseDSL_UseCase = UseCaseDSL_UseCase
        self.UseCaseDSL_UseCase26 = UseCaseDSL_UseCase26
        self.UseCaseDSL_UseCase24 = UseCaseDSL_UseCase24
        self.UseCaseDSL_UseCase10 = UseCaseDSL_UseCase10
        self.UseCaseDSL_UseCase20 = UseCaseDSL_UseCase20
        self.UseCaseDSL_UseCase28 = UseCaseDSL_UseCase28 if UseCaseDSL_UseCase28 is not None else set()
        
        pass
    @property
    def preConditions(self):
        return self.__preConditions

    @preConditions.setter
    def preConditions(self, preConditions: str):
        self.__preConditions = preConditions


    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


    @property
    def postcondition(self):
        return self.__postcondition

    @postcondition.setter
    def postcondition(self, postcondition: str):
        self.__postcondition = postcondition


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def UseCaseDSL_UseCase10(self):
        return self.__UseCaseDSL_UseCase10

    @UseCaseDSL_UseCase10.setter
    def UseCaseDSL_UseCase10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UseCaseDSL_UseCase__UseCaseDSL_UseCase10", None)
        self.__UseCaseDSL_UseCase10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UseCaseDSL_PackageDeclaration"):
                opp_val = getattr(old_value, "UseCaseDSL_PackageDeclaration", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UseCaseDSL_PackageDeclaration"):
                opp_val = getattr(value, "UseCaseDSL_PackageDeclaration", None)
                if opp_val is None:
                    setattr(value, "UseCaseDSL_PackageDeclaration", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UseCaseDSL_UseCase24(self):
        return self.__UseCaseDSL_UseCase24

    @UseCaseDSL_UseCase24.setter
    def UseCaseDSL_UseCase24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UseCaseDSL_UseCase__UseCaseDSL_UseCase24", None)
        self.__UseCaseDSL_UseCase24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UseCaseDSL_UseCase26"):
                opp_val = getattr(old_value, "UseCaseDSL_UseCase26", None)
                if opp_val == self:
                    setattr(old_value, "UseCaseDSL_UseCase26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UseCaseDSL_UseCase26"):
                opp_val = getattr(value, "UseCaseDSL_UseCase26", None)
                setattr(value, "UseCaseDSL_UseCase26", self)

    @property
    def UseCaseDSL_UseCase(self):
        return self.__UseCaseDSL_UseCase

    @UseCaseDSL_UseCase.setter
    def UseCaseDSL_UseCase(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UseCaseDSL_UseCase__UseCaseDSL_UseCase", None)
        self.__UseCaseDSL_UseCase = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UseCaseDSL_LocalAlternative"):
                opp_val = getattr(old_value, "UseCaseDSL_LocalAlternative", None)
                if opp_val == self:
                    setattr(old_value, "UseCaseDSL_LocalAlternative", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UseCaseDSL_LocalAlternative"):
                opp_val = getattr(value, "UseCaseDSL_LocalAlternative", None)
                setattr(value, "UseCaseDSL_LocalAlternative", self)

    @property
    def UseCaseDSL_UseCase20(self):
        return self.__UseCaseDSL_UseCase20

    @UseCaseDSL_UseCase20.setter
    def UseCaseDSL_UseCase20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UseCaseDSL_UseCase__UseCaseDSL_UseCase20", None)
        self.__UseCaseDSL_UseCase20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UseCaseDSL_Step19"):
                opp_val = getattr(old_value, "UseCaseDSL_Step19", None)
                if opp_val == self:
                    setattr(old_value, "UseCaseDSL_Step19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UseCaseDSL_Step19"):
                opp_val = getattr(value, "UseCaseDSL_Step19", None)
                setattr(value, "UseCaseDSL_Step19", self)

    @property
    def UseCaseDSL_UseCase26(self):
        return self.__UseCaseDSL_UseCase26

    @UseCaseDSL_UseCase26.setter
    def UseCaseDSL_UseCase26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UseCaseDSL_UseCase__UseCaseDSL_UseCase26", None)
        self.__UseCaseDSL_UseCase26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UseCaseDSL_UseCase24"):
                opp_val = getattr(old_value, "UseCaseDSL_UseCase24", None)
                if opp_val == self:
                    setattr(old_value, "UseCaseDSL_UseCase24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UseCaseDSL_UseCase24"):
                opp_val = getattr(value, "UseCaseDSL_UseCase24", None)
                setattr(value, "UseCaseDSL_UseCase24", self)

    @property
    def UseCaseDSL_UseCase28(self):
        return self.__UseCaseDSL_UseCase28

    @UseCaseDSL_UseCase28.setter
    def UseCaseDSL_UseCase28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UseCaseDSL_UseCase__UseCaseDSL_UseCase28", None)
        self.__UseCaseDSL_UseCase28 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UseCaseDSL_Flow29"):
                    opp_val = getattr(item, "UseCaseDSL_Flow29", None)
                    
                    if opp_val == self:
                        setattr(item, "UseCaseDSL_Flow29", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UseCaseDSL_Flow29"):
                    opp_val = getattr(item, "UseCaseDSL_Flow29", None)
                    
                    setattr(item, "UseCaseDSL_Flow29", self)
                    

class UseCaseDSL_Step(ABC):

    def __init__(self, label: str, name: str, UseCaseDSL_Step: "UseCaseDSL_Flow" = None, UseCaseDSL_Step17: "UseCaseDSL_Step" = None, UseCaseDSL_Step15: "UseCaseDSL_Step" = None, UseCaseDSL_Step19: "UseCaseDSL_UseCase" = None, UseCaseDSL_Step23: "UseCaseDSL_StepAlternative" = None):
        self.label = label
        self.name = name
        self.UseCaseDSL_Step = UseCaseDSL_Step
        self.UseCaseDSL_Step17 = UseCaseDSL_Step17
        self.UseCaseDSL_Step15 = UseCaseDSL_Step15
        self.UseCaseDSL_Step19 = UseCaseDSL_Step19
        self.UseCaseDSL_Step23 = UseCaseDSL_Step23
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def label(self):
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label


    @property
    def UseCaseDSL_Step17(self):
        return self.__UseCaseDSL_Step17

    @UseCaseDSL_Step17.setter
    def UseCaseDSL_Step17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UseCaseDSL_Step__UseCaseDSL_Step17", None)
        self.__UseCaseDSL_Step17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UseCaseDSL_Step15"):
                opp_val = getattr(old_value, "UseCaseDSL_Step15", None)
                if opp_val == self:
                    setattr(old_value, "UseCaseDSL_Step15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UseCaseDSL_Step15"):
                opp_val = getattr(value, "UseCaseDSL_Step15", None)
                setattr(value, "UseCaseDSL_Step15", self)

    @property
    def UseCaseDSL_Step15(self):
        return self.__UseCaseDSL_Step15

    @UseCaseDSL_Step15.setter
    def UseCaseDSL_Step15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UseCaseDSL_Step__UseCaseDSL_Step15", None)
        self.__UseCaseDSL_Step15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UseCaseDSL_Step17"):
                opp_val = getattr(old_value, "UseCaseDSL_Step17", None)
                if opp_val == self:
                    setattr(old_value, "UseCaseDSL_Step17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UseCaseDSL_Step17"):
                opp_val = getattr(value, "UseCaseDSL_Step17", None)
                setattr(value, "UseCaseDSL_Step17", self)

    @property
    def UseCaseDSL_Step23(self):
        return self.__UseCaseDSL_Step23

    @UseCaseDSL_Step23.setter
    def UseCaseDSL_Step23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UseCaseDSL_Step__UseCaseDSL_Step23", None)
        self.__UseCaseDSL_Step23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UseCaseDSL_StepAlternative22"):
                opp_val = getattr(old_value, "UseCaseDSL_StepAlternative22", None)
                if opp_val == self:
                    setattr(old_value, "UseCaseDSL_StepAlternative22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UseCaseDSL_StepAlternative22"):
                opp_val = getattr(value, "UseCaseDSL_StepAlternative22", None)
                setattr(value, "UseCaseDSL_StepAlternative22", self)

    @property
    def UseCaseDSL_Step(self):
        return self.__UseCaseDSL_Step

    @UseCaseDSL_Step.setter
    def UseCaseDSL_Step(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UseCaseDSL_Step__UseCaseDSL_Step", None)
        self.__UseCaseDSL_Step = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UseCaseDSL_Flow"):
                opp_val = getattr(old_value, "UseCaseDSL_Flow", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UseCaseDSL_Flow"):
                opp_val = getattr(value, "UseCaseDSL_Flow", None)
                if opp_val is None:
                    setattr(value, "UseCaseDSL_Flow", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UseCaseDSL_Step19(self):
        return self.__UseCaseDSL_Step19

    @UseCaseDSL_Step19.setter
    def UseCaseDSL_Step19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UseCaseDSL_Step__UseCaseDSL_Step19", None)
        self.__UseCaseDSL_Step19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UseCaseDSL_UseCase20"):
                opp_val = getattr(old_value, "UseCaseDSL_UseCase20", None)
                if opp_val == self:
                    setattr(old_value, "UseCaseDSL_UseCase20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UseCaseDSL_UseCase20"):
                opp_val = getattr(value, "UseCaseDSL_UseCase20", None)
                setattr(value, "UseCaseDSL_UseCase20", self)

class UseCaseDSL_Flow(ABC):

    def __init__(self, finalState: str, UseCaseDSL_Flow: set["UseCaseDSL_Step"] = None, UseCaseDSL_Flow29: "UseCaseDSL_UseCase" = None):
        self.finalState = finalState
        self.UseCaseDSL_Flow = UseCaseDSL_Flow if UseCaseDSL_Flow is not None else set()
        self.UseCaseDSL_Flow29 = UseCaseDSL_Flow29
        
        pass
    @property
    def finalState(self):
        return self.__finalState

    @finalState.setter
    def finalState(self, finalState: str):
        self.__finalState = finalState


    @property
    def UseCaseDSL_Flow(self):
        return self.__UseCaseDSL_Flow

    @UseCaseDSL_Flow.setter
    def UseCaseDSL_Flow(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UseCaseDSL_Flow__UseCaseDSL_Flow", None)
        self.__UseCaseDSL_Flow = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UseCaseDSL_Step"):
                    opp_val = getattr(item, "UseCaseDSL_Step", None)
                    
                    if opp_val == self:
                        setattr(item, "UseCaseDSL_Step", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UseCaseDSL_Step"):
                    opp_val = getattr(item, "UseCaseDSL_Step", None)
                    
                    setattr(item, "UseCaseDSL_Step", self)
                    

    @property
    def UseCaseDSL_Flow29(self):
        return self.__UseCaseDSL_Flow29

    @UseCaseDSL_Flow29.setter
    def UseCaseDSL_Flow29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UseCaseDSL_Flow__UseCaseDSL_Flow29", None)
        self.__UseCaseDSL_Flow29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UseCaseDSL_UseCase28"):
                opp_val = getattr(old_value, "UseCaseDSL_UseCase28", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UseCaseDSL_UseCase28"):
                opp_val = getattr(value, "UseCaseDSL_UseCase28", None)
                if opp_val is None:
                    setattr(value, "UseCaseDSL_UseCase28", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class StepAlternative:

    pass
class UseCaseDSL_LocalAlternative(StepAlternative):

    def __init__(self, description: str, UseCaseDSL_LocalAlternative: "UseCaseDSL_UseCase" = None):
        self.description = description
        self.UseCaseDSL_LocalAlternative = UseCaseDSL_LocalAlternative
        
        pass
    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


    @property
    def UseCaseDSL_LocalAlternative(self):
        return self.__UseCaseDSL_LocalAlternative

    @UseCaseDSL_LocalAlternative.setter
    def UseCaseDSL_LocalAlternative(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UseCaseDSL_LocalAlternative__UseCaseDSL_LocalAlternative", None)
        self.__UseCaseDSL_LocalAlternative = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UseCaseDSL_UseCase"):
                opp_val = getattr(old_value, "UseCaseDSL_UseCase", None)
                if opp_val == self:
                    setattr(old_value, "UseCaseDSL_UseCase", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UseCaseDSL_UseCase"):
                opp_val = getattr(value, "UseCaseDSL_UseCase", None)
                setattr(value, "UseCaseDSL_UseCase", self)

class UseCaseDSL_Condition(StepAlternative):

    pass
class UseCaseDSL_AlternativeFlowAlternative(StepAlternative):

    pass
class NamedFlow:

    pass
class UseCaseDSL_ExceptionFlow(NamedFlow):

    def __init__(self, condition: str):
        self.condition = condition
        
        pass
    @property
    def condition(self):
        return self.__condition

    @condition.setter
    def condition(self, condition: str):
        self.__condition = condition


class UseCaseDSL_ParallelFlow(NamedFlow):

    pass
class UseCaseDSL_AlternativeFlow(NamedFlow):

    pass
class UseCaseDSL_Actor:

    def __init__(self, description: str, name: str, type: str, UseCaseDSL_Actor: "UseCaseDSL_Actor" = None, UseCaseDSL_Actor0: "UseCaseDSL_Actor" = None, UseCaseDSL_Actor8: "UseCaseDSL_NormalStep" = None, UseCaseDSL_Actor13: "UseCaseDSL_PackageDeclaration" = None):
        self.description = description
        self.name = name
        self.type = type
        self.UseCaseDSL_Actor = UseCaseDSL_Actor
        self.UseCaseDSL_Actor0 = UseCaseDSL_Actor0
        self.UseCaseDSL_Actor8 = UseCaseDSL_Actor8
        self.UseCaseDSL_Actor13 = UseCaseDSL_Actor13
        
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
    def UseCaseDSL_Actor0(self):
        return self.__UseCaseDSL_Actor0

    @UseCaseDSL_Actor0.setter
    def UseCaseDSL_Actor0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UseCaseDSL_Actor__UseCaseDSL_Actor0", None)
        self.__UseCaseDSL_Actor0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UseCaseDSL_Actor"):
                opp_val = getattr(old_value, "UseCaseDSL_Actor", None)
                if opp_val == self:
                    setattr(old_value, "UseCaseDSL_Actor", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UseCaseDSL_Actor"):
                opp_val = getattr(value, "UseCaseDSL_Actor", None)
                setattr(value, "UseCaseDSL_Actor", self)

    @property
    def UseCaseDSL_Actor8(self):
        return self.__UseCaseDSL_Actor8

    @UseCaseDSL_Actor8.setter
    def UseCaseDSL_Actor8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UseCaseDSL_Actor__UseCaseDSL_Actor8", None)
        self.__UseCaseDSL_Actor8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UseCaseDSL_NormalStep7"):
                opp_val = getattr(old_value, "UseCaseDSL_NormalStep7", None)
                if opp_val == self:
                    setattr(old_value, "UseCaseDSL_NormalStep7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UseCaseDSL_NormalStep7"):
                opp_val = getattr(value, "UseCaseDSL_NormalStep7", None)
                setattr(value, "UseCaseDSL_NormalStep7", self)

    @property
    def UseCaseDSL_Actor13(self):
        return self.__UseCaseDSL_Actor13

    @UseCaseDSL_Actor13.setter
    def UseCaseDSL_Actor13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UseCaseDSL_Actor__UseCaseDSL_Actor13", None)
        self.__UseCaseDSL_Actor13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UseCaseDSL_PackageDeclaration12"):
                opp_val = getattr(old_value, "UseCaseDSL_PackageDeclaration12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UseCaseDSL_PackageDeclaration12"):
                opp_val = getattr(value, "UseCaseDSL_PackageDeclaration12", None)
                if opp_val is None:
                    setattr(value, "UseCaseDSL_PackageDeclaration12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UseCaseDSL_Actor(self):
        return self.__UseCaseDSL_Actor

    @UseCaseDSL_Actor.setter
    def UseCaseDSL_Actor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UseCaseDSL_Actor__UseCaseDSL_Actor", None)
        self.__UseCaseDSL_Actor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UseCaseDSL_Actor0"):
                opp_val = getattr(old_value, "UseCaseDSL_Actor0", None)
                if opp_val == self:
                    setattr(old_value, "UseCaseDSL_Actor0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UseCaseDSL_Actor0"):
                opp_val = getattr(value, "UseCaseDSL_Actor0", None)
                setattr(value, "UseCaseDSL_Actor0", self)

class Flow:

    pass
class UseCaseDSL_NamedFlow(Flow):

    def __init__(self, name: str, UseCaseDSL_NamedFlow: "UseCaseDSL_AlternativeFlowAlternative" = None):
        self.name = name
        self.UseCaseDSL_NamedFlow = UseCaseDSL_NamedFlow
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def UseCaseDSL_NamedFlow(self):
        return self.__UseCaseDSL_NamedFlow

    @UseCaseDSL_NamedFlow.setter
    def UseCaseDSL_NamedFlow(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UseCaseDSL_NamedFlow__UseCaseDSL_NamedFlow", None)
        self.__UseCaseDSL_NamedFlow = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UseCaseDSL_AlternativeFlowAlternative"):
                opp_val = getattr(old_value, "UseCaseDSL_AlternativeFlowAlternative", None)
                if opp_val == self:
                    setattr(old_value, "UseCaseDSL_AlternativeFlowAlternative", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UseCaseDSL_AlternativeFlowAlternative"):
                opp_val = getattr(value, "UseCaseDSL_AlternativeFlowAlternative", None)
                setattr(value, "UseCaseDSL_AlternativeFlowAlternative", self)

class UseCaseDSL_BasicFlow(Flow):

    pass