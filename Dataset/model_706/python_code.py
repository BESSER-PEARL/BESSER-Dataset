from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class CollectionKind(Enum):
    Set = "Set"
    OrderedSet = "OrderedSet"
    Bag = "Bag"
    Sequence = "Sequence"
    Collection = "Collection"
class DirectionKind(Enum):
    in_ = "in_"
    inout = "inout"
    out = "out"
class EnforcementMode(Enum):
    Creation = "Creation"
    Deletion = "Deletion"
class ImportKind(Enum):
    extension = "extension"
    access = "access"
class SeverityKind(Enum):
    error = "error"
    warning = "warning"
    fatal = "fatal"


############################################
# Definition of Classes
############################################

class LetExp:

    pass
class Extent:

    pass
class FlatQVT_URIExtent(Extent):

    def __init__(self):
        
        pass
    def uri(self, FlatQVT_element) :
        # TODO: Implement uri method
        pass

    def contextURI(self) :
        # TODO: Implement contextURI method
        pass

    def element(self, FlatQVT_uri) :
        # TODO: Implement element method
        pass

class TupleLiteralExp:

    pass
class TupleLiteralPart:

    pass
class CatchExp:

    pass
class AltExp:

    pass
class ResolveExp:

    pass
class FlatQVT_ResolveInExp(ResolveExp):

    pass
class DomainPattern:

    pass
class RelationDomainAssignment:

    pass
class Key:

    pass
class Transformation:

    pass
class FlatQVT_RelationalTransformation(Transformation):

    pass
class ReflectiveCollection:

    pass
class FlatQVT_ReflectiveSequence(ReflectiveCollection):

    def __init__(self):
        
        pass
    def remove(self, FlatQVT_index) :
        # TODO: Implement remove method
        pass

    def set(self, FlatQVT_object, FlatQVT_index) :
        # TODO: Implement set method
        pass

    def add(self, FlatQVT_index, FlatQVT_object):
        # TODO: Implement add method
        pass

    def get(self, FlatQVT_index) :
        # TODO: Implement get method
        pass

class RelationImplementation:

    pass
class NavigationCallExp:

    pass
class FlatQVT_PropertyCallExp(NavigationCallExp):

    pass
class ObjectTemplateExp:

    pass
class Predicate:

    pass
class OrderedTupleLiteralPart:

    pass
class PropertyCallExp:

    pass
class FlatQVT_OppositePropertyCallExp(PropertyCallExp):

    pass
class ConstructorBody:

    pass
class InstantiationExp:

    pass
class FlatQVT_ObjectExp(InstantiationExp):

    pass
class FlatQVT_Object:

    pass
class MultiplicityElement:

    pass
class PropertyTemplateItem:

    pass
class ModuleImport:

    pass
class EntryOperation:

    pass
class FeatureCallExp:

    pass
class FlatQVT_OperationCallExp(FeatureCallExp):

    pass
class FlatQVT_NavigationCallExp(FeatureCallExp):

    pass
class FlatQVT_MultiplicityElement(ABC):

    def __init__(self, isOrdered: str, isUnique: str, lower: str, upper: str):
        self.isOrdered = isOrdered
        self.isUnique = isUnique
        self.lower = lower
        self.upper = upper
        
        pass
    @property
    def lower(self):
        return self.__lower

    @lower.setter
    def lower(self, lower: str):
        self.__lower = lower


    @property
    def isUnique(self):
        return self.__isUnique

    @isUnique.setter
    def isUnique(self, isUnique: str):
        self.__isUnique = isUnique


    @property
    def upper(self):
        return self.__upper

    @upper.setter
    def upper(self, upper: str):
        self.__upper = upper


    @property
    def isOrdered(self):
        return self.__isOrdered

    @isOrdered.setter
    def isOrdered(self, isOrdered: str):
        self.__isOrdered = isOrdered


class ModelType:

    pass
class Tag:

    pass
class MappingOperation:

    pass
class ImperativeCallExp:

    pass
class FlatQVT_MappingCallExp(ImperativeCallExp):

    def __init__(self, isStrict: str):
        self.isStrict = isStrict
        
        pass
    @property
    def isStrict(self):
        return self.__isStrict

    @isStrict.setter
    def isStrict(self, isStrict: str):
        self.__isStrict = isStrict


class RelationDomain:

    pass
class ModelParameter:

    pass
class Mapping:

    pass
class NumericLiteralExp:

    pass
class FlatQVT_UnlimitedNaturalExp(NumericLiteralExp):

    def __init__(self, symbol: str):
        self.symbol = symbol
        
        pass
    @property
    def symbol(self):
        return self.__symbol

    @symbol.setter
    def symbol(self, symbol: str):
        self.__symbol = symbol


class FlatQVT_RealLiteralExp(NumericLiteralExp):

    def __init__(self, realSymbol: str):
        self.realSymbol = realSymbol
        
        pass
    @property
    def realSymbol(self):
        return self.__realSymbol

    @realSymbol.setter
    def realSymbol(self, realSymbol: str):
        self.__realSymbol = realSymbol


class FlatQVT_IntegerLiteralExp(NumericLiteralExp):

    def __init__(self, integerSymbol: str):
        self.integerSymbol = integerSymbol
        
        pass
    @property
    def integerSymbol(self):
        return self.__integerSymbol

    @integerSymbol.setter
    def integerSymbol(self, integerSymbol: str):
        self.__integerSymbol = integerSymbol


class Module:

    pass
class FlatQVT_OperationalTransformation(Module):

    pass
class FlatQVT_Library(Module):

    pass
class RelationalTransformation:

    pass
class VarParameter:

    pass
class FlatQVT_ModelParameter(VarParameter):

    pass
class LoopExp:

    pass
class FlatQVT_IterateExp(LoopExp):

    pass
class FlatQVT_IteratorExp(LoopExp):

    pass
class Parameter:

    pass
class ImperativeLoopExp:

    pass
class FlatQVT_ImperativeIterateExp(ImperativeLoopExp):

    pass
class FlatQVT_ForExp(ImperativeLoopExp):

    pass
class CallExp:

    pass
class FlatQVT_FeatureCallExp(CallExp):

    pass
class Package:

    pass
class Comment:

    pass
class Enumeration:

    pass
class EnumerationLiteral:

    pass
class OperationCallExp:

    pass
class DictLiteralPart:

    pass
class Object:

    pass
class FlatQVT_Extent(Object):

    def __init__(self):
        
        pass
    def elements(self) :
        # TODO: Implement elements method
        pass

    def useContainment(self) :
        # TODO: Implement useContainment method
        pass

class FlatQVT_ReflectiveCollection(Object):

    def __init__(self):
        
        pass
    def size(self) :
        # TODO: Implement size method
        pass

    def remove(self, FlatQVT_object) :
        # TODO: Implement remove method
        pass

    def clear(self):
        # TODO: Implement clear method
        pass

    def add(self, FlatQVT_object) :
        # TODO: Implement add method
        pass

    def addAll(self, FlatQVT_objects) :
        # TODO: Implement addAll method
        pass

class FlatQVT_Element(Object):

    def __init__(self, FlatQVT_Element: set["Comment"] = None):
        self.FlatQVT_Element = FlatQVT_Element if FlatQVT_Element is not None else set()
        
        pass
    @property
    def FlatQVT_Element(self):
        return self.__FlatQVT_Element

    @FlatQVT_Element.setter
    def FlatQVT_Element(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FlatQVT_Element__FlatQVT_Element", None)
        self.__FlatQVT_Element = value if value is not None else set()
        
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
                    

    def set(self, FlatQVT_property, FlatQVT_object):
        # TODO: Implement set method
        pass

    def isSet(self, FlatQVT_property) :
        # TODO: Implement isSet method
        pass

    def equals(self, FlatQVT_object) :
        # TODO: Implement equals method
        pass

    def unset(self, FlatQVT_property):
        # TODO: Implement unset method
        pass

    def get(self, FlatQVT_property) :
        # TODO: Implement get method
        pass

    def getMetaClass(self) :
        # TODO: Implement getMetaClass method
        pass

    def container(self) :
        # TODO: Implement container method
        pass

class TypedModel:

    pass
class Rule:

    pass
class FlatQVT_Relation(Rule):

    def __init__(self, isTopLevel: str, FlatQVT_Relation: set["RelationImplementation"] = None, FlatQVT_Relation320: set["Variable"] = None, FlatQVT_Relation323: "Pattern" = None, FlatQVT_Relation326: "Pattern" = None, Rule: "FlatQVT_Domain" = None, Rule365: "FlatQVT_Rule" = None, Rule388: "FlatQVT_Transformation" = None):
        self.isTopLevel = isTopLevel
        self.FlatQVT_Relation = FlatQVT_Relation if FlatQVT_Relation is not None else set()
        self.FlatQVT_Relation320 = FlatQVT_Relation320 if FlatQVT_Relation320 is not None else set()
        self.FlatQVT_Relation323 = FlatQVT_Relation323
        self.FlatQVT_Relation326 = FlatQVT_Relation326
        
        pass
    @property
    def isTopLevel(self):
        return self.__isTopLevel

    @isTopLevel.setter
    def isTopLevel(self, isTopLevel: str):
        self.__isTopLevel = isTopLevel


    @property
    def FlatQVT_Relation320(self):
        return self.__FlatQVT_Relation320

    @FlatQVT_Relation320.setter
    def FlatQVT_Relation320(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FlatQVT_Relation__FlatQVT_Relation320", None)
        self.__FlatQVT_Relation320 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Variable321"):
                    opp_val = getattr(item, "Variable321", None)
                    
                    if opp_val == self:
                        setattr(item, "Variable321", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Variable321"):
                    opp_val = getattr(item, "Variable321", None)
                    
                    setattr(item, "Variable321", self)
                    

    @property
    def FlatQVT_Relation323(self):
        return self.__FlatQVT_Relation323

    @FlatQVT_Relation323.setter
    def FlatQVT_Relation323(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FlatQVT_Relation__FlatQVT_Relation323", None)
        self.__FlatQVT_Relation323 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Pattern324"):
                opp_val = getattr(old_value, "Pattern324", None)
                if opp_val == self:
                    setattr(old_value, "Pattern324", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Pattern324"):
                opp_val = getattr(value, "Pattern324", None)
                setattr(value, "Pattern324", self)

    @property
    def FlatQVT_Relation(self):
        return self.__FlatQVT_Relation

    @FlatQVT_Relation.setter
    def FlatQVT_Relation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FlatQVT_Relation__FlatQVT_Relation", None)
        self.__FlatQVT_Relation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RelationImplementation"):
                    opp_val = getattr(item, "RelationImplementation", None)
                    
                    if opp_val == self:
                        setattr(item, "RelationImplementation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RelationImplementation"):
                    opp_val = getattr(item, "RelationImplementation", None)
                    
                    setattr(item, "RelationImplementation", self)
                    

    @property
    def FlatQVT_Relation326(self):
        return self.__FlatQVT_Relation326

    @FlatQVT_Relation326.setter
    def FlatQVT_Relation326(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FlatQVT_Relation__FlatQVT_Relation326", None)
        self.__FlatQVT_Relation326 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Pattern327"):
                opp_val = getattr(old_value, "Pattern327", None)
                if opp_val == self:
                    setattr(old_value, "Pattern327", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Pattern327"):
                opp_val = getattr(value, "Pattern327", None)
                setattr(value, "Pattern327", self)

class NamedElement:

    pass
class FlatQVT_TypedElement(NamedElement):

    pass
class FlatQVT_Package(NamedElement):

    def __init__(self, uri: str, FlatQVT_Package: set["Package"] = None, FlatQVT_Package279: "Package" = None, FlatQVT_Package282: set["Type"] = None, NamedElement: "FlatQVT_Comment" = None):
        self.uri = uri
        self.FlatQVT_Package = FlatQVT_Package if FlatQVT_Package is not None else set()
        self.FlatQVT_Package279 = FlatQVT_Package279
        self.FlatQVT_Package282 = FlatQVT_Package282 if FlatQVT_Package282 is not None else set()
        
        pass
    @property
    def uri(self):
        return self.__uri

    @uri.setter
    def uri(self, uri: str):
        self.__uri = uri


    @property
    def FlatQVT_Package282(self):
        return self.__FlatQVT_Package282

    @FlatQVT_Package282.setter
    def FlatQVT_Package282(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FlatQVT_Package__FlatQVT_Package282", None)
        self.__FlatQVT_Package282 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Type283"):
                    opp_val = getattr(item, "Type283", None)
                    
                    if opp_val == self:
                        setattr(item, "Type283", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Type283"):
                    opp_val = getattr(item, "Type283", None)
                    
                    setattr(item, "Type283", self)
                    

    @property
    def FlatQVT_Package279(self):
        return self.__FlatQVT_Package279

    @FlatQVT_Package279.setter
    def FlatQVT_Package279(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FlatQVT_Package__FlatQVT_Package279", None)
        self.__FlatQVT_Package279 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Package280"):
                opp_val = getattr(old_value, "Package280", None)
                if opp_val == self:
                    setattr(old_value, "Package280", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Package280"):
                opp_val = getattr(value, "Package280", None)
                setattr(value, "Package280", self)

    @property
    def FlatQVT_Package(self):
        return self.__FlatQVT_Package

    @FlatQVT_Package.setter
    def FlatQVT_Package(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FlatQVT_Package__FlatQVT_Package", None)
        self.__FlatQVT_Package = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Package277"):
                    opp_val = getattr(item, "Package277", None)
                    
                    if opp_val == self:
                        setattr(item, "Package277", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Package277"):
                    opp_val = getattr(item, "Package277", None)
                    
                    setattr(item, "Package277", self)
                    

class FlatQVT_Rule(NamedElement):

    pass
class FlatQVT_Type(NamedElement):

    def __init__(self, FlatQVT_Type: "Package" = None, NamedElement: "FlatQVT_Comment" = None):
        self.FlatQVT_Type = FlatQVT_Type
        
        pass
    @property
    def FlatQVT_Type(self):
        return self.__FlatQVT_Type

    @FlatQVT_Type.setter
    def FlatQVT_Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FlatQVT_Type__FlatQVT_Type", None)
        self.__FlatQVT_Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Package402"):
                opp_val = getattr(old_value, "Package402", None)
                if opp_val == self:
                    setattr(old_value, "Package402", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Package402"):
                opp_val = getattr(value, "Package402", None)
                setattr(value, "Package402", self)

    def isInstance(self, FlatQVT_object) :
        # TODO: Implement isInstance method
        pass

class FlatQVT_TypedModel(NamedElement):

    pass
class FlatQVT_Domain(NamedElement):

    def __init__(self, isCheckable: str, isEnforceable: str, FlatQVT_Domain: "Rule" = None, FlatQVT_Domain87: "TypedModel" = None, NamedElement: "FlatQVT_Comment" = None):
        self.isCheckable = isCheckable
        self.isEnforceable = isEnforceable
        self.FlatQVT_Domain = FlatQVT_Domain
        self.FlatQVT_Domain87 = FlatQVT_Domain87
        
        pass
    @property
    def isEnforceable(self):
        return self.__isEnforceable

    @isEnforceable.setter
    def isEnforceable(self, isEnforceable: str):
        self.__isEnforceable = isEnforceable


    @property
    def isCheckable(self):
        return self.__isCheckable

    @isCheckable.setter
    def isCheckable(self, isCheckable: str):
        self.__isCheckable = isCheckable


    @property
    def FlatQVT_Domain87(self):
        return self.__FlatQVT_Domain87

    @FlatQVT_Domain87.setter
    def FlatQVT_Domain87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FlatQVT_Domain__FlatQVT_Domain87", None)
        self.__FlatQVT_Domain87 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TypedModel"):
                opp_val = getattr(old_value, "TypedModel", None)
                if opp_val == self:
                    setattr(old_value, "TypedModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TypedModel"):
                opp_val = getattr(value, "TypedModel", None)
                setattr(value, "TypedModel", self)

    @property
    def FlatQVT_Domain(self):
        return self.__FlatQVT_Domain

    @FlatQVT_Domain.setter
    def FlatQVT_Domain(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FlatQVT_Domain__FlatQVT_Domain", None)
        self.__FlatQVT_Domain = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Rule"):
                opp_val = getattr(old_value, "Rule", None)
                if opp_val == self:
                    setattr(old_value, "Rule", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Rule"):
                opp_val = getattr(value, "Rule", None)
                setattr(value, "Rule", self)

class FlatQVT_EnumerationLiteral(NamedElement):

    pass
class DataType:

    pass
class FlatQVT_Enumeration(DataType):

    pass
class FlatQVT_PrimitiveType(DataType):

    pass
class FlatQVT_CollectionType(DataType):

    pass
class Pattern:

    pass
class FlatQVT_DomainPattern(Pattern):

    pass
class FlatQVT_CorePattern(Pattern):

    pass
class Domain:

    pass
class FlatQVT_RelationDomain(Domain):

    pass
class Variable:

    pass
class FlatQVT_VarParameter(Parameter, Variable):

    def __init__(self, kind: str, FlatQVT_VarParameter: "ImperativeOperation" = None, FlatQVT_VarParameter433: "ImperativeOperation" = None, Variable111: "FlatQVT_ExpressionInOcl" = None, Variable141: "FlatQVT_InstantiationExp" = None, Variable76: "FlatQVT_CorePattern" = None, Variable161: "FlatQVT_LetExp" = None, Variable126: "FlatQVT_ImperativeIterateExp" = None, Variable447: "FlatQVT_VariableInitExp" = None, Variable445: "FlatQVT_VariableExp" = None, Variable108: "FlatQVT_ExpressionInOcl" = None, Variable429: "FlatQVT_UnpackExp" = None, Variable443: "FlatQVT_VariableAssignment" = None, Variable170: "FlatQVT_LoopExp" = None, Variable251: "FlatQVT_OperationBody" = None, Variable338: "FlatQVT_RelationDomain" = None, Variable219: "FlatQVT_Module" = None, Variable146: "FlatQVT_IterateExp" = None, Variable102: "FlatQVT_ExpressionInOcl" = None, Variable357: "FlatQVT_ResolveExp" = None, Variable66: "FlatQVT_ComputeExp" = None, Variable232: "FlatQVT_ObjectExp" = None, Variable374: "FlatQVT_TemplateExp" = None, Variable287: "FlatQVT_Pattern" = None, Variable321: "FlatQVT_Relation" = None, Variable: "FlatQVT_CollectionTemplateExp" = None, Variable343: "FlatQVT_RelationDomainAssignment" = None, Parameter441: "FlatQVT_Variable" = None, Parameter: "FlatQVT_Operation" = None):
        self.kind = kind
        self.FlatQVT_VarParameter = FlatQVT_VarParameter
        self.FlatQVT_VarParameter433 = FlatQVT_VarParameter433
        
        pass
    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind


    @property
    def FlatQVT_VarParameter433(self):
        return self.__FlatQVT_VarParameter433

    @FlatQVT_VarParameter433.setter
    def FlatQVT_VarParameter433(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FlatQVT_VarParameter__FlatQVT_VarParameter433", None)
        self.__FlatQVT_VarParameter433 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ImperativeOperation434"):
                opp_val = getattr(old_value, "ImperativeOperation434", None)
                if opp_val == self:
                    setattr(old_value, "ImperativeOperation434", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ImperativeOperation434"):
                opp_val = getattr(value, "ImperativeOperation434", None)
                setattr(value, "ImperativeOperation434", self)

    @property
    def FlatQVT_VarParameter(self):
        return self.__FlatQVT_VarParameter

    @FlatQVT_VarParameter.setter
    def FlatQVT_VarParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FlatQVT_VarParameter__FlatQVT_VarParameter", None)
        self.__FlatQVT_VarParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ImperativeOperation431"):
                opp_val = getattr(old_value, "ImperativeOperation431", None)
                if opp_val == self:
                    setattr(old_value, "ImperativeOperation431", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ImperativeOperation431"):
                opp_val = getattr(value, "ImperativeOperation431", None)
                setattr(value, "ImperativeOperation431", self)

class FlatQVT_FunctionParameter(Parameter, Variable):

    pass
class FlatQVT_RealizedVariable(Variable):

    pass
class OperationBody:

    pass
class FlatQVT_MappingBody(OperationBody):

    pass
class FlatQVT_ConstructorBody(OperationBody):

    pass
class ImperativeOperation:

    pass
class FlatQVT_Helper(ImperativeOperation):

    def __init__(self, isQuery: str, ImperativeOperation248: "FlatQVT_OperationBody" = None, ImperativeOperation434: "FlatQVT_VarParameter" = None, ImperativeOperation431: "FlatQVT_VarParameter" = None, ImperativeOperation: "FlatQVT_ImperativeOperation" = None):
        self.isQuery = isQuery
        
        pass
    @property
    def isQuery(self):
        return self.__isQuery

    @isQuery.setter
    def isQuery(self, isQuery: str):
        self.__isQuery = isQuery


class FlatQVT_MappingOperation(ImperativeOperation):

    pass
class FlatQVT_EntryOperation(ImperativeOperation):

    pass
class FlatQVT_Constructor(ImperativeOperation):

    pass
class CollectionLiteralExp:

    pass
class TypedElement:

    pass
class FlatQVT_Operation(MultiplicityElement, TypedElement):

    pass
class FlatQVT_Variable(TypedElement):

    pass
class FlatQVT_Parameter(MultiplicityElement, TypedElement):

    pass
class FlatQVT_TupleLiteralPart(TypedElement):

    pass
class FlatQVT_Property(MultiplicityElement, TypedElement):

    def __init__(self, default: str, isComposite: str, isDerived: str, isID: str, isReadOnly: str, FlatQVT_Property: "Class" = None, FlatQVT_Property297: "Property" = None):
        self.default = default
        self.isComposite = isComposite
        self.isDerived = isDerived
        self.isID = isID
        self.isReadOnly = isReadOnly
        self.FlatQVT_Property = FlatQVT_Property
        self.FlatQVT_Property297 = FlatQVT_Property297
        
        pass
    @property
    def isComposite(self):
        return self.__isComposite

    @isComposite.setter
    def isComposite(self, isComposite: str):
        self.__isComposite = isComposite


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
    def isDerived(self, isDerived: str):
        self.__isDerived = isDerived


    @property
    def isReadOnly(self):
        return self.__isReadOnly

    @isReadOnly.setter
    def isReadOnly(self, isReadOnly: str):
        self.__isReadOnly = isReadOnly


    @property
    def isID(self):
        return self.__isID

    @isID.setter
    def isID(self, isID: str):
        self.__isID = isID


    @property
    def FlatQVT_Property297(self):
        return self.__FlatQVT_Property297

    @FlatQVT_Property297.setter
    def FlatQVT_Property297(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FlatQVT_Property__FlatQVT_Property297", None)
        self.__FlatQVT_Property297 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Property298"):
                opp_val = getattr(old_value, "Property298", None)
                if opp_val == self:
                    setattr(old_value, "Property298", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Property298"):
                opp_val = getattr(value, "Property298", None)
                setattr(value, "Property298", self)

    @property
    def FlatQVT_Property(self):
        return self.__FlatQVT_Property

    @FlatQVT_Property.setter
    def FlatQVT_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FlatQVT_Property__FlatQVT_Property", None)
        self.__FlatQVT_Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Class295"):
                opp_val = getattr(old_value, "Class295", None)
                if opp_val == self:
                    setattr(old_value, "Class295", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Class295"):
                opp_val = getattr(value, "Class295", None)
                setattr(value, "Class295", self)

class FlatQVT_OclExpression(TypedElement):

    pass
class FlatQVT_ExpressionInOcl(TypedElement):

    pass
class FlatQVT_CollectionLiteralPart(TypedElement):

    pass
class LiteralExp:

    pass
class FlatQVT_OrderedTupleLiteralExp(LiteralExp):

    pass
class FlatQVT_ListLiteralExp(LiteralExp):

    pass
class FlatQVT_InvalidLiteralExp(LiteralExp):

    pass
class FlatQVT_PrimitiveLiteralExp(LiteralExp):

    pass
class FlatQVT_EnumLiteralExp(LiteralExp):

    pass
class FlatQVT_DictLiteralExp(LiteralExp):

    pass
class FlatQVT_TupleLiteralExp(LiteralExp):

    pass
class FlatQVT_NullLiteralExp(LiteralExp):

    pass
class FlatQVT_TemplateExp(LiteralExp):

    pass
class FlatQVT_CollectionLiteralExp(LiteralExp):

    def __init__(self, kind: str, FlatQVT_CollectionLiteralExp: set["CollectionLiteralPart"] = None):
        self.kind = kind
        self.FlatQVT_CollectionLiteralExp = FlatQVT_CollectionLiteralExp if FlatQVT_CollectionLiteralExp is not None else set()
        
        pass
    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind


    @property
    def FlatQVT_CollectionLiteralExp(self):
        return self.__FlatQVT_CollectionLiteralExp

    @FlatQVT_CollectionLiteralExp.setter
    def FlatQVT_CollectionLiteralExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FlatQVT_CollectionLiteralExp__FlatQVT_CollectionLiteralExp", None)
        self.__FlatQVT_CollectionLiteralExp = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CollectionLiteralPart"):
                    opp_val = getattr(item, "CollectionLiteralPart", None)
                    
                    if opp_val == self:
                        setattr(item, "CollectionLiteralPart", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CollectionLiteralPart"):
                    opp_val = getattr(item, "CollectionLiteralPart", None)
                    
                    setattr(item, "CollectionLiteralPart", self)
                    

class CollectionLiteralPart:

    pass
class FlatQVT_CollectionItem(CollectionLiteralPart):

    pass
class Class:

    pass
class FlatQVT_Typedef(Class):

    pass
class FlatQVT_TupleType(Class, DataType):

    pass
class FlatQVT_ModelType(Class):

    def __init__(self, conformanceKind: str, FlatQVT_ModelType: set["OclExpression"] = None, FlatQVT_ModelType207: set["Package"] = None, Class144: "FlatQVT_InstantiationExp" = None, Class68: "FlatQVT_ContextualProperty" = None, Class148: "FlatQVT_Key" = None, Class: "FlatQVT_Class" = None, Class238: "FlatQVT_Operation" = None, Class295: "FlatQVT_Property" = None, Class236: "FlatQVT_ObjectTemplateExp" = None, Class258: "FlatQVT_OperationalTransformation" = None):
        self.conformanceKind = conformanceKind
        self.FlatQVT_ModelType = FlatQVT_ModelType if FlatQVT_ModelType is not None else set()
        self.FlatQVT_ModelType207 = FlatQVT_ModelType207 if FlatQVT_ModelType207 is not None else set()
        
        pass
    @property
    def conformanceKind(self):
        return self.__conformanceKind

    @conformanceKind.setter
    def conformanceKind(self, conformanceKind: str):
        self.__conformanceKind = conformanceKind


    @property
    def FlatQVT_ModelType(self):
        return self.__FlatQVT_ModelType

    @FlatQVT_ModelType.setter
    def FlatQVT_ModelType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FlatQVT_ModelType__FlatQVT_ModelType", None)
        self.__FlatQVT_ModelType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OclExpression205"):
                    opp_val = getattr(item, "OclExpression205", None)
                    
                    if opp_val == self:
                        setattr(item, "OclExpression205", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OclExpression205"):
                    opp_val = getattr(item, "OclExpression205", None)
                    
                    setattr(item, "OclExpression205", self)
                    

    @property
    def FlatQVT_ModelType207(self):
        return self.__FlatQVT_ModelType207

    @FlatQVT_ModelType207.setter
    def FlatQVT_ModelType207(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FlatQVT_ModelType__FlatQVT_ModelType207", None)
        self.__FlatQVT_ModelType207 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Package208"):
                    opp_val = getattr(item, "Package208", None)
                    
                    if opp_val == self:
                        setattr(item, "Package208", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Package208"):
                    opp_val = getattr(item, "Package208", None)
                    
                    setattr(item, "Package208", self)
                    

class FlatQVT_Module(Class, Package):

    def __init__(self, isBlackbox: str, FlatQVT_Module214: set["ModuleImport"] = None, FlatQVT_Module216: set["Tag"] = None, FlatQVT_Module218: set["Variable"] = None, FlatQVT_Module221: set["ModelType"] = None, FlatQVT_Module: set["Property"] = None, FlatQVT_Module212: "EntryOperation" = None, Class144: "FlatQVT_InstantiationExp" = None, Class68: "FlatQVT_ContextualProperty" = None, Class148: "FlatQVT_Key" = None, Class: "FlatQVT_Class" = None, Class238: "FlatQVT_Operation" = None, Class295: "FlatQVT_Property" = None, Class236: "FlatQVT_ObjectTemplateExp" = None, Class258: "FlatQVT_OperationalTransformation" = None, Package402: "FlatQVT_Type" = None, Package280: "FlatQVT_Package" = None, Package414: "FlatQVT_TypedModel" = None, Package: "FlatQVT_Factory" = None, Package208: "FlatQVT_ModelType" = None, Package277: "FlatQVT_Package" = None):
        self.isBlackbox = isBlackbox
        self.FlatQVT_Module214 = FlatQVT_Module214 if FlatQVT_Module214 is not None else set()
        self.FlatQVT_Module216 = FlatQVT_Module216 if FlatQVT_Module216 is not None else set()
        self.FlatQVT_Module218 = FlatQVT_Module218 if FlatQVT_Module218 is not None else set()
        self.FlatQVT_Module221 = FlatQVT_Module221 if FlatQVT_Module221 is not None else set()
        self.FlatQVT_Module = FlatQVT_Module if FlatQVT_Module is not None else set()
        self.FlatQVT_Module212 = FlatQVT_Module212
        
        pass
    @property
    def isBlackbox(self):
        return self.__isBlackbox

    @isBlackbox.setter
    def isBlackbox(self, isBlackbox: str):
        self.__isBlackbox = isBlackbox


    @property
    def FlatQVT_Module214(self):
        return self.__FlatQVT_Module214

    @FlatQVT_Module214.setter
    def FlatQVT_Module214(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FlatQVT_Module__FlatQVT_Module214", None)
        self.__FlatQVT_Module214 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ModuleImport"):
                    opp_val = getattr(item, "ModuleImport", None)
                    
                    if opp_val == self:
                        setattr(item, "ModuleImport", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ModuleImport"):
                    opp_val = getattr(item, "ModuleImport", None)
                    
                    setattr(item, "ModuleImport", self)
                    

    @property
    def FlatQVT_Module(self):
        return self.__FlatQVT_Module

    @FlatQVT_Module.setter
    def FlatQVT_Module(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FlatQVT_Module__FlatQVT_Module", None)
        self.__FlatQVT_Module = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Property210"):
                    opp_val = getattr(item, "Property210", None)
                    
                    if opp_val == self:
                        setattr(item, "Property210", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Property210"):
                    opp_val = getattr(item, "Property210", None)
                    
                    setattr(item, "Property210", self)
                    

    @property
    def FlatQVT_Module212(self):
        return self.__FlatQVT_Module212

    @FlatQVT_Module212.setter
    def FlatQVT_Module212(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FlatQVT_Module__FlatQVT_Module212", None)
        self.__FlatQVT_Module212 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EntryOperation"):
                opp_val = getattr(old_value, "EntryOperation", None)
                if opp_val == self:
                    setattr(old_value, "EntryOperation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EntryOperation"):
                opp_val = getattr(value, "EntryOperation", None)
                setattr(value, "EntryOperation", self)

    @property
    def FlatQVT_Module221(self):
        return self.__FlatQVT_Module221

    @FlatQVT_Module221.setter
    def FlatQVT_Module221(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FlatQVT_Module__FlatQVT_Module221", None)
        self.__FlatQVT_Module221 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ModelType"):
                    opp_val = getattr(item, "ModelType", None)
                    
                    if opp_val == self:
                        setattr(item, "ModelType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ModelType"):
                    opp_val = getattr(item, "ModelType", None)
                    
                    setattr(item, "ModelType", self)
                    

    @property
    def FlatQVT_Module216(self):
        return self.__FlatQVT_Module216

    @FlatQVT_Module216.setter
    def FlatQVT_Module216(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FlatQVT_Module__FlatQVT_Module216", None)
        self.__FlatQVT_Module216 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Tag"):
                    opp_val = getattr(item, "Tag", None)
                    
                    if opp_val == self:
                        setattr(item, "Tag", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Tag"):
                    opp_val = getattr(item, "Tag", None)
                    
                    setattr(item, "Tag", self)
                    

    @property
    def FlatQVT_Module218(self):
        return self.__FlatQVT_Module218

    @FlatQVT_Module218.setter
    def FlatQVT_Module218(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FlatQVT_Module__FlatQVT_Module218", None)
        self.__FlatQVT_Module218 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Variable219"):
                    opp_val = getattr(item, "Variable219", None)
                    
                    if opp_val == self:
                        setattr(item, "Variable219", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Variable219"):
                    opp_val = getattr(item, "Variable219", None)
                    
                    setattr(item, "Variable219", self)
                    

class FlatQVT_OrderedTupleType(Class):

    pass
class FlatQVT_Transformation(Class, Package):

    pass
class Operation:

    pass
class FlatQVT_Function(Operation):

    pass
class FlatQVT_ImperativeOperation(Operation):

    def __init__(self, isBlackbox: str, FlatQVT_ImperativeOperation: "OperationBody" = None, FlatQVT_ImperativeOperation131: "VarParameter" = None, FlatQVT_ImperativeOperation133: "ImperativeOperation" = None, FlatQVT_ImperativeOperation135: set["VarParameter"] = None, Operation: "FlatQVT_Class" = None, Operation285: "FlatQVT_Parameter" = None, Operation256: "FlatQVT_OperationCallExp" = None, Operation345: "FlatQVT_RelationImplementation" = None):
        self.isBlackbox = isBlackbox
        self.FlatQVT_ImperativeOperation = FlatQVT_ImperativeOperation
        self.FlatQVT_ImperativeOperation131 = FlatQVT_ImperativeOperation131
        self.FlatQVT_ImperativeOperation133 = FlatQVT_ImperativeOperation133
        self.FlatQVT_ImperativeOperation135 = FlatQVT_ImperativeOperation135 if FlatQVT_ImperativeOperation135 is not None else set()
        
        pass
    @property
    def isBlackbox(self):
        return self.__isBlackbox

    @isBlackbox.setter
    def isBlackbox(self, isBlackbox: str):
        self.__isBlackbox = isBlackbox


    @property
    def FlatQVT_ImperativeOperation(self):
        return self.__FlatQVT_ImperativeOperation

    @FlatQVT_ImperativeOperation.setter
    def FlatQVT_ImperativeOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FlatQVT_ImperativeOperation__FlatQVT_ImperativeOperation", None)
        self.__FlatQVT_ImperativeOperation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OperationBody"):
                opp_val = getattr(old_value, "OperationBody", None)
                if opp_val == self:
                    setattr(old_value, "OperationBody", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OperationBody"):
                opp_val = getattr(value, "OperationBody", None)
                setattr(value, "OperationBody", self)

    @property
    def FlatQVT_ImperativeOperation133(self):
        return self.__FlatQVT_ImperativeOperation133

    @FlatQVT_ImperativeOperation133.setter
    def FlatQVT_ImperativeOperation133(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FlatQVT_ImperativeOperation__FlatQVT_ImperativeOperation133", None)
        self.__FlatQVT_ImperativeOperation133 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ImperativeOperation"):
                opp_val = getattr(old_value, "ImperativeOperation", None)
                if opp_val == self:
                    setattr(old_value, "ImperativeOperation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ImperativeOperation"):
                opp_val = getattr(value, "ImperativeOperation", None)
                setattr(value, "ImperativeOperation", self)

    @property
    def FlatQVT_ImperativeOperation135(self):
        return self.__FlatQVT_ImperativeOperation135

    @FlatQVT_ImperativeOperation135.setter
    def FlatQVT_ImperativeOperation135(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FlatQVT_ImperativeOperation__FlatQVT_ImperativeOperation135", None)
        self.__FlatQVT_ImperativeOperation135 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "VarParameter136"):
                    opp_val = getattr(item, "VarParameter136", None)
                    
                    if opp_val == self:
                        setattr(item, "VarParameter136", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "VarParameter136"):
                    opp_val = getattr(item, "VarParameter136", None)
                    
                    setattr(item, "VarParameter136", self)
                    

    @property
    def FlatQVT_ImperativeOperation131(self):
        return self.__FlatQVT_ImperativeOperation131

    @FlatQVT_ImperativeOperation131.setter
    def FlatQVT_ImperativeOperation131(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FlatQVT_ImperativeOperation__FlatQVT_ImperativeOperation131", None)
        self.__FlatQVT_ImperativeOperation131 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VarParameter"):
                opp_val = getattr(old_value, "VarParameter", None)
                if opp_val == self:
                    setattr(old_value, "VarParameter", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VarParameter"):
                opp_val = getattr(value, "VarParameter", None)
                setattr(value, "VarParameter", self)

class Property:

    pass
class FlatQVT_ContextualProperty(Property):

    pass
class TemplateExp:

    pass
class FlatQVT_ObjectTemplateExp(TemplateExp):

    pass
class FlatQVT_CollectionTemplateExp(TemplateExp):

    pass
class FlatQVT_CollectionRange(CollectionLiteralPart):

    pass
class EnforcementOperation:

    pass
class Assignment:

    pass
class FlatQVT_PropertyAssignment(Assignment):

    pass
class FlatQVT_VariableAssignment(Assignment):

    pass
class Area:

    pass
class FlatQVT_CoreDomain(Domain, Area):

    pass
class FlatQVT_Mapping(Area, Rule):

    pass
class CorePattern:

    pass
class FlatQVT_GuardPattern(CorePattern):

    pass
class FlatQVT_BottomPattern(CorePattern):

    pass
class PrimitiveLiteralExp:

    pass
class FlatQVT_StringLiteralExp(PrimitiveLiteralExp):

    def __init__(self, stringSymbol: str):
        self.stringSymbol = stringSymbol
        
        pass
    @property
    def stringSymbol(self):
        return self.__stringSymbol

    @stringSymbol.setter
    def stringSymbol(self, stringSymbol: str):
        self.__stringSymbol = stringSymbol


class FlatQVT_NumericLiteralExp(PrimitiveLiteralExp):

    pass
class FlatQVT_BooleanLiteralExp(PrimitiveLiteralExp):

    def __init__(self, booleanSymbol: str):
        self.booleanSymbol = booleanSymbol
        
        pass
    @property
    def booleanSymbol(self):
        return self.__booleanSymbol

    @booleanSymbol.setter
    def booleanSymbol(self, booleanSymbol: str):
        self.__booleanSymbol = booleanSymbol


class CollectionType:

    pass
class FlatQVT_SetType(CollectionType):

    pass
class FlatQVT_ListType(CollectionType):

    pass
class FlatQVT_OrderedSetType(CollectionType):

    pass
class FlatQVT_SequenceType(CollectionType):

    pass
class FlatQVT_DictionaryType(CollectionType):

    pass
class FlatQVT_BagType(CollectionType):

    pass
class Element:

    pass
class FlatQVT_OrderedTupleLiteralPart(Element):

    pass
class FlatQVT_Key(Element):

    pass
class FlatQVT_PropertyTemplateItem(Element):

    def __init__(self, isOpposite: str, FlatQVT_PropertyTemplateItem: "ObjectTemplateExp" = None, FlatQVT_PropertyTemplateItem308: "Property" = None, FlatQVT_PropertyTemplateItem311: "OclExpression" = None, Element: "FlatQVT_Tag" = None):
        self.isOpposite = isOpposite
        self.FlatQVT_PropertyTemplateItem = FlatQVT_PropertyTemplateItem
        self.FlatQVT_PropertyTemplateItem308 = FlatQVT_PropertyTemplateItem308
        self.FlatQVT_PropertyTemplateItem311 = FlatQVT_PropertyTemplateItem311
        
        pass
    @property
    def isOpposite(self):
        return self.__isOpposite

    @isOpposite.setter
    def isOpposite(self, isOpposite: str):
        self.__isOpposite = isOpposite


    @property
    def FlatQVT_PropertyTemplateItem311(self):
        return self.__FlatQVT_PropertyTemplateItem311

    @FlatQVT_PropertyTemplateItem311.setter
    def FlatQVT_PropertyTemplateItem311(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FlatQVT_PropertyTemplateItem__FlatQVT_PropertyTemplateItem311", None)
        self.__FlatQVT_PropertyTemplateItem311 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression312"):
                opp_val = getattr(old_value, "OclExpression312", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression312", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression312"):
                opp_val = getattr(value, "OclExpression312", None)
                setattr(value, "OclExpression312", self)

    @property
    def FlatQVT_PropertyTemplateItem308(self):
        return self.__FlatQVT_PropertyTemplateItem308

    @FlatQVT_PropertyTemplateItem308.setter
    def FlatQVT_PropertyTemplateItem308(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FlatQVT_PropertyTemplateItem__FlatQVT_PropertyTemplateItem308", None)
        self.__FlatQVT_PropertyTemplateItem308 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Property309"):
                opp_val = getattr(old_value, "Property309", None)
                if opp_val == self:
                    setattr(old_value, "Property309", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Property309"):
                opp_val = getattr(value, "Property309", None)
                setattr(value, "Property309", self)

    @property
    def FlatQVT_PropertyTemplateItem(self):
        return self.__FlatQVT_PropertyTemplateItem

    @FlatQVT_PropertyTemplateItem.setter
    def FlatQVT_PropertyTemplateItem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FlatQVT_PropertyTemplateItem__FlatQVT_PropertyTemplateItem", None)
        self.__FlatQVT_PropertyTemplateItem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ObjectTemplateExp"):
                opp_val = getattr(old_value, "ObjectTemplateExp", None)
                if opp_val == self:
                    setattr(old_value, "ObjectTemplateExp", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ObjectTemplateExp"):
                opp_val = getattr(value, "ObjectTemplateExp", None)
                setattr(value, "ObjectTemplateExp", self)

class FlatQVT_DictLiteralPart(Element):

    pass
class FlatQVT_Pattern(Element):

    pass
class FlatQVT_ModuleImport(Element):

    def __init__(self, kind: str, FlatQVT_ModuleImport: set["ModelType"] = None, FlatQVT_ModuleImport225: "Module" = None, FlatQVT_ModuleImport227: "Module" = None, Element: "FlatQVT_Tag" = None):
        self.kind = kind
        self.FlatQVT_ModuleImport = FlatQVT_ModuleImport if FlatQVT_ModuleImport is not None else set()
        self.FlatQVT_ModuleImport225 = FlatQVT_ModuleImport225
        self.FlatQVT_ModuleImport227 = FlatQVT_ModuleImport227
        
        pass
    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind


    @property
    def FlatQVT_ModuleImport(self):
        return self.__FlatQVT_ModuleImport

    @FlatQVT_ModuleImport.setter
    def FlatQVT_ModuleImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FlatQVT_ModuleImport__FlatQVT_ModuleImport", None)
        self.__FlatQVT_ModuleImport = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ModelType223"):
                    opp_val = getattr(item, "ModelType223", None)
                    
                    if opp_val == self:
                        setattr(item, "ModelType223", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ModelType223"):
                    opp_val = getattr(item, "ModelType223", None)
                    
                    setattr(item, "ModelType223", self)
                    

    @property
    def FlatQVT_ModuleImport227(self):
        return self.__FlatQVT_ModuleImport227

    @FlatQVT_ModuleImport227.setter
    def FlatQVT_ModuleImport227(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FlatQVT_ModuleImport__FlatQVT_ModuleImport227", None)
        self.__FlatQVT_ModuleImport227 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Module228"):
                opp_val = getattr(old_value, "Module228", None)
                if opp_val == self:
                    setattr(old_value, "Module228", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Module228"):
                opp_val = getattr(value, "Module228", None)
                setattr(value, "Module228", self)

    @property
    def FlatQVT_ModuleImport225(self):
        return self.__FlatQVT_ModuleImport225

    @FlatQVT_ModuleImport225.setter
    def FlatQVT_ModuleImport225(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FlatQVT_ModuleImport__FlatQVT_ModuleImport225", None)
        self.__FlatQVT_ModuleImport225 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Module"):
                opp_val = getattr(old_value, "Module", None)
                if opp_val == self:
                    setattr(old_value, "Module", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Module"):
                opp_val = getattr(value, "Module", None)
                setattr(value, "Module", self)

class FlatQVT_EnforcementOperation(Element):

    def __init__(self, enforcementMode: str, FlatQVT_EnforcementOperation93: "OperationCallExp" = None, FlatQVT_EnforcementOperation: "BottomPattern" = None, Element: "FlatQVT_Tag" = None):
        self.enforcementMode = enforcementMode
        self.FlatQVT_EnforcementOperation93 = FlatQVT_EnforcementOperation93
        self.FlatQVT_EnforcementOperation = FlatQVT_EnforcementOperation
        
        pass
    @property
    def enforcementMode(self):
        return self.__enforcementMode

    @enforcementMode.setter
    def enforcementMode(self, enforcementMode: str):
        self.__enforcementMode = enforcementMode


    @property
    def FlatQVT_EnforcementOperation(self):
        return self.__FlatQVT_EnforcementOperation

    @FlatQVT_EnforcementOperation.setter
    def FlatQVT_EnforcementOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FlatQVT_EnforcementOperation__FlatQVT_EnforcementOperation", None)
        self.__FlatQVT_EnforcementOperation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BottomPattern91"):
                opp_val = getattr(old_value, "BottomPattern91", None)
                if opp_val == self:
                    setattr(old_value, "BottomPattern91", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BottomPattern91"):
                opp_val = getattr(value, "BottomPattern91", None)
                setattr(value, "BottomPattern91", self)

    @property
    def FlatQVT_EnforcementOperation93(self):
        return self.__FlatQVT_EnforcementOperation93

    @FlatQVT_EnforcementOperation93.setter
    def FlatQVT_EnforcementOperation93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FlatQVT_EnforcementOperation__FlatQVT_EnforcementOperation93", None)
        self.__FlatQVT_EnforcementOperation93 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OperationCallExp"):
                opp_val = getattr(old_value, "OperationCallExp", None)
                if opp_val == self:
                    setattr(old_value, "OperationCallExp", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OperationCallExp"):
                opp_val = getattr(value, "OperationCallExp", None)
                setattr(value, "OperationCallExp", self)

class FlatQVT_Comment(Element):

    def __init__(self, body: str, FlatQVT_Comment: set["NamedElement"] = None, Element: "FlatQVT_Tag" = None):
        self.body = body
        self.FlatQVT_Comment = FlatQVT_Comment if FlatQVT_Comment is not None else set()
        
        pass
    @property
    def body(self):
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body


    @property
    def FlatQVT_Comment(self):
        return self.__FlatQVT_Comment

    @FlatQVT_Comment.setter
    def FlatQVT_Comment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FlatQVT_Comment__FlatQVT_Comment", None)
        self.__FlatQVT_Comment = value if value is not None else set()
        
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
                    

class FlatQVT_Predicate(Element):

    pass
class FlatQVT_NamedElement(Element):

    def __init__(self, name: str, Element: "FlatQVT_Tag" = None):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class FlatQVT_Tag(Element):

    def __init__(self, name: str, value: str, FlatQVT_Tag: set["Element"] = None, Element: "FlatQVT_Tag" = None):
        self.name = name
        self.value = value
        self.FlatQVT_Tag = FlatQVT_Tag if FlatQVT_Tag is not None else set()
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def FlatQVT_Tag(self):
        return self.__FlatQVT_Tag

    @FlatQVT_Tag.setter
    def FlatQVT_Tag(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FlatQVT_Tag__FlatQVT_Tag", None)
        self.__FlatQVT_Tag = value if value is not None else set()
        
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
                    

class FlatQVT_RelationImplementation(Element):

    pass
class FlatQVT_RelationDomainAssignment(Element):

    pass
class FlatQVT_OperationBody(Element):

    pass
class FlatQVT_Factory(Element):

    def __init__(self, FlatQVT_Factory: "Package" = None, Element: "FlatQVT_Tag" = None):
        self.FlatQVT_Factory = FlatQVT_Factory
        
        pass
    @property
    def FlatQVT_Factory(self):
        return self.__FlatQVT_Factory

    @FlatQVT_Factory.setter
    def FlatQVT_Factory(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FlatQVT_Factory__FlatQVT_Factory", None)
        self.__FlatQVT_Factory = value
        
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

    def convertToString(self, FlatQVT_object, FlatQVT_dataType) :
        # TODO: Implement convertToString method
        pass

    def createFromString(self, FlatQVT_dataType, FlatQVT_string) :
        # TODO: Implement createFromString method
        pass

    def create(self, FlatQVT_metaClass) :
        # TODO: Implement create method
        pass

class FlatQVT_Assignment(Element):

    def __init__(self, isDefault: str, FlatQVT_Assignment: "BottomPattern" = None, FlatQVT_Assignment22: "OclExpression" = None, Element: "FlatQVT_Tag" = None):
        self.isDefault = isDefault
        self.FlatQVT_Assignment = FlatQVT_Assignment
        self.FlatQVT_Assignment22 = FlatQVT_Assignment22
        
        pass
    @property
    def isDefault(self):
        return self.__isDefault

    @isDefault.setter
    def isDefault(self, isDefault: str):
        self.__isDefault = isDefault


    @property
    def FlatQVT_Assignment(self):
        return self.__FlatQVT_Assignment

    @FlatQVT_Assignment.setter
    def FlatQVT_Assignment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FlatQVT_Assignment__FlatQVT_Assignment", None)
        self.__FlatQVT_Assignment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BottomPattern20"):
                opp_val = getattr(old_value, "BottomPattern20", None)
                if opp_val == self:
                    setattr(old_value, "BottomPattern20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BottomPattern20"):
                opp_val = getattr(value, "BottomPattern20", None)
                setattr(value, "BottomPattern20", self)

    @property
    def FlatQVT_Assignment22(self):
        return self.__FlatQVT_Assignment22

    @FlatQVT_Assignment22.setter
    def FlatQVT_Assignment22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FlatQVT_Assignment__FlatQVT_Assignment22", None)
        self.__FlatQVT_Assignment22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression23"):
                opp_val = getattr(old_value, "OclExpression23", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression23"):
                opp_val = getattr(value, "OclExpression23", None)
                setattr(value, "OclExpression23", self)

class RealizedVariable:

    pass
class GuardPattern:

    pass
class BottomPattern:

    pass
class FlatQVT_Area(ABC):

    pass
class Type:

    pass
class FlatQVT_Class(Type):

    def __init__(self, isAbstract: str, FlatQVT_Class: set["Property"] = None, FlatQVT_Class41: set["Operation"] = None, FlatQVT_Class43: set["Class"] = None, Type283: "FlatQVT_Package" = None, Type60: "FlatQVT_CollectionType" = None, Type105: "FlatQVT_ExpressionInOcl" = None, Type416: "FlatQVT_Typedef" = None, Type404: "FlatQVT_TypeExp" = None, Type243: "FlatQVT_Operation" = None, Type317: "FlatQVT_RaiseExp" = None, Type406: "FlatQVT_TypedElement" = None, Type: "FlatQVT_CatchExp" = None, Type84: "FlatQVT_DictionaryType" = None, Type275: "FlatQVT_OrderedTupleType" = None):
        self.isAbstract = isAbstract
        self.FlatQVT_Class = FlatQVT_Class if FlatQVT_Class is not None else set()
        self.FlatQVT_Class41 = FlatQVT_Class41 if FlatQVT_Class41 is not None else set()
        self.FlatQVT_Class43 = FlatQVT_Class43 if FlatQVT_Class43 is not None else set()
        
        pass
    @property
    def isAbstract(self):
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: str):
        self.__isAbstract = isAbstract


    @property
    def FlatQVT_Class(self):
        return self.__FlatQVT_Class

    @FlatQVT_Class.setter
    def FlatQVT_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FlatQVT_Class__FlatQVT_Class", None)
        self.__FlatQVT_Class = value if value is not None else set()
        
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
    def FlatQVT_Class43(self):
        return self.__FlatQVT_Class43

    @FlatQVT_Class43.setter
    def FlatQVT_Class43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FlatQVT_Class__FlatQVT_Class43", None)
        self.__FlatQVT_Class43 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Class"):
                    opp_val = getattr(item, "Class", None)
                    
                    if opp_val == self:
                        setattr(item, "Class", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Class"):
                    opp_val = getattr(item, "Class", None)
                    
                    setattr(item, "Class", self)
                    

    @property
    def FlatQVT_Class41(self):
        return self.__FlatQVT_Class41

    @FlatQVT_Class41.setter
    def FlatQVT_Class41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FlatQVT_Class__FlatQVT_Class41", None)
        self.__FlatQVT_Class41 = value if value is not None else set()
        
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
                    

class FlatQVT_DataType(Type):

    pass
class FlatQVT_TemplateParameterType(Type):

    def __init__(self, specification: str, Type283: "FlatQVT_Package" = None, Type60: "FlatQVT_CollectionType" = None, Type105: "FlatQVT_ExpressionInOcl" = None, Type416: "FlatQVT_Typedef" = None, Type404: "FlatQVT_TypeExp" = None, Type243: "FlatQVT_Operation" = None, Type317: "FlatQVT_RaiseExp" = None, Type406: "FlatQVT_TypedElement" = None, Type: "FlatQVT_CatchExp" = None, Type84: "FlatQVT_DictionaryType" = None, Type275: "FlatQVT_OrderedTupleType" = None):
        self.specification = specification
        
        pass
    @property
    def specification(self):
        return self.__specification

    @specification.setter
    def specification(self, specification: str):
        self.__specification = specification


class FlatQVT_InvalidType(Type):

    pass
class FlatQVT_VoidType(Type):

    pass
class FlatQVT_AnyType(Type):

    pass
class OclExpression:

    pass
class FlatQVT_RelationCallExp(OclExpression):

    pass
class FlatQVT_LiteralExp(OclExpression):

    pass
class FlatQVT_ImperativeExpression(OclExpression):

    pass
class FlatQVT_VariableExp(OclExpression):

    pass
class FlatQVT_LetExp(OclExpression):

    pass
class FlatQVT_CallExp(OclExpression):

    pass
class FlatQVT_IfExp(OclExpression):

    pass
class FlatQVT_TypeExp(OclExpression):

    pass
class ImperativeExpression:

    pass
class FlatQVT_AssertExp(ImperativeExpression):

    def __init__(self, severity: str, FlatQVT_AssertExp10: "LogExp" = None, FlatQVT_AssertExp: "OclExpression" = None):
        self.severity = severity
        self.FlatQVT_AssertExp10 = FlatQVT_AssertExp10
        self.FlatQVT_AssertExp = FlatQVT_AssertExp
        
        pass
    @property
    def severity(self):
        return self.__severity

    @severity.setter
    def severity(self, severity: str):
        self.__severity = severity


    @property
    def FlatQVT_AssertExp10(self):
        return self.__FlatQVT_AssertExp10

    @FlatQVT_AssertExp10.setter
    def FlatQVT_AssertExp10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FlatQVT_AssertExp__FlatQVT_AssertExp10", None)
        self.__FlatQVT_AssertExp10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "LogExp"):
                opp_val = getattr(old_value, "LogExp", None)
                if opp_val == self:
                    setattr(old_value, "LogExp", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LogExp"):
                opp_val = getattr(value, "LogExp", None)
                setattr(value, "LogExp", self)

    @property
    def FlatQVT_AssertExp(self):
        return self.__FlatQVT_AssertExp

    @FlatQVT_AssertExp.setter
    def FlatQVT_AssertExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FlatQVT_AssertExp__FlatQVT_AssertExp", None)
        self.__FlatQVT_AssertExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression8"):
                opp_val = getattr(old_value, "OclExpression8", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression8"):
                opp_val = getattr(value, "OclExpression8", None)
                setattr(value, "OclExpression8", self)

class FlatQVT_UnpackExp(ImperativeExpression):

    pass
class FlatQVT_ResolveExp(ImperativeExpression, CallExp):

    def __init__(self, isDeferred: str, isInverse: str, one: str, FlatQVT_ResolveExp: "OclExpression" = None, FlatQVT_ResolveExp356: "Variable" = None):
        self.isDeferred = isDeferred
        self.isInverse = isInverse
        self.one = one
        self.FlatQVT_ResolveExp = FlatQVT_ResolveExp
        self.FlatQVT_ResolveExp356 = FlatQVT_ResolveExp356
        
        pass
    @property
    def isDeferred(self):
        return self.__isDeferred

    @isDeferred.setter
    def isDeferred(self, isDeferred: str):
        self.__isDeferred = isDeferred


    @property
    def one(self):
        return self.__one

    @one.setter
    def one(self, one: str):
        self.__one = one


    @property
    def isInverse(self):
        return self.__isInverse

    @isInverse.setter
    def isInverse(self, isInverse: str):
        self.__isInverse = isInverse


    @property
    def FlatQVT_ResolveExp(self):
        return self.__FlatQVT_ResolveExp

    @FlatQVT_ResolveExp.setter
    def FlatQVT_ResolveExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FlatQVT_ResolveExp__FlatQVT_ResolveExp", None)
        self.__FlatQVT_ResolveExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression354"):
                opp_val = getattr(old_value, "OclExpression354", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression354", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression354"):
                opp_val = getattr(value, "OclExpression354", None)
                setattr(value, "OclExpression354", self)

    @property
    def FlatQVT_ResolveExp356(self):
        return self.__FlatQVT_ResolveExp356

    @FlatQVT_ResolveExp356.setter
    def FlatQVT_ResolveExp356(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FlatQVT_ResolveExp__FlatQVT_ResolveExp356", None)
        self.__FlatQVT_ResolveExp356 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Variable357"):
                opp_val = getattr(old_value, "Variable357", None)
                if opp_val == self:
                    setattr(old_value, "Variable357", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Variable357"):
                opp_val = getattr(value, "Variable357", None)
                setattr(value, "Variable357", self)

class FlatQVT_InstantiationExp(ImperativeExpression):

    pass
class FlatQVT_BreakExp(ImperativeExpression):

    pass
class FlatQVT_SwitchExp(ImperativeExpression):

    pass
class FlatQVT_TryExp(ImperativeExpression):

    pass
class FlatQVT_ComputeExp(ImperativeExpression):

    pass
class FlatQVT_BlockExp(ImperativeExpression):

    pass
class FlatQVT_UnlinkExp(ImperativeExpression):

    pass
class FlatQVT_CatchExp(ImperativeExpression):

    pass
class FlatQVT_WhileExp(ImperativeExpression):

    pass
class FlatQVT_LogExp(ImperativeExpression, OperationCallExp):

    pass
class FlatQVT_ImperativeLoopExp(ImperativeExpression, LoopExp):

    pass
class FlatQVT_VariableInitExp(ImperativeExpression):

    def __init__(self, withResult: str, FlatQVT_VariableInitExp: "Variable" = None):
        self.withResult = withResult
        self.FlatQVT_VariableInitExp = FlatQVT_VariableInitExp
        
        pass
    @property
    def withResult(self):
        return self.__withResult

    @withResult.setter
    def withResult(self, withResult: str):
        self.__withResult = withResult


    @property
    def FlatQVT_VariableInitExp(self):
        return self.__FlatQVT_VariableInitExp

    @FlatQVT_VariableInitExp.setter
    def FlatQVT_VariableInitExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FlatQVT_VariableInitExp__FlatQVT_VariableInitExp", None)
        self.__FlatQVT_VariableInitExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Variable447"):
                opp_val = getattr(old_value, "Variable447", None)
                if opp_val == self:
                    setattr(old_value, "Variable447", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Variable447"):
                opp_val = getattr(value, "Variable447", None)
                setattr(value, "Variable447", self)

class FlatQVT_ContinueExp(ImperativeExpression):

    pass
class FlatQVT_RaiseExp(ImperativeExpression):

    pass
class FlatQVT_ImperativeCallExp(OperationCallExp, ImperativeExpression):

    def __init__(self, isVirtual: str, OperationCallExp: "FlatQVT_EnforcementOperation" = None):
        self.isVirtual = isVirtual
        
        pass
    @property
    def isVirtual(self):
        return self.__isVirtual

    @isVirtual.setter
    def isVirtual(self, isVirtual: str):
        self.__isVirtual = isVirtual


class FlatQVT_ReturnExp(ImperativeExpression):

    pass
class FlatQVT_AltExp(ImperativeExpression):

    pass
class FlatQVT_AssignExp(ImperativeExpression):

    def __init__(self, isReset: str, FlatQVT_AssignExp: "OclExpression" = None, FlatQVT_AssignExp14: "OclExpression" = None, FlatQVT_AssignExp17: set["OclExpression"] = None):
        self.isReset = isReset
        self.FlatQVT_AssignExp = FlatQVT_AssignExp
        self.FlatQVT_AssignExp14 = FlatQVT_AssignExp14
        self.FlatQVT_AssignExp17 = FlatQVT_AssignExp17 if FlatQVT_AssignExp17 is not None else set()
        
        pass
    @property
    def isReset(self):
        return self.__isReset

    @isReset.setter
    def isReset(self, isReset: str):
        self.__isReset = isReset


    @property
    def FlatQVT_AssignExp(self):
        return self.__FlatQVT_AssignExp

    @FlatQVT_AssignExp.setter
    def FlatQVT_AssignExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FlatQVT_AssignExp__FlatQVT_AssignExp", None)
        self.__FlatQVT_AssignExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression12"):
                opp_val = getattr(old_value, "OclExpression12", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression12"):
                opp_val = getattr(value, "OclExpression12", None)
                setattr(value, "OclExpression12", self)

    @property
    def FlatQVT_AssignExp14(self):
        return self.__FlatQVT_AssignExp14

    @FlatQVT_AssignExp14.setter
    def FlatQVT_AssignExp14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FlatQVT_AssignExp__FlatQVT_AssignExp14", None)
        self.__FlatQVT_AssignExp14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression15"):
                opp_val = getattr(old_value, "OclExpression15", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression15"):
                opp_val = getattr(value, "OclExpression15", None)
                setattr(value, "OclExpression15", self)

    @property
    def FlatQVT_AssignExp17(self):
        return self.__FlatQVT_AssignExp17

    @FlatQVT_AssignExp17.setter
    def FlatQVT_AssignExp17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FlatQVT_AssignExp__FlatQVT_AssignExp17", None)
        self.__FlatQVT_AssignExp17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OclExpression18"):
                    opp_val = getattr(item, "OclExpression18", None)
                    
                    if opp_val == self:
                        setattr(item, "OclExpression18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OclExpression18"):
                    opp_val = getattr(item, "OclExpression18", None)
                    
                    setattr(item, "OclExpression18", self)
                    

class LogExp:

    pass
class FlatQVT_MappingParameter(VarParameter):

    pass
class Relation:

    pass
class FlatQVT_LoopExp(CallExp, OclExpression):

    pass