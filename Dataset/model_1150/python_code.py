from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class KindType(Enum):
    synchronisation = "synchronisation"
    invariant = "invariant"
    assignment = "assignment"
    guard = "guard"
    select = "select"
    comments = "comments"


############################################
# Definition of Classes
############################################

class flat11_UrgentType:

    pass
class flat11_TransitionType:

    def __init__(self, y: str, action: str, color: str, controllable: str, id: str, x: str, flat11_TransitionType: "flat11_DocumentRoot" = None, flat11_TransitionType64: "flat11_TargetType" = None, flat11_TransitionType67: set["flat11_LabelType"] = None, flat11_TransitionType59: "flat11_TemplateType" = None, flat11_TransitionType61: "flat11_SourceType" = None, flat11_TransitionType70: set["flat11_NailType"] = None):
        self.y = y
        self.action = action
        self.color = color
        self.controllable = controllable
        self.id = id
        self.x = x
        self.flat11_TransitionType = flat11_TransitionType
        self.flat11_TransitionType64 = flat11_TransitionType64
        self.flat11_TransitionType67 = flat11_TransitionType67 if flat11_TransitionType67 is not None else set()
        self.flat11_TransitionType59 = flat11_TransitionType59
        self.flat11_TransitionType61 = flat11_TransitionType61
        self.flat11_TransitionType70 = flat11_TransitionType70 if flat11_TransitionType70 is not None else set()
        
    @property
    def x(self) -> str:
        return self.__x

    @x.setter
    def x(self, x: str):
        self.__x = x

    @property
    def controllable(self) -> str:
        return self.__controllable

    @controllable.setter
    def controllable(self, controllable: str):
        self.__controllable = controllable

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
    def action(self) -> str:
        return self.__action

    @action.setter
    def action(self, action: str):
        self.__action = action

    @property
    def y(self) -> str:
        return self.__y

    @y.setter
    def y(self, y: str):
        self.__y = y

    @property
    def flat11_TransitionType64(self):
        return self.__flat11_TransitionType64

    @flat11_TransitionType64.setter
    def flat11_TransitionType64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_flat11_TransitionType__flat11_TransitionType64", None)
        self.__flat11_TransitionType64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "flat11_TargetType65"):
                opp_val = getattr(old_value, "flat11_TargetType65", None)
                if opp_val == self:
                    setattr(old_value, "flat11_TargetType65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "flat11_TargetType65"):
                opp_val = getattr(value, "flat11_TargetType65", None)
                setattr(value, "flat11_TargetType65", self)

    @property
    def flat11_TransitionType67(self):
        return self.__flat11_TransitionType67

    @flat11_TransitionType67.setter
    def flat11_TransitionType67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_flat11_TransitionType__flat11_TransitionType67", None)
        self.__flat11_TransitionType67 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "flat11_LabelType68"):
                    opp_val = getattr(item, "flat11_LabelType68", None)
                    
                    if opp_val == self:
                        setattr(item, "flat11_LabelType68", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "flat11_LabelType68"):
                    opp_val = getattr(item, "flat11_LabelType68", None)
                    
                    setattr(item, "flat11_LabelType68", self)
                    

    @property
    def flat11_TransitionType(self):
        return self.__flat11_TransitionType

    @flat11_TransitionType.setter
    def flat11_TransitionType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_flat11_TransitionType__flat11_TransitionType", None)
        self.__flat11_TransitionType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "flat11_DocumentRoot27"):
                opp_val = getattr(old_value, "flat11_DocumentRoot27", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "flat11_DocumentRoot27"):
                opp_val = getattr(value, "flat11_DocumentRoot27", None)
                if opp_val is None:
                    setattr(value, "flat11_DocumentRoot27", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def flat11_TransitionType59(self):
        return self.__flat11_TransitionType59

    @flat11_TransitionType59.setter
    def flat11_TransitionType59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_flat11_TransitionType__flat11_TransitionType59", None)
        self.__flat11_TransitionType59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "flat11_TemplateType58"):
                opp_val = getattr(old_value, "flat11_TemplateType58", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "flat11_TemplateType58"):
                opp_val = getattr(value, "flat11_TemplateType58", None)
                if opp_val is None:
                    setattr(value, "flat11_TemplateType58", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def flat11_TransitionType61(self):
        return self.__flat11_TransitionType61

    @flat11_TransitionType61.setter
    def flat11_TransitionType61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_flat11_TransitionType__flat11_TransitionType61", None)
        self.__flat11_TransitionType61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "flat11_SourceType62"):
                opp_val = getattr(old_value, "flat11_SourceType62", None)
                if opp_val == self:
                    setattr(old_value, "flat11_SourceType62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "flat11_SourceType62"):
                opp_val = getattr(value, "flat11_SourceType62", None)
                setattr(value, "flat11_SourceType62", self)

    @property
    def flat11_TransitionType70(self):
        return self.__flat11_TransitionType70

    @flat11_TransitionType70.setter
    def flat11_TransitionType70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_flat11_TransitionType__flat11_TransitionType70", None)
        self.__flat11_TransitionType70 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "flat11_NailType71"):
                    opp_val = getattr(item, "flat11_NailType71", None)
                    
                    if opp_val == self:
                        setattr(item, "flat11_NailType71", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "flat11_NailType71"):
                    opp_val = getattr(item, "flat11_NailType71", None)
                    
                    setattr(item, "flat11_NailType71", self)
                    

class flat11_TemplateType:

    def __init__(self, declaration: str, flat11_TemplateType: "flat11_DocumentRoot" = None, flat11_TemplateType44: "flat11_NtaType" = None, flat11_TemplateType46: "flat11_NameType" = None, flat11_TemplateType49: "flat11_ParameterType" = None, flat11_TemplateType52: set["flat11_LocationType"] = None, flat11_TemplateType55: "flat11_InitType" = None, flat11_TemplateType58: set["flat11_TransitionType"] = None):
        self.declaration = declaration
        self.flat11_TemplateType = flat11_TemplateType
        self.flat11_TemplateType44 = flat11_TemplateType44
        self.flat11_TemplateType46 = flat11_TemplateType46
        self.flat11_TemplateType49 = flat11_TemplateType49
        self.flat11_TemplateType52 = flat11_TemplateType52 if flat11_TemplateType52 is not None else set()
        self.flat11_TemplateType55 = flat11_TemplateType55
        self.flat11_TemplateType58 = flat11_TemplateType58 if flat11_TemplateType58 is not None else set()
        
    @property
    def declaration(self) -> str:
        return self.__declaration

    @declaration.setter
    def declaration(self, declaration: str):
        self.__declaration = declaration

    @property
    def flat11_TemplateType55(self):
        return self.__flat11_TemplateType55

    @flat11_TemplateType55.setter
    def flat11_TemplateType55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_flat11_TemplateType__flat11_TemplateType55", None)
        self.__flat11_TemplateType55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "flat11_InitType56"):
                opp_val = getattr(old_value, "flat11_InitType56", None)
                if opp_val == self:
                    setattr(old_value, "flat11_InitType56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "flat11_InitType56"):
                opp_val = getattr(value, "flat11_InitType56", None)
                setattr(value, "flat11_InitType56", self)

    @property
    def flat11_TemplateType(self):
        return self.__flat11_TemplateType

    @flat11_TemplateType.setter
    def flat11_TemplateType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_flat11_TemplateType__flat11_TemplateType", None)
        self.__flat11_TemplateType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "flat11_DocumentRoot25"):
                opp_val = getattr(old_value, "flat11_DocumentRoot25", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "flat11_DocumentRoot25"):
                opp_val = getattr(value, "flat11_DocumentRoot25", None)
                if opp_val is None:
                    setattr(value, "flat11_DocumentRoot25", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def flat11_TemplateType52(self):
        return self.__flat11_TemplateType52

    @flat11_TemplateType52.setter
    def flat11_TemplateType52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_flat11_TemplateType__flat11_TemplateType52", None)
        self.__flat11_TemplateType52 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "flat11_LocationType53"):
                    opp_val = getattr(item, "flat11_LocationType53", None)
                    
                    if opp_val == self:
                        setattr(item, "flat11_LocationType53", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "flat11_LocationType53"):
                    opp_val = getattr(item, "flat11_LocationType53", None)
                    
                    setattr(item, "flat11_LocationType53", self)
                    

    @property
    def flat11_TemplateType46(self):
        return self.__flat11_TemplateType46

    @flat11_TemplateType46.setter
    def flat11_TemplateType46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_flat11_TemplateType__flat11_TemplateType46", None)
        self.__flat11_TemplateType46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "flat11_NameType47"):
                opp_val = getattr(old_value, "flat11_NameType47", None)
                if opp_val == self:
                    setattr(old_value, "flat11_NameType47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "flat11_NameType47"):
                opp_val = getattr(value, "flat11_NameType47", None)
                setattr(value, "flat11_NameType47", self)

    @property
    def flat11_TemplateType49(self):
        return self.__flat11_TemplateType49

    @flat11_TemplateType49.setter
    def flat11_TemplateType49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_flat11_TemplateType__flat11_TemplateType49", None)
        self.__flat11_TemplateType49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "flat11_ParameterType50"):
                opp_val = getattr(old_value, "flat11_ParameterType50", None)
                if opp_val == self:
                    setattr(old_value, "flat11_ParameterType50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "flat11_ParameterType50"):
                opp_val = getattr(value, "flat11_ParameterType50", None)
                setattr(value, "flat11_ParameterType50", self)

    @property
    def flat11_TemplateType44(self):
        return self.__flat11_TemplateType44

    @flat11_TemplateType44.setter
    def flat11_TemplateType44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_flat11_TemplateType__flat11_TemplateType44", None)
        self.__flat11_TemplateType44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "flat11_NtaType43"):
                opp_val = getattr(old_value, "flat11_NtaType43", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "flat11_NtaType43"):
                opp_val = getattr(value, "flat11_NtaType43", None)
                if opp_val is None:
                    setattr(value, "flat11_NtaType43", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def flat11_TemplateType58(self):
        return self.__flat11_TemplateType58

    @flat11_TemplateType58.setter
    def flat11_TemplateType58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_flat11_TemplateType__flat11_TemplateType58", None)
        self.__flat11_TemplateType58 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "flat11_TransitionType59"):
                    opp_val = getattr(item, "flat11_TransitionType59", None)
                    
                    if opp_val == self:
                        setattr(item, "flat11_TransitionType59", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "flat11_TransitionType59"):
                    opp_val = getattr(item, "flat11_TransitionType59", None)
                    
                    setattr(item, "flat11_TransitionType59", self)
                    

class flat11_TargetType:

    def __init__(self, ref: str, flat11_TargetType: "flat11_DocumentRoot" = None, flat11_TargetType65: "flat11_TransitionType" = None):
        self.ref = ref
        self.flat11_TargetType = flat11_TargetType
        self.flat11_TargetType65 = flat11_TargetType65
        
    @property
    def ref(self) -> str:
        return self.__ref

    @ref.setter
    def ref(self, ref: str):
        self.__ref = ref

    @property
    def flat11_TargetType65(self):
        return self.__flat11_TargetType65

    @flat11_TargetType65.setter
    def flat11_TargetType65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_flat11_TargetType__flat11_TargetType65", None)
        self.__flat11_TargetType65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "flat11_TransitionType64"):
                opp_val = getattr(old_value, "flat11_TransitionType64", None)
                if opp_val == self:
                    setattr(old_value, "flat11_TransitionType64", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "flat11_TransitionType64"):
                opp_val = getattr(value, "flat11_TransitionType64", None)
                setattr(value, "flat11_TransitionType64", self)

    @property
    def flat11_TargetType(self):
        return self.__flat11_TargetType

    @flat11_TargetType.setter
    def flat11_TargetType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_flat11_TargetType__flat11_TargetType", None)
        self.__flat11_TargetType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "flat11_DocumentRoot23"):
                opp_val = getattr(old_value, "flat11_DocumentRoot23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "flat11_DocumentRoot23"):
                opp_val = getattr(value, "flat11_DocumentRoot23", None)
                if opp_val is None:
                    setattr(value, "flat11_DocumentRoot23", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class flat11_ParameterType:

    def __init__(self, value: str, x: str, y: str, flat11_ParameterType: "flat11_DocumentRoot" = None, flat11_ParameterType50: "flat11_TemplateType" = None):
        self.value = value
        self.x = x
        self.y = y
        self.flat11_ParameterType = flat11_ParameterType
        self.flat11_ParameterType50 = flat11_ParameterType50
        
    @property
    def y(self) -> str:
        return self.__y

    @y.setter
    def y(self, y: str):
        self.__y = y

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def x(self) -> str:
        return self.__x

    @x.setter
    def x(self, x: str):
        self.__x = x

    @property
    def flat11_ParameterType50(self):
        return self.__flat11_ParameterType50

    @flat11_ParameterType50.setter
    def flat11_ParameterType50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_flat11_ParameterType__flat11_ParameterType50", None)
        self.__flat11_ParameterType50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "flat11_TemplateType49"):
                opp_val = getattr(old_value, "flat11_TemplateType49", None)
                if opp_val == self:
                    setattr(old_value, "flat11_TemplateType49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "flat11_TemplateType49"):
                opp_val = getattr(value, "flat11_TemplateType49", None)
                setattr(value, "flat11_TemplateType49", self)

    @property
    def flat11_ParameterType(self):
        return self.__flat11_ParameterType

    @flat11_ParameterType.setter
    def flat11_ParameterType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_flat11_ParameterType__flat11_ParameterType", None)
        self.__flat11_ParameterType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "flat11_DocumentRoot19"):
                opp_val = getattr(old_value, "flat11_DocumentRoot19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "flat11_DocumentRoot19"):
                opp_val = getattr(value, "flat11_DocumentRoot19", None)
                if opp_val is None:
                    setattr(value, "flat11_DocumentRoot19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class flat11_LabelType:

    def __init__(self, value: str, kind: str, x: str, y: str, flat11_LabelType: "flat11_DocumentRoot" = None, flat11_LabelType35: "flat11_LocationType" = None, flat11_LabelType68: "flat11_TransitionType" = None):
        self.value = value
        self.kind = kind
        self.x = x
        self.y = y
        self.flat11_LabelType = flat11_LabelType
        self.flat11_LabelType35 = flat11_LabelType35
        self.flat11_LabelType68 = flat11_LabelType68
        
    @property
    def y(self) -> str:
        return self.__y

    @y.setter
    def y(self, y: str):
        self.__y = y

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

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
    def flat11_LabelType(self):
        return self.__flat11_LabelType

    @flat11_LabelType.setter
    def flat11_LabelType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_flat11_LabelType__flat11_LabelType", None)
        self.__flat11_LabelType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "flat11_DocumentRoot9"):
                opp_val = getattr(old_value, "flat11_DocumentRoot9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "flat11_DocumentRoot9"):
                opp_val = getattr(value, "flat11_DocumentRoot9", None)
                if opp_val is None:
                    setattr(value, "flat11_DocumentRoot9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def flat11_LabelType35(self):
        return self.__flat11_LabelType35

    @flat11_LabelType35.setter
    def flat11_LabelType35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_flat11_LabelType__flat11_LabelType35", None)
        self.__flat11_LabelType35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "flat11_LocationType34"):
                opp_val = getattr(old_value, "flat11_LocationType34", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "flat11_LocationType34"):
                opp_val = getattr(value, "flat11_LocationType34", None)
                if opp_val is None:
                    setattr(value, "flat11_LocationType34", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def flat11_LabelType68(self):
        return self.__flat11_LabelType68

    @flat11_LabelType68.setter
    def flat11_LabelType68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_flat11_LabelType__flat11_LabelType68", None)
        self.__flat11_LabelType68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "flat11_TransitionType67"):
                opp_val = getattr(old_value, "flat11_TransitionType67", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "flat11_TransitionType67"):
                opp_val = getattr(value, "flat11_TransitionType67", None)
                if opp_val is None:
                    setattr(value, "flat11_TransitionType67", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class flat11_NtaType:

    def __init__(self, instantiation: str, system: str, imports: str, declaration: str, flat11_NtaType: "flat11_DocumentRoot" = None, flat11_NtaType43: set["flat11_TemplateType"] = None):
        self.instantiation = instantiation
        self.system = system
        self.imports = imports
        self.declaration = declaration
        self.flat11_NtaType = flat11_NtaType
        self.flat11_NtaType43 = flat11_NtaType43 if flat11_NtaType43 is not None else set()
        
    @property
    def system(self) -> str:
        return self.__system

    @system.setter
    def system(self, system: str):
        self.__system = system

    @property
    def declaration(self) -> str:
        return self.__declaration

    @declaration.setter
    def declaration(self, declaration: str):
        self.__declaration = declaration

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
    def flat11_NtaType(self):
        return self.__flat11_NtaType

    @flat11_NtaType.setter
    def flat11_NtaType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_flat11_NtaType__flat11_NtaType", None)
        self.__flat11_NtaType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "flat11_DocumentRoot17"):
                opp_val = getattr(old_value, "flat11_DocumentRoot17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "flat11_DocumentRoot17"):
                opp_val = getattr(value, "flat11_DocumentRoot17", None)
                if opp_val is None:
                    setattr(value, "flat11_DocumentRoot17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def flat11_NtaType43(self):
        return self.__flat11_NtaType43

    @flat11_NtaType43.setter
    def flat11_NtaType43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_flat11_NtaType__flat11_NtaType43", None)
        self.__flat11_NtaType43 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "flat11_TemplateType44"):
                    opp_val = getattr(item, "flat11_TemplateType44", None)
                    
                    if opp_val == self:
                        setattr(item, "flat11_TemplateType44", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "flat11_TemplateType44"):
                    opp_val = getattr(item, "flat11_TemplateType44", None)
                    
                    setattr(item, "flat11_TemplateType44", self)
                    

class flat11_NameType:

    def __init__(self, value: str, x: str, y: str, flat11_NameType: "flat11_DocumentRoot" = None, flat11_NameType32: "flat11_LocationType" = None, flat11_NameType47: "flat11_TemplateType" = None):
        self.value = value
        self.x = x
        self.y = y
        self.flat11_NameType = flat11_NameType
        self.flat11_NameType32 = flat11_NameType32
        self.flat11_NameType47 = flat11_NameType47
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

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
    def flat11_NameType32(self):
        return self.__flat11_NameType32

    @flat11_NameType32.setter
    def flat11_NameType32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_flat11_NameType__flat11_NameType32", None)
        self.__flat11_NameType32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "flat11_LocationType31"):
                opp_val = getattr(old_value, "flat11_LocationType31", None)
                if opp_val == self:
                    setattr(old_value, "flat11_LocationType31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "flat11_LocationType31"):
                opp_val = getattr(value, "flat11_LocationType31", None)
                setattr(value, "flat11_LocationType31", self)

    @property
    def flat11_NameType(self):
        return self.__flat11_NameType

    @flat11_NameType.setter
    def flat11_NameType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_flat11_NameType__flat11_NameType", None)
        self.__flat11_NameType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "flat11_DocumentRoot15"):
                opp_val = getattr(old_value, "flat11_DocumentRoot15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "flat11_DocumentRoot15"):
                opp_val = getattr(value, "flat11_DocumentRoot15", None)
                if opp_val is None:
                    setattr(value, "flat11_DocumentRoot15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def flat11_NameType47(self):
        return self.__flat11_NameType47

    @flat11_NameType47.setter
    def flat11_NameType47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_flat11_NameType__flat11_NameType47", None)
        self.__flat11_NameType47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "flat11_TemplateType46"):
                opp_val = getattr(old_value, "flat11_TemplateType46", None)
                if opp_val == self:
                    setattr(old_value, "flat11_TemplateType46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "flat11_TemplateType46"):
                opp_val = getattr(value, "flat11_TemplateType46", None)
                setattr(value, "flat11_TemplateType46", self)

class flat11_NailType:

    def __init__(self, x: str, y: str, flat11_NailType: "flat11_DocumentRoot" = None, flat11_NailType71: "flat11_TransitionType" = None):
        self.x = x
        self.y = y
        self.flat11_NailType = flat11_NailType
        self.flat11_NailType71 = flat11_NailType71
        
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
    def flat11_NailType71(self):
        return self.__flat11_NailType71

    @flat11_NailType71.setter
    def flat11_NailType71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_flat11_NailType__flat11_NailType71", None)
        self.__flat11_NailType71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "flat11_TransitionType70"):
                opp_val = getattr(old_value, "flat11_TransitionType70", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "flat11_TransitionType70"):
                opp_val = getattr(value, "flat11_TransitionType70", None)
                if opp_val is None:
                    setattr(value, "flat11_TransitionType70", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def flat11_NailType(self):
        return self.__flat11_NailType

    @flat11_NailType.setter
    def flat11_NailType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_flat11_NailType__flat11_NailType", None)
        self.__flat11_NailType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "flat11_DocumentRoot13"):
                opp_val = getattr(old_value, "flat11_DocumentRoot13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "flat11_DocumentRoot13"):
                opp_val = getattr(value, "flat11_DocumentRoot13", None)
                if opp_val is None:
                    setattr(value, "flat11_DocumentRoot13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class flat11_SourceType:

    def __init__(self, ref: str, flat11_SourceType: "flat11_DocumentRoot" = None, flat11_SourceType62: "flat11_TransitionType" = None):
        self.ref = ref
        self.flat11_SourceType = flat11_SourceType
        self.flat11_SourceType62 = flat11_SourceType62
        
    @property
    def ref(self) -> str:
        return self.__ref

    @ref.setter
    def ref(self, ref: str):
        self.__ref = ref

    @property
    def flat11_SourceType(self):
        return self.__flat11_SourceType

    @flat11_SourceType.setter
    def flat11_SourceType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_flat11_SourceType__flat11_SourceType", None)
        self.__flat11_SourceType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "flat11_DocumentRoot21"):
                opp_val = getattr(old_value, "flat11_DocumentRoot21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "flat11_DocumentRoot21"):
                opp_val = getattr(value, "flat11_DocumentRoot21", None)
                if opp_val is None:
                    setattr(value, "flat11_DocumentRoot21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def flat11_SourceType62(self):
        return self.__flat11_SourceType62

    @flat11_SourceType62.setter
    def flat11_SourceType62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_flat11_SourceType__flat11_SourceType62", None)
        self.__flat11_SourceType62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "flat11_TransitionType61"):
                opp_val = getattr(old_value, "flat11_TransitionType61", None)
                if opp_val == self:
                    setattr(old_value, "flat11_TransitionType61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "flat11_TransitionType61"):
                opp_val = getattr(value, "flat11_TransitionType61", None)
                setattr(value, "flat11_TransitionType61", self)

class flat11_LocationType:

    def __init__(self, color: str, id: str, x: str, y: str, flat11_LocationType: "flat11_DocumentRoot" = None, flat11_LocationType31: "flat11_NameType" = None, flat11_LocationType34: set["flat11_LabelType"] = None, flat11_LocationType37: "flat11_UrgentType" = None, flat11_LocationType40: "flat11_CommittedType" = None, flat11_LocationType53: "flat11_TemplateType" = None):
        self.color = color
        self.id = id
        self.x = x
        self.y = y
        self.flat11_LocationType = flat11_LocationType
        self.flat11_LocationType31 = flat11_LocationType31
        self.flat11_LocationType34 = flat11_LocationType34 if flat11_LocationType34 is not None else set()
        self.flat11_LocationType37 = flat11_LocationType37
        self.flat11_LocationType40 = flat11_LocationType40
        self.flat11_LocationType53 = flat11_LocationType53
        
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
    def flat11_LocationType34(self):
        return self.__flat11_LocationType34

    @flat11_LocationType34.setter
    def flat11_LocationType34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_flat11_LocationType__flat11_LocationType34", None)
        self.__flat11_LocationType34 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "flat11_LabelType35"):
                    opp_val = getattr(item, "flat11_LabelType35", None)
                    
                    if opp_val == self:
                        setattr(item, "flat11_LabelType35", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "flat11_LabelType35"):
                    opp_val = getattr(item, "flat11_LabelType35", None)
                    
                    setattr(item, "flat11_LabelType35", self)
                    

    @property
    def flat11_LocationType37(self):
        return self.__flat11_LocationType37

    @flat11_LocationType37.setter
    def flat11_LocationType37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_flat11_LocationType__flat11_LocationType37", None)
        self.__flat11_LocationType37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "flat11_UrgentType38"):
                opp_val = getattr(old_value, "flat11_UrgentType38", None)
                if opp_val == self:
                    setattr(old_value, "flat11_UrgentType38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "flat11_UrgentType38"):
                opp_val = getattr(value, "flat11_UrgentType38", None)
                setattr(value, "flat11_UrgentType38", self)

    @property
    def flat11_LocationType31(self):
        return self.__flat11_LocationType31

    @flat11_LocationType31.setter
    def flat11_LocationType31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_flat11_LocationType__flat11_LocationType31", None)
        self.__flat11_LocationType31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "flat11_NameType32"):
                opp_val = getattr(old_value, "flat11_NameType32", None)
                if opp_val == self:
                    setattr(old_value, "flat11_NameType32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "flat11_NameType32"):
                opp_val = getattr(value, "flat11_NameType32", None)
                setattr(value, "flat11_NameType32", self)

    @property
    def flat11_LocationType40(self):
        return self.__flat11_LocationType40

    @flat11_LocationType40.setter
    def flat11_LocationType40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_flat11_LocationType__flat11_LocationType40", None)
        self.__flat11_LocationType40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "flat11_CommittedType41"):
                opp_val = getattr(old_value, "flat11_CommittedType41", None)
                if opp_val == self:
                    setattr(old_value, "flat11_CommittedType41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "flat11_CommittedType41"):
                opp_val = getattr(value, "flat11_CommittedType41", None)
                setattr(value, "flat11_CommittedType41", self)

    @property
    def flat11_LocationType(self):
        return self.__flat11_LocationType

    @flat11_LocationType.setter
    def flat11_LocationType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_flat11_LocationType__flat11_LocationType", None)
        self.__flat11_LocationType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "flat11_DocumentRoot11"):
                opp_val = getattr(old_value, "flat11_DocumentRoot11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "flat11_DocumentRoot11"):
                opp_val = getattr(value, "flat11_DocumentRoot11", None)
                if opp_val is None:
                    setattr(value, "flat11_DocumentRoot11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def flat11_LocationType53(self):
        return self.__flat11_LocationType53

    @flat11_LocationType53.setter
    def flat11_LocationType53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_flat11_LocationType__flat11_LocationType53", None)
        self.__flat11_LocationType53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "flat11_TemplateType52"):
                opp_val = getattr(old_value, "flat11_TemplateType52", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "flat11_TemplateType52"):
                opp_val = getattr(value, "flat11_TemplateType52", None)
                if opp_val is None:
                    setattr(value, "flat11_TemplateType52", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class flat11_EStringToStringMapEntry:

    pass
class flat11_DocumentRoot:

    def __init__(self, declaration: str, imports: str, instantiation: str, mixed: str, system: str, flat11_DocumentRoot2: set["flat11_EStringToStringMapEntry"] = None, flat11_DocumentRoot5: set["flat11_CommittedType"] = None, flat11_DocumentRoot7: set["flat11_InitType"] = None, flat11_DocumentRoot: set["flat11_EStringToStringMapEntry"] = None, flat11_DocumentRoot11: set["flat11_LocationType"] = None, flat11_DocumentRoot21: set["flat11_SourceType"] = None, flat11_DocumentRoot13: set["flat11_NailType"] = None, flat11_DocumentRoot15: set["flat11_NameType"] = None, flat11_DocumentRoot17: set["flat11_NtaType"] = None, flat11_DocumentRoot9: set["flat11_LabelType"] = None, flat11_DocumentRoot19: set["flat11_ParameterType"] = None, flat11_DocumentRoot23: set["flat11_TargetType"] = None, flat11_DocumentRoot25: set["flat11_TemplateType"] = None, flat11_DocumentRoot27: set["flat11_TransitionType"] = None, flat11_DocumentRoot29: set["flat11_UrgentType"] = None):
        self.declaration = declaration
        self.imports = imports
        self.instantiation = instantiation
        self.mixed = mixed
        self.system = system
        self.flat11_DocumentRoot2 = flat11_DocumentRoot2 if flat11_DocumentRoot2 is not None else set()
        self.flat11_DocumentRoot5 = flat11_DocumentRoot5 if flat11_DocumentRoot5 is not None else set()
        self.flat11_DocumentRoot7 = flat11_DocumentRoot7 if flat11_DocumentRoot7 is not None else set()
        self.flat11_DocumentRoot = flat11_DocumentRoot if flat11_DocumentRoot is not None else set()
        self.flat11_DocumentRoot11 = flat11_DocumentRoot11 if flat11_DocumentRoot11 is not None else set()
        self.flat11_DocumentRoot21 = flat11_DocumentRoot21 if flat11_DocumentRoot21 is not None else set()
        self.flat11_DocumentRoot13 = flat11_DocumentRoot13 if flat11_DocumentRoot13 is not None else set()
        self.flat11_DocumentRoot15 = flat11_DocumentRoot15 if flat11_DocumentRoot15 is not None else set()
        self.flat11_DocumentRoot17 = flat11_DocumentRoot17 if flat11_DocumentRoot17 is not None else set()
        self.flat11_DocumentRoot9 = flat11_DocumentRoot9 if flat11_DocumentRoot9 is not None else set()
        self.flat11_DocumentRoot19 = flat11_DocumentRoot19 if flat11_DocumentRoot19 is not None else set()
        self.flat11_DocumentRoot23 = flat11_DocumentRoot23 if flat11_DocumentRoot23 is not None else set()
        self.flat11_DocumentRoot25 = flat11_DocumentRoot25 if flat11_DocumentRoot25 is not None else set()
        self.flat11_DocumentRoot27 = flat11_DocumentRoot27 if flat11_DocumentRoot27 is not None else set()
        self.flat11_DocumentRoot29 = flat11_DocumentRoot29 if flat11_DocumentRoot29 is not None else set()
        
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
    def declaration(self) -> str:
        return self.__declaration

    @declaration.setter
    def declaration(self, declaration: str):
        self.__declaration = declaration

    @property
    def instantiation(self) -> str:
        return self.__instantiation

    @instantiation.setter
    def instantiation(self, instantiation: str):
        self.__instantiation = instantiation

    @property
    def flat11_DocumentRoot19(self):
        return self.__flat11_DocumentRoot19

    @flat11_DocumentRoot19.setter
    def flat11_DocumentRoot19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_flat11_DocumentRoot__flat11_DocumentRoot19", None)
        self.__flat11_DocumentRoot19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "flat11_ParameterType"):
                    opp_val = getattr(item, "flat11_ParameterType", None)
                    
                    if opp_val == self:
                        setattr(item, "flat11_ParameterType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "flat11_ParameterType"):
                    opp_val = getattr(item, "flat11_ParameterType", None)
                    
                    setattr(item, "flat11_ParameterType", self)
                    

    @property
    def flat11_DocumentRoot15(self):
        return self.__flat11_DocumentRoot15

    @flat11_DocumentRoot15.setter
    def flat11_DocumentRoot15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_flat11_DocumentRoot__flat11_DocumentRoot15", None)
        self.__flat11_DocumentRoot15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "flat11_NameType"):
                    opp_val = getattr(item, "flat11_NameType", None)
                    
                    if opp_val == self:
                        setattr(item, "flat11_NameType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "flat11_NameType"):
                    opp_val = getattr(item, "flat11_NameType", None)
                    
                    setattr(item, "flat11_NameType", self)
                    

    @property
    def flat11_DocumentRoot23(self):
        return self.__flat11_DocumentRoot23

    @flat11_DocumentRoot23.setter
    def flat11_DocumentRoot23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_flat11_DocumentRoot__flat11_DocumentRoot23", None)
        self.__flat11_DocumentRoot23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "flat11_TargetType"):
                    opp_val = getattr(item, "flat11_TargetType", None)
                    
                    if opp_val == self:
                        setattr(item, "flat11_TargetType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "flat11_TargetType"):
                    opp_val = getattr(item, "flat11_TargetType", None)
                    
                    setattr(item, "flat11_TargetType", self)
                    

    @property
    def flat11_DocumentRoot(self):
        return self.__flat11_DocumentRoot

    @flat11_DocumentRoot.setter
    def flat11_DocumentRoot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_flat11_DocumentRoot__flat11_DocumentRoot", None)
        self.__flat11_DocumentRoot = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "flat11_EStringToStringMapEntry"):
                    opp_val = getattr(item, "flat11_EStringToStringMapEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "flat11_EStringToStringMapEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "flat11_EStringToStringMapEntry"):
                    opp_val = getattr(item, "flat11_EStringToStringMapEntry", None)
                    
                    setattr(item, "flat11_EStringToStringMapEntry", self)
                    

    @property
    def flat11_DocumentRoot9(self):
        return self.__flat11_DocumentRoot9

    @flat11_DocumentRoot9.setter
    def flat11_DocumentRoot9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_flat11_DocumentRoot__flat11_DocumentRoot9", None)
        self.__flat11_DocumentRoot9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "flat11_LabelType"):
                    opp_val = getattr(item, "flat11_LabelType", None)
                    
                    if opp_val == self:
                        setattr(item, "flat11_LabelType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "flat11_LabelType"):
                    opp_val = getattr(item, "flat11_LabelType", None)
                    
                    setattr(item, "flat11_LabelType", self)
                    

    @property
    def flat11_DocumentRoot2(self):
        return self.__flat11_DocumentRoot2

    @flat11_DocumentRoot2.setter
    def flat11_DocumentRoot2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_flat11_DocumentRoot__flat11_DocumentRoot2", None)
        self.__flat11_DocumentRoot2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "flat11_EStringToStringMapEntry3"):
                    opp_val = getattr(item, "flat11_EStringToStringMapEntry3", None)
                    
                    if opp_val == self:
                        setattr(item, "flat11_EStringToStringMapEntry3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "flat11_EStringToStringMapEntry3"):
                    opp_val = getattr(item, "flat11_EStringToStringMapEntry3", None)
                    
                    setattr(item, "flat11_EStringToStringMapEntry3", self)
                    

    @property
    def flat11_DocumentRoot29(self):
        return self.__flat11_DocumentRoot29

    @flat11_DocumentRoot29.setter
    def flat11_DocumentRoot29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_flat11_DocumentRoot__flat11_DocumentRoot29", None)
        self.__flat11_DocumentRoot29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "flat11_UrgentType"):
                    opp_val = getattr(item, "flat11_UrgentType", None)
                    
                    if opp_val == self:
                        setattr(item, "flat11_UrgentType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "flat11_UrgentType"):
                    opp_val = getattr(item, "flat11_UrgentType", None)
                    
                    setattr(item, "flat11_UrgentType", self)
                    

    @property
    def flat11_DocumentRoot21(self):
        return self.__flat11_DocumentRoot21

    @flat11_DocumentRoot21.setter
    def flat11_DocumentRoot21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_flat11_DocumentRoot__flat11_DocumentRoot21", None)
        self.__flat11_DocumentRoot21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "flat11_SourceType"):
                    opp_val = getattr(item, "flat11_SourceType", None)
                    
                    if opp_val == self:
                        setattr(item, "flat11_SourceType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "flat11_SourceType"):
                    opp_val = getattr(item, "flat11_SourceType", None)
                    
                    setattr(item, "flat11_SourceType", self)
                    

    @property
    def flat11_DocumentRoot17(self):
        return self.__flat11_DocumentRoot17

    @flat11_DocumentRoot17.setter
    def flat11_DocumentRoot17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_flat11_DocumentRoot__flat11_DocumentRoot17", None)
        self.__flat11_DocumentRoot17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "flat11_NtaType"):
                    opp_val = getattr(item, "flat11_NtaType", None)
                    
                    if opp_val == self:
                        setattr(item, "flat11_NtaType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "flat11_NtaType"):
                    opp_val = getattr(item, "flat11_NtaType", None)
                    
                    setattr(item, "flat11_NtaType", self)
                    

    @property
    def flat11_DocumentRoot25(self):
        return self.__flat11_DocumentRoot25

    @flat11_DocumentRoot25.setter
    def flat11_DocumentRoot25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_flat11_DocumentRoot__flat11_DocumentRoot25", None)
        self.__flat11_DocumentRoot25 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "flat11_TemplateType"):
                    opp_val = getattr(item, "flat11_TemplateType", None)
                    
                    if opp_val == self:
                        setattr(item, "flat11_TemplateType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "flat11_TemplateType"):
                    opp_val = getattr(item, "flat11_TemplateType", None)
                    
                    setattr(item, "flat11_TemplateType", self)
                    

    @property
    def flat11_DocumentRoot7(self):
        return self.__flat11_DocumentRoot7

    @flat11_DocumentRoot7.setter
    def flat11_DocumentRoot7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_flat11_DocumentRoot__flat11_DocumentRoot7", None)
        self.__flat11_DocumentRoot7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "flat11_InitType"):
                    opp_val = getattr(item, "flat11_InitType", None)
                    
                    if opp_val == self:
                        setattr(item, "flat11_InitType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "flat11_InitType"):
                    opp_val = getattr(item, "flat11_InitType", None)
                    
                    setattr(item, "flat11_InitType", self)
                    

    @property
    def flat11_DocumentRoot27(self):
        return self.__flat11_DocumentRoot27

    @flat11_DocumentRoot27.setter
    def flat11_DocumentRoot27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_flat11_DocumentRoot__flat11_DocumentRoot27", None)
        self.__flat11_DocumentRoot27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "flat11_TransitionType"):
                    opp_val = getattr(item, "flat11_TransitionType", None)
                    
                    if opp_val == self:
                        setattr(item, "flat11_TransitionType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "flat11_TransitionType"):
                    opp_val = getattr(item, "flat11_TransitionType", None)
                    
                    setattr(item, "flat11_TransitionType", self)
                    

    @property
    def flat11_DocumentRoot5(self):
        return self.__flat11_DocumentRoot5

    @flat11_DocumentRoot5.setter
    def flat11_DocumentRoot5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_flat11_DocumentRoot__flat11_DocumentRoot5", None)
        self.__flat11_DocumentRoot5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "flat11_CommittedType"):
                    opp_val = getattr(item, "flat11_CommittedType", None)
                    
                    if opp_val == self:
                        setattr(item, "flat11_CommittedType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "flat11_CommittedType"):
                    opp_val = getattr(item, "flat11_CommittedType", None)
                    
                    setattr(item, "flat11_CommittedType", self)
                    

    @property
    def flat11_DocumentRoot11(self):
        return self.__flat11_DocumentRoot11

    @flat11_DocumentRoot11.setter
    def flat11_DocumentRoot11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_flat11_DocumentRoot__flat11_DocumentRoot11", None)
        self.__flat11_DocumentRoot11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "flat11_LocationType"):
                    opp_val = getattr(item, "flat11_LocationType", None)
                    
                    if opp_val == self:
                        setattr(item, "flat11_LocationType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "flat11_LocationType"):
                    opp_val = getattr(item, "flat11_LocationType", None)
                    
                    setattr(item, "flat11_LocationType", self)
                    

    @property
    def flat11_DocumentRoot13(self):
        return self.__flat11_DocumentRoot13

    @flat11_DocumentRoot13.setter
    def flat11_DocumentRoot13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_flat11_DocumentRoot__flat11_DocumentRoot13", None)
        self.__flat11_DocumentRoot13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "flat11_NailType"):
                    opp_val = getattr(item, "flat11_NailType", None)
                    
                    if opp_val == self:
                        setattr(item, "flat11_NailType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "flat11_NailType"):
                    opp_val = getattr(item, "flat11_NailType", None)
                    
                    setattr(item, "flat11_NailType", self)
                    

class flat11_CommittedType:

    pass
class flat11_InitType:

    def __init__(self, ref: str, flat11_InitType: "flat11_DocumentRoot" = None, flat11_InitType56: "flat11_TemplateType" = None):
        self.ref = ref
        self.flat11_InitType = flat11_InitType
        self.flat11_InitType56 = flat11_InitType56
        
    @property
    def ref(self) -> str:
        return self.__ref

    @ref.setter
    def ref(self, ref: str):
        self.__ref = ref

    @property
    def flat11_InitType56(self):
        return self.__flat11_InitType56

    @flat11_InitType56.setter
    def flat11_InitType56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_flat11_InitType__flat11_InitType56", None)
        self.__flat11_InitType56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "flat11_TemplateType55"):
                opp_val = getattr(old_value, "flat11_TemplateType55", None)
                if opp_val == self:
                    setattr(old_value, "flat11_TemplateType55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "flat11_TemplateType55"):
                opp_val = getattr(value, "flat11_TemplateType55", None)
                setattr(value, "flat11_TemplateType55", self)

    @property
    def flat11_InitType(self):
        return self.__flat11_InitType

    @flat11_InitType.setter
    def flat11_InitType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_flat11_InitType__flat11_InitType", None)
        self.__flat11_InitType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "flat11_DocumentRoot7"):
                opp_val = getattr(old_value, "flat11_DocumentRoot7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "flat11_DocumentRoot7"):
                opp_val = getattr(value, "flat11_DocumentRoot7", None)
                if opp_val is None:
                    setattr(value, "flat11_DocumentRoot7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
