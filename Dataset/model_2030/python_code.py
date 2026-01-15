from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class ioT_metamodel_Entity:

    pass
class Evaluators:

    pass
class ioT_metamodel_ScriptEvaluator(Evaluators):

    pass
class ioT_metamodel_JavaEvaluator(Evaluators):

    pass
class ioT_metamodel_AtomicDataAttributes(ABC):

    def __init__(self, DataEncoding: str, DeviceID: str, ioT_metamodel_AtomicDataAttributes: "ioT_metamodel_AtomicData" = None):
        self.DataEncoding = DataEncoding
        self.DeviceID = DeviceID
        self.ioT_metamodel_AtomicDataAttributes = ioT_metamodel_AtomicDataAttributes
        
    @property
    def DeviceID(self) -> str:
        return self.__DeviceID

    @DeviceID.setter
    def DeviceID(self, DeviceID: str):
        self.__DeviceID = DeviceID

    @property
    def DataEncoding(self) -> str:
        return self.__DataEncoding

    @DataEncoding.setter
    def DataEncoding(self, DataEncoding: str):
        self.__DataEncoding = DataEncoding

    @property
    def ioT_metamodel_AtomicDataAttributes(self):
        return self.__ioT_metamodel_AtomicDataAttributes

    @ioT_metamodel_AtomicDataAttributes.setter
    def ioT_metamodel_AtomicDataAttributes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioT_metamodel_AtomicDataAttributes__ioT_metamodel_AtomicDataAttributes", None)
        self.__ioT_metamodel_AtomicDataAttributes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ioT_metamodel_AtomicData110"):
                opp_val = getattr(old_value, "ioT_metamodel_AtomicData110", None)
                if opp_val == self:
                    setattr(old_value, "ioT_metamodel_AtomicData110", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ioT_metamodel_AtomicData110"):
                opp_val = getattr(value, "ioT_metamodel_AtomicData110", None)
                setattr(value, "ioT_metamodel_AtomicData110", self)

class ioT_metamodel_DataStreamAttributes(ABC):

    def __init__(self, MeanBitRate: str, Timestamp: str, MaxBitrate: str, Description: str, DataFormat: str, DataEncoding: str, DeviceID: str, ioT_metamodel_DataStreamAttributes: "ioT_metamodel_DataStreams" = None):
        self.MeanBitRate = MeanBitRate
        self.Timestamp = Timestamp
        self.MaxBitrate = MaxBitrate
        self.Description = Description
        self.DataFormat = DataFormat
        self.DataEncoding = DataEncoding
        self.DeviceID = DeviceID
        self.ioT_metamodel_DataStreamAttributes = ioT_metamodel_DataStreamAttributes
        
    @property
    def DataEncoding(self) -> str:
        return self.__DataEncoding

    @DataEncoding.setter
    def DataEncoding(self, DataEncoding: str):
        self.__DataEncoding = DataEncoding

    @property
    def MeanBitRate(self) -> str:
        return self.__MeanBitRate

    @MeanBitRate.setter
    def MeanBitRate(self, MeanBitRate: str):
        self.__MeanBitRate = MeanBitRate

    @property
    def MaxBitrate(self) -> str:
        return self.__MaxBitrate

    @MaxBitrate.setter
    def MaxBitrate(self, MaxBitrate: str):
        self.__MaxBitrate = MaxBitrate

    @property
    def DeviceID(self) -> str:
        return self.__DeviceID

    @DeviceID.setter
    def DeviceID(self, DeviceID: str):
        self.__DeviceID = DeviceID

    @property
    def DataFormat(self) -> str:
        return self.__DataFormat

    @DataFormat.setter
    def DataFormat(self, DataFormat: str):
        self.__DataFormat = DataFormat

    @property
    def Description(self) -> str:
        return self.__Description

    @Description.setter
    def Description(self, Description: str):
        self.__Description = Description

    @property
    def Timestamp(self) -> str:
        return self.__Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp: str):
        self.__Timestamp = Timestamp

    @property
    def ioT_metamodel_DataStreamAttributes(self):
        return self.__ioT_metamodel_DataStreamAttributes

    @ioT_metamodel_DataStreamAttributes.setter
    def ioT_metamodel_DataStreamAttributes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioT_metamodel_DataStreamAttributes__ioT_metamodel_DataStreamAttributes", None)
        self.__ioT_metamodel_DataStreamAttributes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ioT_metamodel_DataStreams108"):
                opp_val = getattr(old_value, "ioT_metamodel_DataStreams108", None)
                if opp_val == self:
                    setattr(old_value, "ioT_metamodel_DataStreams108", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ioT_metamodel_DataStreams108"):
                opp_val = getattr(value, "ioT_metamodel_DataStreams108", None)
                setattr(value, "ioT_metamodel_DataStreams108", self)

class ioT_metamodel_Evaluators(ABC):

    pass
class ioT_metamodel_Operations:

    pass
class ioT_metamodel_Reference_Monitor:

    pass
class ioT_metamodel_Policy_Repository:

    pass
class ioT_metamodel_DataStreams:

    pass
class ioT_metamodel_AtomicData:

    pass
class ioT_metamodel_Information:

    pass
class ioT_metamodel_Port:

    pass
class ioT_metamodel_Service_Resource:

    pass
class ioT_metamodel_Device_Resource:

    pass
class InformationResource:

    pass
class ioT_metamodel_Network_Resource(InformationResource):

    pass
class Actuator:

    pass
class ioT_metamodel_ExternalActuator(Actuator):

    pass
class ioT_metamodel_DeviceActuator(Actuator):

    pass
class Sensor:

    pass
class ioT_metamodel_DeviceSensor(Sensor):

    pass
class ioT_metamodel_ExternalSensor(Sensor):

    pass
class ioT_metamodel_Action:

    def __init__(self, Description: str, ioT_metamodel_Action61: "ioT_metamodel_Transition" = None, ioT_metamodel_Action: "ioT_metamodel_Rule" = None, ioT_metamodel_Action55: "ioT_metamodel_ExternalSensor" = None, ioT_metamodel_Action57: "ioT_metamodel_DeviceActuator" = None, ioT_metamodel_Action59: "ioT_metamodel_ExternalActuator" = None, ioT_metamodel_Action134: "ioT_metamodel_DeviceSensor" = None):
        self.Description = Description
        self.ioT_metamodel_Action61 = ioT_metamodel_Action61
        self.ioT_metamodel_Action = ioT_metamodel_Action
        self.ioT_metamodel_Action55 = ioT_metamodel_Action55
        self.ioT_metamodel_Action57 = ioT_metamodel_Action57
        self.ioT_metamodel_Action59 = ioT_metamodel_Action59
        self.ioT_metamodel_Action134 = ioT_metamodel_Action134
        
    @property
    def Description(self) -> str:
        return self.__Description

    @Description.setter
    def Description(self, Description: str):
        self.__Description = Description

    @property
    def ioT_metamodel_Action55(self):
        return self.__ioT_metamodel_Action55

    @ioT_metamodel_Action55.setter
    def ioT_metamodel_Action55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioT_metamodel_Action__ioT_metamodel_Action55", None)
        self.__ioT_metamodel_Action55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ioT_metamodel_ExternalSensor"):
                opp_val = getattr(old_value, "ioT_metamodel_ExternalSensor", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ioT_metamodel_ExternalSensor"):
                opp_val = getattr(value, "ioT_metamodel_ExternalSensor", None)
                if opp_val is None:
                    setattr(value, "ioT_metamodel_ExternalSensor", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ioT_metamodel_Action59(self):
        return self.__ioT_metamodel_Action59

    @ioT_metamodel_Action59.setter
    def ioT_metamodel_Action59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioT_metamodel_Action__ioT_metamodel_Action59", None)
        self.__ioT_metamodel_Action59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ioT_metamodel_ExternalActuator"):
                opp_val = getattr(old_value, "ioT_metamodel_ExternalActuator", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ioT_metamodel_ExternalActuator"):
                opp_val = getattr(value, "ioT_metamodel_ExternalActuator", None)
                if opp_val is None:
                    setattr(value, "ioT_metamodel_ExternalActuator", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ioT_metamodel_Action57(self):
        return self.__ioT_metamodel_Action57

    @ioT_metamodel_Action57.setter
    def ioT_metamodel_Action57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioT_metamodel_Action__ioT_metamodel_Action57", None)
        self.__ioT_metamodel_Action57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ioT_metamodel_DeviceActuator"):
                opp_val = getattr(old_value, "ioT_metamodel_DeviceActuator", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ioT_metamodel_DeviceActuator"):
                opp_val = getattr(value, "ioT_metamodel_DeviceActuator", None)
                if opp_val is None:
                    setattr(value, "ioT_metamodel_DeviceActuator", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ioT_metamodel_Action(self):
        return self.__ioT_metamodel_Action

    @ioT_metamodel_Action.setter
    def ioT_metamodel_Action(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioT_metamodel_Action__ioT_metamodel_Action", None)
        self.__ioT_metamodel_Action = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ioT_metamodel_Rule53"):
                opp_val = getattr(old_value, "ioT_metamodel_Rule53", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ioT_metamodel_Rule53"):
                opp_val = getattr(value, "ioT_metamodel_Rule53", None)
                if opp_val is None:
                    setattr(value, "ioT_metamodel_Rule53", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ioT_metamodel_Action61(self):
        return self.__ioT_metamodel_Action61

    @ioT_metamodel_Action61.setter
    def ioT_metamodel_Action61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioT_metamodel_Action__ioT_metamodel_Action61", None)
        self.__ioT_metamodel_Action61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ioT_metamodel_Transition"):
                opp_val = getattr(old_value, "ioT_metamodel_Transition", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ioT_metamodel_Transition"):
                opp_val = getattr(value, "ioT_metamodel_Transition", None)
                if opp_val is None:
                    setattr(value, "ioT_metamodel_Transition", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ioT_metamodel_Action134(self):
        return self.__ioT_metamodel_Action134

    @ioT_metamodel_Action134.setter
    def ioT_metamodel_Action134(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioT_metamodel_Action__ioT_metamodel_Action134", None)
        self.__ioT_metamodel_Action134 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ioT_metamodel_DeviceSensor"):
                opp_val = getattr(old_value, "ioT_metamodel_DeviceSensor", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ioT_metamodel_DeviceSensor"):
                opp_val = getattr(value, "ioT_metamodel_DeviceSensor", None)
                if opp_val is None:
                    setattr(value, "ioT_metamodel_DeviceSensor", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class User:

    pass
class ioT_metamodel_Human_User(User):

    pass
class Digital_Artifact:

    pass
class ioT_metamodel_Passive_Digital_Artifact(Digital_Artifact):

    pass
class ioT_metamodel_Active_Digital_Artifact(User, Digital_Artifact):

    pass
class ioT_metamodel_Digital_Artifact:

    pass
class ioT_metamodel_Transition:

    pass
class DeviceState:

    pass
class ioT_metamodel_CompositeState(DeviceState):

    pass
class Device:

    pass
class ioT_metamodel_Actuator(Device):

    def __init__(self, name: str, ioT_metamodel_Actuator43: "ioT_metamodel_DeviceState" = None, ioT_metamodel_Actuator: set["ioT_metamodel_PhysicalThing"] = None):
        self.name = name
        self.ioT_metamodel_Actuator43 = ioT_metamodel_Actuator43
        self.ioT_metamodel_Actuator = ioT_metamodel_Actuator if ioT_metamodel_Actuator is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ioT_metamodel_Actuator(self):
        return self.__ioT_metamodel_Actuator

    @ioT_metamodel_Actuator.setter
    def ioT_metamodel_Actuator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioT_metamodel_Actuator__ioT_metamodel_Actuator", None)
        self.__ioT_metamodel_Actuator = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ioT_metamodel_PhysicalThing41"):
                    opp_val = getattr(item, "ioT_metamodel_PhysicalThing41", None)
                    
                    if opp_val == self:
                        setattr(item, "ioT_metamodel_PhysicalThing41", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ioT_metamodel_PhysicalThing41"):
                    opp_val = getattr(item, "ioT_metamodel_PhysicalThing41", None)
                    
                    setattr(item, "ioT_metamodel_PhysicalThing41", self)
                    

    @property
    def ioT_metamodel_Actuator43(self):
        return self.__ioT_metamodel_Actuator43

    @ioT_metamodel_Actuator43.setter
    def ioT_metamodel_Actuator43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioT_metamodel_Actuator__ioT_metamodel_Actuator43", None)
        self.__ioT_metamodel_Actuator43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ioT_metamodel_DeviceState44"):
                opp_val = getattr(old_value, "ioT_metamodel_DeviceState44", None)
                if opp_val == self:
                    setattr(old_value, "ioT_metamodel_DeviceState44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ioT_metamodel_DeviceState44"):
                opp_val = getattr(value, "ioT_metamodel_DeviceState44", None)
                setattr(value, "ioT_metamodel_DeviceState44", self)

class ioT_metamodel_On_Device_Resource(InformationResource):

    pass
class ioT_metamodel_Communicator:

    def __init__(self, Type: str, ports_number: int, ioT_metamodel_Communicator: "ioT_metamodel_Device" = None, ioT_metamodel_Communicator71: set["ioT_metamodel_Port"] = None):
        self.Type = Type
        self.ports_number = ports_number
        self.ioT_metamodel_Communicator = ioT_metamodel_Communicator
        self.ioT_metamodel_Communicator71 = ioT_metamodel_Communicator71 if ioT_metamodel_Communicator71 is not None else set()
        
    @property
    def ports_number(self) -> int:
        return self.__ports_number

    @ports_number.setter
    def ports_number(self, ports_number: int):
        self.__ports_number = ports_number

    @property
    def Type(self) -> str:
        return self.__Type

    @Type.setter
    def Type(self, Type: str):
        self.__Type = Type

    @property
    def ioT_metamodel_Communicator71(self):
        return self.__ioT_metamodel_Communicator71

    @ioT_metamodel_Communicator71.setter
    def ioT_metamodel_Communicator71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioT_metamodel_Communicator__ioT_metamodel_Communicator71", None)
        self.__ioT_metamodel_Communicator71 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ioT_metamodel_Port"):
                    opp_val = getattr(item, "ioT_metamodel_Port", None)
                    
                    if opp_val == self:
                        setattr(item, "ioT_metamodel_Port", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ioT_metamodel_Port"):
                    opp_val = getattr(item, "ioT_metamodel_Port", None)
                    
                    setattr(item, "ioT_metamodel_Port", self)
                    

    @property
    def ioT_metamodel_Communicator(self):
        return self.__ioT_metamodel_Communicator

    @ioT_metamodel_Communicator.setter
    def ioT_metamodel_Communicator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioT_metamodel_Communicator__ioT_metamodel_Communicator", None)
        self.__ioT_metamodel_Communicator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ioT_metamodel_Device37"):
                opp_val = getattr(old_value, "ioT_metamodel_Device37", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ioT_metamodel_Device37"):
                opp_val = getattr(value, "ioT_metamodel_Device37", None)
                if opp_val is None:
                    setattr(value, "ioT_metamodel_Device37", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ioT_metamodel_DeviceState:

    def __init__(self, Enabled: bool, ioT_metamodel_DeviceState44: "ioT_metamodel_Actuator" = None, ioT_metamodel_DeviceState: "ioT_metamodel_Device" = None, ioT_metamodel_DeviceState64: "ioT_metamodel_Transition" = None, ioT_metamodel_DeviceState67: "ioT_metamodel_Transition" = None, ioT_metamodel_DeviceState51: "ioT_metamodel_Sensor" = None):
        self.Enabled = Enabled
        self.ioT_metamodel_DeviceState44 = ioT_metamodel_DeviceState44
        self.ioT_metamodel_DeviceState = ioT_metamodel_DeviceState
        self.ioT_metamodel_DeviceState64 = ioT_metamodel_DeviceState64
        self.ioT_metamodel_DeviceState67 = ioT_metamodel_DeviceState67
        self.ioT_metamodel_DeviceState51 = ioT_metamodel_DeviceState51
        
    @property
    def Enabled(self) -> bool:
        return self.__Enabled

    @Enabled.setter
    def Enabled(self, Enabled: bool):
        self.__Enabled = Enabled

    @property
    def ioT_metamodel_DeviceState44(self):
        return self.__ioT_metamodel_DeviceState44

    @ioT_metamodel_DeviceState44.setter
    def ioT_metamodel_DeviceState44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioT_metamodel_DeviceState__ioT_metamodel_DeviceState44", None)
        self.__ioT_metamodel_DeviceState44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ioT_metamodel_Actuator43"):
                opp_val = getattr(old_value, "ioT_metamodel_Actuator43", None)
                if opp_val == self:
                    setattr(old_value, "ioT_metamodel_Actuator43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ioT_metamodel_Actuator43"):
                opp_val = getattr(value, "ioT_metamodel_Actuator43", None)
                setattr(value, "ioT_metamodel_Actuator43", self)

    @property
    def ioT_metamodel_DeviceState(self):
        return self.__ioT_metamodel_DeviceState

    @ioT_metamodel_DeviceState.setter
    def ioT_metamodel_DeviceState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioT_metamodel_DeviceState__ioT_metamodel_DeviceState", None)
        self.__ioT_metamodel_DeviceState = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ioT_metamodel_Device35"):
                opp_val = getattr(old_value, "ioT_metamodel_Device35", None)
                if opp_val == self:
                    setattr(old_value, "ioT_metamodel_Device35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ioT_metamodel_Device35"):
                opp_val = getattr(value, "ioT_metamodel_Device35", None)
                setattr(value, "ioT_metamodel_Device35", self)

    @property
    def ioT_metamodel_DeviceState51(self):
        return self.__ioT_metamodel_DeviceState51

    @ioT_metamodel_DeviceState51.setter
    def ioT_metamodel_DeviceState51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioT_metamodel_DeviceState__ioT_metamodel_DeviceState51", None)
        self.__ioT_metamodel_DeviceState51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ioT_metamodel_Sensor50"):
                opp_val = getattr(old_value, "ioT_metamodel_Sensor50", None)
                if opp_val == self:
                    setattr(old_value, "ioT_metamodel_Sensor50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ioT_metamodel_Sensor50"):
                opp_val = getattr(value, "ioT_metamodel_Sensor50", None)
                setattr(value, "ioT_metamodel_Sensor50", self)

    @property
    def ioT_metamodel_DeviceState64(self):
        return self.__ioT_metamodel_DeviceState64

    @ioT_metamodel_DeviceState64.setter
    def ioT_metamodel_DeviceState64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioT_metamodel_DeviceState__ioT_metamodel_DeviceState64", None)
        self.__ioT_metamodel_DeviceState64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ioT_metamodel_Transition63"):
                opp_val = getattr(old_value, "ioT_metamodel_Transition63", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ioT_metamodel_Transition63"):
                opp_val = getattr(value, "ioT_metamodel_Transition63", None)
                if opp_val is None:
                    setattr(value, "ioT_metamodel_Transition63", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ioT_metamodel_DeviceState67(self):
        return self.__ioT_metamodel_DeviceState67

    @ioT_metamodel_DeviceState67.setter
    def ioT_metamodel_DeviceState67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioT_metamodel_DeviceState__ioT_metamodel_DeviceState67", None)
        self.__ioT_metamodel_DeviceState67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ioT_metamodel_Transition66"):
                opp_val = getattr(old_value, "ioT_metamodel_Transition66", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ioT_metamodel_Transition66"):
                opp_val = getattr(value, "ioT_metamodel_Transition66", None)
                if opp_val is None:
                    setattr(value, "ioT_metamodel_Transition66", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ioT_metamodel_Rule:

    def __init__(self, conditionLiteral: str, conditionValue: float, ioT_metamodel_Rule: "ioT_metamodel_Device" = None, ioT_metamodel_Rule53: set["ioT_metamodel_Action"] = None):
        self.conditionLiteral = conditionLiteral
        self.conditionValue = conditionValue
        self.ioT_metamodel_Rule = ioT_metamodel_Rule
        self.ioT_metamodel_Rule53 = ioT_metamodel_Rule53 if ioT_metamodel_Rule53 is not None else set()
        
    @property
    def conditionLiteral(self) -> str:
        return self.__conditionLiteral

    @conditionLiteral.setter
    def conditionLiteral(self, conditionLiteral: str):
        self.__conditionLiteral = conditionLiteral

    @property
    def conditionValue(self) -> float:
        return self.__conditionValue

    @conditionValue.setter
    def conditionValue(self, conditionValue: float):
        self.__conditionValue = conditionValue

    @property
    def ioT_metamodel_Rule53(self):
        return self.__ioT_metamodel_Rule53

    @ioT_metamodel_Rule53.setter
    def ioT_metamodel_Rule53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioT_metamodel_Rule__ioT_metamodel_Rule53", None)
        self.__ioT_metamodel_Rule53 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ioT_metamodel_Action"):
                    opp_val = getattr(item, "ioT_metamodel_Action", None)
                    
                    if opp_val == self:
                        setattr(item, "ioT_metamodel_Action", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ioT_metamodel_Action"):
                    opp_val = getattr(item, "ioT_metamodel_Action", None)
                    
                    setattr(item, "ioT_metamodel_Action", self)
                    

    @property
    def ioT_metamodel_Rule(self):
        return self.__ioT_metamodel_Rule

    @ioT_metamodel_Rule.setter
    def ioT_metamodel_Rule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioT_metamodel_Rule__ioT_metamodel_Rule", None)
        self.__ioT_metamodel_Rule = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ioT_metamodel_Device33"):
                opp_val = getattr(old_value, "ioT_metamodel_Device33", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ioT_metamodel_Device33"):
                opp_val = getattr(value, "ioT_metamodel_Device33", None)
                if opp_val is None:
                    setattr(value, "ioT_metamodel_Device33", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ioT_metamodel_Sensor(Device):

    def __init__(self, Name: str, State: bool, frequency: float, ioT_metamodel_Sensor: set["ioT_metamodel_PhysicalThing"] = None, ioT_metamodel_Sensor50: "ioT_metamodel_DeviceState" = None):
        self.Name = Name
        self.State = State
        self.frequency = frequency
        self.ioT_metamodel_Sensor = ioT_metamodel_Sensor if ioT_metamodel_Sensor is not None else set()
        self.ioT_metamodel_Sensor50 = ioT_metamodel_Sensor50
        
    @property
    def State(self) -> bool:
        return self.__State

    @State.setter
    def State(self, State: bool):
        self.__State = State

    @property
    def frequency(self) -> float:
        return self.__frequency

    @frequency.setter
    def frequency(self, frequency: float):
        self.__frequency = frequency

    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def ioT_metamodel_Sensor(self):
        return self.__ioT_metamodel_Sensor

    @ioT_metamodel_Sensor.setter
    def ioT_metamodel_Sensor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioT_metamodel_Sensor__ioT_metamodel_Sensor", None)
        self.__ioT_metamodel_Sensor = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ioT_metamodel_PhysicalThing48"):
                    opp_val = getattr(item, "ioT_metamodel_PhysicalThing48", None)
                    
                    if opp_val == self:
                        setattr(item, "ioT_metamodel_PhysicalThing48", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ioT_metamodel_PhysicalThing48"):
                    opp_val = getattr(item, "ioT_metamodel_PhysicalThing48", None)
                    
                    setattr(item, "ioT_metamodel_PhysicalThing48", self)
                    

    @property
    def ioT_metamodel_Sensor50(self):
        return self.__ioT_metamodel_Sensor50

    @ioT_metamodel_Sensor50.setter
    def ioT_metamodel_Sensor50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioT_metamodel_Sensor__ioT_metamodel_Sensor50", None)
        self.__ioT_metamodel_Sensor50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ioT_metamodel_DeviceState51"):
                opp_val = getattr(old_value, "ioT_metamodel_DeviceState51", None)
                if opp_val == self:
                    setattr(old_value, "ioT_metamodel_DeviceState51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ioT_metamodel_DeviceState51"):
                opp_val = getattr(value, "ioT_metamodel_DeviceState51", None)
                setattr(value, "ioT_metamodel_DeviceState51", self)

class ioT_metamodel_Tag(Device):

    def __init__(self, Name: str, ioT_metamodel_Tag: set["ioT_metamodel_PhysicalThing"] = None):
        self.Name = Name
        self.ioT_metamodel_Tag = ioT_metamodel_Tag if ioT_metamodel_Tag is not None else set()
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def ioT_metamodel_Tag(self):
        return self.__ioT_metamodel_Tag

    @ioT_metamodel_Tag.setter
    def ioT_metamodel_Tag(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioT_metamodel_Tag__ioT_metamodel_Tag", None)
        self.__ioT_metamodel_Tag = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ioT_metamodel_PhysicalThing46"):
                    opp_val = getattr(item, "ioT_metamodel_PhysicalThing46", None)
                    
                    if opp_val == self:
                        setattr(item, "ioT_metamodel_PhysicalThing46", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ioT_metamodel_PhysicalThing46"):
                    opp_val = getattr(item, "ioT_metamodel_PhysicalThing46", None)
                    
                    setattr(item, "ioT_metamodel_PhysicalThing46", self)
                    

class ioT_metamodel_Authorizor:

    pass
class ioT_metamodel_Database:

    pass
class ioT_metamodel_Cloud:

    pass
class ioT_metamodel_FogNode:

    pass
class PhysicalThing:

    pass
class ioT_metamodel_Fog_Services:

    pass
class ioT_metamodel_Analytics_Engine:

    pass
class ioT_metamodel_Container:

    def __init__(self, ID: str, IP_address: str, ioT_metamodel_Container: "ioT_metamodel_FogNode" = None, ioT_metamodel_Container129: "ioT_metamodel_Operations" = None, ioT_metamodel_Container113: "ioT_metamodel_Fog_Services" = None):
        self.ID = ID
        self.IP_address = IP_address
        self.ioT_metamodel_Container = ioT_metamodel_Container
        self.ioT_metamodel_Container129 = ioT_metamodel_Container129
        self.ioT_metamodel_Container113 = ioT_metamodel_Container113
        
    @property
    def IP_address(self) -> str:
        return self.__IP_address

    @IP_address.setter
    def IP_address(self, IP_address: str):
        self.__IP_address = IP_address

    @property
    def ID(self) -> str:
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

    @property
    def ioT_metamodel_Container(self):
        return self.__ioT_metamodel_Container

    @ioT_metamodel_Container.setter
    def ioT_metamodel_Container(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioT_metamodel_Container__ioT_metamodel_Container", None)
        self.__ioT_metamodel_Container = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ioT_metamodel_FogNode24"):
                opp_val = getattr(old_value, "ioT_metamodel_FogNode24", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ioT_metamodel_FogNode24"):
                opp_val = getattr(value, "ioT_metamodel_FogNode24", None)
                if opp_val is None:
                    setattr(value, "ioT_metamodel_FogNode24", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ioT_metamodel_Container113(self):
        return self.__ioT_metamodel_Container113

    @ioT_metamodel_Container113.setter
    def ioT_metamodel_Container113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioT_metamodel_Container__ioT_metamodel_Container113", None)
        self.__ioT_metamodel_Container113 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ioT_metamodel_Fog_Services112"):
                opp_val = getattr(old_value, "ioT_metamodel_Fog_Services112", None)
                if opp_val == self:
                    setattr(old_value, "ioT_metamodel_Fog_Services112", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ioT_metamodel_Fog_Services112"):
                opp_val = getattr(value, "ioT_metamodel_Fog_Services112", None)
                setattr(value, "ioT_metamodel_Fog_Services112", self)

    @property
    def ioT_metamodel_Container129(self):
        return self.__ioT_metamodel_Container129

    @ioT_metamodel_Container129.setter
    def ioT_metamodel_Container129(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioT_metamodel_Container__ioT_metamodel_Container129", None)
        self.__ioT_metamodel_Container129 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ioT_metamodel_Operations128"):
                opp_val = getattr(old_value, "ioT_metamodel_Operations128", None)
                if opp_val == self:
                    setattr(old_value, "ioT_metamodel_Operations128", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ioT_metamodel_Operations128"):
                opp_val = getattr(value, "ioT_metamodel_Operations128", None)
                setattr(value, "ioT_metamodel_Operations128", self)

class ioT_metamodel_VM:

    pass
class Passive_Digital_Artifact:

    pass
class Active_Digital_Artifact:

    pass
class ioT_metamodel_Property:

    def __init__(self, changeable: bool, ioT_metamodel_Property: "ioT_metamodel_Thing" = None):
        self.changeable = changeable
        self.ioT_metamodel_Property = ioT_metamodel_Property
        
    @property
    def changeable(self) -> bool:
        return self.__changeable

    @changeable.setter
    def changeable(self, changeable: bool):
        self.__changeable = changeable

    @property
    def ioT_metamodel_Property(self):
        return self.__ioT_metamodel_Property

    @ioT_metamodel_Property.setter
    def ioT_metamodel_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioT_metamodel_Property__ioT_metamodel_Property", None)
        self.__ioT_metamodel_Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ioT_metamodel_Thing8"):
                opp_val = getattr(old_value, "ioT_metamodel_Thing8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ioT_metamodel_Thing8"):
                opp_val = getattr(value, "ioT_metamodel_Thing8", None)
                if opp_val is None:
                    setattr(value, "ioT_metamodel_Thing8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ioT_metamodel_Device(PhysicalThing):

    def __init__(self, Technology: str, Device: "ioT_metamodel_PhysicalThing" = None, has: set["ioT_metamodel_PhysicalThing"] = None, ioT_metamodel_Device: "ioT_metamodel_Device" = None, ioT_metamodel_Device30: set["ioT_metamodel_Device"] = None, ioT_metamodel_Device33: set["ioT_metamodel_Rule"] = None, ioT_metamodel_Device35: "ioT_metamodel_DeviceState" = None, ioT_metamodel_Device37: set["ioT_metamodel_Communicator"] = None, ioT_metamodel_Device39: set["ioT_metamodel_On_Device_Resource"] = None):
        self.Technology = Technology
        self.Device = Device
        self.has = has if has is not None else set()
        self.ioT_metamodel_Device = ioT_metamodel_Device
        self.ioT_metamodel_Device30 = ioT_metamodel_Device30 if ioT_metamodel_Device30 is not None else set()
        self.ioT_metamodel_Device33 = ioT_metamodel_Device33 if ioT_metamodel_Device33 is not None else set()
        self.ioT_metamodel_Device35 = ioT_metamodel_Device35
        self.ioT_metamodel_Device37 = ioT_metamodel_Device37 if ioT_metamodel_Device37 is not None else set()
        self.ioT_metamodel_Device39 = ioT_metamodel_Device39 if ioT_metamodel_Device39 is not None else set()
        
    @property
    def Technology(self) -> str:
        return self.__Technology

    @Technology.setter
    def Technology(self, Technology: str):
        self.__Technology = Technology

    @property
    def ioT_metamodel_Device30(self):
        return self.__ioT_metamodel_Device30

    @ioT_metamodel_Device30.setter
    def ioT_metamodel_Device30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioT_metamodel_Device__ioT_metamodel_Device30", None)
        self.__ioT_metamodel_Device30 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ioT_metamodel_Device"):
                    opp_val = getattr(item, "ioT_metamodel_Device", None)
                    
                    if opp_val == self:
                        setattr(item, "ioT_metamodel_Device", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ioT_metamodel_Device"):
                    opp_val = getattr(item, "ioT_metamodel_Device", None)
                    
                    setattr(item, "ioT_metamodel_Device", self)
                    

    @property
    def ioT_metamodel_Device35(self):
        return self.__ioT_metamodel_Device35

    @ioT_metamodel_Device35.setter
    def ioT_metamodel_Device35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioT_metamodel_Device__ioT_metamodel_Device35", None)
        self.__ioT_metamodel_Device35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ioT_metamodel_DeviceState"):
                opp_val = getattr(old_value, "ioT_metamodel_DeviceState", None)
                if opp_val == self:
                    setattr(old_value, "ioT_metamodel_DeviceState", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ioT_metamodel_DeviceState"):
                opp_val = getattr(value, "ioT_metamodel_DeviceState", None)
                setattr(value, "ioT_metamodel_DeviceState", self)

    @property
    def has(self):
        return self.__has

    @has.setter
    def has(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioT_metamodel_Device__has", None)
        self.__has = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PhysicalThing"):
                    opp_val = getattr(item, "PhysicalThing", None)
                    
                    if opp_val == self:
                        setattr(item, "PhysicalThing", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PhysicalThing"):
                    opp_val = getattr(item, "PhysicalThing", None)
                    
                    setattr(item, "PhysicalThing", self)
                    

    @property
    def Device(self):
        return self.__Device

    @Device.setter
    def Device(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioT_metamodel_Device__Device", None)
        self.__Device = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "is_attached_to"):
                opp_val = getattr(old_value, "is_attached_to", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "is_attached_to"):
                opp_val = getattr(value, "is_attached_to", None)
                if opp_val is None:
                    setattr(value, "is_attached_to", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ioT_metamodel_Device33(self):
        return self.__ioT_metamodel_Device33

    @ioT_metamodel_Device33.setter
    def ioT_metamodel_Device33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioT_metamodel_Device__ioT_metamodel_Device33", None)
        self.__ioT_metamodel_Device33 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ioT_metamodel_Rule"):
                    opp_val = getattr(item, "ioT_metamodel_Rule", None)
                    
                    if opp_val == self:
                        setattr(item, "ioT_metamodel_Rule", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ioT_metamodel_Rule"):
                    opp_val = getattr(item, "ioT_metamodel_Rule", None)
                    
                    setattr(item, "ioT_metamodel_Rule", self)
                    

    @property
    def ioT_metamodel_Device39(self):
        return self.__ioT_metamodel_Device39

    @ioT_metamodel_Device39.setter
    def ioT_metamodel_Device39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioT_metamodel_Device__ioT_metamodel_Device39", None)
        self.__ioT_metamodel_Device39 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ioT_metamodel_On_Device_Resource"):
                    opp_val = getattr(item, "ioT_metamodel_On_Device_Resource", None)
                    
                    if opp_val == self:
                        setattr(item, "ioT_metamodel_On_Device_Resource", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ioT_metamodel_On_Device_Resource"):
                    opp_val = getattr(item, "ioT_metamodel_On_Device_Resource", None)
                    
                    setattr(item, "ioT_metamodel_On_Device_Resource", self)
                    

    @property
    def ioT_metamodel_Device37(self):
        return self.__ioT_metamodel_Device37

    @ioT_metamodel_Device37.setter
    def ioT_metamodel_Device37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioT_metamodel_Device__ioT_metamodel_Device37", None)
        self.__ioT_metamodel_Device37 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ioT_metamodel_Communicator"):
                    opp_val = getattr(item, "ioT_metamodel_Communicator", None)
                    
                    if opp_val == self:
                        setattr(item, "ioT_metamodel_Communicator", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ioT_metamodel_Communicator"):
                    opp_val = getattr(item, "ioT_metamodel_Communicator", None)
                    
                    setattr(item, "ioT_metamodel_Communicator", self)
                    

    @property
    def ioT_metamodel_Device(self):
        return self.__ioT_metamodel_Device

    @ioT_metamodel_Device.setter
    def ioT_metamodel_Device(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioT_metamodel_Device__ioT_metamodel_Device", None)
        self.__ioT_metamodel_Device = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ioT_metamodel_Device30"):
                opp_val = getattr(old_value, "ioT_metamodel_Device30", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ioT_metamodel_Device30"):
                opp_val = getattr(value, "ioT_metamodel_Device30", None)
                if opp_val is None:
                    setattr(value, "ioT_metamodel_Device30", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ioT_metamodel_InformationResource:

    pass
class Entity:

    pass
class ioT_metamodel_Attribute(Entity):

    def __init__(self, name: str, Type: str, ioT_metamodel_Attribute: "ioT_metamodel_InformationResource" = None):
        self.name = name
        self.Type = Type
        self.ioT_metamodel_Attribute = ioT_metamodel_Attribute
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Type(self) -> str:
        return self.__Type

    @Type.setter
    def Type(self, Type: str):
        self.__Type = Type

    @property
    def ioT_metamodel_Attribute(self):
        return self.__ioT_metamodel_Attribute

    @ioT_metamodel_Attribute.setter
    def ioT_metamodel_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioT_metamodel_Attribute__ioT_metamodel_Attribute", None)
        self.__ioT_metamodel_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ioT_metamodel_InformationResource78"):
                opp_val = getattr(old_value, "ioT_metamodel_InformationResource78", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ioT_metamodel_InformationResource78"):
                opp_val = getattr(value, "ioT_metamodel_InformationResource78", None)
                if opp_val is None:
                    setattr(value, "ioT_metamodel_InformationResource78", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ioT_metamodel_User(Entity):

    pass
class ioT_metamodel_Thing(Entity):

    def __init__(self, name: str, ioT_metamodel_Thing: "ioT_metamodel_VirtualThing" = None, request_service: "ioT_metamodel_Fog" = None, ioT_metamodel_Thing3: "ioT_metamodel_PhysicalThing" = None, ioT_metamodel_Thing6: "ioT_metamodel_Thing" = None, ioT_metamodel_Thing4: set["ioT_metamodel_Thing"] = None, ioT_metamodel_Thing8: set["ioT_metamodel_Property"] = None, Thing: "ioT_metamodel_Fog" = None):
        self.name = name
        self.ioT_metamodel_Thing = ioT_metamodel_Thing
        self.request_service = request_service
        self.ioT_metamodel_Thing3 = ioT_metamodel_Thing3
        self.ioT_metamodel_Thing6 = ioT_metamodel_Thing6
        self.ioT_metamodel_Thing4 = ioT_metamodel_Thing4 if ioT_metamodel_Thing4 is not None else set()
        self.ioT_metamodel_Thing8 = ioT_metamodel_Thing8 if ioT_metamodel_Thing8 is not None else set()
        self.Thing = Thing
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ioT_metamodel_Thing4(self):
        return self.__ioT_metamodel_Thing4

    @ioT_metamodel_Thing4.setter
    def ioT_metamodel_Thing4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioT_metamodel_Thing__ioT_metamodel_Thing4", None)
        self.__ioT_metamodel_Thing4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ioT_metamodel_Thing6"):
                    opp_val = getattr(item, "ioT_metamodel_Thing6", None)
                    
                    if opp_val == self:
                        setattr(item, "ioT_metamodel_Thing6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ioT_metamodel_Thing6"):
                    opp_val = getattr(item, "ioT_metamodel_Thing6", None)
                    
                    setattr(item, "ioT_metamodel_Thing6", self)
                    

    @property
    def ioT_metamodel_Thing3(self):
        return self.__ioT_metamodel_Thing3

    @ioT_metamodel_Thing3.setter
    def ioT_metamodel_Thing3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioT_metamodel_Thing__ioT_metamodel_Thing3", None)
        self.__ioT_metamodel_Thing3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ioT_metamodel_PhysicalThing"):
                opp_val = getattr(old_value, "ioT_metamodel_PhysicalThing", None)
                if opp_val == self:
                    setattr(old_value, "ioT_metamodel_PhysicalThing", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ioT_metamodel_PhysicalThing"):
                opp_val = getattr(value, "ioT_metamodel_PhysicalThing", None)
                setattr(value, "ioT_metamodel_PhysicalThing", self)

    @property
    def ioT_metamodel_Thing8(self):
        return self.__ioT_metamodel_Thing8

    @ioT_metamodel_Thing8.setter
    def ioT_metamodel_Thing8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioT_metamodel_Thing__ioT_metamodel_Thing8", None)
        self.__ioT_metamodel_Thing8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ioT_metamodel_Property"):
                    opp_val = getattr(item, "ioT_metamodel_Property", None)
                    
                    if opp_val == self:
                        setattr(item, "ioT_metamodel_Property", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ioT_metamodel_Property"):
                    opp_val = getattr(item, "ioT_metamodel_Property", None)
                    
                    setattr(item, "ioT_metamodel_Property", self)
                    

    @property
    def Thing(self):
        return self.__Thing

    @Thing.setter
    def Thing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioT_metamodel_Thing__Thing", None)
        self.__Thing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fog"):
                opp_val = getattr(old_value, "fog", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fog"):
                opp_val = getattr(value, "fog", None)
                if opp_val is None:
                    setattr(value, "fog", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ioT_metamodel_Thing(self):
        return self.__ioT_metamodel_Thing

    @ioT_metamodel_Thing.setter
    def ioT_metamodel_Thing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioT_metamodel_Thing__ioT_metamodel_Thing", None)
        self.__ioT_metamodel_Thing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ioT_metamodel_VirtualThing"):
                opp_val = getattr(old_value, "ioT_metamodel_VirtualThing", None)
                if opp_val == self:
                    setattr(old_value, "ioT_metamodel_VirtualThing", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ioT_metamodel_VirtualThing"):
                opp_val = getattr(value, "ioT_metamodel_VirtualThing", None)
                setattr(value, "ioT_metamodel_VirtualThing", self)

    @property
    def request_service(self):
        return self.__request_service

    @request_service.setter
    def request_service(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioT_metamodel_Thing__request_service", None)
        self.__request_service = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Fog"):
                opp_val = getattr(old_value, "Fog", None)
                if opp_val == self:
                    setattr(old_value, "Fog", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Fog"):
                opp_val = getattr(value, "Fog", None)
                setattr(value, "Fog", self)

    @property
    def ioT_metamodel_Thing6(self):
        return self.__ioT_metamodel_Thing6

    @ioT_metamodel_Thing6.setter
    def ioT_metamodel_Thing6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioT_metamodel_Thing__ioT_metamodel_Thing6", None)
        self.__ioT_metamodel_Thing6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ioT_metamodel_Thing4"):
                opp_val = getattr(old_value, "ioT_metamodel_Thing4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ioT_metamodel_Thing4"):
                opp_val = getattr(value, "ioT_metamodel_Thing4", None)
                if opp_val is None:
                    setattr(value, "ioT_metamodel_Thing4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ioT_metamodel_PhysicalThing:

    pass
class ioT_metamodel_Fog:

    pass
class ioT_metamodel_VirtualThing(Active_Digital_Artifact, Passive_Digital_Artifact):

    def __init__(self, URI: str, ioT_metamodel_VirtualThing: "ioT_metamodel_Thing" = None, ioT_metamodel_VirtualThing13: set["ioT_metamodel_InformationResource"] = None, ioT_metamodel_VirtualThing10: "ioT_metamodel_PhysicalThing" = None, ioT_metamodel_VirtualThing124: "ioT_metamodel_Fog_Services" = None):
        self.URI = URI
        self.ioT_metamodel_VirtualThing = ioT_metamodel_VirtualThing
        self.ioT_metamodel_VirtualThing13 = ioT_metamodel_VirtualThing13 if ioT_metamodel_VirtualThing13 is not None else set()
        self.ioT_metamodel_VirtualThing10 = ioT_metamodel_VirtualThing10
        self.ioT_metamodel_VirtualThing124 = ioT_metamodel_VirtualThing124
        
    @property
    def URI(self) -> str:
        return self.__URI

    @URI.setter
    def URI(self, URI: str):
        self.__URI = URI

    @property
    def ioT_metamodel_VirtualThing13(self):
        return self.__ioT_metamodel_VirtualThing13

    @ioT_metamodel_VirtualThing13.setter
    def ioT_metamodel_VirtualThing13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioT_metamodel_VirtualThing__ioT_metamodel_VirtualThing13", None)
        self.__ioT_metamodel_VirtualThing13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ioT_metamodel_InformationResource"):
                    opp_val = getattr(item, "ioT_metamodel_InformationResource", None)
                    
                    if opp_val == self:
                        setattr(item, "ioT_metamodel_InformationResource", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ioT_metamodel_InformationResource"):
                    opp_val = getattr(item, "ioT_metamodel_InformationResource", None)
                    
                    setattr(item, "ioT_metamodel_InformationResource", self)
                    

    @property
    def ioT_metamodel_VirtualThing(self):
        return self.__ioT_metamodel_VirtualThing

    @ioT_metamodel_VirtualThing.setter
    def ioT_metamodel_VirtualThing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioT_metamodel_VirtualThing__ioT_metamodel_VirtualThing", None)
        self.__ioT_metamodel_VirtualThing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ioT_metamodel_Thing"):
                opp_val = getattr(old_value, "ioT_metamodel_Thing", None)
                if opp_val == self:
                    setattr(old_value, "ioT_metamodel_Thing", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ioT_metamodel_Thing"):
                opp_val = getattr(value, "ioT_metamodel_Thing", None)
                setattr(value, "ioT_metamodel_Thing", self)

    @property
    def ioT_metamodel_VirtualThing10(self):
        return self.__ioT_metamodel_VirtualThing10

    @ioT_metamodel_VirtualThing10.setter
    def ioT_metamodel_VirtualThing10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioT_metamodel_VirtualThing__ioT_metamodel_VirtualThing10", None)
        self.__ioT_metamodel_VirtualThing10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ioT_metamodel_PhysicalThing11"):
                opp_val = getattr(old_value, "ioT_metamodel_PhysicalThing11", None)
                if opp_val == self:
                    setattr(old_value, "ioT_metamodel_PhysicalThing11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ioT_metamodel_PhysicalThing11"):
                opp_val = getattr(value, "ioT_metamodel_PhysicalThing11", None)
                setattr(value, "ioT_metamodel_PhysicalThing11", self)

    @property
    def ioT_metamodel_VirtualThing124(self):
        return self.__ioT_metamodel_VirtualThing124

    @ioT_metamodel_VirtualThing124.setter
    def ioT_metamodel_VirtualThing124(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioT_metamodel_VirtualThing__ioT_metamodel_VirtualThing124", None)
        self.__ioT_metamodel_VirtualThing124 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ioT_metamodel_Fog_Services123"):
                opp_val = getattr(old_value, "ioT_metamodel_Fog_Services123", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ioT_metamodel_Fog_Services123"):
                opp_val = getattr(value, "ioT_metamodel_Fog_Services123", None)
                if opp_val is None:
                    setattr(value, "ioT_metamodel_Fog_Services123", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
