from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class raspduinoDSL_ChangeActuator:

    def __init__(self, ActuatorState: str, raspduinoDSL_ChangeActuator: "raspduinoDSL_EventHandler" = None, raspduinoDSL_ChangeActuator10: "raspduinoDSL_Actuator" = None):
        self.ActuatorState = ActuatorState
        self.raspduinoDSL_ChangeActuator = raspduinoDSL_ChangeActuator
        self.raspduinoDSL_ChangeActuator10 = raspduinoDSL_ChangeActuator10
        
    @property
    def ActuatorState(self) -> str:
        return self.__ActuatorState

    @ActuatorState.setter
    def ActuatorState(self, ActuatorState: str):
        self.__ActuatorState = ActuatorState

    @property
    def raspduinoDSL_ChangeActuator(self):
        return self.__raspduinoDSL_ChangeActuator

    @raspduinoDSL_ChangeActuator.setter
    def raspduinoDSL_ChangeActuator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspduinoDSL_ChangeActuator__raspduinoDSL_ChangeActuator", None)
        self.__raspduinoDSL_ChangeActuator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "raspduinoDSL_EventHandler8"):
                opp_val = getattr(old_value, "raspduinoDSL_EventHandler8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "raspduinoDSL_EventHandler8"):
                opp_val = getattr(value, "raspduinoDSL_EventHandler8", None)
                if opp_val is None:
                    setattr(value, "raspduinoDSL_EventHandler8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def raspduinoDSL_ChangeActuator10(self):
        return self.__raspduinoDSL_ChangeActuator10

    @raspduinoDSL_ChangeActuator10.setter
    def raspduinoDSL_ChangeActuator10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspduinoDSL_ChangeActuator__raspduinoDSL_ChangeActuator10", None)
        self.__raspduinoDSL_ChangeActuator10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "raspduinoDSL_Actuator"):
                opp_val = getattr(old_value, "raspduinoDSL_Actuator", None)
                if opp_val == self:
                    setattr(old_value, "raspduinoDSL_Actuator", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "raspduinoDSL_Actuator"):
                opp_val = getattr(value, "raspduinoDSL_Actuator", None)
                setattr(value, "raspduinoDSL_Actuator", self)

class AbstractDevice:

    pass
class raspduinoDSL_Actuator(AbstractDevice):

    pass
class raspduinoDSL_Sensor(AbstractDevice):

    pass
class raspduinoDSL_Timer:

    def __init__(self, repeattype: str, secs: int, hours: int, minutes: int, raspduinoDSL_Timer: "raspduinoDSL_Model" = None, raspduinoDSL_Timer17: "raspduinoDSL_EventHandler" = None):
        self.repeattype = repeattype
        self.secs = secs
        self.hours = hours
        self.minutes = minutes
        self.raspduinoDSL_Timer = raspduinoDSL_Timer
        self.raspduinoDSL_Timer17 = raspduinoDSL_Timer17
        
    @property
    def secs(self) -> int:
        return self.__secs

    @secs.setter
    def secs(self, secs: int):
        self.__secs = secs

    @property
    def minutes(self) -> int:
        return self.__minutes

    @minutes.setter
    def minutes(self, minutes: int):
        self.__minutes = minutes

    @property
    def hours(self) -> int:
        return self.__hours

    @hours.setter
    def hours(self, hours: int):
        self.__hours = hours

    @property
    def repeattype(self) -> str:
        return self.__repeattype

    @repeattype.setter
    def repeattype(self, repeattype: str):
        self.__repeattype = repeattype

    @property
    def raspduinoDSL_Timer17(self):
        return self.__raspduinoDSL_Timer17

    @raspduinoDSL_Timer17.setter
    def raspduinoDSL_Timer17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspduinoDSL_Timer__raspduinoDSL_Timer17", None)
        self.__raspduinoDSL_Timer17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "raspduinoDSL_EventHandler18"):
                opp_val = getattr(old_value, "raspduinoDSL_EventHandler18", None)
                if opp_val == self:
                    setattr(old_value, "raspduinoDSL_EventHandler18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "raspduinoDSL_EventHandler18"):
                opp_val = getattr(value, "raspduinoDSL_EventHandler18", None)
                setattr(value, "raspduinoDSL_EventHandler18", self)

    @property
    def raspduinoDSL_Timer(self):
        return self.__raspduinoDSL_Timer

    @raspduinoDSL_Timer.setter
    def raspduinoDSL_Timer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspduinoDSL_Timer__raspduinoDSL_Timer", None)
        self.__raspduinoDSL_Timer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "raspduinoDSL_Model6"):
                opp_val = getattr(old_value, "raspduinoDSL_Model6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "raspduinoDSL_Model6"):
                opp_val = getattr(value, "raspduinoDSL_Model6", None)
                if opp_val is None:
                    setattr(value, "raspduinoDSL_Model6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class raspduinoDSL_SensorListener:

    def __init__(self, type: str, l: int, h: int, raspduinoDSL_SensorListener: "raspduinoDSL_Model" = None, raspduinoDSL_SensorListener12: "raspduinoDSL_Sensor" = None, raspduinoDSL_SensorListener14: "raspduinoDSL_EventHandler" = None):
        self.type = type
        self.l = l
        self.h = h
        self.raspduinoDSL_SensorListener = raspduinoDSL_SensorListener
        self.raspduinoDSL_SensorListener12 = raspduinoDSL_SensorListener12
        self.raspduinoDSL_SensorListener14 = raspduinoDSL_SensorListener14
        
    @property
    def l(self) -> int:
        return self.__l

    @l.setter
    def l(self, l: int):
        self.__l = l

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def h(self) -> int:
        return self.__h

    @h.setter
    def h(self, h: int):
        self.__h = h

    @property
    def raspduinoDSL_SensorListener12(self):
        return self.__raspduinoDSL_SensorListener12

    @raspduinoDSL_SensorListener12.setter
    def raspduinoDSL_SensorListener12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspduinoDSL_SensorListener__raspduinoDSL_SensorListener12", None)
        self.__raspduinoDSL_SensorListener12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "raspduinoDSL_Sensor"):
                opp_val = getattr(old_value, "raspduinoDSL_Sensor", None)
                if opp_val == self:
                    setattr(old_value, "raspduinoDSL_Sensor", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "raspduinoDSL_Sensor"):
                opp_val = getattr(value, "raspduinoDSL_Sensor", None)
                setattr(value, "raspduinoDSL_Sensor", self)

    @property
    def raspduinoDSL_SensorListener14(self):
        return self.__raspduinoDSL_SensorListener14

    @raspduinoDSL_SensorListener14.setter
    def raspduinoDSL_SensorListener14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspduinoDSL_SensorListener__raspduinoDSL_SensorListener14", None)
        self.__raspduinoDSL_SensorListener14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "raspduinoDSL_EventHandler15"):
                opp_val = getattr(old_value, "raspduinoDSL_EventHandler15", None)
                if opp_val == self:
                    setattr(old_value, "raspduinoDSL_EventHandler15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "raspduinoDSL_EventHandler15"):
                opp_val = getattr(value, "raspduinoDSL_EventHandler15", None)
                setattr(value, "raspduinoDSL_EventHandler15", self)

    @property
    def raspduinoDSL_SensorListener(self):
        return self.__raspduinoDSL_SensorListener

    @raspduinoDSL_SensorListener.setter
    def raspduinoDSL_SensorListener(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspduinoDSL_SensorListener__raspduinoDSL_SensorListener", None)
        self.__raspduinoDSL_SensorListener = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "raspduinoDSL_Model4"):
                opp_val = getattr(old_value, "raspduinoDSL_Model4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "raspduinoDSL_Model4"):
                opp_val = getattr(value, "raspduinoDSL_Model4", None)
                if opp_val is None:
                    setattr(value, "raspduinoDSL_Model4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class raspduinoDSL_EventHandler:

    def __init__(self, name: str, raspduinoDSL_EventHandler: "raspduinoDSL_Model" = None, raspduinoDSL_EventHandler8: set["raspduinoDSL_ChangeActuator"] = None, raspduinoDSL_EventHandler18: "raspduinoDSL_Timer" = None, raspduinoDSL_EventHandler15: "raspduinoDSL_SensorListener" = None):
        self.name = name
        self.raspduinoDSL_EventHandler = raspduinoDSL_EventHandler
        self.raspduinoDSL_EventHandler8 = raspduinoDSL_EventHandler8 if raspduinoDSL_EventHandler8 is not None else set()
        self.raspduinoDSL_EventHandler18 = raspduinoDSL_EventHandler18
        self.raspduinoDSL_EventHandler15 = raspduinoDSL_EventHandler15
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def raspduinoDSL_EventHandler18(self):
        return self.__raspduinoDSL_EventHandler18

    @raspduinoDSL_EventHandler18.setter
    def raspduinoDSL_EventHandler18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspduinoDSL_EventHandler__raspduinoDSL_EventHandler18", None)
        self.__raspduinoDSL_EventHandler18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "raspduinoDSL_Timer17"):
                opp_val = getattr(old_value, "raspduinoDSL_Timer17", None)
                if opp_val == self:
                    setattr(old_value, "raspduinoDSL_Timer17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "raspduinoDSL_Timer17"):
                opp_val = getattr(value, "raspduinoDSL_Timer17", None)
                setattr(value, "raspduinoDSL_Timer17", self)

    @property
    def raspduinoDSL_EventHandler(self):
        return self.__raspduinoDSL_EventHandler

    @raspduinoDSL_EventHandler.setter
    def raspduinoDSL_EventHandler(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspduinoDSL_EventHandler__raspduinoDSL_EventHandler", None)
        self.__raspduinoDSL_EventHandler = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "raspduinoDSL_Model2"):
                opp_val = getattr(old_value, "raspduinoDSL_Model2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "raspduinoDSL_Model2"):
                opp_val = getattr(value, "raspduinoDSL_Model2", None)
                if opp_val is None:
                    setattr(value, "raspduinoDSL_Model2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def raspduinoDSL_EventHandler8(self):
        return self.__raspduinoDSL_EventHandler8

    @raspduinoDSL_EventHandler8.setter
    def raspduinoDSL_EventHandler8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspduinoDSL_EventHandler__raspduinoDSL_EventHandler8", None)
        self.__raspduinoDSL_EventHandler8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "raspduinoDSL_ChangeActuator"):
                    opp_val = getattr(item, "raspduinoDSL_ChangeActuator", None)
                    
                    if opp_val == self:
                        setattr(item, "raspduinoDSL_ChangeActuator", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "raspduinoDSL_ChangeActuator"):
                    opp_val = getattr(item, "raspduinoDSL_ChangeActuator", None)
                    
                    setattr(item, "raspduinoDSL_ChangeActuator", self)
                    

    @property
    def raspduinoDSL_EventHandler15(self):
        return self.__raspduinoDSL_EventHandler15

    @raspduinoDSL_EventHandler15.setter
    def raspduinoDSL_EventHandler15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspduinoDSL_EventHandler__raspduinoDSL_EventHandler15", None)
        self.__raspduinoDSL_EventHandler15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "raspduinoDSL_SensorListener14"):
                opp_val = getattr(old_value, "raspduinoDSL_SensorListener14", None)
                if opp_val == self:
                    setattr(old_value, "raspduinoDSL_SensorListener14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "raspduinoDSL_SensorListener14"):
                opp_val = getattr(value, "raspduinoDSL_SensorListener14", None)
                setattr(value, "raspduinoDSL_SensorListener14", self)

class raspduinoDSL_AbstractDevice:

    def __init__(self, name: str, pin: str, raspduinoDSL_AbstractDevice: "raspduinoDSL_Model" = None):
        self.name = name
        self.pin = pin
        self.raspduinoDSL_AbstractDevice = raspduinoDSL_AbstractDevice
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def pin(self) -> str:
        return self.__pin

    @pin.setter
    def pin(self, pin: str):
        self.__pin = pin

    @property
    def raspduinoDSL_AbstractDevice(self):
        return self.__raspduinoDSL_AbstractDevice

    @raspduinoDSL_AbstractDevice.setter
    def raspduinoDSL_AbstractDevice(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspduinoDSL_AbstractDevice__raspduinoDSL_AbstractDevice", None)
        self.__raspduinoDSL_AbstractDevice = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "raspduinoDSL_Model"):
                opp_val = getattr(old_value, "raspduinoDSL_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "raspduinoDSL_Model"):
                opp_val = getattr(value, "raspduinoDSL_Model", None)
                if opp_val is None:
                    setattr(value, "raspduinoDSL_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class raspduinoDSL_Model:

    def __init__(self, name: str, hardware: str, raspduinoDSL_Model: set["raspduinoDSL_AbstractDevice"] = None, raspduinoDSL_Model2: set["raspduinoDSL_EventHandler"] = None, raspduinoDSL_Model4: set["raspduinoDSL_SensorListener"] = None, raspduinoDSL_Model6: set["raspduinoDSL_Timer"] = None):
        self.name = name
        self.hardware = hardware
        self.raspduinoDSL_Model = raspduinoDSL_Model if raspduinoDSL_Model is not None else set()
        self.raspduinoDSL_Model2 = raspduinoDSL_Model2 if raspduinoDSL_Model2 is not None else set()
        self.raspduinoDSL_Model4 = raspduinoDSL_Model4 if raspduinoDSL_Model4 is not None else set()
        self.raspduinoDSL_Model6 = raspduinoDSL_Model6 if raspduinoDSL_Model6 is not None else set()
        
    @property
    def hardware(self) -> str:
        return self.__hardware

    @hardware.setter
    def hardware(self, hardware: str):
        self.__hardware = hardware

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def raspduinoDSL_Model2(self):
        return self.__raspduinoDSL_Model2

    @raspduinoDSL_Model2.setter
    def raspduinoDSL_Model2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspduinoDSL_Model__raspduinoDSL_Model2", None)
        self.__raspduinoDSL_Model2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "raspduinoDSL_EventHandler"):
                    opp_val = getattr(item, "raspduinoDSL_EventHandler", None)
                    
                    if opp_val == self:
                        setattr(item, "raspduinoDSL_EventHandler", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "raspduinoDSL_EventHandler"):
                    opp_val = getattr(item, "raspduinoDSL_EventHandler", None)
                    
                    setattr(item, "raspduinoDSL_EventHandler", self)
                    

    @property
    def raspduinoDSL_Model6(self):
        return self.__raspduinoDSL_Model6

    @raspduinoDSL_Model6.setter
    def raspduinoDSL_Model6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspduinoDSL_Model__raspduinoDSL_Model6", None)
        self.__raspduinoDSL_Model6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "raspduinoDSL_Timer"):
                    opp_val = getattr(item, "raspduinoDSL_Timer", None)
                    
                    if opp_val == self:
                        setattr(item, "raspduinoDSL_Timer", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "raspduinoDSL_Timer"):
                    opp_val = getattr(item, "raspduinoDSL_Timer", None)
                    
                    setattr(item, "raspduinoDSL_Timer", self)
                    

    @property
    def raspduinoDSL_Model4(self):
        return self.__raspduinoDSL_Model4

    @raspduinoDSL_Model4.setter
    def raspduinoDSL_Model4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspduinoDSL_Model__raspduinoDSL_Model4", None)
        self.__raspduinoDSL_Model4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "raspduinoDSL_SensorListener"):
                    opp_val = getattr(item, "raspduinoDSL_SensorListener", None)
                    
                    if opp_val == self:
                        setattr(item, "raspduinoDSL_SensorListener", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "raspduinoDSL_SensorListener"):
                    opp_val = getattr(item, "raspduinoDSL_SensorListener", None)
                    
                    setattr(item, "raspduinoDSL_SensorListener", self)
                    

    @property
    def raspduinoDSL_Model(self):
        return self.__raspduinoDSL_Model

    @raspduinoDSL_Model.setter
    def raspduinoDSL_Model(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspduinoDSL_Model__raspduinoDSL_Model", None)
        self.__raspduinoDSL_Model = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "raspduinoDSL_AbstractDevice"):
                    opp_val = getattr(item, "raspduinoDSL_AbstractDevice", None)
                    
                    if opp_val == self:
                        setattr(item, "raspduinoDSL_AbstractDevice", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "raspduinoDSL_AbstractDevice"):
                    opp_val = getattr(item, "raspduinoDSL_AbstractDevice", None)
                    
                    setattr(item, "raspduinoDSL_AbstractDevice", self)
                    
