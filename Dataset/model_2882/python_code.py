from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Feature:

    pass
class entitiesDsl_Attribute(Feature):

    def __init__(self, attrrName: str, entitiesDsl_Attribute: "entitiesDsl_Type" = None):
        self.attrrName = attrrName
        self.entitiesDsl_Attribute = entitiesDsl_Attribute
        
    @property
    def attrrName(self) -> str:
        return self.__attrrName

    @attrrName.setter
    def attrrName(self, attrrName: str):
        self.__attrrName = attrrName

    @property
    def entitiesDsl_Attribute(self):
        return self.__entitiesDsl_Attribute

    @entitiesDsl_Attribute.setter
    def entitiesDsl_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entitiesDsl_Attribute__entitiesDsl_Attribute", None)
        self.__entitiesDsl_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entitiesDsl_Type3"):
                opp_val = getattr(old_value, "entitiesDsl_Type3", None)
                if opp_val == self:
                    setattr(old_value, "entitiesDsl_Type3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entitiesDsl_Type3"):
                opp_val = getattr(value, "entitiesDsl_Type3", None)
                setattr(value, "entitiesDsl_Type3", self)

class entitiesDsl_Feature:

    pass
class Type:

    pass
class entitiesDsl_Entity(Type):

    pass
class entitiesDsl_DataType(Type):

    pass
class entitiesDsl_Type:

    def __init__(self, name: str, entitiesDsl_Type: "entitiesDsl_Model" = None, entitiesDsl_Type3: "entitiesDsl_Attribute" = None):
        self.name = name
        self.entitiesDsl_Type = entitiesDsl_Type
        self.entitiesDsl_Type3 = entitiesDsl_Type3
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def entitiesDsl_Type(self):
        return self.__entitiesDsl_Type

    @entitiesDsl_Type.setter
    def entitiesDsl_Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entitiesDsl_Type__entitiesDsl_Type", None)
        self.__entitiesDsl_Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entitiesDsl_Model"):
                opp_val = getattr(old_value, "entitiesDsl_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entitiesDsl_Model"):
                opp_val = getattr(value, "entitiesDsl_Model", None)
                if opp_val is None:
                    setattr(value, "entitiesDsl_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def entitiesDsl_Type3(self):
        return self.__entitiesDsl_Type3

    @entitiesDsl_Type3.setter
    def entitiesDsl_Type3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entitiesDsl_Type__entitiesDsl_Type3", None)
        self.__entitiesDsl_Type3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entitiesDsl_Attribute"):
                opp_val = getattr(old_value, "entitiesDsl_Attribute", None)
                if opp_val == self:
                    setattr(old_value, "entitiesDsl_Attribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entitiesDsl_Attribute"):
                opp_val = getattr(value, "entitiesDsl_Attribute", None)
                setattr(value, "entitiesDsl_Attribute", self)

class entitiesDsl_Model:

    pass