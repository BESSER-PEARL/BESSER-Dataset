from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class architectureTool_Method:

    def __init__(self, name: str, returnType: str, visable: str, parameter: str, architectureTool_Method: "architectureTool_classMember" = None):
        self.name = name
        self.returnType = returnType
        self.visable = visable
        self.parameter = parameter
        self.architectureTool_Method = architectureTool_Method
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def returnType(self) -> str:
        return self.__returnType

    @returnType.setter
    def returnType(self, returnType: str):
        self.__returnType = returnType

    @property
    def parameter(self) -> str:
        return self.__parameter

    @parameter.setter
    def parameter(self, parameter: str):
        self.__parameter = parameter

    @property
    def visable(self) -> str:
        return self.__visable

    @visable.setter
    def visable(self, visable: str):
        self.__visable = visable

    @property
    def architectureTool_Method(self):
        return self.__architectureTool_Method

    @architectureTool_Method.setter
    def architectureTool_Method(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_architectureTool_Method__architectureTool_Method", None)
        self.__architectureTool_Method = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "architectureTool_classMember66"):
                opp_val = getattr(old_value, "architectureTool_classMember66", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "architectureTool_classMember66"):
                opp_val = getattr(value, "architectureTool_classMember66", None)
                if opp_val is None:
                    setattr(value, "architectureTool_classMember66", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class architectureTool_Attribute:

    def __init__(self, name: str, type: str, Visable: str, architectureTool_Attribute: "architectureTool_classMember" = None):
        self.name = name
        self.type = type
        self.Visable = Visable
        self.architectureTool_Attribute = architectureTool_Attribute
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Visable(self) -> str:
        return self.__Visable

    @Visable.setter
    def Visable(self, Visable: str):
        self.__Visable = Visable

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def architectureTool_Attribute(self):
        return self.__architectureTool_Attribute

    @architectureTool_Attribute.setter
    def architectureTool_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_architectureTool_Attribute__architectureTool_Attribute", None)
        self.__architectureTool_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "architectureTool_classMember"):
                opp_val = getattr(old_value, "architectureTool_classMember", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "architectureTool_classMember"):
                opp_val = getattr(value, "architectureTool_classMember", None)
                if opp_val is None:
                    setattr(value, "architectureTool_classMember", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class architectureTool_classMember(ABC):

    def __init__(self, name: str, architectureTool_classMember: set["architectureTool_Attribute"] = None, architectureTool_classMember66: set["architectureTool_Method"] = None):
        self.name = name
        self.architectureTool_classMember = architectureTool_classMember if architectureTool_classMember is not None else set()
        self.architectureTool_classMember66 = architectureTool_classMember66 if architectureTool_classMember66 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def architectureTool_classMember(self):
        return self.__architectureTool_classMember

    @architectureTool_classMember.setter
    def architectureTool_classMember(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_architectureTool_classMember__architectureTool_classMember", None)
        self.__architectureTool_classMember = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "architectureTool_Attribute"):
                    opp_val = getattr(item, "architectureTool_Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "architectureTool_Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "architectureTool_Attribute"):
                    opp_val = getattr(item, "architectureTool_Attribute", None)
                    
                    setattr(item, "architectureTool_Attribute", self)
                    

    @property
    def architectureTool_classMember66(self):
        return self.__architectureTool_classMember66

    @architectureTool_classMember66.setter
    def architectureTool_classMember66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_architectureTool_classMember__architectureTool_classMember66", None)
        self.__architectureTool_classMember66 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "architectureTool_Method"):
                    opp_val = getattr(item, "architectureTool_Method", None)
                    
                    if opp_val == self:
                        setattr(item, "architectureTool_Method", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "architectureTool_Method"):
                    opp_val = getattr(item, "architectureTool_Method", None)
                    
                    setattr(item, "architectureTool_Method", self)
                    

class classMember:

    pass
class architectureTool_System:

    def __init__(self, name: str, architectureTool_System: "architectureTool_System" = None, architectureTool_System27: set["architectureTool_System"] = None, architectureTool_System30: set["architectureTool_Component"] = None, architectureTool_System33: set["architectureTool_Port"] = None, architectureTool_System37: "architectureTool_System" = None, architectureTool_System35: set["architectureTool_System"] = None, architectureTool_System39: set["architectureTool_Interface"] = None, ComponentDependence42: set["architectureTool_Component"] = None, System: "architectureTool_Component" = None):
        self.name = name
        self.architectureTool_System = architectureTool_System
        self.architectureTool_System27 = architectureTool_System27 if architectureTool_System27 is not None else set()
        self.architectureTool_System30 = architectureTool_System30 if architectureTool_System30 is not None else set()
        self.architectureTool_System33 = architectureTool_System33 if architectureTool_System33 is not None else set()
        self.architectureTool_System37 = architectureTool_System37
        self.architectureTool_System35 = architectureTool_System35 if architectureTool_System35 is not None else set()
        self.architectureTool_System39 = architectureTool_System39 if architectureTool_System39 is not None else set()
        self.ComponentDependence42 = ComponentDependence42 if ComponentDependence42 is not None else set()
        self.System = System
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def architectureTool_System30(self):
        return self.__architectureTool_System30

    @architectureTool_System30.setter
    def architectureTool_System30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_architectureTool_System__architectureTool_System30", None)
        self.__architectureTool_System30 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "architectureTool_Component31"):
                    opp_val = getattr(item, "architectureTool_Component31", None)
                    
                    if opp_val == self:
                        setattr(item, "architectureTool_Component31", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "architectureTool_Component31"):
                    opp_val = getattr(item, "architectureTool_Component31", None)
                    
                    setattr(item, "architectureTool_Component31", self)
                    

    @property
    def architectureTool_System39(self):
        return self.__architectureTool_System39

    @architectureTool_System39.setter
    def architectureTool_System39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_architectureTool_System__architectureTool_System39", None)
        self.__architectureTool_System39 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "architectureTool_Interface40"):
                    opp_val = getattr(item, "architectureTool_Interface40", None)
                    
                    if opp_val == self:
                        setattr(item, "architectureTool_Interface40", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "architectureTool_Interface40"):
                    opp_val = getattr(item, "architectureTool_Interface40", None)
                    
                    setattr(item, "architectureTool_Interface40", self)
                    

    @property
    def System(self):
        return self.__System

    @System.setter
    def System(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_architectureTool_System__System", None)
        self.__System = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ComponentDependence"):
                opp_val = getattr(old_value, "ComponentDependence", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ComponentDependence"):
                opp_val = getattr(value, "ComponentDependence", None)
                if opp_val is None:
                    setattr(value, "ComponentDependence", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def architectureTool_System37(self):
        return self.__architectureTool_System37

    @architectureTool_System37.setter
    def architectureTool_System37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_architectureTool_System__architectureTool_System37", None)
        self.__architectureTool_System37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "architectureTool_System35"):
                opp_val = getattr(old_value, "architectureTool_System35", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "architectureTool_System35"):
                opp_val = getattr(value, "architectureTool_System35", None)
                if opp_val is None:
                    setattr(value, "architectureTool_System35", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def architectureTool_System35(self):
        return self.__architectureTool_System35

    @architectureTool_System35.setter
    def architectureTool_System35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_architectureTool_System__architectureTool_System35", None)
        self.__architectureTool_System35 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "architectureTool_System37"):
                    opp_val = getattr(item, "architectureTool_System37", None)
                    
                    if opp_val == self:
                        setattr(item, "architectureTool_System37", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "architectureTool_System37"):
                    opp_val = getattr(item, "architectureTool_System37", None)
                    
                    setattr(item, "architectureTool_System37", self)
                    

    @property
    def architectureTool_System27(self):
        return self.__architectureTool_System27

    @architectureTool_System27.setter
    def architectureTool_System27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_architectureTool_System__architectureTool_System27", None)
        self.__architectureTool_System27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "architectureTool_System"):
                    opp_val = getattr(item, "architectureTool_System", None)
                    
                    if opp_val == self:
                        setattr(item, "architectureTool_System", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "architectureTool_System"):
                    opp_val = getattr(item, "architectureTool_System", None)
                    
                    setattr(item, "architectureTool_System", self)
                    

    @property
    def architectureTool_System(self):
        return self.__architectureTool_System

    @architectureTool_System.setter
    def architectureTool_System(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_architectureTool_System__architectureTool_System", None)
        self.__architectureTool_System = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "architectureTool_System27"):
                opp_val = getattr(old_value, "architectureTool_System27", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "architectureTool_System27"):
                opp_val = getattr(value, "architectureTool_System27", None)
                if opp_val is None:
                    setattr(value, "architectureTool_System27", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ComponentDependence42(self):
        return self.__ComponentDependence42

    @ComponentDependence42.setter
    def ComponentDependence42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_architectureTool_System__ComponentDependence42", None)
        self.__ComponentDependence42 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Component"):
                    opp_val = getattr(item, "Component", None)
                    
                    if opp_val == self:
                        setattr(item, "Component", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Component"):
                    opp_val = getattr(item, "Component", None)
                    
                    setattr(item, "Component", self)
                    

    @property
    def architectureTool_System33(self):
        return self.__architectureTool_System33

    @architectureTool_System33.setter
    def architectureTool_System33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_architectureTool_System__architectureTool_System33", None)
        self.__architectureTool_System33 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "architectureTool_Port34"):
                    opp_val = getattr(item, "architectureTool_Port34", None)
                    
                    if opp_val == self:
                        setattr(item, "architectureTool_Port34", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "architectureTool_Port34"):
                    opp_val = getattr(item, "architectureTool_Port34", None)
                    
                    setattr(item, "architectureTool_Port34", self)
                    

class architectureTool_Interface(classMember):

    pass
class architectureTool_Class(classMember):

    pass
class architectureTool_Port(ABC):

    def __init__(self, type: str, simple: str, provided: str, required: str, name: str, architectureTool_Port: "architectureTool_Component" = None, architectureTool_Port34: "architectureTool_System" = None, architectureTool_Port44: set["architectureTool_Interface"] = None, architectureTool_Port48: "architectureTool_Port" = None, architectureTool_Port46: set["architectureTool_Port"] = None, architectureTool_Port50: set["architectureTool_Interface"] = None, architectureTool_Port54: "architectureTool_Interface" = None, architectureTool_Port63: "architectureTool_Interface" = None):
        self.type = type
        self.simple = simple
        self.provided = provided
        self.required = required
        self.name = name
        self.architectureTool_Port = architectureTool_Port
        self.architectureTool_Port34 = architectureTool_Port34
        self.architectureTool_Port44 = architectureTool_Port44 if architectureTool_Port44 is not None else set()
        self.architectureTool_Port48 = architectureTool_Port48
        self.architectureTool_Port46 = architectureTool_Port46 if architectureTool_Port46 is not None else set()
        self.architectureTool_Port50 = architectureTool_Port50 if architectureTool_Port50 is not None else set()
        self.architectureTool_Port54 = architectureTool_Port54
        self.architectureTool_Port63 = architectureTool_Port63
        
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
    def required(self) -> str:
        return self.__required

    @required.setter
    def required(self, required: str):
        self.__required = required

    @property
    def simple(self) -> str:
        return self.__simple

    @simple.setter
    def simple(self, simple: str):
        self.__simple = simple

    @property
    def provided(self) -> str:
        return self.__provided

    @provided.setter
    def provided(self, provided: str):
        self.__provided = provided

    @property
    def architectureTool_Port63(self):
        return self.__architectureTool_Port63

    @architectureTool_Port63.setter
    def architectureTool_Port63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_architectureTool_Port__architectureTool_Port63", None)
        self.__architectureTool_Port63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "architectureTool_Interface62"):
                opp_val = getattr(old_value, "architectureTool_Interface62", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "architectureTool_Interface62"):
                opp_val = getattr(value, "architectureTool_Interface62", None)
                if opp_val is None:
                    setattr(value, "architectureTool_Interface62", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def architectureTool_Port44(self):
        return self.__architectureTool_Port44

    @architectureTool_Port44.setter
    def architectureTool_Port44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_architectureTool_Port__architectureTool_Port44", None)
        self.__architectureTool_Port44 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "architectureTool_Interface45"):
                    opp_val = getattr(item, "architectureTool_Interface45", None)
                    
                    if opp_val == self:
                        setattr(item, "architectureTool_Interface45", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "architectureTool_Interface45"):
                    opp_val = getattr(item, "architectureTool_Interface45", None)
                    
                    setattr(item, "architectureTool_Interface45", self)
                    

    @property
    def architectureTool_Port46(self):
        return self.__architectureTool_Port46

    @architectureTool_Port46.setter
    def architectureTool_Port46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_architectureTool_Port__architectureTool_Port46", None)
        self.__architectureTool_Port46 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "architectureTool_Port48"):
                    opp_val = getattr(item, "architectureTool_Port48", None)
                    
                    if opp_val == self:
                        setattr(item, "architectureTool_Port48", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "architectureTool_Port48"):
                    opp_val = getattr(item, "architectureTool_Port48", None)
                    
                    setattr(item, "architectureTool_Port48", self)
                    

    @property
    def architectureTool_Port54(self):
        return self.__architectureTool_Port54

    @architectureTool_Port54.setter
    def architectureTool_Port54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_architectureTool_Port__architectureTool_Port54", None)
        self.__architectureTool_Port54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "architectureTool_Interface53"):
                opp_val = getattr(old_value, "architectureTool_Interface53", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "architectureTool_Interface53"):
                opp_val = getattr(value, "architectureTool_Interface53", None)
                if opp_val is None:
                    setattr(value, "architectureTool_Interface53", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def architectureTool_Port50(self):
        return self.__architectureTool_Port50

    @architectureTool_Port50.setter
    def architectureTool_Port50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_architectureTool_Port__architectureTool_Port50", None)
        self.__architectureTool_Port50 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "architectureTool_Interface51"):
                    opp_val = getattr(item, "architectureTool_Interface51", None)
                    
                    if opp_val == self:
                        setattr(item, "architectureTool_Interface51", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "architectureTool_Interface51"):
                    opp_val = getattr(item, "architectureTool_Interface51", None)
                    
                    setattr(item, "architectureTool_Interface51", self)
                    

    @property
    def architectureTool_Port(self):
        return self.__architectureTool_Port

    @architectureTool_Port.setter
    def architectureTool_Port(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_architectureTool_Port__architectureTool_Port", None)
        self.__architectureTool_Port = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "architectureTool_Component"):
                opp_val = getattr(old_value, "architectureTool_Component", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "architectureTool_Component"):
                opp_val = getattr(value, "architectureTool_Component", None)
                if opp_val is None:
                    setattr(value, "architectureTool_Component", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def architectureTool_Port34(self):
        return self.__architectureTool_Port34

    @architectureTool_Port34.setter
    def architectureTool_Port34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_architectureTool_Port__architectureTool_Port34", None)
        self.__architectureTool_Port34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "architectureTool_System33"):
                opp_val = getattr(old_value, "architectureTool_System33", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "architectureTool_System33"):
                opp_val = getattr(value, "architectureTool_System33", None)
                if opp_val is None:
                    setattr(value, "architectureTool_System33", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def architectureTool_Port48(self):
        return self.__architectureTool_Port48

    @architectureTool_Port48.setter
    def architectureTool_Port48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_architectureTool_Port__architectureTool_Port48", None)
        self.__architectureTool_Port48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "architectureTool_Port46"):
                opp_val = getattr(old_value, "architectureTool_Port46", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "architectureTool_Port46"):
                opp_val = getattr(value, "architectureTool_Port46", None)
                if opp_val is None:
                    setattr(value, "architectureTool_Port46", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class architectureTool_Component:

    def __init__(self, name: str, architectureTool_Component: set["architectureTool_Port"] = None, architectureTool_Component3: "architectureTool_Component" = None, architectureTool_Component1: set["architectureTool_Component"] = None, architectureTool_Component5: set["architectureTool_Class"] = None, architectureTool_Component8: "architectureTool_Component" = None, architectureTool_Component6: set["architectureTool_Component"] = None, architectureTool_Component10: set["architectureTool_Interface"] = None, architectureTool_Component31: "architectureTool_System" = None, Component: "architectureTool_System" = None, ComponentDependence: set["architectureTool_System"] = None):
        self.name = name
        self.architectureTool_Component = architectureTool_Component if architectureTool_Component is not None else set()
        self.architectureTool_Component3 = architectureTool_Component3
        self.architectureTool_Component1 = architectureTool_Component1 if architectureTool_Component1 is not None else set()
        self.architectureTool_Component5 = architectureTool_Component5 if architectureTool_Component5 is not None else set()
        self.architectureTool_Component8 = architectureTool_Component8
        self.architectureTool_Component6 = architectureTool_Component6 if architectureTool_Component6 is not None else set()
        self.architectureTool_Component10 = architectureTool_Component10 if architectureTool_Component10 is not None else set()
        self.architectureTool_Component31 = architectureTool_Component31
        self.Component = Component
        self.ComponentDependence = ComponentDependence if ComponentDependence is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def architectureTool_Component6(self):
        return self.__architectureTool_Component6

    @architectureTool_Component6.setter
    def architectureTool_Component6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_architectureTool_Component__architectureTool_Component6", None)
        self.__architectureTool_Component6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "architectureTool_Component8"):
                    opp_val = getattr(item, "architectureTool_Component8", None)
                    
                    if opp_val == self:
                        setattr(item, "architectureTool_Component8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "architectureTool_Component8"):
                    opp_val = getattr(item, "architectureTool_Component8", None)
                    
                    setattr(item, "architectureTool_Component8", self)
                    

    @property
    def Component(self):
        return self.__Component

    @Component.setter
    def Component(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_architectureTool_Component__Component", None)
        self.__Component = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ComponentDependence42"):
                opp_val = getattr(old_value, "ComponentDependence42", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ComponentDependence42"):
                opp_val = getattr(value, "ComponentDependence42", None)
                if opp_val is None:
                    setattr(value, "ComponentDependence42", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ComponentDependence(self):
        return self.__ComponentDependence

    @ComponentDependence.setter
    def ComponentDependence(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_architectureTool_Component__ComponentDependence", None)
        self.__ComponentDependence = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "System"):
                    opp_val = getattr(item, "System", None)
                    
                    if opp_val == self:
                        setattr(item, "System", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "System"):
                    opp_val = getattr(item, "System", None)
                    
                    setattr(item, "System", self)
                    

    @property
    def architectureTool_Component8(self):
        return self.__architectureTool_Component8

    @architectureTool_Component8.setter
    def architectureTool_Component8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_architectureTool_Component__architectureTool_Component8", None)
        self.__architectureTool_Component8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "architectureTool_Component6"):
                opp_val = getattr(old_value, "architectureTool_Component6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "architectureTool_Component6"):
                opp_val = getattr(value, "architectureTool_Component6", None)
                if opp_val is None:
                    setattr(value, "architectureTool_Component6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def architectureTool_Component(self):
        return self.__architectureTool_Component

    @architectureTool_Component.setter
    def architectureTool_Component(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_architectureTool_Component__architectureTool_Component", None)
        self.__architectureTool_Component = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "architectureTool_Port"):
                    opp_val = getattr(item, "architectureTool_Port", None)
                    
                    if opp_val == self:
                        setattr(item, "architectureTool_Port", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "architectureTool_Port"):
                    opp_val = getattr(item, "architectureTool_Port", None)
                    
                    setattr(item, "architectureTool_Port", self)
                    

    @property
    def architectureTool_Component31(self):
        return self.__architectureTool_Component31

    @architectureTool_Component31.setter
    def architectureTool_Component31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_architectureTool_Component__architectureTool_Component31", None)
        self.__architectureTool_Component31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "architectureTool_System30"):
                opp_val = getattr(old_value, "architectureTool_System30", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "architectureTool_System30"):
                opp_val = getattr(value, "architectureTool_System30", None)
                if opp_val is None:
                    setattr(value, "architectureTool_System30", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def architectureTool_Component10(self):
        return self.__architectureTool_Component10

    @architectureTool_Component10.setter
    def architectureTool_Component10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_architectureTool_Component__architectureTool_Component10", None)
        self.__architectureTool_Component10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "architectureTool_Interface"):
                    opp_val = getattr(item, "architectureTool_Interface", None)
                    
                    if opp_val == self:
                        setattr(item, "architectureTool_Interface", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "architectureTool_Interface"):
                    opp_val = getattr(item, "architectureTool_Interface", None)
                    
                    setattr(item, "architectureTool_Interface", self)
                    

    @property
    def architectureTool_Component3(self):
        return self.__architectureTool_Component3

    @architectureTool_Component3.setter
    def architectureTool_Component3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_architectureTool_Component__architectureTool_Component3", None)
        self.__architectureTool_Component3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "architectureTool_Component1"):
                opp_val = getattr(old_value, "architectureTool_Component1", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "architectureTool_Component1"):
                opp_val = getattr(value, "architectureTool_Component1", None)
                if opp_val is None:
                    setattr(value, "architectureTool_Component1", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def architectureTool_Component1(self):
        return self.__architectureTool_Component1

    @architectureTool_Component1.setter
    def architectureTool_Component1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_architectureTool_Component__architectureTool_Component1", None)
        self.__architectureTool_Component1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "architectureTool_Component3"):
                    opp_val = getattr(item, "architectureTool_Component3", None)
                    
                    if opp_val == self:
                        setattr(item, "architectureTool_Component3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "architectureTool_Component3"):
                    opp_val = getattr(item, "architectureTool_Component3", None)
                    
                    setattr(item, "architectureTool_Component3", self)
                    

    @property
    def architectureTool_Component5(self):
        return self.__architectureTool_Component5

    @architectureTool_Component5.setter
    def architectureTool_Component5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_architectureTool_Component__architectureTool_Component5", None)
        self.__architectureTool_Component5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "architectureTool_Class"):
                    opp_val = getattr(item, "architectureTool_Class", None)
                    
                    if opp_val == self:
                        setattr(item, "architectureTool_Class", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "architectureTool_Class"):
                    opp_val = getattr(item, "architectureTool_Class", None)
                    
                    setattr(item, "architectureTool_Class", self)
                    
