from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class simpleTypes(Enum):
    int = "int"
    boolean = "boolean"
    char = "char"
    date = "date"
    double = "double"
    float = "float"
    list = "list"
    long = "long"
    map = "map"
    string = "string"


############################################
# Definition of Classes
############################################

class componentBasedSystem_roles_AssemblyConnector:

    def __init__(self, name: str, componentBasedSystem_roles_AssemblyConnector77: "roles_componentBasedSystem_AssemblyContext" = None, componentBasedSystem_roles_AssemblyConnector79: "roles_componentBasedSystem_AssemblyContext" = None, componentBasedSystem_roles_AssemblyConnector: "ProvidedRole" = None, componentBasedSystem_roles_AssemblyConnector74: "RequiredRole" = None):
        self.name = name
        self.componentBasedSystem_roles_AssemblyConnector77 = componentBasedSystem_roles_AssemblyConnector77
        self.componentBasedSystem_roles_AssemblyConnector79 = componentBasedSystem_roles_AssemblyConnector79
        self.componentBasedSystem_roles_AssemblyConnector = componentBasedSystem_roles_AssemblyConnector
        self.componentBasedSystem_roles_AssemblyConnector74 = componentBasedSystem_roles_AssemblyConnector74
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def componentBasedSystem_roles_AssemblyConnector77(self):
        return self.__componentBasedSystem_roles_AssemblyConnector77

    @componentBasedSystem_roles_AssemblyConnector77.setter
    def componentBasedSystem_roles_AssemblyConnector77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_componentBasedSystem_roles_AssemblyConnector__componentBasedSystem_roles_AssemblyConnector77", None)
        self.__componentBasedSystem_roles_AssemblyConnector77 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "roles_componentBasedSystem_AssemblyContext"):
                opp_val = getattr(old_value, "roles_componentBasedSystem_AssemblyContext", None)
                if opp_val == self:
                    setattr(old_value, "roles_componentBasedSystem_AssemblyContext", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "roles_componentBasedSystem_AssemblyContext"):
                opp_val = getattr(value, "roles_componentBasedSystem_AssemblyContext", None)
                setattr(value, "roles_componentBasedSystem_AssemblyContext", self)

    @property
    def componentBasedSystem_roles_AssemblyConnector74(self):
        return self.__componentBasedSystem_roles_AssemblyConnector74

    @componentBasedSystem_roles_AssemblyConnector74.setter
    def componentBasedSystem_roles_AssemblyConnector74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_componentBasedSystem_roles_AssemblyConnector__componentBasedSystem_roles_AssemblyConnector74", None)
        self.__componentBasedSystem_roles_AssemblyConnector74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RequiredRole75"):
                opp_val = getattr(old_value, "RequiredRole75", None)
                if opp_val == self:
                    setattr(old_value, "RequiredRole75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RequiredRole75"):
                opp_val = getattr(value, "RequiredRole75", None)
                setattr(value, "RequiredRole75", self)

    @property
    def componentBasedSystem_roles_AssemblyConnector79(self):
        return self.__componentBasedSystem_roles_AssemblyConnector79

    @componentBasedSystem_roles_AssemblyConnector79.setter
    def componentBasedSystem_roles_AssemblyConnector79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_componentBasedSystem_roles_AssemblyConnector__componentBasedSystem_roles_AssemblyConnector79", None)
        self.__componentBasedSystem_roles_AssemblyConnector79 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "roles_componentBasedSystem_AssemblyContext80"):
                opp_val = getattr(old_value, "roles_componentBasedSystem_AssemblyContext80", None)
                if opp_val == self:
                    setattr(old_value, "roles_componentBasedSystem_AssemblyContext80", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "roles_componentBasedSystem_AssemblyContext80"):
                opp_val = getattr(value, "roles_componentBasedSystem_AssemblyContext80", None)
                setattr(value, "roles_componentBasedSystem_AssemblyContext80", self)

    @property
    def componentBasedSystem_roles_AssemblyConnector(self):
        return self.__componentBasedSystem_roles_AssemblyConnector

    @componentBasedSystem_roles_AssemblyConnector.setter
    def componentBasedSystem_roles_AssemblyConnector(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_componentBasedSystem_roles_AssemblyConnector__componentBasedSystem_roles_AssemblyConnector", None)
        self.__componentBasedSystem_roles_AssemblyConnector = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ProvidedRole72"):
                opp_val = getattr(old_value, "ProvidedRole72", None)
                if opp_val == self:
                    setattr(old_value, "ProvidedRole72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ProvidedRole72"):
                opp_val = getattr(value, "ProvidedRole72", None)
                setattr(value, "ProvidedRole72", self)

class roles_componentBasedSystem_Interface:

    pass
class componentBasedSystem_roles_Role:

    def __init__(self, name: str, componentBasedSystem_roles_Role: "roles_componentBasedSystem_Interface" = None):
        self.name = name
        self.componentBasedSystem_roles_Role = componentBasedSystem_roles_Role
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def componentBasedSystem_roles_Role(self):
        return self.__componentBasedSystem_roles_Role

    @componentBasedSystem_roles_Role.setter
    def componentBasedSystem_roles_Role(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_componentBasedSystem_roles_Role__componentBasedSystem_roles_Role", None)
        self.__componentBasedSystem_roles_Role = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "roles_componentBasedSystem_Interface"):
                opp_val = getattr(old_value, "roles_componentBasedSystem_Interface", None)
                if opp_val == self:
                    setattr(old_value, "roles_componentBasedSystem_Interface", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "roles_componentBasedSystem_Interface"):
                opp_val = getattr(value, "roles_componentBasedSystem_Interface", None)
                setattr(value, "roles_componentBasedSystem_Interface", self)

class componentBasedSystem_behaviourDescription_BehaviourDescription:

    pass
class roles_componentBasedSystem_AssemblyContext:

    pass
class Simple:

    pass
class dataTypes_ReturnType:

    pass
class dataTypes_ParameterType:

    pass
class componentBasedSystem_dataTypes_Complex(dataTypes_ParameterType, dataTypes_ReturnType):

    pass
class componentBasedSystem_dataTypes_Simple(dataTypes_ParameterType, dataTypes_ReturnType):

    def __init__(self, kind: str):
        self.kind = kind
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

class DescriptionElement:

    pass
class componentBasedSystem_behaviourDescription_Branch(DescriptionElement):

    pass
class componentBasedSystem_behaviourDescription_Loop(DescriptionElement):

    pass
class componentBasedSystem_behaviourDescription_ExternalCall(DescriptionElement):

    pass
class componentBasedSystem_behaviourDescription_InternalAction(DescriptionElement):

    pass
class componentBasedSystem_behaviourDescription_DescriptionElement:

    pass
class componentBasedSystem_dataTypes_Type:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class componentBasedSystem_AllocationContext:

    pass
class ParameterType:

    pass
class ReturnType:

    pass
class componentBasedSystem_dataTypes_Void(ReturnType):

    pass
class componentBasedSystem_Parameter:

    def __init__(self, name: str, componentBasedSystem_Parameter: "componentBasedSystem_Signature" = None, componentBasedSystem_Parameter35: "ParameterType" = None):
        self.name = name
        self.componentBasedSystem_Parameter = componentBasedSystem_Parameter
        self.componentBasedSystem_Parameter35 = componentBasedSystem_Parameter35
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def componentBasedSystem_Parameter35(self):
        return self.__componentBasedSystem_Parameter35

    @componentBasedSystem_Parameter35.setter
    def componentBasedSystem_Parameter35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_componentBasedSystem_Parameter__componentBasedSystem_Parameter35", None)
        self.__componentBasedSystem_Parameter35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ParameterType"):
                opp_val = getattr(old_value, "ParameterType", None)
                if opp_val == self:
                    setattr(old_value, "ParameterType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ParameterType"):
                opp_val = getattr(value, "ParameterType", None)
                setattr(value, "ParameterType", self)

    @property
    def componentBasedSystem_Parameter(self):
        return self.__componentBasedSystem_Parameter

    @componentBasedSystem_Parameter.setter
    def componentBasedSystem_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_componentBasedSystem_Parameter__componentBasedSystem_Parameter", None)
        self.__componentBasedSystem_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "componentBasedSystem_Signature31"):
                opp_val = getattr(old_value, "componentBasedSystem_Signature31", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "componentBasedSystem_Signature31"):
                opp_val = getattr(value, "componentBasedSystem_Signature31", None)
                if opp_val is None:
                    setattr(value, "componentBasedSystem_Signature31", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class componentBasedSystem_Link:

    def __init__(self, name: str, componentBasedSystem_Link51: "componentBasedSystem_Environment" = None, componentBasedSystem_Link: set["componentBasedSystem_Container"] = None):
        self.name = name
        self.componentBasedSystem_Link51 = componentBasedSystem_Link51
        self.componentBasedSystem_Link = componentBasedSystem_Link if componentBasedSystem_Link is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def componentBasedSystem_Link51(self):
        return self.__componentBasedSystem_Link51

    @componentBasedSystem_Link51.setter
    def componentBasedSystem_Link51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_componentBasedSystem_Link__componentBasedSystem_Link51", None)
        self.__componentBasedSystem_Link51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "componentBasedSystem_Environment50"):
                opp_val = getattr(old_value, "componentBasedSystem_Environment50", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "componentBasedSystem_Environment50"):
                opp_val = getattr(value, "componentBasedSystem_Environment50", None)
                if opp_val is None:
                    setattr(value, "componentBasedSystem_Environment50", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def componentBasedSystem_Link(self):
        return self.__componentBasedSystem_Link

    @componentBasedSystem_Link.setter
    def componentBasedSystem_Link(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_componentBasedSystem_Link__componentBasedSystem_Link", None)
        self.__componentBasedSystem_Link = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "componentBasedSystem_Container"):
                    opp_val = getattr(item, "componentBasedSystem_Container", None)
                    
                    if opp_val == self:
                        setattr(item, "componentBasedSystem_Container", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "componentBasedSystem_Container"):
                    opp_val = getattr(item, "componentBasedSystem_Container", None)
                    
                    setattr(item, "componentBasedSystem_Container", self)
                    

class Role:

    pass
class componentBasedSystem_roles_ProvidedRole(Role):

    pass
class componentBasedSystem_roles_RequiredRole(Role):

    pass
class BehaviourDescription:

    pass
class componentBasedSystem_Component:

    def __init__(self, name: str, componentBasedSystem_Component17: set["componentBasedSystem_Service"] = None, componentBasedSystem_Component19: set["RequiredRole"] = None, componentBasedSystem_Component22: set["ProvidedRole"] = None, componentBasedSystem_Component: set["BehaviourDescription"] = None, componentBasedSystem_Component38: "componentBasedSystem_AssemblyContext" = None, componentBasedSystem_Component57: "componentBasedSystem_Repository" = None):
        self.name = name
        self.componentBasedSystem_Component17 = componentBasedSystem_Component17 if componentBasedSystem_Component17 is not None else set()
        self.componentBasedSystem_Component19 = componentBasedSystem_Component19 if componentBasedSystem_Component19 is not None else set()
        self.componentBasedSystem_Component22 = componentBasedSystem_Component22 if componentBasedSystem_Component22 is not None else set()
        self.componentBasedSystem_Component = componentBasedSystem_Component if componentBasedSystem_Component is not None else set()
        self.componentBasedSystem_Component38 = componentBasedSystem_Component38
        self.componentBasedSystem_Component57 = componentBasedSystem_Component57
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def componentBasedSystem_Component38(self):
        return self.__componentBasedSystem_Component38

    @componentBasedSystem_Component38.setter
    def componentBasedSystem_Component38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_componentBasedSystem_Component__componentBasedSystem_Component38", None)
        self.__componentBasedSystem_Component38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "componentBasedSystem_AssemblyContext37"):
                opp_val = getattr(old_value, "componentBasedSystem_AssemblyContext37", None)
                if opp_val == self:
                    setattr(old_value, "componentBasedSystem_AssemblyContext37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "componentBasedSystem_AssemblyContext37"):
                opp_val = getattr(value, "componentBasedSystem_AssemblyContext37", None)
                setattr(value, "componentBasedSystem_AssemblyContext37", self)

    @property
    def componentBasedSystem_Component(self):
        return self.__componentBasedSystem_Component

    @componentBasedSystem_Component.setter
    def componentBasedSystem_Component(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_componentBasedSystem_Component__componentBasedSystem_Component", None)
        self.__componentBasedSystem_Component = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BehaviourDescription"):
                    opp_val = getattr(item, "BehaviourDescription", None)
                    
                    if opp_val == self:
                        setattr(item, "BehaviourDescription", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BehaviourDescription"):
                    opp_val = getattr(item, "BehaviourDescription", None)
                    
                    setattr(item, "BehaviourDescription", self)
                    

    @property
    def componentBasedSystem_Component17(self):
        return self.__componentBasedSystem_Component17

    @componentBasedSystem_Component17.setter
    def componentBasedSystem_Component17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_componentBasedSystem_Component__componentBasedSystem_Component17", None)
        self.__componentBasedSystem_Component17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "componentBasedSystem_Service"):
                    opp_val = getattr(item, "componentBasedSystem_Service", None)
                    
                    if opp_val == self:
                        setattr(item, "componentBasedSystem_Service", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "componentBasedSystem_Service"):
                    opp_val = getattr(item, "componentBasedSystem_Service", None)
                    
                    setattr(item, "componentBasedSystem_Service", self)
                    

    @property
    def componentBasedSystem_Component22(self):
        return self.__componentBasedSystem_Component22

    @componentBasedSystem_Component22.setter
    def componentBasedSystem_Component22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_componentBasedSystem_Component__componentBasedSystem_Component22", None)
        self.__componentBasedSystem_Component22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ProvidedRole23"):
                    opp_val = getattr(item, "ProvidedRole23", None)
                    
                    if opp_val == self:
                        setattr(item, "ProvidedRole23", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ProvidedRole23"):
                    opp_val = getattr(item, "ProvidedRole23", None)
                    
                    setattr(item, "ProvidedRole23", self)
                    

    @property
    def componentBasedSystem_Component19(self):
        return self.__componentBasedSystem_Component19

    @componentBasedSystem_Component19.setter
    def componentBasedSystem_Component19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_componentBasedSystem_Component__componentBasedSystem_Component19", None)
        self.__componentBasedSystem_Component19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RequiredRole20"):
                    opp_val = getattr(item, "RequiredRole20", None)
                    
                    if opp_val == self:
                        setattr(item, "RequiredRole20", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RequiredRole20"):
                    opp_val = getattr(item, "RequiredRole20", None)
                    
                    setattr(item, "RequiredRole20", self)
                    

    @property
    def componentBasedSystem_Component57(self):
        return self.__componentBasedSystem_Component57

    @componentBasedSystem_Component57.setter
    def componentBasedSystem_Component57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_componentBasedSystem_Component__componentBasedSystem_Component57", None)
        self.__componentBasedSystem_Component57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "componentBasedSystem_Repository56"):
                opp_val = getattr(old_value, "componentBasedSystem_Repository56", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "componentBasedSystem_Repository56"):
                opp_val = getattr(value, "componentBasedSystem_Repository56", None)
                if opp_val is None:
                    setattr(value, "componentBasedSystem_Repository56", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class RequiredRole:

    pass
class ProvidedRole:

    pass
class componentBasedSystem_Environment:

    def __init__(self, componentBasedSystem_Environment: "componentBasedSystem_ComponentBasedSystem" = None, componentBasedSystem_Environment47: set["componentBasedSystem_Container"] = None, componentBasedSystem_Environment50: set["componentBasedSystem_Link"] = None):
        self.componentBasedSystem_Environment = componentBasedSystem_Environment
        self.componentBasedSystem_Environment47 = componentBasedSystem_Environment47 if componentBasedSystem_Environment47 is not None else set()
        self.componentBasedSystem_Environment50 = componentBasedSystem_Environment50 if componentBasedSystem_Environment50 is not None else set()
        
    @property
    def componentBasedSystem_Environment47(self):
        return self.__componentBasedSystem_Environment47

    @componentBasedSystem_Environment47.setter
    def componentBasedSystem_Environment47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_componentBasedSystem_Environment__componentBasedSystem_Environment47", None)
        self.__componentBasedSystem_Environment47 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "componentBasedSystem_Container48"):
                    opp_val = getattr(item, "componentBasedSystem_Container48", None)
                    
                    if opp_val == self:
                        setattr(item, "componentBasedSystem_Container48", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "componentBasedSystem_Container48"):
                    opp_val = getattr(item, "componentBasedSystem_Container48", None)
                    
                    setattr(item, "componentBasedSystem_Container48", self)
                    

    @property
    def componentBasedSystem_Environment50(self):
        return self.__componentBasedSystem_Environment50

    @componentBasedSystem_Environment50.setter
    def componentBasedSystem_Environment50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_componentBasedSystem_Environment__componentBasedSystem_Environment50", None)
        self.__componentBasedSystem_Environment50 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "componentBasedSystem_Link51"):
                    opp_val = getattr(item, "componentBasedSystem_Link51", None)
                    
                    if opp_val == self:
                        setattr(item, "componentBasedSystem_Link51", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "componentBasedSystem_Link51"):
                    opp_val = getattr(item, "componentBasedSystem_Link51", None)
                    
                    setattr(item, "componentBasedSystem_Link51", self)
                    

    @property
    def componentBasedSystem_Environment(self):
        return self.__componentBasedSystem_Environment

    @componentBasedSystem_Environment.setter
    def componentBasedSystem_Environment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_componentBasedSystem_Environment__componentBasedSystem_Environment", None)
        self.__componentBasedSystem_Environment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "componentBasedSystem_ComponentBasedSystem10"):
                opp_val = getattr(old_value, "componentBasedSystem_ComponentBasedSystem10", None)
                if opp_val == self:
                    setattr(old_value, "componentBasedSystem_ComponentBasedSystem10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "componentBasedSystem_ComponentBasedSystem10"):
                opp_val = getattr(value, "componentBasedSystem_ComponentBasedSystem10", None)
                setattr(value, "componentBasedSystem_ComponentBasedSystem10", self)

    def IsLinked(self, c2: str, c1: str) -> bool:
        # TODO: Implement IsLinked method
        pass

class componentBasedSystem_Repository:

    pass
class componentBasedSystem_Allocation:

    pass
class AssemblyConnector:

    pass
class Type:

    pass
class componentBasedSystem_dataTypes_ReturnType(Type):

    pass
class componentBasedSystem_dataTypes_ParameterType(Type):

    pass
class componentBasedSystem_Container:

    def __init__(self, name: str, componentBasedSystem_Container48: "componentBasedSystem_Environment" = None, componentBasedSystem_Container: "componentBasedSystem_Link" = None, componentBasedSystem_Container40: "componentBasedSystem_AllocationContext" = None):
        self.name = name
        self.componentBasedSystem_Container48 = componentBasedSystem_Container48
        self.componentBasedSystem_Container = componentBasedSystem_Container
        self.componentBasedSystem_Container40 = componentBasedSystem_Container40
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def componentBasedSystem_Container40(self):
        return self.__componentBasedSystem_Container40

    @componentBasedSystem_Container40.setter
    def componentBasedSystem_Container40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_componentBasedSystem_Container__componentBasedSystem_Container40", None)
        self.__componentBasedSystem_Container40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "componentBasedSystem_AllocationContext"):
                opp_val = getattr(old_value, "componentBasedSystem_AllocationContext", None)
                if opp_val == self:
                    setattr(old_value, "componentBasedSystem_AllocationContext", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "componentBasedSystem_AllocationContext"):
                opp_val = getattr(value, "componentBasedSystem_AllocationContext", None)
                setattr(value, "componentBasedSystem_AllocationContext", self)

    @property
    def componentBasedSystem_Container(self):
        return self.__componentBasedSystem_Container

    @componentBasedSystem_Container.setter
    def componentBasedSystem_Container(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_componentBasedSystem_Container__componentBasedSystem_Container", None)
        self.__componentBasedSystem_Container = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "componentBasedSystem_Link"):
                opp_val = getattr(old_value, "componentBasedSystem_Link", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "componentBasedSystem_Link"):
                opp_val = getattr(value, "componentBasedSystem_Link", None)
                if opp_val is None:
                    setattr(value, "componentBasedSystem_Link", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def componentBasedSystem_Container48(self):
        return self.__componentBasedSystem_Container48

    @componentBasedSystem_Container48.setter
    def componentBasedSystem_Container48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_componentBasedSystem_Container__componentBasedSystem_Container48", None)
        self.__componentBasedSystem_Container48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "componentBasedSystem_Environment47"):
                opp_val = getattr(old_value, "componentBasedSystem_Environment47", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "componentBasedSystem_Environment47"):
                opp_val = getattr(value, "componentBasedSystem_Environment47", None)
                if opp_val is None:
                    setattr(value, "componentBasedSystem_Environment47", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class componentBasedSystem_DelegationConnector:

    def __init__(self, name: str, componentBasedSystem_DelegationConnector: "componentBasedSystem_CompositeComponent" = None, componentBasedSystem_DelegationConnector45: set["Role"] = None):
        self.name = name
        self.componentBasedSystem_DelegationConnector = componentBasedSystem_DelegationConnector
        self.componentBasedSystem_DelegationConnector45 = componentBasedSystem_DelegationConnector45 if componentBasedSystem_DelegationConnector45 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def componentBasedSystem_DelegationConnector(self):
        return self.__componentBasedSystem_DelegationConnector

    @componentBasedSystem_DelegationConnector.setter
    def componentBasedSystem_DelegationConnector(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_componentBasedSystem_DelegationConnector__componentBasedSystem_DelegationConnector", None)
        self.__componentBasedSystem_DelegationConnector = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "componentBasedSystem_CompositeComponent28"):
                opp_val = getattr(old_value, "componentBasedSystem_CompositeComponent28", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "componentBasedSystem_CompositeComponent28"):
                opp_val = getattr(value, "componentBasedSystem_CompositeComponent28", None)
                if opp_val is None:
                    setattr(value, "componentBasedSystem_CompositeComponent28", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def componentBasedSystem_DelegationConnector45(self):
        return self.__componentBasedSystem_DelegationConnector45

    @componentBasedSystem_DelegationConnector45.setter
    def componentBasedSystem_DelegationConnector45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_componentBasedSystem_DelegationConnector__componentBasedSystem_DelegationConnector45", None)
        self.__componentBasedSystem_DelegationConnector45 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Role"):
                    opp_val = getattr(item, "Role", None)
                    
                    if opp_val == self:
                        setattr(item, "Role", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Role"):
                    opp_val = getattr(item, "Role", None)
                    
                    setattr(item, "Role", self)
                    

class Component:

    pass
class componentBasedSystem_CompositeComponent(Component):

    pass
class componentBasedSystem_Signature:

    def __init__(self, name: str, componentBasedSystem_Signature: "componentBasedSystem_Interface" = None, componentBasedSystem_Signature31: set["componentBasedSystem_Parameter"] = None, componentBasedSystem_Signature33: "ReturnType" = None, componentBasedSystem_Signature63: "componentBasedSystem_Service" = None):
        self.name = name
        self.componentBasedSystem_Signature = componentBasedSystem_Signature
        self.componentBasedSystem_Signature31 = componentBasedSystem_Signature31 if componentBasedSystem_Signature31 is not None else set()
        self.componentBasedSystem_Signature33 = componentBasedSystem_Signature33
        self.componentBasedSystem_Signature63 = componentBasedSystem_Signature63
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def componentBasedSystem_Signature33(self):
        return self.__componentBasedSystem_Signature33

    @componentBasedSystem_Signature33.setter
    def componentBasedSystem_Signature33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_componentBasedSystem_Signature__componentBasedSystem_Signature33", None)
        self.__componentBasedSystem_Signature33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ReturnType"):
                opp_val = getattr(old_value, "ReturnType", None)
                if opp_val == self:
                    setattr(old_value, "ReturnType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ReturnType"):
                opp_val = getattr(value, "ReturnType", None)
                setattr(value, "ReturnType", self)

    @property
    def componentBasedSystem_Signature(self):
        return self.__componentBasedSystem_Signature

    @componentBasedSystem_Signature.setter
    def componentBasedSystem_Signature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_componentBasedSystem_Signature__componentBasedSystem_Signature", None)
        self.__componentBasedSystem_Signature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "componentBasedSystem_Interface"):
                opp_val = getattr(old_value, "componentBasedSystem_Interface", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "componentBasedSystem_Interface"):
                opp_val = getattr(value, "componentBasedSystem_Interface", None)
                if opp_val is None:
                    setattr(value, "componentBasedSystem_Interface", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def componentBasedSystem_Signature63(self):
        return self.__componentBasedSystem_Signature63

    @componentBasedSystem_Signature63.setter
    def componentBasedSystem_Signature63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_componentBasedSystem_Signature__componentBasedSystem_Signature63", None)
        self.__componentBasedSystem_Signature63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "componentBasedSystem_Service62"):
                opp_val = getattr(old_value, "componentBasedSystem_Service62", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "componentBasedSystem_Service62"):
                opp_val = getattr(value, "componentBasedSystem_Service62", None)
                if opp_val is None:
                    setattr(value, "componentBasedSystem_Service62", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def componentBasedSystem_Signature31(self):
        return self.__componentBasedSystem_Signature31

    @componentBasedSystem_Signature31.setter
    def componentBasedSystem_Signature31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_componentBasedSystem_Signature__componentBasedSystem_Signature31", None)
        self.__componentBasedSystem_Signature31 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "componentBasedSystem_Parameter"):
                    opp_val = getattr(item, "componentBasedSystem_Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "componentBasedSystem_Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "componentBasedSystem_Parameter"):
                    opp_val = getattr(item, "componentBasedSystem_Parameter", None)
                    
                    setattr(item, "componentBasedSystem_Parameter", self)
                    

class componentBasedSystem_Interface:

    def __init__(self, name: str, componentBasedSystem_Interface: set["componentBasedSystem_Signature"] = None, componentBasedSystem_Interface54: "componentBasedSystem_Repository" = None):
        self.name = name
        self.componentBasedSystem_Interface = componentBasedSystem_Interface if componentBasedSystem_Interface is not None else set()
        self.componentBasedSystem_Interface54 = componentBasedSystem_Interface54
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def componentBasedSystem_Interface(self):
        return self.__componentBasedSystem_Interface

    @componentBasedSystem_Interface.setter
    def componentBasedSystem_Interface(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_componentBasedSystem_Interface__componentBasedSystem_Interface", None)
        self.__componentBasedSystem_Interface = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "componentBasedSystem_Signature"):
                    opp_val = getattr(item, "componentBasedSystem_Signature", None)
                    
                    if opp_val == self:
                        setattr(item, "componentBasedSystem_Signature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "componentBasedSystem_Signature"):
                    opp_val = getattr(item, "componentBasedSystem_Signature", None)
                    
                    setattr(item, "componentBasedSystem_Signature", self)
                    

    @property
    def componentBasedSystem_Interface54(self):
        return self.__componentBasedSystem_Interface54

    @componentBasedSystem_Interface54.setter
    def componentBasedSystem_Interface54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_componentBasedSystem_Interface__componentBasedSystem_Interface54", None)
        self.__componentBasedSystem_Interface54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "componentBasedSystem_Repository53"):
                opp_val = getattr(old_value, "componentBasedSystem_Repository53", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "componentBasedSystem_Repository53"):
                opp_val = getattr(value, "componentBasedSystem_Repository53", None)
                if opp_val is None:
                    setattr(value, "componentBasedSystem_Repository53", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class componentBasedSystem_Service:

    pass
class componentBasedSystem_AssemblyContext:

    def __init__(self, name: str, componentBasedSystem_AssemblyContext: "componentBasedSystem_ComponentBasedSystem" = None, componentBasedSystem_AssemblyContext26: "componentBasedSystem_CompositeComponent" = None, componentBasedSystem_AssemblyContext43: "componentBasedSystem_AllocationContext" = None, componentBasedSystem_AssemblyContext37: "componentBasedSystem_Component" = None):
        self.name = name
        self.componentBasedSystem_AssemblyContext = componentBasedSystem_AssemblyContext
        self.componentBasedSystem_AssemblyContext26 = componentBasedSystem_AssemblyContext26
        self.componentBasedSystem_AssemblyContext43 = componentBasedSystem_AssemblyContext43
        self.componentBasedSystem_AssemblyContext37 = componentBasedSystem_AssemblyContext37
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def componentBasedSystem_AssemblyContext43(self):
        return self.__componentBasedSystem_AssemblyContext43

    @componentBasedSystem_AssemblyContext43.setter
    def componentBasedSystem_AssemblyContext43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_componentBasedSystem_AssemblyContext__componentBasedSystem_AssemblyContext43", None)
        self.__componentBasedSystem_AssemblyContext43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "componentBasedSystem_AllocationContext42"):
                opp_val = getattr(old_value, "componentBasedSystem_AllocationContext42", None)
                if opp_val == self:
                    setattr(old_value, "componentBasedSystem_AllocationContext42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "componentBasedSystem_AllocationContext42"):
                opp_val = getattr(value, "componentBasedSystem_AllocationContext42", None)
                setattr(value, "componentBasedSystem_AllocationContext42", self)

    @property
    def componentBasedSystem_AssemblyContext37(self):
        return self.__componentBasedSystem_AssemblyContext37

    @componentBasedSystem_AssemblyContext37.setter
    def componentBasedSystem_AssemblyContext37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_componentBasedSystem_AssemblyContext__componentBasedSystem_AssemblyContext37", None)
        self.__componentBasedSystem_AssemblyContext37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "componentBasedSystem_Component38"):
                opp_val = getattr(old_value, "componentBasedSystem_Component38", None)
                if opp_val == self:
                    setattr(old_value, "componentBasedSystem_Component38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "componentBasedSystem_Component38"):
                opp_val = getattr(value, "componentBasedSystem_Component38", None)
                setattr(value, "componentBasedSystem_Component38", self)

    @property
    def componentBasedSystem_AssemblyContext26(self):
        return self.__componentBasedSystem_AssemblyContext26

    @componentBasedSystem_AssemblyContext26.setter
    def componentBasedSystem_AssemblyContext26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_componentBasedSystem_AssemblyContext__componentBasedSystem_AssemblyContext26", None)
        self.__componentBasedSystem_AssemblyContext26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "componentBasedSystem_CompositeComponent"):
                opp_val = getattr(old_value, "componentBasedSystem_CompositeComponent", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "componentBasedSystem_CompositeComponent"):
                opp_val = getattr(value, "componentBasedSystem_CompositeComponent", None)
                if opp_val is None:
                    setattr(value, "componentBasedSystem_CompositeComponent", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def componentBasedSystem_AssemblyContext(self):
        return self.__componentBasedSystem_AssemblyContext

    @componentBasedSystem_AssemblyContext.setter
    def componentBasedSystem_AssemblyContext(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_componentBasedSystem_AssemblyContext__componentBasedSystem_AssemblyContext", None)
        self.__componentBasedSystem_AssemblyContext = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "componentBasedSystem_ComponentBasedSystem"):
                opp_val = getattr(old_value, "componentBasedSystem_ComponentBasedSystem", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "componentBasedSystem_ComponentBasedSystem"):
                opp_val = getattr(value, "componentBasedSystem_ComponentBasedSystem", None)
                if opp_val is None:
                    setattr(value, "componentBasedSystem_ComponentBasedSystem", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class componentBasedSystem_ComponentBasedSystem:

    def __init__(self, componentBasedSystem_ComponentBasedSystem: set["componentBasedSystem_AssemblyContext"] = None, componentBasedSystem_ComponentBasedSystem2: set["Type"] = None, componentBasedSystem_ComponentBasedSystem4: set["AssemblyConnector"] = None, componentBasedSystem_ComponentBasedSystem6: "componentBasedSystem_Allocation" = None, componentBasedSystem_ComponentBasedSystem8: "componentBasedSystem_Repository" = None, componentBasedSystem_ComponentBasedSystem10: "componentBasedSystem_Environment" = None, componentBasedSystem_ComponentBasedSystem12: set["ProvidedRole"] = None, componentBasedSystem_ComponentBasedSystem14: set["RequiredRole"] = None):
        self.componentBasedSystem_ComponentBasedSystem = componentBasedSystem_ComponentBasedSystem if componentBasedSystem_ComponentBasedSystem is not None else set()
        self.componentBasedSystem_ComponentBasedSystem2 = componentBasedSystem_ComponentBasedSystem2 if componentBasedSystem_ComponentBasedSystem2 is not None else set()
        self.componentBasedSystem_ComponentBasedSystem4 = componentBasedSystem_ComponentBasedSystem4 if componentBasedSystem_ComponentBasedSystem4 is not None else set()
        self.componentBasedSystem_ComponentBasedSystem6 = componentBasedSystem_ComponentBasedSystem6
        self.componentBasedSystem_ComponentBasedSystem8 = componentBasedSystem_ComponentBasedSystem8
        self.componentBasedSystem_ComponentBasedSystem10 = componentBasedSystem_ComponentBasedSystem10
        self.componentBasedSystem_ComponentBasedSystem12 = componentBasedSystem_ComponentBasedSystem12 if componentBasedSystem_ComponentBasedSystem12 is not None else set()
        self.componentBasedSystem_ComponentBasedSystem14 = componentBasedSystem_ComponentBasedSystem14 if componentBasedSystem_ComponentBasedSystem14 is not None else set()
        
    @property
    def componentBasedSystem_ComponentBasedSystem10(self):
        return self.__componentBasedSystem_ComponentBasedSystem10

    @componentBasedSystem_ComponentBasedSystem10.setter
    def componentBasedSystem_ComponentBasedSystem10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_componentBasedSystem_ComponentBasedSystem__componentBasedSystem_ComponentBasedSystem10", None)
        self.__componentBasedSystem_ComponentBasedSystem10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "componentBasedSystem_Environment"):
                opp_val = getattr(old_value, "componentBasedSystem_Environment", None)
                if opp_val == self:
                    setattr(old_value, "componentBasedSystem_Environment", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "componentBasedSystem_Environment"):
                opp_val = getattr(value, "componentBasedSystem_Environment", None)
                setattr(value, "componentBasedSystem_Environment", self)

    @property
    def componentBasedSystem_ComponentBasedSystem4(self):
        return self.__componentBasedSystem_ComponentBasedSystem4

    @componentBasedSystem_ComponentBasedSystem4.setter
    def componentBasedSystem_ComponentBasedSystem4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_componentBasedSystem_ComponentBasedSystem__componentBasedSystem_ComponentBasedSystem4", None)
        self.__componentBasedSystem_ComponentBasedSystem4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AssemblyConnector"):
                    opp_val = getattr(item, "AssemblyConnector", None)
                    
                    if opp_val == self:
                        setattr(item, "AssemblyConnector", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AssemblyConnector"):
                    opp_val = getattr(item, "AssemblyConnector", None)
                    
                    setattr(item, "AssemblyConnector", self)
                    

    @property
    def componentBasedSystem_ComponentBasedSystem(self):
        return self.__componentBasedSystem_ComponentBasedSystem

    @componentBasedSystem_ComponentBasedSystem.setter
    def componentBasedSystem_ComponentBasedSystem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_componentBasedSystem_ComponentBasedSystem__componentBasedSystem_ComponentBasedSystem", None)
        self.__componentBasedSystem_ComponentBasedSystem = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "componentBasedSystem_AssemblyContext"):
                    opp_val = getattr(item, "componentBasedSystem_AssemblyContext", None)
                    
                    if opp_val == self:
                        setattr(item, "componentBasedSystem_AssemblyContext", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "componentBasedSystem_AssemblyContext"):
                    opp_val = getattr(item, "componentBasedSystem_AssemblyContext", None)
                    
                    setattr(item, "componentBasedSystem_AssemblyContext", self)
                    

    @property
    def componentBasedSystem_ComponentBasedSystem12(self):
        return self.__componentBasedSystem_ComponentBasedSystem12

    @componentBasedSystem_ComponentBasedSystem12.setter
    def componentBasedSystem_ComponentBasedSystem12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_componentBasedSystem_ComponentBasedSystem__componentBasedSystem_ComponentBasedSystem12", None)
        self.__componentBasedSystem_ComponentBasedSystem12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ProvidedRole"):
                    opp_val = getattr(item, "ProvidedRole", None)
                    
                    if opp_val == self:
                        setattr(item, "ProvidedRole", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ProvidedRole"):
                    opp_val = getattr(item, "ProvidedRole", None)
                    
                    setattr(item, "ProvidedRole", self)
                    

    @property
    def componentBasedSystem_ComponentBasedSystem8(self):
        return self.__componentBasedSystem_ComponentBasedSystem8

    @componentBasedSystem_ComponentBasedSystem8.setter
    def componentBasedSystem_ComponentBasedSystem8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_componentBasedSystem_ComponentBasedSystem__componentBasedSystem_ComponentBasedSystem8", None)
        self.__componentBasedSystem_ComponentBasedSystem8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "componentBasedSystem_Repository"):
                opp_val = getattr(old_value, "componentBasedSystem_Repository", None)
                if opp_val == self:
                    setattr(old_value, "componentBasedSystem_Repository", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "componentBasedSystem_Repository"):
                opp_val = getattr(value, "componentBasedSystem_Repository", None)
                setattr(value, "componentBasedSystem_Repository", self)

    @property
    def componentBasedSystem_ComponentBasedSystem14(self):
        return self.__componentBasedSystem_ComponentBasedSystem14

    @componentBasedSystem_ComponentBasedSystem14.setter
    def componentBasedSystem_ComponentBasedSystem14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_componentBasedSystem_ComponentBasedSystem__componentBasedSystem_ComponentBasedSystem14", None)
        self.__componentBasedSystem_ComponentBasedSystem14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RequiredRole"):
                    opp_val = getattr(item, "RequiredRole", None)
                    
                    if opp_val == self:
                        setattr(item, "RequiredRole", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RequiredRole"):
                    opp_val = getattr(item, "RequiredRole", None)
                    
                    setattr(item, "RequiredRole", self)
                    

    @property
    def componentBasedSystem_ComponentBasedSystem2(self):
        return self.__componentBasedSystem_ComponentBasedSystem2

    @componentBasedSystem_ComponentBasedSystem2.setter
    def componentBasedSystem_ComponentBasedSystem2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_componentBasedSystem_ComponentBasedSystem__componentBasedSystem_ComponentBasedSystem2", None)
        self.__componentBasedSystem_ComponentBasedSystem2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Type"):
                    opp_val = getattr(item, "Type", None)
                    
                    if opp_val == self:
                        setattr(item, "Type", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Type"):
                    opp_val = getattr(item, "Type", None)
                    
                    setattr(item, "Type", self)
                    

    @property
    def componentBasedSystem_ComponentBasedSystem6(self):
        return self.__componentBasedSystem_ComponentBasedSystem6

    @componentBasedSystem_ComponentBasedSystem6.setter
    def componentBasedSystem_ComponentBasedSystem6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_componentBasedSystem_ComponentBasedSystem__componentBasedSystem_ComponentBasedSystem6", None)
        self.__componentBasedSystem_ComponentBasedSystem6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "componentBasedSystem_Allocation"):
                opp_val = getattr(old_value, "componentBasedSystem_Allocation", None)
                if opp_val == self:
                    setattr(old_value, "componentBasedSystem_Allocation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "componentBasedSystem_Allocation"):
                opp_val = getattr(value, "componentBasedSystem_Allocation", None)
                setattr(value, "componentBasedSystem_Allocation", self)

    def GetContainerOfContext(self, context: str) -> str:
        # TODO: Implement GetContainerOfContext method
        pass
