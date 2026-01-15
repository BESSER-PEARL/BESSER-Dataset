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
class ParameterDirectionKind(Enum):
    in = "in"
    inout = "inout"
    out = "out"
    return = "return"
class AggregationKind(Enum):
    none = "none"
    shared = "shared"
    composite = "composite"


############################################
# Definition of Classes
############################################

class cmof_Exception:

    def __init__(self, description: str, cmof_Exception: "cmof_Element" = None, cmof_Exception185: "cmof_Element" = None):
        self.description = description
        self.cmof_Exception = cmof_Exception
        self.cmof_Exception185 = cmof_Exception185
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def cmof_Exception185(self):
        return self.__cmof_Exception185

    @cmof_Exception185.setter
    def cmof_Exception185(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Exception__cmof_Exception185", None)
        self.__cmof_Exception185 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_Element186"):
                opp_val = getattr(old_value, "cmof_Element186", None)
                if opp_val == self:
                    setattr(old_value, "cmof_Element186", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_Element186"):
                opp_val = getattr(value, "cmof_Element186", None)
                setattr(value, "cmof_Element186", self)

    @property
    def cmof_Exception(self):
        return self.__cmof_Exception

    @cmof_Exception.setter
    def cmof_Exception(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Exception__cmof_Exception", None)
        self.__cmof_Exception = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_Element183"):
                opp_val = getattr(old_value, "cmof_Element183", None)
                if opp_val == self:
                    setattr(old_value, "cmof_Element183", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_Element183"):
                opp_val = getattr(value, "cmof_Element183", None)
                setattr(value, "cmof_Element183", self)

class Extent:

    pass
class cmof_URIExtent(Extent):

    def __init__(self):
        
    def element(self, uri: str) -> Element:
        # TODO: Implement element method
        pass

    def uri(self, object: Element) -> str:
        # TODO: Implement uri method
        pass

    def contextURI(self) -> str:
        # TODO: Implement contextURI method
        pass

class ValueSpecification:

    pass
class cmof_OpaqueExpression(ValueSpecification):

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

    def value(self) -> str:
        # TODO: Implement value method
        pass

    def isIntegral(self) -> str:
        # TODO: Implement isIntegral method
        pass

    def isPositive(self) -> str:
        # TODO: Implement isPositive method
        pass

    def language_body_size(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement language_body_size method
        pass

    def isNonNegative(self) -> str:
        # TODO: Implement isNonNegative method
        pass

class cmof_LiteralSpecification(ValueSpecification):

    pass
class cmof_Expression(ValueSpecification):

    def __init__(self, symbol: str, cmof_Expression: set["cmof_ValueSpecification"] = None):
        self.symbol = symbol
        self.cmof_Expression = cmof_Expression if cmof_Expression is not None else set()
        
    @property
    def symbol(self) -> str:
        return self.__symbol

    @symbol.setter
    def symbol(self, symbol: str):
        self.__symbol = symbol

    @property
    def cmof_Expression(self):
        return self.__cmof_Expression

    @cmof_Expression.setter
    def cmof_Expression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Expression__cmof_Expression", None)
        self.__cmof_Expression = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cmof_ValueSpecification169"):
                    opp_val = getattr(item, "cmof_ValueSpecification169", None)
                    
                    if opp_val == self:
                        setattr(item, "cmof_ValueSpecification169", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cmof_ValueSpecification169"):
                    opp_val = getattr(item, "cmof_ValueSpecification169", None)
                    
                    setattr(item, "cmof_ValueSpecification169", self)
                    

class LiteralSpecification:

    pass
class cmof_LiteralReal(LiteralSpecification):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class cmof_LiteralString(LiteralSpecification):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class cmof_LiteralUnlimitedNatural(LiteralSpecification):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class cmof_LiteralNull(LiteralSpecification):

    pass
class cmof_LiteralInteger(LiteralSpecification):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class cmof_LiteralBoolean(LiteralSpecification):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class cmof_InstanceValue(ValueSpecification):

    pass
class DataType:

    pass
class cmof_PrimitiveType(DataType):

    pass
class cmof_Enumeration(DataType):

    pass
class cmof_Argument:

    def __init__(self, name: str, cmof_Argument: "cmof_Object" = None):
        self.name = name
        self.cmof_Argument = cmof_Argument
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def cmof_Argument(self):
        return self.__cmof_Argument

    @cmof_Argument.setter
    def cmof_Argument(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Argument__cmof_Argument", None)
        self.__cmof_Argument = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_Object"):
                opp_val = getattr(old_value, "cmof_Object", None)
                if opp_val == self:
                    setattr(old_value, "cmof_Object", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_Object"):
                opp_val = getattr(value, "cmof_Object", None)
                setattr(value, "cmof_Object", self)

class InstanceSpecification:

    pass
class cmof_EnumerationLiteral(InstanceSpecification):

    def __init__(self, EnumerationLiteral: "cmof_Enumeration" = None, ownedLiteral: "cmof_Enumeration" = None):
        self.EnumerationLiteral = EnumerationLiteral
        self.ownedLiteral = ownedLiteral
        
    @property
    def ownedLiteral(self):
        return self.__ownedLiteral

    @ownedLiteral.setter
    def ownedLiteral(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_EnumerationLiteral__ownedLiteral", None)
        self.__ownedLiteral = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Enumeration"):
                opp_val = getattr(old_value, "Enumeration", None)
                if opp_val == self:
                    setattr(old_value, "Enumeration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Enumeration"):
                opp_val = getattr(value, "Enumeration", None)
                setattr(value, "Enumeration", self)

    @property
    def EnumerationLiteral(self):
        return self.__EnumerationLiteral

    @EnumerationLiteral.setter
    def EnumerationLiteral(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_EnumerationLiteral__EnumerationLiteral", None)
        self.__EnumerationLiteral = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "enumeration"):
                opp_val = getattr(old_value, "enumeration", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "enumeration"):
                opp_val = getattr(value, "enumeration", None)
                if opp_val is None:
                    setattr(value, "enumeration", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def classifier_equals_owning_enumeration(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement classifier_equals_owning_enumeration method
        pass

    def classifier(self) -> str:
        # TODO: Implement classifier method
        pass

class BehavioralFeature:

    pass
class Relationship:

    pass
class cmof_DirectedRelationship(Relationship):

    pass
class DirectedRelationship:

    pass
class cmof_PackageImport(DirectedRelationship):

    def __init__(self, visibility: str, PackageImport: "cmof_Namespace" = None, cmof_PackageImport: "cmof_Package" = None, packageImport: "cmof_Namespace" = None):
        self.visibility = visibility
        self.PackageImport = PackageImport
        self.cmof_PackageImport = cmof_PackageImport
        self.packageImport = packageImport
        
    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def cmof_PackageImport(self):
        return self.__cmof_PackageImport

    @cmof_PackageImport.setter
    def cmof_PackageImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_PackageImport__cmof_PackageImport", None)
        self.__cmof_PackageImport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_Package95"):
                opp_val = getattr(old_value, "cmof_Package95", None)
                if opp_val == self:
                    setattr(old_value, "cmof_Package95", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_Package95"):
                opp_val = getattr(value, "cmof_Package95", None)
                setattr(value, "cmof_Package95", self)

    @property
    def PackageImport(self):
        return self.__PackageImport

    @PackageImport.setter
    def PackageImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_PackageImport__PackageImport", None)
        self.__PackageImport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "importingNamespace74"):
                opp_val = getattr(old_value, "importingNamespace74", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "importingNamespace74"):
                opp_val = getattr(value, "importingNamespace74", None)
                if opp_val is None:
                    setattr(value, "importingNamespace74", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def packageImport(self):
        return self.__packageImport

    @packageImport.setter
    def packageImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_PackageImport__packageImport", None)
        self.__packageImport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Namespace97"):
                opp_val = getattr(old_value, "Namespace97", None)
                if opp_val == self:
                    setattr(old_value, "Namespace97", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Namespace97"):
                opp_val = getattr(value, "Namespace97", None)
                setattr(value, "Namespace97", self)

    def public_or_private(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement public_or_private method
        pass

class cmof_ElementImport(DirectedRelationship):

    def __init__(self, alias: str, visibility: str, ElementImport: "cmof_Namespace" = None, cmof_ElementImport: "cmof_PackageableElement" = None, elementImport: "cmof_Namespace" = None):
        self.alias = alias
        self.visibility = visibility
        self.ElementImport = ElementImport
        self.cmof_ElementImport = cmof_ElementImport
        self.elementImport = elementImport
        
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
    def elementImport(self):
        return self.__elementImport

    @elementImport.setter
    def elementImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_ElementImport__elementImport", None)
        self.__elementImport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Namespace78"):
                opp_val = getattr(old_value, "Namespace78", None)
                if opp_val == self:
                    setattr(old_value, "Namespace78", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Namespace78"):
                opp_val = getattr(value, "Namespace78", None)
                setattr(value, "Namespace78", self)

    @property
    def cmof_ElementImport(self):
        return self.__cmof_ElementImport

    @cmof_ElementImport.setter
    def cmof_ElementImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_ElementImport__cmof_ElementImport", None)
        self.__cmof_ElementImport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_PackageableElement76"):
                opp_val = getattr(old_value, "cmof_PackageableElement76", None)
                if opp_val == self:
                    setattr(old_value, "cmof_PackageableElement76", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_PackageableElement76"):
                opp_val = getattr(value, "cmof_PackageableElement76", None)
                setattr(value, "cmof_PackageableElement76", self)

    @property
    def ElementImport(self):
        return self.__ElementImport

    @ElementImport.setter
    def ElementImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_ElementImport__ElementImport", None)
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

    def getName(self) -> str:
        # TODO: Implement getName method
        pass

    def visibility_public_or_private(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement visibility_public_or_private method
        pass

    def imported_element_is_public(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement imported_element_is_public method
        pass

class cmof_PackageMerge(DirectedRelationship):

    pass
class cmof_Generalization(DirectedRelationship):

    def __init__(self, isSubstitutable: str, Generalization: "cmof_Classifier" = None, cmof_Generalization: "cmof_Classifier" = None, generalization: "cmof_Classifier" = None):
        self.isSubstitutable = isSubstitutable
        self.Generalization = Generalization
        self.cmof_Generalization = cmof_Generalization
        self.generalization = generalization
        
    @property
    def isSubstitutable(self) -> str:
        return self.__isSubstitutable

    @isSubstitutable.setter
    def isSubstitutable(self, isSubstitutable: str):
        self.__isSubstitutable = isSubstitutable

    @property
    def generalization(self):
        return self.__generalization

    @generalization.setter
    def generalization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Generalization__generalization", None)
        self.__generalization = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Classifier105"):
                opp_val = getattr(old_value, "Classifier105", None)
                if opp_val == self:
                    setattr(old_value, "Classifier105", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Classifier105"):
                opp_val = getattr(value, "Classifier105", None)
                setattr(value, "Classifier105", self)

    @property
    def cmof_Generalization(self):
        return self.__cmof_Generalization

    @cmof_Generalization.setter
    def cmof_Generalization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Generalization__cmof_Generalization", None)
        self.__cmof_Generalization = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_Classifier103"):
                opp_val = getattr(old_value, "cmof_Classifier103", None)
                if opp_val == self:
                    setattr(old_value, "cmof_Classifier103", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_Classifier103"):
                opp_val = getattr(value, "cmof_Classifier103", None)
                setattr(value, "cmof_Classifier103", self)

    @property
    def Generalization(self):
        return self.__Generalization

    @Generalization.setter
    def Generalization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Generalization__Generalization", None)
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

class PackageableElement:

    pass
class cmof_Constraint(PackageableElement):

    def __init__(self, Constraint: "cmof_Namespace" = None, ownedRule: "cmof_Namespace" = None, cmof_Constraint: set["cmof_Element"] = None, cmof_Constraint89: "cmof_ValueSpecification" = None, cmof_Constraint107: "cmof_Operation" = None, cmof_Constraint112: "cmof_Operation" = None, cmof_Constraint115: "cmof_Operation" = None):
        self.Constraint = Constraint
        self.ownedRule = ownedRule
        self.cmof_Constraint = cmof_Constraint if cmof_Constraint is not None else set()
        self.cmof_Constraint89 = cmof_Constraint89
        self.cmof_Constraint107 = cmof_Constraint107
        self.cmof_Constraint112 = cmof_Constraint112
        self.cmof_Constraint115 = cmof_Constraint115
        
    @property
    def cmof_Constraint(self):
        return self.__cmof_Constraint

    @cmof_Constraint.setter
    def cmof_Constraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Constraint__cmof_Constraint", None)
        self.__cmof_Constraint = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cmof_Element87"):
                    opp_val = getattr(item, "cmof_Element87", None)
                    
                    if opp_val == self:
                        setattr(item, "cmof_Element87", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cmof_Element87"):
                    opp_val = getattr(item, "cmof_Element87", None)
                    
                    setattr(item, "cmof_Element87", self)
                    

    @property
    def cmof_Constraint107(self):
        return self.__cmof_Constraint107

    @cmof_Constraint107.setter
    def cmof_Constraint107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Constraint__cmof_Constraint107", None)
        self.__cmof_Constraint107 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_Operation"):
                opp_val = getattr(old_value, "cmof_Operation", None)
                if opp_val == self:
                    setattr(old_value, "cmof_Operation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_Operation"):
                opp_val = getattr(value, "cmof_Operation", None)
                setattr(value, "cmof_Operation", self)

    @property
    def ownedRule(self):
        return self.__ownedRule

    @ownedRule.setter
    def ownedRule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Constraint__ownedRule", None)
        self.__ownedRule = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Namespace92"):
                opp_val = getattr(old_value, "Namespace92", None)
                if opp_val == self:
                    setattr(old_value, "Namespace92", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Namespace92"):
                opp_val = getattr(value, "Namespace92", None)
                setattr(value, "Namespace92", self)

    @property
    def cmof_Constraint112(self):
        return self.__cmof_Constraint112

    @cmof_Constraint112.setter
    def cmof_Constraint112(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Constraint__cmof_Constraint112", None)
        self.__cmof_Constraint112 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_Operation111"):
                opp_val = getattr(old_value, "cmof_Operation111", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_Operation111"):
                opp_val = getattr(value, "cmof_Operation111", None)
                if opp_val is None:
                    setattr(value, "cmof_Operation111", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Constraint(self):
        return self.__Constraint

    @Constraint.setter
    def Constraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Constraint__Constraint", None)
        self.__Constraint = value
        
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
    def cmof_Constraint89(self):
        return self.__cmof_Constraint89

    @cmof_Constraint89.setter
    def cmof_Constraint89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Constraint__cmof_Constraint89", None)
        self.__cmof_Constraint89 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_ValueSpecification90"):
                opp_val = getattr(old_value, "cmof_ValueSpecification90", None)
                if opp_val == self:
                    setattr(old_value, "cmof_ValueSpecification90", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_ValueSpecification90"):
                opp_val = getattr(value, "cmof_ValueSpecification90", None)
                setattr(value, "cmof_ValueSpecification90", self)

    @property
    def cmof_Constraint115(self):
        return self.__cmof_Constraint115

    @cmof_Constraint115.setter
    def cmof_Constraint115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Constraint__cmof_Constraint115", None)
        self.__cmof_Constraint115 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_Operation114"):
                opp_val = getattr(old_value, "cmof_Operation114", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_Operation114"):
                opp_val = getattr(value, "cmof_Operation114", None)
                if opp_val is None:
                    setattr(value, "cmof_Operation114", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def value_specification_boolean(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement value_specification_boolean method
        pass

    def no_side_effects(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement no_side_effects method
        pass

    def boolean_value(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement boolean_value method
        pass

    def not_apply_to_self(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement not_apply_to_self method
        pass

class cmof_InstanceSpecification(PackageableElement):

    def __init__(self, InstanceSpecification: "cmof_Slot" = None, cmof_InstanceSpecification: set["cmof_Classifier"] = None, owningInstance: set["cmof_Slot"] = None, cmof_InstanceSpecification161: "cmof_ValueSpecification" = None, cmof_InstanceSpecification171: "cmof_InstanceValue" = None):
        self.InstanceSpecification = InstanceSpecification
        self.cmof_InstanceSpecification = cmof_InstanceSpecification if cmof_InstanceSpecification is not None else set()
        self.owningInstance = owningInstance if owningInstance is not None else set()
        self.cmof_InstanceSpecification161 = cmof_InstanceSpecification161
        self.cmof_InstanceSpecification171 = cmof_InstanceSpecification171
        
    @property
    def owningInstance(self):
        return self.__owningInstance

    @owningInstance.setter
    def owningInstance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_InstanceSpecification__owningInstance", None)
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
    def cmof_InstanceSpecification171(self):
        return self.__cmof_InstanceSpecification171

    @cmof_InstanceSpecification171.setter
    def cmof_InstanceSpecification171(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_InstanceSpecification__cmof_InstanceSpecification171", None)
        self.__cmof_InstanceSpecification171 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_InstanceValue"):
                opp_val = getattr(old_value, "cmof_InstanceValue", None)
                if opp_val == self:
                    setattr(old_value, "cmof_InstanceValue", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_InstanceValue"):
                opp_val = getattr(value, "cmof_InstanceValue", None)
                setattr(value, "cmof_InstanceValue", self)

    @property
    def cmof_InstanceSpecification161(self):
        return self.__cmof_InstanceSpecification161

    @cmof_InstanceSpecification161.setter
    def cmof_InstanceSpecification161(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_InstanceSpecification__cmof_InstanceSpecification161", None)
        self.__cmof_InstanceSpecification161 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_ValueSpecification162"):
                opp_val = getattr(old_value, "cmof_ValueSpecification162", None)
                if opp_val == self:
                    setattr(old_value, "cmof_ValueSpecification162", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_ValueSpecification162"):
                opp_val = getattr(value, "cmof_ValueSpecification162", None)
                setattr(value, "cmof_ValueSpecification162", self)

    @property
    def cmof_InstanceSpecification(self):
        return self.__cmof_InstanceSpecification

    @cmof_InstanceSpecification.setter
    def cmof_InstanceSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_InstanceSpecification__cmof_InstanceSpecification", None)
        self.__cmof_InstanceSpecification = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cmof_Classifier158"):
                    opp_val = getattr(item, "cmof_Classifier158", None)
                    
                    if opp_val == self:
                        setattr(item, "cmof_Classifier158", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cmof_Classifier158"):
                    opp_val = getattr(item, "cmof_Classifier158", None)
                    
                    setattr(item, "cmof_Classifier158", self)
                    

    @property
    def InstanceSpecification(self):
        return self.__InstanceSpecification

    @InstanceSpecification.setter
    def InstanceSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_InstanceSpecification__InstanceSpecification", None)
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

    def defining_feature(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement defining_feature method
        pass

    def structural_feature(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement structural_feature method
        pass

class cmof_Type(PackageableElement):

    def __init__(self, ownedType.1: "cmof_Package" = None, Type: "cmof_Package" = None, cmof_Type: "cmof_TypedElement" = None, cmof_Type121: "cmof_Operation" = None, cmof_Type128: "cmof_BehavioralFeature" = None, cmof_Type146: "cmof_Association" = None):
        self.ownedType.1 = ownedType.1
        self.Type = Type
        self.cmof_Type = cmof_Type
        self.cmof_Type121 = cmof_Type121
        self.cmof_Type128 = cmof_Type128
        self.cmof_Type146 = cmof_Type146
        
    @property
    def cmof_Type(self):
        return self.__cmof_Type

    @cmof_Type.setter
    def cmof_Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Type__cmof_Type", None)
        self.__cmof_Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_TypedElement"):
                opp_val = getattr(old_value, "cmof_TypedElement", None)
                if opp_val == self:
                    setattr(old_value, "cmof_TypedElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_TypedElement"):
                opp_val = getattr(value, "cmof_TypedElement", None)
                setattr(value, "cmof_TypedElement", self)

    @property
    def ownedType.1(self):
        return self.__ownedType.1

    @ownedType.1.setter
    def ownedType.1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Type__ownedType.1", None)
        self.__ownedType.1 = value
        
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
    def cmof_Type146(self):
        return self.__cmof_Type146

    @cmof_Type146.setter
    def cmof_Type146(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Type__cmof_Type146", None)
        self.__cmof_Type146 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_Association"):
                opp_val = getattr(old_value, "cmof_Association", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_Association"):
                opp_val = getattr(value, "cmof_Association", None)
                if opp_val is None:
                    setattr(value, "cmof_Association", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cmof_Type121(self):
        return self.__cmof_Type121

    @cmof_Type121.setter
    def cmof_Type121(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Type__cmof_Type121", None)
        self.__cmof_Type121 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_Operation120"):
                opp_val = getattr(old_value, "cmof_Operation120", None)
                if opp_val == self:
                    setattr(old_value, "cmof_Operation120", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_Operation120"):
                opp_val = getattr(value, "cmof_Operation120", None)
                setattr(value, "cmof_Operation120", self)

    @property
    def Type(self):
        return self.__Type

    @Type.setter
    def Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Type__Type", None)
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
    def cmof_Type128(self):
        return self.__cmof_Type128

    @cmof_Type128.setter
    def cmof_Type128(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Type__cmof_Type128", None)
        self.__cmof_Type128 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_BehavioralFeature127"):
                opp_val = getattr(old_value, "cmof_BehavioralFeature127", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_BehavioralFeature127"):
                opp_val = getattr(value, "cmof_BehavioralFeature127", None)
                if opp_val is None:
                    setattr(value, "cmof_BehavioralFeature127", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def isInstance(self, object: Object) -> str:
        # TODO: Implement isInstance method
        pass

    def conformsTo(self, other: Type) -> str:
        # TODO: Implement conformsTo method
        pass

class cmof_Operation(BehavioralFeature):

    def __init__(self, isUnique: str, lower: str, isOrdered: str, isQuery: str, upper: str, Operation: "cmof_Class" = None, cmof_Operation: "cmof_Constraint" = None, cmof_Operation111: set["cmof_Constraint"] = None, cmof_Operation114: set["cmof_Constraint"] = None, ownedOperation: "cmof_DataType" = None, ownedOperation123: "cmof_Class" = None, cmof_Operation118: "cmof_Operation" = None, cmof_Operation116: set["cmof_Operation"] = None, cmof_Operation120: "cmof_Type" = None, cmof_Operation134: "cmof_Parameter" = None, Operation144: "cmof_DataType" = None):
        self.isUnique = isUnique
        self.lower = lower
        self.isOrdered = isOrdered
        self.isQuery = isQuery
        self.upper = upper
        self.Operation = Operation
        self.cmof_Operation = cmof_Operation
        self.cmof_Operation111 = cmof_Operation111 if cmof_Operation111 is not None else set()
        self.cmof_Operation114 = cmof_Operation114 if cmof_Operation114 is not None else set()
        self.ownedOperation = ownedOperation
        self.ownedOperation123 = ownedOperation123
        self.cmof_Operation118 = cmof_Operation118
        self.cmof_Operation116 = cmof_Operation116 if cmof_Operation116 is not None else set()
        self.cmof_Operation120 = cmof_Operation120
        self.cmof_Operation134 = cmof_Operation134
        self.Operation144 = Operation144
        
    @property
    def lower(self) -> str:
        return self.__lower

    @lower.setter
    def lower(self, lower: str):
        self.__lower = lower

    @property
    def isUnique(self) -> str:
        return self.__isUnique

    @isUnique.setter
    def isUnique(self, isUnique: str):
        self.__isUnique = isUnique

    @property
    def upper(self) -> str:
        return self.__upper

    @upper.setter
    def upper(self, upper: str):
        self.__upper = upper

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
    def cmof_Operation(self):
        return self.__cmof_Operation

    @cmof_Operation.setter
    def cmof_Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Operation__cmof_Operation", None)
        self.__cmof_Operation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_Constraint107"):
                opp_val = getattr(old_value, "cmof_Constraint107", None)
                if opp_val == self:
                    setattr(old_value, "cmof_Constraint107", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_Constraint107"):
                opp_val = getattr(value, "cmof_Constraint107", None)
                setattr(value, "cmof_Constraint107", self)

    @property
    def cmof_Operation111(self):
        return self.__cmof_Operation111

    @cmof_Operation111.setter
    def cmof_Operation111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Operation__cmof_Operation111", None)
        self.__cmof_Operation111 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cmof_Constraint112"):
                    opp_val = getattr(item, "cmof_Constraint112", None)
                    
                    if opp_val == self:
                        setattr(item, "cmof_Constraint112", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cmof_Constraint112"):
                    opp_val = getattr(item, "cmof_Constraint112", None)
                    
                    setattr(item, "cmof_Constraint112", self)
                    

    @property
    def cmof_Operation120(self):
        return self.__cmof_Operation120

    @cmof_Operation120.setter
    def cmof_Operation120(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Operation__cmof_Operation120", None)
        self.__cmof_Operation120 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_Type121"):
                opp_val = getattr(old_value, "cmof_Type121", None)
                if opp_val == self:
                    setattr(old_value, "cmof_Type121", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_Type121"):
                opp_val = getattr(value, "cmof_Type121", None)
                setattr(value, "cmof_Type121", self)

    @property
    def cmof_Operation114(self):
        return self.__cmof_Operation114

    @cmof_Operation114.setter
    def cmof_Operation114(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Operation__cmof_Operation114", None)
        self.__cmof_Operation114 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cmof_Constraint115"):
                    opp_val = getattr(item, "cmof_Constraint115", None)
                    
                    if opp_val == self:
                        setattr(item, "cmof_Constraint115", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cmof_Constraint115"):
                    opp_val = getattr(item, "cmof_Constraint115", None)
                    
                    setattr(item, "cmof_Constraint115", self)
                    

    @property
    def Operation144(self):
        return self.__Operation144

    @Operation144.setter
    def Operation144(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Operation__Operation144", None)
        self.__Operation144 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datatype143"):
                opp_val = getattr(old_value, "datatype143", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datatype143"):
                opp_val = getattr(value, "datatype143", None)
                if opp_val is None:
                    setattr(value, "datatype143", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cmof_Operation116(self):
        return self.__cmof_Operation116

    @cmof_Operation116.setter
    def cmof_Operation116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Operation__cmof_Operation116", None)
        self.__cmof_Operation116 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cmof_Operation118"):
                    opp_val = getattr(item, "cmof_Operation118", None)
                    
                    if opp_val == self:
                        setattr(item, "cmof_Operation118", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cmof_Operation118"):
                    opp_val = getattr(item, "cmof_Operation118", None)
                    
                    setattr(item, "cmof_Operation118", self)
                    

    @property
    def cmof_Operation134(self):
        return self.__cmof_Operation134

    @cmof_Operation134.setter
    def cmof_Operation134(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Operation__cmof_Operation134", None)
        self.__cmof_Operation134 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_Parameter133"):
                opp_val = getattr(old_value, "cmof_Parameter133", None)
                if opp_val == self:
                    setattr(old_value, "cmof_Parameter133", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_Parameter133"):
                opp_val = getattr(value, "cmof_Parameter133", None)
                setattr(value, "cmof_Parameter133", self)

    @property
    def cmof_Operation118(self):
        return self.__cmof_Operation118

    @cmof_Operation118.setter
    def cmof_Operation118(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Operation__cmof_Operation118", None)
        self.__cmof_Operation118 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_Operation116"):
                opp_val = getattr(old_value, "cmof_Operation116", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_Operation116"):
                opp_val = getattr(value, "cmof_Operation116", None)
                if opp_val is None:
                    setattr(value, "cmof_Operation116", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Operation(self):
        return self.__Operation

    @Operation.setter
    def Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Operation__Operation", None)
        self.__Operation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "class38"):
                opp_val = getattr(old_value, "class38", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "class38"):
                opp_val = getattr(value, "class38", None)
                if opp_val is None:
                    setattr(value, "class38", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ownedOperation(self):
        return self.__ownedOperation

    @ownedOperation.setter
    def ownedOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Operation__ownedOperation", None)
        self.__ownedOperation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DataType109"):
                opp_val = getattr(old_value, "DataType109", None)
                if opp_val == self:
                    setattr(old_value, "DataType109", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DataType109"):
                opp_val = getattr(value, "DataType109", None)
                setattr(value, "DataType109", self)

    @property
    def ownedOperation123(self):
        return self.__ownedOperation123

    @ownedOperation123.setter
    def ownedOperation123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Operation__ownedOperation123", None)
        self.__ownedOperation123 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Class124"):
                opp_val = getattr(old_value, "Class124", None)
                if opp_val == self:
                    setattr(old_value, "Class124", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Class124"):
                opp_val = getattr(value, "Class124", None)
                setattr(value, "Class124", self)

    def isOrdered(self) -> str:
        # TODO: Implement isOrdered method
        pass

    def at_most_one_return(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement at_most_one_return method
        pass

    def returnResult(self) -> str:
        # TODO: Implement returnResult method
        pass

    def only_body_for_query(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement only_body_for_query method
        pass

    def type(self) -> Type:
        # TODO: Implement type method
        pass

    def isUnique(self) -> str:
        # TODO: Implement isUnique method
        pass

    def upper(self) -> str:
        # TODO: Implement upper method
        pass

    def lower(self) -> str:
        # TODO: Implement lower method
        pass

class Type:

    pass
class Namespace:

    pass
class cmof_Package(PackageableElement, Namespace):

    def __init__(self, URI: str, Package: "cmof_Type" = None, receivingPackage: set["cmof_PackageMerge"] = None, cmof_Package: set["cmof_PackageableElement"] = None, package: set["cmof_Type"] = None, Package58: "cmof_Package" = None, nestingPackage: set["cmof_Package"] = None, Package61: "cmof_Package" = None, nestedPackage.1: "cmof_Package" = None, cmof_Package95: "cmof_PackageImport" = None, cmof_Package99: "cmof_PackageMerge" = None, Package101: "cmof_PackageMerge" = None, cmof_Package181: "cmof_Factory" = None):
        self.URI = URI
        self.Package = Package
        self.receivingPackage = receivingPackage if receivingPackage is not None else set()
        self.cmof_Package = cmof_Package if cmof_Package is not None else set()
        self.package = package if package is not None else set()
        self.Package58 = Package58
        self.nestingPackage = nestingPackage if nestingPackage is not None else set()
        self.Package61 = Package61
        self.nestedPackage.1 = nestedPackage.1
        self.cmof_Package95 = cmof_Package95
        self.cmof_Package99 = cmof_Package99
        self.Package101 = Package101
        self.cmof_Package181 = cmof_Package181
        
    @property
    def URI(self) -> str:
        return self.__URI

    @URI.setter
    def URI(self, URI: str):
        self.__URI = URI

    @property
    def package(self):
        return self.__package

    @package.setter
    def package(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Package__package", None)
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
    def Package101(self):
        return self.__Package101

    @Package101.setter
    def Package101(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Package__Package101", None)
        self.__Package101 = value
        
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
    def cmof_Package95(self):
        return self.__cmof_Package95

    @cmof_Package95.setter
    def cmof_Package95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Package__cmof_Package95", None)
        self.__cmof_Package95 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_PackageImport"):
                opp_val = getattr(old_value, "cmof_PackageImport", None)
                if opp_val == self:
                    setattr(old_value, "cmof_PackageImport", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_PackageImport"):
                opp_val = getattr(value, "cmof_PackageImport", None)
                setattr(value, "cmof_PackageImport", self)

    @property
    def Package58(self):
        return self.__Package58

    @Package58.setter
    def Package58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Package__Package58", None)
        self.__Package58 = value
        
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
    def nestingPackage(self):
        return self.__nestingPackage

    @nestingPackage.setter
    def nestingPackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Package__nestingPackage", None)
        self.__nestingPackage = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Package58"):
                    opp_val = getattr(item, "Package58", None)
                    
                    if opp_val == self:
                        setattr(item, "Package58", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Package58"):
                    opp_val = getattr(item, "Package58", None)
                    
                    setattr(item, "Package58", self)
                    

    @property
    def Package61(self):
        return self.__Package61

    @Package61.setter
    def Package61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Package__Package61", None)
        self.__Package61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nestedPackage.1"):
                opp_val = getattr(old_value, "nestedPackage.1", None)
                if opp_val == self:
                    setattr(old_value, "nestedPackage.1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nestedPackage.1"):
                opp_val = getattr(value, "nestedPackage.1", None)
                setattr(value, "nestedPackage.1", self)

    @property
    def cmof_Package181(self):
        return self.__cmof_Package181

    @cmof_Package181.setter
    def cmof_Package181(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Package__cmof_Package181", None)
        self.__cmof_Package181 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_Factory"):
                opp_val = getattr(old_value, "cmof_Factory", None)
                if opp_val == self:
                    setattr(old_value, "cmof_Factory", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_Factory"):
                opp_val = getattr(value, "cmof_Factory", None)
                setattr(value, "cmof_Factory", self)

    @property
    def Package(self):
        return self.__Package

    @Package.setter
    def Package(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Package__Package", None)
        self.__Package = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownedType.1"):
                opp_val = getattr(old_value, "ownedType.1", None)
                if opp_val == self:
                    setattr(old_value, "ownedType.1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedType.1"):
                opp_val = getattr(value, "ownedType.1", None)
                setattr(value, "ownedType.1", self)

    @property
    def nestedPackage.1(self):
        return self.__nestedPackage.1

    @nestedPackage.1.setter
    def nestedPackage.1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Package__nestedPackage.1", None)
        self.__nestedPackage.1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Package61"):
                opp_val = getattr(old_value, "Package61", None)
                if opp_val == self:
                    setattr(old_value, "Package61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Package61"):
                opp_val = getattr(value, "Package61", None)
                setattr(value, "Package61", self)

    @property
    def cmof_Package(self):
        return self.__cmof_Package

    @cmof_Package.setter
    def cmof_Package(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Package__cmof_Package", None)
        self.__cmof_Package = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cmof_PackageableElement"):
                    opp_val = getattr(item, "cmof_PackageableElement", None)
                    
                    if opp_val == self:
                        setattr(item, "cmof_PackageableElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cmof_PackageableElement"):
                    opp_val = getattr(item, "cmof_PackageableElement", None)
                    
                    setattr(item, "cmof_PackageableElement", self)
                    

    @property
    def cmof_Package99(self):
        return self.__cmof_Package99

    @cmof_Package99.setter
    def cmof_Package99(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Package__cmof_Package99", None)
        self.__cmof_Package99 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_PackageMerge"):
                opp_val = getattr(old_value, "cmof_PackageMerge", None)
                if opp_val == self:
                    setattr(old_value, "cmof_PackageMerge", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_PackageMerge"):
                opp_val = getattr(value, "cmof_PackageMerge", None)
                setattr(value, "cmof_PackageMerge", self)

    @property
    def receivingPackage(self):
        return self.__receivingPackage

    @receivingPackage.setter
    def receivingPackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Package__receivingPackage", None)
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
                    

    def visibleMembers(self) -> PackageableElement:
        # TODO: Implement visibleMembers method
        pass

    def makesVisible(self, el: NamedElement) -> str:
        # TODO: Implement makesVisible method
        pass

    def nestedPackage(self) -> str:
        # TODO: Implement nestedPackage method
        pass

    def elements_public_or_private(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement elements_public_or_private method
        pass

    def ownedType(self) -> Type:
        # TODO: Implement ownedType method
        pass

class Classifier:

    pass
class Element:

    pass
class cmof_Slot(Element):

    pass
class cmof_MultiplicityElement(Element):

    def __init__(self, isOrdered: str, upper: str, isUnique: str, lower: str, cmof_MultiplicityElement138: "cmof_ValueSpecification" = None, cmof_MultiplicityElement: "cmof_ValueSpecification" = None):
        self.isOrdered = isOrdered
        self.upper = upper
        self.isUnique = isUnique
        self.lower = lower
        self.cmof_MultiplicityElement138 = cmof_MultiplicityElement138
        self.cmof_MultiplicityElement = cmof_MultiplicityElement
        
    @property
    def isUnique(self) -> str:
        return self.__isUnique

    @isUnique.setter
    def isUnique(self, isUnique: str):
        self.__isUnique = isUnique

    @property
    def lower(self) -> str:
        return self.__lower

    @lower.setter
    def lower(self, lower: str):
        self.__lower = lower

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
    def cmof_MultiplicityElement(self):
        return self.__cmof_MultiplicityElement

    @cmof_MultiplicityElement.setter
    def cmof_MultiplicityElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_MultiplicityElement__cmof_MultiplicityElement", None)
        self.__cmof_MultiplicityElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_ValueSpecification136"):
                opp_val = getattr(old_value, "cmof_ValueSpecification136", None)
                if opp_val == self:
                    setattr(old_value, "cmof_ValueSpecification136", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_ValueSpecification136"):
                opp_val = getattr(value, "cmof_ValueSpecification136", None)
                setattr(value, "cmof_ValueSpecification136", self)

    @property
    def cmof_MultiplicityElement138(self):
        return self.__cmof_MultiplicityElement138

    @cmof_MultiplicityElement138.setter
    def cmof_MultiplicityElement138(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_MultiplicityElement__cmof_MultiplicityElement138", None)
        self.__cmof_MultiplicityElement138 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_ValueSpecification139"):
                opp_val = getattr(old_value, "cmof_ValueSpecification139", None)
                if opp_val == self:
                    setattr(old_value, "cmof_ValueSpecification139", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_ValueSpecification139"):
                opp_val = getattr(value, "cmof_ValueSpecification139", None)
                setattr(value, "cmof_ValueSpecification139", self)

    def value_specification_constant(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement value_specification_constant method
        pass

    def lowerBound(self) -> str:
        # TODO: Implement lowerBound method
        pass

    def upper(self) -> str:
        # TODO: Implement upper method
        pass

    def value_specification_no_side_effects(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement value_specification_no_side_effects method
        pass

    def lower(self) -> str:
        # TODO: Implement lower method
        pass

    def lower_ge_0(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement lower_ge_0 method
        pass

    def upper_ge_lower(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement upper_ge_lower method
        pass

    def includesCardinality(self, C: str) -> str:
        # TODO: Implement includesCardinality method
        pass

    def upperBound(self) -> str:
        # TODO: Implement upperBound method
        pass

    def isMultivalued(self) -> str:
        # TODO: Implement isMultivalued method
        pass

    def includesMultiplicity(self, M: MultiplicityElement) -> str:
        # TODO: Implement includesMultiplicity method
        pass

class cmof_Factory(Element):

    def __init__(self, cmof_Factory: "cmof_Package" = None):
        self.cmof_Factory = cmof_Factory
        
    @property
    def cmof_Factory(self):
        return self.__cmof_Factory

    @cmof_Factory.setter
    def cmof_Factory(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Factory__cmof_Factory", None)
        self.__cmof_Factory = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_Package181"):
                opp_val = getattr(old_value, "cmof_Package181", None)
                if opp_val == self:
                    setattr(old_value, "cmof_Package181", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_Package181"):
                opp_val = getattr(value, "cmof_Package181", None)
                setattr(value, "cmof_Package181", self)

    def createElement(self, arguments: str, class: str) -> Element:
        # TODO: Implement createElement method
        pass

    def convertToString(self, dataType: DataType, object: Object) -> str:
        # TODO: Implement convertToString method
        pass

    def createFromString(self, string: str, dataType: DataType) -> Object:
        # TODO: Implement createFromString method
        pass

    def create(self, metaClass: str) -> Element:
        # TODO: Implement create method
        pass

    def createLink(self, association: str, secondElement: Element, firstElement: Element) -> str:
        # TODO: Implement createLink method
        pass

class cmof_Tag(Element):

    def __init__(self, name: str, value: str, cmof_Tag: set["cmof_Element"] = None, cmof_Tag190: "cmof_Element" = None):
        self.name = name
        self.value = value
        self.cmof_Tag = cmof_Tag if cmof_Tag is not None else set()
        self.cmof_Tag190 = cmof_Tag190
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def cmof_Tag190(self):
        return self.__cmof_Tag190

    @cmof_Tag190.setter
    def cmof_Tag190(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Tag__cmof_Tag190", None)
        self.__cmof_Tag190 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_Element191"):
                opp_val = getattr(old_value, "cmof_Element191", None)
                if opp_val == self:
                    setattr(old_value, "cmof_Element191", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_Element191"):
                opp_val = getattr(value, "cmof_Element191", None)
                setattr(value, "cmof_Element191", self)

    @property
    def cmof_Tag(self):
        return self.__cmof_Tag

    @cmof_Tag.setter
    def cmof_Tag(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Tag__cmof_Tag", None)
        self.__cmof_Tag = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cmof_Element188"):
                    opp_val = getattr(item, "cmof_Element188", None)
                    
                    if opp_val == self:
                        setattr(item, "cmof_Element188", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cmof_Element188"):
                    opp_val = getattr(item, "cmof_Element188", None)
                    
                    setattr(item, "cmof_Element188", self)
                    

class cmof_Relationship(Element):

    pass
class cmof_Comment(Element):

    def __init__(self, body: str, cmof_Comment: "cmof_Element" = None, cmof_Comment31: set["cmof_Element"] = None):
        self.body = body
        self.cmof_Comment = cmof_Comment
        self.cmof_Comment31 = cmof_Comment31 if cmof_Comment31 is not None else set()
        
    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

    @property
    def cmof_Comment31(self):
        return self.__cmof_Comment31

    @cmof_Comment31.setter
    def cmof_Comment31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Comment__cmof_Comment31", None)
        self.__cmof_Comment31 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cmof_Element32"):
                    opp_val = getattr(item, "cmof_Element32", None)
                    
                    if opp_val == self:
                        setattr(item, "cmof_Element32", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cmof_Element32"):
                    opp_val = getattr(item, "cmof_Element32", None)
                    
                    setattr(item, "cmof_Element32", self)
                    

    @property
    def cmof_Comment(self):
        return self.__cmof_Comment

    @cmof_Comment.setter
    def cmof_Comment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Comment__cmof_Comment", None)
        self.__cmof_Comment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_Element"):
                opp_val = getattr(old_value, "cmof_Element", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_Element"):
                opp_val = getattr(value, "cmof_Element", None)
                if opp_val is None:
                    setattr(value, "cmof_Element", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class cmof_NamedElement(Element):

    def __init__(self, name: str, qualifiedName: str, visibility: str, ownedMember: "cmof_Namespace" = None, cmof_NamedElement: "cmof_Classifier" = None, NamedElement: "cmof_Namespace" = None, cmof_NamedElement70: "cmof_Namespace" = None):
        self.name = name
        self.qualifiedName = qualifiedName
        self.visibility = visibility
        self.ownedMember = ownedMember
        self.cmof_NamedElement = cmof_NamedElement
        self.NamedElement = NamedElement
        self.cmof_NamedElement70 = cmof_NamedElement70
        
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
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def ownedMember(self):
        return self.__ownedMember

    @ownedMember.setter
    def ownedMember(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_NamedElement__ownedMember", None)
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
    def cmof_NamedElement(self):
        return self.__cmof_NamedElement

    @cmof_NamedElement.setter
    def cmof_NamedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_NamedElement__cmof_NamedElement", None)
        self.__cmof_NamedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_Classifier51"):
                opp_val = getattr(old_value, "cmof_Classifier51", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_Classifier51"):
                opp_val = getattr(value, "cmof_Classifier51", None)
                if opp_val is None:
                    setattr(value, "cmof_Classifier51", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cmof_NamedElement70(self):
        return self.__cmof_NamedElement70

    @cmof_NamedElement70.setter
    def cmof_NamedElement70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_NamedElement__cmof_NamedElement70", None)
        self.__cmof_NamedElement70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_Namespace69"):
                opp_val = getattr(old_value, "cmof_Namespace69", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_Namespace69"):
                opp_val = getattr(value, "cmof_Namespace69", None)
                if opp_val is None:
                    setattr(value, "cmof_Namespace69", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def NamedElement(self):
        return self.__NamedElement

    @NamedElement.setter
    def NamedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_NamedElement__NamedElement", None)
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

    def has_qualified_name(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement has_qualified_name method
        pass

    def qualifiedName(self) -> str:
        # TODO: Implement qualifiedName method
        pass

    def has_no_qualified_name(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement has_no_qualified_name method
        pass

    def separator(self) -> str:
        # TODO: Implement separator method
        pass

    def visibility_needs_ownership(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement visibility_needs_ownership method
        pass

    def isDistinguishableFrom(self, n: NamedElement, ns: str) -> str:
        # TODO: Implement isDistinguishableFrom method
        pass

    def allNamespaces(self) -> str:
        # TODO: Implement allNamespaces method
        pass

class NamedElement:

    pass
class cmof_TypedElement(NamedElement):

    pass
class cmof_Namespace(NamedElement):

    def __init__(self, Namespace: "cmof_NamedElement" = None, importingNamespace: set["cmof_ElementImport"] = None, namespace: set["cmof_NamedElement"] = None, context: set["cmof_Constraint"] = None, importingNamespace74: set["cmof_PackageImport"] = None, cmof_Namespace: set["cmof_PackageableElement"] = None, cmof_Namespace69: set["cmof_NamedElement"] = None, Namespace78: "cmof_ElementImport" = None, Namespace92: "cmof_Constraint" = None, Namespace97: "cmof_PackageImport" = None):
        self.Namespace = Namespace
        self.importingNamespace = importingNamespace if importingNamespace is not None else set()
        self.namespace = namespace if namespace is not None else set()
        self.context = context if context is not None else set()
        self.importingNamespace74 = importingNamespace74 if importingNamespace74 is not None else set()
        self.cmof_Namespace = cmof_Namespace if cmof_Namespace is not None else set()
        self.cmof_Namespace69 = cmof_Namespace69 if cmof_Namespace69 is not None else set()
        self.Namespace78 = Namespace78
        self.Namespace92 = Namespace92
        self.Namespace97 = Namespace97
        
    @property
    def importingNamespace74(self):
        return self.__importingNamespace74

    @importingNamespace74.setter
    def importingNamespace74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Namespace__importingNamespace74", None)
        self.__importingNamespace74 = value if value is not None else set()
        
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
    def Namespace92(self):
        return self.__Namespace92

    @Namespace92.setter
    def Namespace92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Namespace__Namespace92", None)
        self.__Namespace92 = value
        
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
    def cmof_Namespace69(self):
        return self.__cmof_Namespace69

    @cmof_Namespace69.setter
    def cmof_Namespace69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Namespace__cmof_Namespace69", None)
        self.__cmof_Namespace69 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cmof_NamedElement70"):
                    opp_val = getattr(item, "cmof_NamedElement70", None)
                    
                    if opp_val == self:
                        setattr(item, "cmof_NamedElement70", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cmof_NamedElement70"):
                    opp_val = getattr(item, "cmof_NamedElement70", None)
                    
                    setattr(item, "cmof_NamedElement70", self)
                    

    @property
    def namespace(self):
        return self.__namespace

    @namespace.setter
    def namespace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Namespace__namespace", None)
        self.__namespace = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "NamedElement"):
                    opp_val = getattr(item, "NamedElement", None)
                    
                    if opp_val == self:
                        setattr(item, "NamedElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "NamedElement"):
                    opp_val = getattr(item, "NamedElement", None)
                    
                    setattr(item, "NamedElement", self)
                    

    @property
    def Namespace97(self):
        return self.__Namespace97

    @Namespace97.setter
    def Namespace97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Namespace__Namespace97", None)
        self.__Namespace97 = value
        
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
    def Namespace(self):
        return self.__Namespace

    @Namespace.setter
    def Namespace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Namespace__Namespace", None)
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
    def context(self):
        return self.__context

    @context.setter
    def context(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Namespace__context", None)
        self.__context = value if value is not None else set()
        
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
    def Namespace78(self):
        return self.__Namespace78

    @Namespace78.setter
    def Namespace78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Namespace__Namespace78", None)
        self.__Namespace78 = value
        
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
    def cmof_Namespace(self):
        return self.__cmof_Namespace

    @cmof_Namespace.setter
    def cmof_Namespace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Namespace__cmof_Namespace", None)
        self.__cmof_Namespace = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cmof_PackageableElement67"):
                    opp_val = getattr(item, "cmof_PackageableElement67", None)
                    
                    if opp_val == self:
                        setattr(item, "cmof_PackageableElement67", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cmof_PackageableElement67"):
                    opp_val = getattr(item, "cmof_PackageableElement67", None)
                    
                    setattr(item, "cmof_PackageableElement67", self)
                    

    @property
    def importingNamespace(self):
        return self.__importingNamespace

    @importingNamespace.setter
    def importingNamespace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Namespace__importingNamespace", None)
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
                    

    def getNamesOfMember(self, element: NamedElement) -> str:
        # TODO: Implement getNamesOfMember method
        pass

    def members_distinguishable(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement members_distinguishable method
        pass

    def excludeCollisions(self, imps: PackageableElement) -> PackageableElement:
        # TODO: Implement excludeCollisions method
        pass

    def membersAreDistinguishable(self) -> str:
        # TODO: Implement membersAreDistinguishable method
        pass

    def importedMember(self) -> PackageableElement:
        # TODO: Implement importedMember method
        pass

    def importMembers(self, imps: PackageableElement) -> PackageableElement:
        # TODO: Implement importMembers method
        pass

class cmof_PackageableElement(NamedElement):

    pass
class cmof_RedefinableElement(NamedElement):

    def __init__(self, isLeaf: str, cmof_RedefinableElement: "cmof_RedefinableElement" = None, cmof_RedefinableElement17: set["cmof_RedefinableElement"] = None, cmof_RedefinableElement20: set["cmof_Classifier"] = None):
        self.isLeaf = isLeaf
        self.cmof_RedefinableElement = cmof_RedefinableElement
        self.cmof_RedefinableElement17 = cmof_RedefinableElement17 if cmof_RedefinableElement17 is not None else set()
        self.cmof_RedefinableElement20 = cmof_RedefinableElement20 if cmof_RedefinableElement20 is not None else set()
        
    @property
    def isLeaf(self) -> str:
        return self.__isLeaf

    @isLeaf.setter
    def isLeaf(self, isLeaf: str):
        self.__isLeaf = isLeaf

    @property
    def cmof_RedefinableElement(self):
        return self.__cmof_RedefinableElement

    @cmof_RedefinableElement.setter
    def cmof_RedefinableElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_RedefinableElement__cmof_RedefinableElement", None)
        self.__cmof_RedefinableElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_RedefinableElement17"):
                opp_val = getattr(old_value, "cmof_RedefinableElement17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_RedefinableElement17"):
                opp_val = getattr(value, "cmof_RedefinableElement17", None)
                if opp_val is None:
                    setattr(value, "cmof_RedefinableElement17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cmof_RedefinableElement17(self):
        return self.__cmof_RedefinableElement17

    @cmof_RedefinableElement17.setter
    def cmof_RedefinableElement17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_RedefinableElement__cmof_RedefinableElement17", None)
        self.__cmof_RedefinableElement17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cmof_RedefinableElement"):
                    opp_val = getattr(item, "cmof_RedefinableElement", None)
                    
                    if opp_val == self:
                        setattr(item, "cmof_RedefinableElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cmof_RedefinableElement"):
                    opp_val = getattr(item, "cmof_RedefinableElement", None)
                    
                    setattr(item, "cmof_RedefinableElement", self)
                    

    @property
    def cmof_RedefinableElement20(self):
        return self.__cmof_RedefinableElement20

    @cmof_RedefinableElement20.setter
    def cmof_RedefinableElement20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_RedefinableElement__cmof_RedefinableElement20", None)
        self.__cmof_RedefinableElement20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cmof_Classifier"):
                    opp_val = getattr(item, "cmof_Classifier", None)
                    
                    if opp_val == self:
                        setattr(item, "cmof_Classifier", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cmof_Classifier"):
                    opp_val = getattr(item, "cmof_Classifier", None)
                    
                    setattr(item, "cmof_Classifier", self)
                    

    def isRedefinitionContextValid(self, redefined: RedefinableElement) -> str:
        # TODO: Implement isRedefinitionContextValid method
        pass

    def redefinition_context_valid(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement redefinition_context_valid method
        pass

    def isConsistentWith(self, redefinee: RedefinableElement) -> str:
        # TODO: Implement isConsistentWith method
        pass

    def non_leaf_redefinition(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement non_leaf_redefinition method
        pass

    def redefinition_consistent(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement redefinition_consistent method
        pass

class RedefinableElement:

    pass
class cmof_Classifier(Type, RedefinableElement, Namespace):

    def __init__(self, isAbstract: str, isFinalSpecialization: str, Classifier: "cmof_Feature" = None, cmof_Classifier: "cmof_RedefinableElement" = None, cmof_Classifier35: "cmof_Class" = None, cmof_Classifier43: set["cmof_Property"] = None, featuringClassifier: set["cmof_Feature"] = None, cmof_Classifier51: set["cmof_NamedElement"] = None, cmof_Classifier54: "cmof_Classifier" = None, cmof_Classifier52: set["cmof_Classifier"] = None, cmof_Classifier48: "cmof_Classifier" = None, cmof_Classifier46: set["cmof_Classifier"] = None, specific: set["cmof_Generalization"] = None, cmof_Classifier103: "cmof_Generalization" = None, Classifier105: "cmof_Generalization" = None, cmof_Classifier158: "cmof_InstanceSpecification" = None):
        self.isAbstract = isAbstract
        self.isFinalSpecialization = isFinalSpecialization
        self.Classifier = Classifier
        self.cmof_Classifier = cmof_Classifier
        self.cmof_Classifier35 = cmof_Classifier35
        self.cmof_Classifier43 = cmof_Classifier43 if cmof_Classifier43 is not None else set()
        self.featuringClassifier = featuringClassifier if featuringClassifier is not None else set()
        self.cmof_Classifier51 = cmof_Classifier51 if cmof_Classifier51 is not None else set()
        self.cmof_Classifier54 = cmof_Classifier54
        self.cmof_Classifier52 = cmof_Classifier52 if cmof_Classifier52 is not None else set()
        self.cmof_Classifier48 = cmof_Classifier48
        self.cmof_Classifier46 = cmof_Classifier46 if cmof_Classifier46 is not None else set()
        self.specific = specific if specific is not None else set()
        self.cmof_Classifier103 = cmof_Classifier103
        self.Classifier105 = Classifier105
        self.cmof_Classifier158 = cmof_Classifier158
        
    @property
    def isAbstract(self) -> str:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: str):
        self.__isAbstract = isAbstract

    @property
    def isFinalSpecialization(self) -> str:
        return self.__isFinalSpecialization

    @isFinalSpecialization.setter
    def isFinalSpecialization(self, isFinalSpecialization: str):
        self.__isFinalSpecialization = isFinalSpecialization

    @property
    def cmof_Classifier52(self):
        return self.__cmof_Classifier52

    @cmof_Classifier52.setter
    def cmof_Classifier52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Classifier__cmof_Classifier52", None)
        self.__cmof_Classifier52 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cmof_Classifier54"):
                    opp_val = getattr(item, "cmof_Classifier54", None)
                    
                    if opp_val == self:
                        setattr(item, "cmof_Classifier54", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cmof_Classifier54"):
                    opp_val = getattr(item, "cmof_Classifier54", None)
                    
                    setattr(item, "cmof_Classifier54", self)
                    

    @property
    def featuringClassifier(self):
        return self.__featuringClassifier

    @featuringClassifier.setter
    def featuringClassifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Classifier__featuringClassifier", None)
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
    def Classifier105(self):
        return self.__Classifier105

    @Classifier105.setter
    def Classifier105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Classifier__Classifier105", None)
        self.__Classifier105 = value
        
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
    def cmof_Classifier103(self):
        return self.__cmof_Classifier103

    @cmof_Classifier103.setter
    def cmof_Classifier103(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Classifier__cmof_Classifier103", None)
        self.__cmof_Classifier103 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_Generalization"):
                opp_val = getattr(old_value, "cmof_Generalization", None)
                if opp_val == self:
                    setattr(old_value, "cmof_Generalization", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_Generalization"):
                opp_val = getattr(value, "cmof_Generalization", None)
                setattr(value, "cmof_Generalization", self)

    @property
    def cmof_Classifier51(self):
        return self.__cmof_Classifier51

    @cmof_Classifier51.setter
    def cmof_Classifier51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Classifier__cmof_Classifier51", None)
        self.__cmof_Classifier51 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cmof_NamedElement"):
                    opp_val = getattr(item, "cmof_NamedElement", None)
                    
                    if opp_val == self:
                        setattr(item, "cmof_NamedElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cmof_NamedElement"):
                    opp_val = getattr(item, "cmof_NamedElement", None)
                    
                    setattr(item, "cmof_NamedElement", self)
                    

    @property
    def Classifier(self):
        return self.__Classifier

    @Classifier.setter
    def Classifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Classifier__Classifier", None)
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
    def cmof_Classifier46(self):
        return self.__cmof_Classifier46

    @cmof_Classifier46.setter
    def cmof_Classifier46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Classifier__cmof_Classifier46", None)
        self.__cmof_Classifier46 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cmof_Classifier48"):
                    opp_val = getattr(item, "cmof_Classifier48", None)
                    
                    if opp_val == self:
                        setattr(item, "cmof_Classifier48", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cmof_Classifier48"):
                    opp_val = getattr(item, "cmof_Classifier48", None)
                    
                    setattr(item, "cmof_Classifier48", self)
                    

    @property
    def cmof_Classifier43(self):
        return self.__cmof_Classifier43

    @cmof_Classifier43.setter
    def cmof_Classifier43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Classifier__cmof_Classifier43", None)
        self.__cmof_Classifier43 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cmof_Property44"):
                    opp_val = getattr(item, "cmof_Property44", None)
                    
                    if opp_val == self:
                        setattr(item, "cmof_Property44", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cmof_Property44"):
                    opp_val = getattr(item, "cmof_Property44", None)
                    
                    setattr(item, "cmof_Property44", self)
                    

    @property
    def cmof_Classifier54(self):
        return self.__cmof_Classifier54

    @cmof_Classifier54.setter
    def cmof_Classifier54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Classifier__cmof_Classifier54", None)
        self.__cmof_Classifier54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_Classifier52"):
                opp_val = getattr(old_value, "cmof_Classifier52", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_Classifier52"):
                opp_val = getattr(value, "cmof_Classifier52", None)
                if opp_val is None:
                    setattr(value, "cmof_Classifier52", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cmof_Classifier(self):
        return self.__cmof_Classifier

    @cmof_Classifier.setter
    def cmof_Classifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Classifier__cmof_Classifier", None)
        self.__cmof_Classifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_RedefinableElement20"):
                opp_val = getattr(old_value, "cmof_RedefinableElement20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_RedefinableElement20"):
                opp_val = getattr(value, "cmof_RedefinableElement20", None)
                if opp_val is None:
                    setattr(value, "cmof_RedefinableElement20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cmof_Classifier48(self):
        return self.__cmof_Classifier48

    @cmof_Classifier48.setter
    def cmof_Classifier48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Classifier__cmof_Classifier48", None)
        self.__cmof_Classifier48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_Classifier46"):
                opp_val = getattr(old_value, "cmof_Classifier46", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_Classifier46"):
                opp_val = getattr(value, "cmof_Classifier46", None)
                if opp_val is None:
                    setattr(value, "cmof_Classifier46", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def specific(self):
        return self.__specific

    @specific.setter
    def specific(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Classifier__specific", None)
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
    def cmof_Classifier158(self):
        return self.__cmof_Classifier158

    @cmof_Classifier158.setter
    def cmof_Classifier158(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Classifier__cmof_Classifier158", None)
        self.__cmof_Classifier158 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_InstanceSpecification"):
                opp_val = getattr(old_value, "cmof_InstanceSpecification", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_InstanceSpecification"):
                opp_val = getattr(value, "cmof_InstanceSpecification", None)
                if opp_val is None:
                    setattr(value, "cmof_InstanceSpecification", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cmof_Classifier35(self):
        return self.__cmof_Classifier35

    @cmof_Classifier35.setter
    def cmof_Classifier35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Classifier__cmof_Classifier35", None)
        self.__cmof_Classifier35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_Class34"):
                opp_val = getattr(old_value, "cmof_Class34", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_Class34"):
                opp_val = getattr(value, "cmof_Class34", None)
                if opp_val is None:
                    setattr(value, "cmof_Class34", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def parents(self) -> Classifier:
        # TODO: Implement parents method
        pass

    def no_cycles_in_generalization(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement no_cycles_in_generalization method
        pass

    def hasVisibilityOf(self, n: NamedElement) -> str:
        # TODO: Implement hasVisibilityOf method
        pass

    def non_final_parents(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement non_final_parents method
        pass

    def specialize_type(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement specialize_type method
        pass

    def inherit(self, inhs: NamedElement) -> NamedElement:
        # TODO: Implement inherit method
        pass

    def general(self) -> Classifier:
        # TODO: Implement general method
        pass

    def maySpecializeType(self, c: Classifier) -> str:
        # TODO: Implement maySpecializeType method
        pass

    def allFeatures(self) -> Feature:
        # TODO: Implement allFeatures method
        pass

    def inheritableMembers(self, c: Classifier) -> NamedElement:
        # TODO: Implement inheritableMembers method
        pass

    def inheritedMember(self) -> NamedElement:
        # TODO: Implement inheritedMember method
        pass

    def conformsTo(self, other: Classifier) -> str:
        # TODO: Implement conformsTo method
        pass

    def allParents(self) -> Classifier:
        # TODO: Implement allParents method
        pass

class cmof_Feature(RedefinableElement):

    def __init__(self, isStatic: str, feature: set["cmof_Classifier"] = None, Feature: "cmof_Classifier" = None):
        self.isStatic = isStatic
        self.feature = feature if feature is not None else set()
        self.Feature = Feature
        
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
        old_value = getattr(self, f"_cmof_Feature__Feature", None)
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
        old_value = getattr(self, f"_cmof_Feature__feature", None)
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
                    

class TypedElement:

    pass
class MultiplicityElement:

    pass
class cmof_Parameter(TypedElement, MultiplicityElement):

    def __init__(self, default: str, direction: str, cmof_Parameter130: "cmof_ValueSpecification" = None, cmof_Parameter133: "cmof_Operation" = None, cmof_Parameter: "cmof_BehavioralFeature" = None):
        self.default = default
        self.direction = direction
        self.cmof_Parameter130 = cmof_Parameter130
        self.cmof_Parameter133 = cmof_Parameter133
        self.cmof_Parameter = cmof_Parameter
        
    @property
    def default(self) -> str:
        return self.__default

    @default.setter
    def default(self, default: str):
        self.__default = default

    @property
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction

    @property
    def cmof_Parameter(self):
        return self.__cmof_Parameter

    @cmof_Parameter.setter
    def cmof_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Parameter__cmof_Parameter", None)
        self.__cmof_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_BehavioralFeature"):
                opp_val = getattr(old_value, "cmof_BehavioralFeature", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_BehavioralFeature"):
                opp_val = getattr(value, "cmof_BehavioralFeature", None)
                if opp_val is None:
                    setattr(value, "cmof_BehavioralFeature", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cmof_Parameter130(self):
        return self.__cmof_Parameter130

    @cmof_Parameter130.setter
    def cmof_Parameter130(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Parameter__cmof_Parameter130", None)
        self.__cmof_Parameter130 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_ValueSpecification131"):
                opp_val = getattr(old_value, "cmof_ValueSpecification131", None)
                if opp_val == self:
                    setattr(old_value, "cmof_ValueSpecification131", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_ValueSpecification131"):
                opp_val = getattr(value, "cmof_ValueSpecification131", None)
                setattr(value, "cmof_ValueSpecification131", self)

    @property
    def cmof_Parameter133(self):
        return self.__cmof_Parameter133

    @cmof_Parameter133.setter
    def cmof_Parameter133(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Parameter__cmof_Parameter133", None)
        self.__cmof_Parameter133 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_Operation134"):
                opp_val = getattr(old_value, "cmof_Operation134", None)
                if opp_val == self:
                    setattr(old_value, "cmof_Operation134", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_Operation134"):
                opp_val = getattr(value, "cmof_Operation134", None)
                setattr(value, "cmof_Operation134", self)

    def default(self) -> str:
        # TODO: Implement default method
        pass

class Feature:

    pass
class cmof_BehavioralFeature(Feature, Namespace):

    pass
class cmof_StructuralFeature(Feature, TypedElement, MultiplicityElement):

    def __init__(self, isReadOnly: str, cmof_StructuralFeature: "cmof_Slot" = None):
        self.isReadOnly = isReadOnly
        self.cmof_StructuralFeature = cmof_StructuralFeature
        
    @property
    def isReadOnly(self) -> str:
        return self.__isReadOnly

    @isReadOnly.setter
    def isReadOnly(self, isReadOnly: str):
        self.__isReadOnly = isReadOnly

    @property
    def cmof_StructuralFeature(self):
        return self.__cmof_StructuralFeature

    @cmof_StructuralFeature.setter
    def cmof_StructuralFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_StructuralFeature__cmof_StructuralFeature", None)
        self.__cmof_StructuralFeature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_Slot"):
                opp_val = getattr(old_value, "cmof_Slot", None)
                if opp_val == self:
                    setattr(old_value, "cmof_Slot", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_Slot"):
                opp_val = getattr(value, "cmof_Slot", None)
                setattr(value, "cmof_Slot", self)

class cmof_ValueSpecification(TypedElement, PackageableElement):

    def __init__(self, cmof_ValueSpecification: "cmof_Property" = None, cmof_ValueSpecification90: "cmof_Constraint" = None, cmof_ValueSpecification131: "cmof_Parameter" = None, cmof_ValueSpecification139: "cmof_MultiplicityElement" = None, cmof_ValueSpecification136: "cmof_MultiplicityElement" = None, cmof_ValueSpecification166: "cmof_Slot" = None, cmof_ValueSpecification162: "cmof_InstanceSpecification" = None, cmof_ValueSpecification169: "cmof_Expression" = None):
        self.cmof_ValueSpecification = cmof_ValueSpecification
        self.cmof_ValueSpecification90 = cmof_ValueSpecification90
        self.cmof_ValueSpecification131 = cmof_ValueSpecification131
        self.cmof_ValueSpecification139 = cmof_ValueSpecification139
        self.cmof_ValueSpecification136 = cmof_ValueSpecification136
        self.cmof_ValueSpecification166 = cmof_ValueSpecification166
        self.cmof_ValueSpecification162 = cmof_ValueSpecification162
        self.cmof_ValueSpecification169 = cmof_ValueSpecification169
        
    @property
    def cmof_ValueSpecification(self):
        return self.__cmof_ValueSpecification

    @cmof_ValueSpecification.setter
    def cmof_ValueSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_ValueSpecification__cmof_ValueSpecification", None)
        self.__cmof_ValueSpecification = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_Property"):
                opp_val = getattr(old_value, "cmof_Property", None)
                if opp_val == self:
                    setattr(old_value, "cmof_Property", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_Property"):
                opp_val = getattr(value, "cmof_Property", None)
                setattr(value, "cmof_Property", self)

    @property
    def cmof_ValueSpecification166(self):
        return self.__cmof_ValueSpecification166

    @cmof_ValueSpecification166.setter
    def cmof_ValueSpecification166(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_ValueSpecification__cmof_ValueSpecification166", None)
        self.__cmof_ValueSpecification166 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_Slot165"):
                opp_val = getattr(old_value, "cmof_Slot165", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_Slot165"):
                opp_val = getattr(value, "cmof_Slot165", None)
                if opp_val is None:
                    setattr(value, "cmof_Slot165", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cmof_ValueSpecification169(self):
        return self.__cmof_ValueSpecification169

    @cmof_ValueSpecification169.setter
    def cmof_ValueSpecification169(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_ValueSpecification__cmof_ValueSpecification169", None)
        self.__cmof_ValueSpecification169 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_Expression"):
                opp_val = getattr(old_value, "cmof_Expression", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_Expression"):
                opp_val = getattr(value, "cmof_Expression", None)
                if opp_val is None:
                    setattr(value, "cmof_Expression", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cmof_ValueSpecification162(self):
        return self.__cmof_ValueSpecification162

    @cmof_ValueSpecification162.setter
    def cmof_ValueSpecification162(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_ValueSpecification__cmof_ValueSpecification162", None)
        self.__cmof_ValueSpecification162 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_InstanceSpecification161"):
                opp_val = getattr(old_value, "cmof_InstanceSpecification161", None)
                if opp_val == self:
                    setattr(old_value, "cmof_InstanceSpecification161", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_InstanceSpecification161"):
                opp_val = getattr(value, "cmof_InstanceSpecification161", None)
                setattr(value, "cmof_InstanceSpecification161", self)

    @property
    def cmof_ValueSpecification139(self):
        return self.__cmof_ValueSpecification139

    @cmof_ValueSpecification139.setter
    def cmof_ValueSpecification139(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_ValueSpecification__cmof_ValueSpecification139", None)
        self.__cmof_ValueSpecification139 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_MultiplicityElement138"):
                opp_val = getattr(old_value, "cmof_MultiplicityElement138", None)
                if opp_val == self:
                    setattr(old_value, "cmof_MultiplicityElement138", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_MultiplicityElement138"):
                opp_val = getattr(value, "cmof_MultiplicityElement138", None)
                setattr(value, "cmof_MultiplicityElement138", self)

    @property
    def cmof_ValueSpecification90(self):
        return self.__cmof_ValueSpecification90

    @cmof_ValueSpecification90.setter
    def cmof_ValueSpecification90(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_ValueSpecification__cmof_ValueSpecification90", None)
        self.__cmof_ValueSpecification90 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_Constraint89"):
                opp_val = getattr(old_value, "cmof_Constraint89", None)
                if opp_val == self:
                    setattr(old_value, "cmof_Constraint89", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_Constraint89"):
                opp_val = getattr(value, "cmof_Constraint89", None)
                setattr(value, "cmof_Constraint89", self)

    @property
    def cmof_ValueSpecification131(self):
        return self.__cmof_ValueSpecification131

    @cmof_ValueSpecification131.setter
    def cmof_ValueSpecification131(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_ValueSpecification__cmof_ValueSpecification131", None)
        self.__cmof_ValueSpecification131 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_Parameter130"):
                opp_val = getattr(old_value, "cmof_Parameter130", None)
                if opp_val == self:
                    setattr(old_value, "cmof_Parameter130", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_Parameter130"):
                opp_val = getattr(value, "cmof_Parameter130", None)
                setattr(value, "cmof_Parameter130", self)

    @property
    def cmof_ValueSpecification136(self):
        return self.__cmof_ValueSpecification136

    @cmof_ValueSpecification136.setter
    def cmof_ValueSpecification136(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_ValueSpecification__cmof_ValueSpecification136", None)
        self.__cmof_ValueSpecification136 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_MultiplicityElement"):
                opp_val = getattr(old_value, "cmof_MultiplicityElement", None)
                if opp_val == self:
                    setattr(old_value, "cmof_MultiplicityElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_MultiplicityElement"):
                opp_val = getattr(value, "cmof_MultiplicityElement", None)
                setattr(value, "cmof_MultiplicityElement", self)

    def booleanValue(self) -> str:
        # TODO: Implement booleanValue method
        pass

    def integerValue(self) -> str:
        # TODO: Implement integerValue method
        pass

    def isComputable(self) -> str:
        # TODO: Implement isComputable method
        pass

    def unlimitedValue(self) -> str:
        # TODO: Implement unlimitedValue method
        pass

    def isNull(self) -> str:
        # TODO: Implement isNull method
        pass

    def stringValue(self) -> str:
        # TODO: Implement stringValue method
        pass

    def realValue(self) -> str:
        # TODO: Implement realValue method
        pass

class cmof_Association(Classifier, Relationship):

    def __init__(self, isDerived: str, Association: "cmof_Property" = None, Association5: "cmof_Property" = None, cmof_Association148: set["cmof_Property"] = None, owningAssociation: set["cmof_Property"] = None, association: set["cmof_Property"] = None, cmof_Association: set["cmof_Type"] = None, cmof_Association179: "cmof_Link" = None):
        self.isDerived = isDerived
        self.Association = Association
        self.Association5 = Association5
        self.cmof_Association148 = cmof_Association148 if cmof_Association148 is not None else set()
        self.owningAssociation = owningAssociation if owningAssociation is not None else set()
        self.association = association if association is not None else set()
        self.cmof_Association = cmof_Association if cmof_Association is not None else set()
        self.cmof_Association179 = cmof_Association179
        
    @property
    def isDerived(self) -> str:
        return self.__isDerived

    @isDerived.setter
    def isDerived(self, isDerived: str):
        self.__isDerived = isDerived

    @property
    def owningAssociation(self):
        return self.__owningAssociation

    @owningAssociation.setter
    def owningAssociation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Association__owningAssociation", None)
        self.__owningAssociation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Property151"):
                    opp_val = getattr(item, "Property151", None)
                    
                    if opp_val == self:
                        setattr(item, "Property151", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Property151"):
                    opp_val = getattr(item, "Property151", None)
                    
                    setattr(item, "Property151", self)
                    

    @property
    def cmof_Association148(self):
        return self.__cmof_Association148

    @cmof_Association148.setter
    def cmof_Association148(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Association__cmof_Association148", None)
        self.__cmof_Association148 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cmof_Property149"):
                    opp_val = getattr(item, "cmof_Property149", None)
                    
                    if opp_val == self:
                        setattr(item, "cmof_Property149", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cmof_Property149"):
                    opp_val = getattr(item, "cmof_Property149", None)
                    
                    setattr(item, "cmof_Property149", self)
                    

    @property
    def cmof_Association(self):
        return self.__cmof_Association

    @cmof_Association.setter
    def cmof_Association(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Association__cmof_Association", None)
        self.__cmof_Association = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cmof_Type146"):
                    opp_val = getattr(item, "cmof_Type146", None)
                    
                    if opp_val == self:
                        setattr(item, "cmof_Type146", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cmof_Type146"):
                    opp_val = getattr(item, "cmof_Type146", None)
                    
                    setattr(item, "cmof_Type146", self)
                    

    @property
    def association(self):
        return self.__association

    @association.setter
    def association(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Association__association", None)
        self.__association = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Property153"):
                    opp_val = getattr(item, "Property153", None)
                    
                    if opp_val == self:
                        setattr(item, "Property153", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Property153"):
                    opp_val = getattr(item, "Property153", None)
                    
                    setattr(item, "Property153", self)
                    

    @property
    def Association(self):
        return self.__Association

    @Association.setter
    def Association(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Association__Association", None)
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
    def cmof_Association179(self):
        return self.__cmof_Association179

    @cmof_Association179.setter
    def cmof_Association179(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Association__cmof_Association179", None)
        self.__cmof_Association179 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_Link178"):
                opp_val = getattr(old_value, "cmof_Link178", None)
                if opp_val == self:
                    setattr(old_value, "cmof_Link178", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_Link178"):
                opp_val = getattr(value, "cmof_Link178", None)
                setattr(value, "cmof_Link178", self)

    @property
    def Association5(self):
        return self.__Association5

    @Association5.setter
    def Association5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Association__Association5", None)
        self.__Association5 = value
        
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

    def specialized_end_number(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement specialized_end_number method
        pass

    def binary_associations(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement binary_associations method
        pass

    def specialized_end_types(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement specialized_end_types method
        pass

    def endType(self) -> Type:
        # TODO: Implement endType method
        pass

    def association_ends(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement association_ends method
        pass

class cmof_DataType(Classifier):

    pass
class cmof_Class(Classifier):

    def __init__(self, Class: "cmof_Property" = None, cmof_Class: "cmof_Element" = None, cmof_Class34: set["cmof_Classifier"] = None, class: set["cmof_Property"] = None, class38: set["cmof_Operation"] = None, cmof_Class41: "cmof_Class" = None, cmof_Class39: set["cmof_Class"] = None, Class124: "cmof_Operation" = None):
        self.Class = Class
        self.cmof_Class = cmof_Class
        self.cmof_Class34 = cmof_Class34 if cmof_Class34 is not None else set()
        self.class = class if class is not None else set()
        self.class38 = class38 if class38 is not None else set()
        self.cmof_Class41 = cmof_Class41
        self.cmof_Class39 = cmof_Class39 if cmof_Class39 is not None else set()
        self.Class124 = Class124
        
    @property
    def cmof_Class41(self):
        return self.__cmof_Class41

    @cmof_Class41.setter
    def cmof_Class41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Class__cmof_Class41", None)
        self.__cmof_Class41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_Class39"):
                opp_val = getattr(old_value, "cmof_Class39", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_Class39"):
                opp_val = getattr(value, "cmof_Class39", None)
                if opp_val is None:
                    setattr(value, "cmof_Class39", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Class124(self):
        return self.__Class124

    @Class124.setter
    def Class124(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Class__Class124", None)
        self.__Class124 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownedOperation123"):
                opp_val = getattr(old_value, "ownedOperation123", None)
                if opp_val == self:
                    setattr(old_value, "ownedOperation123", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedOperation123"):
                opp_val = getattr(value, "ownedOperation123", None)
                setattr(value, "ownedOperation123", self)

    @property
    def class(self):
        return self.__class

    @class.setter
    def class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Class__class", None)
        self.__class = value if value is not None else set()
        
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
    def class38(self):
        return self.__class38

    @class38.setter
    def class38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Class__class38", None)
        self.__class38 = value if value is not None else set()
        
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
    def Class(self):
        return self.__Class

    @Class.setter
    def Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Class__Class", None)
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
    def cmof_Class39(self):
        return self.__cmof_Class39

    @cmof_Class39.setter
    def cmof_Class39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Class__cmof_Class39", None)
        self.__cmof_Class39 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cmof_Class41"):
                    opp_val = getattr(item, "cmof_Class41", None)
                    
                    if opp_val == self:
                        setattr(item, "cmof_Class41", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cmof_Class41"):
                    opp_val = getattr(item, "cmof_Class41", None)
                    
                    setattr(item, "cmof_Class41", self)
                    

    @property
    def cmof_Class(self):
        return self.__cmof_Class

    @cmof_Class.setter
    def cmof_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Class__cmof_Class", None)
        self.__cmof_Class = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_Element29"):
                opp_val = getattr(old_value, "cmof_Element29", None)
                if opp_val == self:
                    setattr(old_value, "cmof_Element29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_Element29"):
                opp_val = getattr(value, "cmof_Element29", None)
                setattr(value, "cmof_Element29", self)

    @property
    def cmof_Class34(self):
        return self.__cmof_Class34

    @cmof_Class34.setter
    def cmof_Class34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Class__cmof_Class34", None)
        self.__cmof_Class34 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cmof_Classifier35"):
                    opp_val = getattr(item, "cmof_Classifier35", None)
                    
                    if opp_val == self:
                        setattr(item, "cmof_Classifier35", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cmof_Classifier35"):
                    opp_val = getattr(item, "cmof_Classifier35", None)
                    
                    setattr(item, "cmof_Classifier35", self)
                    

    def superClass(self) -> str:
        # TODO: Implement superClass method
        pass

class StructuralFeature:

    pass
class cmof_Property(StructuralFeature):

    def __init__(self, aggregation: str, default: str, isComposite: str, isDerived: str, isDerivedUnion: str, isID: str, ownedAttribute: "cmof_Class" = None, ownedAttribute2: "cmof_DataType" = None, memberEnd: "cmof_Association" = None, ownedEnd: "cmof_Association" = None, cmof_Property: "cmof_ValueSpecification" = None, cmof_Property9: "cmof_Property" = None, cmof_Property7: "cmof_Property" = None, cmof_Property12: "cmof_Property" = None, cmof_Property10: set["cmof_Property"] = None, cmof_Property15: "cmof_Property" = None, cmof_Property13: set["cmof_Property"] = None, Property: "cmof_Class" = None, cmof_Property44: "cmof_Classifier" = None, Property141: "cmof_DataType" = None, cmof_Property149: "cmof_Association" = None, Property151: "cmof_Association" = None, Property153: "cmof_Association" = None):
        self.aggregation = aggregation
        self.default = default
        self.isComposite = isComposite
        self.isDerived = isDerived
        self.isDerivedUnion = isDerivedUnion
        self.isID = isID
        self.ownedAttribute = ownedAttribute
        self.ownedAttribute2 = ownedAttribute2
        self.memberEnd = memberEnd
        self.ownedEnd = ownedEnd
        self.cmof_Property = cmof_Property
        self.cmof_Property9 = cmof_Property9
        self.cmof_Property7 = cmof_Property7
        self.cmof_Property12 = cmof_Property12
        self.cmof_Property10 = cmof_Property10 if cmof_Property10 is not None else set()
        self.cmof_Property15 = cmof_Property15
        self.cmof_Property13 = cmof_Property13 if cmof_Property13 is not None else set()
        self.Property = Property
        self.cmof_Property44 = cmof_Property44
        self.Property141 = Property141
        self.cmof_Property149 = cmof_Property149
        self.Property151 = Property151
        self.Property153 = Property153
        
    @property
    def default(self) -> str:
        return self.__default

    @default.setter
    def default(self, default: str):
        self.__default = default

    @property
    def isID(self) -> str:
        return self.__isID

    @isID.setter
    def isID(self, isID: str):
        self.__isID = isID

    @property
    def isComposite(self) -> str:
        return self.__isComposite

    @isComposite.setter
    def isComposite(self, isComposite: str):
        self.__isComposite = isComposite

    @property
    def isDerived(self) -> str:
        return self.__isDerived

    @isDerived.setter
    def isDerived(self, isDerived: str):
        self.__isDerived = isDerived

    @property
    def isDerivedUnion(self) -> str:
        return self.__isDerivedUnion

    @isDerivedUnion.setter
    def isDerivedUnion(self, isDerivedUnion: str):
        self.__isDerivedUnion = isDerivedUnion

    @property
    def aggregation(self) -> str:
        return self.__aggregation

    @aggregation.setter
    def aggregation(self, aggregation: str):
        self.__aggregation = aggregation

    @property
    def Property151(self):
        return self.__Property151

    @Property151.setter
    def Property151(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Property__Property151", None)
        self.__Property151 = value
        
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
    def memberEnd(self):
        return self.__memberEnd

    @memberEnd.setter
    def memberEnd(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Property__memberEnd", None)
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
    def cmof_Property12(self):
        return self.__cmof_Property12

    @cmof_Property12.setter
    def cmof_Property12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Property__cmof_Property12", None)
        self.__cmof_Property12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_Property10"):
                opp_val = getattr(old_value, "cmof_Property10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_Property10"):
                opp_val = getattr(value, "cmof_Property10", None)
                if opp_val is None:
                    setattr(value, "cmof_Property10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cmof_Property149(self):
        return self.__cmof_Property149

    @cmof_Property149.setter
    def cmof_Property149(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Property__cmof_Property149", None)
        self.__cmof_Property149 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_Association148"):
                opp_val = getattr(old_value, "cmof_Association148", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_Association148"):
                opp_val = getattr(value, "cmof_Association148", None)
                if opp_val is None:
                    setattr(value, "cmof_Association148", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cmof_Property10(self):
        return self.__cmof_Property10

    @cmof_Property10.setter
    def cmof_Property10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Property__cmof_Property10", None)
        self.__cmof_Property10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cmof_Property12"):
                    opp_val = getattr(item, "cmof_Property12", None)
                    
                    if opp_val == self:
                        setattr(item, "cmof_Property12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cmof_Property12"):
                    opp_val = getattr(item, "cmof_Property12", None)
                    
                    setattr(item, "cmof_Property12", self)
                    

    @property
    def cmof_Property15(self):
        return self.__cmof_Property15

    @cmof_Property15.setter
    def cmof_Property15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Property__cmof_Property15", None)
        self.__cmof_Property15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_Property13"):
                opp_val = getattr(old_value, "cmof_Property13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_Property13"):
                opp_val = getattr(value, "cmof_Property13", None)
                if opp_val is None:
                    setattr(value, "cmof_Property13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ownedAttribute2(self):
        return self.__ownedAttribute2

    @ownedAttribute2.setter
    def ownedAttribute2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Property__ownedAttribute2", None)
        self.__ownedAttribute2 = value
        
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
    def cmof_Property(self):
        return self.__cmof_Property

    @cmof_Property.setter
    def cmof_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Property__cmof_Property", None)
        self.__cmof_Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_ValueSpecification"):
                opp_val = getattr(old_value, "cmof_ValueSpecification", None)
                if opp_val == self:
                    setattr(old_value, "cmof_ValueSpecification", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_ValueSpecification"):
                opp_val = getattr(value, "cmof_ValueSpecification", None)
                setattr(value, "cmof_ValueSpecification", self)

    @property
    def Property(self):
        return self.__Property

    @Property.setter
    def Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Property__Property", None)
        self.__Property = value
        
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
    def ownedAttribute(self):
        return self.__ownedAttribute

    @ownedAttribute.setter
    def ownedAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Property__ownedAttribute", None)
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
    def cmof_Property44(self):
        return self.__cmof_Property44

    @cmof_Property44.setter
    def cmof_Property44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Property__cmof_Property44", None)
        self.__cmof_Property44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_Classifier43"):
                opp_val = getattr(old_value, "cmof_Classifier43", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_Classifier43"):
                opp_val = getattr(value, "cmof_Classifier43", None)
                if opp_val is None:
                    setattr(value, "cmof_Classifier43", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cmof_Property13(self):
        return self.__cmof_Property13

    @cmof_Property13.setter
    def cmof_Property13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Property__cmof_Property13", None)
        self.__cmof_Property13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cmof_Property15"):
                    opp_val = getattr(item, "cmof_Property15", None)
                    
                    if opp_val == self:
                        setattr(item, "cmof_Property15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cmof_Property15"):
                    opp_val = getattr(item, "cmof_Property15", None)
                    
                    setattr(item, "cmof_Property15", self)
                    

    @property
    def cmof_Property7(self):
        return self.__cmof_Property7

    @cmof_Property7.setter
    def cmof_Property7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Property__cmof_Property7", None)
        self.__cmof_Property7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_Property9"):
                opp_val = getattr(old_value, "cmof_Property9", None)
                if opp_val == self:
                    setattr(old_value, "cmof_Property9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_Property9"):
                opp_val = getattr(value, "cmof_Property9", None)
                setattr(value, "cmof_Property9", self)

    @property
    def ownedEnd(self):
        return self.__ownedEnd

    @ownedEnd.setter
    def ownedEnd(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Property__ownedEnd", None)
        self.__ownedEnd = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Association5"):
                opp_val = getattr(old_value, "Association5", None)
                if opp_val == self:
                    setattr(old_value, "Association5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Association5"):
                opp_val = getattr(value, "Association5", None)
                setattr(value, "Association5", self)

    @property
    def Property141(self):
        return self.__Property141

    @Property141.setter
    def Property141(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Property__Property141", None)
        self.__Property141 = value
        
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
    def Property153(self):
        return self.__Property153

    @Property153.setter
    def Property153(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Property__Property153", None)
        self.__Property153 = value
        
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
    def cmof_Property9(self):
        return self.__cmof_Property9

    @cmof_Property9.setter
    def cmof_Property9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Property__cmof_Property9", None)
        self.__cmof_Property9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_Property7"):
                opp_val = getattr(old_value, "cmof_Property7", None)
                if opp_val == self:
                    setattr(old_value, "cmof_Property7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_Property7"):
                opp_val = getattr(value, "cmof_Property7", None)
                setattr(value, "cmof_Property7", self)

    def subsetting_context_conforms(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement subsetting_context_conforms method
        pass

    def default(self) -> str:
        # TODO: Implement default method
        pass

    def derived_union_is_read_only(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement derived_union_is_read_only method
        pass

    def isAttribute(self, p: str) -> str:
        # TODO: Implement isAttribute method
        pass

    def subsetted_property_names(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement subsetted_property_names method
        pass

    def subsetting_rules(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement subsetting_rules method
        pass

    def opposite(self) -> str:
        # TODO: Implement opposite method
        pass

    def subsettingContext(self) -> str:
        # TODO: Implement subsettingContext method
        pass

    def multiplicity_of_composite(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement multiplicity_of_composite method
        pass

    def isComposite(self) -> str:
        # TODO: Implement isComposite method
        pass

    def derived_union_is_derived(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement derived_union_is_derived method
        pass

    def isNavigable(self) -> str:
        # TODO: Implement isNavigable method
        pass

    def redefined_property_inherited(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement redefined_property_inherited method
        pass

class cmof_Object:

    def __init__(self, cmof_Object: "cmof_Argument" = None):
        self.cmof_Object = cmof_Object
        
    @property
    def cmof_Object(self):
        return self.__cmof_Object

    @cmof_Object.setter
    def cmof_Object(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Object__cmof_Object", None)
        self.__cmof_Object = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_Argument"):
                opp_val = getattr(old_value, "cmof_Argument", None)
                if opp_val == self:
                    setattr(old_value, "cmof_Argument", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_Argument"):
                opp_val = getattr(value, "cmof_Argument", None)
                setattr(value, "cmof_Argument", self)

    def get(self, property: str) -> Object:
        # TODO: Implement get method
        pass

    def invoke(self, op: str, arguments: str) -> Object:
        # TODO: Implement invoke method
        pass

    def set(self, value: Object, property: str):
        # TODO: Implement set method
        pass

    def isSet(self, property: str) -> str:
        # TODO: Implement isSet method
        pass

    def equals(self, element: Object) -> str:
        # TODO: Implement equals method
        pass

    def unset(self, property: str):
        # TODO: Implement unset method
        pass

class Object:

    pass
class cmof_Element(Object):

    def __init__(self, cmof_Element: set["cmof_Comment"] = None, Element: "cmof_Element" = None, owner: set["cmof_Element"] = None, Element27: "cmof_Element" = None, ownedElement: "cmof_Element" = None, cmof_Element29: "cmof_Class" = None, cmof_Element32: "cmof_Comment" = None, cmof_Element83: "cmof_DirectedRelationship" = None, cmof_Element85: "cmof_Relationship" = None, cmof_Element80: "cmof_DirectedRelationship" = None, cmof_Element87: "cmof_Constraint" = None, cmof_Element173: "cmof_Link" = None, cmof_Element176: "cmof_Link" = None, cmof_Element188: "cmof_Tag" = None, cmof_Element191: "cmof_Tag" = None, cmof_Element183: "cmof_Exception" = None, cmof_Element186: "cmof_Exception" = None):
        self.cmof_Element = cmof_Element if cmof_Element is not None else set()
        self.Element = Element
        self.owner = owner if owner is not None else set()
        self.Element27 = Element27
        self.ownedElement = ownedElement
        self.cmof_Element29 = cmof_Element29
        self.cmof_Element32 = cmof_Element32
        self.cmof_Element83 = cmof_Element83
        self.cmof_Element85 = cmof_Element85
        self.cmof_Element80 = cmof_Element80
        self.cmof_Element87 = cmof_Element87
        self.cmof_Element173 = cmof_Element173
        self.cmof_Element176 = cmof_Element176
        self.cmof_Element188 = cmof_Element188
        self.cmof_Element191 = cmof_Element191
        self.cmof_Element183 = cmof_Element183
        self.cmof_Element186 = cmof_Element186
        
    @property
    def Element27(self):
        return self.__Element27

    @Element27.setter
    def Element27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Element__Element27", None)
        self.__Element27 = value
        
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
    def cmof_Element188(self):
        return self.__cmof_Element188

    @cmof_Element188.setter
    def cmof_Element188(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Element__cmof_Element188", None)
        self.__cmof_Element188 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_Tag"):
                opp_val = getattr(old_value, "cmof_Tag", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_Tag"):
                opp_val = getattr(value, "cmof_Tag", None)
                if opp_val is None:
                    setattr(value, "cmof_Tag", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ownedElement(self):
        return self.__ownedElement

    @ownedElement.setter
    def ownedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Element__ownedElement", None)
        self.__ownedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Element27"):
                opp_val = getattr(old_value, "Element27", None)
                if opp_val == self:
                    setattr(old_value, "Element27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Element27"):
                opp_val = getattr(value, "Element27", None)
                setattr(value, "Element27", self)

    @property
    def cmof_Element186(self):
        return self.__cmof_Element186

    @cmof_Element186.setter
    def cmof_Element186(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Element__cmof_Element186", None)
        self.__cmof_Element186 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_Exception185"):
                opp_val = getattr(old_value, "cmof_Exception185", None)
                if opp_val == self:
                    setattr(old_value, "cmof_Exception185", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_Exception185"):
                opp_val = getattr(value, "cmof_Exception185", None)
                setattr(value, "cmof_Exception185", self)

    @property
    def cmof_Element85(self):
        return self.__cmof_Element85

    @cmof_Element85.setter
    def cmof_Element85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Element__cmof_Element85", None)
        self.__cmof_Element85 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_Relationship"):
                opp_val = getattr(old_value, "cmof_Relationship", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_Relationship"):
                opp_val = getattr(value, "cmof_Relationship", None)
                if opp_val is None:
                    setattr(value, "cmof_Relationship", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Element(self):
        return self.__Element

    @Element.setter
    def Element(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Element__Element", None)
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
    def cmof_Element83(self):
        return self.__cmof_Element83

    @cmof_Element83.setter
    def cmof_Element83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Element__cmof_Element83", None)
        self.__cmof_Element83 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_DirectedRelationship82"):
                opp_val = getattr(old_value, "cmof_DirectedRelationship82", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_DirectedRelationship82"):
                opp_val = getattr(value, "cmof_DirectedRelationship82", None)
                if opp_val is None:
                    setattr(value, "cmof_DirectedRelationship82", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cmof_Element80(self):
        return self.__cmof_Element80

    @cmof_Element80.setter
    def cmof_Element80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Element__cmof_Element80", None)
        self.__cmof_Element80 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_DirectedRelationship"):
                opp_val = getattr(old_value, "cmof_DirectedRelationship", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_DirectedRelationship"):
                opp_val = getattr(value, "cmof_DirectedRelationship", None)
                if opp_val is None:
                    setattr(value, "cmof_DirectedRelationship", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cmof_Element176(self):
        return self.__cmof_Element176

    @cmof_Element176.setter
    def cmof_Element176(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Element__cmof_Element176", None)
        self.__cmof_Element176 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_Link175"):
                opp_val = getattr(old_value, "cmof_Link175", None)
                if opp_val == self:
                    setattr(old_value, "cmof_Link175", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_Link175"):
                opp_val = getattr(value, "cmof_Link175", None)
                setattr(value, "cmof_Link175", self)

    @property
    def cmof_Element173(self):
        return self.__cmof_Element173

    @cmof_Element173.setter
    def cmof_Element173(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Element__cmof_Element173", None)
        self.__cmof_Element173 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_Link"):
                opp_val = getattr(old_value, "cmof_Link", None)
                if opp_val == self:
                    setattr(old_value, "cmof_Link", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_Link"):
                opp_val = getattr(value, "cmof_Link", None)
                setattr(value, "cmof_Link", self)

    @property
    def cmof_Element191(self):
        return self.__cmof_Element191

    @cmof_Element191.setter
    def cmof_Element191(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Element__cmof_Element191", None)
        self.__cmof_Element191 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_Tag190"):
                opp_val = getattr(old_value, "cmof_Tag190", None)
                if opp_val == self:
                    setattr(old_value, "cmof_Tag190", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_Tag190"):
                opp_val = getattr(value, "cmof_Tag190", None)
                setattr(value, "cmof_Tag190", self)

    @property
    def cmof_Element87(self):
        return self.__cmof_Element87

    @cmof_Element87.setter
    def cmof_Element87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Element__cmof_Element87", None)
        self.__cmof_Element87 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_Constraint"):
                opp_val = getattr(old_value, "cmof_Constraint", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_Constraint"):
                opp_val = getattr(value, "cmof_Constraint", None)
                if opp_val is None:
                    setattr(value, "cmof_Constraint", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cmof_Element29(self):
        return self.__cmof_Element29

    @cmof_Element29.setter
    def cmof_Element29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Element__cmof_Element29", None)
        self.__cmof_Element29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_Class"):
                opp_val = getattr(old_value, "cmof_Class", None)
                if opp_val == self:
                    setattr(old_value, "cmof_Class", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_Class"):
                opp_val = getattr(value, "cmof_Class", None)
                setattr(value, "cmof_Class", self)

    @property
    def cmof_Element183(self):
        return self.__cmof_Element183

    @cmof_Element183.setter
    def cmof_Element183(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Element__cmof_Element183", None)
        self.__cmof_Element183 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_Exception"):
                opp_val = getattr(old_value, "cmof_Exception", None)
                if opp_val == self:
                    setattr(old_value, "cmof_Exception", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_Exception"):
                opp_val = getattr(value, "cmof_Exception", None)
                setattr(value, "cmof_Exception", self)

    @property
    def cmof_Element32(self):
        return self.__cmof_Element32

    @cmof_Element32.setter
    def cmof_Element32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Element__cmof_Element32", None)
        self.__cmof_Element32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_Comment31"):
                opp_val = getattr(old_value, "cmof_Comment31", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_Comment31"):
                opp_val = getattr(value, "cmof_Comment31", None)
                if opp_val is None:
                    setattr(value, "cmof_Comment31", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cmof_Element(self):
        return self.__cmof_Element

    @cmof_Element.setter
    def cmof_Element(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Element__cmof_Element", None)
        self.__cmof_Element = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cmof_Comment"):
                    opp_val = getattr(item, "cmof_Comment", None)
                    
                    if opp_val == self:
                        setattr(item, "cmof_Comment", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cmof_Comment"):
                    opp_val = getattr(item, "cmof_Comment", None)
                    
                    setattr(item, "cmof_Comment", self)
                    

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Element__owner", None)
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
                    

    def getMetaClass(self) -> str:
        # TODO: Implement getMetaClass method
        pass

    def container(self) -> Element:
        # TODO: Implement container method
        pass

    def mustBeOwned(self) -> str:
        # TODO: Implement mustBeOwned method
        pass

    def has_owner(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement has_owner method
        pass

    def isInstanceOfType(self, includesSubtypes: str, type: str) -> str:
        # TODO: Implement isInstanceOfType method
        pass

    def allOwnedElements(self) -> Element:
        # TODO: Implement allOwnedElements method
        pass

    def not_own_self(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement not_own_self method
        pass

    def delete(self):
        # TODO: Implement delete method
        pass

class cmof_Extent(Object):

    def __init__(self):
        
    def elementsOfType(self, includesSubtypes: str, type: str) -> Element:
        # TODO: Implement elementsOfType method
        pass

    def elements(self) -> str:
        # TODO: Implement elements method
        pass

    def linksOfType(self, type: str) -> str:
        # TODO: Implement linksOfType method
        pass

    def linkExists(self, firstElement: Element, association: str, secondElement: Element) -> str:
        # TODO: Implement linkExists method
        pass

    def useContainment(self) -> str:
        # TODO: Implement useContainment method
        pass

    def linkedElements(self, association: str, endElement: Element, end1ToEnd2Direction: str) -> Element:
        # TODO: Implement linkedElements method
        pass

class cmof_Link(Object):

    def __init__(self, cmof_Link: "cmof_Element" = None, cmof_Link175: "cmof_Element" = None, cmof_Link178: "cmof_Association" = None):
        self.cmof_Link = cmof_Link
        self.cmof_Link175 = cmof_Link175
        self.cmof_Link178 = cmof_Link178
        
    @property
    def cmof_Link175(self):
        return self.__cmof_Link175

    @cmof_Link175.setter
    def cmof_Link175(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Link__cmof_Link175", None)
        self.__cmof_Link175 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_Element176"):
                opp_val = getattr(old_value, "cmof_Element176", None)
                if opp_val == self:
                    setattr(old_value, "cmof_Element176", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_Element176"):
                opp_val = getattr(value, "cmof_Element176", None)
                setattr(value, "cmof_Element176", self)

    @property
    def cmof_Link178(self):
        return self.__cmof_Link178

    @cmof_Link178.setter
    def cmof_Link178(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Link__cmof_Link178", None)
        self.__cmof_Link178 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_Association179"):
                opp_val = getattr(old_value, "cmof_Association179", None)
                if opp_val == self:
                    setattr(old_value, "cmof_Association179", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_Association179"):
                opp_val = getattr(value, "cmof_Association179", None)
                setattr(value, "cmof_Association179", self)

    @property
    def cmof_Link(self):
        return self.__cmof_Link

    @cmof_Link.setter
    def cmof_Link(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cmof_Link__cmof_Link", None)
        self.__cmof_Link = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cmof_Element173"):
                opp_val = getattr(old_value, "cmof_Element173", None)
                if opp_val == self:
                    setattr(old_value, "cmof_Element173", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cmof_Element173"):
                opp_val = getattr(value, "cmof_Element173", None)
                setattr(value, "cmof_Element173", self)

    def equals(self, otherLink: str) -> str:
        # TODO: Implement equals method
        pass

    def delete(self):
        # TODO: Implement delete method
        pass

class cmof_ReflectiveCollection(Object):

    def __init__(self):
        
    def add(self, object: Object) -> str:
        # TODO: Implement add method
        pass

    def addAll(self, objects: ReflectiveCollection) -> str:
        # TODO: Implement addAll method
        pass

    def size(self) -> str:
        # TODO: Implement size method
        pass

    def clear(self):
        # TODO: Implement clear method
        pass

    def remove(self, object: Object) -> str:
        # TODO: Implement remove method
        pass

class ReflectiveCollection:

    pass
class cmof_ReflectiveSequence(ReflectiveCollection):

    def __init__(self):
        
    def get(self, index: str) -> str:
        # TODO: Implement get method
        pass

    def remove(self, index: str) -> str:
        # TODO: Implement remove method
        pass

    def add(self, index: str, object: str):
        # TODO: Implement add method
        pass

    def set(self, object: str, index: str) -> str:
        # TODO: Implement set method
        pass
