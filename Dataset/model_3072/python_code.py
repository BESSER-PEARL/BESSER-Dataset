from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class VisibilityEnum(Enum):
    public = "public"
    private = "private"


############################################
# Definition of Classes
############################################

class Feature:

    pass
class OO_Operation(Feature):

    pass
class OO_StructuralFeature(Feature):

    def __init__(self, isMany: str):
        self.isMany = isMany
        
    @property
    def isMany(self) -> str:
        return self.__isMany

    @isMany.setter
    def isMany(self, isMany: str):
        self.__isMany = isMany

class StructuralFeature:

    pass
class OO_Attribute(StructuralFeature):

    pass
class OO_Reference(StructuralFeature):

    pass
class Classifier:

    pass
class OO_Class(Classifier):

    def __init__(self, isAbstract: str, Class7: "OO_Class" = None, extends: set["OO_Class"] = None, owner: set["OO_Feature"] = None, Class10: "OO_Feature" = None, Class: "OO_Class" = None, extendedBy: "OO_Class" = None):
        self.isAbstract = isAbstract
        self.Class7 = Class7
        self.extends = extends if extends is not None else set()
        self.owner = owner if owner is not None else set()
        self.Class10 = Class10
        self.Class = Class
        self.extendedBy = extendedBy
        
    @property
    def isAbstract(self) -> str:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: str):
        self.__isAbstract = isAbstract

    @property
    def extends(self):
        return self.__extends

    @extends.setter
    def extends(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OO_Class__extends", None)
        self.__extends = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Class7"):
                    opp_val = getattr(item, "Class7", None)
                    
                    if opp_val == self:
                        setattr(item, "Class7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Class7"):
                    opp_val = getattr(item, "Class7", None)
                    
                    setattr(item, "Class7", self)
                    

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OO_Class__owner", None)
        self.__owner = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Feature"):
                    opp_val = getattr(item, "Feature", None)
                    
                    if opp_val == self:
                        setattr(item, "Feature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Feature"):
                    opp_val = getattr(item, "Feature", None)
                    
                    setattr(item, "Feature", self)
                    

    @property
    def extendedBy(self):
        return self.__extendedBy

    @extendedBy.setter
    def extendedBy(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OO_Class__extendedBy", None)
        self.__extendedBy = value
        
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
    def Class(self):
        return self.__Class

    @Class.setter
    def Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OO_Class__Class", None)
        self.__Class = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "extendedBy"):
                opp_val = getattr(old_value, "extendedBy", None)
                if opp_val == self:
                    setattr(old_value, "extendedBy", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "extendedBy"):
                opp_val = getattr(value, "extendedBy", None)
                setattr(value, "extendedBy", self)

    @property
    def Class7(self):
        return self.__Class7

    @Class7.setter
    def Class7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OO_Class__Class7", None)
        self.__Class7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "extends"):
                opp_val = getattr(old_value, "extends", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "extends"):
                opp_val = getattr(value, "extends", None)
                if opp_val is None:
                    setattr(value, "extends", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Class10(self):
        return self.__Class10

    @Class10.setter
    def Class10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OO_Class__Class10", None)
        self.__Class10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "features"):
                opp_val = getattr(old_value, "features", None)
                if opp_val == self:
                    setattr(old_value, "features", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "features"):
                opp_val = getattr(value, "features", None)
                setattr(value, "features", self)

class Class:

    pass
class OO_ExternalClass(Class):

    pass
class OO_Datatype(Classifier):

    pass
class NamedElement:

    pass
class OO_Parameter(NamedElement):

    pass
class OO_Feature(NamedElement):

    def __init__(self, visibility: str, Feature: "OO_Class" = None, features: "OO_Class" = None, OO_Feature: "OO_Classifier" = None):
        self.visibility = visibility
        self.Feature = Feature
        self.features = features
        self.OO_Feature = OO_Feature
        
    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def features(self):
        return self.__features

    @features.setter
    def features(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OO_Feature__features", None)
        self.__features = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Class10"):
                opp_val = getattr(old_value, "Class10", None)
                if opp_val == self:
                    setattr(old_value, "Class10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Class10"):
                opp_val = getattr(value, "Class10", None)
                setattr(value, "Class10", self)

    @property
    def Feature(self):
        return self.__Feature

    @Feature.setter
    def Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OO_Feature__Feature", None)
        self.__Feature = value
        
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

    @property
    def OO_Feature(self):
        return self.__OO_Feature

    @OO_Feature.setter
    def OO_Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OO_Feature__OO_Feature", None)
        self.__OO_Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OO_Classifier"):
                opp_val = getattr(old_value, "OO_Classifier", None)
                if opp_val == self:
                    setattr(old_value, "OO_Classifier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OO_Classifier"):
                opp_val = getattr(value, "OO_Classifier", None)
                setattr(value, "OO_Classifier", self)

class OO_PackageableElement(NamedElement):

    pass
class Package:

    pass
class OO_Model(Package):

    pass
class PackageableElement:

    pass
class OO_Classifier(PackageableElement):

    pass
class AnnotatedElement:

    pass
class OO_NamedElement(AnnotatedElement):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class OO_Annotation:

    def __init__(self, key: str, value: str, OO_Annotation: "OO_AnnotatedElement" = None):
        self.key = key
        self.value = value
        self.OO_Annotation = OO_Annotation
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def OO_Annotation(self):
        return self.__OO_Annotation

    @OO_Annotation.setter
    def OO_Annotation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OO_Annotation__OO_Annotation", None)
        self.__OO_Annotation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OO_AnnotatedElement"):
                opp_val = getattr(old_value, "OO_AnnotatedElement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OO_AnnotatedElement"):
                opp_val = getattr(value, "OO_AnnotatedElement", None)
                if opp_val is None:
                    setattr(value, "OO_AnnotatedElement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class OO_AnnotatedElement(ABC):

    pass
class OO_Package(PackageableElement):

    pass