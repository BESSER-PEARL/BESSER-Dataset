from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class panamaNeo4j_Entity:

    def __init__(self, name: str, panamaNeo4j_Entity: "panamaNeo4j_Officer" = None):
        self.name = name
        self.panamaNeo4j_Entity = panamaNeo4j_Entity
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def panamaNeo4j_Entity(self):
        return self.__panamaNeo4j_Entity

    @panamaNeo4j_Entity.setter
    def panamaNeo4j_Entity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_panamaNeo4j_Entity__panamaNeo4j_Entity", None)
        self.__panamaNeo4j_Entity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "panamaNeo4j_Officer"):
                opp_val = getattr(old_value, "panamaNeo4j_Officer", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "panamaNeo4j_Officer"):
                opp_val = getattr(value, "panamaNeo4j_Officer", None)
                if opp_val is None:
                    setattr(value, "panamaNeo4j_Officer", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class panamaNeo4j_Officer:

    def __init__(self, name: str, panamaNeo4j_Officer: set["panamaNeo4j_Entity"] = None):
        self.name = name
        self.panamaNeo4j_Officer = panamaNeo4j_Officer if panamaNeo4j_Officer is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def panamaNeo4j_Officer(self):
        return self.__panamaNeo4j_Officer

    @panamaNeo4j_Officer.setter
    def panamaNeo4j_Officer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_panamaNeo4j_Officer__panamaNeo4j_Officer", None)
        self.__panamaNeo4j_Officer = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "panamaNeo4j_Entity"):
                    opp_val = getattr(item, "panamaNeo4j_Entity", None)
                    
                    if opp_val == self:
                        setattr(item, "panamaNeo4j_Entity", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "panamaNeo4j_Entity"):
                    opp_val = getattr(item, "panamaNeo4j_Entity", None)
                    
                    setattr(item, "panamaNeo4j_Entity", self)
                    
