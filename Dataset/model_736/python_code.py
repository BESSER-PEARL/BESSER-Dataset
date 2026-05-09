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

class art_implem_ComponentImplementation(ABC):

    pass
class art_type_DictionaryDefaultValue:

    def __init__(self, key: str, value: str):
        self.key = key
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key


class art_implem_TypeImplementation(ABC):

    pass
class TypeImplementation:

    pass
class art_implem_OSGiType(TypeImplementation):

    def __init__(self, generateInstanceBundle: str, TypeImplementation: "art_type_ComponentType" = None):
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
class type_art_DataType:

    pass
class PortId:

    pass
class type_AbstractPort:

    pass
class CardinalityElement:

    pass
class art_type_Port(type_AbstractPort, CardinalityElement):

    def __init__(self, isOptional: str):
        self.isOptional = isOptional
        
        pass
    @property
    def isOptional(self):
        return self.__isOptional

    @isOptional.setter
    def isOptional(self, isOptional: str):
        self.__isOptional = isOptional


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
class DelegationBinding:

    pass
class ComponentInstance:

    pass
class art_instance_CompositeInstance(ComponentInstance):

    pass
class art_instance_PrimitiveInstance(ComponentInstance):

    pass
class Attribute:

    pass
class art_type_BasicAttribute(Attribute):

    def __init__(self, defaultValue: str, Attribute: "art_type_ComponentType" = None):
        self.defaultValue = defaultValue
        
        pass
    @property
    def defaultValue(self):
        return self.__defaultValue

    @defaultValue.setter
    def defaultValue(self, defaultValue: str):
        self.__defaultValue = defaultValue


class art_type_Dictionary(Attribute):

    pass
class DictionaryDefaultValue:

    pass
class art_instance_Entry(ABC):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class Dictionary:

    pass
class Entry:

    pass
class art_instance_OtherEntry(Entry):

    def __init__(self, key: str, Entry: "art_instance_DictionaryValuedAttribute" = None):
        self.key = key
        
        pass
    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key


class art_instance_DefaultEntry(Entry):

    pass
class BasicAttribute:

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
        
        pass
    @property
    def id(self):
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

class art_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class InstanceGroup:

    pass
class ComponentImplementation:

    pass
class art_implem_OSGiComponent(ComponentImplementation):

    def __init__(self, implementingClass: str, ComponentImplementation: "art_instance_ComponentInstance" = None):
        self.implementingClass = implementingClass
        
        pass
    @property
    def implementingClass(self):
        return self.__implementingClass

    @implementingClass.setter
    def implementingClass(self, implementingClass: str):
        self.__implementingClass = implementingClass


class art_implem_FractalComponent(ComponentImplementation):

    def __init__(self, controllerDesc: str, contentDesc: str, ComponentImplementation: "art_instance_ComponentInstance" = None):
        self.controllerDesc = controllerDesc
        self.contentDesc = contentDesc
        
        pass
    @property
    def controllerDesc(self):
        return self.__controllerDesc

    @controllerDesc.setter
    def controllerDesc(self, controllerDesc: str):
        self.__controllerDesc = controllerDesc


    @property
    def contentDesc(self):
        return self.__contentDesc

    @contentDesc.setter
    def contentDesc(self, contentDesc: str):
        self.__contentDesc = contentDesc


class TransmissionBinding:

    pass
class AttributeInstance:

    pass
class art_instance_ValuedAttribute(AttributeInstance):

    def __init__(self, value: str, art_instance_ValuedAttribute: "BasicAttribute" = None, AttributeInstance: "art_instance_ComponentInstance" = None):
        self.value = value
        self.art_instance_ValuedAttribute = art_instance_ValuedAttribute
        
        pass
    @property
    def value(self):
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
class art_type_FunctionalService(Service):

    pass
class art_type_ControlService(Service):

    pass
class CompositeInstance:

    pass
class ModelElement:

    pass
class art_CardinalityElement(ModelElement):

    def __init__(self, lower: str, upper: str):
        self.lower = lower
        self.upper = upper
        
        pass
    @property
    def upper(self):
        return self.__upper

    @upper.setter
    def upper(self, upper: str):
        self.__upper = upper


    @property
    def lower(self):
        return self.__lower

    @lower.setter
    def lower(self, lower: str):
        self.__lower = lower


class art_type_ComponentType(ModelElement):

    pass
class art_TypedElement(ModelElement):

    pass
class art_DataType(ModelElement):

    pass
class art_type_Service(ModelElement):

    pass
class art_type_Operation(ModelElement):

    pass
class art_instance_ComponentInstance(ModelElement):

    def __init__(self, state: str, art_instance_ComponentInstance: "ComponentType" = None, art_instance_ComponentInstance18: set["TransmissionBinding"] = None, art_instance_ComponentInstance20: "ComponentImplementation" = None, instances: set["InstanceGroup"] = None, subComponent: "CompositeInstance" = None, art_instance_ComponentInstance16: set["AttributeInstance"] = None):
        self.state = state
        self.art_instance_ComponentInstance = art_instance_ComponentInstance
        self.art_instance_ComponentInstance18 = art_instance_ComponentInstance18 if art_instance_ComponentInstance18 is not None else set()
        self.art_instance_ComponentInstance20 = art_instance_ComponentInstance20
        self.instances = instances if instances is not None else set()
        self.subComponent = subComponent
        self.art_instance_ComponentInstance16 = art_instance_ComponentInstance16 if art_instance_ComponentInstance16 is not None else set()
        
        pass
    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, state: str):
        self.__state = state


    @property
    def art_instance_ComponentInstance18(self):
        return self.__art_instance_ComponentInstance18

    @art_instance_ComponentInstance18.setter
    def art_instance_ComponentInstance18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_art_instance_ComponentInstance__art_instance_ComponentInstance18", None)
        self.__art_instance_ComponentInstance18 = value if value is not None else set()
        
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
    def art_instance_ComponentInstance16(self):
        return self.__art_instance_ComponentInstance16

    @art_instance_ComponentInstance16.setter
    def art_instance_ComponentInstance16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_art_instance_ComponentInstance__art_instance_ComponentInstance16", None)
        self.__art_instance_ComponentInstance16 = value if value is not None else set()
        
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
    def art_instance_ComponentInstance20(self):
        return self.__art_instance_ComponentInstance20

    @art_instance_ComponentInstance20.setter
    def art_instance_ComponentInstance20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_art_instance_ComponentInstance__art_instance_ComponentInstance20", None)
        self.__art_instance_ComponentInstance20 = value
        
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

    @property
    def instances(self):
        return self.__instances

    @instances.setter
    def instances(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_art_instance_ComponentInstance__instances", None)
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
    def subComponent(self):
        return self.__subComponent

    @subComponent.setter
    def subComponent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_art_instance_ComponentInstance__subComponent", None)
        self.__subComponent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompositeInstance14"):
                opp_val = getattr(old_value, "CompositeInstance14", None)
                if opp_val == self:
                    setattr(old_value, "CompositeInstance14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompositeInstance14"):
                opp_val = getattr(value, "CompositeInstance14", None)
                setattr(value, "CompositeInstance14", self)

class art_System(ModelElement):

    pass
class NamedElement:

    pass
class art_type_PortId(NamedElement):

    pass
class art_group_Group(NamedElement):

    pass
class art_type_AbstractPort(NamedElement):

    def __init__(self, role: str, art_type_AbstractPort: "Service" = None):
        self.role = role
        self.art_type_AbstractPort = art_type_AbstractPort
        
        pass
    @property
    def role(self):
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
            if hasattr(old_value, "Service53"):
                opp_val = getattr(old_value, "Service53", None)
                if opp_val == self:
                    setattr(old_value, "Service53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Service53"):
                opp_val = getattr(value, "Service53", None)
                setattr(value, "Service53", self)

class art_ModelElement(NamedElement):

    pass