from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class workbench101_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class workbench101_Workbench:

    def __init__(self, aprop: str, workbench101_Workbench: set["workbench101_Thing"] = None, workbench101_Workbench2: set["workbench101_Thoughts"] = None):
        self.aprop = aprop
        self.workbench101_Workbench = workbench101_Workbench if workbench101_Workbench is not None else set()
        self.workbench101_Workbench2 = workbench101_Workbench2 if workbench101_Workbench2 is not None else set()
        
    @property
    def aprop(self) -> str:
        return self.__aprop

    @aprop.setter
    def aprop(self, aprop: str):
        self.__aprop = aprop

    @property
    def workbench101_Workbench2(self):
        return self.__workbench101_Workbench2

    @workbench101_Workbench2.setter
    def workbench101_Workbench2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workbench101_Workbench__workbench101_Workbench2", None)
        self.__workbench101_Workbench2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "workbench101_Thoughts"):
                    opp_val = getattr(item, "workbench101_Thoughts", None)
                    
                    if opp_val == self:
                        setattr(item, "workbench101_Thoughts", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "workbench101_Thoughts"):
                    opp_val = getattr(item, "workbench101_Thoughts", None)
                    
                    setattr(item, "workbench101_Thoughts", self)
                    

    @property
    def workbench101_Workbench(self):
        return self.__workbench101_Workbench

    @workbench101_Workbench.setter
    def workbench101_Workbench(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workbench101_Workbench__workbench101_Workbench", None)
        self.__workbench101_Workbench = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "workbench101_Thing"):
                    opp_val = getattr(item, "workbench101_Thing", None)
                    
                    if opp_val == self:
                        setattr(item, "workbench101_Thing", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "workbench101_Thing"):
                    opp_val = getattr(item, "workbench101_Thing", None)
                    
                    setattr(item, "workbench101_Thing", self)
                    

class NamedElement:

    pass
class workbench101_RelatedTo(NamedElement):

    def __init__(self, since: str, RelatedTo: "workbench101_Thing" = None, workbench101_RelatedTo: "workbench101_Thing" = None, relations: "workbench101_Thing" = None):
        self.since = since
        self.RelatedTo = RelatedTo
        self.workbench101_RelatedTo = workbench101_RelatedTo
        self.relations = relations
        
    @property
    def since(self) -> str:
        return self.__since

    @since.setter
    def since(self, since: str):
        self.__since = since

    @property
    def workbench101_RelatedTo(self):
        return self.__workbench101_RelatedTo

    @workbench101_RelatedTo.setter
    def workbench101_RelatedTo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workbench101_RelatedTo__workbench101_RelatedTo", None)
        self.__workbench101_RelatedTo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "workbench101_Thing6"):
                opp_val = getattr(old_value, "workbench101_Thing6", None)
                if opp_val == self:
                    setattr(old_value, "workbench101_Thing6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "workbench101_Thing6"):
                opp_val = getattr(value, "workbench101_Thing6", None)
                setattr(value, "workbench101_Thing6", self)

    @property
    def relations(self):
        return self.__relations

    @relations.setter
    def relations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workbench101_RelatedTo__relations", None)
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
    def RelatedTo(self):
        return self.__RelatedTo

    @RelatedTo.setter
    def RelatedTo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workbench101_RelatedTo__RelatedTo", None)
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

class workbench101_Thoughts(NamedElement):

    pass
class workbench101_Thing(NamedElement):

    def __init__(self, id: int, workbench101_Thing: "workbench101_Workbench" = None, workbench101_Thing6: "workbench101_RelatedTo" = None, workbench101_Thing9: "workbench101_Thoughts" = None, fromThing: set["workbench101_RelatedTo"] = None, Thing: "workbench101_RelatedTo" = None):
        self.id = id
        self.workbench101_Thing = workbench101_Thing
        self.workbench101_Thing6 = workbench101_Thing6
        self.workbench101_Thing9 = workbench101_Thing9
        self.fromThing = fromThing if fromThing is not None else set()
        self.Thing = Thing
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def workbench101_Thing6(self):
        return self.__workbench101_Thing6

    @workbench101_Thing6.setter
    def workbench101_Thing6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workbench101_Thing__workbench101_Thing6", None)
        self.__workbench101_Thing6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "workbench101_RelatedTo"):
                opp_val = getattr(old_value, "workbench101_RelatedTo", None)
                if opp_val == self:
                    setattr(old_value, "workbench101_RelatedTo", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "workbench101_RelatedTo"):
                opp_val = getattr(value, "workbench101_RelatedTo", None)
                setattr(value, "workbench101_RelatedTo", self)

    @property
    def fromThing(self):
        return self.__fromThing

    @fromThing.setter
    def fromThing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workbench101_Thing__fromThing", None)
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
    def workbench101_Thing9(self):
        return self.__workbench101_Thing9

    @workbench101_Thing9.setter
    def workbench101_Thing9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workbench101_Thing__workbench101_Thing9", None)
        self.__workbench101_Thing9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "workbench101_Thoughts8"):
                opp_val = getattr(old_value, "workbench101_Thoughts8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "workbench101_Thoughts8"):
                opp_val = getattr(value, "workbench101_Thoughts8", None)
                if opp_val is None:
                    setattr(value, "workbench101_Thoughts8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def workbench101_Thing(self):
        return self.__workbench101_Thing

    @workbench101_Thing.setter
    def workbench101_Thing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workbench101_Thing__workbench101_Thing", None)
        self.__workbench101_Thing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "workbench101_Workbench"):
                opp_val = getattr(old_value, "workbench101_Workbench", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "workbench101_Workbench"):
                opp_val = getattr(value, "workbench101_Workbench", None)
                if opp_val is None:
                    setattr(value, "workbench101_Workbench", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Thing(self):
        return self.__Thing

    @Thing.setter
    def Thing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workbench101_Thing__Thing", None)
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
