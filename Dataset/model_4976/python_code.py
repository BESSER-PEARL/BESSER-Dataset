from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class ElectronicDevice:

    pass
class component_diagram_Sensor(ElectronicDevice):

    def __init__(self, type: str):
        self.type = type
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class MechanicalDevice:

    pass
class component_diagram_Actuator(MechanicalDevice):

    pass
class HardwareComponent:

    pass
class component_diagram_MechanicalDevice(HardwareComponent):

    pass
class component_diagram_ElectronicDevice(HardwareComponent):

    pass
class ComponentType:

    pass
class component_diagram_SoftwareComponent(ComponentType):

    pass
class component_diagram_HardwareComponent(ComponentType):

    def __init__(self, powerSupply: str):
        self.powerSupply = powerSupply
        
    @property
    def powerSupply(self) -> str:
        return self.__powerSupply

    @powerSupply.setter
    def powerSupply(self, powerSupply: str):
        self.__powerSupply = powerSupply

class IDBase:

    pass
class component_diagram_Architecture(IDBase):

    pass
class component_diagram_PortInstance(IDBase):

    def __init__(self, name: str, PortInstance: "component_diagram_Connector" = None, port_instance: "component_diagram_PortType" = None, component_diagram_PortInstance: "component_diagram_Architecture" = None, port: "component_diagram_Connector" = None, outPorts: "component_diagram_ComponentInstance" = None, inPorts: "component_diagram_ComponentInstance" = None, PortInstance28: "component_diagram_ComponentInstance" = None, PortInstance34: "component_diagram_PortType" = None, PortInstance26: "component_diagram_ComponentInstance" = None):
        self.name = name
        self.PortInstance = PortInstance
        self.port_instance = port_instance
        self.component_diagram_PortInstance = component_diagram_PortInstance
        self.port = port
        self.outPorts = outPorts
        self.inPorts = inPorts
        self.PortInstance28 = PortInstance28
        self.PortInstance34 = PortInstance34
        self.PortInstance26 = PortInstance26
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def inPorts(self):
        return self.__inPorts

    @inPorts.setter
    def inPorts(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_component_diagram_PortInstance__inPorts", None)
        self.__inPorts = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ComponentInstance7"):
                opp_val = getattr(old_value, "ComponentInstance7", None)
                if opp_val == self:
                    setattr(old_value, "ComponentInstance7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ComponentInstance7"):
                opp_val = getattr(value, "ComponentInstance7", None)
                setattr(value, "ComponentInstance7", self)

    @property
    def component_diagram_PortInstance(self):
        return self.__component_diagram_PortInstance

    @component_diagram_PortInstance.setter
    def component_diagram_PortInstance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_component_diagram_PortInstance__component_diagram_PortInstance", None)
        self.__component_diagram_PortInstance = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "component_diagram_Architecture14"):
                opp_val = getattr(old_value, "component_diagram_Architecture14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "component_diagram_Architecture14"):
                opp_val = getattr(value, "component_diagram_Architecture14", None)
                if opp_val is None:
                    setattr(value, "component_diagram_Architecture14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def outPorts(self):
        return self.__outPorts

    @outPorts.setter
    def outPorts(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_component_diagram_PortInstance__outPorts", None)
        self.__outPorts = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ComponentInstance5"):
                opp_val = getattr(old_value, "ComponentInstance5", None)
                if opp_val == self:
                    setattr(old_value, "ComponentInstance5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ComponentInstance5"):
                opp_val = getattr(value, "ComponentInstance5", None)
                setattr(value, "ComponentInstance5", self)

    @property
    def PortInstance26(self):
        return self.__PortInstance26

    @PortInstance26.setter
    def PortInstance26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_component_diagram_PortInstance__PortInstance26", None)
        self.__PortInstance26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "inComponent"):
                opp_val = getattr(old_value, "inComponent", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "inComponent"):
                opp_val = getattr(value, "inComponent", None)
                if opp_val is None:
                    setattr(value, "inComponent", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def PortInstance28(self):
        return self.__PortInstance28

    @PortInstance28.setter
    def PortInstance28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_component_diagram_PortInstance__PortInstance28", None)
        self.__PortInstance28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outComponent"):
                opp_val = getattr(old_value, "outComponent", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outComponent"):
                opp_val = getattr(value, "outComponent", None)
                if opp_val is None:
                    setattr(value, "outComponent", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def port(self):
        return self.__port

    @port.setter
    def port(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_component_diagram_PortInstance__port", None)
        self.__port = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Connector"):
                opp_val = getattr(old_value, "Connector", None)
                if opp_val == self:
                    setattr(old_value, "Connector", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Connector"):
                opp_val = getattr(value, "Connector", None)
                setattr(value, "Connector", self)

    @property
    def port_instance(self):
        return self.__port_instance

    @port_instance.setter
    def port_instance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_component_diagram_PortInstance__port_instance", None)
        self.__port_instance = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PortType9"):
                opp_val = getattr(old_value, "PortType9", None)
                if opp_val == self:
                    setattr(old_value, "PortType9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PortType9"):
                opp_val = getattr(value, "PortType9", None)
                setattr(value, "PortType9", self)

    @property
    def PortInstance34(self):
        return self.__PortInstance34

    @PortInstance34.setter
    def PortInstance34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_component_diagram_PortInstance__PortInstance34", None)
        self.__PortInstance34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "type33"):
                opp_val = getattr(old_value, "type33", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "type33"):
                opp_val = getattr(value, "type33", None)
                if opp_val is None:
                    setattr(value, "type33", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def PortInstance(self):
        return self.__PortInstance

    @PortInstance.setter
    def PortInstance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_component_diagram_PortInstance__PortInstance", None)
        self.__PortInstance = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "connect"):
                opp_val = getattr(old_value, "connect", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "connect"):
                opp_val = getattr(value, "connect", None)
                if opp_val is None:
                    setattr(value, "connect", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class component_diagram_PortType(IDBase):

    def __init__(self, name: str, PortType: "component_diagram_ComponentType" = None, PortType9: "component_diagram_PortInstance" = None, port_types: "component_diagram_ComponentType" = None, type33: set["component_diagram_PortInstance"] = None, component_diagram_PortType: "component_diagram_Architecture" = None):
        self.name = name
        self.PortType = PortType
        self.PortType9 = PortType9
        self.port_types = port_types
        self.type33 = type33 if type33 is not None else set()
        self.component_diagram_PortType = component_diagram_PortType
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def type33(self):
        return self.__type33

    @type33.setter
    def type33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_component_diagram_PortType__type33", None)
        self.__type33 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PortInstance34"):
                    opp_val = getattr(item, "PortInstance34", None)
                    
                    if opp_val == self:
                        setattr(item, "PortInstance34", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PortInstance34"):
                    opp_val = getattr(item, "PortInstance34", None)
                    
                    setattr(item, "PortInstance34", self)
                    

    @property
    def component_diagram_PortType(self):
        return self.__component_diagram_PortType

    @component_diagram_PortType.setter
    def component_diagram_PortType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_component_diagram_PortType__component_diagram_PortType", None)
        self.__component_diagram_PortType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "component_diagram_Architecture18"):
                opp_val = getattr(old_value, "component_diagram_Architecture18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "component_diagram_Architecture18"):
                opp_val = getattr(value, "component_diagram_Architecture18", None)
                if opp_val is None:
                    setattr(value, "component_diagram_Architecture18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def port_types(self):
        return self.__port_types

    @port_types.setter
    def port_types(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_component_diagram_PortType__port_types", None)
        self.__port_types = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ComponentType31"):
                opp_val = getattr(old_value, "ComponentType31", None)
                if opp_val == self:
                    setattr(old_value, "ComponentType31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ComponentType31"):
                opp_val = getattr(value, "ComponentType31", None)
                setattr(value, "ComponentType31", self)

    @property
    def PortType9(self):
        return self.__PortType9

    @PortType9.setter
    def PortType9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_component_diagram_PortType__PortType9", None)
        self.__PortType9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "port_instance"):
                opp_val = getattr(old_value, "port_instance", None)
                if opp_val == self:
                    setattr(old_value, "port_instance", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "port_instance"):
                opp_val = getattr(value, "port_instance", None)
                setattr(value, "port_instance", self)

    @property
    def PortType(self):
        return self.__PortType

    @PortType.setter
    def PortType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_component_diagram_PortType__PortType", None)
        self.__PortType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "component_type"):
                opp_val = getattr(old_value, "component_type", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "component_type"):
                opp_val = getattr(value, "component_type", None)
                if opp_val is None:
                    setattr(value, "component_type", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class component_diagram_ComponentInstance(IDBase):

    def __init__(self, version: int, name: str, ComponentInstance: "component_diagram_ComponentType" = None, ComponentInstance5: "component_diagram_PortInstance" = None, ComponentInstance7: "component_diagram_PortInstance" = None, inComponent: set["component_diagram_PortInstance"] = None, outComponent: set["component_diagram_PortInstance"] = None, instance: "component_diagram_ComponentType" = None, component_diagram_ComponentInstance: "component_diagram_Architecture" = None, ComponentInstance21: "component_diagram_ComponentInstance" = None, parentcomponent: set["component_diagram_ComponentInstance"] = None, ComponentInstance24: "component_diagram_ComponentInstance" = None, subcomponent: "component_diagram_ComponentInstance" = None):
        self.version = version
        self.name = name
        self.ComponentInstance = ComponentInstance
        self.ComponentInstance5 = ComponentInstance5
        self.ComponentInstance7 = ComponentInstance7
        self.inComponent = inComponent if inComponent is not None else set()
        self.outComponent = outComponent if outComponent is not None else set()
        self.instance = instance
        self.component_diagram_ComponentInstance = component_diagram_ComponentInstance
        self.ComponentInstance21 = ComponentInstance21
        self.parentcomponent = parentcomponent if parentcomponent is not None else set()
        self.ComponentInstance24 = ComponentInstance24
        self.subcomponent = subcomponent
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def version(self) -> int:
        return self.__version

    @version.setter
    def version(self, version: int):
        self.__version = version

    @property
    def ComponentInstance5(self):
        return self.__ComponentInstance5

    @ComponentInstance5.setter
    def ComponentInstance5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_component_diagram_ComponentInstance__ComponentInstance5", None)
        self.__ComponentInstance5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outPorts"):
                opp_val = getattr(old_value, "outPorts", None)
                if opp_val == self:
                    setattr(old_value, "outPorts", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outPorts"):
                opp_val = getattr(value, "outPorts", None)
                setattr(value, "outPorts", self)

    @property
    def outComponent(self):
        return self.__outComponent

    @outComponent.setter
    def outComponent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_component_diagram_ComponentInstance__outComponent", None)
        self.__outComponent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PortInstance28"):
                    opp_val = getattr(item, "PortInstance28", None)
                    
                    if opp_val == self:
                        setattr(item, "PortInstance28", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PortInstance28"):
                    opp_val = getattr(item, "PortInstance28", None)
                    
                    setattr(item, "PortInstance28", self)
                    

    @property
    def instance(self):
        return self.__instance

    @instance.setter
    def instance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_component_diagram_ComponentInstance__instance", None)
        self.__instance = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ComponentType"):
                opp_val = getattr(old_value, "ComponentType", None)
                if opp_val == self:
                    setattr(old_value, "ComponentType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ComponentType"):
                opp_val = getattr(value, "ComponentType", None)
                setattr(value, "ComponentType", self)

    @property
    def parentcomponent(self):
        return self.__parentcomponent

    @parentcomponent.setter
    def parentcomponent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_component_diagram_ComponentInstance__parentcomponent", None)
        self.__parentcomponent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ComponentInstance21"):
                    opp_val = getattr(item, "ComponentInstance21", None)
                    
                    if opp_val == self:
                        setattr(item, "ComponentInstance21", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ComponentInstance21"):
                    opp_val = getattr(item, "ComponentInstance21", None)
                    
                    setattr(item, "ComponentInstance21", self)
                    

    @property
    def inComponent(self):
        return self.__inComponent

    @inComponent.setter
    def inComponent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_component_diagram_ComponentInstance__inComponent", None)
        self.__inComponent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PortInstance26"):
                    opp_val = getattr(item, "PortInstance26", None)
                    
                    if opp_val == self:
                        setattr(item, "PortInstance26", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PortInstance26"):
                    opp_val = getattr(item, "PortInstance26", None)
                    
                    setattr(item, "PortInstance26", self)
                    

    @property
    def ComponentInstance7(self):
        return self.__ComponentInstance7

    @ComponentInstance7.setter
    def ComponentInstance7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_component_diagram_ComponentInstance__ComponentInstance7", None)
        self.__ComponentInstance7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "inPorts"):
                opp_val = getattr(old_value, "inPorts", None)
                if opp_val == self:
                    setattr(old_value, "inPorts", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "inPorts"):
                opp_val = getattr(value, "inPorts", None)
                setattr(value, "inPorts", self)

    @property
    def component_diagram_ComponentInstance(self):
        return self.__component_diagram_ComponentInstance

    @component_diagram_ComponentInstance.setter
    def component_diagram_ComponentInstance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_component_diagram_ComponentInstance__component_diagram_ComponentInstance", None)
        self.__component_diagram_ComponentInstance = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "component_diagram_Architecture16"):
                opp_val = getattr(old_value, "component_diagram_Architecture16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "component_diagram_Architecture16"):
                opp_val = getattr(value, "component_diagram_Architecture16", None)
                if opp_val is None:
                    setattr(value, "component_diagram_Architecture16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ComponentInstance(self):
        return self.__ComponentInstance

    @ComponentInstance.setter
    def ComponentInstance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_component_diagram_ComponentInstance__ComponentInstance", None)
        self.__ComponentInstance = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "type"):
                opp_val = getattr(old_value, "type", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "type"):
                opp_val = getattr(value, "type", None)
                if opp_val is None:
                    setattr(value, "type", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ComponentInstance21(self):
        return self.__ComponentInstance21

    @ComponentInstance21.setter
    def ComponentInstance21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_component_diagram_ComponentInstance__ComponentInstance21", None)
        self.__ComponentInstance21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parentcomponent"):
                opp_val = getattr(old_value, "parentcomponent", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parentcomponent"):
                opp_val = getattr(value, "parentcomponent", None)
                if opp_val is None:
                    setattr(value, "parentcomponent", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def subcomponent(self):
        return self.__subcomponent

    @subcomponent.setter
    def subcomponent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_component_diagram_ComponentInstance__subcomponent", None)
        self.__subcomponent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ComponentInstance24"):
                opp_val = getattr(old_value, "ComponentInstance24", None)
                if opp_val == self:
                    setattr(old_value, "ComponentInstance24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ComponentInstance24"):
                opp_val = getattr(value, "ComponentInstance24", None)
                setattr(value, "ComponentInstance24", self)

    @property
    def ComponentInstance24(self):
        return self.__ComponentInstance24

    @ComponentInstance24.setter
    def ComponentInstance24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_component_diagram_ComponentInstance__ComponentInstance24", None)
        self.__ComponentInstance24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "subcomponent"):
                opp_val = getattr(old_value, "subcomponent", None)
                if opp_val == self:
                    setattr(old_value, "subcomponent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "subcomponent"):
                opp_val = getattr(value, "subcomponent", None)
                setattr(value, "subcomponent", self)

class component_diagram_Connector(IDBase):

    def __init__(self, name: str, connect: set["component_diagram_PortInstance"] = None, component_diagram_Connector: "component_diagram_Architecture" = None, Connector: "component_diagram_PortInstance" = None):
        self.name = name
        self.connect = connect if connect is not None else set()
        self.component_diagram_Connector = component_diagram_Connector
        self.Connector = Connector
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Connector(self):
        return self.__Connector

    @Connector.setter
    def Connector(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_component_diagram_Connector__Connector", None)
        self.__Connector = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "port"):
                opp_val = getattr(old_value, "port", None)
                if opp_val == self:
                    setattr(old_value, "port", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "port"):
                opp_val = getattr(value, "port", None)
                setattr(value, "port", self)

    @property
    def connect(self):
        return self.__connect

    @connect.setter
    def connect(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_component_diagram_Connector__connect", None)
        self.__connect = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PortInstance"):
                    opp_val = getattr(item, "PortInstance", None)
                    
                    if opp_val == self:
                        setattr(item, "PortInstance", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PortInstance"):
                    opp_val = getattr(item, "PortInstance", None)
                    
                    setattr(item, "PortInstance", self)
                    

    @property
    def component_diagram_Connector(self):
        return self.__component_diagram_Connector

    @component_diagram_Connector.setter
    def component_diagram_Connector(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_component_diagram_Connector__component_diagram_Connector", None)
        self.__component_diagram_Connector = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "component_diagram_Architecture12"):
                opp_val = getattr(old_value, "component_diagram_Architecture12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "component_diagram_Architecture12"):
                opp_val = getattr(value, "component_diagram_Architecture12", None)
                if opp_val is None:
                    setattr(value, "component_diagram_Architecture12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class component_diagram_ComponentType(IDBase):

    def __init__(self, name: str, component_type: set["component_diagram_PortType"] = None, type: set["component_diagram_ComponentInstance"] = None, component_diagram_ComponentType: "component_diagram_Architecture" = None, ComponentType: "component_diagram_ComponentInstance" = None, ComponentType31: "component_diagram_PortType" = None):
        self.name = name
        self.component_type = component_type if component_type is not None else set()
        self.type = type if type is not None else set()
        self.component_diagram_ComponentType = component_diagram_ComponentType
        self.ComponentType = ComponentType
        self.ComponentType31 = ComponentType31
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def component_diagram_ComponentType(self):
        return self.__component_diagram_ComponentType

    @component_diagram_ComponentType.setter
    def component_diagram_ComponentType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_component_diagram_ComponentType__component_diagram_ComponentType", None)
        self.__component_diagram_ComponentType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "component_diagram_Architecture"):
                opp_val = getattr(old_value, "component_diagram_Architecture", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "component_diagram_Architecture"):
                opp_val = getattr(value, "component_diagram_Architecture", None)
                if opp_val is None:
                    setattr(value, "component_diagram_Architecture", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ComponentType(self):
        return self.__ComponentType

    @ComponentType.setter
    def ComponentType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_component_diagram_ComponentType__ComponentType", None)
        self.__ComponentType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "instance"):
                opp_val = getattr(old_value, "instance", None)
                if opp_val == self:
                    setattr(old_value, "instance", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "instance"):
                opp_val = getattr(value, "instance", None)
                setattr(value, "instance", self)

    @property
    def ComponentType31(self):
        return self.__ComponentType31

    @ComponentType31.setter
    def ComponentType31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_component_diagram_ComponentType__ComponentType31", None)
        self.__ComponentType31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "port_types"):
                opp_val = getattr(old_value, "port_types", None)
                if opp_val == self:
                    setattr(old_value, "port_types", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "port_types"):
                opp_val = getattr(value, "port_types", None)
                setattr(value, "port_types", self)

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_component_diagram_ComponentType__type", None)
        self.__type = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ComponentInstance"):
                    opp_val = getattr(item, "ComponentInstance", None)
                    
                    if opp_val == self:
                        setattr(item, "ComponentInstance", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ComponentInstance"):
                    opp_val = getattr(item, "ComponentInstance", None)
                    
                    setattr(item, "ComponentInstance", self)
                    

    @property
    def component_type(self):
        return self.__component_type

    @component_type.setter
    def component_type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_component_diagram_ComponentType__component_type", None)
        self.__component_type = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PortType"):
                    opp_val = getattr(item, "PortType", None)
                    
                    if opp_val == self:
                        setattr(item, "PortType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PortType"):
                    opp_val = getattr(item, "PortType", None)
                    
                    setattr(item, "PortType", self)
                    
