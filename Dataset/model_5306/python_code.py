from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class typeB_DefinitionB:

    def __init__(self, name: str, typeB_DefinitionB: "typeB_RootB" = None, typeB_DefinitionB5: "typeB_ElementB" = None):
        self.name = name
        self.typeB_DefinitionB = typeB_DefinitionB
        self.typeB_DefinitionB5 = typeB_DefinitionB5
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def typeB_DefinitionB5(self):
        return self.__typeB_DefinitionB5

    @typeB_DefinitionB5.setter
    def typeB_DefinitionB5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_typeB_DefinitionB__typeB_DefinitionB5", None)
        self.__typeB_DefinitionB5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "typeB_ElementB4"):
                opp_val = getattr(old_value, "typeB_ElementB4", None)
                if opp_val == self:
                    setattr(old_value, "typeB_ElementB4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "typeB_ElementB4"):
                opp_val = getattr(value, "typeB_ElementB4", None)
                setattr(value, "typeB_ElementB4", self)

    @property
    def typeB_DefinitionB(self):
        return self.__typeB_DefinitionB

    @typeB_DefinitionB.setter
    def typeB_DefinitionB(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_typeB_DefinitionB__typeB_DefinitionB", None)
        self.__typeB_DefinitionB = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "typeB_RootB2"):
                opp_val = getattr(old_value, "typeB_RootB2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "typeB_RootB2"):
                opp_val = getattr(value, "typeB_RootB2", None)
                if opp_val is None:
                    setattr(value, "typeB_RootB2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class typeB_ElementB:

    pass
class typeB_RootB:

    pass