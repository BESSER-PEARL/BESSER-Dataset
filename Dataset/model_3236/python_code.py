from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class UppaalFlat11_TargetType:

    def __init__(self, ref: str, UppaalFlat11_TargetType: "UppaalFlat11_DocumentRoot" = None, UppaalFlat11_TargetType65: "UppaalFlat11_TransitionType" = None):
        self.ref = ref
        self.UppaalFlat11_TargetType = UppaalFlat11_TargetType
        self.UppaalFlat11_TargetType65 = UppaalFlat11_TargetType65
        
    @property
    def ref(self) -> str:
        return self.__ref

    @ref.setter
    def ref(self, ref: str):
        self.__ref = ref

    @property
    def UppaalFlat11_TargetType65(self):
        return self.__UppaalFlat11_TargetType65

    @UppaalFlat11_TargetType65.setter
    def UppaalFlat11_TargetType65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UppaalFlat11_TargetType__UppaalFlat11_TargetType65", None)
        self.__UppaalFlat11_TargetType65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UppaalFlat11_TransitionType64"):
                opp_val = getattr(old_value, "UppaalFlat11_TransitionType64", None)
                if opp_val == self:
                    setattr(old_value, "UppaalFlat11_TransitionType64", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UppaalFlat11_TransitionType64"):
                opp_val = getattr(value, "UppaalFlat11_TransitionType64", None)
                setattr(value, "UppaalFlat11_TransitionType64", self)

    @property
    def UppaalFlat11_TargetType(self):
        return self.__UppaalFlat11_TargetType

    @UppaalFlat11_TargetType.setter
    def UppaalFlat11_TargetType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UppaalFlat11_TargetType__UppaalFlat11_TargetType", None)
        self.__UppaalFlat11_TargetType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UppaalFlat11_DocumentRoot23"):
                opp_val = getattr(old_value, "UppaalFlat11_DocumentRoot23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UppaalFlat11_DocumentRoot23"):
                opp_val = getattr(value, "UppaalFlat11_DocumentRoot23", None)
                if opp_val is None:
                    setattr(value, "UppaalFlat11_DocumentRoot23", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class UppaalFlat11_UrgentType:

    pass
class UppaalFlat11_TransitionType:

    def __init__(self, x: str, y: str, color: str, id: str, UppaalFlat11_TransitionType: "UppaalFlat11_DocumentRoot" = None, UppaalFlat11_TransitionType59: "UppaalFlat11_TemplateType" = None, UppaalFlat11_TransitionType61: "UppaalFlat11_SourceType" = None, UppaalFlat11_TransitionType64: "UppaalFlat11_TargetType" = None, UppaalFlat11_TransitionType67: set["UppaalFlat11_LabelType"] = None, UppaalFlat11_TransitionType70: set["UppaalFlat11_NailType"] = None):
        self.x = x
        self.y = y
        self.color = color
        self.id = id
        self.UppaalFlat11_TransitionType = UppaalFlat11_TransitionType
        self.UppaalFlat11_TransitionType59 = UppaalFlat11_TransitionType59
        self.UppaalFlat11_TransitionType61 = UppaalFlat11_TransitionType61
        self.UppaalFlat11_TransitionType64 = UppaalFlat11_TransitionType64
        self.UppaalFlat11_TransitionType67 = UppaalFlat11_TransitionType67 if UppaalFlat11_TransitionType67 is not None else set()
        self.UppaalFlat11_TransitionType70 = UppaalFlat11_TransitionType70 if UppaalFlat11_TransitionType70 is not None else set()
        
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
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color

    @property
    def UppaalFlat11_TransitionType70(self):
        return self.__UppaalFlat11_TransitionType70

    @UppaalFlat11_TransitionType70.setter
    def UppaalFlat11_TransitionType70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UppaalFlat11_TransitionType__UppaalFlat11_TransitionType70", None)
        self.__UppaalFlat11_TransitionType70 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UppaalFlat11_NailType71"):
                    opp_val = getattr(item, "UppaalFlat11_NailType71", None)
                    
                    if opp_val == self:
                        setattr(item, "UppaalFlat11_NailType71", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UppaalFlat11_NailType71"):
                    opp_val = getattr(item, "UppaalFlat11_NailType71", None)
                    
                    setattr(item, "UppaalFlat11_NailType71", self)
                    

    @property
    def UppaalFlat11_TransitionType59(self):
        return self.__UppaalFlat11_TransitionType59

    @UppaalFlat11_TransitionType59.setter
    def UppaalFlat11_TransitionType59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UppaalFlat11_TransitionType__UppaalFlat11_TransitionType59", None)
        self.__UppaalFlat11_TransitionType59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UppaalFlat11_TemplateType58"):
                opp_val = getattr(old_value, "UppaalFlat11_TemplateType58", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UppaalFlat11_TemplateType58"):
                opp_val = getattr(value, "UppaalFlat11_TemplateType58", None)
                if opp_val is None:
                    setattr(value, "UppaalFlat11_TemplateType58", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UppaalFlat11_TransitionType67(self):
        return self.__UppaalFlat11_TransitionType67

    @UppaalFlat11_TransitionType67.setter
    def UppaalFlat11_TransitionType67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UppaalFlat11_TransitionType__UppaalFlat11_TransitionType67", None)
        self.__UppaalFlat11_TransitionType67 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UppaalFlat11_LabelType68"):
                    opp_val = getattr(item, "UppaalFlat11_LabelType68", None)
                    
                    if opp_val == self:
                        setattr(item, "UppaalFlat11_LabelType68", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UppaalFlat11_LabelType68"):
                    opp_val = getattr(item, "UppaalFlat11_LabelType68", None)
                    
                    setattr(item, "UppaalFlat11_LabelType68", self)
                    

    @property
    def UppaalFlat11_TransitionType(self):
        return self.__UppaalFlat11_TransitionType

    @UppaalFlat11_TransitionType.setter
    def UppaalFlat11_TransitionType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UppaalFlat11_TransitionType__UppaalFlat11_TransitionType", None)
        self.__UppaalFlat11_TransitionType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UppaalFlat11_DocumentRoot27"):
                opp_val = getattr(old_value, "UppaalFlat11_DocumentRoot27", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UppaalFlat11_DocumentRoot27"):
                opp_val = getattr(value, "UppaalFlat11_DocumentRoot27", None)
                if opp_val is None:
                    setattr(value, "UppaalFlat11_DocumentRoot27", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UppaalFlat11_TransitionType64(self):
        return self.__UppaalFlat11_TransitionType64

    @UppaalFlat11_TransitionType64.setter
    def UppaalFlat11_TransitionType64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UppaalFlat11_TransitionType__UppaalFlat11_TransitionType64", None)
        self.__UppaalFlat11_TransitionType64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UppaalFlat11_TargetType65"):
                opp_val = getattr(old_value, "UppaalFlat11_TargetType65", None)
                if opp_val == self:
                    setattr(old_value, "UppaalFlat11_TargetType65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UppaalFlat11_TargetType65"):
                opp_val = getattr(value, "UppaalFlat11_TargetType65", None)
                setattr(value, "UppaalFlat11_TargetType65", self)

    @property
    def UppaalFlat11_TransitionType61(self):
        return self.__UppaalFlat11_TransitionType61

    @UppaalFlat11_TransitionType61.setter
    def UppaalFlat11_TransitionType61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UppaalFlat11_TransitionType__UppaalFlat11_TransitionType61", None)
        self.__UppaalFlat11_TransitionType61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UppaalFlat11_SourceType62"):
                opp_val = getattr(old_value, "UppaalFlat11_SourceType62", None)
                if opp_val == self:
                    setattr(old_value, "UppaalFlat11_SourceType62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UppaalFlat11_SourceType62"):
                opp_val = getattr(value, "UppaalFlat11_SourceType62", None)
                setattr(value, "UppaalFlat11_SourceType62", self)

class UppaalFlat11_TemplateType:

    def __init__(self, declaration: str, UppaalFlat11_TemplateType: "UppaalFlat11_DocumentRoot" = None, UppaalFlat11_TemplateType44: "UppaalFlat11_NtaType" = None, UppaalFlat11_TemplateType52: set["UppaalFlat11_LocationType"] = None, UppaalFlat11_TemplateType46: "UppaalFlat11_NameType" = None, UppaalFlat11_TemplateType49: "UppaalFlat11_ParameterType" = None, UppaalFlat11_TemplateType55: "UppaalFlat11_InitType" = None, UppaalFlat11_TemplateType58: set["UppaalFlat11_TransitionType"] = None):
        self.declaration = declaration
        self.UppaalFlat11_TemplateType = UppaalFlat11_TemplateType
        self.UppaalFlat11_TemplateType44 = UppaalFlat11_TemplateType44
        self.UppaalFlat11_TemplateType52 = UppaalFlat11_TemplateType52 if UppaalFlat11_TemplateType52 is not None else set()
        self.UppaalFlat11_TemplateType46 = UppaalFlat11_TemplateType46
        self.UppaalFlat11_TemplateType49 = UppaalFlat11_TemplateType49
        self.UppaalFlat11_TemplateType55 = UppaalFlat11_TemplateType55
        self.UppaalFlat11_TemplateType58 = UppaalFlat11_TemplateType58 if UppaalFlat11_TemplateType58 is not None else set()
        
    @property
    def declaration(self) -> str:
        return self.__declaration

    @declaration.setter
    def declaration(self, declaration: str):
        self.__declaration = declaration

    @property
    def UppaalFlat11_TemplateType46(self):
        return self.__UppaalFlat11_TemplateType46

    @UppaalFlat11_TemplateType46.setter
    def UppaalFlat11_TemplateType46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UppaalFlat11_TemplateType__UppaalFlat11_TemplateType46", None)
        self.__UppaalFlat11_TemplateType46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UppaalFlat11_NameType47"):
                opp_val = getattr(old_value, "UppaalFlat11_NameType47", None)
                if opp_val == self:
                    setattr(old_value, "UppaalFlat11_NameType47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UppaalFlat11_NameType47"):
                opp_val = getattr(value, "UppaalFlat11_NameType47", None)
                setattr(value, "UppaalFlat11_NameType47", self)

    @property
    def UppaalFlat11_TemplateType55(self):
        return self.__UppaalFlat11_TemplateType55

    @UppaalFlat11_TemplateType55.setter
    def UppaalFlat11_TemplateType55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UppaalFlat11_TemplateType__UppaalFlat11_TemplateType55", None)
        self.__UppaalFlat11_TemplateType55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UppaalFlat11_InitType56"):
                opp_val = getattr(old_value, "UppaalFlat11_InitType56", None)
                if opp_val == self:
                    setattr(old_value, "UppaalFlat11_InitType56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UppaalFlat11_InitType56"):
                opp_val = getattr(value, "UppaalFlat11_InitType56", None)
                setattr(value, "UppaalFlat11_InitType56", self)

    @property
    def UppaalFlat11_TemplateType49(self):
        return self.__UppaalFlat11_TemplateType49

    @UppaalFlat11_TemplateType49.setter
    def UppaalFlat11_TemplateType49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UppaalFlat11_TemplateType__UppaalFlat11_TemplateType49", None)
        self.__UppaalFlat11_TemplateType49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UppaalFlat11_ParameterType50"):
                opp_val = getattr(old_value, "UppaalFlat11_ParameterType50", None)
                if opp_val == self:
                    setattr(old_value, "UppaalFlat11_ParameterType50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UppaalFlat11_ParameterType50"):
                opp_val = getattr(value, "UppaalFlat11_ParameterType50", None)
                setattr(value, "UppaalFlat11_ParameterType50", self)

    @property
    def UppaalFlat11_TemplateType(self):
        return self.__UppaalFlat11_TemplateType

    @UppaalFlat11_TemplateType.setter
    def UppaalFlat11_TemplateType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UppaalFlat11_TemplateType__UppaalFlat11_TemplateType", None)
        self.__UppaalFlat11_TemplateType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UppaalFlat11_DocumentRoot25"):
                opp_val = getattr(old_value, "UppaalFlat11_DocumentRoot25", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UppaalFlat11_DocumentRoot25"):
                opp_val = getattr(value, "UppaalFlat11_DocumentRoot25", None)
                if opp_val is None:
                    setattr(value, "UppaalFlat11_DocumentRoot25", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UppaalFlat11_TemplateType58(self):
        return self.__UppaalFlat11_TemplateType58

    @UppaalFlat11_TemplateType58.setter
    def UppaalFlat11_TemplateType58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UppaalFlat11_TemplateType__UppaalFlat11_TemplateType58", None)
        self.__UppaalFlat11_TemplateType58 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UppaalFlat11_TransitionType59"):
                    opp_val = getattr(item, "UppaalFlat11_TransitionType59", None)
                    
                    if opp_val == self:
                        setattr(item, "UppaalFlat11_TransitionType59", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UppaalFlat11_TransitionType59"):
                    opp_val = getattr(item, "UppaalFlat11_TransitionType59", None)
                    
                    setattr(item, "UppaalFlat11_TransitionType59", self)
                    

    @property
    def UppaalFlat11_TemplateType44(self):
        return self.__UppaalFlat11_TemplateType44

    @UppaalFlat11_TemplateType44.setter
    def UppaalFlat11_TemplateType44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UppaalFlat11_TemplateType__UppaalFlat11_TemplateType44", None)
        self.__UppaalFlat11_TemplateType44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UppaalFlat11_NtaType43"):
                opp_val = getattr(old_value, "UppaalFlat11_NtaType43", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UppaalFlat11_NtaType43"):
                opp_val = getattr(value, "UppaalFlat11_NtaType43", None)
                if opp_val is None:
                    setattr(value, "UppaalFlat11_NtaType43", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UppaalFlat11_TemplateType52(self):
        return self.__UppaalFlat11_TemplateType52

    @UppaalFlat11_TemplateType52.setter
    def UppaalFlat11_TemplateType52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UppaalFlat11_TemplateType__UppaalFlat11_TemplateType52", None)
        self.__UppaalFlat11_TemplateType52 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UppaalFlat11_LocationType53"):
                    opp_val = getattr(item, "UppaalFlat11_LocationType53", None)
                    
                    if opp_val == self:
                        setattr(item, "UppaalFlat11_LocationType53", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UppaalFlat11_LocationType53"):
                    opp_val = getattr(item, "UppaalFlat11_LocationType53", None)
                    
                    setattr(item, "UppaalFlat11_LocationType53", self)
                    

class UppaalFlat11_NameType:

    def __init__(self, mixed: str, x: str, y: str, UppaalFlat11_NameType: "UppaalFlat11_DocumentRoot" = None, UppaalFlat11_NameType32: "UppaalFlat11_LocationType" = None, UppaalFlat11_NameType47: "UppaalFlat11_TemplateType" = None):
        self.mixed = mixed
        self.x = x
        self.y = y
        self.UppaalFlat11_NameType = UppaalFlat11_NameType
        self.UppaalFlat11_NameType32 = UppaalFlat11_NameType32
        self.UppaalFlat11_NameType47 = UppaalFlat11_NameType47
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

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
    def UppaalFlat11_NameType47(self):
        return self.__UppaalFlat11_NameType47

    @UppaalFlat11_NameType47.setter
    def UppaalFlat11_NameType47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UppaalFlat11_NameType__UppaalFlat11_NameType47", None)
        self.__UppaalFlat11_NameType47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UppaalFlat11_TemplateType46"):
                opp_val = getattr(old_value, "UppaalFlat11_TemplateType46", None)
                if opp_val == self:
                    setattr(old_value, "UppaalFlat11_TemplateType46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UppaalFlat11_TemplateType46"):
                opp_val = getattr(value, "UppaalFlat11_TemplateType46", None)
                setattr(value, "UppaalFlat11_TemplateType46", self)

    @property
    def UppaalFlat11_NameType32(self):
        return self.__UppaalFlat11_NameType32

    @UppaalFlat11_NameType32.setter
    def UppaalFlat11_NameType32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UppaalFlat11_NameType__UppaalFlat11_NameType32", None)
        self.__UppaalFlat11_NameType32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UppaalFlat11_LocationType31"):
                opp_val = getattr(old_value, "UppaalFlat11_LocationType31", None)
                if opp_val == self:
                    setattr(old_value, "UppaalFlat11_LocationType31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UppaalFlat11_LocationType31"):
                opp_val = getattr(value, "UppaalFlat11_LocationType31", None)
                setattr(value, "UppaalFlat11_LocationType31", self)

    @property
    def UppaalFlat11_NameType(self):
        return self.__UppaalFlat11_NameType

    @UppaalFlat11_NameType.setter
    def UppaalFlat11_NameType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UppaalFlat11_NameType__UppaalFlat11_NameType", None)
        self.__UppaalFlat11_NameType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UppaalFlat11_DocumentRoot15"):
                opp_val = getattr(old_value, "UppaalFlat11_DocumentRoot15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UppaalFlat11_DocumentRoot15"):
                opp_val = getattr(value, "UppaalFlat11_DocumentRoot15", None)
                if opp_val is None:
                    setattr(value, "UppaalFlat11_DocumentRoot15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class UppaalFlat11_SourceType:

    def __init__(self, ref: str, UppaalFlat11_SourceType: "UppaalFlat11_DocumentRoot" = None, UppaalFlat11_SourceType62: "UppaalFlat11_TransitionType" = None):
        self.ref = ref
        self.UppaalFlat11_SourceType = UppaalFlat11_SourceType
        self.UppaalFlat11_SourceType62 = UppaalFlat11_SourceType62
        
    @property
    def ref(self) -> str:
        return self.__ref

    @ref.setter
    def ref(self, ref: str):
        self.__ref = ref

    @property
    def UppaalFlat11_SourceType(self):
        return self.__UppaalFlat11_SourceType

    @UppaalFlat11_SourceType.setter
    def UppaalFlat11_SourceType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UppaalFlat11_SourceType__UppaalFlat11_SourceType", None)
        self.__UppaalFlat11_SourceType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UppaalFlat11_DocumentRoot21"):
                opp_val = getattr(old_value, "UppaalFlat11_DocumentRoot21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UppaalFlat11_DocumentRoot21"):
                opp_val = getattr(value, "UppaalFlat11_DocumentRoot21", None)
                if opp_val is None:
                    setattr(value, "UppaalFlat11_DocumentRoot21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UppaalFlat11_SourceType62(self):
        return self.__UppaalFlat11_SourceType62

    @UppaalFlat11_SourceType62.setter
    def UppaalFlat11_SourceType62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UppaalFlat11_SourceType__UppaalFlat11_SourceType62", None)
        self.__UppaalFlat11_SourceType62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UppaalFlat11_TransitionType61"):
                opp_val = getattr(old_value, "UppaalFlat11_TransitionType61", None)
                if opp_val == self:
                    setattr(old_value, "UppaalFlat11_TransitionType61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UppaalFlat11_TransitionType61"):
                opp_val = getattr(value, "UppaalFlat11_TransitionType61", None)
                setattr(value, "UppaalFlat11_TransitionType61", self)

class UppaalFlat11_ParameterType:

    def __init__(self, mixed: str, x: str, y: str, UppaalFlat11_ParameterType: "UppaalFlat11_DocumentRoot" = None, UppaalFlat11_ParameterType50: "UppaalFlat11_TemplateType" = None):
        self.mixed = mixed
        self.x = x
        self.y = y
        self.UppaalFlat11_ParameterType = UppaalFlat11_ParameterType
        self.UppaalFlat11_ParameterType50 = UppaalFlat11_ParameterType50
        
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
    def y(self) -> str:
        return self.__y

    @y.setter
    def y(self, y: str):
        self.__y = y

    @property
    def UppaalFlat11_ParameterType(self):
        return self.__UppaalFlat11_ParameterType

    @UppaalFlat11_ParameterType.setter
    def UppaalFlat11_ParameterType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UppaalFlat11_ParameterType__UppaalFlat11_ParameterType", None)
        self.__UppaalFlat11_ParameterType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UppaalFlat11_DocumentRoot19"):
                opp_val = getattr(old_value, "UppaalFlat11_DocumentRoot19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UppaalFlat11_DocumentRoot19"):
                opp_val = getattr(value, "UppaalFlat11_DocumentRoot19", None)
                if opp_val is None:
                    setattr(value, "UppaalFlat11_DocumentRoot19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UppaalFlat11_ParameterType50(self):
        return self.__UppaalFlat11_ParameterType50

    @UppaalFlat11_ParameterType50.setter
    def UppaalFlat11_ParameterType50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UppaalFlat11_ParameterType__UppaalFlat11_ParameterType50", None)
        self.__UppaalFlat11_ParameterType50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UppaalFlat11_TemplateType49"):
                opp_val = getattr(old_value, "UppaalFlat11_TemplateType49", None)
                if opp_val == self:
                    setattr(old_value, "UppaalFlat11_TemplateType49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UppaalFlat11_TemplateType49"):
                opp_val = getattr(value, "UppaalFlat11_TemplateType49", None)
                setattr(value, "UppaalFlat11_TemplateType49", self)

class UppaalFlat11_NtaType:

    def __init__(self, declaration: str, imports: str, instantiation: str, system: str, UppaalFlat11_NtaType: "UppaalFlat11_DocumentRoot" = None, UppaalFlat11_NtaType43: set["UppaalFlat11_TemplateType"] = None):
        self.declaration = declaration
        self.imports = imports
        self.instantiation = instantiation
        self.system = system
        self.UppaalFlat11_NtaType = UppaalFlat11_NtaType
        self.UppaalFlat11_NtaType43 = UppaalFlat11_NtaType43 if UppaalFlat11_NtaType43 is not None else set()
        
    @property
    def system(self) -> str:
        return self.__system

    @system.setter
    def system(self, system: str):
        self.__system = system

    @property
    def instantiation(self) -> str:
        return self.__instantiation

    @instantiation.setter
    def instantiation(self, instantiation: str):
        self.__instantiation = instantiation

    @property
    def imports(self) -> str:
        return self.__imports

    @imports.setter
    def imports(self, imports: str):
        self.__imports = imports

    @property
    def declaration(self) -> str:
        return self.__declaration

    @declaration.setter
    def declaration(self, declaration: str):
        self.__declaration = declaration

    @property
    def UppaalFlat11_NtaType43(self):
        return self.__UppaalFlat11_NtaType43

    @UppaalFlat11_NtaType43.setter
    def UppaalFlat11_NtaType43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UppaalFlat11_NtaType__UppaalFlat11_NtaType43", None)
        self.__UppaalFlat11_NtaType43 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UppaalFlat11_TemplateType44"):
                    opp_val = getattr(item, "UppaalFlat11_TemplateType44", None)
                    
                    if opp_val == self:
                        setattr(item, "UppaalFlat11_TemplateType44", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UppaalFlat11_TemplateType44"):
                    opp_val = getattr(item, "UppaalFlat11_TemplateType44", None)
                    
                    setattr(item, "UppaalFlat11_TemplateType44", self)
                    

    @property
    def UppaalFlat11_NtaType(self):
        return self.__UppaalFlat11_NtaType

    @UppaalFlat11_NtaType.setter
    def UppaalFlat11_NtaType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UppaalFlat11_NtaType__UppaalFlat11_NtaType", None)
        self.__UppaalFlat11_NtaType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UppaalFlat11_DocumentRoot17"):
                opp_val = getattr(old_value, "UppaalFlat11_DocumentRoot17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UppaalFlat11_DocumentRoot17"):
                opp_val = getattr(value, "UppaalFlat11_DocumentRoot17", None)
                if opp_val is None:
                    setattr(value, "UppaalFlat11_DocumentRoot17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class UppaalFlat11_NailType:

    def __init__(self, x: str, y: str, UppaalFlat11_NailType: "UppaalFlat11_DocumentRoot" = None, UppaalFlat11_NailType71: "UppaalFlat11_TransitionType" = None):
        self.x = x
        self.y = y
        self.UppaalFlat11_NailType = UppaalFlat11_NailType
        self.UppaalFlat11_NailType71 = UppaalFlat11_NailType71
        
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
    def UppaalFlat11_NailType71(self):
        return self.__UppaalFlat11_NailType71

    @UppaalFlat11_NailType71.setter
    def UppaalFlat11_NailType71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UppaalFlat11_NailType__UppaalFlat11_NailType71", None)
        self.__UppaalFlat11_NailType71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UppaalFlat11_TransitionType70"):
                opp_val = getattr(old_value, "UppaalFlat11_TransitionType70", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UppaalFlat11_TransitionType70"):
                opp_val = getattr(value, "UppaalFlat11_TransitionType70", None)
                if opp_val is None:
                    setattr(value, "UppaalFlat11_TransitionType70", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UppaalFlat11_NailType(self):
        return self.__UppaalFlat11_NailType

    @UppaalFlat11_NailType.setter
    def UppaalFlat11_NailType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UppaalFlat11_NailType__UppaalFlat11_NailType", None)
        self.__UppaalFlat11_NailType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UppaalFlat11_DocumentRoot13"):
                opp_val = getattr(old_value, "UppaalFlat11_DocumentRoot13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UppaalFlat11_DocumentRoot13"):
                opp_val = getattr(value, "UppaalFlat11_DocumentRoot13", None)
                if opp_val is None:
                    setattr(value, "UppaalFlat11_DocumentRoot13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class UppaalFlat11_LocationType:

    def __init__(self, color: str, id: str, x: str, y: str, UppaalFlat11_LocationType: "UppaalFlat11_DocumentRoot" = None, UppaalFlat11_LocationType37: "UppaalFlat11_UrgentType" = None, UppaalFlat11_LocationType40: "UppaalFlat11_CommittedType" = None, UppaalFlat11_LocationType31: "UppaalFlat11_NameType" = None, UppaalFlat11_LocationType34: set["UppaalFlat11_LabelType"] = None, UppaalFlat11_LocationType53: "UppaalFlat11_TemplateType" = None):
        self.color = color
        self.id = id
        self.x = x
        self.y = y
        self.UppaalFlat11_LocationType = UppaalFlat11_LocationType
        self.UppaalFlat11_LocationType37 = UppaalFlat11_LocationType37
        self.UppaalFlat11_LocationType40 = UppaalFlat11_LocationType40
        self.UppaalFlat11_LocationType31 = UppaalFlat11_LocationType31
        self.UppaalFlat11_LocationType34 = UppaalFlat11_LocationType34 if UppaalFlat11_LocationType34 is not None else set()
        self.UppaalFlat11_LocationType53 = UppaalFlat11_LocationType53
        
    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color

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
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def UppaalFlat11_LocationType37(self):
        return self.__UppaalFlat11_LocationType37

    @UppaalFlat11_LocationType37.setter
    def UppaalFlat11_LocationType37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UppaalFlat11_LocationType__UppaalFlat11_LocationType37", None)
        self.__UppaalFlat11_LocationType37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UppaalFlat11_UrgentType38"):
                opp_val = getattr(old_value, "UppaalFlat11_UrgentType38", None)
                if opp_val == self:
                    setattr(old_value, "UppaalFlat11_UrgentType38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UppaalFlat11_UrgentType38"):
                opp_val = getattr(value, "UppaalFlat11_UrgentType38", None)
                setattr(value, "UppaalFlat11_UrgentType38", self)

    @property
    def UppaalFlat11_LocationType40(self):
        return self.__UppaalFlat11_LocationType40

    @UppaalFlat11_LocationType40.setter
    def UppaalFlat11_LocationType40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UppaalFlat11_LocationType__UppaalFlat11_LocationType40", None)
        self.__UppaalFlat11_LocationType40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UppaalFlat11_CommittedType41"):
                opp_val = getattr(old_value, "UppaalFlat11_CommittedType41", None)
                if opp_val == self:
                    setattr(old_value, "UppaalFlat11_CommittedType41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UppaalFlat11_CommittedType41"):
                opp_val = getattr(value, "UppaalFlat11_CommittedType41", None)
                setattr(value, "UppaalFlat11_CommittedType41", self)

    @property
    def UppaalFlat11_LocationType34(self):
        return self.__UppaalFlat11_LocationType34

    @UppaalFlat11_LocationType34.setter
    def UppaalFlat11_LocationType34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UppaalFlat11_LocationType__UppaalFlat11_LocationType34", None)
        self.__UppaalFlat11_LocationType34 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UppaalFlat11_LabelType35"):
                    opp_val = getattr(item, "UppaalFlat11_LabelType35", None)
                    
                    if opp_val == self:
                        setattr(item, "UppaalFlat11_LabelType35", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UppaalFlat11_LabelType35"):
                    opp_val = getattr(item, "UppaalFlat11_LabelType35", None)
                    
                    setattr(item, "UppaalFlat11_LabelType35", self)
                    

    @property
    def UppaalFlat11_LocationType31(self):
        return self.__UppaalFlat11_LocationType31

    @UppaalFlat11_LocationType31.setter
    def UppaalFlat11_LocationType31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UppaalFlat11_LocationType__UppaalFlat11_LocationType31", None)
        self.__UppaalFlat11_LocationType31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UppaalFlat11_NameType32"):
                opp_val = getattr(old_value, "UppaalFlat11_NameType32", None)
                if opp_val == self:
                    setattr(old_value, "UppaalFlat11_NameType32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UppaalFlat11_NameType32"):
                opp_val = getattr(value, "UppaalFlat11_NameType32", None)
                setattr(value, "UppaalFlat11_NameType32", self)

    @property
    def UppaalFlat11_LocationType53(self):
        return self.__UppaalFlat11_LocationType53

    @UppaalFlat11_LocationType53.setter
    def UppaalFlat11_LocationType53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UppaalFlat11_LocationType__UppaalFlat11_LocationType53", None)
        self.__UppaalFlat11_LocationType53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UppaalFlat11_TemplateType52"):
                opp_val = getattr(old_value, "UppaalFlat11_TemplateType52", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UppaalFlat11_TemplateType52"):
                opp_val = getattr(value, "UppaalFlat11_TemplateType52", None)
                if opp_val is None:
                    setattr(value, "UppaalFlat11_TemplateType52", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UppaalFlat11_LocationType(self):
        return self.__UppaalFlat11_LocationType

    @UppaalFlat11_LocationType.setter
    def UppaalFlat11_LocationType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UppaalFlat11_LocationType__UppaalFlat11_LocationType", None)
        self.__UppaalFlat11_LocationType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UppaalFlat11_DocumentRoot11"):
                opp_val = getattr(old_value, "UppaalFlat11_DocumentRoot11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UppaalFlat11_DocumentRoot11"):
                opp_val = getattr(value, "UppaalFlat11_DocumentRoot11", None)
                if opp_val is None:
                    setattr(value, "UppaalFlat11_DocumentRoot11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class UppaalFlat11_LabelType:

    def __init__(self, x: str, y: str, mixed: str, kind: str, UppaalFlat11_LabelType: "UppaalFlat11_DocumentRoot" = None, UppaalFlat11_LabelType35: "UppaalFlat11_LocationType" = None, UppaalFlat11_LabelType68: "UppaalFlat11_TransitionType" = None):
        self.x = x
        self.y = y
        self.mixed = mixed
        self.kind = kind
        self.UppaalFlat11_LabelType = UppaalFlat11_LabelType
        self.UppaalFlat11_LabelType35 = UppaalFlat11_LabelType35
        self.UppaalFlat11_LabelType68 = UppaalFlat11_LabelType68
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def y(self) -> str:
        return self.__y

    @y.setter
    def y(self, y: str):
        self.__y = y

    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def x(self) -> str:
        return self.__x

    @x.setter
    def x(self, x: str):
        self.__x = x

    @property
    def UppaalFlat11_LabelType68(self):
        return self.__UppaalFlat11_LabelType68

    @UppaalFlat11_LabelType68.setter
    def UppaalFlat11_LabelType68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UppaalFlat11_LabelType__UppaalFlat11_LabelType68", None)
        self.__UppaalFlat11_LabelType68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UppaalFlat11_TransitionType67"):
                opp_val = getattr(old_value, "UppaalFlat11_TransitionType67", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UppaalFlat11_TransitionType67"):
                opp_val = getattr(value, "UppaalFlat11_TransitionType67", None)
                if opp_val is None:
                    setattr(value, "UppaalFlat11_TransitionType67", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UppaalFlat11_LabelType(self):
        return self.__UppaalFlat11_LabelType

    @UppaalFlat11_LabelType.setter
    def UppaalFlat11_LabelType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UppaalFlat11_LabelType__UppaalFlat11_LabelType", None)
        self.__UppaalFlat11_LabelType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UppaalFlat11_DocumentRoot9"):
                opp_val = getattr(old_value, "UppaalFlat11_DocumentRoot9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UppaalFlat11_DocumentRoot9"):
                opp_val = getattr(value, "UppaalFlat11_DocumentRoot9", None)
                if opp_val is None:
                    setattr(value, "UppaalFlat11_DocumentRoot9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UppaalFlat11_LabelType35(self):
        return self.__UppaalFlat11_LabelType35

    @UppaalFlat11_LabelType35.setter
    def UppaalFlat11_LabelType35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UppaalFlat11_LabelType__UppaalFlat11_LabelType35", None)
        self.__UppaalFlat11_LabelType35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UppaalFlat11_LocationType34"):
                opp_val = getattr(old_value, "UppaalFlat11_LocationType34", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UppaalFlat11_LocationType34"):
                opp_val = getattr(value, "UppaalFlat11_LocationType34", None)
                if opp_val is None:
                    setattr(value, "UppaalFlat11_LocationType34", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class UppaalFlat11_InitType:

    def __init__(self, ref: str, UppaalFlat11_InitType: "UppaalFlat11_DocumentRoot" = None, UppaalFlat11_InitType56: "UppaalFlat11_TemplateType" = None):
        self.ref = ref
        self.UppaalFlat11_InitType = UppaalFlat11_InitType
        self.UppaalFlat11_InitType56 = UppaalFlat11_InitType56
        
    @property
    def ref(self) -> str:
        return self.__ref

    @ref.setter
    def ref(self, ref: str):
        self.__ref = ref

    @property
    def UppaalFlat11_InitType(self):
        return self.__UppaalFlat11_InitType

    @UppaalFlat11_InitType.setter
    def UppaalFlat11_InitType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UppaalFlat11_InitType__UppaalFlat11_InitType", None)
        self.__UppaalFlat11_InitType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UppaalFlat11_DocumentRoot7"):
                opp_val = getattr(old_value, "UppaalFlat11_DocumentRoot7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UppaalFlat11_DocumentRoot7"):
                opp_val = getattr(value, "UppaalFlat11_DocumentRoot7", None)
                if opp_val is None:
                    setattr(value, "UppaalFlat11_DocumentRoot7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UppaalFlat11_InitType56(self):
        return self.__UppaalFlat11_InitType56

    @UppaalFlat11_InitType56.setter
    def UppaalFlat11_InitType56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UppaalFlat11_InitType__UppaalFlat11_InitType56", None)
        self.__UppaalFlat11_InitType56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UppaalFlat11_TemplateType55"):
                opp_val = getattr(old_value, "UppaalFlat11_TemplateType55", None)
                if opp_val == self:
                    setattr(old_value, "UppaalFlat11_TemplateType55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UppaalFlat11_TemplateType55"):
                opp_val = getattr(value, "UppaalFlat11_TemplateType55", None)
                setattr(value, "UppaalFlat11_TemplateType55", self)

class UppaalFlat11_DocumentRoot:

    def __init__(self, mixed: str, declaration: str, instantiation: str, imports: str, system: str, UppaalFlat11_DocumentRoot: set["UppaalFlat11_EStringToStringMapEntry"] = None, UppaalFlat11_DocumentRoot2: set["UppaalFlat11_EStringToStringMapEntry"] = None, UppaalFlat11_DocumentRoot5: set["UppaalFlat11_CommittedType"] = None, UppaalFlat11_DocumentRoot7: set["UppaalFlat11_InitType"] = None, UppaalFlat11_DocumentRoot9: set["UppaalFlat11_LabelType"] = None, UppaalFlat11_DocumentRoot11: set["UppaalFlat11_LocationType"] = None, UppaalFlat11_DocumentRoot17: set["UppaalFlat11_NtaType"] = None, UppaalFlat11_DocumentRoot19: set["UppaalFlat11_ParameterType"] = None, UppaalFlat11_DocumentRoot21: set["UppaalFlat11_SourceType"] = None, UppaalFlat11_DocumentRoot13: set["UppaalFlat11_NailType"] = None, UppaalFlat11_DocumentRoot15: set["UppaalFlat11_NameType"] = None, UppaalFlat11_DocumentRoot25: set["UppaalFlat11_TemplateType"] = None, UppaalFlat11_DocumentRoot27: set["UppaalFlat11_TransitionType"] = None, UppaalFlat11_DocumentRoot29: set["UppaalFlat11_UrgentType"] = None, UppaalFlat11_DocumentRoot23: set["UppaalFlat11_TargetType"] = None):
        self.mixed = mixed
        self.declaration = declaration
        self.instantiation = instantiation
        self.imports = imports
        self.system = system
        self.UppaalFlat11_DocumentRoot = UppaalFlat11_DocumentRoot if UppaalFlat11_DocumentRoot is not None else set()
        self.UppaalFlat11_DocumentRoot2 = UppaalFlat11_DocumentRoot2 if UppaalFlat11_DocumentRoot2 is not None else set()
        self.UppaalFlat11_DocumentRoot5 = UppaalFlat11_DocumentRoot5 if UppaalFlat11_DocumentRoot5 is not None else set()
        self.UppaalFlat11_DocumentRoot7 = UppaalFlat11_DocumentRoot7 if UppaalFlat11_DocumentRoot7 is not None else set()
        self.UppaalFlat11_DocumentRoot9 = UppaalFlat11_DocumentRoot9 if UppaalFlat11_DocumentRoot9 is not None else set()
        self.UppaalFlat11_DocumentRoot11 = UppaalFlat11_DocumentRoot11 if UppaalFlat11_DocumentRoot11 is not None else set()
        self.UppaalFlat11_DocumentRoot17 = UppaalFlat11_DocumentRoot17 if UppaalFlat11_DocumentRoot17 is not None else set()
        self.UppaalFlat11_DocumentRoot19 = UppaalFlat11_DocumentRoot19 if UppaalFlat11_DocumentRoot19 is not None else set()
        self.UppaalFlat11_DocumentRoot21 = UppaalFlat11_DocumentRoot21 if UppaalFlat11_DocumentRoot21 is not None else set()
        self.UppaalFlat11_DocumentRoot13 = UppaalFlat11_DocumentRoot13 if UppaalFlat11_DocumentRoot13 is not None else set()
        self.UppaalFlat11_DocumentRoot15 = UppaalFlat11_DocumentRoot15 if UppaalFlat11_DocumentRoot15 is not None else set()
        self.UppaalFlat11_DocumentRoot25 = UppaalFlat11_DocumentRoot25 if UppaalFlat11_DocumentRoot25 is not None else set()
        self.UppaalFlat11_DocumentRoot27 = UppaalFlat11_DocumentRoot27 if UppaalFlat11_DocumentRoot27 is not None else set()
        self.UppaalFlat11_DocumentRoot29 = UppaalFlat11_DocumentRoot29 if UppaalFlat11_DocumentRoot29 is not None else set()
        self.UppaalFlat11_DocumentRoot23 = UppaalFlat11_DocumentRoot23 if UppaalFlat11_DocumentRoot23 is not None else set()
        
    @property
    def declaration(self) -> str:
        return self.__declaration

    @declaration.setter
    def declaration(self, declaration: str):
        self.__declaration = declaration

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def imports(self) -> str:
        return self.__imports

    @imports.setter
    def imports(self, imports: str):
        self.__imports = imports

    @property
    def system(self) -> str:
        return self.__system

    @system.setter
    def system(self, system: str):
        self.__system = system

    @property
    def instantiation(self) -> str:
        return self.__instantiation

    @instantiation.setter
    def instantiation(self, instantiation: str):
        self.__instantiation = instantiation

    @property
    def UppaalFlat11_DocumentRoot19(self):
        return self.__UppaalFlat11_DocumentRoot19

    @UppaalFlat11_DocumentRoot19.setter
    def UppaalFlat11_DocumentRoot19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UppaalFlat11_DocumentRoot__UppaalFlat11_DocumentRoot19", None)
        self.__UppaalFlat11_DocumentRoot19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UppaalFlat11_ParameterType"):
                    opp_val = getattr(item, "UppaalFlat11_ParameterType", None)
                    
                    if opp_val == self:
                        setattr(item, "UppaalFlat11_ParameterType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UppaalFlat11_ParameterType"):
                    opp_val = getattr(item, "UppaalFlat11_ParameterType", None)
                    
                    setattr(item, "UppaalFlat11_ParameterType", self)
                    

    @property
    def UppaalFlat11_DocumentRoot17(self):
        return self.__UppaalFlat11_DocumentRoot17

    @UppaalFlat11_DocumentRoot17.setter
    def UppaalFlat11_DocumentRoot17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UppaalFlat11_DocumentRoot__UppaalFlat11_DocumentRoot17", None)
        self.__UppaalFlat11_DocumentRoot17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UppaalFlat11_NtaType"):
                    opp_val = getattr(item, "UppaalFlat11_NtaType", None)
                    
                    if opp_val == self:
                        setattr(item, "UppaalFlat11_NtaType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UppaalFlat11_NtaType"):
                    opp_val = getattr(item, "UppaalFlat11_NtaType", None)
                    
                    setattr(item, "UppaalFlat11_NtaType", self)
                    

    @property
    def UppaalFlat11_DocumentRoot23(self):
        return self.__UppaalFlat11_DocumentRoot23

    @UppaalFlat11_DocumentRoot23.setter
    def UppaalFlat11_DocumentRoot23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UppaalFlat11_DocumentRoot__UppaalFlat11_DocumentRoot23", None)
        self.__UppaalFlat11_DocumentRoot23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UppaalFlat11_TargetType"):
                    opp_val = getattr(item, "UppaalFlat11_TargetType", None)
                    
                    if opp_val == self:
                        setattr(item, "UppaalFlat11_TargetType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UppaalFlat11_TargetType"):
                    opp_val = getattr(item, "UppaalFlat11_TargetType", None)
                    
                    setattr(item, "UppaalFlat11_TargetType", self)
                    

    @property
    def UppaalFlat11_DocumentRoot5(self):
        return self.__UppaalFlat11_DocumentRoot5

    @UppaalFlat11_DocumentRoot5.setter
    def UppaalFlat11_DocumentRoot5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UppaalFlat11_DocumentRoot__UppaalFlat11_DocumentRoot5", None)
        self.__UppaalFlat11_DocumentRoot5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UppaalFlat11_CommittedType"):
                    opp_val = getattr(item, "UppaalFlat11_CommittedType", None)
                    
                    if opp_val == self:
                        setattr(item, "UppaalFlat11_CommittedType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UppaalFlat11_CommittedType"):
                    opp_val = getattr(item, "UppaalFlat11_CommittedType", None)
                    
                    setattr(item, "UppaalFlat11_CommittedType", self)
                    

    @property
    def UppaalFlat11_DocumentRoot(self):
        return self.__UppaalFlat11_DocumentRoot

    @UppaalFlat11_DocumentRoot.setter
    def UppaalFlat11_DocumentRoot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UppaalFlat11_DocumentRoot__UppaalFlat11_DocumentRoot", None)
        self.__UppaalFlat11_DocumentRoot = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UppaalFlat11_EStringToStringMapEntry"):
                    opp_val = getattr(item, "UppaalFlat11_EStringToStringMapEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "UppaalFlat11_EStringToStringMapEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UppaalFlat11_EStringToStringMapEntry"):
                    opp_val = getattr(item, "UppaalFlat11_EStringToStringMapEntry", None)
                    
                    setattr(item, "UppaalFlat11_EStringToStringMapEntry", self)
                    

    @property
    def UppaalFlat11_DocumentRoot11(self):
        return self.__UppaalFlat11_DocumentRoot11

    @UppaalFlat11_DocumentRoot11.setter
    def UppaalFlat11_DocumentRoot11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UppaalFlat11_DocumentRoot__UppaalFlat11_DocumentRoot11", None)
        self.__UppaalFlat11_DocumentRoot11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UppaalFlat11_LocationType"):
                    opp_val = getattr(item, "UppaalFlat11_LocationType", None)
                    
                    if opp_val == self:
                        setattr(item, "UppaalFlat11_LocationType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UppaalFlat11_LocationType"):
                    opp_val = getattr(item, "UppaalFlat11_LocationType", None)
                    
                    setattr(item, "UppaalFlat11_LocationType", self)
                    

    @property
    def UppaalFlat11_DocumentRoot15(self):
        return self.__UppaalFlat11_DocumentRoot15

    @UppaalFlat11_DocumentRoot15.setter
    def UppaalFlat11_DocumentRoot15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UppaalFlat11_DocumentRoot__UppaalFlat11_DocumentRoot15", None)
        self.__UppaalFlat11_DocumentRoot15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UppaalFlat11_NameType"):
                    opp_val = getattr(item, "UppaalFlat11_NameType", None)
                    
                    if opp_val == self:
                        setattr(item, "UppaalFlat11_NameType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UppaalFlat11_NameType"):
                    opp_val = getattr(item, "UppaalFlat11_NameType", None)
                    
                    setattr(item, "UppaalFlat11_NameType", self)
                    

    @property
    def UppaalFlat11_DocumentRoot2(self):
        return self.__UppaalFlat11_DocumentRoot2

    @UppaalFlat11_DocumentRoot2.setter
    def UppaalFlat11_DocumentRoot2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UppaalFlat11_DocumentRoot__UppaalFlat11_DocumentRoot2", None)
        self.__UppaalFlat11_DocumentRoot2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UppaalFlat11_EStringToStringMapEntry3"):
                    opp_val = getattr(item, "UppaalFlat11_EStringToStringMapEntry3", None)
                    
                    if opp_val == self:
                        setattr(item, "UppaalFlat11_EStringToStringMapEntry3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UppaalFlat11_EStringToStringMapEntry3"):
                    opp_val = getattr(item, "UppaalFlat11_EStringToStringMapEntry3", None)
                    
                    setattr(item, "UppaalFlat11_EStringToStringMapEntry3", self)
                    

    @property
    def UppaalFlat11_DocumentRoot21(self):
        return self.__UppaalFlat11_DocumentRoot21

    @UppaalFlat11_DocumentRoot21.setter
    def UppaalFlat11_DocumentRoot21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UppaalFlat11_DocumentRoot__UppaalFlat11_DocumentRoot21", None)
        self.__UppaalFlat11_DocumentRoot21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UppaalFlat11_SourceType"):
                    opp_val = getattr(item, "UppaalFlat11_SourceType", None)
                    
                    if opp_val == self:
                        setattr(item, "UppaalFlat11_SourceType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UppaalFlat11_SourceType"):
                    opp_val = getattr(item, "UppaalFlat11_SourceType", None)
                    
                    setattr(item, "UppaalFlat11_SourceType", self)
                    

    @property
    def UppaalFlat11_DocumentRoot25(self):
        return self.__UppaalFlat11_DocumentRoot25

    @UppaalFlat11_DocumentRoot25.setter
    def UppaalFlat11_DocumentRoot25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UppaalFlat11_DocumentRoot__UppaalFlat11_DocumentRoot25", None)
        self.__UppaalFlat11_DocumentRoot25 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UppaalFlat11_TemplateType"):
                    opp_val = getattr(item, "UppaalFlat11_TemplateType", None)
                    
                    if opp_val == self:
                        setattr(item, "UppaalFlat11_TemplateType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UppaalFlat11_TemplateType"):
                    opp_val = getattr(item, "UppaalFlat11_TemplateType", None)
                    
                    setattr(item, "UppaalFlat11_TemplateType", self)
                    

    @property
    def UppaalFlat11_DocumentRoot9(self):
        return self.__UppaalFlat11_DocumentRoot9

    @UppaalFlat11_DocumentRoot9.setter
    def UppaalFlat11_DocumentRoot9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UppaalFlat11_DocumentRoot__UppaalFlat11_DocumentRoot9", None)
        self.__UppaalFlat11_DocumentRoot9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UppaalFlat11_LabelType"):
                    opp_val = getattr(item, "UppaalFlat11_LabelType", None)
                    
                    if opp_val == self:
                        setattr(item, "UppaalFlat11_LabelType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UppaalFlat11_LabelType"):
                    opp_val = getattr(item, "UppaalFlat11_LabelType", None)
                    
                    setattr(item, "UppaalFlat11_LabelType", self)
                    

    @property
    def UppaalFlat11_DocumentRoot29(self):
        return self.__UppaalFlat11_DocumentRoot29

    @UppaalFlat11_DocumentRoot29.setter
    def UppaalFlat11_DocumentRoot29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UppaalFlat11_DocumentRoot__UppaalFlat11_DocumentRoot29", None)
        self.__UppaalFlat11_DocumentRoot29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UppaalFlat11_UrgentType"):
                    opp_val = getattr(item, "UppaalFlat11_UrgentType", None)
                    
                    if opp_val == self:
                        setattr(item, "UppaalFlat11_UrgentType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UppaalFlat11_UrgentType"):
                    opp_val = getattr(item, "UppaalFlat11_UrgentType", None)
                    
                    setattr(item, "UppaalFlat11_UrgentType", self)
                    

    @property
    def UppaalFlat11_DocumentRoot27(self):
        return self.__UppaalFlat11_DocumentRoot27

    @UppaalFlat11_DocumentRoot27.setter
    def UppaalFlat11_DocumentRoot27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UppaalFlat11_DocumentRoot__UppaalFlat11_DocumentRoot27", None)
        self.__UppaalFlat11_DocumentRoot27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UppaalFlat11_TransitionType"):
                    opp_val = getattr(item, "UppaalFlat11_TransitionType", None)
                    
                    if opp_val == self:
                        setattr(item, "UppaalFlat11_TransitionType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UppaalFlat11_TransitionType"):
                    opp_val = getattr(item, "UppaalFlat11_TransitionType", None)
                    
                    setattr(item, "UppaalFlat11_TransitionType", self)
                    

    @property
    def UppaalFlat11_DocumentRoot7(self):
        return self.__UppaalFlat11_DocumentRoot7

    @UppaalFlat11_DocumentRoot7.setter
    def UppaalFlat11_DocumentRoot7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UppaalFlat11_DocumentRoot__UppaalFlat11_DocumentRoot7", None)
        self.__UppaalFlat11_DocumentRoot7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UppaalFlat11_InitType"):
                    opp_val = getattr(item, "UppaalFlat11_InitType", None)
                    
                    if opp_val == self:
                        setattr(item, "UppaalFlat11_InitType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UppaalFlat11_InitType"):
                    opp_val = getattr(item, "UppaalFlat11_InitType", None)
                    
                    setattr(item, "UppaalFlat11_InitType", self)
                    

    @property
    def UppaalFlat11_DocumentRoot13(self):
        return self.__UppaalFlat11_DocumentRoot13

    @UppaalFlat11_DocumentRoot13.setter
    def UppaalFlat11_DocumentRoot13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UppaalFlat11_DocumentRoot__UppaalFlat11_DocumentRoot13", None)
        self.__UppaalFlat11_DocumentRoot13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UppaalFlat11_NailType"):
                    opp_val = getattr(item, "UppaalFlat11_NailType", None)
                    
                    if opp_val == self:
                        setattr(item, "UppaalFlat11_NailType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UppaalFlat11_NailType"):
                    opp_val = getattr(item, "UppaalFlat11_NailType", None)
                    
                    setattr(item, "UppaalFlat11_NailType", self)
                    

class UppaalFlat11_CommittedType:

    pass
class UppaalFlat11_EStringToStringMapEntry:

    pass