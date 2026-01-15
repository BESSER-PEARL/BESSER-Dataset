from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class InstanceState(Enum):
    OFF = "OFF"
    ON = "ON"
class PortRole(Enum):
    client = "client"
    server = "server"


############################################
# Definition of Classes
############################################

class PortId:

    pass
class type_relaxed_AbstractPort:

    pass
class CardinalityElement:

    pass
class art_relaxed_type_relaxed_Port(type_relaxed_AbstractPort, CardinalityElement):

    pass
class type_relaxed_art_relaxed_DataType:

    pass
class DictionaryDefaultValue:

    pass
class Dictionary:

    pass
class Entry:

    pass
class art_relaxed_instance_relaxed_OtherEntry(Entry):

    def __init__(self, key: str, Entry: "art_relaxed_instance_relaxed_DictionaryValuedAttribute"):
        self.key = key
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

class art_relaxed_instance_relaxed_DefaultEntry(Entry):

    pass
class BasicAttribute:

    pass
class TypedElement:

    pass
class art_relaxed_type_relaxed_Attribute(TypedElement):

    pass
class art_relaxed_type_relaxed_Parameter(TypedElement):

    pass
class Parameter:

    pass
class Operation:

    pass
class TypeImplementation:

    pass
class art_relaxed_implem_relaxed_OSGiType(TypeImplementation):

    def __init__(self, generateInstanceBundle: str, TypeImplementation: "art_relaxed_type_relaxed_ComponentType"):
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
class art_relaxed_type_relaxed_Dictionary(Attribute):

    pass
class art_relaxed_type_relaxed_BasicAttribute(Attribute):

    def __init__(self, defaultValue: str, Attribute: "art_relaxed_type_relaxed_ComponentType"):
        self.defaultValue = defaultValue
        
    @property
    def defaultValue(self) -> str:
        return self.__defaultValue

    @defaultValue.setter
    def defaultValue(self, defaultValue: str):
        self.__defaultValue = defaultValue

class ComponentInstance:

    pass
class art_relaxed_instance_relaxed_CompositeInstance(ComponentInstance):

    pass
class art_relaxed_instance_relaxed_PrimitiveInstance(ComponentInstance):

    pass
class InstanceGroup:

    pass
class ComponentImplementation:

    pass
class art_relaxed_implem_relaxed_FractalComponent(ComponentImplementation):

    def __init__(self, controllerDesc: str, contentDesc: str, ComponentImplementation: "art_relaxed_instance_relaxed_ComponentInstance"):
        self.controllerDesc = controllerDesc
        self.contentDesc = contentDesc
        
    @property
    def controllerDesc(self) -> str:
        return self.__controllerDesc

    @controllerDesc.setter
    def controllerDesc(self, controllerDesc: str):
        self.__controllerDesc = controllerDesc

    @property
    def contentDesc(self) -> str:
        return self.__contentDesc

    @contentDesc.setter
    def contentDesc(self, contentDesc: str):
        self.__contentDesc = contentDesc

class art_relaxed_implem_relaxed_OSGiComponent(ComponentImplementation):

    def __init__(self, implementingClass: str, ComponentImplementation: "art_relaxed_instance_relaxed_ComponentInstance"):
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
class art_relaxed_instance_relaxed_DictionaryValuedAttribute(AttributeInstance):

    pass
class CompositeInstance:

    pass
class art_relaxed_instance_relaxed_ValuedAttribute(AttributeInstance):

    def __init__(self, value: str, art_relaxed_instance_relaxed_ValuedAttribute: "BasicAttribute" = None, AttributeInstance: "art_relaxed_instance_relaxed_ComponentInstance"):
        self.value = value
        self.art_relaxed_instance_relaxed_ValuedAttribute = art_relaxed_instance_relaxed_ValuedAttribute
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def art_relaxed_instance_relaxed_ValuedAttribute(self):
        return self.__art_relaxed_instance_relaxed_ValuedAttribute

    @art_relaxed_instance_relaxed_ValuedAttribute.setter
    def art_relaxed_instance_relaxed_ValuedAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_art_relaxed_instance_relaxed_ValuedAttribute__art_relaxed_instance_relaxed_ValuedAttribute", None)
        self.__art_relaxed_instance_relaxed_ValuedAttribute = value
        
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

class AbstractPort:

    pass
class art_relaxed_type_relaxed_PortCollection(AbstractPort):

    pass
class Binding:

    pass
class art_relaxed_instance_relaxed_DelegationBinding(Binding):

    pass
class art_relaxed_instance_relaxed_TransmissionBinding(Binding):

    pass
class DelegationBinding:

    pass
class ModelElement:

    pass
class art_relaxed_type_relaxed_Service(ModelElement):

    pass
class art_relaxed_type_relaxed_Operation(ModelElement):

    pass
class art_relaxed_instance_relaxed_ComponentInstance(ModelElement):

    def __init__(self, state: str, art_relaxed_instance_relaxed_ComponentInstance: "ComponentType" = None, CompositeInstance: "CompositeInstance" = None, art_relaxed_instance_relaxed_ComponentInstance15: set["AttributeInstance"] = None, art_relaxed_instance_relaxed_ComponentInstance17: set["TransmissionBinding"] = None, art_relaxed_instance_relaxed_ComponentInstance19: "ComponentImplementation" = None, InstanceGroup: set["InstanceGroup"] = None):
        self.state = state
        self.art_relaxed_instance_relaxed_ComponentInstance = art_relaxed_instance_relaxed_ComponentInstance
        self.CompositeInstance = CompositeInstance
        self.art_relaxed_instance_relaxed_ComponentInstance15 = art_relaxed_instance_relaxed_ComponentInstance15 if art_relaxed_instance_relaxed_ComponentInstance15 is not None else set()
        self.art_relaxed_instance_relaxed_ComponentInstance17 = art_relaxed_instance_relaxed_ComponentInstance17 if art_relaxed_instance_relaxed_ComponentInstance17 is not None else set()
        self.art_relaxed_instance_relaxed_ComponentInstance19 = art_relaxed_instance_relaxed_ComponentInstance19
        self.InstanceGroup = InstanceGroup if InstanceGroup is not None else set()
        
    @property
    def state(self) -> str:
        return self.__state

    @state.setter
    def state(self, state: str):
        self.__state = state

    @property
    def art_relaxed_instance_relaxed_ComponentInstance19(self):
        return self.__art_relaxed_instance_relaxed_ComponentInstance19

    @art_relaxed_instance_relaxed_ComponentInstance19.setter
    def art_relaxed_instance_relaxed_ComponentInstance19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_art_relaxed_instance_relaxed_ComponentInstance__art_relaxed_instance_relaxed_ComponentInstance19", None)
        self.__art_relaxed_instance_relaxed_ComponentInstance19 = value
        
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
    def InstanceGroup(self):
        return self.__InstanceGroup

    @InstanceGroup.setter
    def InstanceGroup(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_art_relaxed_instance_relaxed_ComponentInstance__InstanceGroup", None)
        self.__InstanceGroup = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "group_relaxed"):
                    opp_val = getattr(item, "group_relaxed", None)
                    
                    if opp_val == self:
                        setattr(item, "group_relaxed", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "group_relaxed"):
                    opp_val = getattr(item, "group_relaxed", None)
                    
                    setattr(item, "group_relaxed", self)
                    

    @property
    def CompositeInstance(self):
        return self.__CompositeInstance

    @CompositeInstance.setter
    def CompositeInstance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_art_relaxed_instance_relaxed_ComponentInstance__CompositeInstance", None)
        self.__CompositeInstance = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "instance_relaxed"):
                opp_val = getattr(old_value, "instance_relaxed", None)
                if opp_val == self:
                    setattr(old_value, "instance_relaxed", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "instance_relaxed"):
                opp_val = getattr(value, "instance_relaxed", None)
                setattr(value, "instance_relaxed", self)

    @property
    def art_relaxed_instance_relaxed_ComponentInstance(self):
        return self.__art_relaxed_instance_relaxed_ComponentInstance

    @art_relaxed_instance_relaxed_ComponentInstance.setter
    def art_relaxed_instance_relaxed_ComponentInstance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_art_relaxed_instance_relaxed_ComponentInstance__art_relaxed_instance_relaxed_ComponentInstance", None)
        self.__art_relaxed_instance_relaxed_ComponentInstance = value
        
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

    @property
    def art_relaxed_instance_relaxed_ComponentInstance17(self):
        return self.__art_relaxed_instance_relaxed_ComponentInstance17

    @art_relaxed_instance_relaxed_ComponentInstance17.setter
    def art_relaxed_instance_relaxed_ComponentInstance17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_art_relaxed_instance_relaxed_ComponentInstance__art_relaxed_instance_relaxed_ComponentInstance17", None)
        self.__art_relaxed_instance_relaxed_ComponentInstance17 = value if value is not None else set()
        
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
    def art_relaxed_instance_relaxed_ComponentInstance15(self):
        return self.__art_relaxed_instance_relaxed_ComponentInstance15

    @art_relaxed_instance_relaxed_ComponentInstance15.setter
    def art_relaxed_instance_relaxed_ComponentInstance15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_art_relaxed_instance_relaxed_ComponentInstance__art_relaxed_instance_relaxed_ComponentInstance15", None)
        self.__art_relaxed_instance_relaxed_ComponentInstance15 = value if value is not None else set()
        
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
                    

class art_relaxed_type_relaxed_ComponentType(ModelElement):

    pass
class art_relaxed_System(ModelElement):

    pass
class NamedElement:

    pass
class art_relaxed_type_relaxed_PortId(NamedElement):

    pass
class art_relaxed_distrib_relaxed_Node(NamedElement):

    def __init__(self, uri: str, art_relaxed_distrib_relaxed_Node: set["ComponentInstance"] = None):
        self.uri = uri
        self.art_relaxed_distrib_relaxed_Node = art_relaxed_distrib_relaxed_Node if art_relaxed_distrib_relaxed_Node is not None else set()
        
    @property
    def uri(self) -> str:
        return self.__uri

    @uri.setter
    def uri(self, uri: str):
        self.__uri = uri

    @property
    def art_relaxed_distrib_relaxed_Node(self):
        return self.__art_relaxed_distrib_relaxed_Node

    @art_relaxed_distrib_relaxed_Node.setter
    def art_relaxed_distrib_relaxed_Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_art_relaxed_distrib_relaxed_Node__art_relaxed_distrib_relaxed_Node", None)
        self.__art_relaxed_distrib_relaxed_Node = value if value is not None else set()
        
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
                    

class art_relaxed_group_relaxed_Group(NamedElement):

    pass
class art_relaxed_type_relaxed_AbstractPort(NamedElement):

    def __init__(self, role: str, protocol: str, uri: str, art_relaxed_type_relaxed_AbstractPort: "Service" = None):
        self.role = role
        self.protocol = protocol
        self.uri = uri
        self.art_relaxed_type_relaxed_AbstractPort = art_relaxed_type_relaxed_AbstractPort
        
    @property
    def uri(self) -> str:
        return self.__uri

    @uri.setter
    def uri(self, uri: str):
        self.__uri = uri

    @property
    def protocol(self) -> str:
        return self.__protocol

    @protocol.setter
    def protocol(self, protocol: str):
        self.__protocol = protocol

    @property
    def role(self) -> str:
        return self.__role

    @role.setter
    def role(self, role: str):
        self.__role = role

    @property
    def art_relaxed_type_relaxed_AbstractPort(self):
        return self.__art_relaxed_type_relaxed_AbstractPort

    @art_relaxed_type_relaxed_AbstractPort.setter
    def art_relaxed_type_relaxed_AbstractPort(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_art_relaxed_type_relaxed_AbstractPort__art_relaxed_type_relaxed_AbstractPort", None)
        self.__art_relaxed_type_relaxed_AbstractPort = value
        
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

class art_relaxed_ModelElement(NamedElement):

    pass
class AspectModelElement:

    pass
class art_relaxed_implem_relaxed_TypeImplementation(AspectModelElement):

    pass
class art_relaxed_implem_relaxed_ComponentImplementation(AspectModelElement):

    pass
class art_relaxed_instance_relaxed_AttributeInstance(AspectModelElement):

    pass
class art_relaxed_instance_relaxed_Entry(AspectModelElement):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class art_relaxed_type_relaxed_DictionaryDefaultValue(AspectModelElement):

    def __init__(self, key: str, value: str):
        self.key = key
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

class art_relaxed_instance_relaxed_Binding(AspectModelElement):

    def __init__(self, id: str, art_relaxed_instance_relaxed_Binding: "ComponentInstance" = None):
        self.id = id
        self.art_relaxed_instance_relaxed_Binding = art_relaxed_instance_relaxed_Binding
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def art_relaxed_instance_relaxed_Binding(self):
        return self.__art_relaxed_instance_relaxed_Binding

    @art_relaxed_instance_relaxed_Binding.setter
    def art_relaxed_instance_relaxed_Binding(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_art_relaxed_instance_relaxed_Binding__art_relaxed_instance_relaxed_Binding", None)
        self.__art_relaxed_instance_relaxed_Binding = value
        
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

class art_relaxed_NamedElement(AspectModelElement):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class art_relaxed_AspectModelElement(ABC):

    def __init__(self, pid: str):
        self.pid = pid
        
    @property
    def pid(self) -> str:
        return self.__pid

    @pid.setter
    def pid(self, pid: str):
        self.__pid = pid

class art_relaxed_CardinalityElement(ModelElement):

    def __init__(self, lower: str, upper: str):
        self.lower = lower
        self.upper = upper
        
    @property
    def upper(self) -> str:
        return self.__upper

    @upper.setter
    def upper(self, upper: str):
        self.__upper = upper

    @property
    def lower(self) -> str:
        return self.__lower

    @lower.setter
    def lower(self, lower: str):
        self.__lower = lower

class art_relaxed_TypedElement(ModelElement):

    pass
class Group:

    pass
class art_relaxed_group_relaxed_InstanceGroup(Group):

    pass
class art_relaxed_group_relaxed_TypeGroup(Group):

    pass
class art_relaxed_DataType(ModelElement):

    pass
class ComponentType:

    pass
class art_relaxed_type_relaxed_PrimitiveType(ComponentType):

    pass
class art_relaxed_type_relaxed_CompositeType(ComponentType):

    pass
class Service:

    pass
class art_relaxed_type_relaxed_FunctionalService(Service):

    pass
class art_relaxed_type_relaxed_ControlService(Service):

    pass
class Node:

    pass