from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class VisibilityKind(Enum):
    protected = "protected"
    private = "private"
    package = "package"
    public = "public"
class ChangeableKind(Enum):
    changeable = "changeable"
    frozen = "frozen"
    addOnly = "addOnly"
class AggregationKind(Enum):
    none = "none"
    aggregate = "aggregate"
    composite = "composite"
class ScopeKind(Enum):
    instance = "instance"
    classifier = "classifier"
class OrderingKind(Enum):
    unordered = "unordered"
    ordered = "ordered"
class ParameterDirectionKind(Enum):
    in = "in"
    out = "out"
    inout = "inout"
    return = "return"


############################################
# Definition of Classes
############################################

class UML_14_ElementOwnership:

    def __init__(self, visibility: str, isSpecification: bool):
        self.visibility = visibility
        self.isSpecification = isSpecification
        
    @property
    def isSpecification(self) -> bool:
        return self.__isSpecification

    @isSpecification.setter
    def isSpecification(self, isSpecification: bool):
        self.__isSpecification = isSpecification

    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

class Dependency:

    pass
class UML_14_Abstraction(Dependency):

    pass
class UML_14_Permission(Dependency):

    pass
class UML_14_Usage(Dependency):

    pass
class UML_14_Binding(Dependency):

    pass
class UML_14_Element(ABC):

    pass
class Association:

    pass
class Class:

    pass
class UML_14_AssociationClass(Class, Association):

    pass
class DataType:

    pass
class UML_14_Enumeration(DataType):

    pass
class UML_14_Primitive(DataType):

    pass
class Classifier:

    pass
class UML_14_Interface(Classifier):

    pass
class UML_14_DataType(Classifier):

    pass
class UML_14_Class(Classifier):

    pass
class BehavioralFeature:

    pass
class UML_14_Operation(BehavioralFeature):

    def __init__(self, isLeaf: bool, isAbstract: bool, specification: str, isRoot: bool, UML_14_Operation: "UML_14_Method" = None):
        self.isLeaf = isLeaf
        self.isAbstract = isAbstract
        self.specification = specification
        self.isRoot = isRoot
        self.UML_14_Operation = UML_14_Operation
        
    @property
    def specification(self) -> str:
        return self.__specification

    @specification.setter
    def specification(self, specification: str):
        self.__specification = specification

    @property
    def isRoot(self) -> bool:
        return self.__isRoot

    @isRoot.setter
    def isRoot(self, isRoot: bool):
        self.__isRoot = isRoot

    @property
    def isAbstract(self) -> bool:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: bool):
        self.__isAbstract = isAbstract

    @property
    def isLeaf(self) -> bool:
        return self.__isLeaf

    @isLeaf.setter
    def isLeaf(self, isLeaf: bool):
        self.__isLeaf = isLeaf

    @property
    def UML_14_Operation(self):
        return self.__UML_14_Operation

    @UML_14_Operation.setter
    def UML_14_Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_Operation__UML_14_Operation", None)
        self.__UML_14_Operation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML_14_Method"):
                opp_val = getattr(old_value, "UML_14_Method", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML_14_Method"):
                opp_val = getattr(value, "UML_14_Method", None)
                if opp_val is None:
                    setattr(value, "UML_14_Method", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Relationship:

    pass
class StructuralFeature:

    pass
class UML_14_Attribute(StructuralFeature):

    def __init__(self, initialValue: str, qualifier: "UML_14_AssociationEnd" = None, Attribute: "UML_14_AssociationEnd" = None):
        self.initialValue = initialValue
        self.qualifier = qualifier
        self.Attribute = Attribute
        
    @property
    def initialValue(self) -> str:
        return self.__initialValue

    @initialValue.setter
    def initialValue(self, initialValue: str):
        self.__initialValue = initialValue

    @property
    def qualifier(self):
        return self.__qualifier

    @qualifier.setter
    def qualifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_Attribute__qualifier", None)
        self.__qualifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AssociationEnd32"):
                opp_val = getattr(old_value, "AssociationEnd32", None)
                if opp_val == self:
                    setattr(old_value, "AssociationEnd32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AssociationEnd32"):
                opp_val = getattr(value, "AssociationEnd32", None)
                setattr(value, "AssociationEnd32", self)

    @property
    def Attribute(self):
        return self.__Attribute

    @Attribute.setter
    def Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_Attribute__Attribute", None)
        self.__Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "associationEnd"):
                opp_val = getattr(old_value, "associationEnd", None)
                if opp_val == self:
                    setattr(old_value, "associationEnd", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "associationEnd"):
                opp_val = getattr(value, "associationEnd", None)
                setattr(value, "associationEnd", self)

class UML_14_Method(BehavioralFeature):

    def __init__(self, body: str, UML_14_Method: set["UML_14_Operation"] = None):
        self.body = body
        self.UML_14_Method = UML_14_Method if UML_14_Method is not None else set()
        
    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

    @property
    def UML_14_Method(self):
        return self.__UML_14_Method

    @UML_14_Method.setter
    def UML_14_Method(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_Method__UML_14_Method", None)
        self.__UML_14_Method = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML_14_Operation"):
                    opp_val = getattr(item, "UML_14_Operation", None)
                    
                    if opp_val == self:
                        setattr(item, "UML_14_Operation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML_14_Operation"):
                    opp_val = getattr(item, "UML_14_Operation", None)
                    
                    setattr(item, "UML_14_Operation", self)
                    

class Feature:

    pass
class UML_14_MultiplicityRange:

    def __init__(self, lower: int, upper: int, MultiplicityRange: "UML_14_Multiplicity" = None, range: "UML_14_Multiplicity" = None):
        self.lower = lower
        self.upper = upper
        self.MultiplicityRange = MultiplicityRange
        self.range = range
        
    @property
    def upper(self) -> int:
        return self.__upper

    @upper.setter
    def upper(self, upper: int):
        self.__upper = upper

    @property
    def lower(self) -> int:
        return self.__lower

    @lower.setter
    def lower(self, lower: int):
        self.__lower = lower

    @property
    def MultiplicityRange(self):
        return self.__MultiplicityRange

    @MultiplicityRange.setter
    def MultiplicityRange(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_MultiplicityRange__MultiplicityRange", None)
        self.__MultiplicityRange = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "multiplicity"):
                opp_val = getattr(old_value, "multiplicity", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "multiplicity"):
                opp_val = getattr(value, "multiplicity", None)
                if opp_val is None:
                    setattr(value, "multiplicity", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def range(self):
        return self.__range

    @range.setter
    def range(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_MultiplicityRange__range", None)
        self.__range = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Multiplicity"):
                opp_val = getattr(old_value, "Multiplicity", None)
                if opp_val == self:
                    setattr(old_value, "Multiplicity", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Multiplicity"):
                opp_val = getattr(value, "Multiplicity", None)
                setattr(value, "Multiplicity", self)

class UML_14_Multiplicity:

    pass
class GeneralizableElement:

    pass
class UML_14_Association(GeneralizableElement, Relationship):

    pass
class NameSpace:

    pass
class UML_14_StructuralFeature(Feature):

    pass
class UML_14_Generalization(Relationship):

    def __init__(self, discriminator: str, Generalization: "UML_14_GeneralizableElement" = None, Generalization8: "UML_14_GeneralizableElement" = None, Generalization18: "UML_14_Classifier" = None, specialization: set["UML_14_GeneralizableElement"] = None, powertypeRange: "UML_14_Classifier" = None, generalization: set["UML_14_GeneralizableElement"] = None):
        self.discriminator = discriminator
        self.Generalization = Generalization
        self.Generalization8 = Generalization8
        self.Generalization18 = Generalization18
        self.specialization = specialization if specialization is not None else set()
        self.powertypeRange = powertypeRange
        self.generalization = generalization if generalization is not None else set()
        
    @property
    def discriminator(self) -> str:
        return self.__discriminator

    @discriminator.setter
    def discriminator(self, discriminator: str):
        self.__discriminator = discriminator

    @property
    def Generalization(self):
        return self.__Generalization

    @Generalization.setter
    def Generalization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_Generalization__Generalization", None)
        self.__Generalization = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "child"):
                opp_val = getattr(old_value, "child", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "child"):
                opp_val = getattr(value, "child", None)
                if opp_val is None:
                    setattr(value, "child", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def generalization(self):
        return self.__generalization

    @generalization.setter
    def generalization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_Generalization__generalization", None)
        self.__generalization = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GeneralizableElement"):
                    opp_val = getattr(item, "GeneralizableElement", None)
                    
                    if opp_val == self:
                        setattr(item, "GeneralizableElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GeneralizableElement"):
                    opp_val = getattr(item, "GeneralizableElement", None)
                    
                    setattr(item, "GeneralizableElement", self)
                    

    @property
    def powertypeRange(self):
        return self.__powertypeRange

    @powertypeRange.setter
    def powertypeRange(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_Generalization__powertypeRange", None)
        self.__powertypeRange = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Classifier37"):
                opp_val = getattr(old_value, "Classifier37", None)
                if opp_val == self:
                    setattr(old_value, "Classifier37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Classifier37"):
                opp_val = getattr(value, "Classifier37", None)
                setattr(value, "Classifier37", self)

    @property
    def specialization(self):
        return self.__specialization

    @specialization.setter
    def specialization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_Generalization__specialization", None)
        self.__specialization = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GeneralizableElement35"):
                    opp_val = getattr(item, "GeneralizableElement35", None)
                    
                    if opp_val == self:
                        setattr(item, "GeneralizableElement35", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GeneralizableElement35"):
                    opp_val = getattr(item, "GeneralizableElement35", None)
                    
                    setattr(item, "GeneralizableElement35", self)
                    

    @property
    def Generalization18(self):
        return self.__Generalization18

    @Generalization18.setter
    def Generalization18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_Generalization__Generalization18", None)
        self.__Generalization18 = value
        
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
    def Generalization8(self):
        return self.__Generalization8

    @Generalization8.setter
    def Generalization8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_Generalization__Generalization8", None)
        self.__Generalization8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent"):
                opp_val = getattr(old_value, "parent", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent"):
                opp_val = getattr(value, "parent", None)
                if opp_val is None:
                    setattr(value, "parent", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class UML_14_BehavioralFeature(Feature):

    def __init__(self, isQuery: bool, BehavioralFeature: "UML_14_Parameter" = None, feature26: set["UML_14_Parameter"] = None):
        self.isQuery = isQuery
        self.BehavioralFeature = BehavioralFeature
        self.feature26 = feature26 if feature26 is not None else set()
        
    @property
    def isQuery(self) -> bool:
        return self.__isQuery

    @isQuery.setter
    def isQuery(self, isQuery: bool):
        self.__isQuery = isQuery

    @property
    def feature26(self):
        return self.__feature26

    @feature26.setter
    def feature26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_BehavioralFeature__feature26", None)
        self.__feature26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Parameter27"):
                    opp_val = getattr(item, "Parameter27", None)
                    
                    if opp_val == self:
                        setattr(item, "Parameter27", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Parameter27"):
                    opp_val = getattr(item, "Parameter27", None)
                    
                    setattr(item, "Parameter27", self)
                    

    @property
    def BehavioralFeature(self):
        return self.__BehavioralFeature

    @BehavioralFeature.setter
    def BehavioralFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_BehavioralFeature__BehavioralFeature", None)
        self.__BehavioralFeature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parameter"):
                opp_val = getattr(old_value, "parameter", None)
                if opp_val == self:
                    setattr(old_value, "parameter", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parameter"):
                opp_val = getattr(value, "parameter", None)
                setattr(value, "parameter", self)

class UML_14_Classifier(NameSpace, GeneralizableElement):

    pass
class ModelElement:

    pass
class UML_14_AssociationEnd(ModelElement):

    def __init__(self, isNavigable: bool, aggregation: str, visibility: str, targetScope: str, changeability: str, AssociationEnd: "UML_14_Classifier" = None, AssociationEnd21: "UML_14_Classifier" = None, AssociationEnd32: "UML_14_Attribute" = None, UML_14_AssociationEnd: "UML_14_Multiplicity" = None, AssociationEnd39: "UML_14_Association" = None, connection: "UML_14_Association" = None, association42: "UML_14_Classifier" = None, specifiedEnd: "UML_14_Classifier" = None, associationEnd: "UML_14_Attribute" = None):
        self.isNavigable = isNavigable
        self.aggregation = aggregation
        self.visibility = visibility
        self.targetScope = targetScope
        self.changeability = changeability
        self.AssociationEnd = AssociationEnd
        self.AssociationEnd21 = AssociationEnd21
        self.AssociationEnd32 = AssociationEnd32
        self.UML_14_AssociationEnd = UML_14_AssociationEnd
        self.AssociationEnd39 = AssociationEnd39
        self.connection = connection
        self.association42 = association42
        self.specifiedEnd = specifiedEnd
        self.associationEnd = associationEnd
        
    @property
    def isNavigable(self) -> bool:
        return self.__isNavigable

    @isNavigable.setter
    def isNavigable(self, isNavigable: bool):
        self.__isNavigable = isNavigable

    @property
    def targetScope(self) -> str:
        return self.__targetScope

    @targetScope.setter
    def targetScope(self, targetScope: str):
        self.__targetScope = targetScope

    @property
    def aggregation(self) -> str:
        return self.__aggregation

    @aggregation.setter
    def aggregation(self, aggregation: str):
        self.__aggregation = aggregation

    @property
    def changeability(self) -> str:
        return self.__changeability

    @changeability.setter
    def changeability(self, changeability: str):
        self.__changeability = changeability

    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def AssociationEnd(self):
        return self.__AssociationEnd

    @AssociationEnd.setter
    def AssociationEnd(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_AssociationEnd__AssociationEnd", None)
        self.__AssociationEnd = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "participant"):
                opp_val = getattr(old_value, "participant", None)
                if opp_val == self:
                    setattr(old_value, "participant", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "participant"):
                opp_val = getattr(value, "participant", None)
                setattr(value, "participant", self)

    @property
    def connection(self):
        return self.__connection

    @connection.setter
    def connection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_AssociationEnd__connection", None)
        self.__connection = value
        
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
        old_value = getattr(self, f"_UML_14_AssociationEnd__associationEnd", None)
        self.__associationEnd = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Attribute"):
                opp_val = getattr(old_value, "Attribute", None)
                if opp_val == self:
                    setattr(old_value, "Attribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Attribute"):
                opp_val = getattr(value, "Attribute", None)
                setattr(value, "Attribute", self)

    @property
    def AssociationEnd21(self):
        return self.__AssociationEnd21

    @AssociationEnd21.setter
    def AssociationEnd21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_AssociationEnd__AssociationEnd21", None)
        self.__AssociationEnd21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "specification"):
                opp_val = getattr(old_value, "specification", None)
                if opp_val == self:
                    setattr(old_value, "specification", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "specification"):
                opp_val = getattr(value, "specification", None)
                setattr(value, "specification", self)

    @property
    def UML_14_AssociationEnd(self):
        return self.__UML_14_AssociationEnd

    @UML_14_AssociationEnd.setter
    def UML_14_AssociationEnd(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_AssociationEnd__UML_14_AssociationEnd", None)
        self.__UML_14_AssociationEnd = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML_14_Multiplicity47"):
                opp_val = getattr(old_value, "UML_14_Multiplicity47", None)
                if opp_val == self:
                    setattr(old_value, "UML_14_Multiplicity47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML_14_Multiplicity47"):
                opp_val = getattr(value, "UML_14_Multiplicity47", None)
                setattr(value, "UML_14_Multiplicity47", self)

    @property
    def specifiedEnd(self):
        return self.__specifiedEnd

    @specifiedEnd.setter
    def specifiedEnd(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_AssociationEnd__specifiedEnd", None)
        self.__specifiedEnd = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Classifier45"):
                opp_val = getattr(old_value, "Classifier45", None)
                if opp_val == self:
                    setattr(old_value, "Classifier45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Classifier45"):
                opp_val = getattr(value, "Classifier45", None)
                setattr(value, "Classifier45", self)

    @property
    def association42(self):
        return self.__association42

    @association42.setter
    def association42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_AssociationEnd__association42", None)
        self.__association42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Classifier43"):
                opp_val = getattr(old_value, "Classifier43", None)
                if opp_val == self:
                    setattr(old_value, "Classifier43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Classifier43"):
                opp_val = getattr(value, "Classifier43", None)
                setattr(value, "Classifier43", self)

    @property
    def AssociationEnd39(self):
        return self.__AssociationEnd39

    @AssociationEnd39.setter
    def AssociationEnd39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_AssociationEnd__AssociationEnd39", None)
        self.__AssociationEnd39 = value
        
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
    def AssociationEnd32(self):
        return self.__AssociationEnd32

    @AssociationEnd32.setter
    def AssociationEnd32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_AssociationEnd__AssociationEnd32", None)
        self.__AssociationEnd32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "qualifier"):
                opp_val = getattr(old_value, "qualifier", None)
                if opp_val == self:
                    setattr(old_value, "qualifier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "qualifier"):
                opp_val = getattr(value, "qualifier", None)
                setattr(value, "qualifier", self)

class UML_14_NameSpace(ModelElement):

    pass
class UML_14_GeneralizableElement(ModelElement):

    def __init__(self, isAbstract: bool, child: set["UML_14_Generalization"] = None, parent: set["UML_14_Generalization"] = None, GeneralizableElement35: "UML_14_Generalization" = None, GeneralizableElement: "UML_14_Generalization" = None):
        self.isAbstract = isAbstract
        self.child = child if child is not None else set()
        self.parent = parent if parent is not None else set()
        self.GeneralizableElement35 = GeneralizableElement35
        self.GeneralizableElement = GeneralizableElement
        
    @property
    def isAbstract(self) -> bool:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: bool):
        self.__isAbstract = isAbstract

    @property
    def child(self):
        return self.__child

    @child.setter
    def child(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_GeneralizableElement__child", None)
        self.__child = value if value is not None else set()
        
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
    def GeneralizableElement(self):
        return self.__GeneralizableElement

    @GeneralizableElement.setter
    def GeneralizableElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_GeneralizableElement__GeneralizableElement", None)
        self.__GeneralizableElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "generalization"):
                opp_val = getattr(old_value, "generalization", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "generalization"):
                opp_val = getattr(value, "generalization", None)
                if opp_val is None:
                    setattr(value, "generalization", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_GeneralizableElement__parent", None)
        self.__parent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Generalization8"):
                    opp_val = getattr(item, "Generalization8", None)
                    
                    if opp_val == self:
                        setattr(item, "Generalization8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Generalization8"):
                    opp_val = getattr(item, "Generalization8", None)
                    
                    setattr(item, "Generalization8", self)
                    

    @property
    def GeneralizableElement35(self):
        return self.__GeneralizableElement35

    @GeneralizableElement35.setter
    def GeneralizableElement35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_GeneralizableElement__GeneralizableElement35", None)
        self.__GeneralizableElement35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "specialization"):
                opp_val = getattr(old_value, "specialization", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "specialization"):
                opp_val = getattr(value, "specialization", None)
                if opp_val is None:
                    setattr(value, "specialization", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class UML_14_Relationship(ModelElement):

    pass
class UML_14_Parameter(ModelElement):

    def __init__(self, kind: str, defaultValue: str, typedParameter: "UML_14_Classifier" = None, parameter: "UML_14_BehavioralFeature" = None, Parameter: "UML_14_Classifier" = None, Parameter27: "UML_14_BehavioralFeature" = None):
        self.kind = kind
        self.defaultValue = defaultValue
        self.typedParameter = typedParameter
        self.parameter = parameter
        self.Parameter = Parameter
        self.Parameter27 = Parameter27
        
    @property
    def defaultValue(self) -> str:
        return self.__defaultValue

    @defaultValue.setter
    def defaultValue(self, defaultValue: str):
        self.__defaultValue = defaultValue

    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def typedParameter(self):
        return self.__typedParameter

    @typedParameter.setter
    def typedParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_Parameter__typedParameter", None)
        self.__typedParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Classifier10"):
                opp_val = getattr(old_value, "Classifier10", None)
                if opp_val == self:
                    setattr(old_value, "Classifier10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Classifier10"):
                opp_val = getattr(value, "Classifier10", None)
                setattr(value, "Classifier10", self)

    @property
    def parameter(self):
        return self.__parameter

    @parameter.setter
    def parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_Parameter__parameter", None)
        self.__parameter = value
        
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
    def Parameter(self):
        return self.__Parameter

    @Parameter.setter
    def Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_Parameter__Parameter", None)
        self.__Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "type"):
                opp_val = getattr(old_value, "type", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "type"):
                opp_val = getattr(value, "type", None)
                if opp_val is None:
                    setattr(value, "type", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Parameter27(self):
        return self.__Parameter27

    @Parameter27.setter
    def Parameter27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_Parameter__Parameter27", None)
        self.__Parameter27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "feature26"):
                opp_val = getattr(old_value, "feature26", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "feature26"):
                opp_val = getattr(value, "feature26", None)
                if opp_val is None:
                    setattr(value, "feature26", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class UML_14_Constraint(ModelElement):

    def __init__(self, body: str, Constraint: "UML_14_ModelElement" = None, constraint: set["UML_14_ModelElement"] = None):
        self.body = body
        self.Constraint = Constraint
        self.constraint = constraint if constraint is not None else set()
        
    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

    @property
    def constraint(self):
        return self.__constraint

    @constraint.setter
    def constraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_Constraint__constraint", None)
        self.__constraint = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ModelElement"):
                    opp_val = getattr(item, "ModelElement", None)
                    
                    if opp_val == self:
                        setattr(item, "ModelElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ModelElement"):
                    opp_val = getattr(item, "ModelElement", None)
                    
                    setattr(item, "ModelElement", self)
                    

    @property
    def Constraint(self):
        return self.__Constraint

    @Constraint.setter
    def Constraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_Constraint__Constraint", None)
        self.__Constraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "constrainedElement"):
                opp_val = getattr(old_value, "constrainedElement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "constrainedElement"):
                opp_val = getattr(value, "constrainedElement", None)
                if opp_val is None:
                    setattr(value, "constrainedElement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class UML_14_EnumerationLiteral(ModelElement):

    pass
class UML_14_Feature(ModelElement):

    pass
class UML_14_Dependency(Relationship):

    pass
class UML_14_Comment:

    def __init__(self, body: str, Comment: "UML_14_ModelElement" = None, comments: "UML_14_ModelElement" = None):
        self.body = body
        self.Comment = Comment
        self.comments = comments
        
    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

    @property
    def Comment(self):
        return self.__Comment

    @Comment.setter
    def Comment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_Comment__Comment", None)
        self.__Comment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "annotatedElement"):
                opp_val = getattr(old_value, "annotatedElement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "annotatedElement"):
                opp_val = getattr(value, "annotatedElement", None)
                if opp_val is None:
                    setattr(value, "annotatedElement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def comments(self):
        return self.__comments

    @comments.setter
    def comments(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_Comment__comments", None)
        self.__comments = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ModelElement56"):
                opp_val = getattr(old_value, "ModelElement56", None)
                if opp_val == self:
                    setattr(old_value, "ModelElement56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ModelElement56"):
                opp_val = getattr(value, "ModelElement56", None)
                setattr(value, "ModelElement56", self)

class Element:

    pass
class UML_14_ModelElement(Element):

    def __init__(self, name: str, constrainedElement: set["UML_14_Constraint"] = None, annotatedElement: set["UML_14_Comment"] = None, supplier: set["UML_14_Dependency"] = None, client: set["UML_14_Dependency"] = None, ModelElement: "UML_14_Constraint" = None, ModelElement50: "UML_14_Dependency" = None, ModelElement52: "UML_14_Dependency" = None, ModelElement56: "UML_14_Comment" = None):
        self.name = name
        self.constrainedElement = constrainedElement if constrainedElement is not None else set()
        self.annotatedElement = annotatedElement if annotatedElement is not None else set()
        self.supplier = supplier if supplier is not None else set()
        self.client = client if client is not None else set()
        self.ModelElement = ModelElement
        self.ModelElement50 = ModelElement50
        self.ModelElement52 = ModelElement52
        self.ModelElement56 = ModelElement56
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ModelElement56(self):
        return self.__ModelElement56

    @ModelElement56.setter
    def ModelElement56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_ModelElement__ModelElement56", None)
        self.__ModelElement56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "comments"):
                opp_val = getattr(old_value, "comments", None)
                if opp_val == self:
                    setattr(old_value, "comments", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "comments"):
                opp_val = getattr(value, "comments", None)
                setattr(value, "comments", self)

    @property
    def ModelElement52(self):
        return self.__ModelElement52

    @ModelElement52.setter
    def ModelElement52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_ModelElement__ModelElement52", None)
        self.__ModelElement52 = value
        
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
        old_value = getattr(self, f"_UML_14_ModelElement__supplier", None)
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
    def annotatedElement(self):
        return self.__annotatedElement

    @annotatedElement.setter
    def annotatedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_ModelElement__annotatedElement", None)
        self.__annotatedElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Comment"):
                    opp_val = getattr(item, "Comment", None)
                    
                    if opp_val == self:
                        setattr(item, "Comment", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Comment"):
                    opp_val = getattr(item, "Comment", None)
                    
                    setattr(item, "Comment", self)
                    

    @property
    def ModelElement50(self):
        return self.__ModelElement50

    @ModelElement50.setter
    def ModelElement50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_ModelElement__ModelElement50", None)
        self.__ModelElement50 = value
        
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

    @property
    def constrainedElement(self):
        return self.__constrainedElement

    @constrainedElement.setter
    def constrainedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_ModelElement__constrainedElement", None)
        self.__constrainedElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Constraint"):
                    opp_val = getattr(item, "Constraint", None)
                    
                    if opp_val == self:
                        setattr(item, "Constraint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Constraint"):
                    opp_val = getattr(item, "Constraint", None)
                    
                    setattr(item, "Constraint", self)
                    

    @property
    def client(self):
        return self.__client

    @client.setter
    def client(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_ModelElement__client", None)
        self.__client = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Dependency4"):
                    opp_val = getattr(item, "Dependency4", None)
                    
                    if opp_val == self:
                        setattr(item, "Dependency4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Dependency4"):
                    opp_val = getattr(item, "Dependency4", None)
                    
                    setattr(item, "Dependency4", self)
                    

    @property
    def ModelElement(self):
        return self.__ModelElement

    @ModelElement.setter
    def ModelElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_ModelElement__ModelElement", None)
        self.__ModelElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "constraint"):
                opp_val = getattr(old_value, "constraint", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "constraint"):
                opp_val = getattr(value, "constraint", None)
                if opp_val is None:
                    setattr(value, "constraint", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
