from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class uppaal_TargetType:

    def __init__(self, ref: str, uppaal_TargetType: "uppaal_DocumentRoot" = None, uppaal_TargetType65: "uppaal_TransitionType" = None):
        self.ref = ref
        self.uppaal_TargetType = uppaal_TargetType
        self.uppaal_TargetType65 = uppaal_TargetType65
        
    @property
    def ref(self) -> str:
        return self.__ref

    @ref.setter
    def ref(self, ref: str):
        self.__ref = ref

    @property
    def uppaal_TargetType65(self):
        return self.__uppaal_TargetType65

    @uppaal_TargetType65.setter
    def uppaal_TargetType65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uppaal_TargetType__uppaal_TargetType65", None)
        self.__uppaal_TargetType65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uppaal_TransitionType64"):
                opp_val = getattr(old_value, "uppaal_TransitionType64", None)
                if opp_val == self:
                    setattr(old_value, "uppaal_TransitionType64", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uppaal_TransitionType64"):
                opp_val = getattr(value, "uppaal_TransitionType64", None)
                setattr(value, "uppaal_TransitionType64", self)

    @property
    def uppaal_TargetType(self):
        return self.__uppaal_TargetType

    @uppaal_TargetType.setter
    def uppaal_TargetType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uppaal_TargetType__uppaal_TargetType", None)
        self.__uppaal_TargetType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uppaal_DocumentRoot23"):
                opp_val = getattr(old_value, "uppaal_DocumentRoot23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uppaal_DocumentRoot23"):
                opp_val = getattr(value, "uppaal_DocumentRoot23", None)
                if opp_val is None:
                    setattr(value, "uppaal_DocumentRoot23", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class uppaal_SourceType:

    def __init__(self, ref: str, uppaal_SourceType: "uppaal_DocumentRoot" = None, uppaal_SourceType62: "uppaal_TransitionType" = None):
        self.ref = ref
        self.uppaal_SourceType = uppaal_SourceType
        self.uppaal_SourceType62 = uppaal_SourceType62
        
    @property
    def ref(self) -> str:
        return self.__ref

    @ref.setter
    def ref(self, ref: str):
        self.__ref = ref

    @property
    def uppaal_SourceType(self):
        return self.__uppaal_SourceType

    @uppaal_SourceType.setter
    def uppaal_SourceType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uppaal_SourceType__uppaal_SourceType", None)
        self.__uppaal_SourceType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uppaal_DocumentRoot21"):
                opp_val = getattr(old_value, "uppaal_DocumentRoot21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uppaal_DocumentRoot21"):
                opp_val = getattr(value, "uppaal_DocumentRoot21", None)
                if opp_val is None:
                    setattr(value, "uppaal_DocumentRoot21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uppaal_SourceType62(self):
        return self.__uppaal_SourceType62

    @uppaal_SourceType62.setter
    def uppaal_SourceType62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uppaal_SourceType__uppaal_SourceType62", None)
        self.__uppaal_SourceType62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uppaal_TransitionType61"):
                opp_val = getattr(old_value, "uppaal_TransitionType61", None)
                if opp_val == self:
                    setattr(old_value, "uppaal_TransitionType61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uppaal_TransitionType61"):
                opp_val = getattr(value, "uppaal_TransitionType61", None)
                setattr(value, "uppaal_TransitionType61", self)

class uppaal_ParameterType:

    def __init__(self, mixed: str, x: str, y: str, uppaal_ParameterType: "uppaal_DocumentRoot" = None, uppaal_ParameterType50: "uppaal_TemplateType" = None):
        self.mixed = mixed
        self.x = x
        self.y = y
        self.uppaal_ParameterType = uppaal_ParameterType
        self.uppaal_ParameterType50 = uppaal_ParameterType50
        
    @property
    def x(self) -> str:
        return self.__x

    @x.setter
    def x(self, x: str):
        self.__x = x

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
    def uppaal_ParameterType(self):
        return self.__uppaal_ParameterType

    @uppaal_ParameterType.setter
    def uppaal_ParameterType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uppaal_ParameterType__uppaal_ParameterType", None)
        self.__uppaal_ParameterType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uppaal_DocumentRoot19"):
                opp_val = getattr(old_value, "uppaal_DocumentRoot19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uppaal_DocumentRoot19"):
                opp_val = getattr(value, "uppaal_DocumentRoot19", None)
                if opp_val is None:
                    setattr(value, "uppaal_DocumentRoot19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uppaal_ParameterType50(self):
        return self.__uppaal_ParameterType50

    @uppaal_ParameterType50.setter
    def uppaal_ParameterType50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uppaal_ParameterType__uppaal_ParameterType50", None)
        self.__uppaal_ParameterType50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uppaal_TemplateType49"):
                opp_val = getattr(old_value, "uppaal_TemplateType49", None)
                if opp_val == self:
                    setattr(old_value, "uppaal_TemplateType49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uppaal_TemplateType49"):
                opp_val = getattr(value, "uppaal_TemplateType49", None)
                setattr(value, "uppaal_TemplateType49", self)

class uppaal_NtaType:

    def __init__(self, declaration: str, instantiation: str, system: str, imports: str, uppaal_NtaType: "uppaal_DocumentRoot" = None, uppaal_NtaType43: set["uppaal_TemplateType"] = None):
        self.declaration = declaration
        self.instantiation = instantiation
        self.system = system
        self.imports = imports
        self.uppaal_NtaType = uppaal_NtaType
        self.uppaal_NtaType43 = uppaal_NtaType43 if uppaal_NtaType43 is not None else set()
        
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
    def declaration(self) -> str:
        return self.__declaration

    @declaration.setter
    def declaration(self, declaration: str):
        self.__declaration = declaration

    @property
    def imports(self) -> str:
        return self.__imports

    @imports.setter
    def imports(self, imports: str):
        self.__imports = imports

    @property
    def uppaal_NtaType43(self):
        return self.__uppaal_NtaType43

    @uppaal_NtaType43.setter
    def uppaal_NtaType43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uppaal_NtaType__uppaal_NtaType43", None)
        self.__uppaal_NtaType43 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uppaal_TemplateType44"):
                    opp_val = getattr(item, "uppaal_TemplateType44", None)
                    
                    if opp_val == self:
                        setattr(item, "uppaal_TemplateType44", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uppaal_TemplateType44"):
                    opp_val = getattr(item, "uppaal_TemplateType44", None)
                    
                    setattr(item, "uppaal_TemplateType44", self)
                    

    @property
    def uppaal_NtaType(self):
        return self.__uppaal_NtaType

    @uppaal_NtaType.setter
    def uppaal_NtaType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uppaal_NtaType__uppaal_NtaType", None)
        self.__uppaal_NtaType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uppaal_DocumentRoot17"):
                opp_val = getattr(old_value, "uppaal_DocumentRoot17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uppaal_DocumentRoot17"):
                opp_val = getattr(value, "uppaal_DocumentRoot17", None)
                if opp_val is None:
                    setattr(value, "uppaal_DocumentRoot17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class uppaal_UrgentType:

    pass
class uppaal_TransitionType:

    def __init__(self, x: str, y: str, color: str, id: str, uppaal_TransitionType: "uppaal_DocumentRoot" = None, uppaal_TransitionType59: "uppaal_TemplateType" = None, uppaal_TransitionType61: "uppaal_SourceType" = None, uppaal_TransitionType64: "uppaal_TargetType" = None, uppaal_TransitionType67: set["uppaal_LabelType"] = None, uppaal_TransitionType70: set["uppaal_NailType"] = None):
        self.x = x
        self.y = y
        self.color = color
        self.id = id
        self.uppaal_TransitionType = uppaal_TransitionType
        self.uppaal_TransitionType59 = uppaal_TransitionType59
        self.uppaal_TransitionType61 = uppaal_TransitionType61
        self.uppaal_TransitionType64 = uppaal_TransitionType64
        self.uppaal_TransitionType67 = uppaal_TransitionType67 if uppaal_TransitionType67 is not None else set()
        self.uppaal_TransitionType70 = uppaal_TransitionType70 if uppaal_TransitionType70 is not None else set()
        
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
    def uppaal_TransitionType64(self):
        return self.__uppaal_TransitionType64

    @uppaal_TransitionType64.setter
    def uppaal_TransitionType64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uppaal_TransitionType__uppaal_TransitionType64", None)
        self.__uppaal_TransitionType64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uppaal_TargetType65"):
                opp_val = getattr(old_value, "uppaal_TargetType65", None)
                if opp_val == self:
                    setattr(old_value, "uppaal_TargetType65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uppaal_TargetType65"):
                opp_val = getattr(value, "uppaal_TargetType65", None)
                setattr(value, "uppaal_TargetType65", self)

    @property
    def uppaal_TransitionType59(self):
        return self.__uppaal_TransitionType59

    @uppaal_TransitionType59.setter
    def uppaal_TransitionType59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uppaal_TransitionType__uppaal_TransitionType59", None)
        self.__uppaal_TransitionType59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uppaal_TemplateType58"):
                opp_val = getattr(old_value, "uppaal_TemplateType58", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uppaal_TemplateType58"):
                opp_val = getattr(value, "uppaal_TemplateType58", None)
                if opp_val is None:
                    setattr(value, "uppaal_TemplateType58", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uppaal_TransitionType61(self):
        return self.__uppaal_TransitionType61

    @uppaal_TransitionType61.setter
    def uppaal_TransitionType61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uppaal_TransitionType__uppaal_TransitionType61", None)
        self.__uppaal_TransitionType61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uppaal_SourceType62"):
                opp_val = getattr(old_value, "uppaal_SourceType62", None)
                if opp_val == self:
                    setattr(old_value, "uppaal_SourceType62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uppaal_SourceType62"):
                opp_val = getattr(value, "uppaal_SourceType62", None)
                setattr(value, "uppaal_SourceType62", self)

    @property
    def uppaal_TransitionType70(self):
        return self.__uppaal_TransitionType70

    @uppaal_TransitionType70.setter
    def uppaal_TransitionType70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uppaal_TransitionType__uppaal_TransitionType70", None)
        self.__uppaal_TransitionType70 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uppaal_NailType71"):
                    opp_val = getattr(item, "uppaal_NailType71", None)
                    
                    if opp_val == self:
                        setattr(item, "uppaal_NailType71", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uppaal_NailType71"):
                    opp_val = getattr(item, "uppaal_NailType71", None)
                    
                    setattr(item, "uppaal_NailType71", self)
                    

    @property
    def uppaal_TransitionType67(self):
        return self.__uppaal_TransitionType67

    @uppaal_TransitionType67.setter
    def uppaal_TransitionType67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uppaal_TransitionType__uppaal_TransitionType67", None)
        self.__uppaal_TransitionType67 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uppaal_LabelType68"):
                    opp_val = getattr(item, "uppaal_LabelType68", None)
                    
                    if opp_val == self:
                        setattr(item, "uppaal_LabelType68", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uppaal_LabelType68"):
                    opp_val = getattr(item, "uppaal_LabelType68", None)
                    
                    setattr(item, "uppaal_LabelType68", self)
                    

    @property
    def uppaal_TransitionType(self):
        return self.__uppaal_TransitionType

    @uppaal_TransitionType.setter
    def uppaal_TransitionType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uppaal_TransitionType__uppaal_TransitionType", None)
        self.__uppaal_TransitionType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uppaal_DocumentRoot27"):
                opp_val = getattr(old_value, "uppaal_DocumentRoot27", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uppaal_DocumentRoot27"):
                opp_val = getattr(value, "uppaal_DocumentRoot27", None)
                if opp_val is None:
                    setattr(value, "uppaal_DocumentRoot27", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class uppaal_TemplateType:

    def __init__(self, declaration: str, uppaal_TemplateType: "uppaal_DocumentRoot" = None, uppaal_TemplateType44: "uppaal_NtaType" = None, uppaal_TemplateType49: "uppaal_ParameterType" = None, uppaal_TemplateType52: set["uppaal_LocationType"] = None, uppaal_TemplateType55: "uppaal_InitType" = None, uppaal_TemplateType58: set["uppaal_TransitionType"] = None, uppaal_TemplateType46: "uppaal_NameType" = None):
        self.declaration = declaration
        self.uppaal_TemplateType = uppaal_TemplateType
        self.uppaal_TemplateType44 = uppaal_TemplateType44
        self.uppaal_TemplateType49 = uppaal_TemplateType49
        self.uppaal_TemplateType52 = uppaal_TemplateType52 if uppaal_TemplateType52 is not None else set()
        self.uppaal_TemplateType55 = uppaal_TemplateType55
        self.uppaal_TemplateType58 = uppaal_TemplateType58 if uppaal_TemplateType58 is not None else set()
        self.uppaal_TemplateType46 = uppaal_TemplateType46
        
    @property
    def declaration(self) -> str:
        return self.__declaration

    @declaration.setter
    def declaration(self, declaration: str):
        self.__declaration = declaration

    @property
    def uppaal_TemplateType55(self):
        return self.__uppaal_TemplateType55

    @uppaal_TemplateType55.setter
    def uppaal_TemplateType55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uppaal_TemplateType__uppaal_TemplateType55", None)
        self.__uppaal_TemplateType55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uppaal_InitType56"):
                opp_val = getattr(old_value, "uppaal_InitType56", None)
                if opp_val == self:
                    setattr(old_value, "uppaal_InitType56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uppaal_InitType56"):
                opp_val = getattr(value, "uppaal_InitType56", None)
                setattr(value, "uppaal_InitType56", self)

    @property
    def uppaal_TemplateType58(self):
        return self.__uppaal_TemplateType58

    @uppaal_TemplateType58.setter
    def uppaal_TemplateType58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uppaal_TemplateType__uppaal_TemplateType58", None)
        self.__uppaal_TemplateType58 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uppaal_TransitionType59"):
                    opp_val = getattr(item, "uppaal_TransitionType59", None)
                    
                    if opp_val == self:
                        setattr(item, "uppaal_TransitionType59", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uppaal_TransitionType59"):
                    opp_val = getattr(item, "uppaal_TransitionType59", None)
                    
                    setattr(item, "uppaal_TransitionType59", self)
                    

    @property
    def uppaal_TemplateType(self):
        return self.__uppaal_TemplateType

    @uppaal_TemplateType.setter
    def uppaal_TemplateType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uppaal_TemplateType__uppaal_TemplateType", None)
        self.__uppaal_TemplateType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uppaal_DocumentRoot25"):
                opp_val = getattr(old_value, "uppaal_DocumentRoot25", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uppaal_DocumentRoot25"):
                opp_val = getattr(value, "uppaal_DocumentRoot25", None)
                if opp_val is None:
                    setattr(value, "uppaal_DocumentRoot25", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uppaal_TemplateType46(self):
        return self.__uppaal_TemplateType46

    @uppaal_TemplateType46.setter
    def uppaal_TemplateType46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uppaal_TemplateType__uppaal_TemplateType46", None)
        self.__uppaal_TemplateType46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uppaal_NameType47"):
                opp_val = getattr(old_value, "uppaal_NameType47", None)
                if opp_val == self:
                    setattr(old_value, "uppaal_NameType47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uppaal_NameType47"):
                opp_val = getattr(value, "uppaal_NameType47", None)
                setattr(value, "uppaal_NameType47", self)

    @property
    def uppaal_TemplateType44(self):
        return self.__uppaal_TemplateType44

    @uppaal_TemplateType44.setter
    def uppaal_TemplateType44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uppaal_TemplateType__uppaal_TemplateType44", None)
        self.__uppaal_TemplateType44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uppaal_NtaType43"):
                opp_val = getattr(old_value, "uppaal_NtaType43", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uppaal_NtaType43"):
                opp_val = getattr(value, "uppaal_NtaType43", None)
                if opp_val is None:
                    setattr(value, "uppaal_NtaType43", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uppaal_TemplateType52(self):
        return self.__uppaal_TemplateType52

    @uppaal_TemplateType52.setter
    def uppaal_TemplateType52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uppaal_TemplateType__uppaal_TemplateType52", None)
        self.__uppaal_TemplateType52 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uppaal_LocationType53"):
                    opp_val = getattr(item, "uppaal_LocationType53", None)
                    
                    if opp_val == self:
                        setattr(item, "uppaal_LocationType53", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uppaal_LocationType53"):
                    opp_val = getattr(item, "uppaal_LocationType53", None)
                    
                    setattr(item, "uppaal_LocationType53", self)
                    

    @property
    def uppaal_TemplateType49(self):
        return self.__uppaal_TemplateType49

    @uppaal_TemplateType49.setter
    def uppaal_TemplateType49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uppaal_TemplateType__uppaal_TemplateType49", None)
        self.__uppaal_TemplateType49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uppaal_ParameterType50"):
                opp_val = getattr(old_value, "uppaal_ParameterType50", None)
                if opp_val == self:
                    setattr(old_value, "uppaal_ParameterType50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uppaal_ParameterType50"):
                opp_val = getattr(value, "uppaal_ParameterType50", None)
                setattr(value, "uppaal_ParameterType50", self)

class uppaal_LabelType:

    def __init__(self, mixed: str, kind: str, x: str, y: str, uppaal_LabelType: "uppaal_DocumentRoot" = None, uppaal_LabelType35: "uppaal_LocationType" = None, uppaal_LabelType68: "uppaal_TransitionType" = None):
        self.mixed = mixed
        self.kind = kind
        self.x = x
        self.y = y
        self.uppaal_LabelType = uppaal_LabelType
        self.uppaal_LabelType35 = uppaal_LabelType35
        self.uppaal_LabelType68 = uppaal_LabelType68
        
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
    def uppaal_LabelType(self):
        return self.__uppaal_LabelType

    @uppaal_LabelType.setter
    def uppaal_LabelType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uppaal_LabelType__uppaal_LabelType", None)
        self.__uppaal_LabelType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uppaal_DocumentRoot9"):
                opp_val = getattr(old_value, "uppaal_DocumentRoot9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uppaal_DocumentRoot9"):
                opp_val = getattr(value, "uppaal_DocumentRoot9", None)
                if opp_val is None:
                    setattr(value, "uppaal_DocumentRoot9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uppaal_LabelType68(self):
        return self.__uppaal_LabelType68

    @uppaal_LabelType68.setter
    def uppaal_LabelType68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uppaal_LabelType__uppaal_LabelType68", None)
        self.__uppaal_LabelType68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uppaal_TransitionType67"):
                opp_val = getattr(old_value, "uppaal_TransitionType67", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uppaal_TransitionType67"):
                opp_val = getattr(value, "uppaal_TransitionType67", None)
                if opp_val is None:
                    setattr(value, "uppaal_TransitionType67", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uppaal_LabelType35(self):
        return self.__uppaal_LabelType35

    @uppaal_LabelType35.setter
    def uppaal_LabelType35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uppaal_LabelType__uppaal_LabelType35", None)
        self.__uppaal_LabelType35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uppaal_LocationType34"):
                opp_val = getattr(old_value, "uppaal_LocationType34", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uppaal_LocationType34"):
                opp_val = getattr(value, "uppaal_LocationType34", None)
                if opp_val is None:
                    setattr(value, "uppaal_LocationType34", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class uppaal_InitType:

    def __init__(self, ref: str, uppaal_InitType: "uppaal_DocumentRoot" = None, uppaal_InitType56: "uppaal_TemplateType" = None):
        self.ref = ref
        self.uppaal_InitType = uppaal_InitType
        self.uppaal_InitType56 = uppaal_InitType56
        
    @property
    def ref(self) -> str:
        return self.__ref

    @ref.setter
    def ref(self, ref: str):
        self.__ref = ref

    @property
    def uppaal_InitType(self):
        return self.__uppaal_InitType

    @uppaal_InitType.setter
    def uppaal_InitType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uppaal_InitType__uppaal_InitType", None)
        self.__uppaal_InitType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uppaal_DocumentRoot7"):
                opp_val = getattr(old_value, "uppaal_DocumentRoot7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uppaal_DocumentRoot7"):
                opp_val = getattr(value, "uppaal_DocumentRoot7", None)
                if opp_val is None:
                    setattr(value, "uppaal_DocumentRoot7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uppaal_InitType56(self):
        return self.__uppaal_InitType56

    @uppaal_InitType56.setter
    def uppaal_InitType56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uppaal_InitType__uppaal_InitType56", None)
        self.__uppaal_InitType56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uppaal_TemplateType55"):
                opp_val = getattr(old_value, "uppaal_TemplateType55", None)
                if opp_val == self:
                    setattr(old_value, "uppaal_TemplateType55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uppaal_TemplateType55"):
                opp_val = getattr(value, "uppaal_TemplateType55", None)
                setattr(value, "uppaal_TemplateType55", self)

class uppaal_NameType:

    def __init__(self, mixed: str, x: str, y: str, uppaal_NameType: "uppaal_DocumentRoot" = None, uppaal_NameType32: "uppaal_LocationType" = None, uppaal_NameType47: "uppaal_TemplateType" = None):
        self.mixed = mixed
        self.x = x
        self.y = y
        self.uppaal_NameType = uppaal_NameType
        self.uppaal_NameType32 = uppaal_NameType32
        self.uppaal_NameType47 = uppaal_NameType47
        
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
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def uppaal_NameType(self):
        return self.__uppaal_NameType

    @uppaal_NameType.setter
    def uppaal_NameType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uppaal_NameType__uppaal_NameType", None)
        self.__uppaal_NameType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uppaal_DocumentRoot15"):
                opp_val = getattr(old_value, "uppaal_DocumentRoot15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uppaal_DocumentRoot15"):
                opp_val = getattr(value, "uppaal_DocumentRoot15", None)
                if opp_val is None:
                    setattr(value, "uppaal_DocumentRoot15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uppaal_NameType47(self):
        return self.__uppaal_NameType47

    @uppaal_NameType47.setter
    def uppaal_NameType47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uppaal_NameType__uppaal_NameType47", None)
        self.__uppaal_NameType47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uppaal_TemplateType46"):
                opp_val = getattr(old_value, "uppaal_TemplateType46", None)
                if opp_val == self:
                    setattr(old_value, "uppaal_TemplateType46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uppaal_TemplateType46"):
                opp_val = getattr(value, "uppaal_TemplateType46", None)
                setattr(value, "uppaal_TemplateType46", self)

    @property
    def uppaal_NameType32(self):
        return self.__uppaal_NameType32

    @uppaal_NameType32.setter
    def uppaal_NameType32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uppaal_NameType__uppaal_NameType32", None)
        self.__uppaal_NameType32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uppaal_LocationType31"):
                opp_val = getattr(old_value, "uppaal_LocationType31", None)
                if opp_val == self:
                    setattr(old_value, "uppaal_LocationType31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uppaal_LocationType31"):
                opp_val = getattr(value, "uppaal_LocationType31", None)
                setattr(value, "uppaal_LocationType31", self)

class uppaal_NailType:

    def __init__(self, x: str, y: str, uppaal_NailType: "uppaal_DocumentRoot" = None, uppaal_NailType71: "uppaal_TransitionType" = None):
        self.x = x
        self.y = y
        self.uppaal_NailType = uppaal_NailType
        self.uppaal_NailType71 = uppaal_NailType71
        
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
    def uppaal_NailType71(self):
        return self.__uppaal_NailType71

    @uppaal_NailType71.setter
    def uppaal_NailType71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uppaal_NailType__uppaal_NailType71", None)
        self.__uppaal_NailType71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uppaal_TransitionType70"):
                opp_val = getattr(old_value, "uppaal_TransitionType70", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uppaal_TransitionType70"):
                opp_val = getattr(value, "uppaal_TransitionType70", None)
                if opp_val is None:
                    setattr(value, "uppaal_TransitionType70", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uppaal_NailType(self):
        return self.__uppaal_NailType

    @uppaal_NailType.setter
    def uppaal_NailType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uppaal_NailType__uppaal_NailType", None)
        self.__uppaal_NailType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uppaal_DocumentRoot13"):
                opp_val = getattr(old_value, "uppaal_DocumentRoot13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uppaal_DocumentRoot13"):
                opp_val = getattr(value, "uppaal_DocumentRoot13", None)
                if opp_val is None:
                    setattr(value, "uppaal_DocumentRoot13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class uppaal_LocationType:

    def __init__(self, color: str, id: str, x: str, y: str, uppaal_LocationType: "uppaal_DocumentRoot" = None, uppaal_LocationType37: "uppaal_UrgentType" = None, uppaal_LocationType40: "uppaal_CommittedType" = None, uppaal_LocationType31: "uppaal_NameType" = None, uppaal_LocationType34: set["uppaal_LabelType"] = None, uppaal_LocationType53: "uppaal_TemplateType" = None):
        self.color = color
        self.id = id
        self.x = x
        self.y = y
        self.uppaal_LocationType = uppaal_LocationType
        self.uppaal_LocationType37 = uppaal_LocationType37
        self.uppaal_LocationType40 = uppaal_LocationType40
        self.uppaal_LocationType31 = uppaal_LocationType31
        self.uppaal_LocationType34 = uppaal_LocationType34 if uppaal_LocationType34 is not None else set()
        self.uppaal_LocationType53 = uppaal_LocationType53
        
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
    def uppaal_LocationType37(self):
        return self.__uppaal_LocationType37

    @uppaal_LocationType37.setter
    def uppaal_LocationType37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uppaal_LocationType__uppaal_LocationType37", None)
        self.__uppaal_LocationType37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uppaal_UrgentType38"):
                opp_val = getattr(old_value, "uppaal_UrgentType38", None)
                if opp_val == self:
                    setattr(old_value, "uppaal_UrgentType38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uppaal_UrgentType38"):
                opp_val = getattr(value, "uppaal_UrgentType38", None)
                setattr(value, "uppaal_UrgentType38", self)

    @property
    def uppaal_LocationType34(self):
        return self.__uppaal_LocationType34

    @uppaal_LocationType34.setter
    def uppaal_LocationType34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uppaal_LocationType__uppaal_LocationType34", None)
        self.__uppaal_LocationType34 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uppaal_LabelType35"):
                    opp_val = getattr(item, "uppaal_LabelType35", None)
                    
                    if opp_val == self:
                        setattr(item, "uppaal_LabelType35", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uppaal_LabelType35"):
                    opp_val = getattr(item, "uppaal_LabelType35", None)
                    
                    setattr(item, "uppaal_LabelType35", self)
                    

    @property
    def uppaal_LocationType(self):
        return self.__uppaal_LocationType

    @uppaal_LocationType.setter
    def uppaal_LocationType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uppaal_LocationType__uppaal_LocationType", None)
        self.__uppaal_LocationType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uppaal_DocumentRoot11"):
                opp_val = getattr(old_value, "uppaal_DocumentRoot11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uppaal_DocumentRoot11"):
                opp_val = getattr(value, "uppaal_DocumentRoot11", None)
                if opp_val is None:
                    setattr(value, "uppaal_DocumentRoot11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uppaal_LocationType31(self):
        return self.__uppaal_LocationType31

    @uppaal_LocationType31.setter
    def uppaal_LocationType31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uppaal_LocationType__uppaal_LocationType31", None)
        self.__uppaal_LocationType31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uppaal_NameType32"):
                opp_val = getattr(old_value, "uppaal_NameType32", None)
                if opp_val == self:
                    setattr(old_value, "uppaal_NameType32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uppaal_NameType32"):
                opp_val = getattr(value, "uppaal_NameType32", None)
                setattr(value, "uppaal_NameType32", self)

    @property
    def uppaal_LocationType53(self):
        return self.__uppaal_LocationType53

    @uppaal_LocationType53.setter
    def uppaal_LocationType53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uppaal_LocationType__uppaal_LocationType53", None)
        self.__uppaal_LocationType53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uppaal_TemplateType52"):
                opp_val = getattr(old_value, "uppaal_TemplateType52", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uppaal_TemplateType52"):
                opp_val = getattr(value, "uppaal_TemplateType52", None)
                if opp_val is None:
                    setattr(value, "uppaal_TemplateType52", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uppaal_LocationType40(self):
        return self.__uppaal_LocationType40

    @uppaal_LocationType40.setter
    def uppaal_LocationType40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uppaal_LocationType__uppaal_LocationType40", None)
        self.__uppaal_LocationType40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uppaal_CommittedType41"):
                opp_val = getattr(old_value, "uppaal_CommittedType41", None)
                if opp_val == self:
                    setattr(old_value, "uppaal_CommittedType41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uppaal_CommittedType41"):
                opp_val = getattr(value, "uppaal_CommittedType41", None)
                setattr(value, "uppaal_CommittedType41", self)

class uppaal_EStringToStringMapEntry:

    pass
class uppaal_DocumentRoot:

    def __init__(self, mixed: str, declaration: str, imports: str, instantiation: str, system: str, uppaal_DocumentRoot: set["uppaal_EStringToStringMapEntry"] = None, uppaal_DocumentRoot2: set["uppaal_EStringToStringMapEntry"] = None, uppaal_DocumentRoot11: set["uppaal_LocationType"] = None, uppaal_DocumentRoot13: set["uppaal_NailType"] = None, uppaal_DocumentRoot15: set["uppaal_NameType"] = None, uppaal_DocumentRoot5: set["uppaal_CommittedType"] = None, uppaal_DocumentRoot7: set["uppaal_InitType"] = None, uppaal_DocumentRoot9: set["uppaal_LabelType"] = None, uppaal_DocumentRoot25: set["uppaal_TemplateType"] = None, uppaal_DocumentRoot27: set["uppaal_TransitionType"] = None, uppaal_DocumentRoot29: set["uppaal_UrgentType"] = None, uppaal_DocumentRoot17: set["uppaal_NtaType"] = None, uppaal_DocumentRoot19: set["uppaal_ParameterType"] = None, uppaal_DocumentRoot21: set["uppaal_SourceType"] = None, uppaal_DocumentRoot23: set["uppaal_TargetType"] = None):
        self.mixed = mixed
        self.declaration = declaration
        self.imports = imports
        self.instantiation = instantiation
        self.system = system
        self.uppaal_DocumentRoot = uppaal_DocumentRoot if uppaal_DocumentRoot is not None else set()
        self.uppaal_DocumentRoot2 = uppaal_DocumentRoot2 if uppaal_DocumentRoot2 is not None else set()
        self.uppaal_DocumentRoot11 = uppaal_DocumentRoot11 if uppaal_DocumentRoot11 is not None else set()
        self.uppaal_DocumentRoot13 = uppaal_DocumentRoot13 if uppaal_DocumentRoot13 is not None else set()
        self.uppaal_DocumentRoot15 = uppaal_DocumentRoot15 if uppaal_DocumentRoot15 is not None else set()
        self.uppaal_DocumentRoot5 = uppaal_DocumentRoot5 if uppaal_DocumentRoot5 is not None else set()
        self.uppaal_DocumentRoot7 = uppaal_DocumentRoot7 if uppaal_DocumentRoot7 is not None else set()
        self.uppaal_DocumentRoot9 = uppaal_DocumentRoot9 if uppaal_DocumentRoot9 is not None else set()
        self.uppaal_DocumentRoot25 = uppaal_DocumentRoot25 if uppaal_DocumentRoot25 is not None else set()
        self.uppaal_DocumentRoot27 = uppaal_DocumentRoot27 if uppaal_DocumentRoot27 is not None else set()
        self.uppaal_DocumentRoot29 = uppaal_DocumentRoot29 if uppaal_DocumentRoot29 is not None else set()
        self.uppaal_DocumentRoot17 = uppaal_DocumentRoot17 if uppaal_DocumentRoot17 is not None else set()
        self.uppaal_DocumentRoot19 = uppaal_DocumentRoot19 if uppaal_DocumentRoot19 is not None else set()
        self.uppaal_DocumentRoot21 = uppaal_DocumentRoot21 if uppaal_DocumentRoot21 is not None else set()
        self.uppaal_DocumentRoot23 = uppaal_DocumentRoot23 if uppaal_DocumentRoot23 is not None else set()
        
    @property
    def instantiation(self) -> str:
        return self.__instantiation

    @instantiation.setter
    def instantiation(self, instantiation: str):
        self.__instantiation = instantiation

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
    def declaration(self) -> str:
        return self.__declaration

    @declaration.setter
    def declaration(self, declaration: str):
        self.__declaration = declaration

    @property
    def system(self) -> str:
        return self.__system

    @system.setter
    def system(self, system: str):
        self.__system = system

    @property
    def uppaal_DocumentRoot9(self):
        return self.__uppaal_DocumentRoot9

    @uppaal_DocumentRoot9.setter
    def uppaal_DocumentRoot9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uppaal_DocumentRoot__uppaal_DocumentRoot9", None)
        self.__uppaal_DocumentRoot9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uppaal_LabelType"):
                    opp_val = getattr(item, "uppaal_LabelType", None)
                    
                    if opp_val == self:
                        setattr(item, "uppaal_LabelType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uppaal_LabelType"):
                    opp_val = getattr(item, "uppaal_LabelType", None)
                    
                    setattr(item, "uppaal_LabelType", self)
                    

    @property
    def uppaal_DocumentRoot(self):
        return self.__uppaal_DocumentRoot

    @uppaal_DocumentRoot.setter
    def uppaal_DocumentRoot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uppaal_DocumentRoot__uppaal_DocumentRoot", None)
        self.__uppaal_DocumentRoot = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uppaal_EStringToStringMapEntry"):
                    opp_val = getattr(item, "uppaal_EStringToStringMapEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "uppaal_EStringToStringMapEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uppaal_EStringToStringMapEntry"):
                    opp_val = getattr(item, "uppaal_EStringToStringMapEntry", None)
                    
                    setattr(item, "uppaal_EStringToStringMapEntry", self)
                    

    @property
    def uppaal_DocumentRoot29(self):
        return self.__uppaal_DocumentRoot29

    @uppaal_DocumentRoot29.setter
    def uppaal_DocumentRoot29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uppaal_DocumentRoot__uppaal_DocumentRoot29", None)
        self.__uppaal_DocumentRoot29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uppaal_UrgentType"):
                    opp_val = getattr(item, "uppaal_UrgentType", None)
                    
                    if opp_val == self:
                        setattr(item, "uppaal_UrgentType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uppaal_UrgentType"):
                    opp_val = getattr(item, "uppaal_UrgentType", None)
                    
                    setattr(item, "uppaal_UrgentType", self)
                    

    @property
    def uppaal_DocumentRoot13(self):
        return self.__uppaal_DocumentRoot13

    @uppaal_DocumentRoot13.setter
    def uppaal_DocumentRoot13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uppaal_DocumentRoot__uppaal_DocumentRoot13", None)
        self.__uppaal_DocumentRoot13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uppaal_NailType"):
                    opp_val = getattr(item, "uppaal_NailType", None)
                    
                    if opp_val == self:
                        setattr(item, "uppaal_NailType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uppaal_NailType"):
                    opp_val = getattr(item, "uppaal_NailType", None)
                    
                    setattr(item, "uppaal_NailType", self)
                    

    @property
    def uppaal_DocumentRoot23(self):
        return self.__uppaal_DocumentRoot23

    @uppaal_DocumentRoot23.setter
    def uppaal_DocumentRoot23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uppaal_DocumentRoot__uppaal_DocumentRoot23", None)
        self.__uppaal_DocumentRoot23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uppaal_TargetType"):
                    opp_val = getattr(item, "uppaal_TargetType", None)
                    
                    if opp_val == self:
                        setattr(item, "uppaal_TargetType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uppaal_TargetType"):
                    opp_val = getattr(item, "uppaal_TargetType", None)
                    
                    setattr(item, "uppaal_TargetType", self)
                    

    @property
    def uppaal_DocumentRoot2(self):
        return self.__uppaal_DocumentRoot2

    @uppaal_DocumentRoot2.setter
    def uppaal_DocumentRoot2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uppaal_DocumentRoot__uppaal_DocumentRoot2", None)
        self.__uppaal_DocumentRoot2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uppaal_EStringToStringMapEntry3"):
                    opp_val = getattr(item, "uppaal_EStringToStringMapEntry3", None)
                    
                    if opp_val == self:
                        setattr(item, "uppaal_EStringToStringMapEntry3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uppaal_EStringToStringMapEntry3"):
                    opp_val = getattr(item, "uppaal_EStringToStringMapEntry3", None)
                    
                    setattr(item, "uppaal_EStringToStringMapEntry3", self)
                    

    @property
    def uppaal_DocumentRoot27(self):
        return self.__uppaal_DocumentRoot27

    @uppaal_DocumentRoot27.setter
    def uppaal_DocumentRoot27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uppaal_DocumentRoot__uppaal_DocumentRoot27", None)
        self.__uppaal_DocumentRoot27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uppaal_TransitionType"):
                    opp_val = getattr(item, "uppaal_TransitionType", None)
                    
                    if opp_val == self:
                        setattr(item, "uppaal_TransitionType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uppaal_TransitionType"):
                    opp_val = getattr(item, "uppaal_TransitionType", None)
                    
                    setattr(item, "uppaal_TransitionType", self)
                    

    @property
    def uppaal_DocumentRoot5(self):
        return self.__uppaal_DocumentRoot5

    @uppaal_DocumentRoot5.setter
    def uppaal_DocumentRoot5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uppaal_DocumentRoot__uppaal_DocumentRoot5", None)
        self.__uppaal_DocumentRoot5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uppaal_CommittedType"):
                    opp_val = getattr(item, "uppaal_CommittedType", None)
                    
                    if opp_val == self:
                        setattr(item, "uppaal_CommittedType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uppaal_CommittedType"):
                    opp_val = getattr(item, "uppaal_CommittedType", None)
                    
                    setattr(item, "uppaal_CommittedType", self)
                    

    @property
    def uppaal_DocumentRoot21(self):
        return self.__uppaal_DocumentRoot21

    @uppaal_DocumentRoot21.setter
    def uppaal_DocumentRoot21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uppaal_DocumentRoot__uppaal_DocumentRoot21", None)
        self.__uppaal_DocumentRoot21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uppaal_SourceType"):
                    opp_val = getattr(item, "uppaal_SourceType", None)
                    
                    if opp_val == self:
                        setattr(item, "uppaal_SourceType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uppaal_SourceType"):
                    opp_val = getattr(item, "uppaal_SourceType", None)
                    
                    setattr(item, "uppaal_SourceType", self)
                    

    @property
    def uppaal_DocumentRoot15(self):
        return self.__uppaal_DocumentRoot15

    @uppaal_DocumentRoot15.setter
    def uppaal_DocumentRoot15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uppaal_DocumentRoot__uppaal_DocumentRoot15", None)
        self.__uppaal_DocumentRoot15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uppaal_NameType"):
                    opp_val = getattr(item, "uppaal_NameType", None)
                    
                    if opp_val == self:
                        setattr(item, "uppaal_NameType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uppaal_NameType"):
                    opp_val = getattr(item, "uppaal_NameType", None)
                    
                    setattr(item, "uppaal_NameType", self)
                    

    @property
    def uppaal_DocumentRoot17(self):
        return self.__uppaal_DocumentRoot17

    @uppaal_DocumentRoot17.setter
    def uppaal_DocumentRoot17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uppaal_DocumentRoot__uppaal_DocumentRoot17", None)
        self.__uppaal_DocumentRoot17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uppaal_NtaType"):
                    opp_val = getattr(item, "uppaal_NtaType", None)
                    
                    if opp_val == self:
                        setattr(item, "uppaal_NtaType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uppaal_NtaType"):
                    opp_val = getattr(item, "uppaal_NtaType", None)
                    
                    setattr(item, "uppaal_NtaType", self)
                    

    @property
    def uppaal_DocumentRoot19(self):
        return self.__uppaal_DocumentRoot19

    @uppaal_DocumentRoot19.setter
    def uppaal_DocumentRoot19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uppaal_DocumentRoot__uppaal_DocumentRoot19", None)
        self.__uppaal_DocumentRoot19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uppaal_ParameterType"):
                    opp_val = getattr(item, "uppaal_ParameterType", None)
                    
                    if opp_val == self:
                        setattr(item, "uppaal_ParameterType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uppaal_ParameterType"):
                    opp_val = getattr(item, "uppaal_ParameterType", None)
                    
                    setattr(item, "uppaal_ParameterType", self)
                    

    @property
    def uppaal_DocumentRoot11(self):
        return self.__uppaal_DocumentRoot11

    @uppaal_DocumentRoot11.setter
    def uppaal_DocumentRoot11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uppaal_DocumentRoot__uppaal_DocumentRoot11", None)
        self.__uppaal_DocumentRoot11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uppaal_LocationType"):
                    opp_val = getattr(item, "uppaal_LocationType", None)
                    
                    if opp_val == self:
                        setattr(item, "uppaal_LocationType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uppaal_LocationType"):
                    opp_val = getattr(item, "uppaal_LocationType", None)
                    
                    setattr(item, "uppaal_LocationType", self)
                    

    @property
    def uppaal_DocumentRoot7(self):
        return self.__uppaal_DocumentRoot7

    @uppaal_DocumentRoot7.setter
    def uppaal_DocumentRoot7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uppaal_DocumentRoot__uppaal_DocumentRoot7", None)
        self.__uppaal_DocumentRoot7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uppaal_InitType"):
                    opp_val = getattr(item, "uppaal_InitType", None)
                    
                    if opp_val == self:
                        setattr(item, "uppaal_InitType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uppaal_InitType"):
                    opp_val = getattr(item, "uppaal_InitType", None)
                    
                    setattr(item, "uppaal_InitType", self)
                    

    @property
    def uppaal_DocumentRoot25(self):
        return self.__uppaal_DocumentRoot25

    @uppaal_DocumentRoot25.setter
    def uppaal_DocumentRoot25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uppaal_DocumentRoot__uppaal_DocumentRoot25", None)
        self.__uppaal_DocumentRoot25 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uppaal_TemplateType"):
                    opp_val = getattr(item, "uppaal_TemplateType", None)
                    
                    if opp_val == self:
                        setattr(item, "uppaal_TemplateType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uppaal_TemplateType"):
                    opp_val = getattr(item, "uppaal_TemplateType", None)
                    
                    setattr(item, "uppaal_TemplateType", self)
                    

class uppaal_CommittedType:

    pass