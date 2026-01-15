from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class cbmg_RequestParameter:

    def __init__(self, parameterName: str, parameterValue: str, cbmg_RequestParameter: "cbmg_Transition" = None, cbmg_RequestParameter13: "cbmg_Transition" = None):
        self.parameterName = parameterName
        self.parameterValue = parameterValue
        self.cbmg_RequestParameter = cbmg_RequestParameter
        self.cbmg_RequestParameter13 = cbmg_RequestParameter13
        
    @property
    def parameterName(self) -> str:
        return self.__parameterName

    @parameterName.setter
    def parameterName(self, parameterName: str):
        self.__parameterName = parameterName

    @property
    def parameterValue(self) -> str:
        return self.__parameterValue

    @parameterValue.setter
    def parameterValue(self, parameterValue: str):
        self.__parameterValue = parameterValue

    @property
    def cbmg_RequestParameter13(self):
        return self.__cbmg_RequestParameter13

    @cbmg_RequestParameter13.setter
    def cbmg_RequestParameter13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cbmg_RequestParameter__cbmg_RequestParameter13", None)
        self.__cbmg_RequestParameter13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cbmg_Transition14"):
                opp_val = getattr(old_value, "cbmg_Transition14", None)
                if opp_val == self:
                    setattr(old_value, "cbmg_Transition14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cbmg_Transition14"):
                opp_val = getattr(value, "cbmg_Transition14", None)
                setattr(value, "cbmg_Transition14", self)

    @property
    def cbmg_RequestParameter(self):
        return self.__cbmg_RequestParameter

    @cbmg_RequestParameter.setter
    def cbmg_RequestParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cbmg_RequestParameter__cbmg_RequestParameter", None)
        self.__cbmg_RequestParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cbmg_Transition11"):
                opp_val = getattr(old_value, "cbmg_Transition11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cbmg_Transition11"):
                opp_val = getattr(value, "cbmg_Transition11", None)
                if opp_val is None:
                    setattr(value, "cbmg_Transition11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class cbmg_Transition:

    def __init__(self, method: str, probability: float, thinkTime: float, nbrOfTransitions: int, accept: str, condition: str, cbmg_Transition: "cbmg_State" = None, cbmg_Transition5: "cbmg_State" = None, cbmg_Transition8: "cbmg_State" = None, cbmg_Transition11: set["cbmg_RequestParameter"] = None, cbmg_Transition3: "cbmg_State" = None, cbmg_Transition14: "cbmg_RequestParameter" = None):
        self.method = method
        self.probability = probability
        self.thinkTime = thinkTime
        self.nbrOfTransitions = nbrOfTransitions
        self.accept = accept
        self.condition = condition
        self.cbmg_Transition = cbmg_Transition
        self.cbmg_Transition5 = cbmg_Transition5
        self.cbmg_Transition8 = cbmg_Transition8
        self.cbmg_Transition11 = cbmg_Transition11 if cbmg_Transition11 is not None else set()
        self.cbmg_Transition3 = cbmg_Transition3
        self.cbmg_Transition14 = cbmg_Transition14
        
    @property
    def accept(self) -> str:
        return self.__accept

    @accept.setter
    def accept(self, accept: str):
        self.__accept = accept

    @property
    def condition(self) -> str:
        return self.__condition

    @condition.setter
    def condition(self, condition: str):
        self.__condition = condition

    @property
    def nbrOfTransitions(self) -> int:
        return self.__nbrOfTransitions

    @nbrOfTransitions.setter
    def nbrOfTransitions(self, nbrOfTransitions: int):
        self.__nbrOfTransitions = nbrOfTransitions

    @property
    def probability(self) -> float:
        return self.__probability

    @probability.setter
    def probability(self, probability: float):
        self.__probability = probability

    @property
    def method(self) -> str:
        return self.__method

    @method.setter
    def method(self, method: str):
        self.__method = method

    @property
    def thinkTime(self) -> float:
        return self.__thinkTime

    @thinkTime.setter
    def thinkTime(self, thinkTime: float):
        self.__thinkTime = thinkTime

    @property
    def cbmg_Transition3(self):
        return self.__cbmg_Transition3

    @cbmg_Transition3.setter
    def cbmg_Transition3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cbmg_Transition__cbmg_Transition3", None)
        self.__cbmg_Transition3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cbmg_State2"):
                opp_val = getattr(old_value, "cbmg_State2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cbmg_State2"):
                opp_val = getattr(value, "cbmg_State2", None)
                if opp_val is None:
                    setattr(value, "cbmg_State2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cbmg_Transition(self):
        return self.__cbmg_Transition

    @cbmg_Transition.setter
    def cbmg_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cbmg_Transition__cbmg_Transition", None)
        self.__cbmg_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cbmg_State"):
                opp_val = getattr(old_value, "cbmg_State", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cbmg_State"):
                opp_val = getattr(value, "cbmg_State", None)
                if opp_val is None:
                    setattr(value, "cbmg_State", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cbmg_Transition5(self):
        return self.__cbmg_Transition5

    @cbmg_Transition5.setter
    def cbmg_Transition5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cbmg_Transition__cbmg_Transition5", None)
        self.__cbmg_Transition5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cbmg_State6"):
                opp_val = getattr(old_value, "cbmg_State6", None)
                if opp_val == self:
                    setattr(old_value, "cbmg_State6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cbmg_State6"):
                opp_val = getattr(value, "cbmg_State6", None)
                setattr(value, "cbmg_State6", self)

    @property
    def cbmg_Transition11(self):
        return self.__cbmg_Transition11

    @cbmg_Transition11.setter
    def cbmg_Transition11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cbmg_Transition__cbmg_Transition11", None)
        self.__cbmg_Transition11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cbmg_RequestParameter"):
                    opp_val = getattr(item, "cbmg_RequestParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "cbmg_RequestParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cbmg_RequestParameter"):
                    opp_val = getattr(item, "cbmg_RequestParameter", None)
                    
                    setattr(item, "cbmg_RequestParameter", self)
                    

    @property
    def cbmg_Transition14(self):
        return self.__cbmg_Transition14

    @cbmg_Transition14.setter
    def cbmg_Transition14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cbmg_Transition__cbmg_Transition14", None)
        self.__cbmg_Transition14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cbmg_RequestParameter13"):
                opp_val = getattr(old_value, "cbmg_RequestParameter13", None)
                if opp_val == self:
                    setattr(old_value, "cbmg_RequestParameter13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cbmg_RequestParameter13"):
                opp_val = getattr(value, "cbmg_RequestParameter13", None)
                setattr(value, "cbmg_RequestParameter13", self)

    @property
    def cbmg_Transition8(self):
        return self.__cbmg_Transition8

    @cbmg_Transition8.setter
    def cbmg_Transition8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cbmg_Transition__cbmg_Transition8", None)
        self.__cbmg_Transition8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cbmg_State9"):
                opp_val = getattr(old_value, "cbmg_State9", None)
                if opp_val == self:
                    setattr(old_value, "cbmg_State9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cbmg_State9"):
                opp_val = getattr(value, "cbmg_State9", None)
                setattr(value, "cbmg_State9", self)

class cbmg_State:

    def __init__(self, port: int, localName: str, isStartState: bool, isEndState: bool, requestURL: str, localAddr: str, cbmg_State: set["cbmg_Transition"] = None, cbmg_State6: "cbmg_Transition" = None, cbmg_State9: "cbmg_Transition" = None, cbmg_State2: set["cbmg_Transition"] = None):
        self.port = port
        self.localName = localName
        self.isStartState = isStartState
        self.isEndState = isEndState
        self.requestURL = requestURL
        self.localAddr = localAddr
        self.cbmg_State = cbmg_State if cbmg_State is not None else set()
        self.cbmg_State6 = cbmg_State6
        self.cbmg_State9 = cbmg_State9
        self.cbmg_State2 = cbmg_State2 if cbmg_State2 is not None else set()
        
    @property
    def isEndState(self) -> bool:
        return self.__isEndState

    @isEndState.setter
    def isEndState(self, isEndState: bool):
        self.__isEndState = isEndState

    @property
    def localAddr(self) -> str:
        return self.__localAddr

    @localAddr.setter
    def localAddr(self, localAddr: str):
        self.__localAddr = localAddr

    @property
    def localName(self) -> str:
        return self.__localName

    @localName.setter
    def localName(self, localName: str):
        self.__localName = localName

    @property
    def isStartState(self) -> bool:
        return self.__isStartState

    @isStartState.setter
    def isStartState(self, isStartState: bool):
        self.__isStartState = isStartState

    @property
    def requestURL(self) -> str:
        return self.__requestURL

    @requestURL.setter
    def requestURL(self, requestURL: str):
        self.__requestURL = requestURL

    @property
    def port(self) -> int:
        return self.__port

    @port.setter
    def port(self, port: int):
        self.__port = port

    @property
    def cbmg_State6(self):
        return self.__cbmg_State6

    @cbmg_State6.setter
    def cbmg_State6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cbmg_State__cbmg_State6", None)
        self.__cbmg_State6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cbmg_Transition5"):
                opp_val = getattr(old_value, "cbmg_Transition5", None)
                if opp_val == self:
                    setattr(old_value, "cbmg_Transition5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cbmg_Transition5"):
                opp_val = getattr(value, "cbmg_Transition5", None)
                setattr(value, "cbmg_Transition5", self)

    @property
    def cbmg_State9(self):
        return self.__cbmg_State9

    @cbmg_State9.setter
    def cbmg_State9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cbmg_State__cbmg_State9", None)
        self.__cbmg_State9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cbmg_Transition8"):
                opp_val = getattr(old_value, "cbmg_Transition8", None)
                if opp_val == self:
                    setattr(old_value, "cbmg_Transition8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cbmg_Transition8"):
                opp_val = getattr(value, "cbmg_Transition8", None)
                setattr(value, "cbmg_Transition8", self)

    @property
    def cbmg_State2(self):
        return self.__cbmg_State2

    @cbmg_State2.setter
    def cbmg_State2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cbmg_State__cbmg_State2", None)
        self.__cbmg_State2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cbmg_Transition3"):
                    opp_val = getattr(item, "cbmg_Transition3", None)
                    
                    if opp_val == self:
                        setattr(item, "cbmg_Transition3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cbmg_Transition3"):
                    opp_val = getattr(item, "cbmg_Transition3", None)
                    
                    setattr(item, "cbmg_Transition3", self)
                    

    @property
    def cbmg_State(self):
        return self.__cbmg_State

    @cbmg_State.setter
    def cbmg_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cbmg_State__cbmg_State", None)
        self.__cbmg_State = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cbmg_Transition"):
                    opp_val = getattr(item, "cbmg_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "cbmg_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cbmg_Transition"):
                    opp_val = getattr(item, "cbmg_Transition", None)
                    
                    setattr(item, "cbmg_Transition", self)
                    
