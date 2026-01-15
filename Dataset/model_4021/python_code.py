from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Visibility(Enum):
    protected = "protected"
    package = "package"
    public = "public"
    private = "private"


############################################
# Definition of Classes
############################################

class Classifier:

    pass
class classmm_DataType(Classifier):

    pass
class NamedElt:

    pass
class classmm_Parameter(NamedElt):

    pass
class classmm_Classifier(NamedElt):

    pass
class classmm_NamedElt:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class classmm_Method(NamedElt):

    pass
class classmm_Package(NamedElt):

    pass
class classmm_Attribute(NamedElt):

    def __init__(self, multivalued: bool, visibility: str, Attribute: "classmm_Class" = None, classmm_Attribute: "classmm_Classifier" = None, att: "classmm_Class" = None):
        self.multivalued = multivalued
        self.visibility = visibility
        self.Attribute = Attribute
        self.classmm_Attribute = classmm_Attribute
        self.att = att
        
    @property
    def multivalued(self) -> bool:
        return self.__multivalued

    @multivalued.setter
    def multivalued(self, multivalued: bool):
        self.__multivalued = multivalued

    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def classmm_Attribute(self):
        return self.__classmm_Attribute

    @classmm_Attribute.setter
    def classmm_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classmm_Attribute__classmm_Attribute", None)
        self.__classmm_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classmm_Classifier"):
                opp_val = getattr(old_value, "classmm_Classifier", None)
                if opp_val == self:
                    setattr(old_value, "classmm_Classifier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classmm_Classifier"):
                opp_val = getattr(value, "classmm_Classifier", None)
                setattr(value, "classmm_Classifier", self)

    @property
    def att(self):
        return self.__att

    @att.setter
    def att(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classmm_Attribute__att", None)
        self.__att = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Class"):
                opp_val = getattr(old_value, "Class", None)
                if opp_val == self:
                    setattr(old_value, "Class", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Class"):
                opp_val = getattr(value, "Class", None)
                setattr(value, "Class", self)

    @property
    def Attribute(self):
        return self.__Attribute

    @Attribute.setter
    def Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classmm_Attribute__Attribute", None)
        self.__Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owner"):
                opp_val = getattr(old_value, "owner", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owner"):
                opp_val = getattr(value, "owner", None)
                if opp_val is None:
                    setattr(value, "owner", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class classmm_Class(Classifier):

    def __init__(self, isAbstract: bool, visibility: str, owner: set["classmm_Attribute"] = None, classmm_Class: "classmm_Class" = None, classmm_Class1: set["classmm_Class"] = None, classes: "classmm_Package" = None, owner5: set["classmm_Method"] = None, Class: "classmm_Attribute" = None, Class9: "classmm_Package" = None, Class11: "classmm_Method" = None):
        self.isAbstract = isAbstract
        self.visibility = visibility
        self.owner = owner if owner is not None else set()
        self.classmm_Class = classmm_Class
        self.classmm_Class1 = classmm_Class1 if classmm_Class1 is not None else set()
        self.classes = classes
        self.owner5 = owner5 if owner5 is not None else set()
        self.Class = Class
        self.Class9 = Class9
        self.Class11 = Class11
        
    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def isAbstract(self) -> bool:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: bool):
        self.__isAbstract = isAbstract

    @property
    def owner5(self):
        return self.__owner5

    @owner5.setter
    def owner5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classmm_Class__owner5", None)
        self.__owner5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Method"):
                    opp_val = getattr(item, "Method", None)
                    
                    if opp_val == self:
                        setattr(item, "Method", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Method"):
                    opp_val = getattr(item, "Method", None)
                    
                    setattr(item, "Method", self)
                    

    @property
    def Class9(self):
        return self.__Class9

    @Class9.setter
    def Class9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classmm_Class__Class9", None)
        self.__Class9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "package"):
                opp_val = getattr(old_value, "package", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "package"):
                opp_val = getattr(value, "package", None)
                if opp_val is None:
                    setattr(value, "package", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classmm_Class__owner", None)
        self.__owner = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Attribute"):
                    opp_val = getattr(item, "Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Attribute"):
                    opp_val = getattr(item, "Attribute", None)
                    
                    setattr(item, "Attribute", self)
                    

    @property
    def Class(self):
        return self.__Class

    @Class.setter
    def Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classmm_Class__Class", None)
        self.__Class = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "att"):
                opp_val = getattr(old_value, "att", None)
                if opp_val == self:
                    setattr(old_value, "att", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "att"):
                opp_val = getattr(value, "att", None)
                setattr(value, "att", self)

    @property
    def classmm_Class(self):
        return self.__classmm_Class

    @classmm_Class.setter
    def classmm_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classmm_Class__classmm_Class", None)
        self.__classmm_Class = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classmm_Class1"):
                opp_val = getattr(old_value, "classmm_Class1", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classmm_Class1"):
                opp_val = getattr(value, "classmm_Class1", None)
                if opp_val is None:
                    setattr(value, "classmm_Class1", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def classes(self):
        return self.__classes

    @classes.setter
    def classes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classmm_Class__classes", None)
        self.__classes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Package"):
                opp_val = getattr(old_value, "Package", None)
                if opp_val == self:
                    setattr(old_value, "Package", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Package"):
                opp_val = getattr(value, "Package", None)
                setattr(value, "Package", self)

    @property
    def classmm_Class1(self):
        return self.__classmm_Class1

    @classmm_Class1.setter
    def classmm_Class1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classmm_Class__classmm_Class1", None)
        self.__classmm_Class1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "classmm_Class"):
                    opp_val = getattr(item, "classmm_Class", None)
                    
                    if opp_val == self:
                        setattr(item, "classmm_Class", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "classmm_Class"):
                    opp_val = getattr(item, "classmm_Class", None)
                    
                    setattr(item, "classmm_Class", self)
                    

    @property
    def Class11(self):
        return self.__Class11

    @Class11.setter
    def Class11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classmm_Class__Class11", None)
        self.__Class11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "methods"):
                opp_val = getattr(old_value, "methods", None)
                if opp_val == self:
                    setattr(old_value, "methods", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "methods"):
                opp_val = getattr(value, "methods", None)
                setattr(value, "methods", self)
