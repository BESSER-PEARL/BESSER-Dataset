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
class ParameterDirectionKind(Enum):
    in = "in"
    inout = "inout"
    out = "out"
    return = "return"
class VisibilityKind(Enum):
    public = "public"
    private = "private"
    protected = "protected"
    package = "package"


############################################
# Definition of Classes
############################################

class Class:

    pass
class Association:

    pass
class uml2CD_AssociationClass(Association, Class):

    pass
class Realization:

    pass
class uml2CD_InterfaceRealization(Realization):

    pass
class Abstraction:

    pass
class uml2CD_Realization(Abstraction):

    pass
class Dependency:

    pass
class uml2CD_Usage(Dependency):

    pass
class uml2CD_Abstraction(Dependency):

    pass
class ValueSpecification:

    pass
class uml2CD_EnumerationLiteral(ValueSpecification):

    pass
class DataType:

    pass
class uml2CD_Enumeration(DataType):

    pass
class uml2CD_PrimitiveType(DataType):

    pass
class StructuralFeature:

    pass
class Classifier:

    pass
class uml2CD_Interface(Classifier):

    pass
class uml2CD_DataType(Classifier):

    pass
class BehavioralFeature:

    pass
class uml2CD_Operation(BehavioralFeature):

    def __init__(self, isQuery: bool, uml2CD_Operation: "uml2CD_Operation" = None, uml2CD_Operation76: set["uml2CD_Operation"] = None, ownedOperation: "uml2CD_Class" = None, Operation: "uml2CD_Class" = None):
        self.isQuery = isQuery
        self.uml2CD_Operation = uml2CD_Operation
        self.uml2CD_Operation76 = uml2CD_Operation76 if uml2CD_Operation76 is not None else set()
        self.ownedOperation = ownedOperation
        self.Operation = Operation
        
    @property
    def isQuery(self) -> bool:
        return self.__isQuery

    @isQuery.setter
    def isQuery(self, isQuery: bool):
        self.__isQuery = isQuery

    @property
    def ownedOperation(self):
        return self.__ownedOperation

    @ownedOperation.setter
    def ownedOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2CD_Operation__ownedOperation", None)
        self.__ownedOperation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Class79"):
                opp_val = getattr(old_value, "Class79", None)
                if opp_val == self:
                    setattr(old_value, "Class79", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Class79"):
                opp_val = getattr(value, "Class79", None)
                setattr(value, "Class79", self)

    @property
    def uml2CD_Operation76(self):
        return self.__uml2CD_Operation76

    @uml2CD_Operation76.setter
    def uml2CD_Operation76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2CD_Operation__uml2CD_Operation76", None)
        self.__uml2CD_Operation76 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml2CD_Operation"):
                    opp_val = getattr(item, "uml2CD_Operation", None)
                    
                    if opp_val == self:
                        setattr(item, "uml2CD_Operation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml2CD_Operation"):
                    opp_val = getattr(item, "uml2CD_Operation", None)
                    
                    setattr(item, "uml2CD_Operation", self)
                    

    @property
    def uml2CD_Operation(self):
        return self.__uml2CD_Operation

    @uml2CD_Operation.setter
    def uml2CD_Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2CD_Operation__uml2CD_Operation", None)
        self.__uml2CD_Operation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml2CD_Operation76"):
                opp_val = getattr(old_value, "uml2CD_Operation76", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml2CD_Operation76"):
                opp_val = getattr(value, "uml2CD_Operation76", None)
                if opp_val is None:
                    setattr(value, "uml2CD_Operation76", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Operation(self):
        return self.__Operation

    @Operation.setter
    def Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2CD_Operation__Operation", None)
        self.__Operation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Class86"):
                opp_val = getattr(old_value, "Class86", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Class86"):
                opp_val = getattr(value, "Class86", None)
                if opp_val is None:
                    setattr(value, "Class86", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class MultiplicityElement:

    pass
class Feature:

    pass
class uml2CD_Substitution(Realization):

    pass
class uml2CD_Class(Classifier):

    pass
class uml2CD_Feature(ABC):

    pass
class Typpee:

    pass
class uml2CD_GeneralizationSet:

    def __init__(self, isCovering: bool, isDisjoint: bool, GeneralizationSet: "uml2CD_Generalization" = None, GeneralizationSet65: "uml2CD_Classifier" = None, generalizationSet: set["uml2CD_Generalization"] = None, powertypeExtent: "uml2CD_Classifier" = None):
        self.isCovering = isCovering
        self.isDisjoint = isDisjoint
        self.GeneralizationSet = GeneralizationSet
        self.GeneralizationSet65 = GeneralizationSet65
        self.generalizationSet = generalizationSet if generalizationSet is not None else set()
        self.powertypeExtent = powertypeExtent
        
    @property
    def isCovering(self) -> bool:
        return self.__isCovering

    @isCovering.setter
    def isCovering(self, isCovering: bool):
        self.__isCovering = isCovering

    @property
    def isDisjoint(self) -> bool:
        return self.__isDisjoint

    @isDisjoint.setter
    def isDisjoint(self, isDisjoint: bool):
        self.__isDisjoint = isDisjoint

    @property
    def GeneralizationSet(self):
        return self.__GeneralizationSet

    @GeneralizationSet.setter
    def GeneralizationSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2CD_GeneralizationSet__GeneralizationSet", None)
        self.__GeneralizationSet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "generalization60"):
                opp_val = getattr(old_value, "generalization60", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "generalization60"):
                opp_val = getattr(value, "generalization60", None)
                if opp_val is None:
                    setattr(value, "generalization60", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def generalizationSet(self):
        return self.__generalizationSet

    @generalizationSet.setter
    def generalizationSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2CD_GeneralizationSet__generalizationSet", None)
        self.__generalizationSet = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Generalization125"):
                    opp_val = getattr(item, "Generalization125", None)
                    
                    if opp_val == self:
                        setattr(item, "Generalization125", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Generalization125"):
                    opp_val = getattr(item, "Generalization125", None)
                    
                    setattr(item, "Generalization125", self)
                    

    @property
    def GeneralizationSet65(self):
        return self.__GeneralizationSet65

    @GeneralizationSet65.setter
    def GeneralizationSet65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2CD_GeneralizationSet__GeneralizationSet65", None)
        self.__GeneralizationSet65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "powertype"):
                opp_val = getattr(old_value, "powertype", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "powertype"):
                opp_val = getattr(value, "powertype", None)
                if opp_val is None:
                    setattr(value, "powertype", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def powertypeExtent(self):
        return self.__powertypeExtent

    @powertypeExtent.setter
    def powertypeExtent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2CD_GeneralizationSet__powertypeExtent", None)
        self.__powertypeExtent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Classifier127"):
                opp_val = getattr(old_value, "Classifier127", None)
                if opp_val == self:
                    setattr(old_value, "Classifier127", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Classifier127"):
                opp_val = getattr(value, "Classifier127", None)
                setattr(value, "Classifier127", self)

class uml2CD_Property(StructuralFeature):

    pass
class TypedElement:

    pass
class uml2CD_StructuralFeature(Feature, TypedElement, MultiplicityElement):

    pass
class uml2CD_Parameter(TypedElement, MultiplicityElement):

    def __init__(self, direction: str, Parameter: "uml2CD_ValueSpecification" = None, Parameter70: "uml2CD_BehavioralFeature" = None, ownedParameter: "uml2CD_BehavioralFeature" = None, owningParameter: "uml2CD_ValueSpecification" = None):
        self.direction = direction
        self.Parameter = Parameter
        self.Parameter70 = Parameter70
        self.ownedParameter = ownedParameter
        self.owningParameter = owningParameter
        
    @property
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction

    @property
    def ownedParameter(self):
        return self.__ownedParameter

    @ownedParameter.setter
    def ownedParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2CD_Parameter__ownedParameter", None)
        self.__ownedParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BehavioralFeature"):
                opp_val = getattr(old_value, "BehavioralFeature", None)
                if opp_val == self:
                    setattr(old_value, "BehavioralFeature", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BehavioralFeature"):
                opp_val = getattr(value, "BehavioralFeature", None)
                setattr(value, "BehavioralFeature", self)

    @property
    def Parameter70(self):
        return self.__Parameter70

    @Parameter70.setter
    def Parameter70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2CD_Parameter__Parameter70", None)
        self.__Parameter70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownerFormalParam"):
                opp_val = getattr(old_value, "ownerFormalParam", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownerFormalParam"):
                opp_val = getattr(value, "ownerFormalParam", None)
                if opp_val is None:
                    setattr(value, "ownerFormalParam", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def owningParameter(self):
        return self.__owningParameter

    @owningParameter.setter
    def owningParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2CD_Parameter__owningParameter", None)
        self.__owningParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ValueSpecification75"):
                opp_val = getattr(old_value, "ValueSpecification75", None)
                if opp_val == self:
                    setattr(old_value, "ValueSpecification75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ValueSpecification75"):
                opp_val = getattr(value, "ValueSpecification75", None)
                setattr(value, "ValueSpecification75", self)

    @property
    def Parameter(self):
        return self.__Parameter

    @Parameter.setter
    def Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2CD_Parameter__Parameter", None)
        self.__Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "defaultValue"):
                opp_val = getattr(old_value, "defaultValue", None)
                if opp_val == self:
                    setattr(old_value, "defaultValue", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "defaultValue"):
                opp_val = getattr(value, "defaultValue", None)
                setattr(value, "defaultValue", self)

class Namespace:

    pass
class uml2CD_Classifier(Typpee, Namespace):

    def __init__(self, isAbstract: bool, uml2CD_Classifier: "uml2CD_Generalization" = None, Classifier: "uml2CD_Generalization" = None, specific: set["uml2CD_Generalization"] = None, featuringClassifier: set["uml2CD_Feature"] = None, nestedClassifier: "uml2CD_Class" = None, powertype: set["uml2CD_GeneralizationSet"] = None, substitutingClassifier: set["uml2CD_Substitution"] = None, Classifier68: "uml2CD_Feature" = None, Classifier84: "uml2CD_Class" = None, uml2CD_Classifier117: "uml2CD_Substitution" = None, Classifier119: "uml2CD_Substitution" = None, Classifier127: "uml2CD_GeneralizationSet" = None):
        self.isAbstract = isAbstract
        self.uml2CD_Classifier = uml2CD_Classifier
        self.Classifier = Classifier
        self.specific = specific if specific is not None else set()
        self.featuringClassifier = featuringClassifier if featuringClassifier is not None else set()
        self.nestedClassifier = nestedClassifier
        self.powertype = powertype if powertype is not None else set()
        self.substitutingClassifier = substitutingClassifier if substitutingClassifier is not None else set()
        self.Classifier68 = Classifier68
        self.Classifier84 = Classifier84
        self.uml2CD_Classifier117 = uml2CD_Classifier117
        self.Classifier119 = Classifier119
        self.Classifier127 = Classifier127
        
    @property
    def isAbstract(self) -> bool:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: bool):
        self.__isAbstract = isAbstract

    @property
    def featuringClassifier(self):
        return self.__featuringClassifier

    @featuringClassifier.setter
    def featuringClassifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2CD_Classifier__featuringClassifier", None)
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
    def substitutingClassifier(self):
        return self.__substitutingClassifier

    @substitutingClassifier.setter
    def substitutingClassifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2CD_Classifier__substitutingClassifier", None)
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
    def uml2CD_Classifier117(self):
        return self.__uml2CD_Classifier117

    @uml2CD_Classifier117.setter
    def uml2CD_Classifier117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2CD_Classifier__uml2CD_Classifier117", None)
        self.__uml2CD_Classifier117 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml2CD_Substitution"):
                opp_val = getattr(old_value, "uml2CD_Substitution", None)
                if opp_val == self:
                    setattr(old_value, "uml2CD_Substitution", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml2CD_Substitution"):
                opp_val = getattr(value, "uml2CD_Substitution", None)
                setattr(value, "uml2CD_Substitution", self)

    @property
    def Classifier127(self):
        return self.__Classifier127

    @Classifier127.setter
    def Classifier127(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2CD_Classifier__Classifier127", None)
        self.__Classifier127 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "powertypeExtent"):
                opp_val = getattr(old_value, "powertypeExtent", None)
                if opp_val == self:
                    setattr(old_value, "powertypeExtent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "powertypeExtent"):
                opp_val = getattr(value, "powertypeExtent", None)
                setattr(value, "powertypeExtent", self)

    @property
    def nestedClassifier(self):
        return self.__nestedClassifier

    @nestedClassifier.setter
    def nestedClassifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2CD_Classifier__nestedClassifier", None)
        self.__nestedClassifier = value
        
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
    def Classifier(self):
        return self.__Classifier

    @Classifier.setter
    def Classifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2CD_Classifier__Classifier", None)
        self.__Classifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "generalization"):
                opp_val = getattr(old_value, "generalization", None)
                if opp_val == self:
                    setattr(old_value, "generalization", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "generalization"):
                opp_val = getattr(value, "generalization", None)
                setattr(value, "generalization", self)

    @property
    def Classifier84(self):
        return self.__Classifier84

    @Classifier84.setter
    def Classifier84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2CD_Classifier__Classifier84", None)
        self.__Classifier84 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Class83"):
                opp_val = getattr(old_value, "Class83", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Class83"):
                opp_val = getattr(value, "Class83", None)
                if opp_val is None:
                    setattr(value, "Class83", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Classifier68(self):
        return self.__Classifier68

    @Classifier68.setter
    def Classifier68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2CD_Classifier__Classifier68", None)
        self.__Classifier68 = value
        
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
    def Classifier119(self):
        return self.__Classifier119

    @Classifier119.setter
    def Classifier119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2CD_Classifier__Classifier119", None)
        self.__Classifier119 = value
        
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
    def uml2CD_Classifier(self):
        return self.__uml2CD_Classifier

    @uml2CD_Classifier.setter
    def uml2CD_Classifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2CD_Classifier__uml2CD_Classifier", None)
        self.__uml2CD_Classifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml2CD_Generalization"):
                opp_val = getattr(old_value, "uml2CD_Generalization", None)
                if opp_val == self:
                    setattr(old_value, "uml2CD_Generalization", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml2CD_Generalization"):
                opp_val = getattr(value, "uml2CD_Generalization", None)
                setattr(value, "uml2CD_Generalization", self)

    @property
    def specific(self):
        return self.__specific

    @specific.setter
    def specific(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2CD_Classifier__specific", None)
        self.__specific = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Generalization"):
                    opp_val = getattr(item, "Generalization", None)
                    
                    if opp_val == self:
                        setattr(item, "Generalization", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Generalization"):
                    opp_val = getattr(item, "Generalization", None)
                    
                    setattr(item, "Generalization", self)
                    

    @property
    def powertype(self):
        return self.__powertype

    @powertype.setter
    def powertype(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2CD_Classifier__powertype", None)
        self.__powertype = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GeneralizationSet65"):
                    opp_val = getattr(item, "GeneralizationSet65", None)
                    
                    if opp_val == self:
                        setattr(item, "GeneralizationSet65", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GeneralizationSet65"):
                    opp_val = getattr(item, "GeneralizationSet65", None)
                    
                    setattr(item, "GeneralizationSet65", self)
                    

class uml2CD_BehavioralFeature(Feature, Namespace):

    pass
class PackageableElement:

    pass
class uml2CD_Typpee(PackageableElement):

    pass
class uml2CD_ValueSpecification(PackageableElement, TypedElement):

    pass
class DirectRelationship:

    pass
class uml2CD_PackageMerge(DirectRelationship):

    pass
class uml2CD_Generalization(DirectRelationship):

    def __init__(self, isSubstitutable: bool, uml2CD_Generalization: "uml2CD_Classifier" = None, generalization: "uml2CD_Classifier" = None, generalization60: set["uml2CD_GeneralizationSet"] = None, Generalization: "uml2CD_Classifier" = None, Generalization125: "uml2CD_GeneralizationSet" = None):
        self.isSubstitutable = isSubstitutable
        self.uml2CD_Generalization = uml2CD_Generalization
        self.generalization = generalization
        self.generalization60 = generalization60 if generalization60 is not None else set()
        self.Generalization = Generalization
        self.Generalization125 = Generalization125
        
    @property
    def isSubstitutable(self) -> bool:
        return self.__isSubstitutable

    @isSubstitutable.setter
    def isSubstitutable(self, isSubstitutable: bool):
        self.__isSubstitutable = isSubstitutable

    @property
    def Generalization(self):
        return self.__Generalization

    @Generalization.setter
    def Generalization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2CD_Generalization__Generalization", None)
        self.__Generalization = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "specific"):
                opp_val = getattr(old_value, "specific", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "specific"):
                opp_val = getattr(value, "specific", None)
                if opp_val is None:
                    setattr(value, "specific", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Generalization125(self):
        return self.__Generalization125

    @Generalization125.setter
    def Generalization125(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2CD_Generalization__Generalization125", None)
        self.__Generalization125 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "generalizationSet"):
                opp_val = getattr(old_value, "generalizationSet", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "generalizationSet"):
                opp_val = getattr(value, "generalizationSet", None)
                if opp_val is None:
                    setattr(value, "generalizationSet", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def generalization60(self):
        return self.__generalization60

    @generalization60.setter
    def generalization60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2CD_Generalization__generalization60", None)
        self.__generalization60 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GeneralizationSet"):
                    opp_val = getattr(item, "GeneralizationSet", None)
                    
                    if opp_val == self:
                        setattr(item, "GeneralizationSet", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GeneralizationSet"):
                    opp_val = getattr(item, "GeneralizationSet", None)
                    
                    setattr(item, "GeneralizationSet", self)
                    

    @property
    def uml2CD_Generalization(self):
        return self.__uml2CD_Generalization

    @uml2CD_Generalization.setter
    def uml2CD_Generalization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2CD_Generalization__uml2CD_Generalization", None)
        self.__uml2CD_Generalization = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml2CD_Classifier"):
                opp_val = getattr(old_value, "uml2CD_Classifier", None)
                if opp_val == self:
                    setattr(old_value, "uml2CD_Classifier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml2CD_Classifier"):
                opp_val = getattr(value, "uml2CD_Classifier", None)
                setattr(value, "uml2CD_Classifier", self)

    @property
    def generalization(self):
        return self.__generalization

    @generalization.setter
    def generalization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2CD_Generalization__generalization", None)
        self.__generalization = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Classifier"):
                opp_val = getattr(old_value, "Classifier", None)
                if opp_val == self:
                    setattr(old_value, "Classifier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Classifier"):
                opp_val = getattr(value, "Classifier", None)
                setattr(value, "Classifier", self)

class uml2CD_Constraint(PackageableElement):

    pass
class uml2CD_ElementImport(DirectRelationship):

    def __init__(self, visibility: str, ElementImport: "uml2CD_Namespace" = None, uml2CD_ElementImport: "uml2CD_PackageableElement" = None, elementImport: "uml2CD_Namespace" = None):
        self.visibility = visibility
        self.ElementImport = ElementImport
        self.uml2CD_ElementImport = uml2CD_ElementImport
        self.elementImport = elementImport
        
    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def elementImport(self):
        return self.__elementImport

    @elementImport.setter
    def elementImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2CD_ElementImport__elementImport", None)
        self.__elementImport = value
        
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
    def ElementImport(self):
        return self.__ElementImport

    @ElementImport.setter
    def ElementImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2CD_ElementImport__ElementImport", None)
        self.__ElementImport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "importingNamespace23"):
                opp_val = getattr(old_value, "importingNamespace23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "importingNamespace23"):
                opp_val = getattr(value, "importingNamespace23", None)
                if opp_val is None:
                    setattr(value, "importingNamespace23", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml2CD_ElementImport(self):
        return self.__uml2CD_ElementImport

    @uml2CD_ElementImport.setter
    def uml2CD_ElementImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2CD_ElementImport__uml2CD_ElementImport", None)
        self.__uml2CD_ElementImport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml2CD_PackageableElement26"):
                opp_val = getattr(old_value, "uml2CD_PackageableElement26", None)
                if opp_val == self:
                    setattr(old_value, "uml2CD_PackageableElement26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml2CD_PackageableElement26"):
                opp_val = getattr(value, "uml2CD_PackageableElement26", None)
                setattr(value, "uml2CD_PackageableElement26", self)

class uml2CD_PackageImport(DirectRelationship):

    def __init__(self, visibility: str, PackageImport: "uml2CD_Namespace" = None, uml2CD_PackageImport: "uml2CD_Package" = None, packageImport: "uml2CD_Namespace" = None):
        self.visibility = visibility
        self.PackageImport = PackageImport
        self.uml2CD_PackageImport = uml2CD_PackageImport
        self.packageImport = packageImport
        
    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def uml2CD_PackageImport(self):
        return self.__uml2CD_PackageImport

    @uml2CD_PackageImport.setter
    def uml2CD_PackageImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2CD_PackageImport__uml2CD_PackageImport", None)
        self.__uml2CD_PackageImport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml2CD_Package"):
                opp_val = getattr(old_value, "uml2CD_Package", None)
                if opp_val == self:
                    setattr(old_value, "uml2CD_Package", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml2CD_Package"):
                opp_val = getattr(value, "uml2CD_Package", None)
                setattr(value, "uml2CD_Package", self)

    @property
    def PackageImport(self):
        return self.__PackageImport

    @PackageImport.setter
    def PackageImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2CD_PackageImport__PackageImport", None)
        self.__PackageImport = value
        
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
    def packageImport(self):
        return self.__packageImport

    @packageImport.setter
    def packageImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2CD_PackageImport__packageImport", None)
        self.__packageImport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Namespace30"):
                opp_val = getattr(old_value, "Namespace30", None)
                if opp_val == self:
                    setattr(old_value, "Namespace30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Namespace30"):
                opp_val = getattr(value, "Namespace30", None)
                setattr(value, "Namespace30", self)

class uml2CD_Package(Namespace, PackageableElement):

    pass
class uml2CD_Comment:

    pass
class NamedElement:

    pass
class uml2CD_TypedElement(NamedElement):

    pass
class uml2CD_PackageableElement(NamedElement):

    pass
class uml2CD_Dependency(PackageableElement, DirectRelationship):

    pass
class uml2CD_Namespace(NamedElement):

    pass
class Relationship:

    pass
class uml2CD_Association(Relationship, Classifier):

    def __init__(self, isDerived: bool, Association: "uml2CD_Property" = None, Association96: "uml2CD_Property" = None, association: set["uml2CD_Property"] = None, owningAssociation: set["uml2CD_Property"] = None):
        self.isDerived = isDerived
        self.Association = Association
        self.Association96 = Association96
        self.association = association if association is not None else set()
        self.owningAssociation = owningAssociation if owningAssociation is not None else set()
        
    @property
    def isDerived(self) -> bool:
        return self.__isDerived

    @isDerived.setter
    def isDerived(self, isDerived: bool):
        self.__isDerived = isDerived

    @property
    def Association96(self):
        return self.__Association96

    @Association96.setter
    def Association96(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2CD_Association__Association96", None)
        self.__Association96 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownedEnd"):
                opp_val = getattr(old_value, "ownedEnd", None)
                if opp_val == self:
                    setattr(old_value, "ownedEnd", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedEnd"):
                opp_val = getattr(value, "ownedEnd", None)
                setattr(value, "ownedEnd", self)

    @property
    def association(self):
        return self.__association

    @association.setter
    def association(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2CD_Association__association", None)
        self.__association = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Property104"):
                    opp_val = getattr(item, "Property104", None)
                    
                    if opp_val == self:
                        setattr(item, "Property104", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Property104"):
                    opp_val = getattr(item, "Property104", None)
                    
                    setattr(item, "Property104", self)
                    

    @property
    def Association(self):
        return self.__Association

    @Association.setter
    def Association(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2CD_Association__Association", None)
        self.__Association = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "memberEnd"):
                opp_val = getattr(old_value, "memberEnd", None)
                if opp_val == self:
                    setattr(old_value, "memberEnd", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "memberEnd"):
                opp_val = getattr(value, "memberEnd", None)
                setattr(value, "memberEnd", self)

    @property
    def owningAssociation(self):
        return self.__owningAssociation

    @owningAssociation.setter
    def owningAssociation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2CD_Association__owningAssociation", None)
        self.__owningAssociation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Property106"):
                    opp_val = getattr(item, "Property106", None)
                    
                    if opp_val == self:
                        setattr(item, "Property106", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Property106"):
                    opp_val = getattr(item, "Property106", None)
                    
                    setattr(item, "Property106", self)
                    

class uml2CD_DirectRelationship(Relationship):

    pass
class Element:

    pass
class uml2CD_MultiplicityElement(Element):

    pass
class uml2CD_NamedElement(Element):

    def __init__(self, name: str, uml2CD_NamedElement: "uml2CD_Namespace" = None, supplier: set["uml2CD_Dependency"] = None, client: set["uml2CD_Dependency"] = None, NamedElement: "uml2CD_Dependency" = None, NamedElement115: "uml2CD_Dependency" = None):
        self.name = name
        self.uml2CD_NamedElement = uml2CD_NamedElement
        self.supplier = supplier if supplier is not None else set()
        self.client = client if client is not None else set()
        self.NamedElement = NamedElement
        self.NamedElement115 = NamedElement115
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def uml2CD_NamedElement(self):
        return self.__uml2CD_NamedElement

    @uml2CD_NamedElement.setter
    def uml2CD_NamedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2CD_NamedElement__uml2CD_NamedElement", None)
        self.__uml2CD_NamedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml2CD_Namespace"):
                opp_val = getattr(old_value, "uml2CD_Namespace", None)
                if opp_val == self:
                    setattr(old_value, "uml2CD_Namespace", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml2CD_Namespace"):
                opp_val = getattr(value, "uml2CD_Namespace", None)
                setattr(value, "uml2CD_Namespace", self)

    @property
    def client(self):
        return self.__client

    @client.setter
    def client(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2CD_NamedElement__client", None)
        self.__client = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Dependency17"):
                    opp_val = getattr(item, "Dependency17", None)
                    
                    if opp_val == self:
                        setattr(item, "Dependency17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Dependency17"):
                    opp_val = getattr(item, "Dependency17", None)
                    
                    setattr(item, "Dependency17", self)
                    

    @property
    def NamedElement115(self):
        return self.__NamedElement115

    @NamedElement115.setter
    def NamedElement115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2CD_NamedElement__NamedElement115", None)
        self.__NamedElement115 = value
        
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
    def supplier(self):
        return self.__supplier

    @supplier.setter
    def supplier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2CD_NamedElement__supplier", None)
        self.__supplier = value if value is not None else set()
        
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
        old_value = getattr(self, f"_uml2CD_NamedElement__NamedElement", None)
        self.__NamedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "supplierDependency"):
                opp_val = getattr(old_value, "supplierDependency", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "supplierDependency"):
                opp_val = getattr(value, "supplierDependency", None)
                if opp_val is None:
                    setattr(value, "supplierDependency", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class uml2CD_RedefinableElement(Element):

    def __init__(self, isLeaf: bool, uml2CD_RedefinableElement: "uml2CD_RedefinableElement" = None, uml2CD_RedefinableElement128: set["uml2CD_RedefinableElement"] = None):
        self.isLeaf = isLeaf
        self.uml2CD_RedefinableElement = uml2CD_RedefinableElement
        self.uml2CD_RedefinableElement128 = uml2CD_RedefinableElement128 if uml2CD_RedefinableElement128 is not None else set()
        
    @property
    def isLeaf(self) -> bool:
        return self.__isLeaf

    @isLeaf.setter
    def isLeaf(self, isLeaf: bool):
        self.__isLeaf = isLeaf

    @property
    def uml2CD_RedefinableElement128(self):
        return self.__uml2CD_RedefinableElement128

    @uml2CD_RedefinableElement128.setter
    def uml2CD_RedefinableElement128(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2CD_RedefinableElement__uml2CD_RedefinableElement128", None)
        self.__uml2CD_RedefinableElement128 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml2CD_RedefinableElement"):
                    opp_val = getattr(item, "uml2CD_RedefinableElement", None)
                    
                    if opp_val == self:
                        setattr(item, "uml2CD_RedefinableElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml2CD_RedefinableElement"):
                    opp_val = getattr(item, "uml2CD_RedefinableElement", None)
                    
                    setattr(item, "uml2CD_RedefinableElement", self)
                    

    @property
    def uml2CD_RedefinableElement(self):
        return self.__uml2CD_RedefinableElement

    @uml2CD_RedefinableElement.setter
    def uml2CD_RedefinableElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2CD_RedefinableElement__uml2CD_RedefinableElement", None)
        self.__uml2CD_RedefinableElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml2CD_RedefinableElement128"):
                opp_val = getattr(old_value, "uml2CD_RedefinableElement128", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml2CD_RedefinableElement128"):
                opp_val = getattr(value, "uml2CD_RedefinableElement128", None)
                if opp_val is None:
                    setattr(value, "uml2CD_RedefinableElement128", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class uml2CD_Relationship(Element):

    pass
class uml2CD_Element(ABC):

    pass