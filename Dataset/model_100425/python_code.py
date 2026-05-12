from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Statecharts_Event:

    pass
class BooleanExpression:

    pass
class Statecharts_Guard:

    pass
class CompositeState:

    pass
class Statecharts_StateVertex:

    pass
class Guard:

    pass
class Statecharts_Transition:

    pass
class Event:

    pass
class StateMachine:

    pass
class StateVertex:

    pass
class Statecharts_State(StateVertex):

    pass
class State:

    pass
class Statecharts_CompositeState(State):

    def __init__(self, isConcurrent: str, sv_container: set["StateVertex"] = None, State29: "Statecharts_Event" = None, State10: "Statecharts_Transition" = None, State: "Statecharts_StateMachine" = None):
        self.isConcurrent = isConcurrent
        self.sv_container = sv_container if sv_container is not None else set()
        
        pass
    @property
    def isConcurrent(self):
        return self.__isConcurrent

    @isConcurrent.setter
    def isConcurrent(self, isConcurrent: str):
        self.__isConcurrent = isConcurrent


    @property
    def sv_container(self):
        return self.__sv_container

    @sv_container.setter
    def sv_container(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Statecharts_CompositeState__sv_container", None)
        self.__sv_container = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StateVertex"):
                    opp_val = getattr(item, "StateVertex", None)
                    
                    if opp_val == self:
                        setattr(item, "StateVertex", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StateVertex"):
                    opp_val = getattr(item, "StateVertex", None)
                    
                    setattr(item, "StateVertex", self)
                    

class Transition:

    pass
class Statecharts_StateMachine:

    pass
class Statecharts_BooleanExpression:

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

