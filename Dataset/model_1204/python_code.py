from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class CollectionKind(Enum):
    collection = "collection"
    set = "set"
    orderedSet = "orderedSet"
    bag = "bag"
    sequence = "sequence"


############################################
# Definition of Classes
############################################

class ocl_query_Query:

    def __init__(self, extentMap: str, ocl_query_Query: "OCLExpression" = None):
        self.extentMap = extentMap
        self.ocl_query_Query = ocl_query_Query
        
        pass
    @property
    def extentMap(self):
        return self.__extentMap

    @extentMap.setter
    def extentMap(self, extentMap: str):
        self.__extentMap = extentMap


    @property
    def ocl_query_Query(self):
        return self.__ocl_query_Query

    @ocl_query_Query.setter
    def ocl_query_Query(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ocl_query_Query__ocl_query_Query", None)
        self.__ocl_query_Query = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCLExpression75"):
                opp_val = getattr(old_value, "OCLExpression75", None)
                if opp_val == self:
                    setattr(old_value, "OCLExpression75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCLExpression75"):
                opp_val = getattr(value, "OCLExpression75", None)
                setattr(value, "OCLExpression75", self)

    def evaluate(self, ocl_objects) :
        # TODO: Implement evaluate method
        pass

    def queryText(self) :
        # TODO: Implement queryText method
        pass

    def resultType(self) :
        # TODO: Implement resultType method
        pass

    def select(self, ocl_objects) :
        # TODO: Implement select method
        pass

    def reject(self, ocl_objects) :
        # TODO: Implement reject method
        pass

    def check(self, ocl_objects) :
        # TODO: Implement check method
        pass

class ocl_utilities_Visitable:

    def __init__(self):
        
        pass
    def accept(self, ocl_v) :
        # TODO: Implement accept method
        pass

class ocl_utilities_PredefinedType(ABC):

    def __init__(self):
        
        pass
    def getOperationCodeFor(self, ocl_operName) :
        # TODO: Implement getOperationCodeFor method
        pass

    def getCommonSupertype(self, ocl_type) :
        # TODO: Implement getCommonSupertype method
        pass

    def getOperations(self) :
        # TODO: Implement getOperations method
        pass

    def getResultTypeFor(self, ocl_ownerType, ocl_opcode, ocl_args) :
        # TODO: Implement getResultTypeFor method
        pass

    def getRelationshipTo(self, ocl_type) :
        # TODO: Implement getRelationshipTo method
        pass

    def getOperationNameFor(self, ocl_opcode) :
        # TODO: Implement getOperationNameFor method
        pass

class ASTNode:

    pass
class ocl_utilities_TypedASTNode(ASTNode):

    def __init__(self, typeStartPosition: int, typeEndPosition: int):
        self.typeStartPosition = typeStartPosition
        self.typeEndPosition = typeEndPosition
        
        pass
    @property
    def typeEndPosition(self):
        return self.__typeEndPosition

    @typeEndPosition.setter
    def typeEndPosition(self, typeEndPosition: int):
        self.__typeEndPosition = typeEndPosition


    @property
    def typeStartPosition(self):
        return self.__typeStartPosition

    @typeStartPosition.setter
    def typeStartPosition(self, typeStartPosition: int):
        self.__typeStartPosition = typeStartPosition


class ocl_utilities_CallingASTNode(ASTNode):

    def __init__(self, propertyStartPosition: int, propertyEndPosition: int):
        self.propertyStartPosition = propertyStartPosition
        self.propertyEndPosition = propertyEndPosition
        
        pass
    @property
    def propertyStartPosition(self):
        return self.__propertyStartPosition

    @propertyStartPosition.setter
    def propertyStartPosition(self, propertyStartPosition: int):
        self.__propertyStartPosition = propertyStartPosition


    @property
    def propertyEndPosition(self):
        return self.__propertyEndPosition

    @propertyEndPosition.setter
    def propertyEndPosition(self, propertyEndPosition: int):
        self.__propertyEndPosition = propertyEndPosition


class ocl_utilities_ASTNode(ABC):

    def __init__(self, startPosition: int, endPosition: int):
        self.startPosition = startPosition
        self.endPosition = endPosition
        
        pass
    @property
    def endPosition(self):
        return self.__endPosition

    @endPosition.setter
    def endPosition(self, endPosition: int):
        self.__endPosition = endPosition


    @property
    def startPosition(self):
        return self.__startPosition

    @startPosition.setter
    def startPosition(self, startPosition: int):
        self.__startPosition = startPosition


class uml_ocl_EClassifier:

    pass
class uml_ocl_EClass:

    pass
class ocl_uml_SendSignalAction:

    pass
class uml_ocl_ENamedElement:

    pass
class ENamedElement:

    pass
class ocl_uml_TypedElement(ENamedElement):

    pass
class uml_ocl_EOperation:

    pass
class ocl_uml_CallOperationAction:

    pass
class expressions_ocl_EParameter:

    pass
class expressions_ocl_EClassifier:

    pass
class TupleLiteralPart:

    pass
class expressions_ocl_EObject:

    pass
class expressions_ocl_EOperation:

    pass
class utilities_ASTNode:

    pass
class utilities_Visitable:

    pass
class ocl_uml_Constraint(utilities_Visitable, ENamedElement):

    def __init__(self, instanceVarName: str, stereotype: str, ocl_uml_Constraint: "OCLExpression" = None, ocl_uml_Constraint71: set["uml_ocl_ENamedElement"] = None):
        self.instanceVarName = instanceVarName
        self.stereotype = stereotype
        self.ocl_uml_Constraint = ocl_uml_Constraint
        self.ocl_uml_Constraint71 = ocl_uml_Constraint71 if ocl_uml_Constraint71 is not None else set()
        
        pass
    @property
    def stereotype(self):
        return self.__stereotype

    @stereotype.setter
    def stereotype(self, stereotype: str):
        self.__stereotype = stereotype


    @property
    def instanceVarName(self):
        return self.__instanceVarName

    @instanceVarName.setter
    def instanceVarName(self, instanceVarName: str):
        self.__instanceVarName = instanceVarName


    @property
    def ocl_uml_Constraint(self):
        return self.__ocl_uml_Constraint

    @ocl_uml_Constraint.setter
    def ocl_uml_Constraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ocl_uml_Constraint__ocl_uml_Constraint", None)
        self.__ocl_uml_Constraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCLExpression69"):
                opp_val = getattr(old_value, "OCLExpression69", None)
                if opp_val == self:
                    setattr(old_value, "OCLExpression69", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCLExpression69"):
                opp_val = getattr(value, "OCLExpression69", None)
                setattr(value, "OCLExpression69", self)

    @property
    def ocl_uml_Constraint71(self):
        return self.__ocl_uml_Constraint71

    @ocl_uml_Constraint71.setter
    def ocl_uml_Constraint71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ocl_uml_Constraint__ocl_uml_Constraint71", None)
        self.__ocl_uml_Constraint71 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_ocl_ENamedElement"):
                    opp_val = getattr(item, "uml_ocl_ENamedElement", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_ocl_ENamedElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_ocl_ENamedElement"):
                    opp_val = getattr(item, "uml_ocl_ENamedElement", None)
                    
                    setattr(item, "uml_ocl_ENamedElement", self)
                    

class uml_TypedElement:

    pass
class ocl_expressions_OCLExpression(uml_TypedElement, utilities_Visitable, utilities_ASTNode):

    pass
class expressions_ocl_EStructuralFeature:

    pass
class FeatureCallExp:

    pass
class ocl_expressions_OperationCallExp(FeatureCallExp):

    pass
class ocl_expressions_NavigationCallExp(FeatureCallExp):

    pass
class SendSignalAction:

    pass
class CallOperationAction:

    pass
class Variable:

    pass
class LoopExp:

    pass
class ocl_expressions_IteratorExp(LoopExp):

    pass
class ocl_expressions_IterateExp(LoopExp):

    pass
class NumericLiteralExp:

    pass
class ocl_expressions_RealLiteralExp(NumericLiteralExp):

    def __init__(self, realSymbol: str):
        self.realSymbol = realSymbol
        
        pass
    @property
    def realSymbol(self):
        return self.__realSymbol

    @realSymbol.setter
    def realSymbol(self, realSymbol: str):
        self.__realSymbol = realSymbol


class ocl_expressions_IntegerLiteralExp(NumericLiteralExp):

    def __init__(self, integerSymbol: str):
        self.integerSymbol = integerSymbol
        
        pass
    @property
    def integerSymbol(self):
        return self.__integerSymbol

    @integerSymbol.setter
    def integerSymbol(self, integerSymbol: str):
        self.__integerSymbol = integerSymbol


class CallExp:

    pass
class ocl_expressions_LoopExp(CallExp):

    pass
class ocl_expressions_FeatureCallExp(CallExp):

    def __init__(self, markedPre: bool):
        self.markedPre = markedPre
        
        pass
    @property
    def markedPre(self):
        return self.__markedPre

    @markedPre.setter
    def markedPre(self, markedPre: bool):
        self.__markedPre = markedPre


class expressions_ocl_EEnumLiteral:

    pass
class TypedElement:

    pass
class ocl_expressions_CollectionLiteralPart(TypedElement):

    pass
class LiteralExp:

    pass
class ocl_expressions_NullLiteralExp(LiteralExp):

    pass
class ocl_expressions_TupleLiteralExp(LiteralExp):

    pass
class ocl_expressions_PrimitiveLiteralExp(LiteralExp):

    pass
class ocl_expressions_EnumLiteralExp(LiteralExp):

    pass
class ocl_expressions_InvalidLiteralExp(LiteralExp):

    pass
class ocl_expressions_CollectionLiteralExp(LiteralExp):

    def __init__(self, kind: str, ocl_expressions_CollectionLiteralExp: set["CollectionLiteralPart"] = None):
        self.kind = kind
        self.ocl_expressions_CollectionLiteralExp = ocl_expressions_CollectionLiteralExp if ocl_expressions_CollectionLiteralExp is not None else set()
        
        pass
    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind


    @property
    def ocl_expressions_CollectionLiteralExp(self):
        return self.__ocl_expressions_CollectionLiteralExp

    @ocl_expressions_CollectionLiteralExp.setter
    def ocl_expressions_CollectionLiteralExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ocl_expressions_CollectionLiteralExp__ocl_expressions_CollectionLiteralExp", None)
        self.__ocl_expressions_CollectionLiteralExp = value if value is not None else set()
        
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
class ocl_expressions_CollectionRange(CollectionLiteralPart):

    pass
class ocl_expressions_CollectionItem(CollectionLiteralPart):

    pass
class OCLExpression:

    pass
class ocl_expressions_LiteralExp(OCLExpression):

    pass
class ocl_expressions_LetExp(OCLExpression):

    pass
class ocl_expressions_IfExp(OCLExpression):

    pass
class ocl_expressions_StateExp(OCLExpression):

    pass
class ocl_expressions_TypeExp(OCLExpression):

    pass
class ocl_expressions_VariableExp(OCLExpression):

    pass
class utilities_CallingASTNode:

    pass
class expressions_OCLExpression:

    pass
class ocl_expressions_MessageExp(utilities_CallingASTNode, expressions_OCLExpression):

    pass
class ocl_expressions_CallExp(utilities_CallingASTNode, expressions_OCLExpression):

    pass
class PrimitiveLiteralExp:

    pass
class ocl_expressions_StringLiteralExp(PrimitiveLiteralExp):

    def __init__(self, stringSymbol: str):
        self.stringSymbol = stringSymbol
        
        pass
    @property
    def stringSymbol(self):
        return self.__stringSymbol

    @stringSymbol.setter
    def stringSymbol(self, stringSymbol: str):
        self.__stringSymbol = stringSymbol


class ocl_expressions_NumericLiteralExp(PrimitiveLiteralExp):

    pass
class ocl_expressions_BooleanLiteralExp(PrimitiveLiteralExp):

    def __init__(self, booleanSymbol: str):
        self.booleanSymbol = booleanSymbol
        
        pass
    @property
    def booleanSymbol(self):
        return self.__booleanSymbol

    @booleanSymbol.setter
    def booleanSymbol(self, booleanSymbol: str):
        self.__booleanSymbol = booleanSymbol


class expressions_ocl_EClass:

    pass
class NavigationCallExp:

    pass
class ocl_expressions_PropertyCallExp(NavigationCallExp):

    pass
class ocl_expressions_AssociationClassCallExp(NavigationCallExp):

    pass
class PrimitiveReal:

    pass
class ocl_types_PrimitiveInteger(PrimitiveReal):

    pass
class PrimitiveType:

    pass
class ocl_types_PrimitiveReal(PrimitiveType):

    pass
class ocl_types_PrimitiveString(PrimitiveType):

    pass
class ocl_types_PrimitiveBoolean(PrimitiveType):

    pass
class types_ocl_EClass:

    pass
class types_ocl_EOperation:

    pass
class EClass:

    pass
class ocl_types_TupleType(EClass):

    pass
class ocl_types_ElementType(EClass):

    pass
class types_ocl_EClassifier:

    pass
class utilities_TypedASTNode:

    pass
class ocl_expressions_UnspecifiedValueExp(utilities_TypedASTNode, expressions_OCLExpression):

    pass
class ocl_expressions_Variable(utilities_Visitable, utilities_TypedASTNode, uml_TypedElement):

    pass
class ocl_expressions_TupleLiteralPart(utilities_Visitable, utilities_TypedASTNode, uml_TypedElement):

    pass
class EDataType:

    pass
class CollectionType:

    pass
class ocl_types_OrderedSetType(CollectionType):

    pass
class ocl_types_SequenceType(CollectionType):

    pass
class ocl_types_SetType(CollectionType):

    pass
class ocl_types_BagType(CollectionType):

    pass
class utilities_PredefinedType:

    pass
class ocl_types_PrimitiveType(EDataType, utilities_PredefinedType):

    pass
class ocl_types_MessageType(EClass, utilities_PredefinedType):

    pass
class ocl_types_CollectionType(EDataType, utilities_PredefinedType, utilities_TypedASTNode):

    def __init__(self, kind: str, ocl_types_CollectionType: "types_ocl_EClassifier" = None):
        self.kind = kind
        self.ocl_types_CollectionType = ocl_types_CollectionType
        
        pass
    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind


    @property
    def ocl_types_CollectionType(self):
        return self.__ocl_types_CollectionType

    @ocl_types_CollectionType.setter
    def ocl_types_CollectionType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ocl_types_CollectionType__ocl_types_CollectionType", None)
        self.__ocl_types_CollectionType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_ocl_EClassifier"):
                opp_val = getattr(old_value, "types_ocl_EClassifier", None)
                if opp_val == self:
                    setattr(old_value, "types_ocl_EClassifier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_ocl_EClassifier"):
                opp_val = getattr(value, "types_ocl_EClassifier", None)
                setattr(value, "types_ocl_EClassifier", self)

class EClassifier:

    pass
class ocl_types_TypeType(utilities_PredefinedType, EClassifier):

    pass
class ocl_types_InvalidType(utilities_PredefinedType, EClassifier):

    pass
class ocl_types_VoidType(utilities_PredefinedType, EClassifier):

    pass
class ocl_types_AnyType(utilities_PredefinedType, EClassifier):

    pass