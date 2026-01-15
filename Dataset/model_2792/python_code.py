from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class ComponentPosition(Enum):
    Not_yet_defined = "Not_yet_defined"
    Local = "Local"
    Environmental_context = "Environmental_context"
class BasicFlowTransformationType(Enum):
    EEnumLiteral0 = "EEnumLiteral0"
    Transiform = "Transiform"
    Check_Verify_Validate = "Check_Verify_Validate"
    Control = "Control"
    Decide = "Decide"
    Measure = "Measure"
    Store = "Store"
    Wait = "Wait"
class ComponentType(Enum):
    Process = "Process"
    Activity = "Activity"
    Serrvice = "Serrvice"
    Actor = "Actor"
    Organization_Unit = "Organization_Unit"
    Site = "Site"
    Role = "Role"
    Physical_component = "Physical_component"
    Logical_component = "Logical_component"
    System = "System"
    Operational_system = "Operational_system"
    Information_system = "Information_system"
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
class RequirementOrigin(Enum):
    DesignChoise_induced = "DesignChoise_induced"
    Derived = "Derived"
    Originating = "Originating"


############################################
# Definition of Classes
############################################

class kreq103_Ffff:

    def __init__(self, id: str, kreq103_Ffff7: "kreq103_Ffff" = None, kreq103_Ffff5: set["kreq103_Ffff"] = None, kreq103_Ffff: "kreq103_Cccc" = None):
        self.id = id
        self.kreq103_Ffff7 = kreq103_Ffff7
        self.kreq103_Ffff5 = kreq103_Ffff5 if kreq103_Ffff5 is not None else set()
        self.kreq103_Ffff = kreq103_Ffff
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def kreq103_Ffff7(self):
        return self.__kreq103_Ffff7

    @kreq103_Ffff7.setter
    def kreq103_Ffff7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kreq103_Ffff__kreq103_Ffff7", None)
        self.__kreq103_Ffff7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "kreq103_Ffff5"):
                opp_val = getattr(old_value, "kreq103_Ffff5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kreq103_Ffff5"):
                opp_val = getattr(value, "kreq103_Ffff5", None)
                if opp_val is None:
                    setattr(value, "kreq103_Ffff5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def kreq103_Ffff5(self):
        return self.__kreq103_Ffff5

    @kreq103_Ffff5.setter
    def kreq103_Ffff5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kreq103_Ffff__kreq103_Ffff5", None)
        self.__kreq103_Ffff5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "kreq103_Ffff7"):
                    opp_val = getattr(item, "kreq103_Ffff7", None)
                    
                    if opp_val == self:
                        setattr(item, "kreq103_Ffff7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "kreq103_Ffff7"):
                    opp_val = getattr(item, "kreq103_Ffff7", None)
                    
                    setattr(item, "kreq103_Ffff7", self)
                    

    @property
    def kreq103_Ffff(self):
        return self.__kreq103_Ffff

    @kreq103_Ffff.setter
    def kreq103_Ffff(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kreq103_Ffff__kreq103_Ffff", None)
        self.__kreq103_Ffff = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "kreq103_Cccc4"):
                opp_val = getattr(old_value, "kreq103_Cccc4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kreq103_Cccc4"):
                opp_val = getattr(value, "kreq103_Cccc4", None)
                if opp_val is None:
                    setattr(value, "kreq103_Cccc4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class kreq103_Cccc:

    def __init__(self, id: str, kreq103_Cccc: "kreq103_Bbbb" = None, kreq103_Cccc4: set["kreq103_Ffff"] = None):
        self.id = id
        self.kreq103_Cccc = kreq103_Cccc
        self.kreq103_Cccc4 = kreq103_Cccc4 if kreq103_Cccc4 is not None else set()
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def kreq103_Cccc4(self):
        return self.__kreq103_Cccc4

    @kreq103_Cccc4.setter
    def kreq103_Cccc4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kreq103_Cccc__kreq103_Cccc4", None)
        self.__kreq103_Cccc4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "kreq103_Ffff"):
                    opp_val = getattr(item, "kreq103_Ffff", None)
                    
                    if opp_val == self:
                        setattr(item, "kreq103_Ffff", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "kreq103_Ffff"):
                    opp_val = getattr(item, "kreq103_Ffff", None)
                    
                    setattr(item, "kreq103_Ffff", self)
                    

    @property
    def kreq103_Cccc(self):
        return self.__kreq103_Cccc

    @kreq103_Cccc.setter
    def kreq103_Cccc(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kreq103_Cccc__kreq103_Cccc", None)
        self.__kreq103_Cccc = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "kreq103_Bbbb"):
                opp_val = getattr(old_value, "kreq103_Bbbb", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kreq103_Bbbb"):
                opp_val = getattr(value, "kreq103_Bbbb", None)
                if opp_val is None:
                    setattr(value, "kreq103_Bbbb", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class kreq103_Bbbb:

    pass
class kreq103_Gggg:

    def __init__(self, id: str, kreq103_Gggg: "kreq103_Bbbb" = None):
        self.id = id
        self.kreq103_Gggg = kreq103_Gggg
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def kreq103_Gggg(self):
        return self.__kreq103_Gggg

    @kreq103_Gggg.setter
    def kreq103_Gggg(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kreq103_Gggg__kreq103_Gggg", None)
        self.__kreq103_Gggg = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "kreq103_Bbbb2"):
                opp_val = getattr(old_value, "kreq103_Bbbb2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kreq103_Bbbb2"):
                opp_val = getattr(value, "kreq103_Bbbb2", None)
                if opp_val is None:
                    setattr(value, "kreq103_Bbbb2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
