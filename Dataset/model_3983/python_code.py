from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

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
class CauseType(Enum):
    InputEvent = "InputEvent"
    OutputEvent = "OutputEvent"
    BasicEvent = "BasicEvent"
    Gate = "Gate"
class FMEAType(Enum):
    FMEA = "FMEA"
    FMEDA = "FMEDA"
class FailureOriginType(Enum):
    Input = "Input"
    Output = "Output"
    Internal = "Internal"


############################################
# Definition of Classes
############################################

class FMEA_failureLogic_ProbDist:

    pass
class FMEA_failureLogic_Failure:

    pass
class FTA_failureLogic_Failure:

    pass
class Cause:

    pass
class failureLogic_FTA_Gate(Cause):

    def __init__(self, gateType: str, failureLogic_FTA_Gate: set["Cause"] = None, Cause26: "failureLogic_FTA_Gate", Cause: "failureLogic_FTA_FaultTree"):
        self.gateType = gateType
        self.failureLogic_FTA_Gate = failureLogic_FTA_Gate if failureLogic_FTA_Gate is not None else set()
        
    @property
    def gateType(self) -> str:
        return self.__gateType

    @gateType.setter
    def gateType(self, gateType: str):
        self.__gateType = gateType

    @property
    def failureLogic_FTA_Gate(self):
        return self.__failureLogic_FTA_Gate

    @failureLogic_FTA_Gate.setter
    def failureLogic_FTA_Gate(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_failureLogic_FTA_Gate__failureLogic_FTA_Gate", None)
        self.__failureLogic_FTA_Gate = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Cause26"):
                    opp_val = getattr(item, "Cause26", None)
                    
                    if opp_val == self:
                        setattr(item, "Cause26", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Cause26"):
                    opp_val = getattr(item, "Cause26", None)
                    
                    setattr(item, "Cause26", self)
                    

class FailureModel:

    pass
class failureLogic_FTA_FaultTree(FailureModel):

    pass
class FMEAEntry:

    pass
class failureLogic_FMEA_FMEDAEntry(FMEAEntry):

    def __init__(self, diagnosisRate: float, failureLogic_FMEA_FMEDAEntry: "FMEA_failureLogic_ProbDist" = None, FMEAEntry: "failureLogic_FMEA_FMEA"):
        self.diagnosisRate = diagnosisRate
        self.failureLogic_FMEA_FMEDAEntry = failureLogic_FMEA_FMEDAEntry
        
    @property
    def diagnosisRate(self) -> float:
        return self.__diagnosisRate

    @diagnosisRate.setter
    def diagnosisRate(self, diagnosisRate: float):
        self.__diagnosisRate = diagnosisRate

    @property
    def failureLogic_FMEA_FMEDAEntry(self):
        return self.__failureLogic_FMEA_FMEDAEntry

    @failureLogic_FMEA_FMEDAEntry.setter
    def failureLogic_FMEA_FMEDAEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_failureLogic_FMEA_FMEDAEntry__failureLogic_FMEA_FMEDAEntry", None)
        self.__failureLogic_FMEA_FMEDAEntry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FMEA_failureLogic_ProbDist"):
                opp_val = getattr(old_value, "FMEA_failureLogic_ProbDist", None)
                if opp_val == self:
                    setattr(old_value, "FMEA_failureLogic_ProbDist", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FMEA_failureLogic_ProbDist"):
                opp_val = getattr(value, "FMEA_failureLogic_ProbDist", None)
                setattr(value, "FMEA_failureLogic_ProbDist", self)

class failureLogic_FMEA_FMEA(FailureModel):

    def __init__(self, type: str, failureLogic_FMEA_FMEA: set["FMEAEntry"] = None):
        self.type = type
        self.failureLogic_FMEA_FMEA = failureLogic_FMEA_FMEA if failureLogic_FMEA_FMEA is not None else set()
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def failureLogic_FMEA_FMEA(self):
        return self.__failureLogic_FMEA_FMEA

    @failureLogic_FMEA_FMEA.setter
    def failureLogic_FMEA_FMEA(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_failureLogic_FMEA_FMEA__failureLogic_FMEA_FMEA", None)
        self.__failureLogic_FMEA_FMEA = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "FMEAEntry"):
                    opp_val = getattr(item, "FMEAEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "FMEAEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FMEAEntry"):
                    opp_val = getattr(item, "FMEAEntry", None)
                    
                    setattr(item, "FMEAEntry", self)
                    

class Markov_failureLogic_ProbDist:

    pass
class Markov_failureLogic_Failure:

    pass
class State:

    pass
class Transition:

    pass
class failureLogic_Markov_MarkovChain(FailureModel):

    pass
class Failure:

    pass
class failureLogic_SecurityViolation(Failure):

    pass
class BaseElement:

    pass
class failureLogic_ProbDist(BaseElement):

    def __init__(self, type: str, failureLogic_ProbDist22: set["failureLogic_ProbDistParam"] = None, failureLogic_ProbDist: "failureLogic_Failure" = None):
        self.type = type
        self.failureLogic_ProbDist22 = failureLogic_ProbDist22 if failureLogic_ProbDist22 is not None else set()
        self.failureLogic_ProbDist = failureLogic_ProbDist
        
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

class failureLogic_Markov_State(BaseElement):

    def __init__(self, isInitialState: bool, isFailState: bool, failureLogic_Markov_State: "Markov_failureLogic_Failure" = None):
        self.isInitialState = isInitialState
        self.isFailState = isFailState
        self.failureLogic_Markov_State = failureLogic_Markov_State
        
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
    def failureLogic_Markov_State(self):
        return self.__failureLogic_Markov_State

    @failureLogic_Markov_State.setter
    def failureLogic_Markov_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_failureLogic_Markov_State__failureLogic_Markov_State", None)
        self.__failureLogic_Markov_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Markov_failureLogic_Failure"):
                opp_val = getattr(old_value, "Markov_failureLogic_Failure", None)
                if opp_val == self:
                    setattr(old_value, "Markov_failureLogic_Failure", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Markov_failureLogic_Failure"):
                opp_val = getattr(value, "Markov_failureLogic_Failure", None)
                setattr(value, "Markov_failureLogic_Failure", self)

class failureLogic_Markov_Transition(BaseElement):

    def __init__(self, transition: float, failureLogic_Markov_Transition: "Markov_failureLogic_ProbDist" = None, failureLogic_Markov_Transition33: set["State"] = None, failureLogic_Markov_Transition36: set["State"] = None):
        self.transition = transition
        self.failureLogic_Markov_Transition = failureLogic_Markov_Transition
        self.failureLogic_Markov_Transition33 = failureLogic_Markov_Transition33 if failureLogic_Markov_Transition33 is not None else set()
        self.failureLogic_Markov_Transition36 = failureLogic_Markov_Transition36 if failureLogic_Markov_Transition36 is not None else set()
        
    @property
    def transition(self) -> float:
        return self.__transition

    @transition.setter
    def transition(self, transition: float):
        self.__transition = transition

    @property
    def failureLogic_Markov_Transition36(self):
        return self.__failureLogic_Markov_Transition36

    @failureLogic_Markov_Transition36.setter
    def failureLogic_Markov_Transition36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_failureLogic_Markov_Transition__failureLogic_Markov_Transition36", None)
        self.__failureLogic_Markov_Transition36 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "State37"):
                    opp_val = getattr(item, "State37", None)
                    
                    if opp_val == self:
                        setattr(item, "State37", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "State37"):
                    opp_val = getattr(item, "State37", None)
                    
                    setattr(item, "State37", self)
                    

    @property
    def failureLogic_Markov_Transition(self):
        return self.__failureLogic_Markov_Transition

    @failureLogic_Markov_Transition.setter
    def failureLogic_Markov_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_failureLogic_Markov_Transition__failureLogic_Markov_Transition", None)
        self.__failureLogic_Markov_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Markov_failureLogic_ProbDist"):
                opp_val = getattr(old_value, "Markov_failureLogic_ProbDist", None)
                if opp_val == self:
                    setattr(old_value, "Markov_failureLogic_ProbDist", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Markov_failureLogic_ProbDist"):
                opp_val = getattr(value, "Markov_failureLogic_ProbDist", None)
                setattr(value, "Markov_failureLogic_ProbDist", self)

    @property
    def failureLogic_Markov_Transition33(self):
        return self.__failureLogic_Markov_Transition33

    @failureLogic_Markov_Transition33.setter
    def failureLogic_Markov_Transition33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_failureLogic_Markov_Transition__failureLogic_Markov_Transition33", None)
        self.__failureLogic_Markov_Transition33 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "State34"):
                    opp_val = getattr(item, "State34", None)
                    
                    if opp_val == self:
                        setattr(item, "State34", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "State34"):
                    opp_val = getattr(item, "State34", None)
                    
                    setattr(item, "State34", self)
                    

class failureLogic_FTA_Cause(BaseElement):

    def __init__(self, type: str, failureLogic_FTA_Cause: "FTA_failureLogic_Failure" = None):
        self.type = type
        self.failureLogic_FTA_Cause = failureLogic_FTA_Cause
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def failureLogic_FTA_Cause(self):
        return self.__failureLogic_FTA_Cause

    @failureLogic_FTA_Cause.setter
    def failureLogic_FTA_Cause(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_failureLogic_FTA_Cause__failureLogic_FTA_Cause", None)
        self.__failureLogic_FTA_Cause = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FTA_failureLogic_Failure"):
                opp_val = getattr(old_value, "FTA_failureLogic_Failure", None)
                if opp_val == self:
                    setattr(old_value, "FTA_failureLogic_Failure", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FTA_failureLogic_Failure"):
                opp_val = getattr(value, "FTA_failureLogic_Failure", None)
                setattr(value, "FTA_failureLogic_Failure", self)

class failureLogic_MinimalCutSets(BaseElement):

    pass
class failureLogic_FMEA_FMEAEntry(BaseElement):

    pass
class failureLogic_Failure(BaseElement):

    def __init__(self, originType: str, failureClass: str, failureRate: float, isCcf: bool, failureLogic_Failure9: "failureLogic_FailureModel" = None, failureLogic_Failure17: "failureLogic_MinimalCutSets" = None, failureLogic_Failure20: "failureLogic_MinimalCutset" = None, failureLogic_Failure: "failureLogic_ProbDist" = None, failureLogic_Failure4: "failureLogic_Failure" = None, failureLogic_Failure2: set["failureLogic_Failure"] = None):
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
class failureLogic_FailureModel(BaseElement):

    pass
class failureLogic_FailureLogicPackage:

    pass