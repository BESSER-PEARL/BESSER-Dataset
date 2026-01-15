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
class oml_Operation(Feature):

    pass
class oml_StructuralFeature(Feature):

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
class oml_Attribute(StructuralFeature):

    pass
class oml_Reference(StructuralFeature):

    pass
class Classifier:

    pass
class oml_Class(Classifier):

    def __init__(self, isAbstract: str, Class: "oml_Class" = None, extendedBy: "oml_Class" = None, Class7: "oml_Class" = None, extends: set["oml_Class"] = None, owner: set["oml_Feature"] = None, Class10: "oml_Feature" = None):
        self.isAbstract = isAbstract
        self.Class = Class
        self.extendedBy = extendedBy
        self.Class7 = Class7
        self.extends = extends if extends is not None else set()
        self.owner = owner if owner is not None else set()
        self.Class10 = Class10
        
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
        old_value = getattr(self, f"_oml_Class__extends", None)
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
    def Class10(self):
        return self.__Class10

    @Class10.setter
    def Class10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oml_Class__Class10", None)
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

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oml_Class__owner", None)
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
    def Class(self):
        return self.__Class

    @Class.setter
    def Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oml_Class__Class", None)
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
    def extendedBy(self):
        return self.__extendedBy

    @extendedBy.setter
    def extendedBy(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oml_Class__extendedBy", None)
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
    def Class7(self):
        return self.__Class7

    @Class7.setter
    def Class7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oml_Class__Class7", None)
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

class Class:

    pass
class oml_ExternalClass(Class):

    pass
class PackageableElement:

    pass
class oml_Classifier(PackageableElement):

    pass
class AnnotatedElement:

    pass
class oml_NamedElement(AnnotatedElement):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class oml_Datatype(Classifier):

    pass
class oml_Annotation:

    def __init__(self, key: str, value: str, oml_Annotation: "oml_AnnotatedElement" = None):
        self.key = key
        self.value = value
        self.oml_Annotation = oml_Annotation
        
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
    def oml_Annotation(self):
        return self.__oml_Annotation

    @oml_Annotation.setter
    def oml_Annotation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oml_Annotation__oml_Annotation", None)
        self.__oml_Annotation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oml_AnnotatedElement"):
                opp_val = getattr(old_value, "oml_AnnotatedElement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oml_AnnotatedElement"):
                opp_val = getattr(value, "oml_AnnotatedElement", None)
                if opp_val is None:
                    setattr(value, "oml_AnnotatedElement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class oml_AnnotatedElement(ABC):

    pass
class oml_Package(PackageableElement):

    pass
class NamedElement:

    pass
class oml_Feature(NamedElement):

    def __init__(self, visibility: str, Feature: "oml_Class" = None, features: "oml_Class" = None, oml_Feature: "oml_Classifier" = None):
        self.visibility = visibility
        self.Feature = Feature
        self.features = features
        self.oml_Feature = oml_Feature
        
    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def Feature(self):
        return self.__Feature

    @Feature.setter
    def Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oml_Feature__Feature", None)
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
    def oml_Feature(self):
        return self.__oml_Feature

    @oml_Feature.setter
    def oml_Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oml_Feature__oml_Feature", None)
        self.__oml_Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oml_Classifier"):
                opp_val = getattr(old_value, "oml_Classifier", None)
                if opp_val == self:
                    setattr(old_value, "oml_Classifier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oml_Classifier"):
                opp_val = getattr(value, "oml_Classifier", None)
                setattr(value, "oml_Classifier", self)

    @property
    def features(self):
        return self.__features

    @features.setter
    def features(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oml_Feature__features", None)
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

class oml_Parameter(NamedElement):

    pass
class oml_PackageableElement(NamedElement):

    pass
class Package:

    pass
class oml_Model(Package):

    pass