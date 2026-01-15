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
class AggregationKind(Enum):
    none = "none"
    shared = "shared"
    composite = "composite"


############################################
# Definition of Classes
############################################

class LiteralSpecification:

    pass
class RefUML_LiteralString(LiteralSpecification):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class RefUML_LiteralUnlimitedNatural(LiteralSpecification):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class RefUML_LiteralNull(LiteralSpecification):

    pass
class RefUML_LiteralBoolean(LiteralSpecification):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class RefUML_LiteralInteger(LiteralSpecification):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class InstanceSpecification:

    pass
class RefUML_EnumerationLiteral(InstanceSpecification):

    pass
class DataType:

    pass
class RefUML_PrimitiveType(DataType):

    pass
class RefUML_Enumeration(DataType):

    pass
class MultiplicityElement:

    pass
class Feature:

    pass
class Expression:

    pass
class Package:

    pass
class RefUML_Model(Package):

    def __init__(self, viewpoint: str):
        self.viewpoint = viewpoint
        
    @property
    def viewpoint(self) -> str:
        return self.__viewpoint

    @viewpoint.setter
    def viewpoint(self, viewpoint: str):
        self.__viewpoint = viewpoint

    def isMetamodel(self) -> str:
        # TODO: Implement isMetamodel method
        pass

class StructuralFeature:

    pass
class ValueSpecification:

    pass
class RefUML_LiteralSpecification(ValueSpecification):

    pass
class RefUML_InstanceValue(ValueSpecification):

    pass
class RefUML_Expression(ValueSpecification):

    def __init__(self, symbol: str, RefUML_Expression: set["RefUML_ValueSpecification"] = None):
        self.symbol = symbol
        self.RefUML_Expression = RefUML_Expression if RefUML_Expression is not None else set()
        
    @property
    def symbol(self) -> str:
        return self.__symbol

    @symbol.setter
    def symbol(self, symbol: str):
        self.__symbol = symbol

    @property
    def RefUML_Expression(self):
        return self.__RefUML_Expression

    @RefUML_Expression.setter
    def RefUML_Expression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_Expression__RefUML_Expression", None)
        self.__RefUML_Expression = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RefUML_ValueSpecification134"):
                    opp_val = getattr(item, "RefUML_ValueSpecification134", None)
                    
                    if opp_val == self:
                        setattr(item, "RefUML_ValueSpecification134", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RefUML_ValueSpecification134"):
                    opp_val = getattr(item, "RefUML_ValueSpecification134", None)
                    
                    setattr(item, "RefUML_ValueSpecification134", self)
                    

class RefUML_OpaqueExpression(ValueSpecification):

    def __init__(self, body: str, language: str):
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

    def getResult(self):
        # TODO: Implement getResult method
        pass

    def isIntegral(self) -> str:
        # TODO: Implement isIntegral method
        pass

    def isNonNegative(self) -> str:
        # TODO: Implement isNonNegative method
        pass

    def value(self) -> str:
        # TODO: Implement value method
        pass

    def isPositive(self) -> str:
        # TODO: Implement isPositive method
        pass

class Type:

    pass
class RedefinableElement:

    pass
class RefUML_Feature(RedefinableElement):

    def __init__(self, isStatic: str, Feature: "RefUML_Classifier" = None, feature: set["RefUML_Classifier"] = None):
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
        old_value = getattr(self, f"_RefUML_Feature__feature", None)
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
                    

    @property
    def Feature(self):
        return self.__Feature

    @Feature.setter
    def Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_Feature__Feature", None)
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

class Classifier:

    pass
class RefUML_DataType(Classifier):

    def __init__(self, DataType: "RefUML_Property" = None, datatype: set["RefUML_Property"] = None):
        self.DataType = DataType
        self.datatype = datatype if datatype is not None else set()
        
    @property
    def DataType(self):
        return self.__DataType

    @DataType.setter
    def DataType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_DataType__DataType", None)
        self.__DataType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownedAttribute103"):
                opp_val = getattr(old_value, "ownedAttribute103", None)
                if opp_val == self:
                    setattr(old_value, "ownedAttribute103", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedAttribute103"):
                opp_val = getattr(value, "ownedAttribute103", None)
                setattr(value, "ownedAttribute103", self)

    @property
    def datatype(self):
        return self.__datatype

    @datatype.setter
    def datatype(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_DataType__datatype", None)
        self.__datatype = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Property127"):
                    opp_val = getattr(item, "Property127", None)
                    
                    if opp_val == self:
                        setattr(item, "Property127", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Property127"):
                    opp_val = getattr(item, "Property127", None)
                    
                    setattr(item, "Property127", self)
                    

    def createOwnedOperation(self, returnType: Type, parameterNames: str, parameterTypes: Type, name: str):
        # TODO: Implement createOwnedOperation method
        pass

    def createOwnedAttribute(self, upper: str, lower: str, name: str, type: Type) -> str:
        # TODO: Implement createOwnedAttribute method
        pass

class RefUML_Class(Classifier):

    def __init__(self, isActive: str, Class: "RefUML_Property" = None, class: set["RefUML_Property"] = None, RefUML_Class: set["RefUML_Classifier"] = None, RefUML_Class123: "RefUML_Class" = None, RefUML_Class121: set["RefUML_Class"] = None):
        self.isActive = isActive
        self.Class = Class
        self.class = class if class is not None else set()
        self.RefUML_Class = RefUML_Class if RefUML_Class is not None else set()
        self.RefUML_Class123 = RefUML_Class123
        self.RefUML_Class121 = RefUML_Class121 if RefUML_Class121 is not None else set()
        
    @property
    def isActive(self) -> str:
        return self.__isActive

    @isActive.setter
    def isActive(self, isActive: str):
        self.__isActive = isActive

    @property
    def RefUML_Class(self):
        return self.__RefUML_Class

    @RefUML_Class.setter
    def RefUML_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_Class__RefUML_Class", None)
        self.__RefUML_Class = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RefUML_Classifier120"):
                    opp_val = getattr(item, "RefUML_Classifier120", None)
                    
                    if opp_val == self:
                        setattr(item, "RefUML_Classifier120", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RefUML_Classifier120"):
                    opp_val = getattr(item, "RefUML_Classifier120", None)
                    
                    setattr(item, "RefUML_Classifier120", self)
                    

    @property
    def class(self):
        return self.__class

    @class.setter
    def class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_Class__class", None)
        self.__class = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Property125"):
                    opp_val = getattr(item, "Property125", None)
                    
                    if opp_val == self:
                        setattr(item, "Property125", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Property125"):
                    opp_val = getattr(item, "Property125", None)
                    
                    setattr(item, "Property125", self)
                    

    @property
    def RefUML_Class123(self):
        return self.__RefUML_Class123

    @RefUML_Class123.setter
    def RefUML_Class123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_Class__RefUML_Class123", None)
        self.__RefUML_Class123 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefUML_Class121"):
                opp_val = getattr(old_value, "RefUML_Class121", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefUML_Class121"):
                opp_val = getattr(value, "RefUML_Class121", None)
                if opp_val is None:
                    setattr(value, "RefUML_Class121", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def RefUML_Class121(self):
        return self.__RefUML_Class121

    @RefUML_Class121.setter
    def RefUML_Class121(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_Class__RefUML_Class121", None)
        self.__RefUML_Class121 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RefUML_Class123"):
                    opp_val = getattr(item, "RefUML_Class123", None)
                    
                    if opp_val == self:
                        setattr(item, "RefUML_Class123", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RefUML_Class123"):
                    opp_val = getattr(item, "RefUML_Class123", None)
                    
                    setattr(item, "RefUML_Class123", self)
                    

    @property
    def Class(self):
        return self.__Class

    @Class.setter
    def Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_Class__Class", None)
        self.__Class = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownedAttribute"):
                opp_val = getattr(old_value, "ownedAttribute", None)
                if opp_val == self:
                    setattr(old_value, "ownedAttribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedAttribute"):
                opp_val = getattr(value, "ownedAttribute", None)
                setattr(value, "ownedAttribute", self)

    def isMetaclass(self) -> str:
        # TODO: Implement isMetaclass method
        pass

    def createOwnedOperation(self, parameterTypes: Type, parameterNames: str, returnType: Type, name: str):
        # TODO: Implement createOwnedOperation method
        pass

class RefUML_Property(StructuralFeature):

    def __init__(self, isDerived: str, isDerivedUnion: str, default: str, aggregation: str, isComposite: str, Property: "RefUML_Association" = None, Property60: "RefUML_Association" = None, RefUML_Property: "RefUML_Association" = None, RefUML_Property78: "RefUML_Classifier" = None, ownedAttribute: "RefUML_Class" = None, ownedAttribute103: "RefUML_DataType" = None, ownedEnd: "RefUML_Association" = None, RefUML_Property109: "RefUML_ValueSpecification" = None, RefUML_Property113: "RefUML_Property" = None, RefUML_Property111: "RefUML_Property" = None, RefUML_Property106: "RefUML_Property" = None, RefUML_Property104: set["RefUML_Property"] = None, RefUML_Property116: "RefUML_Property" = None, RefUML_Property114: set["RefUML_Property"] = None, memberEnd: "RefUML_Association" = None, Property125: "RefUML_Class" = None, Property127: "RefUML_DataType" = None):
        self.isDerived = isDerived
        self.isDerivedUnion = isDerivedUnion
        self.default = default
        self.aggregation = aggregation
        self.isComposite = isComposite
        self.Property = Property
        self.Property60 = Property60
        self.RefUML_Property = RefUML_Property
        self.RefUML_Property78 = RefUML_Property78
        self.ownedAttribute = ownedAttribute
        self.ownedAttribute103 = ownedAttribute103
        self.ownedEnd = ownedEnd
        self.RefUML_Property109 = RefUML_Property109
        self.RefUML_Property113 = RefUML_Property113
        self.RefUML_Property111 = RefUML_Property111
        self.RefUML_Property106 = RefUML_Property106
        self.RefUML_Property104 = RefUML_Property104 if RefUML_Property104 is not None else set()
        self.RefUML_Property116 = RefUML_Property116
        self.RefUML_Property114 = RefUML_Property114 if RefUML_Property114 is not None else set()
        self.memberEnd = memberEnd
        self.Property125 = Property125
        self.Property127 = Property127
        
    @property
    def aggregation(self) -> str:
        return self.__aggregation

    @aggregation.setter
    def aggregation(self, aggregation: str):
        self.__aggregation = aggregation

    @property
    def isComposite(self) -> str:
        return self.__isComposite

    @isComposite.setter
    def isComposite(self, isComposite: str):
        self.__isComposite = isComposite

    @property
    def default(self) -> str:
        return self.__default

    @default.setter
    def default(self, default: str):
        self.__default = default

    @property
    def isDerivedUnion(self) -> str:
        return self.__isDerivedUnion

    @isDerivedUnion.setter
    def isDerivedUnion(self, isDerivedUnion: str):
        self.__isDerivedUnion = isDerivedUnion

    @property
    def isDerived(self) -> str:
        return self.__isDerived

    @isDerived.setter
    def isDerived(self, isDerived: str):
        self.__isDerived = isDerived

    @property
    def RefUML_Property(self):
        return self.__RefUML_Property

    @RefUML_Property.setter
    def RefUML_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_Property__RefUML_Property", None)
        self.__RefUML_Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefUML_Association64"):
                opp_val = getattr(old_value, "RefUML_Association64", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefUML_Association64"):
                opp_val = getattr(value, "RefUML_Association64", None)
                if opp_val is None:
                    setattr(value, "RefUML_Association64", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Property127(self):
        return self.__Property127

    @Property127.setter
    def Property127(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_Property__Property127", None)
        self.__Property127 = value
        
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
    def RefUML_Property113(self):
        return self.__RefUML_Property113

    @RefUML_Property113.setter
    def RefUML_Property113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_Property__RefUML_Property113", None)
        self.__RefUML_Property113 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefUML_Property111"):
                opp_val = getattr(old_value, "RefUML_Property111", None)
                if opp_val == self:
                    setattr(old_value, "RefUML_Property111", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefUML_Property111"):
                opp_val = getattr(value, "RefUML_Property111", None)
                setattr(value, "RefUML_Property111", self)

    @property
    def RefUML_Property109(self):
        return self.__RefUML_Property109

    @RefUML_Property109.setter
    def RefUML_Property109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_Property__RefUML_Property109", None)
        self.__RefUML_Property109 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefUML_ValueSpecification110"):
                opp_val = getattr(old_value, "RefUML_ValueSpecification110", None)
                if opp_val == self:
                    setattr(old_value, "RefUML_ValueSpecification110", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefUML_ValueSpecification110"):
                opp_val = getattr(value, "RefUML_ValueSpecification110", None)
                setattr(value, "RefUML_ValueSpecification110", self)

    @property
    def Property(self):
        return self.__Property

    @Property.setter
    def Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_Property__Property", None)
        self.__Property = value
        
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
    def RefUML_Property111(self):
        return self.__RefUML_Property111

    @RefUML_Property111.setter
    def RefUML_Property111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_Property__RefUML_Property111", None)
        self.__RefUML_Property111 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefUML_Property113"):
                opp_val = getattr(old_value, "RefUML_Property113", None)
                if opp_val == self:
                    setattr(old_value, "RefUML_Property113", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefUML_Property113"):
                opp_val = getattr(value, "RefUML_Property113", None)
                setattr(value, "RefUML_Property113", self)

    @property
    def ownedEnd(self):
        return self.__ownedEnd

    @ownedEnd.setter
    def ownedEnd(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_Property__ownedEnd", None)
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
    def RefUML_Property78(self):
        return self.__RefUML_Property78

    @RefUML_Property78.setter
    def RefUML_Property78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_Property__RefUML_Property78", None)
        self.__RefUML_Property78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefUML_Classifier77"):
                opp_val = getattr(old_value, "RefUML_Classifier77", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefUML_Classifier77"):
                opp_val = getattr(value, "RefUML_Classifier77", None)
                if opp_val is None:
                    setattr(value, "RefUML_Classifier77", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def memberEnd(self):
        return self.__memberEnd

    @memberEnd.setter
    def memberEnd(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_Property__memberEnd", None)
        self.__memberEnd = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Association118"):
                opp_val = getattr(old_value, "Association118", None)
                if opp_val == self:
                    setattr(old_value, "Association118", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Association118"):
                opp_val = getattr(value, "Association118", None)
                setattr(value, "Association118", self)

    @property
    def RefUML_Property104(self):
        return self.__RefUML_Property104

    @RefUML_Property104.setter
    def RefUML_Property104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_Property__RefUML_Property104", None)
        self.__RefUML_Property104 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RefUML_Property106"):
                    opp_val = getattr(item, "RefUML_Property106", None)
                    
                    if opp_val == self:
                        setattr(item, "RefUML_Property106", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RefUML_Property106"):
                    opp_val = getattr(item, "RefUML_Property106", None)
                    
                    setattr(item, "RefUML_Property106", self)
                    

    @property
    def ownedAttribute103(self):
        return self.__ownedAttribute103

    @ownedAttribute103.setter
    def ownedAttribute103(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_Property__ownedAttribute103", None)
        self.__ownedAttribute103 = value
        
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
    def RefUML_Property116(self):
        return self.__RefUML_Property116

    @RefUML_Property116.setter
    def RefUML_Property116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_Property__RefUML_Property116", None)
        self.__RefUML_Property116 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefUML_Property114"):
                opp_val = getattr(old_value, "RefUML_Property114", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefUML_Property114"):
                opp_val = getattr(value, "RefUML_Property114", None)
                if opp_val is None:
                    setattr(value, "RefUML_Property114", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def RefUML_Property114(self):
        return self.__RefUML_Property114

    @RefUML_Property114.setter
    def RefUML_Property114(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_Property__RefUML_Property114", None)
        self.__RefUML_Property114 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RefUML_Property116"):
                    opp_val = getattr(item, "RefUML_Property116", None)
                    
                    if opp_val == self:
                        setattr(item, "RefUML_Property116", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RefUML_Property116"):
                    opp_val = getattr(item, "RefUML_Property116", None)
                    
                    setattr(item, "RefUML_Property116", self)
                    

    @property
    def Property60(self):
        return self.__Property60

    @Property60.setter
    def Property60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_Property__Property60", None)
        self.__Property60 = value
        
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
    def RefUML_Property106(self):
        return self.__RefUML_Property106

    @RefUML_Property106.setter
    def RefUML_Property106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_Property__RefUML_Property106", None)
        self.__RefUML_Property106 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefUML_Property104"):
                opp_val = getattr(old_value, "RefUML_Property104", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefUML_Property104"):
                opp_val = getattr(value, "RefUML_Property104", None)
                if opp_val is None:
                    setattr(value, "RefUML_Property104", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ownedAttribute(self):
        return self.__ownedAttribute

    @ownedAttribute.setter
    def ownedAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_Property__ownedAttribute", None)
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
    def Property125(self):
        return self.__Property125

    @Property125.setter
    def Property125(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_Property__Property125", None)
        self.__Property125 = value
        
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

    def setDefault(self, newDefault: str):
        # TODO: Implement setDefault method
        pass

    def subsettingContext(self) -> Type:
        # TODO: Implement subsettingContext method
        pass

    def setOpposite(self, newOpposite: str):
        # TODO: Implement setOpposite method
        pass

    def isComposite(self) -> str:
        # TODO: Implement isComposite method
        pass

    def setIsNavigable(self, isNavigable: str):
        # TODO: Implement setIsNavigable method
        pass

    def setIsComposite(self, newIsComposite: str):
        # TODO: Implement setIsComposite method
        pass

    def unsetDefault(self):
        # TODO: Implement unsetDefault method
        pass

    def getDefault(self) -> str:
        # TODO: Implement getDefault method
        pass

    def setStringDefaultValue(self, value: str):
        # TODO: Implement setStringDefaultValue method
        pass

    def setNullDefaultValue(self):
        # TODO: Implement setNullDefaultValue method
        pass

    def getOpposite(self) -> str:
        # TODO: Implement getOpposite method
        pass

    def isSetDefault(self) -> str:
        # TODO: Implement isSetDefault method
        pass

    def setIntegerDefaultValue(self, value: str):
        # TODO: Implement setIntegerDefaultValue method
        pass

    def isAttribute(self, p: str) -> str:
        # TODO: Implement isAttribute method
        pass

    def isNavigable(self) -> str:
        # TODO: Implement isNavigable method
        pass

    def setUnlimitedNaturalDefaultValue(self, value: str):
        # TODO: Implement setUnlimitedNaturalDefaultValue method
        pass

    def setBooleanDefaultValue(self, value: str):
        # TODO: Implement setBooleanDefaultValue method
        pass

    def getOtherEnd(self) -> str:
        # TODO: Implement getOtherEnd method
        pass

class TypedElement:

    pass
class RefUML_StructuralFeature(Feature, MultiplicityElement, TypedElement):

    def __init__(self, isReadOnly: str, RefUML_StructuralFeature: "RefUML_Slot" = None):
        self.isReadOnly = isReadOnly
        self.RefUML_StructuralFeature = RefUML_StructuralFeature
        
    @property
    def isReadOnly(self) -> str:
        return self.__isReadOnly

    @isReadOnly.setter
    def isReadOnly(self, isReadOnly: str):
        self.__isReadOnly = isReadOnly

    @property
    def RefUML_StructuralFeature(self):
        return self.__RefUML_StructuralFeature

    @RefUML_StructuralFeature.setter
    def RefUML_StructuralFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_StructuralFeature__RefUML_StructuralFeature", None)
        self.__RefUML_StructuralFeature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefUML_Slot"):
                opp_val = getattr(old_value, "RefUML_Slot", None)
                if opp_val == self:
                    setattr(old_value, "RefUML_Slot", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefUML_Slot"):
                opp_val = getattr(value, "RefUML_Slot", None)
                setattr(value, "RefUML_Slot", self)

class Relationship:

    pass
class RefUML_Association(Relationship, Classifier):

    def __init__(self, isDerived: str, owningAssociation: set["RefUML_Property"] = None, association: set["RefUML_Property"] = None, RefUML_Association: set["RefUML_Type"] = None, RefUML_Association64: set["RefUML_Property"] = None, Association: "RefUML_Property" = None, Association118: "RefUML_Property" = None):
        self.isDerived = isDerived
        self.owningAssociation = owningAssociation if owningAssociation is not None else set()
        self.association = association if association is not None else set()
        self.RefUML_Association = RefUML_Association if RefUML_Association is not None else set()
        self.RefUML_Association64 = RefUML_Association64 if RefUML_Association64 is not None else set()
        self.Association = Association
        self.Association118 = Association118
        
    @property
    def isDerived(self) -> str:
        return self.__isDerived

    @isDerived.setter
    def isDerived(self, isDerived: str):
        self.__isDerived = isDerived

    @property
    def Association(self):
        return self.__Association

    @Association.setter
    def Association(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_Association__Association", None)
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
    def owningAssociation(self):
        return self.__owningAssociation

    @owningAssociation.setter
    def owningAssociation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_Association__owningAssociation", None)
        self.__owningAssociation = value if value is not None else set()
        
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
    def Association118(self):
        return self.__Association118

    @Association118.setter
    def Association118(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_Association__Association118", None)
        self.__Association118 = value
        
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
    def association(self):
        return self.__association

    @association.setter
    def association(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_Association__association", None)
        self.__association = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Property60"):
                    opp_val = getattr(item, "Property60", None)
                    
                    if opp_val == self:
                        setattr(item, "Property60", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Property60"):
                    opp_val = getattr(item, "Property60", None)
                    
                    setattr(item, "Property60", self)
                    

    @property
    def RefUML_Association(self):
        return self.__RefUML_Association

    @RefUML_Association.setter
    def RefUML_Association(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_Association__RefUML_Association", None)
        self.__RefUML_Association = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RefUML_Type62"):
                    opp_val = getattr(item, "RefUML_Type62", None)
                    
                    if opp_val == self:
                        setattr(item, "RefUML_Type62", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RefUML_Type62"):
                    opp_val = getattr(item, "RefUML_Type62", None)
                    
                    setattr(item, "RefUML_Type62", self)
                    

    @property
    def RefUML_Association64(self):
        return self.__RefUML_Association64

    @RefUML_Association64.setter
    def RefUML_Association64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_Association__RefUML_Association64", None)
        self.__RefUML_Association64 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RefUML_Property"):
                    opp_val = getattr(item, "RefUML_Property", None)
                    
                    if opp_val == self:
                        setattr(item, "RefUML_Property", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RefUML_Property"):
                    opp_val = getattr(item, "RefUML_Property", None)
                    
                    setattr(item, "RefUML_Property", self)
                    

    def isBinary(self) -> str:
        # TODO: Implement isBinary method
        pass

    def getEndTypes(self) -> str:
        # TODO: Implement getEndTypes method
        pass

class RefUML_DirectedRelationship(Relationship):

    pass
class DirectedRelationship:

    pass
class RefUML_ElementImport(DirectedRelationship):

    def __init__(self, visibility: str, alias: str, ElementImport: "RefUML_Namespace" = None, RefUML_ElementImport: "RefUML_PackageableElement" = None, elementImport: "RefUML_Namespace" = None):
        self.visibility = visibility
        self.alias = alias
        self.ElementImport = ElementImport
        self.RefUML_ElementImport = RefUML_ElementImport
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
    def RefUML_ElementImport(self):
        return self.__RefUML_ElementImport

    @RefUML_ElementImport.setter
    def RefUML_ElementImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_ElementImport__RefUML_ElementImport", None)
        self.__RefUML_ElementImport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefUML_PackageableElement42"):
                opp_val = getattr(old_value, "RefUML_PackageableElement42", None)
                if opp_val == self:
                    setattr(old_value, "RefUML_PackageableElement42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefUML_PackageableElement42"):
                opp_val = getattr(value, "RefUML_PackageableElement42", None)
                setattr(value, "RefUML_PackageableElement42", self)

    @property
    def ElementImport(self):
        return self.__ElementImport

    @ElementImport.setter
    def ElementImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_ElementImport__ElementImport", None)
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
    def elementImport(self):
        return self.__elementImport

    @elementImport.setter
    def elementImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_ElementImport__elementImport", None)
        self.__elementImport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Namespace44"):
                opp_val = getattr(old_value, "Namespace44", None)
                if opp_val == self:
                    setattr(old_value, "Namespace44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Namespace44"):
                opp_val = getattr(value, "Namespace44", None)
                setattr(value, "Namespace44", self)

    def getName(self) -> str:
        # TODO: Implement getName method
        pass

class RefUML_Generalization(DirectedRelationship):

    def __init__(self, isSubstitutable: str, Generalization: "RefUML_Classifier" = None, generalization89: "RefUML_Classifier" = None, Generalization93: "RefUML_GeneralizationSet" = None, RefUML_Generalization: "RefUML_Classifier" = None, generalization: set["RefUML_GeneralizationSet"] = None):
        self.isSubstitutable = isSubstitutable
        self.Generalization = Generalization
        self.generalization89 = generalization89
        self.Generalization93 = Generalization93
        self.RefUML_Generalization = RefUML_Generalization
        self.generalization = generalization if generalization is not None else set()
        
    @property
    def isSubstitutable(self) -> str:
        return self.__isSubstitutable

    @isSubstitutable.setter
    def isSubstitutable(self, isSubstitutable: str):
        self.__isSubstitutable = isSubstitutable

    @property
    def Generalization(self):
        return self.__Generalization

    @Generalization.setter
    def Generalization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_Generalization__Generalization", None)
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
    def Generalization93(self):
        return self.__Generalization93

    @Generalization93.setter
    def Generalization93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_Generalization__Generalization93", None)
        self.__Generalization93 = value
        
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
    def RefUML_Generalization(self):
        return self.__RefUML_Generalization

    @RefUML_Generalization.setter
    def RefUML_Generalization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_Generalization__RefUML_Generalization", None)
        self.__RefUML_Generalization = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefUML_Classifier85"):
                opp_val = getattr(old_value, "RefUML_Classifier85", None)
                if opp_val == self:
                    setattr(old_value, "RefUML_Classifier85", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefUML_Classifier85"):
                opp_val = getattr(value, "RefUML_Classifier85", None)
                setattr(value, "RefUML_Classifier85", self)

    @property
    def generalization89(self):
        return self.__generalization89

    @generalization89.setter
    def generalization89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_Generalization__generalization89", None)
        self.__generalization89 = value
        
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

    @property
    def generalization(self):
        return self.__generalization

    @generalization.setter
    def generalization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_Generalization__generalization", None)
        self.__generalization = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GeneralizationSet87"):
                    opp_val = getattr(item, "GeneralizationSet87", None)
                    
                    if opp_val == self:
                        setattr(item, "GeneralizationSet87", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GeneralizationSet87"):
                    opp_val = getattr(item, "GeneralizationSet87", None)
                    
                    setattr(item, "GeneralizationSet87", self)
                    

class RefUML_PackageImport(DirectedRelationship):

    def __init__(self, visibility: str, PackageImport: "RefUML_Namespace" = None, RefUML_PackageImport: "RefUML_Package" = None, packageImport: "RefUML_Namespace" = None):
        self.visibility = visibility
        self.PackageImport = PackageImport
        self.RefUML_PackageImport = RefUML_PackageImport
        self.packageImport = packageImport
        
    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def RefUML_PackageImport(self):
        return self.__RefUML_PackageImport

    @RefUML_PackageImport.setter
    def RefUML_PackageImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_PackageImport__RefUML_PackageImport", None)
        self.__RefUML_PackageImport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefUML_Package46"):
                opp_val = getattr(old_value, "RefUML_Package46", None)
                if opp_val == self:
                    setattr(old_value, "RefUML_Package46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefUML_Package46"):
                opp_val = getattr(value, "RefUML_Package46", None)
                setattr(value, "RefUML_Package46", self)

    @property
    def packageImport(self):
        return self.__packageImport

    @packageImport.setter
    def packageImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_PackageImport__packageImport", None)
        self.__packageImport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Namespace48"):
                opp_val = getattr(old_value, "Namespace48", None)
                if opp_val == self:
                    setattr(old_value, "Namespace48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Namespace48"):
                opp_val = getattr(value, "Namespace48", None)
                setattr(value, "Namespace48", self)

    @property
    def PackageImport(self):
        return self.__PackageImport

    @PackageImport.setter
    def PackageImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_PackageImport__PackageImport", None)
        self.__PackageImport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "importingNamespace32"):
                opp_val = getattr(old_value, "importingNamespace32", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "importingNamespace32"):
                opp_val = getattr(value, "importingNamespace32", None)
                if opp_val is None:
                    setattr(value, "importingNamespace32", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class RefUML_StringExpression(Expression):

    pass
class RefUML_PackageMerge(DirectedRelationship):

    pass
class NamedElement:

    pass
class RefUML_RedefinableElement(NamedElement):

    def __init__(self, isLeaf: str, RefUML_RedefinableElement: "RefUML_RedefinableElement" = None, RefUML_RedefinableElement79: set["RefUML_RedefinableElement"] = None, RefUML_RedefinableElement82: set["RefUML_Classifier"] = None):
        self.isLeaf = isLeaf
        self.RefUML_RedefinableElement = RefUML_RedefinableElement
        self.RefUML_RedefinableElement79 = RefUML_RedefinableElement79 if RefUML_RedefinableElement79 is not None else set()
        self.RefUML_RedefinableElement82 = RefUML_RedefinableElement82 if RefUML_RedefinableElement82 is not None else set()
        
    @property
    def isLeaf(self) -> str:
        return self.__isLeaf

    @isLeaf.setter
    def isLeaf(self, isLeaf: str):
        self.__isLeaf = isLeaf

    @property
    def RefUML_RedefinableElement(self):
        return self.__RefUML_RedefinableElement

    @RefUML_RedefinableElement.setter
    def RefUML_RedefinableElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_RedefinableElement__RefUML_RedefinableElement", None)
        self.__RefUML_RedefinableElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefUML_RedefinableElement79"):
                opp_val = getattr(old_value, "RefUML_RedefinableElement79", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefUML_RedefinableElement79"):
                opp_val = getattr(value, "RefUML_RedefinableElement79", None)
                if opp_val is None:
                    setattr(value, "RefUML_RedefinableElement79", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def RefUML_RedefinableElement79(self):
        return self.__RefUML_RedefinableElement79

    @RefUML_RedefinableElement79.setter
    def RefUML_RedefinableElement79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_RedefinableElement__RefUML_RedefinableElement79", None)
        self.__RefUML_RedefinableElement79 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RefUML_RedefinableElement"):
                    opp_val = getattr(item, "RefUML_RedefinableElement", None)
                    
                    if opp_val == self:
                        setattr(item, "RefUML_RedefinableElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RefUML_RedefinableElement"):
                    opp_val = getattr(item, "RefUML_RedefinableElement", None)
                    
                    setattr(item, "RefUML_RedefinableElement", self)
                    

    @property
    def RefUML_RedefinableElement82(self):
        return self.__RefUML_RedefinableElement82

    @RefUML_RedefinableElement82.setter
    def RefUML_RedefinableElement82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_RedefinableElement__RefUML_RedefinableElement82", None)
        self.__RefUML_RedefinableElement82 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RefUML_Classifier83"):
                    opp_val = getattr(item, "RefUML_Classifier83", None)
                    
                    if opp_val == self:
                        setattr(item, "RefUML_Classifier83", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RefUML_Classifier83"):
                    opp_val = getattr(item, "RefUML_Classifier83", None)
                    
                    setattr(item, "RefUML_Classifier83", self)
                    

    def isConsistentWith(self, redefinee: RedefinableElement) -> str:
        # TODO: Implement isConsistentWith method
        pass

    def isRedefinitionContextValid(self, redefined: RedefinableElement) -> str:
        # TODO: Implement isRedefinitionContextValid method
        pass

class RefUML_Namespace(NamedElement):

    def __init__(self, Namespace: "RefUML_NamedElement" = None, importingNamespace: set["RefUML_ElementImport"] = None, importingNamespace32: set["RefUML_PackageImport"] = None, context: set["RefUML_Constraintx"] = None, Namespace44: "RefUML_ElementImport" = None, RefUML_Namespace: set["RefUML_NamedElement"] = None, RefUML_Namespace37: set["RefUML_PackageableElement"] = None, namespace: set["RefUML_NamedElement"] = None, Namespace54: "RefUML_Constraintx" = None, Namespace48: "RefUML_PackageImport" = None):
        self.Namespace = Namespace
        self.importingNamespace = importingNamespace if importingNamespace is not None else set()
        self.importingNamespace32 = importingNamespace32 if importingNamespace32 is not None else set()
        self.context = context if context is not None else set()
        self.Namespace44 = Namespace44
        self.RefUML_Namespace = RefUML_Namespace if RefUML_Namespace is not None else set()
        self.RefUML_Namespace37 = RefUML_Namespace37 if RefUML_Namespace37 is not None else set()
        self.namespace = namespace if namespace is not None else set()
        self.Namespace54 = Namespace54
        self.Namespace48 = Namespace48
        
    @property
    def importingNamespace32(self):
        return self.__importingNamespace32

    @importingNamespace32.setter
    def importingNamespace32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_Namespace__importingNamespace32", None)
        self.__importingNamespace32 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PackageImport"):
                    opp_val = getattr(item, "PackageImport", None)
                    
                    if opp_val == self:
                        setattr(item, "PackageImport", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PackageImport"):
                    opp_val = getattr(item, "PackageImport", None)
                    
                    setattr(item, "PackageImport", self)
                    

    @property
    def RefUML_Namespace(self):
        return self.__RefUML_Namespace

    @RefUML_Namespace.setter
    def RefUML_Namespace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_Namespace__RefUML_Namespace", None)
        self.__RefUML_Namespace = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RefUML_NamedElement35"):
                    opp_val = getattr(item, "RefUML_NamedElement35", None)
                    
                    if opp_val == self:
                        setattr(item, "RefUML_NamedElement35", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RefUML_NamedElement35"):
                    opp_val = getattr(item, "RefUML_NamedElement35", None)
                    
                    setattr(item, "RefUML_NamedElement35", self)
                    

    @property
    def Namespace(self):
        return self.__Namespace

    @Namespace.setter
    def Namespace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_Namespace__Namespace", None)
        self.__Namespace = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownedMember"):
                opp_val = getattr(old_value, "ownedMember", None)
                if opp_val == self:
                    setattr(old_value, "ownedMember", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedMember"):
                opp_val = getattr(value, "ownedMember", None)
                setattr(value, "ownedMember", self)

    @property
    def Namespace44(self):
        return self.__Namespace44

    @Namespace44.setter
    def Namespace44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_Namespace__Namespace44", None)
        self.__Namespace44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "elementImport"):
                opp_val = getattr(old_value, "elementImport", None)
                if opp_val == self:
                    setattr(old_value, "elementImport", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "elementImport"):
                opp_val = getattr(value, "elementImport", None)
                setattr(value, "elementImport", self)

    @property
    def Namespace48(self):
        return self.__Namespace48

    @Namespace48.setter
    def Namespace48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_Namespace__Namespace48", None)
        self.__Namespace48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "packageImport"):
                opp_val = getattr(old_value, "packageImport", None)
                if opp_val == self:
                    setattr(old_value, "packageImport", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "packageImport"):
                opp_val = getattr(value, "packageImport", None)
                setattr(value, "packageImport", self)

    @property
    def RefUML_Namespace37(self):
        return self.__RefUML_Namespace37

    @RefUML_Namespace37.setter
    def RefUML_Namespace37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_Namespace__RefUML_Namespace37", None)
        self.__RefUML_Namespace37 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RefUML_PackageableElement38"):
                    opp_val = getattr(item, "RefUML_PackageableElement38", None)
                    
                    if opp_val == self:
                        setattr(item, "RefUML_PackageableElement38", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RefUML_PackageableElement38"):
                    opp_val = getattr(item, "RefUML_PackageableElement38", None)
                    
                    setattr(item, "RefUML_PackageableElement38", self)
                    

    @property
    def importingNamespace(self):
        return self.__importingNamespace

    @importingNamespace.setter
    def importingNamespace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_Namespace__importingNamespace", None)
        self.__importingNamespace = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ElementImport"):
                    opp_val = getattr(item, "ElementImport", None)
                    
                    if opp_val == self:
                        setattr(item, "ElementImport", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ElementImport"):
                    opp_val = getattr(item, "ElementImport", None)
                    
                    setattr(item, "ElementImport", self)
                    

    @property
    def namespace(self):
        return self.__namespace

    @namespace.setter
    def namespace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_Namespace__namespace", None)
        self.__namespace = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "NamedElement40"):
                    opp_val = getattr(item, "NamedElement40", None)
                    
                    if opp_val == self:
                        setattr(item, "NamedElement40", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "NamedElement40"):
                    opp_val = getattr(item, "NamedElement40", None)
                    
                    setattr(item, "NamedElement40", self)
                    

    @property
    def context(self):
        return self.__context

    @context.setter
    def context(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_Namespace__context", None)
        self.__context = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Constraintx"):
                    opp_val = getattr(item, "Constraintx", None)
                    
                    if opp_val == self:
                        setattr(item, "Constraintx", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Constraintx"):
                    opp_val = getattr(item, "Constraintx", None)
                    
                    setattr(item, "Constraintx", self)
                    

    @property
    def Namespace54(self):
        return self.__Namespace54

    @Namespace54.setter
    def Namespace54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_Namespace__Namespace54", None)
        self.__Namespace54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownedRule"):
                opp_val = getattr(old_value, "ownedRule", None)
                if opp_val == self:
                    setattr(old_value, "ownedRule", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedRule"):
                opp_val = getattr(value, "ownedRule", None)
                setattr(value, "ownedRule", self)

    def getImportedMembers(self) -> PackageableElement:
        # TODO: Implement getImportedMembers method
        pass

    def getNamesOfMember(self, element: NamedElement) -> str:
        # TODO: Implement getNamesOfMember method
        pass

    def getImportedElements(self) -> PackageableElement:
        # TODO: Implement getImportedElements method
        pass

    def excludeCollisions(self, imps: PackageableElement) -> PackageableElement:
        # TODO: Implement excludeCollisions method
        pass

    def getImportedPackages(self) -> str:
        # TODO: Implement getImportedPackages method
        pass

    def createPackageImport(self, visibility: str, package_: str) -> str:
        # TODO: Implement createPackageImport method
        pass

    def membersAreDistinguishable(self) -> str:
        # TODO: Implement membersAreDistinguishable method
        pass

    def createElementImport(self, visibility: str, element: PackageableElement) -> str:
        # TODO: Implement createElementImport method
        pass

    def importMembers(self, imps: PackageableElement) -> PackageableElement:
        # TODO: Implement importMembers method
        pass

class RefUML_TypedElement(NamedElement):

    pass
class RefUML_PackageableElement(NamedElement):

    pass
class PackageableElement:

    pass
class RefUML_InstanceSpecification(PackageableElement):

    pass
class RefUML_Dependency(PackageableElement, DirectedRelationship):

    pass
class RefUML_Constraintx(PackageableElement):

    pass
class RefUML_ValueSpecification(PackageableElement, TypedElement):

    def __init__(self, RefUML_ValueSpecification: "RefUML_Constraintx" = None, RefUML_ValueSpecification97: "RefUML_MultiplicityElement" = None, RefUML_ValueSpecification100: "RefUML_MultiplicityElement" = None, RefUML_ValueSpecification110: "RefUML_Property" = None, RefUML_ValueSpecification134: "RefUML_Expression" = None, RefUML_ValueSpecification146: "RefUML_InstanceSpecification" = None, RefUML_ValueSpecification150: "RefUML_Slot" = None):
        self.RefUML_ValueSpecification = RefUML_ValueSpecification
        self.RefUML_ValueSpecification97 = RefUML_ValueSpecification97
        self.RefUML_ValueSpecification100 = RefUML_ValueSpecification100
        self.RefUML_ValueSpecification110 = RefUML_ValueSpecification110
        self.RefUML_ValueSpecification134 = RefUML_ValueSpecification134
        self.RefUML_ValueSpecification146 = RefUML_ValueSpecification146
        self.RefUML_ValueSpecification150 = RefUML_ValueSpecification150
        
    @property
    def RefUML_ValueSpecification146(self):
        return self.__RefUML_ValueSpecification146

    @RefUML_ValueSpecification146.setter
    def RefUML_ValueSpecification146(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_ValueSpecification__RefUML_ValueSpecification146", None)
        self.__RefUML_ValueSpecification146 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefUML_InstanceSpecification145"):
                opp_val = getattr(old_value, "RefUML_InstanceSpecification145", None)
                if opp_val == self:
                    setattr(old_value, "RefUML_InstanceSpecification145", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefUML_InstanceSpecification145"):
                opp_val = getattr(value, "RefUML_InstanceSpecification145", None)
                setattr(value, "RefUML_InstanceSpecification145", self)

    @property
    def RefUML_ValueSpecification97(self):
        return self.__RefUML_ValueSpecification97

    @RefUML_ValueSpecification97.setter
    def RefUML_ValueSpecification97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_ValueSpecification__RefUML_ValueSpecification97", None)
        self.__RefUML_ValueSpecification97 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefUML_MultiplicityElement"):
                opp_val = getattr(old_value, "RefUML_MultiplicityElement", None)
                if opp_val == self:
                    setattr(old_value, "RefUML_MultiplicityElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefUML_MultiplicityElement"):
                opp_val = getattr(value, "RefUML_MultiplicityElement", None)
                setattr(value, "RefUML_MultiplicityElement", self)

    @property
    def RefUML_ValueSpecification100(self):
        return self.__RefUML_ValueSpecification100

    @RefUML_ValueSpecification100.setter
    def RefUML_ValueSpecification100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_ValueSpecification__RefUML_ValueSpecification100", None)
        self.__RefUML_ValueSpecification100 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefUML_MultiplicityElement99"):
                opp_val = getattr(old_value, "RefUML_MultiplicityElement99", None)
                if opp_val == self:
                    setattr(old_value, "RefUML_MultiplicityElement99", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefUML_MultiplicityElement99"):
                opp_val = getattr(value, "RefUML_MultiplicityElement99", None)
                setattr(value, "RefUML_MultiplicityElement99", self)

    @property
    def RefUML_ValueSpecification110(self):
        return self.__RefUML_ValueSpecification110

    @RefUML_ValueSpecification110.setter
    def RefUML_ValueSpecification110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_ValueSpecification__RefUML_ValueSpecification110", None)
        self.__RefUML_ValueSpecification110 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefUML_Property109"):
                opp_val = getattr(old_value, "RefUML_Property109", None)
                if opp_val == self:
                    setattr(old_value, "RefUML_Property109", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefUML_Property109"):
                opp_val = getattr(value, "RefUML_Property109", None)
                setattr(value, "RefUML_Property109", self)

    @property
    def RefUML_ValueSpecification134(self):
        return self.__RefUML_ValueSpecification134

    @RefUML_ValueSpecification134.setter
    def RefUML_ValueSpecification134(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_ValueSpecification__RefUML_ValueSpecification134", None)
        self.__RefUML_ValueSpecification134 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefUML_Expression"):
                opp_val = getattr(old_value, "RefUML_Expression", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefUML_Expression"):
                opp_val = getattr(value, "RefUML_Expression", None)
                if opp_val is None:
                    setattr(value, "RefUML_Expression", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def RefUML_ValueSpecification(self):
        return self.__RefUML_ValueSpecification

    @RefUML_ValueSpecification.setter
    def RefUML_ValueSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_ValueSpecification__RefUML_ValueSpecification", None)
        self.__RefUML_ValueSpecification = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefUML_Constraintx52"):
                opp_val = getattr(old_value, "RefUML_Constraintx52", None)
                if opp_val == self:
                    setattr(old_value, "RefUML_Constraintx52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefUML_Constraintx52"):
                opp_val = getattr(value, "RefUML_Constraintx52", None)
                setattr(value, "RefUML_Constraintx52", self)

    @property
    def RefUML_ValueSpecification150(self):
        return self.__RefUML_ValueSpecification150

    @RefUML_ValueSpecification150.setter
    def RefUML_ValueSpecification150(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_ValueSpecification__RefUML_ValueSpecification150", None)
        self.__RefUML_ValueSpecification150 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefUML_Slot149"):
                opp_val = getattr(old_value, "RefUML_Slot149", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefUML_Slot149"):
                opp_val = getattr(value, "RefUML_Slot149", None)
                if opp_val is None:
                    setattr(value, "RefUML_Slot149", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def booleanValue(self) -> str:
        # TODO: Implement booleanValue method
        pass

    def unlimitedValue(self) -> str:
        # TODO: Implement unlimitedValue method
        pass

    def stringValue(self) -> str:
        # TODO: Implement stringValue method
        pass

    def integerValue(self) -> str:
        # TODO: Implement integerValue method
        pass

    def isNull(self) -> str:
        # TODO: Implement isNull method
        pass

    def isComputable(self) -> str:
        # TODO: Implement isComputable method
        pass

class RefUML_GeneralizationSet(PackageableElement):

    def __init__(self, isCovering: str, isDisjoint: str, GeneralizationSet: "RefUML_Classifier" = None, powertypeExtent: "RefUML_Classifier" = None, generalizationSet: set["RefUML_Generalization"] = None, GeneralizationSet87: "RefUML_Generalization" = None):
        self.isCovering = isCovering
        self.isDisjoint = isDisjoint
        self.GeneralizationSet = GeneralizationSet
        self.powertypeExtent = powertypeExtent
        self.generalizationSet = generalizationSet if generalizationSet is not None else set()
        self.GeneralizationSet87 = GeneralizationSet87
        
    @property
    def isDisjoint(self) -> str:
        return self.__isDisjoint

    @isDisjoint.setter
    def isDisjoint(self, isDisjoint: str):
        self.__isDisjoint = isDisjoint

    @property
    def isCovering(self) -> str:
        return self.__isCovering

    @isCovering.setter
    def isCovering(self, isCovering: str):
        self.__isCovering = isCovering

    @property
    def GeneralizationSet(self):
        return self.__GeneralizationSet

    @GeneralizationSet.setter
    def GeneralizationSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_GeneralizationSet__GeneralizationSet", None)
        self.__GeneralizationSet = value
        
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
    def GeneralizationSet87(self):
        return self.__GeneralizationSet87

    @GeneralizationSet87.setter
    def GeneralizationSet87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_GeneralizationSet__GeneralizationSet87", None)
        self.__GeneralizationSet87 = value
        
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
    def powertypeExtent(self):
        return self.__powertypeExtent

    @powertypeExtent.setter
    def powertypeExtent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_GeneralizationSet__powertypeExtent", None)
        self.__powertypeExtent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Classifier91"):
                opp_val = getattr(old_value, "Classifier91", None)
                if opp_val == self:
                    setattr(old_value, "Classifier91", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Classifier91"):
                opp_val = getattr(value, "Classifier91", None)
                setattr(value, "Classifier91", self)

    @property
    def generalizationSet(self):
        return self.__generalizationSet

    @generalizationSet.setter
    def generalizationSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_GeneralizationSet__generalizationSet", None)
        self.__generalizationSet = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Generalization93"):
                    opp_val = getattr(item, "Generalization93", None)
                    
                    if opp_val == self:
                        setattr(item, "Generalization93", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Generalization93"):
                    opp_val = getattr(item, "Generalization93", None)
                    
                    setattr(item, "Generalization93", self)
                    

class Namespace:

    pass
class RefUML_Classifier(Type, Namespace, RedefinableElement):

    def __init__(self, isAbstract: str, specific: set["RefUML_Generalization"] = None, powertype: set["RefUML_GeneralizationSet"] = None, featuringClassifier: set["RefUML_Feature"] = None, RefUML_Classifier: set["RefUML_NamedElement"] = None, RefUML_Classifier83: "RefUML_RedefinableElement" = None, RefUML_Classifier72: "RefUML_Classifier" = None, RefUML_Classifier70: set["RefUML_Classifier"] = None, RefUML_Classifier75: "RefUML_Classifier" = None, RefUML_Classifier73: set["RefUML_Classifier"] = None, RefUML_Classifier77: set["RefUML_Property"] = None, Classifier: "RefUML_Generalization" = None, Classifier91: "RefUML_GeneralizationSet" = None, RefUML_Classifier85: "RefUML_Generalization" = None, Classifier95: "RefUML_Feature" = None, RefUML_Classifier120: "RefUML_Class" = None, RefUML_Classifier142: "RefUML_InstanceSpecification" = None):
        self.isAbstract = isAbstract
        self.specific = specific if specific is not None else set()
        self.powertype = powertype if powertype is not None else set()
        self.featuringClassifier = featuringClassifier if featuringClassifier is not None else set()
        self.RefUML_Classifier = RefUML_Classifier if RefUML_Classifier is not None else set()
        self.RefUML_Classifier83 = RefUML_Classifier83
        self.RefUML_Classifier72 = RefUML_Classifier72
        self.RefUML_Classifier70 = RefUML_Classifier70 if RefUML_Classifier70 is not None else set()
        self.RefUML_Classifier75 = RefUML_Classifier75
        self.RefUML_Classifier73 = RefUML_Classifier73 if RefUML_Classifier73 is not None else set()
        self.RefUML_Classifier77 = RefUML_Classifier77 if RefUML_Classifier77 is not None else set()
        self.Classifier = Classifier
        self.Classifier91 = Classifier91
        self.RefUML_Classifier85 = RefUML_Classifier85
        self.Classifier95 = Classifier95
        self.RefUML_Classifier120 = RefUML_Classifier120
        self.RefUML_Classifier142 = RefUML_Classifier142
        
    @property
    def isAbstract(self) -> str:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: str):
        self.__isAbstract = isAbstract

    @property
    def RefUML_Classifier73(self):
        return self.__RefUML_Classifier73

    @RefUML_Classifier73.setter
    def RefUML_Classifier73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_Classifier__RefUML_Classifier73", None)
        self.__RefUML_Classifier73 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RefUML_Classifier75"):
                    opp_val = getattr(item, "RefUML_Classifier75", None)
                    
                    if opp_val == self:
                        setattr(item, "RefUML_Classifier75", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RefUML_Classifier75"):
                    opp_val = getattr(item, "RefUML_Classifier75", None)
                    
                    setattr(item, "RefUML_Classifier75", self)
                    

    @property
    def RefUML_Classifier72(self):
        return self.__RefUML_Classifier72

    @RefUML_Classifier72.setter
    def RefUML_Classifier72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_Classifier__RefUML_Classifier72", None)
        self.__RefUML_Classifier72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefUML_Classifier70"):
                opp_val = getattr(old_value, "RefUML_Classifier70", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefUML_Classifier70"):
                opp_val = getattr(value, "RefUML_Classifier70", None)
                if opp_val is None:
                    setattr(value, "RefUML_Classifier70", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Classifier(self):
        return self.__Classifier

    @Classifier.setter
    def Classifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_Classifier__Classifier", None)
        self.__Classifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "generalization89"):
                opp_val = getattr(old_value, "generalization89", None)
                if opp_val == self:
                    setattr(old_value, "generalization89", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "generalization89"):
                opp_val = getattr(value, "generalization89", None)
                setattr(value, "generalization89", self)

    @property
    def RefUML_Classifier(self):
        return self.__RefUML_Classifier

    @RefUML_Classifier.setter
    def RefUML_Classifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_Classifier__RefUML_Classifier", None)
        self.__RefUML_Classifier = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RefUML_NamedElement69"):
                    opp_val = getattr(item, "RefUML_NamedElement69", None)
                    
                    if opp_val == self:
                        setattr(item, "RefUML_NamedElement69", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RefUML_NamedElement69"):
                    opp_val = getattr(item, "RefUML_NamedElement69", None)
                    
                    setattr(item, "RefUML_NamedElement69", self)
                    

    @property
    def Classifier91(self):
        return self.__Classifier91

    @Classifier91.setter
    def Classifier91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_Classifier__Classifier91", None)
        self.__Classifier91 = value
        
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
    def Classifier95(self):
        return self.__Classifier95

    @Classifier95.setter
    def Classifier95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_Classifier__Classifier95", None)
        self.__Classifier95 = value
        
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
    def RefUML_Classifier75(self):
        return self.__RefUML_Classifier75

    @RefUML_Classifier75.setter
    def RefUML_Classifier75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_Classifier__RefUML_Classifier75", None)
        self.__RefUML_Classifier75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefUML_Classifier73"):
                opp_val = getattr(old_value, "RefUML_Classifier73", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefUML_Classifier73"):
                opp_val = getattr(value, "RefUML_Classifier73", None)
                if opp_val is None:
                    setattr(value, "RefUML_Classifier73", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def specific(self):
        return self.__specific

    @specific.setter
    def specific(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_Classifier__specific", None)
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
        old_value = getattr(self, f"_RefUML_Classifier__powertype", None)
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
    def RefUML_Classifier142(self):
        return self.__RefUML_Classifier142

    @RefUML_Classifier142.setter
    def RefUML_Classifier142(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_Classifier__RefUML_Classifier142", None)
        self.__RefUML_Classifier142 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefUML_InstanceSpecification"):
                opp_val = getattr(old_value, "RefUML_InstanceSpecification", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefUML_InstanceSpecification"):
                opp_val = getattr(value, "RefUML_InstanceSpecification", None)
                if opp_val is None:
                    setattr(value, "RefUML_InstanceSpecification", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def RefUML_Classifier120(self):
        return self.__RefUML_Classifier120

    @RefUML_Classifier120.setter
    def RefUML_Classifier120(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_Classifier__RefUML_Classifier120", None)
        self.__RefUML_Classifier120 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefUML_Class"):
                opp_val = getattr(old_value, "RefUML_Class", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefUML_Class"):
                opp_val = getattr(value, "RefUML_Class", None)
                if opp_val is None:
                    setattr(value, "RefUML_Class", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def RefUML_Classifier70(self):
        return self.__RefUML_Classifier70

    @RefUML_Classifier70.setter
    def RefUML_Classifier70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_Classifier__RefUML_Classifier70", None)
        self.__RefUML_Classifier70 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RefUML_Classifier72"):
                    opp_val = getattr(item, "RefUML_Classifier72", None)
                    
                    if opp_val == self:
                        setattr(item, "RefUML_Classifier72", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RefUML_Classifier72"):
                    opp_val = getattr(item, "RefUML_Classifier72", None)
                    
                    setattr(item, "RefUML_Classifier72", self)
                    

    @property
    def RefUML_Classifier77(self):
        return self.__RefUML_Classifier77

    @RefUML_Classifier77.setter
    def RefUML_Classifier77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_Classifier__RefUML_Classifier77", None)
        self.__RefUML_Classifier77 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RefUML_Property78"):
                    opp_val = getattr(item, "RefUML_Property78", None)
                    
                    if opp_val == self:
                        setattr(item, "RefUML_Property78", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RefUML_Property78"):
                    opp_val = getattr(item, "RefUML_Property78", None)
                    
                    setattr(item, "RefUML_Property78", self)
                    

    @property
    def featuringClassifier(self):
        return self.__featuringClassifier

    @featuringClassifier.setter
    def featuringClassifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_Classifier__featuringClassifier", None)
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
    def RefUML_Classifier83(self):
        return self.__RefUML_Classifier83

    @RefUML_Classifier83.setter
    def RefUML_Classifier83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_Classifier__RefUML_Classifier83", None)
        self.__RefUML_Classifier83 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefUML_RedefinableElement82"):
                opp_val = getattr(old_value, "RefUML_RedefinableElement82", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefUML_RedefinableElement82"):
                opp_val = getattr(value, "RefUML_RedefinableElement82", None)
                if opp_val is None:
                    setattr(value, "RefUML_RedefinableElement82", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def RefUML_Classifier85(self):
        return self.__RefUML_Classifier85

    @RefUML_Classifier85.setter
    def RefUML_Classifier85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_Classifier__RefUML_Classifier85", None)
        self.__RefUML_Classifier85 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefUML_Generalization"):
                opp_val = getattr(old_value, "RefUML_Generalization", None)
                if opp_val == self:
                    setattr(old_value, "RefUML_Generalization", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefUML_Generalization"):
                opp_val = getattr(value, "RefUML_Generalization", None)
                setattr(value, "RefUML_Generalization", self)

    def hasKindOffspring(self) -> bool:
        # TODO: Implement hasKindOffspring method
        pass

    def hasKindAncestor(self) -> bool:
        # TODO: Implement hasKindAncestor method
        pass

    def allFeatures(self) -> str:
        # TODO: Implement allFeatures method
        pass

    def getAllAttributes(self) -> str:
        # TODO: Implement getAllAttributes method
        pass

    def conformsTo(self, other: Classifier) -> str:
        # TODO: Implement conformsTo method
        pass

    def hasCollectiveOffspring(self) -> bool:
        # TODO: Implement hasCollectiveOffspring method
        pass

    def parents(self) -> Classifier:
        # TODO: Implement parents method
        pass

    def inherit(self, inhs: NamedElement) -> NamedElement:
        # TODO: Implement inherit method
        pass

    def hasCollectiveInstances(self) -> bool:
        # TODO: Implement hasCollectiveInstances method
        pass

    def hasQuantityOffspring(self) -> bool:
        # TODO: Implement hasQuantityOffspring method
        pass

    def hasQuantityAncestor(self) -> bool:
        # TODO: Implement hasQuantityAncestor method
        pass

    def hasVisibilityOf(self, n: NamedElement) -> str:
        # TODO: Implement hasVisibilityOf method
        pass

    def getGenerals(self) -> Classifier:
        # TODO: Implement getGenerals method
        pass

    def hasCollectiveAncestor(self) -> bool:
        # TODO: Implement hasCollectiveAncestor method
        pass

    def inheritableMembers(self, c: Classifier) -> NamedElement:
        # TODO: Implement inheritableMembers method
        pass

    def hasFunctionalComplexInstances(self) -> bool:
        # TODO: Implement hasFunctionalComplexInstances method
        pass

    def maySpecializeType(self, c: Classifier) -> str:
        # TODO: Implement maySpecializeType method
        pass

    def hasQuantityInstances(self) -> bool:
        # TODO: Implement hasQuantityInstances method
        pass

    def getInheritedMembers(self) -> NamedElement:
        # TODO: Implement getInheritedMembers method
        pass

    def allParents(self) -> Classifier:
        # TODO: Implement allParents method
        pass

class RefUML_Type(PackageableElement):

    def __init__(self, Type: "RefUML_Package" = None, RefUML_Type: "RefUML_TypedElement" = None, RefUML_Type62: "RefUML_Association" = None, ownedType: "RefUML_Package" = None):
        self.Type = Type
        self.RefUML_Type = RefUML_Type
        self.RefUML_Type62 = RefUML_Type62
        self.ownedType = ownedType
        
    @property
    def Type(self):
        return self.__Type

    @Type.setter
    def Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_Type__Type", None)
        self.__Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "package"):
                opp_val = getattr(old_value, "package", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "package"):
                opp_val = getattr(value, "package", None)
                if opp_val is None:
                    setattr(value, "package", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ownedType(self):
        return self.__ownedType

    @ownedType.setter
    def ownedType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_Type__ownedType", None)
        self.__ownedType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Package57"):
                opp_val = getattr(old_value, "Package57", None)
                if opp_val == self:
                    setattr(old_value, "Package57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Package57"):
                opp_val = getattr(value, "Package57", None)
                setattr(value, "Package57", self)

    @property
    def RefUML_Type(self):
        return self.__RefUML_Type

    @RefUML_Type.setter
    def RefUML_Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_Type__RefUML_Type", None)
        self.__RefUML_Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefUML_TypedElement"):
                opp_val = getattr(old_value, "RefUML_TypedElement", None)
                if opp_val == self:
                    setattr(old_value, "RefUML_TypedElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefUML_TypedElement"):
                opp_val = getattr(value, "RefUML_TypedElement", None)
                setattr(value, "RefUML_TypedElement", self)

    @property
    def RefUML_Type62(self):
        return self.__RefUML_Type62

    @RefUML_Type62.setter
    def RefUML_Type62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_Type__RefUML_Type62", None)
        self.__RefUML_Type62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefUML_Association"):
                opp_val = getattr(old_value, "RefUML_Association", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefUML_Association"):
                opp_val = getattr(value, "RefUML_Association", None)
                if opp_val is None:
                    setattr(value, "RefUML_Association", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def conformsTo(self, other: str) -> str:
        # TODO: Implement conformsTo method
        pass

    def getAssociations(self) -> str:
        # TODO: Implement getAssociations method
        pass

    def createAssociation(self, end2Upper: str, end1Name: str, end2IsNavigable: str, end1Aggregation: str, end1Upper: str, end1Type: str, end2Name: str, end2Lower: str, end1IsNavigable: str, end1Lower: str, end2Aggregation: str) -> str:
        # TODO: Implement createAssociation method
        pass

class RefUML_Package(PackageableElement, Namespace):

    def __init__(self, package: set["RefUML_Type"] = None, receivingPackage: set["RefUML_PackageMerge"] = None, RefUML_Package: set["RefUML_PackageableElement"] = None, Package: "RefUML_Package" = None, nestingPackage: set["RefUML_Package"] = None, Package16: "RefUML_Package" = None, nestedPackage: "RefUML_Package" = None, RefUML_Package46: "RefUML_PackageImport" = None, Package57: "RefUML_Type" = None, RefUML_Package136: "RefUML_PackageMerge" = None, Package138: "RefUML_PackageMerge" = None):
        self.package = package if package is not None else set()
        self.receivingPackage = receivingPackage if receivingPackage is not None else set()
        self.RefUML_Package = RefUML_Package if RefUML_Package is not None else set()
        self.Package = Package
        self.nestingPackage = nestingPackage if nestingPackage is not None else set()
        self.Package16 = Package16
        self.nestedPackage = nestedPackage
        self.RefUML_Package46 = RefUML_Package46
        self.Package57 = Package57
        self.RefUML_Package136 = RefUML_Package136
        self.Package138 = Package138
        
    @property
    def nestingPackage(self):
        return self.__nestingPackage

    @nestingPackage.setter
    def nestingPackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_Package__nestingPackage", None)
        self.__nestingPackage = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Package"):
                    opp_val = getattr(item, "Package", None)
                    
                    if opp_val == self:
                        setattr(item, "Package", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Package"):
                    opp_val = getattr(item, "Package", None)
                    
                    setattr(item, "Package", self)
                    

    @property
    def RefUML_Package46(self):
        return self.__RefUML_Package46

    @RefUML_Package46.setter
    def RefUML_Package46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_Package__RefUML_Package46", None)
        self.__RefUML_Package46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefUML_PackageImport"):
                opp_val = getattr(old_value, "RefUML_PackageImport", None)
                if opp_val == self:
                    setattr(old_value, "RefUML_PackageImport", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefUML_PackageImport"):
                opp_val = getattr(value, "RefUML_PackageImport", None)
                setattr(value, "RefUML_PackageImport", self)

    @property
    def Package16(self):
        return self.__Package16

    @Package16.setter
    def Package16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_Package__Package16", None)
        self.__Package16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nestedPackage"):
                opp_val = getattr(old_value, "nestedPackage", None)
                if opp_val == self:
                    setattr(old_value, "nestedPackage", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nestedPackage"):
                opp_val = getattr(value, "nestedPackage", None)
                setattr(value, "nestedPackage", self)

    @property
    def Package138(self):
        return self.__Package138

    @Package138.setter
    def Package138(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_Package__Package138", None)
        self.__Package138 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "packageMerge"):
                opp_val = getattr(old_value, "packageMerge", None)
                if opp_val == self:
                    setattr(old_value, "packageMerge", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "packageMerge"):
                opp_val = getattr(value, "packageMerge", None)
                setattr(value, "packageMerge", self)

    @property
    def receivingPackage(self):
        return self.__receivingPackage

    @receivingPackage.setter
    def receivingPackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_Package__receivingPackage", None)
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
                    

    @property
    def RefUML_Package136(self):
        return self.__RefUML_Package136

    @RefUML_Package136.setter
    def RefUML_Package136(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_Package__RefUML_Package136", None)
        self.__RefUML_Package136 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefUML_PackageMerge"):
                opp_val = getattr(old_value, "RefUML_PackageMerge", None)
                if opp_val == self:
                    setattr(old_value, "RefUML_PackageMerge", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefUML_PackageMerge"):
                opp_val = getattr(value, "RefUML_PackageMerge", None)
                setattr(value, "RefUML_PackageMerge", self)

    @property
    def RefUML_Package(self):
        return self.__RefUML_Package

    @RefUML_Package.setter
    def RefUML_Package(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_Package__RefUML_Package", None)
        self.__RefUML_Package = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RefUML_PackageableElement"):
                    opp_val = getattr(item, "RefUML_PackageableElement", None)
                    
                    if opp_val == self:
                        setattr(item, "RefUML_PackageableElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RefUML_PackageableElement"):
                    opp_val = getattr(item, "RefUML_PackageableElement", None)
                    
                    setattr(item, "RefUML_PackageableElement", self)
                    

    @property
    def package(self):
        return self.__package

    @package.setter
    def package(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_Package__package", None)
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
    def nestedPackage(self):
        return self.__nestedPackage

    @nestedPackage.setter
    def nestedPackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_Package__nestedPackage", None)
        self.__nestedPackage = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Package16"):
                opp_val = getattr(old_value, "Package16", None)
                if opp_val == self:
                    setattr(old_value, "Package16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Package16"):
                opp_val = getattr(value, "Package16", None)
                setattr(value, "Package16", self)

    @property
    def Package57(self):
        return self.__Package57

    @Package57.setter
    def Package57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_Package__Package57", None)
        self.__Package57 = value
        
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

    @property
    def Package(self):
        return self.__Package

    @Package.setter
    def Package(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_Package__Package", None)
        self.__Package = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nestingPackage"):
                opp_val = getattr(old_value, "nestingPackage", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nestingPackage"):
                opp_val = getattr(value, "nestingPackage", None)
                if opp_val is None:
                    setattr(value, "nestingPackage", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def createOwnedClass(self, isAbstract: str, name: str) -> str:
        # TODO: Implement createOwnedClass method
        pass

    def makesVisible(self, el: str) -> str:
        # TODO: Implement makesVisible method
        pass

    def visibleMembers(self) -> PackageableElement:
        # TODO: Implement visibleMembers method
        pass

    def createOwnedInterface(self, name: str):
        # TODO: Implement createOwnedInterface method
        pass

    def getAppliedProfile(self, recurse: str, qualifiedName: str):
        # TODO: Implement getAppliedProfile method
        pass

    def createOwnedEnumeration(self, name: str) -> str:
        # TODO: Implement createOwnedEnumeration method
        pass

    def createOwnedPrimitiveType(self, name: str) -> str:
        # TODO: Implement createOwnedPrimitiveType method
        pass

    def isModelLibrary(self) -> str:
        # TODO: Implement isModelLibrary method
        pass

    def getAppliedProfile(self, qualifiedName: str):
        # TODO: Implement getAppliedProfile method
        pass

class Element:

    pass
class RefUML_NamedElement(Element):

    def __init__(self, qualifiedName: str, name: str, visibility: str, client: set["RefUML_Dependency"] = None, ownedMember: "RefUML_Namespace" = None, RefUML_NamedElement: "RefUML_StringExpression" = None, RefUML_NamedElement21: "RefUML_Dependency" = None, NamedElement: "RefUML_Dependency" = None, RefUML_NamedElement35: "RefUML_Namespace" = None, NamedElement40: "RefUML_Namespace" = None, RefUML_NamedElement69: "RefUML_Classifier" = None):
        self.qualifiedName = qualifiedName
        self.name = name
        self.visibility = visibility
        self.client = client if client is not None else set()
        self.ownedMember = ownedMember
        self.RefUML_NamedElement = RefUML_NamedElement
        self.RefUML_NamedElement21 = RefUML_NamedElement21
        self.NamedElement = NamedElement
        self.RefUML_NamedElement35 = RefUML_NamedElement35
        self.NamedElement40 = NamedElement40
        self.RefUML_NamedElement69 = RefUML_NamedElement69
        
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
    def RefUML_NamedElement21(self):
        return self.__RefUML_NamedElement21

    @RefUML_NamedElement21.setter
    def RefUML_NamedElement21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_NamedElement__RefUML_NamedElement21", None)
        self.__RefUML_NamedElement21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefUML_Dependency"):
                opp_val = getattr(old_value, "RefUML_Dependency", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefUML_Dependency"):
                opp_val = getattr(value, "RefUML_Dependency", None)
                if opp_val is None:
                    setattr(value, "RefUML_Dependency", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def RefUML_NamedElement35(self):
        return self.__RefUML_NamedElement35

    @RefUML_NamedElement35.setter
    def RefUML_NamedElement35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_NamedElement__RefUML_NamedElement35", None)
        self.__RefUML_NamedElement35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefUML_Namespace"):
                opp_val = getattr(old_value, "RefUML_Namespace", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefUML_Namespace"):
                opp_val = getattr(value, "RefUML_Namespace", None)
                if opp_val is None:
                    setattr(value, "RefUML_Namespace", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def NamedElement40(self):
        return self.__NamedElement40

    @NamedElement40.setter
    def NamedElement40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_NamedElement__NamedElement40", None)
        self.__NamedElement40 = value
        
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

    @property
    def client(self):
        return self.__client

    @client.setter
    def client(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_NamedElement__client", None)
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
    def RefUML_NamedElement69(self):
        return self.__RefUML_NamedElement69

    @RefUML_NamedElement69.setter
    def RefUML_NamedElement69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_NamedElement__RefUML_NamedElement69", None)
        self.__RefUML_NamedElement69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefUML_Classifier"):
                opp_val = getattr(old_value, "RefUML_Classifier", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefUML_Classifier"):
                opp_val = getattr(value, "RefUML_Classifier", None)
                if opp_val is None:
                    setattr(value, "RefUML_Classifier", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ownedMember(self):
        return self.__ownedMember

    @ownedMember.setter
    def ownedMember(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_NamedElement__ownedMember", None)
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
    def RefUML_NamedElement(self):
        return self.__RefUML_NamedElement

    @RefUML_NamedElement.setter
    def RefUML_NamedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_NamedElement__RefUML_NamedElement", None)
        self.__RefUML_NamedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefUML_StringExpression"):
                opp_val = getattr(old_value, "RefUML_StringExpression", None)
                if opp_val == self:
                    setattr(old_value, "RefUML_StringExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefUML_StringExpression"):
                opp_val = getattr(value, "RefUML_StringExpression", None)
                setattr(value, "RefUML_StringExpression", self)

    @property
    def NamedElement(self):
        return self.__NamedElement

    @NamedElement.setter
    def NamedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_NamedElement__NamedElement", None)
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

    def createDependency(self, supplier: NamedElement) -> str:
        # TODO: Implement createDependency method
        pass

    def isDistinguishableFrom(self, ns: Namespace, n: NamedElement) -> str:
        # TODO: Implement isDistinguishableFrom method
        pass

    def createUsage(self, supplier: NamedElement):
        # TODO: Implement createUsage method
        pass

    def separator(self) -> str:
        # TODO: Implement separator method
        pass

    def allOwningPackages(self) -> str:
        # TODO: Implement allOwningPackages method
        pass

    def allNamespaces(self) -> Namespace:
        # TODO: Implement allNamespaces method
        pass

    def getQualifiedName(self) -> str:
        # TODO: Implement getQualifiedName method
        pass

    def getLabel(self, localize: str) -> str:
        # TODO: Implement getLabel method
        pass

    def getLabel(self) -> str:
        # TODO: Implement getLabel method
        pass

class RefUML_Slot(Element):

    pass
class RefUML_Relationship(Element):

    pass
class RefUML_MultiplicityElement(Element):

    def __init__(self, isOrdered: str, lower: str, isUnique: str, upper: str, RefUML_MultiplicityElement: "RefUML_ValueSpecification" = None, RefUML_MultiplicityElement99: "RefUML_ValueSpecification" = None):
        self.isOrdered = isOrdered
        self.lower = lower
        self.isUnique = isUnique
        self.upper = upper
        self.RefUML_MultiplicityElement = RefUML_MultiplicityElement
        self.RefUML_MultiplicityElement99 = RefUML_MultiplicityElement99
        
    @property
    def upper(self) -> str:
        return self.__upper

    @upper.setter
    def upper(self, upper: str):
        self.__upper = upper

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
    def lower(self) -> str:
        return self.__lower

    @lower.setter
    def lower(self, lower: str):
        self.__lower = lower

    @property
    def RefUML_MultiplicityElement99(self):
        return self.__RefUML_MultiplicityElement99

    @RefUML_MultiplicityElement99.setter
    def RefUML_MultiplicityElement99(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_MultiplicityElement__RefUML_MultiplicityElement99", None)
        self.__RefUML_MultiplicityElement99 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefUML_ValueSpecification100"):
                opp_val = getattr(old_value, "RefUML_ValueSpecification100", None)
                if opp_val == self:
                    setattr(old_value, "RefUML_ValueSpecification100", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefUML_ValueSpecification100"):
                opp_val = getattr(value, "RefUML_ValueSpecification100", None)
                setattr(value, "RefUML_ValueSpecification100", self)

    @property
    def RefUML_MultiplicityElement(self):
        return self.__RefUML_MultiplicityElement

    @RefUML_MultiplicityElement.setter
    def RefUML_MultiplicityElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_MultiplicityElement__RefUML_MultiplicityElement", None)
        self.__RefUML_MultiplicityElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefUML_ValueSpecification97"):
                opp_val = getattr(old_value, "RefUML_ValueSpecification97", None)
                if opp_val == self:
                    setattr(old_value, "RefUML_ValueSpecification97", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefUML_ValueSpecification97"):
                opp_val = getattr(value, "RefUML_ValueSpecification97", None)
                setattr(value, "RefUML_ValueSpecification97", self)

    def includesCardinality(self, C: str) -> str:
        # TODO: Implement includesCardinality method
        pass

    def upperBound(self) -> str:
        # TODO: Implement upperBound method
        pass

    def includesMultiplicity(self, M: str) -> str:
        # TODO: Implement includesMultiplicity method
        pass

    def getUpper(self) -> str:
        # TODO: Implement getUpper method
        pass

    def compatibleWith(self, other: str) -> str:
        # TODO: Implement compatibleWith method
        pass

    def is(self, upperbound: str, lowerbound: str) -> str:
        # TODO: Implement is method
        pass

    def setLower(self, newLower: str):
        # TODO: Implement setLower method
        pass

    def setUpper(self, newUpper: str):
        # TODO: Implement setUpper method
        pass

    def lowerBound(self) -> str:
        # TODO: Implement lowerBound method
        pass

    def getLower(self) -> str:
        # TODO: Implement getLower method
        pass

    def isMultivalued(self) -> str:
        # TODO: Implement isMultivalued method
        pass

class RefUML_Comment(Element):

    def __init__(self, body: str, RefUML_Comment: set["RefUML_Element"] = None, RefUML_Comment8: "RefUML_Element" = None):
        self.body = body
        self.RefUML_Comment = RefUML_Comment if RefUML_Comment is not None else set()
        self.RefUML_Comment8 = RefUML_Comment8
        
    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

    @property
    def RefUML_Comment(self):
        return self.__RefUML_Comment

    @RefUML_Comment.setter
    def RefUML_Comment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_Comment__RefUML_Comment", None)
        self.__RefUML_Comment = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RefUML_Element"):
                    opp_val = getattr(item, "RefUML_Element", None)
                    
                    if opp_val == self:
                        setattr(item, "RefUML_Element", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RefUML_Element"):
                    opp_val = getattr(item, "RefUML_Element", None)
                    
                    setattr(item, "RefUML_Element", self)
                    

    @property
    def RefUML_Comment8(self):
        return self.__RefUML_Comment8

    @RefUML_Comment8.setter
    def RefUML_Comment8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_Comment__RefUML_Comment8", None)
        self.__RefUML_Comment8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefUML_Element7"):
                opp_val = getattr(old_value, "RefUML_Element7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefUML_Element7"):
                opp_val = getattr(value, "RefUML_Element7", None)
                if opp_val is None:
                    setattr(value, "RefUML_Element7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class EModelElement:

    pass
class RefUML_Element(EModelElement):

    def __init__(self, RefUML_Element: "RefUML_Comment" = None, Element: "RefUML_Element" = None, owner: set["RefUML_Element"] = None, Element5: "RefUML_Element" = None, ownedElement: "RefUML_Element" = None, RefUML_Element7: set["RefUML_Comment"] = None, RefUML_Element27: "RefUML_DirectedRelationship" = None, RefUML_Element29: "RefUML_Relationship" = None, RefUML_Element24: "RefUML_DirectedRelationship" = None, RefUML_Element50: "RefUML_Constraintx" = None):
        self.RefUML_Element = RefUML_Element
        self.Element = Element
        self.owner = owner if owner is not None else set()
        self.Element5 = Element5
        self.ownedElement = ownedElement
        self.RefUML_Element7 = RefUML_Element7 if RefUML_Element7 is not None else set()
        self.RefUML_Element27 = RefUML_Element27
        self.RefUML_Element29 = RefUML_Element29
        self.RefUML_Element24 = RefUML_Element24
        self.RefUML_Element50 = RefUML_Element50
        
    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_Element__owner", None)
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
    def RefUML_Element27(self):
        return self.__RefUML_Element27

    @RefUML_Element27.setter
    def RefUML_Element27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_Element__RefUML_Element27", None)
        self.__RefUML_Element27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefUML_DirectedRelationship26"):
                opp_val = getattr(old_value, "RefUML_DirectedRelationship26", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefUML_DirectedRelationship26"):
                opp_val = getattr(value, "RefUML_DirectedRelationship26", None)
                if opp_val is None:
                    setattr(value, "RefUML_DirectedRelationship26", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def RefUML_Element(self):
        return self.__RefUML_Element

    @RefUML_Element.setter
    def RefUML_Element(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_Element__RefUML_Element", None)
        self.__RefUML_Element = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefUML_Comment"):
                opp_val = getattr(old_value, "RefUML_Comment", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefUML_Comment"):
                opp_val = getattr(value, "RefUML_Comment", None)
                if opp_val is None:
                    setattr(value, "RefUML_Comment", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def RefUML_Element7(self):
        return self.__RefUML_Element7

    @RefUML_Element7.setter
    def RefUML_Element7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_Element__RefUML_Element7", None)
        self.__RefUML_Element7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RefUML_Comment8"):
                    opp_val = getattr(item, "RefUML_Comment8", None)
                    
                    if opp_val == self:
                        setattr(item, "RefUML_Comment8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RefUML_Comment8"):
                    opp_val = getattr(item, "RefUML_Comment8", None)
                    
                    setattr(item, "RefUML_Comment8", self)
                    

    @property
    def RefUML_Element29(self):
        return self.__RefUML_Element29

    @RefUML_Element29.setter
    def RefUML_Element29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_Element__RefUML_Element29", None)
        self.__RefUML_Element29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefUML_Relationship"):
                opp_val = getattr(old_value, "RefUML_Relationship", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefUML_Relationship"):
                opp_val = getattr(value, "RefUML_Relationship", None)
                if opp_val is None:
                    setattr(value, "RefUML_Relationship", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ownedElement(self):
        return self.__ownedElement

    @ownedElement.setter
    def ownedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_Element__ownedElement", None)
        self.__ownedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Element5"):
                opp_val = getattr(old_value, "Element5", None)
                if opp_val == self:
                    setattr(old_value, "Element5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Element5"):
                opp_val = getattr(value, "Element5", None)
                setattr(value, "Element5", self)

    @property
    def Element(self):
        return self.__Element

    @Element.setter
    def Element(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_Element__Element", None)
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
    def RefUML_Element24(self):
        return self.__RefUML_Element24

    @RefUML_Element24.setter
    def RefUML_Element24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_Element__RefUML_Element24", None)
        self.__RefUML_Element24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefUML_DirectedRelationship"):
                opp_val = getattr(old_value, "RefUML_DirectedRelationship", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefUML_DirectedRelationship"):
                opp_val = getattr(value, "RefUML_DirectedRelationship", None)
                if opp_val is None:
                    setattr(value, "RefUML_DirectedRelationship", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Element5(self):
        return self.__Element5

    @Element5.setter
    def Element5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_Element__Element5", None)
        self.__Element5 = value
        
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
    def RefUML_Element50(self):
        return self.__RefUML_Element50

    @RefUML_Element50.setter
    def RefUML_Element50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefUML_Element__RefUML_Element50", None)
        self.__RefUML_Element50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefUML_Constraintx"):
                opp_val = getattr(old_value, "RefUML_Constraintx", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefUML_Constraintx"):
                opp_val = getattr(value, "RefUML_Constraintx", None)
                if opp_val is None:
                    setattr(value, "RefUML_Constraintx", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def getApplicableStereotype(self, qualifiedName: str):
        # TODO: Implement getApplicableStereotype method
        pass

    def getTargetDirectedRelationships(self) -> str:
        # TODO: Implement getTargetDirectedRelationships method
        pass

    def getNearestPackage(self) -> str:
        # TODO: Implement getNearestPackage method
        pass

    def hasKeyword(self, keyword: str) -> str:
        # TODO: Implement hasKeyword method
        pass

    def getRelationships(self) -> str:
        # TODO: Implement getRelationships method
        pass

    def getRelationships(self, eClass: str) -> str:
        # TODO: Implement getRelationships method
        pass

    def addKeyword(self, keyword: str) -> str:
        # TODO: Implement addKeyword method
        pass

    def getAppliedStereotype(self, qualifiedName: str):
        # TODO: Implement getAppliedStereotype method
        pass

    def allOwnedElements(self) -> Element:
        # TODO: Implement allOwnedElements method
        pass

    def removeKeyword(self, keyword: str) -> str:
        # TODO: Implement removeKeyword method
        pass

    def getStereotypeApplications(self) -> str:
        # TODO: Implement getStereotypeApplications method
        pass

    def getModel(self) -> str:
        # TODO: Implement getModel method
        pass

    def getSourceDirectedRelationships(self) -> str:
        # TODO: Implement getSourceDirectedRelationships method
        pass

    def getKeywords(self) -> str:
        # TODO: Implement getKeywords method
        pass

    def destroy(self):
        # TODO: Implement destroy method
        pass

    def mustBeOwned(self) -> str:
        # TODO: Implement mustBeOwned method
        pass

    def createEAnnotation(self, source: str) -> str:
        # TODO: Implement createEAnnotation method
        pass

    def getRequiredStereotype(self, qualifiedName: str):
        # TODO: Implement getRequiredStereotype method
        pass

    def getSourceDirectedRelationships(self, eClass: str) -> str:
        # TODO: Implement getSourceDirectedRelationships method
        pass

    def getTargetDirectedRelationships(self, eClass: str) -> str:
        # TODO: Implement getTargetDirectedRelationships method
        pass
