from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class entities_Entity:

    def __init__(self, name: str, entities_Entity3: "entities_Entity" = None, entities_Entity1: "entities_Entity" = None, entities_Entity5: set["entities_Feature"] = None, entities_Entity8: "entities_Feature" = None, entities_Entity: "entities_DomainModel" = None):
        self.name = name
        self.entities_Entity3 = entities_Entity3
        self.entities_Entity1 = entities_Entity1
        self.entities_Entity5 = entities_Entity5 if entities_Entity5 is not None else set()
        self.entities_Entity8 = entities_Entity8
        self.entities_Entity = entities_Entity
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
    def entities_Entity(self):
        return self.__entities_Entity

    @entities_Entity.setter
    def entities_Entity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entities_Entity__entities_Entity", None)
        self.__entities_Entity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entities_DomainModel"):
                opp_val = getattr(old_value, "entities_DomainModel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entities_DomainModel"):
                opp_val = getattr(value, "entities_DomainModel", None)
                if opp_val is None:
                    setattr(value, "entities_DomainModel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def entities_Entity8(self):
        return self.__entities_Entity8

    @entities_Entity8.setter
    def entities_Entity8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entities_Entity__entities_Entity8", None)
        self.__entities_Entity8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entities_Feature7"):
                opp_val = getattr(old_value, "entities_Feature7", None)
                if opp_val == self:
                    setattr(old_value, "entities_Feature7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entities_Feature7"):
                opp_val = getattr(value, "entities_Feature7", None)
                setattr(value, "entities_Feature7", self)

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
                if hasattr(item, "entities_Feature"):
                    opp_val = getattr(item, "entities_Feature", None)
                    
                    if opp_val == self:
                        setattr(item, "entities_Feature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "entities_Feature"):
                    opp_val = getattr(item, "entities_Feature", None)
                    
                    setattr(item, "entities_Feature", self)
                    

class entities_DomainModel:

    pass
class entities_Feature:

    def __init__(self, name: str, many: bool, entities_Feature: "entities_Entity" = None, entities_Feature7: "entities_Entity" = None):
        self.name = name
        self.many = many
        self.entities_Feature = entities_Feature
        self.entities_Feature7 = entities_Feature7
        
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
    def entities_Feature(self):
        return self.__entities_Feature

    @entities_Feature.setter
    def entities_Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entities_Feature__entities_Feature", None)
        self.__entities_Feature = value
        
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

    @property
    def entities_Feature7(self):
        return self.__entities_Feature7

    @entities_Feature7.setter
    def entities_Feature7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entities_Feature__entities_Feature7", None)
        self.__entities_Feature7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entities_Entity8"):
                opp_val = getattr(old_value, "entities_Entity8", None)
                if opp_val == self:
                    setattr(old_value, "entities_Entity8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entities_Entity8"):
                opp_val = getattr(value, "entities_Entity8", None)
                setattr(value, "entities_Entity8", self)
