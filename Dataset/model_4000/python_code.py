from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Type(Enum):
    integer = "integer"
    float = "float"
    string = "string"
    datetime = "datetime"
    bool = "bool"


############################################
# Definition of Classes
############################################

class classes_Reference:

    def __init__(self, name: str, references: "classes_Class" = None, classes_Reference: "classes_Class" = None, Reference: "classes_Class" = None):
        self.name = name
        self.references = references
        self.classes_Reference = classes_Reference
        self.Reference = Reference
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Reference(self):
        return self.__Reference

    @Reference.setter
    def Reference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_Reference__Reference", None)
        self.__Reference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cls3"):
                opp_val = getattr(old_value, "cls3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cls3"):
                opp_val = getattr(value, "cls3", None)
                if opp_val is None:
                    setattr(value, "cls3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def references(self):
        return self.__references

    @references.setter
    def references(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_Reference__references", None)
        self.__references = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Class9"):
                opp_val = getattr(old_value, "Class9", None)
                if opp_val == self:
                    setattr(old_value, "Class9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Class9"):
                opp_val = getattr(value, "Class9", None)
                setattr(value, "Class9", self)

    @property
    def classes_Reference(self):
        return self.__classes_Reference

    @classes_Reference.setter
    def classes_Reference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_Reference__classes_Reference", None)
        self.__classes_Reference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classes_Class11"):
                opp_val = getattr(old_value, "classes_Class11", None)
                if opp_val == self:
                    setattr(old_value, "classes_Class11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classes_Class11"):
                opp_val = getattr(value, "classes_Class11", None)
                setattr(value, "classes_Class11", self)

class classes_Attribute:

    def __init__(self, name: str, type: str, Attribute: "classes_Class" = None, classes_Attribute: "classes_Class" = None, attributes: "classes_Class" = None):
        self.name = name
        self.type = type
        self.Attribute = Attribute
        self.classes_Attribute = classes_Attribute
        self.attributes = attributes
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def attributes(self):
        return self.__attributes

    @attributes.setter
    def attributes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_Attribute__attributes", None)
        self.__attributes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Class7"):
                opp_val = getattr(old_value, "Class7", None)
                if opp_val == self:
                    setattr(old_value, "Class7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Class7"):
                opp_val = getattr(value, "Class7", None)
                setattr(value, "Class7", self)

    @property
    def Attribute(self):
        return self.__Attribute

    @Attribute.setter
    def Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_Attribute__Attribute", None)
        self.__Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cls"):
                opp_val = getattr(old_value, "cls", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cls"):
                opp_val = getattr(value, "cls", None)
                if opp_val is None:
                    setattr(value, "cls", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def classes_Attribute(self):
        return self.__classes_Attribute

    @classes_Attribute.setter
    def classes_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_Attribute__classes_Attribute", None)
        self.__classes_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classes_Class"):
                opp_val = getattr(old_value, "classes_Class", None)
                if opp_val == self:
                    setattr(old_value, "classes_Class", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classes_Class"):
                opp_val = getattr(value, "classes_Class", None)
                setattr(value, "classes_Class", self)

class classes_Class:

    def __init__(self, name: str, Class: "classes_ClassDiagram" = None, cls: set["classes_Attribute"] = None, classes_Class: "classes_Attribute" = None, Class7: "classes_Attribute" = None, Class9: "classes_Reference" = None, classes_Class11: "classes_Reference" = None, cls3: set["classes_Reference"] = None, classes: "classes_ClassDiagram" = None):
        self.name = name
        self.Class = Class
        self.cls = cls if cls is not None else set()
        self.classes_Class = classes_Class
        self.Class7 = Class7
        self.Class9 = Class9
        self.classes_Class11 = classes_Class11
        self.cls3 = cls3 if cls3 is not None else set()
        self.classes = classes
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def cls3(self):
        return self.__cls3

    @cls3.setter
    def cls3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_Class__cls3", None)
        self.__cls3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Reference"):
                    opp_val = getattr(item, "Reference", None)
                    
                    if opp_val == self:
                        setattr(item, "Reference", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Reference"):
                    opp_val = getattr(item, "Reference", None)
                    
                    setattr(item, "Reference", self)
                    

    @property
    def classes(self):
        return self.__classes

    @classes.setter
    def classes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_Class__classes", None)
        self.__classes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassDiagram"):
                opp_val = getattr(old_value, "ClassDiagram", None)
                if opp_val == self:
                    setattr(old_value, "ClassDiagram", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassDiagram"):
                opp_val = getattr(value, "ClassDiagram", None)
                setattr(value, "ClassDiagram", self)

    @property
    def Class9(self):
        return self.__Class9

    @Class9.setter
    def Class9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_Class__Class9", None)
        self.__Class9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "references"):
                opp_val = getattr(old_value, "references", None)
                if opp_val == self:
                    setattr(old_value, "references", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "references"):
                opp_val = getattr(value, "references", None)
                setattr(value, "references", self)

    @property
    def Class(self):
        return self.__Class

    @Class.setter
    def Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_Class__Class", None)
        self.__Class = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diagram"):
                opp_val = getattr(old_value, "diagram", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagram"):
                opp_val = getattr(value, "diagram", None)
                if opp_val is None:
                    setattr(value, "diagram", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def classes_Class11(self):
        return self.__classes_Class11

    @classes_Class11.setter
    def classes_Class11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_Class__classes_Class11", None)
        self.__classes_Class11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classes_Reference"):
                opp_val = getattr(old_value, "classes_Reference", None)
                if opp_val == self:
                    setattr(old_value, "classes_Reference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classes_Reference"):
                opp_val = getattr(value, "classes_Reference", None)
                setattr(value, "classes_Reference", self)

    @property
    def classes_Class(self):
        return self.__classes_Class

    @classes_Class.setter
    def classes_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_Class__classes_Class", None)
        self.__classes_Class = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classes_Attribute"):
                opp_val = getattr(old_value, "classes_Attribute", None)
                if opp_val == self:
                    setattr(old_value, "classes_Attribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classes_Attribute"):
                opp_val = getattr(value, "classes_Attribute", None)
                setattr(value, "classes_Attribute", self)

    @property
    def cls(self):
        return self.__cls

    @cls.setter
    def cls(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_Class__cls", None)
        self.__cls = value if value is not None else set()
        
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
    def Class7(self):
        return self.__Class7

    @Class7.setter
    def Class7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_Class__Class7", None)
        self.__Class7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "attributes"):
                opp_val = getattr(old_value, "attributes", None)
                if opp_val == self:
                    setattr(old_value, "attributes", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "attributes"):
                opp_val = getattr(value, "attributes", None)
                setattr(value, "attributes", self)

class classes_ClassDiagram:

    def __init__(self, name: str, diagram: set["classes_Class"] = None, ClassDiagram: "classes_Class" = None):
        self.name = name
        self.diagram = diagram if diagram is not None else set()
        self.ClassDiagram = ClassDiagram
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def diagram(self):
        return self.__diagram

    @diagram.setter
    def diagram(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_ClassDiagram__diagram", None)
        self.__diagram = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Class"):
                    opp_val = getattr(item, "Class", None)
                    
                    if opp_val == self:
                        setattr(item, "Class", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Class"):
                    opp_val = getattr(item, "Class", None)
                    
                    setattr(item, "Class", self)
                    

    @property
    def ClassDiagram(self):
        return self.__ClassDiagram

    @ClassDiagram.setter
    def ClassDiagram(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_ClassDiagram__ClassDiagram", None)
        self.__ClassDiagram = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classes"):
                opp_val = getattr(old_value, "classes", None)
                if opp_val == self:
                    setattr(old_value, "classes", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classes"):
                opp_val = getattr(value, "classes", None)
                setattr(value, "classes", self)
