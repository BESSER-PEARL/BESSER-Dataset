from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class entities_Property:

    def __init__(self, name: str, many: bool, entities_Property: "entities_Entity" = None, entities_Property6: "entities_Type" = None):
        self.name = name
        self.many = many
        self.entities_Property = entities_Property
        self.entities_Property6 = entities_Property6
        
    @property
    def many(self) -> bool:
        return self.__many

    @many.setter
    def many(self, many: bool):
        self.__many = many

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def entities_Property(self):
        return self.__entities_Property

    @entities_Property.setter
    def entities_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entities_Property__entities_Property", None)
        self.__entities_Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entities_Entity"):
                opp_val = getattr(old_value, "entities_Entity", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entities_Entity"):
                opp_val = getattr(value, "entities_Entity", None)
                if opp_val is None:
                    setattr(value, "entities_Entity", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def entities_Property6(self):
        return self.__entities_Property6

    @entities_Property6.setter
    def entities_Property6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entities_Property__entities_Property6", None)
        self.__entities_Property6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entities_Type7"):
                opp_val = getattr(old_value, "entities_Type7", None)
                if opp_val == self:
                    setattr(old_value, "entities_Type7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entities_Type7"):
                opp_val = getattr(value, "entities_Type7", None)
                setattr(value, "entities_Type7", self)

class Type:

    pass
class entities_Entity(Type):

    pass
class entities_SimpleType(Type):

    pass
class entities_Type:

    def __init__(self, name: str, entities_Type: "entities_Model" = None, entities_Type7: "entities_Property" = None):
        self.name = name
        self.entities_Type = entities_Type
        self.entities_Type7 = entities_Type7
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def entities_Type(self):
        return self.__entities_Type

    @entities_Type.setter
    def entities_Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entities_Type__entities_Type", None)
        self.__entities_Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entities_Model"):
                opp_val = getattr(old_value, "entities_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entities_Model"):
                opp_val = getattr(value, "entities_Model", None)
                if opp_val is None:
                    setattr(value, "entities_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def entities_Type7(self):
        return self.__entities_Type7

    @entities_Type7.setter
    def entities_Type7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entities_Type__entities_Type7", None)
        self.__entities_Type7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entities_Property6"):
                opp_val = getattr(old_value, "entities_Property6", None)
                if opp_val == self:
                    setattr(old_value, "entities_Property6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entities_Property6"):
                opp_val = getattr(value, "entities_Property6", None)
                setattr(value, "entities_Property6", self)

class entities_Model:

    pass