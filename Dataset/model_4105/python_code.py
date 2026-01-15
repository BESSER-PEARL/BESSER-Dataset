from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class SignalStateKind(Enum):
    SignalStateKind_STOP = "SignalStateKind_STOP"
    SignalStateKind_FAILURE = "SignalStateKind_FAILURE"
    SignalStateKind_GO = "SignalStateKind_GO"
class SwitchStateKind(Enum):
    PointStateKind_FAILURE = "PointStateKind_FAILURE"
    PointStateKind_LEFT = "PointStateKind_LEFT"
    PointStateKind_RIGHT = "PointStateKind_RIGHT"
    PointStateKind_STRAIGHT = "PointStateKind_STRAIGHT"


############################################
# Definition of Classes
############################################

class Concept_IndividualContainer:

    pass
class Concept_Thing:

    pass
class Thing:

    pass
class Concept_Route(Thing):

    pass
class Concept_Sensor(Thing):

    pass
class Concept_Signal(Thing):

    def __init__(self, Signal_actualState: str, Concept_Signal: "Concept_Route" = None, Concept_Signal9: "Concept_Route" = None):
        self.Signal_actualState = Signal_actualState
        self.Concept_Signal = Concept_Signal
        self.Concept_Signal9 = Concept_Signal9
        
    @property
    def Signal_actualState(self) -> str:
        return self.__Signal_actualState

    @Signal_actualState.setter
    def Signal_actualState(self, Signal_actualState: str):
        self.__Signal_actualState = Signal_actualState

    @property
    def Concept_Signal(self):
        return self.__Concept_Signal

    @Concept_Signal.setter
    def Concept_Signal(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Concept_Signal__Concept_Signal", None)
        self.__Concept_Signal = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Concept_Route"):
                opp_val = getattr(old_value, "Concept_Route", None)
                if opp_val == self:
                    setattr(old_value, "Concept_Route", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Concept_Route"):
                opp_val = getattr(value, "Concept_Route", None)
                setattr(value, "Concept_Route", self)

    @property
    def Concept_Signal9(self):
        return self.__Concept_Signal9

    @Concept_Signal9.setter
    def Concept_Signal9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Concept_Signal__Concept_Signal9", None)
        self.__Concept_Signal9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Concept_Route8"):
                opp_val = getattr(old_value, "Concept_Route8", None)
                if opp_val == self:
                    setattr(old_value, "Concept_Route8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Concept_Route8"):
                opp_val = getattr(value, "Concept_Route8", None)
                setattr(value, "Concept_Route8", self)

class Concept_SwitchPosition(Thing):

    def __init__(self, SwitchPosition_switchState: str, Switch_switchPosition: "Concept_Switch" = None, SwitchPosition: "Concept_Switch" = None, SwitchPosition6: "Concept_Route" = None, Route_switchPosition: "Concept_Route" = None):
        self.SwitchPosition_switchState = SwitchPosition_switchState
        self.Switch_switchPosition = Switch_switchPosition
        self.SwitchPosition = SwitchPosition
        self.SwitchPosition6 = SwitchPosition6
        self.Route_switchPosition = Route_switchPosition
        
    @property
    def SwitchPosition_switchState(self) -> str:
        return self.__SwitchPosition_switchState

    @SwitchPosition_switchState.setter
    def SwitchPosition_switchState(self, SwitchPosition_switchState: str):
        self.__SwitchPosition_switchState = SwitchPosition_switchState

    @property
    def SwitchPosition(self):
        return self.__SwitchPosition

    @SwitchPosition.setter
    def SwitchPosition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Concept_SwitchPosition__SwitchPosition", None)
        self.__SwitchPosition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SwitchPosition_switch"):
                opp_val = getattr(old_value, "SwitchPosition_switch", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SwitchPosition_switch"):
                opp_val = getattr(value, "SwitchPosition_switch", None)
                if opp_val is None:
                    setattr(value, "SwitchPosition_switch", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Route_switchPosition(self):
        return self.__Route_switchPosition

    @Route_switchPosition.setter
    def Route_switchPosition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Concept_SwitchPosition__Route_switchPosition", None)
        self.__Route_switchPosition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Route"):
                opp_val = getattr(old_value, "Route", None)
                if opp_val == self:
                    setattr(old_value, "Route", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Route"):
                opp_val = getattr(value, "Route", None)
                setattr(value, "Route", self)

    @property
    def Switch_switchPosition(self):
        return self.__Switch_switchPosition

    @Switch_switchPosition.setter
    def Switch_switchPosition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Concept_SwitchPosition__Switch_switchPosition", None)
        self.__Switch_switchPosition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Switch"):
                opp_val = getattr(old_value, "Switch", None)
                if opp_val == self:
                    setattr(old_value, "Switch", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Switch"):
                opp_val = getattr(value, "Switch", None)
                setattr(value, "Switch", self)

    @property
    def SwitchPosition6(self):
        return self.__SwitchPosition6

    @SwitchPosition6.setter
    def SwitchPosition6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Concept_SwitchPosition__SwitchPosition6", None)
        self.__SwitchPosition6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SwitchPosition_route"):
                opp_val = getattr(old_value, "SwitchPosition_route", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SwitchPosition_route"):
                opp_val = getattr(value, "SwitchPosition_route", None)
                if opp_val is None:
                    setattr(value, "SwitchPosition_route", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Concept_Trackelement(Thing):

    pass
class Trackelement:

    pass
class Concept_Switch(Trackelement):

    def __init__(self, Switch_actualState: str, Switch: "Concept_SwitchPosition" = None, SwitchPosition_switch: set["Concept_SwitchPosition"] = None):
        self.Switch_actualState = Switch_actualState
        self.Switch = Switch
        self.SwitchPosition_switch = SwitchPosition_switch if SwitchPosition_switch is not None else set()
        
    @property
    def Switch_actualState(self) -> str:
        return self.__Switch_actualState

    @Switch_actualState.setter
    def Switch_actualState(self, Switch_actualState: str):
        self.__Switch_actualState = Switch_actualState

    @property
    def Switch(self):
        return self.__Switch

    @Switch.setter
    def Switch(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Concept_Switch__Switch", None)
        self.__Switch = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Switch_switchPosition"):
                opp_val = getattr(old_value, "Switch_switchPosition", None)
                if opp_val == self:
                    setattr(old_value, "Switch_switchPosition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Switch_switchPosition"):
                opp_val = getattr(value, "Switch_switchPosition", None)
                setattr(value, "Switch_switchPosition", self)

    @property
    def SwitchPosition_switch(self):
        return self.__SwitchPosition_switch

    @SwitchPosition_switch.setter
    def SwitchPosition_switch(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Concept_Switch__SwitchPosition_switch", None)
        self.__SwitchPosition_switch = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SwitchPosition"):
                    opp_val = getattr(item, "SwitchPosition", None)
                    
                    if opp_val == self:
                        setattr(item, "SwitchPosition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SwitchPosition"):
                    opp_val = getattr(item, "SwitchPosition", None)
                    
                    setattr(item, "SwitchPosition", self)
                    

class Concept_Segment(Trackelement):

    def __init__(self, Segment_length: int):
        self.Segment_length = Segment_length
        
    @property
    def Segment_length(self) -> int:
        return self.__Segment_length

    @Segment_length.setter
    def Segment_length(self, Segment_length: int):
        self.__Segment_length = Segment_length
