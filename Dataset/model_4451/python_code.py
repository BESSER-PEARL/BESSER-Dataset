from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class ActuatorType(Enum):
    Buzzer = "Buzzer"
    Led = "Led"
    Relay = "Relay"
    Servo = "Servo"
    LCD = "LCD"
    Undefined = "Undefined"
class PortType(Enum):
    Digital = "Digital"
    Analog = "Analog"
class SensorType(Enum):
    Undefined = "Undefined"
    CO2 = "CO2"
    Light = "Light"
    Button = "Button"
    HumidityG = "HumidityG"
    Vibration = "Vibration"
    Temperature = "Temperature"
    Movement = "Movement"
    Contact = "Contact"
    TempHum = "TempHum"
class MessageBrokerType(Enum):
    Undefined = "Undefined"
    MQTT = "MQTT"
class CommunicationType(Enum):
    Undefined = "Undefined"
    WiFi = "WiFi"
    Serial = "Serial"
class DBType(Enum):
    Undefined = "Undefined"
    MySQL = "MySQL"
class ControllerType(Enum):
    Undefined = "Undefined"
    ESP8266 = "ESP8266"


############################################
# Definition of Classes
############################################

class wsmodel3_OutputOrchestrator:

    pass
class wsmodel3_Function:

    def __init__(self, expression: str, wsmodel3_Function69: "wsmodel3_InputOrchestrator" = None, wsmodel3_Function72: "wsmodel3_OutputOrchestrator" = None, wsmodel3_Function75: set["wsmodel3_Break"] = None, wsmodel3_Function: "wsmodel3_Orchestrator" = None):
        self.expression = expression
        self.wsmodel3_Function69 = wsmodel3_Function69
        self.wsmodel3_Function72 = wsmodel3_Function72
        self.wsmodel3_Function75 = wsmodel3_Function75 if wsmodel3_Function75 is not None else set()
        self.wsmodel3_Function = wsmodel3_Function
        
    @property
    def expression(self) -> str:
        return self.__expression

    @expression.setter
    def expression(self, expression: str):
        self.__expression = expression

    @property
    def wsmodel3_Function72(self):
        return self.__wsmodel3_Function72

    @wsmodel3_Function72.setter
    def wsmodel3_Function72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wsmodel3_Function__wsmodel3_Function72", None)
        self.__wsmodel3_Function72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wsmodel3_OutputOrchestrator73"):
                opp_val = getattr(old_value, "wsmodel3_OutputOrchestrator73", None)
                if opp_val == self:
                    setattr(old_value, "wsmodel3_OutputOrchestrator73", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wsmodel3_OutputOrchestrator73"):
                opp_val = getattr(value, "wsmodel3_OutputOrchestrator73", None)
                setattr(value, "wsmodel3_OutputOrchestrator73", self)

    @property
    def wsmodel3_Function69(self):
        return self.__wsmodel3_Function69

    @wsmodel3_Function69.setter
    def wsmodel3_Function69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wsmodel3_Function__wsmodel3_Function69", None)
        self.__wsmodel3_Function69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wsmodel3_InputOrchestrator70"):
                opp_val = getattr(old_value, "wsmodel3_InputOrchestrator70", None)
                if opp_val == self:
                    setattr(old_value, "wsmodel3_InputOrchestrator70", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wsmodel3_InputOrchestrator70"):
                opp_val = getattr(value, "wsmodel3_InputOrchestrator70", None)
                setattr(value, "wsmodel3_InputOrchestrator70", self)

    @property
    def wsmodel3_Function(self):
        return self.__wsmodel3_Function

    @wsmodel3_Function.setter
    def wsmodel3_Function(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wsmodel3_Function__wsmodel3_Function", None)
        self.__wsmodel3_Function = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wsmodel3_Orchestrator59"):
                opp_val = getattr(old_value, "wsmodel3_Orchestrator59", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wsmodel3_Orchestrator59"):
                opp_val = getattr(value, "wsmodel3_Orchestrator59", None)
                if opp_val is None:
                    setattr(value, "wsmodel3_Orchestrator59", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def wsmodel3_Function75(self):
        return self.__wsmodel3_Function75

    @wsmodel3_Function75.setter
    def wsmodel3_Function75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wsmodel3_Function__wsmodel3_Function75", None)
        self.__wsmodel3_Function75 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "wsmodel3_Break"):
                    opp_val = getattr(item, "wsmodel3_Break", None)
                    
                    if opp_val == self:
                        setattr(item, "wsmodel3_Break", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "wsmodel3_Break"):
                    opp_val = getattr(item, "wsmodel3_Break", None)
                    
                    setattr(item, "wsmodel3_Break", self)
                    

class wsmodel3_Orchestrator:

    def __init__(self, name: str, port: str, wsmodel3_Orchestrator66: set["wsmodel3_REST"] = None, wsmodel3_Orchestrator: "wsmodel3_IntegrationPattern" = None, wsmodel3_Orchestrator56: set["wsmodel3_InputOrchestrator"] = None, wsmodel3_Orchestrator59: set["wsmodel3_Function"] = None, wsmodel3_Orchestrator61: set["wsmodel3_OutputOrchestrator"] = None, wsmodel3_Orchestrator63: set["wsmodel3_ExternalAPI"] = None):
        self.name = name
        self.port = port
        self.wsmodel3_Orchestrator66 = wsmodel3_Orchestrator66 if wsmodel3_Orchestrator66 is not None else set()
        self.wsmodel3_Orchestrator = wsmodel3_Orchestrator
        self.wsmodel3_Orchestrator56 = wsmodel3_Orchestrator56 if wsmodel3_Orchestrator56 is not None else set()
        self.wsmodel3_Orchestrator59 = wsmodel3_Orchestrator59 if wsmodel3_Orchestrator59 is not None else set()
        self.wsmodel3_Orchestrator61 = wsmodel3_Orchestrator61 if wsmodel3_Orchestrator61 is not None else set()
        self.wsmodel3_Orchestrator63 = wsmodel3_Orchestrator63 if wsmodel3_Orchestrator63 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def port(self) -> str:
        return self.__port

    @port.setter
    def port(self, port: str):
        self.__port = port

    @property
    def wsmodel3_Orchestrator(self):
        return self.__wsmodel3_Orchestrator

    @wsmodel3_Orchestrator.setter
    def wsmodel3_Orchestrator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wsmodel3_Orchestrator__wsmodel3_Orchestrator", None)
        self.__wsmodel3_Orchestrator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wsmodel3_IntegrationPattern51"):
                opp_val = getattr(old_value, "wsmodel3_IntegrationPattern51", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wsmodel3_IntegrationPattern51"):
                opp_val = getattr(value, "wsmodel3_IntegrationPattern51", None)
                if opp_val is None:
                    setattr(value, "wsmodel3_IntegrationPattern51", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def wsmodel3_Orchestrator63(self):
        return self.__wsmodel3_Orchestrator63

    @wsmodel3_Orchestrator63.setter
    def wsmodel3_Orchestrator63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wsmodel3_Orchestrator__wsmodel3_Orchestrator63", None)
        self.__wsmodel3_Orchestrator63 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "wsmodel3_ExternalAPI64"):
                    opp_val = getattr(item, "wsmodel3_ExternalAPI64", None)
                    
                    if opp_val == self:
                        setattr(item, "wsmodel3_ExternalAPI64", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "wsmodel3_ExternalAPI64"):
                    opp_val = getattr(item, "wsmodel3_ExternalAPI64", None)
                    
                    setattr(item, "wsmodel3_ExternalAPI64", self)
                    

    @property
    def wsmodel3_Orchestrator61(self):
        return self.__wsmodel3_Orchestrator61

    @wsmodel3_Orchestrator61.setter
    def wsmodel3_Orchestrator61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wsmodel3_Orchestrator__wsmodel3_Orchestrator61", None)
        self.__wsmodel3_Orchestrator61 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "wsmodel3_OutputOrchestrator"):
                    opp_val = getattr(item, "wsmodel3_OutputOrchestrator", None)
                    
                    if opp_val == self:
                        setattr(item, "wsmodel3_OutputOrchestrator", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "wsmodel3_OutputOrchestrator"):
                    opp_val = getattr(item, "wsmodel3_OutputOrchestrator", None)
                    
                    setattr(item, "wsmodel3_OutputOrchestrator", self)
                    

    @property
    def wsmodel3_Orchestrator56(self):
        return self.__wsmodel3_Orchestrator56

    @wsmodel3_Orchestrator56.setter
    def wsmodel3_Orchestrator56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wsmodel3_Orchestrator__wsmodel3_Orchestrator56", None)
        self.__wsmodel3_Orchestrator56 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "wsmodel3_InputOrchestrator57"):
                    opp_val = getattr(item, "wsmodel3_InputOrchestrator57", None)
                    
                    if opp_val == self:
                        setattr(item, "wsmodel3_InputOrchestrator57", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "wsmodel3_InputOrchestrator57"):
                    opp_val = getattr(item, "wsmodel3_InputOrchestrator57", None)
                    
                    setattr(item, "wsmodel3_InputOrchestrator57", self)
                    

    @property
    def wsmodel3_Orchestrator66(self):
        return self.__wsmodel3_Orchestrator66

    @wsmodel3_Orchestrator66.setter
    def wsmodel3_Orchestrator66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wsmodel3_Orchestrator__wsmodel3_Orchestrator66", None)
        self.__wsmodel3_Orchestrator66 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "wsmodel3_REST67"):
                    opp_val = getattr(item, "wsmodel3_REST67", None)
                    
                    if opp_val == self:
                        setattr(item, "wsmodel3_REST67", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "wsmodel3_REST67"):
                    opp_val = getattr(item, "wsmodel3_REST67", None)
                    
                    setattr(item, "wsmodel3_REST67", self)
                    

    @property
    def wsmodel3_Orchestrator59(self):
        return self.__wsmodel3_Orchestrator59

    @wsmodel3_Orchestrator59.setter
    def wsmodel3_Orchestrator59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wsmodel3_Orchestrator__wsmodel3_Orchestrator59", None)
        self.__wsmodel3_Orchestrator59 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "wsmodel3_Function"):
                    opp_val = getattr(item, "wsmodel3_Function", None)
                    
                    if opp_val == self:
                        setattr(item, "wsmodel3_Function", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "wsmodel3_Function"):
                    opp_val = getattr(item, "wsmodel3_Function", None)
                    
                    setattr(item, "wsmodel3_Function", self)
                    

class wsmodel3_InputOrchestrator:

    def __init__(self, URI: str, wsmodel3_InputOrchestrator70: "wsmodel3_Function" = None, wsmodel3_InputOrchestrator: "wsmodel3_OutputBridge" = None, wsmodel3_InputOrchestrator57: "wsmodel3_Orchestrator" = None, wsmodel3_InputOrchestrator78: "wsmodel3_OutputOrchestrator" = None):
        self.URI = URI
        self.wsmodel3_InputOrchestrator70 = wsmodel3_InputOrchestrator70
        self.wsmodel3_InputOrchestrator = wsmodel3_InputOrchestrator
        self.wsmodel3_InputOrchestrator57 = wsmodel3_InputOrchestrator57
        self.wsmodel3_InputOrchestrator78 = wsmodel3_InputOrchestrator78
        
    @property
    def URI(self) -> str:
        return self.__URI

    @URI.setter
    def URI(self, URI: str):
        self.__URI = URI

    @property
    def wsmodel3_InputOrchestrator(self):
        return self.__wsmodel3_InputOrchestrator

    @wsmodel3_InputOrchestrator.setter
    def wsmodel3_InputOrchestrator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wsmodel3_InputOrchestrator__wsmodel3_InputOrchestrator", None)
        self.__wsmodel3_InputOrchestrator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wsmodel3_OutputBridge"):
                opp_val = getattr(old_value, "wsmodel3_OutputBridge", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wsmodel3_OutputBridge"):
                opp_val = getattr(value, "wsmodel3_OutputBridge", None)
                if opp_val is None:
                    setattr(value, "wsmodel3_OutputBridge", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def wsmodel3_InputOrchestrator57(self):
        return self.__wsmodel3_InputOrchestrator57

    @wsmodel3_InputOrchestrator57.setter
    def wsmodel3_InputOrchestrator57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wsmodel3_InputOrchestrator__wsmodel3_InputOrchestrator57", None)
        self.__wsmodel3_InputOrchestrator57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wsmodel3_Orchestrator56"):
                opp_val = getattr(old_value, "wsmodel3_Orchestrator56", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wsmodel3_Orchestrator56"):
                opp_val = getattr(value, "wsmodel3_Orchestrator56", None)
                if opp_val is None:
                    setattr(value, "wsmodel3_Orchestrator56", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def wsmodel3_InputOrchestrator70(self):
        return self.__wsmodel3_InputOrchestrator70

    @wsmodel3_InputOrchestrator70.setter
    def wsmodel3_InputOrchestrator70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wsmodel3_InputOrchestrator__wsmodel3_InputOrchestrator70", None)
        self.__wsmodel3_InputOrchestrator70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wsmodel3_Function69"):
                opp_val = getattr(old_value, "wsmodel3_Function69", None)
                if opp_val == self:
                    setattr(old_value, "wsmodel3_Function69", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wsmodel3_Function69"):
                opp_val = getattr(value, "wsmodel3_Function69", None)
                setattr(value, "wsmodel3_Function69", self)

    @property
    def wsmodel3_InputOrchestrator78(self):
        return self.__wsmodel3_InputOrchestrator78

    @wsmodel3_InputOrchestrator78.setter
    def wsmodel3_InputOrchestrator78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wsmodel3_InputOrchestrator__wsmodel3_InputOrchestrator78", None)
        self.__wsmodel3_InputOrchestrator78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wsmodel3_OutputOrchestrator77"):
                opp_val = getattr(old_value, "wsmodel3_OutputOrchestrator77", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wsmodel3_OutputOrchestrator77"):
                opp_val = getattr(value, "wsmodel3_OutputOrchestrator77", None)
                if opp_val is None:
                    setattr(value, "wsmodel3_OutputOrchestrator77", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class wsmodel3_Break:

    def __init__(self, expression: str, wsmodel3_Break: "wsmodel3_Function" = None):
        self.expression = expression
        self.wsmodel3_Break = wsmodel3_Break
        
    @property
    def expression(self) -> str:
        return self.__expression

    @expression.setter
    def expression(self, expression: str):
        self.__expression = expression

    @property
    def wsmodel3_Break(self):
        return self.__wsmodel3_Break

    @wsmodel3_Break.setter
    def wsmodel3_Break(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wsmodel3_Break__wsmodel3_Break", None)
        self.__wsmodel3_Break = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wsmodel3_Function75"):
                opp_val = getattr(old_value, "wsmodel3_Function75", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wsmodel3_Function75"):
                opp_val = getattr(value, "wsmodel3_Function75", None)
                if opp_val is None:
                    setattr(value, "wsmodel3_Function75", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class wsmodel3_Bridge(ABC):

    def __init__(self, topic: str, host: str, port: int, wsmodel3_Bridge: "wsmodel3_REST" = None, wsmodel3_Bridge49: "wsmodel3_MessageBroker" = None):
        self.topic = topic
        self.host = host
        self.port = port
        self.wsmodel3_Bridge = wsmodel3_Bridge
        self.wsmodel3_Bridge49 = wsmodel3_Bridge49
        
    @property
    def topic(self) -> str:
        return self.__topic

    @topic.setter
    def topic(self, topic: str):
        self.__topic = topic

    @property
    def host(self) -> str:
        return self.__host

    @host.setter
    def host(self, host: str):
        self.__host = host

    @property
    def port(self) -> int:
        return self.__port

    @port.setter
    def port(self, port: int):
        self.__port = port

    @property
    def wsmodel3_Bridge49(self):
        return self.__wsmodel3_Bridge49

    @wsmodel3_Bridge49.setter
    def wsmodel3_Bridge49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wsmodel3_Bridge__wsmodel3_Bridge49", None)
        self.__wsmodel3_Bridge49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wsmodel3_MessageBroker48"):
                opp_val = getattr(old_value, "wsmodel3_MessageBroker48", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wsmodel3_MessageBroker48"):
                opp_val = getattr(value, "wsmodel3_MessageBroker48", None)
                if opp_val is None:
                    setattr(value, "wsmodel3_MessageBroker48", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def wsmodel3_Bridge(self):
        return self.__wsmodel3_Bridge

    @wsmodel3_Bridge.setter
    def wsmodel3_Bridge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wsmodel3_Bridge__wsmodel3_Bridge", None)
        self.__wsmodel3_Bridge = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wsmodel3_REST40"):
                opp_val = getattr(old_value, "wsmodel3_REST40", None)
                if opp_val == self:
                    setattr(old_value, "wsmodel3_REST40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wsmodel3_REST40"):
                opp_val = getattr(value, "wsmodel3_REST40", None)
                setattr(value, "wsmodel3_REST40", self)

class wsmodel3_Data(ABC):

    def __init__(self, id: str, Date: str, Time: str, Location: str, Attribute: str, Artefact: str):
        self.id = id
        self.Date = Date
        self.Time = Time
        self.Location = Location
        self.Attribute = Attribute
        self.Artefact = Artefact
        
    @property
    def Date(self) -> str:
        return self.__Date

    @Date.setter
    def Date(self, Date: str):
        self.__Date = Date

    @property
    def Location(self) -> str:
        return self.__Location

    @Location.setter
    def Location(self, Location: str):
        self.__Location = Location

    @property
    def Attribute(self) -> str:
        return self.__Attribute

    @Attribute.setter
    def Attribute(self, Attribute: str):
        self.__Attribute = Attribute

    @property
    def Artefact(self) -> str:
        return self.__Artefact

    @Artefact.setter
    def Artefact(self, Artefact: str):
        self.__Artefact = Artefact

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def Time(self) -> str:
        return self.__Time

    @Time.setter
    def Time(self, Time: str):
        self.__Time = Time

class Data:

    pass
class wsmodel3_OrchestratorData(Data):

    pass
class Port:

    pass
class wsmodel3_OutputPort(Port):

    pass
class wsmodel3_InputPort(Port):

    pass
class Bridge:

    pass
class wsmodel3_OutputBridge(Bridge):

    pass
class wsmodel3_InputBridge(Bridge):

    def __init__(self, URI: str, wsmodel3_InputBridge: "wsmodel3_Actuator" = None, wsmodel3_InputBridge81: "wsmodel3_OutputOrchestrator" = None):
        self.URI = URI
        self.wsmodel3_InputBridge = wsmodel3_InputBridge
        self.wsmodel3_InputBridge81 = wsmodel3_InputBridge81
        
    @property
    def URI(self) -> str:
        return self.__URI

    @URI.setter
    def URI(self, URI: str):
        self.__URI = URI

    @property
    def wsmodel3_InputBridge(self):
        return self.__wsmodel3_InputBridge

    @wsmodel3_InputBridge.setter
    def wsmodel3_InputBridge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wsmodel3_InputBridge__wsmodel3_InputBridge", None)
        self.__wsmodel3_InputBridge = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wsmodel3_Actuator42"):
                opp_val = getattr(old_value, "wsmodel3_Actuator42", None)
                if opp_val == self:
                    setattr(old_value, "wsmodel3_Actuator42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wsmodel3_Actuator42"):
                opp_val = getattr(value, "wsmodel3_Actuator42", None)
                setattr(value, "wsmodel3_Actuator42", self)

    @property
    def wsmodel3_InputBridge81(self):
        return self.__wsmodel3_InputBridge81

    @wsmodel3_InputBridge81.setter
    def wsmodel3_InputBridge81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wsmodel3_InputBridge__wsmodel3_InputBridge81", None)
        self.__wsmodel3_InputBridge81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wsmodel3_OutputOrchestrator80"):
                opp_val = getattr(old_value, "wsmodel3_OutputOrchestrator80", None)
                if opp_val == self:
                    setattr(old_value, "wsmodel3_OutputOrchestrator80", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wsmodel3_OutputOrchestrator80"):
                opp_val = getattr(value, "wsmodel3_OutputOrchestrator80", None)
                setattr(value, "wsmodel3_OutputOrchestrator80", self)

class wsmodel3_Communication:

    def __init__(self, type: str, name: str, wsmodel3_Communication30: set["wsmodel3_CommunicationData"] = None, wsmodel3_Communication32: "wsmodel3_AccesPoint" = None, wsmodel3_Communication: "wsmodel3_Controller" = None, wsmodel3_Communication35: "wsmodel3_MessageBroker" = None):
        self.type = type
        self.name = name
        self.wsmodel3_Communication30 = wsmodel3_Communication30 if wsmodel3_Communication30 is not None else set()
        self.wsmodel3_Communication32 = wsmodel3_Communication32
        self.wsmodel3_Communication = wsmodel3_Communication
        self.wsmodel3_Communication35 = wsmodel3_Communication35
        
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
    def wsmodel3_Communication32(self):
        return self.__wsmodel3_Communication32

    @wsmodel3_Communication32.setter
    def wsmodel3_Communication32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wsmodel3_Communication__wsmodel3_Communication32", None)
        self.__wsmodel3_Communication32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wsmodel3_AccesPoint33"):
                opp_val = getattr(old_value, "wsmodel3_AccesPoint33", None)
                if opp_val == self:
                    setattr(old_value, "wsmodel3_AccesPoint33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wsmodel3_AccesPoint33"):
                opp_val = getattr(value, "wsmodel3_AccesPoint33", None)
                setattr(value, "wsmodel3_AccesPoint33", self)

    @property
    def wsmodel3_Communication30(self):
        return self.__wsmodel3_Communication30

    @wsmodel3_Communication30.setter
    def wsmodel3_Communication30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wsmodel3_Communication__wsmodel3_Communication30", None)
        self.__wsmodel3_Communication30 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "wsmodel3_CommunicationData"):
                    opp_val = getattr(item, "wsmodel3_CommunicationData", None)
                    
                    if opp_val == self:
                        setattr(item, "wsmodel3_CommunicationData", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "wsmodel3_CommunicationData"):
                    opp_val = getattr(item, "wsmodel3_CommunicationData", None)
                    
                    setattr(item, "wsmodel3_CommunicationData", self)
                    

    @property
    def wsmodel3_Communication(self):
        return self.__wsmodel3_Communication

    @wsmodel3_Communication.setter
    def wsmodel3_Communication(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wsmodel3_Communication__wsmodel3_Communication", None)
        self.__wsmodel3_Communication = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wsmodel3_Controller28"):
                opp_val = getattr(old_value, "wsmodel3_Controller28", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wsmodel3_Controller28"):
                opp_val = getattr(value, "wsmodel3_Controller28", None)
                if opp_val is None:
                    setattr(value, "wsmodel3_Controller28", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def wsmodel3_Communication35(self):
        return self.__wsmodel3_Communication35

    @wsmodel3_Communication35.setter
    def wsmodel3_Communication35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wsmodel3_Communication__wsmodel3_Communication35", None)
        self.__wsmodel3_Communication35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wsmodel3_MessageBroker36"):
                opp_val = getattr(old_value, "wsmodel3_MessageBroker36", None)
                if opp_val == self:
                    setattr(old_value, "wsmodel3_MessageBroker36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wsmodel3_MessageBroker36"):
                opp_val = getattr(value, "wsmodel3_MessageBroker36", None)
                setattr(value, "wsmodel3_MessageBroker36", self)

class wsmodel3_Port(ABC):

    def __init__(self, id: str, type: str, wsmodel3_Port: "wsmodel3_Controller" = None):
        self.id = id
        self.type = type
        self.wsmodel3_Port = wsmodel3_Port
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def wsmodel3_Port(self):
        return self.__wsmodel3_Port

    @wsmodel3_Port.setter
    def wsmodel3_Port(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wsmodel3_Port__wsmodel3_Port", None)
        self.__wsmodel3_Port = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wsmodel3_Controller"):
                opp_val = getattr(old_value, "wsmodel3_Controller", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wsmodel3_Controller"):
                opp_val = getattr(value, "wsmodel3_Controller", None)
                if opp_val is None:
                    setattr(value, "wsmodel3_Controller", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Device:

    pass
class wsmodel3_Actuator(Device):

    def __init__(self, type: str, wsmodel3_Actuator42: "wsmodel3_InputBridge" = None, wsmodel3_Actuator: "wsmodel3_OutputPort" = None):
        self.type = type
        self.wsmodel3_Actuator42 = wsmodel3_Actuator42
        self.wsmodel3_Actuator = wsmodel3_Actuator
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def wsmodel3_Actuator42(self):
        return self.__wsmodel3_Actuator42

    @wsmodel3_Actuator42.setter
    def wsmodel3_Actuator42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wsmodel3_Actuator__wsmodel3_Actuator42", None)
        self.__wsmodel3_Actuator42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wsmodel3_InputBridge"):
                opp_val = getattr(old_value, "wsmodel3_InputBridge", None)
                if opp_val == self:
                    setattr(old_value, "wsmodel3_InputBridge", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wsmodel3_InputBridge"):
                opp_val = getattr(value, "wsmodel3_InputBridge", None)
                setattr(value, "wsmodel3_InputBridge", self)

    @property
    def wsmodel3_Actuator(self):
        return self.__wsmodel3_Actuator

    @wsmodel3_Actuator.setter
    def wsmodel3_Actuator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wsmodel3_Actuator__wsmodel3_Actuator", None)
        self.__wsmodel3_Actuator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wsmodel3_OutputPort"):
                opp_val = getattr(old_value, "wsmodel3_OutputPort", None)
                if opp_val == self:
                    setattr(old_value, "wsmodel3_OutputPort", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wsmodel3_OutputPort"):
                opp_val = getattr(value, "wsmodel3_OutputPort", None)
                setattr(value, "wsmodel3_OutputPort", self)

class wsmodel3_Controller(Device):

    def __init__(self, type: str, wsmodel3_Controller: set["wsmodel3_Port"] = None, wsmodel3_Controller28: set["wsmodel3_Communication"] = None):
        self.type = type
        self.wsmodel3_Controller = wsmodel3_Controller if wsmodel3_Controller is not None else set()
        self.wsmodel3_Controller28 = wsmodel3_Controller28 if wsmodel3_Controller28 is not None else set()
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def wsmodel3_Controller(self):
        return self.__wsmodel3_Controller

    @wsmodel3_Controller.setter
    def wsmodel3_Controller(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wsmodel3_Controller__wsmodel3_Controller", None)
        self.__wsmodel3_Controller = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "wsmodel3_Port"):
                    opp_val = getattr(item, "wsmodel3_Port", None)
                    
                    if opp_val == self:
                        setattr(item, "wsmodel3_Port", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "wsmodel3_Port"):
                    opp_val = getattr(item, "wsmodel3_Port", None)
                    
                    setattr(item, "wsmodel3_Port", self)
                    

    @property
    def wsmodel3_Controller28(self):
        return self.__wsmodel3_Controller28

    @wsmodel3_Controller28.setter
    def wsmodel3_Controller28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wsmodel3_Controller__wsmodel3_Controller28", None)
        self.__wsmodel3_Controller28 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "wsmodel3_Communication"):
                    opp_val = getattr(item, "wsmodel3_Communication", None)
                    
                    if opp_val == self:
                        setattr(item, "wsmodel3_Communication", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "wsmodel3_Communication"):
                    opp_val = getattr(item, "wsmodel3_Communication", None)
                    
                    setattr(item, "wsmodel3_Communication", self)
                    

class wsmodel3_Sensor(Device):

    def __init__(self, type: str, wsmodel3_Sensor: "wsmodel3_InputPort" = None, wsmodel3_Sensor46: "wsmodel3_OutputBridge" = None):
        self.type = type
        self.wsmodel3_Sensor = wsmodel3_Sensor
        self.wsmodel3_Sensor46 = wsmodel3_Sensor46
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def wsmodel3_Sensor(self):
        return self.__wsmodel3_Sensor

    @wsmodel3_Sensor.setter
    def wsmodel3_Sensor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wsmodel3_Sensor__wsmodel3_Sensor", None)
        self.__wsmodel3_Sensor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wsmodel3_InputPort"):
                opp_val = getattr(old_value, "wsmodel3_InputPort", None)
                if opp_val == self:
                    setattr(old_value, "wsmodel3_InputPort", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wsmodel3_InputPort"):
                opp_val = getattr(value, "wsmodel3_InputPort", None)
                setattr(value, "wsmodel3_InputPort", self)

    @property
    def wsmodel3_Sensor46(self):
        return self.__wsmodel3_Sensor46

    @wsmodel3_Sensor46.setter
    def wsmodel3_Sensor46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wsmodel3_Sensor__wsmodel3_Sensor46", None)
        self.__wsmodel3_Sensor46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wsmodel3_OutputBridge45"):
                opp_val = getattr(old_value, "wsmodel3_OutputBridge45", None)
                if opp_val == self:
                    setattr(old_value, "wsmodel3_OutputBridge45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wsmodel3_OutputBridge45"):
                opp_val = getattr(value, "wsmodel3_OutputBridge45", None)
                setattr(value, "wsmodel3_OutputBridge45", self)

class wsmodel3_DeviceData(Data):

    pass
class wsmodel3_CommunicationData(Data):

    pass
class wsmodel3_REST:

    def __init__(self, URI: str, port: int, wsmodel3_REST22: "wsmodel3_Device" = None, wsmodel3_REST: "wsmodel3_WebService" = None, wsmodel3_REST40: "wsmodel3_Bridge" = None, wsmodel3_REST67: "wsmodel3_Orchestrator" = None, wsmodel3_REST86: "wsmodel3_OutputOrchestrator" = None):
        self.URI = URI
        self.port = port
        self.wsmodel3_REST22 = wsmodel3_REST22
        self.wsmodel3_REST = wsmodel3_REST
        self.wsmodel3_REST40 = wsmodel3_REST40
        self.wsmodel3_REST67 = wsmodel3_REST67
        self.wsmodel3_REST86 = wsmodel3_REST86
        
    @property
    def URI(self) -> str:
        return self.__URI

    @URI.setter
    def URI(self, URI: str):
        self.__URI = URI

    @property
    def port(self) -> int:
        return self.__port

    @port.setter
    def port(self, port: int):
        self.__port = port

    @property
    def wsmodel3_REST86(self):
        return self.__wsmodel3_REST86

    @wsmodel3_REST86.setter
    def wsmodel3_REST86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wsmodel3_REST__wsmodel3_REST86", None)
        self.__wsmodel3_REST86 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wsmodel3_OutputOrchestrator85"):
                opp_val = getattr(old_value, "wsmodel3_OutputOrchestrator85", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wsmodel3_OutputOrchestrator85"):
                opp_val = getattr(value, "wsmodel3_OutputOrchestrator85", None)
                if opp_val is None:
                    setattr(value, "wsmodel3_OutputOrchestrator85", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def wsmodel3_REST67(self):
        return self.__wsmodel3_REST67

    @wsmodel3_REST67.setter
    def wsmodel3_REST67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wsmodel3_REST__wsmodel3_REST67", None)
        self.__wsmodel3_REST67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wsmodel3_Orchestrator66"):
                opp_val = getattr(old_value, "wsmodel3_Orchestrator66", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wsmodel3_Orchestrator66"):
                opp_val = getattr(value, "wsmodel3_Orchestrator66", None)
                if opp_val is None:
                    setattr(value, "wsmodel3_Orchestrator66", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def wsmodel3_REST(self):
        return self.__wsmodel3_REST

    @wsmodel3_REST.setter
    def wsmodel3_REST(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wsmodel3_REST__wsmodel3_REST", None)
        self.__wsmodel3_REST = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wsmodel3_WebService16"):
                opp_val = getattr(old_value, "wsmodel3_WebService16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wsmodel3_WebService16"):
                opp_val = getattr(value, "wsmodel3_WebService16", None)
                if opp_val is None:
                    setattr(value, "wsmodel3_WebService16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def wsmodel3_REST40(self):
        return self.__wsmodel3_REST40

    @wsmodel3_REST40.setter
    def wsmodel3_REST40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wsmodel3_REST__wsmodel3_REST40", None)
        self.__wsmodel3_REST40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wsmodel3_Bridge"):
                opp_val = getattr(old_value, "wsmodel3_Bridge", None)
                if opp_val == self:
                    setattr(old_value, "wsmodel3_Bridge", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wsmodel3_Bridge"):
                opp_val = getattr(value, "wsmodel3_Bridge", None)
                setattr(value, "wsmodel3_Bridge", self)

    @property
    def wsmodel3_REST22(self):
        return self.__wsmodel3_REST22

    @wsmodel3_REST22.setter
    def wsmodel3_REST22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wsmodel3_REST__wsmodel3_REST22", None)
        self.__wsmodel3_REST22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wsmodel3_Device23"):
                opp_val = getattr(old_value, "wsmodel3_Device23", None)
                if opp_val == self:
                    setattr(old_value, "wsmodel3_Device23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wsmodel3_Device23"):
                opp_val = getattr(value, "wsmodel3_Device23", None)
                setattr(value, "wsmodel3_Device23", self)

class wsmodel3_Device(ABC):

    def __init__(self, name: str, wsmodel3_Device23: "wsmodel3_REST" = None, wsmodel3_Device: "wsmodel3_IoTNode" = None, wsmodel3_Device25: set["wsmodel3_DeviceData"] = None):
        self.name = name
        self.wsmodel3_Device23 = wsmodel3_Device23
        self.wsmodel3_Device = wsmodel3_Device
        self.wsmodel3_Device25 = wsmodel3_Device25 if wsmodel3_Device25 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def wsmodel3_Device(self):
        return self.__wsmodel3_Device

    @wsmodel3_Device.setter
    def wsmodel3_Device(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wsmodel3_Device__wsmodel3_Device", None)
        self.__wsmodel3_Device = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wsmodel3_IoTNode14"):
                opp_val = getattr(old_value, "wsmodel3_IoTNode14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wsmodel3_IoTNode14"):
                opp_val = getattr(value, "wsmodel3_IoTNode14", None)
                if opp_val is None:
                    setattr(value, "wsmodel3_IoTNode14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def wsmodel3_Device25(self):
        return self.__wsmodel3_Device25

    @wsmodel3_Device25.setter
    def wsmodel3_Device25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wsmodel3_Device__wsmodel3_Device25", None)
        self.__wsmodel3_Device25 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "wsmodel3_DeviceData"):
                    opp_val = getattr(item, "wsmodel3_DeviceData", None)
                    
                    if opp_val == self:
                        setattr(item, "wsmodel3_DeviceData", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "wsmodel3_DeviceData"):
                    opp_val = getattr(item, "wsmodel3_DeviceData", None)
                    
                    setattr(item, "wsmodel3_DeviceData", self)
                    

    @property
    def wsmodel3_Device23(self):
        return self.__wsmodel3_Device23

    @wsmodel3_Device23.setter
    def wsmodel3_Device23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wsmodel3_Device__wsmodel3_Device23", None)
        self.__wsmodel3_Device23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wsmodel3_REST22"):
                opp_val = getattr(old_value, "wsmodel3_REST22", None)
                if opp_val == self:
                    setattr(old_value, "wsmodel3_REST22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wsmodel3_REST22"):
                opp_val = getattr(value, "wsmodel3_REST22", None)
                setattr(value, "wsmodel3_REST22", self)

class wsmodel3_ExternalAPI:

    def __init__(self, URI: str, wsmodel3_ExternalAPI: "wsmodel3_System" = None, wsmodel3_ExternalAPI64: "wsmodel3_Orchestrator" = None, wsmodel3_ExternalAPI89: "wsmodel3_OutputOrchestrator" = None):
        self.URI = URI
        self.wsmodel3_ExternalAPI = wsmodel3_ExternalAPI
        self.wsmodel3_ExternalAPI64 = wsmodel3_ExternalAPI64
        self.wsmodel3_ExternalAPI89 = wsmodel3_ExternalAPI89
        
    @property
    def URI(self) -> str:
        return self.__URI

    @URI.setter
    def URI(self, URI: str):
        self.__URI = URI

    @property
    def wsmodel3_ExternalAPI64(self):
        return self.__wsmodel3_ExternalAPI64

    @wsmodel3_ExternalAPI64.setter
    def wsmodel3_ExternalAPI64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wsmodel3_ExternalAPI__wsmodel3_ExternalAPI64", None)
        self.__wsmodel3_ExternalAPI64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wsmodel3_Orchestrator63"):
                opp_val = getattr(old_value, "wsmodel3_Orchestrator63", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wsmodel3_Orchestrator63"):
                opp_val = getattr(value, "wsmodel3_Orchestrator63", None)
                if opp_val is None:
                    setattr(value, "wsmodel3_Orchestrator63", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def wsmodel3_ExternalAPI(self):
        return self.__wsmodel3_ExternalAPI

    @wsmodel3_ExternalAPI.setter
    def wsmodel3_ExternalAPI(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wsmodel3_ExternalAPI__wsmodel3_ExternalAPI", None)
        self.__wsmodel3_ExternalAPI = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wsmodel3_System12"):
                opp_val = getattr(old_value, "wsmodel3_System12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wsmodel3_System12"):
                opp_val = getattr(value, "wsmodel3_System12", None)
                if opp_val is None:
                    setattr(value, "wsmodel3_System12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def wsmodel3_ExternalAPI89(self):
        return self.__wsmodel3_ExternalAPI89

    @wsmodel3_ExternalAPI89.setter
    def wsmodel3_ExternalAPI89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wsmodel3_ExternalAPI__wsmodel3_ExternalAPI89", None)
        self.__wsmodel3_ExternalAPI89 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wsmodel3_OutputOrchestrator88"):
                opp_val = getattr(old_value, "wsmodel3_OutputOrchestrator88", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wsmodel3_OutputOrchestrator88"):
                opp_val = getattr(value, "wsmodel3_OutputOrchestrator88", None)
                if opp_val is None:
                    setattr(value, "wsmodel3_OutputOrchestrator88", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class wsmodel3_MessageBroker:

    def __init__(self, type: str, port: int, host: str, usser: str, pass: str, wsmodel3_MessageBroker: "wsmodel3_System" = None, wsmodel3_MessageBroker36: "wsmodel3_Communication" = None, wsmodel3_MessageBroker48: set["wsmodel3_Bridge"] = None):
        self.type = type
        self.port = port
        self.host = host
        self.usser = usser
        self.pass = pass
        self.wsmodel3_MessageBroker = wsmodel3_MessageBroker
        self.wsmodel3_MessageBroker36 = wsmodel3_MessageBroker36
        self.wsmodel3_MessageBroker48 = wsmodel3_MessageBroker48 if wsmodel3_MessageBroker48 is not None else set()
        
    @property
    def pass(self) -> str:
        return self.__pass

    @pass.setter
    def pass(self, pass: str):
        self.__pass = pass

    @property
    def port(self) -> int:
        return self.__port

    @port.setter
    def port(self, port: int):
        self.__port = port

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def host(self) -> str:
        return self.__host

    @host.setter
    def host(self, host: str):
        self.__host = host

    @property
    def usser(self) -> str:
        return self.__usser

    @usser.setter
    def usser(self, usser: str):
        self.__usser = usser

    @property
    def wsmodel3_MessageBroker(self):
        return self.__wsmodel3_MessageBroker

    @wsmodel3_MessageBroker.setter
    def wsmodel3_MessageBroker(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wsmodel3_MessageBroker__wsmodel3_MessageBroker", None)
        self.__wsmodel3_MessageBroker = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wsmodel3_System10"):
                opp_val = getattr(old_value, "wsmodel3_System10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wsmodel3_System10"):
                opp_val = getattr(value, "wsmodel3_System10", None)
                if opp_val is None:
                    setattr(value, "wsmodel3_System10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def wsmodel3_MessageBroker36(self):
        return self.__wsmodel3_MessageBroker36

    @wsmodel3_MessageBroker36.setter
    def wsmodel3_MessageBroker36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wsmodel3_MessageBroker__wsmodel3_MessageBroker36", None)
        self.__wsmodel3_MessageBroker36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wsmodel3_Communication35"):
                opp_val = getattr(old_value, "wsmodel3_Communication35", None)
                if opp_val == self:
                    setattr(old_value, "wsmodel3_Communication35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wsmodel3_Communication35"):
                opp_val = getattr(value, "wsmodel3_Communication35", None)
                setattr(value, "wsmodel3_Communication35", self)

    @property
    def wsmodel3_MessageBroker48(self):
        return self.__wsmodel3_MessageBroker48

    @wsmodel3_MessageBroker48.setter
    def wsmodel3_MessageBroker48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wsmodel3_MessageBroker__wsmodel3_MessageBroker48", None)
        self.__wsmodel3_MessageBroker48 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "wsmodel3_Bridge49"):
                    opp_val = getattr(item, "wsmodel3_Bridge49", None)
                    
                    if opp_val == self:
                        setattr(item, "wsmodel3_Bridge49", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "wsmodel3_Bridge49"):
                    opp_val = getattr(item, "wsmodel3_Bridge49", None)
                    
                    setattr(item, "wsmodel3_Bridge49", self)
                    

class wsmodel3_IntegrationPattern:

    pass
class wsmodel3_AccesPoint:

    def __init__(self, ssid: str, pass: str, wsmodel3_AccesPoint: "wsmodel3_System" = None, wsmodel3_AccesPoint33: "wsmodel3_Communication" = None):
        self.ssid = ssid
        self.pass = pass
        self.wsmodel3_AccesPoint = wsmodel3_AccesPoint
        self.wsmodel3_AccesPoint33 = wsmodel3_AccesPoint33
        
    @property
    def ssid(self) -> str:
        return self.__ssid

    @ssid.setter
    def ssid(self, ssid: str):
        self.__ssid = ssid

    @property
    def pass(self) -> str:
        return self.__pass

    @pass.setter
    def pass(self, pass: str):
        self.__pass = pass

    @property
    def wsmodel3_AccesPoint(self):
        return self.__wsmodel3_AccesPoint

    @wsmodel3_AccesPoint.setter
    def wsmodel3_AccesPoint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wsmodel3_AccesPoint__wsmodel3_AccesPoint", None)
        self.__wsmodel3_AccesPoint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wsmodel3_System6"):
                opp_val = getattr(old_value, "wsmodel3_System6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wsmodel3_System6"):
                opp_val = getattr(value, "wsmodel3_System6", None)
                if opp_val is None:
                    setattr(value, "wsmodel3_System6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def wsmodel3_AccesPoint33(self):
        return self.__wsmodel3_AccesPoint33

    @wsmodel3_AccesPoint33.setter
    def wsmodel3_AccesPoint33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wsmodel3_AccesPoint__wsmodel3_AccesPoint33", None)
        self.__wsmodel3_AccesPoint33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wsmodel3_Communication32"):
                opp_val = getattr(old_value, "wsmodel3_Communication32", None)
                if opp_val == self:
                    setattr(old_value, "wsmodel3_Communication32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wsmodel3_Communication32"):
                opp_val = getattr(value, "wsmodel3_Communication32", None)
                setattr(value, "wsmodel3_Communication32", self)

class wsmodel3_IoTNode:

    pass
class wsmodel3_Server(ABC):

    def __init__(self, host: str, wsmodel3_Server: "wsmodel3_System" = None):
        self.host = host
        self.wsmodel3_Server = wsmodel3_Server
        
    @property
    def host(self) -> str:
        return self.__host

    @host.setter
    def host(self, host: str):
        self.__host = host

    @property
    def wsmodel3_Server(self):
        return self.__wsmodel3_Server

    @wsmodel3_Server.setter
    def wsmodel3_Server(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wsmodel3_Server__wsmodel3_Server", None)
        self.__wsmodel3_Server = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wsmodel3_System2"):
                opp_val = getattr(old_value, "wsmodel3_System2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wsmodel3_System2"):
                opp_val = getattr(value, "wsmodel3_System2", None)
                if opp_val is None:
                    setattr(value, "wsmodel3_System2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class wsmodel3_WebService:

    pass
class Server:

    pass
class wsmodel3_WebServer(Server):

    pass
class wsmodel3_DBServer(Server):

    def __init__(self, usser: str, pass: str, type: str, port: int, database: str, wsmodel3_DBServer: "wsmodel3_WebService" = None):
        self.usser = usser
        self.pass = pass
        self.type = type
        self.port = port
        self.database = database
        self.wsmodel3_DBServer = wsmodel3_DBServer
        
    @property
    def port(self) -> int:
        return self.__port

    @port.setter
    def port(self, port: int):
        self.__port = port

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def pass(self) -> str:
        return self.__pass

    @pass.setter
    def pass(self, pass: str):
        self.__pass = pass

    @property
    def usser(self) -> str:
        return self.__usser

    @usser.setter
    def usser(self, usser: str):
        self.__usser = usser

    @property
    def database(self) -> str:
        return self.__database

    @database.setter
    def database(self, database: str):
        self.__database = database

    @property
    def wsmodel3_DBServer(self):
        return self.__wsmodel3_DBServer

    @wsmodel3_DBServer.setter
    def wsmodel3_DBServer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wsmodel3_DBServer__wsmodel3_DBServer", None)
        self.__wsmodel3_DBServer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wsmodel3_WebService20"):
                opp_val = getattr(old_value, "wsmodel3_WebService20", None)
                if opp_val == self:
                    setattr(old_value, "wsmodel3_WebService20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wsmodel3_WebService20"):
                opp_val = getattr(value, "wsmodel3_WebService20", None)
                setattr(value, "wsmodel3_WebService20", self)

class wsmodel3_System:

    def __init__(self, name: str, wsmodel3_System: set["wsmodel3_WebService"] = None, wsmodel3_System2: set["wsmodel3_Server"] = None, wsmodel3_System4: set["wsmodel3_IoTNode"] = None, wsmodel3_System6: set["wsmodel3_AccesPoint"] = None, wsmodel3_System8: set["wsmodel3_IntegrationPattern"] = None, wsmodel3_System10: set["wsmodel3_MessageBroker"] = None, wsmodel3_System12: set["wsmodel3_ExternalAPI"] = None):
        self.name = name
        self.wsmodel3_System = wsmodel3_System if wsmodel3_System is not None else set()
        self.wsmodel3_System2 = wsmodel3_System2 if wsmodel3_System2 is not None else set()
        self.wsmodel3_System4 = wsmodel3_System4 if wsmodel3_System4 is not None else set()
        self.wsmodel3_System6 = wsmodel3_System6 if wsmodel3_System6 is not None else set()
        self.wsmodel3_System8 = wsmodel3_System8 if wsmodel3_System8 is not None else set()
        self.wsmodel3_System10 = wsmodel3_System10 if wsmodel3_System10 is not None else set()
        self.wsmodel3_System12 = wsmodel3_System12 if wsmodel3_System12 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def wsmodel3_System12(self):
        return self.__wsmodel3_System12

    @wsmodel3_System12.setter
    def wsmodel3_System12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wsmodel3_System__wsmodel3_System12", None)
        self.__wsmodel3_System12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "wsmodel3_ExternalAPI"):
                    opp_val = getattr(item, "wsmodel3_ExternalAPI", None)
                    
                    if opp_val == self:
                        setattr(item, "wsmodel3_ExternalAPI", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "wsmodel3_ExternalAPI"):
                    opp_val = getattr(item, "wsmodel3_ExternalAPI", None)
                    
                    setattr(item, "wsmodel3_ExternalAPI", self)
                    

    @property
    def wsmodel3_System8(self):
        return self.__wsmodel3_System8

    @wsmodel3_System8.setter
    def wsmodel3_System8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wsmodel3_System__wsmodel3_System8", None)
        self.__wsmodel3_System8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "wsmodel3_IntegrationPattern"):
                    opp_val = getattr(item, "wsmodel3_IntegrationPattern", None)
                    
                    if opp_val == self:
                        setattr(item, "wsmodel3_IntegrationPattern", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "wsmodel3_IntegrationPattern"):
                    opp_val = getattr(item, "wsmodel3_IntegrationPattern", None)
                    
                    setattr(item, "wsmodel3_IntegrationPattern", self)
                    

    @property
    def wsmodel3_System4(self):
        return self.__wsmodel3_System4

    @wsmodel3_System4.setter
    def wsmodel3_System4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wsmodel3_System__wsmodel3_System4", None)
        self.__wsmodel3_System4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "wsmodel3_IoTNode"):
                    opp_val = getattr(item, "wsmodel3_IoTNode", None)
                    
                    if opp_val == self:
                        setattr(item, "wsmodel3_IoTNode", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "wsmodel3_IoTNode"):
                    opp_val = getattr(item, "wsmodel3_IoTNode", None)
                    
                    setattr(item, "wsmodel3_IoTNode", self)
                    

    @property
    def wsmodel3_System6(self):
        return self.__wsmodel3_System6

    @wsmodel3_System6.setter
    def wsmodel3_System6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wsmodel3_System__wsmodel3_System6", None)
        self.__wsmodel3_System6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "wsmodel3_AccesPoint"):
                    opp_val = getattr(item, "wsmodel3_AccesPoint", None)
                    
                    if opp_val == self:
                        setattr(item, "wsmodel3_AccesPoint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "wsmodel3_AccesPoint"):
                    opp_val = getattr(item, "wsmodel3_AccesPoint", None)
                    
                    setattr(item, "wsmodel3_AccesPoint", self)
                    

    @property
    def wsmodel3_System10(self):
        return self.__wsmodel3_System10

    @wsmodel3_System10.setter
    def wsmodel3_System10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wsmodel3_System__wsmodel3_System10", None)
        self.__wsmodel3_System10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "wsmodel3_MessageBroker"):
                    opp_val = getattr(item, "wsmodel3_MessageBroker", None)
                    
                    if opp_val == self:
                        setattr(item, "wsmodel3_MessageBroker", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "wsmodel3_MessageBroker"):
                    opp_val = getattr(item, "wsmodel3_MessageBroker", None)
                    
                    setattr(item, "wsmodel3_MessageBroker", self)
                    

    @property
    def wsmodel3_System(self):
        return self.__wsmodel3_System

    @wsmodel3_System.setter
    def wsmodel3_System(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wsmodel3_System__wsmodel3_System", None)
        self.__wsmodel3_System = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "wsmodel3_WebService"):
                    opp_val = getattr(item, "wsmodel3_WebService", None)
                    
                    if opp_val == self:
                        setattr(item, "wsmodel3_WebService", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "wsmodel3_WebService"):
                    opp_val = getattr(item, "wsmodel3_WebService", None)
                    
                    setattr(item, "wsmodel3_WebService", self)
                    

    @property
    def wsmodel3_System2(self):
        return self.__wsmodel3_System2

    @wsmodel3_System2.setter
    def wsmodel3_System2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wsmodel3_System__wsmodel3_System2", None)
        self.__wsmodel3_System2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "wsmodel3_Server"):
                    opp_val = getattr(item, "wsmodel3_Server", None)
                    
                    if opp_val == self:
                        setattr(item, "wsmodel3_Server", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "wsmodel3_Server"):
                    opp_val = getattr(item, "wsmodel3_Server", None)
                    
                    setattr(item, "wsmodel3_Server", self)
                    
