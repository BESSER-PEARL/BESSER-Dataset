from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class entitymm_Type(ABC):

    def __init__(self, name: str, entitymm_Type: "entitymm_Model" = None):
        self.name = name
        self.entitymm_Type = entitymm_Type
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def entitymm_Type(self):
        return self.__entitymm_Type

    @entitymm_Type.setter
    def entitymm_Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entitymm_Type__entitymm_Type", None)
        self.__entitymm_Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entitymm_Model"):
                opp_val = getattr(old_value, "entitymm_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entitymm_Model"):
                opp_val = getattr(value, "entitymm_Model", None)
                if opp_val is None:
                    setattr(value, "entitymm_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class entitymm_Model:

    def __init__(self, name: str, entitymm_Model: set["entitymm_Type"] = None):
        self.name = name
        self.entitymm_Model = entitymm_Model if entitymm_Model is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def entitymm_Model(self):
        return self.__entitymm_Model

    @entitymm_Model.setter
    def entitymm_Model(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entitymm_Model__entitymm_Model", None)
        self.__entitymm_Model = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "entitymm_Type"):
                    opp_val = getattr(item, "entitymm_Type", None)
                    
                    if opp_val == self:
                        setattr(item, "entitymm_Type", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "entitymm_Type"):
                    opp_val = getattr(item, "entitymm_Type", None)
                    
                    setattr(item, "entitymm_Type", self)
                    

class Type:

    pass
class entitymm_PrimitiveType(Type):

    pass
class entitymm_Entity(Type):

    def __init__(self, isPersistent: bool, size: int, desc: str, Entity: "entitymm_Attribute" = None, entity: set["entitymm_Attribute"] = None):
        self.isPersistent = isPersistent
        self.size = size
        self.desc = desc
        self.Entity = Entity
        self.entity = entity if entity is not None else set()
        
    @property
    def desc(self) -> str:
        return self.__desc

    @desc.setter
    def desc(self, desc: str):
        self.__desc = desc

    @property
    def size(self) -> int:
        return self.__size

    @size.setter
    def size(self, size: int):
        self.__size = size

    @property
    def isPersistent(self) -> bool:
        return self.__isPersistent

    @isPersistent.setter
    def isPersistent(self, isPersistent: bool):
        self.__isPersistent = isPersistent

    @property
    def entity(self):
        return self.__entity

    @entity.setter
    def entity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entitymm_Entity__entity", None)
        self.__entity = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Attribute"):
                    opp_val = getattr(item, "Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Attribute"):
                    opp_val = getattr(item, "Attribute", None)
                    
                    setattr(item, "Attribute", self)
                    

    @property
    def Entity(self):
        return self.__Entity

    @Entity.setter
    def Entity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entitymm_Entity__Entity", None)
        self.__Entity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "attributes"):
                opp_val = getattr(old_value, "attributes", None)
                if opp_val == self:
                    setattr(old_value, "attributes", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "attributes"):
                opp_val = getattr(value, "attributes", None)
                setattr(value, "attributes", self)

class entitymm_Attribute:

    def __init__(self, name: str, attributes: "entitymm_Entity" = None, entitymm_Attribute: "entitymm_PrimitiveType" = None, Attribute: "entitymm_Entity" = None):
        self.name = name
        self.attributes = attributes
        self.entitymm_Attribute = entitymm_Attribute
        self.Attribute = Attribute
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Attribute(self):
        return self.__Attribute

    @Attribute.setter
    def Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entitymm_Attribute__Attribute", None)
        self.__Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entity"):
                opp_val = getattr(old_value, "entity", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entity"):
                opp_val = getattr(value, "entity", None)
                if opp_val is None:
                    setattr(value, "entity", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def entitymm_Attribute(self):
        return self.__entitymm_Attribute

    @entitymm_Attribute.setter
    def entitymm_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entitymm_Attribute__entitymm_Attribute", None)
        self.__entitymm_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entitymm_PrimitiveType"):
                opp_val = getattr(old_value, "entitymm_PrimitiveType", None)
                if opp_val == self:
                    setattr(old_value, "entitymm_PrimitiveType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entitymm_PrimitiveType"):
                opp_val = getattr(value, "entitymm_PrimitiveType", None)
                setattr(value, "entitymm_PrimitiveType", self)

    @property
    def attributes(self):
        return self.__attributes

    @attributes.setter
    def attributes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entitymm_Attribute__attributes", None)
        self.__attributes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Entity"):
                opp_val = getattr(old_value, "Entity", None)
                if opp_val == self:
                    setattr(old_value, "Entity", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Entity"):
                opp_val = getattr(value, "Entity", None)
                setattr(value, "Entity", self)
