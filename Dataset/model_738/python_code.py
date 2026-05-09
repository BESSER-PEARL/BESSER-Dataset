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

class type_relaxed_art_relaxed_DataType:

    pass
class DictionaryDefaultValue:

    pass
class PortId:

    pass
class type_relaxed_AbstractPort:

    pass
class CardinalityElement:

    pass
class art_relaxed_type_relaxed_Port(type_relaxed_AbstractPort, CardinalityElement):

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

    def __init__(self, generateInstanceBundle: str, TypeImplementation: "art_relaxed_type_relaxed_ComponentType" = None):
        self.generateInstanceBundle = generateInstanceBundle
        
        pass
    @property
    def generateInstanceBundle(self):
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

    def __init__(self, defaultValue: str, Attribute: "art_relaxed_type_relaxed_ComponentType" = None):
        self.defaultValue = defaultValue
        
        pass
    @property
    def defaultValue(self):
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
class art_relaxed_implem_relaxed_OSGiComponent(ComponentImplementation):

    def __init__(self, implementingClass: str, ComponentImplementation: "art_relaxed_instance_relaxed_ComponentInstance" = None):
        self.implementingClass = implementingClass
        
        pass
    @property
    def implementingClass(self):
        return self.__implementingClass

    @implementingClass.setter
    def implementingClass(self, implementingClass: str):
        self.__implementingClass = implementingClass


class art_relaxed_implem_relaxed_FractalComponent(ComponentImplementation):

    def __init__(self, controllerDesc: str, contentDesc: str, ComponentImplementation: "art_relaxed_instance_relaxed_ComponentInstance" = None):
        self.controllerDesc = controllerDesc
        self.contentDesc = contentDesc
        
        pass
    @property
    def contentDesc(self):
        return self.__contentDesc

    @contentDesc.setter
    def contentDesc(self, contentDesc: str):
        self.__contentDesc = contentDesc


    @property
    def controllerDesc(self):
        return self.__controllerDesc

    @controllerDesc.setter
    def controllerDesc(self, controllerDesc: str):
        self.__controllerDesc = controllerDesc


class TransmissionBinding:

    pass
class AttributeInstance:

    pass
class Dictionary:

    pass
class Entry:

    pass
class art_relaxed_instance_relaxed_DefaultEntry(Entry):

    pass
class art_relaxed_instance_relaxed_OtherEntry(Entry):

    def __init__(self, key: str, Entry: "art_relaxed_instance_relaxed_DictionaryValuedAttribute" = None):
        self.key = key
        
        pass
    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key


class art_relaxed_instance_relaxed_DictionaryValuedAttribute(AttributeInstance):

    pass
class BasicAttribute:

    pass
class art_relaxed_instance_relaxed_ValuedAttribute(AttributeInstance):

    def __init__(self, value: str, art_relaxed_instance_relaxed_ValuedAttribute: "BasicAttribute" = None, AttributeInstance: "art_relaxed_instance_relaxed_ComponentInstance" = None):
        self.value = value
        self.art_relaxed_instance_relaxed_ValuedAttribute = art_relaxed_instance_relaxed_ValuedAttribute
        
        pass
    @property
    def value(self):
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
class AspectModelElement:

    pass
class art_relaxed_instance_relaxed_AttributeInstance(AspectModelElement):

    pass
class art_relaxed_implem_relaxed_TypeImplementation(AspectModelElement):

    pass
class art_relaxed_implem_relaxed_ComponentImplementation(AspectModelElement):

    pass
class art_relaxed_type_relaxed_DictionaryDefaultValue(AspectModelElement):

    def __init__(self, key: str, value: str):
        self.key = key
        self.value = value
        
        pass
    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key


    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class art_relaxed_instance_relaxed_Entry(AspectModelElement):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class art_relaxed_instance_relaxed_Binding(AspectModelElement):

    def __init__(self, id: str, art_relaxed_instance_relaxed_Binding: "ComponentInstance" = None):
        self.id = id
        self.art_relaxed_instance_relaxed_Binding = art_relaxed_instance_relaxed_Binding
        
        pass
    @property
    def id(self):
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
            if hasattr(old_value, "ComponentInstance24"):
                opp_val = getattr(old_value, "ComponentInstance24", None)
                if opp_val == self:
                    setattr(old_value, "ComponentInstance24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ComponentInstance24"):
                opp_val = getattr(value, "ComponentInstance24", None)
                setattr(value, "ComponentInstance24", self)

class art_relaxed_NamedElement(AspectModelElement):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class CompositeInstance:

    pass
class art_relaxed_AspectModelElement(ABC):

    def __init__(self, pid: str):
        self.pid = pid
        
        pass
    @property
    def pid(self):
        return self.__pid

    @pid.setter
    def pid(self, pid: str):
        self.__pid = pid


class Group:

    pass
class art_relaxed_group_relaxed_TypeGroup(Group):

    pass
class art_relaxed_group_relaxed_InstanceGroup(Group):

    pass
class ComponentType:

    pass
class art_relaxed_type_relaxed_PrimitiveType(ComponentType):

    pass
class art_relaxed_type_relaxed_CompositeType(ComponentType):

    pass
class Service:

    pass
class art_relaxed_type_relaxed_ControlService(Service):

    pass
class art_relaxed_type_relaxed_FunctionalService(Service):

    pass
class Node:

    pass
class ModelElement:

    pass
class art_relaxed_type_relaxed_ComponentType(ModelElement):

    pass
class art_relaxed_type_relaxed_Operation(ModelElement):

    pass
class art_relaxed_type_relaxed_Service(ModelElement):

    pass
class art_relaxed_DataType(ModelElement):

    pass
class art_relaxed_TypedElement(ModelElement):

    pass
class art_relaxed_CardinalityElement(ModelElement):

    def __init__(self, lower: str, upper: str):
        self.lower = lower
        self.upper = upper
        
        pass
    @property
    def lower(self):
        return self.__lower

    @lower.setter
    def lower(self, lower: str):
        self.__lower = lower


    @property
    def upper(self):
        return self.__upper

    @upper.setter
    def upper(self, upper: str):
        self.__upper = upper


class art_relaxed_instance_relaxed_ComponentInstance(ModelElement):

    def __init__(self, state: str, art_relaxed_instance_relaxed_ComponentInstance: "ComponentType" = None, subComponent: "CompositeInstance" = None, art_relaxed_instance_relaxed_ComponentInstance15: set["AttributeInstance"] = None, art_relaxed_instance_relaxed_ComponentInstance17: set["TransmissionBinding"] = None, art_relaxed_instance_relaxed_ComponentInstance19: "ComponentImplementation" = None, instances: set["InstanceGroup"] = None):
        self.state = state
        self.art_relaxed_instance_relaxed_ComponentInstance = art_relaxed_instance_relaxed_ComponentInstance
        self.subComponent = subComponent
        self.art_relaxed_instance_relaxed_ComponentInstance15 = art_relaxed_instance_relaxed_ComponentInstance15 if art_relaxed_instance_relaxed_ComponentInstance15 is not None else set()
        self.art_relaxed_instance_relaxed_ComponentInstance17 = art_relaxed_instance_relaxed_ComponentInstance17 if art_relaxed_instance_relaxed_ComponentInstance17 is not None else set()
        self.art_relaxed_instance_relaxed_ComponentInstance19 = art_relaxed_instance_relaxed_ComponentInstance19
        self.instances = instances if instances is not None else set()
        
        pass
    @property
    def state(self):
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
    def instances(self):
        return self.__instances

    @instances.setter
    def instances(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_art_relaxed_instance_relaxed_ComponentInstance__instances", None)
        self.__instances = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "InstanceGroup"):
                    opp_val = getattr(item, "InstanceGroup", None)
                    
                    if opp_val == self:
                        setattr(item, "InstanceGroup", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "InstanceGroup"):
                    opp_val = getattr(item, "InstanceGroup", None)
                    
                    setattr(item, "InstanceGroup", self)
                    

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
    def subComponent(self):
        return self.__subComponent

    @subComponent.setter
    def subComponent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_art_relaxed_instance_relaxed_ComponentInstance__subComponent", None)
        self.__subComponent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompositeInstance"):
                opp_val = getattr(old_value, "CompositeInstance", None)
                if opp_val == self:
                    setattr(old_value, "CompositeInstance", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompositeInstance"):
                opp_val = getattr(value, "CompositeInstance", None)
                setattr(value, "CompositeInstance", self)

class art_relaxed_System(ModelElement):

    pass
class NamedElement:

    pass
class art_relaxed_type_relaxed_AbstractPort(NamedElement):

    def __init__(self, role: str, protocol: str, uri: str, art_relaxed_type_relaxed_AbstractPort: "Service" = None):
        self.role = role
        self.protocol = protocol
        self.uri = uri
        self.art_relaxed_type_relaxed_AbstractPort = art_relaxed_type_relaxed_AbstractPort
        
        pass
    @property
    def protocol(self):
        return self.__protocol

    @protocol.setter
    def protocol(self, protocol: str):
        self.__protocol = protocol


    @property
    def role(self):
        return self.__role

    @role.setter
    def role(self, role: str):
        self.__role = role


    @property
    def uri(self):
        return self.__uri

    @uri.setter
    def uri(self, uri: str):
        self.__uri = uri


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
            if hasattr(old_value, "Service52"):
                opp_val = getattr(old_value, "Service52", None)
                if opp_val == self:
                    setattr(old_value, "Service52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Service52"):
                opp_val = getattr(value, "Service52", None)
                setattr(value, "Service52", self)

class art_relaxed_distrib_relaxed_Node(NamedElement):

    def __init__(self, uri: str, art_relaxed_distrib_relaxed_Node: set["ComponentInstance"] = None):
        self.uri = uri
        self.art_relaxed_distrib_relaxed_Node = art_relaxed_distrib_relaxed_Node if art_relaxed_distrib_relaxed_Node is not None else set()
        
        pass
    @property
    def uri(self):
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
                if hasattr(item, "ComponentInstance68"):
                    opp_val = getattr(item, "ComponentInstance68", None)
                    
                    if opp_val == self:
                        setattr(item, "ComponentInstance68", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ComponentInstance68"):
                    opp_val = getattr(item, "ComponentInstance68", None)
                    
                    setattr(item, "ComponentInstance68", self)
                    

class art_relaxed_type_relaxed_PortId(NamedElement):

    pass
class art_relaxed_group_relaxed_Group(NamedElement):

    pass
class art_relaxed_ModelElement(NamedElement):

    pass