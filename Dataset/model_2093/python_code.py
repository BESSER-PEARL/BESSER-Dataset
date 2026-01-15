from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class VisualValues(Enum):
    light = "light"
    dark = "dark"
    any = "any"
class SignalValues(Enum):
    off = "off"
    on = "on"
    any = "any"


############################################
# Definition of Classes
############################################

class Port:

    pass
class ftp_HydraulicPort(Port):

    pass
class TypedPortValue:

    pass
class ftp_VisualValue(TypedPortValue):

    def __init__(self, bulb: str):
        self.bulb = bulb
        
    @property
    def bulb(self) -> str:
        return self.__bulb

    @bulb.setter
    def bulb(self, bulb: str):
        self.__bulb = bulb

class ftp_HydraulicValue(TypedPortValue):

    def __init__(self, pressure: float, anyFlow: bool, anyPressure: bool, flow: float):
        self.pressure = pressure
        self.anyFlow = anyFlow
        self.anyPressure = anyPressure
        self.flow = flow
        
    @property
    def flow(self) -> float:
        return self.__flow

    @flow.setter
    def flow(self, flow: float):
        self.__flow = flow

    @property
    def anyFlow(self) -> bool:
        return self.__anyFlow

    @anyFlow.setter
    def anyFlow(self, anyFlow: bool):
        self.__anyFlow = anyFlow

    @property
    def pressure(self) -> float:
        return self.__pressure

    @pressure.setter
    def pressure(self, pressure: float):
        self.__pressure = pressure

    @property
    def anyPressure(self) -> bool:
        return self.__anyPressure

    @anyPressure.setter
    def anyPressure(self, anyPressure: bool):
        self.__anyPressure = anyPressure

class ftp_FloatValue(TypedPortValue):

    def __init__(self, value: float):
        self.value = value
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

class ftp_ElectricalValue(TypedPortValue):

    def __init__(self, current: float, voltage: float, anyCurrent: bool, anyVoltage: bool):
        self.current = current
        self.voltage = voltage
        self.anyCurrent = anyCurrent
        self.anyVoltage = anyVoltage
        
    @property
    def anyVoltage(self) -> bool:
        return self.__anyVoltage

    @anyVoltage.setter
    def anyVoltage(self, anyVoltage: bool):
        self.__anyVoltage = anyVoltage

    @property
    def voltage(self) -> float:
        return self.__voltage

    @voltage.setter
    def voltage(self, voltage: float):
        self.__voltage = voltage

    @property
    def current(self) -> float:
        return self.__current

    @current.setter
    def current(self, current: float):
        self.__current = current

    @property
    def anyCurrent(self) -> bool:
        return self.__anyCurrent

    @anyCurrent.setter
    def anyCurrent(self, anyCurrent: bool):
        self.__anyCurrent = anyCurrent

class ftp_SignalValue(TypedPortValue):

    def __init__(self, signal: str):
        self.signal = signal
        
    @property
    def signal(self) -> str:
        return self.__signal

    @signal.setter
    def signal(self, signal: str):
        self.__signal = signal

class ftp_MechanicalPort(Port):

    pass
class ftp_FaultTreeContext:

    pass
class ftp_VisualPort(Port):

    pass
class ftp_SignalPort(Port):

    pass
class ftp_CompositionElement:

    pass
class ftp_ElectricalPort(Port):

    pass
class PrimitiveComponent:

    pass
class ftp_PTransistor(PrimitiveComponent):

    pass
class ftp_Xor(PrimitiveComponent):

    pass
class ftp_AnalogLamp(PrimitiveComponent):

    pass
class ftp_DFlipFlop(PrimitiveComponent):

    pass
class ftp_NTransistor(PrimitiveComponent):

    pass
class ftp_And(PrimitiveComponent):

    pass
class ftp_DigitalLamp(PrimitiveComponent):

    pass
class ftp_AnalogSwitch(PrimitiveComponent):

    pass
class ftp_DigitalBattery(PrimitiveComponent):

    pass
class ftp_SignalConstant(PrimitiveComponent):

    def __init__(self, value: str, ftp_SignalConstant: "ftp_SignalPort" = None):
        self.value = value
        self.ftp_SignalConstant = ftp_SignalConstant
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def ftp_SignalConstant(self):
        return self.__ftp_SignalConstant

    @ftp_SignalConstant.setter
    def ftp_SignalConstant(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ftp_SignalConstant__ftp_SignalConstant", None)
        self.__ftp_SignalConstant = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ftp_SignalPort106"):
                opp_val = getattr(old_value, "ftp_SignalPort106", None)
                if opp_val == self:
                    setattr(old_value, "ftp_SignalPort106", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ftp_SignalPort106"):
                opp_val = getattr(value, "ftp_SignalPort106", None)
                setattr(value, "ftp_SignalPort106", self)

class ftp_Capacitor(PrimitiveComponent):

    pass
class ftp_Not(PrimitiveComponent):

    pass
class ftp_AnalogBattery(PrimitiveComponent):

    def __init__(self, voltage: float, ftp_AnalogBattery: "ftp_ElectricalPort" = None, ftp_AnalogBattery34: "ftp_ElectricalPort" = None):
        self.voltage = voltage
        self.ftp_AnalogBattery = ftp_AnalogBattery
        self.ftp_AnalogBattery34 = ftp_AnalogBattery34
        
    @property
    def voltage(self) -> float:
        return self.__voltage

    @voltage.setter
    def voltage(self, voltage: float):
        self.__voltage = voltage

    @property
    def ftp_AnalogBattery34(self):
        return self.__ftp_AnalogBattery34

    @ftp_AnalogBattery34.setter
    def ftp_AnalogBattery34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ftp_AnalogBattery__ftp_AnalogBattery34", None)
        self.__ftp_AnalogBattery34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ftp_ElectricalPort35"):
                opp_val = getattr(old_value, "ftp_ElectricalPort35", None)
                if opp_val == self:
                    setattr(old_value, "ftp_ElectricalPort35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ftp_ElectricalPort35"):
                opp_val = getattr(value, "ftp_ElectricalPort35", None)
                setattr(value, "ftp_ElectricalPort35", self)

    @property
    def ftp_AnalogBattery(self):
        return self.__ftp_AnalogBattery

    @ftp_AnalogBattery.setter
    def ftp_AnalogBattery(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ftp_AnalogBattery__ftp_AnalogBattery", None)
        self.__ftp_AnalogBattery = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ftp_ElectricalPort32"):
                opp_val = getattr(old_value, "ftp_ElectricalPort32", None)
                if opp_val == self:
                    setattr(old_value, "ftp_ElectricalPort32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ftp_ElectricalPort32"):
                opp_val = getattr(value, "ftp_ElectricalPort32", None)
                setattr(value, "ftp_ElectricalPort32", self)

class ftp_DigitalSwitch(PrimitiveComponent):

    pass
class ftp_Resistor(PrimitiveComponent):

    def __init__(self, resistance: float, ftp_Resistor: "ftp_ElectricalPort" = None, ftp_Resistor29: "ftp_ElectricalPort" = None):
        self.resistance = resistance
        self.ftp_Resistor = ftp_Resistor
        self.ftp_Resistor29 = ftp_Resistor29
        
    @property
    def resistance(self) -> float:
        return self.__resistance

    @resistance.setter
    def resistance(self, resistance: float):
        self.__resistance = resistance

    @property
    def ftp_Resistor(self):
        return self.__ftp_Resistor

    @ftp_Resistor.setter
    def ftp_Resistor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ftp_Resistor__ftp_Resistor", None)
        self.__ftp_Resistor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ftp_ElectricalPort"):
                opp_val = getattr(old_value, "ftp_ElectricalPort", None)
                if opp_val == self:
                    setattr(old_value, "ftp_ElectricalPort", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ftp_ElectricalPort"):
                opp_val = getattr(value, "ftp_ElectricalPort", None)
                setattr(value, "ftp_ElectricalPort", self)

    @property
    def ftp_Resistor29(self):
        return self.__ftp_Resistor29

    @ftp_Resistor29.setter
    def ftp_Resistor29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ftp_Resistor__ftp_Resistor29", None)
        self.__ftp_Resistor29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ftp_ElectricalPort30"):
                opp_val = getattr(old_value, "ftp_ElectricalPort30", None)
                if opp_val == self:
                    setattr(old_value, "ftp_ElectricalPort30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ftp_ElectricalPort30"):
                opp_val = getattr(value, "ftp_ElectricalPort30", None)
                setattr(value, "ftp_ElectricalPort30", self)

class ftp_TypedPortValue:

    pass
class CompositionElement:

    pass
class Component:

    pass
class ftp_ComposedComponent(Component):

    pass
class ftp_PrimitiveComponent(Component):

    pass
class AnalogConnection:

    pass
class ftp_MechanicalConnection(AnalogConnection):

    pass
class ftp_HydraulicConnection(AnalogConnection):

    pass
class ftp_ElectricalConnection(AnalogConnection):

    pass
class DigintalConnection:

    pass
class ftp_SignalConnection(DigintalConnection):

    pass
class Connection:

    pass
class ftp_VisualConnection(Connection):

    pass
class ftp_AnalogConnection(Connection):

    pass
class ftp_DigintalConnection(Connection):

    pass
class ftp_Connection(CompositionElement):

    pass
class ftp_Port:

    def __init__(self, name: str, type: str, ftp_Port: "ftp_Connection" = None, ftp_Port17: "ftp_Connection" = None, ftp_Port21: "ftp_ComposedComponent" = None, ftp_Port24: "ftp_PortValue" = None):
        self.name = name
        self.type = type
        self.ftp_Port = ftp_Port
        self.ftp_Port17 = ftp_Port17
        self.ftp_Port21 = ftp_Port21
        self.ftp_Port24 = ftp_Port24
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def ftp_Port24(self):
        return self.__ftp_Port24

    @ftp_Port24.setter
    def ftp_Port24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ftp_Port__ftp_Port24", None)
        self.__ftp_Port24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ftp_PortValue23"):
                opp_val = getattr(old_value, "ftp_PortValue23", None)
                if opp_val == self:
                    setattr(old_value, "ftp_PortValue23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ftp_PortValue23"):
                opp_val = getattr(value, "ftp_PortValue23", None)
                setattr(value, "ftp_PortValue23", self)

    @property
    def ftp_Port17(self):
        return self.__ftp_Port17

    @ftp_Port17.setter
    def ftp_Port17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ftp_Port__ftp_Port17", None)
        self.__ftp_Port17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ftp_Connection16"):
                opp_val = getattr(old_value, "ftp_Connection16", None)
                if opp_val == self:
                    setattr(old_value, "ftp_Connection16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ftp_Connection16"):
                opp_val = getattr(value, "ftp_Connection16", None)
                setattr(value, "ftp_Connection16", self)

    @property
    def ftp_Port(self):
        return self.__ftp_Port

    @ftp_Port.setter
    def ftp_Port(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ftp_Port__ftp_Port", None)
        self.__ftp_Port = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ftp_Connection"):
                opp_val = getattr(old_value, "ftp_Connection", None)
                if opp_val == self:
                    setattr(old_value, "ftp_Connection", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ftp_Connection"):
                opp_val = getattr(value, "ftp_Connection", None)
                setattr(value, "ftp_Connection", self)

    @property
    def ftp_Port21(self):
        return self.__ftp_Port21

    @ftp_Port21.setter
    def ftp_Port21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ftp_Port__ftp_Port21", None)
        self.__ftp_Port21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ftp_ComposedComponent20"):
                opp_val = getattr(old_value, "ftp_ComposedComponent20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ftp_ComposedComponent20"):
                opp_val = getattr(value, "ftp_ComposedComponent20", None)
                if opp_val is None:
                    setattr(value, "ftp_ComposedComponent20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def newPortValue(self) -> str:
        # TODO: Implement newPortValue method
        pass

class ftp_FTNode:

    pass
class ftp_PortValue:

    pass
class ftp_Component(CompositionElement):

    def __init__(self, name: str, type: str, ftp_Component: "ftp_Observation" = None):
        self.name = name
        self.type = type
        self.ftp_Component = ftp_Component
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def ftp_Component(self):
        return self.__ftp_Component

    @ftp_Component.setter
    def ftp_Component(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ftp_Component__ftp_Component", None)
        self.__ftp_Component = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ftp_Observation"):
                opp_val = getattr(old_value, "ftp_Observation", None)
                if opp_val == self:
                    setattr(old_value, "ftp_Observation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ftp_Observation"):
                opp_val = getattr(value, "ftp_Observation", None)
                setattr(value, "ftp_Observation", self)

class ftp_Observation:

    def __init__(self, name: str, faultLimit: int, ftp_Observation: "ftp_Component" = None, ftp_Observation10: set["ftp_PortValue"] = None, ftp_Observation12: "ftp_FaultTree" = None, ftp_Observation102: "ftp_FaultTreeContext" = None):
        self.name = name
        self.faultLimit = faultLimit
        self.ftp_Observation = ftp_Observation
        self.ftp_Observation10 = ftp_Observation10 if ftp_Observation10 is not None else set()
        self.ftp_Observation12 = ftp_Observation12
        self.ftp_Observation102 = ftp_Observation102
        
    @property
    def faultLimit(self) -> int:
        return self.__faultLimit

    @faultLimit.setter
    def faultLimit(self, faultLimit: int):
        self.__faultLimit = faultLimit

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ftp_Observation10(self):
        return self.__ftp_Observation10

    @ftp_Observation10.setter
    def ftp_Observation10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ftp_Observation__ftp_Observation10", None)
        self.__ftp_Observation10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ftp_PortValue"):
                    opp_val = getattr(item, "ftp_PortValue", None)
                    
                    if opp_val == self:
                        setattr(item, "ftp_PortValue", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ftp_PortValue"):
                    opp_val = getattr(item, "ftp_PortValue", None)
                    
                    setattr(item, "ftp_PortValue", self)
                    

    @property
    def ftp_Observation102(self):
        return self.__ftp_Observation102

    @ftp_Observation102.setter
    def ftp_Observation102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ftp_Observation__ftp_Observation102", None)
        self.__ftp_Observation102 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ftp_FaultTreeContext101"):
                opp_val = getattr(old_value, "ftp_FaultTreeContext101", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ftp_FaultTreeContext101"):
                opp_val = getattr(value, "ftp_FaultTreeContext101", None)
                if opp_val is None:
                    setattr(value, "ftp_FaultTreeContext101", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ftp_Observation(self):
        return self.__ftp_Observation

    @ftp_Observation.setter
    def ftp_Observation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ftp_Observation__ftp_Observation", None)
        self.__ftp_Observation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ftp_Component"):
                opp_val = getattr(old_value, "ftp_Component", None)
                if opp_val == self:
                    setattr(old_value, "ftp_Component", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ftp_Component"):
                opp_val = getattr(value, "ftp_Component", None)
                setattr(value, "ftp_Component", self)

    @property
    def ftp_Observation12(self):
        return self.__ftp_Observation12

    @ftp_Observation12.setter
    def ftp_Observation12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ftp_Observation__ftp_Observation12", None)
        self.__ftp_Observation12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ftp_FaultTree13"):
                opp_val = getattr(old_value, "ftp_FaultTree13", None)
                if opp_val == self:
                    setattr(old_value, "ftp_FaultTree13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ftp_FaultTree13"):
                opp_val = getattr(value, "ftp_FaultTree13", None)
                setattr(value, "ftp_FaultTree13", self)

    def buildFaultTree(self) -> str:
        # TODO: Implement buildFaultTree method
        pass

class FTNode:

    pass
class ftp_Fault(FTNode):

    def __init__(self, description: str):
        self.description = description
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

class ftp_RootEvent(FTNode):

    def __init__(self, observation: str, ftp_RootEvent: set["ftp_FTNode"] = None):
        self.observation = observation
        self.ftp_RootEvent = ftp_RootEvent if ftp_RootEvent is not None else set()
        
    @property
    def observation(self) -> str:
        return self.__observation

    @observation.setter
    def observation(self, observation: str):
        self.__observation = observation

    @property
    def ftp_RootEvent(self):
        return self.__ftp_RootEvent

    @ftp_RootEvent.setter
    def ftp_RootEvent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ftp_RootEvent__ftp_RootEvent", None)
        self.__ftp_RootEvent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ftp_FTNode104"):
                    opp_val = getattr(item, "ftp_FTNode104", None)
                    
                    if opp_val == self:
                        setattr(item, "ftp_FTNode104", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ftp_FTNode104"):
                    opp_val = getattr(item, "ftp_FTNode104", None)
                    
                    setattr(item, "ftp_FTNode104", self)
                    

class ftp_AndGate(FTNode):

    pass
class ftp_OrGate(FTNode):

    pass
class ftp_FaultTree:

    pass