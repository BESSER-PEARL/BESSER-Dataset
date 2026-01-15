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

class ConceptASE_IndividualContainer:

    pass
class ConceptASE_Thing:

    pass
class Trackelement:

    pass
class ConceptASE_Switch(Trackelement):

    def __init__(self, Switch_actualState: str, SwitchPosition_switch: set["ConceptASE_SwitchPosition"] = None, Switch: "ConceptASE_SwitchPosition" = None):
        self.Switch_actualState = Switch_actualState
        self.SwitchPosition_switch = SwitchPosition_switch if SwitchPosition_switch is not None else set()
        self.Switch = Switch
        
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
        old_value = getattr(self, f"_ConceptASE_Switch__Switch", None)
        self.__Switch = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Switch_switchPosition"):
                opp_val = getattr(old_value, "Switch_switchPosition", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Switch_switchPosition"):
                opp_val = getattr(value, "Switch_switchPosition", None)
                if opp_val is None:
                    setattr(value, "Switch_switchPosition", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def SwitchPosition_switch(self):
        return self.__SwitchPosition_switch

    @SwitchPosition_switch.setter
    def SwitchPosition_switch(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ConceptASE_Switch__SwitchPosition_switch", None)
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
                    

class ConceptASE_Segment(Trackelement):

    def __init__(self, Segment_height: int, Segment_length: int):
        self.Segment_height = Segment_height
        self.Segment_length = Segment_length
        
    @property
    def Segment_length(self) -> int:
        return self.__Segment_length

    @Segment_length.setter
    def Segment_length(self, Segment_length: int):
        self.__Segment_length = Segment_length

    @property
    def Segment_height(self) -> int:
        return self.__Segment_height

    @Segment_height.setter
    def Segment_height(self, Segment_height: int):
        self.__Segment_height = Segment_height

class Thing:

    pass
class ConceptASE_Route(Thing):

    pass
class ConceptASE_Sensor(Thing):

    def __init__(self, Sensor_year: int, Sensor: "ConceptASE_Trackelement" = None, TrackElement_sensor: set["ConceptASE_Trackelement"] = None, ConceptASE_Sensor: "ConceptASE_Route" = None):
        self.Sensor_year = Sensor_year
        self.Sensor = Sensor
        self.TrackElement_sensor = TrackElement_sensor if TrackElement_sensor is not None else set()
        self.ConceptASE_Sensor = ConceptASE_Sensor
        
    @property
    def Sensor_year(self) -> int:
        return self.__Sensor_year

    @Sensor_year.setter
    def Sensor_year(self, Sensor_year: int):
        self.__Sensor_year = Sensor_year

    @property
    def TrackElement_sensor(self):
        return self.__TrackElement_sensor

    @TrackElement_sensor.setter
    def TrackElement_sensor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ConceptASE_Sensor__TrackElement_sensor", None)
        self.__TrackElement_sensor = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Trackelement"):
                    opp_val = getattr(item, "Trackelement", None)
                    
                    if opp_val == self:
                        setattr(item, "Trackelement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Trackelement"):
                    opp_val = getattr(item, "Trackelement", None)
                    
                    setattr(item, "Trackelement", self)
                    

    @property
    def Sensor(self):
        return self.__Sensor

    @Sensor.setter
    def Sensor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ConceptASE_Sensor__Sensor", None)
        self.__Sensor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Sensor_trackElement"):
                opp_val = getattr(old_value, "Sensor_trackElement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Sensor_trackElement"):
                opp_val = getattr(value, "Sensor_trackElement", None)
                if opp_val is None:
                    setattr(value, "Sensor_trackElement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ConceptASE_Sensor(self):
        return self.__ConceptASE_Sensor

    @ConceptASE_Sensor.setter
    def ConceptASE_Sensor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ConceptASE_Sensor__ConceptASE_Sensor", None)
        self.__ConceptASE_Sensor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ConceptASE_Route11"):
                opp_val = getattr(old_value, "ConceptASE_Route11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ConceptASE_Route11"):
                opp_val = getattr(value, "ConceptASE_Route11", None)
                if opp_val is None:
                    setattr(value, "ConceptASE_Route11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ConceptASE_Signal(Thing):

    def __init__(self, Signal_actualState: str, ConceptASE_Signal: "ConceptASE_Route" = None, ConceptASE_Signal9: "ConceptASE_Route" = None):
        self.Signal_actualState = Signal_actualState
        self.ConceptASE_Signal = ConceptASE_Signal
        self.ConceptASE_Signal9 = ConceptASE_Signal9
        
    @property
    def Signal_actualState(self) -> str:
        return self.__Signal_actualState

    @Signal_actualState.setter
    def Signal_actualState(self, Signal_actualState: str):
        self.__Signal_actualState = Signal_actualState

    @property
    def ConceptASE_Signal9(self):
        return self.__ConceptASE_Signal9

    @ConceptASE_Signal9.setter
    def ConceptASE_Signal9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ConceptASE_Signal__ConceptASE_Signal9", None)
        self.__ConceptASE_Signal9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ConceptASE_Route8"):
                opp_val = getattr(old_value, "ConceptASE_Route8", None)
                if opp_val == self:
                    setattr(old_value, "ConceptASE_Route8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ConceptASE_Route8"):
                opp_val = getattr(value, "ConceptASE_Route8", None)
                setattr(value, "ConceptASE_Route8", self)

    @property
    def ConceptASE_Signal(self):
        return self.__ConceptASE_Signal

    @ConceptASE_Signal.setter
    def ConceptASE_Signal(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ConceptASE_Signal__ConceptASE_Signal", None)
        self.__ConceptASE_Signal = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ConceptASE_Route"):
                opp_val = getattr(old_value, "ConceptASE_Route", None)
                if opp_val == self:
                    setattr(old_value, "ConceptASE_Route", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ConceptASE_Route"):
                opp_val = getattr(value, "ConceptASE_Route", None)
                setattr(value, "ConceptASE_Route", self)

class ConceptASE_SwitchPosition(Thing):

    def __init__(self, SwitchPosition_switchState: str, SwitchPosition: "ConceptASE_Switch" = None, SwitchPosition6: "ConceptASE_Route" = None, Switch_switchPosition: set["ConceptASE_Switch"] = None, Route_switchPosition: set["ConceptASE_Route"] = None):
        self.SwitchPosition_switchState = SwitchPosition_switchState
        self.SwitchPosition = SwitchPosition
        self.SwitchPosition6 = SwitchPosition6
        self.Switch_switchPosition = Switch_switchPosition if Switch_switchPosition is not None else set()
        self.Route_switchPosition = Route_switchPosition if Route_switchPosition is not None else set()
        
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
        old_value = getattr(self, f"_ConceptASE_SwitchPosition__SwitchPosition", None)
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
    def Switch_switchPosition(self):
        return self.__Switch_switchPosition

    @Switch_switchPosition.setter
    def Switch_switchPosition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ConceptASE_SwitchPosition__Switch_switchPosition", None)
        self.__Switch_switchPosition = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Switch"):
                    opp_val = getattr(item, "Switch", None)
                    
                    if opp_val == self:
                        setattr(item, "Switch", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Switch"):
                    opp_val = getattr(item, "Switch", None)
                    
                    setattr(item, "Switch", self)
                    

    @property
    def SwitchPosition6(self):
        return self.__SwitchPosition6

    @SwitchPosition6.setter
    def SwitchPosition6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ConceptASE_SwitchPosition__SwitchPosition6", None)
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

    @property
    def Route_switchPosition(self):
        return self.__Route_switchPosition

    @Route_switchPosition.setter
    def Route_switchPosition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ConceptASE_SwitchPosition__Route_switchPosition", None)
        self.__Route_switchPosition = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Route"):
                    opp_val = getattr(item, "Route", None)
                    
                    if opp_val == self:
                        setattr(item, "Route", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Route"):
                    opp_val = getattr(item, "Route", None)
                    
                    setattr(item, "Route", self)
                    

class ConceptASE_Trackelement(Thing):

    pass