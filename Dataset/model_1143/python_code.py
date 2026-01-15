from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class myStateMachines_State:

    def __init__(self, name: str, actions: str, myStateMachines_State7: set["myStateMachines_Transition"] = None, myStateMachines_State13: "myStateMachines_Transition" = None, myStateMachines_State: "myStateMachines_Statemachine" = None, myStateMachines_State4: "myStateMachines_Statemachine" = None):
        self.name = name
        self.actions = actions
        self.myStateMachines_State7 = myStateMachines_State7 if myStateMachines_State7 is not None else set()
        self.myStateMachines_State13 = myStateMachines_State13
        self.myStateMachines_State = myStateMachines_State
        self.myStateMachines_State4 = myStateMachines_State4
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def actions(self) -> str:
        return self.__actions

    @actions.setter
    def actions(self, actions: str):
        self.__actions = actions

    @property
    def myStateMachines_State(self):
        return self.__myStateMachines_State

    @myStateMachines_State.setter
    def myStateMachines_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myStateMachines_State__myStateMachines_State", None)
        self.__myStateMachines_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myStateMachines_Statemachine2"):
                opp_val = getattr(old_value, "myStateMachines_Statemachine2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myStateMachines_Statemachine2"):
                opp_val = getattr(value, "myStateMachines_Statemachine2", None)
                if opp_val is None:
                    setattr(value, "myStateMachines_Statemachine2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def myStateMachines_State7(self):
        return self.__myStateMachines_State7

    @myStateMachines_State7.setter
    def myStateMachines_State7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myStateMachines_State__myStateMachines_State7", None)
        self.__myStateMachines_State7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myStateMachines_Transition"):
                    opp_val = getattr(item, "myStateMachines_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "myStateMachines_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myStateMachines_Transition"):
                    opp_val = getattr(item, "myStateMachines_Transition", None)
                    
                    setattr(item, "myStateMachines_Transition", self)
                    

    @property
    def myStateMachines_State13(self):
        return self.__myStateMachines_State13

    @myStateMachines_State13.setter
    def myStateMachines_State13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myStateMachines_State__myStateMachines_State13", None)
        self.__myStateMachines_State13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myStateMachines_Transition12"):
                opp_val = getattr(old_value, "myStateMachines_Transition12", None)
                if opp_val == self:
                    setattr(old_value, "myStateMachines_Transition12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myStateMachines_Transition12"):
                opp_val = getattr(value, "myStateMachines_Transition12", None)
                setattr(value, "myStateMachines_Transition12", self)

    @property
    def myStateMachines_State4(self):
        return self.__myStateMachines_State4

    @myStateMachines_State4.setter
    def myStateMachines_State4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myStateMachines_State__myStateMachines_State4", None)
        self.__myStateMachines_State4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myStateMachines_Statemachine5"):
                opp_val = getattr(old_value, "myStateMachines_Statemachine5", None)
                if opp_val == self:
                    setattr(old_value, "myStateMachines_Statemachine5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myStateMachines_Statemachine5"):
                opp_val = getattr(value, "myStateMachines_Statemachine5", None)
                setattr(value, "myStateMachines_Statemachine5", self)

class myStateMachines_Event:

    def __init__(self, name: str, myStateMachines_Event10: "myStateMachines_Transition" = None, myStateMachines_Event: "myStateMachines_Statemachine" = None):
        self.name = name
        self.myStateMachines_Event10 = myStateMachines_Event10
        self.myStateMachines_Event = myStateMachines_Event
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myStateMachines_Event(self):
        return self.__myStateMachines_Event

    @myStateMachines_Event.setter
    def myStateMachines_Event(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myStateMachines_Event__myStateMachines_Event", None)
        self.__myStateMachines_Event = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myStateMachines_Statemachine"):
                opp_val = getattr(old_value, "myStateMachines_Statemachine", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myStateMachines_Statemachine"):
                opp_val = getattr(value, "myStateMachines_Statemachine", None)
                if opp_val is None:
                    setattr(value, "myStateMachines_Statemachine", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def myStateMachines_Event10(self):
        return self.__myStateMachines_Event10

    @myStateMachines_Event10.setter
    def myStateMachines_Event10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myStateMachines_Event__myStateMachines_Event10", None)
        self.__myStateMachines_Event10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myStateMachines_Transition9"):
                opp_val = getattr(old_value, "myStateMachines_Transition9", None)
                if opp_val == self:
                    setattr(old_value, "myStateMachines_Transition9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myStateMachines_Transition9"):
                opp_val = getattr(value, "myStateMachines_Transition9", None)
                setattr(value, "myStateMachines_Transition9", self)

class myStateMachines_Transition:

    pass
class myStateMachines_Statemachine:

    pass