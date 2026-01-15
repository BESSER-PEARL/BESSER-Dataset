from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class entities_JAVAID:

    def __init__(self, name: str, entities_JAVAID: "entities_TypeDef" = None):
        self.name = name
        self.entities_JAVAID = entities_JAVAID
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def entities_JAVAID(self):
        return self.__entities_JAVAID

    @entities_JAVAID.setter
    def entities_JAVAID(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entities_JAVAID__entities_JAVAID", None)
        self.__entities_JAVAID = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entities_TypeDef"):
                opp_val = getattr(old_value, "entities_TypeDef", None)
                if opp_val == self:
                    setattr(old_value, "entities_TypeDef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entities_TypeDef"):
                opp_val = getattr(value, "entities_TypeDef", None)
                setattr(value, "entities_TypeDef", self)

class entities_Property:

    def __init__(self, name: str, many: bool, entities_Property: "entities_Type" = None, entities_Property9: "entities_Entity" = None):
        self.name = name
        self.many = many
        self.entities_Property = entities_Property
        self.entities_Property9 = entities_Property9
        
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
    def entities_Property9(self):
        return self.__entities_Property9

    @entities_Property9.setter
    def entities_Property9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entities_Property__entities_Property9", None)
        self.__entities_Property9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entities_Entity8"):
                opp_val = getattr(old_value, "entities_Entity8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entities_Entity8"):
                opp_val = getattr(value, "entities_Entity8", None)
                if opp_val is None:
                    setattr(value, "entities_Entity8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "entities_Type"):
                opp_val = getattr(old_value, "entities_Type", None)
                if opp_val == self:
                    setattr(old_value, "entities_Type", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entities_Type"):
                opp_val = getattr(value, "entities_Type", None)
                setattr(value, "entities_Type", self)

class Type:

    pass
class entities_Entity(Type):

    pass
class entities_SimpleType(Type):

    pass
class entities_PackagedType:

    def __init__(self, name: str, entities_PackagedType: "entities_Package" = None):
        self.name = name
        self.entities_PackagedType = entities_PackagedType
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def entities_PackagedType(self):
        return self.__entities_PackagedType

    @entities_PackagedType.setter
    def entities_PackagedType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entities_PackagedType__entities_PackagedType", None)
        self.__entities_PackagedType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entities_Package3"):
                opp_val = getattr(old_value, "entities_Package3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entities_Package3"):
                opp_val = getattr(value, "entities_Package3", None)
                if opp_val is None:
                    setattr(value, "entities_Package3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class PackagedType:

    pass
class entities_Type(PackagedType):

    pass
class entities_TypeDef:

    def __init__(self, name: str, entities_TypeDef: "entities_JAVAID" = None):
        self.name = name
        self.entities_TypeDef = entities_TypeDef
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def entities_TypeDef(self):
        return self.__entities_TypeDef

    @entities_TypeDef.setter
    def entities_TypeDef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entities_TypeDef__entities_TypeDef", None)
        self.__entities_TypeDef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entities_JAVAID"):
                opp_val = getattr(old_value, "entities_JAVAID", None)
                if opp_val == self:
                    setattr(old_value, "entities_JAVAID", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entities_JAVAID"):
                opp_val = getattr(value, "entities_JAVAID", None)
                setattr(value, "entities_JAVAID", self)

class entities_Package(PackagedType):

    pass
class entities_Model:

    pass