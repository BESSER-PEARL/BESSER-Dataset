from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class StructuralFeature:

    pass
class ClassDiagram_Attribute(StructuralFeature):

    def __init__(self, multivalued: bool):
        self.multivalued = multivalued
        
    @property
    def multivalued(self) -> bool:
        return self.__multivalued

    @multivalued.setter
    def multivalued(self, multivalued: bool):
        self.__multivalued = multivalued

class ClassDiagram_Operation(StructuralFeature):

    pass
class ClassDiagram_TypedElement:

    pass
class TypedElement:

    pass
class ClassDiagram_Parameter(TypedElement):

    def __init__(self, name: str, Parameter: "ClassDiagram_Operation" = None, params: "ClassDiagram_Operation" = None):
        self.name = name
        self.Parameter = Parameter
        self.params = params
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def params(self):
        return self.__params

    @params.setter
    def params(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassDiagram_Parameter__params", None)
        self.__params = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Operation"):
                opp_val = getattr(old_value, "Operation", None)
                if opp_val == self:
                    setattr(old_value, "Operation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Operation"):
                opp_val = getattr(value, "Operation", None)
                setattr(value, "Operation", self)

    @property
    def Parameter(self):
        return self.__Parameter

    @Parameter.setter
    def Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassDiagram_Parameter__Parameter", None)
        self.__Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "paramOf"):
                opp_val = getattr(old_value, "paramOf", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "paramOf"):
                opp_val = getattr(value, "paramOf", None)
                if opp_val is None:
                    setattr(value, "paramOf", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ClassDiagram_StructuralFeature(TypedElement):

    def __init__(self, name: str, visibility: str, StructuralFeature: "ClassDiagram_Class" = None, features: "ClassDiagram_Class" = None):
        self.name = name
        self.visibility = visibility
        self.StructuralFeature = StructuralFeature
        self.features = features
        
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
    def StructuralFeature(self):
        return self.__StructuralFeature

    @StructuralFeature.setter
    def StructuralFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassDiagram_StructuralFeature__StructuralFeature", None)
        self.__StructuralFeature = value
        
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
    def features(self):
        return self.__features

    @features.setter
    def features(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassDiagram_StructuralFeature__features", None)
        self.__features = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Class8"):
                opp_val = getattr(old_value, "Class8", None)
                if opp_val == self:
                    setattr(old_value, "Class8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Class8"):
                opp_val = getattr(value, "Class8", None)
                setattr(value, "Class8", self)

class Classifier:

    pass
class ClassDiagram_PrimitiveType(Classifier):

    pass
class ClassDiagram_Class(Classifier):

    pass
class ClassDiagram_Classifier:

    def __init__(self, name: str, ClassDiagram_Classifier: "ClassDiagram_Model" = None, ClassDiagram_Classifier10: "ClassDiagram_TypedElement" = None):
        self.name = name
        self.ClassDiagram_Classifier = ClassDiagram_Classifier
        self.ClassDiagram_Classifier10 = ClassDiagram_Classifier10
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
            if hasattr(old_value, "ClassDiagram_Model"):
                opp_val = getattr(old_value, "ClassDiagram_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassDiagram_Model"):
                opp_val = getattr(value, "ClassDiagram_Model", None)
                if opp_val is None:
                    setattr(value, "ClassDiagram_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ClassDiagram_Classifier10(self):
        return self.__ClassDiagram_Classifier10

    @ClassDiagram_Classifier10.setter
    def ClassDiagram_Classifier10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassDiagram_Classifier__ClassDiagram_Classifier10", None)
        self.__ClassDiagram_Classifier10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassDiagram_TypedElement"):
                opp_val = getattr(old_value, "ClassDiagram_TypedElement", None)
                if opp_val == self:
                    setattr(old_value, "ClassDiagram_TypedElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassDiagram_TypedElement"):
                opp_val = getattr(value, "ClassDiagram_TypedElement", None)
                setattr(value, "ClassDiagram_TypedElement", self)

class ClassDiagram_Model:

    pass