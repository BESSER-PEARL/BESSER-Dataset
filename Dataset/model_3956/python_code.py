from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class VisibilityKind(Enum):
    package = "package"
    public = "public"
    private = "private"
    protected = "protected"
class AggregationKind(Enum):
    none = "none"
    shared = "shared"
    composite = "composite"


############################################
# Definition of Classes
############################################

class Realization:

    pass
class Classes_Dependencies_Substitution(Realization):

    pass
class Abstraction:

    pass
class Classes_Dependencies_Realization(Abstraction):

    pass
class OpaqueExpression:

    pass
class Kernel_DirectedRelationship:

    pass
class Kernel_Association:

    pass
class Kernel_Class:

    pass
class Classes_AssociationClasses_AssociationClass(Kernel_Association, Kernel_Class):

    pass
class InterfaceRealization:

    pass
class BehavioredClassifier:

    pass
class Classes_Interfaces_InterfaceRealization(Realization):

    pass
class Kernel_Classifier:

    pass
class Kernel_Relationship:

    pass
class Classes_Kernel_Association(Kernel_Classifier, Kernel_Relationship):

    def __init__(self, isDerived: bool, association: set["Property"] = None, owningAssociation: set["Property"] = None, Classes_Kernel_Association: set["Property"] = None):
        self.isDerived = isDerived
        self.association = association if association is not None else set()
        self.owningAssociation = owningAssociation if owningAssociation is not None else set()
        self.Classes_Kernel_Association = Classes_Kernel_Association if Classes_Kernel_Association is not None else set()
        
        pass
    @property
    def isDerived(self):
        return self.__isDerived

    @isDerived.setter
    def isDerived(self, isDerived: bool):
        self.__isDerived = isDerived


    @property
    def association(self):
        return self.__association

    @association.setter
    def association(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Kernel_Association__association", None)
        self.__association = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Property165"):
                    opp_val = getattr(item, "Property165", None)
                    
                    if opp_val == self:
                        setattr(item, "Property165", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Property165"):
                    opp_val = getattr(item, "Property165", None)
                    
                    setattr(item, "Property165", self)
                    

    @property
    def Classes_Kernel_Association(self):
        return self.__Classes_Kernel_Association

    @Classes_Kernel_Association.setter
    def Classes_Kernel_Association(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Kernel_Association__Classes_Kernel_Association", None)
        self.__Classes_Kernel_Association = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Property163"):
                    opp_val = getattr(item, "Property163", None)
                    
                    if opp_val == self:
                        setattr(item, "Property163", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Property163"):
                    opp_val = getattr(item, "Property163", None)
                    
                    setattr(item, "Property163", self)
                    

    @property
    def owningAssociation(self):
        return self.__owningAssociation

    @owningAssociation.setter
    def owningAssociation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Kernel_Association__owningAssociation", None)
        self.__owningAssociation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Property167"):
                    opp_val = getattr(item, "Property167", None)
                    
                    if opp_val == self:
                        setattr(item, "Property167", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Property167"):
                    opp_val = getattr(item, "Property167", None)
                    
                    setattr(item, "Property167", self)
                    

class Operation:

    pass
class Enumeration:

    pass
class EnumerationLiteral:

    pass
class Parameter:

    pass
class Interface:

    pass
class DataType:

    pass
class Classes_Kernel_Enumeration(DataType):

    pass
class Classes_Kernel_PrimitiveType(DataType):

    pass
class BehavioralFeature:

    pass
class Classes_Kernel_Operation(BehavioralFeature):

    def __init__(self, isQuery: bool, isOrdered: bool, isUnique: bool, upper: int, lower: int, Classes_Kernel_Operation: "Type" = None, Classes_Kernel_Operation137: set["Constraint"] = None, Classes_Kernel_Operation140: set["Constraint"] = None, Classes_Kernel_Operation143: set["Constraint"] = None, ownedOperation: "Class" = None, ownedOperation148: "DataType" = None, ownedOperation151: "Interface" = None, BehavioralFeature: "Classes_Kernel_Parameter" = None):
        self.isQuery = isQuery
        self.isOrdered = isOrdered
        self.isUnique = isUnique
        self.upper = upper
        self.lower = lower
        self.Classes_Kernel_Operation = Classes_Kernel_Operation
        self.Classes_Kernel_Operation137 = Classes_Kernel_Operation137 if Classes_Kernel_Operation137 is not None else set()
        self.Classes_Kernel_Operation140 = Classes_Kernel_Operation140 if Classes_Kernel_Operation140 is not None else set()
        self.Classes_Kernel_Operation143 = Classes_Kernel_Operation143 if Classes_Kernel_Operation143 is not None else set()
        self.ownedOperation = ownedOperation
        self.ownedOperation148 = ownedOperation148
        self.ownedOperation151 = ownedOperation151
        
        pass
    @property
    def isQuery(self):
        return self.__isQuery

    @isQuery.setter
    def isQuery(self, isQuery: bool):
        self.__isQuery = isQuery


    @property
    def upper(self):
        return self.__upper

    @upper.setter
    def upper(self, upper: int):
        self.__upper = upper


    @property
    def isOrdered(self):
        return self.__isOrdered

    @isOrdered.setter
    def isOrdered(self, isOrdered: bool):
        self.__isOrdered = isOrdered


    @property
    def isUnique(self):
        return self.__isUnique

    @isUnique.setter
    def isUnique(self, isUnique: bool):
        self.__isUnique = isUnique


    @property
    def lower(self):
        return self.__lower

    @lower.setter
    def lower(self, lower: int):
        self.__lower = lower


    @property
    def ownedOperation148(self):
        return self.__ownedOperation148

    @ownedOperation148.setter
    def ownedOperation148(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Kernel_Operation__ownedOperation148", None)
        self.__ownedOperation148 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DataType149"):
                opp_val = getattr(old_value, "DataType149", None)
                if opp_val == self:
                    setattr(old_value, "DataType149", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DataType149"):
                opp_val = getattr(value, "DataType149", None)
                setattr(value, "DataType149", self)

    @property
    def Classes_Kernel_Operation137(self):
        return self.__Classes_Kernel_Operation137

    @Classes_Kernel_Operation137.setter
    def Classes_Kernel_Operation137(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Kernel_Operation__Classes_Kernel_Operation137", None)
        self.__Classes_Kernel_Operation137 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Constraint138"):
                    opp_val = getattr(item, "Constraint138", None)
                    
                    if opp_val == self:
                        setattr(item, "Constraint138", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Constraint138"):
                    opp_val = getattr(item, "Constraint138", None)
                    
                    setattr(item, "Constraint138", self)
                    

    @property
    def Classes_Kernel_Operation143(self):
        return self.__Classes_Kernel_Operation143

    @Classes_Kernel_Operation143.setter
    def Classes_Kernel_Operation143(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Kernel_Operation__Classes_Kernel_Operation143", None)
        self.__Classes_Kernel_Operation143 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Constraint144"):
                    opp_val = getattr(item, "Constraint144", None)
                    
                    if opp_val == self:
                        setattr(item, "Constraint144", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Constraint144"):
                    opp_val = getattr(item, "Constraint144", None)
                    
                    setattr(item, "Constraint144", self)
                    

    @property
    def ownedOperation151(self):
        return self.__ownedOperation151

    @ownedOperation151.setter
    def ownedOperation151(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Kernel_Operation__ownedOperation151", None)
        self.__ownedOperation151 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Interface152"):
                opp_val = getattr(old_value, "Interface152", None)
                if opp_val == self:
                    setattr(old_value, "Interface152", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Interface152"):
                opp_val = getattr(value, "Interface152", None)
                setattr(value, "Interface152", self)

    @property
    def Classes_Kernel_Operation140(self):
        return self.__Classes_Kernel_Operation140

    @Classes_Kernel_Operation140.setter
    def Classes_Kernel_Operation140(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Kernel_Operation__Classes_Kernel_Operation140", None)
        self.__Classes_Kernel_Operation140 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Constraint141"):
                    opp_val = getattr(item, "Constraint141", None)
                    
                    if opp_val == self:
                        setattr(item, "Constraint141", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Constraint141"):
                    opp_val = getattr(item, "Constraint141", None)
                    
                    setattr(item, "Constraint141", self)
                    

    @property
    def Classes_Kernel_Operation(self):
        return self.__Classes_Kernel_Operation

    @Classes_Kernel_Operation.setter
    def Classes_Kernel_Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Kernel_Operation__Classes_Kernel_Operation", None)
        self.__Classes_Kernel_Operation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Type135"):
                opp_val = getattr(old_value, "Type135", None)
                if opp_val == self:
                    setattr(old_value, "Type135", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Type135"):
                opp_val = getattr(value, "Type135", None)
                setattr(value, "Type135", self)

    @property
    def ownedOperation(self):
        return self.__ownedOperation

    @ownedOperation.setter
    def ownedOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Kernel_Operation__ownedOperation", None)
        self.__ownedOperation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Class146"):
                opp_val = getattr(old_value, "Class146", None)
                if opp_val == self:
                    setattr(old_value, "Class146", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Class146"):
                opp_val = getattr(value, "Class146", None)
                setattr(value, "Class146", self)

class TypedElement:

    pass
class Classes_Kernel_Parameter(TypedElement):

    def __init__(self, default: str, Classes_Kernel_Parameter: "BehavioralFeature" = None, Classes_Kernel_Parameter132: "ValueSpecification" = None):
        self.default = default
        self.Classes_Kernel_Parameter = Classes_Kernel_Parameter
        self.Classes_Kernel_Parameter132 = Classes_Kernel_Parameter132
        
        pass
    @property
    def default(self):
        return self.__default

    @default.setter
    def default(self, default: str):
        self.__default = default


    @property
    def Classes_Kernel_Parameter132(self):
        return self.__Classes_Kernel_Parameter132

    @Classes_Kernel_Parameter132.setter
    def Classes_Kernel_Parameter132(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Kernel_Parameter__Classes_Kernel_Parameter132", None)
        self.__Classes_Kernel_Parameter132 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ValueSpecification133"):
                opp_val = getattr(old_value, "ValueSpecification133", None)
                if opp_val == self:
                    setattr(old_value, "ValueSpecification133", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ValueSpecification133"):
                opp_val = getattr(value, "ValueSpecification133", None)
                setattr(value, "ValueSpecification133", self)

    @property
    def Classes_Kernel_Parameter(self):
        return self.__Classes_Kernel_Parameter

    @Classes_Kernel_Parameter.setter
    def Classes_Kernel_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Kernel_Parameter__Classes_Kernel_Parameter", None)
        self.__Classes_Kernel_Parameter = value
        
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

class Kernel_Feature:

    pass
class GeneralizationSet:

    pass
class Substitution:

    pass
class Generalization_:

    pass
class Association:

    pass
class Class:

    pass
class Kernel_MultiplicityElement:

    pass
class Classifier:

    pass
class Classes_Kernel_DataType(Classifier):

    pass
class Classes_Kernel_Class(Classifier):

    pass
class Classes_Interfaces_Interface(Classifier):

    pass
class Classes_Interfaces_BehavioredClassifier(Classifier):

    pass
class Classes_Kernel_InstanceValue:

    pass
class Property:

    pass
class Feature:

    pass
class Kernel_Type:

    pass
class Kernel_RedefinableElement:

    pass
class RedefinableElement:

    pass
class Classes_Kernel_Feature(RedefinableElement):

    def __init__(self, isStatic: bool, feature: set["Classifier"] = None, RedefinableElement: "Classes_Kernel_RedefinableElement" = None):
        self.isStatic = isStatic
        self.feature = feature if feature is not None else set()
        
        pass
    @property
    def isStatic(self):
        return self.__isStatic

    @isStatic.setter
    def isStatic(self, isStatic: bool):
        self.__isStatic = isStatic


    @property
    def feature(self):
        return self.__feature

    @feature.setter
    def feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Kernel_Feature__feature", None)
        self.__feature = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Classifier95"):
                    opp_val = getattr(item, "Classifier95", None)
                    
                    if opp_val == self:
                        setattr(item, "Classifier95", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Classifier95"):
                    opp_val = getattr(item, "Classifier95", None)
                    
                    setattr(item, "Classifier95", self)
                    

class StructuralFeature:

    pass
class Classes_Kernel_Property(StructuralFeature):

    def __init__(self, isDerived: bool, isDerivedUnion: bool, default: str, isComposite: bool, isID: bool, aggregation: str, ownedAttribute: "Class" = None, Classes_Kernel_Property: set["Property"] = None, Classes_Kernel_Property100: "ValueSpecification" = None, Classes_Kernel_Property103: "Property" = None, Classes_Kernel_Property106: "Property" = None, memberEnd: "Association" = None, ownedEnd: "Association" = None, ownedAttribute112: "DataType" = None, ownedAttribute114: "Interface" = None, associationEnd: set["Property"] = None, qualifier: "Property" = None, StructuralFeature: "Classes_Kernel_Slot" = None):
        self.isDerived = isDerived
        self.isDerivedUnion = isDerivedUnion
        self.default = default
        self.isComposite = isComposite
        self.isID = isID
        self.aggregation = aggregation
        self.ownedAttribute = ownedAttribute
        self.Classes_Kernel_Property = Classes_Kernel_Property if Classes_Kernel_Property is not None else set()
        self.Classes_Kernel_Property100 = Classes_Kernel_Property100
        self.Classes_Kernel_Property103 = Classes_Kernel_Property103
        self.Classes_Kernel_Property106 = Classes_Kernel_Property106
        self.memberEnd = memberEnd
        self.ownedEnd = ownedEnd
        self.ownedAttribute112 = ownedAttribute112
        self.ownedAttribute114 = ownedAttribute114
        self.associationEnd = associationEnd if associationEnd is not None else set()
        self.qualifier = qualifier
        
        pass
    @property
    def default(self):
        return self.__default

    @default.setter
    def default(self, default: str):
        self.__default = default


    @property
    def isDerived(self):
        return self.__isDerived

    @isDerived.setter
    def isDerived(self, isDerived: bool):
        self.__isDerived = isDerived


    @property
    def isComposite(self):
        return self.__isComposite

    @isComposite.setter
    def isComposite(self, isComposite: bool):
        self.__isComposite = isComposite


    @property
    def aggregation(self):
        return self.__aggregation

    @aggregation.setter
    def aggregation(self, aggregation: str):
        self.__aggregation = aggregation


    @property
    def isID(self):
        return self.__isID

    @isID.setter
    def isID(self, isID: bool):
        self.__isID = isID


    @property
    def isDerivedUnion(self):
        return self.__isDerivedUnion

    @isDerivedUnion.setter
    def isDerivedUnion(self, isDerivedUnion: bool):
        self.__isDerivedUnion = isDerivedUnion


    @property
    def Classes_Kernel_Property100(self):
        return self.__Classes_Kernel_Property100

    @Classes_Kernel_Property100.setter
    def Classes_Kernel_Property100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Kernel_Property__Classes_Kernel_Property100", None)
        self.__Classes_Kernel_Property100 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ValueSpecification101"):
                opp_val = getattr(old_value, "ValueSpecification101", None)
                if opp_val == self:
                    setattr(old_value, "ValueSpecification101", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ValueSpecification101"):
                opp_val = getattr(value, "ValueSpecification101", None)
                setattr(value, "ValueSpecification101", self)

    @property
    def memberEnd(self):
        return self.__memberEnd

    @memberEnd.setter
    def memberEnd(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Kernel_Property__memberEnd", None)
        self.__memberEnd = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Association"):
                opp_val = getattr(old_value, "Association", None)
                if opp_val == self:
                    setattr(old_value, "Association", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Association"):
                opp_val = getattr(value, "Association", None)
                setattr(value, "Association", self)

    @property
    def associationEnd(self):
        return self.__associationEnd

    @associationEnd.setter
    def associationEnd(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Kernel_Property__associationEnd", None)
        self.__associationEnd = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Property116"):
                    opp_val = getattr(item, "Property116", None)
                    
                    if opp_val == self:
                        setattr(item, "Property116", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Property116"):
                    opp_val = getattr(item, "Property116", None)
                    
                    setattr(item, "Property116", self)
                    

    @property
    def ownedAttribute114(self):
        return self.__ownedAttribute114

    @ownedAttribute114.setter
    def ownedAttribute114(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Kernel_Property__ownedAttribute114", None)
        self.__ownedAttribute114 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Interface"):
                opp_val = getattr(old_value, "Interface", None)
                if opp_val == self:
                    setattr(old_value, "Interface", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Interface"):
                opp_val = getattr(value, "Interface", None)
                setattr(value, "Interface", self)

    @property
    def ownedAttribute112(self):
        return self.__ownedAttribute112

    @ownedAttribute112.setter
    def ownedAttribute112(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Kernel_Property__ownedAttribute112", None)
        self.__ownedAttribute112 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DataType"):
                opp_val = getattr(old_value, "DataType", None)
                if opp_val == self:
                    setattr(old_value, "DataType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DataType"):
                opp_val = getattr(value, "DataType", None)
                setattr(value, "DataType", self)

    @property
    def ownedAttribute(self):
        return self.__ownedAttribute

    @ownedAttribute.setter
    def ownedAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Kernel_Property__ownedAttribute", None)
        self.__ownedAttribute = value
        
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
    def Classes_Kernel_Property106(self):
        return self.__Classes_Kernel_Property106

    @Classes_Kernel_Property106.setter
    def Classes_Kernel_Property106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Kernel_Property__Classes_Kernel_Property106", None)
        self.__Classes_Kernel_Property106 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Property107"):
                opp_val = getattr(old_value, "Property107", None)
                if opp_val == self:
                    setattr(old_value, "Property107", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Property107"):
                opp_val = getattr(value, "Property107", None)
                setattr(value, "Property107", self)

    @property
    def Classes_Kernel_Property103(self):
        return self.__Classes_Kernel_Property103

    @Classes_Kernel_Property103.setter
    def Classes_Kernel_Property103(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Kernel_Property__Classes_Kernel_Property103", None)
        self.__Classes_Kernel_Property103 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Property104"):
                opp_val = getattr(old_value, "Property104", None)
                if opp_val == self:
                    setattr(old_value, "Property104", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Property104"):
                opp_val = getattr(value, "Property104", None)
                setattr(value, "Property104", self)

    @property
    def qualifier(self):
        return self.__qualifier

    @qualifier.setter
    def qualifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Kernel_Property__qualifier", None)
        self.__qualifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Property118"):
                opp_val = getattr(old_value, "Property118", None)
                if opp_val == self:
                    setattr(old_value, "Property118", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Property118"):
                opp_val = getattr(value, "Property118", None)
                setattr(value, "Property118", self)

    @property
    def ownedEnd(self):
        return self.__ownedEnd

    @ownedEnd.setter
    def ownedEnd(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Kernel_Property__ownedEnd", None)
        self.__ownedEnd = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Association110"):
                opp_val = getattr(old_value, "Association110", None)
                if opp_val == self:
                    setattr(old_value, "Association110", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Association110"):
                opp_val = getattr(value, "Association110", None)
                setattr(value, "Association110", self)

    @property
    def Classes_Kernel_Property(self):
        return self.__Classes_Kernel_Property

    @Classes_Kernel_Property.setter
    def Classes_Kernel_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Kernel_Property__Classes_Kernel_Property", None)
        self.__Classes_Kernel_Property = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Property98"):
                    opp_val = getattr(item, "Property98", None)
                    
                    if opp_val == self:
                        setattr(item, "Property98", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Property98"):
                    opp_val = getattr(item, "Property98", None)
                    
                    setattr(item, "Property98", self)
                    

class MultiplicityElement:

    pass
class Kernel_TypedElement:

    pass
class Classes_Kernel_StructuralFeature(Kernel_Feature, Kernel_MultiplicityElement, Kernel_TypedElement):

    def __init__(self, isReadOnly: bool):
        self.isReadOnly = isReadOnly
        
        pass
    @property
    def isReadOnly(self):
        return self.__isReadOnly

    @isReadOnly.setter
    def isReadOnly(self, isReadOnly: bool):
        self.__isReadOnly = isReadOnly


class ValueSpecification:

    pass
class Relationship:

    pass
class Classes_Kernel_DirectedRelationship(Relationship):

    pass
class LiteralSpecification:

    pass
class Classes_Kernel_LiteralBoolean(LiteralSpecification):

    pass
class Classes_Kernel_LiteralReal(LiteralSpecification):

    pass
class Classes_Kernel_LiteralString(LiteralSpecification):

    pass
class Classes_Kernel_LiteralInteger(LiteralSpecification):

    pass
class Classes_Kernel_LiteralUnilimitedNatural(LiteralSpecification):

    pass
class Classes_Kernel_LiteralNull(LiteralSpecification):

    pass
class Classes_Kernel_LiteralSpecification(ValueSpecification):

    pass
class Classes_Kernel_OpaqueExpression(ValueSpecification):

    def __init__(self, body: str, language: str, ValueSpecification70: "Classes_Kernel_Constraint" = None, ValueSpecification74: "Classes_Kernel_Slot" = None, ValueSpecification: "Classes_Kernel_MultiplicityElement" = None, ValueSpecification101: "Classes_Kernel_Property" = None, ValueSpecification43: "Classes_Kernel_MultiplicityElement" = None, ValueSpecification63: "Classes_Kernel_InstanceSpecification" = None, ValueSpecification133: "Classes_Kernel_Parameter" = None, ValueSpecification57: "Classes_Kernel_Expression" = None):
        self.body = body
        self.language = language
        
        pass
    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language


    @property
    def body(self):
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body


class Classes_Kernel_Expression(ValueSpecification):

    def __init__(self, symbol: str, Classes_Kernel_Expression: "ValueSpecification" = None, ValueSpecification70: "Classes_Kernel_Constraint" = None, ValueSpecification74: "Classes_Kernel_Slot" = None, ValueSpecification: "Classes_Kernel_MultiplicityElement" = None, ValueSpecification101: "Classes_Kernel_Property" = None, ValueSpecification43: "Classes_Kernel_MultiplicityElement" = None, ValueSpecification63: "Classes_Kernel_InstanceSpecification" = None, ValueSpecification133: "Classes_Kernel_Parameter" = None, ValueSpecification57: "Classes_Kernel_Expression" = None):
        self.symbol = symbol
        self.Classes_Kernel_Expression = Classes_Kernel_Expression
        
        pass
    @property
    def symbol(self):
        return self.__symbol

    @symbol.setter
    def symbol(self, symbol: str):
        self.__symbol = symbol


    @property
    def Classes_Kernel_Expression(self):
        return self.__Classes_Kernel_Expression

    @Classes_Kernel_Expression.setter
    def Classes_Kernel_Expression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Kernel_Expression__Classes_Kernel_Expression", None)
        self.__Classes_Kernel_Expression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ValueSpecification57"):
                opp_val = getattr(old_value, "ValueSpecification57", None)
                if opp_val == self:
                    setattr(old_value, "ValueSpecification57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ValueSpecification57"):
                opp_val = getattr(value, "ValueSpecification57", None)
                setattr(value, "ValueSpecification57", self)

class InstanceSpecification:

    pass
class Classes_Kernel_EnumerationLiteral(InstanceSpecification):

    pass
class Slot:

    pass
class DirectedRelationship:

    pass
class Classes_Kernel_PackageImport(DirectedRelationship):

    def __init__(self, visibility: str, Classes_Kernel_PackageImport: "Package" = None, packageImport: "Namespace" = None):
        self.visibility = visibility
        self.Classes_Kernel_PackageImport = Classes_Kernel_PackageImport
        self.packageImport = packageImport
        
        pass
    @property
    def visibility(self):
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility


    @property
    def packageImport(self):
        return self.__packageImport

    @packageImport.setter
    def packageImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Kernel_PackageImport__packageImport", None)
        self.__packageImport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Namespace21"):
                opp_val = getattr(old_value, "Namespace21", None)
                if opp_val == self:
                    setattr(old_value, "Namespace21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Namespace21"):
                opp_val = getattr(value, "Namespace21", None)
                setattr(value, "Namespace21", self)

    @property
    def Classes_Kernel_PackageImport(self):
        return self.__Classes_Kernel_PackageImport

    @Classes_Kernel_PackageImport.setter
    def Classes_Kernel_PackageImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Kernel_PackageImport__Classes_Kernel_PackageImport", None)
        self.__Classes_Kernel_PackageImport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Package"):
                opp_val = getattr(old_value, "Package", None)
                if opp_val == self:
                    setattr(old_value, "Package", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Package"):
                opp_val = getattr(value, "Package", None)
                setattr(value, "Package", self)

class Classes_Kernel_Generalization_(DirectedRelationship):

    def __init__(self, isSubstitutable: bool, Classes_Kernel_Generalization: "Classifier" = None, generalization: "Classifier" = None, generalization124: set["GeneralizationSet"] = None):
        self.isSubstitutable = isSubstitutable
        self.Classes_Kernel_Generalization = Classes_Kernel_Generalization
        self.generalization = generalization
        self.generalization124 = generalization124 if generalization124 is not None else set()
        
        pass
    @property
    def isSubstitutable(self):
        return self.__isSubstitutable

    @isSubstitutable.setter
    def isSubstitutable(self, isSubstitutable: bool):
        self.__isSubstitutable = isSubstitutable


    @property
    def Classes_Kernel_Generalization(self):
        return self.__Classes_Kernel_Generalization

    @Classes_Kernel_Generalization.setter
    def Classes_Kernel_Generalization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Kernel_Generalization___Classes_Kernel_Generalization", None)
        self.__Classes_Kernel_Generalization = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Classifier120"):
                opp_val = getattr(old_value, "Classifier120", None)
                if opp_val == self:
                    setattr(old_value, "Classifier120", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Classifier120"):
                opp_val = getattr(value, "Classifier120", None)
                setattr(value, "Classifier120", self)

    @property
    def generalization(self):
        return self.__generalization

    @generalization.setter
    def generalization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Kernel_Generalization___generalization", None)
        self.__generalization = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Classifier122"):
                opp_val = getattr(old_value, "Classifier122", None)
                if opp_val == self:
                    setattr(old_value, "Classifier122", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Classifier122"):
                opp_val = getattr(value, "Classifier122", None)
                setattr(value, "Classifier122", self)

    @property
    def generalization124(self):
        return self.__generalization124

    @generalization124.setter
    def generalization124(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Kernel_Generalization___generalization124", None)
        self.__generalization124 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GeneralizationSet125"):
                    opp_val = getattr(item, "GeneralizationSet125", None)
                    
                    if opp_val == self:
                        setattr(item, "GeneralizationSet125", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GeneralizationSet125"):
                    opp_val = getattr(item, "GeneralizationSet125", None)
                    
                    setattr(item, "GeneralizationSet125", self)
                    

class Classes_Kernel_PackageMerge(DirectedRelationship):

    pass
class Classes_Kernel_ElementImport(DirectedRelationship):

    def __init__(self, visibility: str, alias: str, Classes_Kernel_ElementImport: "PackageableElement" = None, elementImport: "Namespace" = None):
        self.visibility = visibility
        self.alias = alias
        self.Classes_Kernel_ElementImport = Classes_Kernel_ElementImport
        self.elementImport = elementImport
        
        pass
    @property
    def alias(self):
        return self.__alias

    @alias.setter
    def alias(self, alias: str):
        self.__alias = alias


    @property
    def visibility(self):
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
        old_value = getattr(self, f"_Classes_Kernel_ElementImport__elementImport", None)
        self.__elementImport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Namespace18"):
                opp_val = getattr(old_value, "Namespace18", None)
                if opp_val == self:
                    setattr(old_value, "Namespace18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Namespace18"):
                opp_val = getattr(value, "Namespace18", None)
                setattr(value, "Namespace18", self)

    @property
    def Classes_Kernel_ElementImport(self):
        return self.__Classes_Kernel_ElementImport

    @Classes_Kernel_ElementImport.setter
    def Classes_Kernel_ElementImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Kernel_ElementImport__Classes_Kernel_ElementImport", None)
        self.__Classes_Kernel_ElementImport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PackageableElement16"):
                opp_val = getattr(old_value, "PackageableElement16", None)
                if opp_val == self:
                    setattr(old_value, "PackageableElement16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PackageableElement16"):
                opp_val = getattr(value, "PackageableElement16", None)
                setattr(value, "PackageableElement16", self)

class Constraint:

    pass
class PackageImport:

    pass
class ElementImport:

    pass
class PackageMerge:

    pass
class Type:

    pass
class Kernel_PackageableElement:

    pass
class Classes_Kernel_ValueSpecification(Kernel_PackageableElement, Kernel_TypedElement):

    pass
class Classes_Dependencies_Dependency(Kernel_PackageableElement, Kernel_DirectedRelationship):

    pass
class Kernel_Namespace:

    pass
class Classes_Kernel_BehavioralFeature(Kernel_Feature, Kernel_Namespace):

    pass
class Classes_Kernel_Classifier(Kernel_Namespace, Kernel_RedefinableElement, Kernel_Type):

    def __init__(self, isAbstract: bool, isFinalSpecialization: bool, Classes_Kernel_Classifier: set["NamedElement"] = None, featuringClassifier: set["Feature"] = None, Classes_Kernel_Classifier84: set["Property"] = None, Classes_Kernel_Classifier86: set["Classifier"] = None, Classes_Kernel_Classifier89: set["Classifier"] = None, powertype: set["GeneralizationSet"] = None, specific: set["Generalization_"] = None, substitutingClassifier: set["Substitution"] = None):
        self.isAbstract = isAbstract
        self.isFinalSpecialization = isFinalSpecialization
        self.Classes_Kernel_Classifier = Classes_Kernel_Classifier if Classes_Kernel_Classifier is not None else set()
        self.featuringClassifier = featuringClassifier if featuringClassifier is not None else set()
        self.Classes_Kernel_Classifier84 = Classes_Kernel_Classifier84 if Classes_Kernel_Classifier84 is not None else set()
        self.Classes_Kernel_Classifier86 = Classes_Kernel_Classifier86 if Classes_Kernel_Classifier86 is not None else set()
        self.Classes_Kernel_Classifier89 = Classes_Kernel_Classifier89 if Classes_Kernel_Classifier89 is not None else set()
        self.powertype = powertype if powertype is not None else set()
        self.specific = specific if specific is not None else set()
        self.substitutingClassifier = substitutingClassifier if substitutingClassifier is not None else set()
        
        pass
    @property
    def isFinalSpecialization(self):
        return self.__isFinalSpecialization

    @isFinalSpecialization.setter
    def isFinalSpecialization(self, isFinalSpecialization: bool):
        self.__isFinalSpecialization = isFinalSpecialization


    @property
    def isAbstract(self):
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: bool):
        self.__isAbstract = isAbstract


    @property
    def Classes_Kernel_Classifier84(self):
        return self.__Classes_Kernel_Classifier84

    @Classes_Kernel_Classifier84.setter
    def Classes_Kernel_Classifier84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Kernel_Classifier__Classes_Kernel_Classifier84", None)
        self.__Classes_Kernel_Classifier84 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Property"):
                    opp_val = getattr(item, "Property", None)
                    
                    if opp_val == self:
                        setattr(item, "Property", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Property"):
                    opp_val = getattr(item, "Property", None)
                    
                    setattr(item, "Property", self)
                    

    @property
    def powertype(self):
        return self.__powertype

    @powertype.setter
    def powertype(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Kernel_Classifier__powertype", None)
        self.__powertype = value if value is not None else set()
        
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
    def Classes_Kernel_Classifier89(self):
        return self.__Classes_Kernel_Classifier89

    @Classes_Kernel_Classifier89.setter
    def Classes_Kernel_Classifier89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Kernel_Classifier__Classes_Kernel_Classifier89", None)
        self.__Classes_Kernel_Classifier89 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Classifier90"):
                    opp_val = getattr(item, "Classifier90", None)
                    
                    if opp_val == self:
                        setattr(item, "Classifier90", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Classifier90"):
                    opp_val = getattr(item, "Classifier90", None)
                    
                    setattr(item, "Classifier90", self)
                    

    @property
    def substitutingClassifier(self):
        return self.__substitutingClassifier

    @substitutingClassifier.setter
    def substitutingClassifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Kernel_Classifier__substitutingClassifier", None)
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
    def Classes_Kernel_Classifier86(self):
        return self.__Classes_Kernel_Classifier86

    @Classes_Kernel_Classifier86.setter
    def Classes_Kernel_Classifier86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Kernel_Classifier__Classes_Kernel_Classifier86", None)
        self.__Classes_Kernel_Classifier86 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Classifier87"):
                    opp_val = getattr(item, "Classifier87", None)
                    
                    if opp_val == self:
                        setattr(item, "Classifier87", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Classifier87"):
                    opp_val = getattr(item, "Classifier87", None)
                    
                    setattr(item, "Classifier87", self)
                    

    @property
    def featuringClassifier(self):
        return self.__featuringClassifier

    @featuringClassifier.setter
    def featuringClassifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Kernel_Classifier__featuringClassifier", None)
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
    def Classes_Kernel_Classifier(self):
        return self.__Classes_Kernel_Classifier

    @Classes_Kernel_Classifier.setter
    def Classes_Kernel_Classifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Kernel_Classifier__Classes_Kernel_Classifier", None)
        self.__Classes_Kernel_Classifier = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "NamedElement81"):
                    opp_val = getattr(item, "NamedElement81", None)
                    
                    if opp_val == self:
                        setattr(item, "NamedElement81", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "NamedElement81"):
                    opp_val = getattr(item, "NamedElement81", None)
                    
                    setattr(item, "NamedElement81", self)
                    

    @property
    def specific(self):
        return self.__specific

    @specific.setter
    def specific(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Kernel_Classifier__specific", None)
        self.__specific = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Generalization_"):
                    opp_val = getattr(item, "Generalization_", None)
                    
                    if opp_val == self:
                        setattr(item, "Generalization_", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Generalization_"):
                    opp_val = getattr(item, "Generalization_", None)
                    
                    setattr(item, "Generalization_", self)
                    

class Classes_Kernel_Package(Kernel_Namespace, Kernel_PackageableElement):

    def __init__(self, URI: str, nestingPackage: set["Package"] = None, receivingPackage: set["PackageMerge"] = None, nestedPackage: "Package" = None, Classes_Kernel_Package: set["PackageableElement"] = None, package: set["Type"] = None):
        self.URI = URI
        self.nestingPackage = nestingPackage if nestingPackage is not None else set()
        self.receivingPackage = receivingPackage if receivingPackage is not None else set()
        self.nestedPackage = nestedPackage
        self.Classes_Kernel_Package = Classes_Kernel_Package if Classes_Kernel_Package is not None else set()
        self.package = package if package is not None else set()
        
        pass
    @property
    def URI(self):
        return self.__URI

    @URI.setter
    def URI(self, URI: str):
        self.__URI = URI


    @property
    def nestedPackage(self):
        return self.__nestedPackage

    @nestedPackage.setter
    def nestedPackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Kernel_Package__nestedPackage", None)
        self.__nestedPackage = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Package25"):
                opp_val = getattr(old_value, "Package25", None)
                if opp_val == self:
                    setattr(old_value, "Package25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Package25"):
                opp_val = getattr(value, "Package25", None)
                setattr(value, "Package25", self)

    @property
    def package(self):
        return self.__package

    @package.setter
    def package(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Kernel_Package__package", None)
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
    def Classes_Kernel_Package(self):
        return self.__Classes_Kernel_Package

    @Classes_Kernel_Package.setter
    def Classes_Kernel_Package(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Kernel_Package__Classes_Kernel_Package", None)
        self.__Classes_Kernel_Package = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PackageableElement27"):
                    opp_val = getattr(item, "PackageableElement27", None)
                    
                    if opp_val == self:
                        setattr(item, "PackageableElement27", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PackageableElement27"):
                    opp_val = getattr(item, "PackageableElement27", None)
                    
                    setattr(item, "PackageableElement27", self)
                    

    @property
    def nestingPackage(self):
        return self.__nestingPackage

    @nestingPackage.setter
    def nestingPackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Kernel_Package__nestingPackage", None)
        self.__nestingPackage = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Package23"):
                    opp_val = getattr(item, "Package23", None)
                    
                    if opp_val == self:
                        setattr(item, "Package23", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Package23"):
                    opp_val = getattr(item, "Package23", None)
                    
                    setattr(item, "Package23", self)
                    

    @property
    def receivingPackage(self):
        return self.__receivingPackage

    @receivingPackage.setter
    def receivingPackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Kernel_Package__receivingPackage", None)
        self.__receivingPackage = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PackageMerge"):
                    opp_val = getattr(item, "PackageMerge", None)
                    
                    if opp_val == self:
                        setattr(item, "PackageMerge", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PackageMerge"):
                    opp_val = getattr(item, "PackageMerge", None)
                    
                    setattr(item, "PackageMerge", self)
                    

class Package:

    pass
class PackageableElement:

    pass
class Classes_Kernel_Constraint(PackageableElement):

    pass
class Classes_Kernel_Type(PackageableElement):

    pass
class Classes_PowerTypes_GeneralizationSet(PackageableElement):

    def __init__(self, isCovering: bool, isDisjoint: bool, generalizationSet: set["Generalization_"] = None, powertypeExtent: "Classifier" = None, PackageableElement: "Classes_Kernel_Namespace" = None, PackageableElement16: "Classes_Kernel_ElementImport" = None, PackageableElement27: "Classes_Kernel_Package" = None):
        self.isCovering = isCovering
        self.isDisjoint = isDisjoint
        self.generalizationSet = generalizationSet if generalizationSet is not None else set()
        self.powertypeExtent = powertypeExtent
        
        pass
    @property
    def isDisjoint(self):
        return self.__isDisjoint

    @isDisjoint.setter
    def isDisjoint(self, isDisjoint: bool):
        self.__isDisjoint = isDisjoint


    @property
    def isCovering(self):
        return self.__isCovering

    @isCovering.setter
    def isCovering(self, isCovering: bool):
        self.__isCovering = isCovering


    @property
    def powertypeExtent(self):
        return self.__powertypeExtent

    @powertypeExtent.setter
    def powertypeExtent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_PowerTypes_GeneralizationSet__powertypeExtent", None)
        self.__powertypeExtent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Classifier203"):
                opp_val = getattr(old_value, "Classifier203", None)
                if opp_val == self:
                    setattr(old_value, "Classifier203", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Classifier203"):
                opp_val = getattr(value, "Classifier203", None)
                setattr(value, "Classifier203", self)

    @property
    def generalizationSet(self):
        return self.__generalizationSet

    @generalizationSet.setter
    def generalizationSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_PowerTypes_GeneralizationSet__generalizationSet", None)
        self.__generalizationSet = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Generalization205"):
                    opp_val = getattr(item, "Generalization205", None)
                    
                    if opp_val == self:
                        setattr(item, "Generalization205", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Generalization205"):
                    opp_val = getattr(item, "Generalization205", None)
                    
                    setattr(item, "Generalization205", self)
                    

class Classes_Kernel_InstanceSpecification(PackageableElement):

    pass
class NamedElement:

    pass
class Classes_Kernel_TypedElement(NamedElement):

    pass
class Classes_Kernel_RedefinableElement(NamedElement):

    def __init__(self, isLeaf: bool, Classes_Kernel_RedefinableElement: set["RedefinableElement"] = None, Classes_Kernel_RedefinableElement78: set["Classifier"] = None, NamedElement81: "Classes_Kernel_Classifier" = None, NamedElement: "Classes_Kernel_Namespace" = None, NamedElement10: "Classes_Kernel_Namespace" = None, NamedElement182: "Classes_Dependencies_Dependency" = None, NamedElement180: "Classes_Dependencies_Dependency" = None):
        self.isLeaf = isLeaf
        self.Classes_Kernel_RedefinableElement = Classes_Kernel_RedefinableElement if Classes_Kernel_RedefinableElement is not None else set()
        self.Classes_Kernel_RedefinableElement78 = Classes_Kernel_RedefinableElement78 if Classes_Kernel_RedefinableElement78 is not None else set()
        
        pass
    @property
    def isLeaf(self):
        return self.__isLeaf

    @isLeaf.setter
    def isLeaf(self, isLeaf: bool):
        self.__isLeaf = isLeaf


    @property
    def Classes_Kernel_RedefinableElement78(self):
        return self.__Classes_Kernel_RedefinableElement78

    @Classes_Kernel_RedefinableElement78.setter
    def Classes_Kernel_RedefinableElement78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Kernel_RedefinableElement__Classes_Kernel_RedefinableElement78", None)
        self.__Classes_Kernel_RedefinableElement78 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Classifier79"):
                    opp_val = getattr(item, "Classifier79", None)
                    
                    if opp_val == self:
                        setattr(item, "Classifier79", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Classifier79"):
                    opp_val = getattr(item, "Classifier79", None)
                    
                    setattr(item, "Classifier79", self)
                    

    @property
    def Classes_Kernel_RedefinableElement(self):
        return self.__Classes_Kernel_RedefinableElement

    @Classes_Kernel_RedefinableElement.setter
    def Classes_Kernel_RedefinableElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Kernel_RedefinableElement__Classes_Kernel_RedefinableElement", None)
        self.__Classes_Kernel_RedefinableElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RedefinableElement"):
                    opp_val = getattr(item, "RedefinableElement", None)
                    
                    if opp_val == self:
                        setattr(item, "RedefinableElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RedefinableElement"):
                    opp_val = getattr(item, "RedefinableElement", None)
                    
                    setattr(item, "RedefinableElement", self)
                    

class Classes_Kernel_PackageableElement(NamedElement):

    pass
class Classes_Kernel_Namespace(NamedElement):

    pass
class Dependency:

    pass
class Classes_Dependencies_Usage(Dependency):

    pass
class Classes_Dependencies_Abstraction(Dependency):

    pass
class Namespace:

    pass
class Element:

    pass
class Classes_Kernel_MultiplicityElement(Element):

    def __init__(self, isOrdered: bool, isUnique: bool, upper: int, lower: int, owningUpper: "ValueSpecification" = None, owningLower: "ValueSpecification" = None, Element31: "Classes_Kernel_Comment" = None, Element33: "Classes_Kernel_Comment" = None, Element68: "Classes_Kernel_Constraint" = None, Element35: "Classes_Kernel_Relationship" = None, Element37: "Classes_Kernel_DirectedRelationship" = None, Element40: "Classes_Kernel_DirectedRelationship" = None, Element3: "Classes_Kernel_Element" = None, Element: "Classes_Kernel_Element" = None):
        self.isOrdered = isOrdered
        self.isUnique = isUnique
        self.upper = upper
        self.lower = lower
        self.owningUpper = owningUpper
        self.owningLower = owningLower
        
        pass
    @property
    def isUnique(self):
        return self.__isUnique

    @isUnique.setter
    def isUnique(self, isUnique: bool):
        self.__isUnique = isUnique


    @property
    def upper(self):
        return self.__upper

    @upper.setter
    def upper(self, upper: int):
        self.__upper = upper


    @property
    def isOrdered(self):
        return self.__isOrdered

    @isOrdered.setter
    def isOrdered(self, isOrdered: bool):
        self.__isOrdered = isOrdered


    @property
    def lower(self):
        return self.__lower

    @lower.setter
    def lower(self, lower: int):
        self.__lower = lower


    @property
    def owningUpper(self):
        return self.__owningUpper

    @owningUpper.setter
    def owningUpper(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Kernel_MultiplicityElement__owningUpper", None)
        self.__owningUpper = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ValueSpecification"):
                opp_val = getattr(old_value, "ValueSpecification", None)
                if opp_val == self:
                    setattr(old_value, "ValueSpecification", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ValueSpecification"):
                opp_val = getattr(value, "ValueSpecification", None)
                setattr(value, "ValueSpecification", self)

    @property
    def owningLower(self):
        return self.__owningLower

    @owningLower.setter
    def owningLower(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Kernel_MultiplicityElement__owningLower", None)
        self.__owningLower = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ValueSpecification43"):
                opp_val = getattr(old_value, "ValueSpecification43", None)
                if opp_val == self:
                    setattr(old_value, "ValueSpecification43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ValueSpecification43"):
                opp_val = getattr(value, "ValueSpecification43", None)
                setattr(value, "ValueSpecification43", self)

class Classes_Kernel_Comment(Element):

    def __init__(self, body: str, ownedComment: "Element" = None, Classes_Kernel_Comment: set["Element"] = None, Element31: "Classes_Kernel_Comment" = None, Element33: "Classes_Kernel_Comment" = None, Element68: "Classes_Kernel_Constraint" = None, Element35: "Classes_Kernel_Relationship" = None, Element37: "Classes_Kernel_DirectedRelationship" = None, Element40: "Classes_Kernel_DirectedRelationship" = None, Element3: "Classes_Kernel_Element" = None, Element: "Classes_Kernel_Element" = None):
        self.body = body
        self.ownedComment = ownedComment
        self.Classes_Kernel_Comment = Classes_Kernel_Comment if Classes_Kernel_Comment is not None else set()
        
        pass
    @property
    def body(self):
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body


    @property
    def ownedComment(self):
        return self.__ownedComment

    @ownedComment.setter
    def ownedComment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Kernel_Comment__ownedComment", None)
        self.__ownedComment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Element31"):
                opp_val = getattr(old_value, "Element31", None)
                if opp_val == self:
                    setattr(old_value, "Element31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Element31"):
                opp_val = getattr(value, "Element31", None)
                setattr(value, "Element31", self)

    @property
    def Classes_Kernel_Comment(self):
        return self.__Classes_Kernel_Comment

    @Classes_Kernel_Comment.setter
    def Classes_Kernel_Comment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Kernel_Comment__Classes_Kernel_Comment", None)
        self.__Classes_Kernel_Comment = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Element33"):
                    opp_val = getattr(item, "Element33", None)
                    
                    if opp_val == self:
                        setattr(item, "Element33", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Element33"):
                    opp_val = getattr(item, "Element33", None)
                    
                    setattr(item, "Element33", self)
                    

class Classes_Kernel_Slot(Element):

    pass
class Classes_Kernel_NamedElement(Element):

    def __init__(self, name: str, qualifiedName: str, visibility: str, ownedMember: "Namespace" = None, client: set["Dependency"] = None, Element31: "Classes_Kernel_Comment" = None, Element33: "Classes_Kernel_Comment" = None, Element68: "Classes_Kernel_Constraint" = None, Element35: "Classes_Kernel_Relationship" = None, Element37: "Classes_Kernel_DirectedRelationship" = None, Element40: "Classes_Kernel_DirectedRelationship" = None, Element3: "Classes_Kernel_Element" = None, Element: "Classes_Kernel_Element" = None):
        self.name = name
        self.qualifiedName = qualifiedName
        self.visibility = visibility
        self.ownedMember = ownedMember
        self.client = client if client is not None else set()
        
        pass
    @property
    def visibility(self):
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def qualifiedName(self):
        return self.__qualifiedName

    @qualifiedName.setter
    def qualifiedName(self, qualifiedName: str):
        self.__qualifiedName = qualifiedName


    @property
    def ownedMember(self):
        return self.__ownedMember

    @ownedMember.setter
    def ownedMember(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Kernel_NamedElement__ownedMember", None)
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
    def client(self):
        return self.__client

    @client.setter
    def client(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Kernel_NamedElement__client", None)
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
                    

class Classes_Kernel_Relationship(Element):

    pass
class Comment:

    pass
class Classes_Kernel_Element(ABC):

    pass