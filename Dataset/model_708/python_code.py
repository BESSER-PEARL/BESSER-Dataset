from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class smalluml_Package:

    pass
class smalluml_Association:

    pass
class Type:

    pass
class smalluml_BooleanV(Type):

    def __init__(self, Value: str):
        self.Value = Value
        
    @property
    def Value(self) -> str:
        return self.__Value

    @Value.setter
    def Value(self, Value: str):
        self.__Value = Value

class smalluml_IntegerV(Type):

    def __init__(self, Value: str):
        self.Value = Value
        
    @property
    def Value(self) -> str:
        return self.__Value

    @Value.setter
    def Value(self, Value: str):
        self.__Value = Value

class smalluml_RealV(Type):

    def __init__(self, Value: str):
        self.Value = Value
        
    @property
    def Value(self) -> str:
        return self.__Value

    @Value.setter
    def Value(self, Value: str):
        self.__Value = Value

class smalluml_StringV(Type):

    def __init__(self, Value: str):
        self.Value = Value
        
    @property
    def Value(self) -> str:
        return self.__Value

    @Value.setter
    def Value(self, Value: str):
        self.__Value = Value

class Element:

    pass
class smalluml_NamedElement(Element):

    def __init__(self, Name: str):
        self.Name = Name
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

class smalluml_Element:

    pass
class smalluml_Attribute(Type):

    pass
class NamedElement:

    pass
class smalluml_Operation(NamedElement):

    pass
class smalluml_Enumeration(NamedElement):

    def __init__(self, enumValue: str):
        self.enumValue = enumValue
        
    @property
    def enumValue(self) -> str:
        return self.__enumValue

    @enumValue.setter
    def enumValue(self, enumValue: str):
        self.__enumValue = enumValue

class smalluml_Cardinalite(NamedElement):

    def __init__(self, lowerBound: str, upperBound: str, smalluml_Cardinalite: "smalluml_Association" = None, smalluml_Cardinalite17: "smalluml_Association" = None):
        self.lowerBound = lowerBound
        self.upperBound = upperBound
        self.smalluml_Cardinalite = smalluml_Cardinalite
        self.smalluml_Cardinalite17 = smalluml_Cardinalite17
        
    @property
    def upperBound(self) -> str:
        return self.__upperBound

    @upperBound.setter
    def upperBound(self, upperBound: str):
        self.__upperBound = upperBound

    @property
    def lowerBound(self) -> str:
        return self.__lowerBound

    @lowerBound.setter
    def lowerBound(self, lowerBound: str):
        self.__lowerBound = lowerBound

    @property
    def smalluml_Cardinalite(self):
        return self.__smalluml_Cardinalite

    @smalluml_Cardinalite.setter
    def smalluml_Cardinalite(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smalluml_Cardinalite__smalluml_Cardinalite", None)
        self.__smalluml_Cardinalite = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smalluml_Association14"):
                opp_val = getattr(old_value, "smalluml_Association14", None)
                if opp_val == self:
                    setattr(old_value, "smalluml_Association14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smalluml_Association14"):
                opp_val = getattr(value, "smalluml_Association14", None)
                setattr(value, "smalluml_Association14", self)

    @property
    def smalluml_Cardinalite17(self):
        return self.__smalluml_Cardinalite17

    @smalluml_Cardinalite17.setter
    def smalluml_Cardinalite17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smalluml_Cardinalite__smalluml_Cardinalite17", None)
        self.__smalluml_Cardinalite17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smalluml_Association16"):
                opp_val = getattr(old_value, "smalluml_Association16", None)
                if opp_val == self:
                    setattr(old_value, "smalluml_Association16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smalluml_Association16"):
                opp_val = getattr(value, "smalluml_Association16", None)
                setattr(value, "smalluml_Association16", self)

class smalluml_Type(NamedElement):

    pass
class smalluml_Class(NamedElement):

    pass