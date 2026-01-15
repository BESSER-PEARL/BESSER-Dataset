from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class componentModel_ComponentFeature:

    pass
class SystemPortDec:

    pass
class componentModel_SystemPortOut(SystemPortDec):

    pass
class componentModel_SystemPortIn(SystemPortDec):

    pass
class AbstractFeatures:

    pass
class componentModel_CompConnDec(AbstractFeatures):

    pass
class componentModel_ComponentType(AbstractFeatures):

    pass
class componentModel_ComponentImpl(AbstractFeatures):

    pass
class componentModel_AbstractFeatures:

    def __init__(self, name: str, componentModel_AbstractFeatures: "componentModel_SystemDec" = None):
        self.name = name
        self.componentModel_AbstractFeatures = componentModel_AbstractFeatures
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def componentModel_AbstractFeatures(self):
        return self.__componentModel_AbstractFeatures

    @componentModel_AbstractFeatures.setter
    def componentModel_AbstractFeatures(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_componentModel_AbstractFeatures__componentModel_AbstractFeatures", None)
        self.__componentModel_AbstractFeatures = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "componentModel_SystemDec11"):
                opp_val = getattr(old_value, "componentModel_SystemDec11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "componentModel_SystemDec11"):
                opp_val = getattr(value, "componentModel_SystemDec11", None)
                if opp_val is None:
                    setattr(value, "componentModel_SystemDec11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class componentModel_errorModes:

    def __init__(self, name: str, componentModel_errorModes: "componentModel_PortType" = None):
        self.name = name
        self.componentModel_errorModes = componentModel_errorModes
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def componentModel_errorModes(self):
        return self.__componentModel_errorModes

    @componentModel_errorModes.setter
    def componentModel_errorModes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_componentModel_errorModes__componentModel_errorModes", None)
        self.__componentModel_errorModes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "componentModel_PortType39"):
                opp_val = getattr(old_value, "componentModel_PortType39", None)
                if opp_val == self:
                    setattr(old_value, "componentModel_PortType39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "componentModel_PortType39"):
                opp_val = getattr(value, "componentModel_PortType39", None)
                setattr(value, "componentModel_PortType39", self)

class Port:

    pass
class componentModel_InPort(Port):

    pass
class componentModel_OutPort(Port):

    pass
class componentModel_Port:

    def __init__(self, name: str, componentModel_Port: "componentModel_ComponentFeature" = None, componentModel_Port37: "componentModel_PortType" = None):
        self.name = name
        self.componentModel_Port = componentModel_Port
        self.componentModel_Port37 = componentModel_Port37
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def componentModel_Port(self):
        return self.__componentModel_Port

    @componentModel_Port.setter
    def componentModel_Port(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_componentModel_Port__componentModel_Port", None)
        self.__componentModel_Port = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "componentModel_ComponentFeature35"):
                opp_val = getattr(old_value, "componentModel_ComponentFeature35", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "componentModel_ComponentFeature35"):
                opp_val = getattr(value, "componentModel_ComponentFeature35", None)
                if opp_val is None:
                    setattr(value, "componentModel_ComponentFeature35", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def componentModel_Port37(self):
        return self.__componentModel_Port37

    @componentModel_Port37.setter
    def componentModel_Port37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_componentModel_Port__componentModel_Port37", None)
        self.__componentModel_Port37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "componentModel_PortType"):
                opp_val = getattr(old_value, "componentModel_PortType", None)
                if opp_val == self:
                    setattr(old_value, "componentModel_PortType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "componentModel_PortType"):
                opp_val = getattr(value, "componentModel_PortType", None)
                setattr(value, "componentModel_PortType", self)

class componentModel_SystemPortDec(AbstractFeatures):

    pass
class AbstractElement:

    pass
class componentModel_PortType(AbstractElement):

    pass
class componentModel_SystemDec(AbstractElement):

    pass
class componentModel_SystemConnDec(AbstractElement):

    pass
class componentModel_AbstractElement:

    def __init__(self, name: str, componentModel_AbstractElement: "componentModel_ComponentModel" = None):
        self.name = name
        self.componentModel_AbstractElement = componentModel_AbstractElement
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def componentModel_AbstractElement(self):
        return self.__componentModel_AbstractElement

    @componentModel_AbstractElement.setter
    def componentModel_AbstractElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_componentModel_AbstractElement__componentModel_AbstractElement", None)
        self.__componentModel_AbstractElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "componentModel_ComponentModel"):
                opp_val = getattr(old_value, "componentModel_ComponentModel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "componentModel_ComponentModel"):
                opp_val = getattr(value, "componentModel_ComponentModel", None)
                if opp_val is None:
                    setattr(value, "componentModel_ComponentModel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class componentModel_ComponentModel:

    pass