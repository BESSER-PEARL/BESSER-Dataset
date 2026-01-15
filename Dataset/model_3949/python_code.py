from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class FuzzyRelationType(Enum):
    EQ = "EQ"
    GTE = "GTE"
    LTE = "LTE"
    TERN = "TERN"
class TNormType(Enum):
    HAMACHER = "HAMACHER"
    GODEL = "GODEL"


############################################
# Definition of Classes
############################################

class fuzzyAutomaton_VarUpdate:

    def __init__(self, expression: str, fuzzyAutomaton_VarUpdate: "fuzzyAutomaton_VarTransformation" = None, fuzzyAutomaton_VarUpdate31: "fuzzyAutomaton_Variable" = None):
        self.expression = expression
        self.fuzzyAutomaton_VarUpdate = fuzzyAutomaton_VarUpdate
        self.fuzzyAutomaton_VarUpdate31 = fuzzyAutomaton_VarUpdate31
        
    @property
    def expression(self) -> str:
        return self.__expression

    @expression.setter
    def expression(self, expression: str):
        self.__expression = expression

    @property
    def fuzzyAutomaton_VarUpdate(self):
        return self.__fuzzyAutomaton_VarUpdate

    @fuzzyAutomaton_VarUpdate.setter
    def fuzzyAutomaton_VarUpdate(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuzzyAutomaton_VarUpdate__fuzzyAutomaton_VarUpdate", None)
        self.__fuzzyAutomaton_VarUpdate = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fuzzyAutomaton_VarTransformation29"):
                opp_val = getattr(old_value, "fuzzyAutomaton_VarTransformation29", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fuzzyAutomaton_VarTransformation29"):
                opp_val = getattr(value, "fuzzyAutomaton_VarTransformation29", None)
                if opp_val is None:
                    setattr(value, "fuzzyAutomaton_VarTransformation29", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fuzzyAutomaton_VarUpdate31(self):
        return self.__fuzzyAutomaton_VarUpdate31

    @fuzzyAutomaton_VarUpdate31.setter
    def fuzzyAutomaton_VarUpdate31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuzzyAutomaton_VarUpdate__fuzzyAutomaton_VarUpdate31", None)
        self.__fuzzyAutomaton_VarUpdate31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fuzzyAutomaton_Variable32"):
                opp_val = getattr(old_value, "fuzzyAutomaton_Variable32", None)
                if opp_val == self:
                    setattr(old_value, "fuzzyAutomaton_Variable32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fuzzyAutomaton_Variable32"):
                opp_val = getattr(value, "fuzzyAutomaton_Variable32", None)
                setattr(value, "fuzzyAutomaton_Variable32", self)

class fuzzyAutomaton_FuzzyRelation:

    def __init__(self, tFRelation: str, expression1: str, expression2: str, expression3: str, delta: str, fuzzyAutomaton_FuzzyRelation: "fuzzyAutomaton_FuzzyConstraint" = None):
        self.tFRelation = tFRelation
        self.expression1 = expression1
        self.expression2 = expression2
        self.expression3 = expression3
        self.delta = delta
        self.fuzzyAutomaton_FuzzyRelation = fuzzyAutomaton_FuzzyRelation
        
    @property
    def expression3(self) -> str:
        return self.__expression3

    @expression3.setter
    def expression3(self, expression3: str):
        self.__expression3 = expression3

    @property
    def tFRelation(self) -> str:
        return self.__tFRelation

    @tFRelation.setter
    def tFRelation(self, tFRelation: str):
        self.__tFRelation = tFRelation

    @property
    def expression1(self) -> str:
        return self.__expression1

    @expression1.setter
    def expression1(self, expression1: str):
        self.__expression1 = expression1

    @property
    def delta(self) -> str:
        return self.__delta

    @delta.setter
    def delta(self, delta: str):
        self.__delta = delta

    @property
    def expression2(self) -> str:
        return self.__expression2

    @expression2.setter
    def expression2(self, expression2: str):
        self.__expression2 = expression2

    @property
    def fuzzyAutomaton_FuzzyRelation(self):
        return self.__fuzzyAutomaton_FuzzyRelation

    @fuzzyAutomaton_FuzzyRelation.setter
    def fuzzyAutomaton_FuzzyRelation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuzzyAutomaton_FuzzyRelation__fuzzyAutomaton_FuzzyRelation", None)
        self.__fuzzyAutomaton_FuzzyRelation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fuzzyAutomaton_FuzzyConstraint27"):
                opp_val = getattr(old_value, "fuzzyAutomaton_FuzzyConstraint27", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fuzzyAutomaton_FuzzyConstraint27"):
                opp_val = getattr(value, "fuzzyAutomaton_FuzzyConstraint27", None)
                if opp_val is None:
                    setattr(value, "fuzzyAutomaton_FuzzyConstraint27", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class fuzzyAutomaton_Action(ABC):

    def __init__(self, name: str, fuzzyAutomaton_Action: "fuzzyAutomaton_TransitionFeature" = None):
        self.name = name
        self.fuzzyAutomaton_Action = fuzzyAutomaton_Action
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fuzzyAutomaton_Action(self):
        return self.__fuzzyAutomaton_Action

    @fuzzyAutomaton_Action.setter
    def fuzzyAutomaton_Action(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuzzyAutomaton_Action__fuzzyAutomaton_Action", None)
        self.__fuzzyAutomaton_Action = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fuzzyAutomaton_TransitionFeature19"):
                opp_val = getattr(old_value, "fuzzyAutomaton_TransitionFeature19", None)
                if opp_val == self:
                    setattr(old_value, "fuzzyAutomaton_TransitionFeature19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fuzzyAutomaton_TransitionFeature19"):
                opp_val = getattr(value, "fuzzyAutomaton_TransitionFeature19", None)
                setattr(value, "fuzzyAutomaton_TransitionFeature19", self)

class Action:

    pass
class fuzzyAutomaton_Output(Action):

    def __init__(self, expression: str):
        self.expression = expression
        
    @property
    def expression(self) -> str:
        return self.__expression

    @expression.setter
    def expression(self, expression: str):
        self.__expression = expression

class fuzzyAutomaton_Input(Action):

    pass
class fuzzyAutomaton_VarTransformation:

    def __init__(self, name: str, fuzzyAutomaton_VarTransformation: "fuzzyAutomaton_TransitionFeature" = None, fuzzyAutomaton_VarTransformation29: set["fuzzyAutomaton_VarUpdate"] = None):
        self.name = name
        self.fuzzyAutomaton_VarTransformation = fuzzyAutomaton_VarTransformation
        self.fuzzyAutomaton_VarTransformation29 = fuzzyAutomaton_VarTransformation29 if fuzzyAutomaton_VarTransformation29 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fuzzyAutomaton_VarTransformation(self):
        return self.__fuzzyAutomaton_VarTransformation

    @fuzzyAutomaton_VarTransformation.setter
    def fuzzyAutomaton_VarTransformation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuzzyAutomaton_VarTransformation__fuzzyAutomaton_VarTransformation", None)
        self.__fuzzyAutomaton_VarTransformation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fuzzyAutomaton_TransitionFeature23"):
                opp_val = getattr(old_value, "fuzzyAutomaton_TransitionFeature23", None)
                if opp_val == self:
                    setattr(old_value, "fuzzyAutomaton_TransitionFeature23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fuzzyAutomaton_TransitionFeature23"):
                opp_val = getattr(value, "fuzzyAutomaton_TransitionFeature23", None)
                setattr(value, "fuzzyAutomaton_TransitionFeature23", self)

    @property
    def fuzzyAutomaton_VarTransformation29(self):
        return self.__fuzzyAutomaton_VarTransformation29

    @fuzzyAutomaton_VarTransformation29.setter
    def fuzzyAutomaton_VarTransformation29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuzzyAutomaton_VarTransformation__fuzzyAutomaton_VarTransformation29", None)
        self.__fuzzyAutomaton_VarTransformation29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fuzzyAutomaton_VarUpdate"):
                    opp_val = getattr(item, "fuzzyAutomaton_VarUpdate", None)
                    
                    if opp_val == self:
                        setattr(item, "fuzzyAutomaton_VarUpdate", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fuzzyAutomaton_VarUpdate"):
                    opp_val = getattr(item, "fuzzyAutomaton_VarUpdate", None)
                    
                    setattr(item, "fuzzyAutomaton_VarUpdate", self)
                    

class fuzzyAutomaton_FuzzyConstraint:

    def __init__(self, name: str, tNorm: str, fuzzyAutomaton_FuzzyConstraint: "fuzzyAutomaton_TransitionFeature" = None, fuzzyAutomaton_FuzzyConstraint27: set["fuzzyAutomaton_FuzzyRelation"] = None):
        self.name = name
        self.tNorm = tNorm
        self.fuzzyAutomaton_FuzzyConstraint = fuzzyAutomaton_FuzzyConstraint
        self.fuzzyAutomaton_FuzzyConstraint27 = fuzzyAutomaton_FuzzyConstraint27 if fuzzyAutomaton_FuzzyConstraint27 is not None else set()
        
    @property
    def tNorm(self) -> str:
        return self.__tNorm

    @tNorm.setter
    def tNorm(self, tNorm: str):
        self.__tNorm = tNorm

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fuzzyAutomaton_FuzzyConstraint(self):
        return self.__fuzzyAutomaton_FuzzyConstraint

    @fuzzyAutomaton_FuzzyConstraint.setter
    def fuzzyAutomaton_FuzzyConstraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuzzyAutomaton_FuzzyConstraint__fuzzyAutomaton_FuzzyConstraint", None)
        self.__fuzzyAutomaton_FuzzyConstraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fuzzyAutomaton_TransitionFeature21"):
                opp_val = getattr(old_value, "fuzzyAutomaton_TransitionFeature21", None)
                if opp_val == self:
                    setattr(old_value, "fuzzyAutomaton_TransitionFeature21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fuzzyAutomaton_TransitionFeature21"):
                opp_val = getattr(value, "fuzzyAutomaton_TransitionFeature21", None)
                setattr(value, "fuzzyAutomaton_TransitionFeature21", self)

    @property
    def fuzzyAutomaton_FuzzyConstraint27(self):
        return self.__fuzzyAutomaton_FuzzyConstraint27

    @fuzzyAutomaton_FuzzyConstraint27.setter
    def fuzzyAutomaton_FuzzyConstraint27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuzzyAutomaton_FuzzyConstraint__fuzzyAutomaton_FuzzyConstraint27", None)
        self.__fuzzyAutomaton_FuzzyConstraint27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fuzzyAutomaton_FuzzyRelation"):
                    opp_val = getattr(item, "fuzzyAutomaton_FuzzyRelation", None)
                    
                    if opp_val == self:
                        setattr(item, "fuzzyAutomaton_FuzzyRelation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fuzzyAutomaton_FuzzyRelation"):
                    opp_val = getattr(item, "fuzzyAutomaton_FuzzyRelation", None)
                    
                    setattr(item, "fuzzyAutomaton_FuzzyRelation", self)
                    

class fuzzyAutomaton_Variable:

    def __init__(self, name: str, value: str, fuzzyAutomaton_Variable: "fuzzyAutomaton_VariableSet" = None, fuzzyAutomaton_Variable25: "fuzzyAutomaton_Input" = None, fuzzyAutomaton_Variable32: "fuzzyAutomaton_VarUpdate" = None):
        self.name = name
        self.value = value
        self.fuzzyAutomaton_Variable = fuzzyAutomaton_Variable
        self.fuzzyAutomaton_Variable25 = fuzzyAutomaton_Variable25
        self.fuzzyAutomaton_Variable32 = fuzzyAutomaton_Variable32
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fuzzyAutomaton_Variable(self):
        return self.__fuzzyAutomaton_Variable

    @fuzzyAutomaton_Variable.setter
    def fuzzyAutomaton_Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuzzyAutomaton_Variable__fuzzyAutomaton_Variable", None)
        self.__fuzzyAutomaton_Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fuzzyAutomaton_VariableSet15"):
                opp_val = getattr(old_value, "fuzzyAutomaton_VariableSet15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fuzzyAutomaton_VariableSet15"):
                opp_val = getattr(value, "fuzzyAutomaton_VariableSet15", None)
                if opp_val is None:
                    setattr(value, "fuzzyAutomaton_VariableSet15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fuzzyAutomaton_Variable25(self):
        return self.__fuzzyAutomaton_Variable25

    @fuzzyAutomaton_Variable25.setter
    def fuzzyAutomaton_Variable25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuzzyAutomaton_Variable__fuzzyAutomaton_Variable25", None)
        self.__fuzzyAutomaton_Variable25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fuzzyAutomaton_Input"):
                opp_val = getattr(old_value, "fuzzyAutomaton_Input", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fuzzyAutomaton_Input"):
                opp_val = getattr(value, "fuzzyAutomaton_Input", None)
                if opp_val is None:
                    setattr(value, "fuzzyAutomaton_Input", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fuzzyAutomaton_Variable32(self):
        return self.__fuzzyAutomaton_Variable32

    @fuzzyAutomaton_Variable32.setter
    def fuzzyAutomaton_Variable32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuzzyAutomaton_Variable__fuzzyAutomaton_Variable32", None)
        self.__fuzzyAutomaton_Variable32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fuzzyAutomaton_VarUpdate31"):
                opp_val = getattr(old_value, "fuzzyAutomaton_VarUpdate31", None)
                if opp_val == self:
                    setattr(old_value, "fuzzyAutomaton_VarUpdate31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fuzzyAutomaton_VarUpdate31"):
                opp_val = getattr(value, "fuzzyAutomaton_VarUpdate31", None)
                setattr(value, "fuzzyAutomaton_VarUpdate31", self)

class fuzzyAutomaton_TransitionFeature:

    def __init__(self, name: str, fuzzyAutomaton_TransitionFeature: "fuzzyAutomaton_FuzzyAutomaton" = None, TransitionFeature: "fuzzyAutomaton_Transition" = None, fuzzyAutomaton_TransitionFeature21: "fuzzyAutomaton_FuzzyConstraint" = None, fuzzyAutomaton_TransitionFeature23: "fuzzyAutomaton_VarTransformation" = None, feature: set["fuzzyAutomaton_Transition"] = None, fuzzyAutomaton_TransitionFeature19: "fuzzyAutomaton_Action" = None):
        self.name = name
        self.fuzzyAutomaton_TransitionFeature = fuzzyAutomaton_TransitionFeature
        self.TransitionFeature = TransitionFeature
        self.fuzzyAutomaton_TransitionFeature21 = fuzzyAutomaton_TransitionFeature21
        self.fuzzyAutomaton_TransitionFeature23 = fuzzyAutomaton_TransitionFeature23
        self.feature = feature if feature is not None else set()
        self.fuzzyAutomaton_TransitionFeature19 = fuzzyAutomaton_TransitionFeature19
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fuzzyAutomaton_TransitionFeature19(self):
        return self.__fuzzyAutomaton_TransitionFeature19

    @fuzzyAutomaton_TransitionFeature19.setter
    def fuzzyAutomaton_TransitionFeature19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuzzyAutomaton_TransitionFeature__fuzzyAutomaton_TransitionFeature19", None)
        self.__fuzzyAutomaton_TransitionFeature19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fuzzyAutomaton_Action"):
                opp_val = getattr(old_value, "fuzzyAutomaton_Action", None)
                if opp_val == self:
                    setattr(old_value, "fuzzyAutomaton_Action", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fuzzyAutomaton_Action"):
                opp_val = getattr(value, "fuzzyAutomaton_Action", None)
                setattr(value, "fuzzyAutomaton_Action", self)

    @property
    def TransitionFeature(self):
        return self.__TransitionFeature

    @TransitionFeature.setter
    def TransitionFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuzzyAutomaton_TransitionFeature__TransitionFeature", None)
        self.__TransitionFeature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "featureToTransition"):
                opp_val = getattr(old_value, "featureToTransition", None)
                if opp_val == self:
                    setattr(old_value, "featureToTransition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "featureToTransition"):
                opp_val = getattr(value, "featureToTransition", None)
                setattr(value, "featureToTransition", self)

    @property
    def feature(self):
        return self.__feature

    @feature.setter
    def feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuzzyAutomaton_TransitionFeature__feature", None)
        self.__feature = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Transition17"):
                    opp_val = getattr(item, "Transition17", None)
                    
                    if opp_val == self:
                        setattr(item, "Transition17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transition17"):
                    opp_val = getattr(item, "Transition17", None)
                    
                    setattr(item, "Transition17", self)
                    

    @property
    def fuzzyAutomaton_TransitionFeature21(self):
        return self.__fuzzyAutomaton_TransitionFeature21

    @fuzzyAutomaton_TransitionFeature21.setter
    def fuzzyAutomaton_TransitionFeature21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuzzyAutomaton_TransitionFeature__fuzzyAutomaton_TransitionFeature21", None)
        self.__fuzzyAutomaton_TransitionFeature21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fuzzyAutomaton_FuzzyConstraint"):
                opp_val = getattr(old_value, "fuzzyAutomaton_FuzzyConstraint", None)
                if opp_val == self:
                    setattr(old_value, "fuzzyAutomaton_FuzzyConstraint", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fuzzyAutomaton_FuzzyConstraint"):
                opp_val = getattr(value, "fuzzyAutomaton_FuzzyConstraint", None)
                setattr(value, "fuzzyAutomaton_FuzzyConstraint", self)

    @property
    def fuzzyAutomaton_TransitionFeature(self):
        return self.__fuzzyAutomaton_TransitionFeature

    @fuzzyAutomaton_TransitionFeature.setter
    def fuzzyAutomaton_TransitionFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuzzyAutomaton_TransitionFeature__fuzzyAutomaton_TransitionFeature", None)
        self.__fuzzyAutomaton_TransitionFeature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fuzzyAutomaton_FuzzyAutomaton6"):
                opp_val = getattr(old_value, "fuzzyAutomaton_FuzzyAutomaton6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fuzzyAutomaton_FuzzyAutomaton6"):
                opp_val = getattr(value, "fuzzyAutomaton_FuzzyAutomaton6", None)
                if opp_val is None:
                    setattr(value, "fuzzyAutomaton_FuzzyAutomaton6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fuzzyAutomaton_TransitionFeature23(self):
        return self.__fuzzyAutomaton_TransitionFeature23

    @fuzzyAutomaton_TransitionFeature23.setter
    def fuzzyAutomaton_TransitionFeature23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuzzyAutomaton_TransitionFeature__fuzzyAutomaton_TransitionFeature23", None)
        self.__fuzzyAutomaton_TransitionFeature23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fuzzyAutomaton_VarTransformation"):
                opp_val = getattr(old_value, "fuzzyAutomaton_VarTransformation", None)
                if opp_val == self:
                    setattr(old_value, "fuzzyAutomaton_VarTransformation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fuzzyAutomaton_VarTransformation"):
                opp_val = getattr(value, "fuzzyAutomaton_VarTransformation", None)
                setattr(value, "fuzzyAutomaton_VarTransformation", self)

class fuzzyAutomaton_VariableSet:

    def __init__(self, name: str, fuzzyAutomaton_VariableSet: "fuzzyAutomaton_FuzzyAutomaton" = None, fuzzyAutomaton_VariableSet15: set["fuzzyAutomaton_Variable"] = None):
        self.name = name
        self.fuzzyAutomaton_VariableSet = fuzzyAutomaton_VariableSet
        self.fuzzyAutomaton_VariableSet15 = fuzzyAutomaton_VariableSet15 if fuzzyAutomaton_VariableSet15 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fuzzyAutomaton_VariableSet(self):
        return self.__fuzzyAutomaton_VariableSet

    @fuzzyAutomaton_VariableSet.setter
    def fuzzyAutomaton_VariableSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuzzyAutomaton_VariableSet__fuzzyAutomaton_VariableSet", None)
        self.__fuzzyAutomaton_VariableSet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fuzzyAutomaton_FuzzyAutomaton4"):
                opp_val = getattr(old_value, "fuzzyAutomaton_FuzzyAutomaton4", None)
                if opp_val == self:
                    setattr(old_value, "fuzzyAutomaton_FuzzyAutomaton4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fuzzyAutomaton_FuzzyAutomaton4"):
                opp_val = getattr(value, "fuzzyAutomaton_FuzzyAutomaton4", None)
                setattr(value, "fuzzyAutomaton_FuzzyAutomaton4", self)

    @property
    def fuzzyAutomaton_VariableSet15(self):
        return self.__fuzzyAutomaton_VariableSet15

    @fuzzyAutomaton_VariableSet15.setter
    def fuzzyAutomaton_VariableSet15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuzzyAutomaton_VariableSet__fuzzyAutomaton_VariableSet15", None)
        self.__fuzzyAutomaton_VariableSet15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fuzzyAutomaton_Variable"):
                    opp_val = getattr(item, "fuzzyAutomaton_Variable", None)
                    
                    if opp_val == self:
                        setattr(item, "fuzzyAutomaton_Variable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fuzzyAutomaton_Variable"):
                    opp_val = getattr(item, "fuzzyAutomaton_Variable", None)
                    
                    setattr(item, "fuzzyAutomaton_Variable", self)
                    

class fuzzyAutomaton_Transition:

    pass
class fuzzyAutomaton_State:

    def __init__(self, isInitial: str, fuzzyAutomaton_State: "fuzzyAutomaton_FuzzyAutomaton" = None, State: "fuzzyAutomaton_Transition" = None, State12: "fuzzyAutomaton_Transition" = None, target: set["fuzzyAutomaton_Transition"] = None, source: set["fuzzyAutomaton_Transition"] = None):
        self.isInitial = isInitial
        self.fuzzyAutomaton_State = fuzzyAutomaton_State
        self.State = State
        self.State12 = State12
        self.target = target if target is not None else set()
        self.source = source if source is not None else set()
        
    @property
    def isInitial(self) -> str:
        return self.__isInitial

    @isInitial.setter
    def isInitial(self, isInitial: str):
        self.__isInitial = isInitial

    @property
    def State(self):
        return self.__State

    @State.setter
    def State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuzzyAutomaton_State__State", None)
        self.__State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outgoing"):
                opp_val = getattr(old_value, "outgoing", None)
                if opp_val == self:
                    setattr(old_value, "outgoing", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outgoing"):
                opp_val = getattr(value, "outgoing", None)
                setattr(value, "outgoing", self)

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuzzyAutomaton_State__source", None)
        self.__source = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Transition9"):
                    opp_val = getattr(item, "Transition9", None)
                    
                    if opp_val == self:
                        setattr(item, "Transition9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transition9"):
                    opp_val = getattr(item, "Transition9", None)
                    
                    setattr(item, "Transition9", self)
                    

    @property
    def State12(self):
        return self.__State12

    @State12.setter
    def State12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuzzyAutomaton_State__State12", None)
        self.__State12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "incoming"):
                opp_val = getattr(old_value, "incoming", None)
                if opp_val == self:
                    setattr(old_value, "incoming", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "incoming"):
                opp_val = getattr(value, "incoming", None)
                setattr(value, "incoming", self)

    @property
    def target(self):
        return self.__target

    @target.setter
    def target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuzzyAutomaton_State__target", None)
        self.__target = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Transition"):
                    opp_val = getattr(item, "Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transition"):
                    opp_val = getattr(item, "Transition", None)
                    
                    setattr(item, "Transition", self)
                    

    @property
    def fuzzyAutomaton_State(self):
        return self.__fuzzyAutomaton_State

    @fuzzyAutomaton_State.setter
    def fuzzyAutomaton_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuzzyAutomaton_State__fuzzyAutomaton_State", None)
        self.__fuzzyAutomaton_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fuzzyAutomaton_FuzzyAutomaton"):
                opp_val = getattr(old_value, "fuzzyAutomaton_FuzzyAutomaton", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fuzzyAutomaton_FuzzyAutomaton"):
                opp_val = getattr(value, "fuzzyAutomaton_FuzzyAutomaton", None)
                if opp_val is None:
                    setattr(value, "fuzzyAutomaton_FuzzyAutomaton", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class fuzzyAutomaton_FuzzyAutomaton:

    def __init__(self, name: str, tNorm: str, fuzzyAutomaton_FuzzyAutomaton: set["fuzzyAutomaton_State"] = None, fuzzyAutomaton_FuzzyAutomaton2: set["fuzzyAutomaton_Transition"] = None, fuzzyAutomaton_FuzzyAutomaton4: "fuzzyAutomaton_VariableSet" = None, fuzzyAutomaton_FuzzyAutomaton6: set["fuzzyAutomaton_TransitionFeature"] = None):
        self.name = name
        self.tNorm = tNorm
        self.fuzzyAutomaton_FuzzyAutomaton = fuzzyAutomaton_FuzzyAutomaton if fuzzyAutomaton_FuzzyAutomaton is not None else set()
        self.fuzzyAutomaton_FuzzyAutomaton2 = fuzzyAutomaton_FuzzyAutomaton2 if fuzzyAutomaton_FuzzyAutomaton2 is not None else set()
        self.fuzzyAutomaton_FuzzyAutomaton4 = fuzzyAutomaton_FuzzyAutomaton4
        self.fuzzyAutomaton_FuzzyAutomaton6 = fuzzyAutomaton_FuzzyAutomaton6 if fuzzyAutomaton_FuzzyAutomaton6 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def tNorm(self) -> str:
        return self.__tNorm

    @tNorm.setter
    def tNorm(self, tNorm: str):
        self.__tNorm = tNorm

    @property
    def fuzzyAutomaton_FuzzyAutomaton(self):
        return self.__fuzzyAutomaton_FuzzyAutomaton

    @fuzzyAutomaton_FuzzyAutomaton.setter
    def fuzzyAutomaton_FuzzyAutomaton(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuzzyAutomaton_FuzzyAutomaton__fuzzyAutomaton_FuzzyAutomaton", None)
        self.__fuzzyAutomaton_FuzzyAutomaton = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fuzzyAutomaton_State"):
                    opp_val = getattr(item, "fuzzyAutomaton_State", None)
                    
                    if opp_val == self:
                        setattr(item, "fuzzyAutomaton_State", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fuzzyAutomaton_State"):
                    opp_val = getattr(item, "fuzzyAutomaton_State", None)
                    
                    setattr(item, "fuzzyAutomaton_State", self)
                    

    @property
    def fuzzyAutomaton_FuzzyAutomaton2(self):
        return self.__fuzzyAutomaton_FuzzyAutomaton2

    @fuzzyAutomaton_FuzzyAutomaton2.setter
    def fuzzyAutomaton_FuzzyAutomaton2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuzzyAutomaton_FuzzyAutomaton__fuzzyAutomaton_FuzzyAutomaton2", None)
        self.__fuzzyAutomaton_FuzzyAutomaton2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fuzzyAutomaton_Transition"):
                    opp_val = getattr(item, "fuzzyAutomaton_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "fuzzyAutomaton_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fuzzyAutomaton_Transition"):
                    opp_val = getattr(item, "fuzzyAutomaton_Transition", None)
                    
                    setattr(item, "fuzzyAutomaton_Transition", self)
                    

    @property
    def fuzzyAutomaton_FuzzyAutomaton6(self):
        return self.__fuzzyAutomaton_FuzzyAutomaton6

    @fuzzyAutomaton_FuzzyAutomaton6.setter
    def fuzzyAutomaton_FuzzyAutomaton6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuzzyAutomaton_FuzzyAutomaton__fuzzyAutomaton_FuzzyAutomaton6", None)
        self.__fuzzyAutomaton_FuzzyAutomaton6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fuzzyAutomaton_TransitionFeature"):
                    opp_val = getattr(item, "fuzzyAutomaton_TransitionFeature", None)
                    
                    if opp_val == self:
                        setattr(item, "fuzzyAutomaton_TransitionFeature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fuzzyAutomaton_TransitionFeature"):
                    opp_val = getattr(item, "fuzzyAutomaton_TransitionFeature", None)
                    
                    setattr(item, "fuzzyAutomaton_TransitionFeature", self)
                    

    @property
    def fuzzyAutomaton_FuzzyAutomaton4(self):
        return self.__fuzzyAutomaton_FuzzyAutomaton4

    @fuzzyAutomaton_FuzzyAutomaton4.setter
    def fuzzyAutomaton_FuzzyAutomaton4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuzzyAutomaton_FuzzyAutomaton__fuzzyAutomaton_FuzzyAutomaton4", None)
        self.__fuzzyAutomaton_FuzzyAutomaton4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fuzzyAutomaton_VariableSet"):
                opp_val = getattr(old_value, "fuzzyAutomaton_VariableSet", None)
                if opp_val == self:
                    setattr(old_value, "fuzzyAutomaton_VariableSet", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fuzzyAutomaton_VariableSet"):
                opp_val = getattr(value, "fuzzyAutomaton_VariableSet", None)
                setattr(value, "fuzzyAutomaton_VariableSet", self)
