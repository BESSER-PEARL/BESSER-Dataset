from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class AccessModifiers(Enum):
    public = "public"
    protected = "protected"
    private = "private"
class Types(Enum):
    int = "int"
    long = "long"
    double = "double"
    float = "float"
    string = "string"
    boolean = "boolean"
    void = "void"
class Languages(Enum):
    Java = "Java"
    CS = "CS"
    Python = "Python"
    CPP = "CPP"


############################################
# Definition of Classes
############################################

class design_Relation(ABC):

    pass
class design_Classifier(ABC):

    def __init__(self, accessModifier: str, name: str, design_Classifier5: "design_Relation" = None, design_Classifier8: "design_Relation" = None, design_Classifier10: set["design_Attribute"] = None, design_Classifier12: set["design_Operation"] = None, design_Classifier: "design_Design" = None):
        self.accessModifier = accessModifier
        self.name = name
        self.design_Classifier5 = design_Classifier5
        self.design_Classifier8 = design_Classifier8
        self.design_Classifier10 = design_Classifier10 if design_Classifier10 is not None else set()
        self.design_Classifier12 = design_Classifier12 if design_Classifier12 is not None else set()
        self.design_Classifier = design_Classifier
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def accessModifier(self) -> str:
        return self.__accessModifier

    @accessModifier.setter
    def accessModifier(self, accessModifier: str):
        self.__accessModifier = accessModifier

    @property
    def design_Classifier8(self):
        return self.__design_Classifier8

    @design_Classifier8.setter
    def design_Classifier8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_design_Classifier__design_Classifier8", None)
        self.__design_Classifier8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "design_Relation7"):
                opp_val = getattr(old_value, "design_Relation7", None)
                if opp_val == self:
                    setattr(old_value, "design_Relation7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "design_Relation7"):
                opp_val = getattr(value, "design_Relation7", None)
                setattr(value, "design_Relation7", self)

    @property
    def design_Classifier10(self):
        return self.__design_Classifier10

    @design_Classifier10.setter
    def design_Classifier10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_design_Classifier__design_Classifier10", None)
        self.__design_Classifier10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "design_Attribute"):
                    opp_val = getattr(item, "design_Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "design_Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "design_Attribute"):
                    opp_val = getattr(item, "design_Attribute", None)
                    
                    setattr(item, "design_Attribute", self)
                    

    @property
    def design_Classifier5(self):
        return self.__design_Classifier5

    @design_Classifier5.setter
    def design_Classifier5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_design_Classifier__design_Classifier5", None)
        self.__design_Classifier5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "design_Relation4"):
                opp_val = getattr(old_value, "design_Relation4", None)
                if opp_val == self:
                    setattr(old_value, "design_Relation4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "design_Relation4"):
                opp_val = getattr(value, "design_Relation4", None)
                setattr(value, "design_Relation4", self)

    @property
    def design_Classifier12(self):
        return self.__design_Classifier12

    @design_Classifier12.setter
    def design_Classifier12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_design_Classifier__design_Classifier12", None)
        self.__design_Classifier12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "design_Operation"):
                    opp_val = getattr(item, "design_Operation", None)
                    
                    if opp_val == self:
                        setattr(item, "design_Operation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "design_Operation"):
                    opp_val = getattr(item, "design_Operation", None)
                    
                    setattr(item, "design_Operation", self)
                    

    @property
    def design_Classifier(self):
        return self.__design_Classifier

    @design_Classifier.setter
    def design_Classifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_design_Classifier__design_Classifier", None)
        self.__design_Classifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "design_Design"):
                opp_val = getattr(old_value, "design_Design", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "design_Design"):
                opp_val = getattr(value, "design_Design", None)
                if opp_val is None:
                    setattr(value, "design_Design", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class design_Design:

    def __init__(self, language: str, design_Design: set["design_Classifier"] = None, design_Design2: set["design_Relation"] = None):
        self.language = language
        self.design_Design = design_Design if design_Design is not None else set()
        self.design_Design2 = design_Design2 if design_Design2 is not None else set()
        
    @property
    def language(self) -> str:
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language

    @property
    def design_Design2(self):
        return self.__design_Design2

    @design_Design2.setter
    def design_Design2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_design_Design__design_Design2", None)
        self.__design_Design2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "design_Relation"):
                    opp_val = getattr(item, "design_Relation", None)
                    
                    if opp_val == self:
                        setattr(item, "design_Relation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "design_Relation"):
                    opp_val = getattr(item, "design_Relation", None)
                    
                    setattr(item, "design_Relation", self)
                    

    @property
    def design_Design(self):
        return self.__design_Design

    @design_Design.setter
    def design_Design(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_design_Design__design_Design", None)
        self.__design_Design = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "design_Classifier"):
                    opp_val = getattr(item, "design_Classifier", None)
                    
                    if opp_val == self:
                        setattr(item, "design_Classifier", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "design_Classifier"):
                    opp_val = getattr(item, "design_Classifier", None)
                    
                    setattr(item, "design_Classifier", self)
                    

class Relation:

    pass
class design_Generalization(Relation):

    pass
class design_Aggregation(Relation):

    pass
class design_Dependency(Relation):

    pass
class design_Realization(Relation):

    pass
class design_Composition(Relation):

    pass
class design_Association(Relation):

    pass
class design_Operation:

    def __init__(self, name: str, returnType: str, design_Operation: "design_Classifier" = None):
        self.name = name
        self.returnType = returnType
        self.design_Operation = design_Operation
        
    @property
    def returnType(self) -> str:
        return self.__returnType

    @returnType.setter
    def returnType(self, returnType: str):
        self.__returnType = returnType

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def design_Operation(self):
        return self.__design_Operation

    @design_Operation.setter
    def design_Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_design_Operation__design_Operation", None)
        self.__design_Operation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "design_Classifier12"):
                opp_val = getattr(old_value, "design_Classifier12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "design_Classifier12"):
                opp_val = getattr(value, "design_Classifier12", None)
                if opp_val is None:
                    setattr(value, "design_Classifier12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class design_Attribute:

    def __init__(self, name: str, type: str, design_Attribute: "design_Classifier" = None):
        self.name = name
        self.type = type
        self.design_Attribute = design_Attribute
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def design_Attribute(self):
        return self.__design_Attribute

    @design_Attribute.setter
    def design_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_design_Attribute__design_Attribute", None)
        self.__design_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "design_Classifier10"):
                opp_val = getattr(old_value, "design_Classifier10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "design_Classifier10"):
                opp_val = getattr(value, "design_Classifier10", None)
                if opp_val is None:
                    setattr(value, "design_Classifier10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Classifier:

    pass
class design_Interface(Classifier):

    pass
class design_Class(Classifier):

    pass