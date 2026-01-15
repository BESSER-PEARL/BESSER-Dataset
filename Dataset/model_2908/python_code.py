from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class entity_Attribute:

    def __init__(self, many: bool, name: str, entity_Attribute7: "entity_Type" = None, entity_Attribute: "entity_Entity" = None):
        self.many = many
        self.name = name
        self.entity_Attribute7 = entity_Attribute7
        self.entity_Attribute = entity_Attribute
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def many(self) -> bool:
        return self.__many

    @many.setter
    def many(self, many: bool):
        self.__many = many

    @property
    def entity_Attribute7(self):
        return self.__entity_Attribute7

    @entity_Attribute7.setter
    def entity_Attribute7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entity_Attribute__entity_Attribute7", None)
        self.__entity_Attribute7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entity_Type8"):
                opp_val = getattr(old_value, "entity_Type8", None)
                if opp_val == self:
                    setattr(old_value, "entity_Type8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entity_Type8"):
                opp_val = getattr(value, "entity_Type8", None)
                setattr(value, "entity_Type8", self)

    @property
    def entity_Attribute(self):
        return self.__entity_Attribute

    @entity_Attribute.setter
    def entity_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entity_Attribute__entity_Attribute", None)
        self.__entity_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entity_Entity5"):
                opp_val = getattr(old_value, "entity_Entity5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entity_Entity5"):
                opp_val = getattr(value, "entity_Entity5", None)
                if opp_val is None:
                    setattr(value, "entity_Entity5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class entity_Type:

    def __init__(self, name: str, entity_Type: "entity_Model" = None, entity_Type8: "entity_Attribute" = None):
        self.name = name
        self.entity_Type = entity_Type
        self.entity_Type8 = entity_Type8
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def entity_Type(self):
        return self.__entity_Type

    @entity_Type.setter
    def entity_Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entity_Type__entity_Type", None)
        self.__entity_Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entity_Model"):
                opp_val = getattr(old_value, "entity_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entity_Model"):
                opp_val = getattr(value, "entity_Model", None)
                if opp_val is None:
                    setattr(value, "entity_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def entity_Type8(self):
        return self.__entity_Type8

    @entity_Type8.setter
    def entity_Type8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entity_Type__entity_Type8", None)
        self.__entity_Type8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entity_Attribute7"):
                opp_val = getattr(old_value, "entity_Attribute7", None)
                if opp_val == self:
                    setattr(old_value, "entity_Attribute7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entity_Attribute7"):
                opp_val = getattr(value, "entity_Attribute7", None)
                setattr(value, "entity_Attribute7", self)

class entity_Model:

    pass
class entity_JAVAID:

    def __init__(self, name: str, entity_JAVAID: "entity_TypeDef" = None):
        self.name = name
        self.entity_JAVAID = entity_JAVAID
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def entity_JAVAID(self):
        return self.__entity_JAVAID

    @entity_JAVAID.setter
    def entity_JAVAID(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entity_JAVAID__entity_JAVAID", None)
        self.__entity_JAVAID = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entity_TypeDef"):
                opp_val = getattr(old_value, "entity_TypeDef", None)
                if opp_val == self:
                    setattr(old_value, "entity_TypeDef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entity_TypeDef"):
                opp_val = getattr(value, "entity_TypeDef", None)
                setattr(value, "entity_TypeDef", self)

class Type:

    pass
class entity_Entity(Type):

    pass
class entity_TypeDef(Type):

    pass