from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class yyc_Blias:

    def __init__(self, id: str, yyc_Blias: "yyc_RelatedTo" = None):
        self.id = id
        self.yyc_Blias = yyc_Blias
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def yyc_Blias(self):
        return self.__yyc_Blias

    @yyc_Blias.setter
    def yyc_Blias(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyc_Blias__yyc_Blias", None)
        self.__yyc_Blias = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "yyc_RelatedTo4"):
                opp_val = getattr(old_value, "yyc_RelatedTo4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "yyc_RelatedTo4"):
                opp_val = getattr(value, "yyc_RelatedTo4", None)
                if opp_val is None:
                    setattr(value, "yyc_RelatedTo4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class yyc_Alias:

    def __init__(self, id: str, yyc_Alias: "yyc_RelatedTo" = None):
        self.id = id
        self.yyc_Alias = yyc_Alias
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def yyc_Alias(self):
        return self.__yyc_Alias

    @yyc_Alias.setter
    def yyc_Alias(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyc_Alias__yyc_Alias", None)
        self.__yyc_Alias = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "yyc_RelatedTo"):
                opp_val = getattr(old_value, "yyc_RelatedTo", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "yyc_RelatedTo"):
                opp_val = getattr(value, "yyc_RelatedTo", None)
                if opp_val is None:
                    setattr(value, "yyc_RelatedTo", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class yyc_Thing:

    def __init__(self, id: int, fromThing: set["yyc_RelatedTo"] = None, Thing: "yyc_RelatedTo" = None):
        self.id = id
        self.fromThing = fromThing if fromThing is not None else set()
        self.Thing = Thing
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def Thing(self):
        return self.__Thing

    @Thing.setter
    def Thing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyc_Thing__Thing", None)
        self.__Thing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "relations"):
                opp_val = getattr(old_value, "relations", None)
                if opp_val == self:
                    setattr(old_value, "relations", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "relations"):
                opp_val = getattr(value, "relations", None)
                setattr(value, "relations", self)

    @property
    def fromThing(self):
        return self.__fromThing

    @fromThing.setter
    def fromThing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyc_Thing__fromThing", None)
        self.__fromThing = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RelatedTo"):
                    opp_val = getattr(item, "RelatedTo", None)
                    
                    if opp_val == self:
                        setattr(item, "RelatedTo", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RelatedTo"):
                    opp_val = getattr(item, "RelatedTo", None)
                    
                    setattr(item, "RelatedTo", self)
                    

class yyc_RelatedTo:

    def __init__(self, since: str, RelatedTo: "yyc_Thing" = None, relations: "yyc_Thing" = None, yyc_RelatedTo: set["yyc_Alias"] = None, yyc_RelatedTo4: set["yyc_Blias"] = None):
        self.since = since
        self.RelatedTo = RelatedTo
        self.relations = relations
        self.yyc_RelatedTo = yyc_RelatedTo if yyc_RelatedTo is not None else set()
        self.yyc_RelatedTo4 = yyc_RelatedTo4 if yyc_RelatedTo4 is not None else set()
        
    @property
    def since(self) -> str:
        return self.__since

    @since.setter
    def since(self, since: str):
        self.__since = since

    @property
    def yyc_RelatedTo(self):
        return self.__yyc_RelatedTo

    @yyc_RelatedTo.setter
    def yyc_RelatedTo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyc_RelatedTo__yyc_RelatedTo", None)
        self.__yyc_RelatedTo = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "yyc_Alias"):
                    opp_val = getattr(item, "yyc_Alias", None)
                    
                    if opp_val == self:
                        setattr(item, "yyc_Alias", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "yyc_Alias"):
                    opp_val = getattr(item, "yyc_Alias", None)
                    
                    setattr(item, "yyc_Alias", self)
                    

    @property
    def RelatedTo(self):
        return self.__RelatedTo

    @RelatedTo.setter
    def RelatedTo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyc_RelatedTo__RelatedTo", None)
        self.__RelatedTo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fromThing"):
                opp_val = getattr(old_value, "fromThing", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fromThing"):
                opp_val = getattr(value, "fromThing", None)
                if opp_val is None:
                    setattr(value, "fromThing", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def relations(self):
        return self.__relations

    @relations.setter
    def relations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyc_RelatedTo__relations", None)
        self.__relations = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Thing"):
                opp_val = getattr(old_value, "Thing", None)
                if opp_val == self:
                    setattr(old_value, "Thing", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Thing"):
                opp_val = getattr(value, "Thing", None)
                setattr(value, "Thing", self)

    @property
    def yyc_RelatedTo4(self):
        return self.__yyc_RelatedTo4

    @yyc_RelatedTo4.setter
    def yyc_RelatedTo4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyc_RelatedTo__yyc_RelatedTo4", None)
        self.__yyc_RelatedTo4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "yyc_Blias"):
                    opp_val = getattr(item, "yyc_Blias", None)
                    
                    if opp_val == self:
                        setattr(item, "yyc_Blias", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "yyc_Blias"):
                    opp_val = getattr(item, "yyc_Blias", None)
                    
                    setattr(item, "yyc_Blias", self)
                    
