from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class PortRole(Enum):
    client = "client"
    server = "server"
class InstanceState(Enum):
    OFF = "OFF"
    ON = "ON"


############################################
# Definition of Classes
############################################

class art_implem_TypeImplementation(ABC):

    pass
class art_implem_ComponentImplementation(ABC):

    pass
class art_type_DictionaryDefaultValue:

    def __init__(self, key: str, value: str):
        self.key = key
        self.value = value
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class type_art_DataType:

    pass
class PortId:

    pass
class type_AbstractPort:

    pass
class CardinalityElement:

    pass
class art_type_Port(CardinalityElement, type_AbstractPort):

    pass
class BasicAttribute:

    pass
class TypedElement:

    pass
class art_type_Attribute(TypedElement):

    pass
class art_type_Parameter(TypedElement):

    pass
class Parameter:

    pass
class Operation:

    pass
class TypeImplementation:

    pass
class art_implem_OSGiType(TypeImplementation):

    def __init__(self, generateInstanceBundle: str, TypeImplementation: "art_type_ComponentType"):
        self.generateInstanceBundle = generateInstanceBundle
        
    @property
    def generateInstanceBundle(self) -> str:
        return self.__generateInstanceBundle

    @generateInstanceBundle.setter
    def generateInstanceBundle(self, generateInstanceBundle: str):
        self.__generateInstanceBundle = generateInstanceBundle

class TypeGroup:

    pass
class Attribute:

    pass
class art_type_Dictionary(Attribute):

    pass
class art_type_BasicAttribute(Attribute):

    def __init__(self, defaultValue: str, Attribute: "art_type_ComponentType"):
        self.defaultValue = defaultValue
        
    @property
    def defaultValue(self) -> str:
        return self.__defaultValue

    @defaultValue.setter
    def defaultValue(self, defaultValue: str):
        self.__defaultValue = defaultValue

class DictionaryDefaultValue:

    pass
class art_instance_Entry(ABC):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class Dictionary:

    pass
class Entry:

    pass
class art_instance_OtherEntry(Entry):

    def __init__(self, key: str, Entry: "art_instance_DictionaryValuedAttribute"):
        self.key = key
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

class art_instance_DefaultEntry(Entry):

    pass
class art_instance_AttributeInstance(ABC):

    pass
class AbstractPort:

    pass
class art_type_PortCollection(AbstractPort):

    pass
class Binding:

    pass
class art_instance_DelegationBinding(Binding):

    pass
class art_instance_TransmissionBinding(Binding):

    pass
class art_instance_Binding(ABC):

    def __init__(self, id: str, art_instance_Binding: "ComponentInstance" = None):
        self.id = id
        self.art_instance_Binding = art_instance_Binding
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def art_instance_Binding(self):
        return self.__art_instance_Binding

    @art_instance_Binding.setter
    def art_instance_Binding(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_art_instance_Binding__art_instance_Binding", None)
        self.__art_instance_Binding = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ComponentInstance25"):
                opp_val = getattr(old_value, "ComponentInstance25", None)
                if opp_val == self:
                    setattr(old_value, "ComponentInstance25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ComponentInstance25"):
                opp_val = getattr(value, "ComponentInstance25", None)
                setattr(value, "ComponentInstance25", self)

class DelegationBinding:

    pass
class ComponentInstance:

    pass
class art_instance_CompositeInstance(ComponentInstance):

    pass
class art_instance_PrimitiveInstance(ComponentInstance):

    pass
class InstanceGroup:

    pass
class ComponentImplementation:

    pass
class art_implem_FractalComponent(ComponentImplementation):

    def __init__(self, controllerDesc: str, contentDesc: str, ComponentImplementation: "art_instance_ComponentInstance"):
        self.controllerDesc = controllerDesc
        self.contentDesc = contentDesc
        
    @property
    def contentDesc(self) -> str:
        return self.__contentDesc

    @contentDesc.setter
    def contentDesc(self, contentDesc: str):
        self.__contentDesc = contentDesc

    @property
    def controllerDesc(self) -> str:
        return self.__controllerDesc

    @controllerDesc.setter
    def controllerDesc(self, controllerDesc: str):
        self.__controllerDesc = controllerDesc

class art_implem_OSGiComponent(ComponentImplementation):

    def __init__(self, implementingClass: str, ComponentImplementation: "art_instance_ComponentInstance"):
        self.implementingClass = implementingClass
        
    @property
    def implementingClass(self) -> str:
        return self.__implementingClass

    @implementingClass.setter
    def implementingClass(self, implementingClass: str):
        self.__implementingClass = implementingClass

class TransmissionBinding:

    pass
class AttributeInstance:

    pass
class art_instance_ValuedAttribute(AttributeInstance):

    def __init__(self, value: str, art_instance_ValuedAttribute: "BasicAttribute" = None, AttributeInstance: "art_instance_ComponentInstance"):
        self.value = value
        self.art_instance_ValuedAttribute = art_instance_ValuedAttribute
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def art_instance_ValuedAttribute(self):
        return self.__art_instance_ValuedAttribute

    @art_instance_ValuedAttribute.setter
    def art_instance_ValuedAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_art_instance_ValuedAttribute__art_instance_ValuedAttribute", None)
        self.__art_instance_ValuedAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BasicAttribute"):
                opp_val = getattr(old_value, "BasicAttribute", None)
                if opp_val == self:
                    setattr(old_value, "BasicAttribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BasicAttribute"):
                opp_val = getattr(value, "BasicAttribute", None)
                setattr(value, "BasicAttribute", self)

class art_instance_DictionaryValuedAttribute(AttributeInstance):

    pass
class CompositeInstance:

    pass
class Group:

    pass
class art_group_TypeGroup(Group):

    pass
class art_group_InstanceGroup(Group):

    pass
class ComponentType:

    pass
class art_type_PrimitiveType(ComponentType):

    pass
class art_type_CompositeType(ComponentType):

    pass
class Service:

    pass
class art_type_ControlService(Service):

    pass
class art_type_FunctionalService(Service):

    pass
class Node:

    pass
class ModelElement:

    pass
class art_CardinalityElement(ModelElement):

    def __init__(self, lower: str, upper: str):
        self.lower = lower
        self.upper = upper
        
    @property
    def lower(self) -> str:
        return self.__lower

    @lower.setter
    def lower(self, lower: str):
        self.__lower = lower

    @property
    def upper(self) -> str:
        return self.__upper

    @upper.setter
    def upper(self, upper: str):
        self.__upper = upper

class art_DataType(ModelElement):

    pass
class art_type_ComponentType(ModelElement):

    pass
class art_instance_ComponentInstance(ModelElement):

    def __init__(self, state: str, art_instance_ComponentInstance: "ComponentType" = None, CompositeInstance: "CompositeInstance" = None, art_instance_ComponentInstance15: set["AttributeInstance"] = None, art_instance_ComponentInstance17: set["TransmissionBinding"] = None, art_instance_ComponentInstance19: "ComponentImplementation" = None, InstanceGroup: set["InstanceGroup"] = None):
        self.state = state
        self.art_instance_ComponentInstance = art_instance_ComponentInstance
        self.CompositeInstance = CompositeInstance
        self.art_instance_ComponentInstance15 = art_instance_ComponentInstance15 if art_instance_ComponentInstance15 is not None else set()
        self.art_instance_ComponentInstance17 = art_instance_ComponentInstance17 if art_instance_ComponentInstance17 is not None else set()
        self.art_instance_ComponentInstance19 = art_instance_ComponentInstance19
        self.InstanceGroup = InstanceGroup if InstanceGroup is not None else set()
        
    @property
    def state(self) -> str:
        return self.__state

    @state.setter
    def state(self, state: str):
        self.__state = state

    @property
    def InstanceGroup(self):
        return self.__InstanceGroup

    @InstanceGroup.setter
    def InstanceGroup(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_art_instance_ComponentInstance__InstanceGroup", None)
        self.__InstanceGroup = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "group"):
                    opp_val = getattr(item, "group", None)
                    
                    if opp_val == self:
                        setattr(item, "group", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "group"):
                    opp_val = getattr(item, "group", None)
                    
                    setattr(item, "group", self)
                    

    @property
    def art_instance_ComponentInstance17(self):
        return self.__art_instance_ComponentInstance17

    @art_instance_ComponentInstance17.setter
    def art_instance_ComponentInstance17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_art_instance_ComponentInstance__art_instance_ComponentInstance17", None)
        self.__art_instance_ComponentInstance17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TransmissionBinding"):
                    opp_val = getattr(item, "TransmissionBinding", None)
                    
                    if opp_val == self:
                        setattr(item, "TransmissionBinding", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TransmissionBinding"):
                    opp_val = getattr(item, "TransmissionBinding", None)
                    
                    setattr(item, "TransmissionBinding", self)
                    

    @property
    def CompositeInstance(self):
        return self.__CompositeInstance

    @CompositeInstance.setter
    def CompositeInstance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_art_instance_ComponentInstance__CompositeInstance", None)
        self.__CompositeInstance = value
        
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
    def art_instance_ComponentInstance15(self):
        return self.__art_instance_ComponentInstance15

    @art_instance_ComponentInstance15.setter
    def art_instance_ComponentInstance15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_art_instance_ComponentInstance__art_instance_ComponentInstance15", None)
        self.__art_instance_ComponentInstance15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AttributeInstance"):
                    opp_val = getattr(item, "AttributeInstance", None)
                    
                    if opp_val == self:
                        setattr(item, "AttributeInstance", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AttributeInstance"):
                    opp_val = getattr(item, "AttributeInstance", None)
                    
                    setattr(item, "AttributeInstance", self)
                    

    @property
    def art_instance_ComponentInstance19(self):
        return self.__art_instance_ComponentInstance19

    @art_instance_ComponentInstance19.setter
    def art_instance_ComponentInstance19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_art_instance_ComponentInstance__art_instance_ComponentInstance19", None)
        self.__art_instance_ComponentInstance19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ComponentImplementation"):
                opp_val = getattr(old_value, "ComponentImplementation", None)
                if opp_val == self:
                    setattr(old_value, "ComponentImplementation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ComponentImplementation"):
                opp_val = getattr(value, "ComponentImplementation", None)
                setattr(value, "ComponentImplementation", self)

    @property
    def art_instance_ComponentInstance(self):
        return self.__art_instance_ComponentInstance

    @art_instance_ComponentInstance.setter
    def art_instance_ComponentInstance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_art_instance_ComponentInstance__art_instance_ComponentInstance", None)
        self.__art_instance_ComponentInstance = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ComponentType12"):
                opp_val = getattr(old_value, "ComponentType12", None)
                if opp_val == self:
                    setattr(old_value, "ComponentType12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ComponentType12"):
                opp_val = getattr(value, "ComponentType12", None)
                setattr(value, "ComponentType12", self)

class art_type_Service(ModelElement):

    pass
class art_TypedElement(ModelElement):

    pass
class art_type_Operation(ModelElement):

    pass
class art_System(ModelElement):

    pass
class NamedElement:

    pass
class art_group_Group(NamedElement):

    pass
class art_type_AbstractPort(NamedElement):

    def __init__(self, role: str, protocol: str, uri: str, art_type_AbstractPort: "Service" = None):
        self.role = role
        self.protocol = protocol
        self.uri = uri
        self.art_type_AbstractPort = art_type_AbstractPort
        
    @property
    def protocol(self) -> str:
        return self.__protocol

    @protocol.setter
    def protocol(self, protocol: str):
        self.__protocol = protocol

    @property
    def uri(self) -> str:
        return self.__uri

    @uri.setter
    def uri(self, uri: str):
        self.__uri = uri

    @property
    def role(self) -> str:
        return self.__role

    @role.setter
    def role(self, role: str):
        self.__role = role

    @property
    def art_type_AbstractPort(self):
        return self.__art_type_AbstractPort

    @art_type_AbstractPort.setter
    def art_type_AbstractPort(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_art_type_AbstractPort__art_type_AbstractPort", None)
        self.__art_type_AbstractPort = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Service54"):
                opp_val = getattr(old_value, "Service54", None)
                if opp_val == self:
                    setattr(old_value, "Service54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Service54"):
                opp_val = getattr(value, "Service54", None)
                setattr(value, "Service54", self)

class art_type_PortId(NamedElement):

    pass
class art_distrib_Node(NamedElement):

    def __init__(self, uri: str, art_distrib_Node: set["ComponentInstance"] = None):
        self.uri = uri
        self.art_distrib_Node = art_distrib_Node if art_distrib_Node is not None else set()
        
    @property
    def uri(self) -> str:
        return self.__uri

    @uri.setter
    def uri(self, uri: str):
        self.__uri = uri

    @property
    def art_distrib_Node(self):
        return self.__art_distrib_Node

    @art_distrib_Node.setter
    def art_distrib_Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_art_distrib_Node__art_distrib_Node", None)
        self.__art_distrib_Node = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ComponentInstance70"):
                    opp_val = getattr(item, "ComponentInstance70", None)
                    
                    if opp_val == self:
                        setattr(item, "ComponentInstance70", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ComponentInstance70"):
                    opp_val = getattr(item, "ComponentInstance70", None)
                    
                    setattr(item, "ComponentInstance70", self)
                    

class art_ModelElement(NamedElement):

    pass
class art_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name
