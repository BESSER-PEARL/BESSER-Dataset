from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class VisibilityKind(Enum):
    public = "public"
    private = "private"
    protected = "protected"
    package = "package"


############################################
# Definition of Classes
############################################

class uml_Model:

    def __init__(self, name: str, uml_Model: set["uml_PackageableElement"] = None):
        self.name = name
        self.uml_Model = uml_Model if uml_Model is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def uml_Model(self):
        return self.__uml_Model

    @uml_Model.setter
    def uml_Model(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Model__uml_Model", None)
        self.__uml_Model = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_PackageableElement103"):
                    opp_val = getattr(item, "uml_PackageableElement103", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_PackageableElement103", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_PackageableElement103"):
                    opp_val = getattr(item, "uml_PackageableElement103", None)
                    
                    setattr(item, "uml_PackageableElement103", self)
                    

class Feature:

    pass
class Namespace:

    pass
class uml_BehavioralFeature(Feature, Namespace):

    def __init__(self, isAbstract: str, uml_BehavioralFeature82: set["uml_Type"] = None, uml_BehavioralFeature: set["uml_Parameter"] = None):
        self.isAbstract = isAbstract
        self.uml_BehavioralFeature82 = uml_BehavioralFeature82 if uml_BehavioralFeature82 is not None else set()
        self.uml_BehavioralFeature = uml_BehavioralFeature if uml_BehavioralFeature is not None else set()
        
    @property
    def isAbstract(self) -> str:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: str):
        self.__isAbstract = isAbstract

    @property
    def uml_BehavioralFeature82(self):
        return self.__uml_BehavioralFeature82

    @uml_BehavioralFeature82.setter
    def uml_BehavioralFeature82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_BehavioralFeature__uml_BehavioralFeature82", None)
        self.__uml_BehavioralFeature82 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_Type83"):
                    opp_val = getattr(item, "uml_Type83", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_Type83", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_Type83"):
                    opp_val = getattr(item, "uml_Type83", None)
                    
                    setattr(item, "uml_Type83", self)
                    

    @property
    def uml_BehavioralFeature(self):
        return self.__uml_BehavioralFeature

    @uml_BehavioralFeature.setter
    def uml_BehavioralFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_BehavioralFeature__uml_BehavioralFeature", None)
        self.__uml_BehavioralFeature = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_Parameter80"):
                    opp_val = getattr(item, "uml_Parameter80", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_Parameter80", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_Parameter80"):
                    opp_val = getattr(item, "uml_Parameter80", None)
                    
                    setattr(item, "uml_Parameter80", self)
                    

class BehavioralFeature:

    pass
class uml_Operation(BehavioralFeature):

    def __init__(self, isQuery: str, isOrdered: str, isUnique: str, lower: str, upper: str, uml_Operation: "uml_Parameter" = None, ownedOperation: "uml_Class" = None, uml_Operation78: "uml_Operation" = None, uml_Operation76: set["uml_Operation"] = None, Operation: "uml_Class" = None):
        self.isQuery = isQuery
        self.isOrdered = isOrdered
        self.isUnique = isUnique
        self.lower = lower
        self.upper = upper
        self.uml_Operation = uml_Operation
        self.ownedOperation = ownedOperation
        self.uml_Operation78 = uml_Operation78
        self.uml_Operation76 = uml_Operation76 if uml_Operation76 is not None else set()
        self.Operation = Operation
        
    @property
    def isUnique(self) -> str:
        return self.__isUnique

    @isUnique.setter
    def isUnique(self, isUnique: str):
        self.__isUnique = isUnique

    @property
    def isOrdered(self) -> str:
        return self.__isOrdered

    @isOrdered.setter
    def isOrdered(self, isOrdered: str):
        self.__isOrdered = isOrdered

    @property
    def isQuery(self) -> str:
        return self.__isQuery

    @isQuery.setter
    def isQuery(self, isQuery: str):
        self.__isQuery = isQuery

    @property
    def lower(self) -> str:
        return self.__lower

    @lower.setter
    def lower(self, lower: str):
        self.__lower = lower

    @property
    def upper(self) -> str:
        return self.__upper

    @upper.setter
    def upper(self, upper: str):
        self.__upper = upper

    @property
    def uml_Operation78(self):
        return self.__uml_Operation78

    @uml_Operation78.setter
    def uml_Operation78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Operation__uml_Operation78", None)
        self.__uml_Operation78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Operation76"):
                opp_val = getattr(old_value, "uml_Operation76", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Operation76"):
                opp_val = getattr(value, "uml_Operation76", None)
                if opp_val is None:
                    setattr(value, "uml_Operation76", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml_Operation(self):
        return self.__uml_Operation

    @uml_Operation.setter
    def uml_Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Operation__uml_Operation", None)
        self.__uml_Operation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Parameter"):
                opp_val = getattr(old_value, "uml_Parameter", None)
                if opp_val == self:
                    setattr(old_value, "uml_Parameter", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Parameter"):
                opp_val = getattr(value, "uml_Parameter", None)
                setattr(value, "uml_Parameter", self)

    @property
    def uml_Operation76(self):
        return self.__uml_Operation76

    @uml_Operation76.setter
    def uml_Operation76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Operation__uml_Operation76", None)
        self.__uml_Operation76 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_Operation78"):
                    opp_val = getattr(item, "uml_Operation78", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_Operation78", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_Operation78"):
                    opp_val = getattr(item, "uml_Operation78", None)
                    
                    setattr(item, "uml_Operation78", self)
                    

    @property
    def Operation(self):
        return self.__Operation

    @Operation.setter
    def Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Operation__Operation", None)
        self.__Operation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "class"):
                opp_val = getattr(old_value, "class", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "class"):
                opp_val = getattr(value, "class", None)
                if opp_val is None:
                    setattr(value, "class", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ownedOperation(self):
        return self.__ownedOperation

    @ownedOperation.setter
    def ownedOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Operation__ownedOperation", None)
        self.__ownedOperation = value
        
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

class uml_Parameter:

    def __init__(self, default: str, isException: str, isStream: str, uml_Parameter72: "uml_ValueSpecification" = None, uml_Parameter: "uml_Operation" = None, uml_Parameter80: "uml_BehavioralFeature" = None):
        self.default = default
        self.isException = isException
        self.isStream = isStream
        self.uml_Parameter72 = uml_Parameter72
        self.uml_Parameter = uml_Parameter
        self.uml_Parameter80 = uml_Parameter80
        
    @property
    def isStream(self) -> str:
        return self.__isStream

    @isStream.setter
    def isStream(self, isStream: str):
        self.__isStream = isStream

    @property
    def default(self) -> str:
        return self.__default

    @default.setter
    def default(self, default: str):
        self.__default = default

    @property
    def isException(self) -> str:
        return self.__isException

    @isException.setter
    def isException(self, isException: str):
        self.__isException = isException

    @property
    def uml_Parameter(self):
        return self.__uml_Parameter

    @uml_Parameter.setter
    def uml_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Parameter__uml_Parameter", None)
        self.__uml_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Operation"):
                opp_val = getattr(old_value, "uml_Operation", None)
                if opp_val == self:
                    setattr(old_value, "uml_Operation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Operation"):
                opp_val = getattr(value, "uml_Operation", None)
                setattr(value, "uml_Operation", self)

    @property
    def uml_Parameter72(self):
        return self.__uml_Parameter72

    @uml_Parameter72.setter
    def uml_Parameter72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Parameter__uml_Parameter72", None)
        self.__uml_Parameter72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_ValueSpecification"):
                opp_val = getattr(old_value, "uml_ValueSpecification", None)
                if opp_val == self:
                    setattr(old_value, "uml_ValueSpecification", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_ValueSpecification"):
                opp_val = getattr(value, "uml_ValueSpecification", None)
                setattr(value, "uml_ValueSpecification", self)

    @property
    def uml_Parameter80(self):
        return self.__uml_Parameter80

    @uml_Parameter80.setter
    def uml_Parameter80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Parameter__uml_Parameter80", None)
        self.__uml_Parameter80 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_BehavioralFeature"):
                opp_val = getattr(old_value, "uml_BehavioralFeature", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_BehavioralFeature"):
                opp_val = getattr(value, "uml_BehavioralFeature", None)
                if opp_val is None:
                    setattr(value, "uml_BehavioralFeature", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Dependency:

    pass
class uml_Abstraction(Dependency):

    pass
class Abstraction:

    pass
class uml_Realization(Abstraction):

    pass
class Realization:

    pass
class uml_Feature(ABC):

    def __init__(self, isStatic: str, Feature: "uml_Classifier" = None, feature: set["uml_Classifier"] = None):
        self.isStatic = isStatic
        self.Feature = Feature
        self.feature = feature if feature is not None else set()
        
    @property
    def isStatic(self) -> str:
        return self.__isStatic

    @isStatic.setter
    def isStatic(self, isStatic: str):
        self.__isStatic = isStatic

    @property
    def feature(self):
        return self.__feature

    @feature.setter
    def feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Feature__feature", None)
        self.__feature = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Classifier"):
                    opp_val = getattr(item, "Classifier", None)
                    
                    if opp_val == self:
                        setattr(item, "Classifier", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Classifier"):
                    opp_val = getattr(item, "Classifier", None)
                    
                    setattr(item, "Classifier", self)
                    

    @property
    def Feature(self):
        return self.__Feature

    @Feature.setter
    def Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Feature__Feature", None)
        self.__Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "featuringClassifier"):
                opp_val = getattr(old_value, "featuringClassifier", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "featuringClassifier"):
                opp_val = getattr(value, "featuringClassifier", None)
                if opp_val is None:
                    setattr(value, "featuringClassifier", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Type:

    pass
class uml_Classifier(Type):

    def __init__(self, isAbstract: str, substitutingClassifier: set["uml_Substitution"] = None, featuringClassifier: set["uml_Feature"] = None, uml_Classifier: set["uml_NamedElement"] = None, uml_Classifier57: "uml_Classifier" = None, uml_Classifier55: set["uml_Classifier"] = None, uml_Classifier60: "uml_Classifier" = None, uml_Classifier58: set["uml_Classifier"] = None, uml_Classifier63: set["uml_Property"] = None, Classifier: "uml_Feature" = None, uml_Classifier67: "uml_Substitution" = None, Classifier69: "uml_Substitution" = None, uml_Classifier86: "uml_Class" = None, uml_Classifier98: "uml_Generalization" = None, uml_Classifier101: "uml_Generalization" = None):
        self.isAbstract = isAbstract
        self.substitutingClassifier = substitutingClassifier if substitutingClassifier is not None else set()
        self.featuringClassifier = featuringClassifier if featuringClassifier is not None else set()
        self.uml_Classifier = uml_Classifier if uml_Classifier is not None else set()
        self.uml_Classifier57 = uml_Classifier57
        self.uml_Classifier55 = uml_Classifier55 if uml_Classifier55 is not None else set()
        self.uml_Classifier60 = uml_Classifier60
        self.uml_Classifier58 = uml_Classifier58 if uml_Classifier58 is not None else set()
        self.uml_Classifier63 = uml_Classifier63 if uml_Classifier63 is not None else set()
        self.Classifier = Classifier
        self.uml_Classifier67 = uml_Classifier67
        self.Classifier69 = Classifier69
        self.uml_Classifier86 = uml_Classifier86
        self.uml_Classifier98 = uml_Classifier98
        self.uml_Classifier101 = uml_Classifier101
        
    @property
    def isAbstract(self) -> str:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: str):
        self.__isAbstract = isAbstract

    @property
    def uml_Classifier57(self):
        return self.__uml_Classifier57

    @uml_Classifier57.setter
    def uml_Classifier57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Classifier__uml_Classifier57", None)
        self.__uml_Classifier57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Classifier55"):
                opp_val = getattr(old_value, "uml_Classifier55", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Classifier55"):
                opp_val = getattr(value, "uml_Classifier55", None)
                if opp_val is None:
                    setattr(value, "uml_Classifier55", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Classifier69(self):
        return self.__Classifier69

    @Classifier69.setter
    def Classifier69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Classifier__Classifier69", None)
        self.__Classifier69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "substitution"):
                opp_val = getattr(old_value, "substitution", None)
                if opp_val == self:
                    setattr(old_value, "substitution", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "substitution"):
                opp_val = getattr(value, "substitution", None)
                setattr(value, "substitution", self)

    @property
    def substitutingClassifier(self):
        return self.__substitutingClassifier

    @substitutingClassifier.setter
    def substitutingClassifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Classifier__substitutingClassifier", None)
        self.__substitutingClassifier = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Substitution"):
                    opp_val = getattr(item, "Substitution", None)
                    
                    if opp_val == self:
                        setattr(item, "Substitution", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Substitution"):
                    opp_val = getattr(item, "Substitution", None)
                    
                    setattr(item, "Substitution", self)
                    

    @property
    def uml_Classifier101(self):
        return self.__uml_Classifier101

    @uml_Classifier101.setter
    def uml_Classifier101(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Classifier__uml_Classifier101", None)
        self.__uml_Classifier101 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Generalization100"):
                opp_val = getattr(old_value, "uml_Generalization100", None)
                if opp_val == self:
                    setattr(old_value, "uml_Generalization100", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Generalization100"):
                opp_val = getattr(value, "uml_Generalization100", None)
                setattr(value, "uml_Generalization100", self)

    @property
    def uml_Classifier67(self):
        return self.__uml_Classifier67

    @uml_Classifier67.setter
    def uml_Classifier67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Classifier__uml_Classifier67", None)
        self.__uml_Classifier67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Substitution"):
                opp_val = getattr(old_value, "uml_Substitution", None)
                if opp_val == self:
                    setattr(old_value, "uml_Substitution", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Substitution"):
                opp_val = getattr(value, "uml_Substitution", None)
                setattr(value, "uml_Substitution", self)

    @property
    def featuringClassifier(self):
        return self.__featuringClassifier

    @featuringClassifier.setter
    def featuringClassifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Classifier__featuringClassifier", None)
        self.__featuringClassifier = value if value is not None else set()
        
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
    def uml_Classifier60(self):
        return self.__uml_Classifier60

    @uml_Classifier60.setter
    def uml_Classifier60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Classifier__uml_Classifier60", None)
        self.__uml_Classifier60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Classifier58"):
                opp_val = getattr(old_value, "uml_Classifier58", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Classifier58"):
                opp_val = getattr(value, "uml_Classifier58", None)
                if opp_val is None:
                    setattr(value, "uml_Classifier58", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml_Classifier86(self):
        return self.__uml_Classifier86

    @uml_Classifier86.setter
    def uml_Classifier86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Classifier__uml_Classifier86", None)
        self.__uml_Classifier86 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Class85"):
                opp_val = getattr(old_value, "uml_Class85", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Class85"):
                opp_val = getattr(value, "uml_Class85", None)
                if opp_val is None:
                    setattr(value, "uml_Class85", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml_Classifier98(self):
        return self.__uml_Classifier98

    @uml_Classifier98.setter
    def uml_Classifier98(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Classifier__uml_Classifier98", None)
        self.__uml_Classifier98 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Generalization97"):
                opp_val = getattr(old_value, "uml_Generalization97", None)
                if opp_val == self:
                    setattr(old_value, "uml_Generalization97", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Generalization97"):
                opp_val = getattr(value, "uml_Generalization97", None)
                setattr(value, "uml_Generalization97", self)

    @property
    def Classifier(self):
        return self.__Classifier

    @Classifier.setter
    def Classifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Classifier__Classifier", None)
        self.__Classifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "feature"):
                opp_val = getattr(old_value, "feature", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "feature"):
                opp_val = getattr(value, "feature", None)
                if opp_val is None:
                    setattr(value, "feature", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml_Classifier(self):
        return self.__uml_Classifier

    @uml_Classifier.setter
    def uml_Classifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Classifier__uml_Classifier", None)
        self.__uml_Classifier = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_NamedElement54"):
                    opp_val = getattr(item, "uml_NamedElement54", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_NamedElement54", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_NamedElement54"):
                    opp_val = getattr(item, "uml_NamedElement54", None)
                    
                    setattr(item, "uml_NamedElement54", self)
                    

    @property
    def uml_Classifier63(self):
        return self.__uml_Classifier63

    @uml_Classifier63.setter
    def uml_Classifier63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Classifier__uml_Classifier63", None)
        self.__uml_Classifier63 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_Property64"):
                    opp_val = getattr(item, "uml_Property64", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_Property64", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_Property64"):
                    opp_val = getattr(item, "uml_Property64", None)
                    
                    setattr(item, "uml_Property64", self)
                    

    @property
    def uml_Classifier55(self):
        return self.__uml_Classifier55

    @uml_Classifier55.setter
    def uml_Classifier55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Classifier__uml_Classifier55", None)
        self.__uml_Classifier55 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_Classifier57"):
                    opp_val = getattr(item, "uml_Classifier57", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_Classifier57", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_Classifier57"):
                    opp_val = getattr(item, "uml_Classifier57", None)
                    
                    setattr(item, "uml_Classifier57", self)
                    

    @property
    def uml_Classifier58(self):
        return self.__uml_Classifier58

    @uml_Classifier58.setter
    def uml_Classifier58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Classifier__uml_Classifier58", None)
        self.__uml_Classifier58 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_Classifier60"):
                    opp_val = getattr(item, "uml_Classifier60", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_Classifier60", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_Classifier60"):
                    opp_val = getattr(item, "uml_Classifier60", None)
                    
                    setattr(item, "uml_Classifier60", self)
                    

class uml_Substitution(Realization):

    pass
class uml_Property:

    def __init__(self, name: str, uml_Property: "uml_Association" = None, uml_Property45: "uml_Association" = None, uml_Property51: "uml_Association" = None, uml_Property64: "uml_Classifier" = None, uml_Property74: "uml_Class" = None, uml_Property93: "uml_Class" = None):
        self.name = name
        self.uml_Property = uml_Property
        self.uml_Property45 = uml_Property45
        self.uml_Property51 = uml_Property51
        self.uml_Property64 = uml_Property64
        self.uml_Property74 = uml_Property74
        self.uml_Property93 = uml_Property93
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def uml_Property(self):
        return self.__uml_Property

    @uml_Property.setter
    def uml_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Property__uml_Property", None)
        self.__uml_Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Association"):
                opp_val = getattr(old_value, "uml_Association", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Association"):
                opp_val = getattr(value, "uml_Association", None)
                if opp_val is None:
                    setattr(value, "uml_Association", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml_Property64(self):
        return self.__uml_Property64

    @uml_Property64.setter
    def uml_Property64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Property__uml_Property64", None)
        self.__uml_Property64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Classifier63"):
                opp_val = getattr(old_value, "uml_Classifier63", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Classifier63"):
                opp_val = getattr(value, "uml_Classifier63", None)
                if opp_val is None:
                    setattr(value, "uml_Classifier63", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml_Property74(self):
        return self.__uml_Property74

    @uml_Property74.setter
    def uml_Property74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Property__uml_Property74", None)
        self.__uml_Property74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Class"):
                opp_val = getattr(old_value, "uml_Class", None)
                if opp_val == self:
                    setattr(old_value, "uml_Class", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Class"):
                opp_val = getattr(value, "uml_Class", None)
                setattr(value, "uml_Class", self)

    @property
    def uml_Property93(self):
        return self.__uml_Property93

    @uml_Property93.setter
    def uml_Property93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Property__uml_Property93", None)
        self.__uml_Property93 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Class92"):
                opp_val = getattr(old_value, "uml_Class92", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Class92"):
                opp_val = getattr(value, "uml_Class92", None)
                if opp_val is None:
                    setattr(value, "uml_Class92", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml_Property51(self):
        return self.__uml_Property51

    @uml_Property51.setter
    def uml_Property51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Property__uml_Property51", None)
        self.__uml_Property51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Association50"):
                opp_val = getattr(old_value, "uml_Association50", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Association50"):
                opp_val = getattr(value, "uml_Association50", None)
                if opp_val is None:
                    setattr(value, "uml_Association50", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml_Property45(self):
        return self.__uml_Property45

    @uml_Property45.setter
    def uml_Property45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Property__uml_Property45", None)
        self.__uml_Property45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Association44"):
                opp_val = getattr(old_value, "uml_Association44", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Association44"):
                opp_val = getattr(value, "uml_Association44", None)
                if opp_val is None:
                    setattr(value, "uml_Association44", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Classifier:

    pass
class uml_Class(Classifier):

    def __init__(self, name: str, isActive: str, uml_Class: "uml_Property" = None, Class: "uml_Operation" = None, uml_Class95: set["uml_Generalization"] = None, uml_Class85: set["uml_Classifier"] = None, class: set["uml_Operation"] = None, uml_Class90: "uml_Class" = None, uml_Class88: set["uml_Class"] = None, uml_Class92: set["uml_Property"] = None):
        self.name = name
        self.isActive = isActive
        self.uml_Class = uml_Class
        self.Class = Class
        self.uml_Class95 = uml_Class95 if uml_Class95 is not None else set()
        self.uml_Class85 = uml_Class85 if uml_Class85 is not None else set()
        self.class = class if class is not None else set()
        self.uml_Class90 = uml_Class90
        self.uml_Class88 = uml_Class88 if uml_Class88 is not None else set()
        self.uml_Class92 = uml_Class92 if uml_Class92 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def isActive(self) -> str:
        return self.__isActive

    @isActive.setter
    def isActive(self, isActive: str):
        self.__isActive = isActive

    @property
    def uml_Class88(self):
        return self.__uml_Class88

    @uml_Class88.setter
    def uml_Class88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Class__uml_Class88", None)
        self.__uml_Class88 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_Class90"):
                    opp_val = getattr(item, "uml_Class90", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_Class90", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_Class90"):
                    opp_val = getattr(item, "uml_Class90", None)
                    
                    setattr(item, "uml_Class90", self)
                    

    @property
    def class(self):
        return self.__class

    @class.setter
    def class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Class__class", None)
        self.__class = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Operation"):
                    opp_val = getattr(item, "Operation", None)
                    
                    if opp_val == self:
                        setattr(item, "Operation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Operation"):
                    opp_val = getattr(item, "Operation", None)
                    
                    setattr(item, "Operation", self)
                    

    @property
    def uml_Class92(self):
        return self.__uml_Class92

    @uml_Class92.setter
    def uml_Class92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Class__uml_Class92", None)
        self.__uml_Class92 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_Property93"):
                    opp_val = getattr(item, "uml_Property93", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_Property93", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_Property93"):
                    opp_val = getattr(item, "uml_Property93", None)
                    
                    setattr(item, "uml_Property93", self)
                    

    @property
    def uml_Class95(self):
        return self.__uml_Class95

    @uml_Class95.setter
    def uml_Class95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Class__uml_Class95", None)
        self.__uml_Class95 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_Generalization"):
                    opp_val = getattr(item, "uml_Generalization", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_Generalization", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_Generalization"):
                    opp_val = getattr(item, "uml_Generalization", None)
                    
                    setattr(item, "uml_Generalization", self)
                    

    @property
    def uml_Class(self):
        return self.__uml_Class

    @uml_Class.setter
    def uml_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Class__uml_Class", None)
        self.__uml_Class = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Property74"):
                opp_val = getattr(old_value, "uml_Property74", None)
                if opp_val == self:
                    setattr(old_value, "uml_Property74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Property74"):
                opp_val = getattr(value, "uml_Property74", None)
                setattr(value, "uml_Property74", self)

    @property
    def Class(self):
        return self.__Class

    @Class.setter
    def Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Class__Class", None)
        self.__Class = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownedOperation"):
                opp_val = getattr(old_value, "ownedOperation", None)
                if opp_val == self:
                    setattr(old_value, "ownedOperation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedOperation"):
                opp_val = getattr(value, "ownedOperation", None)
                setattr(value, "ownedOperation", self)

    @property
    def uml_Class90(self):
        return self.__uml_Class90

    @uml_Class90.setter
    def uml_Class90(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Class__uml_Class90", None)
        self.__uml_Class90 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Class88"):
                opp_val = getattr(old_value, "uml_Class88", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Class88"):
                opp_val = getattr(value, "uml_Class88", None)
                if opp_val is None:
                    setattr(value, "uml_Class88", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml_Class85(self):
        return self.__uml_Class85

    @uml_Class85.setter
    def uml_Class85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Class__uml_Class85", None)
        self.__uml_Class85 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_Classifier86"):
                    opp_val = getattr(item, "uml_Classifier86", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_Classifier86", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_Classifier86"):
                    opp_val = getattr(item, "uml_Classifier86", None)
                    
                    setattr(item, "uml_Classifier86", self)
                    

class TypedElement:

    pass
class NamedElement:

    pass
class uml_TypedElement(NamedElement):

    pass
class Relationship:

    pass
class uml_Association(Relationship, Classifier):

    def __init__(self, isDerived: str, uml_Association47: set["uml_Type"] = None, uml_Association: set["uml_Property"] = None, uml_Association44: set["uml_Property"] = None, uml_Association50: set["uml_Property"] = None):
        self.isDerived = isDerived
        self.uml_Association47 = uml_Association47 if uml_Association47 is not None else set()
        self.uml_Association = uml_Association if uml_Association is not None else set()
        self.uml_Association44 = uml_Association44 if uml_Association44 is not None else set()
        self.uml_Association50 = uml_Association50 if uml_Association50 is not None else set()
        
    @property
    def isDerived(self) -> str:
        return self.__isDerived

    @isDerived.setter
    def isDerived(self, isDerived: str):
        self.__isDerived = isDerived

    @property
    def uml_Association44(self):
        return self.__uml_Association44

    @uml_Association44.setter
    def uml_Association44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Association__uml_Association44", None)
        self.__uml_Association44 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_Property45"):
                    opp_val = getattr(item, "uml_Property45", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_Property45", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_Property45"):
                    opp_val = getattr(item, "uml_Property45", None)
                    
                    setattr(item, "uml_Property45", self)
                    

    @property
    def uml_Association50(self):
        return self.__uml_Association50

    @uml_Association50.setter
    def uml_Association50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Association__uml_Association50", None)
        self.__uml_Association50 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_Property51"):
                    opp_val = getattr(item, "uml_Property51", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_Property51", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_Property51"):
                    opp_val = getattr(item, "uml_Property51", None)
                    
                    setattr(item, "uml_Property51", self)
                    

    @property
    def uml_Association(self):
        return self.__uml_Association

    @uml_Association.setter
    def uml_Association(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Association__uml_Association", None)
        self.__uml_Association = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_Property"):
                    opp_val = getattr(item, "uml_Property", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_Property", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_Property"):
                    opp_val = getattr(item, "uml_Property", None)
                    
                    setattr(item, "uml_Property", self)
                    

    @property
    def uml_Association47(self):
        return self.__uml_Association47

    @uml_Association47.setter
    def uml_Association47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Association__uml_Association47", None)
        self.__uml_Association47 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_Type48"):
                    opp_val = getattr(item, "uml_Type48", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_Type48", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_Type48"):
                    opp_val = getattr(item, "uml_Type48", None)
                    
                    setattr(item, "uml_Type48", self)
                    

class uml_DirectedRelationship(Relationship):

    pass
class DirectedRelationship:

    pass
class uml_PackageImport(DirectedRelationship):

    def __init__(self, visibility: str, PackageImport: "uml_Namespace" = None, packageImport: "uml_Namespace" = None, uml_PackageImport: "uml_Package" = None):
        self.visibility = visibility
        self.PackageImport = PackageImport
        self.packageImport = packageImport
        self.uml_PackageImport = uml_PackageImport
        
    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def PackageImport(self):
        return self.__PackageImport

    @PackageImport.setter
    def PackageImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_PackageImport__PackageImport", None)
        self.__PackageImport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "importingNamespace24"):
                opp_val = getattr(old_value, "importingNamespace24", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "importingNamespace24"):
                opp_val = getattr(value, "importingNamespace24", None)
                if opp_val is None:
                    setattr(value, "importingNamespace24", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml_PackageImport(self):
        return self.__uml_PackageImport

    @uml_PackageImport.setter
    def uml_PackageImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_PackageImport__uml_PackageImport", None)
        self.__uml_PackageImport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Package37"):
                opp_val = getattr(old_value, "uml_Package37", None)
                if opp_val == self:
                    setattr(old_value, "uml_Package37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Package37"):
                opp_val = getattr(value, "uml_Package37", None)
                setattr(value, "uml_Package37", self)

    @property
    def packageImport(self):
        return self.__packageImport

    @packageImport.setter
    def packageImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_PackageImport__packageImport", None)
        self.__packageImport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Namespace39"):
                opp_val = getattr(old_value, "Namespace39", None)
                if opp_val == self:
                    setattr(old_value, "Namespace39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Namespace39"):
                opp_val = getattr(value, "Namespace39", None)
                setattr(value, "Namespace39", self)

class uml_Generalization(DirectedRelationship):

    def __init__(self, isSubstitutable: str, uml_Generalization: "uml_Class" = None, uml_Generalization97: "uml_Classifier" = None, uml_Generalization100: "uml_Classifier" = None):
        self.isSubstitutable = isSubstitutable
        self.uml_Generalization = uml_Generalization
        self.uml_Generalization97 = uml_Generalization97
        self.uml_Generalization100 = uml_Generalization100
        
    @property
    def isSubstitutable(self) -> str:
        return self.__isSubstitutable

    @isSubstitutable.setter
    def isSubstitutable(self, isSubstitutable: str):
        self.__isSubstitutable = isSubstitutable

    @property
    def uml_Generalization(self):
        return self.__uml_Generalization

    @uml_Generalization.setter
    def uml_Generalization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Generalization__uml_Generalization", None)
        self.__uml_Generalization = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Class95"):
                opp_val = getattr(old_value, "uml_Class95", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Class95"):
                opp_val = getattr(value, "uml_Class95", None)
                if opp_val is None:
                    setattr(value, "uml_Class95", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml_Generalization100(self):
        return self.__uml_Generalization100

    @uml_Generalization100.setter
    def uml_Generalization100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Generalization__uml_Generalization100", None)
        self.__uml_Generalization100 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Classifier101"):
                opp_val = getattr(old_value, "uml_Classifier101", None)
                if opp_val == self:
                    setattr(old_value, "uml_Classifier101", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Classifier101"):
                opp_val = getattr(value, "uml_Classifier101", None)
                setattr(value, "uml_Classifier101", self)

    @property
    def uml_Generalization97(self):
        return self.__uml_Generalization97

    @uml_Generalization97.setter
    def uml_Generalization97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Generalization__uml_Generalization97", None)
        self.__uml_Generalization97 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Classifier98"):
                opp_val = getattr(old_value, "uml_Classifier98", None)
                if opp_val == self:
                    setattr(old_value, "uml_Classifier98", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Classifier98"):
                opp_val = getattr(value, "uml_Classifier98", None)
                setattr(value, "uml_Classifier98", self)

class uml_ElementImport(DirectedRelationship):

    def __init__(self, visibility: str, alias: str, ElementImport: "uml_Namespace" = None, uml_ElementImport: "uml_PackageableElement" = None, elementImport: "uml_Namespace" = None):
        self.visibility = visibility
        self.alias = alias
        self.ElementImport = ElementImport
        self.uml_ElementImport = uml_ElementImport
        self.elementImport = elementImport
        
    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def alias(self) -> str:
        return self.__alias

    @alias.setter
    def alias(self, alias: str):
        self.__alias = alias

    @property
    def ElementImport(self):
        return self.__ElementImport

    @ElementImport.setter
    def ElementImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_ElementImport__ElementImport", None)
        self.__ElementImport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "importingNamespace"):
                opp_val = getattr(old_value, "importingNamespace", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "importingNamespace"):
                opp_val = getattr(value, "importingNamespace", None)
                if opp_val is None:
                    setattr(value, "importingNamespace", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml_ElementImport(self):
        return self.__uml_ElementImport

    @uml_ElementImport.setter
    def uml_ElementImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_ElementImport__uml_ElementImport", None)
        self.__uml_ElementImport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_PackageableElement33"):
                opp_val = getattr(old_value, "uml_PackageableElement33", None)
                if opp_val == self:
                    setattr(old_value, "uml_PackageableElement33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_PackageableElement33"):
                opp_val = getattr(value, "uml_PackageableElement33", None)
                setattr(value, "uml_PackageableElement33", self)

    @property
    def elementImport(self):
        return self.__elementImport

    @elementImport.setter
    def elementImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_ElementImport__elementImport", None)
        self.__elementImport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Namespace35"):
                opp_val = getattr(old_value, "Namespace35", None)
                if opp_val == self:
                    setattr(old_value, "Namespace35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Namespace35"):
                opp_val = getattr(value, "Namespace35", None)
                setattr(value, "Namespace35", self)

class uml_Namespace(NamedElement):

    pass
class PackageableElement:

    pass
class uml_Dependency(DirectedRelationship, PackageableElement):

    pass
class uml_Type(PackageableElement):

    pass
class uml_ValueSpecification(PackageableElement, TypedElement):

    pass
class uml_Package(PackageableElement):

    def __init__(self, name: str, uml_Package: set["uml_PackageableElement"] = None, package: set["uml_Type"] = None, uml_Package37: "uml_PackageImport" = None, Package: "uml_Type" = None):
        self.name = name
        self.uml_Package = uml_Package if uml_Package is not None else set()
        self.package = package if package is not None else set()
        self.uml_Package37 = uml_Package37
        self.Package = Package
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def uml_Package37(self):
        return self.__uml_Package37

    @uml_Package37.setter
    def uml_Package37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Package__uml_Package37", None)
        self.__uml_Package37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_PackageImport"):
                opp_val = getattr(old_value, "uml_PackageImport", None)
                if opp_val == self:
                    setattr(old_value, "uml_PackageImport", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_PackageImport"):
                opp_val = getattr(value, "uml_PackageImport", None)
                setattr(value, "uml_PackageImport", self)

    @property
    def package(self):
        return self.__package

    @package.setter
    def package(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Package__package", None)
        self.__package = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Type"):
                    opp_val = getattr(item, "Type", None)
                    
                    if opp_val == self:
                        setattr(item, "Type", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Type"):
                    opp_val = getattr(item, "Type", None)
                    
                    setattr(item, "Type", self)
                    

    @property
    def uml_Package(self):
        return self.__uml_Package

    @uml_Package.setter
    def uml_Package(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Package__uml_Package", None)
        self.__uml_Package = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_PackageableElement"):
                    opp_val = getattr(item, "uml_PackageableElement", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_PackageableElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_PackageableElement"):
                    opp_val = getattr(item, "uml_PackageableElement", None)
                    
                    setattr(item, "uml_PackageableElement", self)
                    

    @property
    def Package(self):
        return self.__Package

    @Package.setter
    def Package(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Package__Package", None)
        self.__Package = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownedType"):
                opp_val = getattr(old_value, "ownedType", None)
                if opp_val == self:
                    setattr(old_value, "ownedType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedType"):
                opp_val = getattr(value, "ownedType", None)
                setattr(value, "ownedType", self)

class uml_PackageableElement(ABC):

    pass
class uml_Element(ABC):

    pass
class Element:

    pass
class uml_NamedElement(Element):

    def __init__(self, name: str, visibility: str, qualifiedName: str, ownedMember: "uml_Namespace" = None, client: set["uml_Dependency"] = None, uml_NamedElement: "uml_Dependency" = None, NamedElement: "uml_Dependency" = None, uml_NamedElement26: "uml_Namespace" = None, NamedElement31: "uml_Namespace" = None, uml_NamedElement54: "uml_Classifier" = None):
        self.name = name
        self.visibility = visibility
        self.qualifiedName = qualifiedName
        self.ownedMember = ownedMember
        self.client = client if client is not None else set()
        self.uml_NamedElement = uml_NamedElement
        self.NamedElement = NamedElement
        self.uml_NamedElement26 = uml_NamedElement26
        self.NamedElement31 = NamedElement31
        self.uml_NamedElement54 = uml_NamedElement54
        
    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def qualifiedName(self) -> str:
        return self.__qualifiedName

    @qualifiedName.setter
    def qualifiedName(self, qualifiedName: str):
        self.__qualifiedName = qualifiedName

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def uml_NamedElement(self):
        return self.__uml_NamedElement

    @uml_NamedElement.setter
    def uml_NamedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_NamedElement__uml_NamedElement", None)
        self.__uml_NamedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Dependency"):
                opp_val = getattr(old_value, "uml_Dependency", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Dependency"):
                opp_val = getattr(value, "uml_Dependency", None)
                if opp_val is None:
                    setattr(value, "uml_Dependency", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml_NamedElement26(self):
        return self.__uml_NamedElement26

    @uml_NamedElement26.setter
    def uml_NamedElement26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_NamedElement__uml_NamedElement26", None)
        self.__uml_NamedElement26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Namespace"):
                opp_val = getattr(old_value, "uml_Namespace", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Namespace"):
                opp_val = getattr(value, "uml_Namespace", None)
                if opp_val is None:
                    setattr(value, "uml_Namespace", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def client(self):
        return self.__client

    @client.setter
    def client(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_NamedElement__client", None)
        self.__client = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Dependency"):
                    opp_val = getattr(item, "Dependency", None)
                    
                    if opp_val == self:
                        setattr(item, "Dependency", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Dependency"):
                    opp_val = getattr(item, "Dependency", None)
                    
                    setattr(item, "Dependency", self)
                    

    @property
    def NamedElement(self):
        return self.__NamedElement

    @NamedElement.setter
    def NamedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_NamedElement__NamedElement", None)
        self.__NamedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "clientDependency"):
                opp_val = getattr(old_value, "clientDependency", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "clientDependency"):
                opp_val = getattr(value, "clientDependency", None)
                if opp_val is None:
                    setattr(value, "clientDependency", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ownedMember(self):
        return self.__ownedMember

    @ownedMember.setter
    def ownedMember(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_NamedElement__ownedMember", None)
        self.__ownedMember = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Namespace"):
                opp_val = getattr(old_value, "Namespace", None)
                if opp_val == self:
                    setattr(old_value, "Namespace", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Namespace"):
                opp_val = getattr(value, "Namespace", None)
                setattr(value, "Namespace", self)

    @property
    def uml_NamedElement54(self):
        return self.__uml_NamedElement54

    @uml_NamedElement54.setter
    def uml_NamedElement54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_NamedElement__uml_NamedElement54", None)
        self.__uml_NamedElement54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Classifier"):
                opp_val = getattr(old_value, "uml_Classifier", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Classifier"):
                opp_val = getattr(value, "uml_Classifier", None)
                if opp_val is None:
                    setattr(value, "uml_Classifier", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def NamedElement31(self):
        return self.__NamedElement31

    @NamedElement31.setter
    def NamedElement31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_NamedElement__NamedElement31", None)
        self.__NamedElement31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "namespace"):
                opp_val = getattr(old_value, "namespace", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "namespace"):
                opp_val = getattr(value, "namespace", None)
                if opp_val is None:
                    setattr(value, "namespace", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class uml_Relationship(Element):

    pass
class uml_Comment(Element):

    def __init__(self, body: str, uml_Comment: set["uml_Element"] = None, uml_Comment8: "uml_Element" = None):
        self.body = body
        self.uml_Comment = uml_Comment if uml_Comment is not None else set()
        self.uml_Comment8 = uml_Comment8
        
    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

    @property
    def uml_Comment(self):
        return self.__uml_Comment

    @uml_Comment.setter
    def uml_Comment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Comment__uml_Comment", None)
        self.__uml_Comment = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_Element"):
                    opp_val = getattr(item, "uml_Element", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_Element", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_Element"):
                    opp_val = getattr(item, "uml_Element", None)
                    
                    setattr(item, "uml_Element", self)
                    

    @property
    def uml_Comment8(self):
        return self.__uml_Comment8

    @uml_Comment8.setter
    def uml_Comment8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Comment__uml_Comment8", None)
        self.__uml_Comment8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Element7"):
                opp_val = getattr(old_value, "uml_Element7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Element7"):
                opp_val = getattr(value, "uml_Element7", None)
                if opp_val is None:
                    setattr(value, "uml_Element7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
