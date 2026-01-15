from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Uppaal_TransitionType:

    def __init__(self, color: str, id: str, x: str, y: str, Uppaal_TransitionType: "Uppaal_DocumentRoot" = None, Uppaal_TransitionType83: set["Uppaal_NailType"] = None, Uppaal_TransitionType72: "Uppaal_TemplateType" = None, Uppaal_TransitionType74: "Uppaal_SourceType" = None, Uppaal_TransitionType77: "Uppaal_TargetType" = None, Uppaal_TransitionType80: set["Uppaal_LabelType"] = None):
        self.color = color
        self.id = id
        self.x = x
        self.y = y
        self.Uppaal_TransitionType = Uppaal_TransitionType
        self.Uppaal_TransitionType83 = Uppaal_TransitionType83 if Uppaal_TransitionType83 is not None else set()
        self.Uppaal_TransitionType72 = Uppaal_TransitionType72
        self.Uppaal_TransitionType74 = Uppaal_TransitionType74
        self.Uppaal_TransitionType77 = Uppaal_TransitionType77
        self.Uppaal_TransitionType80 = Uppaal_TransitionType80 if Uppaal_TransitionType80 is not None else set()
        
    @property
    def x(self) -> str:
        return self.__x

    @x.setter
    def x(self, x: str):
        self.__x = x

    @property
    def y(self) -> str:
        return self.__y

    @y.setter
    def y(self, y: str):
        self.__y = y

    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def Uppaal_TransitionType80(self):
        return self.__Uppaal_TransitionType80

    @Uppaal_TransitionType80.setter
    def Uppaal_TransitionType80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Uppaal_TransitionType__Uppaal_TransitionType80", None)
        self.__Uppaal_TransitionType80 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Uppaal_LabelType81"):
                    opp_val = getattr(item, "Uppaal_LabelType81", None)
                    
                    if opp_val == self:
                        setattr(item, "Uppaal_LabelType81", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Uppaal_LabelType81"):
                    opp_val = getattr(item, "Uppaal_LabelType81", None)
                    
                    setattr(item, "Uppaal_LabelType81", self)
                    

    @property
    def Uppaal_TransitionType74(self):
        return self.__Uppaal_TransitionType74

    @Uppaal_TransitionType74.setter
    def Uppaal_TransitionType74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Uppaal_TransitionType__Uppaal_TransitionType74", None)
        self.__Uppaal_TransitionType74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Uppaal_SourceType75"):
                opp_val = getattr(old_value, "Uppaal_SourceType75", None)
                if opp_val == self:
                    setattr(old_value, "Uppaal_SourceType75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Uppaal_SourceType75"):
                opp_val = getattr(value, "Uppaal_SourceType75", None)
                setattr(value, "Uppaal_SourceType75", self)

    @property
    def Uppaal_TransitionType72(self):
        return self.__Uppaal_TransitionType72

    @Uppaal_TransitionType72.setter
    def Uppaal_TransitionType72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Uppaal_TransitionType__Uppaal_TransitionType72", None)
        self.__Uppaal_TransitionType72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Uppaal_TemplateType71"):
                opp_val = getattr(old_value, "Uppaal_TemplateType71", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Uppaal_TemplateType71"):
                opp_val = getattr(value, "Uppaal_TemplateType71", None)
                if opp_val is None:
                    setattr(value, "Uppaal_TemplateType71", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Uppaal_TransitionType(self):
        return self.__Uppaal_TransitionType

    @Uppaal_TransitionType.setter
    def Uppaal_TransitionType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Uppaal_TransitionType__Uppaal_TransitionType", None)
        self.__Uppaal_TransitionType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Uppaal_DocumentRoot33"):
                opp_val = getattr(old_value, "Uppaal_DocumentRoot33", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Uppaal_DocumentRoot33"):
                opp_val = getattr(value, "Uppaal_DocumentRoot33", None)
                if opp_val is None:
                    setattr(value, "Uppaal_DocumentRoot33", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Uppaal_TransitionType83(self):
        return self.__Uppaal_TransitionType83

    @Uppaal_TransitionType83.setter
    def Uppaal_TransitionType83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Uppaal_TransitionType__Uppaal_TransitionType83", None)
        self.__Uppaal_TransitionType83 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Uppaal_NailType84"):
                    opp_val = getattr(item, "Uppaal_NailType84", None)
                    
                    if opp_val == self:
                        setattr(item, "Uppaal_NailType84", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Uppaal_NailType84"):
                    opp_val = getattr(item, "Uppaal_NailType84", None)
                    
                    setattr(item, "Uppaal_NailType84", self)
                    

    @property
    def Uppaal_TransitionType77(self):
        return self.__Uppaal_TransitionType77

    @Uppaal_TransitionType77.setter
    def Uppaal_TransitionType77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Uppaal_TransitionType__Uppaal_TransitionType77", None)
        self.__Uppaal_TransitionType77 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Uppaal_TargetType78"):
                opp_val = getattr(old_value, "Uppaal_TargetType78", None)
                if opp_val == self:
                    setattr(old_value, "Uppaal_TargetType78", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Uppaal_TargetType78"):
                opp_val = getattr(value, "Uppaal_TargetType78", None)
                setattr(value, "Uppaal_TargetType78", self)

class Uppaal_TemplateType:

    pass
class Uppaal_TargetType:

    def __init__(self, ref: str, Uppaal_TargetType: "Uppaal_DocumentRoot" = None, Uppaal_TargetType78: "Uppaal_TransitionType" = None):
        self.ref = ref
        self.Uppaal_TargetType = Uppaal_TargetType
        self.Uppaal_TargetType78 = Uppaal_TargetType78
        
    @property
    def ref(self) -> str:
        return self.__ref

    @ref.setter
    def ref(self, ref: str):
        self.__ref = ref

    @property
    def Uppaal_TargetType78(self):
        return self.__Uppaal_TargetType78

    @Uppaal_TargetType78.setter
    def Uppaal_TargetType78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Uppaal_TargetType__Uppaal_TargetType78", None)
        self.__Uppaal_TargetType78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Uppaal_TransitionType77"):
                opp_val = getattr(old_value, "Uppaal_TransitionType77", None)
                if opp_val == self:
                    setattr(old_value, "Uppaal_TransitionType77", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Uppaal_TransitionType77"):
                opp_val = getattr(value, "Uppaal_TransitionType77", None)
                setattr(value, "Uppaal_TransitionType77", self)

    @property
    def Uppaal_TargetType(self):
        return self.__Uppaal_TargetType

    @Uppaal_TargetType.setter
    def Uppaal_TargetType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Uppaal_TargetType__Uppaal_TargetType", None)
        self.__Uppaal_TargetType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Uppaal_DocumentRoot29"):
                opp_val = getattr(old_value, "Uppaal_DocumentRoot29", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Uppaal_DocumentRoot29"):
                opp_val = getattr(value, "Uppaal_DocumentRoot29", None)
                if opp_val is None:
                    setattr(value, "Uppaal_DocumentRoot29", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Uppaal_SystemType:

    def __init__(self, mixed: str, Uppaal_SystemType: "Uppaal_DocumentRoot" = None, Uppaal_SystemType54: "Uppaal_NtaType" = None):
        self.mixed = mixed
        self.Uppaal_SystemType = Uppaal_SystemType
        self.Uppaal_SystemType54 = Uppaal_SystemType54
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def Uppaal_SystemType(self):
        return self.__Uppaal_SystemType

    @Uppaal_SystemType.setter
    def Uppaal_SystemType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Uppaal_SystemType__Uppaal_SystemType", None)
        self.__Uppaal_SystemType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Uppaal_DocumentRoot27"):
                opp_val = getattr(old_value, "Uppaal_DocumentRoot27", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Uppaal_DocumentRoot27"):
                opp_val = getattr(value, "Uppaal_DocumentRoot27", None)
                if opp_val is None:
                    setattr(value, "Uppaal_DocumentRoot27", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Uppaal_SystemType54(self):
        return self.__Uppaal_SystemType54

    @Uppaal_SystemType54.setter
    def Uppaal_SystemType54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Uppaal_SystemType__Uppaal_SystemType54", None)
        self.__Uppaal_SystemType54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Uppaal_NtaType53"):
                opp_val = getattr(old_value, "Uppaal_NtaType53", None)
                if opp_val == self:
                    setattr(old_value, "Uppaal_NtaType53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Uppaal_NtaType53"):
                opp_val = getattr(value, "Uppaal_NtaType53", None)
                setattr(value, "Uppaal_NtaType53", self)

class Uppaal_SourceType:

    def __init__(self, ref: str, Uppaal_SourceType: "Uppaal_DocumentRoot" = None, Uppaal_SourceType75: "Uppaal_TransitionType" = None):
        self.ref = ref
        self.Uppaal_SourceType = Uppaal_SourceType
        self.Uppaal_SourceType75 = Uppaal_SourceType75
        
    @property
    def ref(self) -> str:
        return self.__ref

    @ref.setter
    def ref(self, ref: str):
        self.__ref = ref

    @property
    def Uppaal_SourceType75(self):
        return self.__Uppaal_SourceType75

    @Uppaal_SourceType75.setter
    def Uppaal_SourceType75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Uppaal_SourceType__Uppaal_SourceType75", None)
        self.__Uppaal_SourceType75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Uppaal_TransitionType74"):
                opp_val = getattr(old_value, "Uppaal_TransitionType74", None)
                if opp_val == self:
                    setattr(old_value, "Uppaal_TransitionType74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Uppaal_TransitionType74"):
                opp_val = getattr(value, "Uppaal_TransitionType74", None)
                setattr(value, "Uppaal_TransitionType74", self)

    @property
    def Uppaal_SourceType(self):
        return self.__Uppaal_SourceType

    @Uppaal_SourceType.setter
    def Uppaal_SourceType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Uppaal_SourceType__Uppaal_SourceType", None)
        self.__Uppaal_SourceType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Uppaal_DocumentRoot25"):
                opp_val = getattr(old_value, "Uppaal_DocumentRoot25", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Uppaal_DocumentRoot25"):
                opp_val = getattr(value, "Uppaal_DocumentRoot25", None)
                if opp_val is None:
                    setattr(value, "Uppaal_DocumentRoot25", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Uppaal_NtaType:

    pass
class Uppaal_NameType:

    def __init__(self, mixed: str, x: str, y: str, Uppaal_NameType: "Uppaal_DocumentRoot" = None, Uppaal_NameType36: "Uppaal_LocationType" = None, Uppaal_NameType57: "Uppaal_TemplateType" = None):
        self.mixed = mixed
        self.x = x
        self.y = y
        self.Uppaal_NameType = Uppaal_NameType
        self.Uppaal_NameType36 = Uppaal_NameType36
        self.Uppaal_NameType57 = Uppaal_NameType57
        
    @property
    def y(self) -> str:
        return self.__y

    @y.setter
    def y(self, y: str):
        self.__y = y

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def x(self) -> str:
        return self.__x

    @x.setter
    def x(self, x: str):
        self.__x = x

    @property
    def Uppaal_NameType57(self):
        return self.__Uppaal_NameType57

    @Uppaal_NameType57.setter
    def Uppaal_NameType57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Uppaal_NameType__Uppaal_NameType57", None)
        self.__Uppaal_NameType57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Uppaal_TemplateType56"):
                opp_val = getattr(old_value, "Uppaal_TemplateType56", None)
                if opp_val == self:
                    setattr(old_value, "Uppaal_TemplateType56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Uppaal_TemplateType56"):
                opp_val = getattr(value, "Uppaal_TemplateType56", None)
                setattr(value, "Uppaal_TemplateType56", self)

    @property
    def Uppaal_NameType36(self):
        return self.__Uppaal_NameType36

    @Uppaal_NameType36.setter
    def Uppaal_NameType36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Uppaal_NameType__Uppaal_NameType36", None)
        self.__Uppaal_NameType36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Uppaal_LocationType35"):
                opp_val = getattr(old_value, "Uppaal_LocationType35", None)
                if opp_val == self:
                    setattr(old_value, "Uppaal_LocationType35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Uppaal_LocationType35"):
                opp_val = getattr(value, "Uppaal_LocationType35", None)
                setattr(value, "Uppaal_LocationType35", self)

    @property
    def Uppaal_NameType(self):
        return self.__Uppaal_NameType

    @Uppaal_NameType.setter
    def Uppaal_NameType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Uppaal_NameType__Uppaal_NameType", None)
        self.__Uppaal_NameType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Uppaal_DocumentRoot19"):
                opp_val = getattr(old_value, "Uppaal_DocumentRoot19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Uppaal_DocumentRoot19"):
                opp_val = getattr(value, "Uppaal_DocumentRoot19", None)
                if opp_val is None:
                    setattr(value, "Uppaal_DocumentRoot19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Uppaal_NailType:

    def __init__(self, x: str, y: str, Uppaal_NailType: "Uppaal_DocumentRoot" = None, Uppaal_NailType84: "Uppaal_TransitionType" = None):
        self.x = x
        self.y = y
        self.Uppaal_NailType = Uppaal_NailType
        self.Uppaal_NailType84 = Uppaal_NailType84
        
    @property
    def y(self) -> str:
        return self.__y

    @y.setter
    def y(self, y: str):
        self.__y = y

    @property
    def x(self) -> str:
        return self.__x

    @x.setter
    def x(self, x: str):
        self.__x = x

    @property
    def Uppaal_NailType(self):
        return self.__Uppaal_NailType

    @Uppaal_NailType.setter
    def Uppaal_NailType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Uppaal_NailType__Uppaal_NailType", None)
        self.__Uppaal_NailType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Uppaal_DocumentRoot17"):
                opp_val = getattr(old_value, "Uppaal_DocumentRoot17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Uppaal_DocumentRoot17"):
                opp_val = getattr(value, "Uppaal_DocumentRoot17", None)
                if opp_val is None:
                    setattr(value, "Uppaal_DocumentRoot17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Uppaal_NailType84(self):
        return self.__Uppaal_NailType84

    @Uppaal_NailType84.setter
    def Uppaal_NailType84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Uppaal_NailType__Uppaal_NailType84", None)
        self.__Uppaal_NailType84 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Uppaal_TransitionType83"):
                opp_val = getattr(old_value, "Uppaal_TransitionType83", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Uppaal_TransitionType83"):
                opp_val = getattr(value, "Uppaal_TransitionType83", None)
                if opp_val is None:
                    setattr(value, "Uppaal_TransitionType83", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Uppaal_LocationType:

    def __init__(self, committed: str, color: str, urgent: str, id: str, x: str, y: str, Uppaal_LocationType: "Uppaal_DocumentRoot" = None, Uppaal_LocationType35: "Uppaal_NameType" = None, Uppaal_LocationType38: set["Uppaal_LabelType"] = None, Uppaal_LocationType66: "Uppaal_TemplateType" = None):
        self.committed = committed
        self.color = color
        self.urgent = urgent
        self.id = id
        self.x = x
        self.y = y
        self.Uppaal_LocationType = Uppaal_LocationType
        self.Uppaal_LocationType35 = Uppaal_LocationType35
        self.Uppaal_LocationType38 = Uppaal_LocationType38 if Uppaal_LocationType38 is not None else set()
        self.Uppaal_LocationType66 = Uppaal_LocationType66
        
    @property
    def y(self) -> str:
        return self.__y

    @y.setter
    def y(self, y: str):
        self.__y = y

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def x(self) -> str:
        return self.__x

    @x.setter
    def x(self, x: str):
        self.__x = x

    @property
    def urgent(self) -> str:
        return self.__urgent

    @urgent.setter
    def urgent(self, urgent: str):
        self.__urgent = urgent

    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color

    @property
    def committed(self) -> str:
        return self.__committed

    @committed.setter
    def committed(self, committed: str):
        self.__committed = committed

    @property
    def Uppaal_LocationType35(self):
        return self.__Uppaal_LocationType35

    @Uppaal_LocationType35.setter
    def Uppaal_LocationType35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Uppaal_LocationType__Uppaal_LocationType35", None)
        self.__Uppaal_LocationType35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Uppaal_NameType36"):
                opp_val = getattr(old_value, "Uppaal_NameType36", None)
                if opp_val == self:
                    setattr(old_value, "Uppaal_NameType36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Uppaal_NameType36"):
                opp_val = getattr(value, "Uppaal_NameType36", None)
                setattr(value, "Uppaal_NameType36", self)

    @property
    def Uppaal_LocationType38(self):
        return self.__Uppaal_LocationType38

    @Uppaal_LocationType38.setter
    def Uppaal_LocationType38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Uppaal_LocationType__Uppaal_LocationType38", None)
        self.__Uppaal_LocationType38 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Uppaal_LabelType39"):
                    opp_val = getattr(item, "Uppaal_LabelType39", None)
                    
                    if opp_val == self:
                        setattr(item, "Uppaal_LabelType39", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Uppaal_LabelType39"):
                    opp_val = getattr(item, "Uppaal_LabelType39", None)
                    
                    setattr(item, "Uppaal_LabelType39", self)
                    

    @property
    def Uppaal_LocationType66(self):
        return self.__Uppaal_LocationType66

    @Uppaal_LocationType66.setter
    def Uppaal_LocationType66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Uppaal_LocationType__Uppaal_LocationType66", None)
        self.__Uppaal_LocationType66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Uppaal_TemplateType65"):
                opp_val = getattr(old_value, "Uppaal_TemplateType65", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Uppaal_TemplateType65"):
                opp_val = getattr(value, "Uppaal_TemplateType65", None)
                if opp_val is None:
                    setattr(value, "Uppaal_TemplateType65", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Uppaal_LocationType(self):
        return self.__Uppaal_LocationType

    @Uppaal_LocationType.setter
    def Uppaal_LocationType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Uppaal_LocationType__Uppaal_LocationType", None)
        self.__Uppaal_LocationType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Uppaal_DocumentRoot15"):
                opp_val = getattr(old_value, "Uppaal_DocumentRoot15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Uppaal_DocumentRoot15"):
                opp_val = getattr(value, "Uppaal_DocumentRoot15", None)
                if opp_val is None:
                    setattr(value, "Uppaal_DocumentRoot15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Uppaal_LabelType:

    def __init__(self, mixed: str, kind: str, x: str, y: str, Uppaal_LabelType: "Uppaal_DocumentRoot" = None, Uppaal_LabelType39: "Uppaal_LocationType" = None, Uppaal_LabelType81: "Uppaal_TransitionType" = None):
        self.mixed = mixed
        self.kind = kind
        self.x = x
        self.y = y
        self.Uppaal_LabelType = Uppaal_LabelType
        self.Uppaal_LabelType39 = Uppaal_LabelType39
        self.Uppaal_LabelType81 = Uppaal_LabelType81
        
    @property
    def x(self) -> str:
        return self.__x

    @x.setter
    def x(self, x: str):
        self.__x = x

    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def y(self) -> str:
        return self.__y

    @y.setter
    def y(self, y: str):
        self.__y = y

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def Uppaal_LabelType39(self):
        return self.__Uppaal_LabelType39

    @Uppaal_LabelType39.setter
    def Uppaal_LabelType39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Uppaal_LabelType__Uppaal_LabelType39", None)
        self.__Uppaal_LabelType39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Uppaal_LocationType38"):
                opp_val = getattr(old_value, "Uppaal_LocationType38", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Uppaal_LocationType38"):
                opp_val = getattr(value, "Uppaal_LocationType38", None)
                if opp_val is None:
                    setattr(value, "Uppaal_LocationType38", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Uppaal_LabelType(self):
        return self.__Uppaal_LabelType

    @Uppaal_LabelType.setter
    def Uppaal_LabelType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Uppaal_LabelType__Uppaal_LabelType", None)
        self.__Uppaal_LabelType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Uppaal_DocumentRoot13"):
                opp_val = getattr(old_value, "Uppaal_DocumentRoot13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Uppaal_DocumentRoot13"):
                opp_val = getattr(value, "Uppaal_DocumentRoot13", None)
                if opp_val is None:
                    setattr(value, "Uppaal_DocumentRoot13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Uppaal_LabelType81(self):
        return self.__Uppaal_LabelType81

    @Uppaal_LabelType81.setter
    def Uppaal_LabelType81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Uppaal_LabelType__Uppaal_LabelType81", None)
        self.__Uppaal_LabelType81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Uppaal_TransitionType80"):
                opp_val = getattr(old_value, "Uppaal_TransitionType80", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Uppaal_TransitionType80"):
                opp_val = getattr(value, "Uppaal_TransitionType80", None)
                if opp_val is None:
                    setattr(value, "Uppaal_TransitionType80", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Uppaal_ParameterType:

    def __init__(self, y: str, mixed: str, x: str, Uppaal_ParameterType: "Uppaal_DocumentRoot" = None, Uppaal_ParameterType60: "Uppaal_TemplateType" = None):
        self.y = y
        self.mixed = mixed
        self.x = x
        self.Uppaal_ParameterType = Uppaal_ParameterType
        self.Uppaal_ParameterType60 = Uppaal_ParameterType60
        
    @property
    def y(self) -> str:
        return self.__y

    @y.setter
    def y(self, y: str):
        self.__y = y

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def x(self) -> str:
        return self.__x

    @x.setter
    def x(self, x: str):
        self.__x = x

    @property
    def Uppaal_ParameterType60(self):
        return self.__Uppaal_ParameterType60

    @Uppaal_ParameterType60.setter
    def Uppaal_ParameterType60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Uppaal_ParameterType__Uppaal_ParameterType60", None)
        self.__Uppaal_ParameterType60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Uppaal_TemplateType59"):
                opp_val = getattr(old_value, "Uppaal_TemplateType59", None)
                if opp_val == self:
                    setattr(old_value, "Uppaal_TemplateType59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Uppaal_TemplateType59"):
                opp_val = getattr(value, "Uppaal_TemplateType59", None)
                setattr(value, "Uppaal_TemplateType59", self)

    @property
    def Uppaal_ParameterType(self):
        return self.__Uppaal_ParameterType

    @Uppaal_ParameterType.setter
    def Uppaal_ParameterType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Uppaal_ParameterType__Uppaal_ParameterType", None)
        self.__Uppaal_ParameterType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Uppaal_DocumentRoot23"):
                opp_val = getattr(old_value, "Uppaal_DocumentRoot23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Uppaal_DocumentRoot23"):
                opp_val = getattr(value, "Uppaal_DocumentRoot23", None)
                if opp_val is None:
                    setattr(value, "Uppaal_DocumentRoot23", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Uppaal_InitType:

    def __init__(self, ref: str, Uppaal_InitType: "Uppaal_DocumentRoot" = None, Uppaal_InitType69: "Uppaal_TemplateType" = None):
        self.ref = ref
        self.Uppaal_InitType = Uppaal_InitType
        self.Uppaal_InitType69 = Uppaal_InitType69
        
    @property
    def ref(self) -> str:
        return self.__ref

    @ref.setter
    def ref(self, ref: str):
        self.__ref = ref

    @property
    def Uppaal_InitType69(self):
        return self.__Uppaal_InitType69

    @Uppaal_InitType69.setter
    def Uppaal_InitType69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Uppaal_InitType__Uppaal_InitType69", None)
        self.__Uppaal_InitType69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Uppaal_TemplateType68"):
                opp_val = getattr(old_value, "Uppaal_TemplateType68", None)
                if opp_val == self:
                    setattr(old_value, "Uppaal_TemplateType68", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Uppaal_TemplateType68"):
                opp_val = getattr(value, "Uppaal_TemplateType68", None)
                setattr(value, "Uppaal_TemplateType68", self)

    @property
    def Uppaal_InitType(self):
        return self.__Uppaal_InitType

    @Uppaal_InitType.setter
    def Uppaal_InitType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Uppaal_InitType__Uppaal_InitType", None)
        self.__Uppaal_InitType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Uppaal_DocumentRoot9"):
                opp_val = getattr(old_value, "Uppaal_DocumentRoot9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Uppaal_DocumentRoot9"):
                opp_val = getattr(value, "Uppaal_DocumentRoot9", None)
                if opp_val is None:
                    setattr(value, "Uppaal_DocumentRoot9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Uppaal_InstantiationType:

    def __init__(self, mixed: str, Uppaal_InstantiationType: "Uppaal_DocumentRoot" = None, Uppaal_InstantiationType51: "Uppaal_NtaType" = None):
        self.mixed = mixed
        self.Uppaal_InstantiationType = Uppaal_InstantiationType
        self.Uppaal_InstantiationType51 = Uppaal_InstantiationType51
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def Uppaal_InstantiationType51(self):
        return self.__Uppaal_InstantiationType51

    @Uppaal_InstantiationType51.setter
    def Uppaal_InstantiationType51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Uppaal_InstantiationType__Uppaal_InstantiationType51", None)
        self.__Uppaal_InstantiationType51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Uppaal_NtaType50"):
                opp_val = getattr(old_value, "Uppaal_NtaType50", None)
                if opp_val == self:
                    setattr(old_value, "Uppaal_NtaType50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Uppaal_NtaType50"):
                opp_val = getattr(value, "Uppaal_NtaType50", None)
                setattr(value, "Uppaal_NtaType50", self)

    @property
    def Uppaal_InstantiationType(self):
        return self.__Uppaal_InstantiationType

    @Uppaal_InstantiationType.setter
    def Uppaal_InstantiationType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Uppaal_InstantiationType__Uppaal_InstantiationType", None)
        self.__Uppaal_InstantiationType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Uppaal_DocumentRoot11"):
                opp_val = getattr(old_value, "Uppaal_DocumentRoot11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Uppaal_DocumentRoot11"):
                opp_val = getattr(value, "Uppaal_DocumentRoot11", None)
                if opp_val is None:
                    setattr(value, "Uppaal_DocumentRoot11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Uppaal_EStringToStringMapEntry:

    pass
class Uppaal_DocumentRoot:

    def __init__(self, mixed: str, committed: str, urgent: str, Uppaal_DocumentRoot7: set["Uppaal_ImportsType"] = None, Uppaal_DocumentRoot: set["Uppaal_EStringToStringMapEntry"] = None, Uppaal_DocumentRoot2: set["Uppaal_EStringToStringMapEntry"] = None, Uppaal_DocumentRoot5: set["Uppaal_DeclarationType"] = None, Uppaal_DocumentRoot11: set["Uppaal_InstantiationType"] = None, Uppaal_DocumentRoot9: set["Uppaal_InitType"] = None, Uppaal_DocumentRoot23: set["Uppaal_ParameterType"] = None, Uppaal_DocumentRoot13: set["Uppaal_LabelType"] = None, Uppaal_DocumentRoot15: set["Uppaal_LocationType"] = None, Uppaal_DocumentRoot17: set["Uppaal_NailType"] = None, Uppaal_DocumentRoot19: set["Uppaal_NameType"] = None, Uppaal_DocumentRoot21: set["Uppaal_NtaType"] = None, Uppaal_DocumentRoot33: set["Uppaal_TransitionType"] = None, Uppaal_DocumentRoot25: set["Uppaal_SourceType"] = None, Uppaal_DocumentRoot27: set["Uppaal_SystemType"] = None, Uppaal_DocumentRoot29: set["Uppaal_TargetType"] = None, Uppaal_DocumentRoot31: set["Uppaal_TemplateType"] = None):
        self.mixed = mixed
        self.committed = committed
        self.urgent = urgent
        self.Uppaal_DocumentRoot7 = Uppaal_DocumentRoot7 if Uppaal_DocumentRoot7 is not None else set()
        self.Uppaal_DocumentRoot = Uppaal_DocumentRoot if Uppaal_DocumentRoot is not None else set()
        self.Uppaal_DocumentRoot2 = Uppaal_DocumentRoot2 if Uppaal_DocumentRoot2 is not None else set()
        self.Uppaal_DocumentRoot5 = Uppaal_DocumentRoot5 if Uppaal_DocumentRoot5 is not None else set()
        self.Uppaal_DocumentRoot11 = Uppaal_DocumentRoot11 if Uppaal_DocumentRoot11 is not None else set()
        self.Uppaal_DocumentRoot9 = Uppaal_DocumentRoot9 if Uppaal_DocumentRoot9 is not None else set()
        self.Uppaal_DocumentRoot23 = Uppaal_DocumentRoot23 if Uppaal_DocumentRoot23 is not None else set()
        self.Uppaal_DocumentRoot13 = Uppaal_DocumentRoot13 if Uppaal_DocumentRoot13 is not None else set()
        self.Uppaal_DocumentRoot15 = Uppaal_DocumentRoot15 if Uppaal_DocumentRoot15 is not None else set()
        self.Uppaal_DocumentRoot17 = Uppaal_DocumentRoot17 if Uppaal_DocumentRoot17 is not None else set()
        self.Uppaal_DocumentRoot19 = Uppaal_DocumentRoot19 if Uppaal_DocumentRoot19 is not None else set()
        self.Uppaal_DocumentRoot21 = Uppaal_DocumentRoot21 if Uppaal_DocumentRoot21 is not None else set()
        self.Uppaal_DocumentRoot33 = Uppaal_DocumentRoot33 if Uppaal_DocumentRoot33 is not None else set()
        self.Uppaal_DocumentRoot25 = Uppaal_DocumentRoot25 if Uppaal_DocumentRoot25 is not None else set()
        self.Uppaal_DocumentRoot27 = Uppaal_DocumentRoot27 if Uppaal_DocumentRoot27 is not None else set()
        self.Uppaal_DocumentRoot29 = Uppaal_DocumentRoot29 if Uppaal_DocumentRoot29 is not None else set()
        self.Uppaal_DocumentRoot31 = Uppaal_DocumentRoot31 if Uppaal_DocumentRoot31 is not None else set()
        
    @property
    def urgent(self) -> str:
        return self.__urgent

    @urgent.setter
    def urgent(self, urgent: str):
        self.__urgent = urgent

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def committed(self) -> str:
        return self.__committed

    @committed.setter
    def committed(self, committed: str):
        self.__committed = committed

    @property
    def Uppaal_DocumentRoot29(self):
        return self.__Uppaal_DocumentRoot29

    @Uppaal_DocumentRoot29.setter
    def Uppaal_DocumentRoot29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Uppaal_DocumentRoot__Uppaal_DocumentRoot29", None)
        self.__Uppaal_DocumentRoot29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Uppaal_TargetType"):
                    opp_val = getattr(item, "Uppaal_TargetType", None)
                    
                    if opp_val == self:
                        setattr(item, "Uppaal_TargetType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Uppaal_TargetType"):
                    opp_val = getattr(item, "Uppaal_TargetType", None)
                    
                    setattr(item, "Uppaal_TargetType", self)
                    

    @property
    def Uppaal_DocumentRoot17(self):
        return self.__Uppaal_DocumentRoot17

    @Uppaal_DocumentRoot17.setter
    def Uppaal_DocumentRoot17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Uppaal_DocumentRoot__Uppaal_DocumentRoot17", None)
        self.__Uppaal_DocumentRoot17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Uppaal_NailType"):
                    opp_val = getattr(item, "Uppaal_NailType", None)
                    
                    if opp_val == self:
                        setattr(item, "Uppaal_NailType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Uppaal_NailType"):
                    opp_val = getattr(item, "Uppaal_NailType", None)
                    
                    setattr(item, "Uppaal_NailType", self)
                    

    @property
    def Uppaal_DocumentRoot5(self):
        return self.__Uppaal_DocumentRoot5

    @Uppaal_DocumentRoot5.setter
    def Uppaal_DocumentRoot5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Uppaal_DocumentRoot__Uppaal_DocumentRoot5", None)
        self.__Uppaal_DocumentRoot5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Uppaal_DeclarationType"):
                    opp_val = getattr(item, "Uppaal_DeclarationType", None)
                    
                    if opp_val == self:
                        setattr(item, "Uppaal_DeclarationType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Uppaal_DeclarationType"):
                    opp_val = getattr(item, "Uppaal_DeclarationType", None)
                    
                    setattr(item, "Uppaal_DeclarationType", self)
                    

    @property
    def Uppaal_DocumentRoot31(self):
        return self.__Uppaal_DocumentRoot31

    @Uppaal_DocumentRoot31.setter
    def Uppaal_DocumentRoot31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Uppaal_DocumentRoot__Uppaal_DocumentRoot31", None)
        self.__Uppaal_DocumentRoot31 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Uppaal_TemplateType"):
                    opp_val = getattr(item, "Uppaal_TemplateType", None)
                    
                    if opp_val == self:
                        setattr(item, "Uppaal_TemplateType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Uppaal_TemplateType"):
                    opp_val = getattr(item, "Uppaal_TemplateType", None)
                    
                    setattr(item, "Uppaal_TemplateType", self)
                    

    @property
    def Uppaal_DocumentRoot15(self):
        return self.__Uppaal_DocumentRoot15

    @Uppaal_DocumentRoot15.setter
    def Uppaal_DocumentRoot15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Uppaal_DocumentRoot__Uppaal_DocumentRoot15", None)
        self.__Uppaal_DocumentRoot15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Uppaal_LocationType"):
                    opp_val = getattr(item, "Uppaal_LocationType", None)
                    
                    if opp_val == self:
                        setattr(item, "Uppaal_LocationType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Uppaal_LocationType"):
                    opp_val = getattr(item, "Uppaal_LocationType", None)
                    
                    setattr(item, "Uppaal_LocationType", self)
                    

    @property
    def Uppaal_DocumentRoot11(self):
        return self.__Uppaal_DocumentRoot11

    @Uppaal_DocumentRoot11.setter
    def Uppaal_DocumentRoot11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Uppaal_DocumentRoot__Uppaal_DocumentRoot11", None)
        self.__Uppaal_DocumentRoot11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Uppaal_InstantiationType"):
                    opp_val = getattr(item, "Uppaal_InstantiationType", None)
                    
                    if opp_val == self:
                        setattr(item, "Uppaal_InstantiationType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Uppaal_InstantiationType"):
                    opp_val = getattr(item, "Uppaal_InstantiationType", None)
                    
                    setattr(item, "Uppaal_InstantiationType", self)
                    

    @property
    def Uppaal_DocumentRoot7(self):
        return self.__Uppaal_DocumentRoot7

    @Uppaal_DocumentRoot7.setter
    def Uppaal_DocumentRoot7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Uppaal_DocumentRoot__Uppaal_DocumentRoot7", None)
        self.__Uppaal_DocumentRoot7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Uppaal_ImportsType"):
                    opp_val = getattr(item, "Uppaal_ImportsType", None)
                    
                    if opp_val == self:
                        setattr(item, "Uppaal_ImportsType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Uppaal_ImportsType"):
                    opp_val = getattr(item, "Uppaal_ImportsType", None)
                    
                    setattr(item, "Uppaal_ImportsType", self)
                    

    @property
    def Uppaal_DocumentRoot27(self):
        return self.__Uppaal_DocumentRoot27

    @Uppaal_DocumentRoot27.setter
    def Uppaal_DocumentRoot27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Uppaal_DocumentRoot__Uppaal_DocumentRoot27", None)
        self.__Uppaal_DocumentRoot27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Uppaal_SystemType"):
                    opp_val = getattr(item, "Uppaal_SystemType", None)
                    
                    if opp_val == self:
                        setattr(item, "Uppaal_SystemType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Uppaal_SystemType"):
                    opp_val = getattr(item, "Uppaal_SystemType", None)
                    
                    setattr(item, "Uppaal_SystemType", self)
                    

    @property
    def Uppaal_DocumentRoot(self):
        return self.__Uppaal_DocumentRoot

    @Uppaal_DocumentRoot.setter
    def Uppaal_DocumentRoot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Uppaal_DocumentRoot__Uppaal_DocumentRoot", None)
        self.__Uppaal_DocumentRoot = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Uppaal_EStringToStringMapEntry"):
                    opp_val = getattr(item, "Uppaal_EStringToStringMapEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "Uppaal_EStringToStringMapEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Uppaal_EStringToStringMapEntry"):
                    opp_val = getattr(item, "Uppaal_EStringToStringMapEntry", None)
                    
                    setattr(item, "Uppaal_EStringToStringMapEntry", self)
                    

    @property
    def Uppaal_DocumentRoot25(self):
        return self.__Uppaal_DocumentRoot25

    @Uppaal_DocumentRoot25.setter
    def Uppaal_DocumentRoot25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Uppaal_DocumentRoot__Uppaal_DocumentRoot25", None)
        self.__Uppaal_DocumentRoot25 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Uppaal_SourceType"):
                    opp_val = getattr(item, "Uppaal_SourceType", None)
                    
                    if opp_val == self:
                        setattr(item, "Uppaal_SourceType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Uppaal_SourceType"):
                    opp_val = getattr(item, "Uppaal_SourceType", None)
                    
                    setattr(item, "Uppaal_SourceType", self)
                    

    @property
    def Uppaal_DocumentRoot13(self):
        return self.__Uppaal_DocumentRoot13

    @Uppaal_DocumentRoot13.setter
    def Uppaal_DocumentRoot13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Uppaal_DocumentRoot__Uppaal_DocumentRoot13", None)
        self.__Uppaal_DocumentRoot13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Uppaal_LabelType"):
                    opp_val = getattr(item, "Uppaal_LabelType", None)
                    
                    if opp_val == self:
                        setattr(item, "Uppaal_LabelType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Uppaal_LabelType"):
                    opp_val = getattr(item, "Uppaal_LabelType", None)
                    
                    setattr(item, "Uppaal_LabelType", self)
                    

    @property
    def Uppaal_DocumentRoot9(self):
        return self.__Uppaal_DocumentRoot9

    @Uppaal_DocumentRoot9.setter
    def Uppaal_DocumentRoot9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Uppaal_DocumentRoot__Uppaal_DocumentRoot9", None)
        self.__Uppaal_DocumentRoot9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Uppaal_InitType"):
                    opp_val = getattr(item, "Uppaal_InitType", None)
                    
                    if opp_val == self:
                        setattr(item, "Uppaal_InitType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Uppaal_InitType"):
                    opp_val = getattr(item, "Uppaal_InitType", None)
                    
                    setattr(item, "Uppaal_InitType", self)
                    

    @property
    def Uppaal_DocumentRoot23(self):
        return self.__Uppaal_DocumentRoot23

    @Uppaal_DocumentRoot23.setter
    def Uppaal_DocumentRoot23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Uppaal_DocumentRoot__Uppaal_DocumentRoot23", None)
        self.__Uppaal_DocumentRoot23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Uppaal_ParameterType"):
                    opp_val = getattr(item, "Uppaal_ParameterType", None)
                    
                    if opp_val == self:
                        setattr(item, "Uppaal_ParameterType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Uppaal_ParameterType"):
                    opp_val = getattr(item, "Uppaal_ParameterType", None)
                    
                    setattr(item, "Uppaal_ParameterType", self)
                    

    @property
    def Uppaal_DocumentRoot2(self):
        return self.__Uppaal_DocumentRoot2

    @Uppaal_DocumentRoot2.setter
    def Uppaal_DocumentRoot2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Uppaal_DocumentRoot__Uppaal_DocumentRoot2", None)
        self.__Uppaal_DocumentRoot2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Uppaal_EStringToStringMapEntry3"):
                    opp_val = getattr(item, "Uppaal_EStringToStringMapEntry3", None)
                    
                    if opp_val == self:
                        setattr(item, "Uppaal_EStringToStringMapEntry3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Uppaal_EStringToStringMapEntry3"):
                    opp_val = getattr(item, "Uppaal_EStringToStringMapEntry3", None)
                    
                    setattr(item, "Uppaal_EStringToStringMapEntry3", self)
                    

    @property
    def Uppaal_DocumentRoot19(self):
        return self.__Uppaal_DocumentRoot19

    @Uppaal_DocumentRoot19.setter
    def Uppaal_DocumentRoot19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Uppaal_DocumentRoot__Uppaal_DocumentRoot19", None)
        self.__Uppaal_DocumentRoot19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Uppaal_NameType"):
                    opp_val = getattr(item, "Uppaal_NameType", None)
                    
                    if opp_val == self:
                        setattr(item, "Uppaal_NameType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Uppaal_NameType"):
                    opp_val = getattr(item, "Uppaal_NameType", None)
                    
                    setattr(item, "Uppaal_NameType", self)
                    

    @property
    def Uppaal_DocumentRoot33(self):
        return self.__Uppaal_DocumentRoot33

    @Uppaal_DocumentRoot33.setter
    def Uppaal_DocumentRoot33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Uppaal_DocumentRoot__Uppaal_DocumentRoot33", None)
        self.__Uppaal_DocumentRoot33 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Uppaal_TransitionType"):
                    opp_val = getattr(item, "Uppaal_TransitionType", None)
                    
                    if opp_val == self:
                        setattr(item, "Uppaal_TransitionType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Uppaal_TransitionType"):
                    opp_val = getattr(item, "Uppaal_TransitionType", None)
                    
                    setattr(item, "Uppaal_TransitionType", self)
                    

    @property
    def Uppaal_DocumentRoot21(self):
        return self.__Uppaal_DocumentRoot21

    @Uppaal_DocumentRoot21.setter
    def Uppaal_DocumentRoot21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Uppaal_DocumentRoot__Uppaal_DocumentRoot21", None)
        self.__Uppaal_DocumentRoot21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Uppaal_NtaType"):
                    opp_val = getattr(item, "Uppaal_NtaType", None)
                    
                    if opp_val == self:
                        setattr(item, "Uppaal_NtaType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Uppaal_NtaType"):
                    opp_val = getattr(item, "Uppaal_NtaType", None)
                    
                    setattr(item, "Uppaal_NtaType", self)
                    

class Uppaal_DeclarationType:

    def __init__(self, mixed: str, Uppaal_DeclarationType: "Uppaal_DocumentRoot" = None, Uppaal_DeclarationType45: "Uppaal_NtaType" = None, Uppaal_DeclarationType63: "Uppaal_TemplateType" = None):
        self.mixed = mixed
        self.Uppaal_DeclarationType = Uppaal_DeclarationType
        self.Uppaal_DeclarationType45 = Uppaal_DeclarationType45
        self.Uppaal_DeclarationType63 = Uppaal_DeclarationType63
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def Uppaal_DeclarationType45(self):
        return self.__Uppaal_DeclarationType45

    @Uppaal_DeclarationType45.setter
    def Uppaal_DeclarationType45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Uppaal_DeclarationType__Uppaal_DeclarationType45", None)
        self.__Uppaal_DeclarationType45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Uppaal_NtaType44"):
                opp_val = getattr(old_value, "Uppaal_NtaType44", None)
                if opp_val == self:
                    setattr(old_value, "Uppaal_NtaType44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Uppaal_NtaType44"):
                opp_val = getattr(value, "Uppaal_NtaType44", None)
                setattr(value, "Uppaal_NtaType44", self)

    @property
    def Uppaal_DeclarationType63(self):
        return self.__Uppaal_DeclarationType63

    @Uppaal_DeclarationType63.setter
    def Uppaal_DeclarationType63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Uppaal_DeclarationType__Uppaal_DeclarationType63", None)
        self.__Uppaal_DeclarationType63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Uppaal_TemplateType62"):
                opp_val = getattr(old_value, "Uppaal_TemplateType62", None)
                if opp_val == self:
                    setattr(old_value, "Uppaal_TemplateType62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Uppaal_TemplateType62"):
                opp_val = getattr(value, "Uppaal_TemplateType62", None)
                setattr(value, "Uppaal_TemplateType62", self)

    @property
    def Uppaal_DeclarationType(self):
        return self.__Uppaal_DeclarationType

    @Uppaal_DeclarationType.setter
    def Uppaal_DeclarationType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Uppaal_DeclarationType__Uppaal_DeclarationType", None)
        self.__Uppaal_DeclarationType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Uppaal_DocumentRoot5"):
                opp_val = getattr(old_value, "Uppaal_DocumentRoot5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Uppaal_DocumentRoot5"):
                opp_val = getattr(value, "Uppaal_DocumentRoot5", None)
                if opp_val is None:
                    setattr(value, "Uppaal_DocumentRoot5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Uppaal_ImportsType:

    def __init__(self, mixed: str, Uppaal_ImportsType: "Uppaal_DocumentRoot" = None, Uppaal_ImportsType42: "Uppaal_NtaType" = None):
        self.mixed = mixed
        self.Uppaal_ImportsType = Uppaal_ImportsType
        self.Uppaal_ImportsType42 = Uppaal_ImportsType42
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def Uppaal_ImportsType(self):
        return self.__Uppaal_ImportsType

    @Uppaal_ImportsType.setter
    def Uppaal_ImportsType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Uppaal_ImportsType__Uppaal_ImportsType", None)
        self.__Uppaal_ImportsType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Uppaal_DocumentRoot7"):
                opp_val = getattr(old_value, "Uppaal_DocumentRoot7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Uppaal_DocumentRoot7"):
                opp_val = getattr(value, "Uppaal_DocumentRoot7", None)
                if opp_val is None:
                    setattr(value, "Uppaal_DocumentRoot7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Uppaal_ImportsType42(self):
        return self.__Uppaal_ImportsType42

    @Uppaal_ImportsType42.setter
    def Uppaal_ImportsType42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Uppaal_ImportsType__Uppaal_ImportsType42", None)
        self.__Uppaal_ImportsType42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Uppaal_NtaType41"):
                opp_val = getattr(old_value, "Uppaal_NtaType41", None)
                if opp_val == self:
                    setattr(old_value, "Uppaal_NtaType41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Uppaal_NtaType41"):
                opp_val = getattr(value, "Uppaal_NtaType41", None)
                setattr(value, "Uppaal_NtaType41", self)
