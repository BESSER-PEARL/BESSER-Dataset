from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class AggregationKind(Enum):
    none = "none"
    shared = "shared"
    composite = "composite"


############################################
# Definition of Classes
############################################

class Dependency:

    pass
class ClassDiagram_Realization(Dependency):

    pass
class Relationship:

    pass
class ClassDiagram_Generalization(Relationship):

    pass
class ClassDiagram_Dependency(Relationship):

    pass
class ClassDiagram_Association(Relationship):

    def __init__(self, name: str, ClassDiagram_Association: set["ClassDiagram_Property"] = None):
        self.name = name
        self.ClassDiagram_Association = ClassDiagram_Association if ClassDiagram_Association is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ClassDiagram_Association(self):
        return self.__ClassDiagram_Association

    @ClassDiagram_Association.setter
    def ClassDiagram_Association(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassDiagram_Association__ClassDiagram_Association", None)
        self.__ClassDiagram_Association = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ClassDiagram_Property6"):
                    opp_val = getattr(item, "ClassDiagram_Property6", None)
                    
                    if opp_val == self:
                        setattr(item, "ClassDiagram_Property6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ClassDiagram_Property6"):
                    opp_val = getattr(item, "ClassDiagram_Property6", None)
                    
                    setattr(item, "ClassDiagram_Property6", self)
                    

class ClassDiagram_Relationship(ABC):

    pass
class Classifier:

    pass
class ClassDiagram_DataType(Classifier):

    pass
class ClassDiagram_Classifier(ABC):

    def __init__(self, name: str, ClassDiagram_Classifier8: "ClassDiagram_Generalization" = None, ClassDiagram_Classifier11: "ClassDiagram_Generalization" = None, ClassDiagram_Classifier: "ClassDiagram_Property" = None, ClassDiagram_Classifier13: "ClassDiagram_Dependency" = None, ClassDiagram_Classifier16: "ClassDiagram_Dependency" = None):
        self.name = name
        self.ClassDiagram_Classifier8 = ClassDiagram_Classifier8
        self.ClassDiagram_Classifier11 = ClassDiagram_Classifier11
        self.ClassDiagram_Classifier = ClassDiagram_Classifier
        self.ClassDiagram_Classifier13 = ClassDiagram_Classifier13
        self.ClassDiagram_Classifier16 = ClassDiagram_Classifier16
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ClassDiagram_Classifier8(self):
        return self.__ClassDiagram_Classifier8

    @ClassDiagram_Classifier8.setter
    def ClassDiagram_Classifier8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassDiagram_Classifier__ClassDiagram_Classifier8", None)
        self.__ClassDiagram_Classifier8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassDiagram_Generalization"):
                opp_val = getattr(old_value, "ClassDiagram_Generalization", None)
                if opp_val == self:
                    setattr(old_value, "ClassDiagram_Generalization", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassDiagram_Generalization"):
                opp_val = getattr(value, "ClassDiagram_Generalization", None)
                setattr(value, "ClassDiagram_Generalization", self)

    @property
    def ClassDiagram_Classifier13(self):
        return self.__ClassDiagram_Classifier13

    @ClassDiagram_Classifier13.setter
    def ClassDiagram_Classifier13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassDiagram_Classifier__ClassDiagram_Classifier13", None)
        self.__ClassDiagram_Classifier13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassDiagram_Dependency"):
                opp_val = getattr(old_value, "ClassDiagram_Dependency", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassDiagram_Dependency"):
                opp_val = getattr(value, "ClassDiagram_Dependency", None)
                if opp_val is None:
                    setattr(value, "ClassDiagram_Dependency", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ClassDiagram_Classifier11(self):
        return self.__ClassDiagram_Classifier11

    @ClassDiagram_Classifier11.setter
    def ClassDiagram_Classifier11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassDiagram_Classifier__ClassDiagram_Classifier11", None)
        self.__ClassDiagram_Classifier11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassDiagram_Generalization10"):
                opp_val = getattr(old_value, "ClassDiagram_Generalization10", None)
                if opp_val == self:
                    setattr(old_value, "ClassDiagram_Generalization10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassDiagram_Generalization10"):
                opp_val = getattr(value, "ClassDiagram_Generalization10", None)
                setattr(value, "ClassDiagram_Generalization10", self)

    @property
    def ClassDiagram_Classifier16(self):
        return self.__ClassDiagram_Classifier16

    @ClassDiagram_Classifier16.setter
    def ClassDiagram_Classifier16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassDiagram_Classifier__ClassDiagram_Classifier16", None)
        self.__ClassDiagram_Classifier16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassDiagram_Dependency15"):
                opp_val = getattr(old_value, "ClassDiagram_Dependency15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassDiagram_Dependency15"):
                opp_val = getattr(value, "ClassDiagram_Dependency15", None)
                if opp_val is None:
                    setattr(value, "ClassDiagram_Dependency15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ClassDiagram_Classifier(self):
        return self.__ClassDiagram_Classifier

    @ClassDiagram_Classifier.setter
    def ClassDiagram_Classifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassDiagram_Classifier__ClassDiagram_Classifier", None)
        self.__ClassDiagram_Classifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassDiagram_Property4"):
                opp_val = getattr(old_value, "ClassDiagram_Property4", None)
                if opp_val == self:
                    setattr(old_value, "ClassDiagram_Property4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassDiagram_Property4"):
                opp_val = getattr(value, "ClassDiagram_Property4", None)
                setattr(value, "ClassDiagram_Property4", self)

class ClassDiagram_Interface(Classifier):

    pass
class ClassDiagram_Property:

    def __init__(self, name: str, lower: int, upper: str, aggregation: str, ClassDiagram_Property: "ClassDiagram_Class" = None, ClassDiagram_Property2: "ClassDiagram_Interface" = None, ClassDiagram_Property4: "ClassDiagram_Classifier" = None, ClassDiagram_Property6: "ClassDiagram_Association" = None):
        self.name = name
        self.lower = lower
        self.upper = upper
        self.aggregation = aggregation
        self.ClassDiagram_Property = ClassDiagram_Property
        self.ClassDiagram_Property2 = ClassDiagram_Property2
        self.ClassDiagram_Property4 = ClassDiagram_Property4
        self.ClassDiagram_Property6 = ClassDiagram_Property6
        
    @property
    def aggregation(self) -> str:
        return self.__aggregation

    @aggregation.setter
    def aggregation(self, aggregation: str):
        self.__aggregation = aggregation

    @property
    def lower(self) -> int:
        return self.__lower

    @lower.setter
    def lower(self, lower: int):
        self.__lower = lower

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def upper(self) -> str:
        return self.__upper

    @upper.setter
    def upper(self, upper: str):
        self.__upper = upper

    @property
    def ClassDiagram_Property(self):
        return self.__ClassDiagram_Property

    @ClassDiagram_Property.setter
    def ClassDiagram_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassDiagram_Property__ClassDiagram_Property", None)
        self.__ClassDiagram_Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassDiagram_Class"):
                opp_val = getattr(old_value, "ClassDiagram_Class", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassDiagram_Class"):
                opp_val = getattr(value, "ClassDiagram_Class", None)
                if opp_val is None:
                    setattr(value, "ClassDiagram_Class", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ClassDiagram_Property2(self):
        return self.__ClassDiagram_Property2

    @ClassDiagram_Property2.setter
    def ClassDiagram_Property2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassDiagram_Property__ClassDiagram_Property2", None)
        self.__ClassDiagram_Property2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassDiagram_Interface"):
                opp_val = getattr(old_value, "ClassDiagram_Interface", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassDiagram_Interface"):
                opp_val = getattr(value, "ClassDiagram_Interface", None)
                if opp_val is None:
                    setattr(value, "ClassDiagram_Interface", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ClassDiagram_Property6(self):
        return self.__ClassDiagram_Property6

    @ClassDiagram_Property6.setter
    def ClassDiagram_Property6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassDiagram_Property__ClassDiagram_Property6", None)
        self.__ClassDiagram_Property6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassDiagram_Association"):
                opp_val = getattr(old_value, "ClassDiagram_Association", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassDiagram_Association"):
                opp_val = getattr(value, "ClassDiagram_Association", None)
                if opp_val is None:
                    setattr(value, "ClassDiagram_Association", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ClassDiagram_Property4(self):
        return self.__ClassDiagram_Property4

    @ClassDiagram_Property4.setter
    def ClassDiagram_Property4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassDiagram_Property__ClassDiagram_Property4", None)
        self.__ClassDiagram_Property4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassDiagram_Classifier"):
                opp_val = getattr(old_value, "ClassDiagram_Classifier", None)
                if opp_val == self:
                    setattr(old_value, "ClassDiagram_Classifier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassDiagram_Classifier"):
                opp_val = getattr(value, "ClassDiagram_Classifier", None)
                setattr(value, "ClassDiagram_Classifier", self)

class ClassDiagram_Class(Classifier):

    pass