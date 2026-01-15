from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class NamedElement:

    pass
class mpupkb_Own(NamedElement):

    def __init__(self, since: str, ownerName: str, Own: "mpupkb_Thing" = None, mpupkb_Own: "mpupkb_Thing" = None, ownership: "mpupkb_Thing" = None):
        self.since = since
        self.ownerName = ownerName
        self.Own = Own
        self.mpupkb_Own = mpupkb_Own
        self.ownership = ownership
        
    @property
    def ownerName(self) -> str:
        return self.__ownerName

    @ownerName.setter
    def ownerName(self, ownerName: str):
        self.__ownerName = ownerName

    @property
    def since(self) -> str:
        return self.__since

    @since.setter
    def since(self, since: str):
        self.__since = since

    @property
    def ownership(self):
        return self.__ownership

    @ownership.setter
    def ownership(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mpupkb_Own__ownership", None)
        self.__ownership = value
        
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
    def mpupkb_Own(self):
        return self.__mpupkb_Own

    @mpupkb_Own.setter
    def mpupkb_Own(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mpupkb_Own__mpupkb_Own", None)
        self.__mpupkb_Own = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mpupkb_Thing"):
                opp_val = getattr(old_value, "mpupkb_Thing", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mpupkb_Thing"):
                opp_val = getattr(value, "mpupkb_Thing", None)
                if opp_val is None:
                    setattr(value, "mpupkb_Thing", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Own(self):
        return self.__Own

    @Own.setter
    def Own(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mpupkb_Own__Own", None)
        self.__Own = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thing"):
                opp_val = getattr(old_value, "thing", None)
                if opp_val == self:
                    setattr(old_value, "thing", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thing"):
                opp_val = getattr(value, "thing", None)
                setattr(value, "thing", self)

class mpupkb_Thing(NamedElement):

    def __init__(self, id: int, thing: "mpupkb_Own" = None, mpupkb_Thing: set["mpupkb_Own"] = None, Thing: "mpupkb_Own" = None):
        self.id = id
        self.thing = thing
        self.mpupkb_Thing = mpupkb_Thing if mpupkb_Thing is not None else set()
        self.Thing = Thing
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def thing(self):
        return self.__thing

    @thing.setter
    def thing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mpupkb_Thing__thing", None)
        self.__thing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Own"):
                opp_val = getattr(old_value, "Own", None)
                if opp_val == self:
                    setattr(old_value, "Own", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Own"):
                opp_val = getattr(value, "Own", None)
                setattr(value, "Own", self)

    @property
    def Thing(self):
        return self.__Thing

    @Thing.setter
    def Thing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mpupkb_Thing__Thing", None)
        self.__Thing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownership"):
                opp_val = getattr(old_value, "ownership", None)
                if opp_val == self:
                    setattr(old_value, "ownership", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownership"):
                opp_val = getattr(value, "ownership", None)
                setattr(value, "ownership", self)

    @property
    def mpupkb_Thing(self):
        return self.__mpupkb_Thing

    @mpupkb_Thing.setter
    def mpupkb_Thing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mpupkb_Thing__mpupkb_Thing", None)
        self.__mpupkb_Thing = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mpupkb_Own"):
                    opp_val = getattr(item, "mpupkb_Own", None)
                    
                    if opp_val == self:
                        setattr(item, "mpupkb_Own", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mpupkb_Own"):
                    opp_val = getattr(item, "mpupkb_Own", None)
                    
                    setattr(item, "mpupkb_Own", self)
                    

class mpupkb_Comment:

    def __init__(self, content: str, mpupkb_Comment: "mpupkb_NamedElement" = None):
        self.content = content
        self.mpupkb_Comment = mpupkb_Comment
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def mpupkb_Comment(self):
        return self.__mpupkb_Comment

    @mpupkb_Comment.setter
    def mpupkb_Comment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mpupkb_Comment__mpupkb_Comment", None)
        self.__mpupkb_Comment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mpupkb_NamedElement"):
                opp_val = getattr(old_value, "mpupkb_NamedElement", None)
                if opp_val == self:
                    setattr(old_value, "mpupkb_NamedElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mpupkb_NamedElement"):
                opp_val = getattr(value, "mpupkb_NamedElement", None)
                setattr(value, "mpupkb_NamedElement", self)

class mpupkb_NamedElement(ABC):

    def __init__(self, name: str, mpupkb_NamedElement: "mpupkb_Comment" = None):
        self.name = name
        self.mpupkb_NamedElement = mpupkb_NamedElement
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mpupkb_NamedElement(self):
        return self.__mpupkb_NamedElement

    @mpupkb_NamedElement.setter
    def mpupkb_NamedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mpupkb_NamedElement__mpupkb_NamedElement", None)
        self.__mpupkb_NamedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mpupkb_Comment"):
                opp_val = getattr(old_value, "mpupkb_Comment", None)
                if opp_val == self:
                    setattr(old_value, "mpupkb_Comment", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mpupkb_Comment"):
                opp_val = getattr(value, "mpupkb_Comment", None)
                setattr(value, "mpupkb_Comment", self)
