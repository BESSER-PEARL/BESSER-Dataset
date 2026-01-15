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
class JavaMM_TestClass(Class):

    pass
class JavaMM_DAOClass(Class):

    pass
class JavaMM_EntityClass(Class):

    pass
class JavaMM_Annotation:

    def __init__(self, type: str, content: str, JavaMM_Annotation: "JavaMM_Attribute" = None):
        self.type = type
        self.content = content
        self.JavaMM_Annotation = JavaMM_Annotation
        
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
    def JavaMM_Annotation(self):
        return self.__JavaMM_Annotation

    @JavaMM_Annotation.setter
    def JavaMM_Annotation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JavaMM_Annotation__JavaMM_Annotation", None)
        self.__JavaMM_Annotation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JavaMM_Attribute12"):
                opp_val = getattr(old_value, "JavaMM_Attribute12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JavaMM_Attribute12"):
                opp_val = getattr(value, "JavaMM_Attribute12", None)
                if opp_val is None:
                    setattr(value, "JavaMM_Attribute12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class JavaMM_Type(ABC):

    def __init__(self, name: str, JavaMM_Type: "JavaMM_Attribute" = None, JavaMM_Type15: "JavaMM_Container" = None):
        self.name = name
        self.JavaMM_Type = JavaMM_Type
        self.JavaMM_Type15 = JavaMM_Type15
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def JavaMM_Type(self):
        return self.__JavaMM_Type

    @JavaMM_Type.setter
    def JavaMM_Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JavaMM_Type__JavaMM_Type", None)
        self.__JavaMM_Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JavaMM_Attribute10"):
                opp_val = getattr(old_value, "JavaMM_Attribute10", None)
                if opp_val == self:
                    setattr(old_value, "JavaMM_Attribute10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JavaMM_Attribute10"):
                opp_val = getattr(value, "JavaMM_Attribute10", None)
                setattr(value, "JavaMM_Attribute10", self)

    @property
    def JavaMM_Type15(self):
        return self.__JavaMM_Type15

    @JavaMM_Type15.setter
    def JavaMM_Type15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JavaMM_Type__JavaMM_Type15", None)
        self.__JavaMM_Type15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JavaMM_Container14"):
                opp_val = getattr(old_value, "JavaMM_Container14", None)
                if opp_val == self:
                    setattr(old_value, "JavaMM_Container14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JavaMM_Container14"):
                opp_val = getattr(value, "JavaMM_Container14", None)
                setattr(value, "JavaMM_Container14", self)

class JavaMM_Attribute:

    def __init__(self, name: str, visibility: str, JavaMM_Attribute: "JavaMM_Class" = None, JavaMM_Attribute10: "JavaMM_Type" = None, JavaMM_Attribute12: set["JavaMM_Annotation"] = None):
        self.name = name
        self.visibility = visibility
        self.JavaMM_Attribute = JavaMM_Attribute
        self.JavaMM_Attribute10 = JavaMM_Attribute10
        self.JavaMM_Attribute12 = JavaMM_Attribute12 if JavaMM_Attribute12 is not None else set()
        
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
    def JavaMM_Attribute12(self):
        return self.__JavaMM_Attribute12

    @JavaMM_Attribute12.setter
    def JavaMM_Attribute12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JavaMM_Attribute__JavaMM_Attribute12", None)
        self.__JavaMM_Attribute12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "JavaMM_Annotation"):
                    opp_val = getattr(item, "JavaMM_Annotation", None)
                    
                    if opp_val == self:
                        setattr(item, "JavaMM_Annotation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "JavaMM_Annotation"):
                    opp_val = getattr(item, "JavaMM_Annotation", None)
                    
                    setattr(item, "JavaMM_Annotation", self)
                    

    @property
    def JavaMM_Attribute(self):
        return self.__JavaMM_Attribute

    @JavaMM_Attribute.setter
    def JavaMM_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JavaMM_Attribute__JavaMM_Attribute", None)
        self.__JavaMM_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JavaMM_Class8"):
                opp_val = getattr(old_value, "JavaMM_Class8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JavaMM_Class8"):
                opp_val = getattr(value, "JavaMM_Class8", None)
                if opp_val is None:
                    setattr(value, "JavaMM_Class8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def JavaMM_Attribute10(self):
        return self.__JavaMM_Attribute10

    @JavaMM_Attribute10.setter
    def JavaMM_Attribute10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JavaMM_Attribute__JavaMM_Attribute10", None)
        self.__JavaMM_Attribute10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JavaMM_Type"):
                opp_val = getattr(old_value, "JavaMM_Type", None)
                if opp_val == self:
                    setattr(old_value, "JavaMM_Type", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JavaMM_Type"):
                opp_val = getattr(value, "JavaMM_Type", None)
                setattr(value, "JavaMM_Type", self)

class Type:

    pass
class JavaMM_Package:

    def __init__(self, name: str, JavaMM_Package6: set["JavaMM_Class"] = None, JavaMM_Package: "JavaMM_Program" = None):
        self.name = name
        self.JavaMM_Package6 = JavaMM_Package6 if JavaMM_Package6 is not None else set()
        self.JavaMM_Package = JavaMM_Package
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def JavaMM_Package(self):
        return self.__JavaMM_Package

    @JavaMM_Package.setter
    def JavaMM_Package(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JavaMM_Package__JavaMM_Package", None)
        self.__JavaMM_Package = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JavaMM_Program"):
                opp_val = getattr(old_value, "JavaMM_Program", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JavaMM_Program"):
                opp_val = getattr(value, "JavaMM_Program", None)
                if opp_val is None:
                    setattr(value, "JavaMM_Program", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def JavaMM_Package6(self):
        return self.__JavaMM_Package6

    @JavaMM_Package6.setter
    def JavaMM_Package6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JavaMM_Package__JavaMM_Package6", None)
        self.__JavaMM_Package6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "JavaMM_Class"):
                    opp_val = getattr(item, "JavaMM_Class", None)
                    
                    if opp_val == self:
                        setattr(item, "JavaMM_Class", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "JavaMM_Class"):
                    opp_val = getattr(item, "JavaMM_Class", None)
                    
                    setattr(item, "JavaMM_Class", self)
                    

class JavaMM_Program:

    pass
class JavaMM_Class(Type):

    pass
class JavaMM_Container(Type):

    def __init__(self, type: str, JavaMM_Container: "JavaMM_Program" = None, JavaMM_Container14: "JavaMM_Type" = None):
        self.type = type
        self.JavaMM_Container = JavaMM_Container
        self.JavaMM_Container14 = JavaMM_Container14
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def JavaMM_Container14(self):
        return self.__JavaMM_Container14

    @JavaMM_Container14.setter
    def JavaMM_Container14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JavaMM_Container__JavaMM_Container14", None)
        self.__JavaMM_Container14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JavaMM_Type15"):
                opp_val = getattr(old_value, "JavaMM_Type15", None)
                if opp_val == self:
                    setattr(old_value, "JavaMM_Type15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JavaMM_Type15"):
                opp_val = getattr(value, "JavaMM_Type15", None)
                setattr(value, "JavaMM_Type15", self)

    @property
    def JavaMM_Container(self):
        return self.__JavaMM_Container

    @JavaMM_Container.setter
    def JavaMM_Container(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JavaMM_Container__JavaMM_Container", None)
        self.__JavaMM_Container = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JavaMM_Program4"):
                opp_val = getattr(old_value, "JavaMM_Program4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JavaMM_Program4"):
                opp_val = getattr(value, "JavaMM_Program4", None)
                if opp_val is None:
                    setattr(value, "JavaMM_Program4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class JavaMM_PrimitiveType(Type):

    pass