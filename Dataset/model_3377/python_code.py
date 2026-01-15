from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Cascade(Enum):
    PERSIST = "PERSIST"
    REMOVE = "REMOVE"
    REFRESH = "REFRESH"
    MERGE = "MERGE"
    ALL = "ALL"
class Fetch(Enum):
    LAZY = "LAZY"
    EAGER = "EAGER"


############################################
# Definition of Classes
############################################

class Anotation:

    pass
class JPA_Column(Anotation):

    def __init__(self, nullable: bool, fetch: str, name: str, type: str):
        self.nullable = nullable
        self.fetch = fetch
        self.name = name
        self.type = type
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def nullable(self) -> bool:
        return self.__nullable

    @nullable.setter
    def nullable(self, nullable: bool):
        self.__nullable = nullable

    @property
    def fetch(self) -> str:
        return self.__fetch

    @fetch.setter
    def fetch(self, fetch: str):
        self.__fetch = fetch

class JPA_ManyToMany(Anotation):

    def __init__(self, name: str, joinColumn: str, inverseJoinColumn: str):
        self.name = name
        self.joinColumn = joinColumn
        self.inverseJoinColumn = inverseJoinColumn
        
    @property
    def joinColumn(self) -> str:
        return self.__joinColumn

    @joinColumn.setter
    def joinColumn(self, joinColumn: str):
        self.__joinColumn = joinColumn

    @property
    def inverseJoinColumn(self) -> str:
        return self.__inverseJoinColumn

    @inverseJoinColumn.setter
    def inverseJoinColumn(self, inverseJoinColumn: str):
        self.__inverseJoinColumn = inverseJoinColumn

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class JPA_Table(Anotation):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class JPA_EntityPk(Anotation):

    def __init__(self, name: str, JPA_EntityPk: set["JPA_Property"] = None):
        self.name = name
        self.JPA_EntityPk = JPA_EntityPk if JPA_EntityPk is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def JPA_EntityPk(self):
        return self.__JPA_EntityPk

    @JPA_EntityPk.setter
    def JPA_EntityPk(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JPA_EntityPk__JPA_EntityPk", None)
        self.__JPA_EntityPk = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "JPA_Property9"):
                    opp_val = getattr(item, "JPA_Property9", None)
                    
                    if opp_val == self:
                        setattr(item, "JPA_Property9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "JPA_Property9"):
                    opp_val = getattr(item, "JPA_Property9", None)
                    
                    setattr(item, "JPA_Property9", self)
                    

class JPA_ManyToOne(Anotation):

    def __init__(self, fetch: str, joinColumn: str, nullable: bool):
        self.fetch = fetch
        self.joinColumn = joinColumn
        self.nullable = nullable
        
    @property
    def nullable(self) -> bool:
        return self.__nullable

    @nullable.setter
    def nullable(self, nullable: bool):
        self.__nullable = nullable

    @property
    def fetch(self) -> str:
        return self.__fetch

    @fetch.setter
    def fetch(self, fetch: str):
        self.__fetch = fetch

    @property
    def joinColumn(self) -> str:
        return self.__joinColumn

    @joinColumn.setter
    def joinColumn(self, joinColumn: str):
        self.__joinColumn = joinColumn

class JPA_OneToMany(Anotation):

    def __init__(self, cascade: str, fetch: str):
        self.cascade = cascade
        self.fetch = fetch
        
    @property
    def fetch(self) -> str:
        return self.__fetch

    @fetch.setter
    def fetch(self, fetch: str):
        self.__fetch = fetch

    @property
    def cascade(self) -> str:
        return self.__cascade

    @cascade.setter
    def cascade(self, cascade: str):
        self.__cascade = cascade

class JPA_OneToOne(Anotation):

    def __init__(self, name: str, referencedColumnName: str, updatable: bool):
        self.name = name
        self.referencedColumnName = referencedColumnName
        self.updatable = updatable
        
    @property
    def updatable(self) -> bool:
        return self.__updatable

    @updatable.setter
    def updatable(self, updatable: bool):
        self.__updatable = updatable

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def referencedColumnName(self) -> str:
        return self.__referencedColumnName

    @referencedColumnName.setter
    def referencedColumnName(self, referencedColumnName: str):
        self.__referencedColumnName = referencedColumnName

class JPA_Entity:

    def __init__(self, name: str, comment: str, JPA_Entity2: set["JPA_Property"] = None, JPA_Entity4: set["JPA_Anotation"] = None, JPA_Entity: "JPA_PersistenceUnit" = None):
        self.name = name
        self.comment = comment
        self.JPA_Entity2 = JPA_Entity2 if JPA_Entity2 is not None else set()
        self.JPA_Entity4 = JPA_Entity4 if JPA_Entity4 is not None else set()
        self.JPA_Entity = JPA_Entity
        
    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def JPA_Entity(self):
        return self.__JPA_Entity

    @JPA_Entity.setter
    def JPA_Entity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JPA_Entity__JPA_Entity", None)
        self.__JPA_Entity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JPA_PersistenceUnit"):
                opp_val = getattr(old_value, "JPA_PersistenceUnit", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JPA_PersistenceUnit"):
                opp_val = getattr(value, "JPA_PersistenceUnit", None)
                if opp_val is None:
                    setattr(value, "JPA_PersistenceUnit", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def JPA_Entity2(self):
        return self.__JPA_Entity2

    @JPA_Entity2.setter
    def JPA_Entity2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JPA_Entity__JPA_Entity2", None)
        self.__JPA_Entity2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "JPA_Property"):
                    opp_val = getattr(item, "JPA_Property", None)
                    
                    if opp_val == self:
                        setattr(item, "JPA_Property", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "JPA_Property"):
                    opp_val = getattr(item, "JPA_Property", None)
                    
                    setattr(item, "JPA_Property", self)
                    

    @property
    def JPA_Entity4(self):
        return self.__JPA_Entity4

    @JPA_Entity4.setter
    def JPA_Entity4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JPA_Entity__JPA_Entity4", None)
        self.__JPA_Entity4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "JPA_Anotation"):
                    opp_val = getattr(item, "JPA_Anotation", None)
                    
                    if opp_val == self:
                        setattr(item, "JPA_Anotation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "JPA_Anotation"):
                    opp_val = getattr(item, "JPA_Anotation", None)
                    
                    setattr(item, "JPA_Anotation", self)
                    

class JPA_PersistenceUnit:

    pass
class JPA_Anotation:

    pass
class JPA_Property:

    def __init__(self, name: str, comment: str, JPA_Property: "JPA_Entity" = None, JPA_Property6: set["JPA_Anotation"] = None, JPA_Property9: "JPA_EntityPk" = None):
        self.name = name
        self.comment = comment
        self.JPA_Property = JPA_Property
        self.JPA_Property6 = JPA_Property6 if JPA_Property6 is not None else set()
        self.JPA_Property9 = JPA_Property9
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def JPA_Property(self):
        return self.__JPA_Property

    @JPA_Property.setter
    def JPA_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JPA_Property__JPA_Property", None)
        self.__JPA_Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JPA_Entity2"):
                opp_val = getattr(old_value, "JPA_Entity2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JPA_Entity2"):
                opp_val = getattr(value, "JPA_Entity2", None)
                if opp_val is None:
                    setattr(value, "JPA_Entity2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def JPA_Property9(self):
        return self.__JPA_Property9

    @JPA_Property9.setter
    def JPA_Property9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JPA_Property__JPA_Property9", None)
        self.__JPA_Property9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JPA_EntityPk"):
                opp_val = getattr(old_value, "JPA_EntityPk", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JPA_EntityPk"):
                opp_val = getattr(value, "JPA_EntityPk", None)
                if opp_val is None:
                    setattr(value, "JPA_EntityPk", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def JPA_Property6(self):
        return self.__JPA_Property6

    @JPA_Property6.setter
    def JPA_Property6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JPA_Property__JPA_Property6", None)
        self.__JPA_Property6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "JPA_Anotation7"):
                    opp_val = getattr(item, "JPA_Anotation7", None)
                    
                    if opp_val == self:
                        setattr(item, "JPA_Anotation7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "JPA_Anotation7"):
                    opp_val = getattr(item, "JPA_Anotation7", None)
                    
                    setattr(item, "JPA_Anotation7", self)
                    
