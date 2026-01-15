from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class ScenarioKind(Enum):
    UNSET = "UNSET"
    INTERFACE = "INTERFACE"
    DATA_FLOW = "DATA_FLOW"
    INTERACTION = "INTERACTION"
    FUNCTIONAL = "FUNCTIONAL"
class InteractionOperatorKind(Enum):
    ALT = "ALT"
    OPT = "OPT"
    PAR = "PAR"
    LOOP = "LOOP"
    CRITICAL = "CRITICAL"
    NEG = "NEG"
    ASSERT = "ASSERT"
    STRICT = "STRICT"
    SEQ = "SEQ"
    IGNORE = "IGNORE"
    CONSIDER = "CONSIDER"
    UNSET = "UNSET"
class MessageKind(Enum):
    UNSET = "UNSET"
    ASYNCHRONOUS_CALL = "ASYNCHRONOUS_CALL"
    SYNCHRONOUS_CALL = "SYNCHRONOUS_CALL"
    REPLY = "REPLY"
    DELETE = "DELETE"
    CREATE = "CREATE"
    TIMER = "TIMER"


############################################
# Definition of Classes
############################################

class interaction_ValueSpecification:

    pass
class interaction_ExchangeItemElement:

    pass
class AbstractBehavior:

    pass
class Namespace:

    pass
class interaction_Scenario(Namespace, AbstractBehavior):

    def __init__(self, kind: str, merged: bool, interaction_Scenario36: "interaction_Scenario" = None, interaction_Scenario34: set["interaction_Scenario"] = None, interaction_Scenario44: "interaction_AbstractCapability" = None, interaction_Scenario: "interaction_Constraint" = None, interaction_Scenario20: "interaction_Constraint" = None, interaction_Scenario23: set["interaction_SequenceMessage"] = None, interaction_Scenario26: set["interaction_AbstractFunction"] = None, interaction_Scenario29: set["interaction_Part"] = None, interaction_Scenario33: "interaction_Scenario" = None, interaction_Scenario31: set["interaction_Scenario"] = None):
        self.kind = kind
        self.merged = merged
        self.interaction_Scenario36 = interaction_Scenario36
        self.interaction_Scenario34 = interaction_Scenario34 if interaction_Scenario34 is not None else set()
        self.interaction_Scenario44 = interaction_Scenario44
        self.interaction_Scenario = interaction_Scenario
        self.interaction_Scenario20 = interaction_Scenario20
        self.interaction_Scenario23 = interaction_Scenario23 if interaction_Scenario23 is not None else set()
        self.interaction_Scenario26 = interaction_Scenario26 if interaction_Scenario26 is not None else set()
        self.interaction_Scenario29 = interaction_Scenario29 if interaction_Scenario29 is not None else set()
        self.interaction_Scenario33 = interaction_Scenario33
        self.interaction_Scenario31 = interaction_Scenario31 if interaction_Scenario31 is not None else set()
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def merged(self) -> bool:
        return self.__merged

    @merged.setter
    def merged(self, merged: bool):
        self.__merged = merged

    @property
    def interaction_Scenario29(self):
        return self.__interaction_Scenario29

    @interaction_Scenario29.setter
    def interaction_Scenario29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_interaction_Scenario__interaction_Scenario29", None)
        self.__interaction_Scenario29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "interaction_Part30"):
                    opp_val = getattr(item, "interaction_Part30", None)
                    
                    if opp_val == self:
                        setattr(item, "interaction_Part30", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "interaction_Part30"):
                    opp_val = getattr(item, "interaction_Part30", None)
                    
                    setattr(item, "interaction_Part30", self)
                    

    @property
    def interaction_Scenario34(self):
        return self.__interaction_Scenario34

    @interaction_Scenario34.setter
    def interaction_Scenario34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_interaction_Scenario__interaction_Scenario34", None)
        self.__interaction_Scenario34 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "interaction_Scenario36"):
                    opp_val = getattr(item, "interaction_Scenario36", None)
                    
                    if opp_val == self:
                        setattr(item, "interaction_Scenario36", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "interaction_Scenario36"):
                    opp_val = getattr(item, "interaction_Scenario36", None)
                    
                    setattr(item, "interaction_Scenario36", self)
                    

    @property
    def interaction_Scenario20(self):
        return self.__interaction_Scenario20

    @interaction_Scenario20.setter
    def interaction_Scenario20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_interaction_Scenario__interaction_Scenario20", None)
        self.__interaction_Scenario20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "interaction_Constraint21"):
                opp_val = getattr(old_value, "interaction_Constraint21", None)
                if opp_val == self:
                    setattr(old_value, "interaction_Constraint21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "interaction_Constraint21"):
                opp_val = getattr(value, "interaction_Constraint21", None)
                setattr(value, "interaction_Constraint21", self)

    @property
    def interaction_Scenario44(self):
        return self.__interaction_Scenario44

    @interaction_Scenario44.setter
    def interaction_Scenario44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_interaction_Scenario__interaction_Scenario44", None)
        self.__interaction_Scenario44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "interaction_AbstractCapability43"):
                opp_val = getattr(old_value, "interaction_AbstractCapability43", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "interaction_AbstractCapability43"):
                opp_val = getattr(value, "interaction_AbstractCapability43", None)
                if opp_val is None:
                    setattr(value, "interaction_AbstractCapability43", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def interaction_Scenario36(self):
        return self.__interaction_Scenario36

    @interaction_Scenario36.setter
    def interaction_Scenario36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_interaction_Scenario__interaction_Scenario36", None)
        self.__interaction_Scenario36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "interaction_Scenario34"):
                opp_val = getattr(old_value, "interaction_Scenario34", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "interaction_Scenario34"):
                opp_val = getattr(value, "interaction_Scenario34", None)
                if opp_val is None:
                    setattr(value, "interaction_Scenario34", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def interaction_Scenario33(self):
        return self.__interaction_Scenario33

    @interaction_Scenario33.setter
    def interaction_Scenario33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_interaction_Scenario__interaction_Scenario33", None)
        self.__interaction_Scenario33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "interaction_Scenario31"):
                opp_val = getattr(old_value, "interaction_Scenario31", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "interaction_Scenario31"):
                opp_val = getattr(value, "interaction_Scenario31", None)
                if opp_val is None:
                    setattr(value, "interaction_Scenario31", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def interaction_Scenario23(self):
        return self.__interaction_Scenario23

    @interaction_Scenario23.setter
    def interaction_Scenario23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_interaction_Scenario__interaction_Scenario23", None)
        self.__interaction_Scenario23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "interaction_SequenceMessage24"):
                    opp_val = getattr(item, "interaction_SequenceMessage24", None)
                    
                    if opp_val == self:
                        setattr(item, "interaction_SequenceMessage24", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "interaction_SequenceMessage24"):
                    opp_val = getattr(item, "interaction_SequenceMessage24", None)
                    
                    setattr(item, "interaction_SequenceMessage24", self)
                    

    @property
    def interaction_Scenario31(self):
        return self.__interaction_Scenario31

    @interaction_Scenario31.setter
    def interaction_Scenario31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_interaction_Scenario__interaction_Scenario31", None)
        self.__interaction_Scenario31 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "interaction_Scenario33"):
                    opp_val = getattr(item, "interaction_Scenario33", None)
                    
                    if opp_val == self:
                        setattr(item, "interaction_Scenario33", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "interaction_Scenario33"):
                    opp_val = getattr(item, "interaction_Scenario33", None)
                    
                    setattr(item, "interaction_Scenario33", self)
                    

    @property
    def interaction_Scenario(self):
        return self.__interaction_Scenario

    @interaction_Scenario.setter
    def interaction_Scenario(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_interaction_Scenario__interaction_Scenario", None)
        self.__interaction_Scenario = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "interaction_Constraint18"):
                opp_val = getattr(old_value, "interaction_Constraint18", None)
                if opp_val == self:
                    setattr(old_value, "interaction_Constraint18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "interaction_Constraint18"):
                opp_val = getattr(value, "interaction_Constraint18", None)
                setattr(value, "interaction_Constraint18", self)

    @property
    def interaction_Scenario26(self):
        return self.__interaction_Scenario26

    @interaction_Scenario26.setter
    def interaction_Scenario26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_interaction_Scenario__interaction_Scenario26", None)
        self.__interaction_Scenario26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "interaction_AbstractFunction27"):
                    opp_val = getattr(item, "interaction_AbstractFunction27", None)
                    
                    if opp_val == self:
                        setattr(item, "interaction_AbstractFunction27", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "interaction_AbstractFunction27"):
                    opp_val = getattr(item, "interaction_AbstractFunction27", None)
                    
                    setattr(item, "interaction_AbstractFunction27", self)
                    

class interaction_FunctionalChain:

    pass
class interaction_State:

    pass
class CapellaElement:

    pass
class interaction_SequenceMessageValuation(CapellaElement):

    pass
class AbstractFunctionalChainContainer:

    pass
class Structure:

    pass
class interaction_AbstractCapability(CapellaElement, AbstractFunctionalChainContainer, Structure):

    pass
class interaction_AbstractFunction:

    pass
class interaction_Part:

    pass
class interaction_ExchangeItem:

    pass
class interaction_AbstractEventOperation:

    pass
class interaction_Constraint:

    pass
class NamedElement:

    pass
class interaction_InteractionOperand(NamedElement):

    pass
class interaction_CombinedFragment(NamedElement):

    def __init__(self, operator: str):
        self.operator = operator
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

class interaction_SequenceMessage(NamedElement):

    def __init__(self, kind: str, interaction_SequenceMessage: "interaction_Constraint" = None, interaction_SequenceMessage2: "interaction_AbstractEventOperation" = None, interaction_SequenceMessage4: set["interaction_ExchangeItem"] = None, interaction_SequenceMessage6: "interaction_Part" = None, interaction_SequenceMessage8: "interaction_Part" = None, interaction_SequenceMessage11: "interaction_AbstractFunction" = None, interaction_SequenceMessage13: "interaction_AbstractFunction" = None, interaction_SequenceMessage16: set["interaction_SequenceMessageValuation"] = None, interaction_SequenceMessage24: "interaction_Scenario" = None):
        self.kind = kind
        self.interaction_SequenceMessage = interaction_SequenceMessage
        self.interaction_SequenceMessage2 = interaction_SequenceMessage2
        self.interaction_SequenceMessage4 = interaction_SequenceMessage4 if interaction_SequenceMessage4 is not None else set()
        self.interaction_SequenceMessage6 = interaction_SequenceMessage6
        self.interaction_SequenceMessage8 = interaction_SequenceMessage8
        self.interaction_SequenceMessage11 = interaction_SequenceMessage11
        self.interaction_SequenceMessage13 = interaction_SequenceMessage13
        self.interaction_SequenceMessage16 = interaction_SequenceMessage16 if interaction_SequenceMessage16 is not None else set()
        self.interaction_SequenceMessage24 = interaction_SequenceMessage24
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def interaction_SequenceMessage11(self):
        return self.__interaction_SequenceMessage11

    @interaction_SequenceMessage11.setter
    def interaction_SequenceMessage11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_interaction_SequenceMessage__interaction_SequenceMessage11", None)
        self.__interaction_SequenceMessage11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "interaction_AbstractFunction"):
                opp_val = getattr(old_value, "interaction_AbstractFunction", None)
                if opp_val == self:
                    setattr(old_value, "interaction_AbstractFunction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "interaction_AbstractFunction"):
                opp_val = getattr(value, "interaction_AbstractFunction", None)
                setattr(value, "interaction_AbstractFunction", self)

    @property
    def interaction_SequenceMessage2(self):
        return self.__interaction_SequenceMessage2

    @interaction_SequenceMessage2.setter
    def interaction_SequenceMessage2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_interaction_SequenceMessage__interaction_SequenceMessage2", None)
        self.__interaction_SequenceMessage2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "interaction_AbstractEventOperation"):
                opp_val = getattr(old_value, "interaction_AbstractEventOperation", None)
                if opp_val == self:
                    setattr(old_value, "interaction_AbstractEventOperation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "interaction_AbstractEventOperation"):
                opp_val = getattr(value, "interaction_AbstractEventOperation", None)
                setattr(value, "interaction_AbstractEventOperation", self)

    @property
    def interaction_SequenceMessage16(self):
        return self.__interaction_SequenceMessage16

    @interaction_SequenceMessage16.setter
    def interaction_SequenceMessage16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_interaction_SequenceMessage__interaction_SequenceMessage16", None)
        self.__interaction_SequenceMessage16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "interaction_SequenceMessageValuation"):
                    opp_val = getattr(item, "interaction_SequenceMessageValuation", None)
                    
                    if opp_val == self:
                        setattr(item, "interaction_SequenceMessageValuation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "interaction_SequenceMessageValuation"):
                    opp_val = getattr(item, "interaction_SequenceMessageValuation", None)
                    
                    setattr(item, "interaction_SequenceMessageValuation", self)
                    

    @property
    def interaction_SequenceMessage(self):
        return self.__interaction_SequenceMessage

    @interaction_SequenceMessage.setter
    def interaction_SequenceMessage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_interaction_SequenceMessage__interaction_SequenceMessage", None)
        self.__interaction_SequenceMessage = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "interaction_Constraint"):
                opp_val = getattr(old_value, "interaction_Constraint", None)
                if opp_val == self:
                    setattr(old_value, "interaction_Constraint", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "interaction_Constraint"):
                opp_val = getattr(value, "interaction_Constraint", None)
                setattr(value, "interaction_Constraint", self)

    @property
    def interaction_SequenceMessage8(self):
        return self.__interaction_SequenceMessage8

    @interaction_SequenceMessage8.setter
    def interaction_SequenceMessage8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_interaction_SequenceMessage__interaction_SequenceMessage8", None)
        self.__interaction_SequenceMessage8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "interaction_Part9"):
                opp_val = getattr(old_value, "interaction_Part9", None)
                if opp_val == self:
                    setattr(old_value, "interaction_Part9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "interaction_Part9"):
                opp_val = getattr(value, "interaction_Part9", None)
                setattr(value, "interaction_Part9", self)

    @property
    def interaction_SequenceMessage6(self):
        return self.__interaction_SequenceMessage6

    @interaction_SequenceMessage6.setter
    def interaction_SequenceMessage6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_interaction_SequenceMessage__interaction_SequenceMessage6", None)
        self.__interaction_SequenceMessage6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "interaction_Part"):
                opp_val = getattr(old_value, "interaction_Part", None)
                if opp_val == self:
                    setattr(old_value, "interaction_Part", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "interaction_Part"):
                opp_val = getattr(value, "interaction_Part", None)
                setattr(value, "interaction_Part", self)

    @property
    def interaction_SequenceMessage24(self):
        return self.__interaction_SequenceMessage24

    @interaction_SequenceMessage24.setter
    def interaction_SequenceMessage24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_interaction_SequenceMessage__interaction_SequenceMessage24", None)
        self.__interaction_SequenceMessage24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "interaction_Scenario23"):
                opp_val = getattr(old_value, "interaction_Scenario23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "interaction_Scenario23"):
                opp_val = getattr(value, "interaction_Scenario23", None)
                if opp_val is None:
                    setattr(value, "interaction_Scenario23", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def interaction_SequenceMessage4(self):
        return self.__interaction_SequenceMessage4

    @interaction_SequenceMessage4.setter
    def interaction_SequenceMessage4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_interaction_SequenceMessage__interaction_SequenceMessage4", None)
        self.__interaction_SequenceMessage4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "interaction_ExchangeItem"):
                    opp_val = getattr(item, "interaction_ExchangeItem", None)
                    
                    if opp_val == self:
                        setattr(item, "interaction_ExchangeItem", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "interaction_ExchangeItem"):
                    opp_val = getattr(item, "interaction_ExchangeItem", None)
                    
                    setattr(item, "interaction_ExchangeItem", self)
                    

    @property
    def interaction_SequenceMessage13(self):
        return self.__interaction_SequenceMessage13

    @interaction_SequenceMessage13.setter
    def interaction_SequenceMessage13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_interaction_SequenceMessage__interaction_SequenceMessage13", None)
        self.__interaction_SequenceMessage13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "interaction_AbstractFunction14"):
                opp_val = getattr(old_value, "interaction_AbstractFunction14", None)
                if opp_val == self:
                    setattr(old_value, "interaction_AbstractFunction14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "interaction_AbstractFunction14"):
                opp_val = getattr(value, "interaction_AbstractFunction14", None)
                setattr(value, "interaction_AbstractFunction14", self)
