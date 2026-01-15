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
    public = "public"
    private = "private"
    protected = "protected"
    package = "package"
class ParameterDirectionKind(Enum):
    in = "in"
    inout = "inout"
    out = "out"
    return = "return"


############################################
# Definition of Classes
############################################

class InstanceSpecification:

    pass
class classes_EnumerationLiteral(InstanceSpecification):

    pass
class Package:

    pass
class classes_Model(Package):

    pass
class DataType:

    pass
class classes_Enumeration(DataType):

    pass
class classes_PrimitiveType(DataType):

    pass
class LiteralSpecification:

    pass
class classes_LiteralNull(LiteralSpecification):

    def __init__(self):
        
    def isNull(self) -> bool:
        # TODO: Implement isNull method
        pass

    def isComputable(self) -> bool:
        # TODO: Implement isComputable method
        pass

class classes_LiteralString(LiteralSpecification):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    def isComputable(self) -> bool:
        # TODO: Implement isComputable method
        pass

    def stringValue(self) -> str:
        # TODO: Implement stringValue method
        pass

class classes_LiteralUnlimitedNatural(LiteralSpecification):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

    def isComputable(self) -> bool:
        # TODO: Implement isComputable method
        pass

    def unlimitedValue(self) -> int:
        # TODO: Implement unlimitedValue method
        pass

class classes_LiteralInteger(LiteralSpecification):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

    def integerValue(self) -> int:
        # TODO: Implement integerValue method
        pass

    def isComputable(self) -> bool:
        # TODO: Implement isComputable method
        pass

class classes_LiteralBoolean(LiteralSpecification):

    def __init__(self, value: bool):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

    def isComputable(self) -> bool:
        # TODO: Implement isComputable method
        pass

    def booleanValue(self) -> bool:
        # TODO: Implement booleanValue method
        pass

class ValueSpecification:

    pass
class classes_LiteralSpecification(ValueSpecification):

    pass
class classes_InstanceValue(ValueSpecification):

    pass
class BehavioralFeature:

    pass
class classes_Operation(BehavioralFeature):

    def __init__(self, query: bool, ordered: bool, unique: bool, lower: str, upper: str, ownedOperation: "classes_Class" = None, classes_Operation: "classes_Operation" = None, classes_Operation81: set["classes_Operation"] = None, classes_Operation84: "classes_Type" = None, Operation: "classes_Class" = None):
        self.query = query
        self.ordered = ordered
        self.unique = unique
        self.lower = lower
        self.upper = upper
        self.ownedOperation = ownedOperation
        self.classes_Operation = classes_Operation
        self.classes_Operation81 = classes_Operation81 if classes_Operation81 is not None else set()
        self.classes_Operation84 = classes_Operation84
        self.Operation = Operation
        
    @property
    def query(self) -> bool:
        return self.__query

    @query.setter
    def query(self, query: bool):
        self.__query = query

    @property
    def ordered(self) -> bool:
        return self.__ordered

    @ordered.setter
    def ordered(self, ordered: bool):
        self.__ordered = ordered

    @property
    def unique(self) -> bool:
        return self.__unique

    @unique.setter
    def unique(self, unique: bool):
        self.__unique = unique

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
    def classes_Operation(self):
        return self.__classes_Operation

    @classes_Operation.setter
    def classes_Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_Operation__classes_Operation", None)
        self.__classes_Operation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classes_Operation81"):
                opp_val = getattr(old_value, "classes_Operation81", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classes_Operation81"):
                opp_val = getattr(value, "classes_Operation81", None)
                if opp_val is None:
                    setattr(value, "classes_Operation81", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Operation(self):
        return self.__Operation

    @Operation.setter
    def Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_Operation__Operation", None)
        self.__Operation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "class101"):
                opp_val = getattr(old_value, "class101", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "class101"):
                opp_val = getattr(value, "class101", None)
                if opp_val is None:
                    setattr(value, "class101", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def classes_Operation81(self):
        return self.__classes_Operation81

    @classes_Operation81.setter
    def classes_Operation81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_Operation__classes_Operation81", None)
        self.__classes_Operation81 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "classes_Operation"):
                    opp_val = getattr(item, "classes_Operation", None)
                    
                    if opp_val == self:
                        setattr(item, "classes_Operation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "classes_Operation"):
                    opp_val = getattr(item, "classes_Operation", None)
                    
                    setattr(item, "classes_Operation", self)
                    

    @property
    def classes_Operation84(self):
        return self.__classes_Operation84

    @classes_Operation84.setter
    def classes_Operation84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_Operation__classes_Operation84", None)
        self.__classes_Operation84 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classes_Type85"):
                opp_val = getattr(old_value, "classes_Type85", None)
                if opp_val == self:
                    setattr(old_value, "classes_Type85", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classes_Type85"):
                opp_val = getattr(value, "classes_Type85", None)
                setattr(value, "classes_Type85", self)

    @property
    def ownedOperation(self):
        return self.__ownedOperation

    @ownedOperation.setter
    def ownedOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_Operation__ownedOperation", None)
        self.__ownedOperation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Class80"):
                opp_val = getattr(old_value, "Class80", None)
                if opp_val == self:
                    setattr(old_value, "Class80", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Class80"):
                opp_val = getattr(value, "Class80", None)
                setattr(value, "Class80", self)

    def returnResult(self) -> str:
        # TODO: Implement returnResult method
        pass

class Classifier:

    pass
class classes_Class(Classifier):

    def __init__(self, active: bool, Class: "classes_Property" = None, Class80: "classes_Operation" = None, class: set["classes_Property"] = None, class101: set["classes_Operation"] = None, classes_Class: "classes_Class" = None, classes_Class102: set["classes_Class"] = None, classes_Class105: set["classes_Classifier"] = None):
        self.active = active
        self.Class = Class
        self.Class80 = Class80
        self.class = class if class is not None else set()
        self.class101 = class101 if class101 is not None else set()
        self.classes_Class = classes_Class
        self.classes_Class102 = classes_Class102 if classes_Class102 is not None else set()
        self.classes_Class105 = classes_Class105 if classes_Class105 is not None else set()
        
    @property
    def active(self) -> bool:
        return self.__active

    @active.setter
    def active(self, active: bool):
        self.__active = active

    @property
    def Class80(self):
        return self.__Class80

    @Class80.setter
    def Class80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_Class__Class80", None)
        self.__Class80 = value
        
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
    def class(self):
        return self.__class

    @class.setter
    def class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_Class__class", None)
        self.__class = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Property99"):
                    opp_val = getattr(item, "Property99", None)
                    
                    if opp_val == self:
                        setattr(item, "Property99", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Property99"):
                    opp_val = getattr(item, "Property99", None)
                    
                    setattr(item, "Property99", self)
                    

    @property
    def classes_Class102(self):
        return self.__classes_Class102

    @classes_Class102.setter
    def classes_Class102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_Class__classes_Class102", None)
        self.__classes_Class102 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "classes_Class"):
                    opp_val = getattr(item, "classes_Class", None)
                    
                    if opp_val == self:
                        setattr(item, "classes_Class", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "classes_Class"):
                    opp_val = getattr(item, "classes_Class", None)
                    
                    setattr(item, "classes_Class", self)
                    

    @property
    def class101(self):
        return self.__class101

    @class101.setter
    def class101(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_Class__class101", None)
        self.__class101 = value if value is not None else set()
        
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
    def classes_Class105(self):
        return self.__classes_Class105

    @classes_Class105.setter
    def classes_Class105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_Class__classes_Class105", None)
        self.__classes_Class105 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "classes_Classifier106"):
                    opp_val = getattr(item, "classes_Classifier106", None)
                    
                    if opp_val == self:
                        setattr(item, "classes_Classifier106", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "classes_Classifier106"):
                    opp_val = getattr(item, "classes_Classifier106", None)
                    
                    setattr(item, "classes_Classifier106", self)
                    

    @property
    def classes_Class(self):
        return self.__classes_Class

    @classes_Class.setter
    def classes_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_Class__classes_Class", None)
        self.__classes_Class = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classes_Class102"):
                opp_val = getattr(old_value, "classes_Class102", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classes_Class102"):
                opp_val = getattr(value, "classes_Class102", None)
                if opp_val is None:
                    setattr(value, "classes_Class102", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Class(self):
        return self.__Class

    @Class.setter
    def Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_Class__Class", None)
        self.__Class = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownedAttribute60"):
                opp_val = getattr(old_value, "ownedAttribute60", None)
                if opp_val == self:
                    setattr(old_value, "ownedAttribute60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedAttribute60"):
                opp_val = getattr(value, "ownedAttribute60", None)
                setattr(value, "ownedAttribute60", self)

class classes_DataType(Classifier):

    pass
class classes_Association(Classifier):

    def __init__(self, derived: bool, Association: "classes_Property" = None, Association57: "classes_Property" = None, classes_Association: set["classes_Type"] = None, association: set["classes_Property"] = None, classes_Association68: set["classes_Property"] = None, owningAssociation: set["classes_Property"] = None):
        self.derived = derived
        self.Association = Association
        self.Association57 = Association57
        self.classes_Association = classes_Association if classes_Association is not None else set()
        self.association = association if association is not None else set()
        self.classes_Association68 = classes_Association68 if classes_Association68 is not None else set()
        self.owningAssociation = owningAssociation if owningAssociation is not None else set()
        
    @property
    def derived(self) -> bool:
        return self.__derived

    @derived.setter
    def derived(self, derived: bool):
        self.__derived = derived

    @property
    def Association57(self):
        return self.__Association57

    @Association57.setter
    def Association57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_Association__Association57", None)
        self.__Association57 = value
        
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
    def Association(self):
        return self.__Association

    @Association.setter
    def Association(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_Association__Association", None)
        self.__Association = value
        
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
    def classes_Association68(self):
        return self.__classes_Association68

    @classes_Association68.setter
    def classes_Association68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_Association__classes_Association68", None)
        self.__classes_Association68 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "classes_Property69"):
                    opp_val = getattr(item, "classes_Property69", None)
                    
                    if opp_val == self:
                        setattr(item, "classes_Property69", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "classes_Property69"):
                    opp_val = getattr(item, "classes_Property69", None)
                    
                    setattr(item, "classes_Property69", self)
                    

    @property
    def classes_Association(self):
        return self.__classes_Association

    @classes_Association.setter
    def classes_Association(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_Association__classes_Association", None)
        self.__classes_Association = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "classes_Type65"):
                    opp_val = getattr(item, "classes_Type65", None)
                    
                    if opp_val == self:
                        setattr(item, "classes_Type65", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "classes_Type65"):
                    opp_val = getattr(item, "classes_Type65", None)
                    
                    setattr(item, "classes_Type65", self)
                    

    @property
    def association(self):
        return self.__association

    @association.setter
    def association(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_Association__association", None)
        self.__association = value if value is not None else set()
        
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
    def owningAssociation(self):
        return self.__owningAssociation

    @owningAssociation.setter
    def owningAssociation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_Association__owningAssociation", None)
        self.__owningAssociation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Property71"):
                    opp_val = getattr(item, "Property71", None)
                    
                    if opp_val == self:
                        setattr(item, "Property71", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Property71"):
                    opp_val = getattr(item, "Property71", None)
                    
                    setattr(item, "Property71", self)
                    

class StructuralFeature:

    pass
class classes_Property(StructuralFeature):

    def __init__(self, derived: bool, derivedUnion: bool, aggregation: str, composite: bool, classes_Property: "classes_Classifier" = None, ownedEnd: "classes_Association" = None, memberEnd: "classes_Association" = None, classes_Property63: "classes_Property" = None, classes_Property61: "classes_Property" = None, Property: "classes_Association" = None, classes_Property69: "classes_Association" = None, ownedAttribute: "classes_DataType" = None, Property71: "classes_Association" = None, ownedAttribute60: "classes_Class" = None, Property73: "classes_DataType" = None, Property99: "classes_Class" = None):
        self.derived = derived
        self.derivedUnion = derivedUnion
        self.aggregation = aggregation
        self.composite = composite
        self.classes_Property = classes_Property
        self.ownedEnd = ownedEnd
        self.memberEnd = memberEnd
        self.classes_Property63 = classes_Property63
        self.classes_Property61 = classes_Property61
        self.Property = Property
        self.classes_Property69 = classes_Property69
        self.ownedAttribute = ownedAttribute
        self.Property71 = Property71
        self.ownedAttribute60 = ownedAttribute60
        self.Property73 = Property73
        self.Property99 = Property99
        
    @property
    def aggregation(self) -> str:
        return self.__aggregation

    @aggregation.setter
    def aggregation(self, aggregation: str):
        self.__aggregation = aggregation

    @property
    def derived(self) -> bool:
        return self.__derived

    @derived.setter
    def derived(self, derived: bool):
        self.__derived = derived

    @property
    def composite(self) -> bool:
        return self.__composite

    @composite.setter
    def composite(self, composite: bool):
        self.__composite = composite

    @property
    def derivedUnion(self) -> bool:
        return self.__derivedUnion

    @derivedUnion.setter
    def derivedUnion(self, derivedUnion: bool):
        self.__derivedUnion = derivedUnion

    @property
    def ownedEnd(self):
        return self.__ownedEnd

    @ownedEnd.setter
    def ownedEnd(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_Property__ownedEnd", None)
        self.__ownedEnd = value
        
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
    def classes_Property69(self):
        return self.__classes_Property69

    @classes_Property69.setter
    def classes_Property69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_Property__classes_Property69", None)
        self.__classes_Property69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classes_Association68"):
                opp_val = getattr(old_value, "classes_Association68", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classes_Association68"):
                opp_val = getattr(value, "classes_Association68", None)
                if opp_val is None:
                    setattr(value, "classes_Association68", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Property73(self):
        return self.__Property73

    @Property73.setter
    def Property73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_Property__Property73", None)
        self.__Property73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datatype"):
                opp_val = getattr(old_value, "datatype", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datatype"):
                opp_val = getattr(value, "datatype", None)
                if opp_val is None:
                    setattr(value, "datatype", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def classes_Property(self):
        return self.__classes_Property

    @classes_Property.setter
    def classes_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_Property__classes_Property", None)
        self.__classes_Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classes_Classifier47"):
                opp_val = getattr(old_value, "classes_Classifier47", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classes_Classifier47"):
                opp_val = getattr(value, "classes_Classifier47", None)
                if opp_val is None:
                    setattr(value, "classes_Classifier47", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def classes_Property61(self):
        return self.__classes_Property61

    @classes_Property61.setter
    def classes_Property61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_Property__classes_Property61", None)
        self.__classes_Property61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classes_Property63"):
                opp_val = getattr(old_value, "classes_Property63", None)
                if opp_val == self:
                    setattr(old_value, "classes_Property63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classes_Property63"):
                opp_val = getattr(value, "classes_Property63", None)
                setattr(value, "classes_Property63", self)

    @property
    def classes_Property63(self):
        return self.__classes_Property63

    @classes_Property63.setter
    def classes_Property63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_Property__classes_Property63", None)
        self.__classes_Property63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classes_Property61"):
                opp_val = getattr(old_value, "classes_Property61", None)
                if opp_val == self:
                    setattr(old_value, "classes_Property61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classes_Property61"):
                opp_val = getattr(value, "classes_Property61", None)
                setattr(value, "classes_Property61", self)

    @property
    def Property71(self):
        return self.__Property71

    @Property71.setter
    def Property71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_Property__Property71", None)
        self.__Property71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owningAssociation"):
                opp_val = getattr(old_value, "owningAssociation", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owningAssociation"):
                opp_val = getattr(value, "owningAssociation", None)
                if opp_val is None:
                    setattr(value, "owningAssociation", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ownedAttribute(self):
        return self.__ownedAttribute

    @ownedAttribute.setter
    def ownedAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_Property__ownedAttribute", None)
        self.__ownedAttribute = value
        
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
    def memberEnd(self):
        return self.__memberEnd

    @memberEnd.setter
    def memberEnd(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_Property__memberEnd", None)
        self.__memberEnd = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Association57"):
                opp_val = getattr(old_value, "Association57", None)
                if opp_val == self:
                    setattr(old_value, "Association57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Association57"):
                opp_val = getattr(value, "Association57", None)
                setattr(value, "Association57", self)

    @property
    def Property(self):
        return self.__Property

    @Property.setter
    def Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_Property__Property", None)
        self.__Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "association"):
                opp_val = getattr(old_value, "association", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "association"):
                opp_val = getattr(value, "association", None)
                if opp_val is None:
                    setattr(value, "association", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Property99(self):
        return self.__Property99

    @Property99.setter
    def Property99(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_Property__Property99", None)
        self.__Property99 = value
        
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
    def ownedAttribute60(self):
        return self.__ownedAttribute60

    @ownedAttribute60.setter
    def ownedAttribute60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_Property__ownedAttribute60", None)
        self.__ownedAttribute60 = value
        
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

class Type:

    pass
class RedefinableElement:

    pass
class classes_Feature(RedefinableElement):

    def __init__(self, static: bool, feature: set["classes_Classifier"] = None, Feature: "classes_Classifier" = None):
        self.static = static
        self.feature = feature if feature is not None else set()
        self.Feature = Feature
        
    @property
    def static(self) -> bool:
        return self.__static

    @static.setter
    def static(self, static: bool):
        self.__static = static

    @property
    def Feature(self):
        return self.__Feature

    @Feature.setter
    def Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_Feature__Feature", None)
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

    @property
    def feature(self):
        return self.__feature

    @feature.setter
    def feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_Feature__feature", None)
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
                    

class MultiplicityElement:

    pass
class Feature:

    pass
class classes_BehavioralFeature(Feature):

    def __init__(self, abstract: bool, classes_BehavioralFeature: set["classes_Parameter"] = None):
        self.abstract = abstract
        self.classes_BehavioralFeature = classes_BehavioralFeature if classes_BehavioralFeature is not None else set()
        
    @property
    def abstract(self) -> bool:
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: bool):
        self.__abstract = abstract

    @property
    def classes_BehavioralFeature(self):
        return self.__classes_BehavioralFeature

    @classes_BehavioralFeature.setter
    def classes_BehavioralFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_BehavioralFeature__classes_BehavioralFeature", None)
        self.__classes_BehavioralFeature = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "classes_Parameter"):
                    opp_val = getattr(item, "classes_Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "classes_Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "classes_Parameter"):
                    opp_val = getattr(item, "classes_Parameter", None)
                    
                    setattr(item, "classes_Parameter", self)
                    

class PackageableElement:

    pass
class Namespace:

    pass
class classes_Classifier(Type, Namespace):

    def __init__(self, abstract: bool, finalSpecialization: bool, Classifier: "classes_Feature" = None, classes_Classifier: "classes_RedefinableElement" = None, specific: set["classes_Generalization"] = None, featuringClassifier: set["classes_Feature"] = None, classes_Classifier44: set["classes_NamedElement"] = None, classes_Classifier47: set["classes_Property"] = None, classes_Classifier50: "classes_Classifier" = None, classes_Classifier48: set["classes_Classifier"] = None, Classifier54: "classes_Generalization" = None, classes_Classifier52: "classes_Generalization" = None, classes_Classifier87: "classes_InstanceSpecification" = None, classes_Classifier106: "classes_Class" = None):
        self.abstract = abstract
        self.finalSpecialization = finalSpecialization
        self.Classifier = Classifier
        self.classes_Classifier = classes_Classifier
        self.specific = specific if specific is not None else set()
        self.featuringClassifier = featuringClassifier if featuringClassifier is not None else set()
        self.classes_Classifier44 = classes_Classifier44 if classes_Classifier44 is not None else set()
        self.classes_Classifier47 = classes_Classifier47 if classes_Classifier47 is not None else set()
        self.classes_Classifier50 = classes_Classifier50
        self.classes_Classifier48 = classes_Classifier48 if classes_Classifier48 is not None else set()
        self.Classifier54 = Classifier54
        self.classes_Classifier52 = classes_Classifier52
        self.classes_Classifier87 = classes_Classifier87
        self.classes_Classifier106 = classes_Classifier106
        
    @property
    def abstract(self) -> bool:
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: bool):
        self.__abstract = abstract

    @property
    def finalSpecialization(self) -> bool:
        return self.__finalSpecialization

    @finalSpecialization.setter
    def finalSpecialization(self, finalSpecialization: bool):
        self.__finalSpecialization = finalSpecialization

    @property
    def specific(self):
        return self.__specific

    @specific.setter
    def specific(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_Classifier__specific", None)
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
    def classes_Classifier48(self):
        return self.__classes_Classifier48

    @classes_Classifier48.setter
    def classes_Classifier48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_Classifier__classes_Classifier48", None)
        self.__classes_Classifier48 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "classes_Classifier50"):
                    opp_val = getattr(item, "classes_Classifier50", None)
                    
                    if opp_val == self:
                        setattr(item, "classes_Classifier50", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "classes_Classifier50"):
                    opp_val = getattr(item, "classes_Classifier50", None)
                    
                    setattr(item, "classes_Classifier50", self)
                    

    @property
    def classes_Classifier44(self):
        return self.__classes_Classifier44

    @classes_Classifier44.setter
    def classes_Classifier44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_Classifier__classes_Classifier44", None)
        self.__classes_Classifier44 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "classes_NamedElement45"):
                    opp_val = getattr(item, "classes_NamedElement45", None)
                    
                    if opp_val == self:
                        setattr(item, "classes_NamedElement45", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "classes_NamedElement45"):
                    opp_val = getattr(item, "classes_NamedElement45", None)
                    
                    setattr(item, "classes_NamedElement45", self)
                    

    @property
    def classes_Classifier47(self):
        return self.__classes_Classifier47

    @classes_Classifier47.setter
    def classes_Classifier47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_Classifier__classes_Classifier47", None)
        self.__classes_Classifier47 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "classes_Property"):
                    opp_val = getattr(item, "classes_Property", None)
                    
                    if opp_val == self:
                        setattr(item, "classes_Property", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "classes_Property"):
                    opp_val = getattr(item, "classes_Property", None)
                    
                    setattr(item, "classes_Property", self)
                    

    @property
    def Classifier54(self):
        return self.__Classifier54

    @Classifier54.setter
    def Classifier54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_Classifier__Classifier54", None)
        self.__Classifier54 = value
        
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
    def classes_Classifier87(self):
        return self.__classes_Classifier87

    @classes_Classifier87.setter
    def classes_Classifier87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_Classifier__classes_Classifier87", None)
        self.__classes_Classifier87 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classes_InstanceSpecification"):
                opp_val = getattr(old_value, "classes_InstanceSpecification", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classes_InstanceSpecification"):
                opp_val = getattr(value, "classes_InstanceSpecification", None)
                if opp_val is None:
                    setattr(value, "classes_InstanceSpecification", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def classes_Classifier106(self):
        return self.__classes_Classifier106

    @classes_Classifier106.setter
    def classes_Classifier106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_Classifier__classes_Classifier106", None)
        self.__classes_Classifier106 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classes_Class105"):
                opp_val = getattr(old_value, "classes_Class105", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classes_Class105"):
                opp_val = getattr(value, "classes_Class105", None)
                if opp_val is None:
                    setattr(value, "classes_Class105", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def classes_Classifier(self):
        return self.__classes_Classifier

    @classes_Classifier.setter
    def classes_Classifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_Classifier__classes_Classifier", None)
        self.__classes_Classifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classes_RedefinableElement40"):
                opp_val = getattr(old_value, "classes_RedefinableElement40", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classes_RedefinableElement40"):
                opp_val = getattr(value, "classes_RedefinableElement40", None)
                if opp_val is None:
                    setattr(value, "classes_RedefinableElement40", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Classifier(self):
        return self.__Classifier

    @Classifier.setter
    def Classifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_Classifier__Classifier", None)
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
    def classes_Classifier50(self):
        return self.__classes_Classifier50

    @classes_Classifier50.setter
    def classes_Classifier50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_Classifier__classes_Classifier50", None)
        self.__classes_Classifier50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classes_Classifier48"):
                opp_val = getattr(old_value, "classes_Classifier48", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classes_Classifier48"):
                opp_val = getattr(value, "classes_Classifier48", None)
                if opp_val is None:
                    setattr(value, "classes_Classifier48", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def classes_Classifier52(self):
        return self.__classes_Classifier52

    @classes_Classifier52.setter
    def classes_Classifier52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_Classifier__classes_Classifier52", None)
        self.__classes_Classifier52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classes_Generalization"):
                opp_val = getattr(old_value, "classes_Generalization", None)
                if opp_val == self:
                    setattr(old_value, "classes_Generalization", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classes_Generalization"):
                opp_val = getattr(value, "classes_Generalization", None)
                setattr(value, "classes_Generalization", self)

    @property
    def featuringClassifier(self):
        return self.__featuringClassifier

    @featuringClassifier.setter
    def featuringClassifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_Classifier__featuringClassifier", None)
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
                    

    def allFeatures(self) -> Feature:
        # TODO: Implement allFeatures method
        pass

class classes_Package(Namespace, PackageableElement):

    pass
class classes_Comment:

    def __init__(self, body: str, classes_Comment: "classes_Element" = None, classes_Comment9: set["classes_Element"] = None):
        self.body = body
        self.classes_Comment = classes_Comment
        self.classes_Comment9 = classes_Comment9 if classes_Comment9 is not None else set()
        
    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

    @property
    def classes_Comment9(self):
        return self.__classes_Comment9

    @classes_Comment9.setter
    def classes_Comment9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_Comment__classes_Comment9", None)
        self.__classes_Comment9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "classes_Element10"):
                    opp_val = getattr(item, "classes_Element10", None)
                    
                    if opp_val == self:
                        setattr(item, "classes_Element10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "classes_Element10"):
                    opp_val = getattr(item, "classes_Element10", None)
                    
                    setattr(item, "classes_Element10", self)
                    

    @property
    def classes_Comment(self):
        return self.__classes_Comment

    @classes_Comment.setter
    def classes_Comment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_Comment__classes_Comment", None)
        self.__classes_Comment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classes_Element"):
                opp_val = getattr(old_value, "classes_Element", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classes_Element"):
                opp_val = getattr(value, "classes_Element", None)
                if opp_val is None:
                    setattr(value, "classes_Element", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class classes_Element(ABC):

    def __init__(self, Element: "classes_Element" = None, owner: set["classes_Element"] = None, Element6: "classes_Element" = None, ownedElement: "classes_Element" = None, classes_Element: set["classes_Comment"] = None, classes_Element10: "classes_Comment" = None):
        self.Element = Element
        self.owner = owner if owner is not None else set()
        self.Element6 = Element6
        self.ownedElement = ownedElement
        self.classes_Element = classes_Element if classes_Element is not None else set()
        self.classes_Element10 = classes_Element10
        
    @property
    def classes_Element10(self):
        return self.__classes_Element10

    @classes_Element10.setter
    def classes_Element10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_Element__classes_Element10", None)
        self.__classes_Element10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classes_Comment9"):
                opp_val = getattr(old_value, "classes_Comment9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classes_Comment9"):
                opp_val = getattr(value, "classes_Comment9", None)
                if opp_val is None:
                    setattr(value, "classes_Comment9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Element(self):
        return self.__Element

    @Element.setter
    def Element(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_Element__Element", None)
        self.__Element = value
        
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
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_Element__owner", None)
        self.__owner = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Element"):
                    opp_val = getattr(item, "Element", None)
                    
                    if opp_val == self:
                        setattr(item, "Element", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Element"):
                    opp_val = getattr(item, "Element", None)
                    
                    setattr(item, "Element", self)
                    

    @property
    def Element6(self):
        return self.__Element6

    @Element6.setter
    def Element6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_Element__Element6", None)
        self.__Element6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownedElement"):
                opp_val = getattr(old_value, "ownedElement", None)
                if opp_val == self:
                    setattr(old_value, "ownedElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedElement"):
                opp_val = getattr(value, "ownedElement", None)
                setattr(value, "ownedElement", self)

    @property
    def classes_Element(self):
        return self.__classes_Element

    @classes_Element.setter
    def classes_Element(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_Element__classes_Element", None)
        self.__classes_Element = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "classes_Comment"):
                    opp_val = getattr(item, "classes_Comment", None)
                    
                    if opp_val == self:
                        setattr(item, "classes_Comment", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "classes_Comment"):
                    opp_val = getattr(item, "classes_Comment", None)
                    
                    setattr(item, "classes_Comment", self)
                    

    @property
    def ownedElement(self):
        return self.__ownedElement

    @ownedElement.setter
    def ownedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_Element__ownedElement", None)
        self.__ownedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Element6"):
                opp_val = getattr(old_value, "Element6", None)
                if opp_val == self:
                    setattr(old_value, "Element6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Element6"):
                opp_val = getattr(value, "Element6", None)
                setattr(value, "Element6", self)

    def allOwnedElements(self) -> Element:
        # TODO: Implement allOwnedElements method
        pass

    def mustBeOwned(self) -> bool:
        # TODO: Implement mustBeOwned method
        pass

class Element:

    pass
class classes_PackageImport(Element):

    def __init__(self, visibility: str, classes_PackageImport: "classes_Package" = None, packageImport: "classes_Namespace" = None, PackageImport: "classes_Namespace" = None):
        self.visibility = visibility
        self.classes_PackageImport = classes_PackageImport
        self.packageImport = packageImport
        self.PackageImport = PackageImport
        
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
        old_value = getattr(self, f"_classes_PackageImport__PackageImport", None)
        self.__PackageImport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "importingNamespace14"):
                opp_val = getattr(old_value, "importingNamespace14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "importingNamespace14"):
                opp_val = getattr(value, "importingNamespace14", None)
                if opp_val is None:
                    setattr(value, "importingNamespace14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def packageImport(self):
        return self.__packageImport

    @packageImport.setter
    def packageImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_PackageImport__packageImport", None)
        self.__packageImport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Namespace24"):
                opp_val = getattr(old_value, "Namespace24", None)
                if opp_val == self:
                    setattr(old_value, "Namespace24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Namespace24"):
                opp_val = getattr(value, "Namespace24", None)
                setattr(value, "Namespace24", self)

    @property
    def classes_PackageImport(self):
        return self.__classes_PackageImport

    @classes_PackageImport.setter
    def classes_PackageImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_PackageImport__classes_PackageImport", None)
        self.__classes_PackageImport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classes_Package"):
                opp_val = getattr(old_value, "classes_Package", None)
                if opp_val == self:
                    setattr(old_value, "classes_Package", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classes_Package"):
                opp_val = getattr(value, "classes_Package", None)
                setattr(value, "classes_Package", self)

class classes_ElementImport(Element):

    def __init__(self, visibility: str, alias: str, classes_ElementImport: "classes_PackageableElement" = None, elementImport: "classes_Namespace" = None, ElementImport: "classes_Namespace" = None):
        self.visibility = visibility
        self.alias = alias
        self.classes_ElementImport = classes_ElementImport
        self.elementImport = elementImport
        self.ElementImport = ElementImport
        
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
    def elementImport(self):
        return self.__elementImport

    @elementImport.setter
    def elementImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_ElementImport__elementImport", None)
        self.__elementImport = value
        
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
    def classes_ElementImport(self):
        return self.__classes_ElementImport

    @classes_ElementImport.setter
    def classes_ElementImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_ElementImport__classes_ElementImport", None)
        self.__classes_ElementImport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classes_PackageableElement19"):
                opp_val = getattr(old_value, "classes_PackageableElement19", None)
                if opp_val == self:
                    setattr(old_value, "classes_PackageableElement19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classes_PackageableElement19"):
                opp_val = getattr(value, "classes_PackageableElement19", None)
                setattr(value, "classes_PackageableElement19", self)

    @property
    def ElementImport(self):
        return self.__ElementImport

    @ElementImport.setter
    def ElementImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_ElementImport__ElementImport", None)
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

class classes_Generalization(Element):

    def __init__(self, substitutable: bool, Generalization: "classes_Classifier" = None, generalization: "classes_Classifier" = None, classes_Generalization: "classes_Classifier" = None):
        self.substitutable = substitutable
        self.Generalization = Generalization
        self.generalization = generalization
        self.classes_Generalization = classes_Generalization
        
    @property
    def substitutable(self) -> bool:
        return self.__substitutable

    @substitutable.setter
    def substitutable(self, substitutable: bool):
        self.__substitutable = substitutable

    @property
    def classes_Generalization(self):
        return self.__classes_Generalization

    @classes_Generalization.setter
    def classes_Generalization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_Generalization__classes_Generalization", None)
        self.__classes_Generalization = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classes_Classifier52"):
                opp_val = getattr(old_value, "classes_Classifier52", None)
                if opp_val == self:
                    setattr(old_value, "classes_Classifier52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classes_Classifier52"):
                opp_val = getattr(value, "classes_Classifier52", None)
                setattr(value, "classes_Classifier52", self)

    @property
    def generalization(self):
        return self.__generalization

    @generalization.setter
    def generalization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_Generalization__generalization", None)
        self.__generalization = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Classifier54"):
                opp_val = getattr(old_value, "Classifier54", None)
                if opp_val == self:
                    setattr(old_value, "Classifier54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Classifier54"):
                opp_val = getattr(value, "Classifier54", None)
                setattr(value, "Classifier54", self)

    @property
    def Generalization(self):
        return self.__Generalization

    @Generalization.setter
    def Generalization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_Generalization__Generalization", None)
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

class classes_Slot(Element):

    pass
class classes_MultiplicityElement(Element):

    def __init__(self, ordered: bool, unique: bool, upper: int, lower: int, classes_MultiplicityElement: "classes_ValueSpecification" = None, classes_MultiplicityElement76: "classes_ValueSpecification" = None):
        self.ordered = ordered
        self.unique = unique
        self.upper = upper
        self.lower = lower
        self.classes_MultiplicityElement = classes_MultiplicityElement
        self.classes_MultiplicityElement76 = classes_MultiplicityElement76
        
    @property
    def unique(self) -> bool:
        return self.__unique

    @unique.setter
    def unique(self, unique: bool):
        self.__unique = unique

    @property
    def upper(self) -> int:
        return self.__upper

    @upper.setter
    def upper(self, upper: int):
        self.__upper = upper

    @property
    def ordered(self) -> bool:
        return self.__ordered

    @ordered.setter
    def ordered(self, ordered: bool):
        self.__ordered = ordered

    @property
    def lower(self) -> int:
        return self.__lower

    @lower.setter
    def lower(self, lower: int):
        self.__lower = lower

    @property
    def classes_MultiplicityElement(self):
        return self.__classes_MultiplicityElement

    @classes_MultiplicityElement.setter
    def classes_MultiplicityElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_MultiplicityElement__classes_MultiplicityElement", None)
        self.__classes_MultiplicityElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classes_ValueSpecification"):
                opp_val = getattr(old_value, "classes_ValueSpecification", None)
                if opp_val == self:
                    setattr(old_value, "classes_ValueSpecification", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classes_ValueSpecification"):
                opp_val = getattr(value, "classes_ValueSpecification", None)
                setattr(value, "classes_ValueSpecification", self)

    @property
    def classes_MultiplicityElement76(self):
        return self.__classes_MultiplicityElement76

    @classes_MultiplicityElement76.setter
    def classes_MultiplicityElement76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_MultiplicityElement__classes_MultiplicityElement76", None)
        self.__classes_MultiplicityElement76 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classes_ValueSpecification77"):
                opp_val = getattr(old_value, "classes_ValueSpecification77", None)
                if opp_val == self:
                    setattr(old_value, "classes_ValueSpecification77", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classes_ValueSpecification77"):
                opp_val = getattr(value, "classes_ValueSpecification77", None)
                setattr(value, "classes_ValueSpecification77", self)

    def upperBound(self) -> int:
        # TODO: Implement upperBound method
        pass

    def lowerBound(self) -> int:
        # TODO: Implement lowerBound method
        pass

class classes_NamedElement(Element):

    def __init__(self, name: str, visibility: str, qualifiedName: str, ownedMember: "classes_Namespace" = None, NamedElement: "classes_Namespace" = None, classes_NamedElement: "classes_Namespace" = None, classes_NamedElement45: "classes_Classifier" = None):
        self.name = name
        self.visibility = visibility
        self.qualifiedName = qualifiedName
        self.ownedMember = ownedMember
        self.NamedElement = NamedElement
        self.classes_NamedElement = classes_NamedElement
        self.classes_NamedElement45 = classes_NamedElement45
        
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
    def qualifiedName(self) -> str:
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
        old_value = getattr(self, f"_classes_NamedElement__ownedMember", None)
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
    def classes_NamedElement(self):
        return self.__classes_NamedElement

    @classes_NamedElement.setter
    def classes_NamedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_NamedElement__classes_NamedElement", None)
        self.__classes_NamedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classes_Namespace"):
                opp_val = getattr(old_value, "classes_Namespace", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classes_Namespace"):
                opp_val = getattr(value, "classes_Namespace", None)
                if opp_val is None:
                    setattr(value, "classes_Namespace", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def classes_NamedElement45(self):
        return self.__classes_NamedElement45

    @classes_NamedElement45.setter
    def classes_NamedElement45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_NamedElement__classes_NamedElement45", None)
        self.__classes_NamedElement45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classes_Classifier44"):
                opp_val = getattr(old_value, "classes_Classifier44", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classes_Classifier44"):
                opp_val = getattr(value, "classes_Classifier44", None)
                if opp_val is None:
                    setattr(value, "classes_Classifier44", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def NamedElement(self):
        return self.__NamedElement

    @NamedElement.setter
    def NamedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_NamedElement__NamedElement", None)
        self.__NamedElement = value
        
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

    def allNamespaces(self) -> str:
        # TODO: Implement allNamespaces method
        pass

    def separator(self) -> str:
        # TODO: Implement separator method
        pass

class classes_Type(PackageableElement):

    pass
class NamedElement:

    pass
class classes_RedefinableElement(NamedElement):

    def __init__(self, leaf: bool, classes_RedefinableElement40: set["classes_Classifier"] = None, classes_RedefinableElement: "classes_RedefinableElement" = None, classes_RedefinableElement37: set["classes_RedefinableElement"] = None):
        self.leaf = leaf
        self.classes_RedefinableElement40 = classes_RedefinableElement40 if classes_RedefinableElement40 is not None else set()
        self.classes_RedefinableElement = classes_RedefinableElement
        self.classes_RedefinableElement37 = classes_RedefinableElement37 if classes_RedefinableElement37 is not None else set()
        
    @property
    def leaf(self) -> bool:
        return self.__leaf

    @leaf.setter
    def leaf(self, leaf: bool):
        self.__leaf = leaf

    @property
    def classes_RedefinableElement(self):
        return self.__classes_RedefinableElement

    @classes_RedefinableElement.setter
    def classes_RedefinableElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_RedefinableElement__classes_RedefinableElement", None)
        self.__classes_RedefinableElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classes_RedefinableElement37"):
                opp_val = getattr(old_value, "classes_RedefinableElement37", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classes_RedefinableElement37"):
                opp_val = getattr(value, "classes_RedefinableElement37", None)
                if opp_val is None:
                    setattr(value, "classes_RedefinableElement37", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def classes_RedefinableElement37(self):
        return self.__classes_RedefinableElement37

    @classes_RedefinableElement37.setter
    def classes_RedefinableElement37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_RedefinableElement__classes_RedefinableElement37", None)
        self.__classes_RedefinableElement37 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "classes_RedefinableElement"):
                    opp_val = getattr(item, "classes_RedefinableElement", None)
                    
                    if opp_val == self:
                        setattr(item, "classes_RedefinableElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "classes_RedefinableElement"):
                    opp_val = getattr(item, "classes_RedefinableElement", None)
                    
                    setattr(item, "classes_RedefinableElement", self)
                    

    @property
    def classes_RedefinableElement40(self):
        return self.__classes_RedefinableElement40

    @classes_RedefinableElement40.setter
    def classes_RedefinableElement40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_RedefinableElement__classes_RedefinableElement40", None)
        self.__classes_RedefinableElement40 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "classes_Classifier"):
                    opp_val = getattr(item, "classes_Classifier", None)
                    
                    if opp_val == self:
                        setattr(item, "classes_Classifier", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "classes_Classifier"):
                    opp_val = getattr(item, "classes_Classifier", None)
                    
                    setattr(item, "classes_Classifier", self)
                    

class classes_InstanceSpecification(NamedElement):

    pass
class classes_PackageableElement(NamedElement):

    pass
class classes_Namespace(NamedElement):

    pass
class classes_TypedElement(NamedElement):

    pass
class TypedElement:

    pass
class classes_StructuralFeature(Feature, MultiplicityElement, TypedElement):

    def __init__(self, readOnly: bool, classes_StructuralFeature: "classes_Slot" = None):
        self.readOnly = readOnly
        self.classes_StructuralFeature = classes_StructuralFeature
        
    @property
    def readOnly(self) -> bool:
        return self.__readOnly

    @readOnly.setter
    def readOnly(self, readOnly: bool):
        self.__readOnly = readOnly

    @property
    def classes_StructuralFeature(self):
        return self.__classes_StructuralFeature

    @classes_StructuralFeature.setter
    def classes_StructuralFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_StructuralFeature__classes_StructuralFeature", None)
        self.__classes_StructuralFeature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classes_Slot"):
                opp_val = getattr(old_value, "classes_Slot", None)
                if opp_val == self:
                    setattr(old_value, "classes_Slot", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classes_Slot"):
                opp_val = getattr(value, "classes_Slot", None)
                setattr(value, "classes_Slot", self)

class classes_Parameter(TypedElement, MultiplicityElement):

    def __init__(self, direction: str, classes_Parameter: "classes_BehavioralFeature" = None):
        self.direction = direction
        self.classes_Parameter = classes_Parameter
        
    @property
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction

    @property
    def classes_Parameter(self):
        return self.__classes_Parameter

    @classes_Parameter.setter
    def classes_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_Parameter__classes_Parameter", None)
        self.__classes_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classes_BehavioralFeature"):
                opp_val = getattr(old_value, "classes_BehavioralFeature", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classes_BehavioralFeature"):
                opp_val = getattr(value, "classes_BehavioralFeature", None)
                if opp_val is None:
                    setattr(value, "classes_BehavioralFeature", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class classes_ValueSpecification(TypedElement):

    def __init__(self, classes_ValueSpecification: "classes_MultiplicityElement" = None, classes_ValueSpecification77: "classes_MultiplicityElement" = None, classes_ValueSpecification92: "classes_Slot" = None):
        self.classes_ValueSpecification = classes_ValueSpecification
        self.classes_ValueSpecification77 = classes_ValueSpecification77
        self.classes_ValueSpecification92 = classes_ValueSpecification92
        
    @property
    def classes_ValueSpecification77(self):
        return self.__classes_ValueSpecification77

    @classes_ValueSpecification77.setter
    def classes_ValueSpecification77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_ValueSpecification__classes_ValueSpecification77", None)
        self.__classes_ValueSpecification77 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classes_MultiplicityElement76"):
                opp_val = getattr(old_value, "classes_MultiplicityElement76", None)
                if opp_val == self:
                    setattr(old_value, "classes_MultiplicityElement76", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classes_MultiplicityElement76"):
                opp_val = getattr(value, "classes_MultiplicityElement76", None)
                setattr(value, "classes_MultiplicityElement76", self)

    @property
    def classes_ValueSpecification(self):
        return self.__classes_ValueSpecification

    @classes_ValueSpecification.setter
    def classes_ValueSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_ValueSpecification__classes_ValueSpecification", None)
        self.__classes_ValueSpecification = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classes_MultiplicityElement"):
                opp_val = getattr(old_value, "classes_MultiplicityElement", None)
                if opp_val == self:
                    setattr(old_value, "classes_MultiplicityElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classes_MultiplicityElement"):
                opp_val = getattr(value, "classes_MultiplicityElement", None)
                setattr(value, "classes_MultiplicityElement", self)

    @property
    def classes_ValueSpecification92(self):
        return self.__classes_ValueSpecification92

    @classes_ValueSpecification92.setter
    def classes_ValueSpecification92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_ValueSpecification__classes_ValueSpecification92", None)
        self.__classes_ValueSpecification92 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classes_Slot91"):
                opp_val = getattr(old_value, "classes_Slot91", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classes_Slot91"):
                opp_val = getattr(value, "classes_Slot91", None)
                if opp_val is None:
                    setattr(value, "classes_Slot91", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def booleanValue(self) -> bool:
        # TODO: Implement booleanValue method
        pass

    def isComputable(self) -> bool:
        # TODO: Implement isComputable method
        pass

    def integerValue(self) -> int:
        # TODO: Implement integerValue method
        pass

    def stringValue(self) -> str:
        # TODO: Implement stringValue method
        pass

    def isNull(self) -> bool:
        # TODO: Implement isNull method
        pass

    def unlimitedValue(self) -> int:
        # TODO: Implement unlimitedValue method
        pass
