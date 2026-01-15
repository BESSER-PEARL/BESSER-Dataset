from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Port:

    pass
class componentmodel_OutPort(Port):

    pass
class componentmodel_InPort(Port):

    pass
class Property:

    pass
class componentmodel_EnumProperty(Property):

    def __init__(self, literalValue: str):
        self.literalValue = literalValue
        
    @property
    def literalValue(self) -> str:
        return self.__literalValue

    @literalValue.setter
    def literalValue(self, literalValue: str):
        self.__literalValue = literalValue

class componentmodel_NumericProperty(Property):

    def __init__(self, minValue: float, maxValue: float, defaultValue: float):
        self.minValue = minValue
        self.maxValue = maxValue
        self.defaultValue = defaultValue
        
    @property
    def maxValue(self) -> float:
        return self.__maxValue

    @maxValue.setter
    def maxValue(self, maxValue: float):
        self.__maxValue = maxValue

    @property
    def minValue(self) -> float:
        return self.__minValue

    @minValue.setter
    def minValue(self, minValue: float):
        self.__minValue = minValue

    @property
    def defaultValue(self) -> float:
        return self.__defaultValue

    @defaultValue.setter
    def defaultValue(self, defaultValue: float):
        self.__defaultValue = defaultValue

class componentmodel_Property(ABC):

    def __init__(self, description: str, name: str, componentmodel_Property: "componentmodel_PrimitiveComponent" = None):
        self.description = description
        self.name = name
        self.componentmodel_Property = componentmodel_Property
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def componentmodel_Property(self):
        return self.__componentmodel_Property

    @componentmodel_Property.setter
    def componentmodel_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_componentmodel_Property__componentmodel_Property", None)
        self.__componentmodel_Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "componentmodel_PrimitiveComponent"):
                opp_val = getattr(old_value, "componentmodel_PrimitiveComponent", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "componentmodel_PrimitiveComponent"):
                opp_val = getattr(value, "componentmodel_PrimitiveComponent", None)
                if opp_val is None:
                    setattr(value, "componentmodel_PrimitiveComponent", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Component:

    pass
class componentmodel_CompositeComponent(Component):

    pass
class componentmodel_PrimitiveComponent(Component):

    pass
class componentmodel_Port(ABC):

    def __init__(self, type: str, typePackage: str, name: str, description: str, componentmodel_Port: "componentmodel_Component" = None):
        self.type = type
        self.typePackage = typePackage
        self.name = name
        self.description = description
        self.componentmodel_Port = componentmodel_Port
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def typePackage(self) -> str:
        return self.__typePackage

    @typePackage.setter
    def typePackage(self, typePackage: str):
        self.__typePackage = typePackage

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def componentmodel_Port(self):
        return self.__componentmodel_Port

    @componentmodel_Port.setter
    def componentmodel_Port(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_componentmodel_Port__componentmodel_Port", None)
        self.__componentmodel_Port = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "componentmodel_Component"):
                opp_val = getattr(old_value, "componentmodel_Component", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "componentmodel_Component"):
                opp_val = getattr(value, "componentmodel_Component", None)
                if opp_val is None:
                    setattr(value, "componentmodel_Component", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class componentmodel_Component(ABC):

    def __init__(self, name: str, description: str, componentmodel_Component: set["componentmodel_Port"] = None, componentmodel_Component3: "componentmodel_CompositeComponent" = None):
        self.name = name
        self.description = description
        self.componentmodel_Component = componentmodel_Component if componentmodel_Component is not None else set()
        self.componentmodel_Component3 = componentmodel_Component3
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def componentmodel_Component(self):
        return self.__componentmodel_Component

    @componentmodel_Component.setter
    def componentmodel_Component(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_componentmodel_Component__componentmodel_Component", None)
        self.__componentmodel_Component = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "componentmodel_Port"):
                    opp_val = getattr(item, "componentmodel_Port", None)
                    
                    if opp_val == self:
                        setattr(item, "componentmodel_Port", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "componentmodel_Port"):
                    opp_val = getattr(item, "componentmodel_Port", None)
                    
                    setattr(item, "componentmodel_Port", self)
                    

    @property
    def componentmodel_Component3(self):
        return self.__componentmodel_Component3

    @componentmodel_Component3.setter
    def componentmodel_Component3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_componentmodel_Component__componentmodel_Component3", None)
        self.__componentmodel_Component3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "componentmodel_CompositeComponent"):
                opp_val = getattr(old_value, "componentmodel_CompositeComponent", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "componentmodel_CompositeComponent"):
                opp_val = getattr(value, "componentmodel_CompositeComponent", None)
                if opp_val is None:
                    setattr(value, "componentmodel_CompositeComponent", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
