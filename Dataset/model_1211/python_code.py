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


############################################
# Definition of Classes
############################################

class ocl_expressions_VariableExp:

    def __init__(self):
        
        pass
    def var_type(self, ocl_context, ocl_diagnostics) :
        # TODO: Implement var_type method
        pass

class ocl_expressions_UnspecifiedValueExp:

    pass
class ocl_expressions_TypeExp:

    pass
class ocl_expressions_TupleLiteralExp:

    def __init__(self):
        
        pass
    def tuple_type(self, ocl_context, ocl_diagnostics) :
        # TODO: Implement tuple_type method
        pass

    def parts_unique(self, ocl_diagnostics, ocl_context) :
        # TODO: Implement parts_unique method
        pass

class ocl_expressions_TupleLiteralPart:

    def __init__(self):
        
        pass
    def value_type(self, ocl_diagnostics, ocl_context) :
        # TODO: Implement value_type method
        pass

class ocl_expressions_PropertyCallExp:

    def __init__(self):
        
        pass
    def property_type(self, ocl_diagnostics, ocl_context) :
        # TODO: Implement property_type method
        pass

class ocl_expressions_StringLiteralExp:

    def __init__(self, stringSymbol: str):
        self.stringSymbol = stringSymbol
        
        pass
    @property
    def stringSymbol(self):
        return self.__stringSymbol

    @stringSymbol.setter
    def stringSymbol(self, stringSymbol: str):
        self.__stringSymbol = stringSymbol


    def string_type(self, ocl_diagnostics, ocl_context) :
        # TODO: Implement string_type method
        pass

class ocl_expressions_StateExp:

    pass
class ocl_expressions_RealLiteralExp:

    def __init__(self, realSymbol: str):
        self.realSymbol = realSymbol
        
        pass
    @property
    def realSymbol(self):
        return self.__realSymbol

    @realSymbol.setter
    def realSymbol(self, realSymbol: str):
        self.__realSymbol = realSymbol


    def real_type(self, ocl_diagnostics, ocl_context) :
        # TODO: Implement real_type method
        pass

class ocl_expressions_OperationCallExp:

    def __init__(self, operationCode: int):
        self.operationCode = operationCode
        
        pass
    @property
    def operationCode(self):
        return self.__operationCode

    @operationCode.setter
    def operationCode(self, operationCode: int):
        self.__operationCode = operationCode


    def arguments_conform(self, ocl_context, ocl_diagnostics) :
        # TODO: Implement arguments_conform method
        pass

    def argument_count(self, ocl_context, ocl_diagnostics) :
        # TODO: Implement argument_count method
        pass

class ocl_expressions_NullLiteralExp:

    pass
class ocl_expressions_LetExp:

    def __init__(self):
        
        pass
    def let_type(self, ocl_context, ocl_diagnostics) :
        # TODO: Implement let_type method
        pass

class ocl_expressions_MessageExp:

    def __init__(self):
        
        pass
    def target_defines_operation(self, ocl_diagnostics, ocl_context) :
        # TODO: Implement target_defines_operation method
        pass

    def has_operation_or_signal(self, ocl_context, ocl_diagnostics) :
        # TODO: Implement has_operation_or_signal method
        pass

    def target_not_collection(self, ocl_context, ocl_diagnostics) :
        # TODO: Implement target_not_collection method
        pass

    def operation_arguments(self, ocl_diagnostics, ocl_context) :
        # TODO: Implement operation_arguments method
        pass

    def signal_arguments(self, ocl_diagnostics, ocl_context) :
        # TODO: Implement signal_arguments method
        pass

class ocl_expressions_Variable:

    def __init__(self):
        
        pass
    def init_type(self, ocl_context, ocl_diagnostics) :
        # TODO: Implement init_type method
        pass

class ocl_expressions_IteratorExp:

    def __init__(self):
        
        pass
    def boolean_body_type(self, ocl_context, ocl_diagnostics) :
        # TODO: Implement boolean_body_type method
        pass

    def collect_type(self, ocl_diagnostics, ocl_context) :
        # TODO: Implement collect_type method
        pass

    def select_reject_type(self, ocl_diagnostics, ocl_context) :
        # TODO: Implement select_reject_type method
        pass

    def boolean_type(self, ocl_context, ocl_diagnostics) :
        # TODO: Implement boolean_type method
        pass

class ocl_expressions_LoopExp(ABC):

    def __init__(self):
        
        pass
    def loop_variable_init(self, ocl_context, ocl_diagnostics) :
        # TODO: Implement loop_variable_init method
        pass

    def loop_variable_type(self, ocl_context, ocl_diagnostics) :
        # TODO: Implement loop_variable_type method
        pass

    def source_collection(self, ocl_diagnostics, ocl_context) :
        # TODO: Implement source_collection method
        pass

class ocl_expressions_IntegerLiteralExp:

    def __init__(self, integerSymbol: str, extendedIntegerSymbol: str, longSymbol: str):
        self.integerSymbol = integerSymbol
        self.extendedIntegerSymbol = extendedIntegerSymbol
        self.longSymbol = longSymbol
        
        pass
    @property
    def extendedIntegerSymbol(self):
        return self.__extendedIntegerSymbol

    @extendedIntegerSymbol.setter
    def extendedIntegerSymbol(self, extendedIntegerSymbol: str):
        self.__extendedIntegerSymbol = extendedIntegerSymbol


    @property
    def longSymbol(self):
        return self.__longSymbol

    @longSymbol.setter
    def longSymbol(self, longSymbol: str):
        self.__longSymbol = longSymbol


    @property
    def integerSymbol(self):
        return self.__integerSymbol

    @integerSymbol.setter
    def integerSymbol(self, integerSymbol: str):
        self.__integerSymbol = integerSymbol


    def integer_type(self, ocl_context, ocl_diagnostics) :
        # TODO: Implement integer_type method
        pass

class ocl_expressions_IterateExp:

    def __init__(self):
        
        pass
    def body_type(self, ocl_diagnostics, ocl_context) :
        # TODO: Implement body_type method
        pass

    def iterate_type(self, ocl_context, ocl_diagnostics) :
        # TODO: Implement iterate_type method
        pass

    def result_init(self, ocl_diagnostics, ocl_context) :
        # TODO: Implement result_init method
        pass

class ocl_expressions_InvalidLiteralExp:

    pass
class ocl_expressions_UnlimitedNaturalLiteralExp:

    def __init__(self, integerSymbol: str, unlimited: bool, extendedIntegerSymbol: str, longSymbol: str):
        self.integerSymbol = integerSymbol
        self.unlimited = unlimited
        self.extendedIntegerSymbol = extendedIntegerSymbol
        self.longSymbol = longSymbol
        
        pass
    @property
    def extendedIntegerSymbol(self):
        return self.__extendedIntegerSymbol

    @extendedIntegerSymbol.setter
    def extendedIntegerSymbol(self, extendedIntegerSymbol: str):
        self.__extendedIntegerSymbol = extendedIntegerSymbol


    @property
    def unlimited(self):
        return self.__unlimited

    @unlimited.setter
    def unlimited(self, unlimited: bool):
        self.__unlimited = unlimited


    @property
    def longSymbol(self):
        return self.__longSymbol

    @longSymbol.setter
    def longSymbol(self, longSymbol: str):
        self.__longSymbol = longSymbol


    @property
    def integerSymbol(self):
        return self.__integerSymbol

    @integerSymbol.setter
    def integerSymbol(self, integerSymbol: str):
        self.__integerSymbol = integerSymbol


    def natural_type(self, ocl_context, ocl_diagnostics) :
        # TODO: Implement natural_type method
        pass

class ocl_expressions_NumericLiteralExp(ABC):

    pass
class ocl_expressions_CollectionRange:

    def __init__(self):
        
        pass
    def range_type(self, ocl_context, ocl_diagnostics) :
        # TODO: Implement range_type method
        pass

class ocl_expressions_IfExp:

    def __init__(self):
        
        pass
    def if_type(self, ocl_context, ocl_diagnostics) :
        # TODO: Implement if_type method
        pass

    def boolean_condition(self, ocl_diagnostics, ocl_context) :
        # TODO: Implement boolean_condition method
        pass

class ocl_expressions_EnumLiteralExp:

    def __init__(self):
        
        pass
    def enum_type(self, ocl_context, ocl_diagnostics) :
        # TODO: Implement enum_type method
        pass

class ocl_expressions_CollectionLiteralExp:

    def __init__(self, kind: str, simpleRange: bool):
        self.kind = kind
        self.simpleRange = simpleRange
        
        pass
    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind


    @property
    def simpleRange(self):
        return self.__simpleRange

    @simpleRange.setter
    def simpleRange(self, simpleRange: bool):
        self.__simpleRange = simpleRange


    def set_kind(self, ocl_context, ocl_diagnostics) :
        # TODO: Implement set_kind method
        pass

    def sequence_kind(self, ocl_context, ocl_diagnostics) :
        # TODO: Implement sequence_kind method
        pass

    def no_collection_instances(self, ocl_diagnostics, ocl_context) :
        # TODO: Implement no_collection_instances method
        pass

    def element_type(self, ocl_context, ocl_diagnostics) :
        # TODO: Implement element_type method
        pass

    def bag_kind(self, ocl_context, ocl_diagnostics) :
        # TODO: Implement bag_kind method
        pass

class ocl_expressions_CallExp(ABC):

    pass
class ocl_expressions_FeatureCallExp(ABC):

    def __init__(self, markedPre: bool):
        self.markedPre = markedPre
        
        pass
    @property
    def markedPre(self):
        return self.__markedPre

    @markedPre.setter
    def markedPre(self, markedPre: bool):
        self.__markedPre = markedPre


class ocl_expressions_CollectionLiteralPart(ABC):

    pass
class ocl_expressions_CollectionItem:

    def __init__(self):
        
        pass
    def item_type(self, ocl_diagnostics, ocl_context) :
        # TODO: Implement item_type method
        pass

class ocl_expressions_LiteralExp(ABC):

    pass
class ocl_expressions_PrimitiveLiteralExp(ABC):

    pass
class ocl_expressions_BooleanLiteralExp:

    def __init__(self, booleanSymbol: str):
        self.booleanSymbol = booleanSymbol
        
        pass
    @property
    def booleanSymbol(self):
        return self.__booleanSymbol

    @booleanSymbol.setter
    def booleanSymbol(self, booleanSymbol: str):
        self.__booleanSymbol = booleanSymbol


    def boolean_type(self, ocl_context, ocl_diagnostics) :
        # TODO: Implement boolean_type method
        pass

class ocl_expressions_OCLExpression(ABC):

    pass
class ocl_expressions_NavigationCallExp(ABC):

    pass
class ocl_expressions_AssociationClassCallExp:

    pass
class ocl_utilities_PredefinedType(ABC):

    def __init__(self):
        
        pass
    def oclOperations(self):
        # TODO: Implement oclOperations method
        pass

    def getName(self) :
        # TODO: Implement getName method
        pass

class Visitable:

    pass
class ocl_utilities_ExpressionInOCL(Visitable):

    pass
class ocl_utilities_TypedElement(ABC):

    def __init__(self):
        
        pass
    def getName(self) :
        # TODO: Implement getName method
        pass

    def getType(self):
        # TODO: Implement getType method
        pass

    def setType(self, ocl_type):
        # TODO: Implement setType method
        pass

    def setName(self, ocl_name):
        # TODO: Implement setName method
        pass

class ASTNode:

    pass
class ocl_utilities_CallingASTNode(ASTNode):

    def __init__(self, propertyStartPosition: int, propertyEndPosition: int):
        self.propertyStartPosition = propertyStartPosition
        self.propertyEndPosition = propertyEndPosition
        
        pass
    @property
    def propertyEndPosition(self):
        return self.__propertyEndPosition

    @propertyEndPosition.setter
    def propertyEndPosition(self, propertyEndPosition: int):
        self.__propertyEndPosition = propertyEndPosition


    @property
    def propertyStartPosition(self):
        return self.__propertyStartPosition

    @propertyStartPosition.setter
    def propertyStartPosition(self, propertyStartPosition: int):
        self.__propertyStartPosition = propertyStartPosition


class ocl_utilities_ASTNode(ABC):

    def __init__(self, startPosition: int, endPosition: int):
        self.startPosition = startPosition
        self.endPosition = endPosition
        
        pass
    @property
    def startPosition(self):
        return self.__startPosition

    @startPosition.setter
    def startPosition(self, startPosition: int):
        self.__startPosition = startPosition


    @property
    def endPosition(self):
        return self.__endPosition

    @endPosition.setter
    def endPosition(self, endPosition: int):
        self.__endPosition = endPosition


class ocl_types_VoidType:

    pass
class ocl_utilities_Visitor(ABC):

    def __init__(self):
        
        pass
    def visitNullLiteralExp(self, ocl_literalExp):
        # TODO: Implement visitNullLiteralExp method
        pass

    def visitOperationCallExp(self, ocl_callExp):
        # TODO: Implement visitOperationCallExp method
        pass

    def visitAssociationClassCallExp(self, ocl_callExp):
        # TODO: Implement visitAssociationClassCallExp method
        pass

    def visitRealLiteralExp(self, ocl_literalExp):
        # TODO: Implement visitRealLiteralExp method
        pass

    def visitIterateExp(self, ocl_callExp):
        # TODO: Implement visitIterateExp method
        pass

    def visitMessageExp(self, ocl_messageExp):
        # TODO: Implement visitMessageExp method
        pass

    def visitCollectionLiteralExp(self, ocl_literalExp):
        # TODO: Implement visitCollectionLiteralExp method
        pass

    def visitPropertyCallExp(self, ocl_callExp):
        # TODO: Implement visitPropertyCallExp method
        pass

    def visitCollectionRange(self, ocl_range):
        # TODO: Implement visitCollectionRange method
        pass

    def visitExpressionInOCL(self, ocl_expression):
        # TODO: Implement visitExpressionInOCL method
        pass

    def visitTypeExp(self, ocl_typeExp):
        # TODO: Implement visitTypeExp method
        pass

    def visitIteratorExp(self, ocl_callExp):
        # TODO: Implement visitIteratorExp method
        pass

    def visitVariableExp(self, ocl_variableExp):
        # TODO: Implement visitVariableExp method
        pass

    def visitTupleLiteralExp(self, ocl_literalExp):
        # TODO: Implement visitTupleLiteralExp method
        pass

    def visitInvalidLiteralExp(self, ocl_literalExp):
        # TODO: Implement visitInvalidLiteralExp method
        pass

    def visitTupleLiteralPart(self, ocl_part):
        # TODO: Implement visitTupleLiteralPart method
        pass

    def visitStringLiteralExp(self, ocl_literalExp):
        # TODO: Implement visitStringLiteralExp method
        pass

    def visitEnumLiteralExp(self, ocl_literalExp):
        # TODO: Implement visitEnumLiteralExp method
        pass

    def visitConstraint(self, ocl_constraint):
        # TODO: Implement visitConstraint method
        pass

    def visitIfExp(self, ocl_ifExp):
        # TODO: Implement visitIfExp method
        pass

    def visitUnlimitedNaturalLiteralExp(self, ocl_literalExp):
        # TODO: Implement visitUnlimitedNaturalLiteralExp method
        pass

    def visitCollectionItem(self, ocl_item):
        # TODO: Implement visitCollectionItem method
        pass

    def visitLetExp(self, ocl_letExp):
        # TODO: Implement visitLetExp method
        pass

    def visitUnspecifiedValueExp(self, ocl_unspecExp):
        # TODO: Implement visitUnspecifiedValueExp method
        pass

    def visitVariable(self, ocl_variable):
        # TODO: Implement visitVariable method
        pass

    def visitIntegerLiteralExp(self, ocl_literalExp):
        # TODO: Implement visitIntegerLiteralExp method
        pass

    def visitStateExp(self, ocl_stateExp):
        # TODO: Implement visitStateExp method
        pass

    def visitBooleanLiteralExp(self, ocl_literalExp):
        # TODO: Implement visitBooleanLiteralExp method
        pass

class ocl_utilities_Visitable(ABC):

    def __init__(self):
        
        pass
    def accept(self, ocl_v):
        # TODO: Implement accept method
        pass

class ocl_utilities_TypedASTNode(ASTNode):

    def __init__(self, typeStartPosition: int, typeEndPosition: int):
        self.typeStartPosition = typeStartPosition
        self.typeEndPosition = typeEndPosition
        
        pass
    @property
    def typeStartPosition(self):
        return self.__typeStartPosition

    @typeStartPosition.setter
    def typeStartPosition(self, typeStartPosition: int):
        self.__typeStartPosition = typeStartPosition


    @property
    def typeEndPosition(self):
        return self.__typeEndPosition

    @typeEndPosition.setter
    def typeEndPosition(self, typeEndPosition: int):
        self.__typeEndPosition = typeEndPosition


class ocl_types_TupleType:

    def __init__(self):
        
        pass
    def features_only_properties(self, ocl_context, ocl_diagnostics) :
        # TODO: Implement features_only_properties method
        pass

    def oclProperties(self):
        # TODO: Implement oclProperties method
        pass

    def tuple_type_name(self, ocl_diagnostics, ocl_context) :
        # TODO: Implement tuple_type_name method
        pass

    def part_names_unique(self, ocl_context, ocl_diagnostics) :
        # TODO: Implement part_names_unique method
        pass

class ocl_types_TemplateParameterType:

    def __init__(self, specification: str):
        self.specification = specification
        
        pass
    @property
    def specification(self):
        return self.__specification

    @specification.setter
    def specification(self, specification: str):
        self.__specification = specification


class ocl_types_TypeType:

    pass
class ocl_types_SetType:

    pass
class ocl_types_SequenceType:

    pass
class ocl_types_PrimitiveType:

    pass
class ocl_types_OrderedSetType:

    pass
class ocl_types_MessageType:

    def __init__(self):
        
        pass
    def exclusive_signature(self, ocl_diagnostics, ocl_context) :
        # TODO: Implement exclusive_signature method
        pass

    def oclProperties(self):
        # TODO: Implement oclProperties method
        pass

    def operation_parameters(self, ocl_context, ocl_diagnostics) :
        # TODO: Implement operation_parameters method
        pass

    def signal_attributes(self, ocl_diagnostics, ocl_context) :
        # TODO: Implement signal_attributes method
        pass

class ocl_types_InvalidType:

    pass
class ocl_types_ElementType:

    pass
class ocl_types_CollectionType:

    def __init__(self, kind: str):
        self.kind = kind
        
        pass
    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind


    def no_invalid_values(self, ocl_context, ocl_diagnostics) :
        # TODO: Implement no_invalid_values method
        pass

    def collection_type_name(self, ocl_context, ocl_diagnostics) :
        # TODO: Implement collection_type_name method
        pass

    def oclIterators(self):
        # TODO: Implement oclIterators method
        pass

class ocl_types_BagType:

    pass
class ocl_types_AnyType:

    pass