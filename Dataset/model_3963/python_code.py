from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class SuperCall:

    pass
class archDSL_OptCall(SuperCall):

    pass
class archDSL_AltCall(SuperCall):

    def __init__(self, opt: bool, archDSL_AltCall: set["archDSL_SuperMethod"] = None):
        self.opt = opt
        self.archDSL_AltCall = archDSL_AltCall if archDSL_AltCall is not None else set()
        
    @property
    def opt(self) -> bool:
        return self.__opt

    @opt.setter
    def opt(self, opt: bool):
        self.__opt = opt

    @property
    def archDSL_AltCall(self):
        return self.__archDSL_AltCall

    @archDSL_AltCall.setter
    def archDSL_AltCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archDSL_AltCall__archDSL_AltCall", None)
        self.__archDSL_AltCall = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "archDSL_SuperMethod42"):
                    opp_val = getattr(item, "archDSL_SuperMethod42", None)
                    
                    if opp_val == self:
                        setattr(item, "archDSL_SuperMethod42", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "archDSL_SuperMethod42"):
                    opp_val = getattr(item, "archDSL_SuperMethod42", None)
                    
                    setattr(item, "archDSL_SuperMethod42", self)
                    

class archDSL_CertainCall(SuperCall):

    pass
class archDSL_SuperCall:

    pass
class archDSL_UncertainBehavior:

    def __init__(self, name: str, archDSL_UncertainBehavior: "archDSL_UncertainConnector" = None, archDSL_UncertainBehavior37: set["archDSL_SuperCall"] = None, archDSL_UncertainBehavior39: "archDSL_Interface" = None):
        self.name = name
        self.archDSL_UncertainBehavior = archDSL_UncertainBehavior
        self.archDSL_UncertainBehavior37 = archDSL_UncertainBehavior37 if archDSL_UncertainBehavior37 is not None else set()
        self.archDSL_UncertainBehavior39 = archDSL_UncertainBehavior39
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def archDSL_UncertainBehavior37(self):
        return self.__archDSL_UncertainBehavior37

    @archDSL_UncertainBehavior37.setter
    def archDSL_UncertainBehavior37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archDSL_UncertainBehavior__archDSL_UncertainBehavior37", None)
        self.__archDSL_UncertainBehavior37 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "archDSL_SuperCall"):
                    opp_val = getattr(item, "archDSL_SuperCall", None)
                    
                    if opp_val == self:
                        setattr(item, "archDSL_SuperCall", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "archDSL_SuperCall"):
                    opp_val = getattr(item, "archDSL_SuperCall", None)
                    
                    setattr(item, "archDSL_SuperCall", self)
                    

    @property
    def archDSL_UncertainBehavior39(self):
        return self.__archDSL_UncertainBehavior39

    @archDSL_UncertainBehavior39.setter
    def archDSL_UncertainBehavior39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archDSL_UncertainBehavior__archDSL_UncertainBehavior39", None)
        self.__archDSL_UncertainBehavior39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "archDSL_Interface40"):
                opp_val = getattr(old_value, "archDSL_Interface40", None)
                if opp_val == self:
                    setattr(old_value, "archDSL_Interface40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "archDSL_Interface40"):
                opp_val = getattr(value, "archDSL_Interface40", None)
                setattr(value, "archDSL_Interface40", self)

    @property
    def archDSL_UncertainBehavior(self):
        return self.__archDSL_UncertainBehavior

    @archDSL_UncertainBehavior.setter
    def archDSL_UncertainBehavior(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archDSL_UncertainBehavior__archDSL_UncertainBehavior", None)
        self.__archDSL_UncertainBehavior = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "archDSL_UncertainConnector25"):
                opp_val = getattr(old_value, "archDSL_UncertainConnector25", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "archDSL_UncertainConnector25"):
                opp_val = getattr(value, "archDSL_UncertainConnector25", None)
                if opp_val is None:
                    setattr(value, "archDSL_UncertainConnector25", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class archDSL_Param:

    def __init__(self, type: str, name: str, archDSL_Param: "archDSL_SuperMethod" = None):
        self.type = type
        self.name = name
        self.archDSL_Param = archDSL_Param
        
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
    def archDSL_Param(self):
        return self.__archDSL_Param

    @archDSL_Param.setter
    def archDSL_Param(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archDSL_Param__archDSL_Param", None)
        self.__archDSL_Param = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "archDSL_SuperMethod"):
                opp_val = getattr(old_value, "archDSL_SuperMethod", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "archDSL_SuperMethod"):
                opp_val = getattr(value, "archDSL_SuperMethod", None)
                if opp_val is None:
                    setattr(value, "archDSL_SuperMethod", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class SuperMethod:

    pass
class archDSL_Method(SuperMethod):

    def __init__(self, type: str, archDSL_Method: "archDSL_Interface" = None, archDSL_Method31: "archDSL_Behavior" = None):
        self.type = type
        self.archDSL_Method = archDSL_Method
        self.archDSL_Method31 = archDSL_Method31
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def archDSL_Method(self):
        return self.__archDSL_Method

    @archDSL_Method.setter
    def archDSL_Method(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archDSL_Method__archDSL_Method", None)
        self.__archDSL_Method = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "archDSL_Interface17"):
                opp_val = getattr(old_value, "archDSL_Interface17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "archDSL_Interface17"):
                opp_val = getattr(value, "archDSL_Interface17", None)
                if opp_val is None:
                    setattr(value, "archDSL_Interface17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def archDSL_Method31(self):
        return self.__archDSL_Method31

    @archDSL_Method31.setter
    def archDSL_Method31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archDSL_Method__archDSL_Method31", None)
        self.__archDSL_Method31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "archDSL_Behavior30"):
                opp_val = getattr(old_value, "archDSL_Behavior30", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "archDSL_Behavior30"):
                opp_val = getattr(value, "archDSL_Behavior30", None)
                if opp_val is None:
                    setattr(value, "archDSL_Behavior30", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class archDSL_OptMethod(SuperMethod):

    def __init__(self, type: str, archDSL_OptMethod: "archDSL_UncertainInterface" = None):
        self.type = type
        self.archDSL_OptMethod = archDSL_OptMethod
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def archDSL_OptMethod(self):
        return self.__archDSL_OptMethod

    @archDSL_OptMethod.setter
    def archDSL_OptMethod(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archDSL_OptMethod__archDSL_OptMethod", None)
        self.__archDSL_OptMethod = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "archDSL_UncertainInterface15"):
                opp_val = getattr(old_value, "archDSL_UncertainInterface15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "archDSL_UncertainInterface15"):
                opp_val = getattr(value, "archDSL_UncertainInterface15", None)
                if opp_val is None:
                    setattr(value, "archDSL_UncertainInterface15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class archDSL_AltMethod(SuperMethod):

    def __init__(self, type: str, a_name: str, archDSL_AltMethod: "archDSL_UncertainInterface" = None):
        self.type = type
        self.a_name = a_name
        self.archDSL_AltMethod = archDSL_AltMethod
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def a_name(self) -> str:
        return self.__a_name

    @a_name.setter
    def a_name(self, a_name: str):
        self.__a_name = a_name

    @property
    def archDSL_AltMethod(self):
        return self.__archDSL_AltMethod

    @archDSL_AltMethod.setter
    def archDSL_AltMethod(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archDSL_AltMethod__archDSL_AltMethod", None)
        self.__archDSL_AltMethod = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "archDSL_UncertainInterface13"):
                opp_val = getattr(old_value, "archDSL_UncertainInterface13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "archDSL_UncertainInterface13"):
                opp_val = getattr(value, "archDSL_UncertainInterface13", None)
                if opp_val is None:
                    setattr(value, "archDSL_UncertainInterface13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class archDSL_SuperMethod:

    def __init__(self, name: str, archDSL_SuperMethod: set["archDSL_Param"] = None, archDSL_SuperMethod42: "archDSL_AltCall" = None, archDSL_SuperMethod45: "archDSL_SuperCall" = None):
        self.name = name
        self.archDSL_SuperMethod = archDSL_SuperMethod if archDSL_SuperMethod is not None else set()
        self.archDSL_SuperMethod42 = archDSL_SuperMethod42
        self.archDSL_SuperMethod45 = archDSL_SuperMethod45
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def archDSL_SuperMethod42(self):
        return self.__archDSL_SuperMethod42

    @archDSL_SuperMethod42.setter
    def archDSL_SuperMethod42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archDSL_SuperMethod__archDSL_SuperMethod42", None)
        self.__archDSL_SuperMethod42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "archDSL_AltCall"):
                opp_val = getattr(old_value, "archDSL_AltCall", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "archDSL_AltCall"):
                opp_val = getattr(value, "archDSL_AltCall", None)
                if opp_val is None:
                    setattr(value, "archDSL_AltCall", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def archDSL_SuperMethod(self):
        return self.__archDSL_SuperMethod

    @archDSL_SuperMethod.setter
    def archDSL_SuperMethod(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archDSL_SuperMethod__archDSL_SuperMethod", None)
        self.__archDSL_SuperMethod = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "archDSL_Param"):
                    opp_val = getattr(item, "archDSL_Param", None)
                    
                    if opp_val == self:
                        setattr(item, "archDSL_Param", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "archDSL_Param"):
                    opp_val = getattr(item, "archDSL_Param", None)
                    
                    setattr(item, "archDSL_Param", self)
                    

    @property
    def archDSL_SuperMethod45(self):
        return self.__archDSL_SuperMethod45

    @archDSL_SuperMethod45.setter
    def archDSL_SuperMethod45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archDSL_SuperMethod__archDSL_SuperMethod45", None)
        self.__archDSL_SuperMethod45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "archDSL_SuperCall44"):
                opp_val = getattr(old_value, "archDSL_SuperCall44", None)
                if opp_val == self:
                    setattr(old_value, "archDSL_SuperCall44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "archDSL_SuperCall44"):
                opp_val = getattr(value, "archDSL_SuperCall44", None)
                setattr(value, "archDSL_SuperCall44", self)

class archDSL_Behavior:

    pass
class archDSL_UncertainInterface:

    def __init__(self, name: str, archDSL_UncertainInterface10: "archDSL_Interface" = None, archDSL_UncertainInterface: "archDSL_Model" = None, archDSL_UncertainInterface13: set["archDSL_AltMethod"] = None, archDSL_UncertainInterface15: set["archDSL_OptMethod"] = None):
        self.name = name
        self.archDSL_UncertainInterface10 = archDSL_UncertainInterface10
        self.archDSL_UncertainInterface = archDSL_UncertainInterface
        self.archDSL_UncertainInterface13 = archDSL_UncertainInterface13 if archDSL_UncertainInterface13 is not None else set()
        self.archDSL_UncertainInterface15 = archDSL_UncertainInterface15 if archDSL_UncertainInterface15 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def archDSL_UncertainInterface(self):
        return self.__archDSL_UncertainInterface

    @archDSL_UncertainInterface.setter
    def archDSL_UncertainInterface(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archDSL_UncertainInterface__archDSL_UncertainInterface", None)
        self.__archDSL_UncertainInterface = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "archDSL_Model2"):
                opp_val = getattr(old_value, "archDSL_Model2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "archDSL_Model2"):
                opp_val = getattr(value, "archDSL_Model2", None)
                if opp_val is None:
                    setattr(value, "archDSL_Model2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def archDSL_UncertainInterface15(self):
        return self.__archDSL_UncertainInterface15

    @archDSL_UncertainInterface15.setter
    def archDSL_UncertainInterface15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archDSL_UncertainInterface__archDSL_UncertainInterface15", None)
        self.__archDSL_UncertainInterface15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "archDSL_OptMethod"):
                    opp_val = getattr(item, "archDSL_OptMethod", None)
                    
                    if opp_val == self:
                        setattr(item, "archDSL_OptMethod", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "archDSL_OptMethod"):
                    opp_val = getattr(item, "archDSL_OptMethod", None)
                    
                    setattr(item, "archDSL_OptMethod", self)
                    

    @property
    def archDSL_UncertainInterface10(self):
        return self.__archDSL_UncertainInterface10

    @archDSL_UncertainInterface10.setter
    def archDSL_UncertainInterface10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archDSL_UncertainInterface__archDSL_UncertainInterface10", None)
        self.__archDSL_UncertainInterface10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "archDSL_Interface11"):
                opp_val = getattr(old_value, "archDSL_Interface11", None)
                if opp_val == self:
                    setattr(old_value, "archDSL_Interface11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "archDSL_Interface11"):
                opp_val = getattr(value, "archDSL_Interface11", None)
                setattr(value, "archDSL_Interface11", self)

    @property
    def archDSL_UncertainInterface13(self):
        return self.__archDSL_UncertainInterface13

    @archDSL_UncertainInterface13.setter
    def archDSL_UncertainInterface13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archDSL_UncertainInterface__archDSL_UncertainInterface13", None)
        self.__archDSL_UncertainInterface13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "archDSL_AltMethod"):
                    opp_val = getattr(item, "archDSL_AltMethod", None)
                    
                    if opp_val == self:
                        setattr(item, "archDSL_AltMethod", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "archDSL_AltMethod"):
                    opp_val = getattr(item, "archDSL_AltMethod", None)
                    
                    setattr(item, "archDSL_AltMethod", self)
                    

class archDSL_Interface:

    def __init__(self, name: str, archDSL_Interface11: "archDSL_UncertainInterface" = None, archDSL_Interface: "archDSL_Model" = None, archDSL_Interface34: "archDSL_Behavior" = None, archDSL_Interface17: set["archDSL_Method"] = None, archDSL_Interface23: "archDSL_UncertainConnector" = None, archDSL_Interface28: "archDSL_Behavior" = None, archDSL_Interface40: "archDSL_UncertainBehavior" = None):
        self.name = name
        self.archDSL_Interface11 = archDSL_Interface11
        self.archDSL_Interface = archDSL_Interface
        self.archDSL_Interface34 = archDSL_Interface34
        self.archDSL_Interface17 = archDSL_Interface17 if archDSL_Interface17 is not None else set()
        self.archDSL_Interface23 = archDSL_Interface23
        self.archDSL_Interface28 = archDSL_Interface28
        self.archDSL_Interface40 = archDSL_Interface40
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def archDSL_Interface(self):
        return self.__archDSL_Interface

    @archDSL_Interface.setter
    def archDSL_Interface(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archDSL_Interface__archDSL_Interface", None)
        self.__archDSL_Interface = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "archDSL_Model"):
                opp_val = getattr(old_value, "archDSL_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "archDSL_Model"):
                opp_val = getattr(value, "archDSL_Model", None)
                if opp_val is None:
                    setattr(value, "archDSL_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def archDSL_Interface28(self):
        return self.__archDSL_Interface28

    @archDSL_Interface28.setter
    def archDSL_Interface28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archDSL_Interface__archDSL_Interface28", None)
        self.__archDSL_Interface28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "archDSL_Behavior27"):
                opp_val = getattr(old_value, "archDSL_Behavior27", None)
                if opp_val == self:
                    setattr(old_value, "archDSL_Behavior27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "archDSL_Behavior27"):
                opp_val = getattr(value, "archDSL_Behavior27", None)
                setattr(value, "archDSL_Behavior27", self)

    @property
    def archDSL_Interface40(self):
        return self.__archDSL_Interface40

    @archDSL_Interface40.setter
    def archDSL_Interface40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archDSL_Interface__archDSL_Interface40", None)
        self.__archDSL_Interface40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "archDSL_UncertainBehavior39"):
                opp_val = getattr(old_value, "archDSL_UncertainBehavior39", None)
                if opp_val == self:
                    setattr(old_value, "archDSL_UncertainBehavior39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "archDSL_UncertainBehavior39"):
                opp_val = getattr(value, "archDSL_UncertainBehavior39", None)
                setattr(value, "archDSL_UncertainBehavior39", self)

    @property
    def archDSL_Interface11(self):
        return self.__archDSL_Interface11

    @archDSL_Interface11.setter
    def archDSL_Interface11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archDSL_Interface__archDSL_Interface11", None)
        self.__archDSL_Interface11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "archDSL_UncertainInterface10"):
                opp_val = getattr(old_value, "archDSL_UncertainInterface10", None)
                if opp_val == self:
                    setattr(old_value, "archDSL_UncertainInterface10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "archDSL_UncertainInterface10"):
                opp_val = getattr(value, "archDSL_UncertainInterface10", None)
                setattr(value, "archDSL_UncertainInterface10", self)

    @property
    def archDSL_Interface34(self):
        return self.__archDSL_Interface34

    @archDSL_Interface34.setter
    def archDSL_Interface34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archDSL_Interface__archDSL_Interface34", None)
        self.__archDSL_Interface34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "archDSL_Behavior33"):
                opp_val = getattr(old_value, "archDSL_Behavior33", None)
                if opp_val == self:
                    setattr(old_value, "archDSL_Behavior33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "archDSL_Behavior33"):
                opp_val = getattr(value, "archDSL_Behavior33", None)
                setattr(value, "archDSL_Behavior33", self)

    @property
    def archDSL_Interface23(self):
        return self.__archDSL_Interface23

    @archDSL_Interface23.setter
    def archDSL_Interface23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archDSL_Interface__archDSL_Interface23", None)
        self.__archDSL_Interface23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "archDSL_UncertainConnector22"):
                opp_val = getattr(old_value, "archDSL_UncertainConnector22", None)
                if opp_val == self:
                    setattr(old_value, "archDSL_UncertainConnector22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "archDSL_UncertainConnector22"):
                opp_val = getattr(value, "archDSL_UncertainConnector22", None)
                setattr(value, "archDSL_UncertainConnector22", self)

    @property
    def archDSL_Interface17(self):
        return self.__archDSL_Interface17

    @archDSL_Interface17.setter
    def archDSL_Interface17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archDSL_Interface__archDSL_Interface17", None)
        self.__archDSL_Interface17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "archDSL_Method"):
                    opp_val = getattr(item, "archDSL_Method", None)
                    
                    if opp_val == self:
                        setattr(item, "archDSL_Method", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "archDSL_Method"):
                    opp_val = getattr(item, "archDSL_Method", None)
                    
                    setattr(item, "archDSL_Method", self)
                    

class archDSL_Model:

    pass
class archDSL_Connector:

    def __init__(self, name: str, archDSL_Connector: "archDSL_Model" = None, archDSL_Connector19: set["archDSL_Behavior"] = None):
        self.name = name
        self.archDSL_Connector = archDSL_Connector
        self.archDSL_Connector19 = archDSL_Connector19 if archDSL_Connector19 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def archDSL_Connector(self):
        return self.__archDSL_Connector

    @archDSL_Connector.setter
    def archDSL_Connector(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archDSL_Connector__archDSL_Connector", None)
        self.__archDSL_Connector = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "archDSL_Model8"):
                opp_val = getattr(old_value, "archDSL_Model8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "archDSL_Model8"):
                opp_val = getattr(value, "archDSL_Model8", None)
                if opp_val is None:
                    setattr(value, "archDSL_Model8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def archDSL_Connector19(self):
        return self.__archDSL_Connector19

    @archDSL_Connector19.setter
    def archDSL_Connector19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archDSL_Connector__archDSL_Connector19", None)
        self.__archDSL_Connector19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "archDSL_Behavior20"):
                    opp_val = getattr(item, "archDSL_Behavior20", None)
                    
                    if opp_val == self:
                        setattr(item, "archDSL_Behavior20", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "archDSL_Behavior20"):
                    opp_val = getattr(item, "archDSL_Behavior20", None)
                    
                    setattr(item, "archDSL_Behavior20", self)
                    

class archDSL_UncertainConnector:

    def __init__(self, name: str, archDSL_UncertainConnector: "archDSL_Model" = None, archDSL_UncertainConnector22: "archDSL_Interface" = None, archDSL_UncertainConnector25: set["archDSL_UncertainBehavior"] = None):
        self.name = name
        self.archDSL_UncertainConnector = archDSL_UncertainConnector
        self.archDSL_UncertainConnector22 = archDSL_UncertainConnector22
        self.archDSL_UncertainConnector25 = archDSL_UncertainConnector25 if archDSL_UncertainConnector25 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def archDSL_UncertainConnector(self):
        return self.__archDSL_UncertainConnector

    @archDSL_UncertainConnector.setter
    def archDSL_UncertainConnector(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archDSL_UncertainConnector__archDSL_UncertainConnector", None)
        self.__archDSL_UncertainConnector = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "archDSL_Model6"):
                opp_val = getattr(old_value, "archDSL_Model6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "archDSL_Model6"):
                opp_val = getattr(value, "archDSL_Model6", None)
                if opp_val is None:
                    setattr(value, "archDSL_Model6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def archDSL_UncertainConnector22(self):
        return self.__archDSL_UncertainConnector22

    @archDSL_UncertainConnector22.setter
    def archDSL_UncertainConnector22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archDSL_UncertainConnector__archDSL_UncertainConnector22", None)
        self.__archDSL_UncertainConnector22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "archDSL_Interface23"):
                opp_val = getattr(old_value, "archDSL_Interface23", None)
                if opp_val == self:
                    setattr(old_value, "archDSL_Interface23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "archDSL_Interface23"):
                opp_val = getattr(value, "archDSL_Interface23", None)
                setattr(value, "archDSL_Interface23", self)

    @property
    def archDSL_UncertainConnector25(self):
        return self.__archDSL_UncertainConnector25

    @archDSL_UncertainConnector25.setter
    def archDSL_UncertainConnector25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archDSL_UncertainConnector__archDSL_UncertainConnector25", None)
        self.__archDSL_UncertainConnector25 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "archDSL_UncertainBehavior"):
                    opp_val = getattr(item, "archDSL_UncertainBehavior", None)
                    
                    if opp_val == self:
                        setattr(item, "archDSL_UncertainBehavior", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "archDSL_UncertainBehavior"):
                    opp_val = getattr(item, "archDSL_UncertainBehavior", None)
                    
                    setattr(item, "archDSL_UncertainBehavior", self)
                    
