from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class ctxmngr_OpaqueExpression:

    pass
class ctxmngr_ManagerTransition:

    pass
class ctxmngr_Manager:

    pass
class ctxmngr_ManagerState:

    pass
class NamedElement:

    pass
class ctxmngr_CtxTransition(NamedElement):

    def __init__(self, input: str, output: str, transProb: float, Action: str, Event: str, Condition: str, transRate: float, isRemote: bool, ownedTransition: "ctxmngr_ContextManager" = None, outgoingTransition: "ctxmngr_CtxState" = None, incomingTransition: "ctxmngr_CtxState" = None, CtxTransition: "ctxmngr_ContextManager" = None, CtxTransition15: "ctxmngr_CtxState" = None, CtxTransition17: "ctxmngr_CtxState" = None, ctxmngr_CtxTransition44: "ctxmngr_RemoteFiringDependency" = None, ctxmngr_CtxTransition: set["ctxmngr_ManagerTransition"] = None):
        self.input = input
        self.output = output
        self.transProb = transProb
        self.Action = Action
        self.Event = Event
        self.Condition = Condition
        self.transRate = transRate
        self.isRemote = isRemote
        self.ownedTransition = ownedTransition
        self.outgoingTransition = outgoingTransition
        self.incomingTransition = incomingTransition
        self.CtxTransition = CtxTransition
        self.CtxTransition15 = CtxTransition15
        self.CtxTransition17 = CtxTransition17
        self.ctxmngr_CtxTransition44 = ctxmngr_CtxTransition44
        self.ctxmngr_CtxTransition = ctxmngr_CtxTransition if ctxmngr_CtxTransition is not None else set()
        
    @property
    def Condition(self) -> str:
        return self.__Condition

    @Condition.setter
    def Condition(self, Condition: str):
        self.__Condition = Condition

    @property
    def input(self) -> str:
        return self.__input

    @input.setter
    def input(self, input: str):
        self.__input = input

    @property
    def isRemote(self) -> bool:
        return self.__isRemote

    @isRemote.setter
    def isRemote(self, isRemote: bool):
        self.__isRemote = isRemote

    @property
    def transRate(self) -> float:
        return self.__transRate

    @transRate.setter
    def transRate(self, transRate: float):
        self.__transRate = transRate

    @property
    def transProb(self) -> float:
        return self.__transProb

    @transProb.setter
    def transProb(self, transProb: float):
        self.__transProb = transProb

    @property
    def Action(self) -> str:
        return self.__Action

    @Action.setter
    def Action(self, Action: str):
        self.__Action = Action

    @property
    def Event(self) -> str:
        return self.__Event

    @Event.setter
    def Event(self, Event: str):
        self.__Event = Event

    @property
    def output(self) -> str:
        return self.__output

    @output.setter
    def output(self, output: str):
        self.__output = output

    @property
    def incomingTransition(self):
        return self.__incomingTransition

    @incomingTransition.setter
    def incomingTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ctxmngr_CtxTransition__incomingTransition", None)
        self.__incomingTransition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CtxState27"):
                opp_val = getattr(old_value, "CtxState27", None)
                if opp_val == self:
                    setattr(old_value, "CtxState27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CtxState27"):
                opp_val = getattr(value, "CtxState27", None)
                setattr(value, "CtxState27", self)

    @property
    def ownedTransition(self):
        return self.__ownedTransition

    @ownedTransition.setter
    def ownedTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ctxmngr_CtxTransition__ownedTransition", None)
        self.__ownedTransition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ContextManager23"):
                opp_val = getattr(old_value, "ContextManager23", None)
                if opp_val == self:
                    setattr(old_value, "ContextManager23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ContextManager23"):
                opp_val = getattr(value, "ContextManager23", None)
                setattr(value, "ContextManager23", self)

    @property
    def ctxmngr_CtxTransition(self):
        return self.__ctxmngr_CtxTransition

    @ctxmngr_CtxTransition.setter
    def ctxmngr_CtxTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ctxmngr_CtxTransition__ctxmngr_CtxTransition", None)
        self.__ctxmngr_CtxTransition = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ctxmngr_ManagerTransition"):
                    opp_val = getattr(item, "ctxmngr_ManagerTransition", None)
                    
                    if opp_val == self:
                        setattr(item, "ctxmngr_ManagerTransition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ctxmngr_ManagerTransition"):
                    opp_val = getattr(item, "ctxmngr_ManagerTransition", None)
                    
                    setattr(item, "ctxmngr_ManagerTransition", self)
                    

    @property
    def ctxmngr_CtxTransition44(self):
        return self.__ctxmngr_CtxTransition44

    @ctxmngr_CtxTransition44.setter
    def ctxmngr_CtxTransition44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ctxmngr_CtxTransition__ctxmngr_CtxTransition44", None)
        self.__ctxmngr_CtxTransition44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ctxmngr_RemoteFiringDependency43"):
                opp_val = getattr(old_value, "ctxmngr_RemoteFiringDependency43", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ctxmngr_RemoteFiringDependency43"):
                opp_val = getattr(value, "ctxmngr_RemoteFiringDependency43", None)
                if opp_val is None:
                    setattr(value, "ctxmngr_RemoteFiringDependency43", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def outgoingTransition(self):
        return self.__outgoingTransition

    @outgoingTransition.setter
    def outgoingTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ctxmngr_CtxTransition__outgoingTransition", None)
        self.__outgoingTransition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CtxState25"):
                opp_val = getattr(old_value, "CtxState25", None)
                if opp_val == self:
                    setattr(old_value, "CtxState25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CtxState25"):
                opp_val = getattr(value, "CtxState25", None)
                setattr(value, "CtxState25", self)

    @property
    def CtxTransition17(self):
        return self.__CtxTransition17

    @CtxTransition17.setter
    def CtxTransition17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ctxmngr_CtxTransition__CtxTransition17", None)
        self.__CtxTransition17 = value
        
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
    def CtxTransition(self):
        return self.__CtxTransition

    @CtxTransition.setter
    def CtxTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ctxmngr_CtxTransition__CtxTransition", None)
        self.__CtxTransition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owningManager12"):
                opp_val = getattr(old_value, "owningManager12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owningManager12"):
                opp_val = getattr(value, "owningManager12", None)
                if opp_val is None:
                    setattr(value, "owningManager12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CtxTransition15(self):
        return self.__CtxTransition15

    @CtxTransition15.setter
    def CtxTransition15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ctxmngr_CtxTransition__CtxTransition15", None)
        self.__CtxTransition15 = value
        
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

class ctxmngr_ContextParameter(NamedElement):

    def __init__(self, LitteralInteger: int, LitteralString: str, LitteralBoolean: bool, LitteralUnlimitedNatural: float, isInput: bool, ContextParameter19: "ctxmngr_CtxState" = None, ContextParameter: "ctxmngr_ContextManager" = None, contextParameters: set["ctxmngr_CtxState"] = None, ctxmngr_ContextParameter: set["ctxmngr_OpaqueExpression"] = None, contextParameters33: "ctxmngr_ContextManager" = None):
        self.LitteralInteger = LitteralInteger
        self.LitteralString = LitteralString
        self.LitteralBoolean = LitteralBoolean
        self.LitteralUnlimitedNatural = LitteralUnlimitedNatural
        self.isInput = isInput
        self.ContextParameter19 = ContextParameter19
        self.ContextParameter = ContextParameter
        self.contextParameters = contextParameters if contextParameters is not None else set()
        self.ctxmngr_ContextParameter = ctxmngr_ContextParameter if ctxmngr_ContextParameter is not None else set()
        self.contextParameters33 = contextParameters33
        
    @property
    def LitteralString(self) -> str:
        return self.__LitteralString

    @LitteralString.setter
    def LitteralString(self, LitteralString: str):
        self.__LitteralString = LitteralString

    @property
    def LitteralInteger(self) -> int:
        return self.__LitteralInteger

    @LitteralInteger.setter
    def LitteralInteger(self, LitteralInteger: int):
        self.__LitteralInteger = LitteralInteger

    @property
    def isInput(self) -> bool:
        return self.__isInput

    @isInput.setter
    def isInput(self, isInput: bool):
        self.__isInput = isInput

    @property
    def LitteralBoolean(self) -> bool:
        return self.__LitteralBoolean

    @LitteralBoolean.setter
    def LitteralBoolean(self, LitteralBoolean: bool):
        self.__LitteralBoolean = LitteralBoolean

    @property
    def LitteralUnlimitedNatural(self) -> float:
        return self.__LitteralUnlimitedNatural

    @LitteralUnlimitedNatural.setter
    def LitteralUnlimitedNatural(self, LitteralUnlimitedNatural: float):
        self.__LitteralUnlimitedNatural = LitteralUnlimitedNatural

    @property
    def ContextParameter19(self):
        return self.__ContextParameter19

    @ContextParameter19.setter
    def ContextParameter19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ctxmngr_ContextParameter__ContextParameter19", None)
        self.__ContextParameter19 = value
        
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
    def contextParameters(self):
        return self.__contextParameters

    @contextParameters.setter
    def contextParameters(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ctxmngr_ContextParameter__contextParameters", None)
        self.__contextParameters = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CtxState30"):
                    opp_val = getattr(item, "CtxState30", None)
                    
                    if opp_val == self:
                        setattr(item, "CtxState30", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CtxState30"):
                    opp_val = getattr(item, "CtxState30", None)
                    
                    setattr(item, "CtxState30", self)
                    

    @property
    def ctxmngr_ContextParameter(self):
        return self.__ctxmngr_ContextParameter

    @ctxmngr_ContextParameter.setter
    def ctxmngr_ContextParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ctxmngr_ContextParameter__ctxmngr_ContextParameter", None)
        self.__ctxmngr_ContextParameter = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ctxmngr_OpaqueExpression"):
                    opp_val = getattr(item, "ctxmngr_OpaqueExpression", None)
                    
                    if opp_val == self:
                        setattr(item, "ctxmngr_OpaqueExpression", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ctxmngr_OpaqueExpression"):
                    opp_val = getattr(item, "ctxmngr_OpaqueExpression", None)
                    
                    setattr(item, "ctxmngr_OpaqueExpression", self)
                    

    @property
    def contextParameters33(self):
        return self.__contextParameters33

    @contextParameters33.setter
    def contextParameters33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ctxmngr_ContextParameter__contextParameters33", None)
        self.__contextParameters33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ContextManager34"):
                opp_val = getattr(old_value, "ContextManager34", None)
                if opp_val == self:
                    setattr(old_value, "ContextManager34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ContextManager34"):
                opp_val = getattr(value, "ContextManager34", None)
                setattr(value, "ContextManager34", self)

    @property
    def ContextParameter(self):
        return self.__ContextParameter

    @ContextParameter.setter
    def ContextParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ctxmngr_ContextParameter__ContextParameter", None)
        self.__ContextParameter = value
        
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

class ctxmngr_CtxState(NamedElement):

    def __init__(self, isStart: bool, isEnd: bool, CtxState: "ctxmngr_ContextManager" = None, state: set["ctxmngr_ContextParameter"] = None, ctxmngr_CtxState21: set["ctxmngr_ManagerState"] = None, CtxState25: "ctxmngr_CtxTransition" = None, CtxState27: "ctxmngr_CtxTransition" = None, ctxmngr_CtxState: "ctxmngr_ContextManager" = None, ctxmngr_CtxState4: "ctxmngr_ContextManager" = None, ownedState: "ctxmngr_ContextManager" = None, source: set["ctxmngr_CtxTransition"] = None, target: set["ctxmngr_CtxTransition"] = None, CtxState30: "ctxmngr_ContextParameter" = None):
        self.isStart = isStart
        self.isEnd = isEnd
        self.CtxState = CtxState
        self.state = state if state is not None else set()
        self.ctxmngr_CtxState21 = ctxmngr_CtxState21 if ctxmngr_CtxState21 is not None else set()
        self.CtxState25 = CtxState25
        self.CtxState27 = CtxState27
        self.ctxmngr_CtxState = ctxmngr_CtxState
        self.ctxmngr_CtxState4 = ctxmngr_CtxState4
        self.ownedState = ownedState
        self.source = source if source is not None else set()
        self.target = target if target is not None else set()
        self.CtxState30 = CtxState30
        
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
    def ctxmngr_CtxState(self):
        return self.__ctxmngr_CtxState

    @ctxmngr_CtxState.setter
    def ctxmngr_CtxState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ctxmngr_CtxState__ctxmngr_CtxState", None)
        self.__ctxmngr_CtxState = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ctxmngr_ContextManager"):
                opp_val = getattr(old_value, "ctxmngr_ContextManager", None)
                if opp_val == self:
                    setattr(old_value, "ctxmngr_ContextManager", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ctxmngr_ContextManager"):
                opp_val = getattr(value, "ctxmngr_ContextManager", None)
                setattr(value, "ctxmngr_ContextManager", self)

    @property
    def CtxState25(self):
        return self.__CtxState25

    @CtxState25.setter
    def CtxState25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ctxmngr_CtxState__CtxState25", None)
        self.__CtxState25 = value
        
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
    def CtxState27(self):
        return self.__CtxState27

    @CtxState27.setter
    def CtxState27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ctxmngr_CtxState__CtxState27", None)
        self.__CtxState27 = value
        
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
    def CtxState(self):
        return self.__CtxState

    @CtxState.setter
    def CtxState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ctxmngr_CtxState__CtxState", None)
        self.__CtxState = value
        
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
    def ctxmngr_CtxState21(self):
        return self.__ctxmngr_CtxState21

    @ctxmngr_CtxState21.setter
    def ctxmngr_CtxState21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ctxmngr_CtxState__ctxmngr_CtxState21", None)
        self.__ctxmngr_CtxState21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ctxmngr_ManagerState"):
                    opp_val = getattr(item, "ctxmngr_ManagerState", None)
                    
                    if opp_val == self:
                        setattr(item, "ctxmngr_ManagerState", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ctxmngr_ManagerState"):
                    opp_val = getattr(item, "ctxmngr_ManagerState", None)
                    
                    setattr(item, "ctxmngr_ManagerState", self)
                    

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ctxmngr_CtxState__source", None)
        self.__source = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CtxTransition15"):
                    opp_val = getattr(item, "CtxTransition15", None)
                    
                    if opp_val == self:
                        setattr(item, "CtxTransition15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CtxTransition15"):
                    opp_val = getattr(item, "CtxTransition15", None)
                    
                    setattr(item, "CtxTransition15", self)
                    

    @property
    def target(self):
        return self.__target

    @target.setter
    def target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ctxmngr_CtxState__target", None)
        self.__target = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CtxTransition17"):
                    opp_val = getattr(item, "CtxTransition17", None)
                    
                    if opp_val == self:
                        setattr(item, "CtxTransition17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CtxTransition17"):
                    opp_val = getattr(item, "CtxTransition17", None)
                    
                    setattr(item, "CtxTransition17", self)
                    

    @property
    def CtxState30(self):
        return self.__CtxState30

    @CtxState30.setter
    def CtxState30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ctxmngr_CtxState__CtxState30", None)
        self.__CtxState30 = value
        
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
    def state(self):
        return self.__state

    @state.setter
    def state(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ctxmngr_CtxState__state", None)
        self.__state = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ContextParameter19"):
                    opp_val = getattr(item, "ContextParameter19", None)
                    
                    if opp_val == self:
                        setattr(item, "ContextParameter19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ContextParameter19"):
                    opp_val = getattr(item, "ContextParameter19", None)
                    
                    setattr(item, "ContextParameter19", self)
                    

    @property
    def ownedState(self):
        return self.__ownedState

    @ownedState.setter
    def ownedState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ctxmngr_CtxState__ownedState", None)
        self.__ownedState = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ContextManager"):
                opp_val = getattr(old_value, "ContextManager", None)
                if opp_val == self:
                    setattr(old_value, "ContextManager", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ContextManager"):
                opp_val = getattr(value, "ContextManager", None)
                setattr(value, "ContextManager", self)

    @property
    def ctxmngr_CtxState4(self):
        return self.__ctxmngr_CtxState4

    @ctxmngr_CtxState4.setter
    def ctxmngr_CtxState4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ctxmngr_CtxState__ctxmngr_CtxState4", None)
        self.__ctxmngr_CtxState4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ctxmngr_ContextManager3"):
                opp_val = getattr(old_value, "ctxmngr_ContextManager3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ctxmngr_ContextManager3"):
                opp_val = getattr(value, "ctxmngr_ContextManager3", None)
                if opp_val is None:
                    setattr(value, "ctxmngr_ContextManager3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ctxmngr_RemoteFiringDependency(NamedElement):

    pass
class ctxmngr_ContextManager(NamedElement):

    pass