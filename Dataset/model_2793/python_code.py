from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class ComponentPosition(Enum):
    Not_yet_defined = "Not_yet_defined"
    Local = "Local"
    Environmental_context = "Environmental_context"
class RequirementOrigin(Enum):
    Derived = "Derived"
    Originating = "Originating"
    DesignChoise_induced = "DesignChoise_induced"
class BasicFlowTransformationType(Enum):
    Decide = "Decide"
    EEnumLiteral0 = "EEnumLiteral0"
    Transiform = "Transiform"
    Check_Verify_Validate = "Check_Verify_Validate"
    Control = "Control"
    Measure = "Measure"
    Store = "Store"
    Wait = "Wait"
class ComponentType(Enum):
    Physical_component = "Physical_component"
    Logical_component = "Logical_component"
    System = "System"
    Operational_system = "Operational_system"
    Information_system = "Information_system"
    Process = "Process"
    Activity = "Activity"
    Serrvice = "Serrvice"
    Actor = "Actor"
    Organization_Unit = "Organization_Unit"
    Site = "Site"
    Role = "Role"
    Tool = "Tool"
    Not_yet_desighed = "Not_yet_desighed"
    Other = "Other"
class CategoryType(Enum):
    Functional = "Functional"
    Non_Functional = "Non_Functional"
    Operational = "Operational"
    VandV = "VandV"
    Interface = "Interface"
    Constraints = "Constraints"


############################################
# Definition of Classes
############################################

class kreq210_Llll:

    def __init__(self, id: str, kreq210_Llll: "kreq210_Gggg" = None, kreq210_Llll15: "kreq210_Cccc" = None, kreq210_Llll18: "kreq210_Hhhh" = None, kreq210_Llll21: set["kreq210_Mmmm"] = None):
        self.id = id
        self.kreq210_Llll = kreq210_Llll
        self.kreq210_Llll15 = kreq210_Llll15
        self.kreq210_Llll18 = kreq210_Llll18
        self.kreq210_Llll21 = kreq210_Llll21 if kreq210_Llll21 is not None else set()
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def kreq210_Llll15(self):
        return self.__kreq210_Llll15

    @kreq210_Llll15.setter
    def kreq210_Llll15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kreq210_Llll__kreq210_Llll15", None)
        self.__kreq210_Llll15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "kreq210_Cccc16"):
                opp_val = getattr(old_value, "kreq210_Cccc16", None)
                if opp_val == self:
                    setattr(old_value, "kreq210_Cccc16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kreq210_Cccc16"):
                opp_val = getattr(value, "kreq210_Cccc16", None)
                setattr(value, "kreq210_Cccc16", self)

    @property
    def kreq210_Llll(self):
        return self.__kreq210_Llll

    @kreq210_Llll.setter
    def kreq210_Llll(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kreq210_Llll__kreq210_Llll", None)
        self.__kreq210_Llll = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "kreq210_Gggg13"):
                opp_val = getattr(old_value, "kreq210_Gggg13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kreq210_Gggg13"):
                opp_val = getattr(value, "kreq210_Gggg13", None)
                if opp_val is None:
                    setattr(value, "kreq210_Gggg13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def kreq210_Llll18(self):
        return self.__kreq210_Llll18

    @kreq210_Llll18.setter
    def kreq210_Llll18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kreq210_Llll__kreq210_Llll18", None)
        self.__kreq210_Llll18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "kreq210_Hhhh19"):
                opp_val = getattr(old_value, "kreq210_Hhhh19", None)
                if opp_val == self:
                    setattr(old_value, "kreq210_Hhhh19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kreq210_Hhhh19"):
                opp_val = getattr(value, "kreq210_Hhhh19", None)
                setattr(value, "kreq210_Hhhh19", self)

    @property
    def kreq210_Llll21(self):
        return self.__kreq210_Llll21

    @kreq210_Llll21.setter
    def kreq210_Llll21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kreq210_Llll__kreq210_Llll21", None)
        self.__kreq210_Llll21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "kreq210_Mmmm22"):
                    opp_val = getattr(item, "kreq210_Mmmm22", None)
                    
                    if opp_val == self:
                        setattr(item, "kreq210_Mmmm22", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "kreq210_Mmmm22"):
                    opp_val = getattr(item, "kreq210_Mmmm22", None)
                    
                    setattr(item, "kreq210_Mmmm22", self)
                    

class kreq210_Ffff:

    def __init__(self, id: str, kreq210_Ffff: "kreq210_Cccc" = None, kreq210_Ffff11: "kreq210_Ffff" = None, kreq210_Ffff9: set["kreq210_Ffff"] = None):
        self.id = id
        self.kreq210_Ffff = kreq210_Ffff
        self.kreq210_Ffff11 = kreq210_Ffff11
        self.kreq210_Ffff9 = kreq210_Ffff9 if kreq210_Ffff9 is not None else set()
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def kreq210_Ffff(self):
        return self.__kreq210_Ffff

    @kreq210_Ffff.setter
    def kreq210_Ffff(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kreq210_Ffff__kreq210_Ffff", None)
        self.__kreq210_Ffff = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "kreq210_Cccc8"):
                opp_val = getattr(old_value, "kreq210_Cccc8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kreq210_Cccc8"):
                opp_val = getattr(value, "kreq210_Cccc8", None)
                if opp_val is None:
                    setattr(value, "kreq210_Cccc8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def kreq210_Ffff11(self):
        return self.__kreq210_Ffff11

    @kreq210_Ffff11.setter
    def kreq210_Ffff11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kreq210_Ffff__kreq210_Ffff11", None)
        self.__kreq210_Ffff11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "kreq210_Ffff9"):
                opp_val = getattr(old_value, "kreq210_Ffff9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kreq210_Ffff9"):
                opp_val = getattr(value, "kreq210_Ffff9", None)
                if opp_val is None:
                    setattr(value, "kreq210_Ffff9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def kreq210_Ffff9(self):
        return self.__kreq210_Ffff9

    @kreq210_Ffff9.setter
    def kreq210_Ffff9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kreq210_Ffff__kreq210_Ffff9", None)
        self.__kreq210_Ffff9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "kreq210_Ffff11"):
                    opp_val = getattr(item, "kreq210_Ffff11", None)
                    
                    if opp_val == self:
                        setattr(item, "kreq210_Ffff11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "kreq210_Ffff11"):
                    opp_val = getattr(item, "kreq210_Ffff11", None)
                    
                    setattr(item, "kreq210_Ffff11", self)
                    

class kreq210_Mmmm:

    def __init__(self, id: str, kreq210_Mmmm: "kreq210_Bbbb" = None, kreq210_Mmmm22: "kreq210_Llll" = None):
        self.id = id
        self.kreq210_Mmmm = kreq210_Mmmm
        self.kreq210_Mmmm22 = kreq210_Mmmm22
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def kreq210_Mmmm(self):
        return self.__kreq210_Mmmm

    @kreq210_Mmmm.setter
    def kreq210_Mmmm(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kreq210_Mmmm__kreq210_Mmmm", None)
        self.__kreq210_Mmmm = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "kreq210_Bbbb6"):
                opp_val = getattr(old_value, "kreq210_Bbbb6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kreq210_Bbbb6"):
                opp_val = getattr(value, "kreq210_Bbbb6", None)
                if opp_val is None:
                    setattr(value, "kreq210_Bbbb6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def kreq210_Mmmm22(self):
        return self.__kreq210_Mmmm22

    @kreq210_Mmmm22.setter
    def kreq210_Mmmm22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kreq210_Mmmm__kreq210_Mmmm22", None)
        self.__kreq210_Mmmm22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "kreq210_Llll21"):
                opp_val = getattr(old_value, "kreq210_Llll21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kreq210_Llll21"):
                opp_val = getattr(value, "kreq210_Llll21", None)
                if opp_val is None:
                    setattr(value, "kreq210_Llll21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class kreq210_Hhhh:

    def __init__(self, id: int, kreq210_Hhhh: "kreq210_Bbbb" = None, kreq210_Hhhh19: "kreq210_Llll" = None):
        self.id = id
        self.kreq210_Hhhh = kreq210_Hhhh
        self.kreq210_Hhhh19 = kreq210_Hhhh19
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def kreq210_Hhhh(self):
        return self.__kreq210_Hhhh

    @kreq210_Hhhh.setter
    def kreq210_Hhhh(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kreq210_Hhhh__kreq210_Hhhh", None)
        self.__kreq210_Hhhh = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "kreq210_Bbbb4"):
                opp_val = getattr(old_value, "kreq210_Bbbb4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kreq210_Bbbb4"):
                opp_val = getattr(value, "kreq210_Bbbb4", None)
                if opp_val is None:
                    setattr(value, "kreq210_Bbbb4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def kreq210_Hhhh19(self):
        return self.__kreq210_Hhhh19

    @kreq210_Hhhh19.setter
    def kreq210_Hhhh19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kreq210_Hhhh__kreq210_Hhhh19", None)
        self.__kreq210_Hhhh19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "kreq210_Llll18"):
                opp_val = getattr(old_value, "kreq210_Llll18", None)
                if opp_val == self:
                    setattr(old_value, "kreq210_Llll18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kreq210_Llll18"):
                opp_val = getattr(value, "kreq210_Llll18", None)
                setattr(value, "kreq210_Llll18", self)

class kreq210_Gggg:

    def __init__(self, id: str, kreq210_Gggg: "kreq210_Bbbb" = None, kreq210_Gggg13: set["kreq210_Llll"] = None):
        self.id = id
        self.kreq210_Gggg = kreq210_Gggg
        self.kreq210_Gggg13 = kreq210_Gggg13 if kreq210_Gggg13 is not None else set()
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def kreq210_Gggg13(self):
        return self.__kreq210_Gggg13

    @kreq210_Gggg13.setter
    def kreq210_Gggg13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kreq210_Gggg__kreq210_Gggg13", None)
        self.__kreq210_Gggg13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "kreq210_Llll"):
                    opp_val = getattr(item, "kreq210_Llll", None)
                    
                    if opp_val == self:
                        setattr(item, "kreq210_Llll", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "kreq210_Llll"):
                    opp_val = getattr(item, "kreq210_Llll", None)
                    
                    setattr(item, "kreq210_Llll", self)
                    

    @property
    def kreq210_Gggg(self):
        return self.__kreq210_Gggg

    @kreq210_Gggg.setter
    def kreq210_Gggg(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kreq210_Gggg__kreq210_Gggg", None)
        self.__kreq210_Gggg = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "kreq210_Bbbb2"):
                opp_val = getattr(old_value, "kreq210_Bbbb2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kreq210_Bbbb2"):
                opp_val = getattr(value, "kreq210_Bbbb2", None)
                if opp_val is None:
                    setattr(value, "kreq210_Bbbb2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class kreq210_Cccc:

    def __init__(self, id: str, kreq210_Cccc: "kreq210_Bbbb" = None, kreq210_Cccc8: set["kreq210_Ffff"] = None, kreq210_Cccc16: "kreq210_Llll" = None):
        self.id = id
        self.kreq210_Cccc = kreq210_Cccc
        self.kreq210_Cccc8 = kreq210_Cccc8 if kreq210_Cccc8 is not None else set()
        self.kreq210_Cccc16 = kreq210_Cccc16
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def kreq210_Cccc16(self):
        return self.__kreq210_Cccc16

    @kreq210_Cccc16.setter
    def kreq210_Cccc16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kreq210_Cccc__kreq210_Cccc16", None)
        self.__kreq210_Cccc16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "kreq210_Llll15"):
                opp_val = getattr(old_value, "kreq210_Llll15", None)
                if opp_val == self:
                    setattr(old_value, "kreq210_Llll15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kreq210_Llll15"):
                opp_val = getattr(value, "kreq210_Llll15", None)
                setattr(value, "kreq210_Llll15", self)

    @property
    def kreq210_Cccc(self):
        return self.__kreq210_Cccc

    @kreq210_Cccc.setter
    def kreq210_Cccc(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kreq210_Cccc__kreq210_Cccc", None)
        self.__kreq210_Cccc = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "kreq210_Bbbb"):
                opp_val = getattr(old_value, "kreq210_Bbbb", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kreq210_Bbbb"):
                opp_val = getattr(value, "kreq210_Bbbb", None)
                if opp_val is None:
                    setattr(value, "kreq210_Bbbb", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def kreq210_Cccc8(self):
        return self.__kreq210_Cccc8

    @kreq210_Cccc8.setter
    def kreq210_Cccc8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kreq210_Cccc__kreq210_Cccc8", None)
        self.__kreq210_Cccc8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "kreq210_Ffff"):
                    opp_val = getattr(item, "kreq210_Ffff", None)
                    
                    if opp_val == self:
                        setattr(item, "kreq210_Ffff", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "kreq210_Ffff"):
                    opp_val = getattr(item, "kreq210_Ffff", None)
                    
                    setattr(item, "kreq210_Ffff", self)
                    

class kreq210_Bbbb:

    pass