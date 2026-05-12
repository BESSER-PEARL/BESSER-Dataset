from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class statemachine_Transition:

    def __init__(self, label: str, statemachine_Transition4: "statemachine_State" = None, statemachine_Transition7: "statemachine_State" = None, statemachine_Transition: "statemachine_StateMachine" = None):
        self.label = label
        self.statemachine_Transition4 = statemachine_Transition4
        self.statemachine_Transition7 = statemachine_Transition7
        self.statemachine_Transition = statemachine_Transition
        
        pass
    @property
    def label(self):
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label


    @property
    def statemachine_Transition(self):
        return self.__statemachine_Transition

    @statemachine_Transition.setter
    def statemachine_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_Transition__statemachine_Transition", None)
        self.__statemachine_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_StateMachine2"):
                opp_val = getattr(old_value, "statemachine_StateMachine2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_StateMachine2"):
                opp_val = getattr(value, "statemachine_StateMachine2", None)
                if opp_val is None:
                    setattr(value, "statemachine_StateMachine2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def statemachine_Transition7(self):
        return self.__statemachine_Transition7

    @statemachine_Transition7.setter
    def statemachine_Transition7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_Transition__statemachine_Transition7", None)
        self.__statemachine_Transition7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_State8"):
                opp_val = getattr(old_value, "statemachine_State8", None)
                if opp_val == self:
                    setattr(old_value, "statemachine_State8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_State8"):
                opp_val = getattr(value, "statemachine_State8", None)
                setattr(value, "statemachine_State8", self)

    @property
    def statemachine_Transition4(self):
        return self.__statemachine_Transition4

    @statemachine_Transition4.setter
    def statemachine_Transition4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_Transition__statemachine_Transition4", None)
        self.__statemachine_Transition4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_State5"):
                opp_val = getattr(old_value, "statemachine_State5", None)
                if opp_val == self:
                    setattr(old_value, "statemachine_State5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_State5"):
                opp_val = getattr(value, "statemachine_State5", None)
                setattr(value, "statemachine_State5", self)

class statemachine_Set(ABC):

    pass
class statemachine_State:

    def __init__(self, initial: bool, terminal: bool, statemachine_State: "statemachine_StateMachine" = None, statemachine_State5: "statemachine_Transition" = None, statemachine_State8: "statemachine_Transition" = None):
        self.initial = initial
        self.terminal = terminal
        self.statemachine_State = statemachine_State
        self.statemachine_State5 = statemachine_State5
        self.statemachine_State8 = statemachine_State8
        
        pass
    @property
    def initial(self):
        return self.__initial

    @initial.setter
    def initial(self, initial: bool):
        self.__initial = initial


    @property
    def terminal(self):
        return self.__terminal

    @terminal.setter
    def terminal(self, terminal: bool):
        self.__terminal = terminal


    @property
    def statemachine_State(self):
        return self.__statemachine_State

    @statemachine_State.setter
    def statemachine_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_State__statemachine_State", None)
        self.__statemachine_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_StateMachine"):
                opp_val = getattr(old_value, "statemachine_StateMachine", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_StateMachine"):
                opp_val = getattr(value, "statemachine_StateMachine", None)
                if opp_val is None:
                    setattr(value, "statemachine_StateMachine", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def statemachine_State8(self):
        return self.__statemachine_State8

    @statemachine_State8.setter
    def statemachine_State8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_State__statemachine_State8", None)
        self.__statemachine_State8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_Transition7"):
                opp_val = getattr(old_value, "statemachine_Transition7", None)
                if opp_val == self:
                    setattr(old_value, "statemachine_Transition7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_Transition7"):
                opp_val = getattr(value, "statemachine_Transition7", None)
                setattr(value, "statemachine_Transition7", self)

    @property
    def statemachine_State5(self):
        return self.__statemachine_State5

    @statemachine_State5.setter
    def statemachine_State5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_State__statemachine_State5", None)
        self.__statemachine_State5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_Transition4"):
                opp_val = getattr(old_value, "statemachine_Transition4", None)
                if opp_val == self:
                    setattr(old_value, "statemachine_Transition4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_Transition4"):
                opp_val = getattr(value, "statemachine_Transition4", None)
                setattr(value, "statemachine_Transition4", self)

class statemachine_StateMachine:

    def __init__(self, statemachine_StateMachine: set["statemachine_State"] = None, statemachine_StateMachine2: set["statemachine_Transition"] = None):
        self.statemachine_StateMachine = statemachine_StateMachine if statemachine_StateMachine is not None else set()
        self.statemachine_StateMachine2 = statemachine_StateMachine2 if statemachine_StateMachine2 is not None else set()
        
        pass
    @property
    def statemachine_StateMachine(self):
        return self.__statemachine_StateMachine

    @statemachine_StateMachine.setter
    def statemachine_StateMachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_StateMachine__statemachine_StateMachine", None)
        self.__statemachine_StateMachine = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statemachine_State"):
                    opp_val = getattr(item, "statemachine_State", None)
                    
                    if opp_val == self:
                        setattr(item, "statemachine_State", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statemachine_State"):
                    opp_val = getattr(item, "statemachine_State", None)
                    
                    setattr(item, "statemachine_State", self)
                    

    @property
    def statemachine_StateMachine2(self):
        return self.__statemachine_StateMachine2

    @statemachine_StateMachine2.setter
    def statemachine_StateMachine2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_StateMachine__statemachine_StateMachine2", None)
        self.__statemachine_StateMachine2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statemachine_Transition"):
                    opp_val = getattr(item, "statemachine_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "statemachine_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statemachine_Transition"):
                    opp_val = getattr(item, "statemachine_Transition", None)
                    
                    setattr(item, "statemachine_Transition", self)
                    

    def initials(self):
        # TODO: Implement initials method
        pass

    def alphabet(self):
        # TODO: Implement alphabet method
        pass

    def steps(self, statemachine_word, statemachine_st):
        # TODO: Implement steps method
        pass

    def terminals(self):
        # TODO: Implement terminals method
        pass

    def delta(self, statemachine_s):
        # TODO: Implement delta method
        pass

    def accessibleStates(self, statemachine_st):
        # TODO: Implement accessibleStates method
        pass

    def addTransition(self, statemachine_transition):
        # TODO: Implement addTransition method
        pass

    def coAccessibleStates(self):
        # TODO: Implement coAccessibleStates method
        pass

    def addState(self, statemachine_terminal, statemachine_initial) :
        # TODO: Implement addState method
        pass

    def step(self, statemachine_s, statemachine_o):
        # TODO: Implement step method
        pass

    def accept(self, statemachine_word) :
        # TODO: Implement accept method
        pass

    def accessibleAndCoAccessibleStates(self):
        # TODO: Implement accessibleAndCoAccessibleStates method
        pass

    def deltaMinusOne(self, statemachine_st):
        # TODO: Implement deltaMinusOne method
        pass

    def deltaFrom(self, statemachine_from_, statemachine_to):
        # TODO: Implement deltaFrom method
        pass
