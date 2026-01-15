from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class dsl_Parametre:

    def __init__(self, name: str, dsl_Parametre5: "dsl_EJavaObject" = None, dsl_Parametre: "dsl_Fonctionnalite" = None):
        self.name = name
        self.dsl_Parametre5 = dsl_Parametre5
        self.dsl_Parametre = dsl_Parametre
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dsl_Parametre5(self):
        return self.__dsl_Parametre5

    @dsl_Parametre5.setter
    def dsl_Parametre5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Parametre__dsl_Parametre5", None)
        self.__dsl_Parametre5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_EJavaObject"):
                opp_val = getattr(old_value, "dsl_EJavaObject", None)
                if opp_val == self:
                    setattr(old_value, "dsl_EJavaObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_EJavaObject"):
                opp_val = getattr(value, "dsl_EJavaObject", None)
                setattr(value, "dsl_EJavaObject", self)

    @property
    def dsl_Parametre(self):
        return self.__dsl_Parametre

    @dsl_Parametre.setter
    def dsl_Parametre(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Parametre__dsl_Parametre", None)
        self.__dsl_Parametre = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Fonctionnalite"):
                opp_val = getattr(old_value, "dsl_Fonctionnalite", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Fonctionnalite"):
                opp_val = getattr(value, "dsl_Fonctionnalite", None)
                if opp_val is None:
                    setattr(value, "dsl_Fonctionnalite", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class dsl_Fonctionnalite:

    def __init__(self, name: str, dsl_Fonctionnalite3: "dsl_Device" = None, dsl_Fonctionnalite: set["dsl_Parametre"] = None):
        self.name = name
        self.dsl_Fonctionnalite3 = dsl_Fonctionnalite3
        self.dsl_Fonctionnalite = dsl_Fonctionnalite if dsl_Fonctionnalite is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dsl_Fonctionnalite(self):
        return self.__dsl_Fonctionnalite

    @dsl_Fonctionnalite.setter
    def dsl_Fonctionnalite(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Fonctionnalite__dsl_Fonctionnalite", None)
        self.__dsl_Fonctionnalite = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dsl_Parametre"):
                    opp_val = getattr(item, "dsl_Parametre", None)
                    
                    if opp_val == self:
                        setattr(item, "dsl_Parametre", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dsl_Parametre"):
                    opp_val = getattr(item, "dsl_Parametre", None)
                    
                    setattr(item, "dsl_Parametre", self)
                    

    @property
    def dsl_Fonctionnalite3(self):
        return self.__dsl_Fonctionnalite3

    @dsl_Fonctionnalite3.setter
    def dsl_Fonctionnalite3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Fonctionnalite__dsl_Fonctionnalite3", None)
        self.__dsl_Fonctionnalite3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Device"):
                opp_val = getattr(old_value, "dsl_Device", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Device"):
                opp_val = getattr(value, "dsl_Device", None)
                if opp_val is None:
                    setattr(value, "dsl_Device", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class dsl_IDevice:

    def __init__(self, typeof: str, name: str, dsl_IDevice: "dsl_Robot" = None):
        self.typeof = typeof
        self.name = name
        self.dsl_IDevice = dsl_IDevice
        
    @property
    def typeof(self) -> str:
        return self.__typeof

    @typeof.setter
    def typeof(self, typeof: str):
        self.__typeof = typeof

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dsl_IDevice(self):
        return self.__dsl_IDevice

    @dsl_IDevice.setter
    def dsl_IDevice(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_IDevice__dsl_IDevice", None)
        self.__dsl_IDevice = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Robot"):
                opp_val = getattr(old_value, "dsl_Robot", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Robot"):
                opp_val = getattr(value, "dsl_Robot", None)
                if opp_val is None:
                    setattr(value, "dsl_Robot", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class EJavaObject:

    pass
class dsl_Object(EJavaObject):

    pass
class Fonctionnalite:

    pass
class dsl_Action(Fonctionnalite):

    pass
class dsl_Capture(Fonctionnalite):

    pass
class dsl_EJavaObject:

    pass
class dsl_Device:

    def __init__(self, name: str, dsl_Device: set["dsl_Fonctionnalite"] = None):
        self.name = name
        self.dsl_Device = dsl_Device if dsl_Device is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dsl_Device(self):
        return self.__dsl_Device

    @dsl_Device.setter
    def dsl_Device(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Device__dsl_Device", None)
        self.__dsl_Device = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dsl_Fonctionnalite3"):
                    opp_val = getattr(item, "dsl_Fonctionnalite3", None)
                    
                    if opp_val == self:
                        setattr(item, "dsl_Fonctionnalite3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dsl_Fonctionnalite3"):
                    opp_val = getattr(item, "dsl_Fonctionnalite3", None)
                    
                    setattr(item, "dsl_Fonctionnalite3", self)
                    

class dsl_Robot:

    def __init__(self, name: str, dsl_Robot: set["dsl_IDevice"] = None):
        self.name = name
        self.dsl_Robot = dsl_Robot if dsl_Robot is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dsl_Robot(self):
        return self.__dsl_Robot

    @dsl_Robot.setter
    def dsl_Robot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Robot__dsl_Robot", None)
        self.__dsl_Robot = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dsl_IDevice"):
                    opp_val = getattr(item, "dsl_IDevice", None)
                    
                    if opp_val == self:
                        setattr(item, "dsl_IDevice", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dsl_IDevice"):
                    opp_val = getattr(item, "dsl_IDevice", None)
                    
                    setattr(item, "dsl_IDevice", self)
                    
