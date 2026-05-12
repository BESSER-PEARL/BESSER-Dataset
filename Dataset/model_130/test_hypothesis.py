import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ActualParameterExpression,
    gastm_ByReferenceActualParameterExpression,
    gastm_ByValueActualParameterExpression,
    UnaryOperator,
    gastm_BitNot,
    gastm_Decrement,
    gastm_Deref,
    gastm_Not,
    gastm_Negate,
    gastm_AddressOf,
    gastm_Increment,
    gastm_PostIncrement,
    gastm_PostDecrement,
    gastm_UnaryPlus,
    Literal,
    gastm_StringLiteral,
    gastm_BitLiteral,
    gastm_BooleanLiteral,
    gastm_CharLiteral,
    gastm_RealLiteral,
    gastm_IntegerlLiteral,
    QualifiedIdentifierReference,
    gastm_QualifiedOverData,
    gastm_QualifiedOverPointer,
    ForStatement,
    gastm_ForCheckAfterStatement,
    gastm_ForCheckBeforeStatement,
    AccessKind,
    gastm_Private,
    gastm_Protected,
    gastm_Public,
    PrimitiveType,
    gastm_WideCharacter,
    gastm_Integer,
    gastm_Boolean,
    gastm_Double,
    gastm_Float,
    gastm_Byte,
    gastm_LongInteger,
    gastm_String,
    gastm_Character,
    gastm_LongDouble,
    gastm_ShortInteger,
    gastm_Void,
    ActualParameter,
    gastm_MissingActualParameter,
    gastm_ActualParameterExpression,
    BinaryOperator,
    gastm_Assign,
    gastm_Exponent,
    gastm_BitLeftShift,
    gastm_Divide,
    gastm_NotGreater,
    gastm_BitRightShift,
    gastm_BitAnd,
    gastm_Equal,
    gastm_NotLess,
    gastm_Less,
    gastm_Greater,
    gastm_BitOr,
    gastm_Subtract,
    gastm_Or,
    gastm_BitXor,
    gastm_Add,
    gastm_Multiply,
    gastm_NotEqual,
    gastm_Modulus,
    gastm_And,
    gastm_OperatorAssign,
    IdentifierReference,
    NameReference,
    gastm_TypeQualifiedIdentifierReference,
    gastm_QualifiedIdentifierReference,
    LoopStatement,
    gastm_DoWhileStatement,
    gastm_WhileStatement,
    gastm_ForStatement,
    CatchBlock,
    gastm_TypesCatchBlock,
    gastm_VariableCatchBlock,
    BlockScope,
    SwitchCase,
    gastm_CaseBlock,
    gastm_DefaultBlock,
    LabelDefinition,
    LabelAccess,
    DerivesFrom,
    EnumLiteralDefinition,
    FormalParameterType,
    gastm_ByValueFormalParameterType,
    gastm_ByReferenceFormalParameterType,
    Type,
    gastm_FunctionType,
    Dimension,
    ConstructedType,
    gastm_ReferenceType,
    gastm_RangeType,
    gastm_CollectionType,
    gastm_PointerType,
    gastm_ArrayType,
    AggregateScope,
    DataType,
    gastm_ExceptionType,
    gastm_ConstructedType,
    gastm_EnumType,
    gastm_AggregateType,
    gastm_NamedType,
    gastm_FormalParameterType,
    gastm_PrimitiveType,
    GASTMSyntaxObject,
    gastm_DefinitionObject,
    gastm_Expression,
    gastm_PreprocessorElement,
    gastm_Type,
    MacroDefinition,
    LabelType,
    NameSpaceType,
    AggregateType,
    gastm_AnnotationType,
    gastm_StructureType,
    gastm_UnionType,
    gastm_ClassType,
    NamedType,
    TypeDefinition,
    gastm_AggregateTypeDefinition,
    gastm_NamedTypeDefinition,
    Definition,
    gastm_EnumLiteralDefinition,
    DataDefinition,
    gastm_BitFieldDefinition,
    Expression,
    gastm_BinaryExpression,
    gastm_ArrayAccess,
    gastm_Literal,
    gastm_AggregateExpression,
    gastm_NewExpression,
    gastm_ConditionalExpression,
    gastm_CastExpression,
    gastm_UnaryExpression,
    gastm_RangeExpression,
    gastm_NameReference,
    gastm_DataDefinition,
    gastm_EntryDefinition,
    VirtualSpecification,
    gastm_PureVirtual,
    gastm_NonVirtual,
    gastm_Virtual,
    gastm_FunctionMemberAttributes,
    FunctionScope,
    Statement,
    gastm_EmptyStatement,
    gastm_ThrowStatement,
    gastm_ExpressionStatement,
    gastm_IfStatement,
    gastm_LoopStatement,
    gastm_LabeledStatement,
    gastm_JumpStatement,
    gastm_TerminateStatement,
    gastm_TryStatement,
    gastm_ReturnStatement,
    gastm_DeclarationOrDefinitionStatement,
    gastm_BreakStatement,
    gastm_BlockStatement,
    gastm_ContinueStatement,
    gastm_SwitchStatement,
    gastm_DeleteStatement,
    FormalParameterDefinition,
    gastm_FunctionDefinition,
    FunctionMemberAttributes,
    FormalParameterDeclaration,
    Declaration,
    gastm_VariableDeclaration,
    gastm_FunctionDeclaration,
    SourceFile,
    TypeReference,
    gastm_NamedTypeReference,
    gastm_UnnamedTypeReference,
    Name,
    DeclarationOrDefinition,
    gastm_Declaration,
    gastm_Definition,
    ProgramScope,
    OtherSyntaxObject,
    gastm_SwitchCase,
    gastm_Dimension,
    gastm_Name,
    gastm_CatchBlock,
    gastm_DerivesFrom,
    gastm_CompilationUnit,
    AnnotationExpression,
    PreprocessorElement,
    gastm_MacroCall,
    gastm_MacroDefinition,
    gastm_Comment,
    gastm_IncludeUnit,
    SourceLocation,
    GASTMObject,
    gastm_GASTMSyntaxObject,
    Scope,
    gastm_GlobalScope,
    DefinitionObject,
    gastm_NameSpaceDefinition,
    gastm_LabelDefinition,
    gastm_DeclarationOrDefinition,
    gastm_TypeDefinition,
    GlobalScope,
    CompilationUnit,
    GASTMSemanticObject,
    gastm_Scope,
    gastm_Project,
    GASTMSourceObject,
    gastm_SourceLocation,
    gastm_SourceFile,
    gastm_ActualParameter,
    gastm_BinaryOperator,
    gastm_UnaryOperator,
    gastm_AccessKind,
    gastm_DataType,
    gastm_StorageSpecification,
    gastm_OtherSyntaxObject,
    gastm_GASTMSemanticObject,
    gastm_GASTMSourceObject,
    gastm_GASTMObject,
    StorageSpecification,
    gastm_FunctionPersistent,
    gastm_FileLocal,
    gastm_NoDef,
    gastm_PerClassMember,
    gastm_External,
    gastm_FunctionMemberAttribute,
    gastm_VariableDefinition,
    gastm_FormalParameterDeclaration,
    gastm_VirtualSpecification,
    gastm_FormalParameterDefinition,
    gastm_IdentifierReference,
    gastm_BlockScope,
    gastm_AggregateScope,
    gastm_LabelType,
    gastm_NameSpaceType,
    gastm_FunctionScope,
    gastm_Statement,
    gastm_TypeReference,
    gastm_ProgramScope,
    gastm_FunctionCallExpression,
    gastm_AnnotationExpression,
    gastm_LabelAccess,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_actualparameterexpression_is_not_abstract():
    assert not inspect.isabstract(ActualParameterExpression)


def test_actualparameterexpression_constructor_exists():
    assert callable(ActualParameterExpression.__init__)


def test_actualparameterexpression_constructor_args():
    sig = inspect.signature(ActualParameterExpression.__init__)
    params = list(sig.parameters.keys())



def test_gastm_byreferenceactualparameterexpression_is_not_abstract():
    assert not inspect.isabstract(gastm_ByReferenceActualParameterExpression)


def test_gastm_byreferenceactualparameterexpression_constructor_exists():
    assert callable(gastm_ByReferenceActualParameterExpression.__init__)


def test_gastm_byreferenceactualparameterexpression_constructor_args():
    sig = inspect.signature(gastm_ByReferenceActualParameterExpression.__init__)
    params = list(sig.parameters.keys())



def test_gastm_byvalueactualparameterexpression_is_not_abstract():
    assert not inspect.isabstract(gastm_ByValueActualParameterExpression)


def test_gastm_byvalueactualparameterexpression_constructor_exists():
    assert callable(gastm_ByValueActualParameterExpression.__init__)


def test_gastm_byvalueactualparameterexpression_constructor_args():
    sig = inspect.signature(gastm_ByValueActualParameterExpression.__init__)
    params = list(sig.parameters.keys())



def test_unaryoperator_is_not_abstract():
    assert not inspect.isabstract(UnaryOperator)


def test_unaryoperator_constructor_exists():
    assert callable(UnaryOperator.__init__)


def test_unaryoperator_constructor_args():
    sig = inspect.signature(UnaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_gastm_bitnot_is_not_abstract():
    assert not inspect.isabstract(gastm_BitNot)


def test_gastm_bitnot_constructor_exists():
    assert callable(gastm_BitNot.__init__)


def test_gastm_bitnot_constructor_args():
    sig = inspect.signature(gastm_BitNot.__init__)
    params = list(sig.parameters.keys())



def test_gastm_decrement_is_not_abstract():
    assert not inspect.isabstract(gastm_Decrement)


def test_gastm_decrement_constructor_exists():
    assert callable(gastm_Decrement.__init__)


def test_gastm_decrement_constructor_args():
    sig = inspect.signature(gastm_Decrement.__init__)
    params = list(sig.parameters.keys())



def test_gastm_deref_is_not_abstract():
    assert not inspect.isabstract(gastm_Deref)


def test_gastm_deref_constructor_exists():
    assert callable(gastm_Deref.__init__)


def test_gastm_deref_constructor_args():
    sig = inspect.signature(gastm_Deref.__init__)
    params = list(sig.parameters.keys())



def test_gastm_not_is_not_abstract():
    assert not inspect.isabstract(gastm_Not)


def test_gastm_not_constructor_exists():
    assert callable(gastm_Not.__init__)


def test_gastm_not_constructor_args():
    sig = inspect.signature(gastm_Not.__init__)
    params = list(sig.parameters.keys())



def test_gastm_negate_is_not_abstract():
    assert not inspect.isabstract(gastm_Negate)


def test_gastm_negate_constructor_exists():
    assert callable(gastm_Negate.__init__)


def test_gastm_negate_constructor_args():
    sig = inspect.signature(gastm_Negate.__init__)
    params = list(sig.parameters.keys())



def test_gastm_addressof_is_not_abstract():
    assert not inspect.isabstract(gastm_AddressOf)


def test_gastm_addressof_constructor_exists():
    assert callable(gastm_AddressOf.__init__)


def test_gastm_addressof_constructor_args():
    sig = inspect.signature(gastm_AddressOf.__init__)
    params = list(sig.parameters.keys())



def test_gastm_increment_is_not_abstract():
    assert not inspect.isabstract(gastm_Increment)


def test_gastm_increment_constructor_exists():
    assert callable(gastm_Increment.__init__)


def test_gastm_increment_constructor_args():
    sig = inspect.signature(gastm_Increment.__init__)
    params = list(sig.parameters.keys())



def test_gastm_postincrement_is_not_abstract():
    assert not inspect.isabstract(gastm_PostIncrement)


def test_gastm_postincrement_constructor_exists():
    assert callable(gastm_PostIncrement.__init__)


def test_gastm_postincrement_constructor_args():
    sig = inspect.signature(gastm_PostIncrement.__init__)
    params = list(sig.parameters.keys())



def test_gastm_postdecrement_is_not_abstract():
    assert not inspect.isabstract(gastm_PostDecrement)


def test_gastm_postdecrement_constructor_exists():
    assert callable(gastm_PostDecrement.__init__)


def test_gastm_postdecrement_constructor_args():
    sig = inspect.signature(gastm_PostDecrement.__init__)
    params = list(sig.parameters.keys())



def test_gastm_unaryplus_is_not_abstract():
    assert not inspect.isabstract(gastm_UnaryPlus)


def test_gastm_unaryplus_constructor_exists():
    assert callable(gastm_UnaryPlus.__init__)


def test_gastm_unaryplus_constructor_args():
    sig = inspect.signature(gastm_UnaryPlus.__init__)
    params = list(sig.parameters.keys())



def test_literal_is_not_abstract():
    assert not inspect.isabstract(Literal)


def test_literal_constructor_exists():
    assert callable(Literal.__init__)


def test_literal_constructor_args():
    sig = inspect.signature(Literal.__init__)
    params = list(sig.parameters.keys())



def test_gastm_stringliteral_is_not_abstract():
    assert not inspect.isabstract(gastm_StringLiteral)


def test_gastm_stringliteral_constructor_exists():
    assert callable(gastm_StringLiteral.__init__)


def test_gastm_stringliteral_constructor_args():
    sig = inspect.signature(gastm_StringLiteral.__init__)
    params = list(sig.parameters.keys())



def test_gastm_bitliteral_is_not_abstract():
    assert not inspect.isabstract(gastm_BitLiteral)


def test_gastm_bitliteral_constructor_exists():
    assert callable(gastm_BitLiteral.__init__)


def test_gastm_bitliteral_constructor_args():
    sig = inspect.signature(gastm_BitLiteral.__init__)
    params = list(sig.parameters.keys())



def test_gastm_booleanliteral_is_not_abstract():
    assert not inspect.isabstract(gastm_BooleanLiteral)


def test_gastm_booleanliteral_constructor_exists():
    assert callable(gastm_BooleanLiteral.__init__)


def test_gastm_booleanliteral_constructor_args():
    sig = inspect.signature(gastm_BooleanLiteral.__init__)
    params = list(sig.parameters.keys())



def test_gastm_charliteral_is_not_abstract():
    assert not inspect.isabstract(gastm_CharLiteral)


def test_gastm_charliteral_constructor_exists():
    assert callable(gastm_CharLiteral.__init__)


def test_gastm_charliteral_constructor_args():
    sig = inspect.signature(gastm_CharLiteral.__init__)
    params = list(sig.parameters.keys())



def test_gastm_realliteral_is_not_abstract():
    assert not inspect.isabstract(gastm_RealLiteral)


def test_gastm_realliteral_constructor_exists():
    assert callable(gastm_RealLiteral.__init__)


def test_gastm_realliteral_constructor_args():
    sig = inspect.signature(gastm_RealLiteral.__init__)
    params = list(sig.parameters.keys())



def test_gastm_integerlliteral_is_not_abstract():
    assert not inspect.isabstract(gastm_IntegerlLiteral)


def test_gastm_integerlliteral_constructor_exists():
    assert callable(gastm_IntegerlLiteral.__init__)


def test_gastm_integerlliteral_constructor_args():
    sig = inspect.signature(gastm_IntegerlLiteral.__init__)
    params = list(sig.parameters.keys())



def test_qualifiedidentifierreference_is_not_abstract():
    assert not inspect.isabstract(QualifiedIdentifierReference)


def test_qualifiedidentifierreference_constructor_exists():
    assert callable(QualifiedIdentifierReference.__init__)


def test_qualifiedidentifierreference_constructor_args():
    sig = inspect.signature(QualifiedIdentifierReference.__init__)
    params = list(sig.parameters.keys())



def test_gastm_qualifiedoverdata_is_not_abstract():
    assert not inspect.isabstract(gastm_QualifiedOverData)


def test_gastm_qualifiedoverdata_constructor_exists():
    assert callable(gastm_QualifiedOverData.__init__)


def test_gastm_qualifiedoverdata_constructor_args():
    sig = inspect.signature(gastm_QualifiedOverData.__init__)
    params = list(sig.parameters.keys())



def test_gastm_qualifiedoverpointer_is_not_abstract():
    assert not inspect.isabstract(gastm_QualifiedOverPointer)


def test_gastm_qualifiedoverpointer_constructor_exists():
    assert callable(gastm_QualifiedOverPointer.__init__)


def test_gastm_qualifiedoverpointer_constructor_args():
    sig = inspect.signature(gastm_QualifiedOverPointer.__init__)
    params = list(sig.parameters.keys())



def test_forstatement_is_not_abstract():
    assert not inspect.isabstract(ForStatement)


def test_forstatement_constructor_exists():
    assert callable(ForStatement.__init__)


def test_forstatement_constructor_args():
    sig = inspect.signature(ForStatement.__init__)
    params = list(sig.parameters.keys())



def test_gastm_forcheckafterstatement_is_not_abstract():
    assert not inspect.isabstract(gastm_ForCheckAfterStatement)


def test_gastm_forcheckafterstatement_constructor_exists():
    assert callable(gastm_ForCheckAfterStatement.__init__)


def test_gastm_forcheckafterstatement_constructor_args():
    sig = inspect.signature(gastm_ForCheckAfterStatement.__init__)
    params = list(sig.parameters.keys())



def test_gastm_forcheckbeforestatement_is_not_abstract():
    assert not inspect.isabstract(gastm_ForCheckBeforeStatement)


def test_gastm_forcheckbeforestatement_constructor_exists():
    assert callable(gastm_ForCheckBeforeStatement.__init__)


def test_gastm_forcheckbeforestatement_constructor_args():
    sig = inspect.signature(gastm_ForCheckBeforeStatement.__init__)
    params = list(sig.parameters.keys())



def test_accesskind_is_not_abstract():
    assert not inspect.isabstract(AccessKind)


def test_accesskind_constructor_exists():
    assert callable(AccessKind.__init__)


def test_accesskind_constructor_args():
    sig = inspect.signature(AccessKind.__init__)
    params = list(sig.parameters.keys())



def test_gastm_private_is_not_abstract():
    assert not inspect.isabstract(gastm_Private)


def test_gastm_private_constructor_exists():
    assert callable(gastm_Private.__init__)


def test_gastm_private_constructor_args():
    sig = inspect.signature(gastm_Private.__init__)
    params = list(sig.parameters.keys())



def test_gastm_protected_is_not_abstract():
    assert not inspect.isabstract(gastm_Protected)


def test_gastm_protected_constructor_exists():
    assert callable(gastm_Protected.__init__)


def test_gastm_protected_constructor_args():
    sig = inspect.signature(gastm_Protected.__init__)
    params = list(sig.parameters.keys())



def test_gastm_public_is_not_abstract():
    assert not inspect.isabstract(gastm_Public)


def test_gastm_public_constructor_exists():
    assert callable(gastm_Public.__init__)


def test_gastm_public_constructor_args():
    sig = inspect.signature(gastm_Public.__init__)
    params = list(sig.parameters.keys())



def test_primitivetype_is_not_abstract():
    assert not inspect.isabstract(PrimitiveType)


def test_primitivetype_constructor_exists():
    assert callable(PrimitiveType.__init__)


def test_primitivetype_constructor_args():
    sig = inspect.signature(PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_gastm_widecharacter_is_not_abstract():
    assert not inspect.isabstract(gastm_WideCharacter)


def test_gastm_widecharacter_constructor_exists():
    assert callable(gastm_WideCharacter.__init__)


def test_gastm_widecharacter_constructor_args():
    sig = inspect.signature(gastm_WideCharacter.__init__)
    params = list(sig.parameters.keys())



def test_gastm_integer_is_not_abstract():
    assert not inspect.isabstract(gastm_Integer)


def test_gastm_integer_constructor_exists():
    assert callable(gastm_Integer.__init__)


def test_gastm_integer_constructor_args():
    sig = inspect.signature(gastm_Integer.__init__)
    params = list(sig.parameters.keys())



def test_gastm_boolean_is_not_abstract():
    assert not inspect.isabstract(gastm_Boolean)


def test_gastm_boolean_constructor_exists():
    assert callable(gastm_Boolean.__init__)


def test_gastm_boolean_constructor_args():
    sig = inspect.signature(gastm_Boolean.__init__)
    params = list(sig.parameters.keys())



def test_gastm_double_is_not_abstract():
    assert not inspect.isabstract(gastm_Double)


def test_gastm_double_constructor_exists():
    assert callable(gastm_Double.__init__)


def test_gastm_double_constructor_args():
    sig = inspect.signature(gastm_Double.__init__)
    params = list(sig.parameters.keys())



def test_gastm_float_is_not_abstract():
    assert not inspect.isabstract(gastm_Float)


def test_gastm_float_constructor_exists():
    assert callable(gastm_Float.__init__)


def test_gastm_float_constructor_args():
    sig = inspect.signature(gastm_Float.__init__)
    params = list(sig.parameters.keys())



def test_gastm_byte_is_not_abstract():
    assert not inspect.isabstract(gastm_Byte)


def test_gastm_byte_constructor_exists():
    assert callable(gastm_Byte.__init__)


def test_gastm_byte_constructor_args():
    sig = inspect.signature(gastm_Byte.__init__)
    params = list(sig.parameters.keys())



def test_gastm_longinteger_is_not_abstract():
    assert not inspect.isabstract(gastm_LongInteger)


def test_gastm_longinteger_constructor_exists():
    assert callable(gastm_LongInteger.__init__)


def test_gastm_longinteger_constructor_args():
    sig = inspect.signature(gastm_LongInteger.__init__)
    params = list(sig.parameters.keys())



def test_gastm_string_is_not_abstract():
    assert not inspect.isabstract(gastm_String)


def test_gastm_string_constructor_exists():
    assert callable(gastm_String.__init__)


def test_gastm_string_constructor_args():
    sig = inspect.signature(gastm_String.__init__)
    params = list(sig.parameters.keys())



def test_gastm_character_is_not_abstract():
    assert not inspect.isabstract(gastm_Character)


def test_gastm_character_constructor_exists():
    assert callable(gastm_Character.__init__)


def test_gastm_character_constructor_args():
    sig = inspect.signature(gastm_Character.__init__)
    params = list(sig.parameters.keys())



def test_gastm_longdouble_is_not_abstract():
    assert not inspect.isabstract(gastm_LongDouble)


def test_gastm_longdouble_constructor_exists():
    assert callable(gastm_LongDouble.__init__)


def test_gastm_longdouble_constructor_args():
    sig = inspect.signature(gastm_LongDouble.__init__)
    params = list(sig.parameters.keys())



def test_gastm_shortinteger_is_not_abstract():
    assert not inspect.isabstract(gastm_ShortInteger)


def test_gastm_shortinteger_constructor_exists():
    assert callable(gastm_ShortInteger.__init__)


def test_gastm_shortinteger_constructor_args():
    sig = inspect.signature(gastm_ShortInteger.__init__)
    params = list(sig.parameters.keys())



def test_gastm_void_is_not_abstract():
    assert not inspect.isabstract(gastm_Void)


def test_gastm_void_constructor_exists():
    assert callable(gastm_Void.__init__)


def test_gastm_void_constructor_args():
    sig = inspect.signature(gastm_Void.__init__)
    params = list(sig.parameters.keys())



def test_actualparameter_is_not_abstract():
    assert not inspect.isabstract(ActualParameter)


def test_actualparameter_constructor_exists():
    assert callable(ActualParameter.__init__)


def test_actualparameter_constructor_args():
    sig = inspect.signature(ActualParameter.__init__)
    params = list(sig.parameters.keys())



def test_gastm_missingactualparameter_is_not_abstract():
    assert not inspect.isabstract(gastm_MissingActualParameter)


def test_gastm_missingactualparameter_constructor_exists():
    assert callable(gastm_MissingActualParameter.__init__)


def test_gastm_missingactualparameter_constructor_args():
    sig = inspect.signature(gastm_MissingActualParameter.__init__)
    params = list(sig.parameters.keys())



def test_gastm_actualparameterexpression_is_not_abstract():
    assert not inspect.isabstract(gastm_ActualParameterExpression)


def test_gastm_actualparameterexpression_constructor_exists():
    assert callable(gastm_ActualParameterExpression.__init__)


def test_gastm_actualparameterexpression_constructor_args():
    sig = inspect.signature(gastm_ActualParameterExpression.__init__)
    params = list(sig.parameters.keys())



def test_binaryoperator_is_not_abstract():
    assert not inspect.isabstract(BinaryOperator)


def test_binaryoperator_constructor_exists():
    assert callable(BinaryOperator.__init__)


def test_binaryoperator_constructor_args():
    sig = inspect.signature(BinaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_gastm_assign_is_not_abstract():
    assert not inspect.isabstract(gastm_Assign)


def test_gastm_assign_constructor_exists():
    assert callable(gastm_Assign.__init__)


def test_gastm_assign_constructor_args():
    sig = inspect.signature(gastm_Assign.__init__)
    params = list(sig.parameters.keys())



def test_gastm_exponent_is_not_abstract():
    assert not inspect.isabstract(gastm_Exponent)


def test_gastm_exponent_constructor_exists():
    assert callable(gastm_Exponent.__init__)


def test_gastm_exponent_constructor_args():
    sig = inspect.signature(gastm_Exponent.__init__)
    params = list(sig.parameters.keys())



def test_gastm_bitleftshift_is_not_abstract():
    assert not inspect.isabstract(gastm_BitLeftShift)


def test_gastm_bitleftshift_constructor_exists():
    assert callable(gastm_BitLeftShift.__init__)


def test_gastm_bitleftshift_constructor_args():
    sig = inspect.signature(gastm_BitLeftShift.__init__)
    params = list(sig.parameters.keys())



def test_gastm_divide_is_not_abstract():
    assert not inspect.isabstract(gastm_Divide)


def test_gastm_divide_constructor_exists():
    assert callable(gastm_Divide.__init__)


def test_gastm_divide_constructor_args():
    sig = inspect.signature(gastm_Divide.__init__)
    params = list(sig.parameters.keys())



def test_gastm_notgreater_is_not_abstract():
    assert not inspect.isabstract(gastm_NotGreater)


def test_gastm_notgreater_constructor_exists():
    assert callable(gastm_NotGreater.__init__)


def test_gastm_notgreater_constructor_args():
    sig = inspect.signature(gastm_NotGreater.__init__)
    params = list(sig.parameters.keys())



def test_gastm_bitrightshift_is_not_abstract():
    assert not inspect.isabstract(gastm_BitRightShift)


def test_gastm_bitrightshift_constructor_exists():
    assert callable(gastm_BitRightShift.__init__)


def test_gastm_bitrightshift_constructor_args():
    sig = inspect.signature(gastm_BitRightShift.__init__)
    params = list(sig.parameters.keys())



def test_gastm_bitand_is_not_abstract():
    assert not inspect.isabstract(gastm_BitAnd)


def test_gastm_bitand_constructor_exists():
    assert callable(gastm_BitAnd.__init__)


def test_gastm_bitand_constructor_args():
    sig = inspect.signature(gastm_BitAnd.__init__)
    params = list(sig.parameters.keys())



def test_gastm_equal_is_not_abstract():
    assert not inspect.isabstract(gastm_Equal)


def test_gastm_equal_constructor_exists():
    assert callable(gastm_Equal.__init__)


def test_gastm_equal_constructor_args():
    sig = inspect.signature(gastm_Equal.__init__)
    params = list(sig.parameters.keys())



def test_gastm_notless_is_not_abstract():
    assert not inspect.isabstract(gastm_NotLess)


def test_gastm_notless_constructor_exists():
    assert callable(gastm_NotLess.__init__)


def test_gastm_notless_constructor_args():
    sig = inspect.signature(gastm_NotLess.__init__)
    params = list(sig.parameters.keys())



def test_gastm_less_is_not_abstract():
    assert not inspect.isabstract(gastm_Less)


def test_gastm_less_constructor_exists():
    assert callable(gastm_Less.__init__)


def test_gastm_less_constructor_args():
    sig = inspect.signature(gastm_Less.__init__)
    params = list(sig.parameters.keys())



def test_gastm_greater_is_not_abstract():
    assert not inspect.isabstract(gastm_Greater)


def test_gastm_greater_constructor_exists():
    assert callable(gastm_Greater.__init__)


def test_gastm_greater_constructor_args():
    sig = inspect.signature(gastm_Greater.__init__)
    params = list(sig.parameters.keys())



def test_gastm_bitor_is_not_abstract():
    assert not inspect.isabstract(gastm_BitOr)


def test_gastm_bitor_constructor_exists():
    assert callable(gastm_BitOr.__init__)


def test_gastm_bitor_constructor_args():
    sig = inspect.signature(gastm_BitOr.__init__)
    params = list(sig.parameters.keys())



def test_gastm_subtract_is_not_abstract():
    assert not inspect.isabstract(gastm_Subtract)


def test_gastm_subtract_constructor_exists():
    assert callable(gastm_Subtract.__init__)


def test_gastm_subtract_constructor_args():
    sig = inspect.signature(gastm_Subtract.__init__)
    params = list(sig.parameters.keys())



def test_gastm_or_is_not_abstract():
    assert not inspect.isabstract(gastm_Or)


def test_gastm_or_constructor_exists():
    assert callable(gastm_Or.__init__)


def test_gastm_or_constructor_args():
    sig = inspect.signature(gastm_Or.__init__)
    params = list(sig.parameters.keys())



def test_gastm_bitxor_is_not_abstract():
    assert not inspect.isabstract(gastm_BitXor)


def test_gastm_bitxor_constructor_exists():
    assert callable(gastm_BitXor.__init__)


def test_gastm_bitxor_constructor_args():
    sig = inspect.signature(gastm_BitXor.__init__)
    params = list(sig.parameters.keys())



def test_gastm_add_is_not_abstract():
    assert not inspect.isabstract(gastm_Add)


def test_gastm_add_constructor_exists():
    assert callable(gastm_Add.__init__)


def test_gastm_add_constructor_args():
    sig = inspect.signature(gastm_Add.__init__)
    params = list(sig.parameters.keys())



def test_gastm_multiply_is_not_abstract():
    assert not inspect.isabstract(gastm_Multiply)


def test_gastm_multiply_constructor_exists():
    assert callable(gastm_Multiply.__init__)


def test_gastm_multiply_constructor_args():
    sig = inspect.signature(gastm_Multiply.__init__)
    params = list(sig.parameters.keys())



def test_gastm_notequal_is_not_abstract():
    assert not inspect.isabstract(gastm_NotEqual)


def test_gastm_notequal_constructor_exists():
    assert callable(gastm_NotEqual.__init__)


def test_gastm_notequal_constructor_args():
    sig = inspect.signature(gastm_NotEqual.__init__)
    params = list(sig.parameters.keys())



def test_gastm_modulus_is_not_abstract():
    assert not inspect.isabstract(gastm_Modulus)


def test_gastm_modulus_constructor_exists():
    assert callable(gastm_Modulus.__init__)


def test_gastm_modulus_constructor_args():
    sig = inspect.signature(gastm_Modulus.__init__)
    params = list(sig.parameters.keys())



def test_gastm_and_is_not_abstract():
    assert not inspect.isabstract(gastm_And)


def test_gastm_and_constructor_exists():
    assert callable(gastm_And.__init__)


def test_gastm_and_constructor_args():
    sig = inspect.signature(gastm_And.__init__)
    params = list(sig.parameters.keys())



def test_gastm_operatorassign_is_not_abstract():
    assert not inspect.isabstract(gastm_OperatorAssign)


def test_gastm_operatorassign_constructor_exists():
    assert callable(gastm_OperatorAssign.__init__)


def test_gastm_operatorassign_constructor_args():
    sig = inspect.signature(gastm_OperatorAssign.__init__)
    params = list(sig.parameters.keys())



def test_identifierreference_is_not_abstract():
    assert not inspect.isabstract(IdentifierReference)


def test_identifierreference_constructor_exists():
    assert callable(IdentifierReference.__init__)


def test_identifierreference_constructor_args():
    sig = inspect.signature(IdentifierReference.__init__)
    params = list(sig.parameters.keys())



def test_namereference_is_not_abstract():
    assert not inspect.isabstract(NameReference)


def test_namereference_constructor_exists():
    assert callable(NameReference.__init__)


def test_namereference_constructor_args():
    sig = inspect.signature(NameReference.__init__)
    params = list(sig.parameters.keys())



def test_gastm_typequalifiedidentifierreference_is_not_abstract():
    assert not inspect.isabstract(gastm_TypeQualifiedIdentifierReference)


def test_gastm_typequalifiedidentifierreference_constructor_exists():
    assert callable(gastm_TypeQualifiedIdentifierReference.__init__)


def test_gastm_typequalifiedidentifierreference_constructor_args():
    sig = inspect.signature(gastm_TypeQualifiedIdentifierReference.__init__)
    params = list(sig.parameters.keys())



def test_gastm_qualifiedidentifierreference_is_not_abstract():
    assert not inspect.isabstract(gastm_QualifiedIdentifierReference)


def test_gastm_qualifiedidentifierreference_constructor_exists():
    assert callable(gastm_QualifiedIdentifierReference.__init__)


def test_gastm_qualifiedidentifierreference_constructor_args():
    sig = inspect.signature(gastm_QualifiedIdentifierReference.__init__)
    params = list(sig.parameters.keys())



def test_loopstatement_is_not_abstract():
    assert not inspect.isabstract(LoopStatement)


def test_loopstatement_constructor_exists():
    assert callable(LoopStatement.__init__)


def test_loopstatement_constructor_args():
    sig = inspect.signature(LoopStatement.__init__)
    params = list(sig.parameters.keys())



def test_gastm_dowhilestatement_is_not_abstract():
    assert not inspect.isabstract(gastm_DoWhileStatement)


def test_gastm_dowhilestatement_constructor_exists():
    assert callable(gastm_DoWhileStatement.__init__)


def test_gastm_dowhilestatement_constructor_args():
    sig = inspect.signature(gastm_DoWhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_gastm_whilestatement_is_not_abstract():
    assert not inspect.isabstract(gastm_WhileStatement)


def test_gastm_whilestatement_constructor_exists():
    assert callable(gastm_WhileStatement.__init__)


def test_gastm_whilestatement_constructor_args():
    sig = inspect.signature(gastm_WhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_gastm_forstatement_is_not_abstract():
    assert not inspect.isabstract(gastm_ForStatement)


def test_gastm_forstatement_constructor_exists():
    assert callable(gastm_ForStatement.__init__)


def test_gastm_forstatement_constructor_args():
    sig = inspect.signature(gastm_ForStatement.__init__)
    params = list(sig.parameters.keys())



def test_catchblock_is_not_abstract():
    assert not inspect.isabstract(CatchBlock)


def test_catchblock_constructor_exists():
    assert callable(CatchBlock.__init__)


def test_catchblock_constructor_args():
    sig = inspect.signature(CatchBlock.__init__)
    params = list(sig.parameters.keys())



def test_gastm_typescatchblock_is_not_abstract():
    assert not inspect.isabstract(gastm_TypesCatchBlock)


def test_gastm_typescatchblock_constructor_exists():
    assert callable(gastm_TypesCatchBlock.__init__)


def test_gastm_typescatchblock_constructor_args():
    sig = inspect.signature(gastm_TypesCatchBlock.__init__)
    params = list(sig.parameters.keys())



def test_gastm_variablecatchblock_is_not_abstract():
    assert not inspect.isabstract(gastm_VariableCatchBlock)


def test_gastm_variablecatchblock_constructor_exists():
    assert callable(gastm_VariableCatchBlock.__init__)


def test_gastm_variablecatchblock_constructor_args():
    sig = inspect.signature(gastm_VariableCatchBlock.__init__)
    params = list(sig.parameters.keys())



def test_blockscope_is_not_abstract():
    assert not inspect.isabstract(BlockScope)


def test_blockscope_constructor_exists():
    assert callable(BlockScope.__init__)


def test_blockscope_constructor_args():
    sig = inspect.signature(BlockScope.__init__)
    params = list(sig.parameters.keys())



def test_switchcase_is_not_abstract():
    assert not inspect.isabstract(SwitchCase)


def test_switchcase_constructor_exists():
    assert callable(SwitchCase.__init__)


def test_switchcase_constructor_args():
    sig = inspect.signature(SwitchCase.__init__)
    params = list(sig.parameters.keys())



def test_gastm_caseblock_is_not_abstract():
    assert not inspect.isabstract(gastm_CaseBlock)


def test_gastm_caseblock_constructor_exists():
    assert callable(gastm_CaseBlock.__init__)


def test_gastm_caseblock_constructor_args():
    sig = inspect.signature(gastm_CaseBlock.__init__)
    params = list(sig.parameters.keys())



def test_gastm_defaultblock_is_not_abstract():
    assert not inspect.isabstract(gastm_DefaultBlock)


def test_gastm_defaultblock_constructor_exists():
    assert callable(gastm_DefaultBlock.__init__)


def test_gastm_defaultblock_constructor_args():
    sig = inspect.signature(gastm_DefaultBlock.__init__)
    params = list(sig.parameters.keys())



def test_labeldefinition_is_not_abstract():
    assert not inspect.isabstract(LabelDefinition)


def test_labeldefinition_constructor_exists():
    assert callable(LabelDefinition.__init__)


def test_labeldefinition_constructor_args():
    sig = inspect.signature(LabelDefinition.__init__)
    params = list(sig.parameters.keys())



def test_labelaccess_is_not_abstract():
    assert not inspect.isabstract(LabelAccess)


def test_labelaccess_constructor_exists():
    assert callable(LabelAccess.__init__)


def test_labelaccess_constructor_args():
    sig = inspect.signature(LabelAccess.__init__)
    params = list(sig.parameters.keys())



def test_derivesfrom_is_not_abstract():
    assert not inspect.isabstract(DerivesFrom)


def test_derivesfrom_constructor_exists():
    assert callable(DerivesFrom.__init__)


def test_derivesfrom_constructor_args():
    sig = inspect.signature(DerivesFrom.__init__)
    params = list(sig.parameters.keys())



def test_enumliteraldefinition_is_not_abstract():
    assert not inspect.isabstract(EnumLiteralDefinition)


def test_enumliteraldefinition_constructor_exists():
    assert callable(EnumLiteralDefinition.__init__)


def test_enumliteraldefinition_constructor_args():
    sig = inspect.signature(EnumLiteralDefinition.__init__)
    params = list(sig.parameters.keys())



def test_formalparametertype_is_not_abstract():
    assert not inspect.isabstract(FormalParameterType)


def test_formalparametertype_constructor_exists():
    assert callable(FormalParameterType.__init__)


def test_formalparametertype_constructor_args():
    sig = inspect.signature(FormalParameterType.__init__)
    params = list(sig.parameters.keys())



def test_gastm_byvalueformalparametertype_is_not_abstract():
    assert not inspect.isabstract(gastm_ByValueFormalParameterType)


def test_gastm_byvalueformalparametertype_constructor_exists():
    assert callable(gastm_ByValueFormalParameterType.__init__)


def test_gastm_byvalueformalparametertype_constructor_args():
    sig = inspect.signature(gastm_ByValueFormalParameterType.__init__)
    params = list(sig.parameters.keys())



def test_gastm_byreferenceformalparametertype_is_not_abstract():
    assert not inspect.isabstract(gastm_ByReferenceFormalParameterType)


def test_gastm_byreferenceformalparametertype_constructor_exists():
    assert callable(gastm_ByReferenceFormalParameterType.__init__)


def test_gastm_byreferenceformalparametertype_constructor_args():
    sig = inspect.signature(gastm_ByReferenceFormalParameterType.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_gastm_functiontype_is_not_abstract():
    assert not inspect.isabstract(gastm_FunctionType)


def test_gastm_functiontype_constructor_exists():
    assert callable(gastm_FunctionType.__init__)


def test_gastm_functiontype_constructor_args():
    sig = inspect.signature(gastm_FunctionType.__init__)
    params = list(sig.parameters.keys())



def test_dimension_is_not_abstract():
    assert not inspect.isabstract(Dimension)


def test_dimension_constructor_exists():
    assert callable(Dimension.__init__)


def test_dimension_constructor_args():
    sig = inspect.signature(Dimension.__init__)
    params = list(sig.parameters.keys())



def test_constructedtype_is_not_abstract():
    assert not inspect.isabstract(ConstructedType)


def test_constructedtype_constructor_exists():
    assert callable(ConstructedType.__init__)


def test_constructedtype_constructor_args():
    sig = inspect.signature(ConstructedType.__init__)
    params = list(sig.parameters.keys())



def test_gastm_referencetype_is_not_abstract():
    assert not inspect.isabstract(gastm_ReferenceType)


def test_gastm_referencetype_constructor_exists():
    assert callable(gastm_ReferenceType.__init__)


def test_gastm_referencetype_constructor_args():
    sig = inspect.signature(gastm_ReferenceType.__init__)
    params = list(sig.parameters.keys())



def test_gastm_rangetype_is_not_abstract():
    assert not inspect.isabstract(gastm_RangeType)


def test_gastm_rangetype_constructor_exists():
    assert callable(gastm_RangeType.__init__)


def test_gastm_rangetype_constructor_args():
    sig = inspect.signature(gastm_RangeType.__init__)
    params = list(sig.parameters.keys())



def test_gastm_collectiontype_is_not_abstract():
    assert not inspect.isabstract(gastm_CollectionType)


def test_gastm_collectiontype_constructor_exists():
    assert callable(gastm_CollectionType.__init__)


def test_gastm_collectiontype_constructor_args():
    sig = inspect.signature(gastm_CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_gastm_pointertype_is_not_abstract():
    assert not inspect.isabstract(gastm_PointerType)


def test_gastm_pointertype_constructor_exists():
    assert callable(gastm_PointerType.__init__)


def test_gastm_pointertype_constructor_args():
    sig = inspect.signature(gastm_PointerType.__init__)
    params = list(sig.parameters.keys())



def test_gastm_arraytype_is_not_abstract():
    assert not inspect.isabstract(gastm_ArrayType)


def test_gastm_arraytype_constructor_exists():
    assert callable(gastm_ArrayType.__init__)


def test_gastm_arraytype_constructor_args():
    sig = inspect.signature(gastm_ArrayType.__init__)
    params = list(sig.parameters.keys())



def test_aggregatescope_is_not_abstract():
    assert not inspect.isabstract(AggregateScope)


def test_aggregatescope_constructor_exists():
    assert callable(AggregateScope.__init__)


def test_aggregatescope_constructor_args():
    sig = inspect.signature(AggregateScope.__init__)
    params = list(sig.parameters.keys())



def test_datatype_is_not_abstract():
    assert not inspect.isabstract(DataType)


def test_datatype_constructor_exists():
    assert callable(DataType.__init__)


def test_datatype_constructor_args():
    sig = inspect.signature(DataType.__init__)
    params = list(sig.parameters.keys())



def test_gastm_exceptiontype_is_not_abstract():
    assert not inspect.isabstract(gastm_ExceptionType)


def test_gastm_exceptiontype_constructor_exists():
    assert callable(gastm_ExceptionType.__init__)


def test_gastm_exceptiontype_constructor_args():
    sig = inspect.signature(gastm_ExceptionType.__init__)
    params = list(sig.parameters.keys())



def test_gastm_constructedtype_is_not_abstract():
    assert not inspect.isabstract(gastm_ConstructedType)


def test_gastm_constructedtype_constructor_exists():
    assert callable(gastm_ConstructedType.__init__)


def test_gastm_constructedtype_constructor_args():
    sig = inspect.signature(gastm_ConstructedType.__init__)
    params = list(sig.parameters.keys())



def test_gastm_enumtype_is_not_abstract():
    assert not inspect.isabstract(gastm_EnumType)


def test_gastm_enumtype_constructor_exists():
    assert callable(gastm_EnumType.__init__)


def test_gastm_enumtype_constructor_args():
    sig = inspect.signature(gastm_EnumType.__init__)
    params = list(sig.parameters.keys())



def test_gastm_aggregatetype_is_not_abstract():
    assert not inspect.isabstract(gastm_AggregateType)


def test_gastm_aggregatetype_constructor_exists():
    assert callable(gastm_AggregateType.__init__)


def test_gastm_aggregatetype_constructor_args():
    sig = inspect.signature(gastm_AggregateType.__init__)
    params = list(sig.parameters.keys())



def test_gastm_namedtype_is_not_abstract():
    assert not inspect.isabstract(gastm_NamedType)


def test_gastm_namedtype_constructor_exists():
    assert callable(gastm_NamedType.__init__)


def test_gastm_namedtype_constructor_args():
    sig = inspect.signature(gastm_NamedType.__init__)
    params = list(sig.parameters.keys())



def test_gastm_formalparametertype_is_not_abstract():
    assert not inspect.isabstract(gastm_FormalParameterType)


def test_gastm_formalparametertype_constructor_exists():
    assert callable(gastm_FormalParameterType.__init__)


def test_gastm_formalparametertype_constructor_args():
    sig = inspect.signature(gastm_FormalParameterType.__init__)
    params = list(sig.parameters.keys())



def test_gastm_primitivetype_is_not_abstract():
    assert not inspect.isabstract(gastm_PrimitiveType)


def test_gastm_primitivetype_constructor_exists():
    assert callable(gastm_PrimitiveType.__init__)


def test_gastm_primitivetype_constructor_args():
    sig = inspect.signature(gastm_PrimitiveType.__init__)
    params = list(sig.parameters.keys())
    assert "isSigned" in params, "Missing parameter 'isSigned'"

def test_gastm_primitivetype_has_isSigned():
    assert hasattr(gastm_PrimitiveType, "isSigned")
    descriptor = None
    for klass in gastm_PrimitiveType.__mro__:
        if "isSigned" in klass.__dict__:
            descriptor = klass.__dict__["isSigned"]
            break
    assert isinstance(descriptor, property)



def test_gastmsyntaxobject_is_not_abstract():
    assert not inspect.isabstract(GASTMSyntaxObject)


def test_gastmsyntaxobject_constructor_exists():
    assert callable(GASTMSyntaxObject.__init__)


def test_gastmsyntaxobject_constructor_args():
    sig = inspect.signature(GASTMSyntaxObject.__init__)
    params = list(sig.parameters.keys())



def test_gastm_definitionobject_is_not_abstract():
    assert not inspect.isabstract(gastm_DefinitionObject)


def test_gastm_definitionobject_constructor_exists():
    assert callable(gastm_DefinitionObject.__init__)


def test_gastm_definitionobject_constructor_args():
    sig = inspect.signature(gastm_DefinitionObject.__init__)
    params = list(sig.parameters.keys())



def test_gastm_expression_is_not_abstract():
    assert not inspect.isabstract(gastm_Expression)


def test_gastm_expression_constructor_exists():
    assert callable(gastm_Expression.__init__)


def test_gastm_expression_constructor_args():
    sig = inspect.signature(gastm_Expression.__init__)
    params = list(sig.parameters.keys())



def test_gastm_preprocessorelement_is_not_abstract():
    assert not inspect.isabstract(gastm_PreprocessorElement)


def test_gastm_preprocessorelement_constructor_exists():
    assert callable(gastm_PreprocessorElement.__init__)


def test_gastm_preprocessorelement_constructor_args():
    sig = inspect.signature(gastm_PreprocessorElement.__init__)
    params = list(sig.parameters.keys())



def test_gastm_type_is_not_abstract():
    assert not inspect.isabstract(gastm_Type)


def test_gastm_type_constructor_exists():
    assert callable(gastm_Type.__init__)


def test_gastm_type_constructor_args():
    sig = inspect.signature(gastm_Type.__init__)
    params = list(sig.parameters.keys())
    assert "isConst" in params, "Missing parameter 'isConst'"
    assert "isVolatile" in params, "Missing parameter 'isVolatile'"

def test_gastm_type_has_isConst():
    assert hasattr(gastm_Type, "isConst")
    descriptor = None
    for klass in gastm_Type.__mro__:
        if "isConst" in klass.__dict__:
            descriptor = klass.__dict__["isConst"]
            break
    assert isinstance(descriptor, property)

def test_gastm_type_has_isVolatile():
    assert hasattr(gastm_Type, "isVolatile")
    descriptor = None
    for klass in gastm_Type.__mro__:
        if "isVolatile" in klass.__dict__:
            descriptor = klass.__dict__["isVolatile"]
            break
    assert isinstance(descriptor, property)



def test_macrodefinition_is_not_abstract():
    assert not inspect.isabstract(MacroDefinition)


def test_macrodefinition_constructor_exists():
    assert callable(MacroDefinition.__init__)


def test_macrodefinition_constructor_args():
    sig = inspect.signature(MacroDefinition.__init__)
    params = list(sig.parameters.keys())



def test_labeltype_is_not_abstract():
    assert not inspect.isabstract(LabelType)


def test_labeltype_constructor_exists():
    assert callable(LabelType.__init__)


def test_labeltype_constructor_args():
    sig = inspect.signature(LabelType.__init__)
    params = list(sig.parameters.keys())



def test_namespacetype_is_not_abstract():
    assert not inspect.isabstract(NameSpaceType)


def test_namespacetype_constructor_exists():
    assert callable(NameSpaceType.__init__)


def test_namespacetype_constructor_args():
    sig = inspect.signature(NameSpaceType.__init__)
    params = list(sig.parameters.keys())



def test_aggregatetype_is_not_abstract():
    assert not inspect.isabstract(AggregateType)


def test_aggregatetype_constructor_exists():
    assert callable(AggregateType.__init__)


def test_aggregatetype_constructor_args():
    sig = inspect.signature(AggregateType.__init__)
    params = list(sig.parameters.keys())



def test_gastm_annotationtype_is_not_abstract():
    assert not inspect.isabstract(gastm_AnnotationType)


def test_gastm_annotationtype_constructor_exists():
    assert callable(gastm_AnnotationType.__init__)


def test_gastm_annotationtype_constructor_args():
    sig = inspect.signature(gastm_AnnotationType.__init__)
    params = list(sig.parameters.keys())



def test_gastm_structuretype_is_not_abstract():
    assert not inspect.isabstract(gastm_StructureType)


def test_gastm_structuretype_constructor_exists():
    assert callable(gastm_StructureType.__init__)


def test_gastm_structuretype_constructor_args():
    sig = inspect.signature(gastm_StructureType.__init__)
    params = list(sig.parameters.keys())



def test_gastm_uniontype_is_not_abstract():
    assert not inspect.isabstract(gastm_UnionType)


def test_gastm_uniontype_constructor_exists():
    assert callable(gastm_UnionType.__init__)


def test_gastm_uniontype_constructor_args():
    sig = inspect.signature(gastm_UnionType.__init__)
    params = list(sig.parameters.keys())



def test_gastm_classtype_is_not_abstract():
    assert not inspect.isabstract(gastm_ClassType)


def test_gastm_classtype_constructor_exists():
    assert callable(gastm_ClassType.__init__)


def test_gastm_classtype_constructor_args():
    sig = inspect.signature(gastm_ClassType.__init__)
    params = list(sig.parameters.keys())



def test_namedtype_is_not_abstract():
    assert not inspect.isabstract(NamedType)


def test_namedtype_constructor_exists():
    assert callable(NamedType.__init__)


def test_namedtype_constructor_args():
    sig = inspect.signature(NamedType.__init__)
    params = list(sig.parameters.keys())



def test_typedefinition_is_not_abstract():
    assert not inspect.isabstract(TypeDefinition)


def test_typedefinition_constructor_exists():
    assert callable(TypeDefinition.__init__)


def test_typedefinition_constructor_args():
    sig = inspect.signature(TypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_gastm_aggregatetypedefinition_is_not_abstract():
    assert not inspect.isabstract(gastm_AggregateTypeDefinition)


def test_gastm_aggregatetypedefinition_constructor_exists():
    assert callable(gastm_AggregateTypeDefinition.__init__)


def test_gastm_aggregatetypedefinition_constructor_args():
    sig = inspect.signature(gastm_AggregateTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_gastm_namedtypedefinition_is_not_abstract():
    assert not inspect.isabstract(gastm_NamedTypeDefinition)


def test_gastm_namedtypedefinition_constructor_exists():
    assert callable(gastm_NamedTypeDefinition.__init__)


def test_gastm_namedtypedefinition_constructor_args():
    sig = inspect.signature(gastm_NamedTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_definition_is_not_abstract():
    assert not inspect.isabstract(Definition)


def test_definition_constructor_exists():
    assert callable(Definition.__init__)


def test_definition_constructor_args():
    sig = inspect.signature(Definition.__init__)
    params = list(sig.parameters.keys())



def test_gastm_enumliteraldefinition_is_not_abstract():
    assert not inspect.isabstract(gastm_EnumLiteralDefinition)


def test_gastm_enumliteraldefinition_constructor_exists():
    assert callable(gastm_EnumLiteralDefinition.__init__)


def test_gastm_enumliteraldefinition_constructor_args():
    sig = inspect.signature(gastm_EnumLiteralDefinition.__init__)
    params = list(sig.parameters.keys())



def test_datadefinition_is_not_abstract():
    assert not inspect.isabstract(DataDefinition)


def test_datadefinition_constructor_exists():
    assert callable(DataDefinition.__init__)


def test_datadefinition_constructor_args():
    sig = inspect.signature(DataDefinition.__init__)
    params = list(sig.parameters.keys())



def test_gastm_bitfielddefinition_is_not_abstract():
    assert not inspect.isabstract(gastm_BitFieldDefinition)


def test_gastm_bitfielddefinition_constructor_exists():
    assert callable(gastm_BitFieldDefinition.__init__)


def test_gastm_bitfielddefinition_constructor_args():
    sig = inspect.signature(gastm_BitFieldDefinition.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_gastm_binaryexpression_is_not_abstract():
    assert not inspect.isabstract(gastm_BinaryExpression)


def test_gastm_binaryexpression_constructor_exists():
    assert callable(gastm_BinaryExpression.__init__)


def test_gastm_binaryexpression_constructor_args():
    sig = inspect.signature(gastm_BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_gastm_arrayaccess_is_not_abstract():
    assert not inspect.isabstract(gastm_ArrayAccess)


def test_gastm_arrayaccess_constructor_exists():
    assert callable(gastm_ArrayAccess.__init__)


def test_gastm_arrayaccess_constructor_args():
    sig = inspect.signature(gastm_ArrayAccess.__init__)
    params = list(sig.parameters.keys())



def test_gastm_literal_is_not_abstract():
    assert not inspect.isabstract(gastm_Literal)


def test_gastm_literal_constructor_exists():
    assert callable(gastm_Literal.__init__)


def test_gastm_literal_constructor_args():
    sig = inspect.signature(gastm_Literal.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_gastm_literal_has_value():
    assert hasattr(gastm_Literal, "value")
    descriptor = None
    for klass in gastm_Literal.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_gastm_aggregateexpression_is_not_abstract():
    assert not inspect.isabstract(gastm_AggregateExpression)


def test_gastm_aggregateexpression_constructor_exists():
    assert callable(gastm_AggregateExpression.__init__)


def test_gastm_aggregateexpression_constructor_args():
    sig = inspect.signature(gastm_AggregateExpression.__init__)
    params = list(sig.parameters.keys())



def test_gastm_newexpression_is_not_abstract():
    assert not inspect.isabstract(gastm_NewExpression)


def test_gastm_newexpression_constructor_exists():
    assert callable(gastm_NewExpression.__init__)


def test_gastm_newexpression_constructor_args():
    sig = inspect.signature(gastm_NewExpression.__init__)
    params = list(sig.parameters.keys())



def test_gastm_conditionalexpression_is_not_abstract():
    assert not inspect.isabstract(gastm_ConditionalExpression)


def test_gastm_conditionalexpression_constructor_exists():
    assert callable(gastm_ConditionalExpression.__init__)


def test_gastm_conditionalexpression_constructor_args():
    sig = inspect.signature(gastm_ConditionalExpression.__init__)
    params = list(sig.parameters.keys())



def test_gastm_castexpression_is_not_abstract():
    assert not inspect.isabstract(gastm_CastExpression)


def test_gastm_castexpression_constructor_exists():
    assert callable(gastm_CastExpression.__init__)


def test_gastm_castexpression_constructor_args():
    sig = inspect.signature(gastm_CastExpression.__init__)
    params = list(sig.parameters.keys())



def test_gastm_unaryexpression_is_not_abstract():
    assert not inspect.isabstract(gastm_UnaryExpression)


def test_gastm_unaryexpression_constructor_exists():
    assert callable(gastm_UnaryExpression.__init__)


def test_gastm_unaryexpression_constructor_args():
    sig = inspect.signature(gastm_UnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_gastm_rangeexpression_is_not_abstract():
    assert not inspect.isabstract(gastm_RangeExpression)


def test_gastm_rangeexpression_constructor_exists():
    assert callable(gastm_RangeExpression.__init__)


def test_gastm_rangeexpression_constructor_args():
    sig = inspect.signature(gastm_RangeExpression.__init__)
    params = list(sig.parameters.keys())



def test_gastm_namereference_is_not_abstract():
    assert not inspect.isabstract(gastm_NameReference)


def test_gastm_namereference_constructor_exists():
    assert callable(gastm_NameReference.__init__)


def test_gastm_namereference_constructor_args():
    sig = inspect.signature(gastm_NameReference.__init__)
    params = list(sig.parameters.keys())



def test_gastm_datadefinition_is_not_abstract():
    assert not inspect.isabstract(gastm_DataDefinition)


def test_gastm_datadefinition_constructor_exists():
    assert callable(gastm_DataDefinition.__init__)


def test_gastm_datadefinition_constructor_args():
    sig = inspect.signature(gastm_DataDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "isMutable" in params, "Missing parameter 'isMutable'"

def test_gastm_datadefinition_has_isMutable():
    assert hasattr(gastm_DataDefinition, "isMutable")
    descriptor = None
    for klass in gastm_DataDefinition.__mro__:
        if "isMutable" in klass.__dict__:
            descriptor = klass.__dict__["isMutable"]
            break
    assert isinstance(descriptor, property)



def test_gastm_entrydefinition_is_not_abstract():
    assert not inspect.isabstract(gastm_EntryDefinition)


def test_gastm_entrydefinition_constructor_exists():
    assert callable(gastm_EntryDefinition.__init__)


def test_gastm_entrydefinition_constructor_args():
    sig = inspect.signature(gastm_EntryDefinition.__init__)
    params = list(sig.parameters.keys())



def test_virtualspecification_is_not_abstract():
    assert not inspect.isabstract(VirtualSpecification)


def test_virtualspecification_constructor_exists():
    assert callable(VirtualSpecification.__init__)


def test_virtualspecification_constructor_args():
    sig = inspect.signature(VirtualSpecification.__init__)
    params = list(sig.parameters.keys())



def test_gastm_purevirtual_is_not_abstract():
    assert not inspect.isabstract(gastm_PureVirtual)


def test_gastm_purevirtual_constructor_exists():
    assert callable(gastm_PureVirtual.__init__)


def test_gastm_purevirtual_constructor_args():
    sig = inspect.signature(gastm_PureVirtual.__init__)
    params = list(sig.parameters.keys())



def test_gastm_nonvirtual_is_not_abstract():
    assert not inspect.isabstract(gastm_NonVirtual)


def test_gastm_nonvirtual_constructor_exists():
    assert callable(gastm_NonVirtual.__init__)


def test_gastm_nonvirtual_constructor_args():
    sig = inspect.signature(gastm_NonVirtual.__init__)
    params = list(sig.parameters.keys())



def test_gastm_virtual_is_not_abstract():
    assert not inspect.isabstract(gastm_Virtual)


def test_gastm_virtual_constructor_exists():
    assert callable(gastm_Virtual.__init__)


def test_gastm_virtual_constructor_args():
    sig = inspect.signature(gastm_Virtual.__init__)
    params = list(sig.parameters.keys())



def test_gastm_functionmemberattributes_is_not_abstract():
    assert not inspect.isabstract(gastm_FunctionMemberAttributes)


def test_gastm_functionmemberattributes_constructor_exists():
    assert callable(gastm_FunctionMemberAttributes.__init__)


def test_gastm_functionmemberattributes_constructor_args():
    sig = inspect.signature(gastm_FunctionMemberAttributes.__init__)
    params = list(sig.parameters.keys())
    assert "isFriend" in params, "Missing parameter 'isFriend'"
    assert "isThisConst" in params, "Missing parameter 'isThisConst'"
    assert "isInline" in params, "Missing parameter 'isInline'"

def test_gastm_functionmemberattributes_has_isFriend():
    assert hasattr(gastm_FunctionMemberAttributes, "isFriend")
    descriptor = None
    for klass in gastm_FunctionMemberAttributes.__mro__:
        if "isFriend" in klass.__dict__:
            descriptor = klass.__dict__["isFriend"]
            break
    assert isinstance(descriptor, property)

def test_gastm_functionmemberattributes_has_isThisConst():
    assert hasattr(gastm_FunctionMemberAttributes, "isThisConst")
    descriptor = None
    for klass in gastm_FunctionMemberAttributes.__mro__:
        if "isThisConst" in klass.__dict__:
            descriptor = klass.__dict__["isThisConst"]
            break
    assert isinstance(descriptor, property)

def test_gastm_functionmemberattributes_has_isInline():
    assert hasattr(gastm_FunctionMemberAttributes, "isInline")
    descriptor = None
    for klass in gastm_FunctionMemberAttributes.__mro__:
        if "isInline" in klass.__dict__:
            descriptor = klass.__dict__["isInline"]
            break
    assert isinstance(descriptor, property)



def test_functionscope_is_not_abstract():
    assert not inspect.isabstract(FunctionScope)


def test_functionscope_constructor_exists():
    assert callable(FunctionScope.__init__)


def test_functionscope_constructor_args():
    sig = inspect.signature(FunctionScope.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_gastm_emptystatement_is_not_abstract():
    assert not inspect.isabstract(gastm_EmptyStatement)


def test_gastm_emptystatement_constructor_exists():
    assert callable(gastm_EmptyStatement.__init__)


def test_gastm_emptystatement_constructor_args():
    sig = inspect.signature(gastm_EmptyStatement.__init__)
    params = list(sig.parameters.keys())



def test_gastm_throwstatement_is_not_abstract():
    assert not inspect.isabstract(gastm_ThrowStatement)


def test_gastm_throwstatement_constructor_exists():
    assert callable(gastm_ThrowStatement.__init__)


def test_gastm_throwstatement_constructor_args():
    sig = inspect.signature(gastm_ThrowStatement.__init__)
    params = list(sig.parameters.keys())



def test_gastm_expressionstatement_is_not_abstract():
    assert not inspect.isabstract(gastm_ExpressionStatement)


def test_gastm_expressionstatement_constructor_exists():
    assert callable(gastm_ExpressionStatement.__init__)


def test_gastm_expressionstatement_constructor_args():
    sig = inspect.signature(gastm_ExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_gastm_ifstatement_is_not_abstract():
    assert not inspect.isabstract(gastm_IfStatement)


def test_gastm_ifstatement_constructor_exists():
    assert callable(gastm_IfStatement.__init__)


def test_gastm_ifstatement_constructor_args():
    sig = inspect.signature(gastm_IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_gastm_loopstatement_is_not_abstract():
    assert not inspect.isabstract(gastm_LoopStatement)


def test_gastm_loopstatement_constructor_exists():
    assert callable(gastm_LoopStatement.__init__)


def test_gastm_loopstatement_constructor_args():
    sig = inspect.signature(gastm_LoopStatement.__init__)
    params = list(sig.parameters.keys())



def test_gastm_labeledstatement_is_not_abstract():
    assert not inspect.isabstract(gastm_LabeledStatement)


def test_gastm_labeledstatement_constructor_exists():
    assert callable(gastm_LabeledStatement.__init__)


def test_gastm_labeledstatement_constructor_args():
    sig = inspect.signature(gastm_LabeledStatement.__init__)
    params = list(sig.parameters.keys())



def test_gastm_jumpstatement_is_not_abstract():
    assert not inspect.isabstract(gastm_JumpStatement)


def test_gastm_jumpstatement_constructor_exists():
    assert callable(gastm_JumpStatement.__init__)


def test_gastm_jumpstatement_constructor_args():
    sig = inspect.signature(gastm_JumpStatement.__init__)
    params = list(sig.parameters.keys())



def test_gastm_terminatestatement_is_not_abstract():
    assert not inspect.isabstract(gastm_TerminateStatement)


def test_gastm_terminatestatement_constructor_exists():
    assert callable(gastm_TerminateStatement.__init__)


def test_gastm_terminatestatement_constructor_args():
    sig = inspect.signature(gastm_TerminateStatement.__init__)
    params = list(sig.parameters.keys())



def test_gastm_trystatement_is_not_abstract():
    assert not inspect.isabstract(gastm_TryStatement)


def test_gastm_trystatement_constructor_exists():
    assert callable(gastm_TryStatement.__init__)


def test_gastm_trystatement_constructor_args():
    sig = inspect.signature(gastm_TryStatement.__init__)
    params = list(sig.parameters.keys())



def test_gastm_returnstatement_is_not_abstract():
    assert not inspect.isabstract(gastm_ReturnStatement)


def test_gastm_returnstatement_constructor_exists():
    assert callable(gastm_ReturnStatement.__init__)


def test_gastm_returnstatement_constructor_args():
    sig = inspect.signature(gastm_ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_gastm_declarationordefinitionstatement_is_not_abstract():
    assert not inspect.isabstract(gastm_DeclarationOrDefinitionStatement)


def test_gastm_declarationordefinitionstatement_constructor_exists():
    assert callable(gastm_DeclarationOrDefinitionStatement.__init__)


def test_gastm_declarationordefinitionstatement_constructor_args():
    sig = inspect.signature(gastm_DeclarationOrDefinitionStatement.__init__)
    params = list(sig.parameters.keys())



def test_gastm_breakstatement_is_not_abstract():
    assert not inspect.isabstract(gastm_BreakStatement)


def test_gastm_breakstatement_constructor_exists():
    assert callable(gastm_BreakStatement.__init__)


def test_gastm_breakstatement_constructor_args():
    sig = inspect.signature(gastm_BreakStatement.__init__)
    params = list(sig.parameters.keys())



def test_gastm_blockstatement_is_not_abstract():
    assert not inspect.isabstract(gastm_BlockStatement)


def test_gastm_blockstatement_constructor_exists():
    assert callable(gastm_BlockStatement.__init__)


def test_gastm_blockstatement_constructor_args():
    sig = inspect.signature(gastm_BlockStatement.__init__)
    params = list(sig.parameters.keys())



def test_gastm_continuestatement_is_not_abstract():
    assert not inspect.isabstract(gastm_ContinueStatement)


def test_gastm_continuestatement_constructor_exists():
    assert callable(gastm_ContinueStatement.__init__)


def test_gastm_continuestatement_constructor_args():
    sig = inspect.signature(gastm_ContinueStatement.__init__)
    params = list(sig.parameters.keys())



def test_gastm_switchstatement_is_not_abstract():
    assert not inspect.isabstract(gastm_SwitchStatement)


def test_gastm_switchstatement_constructor_exists():
    assert callable(gastm_SwitchStatement.__init__)


def test_gastm_switchstatement_constructor_args():
    sig = inspect.signature(gastm_SwitchStatement.__init__)
    params = list(sig.parameters.keys())



def test_gastm_deletestatement_is_not_abstract():
    assert not inspect.isabstract(gastm_DeleteStatement)


def test_gastm_deletestatement_constructor_exists():
    assert callable(gastm_DeleteStatement.__init__)


def test_gastm_deletestatement_constructor_args():
    sig = inspect.signature(gastm_DeleteStatement.__init__)
    params = list(sig.parameters.keys())



def test_formalparameterdefinition_is_not_abstract():
    assert not inspect.isabstract(FormalParameterDefinition)


def test_formalparameterdefinition_constructor_exists():
    assert callable(FormalParameterDefinition.__init__)


def test_formalparameterdefinition_constructor_args():
    sig = inspect.signature(FormalParameterDefinition.__init__)
    params = list(sig.parameters.keys())



def test_gastm_functiondefinition_is_not_abstract():
    assert not inspect.isabstract(gastm_FunctionDefinition)


def test_gastm_functiondefinition_constructor_exists():
    assert callable(gastm_FunctionDefinition.__init__)


def test_gastm_functiondefinition_constructor_args():
    sig = inspect.signature(gastm_FunctionDefinition.__init__)
    params = list(sig.parameters.keys())



def test_functionmemberattributes_is_not_abstract():
    assert not inspect.isabstract(FunctionMemberAttributes)


def test_functionmemberattributes_constructor_exists():
    assert callable(FunctionMemberAttributes.__init__)


def test_functionmemberattributes_constructor_args():
    sig = inspect.signature(FunctionMemberAttributes.__init__)
    params = list(sig.parameters.keys())



def test_formalparameterdeclaration_is_not_abstract():
    assert not inspect.isabstract(FormalParameterDeclaration)


def test_formalparameterdeclaration_constructor_exists():
    assert callable(FormalParameterDeclaration.__init__)


def test_formalparameterdeclaration_constructor_args():
    sig = inspect.signature(FormalParameterDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_declaration_is_not_abstract():
    assert not inspect.isabstract(Declaration)


def test_declaration_constructor_exists():
    assert callable(Declaration.__init__)


def test_declaration_constructor_args():
    sig = inspect.signature(Declaration.__init__)
    params = list(sig.parameters.keys())



def test_gastm_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(gastm_VariableDeclaration)


def test_gastm_variabledeclaration_constructor_exists():
    assert callable(gastm_VariableDeclaration.__init__)


def test_gastm_variabledeclaration_constructor_args():
    sig = inspect.signature(gastm_VariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "isMutable" in params, "Missing parameter 'isMutable'"

def test_gastm_variabledeclaration_has_isMutable():
    assert hasattr(gastm_VariableDeclaration, "isMutable")
    descriptor = None
    for klass in gastm_VariableDeclaration.__mro__:
        if "isMutable" in klass.__dict__:
            descriptor = klass.__dict__["isMutable"]
            break
    assert isinstance(descriptor, property)



def test_gastm_functiondeclaration_is_not_abstract():
    assert not inspect.isabstract(gastm_FunctionDeclaration)


def test_gastm_functiondeclaration_constructor_exists():
    assert callable(gastm_FunctionDeclaration.__init__)


def test_gastm_functiondeclaration_constructor_args():
    sig = inspect.signature(gastm_FunctionDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_sourcefile_is_not_abstract():
    assert not inspect.isabstract(SourceFile)


def test_sourcefile_constructor_exists():
    assert callable(SourceFile.__init__)


def test_sourcefile_constructor_args():
    sig = inspect.signature(SourceFile.__init__)
    params = list(sig.parameters.keys())



def test_typereference_is_not_abstract():
    assert not inspect.isabstract(TypeReference)


def test_typereference_constructor_exists():
    assert callable(TypeReference.__init__)


def test_typereference_constructor_args():
    sig = inspect.signature(TypeReference.__init__)
    params = list(sig.parameters.keys())



def test_gastm_namedtypereference_is_not_abstract():
    assert not inspect.isabstract(gastm_NamedTypeReference)


def test_gastm_namedtypereference_constructor_exists():
    assert callable(gastm_NamedTypeReference.__init__)


def test_gastm_namedtypereference_constructor_args():
    sig = inspect.signature(gastm_NamedTypeReference.__init__)
    params = list(sig.parameters.keys())



def test_gastm_unnamedtypereference_is_not_abstract():
    assert not inspect.isabstract(gastm_UnnamedTypeReference)


def test_gastm_unnamedtypereference_constructor_exists():
    assert callable(gastm_UnnamedTypeReference.__init__)


def test_gastm_unnamedtypereference_constructor_args():
    sig = inspect.signature(gastm_UnnamedTypeReference.__init__)
    params = list(sig.parameters.keys())



def test_name_is_not_abstract():
    assert not inspect.isabstract(Name)


def test_name_constructor_exists():
    assert callable(Name.__init__)


def test_name_constructor_args():
    sig = inspect.signature(Name.__init__)
    params = list(sig.parameters.keys())



def test_declarationordefinition_is_not_abstract():
    assert not inspect.isabstract(DeclarationOrDefinition)


def test_declarationordefinition_constructor_exists():
    assert callable(DeclarationOrDefinition.__init__)


def test_declarationordefinition_constructor_args():
    sig = inspect.signature(DeclarationOrDefinition.__init__)
    params = list(sig.parameters.keys())



def test_gastm_declaration_is_not_abstract():
    assert not inspect.isabstract(gastm_Declaration)


def test_gastm_declaration_constructor_exists():
    assert callable(gastm_Declaration.__init__)


def test_gastm_declaration_constructor_args():
    sig = inspect.signature(gastm_Declaration.__init__)
    params = list(sig.parameters.keys())



def test_gastm_definition_is_not_abstract():
    assert not inspect.isabstract(gastm_Definition)


def test_gastm_definition_constructor_exists():
    assert callable(gastm_Definition.__init__)


def test_gastm_definition_constructor_args():
    sig = inspect.signature(gastm_Definition.__init__)
    params = list(sig.parameters.keys())



def test_programscope_is_not_abstract():
    assert not inspect.isabstract(ProgramScope)


def test_programscope_constructor_exists():
    assert callable(ProgramScope.__init__)


def test_programscope_constructor_args():
    sig = inspect.signature(ProgramScope.__init__)
    params = list(sig.parameters.keys())



def test_othersyntaxobject_is_not_abstract():
    assert not inspect.isabstract(OtherSyntaxObject)


def test_othersyntaxobject_constructor_exists():
    assert callable(OtherSyntaxObject.__init__)


def test_othersyntaxobject_constructor_args():
    sig = inspect.signature(OtherSyntaxObject.__init__)
    params = list(sig.parameters.keys())



def test_gastm_switchcase_is_not_abstract():
    assert not inspect.isabstract(gastm_SwitchCase)


def test_gastm_switchcase_constructor_exists():
    assert callable(gastm_SwitchCase.__init__)


def test_gastm_switchcase_constructor_args():
    sig = inspect.signature(gastm_SwitchCase.__init__)
    params = list(sig.parameters.keys())



def test_gastm_dimension_is_not_abstract():
    assert not inspect.isabstract(gastm_Dimension)


def test_gastm_dimension_constructor_exists():
    assert callable(gastm_Dimension.__init__)


def test_gastm_dimension_constructor_args():
    sig = inspect.signature(gastm_Dimension.__init__)
    params = list(sig.parameters.keys())



def test_gastm_name_is_not_abstract():
    assert not inspect.isabstract(gastm_Name)


def test_gastm_name_constructor_exists():
    assert callable(gastm_Name.__init__)


def test_gastm_name_constructor_args():
    sig = inspect.signature(gastm_Name.__init__)
    params = list(sig.parameters.keys())
    assert "nameString" in params, "Missing parameter 'nameString'"

def test_gastm_name_has_nameString():
    assert hasattr(gastm_Name, "nameString")
    descriptor = None
    for klass in gastm_Name.__mro__:
        if "nameString" in klass.__dict__:
            descriptor = klass.__dict__["nameString"]
            break
    assert isinstance(descriptor, property)



def test_gastm_catchblock_is_not_abstract():
    assert not inspect.isabstract(gastm_CatchBlock)


def test_gastm_catchblock_constructor_exists():
    assert callable(gastm_CatchBlock.__init__)


def test_gastm_catchblock_constructor_args():
    sig = inspect.signature(gastm_CatchBlock.__init__)
    params = list(sig.parameters.keys())



def test_gastm_derivesfrom_is_not_abstract():
    assert not inspect.isabstract(gastm_DerivesFrom)


def test_gastm_derivesfrom_constructor_exists():
    assert callable(gastm_DerivesFrom.__init__)


def test_gastm_derivesfrom_constructor_args():
    sig = inspect.signature(gastm_DerivesFrom.__init__)
    params = list(sig.parameters.keys())
    assert "isVirtual" in params, "Missing parameter 'isVirtual'"

def test_gastm_derivesfrom_has_isVirtual():
    assert hasattr(gastm_DerivesFrom, "isVirtual")
    descriptor = None
    for klass in gastm_DerivesFrom.__mro__:
        if "isVirtual" in klass.__dict__:
            descriptor = klass.__dict__["isVirtual"]
            break
    assert isinstance(descriptor, property)



def test_gastm_compilationunit_is_not_abstract():
    assert not inspect.isabstract(gastm_CompilationUnit)


def test_gastm_compilationunit_constructor_exists():
    assert callable(gastm_CompilationUnit.__init__)


def test_gastm_compilationunit_constructor_args():
    sig = inspect.signature(gastm_CompilationUnit.__init__)
    params = list(sig.parameters.keys())
    assert "language" in params, "Missing parameter 'language'"

def test_gastm_compilationunit_has_language():
    assert hasattr(gastm_CompilationUnit, "language")
    descriptor = None
    for klass in gastm_CompilationUnit.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)



def test_annotationexpression_is_not_abstract():
    assert not inspect.isabstract(AnnotationExpression)


def test_annotationexpression_constructor_exists():
    assert callable(AnnotationExpression.__init__)


def test_annotationexpression_constructor_args():
    sig = inspect.signature(AnnotationExpression.__init__)
    params = list(sig.parameters.keys())



def test_preprocessorelement_is_not_abstract():
    assert not inspect.isabstract(PreprocessorElement)


def test_preprocessorelement_constructor_exists():
    assert callable(PreprocessorElement.__init__)


def test_preprocessorelement_constructor_args():
    sig = inspect.signature(PreprocessorElement.__init__)
    params = list(sig.parameters.keys())



def test_gastm_macrocall_is_not_abstract():
    assert not inspect.isabstract(gastm_MacroCall)


def test_gastm_macrocall_constructor_exists():
    assert callable(gastm_MacroCall.__init__)


def test_gastm_macrocall_constructor_args():
    sig = inspect.signature(gastm_MacroCall.__init__)
    params = list(sig.parameters.keys())



def test_gastm_macrodefinition_is_not_abstract():
    assert not inspect.isabstract(gastm_MacroDefinition)


def test_gastm_macrodefinition_constructor_exists():
    assert callable(gastm_MacroDefinition.__init__)


def test_gastm_macrodefinition_constructor_args():
    sig = inspect.signature(gastm_MacroDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "macroName" in params, "Missing parameter 'macroName'"
    assert "body" in params, "Missing parameter 'body'"

def test_gastm_macrodefinition_has_macroName():
    assert hasattr(gastm_MacroDefinition, "macroName")
    descriptor = None
    for klass in gastm_MacroDefinition.__mro__:
        if "macroName" in klass.__dict__:
            descriptor = klass.__dict__["macroName"]
            break
    assert isinstance(descriptor, property)

def test_gastm_macrodefinition_has_body():
    assert hasattr(gastm_MacroDefinition, "body")
    descriptor = None
    for klass in gastm_MacroDefinition.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)



def test_gastm_comment_is_not_abstract():
    assert not inspect.isabstract(gastm_Comment)


def test_gastm_comment_constructor_exists():
    assert callable(gastm_Comment.__init__)


def test_gastm_comment_constructor_args():
    sig = inspect.signature(gastm_Comment.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_gastm_comment_has_text():
    assert hasattr(gastm_Comment, "text")
    descriptor = None
    for klass in gastm_Comment.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_gastm_includeunit_is_not_abstract():
    assert not inspect.isabstract(gastm_IncludeUnit)


def test_gastm_includeunit_constructor_exists():
    assert callable(gastm_IncludeUnit.__init__)


def test_gastm_includeunit_constructor_args():
    sig = inspect.signature(gastm_IncludeUnit.__init__)
    params = list(sig.parameters.keys())



def test_sourcelocation_is_not_abstract():
    assert not inspect.isabstract(SourceLocation)


def test_sourcelocation_constructor_exists():
    assert callable(SourceLocation.__init__)


def test_sourcelocation_constructor_args():
    sig = inspect.signature(SourceLocation.__init__)
    params = list(sig.parameters.keys())



def test_gastmobject_is_not_abstract():
    assert not inspect.isabstract(GASTMObject)


def test_gastmobject_constructor_exists():
    assert callable(GASTMObject.__init__)


def test_gastmobject_constructor_args():
    sig = inspect.signature(GASTMObject.__init__)
    params = list(sig.parameters.keys())



def test_gastm_gastmsyntaxobject_is_not_abstract():
    assert not inspect.isabstract(gastm_GASTMSyntaxObject)


def test_gastm_gastmsyntaxobject_constructor_exists():
    assert callable(gastm_GASTMSyntaxObject.__init__)


def test_gastm_gastmsyntaxobject_constructor_args():
    sig = inspect.signature(gastm_GASTMSyntaxObject.__init__)
    params = list(sig.parameters.keys())



def test_scope_is_not_abstract():
    assert not inspect.isabstract(Scope)


def test_scope_constructor_exists():
    assert callable(Scope.__init__)


def test_scope_constructor_args():
    sig = inspect.signature(Scope.__init__)
    params = list(sig.parameters.keys())



def test_gastm_globalscope_is_not_abstract():
    assert not inspect.isabstract(gastm_GlobalScope)


def test_gastm_globalscope_constructor_exists():
    assert callable(gastm_GlobalScope.__init__)


def test_gastm_globalscope_constructor_args():
    sig = inspect.signature(gastm_GlobalScope.__init__)
    params = list(sig.parameters.keys())



def test_definitionobject_is_not_abstract():
    assert not inspect.isabstract(DefinitionObject)


def test_definitionobject_constructor_exists():
    assert callable(DefinitionObject.__init__)


def test_definitionobject_constructor_args():
    sig = inspect.signature(DefinitionObject.__init__)
    params = list(sig.parameters.keys())



def test_gastm_namespacedefinition_is_not_abstract():
    assert not inspect.isabstract(gastm_NameSpaceDefinition)


def test_gastm_namespacedefinition_constructor_exists():
    assert callable(gastm_NameSpaceDefinition.__init__)


def test_gastm_namespacedefinition_constructor_args():
    sig = inspect.signature(gastm_NameSpaceDefinition.__init__)
    params = list(sig.parameters.keys())



def test_gastm_labeldefinition_is_not_abstract():
    assert not inspect.isabstract(gastm_LabelDefinition)


def test_gastm_labeldefinition_constructor_exists():
    assert callable(gastm_LabelDefinition.__init__)


def test_gastm_labeldefinition_constructor_args():
    sig = inspect.signature(gastm_LabelDefinition.__init__)
    params = list(sig.parameters.keys())



def test_gastm_declarationordefinition_is_not_abstract():
    assert not inspect.isabstract(gastm_DeclarationOrDefinition)


def test_gastm_declarationordefinition_constructor_exists():
    assert callable(gastm_DeclarationOrDefinition.__init__)


def test_gastm_declarationordefinition_constructor_args():
    sig = inspect.signature(gastm_DeclarationOrDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "isRegister" in params, "Missing parameter 'isRegister'"
    assert "linkageSpecifier" in params, "Missing parameter 'linkageSpecifier'"

def test_gastm_declarationordefinition_has_isRegister():
    assert hasattr(gastm_DeclarationOrDefinition, "isRegister")
    descriptor = None
    for klass in gastm_DeclarationOrDefinition.__mro__:
        if "isRegister" in klass.__dict__:
            descriptor = klass.__dict__["isRegister"]
            break
    assert isinstance(descriptor, property)

def test_gastm_declarationordefinition_has_linkageSpecifier():
    assert hasattr(gastm_DeclarationOrDefinition, "linkageSpecifier")
    descriptor = None
    for klass in gastm_DeclarationOrDefinition.__mro__:
        if "linkageSpecifier" in klass.__dict__:
            descriptor = klass.__dict__["linkageSpecifier"]
            break
    assert isinstance(descriptor, property)



def test_gastm_typedefinition_is_not_abstract():
    assert not inspect.isabstract(gastm_TypeDefinition)


def test_gastm_typedefinition_constructor_exists():
    assert callable(gastm_TypeDefinition.__init__)


def test_gastm_typedefinition_constructor_args():
    sig = inspect.signature(gastm_TypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_globalscope_is_not_abstract():
    assert not inspect.isabstract(GlobalScope)


def test_globalscope_constructor_exists():
    assert callable(GlobalScope.__init__)


def test_globalscope_constructor_args():
    sig = inspect.signature(GlobalScope.__init__)
    params = list(sig.parameters.keys())



def test_compilationunit_is_not_abstract():
    assert not inspect.isabstract(CompilationUnit)


def test_compilationunit_constructor_exists():
    assert callable(CompilationUnit.__init__)


def test_compilationunit_constructor_args():
    sig = inspect.signature(CompilationUnit.__init__)
    params = list(sig.parameters.keys())



def test_gastmsemanticobject_is_not_abstract():
    assert not inspect.isabstract(GASTMSemanticObject)


def test_gastmsemanticobject_constructor_exists():
    assert callable(GASTMSemanticObject.__init__)


def test_gastmsemanticobject_constructor_args():
    sig = inspect.signature(GASTMSemanticObject.__init__)
    params = list(sig.parameters.keys())



def test_gastm_scope_is_not_abstract():
    assert not inspect.isabstract(gastm_Scope)


def test_gastm_scope_constructor_exists():
    assert callable(gastm_Scope.__init__)


def test_gastm_scope_constructor_args():
    sig = inspect.signature(gastm_Scope.__init__)
    params = list(sig.parameters.keys())



def test_gastm_project_is_not_abstract():
    assert not inspect.isabstract(gastm_Project)


def test_gastm_project_constructor_exists():
    assert callable(gastm_Project.__init__)


def test_gastm_project_constructor_args():
    sig = inspect.signature(gastm_Project.__init__)
    params = list(sig.parameters.keys())



def test_gastmsourceobject_is_not_abstract():
    assert not inspect.isabstract(GASTMSourceObject)


def test_gastmsourceobject_constructor_exists():
    assert callable(GASTMSourceObject.__init__)


def test_gastmsourceobject_constructor_args():
    sig = inspect.signature(GASTMSourceObject.__init__)
    params = list(sig.parameters.keys())



def test_gastm_sourcelocation_is_not_abstract():
    assert not inspect.isabstract(gastm_SourceLocation)


def test_gastm_sourcelocation_constructor_exists():
    assert callable(gastm_SourceLocation.__init__)


def test_gastm_sourcelocation_constructor_args():
    sig = inspect.signature(gastm_SourceLocation.__init__)
    params = list(sig.parameters.keys())
    assert "endColumn" in params, "Missing parameter 'endColumn'"
    assert "startLine" in params, "Missing parameter 'startLine'"
    assert "startColumn" in params, "Missing parameter 'startColumn'"
    assert "endLine" in params, "Missing parameter 'endLine'"

def test_gastm_sourcelocation_has_endColumn():
    assert hasattr(gastm_SourceLocation, "endColumn")
    descriptor = None
    for klass in gastm_SourceLocation.__mro__:
        if "endColumn" in klass.__dict__:
            descriptor = klass.__dict__["endColumn"]
            break
    assert isinstance(descriptor, property)

def test_gastm_sourcelocation_has_startLine():
    assert hasattr(gastm_SourceLocation, "startLine")
    descriptor = None
    for klass in gastm_SourceLocation.__mro__:
        if "startLine" in klass.__dict__:
            descriptor = klass.__dict__["startLine"]
            break
    assert isinstance(descriptor, property)

def test_gastm_sourcelocation_has_startColumn():
    assert hasattr(gastm_SourceLocation, "startColumn")
    descriptor = None
    for klass in gastm_SourceLocation.__mro__:
        if "startColumn" in klass.__dict__:
            descriptor = klass.__dict__["startColumn"]
            break
    assert isinstance(descriptor, property)

def test_gastm_sourcelocation_has_endLine():
    assert hasattr(gastm_SourceLocation, "endLine")
    descriptor = None
    for klass in gastm_SourceLocation.__mro__:
        if "endLine" in klass.__dict__:
            descriptor = klass.__dict__["endLine"]
            break
    assert isinstance(descriptor, property)



def test_gastm_sourcefile_is_not_abstract():
    assert not inspect.isabstract(gastm_SourceFile)


def test_gastm_sourcefile_constructor_exists():
    assert callable(gastm_SourceFile.__init__)


def test_gastm_sourcefile_constructor_args():
    sig = inspect.signature(gastm_SourceFile.__init__)
    params = list(sig.parameters.keys())
    assert "pathName" in params, "Missing parameter 'pathName'"

def test_gastm_sourcefile_has_pathName():
    assert hasattr(gastm_SourceFile, "pathName")
    descriptor = None
    for klass in gastm_SourceFile.__mro__:
        if "pathName" in klass.__dict__:
            descriptor = klass.__dict__["pathName"]
            break
    assert isinstance(descriptor, property)



def test_gastm_actualparameter_is_not_abstract():
    assert not inspect.isabstract(gastm_ActualParameter)


def test_gastm_actualparameter_constructor_exists():
    assert callable(gastm_ActualParameter.__init__)


def test_gastm_actualparameter_constructor_args():
    sig = inspect.signature(gastm_ActualParameter.__init__)
    params = list(sig.parameters.keys())



def test_gastm_binaryoperator_is_not_abstract():
    assert not inspect.isabstract(gastm_BinaryOperator)


def test_gastm_binaryoperator_constructor_exists():
    assert callable(gastm_BinaryOperator.__init__)


def test_gastm_binaryoperator_constructor_args():
    sig = inspect.signature(gastm_BinaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_gastm_unaryoperator_is_not_abstract():
    assert not inspect.isabstract(gastm_UnaryOperator)


def test_gastm_unaryoperator_constructor_exists():
    assert callable(gastm_UnaryOperator.__init__)


def test_gastm_unaryoperator_constructor_args():
    sig = inspect.signature(gastm_UnaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_gastm_accesskind_is_not_abstract():
    assert not inspect.isabstract(gastm_AccessKind)


def test_gastm_accesskind_constructor_exists():
    assert callable(gastm_AccessKind.__init__)


def test_gastm_accesskind_constructor_args():
    sig = inspect.signature(gastm_AccessKind.__init__)
    params = list(sig.parameters.keys())



def test_gastm_datatype_is_not_abstract():
    assert not inspect.isabstract(gastm_DataType)


def test_gastm_datatype_constructor_exists():
    assert callable(gastm_DataType.__init__)


def test_gastm_datatype_constructor_args():
    sig = inspect.signature(gastm_DataType.__init__)
    params = list(sig.parameters.keys())



def test_gastm_storagespecification_is_not_abstract():
    assert not inspect.isabstract(gastm_StorageSpecification)


def test_gastm_storagespecification_constructor_exists():
    assert callable(gastm_StorageSpecification.__init__)


def test_gastm_storagespecification_constructor_args():
    sig = inspect.signature(gastm_StorageSpecification.__init__)
    params = list(sig.parameters.keys())



def test_gastm_othersyntaxobject_is_not_abstract():
    assert not inspect.isabstract(gastm_OtherSyntaxObject)


def test_gastm_othersyntaxobject_constructor_exists():
    assert callable(gastm_OtherSyntaxObject.__init__)


def test_gastm_othersyntaxobject_constructor_args():
    sig = inspect.signature(gastm_OtherSyntaxObject.__init__)
    params = list(sig.parameters.keys())



def test_gastm_gastmsemanticobject_is_not_abstract():
    assert not inspect.isabstract(gastm_GASTMSemanticObject)


def test_gastm_gastmsemanticobject_constructor_exists():
    assert callable(gastm_GASTMSemanticObject.__init__)


def test_gastm_gastmsemanticobject_constructor_args():
    sig = inspect.signature(gastm_GASTMSemanticObject.__init__)
    params = list(sig.parameters.keys())



def test_gastm_gastmsourceobject_is_not_abstract():
    assert not inspect.isabstract(gastm_GASTMSourceObject)


def test_gastm_gastmsourceobject_constructor_exists():
    assert callable(gastm_GASTMSourceObject.__init__)


def test_gastm_gastmsourceobject_constructor_args():
    sig = inspect.signature(gastm_GASTMSourceObject.__init__)
    params = list(sig.parameters.keys())



def test_gastm_gastmobject_is_not_abstract():
    assert not inspect.isabstract(gastm_GASTMObject)


def test_gastm_gastmobject_constructor_exists():
    assert callable(gastm_GASTMObject.__init__)


def test_gastm_gastmobject_constructor_args():
    sig = inspect.signature(gastm_GASTMObject.__init__)
    params = list(sig.parameters.keys())



def test_storagespecification_is_not_abstract():
    assert not inspect.isabstract(StorageSpecification)


def test_storagespecification_constructor_exists():
    assert callable(StorageSpecification.__init__)


def test_storagespecification_constructor_args():
    sig = inspect.signature(StorageSpecification.__init__)
    params = list(sig.parameters.keys())



def test_gastm_functionpersistent_is_not_abstract():
    assert not inspect.isabstract(gastm_FunctionPersistent)


def test_gastm_functionpersistent_constructor_exists():
    assert callable(gastm_FunctionPersistent.__init__)


def test_gastm_functionpersistent_constructor_args():
    sig = inspect.signature(gastm_FunctionPersistent.__init__)
    params = list(sig.parameters.keys())



def test_gastm_filelocal_is_not_abstract():
    assert not inspect.isabstract(gastm_FileLocal)


def test_gastm_filelocal_constructor_exists():
    assert callable(gastm_FileLocal.__init__)


def test_gastm_filelocal_constructor_args():
    sig = inspect.signature(gastm_FileLocal.__init__)
    params = list(sig.parameters.keys())



def test_gastm_nodef_is_not_abstract():
    assert not inspect.isabstract(gastm_NoDef)


def test_gastm_nodef_constructor_exists():
    assert callable(gastm_NoDef.__init__)


def test_gastm_nodef_constructor_args():
    sig = inspect.signature(gastm_NoDef.__init__)
    params = list(sig.parameters.keys())



def test_gastm_perclassmember_is_not_abstract():
    assert not inspect.isabstract(gastm_PerClassMember)


def test_gastm_perclassmember_constructor_exists():
    assert callable(gastm_PerClassMember.__init__)


def test_gastm_perclassmember_constructor_args():
    sig = inspect.signature(gastm_PerClassMember.__init__)
    params = list(sig.parameters.keys())



def test_gastm_external_is_not_abstract():
    assert not inspect.isabstract(gastm_External)


def test_gastm_external_constructor_exists():
    assert callable(gastm_External.__init__)


def test_gastm_external_constructor_args():
    sig = inspect.signature(gastm_External.__init__)
    params = list(sig.parameters.keys())



def test_gastm_functionmemberattribute_is_not_abstract():
    assert not inspect.isabstract(gastm_FunctionMemberAttribute)


def test_gastm_functionmemberattribute_constructor_exists():
    assert callable(gastm_FunctionMemberAttribute.__init__)


def test_gastm_functionmemberattribute_constructor_args():
    sig = inspect.signature(gastm_FunctionMemberAttribute.__init__)
    params = list(sig.parameters.keys())



def test_gastm_variabledefinition_is_not_abstract():
    assert not inspect.isabstract(gastm_VariableDefinition)


def test_gastm_variabledefinition_constructor_exists():
    assert callable(gastm_VariableDefinition.__init__)


def test_gastm_variabledefinition_constructor_args():
    sig = inspect.signature(gastm_VariableDefinition.__init__)
    params = list(sig.parameters.keys())



def test_gastm_formalparameterdeclaration_is_not_abstract():
    assert not inspect.isabstract(gastm_FormalParameterDeclaration)


def test_gastm_formalparameterdeclaration_constructor_exists():
    assert callable(gastm_FormalParameterDeclaration.__init__)


def test_gastm_formalparameterdeclaration_constructor_args():
    sig = inspect.signature(gastm_FormalParameterDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_gastm_virtualspecification_is_not_abstract():
    assert not inspect.isabstract(gastm_VirtualSpecification)


def test_gastm_virtualspecification_constructor_exists():
    assert callable(gastm_VirtualSpecification.__init__)


def test_gastm_virtualspecification_constructor_args():
    sig = inspect.signature(gastm_VirtualSpecification.__init__)
    params = list(sig.parameters.keys())



def test_gastm_formalparameterdefinition_is_not_abstract():
    assert not inspect.isabstract(gastm_FormalParameterDefinition)


def test_gastm_formalparameterdefinition_constructor_exists():
    assert callable(gastm_FormalParameterDefinition.__init__)


def test_gastm_formalparameterdefinition_constructor_args():
    sig = inspect.signature(gastm_FormalParameterDefinition.__init__)
    params = list(sig.parameters.keys())



def test_gastm_identifierreference_is_not_abstract():
    assert not inspect.isabstract(gastm_IdentifierReference)


def test_gastm_identifierreference_constructor_exists():
    assert callable(gastm_IdentifierReference.__init__)


def test_gastm_identifierreference_constructor_args():
    sig = inspect.signature(gastm_IdentifierReference.__init__)
    params = list(sig.parameters.keys())



def test_gastm_blockscope_is_not_abstract():
    assert not inspect.isabstract(gastm_BlockScope)


def test_gastm_blockscope_constructor_exists():
    assert callable(gastm_BlockScope.__init__)


def test_gastm_blockscope_constructor_args():
    sig = inspect.signature(gastm_BlockScope.__init__)
    params = list(sig.parameters.keys())



def test_gastm_aggregatescope_is_not_abstract():
    assert not inspect.isabstract(gastm_AggregateScope)


def test_gastm_aggregatescope_constructor_exists():
    assert callable(gastm_AggregateScope.__init__)


def test_gastm_aggregatescope_constructor_args():
    sig = inspect.signature(gastm_AggregateScope.__init__)
    params = list(sig.parameters.keys())



def test_gastm_labeltype_is_not_abstract():
    assert not inspect.isabstract(gastm_LabelType)


def test_gastm_labeltype_constructor_exists():
    assert callable(gastm_LabelType.__init__)


def test_gastm_labeltype_constructor_args():
    sig = inspect.signature(gastm_LabelType.__init__)
    params = list(sig.parameters.keys())



def test_gastm_namespacetype_is_not_abstract():
    assert not inspect.isabstract(gastm_NameSpaceType)


def test_gastm_namespacetype_constructor_exists():
    assert callable(gastm_NameSpaceType.__init__)


def test_gastm_namespacetype_constructor_args():
    sig = inspect.signature(gastm_NameSpaceType.__init__)
    params = list(sig.parameters.keys())



def test_gastm_functionscope_is_not_abstract():
    assert not inspect.isabstract(gastm_FunctionScope)


def test_gastm_functionscope_constructor_exists():
    assert callable(gastm_FunctionScope.__init__)


def test_gastm_functionscope_constructor_args():
    sig = inspect.signature(gastm_FunctionScope.__init__)
    params = list(sig.parameters.keys())



def test_gastm_statement_is_not_abstract():
    assert not inspect.isabstract(gastm_Statement)


def test_gastm_statement_constructor_exists():
    assert callable(gastm_Statement.__init__)


def test_gastm_statement_constructor_args():
    sig = inspect.signature(gastm_Statement.__init__)
    params = list(sig.parameters.keys())



def test_gastm_typereference_is_not_abstract():
    assert not inspect.isabstract(gastm_TypeReference)


def test_gastm_typereference_constructor_exists():
    assert callable(gastm_TypeReference.__init__)


def test_gastm_typereference_constructor_args():
    sig = inspect.signature(gastm_TypeReference.__init__)
    params = list(sig.parameters.keys())



def test_gastm_programscope_is_not_abstract():
    assert not inspect.isabstract(gastm_ProgramScope)


def test_gastm_programscope_constructor_exists():
    assert callable(gastm_ProgramScope.__init__)


def test_gastm_programscope_constructor_args():
    sig = inspect.signature(gastm_ProgramScope.__init__)
    params = list(sig.parameters.keys())



def test_gastm_functioncallexpression_is_not_abstract():
    assert not inspect.isabstract(gastm_FunctionCallExpression)


def test_gastm_functioncallexpression_constructor_exists():
    assert callable(gastm_FunctionCallExpression.__init__)


def test_gastm_functioncallexpression_constructor_args():
    sig = inspect.signature(gastm_FunctionCallExpression.__init__)
    params = list(sig.parameters.keys())



def test_gastm_annotationexpression_is_not_abstract():
    assert not inspect.isabstract(gastm_AnnotationExpression)


def test_gastm_annotationexpression_constructor_exists():
    assert callable(gastm_AnnotationExpression.__init__)


def test_gastm_annotationexpression_constructor_args():
    sig = inspect.signature(gastm_AnnotationExpression.__init__)
    params = list(sig.parameters.keys())



def test_gastm_labelaccess_is_not_abstract():
    assert not inspect.isabstract(gastm_LabelAccess)


def test_gastm_labelaccess_constructor_exists():
    assert callable(gastm_LabelAccess.__init__)


def test_gastm_labelaccess_constructor_args():
    sig = inspect.signature(gastm_LabelAccess.__init__)
    params = list(sig.parameters.keys())


# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
ActualParameterExpression_strategy = st.builds(
    ActualParameterExpression,
)
gastm_ByReferenceActualParameterExpression_strategy = st.builds(
    gastm_ByReferenceActualParameterExpression,
)
gastm_ByValueActualParameterExpression_strategy = st.builds(
    gastm_ByValueActualParameterExpression,
)
UnaryOperator_strategy = st.builds(
    UnaryOperator,
)
gastm_BitNot_strategy = st.builds(
    gastm_BitNot,
)
gastm_Decrement_strategy = st.builds(
    gastm_Decrement,
)
gastm_Deref_strategy = st.builds(
    gastm_Deref,
)
gastm_Not_strategy = st.builds(
    gastm_Not,
)
gastm_Negate_strategy = st.builds(
    gastm_Negate,
)
gastm_AddressOf_strategy = st.builds(
    gastm_AddressOf,
)
gastm_Increment_strategy = st.builds(
    gastm_Increment,
)
gastm_PostIncrement_strategy = st.builds(
    gastm_PostIncrement,
)
gastm_PostDecrement_strategy = st.builds(
    gastm_PostDecrement,
)
gastm_UnaryPlus_strategy = st.builds(
    gastm_UnaryPlus,
)
Literal_strategy = st.builds(
    Literal,
)
gastm_StringLiteral_strategy = st.builds(
    gastm_StringLiteral,
)
gastm_BitLiteral_strategy = st.builds(
    gastm_BitLiteral,
)
gastm_BooleanLiteral_strategy = st.builds(
    gastm_BooleanLiteral,
)
gastm_CharLiteral_strategy = st.builds(
    gastm_CharLiteral,
)
gastm_RealLiteral_strategy = st.builds(
    gastm_RealLiteral,
)
gastm_IntegerlLiteral_strategy = st.builds(
    gastm_IntegerlLiteral,
)
QualifiedIdentifierReference_strategy = st.builds(
    QualifiedIdentifierReference,
)
gastm_QualifiedOverData_strategy = st.builds(
    gastm_QualifiedOverData,
)
gastm_QualifiedOverPointer_strategy = st.builds(
    gastm_QualifiedOverPointer,
)
ForStatement_strategy = st.builds(
    ForStatement,
)
gastm_ForCheckAfterStatement_strategy = st.builds(
    gastm_ForCheckAfterStatement,
)
gastm_ForCheckBeforeStatement_strategy = st.builds(
    gastm_ForCheckBeforeStatement,
)
AccessKind_strategy = st.builds(
    AccessKind,
)
gastm_Private_strategy = st.builds(
    gastm_Private,
)
gastm_Protected_strategy = st.builds(
    gastm_Protected,
)
gastm_Public_strategy = st.builds(
    gastm_Public,
)
PrimitiveType_strategy = st.builds(
    PrimitiveType,
)
gastm_WideCharacter_strategy = st.builds(
    gastm_WideCharacter,
)
gastm_Integer_strategy = st.builds(
    gastm_Integer,
)
gastm_Boolean_strategy = st.builds(
    gastm_Boolean,
)
gastm_Double_strategy = st.builds(
    gastm_Double,
)
gastm_Float_strategy = st.builds(
    gastm_Float,
)
gastm_Byte_strategy = st.builds(
    gastm_Byte,
)
gastm_LongInteger_strategy = st.builds(
    gastm_LongInteger,
)
gastm_String_strategy = st.builds(
    gastm_String,
)
gastm_Character_strategy = st.builds(
    gastm_Character,
)
gastm_LongDouble_strategy = st.builds(
    gastm_LongDouble,
)
gastm_ShortInteger_strategy = st.builds(
    gastm_ShortInteger,
)
gastm_Void_strategy = st.builds(
    gastm_Void,
)
ActualParameter_strategy = st.builds(
    ActualParameter,
)
gastm_MissingActualParameter_strategy = st.builds(
    gastm_MissingActualParameter,
)
gastm_ActualParameterExpression_strategy = st.builds(
    gastm_ActualParameterExpression,
)
BinaryOperator_strategy = st.builds(
    BinaryOperator,
)
gastm_Assign_strategy = st.builds(
    gastm_Assign,
)
gastm_Exponent_strategy = st.builds(
    gastm_Exponent,
)
gastm_BitLeftShift_strategy = st.builds(
    gastm_BitLeftShift,
)
gastm_Divide_strategy = st.builds(
    gastm_Divide,
)
gastm_NotGreater_strategy = st.builds(
    gastm_NotGreater,
)
gastm_BitRightShift_strategy = st.builds(
    gastm_BitRightShift,
)
gastm_BitAnd_strategy = st.builds(
    gastm_BitAnd,
)
gastm_Equal_strategy = st.builds(
    gastm_Equal,
)
gastm_NotLess_strategy = st.builds(
    gastm_NotLess,
)
gastm_Less_strategy = st.builds(
    gastm_Less,
)
gastm_Greater_strategy = st.builds(
    gastm_Greater,
)
gastm_BitOr_strategy = st.builds(
    gastm_BitOr,
)
gastm_Subtract_strategy = st.builds(
    gastm_Subtract,
)
gastm_Or_strategy = st.builds(
    gastm_Or,
)
gastm_BitXor_strategy = st.builds(
    gastm_BitXor,
)
gastm_Add_strategy = st.builds(
    gastm_Add,
)
gastm_Multiply_strategy = st.builds(
    gastm_Multiply,
)
gastm_NotEqual_strategy = st.builds(
    gastm_NotEqual,
)
gastm_Modulus_strategy = st.builds(
    gastm_Modulus,
)
gastm_And_strategy = st.builds(
    gastm_And,
)
gastm_OperatorAssign_strategy = st.builds(
    gastm_OperatorAssign,
)
IdentifierReference_strategy = st.builds(
    IdentifierReference,
)
NameReference_strategy = st.builds(
    NameReference,
)
gastm_TypeQualifiedIdentifierReference_strategy = st.builds(
    gastm_TypeQualifiedIdentifierReference,
)
gastm_QualifiedIdentifierReference_strategy = st.builds(
    gastm_QualifiedIdentifierReference,
)
LoopStatement_strategy = st.builds(
    LoopStatement,
)
gastm_DoWhileStatement_strategy = st.builds(
    gastm_DoWhileStatement,
)
gastm_WhileStatement_strategy = st.builds(
    gastm_WhileStatement,
)
gastm_ForStatement_strategy = st.builds(
    gastm_ForStatement,
)
CatchBlock_strategy = st.builds(
    CatchBlock,
)
gastm_TypesCatchBlock_strategy = st.builds(
    gastm_TypesCatchBlock,
)
gastm_VariableCatchBlock_strategy = st.builds(
    gastm_VariableCatchBlock,
)
BlockScope_strategy = st.builds(
    BlockScope,
)
SwitchCase_strategy = st.builds(
    SwitchCase,
)
gastm_CaseBlock_strategy = st.builds(
    gastm_CaseBlock,
)
gastm_DefaultBlock_strategy = st.builds(
    gastm_DefaultBlock,
)
LabelDefinition_strategy = st.builds(
    LabelDefinition,
)
LabelAccess_strategy = st.builds(
    LabelAccess,
)
DerivesFrom_strategy = st.builds(
    DerivesFrom,
)
EnumLiteralDefinition_strategy = st.builds(
    EnumLiteralDefinition,
)
FormalParameterType_strategy = st.builds(
    FormalParameterType,
)
gastm_ByValueFormalParameterType_strategy = st.builds(
    gastm_ByValueFormalParameterType,
)
gastm_ByReferenceFormalParameterType_strategy = st.builds(
    gastm_ByReferenceFormalParameterType,
)
Type_strategy = st.builds(
    Type,
)
gastm_FunctionType_strategy = st.builds(
    gastm_FunctionType,
)
Dimension_strategy = st.builds(
    Dimension,
)
ConstructedType_strategy = st.builds(
    ConstructedType,
)
gastm_ReferenceType_strategy = st.builds(
    gastm_ReferenceType,
)
gastm_RangeType_strategy = st.builds(
    gastm_RangeType,
)
gastm_CollectionType_strategy = st.builds(
    gastm_CollectionType,
)
gastm_PointerType_strategy = st.builds(
    gastm_PointerType,
)
gastm_ArrayType_strategy = st.builds(
    gastm_ArrayType,
)
AggregateScope_strategy = st.builds(
    AggregateScope,
)
DataType_strategy = st.builds(
    DataType,
)
gastm_ExceptionType_strategy = st.builds(
    gastm_ExceptionType,
)
gastm_ConstructedType_strategy = st.builds(
    gastm_ConstructedType,
)
gastm_EnumType_strategy = st.builds(
    gastm_EnumType,
)
gastm_AggregateType_strategy = st.builds(
    gastm_AggregateType,
)
gastm_NamedType_strategy = st.builds(
    gastm_NamedType,
)
gastm_FormalParameterType_strategy = st.builds(
    gastm_FormalParameterType,
)
gastm_PrimitiveType_strategy = st.builds(
    gastm_PrimitiveType,
    isSigned=
        st.booleans()
)
GASTMSyntaxObject_strategy = st.builds(
    GASTMSyntaxObject,
)
gastm_DefinitionObject_strategy = st.builds(
    gastm_DefinitionObject,
)
gastm_Expression_strategy = st.builds(
    gastm_Expression,
)
gastm_PreprocessorElement_strategy = st.builds(
    gastm_PreprocessorElement,
)
gastm_Type_strategy = st.builds(
    gastm_Type,
    isConst=
        st.booleans(),
    isVolatile=
        st.booleans()
)
MacroDefinition_strategy = st.builds(
    MacroDefinition,
)
LabelType_strategy = st.builds(
    LabelType,
)
NameSpaceType_strategy = st.builds(
    NameSpaceType,
)
AggregateType_strategy = st.builds(
    AggregateType,
)
gastm_AnnotationType_strategy = st.builds(
    gastm_AnnotationType,
)
gastm_StructureType_strategy = st.builds(
    gastm_StructureType,
)
gastm_UnionType_strategy = st.builds(
    gastm_UnionType,
)
gastm_ClassType_strategy = st.builds(
    gastm_ClassType,
)
NamedType_strategy = st.builds(
    NamedType,
)
TypeDefinition_strategy = st.builds(
    TypeDefinition,
)
gastm_AggregateTypeDefinition_strategy = st.builds(
    gastm_AggregateTypeDefinition,
)
gastm_NamedTypeDefinition_strategy = st.builds(
    gastm_NamedTypeDefinition,
)
Definition_strategy = st.builds(
    Definition,
)
gastm_EnumLiteralDefinition_strategy = st.builds(
    gastm_EnumLiteralDefinition,
)
DataDefinition_strategy = st.builds(
    DataDefinition,
)
gastm_BitFieldDefinition_strategy = st.builds(
    gastm_BitFieldDefinition,
)
Expression_strategy = st.builds(
    Expression,
)
gastm_BinaryExpression_strategy = st.builds(
    gastm_BinaryExpression,
)
gastm_ArrayAccess_strategy = st.builds(
    gastm_ArrayAccess,
)
gastm_Literal_strategy = st.builds(
    gastm_Literal,
    value=
        safe_text
)
gastm_AggregateExpression_strategy = st.builds(
    gastm_AggregateExpression,
)
gastm_NewExpression_strategy = st.builds(
    gastm_NewExpression,
)
gastm_ConditionalExpression_strategy = st.builds(
    gastm_ConditionalExpression,
)
gastm_CastExpression_strategy = st.builds(
    gastm_CastExpression,
)
gastm_UnaryExpression_strategy = st.builds(
    gastm_UnaryExpression,
)
gastm_RangeExpression_strategy = st.builds(
    gastm_RangeExpression,
)
gastm_NameReference_strategy = st.builds(
    gastm_NameReference,
)
gastm_DataDefinition_strategy = st.builds(
    gastm_DataDefinition,
    isMutable=
        st.booleans()
)
gastm_EntryDefinition_strategy = st.builds(
    gastm_EntryDefinition,
)
VirtualSpecification_strategy = st.builds(
    VirtualSpecification,
)
gastm_PureVirtual_strategy = st.builds(
    gastm_PureVirtual,
)
gastm_NonVirtual_strategy = st.builds(
    gastm_NonVirtual,
)
gastm_Virtual_strategy = st.builds(
    gastm_Virtual,
)
gastm_FunctionMemberAttributes_strategy = st.builds(
    gastm_FunctionMemberAttributes,
    isFriend=
        st.booleans(),
    isThisConst=
        st.booleans(),
    isInline=
        st.booleans()
)
FunctionScope_strategy = st.builds(
    FunctionScope,
)
Statement_strategy = st.builds(
    Statement,
)
gastm_EmptyStatement_strategy = st.builds(
    gastm_EmptyStatement,
)
gastm_ThrowStatement_strategy = st.builds(
    gastm_ThrowStatement,
)
gastm_ExpressionStatement_strategy = st.builds(
    gastm_ExpressionStatement,
)
gastm_IfStatement_strategy = st.builds(
    gastm_IfStatement,
)
gastm_LoopStatement_strategy = st.builds(
    gastm_LoopStatement,
)
gastm_LabeledStatement_strategy = st.builds(
    gastm_LabeledStatement,
)
gastm_JumpStatement_strategy = st.builds(
    gastm_JumpStatement,
)
gastm_TerminateStatement_strategy = st.builds(
    gastm_TerminateStatement,
)
gastm_TryStatement_strategy = st.builds(
    gastm_TryStatement,
)
gastm_ReturnStatement_strategy = st.builds(
    gastm_ReturnStatement,
)
gastm_DeclarationOrDefinitionStatement_strategy = st.builds(
    gastm_DeclarationOrDefinitionStatement,
)
gastm_BreakStatement_strategy = st.builds(
    gastm_BreakStatement,
)
gastm_BlockStatement_strategy = st.builds(
    gastm_BlockStatement,
)
gastm_ContinueStatement_strategy = st.builds(
    gastm_ContinueStatement,
)
gastm_SwitchStatement_strategy = st.builds(
    gastm_SwitchStatement,
)
gastm_DeleteStatement_strategy = st.builds(
    gastm_DeleteStatement,
)
FormalParameterDefinition_strategy = st.builds(
    FormalParameterDefinition,
)
gastm_FunctionDefinition_strategy = st.builds(
    gastm_FunctionDefinition,
)
FunctionMemberAttributes_strategy = st.builds(
    FunctionMemberAttributes,
)
FormalParameterDeclaration_strategy = st.builds(
    FormalParameterDeclaration,
)
Declaration_strategy = st.builds(
    Declaration,
)
gastm_VariableDeclaration_strategy = st.builds(
    gastm_VariableDeclaration,
    isMutable=
        st.booleans()
)
gastm_FunctionDeclaration_strategy = st.builds(
    gastm_FunctionDeclaration,
)
SourceFile_strategy = st.builds(
    SourceFile,
)
TypeReference_strategy = st.builds(
    TypeReference,
)
gastm_NamedTypeReference_strategy = st.builds(
    gastm_NamedTypeReference,
)
gastm_UnnamedTypeReference_strategy = st.builds(
    gastm_UnnamedTypeReference,
)
Name_strategy = st.builds(
    Name,
)
DeclarationOrDefinition_strategy = st.builds(
    DeclarationOrDefinition,
)
gastm_Declaration_strategy = st.builds(
    gastm_Declaration,
)
gastm_Definition_strategy = st.builds(
    gastm_Definition,
)
ProgramScope_strategy = st.builds(
    ProgramScope,
)
OtherSyntaxObject_strategy = st.builds(
    OtherSyntaxObject,
)
gastm_SwitchCase_strategy = st.builds(
    gastm_SwitchCase,
)
gastm_Dimension_strategy = st.builds(
    gastm_Dimension,
)
gastm_Name_strategy = st.builds(
    gastm_Name,
    nameString=
        safe_text
)
gastm_CatchBlock_strategy = st.builds(
    gastm_CatchBlock,
)
gastm_DerivesFrom_strategy = st.builds(
    gastm_DerivesFrom,
    isVirtual=
        st.booleans()
)
gastm_CompilationUnit_strategy = st.builds(
    gastm_CompilationUnit,
    language=
        safe_text
)
AnnotationExpression_strategy = st.builds(
    AnnotationExpression,
)
PreprocessorElement_strategy = st.builds(
    PreprocessorElement,
)
gastm_MacroCall_strategy = st.builds(
    gastm_MacroCall,
)
gastm_MacroDefinition_strategy = st.builds(
    gastm_MacroDefinition,
    macroName=
        safe_text,
    body=
        safe_text
)
gastm_Comment_strategy = st.builds(
    gastm_Comment,
    text=
        safe_text
)
gastm_IncludeUnit_strategy = st.builds(
    gastm_IncludeUnit,
)
SourceLocation_strategy = st.builds(
    SourceLocation,
)
GASTMObject_strategy = st.builds(
    GASTMObject,
)
gastm_GASTMSyntaxObject_strategy = st.builds(
    gastm_GASTMSyntaxObject,
)
Scope_strategy = st.builds(
    Scope,
)
gastm_GlobalScope_strategy = st.builds(
    gastm_GlobalScope,
)
DefinitionObject_strategy = st.builds(
    DefinitionObject,
)
gastm_NameSpaceDefinition_strategy = st.builds(
    gastm_NameSpaceDefinition,
)
gastm_LabelDefinition_strategy = st.builds(
    gastm_LabelDefinition,
)
gastm_DeclarationOrDefinition_strategy = st.builds(
    gastm_DeclarationOrDefinition,
    isRegister=
        st.booleans(),
    linkageSpecifier=
        safe_text
)
gastm_TypeDefinition_strategy = st.builds(
    gastm_TypeDefinition,
)
GlobalScope_strategy = st.builds(
    GlobalScope,
)
CompilationUnit_strategy = st.builds(
    CompilationUnit,
)
GASTMSemanticObject_strategy = st.builds(
    GASTMSemanticObject,
)
gastm_Scope_strategy = st.builds(
    gastm_Scope,
)
gastm_Project_strategy = st.builds(
    gastm_Project,
)
GASTMSourceObject_strategy = st.builds(
    GASTMSourceObject,
)
gastm_SourceLocation_strategy = st.builds(
    gastm_SourceLocation,
    endColumn=
        st.integers(),
    startLine=
        st.integers(),
    startColumn=
        st.integers(),
    endLine=
        st.integers()
)
gastm_SourceFile_strategy = st.builds(
    gastm_SourceFile,
    pathName=
        safe_text
)
gastm_ActualParameter_strategy = st.builds(
    gastm_ActualParameter,
)
gastm_BinaryOperator_strategy = st.builds(
    gastm_BinaryOperator,
)
gastm_UnaryOperator_strategy = st.builds(
    gastm_UnaryOperator,
)
gastm_AccessKind_strategy = st.builds(
    gastm_AccessKind,
)
gastm_DataType_strategy = st.builds(
    gastm_DataType,
)
gastm_StorageSpecification_strategy = st.builds(
    gastm_StorageSpecification,
)
gastm_OtherSyntaxObject_strategy = st.builds(
    gastm_OtherSyntaxObject,
)
gastm_GASTMSemanticObject_strategy = st.builds(
    gastm_GASTMSemanticObject,
)
gastm_GASTMSourceObject_strategy = st.builds(
    gastm_GASTMSourceObject,
)
gastm_GASTMObject_strategy = st.builds(
    gastm_GASTMObject,
)
StorageSpecification_strategy = st.builds(
    StorageSpecification,
)
gastm_FunctionPersistent_strategy = st.builds(
    gastm_FunctionPersistent,
)
gastm_FileLocal_strategy = st.builds(
    gastm_FileLocal,
)
gastm_NoDef_strategy = st.builds(
    gastm_NoDef,
)
gastm_PerClassMember_strategy = st.builds(
    gastm_PerClassMember,
)
gastm_External_strategy = st.builds(
    gastm_External,
)
gastm_FunctionMemberAttribute_strategy = st.builds(
    gastm_FunctionMemberAttribute,
)
gastm_VariableDefinition_strategy = st.builds(
    gastm_VariableDefinition,
)
gastm_FormalParameterDeclaration_strategy = st.builds(
    gastm_FormalParameterDeclaration,
)
gastm_VirtualSpecification_strategy = st.builds(
    gastm_VirtualSpecification,
)
gastm_FormalParameterDefinition_strategy = st.builds(
    gastm_FormalParameterDefinition,
)
gastm_IdentifierReference_strategy = st.builds(
    gastm_IdentifierReference,
)
gastm_BlockScope_strategy = st.builds(
    gastm_BlockScope,
)
gastm_AggregateScope_strategy = st.builds(
    gastm_AggregateScope,
)
gastm_LabelType_strategy = st.builds(
    gastm_LabelType,
)
gastm_NameSpaceType_strategy = st.builds(
    gastm_NameSpaceType,
)
gastm_FunctionScope_strategy = st.builds(
    gastm_FunctionScope,
)
gastm_Statement_strategy = st.builds(
    gastm_Statement,
)
gastm_TypeReference_strategy = st.builds(
    gastm_TypeReference,
)
gastm_ProgramScope_strategy = st.builds(
    gastm_ProgramScope,
)
gastm_FunctionCallExpression_strategy = st.builds(
    gastm_FunctionCallExpression,
)
gastm_AnnotationExpression_strategy = st.builds(
    gastm_AnnotationExpression,
)
gastm_LabelAccess_strategy = st.builds(
    gastm_LabelAccess,
)

@given(instance=ActualParameterExpression_strategy)
@settings(max_examples=50)
def test_actualparameterexpression_instantiation(instance):
    assert isinstance(instance, ActualParameterExpression)

@given(instance=gastm_ByReferenceActualParameterExpression_strategy)
@settings(max_examples=50)
def test_gastm_byreferenceactualparameterexpression_instantiation(instance):
    assert isinstance(instance, gastm_ByReferenceActualParameterExpression)

@given(instance=gastm_ByValueActualParameterExpression_strategy)
@settings(max_examples=50)
def test_gastm_byvalueactualparameterexpression_instantiation(instance):
    assert isinstance(instance, gastm_ByValueActualParameterExpression)

@given(instance=UnaryOperator_strategy)
@settings(max_examples=50)
def test_unaryoperator_instantiation(instance):
    assert isinstance(instance, UnaryOperator)

@given(instance=gastm_BitNot_strategy)
@settings(max_examples=50)
def test_gastm_bitnot_instantiation(instance):
    assert isinstance(instance, gastm_BitNot)

@given(instance=gastm_Decrement_strategy)
@settings(max_examples=50)
def test_gastm_decrement_instantiation(instance):
    assert isinstance(instance, gastm_Decrement)

@given(instance=gastm_Deref_strategy)
@settings(max_examples=50)
def test_gastm_deref_instantiation(instance):
    assert isinstance(instance, gastm_Deref)

@given(instance=gastm_Not_strategy)
@settings(max_examples=50)
def test_gastm_not_instantiation(instance):
    assert isinstance(instance, gastm_Not)

@given(instance=gastm_Negate_strategy)
@settings(max_examples=50)
def test_gastm_negate_instantiation(instance):
    assert isinstance(instance, gastm_Negate)

@given(instance=gastm_AddressOf_strategy)
@settings(max_examples=50)
def test_gastm_addressof_instantiation(instance):
    assert isinstance(instance, gastm_AddressOf)

@given(instance=gastm_Increment_strategy)
@settings(max_examples=50)
def test_gastm_increment_instantiation(instance):
    assert isinstance(instance, gastm_Increment)

@given(instance=gastm_PostIncrement_strategy)
@settings(max_examples=50)
def test_gastm_postincrement_instantiation(instance):
    assert isinstance(instance, gastm_PostIncrement)

@given(instance=gastm_PostDecrement_strategy)
@settings(max_examples=50)
def test_gastm_postdecrement_instantiation(instance):
    assert isinstance(instance, gastm_PostDecrement)

@given(instance=gastm_UnaryPlus_strategy)
@settings(max_examples=50)
def test_gastm_unaryplus_instantiation(instance):
    assert isinstance(instance, gastm_UnaryPlus)

@given(instance=Literal_strategy)
@settings(max_examples=50)
def test_literal_instantiation(instance):
    assert isinstance(instance, Literal)

@given(instance=gastm_StringLiteral_strategy)
@settings(max_examples=50)
def test_gastm_stringliteral_instantiation(instance):
    assert isinstance(instance, gastm_StringLiteral)

@given(instance=gastm_BitLiteral_strategy)
@settings(max_examples=50)
def test_gastm_bitliteral_instantiation(instance):
    assert isinstance(instance, gastm_BitLiteral)

@given(instance=gastm_BooleanLiteral_strategy)
@settings(max_examples=50)
def test_gastm_booleanliteral_instantiation(instance):
    assert isinstance(instance, gastm_BooleanLiteral)

@given(instance=gastm_CharLiteral_strategy)
@settings(max_examples=50)
def test_gastm_charliteral_instantiation(instance):
    assert isinstance(instance, gastm_CharLiteral)

@given(instance=gastm_RealLiteral_strategy)
@settings(max_examples=50)
def test_gastm_realliteral_instantiation(instance):
    assert isinstance(instance, gastm_RealLiteral)

@given(instance=gastm_IntegerlLiteral_strategy)
@settings(max_examples=50)
def test_gastm_integerlliteral_instantiation(instance):
    assert isinstance(instance, gastm_IntegerlLiteral)

@given(instance=QualifiedIdentifierReference_strategy)
@settings(max_examples=50)
def test_qualifiedidentifierreference_instantiation(instance):
    assert isinstance(instance, QualifiedIdentifierReference)

@given(instance=gastm_QualifiedOverData_strategy)
@settings(max_examples=50)
def test_gastm_qualifiedoverdata_instantiation(instance):
    assert isinstance(instance, gastm_QualifiedOverData)

@given(instance=gastm_QualifiedOverPointer_strategy)
@settings(max_examples=50)
def test_gastm_qualifiedoverpointer_instantiation(instance):
    assert isinstance(instance, gastm_QualifiedOverPointer)

@given(instance=ForStatement_strategy)
@settings(max_examples=50)
def test_forstatement_instantiation(instance):
    assert isinstance(instance, ForStatement)

@given(instance=gastm_ForCheckAfterStatement_strategy)
@settings(max_examples=50)
def test_gastm_forcheckafterstatement_instantiation(instance):
    assert isinstance(instance, gastm_ForCheckAfterStatement)

@given(instance=gastm_ForCheckBeforeStatement_strategy)
@settings(max_examples=50)
def test_gastm_forcheckbeforestatement_instantiation(instance):
    assert isinstance(instance, gastm_ForCheckBeforeStatement)

@given(instance=AccessKind_strategy)
@settings(max_examples=50)
def test_accesskind_instantiation(instance):
    assert isinstance(instance, AccessKind)

@given(instance=gastm_Private_strategy)
@settings(max_examples=50)
def test_gastm_private_instantiation(instance):
    assert isinstance(instance, gastm_Private)

@given(instance=gastm_Protected_strategy)
@settings(max_examples=50)
def test_gastm_protected_instantiation(instance):
    assert isinstance(instance, gastm_Protected)

@given(instance=gastm_Public_strategy)
@settings(max_examples=50)
def test_gastm_public_instantiation(instance):
    assert isinstance(instance, gastm_Public)

@given(instance=PrimitiveType_strategy)
@settings(max_examples=50)
def test_primitivetype_instantiation(instance):
    assert isinstance(instance, PrimitiveType)

@given(instance=gastm_WideCharacter_strategy)
@settings(max_examples=50)
def test_gastm_widecharacter_instantiation(instance):
    assert isinstance(instance, gastm_WideCharacter)

@given(instance=gastm_Integer_strategy)
@settings(max_examples=50)
def test_gastm_integer_instantiation(instance):
    assert isinstance(instance, gastm_Integer)

@given(instance=gastm_Boolean_strategy)
@settings(max_examples=50)
def test_gastm_boolean_instantiation(instance):
    assert isinstance(instance, gastm_Boolean)

@given(instance=gastm_Double_strategy)
@settings(max_examples=50)
def test_gastm_double_instantiation(instance):
    assert isinstance(instance, gastm_Double)

@given(instance=gastm_Float_strategy)
@settings(max_examples=50)
def test_gastm_float_instantiation(instance):
    assert isinstance(instance, gastm_Float)

@given(instance=gastm_Byte_strategy)
@settings(max_examples=50)
def test_gastm_byte_instantiation(instance):
    assert isinstance(instance, gastm_Byte)

@given(instance=gastm_LongInteger_strategy)
@settings(max_examples=50)
def test_gastm_longinteger_instantiation(instance):
    assert isinstance(instance, gastm_LongInteger)

@given(instance=gastm_String_strategy)
@settings(max_examples=50)
def test_gastm_string_instantiation(instance):
    assert isinstance(instance, gastm_String)

@given(instance=gastm_Character_strategy)
@settings(max_examples=50)
def test_gastm_character_instantiation(instance):
    assert isinstance(instance, gastm_Character)

@given(instance=gastm_LongDouble_strategy)
@settings(max_examples=50)
def test_gastm_longdouble_instantiation(instance):
    assert isinstance(instance, gastm_LongDouble)

@given(instance=gastm_ShortInteger_strategy)
@settings(max_examples=50)
def test_gastm_shortinteger_instantiation(instance):
    assert isinstance(instance, gastm_ShortInteger)

@given(instance=gastm_Void_strategy)
@settings(max_examples=50)
def test_gastm_void_instantiation(instance):
    assert isinstance(instance, gastm_Void)

@given(instance=ActualParameter_strategy)
@settings(max_examples=50)
def test_actualparameter_instantiation(instance):
    assert isinstance(instance, ActualParameter)

@given(instance=gastm_MissingActualParameter_strategy)
@settings(max_examples=50)
def test_gastm_missingactualparameter_instantiation(instance):
    assert isinstance(instance, gastm_MissingActualParameter)

@given(instance=gastm_ActualParameterExpression_strategy)
@settings(max_examples=50)
def test_gastm_actualparameterexpression_instantiation(instance):
    assert isinstance(instance, gastm_ActualParameterExpression)

@given(instance=BinaryOperator_strategy)
@settings(max_examples=50)
def test_binaryoperator_instantiation(instance):
    assert isinstance(instance, BinaryOperator)

@given(instance=gastm_Assign_strategy)
@settings(max_examples=50)
def test_gastm_assign_instantiation(instance):
    assert isinstance(instance, gastm_Assign)

@given(instance=gastm_Exponent_strategy)
@settings(max_examples=50)
def test_gastm_exponent_instantiation(instance):
    assert isinstance(instance, gastm_Exponent)

@given(instance=gastm_BitLeftShift_strategy)
@settings(max_examples=50)
def test_gastm_bitleftshift_instantiation(instance):
    assert isinstance(instance, gastm_BitLeftShift)

@given(instance=gastm_Divide_strategy)
@settings(max_examples=50)
def test_gastm_divide_instantiation(instance):
    assert isinstance(instance, gastm_Divide)

@given(instance=gastm_NotGreater_strategy)
@settings(max_examples=50)
def test_gastm_notgreater_instantiation(instance):
    assert isinstance(instance, gastm_NotGreater)

@given(instance=gastm_BitRightShift_strategy)
@settings(max_examples=50)
def test_gastm_bitrightshift_instantiation(instance):
    assert isinstance(instance, gastm_BitRightShift)

@given(instance=gastm_BitAnd_strategy)
@settings(max_examples=50)
def test_gastm_bitand_instantiation(instance):
    assert isinstance(instance, gastm_BitAnd)

@given(instance=gastm_Equal_strategy)
@settings(max_examples=50)
def test_gastm_equal_instantiation(instance):
    assert isinstance(instance, gastm_Equal)

@given(instance=gastm_NotLess_strategy)
@settings(max_examples=50)
def test_gastm_notless_instantiation(instance):
    assert isinstance(instance, gastm_NotLess)

@given(instance=gastm_Less_strategy)
@settings(max_examples=50)
def test_gastm_less_instantiation(instance):
    assert isinstance(instance, gastm_Less)

@given(instance=gastm_Greater_strategy)
@settings(max_examples=50)
def test_gastm_greater_instantiation(instance):
    assert isinstance(instance, gastm_Greater)

@given(instance=gastm_BitOr_strategy)
@settings(max_examples=50)
def test_gastm_bitor_instantiation(instance):
    assert isinstance(instance, gastm_BitOr)

@given(instance=gastm_Subtract_strategy)
@settings(max_examples=50)
def test_gastm_subtract_instantiation(instance):
    assert isinstance(instance, gastm_Subtract)

@given(instance=gastm_Or_strategy)
@settings(max_examples=50)
def test_gastm_or_instantiation(instance):
    assert isinstance(instance, gastm_Or)

@given(instance=gastm_BitXor_strategy)
@settings(max_examples=50)
def test_gastm_bitxor_instantiation(instance):
    assert isinstance(instance, gastm_BitXor)

@given(instance=gastm_Add_strategy)
@settings(max_examples=50)
def test_gastm_add_instantiation(instance):
    assert isinstance(instance, gastm_Add)

@given(instance=gastm_Multiply_strategy)
@settings(max_examples=50)
def test_gastm_multiply_instantiation(instance):
    assert isinstance(instance, gastm_Multiply)

@given(instance=gastm_NotEqual_strategy)
@settings(max_examples=50)
def test_gastm_notequal_instantiation(instance):
    assert isinstance(instance, gastm_NotEqual)

@given(instance=gastm_Modulus_strategy)
@settings(max_examples=50)
def test_gastm_modulus_instantiation(instance):
    assert isinstance(instance, gastm_Modulus)

@given(instance=gastm_And_strategy)
@settings(max_examples=50)
def test_gastm_and_instantiation(instance):
    assert isinstance(instance, gastm_And)

@given(instance=gastm_OperatorAssign_strategy)
@settings(max_examples=50)
def test_gastm_operatorassign_instantiation(instance):
    assert isinstance(instance, gastm_OperatorAssign)

@given(instance=IdentifierReference_strategy)
@settings(max_examples=50)
def test_identifierreference_instantiation(instance):
    assert isinstance(instance, IdentifierReference)

@given(instance=NameReference_strategy)
@settings(max_examples=50)
def test_namereference_instantiation(instance):
    assert isinstance(instance, NameReference)

@given(instance=gastm_TypeQualifiedIdentifierReference_strategy)
@settings(max_examples=50)
def test_gastm_typequalifiedidentifierreference_instantiation(instance):
    assert isinstance(instance, gastm_TypeQualifiedIdentifierReference)

@given(instance=gastm_QualifiedIdentifierReference_strategy)
@settings(max_examples=50)
def test_gastm_qualifiedidentifierreference_instantiation(instance):
    assert isinstance(instance, gastm_QualifiedIdentifierReference)

@given(instance=LoopStatement_strategy)
@settings(max_examples=50)
def test_loopstatement_instantiation(instance):
    assert isinstance(instance, LoopStatement)

@given(instance=gastm_DoWhileStatement_strategy)
@settings(max_examples=50)
def test_gastm_dowhilestatement_instantiation(instance):
    assert isinstance(instance, gastm_DoWhileStatement)

@given(instance=gastm_WhileStatement_strategy)
@settings(max_examples=50)
def test_gastm_whilestatement_instantiation(instance):
    assert isinstance(instance, gastm_WhileStatement)

@given(instance=gastm_ForStatement_strategy)
@settings(max_examples=50)
def test_gastm_forstatement_instantiation(instance):
    assert isinstance(instance, gastm_ForStatement)

@given(instance=CatchBlock_strategy)
@settings(max_examples=50)
def test_catchblock_instantiation(instance):
    assert isinstance(instance, CatchBlock)

@given(instance=gastm_TypesCatchBlock_strategy)
@settings(max_examples=50)
def test_gastm_typescatchblock_instantiation(instance):
    assert isinstance(instance, gastm_TypesCatchBlock)

@given(instance=gastm_VariableCatchBlock_strategy)
@settings(max_examples=50)
def test_gastm_variablecatchblock_instantiation(instance):
    assert isinstance(instance, gastm_VariableCatchBlock)

@given(instance=BlockScope_strategy)
@settings(max_examples=50)
def test_blockscope_instantiation(instance):
    assert isinstance(instance, BlockScope)

@given(instance=SwitchCase_strategy)
@settings(max_examples=50)
def test_switchcase_instantiation(instance):
    assert isinstance(instance, SwitchCase)

@given(instance=gastm_CaseBlock_strategy)
@settings(max_examples=50)
def test_gastm_caseblock_instantiation(instance):
    assert isinstance(instance, gastm_CaseBlock)

@given(instance=gastm_DefaultBlock_strategy)
@settings(max_examples=50)
def test_gastm_defaultblock_instantiation(instance):
    assert isinstance(instance, gastm_DefaultBlock)

@given(instance=LabelDefinition_strategy)
@settings(max_examples=50)
def test_labeldefinition_instantiation(instance):
    assert isinstance(instance, LabelDefinition)

@given(instance=LabelAccess_strategy)
@settings(max_examples=50)
def test_labelaccess_instantiation(instance):
    assert isinstance(instance, LabelAccess)

@given(instance=DerivesFrom_strategy)
@settings(max_examples=50)
def test_derivesfrom_instantiation(instance):
    assert isinstance(instance, DerivesFrom)

@given(instance=EnumLiteralDefinition_strategy)
@settings(max_examples=50)
def test_enumliteraldefinition_instantiation(instance):
    assert isinstance(instance, EnumLiteralDefinition)

@given(instance=FormalParameterType_strategy)
@settings(max_examples=50)
def test_formalparametertype_instantiation(instance):
    assert isinstance(instance, FormalParameterType)

@given(instance=gastm_ByValueFormalParameterType_strategy)
@settings(max_examples=50)
def test_gastm_byvalueformalparametertype_instantiation(instance):
    assert isinstance(instance, gastm_ByValueFormalParameterType)

@given(instance=gastm_ByReferenceFormalParameterType_strategy)
@settings(max_examples=50)
def test_gastm_byreferenceformalparametertype_instantiation(instance):
    assert isinstance(instance, gastm_ByReferenceFormalParameterType)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=gastm_FunctionType_strategy)
@settings(max_examples=50)
def test_gastm_functiontype_instantiation(instance):
    assert isinstance(instance, gastm_FunctionType)

@given(instance=Dimension_strategy)
@settings(max_examples=50)
def test_dimension_instantiation(instance):
    assert isinstance(instance, Dimension)

@given(instance=ConstructedType_strategy)
@settings(max_examples=50)
def test_constructedtype_instantiation(instance):
    assert isinstance(instance, ConstructedType)

@given(instance=gastm_ReferenceType_strategy)
@settings(max_examples=50)
def test_gastm_referencetype_instantiation(instance):
    assert isinstance(instance, gastm_ReferenceType)

@given(instance=gastm_RangeType_strategy)
@settings(max_examples=50)
def test_gastm_rangetype_instantiation(instance):
    assert isinstance(instance, gastm_RangeType)

@given(instance=gastm_CollectionType_strategy)
@settings(max_examples=50)
def test_gastm_collectiontype_instantiation(instance):
    assert isinstance(instance, gastm_CollectionType)

@given(instance=gastm_PointerType_strategy)
@settings(max_examples=50)
def test_gastm_pointertype_instantiation(instance):
    assert isinstance(instance, gastm_PointerType)

@given(instance=gastm_ArrayType_strategy)
@settings(max_examples=50)
def test_gastm_arraytype_instantiation(instance):
    assert isinstance(instance, gastm_ArrayType)

@given(instance=AggregateScope_strategy)
@settings(max_examples=50)
def test_aggregatescope_instantiation(instance):
    assert isinstance(instance, AggregateScope)

@given(instance=DataType_strategy)
@settings(max_examples=50)
def test_datatype_instantiation(instance):
    assert isinstance(instance, DataType)

@given(instance=gastm_ExceptionType_strategy)
@settings(max_examples=50)
def test_gastm_exceptiontype_instantiation(instance):
    assert isinstance(instance, gastm_ExceptionType)

@given(instance=gastm_ConstructedType_strategy)
@settings(max_examples=50)
def test_gastm_constructedtype_instantiation(instance):
    assert isinstance(instance, gastm_ConstructedType)

@given(instance=gastm_EnumType_strategy)
@settings(max_examples=50)
def test_gastm_enumtype_instantiation(instance):
    assert isinstance(instance, gastm_EnumType)

@given(instance=gastm_AggregateType_strategy)
@settings(max_examples=50)
def test_gastm_aggregatetype_instantiation(instance):
    assert isinstance(instance, gastm_AggregateType)

@given(instance=gastm_NamedType_strategy)
@settings(max_examples=50)
def test_gastm_namedtype_instantiation(instance):
    assert isinstance(instance, gastm_NamedType)

@given(instance=gastm_FormalParameterType_strategy)
@settings(max_examples=50)
def test_gastm_formalparametertype_instantiation(instance):
    assert isinstance(instance, gastm_FormalParameterType)

@given(instance=gastm_PrimitiveType_strategy)
@settings(max_examples=50)
def test_gastm_primitivetype_instantiation(instance):
    assert isinstance(instance, gastm_PrimitiveType)



@given(instance=gastm_PrimitiveType_strategy)
def test_gastm_primitivetype_isSigned_setter(instance):
    original = instance.isSigned
    instance.isSigned = original
    assert instance.isSigned == original

@given(instance=GASTMSyntaxObject_strategy)
@settings(max_examples=50)
def test_gastmsyntaxobject_instantiation(instance):
    assert isinstance(instance, GASTMSyntaxObject)

@given(instance=gastm_DefinitionObject_strategy)
@settings(max_examples=50)
def test_gastm_definitionobject_instantiation(instance):
    assert isinstance(instance, gastm_DefinitionObject)

@given(instance=gastm_Expression_strategy)
@settings(max_examples=50)
def test_gastm_expression_instantiation(instance):
    assert isinstance(instance, gastm_Expression)

@given(instance=gastm_PreprocessorElement_strategy)
@settings(max_examples=50)
def test_gastm_preprocessorelement_instantiation(instance):
    assert isinstance(instance, gastm_PreprocessorElement)

@given(instance=gastm_Type_strategy)
@settings(max_examples=50)
def test_gastm_type_instantiation(instance):
    assert isinstance(instance, gastm_Type)



@given(instance=gastm_Type_strategy)
def test_gastm_type_isConst_setter(instance):
    original = instance.isConst
    instance.isConst = original
    assert instance.isConst == original



@given(instance=gastm_Type_strategy)
def test_gastm_type_isVolatile_setter(instance):
    original = instance.isVolatile
    instance.isVolatile = original
    assert instance.isVolatile == original

@given(instance=MacroDefinition_strategy)
@settings(max_examples=50)
def test_macrodefinition_instantiation(instance):
    assert isinstance(instance, MacroDefinition)

@given(instance=LabelType_strategy)
@settings(max_examples=50)
def test_labeltype_instantiation(instance):
    assert isinstance(instance, LabelType)

@given(instance=NameSpaceType_strategy)
@settings(max_examples=50)
def test_namespacetype_instantiation(instance):
    assert isinstance(instance, NameSpaceType)

@given(instance=AggregateType_strategy)
@settings(max_examples=50)
def test_aggregatetype_instantiation(instance):
    assert isinstance(instance, AggregateType)

@given(instance=gastm_AnnotationType_strategy)
@settings(max_examples=50)
def test_gastm_annotationtype_instantiation(instance):
    assert isinstance(instance, gastm_AnnotationType)

@given(instance=gastm_StructureType_strategy)
@settings(max_examples=50)
def test_gastm_structuretype_instantiation(instance):
    assert isinstance(instance, gastm_StructureType)

@given(instance=gastm_UnionType_strategy)
@settings(max_examples=50)
def test_gastm_uniontype_instantiation(instance):
    assert isinstance(instance, gastm_UnionType)

@given(instance=gastm_ClassType_strategy)
@settings(max_examples=50)
def test_gastm_classtype_instantiation(instance):
    assert isinstance(instance, gastm_ClassType)

@given(instance=NamedType_strategy)
@settings(max_examples=50)
def test_namedtype_instantiation(instance):
    assert isinstance(instance, NamedType)

@given(instance=TypeDefinition_strategy)
@settings(max_examples=50)
def test_typedefinition_instantiation(instance):
    assert isinstance(instance, TypeDefinition)

@given(instance=gastm_AggregateTypeDefinition_strategy)
@settings(max_examples=50)
def test_gastm_aggregatetypedefinition_instantiation(instance):
    assert isinstance(instance, gastm_AggregateTypeDefinition)

@given(instance=gastm_NamedTypeDefinition_strategy)
@settings(max_examples=50)
def test_gastm_namedtypedefinition_instantiation(instance):
    assert isinstance(instance, gastm_NamedTypeDefinition)

@given(instance=Definition_strategy)
@settings(max_examples=50)
def test_definition_instantiation(instance):
    assert isinstance(instance, Definition)

@given(instance=gastm_EnumLiteralDefinition_strategy)
@settings(max_examples=50)
def test_gastm_enumliteraldefinition_instantiation(instance):
    assert isinstance(instance, gastm_EnumLiteralDefinition)

@given(instance=DataDefinition_strategy)
@settings(max_examples=50)
def test_datadefinition_instantiation(instance):
    assert isinstance(instance, DataDefinition)

@given(instance=gastm_BitFieldDefinition_strategy)
@settings(max_examples=50)
def test_gastm_bitfielddefinition_instantiation(instance):
    assert isinstance(instance, gastm_BitFieldDefinition)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=gastm_BinaryExpression_strategy)
@settings(max_examples=50)
def test_gastm_binaryexpression_instantiation(instance):
    assert isinstance(instance, gastm_BinaryExpression)

@given(instance=gastm_ArrayAccess_strategy)
@settings(max_examples=50)
def test_gastm_arrayaccess_instantiation(instance):
    assert isinstance(instance, gastm_ArrayAccess)

@given(instance=gastm_Literal_strategy)
@settings(max_examples=50)
def test_gastm_literal_instantiation(instance):
    assert isinstance(instance, gastm_Literal)



@given(instance=gastm_Literal_strategy)
def test_gastm_literal_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=gastm_AggregateExpression_strategy)
@settings(max_examples=50)
def test_gastm_aggregateexpression_instantiation(instance):
    assert isinstance(instance, gastm_AggregateExpression)

@given(instance=gastm_NewExpression_strategy)
@settings(max_examples=50)
def test_gastm_newexpression_instantiation(instance):
    assert isinstance(instance, gastm_NewExpression)

@given(instance=gastm_ConditionalExpression_strategy)
@settings(max_examples=50)
def test_gastm_conditionalexpression_instantiation(instance):
    assert isinstance(instance, gastm_ConditionalExpression)

@given(instance=gastm_CastExpression_strategy)
@settings(max_examples=50)
def test_gastm_castexpression_instantiation(instance):
    assert isinstance(instance, gastm_CastExpression)

@given(instance=gastm_UnaryExpression_strategy)
@settings(max_examples=50)
def test_gastm_unaryexpression_instantiation(instance):
    assert isinstance(instance, gastm_UnaryExpression)

@given(instance=gastm_RangeExpression_strategy)
@settings(max_examples=50)
def test_gastm_rangeexpression_instantiation(instance):
    assert isinstance(instance, gastm_RangeExpression)

@given(instance=gastm_NameReference_strategy)
@settings(max_examples=50)
def test_gastm_namereference_instantiation(instance):
    assert isinstance(instance, gastm_NameReference)

@given(instance=gastm_DataDefinition_strategy)
@settings(max_examples=50)
def test_gastm_datadefinition_instantiation(instance):
    assert isinstance(instance, gastm_DataDefinition)



@given(instance=gastm_DataDefinition_strategy)
def test_gastm_datadefinition_isMutable_setter(instance):
    original = instance.isMutable
    instance.isMutable = original
    assert instance.isMutable == original

@given(instance=gastm_EntryDefinition_strategy)
@settings(max_examples=50)
def test_gastm_entrydefinition_instantiation(instance):
    assert isinstance(instance, gastm_EntryDefinition)

@given(instance=VirtualSpecification_strategy)
@settings(max_examples=50)
def test_virtualspecification_instantiation(instance):
    assert isinstance(instance, VirtualSpecification)

@given(instance=gastm_PureVirtual_strategy)
@settings(max_examples=50)
def test_gastm_purevirtual_instantiation(instance):
    assert isinstance(instance, gastm_PureVirtual)

@given(instance=gastm_NonVirtual_strategy)
@settings(max_examples=50)
def test_gastm_nonvirtual_instantiation(instance):
    assert isinstance(instance, gastm_NonVirtual)

@given(instance=gastm_Virtual_strategy)
@settings(max_examples=50)
def test_gastm_virtual_instantiation(instance):
    assert isinstance(instance, gastm_Virtual)

@given(instance=gastm_FunctionMemberAttributes_strategy)
@settings(max_examples=50)
def test_gastm_functionmemberattributes_instantiation(instance):
    assert isinstance(instance, gastm_FunctionMemberAttributes)



@given(instance=gastm_FunctionMemberAttributes_strategy)
def test_gastm_functionmemberattributes_isFriend_setter(instance):
    original = instance.isFriend
    instance.isFriend = original
    assert instance.isFriend == original



@given(instance=gastm_FunctionMemberAttributes_strategy)
def test_gastm_functionmemberattributes_isThisConst_setter(instance):
    original = instance.isThisConst
    instance.isThisConst = original
    assert instance.isThisConst == original



@given(instance=gastm_FunctionMemberAttributes_strategy)
def test_gastm_functionmemberattributes_isInline_setter(instance):
    original = instance.isInline
    instance.isInline = original
    assert instance.isInline == original

@given(instance=FunctionScope_strategy)
@settings(max_examples=50)
def test_functionscope_instantiation(instance):
    assert isinstance(instance, FunctionScope)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=gastm_EmptyStatement_strategy)
@settings(max_examples=50)
def test_gastm_emptystatement_instantiation(instance):
    assert isinstance(instance, gastm_EmptyStatement)

@given(instance=gastm_ThrowStatement_strategy)
@settings(max_examples=50)
def test_gastm_throwstatement_instantiation(instance):
    assert isinstance(instance, gastm_ThrowStatement)

@given(instance=gastm_ExpressionStatement_strategy)
@settings(max_examples=50)
def test_gastm_expressionstatement_instantiation(instance):
    assert isinstance(instance, gastm_ExpressionStatement)

@given(instance=gastm_IfStatement_strategy)
@settings(max_examples=50)
def test_gastm_ifstatement_instantiation(instance):
    assert isinstance(instance, gastm_IfStatement)

@given(instance=gastm_LoopStatement_strategy)
@settings(max_examples=50)
def test_gastm_loopstatement_instantiation(instance):
    assert isinstance(instance, gastm_LoopStatement)

@given(instance=gastm_LabeledStatement_strategy)
@settings(max_examples=50)
def test_gastm_labeledstatement_instantiation(instance):
    assert isinstance(instance, gastm_LabeledStatement)

@given(instance=gastm_JumpStatement_strategy)
@settings(max_examples=50)
def test_gastm_jumpstatement_instantiation(instance):
    assert isinstance(instance, gastm_JumpStatement)

@given(instance=gastm_TerminateStatement_strategy)
@settings(max_examples=50)
def test_gastm_terminatestatement_instantiation(instance):
    assert isinstance(instance, gastm_TerminateStatement)

@given(instance=gastm_TryStatement_strategy)
@settings(max_examples=50)
def test_gastm_trystatement_instantiation(instance):
    assert isinstance(instance, gastm_TryStatement)

@given(instance=gastm_ReturnStatement_strategy)
@settings(max_examples=50)
def test_gastm_returnstatement_instantiation(instance):
    assert isinstance(instance, gastm_ReturnStatement)

@given(instance=gastm_DeclarationOrDefinitionStatement_strategy)
@settings(max_examples=50)
def test_gastm_declarationordefinitionstatement_instantiation(instance):
    assert isinstance(instance, gastm_DeclarationOrDefinitionStatement)

@given(instance=gastm_BreakStatement_strategy)
@settings(max_examples=50)
def test_gastm_breakstatement_instantiation(instance):
    assert isinstance(instance, gastm_BreakStatement)

@given(instance=gastm_BlockStatement_strategy)
@settings(max_examples=50)
def test_gastm_blockstatement_instantiation(instance):
    assert isinstance(instance, gastm_BlockStatement)

@given(instance=gastm_ContinueStatement_strategy)
@settings(max_examples=50)
def test_gastm_continuestatement_instantiation(instance):
    assert isinstance(instance, gastm_ContinueStatement)

@given(instance=gastm_SwitchStatement_strategy)
@settings(max_examples=50)
def test_gastm_switchstatement_instantiation(instance):
    assert isinstance(instance, gastm_SwitchStatement)

@given(instance=gastm_DeleteStatement_strategy)
@settings(max_examples=50)
def test_gastm_deletestatement_instantiation(instance):
    assert isinstance(instance, gastm_DeleteStatement)

@given(instance=FormalParameterDefinition_strategy)
@settings(max_examples=50)
def test_formalparameterdefinition_instantiation(instance):
    assert isinstance(instance, FormalParameterDefinition)

@given(instance=gastm_FunctionDefinition_strategy)
@settings(max_examples=50)
def test_gastm_functiondefinition_instantiation(instance):
    assert isinstance(instance, gastm_FunctionDefinition)

@given(instance=FunctionMemberAttributes_strategy)
@settings(max_examples=50)
def test_functionmemberattributes_instantiation(instance):
    assert isinstance(instance, FunctionMemberAttributes)

@given(instance=FormalParameterDeclaration_strategy)
@settings(max_examples=50)
def test_formalparameterdeclaration_instantiation(instance):
    assert isinstance(instance, FormalParameterDeclaration)

@given(instance=Declaration_strategy)
@settings(max_examples=50)
def test_declaration_instantiation(instance):
    assert isinstance(instance, Declaration)

@given(instance=gastm_VariableDeclaration_strategy)
@settings(max_examples=50)
def test_gastm_variabledeclaration_instantiation(instance):
    assert isinstance(instance, gastm_VariableDeclaration)



@given(instance=gastm_VariableDeclaration_strategy)
def test_gastm_variabledeclaration_isMutable_setter(instance):
    original = instance.isMutable
    instance.isMutable = original
    assert instance.isMutable == original

@given(instance=gastm_FunctionDeclaration_strategy)
@settings(max_examples=50)
def test_gastm_functiondeclaration_instantiation(instance):
    assert isinstance(instance, gastm_FunctionDeclaration)

@given(instance=SourceFile_strategy)
@settings(max_examples=50)
def test_sourcefile_instantiation(instance):
    assert isinstance(instance, SourceFile)

@given(instance=TypeReference_strategy)
@settings(max_examples=50)
def test_typereference_instantiation(instance):
    assert isinstance(instance, TypeReference)

@given(instance=gastm_NamedTypeReference_strategy)
@settings(max_examples=50)
def test_gastm_namedtypereference_instantiation(instance):
    assert isinstance(instance, gastm_NamedTypeReference)

@given(instance=gastm_UnnamedTypeReference_strategy)
@settings(max_examples=50)
def test_gastm_unnamedtypereference_instantiation(instance):
    assert isinstance(instance, gastm_UnnamedTypeReference)

@given(instance=Name_strategy)
@settings(max_examples=50)
def test_name_instantiation(instance):
    assert isinstance(instance, Name)

@given(instance=DeclarationOrDefinition_strategy)
@settings(max_examples=50)
def test_declarationordefinition_instantiation(instance):
    assert isinstance(instance, DeclarationOrDefinition)

@given(instance=gastm_Declaration_strategy)
@settings(max_examples=50)
def test_gastm_declaration_instantiation(instance):
    assert isinstance(instance, gastm_Declaration)

@given(instance=gastm_Definition_strategy)
@settings(max_examples=50)
def test_gastm_definition_instantiation(instance):
    assert isinstance(instance, gastm_Definition)

@given(instance=ProgramScope_strategy)
@settings(max_examples=50)
def test_programscope_instantiation(instance):
    assert isinstance(instance, ProgramScope)

@given(instance=OtherSyntaxObject_strategy)
@settings(max_examples=50)
def test_othersyntaxobject_instantiation(instance):
    assert isinstance(instance, OtherSyntaxObject)

@given(instance=gastm_SwitchCase_strategy)
@settings(max_examples=50)
def test_gastm_switchcase_instantiation(instance):
    assert isinstance(instance, gastm_SwitchCase)

@given(instance=gastm_Dimension_strategy)
@settings(max_examples=50)
def test_gastm_dimension_instantiation(instance):
    assert isinstance(instance, gastm_Dimension)

@given(instance=gastm_Name_strategy)
@settings(max_examples=50)
def test_gastm_name_instantiation(instance):
    assert isinstance(instance, gastm_Name)



@given(instance=gastm_Name_strategy)
def test_gastm_name_nameString_setter(instance):
    original = instance.nameString
    instance.nameString = original
    assert instance.nameString == original

@given(instance=gastm_CatchBlock_strategy)
@settings(max_examples=50)
def test_gastm_catchblock_instantiation(instance):
    assert isinstance(instance, gastm_CatchBlock)

@given(instance=gastm_DerivesFrom_strategy)
@settings(max_examples=50)
def test_gastm_derivesfrom_instantiation(instance):
    assert isinstance(instance, gastm_DerivesFrom)



@given(instance=gastm_DerivesFrom_strategy)
def test_gastm_derivesfrom_isVirtual_setter(instance):
    original = instance.isVirtual
    instance.isVirtual = original
    assert instance.isVirtual == original

@given(instance=gastm_CompilationUnit_strategy)
@settings(max_examples=50)
def test_gastm_compilationunit_instantiation(instance):
    assert isinstance(instance, gastm_CompilationUnit)



@given(instance=gastm_CompilationUnit_strategy)
def test_gastm_compilationunit_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original

@given(instance=AnnotationExpression_strategy)
@settings(max_examples=50)
def test_annotationexpression_instantiation(instance):
    assert isinstance(instance, AnnotationExpression)

@given(instance=PreprocessorElement_strategy)
@settings(max_examples=50)
def test_preprocessorelement_instantiation(instance):
    assert isinstance(instance, PreprocessorElement)

@given(instance=gastm_MacroCall_strategy)
@settings(max_examples=50)
def test_gastm_macrocall_instantiation(instance):
    assert isinstance(instance, gastm_MacroCall)

@given(instance=gastm_MacroDefinition_strategy)
@settings(max_examples=50)
def test_gastm_macrodefinition_instantiation(instance):
    assert isinstance(instance, gastm_MacroDefinition)



@given(instance=gastm_MacroDefinition_strategy)
def test_gastm_macrodefinition_macroName_setter(instance):
    original = instance.macroName
    instance.macroName = original
    assert instance.macroName == original



@given(instance=gastm_MacroDefinition_strategy)
def test_gastm_macrodefinition_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=gastm_Comment_strategy)
@settings(max_examples=50)
def test_gastm_comment_instantiation(instance):
    assert isinstance(instance, gastm_Comment)



@given(instance=gastm_Comment_strategy)
def test_gastm_comment_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=gastm_IncludeUnit_strategy)
@settings(max_examples=50)
def test_gastm_includeunit_instantiation(instance):
    assert isinstance(instance, gastm_IncludeUnit)

@given(instance=SourceLocation_strategy)
@settings(max_examples=50)
def test_sourcelocation_instantiation(instance):
    assert isinstance(instance, SourceLocation)

@given(instance=GASTMObject_strategy)
@settings(max_examples=50)
def test_gastmobject_instantiation(instance):
    assert isinstance(instance, GASTMObject)

@given(instance=gastm_GASTMSyntaxObject_strategy)
@settings(max_examples=50)
def test_gastm_gastmsyntaxobject_instantiation(instance):
    assert isinstance(instance, gastm_GASTMSyntaxObject)

@given(instance=Scope_strategy)
@settings(max_examples=50)
def test_scope_instantiation(instance):
    assert isinstance(instance, Scope)

@given(instance=gastm_GlobalScope_strategy)
@settings(max_examples=50)
def test_gastm_globalscope_instantiation(instance):
    assert isinstance(instance, gastm_GlobalScope)

@given(instance=DefinitionObject_strategy)
@settings(max_examples=50)
def test_definitionobject_instantiation(instance):
    assert isinstance(instance, DefinitionObject)

@given(instance=gastm_NameSpaceDefinition_strategy)
@settings(max_examples=50)
def test_gastm_namespacedefinition_instantiation(instance):
    assert isinstance(instance, gastm_NameSpaceDefinition)

@given(instance=gastm_LabelDefinition_strategy)
@settings(max_examples=50)
def test_gastm_labeldefinition_instantiation(instance):
    assert isinstance(instance, gastm_LabelDefinition)

@given(instance=gastm_DeclarationOrDefinition_strategy)
@settings(max_examples=50)
def test_gastm_declarationordefinition_instantiation(instance):
    assert isinstance(instance, gastm_DeclarationOrDefinition)



@given(instance=gastm_DeclarationOrDefinition_strategy)
def test_gastm_declarationordefinition_isRegister_setter(instance):
    original = instance.isRegister
    instance.isRegister = original
    assert instance.isRegister == original



@given(instance=gastm_DeclarationOrDefinition_strategy)
def test_gastm_declarationordefinition_linkageSpecifier_setter(instance):
    original = instance.linkageSpecifier
    instance.linkageSpecifier = original
    assert instance.linkageSpecifier == original

@given(instance=gastm_TypeDefinition_strategy)
@settings(max_examples=50)
def test_gastm_typedefinition_instantiation(instance):
    assert isinstance(instance, gastm_TypeDefinition)

@given(instance=GlobalScope_strategy)
@settings(max_examples=50)
def test_globalscope_instantiation(instance):
    assert isinstance(instance, GlobalScope)

@given(instance=CompilationUnit_strategy)
@settings(max_examples=50)
def test_compilationunit_instantiation(instance):
    assert isinstance(instance, CompilationUnit)

@given(instance=GASTMSemanticObject_strategy)
@settings(max_examples=50)
def test_gastmsemanticobject_instantiation(instance):
    assert isinstance(instance, GASTMSemanticObject)

@given(instance=gastm_Scope_strategy)
@settings(max_examples=50)
def test_gastm_scope_instantiation(instance):
    assert isinstance(instance, gastm_Scope)

@given(instance=gastm_Project_strategy)
@settings(max_examples=50)
def test_gastm_project_instantiation(instance):
    assert isinstance(instance, gastm_Project)

@given(instance=GASTMSourceObject_strategy)
@settings(max_examples=50)
def test_gastmsourceobject_instantiation(instance):
    assert isinstance(instance, GASTMSourceObject)

@given(instance=gastm_SourceLocation_strategy)
@settings(max_examples=50)
def test_gastm_sourcelocation_instantiation(instance):
    assert isinstance(instance, gastm_SourceLocation)



@given(instance=gastm_SourceLocation_strategy)
def test_gastm_sourcelocation_endColumn_setter(instance):
    original = instance.endColumn
    instance.endColumn = original
    assert instance.endColumn == original



@given(instance=gastm_SourceLocation_strategy)
def test_gastm_sourcelocation_startLine_setter(instance):
    original = instance.startLine
    instance.startLine = original
    assert instance.startLine == original



@given(instance=gastm_SourceLocation_strategy)
def test_gastm_sourcelocation_startColumn_setter(instance):
    original = instance.startColumn
    instance.startColumn = original
    assert instance.startColumn == original



@given(instance=gastm_SourceLocation_strategy)
def test_gastm_sourcelocation_endLine_setter(instance):
    original = instance.endLine
    instance.endLine = original
    assert instance.endLine == original

@given(instance=gastm_SourceFile_strategy)
@settings(max_examples=50)
def test_gastm_sourcefile_instantiation(instance):
    assert isinstance(instance, gastm_SourceFile)



@given(instance=gastm_SourceFile_strategy)
def test_gastm_sourcefile_pathName_setter(instance):
    original = instance.pathName
    instance.pathName = original
    assert instance.pathName == original

@given(instance=gastm_ActualParameter_strategy)
@settings(max_examples=50)
def test_gastm_actualparameter_instantiation(instance):
    assert isinstance(instance, gastm_ActualParameter)

@given(instance=gastm_BinaryOperator_strategy)
@settings(max_examples=50)
def test_gastm_binaryoperator_instantiation(instance):
    assert isinstance(instance, gastm_BinaryOperator)

@given(instance=gastm_UnaryOperator_strategy)
@settings(max_examples=50)
def test_gastm_unaryoperator_instantiation(instance):
    assert isinstance(instance, gastm_UnaryOperator)

@given(instance=gastm_AccessKind_strategy)
@settings(max_examples=50)
def test_gastm_accesskind_instantiation(instance):
    assert isinstance(instance, gastm_AccessKind)

@given(instance=gastm_DataType_strategy)
@settings(max_examples=50)
def test_gastm_datatype_instantiation(instance):
    assert isinstance(instance, gastm_DataType)

@given(instance=gastm_StorageSpecification_strategy)
@settings(max_examples=50)
def test_gastm_storagespecification_instantiation(instance):
    assert isinstance(instance, gastm_StorageSpecification)

@given(instance=gastm_OtherSyntaxObject_strategy)
@settings(max_examples=50)
def test_gastm_othersyntaxobject_instantiation(instance):
    assert isinstance(instance, gastm_OtherSyntaxObject)

@given(instance=gastm_GASTMSemanticObject_strategy)
@settings(max_examples=50)
def test_gastm_gastmsemanticobject_instantiation(instance):
    assert isinstance(instance, gastm_GASTMSemanticObject)

@given(instance=gastm_GASTMSourceObject_strategy)
@settings(max_examples=50)
def test_gastm_gastmsourceobject_instantiation(instance):
    assert isinstance(instance, gastm_GASTMSourceObject)

@given(instance=gastm_GASTMObject_strategy)
@settings(max_examples=50)
def test_gastm_gastmobject_instantiation(instance):
    assert isinstance(instance, gastm_GASTMObject)

@given(instance=StorageSpecification_strategy)
@settings(max_examples=50)
def test_storagespecification_instantiation(instance):
    assert isinstance(instance, StorageSpecification)

@given(instance=gastm_FunctionPersistent_strategy)
@settings(max_examples=50)
def test_gastm_functionpersistent_instantiation(instance):
    assert isinstance(instance, gastm_FunctionPersistent)

@given(instance=gastm_FileLocal_strategy)
@settings(max_examples=50)
def test_gastm_filelocal_instantiation(instance):
    assert isinstance(instance, gastm_FileLocal)

@given(instance=gastm_NoDef_strategy)
@settings(max_examples=50)
def test_gastm_nodef_instantiation(instance):
    assert isinstance(instance, gastm_NoDef)

@given(instance=gastm_PerClassMember_strategy)
@settings(max_examples=50)
def test_gastm_perclassmember_instantiation(instance):
    assert isinstance(instance, gastm_PerClassMember)

@given(instance=gastm_External_strategy)
@settings(max_examples=50)
def test_gastm_external_instantiation(instance):
    assert isinstance(instance, gastm_External)

@given(instance=gastm_FunctionMemberAttribute_strategy)
@settings(max_examples=50)
def test_gastm_functionmemberattribute_instantiation(instance):
    assert isinstance(instance, gastm_FunctionMemberAttribute)

@given(instance=gastm_VariableDefinition_strategy)
@settings(max_examples=50)
def test_gastm_variabledefinition_instantiation(instance):
    assert isinstance(instance, gastm_VariableDefinition)

@given(instance=gastm_FormalParameterDeclaration_strategy)
@settings(max_examples=50)
def test_gastm_formalparameterdeclaration_instantiation(instance):
    assert isinstance(instance, gastm_FormalParameterDeclaration)

@given(instance=gastm_VirtualSpecification_strategy)
@settings(max_examples=50)
def test_gastm_virtualspecification_instantiation(instance):
    assert isinstance(instance, gastm_VirtualSpecification)

@given(instance=gastm_FormalParameterDefinition_strategy)
@settings(max_examples=50)
def test_gastm_formalparameterdefinition_instantiation(instance):
    assert isinstance(instance, gastm_FormalParameterDefinition)

@given(instance=gastm_IdentifierReference_strategy)
@settings(max_examples=50)
def test_gastm_identifierreference_instantiation(instance):
    assert isinstance(instance, gastm_IdentifierReference)

@given(instance=gastm_BlockScope_strategy)
@settings(max_examples=50)
def test_gastm_blockscope_instantiation(instance):
    assert isinstance(instance, gastm_BlockScope)

@given(instance=gastm_AggregateScope_strategy)
@settings(max_examples=50)
def test_gastm_aggregatescope_instantiation(instance):
    assert isinstance(instance, gastm_AggregateScope)

@given(instance=gastm_LabelType_strategy)
@settings(max_examples=50)
def test_gastm_labeltype_instantiation(instance):
    assert isinstance(instance, gastm_LabelType)

@given(instance=gastm_NameSpaceType_strategy)
@settings(max_examples=50)
def test_gastm_namespacetype_instantiation(instance):
    assert isinstance(instance, gastm_NameSpaceType)

@given(instance=gastm_FunctionScope_strategy)
@settings(max_examples=50)
def test_gastm_functionscope_instantiation(instance):
    assert isinstance(instance, gastm_FunctionScope)

@given(instance=gastm_Statement_strategy)
@settings(max_examples=50)
def test_gastm_statement_instantiation(instance):
    assert isinstance(instance, gastm_Statement)

@given(instance=gastm_TypeReference_strategy)
@settings(max_examples=50)
def test_gastm_typereference_instantiation(instance):
    assert isinstance(instance, gastm_TypeReference)

@given(instance=gastm_ProgramScope_strategy)
@settings(max_examples=50)
def test_gastm_programscope_instantiation(instance):
    assert isinstance(instance, gastm_ProgramScope)

@given(instance=gastm_FunctionCallExpression_strategy)
@settings(max_examples=50)
def test_gastm_functioncallexpression_instantiation(instance):
    assert isinstance(instance, gastm_FunctionCallExpression)

@given(instance=gastm_AnnotationExpression_strategy)
@settings(max_examples=50)
def test_gastm_annotationexpression_instantiation(instance):
    assert isinstance(instance, gastm_AnnotationExpression)

@given(instance=gastm_LabelAccess_strategy)
@settings(max_examples=50)
def test_gastm_labelaccess_instantiation(instance):
    assert isinstance(instance, gastm_LabelAccess)
