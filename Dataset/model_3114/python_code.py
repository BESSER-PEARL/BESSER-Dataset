from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class StereotypeClass(Enum):
    View = "View"
    Security = "Security"
    Entity = "Entity"
class PrimitiveData(Enum):
    String = "String"
    int = "int"
    byte = "byte"
    short = "short"
    long = "long"
    float = "float"
    double = "double"
    char = "char"
    boolean = "boolean"
class StereotypeAttribute(Enum):
    Password = "Password"
    User = "User"


############################################
# Definition of Classes
############################################

class LedsCodeModel_Association:

    def __init__(self, name: str, LedsCodeModel_Association: "LedsCodeModel_Class" = None, LedsCodeModel_Association13: "LedsCodeModel_Class" = None):
        self.name = name
        self.LedsCodeModel_Association = LedsCodeModel_Association
        self.LedsCodeModel_Association13 = LedsCodeModel_Association13
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def LedsCodeModel_Association13(self):
        return self.__LedsCodeModel_Association13

    @LedsCodeModel_Association13.setter
    def LedsCodeModel_Association13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_LedsCodeModel_Association__LedsCodeModel_Association13", None)
        self.__LedsCodeModel_Association13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "LedsCodeModel_Class14"):
                opp_val = getattr(old_value, "LedsCodeModel_Class14", None)
                if opp_val == self:
                    setattr(old_value, "LedsCodeModel_Class14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LedsCodeModel_Class14"):
                opp_val = getattr(value, "LedsCodeModel_Class14", None)
                setattr(value, "LedsCodeModel_Class14", self)

    @property
    def LedsCodeModel_Association(self):
        return self.__LedsCodeModel_Association

    @LedsCodeModel_Association.setter
    def LedsCodeModel_Association(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_LedsCodeModel_Association__LedsCodeModel_Association", None)
        self.__LedsCodeModel_Association = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "LedsCodeModel_Class11"):
                opp_val = getattr(old_value, "LedsCodeModel_Class11", None)
                if opp_val == self:
                    setattr(old_value, "LedsCodeModel_Class11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LedsCodeModel_Class11"):
                opp_val = getattr(value, "LedsCodeModel_Class11", None)
                setattr(value, "LedsCodeModel_Class11", self)

class Classifier:

    pass
class LedsCodeModel_PrimitiveDataType(Classifier):

    def __init__(self, type: str):
        self.type = type
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class LedsCodeModel_Classifier(ABC):

    def __init__(self, name: str, LedsCodeModel_Classifier: "LedsCodeModel_Attribute" = None):
        self.name = name
        self.LedsCodeModel_Classifier = LedsCodeModel_Classifier
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def LedsCodeModel_Classifier(self):
        return self.__LedsCodeModel_Classifier

    @LedsCodeModel_Classifier.setter
    def LedsCodeModel_Classifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_LedsCodeModel_Classifier__LedsCodeModel_Classifier", None)
        self.__LedsCodeModel_Classifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "LedsCodeModel_Attribute9"):
                opp_val = getattr(old_value, "LedsCodeModel_Attribute9", None)
                if opp_val == self:
                    setattr(old_value, "LedsCodeModel_Attribute9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LedsCodeModel_Attribute9"):
                opp_val = getattr(value, "LedsCodeModel_Attribute9", None)
                setattr(value, "LedsCodeModel_Attribute9", self)

class Model:

    pass
class LedsCodeModel_ClassDiagram(Model):

    def __init__(self, name: str, LedsCodeModel_ClassDiagram: set["LedsCodeModel_AbstractClass"] = None):
        self.name = name
        self.LedsCodeModel_ClassDiagram = LedsCodeModel_ClassDiagram if LedsCodeModel_ClassDiagram is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def LedsCodeModel_ClassDiagram(self):
        return self.__LedsCodeModel_ClassDiagram

    @LedsCodeModel_ClassDiagram.setter
    def LedsCodeModel_ClassDiagram(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_LedsCodeModel_ClassDiagram__LedsCodeModel_ClassDiagram", None)
        self.__LedsCodeModel_ClassDiagram = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "LedsCodeModel_AbstractClass"):
                    opp_val = getattr(item, "LedsCodeModel_AbstractClass", None)
                    
                    if opp_val == self:
                        setattr(item, "LedsCodeModel_AbstractClass", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "LedsCodeModel_AbstractClass"):
                    opp_val = getattr(item, "LedsCodeModel_AbstractClass", None)
                    
                    setattr(item, "LedsCodeModel_AbstractClass", self)
                    

class LedsCodeModel_Feature:

    def __init__(self, language: str, dataBaseName: str, engine: str, orm: str, applicationType: str, LedsCodeModel_Feature: "LedsCodeModel_Specification" = None):
        self.language = language
        self.dataBaseName = dataBaseName
        self.engine = engine
        self.orm = orm
        self.applicationType = applicationType
        self.LedsCodeModel_Feature = LedsCodeModel_Feature
        
    @property
    def engine(self) -> str:
        return self.__engine

    @engine.setter
    def engine(self, engine: str):
        self.__engine = engine

    @property
    def dataBaseName(self) -> str:
        return self.__dataBaseName

    @dataBaseName.setter
    def dataBaseName(self, dataBaseName: str):
        self.__dataBaseName = dataBaseName

    @property
    def orm(self) -> str:
        return self.__orm

    @orm.setter
    def orm(self, orm: str):
        self.__orm = orm

    @property
    def language(self) -> str:
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language

    @property
    def applicationType(self) -> str:
        return self.__applicationType

    @applicationType.setter
    def applicationType(self, applicationType: str):
        self.__applicationType = applicationType

    @property
    def LedsCodeModel_Feature(self):
        return self.__LedsCodeModel_Feature

    @LedsCodeModel_Feature.setter
    def LedsCodeModel_Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_LedsCodeModel_Feature__LedsCodeModel_Feature", None)
        self.__LedsCodeModel_Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "LedsCodeModel_Specification2"):
                opp_val = getattr(old_value, "LedsCodeModel_Specification2", None)
                if opp_val == self:
                    setattr(old_value, "LedsCodeModel_Specification2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LedsCodeModel_Specification2"):
                opp_val = getattr(value, "LedsCodeModel_Specification2", None)
                setattr(value, "LedsCodeModel_Specification2", self)

class LedsCodeModel_Model(ABC):

    pass
class LedsCodeModel_Specification:

    def __init__(self, name: str, createdDate: date, LedsCodeModel_Specification: set["LedsCodeModel_Model"] = None, LedsCodeModel_Specification2: "LedsCodeModel_Feature" = None):
        self.name = name
        self.createdDate = createdDate
        self.LedsCodeModel_Specification = LedsCodeModel_Specification if LedsCodeModel_Specification is not None else set()
        self.LedsCodeModel_Specification2 = LedsCodeModel_Specification2
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def createdDate(self) -> date:
        return self.__createdDate

    @createdDate.setter
    def createdDate(self, createdDate: date):
        self.__createdDate = createdDate

    @property
    def LedsCodeModel_Specification2(self):
        return self.__LedsCodeModel_Specification2

    @LedsCodeModel_Specification2.setter
    def LedsCodeModel_Specification2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_LedsCodeModel_Specification__LedsCodeModel_Specification2", None)
        self.__LedsCodeModel_Specification2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "LedsCodeModel_Feature"):
                opp_val = getattr(old_value, "LedsCodeModel_Feature", None)
                if opp_val == self:
                    setattr(old_value, "LedsCodeModel_Feature", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LedsCodeModel_Feature"):
                opp_val = getattr(value, "LedsCodeModel_Feature", None)
                setattr(value, "LedsCodeModel_Feature", self)

    @property
    def LedsCodeModel_Specification(self):
        return self.__LedsCodeModel_Specification

    @LedsCodeModel_Specification.setter
    def LedsCodeModel_Specification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_LedsCodeModel_Specification__LedsCodeModel_Specification", None)
        self.__LedsCodeModel_Specification = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "LedsCodeModel_Model"):
                    opp_val = getattr(item, "LedsCodeModel_Model", None)
                    
                    if opp_val == self:
                        setattr(item, "LedsCodeModel_Model", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "LedsCodeModel_Model"):
                    opp_val = getattr(item, "LedsCodeModel_Model", None)
                    
                    setattr(item, "LedsCodeModel_Model", self)
                    

class LedsCodeModel_Attribute:

    def __init__(self, name: str, LedsCodeModel_Attribute: "LedsCodeModel_Class" = None, LedsCodeModel_Attribute9: "LedsCodeModel_Classifier" = None):
        self.name = name
        self.LedsCodeModel_Attribute = LedsCodeModel_Attribute
        self.LedsCodeModel_Attribute9 = LedsCodeModel_Attribute9
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def LedsCodeModel_Attribute9(self):
        return self.__LedsCodeModel_Attribute9

    @LedsCodeModel_Attribute9.setter
    def LedsCodeModel_Attribute9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_LedsCodeModel_Attribute__LedsCodeModel_Attribute9", None)
        self.__LedsCodeModel_Attribute9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "LedsCodeModel_Classifier"):
                opp_val = getattr(old_value, "LedsCodeModel_Classifier", None)
                if opp_val == self:
                    setattr(old_value, "LedsCodeModel_Classifier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LedsCodeModel_Classifier"):
                opp_val = getattr(value, "LedsCodeModel_Classifier", None)
                setattr(value, "LedsCodeModel_Classifier", self)

    @property
    def LedsCodeModel_Attribute(self):
        return self.__LedsCodeModel_Attribute

    @LedsCodeModel_Attribute.setter
    def LedsCodeModel_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_LedsCodeModel_Attribute__LedsCodeModel_Attribute", None)
        self.__LedsCodeModel_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "LedsCodeModel_Class"):
                opp_val = getattr(old_value, "LedsCodeModel_Class", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LedsCodeModel_Class"):
                opp_val = getattr(value, "LedsCodeModel_Class", None)
                if opp_val is None:
                    setattr(value, "LedsCodeModel_Class", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class AbstractClass:

    pass
class LedsCodeModel_ENUM(AbstractClass):

    def __init__(self, values: str):
        self.values = values
        
    @property
    def values(self) -> str:
        return self.__values

    @values.setter
    def values(self, values: str):
        self.__values = values

class LedsCodeModel_Class(AbstractClass):

    def __init__(self, abstract: bool, stereotypeClass: str, LedsCodeModel_Class: set["LedsCodeModel_Attribute"] = None, LedsCodeModel_Class7: "LedsCodeModel_Class" = None, LedsCodeModel_Class5: set["LedsCodeModel_Class"] = None, LedsCodeModel_Class11: "LedsCodeModel_Association" = None, LedsCodeModel_Class14: "LedsCodeModel_Association" = None):
        self.abstract = abstract
        self.stereotypeClass = stereotypeClass
        self.LedsCodeModel_Class = LedsCodeModel_Class if LedsCodeModel_Class is not None else set()
        self.LedsCodeModel_Class7 = LedsCodeModel_Class7
        self.LedsCodeModel_Class5 = LedsCodeModel_Class5 if LedsCodeModel_Class5 is not None else set()
        self.LedsCodeModel_Class11 = LedsCodeModel_Class11
        self.LedsCodeModel_Class14 = LedsCodeModel_Class14
        
    @property
    def stereotypeClass(self) -> str:
        return self.__stereotypeClass

    @stereotypeClass.setter
    def stereotypeClass(self, stereotypeClass: str):
        self.__stereotypeClass = stereotypeClass

    @property
    def abstract(self) -> bool:
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: bool):
        self.__abstract = abstract

    @property
    def LedsCodeModel_Class14(self):
        return self.__LedsCodeModel_Class14

    @LedsCodeModel_Class14.setter
    def LedsCodeModel_Class14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_LedsCodeModel_Class__LedsCodeModel_Class14", None)
        self.__LedsCodeModel_Class14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "LedsCodeModel_Association13"):
                opp_val = getattr(old_value, "LedsCodeModel_Association13", None)
                if opp_val == self:
                    setattr(old_value, "LedsCodeModel_Association13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LedsCodeModel_Association13"):
                opp_val = getattr(value, "LedsCodeModel_Association13", None)
                setattr(value, "LedsCodeModel_Association13", self)

    @property
    def LedsCodeModel_Class7(self):
        return self.__LedsCodeModel_Class7

    @LedsCodeModel_Class7.setter
    def LedsCodeModel_Class7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_LedsCodeModel_Class__LedsCodeModel_Class7", None)
        self.__LedsCodeModel_Class7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "LedsCodeModel_Class5"):
                opp_val = getattr(old_value, "LedsCodeModel_Class5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LedsCodeModel_Class5"):
                opp_val = getattr(value, "LedsCodeModel_Class5", None)
                if opp_val is None:
                    setattr(value, "LedsCodeModel_Class5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def LedsCodeModel_Class5(self):
        return self.__LedsCodeModel_Class5

    @LedsCodeModel_Class5.setter
    def LedsCodeModel_Class5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_LedsCodeModel_Class__LedsCodeModel_Class5", None)
        self.__LedsCodeModel_Class5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "LedsCodeModel_Class7"):
                    opp_val = getattr(item, "LedsCodeModel_Class7", None)
                    
                    if opp_val == self:
                        setattr(item, "LedsCodeModel_Class7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "LedsCodeModel_Class7"):
                    opp_val = getattr(item, "LedsCodeModel_Class7", None)
                    
                    setattr(item, "LedsCodeModel_Class7", self)
                    

    @property
    def LedsCodeModel_Class11(self):
        return self.__LedsCodeModel_Class11

    @LedsCodeModel_Class11.setter
    def LedsCodeModel_Class11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_LedsCodeModel_Class__LedsCodeModel_Class11", None)
        self.__LedsCodeModel_Class11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "LedsCodeModel_Association"):
                opp_val = getattr(old_value, "LedsCodeModel_Association", None)
                if opp_val == self:
                    setattr(old_value, "LedsCodeModel_Association", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LedsCodeModel_Association"):
                opp_val = getattr(value, "LedsCodeModel_Association", None)
                setattr(value, "LedsCodeModel_Association", self)

    @property
    def LedsCodeModel_Class(self):
        return self.__LedsCodeModel_Class

    @LedsCodeModel_Class.setter
    def LedsCodeModel_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_LedsCodeModel_Class__LedsCodeModel_Class", None)
        self.__LedsCodeModel_Class = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "LedsCodeModel_Attribute"):
                    opp_val = getattr(item, "LedsCodeModel_Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "LedsCodeModel_Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "LedsCodeModel_Attribute"):
                    opp_val = getattr(item, "LedsCodeModel_Attribute", None)
                    
                    setattr(item, "LedsCodeModel_Attribute", self)
                    

class LedsCodeModel_AbstractClass(Classifier):

    pass