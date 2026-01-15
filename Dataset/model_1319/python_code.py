from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class FiniteStateMachines_State:

    def __init__(self, isEndState: bool, isStartState: bool, name: str, startState: set["FiniteStateMachines_Transition"] = None, State: "FiniteStateMachines_Transition" = None, FiniteStateMachines_State7: "FiniteStateMachines_Transition" = None, FiniteStateMachines_State: "FiniteStateMachines_FiniteStateMachine" = None):
        self.isEndState = isEndState
        self.isStartState = isStartState
        self.name = name
        self.startState = startState if startState is not None else set()
        self.State = State
        self.FiniteStateMachines_State7 = FiniteStateMachines_State7
        self.FiniteStateMachines_State = FiniteStateMachines_State
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def isEndState(self) -> bool:
        return self.__isEndState

    @isEndState.setter
    def isEndState(self, isEndState: bool):
        self.__isEndState = isEndState

    @property
    def isStartState(self) -> bool:
        return self.__isStartState

    @isStartState.setter
    def isStartState(self, isStartState: bool):
        self.__isStartState = isStartState

    @property
    def State(self):
        return self.__State

    @State.setter
    def State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FiniteStateMachines_State__State", None)
        self.__State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "transitions"):
                opp_val = getattr(old_value, "transitions", None)
                if opp_val == self:
                    setattr(old_value, "transitions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "transitions"):
                opp_val = getattr(value, "transitions", None)
                setattr(value, "transitions", self)

    @property
    def FiniteStateMachines_State7(self):
        return self.__FiniteStateMachines_State7

    @FiniteStateMachines_State7.setter
    def FiniteStateMachines_State7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FiniteStateMachines_State__FiniteStateMachines_State7", None)
        self.__FiniteStateMachines_State7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FiniteStateMachines_Transition6"):
                opp_val = getattr(old_value, "FiniteStateMachines_Transition6", None)
                if opp_val == self:
                    setattr(old_value, "FiniteStateMachines_Transition6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FiniteStateMachines_Transition6"):
                opp_val = getattr(value, "FiniteStateMachines_Transition6", None)
                setattr(value, "FiniteStateMachines_Transition6", self)

    @property
    def FiniteStateMachines_State(self):
        return self.__FiniteStateMachines_State

    @FiniteStateMachines_State.setter
    def FiniteStateMachines_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FiniteStateMachines_State__FiniteStateMachines_State", None)
        self.__FiniteStateMachines_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FiniteStateMachines_FiniteStateMachine"):
                opp_val = getattr(old_value, "FiniteStateMachines_FiniteStateMachine", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FiniteStateMachines_FiniteStateMachine"):
                opp_val = getattr(value, "FiniteStateMachines_FiniteStateMachine", None)
                if opp_val is None:
                    setattr(value, "FiniteStateMachines_FiniteStateMachine", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def startState(self):
        return self.__startState

    @startState.setter
    def startState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FiniteStateMachines_State__startState", None)
        self.__startState = value if value is not None else set()
        
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
                    

class FiniteStateMachines_FiniteStateMachine:

    def __init__(self, id: str, FiniteStateMachines_FiniteStateMachine2: set["FiniteStateMachines_Transition"] = None, FiniteStateMachines_FiniteStateMachine: set["FiniteStateMachines_State"] = None):
        self.id = id
        self.FiniteStateMachines_FiniteStateMachine2 = FiniteStateMachines_FiniteStateMachine2 if FiniteStateMachines_FiniteStateMachine2 is not None else set()
        self.FiniteStateMachines_FiniteStateMachine = FiniteStateMachines_FiniteStateMachine if FiniteStateMachines_FiniteStateMachine is not None else set()
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def FiniteStateMachines_FiniteStateMachine(self):
        return self.__FiniteStateMachines_FiniteStateMachine

    @FiniteStateMachines_FiniteStateMachine.setter
    def FiniteStateMachines_FiniteStateMachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FiniteStateMachines_FiniteStateMachine__FiniteStateMachines_FiniteStateMachine", None)
        self.__FiniteStateMachines_FiniteStateMachine = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "FiniteStateMachines_State"):
                    opp_val = getattr(item, "FiniteStateMachines_State", None)
                    
                    if opp_val == self:
                        setattr(item, "FiniteStateMachines_State", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FiniteStateMachines_State"):
                    opp_val = getattr(item, "FiniteStateMachines_State", None)
                    
                    setattr(item, "FiniteStateMachines_State", self)
                    

    @property
    def FiniteStateMachines_FiniteStateMachine2(self):
        return self.__FiniteStateMachines_FiniteStateMachine2

    @FiniteStateMachines_FiniteStateMachine2.setter
    def FiniteStateMachines_FiniteStateMachine2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FiniteStateMachines_FiniteStateMachine__FiniteStateMachines_FiniteStateMachine2", None)
        self.__FiniteStateMachines_FiniteStateMachine2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "FiniteStateMachines_Transition"):
                    opp_val = getattr(item, "FiniteStateMachines_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "FiniteStateMachines_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FiniteStateMachines_Transition"):
                    opp_val = getattr(item, "FiniteStateMachines_Transition", None)
                    
                    setattr(item, "FiniteStateMachines_Transition", self)
                    

class FiniteStateMachines_Transition:

    def __init__(self, input: str, FiniteStateMachines_Transition: "FiniteStateMachines_FiniteStateMachine" = None, Transition: "FiniteStateMachines_State" = None, transitions: "FiniteStateMachines_State" = None, FiniteStateMachines_Transition6: "FiniteStateMachines_State" = None):
        self.input = input
        self.FiniteStateMachines_Transition = FiniteStateMachines_Transition
        self.Transition = Transition
        self.transitions = transitions
        self.FiniteStateMachines_Transition6 = FiniteStateMachines_Transition6
        
    @property
    def input(self) -> str:
        return self.__input

    @input.setter
    def input(self, input: str):
        self.__input = input

    @property
    def Transition(self):
        return self.__Transition

    @Transition.setter
    def Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FiniteStateMachines_Transition__Transition", None)
        self.__Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "startState"):
                opp_val = getattr(old_value, "startState", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "startState"):
                opp_val = getattr(value, "startState", None)
                if opp_val is None:
                    setattr(value, "startState", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def transitions(self):
        return self.__transitions

    @transitions.setter
    def transitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FiniteStateMachines_Transition__transitions", None)
        self.__transitions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State"):
                opp_val = getattr(old_value, "State", None)
                if opp_val == self:
                    setattr(old_value, "State", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State"):
                opp_val = getattr(value, "State", None)
                setattr(value, "State", self)

    @property
    def FiniteStateMachines_Transition6(self):
        return self.__FiniteStateMachines_Transition6

    @FiniteStateMachines_Transition6.setter
    def FiniteStateMachines_Transition6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FiniteStateMachines_Transition__FiniteStateMachines_Transition6", None)
        self.__FiniteStateMachines_Transition6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FiniteStateMachines_State7"):
                opp_val = getattr(old_value, "FiniteStateMachines_State7", None)
                if opp_val == self:
                    setattr(old_value, "FiniteStateMachines_State7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FiniteStateMachines_State7"):
                opp_val = getattr(value, "FiniteStateMachines_State7", None)
                setattr(value, "FiniteStateMachines_State7", self)

    @property
    def FiniteStateMachines_Transition(self):
        return self.__FiniteStateMachines_Transition

    @FiniteStateMachines_Transition.setter
    def FiniteStateMachines_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FiniteStateMachines_Transition__FiniteStateMachines_Transition", None)
        self.__FiniteStateMachines_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FiniteStateMachines_FiniteStateMachine2"):
                opp_val = getattr(old_value, "FiniteStateMachines_FiniteStateMachine2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FiniteStateMachines_FiniteStateMachine2"):
                opp_val = getattr(value, "FiniteStateMachines_FiniteStateMachine2", None)
                if opp_val is None:
                    setattr(value, "FiniteStateMachines_FiniteStateMachine2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
