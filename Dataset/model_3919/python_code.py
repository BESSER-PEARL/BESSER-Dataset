from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class entityDsl_Type:

    def __init__(self, name: str, entityDsl_Type7: "entityDsl_Property" = None, entityDsl_Type: "entityDsl_Model" = None):
        self.name = name
        self.entityDsl_Type7 = entityDsl_Type7
        self.entityDsl_Type = entityDsl_Type
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def entityDsl_Type(self):
        return self.__entityDsl_Type

    @entityDsl_Type.setter
    def entityDsl_Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityDsl_Type__entityDsl_Type", None)
        self.__entityDsl_Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entityDsl_Model"):
                opp_val = getattr(old_value, "entityDsl_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entityDsl_Model"):
                opp_val = getattr(value, "entityDsl_Model", None)
                if opp_val is None:
                    setattr(value, "entityDsl_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def entityDsl_Type7(self):
        return self.__entityDsl_Type7

    @entityDsl_Type7.setter
    def entityDsl_Type7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityDsl_Type__entityDsl_Type7", None)
        self.__entityDsl_Type7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entityDsl_Property6"):
                opp_val = getattr(old_value, "entityDsl_Property6", None)
                if opp_val == self:
                    setattr(old_value, "entityDsl_Property6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entityDsl_Property6"):
                opp_val = getattr(value, "entityDsl_Property6", None)
                setattr(value, "entityDsl_Property6", self)

class entityDsl_Model:

    pass
class entityDsl_Property:

    def __init__(self, name: str, many: bool, entityDsl_Property: "entityDsl_Entity" = None, entityDsl_Property6: "entityDsl_Type" = None):
        self.name = name
        self.many = many
        self.entityDsl_Property = entityDsl_Property
        self.entityDsl_Property6 = entityDsl_Property6
        
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
    def entityDsl_Property6(self):
        return self.__entityDsl_Property6

    @entityDsl_Property6.setter
    def entityDsl_Property6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityDsl_Property__entityDsl_Property6", None)
        self.__entityDsl_Property6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entityDsl_Type7"):
                opp_val = getattr(old_value, "entityDsl_Type7", None)
                if opp_val == self:
                    setattr(old_value, "entityDsl_Type7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entityDsl_Type7"):
                opp_val = getattr(value, "entityDsl_Type7", None)
                setattr(value, "entityDsl_Type7", self)

    @property
    def entityDsl_Property(self):
        return self.__entityDsl_Property

    @entityDsl_Property.setter
    def entityDsl_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityDsl_Property__entityDsl_Property", None)
        self.__entityDsl_Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entityDsl_Entity4"):
                opp_val = getattr(old_value, "entityDsl_Entity4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entityDsl_Entity4"):
                opp_val = getattr(value, "entityDsl_Entity4", None)
                if opp_val is None:
                    setattr(value, "entityDsl_Entity4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Type:

    pass
class entityDsl_Entity(Type):

    pass
class entityDsl_SimpleType(Type):

    pass