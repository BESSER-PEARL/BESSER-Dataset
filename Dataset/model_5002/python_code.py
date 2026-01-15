from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class ParameterTyp:

    pass
class componentModel_SimpleParameterType(ParameterTyp):

    pass
class componentModel_ComplexParameterType(ParameterTyp):

    pass
class Type:

    pass
class componentModel_Void(Type):

    pass
class componentModel_ParameterTyp(Type):

    pass
class SimpleParameterType:

    pass
class componentModel_Float(SimpleParameterType):

    pass
class componentModel_Boolean(SimpleParameterType):

    pass
class componentModel_List(SimpleParameterType):

    pass
class componentModel_String(SimpleParameterType):

    pass
class componentModel_Int(SimpleParameterType):

    pass
class componentModel_Char(SimpleParameterType):

    pass
class componentModel_Map(SimpleParameterType):

    pass
class componentModel_Date(SimpleParameterType):

    pass
class componentModel_Long(SimpleParameterType):

    pass
class componentModel_Double(SimpleParameterType):

    pass
class componentModel_System:

    pass
class componentModel_Type(ABC):

    pass
class componentModel_Parameter(SimpleParameterType):

    def __init__(self, name: str, componentModel_Parameter: "componentModel_Signature" = None, componentModel_Parameter75: "componentModel_ParameterTyp" = None):
        self.name = name
        self.componentModel_Parameter = componentModel_Parameter
        self.componentModel_Parameter75 = componentModel_Parameter75
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def componentModel_Parameter(self):
        return self.__componentModel_Parameter

    @componentModel_Parameter.setter
    def componentModel_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_componentModel_Parameter__componentModel_Parameter", None)
        self.__componentModel_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "componentModel_Signature41"):
                opp_val = getattr(old_value, "componentModel_Signature41", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "componentModel_Signature41"):
                opp_val = getattr(value, "componentModel_Signature41", None)
                if opp_val is None:
                    setattr(value, "componentModel_Signature41", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def componentModel_Parameter75(self):
        return self.__componentModel_Parameter75

    @componentModel_Parameter75.setter
    def componentModel_Parameter75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_componentModel_Parameter__componentModel_Parameter75", None)
        self.__componentModel_Parameter75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "componentModel_ParameterTyp"):
                opp_val = getattr(old_value, "componentModel_ParameterTyp", None)
                if opp_val == self:
                    setattr(old_value, "componentModel_ParameterTyp", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "componentModel_ParameterTyp"):
                opp_val = getattr(value, "componentModel_ParameterTyp", None)
                setattr(value, "componentModel_ParameterTyp", self)

class DelegationConnector:

    pass
class componentModel_ProvidedDelegationConnector(DelegationConnector):

    pass
class componentModel_RequiredDelegationConnector(DelegationConnector):

    pass
class Component:

    pass
class componentModel_CompositeComponent(Component):

    pass
class componentModel_ViewPoint(ABC):

    pass
class componentModel_ProvidedRole:

    def __init__(self, name: str, componentModel_ProvidedRole: "componentModel_AssemblyConnector" = None, ProvidedRole: "componentModel_AssemblyContext" = None, componentModel_ProvidedRole68: "componentModel_ProvidedDelegationConnector" = None, providedrole: "componentModel_AssemblyContext" = None, componentModel_ProvidedRole62: "componentModel_Interface" = None):
        self.name = name
        self.componentModel_ProvidedRole = componentModel_ProvidedRole
        self.ProvidedRole = ProvidedRole
        self.componentModel_ProvidedRole68 = componentModel_ProvidedRole68
        self.providedrole = providedrole
        self.componentModel_ProvidedRole62 = componentModel_ProvidedRole62
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def componentModel_ProvidedRole(self):
        return self.__componentModel_ProvidedRole

    @componentModel_ProvidedRole.setter
    def componentModel_ProvidedRole(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_componentModel_ProvidedRole__componentModel_ProvidedRole", None)
        self.__componentModel_ProvidedRole = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "componentModel_AssemblyConnector32"):
                opp_val = getattr(old_value, "componentModel_AssemblyConnector32", None)
                if opp_val == self:
                    setattr(old_value, "componentModel_AssemblyConnector32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "componentModel_AssemblyConnector32"):
                opp_val = getattr(value, "componentModel_AssemblyConnector32", None)
                setattr(value, "componentModel_AssemblyConnector32", self)

    @property
    def componentModel_ProvidedRole62(self):
        return self.__componentModel_ProvidedRole62

    @componentModel_ProvidedRole62.setter
    def componentModel_ProvidedRole62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_componentModel_ProvidedRole__componentModel_ProvidedRole62", None)
        self.__componentModel_ProvidedRole62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "componentModel_Interface63"):
                opp_val = getattr(old_value, "componentModel_Interface63", None)
                if opp_val == self:
                    setattr(old_value, "componentModel_Interface63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "componentModel_Interface63"):
                opp_val = getattr(value, "componentModel_Interface63", None)
                setattr(value, "componentModel_Interface63", self)

    @property
    def providedrole(self):
        return self.__providedrole

    @providedrole.setter
    def providedrole(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_componentModel_ProvidedRole__providedrole", None)
        self.__providedrole = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AssemblyContext60"):
                opp_val = getattr(old_value, "AssemblyContext60", None)
                if opp_val == self:
                    setattr(old_value, "AssemblyContext60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AssemblyContext60"):
                opp_val = getattr(value, "AssemblyContext60", None)
                setattr(value, "AssemblyContext60", self)

    @property
    def ProvidedRole(self):
        return self.__ProvidedRole

    @ProvidedRole.setter
    def ProvidedRole(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_componentModel_ProvidedRole__ProvidedRole", None)
        self.__ProvidedRole = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "assemblycontext"):
                opp_val = getattr(old_value, "assemblycontext", None)
                if opp_val == self:
                    setattr(old_value, "assemblycontext", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "assemblycontext"):
                opp_val = getattr(value, "assemblycontext", None)
                setattr(value, "assemblycontext", self)

    @property
    def componentModel_ProvidedRole68(self):
        return self.__componentModel_ProvidedRole68

    @componentModel_ProvidedRole68.setter
    def componentModel_ProvidedRole68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_componentModel_ProvidedRole__componentModel_ProvidedRole68", None)
        self.__componentModel_ProvidedRole68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "componentModel_ProvidedDelegationConnector67"):
                opp_val = getattr(old_value, "componentModel_ProvidedDelegationConnector67", None)
                if opp_val == self:
                    setattr(old_value, "componentModel_ProvidedDelegationConnector67", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "componentModel_ProvidedDelegationConnector67"):
                opp_val = getattr(value, "componentModel_ProvidedDelegationConnector67", None)
                setattr(value, "componentModel_ProvidedDelegationConnector67", self)

class AssemblyViewType:

    pass
class componentModel_AssemblyContext(AssemblyViewType):

    def __init__(self, name: str, assemblycontext28: "componentModel_RequiredRole" = None, componentModel_AssemblyContext: "componentModel_Component" = None, assemblycontext: "componentModel_ProvidedRole" = None, componentModel_AssemblyContext51: "componentModel_System" = None, AssemblyContext: "componentModel_RequiredRole" = None, AssemblyContext60: "componentModel_ProvidedRole" = None, componentModel_AssemblyContext71: "componentModel_CompositeComponent" = None):
        self.name = name
        self.assemblycontext28 = assemblycontext28
        self.componentModel_AssemblyContext = componentModel_AssemblyContext
        self.assemblycontext = assemblycontext
        self.componentModel_AssemblyContext51 = componentModel_AssemblyContext51
        self.AssemblyContext = AssemblyContext
        self.AssemblyContext60 = AssemblyContext60
        self.componentModel_AssemblyContext71 = componentModel_AssemblyContext71
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def assemblycontext28(self):
        return self.__assemblycontext28

    @assemblycontext28.setter
    def assemblycontext28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_componentModel_AssemblyContext__assemblycontext28", None)
        self.__assemblycontext28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RequiredRole"):
                opp_val = getattr(old_value, "RequiredRole", None)
                if opp_val == self:
                    setattr(old_value, "RequiredRole", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RequiredRole"):
                opp_val = getattr(value, "RequiredRole", None)
                setattr(value, "RequiredRole", self)

    @property
    def AssemblyContext60(self):
        return self.__AssemblyContext60

    @AssemblyContext60.setter
    def AssemblyContext60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_componentModel_AssemblyContext__AssemblyContext60", None)
        self.__AssemblyContext60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "providedrole"):
                opp_val = getattr(old_value, "providedrole", None)
                if opp_val == self:
                    setattr(old_value, "providedrole", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "providedrole"):
                opp_val = getattr(value, "providedrole", None)
                setattr(value, "providedrole", self)

    @property
    def componentModel_AssemblyContext51(self):
        return self.__componentModel_AssemblyContext51

    @componentModel_AssemblyContext51.setter
    def componentModel_AssemblyContext51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_componentModel_AssemblyContext__componentModel_AssemblyContext51", None)
        self.__componentModel_AssemblyContext51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "componentModel_System"):
                opp_val = getattr(old_value, "componentModel_System", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "componentModel_System"):
                opp_val = getattr(value, "componentModel_System", None)
                if opp_val is None:
                    setattr(value, "componentModel_System", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def AssemblyContext(self):
        return self.__AssemblyContext

    @AssemblyContext.setter
    def AssemblyContext(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_componentModel_AssemblyContext__AssemblyContext", None)
        self.__AssemblyContext = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "requiredrole"):
                opp_val = getattr(old_value, "requiredrole", None)
                if opp_val == self:
                    setattr(old_value, "requiredrole", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "requiredrole"):
                opp_val = getattr(value, "requiredrole", None)
                setattr(value, "requiredrole", self)

    @property
    def componentModel_AssemblyContext(self):
        return self.__componentModel_AssemblyContext

    @componentModel_AssemblyContext.setter
    def componentModel_AssemblyContext(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_componentModel_AssemblyContext__componentModel_AssemblyContext", None)
        self.__componentModel_AssemblyContext = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "componentModel_Component30"):
                opp_val = getattr(old_value, "componentModel_Component30", None)
                if opp_val == self:
                    setattr(old_value, "componentModel_Component30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "componentModel_Component30"):
                opp_val = getattr(value, "componentModel_Component30", None)
                setattr(value, "componentModel_Component30", self)

    @property
    def componentModel_AssemblyContext71(self):
        return self.__componentModel_AssemblyContext71

    @componentModel_AssemblyContext71.setter
    def componentModel_AssemblyContext71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_componentModel_AssemblyContext__componentModel_AssemblyContext71", None)
        self.__componentModel_AssemblyContext71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "componentModel_CompositeComponent"):
                opp_val = getattr(old_value, "componentModel_CompositeComponent", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "componentModel_CompositeComponent"):
                opp_val = getattr(value, "componentModel_CompositeComponent", None)
                if opp_val is None:
                    setattr(value, "componentModel_CompositeComponent", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def assemblycontext(self):
        return self.__assemblycontext

    @assemblycontext.setter
    def assemblycontext(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_componentModel_AssemblyContext__assemblycontext", None)
        self.__assemblycontext = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ProvidedRole"):
                opp_val = getattr(old_value, "ProvidedRole", None)
                if opp_val == self:
                    setattr(old_value, "ProvidedRole", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ProvidedRole"):
                opp_val = getattr(value, "ProvidedRole", None)
                setattr(value, "ProvidedRole", self)

class componentModel_ViewType(ABC):

    pass
class componentModel_Signature:

    def __init__(self, name: str, componentModel_Signature: "componentModel_Interface" = None, componentModel_Signature41: set["componentModel_Parameter"] = None, componentModel_Signature43: "componentModel_Type" = None, componentModel_Signature49: "componentModel_Service" = None):
        self.name = name
        self.componentModel_Signature = componentModel_Signature
        self.componentModel_Signature41 = componentModel_Signature41 if componentModel_Signature41 is not None else set()
        self.componentModel_Signature43 = componentModel_Signature43
        self.componentModel_Signature49 = componentModel_Signature49
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def componentModel_Signature(self):
        return self.__componentModel_Signature

    @componentModel_Signature.setter
    def componentModel_Signature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_componentModel_Signature__componentModel_Signature", None)
        self.__componentModel_Signature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "componentModel_Interface25"):
                opp_val = getattr(old_value, "componentModel_Interface25", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "componentModel_Interface25"):
                opp_val = getattr(value, "componentModel_Interface25", None)
                if opp_val is None:
                    setattr(value, "componentModel_Interface25", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def componentModel_Signature43(self):
        return self.__componentModel_Signature43

    @componentModel_Signature43.setter
    def componentModel_Signature43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_componentModel_Signature__componentModel_Signature43", None)
        self.__componentModel_Signature43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "componentModel_Type"):
                opp_val = getattr(old_value, "componentModel_Type", None)
                if opp_val == self:
                    setattr(old_value, "componentModel_Type", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "componentModel_Type"):
                opp_val = getattr(value, "componentModel_Type", None)
                setattr(value, "componentModel_Type", self)

    @property
    def componentModel_Signature41(self):
        return self.__componentModel_Signature41

    @componentModel_Signature41.setter
    def componentModel_Signature41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_componentModel_Signature__componentModel_Signature41", None)
        self.__componentModel_Signature41 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "componentModel_Parameter"):
                    opp_val = getattr(item, "componentModel_Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "componentModel_Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "componentModel_Parameter"):
                    opp_val = getattr(item, "componentModel_Parameter", None)
                    
                    setattr(item, "componentModel_Parameter", self)
                    

    @property
    def componentModel_Signature49(self):
        return self.__componentModel_Signature49

    @componentModel_Signature49.setter
    def componentModel_Signature49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_componentModel_Signature__componentModel_Signature49", None)
        self.__componentModel_Signature49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "componentModel_Service48"):
                opp_val = getattr(old_value, "componentModel_Service48", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "componentModel_Service48"):
                opp_val = getattr(value, "componentModel_Service48", None)
                if opp_val is None:
                    setattr(value, "componentModel_Service48", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Action:

    pass
class componentModel_Loop(Action):

    pass
class componentModel_ExternalCall(Action):

    pass
class componentModel_InternalAction(Action):

    pass
class componentModel_Branch(Action):

    pass
class componentModel_Action:

    pass
class componentModel_Service:

    pass
class componentModel_DelegationConnector(ABC):

    pass
class componentModel_AssemblyConnector:

    pass
class componentModel_RequiredRole:

    def __init__(self, name: str, RequiredRole: "componentModel_AssemblyContext" = None, componentModel_RequiredRole: "componentModel_AssemblyConnector" = None, componentModel_RequiredRole36: "componentModel_RequiredDelegationConnector" = None, requiredrole: "componentModel_AssemblyContext" = None, componentModel_RequiredRole57: "componentModel_Interface" = None):
        self.name = name
        self.RequiredRole = RequiredRole
        self.componentModel_RequiredRole = componentModel_RequiredRole
        self.componentModel_RequiredRole36 = componentModel_RequiredRole36
        self.requiredrole = requiredrole
        self.componentModel_RequiredRole57 = componentModel_RequiredRole57
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def requiredrole(self):
        return self.__requiredrole

    @requiredrole.setter
    def requiredrole(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_componentModel_RequiredRole__requiredrole", None)
        self.__requiredrole = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AssemblyContext"):
                opp_val = getattr(old_value, "AssemblyContext", None)
                if opp_val == self:
                    setattr(old_value, "AssemblyContext", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AssemblyContext"):
                opp_val = getattr(value, "AssemblyContext", None)
                setattr(value, "AssemblyContext", self)

    @property
    def RequiredRole(self):
        return self.__RequiredRole

    @RequiredRole.setter
    def RequiredRole(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_componentModel_RequiredRole__RequiredRole", None)
        self.__RequiredRole = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "assemblycontext28"):
                opp_val = getattr(old_value, "assemblycontext28", None)
                if opp_val == self:
                    setattr(old_value, "assemblycontext28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "assemblycontext28"):
                opp_val = getattr(value, "assemblycontext28", None)
                setattr(value, "assemblycontext28", self)

    @property
    def componentModel_RequiredRole(self):
        return self.__componentModel_RequiredRole

    @componentModel_RequiredRole.setter
    def componentModel_RequiredRole(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_componentModel_RequiredRole__componentModel_RequiredRole", None)
        self.__componentModel_RequiredRole = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "componentModel_AssemblyConnector34"):
                opp_val = getattr(old_value, "componentModel_AssemblyConnector34", None)
                if opp_val == self:
                    setattr(old_value, "componentModel_AssemblyConnector34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "componentModel_AssemblyConnector34"):
                opp_val = getattr(value, "componentModel_AssemblyConnector34", None)
                setattr(value, "componentModel_AssemblyConnector34", self)

    @property
    def componentModel_RequiredRole57(self):
        return self.__componentModel_RequiredRole57

    @componentModel_RequiredRole57.setter
    def componentModel_RequiredRole57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_componentModel_RequiredRole__componentModel_RequiredRole57", None)
        self.__componentModel_RequiredRole57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "componentModel_Interface58"):
                opp_val = getattr(old_value, "componentModel_Interface58", None)
                if opp_val == self:
                    setattr(old_value, "componentModel_Interface58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "componentModel_Interface58"):
                opp_val = getattr(value, "componentModel_Interface58", None)
                setattr(value, "componentModel_Interface58", self)

    @property
    def componentModel_RequiredRole36(self):
        return self.__componentModel_RequiredRole36

    @componentModel_RequiredRole36.setter
    def componentModel_RequiredRole36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_componentModel_RequiredRole__componentModel_RequiredRole36", None)
        self.__componentModel_RequiredRole36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "componentModel_RequiredDelegationConnector"):
                opp_val = getattr(old_value, "componentModel_RequiredDelegationConnector", None)
                if opp_val == self:
                    setattr(old_value, "componentModel_RequiredDelegationConnector", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "componentModel_RequiredDelegationConnector"):
                opp_val = getattr(value, "componentModel_RequiredDelegationConnector", None)
                setattr(value, "componentModel_RequiredDelegationConnector", self)

class componentModel_Component:

    def __init__(self, name: str, componentModel_Component4: "componentModel_ServiceEffectSpecification" = None, componentModel_Component: "componentModel_Repository" = None, componentModel_Component30: "componentModel_AssemblyContext" = None, componentModel_Component6: set["componentModel_InterfaceServiceMapTuple"] = None, componentModel_Component8: set["componentModel_AssemblyConnector"] = None, componentModel_Component10: set["componentModel_DelegationConnector"] = None):
        self.name = name
        self.componentModel_Component4 = componentModel_Component4
        self.componentModel_Component = componentModel_Component
        self.componentModel_Component30 = componentModel_Component30
        self.componentModel_Component6 = componentModel_Component6 if componentModel_Component6 is not None else set()
        self.componentModel_Component8 = componentModel_Component8 if componentModel_Component8 is not None else set()
        self.componentModel_Component10 = componentModel_Component10 if componentModel_Component10 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def componentModel_Component30(self):
        return self.__componentModel_Component30

    @componentModel_Component30.setter
    def componentModel_Component30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_componentModel_Component__componentModel_Component30", None)
        self.__componentModel_Component30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "componentModel_AssemblyContext"):
                opp_val = getattr(old_value, "componentModel_AssemblyContext", None)
                if opp_val == self:
                    setattr(old_value, "componentModel_AssemblyContext", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "componentModel_AssemblyContext"):
                opp_val = getattr(value, "componentModel_AssemblyContext", None)
                setattr(value, "componentModel_AssemblyContext", self)

    @property
    def componentModel_Component4(self):
        return self.__componentModel_Component4

    @componentModel_Component4.setter
    def componentModel_Component4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_componentModel_Component__componentModel_Component4", None)
        self.__componentModel_Component4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "componentModel_ServiceEffectSpecification"):
                opp_val = getattr(old_value, "componentModel_ServiceEffectSpecification", None)
                if opp_val == self:
                    setattr(old_value, "componentModel_ServiceEffectSpecification", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "componentModel_ServiceEffectSpecification"):
                opp_val = getattr(value, "componentModel_ServiceEffectSpecification", None)
                setattr(value, "componentModel_ServiceEffectSpecification", self)

    @property
    def componentModel_Component10(self):
        return self.__componentModel_Component10

    @componentModel_Component10.setter
    def componentModel_Component10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_componentModel_Component__componentModel_Component10", None)
        self.__componentModel_Component10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "componentModel_DelegationConnector"):
                    opp_val = getattr(item, "componentModel_DelegationConnector", None)
                    
                    if opp_val == self:
                        setattr(item, "componentModel_DelegationConnector", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "componentModel_DelegationConnector"):
                    opp_val = getattr(item, "componentModel_DelegationConnector", None)
                    
                    setattr(item, "componentModel_DelegationConnector", self)
                    

    @property
    def componentModel_Component8(self):
        return self.__componentModel_Component8

    @componentModel_Component8.setter
    def componentModel_Component8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_componentModel_Component__componentModel_Component8", None)
        self.__componentModel_Component8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "componentModel_AssemblyConnector"):
                    opp_val = getattr(item, "componentModel_AssemblyConnector", None)
                    
                    if opp_val == self:
                        setattr(item, "componentModel_AssemblyConnector", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "componentModel_AssemblyConnector"):
                    opp_val = getattr(item, "componentModel_AssemblyConnector", None)
                    
                    setattr(item, "componentModel_AssemblyConnector", self)
                    

    @property
    def componentModel_Component6(self):
        return self.__componentModel_Component6

    @componentModel_Component6.setter
    def componentModel_Component6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_componentModel_Component__componentModel_Component6", None)
        self.__componentModel_Component6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "componentModel_InterfaceServiceMapTuple"):
                    opp_val = getattr(item, "componentModel_InterfaceServiceMapTuple", None)
                    
                    if opp_val == self:
                        setattr(item, "componentModel_InterfaceServiceMapTuple", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "componentModel_InterfaceServiceMapTuple"):
                    opp_val = getattr(item, "componentModel_InterfaceServiceMapTuple", None)
                    
                    setattr(item, "componentModel_InterfaceServiceMapTuple", self)
                    

    @property
    def componentModel_Component(self):
        return self.__componentModel_Component

    @componentModel_Component.setter
    def componentModel_Component(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_componentModel_Component__componentModel_Component", None)
        self.__componentModel_Component = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "componentModel_Repository"):
                opp_val = getattr(old_value, "componentModel_Repository", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "componentModel_Repository"):
                opp_val = getattr(value, "componentModel_Repository", None)
                if opp_val is None:
                    setattr(value, "componentModel_Repository", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ViewType:

    pass
class componentModel_EnvironmentViewType(ViewType):

    pass
class componentModel_RepositoryViewType(ViewType):

    pass
class componentModel_AllocationViewType(ViewType):

    pass
class componentModel_AssemblyViewType(ViewType):

    pass
class componentModel_Repository(ViewType):

    pass
class ViewPoint:

    pass
class componentModel_DeploymentViewPoint(ViewPoint):

    pass
class componentModel_AssemblyViewPoint(ViewPoint):

    pass
class componentModel_SystemIndependentViewPoint(ViewPoint):

    pass
class componentModel_InterfaceServiceMapTuple:

    pass
class componentModel_ServiceEffectSpecification:

    pass
class componentModel_Interface:

    def __init__(self, name: str, componentModel_Interface: "componentModel_Repository" = None, componentModel_Interface13: "componentModel_InterfaceServiceMapTuple" = None, componentModel_Interface25: set["componentModel_Signature"] = None, componentModel_Interface39: "componentModel_RequiredDelegationConnector" = None, componentModel_Interface46: "componentModel_Service" = None, componentModel_Interface54: "componentModel_System" = None, componentModel_Interface58: "componentModel_RequiredRole" = None, componentModel_Interface63: "componentModel_ProvidedRole" = None, componentModel_Interface65: "componentModel_ProvidedDelegationConnector" = None):
        self.name = name
        self.componentModel_Interface = componentModel_Interface
        self.componentModel_Interface13 = componentModel_Interface13
        self.componentModel_Interface25 = componentModel_Interface25 if componentModel_Interface25 is not None else set()
        self.componentModel_Interface39 = componentModel_Interface39
        self.componentModel_Interface46 = componentModel_Interface46
        self.componentModel_Interface54 = componentModel_Interface54
        self.componentModel_Interface58 = componentModel_Interface58
        self.componentModel_Interface63 = componentModel_Interface63
        self.componentModel_Interface65 = componentModel_Interface65
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def componentModel_Interface(self):
        return self.__componentModel_Interface

    @componentModel_Interface.setter
    def componentModel_Interface(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_componentModel_Interface__componentModel_Interface", None)
        self.__componentModel_Interface = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "componentModel_Repository2"):
                opp_val = getattr(old_value, "componentModel_Repository2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "componentModel_Repository2"):
                opp_val = getattr(value, "componentModel_Repository2", None)
                if opp_val is None:
                    setattr(value, "componentModel_Repository2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def componentModel_Interface39(self):
        return self.__componentModel_Interface39

    @componentModel_Interface39.setter
    def componentModel_Interface39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_componentModel_Interface__componentModel_Interface39", None)
        self.__componentModel_Interface39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "componentModel_RequiredDelegationConnector38"):
                opp_val = getattr(old_value, "componentModel_RequiredDelegationConnector38", None)
                if opp_val == self:
                    setattr(old_value, "componentModel_RequiredDelegationConnector38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "componentModel_RequiredDelegationConnector38"):
                opp_val = getattr(value, "componentModel_RequiredDelegationConnector38", None)
                setattr(value, "componentModel_RequiredDelegationConnector38", self)

    @property
    def componentModel_Interface13(self):
        return self.__componentModel_Interface13

    @componentModel_Interface13.setter
    def componentModel_Interface13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_componentModel_Interface__componentModel_Interface13", None)
        self.__componentModel_Interface13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "componentModel_InterfaceServiceMapTuple12"):
                opp_val = getattr(old_value, "componentModel_InterfaceServiceMapTuple12", None)
                if opp_val == self:
                    setattr(old_value, "componentModel_InterfaceServiceMapTuple12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "componentModel_InterfaceServiceMapTuple12"):
                opp_val = getattr(value, "componentModel_InterfaceServiceMapTuple12", None)
                setattr(value, "componentModel_InterfaceServiceMapTuple12", self)

    @property
    def componentModel_Interface65(self):
        return self.__componentModel_Interface65

    @componentModel_Interface65.setter
    def componentModel_Interface65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_componentModel_Interface__componentModel_Interface65", None)
        self.__componentModel_Interface65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "componentModel_ProvidedDelegationConnector"):
                opp_val = getattr(old_value, "componentModel_ProvidedDelegationConnector", None)
                if opp_val == self:
                    setattr(old_value, "componentModel_ProvidedDelegationConnector", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "componentModel_ProvidedDelegationConnector"):
                opp_val = getattr(value, "componentModel_ProvidedDelegationConnector", None)
                setattr(value, "componentModel_ProvidedDelegationConnector", self)

    @property
    def componentModel_Interface58(self):
        return self.__componentModel_Interface58

    @componentModel_Interface58.setter
    def componentModel_Interface58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_componentModel_Interface__componentModel_Interface58", None)
        self.__componentModel_Interface58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "componentModel_RequiredRole57"):
                opp_val = getattr(old_value, "componentModel_RequiredRole57", None)
                if opp_val == self:
                    setattr(old_value, "componentModel_RequiredRole57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "componentModel_RequiredRole57"):
                opp_val = getattr(value, "componentModel_RequiredRole57", None)
                setattr(value, "componentModel_RequiredRole57", self)

    @property
    def componentModel_Interface46(self):
        return self.__componentModel_Interface46

    @componentModel_Interface46.setter
    def componentModel_Interface46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_componentModel_Interface__componentModel_Interface46", None)
        self.__componentModel_Interface46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "componentModel_Service45"):
                opp_val = getattr(old_value, "componentModel_Service45", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "componentModel_Service45"):
                opp_val = getattr(value, "componentModel_Service45", None)
                if opp_val is None:
                    setattr(value, "componentModel_Service45", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def componentModel_Interface63(self):
        return self.__componentModel_Interface63

    @componentModel_Interface63.setter
    def componentModel_Interface63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_componentModel_Interface__componentModel_Interface63", None)
        self.__componentModel_Interface63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "componentModel_ProvidedRole62"):
                opp_val = getattr(old_value, "componentModel_ProvidedRole62", None)
                if opp_val == self:
                    setattr(old_value, "componentModel_ProvidedRole62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "componentModel_ProvidedRole62"):
                opp_val = getattr(value, "componentModel_ProvidedRole62", None)
                setattr(value, "componentModel_ProvidedRole62", self)

    @property
    def componentModel_Interface54(self):
        return self.__componentModel_Interface54

    @componentModel_Interface54.setter
    def componentModel_Interface54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_componentModel_Interface__componentModel_Interface54", None)
        self.__componentModel_Interface54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "componentModel_System53"):
                opp_val = getattr(old_value, "componentModel_System53", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "componentModel_System53"):
                opp_val = getattr(value, "componentModel_System53", None)
                if opp_val is None:
                    setattr(value, "componentModel_System53", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def componentModel_Interface25(self):
        return self.__componentModel_Interface25

    @componentModel_Interface25.setter
    def componentModel_Interface25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_componentModel_Interface__componentModel_Interface25", None)
        self.__componentModel_Interface25 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "componentModel_Signature"):
                    opp_val = getattr(item, "componentModel_Signature", None)
                    
                    if opp_val == self:
                        setattr(item, "componentModel_Signature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "componentModel_Signature"):
                    opp_val = getattr(item, "componentModel_Signature", None)
                    
                    setattr(item, "componentModel_Signature", self)
                    
