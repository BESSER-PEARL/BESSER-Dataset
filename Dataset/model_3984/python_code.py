from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class CauseType(Enum):
    InputEvent = "InputEvent"
    OutputEvent = "OutputEvent"
    BasicEvent = "BasicEvent"
    Gate = "Gate"
class FMEAType(Enum):
    FMEA = "FMEA"
    FMEDA = "FMEDA"
class GateType(Enum):
    OR = "OR"
    AND = "AND"
    NOT = "NOT"
    XOR = "XOR"
    VOTE = "VOTE"
    PAND = "PAND"
    POR = "POR"
    SAND = "SAND"
    InputEvent = "InputEvent"
    OutputEvent = "OutputEvent"
class FailureOriginType(Enum):
    Input = "Input"
    Output = "Output"
    Internal = "Internal"


############################################
# Definition of Classes
############################################

class FMEAEntry:

    pass
class failureLogic_FMEDAEntry(FMEAEntry):

    def __init__(self, diagnosisRate: float, failureLogic_FMEDAEntry: "failureLogic_ProbDist" = None):
        self.diagnosisRate = diagnosisRate
        self.failureLogic_FMEDAEntry = failureLogic_FMEDAEntry
        
    @property
    def diagnosisRate(self) -> float:
        return self.__diagnosisRate

    @diagnosisRate.setter
    def diagnosisRate(self, diagnosisRate: float):
        self.__diagnosisRate = diagnosisRate

    @property
    def failureLogic_FMEDAEntry(self):
        return self.__failureLogic_FMEDAEntry

    @failureLogic_FMEDAEntry.setter
    def failureLogic_FMEDAEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_failureLogic_FMEDAEntry__failureLogic_FMEDAEntry", None)
        self.__failureLogic_FMEDAEntry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "failureLogic_ProbDist52"):
                opp_val = getattr(old_value, "failureLogic_ProbDist52", None)
                if opp_val == self:
                    setattr(old_value, "failureLogic_ProbDist52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "failureLogic_ProbDist52"):
                opp_val = getattr(value, "failureLogic_ProbDist52", None)
                setattr(value, "failureLogic_ProbDist52", self)

class Cause:

    pass
class failureLogic_Gate(Cause):

    def __init__(self, gateType: str, failureLogic_Gate: set["failureLogic_Cause"] = None):
        self.gateType = gateType
        self.failureLogic_Gate = failureLogic_Gate if failureLogic_Gate is not None else set()
        
    @property
    def gateType(self) -> str:
        return self.__gateType

    @gateType.setter
    def gateType(self, gateType: str):
        self.__gateType = gateType

    @property
    def failureLogic_Gate(self):
        return self.__failureLogic_Gate

    @failureLogic_Gate.setter
    def failureLogic_Gate(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_failureLogic_Gate__failureLogic_Gate", None)
        self.__failureLogic_Gate = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "failureLogic_Cause28"):
                    opp_val = getattr(item, "failureLogic_Cause28", None)
                    
                    if opp_val == self:
                        setattr(item, "failureLogic_Cause28", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "failureLogic_Cause28"):
                    opp_val = getattr(item, "failureLogic_Cause28", None)
                    
                    setattr(item, "failureLogic_Cause28", self)
                    

class FailureModel:

    pass
class failureLogic_FMEA(FailureModel):

    def __init__(self, type: str, failureLogic_FMEA: set["failureLogic_FMEAEntry"] = None):
        self.type = type
        self.failureLogic_FMEA = failureLogic_FMEA if failureLogic_FMEA is not None else set()
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def failureLogic_FMEA(self):
        return self.__failureLogic_FMEA

    @failureLogic_FMEA.setter
    def failureLogic_FMEA(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_failureLogic_FMEA__failureLogic_FMEA", None)
        self.__failureLogic_FMEA = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "failureLogic_FMEAEntry"):
                    opp_val = getattr(item, "failureLogic_FMEAEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "failureLogic_FMEAEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "failureLogic_FMEAEntry"):
                    opp_val = getattr(item, "failureLogic_FMEAEntry", None)
                    
                    setattr(item, "failureLogic_FMEAEntry", self)
                    

class failureLogic_MarkovChain(FailureModel):

    pass
class failureLogic_FaultTree(FailureModel):

    pass
class Failure:

    pass
class failureLogic_SecurityViolation(Failure):

    pass
class BaseElement:

    pass
class failureLogic_Cause(BaseElement):

    def __init__(self, causeType: str, failureLogic_Cause: "failureLogic_FaultTree" = None, failureLogic_Cause25: "failureLogic_Failure" = None, failureLogic_Cause28: "failureLogic_Gate" = None):
        self.causeType = causeType
        self.failureLogic_Cause = failureLogic_Cause
        self.failureLogic_Cause25 = failureLogic_Cause25
        self.failureLogic_Cause28 = failureLogic_Cause28
        
    @property
    def causeType(self) -> str:
        return self.__causeType

    @causeType.setter
    def causeType(self, causeType: str):
        self.__causeType = causeType

    @property
    def failureLogic_Cause(self):
        return self.__failureLogic_Cause

    @failureLogic_Cause.setter
    def failureLogic_Cause(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_failureLogic_Cause__failureLogic_Cause", None)
        self.__failureLogic_Cause = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "failureLogic_FaultTree"):
                opp_val = getattr(old_value, "failureLogic_FaultTree", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "failureLogic_FaultTree"):
                opp_val = getattr(value, "failureLogic_FaultTree", None)
                if opp_val is None:
                    setattr(value, "failureLogic_FaultTree", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def failureLogic_Cause28(self):
        return self.__failureLogic_Cause28

    @failureLogic_Cause28.setter
    def failureLogic_Cause28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_failureLogic_Cause__failureLogic_Cause28", None)
        self.__failureLogic_Cause28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "failureLogic_Gate"):
                opp_val = getattr(old_value, "failureLogic_Gate", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "failureLogic_Gate"):
                opp_val = getattr(value, "failureLogic_Gate", None)
                if opp_val is None:
                    setattr(value, "failureLogic_Gate", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def failureLogic_Cause25(self):
        return self.__failureLogic_Cause25

    @failureLogic_Cause25.setter
    def failureLogic_Cause25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_failureLogic_Cause__failureLogic_Cause25", None)
        self.__failureLogic_Cause25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "failureLogic_Failure26"):
                opp_val = getattr(old_value, "failureLogic_Failure26", None)
                if opp_val == self:
                    setattr(old_value, "failureLogic_Failure26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "failureLogic_Failure26"):
                opp_val = getattr(value, "failureLogic_Failure26", None)
                setattr(value, "failureLogic_Failure26", self)

class failureLogic_FMEAEntry(BaseElement):

    pass
class failureLogic_State(BaseElement):

    def __init__(self, isInitialState: bool, isFailState: bool, failureLogic_State: "failureLogic_MarkovChain" = None, failureLogic_State33: "failureLogic_Failure" = None, failureLogic_State40: "failureLogic_Transition" = None, failureLogic_State43: "failureLogic_Transition" = None):
        self.isInitialState = isInitialState
        self.isFailState = isFailState
        self.failureLogic_State = failureLogic_State
        self.failureLogic_State33 = failureLogic_State33
        self.failureLogic_State40 = failureLogic_State40
        self.failureLogic_State43 = failureLogic_State43
        
    @property
    def isFailState(self) -> bool:
        return self.__isFailState

    @isFailState.setter
    def isFailState(self, isFailState: bool):
        self.__isFailState = isFailState

    @property
    def isInitialState(self) -> bool:
        return self.__isInitialState

    @isInitialState.setter
    def isInitialState(self, isInitialState: bool):
        self.__isInitialState = isInitialState

    @property
    def failureLogic_State40(self):
        return self.__failureLogic_State40

    @failureLogic_State40.setter
    def failureLogic_State40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_failureLogic_State__failureLogic_State40", None)
        self.__failureLogic_State40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "failureLogic_Transition39"):
                opp_val = getattr(old_value, "failureLogic_Transition39", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "failureLogic_Transition39"):
                opp_val = getattr(value, "failureLogic_Transition39", None)
                if opp_val is None:
                    setattr(value, "failureLogic_Transition39", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def failureLogic_State43(self):
        return self.__failureLogic_State43

    @failureLogic_State43.setter
    def failureLogic_State43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_failureLogic_State__failureLogic_State43", None)
        self.__failureLogic_State43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "failureLogic_Transition42"):
                opp_val = getattr(old_value, "failureLogic_Transition42", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "failureLogic_Transition42"):
                opp_val = getattr(value, "failureLogic_Transition42", None)
                if opp_val is None:
                    setattr(value, "failureLogic_Transition42", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def failureLogic_State33(self):
        return self.__failureLogic_State33

    @failureLogic_State33.setter
    def failureLogic_State33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_failureLogic_State__failureLogic_State33", None)
        self.__failureLogic_State33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "failureLogic_Failure34"):
                opp_val = getattr(old_value, "failureLogic_Failure34", None)
                if opp_val == self:
                    setattr(old_value, "failureLogic_Failure34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "failureLogic_Failure34"):
                opp_val = getattr(value, "failureLogic_Failure34", None)
                setattr(value, "failureLogic_Failure34", self)

    @property
    def failureLogic_State(self):
        return self.__failureLogic_State

    @failureLogic_State.setter
    def failureLogic_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_failureLogic_State__failureLogic_State", None)
        self.__failureLogic_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "failureLogic_MarkovChain31"):
                opp_val = getattr(old_value, "failureLogic_MarkovChain31", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "failureLogic_MarkovChain31"):
                opp_val = getattr(value, "failureLogic_MarkovChain31", None)
                if opp_val is None:
                    setattr(value, "failureLogic_MarkovChain31", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class failureLogic_Transition(BaseElement):

    def __init__(self, transition: float, failureLogic_Transition: "failureLogic_MarkovChain" = None, failureLogic_Transition36: "failureLogic_ProbDist" = None, failureLogic_Transition39: set["failureLogic_State"] = None, failureLogic_Transition42: set["failureLogic_State"] = None):
        self.transition = transition
        self.failureLogic_Transition = failureLogic_Transition
        self.failureLogic_Transition36 = failureLogic_Transition36
        self.failureLogic_Transition39 = failureLogic_Transition39 if failureLogic_Transition39 is not None else set()
        self.failureLogic_Transition42 = failureLogic_Transition42 if failureLogic_Transition42 is not None else set()
        
    @property
    def transition(self) -> float:
        return self.__transition

    @transition.setter
    def transition(self, transition: float):
        self.__transition = transition

    @property
    def failureLogic_Transition39(self):
        return self.__failureLogic_Transition39

    @failureLogic_Transition39.setter
    def failureLogic_Transition39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_failureLogic_Transition__failureLogic_Transition39", None)
        self.__failureLogic_Transition39 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "failureLogic_State40"):
                    opp_val = getattr(item, "failureLogic_State40", None)
                    
                    if opp_val == self:
                        setattr(item, "failureLogic_State40", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "failureLogic_State40"):
                    opp_val = getattr(item, "failureLogic_State40", None)
                    
                    setattr(item, "failureLogic_State40", self)
                    

    @property
    def failureLogic_Transition36(self):
        return self.__failureLogic_Transition36

    @failureLogic_Transition36.setter
    def failureLogic_Transition36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_failureLogic_Transition__failureLogic_Transition36", None)
        self.__failureLogic_Transition36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "failureLogic_ProbDist37"):
                opp_val = getattr(old_value, "failureLogic_ProbDist37", None)
                if opp_val == self:
                    setattr(old_value, "failureLogic_ProbDist37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "failureLogic_ProbDist37"):
                opp_val = getattr(value, "failureLogic_ProbDist37", None)
                setattr(value, "failureLogic_ProbDist37", self)

    @property
    def failureLogic_Transition(self):
        return self.__failureLogic_Transition

    @failureLogic_Transition.setter
    def failureLogic_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_failureLogic_Transition__failureLogic_Transition", None)
        self.__failureLogic_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "failureLogic_MarkovChain"):
                opp_val = getattr(old_value, "failureLogic_MarkovChain", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "failureLogic_MarkovChain"):
                opp_val = getattr(value, "failureLogic_MarkovChain", None)
                if opp_val is None:
                    setattr(value, "failureLogic_MarkovChain", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def failureLogic_Transition42(self):
        return self.__failureLogic_Transition42

    @failureLogic_Transition42.setter
    def failureLogic_Transition42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_failureLogic_Transition__failureLogic_Transition42", None)
        self.__failureLogic_Transition42 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "failureLogic_State43"):
                    opp_val = getattr(item, "failureLogic_State43", None)
                    
                    if opp_val == self:
                        setattr(item, "failureLogic_State43", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "failureLogic_State43"):
                    opp_val = getattr(item, "failureLogic_State43", None)
                    
                    setattr(item, "failureLogic_State43", self)
                    

class failureLogic_ProbDist(BaseElement):

    def __init__(self, type: str, failureLogic_ProbDist22: set["failureLogic_ProbDistParam"] = None, failureLogic_ProbDist: "failureLogic_Failure" = None, failureLogic_ProbDist52: "failureLogic_FMEDAEntry" = None, failureLogic_ProbDist37: "failureLogic_Transition" = None):
        self.type = type
        self.failureLogic_ProbDist22 = failureLogic_ProbDist22 if failureLogic_ProbDist22 is not None else set()
        self.failureLogic_ProbDist = failureLogic_ProbDist
        self.failureLogic_ProbDist52 = failureLogic_ProbDist52
        self.failureLogic_ProbDist37 = failureLogic_ProbDist37
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def failureLogic_ProbDist22(self):
        return self.__failureLogic_ProbDist22

    @failureLogic_ProbDist22.setter
    def failureLogic_ProbDist22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_failureLogic_ProbDist__failureLogic_ProbDist22", None)
        self.__failureLogic_ProbDist22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "failureLogic_ProbDistParam"):
                    opp_val = getattr(item, "failureLogic_ProbDistParam", None)
                    
                    if opp_val == self:
                        setattr(item, "failureLogic_ProbDistParam", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "failureLogic_ProbDistParam"):
                    opp_val = getattr(item, "failureLogic_ProbDistParam", None)
                    
                    setattr(item, "failureLogic_ProbDistParam", self)
                    

    @property
    def failureLogic_ProbDist37(self):
        return self.__failureLogic_ProbDist37

    @failureLogic_ProbDist37.setter
    def failureLogic_ProbDist37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_failureLogic_ProbDist__failureLogic_ProbDist37", None)
        self.__failureLogic_ProbDist37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "failureLogic_Transition36"):
                opp_val = getattr(old_value, "failureLogic_Transition36", None)
                if opp_val == self:
                    setattr(old_value, "failureLogic_Transition36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "failureLogic_Transition36"):
                opp_val = getattr(value, "failureLogic_Transition36", None)
                setattr(value, "failureLogic_Transition36", self)

    @property
    def failureLogic_ProbDist(self):
        return self.__failureLogic_ProbDist

    @failureLogic_ProbDist.setter
    def failureLogic_ProbDist(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_failureLogic_ProbDist__failureLogic_ProbDist", None)
        self.__failureLogic_ProbDist = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "failureLogic_Failure"):
                opp_val = getattr(old_value, "failureLogic_Failure", None)
                if opp_val == self:
                    setattr(old_value, "failureLogic_Failure", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "failureLogic_Failure"):
                opp_val = getattr(value, "failureLogic_Failure", None)
                setattr(value, "failureLogic_Failure", self)

    @property
    def failureLogic_ProbDist52(self):
        return self.__failureLogic_ProbDist52

    @failureLogic_ProbDist52.setter
    def failureLogic_ProbDist52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_failureLogic_ProbDist__failureLogic_ProbDist52", None)
        self.__failureLogic_ProbDist52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "failureLogic_FMEDAEntry"):
                opp_val = getattr(old_value, "failureLogic_FMEDAEntry", None)
                if opp_val == self:
                    setattr(old_value, "failureLogic_FMEDAEntry", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "failureLogic_FMEDAEntry"):
                opp_val = getattr(value, "failureLogic_FMEDAEntry", None)
                setattr(value, "failureLogic_FMEDAEntry", self)

class failureLogic_Failure(BaseElement):

    def __init__(self, originType: str, failureClass: str, failureRate: float, isCcf: bool, failureLogic_Failure9: "failureLogic_FailureModel" = None, failureLogic_Failure17: "failureLogic_MinimalCutSets" = None, failureLogic_Failure20: "failureLogic_MinimalCutset" = None, failureLogic_Failure: "failureLogic_ProbDist" = None, failureLogic_Failure4: "failureLogic_Failure" = None, failureLogic_Failure2: set["failureLogic_Failure"] = None, failureLogic_Failure26: "failureLogic_Cause" = None, failureLogic_Failure34: "failureLogic_State" = None, failureLogic_Failure47: "failureLogic_FMEAEntry" = None, failureLogic_Failure50: "failureLogic_FMEAEntry" = None):
        self.originType = originType
        self.failureClass = failureClass
        self.failureRate = failureRate
        self.isCcf = isCcf
        self.failureLogic_Failure9 = failureLogic_Failure9
        self.failureLogic_Failure17 = failureLogic_Failure17
        self.failureLogic_Failure20 = failureLogic_Failure20
        self.failureLogic_Failure = failureLogic_Failure
        self.failureLogic_Failure4 = failureLogic_Failure4
        self.failureLogic_Failure2 = failureLogic_Failure2 if failureLogic_Failure2 is not None else set()
        self.failureLogic_Failure26 = failureLogic_Failure26
        self.failureLogic_Failure34 = failureLogic_Failure34
        self.failureLogic_Failure47 = failureLogic_Failure47
        self.failureLogic_Failure50 = failureLogic_Failure50
        
    @property
    def failureClass(self) -> str:
        return self.__failureClass

    @failureClass.setter
    def failureClass(self, failureClass: str):
        self.__failureClass = failureClass

    @property
    def isCcf(self) -> bool:
        return self.__isCcf

    @isCcf.setter
    def isCcf(self, isCcf: bool):
        self.__isCcf = isCcf

    @property
    def originType(self) -> str:
        return self.__originType

    @originType.setter
    def originType(self, originType: str):
        self.__originType = originType

    @property
    def failureRate(self) -> float:
        return self.__failureRate

    @failureRate.setter
    def failureRate(self, failureRate: float):
        self.__failureRate = failureRate

    @property
    def failureLogic_Failure9(self):
        return self.__failureLogic_Failure9

    @failureLogic_Failure9.setter
    def failureLogic_Failure9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_failureLogic_Failure__failureLogic_Failure9", None)
        self.__failureLogic_Failure9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "failureLogic_FailureModel8"):
                opp_val = getattr(old_value, "failureLogic_FailureModel8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "failureLogic_FailureModel8"):
                opp_val = getattr(value, "failureLogic_FailureModel8", None)
                if opp_val is None:
                    setattr(value, "failureLogic_FailureModel8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def failureLogic_Failure(self):
        return self.__failureLogic_Failure

    @failureLogic_Failure.setter
    def failureLogic_Failure(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_failureLogic_Failure__failureLogic_Failure", None)
        self.__failureLogic_Failure = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "failureLogic_ProbDist"):
                opp_val = getattr(old_value, "failureLogic_ProbDist", None)
                if opp_val == self:
                    setattr(old_value, "failureLogic_ProbDist", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "failureLogic_ProbDist"):
                opp_val = getattr(value, "failureLogic_ProbDist", None)
                setattr(value, "failureLogic_ProbDist", self)

    @property
    def failureLogic_Failure34(self):
        return self.__failureLogic_Failure34

    @failureLogic_Failure34.setter
    def failureLogic_Failure34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_failureLogic_Failure__failureLogic_Failure34", None)
        self.__failureLogic_Failure34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "failureLogic_State33"):
                opp_val = getattr(old_value, "failureLogic_State33", None)
                if opp_val == self:
                    setattr(old_value, "failureLogic_State33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "failureLogic_State33"):
                opp_val = getattr(value, "failureLogic_State33", None)
                setattr(value, "failureLogic_State33", self)

    @property
    def failureLogic_Failure50(self):
        return self.__failureLogic_Failure50

    @failureLogic_Failure50.setter
    def failureLogic_Failure50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_failureLogic_Failure__failureLogic_Failure50", None)
        self.__failureLogic_Failure50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "failureLogic_FMEAEntry49"):
                opp_val = getattr(old_value, "failureLogic_FMEAEntry49", None)
                if opp_val == self:
                    setattr(old_value, "failureLogic_FMEAEntry49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "failureLogic_FMEAEntry49"):
                opp_val = getattr(value, "failureLogic_FMEAEntry49", None)
                setattr(value, "failureLogic_FMEAEntry49", self)

    @property
    def failureLogic_Failure47(self):
        return self.__failureLogic_Failure47

    @failureLogic_Failure47.setter
    def failureLogic_Failure47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_failureLogic_Failure__failureLogic_Failure47", None)
        self.__failureLogic_Failure47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "failureLogic_FMEAEntry46"):
                opp_val = getattr(old_value, "failureLogic_FMEAEntry46", None)
                if opp_val == self:
                    setattr(old_value, "failureLogic_FMEAEntry46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "failureLogic_FMEAEntry46"):
                opp_val = getattr(value, "failureLogic_FMEAEntry46", None)
                setattr(value, "failureLogic_FMEAEntry46", self)

    @property
    def failureLogic_Failure2(self):
        return self.__failureLogic_Failure2

    @failureLogic_Failure2.setter
    def failureLogic_Failure2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_failureLogic_Failure__failureLogic_Failure2", None)
        self.__failureLogic_Failure2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "failureLogic_Failure4"):
                    opp_val = getattr(item, "failureLogic_Failure4", None)
                    
                    if opp_val == self:
                        setattr(item, "failureLogic_Failure4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "failureLogic_Failure4"):
                    opp_val = getattr(item, "failureLogic_Failure4", None)
                    
                    setattr(item, "failureLogic_Failure4", self)
                    

    @property
    def failureLogic_Failure20(self):
        return self.__failureLogic_Failure20

    @failureLogic_Failure20.setter
    def failureLogic_Failure20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_failureLogic_Failure__failureLogic_Failure20", None)
        self.__failureLogic_Failure20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "failureLogic_MinimalCutset19"):
                opp_val = getattr(old_value, "failureLogic_MinimalCutset19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "failureLogic_MinimalCutset19"):
                opp_val = getattr(value, "failureLogic_MinimalCutset19", None)
                if opp_val is None:
                    setattr(value, "failureLogic_MinimalCutset19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def failureLogic_Failure17(self):
        return self.__failureLogic_Failure17

    @failureLogic_Failure17.setter
    def failureLogic_Failure17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_failureLogic_Failure__failureLogic_Failure17", None)
        self.__failureLogic_Failure17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "failureLogic_MinimalCutSets16"):
                opp_val = getattr(old_value, "failureLogic_MinimalCutSets16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "failureLogic_MinimalCutSets16"):
                opp_val = getattr(value, "failureLogic_MinimalCutSets16", None)
                if opp_val is None:
                    setattr(value, "failureLogic_MinimalCutSets16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def failureLogic_Failure26(self):
        return self.__failureLogic_Failure26

    @failureLogic_Failure26.setter
    def failureLogic_Failure26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_failureLogic_Failure__failureLogic_Failure26", None)
        self.__failureLogic_Failure26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "failureLogic_Cause25"):
                opp_val = getattr(old_value, "failureLogic_Cause25", None)
                if opp_val == self:
                    setattr(old_value, "failureLogic_Cause25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "failureLogic_Cause25"):
                opp_val = getattr(value, "failureLogic_Cause25", None)
                setattr(value, "failureLogic_Cause25", self)

    @property
    def failureLogic_Failure4(self):
        return self.__failureLogic_Failure4

    @failureLogic_Failure4.setter
    def failureLogic_Failure4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_failureLogic_Failure__failureLogic_Failure4", None)
        self.__failureLogic_Failure4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "failureLogic_Failure2"):
                opp_val = getattr(old_value, "failureLogic_Failure2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "failureLogic_Failure2"):
                opp_val = getattr(value, "failureLogic_Failure2", None)
                if opp_val is None:
                    setattr(value, "failureLogic_Failure2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class failureLogic_FailureModel(BaseElement):

    pass
class failureLogic_ProbDistParam(BaseElement):

    def __init__(self, value: str, failureLogic_ProbDistParam: "failureLogic_ProbDist" = None):
        self.value = value
        self.failureLogic_ProbDistParam = failureLogic_ProbDistParam
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def failureLogic_ProbDistParam(self):
        return self.__failureLogic_ProbDistParam

    @failureLogic_ProbDistParam.setter
    def failureLogic_ProbDistParam(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_failureLogic_ProbDistParam__failureLogic_ProbDistParam", None)
        self.__failureLogic_ProbDistParam = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "failureLogic_ProbDist22"):
                opp_val = getattr(old_value, "failureLogic_ProbDist22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "failureLogic_ProbDist22"):
                opp_val = getattr(value, "failureLogic_ProbDist22", None)
                if opp_val is None:
                    setattr(value, "failureLogic_ProbDist22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class failureLogic_MinimalCutset(BaseElement):

    pass
class failureLogic_MinimalCutSets(BaseElement):

    pass
class ODEProductPackage:

    pass
class failureLogic_FailureLogicPackage(ODEProductPackage):

    pass