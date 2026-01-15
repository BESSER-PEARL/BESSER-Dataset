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
    private = "private"
    protected = "protected"
    package = "package"
    public = "public"


############################################
# Definition of Classes
############################################

class DependencyRelationship:

    pass
class RefOntoUML_Mediation(DependencyRelationship):

    def __init__(self):
        
    def mediatedEnd(self) -> str:
        # TODO: Implement mediatedEnd method
        pass

    def relator(self) -> Classifier:
        # TODO: Implement relator method
        pass

    def mediated(self) -> Classifier:
        # TODO: Implement mediated method
        pass

    def relatorEnd(self) -> str:
        # TODO: Implement relatorEnd method
        pass

class RefOntoUML_Derivation(DependencyRelationship):

    def __init__(self):
        
    def material(self) -> Classifier:
        # TODO: Implement material method
        pass

    def materialEnd(self) -> str:
        # TODO: Implement materialEnd method
        pass

    def relatorEnd(self) -> str:
        # TODO: Implement relatorEnd method
        pass

    def relator(self) -> Classifier:
        # TODO: Implement relator method
        pass

class RefOntoUML_Characterization(DependencyRelationship):

    def __init__(self):
        
    def characterized(self) -> Classifier:
        # TODO: Implement characterized method
        pass

    def characterizingEnd(self) -> str:
        # TODO: Implement characterizingEnd method
        pass

    def characterizedEnd(self) -> str:
        # TODO: Implement characterizedEnd method
        pass

    def characterizing(self) -> Classifier:
        # TODO: Implement characterizing method
        pass

class Meronymic:

    pass
class RefOntoUML_componentOf(Meronymic):

    pass
class RefOntoUML_subQuantityOf(Meronymic):

    pass
class DirectedBinaryAssociation:

    pass
class RefOntoUML_DependencyRelationship(DirectedBinaryAssociation):

    pass
class RefOntoUML_Meronymic(DirectedBinaryAssociation):

    def __init__(self, isShareable: bool, isEssential: bool, isInseparable: bool, isImmutablePart: bool, isImmutableWhole: bool):
        self.isShareable = isShareable
        self.isEssential = isEssential
        self.isInseparable = isInseparable
        self.isImmutablePart = isImmutablePart
        self.isImmutableWhole = isImmutableWhole
        
    @property
    def isImmutablePart(self) -> bool:
        return self.__isImmutablePart

    @isImmutablePart.setter
    def isImmutablePart(self, isImmutablePart: bool):
        self.__isImmutablePart = isImmutablePart

    @property
    def isInseparable(self) -> bool:
        return self.__isInseparable

    @isInseparable.setter
    def isInseparable(self, isInseparable: bool):
        self.__isInseparable = isInseparable

    @property
    def isImmutableWhole(self) -> bool:
        return self.__isImmutableWhole

    @isImmutableWhole.setter
    def isImmutableWhole(self, isImmutableWhole: bool):
        self.__isImmutableWhole = isImmutableWhole

    @property
    def isEssential(self) -> bool:
        return self.__isEssential

    @isEssential.setter
    def isEssential(self, isEssential: bool):
        self.__isEssential = isEssential

    @property
    def isShareable(self) -> bool:
        return self.__isShareable

    @isShareable.setter
    def isShareable(self, isShareable: bool):
        self.__isShareable = isShareable

    def partEnd(self) -> str:
        # TODO: Implement partEnd method
        pass

    def part(self) -> Classifier:
        # TODO: Implement part method
        pass

    def whole(self) -> Classifier:
        # TODO: Implement whole method
        pass

    def wholeEnd(self) -> str:
        # TODO: Implement wholeEnd method
        pass

class RefOntoUML_memberOf(Meronymic):

    pass
class RefOntoUML_subCollectionOf(Meronymic):

    pass
class IntrinsicMomentClass:

    pass
class RefOntoUML_Quality(IntrinsicMomentClass):

    pass
class RefOntoUML_Mode(IntrinsicMomentClass):

    pass
class MomentClass:

    pass
class RefOntoUML_IntrinsicMomentClass(MomentClass):

    def __init__(self):
        
    def characterized(self) -> Classifier:
        # TODO: Implement characterized method
        pass

    def characterization(self) -> str:
        # TODO: Implement characterization method
        pass

class SemiRigidMixinClass:

    pass
class RefOntoUML_Mixin(SemiRigidMixinClass):

    pass
class AntiRigidMixinClass:

    pass
class RefOntoUML_RoleMixin(AntiRigidMixinClass):

    def __init__(self):
        
    def roles(self) -> str:
        # TODO: Implement roles method
        pass

    def rigidSortals(self) -> RigidSortalClass:
        # TODO: Implement rigidSortals method
        pass

    def mediation(self) -> str:
        # TODO: Implement mediation method
        pass

    def relator(self) -> str:
        # TODO: Implement relator method
        pass

class Association:

    pass
class RefOntoUML_FormalAssociation(Association):

    pass
class RefOntoUML_MaterialAssociation(Association):

    pass
class RefOntoUML_DirectedBinaryAssociation(Association):

    def __init__(self):
        
    def targetEnd(self) -> str:
        # TODO: Implement targetEnd method
        pass

    def sourceEnd(self) -> str:
        # TODO: Implement sourceEnd method
        pass

class RefOntoUML_Relator(MomentClass):

    def __init__(self):
        
    def mediated(self) -> Classifier:
        # TODO: Implement mediated method
        pass

    def mediations(self) -> str:
        # TODO: Implement mediations method
        pass

class AntiRigidSortalClass:

    pass
class RefOntoUML_Role(AntiRigidSortalClass):

    def __init__(self):
        
    def relator(self) -> str:
        # TODO: Implement relator method
        pass

    def mediation(self) -> str:
        # TODO: Implement mediation method
        pass

class RefOntoUML_Phase(AntiRigidSortalClass):

    pass
class SubstanceSortal:

    pass
class RefOntoUML_Quantity(SubstanceSortal):

    pass
class RefOntoUML_Collective(SubstanceSortal):

    def __init__(self, isExtensional: bool):
        self.isExtensional = isExtensional
        
    @property
    def isExtensional(self) -> bool:
        return self.__isExtensional

    @isExtensional.setter
    def isExtensional(self, isExtensional: bool):
        self.__isExtensional = isExtensional

class RefOntoUML_Kind(SubstanceSortal):

    pass
class RigidSortalClass:

    pass
class RefOntoUML_SubKind(RigidSortalClass):

    pass
class RefOntoUML_SubstanceSortal(RigidSortalClass):

    pass
class NonRigidMixinClass:

    pass
class RefOntoUML_SemiRigidMixinClass(NonRigidMixinClass):

    pass
class RefOntoUML_AntiRigidMixinClass(NonRigidMixinClass):

    pass
class RigidMixinClass:

    pass
class RefOntoUML_Category(RigidMixinClass):

    pass
class MixinClass:

    pass
class RefOntoUML_NonRigidMixinClass(MixinClass):

    pass
class RefOntoUML_RigidMixinClass(MixinClass):

    pass
class ObjectClass:

    pass
class RefOntoUML_SortalClass(ObjectClass):

    pass
class Class:

    pass
class RefOntoUML_MomentClass(Class):

    pass
class RefOntoUML_ObjectClass(Class):

    pass
class SortalClass:

    pass
class RefOntoUML_AntiRigidSortalClass(SortalClass):

    def __init__(self):
        
    def rigidParent(self) -> str:
        # TODO: Implement rigidParent method
        pass

class RefOntoUML_RigidSortalClass(SortalClass):

    pass
class RefOntoUML_MixinClass(ObjectClass):

    pass
class LiteralSpecification:

    pass
class RefOntoUML_LiteralBoolean(LiteralSpecification):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class RefOntoUML_LiteralUnlimitedNatural(LiteralSpecification):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class RefOntoUML_LiteralNull(LiteralSpecification):

    pass
class RefOntoUML_LiteralInteger(LiteralSpecification):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class RefOntoUML_LiteralString(LiteralSpecification):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class DataType:

    pass
class RefOntoUML_PrimitiveType(DataType):

    pass
class RefOntoUML_Enumeration(DataType):

    pass
class InstanceSpecification:

    pass
class RefOntoUML_EnumerationLiteral(InstanceSpecification):

    pass
class Expression:

    pass
class MultiplicityElement:

    pass
class Feature:

    pass
class Package:

    pass
class RefOntoUML_Model(Package):

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
class RefOntoUML_InstanceValue(ValueSpecification):

    pass
class RefOntoUML_LiteralSpecification(ValueSpecification):

    pass
class RefOntoUML_Expression(ValueSpecification):

    def __init__(self, symbol: str, RefOntoUML_Expression: set["RefOntoUML_ValueSpecification"] = None):
        self.symbol = symbol
        self.RefOntoUML_Expression = RefOntoUML_Expression if RefOntoUML_Expression is not None else set()
        
    @property
    def symbol(self) -> str:
        return self.__symbol

    @symbol.setter
    def symbol(self, symbol: str):
        self.__symbol = symbol

    @property
    def RefOntoUML_Expression(self):
        return self.__RefOntoUML_Expression

    @RefOntoUML_Expression.setter
    def RefOntoUML_Expression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_Expression__RefOntoUML_Expression", None)
        self.__RefOntoUML_Expression = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RefOntoUML_ValueSpecification134"):
                    opp_val = getattr(item, "RefOntoUML_ValueSpecification134", None)
                    
                    if opp_val == self:
                        setattr(item, "RefOntoUML_ValueSpecification134", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RefOntoUML_ValueSpecification134"):
                    opp_val = getattr(item, "RefOntoUML_ValueSpecification134", None)
                    
                    setattr(item, "RefOntoUML_ValueSpecification134", self)
                    

class RefOntoUML_OpaqueExpression(ValueSpecification):

    def __init__(self, body: str, language: str):
        self.body = body
        self.language = language
        
    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

    @property
    def language(self) -> str:
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language

    def isPositive(self) -> str:
        # TODO: Implement isPositive method
        pass

    def isNonNegative(self) -> str:
        # TODO: Implement isNonNegative method
        pass

    def language_body_size(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement language_body_size method
        pass

    def only_return_result_parameters(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement only_return_result_parameters method
        pass

    def getResult(self):
        # TODO: Implement getResult method
        pass

    def value(self) -> str:
        # TODO: Implement value method
        pass

    def isIntegral(self) -> str:
        # TODO: Implement isIntegral method
        pass

    def one_return_result_parameter(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement one_return_result_parameter method
        pass

class Type:

    pass
class RedefinableElement:

    pass
class RefOntoUML_Feature(RedefinableElement):

    def __init__(self, isStatic: str, Feature: "RefOntoUML_Classifier" = None, feature: set["RefOntoUML_Classifier"] = None):
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
    def Feature(self):
        return self.__Feature

    @Feature.setter
    def Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_Feature__Feature", None)
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
        old_value = getattr(self, f"_RefOntoUML_Feature__feature", None)
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
                    

class RefOntoUML_Property(StructuralFeature):

    def __init__(self, isDerived: str, isDerivedUnion: str, default: str, aggregation: str, isComposite: str, Property: "RefOntoUML_Association" = None, Property60: "RefOntoUML_Association" = None, RefOntoUML_Property: "RefOntoUML_Association" = None, RefOntoUML_Property78: "RefOntoUML_Classifier" = None, RefOntoUML_Property109: "RefOntoUML_ValueSpecification" = None, RefOntoUML_Property113: "RefOntoUML_Property" = None, RefOntoUML_Property111: "RefOntoUML_Property" = None, RefOntoUML_Property116: "RefOntoUML_Property" = None, RefOntoUML_Property114: set["RefOntoUML_Property"] = None, ownedAttribute: "RefOntoUML_Class" = None, ownedAttribute103: "RefOntoUML_DataType" = None, RefOntoUML_Property106: "RefOntoUML_Property" = None, RefOntoUML_Property104: set["RefOntoUML_Property"] = None, ownedEnd: "RefOntoUML_Association" = None, memberEnd: "RefOntoUML_Association" = None, Property125: "RefOntoUML_Class" = None, Property127: "RefOntoUML_DataType" = None):
        self.isDerived = isDerived
        self.isDerivedUnion = isDerivedUnion
        self.default = default
        self.aggregation = aggregation
        self.isComposite = isComposite
        self.Property = Property
        self.Property60 = Property60
        self.RefOntoUML_Property = RefOntoUML_Property
        self.RefOntoUML_Property78 = RefOntoUML_Property78
        self.RefOntoUML_Property109 = RefOntoUML_Property109
        self.RefOntoUML_Property113 = RefOntoUML_Property113
        self.RefOntoUML_Property111 = RefOntoUML_Property111
        self.RefOntoUML_Property116 = RefOntoUML_Property116
        self.RefOntoUML_Property114 = RefOntoUML_Property114 if RefOntoUML_Property114 is not None else set()
        self.ownedAttribute = ownedAttribute
        self.ownedAttribute103 = ownedAttribute103
        self.RefOntoUML_Property106 = RefOntoUML_Property106
        self.RefOntoUML_Property104 = RefOntoUML_Property104 if RefOntoUML_Property104 is not None else set()
        self.ownedEnd = ownedEnd
        self.memberEnd = memberEnd
        self.Property125 = Property125
        self.Property127 = Property127
        
    @property
    def isComposite(self) -> str:
        return self.__isComposite

    @isComposite.setter
    def isComposite(self, isComposite: str):
        self.__isComposite = isComposite

    @property
    def isDerivedUnion(self) -> str:
        return self.__isDerivedUnion

    @isDerivedUnion.setter
    def isDerivedUnion(self, isDerivedUnion: str):
        self.__isDerivedUnion = isDerivedUnion

    @property
    def default(self) -> str:
        return self.__default

    @default.setter
    def default(self, default: str):
        self.__default = default

    @property
    def isDerived(self) -> str:
        return self.__isDerived

    @isDerived.setter
    def isDerived(self, isDerived: str):
        self.__isDerived = isDerived

    @property
    def aggregation(self) -> str:
        return self.__aggregation

    @aggregation.setter
    def aggregation(self, aggregation: str):
        self.__aggregation = aggregation

    @property
    def memberEnd(self):
        return self.__memberEnd

    @memberEnd.setter
    def memberEnd(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_Property__memberEnd", None)
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
    def RefOntoUML_Property111(self):
        return self.__RefOntoUML_Property111

    @RefOntoUML_Property111.setter
    def RefOntoUML_Property111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_Property__RefOntoUML_Property111", None)
        self.__RefOntoUML_Property111 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefOntoUML_Property113"):
                opp_val = getattr(old_value, "RefOntoUML_Property113", None)
                if opp_val == self:
                    setattr(old_value, "RefOntoUML_Property113", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefOntoUML_Property113"):
                opp_val = getattr(value, "RefOntoUML_Property113", None)
                setattr(value, "RefOntoUML_Property113", self)

    @property
    def ownedEnd(self):
        return self.__ownedEnd

    @ownedEnd.setter
    def ownedEnd(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_Property__ownedEnd", None)
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
    def Property127(self):
        return self.__Property127

    @Property127.setter
    def Property127(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_Property__Property127", None)
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
    def RefOntoUML_Property106(self):
        return self.__RefOntoUML_Property106

    @RefOntoUML_Property106.setter
    def RefOntoUML_Property106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_Property__RefOntoUML_Property106", None)
        self.__RefOntoUML_Property106 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefOntoUML_Property104"):
                opp_val = getattr(old_value, "RefOntoUML_Property104", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefOntoUML_Property104"):
                opp_val = getattr(value, "RefOntoUML_Property104", None)
                if opp_val is None:
                    setattr(value, "RefOntoUML_Property104", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def RefOntoUML_Property78(self):
        return self.__RefOntoUML_Property78

    @RefOntoUML_Property78.setter
    def RefOntoUML_Property78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_Property__RefOntoUML_Property78", None)
        self.__RefOntoUML_Property78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefOntoUML_Classifier77"):
                opp_val = getattr(old_value, "RefOntoUML_Classifier77", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefOntoUML_Classifier77"):
                opp_val = getattr(value, "RefOntoUML_Classifier77", None)
                if opp_val is None:
                    setattr(value, "RefOntoUML_Classifier77", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Property60(self):
        return self.__Property60

    @Property60.setter
    def Property60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_Property__Property60", None)
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
    def Property125(self):
        return self.__Property125

    @Property125.setter
    def Property125(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_Property__Property125", None)
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

    @property
    def ownedAttribute103(self):
        return self.__ownedAttribute103

    @ownedAttribute103.setter
    def ownedAttribute103(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_Property__ownedAttribute103", None)
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
    def Property(self):
        return self.__Property

    @Property.setter
    def Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_Property__Property", None)
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
    def RefOntoUML_Property114(self):
        return self.__RefOntoUML_Property114

    @RefOntoUML_Property114.setter
    def RefOntoUML_Property114(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_Property__RefOntoUML_Property114", None)
        self.__RefOntoUML_Property114 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RefOntoUML_Property116"):
                    opp_val = getattr(item, "RefOntoUML_Property116", None)
                    
                    if opp_val == self:
                        setattr(item, "RefOntoUML_Property116", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RefOntoUML_Property116"):
                    opp_val = getattr(item, "RefOntoUML_Property116", None)
                    
                    setattr(item, "RefOntoUML_Property116", self)
                    

    @property
    def ownedAttribute(self):
        return self.__ownedAttribute

    @ownedAttribute.setter
    def ownedAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_Property__ownedAttribute", None)
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
    def RefOntoUML_Property109(self):
        return self.__RefOntoUML_Property109

    @RefOntoUML_Property109.setter
    def RefOntoUML_Property109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_Property__RefOntoUML_Property109", None)
        self.__RefOntoUML_Property109 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefOntoUML_ValueSpecification110"):
                opp_val = getattr(old_value, "RefOntoUML_ValueSpecification110", None)
                if opp_val == self:
                    setattr(old_value, "RefOntoUML_ValueSpecification110", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefOntoUML_ValueSpecification110"):
                opp_val = getattr(value, "RefOntoUML_ValueSpecification110", None)
                setattr(value, "RefOntoUML_ValueSpecification110", self)

    @property
    def RefOntoUML_Property116(self):
        return self.__RefOntoUML_Property116

    @RefOntoUML_Property116.setter
    def RefOntoUML_Property116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_Property__RefOntoUML_Property116", None)
        self.__RefOntoUML_Property116 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefOntoUML_Property114"):
                opp_val = getattr(old_value, "RefOntoUML_Property114", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefOntoUML_Property114"):
                opp_val = getattr(value, "RefOntoUML_Property114", None)
                if opp_val is None:
                    setattr(value, "RefOntoUML_Property114", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def RefOntoUML_Property(self):
        return self.__RefOntoUML_Property

    @RefOntoUML_Property.setter
    def RefOntoUML_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_Property__RefOntoUML_Property", None)
        self.__RefOntoUML_Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefOntoUML_Association64"):
                opp_val = getattr(old_value, "RefOntoUML_Association64", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefOntoUML_Association64"):
                opp_val = getattr(value, "RefOntoUML_Association64", None)
                if opp_val is None:
                    setattr(value, "RefOntoUML_Association64", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def RefOntoUML_Property113(self):
        return self.__RefOntoUML_Property113

    @RefOntoUML_Property113.setter
    def RefOntoUML_Property113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_Property__RefOntoUML_Property113", None)
        self.__RefOntoUML_Property113 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefOntoUML_Property111"):
                opp_val = getattr(old_value, "RefOntoUML_Property111", None)
                if opp_val == self:
                    setattr(old_value, "RefOntoUML_Property111", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefOntoUML_Property111"):
                opp_val = getattr(value, "RefOntoUML_Property111", None)
                setattr(value, "RefOntoUML_Property111", self)

    @property
    def RefOntoUML_Property104(self):
        return self.__RefOntoUML_Property104

    @RefOntoUML_Property104.setter
    def RefOntoUML_Property104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_Property__RefOntoUML_Property104", None)
        self.__RefOntoUML_Property104 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RefOntoUML_Property106"):
                    opp_val = getattr(item, "RefOntoUML_Property106", None)
                    
                    if opp_val == self:
                        setattr(item, "RefOntoUML_Property106", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RefOntoUML_Property106"):
                    opp_val = getattr(item, "RefOntoUML_Property106", None)
                    
                    setattr(item, "RefOntoUML_Property106", self)
                    

    def setBooleanDefaultValue(self, value: str):
        # TODO: Implement setBooleanDefaultValue method
        pass

    def subsetting_context_conforms(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement subsetting_context_conforms method
        pass

    def setStringDefaultValue(self, value: str):
        # TODO: Implement setStringDefaultValue method
        pass

    def setIsComposite(self, newIsComposite: str):
        # TODO: Implement setIsComposite method
        pass

    def redefined_property_inherited(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement redefined_property_inherited method
        pass

    def isAttribute(self, p: str) -> str:
        # TODO: Implement isAttribute method
        pass

    def setOpposite(self, newOpposite: str):
        # TODO: Implement setOpposite method
        pass

    def getOtherEnd(self) -> str:
        # TODO: Implement getOtherEnd method
        pass

    def unsetDefault(self):
        # TODO: Implement unsetDefault method
        pass

    def setIsNavigable(self, isNavigable: str):
        # TODO: Implement setIsNavigable method
        pass

    def binding_to_attribute(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement binding_to_attribute method
        pass

    def subsetting_rules(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement subsetting_rules method
        pass

    def isSetDefault(self) -> str:
        # TODO: Implement isSetDefault method
        pass

    def derived_union_is_read_only(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement derived_union_is_read_only method
        pass

    def setNullDefaultValue(self):
        # TODO: Implement setNullDefaultValue method
        pass

    def getOpposite(self) -> str:
        # TODO: Implement getOpposite method
        pass

    def derived_union_is_derived(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement derived_union_is_derived method
        pass

    def isNavigable(self) -> str:
        # TODO: Implement isNavigable method
        pass

    def setUnlimitedNaturalDefaultValue(self, value: str):
        # TODO: Implement setUnlimitedNaturalDefaultValue method
        pass

    def subsettingContext(self) -> Type:
        # TODO: Implement subsettingContext method
        pass

    def subsetted_property_names(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement subsetted_property_names method
        pass

    def setIntegerDefaultValue(self, value: str):
        # TODO: Implement setIntegerDefaultValue method
        pass

    def deployment_target(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement deployment_target method
        pass

    def isComposite(self) -> str:
        # TODO: Implement isComposite method
        pass

    def getDefault(self) -> str:
        # TODO: Implement getDefault method
        pass

    def setDefault(self, newDefault: str):
        # TODO: Implement setDefault method
        pass

    def multiplicity_of_composite(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement multiplicity_of_composite method
        pass

    def navigable_readonly(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement navigable_readonly method
        pass

class Classifier:

    pass
class RefOntoUML_DataType(Classifier):

    def __init__(self, DataType: "RefOntoUML_Property" = None, datatype: set["RefOntoUML_Property"] = None):
        self.DataType = DataType
        self.datatype = datatype if datatype is not None else set()
        
    @property
    def DataType(self):
        return self.__DataType

    @DataType.setter
    def DataType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_DataType__DataType", None)
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
        old_value = getattr(self, f"_RefOntoUML_DataType__datatype", None)
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
                    

    def createOwnedOperation(self, parameterTypes: Type, name: str, parameterNames: str, returnType: Type):
        # TODO: Implement createOwnedOperation method
        pass

    def createOwnedAttribute(self, upper: str, name: str, lower: str, type: Type) -> str:
        # TODO: Implement createOwnedAttribute method
        pass

class RefOntoUML_Class(Classifier):

    def __init__(self, isActive: str, Class: "RefOntoUML_Property" = None, RefOntoUML_Class: set["RefOntoUML_Classifier"] = None, RefOntoUML_Class123: "RefOntoUML_Class" = None, RefOntoUML_Class121: set["RefOntoUML_Class"] = None, class: set["RefOntoUML_Property"] = None):
        self.isActive = isActive
        self.Class = Class
        self.RefOntoUML_Class = RefOntoUML_Class if RefOntoUML_Class is not None else set()
        self.RefOntoUML_Class123 = RefOntoUML_Class123
        self.RefOntoUML_Class121 = RefOntoUML_Class121 if RefOntoUML_Class121 is not None else set()
        self.class = class if class is not None else set()
        
    @property
    def isActive(self) -> str:
        return self.__isActive

    @isActive.setter
    def isActive(self, isActive: str):
        self.__isActive = isActive

    @property
    def RefOntoUML_Class121(self):
        return self.__RefOntoUML_Class121

    @RefOntoUML_Class121.setter
    def RefOntoUML_Class121(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_Class__RefOntoUML_Class121", None)
        self.__RefOntoUML_Class121 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RefOntoUML_Class123"):
                    opp_val = getattr(item, "RefOntoUML_Class123", None)
                    
                    if opp_val == self:
                        setattr(item, "RefOntoUML_Class123", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RefOntoUML_Class123"):
                    opp_val = getattr(item, "RefOntoUML_Class123", None)
                    
                    setattr(item, "RefOntoUML_Class123", self)
                    

    @property
    def Class(self):
        return self.__Class

    @Class.setter
    def Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_Class__Class", None)
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

    @property
    def RefOntoUML_Class123(self):
        return self.__RefOntoUML_Class123

    @RefOntoUML_Class123.setter
    def RefOntoUML_Class123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_Class__RefOntoUML_Class123", None)
        self.__RefOntoUML_Class123 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefOntoUML_Class121"):
                opp_val = getattr(old_value, "RefOntoUML_Class121", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefOntoUML_Class121"):
                opp_val = getattr(value, "RefOntoUML_Class121", None)
                if opp_val is None:
                    setattr(value, "RefOntoUML_Class121", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def class(self):
        return self.__class

    @class.setter
    def class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_Class__class", None)
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
    def RefOntoUML_Class(self):
        return self.__RefOntoUML_Class

    @RefOntoUML_Class.setter
    def RefOntoUML_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_Class__RefOntoUML_Class", None)
        self.__RefOntoUML_Class = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RefOntoUML_Classifier120"):
                    opp_val = getattr(item, "RefOntoUML_Classifier120", None)
                    
                    if opp_val == self:
                        setattr(item, "RefOntoUML_Classifier120", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RefOntoUML_Classifier120"):
                    opp_val = getattr(item, "RefOntoUML_Classifier120", None)
                    
                    setattr(item, "RefOntoUML_Classifier120", self)
                    

    def createOwnedOperation(self, returnType: Type, parameterTypes: Type, name: str, parameterNames: str):
        # TODO: Implement createOwnedOperation method
        pass

    def passive_class(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement passive_class method
        pass

    def isMetaclass(self) -> str:
        # TODO: Implement isMetaclass method
        pass

class TypedElement:

    pass
class RefOntoUML_StructuralFeature(MultiplicityElement, TypedElement, Feature):

    def __init__(self, isReadOnly: str, RefOntoUML_StructuralFeature: "RefOntoUML_Slot" = None):
        self.isReadOnly = isReadOnly
        self.RefOntoUML_StructuralFeature = RefOntoUML_StructuralFeature
        
    @property
    def isReadOnly(self) -> str:
        return self.__isReadOnly

    @isReadOnly.setter
    def isReadOnly(self, isReadOnly: str):
        self.__isReadOnly = isReadOnly

    @property
    def RefOntoUML_StructuralFeature(self):
        return self.__RefOntoUML_StructuralFeature

    @RefOntoUML_StructuralFeature.setter
    def RefOntoUML_StructuralFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_StructuralFeature__RefOntoUML_StructuralFeature", None)
        self.__RefOntoUML_StructuralFeature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefOntoUML_Slot"):
                opp_val = getattr(old_value, "RefOntoUML_Slot", None)
                if opp_val == self:
                    setattr(old_value, "RefOntoUML_Slot", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefOntoUML_Slot"):
                opp_val = getattr(value, "RefOntoUML_Slot", None)
                setattr(value, "RefOntoUML_Slot", self)

class Relationship:

    pass
class RefOntoUML_Association(Classifier, Relationship):

    def __init__(self, isDerived: str, owningAssociation: set["RefOntoUML_Property"] = None, association: set["RefOntoUML_Property"] = None, RefOntoUML_Association: set["RefOntoUML_Type"] = None, RefOntoUML_Association64: set["RefOntoUML_Property"] = None, Association: "RefOntoUML_Property" = None, Association118: "RefOntoUML_Property" = None):
        self.isDerived = isDerived
        self.owningAssociation = owningAssociation if owningAssociation is not None else set()
        self.association = association if association is not None else set()
        self.RefOntoUML_Association = RefOntoUML_Association if RefOntoUML_Association is not None else set()
        self.RefOntoUML_Association64 = RefOntoUML_Association64 if RefOntoUML_Association64 is not None else set()
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
        old_value = getattr(self, f"_RefOntoUML_Association__Association", None)
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
    def RefOntoUML_Association(self):
        return self.__RefOntoUML_Association

    @RefOntoUML_Association.setter
    def RefOntoUML_Association(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_Association__RefOntoUML_Association", None)
        self.__RefOntoUML_Association = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RefOntoUML_Type62"):
                    opp_val = getattr(item, "RefOntoUML_Type62", None)
                    
                    if opp_val == self:
                        setattr(item, "RefOntoUML_Type62", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RefOntoUML_Type62"):
                    opp_val = getattr(item, "RefOntoUML_Type62", None)
                    
                    setattr(item, "RefOntoUML_Type62", self)
                    

    @property
    def RefOntoUML_Association64(self):
        return self.__RefOntoUML_Association64

    @RefOntoUML_Association64.setter
    def RefOntoUML_Association64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_Association__RefOntoUML_Association64", None)
        self.__RefOntoUML_Association64 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RefOntoUML_Property"):
                    opp_val = getattr(item, "RefOntoUML_Property", None)
                    
                    if opp_val == self:
                        setattr(item, "RefOntoUML_Property", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RefOntoUML_Property"):
                    opp_val = getattr(item, "RefOntoUML_Property", None)
                    
                    setattr(item, "RefOntoUML_Property", self)
                    

    @property
    def Association118(self):
        return self.__Association118

    @Association118.setter
    def Association118(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_Association__Association118", None)
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
    def owningAssociation(self):
        return self.__owningAssociation

    @owningAssociation.setter
    def owningAssociation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_Association__owningAssociation", None)
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
    def association(self):
        return self.__association

    @association.setter
    def association(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_Association__association", None)
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
                    

    def association_ends(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement association_ends method
        pass

    def getEndTypes(self) -> str:
        # TODO: Implement getEndTypes method
        pass

    def specialized_end_types(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement specialized_end_types method
        pass

    def isBinary(self) -> str:
        # TODO: Implement isBinary method
        pass

    def specialized_end_number(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement specialized_end_number method
        pass

    def binary_associations(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement binary_associations method
        pass

class RefOntoUML_DirectedRelationship(Relationship):

    pass
class RefOntoUML_StringExpression(Expression):

    def __init__(self, RefOntoUML_StringExpression: "RefOntoUML_NamedElement" = None, StringExpression: "RefOntoUML_StringExpression" = None, owningExpression: set["RefOntoUML_StringExpression"] = None, StringExpression132: "RefOntoUML_StringExpression" = None, subExpression: "RefOntoUML_StringExpression" = None):
        self.RefOntoUML_StringExpression = RefOntoUML_StringExpression
        self.StringExpression = StringExpression
        self.owningExpression = owningExpression if owningExpression is not None else set()
        self.StringExpression132 = StringExpression132
        self.subExpression = subExpression
        
    @property
    def RefOntoUML_StringExpression(self):
        return self.__RefOntoUML_StringExpression

    @RefOntoUML_StringExpression.setter
    def RefOntoUML_StringExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_StringExpression__RefOntoUML_StringExpression", None)
        self.__RefOntoUML_StringExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefOntoUML_NamedElement"):
                opp_val = getattr(old_value, "RefOntoUML_NamedElement", None)
                if opp_val == self:
                    setattr(old_value, "RefOntoUML_NamedElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefOntoUML_NamedElement"):
                opp_val = getattr(value, "RefOntoUML_NamedElement", None)
                setattr(value, "RefOntoUML_NamedElement", self)

    @property
    def StringExpression132(self):
        return self.__StringExpression132

    @StringExpression132.setter
    def StringExpression132(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_StringExpression__StringExpression132", None)
        self.__StringExpression132 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "subExpression"):
                opp_val = getattr(old_value, "subExpression", None)
                if opp_val == self:
                    setattr(old_value, "subExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "subExpression"):
                opp_val = getattr(value, "subExpression", None)
                setattr(value, "subExpression", self)

    @property
    def StringExpression(self):
        return self.__StringExpression

    @StringExpression.setter
    def StringExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_StringExpression__StringExpression", None)
        self.__StringExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owningExpression"):
                opp_val = getattr(old_value, "owningExpression", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owningExpression"):
                opp_val = getattr(value, "owningExpression", None)
                if opp_val is None:
                    setattr(value, "owningExpression", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def owningExpression(self):
        return self.__owningExpression

    @owningExpression.setter
    def owningExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_StringExpression__owningExpression", None)
        self.__owningExpression = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StringExpression"):
                    opp_val = getattr(item, "StringExpression", None)
                    
                    if opp_val == self:
                        setattr(item, "StringExpression", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StringExpression"):
                    opp_val = getattr(item, "StringExpression", None)
                    
                    setattr(item, "StringExpression", self)
                    

    @property
    def subExpression(self):
        return self.__subExpression

    @subExpression.setter
    def subExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_StringExpression__subExpression", None)
        self.__subExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StringExpression132"):
                opp_val = getattr(old_value, "StringExpression132", None)
                if opp_val == self:
                    setattr(old_value, "StringExpression132", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StringExpression132"):
                opp_val = getattr(value, "StringExpression132", None)
                setattr(value, "StringExpression132", self)

    def operands(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement operands method
        pass

    def subexpressions(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement subexpressions method
        pass

class DirectedRelationship:

    pass
class RefOntoUML_ElementImport(DirectedRelationship):

    def __init__(self, alias: str, visibility: str, ElementImport: "RefOntoUML_Namespace" = None, RefOntoUML_ElementImport: "RefOntoUML_PackageableElement" = None, elementImport: "RefOntoUML_Namespace" = None):
        self.alias = alias
        self.visibility = visibility
        self.ElementImport = ElementImport
        self.RefOntoUML_ElementImport = RefOntoUML_ElementImport
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
        old_value = getattr(self, f"_RefOntoUML_ElementImport__ElementImport", None)
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
        old_value = getattr(self, f"_RefOntoUML_ElementImport__elementImport", None)
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

    @property
    def RefOntoUML_ElementImport(self):
        return self.__RefOntoUML_ElementImport

    @RefOntoUML_ElementImport.setter
    def RefOntoUML_ElementImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_ElementImport__RefOntoUML_ElementImport", None)
        self.__RefOntoUML_ElementImport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefOntoUML_PackageableElement42"):
                opp_val = getattr(old_value, "RefOntoUML_PackageableElement42", None)
                if opp_val == self:
                    setattr(old_value, "RefOntoUML_PackageableElement42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefOntoUML_PackageableElement42"):
                opp_val = getattr(value, "RefOntoUML_PackageableElement42", None)
                setattr(value, "RefOntoUML_PackageableElement42", self)

    def visibility_public_or_private(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement visibility_public_or_private method
        pass

    def getName(self) -> str:
        # TODO: Implement getName method
        pass

    def imported_element_is_public(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement imported_element_is_public method
        pass

class RefOntoUML_Generalization(DirectedRelationship):

    def __init__(self, isSubstitutable: str, Generalization: "RefOntoUML_Classifier" = None, RefOntoUML_Generalization: "RefOntoUML_Classifier" = None, generalization: set["RefOntoUML_GeneralizationSet"] = None, generalization89: "RefOntoUML_Classifier" = None, Generalization93: "RefOntoUML_GeneralizationSet" = None):
        self.isSubstitutable = isSubstitutable
        self.Generalization = Generalization
        self.RefOntoUML_Generalization = RefOntoUML_Generalization
        self.generalization = generalization if generalization is not None else set()
        self.generalization89 = generalization89
        self.Generalization93 = Generalization93
        
    @property
    def isSubstitutable(self) -> str:
        return self.__isSubstitutable

    @isSubstitutable.setter
    def isSubstitutable(self, isSubstitutable: str):
        self.__isSubstitutable = isSubstitutable

    @property
    def generalization89(self):
        return self.__generalization89

    @generalization89.setter
    def generalization89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_Generalization__generalization89", None)
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
        old_value = getattr(self, f"_RefOntoUML_Generalization__generalization", None)
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
                    

    @property
    def RefOntoUML_Generalization(self):
        return self.__RefOntoUML_Generalization

    @RefOntoUML_Generalization.setter
    def RefOntoUML_Generalization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_Generalization__RefOntoUML_Generalization", None)
        self.__RefOntoUML_Generalization = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefOntoUML_Classifier85"):
                opp_val = getattr(old_value, "RefOntoUML_Classifier85", None)
                if opp_val == self:
                    setattr(old_value, "RefOntoUML_Classifier85", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefOntoUML_Classifier85"):
                opp_val = getattr(value, "RefOntoUML_Classifier85", None)
                setattr(value, "RefOntoUML_Classifier85", self)

    @property
    def Generalization93(self):
        return self.__Generalization93

    @Generalization93.setter
    def Generalization93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_Generalization__Generalization93", None)
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
    def Generalization(self):
        return self.__Generalization

    @Generalization.setter
    def Generalization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_Generalization__Generalization", None)
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

    def generalization_same_classifier(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement generalization_same_classifier method
        pass

class RefOntoUML_PackageImport(DirectedRelationship):

    def __init__(self, visibility: str, PackageImport: "RefOntoUML_Namespace" = None, RefOntoUML_PackageImport: "RefOntoUML_Package" = None, packageImport: "RefOntoUML_Namespace" = None):
        self.visibility = visibility
        self.PackageImport = PackageImport
        self.RefOntoUML_PackageImport = RefOntoUML_PackageImport
        self.packageImport = packageImport
        
    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def RefOntoUML_PackageImport(self):
        return self.__RefOntoUML_PackageImport

    @RefOntoUML_PackageImport.setter
    def RefOntoUML_PackageImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_PackageImport__RefOntoUML_PackageImport", None)
        self.__RefOntoUML_PackageImport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefOntoUML_Package46"):
                opp_val = getattr(old_value, "RefOntoUML_Package46", None)
                if opp_val == self:
                    setattr(old_value, "RefOntoUML_Package46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefOntoUML_Package46"):
                opp_val = getattr(value, "RefOntoUML_Package46", None)
                setattr(value, "RefOntoUML_Package46", self)

    @property
    def PackageImport(self):
        return self.__PackageImport

    @PackageImport.setter
    def PackageImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_PackageImport__PackageImport", None)
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

    @property
    def packageImport(self):
        return self.__packageImport

    @packageImport.setter
    def packageImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_PackageImport__packageImport", None)
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

    def public_or_private(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement public_or_private method
        pass

class RefOntoUML_PackageMerge(DirectedRelationship):

    pass
class NamedElement:

    pass
class RefOntoUML_TypedElement(NamedElement):

    pass
class RefOntoUML_Namespace(NamedElement):

    def __init__(self, Namespace: "RefOntoUML_NamedElement" = None, importingNamespace32: set["RefOntoUML_PackageImport"] = None, context: set["RefOntoUML_Constraintx"] = None, RefOntoUML_Namespace: set["RefOntoUML_NamedElement"] = None, RefOntoUML_Namespace37: set["RefOntoUML_PackageableElement"] = None, importingNamespace: set["RefOntoUML_ElementImport"] = None, Namespace44: "RefOntoUML_ElementImport" = None, namespace: set["RefOntoUML_NamedElement"] = None, Namespace48: "RefOntoUML_PackageImport" = None, Namespace54: "RefOntoUML_Constraintx" = None):
        self.Namespace = Namespace
        self.importingNamespace32 = importingNamespace32 if importingNamespace32 is not None else set()
        self.context = context if context is not None else set()
        self.RefOntoUML_Namespace = RefOntoUML_Namespace if RefOntoUML_Namespace is not None else set()
        self.RefOntoUML_Namespace37 = RefOntoUML_Namespace37 if RefOntoUML_Namespace37 is not None else set()
        self.importingNamespace = importingNamespace if importingNamespace is not None else set()
        self.Namespace44 = Namespace44
        self.namespace = namespace if namespace is not None else set()
        self.Namespace48 = Namespace48
        self.Namespace54 = Namespace54
        
    @property
    def Namespace54(self):
        return self.__Namespace54

    @Namespace54.setter
    def Namespace54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_Namespace__Namespace54", None)
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

    @property
    def context(self):
        return self.__context

    @context.setter
    def context(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_Namespace__context", None)
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
    def Namespace(self):
        return self.__Namespace

    @Namespace.setter
    def Namespace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_Namespace__Namespace", None)
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
    def importingNamespace32(self):
        return self.__importingNamespace32

    @importingNamespace32.setter
    def importingNamespace32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_Namespace__importingNamespace32", None)
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
    def Namespace44(self):
        return self.__Namespace44

    @Namespace44.setter
    def Namespace44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_Namespace__Namespace44", None)
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
    def namespace(self):
        return self.__namespace

    @namespace.setter
    def namespace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_Namespace__namespace", None)
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
    def Namespace48(self):
        return self.__Namespace48

    @Namespace48.setter
    def Namespace48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_Namespace__Namespace48", None)
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
    def RefOntoUML_Namespace37(self):
        return self.__RefOntoUML_Namespace37

    @RefOntoUML_Namespace37.setter
    def RefOntoUML_Namespace37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_Namespace__RefOntoUML_Namespace37", None)
        self.__RefOntoUML_Namespace37 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RefOntoUML_PackageableElement38"):
                    opp_val = getattr(item, "RefOntoUML_PackageableElement38", None)
                    
                    if opp_val == self:
                        setattr(item, "RefOntoUML_PackageableElement38", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RefOntoUML_PackageableElement38"):
                    opp_val = getattr(item, "RefOntoUML_PackageableElement38", None)
                    
                    setattr(item, "RefOntoUML_PackageableElement38", self)
                    

    @property
    def importingNamespace(self):
        return self.__importingNamespace

    @importingNamespace.setter
    def importingNamespace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_Namespace__importingNamespace", None)
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
    def RefOntoUML_Namespace(self):
        return self.__RefOntoUML_Namespace

    @RefOntoUML_Namespace.setter
    def RefOntoUML_Namespace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_Namespace__RefOntoUML_Namespace", None)
        self.__RefOntoUML_Namespace = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RefOntoUML_NamedElement35"):
                    opp_val = getattr(item, "RefOntoUML_NamedElement35", None)
                    
                    if opp_val == self:
                        setattr(item, "RefOntoUML_NamedElement35", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RefOntoUML_NamedElement35"):
                    opp_val = getattr(item, "RefOntoUML_NamedElement35", None)
                    
                    setattr(item, "RefOntoUML_NamedElement35", self)
                    

    def getImportedElements(self) -> PackageableElement:
        # TODO: Implement getImportedElements method
        pass

    def getImportedPackages(self) -> str:
        # TODO: Implement getImportedPackages method
        pass

    def getImportedMembers(self) -> PackageableElement:
        # TODO: Implement getImportedMembers method
        pass

    def importMembers(self, imps: PackageableElement) -> PackageableElement:
        # TODO: Implement importMembers method
        pass

    def excludeCollisions(self, imps: PackageableElement) -> PackageableElement:
        # TODO: Implement excludeCollisions method
        pass

    def members_distinguishable(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement members_distinguishable method
        pass

    def membersAreDistinguishable(self) -> str:
        # TODO: Implement membersAreDistinguishable method
        pass

    def createElementImport(self, element: PackageableElement, visibility: str) -> str:
        # TODO: Implement createElementImport method
        pass

    def getNamesOfMember(self, element: NamedElement) -> str:
        # TODO: Implement getNamesOfMember method
        pass

    def createPackageImport(self, package_: str, visibility: str) -> str:
        # TODO: Implement createPackageImport method
        pass

class RefOntoUML_PackageableElement(NamedElement):

    pass
class RefOntoUML_RedefinableElement(NamedElement):

    def __init__(self, isLeaf: str, RefOntoUML_RedefinableElement: "RefOntoUML_RedefinableElement" = None, RefOntoUML_RedefinableElement79: set["RefOntoUML_RedefinableElement"] = None, RefOntoUML_RedefinableElement82: set["RefOntoUML_Classifier"] = None):
        self.isLeaf = isLeaf
        self.RefOntoUML_RedefinableElement = RefOntoUML_RedefinableElement
        self.RefOntoUML_RedefinableElement79 = RefOntoUML_RedefinableElement79 if RefOntoUML_RedefinableElement79 is not None else set()
        self.RefOntoUML_RedefinableElement82 = RefOntoUML_RedefinableElement82 if RefOntoUML_RedefinableElement82 is not None else set()
        
    @property
    def isLeaf(self) -> str:
        return self.__isLeaf

    @isLeaf.setter
    def isLeaf(self, isLeaf: str):
        self.__isLeaf = isLeaf

    @property
    def RefOntoUML_RedefinableElement79(self):
        return self.__RefOntoUML_RedefinableElement79

    @RefOntoUML_RedefinableElement79.setter
    def RefOntoUML_RedefinableElement79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_RedefinableElement__RefOntoUML_RedefinableElement79", None)
        self.__RefOntoUML_RedefinableElement79 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RefOntoUML_RedefinableElement"):
                    opp_val = getattr(item, "RefOntoUML_RedefinableElement", None)
                    
                    if opp_val == self:
                        setattr(item, "RefOntoUML_RedefinableElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RefOntoUML_RedefinableElement"):
                    opp_val = getattr(item, "RefOntoUML_RedefinableElement", None)
                    
                    setattr(item, "RefOntoUML_RedefinableElement", self)
                    

    @property
    def RefOntoUML_RedefinableElement82(self):
        return self.__RefOntoUML_RedefinableElement82

    @RefOntoUML_RedefinableElement82.setter
    def RefOntoUML_RedefinableElement82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_RedefinableElement__RefOntoUML_RedefinableElement82", None)
        self.__RefOntoUML_RedefinableElement82 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RefOntoUML_Classifier83"):
                    opp_val = getattr(item, "RefOntoUML_Classifier83", None)
                    
                    if opp_val == self:
                        setattr(item, "RefOntoUML_Classifier83", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RefOntoUML_Classifier83"):
                    opp_val = getattr(item, "RefOntoUML_Classifier83", None)
                    
                    setattr(item, "RefOntoUML_Classifier83", self)
                    

    @property
    def RefOntoUML_RedefinableElement(self):
        return self.__RefOntoUML_RedefinableElement

    @RefOntoUML_RedefinableElement.setter
    def RefOntoUML_RedefinableElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_RedefinableElement__RefOntoUML_RedefinableElement", None)
        self.__RefOntoUML_RedefinableElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefOntoUML_RedefinableElement79"):
                opp_val = getattr(old_value, "RefOntoUML_RedefinableElement79", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefOntoUML_RedefinableElement79"):
                opp_val = getattr(value, "RefOntoUML_RedefinableElement79", None)
                if opp_val is None:
                    setattr(value, "RefOntoUML_RedefinableElement79", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def isConsistentWith(self, redefinee: RedefinableElement) -> str:
        # TODO: Implement isConsistentWith method
        pass

    def redefinition_context_valid(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement redefinition_context_valid method
        pass

    def isRedefinitionContextValid(self, redefined: RedefinableElement) -> str:
        # TODO: Implement isRedefinitionContextValid method
        pass

    def redefinition_consistent(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement redefinition_consistent method
        pass

class PackageableElement:

    pass
class RefOntoUML_Type(PackageableElement):

    def __init__(self, Type: "RefOntoUML_Package" = None, RefOntoUML_Type: "RefOntoUML_TypedElement" = None, ownedType: "RefOntoUML_Package" = None, RefOntoUML_Type62: "RefOntoUML_Association" = None):
        self.Type = Type
        self.RefOntoUML_Type = RefOntoUML_Type
        self.ownedType = ownedType
        self.RefOntoUML_Type62 = RefOntoUML_Type62
        
    @property
    def RefOntoUML_Type(self):
        return self.__RefOntoUML_Type

    @RefOntoUML_Type.setter
    def RefOntoUML_Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_Type__RefOntoUML_Type", None)
        self.__RefOntoUML_Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefOntoUML_TypedElement"):
                opp_val = getattr(old_value, "RefOntoUML_TypedElement", None)
                if opp_val == self:
                    setattr(old_value, "RefOntoUML_TypedElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefOntoUML_TypedElement"):
                opp_val = getattr(value, "RefOntoUML_TypedElement", None)
                setattr(value, "RefOntoUML_TypedElement", self)

    @property
    def RefOntoUML_Type62(self):
        return self.__RefOntoUML_Type62

    @RefOntoUML_Type62.setter
    def RefOntoUML_Type62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_Type__RefOntoUML_Type62", None)
        self.__RefOntoUML_Type62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefOntoUML_Association"):
                opp_val = getattr(old_value, "RefOntoUML_Association", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefOntoUML_Association"):
                opp_val = getattr(value, "RefOntoUML_Association", None)
                if opp_val is None:
                    setattr(value, "RefOntoUML_Association", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Type(self):
        return self.__Type

    @Type.setter
    def Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_Type__Type", None)
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
        old_value = getattr(self, f"_RefOntoUML_Type__ownedType", None)
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

    def conformsTo(self, other: str) -> str:
        # TODO: Implement conformsTo method
        pass

    def getAssociations(self) -> str:
        # TODO: Implement getAssociations method
        pass

    def createAssociation(self, end2Aggregation: str, end1Aggregation: str, end2Lower: str, end1Name: str, end1Lower: str, end2IsNavigable: str, end1Upper: str, end1Type: str, end2Upper: str, end1IsNavigable: str, end2Name: str) -> str:
        # TODO: Implement createAssociation method
        pass

class RefOntoUML_Dependency(DirectedRelationship, PackageableElement):

    pass
class RefOntoUML_Constraintx(PackageableElement):

    def __init__(self, Constraintx: "RefOntoUML_Namespace" = None, RefOntoUML_Constraintx: set["RefOntoUML_Element"] = None, RefOntoUML_Constraintx52: "RefOntoUML_ValueSpecification" = None, ownedRule: "RefOntoUML_Namespace" = None):
        self.Constraintx = Constraintx
        self.RefOntoUML_Constraintx = RefOntoUML_Constraintx if RefOntoUML_Constraintx is not None else set()
        self.RefOntoUML_Constraintx52 = RefOntoUML_Constraintx52
        self.ownedRule = ownedRule
        
    @property
    def ownedRule(self):
        return self.__ownedRule

    @ownedRule.setter
    def ownedRule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_Constraintx__ownedRule", None)
        self.__ownedRule = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Namespace54"):
                opp_val = getattr(old_value, "Namespace54", None)
                if opp_val == self:
                    setattr(old_value, "Namespace54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Namespace54"):
                opp_val = getattr(value, "Namespace54", None)
                setattr(value, "Namespace54", self)

    @property
    def RefOntoUML_Constraintx(self):
        return self.__RefOntoUML_Constraintx

    @RefOntoUML_Constraintx.setter
    def RefOntoUML_Constraintx(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_Constraintx__RefOntoUML_Constraintx", None)
        self.__RefOntoUML_Constraintx = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RefOntoUML_Element50"):
                    opp_val = getattr(item, "RefOntoUML_Element50", None)
                    
                    if opp_val == self:
                        setattr(item, "RefOntoUML_Element50", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RefOntoUML_Element50"):
                    opp_val = getattr(item, "RefOntoUML_Element50", None)
                    
                    setattr(item, "RefOntoUML_Element50", self)
                    

    @property
    def Constraintx(self):
        return self.__Constraintx

    @Constraintx.setter
    def Constraintx(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_Constraintx__Constraintx", None)
        self.__Constraintx = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "context"):
                opp_val = getattr(old_value, "context", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "context"):
                opp_val = getattr(value, "context", None)
                if opp_val is None:
                    setattr(value, "context", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def RefOntoUML_Constraintx52(self):
        return self.__RefOntoUML_Constraintx52

    @RefOntoUML_Constraintx52.setter
    def RefOntoUML_Constraintx52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_Constraintx__RefOntoUML_Constraintx52", None)
        self.__RefOntoUML_Constraintx52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefOntoUML_ValueSpecification"):
                opp_val = getattr(old_value, "RefOntoUML_ValueSpecification", None)
                if opp_val == self:
                    setattr(old_value, "RefOntoUML_ValueSpecification", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefOntoUML_ValueSpecification"):
                opp_val = getattr(value, "RefOntoUML_ValueSpecification", None)
                setattr(value, "RefOntoUML_ValueSpecification", self)

    def value_specification_boolean(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement value_specification_boolean method
        pass

    def not_applied_to_self(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement not_applied_to_self method
        pass

    def boolean_value(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement boolean_value method
        pass

    def no_side_effects(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement no_side_effects method
        pass

    def not_apply_to_self(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement not_apply_to_self method
        pass

class RefOntoUML_InstanceSpecification(PackageableElement):

    def __init__(self, owningInstance: set["RefOntoUML_Slot"] = None, RefOntoUML_InstanceSpecification145: "RefOntoUML_ValueSpecification" = None, RefOntoUML_InstanceSpecification: set["RefOntoUML_Classifier"] = None, InstanceSpecification: "RefOntoUML_Slot" = None, RefOntoUML_InstanceSpecification153: "RefOntoUML_InstanceValue" = None):
        self.owningInstance = owningInstance if owningInstance is not None else set()
        self.RefOntoUML_InstanceSpecification145 = RefOntoUML_InstanceSpecification145
        self.RefOntoUML_InstanceSpecification = RefOntoUML_InstanceSpecification if RefOntoUML_InstanceSpecification is not None else set()
        self.InstanceSpecification = InstanceSpecification
        self.RefOntoUML_InstanceSpecification153 = RefOntoUML_InstanceSpecification153
        
    @property
    def owningInstance(self):
        return self.__owningInstance

    @owningInstance.setter
    def owningInstance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_InstanceSpecification__owningInstance", None)
        self.__owningInstance = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Slot"):
                    opp_val = getattr(item, "Slot", None)
                    
                    if opp_val == self:
                        setattr(item, "Slot", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Slot"):
                    opp_val = getattr(item, "Slot", None)
                    
                    setattr(item, "Slot", self)
                    

    @property
    def InstanceSpecification(self):
        return self.__InstanceSpecification

    @InstanceSpecification.setter
    def InstanceSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_InstanceSpecification__InstanceSpecification", None)
        self.__InstanceSpecification = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "slot"):
                opp_val = getattr(old_value, "slot", None)
                if opp_val == self:
                    setattr(old_value, "slot", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "slot"):
                opp_val = getattr(value, "slot", None)
                setattr(value, "slot", self)

    @property
    def RefOntoUML_InstanceSpecification(self):
        return self.__RefOntoUML_InstanceSpecification

    @RefOntoUML_InstanceSpecification.setter
    def RefOntoUML_InstanceSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_InstanceSpecification__RefOntoUML_InstanceSpecification", None)
        self.__RefOntoUML_InstanceSpecification = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RefOntoUML_Classifier142"):
                    opp_val = getattr(item, "RefOntoUML_Classifier142", None)
                    
                    if opp_val == self:
                        setattr(item, "RefOntoUML_Classifier142", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RefOntoUML_Classifier142"):
                    opp_val = getattr(item, "RefOntoUML_Classifier142", None)
                    
                    setattr(item, "RefOntoUML_Classifier142", self)
                    

    @property
    def RefOntoUML_InstanceSpecification145(self):
        return self.__RefOntoUML_InstanceSpecification145

    @RefOntoUML_InstanceSpecification145.setter
    def RefOntoUML_InstanceSpecification145(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_InstanceSpecification__RefOntoUML_InstanceSpecification145", None)
        self.__RefOntoUML_InstanceSpecification145 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefOntoUML_ValueSpecification146"):
                opp_val = getattr(old_value, "RefOntoUML_ValueSpecification146", None)
                if opp_val == self:
                    setattr(old_value, "RefOntoUML_ValueSpecification146", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefOntoUML_ValueSpecification146"):
                opp_val = getattr(value, "RefOntoUML_ValueSpecification146", None)
                setattr(value, "RefOntoUML_ValueSpecification146", self)

    @property
    def RefOntoUML_InstanceSpecification153(self):
        return self.__RefOntoUML_InstanceSpecification153

    @RefOntoUML_InstanceSpecification153.setter
    def RefOntoUML_InstanceSpecification153(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_InstanceSpecification__RefOntoUML_InstanceSpecification153", None)
        self.__RefOntoUML_InstanceSpecification153 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefOntoUML_InstanceValue"):
                opp_val = getattr(old_value, "RefOntoUML_InstanceValue", None)
                if opp_val == self:
                    setattr(old_value, "RefOntoUML_InstanceValue", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefOntoUML_InstanceValue"):
                opp_val = getattr(value, "RefOntoUML_InstanceValue", None)
                setattr(value, "RefOntoUML_InstanceValue", self)

    def defining_feature(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement defining_feature method
        pass

    def deployment_target(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement deployment_target method
        pass

    def structural_feature(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement structural_feature method
        pass

    def deployment_artifact(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement deployment_artifact method
        pass

class RefOntoUML_GeneralizationSet(PackageableElement):

    def __init__(self, isCovering: str, isDisjoint: str, GeneralizationSet: "RefOntoUML_Classifier" = None, GeneralizationSet87: "RefOntoUML_Generalization" = None, generalizationSet: set["RefOntoUML_Generalization"] = None, powertypeExtent: "RefOntoUML_Classifier" = None):
        self.isCovering = isCovering
        self.isDisjoint = isDisjoint
        self.GeneralizationSet = GeneralizationSet
        self.GeneralizationSet87 = GeneralizationSet87
        self.generalizationSet = generalizationSet if generalizationSet is not None else set()
        self.powertypeExtent = powertypeExtent
        
    @property
    def isCovering(self) -> str:
        return self.__isCovering

    @isCovering.setter
    def isCovering(self, isCovering: str):
        self.__isCovering = isCovering

    @property
    def isDisjoint(self) -> str:
        return self.__isDisjoint

    @isDisjoint.setter
    def isDisjoint(self, isDisjoint: str):
        self.__isDisjoint = isDisjoint

    @property
    def powertypeExtent(self):
        return self.__powertypeExtent

    @powertypeExtent.setter
    def powertypeExtent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_GeneralizationSet__powertypeExtent", None)
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
        old_value = getattr(self, f"_RefOntoUML_GeneralizationSet__generalizationSet", None)
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
                    

    @property
    def GeneralizationSet87(self):
        return self.__GeneralizationSet87

    @GeneralizationSet87.setter
    def GeneralizationSet87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_GeneralizationSet__GeneralizationSet87", None)
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
    def GeneralizationSet(self):
        return self.__GeneralizationSet

    @GeneralizationSet.setter
    def GeneralizationSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_GeneralizationSet__GeneralizationSet", None)
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

    def generalization_same_classifier(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement generalization_same_classifier method
        pass

    def children(self) -> Classifier:
        # TODO: Implement children method
        pass

    def maps_to_generalization_set(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement maps_to_generalization_set method
        pass

    def parent(self) -> Classifier:
        # TODO: Implement parent method
        pass

class RefOntoUML_ValueSpecification(PackageableElement, TypedElement):

    def __init__(self, RefOntoUML_ValueSpecification: "RefOntoUML_Constraintx" = None, RefOntoUML_ValueSpecification97: "RefOntoUML_MultiplicityElement" = None, RefOntoUML_ValueSpecification100: "RefOntoUML_MultiplicityElement" = None, RefOntoUML_ValueSpecification110: "RefOntoUML_Property" = None, RefOntoUML_ValueSpecification134: "RefOntoUML_Expression" = None, RefOntoUML_ValueSpecification146: "RefOntoUML_InstanceSpecification" = None, RefOntoUML_ValueSpecification150: "RefOntoUML_Slot" = None):
        self.RefOntoUML_ValueSpecification = RefOntoUML_ValueSpecification
        self.RefOntoUML_ValueSpecification97 = RefOntoUML_ValueSpecification97
        self.RefOntoUML_ValueSpecification100 = RefOntoUML_ValueSpecification100
        self.RefOntoUML_ValueSpecification110 = RefOntoUML_ValueSpecification110
        self.RefOntoUML_ValueSpecification134 = RefOntoUML_ValueSpecification134
        self.RefOntoUML_ValueSpecification146 = RefOntoUML_ValueSpecification146
        self.RefOntoUML_ValueSpecification150 = RefOntoUML_ValueSpecification150
        
    @property
    def RefOntoUML_ValueSpecification100(self):
        return self.__RefOntoUML_ValueSpecification100

    @RefOntoUML_ValueSpecification100.setter
    def RefOntoUML_ValueSpecification100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_ValueSpecification__RefOntoUML_ValueSpecification100", None)
        self.__RefOntoUML_ValueSpecification100 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefOntoUML_MultiplicityElement99"):
                opp_val = getattr(old_value, "RefOntoUML_MultiplicityElement99", None)
                if opp_val == self:
                    setattr(old_value, "RefOntoUML_MultiplicityElement99", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefOntoUML_MultiplicityElement99"):
                opp_val = getattr(value, "RefOntoUML_MultiplicityElement99", None)
                setattr(value, "RefOntoUML_MultiplicityElement99", self)

    @property
    def RefOntoUML_ValueSpecification110(self):
        return self.__RefOntoUML_ValueSpecification110

    @RefOntoUML_ValueSpecification110.setter
    def RefOntoUML_ValueSpecification110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_ValueSpecification__RefOntoUML_ValueSpecification110", None)
        self.__RefOntoUML_ValueSpecification110 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefOntoUML_Property109"):
                opp_val = getattr(old_value, "RefOntoUML_Property109", None)
                if opp_val == self:
                    setattr(old_value, "RefOntoUML_Property109", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefOntoUML_Property109"):
                opp_val = getattr(value, "RefOntoUML_Property109", None)
                setattr(value, "RefOntoUML_Property109", self)

    @property
    def RefOntoUML_ValueSpecification134(self):
        return self.__RefOntoUML_ValueSpecification134

    @RefOntoUML_ValueSpecification134.setter
    def RefOntoUML_ValueSpecification134(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_ValueSpecification__RefOntoUML_ValueSpecification134", None)
        self.__RefOntoUML_ValueSpecification134 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefOntoUML_Expression"):
                opp_val = getattr(old_value, "RefOntoUML_Expression", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefOntoUML_Expression"):
                opp_val = getattr(value, "RefOntoUML_Expression", None)
                if opp_val is None:
                    setattr(value, "RefOntoUML_Expression", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def RefOntoUML_ValueSpecification146(self):
        return self.__RefOntoUML_ValueSpecification146

    @RefOntoUML_ValueSpecification146.setter
    def RefOntoUML_ValueSpecification146(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_ValueSpecification__RefOntoUML_ValueSpecification146", None)
        self.__RefOntoUML_ValueSpecification146 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefOntoUML_InstanceSpecification145"):
                opp_val = getattr(old_value, "RefOntoUML_InstanceSpecification145", None)
                if opp_val == self:
                    setattr(old_value, "RefOntoUML_InstanceSpecification145", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefOntoUML_InstanceSpecification145"):
                opp_val = getattr(value, "RefOntoUML_InstanceSpecification145", None)
                setattr(value, "RefOntoUML_InstanceSpecification145", self)

    @property
    def RefOntoUML_ValueSpecification97(self):
        return self.__RefOntoUML_ValueSpecification97

    @RefOntoUML_ValueSpecification97.setter
    def RefOntoUML_ValueSpecification97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_ValueSpecification__RefOntoUML_ValueSpecification97", None)
        self.__RefOntoUML_ValueSpecification97 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefOntoUML_MultiplicityElement"):
                opp_val = getattr(old_value, "RefOntoUML_MultiplicityElement", None)
                if opp_val == self:
                    setattr(old_value, "RefOntoUML_MultiplicityElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefOntoUML_MultiplicityElement"):
                opp_val = getattr(value, "RefOntoUML_MultiplicityElement", None)
                setattr(value, "RefOntoUML_MultiplicityElement", self)

    @property
    def RefOntoUML_ValueSpecification150(self):
        return self.__RefOntoUML_ValueSpecification150

    @RefOntoUML_ValueSpecification150.setter
    def RefOntoUML_ValueSpecification150(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_ValueSpecification__RefOntoUML_ValueSpecification150", None)
        self.__RefOntoUML_ValueSpecification150 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefOntoUML_Slot149"):
                opp_val = getattr(old_value, "RefOntoUML_Slot149", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefOntoUML_Slot149"):
                opp_val = getattr(value, "RefOntoUML_Slot149", None)
                if opp_val is None:
                    setattr(value, "RefOntoUML_Slot149", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def RefOntoUML_ValueSpecification(self):
        return self.__RefOntoUML_ValueSpecification

    @RefOntoUML_ValueSpecification.setter
    def RefOntoUML_ValueSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_ValueSpecification__RefOntoUML_ValueSpecification", None)
        self.__RefOntoUML_ValueSpecification = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefOntoUML_Constraintx52"):
                opp_val = getattr(old_value, "RefOntoUML_Constraintx52", None)
                if opp_val == self:
                    setattr(old_value, "RefOntoUML_Constraintx52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefOntoUML_Constraintx52"):
                opp_val = getattr(value, "RefOntoUML_Constraintx52", None)
                setattr(value, "RefOntoUML_Constraintx52", self)

    def unlimitedValue(self) -> str:
        # TODO: Implement unlimitedValue method
        pass

    def booleanValue(self) -> str:
        # TODO: Implement booleanValue method
        pass

    def integerValue(self) -> str:
        # TODO: Implement integerValue method
        pass

    def isComputable(self) -> str:
        # TODO: Implement isComputable method
        pass

    def isNull(self) -> str:
        # TODO: Implement isNull method
        pass

    def stringValue(self) -> str:
        # TODO: Implement stringValue method
        pass

class Namespace:

    pass
class RefOntoUML_Classifier(Type, RedefinableElement, Namespace):

    def __init__(self, isAbstract: str, featuringClassifier: set["RefOntoUML_Feature"] = None, RefOntoUML_Classifier: set["RefOntoUML_NamedElement"] = None, RefOntoUML_Classifier72: "RefOntoUML_Classifier" = None, RefOntoUML_Classifier70: set["RefOntoUML_Classifier"] = None, specific: set["RefOntoUML_Generalization"] = None, powertype: set["RefOntoUML_GeneralizationSet"] = None, RefOntoUML_Classifier75: "RefOntoUML_Classifier" = None, RefOntoUML_Classifier73: set["RefOntoUML_Classifier"] = None, RefOntoUML_Classifier77: set["RefOntoUML_Property"] = None, RefOntoUML_Classifier85: "RefOntoUML_Generalization" = None, Classifier: "RefOntoUML_Generalization" = None, RefOntoUML_Classifier83: "RefOntoUML_RedefinableElement" = None, Classifier91: "RefOntoUML_GeneralizationSet" = None, Classifier95: "RefOntoUML_Feature" = None, RefOntoUML_Classifier120: "RefOntoUML_Class" = None, RefOntoUML_Classifier142: "RefOntoUML_InstanceSpecification" = None):
        self.isAbstract = isAbstract
        self.featuringClassifier = featuringClassifier if featuringClassifier is not None else set()
        self.RefOntoUML_Classifier = RefOntoUML_Classifier if RefOntoUML_Classifier is not None else set()
        self.RefOntoUML_Classifier72 = RefOntoUML_Classifier72
        self.RefOntoUML_Classifier70 = RefOntoUML_Classifier70 if RefOntoUML_Classifier70 is not None else set()
        self.specific = specific if specific is not None else set()
        self.powertype = powertype if powertype is not None else set()
        self.RefOntoUML_Classifier75 = RefOntoUML_Classifier75
        self.RefOntoUML_Classifier73 = RefOntoUML_Classifier73 if RefOntoUML_Classifier73 is not None else set()
        self.RefOntoUML_Classifier77 = RefOntoUML_Classifier77 if RefOntoUML_Classifier77 is not None else set()
        self.RefOntoUML_Classifier85 = RefOntoUML_Classifier85
        self.Classifier = Classifier
        self.RefOntoUML_Classifier83 = RefOntoUML_Classifier83
        self.Classifier91 = Classifier91
        self.Classifier95 = Classifier95
        self.RefOntoUML_Classifier120 = RefOntoUML_Classifier120
        self.RefOntoUML_Classifier142 = RefOntoUML_Classifier142
        
    @property
    def isAbstract(self) -> str:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: str):
        self.__isAbstract = isAbstract

    @property
    def Classifier91(self):
        return self.__Classifier91

    @Classifier91.setter
    def Classifier91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_Classifier__Classifier91", None)
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
    def RefOntoUML_Classifier120(self):
        return self.__RefOntoUML_Classifier120

    @RefOntoUML_Classifier120.setter
    def RefOntoUML_Classifier120(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_Classifier__RefOntoUML_Classifier120", None)
        self.__RefOntoUML_Classifier120 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefOntoUML_Class"):
                opp_val = getattr(old_value, "RefOntoUML_Class", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefOntoUML_Class"):
                opp_val = getattr(value, "RefOntoUML_Class", None)
                if opp_val is None:
                    setattr(value, "RefOntoUML_Class", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def featuringClassifier(self):
        return self.__featuringClassifier

    @featuringClassifier.setter
    def featuringClassifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_Classifier__featuringClassifier", None)
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
    def powertype(self):
        return self.__powertype

    @powertype.setter
    def powertype(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_Classifier__powertype", None)
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
    def RefOntoUML_Classifier83(self):
        return self.__RefOntoUML_Classifier83

    @RefOntoUML_Classifier83.setter
    def RefOntoUML_Classifier83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_Classifier__RefOntoUML_Classifier83", None)
        self.__RefOntoUML_Classifier83 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefOntoUML_RedefinableElement82"):
                opp_val = getattr(old_value, "RefOntoUML_RedefinableElement82", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefOntoUML_RedefinableElement82"):
                opp_val = getattr(value, "RefOntoUML_RedefinableElement82", None)
                if opp_val is None:
                    setattr(value, "RefOntoUML_RedefinableElement82", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def RefOntoUML_Classifier(self):
        return self.__RefOntoUML_Classifier

    @RefOntoUML_Classifier.setter
    def RefOntoUML_Classifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_Classifier__RefOntoUML_Classifier", None)
        self.__RefOntoUML_Classifier = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RefOntoUML_NamedElement69"):
                    opp_val = getattr(item, "RefOntoUML_NamedElement69", None)
                    
                    if opp_val == self:
                        setattr(item, "RefOntoUML_NamedElement69", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RefOntoUML_NamedElement69"):
                    opp_val = getattr(item, "RefOntoUML_NamedElement69", None)
                    
                    setattr(item, "RefOntoUML_NamedElement69", self)
                    

    @property
    def specific(self):
        return self.__specific

    @specific.setter
    def specific(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_Classifier__specific", None)
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
    def RefOntoUML_Classifier77(self):
        return self.__RefOntoUML_Classifier77

    @RefOntoUML_Classifier77.setter
    def RefOntoUML_Classifier77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_Classifier__RefOntoUML_Classifier77", None)
        self.__RefOntoUML_Classifier77 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RefOntoUML_Property78"):
                    opp_val = getattr(item, "RefOntoUML_Property78", None)
                    
                    if opp_val == self:
                        setattr(item, "RefOntoUML_Property78", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RefOntoUML_Property78"):
                    opp_val = getattr(item, "RefOntoUML_Property78", None)
                    
                    setattr(item, "RefOntoUML_Property78", self)
                    

    @property
    def Classifier95(self):
        return self.__Classifier95

    @Classifier95.setter
    def Classifier95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_Classifier__Classifier95", None)
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
    def RefOntoUML_Classifier73(self):
        return self.__RefOntoUML_Classifier73

    @RefOntoUML_Classifier73.setter
    def RefOntoUML_Classifier73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_Classifier__RefOntoUML_Classifier73", None)
        self.__RefOntoUML_Classifier73 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RefOntoUML_Classifier75"):
                    opp_val = getattr(item, "RefOntoUML_Classifier75", None)
                    
                    if opp_val == self:
                        setattr(item, "RefOntoUML_Classifier75", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RefOntoUML_Classifier75"):
                    opp_val = getattr(item, "RefOntoUML_Classifier75", None)
                    
                    setattr(item, "RefOntoUML_Classifier75", self)
                    

    @property
    def RefOntoUML_Classifier75(self):
        return self.__RefOntoUML_Classifier75

    @RefOntoUML_Classifier75.setter
    def RefOntoUML_Classifier75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_Classifier__RefOntoUML_Classifier75", None)
        self.__RefOntoUML_Classifier75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefOntoUML_Classifier73"):
                opp_val = getattr(old_value, "RefOntoUML_Classifier73", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefOntoUML_Classifier73"):
                opp_val = getattr(value, "RefOntoUML_Classifier73", None)
                if opp_val is None:
                    setattr(value, "RefOntoUML_Classifier73", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def RefOntoUML_Classifier85(self):
        return self.__RefOntoUML_Classifier85

    @RefOntoUML_Classifier85.setter
    def RefOntoUML_Classifier85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_Classifier__RefOntoUML_Classifier85", None)
        self.__RefOntoUML_Classifier85 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefOntoUML_Generalization"):
                opp_val = getattr(old_value, "RefOntoUML_Generalization", None)
                if opp_val == self:
                    setattr(old_value, "RefOntoUML_Generalization", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefOntoUML_Generalization"):
                opp_val = getattr(value, "RefOntoUML_Generalization", None)
                setattr(value, "RefOntoUML_Generalization", self)

    @property
    def RefOntoUML_Classifier72(self):
        return self.__RefOntoUML_Classifier72

    @RefOntoUML_Classifier72.setter
    def RefOntoUML_Classifier72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_Classifier__RefOntoUML_Classifier72", None)
        self.__RefOntoUML_Classifier72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefOntoUML_Classifier70"):
                opp_val = getattr(old_value, "RefOntoUML_Classifier70", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefOntoUML_Classifier70"):
                opp_val = getattr(value, "RefOntoUML_Classifier70", None)
                if opp_val is None:
                    setattr(value, "RefOntoUML_Classifier70", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def RefOntoUML_Classifier70(self):
        return self.__RefOntoUML_Classifier70

    @RefOntoUML_Classifier70.setter
    def RefOntoUML_Classifier70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_Classifier__RefOntoUML_Classifier70", None)
        self.__RefOntoUML_Classifier70 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RefOntoUML_Classifier72"):
                    opp_val = getattr(item, "RefOntoUML_Classifier72", None)
                    
                    if opp_val == self:
                        setattr(item, "RefOntoUML_Classifier72", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RefOntoUML_Classifier72"):
                    opp_val = getattr(item, "RefOntoUML_Classifier72", None)
                    
                    setattr(item, "RefOntoUML_Classifier72", self)
                    

    @property
    def RefOntoUML_Classifier142(self):
        return self.__RefOntoUML_Classifier142

    @RefOntoUML_Classifier142.setter
    def RefOntoUML_Classifier142(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_Classifier__RefOntoUML_Classifier142", None)
        self.__RefOntoUML_Classifier142 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefOntoUML_InstanceSpecification"):
                opp_val = getattr(old_value, "RefOntoUML_InstanceSpecification", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefOntoUML_InstanceSpecification"):
                opp_val = getattr(value, "RefOntoUML_InstanceSpecification", None)
                if opp_val is None:
                    setattr(value, "RefOntoUML_InstanceSpecification", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Classifier(self):
        return self.__Classifier

    @Classifier.setter
    def Classifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_Classifier__Classifier", None)
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

    def hasKindOffspring(self) -> bool:
        # TODO: Implement hasKindOffspring method
        pass

    def maps_to_generalization_set(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement maps_to_generalization_set method
        pass

    def maySpecializeType(self, c: Classifier) -> str:
        # TODO: Implement maySpecializeType method
        pass

    def inheritableMembers(self, c: Classifier) -> NamedElement:
        # TODO: Implement inheritableMembers method
        pass

    def hasCollectiveOffspring(self) -> bool:
        # TODO: Implement hasCollectiveOffspring method
        pass

    def children(self) -> Classifier:
        # TODO: Implement children method
        pass

    def hasQuantityInstances(self) -> bool:
        # TODO: Implement hasQuantityInstances method
        pass

    def hasQuantityAncestor(self) -> bool:
        # TODO: Implement hasQuantityAncestor method
        pass

    def conformsTo(self, other: Classifier) -> str:
        # TODO: Implement conformsTo method
        pass

    def specialize_type(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement specialize_type method
        pass

    def allChildren(self) -> Classifier:
        # TODO: Implement allChildren method
        pass

    def generalization_hierarchies(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement generalization_hierarchies method
        pass

    def no_cycles_in_generalization(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement no_cycles_in_generalization method
        pass

    def partitions(self) -> str:
        # TODO: Implement partitions method
        pass

    def hasVisibilityOf(self, n: NamedElement) -> str:
        # TODO: Implement hasVisibilityOf method
        pass

    def allParents(self) -> Classifier:
        # TODO: Implement allParents method
        pass

    def parents(self) -> Classifier:
        # TODO: Implement parents method
        pass

    def hasCollectiveInstances(self) -> bool:
        # TODO: Implement hasCollectiveInstances method
        pass

    def getAllAttributes(self) -> str:
        # TODO: Implement getAllAttributes method
        pass

    def hasFunctionalComplexInstances(self) -> bool:
        # TODO: Implement hasFunctionalComplexInstances method
        pass

    def hasCollectiveAncestor(self) -> bool:
        # TODO: Implement hasCollectiveAncestor method
        pass

    def getInheritedMembers(self) -> NamedElement:
        # TODO: Implement getInheritedMembers method
        pass

    def inherit(self, inhs: NamedElement) -> NamedElement:
        # TODO: Implement inherit method
        pass

    def hasKindAncestor(self) -> bool:
        # TODO: Implement hasKindAncestor method
        pass

    def allFeatures(self) -> str:
        # TODO: Implement allFeatures method
        pass

    def hasQuantityOffspring(self) -> bool:
        # TODO: Implement hasQuantityOffspring method
        pass

    def getGenerals(self) -> Classifier:
        # TODO: Implement getGenerals method
        pass

class RefOntoUML_Package(Namespace, PackageableElement):

    def __init__(self, Package16: "RefOntoUML_Package" = None, nestedPackage: "RefOntoUML_Package" = None, package: set["RefOntoUML_Type"] = None, receivingPackage: set["RefOntoUML_PackageMerge"] = None, RefOntoUML_Package: set["RefOntoUML_PackageableElement"] = None, Package: "RefOntoUML_Package" = None, nestingPackage: set["RefOntoUML_Package"] = None, RefOntoUML_Package46: "RefOntoUML_PackageImport" = None, Package57: "RefOntoUML_Type" = None, RefOntoUML_Package136: "RefOntoUML_PackageMerge" = None, Package138: "RefOntoUML_PackageMerge" = None):
        self.Package16 = Package16
        self.nestedPackage = nestedPackage
        self.package = package if package is not None else set()
        self.receivingPackage = receivingPackage if receivingPackage is not None else set()
        self.RefOntoUML_Package = RefOntoUML_Package if RefOntoUML_Package is not None else set()
        self.Package = Package
        self.nestingPackage = nestingPackage if nestingPackage is not None else set()
        self.RefOntoUML_Package46 = RefOntoUML_Package46
        self.Package57 = Package57
        self.RefOntoUML_Package136 = RefOntoUML_Package136
        self.Package138 = Package138
        
    @property
    def Package16(self):
        return self.__Package16

    @Package16.setter
    def Package16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_Package__Package16", None)
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
    def nestedPackage(self):
        return self.__nestedPackage

    @nestedPackage.setter
    def nestedPackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_Package__nestedPackage", None)
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
    def RefOntoUML_Package136(self):
        return self.__RefOntoUML_Package136

    @RefOntoUML_Package136.setter
    def RefOntoUML_Package136(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_Package__RefOntoUML_Package136", None)
        self.__RefOntoUML_Package136 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefOntoUML_PackageMerge"):
                opp_val = getattr(old_value, "RefOntoUML_PackageMerge", None)
                if opp_val == self:
                    setattr(old_value, "RefOntoUML_PackageMerge", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefOntoUML_PackageMerge"):
                opp_val = getattr(value, "RefOntoUML_PackageMerge", None)
                setattr(value, "RefOntoUML_PackageMerge", self)

    @property
    def nestingPackage(self):
        return self.__nestingPackage

    @nestingPackage.setter
    def nestingPackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_Package__nestingPackage", None)
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
    def Package(self):
        return self.__Package

    @Package.setter
    def Package(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_Package__Package", None)
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

    @property
    def RefOntoUML_Package46(self):
        return self.__RefOntoUML_Package46

    @RefOntoUML_Package46.setter
    def RefOntoUML_Package46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_Package__RefOntoUML_Package46", None)
        self.__RefOntoUML_Package46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefOntoUML_PackageImport"):
                opp_val = getattr(old_value, "RefOntoUML_PackageImport", None)
                if opp_val == self:
                    setattr(old_value, "RefOntoUML_PackageImport", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefOntoUML_PackageImport"):
                opp_val = getattr(value, "RefOntoUML_PackageImport", None)
                setattr(value, "RefOntoUML_PackageImport", self)

    @property
    def Package138(self):
        return self.__Package138

    @Package138.setter
    def Package138(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_Package__Package138", None)
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
    def Package57(self):
        return self.__Package57

    @Package57.setter
    def Package57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_Package__Package57", None)
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
    def RefOntoUML_Package(self):
        return self.__RefOntoUML_Package

    @RefOntoUML_Package.setter
    def RefOntoUML_Package(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_Package__RefOntoUML_Package", None)
        self.__RefOntoUML_Package = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RefOntoUML_PackageableElement"):
                    opp_val = getattr(item, "RefOntoUML_PackageableElement", None)
                    
                    if opp_val == self:
                        setattr(item, "RefOntoUML_PackageableElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RefOntoUML_PackageableElement"):
                    opp_val = getattr(item, "RefOntoUML_PackageableElement", None)
                    
                    setattr(item, "RefOntoUML_PackageableElement", self)
                    

    @property
    def receivingPackage(self):
        return self.__receivingPackage

    @receivingPackage.setter
    def receivingPackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_Package__receivingPackage", None)
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
    def package(self):
        return self.__package

    @package.setter
    def package(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_Package__package", None)
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
                    

    def visibleMembers(self) -> PackageableElement:
        # TODO: Implement visibleMembers method
        pass

    def makesVisible(self, el: str) -> str:
        # TODO: Implement makesVisible method
        pass

    def getAppliedProfile(self, qualifiedName: str):
        # TODO: Implement getAppliedProfile method
        pass

    def createOwnedPrimitiveType(self, name: str) -> str:
        # TODO: Implement createOwnedPrimitiveType method
        pass

    def isModelLibrary(self) -> str:
        # TODO: Implement isModelLibrary method
        pass

    def createOwnedClass(self, name: str, isAbstract: str) -> str:
        # TODO: Implement createOwnedClass method
        pass

    def getAppliedProfile(self, qualifiedName: str, recurse: str):
        # TODO: Implement getAppliedProfile method
        pass

    def elements_public_or_private(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement elements_public_or_private method
        pass

    def createOwnedInterface(self, name: str):
        # TODO: Implement createOwnedInterface method
        pass

    def createOwnedEnumeration(self, name: str) -> str:
        # TODO: Implement createOwnedEnumeration method
        pass

class EModelElement:

    pass
class RefOntoUML_Element(EModelElement):

    def __init__(self, RefOntoUML_Element: "RefOntoUML_Comment" = None, Element: "RefOntoUML_Element" = None, owner: set["RefOntoUML_Element"] = None, Element5: "RefOntoUML_Element" = None, ownedElement: "RefOntoUML_Element" = None, RefOntoUML_Element7: set["RefOntoUML_Comment"] = None, RefOntoUML_Element24: "RefOntoUML_DirectedRelationship" = None, RefOntoUML_Element27: "RefOntoUML_DirectedRelationship" = None, RefOntoUML_Element29: "RefOntoUML_Relationship" = None, RefOntoUML_Element50: "RefOntoUML_Constraintx" = None):
        self.RefOntoUML_Element = RefOntoUML_Element
        self.Element = Element
        self.owner = owner if owner is not None else set()
        self.Element5 = Element5
        self.ownedElement = ownedElement
        self.RefOntoUML_Element7 = RefOntoUML_Element7 if RefOntoUML_Element7 is not None else set()
        self.RefOntoUML_Element24 = RefOntoUML_Element24
        self.RefOntoUML_Element27 = RefOntoUML_Element27
        self.RefOntoUML_Element29 = RefOntoUML_Element29
        self.RefOntoUML_Element50 = RefOntoUML_Element50
        
    @property
    def RefOntoUML_Element24(self):
        return self.__RefOntoUML_Element24

    @RefOntoUML_Element24.setter
    def RefOntoUML_Element24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_Element__RefOntoUML_Element24", None)
        self.__RefOntoUML_Element24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefOntoUML_DirectedRelationship"):
                opp_val = getattr(old_value, "RefOntoUML_DirectedRelationship", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefOntoUML_DirectedRelationship"):
                opp_val = getattr(value, "RefOntoUML_DirectedRelationship", None)
                if opp_val is None:
                    setattr(value, "RefOntoUML_DirectedRelationship", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def RefOntoUML_Element50(self):
        return self.__RefOntoUML_Element50

    @RefOntoUML_Element50.setter
    def RefOntoUML_Element50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_Element__RefOntoUML_Element50", None)
        self.__RefOntoUML_Element50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefOntoUML_Constraintx"):
                opp_val = getattr(old_value, "RefOntoUML_Constraintx", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefOntoUML_Constraintx"):
                opp_val = getattr(value, "RefOntoUML_Constraintx", None)
                if opp_val is None:
                    setattr(value, "RefOntoUML_Constraintx", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ownedElement(self):
        return self.__ownedElement

    @ownedElement.setter
    def ownedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_Element__ownedElement", None)
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
    def Element5(self):
        return self.__Element5

    @Element5.setter
    def Element5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_Element__Element5", None)
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
    def RefOntoUML_Element7(self):
        return self.__RefOntoUML_Element7

    @RefOntoUML_Element7.setter
    def RefOntoUML_Element7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_Element__RefOntoUML_Element7", None)
        self.__RefOntoUML_Element7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RefOntoUML_Comment8"):
                    opp_val = getattr(item, "RefOntoUML_Comment8", None)
                    
                    if opp_val == self:
                        setattr(item, "RefOntoUML_Comment8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RefOntoUML_Comment8"):
                    opp_val = getattr(item, "RefOntoUML_Comment8", None)
                    
                    setattr(item, "RefOntoUML_Comment8", self)
                    

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_Element__owner", None)
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
    def RefOntoUML_Element(self):
        return self.__RefOntoUML_Element

    @RefOntoUML_Element.setter
    def RefOntoUML_Element(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_Element__RefOntoUML_Element", None)
        self.__RefOntoUML_Element = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefOntoUML_Comment"):
                opp_val = getattr(old_value, "RefOntoUML_Comment", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefOntoUML_Comment"):
                opp_val = getattr(value, "RefOntoUML_Comment", None)
                if opp_val is None:
                    setattr(value, "RefOntoUML_Comment", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Element(self):
        return self.__Element

    @Element.setter
    def Element(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_Element__Element", None)
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
    def RefOntoUML_Element29(self):
        return self.__RefOntoUML_Element29

    @RefOntoUML_Element29.setter
    def RefOntoUML_Element29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_Element__RefOntoUML_Element29", None)
        self.__RefOntoUML_Element29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefOntoUML_Relationship"):
                opp_val = getattr(old_value, "RefOntoUML_Relationship", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefOntoUML_Relationship"):
                opp_val = getattr(value, "RefOntoUML_Relationship", None)
                if opp_val is None:
                    setattr(value, "RefOntoUML_Relationship", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def RefOntoUML_Element27(self):
        return self.__RefOntoUML_Element27

    @RefOntoUML_Element27.setter
    def RefOntoUML_Element27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_Element__RefOntoUML_Element27", None)
        self.__RefOntoUML_Element27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefOntoUML_DirectedRelationship26"):
                opp_val = getattr(old_value, "RefOntoUML_DirectedRelationship26", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefOntoUML_DirectedRelationship26"):
                opp_val = getattr(value, "RefOntoUML_DirectedRelationship26", None)
                if opp_val is None:
                    setattr(value, "RefOntoUML_DirectedRelationship26", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def getNearestPackage(self) -> str:
        # TODO: Implement getNearestPackage method
        pass

    def allOwnedElements(self) -> Element:
        # TODO: Implement allOwnedElements method
        pass

    def mustBeOwned(self) -> str:
        # TODO: Implement mustBeOwned method
        pass

    def hasKeyword(self, keyword: str) -> str:
        # TODO: Implement hasKeyword method
        pass

    def getTargetDirectedRelationships(self, eClass: str) -> str:
        # TODO: Implement getTargetDirectedRelationships method
        pass

    def destroy(self):
        # TODO: Implement destroy method
        pass

    def getApplicableStereotype(self, qualifiedName: str):
        # TODO: Implement getApplicableStereotype method
        pass

    def getAppliedStereotype(self, qualifiedName: str):
        # TODO: Implement getAppliedStereotype method
        pass

    def createEAnnotation(self, source: str) -> str:
        # TODO: Implement createEAnnotation method
        pass

    def getStereotypeApplications(self) -> str:
        # TODO: Implement getStereotypeApplications method
        pass

    def has_owner(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement has_owner method
        pass

    def getModel(self) -> str:
        # TODO: Implement getModel method
        pass

    def getRelationships(self) -> str:
        # TODO: Implement getRelationships method
        pass

    def getRelationships(self, eClass: str) -> str:
        # TODO: Implement getRelationships method
        pass

    def getSourceDirectedRelationships(self) -> str:
        # TODO: Implement getSourceDirectedRelationships method
        pass

    def not_own_self(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement not_own_self method
        pass

    def getTargetDirectedRelationships(self) -> str:
        # TODO: Implement getTargetDirectedRelationships method
        pass

    def removeKeyword(self, keyword: str) -> str:
        # TODO: Implement removeKeyword method
        pass

    def getSourceDirectedRelationships(self, eClass: str) -> str:
        # TODO: Implement getSourceDirectedRelationships method
        pass

    def getRequiredStereotype(self, qualifiedName: str):
        # TODO: Implement getRequiredStereotype method
        pass

    def getKeywords(self) -> str:
        # TODO: Implement getKeywords method
        pass

    def addKeyword(self, keyword: str) -> str:
        # TODO: Implement addKeyword method
        pass

class Element:

    pass
class RefOntoUML_Slot(Element):

    pass
class RefOntoUML_Relationship(Element):

    pass
class RefOntoUML_MultiplicityElement(Element):

    def __init__(self, lower: str, isOrdered: str, isUnique: str, upper: str, RefOntoUML_MultiplicityElement: "RefOntoUML_ValueSpecification" = None, RefOntoUML_MultiplicityElement99: "RefOntoUML_ValueSpecification" = None):
        self.lower = lower
        self.isOrdered = isOrdered
        self.isUnique = isUnique
        self.upper = upper
        self.RefOntoUML_MultiplicityElement = RefOntoUML_MultiplicityElement
        self.RefOntoUML_MultiplicityElement99 = RefOntoUML_MultiplicityElement99
        
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
    def upper(self) -> str:
        return self.__upper

    @upper.setter
    def upper(self, upper: str):
        self.__upper = upper

    @property
    def lower(self) -> str:
        return self.__lower

    @lower.setter
    def lower(self, lower: str):
        self.__lower = lower

    @property
    def RefOntoUML_MultiplicityElement99(self):
        return self.__RefOntoUML_MultiplicityElement99

    @RefOntoUML_MultiplicityElement99.setter
    def RefOntoUML_MultiplicityElement99(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_MultiplicityElement__RefOntoUML_MultiplicityElement99", None)
        self.__RefOntoUML_MultiplicityElement99 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefOntoUML_ValueSpecification100"):
                opp_val = getattr(old_value, "RefOntoUML_ValueSpecification100", None)
                if opp_val == self:
                    setattr(old_value, "RefOntoUML_ValueSpecification100", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefOntoUML_ValueSpecification100"):
                opp_val = getattr(value, "RefOntoUML_ValueSpecification100", None)
                setattr(value, "RefOntoUML_ValueSpecification100", self)

    @property
    def RefOntoUML_MultiplicityElement(self):
        return self.__RefOntoUML_MultiplicityElement

    @RefOntoUML_MultiplicityElement.setter
    def RefOntoUML_MultiplicityElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_MultiplicityElement__RefOntoUML_MultiplicityElement", None)
        self.__RefOntoUML_MultiplicityElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefOntoUML_ValueSpecification97"):
                opp_val = getattr(old_value, "RefOntoUML_ValueSpecification97", None)
                if opp_val == self:
                    setattr(old_value, "RefOntoUML_ValueSpecification97", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefOntoUML_ValueSpecification97"):
                opp_val = getattr(value, "RefOntoUML_ValueSpecification97", None)
                setattr(value, "RefOntoUML_ValueSpecification97", self)

    def value_specification_constant(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement value_specification_constant method
        pass

    def setUpper(self, newUpper: str):
        # TODO: Implement setUpper method
        pass

    def upperBound(self) -> str:
        # TODO: Implement upperBound method
        pass

    def lowerBound(self) -> str:
        # TODO: Implement lowerBound method
        pass

    def isMultivalued(self) -> str:
        # TODO: Implement isMultivalued method
        pass

    def is(self, lowerbound: str, upperbound: str) -> str:
        # TODO: Implement is method
        pass

    def includesCardinality(self, C: str) -> str:
        # TODO: Implement includesCardinality method
        pass

    def setLower(self, newLower: str):
        # TODO: Implement setLower method
        pass

    def lower_ge_0(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement lower_ge_0 method
        pass

    def upper_ge_lower(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement upper_ge_lower method
        pass

    def getLower(self) -> str:
        # TODO: Implement getLower method
        pass

    def value_specification_no_side_effects(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement value_specification_no_side_effects method
        pass

    def compatibleWith(self, other: str) -> str:
        # TODO: Implement compatibleWith method
        pass

    def includesMultiplicity(self, M: str) -> str:
        # TODO: Implement includesMultiplicity method
        pass

    def getUpper(self) -> str:
        # TODO: Implement getUpper method
        pass

class RefOntoUML_NamedElement(Element):

    def __init__(self, name: str, visibility: str, qualifiedName: str, RefOntoUML_NamedElement21: "RefOntoUML_Dependency" = None, client: set["RefOntoUML_Dependency"] = None, ownedMember: "RefOntoUML_Namespace" = None, RefOntoUML_NamedElement: "RefOntoUML_StringExpression" = None, NamedElement: "RefOntoUML_Dependency" = None, RefOntoUML_NamedElement35: "RefOntoUML_Namespace" = None, NamedElement40: "RefOntoUML_Namespace" = None, RefOntoUML_NamedElement69: "RefOntoUML_Classifier" = None):
        self.name = name
        self.visibility = visibility
        self.qualifiedName = qualifiedName
        self.RefOntoUML_NamedElement21 = RefOntoUML_NamedElement21
        self.client = client if client is not None else set()
        self.ownedMember = ownedMember
        self.RefOntoUML_NamedElement = RefOntoUML_NamedElement
        self.NamedElement = NamedElement
        self.RefOntoUML_NamedElement35 = RefOntoUML_NamedElement35
        self.NamedElement40 = NamedElement40
        self.RefOntoUML_NamedElement69 = RefOntoUML_NamedElement69
        
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
    def client(self):
        return self.__client

    @client.setter
    def client(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_NamedElement__client", None)
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
    def RefOntoUML_NamedElement69(self):
        return self.__RefOntoUML_NamedElement69

    @RefOntoUML_NamedElement69.setter
    def RefOntoUML_NamedElement69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_NamedElement__RefOntoUML_NamedElement69", None)
        self.__RefOntoUML_NamedElement69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefOntoUML_Classifier"):
                opp_val = getattr(old_value, "RefOntoUML_Classifier", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefOntoUML_Classifier"):
                opp_val = getattr(value, "RefOntoUML_Classifier", None)
                if opp_val is None:
                    setattr(value, "RefOntoUML_Classifier", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def RefOntoUML_NamedElement21(self):
        return self.__RefOntoUML_NamedElement21

    @RefOntoUML_NamedElement21.setter
    def RefOntoUML_NamedElement21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_NamedElement__RefOntoUML_NamedElement21", None)
        self.__RefOntoUML_NamedElement21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefOntoUML_Dependency"):
                opp_val = getattr(old_value, "RefOntoUML_Dependency", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefOntoUML_Dependency"):
                opp_val = getattr(value, "RefOntoUML_Dependency", None)
                if opp_val is None:
                    setattr(value, "RefOntoUML_Dependency", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def RefOntoUML_NamedElement35(self):
        return self.__RefOntoUML_NamedElement35

    @RefOntoUML_NamedElement35.setter
    def RefOntoUML_NamedElement35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_NamedElement__RefOntoUML_NamedElement35", None)
        self.__RefOntoUML_NamedElement35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefOntoUML_Namespace"):
                opp_val = getattr(old_value, "RefOntoUML_Namespace", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefOntoUML_Namespace"):
                opp_val = getattr(value, "RefOntoUML_Namespace", None)
                if opp_val is None:
                    setattr(value, "RefOntoUML_Namespace", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ownedMember(self):
        return self.__ownedMember

    @ownedMember.setter
    def ownedMember(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_NamedElement__ownedMember", None)
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
    def NamedElement(self):
        return self.__NamedElement

    @NamedElement.setter
    def NamedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_NamedElement__NamedElement", None)
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
    def NamedElement40(self):
        return self.__NamedElement40

    @NamedElement40.setter
    def NamedElement40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_NamedElement__NamedElement40", None)
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
    def RefOntoUML_NamedElement(self):
        return self.__RefOntoUML_NamedElement

    @RefOntoUML_NamedElement.setter
    def RefOntoUML_NamedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_NamedElement__RefOntoUML_NamedElement", None)
        self.__RefOntoUML_NamedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefOntoUML_StringExpression"):
                opp_val = getattr(old_value, "RefOntoUML_StringExpression", None)
                if opp_val == self:
                    setattr(old_value, "RefOntoUML_StringExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefOntoUML_StringExpression"):
                opp_val = getattr(value, "RefOntoUML_StringExpression", None)
                setattr(value, "RefOntoUML_StringExpression", self)

    def getLabel(self) -> str:
        # TODO: Implement getLabel method
        pass

    def getLabel(self, localize: str) -> str:
        # TODO: Implement getLabel method
        pass

    def separator(self) -> str:
        # TODO: Implement separator method
        pass

    def has_no_qualified_name(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement has_no_qualified_name method
        pass

    def allNamespaces(self) -> Namespace:
        # TODO: Implement allNamespaces method
        pass

    def allOwningPackages(self) -> str:
        # TODO: Implement allOwningPackages method
        pass

    def has_qualified_name(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement has_qualified_name method
        pass

    def createUsage(self, supplier: NamedElement):
        # TODO: Implement createUsage method
        pass

    def isDistinguishableFrom(self, ns: Namespace, n: NamedElement) -> str:
        # TODO: Implement isDistinguishableFrom method
        pass

    def getQualifiedName(self) -> str:
        # TODO: Implement getQualifiedName method
        pass

    def createDependency(self, supplier: NamedElement) -> str:
        # TODO: Implement createDependency method
        pass

    def visibility_needs_ownership(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement visibility_needs_ownership method
        pass

class RefOntoUML_Comment(Element):

    def __init__(self, body: str, RefOntoUML_Comment: set["RefOntoUML_Element"] = None, RefOntoUML_Comment8: "RefOntoUML_Element" = None):
        self.body = body
        self.RefOntoUML_Comment = RefOntoUML_Comment if RefOntoUML_Comment is not None else set()
        self.RefOntoUML_Comment8 = RefOntoUML_Comment8
        
    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

    @property
    def RefOntoUML_Comment8(self):
        return self.__RefOntoUML_Comment8

    @RefOntoUML_Comment8.setter
    def RefOntoUML_Comment8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_Comment__RefOntoUML_Comment8", None)
        self.__RefOntoUML_Comment8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefOntoUML_Element7"):
                opp_val = getattr(old_value, "RefOntoUML_Element7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefOntoUML_Element7"):
                opp_val = getattr(value, "RefOntoUML_Element7", None)
                if opp_val is None:
                    setattr(value, "RefOntoUML_Element7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def RefOntoUML_Comment(self):
        return self.__RefOntoUML_Comment

    @RefOntoUML_Comment.setter
    def RefOntoUML_Comment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefOntoUML_Comment__RefOntoUML_Comment", None)
        self.__RefOntoUML_Comment = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RefOntoUML_Element"):
                    opp_val = getattr(item, "RefOntoUML_Element", None)
                    
                    if opp_val == self:
                        setattr(item, "RefOntoUML_Element", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RefOntoUML_Element"):
                    opp_val = getattr(item, "RefOntoUML_Element", None)
                    
                    setattr(item, "RefOntoUML_Element", self)
                    
