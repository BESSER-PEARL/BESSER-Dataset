from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class ClassM_Model:

    pass
class StructuralFeature:

    pass
class ClassM_Attribute(StructuralFeature):

    def __init__(self, multivalued: bool):
        self.multivalued = multivalued
        
    @property
    def multivalued(self) -> bool:
        return self.__multivalued

    @multivalued.setter
    def multivalued(self, multivalued: bool):
        self.__multivalued = multivalued

class ClassM_Operation(StructuralFeature):

    pass
class TypedElement:

    pass
class ClassM_Parameter(TypedElement):

    def __init__(self, name: str, Parameter: "ClassM_Operation" = None, params: "ClassM_Operation" = None):
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
    def Parameter(self):
        return self.__Parameter

    @Parameter.setter
    def Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassM_Parameter__Parameter", None)
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

    @property
    def params(self):
        return self.__params

    @params.setter
    def params(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassM_Parameter__params", None)
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

class ClassM_TypedElement:

    pass
class ClassM_Classifier:

    def __init__(self, name: str, type: set["ClassM_TypedElement"] = None, Classifier: "ClassM_TypedElement" = None, ClassM_Classifier: "ClassM_Model" = None):
        self.name = name
        self.type = type if type is not None else set()
        self.Classifier = Classifier
        self.ClassM_Classifier = ClassM_Classifier
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassM_Classifier__type", None)
        self.__type = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TypedElement"):
                    opp_val = getattr(item, "TypedElement", None)
                    
                    if opp_val == self:
                        setattr(item, "TypedElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TypedElement"):
                    opp_val = getattr(item, "TypedElement", None)
                    
                    setattr(item, "TypedElement", self)
                    

    @property
    def Classifier(self):
        return self.__Classifier

    @Classifier.setter
    def Classifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassM_Classifier__Classifier", None)
        self.__Classifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "typeOf"):
                opp_val = getattr(old_value, "typeOf", None)
                if opp_val == self:
                    setattr(old_value, "typeOf", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "typeOf"):
                opp_val = getattr(value, "typeOf", None)
                setattr(value, "typeOf", self)

    @property
    def ClassM_Classifier(self):
        return self.__ClassM_Classifier

    @ClassM_Classifier.setter
    def ClassM_Classifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassM_Classifier__ClassM_Classifier", None)
        self.__ClassM_Classifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassM_Model"):
                opp_val = getattr(old_value, "ClassM_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassM_Model"):
                opp_val = getattr(value, "ClassM_Model", None)
                if opp_val is None:
                    setattr(value, "ClassM_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ClassM_StructuralFeature(TypedElement):

    def __init__(self, name: str, visibility: str, StructuralFeature: "ClassM_Class" = None, features: "ClassM_Class" = None):
        self.name = name
        self.visibility = visibility
        self.StructuralFeature = StructuralFeature
        self.features = features
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
        old_value = getattr(self, f"_ClassM_StructuralFeature__features", None)
        self.__features = value
        
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
    def StructuralFeature(self):
        return self.__StructuralFeature

    @StructuralFeature.setter
    def StructuralFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassM_StructuralFeature__StructuralFeature", None)
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

class Classifier:

    pass
class ClassM_PrimitiveType(Classifier):

    pass
class ClassM_Class(Classifier):

    pass