from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Property:

    pass
class entities_Reference(Property):

    pass
class entities_SimpleProperty(Property):

    pass
class entities_Property:

    def __init__(self, name: str, many: bool, entities_Property: "entities_Entity" = None):
        self.name = name
        self.many = many
        self.entities_Property = entities_Property
        
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
            if hasattr(old_value, "entities_Entity6"):
                opp_val = getattr(old_value, "entities_Entity6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entities_Entity6"):
                opp_val = getattr(value, "entities_Entity6", None)
                if opp_val is None:
                    setattr(value, "entities_Entity6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Type:

    pass
class entities_Entity(Type):

    pass
class entities_SimpleType(Type):

    pass
class entities_Type:

    def __init__(self, name: str, entities_Type: "entities_Model" = None):
        self.name = name
        self.entities_Type = entities_Type
        
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
            if hasattr(old_value, "entities_Model2"):
                opp_val = getattr(old_value, "entities_Model2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entities_Model2"):
                opp_val = getattr(value, "entities_Model2", None)
                if opp_val is None:
                    setattr(value, "entities_Model2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class entities_Import:

    def __init__(self, importURI: str, entities_Import: "entities_Model" = None):
        self.importURI = importURI
        self.entities_Import = entities_Import
        
    @property
    def importURI(self) -> str:
        return self.__importURI

    @importURI.setter
    def importURI(self, importURI: str):
        self.__importURI = importURI

    @property
    def entities_Import(self):
        return self.__entities_Import

    @entities_Import.setter
    def entities_Import(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entities_Import__entities_Import", None)
        self.__entities_Import = value
        
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