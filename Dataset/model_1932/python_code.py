from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class PlatformLayers(Enum):
    ServiceLayer = "ServiceLayer"
    UILayer = "UILayer"
class Comparator(Enum):
    EQ = "EQ"
    NEQ = "NEQ"
    GT = "GT"
    GEQ = "GEQ"
    LT = "LT"
    LEQ = "LEQ"
class RelationType(Enum):
    One2One = "One2One"
    One2Many = "One2Many"
    Many2Many = "Many2Many"
class Order(Enum):
    ASC = "ASC"
    DESC = "DESC"
class Orientation(Enum):
    Top = "Top"
    Bottom = "Bottom"
    Left = "Left"
    Right = "Right"


############################################
# Definition of Classes
############################################

class MenuElement:

    pass
class domain_MenuSeparator(MenuElement):

    pass
class MenuExtensionRef:

    pass
class domain_MenuExtensionPoint(MenuElement, MenuExtensionRef):

    pass
class domain_MenuExtensionRef:

    pass
class domain_MenuHolder:

    pass
class domain_InfrastructureComponent:

    def __init__(self, uid: str, name: str, domain_InfrastructureComponent: "domain_InfrastructureConnection" = None, domain_InfrastructureComponent582: "domain_InfrastructureConnection" = None, infrastructureComponent: "domain_InfrastructureLayer" = None, InfrastructureComponent: "domain_InfrastructureLayer" = None):
        self.uid = uid
        self.name = name
        self.domain_InfrastructureComponent = domain_InfrastructureComponent
        self.domain_InfrastructureComponent582 = domain_InfrastructureComponent582
        self.infrastructureComponent = infrastructureComponent
        self.InfrastructureComponent = InfrastructureComponent
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def domain_InfrastructureComponent582(self):
        return self.__domain_InfrastructureComponent582

    @domain_InfrastructureComponent582.setter
    def domain_InfrastructureComponent582(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_InfrastructureComponent__domain_InfrastructureComponent582", None)
        self.__domain_InfrastructureComponent582 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_InfrastructureConnection581"):
                opp_val = getattr(old_value, "domain_InfrastructureConnection581", None)
                if opp_val == self:
                    setattr(old_value, "domain_InfrastructureConnection581", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_InfrastructureConnection581"):
                opp_val = getattr(value, "domain_InfrastructureConnection581", None)
                setattr(value, "domain_InfrastructureConnection581", self)

    @property
    def domain_InfrastructureComponent(self):
        return self.__domain_InfrastructureComponent

    @domain_InfrastructureComponent.setter
    def domain_InfrastructureComponent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_InfrastructureComponent__domain_InfrastructureComponent", None)
        self.__domain_InfrastructureComponent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_InfrastructureConnection579"):
                opp_val = getattr(old_value, "domain_InfrastructureConnection579", None)
                if opp_val == self:
                    setattr(old_value, "domain_InfrastructureConnection579", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_InfrastructureConnection579"):
                opp_val = getattr(value, "domain_InfrastructureConnection579", None)
                setattr(value, "domain_InfrastructureConnection579", self)

    @property
    def InfrastructureComponent(self):
        return self.__InfrastructureComponent

    @InfrastructureComponent.setter
    def InfrastructureComponent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_InfrastructureComponent__InfrastructureComponent", None)
        self.__InfrastructureComponent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent577"):
                opp_val = getattr(old_value, "parent577", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent577"):
                opp_val = getattr(value, "parent577", None)
                if opp_val is None:
                    setattr(value, "parent577", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def infrastructureComponent(self):
        return self.__infrastructureComponent

    @infrastructureComponent.setter
    def infrastructureComponent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_InfrastructureComponent__infrastructureComponent", None)
        self.__infrastructureComponent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "InfrastructureLayer584"):
                opp_val = getattr(old_value, "InfrastructureLayer584", None)
                if opp_val == self:
                    setattr(old_value, "InfrastructureLayer584", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "InfrastructureLayer584"):
                opp_val = getattr(value, "InfrastructureLayer584", None)
                setattr(value, "InfrastructureLayer584", self)

class InfrastructureComponent:

    pass
class domain_Hub(InfrastructureComponent):

    pass
class domain_ServerClaster(InfrastructureComponent):

    pass
class domain_Storage(InfrastructureComponent):

    pass
class domain_Router(InfrastructureComponent):

    pass
class domain_Server(InfrastructureComponent):

    pass
class domain_InfrastructureLayer:

    def __init__(self, uid: str, name: str, InfrastructureLayer: "domain_Subsystem" = None, InfrastructureLayer584: "domain_InfrastructureComponent" = None, infrastructureLayer: "domain_Subsystem" = None, parent577: set["domain_InfrastructureComponent"] = None):
        self.uid = uid
        self.name = name
        self.InfrastructureLayer = InfrastructureLayer
        self.InfrastructureLayer584 = InfrastructureLayer584
        self.infrastructureLayer = infrastructureLayer
        self.parent577 = parent577 if parent577 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def parent577(self):
        return self.__parent577

    @parent577.setter
    def parent577(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_InfrastructureLayer__parent577", None)
        self.__parent577 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "InfrastructureComponent"):
                    opp_val = getattr(item, "InfrastructureComponent", None)
                    
                    if opp_val == self:
                        setattr(item, "InfrastructureComponent", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "InfrastructureComponent"):
                    opp_val = getattr(item, "InfrastructureComponent", None)
                    
                    setattr(item, "InfrastructureComponent", self)
                    

    @property
    def InfrastructureLayer584(self):
        return self.__InfrastructureLayer584

    @InfrastructureLayer584.setter
    def InfrastructureLayer584(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_InfrastructureLayer__InfrastructureLayer584", None)
        self.__InfrastructureLayer584 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "infrastructureComponent"):
                opp_val = getattr(old_value, "infrastructureComponent", None)
                if opp_val == self:
                    setattr(old_value, "infrastructureComponent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "infrastructureComponent"):
                opp_val = getattr(value, "infrastructureComponent", None)
                setattr(value, "infrastructureComponent", self)

    @property
    def InfrastructureLayer(self):
        return self.__InfrastructureLayer

    @InfrastructureLayer.setter
    def InfrastructureLayer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_InfrastructureLayer__InfrastructureLayer", None)
        self.__InfrastructureLayer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent573"):
                opp_val = getattr(old_value, "parent573", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent573"):
                opp_val = getattr(value, "parent573", None)
                if opp_val is None:
                    setattr(value, "parent573", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def infrastructureLayer(self):
        return self.__infrastructureLayer

    @infrastructureLayer.setter
    def infrastructureLayer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_InfrastructureLayer__infrastructureLayer", None)
        self.__infrastructureLayer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Subsystem575"):
                opp_val = getattr(old_value, "Subsystem575", None)
                if opp_val == self:
                    setattr(old_value, "Subsystem575", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Subsystem575"):
                opp_val = getattr(value, "Subsystem575", None)
                setattr(value, "Subsystem575", self)

class domain_Subsystem:

    def __init__(self, uid: str, name: str, Subsystem: "domain_Datacenter" = None, subsystems: "domain_Datacenter" = None, parent573: set["domain_InfrastructureLayer"] = None, Subsystem575: "domain_InfrastructureLayer" = None):
        self.uid = uid
        self.name = name
        self.Subsystem = Subsystem
        self.subsystems = subsystems
        self.parent573 = parent573 if parent573 is not None else set()
        self.Subsystem575 = Subsystem575
        
    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def subsystems(self):
        return self.__subsystems

    @subsystems.setter
    def subsystems(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Subsystem__subsystems", None)
        self.__subsystems = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Datacenter571"):
                opp_val = getattr(old_value, "Datacenter571", None)
                if opp_val == self:
                    setattr(old_value, "Datacenter571", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Datacenter571"):
                opp_val = getattr(value, "Datacenter571", None)
                setattr(value, "Datacenter571", self)

    @property
    def Subsystem(self):
        return self.__Subsystem

    @Subsystem.setter
    def Subsystem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Subsystem__Subsystem", None)
        self.__Subsystem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent569"):
                opp_val = getattr(old_value, "parent569", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent569"):
                opp_val = getattr(value, "parent569", None)
                if opp_val is None:
                    setattr(value, "parent569", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def parent573(self):
        return self.__parent573

    @parent573.setter
    def parent573(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Subsystem__parent573", None)
        self.__parent573 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "InfrastructureLayer"):
                    opp_val = getattr(item, "InfrastructureLayer", None)
                    
                    if opp_val == self:
                        setattr(item, "InfrastructureLayer", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "InfrastructureLayer"):
                    opp_val = getattr(item, "InfrastructureLayer", None)
                    
                    setattr(item, "InfrastructureLayer", self)
                    

    @property
    def Subsystem575(self):
        return self.__Subsystem575

    @Subsystem575.setter
    def Subsystem575(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Subsystem__Subsystem575", None)
        self.__Subsystem575 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "infrastructureLayer"):
                opp_val = getattr(old_value, "infrastructureLayer", None)
                if opp_val == self:
                    setattr(old_value, "infrastructureLayer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "infrastructureLayer"):
                opp_val = getattr(value, "infrastructureLayer", None)
                setattr(value, "infrastructureLayer", self)

class domain_InfrastructureConnection:

    def __init__(self, uid: str, domain_InfrastructureConnection: "domain_EnterpriseInfrastructure" = None, domain_InfrastructureConnection579: "domain_InfrastructureComponent" = None, domain_InfrastructureConnection581: "domain_InfrastructureComponent" = None):
        self.uid = uid
        self.domain_InfrastructureConnection = domain_InfrastructureConnection
        self.domain_InfrastructureConnection579 = domain_InfrastructureConnection579
        self.domain_InfrastructureConnection581 = domain_InfrastructureConnection581
        
    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def domain_InfrastructureConnection579(self):
        return self.__domain_InfrastructureConnection579

    @domain_InfrastructureConnection579.setter
    def domain_InfrastructureConnection579(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_InfrastructureConnection__domain_InfrastructureConnection579", None)
        self.__domain_InfrastructureConnection579 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_InfrastructureComponent"):
                opp_val = getattr(old_value, "domain_InfrastructureComponent", None)
                if opp_val == self:
                    setattr(old_value, "domain_InfrastructureComponent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_InfrastructureComponent"):
                opp_val = getattr(value, "domain_InfrastructureComponent", None)
                setattr(value, "domain_InfrastructureComponent", self)

    @property
    def domain_InfrastructureConnection581(self):
        return self.__domain_InfrastructureConnection581

    @domain_InfrastructureConnection581.setter
    def domain_InfrastructureConnection581(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_InfrastructureConnection__domain_InfrastructureConnection581", None)
        self.__domain_InfrastructureConnection581 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_InfrastructureComponent582"):
                opp_val = getattr(old_value, "domain_InfrastructureComponent582", None)
                if opp_val == self:
                    setattr(old_value, "domain_InfrastructureComponent582", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_InfrastructureComponent582"):
                opp_val = getattr(value, "domain_InfrastructureComponent582", None)
                setattr(value, "domain_InfrastructureComponent582", self)

    @property
    def domain_InfrastructureConnection(self):
        return self.__domain_InfrastructureConnection

    @domain_InfrastructureConnection.setter
    def domain_InfrastructureConnection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_InfrastructureConnection__domain_InfrastructureConnection", None)
        self.__domain_InfrastructureConnection = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_EnterpriseInfrastructure"):
                opp_val = getattr(old_value, "domain_EnterpriseInfrastructure", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_EnterpriseInfrastructure"):
                opp_val = getattr(value, "domain_EnterpriseInfrastructure", None)
                if opp_val is None:
                    setattr(value, "domain_EnterpriseInfrastructure", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class domain_EnterpriseInfrastructure:

    def __init__(self, uid: str, EnterpriseInfrastructure: "domain_ApplicationInfrastructureLayer" = None, infarastructure: "domain_ApplicationInfrastructureLayer" = None, parent561: set["domain_Datacenter"] = None, domain_EnterpriseInfrastructure: set["domain_InfrastructureConnection"] = None, domain_EnterpriseInfrastructure564: "domain_EObject" = None, EnterpriseInfrastructure567: "domain_Datacenter" = None):
        self.uid = uid
        self.EnterpriseInfrastructure = EnterpriseInfrastructure
        self.infarastructure = infarastructure
        self.parent561 = parent561 if parent561 is not None else set()
        self.domain_EnterpriseInfrastructure = domain_EnterpriseInfrastructure if domain_EnterpriseInfrastructure is not None else set()
        self.domain_EnterpriseInfrastructure564 = domain_EnterpriseInfrastructure564
        self.EnterpriseInfrastructure567 = EnterpriseInfrastructure567
        
    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def EnterpriseInfrastructure567(self):
        return self.__EnterpriseInfrastructure567

    @EnterpriseInfrastructure567.setter
    def EnterpriseInfrastructure567(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_EnterpriseInfrastructure__EnterpriseInfrastructure567", None)
        self.__EnterpriseInfrastructure567 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datacenters"):
                opp_val = getattr(old_value, "datacenters", None)
                if opp_val == self:
                    setattr(old_value, "datacenters", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datacenters"):
                opp_val = getattr(value, "datacenters", None)
                setattr(value, "datacenters", self)

    @property
    def parent561(self):
        return self.__parent561

    @parent561.setter
    def parent561(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_EnterpriseInfrastructure__parent561", None)
        self.__parent561 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Datacenter"):
                    opp_val = getattr(item, "Datacenter", None)
                    
                    if opp_val == self:
                        setattr(item, "Datacenter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Datacenter"):
                    opp_val = getattr(item, "Datacenter", None)
                    
                    setattr(item, "Datacenter", self)
                    

    @property
    def infarastructure(self):
        return self.__infarastructure

    @infarastructure.setter
    def infarastructure(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_EnterpriseInfrastructure__infarastructure", None)
        self.__infarastructure = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ApplicationInfrastructureLayer559"):
                opp_val = getattr(old_value, "ApplicationInfrastructureLayer559", None)
                if opp_val == self:
                    setattr(old_value, "ApplicationInfrastructureLayer559", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ApplicationInfrastructureLayer559"):
                opp_val = getattr(value, "ApplicationInfrastructureLayer559", None)
                setattr(value, "ApplicationInfrastructureLayer559", self)

    @property
    def domain_EnterpriseInfrastructure(self):
        return self.__domain_EnterpriseInfrastructure

    @domain_EnterpriseInfrastructure.setter
    def domain_EnterpriseInfrastructure(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_EnterpriseInfrastructure__domain_EnterpriseInfrastructure", None)
        self.__domain_EnterpriseInfrastructure = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "domain_InfrastructureConnection"):
                    opp_val = getattr(item, "domain_InfrastructureConnection", None)
                    
                    if opp_val == self:
                        setattr(item, "domain_InfrastructureConnection", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "domain_InfrastructureConnection"):
                    opp_val = getattr(item, "domain_InfrastructureConnection", None)
                    
                    setattr(item, "domain_InfrastructureConnection", self)
                    

    @property
    def domain_EnterpriseInfrastructure564(self):
        return self.__domain_EnterpriseInfrastructure564

    @domain_EnterpriseInfrastructure564.setter
    def domain_EnterpriseInfrastructure564(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_EnterpriseInfrastructure__domain_EnterpriseInfrastructure564", None)
        self.__domain_EnterpriseInfrastructure564 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_EObject565"):
                opp_val = getattr(old_value, "domain_EObject565", None)
                if opp_val == self:
                    setattr(old_value, "domain_EObject565", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_EObject565"):
                opp_val = getattr(value, "domain_EObject565", None)
                setattr(value, "domain_EObject565", self)

    @property
    def EnterpriseInfrastructure(self):
        return self.__EnterpriseInfrastructure

    @EnterpriseInfrastructure.setter
    def EnterpriseInfrastructure(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_EnterpriseInfrastructure__EnterpriseInfrastructure", None)
        self.__EnterpriseInfrastructure = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent557"):
                opp_val = getattr(old_value, "parent557", None)
                if opp_val == self:
                    setattr(old_value, "parent557", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent557"):
                opp_val = getattr(value, "parent557", None)
                setattr(value, "parent557", self)

class domain_OrderBy:

    def __init__(self, uid: str, order: str, domain_OrderBy: "domain_Orders" = None, domain_OrderBy529: "domain_EObject" = None):
        self.uid = uid
        self.order = order
        self.domain_OrderBy = domain_OrderBy
        self.domain_OrderBy529 = domain_OrderBy529
        
    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def order(self) -> str:
        return self.__order

    @order.setter
    def order(self, order: str):
        self.__order = order

    @property
    def domain_OrderBy(self):
        return self.__domain_OrderBy

    @domain_OrderBy.setter
    def domain_OrderBy(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_OrderBy__domain_OrderBy", None)
        self.__domain_OrderBy = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_Orders527"):
                opp_val = getattr(old_value, "domain_Orders527", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_Orders527"):
                opp_val = getattr(value, "domain_Orders527", None)
                if opp_val is None:
                    setattr(value, "domain_Orders527", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def domain_OrderBy529(self):
        return self.__domain_OrderBy529

    @domain_OrderBy529.setter
    def domain_OrderBy529(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_OrderBy__domain_OrderBy529", None)
        self.__domain_OrderBy529 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_EObject530"):
                opp_val = getattr(old_value, "domain_EObject530", None)
                if opp_val == self:
                    setattr(old_value, "domain_EObject530", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_EObject530"):
                opp_val = getattr(value, "domain_EObject530", None)
                setattr(value, "domain_EObject530", self)

class domain_Orders:

    def __init__(self, uid: str, domain_Orders: "domain_DataControl" = None, domain_Orders527: set["domain_OrderBy"] = None):
        self.uid = uid
        self.domain_Orders = domain_Orders
        self.domain_Orders527 = domain_Orders527 if domain_Orders527 is not None else set()
        
    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def domain_Orders527(self):
        return self.__domain_Orders527

    @domain_Orders527.setter
    def domain_Orders527(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Orders__domain_Orders527", None)
        self.__domain_Orders527 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "domain_OrderBy"):
                    opp_val = getattr(item, "domain_OrderBy", None)
                    
                    if opp_val == self:
                        setattr(item, "domain_OrderBy", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "domain_OrderBy"):
                    opp_val = getattr(item, "domain_OrderBy", None)
                    
                    setattr(item, "domain_OrderBy", self)
                    

    @property
    def domain_Orders(self):
        return self.__domain_Orders

    @domain_Orders.setter
    def domain_Orders(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Orders__domain_Orders", None)
        self.__domain_Orders = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_DataControl525"):
                opp_val = getattr(old_value, "domain_DataControl525", None)
                if opp_val == self:
                    setattr(old_value, "domain_DataControl525", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_DataControl525"):
                opp_val = getattr(value, "domain_DataControl525", None)
                setattr(value, "domain_DataControl525", self)

class ProxiesList:

    pass
class domain_ProxiesList:

    pass
class domain_Relation:

    def __init__(self, uid: str, name: str, isTree: bool, domain_Relation: "domain_Controls" = None, domain_Relation532: "domain_DataControl" = None, domain_Relation535: "domain_DataControl" = None, domain_Relation538: set["domain_Link"] = None):
        self.uid = uid
        self.name = name
        self.isTree = isTree
        self.domain_Relation = domain_Relation
        self.domain_Relation532 = domain_Relation532
        self.domain_Relation535 = domain_Relation535
        self.domain_Relation538 = domain_Relation538 if domain_Relation538 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def isTree(self) -> bool:
        return self.__isTree

    @isTree.setter
    def isTree(self, isTree: bool):
        self.__isTree = isTree

    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def domain_Relation(self):
        return self.__domain_Relation

    @domain_Relation.setter
    def domain_Relation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Relation__domain_Relation", None)
        self.__domain_Relation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_Controls474"):
                opp_val = getattr(old_value, "domain_Controls474", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_Controls474"):
                opp_val = getattr(value, "domain_Controls474", None)
                if opp_val is None:
                    setattr(value, "domain_Controls474", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def domain_Relation532(self):
        return self.__domain_Relation532

    @domain_Relation532.setter
    def domain_Relation532(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Relation__domain_Relation532", None)
        self.__domain_Relation532 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_DataControl533"):
                opp_val = getattr(old_value, "domain_DataControl533", None)
                if opp_val == self:
                    setattr(old_value, "domain_DataControl533", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_DataControl533"):
                opp_val = getattr(value, "domain_DataControl533", None)
                setattr(value, "domain_DataControl533", self)

    @property
    def domain_Relation535(self):
        return self.__domain_Relation535

    @domain_Relation535.setter
    def domain_Relation535(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Relation__domain_Relation535", None)
        self.__domain_Relation535 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_DataControl536"):
                opp_val = getattr(old_value, "domain_DataControl536", None)
                if opp_val == self:
                    setattr(old_value, "domain_DataControl536", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_DataControl536"):
                opp_val = getattr(value, "domain_DataControl536", None)
                setattr(value, "domain_DataControl536", self)

    @property
    def domain_Relation538(self):
        return self.__domain_Relation538

    @domain_Relation538.setter
    def domain_Relation538(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Relation__domain_Relation538", None)
        self.__domain_Relation538 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "domain_Link539"):
                    opp_val = getattr(item, "domain_Link539", None)
                    
                    if opp_val == self:
                        setattr(item, "domain_Link539", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "domain_Link539"):
                    opp_val = getattr(item, "domain_Link539", None)
                    
                    setattr(item, "domain_Link539", self)
                    

class domain_Root:

    def __init__(self, uid: str, name: str, domain_Root: "domain_Controls" = None, domain_Root483: "domain_PREFormTrigger" = None, domain_Root485: set["domain_FormVariable"] = None):
        self.uid = uid
        self.name = name
        self.domain_Root = domain_Root
        self.domain_Root483 = domain_Root483
        self.domain_Root485 = domain_Root485 if domain_Root485 is not None else set()
        
    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def domain_Root483(self):
        return self.__domain_Root483

    @domain_Root483.setter
    def domain_Root483(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Root__domain_Root483", None)
        self.__domain_Root483 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_PREFormTrigger"):
                opp_val = getattr(old_value, "domain_PREFormTrigger", None)
                if opp_val == self:
                    setattr(old_value, "domain_PREFormTrigger", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_PREFormTrigger"):
                opp_val = getattr(value, "domain_PREFormTrigger", None)
                setattr(value, "domain_PREFormTrigger", self)

    @property
    def domain_Root485(self):
        return self.__domain_Root485

    @domain_Root485.setter
    def domain_Root485(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Root__domain_Root485", None)
        self.__domain_Root485 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "domain_FormVariable"):
                    opp_val = getattr(item, "domain_FormVariable", None)
                    
                    if opp_val == self:
                        setattr(item, "domain_FormVariable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "domain_FormVariable"):
                    opp_val = getattr(item, "domain_FormVariable", None)
                    
                    setattr(item, "domain_FormVariable", self)
                    

    @property
    def domain_Root(self):
        return self.__domain_Root

    @domain_Root.setter
    def domain_Root(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Root__domain_Root", None)
        self.__domain_Root = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_Controls"):
                opp_val = getattr(old_value, "domain_Controls", None)
                if opp_val == self:
                    setattr(old_value, "domain_Controls", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_Controls"):
                opp_val = getattr(value, "domain_Controls", None)
                setattr(value, "domain_Controls", self)

class MethodPointer:

    pass
class domain_Dependency:

    def __init__(self, uid: str, name: str, domain_Dependency: "domain_Controls" = None, domain_Dependency544: "domain_DataControl" = None, domain_Dependency541: "domain_DataControl" = None):
        self.uid = uid
        self.name = name
        self.domain_Dependency = domain_Dependency
        self.domain_Dependency544 = domain_Dependency544
        self.domain_Dependency541 = domain_Dependency541
        
    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def domain_Dependency541(self):
        return self.__domain_Dependency541

    @domain_Dependency541.setter
    def domain_Dependency541(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Dependency__domain_Dependency541", None)
        self.__domain_Dependency541 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_DataControl542"):
                opp_val = getattr(old_value, "domain_DataControl542", None)
                if opp_val == self:
                    setattr(old_value, "domain_DataControl542", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_DataControl542"):
                opp_val = getattr(value, "domain_DataControl542", None)
                setattr(value, "domain_DataControl542", self)

    @property
    def domain_Dependency(self):
        return self.__domain_Dependency

    @domain_Dependency.setter
    def domain_Dependency(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Dependency__domain_Dependency", None)
        self.__domain_Dependency = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_Controls476"):
                opp_val = getattr(old_value, "domain_Controls476", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_Controls476"):
                opp_val = getattr(value, "domain_Controls476", None)
                if opp_val is None:
                    setattr(value, "domain_Controls476", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def domain_Dependency544(self):
        return self.__domain_Dependency544

    @domain_Dependency544.setter
    def domain_Dependency544(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Dependency__domain_Dependency544", None)
        self.__domain_Dependency544 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_DataControl545"):
                opp_val = getattr(old_value, "domain_DataControl545", None)
                if opp_val == self:
                    setattr(old_value, "domain_DataControl545", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_DataControl545"):
                opp_val = getattr(value, "domain_DataControl545", None)
                setattr(value, "domain_DataControl545", self)

class ItemIcon:

    pass
class domain_SubMenu(MenuElement, ItemIcon):

    pass
class OptionSelection:

    pass
class domain_DropDownSelection(OptionSelection):

    def __init__(self, initialOptionValue: str, domain_DropDownSelection: "domain_Selection" = None, domain_DropDownSelection458: "domain_Context" = None):
        self.initialOptionValue = initialOptionValue
        self.domain_DropDownSelection = domain_DropDownSelection
        self.domain_DropDownSelection458 = domain_DropDownSelection458
        
    @property
    def initialOptionValue(self) -> str:
        return self.__initialOptionValue

    @initialOptionValue.setter
    def initialOptionValue(self, initialOptionValue: str):
        self.__initialOptionValue = initialOptionValue

    @property
    def domain_DropDownSelection(self):
        return self.__domain_DropDownSelection

    @domain_DropDownSelection.setter
    def domain_DropDownSelection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_DropDownSelection__domain_DropDownSelection", None)
        self.__domain_DropDownSelection = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_Selection456"):
                opp_val = getattr(old_value, "domain_Selection456", None)
                if opp_val == self:
                    setattr(old_value, "domain_Selection456", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_Selection456"):
                opp_val = getattr(value, "domain_Selection456", None)
                setattr(value, "domain_Selection456", self)

    @property
    def domain_DropDownSelection458(self):
        return self.__domain_DropDownSelection458

    @domain_DropDownSelection458.setter
    def domain_DropDownSelection458(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_DropDownSelection__domain_DropDownSelection458", None)
        self.__domain_DropDownSelection458 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_Context459"):
                opp_val = getattr(old_value, "domain_Context459", None)
                if opp_val == self:
                    setattr(old_value, "domain_Context459", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_Context459"):
                opp_val = getattr(value, "domain_Context459", None)
                setattr(value, "domain_Context459", self)

class SourcesPointer:

    pass
class Formatable:

    pass
class ChildrenHolder:

    pass
class InputElement:

    pass
class domain_Image(InputElement):

    pass
class domain_CheckBox(InputElement):

    pass
class domain_OutputText(InputElement, Formatable):

    pass
class domain_Date(InputElement, Formatable):

    pass
class domain_Password(InputElement, Formatable):

    pass
class domain_InputText(InputElement, Formatable):

    pass
class domain_OptionSelection(InputElement):

    pass
class domain_ItemIcon:

    pass
class domain_DataControl:

    def __init__(self, uid: str, name: str, domain_DataControl: "domain_SourcesPointer" = None, domain_DataControl448: "domain_OptionSelection" = None, domain_DataControl454: "domain_OptionSelection" = None, domain_DataControl441: "domain_SourcesPointer" = None, DataControl: "domain_Controls" = None, domain_DataControl490: "domain_TypePointer" = None, controls: "domain_Controls" = None, domain_DataControl498: "domain_PREQueryTrigger" = None, domain_DataControl500: "domain_POSTQueryTrigger" = None, domain_DataControl502: "domain_PREInsertTrigger" = None, domain_DataControl504: "domain_PREDeleteTrigger" = None, domain_DataControl493: "domain_TypePointer" = None, domain_DataControl508: "domain_PREUpdateTrigger" = None, domain_DataControl510: "domain_CreateTrigger" = None, domain_DataControl512: "domain_InsertTrigger" = None, domain_DataControl514: "domain_UpdateTrigger" = None, domain_DataControl516: "domain_DeleteTrigger" = None, domain_DataControl506: "domain_POSTCreateTrigger" = None, parent520: set["domain_ArtificialField"] = None, domain_DataControl522: "domain_ContextParameters" = None, domain_DataControl525: "domain_Orders" = None, domain_DataControl518: "domain_SearchTrigger" = None, domain_DataControl533: "domain_Relation" = None, domain_DataControl536: "domain_Relation" = None, DataControl547: "domain_ArtificialField" = None, domain_DataControl542: "domain_Dependency" = None, domain_DataControl545: "domain_Dependency" = None):
        self.uid = uid
        self.name = name
        self.domain_DataControl = domain_DataControl
        self.domain_DataControl448 = domain_DataControl448
        self.domain_DataControl454 = domain_DataControl454
        self.domain_DataControl441 = domain_DataControl441
        self.DataControl = DataControl
        self.domain_DataControl490 = domain_DataControl490
        self.controls = controls
        self.domain_DataControl498 = domain_DataControl498
        self.domain_DataControl500 = domain_DataControl500
        self.domain_DataControl502 = domain_DataControl502
        self.domain_DataControl504 = domain_DataControl504
        self.domain_DataControl493 = domain_DataControl493
        self.domain_DataControl508 = domain_DataControl508
        self.domain_DataControl510 = domain_DataControl510
        self.domain_DataControl512 = domain_DataControl512
        self.domain_DataControl514 = domain_DataControl514
        self.domain_DataControl516 = domain_DataControl516
        self.domain_DataControl506 = domain_DataControl506
        self.parent520 = parent520 if parent520 is not None else set()
        self.domain_DataControl522 = domain_DataControl522
        self.domain_DataControl525 = domain_DataControl525
        self.domain_DataControl518 = domain_DataControl518
        self.domain_DataControl533 = domain_DataControl533
        self.domain_DataControl536 = domain_DataControl536
        self.DataControl547 = DataControl547
        self.domain_DataControl542 = domain_DataControl542
        self.domain_DataControl545 = domain_DataControl545
        
    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def domain_DataControl512(self):
        return self.__domain_DataControl512

    @domain_DataControl512.setter
    def domain_DataControl512(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_DataControl__domain_DataControl512", None)
        self.__domain_DataControl512 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_InsertTrigger"):
                opp_val = getattr(old_value, "domain_InsertTrigger", None)
                if opp_val == self:
                    setattr(old_value, "domain_InsertTrigger", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_InsertTrigger"):
                opp_val = getattr(value, "domain_InsertTrigger", None)
                setattr(value, "domain_InsertTrigger", self)

    @property
    def domain_DataControl508(self):
        return self.__domain_DataControl508

    @domain_DataControl508.setter
    def domain_DataControl508(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_DataControl__domain_DataControl508", None)
        self.__domain_DataControl508 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_PREUpdateTrigger"):
                opp_val = getattr(old_value, "domain_PREUpdateTrigger", None)
                if opp_val == self:
                    setattr(old_value, "domain_PREUpdateTrigger", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_PREUpdateTrigger"):
                opp_val = getattr(value, "domain_PREUpdateTrigger", None)
                setattr(value, "domain_PREUpdateTrigger", self)

    @property
    def controls(self):
        return self.__controls

    @controls.setter
    def controls(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_DataControl__controls", None)
        self.__controls = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Controls496"):
                opp_val = getattr(old_value, "Controls496", None)
                if opp_val == self:
                    setattr(old_value, "Controls496", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Controls496"):
                opp_val = getattr(value, "Controls496", None)
                setattr(value, "Controls496", self)

    @property
    def domain_DataControl514(self):
        return self.__domain_DataControl514

    @domain_DataControl514.setter
    def domain_DataControl514(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_DataControl__domain_DataControl514", None)
        self.__domain_DataControl514 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_UpdateTrigger"):
                opp_val = getattr(old_value, "domain_UpdateTrigger", None)
                if opp_val == self:
                    setattr(old_value, "domain_UpdateTrigger", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_UpdateTrigger"):
                opp_val = getattr(value, "domain_UpdateTrigger", None)
                setattr(value, "domain_UpdateTrigger", self)

    @property
    def domain_DataControl502(self):
        return self.__domain_DataControl502

    @domain_DataControl502.setter
    def domain_DataControl502(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_DataControl__domain_DataControl502", None)
        self.__domain_DataControl502 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_PREInsertTrigger"):
                opp_val = getattr(old_value, "domain_PREInsertTrigger", None)
                if opp_val == self:
                    setattr(old_value, "domain_PREInsertTrigger", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_PREInsertTrigger"):
                opp_val = getattr(value, "domain_PREInsertTrigger", None)
                setattr(value, "domain_PREInsertTrigger", self)

    @property
    def domain_DataControl536(self):
        return self.__domain_DataControl536

    @domain_DataControl536.setter
    def domain_DataControl536(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_DataControl__domain_DataControl536", None)
        self.__domain_DataControl536 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_Relation535"):
                opp_val = getattr(old_value, "domain_Relation535", None)
                if opp_val == self:
                    setattr(old_value, "domain_Relation535", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_Relation535"):
                opp_val = getattr(value, "domain_Relation535", None)
                setattr(value, "domain_Relation535", self)

    @property
    def domain_DataControl500(self):
        return self.__domain_DataControl500

    @domain_DataControl500.setter
    def domain_DataControl500(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_DataControl__domain_DataControl500", None)
        self.__domain_DataControl500 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_POSTQueryTrigger"):
                opp_val = getattr(old_value, "domain_POSTQueryTrigger", None)
                if opp_val == self:
                    setattr(old_value, "domain_POSTQueryTrigger", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_POSTQueryTrigger"):
                opp_val = getattr(value, "domain_POSTQueryTrigger", None)
                setattr(value, "domain_POSTQueryTrigger", self)

    @property
    def domain_DataControl533(self):
        return self.__domain_DataControl533

    @domain_DataControl533.setter
    def domain_DataControl533(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_DataControl__domain_DataControl533", None)
        self.__domain_DataControl533 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_Relation532"):
                opp_val = getattr(old_value, "domain_Relation532", None)
                if opp_val == self:
                    setattr(old_value, "domain_Relation532", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_Relation532"):
                opp_val = getattr(value, "domain_Relation532", None)
                setattr(value, "domain_Relation532", self)

    @property
    def domain_DataControl454(self):
        return self.__domain_DataControl454

    @domain_DataControl454.setter
    def domain_DataControl454(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_DataControl__domain_DataControl454", None)
        self.__domain_DataControl454 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_OptionSelection453"):
                opp_val = getattr(old_value, "domain_OptionSelection453", None)
                if opp_val == self:
                    setattr(old_value, "domain_OptionSelection453", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_OptionSelection453"):
                opp_val = getattr(value, "domain_OptionSelection453", None)
                setattr(value, "domain_OptionSelection453", self)

    @property
    def DataControl547(self):
        return self.__DataControl547

    @DataControl547.setter
    def DataControl547(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_DataControl__DataControl547", None)
        self.__DataControl547 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "artificialFields"):
                opp_val = getattr(old_value, "artificialFields", None)
                if opp_val == self:
                    setattr(old_value, "artificialFields", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "artificialFields"):
                opp_val = getattr(value, "artificialFields", None)
                setattr(value, "artificialFields", self)

    @property
    def domain_DataControl516(self):
        return self.__domain_DataControl516

    @domain_DataControl516.setter
    def domain_DataControl516(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_DataControl__domain_DataControl516", None)
        self.__domain_DataControl516 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_DeleteTrigger"):
                opp_val = getattr(old_value, "domain_DeleteTrigger", None)
                if opp_val == self:
                    setattr(old_value, "domain_DeleteTrigger", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_DeleteTrigger"):
                opp_val = getattr(value, "domain_DeleteTrigger", None)
                setattr(value, "domain_DeleteTrigger", self)

    @property
    def parent520(self):
        return self.__parent520

    @parent520.setter
    def parent520(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_DataControl__parent520", None)
        self.__parent520 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ArtificialField"):
                    opp_val = getattr(item, "ArtificialField", None)
                    
                    if opp_val == self:
                        setattr(item, "ArtificialField", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ArtificialField"):
                    opp_val = getattr(item, "ArtificialField", None)
                    
                    setattr(item, "ArtificialField", self)
                    

    @property
    def domain_DataControl448(self):
        return self.__domain_DataControl448

    @domain_DataControl448.setter
    def domain_DataControl448(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_DataControl__domain_DataControl448", None)
        self.__domain_DataControl448 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_OptionSelection"):
                opp_val = getattr(old_value, "domain_OptionSelection", None)
                if opp_val == self:
                    setattr(old_value, "domain_OptionSelection", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_OptionSelection"):
                opp_val = getattr(value, "domain_OptionSelection", None)
                setattr(value, "domain_OptionSelection", self)

    @property
    def domain_DataControl522(self):
        return self.__domain_DataControl522

    @domain_DataControl522.setter
    def domain_DataControl522(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_DataControl__domain_DataControl522", None)
        self.__domain_DataControl522 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_ContextParameters523"):
                opp_val = getattr(old_value, "domain_ContextParameters523", None)
                if opp_val == self:
                    setattr(old_value, "domain_ContextParameters523", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_ContextParameters523"):
                opp_val = getattr(value, "domain_ContextParameters523", None)
                setattr(value, "domain_ContextParameters523", self)

    @property
    def domain_DataControl490(self):
        return self.__domain_DataControl490

    @domain_DataControl490.setter
    def domain_DataControl490(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_DataControl__domain_DataControl490", None)
        self.__domain_DataControl490 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_TypePointer491"):
                opp_val = getattr(old_value, "domain_TypePointer491", None)
                if opp_val == self:
                    setattr(old_value, "domain_TypePointer491", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_TypePointer491"):
                opp_val = getattr(value, "domain_TypePointer491", None)
                setattr(value, "domain_TypePointer491", self)

    @property
    def domain_DataControl493(self):
        return self.__domain_DataControl493

    @domain_DataControl493.setter
    def domain_DataControl493(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_DataControl__domain_DataControl493", None)
        self.__domain_DataControl493 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_TypePointer494"):
                opp_val = getattr(old_value, "domain_TypePointer494", None)
                if opp_val == self:
                    setattr(old_value, "domain_TypePointer494", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_TypePointer494"):
                opp_val = getattr(value, "domain_TypePointer494", None)
                setattr(value, "domain_TypePointer494", self)

    @property
    def domain_DataControl441(self):
        return self.__domain_DataControl441

    @domain_DataControl441.setter
    def domain_DataControl441(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_DataControl__domain_DataControl441", None)
        self.__domain_DataControl441 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_SourcesPointer440"):
                opp_val = getattr(old_value, "domain_SourcesPointer440", None)
                if opp_val == self:
                    setattr(old_value, "domain_SourcesPointer440", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_SourcesPointer440"):
                opp_val = getattr(value, "domain_SourcesPointer440", None)
                setattr(value, "domain_SourcesPointer440", self)

    @property
    def domain_DataControl510(self):
        return self.__domain_DataControl510

    @domain_DataControl510.setter
    def domain_DataControl510(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_DataControl__domain_DataControl510", None)
        self.__domain_DataControl510 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_CreateTrigger"):
                opp_val = getattr(old_value, "domain_CreateTrigger", None)
                if opp_val == self:
                    setattr(old_value, "domain_CreateTrigger", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_CreateTrigger"):
                opp_val = getattr(value, "domain_CreateTrigger", None)
                setattr(value, "domain_CreateTrigger", self)

    @property
    def DataControl(self):
        return self.__DataControl

    @DataControl.setter
    def DataControl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_DataControl__DataControl", None)
        self.__DataControl = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent472"):
                opp_val = getattr(old_value, "parent472", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent472"):
                opp_val = getattr(value, "parent472", None)
                if opp_val is None:
                    setattr(value, "parent472", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def domain_DataControl506(self):
        return self.__domain_DataControl506

    @domain_DataControl506.setter
    def domain_DataControl506(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_DataControl__domain_DataControl506", None)
        self.__domain_DataControl506 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_POSTCreateTrigger"):
                opp_val = getattr(old_value, "domain_POSTCreateTrigger", None)
                if opp_val == self:
                    setattr(old_value, "domain_POSTCreateTrigger", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_POSTCreateTrigger"):
                opp_val = getattr(value, "domain_POSTCreateTrigger", None)
                setattr(value, "domain_POSTCreateTrigger", self)

    @property
    def domain_DataControl525(self):
        return self.__domain_DataControl525

    @domain_DataControl525.setter
    def domain_DataControl525(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_DataControl__domain_DataControl525", None)
        self.__domain_DataControl525 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_Orders"):
                opp_val = getattr(old_value, "domain_Orders", None)
                if opp_val == self:
                    setattr(old_value, "domain_Orders", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_Orders"):
                opp_val = getattr(value, "domain_Orders", None)
                setattr(value, "domain_Orders", self)

    @property
    def domain_DataControl(self):
        return self.__domain_DataControl

    @domain_DataControl.setter
    def domain_DataControl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_DataControl__domain_DataControl", None)
        self.__domain_DataControl = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_SourcesPointer"):
                opp_val = getattr(old_value, "domain_SourcesPointer", None)
                if opp_val == self:
                    setattr(old_value, "domain_SourcesPointer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_SourcesPointer"):
                opp_val = getattr(value, "domain_SourcesPointer", None)
                setattr(value, "domain_SourcesPointer", self)

    @property
    def domain_DataControl518(self):
        return self.__domain_DataControl518

    @domain_DataControl518.setter
    def domain_DataControl518(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_DataControl__domain_DataControl518", None)
        self.__domain_DataControl518 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_SearchTrigger"):
                opp_val = getattr(old_value, "domain_SearchTrigger", None)
                if opp_val == self:
                    setattr(old_value, "domain_SearchTrigger", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_SearchTrigger"):
                opp_val = getattr(value, "domain_SearchTrigger", None)
                setattr(value, "domain_SearchTrigger", self)

    @property
    def domain_DataControl498(self):
        return self.__domain_DataControl498

    @domain_DataControl498.setter
    def domain_DataControl498(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_DataControl__domain_DataControl498", None)
        self.__domain_DataControl498 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_PREQueryTrigger"):
                opp_val = getattr(old_value, "domain_PREQueryTrigger", None)
                if opp_val == self:
                    setattr(old_value, "domain_PREQueryTrigger", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_PREQueryTrigger"):
                opp_val = getattr(value, "domain_PREQueryTrigger", None)
                setattr(value, "domain_PREQueryTrigger", self)

    @property
    def domain_DataControl545(self):
        return self.__domain_DataControl545

    @domain_DataControl545.setter
    def domain_DataControl545(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_DataControl__domain_DataControl545", None)
        self.__domain_DataControl545 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_Dependency544"):
                opp_val = getattr(old_value, "domain_Dependency544", None)
                if opp_val == self:
                    setattr(old_value, "domain_Dependency544", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_Dependency544"):
                opp_val = getattr(value, "domain_Dependency544", None)
                setattr(value, "domain_Dependency544", self)

    @property
    def domain_DataControl504(self):
        return self.__domain_DataControl504

    @domain_DataControl504.setter
    def domain_DataControl504(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_DataControl__domain_DataControl504", None)
        self.__domain_DataControl504 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_PREDeleteTrigger"):
                opp_val = getattr(old_value, "domain_PREDeleteTrigger", None)
                if opp_val == self:
                    setattr(old_value, "domain_PREDeleteTrigger", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_PREDeleteTrigger"):
                opp_val = getattr(value, "domain_PREDeleteTrigger", None)
                setattr(value, "domain_PREDeleteTrigger", self)

    @property
    def domain_DataControl542(self):
        return self.__domain_DataControl542

    @domain_DataControl542.setter
    def domain_DataControl542(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_DataControl__domain_DataControl542", None)
        self.__domain_DataControl542 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_Dependency541"):
                opp_val = getattr(old_value, "domain_Dependency541", None)
                if opp_val == self:
                    setattr(old_value, "domain_Dependency541", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_Dependency541"):
                opp_val = getattr(value, "domain_Dependency541", None)
                setattr(value, "domain_Dependency541", self)

class Uielement:

    pass
class domain_Menu(Uielement):

    def __init__(self, fakeName: str):
        self.fakeName = fakeName
        
    @property
    def fakeName(self) -> str:
        return self.__fakeName

    @fakeName.setter
    def fakeName(self, fakeName: str):
        self.__fakeName = fakeName

class domain_SourcesPointer(Uielement):

    pass
class domain_Formatable:

    def __init__(self, format: str):
        self.format = format
        
    @property
    def format(self) -> str:
        return self.__format

    @format.setter
    def format(self, format: str):
        self.__format = format

class domain_FlexFields:

    pass
class domain_AreaRef:

    def __init__(self, group: int, domain_AreaRef: "domain_Uielement" = None, domain_AreaRef432: "domain_NickNamed" = None, domain_AreaRef601: "domain_MenuItem" = None):
        self.group = group
        self.domain_AreaRef = domain_AreaRef
        self.domain_AreaRef432 = domain_AreaRef432
        self.domain_AreaRef601 = domain_AreaRef601
        
    @property
    def group(self) -> int:
        return self.__group

    @group.setter
    def group(self, group: int):
        self.__group = group

    @property
    def domain_AreaRef601(self):
        return self.__domain_AreaRef601

    @domain_AreaRef601.setter
    def domain_AreaRef601(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_AreaRef__domain_AreaRef601", None)
        self.__domain_AreaRef601 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_MenuItem600"):
                opp_val = getattr(old_value, "domain_MenuItem600", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_MenuItem600"):
                opp_val = getattr(value, "domain_MenuItem600", None)
                if opp_val is None:
                    setattr(value, "domain_MenuItem600", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def domain_AreaRef432(self):
        return self.__domain_AreaRef432

    @domain_AreaRef432.setter
    def domain_AreaRef432(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_AreaRef__domain_AreaRef432", None)
        self.__domain_AreaRef432 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_NickNamed"):
                opp_val = getattr(old_value, "domain_NickNamed", None)
                if opp_val == self:
                    setattr(old_value, "domain_NickNamed", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_NickNamed"):
                opp_val = getattr(value, "domain_NickNamed", None)
                setattr(value, "domain_NickNamed", self)

    @property
    def domain_AreaRef(self):
        return self.__domain_AreaRef

    @domain_AreaRef.setter
    def domain_AreaRef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_AreaRef__domain_AreaRef", None)
        self.__domain_AreaRef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_Uielement428"):
                opp_val = getattr(old_value, "domain_Uielement428", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_Uielement428"):
                opp_val = getattr(value, "domain_Uielement428", None)
                if opp_val is None:
                    setattr(value, "domain_Uielement428", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class MenuHolder:

    pass
class EnabledUIItem:

    pass
class domain_EnabledUIItem:

    pass
class Context:

    pass
class domain_NickNamed:

    def __init__(self, nickname: str, domain_NickNamed: "domain_AreaRef" = None):
        self.nickname = nickname
        self.domain_NickNamed = domain_NickNamed
        
    @property
    def nickname(self) -> str:
        return self.__nickname

    @nickname.setter
    def nickname(self, nickname: str):
        self.__nickname = nickname

    @property
    def domain_NickNamed(self):
        return self.__domain_NickNamed

    @domain_NickNamed.setter
    def domain_NickNamed(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_NickNamed__domain_NickNamed", None)
        self.__domain_NickNamed = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_AreaRef432"):
                opp_val = getattr(old_value, "domain_AreaRef432", None)
                if opp_val == self:
                    setattr(old_value, "domain_AreaRef432", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_AreaRef432"):
                opp_val = getattr(value, "domain_AreaRef432", None)
                setattr(value, "domain_AreaRef432", self)

class domain_StyleElement:

    pass
class ContextParameters:

    pass
class domain_Trigger(ContextParameters, MethodPointer):

    pass
class ContextValue:

    pass
class domain_StyleClass(ContextValue):

    pass
class domain_ContextParameters:

    pass
class domain_ExpressionPart:

    def __init__(self, order: int, expressionType: str, uid: str, domain_ExpressionPart: "domain_ContextValue" = None, domain_ExpressionPart407: "domain_EObject" = None):
        self.order = order
        self.expressionType = expressionType
        self.uid = uid
        self.domain_ExpressionPart = domain_ExpressionPart
        self.domain_ExpressionPart407 = domain_ExpressionPart407
        
    @property
    def order(self) -> int:
        return self.__order

    @order.setter
    def order(self, order: int):
        self.__order = order

    @property
    def expressionType(self) -> str:
        return self.__expressionType

    @expressionType.setter
    def expressionType(self, expressionType: str):
        self.__expressionType = expressionType

    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def domain_ExpressionPart(self):
        return self.__domain_ExpressionPart

    @domain_ExpressionPart.setter
    def domain_ExpressionPart(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_ExpressionPart__domain_ExpressionPart", None)
        self.__domain_ExpressionPart = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_ContextValue405"):
                opp_val = getattr(old_value, "domain_ContextValue405", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_ContextValue405"):
                opp_val = getattr(value, "domain_ContextValue405", None)
                if opp_val is None:
                    setattr(value, "domain_ContextValue405", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def domain_ExpressionPart407(self):
        return self.__domain_ExpressionPart407

    @domain_ExpressionPart407.setter
    def domain_ExpressionPart407(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_ExpressionPart__domain_ExpressionPart407", None)
        self.__domain_ExpressionPart407 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_EObject408"):
                opp_val = getattr(old_value, "domain_EObject408", None)
                if opp_val == self:
                    setattr(old_value, "domain_EObject408", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_EObject408"):
                opp_val = getattr(value, "domain_EObject408", None)
                setattr(value, "domain_EObject408", self)

class domain_ContextValue:

    def __init__(self, uid: str, constant: bool, value: str, domain_ContextValue: "domain_ContextParameter" = None, domain_ContextValue405: set["domain_ExpressionPart"] = None):
        self.uid = uid
        self.constant = constant
        self.value = value
        self.domain_ContextValue = domain_ContextValue
        self.domain_ContextValue405 = domain_ContextValue405 if domain_ContextValue405 is not None else set()
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def constant(self) -> bool:
        return self.__constant

    @constant.setter
    def constant(self, constant: bool):
        self.__constant = constant

    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def domain_ContextValue(self):
        return self.__domain_ContextValue

    @domain_ContextValue.setter
    def domain_ContextValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_ContextValue__domain_ContextValue", None)
        self.__domain_ContextValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_ContextParameter403"):
                opp_val = getattr(old_value, "domain_ContextParameter403", None)
                if opp_val == self:
                    setattr(old_value, "domain_ContextParameter403", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_ContextParameter403"):
                opp_val = getattr(value, "domain_ContextParameter403", None)
                setattr(value, "domain_ContextParameter403", self)

    @property
    def domain_ContextValue405(self):
        return self.__domain_ContextValue405

    @domain_ContextValue405.setter
    def domain_ContextValue405(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_ContextValue__domain_ContextValue405", None)
        self.__domain_ContextValue405 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "domain_ExpressionPart"):
                    opp_val = getattr(item, "domain_ExpressionPart", None)
                    
                    if opp_val == self:
                        setattr(item, "domain_ExpressionPart", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "domain_ExpressionPart"):
                    opp_val = getattr(item, "domain_ExpressionPart", None)
                    
                    setattr(item, "domain_ExpressionPart", self)
                    

class domain_ContextParameter:

    def __init__(self, uid: str, operation: str, domain_ContextParameter: "domain_EObject" = None, domain_ContextParameter403: "domain_ContextValue" = None, domain_ContextParameter410: "domain_ContextParameters" = None):
        self.uid = uid
        self.operation = operation
        self.domain_ContextParameter = domain_ContextParameter
        self.domain_ContextParameter403 = domain_ContextParameter403
        self.domain_ContextParameter410 = domain_ContextParameter410
        
    @property
    def operation(self) -> str:
        return self.__operation

    @operation.setter
    def operation(self, operation: str):
        self.__operation = operation

    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def domain_ContextParameter410(self):
        return self.__domain_ContextParameter410

    @domain_ContextParameter410.setter
    def domain_ContextParameter410(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_ContextParameter__domain_ContextParameter410", None)
        self.__domain_ContextParameter410 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_ContextParameters"):
                opp_val = getattr(old_value, "domain_ContextParameters", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_ContextParameters"):
                opp_val = getattr(value, "domain_ContextParameters", None)
                if opp_val is None:
                    setattr(value, "domain_ContextParameters", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def domain_ContextParameter403(self):
        return self.__domain_ContextParameter403

    @domain_ContextParameter403.setter
    def domain_ContextParameter403(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_ContextParameter__domain_ContextParameter403", None)
        self.__domain_ContextParameter403 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_ContextValue"):
                opp_val = getattr(old_value, "domain_ContextValue", None)
                if opp_val == self:
                    setattr(old_value, "domain_ContextValue", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_ContextValue"):
                opp_val = getattr(value, "domain_ContextValue", None)
                setattr(value, "domain_ContextValue", self)

    @property
    def domain_ContextParameter(self):
        return self.__domain_ContextParameter

    @domain_ContextParameter.setter
    def domain_ContextParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_ContextParameter__domain_ContextParameter", None)
        self.__domain_ContextParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_EObject401"):
                opp_val = getattr(old_value, "domain_EObject401", None)
                if opp_val == self:
                    setattr(old_value, "domain_EObject401", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_EObject401"):
                opp_val = getattr(value, "domain_EObject401", None)
                setattr(value, "domain_EObject401", self)

class domain_ChildrenHolder:

    pass
class domain_LinkToLabel:

    def __init__(self, uid: str, domain_LinkToLabel: "domain_CanvasView" = None, domain_LinkToLabel398: "domain_Label" = None, domain_LinkToLabel395: "domain_InputElement" = None):
        self.uid = uid
        self.domain_LinkToLabel = domain_LinkToLabel
        self.domain_LinkToLabel398 = domain_LinkToLabel398
        self.domain_LinkToLabel395 = domain_LinkToLabel395
        
    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def domain_LinkToLabel(self):
        return self.__domain_LinkToLabel

    @domain_LinkToLabel.setter
    def domain_LinkToLabel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_LinkToLabel__domain_LinkToLabel", None)
        self.__domain_LinkToLabel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_CanvasView384"):
                opp_val = getattr(old_value, "domain_CanvasView384", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_CanvasView384"):
                opp_val = getattr(value, "domain_CanvasView384", None)
                if opp_val is None:
                    setattr(value, "domain_CanvasView384", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def domain_LinkToLabel398(self):
        return self.__domain_LinkToLabel398

    @domain_LinkToLabel398.setter
    def domain_LinkToLabel398(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_LinkToLabel__domain_LinkToLabel398", None)
        self.__domain_LinkToLabel398 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_Label"):
                opp_val = getattr(old_value, "domain_Label", None)
                if opp_val == self:
                    setattr(old_value, "domain_Label", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_Label"):
                opp_val = getattr(value, "domain_Label", None)
                setattr(value, "domain_Label", self)

    @property
    def domain_LinkToLabel395(self):
        return self.__domain_LinkToLabel395

    @domain_LinkToLabel395.setter
    def domain_LinkToLabel395(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_LinkToLabel__domain_LinkToLabel395", None)
        self.__domain_LinkToLabel395 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_InputElement396"):
                opp_val = getattr(old_value, "domain_InputElement396", None)
                if opp_val == self:
                    setattr(old_value, "domain_InputElement396", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_InputElement396"):
                opp_val = getattr(value, "domain_InputElement396", None)
                setattr(value, "domain_InputElement396", self)

class domain_InputElement(SourcesPointer):

    pass
class domain_LinkToMessage:

    def __init__(self, uid: str, domain_LinkToMessage: "domain_CanvasView" = None, domain_LinkToMessage391: "domain_InputElement" = None, domain_LinkToMessage393: "domain_MessageElement" = None):
        self.uid = uid
        self.domain_LinkToMessage = domain_LinkToMessage
        self.domain_LinkToMessage391 = domain_LinkToMessage391
        self.domain_LinkToMessage393 = domain_LinkToMessage393
        
    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def domain_LinkToMessage393(self):
        return self.__domain_LinkToMessage393

    @domain_LinkToMessage393.setter
    def domain_LinkToMessage393(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_LinkToMessage__domain_LinkToMessage393", None)
        self.__domain_LinkToMessage393 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_MessageElement"):
                opp_val = getattr(old_value, "domain_MessageElement", None)
                if opp_val == self:
                    setattr(old_value, "domain_MessageElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_MessageElement"):
                opp_val = getattr(value, "domain_MessageElement", None)
                setattr(value, "domain_MessageElement", self)

    @property
    def domain_LinkToMessage(self):
        return self.__domain_LinkToMessage

    @domain_LinkToMessage.setter
    def domain_LinkToMessage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_LinkToMessage__domain_LinkToMessage", None)
        self.__domain_LinkToMessage = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_CanvasView386"):
                opp_val = getattr(old_value, "domain_CanvasView386", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_CanvasView386"):
                opp_val = getattr(value, "domain_CanvasView386", None)
                if opp_val is None:
                    setattr(value, "domain_CanvasView386", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def domain_LinkToMessage391(self):
        return self.__domain_LinkToMessage391

    @domain_LinkToMessage391.setter
    def domain_LinkToMessage391(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_LinkToMessage__domain_LinkToMessage391", None)
        self.__domain_LinkToMessage391 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_InputElement"):
                opp_val = getattr(old_value, "domain_InputElement", None)
                if opp_val == self:
                    setattr(old_value, "domain_InputElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_InputElement"):
                opp_val = getattr(value, "domain_InputElement", None)
                setattr(value, "domain_InputElement", self)

class domain_Controls:

    def __init__(self, uid: str, Controls: "domain_FormDataControls" = None, domain_Controls476: set["domain_Dependency"] = None, domain_Controls478: "domain_EObject" = None, formControl: "domain_FormDataControls" = None, domain_Controls: "domain_Root" = None, parent472: set["domain_DataControl"] = None, domain_Controls474: set["domain_Relation"] = None, Controls496: "domain_DataControl" = None):
        self.uid = uid
        self.Controls = Controls
        self.domain_Controls476 = domain_Controls476 if domain_Controls476 is not None else set()
        self.domain_Controls478 = domain_Controls478
        self.formControl = formControl
        self.domain_Controls = domain_Controls
        self.parent472 = parent472 if parent472 is not None else set()
        self.domain_Controls474 = domain_Controls474 if domain_Controls474 is not None else set()
        self.Controls496 = Controls496
        
    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def domain_Controls478(self):
        return self.__domain_Controls478

    @domain_Controls478.setter
    def domain_Controls478(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Controls__domain_Controls478", None)
        self.__domain_Controls478 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_EObject479"):
                opp_val = getattr(old_value, "domain_EObject479", None)
                if opp_val == self:
                    setattr(old_value, "domain_EObject479", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_EObject479"):
                opp_val = getattr(value, "domain_EObject479", None)
                setattr(value, "domain_EObject479", self)

    @property
    def Controls(self):
        return self.__Controls

    @Controls.setter
    def Controls(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Controls__Controls", None)
        self.__Controls = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent380"):
                opp_val = getattr(old_value, "parent380", None)
                if opp_val == self:
                    setattr(old_value, "parent380", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent380"):
                opp_val = getattr(value, "parent380", None)
                setattr(value, "parent380", self)

    @property
    def domain_Controls(self):
        return self.__domain_Controls

    @domain_Controls.setter
    def domain_Controls(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Controls__domain_Controls", None)
        self.__domain_Controls = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_Root"):
                opp_val = getattr(old_value, "domain_Root", None)
                if opp_val == self:
                    setattr(old_value, "domain_Root", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_Root"):
                opp_val = getattr(value, "domain_Root", None)
                setattr(value, "domain_Root", self)

    @property
    def Controls496(self):
        return self.__Controls496

    @Controls496.setter
    def Controls496(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Controls__Controls496", None)
        self.__Controls496 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "controls"):
                opp_val = getattr(old_value, "controls", None)
                if opp_val == self:
                    setattr(old_value, "controls", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "controls"):
                opp_val = getattr(value, "controls", None)
                setattr(value, "controls", self)

    @property
    def domain_Controls476(self):
        return self.__domain_Controls476

    @domain_Controls476.setter
    def domain_Controls476(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Controls__domain_Controls476", None)
        self.__domain_Controls476 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "domain_Dependency"):
                    opp_val = getattr(item, "domain_Dependency", None)
                    
                    if opp_val == self:
                        setattr(item, "domain_Dependency", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "domain_Dependency"):
                    opp_val = getattr(item, "domain_Dependency", None)
                    
                    setattr(item, "domain_Dependency", self)
                    

    @property
    def formControl(self):
        return self.__formControl

    @formControl.setter
    def formControl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Controls__formControl", None)
        self.__formControl = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FormDataControls"):
                opp_val = getattr(old_value, "FormDataControls", None)
                if opp_val == self:
                    setattr(old_value, "FormDataControls", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FormDataControls"):
                opp_val = getattr(value, "FormDataControls", None)
                setattr(value, "FormDataControls", self)

    @property
    def parent472(self):
        return self.__parent472

    @parent472.setter
    def parent472(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Controls__parent472", None)
        self.__parent472 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DataControl"):
                    opp_val = getattr(item, "DataControl", None)
                    
                    if opp_val == self:
                        setattr(item, "DataControl", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DataControl"):
                    opp_val = getattr(item, "DataControl", None)
                    
                    setattr(item, "DataControl", self)
                    

    @property
    def domain_Controls474(self):
        return self.__domain_Controls474

    @domain_Controls474.setter
    def domain_Controls474(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Controls__domain_Controls474", None)
        self.__domain_Controls474 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "domain_Relation"):
                    opp_val = getattr(item, "domain_Relation", None)
                    
                    if opp_val == self:
                        setattr(item, "domain_Relation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "domain_Relation"):
                    opp_val = getattr(item, "domain_Relation", None)
                    
                    setattr(item, "domain_Relation", self)
                    

class Trigger:

    pass
class domain_PREFormTrigger(Trigger):

    def __init__(self, uid: str, domain_PREFormTrigger: "domain_Root" = None):
        self.uid = uid
        self.domain_PREFormTrigger = domain_PREFormTrigger
        
    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def domain_PREFormTrigger(self):
        return self.__domain_PREFormTrigger

    @domain_PREFormTrigger.setter
    def domain_PREFormTrigger(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_PREFormTrigger__domain_PREFormTrigger", None)
        self.__domain_PREFormTrigger = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_Root483"):
                opp_val = getattr(old_value, "domain_Root483", None)
                if opp_val == self:
                    setattr(old_value, "domain_Root483", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_Root483"):
                opp_val = getattr(value, "domain_Root483", None)
                setattr(value, "domain_Root483", self)

class domain_PREDeleteTrigger(Trigger):

    def __init__(self, uid: str, domain_PREDeleteTrigger: "domain_DataControl" = None):
        self.uid = uid
        self.domain_PREDeleteTrigger = domain_PREDeleteTrigger
        
    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def domain_PREDeleteTrigger(self):
        return self.__domain_PREDeleteTrigger

    @domain_PREDeleteTrigger.setter
    def domain_PREDeleteTrigger(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_PREDeleteTrigger__domain_PREDeleteTrigger", None)
        self.__domain_PREDeleteTrigger = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_DataControl504"):
                opp_val = getattr(old_value, "domain_DataControl504", None)
                if opp_val == self:
                    setattr(old_value, "domain_DataControl504", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_DataControl504"):
                opp_val = getattr(value, "domain_DataControl504", None)
                setattr(value, "domain_DataControl504", self)

class domain_DeleteTrigger(Trigger, ProxiesList):

    def __init__(self, uid: str, domain_DeleteTrigger: "domain_DataControl" = None):
        self.uid = uid
        self.domain_DeleteTrigger = domain_DeleteTrigger
        
    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def domain_DeleteTrigger(self):
        return self.__domain_DeleteTrigger

    @domain_DeleteTrigger.setter
    def domain_DeleteTrigger(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_DeleteTrigger__domain_DeleteTrigger", None)
        self.__domain_DeleteTrigger = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_DataControl516"):
                opp_val = getattr(old_value, "domain_DataControl516", None)
                if opp_val == self:
                    setattr(old_value, "domain_DataControl516", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_DataControl516"):
                opp_val = getattr(value, "domain_DataControl516", None)
                setattr(value, "domain_DataControl516", self)

class domain_POSTCreateTrigger(Trigger):

    def __init__(self, uid: str, domain_POSTCreateTrigger: "domain_DataControl" = None):
        self.uid = uid
        self.domain_POSTCreateTrigger = domain_POSTCreateTrigger
        
    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def domain_POSTCreateTrigger(self):
        return self.__domain_POSTCreateTrigger

    @domain_POSTCreateTrigger.setter
    def domain_POSTCreateTrigger(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_POSTCreateTrigger__domain_POSTCreateTrigger", None)
        self.__domain_POSTCreateTrigger = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_DataControl506"):
                opp_val = getattr(old_value, "domain_DataControl506", None)
                if opp_val == self:
                    setattr(old_value, "domain_DataControl506", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_DataControl506"):
                opp_val = getattr(value, "domain_DataControl506", None)
                setattr(value, "domain_DataControl506", self)

class domain_PREUpdateTrigger(Trigger):

    def __init__(self, uid: str, domain_PREUpdateTrigger: "domain_DataControl" = None):
        self.uid = uid
        self.domain_PREUpdateTrigger = domain_PREUpdateTrigger
        
    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def domain_PREUpdateTrigger(self):
        return self.__domain_PREUpdateTrigger

    @domain_PREUpdateTrigger.setter
    def domain_PREUpdateTrigger(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_PREUpdateTrigger__domain_PREUpdateTrigger", None)
        self.__domain_PREUpdateTrigger = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_DataControl508"):
                opp_val = getattr(old_value, "domain_DataControl508", None)
                if opp_val == self:
                    setattr(old_value, "domain_DataControl508", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_DataControl508"):
                opp_val = getattr(value, "domain_DataControl508", None)
                setattr(value, "domain_DataControl508", self)

class domain_POSTQueryTrigger(Trigger):

    def __init__(self, uid: str, domain_POSTQueryTrigger: "domain_DataControl" = None):
        self.uid = uid
        self.domain_POSTQueryTrigger = domain_POSTQueryTrigger
        
    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def domain_POSTQueryTrigger(self):
        return self.__domain_POSTQueryTrigger

    @domain_POSTQueryTrigger.setter
    def domain_POSTQueryTrigger(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_POSTQueryTrigger__domain_POSTQueryTrigger", None)
        self.__domain_POSTQueryTrigger = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_DataControl500"):
                opp_val = getattr(old_value, "domain_DataControl500", None)
                if opp_val == self:
                    setattr(old_value, "domain_DataControl500", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_DataControl500"):
                opp_val = getattr(value, "domain_DataControl500", None)
                setattr(value, "domain_DataControl500", self)

class domain_CreateTrigger(Trigger, ProxiesList):

    def __init__(self, uid: str, domain_CreateTrigger: "domain_DataControl" = None):
        self.uid = uid
        self.domain_CreateTrigger = domain_CreateTrigger
        
    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def domain_CreateTrigger(self):
        return self.__domain_CreateTrigger

    @domain_CreateTrigger.setter
    def domain_CreateTrigger(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_CreateTrigger__domain_CreateTrigger", None)
        self.__domain_CreateTrigger = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_DataControl510"):
                opp_val = getattr(old_value, "domain_DataControl510", None)
                if opp_val == self:
                    setattr(old_value, "domain_DataControl510", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_DataControl510"):
                opp_val = getattr(value, "domain_DataControl510", None)
                setattr(value, "domain_DataControl510", self)

class domain_PREQueryTrigger(Trigger):

    def __init__(self, uid: str, domain_PREQueryTrigger: "domain_DataControl" = None):
        self.uid = uid
        self.domain_PREQueryTrigger = domain_PREQueryTrigger
        
    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def domain_PREQueryTrigger(self):
        return self.__domain_PREQueryTrigger

    @domain_PREQueryTrigger.setter
    def domain_PREQueryTrigger(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_PREQueryTrigger__domain_PREQueryTrigger", None)
        self.__domain_PREQueryTrigger = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_DataControl498"):
                opp_val = getattr(old_value, "domain_DataControl498", None)
                if opp_val == self:
                    setattr(old_value, "domain_DataControl498", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_DataControl498"):
                opp_val = getattr(value, "domain_DataControl498", None)
                setattr(value, "domain_DataControl498", self)

class domain_UpdateTrigger(Trigger, ProxiesList):

    def __init__(self, uid: str, domain_UpdateTrigger: "domain_DataControl" = None):
        self.uid = uid
        self.domain_UpdateTrigger = domain_UpdateTrigger
        
    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def domain_UpdateTrigger(self):
        return self.__domain_UpdateTrigger

    @domain_UpdateTrigger.setter
    def domain_UpdateTrigger(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_UpdateTrigger__domain_UpdateTrigger", None)
        self.__domain_UpdateTrigger = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_DataControl514"):
                opp_val = getattr(old_value, "domain_DataControl514", None)
                if opp_val == self:
                    setattr(old_value, "domain_DataControl514", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_DataControl514"):
                opp_val = getattr(value, "domain_DataControl514", None)
                setattr(value, "domain_DataControl514", self)

class domain_SearchTrigger(Trigger, ProxiesList):

    def __init__(self, uid: str, domain_SearchTrigger: "domain_DataControl" = None):
        self.uid = uid
        self.domain_SearchTrigger = domain_SearchTrigger
        
    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def domain_SearchTrigger(self):
        return self.__domain_SearchTrigger

    @domain_SearchTrigger.setter
    def domain_SearchTrigger(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_SearchTrigger__domain_SearchTrigger", None)
        self.__domain_SearchTrigger = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_DataControl518"):
                opp_val = getattr(old_value, "domain_DataControl518", None)
                if opp_val == self:
                    setattr(old_value, "domain_DataControl518", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_DataControl518"):
                opp_val = getattr(value, "domain_DataControl518", None)
                setattr(value, "domain_DataControl518", self)

class domain_PREInsertTrigger(Trigger):

    def __init__(self, uid: str, domain_PREInsertTrigger: "domain_DataControl" = None):
        self.uid = uid
        self.domain_PREInsertTrigger = domain_PREInsertTrigger
        
    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def domain_PREInsertTrigger(self):
        return self.__domain_PREInsertTrigger

    @domain_PREInsertTrigger.setter
    def domain_PREInsertTrigger(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_PREInsertTrigger__domain_PREInsertTrigger", None)
        self.__domain_PREInsertTrigger = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_DataControl502"):
                opp_val = getattr(old_value, "domain_DataControl502", None)
                if opp_val == self:
                    setattr(old_value, "domain_DataControl502", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_DataControl502"):
                opp_val = getattr(value, "domain_DataControl502", None)
                setattr(value, "domain_DataControl502", self)

class domain_InsertTrigger(Trigger, ProxiesList):

    def __init__(self, uid: str, domain_InsertTrigger: "domain_DataControl" = None):
        self.uid = uid
        self.domain_InsertTrigger = domain_InsertTrigger
        
    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def domain_InsertTrigger(self):
        return self.__domain_InsertTrigger

    @domain_InsertTrigger.setter
    def domain_InsertTrigger(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_InsertTrigger__domain_InsertTrigger", None)
        self.__domain_InsertTrigger = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_DataControl512"):
                opp_val = getattr(old_value, "domain_DataControl512", None)
                if opp_val == self:
                    setattr(old_value, "domain_DataControl512", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_DataControl512"):
                opp_val = getattr(value, "domain_DataControl512", None)
                setattr(value, "domain_DataControl512", self)

class domain_CanvasView:

    def __init__(self, uid: str, CanvasView: "domain_ViewArea" = None, canvasView: "domain_ViewArea" = None, domain_CanvasView: "domain_LayerHolder" = None, domain_CanvasView386: set["domain_LinkToMessage"] = None, domain_CanvasView388: "domain_EObject" = None, domain_CanvasView384: set["domain_LinkToLabel"] = None):
        self.uid = uid
        self.CanvasView = CanvasView
        self.canvasView = canvasView
        self.domain_CanvasView = domain_CanvasView
        self.domain_CanvasView386 = domain_CanvasView386 if domain_CanvasView386 is not None else set()
        self.domain_CanvasView388 = domain_CanvasView388
        self.domain_CanvasView384 = domain_CanvasView384 if domain_CanvasView384 is not None else set()
        
    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def domain_CanvasView386(self):
        return self.__domain_CanvasView386

    @domain_CanvasView386.setter
    def domain_CanvasView386(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_CanvasView__domain_CanvasView386", None)
        self.__domain_CanvasView386 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "domain_LinkToMessage"):
                    opp_val = getattr(item, "domain_LinkToMessage", None)
                    
                    if opp_val == self:
                        setattr(item, "domain_LinkToMessage", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "domain_LinkToMessage"):
                    opp_val = getattr(item, "domain_LinkToMessage", None)
                    
                    setattr(item, "domain_LinkToMessage", self)
                    

    @property
    def canvasView(self):
        return self.__canvasView

    @canvasView.setter
    def canvasView(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_CanvasView__canvasView", None)
        self.__canvasView = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ViewArea"):
                opp_val = getattr(old_value, "ViewArea", None)
                if opp_val == self:
                    setattr(old_value, "ViewArea", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ViewArea"):
                opp_val = getattr(value, "ViewArea", None)
                setattr(value, "ViewArea", self)

    @property
    def domain_CanvasView388(self):
        return self.__domain_CanvasView388

    @domain_CanvasView388.setter
    def domain_CanvasView388(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_CanvasView__domain_CanvasView388", None)
        self.__domain_CanvasView388 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_EObject389"):
                opp_val = getattr(old_value, "domain_EObject389", None)
                if opp_val == self:
                    setattr(old_value, "domain_EObject389", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_EObject389"):
                opp_val = getattr(value, "domain_EObject389", None)
                setattr(value, "domain_EObject389", self)

    @property
    def domain_CanvasView384(self):
        return self.__domain_CanvasView384

    @domain_CanvasView384.setter
    def domain_CanvasView384(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_CanvasView__domain_CanvasView384", None)
        self.__domain_CanvasView384 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "domain_LinkToLabel"):
                    opp_val = getattr(item, "domain_LinkToLabel", None)
                    
                    if opp_val == self:
                        setattr(item, "domain_LinkToLabel", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "domain_LinkToLabel"):
                    opp_val = getattr(item, "domain_LinkToLabel", None)
                    
                    setattr(item, "domain_LinkToLabel", self)
                    

    @property
    def domain_CanvasView(self):
        return self.__domain_CanvasView

    @domain_CanvasView.setter
    def domain_CanvasView(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_CanvasView__domain_CanvasView", None)
        self.__domain_CanvasView = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_LayerHolder"):
                opp_val = getattr(old_value, "domain_LayerHolder", None)
                if opp_val == self:
                    setattr(old_value, "domain_LayerHolder", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_LayerHolder"):
                opp_val = getattr(value, "domain_LayerHolder", None)
                setattr(value, "domain_LayerHolder", self)

    @property
    def CanvasView(self):
        return self.__CanvasView

    @CanvasView.setter
    def CanvasView(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_CanvasView__CanvasView", None)
        self.__CanvasView = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent368"):
                opp_val = getattr(old_value, "parent368", None)
                if opp_val == self:
                    setattr(old_value, "parent368", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent368"):
                opp_val = getattr(value, "parent368", None)
                setattr(value, "parent368", self)

class domain_ViewPortTrigger(Trigger):

    def __init__(self, uid: str, domain_ViewPortTrigger: "domain_ViewPort" = None):
        self.uid = uid
        self.domain_ViewPortTrigger = domain_ViewPortTrigger
        
    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def domain_ViewPortTrigger(self):
        return self.__domain_ViewPortTrigger

    @domain_ViewPortTrigger.setter
    def domain_ViewPortTrigger(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_ViewPortTrigger__domain_ViewPortTrigger", None)
        self.__domain_ViewPortTrigger = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_ViewPort"):
                opp_val = getattr(old_value, "domain_ViewPort", None)
                if opp_val == self:
                    setattr(old_value, "domain_ViewPort", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_ViewPort"):
                opp_val = getattr(value, "domain_ViewPort", None)
                setattr(value, "domain_ViewPort", self)

class ViewElement:

    pass
class Orderable:

    pass
class domain_ViewPort(ViewElement, Orderable):

    def __init__(self, uid: str, name: str, domain_ViewPort: "domain_ViewPortTrigger" = None, domain_ViewPort371: "domain_ViewInheritance" = None):
        self.uid = uid
        self.name = name
        self.domain_ViewPort = domain_ViewPort
        self.domain_ViewPort371 = domain_ViewPort371
        
    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def domain_ViewPort(self):
        return self.__domain_ViewPort

    @domain_ViewPort.setter
    def domain_ViewPort(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_ViewPort__domain_ViewPort", None)
        self.__domain_ViewPort = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_ViewPortTrigger"):
                opp_val = getattr(old_value, "domain_ViewPortTrigger", None)
                if opp_val == self:
                    setattr(old_value, "domain_ViewPortTrigger", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_ViewPortTrigger"):
                opp_val = getattr(value, "domain_ViewPortTrigger", None)
                setattr(value, "domain_ViewPortTrigger", self)

    @property
    def domain_ViewPort371(self):
        return self.__domain_ViewPort371

    @domain_ViewPort371.setter
    def domain_ViewPort371(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_ViewPort__domain_ViewPort371", None)
        self.__domain_ViewPort371 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_ViewInheritance370"):
                opp_val = getattr(old_value, "domain_ViewInheritance370", None)
                if opp_val == self:
                    setattr(old_value, "domain_ViewInheritance370", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_ViewInheritance370"):
                opp_val = getattr(value, "domain_ViewInheritance370", None)
                setattr(value, "domain_ViewInheritance370", self)

class domain_ViewArea(ViewElement, Orderable):

    def __init__(self, uid: str, name: str, parent368: "domain_CanvasView" = None, ViewArea: "domain_CanvasView" = None):
        self.uid = uid
        self.name = name
        self.parent368 = parent368
        self.ViewArea = ViewArea
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def parent368(self):
        return self.__parent368

    @parent368.setter
    def parent368(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_ViewArea__parent368", None)
        self.__parent368 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CanvasView"):
                opp_val = getattr(old_value, "CanvasView", None)
                if opp_val == self:
                    setattr(old_value, "CanvasView", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CanvasView"):
                opp_val = getattr(value, "CanvasView", None)
                setattr(value, "CanvasView", self)

    @property
    def ViewArea(self):
        return self.__ViewArea

    @ViewArea.setter
    def ViewArea(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_ViewArea__ViewArea", None)
        self.__ViewArea = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "canvasView"):
                opp_val = getattr(old_value, "canvasView", None)
                if opp_val == self:
                    setattr(old_value, "canvasView", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "canvasView"):
                opp_val = getattr(value, "canvasView", None)
                setattr(value, "canvasView", self)

class domain_MenuView:

    def __init__(self, uid: str, MenuView: "domain_MenuDefinition" = None, menuView: "domain_MenuDefinition" = None, domain_MenuView: set["domain_MenuFolder"] = None, domain_MenuView589: "domain_EObject" = None):
        self.uid = uid
        self.MenuView = MenuView
        self.menuView = menuView
        self.domain_MenuView = domain_MenuView if domain_MenuView is not None else set()
        self.domain_MenuView589 = domain_MenuView589
        
    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def domain_MenuView589(self):
        return self.__domain_MenuView589

    @domain_MenuView589.setter
    def domain_MenuView589(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_MenuView__domain_MenuView589", None)
        self.__domain_MenuView589 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_EObject590"):
                opp_val = getattr(old_value, "domain_EObject590", None)
                if opp_val == self:
                    setattr(old_value, "domain_EObject590", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_EObject590"):
                opp_val = getattr(value, "domain_EObject590", None)
                setattr(value, "domain_EObject590", self)

    @property
    def menuView(self):
        return self.__menuView

    @menuView.setter
    def menuView(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_MenuView__menuView", None)
        self.__menuView = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MenuDefinition"):
                opp_val = getattr(old_value, "MenuDefinition", None)
                if opp_val == self:
                    setattr(old_value, "MenuDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MenuDefinition"):
                opp_val = getattr(value, "MenuDefinition", None)
                setattr(value, "MenuDefinition", self)

    @property
    def domain_MenuView(self):
        return self.__domain_MenuView

    @domain_MenuView.setter
    def domain_MenuView(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_MenuView__domain_MenuView", None)
        self.__domain_MenuView = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "domain_MenuFolder"):
                    opp_val = getattr(item, "domain_MenuFolder", None)
                    
                    if opp_val == self:
                        setattr(item, "domain_MenuFolder", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "domain_MenuFolder"):
                    opp_val = getattr(item, "domain_MenuFolder", None)
                    
                    setattr(item, "domain_MenuFolder", self)
                    

    @property
    def MenuView(self):
        return self.__MenuView

    @MenuView.setter
    def MenuView(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_MenuView__MenuView", None)
        self.__MenuView = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent365"):
                opp_val = getattr(old_value, "parent365", None)
                if opp_val == self:
                    setattr(old_value, "parent365", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent365"):
                opp_val = getattr(value, "parent365", None)
                setattr(value, "parent365", self)

class StyleElement:

    pass
class domain_Selection(StyleElement):

    pass
class FlexFields:

    pass
class domain_MenuItem(FlexFields, ItemIcon, MenuElement):

    pass
class MultiLangLabel:

    pass
class domain_Button(Uielement, MultiLangLabel, ItemIcon):

    def __init__(self, label: str):
        self.label = label
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

class domain_MessageElement(Uielement, MultiLangLabel):

    def __init__(self, label: str, domain_MessageElement: "domain_LinkToMessage" = None):
        self.label = label
        self.domain_MessageElement = domain_MessageElement
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def domain_MessageElement(self):
        return self.__domain_MessageElement

    @domain_MessageElement.setter
    def domain_MessageElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_MessageElement__domain_MessageElement", None)
        self.__domain_MessageElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_LinkToMessage393"):
                opp_val = getattr(old_value, "domain_LinkToMessage393", None)
                if opp_val == self:
                    setattr(old_value, "domain_LinkToMessage393", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_LinkToMessage393"):
                opp_val = getattr(value, "domain_LinkToMessage393", None)
                setattr(value, "domain_LinkToMessage393", self)

class domain_Label(Uielement, MultiLangLabel):

    def __init__(self, label: str, domain_Label: "domain_LinkToLabel" = None):
        self.label = label
        self.domain_Label = domain_Label
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def domain_Label(self):
        return self.__domain_Label

    @domain_Label.setter
    def domain_Label(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Label__domain_Label", None)
        self.__domain_Label = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_LinkToLabel398"):
                opp_val = getattr(old_value, "domain_LinkToLabel398", None)
                if opp_val == self:
                    setattr(old_value, "domain_LinkToLabel398", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_LinkToLabel398"):
                opp_val = getattr(value, "domain_LinkToLabel398", None)
                setattr(value, "domain_LinkToLabel398", self)

class DefaultCavas:

    pass
class ViewPortHolder:

    pass
class CanvasFrame:

    pass
class NickNamed:

    pass
class domain_DefaultCavas:

    def __init__(self, defaultCanvas: bool):
        self.defaultCanvas = defaultCanvas
        
    @property
    def defaultCanvas(self) -> bool:
        return self.__defaultCanvas

    @defaultCanvas.setter
    def defaultCanvas(self, defaultCanvas: bool):
        self.__defaultCanvas = defaultCanvas

class domain_ViewInheritance:

    def __init__(self, uid: str, domain_ViewInheritance: "domain_Views" = None, domain_ViewInheritance370: "domain_ViewPort" = None, domain_ViewInheritance373: "domain_CanvasFrame" = None):
        self.uid = uid
        self.domain_ViewInheritance = domain_ViewInheritance
        self.domain_ViewInheritance370 = domain_ViewInheritance370
        self.domain_ViewInheritance373 = domain_ViewInheritance373
        
    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def domain_ViewInheritance370(self):
        return self.__domain_ViewInheritance370

    @domain_ViewInheritance370.setter
    def domain_ViewInheritance370(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_ViewInheritance__domain_ViewInheritance370", None)
        self.__domain_ViewInheritance370 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_ViewPort371"):
                opp_val = getattr(old_value, "domain_ViewPort371", None)
                if opp_val == self:
                    setattr(old_value, "domain_ViewPort371", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_ViewPort371"):
                opp_val = getattr(value, "domain_ViewPort371", None)
                setattr(value, "domain_ViewPort371", self)

    @property
    def domain_ViewInheritance(self):
        return self.__domain_ViewInheritance

    @domain_ViewInheritance.setter
    def domain_ViewInheritance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_ViewInheritance__domain_ViewInheritance", None)
        self.__domain_ViewInheritance = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_Views354"):
                opp_val = getattr(old_value, "domain_Views354", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_Views354"):
                opp_val = getattr(value, "domain_Views354", None)
                if opp_val is None:
                    setattr(value, "domain_Views354", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def domain_ViewInheritance373(self):
        return self.__domain_ViewInheritance373

    @domain_ViewInheritance373.setter
    def domain_ViewInheritance373(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_ViewInheritance__domain_ViewInheritance373", None)
        self.__domain_ViewInheritance373 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_CanvasFrame374"):
                opp_val = getattr(old_value, "domain_CanvasFrame374", None)
                if opp_val == self:
                    setattr(old_value, "domain_CanvasFrame374", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_CanvasFrame374"):
                opp_val = getattr(value, "domain_CanvasFrame374", None)
                setattr(value, "domain_CanvasFrame374", self)

class domain_CanvasFrame(StyleElement):

    def __init__(self, uid: str, name: str, domain_CanvasFrame: "domain_Views" = None, domain_CanvasFrame374: "domain_ViewInheritance" = None):
        self.uid = uid
        self.name = name
        self.domain_CanvasFrame = domain_CanvasFrame
        self.domain_CanvasFrame374 = domain_CanvasFrame374
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def domain_CanvasFrame(self):
        return self.__domain_CanvasFrame

    @domain_CanvasFrame.setter
    def domain_CanvasFrame(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_CanvasFrame__domain_CanvasFrame", None)
        self.__domain_CanvasFrame = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_Views"):
                opp_val = getattr(old_value, "domain_Views", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_Views"):
                opp_val = getattr(value, "domain_Views", None)
                if opp_val is None:
                    setattr(value, "domain_Views", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def domain_CanvasFrame374(self):
        return self.__domain_CanvasFrame374

    @domain_CanvasFrame374.setter
    def domain_CanvasFrame374(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_CanvasFrame__domain_CanvasFrame374", None)
        self.__domain_CanvasFrame374 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_ViewInheritance373"):
                opp_val = getattr(old_value, "domain_ViewInheritance373", None)
                if opp_val == self:
                    setattr(old_value, "domain_ViewInheritance373", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_ViewInheritance373"):
                opp_val = getattr(value, "domain_ViewInheritance373", None)
                setattr(value, "domain_ViewInheritance373", self)

class domain_Context(ContextParameters, ContextValue):

    pass
class domain_MultiLangLabel:

    pass
class domain_Orderable:

    def __init__(self, order: int):
        self.order = order
        
    @property
    def order(self) -> int:
        return self.__order

    @order.setter
    def order(self, order: int):
        self.__order = order

class domain_TabPagesInheritance:

    def __init__(self, uid: str, domain_TabPagesInheritance: "domain_Views" = None, domain_TabPagesInheritance376: "domain_TabCanvas" = None, domain_TabPagesInheritance378: "domain_TabPage" = None):
        self.uid = uid
        self.domain_TabPagesInheritance = domain_TabPagesInheritance
        self.domain_TabPagesInheritance376 = domain_TabPagesInheritance376
        self.domain_TabPagesInheritance378 = domain_TabPagesInheritance378
        
    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def domain_TabPagesInheritance378(self):
        return self.__domain_TabPagesInheritance378

    @domain_TabPagesInheritance378.setter
    def domain_TabPagesInheritance378(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_TabPagesInheritance__domain_TabPagesInheritance378", None)
        self.__domain_TabPagesInheritance378 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_TabPage"):
                opp_val = getattr(old_value, "domain_TabPage", None)
                if opp_val == self:
                    setattr(old_value, "domain_TabPage", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_TabPage"):
                opp_val = getattr(value, "domain_TabPage", None)
                setattr(value, "domain_TabPage", self)

    @property
    def domain_TabPagesInheritance376(self):
        return self.__domain_TabPagesInheritance376

    @domain_TabPagesInheritance376.setter
    def domain_TabPagesInheritance376(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_TabPagesInheritance__domain_TabPagesInheritance376", None)
        self.__domain_TabPagesInheritance376 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_TabCanvas"):
                opp_val = getattr(old_value, "domain_TabCanvas", None)
                if opp_val == self:
                    setattr(old_value, "domain_TabCanvas", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_TabCanvas"):
                opp_val = getattr(value, "domain_TabCanvas", None)
                setattr(value, "domain_TabCanvas", self)

    @property
    def domain_TabPagesInheritance(self):
        return self.__domain_TabPagesInheritance

    @domain_TabPagesInheritance.setter
    def domain_TabPagesInheritance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_TabPagesInheritance__domain_TabPagesInheritance", None)
        self.__domain_TabPagesInheritance = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_Views356"):
                opp_val = getattr(old_value, "domain_Views356", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_Views356"):
                opp_val = getattr(value, "domain_Views356", None)
                if opp_val is None:
                    setattr(value, "domain_Views356", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class domain_FormDataControls:

    def __init__(self, uid: str, name: str, domain_FormDataControls: "domain_Form" = None, parent380: "domain_Controls" = None, FormDataControls: "domain_Controls" = None):
        self.uid = uid
        self.name = name
        self.domain_FormDataControls = domain_FormDataControls
        self.parent380 = parent380
        self.FormDataControls = FormDataControls
        
    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def parent380(self):
        return self.__parent380

    @parent380.setter
    def parent380(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_FormDataControls__parent380", None)
        self.__parent380 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Controls"):
                opp_val = getattr(old_value, "Controls", None)
                if opp_val == self:
                    setattr(old_value, "Controls", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Controls"):
                opp_val = getattr(value, "Controls", None)
                setattr(value, "Controls", self)

    @property
    def FormDataControls(self):
        return self.__FormDataControls

    @FormDataControls.setter
    def FormDataControls(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_FormDataControls__FormDataControls", None)
        self.__FormDataControls = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "formControl"):
                opp_val = getattr(old_value, "formControl", None)
                if opp_val == self:
                    setattr(old_value, "formControl", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "formControl"):
                opp_val = getattr(value, "formControl", None)
                setattr(value, "formControl", self)

    @property
    def domain_FormDataControls(self):
        return self.__domain_FormDataControls

    @domain_FormDataControls.setter
    def domain_FormDataControls(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_FormDataControls__domain_FormDataControls", None)
        self.__domain_FormDataControls = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_Form346"):
                opp_val = getattr(old_value, "domain_Form346", None)
                if opp_val == self:
                    setattr(old_value, "domain_Form346", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_Form346"):
                opp_val = getattr(value, "domain_Form346", None)
                setattr(value, "domain_Form346", self)

class domain_Views:

    def __init__(self, uid: str, Views: "domain_FormView" = None, domain_Views356: set["domain_TabPagesInheritance"] = None, domain_Views358: set["domain_MenuDefinition"] = None, domain_Views360: "domain_EObject" = None, view: "domain_FormView" = None, domain_Views: set["domain_CanvasFrame"] = None, domain_Views354: set["domain_ViewInheritance"] = None):
        self.uid = uid
        self.Views = Views
        self.domain_Views356 = domain_Views356 if domain_Views356 is not None else set()
        self.domain_Views358 = domain_Views358 if domain_Views358 is not None else set()
        self.domain_Views360 = domain_Views360
        self.view = view
        self.domain_Views = domain_Views if domain_Views is not None else set()
        self.domain_Views354 = domain_Views354 if domain_Views354 is not None else set()
        
    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def domain_Views(self):
        return self.__domain_Views

    @domain_Views.setter
    def domain_Views(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Views__domain_Views", None)
        self.__domain_Views = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "domain_CanvasFrame"):
                    opp_val = getattr(item, "domain_CanvasFrame", None)
                    
                    if opp_val == self:
                        setattr(item, "domain_CanvasFrame", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "domain_CanvasFrame"):
                    opp_val = getattr(item, "domain_CanvasFrame", None)
                    
                    setattr(item, "domain_CanvasFrame", self)
                    

    @property
    def domain_Views356(self):
        return self.__domain_Views356

    @domain_Views356.setter
    def domain_Views356(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Views__domain_Views356", None)
        self.__domain_Views356 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "domain_TabPagesInheritance"):
                    opp_val = getattr(item, "domain_TabPagesInheritance", None)
                    
                    if opp_val == self:
                        setattr(item, "domain_TabPagesInheritance", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "domain_TabPagesInheritance"):
                    opp_val = getattr(item, "domain_TabPagesInheritance", None)
                    
                    setattr(item, "domain_TabPagesInheritance", self)
                    

    @property
    def domain_Views358(self):
        return self.__domain_Views358

    @domain_Views358.setter
    def domain_Views358(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Views__domain_Views358", None)
        self.__domain_Views358 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "domain_MenuDefinition"):
                    opp_val = getattr(item, "domain_MenuDefinition", None)
                    
                    if opp_val == self:
                        setattr(item, "domain_MenuDefinition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "domain_MenuDefinition"):
                    opp_val = getattr(item, "domain_MenuDefinition", None)
                    
                    setattr(item, "domain_MenuDefinition", self)
                    

    @property
    def domain_Views360(self):
        return self.__domain_Views360

    @domain_Views360.setter
    def domain_Views360(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Views__domain_Views360", None)
        self.__domain_Views360 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_EObject361"):
                opp_val = getattr(old_value, "domain_EObject361", None)
                if opp_val == self:
                    setattr(old_value, "domain_EObject361", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_EObject361"):
                opp_val = getattr(value, "domain_EObject361", None)
                setattr(value, "domain_EObject361", self)

    @property
    def Views(self):
        return self.__Views

    @Views.setter
    def Views(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Views__Views", None)
        self.__Views = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent350"):
                opp_val = getattr(old_value, "parent350", None)
                if opp_val == self:
                    setattr(old_value, "parent350", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent350"):
                opp_val = getattr(value, "parent350", None)
                setattr(value, "parent350", self)

    @property
    def domain_Views354(self):
        return self.__domain_Views354

    @domain_Views354.setter
    def domain_Views354(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Views__domain_Views354", None)
        self.__domain_Views354 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "domain_ViewInheritance"):
                    opp_val = getattr(item, "domain_ViewInheritance", None)
                    
                    if opp_val == self:
                        setattr(item, "domain_ViewInheritance", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "domain_ViewInheritance"):
                    opp_val = getattr(item, "domain_ViewInheritance", None)
                    
                    setattr(item, "domain_ViewInheritance", self)
                    

    @property
    def view(self):
        return self.__view

    @view.setter
    def view(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Views__view", None)
        self.__view = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FormView"):
                opp_val = getattr(old_value, "FormView", None)
                if opp_val == self:
                    setattr(old_value, "FormView", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FormView"):
                opp_val = getattr(value, "FormView", None)
                setattr(value, "FormView", self)

class domain_FormView:

    def __init__(self, uid: str, name: str, domain_FormView: "domain_Form" = None, parent350: "domain_Views" = None, FormView: "domain_Views" = None):
        self.uid = uid
        self.name = name
        self.domain_FormView = domain_FormView
        self.parent350 = parent350
        self.FormView = FormView
        
    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def parent350(self):
        return self.__parent350

    @parent350.setter
    def parent350(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_FormView__parent350", None)
        self.__parent350 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Views"):
                opp_val = getattr(old_value, "Views", None)
                if opp_val == self:
                    setattr(old_value, "Views", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Views"):
                opp_val = getattr(value, "Views", None)
                setattr(value, "Views", self)

    @property
    def domain_FormView(self):
        return self.__domain_FormView

    @domain_FormView.setter
    def domain_FormView(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_FormView__domain_FormView", None)
        self.__domain_FormView = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_Form344"):
                opp_val = getattr(old_value, "domain_Form344", None)
                if opp_val == self:
                    setattr(old_value, "domain_Form344", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_Form344"):
                opp_val = getattr(value, "domain_Form344", None)
                setattr(value, "domain_Form344", self)

    @property
    def FormView(self):
        return self.__FormView

    @FormView.setter
    def FormView(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_FormView__FormView", None)
        self.__FormView = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "view"):
                opp_val = getattr(old_value, "view", None)
                if opp_val == self:
                    setattr(old_value, "view", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "view"):
                opp_val = getattr(value, "view", None)
                setattr(value, "view", self)

class domain_Form:

    def __init__(self, uid: str, name: str, domain_Form: "domain_UIPackage" = None, domain_Form344: "domain_FormView" = None, domain_Form346: "domain_FormDataControls" = None, domain_Form348: set["domain_FormParameter"] = None):
        self.uid = uid
        self.name = name
        self.domain_Form = domain_Form
        self.domain_Form344 = domain_Form344
        self.domain_Form346 = domain_Form346
        self.domain_Form348 = domain_Form348 if domain_Form348 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def domain_Form348(self):
        return self.__domain_Form348

    @domain_Form348.setter
    def domain_Form348(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Form__domain_Form348", None)
        self.__domain_Form348 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "domain_FormParameter"):
                    opp_val = getattr(item, "domain_FormParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "domain_FormParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "domain_FormParameter"):
                    opp_val = getattr(item, "domain_FormParameter", None)
                    
                    setattr(item, "domain_FormParameter", self)
                    

    @property
    def domain_Form(self):
        return self.__domain_Form

    @domain_Form.setter
    def domain_Form(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Form__domain_Form", None)
        self.__domain_Form = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_UIPackage"):
                opp_val = getattr(old_value, "domain_UIPackage", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_UIPackage"):
                opp_val = getattr(value, "domain_UIPackage", None)
                if opp_val is None:
                    setattr(value, "domain_UIPackage", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def domain_Form346(self):
        return self.__domain_Form346

    @domain_Form346.setter
    def domain_Form346(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Form__domain_Form346", None)
        self.__domain_Form346 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_FormDataControls"):
                opp_val = getattr(old_value, "domain_FormDataControls", None)
                if opp_val == self:
                    setattr(old_value, "domain_FormDataControls", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_FormDataControls"):
                opp_val = getattr(value, "domain_FormDataControls", None)
                setattr(value, "domain_FormDataControls", self)

    @property
    def domain_Form344(self):
        return self.__domain_Form344

    @domain_Form344.setter
    def domain_Form344(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Form__domain_Form344", None)
        self.__domain_Form344 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_FormView"):
                opp_val = getattr(old_value, "domain_FormView", None)
                if opp_val == self:
                    setattr(old_value, "domain_FormView", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_FormView"):
                opp_val = getattr(value, "domain_FormView", None)
                setattr(value, "domain_FormView", self)

class domain_EnumAttribute:

    def __init__(self, uid: str, name: str, value: str, EnumAttribute: "domain_Enumarator" = None, values: "domain_Enumarator" = None):
        self.uid = uid
        self.name = name
        self.value = value
        self.EnumAttribute = EnumAttribute
        self.values = values
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def values(self):
        return self.__values

    @values.setter
    def values(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_EnumAttribute__values", None)
        self.__values = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Enumarator"):
                opp_val = getattr(old_value, "Enumarator", None)
                if opp_val == self:
                    setattr(old_value, "Enumarator", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Enumarator"):
                opp_val = getattr(value, "Enumarator", None)
                setattr(value, "Enumarator", self)

    @property
    def EnumAttribute(self):
        return self.__EnumAttribute

    @EnumAttribute.setter
    def EnumAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_EnumAttribute__EnumAttribute", None)
        self.__EnumAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent319"):
                opp_val = getattr(old_value, "parent319", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent319"):
                opp_val = getattr(value, "parent319", None)
                if opp_val is None:
                    setattr(value, "parent319", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Secured:

    pass
class TypeElement:

    pass
class domain_Enumarator(TypeElement):

    pass
class domain_Primitive(TypeElement):

    pass
class domain_Link:

    def __init__(self, uid: str, domain_Link: "domain_Assosiation" = None, domain_Link539: "domain_Relation" = None, domain_Link549: "domain_Attribute" = None, domain_Link552: "domain_Attribute" = None):
        self.uid = uid
        self.domain_Link = domain_Link
        self.domain_Link539 = domain_Link539
        self.domain_Link549 = domain_Link549
        self.domain_Link552 = domain_Link552
        
    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def domain_Link539(self):
        return self.__domain_Link539

    @domain_Link539.setter
    def domain_Link539(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Link__domain_Link539", None)
        self.__domain_Link539 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_Relation538"):
                opp_val = getattr(old_value, "domain_Relation538", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_Relation538"):
                opp_val = getattr(value, "domain_Relation538", None)
                if opp_val is None:
                    setattr(value, "domain_Relation538", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def domain_Link549(self):
        return self.__domain_Link549

    @domain_Link549.setter
    def domain_Link549(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Link__domain_Link549", None)
        self.__domain_Link549 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_Attribute550"):
                opp_val = getattr(old_value, "domain_Attribute550", None)
                if opp_val == self:
                    setattr(old_value, "domain_Attribute550", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_Attribute550"):
                opp_val = getattr(value, "domain_Attribute550", None)
                setattr(value, "domain_Attribute550", self)

    @property
    def domain_Link(self):
        return self.__domain_Link

    @domain_Link.setter
    def domain_Link(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Link__domain_Link", None)
        self.__domain_Link = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_Assosiation"):
                opp_val = getattr(old_value, "domain_Assosiation", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_Assosiation"):
                opp_val = getattr(value, "domain_Assosiation", None)
                if opp_val is None:
                    setattr(value, "domain_Assosiation", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def domain_Link552(self):
        return self.__domain_Link552

    @domain_Link552.setter
    def domain_Link552(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Link__domain_Link552", None)
        self.__domain_Link552 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_Attribute553"):
                opp_val = getattr(old_value, "domain_Attribute553", None)
                if opp_val == self:
                    setattr(old_value, "domain_Attribute553", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_Attribute553"):
                opp_val = getattr(value, "domain_Attribute553", None)
                setattr(value, "domain_Attribute553", self)

class RelationShip:

    pass
class domain_Assosiation(RelationShip):

    def __init__(self, type: str, domain_Assosiation: set["domain_Link"] = None, domain_Assosiation296: "domain_Attribute" = None, domain_Assosiation298: "domain_Attribute" = None, domain_Assosiation301: "domain_TypePointer" = None):
        self.type = type
        self.domain_Assosiation = domain_Assosiation if domain_Assosiation is not None else set()
        self.domain_Assosiation296 = domain_Assosiation296
        self.domain_Assosiation298 = domain_Assosiation298
        self.domain_Assosiation301 = domain_Assosiation301
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def domain_Assosiation301(self):
        return self.__domain_Assosiation301

    @domain_Assosiation301.setter
    def domain_Assosiation301(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Assosiation__domain_Assosiation301", None)
        self.__domain_Assosiation301 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_TypePointer302"):
                opp_val = getattr(old_value, "domain_TypePointer302", None)
                if opp_val == self:
                    setattr(old_value, "domain_TypePointer302", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_TypePointer302"):
                opp_val = getattr(value, "domain_TypePointer302", None)
                setattr(value, "domain_TypePointer302", self)

    @property
    def domain_Assosiation298(self):
        return self.__domain_Assosiation298

    @domain_Assosiation298.setter
    def domain_Assosiation298(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Assosiation__domain_Assosiation298", None)
        self.__domain_Assosiation298 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_Attribute299"):
                opp_val = getattr(old_value, "domain_Attribute299", None)
                if opp_val == self:
                    setattr(old_value, "domain_Attribute299", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_Attribute299"):
                opp_val = getattr(value, "domain_Attribute299", None)
                setattr(value, "domain_Attribute299", self)

    @property
    def domain_Assosiation(self):
        return self.__domain_Assosiation

    @domain_Assosiation.setter
    def domain_Assosiation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Assosiation__domain_Assosiation", None)
        self.__domain_Assosiation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "domain_Link"):
                    opp_val = getattr(item, "domain_Link", None)
                    
                    if opp_val == self:
                        setattr(item, "domain_Link", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "domain_Link"):
                    opp_val = getattr(item, "domain_Link", None)
                    
                    setattr(item, "domain_Link", self)
                    

    @property
    def domain_Assosiation296(self):
        return self.__domain_Assosiation296

    @domain_Assosiation296.setter
    def domain_Assosiation296(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Assosiation__domain_Assosiation296", None)
        self.__domain_Assosiation296 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_Attribute"):
                opp_val = getattr(old_value, "domain_Attribute", None)
                if opp_val == self:
                    setattr(old_value, "domain_Attribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_Attribute"):
                opp_val = getattr(value, "domain_Attribute", None)
                setattr(value, "domain_Attribute", self)

class domain_Generalization(RelationShip):

    pass
class domain_References(RelationShip):

    pass
class domain_ArtifactRef:

    def __init__(self, uid: str, domain_ArtifactRef: "domain_DomainArtifact" = None, domain_ArtifactRef276: "domain_Artifact" = None):
        self.uid = uid
        self.domain_ArtifactRef = domain_ArtifactRef
        self.domain_ArtifactRef276 = domain_ArtifactRef276
        
    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def domain_ArtifactRef276(self):
        return self.__domain_ArtifactRef276

    @domain_ArtifactRef276.setter
    def domain_ArtifactRef276(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_ArtifactRef__domain_ArtifactRef276", None)
        self.__domain_ArtifactRef276 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_Artifact277"):
                opp_val = getattr(old_value, "domain_Artifact277", None)
                if opp_val == self:
                    setattr(old_value, "domain_Artifact277", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_Artifact277"):
                opp_val = getattr(value, "domain_Artifact277", None)
                setattr(value, "domain_Artifact277", self)

    @property
    def domain_ArtifactRef(self):
        return self.__domain_ArtifactRef

    @domain_ArtifactRef.setter
    def domain_ArtifactRef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_ArtifactRef__domain_ArtifactRef", None)
        self.__domain_ArtifactRef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_DomainArtifact"):
                opp_val = getattr(old_value, "domain_DomainArtifact", None)
                if opp_val == self:
                    setattr(old_value, "domain_DomainArtifact", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_DomainArtifact"):
                opp_val = getattr(value, "domain_DomainArtifact", None)
                setattr(value, "domain_DomainArtifact", self)

class domain_TypeDefinition:

    def __init__(self, uid: str, parent282: set["domain_TypeElement"] = None, typedefinition: "domain_Package" = None, domain_TypeDefinition286: "domain_EObject" = None, domain_TypeDefinition: set["domain_RelationShip"] = None, TypeDefinition: "domain_TypeElement" = None, TypeDefinition334: "domain_Package" = None):
        self.uid = uid
        self.parent282 = parent282 if parent282 is not None else set()
        self.typedefinition = typedefinition
        self.domain_TypeDefinition286 = domain_TypeDefinition286
        self.domain_TypeDefinition = domain_TypeDefinition if domain_TypeDefinition is not None else set()
        self.TypeDefinition = TypeDefinition
        self.TypeDefinition334 = TypeDefinition334
        
    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def parent282(self):
        return self.__parent282

    @parent282.setter
    def parent282(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_TypeDefinition__parent282", None)
        self.__parent282 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TypeElement"):
                    opp_val = getattr(item, "TypeElement", None)
                    
                    if opp_val == self:
                        setattr(item, "TypeElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TypeElement"):
                    opp_val = getattr(item, "TypeElement", None)
                    
                    setattr(item, "TypeElement", self)
                    

    @property
    def domain_TypeDefinition(self):
        return self.__domain_TypeDefinition

    @domain_TypeDefinition.setter
    def domain_TypeDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_TypeDefinition__domain_TypeDefinition", None)
        self.__domain_TypeDefinition = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "domain_RelationShip"):
                    opp_val = getattr(item, "domain_RelationShip", None)
                    
                    if opp_val == self:
                        setattr(item, "domain_RelationShip", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "domain_RelationShip"):
                    opp_val = getattr(item, "domain_RelationShip", None)
                    
                    setattr(item, "domain_RelationShip", self)
                    

    @property
    def typedefinition(self):
        return self.__typedefinition

    @typedefinition.setter
    def typedefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_TypeDefinition__typedefinition", None)
        self.__typedefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Package"):
                opp_val = getattr(old_value, "Package", None)
                if opp_val == self:
                    setattr(old_value, "Package", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Package"):
                opp_val = getattr(value, "Package", None)
                setattr(value, "Package", self)

    @property
    def TypeDefinition334(self):
        return self.__TypeDefinition334

    @TypeDefinition334.setter
    def TypeDefinition334(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_TypeDefinition__TypeDefinition334", None)
        self.__TypeDefinition334 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent333"):
                opp_val = getattr(old_value, "parent333", None)
                if opp_val == self:
                    setattr(old_value, "parent333", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent333"):
                opp_val = getattr(value, "parent333", None)
                setattr(value, "parent333", self)

    @property
    def TypeDefinition(self):
        return self.__TypeDefinition

    @TypeDefinition.setter
    def TypeDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_TypeDefinition__TypeDefinition", None)
        self.__TypeDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types"):
                opp_val = getattr(old_value, "types", None)
                if opp_val == self:
                    setattr(old_value, "types", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types"):
                opp_val = getattr(value, "types", None)
                setattr(value, "types", self)

    @property
    def domain_TypeDefinition286(self):
        return self.__domain_TypeDefinition286

    @domain_TypeDefinition286.setter
    def domain_TypeDefinition286(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_TypeDefinition__domain_TypeDefinition286", None)
        self.__domain_TypeDefinition286 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_EObject287"):
                opp_val = getattr(old_value, "domain_EObject287", None)
                if opp_val == self:
                    setattr(old_value, "domain_EObject287", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_EObject287"):
                opp_val = getattr(value, "domain_EObject287", None)
                setattr(value, "domain_EObject287", self)

class domain_TypeElement:

    def __init__(self, uid: str, name: str, domain_TypeElement: "domain_TypePointer" = None, TypeElement: "domain_TypeDefinition" = None, domain_TypeElement290: "domain_RelationShip" = None, domain_TypeElement293: "domain_RelationShip" = None, types: "domain_TypeDefinition" = None):
        self.uid = uid
        self.name = name
        self.domain_TypeElement = domain_TypeElement
        self.TypeElement = TypeElement
        self.domain_TypeElement290 = domain_TypeElement290
        self.domain_TypeElement293 = domain_TypeElement293
        self.types = types
        
    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def TypeElement(self):
        return self.__TypeElement

    @TypeElement.setter
    def TypeElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_TypeElement__TypeElement", None)
        self.__TypeElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent282"):
                opp_val = getattr(old_value, "parent282", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent282"):
                opp_val = getattr(value, "parent282", None)
                if opp_val is None:
                    setattr(value, "parent282", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def types(self):
        return self.__types

    @types.setter
    def types(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_TypeElement__types", None)
        self.__types = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TypeDefinition"):
                opp_val = getattr(old_value, "TypeDefinition", None)
                if opp_val == self:
                    setattr(old_value, "TypeDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TypeDefinition"):
                opp_val = getattr(value, "TypeDefinition", None)
                setattr(value, "TypeDefinition", self)

    @property
    def domain_TypeElement290(self):
        return self.__domain_TypeElement290

    @domain_TypeElement290.setter
    def domain_TypeElement290(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_TypeElement__domain_TypeElement290", None)
        self.__domain_TypeElement290 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_RelationShip289"):
                opp_val = getattr(old_value, "domain_RelationShip289", None)
                if opp_val == self:
                    setattr(old_value, "domain_RelationShip289", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_RelationShip289"):
                opp_val = getattr(value, "domain_RelationShip289", None)
                setattr(value, "domain_RelationShip289", self)

    @property
    def domain_TypeElement293(self):
        return self.__domain_TypeElement293

    @domain_TypeElement293.setter
    def domain_TypeElement293(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_TypeElement__domain_TypeElement293", None)
        self.__domain_TypeElement293 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_RelationShip292"):
                opp_val = getattr(old_value, "domain_RelationShip292", None)
                if opp_val == self:
                    setattr(old_value, "domain_RelationShip292", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_RelationShip292"):
                opp_val = getattr(value, "domain_RelationShip292", None)
                setattr(value, "domain_RelationShip292", self)

    @property
    def domain_TypeElement(self):
        return self.__domain_TypeElement

    @domain_TypeElement.setter
    def domain_TypeElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_TypeElement__domain_TypeElement", None)
        self.__domain_TypeElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_TypePointer280"):
                opp_val = getattr(old_value, "domain_TypePointer280", None)
                if opp_val == self:
                    setattr(old_value, "domain_TypePointer280", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_TypePointer280"):
                opp_val = getattr(value, "domain_TypePointer280", None)
                setattr(value, "domain_TypePointer280", self)

class domain_Package:

    def __init__(self, uid: str, name: str, domain_Package: "domain_TypePointer" = None, Package: "domain_TypeDefinition" = None, Package331: "domain_Types" = None, parent333: "domain_TypeDefinition" = None, packages: "domain_Types" = None):
        self.uid = uid
        self.name = name
        self.domain_Package = domain_Package
        self.Package = Package
        self.Package331 = Package331
        self.parent333 = parent333
        self.packages = packages
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def parent333(self):
        return self.__parent333

    @parent333.setter
    def parent333(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Package__parent333", None)
        self.__parent333 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TypeDefinition334"):
                opp_val = getattr(old_value, "TypeDefinition334", None)
                if opp_val == self:
                    setattr(old_value, "TypeDefinition334", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TypeDefinition334"):
                opp_val = getattr(value, "TypeDefinition334", None)
                setattr(value, "TypeDefinition334", self)

    @property
    def Package331(self):
        return self.__Package331

    @Package331.setter
    def Package331(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Package__Package331", None)
        self.__Package331 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent330"):
                opp_val = getattr(old_value, "parent330", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent330"):
                opp_val = getattr(value, "parent330", None)
                if opp_val is None:
                    setattr(value, "parent330", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def domain_Package(self):
        return self.__domain_Package

    @domain_Package.setter
    def domain_Package(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Package__domain_Package", None)
        self.__domain_Package = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_TypePointer"):
                opp_val = getattr(old_value, "domain_TypePointer", None)
                if opp_val == self:
                    setattr(old_value, "domain_TypePointer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_TypePointer"):
                opp_val = getattr(value, "domain_TypePointer", None)
                setattr(value, "domain_TypePointer", self)

    @property
    def Package(self):
        return self.__Package

    @Package.setter
    def Package(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Package__Package", None)
        self.__Package = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "typedefinition"):
                opp_val = getattr(old_value, "typedefinition", None)
                if opp_val == self:
                    setattr(old_value, "typedefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "typedefinition"):
                opp_val = getattr(value, "typedefinition", None)
                setattr(value, "typedefinition", self)

    @property
    def packages(self):
        return self.__packages

    @packages.setter
    def packages(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Package__packages", None)
        self.__packages = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Types336"):
                opp_val = getattr(old_value, "Types336", None)
                if opp_val == self:
                    setattr(old_value, "Types336", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Types336"):
                opp_val = getattr(value, "Types336", None)
                setattr(value, "Types336", self)

class domain_TypePointer:

    def __init__(self, fakePackageName: str, fakeTypeName: str, domain_TypePointer: "domain_Package" = None, domain_TypePointer280: "domain_TypeElement" = None, domain_TypePointer302: "domain_Assosiation" = None, domain_TypePointer481: "domain_ProxiesList" = None, domain_TypePointer491: "domain_DataControl" = None, domain_TypePointer494: "domain_DataControl" = None):
        self.fakePackageName = fakePackageName
        self.fakeTypeName = fakeTypeName
        self.domain_TypePointer = domain_TypePointer
        self.domain_TypePointer280 = domain_TypePointer280
        self.domain_TypePointer302 = domain_TypePointer302
        self.domain_TypePointer481 = domain_TypePointer481
        self.domain_TypePointer491 = domain_TypePointer491
        self.domain_TypePointer494 = domain_TypePointer494
        
    @property
    def fakeTypeName(self) -> str:
        return self.__fakeTypeName

    @fakeTypeName.setter
    def fakeTypeName(self, fakeTypeName: str):
        self.__fakeTypeName = fakeTypeName

    @property
    def fakePackageName(self) -> str:
        return self.__fakePackageName

    @fakePackageName.setter
    def fakePackageName(self, fakePackageName: str):
        self.__fakePackageName = fakePackageName

    @property
    def domain_TypePointer280(self):
        return self.__domain_TypePointer280

    @domain_TypePointer280.setter
    def domain_TypePointer280(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_TypePointer__domain_TypePointer280", None)
        self.__domain_TypePointer280 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_TypeElement"):
                opp_val = getattr(old_value, "domain_TypeElement", None)
                if opp_val == self:
                    setattr(old_value, "domain_TypeElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_TypeElement"):
                opp_val = getattr(value, "domain_TypeElement", None)
                setattr(value, "domain_TypeElement", self)

    @property
    def domain_TypePointer302(self):
        return self.__domain_TypePointer302

    @domain_TypePointer302.setter
    def domain_TypePointer302(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_TypePointer__domain_TypePointer302", None)
        self.__domain_TypePointer302 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_Assosiation301"):
                opp_val = getattr(old_value, "domain_Assosiation301", None)
                if opp_val == self:
                    setattr(old_value, "domain_Assosiation301", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_Assosiation301"):
                opp_val = getattr(value, "domain_Assosiation301", None)
                setattr(value, "domain_Assosiation301", self)

    @property
    def domain_TypePointer(self):
        return self.__domain_TypePointer

    @domain_TypePointer.setter
    def domain_TypePointer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_TypePointer__domain_TypePointer", None)
        self.__domain_TypePointer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_Package"):
                opp_val = getattr(old_value, "domain_Package", None)
                if opp_val == self:
                    setattr(old_value, "domain_Package", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_Package"):
                opp_val = getattr(value, "domain_Package", None)
                setattr(value, "domain_Package", self)

    @property
    def domain_TypePointer491(self):
        return self.__domain_TypePointer491

    @domain_TypePointer491.setter
    def domain_TypePointer491(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_TypePointer__domain_TypePointer491", None)
        self.__domain_TypePointer491 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_DataControl490"):
                opp_val = getattr(old_value, "domain_DataControl490", None)
                if opp_val == self:
                    setattr(old_value, "domain_DataControl490", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_DataControl490"):
                opp_val = getattr(value, "domain_DataControl490", None)
                setattr(value, "domain_DataControl490", self)

    @property
    def domain_TypePointer481(self):
        return self.__domain_TypePointer481

    @domain_TypePointer481.setter
    def domain_TypePointer481(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_TypePointer__domain_TypePointer481", None)
        self.__domain_TypePointer481 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_ProxiesList"):
                opp_val = getattr(old_value, "domain_ProxiesList", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_ProxiesList"):
                opp_val = getattr(value, "domain_ProxiesList", None)
                if opp_val is None:
                    setattr(value, "domain_ProxiesList", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def domain_TypePointer494(self):
        return self.__domain_TypePointer494

    @domain_TypePointer494.setter
    def domain_TypePointer494(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_TypePointer__domain_TypePointer494", None)
        self.__domain_TypePointer494 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_DataControl493"):
                opp_val = getattr(old_value, "domain_DataControl493", None)
                if opp_val == self:
                    setattr(old_value, "domain_DataControl493", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_DataControl493"):
                opp_val = getattr(value, "domain_DataControl493", None)
                setattr(value, "domain_DataControl493", self)

class domain_QueryVariable:

    def __init__(self, uid: str, value: str, domain_QueryVariable: "domain_Query" = None, domain_QueryVariable273: "domain_QueryParameter" = None):
        self.uid = uid
        self.value = value
        self.domain_QueryVariable = domain_QueryVariable
        self.domain_QueryVariable273 = domain_QueryVariable273
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def domain_QueryVariable(self):
        return self.__domain_QueryVariable

    @domain_QueryVariable.setter
    def domain_QueryVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_QueryVariable__domain_QueryVariable", None)
        self.__domain_QueryVariable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_Query271"):
                opp_val = getattr(old_value, "domain_Query271", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_Query271"):
                opp_val = getattr(value, "domain_Query271", None)
                if opp_val is None:
                    setattr(value, "domain_Query271", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def domain_QueryVariable273(self):
        return self.__domain_QueryVariable273

    @domain_QueryVariable273.setter
    def domain_QueryVariable273(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_QueryVariable__domain_QueryVariable273", None)
        self.__domain_QueryVariable273 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_QueryParameter"):
                opp_val = getattr(old_value, "domain_QueryParameter", None)
                if opp_val == self:
                    setattr(old_value, "domain_QueryParameter", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_QueryParameter"):
                opp_val = getattr(value, "domain_QueryParameter", None)
                setattr(value, "domain_QueryParameter", self)

class domain_KeyValuePair:

    def __init__(self, uid: str, key: str, value: str, domain_KeyValuePair: "domain_HashProperty" = None):
        self.uid = uid
        self.key = key
        self.value = value
        self.domain_KeyValuePair = domain_KeyValuePair
        
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

    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def domain_KeyValuePair(self):
        return self.__domain_KeyValuePair

    @domain_KeyValuePair.setter
    def domain_KeyValuePair(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_KeyValuePair__domain_KeyValuePair", None)
        self.__domain_KeyValuePair = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_HashProperty260"):
                opp_val = getattr(old_value, "domain_HashProperty260", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_HashProperty260"):
                opp_val = getattr(value, "domain_HashProperty260", None)
                if opp_val is None:
                    setattr(value, "domain_HashProperty260", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class domain_Query:

    def __init__(self, uid: str, name: str, domain_Query: "domain_ModelMapper" = None, domain_Query266: "domain_ModelQuery" = None, domain_Query268: "domain_ModelQuery" = None, domain_Query271: set["domain_QueryVariable"] = None):
        self.uid = uid
        self.name = name
        self.domain_Query = domain_Query
        self.domain_Query266 = domain_Query266
        self.domain_Query268 = domain_Query268
        self.domain_Query271 = domain_Query271 if domain_Query271 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def domain_Query271(self):
        return self.__domain_Query271

    @domain_Query271.setter
    def domain_Query271(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Query__domain_Query271", None)
        self.__domain_Query271 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "domain_QueryVariable"):
                    opp_val = getattr(item, "domain_QueryVariable", None)
                    
                    if opp_val == self:
                        setattr(item, "domain_QueryVariable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "domain_QueryVariable"):
                    opp_val = getattr(item, "domain_QueryVariable", None)
                    
                    setattr(item, "domain_QueryVariable", self)
                    

    @property
    def domain_Query(self):
        return self.__domain_Query

    @domain_Query.setter
    def domain_Query(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Query__domain_Query", None)
        self.__domain_Query = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_ModelMapper254"):
                opp_val = getattr(old_value, "domain_ModelMapper254", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_ModelMapper254"):
                opp_val = getattr(value, "domain_ModelMapper254", None)
                if opp_val is None:
                    setattr(value, "domain_ModelMapper254", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def domain_Query268(self):
        return self.__domain_Query268

    @domain_Query268.setter
    def domain_Query268(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Query__domain_Query268", None)
        self.__domain_Query268 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_ModelQuery269"):
                opp_val = getattr(old_value, "domain_ModelQuery269", None)
                if opp_val == self:
                    setattr(old_value, "domain_ModelQuery269", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_ModelQuery269"):
                opp_val = getattr(value, "domain_ModelQuery269", None)
                setattr(value, "domain_ModelQuery269", self)

    @property
    def domain_Query266(self):
        return self.__domain_Query266

    @domain_Query266.setter
    def domain_Query266(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Query__domain_Query266", None)
        self.__domain_Query266 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_ModelQuery"):
                opp_val = getattr(old_value, "domain_ModelQuery", None)
                if opp_val == self:
                    setattr(old_value, "domain_ModelQuery", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_ModelQuery"):
                opp_val = getattr(value, "domain_ModelQuery", None)
                setattr(value, "domain_ModelQuery", self)

class domain_MappingSpecifier:

    def __init__(self, uid: str, domain_MappingSpecifier: "domain_ModelMapper" = None, domain_MappingSpecifier262: "domain_Specifier" = None, domain_MappingSpecifier264: "domain_Option" = None):
        self.uid = uid
        self.domain_MappingSpecifier = domain_MappingSpecifier
        self.domain_MappingSpecifier262 = domain_MappingSpecifier262
        self.domain_MappingSpecifier264 = domain_MappingSpecifier264
        
    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def domain_MappingSpecifier(self):
        return self.__domain_MappingSpecifier

    @domain_MappingSpecifier.setter
    def domain_MappingSpecifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_MappingSpecifier__domain_MappingSpecifier", None)
        self.__domain_MappingSpecifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_ModelMapper252"):
                opp_val = getattr(old_value, "domain_ModelMapper252", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_ModelMapper252"):
                opp_val = getattr(value, "domain_ModelMapper252", None)
                if opp_val is None:
                    setattr(value, "domain_ModelMapper252", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def domain_MappingSpecifier264(self):
        return self.__domain_MappingSpecifier264

    @domain_MappingSpecifier264.setter
    def domain_MappingSpecifier264(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_MappingSpecifier__domain_MappingSpecifier264", None)
        self.__domain_MappingSpecifier264 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_Option"):
                opp_val = getattr(old_value, "domain_Option", None)
                if opp_val == self:
                    setattr(old_value, "domain_Option", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_Option"):
                opp_val = getattr(value, "domain_Option", None)
                setattr(value, "domain_Option", self)

    @property
    def domain_MappingSpecifier262(self):
        return self.__domain_MappingSpecifier262

    @domain_MappingSpecifier262.setter
    def domain_MappingSpecifier262(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_MappingSpecifier__domain_MappingSpecifier262", None)
        self.__domain_MappingSpecifier262 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_Specifier"):
                opp_val = getattr(old_value, "domain_Specifier", None)
                if opp_val == self:
                    setattr(old_value, "domain_Specifier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_Specifier"):
                opp_val = getattr(value, "domain_Specifier", None)
                setattr(value, "domain_Specifier", self)

class ArtifactRef:

    pass
class domain_HashProperty:

    def __init__(self, uid: str, fakeName: str, domain_HashProperty: "domain_Configuration" = None, domain_HashProperty258: "domain_ConfigHash" = None, domain_HashProperty260: set["domain_KeyValuePair"] = None):
        self.uid = uid
        self.fakeName = fakeName
        self.domain_HashProperty = domain_HashProperty
        self.domain_HashProperty258 = domain_HashProperty258
        self.domain_HashProperty260 = domain_HashProperty260 if domain_HashProperty260 is not None else set()
        
    @property
    def fakeName(self) -> str:
        return self.__fakeName

    @fakeName.setter
    def fakeName(self, fakeName: str):
        self.__fakeName = fakeName

    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def domain_HashProperty258(self):
        return self.__domain_HashProperty258

    @domain_HashProperty258.setter
    def domain_HashProperty258(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_HashProperty__domain_HashProperty258", None)
        self.__domain_HashProperty258 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_ConfigHash"):
                opp_val = getattr(old_value, "domain_ConfigHash", None)
                if opp_val == self:
                    setattr(old_value, "domain_ConfigHash", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_ConfigHash"):
                opp_val = getattr(value, "domain_ConfigHash", None)
                setattr(value, "domain_ConfigHash", self)

    @property
    def domain_HashProperty(self):
        return self.__domain_HashProperty

    @domain_HashProperty.setter
    def domain_HashProperty(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_HashProperty__domain_HashProperty", None)
        self.__domain_HashProperty = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_Configuration247"):
                opp_val = getattr(old_value, "domain_Configuration247", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_Configuration247"):
                opp_val = getattr(value, "domain_Configuration247", None)
                if opp_val is None:
                    setattr(value, "domain_Configuration247", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def domain_HashProperty260(self):
        return self.__domain_HashProperty260

    @domain_HashProperty260.setter
    def domain_HashProperty260(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_HashProperty__domain_HashProperty260", None)
        self.__domain_HashProperty260 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "domain_KeyValuePair"):
                    opp_val = getattr(item, "domain_KeyValuePair", None)
                    
                    if opp_val == self:
                        setattr(item, "domain_KeyValuePair", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "domain_KeyValuePair"):
                    opp_val = getattr(item, "domain_KeyValuePair", None)
                    
                    setattr(item, "domain_KeyValuePair", self)
                    

class domain_Property:

    def __init__(self, uid: str, value: str, fakeName: str, domain_Property: "domain_Configuration" = None, domain_Property256: "domain_ConfigVariable" = None):
        self.uid = uid
        self.value = value
        self.fakeName = fakeName
        self.domain_Property = domain_Property
        self.domain_Property256 = domain_Property256
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def fakeName(self) -> str:
        return self.__fakeName

    @fakeName.setter
    def fakeName(self, fakeName: str):
        self.__fakeName = fakeName

    @property
    def domain_Property256(self):
        return self.__domain_Property256

    @domain_Property256.setter
    def domain_Property256(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Property__domain_Property256", None)
        self.__domain_Property256 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_ConfigVariable"):
                opp_val = getattr(old_value, "domain_ConfigVariable", None)
                if opp_val == self:
                    setattr(old_value, "domain_ConfigVariable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_ConfigVariable"):
                opp_val = getattr(value, "domain_ConfigVariable", None)
                setattr(value, "domain_ConfigVariable", self)

    @property
    def domain_Property(self):
        return self.__domain_Property

    @domain_Property.setter
    def domain_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Property__domain_Property", None)
        self.__domain_Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_Configuration245"):
                opp_val = getattr(old_value, "domain_Configuration245", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_Configuration245"):
                opp_val = getattr(value, "domain_Configuration245", None)
                if opp_val is None:
                    setattr(value, "domain_Configuration245", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Component:

    pass
class domain_JavaComponent(Component):

    def __init__(self, artifactId: str, groupId: str, version: str, basePackage: str):
        self.artifactId = artifactId
        self.groupId = groupId
        self.version = version
        self.basePackage = basePackage
        
    @property
    def artifactId(self) -> str:
        return self.__artifactId

    @artifactId.setter
    def artifactId(self, artifactId: str):
        self.__artifactId = artifactId

    @property
    def groupId(self) -> str:
        return self.__groupId

    @groupId.setter
    def groupId(self, groupId: str):
        self.__groupId = groupId

    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def basePackage(self) -> str:
        return self.__basePackage

    @basePackage.setter
    def basePackage(self, basePackage: str):
        self.__basePackage = basePackage

class domain_UsingMappers:

    pass
class UsingMappers:

    pass
class domain_DeploymentStarStep:

    def __init__(self, uid: str, name: str, domain_DeploymentStarStep: "domain_DeploymentComponents" = None, domain_DeploymentStarStep214: "domain_DeploymentComponent" = None):
        self.uid = uid
        self.name = name
        self.domain_DeploymentStarStep = domain_DeploymentStarStep
        self.domain_DeploymentStarStep214 = domain_DeploymentStarStep214
        
    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def domain_DeploymentStarStep214(self):
        return self.__domain_DeploymentStarStep214

    @domain_DeploymentStarStep214.setter
    def domain_DeploymentStarStep214(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_DeploymentStarStep__domain_DeploymentStarStep214", None)
        self.__domain_DeploymentStarStep214 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_DeploymentComponent215"):
                opp_val = getattr(old_value, "domain_DeploymentComponent215", None)
                if opp_val == self:
                    setattr(old_value, "domain_DeploymentComponent215", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_DeploymentComponent215"):
                opp_val = getattr(value, "domain_DeploymentComponent215", None)
                setattr(value, "domain_DeploymentComponent215", self)

    @property
    def domain_DeploymentStarStep(self):
        return self.__domain_DeploymentStarStep

    @domain_DeploymentStarStep.setter
    def domain_DeploymentStarStep(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_DeploymentStarStep__domain_DeploymentStarStep", None)
        self.__domain_DeploymentStarStep = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_DeploymentComponents204"):
                opp_val = getattr(old_value, "domain_DeploymentComponents204", None)
                if opp_val == self:
                    setattr(old_value, "domain_DeploymentComponents204", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_DeploymentComponents204"):
                opp_val = getattr(value, "domain_DeploymentComponents204", None)
                setattr(value, "domain_DeploymentComponents204", self)

class domain_DeploymentComponent:

    def __init__(self, uid: str, name: str, domain_DeploymentComponent209: "domain_ModelMapper" = None, domain_DeploymentComponent212: "domain_DeploymentComponent" = None, domain_DeploymentComponent210: "domain_DeploymentComponent" = None, domain_DeploymentComponent: "domain_DeploymentComponents" = None, domain_DeploymentComponent215: "domain_DeploymentStarStep" = None):
        self.uid = uid
        self.name = name
        self.domain_DeploymentComponent209 = domain_DeploymentComponent209
        self.domain_DeploymentComponent212 = domain_DeploymentComponent212
        self.domain_DeploymentComponent210 = domain_DeploymentComponent210
        self.domain_DeploymentComponent = domain_DeploymentComponent
        self.domain_DeploymentComponent215 = domain_DeploymentComponent215
        
    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def domain_DeploymentComponent215(self):
        return self.__domain_DeploymentComponent215

    @domain_DeploymentComponent215.setter
    def domain_DeploymentComponent215(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_DeploymentComponent__domain_DeploymentComponent215", None)
        self.__domain_DeploymentComponent215 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_DeploymentStarStep214"):
                opp_val = getattr(old_value, "domain_DeploymentStarStep214", None)
                if opp_val == self:
                    setattr(old_value, "domain_DeploymentStarStep214", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_DeploymentStarStep214"):
                opp_val = getattr(value, "domain_DeploymentStarStep214", None)
                setattr(value, "domain_DeploymentStarStep214", self)

    @property
    def domain_DeploymentComponent(self):
        return self.__domain_DeploymentComponent

    @domain_DeploymentComponent.setter
    def domain_DeploymentComponent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_DeploymentComponent__domain_DeploymentComponent", None)
        self.__domain_DeploymentComponent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_DeploymentComponents202"):
                opp_val = getattr(old_value, "domain_DeploymentComponents202", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_DeploymentComponents202"):
                opp_val = getattr(value, "domain_DeploymentComponents202", None)
                if opp_val is None:
                    setattr(value, "domain_DeploymentComponents202", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def domain_DeploymentComponent210(self):
        return self.__domain_DeploymentComponent210

    @domain_DeploymentComponent210.setter
    def domain_DeploymentComponent210(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_DeploymentComponent__domain_DeploymentComponent210", None)
        self.__domain_DeploymentComponent210 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_DeploymentComponent212"):
                opp_val = getattr(old_value, "domain_DeploymentComponent212", None)
                if opp_val == self:
                    setattr(old_value, "domain_DeploymentComponent212", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_DeploymentComponent212"):
                opp_val = getattr(value, "domain_DeploymentComponent212", None)
                setattr(value, "domain_DeploymentComponent212", self)

    @property
    def domain_DeploymentComponent212(self):
        return self.__domain_DeploymentComponent212

    @domain_DeploymentComponent212.setter
    def domain_DeploymentComponent212(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_DeploymentComponent__domain_DeploymentComponent212", None)
        self.__domain_DeploymentComponent212 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_DeploymentComponent210"):
                opp_val = getattr(old_value, "domain_DeploymentComponent210", None)
                if opp_val == self:
                    setattr(old_value, "domain_DeploymentComponent210", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_DeploymentComponent210"):
                opp_val = getattr(value, "domain_DeploymentComponent210", None)
                setattr(value, "domain_DeploymentComponent210", self)

    @property
    def domain_DeploymentComponent209(self):
        return self.__domain_DeploymentComponent209

    @domain_DeploymentComponent209.setter
    def domain_DeploymentComponent209(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_DeploymentComponent__domain_DeploymentComponent209", None)
        self.__domain_DeploymentComponent209 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_ModelMapper"):
                opp_val = getattr(old_value, "domain_ModelMapper", None)
                if opp_val == self:
                    setattr(old_value, "domain_ModelMapper", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_ModelMapper"):
                opp_val = getattr(value, "domain_ModelMapper", None)
                setattr(value, "domain_ModelMapper", self)

class domain_ModelMapper(ArtifactRef):

    def __init__(self, name: str, artifactRoot: str, artifactExecutionString: str, domain_ModelMapper: "domain_DeploymentComponent" = None, ModelMapper: "domain_Component" = None, mappers249: "domain_Component" = None, domain_ModelMapper252: set["domain_MappingSpecifier"] = None, domain_ModelMapper254: set["domain_Query"] = None):
        self.name = name
        self.artifactRoot = artifactRoot
        self.artifactExecutionString = artifactExecutionString
        self.domain_ModelMapper = domain_ModelMapper
        self.ModelMapper = ModelMapper
        self.mappers249 = mappers249
        self.domain_ModelMapper252 = domain_ModelMapper252 if domain_ModelMapper252 is not None else set()
        self.domain_ModelMapper254 = domain_ModelMapper254 if domain_ModelMapper254 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def artifactRoot(self) -> str:
        return self.__artifactRoot

    @artifactRoot.setter
    def artifactRoot(self, artifactRoot: str):
        self.__artifactRoot = artifactRoot

    @property
    def artifactExecutionString(self) -> str:
        return self.__artifactExecutionString

    @artifactExecutionString.setter
    def artifactExecutionString(self, artifactExecutionString: str):
        self.__artifactExecutionString = artifactExecutionString

    @property
    def domain_ModelMapper(self):
        return self.__domain_ModelMapper

    @domain_ModelMapper.setter
    def domain_ModelMapper(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_ModelMapper__domain_ModelMapper", None)
        self.__domain_ModelMapper = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_DeploymentComponent209"):
                opp_val = getattr(old_value, "domain_DeploymentComponent209", None)
                if opp_val == self:
                    setattr(old_value, "domain_DeploymentComponent209", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_DeploymentComponent209"):
                opp_val = getattr(value, "domain_DeploymentComponent209", None)
                setattr(value, "domain_DeploymentComponent209", self)

    @property
    def domain_ModelMapper254(self):
        return self.__domain_ModelMapper254

    @domain_ModelMapper254.setter
    def domain_ModelMapper254(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_ModelMapper__domain_ModelMapper254", None)
        self.__domain_ModelMapper254 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "domain_Query"):
                    opp_val = getattr(item, "domain_Query", None)
                    
                    if opp_val == self:
                        setattr(item, "domain_Query", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "domain_Query"):
                    opp_val = getattr(item, "domain_Query", None)
                    
                    setattr(item, "domain_Query", self)
                    

    @property
    def domain_ModelMapper252(self):
        return self.__domain_ModelMapper252

    @domain_ModelMapper252.setter
    def domain_ModelMapper252(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_ModelMapper__domain_ModelMapper252", None)
        self.__domain_ModelMapper252 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "domain_MappingSpecifier"):
                    opp_val = getattr(item, "domain_MappingSpecifier", None)
                    
                    if opp_val == self:
                        setattr(item, "domain_MappingSpecifier", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "domain_MappingSpecifier"):
                    opp_val = getattr(item, "domain_MappingSpecifier", None)
                    
                    setattr(item, "domain_MappingSpecifier", self)
                    

    @property
    def mappers249(self):
        return self.__mappers249

    @mappers249.setter
    def mappers249(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_ModelMapper__mappers249", None)
        self.__mappers249 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Component250"):
                opp_val = getattr(old_value, "Component250", None)
                if opp_val == self:
                    setattr(old_value, "Component250", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Component250"):
                opp_val = getattr(value, "Component250", None)
                setattr(value, "Component250", self)

    @property
    def ModelMapper(self):
        return self.__ModelMapper

    @ModelMapper.setter
    def ModelMapper(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_ModelMapper__ModelMapper", None)
        self.__ModelMapper = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent238"):
                opp_val = getattr(old_value, "parent238", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent238"):
                opp_val = getattr(value, "parent238", None)
                if opp_val is None:
                    setattr(value, "parent238", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class domain_Infrastructure:

    def __init__(self, uid: str, name: str, domain_Infrastructure: "domain_Recipes" = None, Infrastructure: "domain_Recipe" = None, infrastructures: "domain_Recipe" = None, infrastructure: "domain_Configuration" = None, Infrastructure243: "domain_Configuration" = None):
        self.uid = uid
        self.name = name
        self.domain_Infrastructure = domain_Infrastructure
        self.Infrastructure = Infrastructure
        self.infrastructures = infrastructures
        self.infrastructure = infrastructure
        self.Infrastructure243 = Infrastructure243
        
    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def infrastructure(self):
        return self.__infrastructure

    @infrastructure.setter
    def infrastructure(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Infrastructure__infrastructure", None)
        self.__infrastructure = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Configuration"):
                opp_val = getattr(old_value, "Configuration", None)
                if opp_val == self:
                    setattr(old_value, "Configuration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Configuration"):
                opp_val = getattr(value, "Configuration", None)
                setattr(value, "Configuration", self)

    @property
    def Infrastructure(self):
        return self.__Infrastructure

    @Infrastructure.setter
    def Infrastructure(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Infrastructure__Infrastructure", None)
        self.__Infrastructure = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "recipe222"):
                opp_val = getattr(old_value, "recipe222", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "recipe222"):
                opp_val = getattr(value, "recipe222", None)
                if opp_val is None:
                    setattr(value, "recipe222", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def infrastructures(self):
        return self.__infrastructures

    @infrastructures.setter
    def infrastructures(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Infrastructure__infrastructures", None)
        self.__infrastructures = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Recipe240"):
                opp_val = getattr(old_value, "Recipe240", None)
                if opp_val == self:
                    setattr(old_value, "Recipe240", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Recipe240"):
                opp_val = getattr(value, "Recipe240", None)
                setattr(value, "Recipe240", self)

    @property
    def domain_Infrastructure(self):
        return self.__domain_Infrastructure

    @domain_Infrastructure.setter
    def domain_Infrastructure(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Infrastructure__domain_Infrastructure", None)
        self.__domain_Infrastructure = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_Recipes188"):
                opp_val = getattr(old_value, "domain_Recipes188", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_Recipes188"):
                opp_val = getattr(value, "domain_Recipes188", None)
                if opp_val is None:
                    setattr(value, "domain_Recipes188", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Infrastructure243(self):
        return self.__Infrastructure243

    @Infrastructure243.setter
    def Infrastructure243(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Infrastructure__Infrastructure243", None)
        self.__Infrastructure243 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "recipeConfig"):
                opp_val = getattr(old_value, "recipeConfig", None)
                if opp_val == self:
                    setattr(old_value, "recipeConfig", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "recipeConfig"):
                opp_val = getattr(value, "recipeConfig", None)
                setattr(value, "recipeConfig", self)

class domain_DeploymentComponents:

    def __init__(self, uid: str, domain_DeploymentComponents: "domain_DeploymentSequence" = None, domain_DeploymentComponents206: "domain_EObject" = None, domain_DeploymentComponents202: set["domain_DeploymentComponent"] = None, domain_DeploymentComponents204: "domain_DeploymentStarStep" = None):
        self.uid = uid
        self.domain_DeploymentComponents = domain_DeploymentComponents
        self.domain_DeploymentComponents206 = domain_DeploymentComponents206
        self.domain_DeploymentComponents202 = domain_DeploymentComponents202 if domain_DeploymentComponents202 is not None else set()
        self.domain_DeploymentComponents204 = domain_DeploymentComponents204
        
    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def domain_DeploymentComponents202(self):
        return self.__domain_DeploymentComponents202

    @domain_DeploymentComponents202.setter
    def domain_DeploymentComponents202(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_DeploymentComponents__domain_DeploymentComponents202", None)
        self.__domain_DeploymentComponents202 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "domain_DeploymentComponent"):
                    opp_val = getattr(item, "domain_DeploymentComponent", None)
                    
                    if opp_val == self:
                        setattr(item, "domain_DeploymentComponent", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "domain_DeploymentComponent"):
                    opp_val = getattr(item, "domain_DeploymentComponent", None)
                    
                    setattr(item, "domain_DeploymentComponent", self)
                    

    @property
    def domain_DeploymentComponents(self):
        return self.__domain_DeploymentComponents

    @domain_DeploymentComponents.setter
    def domain_DeploymentComponents(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_DeploymentComponents__domain_DeploymentComponents", None)
        self.__domain_DeploymentComponents = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_DeploymentSequence200"):
                opp_val = getattr(old_value, "domain_DeploymentSequence200", None)
                if opp_val == self:
                    setattr(old_value, "domain_DeploymentSequence200", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_DeploymentSequence200"):
                opp_val = getattr(value, "domain_DeploymentSequence200", None)
                setattr(value, "domain_DeploymentSequence200", self)

    @property
    def domain_DeploymentComponents204(self):
        return self.__domain_DeploymentComponents204

    @domain_DeploymentComponents204.setter
    def domain_DeploymentComponents204(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_DeploymentComponents__domain_DeploymentComponents204", None)
        self.__domain_DeploymentComponents204 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_DeploymentStarStep"):
                opp_val = getattr(old_value, "domain_DeploymentStarStep", None)
                if opp_val == self:
                    setattr(old_value, "domain_DeploymentStarStep", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_DeploymentStarStep"):
                opp_val = getattr(value, "domain_DeploymentStarStep", None)
                setattr(value, "domain_DeploymentStarStep", self)

    @property
    def domain_DeploymentComponents206(self):
        return self.__domain_DeploymentComponents206

    @domain_DeploymentComponents206.setter
    def domain_DeploymentComponents206(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_DeploymentComponents__domain_DeploymentComponents206", None)
        self.__domain_DeploymentComponents206 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_EObject207"):
                opp_val = getattr(old_value, "domain_EObject207", None)
                if opp_val == self:
                    setattr(old_value, "domain_EObject207", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_EObject207"):
                opp_val = getattr(value, "domain_EObject207", None)
                setattr(value, "domain_EObject207", self)

class domain_ConfigExtension:

    def __init__(self, uid: str, domain_ConfigExtension: "domain_Recipes" = None, domain_ConfigExtension226: "domain_Configuration" = None, domain_ConfigExtension229: "domain_Configuration" = None):
        self.uid = uid
        self.domain_ConfigExtension = domain_ConfigExtension
        self.domain_ConfigExtension226 = domain_ConfigExtension226
        self.domain_ConfigExtension229 = domain_ConfigExtension229
        
    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def domain_ConfigExtension226(self):
        return self.__domain_ConfigExtension226

    @domain_ConfigExtension226.setter
    def domain_ConfigExtension226(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_ConfigExtension__domain_ConfigExtension226", None)
        self.__domain_ConfigExtension226 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_Configuration227"):
                opp_val = getattr(old_value, "domain_Configuration227", None)
                if opp_val == self:
                    setattr(old_value, "domain_Configuration227", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_Configuration227"):
                opp_val = getattr(value, "domain_Configuration227", None)
                setattr(value, "domain_Configuration227", self)

    @property
    def domain_ConfigExtension229(self):
        return self.__domain_ConfigExtension229

    @domain_ConfigExtension229.setter
    def domain_ConfigExtension229(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_ConfigExtension__domain_ConfigExtension229", None)
        self.__domain_ConfigExtension229 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_Configuration230"):
                opp_val = getattr(old_value, "domain_Configuration230", None)
                if opp_val == self:
                    setattr(old_value, "domain_Configuration230", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_Configuration230"):
                opp_val = getattr(value, "domain_Configuration230", None)
                setattr(value, "domain_Configuration230", self)

    @property
    def domain_ConfigExtension(self):
        return self.__domain_ConfigExtension

    @domain_ConfigExtension.setter
    def domain_ConfigExtension(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_ConfigExtension__domain_ConfigExtension", None)
        self.__domain_ConfigExtension = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_Recipes195"):
                opp_val = getattr(old_value, "domain_Recipes195", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_Recipes195"):
                opp_val = getattr(value, "domain_Recipes195", None)
                if opp_val is None:
                    setattr(value, "domain_Recipes195", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class domain_DeploymentSequence:

    def __init__(self, uid: str, name: str, domain_DeploymentSequence: "domain_Recipes" = None, domain_DeploymentSequence200: "domain_DeploymentComponents" = None, domain_DeploymentSequence224: "domain_Recipe" = None):
        self.uid = uid
        self.name = name
        self.domain_DeploymentSequence = domain_DeploymentSequence
        self.domain_DeploymentSequence200 = domain_DeploymentSequence200
        self.domain_DeploymentSequence224 = domain_DeploymentSequence224
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def domain_DeploymentSequence200(self):
        return self.__domain_DeploymentSequence200

    @domain_DeploymentSequence200.setter
    def domain_DeploymentSequence200(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_DeploymentSequence__domain_DeploymentSequence200", None)
        self.__domain_DeploymentSequence200 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_DeploymentComponents"):
                opp_val = getattr(old_value, "domain_DeploymentComponents", None)
                if opp_val == self:
                    setattr(old_value, "domain_DeploymentComponents", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_DeploymentComponents"):
                opp_val = getattr(value, "domain_DeploymentComponents", None)
                setattr(value, "domain_DeploymentComponents", self)

    @property
    def domain_DeploymentSequence224(self):
        return self.__domain_DeploymentSequence224

    @domain_DeploymentSequence224.setter
    def domain_DeploymentSequence224(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_DeploymentSequence__domain_DeploymentSequence224", None)
        self.__domain_DeploymentSequence224 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_Recipe"):
                opp_val = getattr(old_value, "domain_Recipe", None)
                if opp_val == self:
                    setattr(old_value, "domain_Recipe", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_Recipe"):
                opp_val = getattr(value, "domain_Recipe", None)
                setattr(value, "domain_Recipe", self)

    @property
    def domain_DeploymentSequence(self):
        return self.__domain_DeploymentSequence

    @domain_DeploymentSequence.setter
    def domain_DeploymentSequence(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_DeploymentSequence__domain_DeploymentSequence", None)
        self.__domain_DeploymentSequence = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_Recipes193"):
                opp_val = getattr(old_value, "domain_Recipes193", None)
                if opp_val == self:
                    setattr(old_value, "domain_Recipes193", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_Recipes193"):
                opp_val = getattr(value, "domain_Recipes193", None)
                setattr(value, "domain_Recipes193", self)

class domain_Configuration:

    def __init__(self, uid: str, name: str, domain_Configuration: "domain_Recipes" = None, domain_Configuration227: "domain_ConfigExtension" = None, domain_Configuration230: "domain_ConfigExtension" = None, Configuration: "domain_Infrastructure" = None, domain_Configuration245: set["domain_Property"] = None, domain_Configuration247: set["domain_HashProperty"] = None, recipeConfig: "domain_Infrastructure" = None):
        self.uid = uid
        self.name = name
        self.domain_Configuration = domain_Configuration
        self.domain_Configuration227 = domain_Configuration227
        self.domain_Configuration230 = domain_Configuration230
        self.Configuration = Configuration
        self.domain_Configuration245 = domain_Configuration245 if domain_Configuration245 is not None else set()
        self.domain_Configuration247 = domain_Configuration247 if domain_Configuration247 is not None else set()
        self.recipeConfig = recipeConfig
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def domain_Configuration227(self):
        return self.__domain_Configuration227

    @domain_Configuration227.setter
    def domain_Configuration227(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Configuration__domain_Configuration227", None)
        self.__domain_Configuration227 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_ConfigExtension226"):
                opp_val = getattr(old_value, "domain_ConfigExtension226", None)
                if opp_val == self:
                    setattr(old_value, "domain_ConfigExtension226", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_ConfigExtension226"):
                opp_val = getattr(value, "domain_ConfigExtension226", None)
                setattr(value, "domain_ConfigExtension226", self)

    @property
    def domain_Configuration(self):
        return self.__domain_Configuration

    @domain_Configuration.setter
    def domain_Configuration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Configuration__domain_Configuration", None)
        self.__domain_Configuration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_Recipes"):
                opp_val = getattr(old_value, "domain_Recipes", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_Recipes"):
                opp_val = getattr(value, "domain_Recipes", None)
                if opp_val is None:
                    setattr(value, "domain_Recipes", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def recipeConfig(self):
        return self.__recipeConfig

    @recipeConfig.setter
    def recipeConfig(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Configuration__recipeConfig", None)
        self.__recipeConfig = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Infrastructure243"):
                opp_val = getattr(old_value, "Infrastructure243", None)
                if opp_val == self:
                    setattr(old_value, "Infrastructure243", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Infrastructure243"):
                opp_val = getattr(value, "Infrastructure243", None)
                setattr(value, "Infrastructure243", self)

    @property
    def Configuration(self):
        return self.__Configuration

    @Configuration.setter
    def Configuration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Configuration__Configuration", None)
        self.__Configuration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "infrastructure"):
                opp_val = getattr(old_value, "infrastructure", None)
                if opp_val == self:
                    setattr(old_value, "infrastructure", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "infrastructure"):
                opp_val = getattr(value, "infrastructure", None)
                setattr(value, "infrastructure", self)

    @property
    def domain_Configuration230(self):
        return self.__domain_Configuration230

    @domain_Configuration230.setter
    def domain_Configuration230(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Configuration__domain_Configuration230", None)
        self.__domain_Configuration230 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_ConfigExtension229"):
                opp_val = getattr(old_value, "domain_ConfigExtension229", None)
                if opp_val == self:
                    setattr(old_value, "domain_ConfigExtension229", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_ConfigExtension229"):
                opp_val = getattr(value, "domain_ConfigExtension229", None)
                setattr(value, "domain_ConfigExtension229", self)

    @property
    def domain_Configuration245(self):
        return self.__domain_Configuration245

    @domain_Configuration245.setter
    def domain_Configuration245(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Configuration__domain_Configuration245", None)
        self.__domain_Configuration245 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "domain_Property"):
                    opp_val = getattr(item, "domain_Property", None)
                    
                    if opp_val == self:
                        setattr(item, "domain_Property", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "domain_Property"):
                    opp_val = getattr(item, "domain_Property", None)
                    
                    setattr(item, "domain_Property", self)
                    

    @property
    def domain_Configuration247(self):
        return self.__domain_Configuration247

    @domain_Configuration247.setter
    def domain_Configuration247(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Configuration__domain_Configuration247", None)
        self.__domain_Configuration247 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "domain_HashProperty"):
                    opp_val = getattr(item, "domain_HashProperty", None)
                    
                    if opp_val == self:
                        setattr(item, "domain_HashProperty", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "domain_HashProperty"):
                    opp_val = getattr(item, "domain_HashProperty", None)
                    
                    setattr(item, "domain_HashProperty", self)
                    

class domain_Recipe(UsingMappers):

    def __init__(self, uid: str, name: str, Recipe: "domain_Recipes" = None, recipe222: set["domain_Infrastructure"] = None, domain_Recipe: "domain_DeploymentSequence" = None, recipe: "domain_Recipes" = None, parent220: set["domain_Ingredient"] = None, Recipe232: "domain_Ingredient" = None, Recipe240: "domain_Infrastructure" = None):
        self.uid = uid
        self.name = name
        self.Recipe = Recipe
        self.recipe222 = recipe222 if recipe222 is not None else set()
        self.domain_Recipe = domain_Recipe
        self.recipe = recipe
        self.parent220 = parent220 if parent220 is not None else set()
        self.Recipe232 = Recipe232
        self.Recipe240 = Recipe240
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def recipe222(self):
        return self.__recipe222

    @recipe222.setter
    def recipe222(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Recipe__recipe222", None)
        self.__recipe222 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Infrastructure"):
                    opp_val = getattr(item, "Infrastructure", None)
                    
                    if opp_val == self:
                        setattr(item, "Infrastructure", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Infrastructure"):
                    opp_val = getattr(item, "Infrastructure", None)
                    
                    setattr(item, "Infrastructure", self)
                    

    @property
    def recipe(self):
        return self.__recipe

    @recipe.setter
    def recipe(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Recipe__recipe", None)
        self.__recipe = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Recipes218"):
                opp_val = getattr(old_value, "Recipes218", None)
                if opp_val == self:
                    setattr(old_value, "Recipes218", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Recipes218"):
                opp_val = getattr(value, "Recipes218", None)
                setattr(value, "Recipes218", self)

    @property
    def domain_Recipe(self):
        return self.__domain_Recipe

    @domain_Recipe.setter
    def domain_Recipe(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Recipe__domain_Recipe", None)
        self.__domain_Recipe = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_DeploymentSequence224"):
                opp_val = getattr(old_value, "domain_DeploymentSequence224", None)
                if opp_val == self:
                    setattr(old_value, "domain_DeploymentSequence224", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_DeploymentSequence224"):
                opp_val = getattr(value, "domain_DeploymentSequence224", None)
                setattr(value, "domain_DeploymentSequence224", self)

    @property
    def Recipe(self):
        return self.__Recipe

    @Recipe.setter
    def Recipe(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Recipe__Recipe", None)
        self.__Recipe = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent185"):
                opp_val = getattr(old_value, "parent185", None)
                if opp_val == self:
                    setattr(old_value, "parent185", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent185"):
                opp_val = getattr(value, "parent185", None)
                setattr(value, "parent185", self)

    @property
    def parent220(self):
        return self.__parent220

    @parent220.setter
    def parent220(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Recipe__parent220", None)
        self.__parent220 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Ingredient"):
                    opp_val = getattr(item, "Ingredient", None)
                    
                    if opp_val == self:
                        setattr(item, "Ingredient", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Ingredient"):
                    opp_val = getattr(item, "Ingredient", None)
                    
                    setattr(item, "Ingredient", self)
                    

    @property
    def Recipe240(self):
        return self.__Recipe240

    @Recipe240.setter
    def Recipe240(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Recipe__Recipe240", None)
        self.__Recipe240 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "infrastructures"):
                opp_val = getattr(old_value, "infrastructures", None)
                if opp_val == self:
                    setattr(old_value, "infrastructures", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "infrastructures"):
                opp_val = getattr(value, "infrastructures", None)
                setattr(value, "infrastructures", self)

    @property
    def Recipe232(self):
        return self.__Recipe232

    @Recipe232.setter
    def Recipe232(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Recipe__Recipe232", None)
        self.__Recipe232 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ingredients"):
                opp_val = getattr(old_value, "ingredients", None)
                if opp_val == self:
                    setattr(old_value, "ingredients", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ingredients"):
                opp_val = getattr(value, "ingredients", None)
                setattr(value, "ingredients", self)

class TypeMapper:

    pass
class domain_JavaMapper(TypeMapper):

    def __init__(self, mappedToPackageName: str, mappedToClassName: str, artifactId: str, groupId: str, version: str, libraryName: str, artifactType: str):
        self.mappedToPackageName = mappedToPackageName
        self.mappedToClassName = mappedToClassName
        self.artifactId = artifactId
        self.groupId = groupId
        self.version = version
        self.libraryName = libraryName
        self.artifactType = artifactType
        
    @property
    def mappedToClassName(self) -> str:
        return self.__mappedToClassName

    @mappedToClassName.setter
    def mappedToClassName(self, mappedToClassName: str):
        self.__mappedToClassName = mappedToClassName

    @property
    def artifactId(self) -> str:
        return self.__artifactId

    @artifactId.setter
    def artifactId(self, artifactId: str):
        self.__artifactId = artifactId

    @property
    def libraryName(self) -> str:
        return self.__libraryName

    @libraryName.setter
    def libraryName(self, libraryName: str):
        self.__libraryName = libraryName

    @property
    def artifactType(self) -> str:
        return self.__artifactType

    @artifactType.setter
    def artifactType(self, artifactType: str):
        self.__artifactType = artifactType

    @property
    def groupId(self) -> str:
        return self.__groupId

    @groupId.setter
    def groupId(self, groupId: str):
        self.__groupId = groupId

    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def mappedToPackageName(self) -> str:
        return self.__mappedToPackageName

    @mappedToPackageName.setter
    def mappedToPackageName(self, mappedToPackageName: str):
        self.__mappedToPackageName = mappedToPackageName

class Mapper:

    pass
class domain_RoleMapper(Mapper):

    def __init__(self, localRoleName: str, globalRoleName: str, fakeRoleName: str, domain_RoleMapper: "domain_EObject" = None):
        self.localRoleName = localRoleName
        self.globalRoleName = globalRoleName
        self.fakeRoleName = fakeRoleName
        self.domain_RoleMapper = domain_RoleMapper
        
    @property
    def fakeRoleName(self) -> str:
        return self.__fakeRoleName

    @fakeRoleName.setter
    def fakeRoleName(self, fakeRoleName: str):
        self.__fakeRoleName = fakeRoleName

    @property
    def localRoleName(self) -> str:
        return self.__localRoleName

    @localRoleName.setter
    def localRoleName(self, localRoleName: str):
        self.__localRoleName = localRoleName

    @property
    def globalRoleName(self) -> str:
        return self.__globalRoleName

    @globalRoleName.setter
    def globalRoleName(self, globalRoleName: str):
        self.__globalRoleName = globalRoleName

    @property
    def domain_RoleMapper(self):
        return self.__domain_RoleMapper

    @domain_RoleMapper.setter
    def domain_RoleMapper(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_RoleMapper__domain_RoleMapper", None)
        self.__domain_RoleMapper = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_EObject183"):
                opp_val = getattr(old_value, "domain_EObject183", None)
                if opp_val == self:
                    setattr(old_value, "domain_EObject183", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_EObject183"):
                opp_val = getattr(value, "domain_EObject183", None)
                setattr(value, "domain_EObject183", self)

class domain_CSSMapper(Mapper):

    def __init__(self, fakePackageName: str, fakeTypeName: str, libraryUrl: str, domain_CSSMapper: "domain_StylesPackage" = None, domain_CSSMapper180: "domain_StyleLibrary" = None):
        self.fakePackageName = fakePackageName
        self.fakeTypeName = fakeTypeName
        self.libraryUrl = libraryUrl
        self.domain_CSSMapper = domain_CSSMapper
        self.domain_CSSMapper180 = domain_CSSMapper180
        
    @property
    def libraryUrl(self) -> str:
        return self.__libraryUrl

    @libraryUrl.setter
    def libraryUrl(self, libraryUrl: str):
        self.__libraryUrl = libraryUrl

    @property
    def fakeTypeName(self) -> str:
        return self.__fakeTypeName

    @fakeTypeName.setter
    def fakeTypeName(self, fakeTypeName: str):
        self.__fakeTypeName = fakeTypeName

    @property
    def fakePackageName(self) -> str:
        return self.__fakePackageName

    @fakePackageName.setter
    def fakePackageName(self, fakePackageName: str):
        self.__fakePackageName = fakePackageName

    @property
    def domain_CSSMapper(self):
        return self.__domain_CSSMapper

    @domain_CSSMapper.setter
    def domain_CSSMapper(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_CSSMapper__domain_CSSMapper", None)
        self.__domain_CSSMapper = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_StylesPackage"):
                opp_val = getattr(old_value, "domain_StylesPackage", None)
                if opp_val == self:
                    setattr(old_value, "domain_StylesPackage", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_StylesPackage"):
                opp_val = getattr(value, "domain_StylesPackage", None)
                setattr(value, "domain_StylesPackage", self)

    @property
    def domain_CSSMapper180(self):
        return self.__domain_CSSMapper180

    @domain_CSSMapper180.setter
    def domain_CSSMapper180(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_CSSMapper__domain_CSSMapper180", None)
        self.__domain_CSSMapper180 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_StyleLibrary181"):
                opp_val = getattr(old_value, "domain_StyleLibrary181", None)
                if opp_val == self:
                    setattr(old_value, "domain_StyleLibrary181", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_StyleLibrary181"):
                opp_val = getattr(value, "domain_StyleLibrary181", None)
                setattr(value, "domain_StyleLibrary181", self)

class domain_JavaScriptMapper(TypeMapper):

    def __init__(self, libraryUrl: str):
        self.libraryUrl = libraryUrl
        
    @property
    def libraryUrl(self) -> str:
        return self.__libraryUrl

    @libraryUrl.setter
    def libraryUrl(self, libraryUrl: str):
        self.__libraryUrl = libraryUrl

class domain_Mapper:

    def __init__(self, uid: str, serviceLayer: bool, uiLayer: bool, Mapper: "domain_Mappers" = None, mappers176: "domain_Mappers" = None):
        self.uid = uid
        self.serviceLayer = serviceLayer
        self.uiLayer = uiLayer
        self.Mapper = Mapper
        self.mappers176 = mappers176
        
    @property
    def uiLayer(self) -> bool:
        return self.__uiLayer

    @uiLayer.setter
    def uiLayer(self, uiLayer: bool):
        self.__uiLayer = uiLayer

    @property
    def serviceLayer(self) -> bool:
        return self.__serviceLayer

    @serviceLayer.setter
    def serviceLayer(self, serviceLayer: bool):
        self.__serviceLayer = serviceLayer

    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def Mapper(self):
        return self.__Mapper

    @Mapper.setter
    def Mapper(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Mapper__Mapper", None)
        self.__Mapper = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent170"):
                opp_val = getattr(old_value, "parent170", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent170"):
                opp_val = getattr(value, "parent170", None)
                if opp_val is None:
                    setattr(value, "parent170", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mappers176(self):
        return self.__mappers176

    @mappers176.setter
    def mappers176(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Mapper__mappers176", None)
        self.__mappers176 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Mappers177"):
                opp_val = getattr(old_value, "Mappers177", None)
                if opp_val == self:
                    setattr(old_value, "Mappers177", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Mappers177"):
                opp_val = getattr(value, "Mappers177", None)
                setattr(value, "Mappers177", self)

class domain_StyleSet:

    def __init__(self, uid: str, name: str, domain_StyleSet: "domain_StyleLibrary" = None):
        self.uid = uid
        self.name = name
        self.domain_StyleSet = domain_StyleSet
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def domain_StyleSet(self):
        return self.__domain_StyleSet

    @domain_StyleSet.setter
    def domain_StyleSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_StyleSet__domain_StyleSet", None)
        self.__domain_StyleSet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_StyleLibrary168"):
                opp_val = getattr(old_value, "domain_StyleLibrary168", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_StyleLibrary168"):
                opp_val = getattr(value, "domain_StyleLibrary168", None)
                if opp_val is None:
                    setattr(value, "domain_StyleLibrary168", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class domain_StyleLibrary:

    def __init__(self, uid: str, name: str, domain_StyleLibrary: "domain_Styles" = None, domain_StyleLibrary168: set["domain_StyleSet"] = None, domain_StyleLibrary181: "domain_CSSMapper" = None):
        self.uid = uid
        self.name = name
        self.domain_StyleLibrary = domain_StyleLibrary
        self.domain_StyleLibrary168 = domain_StyleLibrary168 if domain_StyleLibrary168 is not None else set()
        self.domain_StyleLibrary181 = domain_StyleLibrary181
        
    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def domain_StyleLibrary(self):
        return self.__domain_StyleLibrary

    @domain_StyleLibrary.setter
    def domain_StyleLibrary(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_StyleLibrary__domain_StyleLibrary", None)
        self.__domain_StyleLibrary = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_Styles"):
                opp_val = getattr(old_value, "domain_Styles", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_Styles"):
                opp_val = getattr(value, "domain_Styles", None)
                if opp_val is None:
                    setattr(value, "domain_Styles", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def domain_StyleLibrary168(self):
        return self.__domain_StyleLibrary168

    @domain_StyleLibrary168.setter
    def domain_StyleLibrary168(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_StyleLibrary__domain_StyleLibrary168", None)
        self.__domain_StyleLibrary168 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "domain_StyleSet"):
                    opp_val = getattr(item, "domain_StyleSet", None)
                    
                    if opp_val == self:
                        setattr(item, "domain_StyleSet", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "domain_StyleSet"):
                    opp_val = getattr(item, "domain_StyleSet", None)
                    
                    setattr(item, "domain_StyleSet", self)
                    

    @property
    def domain_StyleLibrary181(self):
        return self.__domain_StyleLibrary181

    @domain_StyleLibrary181.setter
    def domain_StyleLibrary181(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_StyleLibrary__domain_StyleLibrary181", None)
        self.__domain_StyleLibrary181 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_CSSMapper180"):
                opp_val = getattr(old_value, "domain_CSSMapper180", None)
                if opp_val == self:
                    setattr(old_value, "domain_CSSMapper180", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_CSSMapper180"):
                opp_val = getattr(value, "domain_CSSMapper180", None)
                setattr(value, "domain_CSSMapper180", self)

class domain_Group:

    def __init__(self, uid: str, name: str, domain_Group: "domain_Roles" = None, domain_Group159: set["domain_Role"] = None, domain_Group157: "domain_Group" = None, domain_Group155: set["domain_Group"] = None):
        self.uid = uid
        self.name = name
        self.domain_Group = domain_Group
        self.domain_Group159 = domain_Group159 if domain_Group159 is not None else set()
        self.domain_Group157 = domain_Group157
        self.domain_Group155 = domain_Group155 if domain_Group155 is not None else set()
        
    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def domain_Group155(self):
        return self.__domain_Group155

    @domain_Group155.setter
    def domain_Group155(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Group__domain_Group155", None)
        self.__domain_Group155 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "domain_Group157"):
                    opp_val = getattr(item, "domain_Group157", None)
                    
                    if opp_val == self:
                        setattr(item, "domain_Group157", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "domain_Group157"):
                    opp_val = getattr(item, "domain_Group157", None)
                    
                    setattr(item, "domain_Group157", self)
                    

    @property
    def domain_Group157(self):
        return self.__domain_Group157

    @domain_Group157.setter
    def domain_Group157(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Group__domain_Group157", None)
        self.__domain_Group157 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_Group155"):
                opp_val = getattr(old_value, "domain_Group155", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_Group155"):
                opp_val = getattr(value, "domain_Group155", None)
                if opp_val is None:
                    setattr(value, "domain_Group155", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def domain_Group159(self):
        return self.__domain_Group159

    @domain_Group159.setter
    def domain_Group159(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Group__domain_Group159", None)
        self.__domain_Group159 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "domain_Role160"):
                    opp_val = getattr(item, "domain_Role160", None)
                    
                    if opp_val == self:
                        setattr(item, "domain_Role160", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "domain_Role160"):
                    opp_val = getattr(item, "domain_Role160", None)
                    
                    setattr(item, "domain_Role160", self)
                    

    @property
    def domain_Group(self):
        return self.__domain_Group

    @domain_Group.setter
    def domain_Group(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Group__domain_Group", None)
        self.__domain_Group = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_Roles151"):
                opp_val = getattr(old_value, "domain_Roles151", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_Roles151"):
                opp_val = getattr(value, "domain_Roles151", None)
                if opp_val is None:
                    setattr(value, "domain_Roles151", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class domain_Translation:

    def __init__(self, uid: str, translation: str, domain_Translation: "domain_Message" = None, domain_Translation144: "domain_LanguageRef" = None):
        self.uid = uid
        self.translation = translation
        self.domain_Translation = domain_Translation
        self.domain_Translation144 = domain_Translation144
        
    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def translation(self) -> str:
        return self.__translation

    @translation.setter
    def translation(self, translation: str):
        self.__translation = translation

    @property
    def domain_Translation144(self):
        return self.__domain_Translation144

    @domain_Translation144.setter
    def domain_Translation144(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Translation__domain_Translation144", None)
        self.__domain_Translation144 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_LanguageRef145"):
                opp_val = getattr(old_value, "domain_LanguageRef145", None)
                if opp_val == self:
                    setattr(old_value, "domain_LanguageRef145", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_LanguageRef145"):
                opp_val = getattr(value, "domain_LanguageRef145", None)
                setattr(value, "domain_LanguageRef145", self)

    @property
    def domain_Translation(self):
        return self.__domain_Translation

    @domain_Translation.setter
    def domain_Translation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Translation__domain_Translation", None)
        self.__domain_Translation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_Message142"):
                opp_val = getattr(old_value, "domain_Message142", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_Message142"):
                opp_val = getattr(value, "domain_Message142", None)
                if opp_val is None:
                    setattr(value, "domain_Message142", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class domain_Message:

    def __init__(self, uid: str, name: str, domain_Message: "domain_MessageLibrary" = None, domain_Message142: set["domain_Translation"] = None):
        self.uid = uid
        self.name = name
        self.domain_Message = domain_Message
        self.domain_Message142 = domain_Message142 if domain_Message142 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def domain_Message142(self):
        return self.__domain_Message142

    @domain_Message142.setter
    def domain_Message142(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Message__domain_Message142", None)
        self.__domain_Message142 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "domain_Translation"):
                    opp_val = getattr(item, "domain_Translation", None)
                    
                    if opp_val == self:
                        setattr(item, "domain_Translation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "domain_Translation"):
                    opp_val = getattr(item, "domain_Translation", None)
                    
                    setattr(item, "domain_Translation", self)
                    

    @property
    def domain_Message(self):
        return self.__domain_Message

    @domain_Message.setter
    def domain_Message(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Message__domain_Message", None)
        self.__domain_Message = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_MessageLibrary137"):
                opp_val = getattr(old_value, "domain_MessageLibrary137", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_MessageLibrary137"):
                opp_val = getattr(value, "domain_MessageLibrary137", None)
                if opp_val is None:
                    setattr(value, "domain_MessageLibrary137", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class domain_LanguageRef:

    def __init__(self, uid: str, domain_LanguageRef: "domain_MessageLibrary" = None, domain_LanguageRef139: "domain_Language" = None, domain_LanguageRef145: "domain_Translation" = None):
        self.uid = uid
        self.domain_LanguageRef = domain_LanguageRef
        self.domain_LanguageRef139 = domain_LanguageRef139
        self.domain_LanguageRef145 = domain_LanguageRef145
        
    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def domain_LanguageRef139(self):
        return self.__domain_LanguageRef139

    @domain_LanguageRef139.setter
    def domain_LanguageRef139(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_LanguageRef__domain_LanguageRef139", None)
        self.__domain_LanguageRef139 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_Language140"):
                opp_val = getattr(old_value, "domain_Language140", None)
                if opp_val == self:
                    setattr(old_value, "domain_Language140", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_Language140"):
                opp_val = getattr(value, "domain_Language140", None)
                setattr(value, "domain_Language140", self)

    @property
    def domain_LanguageRef145(self):
        return self.__domain_LanguageRef145

    @domain_LanguageRef145.setter
    def domain_LanguageRef145(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_LanguageRef__domain_LanguageRef145", None)
        self.__domain_LanguageRef145 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_Translation144"):
                opp_val = getattr(old_value, "domain_Translation144", None)
                if opp_val == self:
                    setattr(old_value, "domain_Translation144", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_Translation144"):
                opp_val = getattr(value, "domain_Translation144", None)
                setattr(value, "domain_Translation144", self)

    @property
    def domain_LanguageRef(self):
        return self.__domain_LanguageRef

    @domain_LanguageRef.setter
    def domain_LanguageRef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_LanguageRef__domain_LanguageRef", None)
        self.__domain_LanguageRef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_MessageLibrary135"):
                opp_val = getattr(old_value, "domain_MessageLibrary135", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_MessageLibrary135"):
                opp_val = getattr(value, "domain_MessageLibrary135", None)
                if opp_val is None:
                    setattr(value, "domain_MessageLibrary135", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Categorized:

    pass
class domain_MenuElement(Categorized, Orderable, MultiLangLabel, EnabledUIItem, StyleElement):

    def __init__(self, uid: str, name: str, domain_MenuElement: "domain_MenuFolder" = None):
        self.uid = uid
        self.name = name
        self.domain_MenuElement = domain_MenuElement
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def domain_MenuElement(self):
        return self.__domain_MenuElement

    @domain_MenuElement.setter
    def domain_MenuElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_MenuElement__domain_MenuElement", None)
        self.__domain_MenuElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_MenuFolder596"):
                opp_val = getattr(old_value, "domain_MenuFolder596", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_MenuFolder596"):
                opp_val = getattr(value, "domain_MenuFolder596", None)
                if opp_val is None:
                    setattr(value, "domain_MenuFolder596", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class domain_Canvas(Categorized, MultiLangLabel, ViewPortHolder, CanvasFrame, DefaultCavas):

    pass
class domain_Type(Categorized, TypeElement):

    pass
class domain_PopupCanvas(FlexFields, Categorized, MultiLangLabel, ViewPortHolder, CanvasFrame, DefaultCavas):

    def __init__(self, modal: bool):
        self.modal = modal
        
    @property
    def modal(self) -> bool:
        return self.__modal

    @modal.setter
    def modal(self, modal: bool):
        self.__modal = modal

class domain_TabCanvas(Categorized, CanvasFrame, MultiLangLabel, DefaultCavas):

    def __init__(self, orientation: str, domain_TabCanvas: "domain_TabPagesInheritance" = None):
        self.orientation = orientation
        self.domain_TabCanvas = domain_TabCanvas
        
    @property
    def orientation(self) -> str:
        return self.__orientation

    @orientation.setter
    def orientation(self, orientation: str):
        self.__orientation = orientation

    @property
    def domain_TabCanvas(self):
        return self.__domain_TabCanvas

    @domain_TabCanvas.setter
    def domain_TabCanvas(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_TabCanvas__domain_TabCanvas", None)
        self.__domain_TabCanvas = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_TabPagesInheritance376"):
                opp_val = getattr(old_value, "domain_TabPagesInheritance376", None)
                if opp_val == self:
                    setattr(old_value, "domain_TabPagesInheritance376", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_TabPagesInheritance376"):
                opp_val = getattr(value, "domain_TabPagesInheritance376", None)
                setattr(value, "domain_TabPagesInheritance376", self)

class domain_Window(Categorized, MultiLangLabel, Secured, ViewPortHolder, CanvasFrame):

    pass
class domain_MenuDefinition(Categorized, StyleElement):

    def __init__(self, uid: str, name: str, domain_MenuDefinition: "domain_Views" = None, parent365: "domain_MenuView" = None, MenuDefinition: "domain_MenuView" = None):
        self.uid = uid
        self.name = name
        self.domain_MenuDefinition = domain_MenuDefinition
        self.parent365 = parent365
        self.MenuDefinition = MenuDefinition
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def MenuDefinition(self):
        return self.__MenuDefinition

    @MenuDefinition.setter
    def MenuDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_MenuDefinition__MenuDefinition", None)
        self.__MenuDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "menuView"):
                opp_val = getattr(old_value, "menuView", None)
                if opp_val == self:
                    setattr(old_value, "menuView", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "menuView"):
                opp_val = getattr(value, "menuView", None)
                setattr(value, "menuView", self)

    @property
    def parent365(self):
        return self.__parent365

    @parent365.setter
    def parent365(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_MenuDefinition__parent365", None)
        self.__parent365 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MenuView"):
                opp_val = getattr(old_value, "MenuView", None)
                if opp_val == self:
                    setattr(old_value, "MenuView", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MenuView"):
                opp_val = getattr(value, "MenuView", None)
                setattr(value, "MenuView", self)

    @property
    def domain_MenuDefinition(self):
        return self.__domain_MenuDefinition

    @domain_MenuDefinition.setter
    def domain_MenuDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_MenuDefinition__domain_MenuDefinition", None)
        self.__domain_MenuDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_Views358"):
                opp_val = getattr(old_value, "domain_Views358", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_Views358"):
                opp_val = getattr(value, "domain_Views358", None)
                if opp_val is None:
                    setattr(value, "domain_Views358", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class domain_FlexField(Categorized, Context):

    pass
class domain_TabPage(Categorized, Orderable, MultiLangLabel, ViewPortHolder, CanvasFrame):

    pass
class domain_RelationShip(Categorized):

    def __init__(self, uid: str, domain_RelationShip289: "domain_TypeElement" = None, domain_RelationShip292: "domain_TypeElement" = None, domain_RelationShip: "domain_TypeDefinition" = None):
        self.uid = uid
        self.domain_RelationShip289 = domain_RelationShip289
        self.domain_RelationShip292 = domain_RelationShip292
        self.domain_RelationShip = domain_RelationShip
        
    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def domain_RelationShip(self):
        return self.__domain_RelationShip

    @domain_RelationShip.setter
    def domain_RelationShip(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_RelationShip__domain_RelationShip", None)
        self.__domain_RelationShip = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_TypeDefinition"):
                opp_val = getattr(old_value, "domain_TypeDefinition", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_TypeDefinition"):
                opp_val = getattr(value, "domain_TypeDefinition", None)
                if opp_val is None:
                    setattr(value, "domain_TypeDefinition", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def domain_RelationShip289(self):
        return self.__domain_RelationShip289

    @domain_RelationShip289.setter
    def domain_RelationShip289(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_RelationShip__domain_RelationShip289", None)
        self.__domain_RelationShip289 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_TypeElement290"):
                opp_val = getattr(old_value, "domain_TypeElement290", None)
                if opp_val == self:
                    setattr(old_value, "domain_TypeElement290", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_TypeElement290"):
                opp_val = getattr(value, "domain_TypeElement290", None)
                setattr(value, "domain_TypeElement290", self)

    @property
    def domain_RelationShip292(self):
        return self.__domain_RelationShip292

    @domain_RelationShip292.setter
    def domain_RelationShip292(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_RelationShip__domain_RelationShip292", None)
        self.__domain_RelationShip292 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_TypeElement293"):
                opp_val = getattr(old_value, "domain_TypeElement293", None)
                if opp_val == self:
                    setattr(old_value, "domain_TypeElement293", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_TypeElement293"):
                opp_val = getattr(value, "domain_TypeElement293", None)
                setattr(value, "domain_TypeElement293", self)

class domain_ViewElement(Categorized, NickNamed, StyleElement):

    pass
class domain_Uielement(FlexFields, Categorized, NickNamed, Orderable, EnabledUIItem, MenuHolder, StyleElement):

    def __init__(self, uid: str, domain_Uielement: "domain_ChildrenHolder" = None, domain_Uielement422: "domain_Context" = None, domain_Uielement425: "domain_Context" = None, domain_Uielement428: set["domain_AreaRef"] = None, domain_Uielement461: "domain_Column" = None):
        self.uid = uid
        self.domain_Uielement = domain_Uielement
        self.domain_Uielement422 = domain_Uielement422
        self.domain_Uielement425 = domain_Uielement425
        self.domain_Uielement428 = domain_Uielement428 if domain_Uielement428 is not None else set()
        self.domain_Uielement461 = domain_Uielement461
        
    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def domain_Uielement461(self):
        return self.__domain_Uielement461

    @domain_Uielement461.setter
    def domain_Uielement461(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Uielement__domain_Uielement461", None)
        self.__domain_Uielement461 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_Column"):
                opp_val = getattr(old_value, "domain_Column", None)
                if opp_val == self:
                    setattr(old_value, "domain_Column", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_Column"):
                opp_val = getattr(value, "domain_Column", None)
                setattr(value, "domain_Column", self)

    @property
    def domain_Uielement422(self):
        return self.__domain_Uielement422

    @domain_Uielement422.setter
    def domain_Uielement422(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Uielement__domain_Uielement422", None)
        self.__domain_Uielement422 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_Context423"):
                opp_val = getattr(old_value, "domain_Context423", None)
                if opp_val == self:
                    setattr(old_value, "domain_Context423", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_Context423"):
                opp_val = getattr(value, "domain_Context423", None)
                setattr(value, "domain_Context423", self)

    @property
    def domain_Uielement428(self):
        return self.__domain_Uielement428

    @domain_Uielement428.setter
    def domain_Uielement428(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Uielement__domain_Uielement428", None)
        self.__domain_Uielement428 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "domain_AreaRef"):
                    opp_val = getattr(item, "domain_AreaRef", None)
                    
                    if opp_val == self:
                        setattr(item, "domain_AreaRef", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "domain_AreaRef"):
                    opp_val = getattr(item, "domain_AreaRef", None)
                    
                    setattr(item, "domain_AreaRef", self)
                    

    @property
    def domain_Uielement425(self):
        return self.__domain_Uielement425

    @domain_Uielement425.setter
    def domain_Uielement425(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Uielement__domain_Uielement425", None)
        self.__domain_Uielement425 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_Context426"):
                opp_val = getattr(old_value, "domain_Context426", None)
                if opp_val == self:
                    setattr(old_value, "domain_Context426", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_Context426"):
                opp_val = getattr(value, "domain_Context426", None)
                setattr(value, "domain_Context426", self)

    @property
    def domain_Uielement(self):
        return self.__domain_Uielement

    @domain_Uielement.setter
    def domain_Uielement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Uielement__domain_Uielement", None)
        self.__domain_Uielement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_ChildrenHolder"):
                opp_val = getattr(old_value, "domain_ChildrenHolder", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_ChildrenHolder"):
                opp_val = getattr(value, "domain_ChildrenHolder", None)
                if opp_val is None:
                    setattr(value, "domain_ChildrenHolder", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class domain_Language:

    def __init__(self, uid: str, lang: str, code: str, defaultLang: bool, domain_Language: "domain_Messages" = None, domain_Language140: "domain_LanguageRef" = None):
        self.uid = uid
        self.lang = lang
        self.code = code
        self.defaultLang = defaultLang
        self.domain_Language = domain_Language
        self.domain_Language140 = domain_Language140
        
    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def defaultLang(self) -> bool:
        return self.__defaultLang

    @defaultLang.setter
    def defaultLang(self, defaultLang: bool):
        self.__defaultLang = defaultLang

    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def domain_Language(self):
        return self.__domain_Language

    @domain_Language.setter
    def domain_Language(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Language__domain_Language", None)
        self.__domain_Language = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_Messages130"):
                opp_val = getattr(old_value, "domain_Messages130", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_Messages130"):
                opp_val = getattr(value, "domain_Messages130", None)
                if opp_val is None:
                    setattr(value, "domain_Messages130", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def domain_Language140(self):
        return self.__domain_Language140

    @domain_Language140.setter
    def domain_Language140(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Language__domain_Language140", None)
        self.__domain_Language140 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_LanguageRef139"):
                opp_val = getattr(old_value, "domain_LanguageRef139", None)
                if opp_val == self:
                    setattr(old_value, "domain_LanguageRef139", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_LanguageRef139"):
                opp_val = getattr(value, "domain_LanguageRef139", None)
                setattr(value, "domain_LanguageRef139", self)

class domain_MessageLibrary(Categorized):

    def __init__(self, uid: str, name: str, domain_MessageLibrary: "domain_Messages" = None, domain_MessageLibrary135: set["domain_LanguageRef"] = None, domain_MessageLibrary137: set["domain_Message"] = None):
        self.uid = uid
        self.name = name
        self.domain_MessageLibrary = domain_MessageLibrary
        self.domain_MessageLibrary135 = domain_MessageLibrary135 if domain_MessageLibrary135 is not None else set()
        self.domain_MessageLibrary137 = domain_MessageLibrary137 if domain_MessageLibrary137 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def domain_MessageLibrary137(self):
        return self.__domain_MessageLibrary137

    @domain_MessageLibrary137.setter
    def domain_MessageLibrary137(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_MessageLibrary__domain_MessageLibrary137", None)
        self.__domain_MessageLibrary137 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "domain_Message"):
                    opp_val = getattr(item, "domain_Message", None)
                    
                    if opp_val == self:
                        setattr(item, "domain_Message", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "domain_Message"):
                    opp_val = getattr(item, "domain_Message", None)
                    
                    setattr(item, "domain_Message", self)
                    

    @property
    def domain_MessageLibrary(self):
        return self.__domain_MessageLibrary

    @domain_MessageLibrary.setter
    def domain_MessageLibrary(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_MessageLibrary__domain_MessageLibrary", None)
        self.__domain_MessageLibrary = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_Messages"):
                opp_val = getattr(old_value, "domain_Messages", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_Messages"):
                opp_val = getattr(value, "domain_Messages", None)
                if opp_val is None:
                    setattr(value, "domain_Messages", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def domain_MessageLibrary135(self):
        return self.__domain_MessageLibrary135

    @domain_MessageLibrary135.setter
    def domain_MessageLibrary135(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_MessageLibrary__domain_MessageLibrary135", None)
        self.__domain_MessageLibrary135 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "domain_LanguageRef"):
                    opp_val = getattr(item, "domain_LanguageRef", None)
                    
                    if opp_val == self:
                        setattr(item, "domain_LanguageRef", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "domain_LanguageRef"):
                    opp_val = getattr(item, "domain_LanguageRef", None)
                    
                    setattr(item, "domain_LanguageRef", self)
                    

class domain_Operation(Categorized, Secured):

    def __init__(self, uid: str, name: str, domain_Operation: "domain_MethodPointer" = None, Operation: "domain_Type" = None, operations: "domain_Type" = None, parent312: set["domain_Parameter"] = None, domain_Operation314: "domain_ReturnValue" = None, Operation317: "domain_Parameter" = None):
        self.uid = uid
        self.name = name
        self.domain_Operation = domain_Operation
        self.Operation = Operation
        self.operations = operations
        self.parent312 = parent312 if parent312 is not None else set()
        self.domain_Operation314 = domain_Operation314
        self.Operation317 = Operation317
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def Operation(self):
        return self.__Operation

    @Operation.setter
    def Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Operation__Operation", None)
        self.__Operation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent307"):
                opp_val = getattr(old_value, "parent307", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent307"):
                opp_val = getattr(value, "parent307", None)
                if opp_val is None:
                    setattr(value, "parent307", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def parent312(self):
        return self.__parent312

    @parent312.setter
    def parent312(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Operation__parent312", None)
        self.__parent312 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Parameter"):
                    opp_val = getattr(item, "Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Parameter"):
                    opp_val = getattr(item, "Parameter", None)
                    
                    setattr(item, "Parameter", self)
                    

    @property
    def domain_Operation314(self):
        return self.__domain_Operation314

    @domain_Operation314.setter
    def domain_Operation314(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Operation__domain_Operation314", None)
        self.__domain_Operation314 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_ReturnValue"):
                opp_val = getattr(old_value, "domain_ReturnValue", None)
                if opp_val == self:
                    setattr(old_value, "domain_ReturnValue", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_ReturnValue"):
                opp_val = getattr(value, "domain_ReturnValue", None)
                setattr(value, "domain_ReturnValue", self)

    @property
    def domain_Operation(self):
        return self.__domain_Operation

    @domain_Operation.setter
    def domain_Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Operation__domain_Operation", None)
        self.__domain_Operation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_MethodPointer"):
                opp_val = getattr(old_value, "domain_MethodPointer", None)
                if opp_val == self:
                    setattr(old_value, "domain_MethodPointer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_MethodPointer"):
                opp_val = getattr(value, "domain_MethodPointer", None)
                setattr(value, "domain_MethodPointer", self)

    @property
    def operations(self):
        return self.__operations

    @operations.setter
    def operations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Operation__operations", None)
        self.__operations = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Type310"):
                opp_val = getattr(old_value, "Type310", None)
                if opp_val == self:
                    setattr(old_value, "Type310", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Type310"):
                opp_val = getattr(value, "Type310", None)
                setattr(value, "Type310", self)

    @property
    def Operation317(self):
        return self.__Operation317

    @Operation317.setter
    def Operation317(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Operation__Operation317", None)
        self.__Operation317 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parameters316"):
                opp_val = getattr(old_value, "parameters316", None)
                if opp_val == self:
                    setattr(old_value, "parameters316", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parameters316"):
                opp_val = getattr(value, "parameters316", None)
                setattr(value, "parameters316", self)

class TypePointer:

    pass
class domain_Attribute(Categorized, TypePointer):

    def __init__(self, uid: str, name: str, pk: bool, domain_Attribute: "domain_Assosiation" = None, domain_Attribute299: "domain_Assosiation" = None, Attribute: "domain_Type" = None, attributes: "domain_Type" = None, domain_Attribute550: "domain_Link" = None, domain_Attribute553: "domain_Link" = None):
        self.uid = uid
        self.name = name
        self.pk = pk
        self.domain_Attribute = domain_Attribute
        self.domain_Attribute299 = domain_Attribute299
        self.Attribute = Attribute
        self.attributes = attributes
        self.domain_Attribute550 = domain_Attribute550
        self.domain_Attribute553 = domain_Attribute553
        
    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def pk(self) -> bool:
        return self.__pk

    @pk.setter
    def pk(self, pk: bool):
        self.__pk = pk

    @property
    def domain_Attribute(self):
        return self.__domain_Attribute

    @domain_Attribute.setter
    def domain_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Attribute__domain_Attribute", None)
        self.__domain_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_Assosiation296"):
                opp_val = getattr(old_value, "domain_Assosiation296", None)
                if opp_val == self:
                    setattr(old_value, "domain_Assosiation296", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_Assosiation296"):
                opp_val = getattr(value, "domain_Assosiation296", None)
                setattr(value, "domain_Assosiation296", self)

    @property
    def Attribute(self):
        return self.__Attribute

    @Attribute.setter
    def Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Attribute__Attribute", None)
        self.__Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent305"):
                opp_val = getattr(old_value, "parent305", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent305"):
                opp_val = getattr(value, "parent305", None)
                if opp_val is None:
                    setattr(value, "parent305", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def domain_Attribute299(self):
        return self.__domain_Attribute299

    @domain_Attribute299.setter
    def domain_Attribute299(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Attribute__domain_Attribute299", None)
        self.__domain_Attribute299 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_Assosiation298"):
                opp_val = getattr(old_value, "domain_Assosiation298", None)
                if opp_val == self:
                    setattr(old_value, "domain_Assosiation298", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_Assosiation298"):
                opp_val = getattr(value, "domain_Assosiation298", None)
                setattr(value, "domain_Assosiation298", self)

    @property
    def domain_Attribute550(self):
        return self.__domain_Attribute550

    @domain_Attribute550.setter
    def domain_Attribute550(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Attribute__domain_Attribute550", None)
        self.__domain_Attribute550 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_Link549"):
                opp_val = getattr(old_value, "domain_Link549", None)
                if opp_val == self:
                    setattr(old_value, "domain_Link549", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_Link549"):
                opp_val = getattr(value, "domain_Link549", None)
                setattr(value, "domain_Link549", self)

    @property
    def attributes(self):
        return self.__attributes

    @attributes.setter
    def attributes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Attribute__attributes", None)
        self.__attributes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Type"):
                opp_val = getattr(old_value, "Type", None)
                if opp_val == self:
                    setattr(old_value, "Type", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Type"):
                opp_val = getattr(value, "Type", None)
                setattr(value, "Type", self)

    @property
    def domain_Attribute553(self):
        return self.__domain_Attribute553

    @domain_Attribute553.setter
    def domain_Attribute553(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Attribute__domain_Attribute553", None)
        self.__domain_Attribute553 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_Link552"):
                opp_val = getattr(old_value, "domain_Link552", None)
                if opp_val == self:
                    setattr(old_value, "domain_Link552", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_Link552"):
                opp_val = getattr(value, "domain_Link552", None)
                setattr(value, "domain_Link552", self)

class domain_TypeMapper(Mapper, TypePointer):

    pass
class domain_Parameter(TypePointer):

    def __init__(self, uid: str, name: str, order: int, Parameter: "domain_Operation" = None, parameters316: "domain_Operation" = None):
        self.uid = uid
        self.name = name
        self.order = order
        self.Parameter = Parameter
        self.parameters316 = parameters316
        
    @property
    def order(self) -> int:
        return self.__order

    @order.setter
    def order(self, order: int):
        self.__order = order

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def Parameter(self):
        return self.__Parameter

    @Parameter.setter
    def Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Parameter__Parameter", None)
        self.__Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent312"):
                opp_val = getattr(old_value, "parent312", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent312"):
                opp_val = getattr(value, "parent312", None)
                if opp_val is None:
                    setattr(value, "parent312", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def parameters316(self):
        return self.__parameters316

    @parameters316.setter
    def parameters316(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Parameter__parameters316", None)
        self.__parameters316 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Operation317"):
                opp_val = getattr(old_value, "Operation317", None)
                if opp_val == self:
                    setattr(old_value, "Operation317", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Operation317"):
                opp_val = getattr(value, "Operation317", None)
                setattr(value, "Operation317", self)

class domain_ReturnValue(TypePointer):

    def __init__(self, uid: str, domain_ReturnValue: "domain_Operation" = None):
        self.uid = uid
        self.domain_ReturnValue = domain_ReturnValue
        
    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def domain_ReturnValue(self):
        return self.__domain_ReturnValue

    @domain_ReturnValue.setter
    def domain_ReturnValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_ReturnValue__domain_ReturnValue", None)
        self.__domain_ReturnValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_Operation314"):
                opp_val = getattr(old_value, "domain_Operation314", None)
                if opp_val == self:
                    setattr(old_value, "domain_Operation314", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_Operation314"):
                opp_val = getattr(value, "domain_Operation314", None)
                setattr(value, "domain_Operation314", self)

class domain_ArtificialField(TypePointer):

    def __init__(self, uid: str, name: str, ArtificialField: "domain_DataControl" = None, artificialFields: "domain_DataControl" = None):
        self.uid = uid
        self.name = name
        self.ArtificialField = ArtificialField
        self.artificialFields = artificialFields
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def ArtificialField(self):
        return self.__ArtificialField

    @ArtificialField.setter
    def ArtificialField(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_ArtificialField__ArtificialField", None)
        self.__ArtificialField = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent520"):
                opp_val = getattr(old_value, "parent520", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent520"):
                opp_val = getattr(value, "parent520", None)
                if opp_val is None:
                    setattr(value, "parent520", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def artificialFields(self):
        return self.__artificialFields

    @artificialFields.setter
    def artificialFields(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_ArtificialField__artificialFields", None)
        self.__artificialFields = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DataControl547"):
                opp_val = getattr(old_value, "DataControl547", None)
                if opp_val == self:
                    setattr(old_value, "DataControl547", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DataControl547"):
                opp_val = getattr(value, "DataControl547", None)
                setattr(value, "DataControl547", self)

class domain_TypeReference(TypePointer, TypeElement):

    pass
class domain_FormParameter(TypePointer):

    def __init__(self, uid: str, name: str, domain_FormParameter: "domain_Form" = None, domain_FormParameter488: "domain_FormVariable" = None):
        self.uid = uid
        self.name = name
        self.domain_FormParameter = domain_FormParameter
        self.domain_FormParameter488 = domain_FormParameter488
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def domain_FormParameter(self):
        return self.__domain_FormParameter

    @domain_FormParameter.setter
    def domain_FormParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_FormParameter__domain_FormParameter", None)
        self.__domain_FormParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_Form348"):
                opp_val = getattr(old_value, "domain_Form348", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_Form348"):
                opp_val = getattr(value, "domain_Form348", None)
                if opp_val is None:
                    setattr(value, "domain_Form348", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def domain_FormParameter488(self):
        return self.__domain_FormParameter488

    @domain_FormParameter488.setter
    def domain_FormParameter488(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_FormParameter__domain_FormParameter488", None)
        self.__domain_FormParameter488 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_FormVariable487"):
                opp_val = getattr(old_value, "domain_FormVariable487", None)
                if opp_val == self:
                    setattr(old_value, "domain_FormVariable487", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_FormVariable487"):
                opp_val = getattr(value, "domain_FormVariable487", None)
                setattr(value, "domain_FormVariable487", self)

class domain_FormVariable(TypePointer):

    def __init__(self, uid: str, name: str, domain_FormVariable: "domain_Root" = None, domain_FormVariable487: "domain_FormParameter" = None):
        self.uid = uid
        self.name = name
        self.domain_FormVariable = domain_FormVariable
        self.domain_FormVariable487 = domain_FormVariable487
        
    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def domain_FormVariable(self):
        return self.__domain_FormVariable

    @domain_FormVariable.setter
    def domain_FormVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_FormVariable__domain_FormVariable", None)
        self.__domain_FormVariable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_Root485"):
                opp_val = getattr(old_value, "domain_Root485", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_Root485"):
                opp_val = getattr(value, "domain_Root485", None)
                if opp_val is None:
                    setattr(value, "domain_Root485", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def domain_FormVariable487(self):
        return self.__domain_FormVariable487

    @domain_FormVariable487.setter
    def domain_FormVariable487(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_FormVariable__domain_FormVariable487", None)
        self.__domain_FormVariable487 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_FormParameter488"):
                opp_val = getattr(old_value, "domain_FormParameter488", None)
                if opp_val == self:
                    setattr(old_value, "domain_FormParameter488", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_FormParameter488"):
                opp_val = getattr(value, "domain_FormParameter488", None)
                setattr(value, "domain_FormParameter488", self)

class domain_MethodPointer(TypePointer):

    def __init__(self, fakeMethod: str, domain_MethodPointer: "domain_Operation" = None):
        self.fakeMethod = fakeMethod
        self.domain_MethodPointer = domain_MethodPointer
        
    @property
    def fakeMethod(self) -> str:
        return self.__fakeMethod

    @fakeMethod.setter
    def fakeMethod(self, fakeMethod: str):
        self.__fakeMethod = fakeMethod

    @property
    def domain_MethodPointer(self):
        return self.__domain_MethodPointer

    @domain_MethodPointer.setter
    def domain_MethodPointer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_MethodPointer__domain_MethodPointer", None)
        self.__domain_MethodPointer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_Operation"):
                opp_val = getattr(old_value, "domain_Operation", None)
                if opp_val == self:
                    setattr(old_value, "domain_Operation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_Operation"):
                opp_val = getattr(value, "domain_Operation", None)
                setattr(value, "domain_Operation", self)

class domain_Mappers:

    def __init__(self, uid: str, Mappers: "domain_ApplicationMapper" = None, parent170: set["domain_Mapper"] = None, mapper: "domain_ApplicationMapper" = None, domain_Mappers: "domain_EObject" = None, Mappers177: "domain_Mapper" = None):
        self.uid = uid
        self.Mappers = Mappers
        self.parent170 = parent170 if parent170 is not None else set()
        self.mapper = mapper
        self.domain_Mappers = domain_Mappers
        self.Mappers177 = Mappers177
        
    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def Mappers177(self):
        return self.__Mappers177

    @Mappers177.setter
    def Mappers177(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Mappers__Mappers177", None)
        self.__Mappers177 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mappers176"):
                opp_val = getattr(old_value, "mappers176", None)
                if opp_val == self:
                    setattr(old_value, "mappers176", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mappers176"):
                opp_val = getattr(value, "mappers176", None)
                setattr(value, "mappers176", self)

    @property
    def parent170(self):
        return self.__parent170

    @parent170.setter
    def parent170(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Mappers__parent170", None)
        self.__parent170 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Mapper"):
                    opp_val = getattr(item, "Mapper", None)
                    
                    if opp_val == self:
                        setattr(item, "Mapper", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Mapper"):
                    opp_val = getattr(item, "Mapper", None)
                    
                    setattr(item, "Mapper", self)
                    

    @property
    def domain_Mappers(self):
        return self.__domain_Mappers

    @domain_Mappers.setter
    def domain_Mappers(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Mappers__domain_Mappers", None)
        self.__domain_Mappers = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_EObject174"):
                opp_val = getattr(old_value, "domain_EObject174", None)
                if opp_val == self:
                    setattr(old_value, "domain_EObject174", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_EObject174"):
                opp_val = getattr(value, "domain_EObject174", None)
                setattr(value, "domain_EObject174", self)

    @property
    def Mappers(self):
        return self.__Mappers

    @Mappers.setter
    def Mappers(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Mappers__Mappers", None)
        self.__Mappers = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent122"):
                opp_val = getattr(old_value, "parent122", None)
                if opp_val == self:
                    setattr(old_value, "parent122", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent122"):
                opp_val = getattr(value, "parent122", None)
                setattr(value, "parent122", self)

    @property
    def mapper(self):
        return self.__mapper

    @mapper.setter
    def mapper(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Mappers__mapper", None)
        self.__mapper = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ApplicationMapper172"):
                opp_val = getattr(old_value, "ApplicationMapper172", None)
                if opp_val == self:
                    setattr(old_value, "ApplicationMapper172", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ApplicationMapper172"):
                opp_val = getattr(value, "ApplicationMapper172", None)
                setattr(value, "ApplicationMapper172", self)

class domain_ApplicationMapper:

    def __init__(self, uid: str, name: str, ApplicationMapper: "domain_ApplicationMappers" = None, parent122: "domain_Mappers" = None, mappers: "domain_ApplicationMappers" = None, ApplicationMapper172: "domain_Mappers" = None, domain_ApplicationMapper: "domain_UsingMappers" = None):
        self.uid = uid
        self.name = name
        self.ApplicationMapper = ApplicationMapper
        self.parent122 = parent122
        self.mappers = mappers
        self.ApplicationMapper172 = ApplicationMapper172
        self.domain_ApplicationMapper = domain_ApplicationMapper
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def parent122(self):
        return self.__parent122

    @parent122.setter
    def parent122(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_ApplicationMapper__parent122", None)
        self.__parent122 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Mappers"):
                opp_val = getattr(old_value, "Mappers", None)
                if opp_val == self:
                    setattr(old_value, "Mappers", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Mappers"):
                opp_val = getattr(value, "Mappers", None)
                setattr(value, "Mappers", self)

    @property
    def domain_ApplicationMapper(self):
        return self.__domain_ApplicationMapper

    @domain_ApplicationMapper.setter
    def domain_ApplicationMapper(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_ApplicationMapper__domain_ApplicationMapper", None)
        self.__domain_ApplicationMapper = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_UsingMappers"):
                opp_val = getattr(old_value, "domain_UsingMappers", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_UsingMappers"):
                opp_val = getattr(value, "domain_UsingMappers", None)
                if opp_val is None:
                    setattr(value, "domain_UsingMappers", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ApplicationMapper(self):
        return self.__ApplicationMapper

    @ApplicationMapper.setter
    def ApplicationMapper(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_ApplicationMapper__ApplicationMapper", None)
        self.__ApplicationMapper = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent120"):
                opp_val = getattr(old_value, "parent120", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent120"):
                opp_val = getattr(value, "parent120", None)
                if opp_val is None:
                    setattr(value, "parent120", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ApplicationMapper172(self):
        return self.__ApplicationMapper172

    @ApplicationMapper172.setter
    def ApplicationMapper172(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_ApplicationMapper__ApplicationMapper172", None)
        self.__ApplicationMapper172 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mapper"):
                opp_val = getattr(old_value, "mapper", None)
                if opp_val == self:
                    setattr(old_value, "mapper", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mapper"):
                opp_val = getattr(value, "mapper", None)
                setattr(value, "mapper", self)

    @property
    def mappers(self):
        return self.__mappers

    @mappers.setter
    def mappers(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_ApplicationMapper__mappers", None)
        self.__mappers = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ApplicationMappers124"):
                opp_val = getattr(old_value, "ApplicationMappers124", None)
                if opp_val == self:
                    setattr(old_value, "ApplicationMappers124", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ApplicationMappers124"):
                opp_val = getattr(value, "ApplicationMappers124", None)
                setattr(value, "ApplicationMappers124", self)

class domain_UIPackage:

    def __init__(self, uid: str, UIPackage: "domain_ApplicationUIPackage" = None, uipackage: "domain_ApplicationUIPackage" = None, domain_UIPackage: set["domain_Form"] = None, domain_UIPackage341: "domain_EObject" = None):
        self.uid = uid
        self.UIPackage = UIPackage
        self.uipackage = uipackage
        self.domain_UIPackage = domain_UIPackage if domain_UIPackage is not None else set()
        self.domain_UIPackage341 = domain_UIPackage341
        
    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def uipackage(self):
        return self.__uipackage

    @uipackage.setter
    def uipackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_UIPackage__uipackage", None)
        self.__uipackage = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ApplicationUIPackage338"):
                opp_val = getattr(old_value, "ApplicationUIPackage338", None)
                if opp_val == self:
                    setattr(old_value, "ApplicationUIPackage338", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ApplicationUIPackage338"):
                opp_val = getattr(value, "ApplicationUIPackage338", None)
                setattr(value, "ApplicationUIPackage338", self)

    @property
    def domain_UIPackage341(self):
        return self.__domain_UIPackage341

    @domain_UIPackage341.setter
    def domain_UIPackage341(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_UIPackage__domain_UIPackage341", None)
        self.__domain_UIPackage341 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_EObject342"):
                opp_val = getattr(old_value, "domain_EObject342", None)
                if opp_val == self:
                    setattr(old_value, "domain_EObject342", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_EObject342"):
                opp_val = getattr(value, "domain_EObject342", None)
                setattr(value, "domain_EObject342", self)

    @property
    def UIPackage(self):
        return self.__UIPackage

    @UIPackage.setter
    def UIPackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_UIPackage__UIPackage", None)
        self.__UIPackage = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent108"):
                opp_val = getattr(old_value, "parent108", None)
                if opp_val == self:
                    setattr(old_value, "parent108", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent108"):
                opp_val = getattr(value, "parent108", None)
                setattr(value, "parent108", self)

    @property
    def domain_UIPackage(self):
        return self.__domain_UIPackage

    @domain_UIPackage.setter
    def domain_UIPackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_UIPackage__domain_UIPackage", None)
        self.__domain_UIPackage = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "domain_Form"):
                    opp_val = getattr(item, "domain_Form", None)
                    
                    if opp_val == self:
                        setattr(item, "domain_Form", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "domain_Form"):
                    opp_val = getattr(item, "domain_Form", None)
                    
                    setattr(item, "domain_Form", self)
                    

class domain_Recipes:

    def __init__(self, uid: str, Recipes: "domain_ApplicationRecipe" = None, parent185: "domain_Recipe" = None, domain_Recipes193: "domain_DeploymentSequence" = None, domain_Recipes195: set["domain_ConfigExtension"] = None, domain_Recipes197: "domain_EObject" = None, domain_Recipes: set["domain_Configuration"] = None, domain_Recipes188: set["domain_Infrastructure"] = None, recipes190: "domain_ApplicationRecipe" = None, Recipes218: "domain_Recipe" = None):
        self.uid = uid
        self.Recipes = Recipes
        self.parent185 = parent185
        self.domain_Recipes193 = domain_Recipes193
        self.domain_Recipes195 = domain_Recipes195 if domain_Recipes195 is not None else set()
        self.domain_Recipes197 = domain_Recipes197
        self.domain_Recipes = domain_Recipes if domain_Recipes is not None else set()
        self.domain_Recipes188 = domain_Recipes188 if domain_Recipes188 is not None else set()
        self.recipes190 = recipes190
        self.Recipes218 = Recipes218
        
    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def recipes190(self):
        return self.__recipes190

    @recipes190.setter
    def recipes190(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Recipes__recipes190", None)
        self.__recipes190 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ApplicationRecipe191"):
                opp_val = getattr(old_value, "ApplicationRecipe191", None)
                if opp_val == self:
                    setattr(old_value, "ApplicationRecipe191", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ApplicationRecipe191"):
                opp_val = getattr(value, "ApplicationRecipe191", None)
                setattr(value, "ApplicationRecipe191", self)

    @property
    def domain_Recipes195(self):
        return self.__domain_Recipes195

    @domain_Recipes195.setter
    def domain_Recipes195(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Recipes__domain_Recipes195", None)
        self.__domain_Recipes195 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "domain_ConfigExtension"):
                    opp_val = getattr(item, "domain_ConfigExtension", None)
                    
                    if opp_val == self:
                        setattr(item, "domain_ConfigExtension", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "domain_ConfigExtension"):
                    opp_val = getattr(item, "domain_ConfigExtension", None)
                    
                    setattr(item, "domain_ConfigExtension", self)
                    

    @property
    def domain_Recipes197(self):
        return self.__domain_Recipes197

    @domain_Recipes197.setter
    def domain_Recipes197(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Recipes__domain_Recipes197", None)
        self.__domain_Recipes197 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_EObject198"):
                opp_val = getattr(old_value, "domain_EObject198", None)
                if opp_val == self:
                    setattr(old_value, "domain_EObject198", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_EObject198"):
                opp_val = getattr(value, "domain_EObject198", None)
                setattr(value, "domain_EObject198", self)

    @property
    def parent185(self):
        return self.__parent185

    @parent185.setter
    def parent185(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Recipes__parent185", None)
        self.__parent185 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Recipe"):
                opp_val = getattr(old_value, "Recipe", None)
                if opp_val == self:
                    setattr(old_value, "Recipe", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Recipe"):
                opp_val = getattr(value, "Recipe", None)
                setattr(value, "Recipe", self)

    @property
    def Recipes218(self):
        return self.__Recipes218

    @Recipes218.setter
    def Recipes218(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Recipes__Recipes218", None)
        self.__Recipes218 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "recipe"):
                opp_val = getattr(old_value, "recipe", None)
                if opp_val == self:
                    setattr(old_value, "recipe", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "recipe"):
                opp_val = getattr(value, "recipe", None)
                setattr(value, "recipe", self)

    @property
    def domain_Recipes188(self):
        return self.__domain_Recipes188

    @domain_Recipes188.setter
    def domain_Recipes188(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Recipes__domain_Recipes188", None)
        self.__domain_Recipes188 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "domain_Infrastructure"):
                    opp_val = getattr(item, "domain_Infrastructure", None)
                    
                    if opp_val == self:
                        setattr(item, "domain_Infrastructure", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "domain_Infrastructure"):
                    opp_val = getattr(item, "domain_Infrastructure", None)
                    
                    setattr(item, "domain_Infrastructure", self)
                    

    @property
    def Recipes(self):
        return self.__Recipes

    @Recipes.setter
    def Recipes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Recipes__Recipes", None)
        self.__Recipes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent114"):
                opp_val = getattr(old_value, "parent114", None)
                if opp_val == self:
                    setattr(old_value, "parent114", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent114"):
                opp_val = getattr(value, "parent114", None)
                setattr(value, "parent114", self)

    @property
    def domain_Recipes(self):
        return self.__domain_Recipes

    @domain_Recipes.setter
    def domain_Recipes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Recipes__domain_Recipes", None)
        self.__domain_Recipes = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "domain_Configuration"):
                    opp_val = getattr(item, "domain_Configuration", None)
                    
                    if opp_val == self:
                        setattr(item, "domain_Configuration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "domain_Configuration"):
                    opp_val = getattr(item, "domain_Configuration", None)
                    
                    setattr(item, "domain_Configuration", self)
                    

    @property
    def domain_Recipes193(self):
        return self.__domain_Recipes193

    @domain_Recipes193.setter
    def domain_Recipes193(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Recipes__domain_Recipes193", None)
        self.__domain_Recipes193 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_DeploymentSequence"):
                opp_val = getattr(old_value, "domain_DeploymentSequence", None)
                if opp_val == self:
                    setattr(old_value, "domain_DeploymentSequence", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_DeploymentSequence"):
                opp_val = getattr(value, "domain_DeploymentSequence", None)
                setattr(value, "domain_DeploymentSequence", self)

class domain_ApplicationRecipe:

    def __init__(self, uid: str, name: str, ApplicationRecipe: "domain_ApplicationRecipes" = None, parent114: "domain_Recipes" = None, recipes: "domain_ApplicationRecipes" = None, ApplicationRecipe191: "domain_Recipes" = None):
        self.uid = uid
        self.name = name
        self.ApplicationRecipe = ApplicationRecipe
        self.parent114 = parent114
        self.recipes = recipes
        self.ApplicationRecipe191 = ApplicationRecipe191
        
    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ApplicationRecipe191(self):
        return self.__ApplicationRecipe191

    @ApplicationRecipe191.setter
    def ApplicationRecipe191(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_ApplicationRecipe__ApplicationRecipe191", None)
        self.__ApplicationRecipe191 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "recipes190"):
                opp_val = getattr(old_value, "recipes190", None)
                if opp_val == self:
                    setattr(old_value, "recipes190", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "recipes190"):
                opp_val = getattr(value, "recipes190", None)
                setattr(value, "recipes190", self)

    @property
    def ApplicationRecipe(self):
        return self.__ApplicationRecipe

    @ApplicationRecipe.setter
    def ApplicationRecipe(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_ApplicationRecipe__ApplicationRecipe", None)
        self.__ApplicationRecipe = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent112"):
                opp_val = getattr(old_value, "parent112", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent112"):
                opp_val = getattr(value, "parent112", None)
                if opp_val is None:
                    setattr(value, "parent112", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def parent114(self):
        return self.__parent114

    @parent114.setter
    def parent114(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_ApplicationRecipe__parent114", None)
        self.__parent114 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Recipes"):
                opp_val = getattr(old_value, "Recipes", None)
                if opp_val == self:
                    setattr(old_value, "Recipes", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Recipes"):
                opp_val = getattr(value, "Recipes", None)
                setattr(value, "Recipes", self)

    @property
    def recipes(self):
        return self.__recipes

    @recipes.setter
    def recipes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_ApplicationRecipe__recipes", None)
        self.__recipes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ApplicationRecipes116"):
                opp_val = getattr(old_value, "ApplicationRecipes116", None)
                if opp_val == self:
                    setattr(old_value, "ApplicationRecipes116", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ApplicationRecipes116"):
                opp_val = getattr(value, "ApplicationRecipes116", None)
                setattr(value, "ApplicationRecipes116", self)

class domain_Styles:

    def __init__(self, uid: str, Styles: "domain_StylesPackage" = None, styles: "domain_StylesPackage" = None, domain_Styles: set["domain_StyleLibrary"] = None, domain_Styles165: "domain_EObject" = None):
        self.uid = uid
        self.Styles = Styles
        self.styles = styles
        self.domain_Styles = domain_Styles if domain_Styles is not None else set()
        self.domain_Styles165 = domain_Styles165
        
    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def Styles(self):
        return self.__Styles

    @Styles.setter
    def Styles(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Styles__Styles", None)
        self.__Styles = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent100"):
                opp_val = getattr(old_value, "parent100", None)
                if opp_val == self:
                    setattr(old_value, "parent100", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent100"):
                opp_val = getattr(value, "parent100", None)
                setattr(value, "parent100", self)

    @property
    def styles(self):
        return self.__styles

    @styles.setter
    def styles(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Styles__styles", None)
        self.__styles = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StylesPackage162"):
                opp_val = getattr(old_value, "StylesPackage162", None)
                if opp_val == self:
                    setattr(old_value, "StylesPackage162", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StylesPackage162"):
                opp_val = getattr(value, "StylesPackage162", None)
                setattr(value, "StylesPackage162", self)

    @property
    def domain_Styles165(self):
        return self.__domain_Styles165

    @domain_Styles165.setter
    def domain_Styles165(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Styles__domain_Styles165", None)
        self.__domain_Styles165 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_EObject166"):
                opp_val = getattr(old_value, "domain_EObject166", None)
                if opp_val == self:
                    setattr(old_value, "domain_EObject166", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_EObject166"):
                opp_val = getattr(value, "domain_EObject166", None)
                setattr(value, "domain_EObject166", self)

    @property
    def domain_Styles(self):
        return self.__domain_Styles

    @domain_Styles.setter
    def domain_Styles(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Styles__domain_Styles", None)
        self.__domain_Styles = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "domain_StyleLibrary"):
                    opp_val = getattr(item, "domain_StyleLibrary", None)
                    
                    if opp_val == self:
                        setattr(item, "domain_StyleLibrary", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "domain_StyleLibrary"):
                    opp_val = getattr(item, "domain_StyleLibrary", None)
                    
                    setattr(item, "domain_StyleLibrary", self)
                    

class domain_ApplicationUIPackage:

    def __init__(self, uid: str, name: str, ApplicationUIPackage: "domain_ApplicationUILayer" = None, applicationUIPackages: "domain_ApplicationUILayer" = None, parent108: "domain_UIPackage" = None, ApplicationUIPackage338: "domain_UIPackage" = None):
        self.uid = uid
        self.name = name
        self.ApplicationUIPackage = ApplicationUIPackage
        self.applicationUIPackages = applicationUIPackages
        self.parent108 = parent108
        self.ApplicationUIPackage338 = ApplicationUIPackage338
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def applicationUIPackages(self):
        return self.__applicationUIPackages

    @applicationUIPackages.setter
    def applicationUIPackages(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_ApplicationUIPackage__applicationUIPackages", None)
        self.__applicationUIPackages = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ApplicationUILayer106"):
                opp_val = getattr(old_value, "ApplicationUILayer106", None)
                if opp_val == self:
                    setattr(old_value, "ApplicationUILayer106", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ApplicationUILayer106"):
                opp_val = getattr(value, "ApplicationUILayer106", None)
                setattr(value, "ApplicationUILayer106", self)

    @property
    def ApplicationUIPackage338(self):
        return self.__ApplicationUIPackage338

    @ApplicationUIPackage338.setter
    def ApplicationUIPackage338(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_ApplicationUIPackage__ApplicationUIPackage338", None)
        self.__ApplicationUIPackage338 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uipackage"):
                opp_val = getattr(old_value, "uipackage", None)
                if opp_val == self:
                    setattr(old_value, "uipackage", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uipackage"):
                opp_val = getattr(value, "uipackage", None)
                setattr(value, "uipackage", self)

    @property
    def ApplicationUIPackage(self):
        return self.__ApplicationUIPackage

    @ApplicationUIPackage.setter
    def ApplicationUIPackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_ApplicationUIPackage__ApplicationUIPackage", None)
        self.__ApplicationUIPackage = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent104"):
                opp_val = getattr(old_value, "parent104", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent104"):
                opp_val = getattr(value, "parent104", None)
                if opp_val is None:
                    setattr(value, "parent104", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def parent108(self):
        return self.__parent108

    @parent108.setter
    def parent108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_ApplicationUIPackage__parent108", None)
        self.__parent108 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UIPackage"):
                opp_val = getattr(old_value, "UIPackage", None)
                if opp_val == self:
                    setattr(old_value, "UIPackage", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UIPackage"):
                opp_val = getattr(value, "UIPackage", None)
                setattr(value, "UIPackage", self)

class domain_Roles:

    def __init__(self, uid: str, Roles: "domain_ApplicationRole" = None, roles: "domain_ApplicationRole" = None, domain_Roles: set["domain_Role"] = None, domain_Roles151: set["domain_Group"] = None, domain_Roles153: "domain_EObject" = None):
        self.uid = uid
        self.Roles = Roles
        self.roles = roles
        self.domain_Roles = domain_Roles if domain_Roles is not None else set()
        self.domain_Roles151 = domain_Roles151 if domain_Roles151 is not None else set()
        self.domain_Roles153 = domain_Roles153
        
    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def domain_Roles151(self):
        return self.__domain_Roles151

    @domain_Roles151.setter
    def domain_Roles151(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Roles__domain_Roles151", None)
        self.__domain_Roles151 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "domain_Group"):
                    opp_val = getattr(item, "domain_Group", None)
                    
                    if opp_val == self:
                        setattr(item, "domain_Group", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "domain_Group"):
                    opp_val = getattr(item, "domain_Group", None)
                    
                    setattr(item, "domain_Group", self)
                    

    @property
    def domain_Roles(self):
        return self.__domain_Roles

    @domain_Roles.setter
    def domain_Roles(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Roles__domain_Roles", None)
        self.__domain_Roles = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "domain_Role149"):
                    opp_val = getattr(item, "domain_Role149", None)
                    
                    if opp_val == self:
                        setattr(item, "domain_Role149", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "domain_Role149"):
                    opp_val = getattr(item, "domain_Role149", None)
                    
                    setattr(item, "domain_Role149", self)
                    

    @property
    def roles(self):
        return self.__roles

    @roles.setter
    def roles(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Roles__roles", None)
        self.__roles = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ApplicationRole147"):
                opp_val = getattr(old_value, "ApplicationRole147", None)
                if opp_val == self:
                    setattr(old_value, "ApplicationRole147", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ApplicationRole147"):
                opp_val = getattr(value, "ApplicationRole147", None)
                setattr(value, "ApplicationRole147", self)

    @property
    def domain_Roles153(self):
        return self.__domain_Roles153

    @domain_Roles153.setter
    def domain_Roles153(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Roles__domain_Roles153", None)
        self.__domain_Roles153 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_EObject154"):
                opp_val = getattr(old_value, "domain_EObject154", None)
                if opp_val == self:
                    setattr(old_value, "domain_EObject154", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_EObject154"):
                opp_val = getattr(value, "domain_EObject154", None)
                setattr(value, "domain_EObject154", self)

    @property
    def Roles(self):
        return self.__Roles

    @Roles.setter
    def Roles(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Roles__Roles", None)
        self.__Roles = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent92"):
                opp_val = getattr(old_value, "parent92", None)
                if opp_val == self:
                    setattr(old_value, "parent92", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent92"):
                opp_val = getattr(value, "parent92", None)
                setattr(value, "parent92", self)

class domain_StylesPackage:

    def __init__(self, uid: str, name: str, StylesPackage: "domain_ApplicationStyle" = None, stylesPackage: "domain_ApplicationStyle" = None, parent100: "domain_Styles" = None, StylesPackage162: "domain_Styles" = None, domain_StylesPackage: "domain_CSSMapper" = None):
        self.uid = uid
        self.name = name
        self.StylesPackage = StylesPackage
        self.stylesPackage = stylesPackage
        self.parent100 = parent100
        self.StylesPackage162 = StylesPackage162
        self.domain_StylesPackage = domain_StylesPackage
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def parent100(self):
        return self.__parent100

    @parent100.setter
    def parent100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_StylesPackage__parent100", None)
        self.__parent100 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Styles"):
                opp_val = getattr(old_value, "Styles", None)
                if opp_val == self:
                    setattr(old_value, "Styles", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Styles"):
                opp_val = getattr(value, "Styles", None)
                setattr(value, "Styles", self)

    @property
    def stylesPackage(self):
        return self.__stylesPackage

    @stylesPackage.setter
    def stylesPackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_StylesPackage__stylesPackage", None)
        self.__stylesPackage = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ApplicationStyle98"):
                opp_val = getattr(old_value, "ApplicationStyle98", None)
                if opp_val == self:
                    setattr(old_value, "ApplicationStyle98", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ApplicationStyle98"):
                opp_val = getattr(value, "ApplicationStyle98", None)
                setattr(value, "ApplicationStyle98", self)

    @property
    def domain_StylesPackage(self):
        return self.__domain_StylesPackage

    @domain_StylesPackage.setter
    def domain_StylesPackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_StylesPackage__domain_StylesPackage", None)
        self.__domain_StylesPackage = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_CSSMapper"):
                opp_val = getattr(old_value, "domain_CSSMapper", None)
                if opp_val == self:
                    setattr(old_value, "domain_CSSMapper", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_CSSMapper"):
                opp_val = getattr(value, "domain_CSSMapper", None)
                setattr(value, "domain_CSSMapper", self)

    @property
    def StylesPackage162(self):
        return self.__StylesPackage162

    @StylesPackage162.setter
    def StylesPackage162(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_StylesPackage__StylesPackage162", None)
        self.__StylesPackage162 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "styles"):
                opp_val = getattr(old_value, "styles", None)
                if opp_val == self:
                    setattr(old_value, "styles", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "styles"):
                opp_val = getattr(value, "styles", None)
                setattr(value, "styles", self)

    @property
    def StylesPackage(self):
        return self.__StylesPackage

    @StylesPackage.setter
    def StylesPackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_StylesPackage__StylesPackage", None)
        self.__StylesPackage = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent96"):
                opp_val = getattr(old_value, "parent96", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent96"):
                opp_val = getattr(value, "parent96", None)
                if opp_val is None:
                    setattr(value, "parent96", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class domain_ApplicationMessages:

    def __init__(self, uid: str, name: str, applicationMessages: "domain_Application" = None, parent88: "domain_Messages" = None, ApplicationMessages: "domain_Application" = None, ApplicationMessages127: "domain_Messages" = None):
        self.uid = uid
        self.name = name
        self.applicationMessages = applicationMessages
        self.parent88 = parent88
        self.ApplicationMessages = ApplicationMessages
        self.ApplicationMessages127 = ApplicationMessages127
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def parent88(self):
        return self.__parent88

    @parent88.setter
    def parent88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_ApplicationMessages__parent88", None)
        self.__parent88 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Messages"):
                opp_val = getattr(old_value, "Messages", None)
                if opp_val == self:
                    setattr(old_value, "Messages", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Messages"):
                opp_val = getattr(value, "Messages", None)
                setattr(value, "Messages", self)

    @property
    def applicationMessages(self):
        return self.__applicationMessages

    @applicationMessages.setter
    def applicationMessages(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_ApplicationMessages__applicationMessages", None)
        self.__applicationMessages = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Application86"):
                opp_val = getattr(old_value, "Application86", None)
                if opp_val == self:
                    setattr(old_value, "Application86", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Application86"):
                opp_val = getattr(value, "Application86", None)
                setattr(value, "Application86", self)

    @property
    def ApplicationMessages127(self):
        return self.__ApplicationMessages127

    @ApplicationMessages127.setter
    def ApplicationMessages127(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_ApplicationMessages__ApplicationMessages127", None)
        self.__ApplicationMessages127 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "messages"):
                opp_val = getattr(old_value, "messages", None)
                if opp_val == self:
                    setattr(old_value, "messages", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "messages"):
                opp_val = getattr(value, "messages", None)
                setattr(value, "messages", self)

    @property
    def ApplicationMessages(self):
        return self.__ApplicationMessages

    @ApplicationMessages.setter
    def ApplicationMessages(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_ApplicationMessages__ApplicationMessages", None)
        self.__ApplicationMessages = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent80"):
                opp_val = getattr(old_value, "parent80", None)
                if opp_val == self:
                    setattr(old_value, "parent80", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent80"):
                opp_val = getattr(value, "parent80", None)
                setattr(value, "parent80", self)

class domain_ApplicationRole:

    def __init__(self, uid: str, name: str, ApplicationRole: "domain_Application" = None, parent92: "domain_Roles" = None, applicationRole: "domain_Application" = None, ApplicationRole147: "domain_Roles" = None):
        self.uid = uid
        self.name = name
        self.ApplicationRole = ApplicationRole
        self.parent92 = parent92
        self.applicationRole = applicationRole
        self.ApplicationRole147 = ApplicationRole147
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def applicationRole(self):
        return self.__applicationRole

    @applicationRole.setter
    def applicationRole(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_ApplicationRole__applicationRole", None)
        self.__applicationRole = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Application90"):
                opp_val = getattr(old_value, "Application90", None)
                if opp_val == self:
                    setattr(old_value, "Application90", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Application90"):
                opp_val = getattr(value, "Application90", None)
                setattr(value, "Application90", self)

    @property
    def parent92(self):
        return self.__parent92

    @parent92.setter
    def parent92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_ApplicationRole__parent92", None)
        self.__parent92 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Roles"):
                opp_val = getattr(old_value, "Roles", None)
                if opp_val == self:
                    setattr(old_value, "Roles", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Roles"):
                opp_val = getattr(value, "Roles", None)
                setattr(value, "Roles", self)

    @property
    def ApplicationRole147(self):
        return self.__ApplicationRole147

    @ApplicationRole147.setter
    def ApplicationRole147(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_ApplicationRole__ApplicationRole147", None)
        self.__ApplicationRole147 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "roles"):
                opp_val = getattr(old_value, "roles", None)
                if opp_val == self:
                    setattr(old_value, "roles", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "roles"):
                opp_val = getattr(value, "roles", None)
                setattr(value, "roles", self)

    @property
    def ApplicationRole(self):
        return self.__ApplicationRole

    @ApplicationRole.setter
    def ApplicationRole(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_ApplicationRole__ApplicationRole", None)
        self.__ApplicationRole = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent78"):
                opp_val = getattr(old_value, "parent78", None)
                if opp_val == self:
                    setattr(old_value, "parent78", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent78"):
                opp_val = getattr(value, "parent78", None)
                setattr(value, "parent78", self)

class domain_Messages:

    def __init__(self, uid: str, Messages: "domain_ApplicationMessages" = None, messages: "domain_ApplicationMessages" = None, domain_Messages: set["domain_MessageLibrary"] = None, domain_Messages130: set["domain_Language"] = None, domain_Messages132: "domain_EObject" = None):
        self.uid = uid
        self.Messages = Messages
        self.messages = messages
        self.domain_Messages = domain_Messages if domain_Messages is not None else set()
        self.domain_Messages130 = domain_Messages130 if domain_Messages130 is not None else set()
        self.domain_Messages132 = domain_Messages132
        
    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def Messages(self):
        return self.__Messages

    @Messages.setter
    def Messages(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Messages__Messages", None)
        self.__Messages = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent88"):
                opp_val = getattr(old_value, "parent88", None)
                if opp_val == self:
                    setattr(old_value, "parent88", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent88"):
                opp_val = getattr(value, "parent88", None)
                setattr(value, "parent88", self)

    @property
    def domain_Messages132(self):
        return self.__domain_Messages132

    @domain_Messages132.setter
    def domain_Messages132(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Messages__domain_Messages132", None)
        self.__domain_Messages132 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_EObject133"):
                opp_val = getattr(old_value, "domain_EObject133", None)
                if opp_val == self:
                    setattr(old_value, "domain_EObject133", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_EObject133"):
                opp_val = getattr(value, "domain_EObject133", None)
                setattr(value, "domain_EObject133", self)

    @property
    def messages(self):
        return self.__messages

    @messages.setter
    def messages(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Messages__messages", None)
        self.__messages = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ApplicationMessages127"):
                opp_val = getattr(old_value, "ApplicationMessages127", None)
                if opp_val == self:
                    setattr(old_value, "ApplicationMessages127", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ApplicationMessages127"):
                opp_val = getattr(value, "ApplicationMessages127", None)
                setattr(value, "ApplicationMessages127", self)

    @property
    def domain_Messages130(self):
        return self.__domain_Messages130

    @domain_Messages130.setter
    def domain_Messages130(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Messages__domain_Messages130", None)
        self.__domain_Messages130 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "domain_Language"):
                    opp_val = getattr(item, "domain_Language", None)
                    
                    if opp_val == self:
                        setattr(item, "domain_Language", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "domain_Language"):
                    opp_val = getattr(item, "domain_Language", None)
                    
                    setattr(item, "domain_Language", self)
                    

    @property
    def domain_Messages(self):
        return self.__domain_Messages

    @domain_Messages.setter
    def domain_Messages(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Messages__domain_Messages", None)
        self.__domain_Messages = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "domain_MessageLibrary"):
                    opp_val = getattr(item, "domain_MessageLibrary", None)
                    
                    if opp_val == self:
                        setattr(item, "domain_MessageLibrary", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "domain_MessageLibrary"):
                    opp_val = getattr(item, "domain_MessageLibrary", None)
                    
                    setattr(item, "domain_MessageLibrary", self)
                    

class domain_Option:

    def __init__(self, uid: str, value: str, options: "domain_Specifier" = None, Option: "domain_Specifier" = None, domain_Option: "domain_MappingSpecifier" = None):
        self.uid = uid
        self.value = value
        self.options = options
        self.Option = Option
        self.domain_Option = domain_Option
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def Option(self):
        return self.__Option

    @Option.setter
    def Option(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Option__Option", None)
        self.__Option = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent64"):
                opp_val = getattr(old_value, "parent64", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent64"):
                opp_val = getattr(value, "parent64", None)
                if opp_val is None:
                    setattr(value, "parent64", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def domain_Option(self):
        return self.__domain_Option

    @domain_Option.setter
    def domain_Option(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Option__domain_Option", None)
        self.__domain_Option = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_MappingSpecifier264"):
                opp_val = getattr(old_value, "domain_MappingSpecifier264", None)
                if opp_val == self:
                    setattr(old_value, "domain_MappingSpecifier264", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_MappingSpecifier264"):
                opp_val = getattr(value, "domain_MappingSpecifier264", None)
                setattr(value, "domain_MappingSpecifier264", self)

    @property
    def options(self):
        return self.__options

    @options.setter
    def options(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Option__options", None)
        self.__options = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Specifier66"):
                opp_val = getattr(old_value, "Specifier66", None)
                if opp_val == self:
                    setattr(old_value, "Specifier66", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Specifier66"):
                opp_val = getattr(value, "Specifier66", None)
                setattr(value, "Specifier66", self)

class domain_ApplicationInfrastructureLayer:

    def __init__(self, uid: str, name: str, ApplicationInfrastructureLayer: "domain_Application" = None, applicationInfrastructureLayer: "domain_Application" = None, parent557: "domain_EnterpriseInfrastructure" = None, ApplicationInfrastructureLayer559: "domain_EnterpriseInfrastructure" = None):
        self.uid = uid
        self.name = name
        self.ApplicationInfrastructureLayer = ApplicationInfrastructureLayer
        self.applicationInfrastructureLayer = applicationInfrastructureLayer
        self.parent557 = parent557
        self.ApplicationInfrastructureLayer559 = ApplicationInfrastructureLayer559
        
    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ApplicationInfrastructureLayer559(self):
        return self.__ApplicationInfrastructureLayer559

    @ApplicationInfrastructureLayer559.setter
    def ApplicationInfrastructureLayer559(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_ApplicationInfrastructureLayer__ApplicationInfrastructureLayer559", None)
        self.__ApplicationInfrastructureLayer559 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "infarastructure"):
                opp_val = getattr(old_value, "infarastructure", None)
                if opp_val == self:
                    setattr(old_value, "infarastructure", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "infarastructure"):
                opp_val = getattr(value, "infarastructure", None)
                setattr(value, "infarastructure", self)

    @property
    def parent557(self):
        return self.__parent557

    @parent557.setter
    def parent557(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_ApplicationInfrastructureLayer__parent557", None)
        self.__parent557 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EnterpriseInfrastructure"):
                opp_val = getattr(old_value, "EnterpriseInfrastructure", None)
                if opp_val == self:
                    setattr(old_value, "EnterpriseInfrastructure", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EnterpriseInfrastructure"):
                opp_val = getattr(value, "EnterpriseInfrastructure", None)
                setattr(value, "EnterpriseInfrastructure", self)

    @property
    def applicationInfrastructureLayer(self):
        return self.__applicationInfrastructureLayer

    @applicationInfrastructureLayer.setter
    def applicationInfrastructureLayer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_ApplicationInfrastructureLayer__applicationInfrastructureLayer", None)
        self.__applicationInfrastructureLayer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Application555"):
                opp_val = getattr(old_value, "Application555", None)
                if opp_val == self:
                    setattr(old_value, "Application555", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Application555"):
                opp_val = getattr(value, "Application555", None)
                setattr(value, "Application555", self)

    @property
    def ApplicationInfrastructureLayer(self):
        return self.__ApplicationInfrastructureLayer

    @ApplicationInfrastructureLayer.setter
    def ApplicationInfrastructureLayer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_ApplicationInfrastructureLayer__ApplicationInfrastructureLayer", None)
        self.__ApplicationInfrastructureLayer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent74"):
                opp_val = getattr(old_value, "parent74", None)
                if opp_val == self:
                    setattr(old_value, "parent74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent74"):
                opp_val = getattr(value, "parent74", None)
                setattr(value, "parent74", self)

class domain_QueryParameter:

    def __init__(self, uid: str, name: str, QueryParameter: "domain_ModelQuery" = None, parameters: "domain_ModelQuery" = None, domain_QueryParameter: "domain_QueryVariable" = None):
        self.uid = uid
        self.name = name
        self.QueryParameter = QueryParameter
        self.parameters = parameters
        self.domain_QueryParameter = domain_QueryParameter
        
    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def QueryParameter(self):
        return self.__QueryParameter

    @QueryParameter.setter
    def QueryParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_QueryParameter__QueryParameter", None)
        self.__QueryParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent58"):
                opp_val = getattr(old_value, "parent58", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent58"):
                opp_val = getattr(value, "parent58", None)
                if opp_val is None:
                    setattr(value, "parent58", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def parameters(self):
        return self.__parameters

    @parameters.setter
    def parameters(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_QueryParameter__parameters", None)
        self.__parameters = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ModelQuery60"):
                opp_val = getattr(old_value, "ModelQuery60", None)
                if opp_val == self:
                    setattr(old_value, "ModelQuery60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ModelQuery60"):
                opp_val = getattr(value, "ModelQuery60", None)
                setattr(value, "ModelQuery60", self)

    @property
    def domain_QueryParameter(self):
        return self.__domain_QueryParameter

    @domain_QueryParameter.setter
    def domain_QueryParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_QueryParameter__domain_QueryParameter", None)
        self.__domain_QueryParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_QueryVariable273"):
                opp_val = getattr(old_value, "domain_QueryVariable273", None)
                if opp_val == self:
                    setattr(old_value, "domain_QueryVariable273", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_QueryVariable273"):
                opp_val = getattr(value, "domain_QueryVariable273", None)
                setattr(value, "domain_QueryVariable273", self)

class domain_Specifier:

    def __init__(self, uid: str, name: str, Specifier: "domain_Artifact" = None, Specifier66: "domain_Option" = None, specifiers: "domain_Artifact" = None, parent64: set["domain_Option"] = None, domain_Specifier: "domain_MappingSpecifier" = None):
        self.uid = uid
        self.name = name
        self.Specifier = Specifier
        self.Specifier66 = Specifier66
        self.specifiers = specifiers
        self.parent64 = parent64 if parent64 is not None else set()
        self.domain_Specifier = domain_Specifier
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def parent64(self):
        return self.__parent64

    @parent64.setter
    def parent64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Specifier__parent64", None)
        self.__parent64 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Option"):
                    opp_val = getattr(item, "Option", None)
                    
                    if opp_val == self:
                        setattr(item, "Option", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Option"):
                    opp_val = getattr(item, "Option", None)
                    
                    setattr(item, "Option", self)
                    

    @property
    def domain_Specifier(self):
        return self.__domain_Specifier

    @domain_Specifier.setter
    def domain_Specifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Specifier__domain_Specifier", None)
        self.__domain_Specifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_MappingSpecifier262"):
                opp_val = getattr(old_value, "domain_MappingSpecifier262", None)
                if opp_val == self:
                    setattr(old_value, "domain_MappingSpecifier262", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_MappingSpecifier262"):
                opp_val = getattr(value, "domain_MappingSpecifier262", None)
                setattr(value, "domain_MappingSpecifier262", self)

    @property
    def specifiers(self):
        return self.__specifiers

    @specifiers.setter
    def specifiers(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Specifier__specifiers", None)
        self.__specifiers = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Artifact62"):
                opp_val = getattr(old_value, "Artifact62", None)
                if opp_val == self:
                    setattr(old_value, "Artifact62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Artifact62"):
                opp_val = getattr(value, "Artifact62", None)
                setattr(value, "Artifact62", self)

    @property
    def Specifier(self):
        return self.__Specifier

    @Specifier.setter
    def Specifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Specifier__Specifier", None)
        self.__Specifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent48"):
                opp_val = getattr(old_value, "parent48", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent48"):
                opp_val = getattr(value, "parent48", None)
                if opp_val is None:
                    setattr(value, "parent48", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Specifier66(self):
        return self.__Specifier66

    @Specifier66.setter
    def Specifier66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Specifier__Specifier66", None)
        self.__Specifier66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "options"):
                opp_val = getattr(old_value, "options", None)
                if opp_val == self:
                    setattr(old_value, "options", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "options"):
                opp_val = getattr(value, "options", None)
                setattr(value, "options", self)

class domain_ModelQuery:

    def __init__(self, uid: str, name: str, query: str, ModelQuery: "domain_Artifact" = None, modelQuery: "domain_Artifact" = None, parent58: set["domain_QueryParameter"] = None, ModelQuery60: "domain_QueryParameter" = None, domain_ModelQuery: "domain_Query" = None, domain_ModelQuery269: "domain_Query" = None):
        self.uid = uid
        self.name = name
        self.query = query
        self.ModelQuery = ModelQuery
        self.modelQuery = modelQuery
        self.parent58 = parent58 if parent58 is not None else set()
        self.ModelQuery60 = ModelQuery60
        self.domain_ModelQuery = domain_ModelQuery
        self.domain_ModelQuery269 = domain_ModelQuery269
        
    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def query(self) -> str:
        return self.__query

    @query.setter
    def query(self, query: str):
        self.__query = query

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ModelQuery(self):
        return self.__ModelQuery

    @ModelQuery.setter
    def ModelQuery(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_ModelQuery__ModelQuery", None)
        self.__ModelQuery = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent46"):
                opp_val = getattr(old_value, "parent46", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent46"):
                opp_val = getattr(value, "parent46", None)
                if opp_val is None:
                    setattr(value, "parent46", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def parent58(self):
        return self.__parent58

    @parent58.setter
    def parent58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_ModelQuery__parent58", None)
        self.__parent58 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "QueryParameter"):
                    opp_val = getattr(item, "QueryParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "QueryParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "QueryParameter"):
                    opp_val = getattr(item, "QueryParameter", None)
                    
                    setattr(item, "QueryParameter", self)
                    

    @property
    def domain_ModelQuery(self):
        return self.__domain_ModelQuery

    @domain_ModelQuery.setter
    def domain_ModelQuery(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_ModelQuery__domain_ModelQuery", None)
        self.__domain_ModelQuery = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_Query266"):
                opp_val = getattr(old_value, "domain_Query266", None)
                if opp_val == self:
                    setattr(old_value, "domain_Query266", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_Query266"):
                opp_val = getattr(value, "domain_Query266", None)
                setattr(value, "domain_Query266", self)

    @property
    def modelQuery(self):
        return self.__modelQuery

    @modelQuery.setter
    def modelQuery(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_ModelQuery__modelQuery", None)
        self.__modelQuery = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Artifact56"):
                opp_val = getattr(old_value, "Artifact56", None)
                if opp_val == self:
                    setattr(old_value, "Artifact56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Artifact56"):
                opp_val = getattr(value, "Artifact56", None)
                setattr(value, "Artifact56", self)

    @property
    def domain_ModelQuery269(self):
        return self.__domain_ModelQuery269

    @domain_ModelQuery269.setter
    def domain_ModelQuery269(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_ModelQuery__domain_ModelQuery269", None)
        self.__domain_ModelQuery269 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_Query268"):
                opp_val = getattr(old_value, "domain_Query268", None)
                if opp_val == self:
                    setattr(old_value, "domain_Query268", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_Query268"):
                opp_val = getattr(value, "domain_Query268", None)
                setattr(value, "domain_Query268", self)

    @property
    def ModelQuery60(self):
        return self.__ModelQuery60

    @ModelQuery60.setter
    def ModelQuery60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_ModelQuery__ModelQuery60", None)
        self.__ModelQuery60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parameters"):
                opp_val = getattr(old_value, "parameters", None)
                if opp_val == self:
                    setattr(old_value, "parameters", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parameters"):
                opp_val = getattr(value, "parameters", None)
                setattr(value, "parameters", self)

class domain_ConfigHash:

    def __init__(self, uid: str, name: str, ConfigHash: "domain_Artifact" = None, configHashes: "domain_Artifact" = None, domain_ConfigHash: "domain_HashProperty" = None):
        self.uid = uid
        self.name = name
        self.ConfigHash = ConfigHash
        self.configHashes = configHashes
        self.domain_ConfigHash = domain_ConfigHash
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def configHashes(self):
        return self.__configHashes

    @configHashes.setter
    def configHashes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_ConfigHash__configHashes", None)
        self.__configHashes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Artifact54"):
                opp_val = getattr(old_value, "Artifact54", None)
                if opp_val == self:
                    setattr(old_value, "Artifact54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Artifact54"):
                opp_val = getattr(value, "Artifact54", None)
                setattr(value, "Artifact54", self)

    @property
    def ConfigHash(self):
        return self.__ConfigHash

    @ConfigHash.setter
    def ConfigHash(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_ConfigHash__ConfigHash", None)
        self.__ConfigHash = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent44"):
                opp_val = getattr(old_value, "parent44", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent44"):
                opp_val = getattr(value, "parent44", None)
                if opp_val is None:
                    setattr(value, "parent44", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def domain_ConfigHash(self):
        return self.__domain_ConfigHash

    @domain_ConfigHash.setter
    def domain_ConfigHash(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_ConfigHash__domain_ConfigHash", None)
        self.__domain_ConfigHash = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_HashProperty258"):
                opp_val = getattr(old_value, "domain_HashProperty258", None)
                if opp_val == self:
                    setattr(old_value, "domain_HashProperty258", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_HashProperty258"):
                opp_val = getattr(value, "domain_HashProperty258", None)
                setattr(value, "domain_HashProperty258", self)

class domain_ConfigVariable:

    def __init__(self, uid: str, name: str, ConfigVariable: "domain_Artifact" = None, configVariables: "domain_Artifact" = None, domain_ConfigVariable: "domain_Property" = None):
        self.uid = uid
        self.name = name
        self.ConfigVariable = ConfigVariable
        self.configVariables = configVariables
        self.domain_ConfigVariable = domain_ConfigVariable
        
    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ConfigVariable(self):
        return self.__ConfigVariable

    @ConfigVariable.setter
    def ConfigVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_ConfigVariable__ConfigVariable", None)
        self.__ConfigVariable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent42"):
                opp_val = getattr(old_value, "parent42", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent42"):
                opp_val = getattr(value, "parent42", None)
                if opp_val is None:
                    setattr(value, "parent42", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def domain_ConfigVariable(self):
        return self.__domain_ConfigVariable

    @domain_ConfigVariable.setter
    def domain_ConfigVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_ConfigVariable__domain_ConfigVariable", None)
        self.__domain_ConfigVariable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_Property256"):
                opp_val = getattr(old_value, "domain_Property256", None)
                if opp_val == self:
                    setattr(old_value, "domain_Property256", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_Property256"):
                opp_val = getattr(value, "domain_Property256", None)
                setattr(value, "domain_Property256", self)

    @property
    def configVariables(self):
        return self.__configVariables

    @configVariables.setter
    def configVariables(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_ConfigVariable__configVariables", None)
        self.__configVariables = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Artifact52"):
                opp_val = getattr(old_value, "Artifact52", None)
                if opp_val == self:
                    setattr(old_value, "Artifact52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Artifact52"):
                opp_val = getattr(value, "Artifact52", None)
                setattr(value, "Artifact52", self)

class DomainArtifact:

    pass
class domain_JPAService(DomainArtifact):

    pass
class domain_ORMEntity(DomainArtifact):

    pass
class domain_Artifact:

    def __init__(self, name: str, description: str, uid: str, template: str, Artifact: "domain_Artifacts" = None, artifacts: "domain_Artifacts" = None, parent42: set["domain_ConfigVariable"] = None, parent44: set["domain_ConfigHash"] = None, parent46: set["domain_ModelQuery"] = None, parent48: set["domain_Specifier"] = None, Artifact52: "domain_ConfigVariable" = None, domain_Artifact: set["domain_GenerationHint"] = None, Artifact56: "domain_ModelQuery" = None, Artifact54: "domain_ConfigHash" = None, Artifact62: "domain_Specifier" = None, domain_Artifact277: "domain_ArtifactRef" = None):
        self.name = name
        self.description = description
        self.uid = uid
        self.template = template
        self.Artifact = Artifact
        self.artifacts = artifacts
        self.parent42 = parent42 if parent42 is not None else set()
        self.parent44 = parent44 if parent44 is not None else set()
        self.parent46 = parent46 if parent46 is not None else set()
        self.parent48 = parent48 if parent48 is not None else set()
        self.Artifact52 = Artifact52
        self.domain_Artifact = domain_Artifact if domain_Artifact is not None else set()
        self.Artifact56 = Artifact56
        self.Artifact54 = Artifact54
        self.Artifact62 = Artifact62
        self.domain_Artifact277 = domain_Artifact277
        
    @property
    def template(self) -> str:
        return self.__template

    @template.setter
    def template(self, template: str):
        self.__template = template

    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

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
    def Artifact56(self):
        return self.__Artifact56

    @Artifact56.setter
    def Artifact56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Artifact__Artifact56", None)
        self.__Artifact56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "modelQuery"):
                opp_val = getattr(old_value, "modelQuery", None)
                if opp_val == self:
                    setattr(old_value, "modelQuery", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "modelQuery"):
                opp_val = getattr(value, "modelQuery", None)
                setattr(value, "modelQuery", self)

    @property
    def parent44(self):
        return self.__parent44

    @parent44.setter
    def parent44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Artifact__parent44", None)
        self.__parent44 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ConfigHash"):
                    opp_val = getattr(item, "ConfigHash", None)
                    
                    if opp_val == self:
                        setattr(item, "ConfigHash", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ConfigHash"):
                    opp_val = getattr(item, "ConfigHash", None)
                    
                    setattr(item, "ConfigHash", self)
                    

    @property
    def Artifact(self):
        return self.__Artifact

    @Artifact.setter
    def Artifact(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Artifact__Artifact", None)
        self.__Artifact = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent34"):
                opp_val = getattr(old_value, "parent34", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent34"):
                opp_val = getattr(value, "parent34", None)
                if opp_val is None:
                    setattr(value, "parent34", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Artifact54(self):
        return self.__Artifact54

    @Artifact54.setter
    def Artifact54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Artifact__Artifact54", None)
        self.__Artifact54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "configHashes"):
                opp_val = getattr(old_value, "configHashes", None)
                if opp_val == self:
                    setattr(old_value, "configHashes", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "configHashes"):
                opp_val = getattr(value, "configHashes", None)
                setattr(value, "configHashes", self)

    @property
    def parent46(self):
        return self.__parent46

    @parent46.setter
    def parent46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Artifact__parent46", None)
        self.__parent46 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ModelQuery"):
                    opp_val = getattr(item, "ModelQuery", None)
                    
                    if opp_val == self:
                        setattr(item, "ModelQuery", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ModelQuery"):
                    opp_val = getattr(item, "ModelQuery", None)
                    
                    setattr(item, "ModelQuery", self)
                    

    @property
    def parent42(self):
        return self.__parent42

    @parent42.setter
    def parent42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Artifact__parent42", None)
        self.__parent42 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ConfigVariable"):
                    opp_val = getattr(item, "ConfigVariable", None)
                    
                    if opp_val == self:
                        setattr(item, "ConfigVariable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ConfigVariable"):
                    opp_val = getattr(item, "ConfigVariable", None)
                    
                    setattr(item, "ConfigVariable", self)
                    

    @property
    def domain_Artifact(self):
        return self.__domain_Artifact

    @domain_Artifact.setter
    def domain_Artifact(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Artifact__domain_Artifact", None)
        self.__domain_Artifact = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "domain_GenerationHint50"):
                    opp_val = getattr(item, "domain_GenerationHint50", None)
                    
                    if opp_val == self:
                        setattr(item, "domain_GenerationHint50", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "domain_GenerationHint50"):
                    opp_val = getattr(item, "domain_GenerationHint50", None)
                    
                    setattr(item, "domain_GenerationHint50", self)
                    

    @property
    def artifacts(self):
        return self.__artifacts

    @artifacts.setter
    def artifacts(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Artifact__artifacts", None)
        self.__artifacts = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Artifacts40"):
                opp_val = getattr(old_value, "Artifacts40", None)
                if opp_val == self:
                    setattr(old_value, "Artifacts40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Artifacts40"):
                opp_val = getattr(value, "Artifacts40", None)
                setattr(value, "Artifacts40", self)

    @property
    def parent48(self):
        return self.__parent48

    @parent48.setter
    def parent48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Artifact__parent48", None)
        self.__parent48 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Specifier"):
                    opp_val = getattr(item, "Specifier", None)
                    
                    if opp_val == self:
                        setattr(item, "Specifier", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Specifier"):
                    opp_val = getattr(item, "Specifier", None)
                    
                    setattr(item, "Specifier", self)
                    

    @property
    def Artifact62(self):
        return self.__Artifact62

    @Artifact62.setter
    def Artifact62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Artifact__Artifact62", None)
        self.__Artifact62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "specifiers"):
                opp_val = getattr(old_value, "specifiers", None)
                if opp_val == self:
                    setattr(old_value, "specifiers", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "specifiers"):
                opp_val = getattr(value, "specifiers", None)
                setattr(value, "specifiers", self)

    @property
    def Artifact52(self):
        return self.__Artifact52

    @Artifact52.setter
    def Artifact52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Artifact__Artifact52", None)
        self.__Artifact52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "configVariables"):
                opp_val = getattr(old_value, "configVariables", None)
                if opp_val == self:
                    setattr(old_value, "configVariables", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "configVariables"):
                opp_val = getattr(value, "configVariables", None)
                setattr(value, "configVariables", self)

    @property
    def domain_Artifact277(self):
        return self.__domain_Artifact277

    @domain_Artifact277.setter
    def domain_Artifact277(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Artifact__domain_Artifact277", None)
        self.__domain_Artifact277 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_ArtifactRef276"):
                opp_val = getattr(old_value, "domain_ArtifactRef276", None)
                if opp_val == self:
                    setattr(old_value, "domain_ArtifactRef276", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_ArtifactRef276"):
                opp_val = getattr(value, "domain_ArtifactRef276", None)
                setattr(value, "domain_ArtifactRef276", self)

class domain_ContinuousIintegration(DomainArtifact):

    pass
class domain_EJBService(DomainArtifact):

    pass
class domain_Artifacts:

    def __init__(self, uid: str, Artifacts: "domain_DomainArtifact" = None, parent34: set["domain_Artifact"] = None, artifact: "domain_DomainArtifact" = None, domain_Artifacts: "domain_EObject" = None, Artifacts40: "domain_Artifact" = None):
        self.uid = uid
        self.Artifacts = Artifacts
        self.parent34 = parent34 if parent34 is not None else set()
        self.artifact = artifact
        self.domain_Artifacts = domain_Artifacts
        self.Artifacts40 = Artifacts40
        
    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def parent34(self):
        return self.__parent34

    @parent34.setter
    def parent34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Artifacts__parent34", None)
        self.__parent34 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Artifact"):
                    opp_val = getattr(item, "Artifact", None)
                    
                    if opp_val == self:
                        setattr(item, "Artifact", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Artifact"):
                    opp_val = getattr(item, "Artifact", None)
                    
                    setattr(item, "Artifact", self)
                    

    @property
    def Artifacts(self):
        return self.__Artifacts

    @Artifacts.setter
    def Artifacts(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Artifacts__Artifacts", None)
        self.__Artifacts = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent32"):
                opp_val = getattr(old_value, "parent32", None)
                if opp_val == self:
                    setattr(old_value, "parent32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent32"):
                opp_val = getattr(value, "parent32", None)
                setattr(value, "parent32", self)

    @property
    def Artifacts40(self):
        return self.__Artifacts40

    @Artifacts40.setter
    def Artifacts40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Artifacts__Artifacts40", None)
        self.__Artifacts40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "artifacts"):
                opp_val = getattr(old_value, "artifacts", None)
                if opp_val == self:
                    setattr(old_value, "artifacts", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "artifacts"):
                opp_val = getattr(value, "artifacts", None)
                setattr(value, "artifacts", self)

    @property
    def artifact(self):
        return self.__artifact

    @artifact.setter
    def artifact(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Artifacts__artifact", None)
        self.__artifact = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DomainArtifact36"):
                opp_val = getattr(old_value, "DomainArtifact36", None)
                if opp_val == self:
                    setattr(old_value, "DomainArtifact36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DomainArtifact36"):
                opp_val = getattr(value, "DomainArtifact36", None)
                setattr(value, "DomainArtifact36", self)

    @property
    def domain_Artifacts(self):
        return self.__domain_Artifacts

    @domain_Artifacts.setter
    def domain_Artifacts(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Artifacts__domain_Artifacts", None)
        self.__domain_Artifacts = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_EObject38"):
                opp_val = getattr(old_value, "domain_EObject38", None)
                if opp_val == self:
                    setattr(old_value, "domain_EObject38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_EObject38"):
                opp_val = getattr(value, "domain_EObject38", None)
                setattr(value, "domain_EObject38", self)

class domain_Application:

    def __init__(self, uid: str, Application: "domain_DomainApplication" = None, parent68: "domain_ApplicationRecipes" = None, parent70: "domain_ApplicationMappers" = None, parent72: "domain_ApplicationUILayer" = None, parent74: "domain_ApplicationInfrastructureLayer" = None, application: "domain_DomainApplication" = None, domain_Application: "domain_EObject" = None, Application86: "domain_ApplicationMessages" = None, parent76: "domain_ApplicationStyle" = None, parent78: "domain_ApplicationRole" = None, parent80: "domain_ApplicationMessages" = None, Application94: "domain_ApplicationStyle" = None, Application90: "domain_ApplicationRole" = None, Application102: "domain_ApplicationUILayer" = None, Application110: "domain_ApplicationRecipes" = None, Application118: "domain_ApplicationMappers" = None, Application555: "domain_ApplicationInfrastructureLayer" = None):
        self.uid = uid
        self.Application = Application
        self.parent68 = parent68
        self.parent70 = parent70
        self.parent72 = parent72
        self.parent74 = parent74
        self.application = application
        self.domain_Application = domain_Application
        self.Application86 = Application86
        self.parent76 = parent76
        self.parent78 = parent78
        self.parent80 = parent80
        self.Application94 = Application94
        self.Application90 = Application90
        self.Application102 = Application102
        self.Application110 = Application110
        self.Application118 = Application118
        self.Application555 = Application555
        
    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def Application90(self):
        return self.__Application90

    @Application90.setter
    def Application90(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Application__Application90", None)
        self.__Application90 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applicationRole"):
                opp_val = getattr(old_value, "applicationRole", None)
                if opp_val == self:
                    setattr(old_value, "applicationRole", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applicationRole"):
                opp_val = getattr(value, "applicationRole", None)
                setattr(value, "applicationRole", self)

    @property
    def domain_Application(self):
        return self.__domain_Application

    @domain_Application.setter
    def domain_Application(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Application__domain_Application", None)
        self.__domain_Application = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_EObject84"):
                opp_val = getattr(old_value, "domain_EObject84", None)
                if opp_val == self:
                    setattr(old_value, "domain_EObject84", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_EObject84"):
                opp_val = getattr(value, "domain_EObject84", None)
                setattr(value, "domain_EObject84", self)

    @property
    def parent68(self):
        return self.__parent68

    @parent68.setter
    def parent68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Application__parent68", None)
        self.__parent68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ApplicationRecipes"):
                opp_val = getattr(old_value, "ApplicationRecipes", None)
                if opp_val == self:
                    setattr(old_value, "ApplicationRecipes", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ApplicationRecipes"):
                opp_val = getattr(value, "ApplicationRecipes", None)
                setattr(value, "ApplicationRecipes", self)

    @property
    def Application555(self):
        return self.__Application555

    @Application555.setter
    def Application555(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Application__Application555", None)
        self.__Application555 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applicationInfrastructureLayer"):
                opp_val = getattr(old_value, "applicationInfrastructureLayer", None)
                if opp_val == self:
                    setattr(old_value, "applicationInfrastructureLayer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applicationInfrastructureLayer"):
                opp_val = getattr(value, "applicationInfrastructureLayer", None)
                setattr(value, "applicationInfrastructureLayer", self)

    @property
    def parent74(self):
        return self.__parent74

    @parent74.setter
    def parent74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Application__parent74", None)
        self.__parent74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ApplicationInfrastructureLayer"):
                opp_val = getattr(old_value, "ApplicationInfrastructureLayer", None)
                if opp_val == self:
                    setattr(old_value, "ApplicationInfrastructureLayer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ApplicationInfrastructureLayer"):
                opp_val = getattr(value, "ApplicationInfrastructureLayer", None)
                setattr(value, "ApplicationInfrastructureLayer", self)

    @property
    def Application118(self):
        return self.__Application118

    @Application118.setter
    def Application118(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Application__Application118", None)
        self.__Application118 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applicationMappers"):
                opp_val = getattr(old_value, "applicationMappers", None)
                if opp_val == self:
                    setattr(old_value, "applicationMappers", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applicationMappers"):
                opp_val = getattr(value, "applicationMappers", None)
                setattr(value, "applicationMappers", self)

    @property
    def application(self):
        return self.__application

    @application.setter
    def application(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Application__application", None)
        self.__application = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DomainApplication82"):
                opp_val = getattr(old_value, "DomainApplication82", None)
                if opp_val == self:
                    setattr(old_value, "DomainApplication82", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DomainApplication82"):
                opp_val = getattr(value, "DomainApplication82", None)
                setattr(value, "DomainApplication82", self)

    @property
    def Application86(self):
        return self.__Application86

    @Application86.setter
    def Application86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Application__Application86", None)
        self.__Application86 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applicationMessages"):
                opp_val = getattr(old_value, "applicationMessages", None)
                if opp_val == self:
                    setattr(old_value, "applicationMessages", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applicationMessages"):
                opp_val = getattr(value, "applicationMessages", None)
                setattr(value, "applicationMessages", self)

    @property
    def parent80(self):
        return self.__parent80

    @parent80.setter
    def parent80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Application__parent80", None)
        self.__parent80 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ApplicationMessages"):
                opp_val = getattr(old_value, "ApplicationMessages", None)
                if opp_val == self:
                    setattr(old_value, "ApplicationMessages", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ApplicationMessages"):
                opp_val = getattr(value, "ApplicationMessages", None)
                setattr(value, "ApplicationMessages", self)

    @property
    def Application110(self):
        return self.__Application110

    @Application110.setter
    def Application110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Application__Application110", None)
        self.__Application110 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applicationRecipes"):
                opp_val = getattr(old_value, "applicationRecipes", None)
                if opp_val == self:
                    setattr(old_value, "applicationRecipes", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applicationRecipes"):
                opp_val = getattr(value, "applicationRecipes", None)
                setattr(value, "applicationRecipes", self)

    @property
    def Application94(self):
        return self.__Application94

    @Application94.setter
    def Application94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Application__Application94", None)
        self.__Application94 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applicationStyle"):
                opp_val = getattr(old_value, "applicationStyle", None)
                if opp_val == self:
                    setattr(old_value, "applicationStyle", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applicationStyle"):
                opp_val = getattr(value, "applicationStyle", None)
                setattr(value, "applicationStyle", self)

    @property
    def parent70(self):
        return self.__parent70

    @parent70.setter
    def parent70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Application__parent70", None)
        self.__parent70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ApplicationMappers"):
                opp_val = getattr(old_value, "ApplicationMappers", None)
                if opp_val == self:
                    setattr(old_value, "ApplicationMappers", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ApplicationMappers"):
                opp_val = getattr(value, "ApplicationMappers", None)
                setattr(value, "ApplicationMappers", self)

    @property
    def Application102(self):
        return self.__Application102

    @Application102.setter
    def Application102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Application__Application102", None)
        self.__Application102 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applicationUILayer"):
                opp_val = getattr(old_value, "applicationUILayer", None)
                if opp_val == self:
                    setattr(old_value, "applicationUILayer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applicationUILayer"):
                opp_val = getattr(value, "applicationUILayer", None)
                setattr(value, "applicationUILayer", self)

    @property
    def parent78(self):
        return self.__parent78

    @parent78.setter
    def parent78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Application__parent78", None)
        self.__parent78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ApplicationRole"):
                opp_val = getattr(old_value, "ApplicationRole", None)
                if opp_val == self:
                    setattr(old_value, "ApplicationRole", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ApplicationRole"):
                opp_val = getattr(value, "ApplicationRole", None)
                setattr(value, "ApplicationRole", self)

    @property
    def parent76(self):
        return self.__parent76

    @parent76.setter
    def parent76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Application__parent76", None)
        self.__parent76 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ApplicationStyle"):
                opp_val = getattr(old_value, "ApplicationStyle", None)
                if opp_val == self:
                    setattr(old_value, "ApplicationStyle", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ApplicationStyle"):
                opp_val = getattr(value, "ApplicationStyle", None)
                setattr(value, "ApplicationStyle", self)

    @property
    def parent72(self):
        return self.__parent72

    @parent72.setter
    def parent72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Application__parent72", None)
        self.__parent72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ApplicationUILayer"):
                opp_val = getattr(old_value, "ApplicationUILayer", None)
                if opp_val == self:
                    setattr(old_value, "ApplicationUILayer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ApplicationUILayer"):
                opp_val = getattr(value, "ApplicationUILayer", None)
                setattr(value, "ApplicationUILayer", self)

    @property
    def Application(self):
        return self.__Application

    @Application.setter
    def Application(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Application__Application", None)
        self.__Application = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent26"):
                opp_val = getattr(old_value, "parent26", None)
                if opp_val == self:
                    setattr(old_value, "parent26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent26"):
                opp_val = getattr(value, "parent26", None)
                setattr(value, "parent26", self)

class domain_TypesRepository:

    def __init__(self, uid: str, TypesRepository: "domain_DomainTypes" = None, domain_TypesRepository: "domain_EObject" = None, TypesRepository328: "domain_Types" = None, parent322: "domain_Types" = None, typesrepository: "domain_DomainTypes" = None):
        self.uid = uid
        self.TypesRepository = TypesRepository
        self.domain_TypesRepository = domain_TypesRepository
        self.TypesRepository328 = TypesRepository328
        self.parent322 = parent322
        self.typesrepository = typesrepository
        
    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def domain_TypesRepository(self):
        return self.__domain_TypesRepository

    @domain_TypesRepository.setter
    def domain_TypesRepository(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_TypesRepository__domain_TypesRepository", None)
        self.__domain_TypesRepository = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_EObject326"):
                opp_val = getattr(old_value, "domain_EObject326", None)
                if opp_val == self:
                    setattr(old_value, "domain_EObject326", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_EObject326"):
                opp_val = getattr(value, "domain_EObject326", None)
                setattr(value, "domain_EObject326", self)

    @property
    def parent322(self):
        return self.__parent322

    @parent322.setter
    def parent322(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_TypesRepository__parent322", None)
        self.__parent322 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Types"):
                opp_val = getattr(old_value, "Types", None)
                if opp_val == self:
                    setattr(old_value, "Types", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Types"):
                opp_val = getattr(value, "Types", None)
                setattr(value, "Types", self)

    @property
    def TypesRepository(self):
        return self.__TypesRepository

    @TypesRepository.setter
    def TypesRepository(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_TypesRepository__TypesRepository", None)
        self.__TypesRepository = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent18"):
                opp_val = getattr(old_value, "parent18", None)
                if opp_val == self:
                    setattr(old_value, "parent18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent18"):
                opp_val = getattr(value, "parent18", None)
                setattr(value, "parent18", self)

    @property
    def TypesRepository328(self):
        return self.__TypesRepository328

    @TypesRepository328.setter
    def TypesRepository328(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_TypesRepository__TypesRepository328", None)
        self.__TypesRepository328 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "typeDefinition"):
                opp_val = getattr(old_value, "typeDefinition", None)
                if opp_val == self:
                    setattr(old_value, "typeDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "typeDefinition"):
                opp_val = getattr(value, "typeDefinition", None)
                setattr(value, "typeDefinition", self)

    @property
    def typesrepository(self):
        return self.__typesrepository

    @typesrepository.setter
    def typesrepository(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_TypesRepository__typesrepository", None)
        self.__typesrepository = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DomainTypes324"):
                opp_val = getattr(old_value, "DomainTypes324", None)
                if opp_val == self:
                    setattr(old_value, "DomainTypes324", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DomainTypes324"):
                opp_val = getattr(value, "DomainTypes324", None)
                setattr(value, "DomainTypes324", self)

class domain_DomainArtifact:

    def __init__(self, uid: str, name: str, DomainArtifact: "domain_DomainArtifacts" = None, domainArtifact: "domain_DomainArtifacts" = None, parent32: "domain_Artifacts" = None, DomainArtifact36: "domain_Artifacts" = None, domain_DomainArtifact: "domain_ArtifactRef" = None):
        self.uid = uid
        self.name = name
        self.DomainArtifact = DomainArtifact
        self.domainArtifact = domainArtifact
        self.parent32 = parent32
        self.DomainArtifact36 = DomainArtifact36
        self.domain_DomainArtifact = domain_DomainArtifact
        
    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def DomainArtifact(self):
        return self.__DomainArtifact

    @DomainArtifact.setter
    def DomainArtifact(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_DomainArtifact__DomainArtifact", None)
        self.__DomainArtifact = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent16"):
                opp_val = getattr(old_value, "parent16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent16"):
                opp_val = getattr(value, "parent16", None)
                if opp_val is None:
                    setattr(value, "parent16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def DomainArtifact36(self):
        return self.__DomainArtifact36

    @DomainArtifact36.setter
    def DomainArtifact36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_DomainArtifact__DomainArtifact36", None)
        self.__DomainArtifact36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "artifact"):
                opp_val = getattr(old_value, "artifact", None)
                if opp_val == self:
                    setattr(old_value, "artifact", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "artifact"):
                opp_val = getattr(value, "artifact", None)
                setattr(value, "artifact", self)

    @property
    def domain_DomainArtifact(self):
        return self.__domain_DomainArtifact

    @domain_DomainArtifact.setter
    def domain_DomainArtifact(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_DomainArtifact__domain_DomainArtifact", None)
        self.__domain_DomainArtifact = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_ArtifactRef"):
                opp_val = getattr(old_value, "domain_ArtifactRef", None)
                if opp_val == self:
                    setattr(old_value, "domain_ArtifactRef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_ArtifactRef"):
                opp_val = getattr(value, "domain_ArtifactRef", None)
                setattr(value, "domain_ArtifactRef", self)

    @property
    def parent32(self):
        return self.__parent32

    @parent32.setter
    def parent32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_DomainArtifact__parent32", None)
        self.__parent32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Artifacts"):
                opp_val = getattr(old_value, "Artifacts", None)
                if opp_val == self:
                    setattr(old_value, "Artifacts", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Artifacts"):
                opp_val = getattr(value, "Artifacts", None)
                setattr(value, "Artifacts", self)

    @property
    def domainArtifact(self):
        return self.__domainArtifact

    @domainArtifact.setter
    def domainArtifact(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_DomainArtifact__domainArtifact", None)
        self.__domainArtifact = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DomainArtifacts30"):
                opp_val = getattr(old_value, "DomainArtifacts30", None)
                if opp_val == self:
                    setattr(old_value, "DomainArtifacts30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DomainArtifacts30"):
                opp_val = getattr(value, "DomainArtifacts30", None)
                setattr(value, "DomainArtifacts30", self)

class domain_Classifier:

    def __init__(self, uid: str, details: str, domain_Classifier8: "domain_GenerationHint" = None, domain_Classifier: "domain_Categorized" = None, domain_Classifier417: "domain_StyleClass" = None):
        self.uid = uid
        self.details = details
        self.domain_Classifier8 = domain_Classifier8
        self.domain_Classifier = domain_Classifier
        self.domain_Classifier417 = domain_Classifier417
        
    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def details(self) -> str:
        return self.__details

    @details.setter
    def details(self, details: str):
        self.__details = details

    @property
    def domain_Classifier417(self):
        return self.__domain_Classifier417

    @domain_Classifier417.setter
    def domain_Classifier417(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Classifier__domain_Classifier417", None)
        self.__domain_Classifier417 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_StyleClass416"):
                opp_val = getattr(old_value, "domain_StyleClass416", None)
                if opp_val == self:
                    setattr(old_value, "domain_StyleClass416", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_StyleClass416"):
                opp_val = getattr(value, "domain_StyleClass416", None)
                setattr(value, "domain_StyleClass416", self)

    @property
    def domain_Classifier8(self):
        return self.__domain_Classifier8

    @domain_Classifier8.setter
    def domain_Classifier8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Classifier__domain_Classifier8", None)
        self.__domain_Classifier8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_GenerationHint"):
                opp_val = getattr(old_value, "domain_GenerationHint", None)
                if opp_val == self:
                    setattr(old_value, "domain_GenerationHint", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_GenerationHint"):
                opp_val = getattr(value, "domain_GenerationHint", None)
                setattr(value, "domain_GenerationHint", self)

    @property
    def domain_Classifier(self):
        return self.__domain_Classifier

    @domain_Classifier.setter
    def domain_Classifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Classifier__domain_Classifier", None)
        self.__domain_Classifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_Categorized"):
                opp_val = getattr(old_value, "domain_Categorized", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_Categorized"):
                opp_val = getattr(value, "domain_Categorized", None)
                if opp_val is None:
                    setattr(value, "domain_Categorized", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class domain_Categorized:

    pass
class domain_HTMLLayerHolder:

    def __init__(self, columns: int):
        self.columns = columns
        
    @property
    def columns(self) -> int:
        return self.__columns

    @columns.setter
    def columns(self, columns: int):
        self.__columns = columns

class HTMLLayerHolder:

    pass
class domain_Table(SourcesPointer, MultiLangLabel, HTMLLayerHolder):

    def __init__(self, label: str, rowNumber: int, domain_Table: set["domain_Column"] = None):
        self.label = label
        self.rowNumber = rowNumber
        self.domain_Table = domain_Table if domain_Table is not None else set()
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def rowNumber(self) -> int:
        return self.__rowNumber

    @rowNumber.setter
    def rowNumber(self, rowNumber: int):
        self.__rowNumber = rowNumber

    @property
    def domain_Table(self):
        return self.__domain_Table

    @domain_Table.setter
    def domain_Table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Table__domain_Table", None)
        self.__domain_Table = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "domain_Column463"):
                    opp_val = getattr(item, "domain_Column463", None)
                    
                    if opp_val == self:
                        setattr(item, "domain_Column463", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "domain_Column463"):
                    opp_val = getattr(item, "domain_Column463", None)
                    
                    setattr(item, "domain_Column463", self)
                    

class domain_LayerHolder(Uielement, ChildrenHolder, HTMLLayerHolder):

    pass
class domain_ApplicationStyle(HTMLLayerHolder):

    def __init__(self, uid: str, name: str, ApplicationStyle: "domain_Application" = None, applicationStyle: "domain_Application" = None, parent96: set["domain_StylesPackage"] = None, ApplicationStyle98: "domain_StylesPackage" = None):
        self.uid = uid
        self.name = name
        self.ApplicationStyle = ApplicationStyle
        self.applicationStyle = applicationStyle
        self.parent96 = parent96 if parent96 is not None else set()
        self.ApplicationStyle98 = ApplicationStyle98
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def applicationStyle(self):
        return self.__applicationStyle

    @applicationStyle.setter
    def applicationStyle(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_ApplicationStyle__applicationStyle", None)
        self.__applicationStyle = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Application94"):
                opp_val = getattr(old_value, "Application94", None)
                if opp_val == self:
                    setattr(old_value, "Application94", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Application94"):
                opp_val = getattr(value, "Application94", None)
                setattr(value, "Application94", self)

    @property
    def ApplicationStyle(self):
        return self.__ApplicationStyle

    @ApplicationStyle.setter
    def ApplicationStyle(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_ApplicationStyle__ApplicationStyle", None)
        self.__ApplicationStyle = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent76"):
                opp_val = getattr(old_value, "parent76", None)
                if opp_val == self:
                    setattr(old_value, "parent76", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent76"):
                opp_val = getattr(value, "parent76", None)
                setattr(value, "parent76", self)

    @property
    def ApplicationStyle98(self):
        return self.__ApplicationStyle98

    @ApplicationStyle98.setter
    def ApplicationStyle98(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_ApplicationStyle__ApplicationStyle98", None)
        self.__ApplicationStyle98 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stylesPackage"):
                opp_val = getattr(old_value, "stylesPackage", None)
                if opp_val == self:
                    setattr(old_value, "stylesPackage", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stylesPackage"):
                opp_val = getattr(value, "stylesPackage", None)
                setattr(value, "stylesPackage", self)

    @property
    def parent96(self):
        return self.__parent96

    @parent96.setter
    def parent96(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_ApplicationStyle__parent96", None)
        self.__parent96 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StylesPackage"):
                    opp_val = getattr(item, "StylesPackage", None)
                    
                    if opp_val == self:
                        setattr(item, "StylesPackage", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StylesPackage"):
                    opp_val = getattr(item, "StylesPackage", None)
                    
                    setattr(item, "StylesPackage", self)
                    

class domain_Types(HTMLLayerHolder):

    def __init__(self, uid: str, name: str, typeDefinition: "domain_TypesRepository" = None, parent330: set["domain_Package"] = None, Types: "domain_TypesRepository" = None, Types336: "domain_Package" = None):
        self.uid = uid
        self.name = name
        self.typeDefinition = typeDefinition
        self.parent330 = parent330 if parent330 is not None else set()
        self.Types = Types
        self.Types336 = Types336
        
    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Types336(self):
        return self.__Types336

    @Types336.setter
    def Types336(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Types__Types336", None)
        self.__Types336 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "packages"):
                opp_val = getattr(old_value, "packages", None)
                if opp_val == self:
                    setattr(old_value, "packages", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "packages"):
                opp_val = getattr(value, "packages", None)
                setattr(value, "packages", self)

    @property
    def typeDefinition(self):
        return self.__typeDefinition

    @typeDefinition.setter
    def typeDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Types__typeDefinition", None)
        self.__typeDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TypesRepository328"):
                opp_val = getattr(old_value, "TypesRepository328", None)
                if opp_val == self:
                    setattr(old_value, "TypesRepository328", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TypesRepository328"):
                opp_val = getattr(value, "TypesRepository328", None)
                setattr(value, "TypesRepository328", self)

    @property
    def parent330(self):
        return self.__parent330

    @parent330.setter
    def parent330(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Types__parent330", None)
        self.__parent330 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Package331"):
                    opp_val = getattr(item, "Package331", None)
                    
                    if opp_val == self:
                        setattr(item, "Package331", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Package331"):
                    opp_val = getattr(item, "Package331", None)
                    
                    setattr(item, "Package331", self)
                    

    @property
    def Types(self):
        return self.__Types

    @Types.setter
    def Types(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Types__Types", None)
        self.__Types = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent322"):
                opp_val = getattr(old_value, "parent322", None)
                if opp_val == self:
                    setattr(old_value, "parent322", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent322"):
                opp_val = getattr(value, "parent322", None)
                setattr(value, "parent322", self)

class domain_MenuFolder(HTMLLayerHolder, Categorized, MultiLangLabel, EnabledUIItem, ItemIcon, StyleElement):

    def __init__(self, uid: str, name: str, extensionPoint: bool, domain_MenuFolder: "domain_MenuView" = None, domain_MenuFolder592: "domain_MenuHolder" = None, domain_MenuFolder594: "domain_MenuExtensionRef" = None, domain_MenuFolder596: set["domain_MenuElement"] = None, domain_MenuFolder603: "domain_SubMenu" = None):
        self.uid = uid
        self.name = name
        self.extensionPoint = extensionPoint
        self.domain_MenuFolder = domain_MenuFolder
        self.domain_MenuFolder592 = domain_MenuFolder592
        self.domain_MenuFolder594 = domain_MenuFolder594
        self.domain_MenuFolder596 = domain_MenuFolder596 if domain_MenuFolder596 is not None else set()
        self.domain_MenuFolder603 = domain_MenuFolder603
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def extensionPoint(self) -> bool:
        return self.__extensionPoint

    @extensionPoint.setter
    def extensionPoint(self, extensionPoint: bool):
        self.__extensionPoint = extensionPoint

    @property
    def domain_MenuFolder592(self):
        return self.__domain_MenuFolder592

    @domain_MenuFolder592.setter
    def domain_MenuFolder592(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_MenuFolder__domain_MenuFolder592", None)
        self.__domain_MenuFolder592 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_MenuHolder"):
                opp_val = getattr(old_value, "domain_MenuHolder", None)
                if opp_val == self:
                    setattr(old_value, "domain_MenuHolder", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_MenuHolder"):
                opp_val = getattr(value, "domain_MenuHolder", None)
                setattr(value, "domain_MenuHolder", self)

    @property
    def domain_MenuFolder596(self):
        return self.__domain_MenuFolder596

    @domain_MenuFolder596.setter
    def domain_MenuFolder596(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_MenuFolder__domain_MenuFolder596", None)
        self.__domain_MenuFolder596 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "domain_MenuElement"):
                    opp_val = getattr(item, "domain_MenuElement", None)
                    
                    if opp_val == self:
                        setattr(item, "domain_MenuElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "domain_MenuElement"):
                    opp_val = getattr(item, "domain_MenuElement", None)
                    
                    setattr(item, "domain_MenuElement", self)
                    

    @property
    def domain_MenuFolder(self):
        return self.__domain_MenuFolder

    @domain_MenuFolder.setter
    def domain_MenuFolder(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_MenuFolder__domain_MenuFolder", None)
        self.__domain_MenuFolder = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_MenuView"):
                opp_val = getattr(old_value, "domain_MenuView", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_MenuView"):
                opp_val = getattr(value, "domain_MenuView", None)
                if opp_val is None:
                    setattr(value, "domain_MenuView", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def domain_MenuFolder594(self):
        return self.__domain_MenuFolder594

    @domain_MenuFolder594.setter
    def domain_MenuFolder594(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_MenuFolder__domain_MenuFolder594", None)
        self.__domain_MenuFolder594 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_MenuExtensionRef"):
                opp_val = getattr(old_value, "domain_MenuExtensionRef", None)
                if opp_val == self:
                    setattr(old_value, "domain_MenuExtensionRef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_MenuExtensionRef"):
                opp_val = getattr(value, "domain_MenuExtensionRef", None)
                setattr(value, "domain_MenuExtensionRef", self)

    @property
    def domain_MenuFolder603(self):
        return self.__domain_MenuFolder603

    @domain_MenuFolder603.setter
    def domain_MenuFolder603(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_MenuFolder__domain_MenuFolder603", None)
        self.__domain_MenuFolder603 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_SubMenu"):
                opp_val = getattr(old_value, "domain_SubMenu", None)
                if opp_val == self:
                    setattr(old_value, "domain_SubMenu", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_SubMenu"):
                opp_val = getattr(value, "domain_SubMenu", None)
                setattr(value, "domain_SubMenu", self)

class domain_ViewPortHolder(HTMLLayerHolder):

    pass
class domain_ApplicationRecipes(HTMLLayerHolder):

    def __init__(self, uid: str, name: str, ApplicationRecipes: "domain_Application" = None, applicationRecipes: "domain_Application" = None, parent112: set["domain_ApplicationRecipe"] = None, ApplicationRecipes116: "domain_ApplicationRecipe" = None):
        self.uid = uid
        self.name = name
        self.ApplicationRecipes = ApplicationRecipes
        self.applicationRecipes = applicationRecipes
        self.parent112 = parent112 if parent112 is not None else set()
        self.ApplicationRecipes116 = ApplicationRecipes116
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def applicationRecipes(self):
        return self.__applicationRecipes

    @applicationRecipes.setter
    def applicationRecipes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_ApplicationRecipes__applicationRecipes", None)
        self.__applicationRecipes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Application110"):
                opp_val = getattr(old_value, "Application110", None)
                if opp_val == self:
                    setattr(old_value, "Application110", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Application110"):
                opp_val = getattr(value, "Application110", None)
                setattr(value, "Application110", self)

    @property
    def parent112(self):
        return self.__parent112

    @parent112.setter
    def parent112(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_ApplicationRecipes__parent112", None)
        self.__parent112 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ApplicationRecipe"):
                    opp_val = getattr(item, "ApplicationRecipe", None)
                    
                    if opp_val == self:
                        setattr(item, "ApplicationRecipe", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ApplicationRecipe"):
                    opp_val = getattr(item, "ApplicationRecipe", None)
                    
                    setattr(item, "ApplicationRecipe", self)
                    

    @property
    def ApplicationRecipes116(self):
        return self.__ApplicationRecipes116

    @ApplicationRecipes116.setter
    def ApplicationRecipes116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_ApplicationRecipes__ApplicationRecipes116", None)
        self.__ApplicationRecipes116 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "recipes"):
                opp_val = getattr(old_value, "recipes", None)
                if opp_val == self:
                    setattr(old_value, "recipes", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "recipes"):
                opp_val = getattr(value, "recipes", None)
                setattr(value, "recipes", self)

    @property
    def ApplicationRecipes(self):
        return self.__ApplicationRecipes

    @ApplicationRecipes.setter
    def ApplicationRecipes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_ApplicationRecipes__ApplicationRecipes", None)
        self.__ApplicationRecipes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent68"):
                opp_val = getattr(old_value, "parent68", None)
                if opp_val == self:
                    setattr(old_value, "parent68", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent68"):
                opp_val = getattr(value, "parent68", None)
                setattr(value, "parent68", self)

class domain_Datacenter(HTMLLayerHolder):

    def __init__(self, name: str, uid: str, Datacenter: "domain_EnterpriseInfrastructure" = None, datacenters: "domain_EnterpriseInfrastructure" = None, parent569: set["domain_Subsystem"] = None, Datacenter571: "domain_Subsystem" = None):
        self.name = name
        self.uid = uid
        self.Datacenter = Datacenter
        self.datacenters = datacenters
        self.parent569 = parent569 if parent569 is not None else set()
        self.Datacenter571 = Datacenter571
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def datacenters(self):
        return self.__datacenters

    @datacenters.setter
    def datacenters(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Datacenter__datacenters", None)
        self.__datacenters = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EnterpriseInfrastructure567"):
                opp_val = getattr(old_value, "EnterpriseInfrastructure567", None)
                if opp_val == self:
                    setattr(old_value, "EnterpriseInfrastructure567", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EnterpriseInfrastructure567"):
                opp_val = getattr(value, "EnterpriseInfrastructure567", None)
                setattr(value, "EnterpriseInfrastructure567", self)

    @property
    def Datacenter(self):
        return self.__Datacenter

    @Datacenter.setter
    def Datacenter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Datacenter__Datacenter", None)
        self.__Datacenter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent561"):
                opp_val = getattr(old_value, "parent561", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent561"):
                opp_val = getattr(value, "parent561", None)
                if opp_val is None:
                    setattr(value, "parent561", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Datacenter571(self):
        return self.__Datacenter571

    @Datacenter571.setter
    def Datacenter571(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Datacenter__Datacenter571", None)
        self.__Datacenter571 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "subsystems"):
                opp_val = getattr(old_value, "subsystems", None)
                if opp_val == self:
                    setattr(old_value, "subsystems", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "subsystems"):
                opp_val = getattr(value, "subsystems", None)
                setattr(value, "subsystems", self)

    @property
    def parent569(self):
        return self.__parent569

    @parent569.setter
    def parent569(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Datacenter__parent569", None)
        self.__parent569 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Subsystem"):
                    opp_val = getattr(item, "Subsystem", None)
                    
                    if opp_val == self:
                        setattr(item, "Subsystem", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Subsystem"):
                    opp_val = getattr(item, "Subsystem", None)
                    
                    setattr(item, "Subsystem", self)
                    

class domain_Column(HTMLLayerHolder, Categorized, Orderable, MultiLangLabel, StyleElement):

    def __init__(self, label: str, uid: str, domain_Column: "domain_Uielement" = None, domain_Column463: "domain_Table" = None, domain_Column468: "domain_Tree" = None):
        self.label = label
        self.uid = uid
        self.domain_Column = domain_Column
        self.domain_Column463 = domain_Column463
        self.domain_Column468 = domain_Column468
        
    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def domain_Column468(self):
        return self.__domain_Column468

    @domain_Column468.setter
    def domain_Column468(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Column__domain_Column468", None)
        self.__domain_Column468 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_Tree467"):
                opp_val = getattr(old_value, "domain_Tree467", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_Tree467"):
                opp_val = getattr(value, "domain_Tree467", None)
                if opp_val is None:
                    setattr(value, "domain_Tree467", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def domain_Column(self):
        return self.__domain_Column

    @domain_Column.setter
    def domain_Column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Column__domain_Column", None)
        self.__domain_Column = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_Uielement461"):
                opp_val = getattr(old_value, "domain_Uielement461", None)
                if opp_val == self:
                    setattr(old_value, "domain_Uielement461", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_Uielement461"):
                opp_val = getattr(value, "domain_Uielement461", None)
                setattr(value, "domain_Uielement461", self)

    @property
    def domain_Column463(self):
        return self.__domain_Column463

    @domain_Column463.setter
    def domain_Column463(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Column__domain_Column463", None)
        self.__domain_Column463 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_Table"):
                opp_val = getattr(old_value, "domain_Table", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_Table"):
                opp_val = getattr(value, "domain_Table", None)
                if opp_val is None:
                    setattr(value, "domain_Table", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class domain_Tree(SourcesPointer, MultiLangLabel, HTMLLayerHolder):

    def __init__(self, label: str, domain_Tree: "domain_Context" = None, domain_Tree467: set["domain_Column"] = None):
        self.label = label
        self.domain_Tree = domain_Tree
        self.domain_Tree467 = domain_Tree467 if domain_Tree467 is not None else set()
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def domain_Tree467(self):
        return self.__domain_Tree467

    @domain_Tree467.setter
    def domain_Tree467(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Tree__domain_Tree467", None)
        self.__domain_Tree467 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "domain_Column468"):
                    opp_val = getattr(item, "domain_Column468", None)
                    
                    if opp_val == self:
                        setattr(item, "domain_Column468", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "domain_Column468"):
                    opp_val = getattr(item, "domain_Column468", None)
                    
                    setattr(item, "domain_Column468", self)
                    

    @property
    def domain_Tree(self):
        return self.__domain_Tree

    @domain_Tree.setter
    def domain_Tree(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Tree__domain_Tree", None)
        self.__domain_Tree = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_Context465"):
                opp_val = getattr(old_value, "domain_Context465", None)
                if opp_val == self:
                    setattr(old_value, "domain_Context465", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_Context465"):
                opp_val = getattr(value, "domain_Context465", None)
                setattr(value, "domain_Context465", self)

class domain_Component(HTMLLayerHolder):

    def __init__(self, uid: str, name: str, componentRoot: str, Component: "domain_Ingredient" = None, components: "domain_Ingredient" = None, parent238: set["domain_ModelMapper"] = None, Component250: "domain_ModelMapper" = None):
        self.uid = uid
        self.name = name
        self.componentRoot = componentRoot
        self.Component = Component
        self.components = components
        self.parent238 = parent238 if parent238 is not None else set()
        self.Component250 = Component250
        
    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def componentRoot(self) -> str:
        return self.__componentRoot

    @componentRoot.setter
    def componentRoot(self, componentRoot: str):
        self.__componentRoot = componentRoot

    @property
    def components(self):
        return self.__components

    @components.setter
    def components(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Component__components", None)
        self.__components = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Ingredient236"):
                opp_val = getattr(old_value, "Ingredient236", None)
                if opp_val == self:
                    setattr(old_value, "Ingredient236", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Ingredient236"):
                opp_val = getattr(value, "Ingredient236", None)
                setattr(value, "Ingredient236", self)

    @property
    def parent238(self):
        return self.__parent238

    @parent238.setter
    def parent238(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Component__parent238", None)
        self.__parent238 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ModelMapper"):
                    opp_val = getattr(item, "ModelMapper", None)
                    
                    if opp_val == self:
                        setattr(item, "ModelMapper", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ModelMapper"):
                    opp_val = getattr(item, "ModelMapper", None)
                    
                    setattr(item, "ModelMapper", self)
                    

    @property
    def Component250(self):
        return self.__Component250

    @Component250.setter
    def Component250(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Component__Component250", None)
        self.__Component250 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mappers249"):
                opp_val = getattr(old_value, "mappers249", None)
                if opp_val == self:
                    setattr(old_value, "mappers249", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mappers249"):
                opp_val = getattr(value, "mappers249", None)
                setattr(value, "mappers249", self)

    @property
    def Component(self):
        return self.__Component

    @Component.setter
    def Component(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Component__Component", None)
        self.__Component = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent234"):
                opp_val = getattr(old_value, "parent234", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent234"):
                opp_val = getattr(value, "parent234", None)
                if opp_val is None:
                    setattr(value, "parent234", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class domain_ApplicationMappers(HTMLLayerHolder):

    def __init__(self, name: str, uid: str, ApplicationMappers: "domain_Application" = None, applicationMappers: "domain_Application" = None, parent120: set["domain_ApplicationMapper"] = None, ApplicationMappers124: "domain_ApplicationMapper" = None):
        self.name = name
        self.uid = uid
        self.ApplicationMappers = ApplicationMappers
        self.applicationMappers = applicationMappers
        self.parent120 = parent120 if parent120 is not None else set()
        self.ApplicationMappers124 = ApplicationMappers124
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def applicationMappers(self):
        return self.__applicationMappers

    @applicationMappers.setter
    def applicationMappers(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_ApplicationMappers__applicationMappers", None)
        self.__applicationMappers = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Application118"):
                opp_val = getattr(old_value, "Application118", None)
                if opp_val == self:
                    setattr(old_value, "Application118", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Application118"):
                opp_val = getattr(value, "Application118", None)
                setattr(value, "Application118", self)

    @property
    def ApplicationMappers124(self):
        return self.__ApplicationMappers124

    @ApplicationMappers124.setter
    def ApplicationMappers124(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_ApplicationMappers__ApplicationMappers124", None)
        self.__ApplicationMappers124 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mappers"):
                opp_val = getattr(old_value, "mappers", None)
                if opp_val == self:
                    setattr(old_value, "mappers", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mappers"):
                opp_val = getattr(value, "mappers", None)
                setattr(value, "mappers", self)

    @property
    def parent120(self):
        return self.__parent120

    @parent120.setter
    def parent120(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_ApplicationMappers__parent120", None)
        self.__parent120 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ApplicationMapper"):
                    opp_val = getattr(item, "ApplicationMapper", None)
                    
                    if opp_val == self:
                        setattr(item, "ApplicationMapper", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ApplicationMapper"):
                    opp_val = getattr(item, "ApplicationMapper", None)
                    
                    setattr(item, "ApplicationMapper", self)
                    

    @property
    def ApplicationMappers(self):
        return self.__ApplicationMappers

    @ApplicationMappers.setter
    def ApplicationMappers(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_ApplicationMappers__ApplicationMappers", None)
        self.__ApplicationMappers = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent70"):
                opp_val = getattr(old_value, "parent70", None)
                if opp_val == self:
                    setattr(old_value, "parent70", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent70"):
                opp_val = getattr(value, "parent70", None)
                setattr(value, "parent70", self)

class domain_Ingredient(UsingMappers, HTMLLayerHolder):

    def __init__(self, name: str, layer: str, uid: str, Ingredient: "domain_Recipe" = None, ingredients: "domain_Recipe" = None, parent234: set["domain_Component"] = None, Ingredient236: "domain_Component" = None):
        self.name = name
        self.layer = layer
        self.uid = uid
        self.Ingredient = Ingredient
        self.ingredients = ingredients
        self.parent234 = parent234 if parent234 is not None else set()
        self.Ingredient236 = Ingredient236
        
    @property
    def layer(self) -> str:
        return self.__layer

    @layer.setter
    def layer(self, layer: str):
        self.__layer = layer

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def parent234(self):
        return self.__parent234

    @parent234.setter
    def parent234(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Ingredient__parent234", None)
        self.__parent234 = value if value is not None else set()
        
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
    def Ingredient(self):
        return self.__Ingredient

    @Ingredient.setter
    def Ingredient(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Ingredient__Ingredient", None)
        self.__Ingredient = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent220"):
                opp_val = getattr(old_value, "parent220", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent220"):
                opp_val = getattr(value, "parent220", None)
                if opp_val is None:
                    setattr(value, "parent220", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ingredients(self):
        return self.__ingredients

    @ingredients.setter
    def ingredients(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Ingredient__ingredients", None)
        self.__ingredients = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Recipe232"):
                opp_val = getattr(old_value, "Recipe232", None)
                if opp_val == self:
                    setattr(old_value, "Recipe232", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Recipe232"):
                opp_val = getattr(value, "Recipe232", None)
                setattr(value, "Recipe232", self)

    @property
    def Ingredient236(self):
        return self.__Ingredient236

    @Ingredient236.setter
    def Ingredient236(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Ingredient__Ingredient236", None)
        self.__Ingredient236 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "components"):
                opp_val = getattr(old_value, "components", None)
                if opp_val == self:
                    setattr(old_value, "components", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "components"):
                opp_val = getattr(value, "components", None)
                setattr(value, "components", self)

class domain_ApplicationUILayer(HTMLLayerHolder):

    def __init__(self, uid: str, name: str, ApplicationUILayer: "domain_Application" = None, applicationUILayer: "domain_Application" = None, parent104: set["domain_ApplicationUIPackage"] = None, ApplicationUILayer106: "domain_ApplicationUIPackage" = None):
        self.uid = uid
        self.name = name
        self.ApplicationUILayer = ApplicationUILayer
        self.applicationUILayer = applicationUILayer
        self.parent104 = parent104 if parent104 is not None else set()
        self.ApplicationUILayer106 = ApplicationUILayer106
        
    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def applicationUILayer(self):
        return self.__applicationUILayer

    @applicationUILayer.setter
    def applicationUILayer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_ApplicationUILayer__applicationUILayer", None)
        self.__applicationUILayer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Application102"):
                opp_val = getattr(old_value, "Application102", None)
                if opp_val == self:
                    setattr(old_value, "Application102", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Application102"):
                opp_val = getattr(value, "Application102", None)
                setattr(value, "Application102", self)

    @property
    def ApplicationUILayer106(self):
        return self.__ApplicationUILayer106

    @ApplicationUILayer106.setter
    def ApplicationUILayer106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_ApplicationUILayer__ApplicationUILayer106", None)
        self.__ApplicationUILayer106 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applicationUIPackages"):
                opp_val = getattr(old_value, "applicationUIPackages", None)
                if opp_val == self:
                    setattr(old_value, "applicationUIPackages", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applicationUIPackages"):
                opp_val = getattr(value, "applicationUIPackages", None)
                setattr(value, "applicationUIPackages", self)

    @property
    def parent104(self):
        return self.__parent104

    @parent104.setter
    def parent104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_ApplicationUILayer__parent104", None)
        self.__parent104 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ApplicationUIPackage"):
                    opp_val = getattr(item, "ApplicationUIPackage", None)
                    
                    if opp_val == self:
                        setattr(item, "ApplicationUIPackage", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ApplicationUIPackage"):
                    opp_val = getattr(item, "ApplicationUIPackage", None)
                    
                    setattr(item, "ApplicationUIPackage", self)
                    

    @property
    def ApplicationUILayer(self):
        return self.__ApplicationUILayer

    @ApplicationUILayer.setter
    def ApplicationUILayer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_ApplicationUILayer__ApplicationUILayer", None)
        self.__ApplicationUILayer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent72"):
                opp_val = getattr(old_value, "parent72", None)
                if opp_val == self:
                    setattr(old_value, "parent72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent72"):
                opp_val = getattr(value, "parent72", None)
                setattr(value, "parent72", self)

class domain_Role:

    def __init__(self, uid: str, name: str, domain_Role: "domain_GrantAccess" = None, domain_Role149: "domain_Roles" = None, domain_Role160: "domain_Group" = None):
        self.uid = uid
        self.name = name
        self.domain_Role = domain_Role
        self.domain_Role149 = domain_Role149
        self.domain_Role160 = domain_Role160
        
    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def domain_Role(self):
        return self.__domain_Role

    @domain_Role.setter
    def domain_Role(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Role__domain_Role", None)
        self.__domain_Role = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_GrantAccess13"):
                opp_val = getattr(old_value, "domain_GrantAccess13", None)
                if opp_val == self:
                    setattr(old_value, "domain_GrantAccess13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_GrantAccess13"):
                opp_val = getattr(value, "domain_GrantAccess13", None)
                setattr(value, "domain_GrantAccess13", self)

    @property
    def domain_Role149(self):
        return self.__domain_Role149

    @domain_Role149.setter
    def domain_Role149(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Role__domain_Role149", None)
        self.__domain_Role149 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_Roles"):
                opp_val = getattr(old_value, "domain_Roles", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_Roles"):
                opp_val = getattr(value, "domain_Roles", None)
                if opp_val is None:
                    setattr(value, "domain_Roles", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def domain_Role160(self):
        return self.__domain_Role160

    @domain_Role160.setter
    def domain_Role160(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Role__domain_Role160", None)
        self.__domain_Role160 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_Group159"):
                opp_val = getattr(old_value, "domain_Group159", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_Group159"):
                opp_val = getattr(value, "domain_Group159", None)
                if opp_val is None:
                    setattr(value, "domain_Group159", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class domain_DomainApplication:

    def __init__(self, uid: str, name: str, domain_DomainApplication: "domain_GrantAccess" = None, parent26: "domain_Application" = None, applications: "domain_DomainApplications" = None, DomainApplication: "domain_DomainApplications" = None, DomainApplication82: "domain_Application" = None):
        self.uid = uid
        self.name = name
        self.domain_DomainApplication = domain_DomainApplication
        self.parent26 = parent26
        self.applications = applications
        self.DomainApplication = DomainApplication
        self.DomainApplication82 = DomainApplication82
        
    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def applications(self):
        return self.__applications

    @applications.setter
    def applications(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_DomainApplication__applications", None)
        self.__applications = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DomainApplications28"):
                opp_val = getattr(old_value, "DomainApplications28", None)
                if opp_val == self:
                    setattr(old_value, "DomainApplications28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DomainApplications28"):
                opp_val = getattr(value, "DomainApplications28", None)
                setattr(value, "DomainApplications28", self)

    @property
    def DomainApplication82(self):
        return self.__DomainApplication82

    @DomainApplication82.setter
    def DomainApplication82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_DomainApplication__DomainApplication82", None)
        self.__DomainApplication82 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "application"):
                opp_val = getattr(old_value, "application", None)
                if opp_val == self:
                    setattr(old_value, "application", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "application"):
                opp_val = getattr(value, "application", None)
                setattr(value, "application", self)

    @property
    def DomainApplication(self):
        return self.__DomainApplication

    @DomainApplication.setter
    def DomainApplication(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_DomainApplication__DomainApplication", None)
        self.__DomainApplication = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent22"):
                opp_val = getattr(old_value, "parent22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent22"):
                opp_val = getattr(value, "parent22", None)
                if opp_val is None:
                    setattr(value, "parent22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def domain_DomainApplication(self):
        return self.__domain_DomainApplication

    @domain_DomainApplication.setter
    def domain_DomainApplication(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_DomainApplication__domain_DomainApplication", None)
        self.__domain_DomainApplication = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_GrantAccess11"):
                opp_val = getattr(old_value, "domain_GrantAccess11", None)
                if opp_val == self:
                    setattr(old_value, "domain_GrantAccess11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_GrantAccess11"):
                opp_val = getattr(value, "domain_GrantAccess11", None)
                setattr(value, "domain_GrantAccess11", self)

    @property
    def parent26(self):
        return self.__parent26

    @parent26.setter
    def parent26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_DomainApplication__parent26", None)
        self.__parent26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Application"):
                opp_val = getattr(old_value, "Application", None)
                if opp_val == self:
                    setattr(old_value, "Application", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Application"):
                opp_val = getattr(value, "Application", None)
                setattr(value, "Application", self)

class domain_GrantAccess:

    def __init__(self, uid: str, domain_GrantAccess: "domain_Secured" = None, domain_GrantAccess11: "domain_DomainApplication" = None, domain_GrantAccess13: "domain_Role" = None):
        self.uid = uid
        self.domain_GrantAccess = domain_GrantAccess
        self.domain_GrantAccess11 = domain_GrantAccess11
        self.domain_GrantAccess13 = domain_GrantAccess13
        
    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def domain_GrantAccess(self):
        return self.__domain_GrantAccess

    @domain_GrantAccess.setter
    def domain_GrantAccess(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_GrantAccess__domain_GrantAccess", None)
        self.__domain_GrantAccess = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_Secured"):
                opp_val = getattr(old_value, "domain_Secured", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_Secured"):
                opp_val = getattr(value, "domain_Secured", None)
                if opp_val is None:
                    setattr(value, "domain_Secured", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def domain_GrantAccess11(self):
        return self.__domain_GrantAccess11

    @domain_GrantAccess11.setter
    def domain_GrantAccess11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_GrantAccess__domain_GrantAccess11", None)
        self.__domain_GrantAccess11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_DomainApplication"):
                opp_val = getattr(old_value, "domain_DomainApplication", None)
                if opp_val == self:
                    setattr(old_value, "domain_DomainApplication", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_DomainApplication"):
                opp_val = getattr(value, "domain_DomainApplication", None)
                setattr(value, "domain_DomainApplication", self)

    @property
    def domain_GrantAccess13(self):
        return self.__domain_GrantAccess13

    @domain_GrantAccess13.setter
    def domain_GrantAccess13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_GrantAccess__domain_GrantAccess13", None)
        self.__domain_GrantAccess13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_Role"):
                opp_val = getattr(old_value, "domain_Role", None)
                if opp_val == self:
                    setattr(old_value, "domain_Role", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_Role"):
                opp_val = getattr(value, "domain_Role", None)
                setattr(value, "domain_Role", self)

class domain_Secured:

    pass
class domain_GenerationHint:

    def __init__(self, uid: str, name: str, applyedClass: str, domain_GenerationHint: "domain_Classifier" = None, domain_GenerationHint50: "domain_Artifact" = None):
        self.uid = uid
        self.name = name
        self.applyedClass = applyedClass
        self.domain_GenerationHint = domain_GenerationHint
        self.domain_GenerationHint50 = domain_GenerationHint50
        
    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def applyedClass(self) -> str:
        return self.__applyedClass

    @applyedClass.setter
    def applyedClass(self, applyedClass: str):
        self.__applyedClass = applyedClass

    @property
    def domain_GenerationHint(self):
        return self.__domain_GenerationHint

    @domain_GenerationHint.setter
    def domain_GenerationHint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_GenerationHint__domain_GenerationHint", None)
        self.__domain_GenerationHint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_Classifier8"):
                opp_val = getattr(old_value, "domain_Classifier8", None)
                if opp_val == self:
                    setattr(old_value, "domain_Classifier8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_Classifier8"):
                opp_val = getattr(value, "domain_Classifier8", None)
                setattr(value, "domain_Classifier8", self)

    @property
    def domain_GenerationHint50(self):
        return self.__domain_GenerationHint50

    @domain_GenerationHint50.setter
    def domain_GenerationHint50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_GenerationHint__domain_GenerationHint50", None)
        self.__domain_GenerationHint50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_Artifact"):
                opp_val = getattr(old_value, "domain_Artifact", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_Artifact"):
                opp_val = getattr(value, "domain_Artifact", None)
                if opp_val is None:
                    setattr(value, "domain_Artifact", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class domain_EObject:

    pass
class domain_DomainApplications(HTMLLayerHolder):

    def __init__(self, uid: str, name: str, DomainApplications: "domain_Domain" = None, DomainApplications28: "domain_DomainApplication" = None, parent22: set["domain_DomainApplication"] = None, domainApplications: "domain_Domain" = None):
        self.uid = uid
        self.name = name
        self.DomainApplications = DomainApplications
        self.DomainApplications28 = DomainApplications28
        self.parent22 = parent22 if parent22 is not None else set()
        self.domainApplications = domainApplications
        
    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def DomainApplications(self):
        return self.__DomainApplications

    @DomainApplications.setter
    def DomainApplications(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_DomainApplications__DomainApplications", None)
        self.__DomainApplications = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent4"):
                opp_val = getattr(old_value, "parent4", None)
                if opp_val == self:
                    setattr(old_value, "parent4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent4"):
                opp_val = getattr(value, "parent4", None)
                setattr(value, "parent4", self)

    @property
    def parent22(self):
        return self.__parent22

    @parent22.setter
    def parent22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_DomainApplications__parent22", None)
        self.__parent22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DomainApplication"):
                    opp_val = getattr(item, "DomainApplication", None)
                    
                    if opp_val == self:
                        setattr(item, "DomainApplication", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DomainApplication"):
                    opp_val = getattr(item, "DomainApplication", None)
                    
                    setattr(item, "DomainApplication", self)
                    

    @property
    def domainApplications(self):
        return self.__domainApplications

    @domainApplications.setter
    def domainApplications(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_DomainApplications__domainApplications", None)
        self.__domainApplications = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Domain24"):
                opp_val = getattr(old_value, "Domain24", None)
                if opp_val == self:
                    setattr(old_value, "Domain24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Domain24"):
                opp_val = getattr(value, "Domain24", None)
                setattr(value, "Domain24", self)

    @property
    def DomainApplications28(self):
        return self.__DomainApplications28

    @DomainApplications28.setter
    def DomainApplications28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_DomainApplications__DomainApplications28", None)
        self.__DomainApplications28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applications"):
                opp_val = getattr(old_value, "applications", None)
                if opp_val == self:
                    setattr(old_value, "applications", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applications"):
                opp_val = getattr(value, "applications", None)
                setattr(value, "applications", self)

class domain_DomainTypes:

    def __init__(self, uid: str, name: str, DomainTypes: "domain_Domain" = None, parent18: "domain_TypesRepository" = None, domainTypes: "domain_Domain" = None, DomainTypes324: "domain_TypesRepository" = None):
        self.uid = uid
        self.name = name
        self.DomainTypes = DomainTypes
        self.parent18 = parent18
        self.domainTypes = domainTypes
        self.DomainTypes324 = DomainTypes324
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def DomainTypes324(self):
        return self.__DomainTypes324

    @DomainTypes324.setter
    def DomainTypes324(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_DomainTypes__DomainTypes324", None)
        self.__DomainTypes324 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "typesrepository"):
                opp_val = getattr(old_value, "typesrepository", None)
                if opp_val == self:
                    setattr(old_value, "typesrepository", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "typesrepository"):
                opp_val = getattr(value, "typesrepository", None)
                setattr(value, "typesrepository", self)

    @property
    def parent18(self):
        return self.__parent18

    @parent18.setter
    def parent18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_DomainTypes__parent18", None)
        self.__parent18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TypesRepository"):
                opp_val = getattr(old_value, "TypesRepository", None)
                if opp_val == self:
                    setattr(old_value, "TypesRepository", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TypesRepository"):
                opp_val = getattr(value, "TypesRepository", None)
                setattr(value, "TypesRepository", self)

    @property
    def DomainTypes(self):
        return self.__DomainTypes

    @DomainTypes.setter
    def DomainTypes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_DomainTypes__DomainTypes", None)
        self.__DomainTypes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent2"):
                opp_val = getattr(old_value, "parent2", None)
                if opp_val == self:
                    setattr(old_value, "parent2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent2"):
                opp_val = getattr(value, "parent2", None)
                setattr(value, "parent2", self)

    @property
    def domainTypes(self):
        return self.__domainTypes

    @domainTypes.setter
    def domainTypes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_DomainTypes__domainTypes", None)
        self.__domainTypes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Domain20"):
                opp_val = getattr(old_value, "Domain20", None)
                if opp_val == self:
                    setattr(old_value, "Domain20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Domain20"):
                opp_val = getattr(value, "Domain20", None)
                setattr(value, "Domain20", self)

class domain_DomainArtifacts(HTMLLayerHolder):

    def __init__(self, uid: str, name: str, DomainArtifacts: "domain_Domain" = None, parent16: set["domain_DomainArtifact"] = None, domainArtifacts: "domain_Domain" = None, DomainArtifacts30: "domain_DomainArtifact" = None):
        self.uid = uid
        self.name = name
        self.DomainArtifacts = DomainArtifacts
        self.parent16 = parent16 if parent16 is not None else set()
        self.domainArtifacts = domainArtifacts
        self.DomainArtifacts30 = DomainArtifacts30
        
    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def domainArtifacts(self):
        return self.__domainArtifacts

    @domainArtifacts.setter
    def domainArtifacts(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_DomainArtifacts__domainArtifacts", None)
        self.__domainArtifacts = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Domain"):
                opp_val = getattr(old_value, "Domain", None)
                if opp_val == self:
                    setattr(old_value, "Domain", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Domain"):
                opp_val = getattr(value, "Domain", None)
                setattr(value, "Domain", self)

    @property
    def parent16(self):
        return self.__parent16

    @parent16.setter
    def parent16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_DomainArtifacts__parent16", None)
        self.__parent16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DomainArtifact"):
                    opp_val = getattr(item, "DomainArtifact", None)
                    
                    if opp_val == self:
                        setattr(item, "DomainArtifact", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DomainArtifact"):
                    opp_val = getattr(item, "DomainArtifact", None)
                    
                    setattr(item, "DomainArtifact", self)
                    

    @property
    def DomainArtifacts(self):
        return self.__DomainArtifacts

    @DomainArtifacts.setter
    def DomainArtifacts(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_DomainArtifacts__DomainArtifacts", None)
        self.__DomainArtifacts = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent"):
                opp_val = getattr(old_value, "parent", None)
                if opp_val == self:
                    setattr(old_value, "parent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent"):
                opp_val = getattr(value, "parent", None)
                setattr(value, "parent", self)

    @property
    def DomainArtifacts30(self):
        return self.__DomainArtifacts30

    @DomainArtifacts30.setter
    def DomainArtifacts30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_DomainArtifacts__DomainArtifacts30", None)
        self.__DomainArtifacts30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domainArtifact"):
                opp_val = getattr(old_value, "domainArtifact", None)
                if opp_val == self:
                    setattr(old_value, "domainArtifact", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domainArtifact"):
                opp_val = getattr(value, "domainArtifact", None)
                setattr(value, "domainArtifact", self)

class domain_Domain:

    def __init__(self, uid: str, parent: "domain_DomainArtifacts" = None, parent2: "domain_DomainTypes" = None, parent4: "domain_DomainApplications" = None, domain_Domain: "domain_EObject" = None, Domain20: "domain_DomainTypes" = None, Domain: "domain_DomainArtifacts" = None, Domain24: "domain_DomainApplications" = None):
        self.uid = uid
        self.parent = parent
        self.parent2 = parent2
        self.parent4 = parent4
        self.domain_Domain = domain_Domain
        self.Domain20 = Domain20
        self.Domain = Domain
        self.Domain24 = Domain24
        
    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Domain__parent", None)
        self.__parent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DomainArtifacts"):
                opp_val = getattr(old_value, "DomainArtifacts", None)
                if opp_val == self:
                    setattr(old_value, "DomainArtifacts", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DomainArtifacts"):
                opp_val = getattr(value, "DomainArtifacts", None)
                setattr(value, "DomainArtifacts", self)

    @property
    def Domain20(self):
        return self.__Domain20

    @Domain20.setter
    def Domain20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Domain__Domain20", None)
        self.__Domain20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domainTypes"):
                opp_val = getattr(old_value, "domainTypes", None)
                if opp_val == self:
                    setattr(old_value, "domainTypes", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domainTypes"):
                opp_val = getattr(value, "domainTypes", None)
                setattr(value, "domainTypes", self)

    @property
    def Domain(self):
        return self.__Domain

    @Domain.setter
    def Domain(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Domain__Domain", None)
        self.__Domain = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domainArtifacts"):
                opp_val = getattr(old_value, "domainArtifacts", None)
                if opp_val == self:
                    setattr(old_value, "domainArtifacts", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domainArtifacts"):
                opp_val = getattr(value, "domainArtifacts", None)
                setattr(value, "domainArtifacts", self)

    @property
    def domain_Domain(self):
        return self.__domain_Domain

    @domain_Domain.setter
    def domain_Domain(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Domain__domain_Domain", None)
        self.__domain_Domain = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain_EObject"):
                opp_val = getattr(old_value, "domain_EObject", None)
                if opp_val == self:
                    setattr(old_value, "domain_EObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain_EObject"):
                opp_val = getattr(value, "domain_EObject", None)
                setattr(value, "domain_EObject", self)

    @property
    def parent2(self):
        return self.__parent2

    @parent2.setter
    def parent2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Domain__parent2", None)
        self.__parent2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DomainTypes"):
                opp_val = getattr(old_value, "DomainTypes", None)
                if opp_val == self:
                    setattr(old_value, "DomainTypes", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DomainTypes"):
                opp_val = getattr(value, "DomainTypes", None)
                setattr(value, "DomainTypes", self)

    @property
    def Domain24(self):
        return self.__Domain24

    @Domain24.setter
    def Domain24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Domain__Domain24", None)
        self.__Domain24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domainApplications"):
                opp_val = getattr(old_value, "domainApplications", None)
                if opp_val == self:
                    setattr(old_value, "domainApplications", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domainApplications"):
                opp_val = getattr(value, "domainApplications", None)
                setattr(value, "domainApplications", self)

    @property
    def parent4(self):
        return self.__parent4

    @parent4.setter
    def parent4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Domain__parent4", None)
        self.__parent4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DomainApplications"):
                opp_val = getattr(old_value, "DomainApplications", None)
                if opp_val == self:
                    setattr(old_value, "DomainApplications", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DomainApplications"):
                opp_val = getattr(value, "DomainApplications", None)
                setattr(value, "DomainApplications", self)
