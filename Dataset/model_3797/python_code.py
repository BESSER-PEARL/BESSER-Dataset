from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Entity_Entity:

    def __init__(self, name: str, inDomain: str, Entity: "Entity_System" = None, entity: "Entity_System" = None):
        self.name = name
        self.inDomain = inDomain
        self.Entity = Entity
        self.entity = entity
        
    @property
    def inDomain(self) -> str:
        return self.__inDomain

    @inDomain.setter
    def inDomain(self, inDomain: str):
        self.__inDomain = inDomain

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Entity(self):
        return self.__Entity

    @Entity.setter
    def Entity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Entity_Entity__Entity", None)
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
    def entity(self):
        return self.__entity

    @entity.setter
    def entity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Entity_Entity__entity", None)
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

class Entity_System:

    pass