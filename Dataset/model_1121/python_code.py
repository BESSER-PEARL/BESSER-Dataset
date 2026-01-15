from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class mngr_OpaqueExpression:

    pass
class NamedElement:

    pass
class mngr_ManagedElement(NamedElement):

    def __init__(self, description: str, ManagedElement: "mngr_Manager" = None, managedElement: "mngr_Manager" = None):
        self.description = description
        self.ManagedElement = ManagedElement
        self.managedElement = managedElement
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def ManagedElement(self):
        return self.__ManagedElement

    @ManagedElement.setter
    def ManagedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mngr_ManagedElement__ManagedElement", None)
        self.__ManagedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owningManager8"):
                opp_val = getattr(old_value, "owningManager8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owningManager8"):
                opp_val = getattr(value, "owningManager8", None)
                if opp_val is None:
                    setattr(value, "owningManager8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def managedElement(self):
        return self.__managedElement

    @managedElement.setter
    def managedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mngr_ManagedElement__managedElement", None)
        self.__managedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Manager31"):
                opp_val = getattr(old_value, "Manager31", None)
                if opp_val == self:
                    setattr(old_value, "Manager31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Manager31"):
                opp_val = getattr(value, "Manager31", None)
                setattr(value, "Manager31", self)

class mngr_ManagerParameter(NamedElement):

    def __init__(self, isInput: bool, LitteralInteger: int, LitteralString: str, LitteralBoolean: bool, LitteralUnlimitedNatural: float, ManagerParameter17: "mngr_ManagerState" = None, ManagerParameter: "mngr_Manager" = None, contextParameters: set["mngr_ManagerState"] = None, mngr_ManagerParameter: set["mngr_OpaqueExpression"] = None, contextParameters28: "mngr_Manager" = None):
        self.isInput = isInput
        self.LitteralInteger = LitteralInteger
        self.LitteralString = LitteralString
        self.LitteralBoolean = LitteralBoolean
        self.LitteralUnlimitedNatural = LitteralUnlimitedNatural
        self.ManagerParameter17 = ManagerParameter17
        self.ManagerParameter = ManagerParameter
        self.contextParameters = contextParameters if contextParameters is not None else set()
        self.mngr_ManagerParameter = mngr_ManagerParameter if mngr_ManagerParameter is not None else set()
        self.contextParameters28 = contextParameters28
        
    @property
    def LitteralBoolean(self) -> bool:
        return self.__LitteralBoolean

    @LitteralBoolean.setter
    def LitteralBoolean(self, LitteralBoolean: bool):
        self.__LitteralBoolean = LitteralBoolean

    @property
    def LitteralInteger(self) -> int:
        return self.__LitteralInteger

    @LitteralInteger.setter
    def LitteralInteger(self, LitteralInteger: int):
        self.__LitteralInteger = LitteralInteger

    @property
    def LitteralString(self) -> str:
        return self.__LitteralString

    @LitteralString.setter
    def LitteralString(self, LitteralString: str):
        self.__LitteralString = LitteralString

    @property
    def isInput(self) -> bool:
        return self.__isInput

    @isInput.setter
    def isInput(self, isInput: bool):
        self.__isInput = isInput

    @property
    def LitteralUnlimitedNatural(self) -> float:
        return self.__LitteralUnlimitedNatural

    @LitteralUnlimitedNatural.setter
    def LitteralUnlimitedNatural(self, LitteralUnlimitedNatural: float):
        self.__LitteralUnlimitedNatural = LitteralUnlimitedNatural

    @property
    def ManagerParameter17(self):
        return self.__ManagerParameter17

    @ManagerParameter17.setter
    def ManagerParameter17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mngr_ManagerParameter__ManagerParameter17", None)
        self.__ManagerParameter17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "state"):
                opp_val = getattr(old_value, "state", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "state"):
                opp_val = getattr(value, "state", None)
                if opp_val is None:
                    setattr(value, "state", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mngr_ManagerParameter(self):
        return self.__mngr_ManagerParameter

    @mngr_ManagerParameter.setter
    def mngr_ManagerParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mngr_ManagerParameter__mngr_ManagerParameter", None)
        self.__mngr_ManagerParameter = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mngr_OpaqueExpression"):
                    opp_val = getattr(item, "mngr_OpaqueExpression", None)
                    
                    if opp_val == self:
                        setattr(item, "mngr_OpaqueExpression", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mngr_OpaqueExpression"):
                    opp_val = getattr(item, "mngr_OpaqueExpression", None)
                    
                    setattr(item, "mngr_OpaqueExpression", self)
                    

    @property
    def ManagerParameter(self):
        return self.__ManagerParameter

    @ManagerParameter.setter
    def ManagerParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mngr_ManagerParameter__ManagerParameter", None)
        self.__ManagerParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owningManager6"):
                opp_val = getattr(old_value, "owningManager6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owningManager6"):
                opp_val = getattr(value, "owningManager6", None)
                if opp_val is None:
                    setattr(value, "owningManager6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def contextParameters(self):
        return self.__contextParameters

    @contextParameters.setter
    def contextParameters(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mngr_ManagerParameter__contextParameters", None)
        self.__contextParameters = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ManagerState25"):
                    opp_val = getattr(item, "ManagerState25", None)
                    
                    if opp_val == self:
                        setattr(item, "ManagerState25", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ManagerState25"):
                    opp_val = getattr(item, "ManagerState25", None)
                    
                    setattr(item, "ManagerState25", self)
                    

    @property
    def contextParameters28(self):
        return self.__contextParameters28

    @contextParameters28.setter
    def contextParameters28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mngr_ManagerParameter__contextParameters28", None)
        self.__contextParameters28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Manager29"):
                opp_val = getattr(old_value, "Manager29", None)
                if opp_val == self:
                    setattr(old_value, "Manager29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Manager29"):
                opp_val = getattr(value, "Manager29", None)
                setattr(value, "Manager29", self)

class mngr_ManagerTransition(NamedElement):

    def __init__(self, Event: str, Condition: str, Action: str, input: str, output: str, transProb: float, transRate: float, ManagerTransition13: "mngr_ManagerState" = None, ManagerTransition15: "mngr_ManagerState" = None, ManagerTransition: "mngr_Manager" = None, ownedTransition: "mngr_Manager" = None, outgoingTransition: "mngr_ManagerState" = None, incomingTransition: "mngr_ManagerState" = None):
        self.Event = Event
        self.Condition = Condition
        self.Action = Action
        self.input = input
        self.output = output
        self.transProb = transProb
        self.transRate = transRate
        self.ManagerTransition13 = ManagerTransition13
        self.ManagerTransition15 = ManagerTransition15
        self.ManagerTransition = ManagerTransition
        self.ownedTransition = ownedTransition
        self.outgoingTransition = outgoingTransition
        self.incomingTransition = incomingTransition
        
    @property
    def output(self) -> str:
        return self.__output

    @output.setter
    def output(self, output: str):
        self.__output = output

    @property
    def input(self) -> str:
        return self.__input

    @input.setter
    def input(self, input: str):
        self.__input = input

    @property
    def Event(self) -> str:
        return self.__Event

    @Event.setter
    def Event(self, Event: str):
        self.__Event = Event

    @property
    def Action(self) -> str:
        return self.__Action

    @Action.setter
    def Action(self, Action: str):
        self.__Action = Action

    @property
    def transProb(self) -> float:
        return self.__transProb

    @transProb.setter
    def transProb(self, transProb: float):
        self.__transProb = transProb

    @property
    def transRate(self) -> float:
        return self.__transRate

    @transRate.setter
    def transRate(self, transRate: float):
        self.__transRate = transRate

    @property
    def Condition(self) -> str:
        return self.__Condition

    @Condition.setter
    def Condition(self, Condition: str):
        self.__Condition = Condition

    @property
    def incomingTransition(self):
        return self.__incomingTransition

    @incomingTransition.setter
    def incomingTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mngr_ManagerTransition__incomingTransition", None)
        self.__incomingTransition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ManagerState23"):
                opp_val = getattr(old_value, "ManagerState23", None)
                if opp_val == self:
                    setattr(old_value, "ManagerState23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ManagerState23"):
                opp_val = getattr(value, "ManagerState23", None)
                setattr(value, "ManagerState23", self)

    @property
    def ManagerTransition13(self):
        return self.__ManagerTransition13

    @ManagerTransition13.setter
    def ManagerTransition13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mngr_ManagerTransition__ManagerTransition13", None)
        self.__ManagerTransition13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "source"):
                opp_val = getattr(old_value, "source", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "source"):
                opp_val = getattr(value, "source", None)
                if opp_val is None:
                    setattr(value, "source", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def outgoingTransition(self):
        return self.__outgoingTransition

    @outgoingTransition.setter
    def outgoingTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mngr_ManagerTransition__outgoingTransition", None)
        self.__outgoingTransition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ManagerState21"):
                opp_val = getattr(old_value, "ManagerState21", None)
                if opp_val == self:
                    setattr(old_value, "ManagerState21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ManagerState21"):
                opp_val = getattr(value, "ManagerState21", None)
                setattr(value, "ManagerState21", self)

    @property
    def ownedTransition(self):
        return self.__ownedTransition

    @ownedTransition.setter
    def ownedTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mngr_ManagerTransition__ownedTransition", None)
        self.__ownedTransition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Manager19"):
                opp_val = getattr(old_value, "Manager19", None)
                if opp_val == self:
                    setattr(old_value, "Manager19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Manager19"):
                opp_val = getattr(value, "Manager19", None)
                setattr(value, "Manager19", self)

    @property
    def ManagerTransition15(self):
        return self.__ManagerTransition15

    @ManagerTransition15.setter
    def ManagerTransition15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mngr_ManagerTransition__ManagerTransition15", None)
        self.__ManagerTransition15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "target"):
                opp_val = getattr(old_value, "target", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "target"):
                opp_val = getattr(value, "target", None)
                if opp_val is None:
                    setattr(value, "target", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ManagerTransition(self):
        return self.__ManagerTransition

    @ManagerTransition.setter
    def ManagerTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mngr_ManagerTransition__ManagerTransition", None)
        self.__ManagerTransition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owningManager10"):
                opp_val = getattr(old_value, "owningManager10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owningManager10"):
                opp_val = getattr(value, "owningManager10", None)
                if opp_val is None:
                    setattr(value, "owningManager10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class mngr_ManagerState(NamedElement):

    def __init__(self, isStart: bool, isEnd: bool, Prob: float, ManagerState: "mngr_Manager" = None, mngr_ManagerState: "mngr_Manager" = None, ownedState: "mngr_Manager" = None, source: set["mngr_ManagerTransition"] = None, target: set["mngr_ManagerTransition"] = None, state: set["mngr_ManagerParameter"] = None, mngr_ManagerState4: "mngr_Manager" = None, ManagerState25: "mngr_ManagerParameter" = None, ManagerState21: "mngr_ManagerTransition" = None, ManagerState23: "mngr_ManagerTransition" = None):
        self.isStart = isStart
        self.isEnd = isEnd
        self.Prob = Prob
        self.ManagerState = ManagerState
        self.mngr_ManagerState = mngr_ManagerState
        self.ownedState = ownedState
        self.source = source if source is not None else set()
        self.target = target if target is not None else set()
        self.state = state if state is not None else set()
        self.mngr_ManagerState4 = mngr_ManagerState4
        self.ManagerState25 = ManagerState25
        self.ManagerState21 = ManagerState21
        self.ManagerState23 = ManagerState23
        
    @property
    def Prob(self) -> float:
        return self.__Prob

    @Prob.setter
    def Prob(self, Prob: float):
        self.__Prob = Prob

    @property
    def isStart(self) -> bool:
        return self.__isStart

    @isStart.setter
    def isStart(self, isStart: bool):
        self.__isStart = isStart

    @property
    def isEnd(self) -> bool:
        return self.__isEnd

    @isEnd.setter
    def isEnd(self, isEnd: bool):
        self.__isEnd = isEnd

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mngr_ManagerState__state", None)
        self.__state = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ManagerParameter17"):
                    opp_val = getattr(item, "ManagerParameter17", None)
                    
                    if opp_val == self:
                        setattr(item, "ManagerParameter17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ManagerParameter17"):
                    opp_val = getattr(item, "ManagerParameter17", None)
                    
                    setattr(item, "ManagerParameter17", self)
                    

    @property
    def ownedState(self):
        return self.__ownedState

    @ownedState.setter
    def ownedState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mngr_ManagerState__ownedState", None)
        self.__ownedState = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Manager"):
                opp_val = getattr(old_value, "Manager", None)
                if opp_val == self:
                    setattr(old_value, "Manager", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Manager"):
                opp_val = getattr(value, "Manager", None)
                setattr(value, "Manager", self)

    @property
    def mngr_ManagerState(self):
        return self.__mngr_ManagerState

    @mngr_ManagerState.setter
    def mngr_ManagerState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mngr_ManagerState__mngr_ManagerState", None)
        self.__mngr_ManagerState = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mngr_Manager"):
                opp_val = getattr(old_value, "mngr_Manager", None)
                if opp_val == self:
                    setattr(old_value, "mngr_Manager", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mngr_Manager"):
                opp_val = getattr(value, "mngr_Manager", None)
                setattr(value, "mngr_Manager", self)

    @property
    def ManagerState21(self):
        return self.__ManagerState21

    @ManagerState21.setter
    def ManagerState21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mngr_ManagerState__ManagerState21", None)
        self.__ManagerState21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outgoingTransition"):
                opp_val = getattr(old_value, "outgoingTransition", None)
                if opp_val == self:
                    setattr(old_value, "outgoingTransition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outgoingTransition"):
                opp_val = getattr(value, "outgoingTransition", None)
                setattr(value, "outgoingTransition", self)

    @property
    def ManagerState(self):
        return self.__ManagerState

    @ManagerState.setter
    def ManagerState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mngr_ManagerState__ManagerState", None)
        self.__ManagerState = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owningManager"):
                opp_val = getattr(old_value, "owningManager", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owningManager"):
                opp_val = getattr(value, "owningManager", None)
                if opp_val is None:
                    setattr(value, "owningManager", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ManagerState25(self):
        return self.__ManagerState25

    @ManagerState25.setter
    def ManagerState25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mngr_ManagerState__ManagerState25", None)
        self.__ManagerState25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contextParameters"):
                opp_val = getattr(old_value, "contextParameters", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contextParameters"):
                opp_val = getattr(value, "contextParameters", None)
                if opp_val is None:
                    setattr(value, "contextParameters", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mngr_ManagerState__source", None)
        self.__source = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ManagerTransition13"):
                    opp_val = getattr(item, "ManagerTransition13", None)
                    
                    if opp_val == self:
                        setattr(item, "ManagerTransition13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ManagerTransition13"):
                    opp_val = getattr(item, "ManagerTransition13", None)
                    
                    setattr(item, "ManagerTransition13", self)
                    

    @property
    def mngr_ManagerState4(self):
        return self.__mngr_ManagerState4

    @mngr_ManagerState4.setter
    def mngr_ManagerState4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mngr_ManagerState__mngr_ManagerState4", None)
        self.__mngr_ManagerState4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mngr_Manager3"):
                opp_val = getattr(old_value, "mngr_Manager3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mngr_Manager3"):
                opp_val = getattr(value, "mngr_Manager3", None)
                if opp_val is None:
                    setattr(value, "mngr_Manager3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ManagerState23(self):
        return self.__ManagerState23

    @ManagerState23.setter
    def ManagerState23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mngr_ManagerState__ManagerState23", None)
        self.__ManagerState23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "incomingTransition"):
                opp_val = getattr(old_value, "incomingTransition", None)
                if opp_val == self:
                    setattr(old_value, "incomingTransition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "incomingTransition"):
                opp_val = getattr(value, "incomingTransition", None)
                setattr(value, "incomingTransition", self)

    @property
    def target(self):
        return self.__target

    @target.setter
    def target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mngr_ManagerState__target", None)
        self.__target = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ManagerTransition15"):
                    opp_val = getattr(item, "ManagerTransition15", None)
                    
                    if opp_val == self:
                        setattr(item, "ManagerTransition15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ManagerTransition15"):
                    opp_val = getattr(item, "ManagerTransition15", None)
                    
                    setattr(item, "ManagerTransition15", self)
                    

class mngr_Manager(NamedElement):

    pass