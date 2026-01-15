from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class fsm_Transition:

    def __init__(self, name: str, input: str, output: str, fsm_Transition7: "fsm_State" = None, fsm_Transition: "fsm_State" = None):
        self.name = name
        self.input = input
        self.output = output
        self.fsm_Transition7 = fsm_Transition7
        self.fsm_Transition = fsm_Transition
        
    @property
    def input(self) -> str:
        return self.__input

    @input.setter
    def input(self, input: str):
        self.__input = input

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def output(self) -> str:
        return self.__output

    @output.setter
    def output(self, output: str):
        self.__output = output

    @property
    def fsm_Transition(self):
        return self.__fsm_Transition

    @fsm_Transition.setter
    def fsm_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__fsm_Transition", None)
        self.__fsm_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_State5"):
                opp_val = getattr(old_value, "fsm_State5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_State5"):
                opp_val = getattr(value, "fsm_State5", None)
                if opp_val is None:
                    setattr(value, "fsm_State5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fsm_Transition7(self):
        return self.__fsm_Transition7

    @fsm_Transition7.setter
    def fsm_Transition7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__fsm_Transition7", None)
        self.__fsm_Transition7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_State8"):
                opp_val = getattr(old_value, "fsm_State8", None)
                if opp_val == self:
                    setattr(old_value, "fsm_State8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_State8"):
                opp_val = getattr(value, "fsm_State8", None)
                setattr(value, "fsm_State8", self)

    def fire(self):
        # TODO: Implement fire method
        pass

class fsm_State:

    def __init__(self, name: str, isInitialState: bool, fsm_State8: "fsm_Transition" = None, fsm_State: "fsm_FiniteStateMachine" = None, fsm_State3: "fsm_FiniteStateMachine" = None, fsm_State5: set["fsm_Transition"] = None):
        self.name = name
        self.isInitialState = isInitialState
        self.fsm_State8 = fsm_State8
        self.fsm_State = fsm_State
        self.fsm_State3 = fsm_State3
        self.fsm_State5 = fsm_State5 if fsm_State5 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def isInitialState(self) -> bool:
        return self.__isInitialState

    @isInitialState.setter
    def isInitialState(self, isInitialState: bool):
        self.__isInitialState = isInitialState

    @property
    def fsm_State5(self):
        return self.__fsm_State5

    @fsm_State5.setter
    def fsm_State5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__fsm_State5", None)
        self.__fsm_State5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fsm_Transition"):
                    opp_val = getattr(item, "fsm_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "fsm_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fsm_Transition"):
                    opp_val = getattr(item, "fsm_Transition", None)
                    
                    setattr(item, "fsm_Transition", self)
                    

    @property
    def fsm_State(self):
        return self.__fsm_State

    @fsm_State.setter
    def fsm_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__fsm_State", None)
        self.__fsm_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_FiniteStateMachine"):
                opp_val = getattr(old_value, "fsm_FiniteStateMachine", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_FiniteStateMachine"):
                opp_val = getattr(value, "fsm_FiniteStateMachine", None)
                if opp_val is None:
                    setattr(value, "fsm_FiniteStateMachine", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fsm_State8(self):
        return self.__fsm_State8

    @fsm_State8.setter
    def fsm_State8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__fsm_State8", None)
        self.__fsm_State8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_Transition7"):
                opp_val = getattr(old_value, "fsm_Transition7", None)
                if opp_val == self:
                    setattr(old_value, "fsm_Transition7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_Transition7"):
                opp_val = getattr(value, "fsm_Transition7", None)
                setattr(value, "fsm_Transition7", self)

    @property
    def fsm_State3(self):
        return self.__fsm_State3

    @fsm_State3.setter
    def fsm_State3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__fsm_State3", None)
        self.__fsm_State3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_FiniteStateMachine2"):
                opp_val = getattr(old_value, "fsm_FiniteStateMachine2", None)
                if opp_val == self:
                    setattr(old_value, "fsm_FiniteStateMachine2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_FiniteStateMachine2"):
                opp_val = getattr(value, "fsm_FiniteStateMachine2", None)
                setattr(value, "fsm_FiniteStateMachine2", self)

    def step(self, inputString: str):
        # TODO: Implement step method
        pass

class fsm_FiniteStateMachine:

    def __init__(self, name: str, unprocessedString: str, consummedString: str, producedString: str, fsm_FiniteStateMachine: set["fsm_State"] = None, fsm_FiniteStateMachine2: "fsm_State" = None):
        self.name = name
        self.unprocessedString = unprocessedString
        self.consummedString = consummedString
        self.producedString = producedString
        self.fsm_FiniteStateMachine = fsm_FiniteStateMachine if fsm_FiniteStateMachine is not None else set()
        self.fsm_FiniteStateMachine2 = fsm_FiniteStateMachine2
        
    @property
    def producedString(self) -> str:
        return self.__producedString

    @producedString.setter
    def producedString(self, producedString: str):
        self.__producedString = producedString

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def consummedString(self) -> str:
        return self.__consummedString

    @consummedString.setter
    def consummedString(self, consummedString: str):
        self.__consummedString = consummedString

    @property
    def unprocessedString(self) -> str:
        return self.__unprocessedString

    @unprocessedString.setter
    def unprocessedString(self, unprocessedString: str):
        self.__unprocessedString = unprocessedString

    @property
    def fsm_FiniteStateMachine(self):
        return self.__fsm_FiniteStateMachine

    @fsm_FiniteStateMachine.setter
    def fsm_FiniteStateMachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_FiniteStateMachine__fsm_FiniteStateMachine", None)
        self.__fsm_FiniteStateMachine = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fsm_State"):
                    opp_val = getattr(item, "fsm_State", None)
                    
                    if opp_val == self:
                        setattr(item, "fsm_State", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fsm_State"):
                    opp_val = getattr(item, "fsm_State", None)
                    
                    setattr(item, "fsm_State", self)
                    

    @property
    def fsm_FiniteStateMachine2(self):
        return self.__fsm_FiniteStateMachine2

    @fsm_FiniteStateMachine2.setter
    def fsm_FiniteStateMachine2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_FiniteStateMachine__fsm_FiniteStateMachine2", None)
        self.__fsm_FiniteStateMachine2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_State3"):
                opp_val = getattr(old_value, "fsm_State3", None)
                if opp_val == self:
                    setattr(old_value, "fsm_State3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_State3"):
                opp_val = getattr(value, "fsm_State3", None)
                setattr(value, "fsm_State3", self)

    def initializeModel(self, args: str):
        # TODO: Implement initializeModel method
        pass

    def main(self):
        # TODO: Implement main method
        pass
