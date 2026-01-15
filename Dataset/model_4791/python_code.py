from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class types_Library:

    def __init__(self, id: str, Library: "types_Type" = None, owningLibrary: set["types_Type"] = None):
        self.id = id
        self.Library = Library
        self.owningLibrary = owningLibrary if owningLibrary is not None else set()
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def Library(self):
        return self.__Library

    @Library.setter
    def Library(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_Library__Library", None)
        self.__Library = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types"):
                opp_val = getattr(old_value, "types", None)
                if opp_val == self:
                    setattr(old_value, "types", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types"):
                opp_val = getattr(value, "types", None)
                setattr(value, "types", self)

    @property
    def owningLibrary(self):
        return self.__owningLibrary

    @owningLibrary.setter
    def owningLibrary(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_Library__owningLibrary", None)
        self.__owningLibrary = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Type"):
                    opp_val = getattr(item, "Type", None)
                    
                    if opp_val == self:
                        setattr(item, "Type", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Type"):
                    opp_val = getattr(item, "Type", None)
                    
                    setattr(item, "Type", self)
                    

class types_TypedElement(ABC):

    pass
class Feature:

    pass
class types_Property(Feature):

    pass
class types_Event(Feature):

    pass
class types_Operation(Feature):

    pass
class TypedElement:

    pass
class NamedElement:

    pass
class types_Feature(TypedElement, NamedElement):

    pass
class types_Type(NamedElement):

    pass
class types_Parameter(TypedElement, NamedElement):

    pass