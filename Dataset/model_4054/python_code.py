from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class smalluml_Diagram:

    pass
class smalluml_NamedElement:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class Type:

    pass
class smalluml_Int(Type):

    pass
class smalluml_String(Type):

    pass
class smalluml_Boolean(Type):

    pass
class smalluml_Float(Type):

    pass
class NamedElement:

    pass
class smalluml_Role(NamedElement):

    def __init__(self, upper: int, lower: int, smalluml_Role: "smalluml_Association" = None, smalluml_Role12: "smalluml_Association" = None, smalluml_Role14: "smalluml_Heritage" = None, smalluml_Role17: "smalluml_Heritage" = None, smalluml_Role19: "smalluml_Class" = None):
        self.upper = upper
        self.lower = lower
        self.smalluml_Role = smalluml_Role
        self.smalluml_Role12 = smalluml_Role12
        self.smalluml_Role14 = smalluml_Role14
        self.smalluml_Role17 = smalluml_Role17
        self.smalluml_Role19 = smalluml_Role19
        
    @property
    def upper(self) -> int:
        return self.__upper

    @upper.setter
    def upper(self, upper: int):
        self.__upper = upper

    @property
    def lower(self) -> int:
        return self.__lower

    @lower.setter
    def lower(self, lower: int):
        self.__lower = lower

    @property
    def smalluml_Role14(self):
        return self.__smalluml_Role14

    @smalluml_Role14.setter
    def smalluml_Role14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smalluml_Role__smalluml_Role14", None)
        self.__smalluml_Role14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smalluml_Heritage"):
                opp_val = getattr(old_value, "smalluml_Heritage", None)
                if opp_val == self:
                    setattr(old_value, "smalluml_Heritage", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smalluml_Heritage"):
                opp_val = getattr(value, "smalluml_Heritage", None)
                setattr(value, "smalluml_Heritage", self)

    @property
    def smalluml_Role12(self):
        return self.__smalluml_Role12

    @smalluml_Role12.setter
    def smalluml_Role12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smalluml_Role__smalluml_Role12", None)
        self.__smalluml_Role12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smalluml_Association11"):
                opp_val = getattr(old_value, "smalluml_Association11", None)
                if opp_val == self:
                    setattr(old_value, "smalluml_Association11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smalluml_Association11"):
                opp_val = getattr(value, "smalluml_Association11", None)
                setattr(value, "smalluml_Association11", self)

    @property
    def smalluml_Role19(self):
        return self.__smalluml_Role19

    @smalluml_Role19.setter
    def smalluml_Role19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smalluml_Role__smalluml_Role19", None)
        self.__smalluml_Role19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smalluml_Class20"):
                opp_val = getattr(old_value, "smalluml_Class20", None)
                if opp_val == self:
                    setattr(old_value, "smalluml_Class20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smalluml_Class20"):
                opp_val = getattr(value, "smalluml_Class20", None)
                setattr(value, "smalluml_Class20", self)

    @property
    def smalluml_Role17(self):
        return self.__smalluml_Role17

    @smalluml_Role17.setter
    def smalluml_Role17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smalluml_Role__smalluml_Role17", None)
        self.__smalluml_Role17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smalluml_Heritage16"):
                opp_val = getattr(old_value, "smalluml_Heritage16", None)
                if opp_val == self:
                    setattr(old_value, "smalluml_Heritage16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smalluml_Heritage16"):
                opp_val = getattr(value, "smalluml_Heritage16", None)
                setattr(value, "smalluml_Heritage16", self)

    @property
    def smalluml_Role(self):
        return self.__smalluml_Role

    @smalluml_Role.setter
    def smalluml_Role(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smalluml_Role__smalluml_Role", None)
        self.__smalluml_Role = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smalluml_Association"):
                opp_val = getattr(old_value, "smalluml_Association", None)
                if opp_val == self:
                    setattr(old_value, "smalluml_Association", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smalluml_Association"):
                opp_val = getattr(value, "smalluml_Association", None)
                setattr(value, "smalluml_Association", self)

class smalluml_Association(NamedElement):

    pass
class smalluml_Heritage(NamedElement):

    pass
class smalluml_Method(NamedElement):

    pass
class smalluml_Type(NamedElement):

    pass
class smalluml_Class(NamedElement):

    pass