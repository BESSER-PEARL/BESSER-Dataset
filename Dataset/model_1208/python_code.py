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

class ocl_expressions_TupleLiteralPart:

    def __init__(self):
        
    def value_type(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement value_type method
        pass

class ocl_expressions_VariableExp:

    def __init__(self):
        
    def var_type(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement var_type method
        pass

class ocl_expressions_UnspecifiedValueExp:

    pass
class ocl_expressions_TypeExp:

    pass
class ocl_expressions_RealLiteralExp:

    def __init__(self, realSymbol: str):
        self.realSymbol = realSymbol
        
    @property
    def realSymbol(self) -> str:
        return self.__realSymbol

    @realSymbol.setter
    def realSymbol(self, realSymbol: str):
        self.__realSymbol = realSymbol

    def real_type(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement real_type method
        pass

class ocl_expressions_TupleLiteralExp:

    def __init__(self):
        
    def tuple_type(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement tuple_type method
        pass

    def parts_unique(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement parts_unique method
        pass

class ocl_expressions_StringLiteralExp:

    def __init__(self, stringSymbol: str):
        self.stringSymbol = stringSymbol
        
    @property
    def stringSymbol(self) -> str:
        return self.__stringSymbol

    @stringSymbol.setter
    def stringSymbol(self, stringSymbol: str):
        self.__stringSymbol = stringSymbol

    def string_type(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement string_type method
        pass

class ocl_expressions_StateExp:

    pass
class ocl_expressions_OperationCallExp:

    def __init__(self, operationCode: int):
        self.operationCode = operationCode
        
    @property
    def operationCode(self) -> int:
        return self.__operationCode

    @operationCode.setter
    def operationCode(self, operationCode: int):
        self.__operationCode = operationCode

    def argument_count(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement argument_count method
        pass

    def arguments_conform(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement arguments_conform method
        pass

class ocl_expressions_NullLiteralExp:

    pass
class ocl_expressions_PropertyCallExp:

    def __init__(self):
        
    def property_type(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement property_type method
        pass

class ocl_expressions_MessageExp:

    def __init__(self):
        
    def has_operation_or_signal(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement has_operation_or_signal method
        pass

    def target_not_collection(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement target_not_collection method
        pass

    def operation_arguments(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement operation_arguments method
        pass

    def signal_arguments(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement signal_arguments method
        pass

    def target_defines_operation(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement target_defines_operation method
        pass

class ocl_expressions_LetExp:

    def __init__(self):
        
    def let_type(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement let_type method
        pass

class ocl_expressions_IteratorExp:

    def __init__(self):
        
    def boolean_body_type(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement boolean_body_type method
        pass

    def select_reject_type(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement select_reject_type method
        pass

    def boolean_type(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement boolean_type method
        pass

    def collect_type(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement collect_type method
        pass

class ocl_expressions_Variable:

    def __init__(self):
        
    def init_type(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement init_type method
        pass

class ocl_expressions_IterateExp:

    def __init__(self):
        
    def iterate_type(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement iterate_type method
        pass

    def body_type(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement body_type method
        pass

    def result_init(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement result_init method
        pass

class ocl_expressions_InvalidLiteralExp:

    pass
class ocl_expressions_LoopExp(ABC):

    def __init__(self):
        
    def loop_variable_init(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement loop_variable_init method
        pass

    def source_collection(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement source_collection method
        pass

    def loop_variable_type(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement loop_variable_type method
        pass

class ocl_expressions_IfExp:

    def __init__(self):
        
    def boolean_condition(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement boolean_condition method
        pass

    def if_type(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement if_type method
        pass

class ocl_expressions_UnlimitedNaturalLiteralExp:

    def __init__(self, integerSymbol: str, unlimited: bool):
        self.integerSymbol = integerSymbol
        self.unlimited = unlimited
        
    @property
    def unlimited(self) -> bool:
        return self.__unlimited

    @unlimited.setter
    def unlimited(self, unlimited: bool):
        self.__unlimited = unlimited

    @property
    def integerSymbol(self) -> str:
        return self.__integerSymbol

    @integerSymbol.setter
    def integerSymbol(self, integerSymbol: str):
        self.__integerSymbol = integerSymbol

    def natural_type(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement natural_type method
        pass

class ocl_expressions_NumericLiteralExp(ABC):

    pass
class ocl_expressions_IntegerLiteralExp:

    def __init__(self, integerSymbol: str):
        self.integerSymbol = integerSymbol
        
    @property
    def integerSymbol(self) -> str:
        return self.__integerSymbol

    @integerSymbol.setter
    def integerSymbol(self, integerSymbol: str):
        self.__integerSymbol = integerSymbol

    def integer_type(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement integer_type method
        pass

class ocl_expressions_CollectionRange:

    def __init__(self):
        
    def range_type(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement range_type method
        pass

class ocl_expressions_EnumLiteralExp:

    def __init__(self):
        
    def enum_type(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement enum_type method
        pass

class ocl_expressions_CollectionItem:

    def __init__(self):
        
    def item_type(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement item_type method
        pass

class ocl_expressions_LiteralExp(ABC):

    pass
class ocl_expressions_PrimitiveLiteralExp(ABC):

    pass
class ocl_expressions_BooleanLiteralExp:

    def __init__(self, booleanSymbol: str):
        self.booleanSymbol = booleanSymbol
        
    @property
    def booleanSymbol(self) -> str:
        return self.__booleanSymbol

    @booleanSymbol.setter
    def booleanSymbol(self, booleanSymbol: str):
        self.__booleanSymbol = booleanSymbol

    def boolean_type(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement boolean_type method
        pass

class ocl_expressions_OCLExpression(ABC):

    pass
class ocl_expressions_CollectionLiteralExp:

    def __init__(self, kind: str, simpleRange: bool):
        self.kind = kind
        self.simpleRange = simpleRange
        
    @property
    def simpleRange(self) -> bool:
        return self.__simpleRange

    @simpleRange.setter
    def simpleRange(self, simpleRange: bool):
        self.__simpleRange = simpleRange

    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    def sequence_kind(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement sequence_kind method
        pass

    def no_collection_instances(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement no_collection_instances method
        pass

    def bag_kind(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement bag_kind method
        pass

    def set_kind(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement set_kind method
        pass

    def element_type(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement element_type method
        pass

class ocl_expressions_CollectionLiteralPart(ABC):

    pass
class ocl_utilities_PredefinedType(ABC):

    def __init__(self):
        
    def oclOperations(self):
        # TODO: Implement oclOperations method
        pass

    def getName(self) -> str:
        # TODO: Implement getName method
        pass

class Visitable:

    pass
class ocl_utilities_ExpressionInOCL(Visitable):

    pass
class ocl_expressions_CallExp(ABC):

    pass
class ocl_expressions_FeatureCallExp(ABC):

    def __init__(self, markedPre: bool):
        self.markedPre = markedPre
        
    @property
    def markedPre(self) -> bool:
        return self.__markedPre

    @markedPre.setter
    def markedPre(self, markedPre: bool):
        self.__markedPre = markedPre

class ocl_expressions_NavigationCallExp(ABC):

    pass
class ocl_expressions_AssociationClassCallExp:

    pass
class ocl_utilities_TypedElement(ABC):

    def __init__(self):
        
    def getName(self) -> str:
        # TODO: Implement getName method
        pass

    def setType(self, type: str):
        # TODO: Implement setType method
        pass

    def getType(self):
        # TODO: Implement getType method
        pass

    def setName(self, name: str):
        # TODO: Implement setName method
        pass

class ocl_utilities_Visitable(ABC):

    def __init__(self):
        
    def accept(self, v: str):
        # TODO: Implement accept method
        pass

class ASTNode:

    pass
class ocl_utilities_TypedASTNode(ASTNode):

    def __init__(self, typeStartPosition: int, typeEndPosition: int):
        self.typeStartPosition = typeStartPosition
        self.typeEndPosition = typeEndPosition
        
    @property
    def typeEndPosition(self) -> int:
        return self.__typeEndPosition

    @typeEndPosition.setter
    def typeEndPosition(self, typeEndPosition: int):
        self.__typeEndPosition = typeEndPosition

    @property
    def typeStartPosition(self) -> int:
        return self.__typeStartPosition

    @typeStartPosition.setter
    def typeStartPosition(self, typeStartPosition: int):
        self.__typeStartPosition = typeStartPosition

class ocl_utilities_CallingASTNode(ASTNode):

    def __init__(self, propertyStartPosition: int, propertyEndPosition: int):
        self.propertyStartPosition = propertyStartPosition
        self.propertyEndPosition = propertyEndPosition
        
    @property
    def propertyEndPosition(self) -> int:
        return self.__propertyEndPosition

    @propertyEndPosition.setter
    def propertyEndPosition(self, propertyEndPosition: int):
        self.__propertyEndPosition = propertyEndPosition

    @property
    def propertyStartPosition(self) -> int:
        return self.__propertyStartPosition

    @propertyStartPosition.setter
    def propertyStartPosition(self, propertyStartPosition: int):
        self.__propertyStartPosition = propertyStartPosition

class ocl_utilities_ASTNode(ABC):

    def __init__(self, startPosition: int, endPosition: int):
        self.startPosition = startPosition
        self.endPosition = endPosition
        
    @property
    def startPosition(self) -> int:
        return self.__startPosition

    @startPosition.setter
    def startPosition(self, startPosition: int):
        self.__startPosition = startPosition

    @property
    def endPosition(self) -> int:
        return self.__endPosition

    @endPosition.setter
    def endPosition(self, endPosition: int):
        self.__endPosition = endPosition

class ocl_types_VoidType:

    pass
class ocl_utilities_Visitor(ABC):

    def __init__(self):
        
    def visitCollectionRange(self, range: str):
        # TODO: Implement visitCollectionRange method
        pass

    def visitIteratorExp(self, callExp: str):
        # TODO: Implement visitIteratorExp method
        pass

    def visitUnlimitedNaturalLiteralExp(self, literalExp: str):
        # TODO: Implement visitUnlimitedNaturalLiteralExp method
        pass

    def visitUnspecifiedValueExp(self, unspecExp: str):
        # TODO: Implement visitUnspecifiedValueExp method
        pass

    def visitConstraint(self, constraint: str):
        # TODO: Implement visitConstraint method
        pass

    def visitOperationCallExp(self, callExp: str):
        # TODO: Implement visitOperationCallExp method
        pass

    def visitIfExp(self, ifExp: str):
        # TODO: Implement visitIfExp method
        pass

    def visitPropertyCallExp(self, callExp: str):
        # TODO: Implement visitPropertyCallExp method
        pass

    def visitTypeExp(self, typeExp: str):
        # TODO: Implement visitTypeExp method
        pass

    def visitBooleanLiteralExp(self, literalExp: str):
        # TODO: Implement visitBooleanLiteralExp method
        pass

    def visitVariableExp(self, variableExp: str):
        # TODO: Implement visitVariableExp method
        pass

    def visitStateExp(self, stateExp: str):
        # TODO: Implement visitStateExp method
        pass

    def visitNullLiteralExp(self, literalExp: str):
        # TODO: Implement visitNullLiteralExp method
        pass

    def visitEnumLiteralExp(self, literalExp: str):
        # TODO: Implement visitEnumLiteralExp method
        pass

    def visitVariable(self, variable: str):
        # TODO: Implement visitVariable method
        pass

    def visitIntegerLiteralExp(self, literalExp: str):
        # TODO: Implement visitIntegerLiteralExp method
        pass

    def visitInvalidLiteralExp(self, literalExp: str):
        # TODO: Implement visitInvalidLiteralExp method
        pass

    def visitCollectionItem(self, item: str):
        # TODO: Implement visitCollectionItem method
        pass

    def visitRealLiteralExp(self, literalExp: str):
        # TODO: Implement visitRealLiteralExp method
        pass

    def visitStringLiteralExp(self, literalExp: str):
        # TODO: Implement visitStringLiteralExp method
        pass

    def visitTupleLiteralExp(self, literalExp: str):
        # TODO: Implement visitTupleLiteralExp method
        pass

    def visitLetExp(self, letExp: str):
        # TODO: Implement visitLetExp method
        pass

    def visitAssociationClassCallExp(self, callExp: str):
        # TODO: Implement visitAssociationClassCallExp method
        pass

    def visitIterateExp(self, callExp: str):
        # TODO: Implement visitIterateExp method
        pass

    def visitCollectionLiteralExp(self, literalExp: str):
        # TODO: Implement visitCollectionLiteralExp method
        pass

    def visitTupleLiteralPart(self, part: str):
        # TODO: Implement visitTupleLiteralPart method
        pass

    def visitExpressionInOCL(self, expression: str):
        # TODO: Implement visitExpressionInOCL method
        pass

    def visitMessageExp(self, messageExp: str):
        # TODO: Implement visitMessageExp method
        pass

class ocl_types_TupleType:

    def __init__(self):
        
    def part_names_unique(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement part_names_unique method
        pass

    def features_only_properties(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement features_only_properties method
        pass

    def tuple_type_name(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement tuple_type_name method
        pass

    def oclProperties(self):
        # TODO: Implement oclProperties method
        pass

class ocl_types_TemplateParameterType:

    def __init__(self, specification: str):
        self.specification = specification
        
    @property
    def specification(self) -> str:
        return self.__specification

    @specification.setter
    def specification(self, specification: str):
        self.__specification = specification

class ocl_types_TypeType:

    pass
class ocl_types_OrderedSetType:

    pass
class ocl_types_SetType:

    pass
class ocl_types_SequenceType:

    pass
class ocl_types_PrimitiveType:

    pass
class ocl_types_CollectionType:

    def __init__(self, kind: str):
        self.kind = kind
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    def collection_type_name(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement collection_type_name method
        pass

    def oclIterators(self):
        # TODO: Implement oclIterators method
        pass

    def no_invalid_values(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement no_invalid_values method
        pass

class ocl_types_MessageType:

    def __init__(self):
        
    def oclProperties(self):
        # TODO: Implement oclProperties method
        pass

    def operation_parameters(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement operation_parameters method
        pass

    def signal_attributes(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement signal_attributes method
        pass

    def exclusive_signature(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement exclusive_signature method
        pass

class ocl_types_InvalidType:

    pass
class ocl_types_ElementType:

    pass
class ocl_types_BagType:

    pass
class ocl_types_AnyType:

    pass