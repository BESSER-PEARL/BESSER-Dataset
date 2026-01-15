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
class VisibilityKind(Enum):
    package = "package"
    public = "public"
    private = "private"
    protected = "protected"


############################################
# Definition of Classes
############################################

class Kernel_Association:

    pass
class Kernel_Class:

    pass
class Classes_AssociationClasses_AssociationClass(Kernel_Class, Kernel_Association):

    pass
class InterfaceRealization:

    pass
class BehavioredClassifier:

    pass
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
class Classes_Interfaces_InterfaceRealization(Realization):

    pass
class Kernel_Classifier:

    pass
class Kernel_Relationship:

    pass
class Classes_Kernel_Association(Kernel_Relationship, Kernel_Classifier):

    def __init__(self, isDerived: bool, Classes_Kernel_Association: set["Property"] = None, Property202: set["Property"] = None, Property205: set["Property"] = None):
        self.isDerived = isDerived
        self.Classes_Kernel_Association = Classes_Kernel_Association if Classes_Kernel_Association is not None else set()
        self.Property202 = Property202 if Property202 is not None else set()
        self.Property205 = Property205 if Property205 is not None else set()
        
    @property
    def isDerived(self) -> bool:
        return self.__isDerived

    @isDerived.setter
    def isDerived(self, isDerived: bool):
        self.__isDerived = isDerived

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
                if hasattr(item, "Property200"):
                    opp_val = getattr(item, "Property200", None)
                    
                    if opp_val == self:
                        setattr(item, "Property200", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Property200"):
                    opp_val = getattr(item, "Property200", None)
                    
                    setattr(item, "Property200", self)
                    

    @property
    def Property202(self):
        return self.__Property202

    @Property202.setter
    def Property202(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Kernel_Association__Property202", None)
        self.__Property202 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Kernel203"):
                    opp_val = getattr(item, "Kernel203", None)
                    
                    if opp_val == self:
                        setattr(item, "Kernel203", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Kernel203"):
                    opp_val = getattr(item, "Kernel203", None)
                    
                    setattr(item, "Kernel203", self)
                    

    @property
    def Property205(self):
        return self.__Property205

    @Property205.setter
    def Property205(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Kernel_Association__Property205", None)
        self.__Property205 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Kernel206"):
                    opp_val = getattr(item, "Kernel206", None)
                    
                    if opp_val == self:
                        setattr(item, "Kernel206", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Kernel206"):
                    opp_val = getattr(item, "Kernel206", None)
                    
                    setattr(item, "Kernel206", self)
                    

class Operation:

    pass
class Enumeration:

    pass
class EnumerationLiteral:

    pass
class BehavioralFeature:

    pass
class TypedElement:

    pass
class Classes_Kernel_Parameter(TypedElement):

    def __init__(self, default: str, Classes_Kernel_Parameter: "BehavioralFeature" = None, Classes_Kernel_Parameter167: "ValueSpecification" = None):
        self.default = default
        self.Classes_Kernel_Parameter = Classes_Kernel_Parameter
        self.Classes_Kernel_Parameter167 = Classes_Kernel_Parameter167
        
    @property
    def default(self) -> str:
        return self.__default

    @default.setter
    def default(self, default: str):
        self.__default = default

    @property
    def Classes_Kernel_Parameter167(self):
        return self.__Classes_Kernel_Parameter167

    @Classes_Kernel_Parameter167.setter
    def Classes_Kernel_Parameter167(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Kernel_Parameter__Classes_Kernel_Parameter167", None)
        self.__Classes_Kernel_Parameter167 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ValueSpecification168"):
                opp_val = getattr(old_value, "ValueSpecification168", None)
                if opp_val == self:
                    setattr(old_value, "ValueSpecification168", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ValueSpecification168"):
                opp_val = getattr(value, "ValueSpecification168", None)
                setattr(value, "ValueSpecification168", self)

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
class Classes_Kernel_Operation(BehavioralFeature):

    def __init__(self, isQuery: bool, isOrdered: bool, isUnique: bool, upper: int, lower: int, Classes_Kernel_Operation: "Type" = None, Classes_Kernel_Operation172: set["Constraint"] = None, Classes_Kernel_Operation175: set["Constraint"] = None, Classes_Kernel_Operation178: set["Constraint"] = None, Class181: "Class" = None, DataType184: "DataType" = None, Interface187: "Interface" = None, BehavioralFeature: "Classes_Kernel_Parameter"):
        self.isQuery = isQuery
        self.isOrdered = isOrdered
        self.isUnique = isUnique
        self.upper = upper
        self.lower = lower
        self.Classes_Kernel_Operation = Classes_Kernel_Operation
        self.Classes_Kernel_Operation172 = Classes_Kernel_Operation172 if Classes_Kernel_Operation172 is not None else set()
        self.Classes_Kernel_Operation175 = Classes_Kernel_Operation175 if Classes_Kernel_Operation175 is not None else set()
        self.Classes_Kernel_Operation178 = Classes_Kernel_Operation178 if Classes_Kernel_Operation178 is not None else set()
        self.Class181 = Class181
        self.DataType184 = DataType184
        self.Interface187 = Interface187
        
    @property
    def lower(self) -> int:
        return self.__lower

    @lower.setter
    def lower(self, lower: int):
        self.__lower = lower

    @property
    def upper(self) -> int:
        return self.__upper

    @upper.setter
    def upper(self, upper: int):
        self.__upper = upper

    @property
    def isQuery(self) -> bool:
        return self.__isQuery

    @isQuery.setter
    def isQuery(self, isQuery: bool):
        self.__isQuery = isQuery

    @property
    def isOrdered(self) -> bool:
        return self.__isOrdered

    @isOrdered.setter
    def isOrdered(self, isOrdered: bool):
        self.__isOrdered = isOrdered

    @property
    def isUnique(self) -> bool:
        return self.__isUnique

    @isUnique.setter
    def isUnique(self, isUnique: bool):
        self.__isUnique = isUnique

    @property
    def Classes_Kernel_Operation172(self):
        return self.__Classes_Kernel_Operation172

    @Classes_Kernel_Operation172.setter
    def Classes_Kernel_Operation172(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Kernel_Operation__Classes_Kernel_Operation172", None)
        self.__Classes_Kernel_Operation172 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Constraint173"):
                    opp_val = getattr(item, "Constraint173", None)
                    
                    if opp_val == self:
                        setattr(item, "Constraint173", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Constraint173"):
                    opp_val = getattr(item, "Constraint173", None)
                    
                    setattr(item, "Constraint173", self)
                    

    @property
    def Interface187(self):
        return self.__Interface187

    @Interface187.setter
    def Interface187(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Kernel_Operation__Interface187", None)
        self.__Interface187 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Interfaces188"):
                opp_val = getattr(old_value, "Interfaces188", None)
                if opp_val == self:
                    setattr(old_value, "Interfaces188", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Interfaces188"):
                opp_val = getattr(value, "Interfaces188", None)
                setattr(value, "Interfaces188", self)

    @property
    def DataType184(self):
        return self.__DataType184

    @DataType184.setter
    def DataType184(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Kernel_Operation__DataType184", None)
        self.__DataType184 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Kernel185"):
                opp_val = getattr(old_value, "Kernel185", None)
                if opp_val == self:
                    setattr(old_value, "Kernel185", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Kernel185"):
                opp_val = getattr(value, "Kernel185", None)
                setattr(value, "Kernel185", self)

    @property
    def Classes_Kernel_Operation175(self):
        return self.__Classes_Kernel_Operation175

    @Classes_Kernel_Operation175.setter
    def Classes_Kernel_Operation175(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Kernel_Operation__Classes_Kernel_Operation175", None)
        self.__Classes_Kernel_Operation175 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Constraint176"):
                    opp_val = getattr(item, "Constraint176", None)
                    
                    if opp_val == self:
                        setattr(item, "Constraint176", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Constraint176"):
                    opp_val = getattr(item, "Constraint176", None)
                    
                    setattr(item, "Constraint176", self)
                    

    @property
    def Classes_Kernel_Operation178(self):
        return self.__Classes_Kernel_Operation178

    @Classes_Kernel_Operation178.setter
    def Classes_Kernel_Operation178(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Kernel_Operation__Classes_Kernel_Operation178", None)
        self.__Classes_Kernel_Operation178 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Constraint179"):
                    opp_val = getattr(item, "Constraint179", None)
                    
                    if opp_val == self:
                        setattr(item, "Constraint179", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Constraint179"):
                    opp_val = getattr(item, "Constraint179", None)
                    
                    setattr(item, "Constraint179", self)
                    

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
            if hasattr(old_value, "Type170"):
                opp_val = getattr(old_value, "Type170", None)
                if opp_val == self:
                    setattr(old_value, "Type170", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Type170"):
                opp_val = getattr(value, "Type170", None)
                setattr(value, "Type170", self)

    @property
    def Class181(self):
        return self.__Class181

    @Class181.setter
    def Class181(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Kernel_Operation__Class181", None)
        self.__Class181 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Kernel182"):
                opp_val = getattr(old_value, "Kernel182", None)
                if opp_val == self:
                    setattr(old_value, "Kernel182", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Kernel182"):
                opp_val = getattr(value, "Kernel182", None)
                setattr(value, "Kernel182", self)

class Class:

    pass
class Kernel_MultiplicityElement:

    pass
class Kernel_Feature:

    pass
class GeneralizationSet:

    pass
class Substitution:

    pass
class Generalization:

    pass
class Property:

    pass
class Feature:

    pass
class Association:

    pass
class Classifier:

    pass
class Classes_Interfaces_Interface(Classifier):

    pass
class Classes_Interfaces_BehavioredClassifier(Classifier):

    pass
class Classes_Kernel_DataType(Classifier):

    pass
class Classes_Kernel_Class(Classifier):

    pass
class Classes_Kernel_InstanceValue:

    pass
class Kernel_Type:

    pass
class Kernel_RedefinableElement:

    pass
class RedefinableElement:

    pass
class Classes_Kernel_Feature(RedefinableElement):

    def __init__(self, isStatic: bool, Classifier124: set["Classifier"] = None, RedefinableElement: "Classes_Kernel_RedefinableElement"):
        self.isStatic = isStatic
        self.Classifier124 = Classifier124 if Classifier124 is not None else set()
        
    @property
    def isStatic(self) -> bool:
        return self.__isStatic

    @isStatic.setter
    def isStatic(self, isStatic: bool):
        self.__isStatic = isStatic

    @property
    def Classifier124(self):
        return self.__Classifier124

    @Classifier124.setter
    def Classifier124(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Kernel_Feature__Classifier124", None)
        self.__Classifier124 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Kernel125"):
                    opp_val = getattr(item, "Kernel125", None)
                    
                    if opp_val == self:
                        setattr(item, "Kernel125", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Kernel125"):
                    opp_val = getattr(item, "Kernel125", None)
                    
                    setattr(item, "Kernel125", self)
                    

class StructuralFeature:

    pass
class Classes_Kernel_Property(StructuralFeature):

    def __init__(self, default: str, isComposite: bool, isID: bool, aggregation: str, isDerived: bool, isDerivedUnion: bool, Classes_Kernel_Property: set["Property"] = None, Classes_Kernel_Property131: "ValueSpecification" = None, Classes_Kernel_Property134: "Property" = None, Classes_Kernel_Property137: "Property" = None, Association: "Association" = None, Class: "Class" = None, Association142: "Association" = None, DataType: "DataType" = None, Interface: "Interface" = None, Property148: set["Property"] = None, Property151: "Property" = None, StructuralFeature: "Classes_Kernel_Slot"):
        self.default = default
        self.isComposite = isComposite
        self.isID = isID
        self.aggregation = aggregation
        self.isDerived = isDerived
        self.isDerivedUnion = isDerivedUnion
        self.Classes_Kernel_Property = Classes_Kernel_Property if Classes_Kernel_Property is not None else set()
        self.Classes_Kernel_Property131 = Classes_Kernel_Property131
        self.Classes_Kernel_Property134 = Classes_Kernel_Property134
        self.Classes_Kernel_Property137 = Classes_Kernel_Property137
        self.Association = Association
        self.Class = Class
        self.Association142 = Association142
        self.DataType = DataType
        self.Interface = Interface
        self.Property148 = Property148 if Property148 is not None else set()
        self.Property151 = Property151
        
    @property
    def default(self) -> str:
        return self.__default

    @default.setter
    def default(self, default: str):
        self.__default = default

    @property
    def aggregation(self) -> str:
        return self.__aggregation

    @aggregation.setter
    def aggregation(self, aggregation: str):
        self.__aggregation = aggregation

    @property
    def isDerived(self) -> bool:
        return self.__isDerived

    @isDerived.setter
    def isDerived(self, isDerived: bool):
        self.__isDerived = isDerived

    @property
    def isDerivedUnion(self) -> bool:
        return self.__isDerivedUnion

    @isDerivedUnion.setter
    def isDerivedUnion(self, isDerivedUnion: bool):
        self.__isDerivedUnion = isDerivedUnion

    @property
    def isComposite(self) -> bool:
        return self.__isComposite

    @isComposite.setter
    def isComposite(self, isComposite: bool):
        self.__isComposite = isComposite

    @property
    def isID(self) -> bool:
        return self.__isID

    @isID.setter
    def isID(self, isID: bool):
        self.__isID = isID

    @property
    def DataType(self):
        return self.__DataType

    @DataType.setter
    def DataType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Kernel_Property__DataType", None)
        self.__DataType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Kernel145"):
                opp_val = getattr(old_value, "Kernel145", None)
                if opp_val == self:
                    setattr(old_value, "Kernel145", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Kernel145"):
                opp_val = getattr(value, "Kernel145", None)
                setattr(value, "Kernel145", self)

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
                if hasattr(item, "Property129"):
                    opp_val = getattr(item, "Property129", None)
                    
                    if opp_val == self:
                        setattr(item, "Property129", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Property129"):
                    opp_val = getattr(item, "Property129", None)
                    
                    setattr(item, "Property129", self)
                    

    @property
    def Property148(self):
        return self.__Property148

    @Property148.setter
    def Property148(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Kernel_Property__Property148", None)
        self.__Property148 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Kernel149"):
                    opp_val = getattr(item, "Kernel149", None)
                    
                    if opp_val == self:
                        setattr(item, "Kernel149", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Kernel149"):
                    opp_val = getattr(item, "Kernel149", None)
                    
                    setattr(item, "Kernel149", self)
                    

    @property
    def Classes_Kernel_Property137(self):
        return self.__Classes_Kernel_Property137

    @Classes_Kernel_Property137.setter
    def Classes_Kernel_Property137(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Kernel_Property__Classes_Kernel_Property137", None)
        self.__Classes_Kernel_Property137 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Property138"):
                opp_val = getattr(old_value, "Property138", None)
                if opp_val == self:
                    setattr(old_value, "Property138", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Property138"):
                opp_val = getattr(value, "Property138", None)
                setattr(value, "Property138", self)

    @property
    def Class(self):
        return self.__Class

    @Class.setter
    def Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Kernel_Property__Class", None)
        self.__Class = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Kernel127"):
                opp_val = getattr(old_value, "Kernel127", None)
                if opp_val == self:
                    setattr(old_value, "Kernel127", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Kernel127"):
                opp_val = getattr(value, "Kernel127", None)
                setattr(value, "Kernel127", self)

    @property
    def Property151(self):
        return self.__Property151

    @Property151.setter
    def Property151(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Kernel_Property__Property151", None)
        self.__Property151 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Kernel152"):
                opp_val = getattr(old_value, "Kernel152", None)
                if opp_val == self:
                    setattr(old_value, "Kernel152", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Kernel152"):
                opp_val = getattr(value, "Kernel152", None)
                setattr(value, "Kernel152", self)

    @property
    def Interface(self):
        return self.__Interface

    @Interface.setter
    def Interface(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Kernel_Property__Interface", None)
        self.__Interface = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Interfaces"):
                opp_val = getattr(old_value, "Interfaces", None)
                if opp_val == self:
                    setattr(old_value, "Interfaces", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Interfaces"):
                opp_val = getattr(value, "Interfaces", None)
                setattr(value, "Interfaces", self)

    @property
    def Classes_Kernel_Property134(self):
        return self.__Classes_Kernel_Property134

    @Classes_Kernel_Property134.setter
    def Classes_Kernel_Property134(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Kernel_Property__Classes_Kernel_Property134", None)
        self.__Classes_Kernel_Property134 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Property135"):
                opp_val = getattr(old_value, "Property135", None)
                if opp_val == self:
                    setattr(old_value, "Property135", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Property135"):
                opp_val = getattr(value, "Property135", None)
                setattr(value, "Property135", self)

    @property
    def Association(self):
        return self.__Association

    @Association.setter
    def Association(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Kernel_Property__Association", None)
        self.__Association = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Kernel140"):
                opp_val = getattr(old_value, "Kernel140", None)
                if opp_val == self:
                    setattr(old_value, "Kernel140", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Kernel140"):
                opp_val = getattr(value, "Kernel140", None)
                setattr(value, "Kernel140", self)

    @property
    def Association142(self):
        return self.__Association142

    @Association142.setter
    def Association142(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Kernel_Property__Association142", None)
        self.__Association142 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Kernel143"):
                opp_val = getattr(old_value, "Kernel143", None)
                if opp_val == self:
                    setattr(old_value, "Kernel143", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Kernel143"):
                opp_val = getattr(value, "Kernel143", None)
                setattr(value, "Kernel143", self)

    @property
    def Classes_Kernel_Property131(self):
        return self.__Classes_Kernel_Property131

    @Classes_Kernel_Property131.setter
    def Classes_Kernel_Property131(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Kernel_Property__Classes_Kernel_Property131", None)
        self.__Classes_Kernel_Property131 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ValueSpecification132"):
                opp_val = getattr(old_value, "ValueSpecification132", None)
                if opp_val == self:
                    setattr(old_value, "ValueSpecification132", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ValueSpecification132"):
                opp_val = getattr(value, "ValueSpecification132", None)
                setattr(value, "ValueSpecification132", self)

class InstanceSpecification:

    pass
class Classes_Kernel_EnumerationLiteral(InstanceSpecification):

    pass
class Slot:

    pass
class MultiplicityElement:

    pass
class Kernel_TypedElement:

    pass
class Classes_Kernel_StructuralFeature(Kernel_Feature, Kernel_MultiplicityElement, Kernel_TypedElement):

    def __init__(self, isReadOnly: bool):
        self.isReadOnly = isReadOnly
        
    @property
    def isReadOnly(self) -> bool:
        return self.__isReadOnly

    @isReadOnly.setter
    def isReadOnly(self, isReadOnly: bool):
        self.__isReadOnly = isReadOnly

class ValueSpecification:

    pass
class LiteralSpecification:

    pass
class Classes_Kernel_LiteralReal(LiteralSpecification):

    pass
class Classes_Kernel_LiteralUnilimitedNatural(LiteralSpecification):

    pass
class Classes_Kernel_LiteralInteger(LiteralSpecification):

    pass
class Classes_Kernel_LiteralString(LiteralSpecification):

    pass
class Classes_Kernel_LiteralBoolean(LiteralSpecification):

    pass
class Classes_Kernel_LiteralNull(LiteralSpecification):

    pass
class Classes_Kernel_LiteralSpecification(ValueSpecification):

    pass
class Classes_Kernel_OpaqueExpression(ValueSpecification):

    def __init__(self, body: str, language: str, ValueSpecification168: "Classes_Kernel_Parameter", Kernel100: "Classes_Kernel_Slot", Kernel58: "Classes_Kernel_MultiplicityElement", ValueSpecification77: "Classes_Kernel_Expression", Kernel85: "Classes_Kernel_InstanceSpecification", ValueSpecification132: "Classes_Kernel_Property", Kernel55: "Classes_Kernel_MultiplicityElement", Kernel94: "Classes_Kernel_Constraint"):
        self.body = body
        self.language = language
        
    @property
    def language(self) -> str:
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language

    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

class Classes_Kernel_Expression(ValueSpecification):

    def __init__(self, symbol: str, Classes_Kernel_Expression: "ValueSpecification" = None, ValueSpecification168: "Classes_Kernel_Parameter", Kernel100: "Classes_Kernel_Slot", Kernel58: "Classes_Kernel_MultiplicityElement", ValueSpecification77: "Classes_Kernel_Expression", Kernel85: "Classes_Kernel_InstanceSpecification", ValueSpecification132: "Classes_Kernel_Property", Kernel55: "Classes_Kernel_MultiplicityElement", Kernel94: "Classes_Kernel_Constraint"):
        self.symbol = symbol
        self.Classes_Kernel_Expression = Classes_Kernel_Expression
        
    @property
    def symbol(self) -> str:
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
            if hasattr(old_value, "ValueSpecification77"):
                opp_val = getattr(old_value, "ValueSpecification77", None)
                if opp_val == self:
                    setattr(old_value, "ValueSpecification77", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ValueSpecification77"):
                opp_val = getattr(value, "ValueSpecification77", None)
                setattr(value, "ValueSpecification77", self)

class PackageMerge:

    pass
class Type:

    pass
class Kernel_PackageableElement:

    pass
class Classes_Kernel_ValueSpecification(Kernel_TypedElement, Kernel_PackageableElement):

    pass
class Classes_Dependencies_Dependency(Kernel_DirectedRelationship, Kernel_PackageableElement):

    pass
class Kernel_Namespace:

    pass
class Classes_Kernel_Classifier(Kernel_Type, Kernel_Namespace, Kernel_RedefinableElement):

    def __init__(self, isAbstract: bool, isFinalSpecialization: bool, Classes_Kernel_Classifier: set["NamedElement"] = None, Feature: set["Feature"] = None, Classes_Kernel_Classifier111: set["Property"] = None, Classes_Kernel_Classifier113: set["Classifier"] = None, Classes_Kernel_Classifier116: set["Classifier"] = None, Generalization: set["Generalization"] = None, Substitution: set["Substitution"] = None, GeneralizationSet: set["GeneralizationSet"] = None):
        self.isAbstract = isAbstract
        self.isFinalSpecialization = isFinalSpecialization
        self.Classes_Kernel_Classifier = Classes_Kernel_Classifier if Classes_Kernel_Classifier is not None else set()
        self.Feature = Feature if Feature is not None else set()
        self.Classes_Kernel_Classifier111 = Classes_Kernel_Classifier111 if Classes_Kernel_Classifier111 is not None else set()
        self.Classes_Kernel_Classifier113 = Classes_Kernel_Classifier113 if Classes_Kernel_Classifier113 is not None else set()
        self.Classes_Kernel_Classifier116 = Classes_Kernel_Classifier116 if Classes_Kernel_Classifier116 is not None else set()
        self.Generalization = Generalization if Generalization is not None else set()
        self.Substitution = Substitution if Substitution is not None else set()
        self.GeneralizationSet = GeneralizationSet if GeneralizationSet is not None else set()
        
    @property
    def isFinalSpecialization(self) -> bool:
        return self.__isFinalSpecialization

    @isFinalSpecialization.setter
    def isFinalSpecialization(self, isFinalSpecialization: bool):
        self.__isFinalSpecialization = isFinalSpecialization

    @property
    def isAbstract(self) -> bool:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: bool):
        self.__isAbstract = isAbstract

    @property
    def GeneralizationSet(self):
        return self.__GeneralizationSet

    @GeneralizationSet.setter
    def GeneralizationSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Kernel_Classifier__GeneralizationSet", None)
        self.__GeneralizationSet = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PowerTypes"):
                    opp_val = getattr(item, "PowerTypes", None)
                    
                    if opp_val == self:
                        setattr(item, "PowerTypes", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PowerTypes"):
                    opp_val = getattr(item, "PowerTypes", None)
                    
                    setattr(item, "PowerTypes", self)
                    

    @property
    def Substitution(self):
        return self.__Substitution

    @Substitution.setter
    def Substitution(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Kernel_Classifier__Substitution", None)
        self.__Substitution = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Dependencies121"):
                    opp_val = getattr(item, "Dependencies121", None)
                    
                    if opp_val == self:
                        setattr(item, "Dependencies121", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Dependencies121"):
                    opp_val = getattr(item, "Dependencies121", None)
                    
                    setattr(item, "Dependencies121", self)
                    

    @property
    def Classes_Kernel_Classifier116(self):
        return self.__Classes_Kernel_Classifier116

    @Classes_Kernel_Classifier116.setter
    def Classes_Kernel_Classifier116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Kernel_Classifier__Classes_Kernel_Classifier116", None)
        self.__Classes_Kernel_Classifier116 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Classifier117"):
                    opp_val = getattr(item, "Classifier117", None)
                    
                    if opp_val == self:
                        setattr(item, "Classifier117", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Classifier117"):
                    opp_val = getattr(item, "Classifier117", None)
                    
                    setattr(item, "Classifier117", self)
                    

    @property
    def Generalization(self):
        return self.__Generalization

    @Generalization.setter
    def Generalization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Kernel_Classifier__Generalization", None)
        self.__Generalization = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Kernel119"):
                    opp_val = getattr(item, "Kernel119", None)
                    
                    if opp_val == self:
                        setattr(item, "Kernel119", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Kernel119"):
                    opp_val = getattr(item, "Kernel119", None)
                    
                    setattr(item, "Kernel119", self)
                    

    @property
    def Feature(self):
        return self.__Feature

    @Feature.setter
    def Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Kernel_Classifier__Feature", None)
        self.__Feature = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Kernel109"):
                    opp_val = getattr(item, "Kernel109", None)
                    
                    if opp_val == self:
                        setattr(item, "Kernel109", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Kernel109"):
                    opp_val = getattr(item, "Kernel109", None)
                    
                    setattr(item, "Kernel109", self)
                    

    @property
    def Classes_Kernel_Classifier113(self):
        return self.__Classes_Kernel_Classifier113

    @Classes_Kernel_Classifier113.setter
    def Classes_Kernel_Classifier113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Kernel_Classifier__Classes_Kernel_Classifier113", None)
        self.__Classes_Kernel_Classifier113 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Classifier114"):
                    opp_val = getattr(item, "Classifier114", None)
                    
                    if opp_val == self:
                        setattr(item, "Classifier114", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Classifier114"):
                    opp_val = getattr(item, "Classifier114", None)
                    
                    setattr(item, "Classifier114", self)
                    

    @property
    def Classes_Kernel_Classifier111(self):
        return self.__Classes_Kernel_Classifier111

    @Classes_Kernel_Classifier111.setter
    def Classes_Kernel_Classifier111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Kernel_Classifier__Classes_Kernel_Classifier111", None)
        self.__Classes_Kernel_Classifier111 = value if value is not None else set()
        
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
                if hasattr(item, "NamedElement107"):
                    opp_val = getattr(item, "NamedElement107", None)
                    
                    if opp_val == self:
                        setattr(item, "NamedElement107", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "NamedElement107"):
                    opp_val = getattr(item, "NamedElement107", None)
                    
                    setattr(item, "NamedElement107", self)
                    

class Classes_Kernel_BehavioralFeature(Kernel_Namespace, Kernel_Feature):

    pass
class Classes_Kernel_Package(Kernel_Namespace, Kernel_PackageableElement):

    def __init__(self, URI: str, Package31: set["Package"] = None, Package34: "Package" = None, Classes_Kernel_Package: set["PackageableElement"] = None, Type: set["Type"] = None, PackageMerge: set["PackageMerge"] = None):
        self.URI = URI
        self.Package31 = Package31 if Package31 is not None else set()
        self.Package34 = Package34
        self.Classes_Kernel_Package = Classes_Kernel_Package if Classes_Kernel_Package is not None else set()
        self.Type = Type if Type is not None else set()
        self.PackageMerge = PackageMerge if PackageMerge is not None else set()
        
    @property
    def URI(self) -> str:
        return self.__URI

    @URI.setter
    def URI(self, URI: str):
        self.__URI = URI

    @property
    def Package34(self):
        return self.__Package34

    @Package34.setter
    def Package34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Kernel_Package__Package34", None)
        self.__Package34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Kernel35"):
                opp_val = getattr(old_value, "Kernel35", None)
                if opp_val == self:
                    setattr(old_value, "Kernel35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Kernel35"):
                opp_val = getattr(value, "Kernel35", None)
                setattr(value, "Kernel35", self)

    @property
    def Type(self):
        return self.__Type

    @Type.setter
    def Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Kernel_Package__Type", None)
        self.__Type = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Kernel39"):
                    opp_val = getattr(item, "Kernel39", None)
                    
                    if opp_val == self:
                        setattr(item, "Kernel39", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Kernel39"):
                    opp_val = getattr(item, "Kernel39", None)
                    
                    setattr(item, "Kernel39", self)
                    

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
                if hasattr(item, "PackageableElement37"):
                    opp_val = getattr(item, "PackageableElement37", None)
                    
                    if opp_val == self:
                        setattr(item, "PackageableElement37", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PackageableElement37"):
                    opp_val = getattr(item, "PackageableElement37", None)
                    
                    setattr(item, "PackageableElement37", self)
                    

    @property
    def PackageMerge(self):
        return self.__PackageMerge

    @PackageMerge.setter
    def PackageMerge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Kernel_Package__PackageMerge", None)
        self.__PackageMerge = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Kernel41"):
                    opp_val = getattr(item, "Kernel41", None)
                    
                    if opp_val == self:
                        setattr(item, "Kernel41", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Kernel41"):
                    opp_val = getattr(item, "Kernel41", None)
                    
                    setattr(item, "Kernel41", self)
                    

    @property
    def Package31(self):
        return self.__Package31

    @Package31.setter
    def Package31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Kernel_Package__Package31", None)
        self.__Package31 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Kernel32"):
                    opp_val = getattr(item, "Kernel32", None)
                    
                    if opp_val == self:
                        setattr(item, "Kernel32", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Kernel32"):
                    opp_val = getattr(item, "Kernel32", None)
                    
                    setattr(item, "Kernel32", self)
                    

class Package:

    pass
class Relationship:

    pass
class Classes_Kernel_DirectedRelationship(Relationship):

    pass
class PackageableElement:

    pass
class Classes_Kernel_InstanceSpecification(PackageableElement):

    pass
class Classes_Kernel_Constraint(PackageableElement):

    pass
class Classes_PowerTypes_GeneralizationSet(PackageableElement):

    def __init__(self, isCovering: bool, isDisjoint: bool, Classifier251: "Classifier" = None, Generalization254: set["Generalization"] = None, PackageableElement22: "Classes_Kernel_ElementImport", PackageableElement37: "Classes_Kernel_Package", PackageableElement: "Classes_Kernel_Namespace"):
        self.isCovering = isCovering
        self.isDisjoint = isDisjoint
        self.Classifier251 = Classifier251
        self.Generalization254 = Generalization254 if Generalization254 is not None else set()
        
    @property
    def isDisjoint(self) -> bool:
        return self.__isDisjoint

    @isDisjoint.setter
    def isDisjoint(self, isDisjoint: bool):
        self.__isDisjoint = isDisjoint

    @property
    def isCovering(self) -> bool:
        return self.__isCovering

    @isCovering.setter
    def isCovering(self, isCovering: bool):
        self.__isCovering = isCovering

    @property
    def Generalization254(self):
        return self.__Generalization254

    @Generalization254.setter
    def Generalization254(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_PowerTypes_GeneralizationSet__Generalization254", None)
        self.__Generalization254 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Kernel255"):
                    opp_val = getattr(item, "Kernel255", None)
                    
                    if opp_val == self:
                        setattr(item, "Kernel255", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Kernel255"):
                    opp_val = getattr(item, "Kernel255", None)
                    
                    setattr(item, "Kernel255", self)
                    

    @property
    def Classifier251(self):
        return self.__Classifier251

    @Classifier251.setter
    def Classifier251(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_PowerTypes_GeneralizationSet__Classifier251", None)
        self.__Classifier251 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Kernel252"):
                opp_val = getattr(old_value, "Kernel252", None)
                if opp_val == self:
                    setattr(old_value, "Kernel252", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Kernel252"):
                opp_val = getattr(value, "Kernel252", None)
                setattr(value, "Kernel252", self)

class Classes_Kernel_Type(PackageableElement):

    pass
class NamedElement:

    pass
class Classes_Kernel_TypedElement(NamedElement):

    pass
class Classes_Kernel_RedefinableElement(NamedElement):

    def __init__(self, isLeaf: bool, Classes_Kernel_RedefinableElement: set["RedefinableElement"] = None, Classes_Kernel_RedefinableElement104: set["Classifier"] = None, Kernel224: "Classes_Dependencies_Dependency", Kernel14: "Classes_Kernel_Namespace", NamedElement226: "Classes_Dependencies_Dependency", NamedElement: "Classes_Kernel_Namespace", NamedElement107: "Classes_Kernel_Classifier"):
        self.isLeaf = isLeaf
        self.Classes_Kernel_RedefinableElement = Classes_Kernel_RedefinableElement if Classes_Kernel_RedefinableElement is not None else set()
        self.Classes_Kernel_RedefinableElement104 = Classes_Kernel_RedefinableElement104 if Classes_Kernel_RedefinableElement104 is not None else set()
        
    @property
    def isLeaf(self) -> bool:
        return self.__isLeaf

    @isLeaf.setter
    def isLeaf(self, isLeaf: bool):
        self.__isLeaf = isLeaf

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
                    

    @property
    def Classes_Kernel_RedefinableElement104(self):
        return self.__Classes_Kernel_RedefinableElement104

    @Classes_Kernel_RedefinableElement104.setter
    def Classes_Kernel_RedefinableElement104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Kernel_RedefinableElement__Classes_Kernel_RedefinableElement104", None)
        self.__Classes_Kernel_RedefinableElement104 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Classifier105"):
                    opp_val = getattr(item, "Classifier105", None)
                    
                    if opp_val == self:
                        setattr(item, "Classifier105", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Classifier105"):
                    opp_val = getattr(item, "Classifier105", None)
                    
                    setattr(item, "Classifier105", self)
                    

class Classes_Kernel_Namespace(NamedElement):

    pass
class Dependency:

    pass
class Classes_Dependencies_Abstraction(Dependency):

    pass
class Classes_Dependencies_Usage(Dependency):

    pass
class Namespace:

    pass
class Element:

    pass
class Classes_Kernel_MultiplicityElement(Element):

    def __init__(self, isOrdered: bool, isUnique: bool, upper: int, lower: int, ValueSpecification: "ValueSpecification" = None, ValueSpecification57: "ValueSpecification" = None, Element48: "Classes_Kernel_Relationship", Element50: "Classes_Kernel_DirectedRelationship", Kernel44: "Classes_Kernel_Comment", Kernel2: "Classes_Kernel_Element", Element53: "Classes_Kernel_DirectedRelationship", Element46: "Classes_Kernel_Comment", Element91: "Classes_Kernel_Constraint", Kernel5: "Classes_Kernel_Element"):
        self.isOrdered = isOrdered
        self.isUnique = isUnique
        self.upper = upper
        self.lower = lower
        self.ValueSpecification = ValueSpecification
        self.ValueSpecification57 = ValueSpecification57
        
    @property
    def lower(self) -> int:
        return self.__lower

    @lower.setter
    def lower(self, lower: int):
        self.__lower = lower

    @property
    def upper(self) -> int:
        return self.__upper

    @upper.setter
    def upper(self, upper: int):
        self.__upper = upper

    @property
    def isUnique(self) -> bool:
        return self.__isUnique

    @isUnique.setter
    def isUnique(self, isUnique: bool):
        self.__isUnique = isUnique

    @property
    def isOrdered(self) -> bool:
        return self.__isOrdered

    @isOrdered.setter
    def isOrdered(self, isOrdered: bool):
        self.__isOrdered = isOrdered

    @property
    def ValueSpecification(self):
        return self.__ValueSpecification

    @ValueSpecification.setter
    def ValueSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Kernel_MultiplicityElement__ValueSpecification", None)
        self.__ValueSpecification = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Kernel55"):
                opp_val = getattr(old_value, "Kernel55", None)
                if opp_val == self:
                    setattr(old_value, "Kernel55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Kernel55"):
                opp_val = getattr(value, "Kernel55", None)
                setattr(value, "Kernel55", self)

    @property
    def ValueSpecification57(self):
        return self.__ValueSpecification57

    @ValueSpecification57.setter
    def ValueSpecification57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Kernel_MultiplicityElement__ValueSpecification57", None)
        self.__ValueSpecification57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Kernel58"):
                opp_val = getattr(old_value, "Kernel58", None)
                if opp_val == self:
                    setattr(old_value, "Kernel58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Kernel58"):
                opp_val = getattr(value, "Kernel58", None)
                setattr(value, "Kernel58", self)

class Classes_Kernel_Comment(Element):

    def __init__(self, body: str, Classes_Kernel_Comment: set["Element"] = None, Element43: "Element" = None, Element48: "Classes_Kernel_Relationship", Element50: "Classes_Kernel_DirectedRelationship", Kernel44: "Classes_Kernel_Comment", Kernel2: "Classes_Kernel_Element", Element53: "Classes_Kernel_DirectedRelationship", Element46: "Classes_Kernel_Comment", Element91: "Classes_Kernel_Constraint", Kernel5: "Classes_Kernel_Element"):
        self.body = body
        self.Classes_Kernel_Comment = Classes_Kernel_Comment if Classes_Kernel_Comment is not None else set()
        self.Element43 = Element43
        
    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

    @property
    def Element43(self):
        return self.__Element43

    @Element43.setter
    def Element43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Kernel_Comment__Element43", None)
        self.__Element43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Kernel44"):
                opp_val = getattr(old_value, "Kernel44", None)
                if opp_val == self:
                    setattr(old_value, "Kernel44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Kernel44"):
                opp_val = getattr(value, "Kernel44", None)
                setattr(value, "Kernel44", self)

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
                if hasattr(item, "Element46"):
                    opp_val = getattr(item, "Element46", None)
                    
                    if opp_val == self:
                        setattr(item, "Element46", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Element46"):
                    opp_val = getattr(item, "Element46", None)
                    
                    setattr(item, "Element46", self)
                    

class Classes_Kernel_Slot(Element):

    pass
class Classes_Kernel_NamedElement(Element):

    def __init__(self, name: str, qualifiedName: str, visibility: str, Namespace: "Namespace" = None, Dependency: set["Dependency"] = None, Element48: "Classes_Kernel_Relationship", Element50: "Classes_Kernel_DirectedRelationship", Kernel44: "Classes_Kernel_Comment", Kernel2: "Classes_Kernel_Element", Element53: "Classes_Kernel_DirectedRelationship", Element46: "Classes_Kernel_Comment", Element91: "Classes_Kernel_Constraint", Kernel5: "Classes_Kernel_Element"):
        self.name = name
        self.qualifiedName = qualifiedName
        self.visibility = visibility
        self.Namespace = Namespace
        self.Dependency = Dependency if Dependency is not None else set()
        
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
    def qualifiedName(self) -> str:
        return self.__qualifiedName

    @qualifiedName.setter
    def qualifiedName(self, qualifiedName: str):
        self.__qualifiedName = qualifiedName

    @property
    def Namespace(self):
        return self.__Namespace

    @Namespace.setter
    def Namespace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Kernel_NamedElement__Namespace", None)
        self.__Namespace = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Kernel7"):
                opp_val = getattr(old_value, "Kernel7", None)
                if opp_val == self:
                    setattr(old_value, "Kernel7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Kernel7"):
                opp_val = getattr(value, "Kernel7", None)
                setattr(value, "Kernel7", self)

    @property
    def Dependency(self):
        return self.__Dependency

    @Dependency.setter
    def Dependency(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Kernel_NamedElement__Dependency", None)
        self.__Dependency = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Dependencies"):
                    opp_val = getattr(item, "Dependencies", None)
                    
                    if opp_val == self:
                        setattr(item, "Dependencies", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Dependencies"):
                    opp_val = getattr(item, "Dependencies", None)
                    
                    setattr(item, "Dependencies", self)
                    

class Classes_Kernel_Relationship(Element):

    pass
class DirectedRelationship:

    pass
class Classes_Kernel_PackageMerge(DirectedRelationship):

    pass
class Classes_Kernel_PackageImport(DirectedRelationship):

    def __init__(self, visibility: str, Classes_Kernel_PackageImport: "Package" = None, Namespace28: "Namespace" = None):
        self.visibility = visibility
        self.Classes_Kernel_PackageImport = Classes_Kernel_PackageImport
        self.Namespace28 = Namespace28
        
    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

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

    @property
    def Namespace28(self):
        return self.__Namespace28

    @Namespace28.setter
    def Namespace28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Kernel_PackageImport__Namespace28", None)
        self.__Namespace28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Kernel29"):
                opp_val = getattr(old_value, "Kernel29", None)
                if opp_val == self:
                    setattr(old_value, "Kernel29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Kernel29"):
                opp_val = getattr(value, "Kernel29", None)
                setattr(value, "Kernel29", self)

class Classes_Kernel_Generalization(DirectedRelationship):

    def __init__(self, isSubstitutable: bool, Classes_Kernel_Generalization: "Classifier" = None, Classifier156: "Classifier" = None, GeneralizationSet159: set["GeneralizationSet"] = None):
        self.isSubstitutable = isSubstitutable
        self.Classes_Kernel_Generalization = Classes_Kernel_Generalization
        self.Classifier156 = Classifier156
        self.GeneralizationSet159 = GeneralizationSet159 if GeneralizationSet159 is not None else set()
        
    @property
    def isSubstitutable(self) -> bool:
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
        old_value = getattr(self, f"_Classes_Kernel_Generalization__Classes_Kernel_Generalization", None)
        self.__Classes_Kernel_Generalization = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Classifier154"):
                opp_val = getattr(old_value, "Classifier154", None)
                if opp_val == self:
                    setattr(old_value, "Classifier154", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Classifier154"):
                opp_val = getattr(value, "Classifier154", None)
                setattr(value, "Classifier154", self)

    @property
    def Classifier156(self):
        return self.__Classifier156

    @Classifier156.setter
    def Classifier156(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Kernel_Generalization__Classifier156", None)
        self.__Classifier156 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Kernel157"):
                opp_val = getattr(old_value, "Kernel157", None)
                if opp_val == self:
                    setattr(old_value, "Kernel157", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Kernel157"):
                opp_val = getattr(value, "Kernel157", None)
                setattr(value, "Kernel157", self)

    @property
    def GeneralizationSet159(self):
        return self.__GeneralizationSet159

    @GeneralizationSet159.setter
    def GeneralizationSet159(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Kernel_Generalization__GeneralizationSet159", None)
        self.__GeneralizationSet159 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PowerTypes160"):
                    opp_val = getattr(item, "PowerTypes160", None)
                    
                    if opp_val == self:
                        setattr(item, "PowerTypes160", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PowerTypes160"):
                    opp_val = getattr(item, "PowerTypes160", None)
                    
                    setattr(item, "PowerTypes160", self)
                    

class Classes_Kernel_ElementImport(DirectedRelationship):

    def __init__(self, visibility: str, alias: str, Classes_Kernel_ElementImport: "PackageableElement" = None, Namespace24: "Namespace" = None):
        self.visibility = visibility
        self.alias = alias
        self.Classes_Kernel_ElementImport = Classes_Kernel_ElementImport
        self.Namespace24 = Namespace24
        
    @property
    def alias(self) -> str:
        return self.__alias

    @alias.setter
    def alias(self, alias: str):
        self.__alias = alias

    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def Namespace24(self):
        return self.__Namespace24

    @Namespace24.setter
    def Namespace24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Kernel_ElementImport__Namespace24", None)
        self.__Namespace24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Kernel25"):
                opp_val = getattr(old_value, "Kernel25", None)
                if opp_val == self:
                    setattr(old_value, "Kernel25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Kernel25"):
                opp_val = getattr(value, "Kernel25", None)
                setattr(value, "Kernel25", self)

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
            if hasattr(old_value, "PackageableElement22"):
                opp_val = getattr(old_value, "PackageableElement22", None)
                if opp_val == self:
                    setattr(old_value, "PackageableElement22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PackageableElement22"):
                opp_val = getattr(value, "PackageableElement22", None)
                setattr(value, "PackageableElement22", self)

class Classes_Kernel_PackageableElement(NamedElement):

    pass
class Constraint:

    pass
class PackageImport:

    pass
class ElementImport:

    pass
class Comment:

    pass
class Classes_Kernel_Element(ABC):

    pass