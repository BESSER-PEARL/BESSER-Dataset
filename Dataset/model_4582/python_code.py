from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class EJavaObject:

    pass
class device_Object(EJavaObject):

    pass
class Fonctionnalite:

    pass
class device_Action(Fonctionnalite):

    pass
class device_Capture(Fonctionnalite):

    pass
class device_EJavaObject:

    pass
class device_Parametre:

    def __init__(self, name: str, device_Parametre: "device_Fonctionnalite" = None, device_Parametre6: "device_EJavaObject" = None):
        self.name = name
        self.device_Parametre = device_Parametre
        self.device_Parametre6 = device_Parametre6
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def device_Parametre(self):
        return self.__device_Parametre

    @device_Parametre.setter
    def device_Parametre(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_device_Parametre__device_Parametre", None)
        self.__device_Parametre = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "device_Fonctionnalite4"):
                opp_val = getattr(old_value, "device_Fonctionnalite4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "device_Fonctionnalite4"):
                opp_val = getattr(value, "device_Fonctionnalite4", None)
                if opp_val is None:
                    setattr(value, "device_Fonctionnalite4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def device_Parametre6(self):
        return self.__device_Parametre6

    @device_Parametre6.setter
    def device_Parametre6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_device_Parametre__device_Parametre6", None)
        self.__device_Parametre6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "device_EJavaObject"):
                opp_val = getattr(old_value, "device_EJavaObject", None)
                if opp_val == self:
                    setattr(old_value, "device_EJavaObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "device_EJavaObject"):
                opp_val = getattr(value, "device_EJavaObject", None)
                setattr(value, "device_EJavaObject", self)

class device_Fonctionnalite:

    def __init__(self, name: str, device_Fonctionnalite: "device_Device" = None, device_Fonctionnalite4: set["device_Parametre"] = None):
        self.name = name
        self.device_Fonctionnalite = device_Fonctionnalite
        self.device_Fonctionnalite4 = device_Fonctionnalite4 if device_Fonctionnalite4 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def device_Fonctionnalite(self):
        return self.__device_Fonctionnalite

    @device_Fonctionnalite.setter
    def device_Fonctionnalite(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_device_Fonctionnalite__device_Fonctionnalite", None)
        self.__device_Fonctionnalite = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "device_Device2"):
                opp_val = getattr(old_value, "device_Device2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "device_Device2"):
                opp_val = getattr(value, "device_Device2", None)
                if opp_val is None:
                    setattr(value, "device_Device2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def device_Fonctionnalite4(self):
        return self.__device_Fonctionnalite4

    @device_Fonctionnalite4.setter
    def device_Fonctionnalite4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_device_Fonctionnalite__device_Fonctionnalite4", None)
        self.__device_Fonctionnalite4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "device_Parametre"):
                    opp_val = getattr(item, "device_Parametre", None)
                    
                    if opp_val == self:
                        setattr(item, "device_Parametre", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "device_Parametre"):
                    opp_val = getattr(item, "device_Parametre", None)
                    
                    setattr(item, "device_Parametre", self)
                    

class device_Device:

    def __init__(self, name: str, device_Device: "device_Types" = None, device_Device2: set["device_Fonctionnalite"] = None):
        self.name = name
        self.device_Device = device_Device
        self.device_Device2 = device_Device2 if device_Device2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def device_Device2(self):
        return self.__device_Device2

    @device_Device2.setter
    def device_Device2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_device_Device__device_Device2", None)
        self.__device_Device2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "device_Fonctionnalite"):
                    opp_val = getattr(item, "device_Fonctionnalite", None)
                    
                    if opp_val == self:
                        setattr(item, "device_Fonctionnalite", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "device_Fonctionnalite"):
                    opp_val = getattr(item, "device_Fonctionnalite", None)
                    
                    setattr(item, "device_Fonctionnalite", self)
                    

    @property
    def device_Device(self):
        return self.__device_Device

    @device_Device.setter
    def device_Device(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_device_Device__device_Device", None)
        self.__device_Device = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "device_Types"):
                opp_val = getattr(old_value, "device_Types", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "device_Types"):
                opp_val = getattr(value, "device_Types", None)
                if opp_val is None:
                    setattr(value, "device_Types", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class device_Types:

    pass