from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class World:

    pass
class testcompat103_EClass3(World):

    pass
class EClass0:

    pass
class testcompat103_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class NamedElement:

    pass
class testcompat103_EClass1(NamedElement):

    pass
class testcompat103_RelatedTo(NamedElement):

    def __init__(self, since: str, relations: "testcompat103_Thing" = None, testcompat103_RelatedTo: "testcompat103_Thing" = None, RelatedTo: "testcompat103_Thing" = None):
        self.since = since
        self.relations = relations
        self.testcompat103_RelatedTo = testcompat103_RelatedTo
        self.RelatedTo = RelatedTo
        
    @property
    def since(self) -> str:
        return self.__since

    @since.setter
    def since(self, since: str):
        self.__since = since

    @property
    def relations(self):
        return self.__relations

    @relations.setter
    def relations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testcompat103_RelatedTo__relations", None)
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
        old_value = getattr(self, f"_testcompat103_RelatedTo__RelatedTo", None)
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
    def testcompat103_RelatedTo(self):
        return self.__testcompat103_RelatedTo

    @testcompat103_RelatedTo.setter
    def testcompat103_RelatedTo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testcompat103_RelatedTo__testcompat103_RelatedTo", None)
        self.__testcompat103_RelatedTo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "testcompat103_Thing10"):
                opp_val = getattr(old_value, "testcompat103_Thing10", None)
                if opp_val == self:
                    setattr(old_value, "testcompat103_Thing10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "testcompat103_Thing10"):
                opp_val = getattr(value, "testcompat103_Thing10", None)
                setattr(value, "testcompat103_Thing10", self)

class testcompat103_World(NamedElement):

    pass
class testcompat103_EClass2(EClass0):

    pass
class testcompat103_EClass0(NamedElement):

    pass
class testcompat103_Foo(NamedElement):

    pass
class testcompat103_Thing(NamedElement):

    def __init__(self, id: int, testcompat103_Thing: "testcompat103_World" = None, Thing: "testcompat103_RelatedTo" = None, testcompat103_Thing10: "testcompat103_RelatedTo" = None, fromThing: set["testcompat103_RelatedTo"] = None):
        self.id = id
        self.testcompat103_Thing = testcompat103_Thing
        self.Thing = Thing
        self.testcompat103_Thing10 = testcompat103_Thing10
        self.fromThing = fromThing if fromThing is not None else set()
        
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
        old_value = getattr(self, f"_testcompat103_Thing__Thing", None)
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
    def testcompat103_Thing10(self):
        return self.__testcompat103_Thing10

    @testcompat103_Thing10.setter
    def testcompat103_Thing10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testcompat103_Thing__testcompat103_Thing10", None)
        self.__testcompat103_Thing10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "testcompat103_RelatedTo"):
                opp_val = getattr(old_value, "testcompat103_RelatedTo", None)
                if opp_val == self:
                    setattr(old_value, "testcompat103_RelatedTo", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "testcompat103_RelatedTo"):
                opp_val = getattr(value, "testcompat103_RelatedTo", None)
                setattr(value, "testcompat103_RelatedTo", self)

    @property
    def fromThing(self):
        return self.__fromThing

    @fromThing.setter
    def fromThing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testcompat103_Thing__fromThing", None)
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
    def testcompat103_Thing(self):
        return self.__testcompat103_Thing

    @testcompat103_Thing.setter
    def testcompat103_Thing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testcompat103_Thing__testcompat103_Thing", None)
        self.__testcompat103_Thing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "testcompat103_World"):
                opp_val = getattr(old_value, "testcompat103_World", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "testcompat103_World"):
                opp_val = getattr(value, "testcompat103_World", None)
                if opp_val is None:
                    setattr(value, "testcompat103_World", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
