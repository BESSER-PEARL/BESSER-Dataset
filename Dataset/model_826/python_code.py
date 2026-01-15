from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class wheel_Transition:

    def __init__(self, speed: str, time: str, wheel_Transition: "wheel_State" = None, Transition: "wheel_State" = None, wheel_Transition10: "wheel_State" = None, outgoingTransition: "wheel_State" = None):
        self.speed = speed
        self.time = time
        self.wheel_Transition = wheel_Transition
        self.Transition = Transition
        self.wheel_Transition10 = wheel_Transition10
        self.outgoingTransition = outgoingTransition
        
    @property
    def speed(self) -> str:
        return self.__speed

    @speed.setter
    def speed(self, speed: str):
        self.__speed = speed

    @property
    def time(self) -> str:
        return self.__time

    @time.setter
    def time(self, time: str):
        self.__time = time

    @property
    def wheel_Transition10(self):
        return self.__wheel_Transition10

    @wheel_Transition10.setter
    def wheel_Transition10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wheel_Transition__wheel_Transition10", None)
        self.__wheel_Transition10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wheel_State11"):
                opp_val = getattr(old_value, "wheel_State11", None)
                if opp_val == self:
                    setattr(old_value, "wheel_State11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wheel_State11"):
                opp_val = getattr(value, "wheel_State11", None)
                setattr(value, "wheel_State11", self)

    @property
    def wheel_Transition(self):
        return self.__wheel_Transition

    @wheel_Transition.setter
    def wheel_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wheel_Transition__wheel_Transition", None)
        self.__wheel_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wheel_State6"):
                opp_val = getattr(old_value, "wheel_State6", None)
                if opp_val == self:
                    setattr(old_value, "wheel_State6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wheel_State6"):
                opp_val = getattr(value, "wheel_State6", None)
                setattr(value, "wheel_State6", self)

    @property
    def outgoingTransition(self):
        return self.__outgoingTransition

    @outgoingTransition.setter
    def outgoingTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wheel_Transition__outgoingTransition", None)
        self.__outgoingTransition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State13"):
                opp_val = getattr(old_value, "State13", None)
                if opp_val == self:
                    setattr(old_value, "State13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State13"):
                opp_val = getattr(value, "State13", None)
                setattr(value, "State13", self)

    @property
    def Transition(self):
        return self.__Transition

    @Transition.setter
    def Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wheel_Transition__Transition", None)
        self.__Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Source"):
                opp_val = getattr(old_value, "Source", None)
                if opp_val == self:
                    setattr(old_value, "Source", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Source"):
                opp_val = getattr(value, "Source", None)
                setattr(value, "Source", self)

class wheel_State:

    def __init__(self, name: str, ownedState: "wheel_WheelSM" = None, wheel_State: "wheel_WheelSM" = None, wheel_State3: "wheel_WheelSM" = None, State: "wheel_WheelSM" = None, wheel_State6: "wheel_Transition" = None, Source: "wheel_Transition" = None, wheel_State11: "wheel_Transition" = None, State13: "wheel_Transition" = None):
        self.name = name
        self.ownedState = ownedState
        self.wheel_State = wheel_State
        self.wheel_State3 = wheel_State3
        self.State = State
        self.wheel_State6 = wheel_State6
        self.Source = Source
        self.wheel_State11 = wheel_State11
        self.State13 = State13
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def wheel_State11(self):
        return self.__wheel_State11

    @wheel_State11.setter
    def wheel_State11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wheel_State__wheel_State11", None)
        self.__wheel_State11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wheel_Transition10"):
                opp_val = getattr(old_value, "wheel_Transition10", None)
                if opp_val == self:
                    setattr(old_value, "wheel_Transition10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wheel_Transition10"):
                opp_val = getattr(value, "wheel_Transition10", None)
                setattr(value, "wheel_Transition10", self)

    @property
    def Source(self):
        return self.__Source

    @Source.setter
    def Source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wheel_State__Source", None)
        self.__Source = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Transition"):
                opp_val = getattr(old_value, "Transition", None)
                if opp_val == self:
                    setattr(old_value, "Transition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Transition"):
                opp_val = getattr(value, "Transition", None)
                setattr(value, "Transition", self)

    @property
    def wheel_State3(self):
        return self.__wheel_State3

    @wheel_State3.setter
    def wheel_State3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wheel_State__wheel_State3", None)
        self.__wheel_State3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wheel_WheelSM2"):
                opp_val = getattr(old_value, "wheel_WheelSM2", None)
                if opp_val == self:
                    setattr(old_value, "wheel_WheelSM2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wheel_WheelSM2"):
                opp_val = getattr(value, "wheel_WheelSM2", None)
                setattr(value, "wheel_WheelSM2", self)

    @property
    def wheel_State(self):
        return self.__wheel_State

    @wheel_State.setter
    def wheel_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wheel_State__wheel_State", None)
        self.__wheel_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wheel_WheelSM"):
                opp_val = getattr(old_value, "wheel_WheelSM", None)
                if opp_val == self:
                    setattr(old_value, "wheel_WheelSM", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wheel_WheelSM"):
                opp_val = getattr(value, "wheel_WheelSM", None)
                setattr(value, "wheel_WheelSM", self)

    @property
    def State(self):
        return self.__State

    @State.setter
    def State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wheel_State__State", None)
        self.__State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owningFSM"):
                opp_val = getattr(old_value, "owningFSM", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owningFSM"):
                opp_val = getattr(value, "owningFSM", None)
                if opp_val is None:
                    setattr(value, "owningFSM", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def State13(self):
        return self.__State13

    @State13.setter
    def State13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wheel_State__State13", None)
        self.__State13 = value
        
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
    def wheel_State6(self):
        return self.__wheel_State6

    @wheel_State6.setter
    def wheel_State6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wheel_State__wheel_State6", None)
        self.__wheel_State6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wheel_Transition"):
                opp_val = getattr(old_value, "wheel_Transition", None)
                if opp_val == self:
                    setattr(old_value, "wheel_Transition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wheel_Transition"):
                opp_val = getattr(value, "wheel_Transition", None)
                setattr(value, "wheel_Transition", self)

    @property
    def ownedState(self):
        return self.__ownedState

    @ownedState.setter
    def ownedState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wheel_State__ownedState", None)
        self.__ownedState = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "WheelSM"):
                opp_val = getattr(old_value, "WheelSM", None)
                if opp_val == self:
                    setattr(old_value, "WheelSM", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "WheelSM"):
                opp_val = getattr(value, "WheelSM", None)
                setattr(value, "WheelSM", self)

class wheel_WheelSM:

    pass