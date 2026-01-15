from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class LogicOperators(Enum):
    and = "and"
    or = "or"
    not = "not"
class RelationalOperators(Enum):
    equals = "equals"
    lesser = "lesser"
    greater = "greater"
    greater_or_equals = "greater_or_equals"
    lesser_or_equals = "lesser_or_equals"
    not_equals = "not_equals"
class Classifier(Enum):
    Integer = "Integer"
    Double = "Double"
    String = "String"
    Class = "Class"
class MathOperators(Enum):
    plus = "plus"
    minus = "minus"
    multiple = "multiple"
    divide = "divide"


############################################
# Definition of Classes
############################################

class Predicate:

    pass
class Model_Expression(Predicate):

    def __init__(self, operator: str, Model_Expression: "Model_Predicate" = None, Model_Expression71: "Model_Predicate" = None):
        self.operator = operator
        self.Model_Expression = Model_Expression
        self.Model_Expression71 = Model_Expression71
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def Model_Expression(self):
        return self.__Model_Expression

    @Model_Expression.setter
    def Model_Expression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Model_Expression__Model_Expression", None)
        self.__Model_Expression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Model_Predicate69"):
                opp_val = getattr(old_value, "Model_Predicate69", None)
                if opp_val == self:
                    setattr(old_value, "Model_Predicate69", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Model_Predicate69"):
                opp_val = getattr(value, "Model_Predicate69", None)
                setattr(value, "Model_Predicate69", self)

    @property
    def Model_Expression71(self):
        return self.__Model_Expression71

    @Model_Expression71.setter
    def Model_Expression71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Model_Expression__Model_Expression71", None)
        self.__Model_Expression71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Model_Predicate72"):
                opp_val = getattr(old_value, "Model_Predicate72", None)
                if opp_val == self:
                    setattr(old_value, "Model_Predicate72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Model_Predicate72"):
                opp_val = getattr(value, "Model_Predicate72", None)
                setattr(value, "Model_Predicate72", self)

class Model_SimplePredicate(Predicate):

    def __init__(self, operator: str, Model_SimplePredicate: "Model_Variable" = None):
        self.operator = operator
        self.Model_SimplePredicate = Model_SimplePredicate
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def Model_SimplePredicate(self):
        return self.__Model_SimplePredicate

    @Model_SimplePredicate.setter
    def Model_SimplePredicate(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Model_SimplePredicate__Model_SimplePredicate", None)
        self.__Model_SimplePredicate = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Model_Variable67"):
                opp_val = getattr(old_value, "Model_Variable67", None)
                if opp_val == self:
                    setattr(old_value, "Model_Variable67", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Model_Variable67"):
                opp_val = getattr(value, "Model_Variable67", None)
                setattr(value, "Model_Variable67", self)

class Model_PhaseTransition(ABC):

    pass
class Model_Predicate(ABC):

    pass
class Model_Property:

    pass
class Model_Phase:

    def __init__(self, phaseID: str, timeAdvance: float, Model_Phase: "Model_AtomicDEVS" = None, Model_Phase58: "Model_Property" = None, Model_Phase62: "Model_PhaseTransition" = None, Model_Phase65: "Model_PhaseTransition" = None):
        self.phaseID = phaseID
        self.timeAdvance = timeAdvance
        self.Model_Phase = Model_Phase
        self.Model_Phase58 = Model_Phase58
        self.Model_Phase62 = Model_Phase62
        self.Model_Phase65 = Model_Phase65
        
    @property
    def phaseID(self) -> str:
        return self.__phaseID

    @phaseID.setter
    def phaseID(self, phaseID: str):
        self.__phaseID = phaseID

    @property
    def timeAdvance(self) -> float:
        return self.__timeAdvance

    @timeAdvance.setter
    def timeAdvance(self, timeAdvance: float):
        self.__timeAdvance = timeAdvance

    @property
    def Model_Phase(self):
        return self.__Model_Phase

    @Model_Phase.setter
    def Model_Phase(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Model_Phase__Model_Phase", None)
        self.__Model_Phase = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Model_AtomicDEVS12"):
                opp_val = getattr(old_value, "Model_AtomicDEVS12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Model_AtomicDEVS12"):
                opp_val = getattr(value, "Model_AtomicDEVS12", None)
                if opp_val is None:
                    setattr(value, "Model_AtomicDEVS12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Model_Phase58(self):
        return self.__Model_Phase58

    @Model_Phase58.setter
    def Model_Phase58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Model_Phase__Model_Phase58", None)
        self.__Model_Phase58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Model_Property"):
                opp_val = getattr(old_value, "Model_Property", None)
                if opp_val == self:
                    setattr(old_value, "Model_Property", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Model_Property"):
                opp_val = getattr(value, "Model_Property", None)
                setattr(value, "Model_Property", self)

    @property
    def Model_Phase65(self):
        return self.__Model_Phase65

    @Model_Phase65.setter
    def Model_Phase65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Model_Phase__Model_Phase65", None)
        self.__Model_Phase65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Model_PhaseTransition64"):
                opp_val = getattr(old_value, "Model_PhaseTransition64", None)
                if opp_val == self:
                    setattr(old_value, "Model_PhaseTransition64", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Model_PhaseTransition64"):
                opp_val = getattr(value, "Model_PhaseTransition64", None)
                setattr(value, "Model_PhaseTransition64", self)

    @property
    def Model_Phase62(self):
        return self.__Model_Phase62

    @Model_Phase62.setter
    def Model_Phase62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Model_Phase__Model_Phase62", None)
        self.__Model_Phase62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Model_PhaseTransition"):
                opp_val = getattr(old_value, "Model_PhaseTransition", None)
                if opp_val == self:
                    setattr(old_value, "Model_PhaseTransition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Model_PhaseTransition"):
                opp_val = getattr(value, "Model_PhaseTransition", None)
                setattr(value, "Model_PhaseTransition", self)

class Model_Event:

    pass
class PhaseTransition:

    pass
class Model_Port(ABC):

    def __init__(self, portId: str, portType: str, Model_Port: "Model_DEVS" = None, Model_Port56: "Model_Event" = None):
        self.portId = portId
        self.portType = portType
        self.Model_Port = Model_Port
        self.Model_Port56 = Model_Port56
        
    @property
    def portId(self) -> str:
        return self.__portId

    @portId.setter
    def portId(self, portId: str):
        self.__portId = portId

    @property
    def portType(self) -> str:
        return self.__portType

    @portType.setter
    def portType(self, portType: str):
        self.__portType = portType

    @property
    def Model_Port56(self):
        return self.__Model_Port56

    @Model_Port56.setter
    def Model_Port56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Model_Port__Model_Port56", None)
        self.__Model_Port56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Model_Event55"):
                opp_val = getattr(old_value, "Model_Event55", None)
                if opp_val == self:
                    setattr(old_value, "Model_Event55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Model_Event55"):
                opp_val = getattr(value, "Model_Event55", None)
                setattr(value, "Model_Event55", self)

    @property
    def Model_Port(self):
        return self.__Model_Port

    @Model_Port.setter
    def Model_Port(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Model_Port__Model_Port", None)
        self.__Model_Port = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Model_DEVS24"):
                opp_val = getattr(old_value, "Model_DEVS24", None)
                if opp_val == self:
                    setattr(old_value, "Model_DEVS24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Model_DEVS24"):
                opp_val = getattr(value, "Model_DEVS24", None)
                setattr(value, "Model_DEVS24", self)

class Port:

    pass
class Model_EOC:

    pass
class Model_IC:

    pass
class Model_EIC:

    pass
class Model_Variable:

    def __init__(self, name: str, domain: str, Model_Variable: "Model_AtomicDEVS" = None, Model_Variable67: "Model_SimplePredicate" = None):
        self.name = name
        self.domain = domain
        self.Model_Variable = Model_Variable
        self.Model_Variable67 = Model_Variable67
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def domain(self) -> str:
        return self.__domain

    @domain.setter
    def domain(self, domain: str):
        self.__domain = domain

    @property
    def Model_Variable67(self):
        return self.__Model_Variable67

    @Model_Variable67.setter
    def Model_Variable67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Model_Variable__Model_Variable67", None)
        self.__Model_Variable67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Model_SimplePredicate"):
                opp_val = getattr(old_value, "Model_SimplePredicate", None)
                if opp_val == self:
                    setattr(old_value, "Model_SimplePredicate", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Model_SimplePredicate"):
                opp_val = getattr(value, "Model_SimplePredicate", None)
                setattr(value, "Model_SimplePredicate", self)

    @property
    def Model_Variable(self):
        return self.__Model_Variable

    @Model_Variable.setter
    def Model_Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Model_Variable__Model_Variable", None)
        self.__Model_Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Model_AtomicDEVS14"):
                opp_val = getattr(old_value, "Model_AtomicDEVS14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Model_AtomicDEVS14"):
                opp_val = getattr(value, "Model_AtomicDEVS14", None)
                if opp_val is None:
                    setattr(value, "Model_AtomicDEVS14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Model_ExtTrans(PhaseTransition):

    pass
class Model_ConfTrans(PhaseTransition):

    pass
class Model_IntTransition(PhaseTransition):

    pass
class DEVS:

    pass
class Model_CoupledDEVS(DEVS):

    pass
class Model_AtomicDEVS(DEVS):

    pass
class Model_OPort(Port):

    pass
class Model_IPort(Port):

    pass
class Model_DEVS(ABC):

    def __init__(self, name: str, Model_DEVS: "Model_DEVS" = None, Model_DEVS0: "Model_DEVS" = None, Model_DEVS3: set["Model_IPort"] = None, Model_DEVS5: set["Model_OPort"] = None, Model_DEVS16: "Model_CoupledDEVS" = None, Model_DEVS24: "Model_Port" = None):
        self.name = name
        self.Model_DEVS = Model_DEVS
        self.Model_DEVS0 = Model_DEVS0
        self.Model_DEVS3 = Model_DEVS3 if Model_DEVS3 is not None else set()
        self.Model_DEVS5 = Model_DEVS5 if Model_DEVS5 is not None else set()
        self.Model_DEVS16 = Model_DEVS16
        self.Model_DEVS24 = Model_DEVS24
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Model_DEVS3(self):
        return self.__Model_DEVS3

    @Model_DEVS3.setter
    def Model_DEVS3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Model_DEVS__Model_DEVS3", None)
        self.__Model_DEVS3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Model_IPort"):
                    opp_val = getattr(item, "Model_IPort", None)
                    
                    if opp_val == self:
                        setattr(item, "Model_IPort", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Model_IPort"):
                    opp_val = getattr(item, "Model_IPort", None)
                    
                    setattr(item, "Model_IPort", self)
                    

    @property
    def Model_DEVS(self):
        return self.__Model_DEVS

    @Model_DEVS.setter
    def Model_DEVS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Model_DEVS__Model_DEVS", None)
        self.__Model_DEVS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Model_DEVS0"):
                opp_val = getattr(old_value, "Model_DEVS0", None)
                if opp_val == self:
                    setattr(old_value, "Model_DEVS0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Model_DEVS0"):
                opp_val = getattr(value, "Model_DEVS0", None)
                setattr(value, "Model_DEVS0", self)

    @property
    def Model_DEVS0(self):
        return self.__Model_DEVS0

    @Model_DEVS0.setter
    def Model_DEVS0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Model_DEVS__Model_DEVS0", None)
        self.__Model_DEVS0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Model_DEVS"):
                opp_val = getattr(old_value, "Model_DEVS", None)
                if opp_val == self:
                    setattr(old_value, "Model_DEVS", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Model_DEVS"):
                opp_val = getattr(value, "Model_DEVS", None)
                setattr(value, "Model_DEVS", self)

    @property
    def Model_DEVS5(self):
        return self.__Model_DEVS5

    @Model_DEVS5.setter
    def Model_DEVS5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Model_DEVS__Model_DEVS5", None)
        self.__Model_DEVS5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Model_OPort"):
                    opp_val = getattr(item, "Model_OPort", None)
                    
                    if opp_val == self:
                        setattr(item, "Model_OPort", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Model_OPort"):
                    opp_val = getattr(item, "Model_OPort", None)
                    
                    setattr(item, "Model_OPort", self)
                    

    @property
    def Model_DEVS16(self):
        return self.__Model_DEVS16

    @Model_DEVS16.setter
    def Model_DEVS16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Model_DEVS__Model_DEVS16", None)
        self.__Model_DEVS16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Model_CoupledDEVS"):
                opp_val = getattr(old_value, "Model_CoupledDEVS", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Model_CoupledDEVS"):
                opp_val = getattr(value, "Model_CoupledDEVS", None)
                if opp_val is None:
                    setattr(value, "Model_CoupledDEVS", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Model_DEVS24(self):
        return self.__Model_DEVS24

    @Model_DEVS24.setter
    def Model_DEVS24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Model_DEVS__Model_DEVS24", None)
        self.__Model_DEVS24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Model_Port"):
                opp_val = getattr(old_value, "Model_Port", None)
                if opp_val == self:
                    setattr(old_value, "Model_Port", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Model_Port"):
                opp_val = getattr(value, "Model_Port", None)
                setattr(value, "Model_Port", self)
