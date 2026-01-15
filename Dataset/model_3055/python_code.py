from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Property:

    pass
class entities_ReferenceProperty(Property):

    def __init__(self, many: bool, entities_ReferenceProperty: "entities_Entity" = None):
        self.many = many
        self.entities_ReferenceProperty = entities_ReferenceProperty
        
    @property
    def many(self) -> bool:
        return self.__many

    @many.setter
    def many(self, many: bool):
        self.__many = many

    @property
    def entities_ReferenceProperty(self):
        return self.__entities_ReferenceProperty

    @entities_ReferenceProperty.setter
    def entities_ReferenceProperty(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entities_ReferenceProperty__entities_ReferenceProperty", None)
        self.__entities_ReferenceProperty = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entities_Entity7"):
                opp_val = getattr(old_value, "entities_Entity7", None)
                if opp_val == self:
                    setattr(old_value, "entities_Entity7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entities_Entity7"):
                opp_val = getattr(value, "entities_Entity7", None)
                setattr(value, "entities_Entity7", self)

class entities_SimpleProperty(Property):

    def __init__(self, type: str):
        self.type = type
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class entities_Property:

    def __init__(self, name: str, entities_Property: "entities_Entity" = None):
        self.name = name
        self.entities_Property = entities_Property
        
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
            if hasattr(old_value, "entities_Entity5"):
                opp_val = getattr(old_value, "entities_Entity5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entities_Entity5"):
                opp_val = getattr(value, "entities_Entity5", None)
                if opp_val is None:
                    setattr(value, "entities_Entity5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class entities_Entity:

    def __init__(self, name: str, entities_Entity: "entities_Model" = None, entities_Entity3: "entities_Entity" = None, entities_Entity1: "entities_Entity" = None, entities_Entity5: set["entities_Property"] = None, entities_Entity7: "entities_ReferenceProperty" = None):
        self.name = name
        self.entities_Entity = entities_Entity
        self.entities_Entity3 = entities_Entity3
        self.entities_Entity1 = entities_Entity1
        self.entities_Entity5 = entities_Entity5 if entities_Entity5 is not None else set()
        self.entities_Entity7 = entities_Entity7
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def entities_Entity5(self):
        return self.__entities_Entity5

    @entities_Entity5.setter
    def entities_Entity5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entities_Entity__entities_Entity5", None)
        self.__entities_Entity5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "entities_Property"):
                    opp_val = getattr(item, "entities_Property", None)
                    
                    if opp_val == self:
                        setattr(item, "entities_Property", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "entities_Property"):
                    opp_val = getattr(item, "entities_Property", None)
                    
                    setattr(item, "entities_Property", self)
                    

    @property
    def entities_Entity3(self):
        return self.__entities_Entity3

    @entities_Entity3.setter
    def entities_Entity3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entities_Entity__entities_Entity3", None)
        self.__entities_Entity3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entities_Entity1"):
                opp_val = getattr(old_value, "entities_Entity1", None)
                if opp_val == self:
                    setattr(old_value, "entities_Entity1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entities_Entity1"):
                opp_val = getattr(value, "entities_Entity1", None)
                setattr(value, "entities_Entity1", self)

    @property
    def entities_Entity1(self):
        return self.__entities_Entity1

    @entities_Entity1.setter
    def entities_Entity1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entities_Entity__entities_Entity1", None)
        self.__entities_Entity1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entities_Entity3"):
                opp_val = getattr(old_value, "entities_Entity3", None)
                if opp_val == self:
                    setattr(old_value, "entities_Entity3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entities_Entity3"):
                opp_val = getattr(value, "entities_Entity3", None)
                setattr(value, "entities_Entity3", self)

    @property
    def entities_Entity7(self):
        return self.__entities_Entity7

    @entities_Entity7.setter
    def entities_Entity7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entities_Entity__entities_Entity7", None)
        self.__entities_Entity7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entities_ReferenceProperty"):
                opp_val = getattr(old_value, "entities_ReferenceProperty", None)
                if opp_val == self:
                    setattr(old_value, "entities_ReferenceProperty", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entities_ReferenceProperty"):
                opp_val = getattr(value, "entities_ReferenceProperty", None)
                setattr(value, "entities_ReferenceProperty", self)

    @property
    def entities_Entity(self):
        return self.__entities_Entity

    @entities_Entity.setter
    def entities_Entity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entities_Entity__entities_Entity", None)
        self.__entities_Entity = value
        
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

class entities_Model:

    pass