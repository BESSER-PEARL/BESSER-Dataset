from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Visibility(Enum):
    private = "private"
    public = "public"


############################################
# Definition of Classes
############################################

class Class:

    pass
class tallerE1Java_DAOClass(Class):

    pass
class tallerE1Java_TestClass(Class):

    pass
class tallerE1Java_EntityClass(Class):

    pass
class tallerE1Java_Annotation:

    def __init__(self, type: str, content: str, tallerE1Java_Annotation: "tallerE1Java_Attribute" = None):
        self.type = type
        self.content = content
        self.tallerE1Java_Annotation = tallerE1Java_Annotation
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def tallerE1Java_Annotation(self):
        return self.__tallerE1Java_Annotation

    @tallerE1Java_Annotation.setter
    def tallerE1Java_Annotation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tallerE1Java_Annotation__tallerE1Java_Annotation", None)
        self.__tallerE1Java_Annotation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tallerE1Java_Attribute12"):
                opp_val = getattr(old_value, "tallerE1Java_Attribute12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tallerE1Java_Attribute12"):
                opp_val = getattr(value, "tallerE1Java_Attribute12", None)
                if opp_val is None:
                    setattr(value, "tallerE1Java_Attribute12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class tallerE1Java_Type(ABC):

    def __init__(self, name: str, tallerE1Java_Type: "tallerE1Java_Attribute" = None, tallerE1Java_Type15: "tallerE1Java_Container" = None):
        self.name = name
        self.tallerE1Java_Type = tallerE1Java_Type
        self.tallerE1Java_Type15 = tallerE1Java_Type15
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def tallerE1Java_Type15(self):
        return self.__tallerE1Java_Type15

    @tallerE1Java_Type15.setter
    def tallerE1Java_Type15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tallerE1Java_Type__tallerE1Java_Type15", None)
        self.__tallerE1Java_Type15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tallerE1Java_Container14"):
                opp_val = getattr(old_value, "tallerE1Java_Container14", None)
                if opp_val == self:
                    setattr(old_value, "tallerE1Java_Container14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tallerE1Java_Container14"):
                opp_val = getattr(value, "tallerE1Java_Container14", None)
                setattr(value, "tallerE1Java_Container14", self)

    @property
    def tallerE1Java_Type(self):
        return self.__tallerE1Java_Type

    @tallerE1Java_Type.setter
    def tallerE1Java_Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tallerE1Java_Type__tallerE1Java_Type", None)
        self.__tallerE1Java_Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tallerE1Java_Attribute10"):
                opp_val = getattr(old_value, "tallerE1Java_Attribute10", None)
                if opp_val == self:
                    setattr(old_value, "tallerE1Java_Attribute10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tallerE1Java_Attribute10"):
                opp_val = getattr(value, "tallerE1Java_Attribute10", None)
                setattr(value, "tallerE1Java_Attribute10", self)

class tallerE1Java_Attribute:

    def __init__(self, name: str, visibility: str, tallerE1Java_Attribute: "tallerE1Java_Class" = None, tallerE1Java_Attribute10: "tallerE1Java_Type" = None, tallerE1Java_Attribute12: set["tallerE1Java_Annotation"] = None):
        self.name = name
        self.visibility = visibility
        self.tallerE1Java_Attribute = tallerE1Java_Attribute
        self.tallerE1Java_Attribute10 = tallerE1Java_Attribute10
        self.tallerE1Java_Attribute12 = tallerE1Java_Attribute12 if tallerE1Java_Attribute12 is not None else set()
        
    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def tallerE1Java_Attribute10(self):
        return self.__tallerE1Java_Attribute10

    @tallerE1Java_Attribute10.setter
    def tallerE1Java_Attribute10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tallerE1Java_Attribute__tallerE1Java_Attribute10", None)
        self.__tallerE1Java_Attribute10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tallerE1Java_Type"):
                opp_val = getattr(old_value, "tallerE1Java_Type", None)
                if opp_val == self:
                    setattr(old_value, "tallerE1Java_Type", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tallerE1Java_Type"):
                opp_val = getattr(value, "tallerE1Java_Type", None)
                setattr(value, "tallerE1Java_Type", self)

    @property
    def tallerE1Java_Attribute12(self):
        return self.__tallerE1Java_Attribute12

    @tallerE1Java_Attribute12.setter
    def tallerE1Java_Attribute12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tallerE1Java_Attribute__tallerE1Java_Attribute12", None)
        self.__tallerE1Java_Attribute12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tallerE1Java_Annotation"):
                    opp_val = getattr(item, "tallerE1Java_Annotation", None)
                    
                    if opp_val == self:
                        setattr(item, "tallerE1Java_Annotation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tallerE1Java_Annotation"):
                    opp_val = getattr(item, "tallerE1Java_Annotation", None)
                    
                    setattr(item, "tallerE1Java_Annotation", self)
                    

    @property
    def tallerE1Java_Attribute(self):
        return self.__tallerE1Java_Attribute

    @tallerE1Java_Attribute.setter
    def tallerE1Java_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tallerE1Java_Attribute__tallerE1Java_Attribute", None)
        self.__tallerE1Java_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tallerE1Java_Class8"):
                opp_val = getattr(old_value, "tallerE1Java_Class8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tallerE1Java_Class8"):
                opp_val = getattr(value, "tallerE1Java_Class8", None)
                if opp_val is None:
                    setattr(value, "tallerE1Java_Class8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Type:

    pass
class tallerE1Java_Class(Type):

    pass
class tallerE1Java_Container(Type):

    def __init__(self, type: str, tallerE1Java_Container: "tallerE1Java_Program" = None, tallerE1Java_Container14: "tallerE1Java_Type" = None):
        self.type = type
        self.tallerE1Java_Container = tallerE1Java_Container
        self.tallerE1Java_Container14 = tallerE1Java_Container14
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def tallerE1Java_Container(self):
        return self.__tallerE1Java_Container

    @tallerE1Java_Container.setter
    def tallerE1Java_Container(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tallerE1Java_Container__tallerE1Java_Container", None)
        self.__tallerE1Java_Container = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tallerE1Java_Program4"):
                opp_val = getattr(old_value, "tallerE1Java_Program4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tallerE1Java_Program4"):
                opp_val = getattr(value, "tallerE1Java_Program4", None)
                if opp_val is None:
                    setattr(value, "tallerE1Java_Program4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tallerE1Java_Container14(self):
        return self.__tallerE1Java_Container14

    @tallerE1Java_Container14.setter
    def tallerE1Java_Container14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tallerE1Java_Container__tallerE1Java_Container14", None)
        self.__tallerE1Java_Container14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tallerE1Java_Type15"):
                opp_val = getattr(old_value, "tallerE1Java_Type15", None)
                if opp_val == self:
                    setattr(old_value, "tallerE1Java_Type15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tallerE1Java_Type15"):
                opp_val = getattr(value, "tallerE1Java_Type15", None)
                setattr(value, "tallerE1Java_Type15", self)

class tallerE1Java_PrimitiveType(Type):

    pass
class tallerE1Java_Package:

    def __init__(self, name: str, tallerE1Java_Package: "tallerE1Java_Program" = None, tallerE1Java_Package6: set["tallerE1Java_Class"] = None):
        self.name = name
        self.tallerE1Java_Package = tallerE1Java_Package
        self.tallerE1Java_Package6 = tallerE1Java_Package6 if tallerE1Java_Package6 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def tallerE1Java_Package6(self):
        return self.__tallerE1Java_Package6

    @tallerE1Java_Package6.setter
    def tallerE1Java_Package6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tallerE1Java_Package__tallerE1Java_Package6", None)
        self.__tallerE1Java_Package6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tallerE1Java_Class"):
                    opp_val = getattr(item, "tallerE1Java_Class", None)
                    
                    if opp_val == self:
                        setattr(item, "tallerE1Java_Class", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tallerE1Java_Class"):
                    opp_val = getattr(item, "tallerE1Java_Class", None)
                    
                    setattr(item, "tallerE1Java_Class", self)
                    

    @property
    def tallerE1Java_Package(self):
        return self.__tallerE1Java_Package

    @tallerE1Java_Package.setter
    def tallerE1Java_Package(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tallerE1Java_Package__tallerE1Java_Package", None)
        self.__tallerE1Java_Package = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tallerE1Java_Program"):
                opp_val = getattr(old_value, "tallerE1Java_Program", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tallerE1Java_Program"):
                opp_val = getattr(value, "tallerE1Java_Program", None)
                if opp_val is None:
                    setattr(value, "tallerE1Java_Program", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class tallerE1Java_Program:

    pass