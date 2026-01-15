from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class era_Relationship:

    def __init__(self, name: str, relationships: set["era_Entity"] = None, Relationship: "era_Entity" = None):
        self.name = name
        self.relationships = relationships if relationships is not None else set()
        self.Relationship = Relationship
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Relationship(self):
        return self.__Relationship

    @Relationship.setter
    def Relationship(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_era_Relationship__Relationship", None)
        self.__Relationship = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entities"):
                opp_val = getattr(old_value, "entities", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entities"):
                opp_val = getattr(value, "entities", None)
                if opp_val is None:
                    setattr(value, "entities", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def relationships(self):
        return self.__relationships

    @relationships.setter
    def relationships(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_era_Relationship__relationships", None)
        self.__relationships = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Entity4"):
                    opp_val = getattr(item, "Entity4", None)
                    
                    if opp_val == self:
                        setattr(item, "Entity4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Entity4"):
                    opp_val = getattr(item, "Entity4", None)
                    
                    setattr(item, "Entity4", self)
                    

class era_Entity:

    def __init__(self, name: str, inDomain: str, Entity4: "era_Relationship" = None, Entity: "era_System" = None, entity: "era_System" = None, entities: set["era_Relationship"] = None):
        self.name = name
        self.inDomain = inDomain
        self.Entity4 = Entity4
        self.Entity = Entity
        self.entity = entity
        self.entities = entities if entities is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def inDomain(self) -> str:
        return self.__inDomain

    @inDomain.setter
    def inDomain(self, inDomain: str):
        self.__inDomain = inDomain

    @property
    def Entity(self):
        return self.__Entity

    @Entity.setter
    def Entity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_era_Entity__Entity", None)
        self.__Entity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "system"):
                opp_val = getattr(old_value, "system", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "system"):
                opp_val = getattr(value, "system", None)
                if opp_val is None:
                    setattr(value, "system", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def entities(self):
        return self.__entities

    @entities.setter
    def entities(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_era_Entity__entities", None)
        self.__entities = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Relationship"):
                    opp_val = getattr(item, "Relationship", None)
                    
                    if opp_val == self:
                        setattr(item, "Relationship", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Relationship"):
                    opp_val = getattr(item, "Relationship", None)
                    
                    setattr(item, "Relationship", self)
                    

    @property
    def Entity4(self):
        return self.__Entity4

    @Entity4.setter
    def Entity4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_era_Entity__Entity4", None)
        self.__Entity4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "relationships"):
                opp_val = getattr(old_value, "relationships", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "relationships"):
                opp_val = getattr(value, "relationships", None)
                if opp_val is None:
                    setattr(value, "relationships", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def entity(self):
        return self.__entity

    @entity.setter
    def entity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_era_Entity__entity", None)
        self.__entity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "System"):
                opp_val = getattr(old_value, "System", None)
                if opp_val == self:
                    setattr(old_value, "System", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "System"):
                opp_val = getattr(value, "System", None)
                setattr(value, "System", self)

class era_System:

    pass
class era_Attribute:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name
