from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class basic_RelatedTo:

    def __init__(self, since: str, RelatedTo: "basic_Thing" = None, relations: "basic_Thing" = None, basic_RelatedTo: "basic_Thing" = None):
        self.since = since
        self.RelatedTo = RelatedTo
        self.relations = relations
        self.basic_RelatedTo = basic_RelatedTo
        
    @property
    def since(self) -> str:
        return self.__since

    @since.setter
    def since(self, since: str):
        self.__since = since

    @property
    def RelatedTo(self):
        return self.__RelatedTo

    @RelatedTo.setter
    def RelatedTo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basic_RelatedTo__RelatedTo", None)
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
        old_value = getattr(self, f"_basic_RelatedTo__relations", None)
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
    def basic_RelatedTo(self):
        return self.__basic_RelatedTo

    @basic_RelatedTo.setter
    def basic_RelatedTo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basic_RelatedTo__basic_RelatedTo", None)
        self.__basic_RelatedTo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basic_Thing4"):
                opp_val = getattr(old_value, "basic_Thing4", None)
                if opp_val == self:
                    setattr(old_value, "basic_Thing4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basic_Thing4"):
                opp_val = getattr(value, "basic_Thing4", None)
                setattr(value, "basic_Thing4", self)

class basic_Thing:

    def __init__(self, id: int, basic_Thing: "basic_World" = None, fromThing: set["basic_RelatedTo"] = None, Thing: "basic_RelatedTo" = None, basic_Thing4: "basic_RelatedTo" = None):
        self.id = id
        self.basic_Thing = basic_Thing
        self.fromThing = fromThing if fromThing is not None else set()
        self.Thing = Thing
        self.basic_Thing4 = basic_Thing4
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def basic_Thing4(self):
        return self.__basic_Thing4

    @basic_Thing4.setter
    def basic_Thing4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basic_Thing__basic_Thing4", None)
        self.__basic_Thing4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basic_RelatedTo"):
                opp_val = getattr(old_value, "basic_RelatedTo", None)
                if opp_val == self:
                    setattr(old_value, "basic_RelatedTo", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basic_RelatedTo"):
                opp_val = getattr(value, "basic_RelatedTo", None)
                setattr(value, "basic_RelatedTo", self)

    @property
    def Thing(self):
        return self.__Thing

    @Thing.setter
    def Thing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basic_Thing__Thing", None)
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
        old_value = getattr(self, f"_basic_Thing__fromThing", None)
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
                    

    @property
    def basic_Thing(self):
        return self.__basic_Thing

    @basic_Thing.setter
    def basic_Thing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basic_Thing__basic_Thing", None)
        self.__basic_Thing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basic_World"):
                opp_val = getattr(old_value, "basic_World", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basic_World"):
                opp_val = getattr(value, "basic_World", None)
                if opp_val is None:
                    setattr(value, "basic_World", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class basic_World:

    pass