import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    UnaryOperator,
    astm_AddressOf,
    astm_Not,
    astm_Deref,
    astm_BitNot,
    astm_Negate,
    astm_UnaryPlus,
    Literal,
    astm_RealLiteral,
    astm_BitLiteral,
    astm_CharLiteral,
    astm_BooleanLiteral,
    astm_StringLiteral,
    astm_PostDecrement,
    astm_PostIncrement,
    astm_IntegerLiteral,
    astm_Decrement,
    astm_Increment,
    QualifiedIdentifierReference,
    astm_QualifiedOverData,
    astm_QualifiedOverPointer,
    ForStatement,
    astm_ForCheckAfterStatement,
    astm_ForCheckBeforeStatement,
    AccessKind,
    astm_Protected,
    astm_Private,
    astm_Public,
    FormalParameterType,
    astm_ByReferenceFormalParameterType,
    astm_ByValueFormalParameterType,
    PrimitiveType,
    astm_Integer,
    astm_Float,
    astm_Double,
    astm_Boolean,
    astm_String,
    astm_LongDouble,
    astm_LongInteger,
    astm_ShortInteger,
    astm_Character,
    astm_Byte,
    astm_WideCharacter,
    astm_Void,
    ActualParameterExpression,
    astm_ByReferenceActualParameterExpression,
    astm_ByValueActualParameterExpression,
    astm_Visitable,
    VirtualSpecification,
    astm_PureVirtual,
    astm_NonVirtual,
    astm_Virtual,
    StorageSpecification,
    astm_PerClassMember,
    astm_FileLocal,
    astm_FunctionPersistent,
    astm_NoDef,
    astm_External,
    Scope,
    ActualParameter,
    astm_MissingActualParameter,
    astm_ActualParameterExpression,
    BinaryOperator,
    astm_Greater,
    astm_NotLess,
    astm_Subtract,
    astm_BitAnd,
    astm_Add,
    astm_NotGreater,
    astm_Equal,
    astm_SpecificConcatString,
    astm_Assign,
    astm_Multiply,
    astm_Or,
    astm_Divide,
    astm_SpecificIn,
    astm_Exponent,
    astm_NotEqual,
    astm_SpecificLike,
    astm_BitRightShift,
    astm_SpecificLessEqual,
    astm_SpecificGreaterEqual,
    astm_BitLeftShift,
    astm_Modulus,
    astm_BitOr,
    astm_Less,
    astm_And,
    astm_BitXor,
    astm_OperatorAssign,
    NameReference,
    astm_IdentifierReference,
    astm_TypeQualifiedIdentifierReference,
    astm_QualifiedIdentifierReference,
    CatchBlock,
    astm_VariableCatchBlock,
    astm_TypesCatchBlock,
    Expression,
    astm_BinaryExpression,
    astm_UnaryExpression,
    astm_NewExpression,
    astm_FunctionCallExpression,
    astm_RangeExpression,
    astm_ConditionalExpression,
    astm_Literal,
    astm_CastExpression,
    astm_AggregateExpression,
    astm_ArrayAccess,
    astm_NameReference,
    LoopStatement,
    astm_WhileStatement,
    astm_DoWhileStatement,
    astm_ForStatement,
    SwitchCase,
    astm_DefaultBlock,
    astm_CaseBlock,
    astm_LabelAccess,
    Statement,
    astm_IfStatement,
    astm_LabeledStatement,
    astm_ThrowStatement,
    astm_LoopStatement,
    astm_JumpStatement,
    astm_ExpressionStatement,
    astm_SwitchStatement,
    astm_ContinueStatement,
    astm_DeclarationOrDefinitionStatement,
    astm_ReturnStatement,
    astm_SpecificSelectStatement,
    astm_EmptyStatement,
    astm_TryStatement,
    astm_BreakStatement,
    astm_TerminateStatement,
    astm_DeleteStatement,
    astm_BlockScope,
    TypeReference,
    astm_BlockStatement,
    astm_UnnamedTypeReference,
    AggregateType,
    astm_StructureType,
    astm_AnnotationType,
    astm_UnionType,
    astm_ClassType,
    DataType,
    astm_ExceptionType,
    astm_EnumType,
    astm_ConstructedType,
    astm_PrimitiveType,
    astm_FormalParameterType,
    ConstructedType,
    astm_RangeType,
    astm_CollectionType,
    astm_PointerType,
    astm_ReferenceType,
    astm_ArrayType,
    astm_AggregateScope,
    PreprocessorElement,
    astm_MacroDefinition,
    astm_MacroCall,
    astm_IncludeUnit,
    astm_Comment,
    astm_AggregateType,
    astm_NamedType,
    TypeDefinition,
    astm_AggregateTypeDefinition,
    astm_NamedTypeDefinition,
    astm_FunctionScope,
    Definition,
    astm_SpecificTriggerDefinition,
    astm_FunctionDefinition,
    Declaration,
    astm_FormalParameterDeclaration,
    astm_VariableDeclaration,
    astm_FunctionDeclaration,
    astm_EnumLiteralDefinition,
    DataDefinition,
    astm_FormalParameterDefinition,
    astm_VariableDefinition,
    astm_BitFieldDefinition,
    astm_DataDefinition,
    astm_EntryDefinition,
    DefinitionObject,
    astm_TypeDefinition,
    astm_NameSpaceDefinition,
    astm_LabelDefinition,
    astm_DeclarationOrDefinition,
    astm_ProgramScope,
    OtherSyntaxObject,
    astm_SwitchCase,
    astm_FunctionMemberAttribute,
    astm_Operator,
    astm_CatchBlock,
    astm_VirtualSpecification,
    astm_Dimension,
    astm_DerivesFrom,
    astm_AnnotationExpression,
    GASTMObject,
    astm_GASTMSyntaxObject,
    DeclarationOrDefinition,
    astm_Declaration,
    astm_Definition,
    GASTMSourceObject,
    astm_SourceFile,
    Operator,
    astm_BinaryOperator,
    astm_UnaryOperator,
    Type,
    astm_LabelType,
    astm_TypeReference,
    astm_NameSpaceType,
    astm_FunctionType,
    astm_DataType,
    GASTMSyntaxObject,
    astm_Statement,
    astm_Expression,
    astm_PreprocessorElement,
    astm_Type,
    astm_OtherSyntaxObject,
    Visitable,
    astm_GASTMSemanticObject,
    astm_StorageSpecification,
    astm_ActualParameter,
    astm_GASTMSourceObject,
    astm_FunctionMemberAttributes,
    astm_AccessKind,
    astm_GASTMObject,
    FunctionCallExpression,
    astm_DelphiFunctionCallExpression,
    astm_DefinitionObject,
    astm_GlobalScope,
    astm_CompilationUnit,
    GASTMSemanticObject,
    astm_Scope,
    astm_Project,
    astm_SourceLocation,
    CompilationUnit,
    astm_DelphiUnit,
    BlockStatement,
    astm_DelphiWithStatement,
    astm_DelphiBlockStatement,
    astm_NamedTypeReference,
    astm_DelphiImplementationSection,
    astm_DelphiInterfaceSection,
    astm_Name,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_unaryoperator_is_not_abstract():
    assert not inspect.isabstract(UnaryOperator)


def test_unaryoperator_constructor_exists():
    assert callable(UnaryOperator.__init__)


def test_unaryoperator_constructor_args():
    sig = inspect.signature(UnaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_astm_addressof_is_not_abstract():
    assert not inspect.isabstract(astm_AddressOf)


def test_astm_addressof_constructor_exists():
    assert callable(astm_AddressOf.__init__)


def test_astm_addressof_constructor_args():
    sig = inspect.signature(astm_AddressOf.__init__)
    params = list(sig.parameters.keys())



def test_astm_not_is_not_abstract():
    assert not inspect.isabstract(astm_Not)


def test_astm_not_constructor_exists():
    assert callable(astm_Not.__init__)


def test_astm_not_constructor_args():
    sig = inspect.signature(astm_Not.__init__)
    params = list(sig.parameters.keys())



def test_astm_deref_is_not_abstract():
    assert not inspect.isabstract(astm_Deref)


def test_astm_deref_constructor_exists():
    assert callable(astm_Deref.__init__)


def test_astm_deref_constructor_args():
    sig = inspect.signature(astm_Deref.__init__)
    params = list(sig.parameters.keys())



def test_astm_bitnot_is_not_abstract():
    assert not inspect.isabstract(astm_BitNot)


def test_astm_bitnot_constructor_exists():
    assert callable(astm_BitNot.__init__)


def test_astm_bitnot_constructor_args():
    sig = inspect.signature(astm_BitNot.__init__)
    params = list(sig.parameters.keys())



def test_astm_negate_is_not_abstract():
    assert not inspect.isabstract(astm_Negate)


def test_astm_negate_constructor_exists():
    assert callable(astm_Negate.__init__)


def test_astm_negate_constructor_args():
    sig = inspect.signature(astm_Negate.__init__)
    params = list(sig.parameters.keys())



def test_astm_unaryplus_is_not_abstract():
    assert not inspect.isabstract(astm_UnaryPlus)


def test_astm_unaryplus_constructor_exists():
    assert callable(astm_UnaryPlus.__init__)


def test_astm_unaryplus_constructor_args():
    sig = inspect.signature(astm_UnaryPlus.__init__)
    params = list(sig.parameters.keys())



def test_literal_is_not_abstract():
    assert not inspect.isabstract(Literal)


def test_literal_constructor_exists():
    assert callable(Literal.__init__)


def test_literal_constructor_args():
    sig = inspect.signature(Literal.__init__)
    params = list(sig.parameters.keys())



def test_astm_realliteral_is_not_abstract():
    assert not inspect.isabstract(astm_RealLiteral)


def test_astm_realliteral_constructor_exists():
    assert callable(astm_RealLiteral.__init__)


def test_astm_realliteral_constructor_args():
    sig = inspect.signature(astm_RealLiteral.__init__)
    params = list(sig.parameters.keys())



def test_astm_bitliteral_is_not_abstract():
    assert not inspect.isabstract(astm_BitLiteral)


def test_astm_bitliteral_constructor_exists():
    assert callable(astm_BitLiteral.__init__)


def test_astm_bitliteral_constructor_args():
    sig = inspect.signature(astm_BitLiteral.__init__)
    params = list(sig.parameters.keys())



def test_astm_charliteral_is_not_abstract():
    assert not inspect.isabstract(astm_CharLiteral)


def test_astm_charliteral_constructor_exists():
    assert callable(astm_CharLiteral.__init__)


def test_astm_charliteral_constructor_args():
    sig = inspect.signature(astm_CharLiteral.__init__)
    params = list(sig.parameters.keys())



def test_astm_booleanliteral_is_not_abstract():
    assert not inspect.isabstract(astm_BooleanLiteral)


def test_astm_booleanliteral_constructor_exists():
    assert callable(astm_BooleanLiteral.__init__)


def test_astm_booleanliteral_constructor_args():
    sig = inspect.signature(astm_BooleanLiteral.__init__)
    params = list(sig.parameters.keys())



def test_astm_stringliteral_is_not_abstract():
    assert not inspect.isabstract(astm_StringLiteral)


def test_astm_stringliteral_constructor_exists():
    assert callable(astm_StringLiteral.__init__)


def test_astm_stringliteral_constructor_args():
    sig = inspect.signature(astm_StringLiteral.__init__)
    params = list(sig.parameters.keys())



def test_astm_postdecrement_is_not_abstract():
    assert not inspect.isabstract(astm_PostDecrement)


def test_astm_postdecrement_constructor_exists():
    assert callable(astm_PostDecrement.__init__)


def test_astm_postdecrement_constructor_args():
    sig = inspect.signature(astm_PostDecrement.__init__)
    params = list(sig.parameters.keys())



def test_astm_postincrement_is_not_abstract():
    assert not inspect.isabstract(astm_PostIncrement)


def test_astm_postincrement_constructor_exists():
    assert callable(astm_PostIncrement.__init__)


def test_astm_postincrement_constructor_args():
    sig = inspect.signature(astm_PostIncrement.__init__)
    params = list(sig.parameters.keys())



def test_astm_integerliteral_is_not_abstract():
    assert not inspect.isabstract(astm_IntegerLiteral)


def test_astm_integerliteral_constructor_exists():
    assert callable(astm_IntegerLiteral.__init__)


def test_astm_integerliteral_constructor_args():
    sig = inspect.signature(astm_IntegerLiteral.__init__)
    params = list(sig.parameters.keys())



def test_astm_decrement_is_not_abstract():
    assert not inspect.isabstract(astm_Decrement)


def test_astm_decrement_constructor_exists():
    assert callable(astm_Decrement.__init__)


def test_astm_decrement_constructor_args():
    sig = inspect.signature(astm_Decrement.__init__)
    params = list(sig.parameters.keys())



def test_astm_increment_is_not_abstract():
    assert not inspect.isabstract(astm_Increment)


def test_astm_increment_constructor_exists():
    assert callable(astm_Increment.__init__)


def test_astm_increment_constructor_args():
    sig = inspect.signature(astm_Increment.__init__)
    params = list(sig.parameters.keys())



def test_qualifiedidentifierreference_is_not_abstract():
    assert not inspect.isabstract(QualifiedIdentifierReference)


def test_qualifiedidentifierreference_constructor_exists():
    assert callable(QualifiedIdentifierReference.__init__)


def test_qualifiedidentifierreference_constructor_args():
    sig = inspect.signature(QualifiedIdentifierReference.__init__)
    params = list(sig.parameters.keys())



def test_astm_qualifiedoverdata_is_not_abstract():
    assert not inspect.isabstract(astm_QualifiedOverData)


def test_astm_qualifiedoverdata_constructor_exists():
    assert callable(astm_QualifiedOverData.__init__)


def test_astm_qualifiedoverdata_constructor_args():
    sig = inspect.signature(astm_QualifiedOverData.__init__)
    params = list(sig.parameters.keys())



def test_astm_qualifiedoverpointer_is_not_abstract():
    assert not inspect.isabstract(astm_QualifiedOverPointer)


def test_astm_qualifiedoverpointer_constructor_exists():
    assert callable(astm_QualifiedOverPointer.__init__)


def test_astm_qualifiedoverpointer_constructor_args():
    sig = inspect.signature(astm_QualifiedOverPointer.__init__)
    params = list(sig.parameters.keys())



def test_forstatement_is_not_abstract():
    assert not inspect.isabstract(ForStatement)


def test_forstatement_constructor_exists():
    assert callable(ForStatement.__init__)


def test_forstatement_constructor_args():
    sig = inspect.signature(ForStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm_forcheckafterstatement_is_not_abstract():
    assert not inspect.isabstract(astm_ForCheckAfterStatement)


def test_astm_forcheckafterstatement_constructor_exists():
    assert callable(astm_ForCheckAfterStatement.__init__)


def test_astm_forcheckafterstatement_constructor_args():
    sig = inspect.signature(astm_ForCheckAfterStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm_forcheckbeforestatement_is_not_abstract():
    assert not inspect.isabstract(astm_ForCheckBeforeStatement)


def test_astm_forcheckbeforestatement_constructor_exists():
    assert callable(astm_ForCheckBeforeStatement.__init__)


def test_astm_forcheckbeforestatement_constructor_args():
    sig = inspect.signature(astm_ForCheckBeforeStatement.__init__)
    params = list(sig.parameters.keys())



def test_accesskind_is_not_abstract():
    assert not inspect.isabstract(AccessKind)


def test_accesskind_constructor_exists():
    assert callable(AccessKind.__init__)


def test_accesskind_constructor_args():
    sig = inspect.signature(AccessKind.__init__)
    params = list(sig.parameters.keys())



def test_astm_protected_is_not_abstract():
    assert not inspect.isabstract(astm_Protected)


def test_astm_protected_constructor_exists():
    assert callable(astm_Protected.__init__)


def test_astm_protected_constructor_args():
    sig = inspect.signature(astm_Protected.__init__)
    params = list(sig.parameters.keys())



def test_astm_private_is_not_abstract():
    assert not inspect.isabstract(astm_Private)


def test_astm_private_constructor_exists():
    assert callable(astm_Private.__init__)


def test_astm_private_constructor_args():
    sig = inspect.signature(astm_Private.__init__)
    params = list(sig.parameters.keys())



def test_astm_public_is_not_abstract():
    assert not inspect.isabstract(astm_Public)


def test_astm_public_constructor_exists():
    assert callable(astm_Public.__init__)


def test_astm_public_constructor_args():
    sig = inspect.signature(astm_Public.__init__)
    params = list(sig.parameters.keys())



def test_formalparametertype_is_not_abstract():
    assert not inspect.isabstract(FormalParameterType)


def test_formalparametertype_constructor_exists():
    assert callable(FormalParameterType.__init__)


def test_formalparametertype_constructor_args():
    sig = inspect.signature(FormalParameterType.__init__)
    params = list(sig.parameters.keys())



def test_astm_byreferenceformalparametertype_is_not_abstract():
    assert not inspect.isabstract(astm_ByReferenceFormalParameterType)


def test_astm_byreferenceformalparametertype_constructor_exists():
    assert callable(astm_ByReferenceFormalParameterType.__init__)


def test_astm_byreferenceformalparametertype_constructor_args():
    sig = inspect.signature(astm_ByReferenceFormalParameterType.__init__)
    params = list(sig.parameters.keys())



def test_astm_byvalueformalparametertype_is_not_abstract():
    assert not inspect.isabstract(astm_ByValueFormalParameterType)


def test_astm_byvalueformalparametertype_constructor_exists():
    assert callable(astm_ByValueFormalParameterType.__init__)


def test_astm_byvalueformalparametertype_constructor_args():
    sig = inspect.signature(astm_ByValueFormalParameterType.__init__)
    params = list(sig.parameters.keys())



def test_primitivetype_is_not_abstract():
    assert not inspect.isabstract(PrimitiveType)


def test_primitivetype_constructor_exists():
    assert callable(PrimitiveType.__init__)


def test_primitivetype_constructor_args():
    sig = inspect.signature(PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_astm_integer_is_not_abstract():
    assert not inspect.isabstract(astm_Integer)


def test_astm_integer_constructor_exists():
    assert callable(astm_Integer.__init__)


def test_astm_integer_constructor_args():
    sig = inspect.signature(astm_Integer.__init__)
    params = list(sig.parameters.keys())



def test_astm_float_is_not_abstract():
    assert not inspect.isabstract(astm_Float)


def test_astm_float_constructor_exists():
    assert callable(astm_Float.__init__)


def test_astm_float_constructor_args():
    sig = inspect.signature(astm_Float.__init__)
    params = list(sig.parameters.keys())



def test_astm_double_is_not_abstract():
    assert not inspect.isabstract(astm_Double)


def test_astm_double_constructor_exists():
    assert callable(astm_Double.__init__)


def test_astm_double_constructor_args():
    sig = inspect.signature(astm_Double.__init__)
    params = list(sig.parameters.keys())



def test_astm_boolean_is_not_abstract():
    assert not inspect.isabstract(astm_Boolean)


def test_astm_boolean_constructor_exists():
    assert callable(astm_Boolean.__init__)


def test_astm_boolean_constructor_args():
    sig = inspect.signature(astm_Boolean.__init__)
    params = list(sig.parameters.keys())



def test_astm_string_is_not_abstract():
    assert not inspect.isabstract(astm_String)


def test_astm_string_constructor_exists():
    assert callable(astm_String.__init__)


def test_astm_string_constructor_args():
    sig = inspect.signature(astm_String.__init__)
    params = list(sig.parameters.keys())



def test_astm_longdouble_is_not_abstract():
    assert not inspect.isabstract(astm_LongDouble)


def test_astm_longdouble_constructor_exists():
    assert callable(astm_LongDouble.__init__)


def test_astm_longdouble_constructor_args():
    sig = inspect.signature(astm_LongDouble.__init__)
    params = list(sig.parameters.keys())



def test_astm_longinteger_is_not_abstract():
    assert not inspect.isabstract(astm_LongInteger)


def test_astm_longinteger_constructor_exists():
    assert callable(astm_LongInteger.__init__)


def test_astm_longinteger_constructor_args():
    sig = inspect.signature(astm_LongInteger.__init__)
    params = list(sig.parameters.keys())



def test_astm_shortinteger_is_not_abstract():
    assert not inspect.isabstract(astm_ShortInteger)


def test_astm_shortinteger_constructor_exists():
    assert callable(astm_ShortInteger.__init__)


def test_astm_shortinteger_constructor_args():
    sig = inspect.signature(astm_ShortInteger.__init__)
    params = list(sig.parameters.keys())



def test_astm_character_is_not_abstract():
    assert not inspect.isabstract(astm_Character)


def test_astm_character_constructor_exists():
    assert callable(astm_Character.__init__)


def test_astm_character_constructor_args():
    sig = inspect.signature(astm_Character.__init__)
    params = list(sig.parameters.keys())



def test_astm_byte_is_not_abstract():
    assert not inspect.isabstract(astm_Byte)


def test_astm_byte_constructor_exists():
    assert callable(astm_Byte.__init__)


def test_astm_byte_constructor_args():
    sig = inspect.signature(astm_Byte.__init__)
    params = list(sig.parameters.keys())



def test_astm_widecharacter_is_not_abstract():
    assert not inspect.isabstract(astm_WideCharacter)


def test_astm_widecharacter_constructor_exists():
    assert callable(astm_WideCharacter.__init__)


def test_astm_widecharacter_constructor_args():
    sig = inspect.signature(astm_WideCharacter.__init__)
    params = list(sig.parameters.keys())



def test_astm_void_is_not_abstract():
    assert not inspect.isabstract(astm_Void)


def test_astm_void_constructor_exists():
    assert callable(astm_Void.__init__)


def test_astm_void_constructor_args():
    sig = inspect.signature(astm_Void.__init__)
    params = list(sig.parameters.keys())



def test_actualparameterexpression_is_not_abstract():
    assert not inspect.isabstract(ActualParameterExpression)


def test_actualparameterexpression_constructor_exists():
    assert callable(ActualParameterExpression.__init__)


def test_actualparameterexpression_constructor_args():
    sig = inspect.signature(ActualParameterExpression.__init__)
    params = list(sig.parameters.keys())



def test_astm_byreferenceactualparameterexpression_is_not_abstract():
    assert not inspect.isabstract(astm_ByReferenceActualParameterExpression)


def test_astm_byreferenceactualparameterexpression_constructor_exists():
    assert callable(astm_ByReferenceActualParameterExpression.__init__)


def test_astm_byreferenceactualparameterexpression_constructor_args():
    sig = inspect.signature(astm_ByReferenceActualParameterExpression.__init__)
    params = list(sig.parameters.keys())



def test_astm_byvalueactualparameterexpression_is_not_abstract():
    assert not inspect.isabstract(astm_ByValueActualParameterExpression)


def test_astm_byvalueactualparameterexpression_constructor_exists():
    assert callable(astm_ByValueActualParameterExpression.__init__)


def test_astm_byvalueactualparameterexpression_constructor_args():
    sig = inspect.signature(astm_ByValueActualParameterExpression.__init__)
    params = list(sig.parameters.keys())



def test_astm_visitable_is_not_abstract():
    assert not inspect.isabstract(astm_Visitable)


def test_astm_visitable_constructor_exists():
    assert callable(astm_Visitable.__init__)


def test_astm_visitable_constructor_args():
    sig = inspect.signature(astm_Visitable.__init__)
    params = list(sig.parameters.keys())



def test_virtualspecification_is_not_abstract():
    assert not inspect.isabstract(VirtualSpecification)


def test_virtualspecification_constructor_exists():
    assert callable(VirtualSpecification.__init__)


def test_virtualspecification_constructor_args():
    sig = inspect.signature(VirtualSpecification.__init__)
    params = list(sig.parameters.keys())



def test_astm_purevirtual_is_not_abstract():
    assert not inspect.isabstract(astm_PureVirtual)


def test_astm_purevirtual_constructor_exists():
    assert callable(astm_PureVirtual.__init__)


def test_astm_purevirtual_constructor_args():
    sig = inspect.signature(astm_PureVirtual.__init__)
    params = list(sig.parameters.keys())



def test_astm_nonvirtual_is_not_abstract():
    assert not inspect.isabstract(astm_NonVirtual)


def test_astm_nonvirtual_constructor_exists():
    assert callable(astm_NonVirtual.__init__)


def test_astm_nonvirtual_constructor_args():
    sig = inspect.signature(astm_NonVirtual.__init__)
    params = list(sig.parameters.keys())



def test_astm_virtual_is_not_abstract():
    assert not inspect.isabstract(astm_Virtual)


def test_astm_virtual_constructor_exists():
    assert callable(astm_Virtual.__init__)


def test_astm_virtual_constructor_args():
    sig = inspect.signature(astm_Virtual.__init__)
    params = list(sig.parameters.keys())



def test_storagespecification_is_not_abstract():
    assert not inspect.isabstract(StorageSpecification)


def test_storagespecification_constructor_exists():
    assert callable(StorageSpecification.__init__)


def test_storagespecification_constructor_args():
    sig = inspect.signature(StorageSpecification.__init__)
    params = list(sig.parameters.keys())



def test_astm_perclassmember_is_not_abstract():
    assert not inspect.isabstract(astm_PerClassMember)


def test_astm_perclassmember_constructor_exists():
    assert callable(astm_PerClassMember.__init__)


def test_astm_perclassmember_constructor_args():
    sig = inspect.signature(astm_PerClassMember.__init__)
    params = list(sig.parameters.keys())



def test_astm_filelocal_is_not_abstract():
    assert not inspect.isabstract(astm_FileLocal)


def test_astm_filelocal_constructor_exists():
    assert callable(astm_FileLocal.__init__)


def test_astm_filelocal_constructor_args():
    sig = inspect.signature(astm_FileLocal.__init__)
    params = list(sig.parameters.keys())



def test_astm_functionpersistent_is_not_abstract():
    assert not inspect.isabstract(astm_FunctionPersistent)


def test_astm_functionpersistent_constructor_exists():
    assert callable(astm_FunctionPersistent.__init__)


def test_astm_functionpersistent_constructor_args():
    sig = inspect.signature(astm_FunctionPersistent.__init__)
    params = list(sig.parameters.keys())



def test_astm_nodef_is_not_abstract():
    assert not inspect.isabstract(astm_NoDef)


def test_astm_nodef_constructor_exists():
    assert callable(astm_NoDef.__init__)


def test_astm_nodef_constructor_args():
    sig = inspect.signature(astm_NoDef.__init__)
    params = list(sig.parameters.keys())



def test_astm_external_is_not_abstract():
    assert not inspect.isabstract(astm_External)


def test_astm_external_constructor_exists():
    assert callable(astm_External.__init__)


def test_astm_external_constructor_args():
    sig = inspect.signature(astm_External.__init__)
    params = list(sig.parameters.keys())



def test_scope_is_not_abstract():
    assert not inspect.isabstract(Scope)


def test_scope_constructor_exists():
    assert callable(Scope.__init__)


def test_scope_constructor_args():
    sig = inspect.signature(Scope.__init__)
    params = list(sig.parameters.keys())



def test_actualparameter_is_not_abstract():
    assert not inspect.isabstract(ActualParameter)


def test_actualparameter_constructor_exists():
    assert callable(ActualParameter.__init__)


def test_actualparameter_constructor_args():
    sig = inspect.signature(ActualParameter.__init__)
    params = list(sig.parameters.keys())



def test_astm_missingactualparameter_is_not_abstract():
    assert not inspect.isabstract(astm_MissingActualParameter)


def test_astm_missingactualparameter_constructor_exists():
    assert callable(astm_MissingActualParameter.__init__)


def test_astm_missingactualparameter_constructor_args():
    sig = inspect.signature(astm_MissingActualParameter.__init__)
    params = list(sig.parameters.keys())



def test_astm_actualparameterexpression_is_not_abstract():
    assert not inspect.isabstract(astm_ActualParameterExpression)


def test_astm_actualparameterexpression_constructor_exists():
    assert callable(astm_ActualParameterExpression.__init__)


def test_astm_actualparameterexpression_constructor_args():
    sig = inspect.signature(astm_ActualParameterExpression.__init__)
    params = list(sig.parameters.keys())



def test_binaryoperator_is_not_abstract():
    assert not inspect.isabstract(BinaryOperator)


def test_binaryoperator_constructor_exists():
    assert callable(BinaryOperator.__init__)


def test_binaryoperator_constructor_args():
    sig = inspect.signature(BinaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_astm_greater_is_not_abstract():
    assert not inspect.isabstract(astm_Greater)


def test_astm_greater_constructor_exists():
    assert callable(astm_Greater.__init__)


def test_astm_greater_constructor_args():
    sig = inspect.signature(astm_Greater.__init__)
    params = list(sig.parameters.keys())



def test_astm_notless_is_not_abstract():
    assert not inspect.isabstract(astm_NotLess)


def test_astm_notless_constructor_exists():
    assert callable(astm_NotLess.__init__)


def test_astm_notless_constructor_args():
    sig = inspect.signature(astm_NotLess.__init__)
    params = list(sig.parameters.keys())



def test_astm_subtract_is_not_abstract():
    assert not inspect.isabstract(astm_Subtract)


def test_astm_subtract_constructor_exists():
    assert callable(astm_Subtract.__init__)


def test_astm_subtract_constructor_args():
    sig = inspect.signature(astm_Subtract.__init__)
    params = list(sig.parameters.keys())



def test_astm_bitand_is_not_abstract():
    assert not inspect.isabstract(astm_BitAnd)


def test_astm_bitand_constructor_exists():
    assert callable(astm_BitAnd.__init__)


def test_astm_bitand_constructor_args():
    sig = inspect.signature(astm_BitAnd.__init__)
    params = list(sig.parameters.keys())



def test_astm_add_is_not_abstract():
    assert not inspect.isabstract(astm_Add)


def test_astm_add_constructor_exists():
    assert callable(astm_Add.__init__)


def test_astm_add_constructor_args():
    sig = inspect.signature(astm_Add.__init__)
    params = list(sig.parameters.keys())



def test_astm_notgreater_is_not_abstract():
    assert not inspect.isabstract(astm_NotGreater)


def test_astm_notgreater_constructor_exists():
    assert callable(astm_NotGreater.__init__)


def test_astm_notgreater_constructor_args():
    sig = inspect.signature(astm_NotGreater.__init__)
    params = list(sig.parameters.keys())



def test_astm_equal_is_not_abstract():
    assert not inspect.isabstract(astm_Equal)


def test_astm_equal_constructor_exists():
    assert callable(astm_Equal.__init__)


def test_astm_equal_constructor_args():
    sig = inspect.signature(astm_Equal.__init__)
    params = list(sig.parameters.keys())



def test_astm_specificconcatstring_is_not_abstract():
    assert not inspect.isabstract(astm_SpecificConcatString)


def test_astm_specificconcatstring_constructor_exists():
    assert callable(astm_SpecificConcatString.__init__)


def test_astm_specificconcatstring_constructor_args():
    sig = inspect.signature(astm_SpecificConcatString.__init__)
    params = list(sig.parameters.keys())



def test_astm_assign_is_not_abstract():
    assert not inspect.isabstract(astm_Assign)


def test_astm_assign_constructor_exists():
    assert callable(astm_Assign.__init__)


def test_astm_assign_constructor_args():
    sig = inspect.signature(astm_Assign.__init__)
    params = list(sig.parameters.keys())



def test_astm_multiply_is_not_abstract():
    assert not inspect.isabstract(astm_Multiply)


def test_astm_multiply_constructor_exists():
    assert callable(astm_Multiply.__init__)


def test_astm_multiply_constructor_args():
    sig = inspect.signature(astm_Multiply.__init__)
    params = list(sig.parameters.keys())



def test_astm_or_is_not_abstract():
    assert not inspect.isabstract(astm_Or)


def test_astm_or_constructor_exists():
    assert callable(astm_Or.__init__)


def test_astm_or_constructor_args():
    sig = inspect.signature(astm_Or.__init__)
    params = list(sig.parameters.keys())



def test_astm_divide_is_not_abstract():
    assert not inspect.isabstract(astm_Divide)


def test_astm_divide_constructor_exists():
    assert callable(astm_Divide.__init__)


def test_astm_divide_constructor_args():
    sig = inspect.signature(astm_Divide.__init__)
    params = list(sig.parameters.keys())



def test_astm_specificin_is_not_abstract():
    assert not inspect.isabstract(astm_SpecificIn)


def test_astm_specificin_constructor_exists():
    assert callable(astm_SpecificIn.__init__)


def test_astm_specificin_constructor_args():
    sig = inspect.signature(astm_SpecificIn.__init__)
    params = list(sig.parameters.keys())



def test_astm_exponent_is_not_abstract():
    assert not inspect.isabstract(astm_Exponent)


def test_astm_exponent_constructor_exists():
    assert callable(astm_Exponent.__init__)


def test_astm_exponent_constructor_args():
    sig = inspect.signature(astm_Exponent.__init__)
    params = list(sig.parameters.keys())



def test_astm_notequal_is_not_abstract():
    assert not inspect.isabstract(astm_NotEqual)


def test_astm_notequal_constructor_exists():
    assert callable(astm_NotEqual.__init__)


def test_astm_notequal_constructor_args():
    sig = inspect.signature(astm_NotEqual.__init__)
    params = list(sig.parameters.keys())



def test_astm_specificlike_is_not_abstract():
    assert not inspect.isabstract(astm_SpecificLike)


def test_astm_specificlike_constructor_exists():
    assert callable(astm_SpecificLike.__init__)


def test_astm_specificlike_constructor_args():
    sig = inspect.signature(astm_SpecificLike.__init__)
    params = list(sig.parameters.keys())



def test_astm_bitrightshift_is_not_abstract():
    assert not inspect.isabstract(astm_BitRightShift)


def test_astm_bitrightshift_constructor_exists():
    assert callable(astm_BitRightShift.__init__)


def test_astm_bitrightshift_constructor_args():
    sig = inspect.signature(astm_BitRightShift.__init__)
    params = list(sig.parameters.keys())



def test_astm_specificlessequal_is_not_abstract():
    assert not inspect.isabstract(astm_SpecificLessEqual)


def test_astm_specificlessequal_constructor_exists():
    assert callable(astm_SpecificLessEqual.__init__)


def test_astm_specificlessequal_constructor_args():
    sig = inspect.signature(astm_SpecificLessEqual.__init__)
    params = list(sig.parameters.keys())



def test_astm_specificgreaterequal_is_not_abstract():
    assert not inspect.isabstract(astm_SpecificGreaterEqual)


def test_astm_specificgreaterequal_constructor_exists():
    assert callable(astm_SpecificGreaterEqual.__init__)


def test_astm_specificgreaterequal_constructor_args():
    sig = inspect.signature(astm_SpecificGreaterEqual.__init__)
    params = list(sig.parameters.keys())



def test_astm_bitleftshift_is_not_abstract():
    assert not inspect.isabstract(astm_BitLeftShift)


def test_astm_bitleftshift_constructor_exists():
    assert callable(astm_BitLeftShift.__init__)


def test_astm_bitleftshift_constructor_args():
    sig = inspect.signature(astm_BitLeftShift.__init__)
    params = list(sig.parameters.keys())



def test_astm_modulus_is_not_abstract():
    assert not inspect.isabstract(astm_Modulus)


def test_astm_modulus_constructor_exists():
    assert callable(astm_Modulus.__init__)


def test_astm_modulus_constructor_args():
    sig = inspect.signature(astm_Modulus.__init__)
    params = list(sig.parameters.keys())



def test_astm_bitor_is_not_abstract():
    assert not inspect.isabstract(astm_BitOr)


def test_astm_bitor_constructor_exists():
    assert callable(astm_BitOr.__init__)


def test_astm_bitor_constructor_args():
    sig = inspect.signature(astm_BitOr.__init__)
    params = list(sig.parameters.keys())



def test_astm_less_is_not_abstract():
    assert not inspect.isabstract(astm_Less)


def test_astm_less_constructor_exists():
    assert callable(astm_Less.__init__)


def test_astm_less_constructor_args():
    sig = inspect.signature(astm_Less.__init__)
    params = list(sig.parameters.keys())



def test_astm_and_is_not_abstract():
    assert not inspect.isabstract(astm_And)


def test_astm_and_constructor_exists():
    assert callable(astm_And.__init__)


def test_astm_and_constructor_args():
    sig = inspect.signature(astm_And.__init__)
    params = list(sig.parameters.keys())



def test_astm_bitxor_is_not_abstract():
    assert not inspect.isabstract(astm_BitXor)


def test_astm_bitxor_constructor_exists():
    assert callable(astm_BitXor.__init__)


def test_astm_bitxor_constructor_args():
    sig = inspect.signature(astm_BitXor.__init__)
    params = list(sig.parameters.keys())



def test_astm_operatorassign_is_not_abstract():
    assert not inspect.isabstract(astm_OperatorAssign)


def test_astm_operatorassign_constructor_exists():
    assert callable(astm_OperatorAssign.__init__)


def test_astm_operatorassign_constructor_args():
    sig = inspect.signature(astm_OperatorAssign.__init__)
    params = list(sig.parameters.keys())



def test_namereference_is_not_abstract():
    assert not inspect.isabstract(NameReference)


def test_namereference_constructor_exists():
    assert callable(NameReference.__init__)


def test_namereference_constructor_args():
    sig = inspect.signature(NameReference.__init__)
    params = list(sig.parameters.keys())



def test_astm_identifierreference_is_not_abstract():
    assert not inspect.isabstract(astm_IdentifierReference)


def test_astm_identifierreference_constructor_exists():
    assert callable(astm_IdentifierReference.__init__)


def test_astm_identifierreference_constructor_args():
    sig = inspect.signature(astm_IdentifierReference.__init__)
    params = list(sig.parameters.keys())



def test_astm_typequalifiedidentifierreference_is_not_abstract():
    assert not inspect.isabstract(astm_TypeQualifiedIdentifierReference)


def test_astm_typequalifiedidentifierreference_constructor_exists():
    assert callable(astm_TypeQualifiedIdentifierReference.__init__)


def test_astm_typequalifiedidentifierreference_constructor_args():
    sig = inspect.signature(astm_TypeQualifiedIdentifierReference.__init__)
    params = list(sig.parameters.keys())



def test_astm_qualifiedidentifierreference_is_not_abstract():
    assert not inspect.isabstract(astm_QualifiedIdentifierReference)


def test_astm_qualifiedidentifierreference_constructor_exists():
    assert callable(astm_QualifiedIdentifierReference.__init__)


def test_astm_qualifiedidentifierreference_constructor_args():
    sig = inspect.signature(astm_QualifiedIdentifierReference.__init__)
    params = list(sig.parameters.keys())



def test_catchblock_is_not_abstract():
    assert not inspect.isabstract(CatchBlock)


def test_catchblock_constructor_exists():
    assert callable(CatchBlock.__init__)


def test_catchblock_constructor_args():
    sig = inspect.signature(CatchBlock.__init__)
    params = list(sig.parameters.keys())



def test_astm_variablecatchblock_is_not_abstract():
    assert not inspect.isabstract(astm_VariableCatchBlock)


def test_astm_variablecatchblock_constructor_exists():
    assert callable(astm_VariableCatchBlock.__init__)


def test_astm_variablecatchblock_constructor_args():
    sig = inspect.signature(astm_VariableCatchBlock.__init__)
    params = list(sig.parameters.keys())



def test_astm_typescatchblock_is_not_abstract():
    assert not inspect.isabstract(astm_TypesCatchBlock)


def test_astm_typescatchblock_constructor_exists():
    assert callable(astm_TypesCatchBlock.__init__)


def test_astm_typescatchblock_constructor_args():
    sig = inspect.signature(astm_TypesCatchBlock.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_astm_binaryexpression_is_not_abstract():
    assert not inspect.isabstract(astm_BinaryExpression)


def test_astm_binaryexpression_constructor_exists():
    assert callable(astm_BinaryExpression.__init__)


def test_astm_binaryexpression_constructor_args():
    sig = inspect.signature(astm_BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_astm_unaryexpression_is_not_abstract():
    assert not inspect.isabstract(astm_UnaryExpression)


def test_astm_unaryexpression_constructor_exists():
    assert callable(astm_UnaryExpression.__init__)


def test_astm_unaryexpression_constructor_args():
    sig = inspect.signature(astm_UnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_astm_newexpression_is_not_abstract():
    assert not inspect.isabstract(astm_NewExpression)


def test_astm_newexpression_constructor_exists():
    assert callable(astm_NewExpression.__init__)


def test_astm_newexpression_constructor_args():
    sig = inspect.signature(astm_NewExpression.__init__)
    params = list(sig.parameters.keys())



def test_astm_functioncallexpression_is_not_abstract():
    assert not inspect.isabstract(astm_FunctionCallExpression)


def test_astm_functioncallexpression_constructor_exists():
    assert callable(astm_FunctionCallExpression.__init__)


def test_astm_functioncallexpression_constructor_args():
    sig = inspect.signature(astm_FunctionCallExpression.__init__)
    params = list(sig.parameters.keys())



def test_astm_rangeexpression_is_not_abstract():
    assert not inspect.isabstract(astm_RangeExpression)


def test_astm_rangeexpression_constructor_exists():
    assert callable(astm_RangeExpression.__init__)


def test_astm_rangeexpression_constructor_args():
    sig = inspect.signature(astm_RangeExpression.__init__)
    params = list(sig.parameters.keys())



def test_astm_conditionalexpression_is_not_abstract():
    assert not inspect.isabstract(astm_ConditionalExpression)


def test_astm_conditionalexpression_constructor_exists():
    assert callable(astm_ConditionalExpression.__init__)


def test_astm_conditionalexpression_constructor_args():
    sig = inspect.signature(astm_ConditionalExpression.__init__)
    params = list(sig.parameters.keys())



def test_astm_literal_is_not_abstract():
    assert not inspect.isabstract(astm_Literal)


def test_astm_literal_constructor_exists():
    assert callable(astm_Literal.__init__)


def test_astm_literal_constructor_args():
    sig = inspect.signature(astm_Literal.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_astm_literal_has_value():
    assert hasattr(astm_Literal, "value")
    descriptor = None
    for klass in astm_Literal.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_astm_castexpression_is_not_abstract():
    assert not inspect.isabstract(astm_CastExpression)


def test_astm_castexpression_constructor_exists():
    assert callable(astm_CastExpression.__init__)


def test_astm_castexpression_constructor_args():
    sig = inspect.signature(astm_CastExpression.__init__)
    params = list(sig.parameters.keys())



def test_astm_aggregateexpression_is_not_abstract():
    assert not inspect.isabstract(astm_AggregateExpression)


def test_astm_aggregateexpression_constructor_exists():
    assert callable(astm_AggregateExpression.__init__)


def test_astm_aggregateexpression_constructor_args():
    sig = inspect.signature(astm_AggregateExpression.__init__)
    params = list(sig.parameters.keys())



def test_astm_arrayaccess_is_not_abstract():
    assert not inspect.isabstract(astm_ArrayAccess)


def test_astm_arrayaccess_constructor_exists():
    assert callable(astm_ArrayAccess.__init__)


def test_astm_arrayaccess_constructor_args():
    sig = inspect.signature(astm_ArrayAccess.__init__)
    params = list(sig.parameters.keys())



def test_astm_namereference_is_not_abstract():
    assert not inspect.isabstract(astm_NameReference)


def test_astm_namereference_constructor_exists():
    assert callable(astm_NameReference.__init__)


def test_astm_namereference_constructor_args():
    sig = inspect.signature(astm_NameReference.__init__)
    params = list(sig.parameters.keys())



def test_loopstatement_is_not_abstract():
    assert not inspect.isabstract(LoopStatement)


def test_loopstatement_constructor_exists():
    assert callable(LoopStatement.__init__)


def test_loopstatement_constructor_args():
    sig = inspect.signature(LoopStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm_whilestatement_is_not_abstract():
    assert not inspect.isabstract(astm_WhileStatement)


def test_astm_whilestatement_constructor_exists():
    assert callable(astm_WhileStatement.__init__)


def test_astm_whilestatement_constructor_args():
    sig = inspect.signature(astm_WhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm_dowhilestatement_is_not_abstract():
    assert not inspect.isabstract(astm_DoWhileStatement)


def test_astm_dowhilestatement_constructor_exists():
    assert callable(astm_DoWhileStatement.__init__)


def test_astm_dowhilestatement_constructor_args():
    sig = inspect.signature(astm_DoWhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm_forstatement_is_not_abstract():
    assert not inspect.isabstract(astm_ForStatement)


def test_astm_forstatement_constructor_exists():
    assert callable(astm_ForStatement.__init__)


def test_astm_forstatement_constructor_args():
    sig = inspect.signature(astm_ForStatement.__init__)
    params = list(sig.parameters.keys())



def test_switchcase_is_not_abstract():
    assert not inspect.isabstract(SwitchCase)


def test_switchcase_constructor_exists():
    assert callable(SwitchCase.__init__)


def test_switchcase_constructor_args():
    sig = inspect.signature(SwitchCase.__init__)
    params = list(sig.parameters.keys())



def test_astm_defaultblock_is_not_abstract():
    assert not inspect.isabstract(astm_DefaultBlock)


def test_astm_defaultblock_constructor_exists():
    assert callable(astm_DefaultBlock.__init__)


def test_astm_defaultblock_constructor_args():
    sig = inspect.signature(astm_DefaultBlock.__init__)
    params = list(sig.parameters.keys())



def test_astm_caseblock_is_not_abstract():
    assert not inspect.isabstract(astm_CaseBlock)


def test_astm_caseblock_constructor_exists():
    assert callable(astm_CaseBlock.__init__)


def test_astm_caseblock_constructor_args():
    sig = inspect.signature(astm_CaseBlock.__init__)
    params = list(sig.parameters.keys())



def test_astm_labelaccess_is_not_abstract():
    assert not inspect.isabstract(astm_LabelAccess)


def test_astm_labelaccess_constructor_exists():
    assert callable(astm_LabelAccess.__init__)


def test_astm_labelaccess_constructor_args():
    sig = inspect.signature(astm_LabelAccess.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_astm_ifstatement_is_not_abstract():
    assert not inspect.isabstract(astm_IfStatement)


def test_astm_ifstatement_constructor_exists():
    assert callable(astm_IfStatement.__init__)


def test_astm_ifstatement_constructor_args():
    sig = inspect.signature(astm_IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm_labeledstatement_is_not_abstract():
    assert not inspect.isabstract(astm_LabeledStatement)


def test_astm_labeledstatement_constructor_exists():
    assert callable(astm_LabeledStatement.__init__)


def test_astm_labeledstatement_constructor_args():
    sig = inspect.signature(astm_LabeledStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm_throwstatement_is_not_abstract():
    assert not inspect.isabstract(astm_ThrowStatement)


def test_astm_throwstatement_constructor_exists():
    assert callable(astm_ThrowStatement.__init__)


def test_astm_throwstatement_constructor_args():
    sig = inspect.signature(astm_ThrowStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm_loopstatement_is_not_abstract():
    assert not inspect.isabstract(astm_LoopStatement)


def test_astm_loopstatement_constructor_exists():
    assert callable(astm_LoopStatement.__init__)


def test_astm_loopstatement_constructor_args():
    sig = inspect.signature(astm_LoopStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm_jumpstatement_is_not_abstract():
    assert not inspect.isabstract(astm_JumpStatement)


def test_astm_jumpstatement_constructor_exists():
    assert callable(astm_JumpStatement.__init__)


def test_astm_jumpstatement_constructor_args():
    sig = inspect.signature(astm_JumpStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm_expressionstatement_is_not_abstract():
    assert not inspect.isabstract(astm_ExpressionStatement)


def test_astm_expressionstatement_constructor_exists():
    assert callable(astm_ExpressionStatement.__init__)


def test_astm_expressionstatement_constructor_args():
    sig = inspect.signature(astm_ExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm_switchstatement_is_not_abstract():
    assert not inspect.isabstract(astm_SwitchStatement)


def test_astm_switchstatement_constructor_exists():
    assert callable(astm_SwitchStatement.__init__)


def test_astm_switchstatement_constructor_args():
    sig = inspect.signature(astm_SwitchStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm_continuestatement_is_not_abstract():
    assert not inspect.isabstract(astm_ContinueStatement)


def test_astm_continuestatement_constructor_exists():
    assert callable(astm_ContinueStatement.__init__)


def test_astm_continuestatement_constructor_args():
    sig = inspect.signature(astm_ContinueStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm_declarationordefinitionstatement_is_not_abstract():
    assert not inspect.isabstract(astm_DeclarationOrDefinitionStatement)


def test_astm_declarationordefinitionstatement_constructor_exists():
    assert callable(astm_DeclarationOrDefinitionStatement.__init__)


def test_astm_declarationordefinitionstatement_constructor_args():
    sig = inspect.signature(astm_DeclarationOrDefinitionStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm_returnstatement_is_not_abstract():
    assert not inspect.isabstract(astm_ReturnStatement)


def test_astm_returnstatement_constructor_exists():
    assert callable(astm_ReturnStatement.__init__)


def test_astm_returnstatement_constructor_args():
    sig = inspect.signature(astm_ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm_specificselectstatement_is_not_abstract():
    assert not inspect.isabstract(astm_SpecificSelectStatement)


def test_astm_specificselectstatement_constructor_exists():
    assert callable(astm_SpecificSelectStatement.__init__)


def test_astm_specificselectstatement_constructor_args():
    sig = inspect.signature(astm_SpecificSelectStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm_emptystatement_is_not_abstract():
    assert not inspect.isabstract(astm_EmptyStatement)


def test_astm_emptystatement_constructor_exists():
    assert callable(astm_EmptyStatement.__init__)


def test_astm_emptystatement_constructor_args():
    sig = inspect.signature(astm_EmptyStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm_trystatement_is_not_abstract():
    assert not inspect.isabstract(astm_TryStatement)


def test_astm_trystatement_constructor_exists():
    assert callable(astm_TryStatement.__init__)


def test_astm_trystatement_constructor_args():
    sig = inspect.signature(astm_TryStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm_breakstatement_is_not_abstract():
    assert not inspect.isabstract(astm_BreakStatement)


def test_astm_breakstatement_constructor_exists():
    assert callable(astm_BreakStatement.__init__)


def test_astm_breakstatement_constructor_args():
    sig = inspect.signature(astm_BreakStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm_terminatestatement_is_not_abstract():
    assert not inspect.isabstract(astm_TerminateStatement)


def test_astm_terminatestatement_constructor_exists():
    assert callable(astm_TerminateStatement.__init__)


def test_astm_terminatestatement_constructor_args():
    sig = inspect.signature(astm_TerminateStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm_deletestatement_is_not_abstract():
    assert not inspect.isabstract(astm_DeleteStatement)


def test_astm_deletestatement_constructor_exists():
    assert callable(astm_DeleteStatement.__init__)


def test_astm_deletestatement_constructor_args():
    sig = inspect.signature(astm_DeleteStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm_blockscope_is_not_abstract():
    assert not inspect.isabstract(astm_BlockScope)


def test_astm_blockscope_constructor_exists():
    assert callable(astm_BlockScope.__init__)


def test_astm_blockscope_constructor_args():
    sig = inspect.signature(astm_BlockScope.__init__)
    params = list(sig.parameters.keys())



def test_typereference_is_not_abstract():
    assert not inspect.isabstract(TypeReference)


def test_typereference_constructor_exists():
    assert callable(TypeReference.__init__)


def test_typereference_constructor_args():
    sig = inspect.signature(TypeReference.__init__)
    params = list(sig.parameters.keys())



def test_astm_blockstatement_is_not_abstract():
    assert not inspect.isabstract(astm_BlockStatement)


def test_astm_blockstatement_constructor_exists():
    assert callable(astm_BlockStatement.__init__)


def test_astm_blockstatement_constructor_args():
    sig = inspect.signature(astm_BlockStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm_unnamedtypereference_is_not_abstract():
    assert not inspect.isabstract(astm_UnnamedTypeReference)


def test_astm_unnamedtypereference_constructor_exists():
    assert callable(astm_UnnamedTypeReference.__init__)


def test_astm_unnamedtypereference_constructor_args():
    sig = inspect.signature(astm_UnnamedTypeReference.__init__)
    params = list(sig.parameters.keys())



def test_aggregatetype_is_not_abstract():
    assert not inspect.isabstract(AggregateType)


def test_aggregatetype_constructor_exists():
    assert callable(AggregateType.__init__)


def test_aggregatetype_constructor_args():
    sig = inspect.signature(AggregateType.__init__)
    params = list(sig.parameters.keys())



def test_astm_structuretype_is_not_abstract():
    assert not inspect.isabstract(astm_StructureType)


def test_astm_structuretype_constructor_exists():
    assert callable(astm_StructureType.__init__)


def test_astm_structuretype_constructor_args():
    sig = inspect.signature(astm_StructureType.__init__)
    params = list(sig.parameters.keys())



def test_astm_annotationtype_is_not_abstract():
    assert not inspect.isabstract(astm_AnnotationType)


def test_astm_annotationtype_constructor_exists():
    assert callable(astm_AnnotationType.__init__)


def test_astm_annotationtype_constructor_args():
    sig = inspect.signature(astm_AnnotationType.__init__)
    params = list(sig.parameters.keys())



def test_astm_uniontype_is_not_abstract():
    assert not inspect.isabstract(astm_UnionType)


def test_astm_uniontype_constructor_exists():
    assert callable(astm_UnionType.__init__)


def test_astm_uniontype_constructor_args():
    sig = inspect.signature(astm_UnionType.__init__)
    params = list(sig.parameters.keys())



def test_astm_classtype_is_not_abstract():
    assert not inspect.isabstract(astm_ClassType)


def test_astm_classtype_constructor_exists():
    assert callable(astm_ClassType.__init__)


def test_astm_classtype_constructor_args():
    sig = inspect.signature(astm_ClassType.__init__)
    params = list(sig.parameters.keys())



def test_datatype_is_not_abstract():
    assert not inspect.isabstract(DataType)


def test_datatype_constructor_exists():
    assert callable(DataType.__init__)


def test_datatype_constructor_args():
    sig = inspect.signature(DataType.__init__)
    params = list(sig.parameters.keys())



def test_astm_exceptiontype_is_not_abstract():
    assert not inspect.isabstract(astm_ExceptionType)


def test_astm_exceptiontype_constructor_exists():
    assert callable(astm_ExceptionType.__init__)


def test_astm_exceptiontype_constructor_args():
    sig = inspect.signature(astm_ExceptionType.__init__)
    params = list(sig.parameters.keys())



def test_astm_enumtype_is_not_abstract():
    assert not inspect.isabstract(astm_EnumType)


def test_astm_enumtype_constructor_exists():
    assert callable(astm_EnumType.__init__)


def test_astm_enumtype_constructor_args():
    sig = inspect.signature(astm_EnumType.__init__)
    params = list(sig.parameters.keys())



def test_astm_constructedtype_is_not_abstract():
    assert not inspect.isabstract(astm_ConstructedType)


def test_astm_constructedtype_constructor_exists():
    assert callable(astm_ConstructedType.__init__)


def test_astm_constructedtype_constructor_args():
    sig = inspect.signature(astm_ConstructedType.__init__)
    params = list(sig.parameters.keys())



def test_astm_primitivetype_is_not_abstract():
    assert not inspect.isabstract(astm_PrimitiveType)


def test_astm_primitivetype_constructor_exists():
    assert callable(astm_PrimitiveType.__init__)


def test_astm_primitivetype_constructor_args():
    sig = inspect.signature(astm_PrimitiveType.__init__)
    params = list(sig.parameters.keys())
    assert "isSigned" in params, "Missing parameter 'isSigned'"

def test_astm_primitivetype_has_isSigned():
    assert hasattr(astm_PrimitiveType, "isSigned")
    descriptor = None
    for klass in astm_PrimitiveType.__mro__:
        if "isSigned" in klass.__dict__:
            descriptor = klass.__dict__["isSigned"]
            break
    assert isinstance(descriptor, property)



def test_astm_formalparametertype_is_not_abstract():
    assert not inspect.isabstract(astm_FormalParameterType)


def test_astm_formalparametertype_constructor_exists():
    assert callable(astm_FormalParameterType.__init__)


def test_astm_formalparametertype_constructor_args():
    sig = inspect.signature(astm_FormalParameterType.__init__)
    params = list(sig.parameters.keys())



def test_constructedtype_is_not_abstract():
    assert not inspect.isabstract(ConstructedType)


def test_constructedtype_constructor_exists():
    assert callable(ConstructedType.__init__)


def test_constructedtype_constructor_args():
    sig = inspect.signature(ConstructedType.__init__)
    params = list(sig.parameters.keys())



def test_astm_rangetype_is_not_abstract():
    assert not inspect.isabstract(astm_RangeType)


def test_astm_rangetype_constructor_exists():
    assert callable(astm_RangeType.__init__)


def test_astm_rangetype_constructor_args():
    sig = inspect.signature(astm_RangeType.__init__)
    params = list(sig.parameters.keys())



def test_astm_collectiontype_is_not_abstract():
    assert not inspect.isabstract(astm_CollectionType)


def test_astm_collectiontype_constructor_exists():
    assert callable(astm_CollectionType.__init__)


def test_astm_collectiontype_constructor_args():
    sig = inspect.signature(astm_CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_astm_pointertype_is_not_abstract():
    assert not inspect.isabstract(astm_PointerType)


def test_astm_pointertype_constructor_exists():
    assert callable(astm_PointerType.__init__)


def test_astm_pointertype_constructor_args():
    sig = inspect.signature(astm_PointerType.__init__)
    params = list(sig.parameters.keys())



def test_astm_referencetype_is_not_abstract():
    assert not inspect.isabstract(astm_ReferenceType)


def test_astm_referencetype_constructor_exists():
    assert callable(astm_ReferenceType.__init__)


def test_astm_referencetype_constructor_args():
    sig = inspect.signature(astm_ReferenceType.__init__)
    params = list(sig.parameters.keys())



def test_astm_arraytype_is_not_abstract():
    assert not inspect.isabstract(astm_ArrayType)


def test_astm_arraytype_constructor_exists():
    assert callable(astm_ArrayType.__init__)


def test_astm_arraytype_constructor_args():
    sig = inspect.signature(astm_ArrayType.__init__)
    params = list(sig.parameters.keys())



def test_astm_aggregatescope_is_not_abstract():
    assert not inspect.isabstract(astm_AggregateScope)


def test_astm_aggregatescope_constructor_exists():
    assert callable(astm_AggregateScope.__init__)


def test_astm_aggregatescope_constructor_args():
    sig = inspect.signature(astm_AggregateScope.__init__)
    params = list(sig.parameters.keys())



def test_preprocessorelement_is_not_abstract():
    assert not inspect.isabstract(PreprocessorElement)


def test_preprocessorelement_constructor_exists():
    assert callable(PreprocessorElement.__init__)


def test_preprocessorelement_constructor_args():
    sig = inspect.signature(PreprocessorElement.__init__)
    params = list(sig.parameters.keys())



def test_astm_macrodefinition_is_not_abstract():
    assert not inspect.isabstract(astm_MacroDefinition)


def test_astm_macrodefinition_constructor_exists():
    assert callable(astm_MacroDefinition.__init__)


def test_astm_macrodefinition_constructor_args():
    sig = inspect.signature(astm_MacroDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"
    assert "macroName" in params, "Missing parameter 'macroName'"

def test_astm_macrodefinition_has_body():
    assert hasattr(astm_MacroDefinition, "body")
    descriptor = None
    for klass in astm_MacroDefinition.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)

def test_astm_macrodefinition_has_macroName():
    assert hasattr(astm_MacroDefinition, "macroName")
    descriptor = None
    for klass in astm_MacroDefinition.__mro__:
        if "macroName" in klass.__dict__:
            descriptor = klass.__dict__["macroName"]
            break
    assert isinstance(descriptor, property)



def test_astm_macrocall_is_not_abstract():
    assert not inspect.isabstract(astm_MacroCall)


def test_astm_macrocall_constructor_exists():
    assert callable(astm_MacroCall.__init__)


def test_astm_macrocall_constructor_args():
    sig = inspect.signature(astm_MacroCall.__init__)
    params = list(sig.parameters.keys())



def test_astm_includeunit_is_not_abstract():
    assert not inspect.isabstract(astm_IncludeUnit)


def test_astm_includeunit_constructor_exists():
    assert callable(astm_IncludeUnit.__init__)


def test_astm_includeunit_constructor_args():
    sig = inspect.signature(astm_IncludeUnit.__init__)
    params = list(sig.parameters.keys())



def test_astm_comment_is_not_abstract():
    assert not inspect.isabstract(astm_Comment)


def test_astm_comment_constructor_exists():
    assert callable(astm_Comment.__init__)


def test_astm_comment_constructor_args():
    sig = inspect.signature(astm_Comment.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_astm_comment_has_text():
    assert hasattr(astm_Comment, "text")
    descriptor = None
    for klass in astm_Comment.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_astm_aggregatetype_is_not_abstract():
    assert not inspect.isabstract(astm_AggregateType)


def test_astm_aggregatetype_constructor_exists():
    assert callable(astm_AggregateType.__init__)


def test_astm_aggregatetype_constructor_args():
    sig = inspect.signature(astm_AggregateType.__init__)
    params = list(sig.parameters.keys())



def test_astm_namedtype_is_not_abstract():
    assert not inspect.isabstract(astm_NamedType)


def test_astm_namedtype_constructor_exists():
    assert callable(astm_NamedType.__init__)


def test_astm_namedtype_constructor_args():
    sig = inspect.signature(astm_NamedType.__init__)
    params = list(sig.parameters.keys())



def test_typedefinition_is_not_abstract():
    assert not inspect.isabstract(TypeDefinition)


def test_typedefinition_constructor_exists():
    assert callable(TypeDefinition.__init__)


def test_typedefinition_constructor_args():
    sig = inspect.signature(TypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_astm_aggregatetypedefinition_is_not_abstract():
    assert not inspect.isabstract(astm_AggregateTypeDefinition)


def test_astm_aggregatetypedefinition_constructor_exists():
    assert callable(astm_AggregateTypeDefinition.__init__)


def test_astm_aggregatetypedefinition_constructor_args():
    sig = inspect.signature(astm_AggregateTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_astm_namedtypedefinition_is_not_abstract():
    assert not inspect.isabstract(astm_NamedTypeDefinition)


def test_astm_namedtypedefinition_constructor_exists():
    assert callable(astm_NamedTypeDefinition.__init__)


def test_astm_namedtypedefinition_constructor_args():
    sig = inspect.signature(astm_NamedTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_astm_functionscope_is_not_abstract():
    assert not inspect.isabstract(astm_FunctionScope)


def test_astm_functionscope_constructor_exists():
    assert callable(astm_FunctionScope.__init__)


def test_astm_functionscope_constructor_args():
    sig = inspect.signature(astm_FunctionScope.__init__)
    params = list(sig.parameters.keys())



def test_definition_is_not_abstract():
    assert not inspect.isabstract(Definition)


def test_definition_constructor_exists():
    assert callable(Definition.__init__)


def test_definition_constructor_args():
    sig = inspect.signature(Definition.__init__)
    params = list(sig.parameters.keys())



def test_astm_specifictriggerdefinition_is_not_abstract():
    assert not inspect.isabstract(astm_SpecificTriggerDefinition)


def test_astm_specifictriggerdefinition_constructor_exists():
    assert callable(astm_SpecificTriggerDefinition.__init__)


def test_astm_specifictriggerdefinition_constructor_args():
    sig = inspect.signature(astm_SpecificTriggerDefinition.__init__)
    params = list(sig.parameters.keys())



def test_astm_functiondefinition_is_not_abstract():
    assert not inspect.isabstract(astm_FunctionDefinition)


def test_astm_functiondefinition_constructor_exists():
    assert callable(astm_FunctionDefinition.__init__)


def test_astm_functiondefinition_constructor_args():
    sig = inspect.signature(astm_FunctionDefinition.__init__)
    params = list(sig.parameters.keys())



def test_declaration_is_not_abstract():
    assert not inspect.isabstract(Declaration)


def test_declaration_constructor_exists():
    assert callable(Declaration.__init__)


def test_declaration_constructor_args():
    sig = inspect.signature(Declaration.__init__)
    params = list(sig.parameters.keys())



def test_astm_formalparameterdeclaration_is_not_abstract():
    assert not inspect.isabstract(astm_FormalParameterDeclaration)


def test_astm_formalparameterdeclaration_constructor_exists():
    assert callable(astm_FormalParameterDeclaration.__init__)


def test_astm_formalparameterdeclaration_constructor_args():
    sig = inspect.signature(astm_FormalParameterDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_astm_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(astm_VariableDeclaration)


def test_astm_variabledeclaration_constructor_exists():
    assert callable(astm_VariableDeclaration.__init__)


def test_astm_variabledeclaration_constructor_args():
    sig = inspect.signature(astm_VariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "isMutable" in params, "Missing parameter 'isMutable'"

def test_astm_variabledeclaration_has_isMutable():
    assert hasattr(astm_VariableDeclaration, "isMutable")
    descriptor = None
    for klass in astm_VariableDeclaration.__mro__:
        if "isMutable" in klass.__dict__:
            descriptor = klass.__dict__["isMutable"]
            break
    assert isinstance(descriptor, property)



def test_astm_functiondeclaration_is_not_abstract():
    assert not inspect.isabstract(astm_FunctionDeclaration)


def test_astm_functiondeclaration_constructor_exists():
    assert callable(astm_FunctionDeclaration.__init__)


def test_astm_functiondeclaration_constructor_args():
    sig = inspect.signature(astm_FunctionDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_astm_enumliteraldefinition_is_not_abstract():
    assert not inspect.isabstract(astm_EnumLiteralDefinition)


def test_astm_enumliteraldefinition_constructor_exists():
    assert callable(astm_EnumLiteralDefinition.__init__)


def test_astm_enumliteraldefinition_constructor_args():
    sig = inspect.signature(astm_EnumLiteralDefinition.__init__)
    params = list(sig.parameters.keys())



def test_datadefinition_is_not_abstract():
    assert not inspect.isabstract(DataDefinition)


def test_datadefinition_constructor_exists():
    assert callable(DataDefinition.__init__)


def test_datadefinition_constructor_args():
    sig = inspect.signature(DataDefinition.__init__)
    params = list(sig.parameters.keys())



def test_astm_formalparameterdefinition_is_not_abstract():
    assert not inspect.isabstract(astm_FormalParameterDefinition)


def test_astm_formalparameterdefinition_constructor_exists():
    assert callable(astm_FormalParameterDefinition.__init__)


def test_astm_formalparameterdefinition_constructor_args():
    sig = inspect.signature(astm_FormalParameterDefinition.__init__)
    params = list(sig.parameters.keys())



def test_astm_variabledefinition_is_not_abstract():
    assert not inspect.isabstract(astm_VariableDefinition)


def test_astm_variabledefinition_constructor_exists():
    assert callable(astm_VariableDefinition.__init__)


def test_astm_variabledefinition_constructor_args():
    sig = inspect.signature(astm_VariableDefinition.__init__)
    params = list(sig.parameters.keys())



def test_astm_bitfielddefinition_is_not_abstract():
    assert not inspect.isabstract(astm_BitFieldDefinition)


def test_astm_bitfielddefinition_constructor_exists():
    assert callable(astm_BitFieldDefinition.__init__)


def test_astm_bitfielddefinition_constructor_args():
    sig = inspect.signature(astm_BitFieldDefinition.__init__)
    params = list(sig.parameters.keys())



def test_astm_datadefinition_is_not_abstract():
    assert not inspect.isabstract(astm_DataDefinition)


def test_astm_datadefinition_constructor_exists():
    assert callable(astm_DataDefinition.__init__)


def test_astm_datadefinition_constructor_args():
    sig = inspect.signature(astm_DataDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "isMutable" in params, "Missing parameter 'isMutable'"

def test_astm_datadefinition_has_isMutable():
    assert hasattr(astm_DataDefinition, "isMutable")
    descriptor = None
    for klass in astm_DataDefinition.__mro__:
        if "isMutable" in klass.__dict__:
            descriptor = klass.__dict__["isMutable"]
            break
    assert isinstance(descriptor, property)



def test_astm_entrydefinition_is_not_abstract():
    assert not inspect.isabstract(astm_EntryDefinition)


def test_astm_entrydefinition_constructor_exists():
    assert callable(astm_EntryDefinition.__init__)


def test_astm_entrydefinition_constructor_args():
    sig = inspect.signature(astm_EntryDefinition.__init__)
    params = list(sig.parameters.keys())



def test_definitionobject_is_not_abstract():
    assert not inspect.isabstract(DefinitionObject)


def test_definitionobject_constructor_exists():
    assert callable(DefinitionObject.__init__)


def test_definitionobject_constructor_args():
    sig = inspect.signature(DefinitionObject.__init__)
    params = list(sig.parameters.keys())



def test_astm_typedefinition_is_not_abstract():
    assert not inspect.isabstract(astm_TypeDefinition)


def test_astm_typedefinition_constructor_exists():
    assert callable(astm_TypeDefinition.__init__)


def test_astm_typedefinition_constructor_args():
    sig = inspect.signature(astm_TypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_astm_namespacedefinition_is_not_abstract():
    assert not inspect.isabstract(astm_NameSpaceDefinition)


def test_astm_namespacedefinition_constructor_exists():
    assert callable(astm_NameSpaceDefinition.__init__)


def test_astm_namespacedefinition_constructor_args():
    sig = inspect.signature(astm_NameSpaceDefinition.__init__)
    params = list(sig.parameters.keys())



def test_astm_labeldefinition_is_not_abstract():
    assert not inspect.isabstract(astm_LabelDefinition)


def test_astm_labeldefinition_constructor_exists():
    assert callable(astm_LabelDefinition.__init__)


def test_astm_labeldefinition_constructor_args():
    sig = inspect.signature(astm_LabelDefinition.__init__)
    params = list(sig.parameters.keys())



def test_astm_declarationordefinition_is_not_abstract():
    assert not inspect.isabstract(astm_DeclarationOrDefinition)


def test_astm_declarationordefinition_constructor_exists():
    assert callable(astm_DeclarationOrDefinition.__init__)


def test_astm_declarationordefinition_constructor_args():
    sig = inspect.signature(astm_DeclarationOrDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "isRegister" in params, "Missing parameter 'isRegister'"
    assert "linkageSpecifier" in params, "Missing parameter 'linkageSpecifier'"

def test_astm_declarationordefinition_has_isRegister():
    assert hasattr(astm_DeclarationOrDefinition, "isRegister")
    descriptor = None
    for klass in astm_DeclarationOrDefinition.__mro__:
        if "isRegister" in klass.__dict__:
            descriptor = klass.__dict__["isRegister"]
            break
    assert isinstance(descriptor, property)

def test_astm_declarationordefinition_has_linkageSpecifier():
    assert hasattr(astm_DeclarationOrDefinition, "linkageSpecifier")
    descriptor = None
    for klass in astm_DeclarationOrDefinition.__mro__:
        if "linkageSpecifier" in klass.__dict__:
            descriptor = klass.__dict__["linkageSpecifier"]
            break
    assert isinstance(descriptor, property)



def test_astm_programscope_is_not_abstract():
    assert not inspect.isabstract(astm_ProgramScope)


def test_astm_programscope_constructor_exists():
    assert callable(astm_ProgramScope.__init__)


def test_astm_programscope_constructor_args():
    sig = inspect.signature(astm_ProgramScope.__init__)
    params = list(sig.parameters.keys())



def test_othersyntaxobject_is_not_abstract():
    assert not inspect.isabstract(OtherSyntaxObject)


def test_othersyntaxobject_constructor_exists():
    assert callable(OtherSyntaxObject.__init__)


def test_othersyntaxobject_constructor_args():
    sig = inspect.signature(OtherSyntaxObject.__init__)
    params = list(sig.parameters.keys())



def test_astm_switchcase_is_not_abstract():
    assert not inspect.isabstract(astm_SwitchCase)


def test_astm_switchcase_constructor_exists():
    assert callable(astm_SwitchCase.__init__)


def test_astm_switchcase_constructor_args():
    sig = inspect.signature(astm_SwitchCase.__init__)
    params = list(sig.parameters.keys())



def test_astm_functionmemberattribute_is_not_abstract():
    assert not inspect.isabstract(astm_FunctionMemberAttribute)


def test_astm_functionmemberattribute_constructor_exists():
    assert callable(astm_FunctionMemberAttribute.__init__)


def test_astm_functionmemberattribute_constructor_args():
    sig = inspect.signature(astm_FunctionMemberAttribute.__init__)
    params = list(sig.parameters.keys())



def test_astm_operator_is_not_abstract():
    assert not inspect.isabstract(astm_Operator)


def test_astm_operator_constructor_exists():
    assert callable(astm_Operator.__init__)


def test_astm_operator_constructor_args():
    sig = inspect.signature(astm_Operator.__init__)
    params = list(sig.parameters.keys())



def test_astm_catchblock_is_not_abstract():
    assert not inspect.isabstract(astm_CatchBlock)


def test_astm_catchblock_constructor_exists():
    assert callable(astm_CatchBlock.__init__)


def test_astm_catchblock_constructor_args():
    sig = inspect.signature(astm_CatchBlock.__init__)
    params = list(sig.parameters.keys())



def test_astm_virtualspecification_is_not_abstract():
    assert not inspect.isabstract(astm_VirtualSpecification)


def test_astm_virtualspecification_constructor_exists():
    assert callable(astm_VirtualSpecification.__init__)


def test_astm_virtualspecification_constructor_args():
    sig = inspect.signature(astm_VirtualSpecification.__init__)
    params = list(sig.parameters.keys())



def test_astm_dimension_is_not_abstract():
    assert not inspect.isabstract(astm_Dimension)


def test_astm_dimension_constructor_exists():
    assert callable(astm_Dimension.__init__)


def test_astm_dimension_constructor_args():
    sig = inspect.signature(astm_Dimension.__init__)
    params = list(sig.parameters.keys())



def test_astm_derivesfrom_is_not_abstract():
    assert not inspect.isabstract(astm_DerivesFrom)


def test_astm_derivesfrom_constructor_exists():
    assert callable(astm_DerivesFrom.__init__)


def test_astm_derivesfrom_constructor_args():
    sig = inspect.signature(astm_DerivesFrom.__init__)
    params = list(sig.parameters.keys())
    assert "isVirtual" in params, "Missing parameter 'isVirtual'"

def test_astm_derivesfrom_has_isVirtual():
    assert hasattr(astm_DerivesFrom, "isVirtual")
    descriptor = None
    for klass in astm_DerivesFrom.__mro__:
        if "isVirtual" in klass.__dict__:
            descriptor = klass.__dict__["isVirtual"]
            break
    assert isinstance(descriptor, property)



def test_astm_annotationexpression_is_not_abstract():
    assert not inspect.isabstract(astm_AnnotationExpression)


def test_astm_annotationexpression_constructor_exists():
    assert callable(astm_AnnotationExpression.__init__)


def test_astm_annotationexpression_constructor_args():
    sig = inspect.signature(astm_AnnotationExpression.__init__)
    params = list(sig.parameters.keys())



def test_gastmobject_is_not_abstract():
    assert not inspect.isabstract(GASTMObject)


def test_gastmobject_constructor_exists():
    assert callable(GASTMObject.__init__)


def test_gastmobject_constructor_args():
    sig = inspect.signature(GASTMObject.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastmsyntaxobject_is_not_abstract():
    assert not inspect.isabstract(astm_GASTMSyntaxObject)


def test_astm_gastmsyntaxobject_constructor_exists():
    assert callable(astm_GASTMSyntaxObject.__init__)


def test_astm_gastmsyntaxobject_constructor_args():
    sig = inspect.signature(astm_GASTMSyntaxObject.__init__)
    params = list(sig.parameters.keys())



def test_declarationordefinition_is_not_abstract():
    assert not inspect.isabstract(DeclarationOrDefinition)


def test_declarationordefinition_constructor_exists():
    assert callable(DeclarationOrDefinition.__init__)


def test_declarationordefinition_constructor_args():
    sig = inspect.signature(DeclarationOrDefinition.__init__)
    params = list(sig.parameters.keys())



def test_astm_declaration_is_not_abstract():
    assert not inspect.isabstract(astm_Declaration)


def test_astm_declaration_constructor_exists():
    assert callable(astm_Declaration.__init__)


def test_astm_declaration_constructor_args():
    sig = inspect.signature(astm_Declaration.__init__)
    params = list(sig.parameters.keys())



def test_astm_definition_is_not_abstract():
    assert not inspect.isabstract(astm_Definition)


def test_astm_definition_constructor_exists():
    assert callable(astm_Definition.__init__)


def test_astm_definition_constructor_args():
    sig = inspect.signature(astm_Definition.__init__)
    params = list(sig.parameters.keys())



def test_gastmsourceobject_is_not_abstract():
    assert not inspect.isabstract(GASTMSourceObject)


def test_gastmsourceobject_constructor_exists():
    assert callable(GASTMSourceObject.__init__)


def test_gastmsourceobject_constructor_args():
    sig = inspect.signature(GASTMSourceObject.__init__)
    params = list(sig.parameters.keys())



def test_astm_sourcefile_is_not_abstract():
    assert not inspect.isabstract(astm_SourceFile)


def test_astm_sourcefile_constructor_exists():
    assert callable(astm_SourceFile.__init__)


def test_astm_sourcefile_constructor_args():
    sig = inspect.signature(astm_SourceFile.__init__)
    params = list(sig.parameters.keys())
    assert "pathName" in params, "Missing parameter 'pathName'"

def test_astm_sourcefile_has_pathName():
    assert hasattr(astm_SourceFile, "pathName")
    descriptor = None
    for klass in astm_SourceFile.__mro__:
        if "pathName" in klass.__dict__:
            descriptor = klass.__dict__["pathName"]
            break
    assert isinstance(descriptor, property)



def test_operator_is_not_abstract():
    assert not inspect.isabstract(Operator)


def test_operator_constructor_exists():
    assert callable(Operator.__init__)


def test_operator_constructor_args():
    sig = inspect.signature(Operator.__init__)
    params = list(sig.parameters.keys())



def test_astm_binaryoperator_is_not_abstract():
    assert not inspect.isabstract(astm_BinaryOperator)


def test_astm_binaryoperator_constructor_exists():
    assert callable(astm_BinaryOperator.__init__)


def test_astm_binaryoperator_constructor_args():
    sig = inspect.signature(astm_BinaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_astm_unaryoperator_is_not_abstract():
    assert not inspect.isabstract(astm_UnaryOperator)


def test_astm_unaryoperator_constructor_exists():
    assert callable(astm_UnaryOperator.__init__)


def test_astm_unaryoperator_constructor_args():
    sig = inspect.signature(astm_UnaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_astm_labeltype_is_not_abstract():
    assert not inspect.isabstract(astm_LabelType)


def test_astm_labeltype_constructor_exists():
    assert callable(astm_LabelType.__init__)


def test_astm_labeltype_constructor_args():
    sig = inspect.signature(astm_LabelType.__init__)
    params = list(sig.parameters.keys())



def test_astm_typereference_is_not_abstract():
    assert not inspect.isabstract(astm_TypeReference)


def test_astm_typereference_constructor_exists():
    assert callable(astm_TypeReference.__init__)


def test_astm_typereference_constructor_args():
    sig = inspect.signature(astm_TypeReference.__init__)
    params = list(sig.parameters.keys())



def test_astm_namespacetype_is_not_abstract():
    assert not inspect.isabstract(astm_NameSpaceType)


def test_astm_namespacetype_constructor_exists():
    assert callable(astm_NameSpaceType.__init__)


def test_astm_namespacetype_constructor_args():
    sig = inspect.signature(astm_NameSpaceType.__init__)
    params = list(sig.parameters.keys())



def test_astm_functiontype_is_not_abstract():
    assert not inspect.isabstract(astm_FunctionType)


def test_astm_functiontype_constructor_exists():
    assert callable(astm_FunctionType.__init__)


def test_astm_functiontype_constructor_args():
    sig = inspect.signature(astm_FunctionType.__init__)
    params = list(sig.parameters.keys())



def test_astm_datatype_is_not_abstract():
    assert not inspect.isabstract(astm_DataType)


def test_astm_datatype_constructor_exists():
    assert callable(astm_DataType.__init__)


def test_astm_datatype_constructor_args():
    sig = inspect.signature(astm_DataType.__init__)
    params = list(sig.parameters.keys())



def test_gastmsyntaxobject_is_not_abstract():
    assert not inspect.isabstract(GASTMSyntaxObject)


def test_gastmsyntaxobject_constructor_exists():
    assert callable(GASTMSyntaxObject.__init__)


def test_gastmsyntaxobject_constructor_args():
    sig = inspect.signature(GASTMSyntaxObject.__init__)
    params = list(sig.parameters.keys())



def test_astm_statement_is_not_abstract():
    assert not inspect.isabstract(astm_Statement)


def test_astm_statement_constructor_exists():
    assert callable(astm_Statement.__init__)


def test_astm_statement_constructor_args():
    sig = inspect.signature(astm_Statement.__init__)
    params = list(sig.parameters.keys())



def test_astm_expression_is_not_abstract():
    assert not inspect.isabstract(astm_Expression)


def test_astm_expression_constructor_exists():
    assert callable(astm_Expression.__init__)


def test_astm_expression_constructor_args():
    sig = inspect.signature(astm_Expression.__init__)
    params = list(sig.parameters.keys())



def test_astm_preprocessorelement_is_not_abstract():
    assert not inspect.isabstract(astm_PreprocessorElement)


def test_astm_preprocessorelement_constructor_exists():
    assert callable(astm_PreprocessorElement.__init__)


def test_astm_preprocessorelement_constructor_args():
    sig = inspect.signature(astm_PreprocessorElement.__init__)
    params = list(sig.parameters.keys())



def test_astm_type_is_not_abstract():
    assert not inspect.isabstract(astm_Type)


def test_astm_type_constructor_exists():
    assert callable(astm_Type.__init__)


def test_astm_type_constructor_args():
    sig = inspect.signature(astm_Type.__init__)
    params = list(sig.parameters.keys())
    assert "isConst" in params, "Missing parameter 'isConst'"
    assert "isVolatile" in params, "Missing parameter 'isVolatile'"

def test_astm_type_has_isConst():
    assert hasattr(astm_Type, "isConst")
    descriptor = None
    for klass in astm_Type.__mro__:
        if "isConst" in klass.__dict__:
            descriptor = klass.__dict__["isConst"]
            break
    assert isinstance(descriptor, property)

def test_astm_type_has_isVolatile():
    assert hasattr(astm_Type, "isVolatile")
    descriptor = None
    for klass in astm_Type.__mro__:
        if "isVolatile" in klass.__dict__:
            descriptor = klass.__dict__["isVolatile"]
            break
    assert isinstance(descriptor, property)



def test_astm_othersyntaxobject_is_not_abstract():
    assert not inspect.isabstract(astm_OtherSyntaxObject)


def test_astm_othersyntaxobject_constructor_exists():
    assert callable(astm_OtherSyntaxObject.__init__)


def test_astm_othersyntaxobject_constructor_args():
    sig = inspect.signature(astm_OtherSyntaxObject.__init__)
    params = list(sig.parameters.keys())



def test_visitable_is_not_abstract():
    assert not inspect.isabstract(Visitable)


def test_visitable_constructor_exists():
    assert callable(Visitable.__init__)


def test_visitable_constructor_args():
    sig = inspect.signature(Visitable.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastmsemanticobject_is_not_abstract():
    assert not inspect.isabstract(astm_GASTMSemanticObject)


def test_astm_gastmsemanticobject_constructor_exists():
    assert callable(astm_GASTMSemanticObject.__init__)


def test_astm_gastmsemanticobject_constructor_args():
    sig = inspect.signature(astm_GASTMSemanticObject.__init__)
    params = list(sig.parameters.keys())



def test_astm_storagespecification_is_not_abstract():
    assert not inspect.isabstract(astm_StorageSpecification)


def test_astm_storagespecification_constructor_exists():
    assert callable(astm_StorageSpecification.__init__)


def test_astm_storagespecification_constructor_args():
    sig = inspect.signature(astm_StorageSpecification.__init__)
    params = list(sig.parameters.keys())



def test_astm_actualparameter_is_not_abstract():
    assert not inspect.isabstract(astm_ActualParameter)


def test_astm_actualparameter_constructor_exists():
    assert callable(astm_ActualParameter.__init__)


def test_astm_actualparameter_constructor_args():
    sig = inspect.signature(astm_ActualParameter.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastmsourceobject_is_not_abstract():
    assert not inspect.isabstract(astm_GASTMSourceObject)


def test_astm_gastmsourceobject_constructor_exists():
    assert callable(astm_GASTMSourceObject.__init__)


def test_astm_gastmsourceobject_constructor_args():
    sig = inspect.signature(astm_GASTMSourceObject.__init__)
    params = list(sig.parameters.keys())



def test_astm_functionmemberattributes_is_not_abstract():
    assert not inspect.isabstract(astm_FunctionMemberAttributes)


def test_astm_functionmemberattributes_constructor_exists():
    assert callable(astm_FunctionMemberAttributes.__init__)


def test_astm_functionmemberattributes_constructor_args():
    sig = inspect.signature(astm_FunctionMemberAttributes.__init__)
    params = list(sig.parameters.keys())
    assert "isFriend" in params, "Missing parameter 'isFriend'"
    assert "isThisConst" in params, "Missing parameter 'isThisConst'"
    assert "isInline" in params, "Missing parameter 'isInline'"

def test_astm_functionmemberattributes_has_isFriend():
    assert hasattr(astm_FunctionMemberAttributes, "isFriend")
    descriptor = None
    for klass in astm_FunctionMemberAttributes.__mro__:
        if "isFriend" in klass.__dict__:
            descriptor = klass.__dict__["isFriend"]
            break
    assert isinstance(descriptor, property)

def test_astm_functionmemberattributes_has_isThisConst():
    assert hasattr(astm_FunctionMemberAttributes, "isThisConst")
    descriptor = None
    for klass in astm_FunctionMemberAttributes.__mro__:
        if "isThisConst" in klass.__dict__:
            descriptor = klass.__dict__["isThisConst"]
            break
    assert isinstance(descriptor, property)

def test_astm_functionmemberattributes_has_isInline():
    assert hasattr(astm_FunctionMemberAttributes, "isInline")
    descriptor = None
    for klass in astm_FunctionMemberAttributes.__mro__:
        if "isInline" in klass.__dict__:
            descriptor = klass.__dict__["isInline"]
            break
    assert isinstance(descriptor, property)



def test_astm_accesskind_is_not_abstract():
    assert not inspect.isabstract(astm_AccessKind)


def test_astm_accesskind_constructor_exists():
    assert callable(astm_AccessKind.__init__)


def test_astm_accesskind_constructor_args():
    sig = inspect.signature(astm_AccessKind.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastmobject_is_not_abstract():
    assert not inspect.isabstract(astm_GASTMObject)


def test_astm_gastmobject_constructor_exists():
    assert callable(astm_GASTMObject.__init__)


def test_astm_gastmobject_constructor_args():
    sig = inspect.signature(astm_GASTMObject.__init__)
    params = list(sig.parameters.keys())



def test_functioncallexpression_is_not_abstract():
    assert not inspect.isabstract(FunctionCallExpression)


def test_functioncallexpression_constructor_exists():
    assert callable(FunctionCallExpression.__init__)


def test_functioncallexpression_constructor_args():
    sig = inspect.signature(FunctionCallExpression.__init__)
    params = list(sig.parameters.keys())



def test_astm_delphifunctioncallexpression_is_not_abstract():
    assert not inspect.isabstract(astm_DelphiFunctionCallExpression)


def test_astm_delphifunctioncallexpression_constructor_exists():
    assert callable(astm_DelphiFunctionCallExpression.__init__)


def test_astm_delphifunctioncallexpression_constructor_args():
    sig = inspect.signature(astm_DelphiFunctionCallExpression.__init__)
    params = list(sig.parameters.keys())



def test_astm_definitionobject_is_not_abstract():
    assert not inspect.isabstract(astm_DefinitionObject)


def test_astm_definitionobject_constructor_exists():
    assert callable(astm_DefinitionObject.__init__)


def test_astm_definitionobject_constructor_args():
    sig = inspect.signature(astm_DefinitionObject.__init__)
    params = list(sig.parameters.keys())



def test_astm_globalscope_is_not_abstract():
    assert not inspect.isabstract(astm_GlobalScope)


def test_astm_globalscope_constructor_exists():
    assert callable(astm_GlobalScope.__init__)


def test_astm_globalscope_constructor_args():
    sig = inspect.signature(astm_GlobalScope.__init__)
    params = list(sig.parameters.keys())



def test_astm_compilationunit_is_not_abstract():
    assert not inspect.isabstract(astm_CompilationUnit)


def test_astm_compilationunit_constructor_exists():
    assert callable(astm_CompilationUnit.__init__)


def test_astm_compilationunit_constructor_args():
    sig = inspect.signature(astm_CompilationUnit.__init__)
    params = list(sig.parameters.keys())
    assert "language" in params, "Missing parameter 'language'"

def test_astm_compilationunit_has_language():
    assert hasattr(astm_CompilationUnit, "language")
    descriptor = None
    for klass in astm_CompilationUnit.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)



def test_gastmsemanticobject_is_not_abstract():
    assert not inspect.isabstract(GASTMSemanticObject)


def test_gastmsemanticobject_constructor_exists():
    assert callable(GASTMSemanticObject.__init__)


def test_gastmsemanticobject_constructor_args():
    sig = inspect.signature(GASTMSemanticObject.__init__)
    params = list(sig.parameters.keys())



def test_astm_scope_is_not_abstract():
    assert not inspect.isabstract(astm_Scope)


def test_astm_scope_constructor_exists():
    assert callable(astm_Scope.__init__)


def test_astm_scope_constructor_args():
    sig = inspect.signature(astm_Scope.__init__)
    params = list(sig.parameters.keys())



def test_astm_project_is_not_abstract():
    assert not inspect.isabstract(astm_Project)


def test_astm_project_constructor_exists():
    assert callable(astm_Project.__init__)


def test_astm_project_constructor_args():
    sig = inspect.signature(astm_Project.__init__)
    params = list(sig.parameters.keys())



def test_astm_sourcelocation_is_not_abstract():
    assert not inspect.isabstract(astm_SourceLocation)


def test_astm_sourcelocation_constructor_exists():
    assert callable(astm_SourceLocation.__init__)


def test_astm_sourcelocation_constructor_args():
    sig = inspect.signature(astm_SourceLocation.__init__)
    params = list(sig.parameters.keys())
    assert "startColumn" in params, "Missing parameter 'startColumn'"
    assert "startLine" in params, "Missing parameter 'startLine'"
    assert "endLine" in params, "Missing parameter 'endLine'"
    assert "endColumn" in params, "Missing parameter 'endColumn'"

def test_astm_sourcelocation_has_startColumn():
    assert hasattr(astm_SourceLocation, "startColumn")
    descriptor = None
    for klass in astm_SourceLocation.__mro__:
        if "startColumn" in klass.__dict__:
            descriptor = klass.__dict__["startColumn"]
            break
    assert isinstance(descriptor, property)

def test_astm_sourcelocation_has_startLine():
    assert hasattr(astm_SourceLocation, "startLine")
    descriptor = None
    for klass in astm_SourceLocation.__mro__:
        if "startLine" in klass.__dict__:
            descriptor = klass.__dict__["startLine"]
            break
    assert isinstance(descriptor, property)

def test_astm_sourcelocation_has_endLine():
    assert hasattr(astm_SourceLocation, "endLine")
    descriptor = None
    for klass in astm_SourceLocation.__mro__:
        if "endLine" in klass.__dict__:
            descriptor = klass.__dict__["endLine"]
            break
    assert isinstance(descriptor, property)

def test_astm_sourcelocation_has_endColumn():
    assert hasattr(astm_SourceLocation, "endColumn")
    descriptor = None
    for klass in astm_SourceLocation.__mro__:
        if "endColumn" in klass.__dict__:
            descriptor = klass.__dict__["endColumn"]
            break
    assert isinstance(descriptor, property)



def test_compilationunit_is_not_abstract():
    assert not inspect.isabstract(CompilationUnit)


def test_compilationunit_constructor_exists():
    assert callable(CompilationUnit.__init__)


def test_compilationunit_constructor_args():
    sig = inspect.signature(CompilationUnit.__init__)
    params = list(sig.parameters.keys())



def test_astm_delphiunit_is_not_abstract():
    assert not inspect.isabstract(astm_DelphiUnit)


def test_astm_delphiunit_constructor_exists():
    assert callable(astm_DelphiUnit.__init__)


def test_astm_delphiunit_constructor_args():
    sig = inspect.signature(astm_DelphiUnit.__init__)
    params = list(sig.parameters.keys())



def test_blockstatement_is_not_abstract():
    assert not inspect.isabstract(BlockStatement)


def test_blockstatement_constructor_exists():
    assert callable(BlockStatement.__init__)


def test_blockstatement_constructor_args():
    sig = inspect.signature(BlockStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm_delphiwithstatement_is_not_abstract():
    assert not inspect.isabstract(astm_DelphiWithStatement)


def test_astm_delphiwithstatement_constructor_exists():
    assert callable(astm_DelphiWithStatement.__init__)


def test_astm_delphiwithstatement_constructor_args():
    sig = inspect.signature(astm_DelphiWithStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm_delphiblockstatement_is_not_abstract():
    assert not inspect.isabstract(astm_DelphiBlockStatement)


def test_astm_delphiblockstatement_constructor_exists():
    assert callable(astm_DelphiBlockStatement.__init__)


def test_astm_delphiblockstatement_constructor_args():
    sig = inspect.signature(astm_DelphiBlockStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm_namedtypereference_is_not_abstract():
    assert not inspect.isabstract(astm_NamedTypeReference)


def test_astm_namedtypereference_constructor_exists():
    assert callable(astm_NamedTypeReference.__init__)


def test_astm_namedtypereference_constructor_args():
    sig = inspect.signature(astm_NamedTypeReference.__init__)
    params = list(sig.parameters.keys())



def test_astm_delphiimplementationsection_is_not_abstract():
    assert not inspect.isabstract(astm_DelphiImplementationSection)


def test_astm_delphiimplementationsection_constructor_exists():
    assert callable(astm_DelphiImplementationSection.__init__)


def test_astm_delphiimplementationsection_constructor_args():
    sig = inspect.signature(astm_DelphiImplementationSection.__init__)
    params = list(sig.parameters.keys())



def test_astm_delphiinterfacesection_is_not_abstract():
    assert not inspect.isabstract(astm_DelphiInterfaceSection)


def test_astm_delphiinterfacesection_constructor_exists():
    assert callable(astm_DelphiInterfaceSection.__init__)


def test_astm_delphiinterfacesection_constructor_args():
    sig = inspect.signature(astm_DelphiInterfaceSection.__init__)
    params = list(sig.parameters.keys())



def test_astm_name_is_not_abstract():
    assert not inspect.isabstract(astm_Name)


def test_astm_name_constructor_exists():
    assert callable(astm_Name.__init__)


def test_astm_name_constructor_args():
    sig = inspect.signature(astm_Name.__init__)
    params = list(sig.parameters.keys())
    assert "nameString" in params, "Missing parameter 'nameString'"

def test_astm_name_has_nameString():
    assert hasattr(astm_Name, "nameString")
    descriptor = None
    for klass in astm_Name.__mro__:
        if "nameString" in klass.__dict__:
            descriptor = klass.__dict__["nameString"]
            break
    assert isinstance(descriptor, property)


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
UnaryOperator_strategy = st.builds(
    UnaryOperator,
)
astm_AddressOf_strategy = st.builds(
    astm_AddressOf,
)
astm_Not_strategy = st.builds(
    astm_Not,
)
astm_Deref_strategy = st.builds(
    astm_Deref,
)
astm_BitNot_strategy = st.builds(
    astm_BitNot,
)
astm_Negate_strategy = st.builds(
    astm_Negate,
)
astm_UnaryPlus_strategy = st.builds(
    astm_UnaryPlus,
)
Literal_strategy = st.builds(
    Literal,
)
astm_RealLiteral_strategy = st.builds(
    astm_RealLiteral,
)
astm_BitLiteral_strategy = st.builds(
    astm_BitLiteral,
)
astm_CharLiteral_strategy = st.builds(
    astm_CharLiteral,
)
astm_BooleanLiteral_strategy = st.builds(
    astm_BooleanLiteral,
)
astm_StringLiteral_strategy = st.builds(
    astm_StringLiteral,
)
astm_PostDecrement_strategy = st.builds(
    astm_PostDecrement,
)
astm_PostIncrement_strategy = st.builds(
    astm_PostIncrement,
)
astm_IntegerLiteral_strategy = st.builds(
    astm_IntegerLiteral,
)
astm_Decrement_strategy = st.builds(
    astm_Decrement,
)
astm_Increment_strategy = st.builds(
    astm_Increment,
)
QualifiedIdentifierReference_strategy = st.builds(
    QualifiedIdentifierReference,
)
astm_QualifiedOverData_strategy = st.builds(
    astm_QualifiedOverData,
)
astm_QualifiedOverPointer_strategy = st.builds(
    astm_QualifiedOverPointer,
)
ForStatement_strategy = st.builds(
    ForStatement,
)
astm_ForCheckAfterStatement_strategy = st.builds(
    astm_ForCheckAfterStatement,
)
astm_ForCheckBeforeStatement_strategy = st.builds(
    astm_ForCheckBeforeStatement,
)
AccessKind_strategy = st.builds(
    AccessKind,
)
astm_Protected_strategy = st.builds(
    astm_Protected,
)
astm_Private_strategy = st.builds(
    astm_Private,
)
astm_Public_strategy = st.builds(
    astm_Public,
)
FormalParameterType_strategy = st.builds(
    FormalParameterType,
)
astm_ByReferenceFormalParameterType_strategy = st.builds(
    astm_ByReferenceFormalParameterType,
)
astm_ByValueFormalParameterType_strategy = st.builds(
    astm_ByValueFormalParameterType,
)
PrimitiveType_strategy = st.builds(
    PrimitiveType,
)
astm_Integer_strategy = st.builds(
    astm_Integer,
)
astm_Float_strategy = st.builds(
    astm_Float,
)
astm_Double_strategy = st.builds(
    astm_Double,
)
astm_Boolean_strategy = st.builds(
    astm_Boolean,
)
astm_String_strategy = st.builds(
    astm_String,
)
astm_LongDouble_strategy = st.builds(
    astm_LongDouble,
)
astm_LongInteger_strategy = st.builds(
    astm_LongInteger,
)
astm_ShortInteger_strategy = st.builds(
    astm_ShortInteger,
)
astm_Character_strategy = st.builds(
    astm_Character,
)
astm_Byte_strategy = st.builds(
    astm_Byte,
)
astm_WideCharacter_strategy = st.builds(
    astm_WideCharacter,
)
astm_Void_strategy = st.builds(
    astm_Void,
)
ActualParameterExpression_strategy = st.builds(
    ActualParameterExpression,
)
astm_ByReferenceActualParameterExpression_strategy = st.builds(
    astm_ByReferenceActualParameterExpression,
)
astm_ByValueActualParameterExpression_strategy = st.builds(
    astm_ByValueActualParameterExpression,
)
astm_Visitable_strategy = st.builds(
    astm_Visitable,
)
VirtualSpecification_strategy = st.builds(
    VirtualSpecification,
)
astm_PureVirtual_strategy = st.builds(
    astm_PureVirtual,
)
astm_NonVirtual_strategy = st.builds(
    astm_NonVirtual,
)
astm_Virtual_strategy = st.builds(
    astm_Virtual,
)
StorageSpecification_strategy = st.builds(
    StorageSpecification,
)
astm_PerClassMember_strategy = st.builds(
    astm_PerClassMember,
)
astm_FileLocal_strategy = st.builds(
    astm_FileLocal,
)
astm_FunctionPersistent_strategy = st.builds(
    astm_FunctionPersistent,
)
astm_NoDef_strategy = st.builds(
    astm_NoDef,
)
astm_External_strategy = st.builds(
    astm_External,
)
Scope_strategy = st.builds(
    Scope,
)
ActualParameter_strategy = st.builds(
    ActualParameter,
)
astm_MissingActualParameter_strategy = st.builds(
    astm_MissingActualParameter,
)
astm_ActualParameterExpression_strategy = st.builds(
    astm_ActualParameterExpression,
)
BinaryOperator_strategy = st.builds(
    BinaryOperator,
)
astm_Greater_strategy = st.builds(
    astm_Greater,
)
astm_NotLess_strategy = st.builds(
    astm_NotLess,
)
astm_Subtract_strategy = st.builds(
    astm_Subtract,
)
astm_BitAnd_strategy = st.builds(
    astm_BitAnd,
)
astm_Add_strategy = st.builds(
    astm_Add,
)
astm_NotGreater_strategy = st.builds(
    astm_NotGreater,
)
astm_Equal_strategy = st.builds(
    astm_Equal,
)
astm_SpecificConcatString_strategy = st.builds(
    astm_SpecificConcatString,
)
astm_Assign_strategy = st.builds(
    astm_Assign,
)
astm_Multiply_strategy = st.builds(
    astm_Multiply,
)
astm_Or_strategy = st.builds(
    astm_Or,
)
astm_Divide_strategy = st.builds(
    astm_Divide,
)
astm_SpecificIn_strategy = st.builds(
    astm_SpecificIn,
)
astm_Exponent_strategy = st.builds(
    astm_Exponent,
)
astm_NotEqual_strategy = st.builds(
    astm_NotEqual,
)
astm_SpecificLike_strategy = st.builds(
    astm_SpecificLike,
)
astm_BitRightShift_strategy = st.builds(
    astm_BitRightShift,
)
astm_SpecificLessEqual_strategy = st.builds(
    astm_SpecificLessEqual,
)
astm_SpecificGreaterEqual_strategy = st.builds(
    astm_SpecificGreaterEqual,
)
astm_BitLeftShift_strategy = st.builds(
    astm_BitLeftShift,
)
astm_Modulus_strategy = st.builds(
    astm_Modulus,
)
astm_BitOr_strategy = st.builds(
    astm_BitOr,
)
astm_Less_strategy = st.builds(
    astm_Less,
)
astm_And_strategy = st.builds(
    astm_And,
)
astm_BitXor_strategy = st.builds(
    astm_BitXor,
)
astm_OperatorAssign_strategy = st.builds(
    astm_OperatorAssign,
)
NameReference_strategy = st.builds(
    NameReference,
)
astm_IdentifierReference_strategy = st.builds(
    astm_IdentifierReference,
)
astm_TypeQualifiedIdentifierReference_strategy = st.builds(
    astm_TypeQualifiedIdentifierReference,
)
astm_QualifiedIdentifierReference_strategy = st.builds(
    astm_QualifiedIdentifierReference,
)
CatchBlock_strategy = st.builds(
    CatchBlock,
)
astm_VariableCatchBlock_strategy = st.builds(
    astm_VariableCatchBlock,
)
astm_TypesCatchBlock_strategy = st.builds(
    astm_TypesCatchBlock,
)
Expression_strategy = st.builds(
    Expression,
)
astm_BinaryExpression_strategy = st.builds(
    astm_BinaryExpression,
)
astm_UnaryExpression_strategy = st.builds(
    astm_UnaryExpression,
)
astm_NewExpression_strategy = st.builds(
    astm_NewExpression,
)
astm_FunctionCallExpression_strategy = st.builds(
    astm_FunctionCallExpression,
)
astm_RangeExpression_strategy = st.builds(
    astm_RangeExpression,
)
astm_ConditionalExpression_strategy = st.builds(
    astm_ConditionalExpression,
)
astm_Literal_strategy = st.builds(
    astm_Literal,
    value=
        safe_text
)
astm_CastExpression_strategy = st.builds(
    astm_CastExpression,
)
astm_AggregateExpression_strategy = st.builds(
    astm_AggregateExpression,
)
astm_ArrayAccess_strategy = st.builds(
    astm_ArrayAccess,
)
astm_NameReference_strategy = st.builds(
    astm_NameReference,
)
LoopStatement_strategy = st.builds(
    LoopStatement,
)
astm_WhileStatement_strategy = st.builds(
    astm_WhileStatement,
)
astm_DoWhileStatement_strategy = st.builds(
    astm_DoWhileStatement,
)
astm_ForStatement_strategy = st.builds(
    astm_ForStatement,
)
SwitchCase_strategy = st.builds(
    SwitchCase,
)
astm_DefaultBlock_strategy = st.builds(
    astm_DefaultBlock,
)
astm_CaseBlock_strategy = st.builds(
    astm_CaseBlock,
)
astm_LabelAccess_strategy = st.builds(
    astm_LabelAccess,
)
Statement_strategy = st.builds(
    Statement,
)
astm_IfStatement_strategy = st.builds(
    astm_IfStatement,
)
astm_LabeledStatement_strategy = st.builds(
    astm_LabeledStatement,
)
astm_ThrowStatement_strategy = st.builds(
    astm_ThrowStatement,
)
astm_LoopStatement_strategy = st.builds(
    astm_LoopStatement,
)
astm_JumpStatement_strategy = st.builds(
    astm_JumpStatement,
)
astm_ExpressionStatement_strategy = st.builds(
    astm_ExpressionStatement,
)
astm_SwitchStatement_strategy = st.builds(
    astm_SwitchStatement,
)
astm_ContinueStatement_strategy = st.builds(
    astm_ContinueStatement,
)
astm_DeclarationOrDefinitionStatement_strategy = st.builds(
    astm_DeclarationOrDefinitionStatement,
)
astm_ReturnStatement_strategy = st.builds(
    astm_ReturnStatement,
)
astm_SpecificSelectStatement_strategy = st.builds(
    astm_SpecificSelectStatement,
)
astm_EmptyStatement_strategy = st.builds(
    astm_EmptyStatement,
)
astm_TryStatement_strategy = st.builds(
    astm_TryStatement,
)
astm_BreakStatement_strategy = st.builds(
    astm_BreakStatement,
)
astm_TerminateStatement_strategy = st.builds(
    astm_TerminateStatement,
)
astm_DeleteStatement_strategy = st.builds(
    astm_DeleteStatement,
)
astm_BlockScope_strategy = st.builds(
    astm_BlockScope,
)
TypeReference_strategy = st.builds(
    TypeReference,
)
astm_BlockStatement_strategy = st.builds(
    astm_BlockStatement,
)
astm_UnnamedTypeReference_strategy = st.builds(
    astm_UnnamedTypeReference,
)
AggregateType_strategy = st.builds(
    AggregateType,
)
astm_StructureType_strategy = st.builds(
    astm_StructureType,
)
astm_AnnotationType_strategy = st.builds(
    astm_AnnotationType,
)
astm_UnionType_strategy = st.builds(
    astm_UnionType,
)
astm_ClassType_strategy = st.builds(
    astm_ClassType,
)
DataType_strategy = st.builds(
    DataType,
)
astm_ExceptionType_strategy = st.builds(
    astm_ExceptionType,
)
astm_EnumType_strategy = st.builds(
    astm_EnumType,
)
astm_ConstructedType_strategy = st.builds(
    astm_ConstructedType,
)
astm_PrimitiveType_strategy = st.builds(
    astm_PrimitiveType,
    isSigned=
        st.booleans()
)
astm_FormalParameterType_strategy = st.builds(
    astm_FormalParameterType,
)
ConstructedType_strategy = st.builds(
    ConstructedType,
)
astm_RangeType_strategy = st.builds(
    astm_RangeType,
)
astm_CollectionType_strategy = st.builds(
    astm_CollectionType,
)
astm_PointerType_strategy = st.builds(
    astm_PointerType,
)
astm_ReferenceType_strategy = st.builds(
    astm_ReferenceType,
)
astm_ArrayType_strategy = st.builds(
    astm_ArrayType,
)
astm_AggregateScope_strategy = st.builds(
    astm_AggregateScope,
)
PreprocessorElement_strategy = st.builds(
    PreprocessorElement,
)
astm_MacroDefinition_strategy = st.builds(
    astm_MacroDefinition,
    body=
        safe_text,
    macroName=
        safe_text
)
astm_MacroCall_strategy = st.builds(
    astm_MacroCall,
)
astm_IncludeUnit_strategy = st.builds(
    astm_IncludeUnit,
)
astm_Comment_strategy = st.builds(
    astm_Comment,
    text=
        safe_text
)
astm_AggregateType_strategy = st.builds(
    astm_AggregateType,
)
astm_NamedType_strategy = st.builds(
    astm_NamedType,
)
TypeDefinition_strategy = st.builds(
    TypeDefinition,
)
astm_AggregateTypeDefinition_strategy = st.builds(
    astm_AggregateTypeDefinition,
)
astm_NamedTypeDefinition_strategy = st.builds(
    astm_NamedTypeDefinition,
)
astm_FunctionScope_strategy = st.builds(
    astm_FunctionScope,
)
Definition_strategy = st.builds(
    Definition,
)
astm_SpecificTriggerDefinition_strategy = st.builds(
    astm_SpecificTriggerDefinition,
)
astm_FunctionDefinition_strategy = st.builds(
    astm_FunctionDefinition,
)
Declaration_strategy = st.builds(
    Declaration,
)
astm_FormalParameterDeclaration_strategy = st.builds(
    astm_FormalParameterDeclaration,
)
astm_VariableDeclaration_strategy = st.builds(
    astm_VariableDeclaration,
    isMutable=
        st.booleans()
)
astm_FunctionDeclaration_strategy = st.builds(
    astm_FunctionDeclaration,
)
astm_EnumLiteralDefinition_strategy = st.builds(
    astm_EnumLiteralDefinition,
)
DataDefinition_strategy = st.builds(
    DataDefinition,
)
astm_FormalParameterDefinition_strategy = st.builds(
    astm_FormalParameterDefinition,
)
astm_VariableDefinition_strategy = st.builds(
    astm_VariableDefinition,
)
astm_BitFieldDefinition_strategy = st.builds(
    astm_BitFieldDefinition,
)
astm_DataDefinition_strategy = st.builds(
    astm_DataDefinition,
    isMutable=
        st.booleans()
)
astm_EntryDefinition_strategy = st.builds(
    astm_EntryDefinition,
)
DefinitionObject_strategy = st.builds(
    DefinitionObject,
)
astm_TypeDefinition_strategy = st.builds(
    astm_TypeDefinition,
)
astm_NameSpaceDefinition_strategy = st.builds(
    astm_NameSpaceDefinition,
)
astm_LabelDefinition_strategy = st.builds(
    astm_LabelDefinition,
)
astm_DeclarationOrDefinition_strategy = st.builds(
    astm_DeclarationOrDefinition,
    isRegister=
        st.booleans(),
    linkageSpecifier=
        safe_text
)
astm_ProgramScope_strategy = st.builds(
    astm_ProgramScope,
)
OtherSyntaxObject_strategy = st.builds(
    OtherSyntaxObject,
)
astm_SwitchCase_strategy = st.builds(
    astm_SwitchCase,
)
astm_FunctionMemberAttribute_strategy = st.builds(
    astm_FunctionMemberAttribute,
)
astm_Operator_strategy = st.builds(
    astm_Operator,
)
astm_CatchBlock_strategy = st.builds(
    astm_CatchBlock,
)
astm_VirtualSpecification_strategy = st.builds(
    astm_VirtualSpecification,
)
astm_Dimension_strategy = st.builds(
    astm_Dimension,
)
astm_DerivesFrom_strategy = st.builds(
    astm_DerivesFrom,
    isVirtual=
        st.booleans()
)
astm_AnnotationExpression_strategy = st.builds(
    astm_AnnotationExpression,
)
GASTMObject_strategy = st.builds(
    GASTMObject,
)
astm_GASTMSyntaxObject_strategy = st.builds(
    astm_GASTMSyntaxObject,
)
DeclarationOrDefinition_strategy = st.builds(
    DeclarationOrDefinition,
)
astm_Declaration_strategy = st.builds(
    astm_Declaration,
)
astm_Definition_strategy = st.builds(
    astm_Definition,
)
GASTMSourceObject_strategy = st.builds(
    GASTMSourceObject,
)
astm_SourceFile_strategy = st.builds(
    astm_SourceFile,
    pathName=
        safe_text
)
Operator_strategy = st.builds(
    Operator,
)
astm_BinaryOperator_strategy = st.builds(
    astm_BinaryOperator,
)
astm_UnaryOperator_strategy = st.builds(
    astm_UnaryOperator,
)
Type_strategy = st.builds(
    Type,
)
astm_LabelType_strategy = st.builds(
    astm_LabelType,
)
astm_TypeReference_strategy = st.builds(
    astm_TypeReference,
)
astm_NameSpaceType_strategy = st.builds(
    astm_NameSpaceType,
)
astm_FunctionType_strategy = st.builds(
    astm_FunctionType,
)
astm_DataType_strategy = st.builds(
    astm_DataType,
)
GASTMSyntaxObject_strategy = st.builds(
    GASTMSyntaxObject,
)
astm_Statement_strategy = st.builds(
    astm_Statement,
)
astm_Expression_strategy = st.builds(
    astm_Expression,
)
astm_PreprocessorElement_strategy = st.builds(
    astm_PreprocessorElement,
)
astm_Type_strategy = st.builds(
    astm_Type,
    isConst=
        st.booleans(),
    isVolatile=
        st.booleans()
)
astm_OtherSyntaxObject_strategy = st.builds(
    astm_OtherSyntaxObject,
)
Visitable_strategy = st.builds(
    Visitable,
)
astm_GASTMSemanticObject_strategy = st.builds(
    astm_GASTMSemanticObject,
)
astm_StorageSpecification_strategy = st.builds(
    astm_StorageSpecification,
)
astm_ActualParameter_strategy = st.builds(
    astm_ActualParameter,
)
astm_GASTMSourceObject_strategy = st.builds(
    astm_GASTMSourceObject,
)
astm_FunctionMemberAttributes_strategy = st.builds(
    astm_FunctionMemberAttributes,
    isFriend=
        st.booleans(),
    isThisConst=
        st.booleans(),
    isInline=
        st.booleans()
)
astm_AccessKind_strategy = st.builds(
    astm_AccessKind,
)
astm_GASTMObject_strategy = st.builds(
    astm_GASTMObject,
)
FunctionCallExpression_strategy = st.builds(
    FunctionCallExpression,
)
astm_DelphiFunctionCallExpression_strategy = st.builds(
    astm_DelphiFunctionCallExpression,
)
astm_DefinitionObject_strategy = st.builds(
    astm_DefinitionObject,
)
astm_GlobalScope_strategy = st.builds(
    astm_GlobalScope,
)
astm_CompilationUnit_strategy = st.builds(
    astm_CompilationUnit,
    language=
        safe_text
)
GASTMSemanticObject_strategy = st.builds(
    GASTMSemanticObject,
)
astm_Scope_strategy = st.builds(
    astm_Scope,
)
astm_Project_strategy = st.builds(
    astm_Project,
)
astm_SourceLocation_strategy = st.builds(
    astm_SourceLocation,
    startColumn=
        st.integers(),
    startLine=
        st.integers(),
    endLine=
        st.integers(),
    endColumn=
        st.integers()
)
CompilationUnit_strategy = st.builds(
    CompilationUnit,
)
astm_DelphiUnit_strategy = st.builds(
    astm_DelphiUnit,
)
BlockStatement_strategy = st.builds(
    BlockStatement,
)
astm_DelphiWithStatement_strategy = st.builds(
    astm_DelphiWithStatement,
)
astm_DelphiBlockStatement_strategy = st.builds(
    astm_DelphiBlockStatement,
)
astm_NamedTypeReference_strategy = st.builds(
    astm_NamedTypeReference,
)
astm_DelphiImplementationSection_strategy = st.builds(
    astm_DelphiImplementationSection,
)
astm_DelphiInterfaceSection_strategy = st.builds(
    astm_DelphiInterfaceSection,
)
astm_Name_strategy = st.builds(
    astm_Name,
    nameString=
        safe_text
)

@given(instance=UnaryOperator_strategy)
@settings(max_examples=50)
def test_unaryoperator_instantiation(instance):
    assert isinstance(instance, UnaryOperator)

@given(instance=astm_AddressOf_strategy)
@settings(max_examples=50)
def test_astm_addressof_instantiation(instance):
    assert isinstance(instance, astm_AddressOf)

@given(instance=astm_Not_strategy)
@settings(max_examples=50)
def test_astm_not_instantiation(instance):
    assert isinstance(instance, astm_Not)

@given(instance=astm_Deref_strategy)
@settings(max_examples=50)
def test_astm_deref_instantiation(instance):
    assert isinstance(instance, astm_Deref)

@given(instance=astm_BitNot_strategy)
@settings(max_examples=50)
def test_astm_bitnot_instantiation(instance):
    assert isinstance(instance, astm_BitNot)

@given(instance=astm_Negate_strategy)
@settings(max_examples=50)
def test_astm_negate_instantiation(instance):
    assert isinstance(instance, astm_Negate)

@given(instance=astm_UnaryPlus_strategy)
@settings(max_examples=50)
def test_astm_unaryplus_instantiation(instance):
    assert isinstance(instance, astm_UnaryPlus)

@given(instance=Literal_strategy)
@settings(max_examples=50)
def test_literal_instantiation(instance):
    assert isinstance(instance, Literal)

@given(instance=astm_RealLiteral_strategy)
@settings(max_examples=50)
def test_astm_realliteral_instantiation(instance):
    assert isinstance(instance, astm_RealLiteral)

@given(instance=astm_BitLiteral_strategy)
@settings(max_examples=50)
def test_astm_bitliteral_instantiation(instance):
    assert isinstance(instance, astm_BitLiteral)

@given(instance=astm_CharLiteral_strategy)
@settings(max_examples=50)
def test_astm_charliteral_instantiation(instance):
    assert isinstance(instance, astm_CharLiteral)

@given(instance=astm_BooleanLiteral_strategy)
@settings(max_examples=50)
def test_astm_booleanliteral_instantiation(instance):
    assert isinstance(instance, astm_BooleanLiteral)

@given(instance=astm_StringLiteral_strategy)
@settings(max_examples=50)
def test_astm_stringliteral_instantiation(instance):
    assert isinstance(instance, astm_StringLiteral)

@given(instance=astm_PostDecrement_strategy)
@settings(max_examples=50)
def test_astm_postdecrement_instantiation(instance):
    assert isinstance(instance, astm_PostDecrement)

@given(instance=astm_PostIncrement_strategy)
@settings(max_examples=50)
def test_astm_postincrement_instantiation(instance):
    assert isinstance(instance, astm_PostIncrement)

@given(instance=astm_IntegerLiteral_strategy)
@settings(max_examples=50)
def test_astm_integerliteral_instantiation(instance):
    assert isinstance(instance, astm_IntegerLiteral)

@given(instance=astm_Decrement_strategy)
@settings(max_examples=50)
def test_astm_decrement_instantiation(instance):
    assert isinstance(instance, astm_Decrement)

@given(instance=astm_Increment_strategy)
@settings(max_examples=50)
def test_astm_increment_instantiation(instance):
    assert isinstance(instance, astm_Increment)

@given(instance=QualifiedIdentifierReference_strategy)
@settings(max_examples=50)
def test_qualifiedidentifierreference_instantiation(instance):
    assert isinstance(instance, QualifiedIdentifierReference)

@given(instance=astm_QualifiedOverData_strategy)
@settings(max_examples=50)
def test_astm_qualifiedoverdata_instantiation(instance):
    assert isinstance(instance, astm_QualifiedOverData)

@given(instance=astm_QualifiedOverPointer_strategy)
@settings(max_examples=50)
def test_astm_qualifiedoverpointer_instantiation(instance):
    assert isinstance(instance, astm_QualifiedOverPointer)

@given(instance=ForStatement_strategy)
@settings(max_examples=50)
def test_forstatement_instantiation(instance):
    assert isinstance(instance, ForStatement)

@given(instance=astm_ForCheckAfterStatement_strategy)
@settings(max_examples=50)
def test_astm_forcheckafterstatement_instantiation(instance):
    assert isinstance(instance, astm_ForCheckAfterStatement)

@given(instance=astm_ForCheckBeforeStatement_strategy)
@settings(max_examples=50)
def test_astm_forcheckbeforestatement_instantiation(instance):
    assert isinstance(instance, astm_ForCheckBeforeStatement)

@given(instance=AccessKind_strategy)
@settings(max_examples=50)
def test_accesskind_instantiation(instance):
    assert isinstance(instance, AccessKind)

@given(instance=astm_Protected_strategy)
@settings(max_examples=50)
def test_astm_protected_instantiation(instance):
    assert isinstance(instance, astm_Protected)

@given(instance=astm_Private_strategy)
@settings(max_examples=50)
def test_astm_private_instantiation(instance):
    assert isinstance(instance, astm_Private)

@given(instance=astm_Public_strategy)
@settings(max_examples=50)
def test_astm_public_instantiation(instance):
    assert isinstance(instance, astm_Public)

@given(instance=FormalParameterType_strategy)
@settings(max_examples=50)
def test_formalparametertype_instantiation(instance):
    assert isinstance(instance, FormalParameterType)

@given(instance=astm_ByReferenceFormalParameterType_strategy)
@settings(max_examples=50)
def test_astm_byreferenceformalparametertype_instantiation(instance):
    assert isinstance(instance, astm_ByReferenceFormalParameterType)

@given(instance=astm_ByValueFormalParameterType_strategy)
@settings(max_examples=50)
def test_astm_byvalueformalparametertype_instantiation(instance):
    assert isinstance(instance, astm_ByValueFormalParameterType)

@given(instance=PrimitiveType_strategy)
@settings(max_examples=50)
def test_primitivetype_instantiation(instance):
    assert isinstance(instance, PrimitiveType)

@given(instance=astm_Integer_strategy)
@settings(max_examples=50)
def test_astm_integer_instantiation(instance):
    assert isinstance(instance, astm_Integer)

@given(instance=astm_Float_strategy)
@settings(max_examples=50)
def test_astm_float_instantiation(instance):
    assert isinstance(instance, astm_Float)

@given(instance=astm_Double_strategy)
@settings(max_examples=50)
def test_astm_double_instantiation(instance):
    assert isinstance(instance, astm_Double)

@given(instance=astm_Boolean_strategy)
@settings(max_examples=50)
def test_astm_boolean_instantiation(instance):
    assert isinstance(instance, astm_Boolean)

@given(instance=astm_String_strategy)
@settings(max_examples=50)
def test_astm_string_instantiation(instance):
    assert isinstance(instance, astm_String)

@given(instance=astm_LongDouble_strategy)
@settings(max_examples=50)
def test_astm_longdouble_instantiation(instance):
    assert isinstance(instance, astm_LongDouble)

@given(instance=astm_LongInteger_strategy)
@settings(max_examples=50)
def test_astm_longinteger_instantiation(instance):
    assert isinstance(instance, astm_LongInteger)

@given(instance=astm_ShortInteger_strategy)
@settings(max_examples=50)
def test_astm_shortinteger_instantiation(instance):
    assert isinstance(instance, astm_ShortInteger)

@given(instance=astm_Character_strategy)
@settings(max_examples=50)
def test_astm_character_instantiation(instance):
    assert isinstance(instance, astm_Character)

@given(instance=astm_Byte_strategy)
@settings(max_examples=50)
def test_astm_byte_instantiation(instance):
    assert isinstance(instance, astm_Byte)

@given(instance=astm_WideCharacter_strategy)
@settings(max_examples=50)
def test_astm_widecharacter_instantiation(instance):
    assert isinstance(instance, astm_WideCharacter)

@given(instance=astm_Void_strategy)
@settings(max_examples=50)
def test_astm_void_instantiation(instance):
    assert isinstance(instance, astm_Void)

@given(instance=ActualParameterExpression_strategy)
@settings(max_examples=50)
def test_actualparameterexpression_instantiation(instance):
    assert isinstance(instance, ActualParameterExpression)

@given(instance=astm_ByReferenceActualParameterExpression_strategy)
@settings(max_examples=50)
def test_astm_byreferenceactualparameterexpression_instantiation(instance):
    assert isinstance(instance, astm_ByReferenceActualParameterExpression)

@given(instance=astm_ByValueActualParameterExpression_strategy)
@settings(max_examples=50)
def test_astm_byvalueactualparameterexpression_instantiation(instance):
    assert isinstance(instance, astm_ByValueActualParameterExpression)

@given(instance=astm_Visitable_strategy)
@settings(max_examples=50)
def test_astm_visitable_instantiation(instance):
    assert isinstance(instance, astm_Visitable)

@given(instance=VirtualSpecification_strategy)
@settings(max_examples=50)
def test_virtualspecification_instantiation(instance):
    assert isinstance(instance, VirtualSpecification)

@given(instance=astm_PureVirtual_strategy)
@settings(max_examples=50)
def test_astm_purevirtual_instantiation(instance):
    assert isinstance(instance, astm_PureVirtual)

@given(instance=astm_NonVirtual_strategy)
@settings(max_examples=50)
def test_astm_nonvirtual_instantiation(instance):
    assert isinstance(instance, astm_NonVirtual)

@given(instance=astm_Virtual_strategy)
@settings(max_examples=50)
def test_astm_virtual_instantiation(instance):
    assert isinstance(instance, astm_Virtual)

@given(instance=StorageSpecification_strategy)
@settings(max_examples=50)
def test_storagespecification_instantiation(instance):
    assert isinstance(instance, StorageSpecification)

@given(instance=astm_PerClassMember_strategy)
@settings(max_examples=50)
def test_astm_perclassmember_instantiation(instance):
    assert isinstance(instance, astm_PerClassMember)

@given(instance=astm_FileLocal_strategy)
@settings(max_examples=50)
def test_astm_filelocal_instantiation(instance):
    assert isinstance(instance, astm_FileLocal)

@given(instance=astm_FunctionPersistent_strategy)
@settings(max_examples=50)
def test_astm_functionpersistent_instantiation(instance):
    assert isinstance(instance, astm_FunctionPersistent)

@given(instance=astm_NoDef_strategy)
@settings(max_examples=50)
def test_astm_nodef_instantiation(instance):
    assert isinstance(instance, astm_NoDef)

@given(instance=astm_External_strategy)
@settings(max_examples=50)
def test_astm_external_instantiation(instance):
    assert isinstance(instance, astm_External)

@given(instance=Scope_strategy)
@settings(max_examples=50)
def test_scope_instantiation(instance):
    assert isinstance(instance, Scope)

@given(instance=ActualParameter_strategy)
@settings(max_examples=50)
def test_actualparameter_instantiation(instance):
    assert isinstance(instance, ActualParameter)

@given(instance=astm_MissingActualParameter_strategy)
@settings(max_examples=50)
def test_astm_missingactualparameter_instantiation(instance):
    assert isinstance(instance, astm_MissingActualParameter)

@given(instance=astm_ActualParameterExpression_strategy)
@settings(max_examples=50)
def test_astm_actualparameterexpression_instantiation(instance):
    assert isinstance(instance, astm_ActualParameterExpression)

@given(instance=BinaryOperator_strategy)
@settings(max_examples=50)
def test_binaryoperator_instantiation(instance):
    assert isinstance(instance, BinaryOperator)

@given(instance=astm_Greater_strategy)
@settings(max_examples=50)
def test_astm_greater_instantiation(instance):
    assert isinstance(instance, astm_Greater)

@given(instance=astm_NotLess_strategy)
@settings(max_examples=50)
def test_astm_notless_instantiation(instance):
    assert isinstance(instance, astm_NotLess)

@given(instance=astm_Subtract_strategy)
@settings(max_examples=50)
def test_astm_subtract_instantiation(instance):
    assert isinstance(instance, astm_Subtract)

@given(instance=astm_BitAnd_strategy)
@settings(max_examples=50)
def test_astm_bitand_instantiation(instance):
    assert isinstance(instance, astm_BitAnd)

@given(instance=astm_Add_strategy)
@settings(max_examples=50)
def test_astm_add_instantiation(instance):
    assert isinstance(instance, astm_Add)

@given(instance=astm_NotGreater_strategy)
@settings(max_examples=50)
def test_astm_notgreater_instantiation(instance):
    assert isinstance(instance, astm_NotGreater)

@given(instance=astm_Equal_strategy)
@settings(max_examples=50)
def test_astm_equal_instantiation(instance):
    assert isinstance(instance, astm_Equal)

@given(instance=astm_SpecificConcatString_strategy)
@settings(max_examples=50)
def test_astm_specificconcatstring_instantiation(instance):
    assert isinstance(instance, astm_SpecificConcatString)

@given(instance=astm_Assign_strategy)
@settings(max_examples=50)
def test_astm_assign_instantiation(instance):
    assert isinstance(instance, astm_Assign)

@given(instance=astm_Multiply_strategy)
@settings(max_examples=50)
def test_astm_multiply_instantiation(instance):
    assert isinstance(instance, astm_Multiply)

@given(instance=astm_Or_strategy)
@settings(max_examples=50)
def test_astm_or_instantiation(instance):
    assert isinstance(instance, astm_Or)

@given(instance=astm_Divide_strategy)
@settings(max_examples=50)
def test_astm_divide_instantiation(instance):
    assert isinstance(instance, astm_Divide)

@given(instance=astm_SpecificIn_strategy)
@settings(max_examples=50)
def test_astm_specificin_instantiation(instance):
    assert isinstance(instance, astm_SpecificIn)

@given(instance=astm_Exponent_strategy)
@settings(max_examples=50)
def test_astm_exponent_instantiation(instance):
    assert isinstance(instance, astm_Exponent)

@given(instance=astm_NotEqual_strategy)
@settings(max_examples=50)
def test_astm_notequal_instantiation(instance):
    assert isinstance(instance, astm_NotEqual)

@given(instance=astm_SpecificLike_strategy)
@settings(max_examples=50)
def test_astm_specificlike_instantiation(instance):
    assert isinstance(instance, astm_SpecificLike)

@given(instance=astm_BitRightShift_strategy)
@settings(max_examples=50)
def test_astm_bitrightshift_instantiation(instance):
    assert isinstance(instance, astm_BitRightShift)

@given(instance=astm_SpecificLessEqual_strategy)
@settings(max_examples=50)
def test_astm_specificlessequal_instantiation(instance):
    assert isinstance(instance, astm_SpecificLessEqual)

@given(instance=astm_SpecificGreaterEqual_strategy)
@settings(max_examples=50)
def test_astm_specificgreaterequal_instantiation(instance):
    assert isinstance(instance, astm_SpecificGreaterEqual)

@given(instance=astm_BitLeftShift_strategy)
@settings(max_examples=50)
def test_astm_bitleftshift_instantiation(instance):
    assert isinstance(instance, astm_BitLeftShift)

@given(instance=astm_Modulus_strategy)
@settings(max_examples=50)
def test_astm_modulus_instantiation(instance):
    assert isinstance(instance, astm_Modulus)

@given(instance=astm_BitOr_strategy)
@settings(max_examples=50)
def test_astm_bitor_instantiation(instance):
    assert isinstance(instance, astm_BitOr)

@given(instance=astm_Less_strategy)
@settings(max_examples=50)
def test_astm_less_instantiation(instance):
    assert isinstance(instance, astm_Less)

@given(instance=astm_And_strategy)
@settings(max_examples=50)
def test_astm_and_instantiation(instance):
    assert isinstance(instance, astm_And)

@given(instance=astm_BitXor_strategy)
@settings(max_examples=50)
def test_astm_bitxor_instantiation(instance):
    assert isinstance(instance, astm_BitXor)

@given(instance=astm_OperatorAssign_strategy)
@settings(max_examples=50)
def test_astm_operatorassign_instantiation(instance):
    assert isinstance(instance, astm_OperatorAssign)

@given(instance=NameReference_strategy)
@settings(max_examples=50)
def test_namereference_instantiation(instance):
    assert isinstance(instance, NameReference)

@given(instance=astm_IdentifierReference_strategy)
@settings(max_examples=50)
def test_astm_identifierreference_instantiation(instance):
    assert isinstance(instance, astm_IdentifierReference)

@given(instance=astm_TypeQualifiedIdentifierReference_strategy)
@settings(max_examples=50)
def test_astm_typequalifiedidentifierreference_instantiation(instance):
    assert isinstance(instance, astm_TypeQualifiedIdentifierReference)

@given(instance=astm_QualifiedIdentifierReference_strategy)
@settings(max_examples=50)
def test_astm_qualifiedidentifierreference_instantiation(instance):
    assert isinstance(instance, astm_QualifiedIdentifierReference)

@given(instance=CatchBlock_strategy)
@settings(max_examples=50)
def test_catchblock_instantiation(instance):
    assert isinstance(instance, CatchBlock)

@given(instance=astm_VariableCatchBlock_strategy)
@settings(max_examples=50)
def test_astm_variablecatchblock_instantiation(instance):
    assert isinstance(instance, astm_VariableCatchBlock)

@given(instance=astm_TypesCatchBlock_strategy)
@settings(max_examples=50)
def test_astm_typescatchblock_instantiation(instance):
    assert isinstance(instance, astm_TypesCatchBlock)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=astm_BinaryExpression_strategy)
@settings(max_examples=50)
def test_astm_binaryexpression_instantiation(instance):
    assert isinstance(instance, astm_BinaryExpression)

@given(instance=astm_UnaryExpression_strategy)
@settings(max_examples=50)
def test_astm_unaryexpression_instantiation(instance):
    assert isinstance(instance, astm_UnaryExpression)

@given(instance=astm_NewExpression_strategy)
@settings(max_examples=50)
def test_astm_newexpression_instantiation(instance):
    assert isinstance(instance, astm_NewExpression)

@given(instance=astm_FunctionCallExpression_strategy)
@settings(max_examples=50)
def test_astm_functioncallexpression_instantiation(instance):
    assert isinstance(instance, astm_FunctionCallExpression)

@given(instance=astm_RangeExpression_strategy)
@settings(max_examples=50)
def test_astm_rangeexpression_instantiation(instance):
    assert isinstance(instance, astm_RangeExpression)

@given(instance=astm_ConditionalExpression_strategy)
@settings(max_examples=50)
def test_astm_conditionalexpression_instantiation(instance):
    assert isinstance(instance, astm_ConditionalExpression)

@given(instance=astm_Literal_strategy)
@settings(max_examples=50)
def test_astm_literal_instantiation(instance):
    assert isinstance(instance, astm_Literal)



@given(instance=astm_Literal_strategy)
def test_astm_literal_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=astm_CastExpression_strategy)
@settings(max_examples=50)
def test_astm_castexpression_instantiation(instance):
    assert isinstance(instance, astm_CastExpression)

@given(instance=astm_AggregateExpression_strategy)
@settings(max_examples=50)
def test_astm_aggregateexpression_instantiation(instance):
    assert isinstance(instance, astm_AggregateExpression)

@given(instance=astm_ArrayAccess_strategy)
@settings(max_examples=50)
def test_astm_arrayaccess_instantiation(instance):
    assert isinstance(instance, astm_ArrayAccess)

@given(instance=astm_NameReference_strategy)
@settings(max_examples=50)
def test_astm_namereference_instantiation(instance):
    assert isinstance(instance, astm_NameReference)

@given(instance=LoopStatement_strategy)
@settings(max_examples=50)
def test_loopstatement_instantiation(instance):
    assert isinstance(instance, LoopStatement)

@given(instance=astm_WhileStatement_strategy)
@settings(max_examples=50)
def test_astm_whilestatement_instantiation(instance):
    assert isinstance(instance, astm_WhileStatement)

@given(instance=astm_DoWhileStatement_strategy)
@settings(max_examples=50)
def test_astm_dowhilestatement_instantiation(instance):
    assert isinstance(instance, astm_DoWhileStatement)

@given(instance=astm_ForStatement_strategy)
@settings(max_examples=50)
def test_astm_forstatement_instantiation(instance):
    assert isinstance(instance, astm_ForStatement)

@given(instance=SwitchCase_strategy)
@settings(max_examples=50)
def test_switchcase_instantiation(instance):
    assert isinstance(instance, SwitchCase)

@given(instance=astm_DefaultBlock_strategy)
@settings(max_examples=50)
def test_astm_defaultblock_instantiation(instance):
    assert isinstance(instance, astm_DefaultBlock)

@given(instance=astm_CaseBlock_strategy)
@settings(max_examples=50)
def test_astm_caseblock_instantiation(instance):
    assert isinstance(instance, astm_CaseBlock)

@given(instance=astm_LabelAccess_strategy)
@settings(max_examples=50)
def test_astm_labelaccess_instantiation(instance):
    assert isinstance(instance, astm_LabelAccess)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=astm_IfStatement_strategy)
@settings(max_examples=50)
def test_astm_ifstatement_instantiation(instance):
    assert isinstance(instance, astm_IfStatement)

@given(instance=astm_LabeledStatement_strategy)
@settings(max_examples=50)
def test_astm_labeledstatement_instantiation(instance):
    assert isinstance(instance, astm_LabeledStatement)

@given(instance=astm_ThrowStatement_strategy)
@settings(max_examples=50)
def test_astm_throwstatement_instantiation(instance):
    assert isinstance(instance, astm_ThrowStatement)

@given(instance=astm_LoopStatement_strategy)
@settings(max_examples=50)
def test_astm_loopstatement_instantiation(instance):
    assert isinstance(instance, astm_LoopStatement)

@given(instance=astm_JumpStatement_strategy)
@settings(max_examples=50)
def test_astm_jumpstatement_instantiation(instance):
    assert isinstance(instance, astm_JumpStatement)

@given(instance=astm_ExpressionStatement_strategy)
@settings(max_examples=50)
def test_astm_expressionstatement_instantiation(instance):
    assert isinstance(instance, astm_ExpressionStatement)

@given(instance=astm_SwitchStatement_strategy)
@settings(max_examples=50)
def test_astm_switchstatement_instantiation(instance):
    assert isinstance(instance, astm_SwitchStatement)

@given(instance=astm_ContinueStatement_strategy)
@settings(max_examples=50)
def test_astm_continuestatement_instantiation(instance):
    assert isinstance(instance, astm_ContinueStatement)

@given(instance=astm_DeclarationOrDefinitionStatement_strategy)
@settings(max_examples=50)
def test_astm_declarationordefinitionstatement_instantiation(instance):
    assert isinstance(instance, astm_DeclarationOrDefinitionStatement)

@given(instance=astm_ReturnStatement_strategy)
@settings(max_examples=50)
def test_astm_returnstatement_instantiation(instance):
    assert isinstance(instance, astm_ReturnStatement)

@given(instance=astm_SpecificSelectStatement_strategy)
@settings(max_examples=50)
def test_astm_specificselectstatement_instantiation(instance):
    assert isinstance(instance, astm_SpecificSelectStatement)

@given(instance=astm_EmptyStatement_strategy)
@settings(max_examples=50)
def test_astm_emptystatement_instantiation(instance):
    assert isinstance(instance, astm_EmptyStatement)

@given(instance=astm_TryStatement_strategy)
@settings(max_examples=50)
def test_astm_trystatement_instantiation(instance):
    assert isinstance(instance, astm_TryStatement)

@given(instance=astm_BreakStatement_strategy)
@settings(max_examples=50)
def test_astm_breakstatement_instantiation(instance):
    assert isinstance(instance, astm_BreakStatement)

@given(instance=astm_TerminateStatement_strategy)
@settings(max_examples=50)
def test_astm_terminatestatement_instantiation(instance):
    assert isinstance(instance, astm_TerminateStatement)

@given(instance=astm_DeleteStatement_strategy)
@settings(max_examples=50)
def test_astm_deletestatement_instantiation(instance):
    assert isinstance(instance, astm_DeleteStatement)

@given(instance=astm_BlockScope_strategy)
@settings(max_examples=50)
def test_astm_blockscope_instantiation(instance):
    assert isinstance(instance, astm_BlockScope)

@given(instance=TypeReference_strategy)
@settings(max_examples=50)
def test_typereference_instantiation(instance):
    assert isinstance(instance, TypeReference)

@given(instance=astm_BlockStatement_strategy)
@settings(max_examples=50)
def test_astm_blockstatement_instantiation(instance):
    assert isinstance(instance, astm_BlockStatement)

@given(instance=astm_UnnamedTypeReference_strategy)
@settings(max_examples=50)
def test_astm_unnamedtypereference_instantiation(instance):
    assert isinstance(instance, astm_UnnamedTypeReference)

@given(instance=AggregateType_strategy)
@settings(max_examples=50)
def test_aggregatetype_instantiation(instance):
    assert isinstance(instance, AggregateType)

@given(instance=astm_StructureType_strategy)
@settings(max_examples=50)
def test_astm_structuretype_instantiation(instance):
    assert isinstance(instance, astm_StructureType)

@given(instance=astm_AnnotationType_strategy)
@settings(max_examples=50)
def test_astm_annotationtype_instantiation(instance):
    assert isinstance(instance, astm_AnnotationType)

@given(instance=astm_UnionType_strategy)
@settings(max_examples=50)
def test_astm_uniontype_instantiation(instance):
    assert isinstance(instance, astm_UnionType)

@given(instance=astm_ClassType_strategy)
@settings(max_examples=50)
def test_astm_classtype_instantiation(instance):
    assert isinstance(instance, astm_ClassType)

@given(instance=DataType_strategy)
@settings(max_examples=50)
def test_datatype_instantiation(instance):
    assert isinstance(instance, DataType)

@given(instance=astm_ExceptionType_strategy)
@settings(max_examples=50)
def test_astm_exceptiontype_instantiation(instance):
    assert isinstance(instance, astm_ExceptionType)

@given(instance=astm_EnumType_strategy)
@settings(max_examples=50)
def test_astm_enumtype_instantiation(instance):
    assert isinstance(instance, astm_EnumType)

@given(instance=astm_ConstructedType_strategy)
@settings(max_examples=50)
def test_astm_constructedtype_instantiation(instance):
    assert isinstance(instance, astm_ConstructedType)

@given(instance=astm_PrimitiveType_strategy)
@settings(max_examples=50)
def test_astm_primitivetype_instantiation(instance):
    assert isinstance(instance, astm_PrimitiveType)



@given(instance=astm_PrimitiveType_strategy)
def test_astm_primitivetype_isSigned_setter(instance):
    original = instance.isSigned
    instance.isSigned = original
    assert instance.isSigned == original

@given(instance=astm_FormalParameterType_strategy)
@settings(max_examples=50)
def test_astm_formalparametertype_instantiation(instance):
    assert isinstance(instance, astm_FormalParameterType)

@given(instance=ConstructedType_strategy)
@settings(max_examples=50)
def test_constructedtype_instantiation(instance):
    assert isinstance(instance, ConstructedType)

@given(instance=astm_RangeType_strategy)
@settings(max_examples=50)
def test_astm_rangetype_instantiation(instance):
    assert isinstance(instance, astm_RangeType)

@given(instance=astm_CollectionType_strategy)
@settings(max_examples=50)
def test_astm_collectiontype_instantiation(instance):
    assert isinstance(instance, astm_CollectionType)

@given(instance=astm_PointerType_strategy)
@settings(max_examples=50)
def test_astm_pointertype_instantiation(instance):
    assert isinstance(instance, astm_PointerType)

@given(instance=astm_ReferenceType_strategy)
@settings(max_examples=50)
def test_astm_referencetype_instantiation(instance):
    assert isinstance(instance, astm_ReferenceType)

@given(instance=astm_ArrayType_strategy)
@settings(max_examples=50)
def test_astm_arraytype_instantiation(instance):
    assert isinstance(instance, astm_ArrayType)

@given(instance=astm_AggregateScope_strategy)
@settings(max_examples=50)
def test_astm_aggregatescope_instantiation(instance):
    assert isinstance(instance, astm_AggregateScope)

@given(instance=PreprocessorElement_strategy)
@settings(max_examples=50)
def test_preprocessorelement_instantiation(instance):
    assert isinstance(instance, PreprocessorElement)

@given(instance=astm_MacroDefinition_strategy)
@settings(max_examples=50)
def test_astm_macrodefinition_instantiation(instance):
    assert isinstance(instance, astm_MacroDefinition)



@given(instance=astm_MacroDefinition_strategy)
def test_astm_macrodefinition_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original



@given(instance=astm_MacroDefinition_strategy)
def test_astm_macrodefinition_macroName_setter(instance):
    original = instance.macroName
    instance.macroName = original
    assert instance.macroName == original

@given(instance=astm_MacroCall_strategy)
@settings(max_examples=50)
def test_astm_macrocall_instantiation(instance):
    assert isinstance(instance, astm_MacroCall)

@given(instance=astm_IncludeUnit_strategy)
@settings(max_examples=50)
def test_astm_includeunit_instantiation(instance):
    assert isinstance(instance, astm_IncludeUnit)

@given(instance=astm_Comment_strategy)
@settings(max_examples=50)
def test_astm_comment_instantiation(instance):
    assert isinstance(instance, astm_Comment)



@given(instance=astm_Comment_strategy)
def test_astm_comment_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=astm_AggregateType_strategy)
@settings(max_examples=50)
def test_astm_aggregatetype_instantiation(instance):
    assert isinstance(instance, astm_AggregateType)

@given(instance=astm_NamedType_strategy)
@settings(max_examples=50)
def test_astm_namedtype_instantiation(instance):
    assert isinstance(instance, astm_NamedType)

@given(instance=TypeDefinition_strategy)
@settings(max_examples=50)
def test_typedefinition_instantiation(instance):
    assert isinstance(instance, TypeDefinition)

@given(instance=astm_AggregateTypeDefinition_strategy)
@settings(max_examples=50)
def test_astm_aggregatetypedefinition_instantiation(instance):
    assert isinstance(instance, astm_AggregateTypeDefinition)

@given(instance=astm_NamedTypeDefinition_strategy)
@settings(max_examples=50)
def test_astm_namedtypedefinition_instantiation(instance):
    assert isinstance(instance, astm_NamedTypeDefinition)

@given(instance=astm_FunctionScope_strategy)
@settings(max_examples=50)
def test_astm_functionscope_instantiation(instance):
    assert isinstance(instance, astm_FunctionScope)

@given(instance=Definition_strategy)
@settings(max_examples=50)
def test_definition_instantiation(instance):
    assert isinstance(instance, Definition)

@given(instance=astm_SpecificTriggerDefinition_strategy)
@settings(max_examples=50)
def test_astm_specifictriggerdefinition_instantiation(instance):
    assert isinstance(instance, astm_SpecificTriggerDefinition)

@given(instance=astm_FunctionDefinition_strategy)
@settings(max_examples=50)
def test_astm_functiondefinition_instantiation(instance):
    assert isinstance(instance, astm_FunctionDefinition)

@given(instance=Declaration_strategy)
@settings(max_examples=50)
def test_declaration_instantiation(instance):
    assert isinstance(instance, Declaration)

@given(instance=astm_FormalParameterDeclaration_strategy)
@settings(max_examples=50)
def test_astm_formalparameterdeclaration_instantiation(instance):
    assert isinstance(instance, astm_FormalParameterDeclaration)

@given(instance=astm_VariableDeclaration_strategy)
@settings(max_examples=50)
def test_astm_variabledeclaration_instantiation(instance):
    assert isinstance(instance, astm_VariableDeclaration)



@given(instance=astm_VariableDeclaration_strategy)
def test_astm_variabledeclaration_isMutable_setter(instance):
    original = instance.isMutable
    instance.isMutable = original
    assert instance.isMutable == original

@given(instance=astm_FunctionDeclaration_strategy)
@settings(max_examples=50)
def test_astm_functiondeclaration_instantiation(instance):
    assert isinstance(instance, astm_FunctionDeclaration)

@given(instance=astm_EnumLiteralDefinition_strategy)
@settings(max_examples=50)
def test_astm_enumliteraldefinition_instantiation(instance):
    assert isinstance(instance, astm_EnumLiteralDefinition)

@given(instance=DataDefinition_strategy)
@settings(max_examples=50)
def test_datadefinition_instantiation(instance):
    assert isinstance(instance, DataDefinition)

@given(instance=astm_FormalParameterDefinition_strategy)
@settings(max_examples=50)
def test_astm_formalparameterdefinition_instantiation(instance):
    assert isinstance(instance, astm_FormalParameterDefinition)

@given(instance=astm_VariableDefinition_strategy)
@settings(max_examples=50)
def test_astm_variabledefinition_instantiation(instance):
    assert isinstance(instance, astm_VariableDefinition)

@given(instance=astm_BitFieldDefinition_strategy)
@settings(max_examples=50)
def test_astm_bitfielddefinition_instantiation(instance):
    assert isinstance(instance, astm_BitFieldDefinition)

@given(instance=astm_DataDefinition_strategy)
@settings(max_examples=50)
def test_astm_datadefinition_instantiation(instance):
    assert isinstance(instance, astm_DataDefinition)



@given(instance=astm_DataDefinition_strategy)
def test_astm_datadefinition_isMutable_setter(instance):
    original = instance.isMutable
    instance.isMutable = original
    assert instance.isMutable == original

@given(instance=astm_EntryDefinition_strategy)
@settings(max_examples=50)
def test_astm_entrydefinition_instantiation(instance):
    assert isinstance(instance, astm_EntryDefinition)

@given(instance=DefinitionObject_strategy)
@settings(max_examples=50)
def test_definitionobject_instantiation(instance):
    assert isinstance(instance, DefinitionObject)

@given(instance=astm_TypeDefinition_strategy)
@settings(max_examples=50)
def test_astm_typedefinition_instantiation(instance):
    assert isinstance(instance, astm_TypeDefinition)

@given(instance=astm_NameSpaceDefinition_strategy)
@settings(max_examples=50)
def test_astm_namespacedefinition_instantiation(instance):
    assert isinstance(instance, astm_NameSpaceDefinition)

@given(instance=astm_LabelDefinition_strategy)
@settings(max_examples=50)
def test_astm_labeldefinition_instantiation(instance):
    assert isinstance(instance, astm_LabelDefinition)

@given(instance=astm_DeclarationOrDefinition_strategy)
@settings(max_examples=50)
def test_astm_declarationordefinition_instantiation(instance):
    assert isinstance(instance, astm_DeclarationOrDefinition)



@given(instance=astm_DeclarationOrDefinition_strategy)
def test_astm_declarationordefinition_isRegister_setter(instance):
    original = instance.isRegister
    instance.isRegister = original
    assert instance.isRegister == original



@given(instance=astm_DeclarationOrDefinition_strategy)
def test_astm_declarationordefinition_linkageSpecifier_setter(instance):
    original = instance.linkageSpecifier
    instance.linkageSpecifier = original
    assert instance.linkageSpecifier == original

@given(instance=astm_ProgramScope_strategy)
@settings(max_examples=50)
def test_astm_programscope_instantiation(instance):
    assert isinstance(instance, astm_ProgramScope)

@given(instance=OtherSyntaxObject_strategy)
@settings(max_examples=50)
def test_othersyntaxobject_instantiation(instance):
    assert isinstance(instance, OtherSyntaxObject)

@given(instance=astm_SwitchCase_strategy)
@settings(max_examples=50)
def test_astm_switchcase_instantiation(instance):
    assert isinstance(instance, astm_SwitchCase)

@given(instance=astm_FunctionMemberAttribute_strategy)
@settings(max_examples=50)
def test_astm_functionmemberattribute_instantiation(instance):
    assert isinstance(instance, astm_FunctionMemberAttribute)

@given(instance=astm_Operator_strategy)
@settings(max_examples=50)
def test_astm_operator_instantiation(instance):
    assert isinstance(instance, astm_Operator)

@given(instance=astm_CatchBlock_strategy)
@settings(max_examples=50)
def test_astm_catchblock_instantiation(instance):
    assert isinstance(instance, astm_CatchBlock)

@given(instance=astm_VirtualSpecification_strategy)
@settings(max_examples=50)
def test_astm_virtualspecification_instantiation(instance):
    assert isinstance(instance, astm_VirtualSpecification)

@given(instance=astm_Dimension_strategy)
@settings(max_examples=50)
def test_astm_dimension_instantiation(instance):
    assert isinstance(instance, astm_Dimension)

@given(instance=astm_DerivesFrom_strategy)
@settings(max_examples=50)
def test_astm_derivesfrom_instantiation(instance):
    assert isinstance(instance, astm_DerivesFrom)



@given(instance=astm_DerivesFrom_strategy)
def test_astm_derivesfrom_isVirtual_setter(instance):
    original = instance.isVirtual
    instance.isVirtual = original
    assert instance.isVirtual == original

@given(instance=astm_AnnotationExpression_strategy)
@settings(max_examples=50)
def test_astm_annotationexpression_instantiation(instance):
    assert isinstance(instance, astm_AnnotationExpression)

@given(instance=GASTMObject_strategy)
@settings(max_examples=50)
def test_gastmobject_instantiation(instance):
    assert isinstance(instance, GASTMObject)

@given(instance=astm_GASTMSyntaxObject_strategy)
@settings(max_examples=50)
def test_astm_gastmsyntaxobject_instantiation(instance):
    assert isinstance(instance, astm_GASTMSyntaxObject)

@given(instance=DeclarationOrDefinition_strategy)
@settings(max_examples=50)
def test_declarationordefinition_instantiation(instance):
    assert isinstance(instance, DeclarationOrDefinition)

@given(instance=astm_Declaration_strategy)
@settings(max_examples=50)
def test_astm_declaration_instantiation(instance):
    assert isinstance(instance, astm_Declaration)

@given(instance=astm_Definition_strategy)
@settings(max_examples=50)
def test_astm_definition_instantiation(instance):
    assert isinstance(instance, astm_Definition)

@given(instance=GASTMSourceObject_strategy)
@settings(max_examples=50)
def test_gastmsourceobject_instantiation(instance):
    assert isinstance(instance, GASTMSourceObject)

@given(instance=astm_SourceFile_strategy)
@settings(max_examples=50)
def test_astm_sourcefile_instantiation(instance):
    assert isinstance(instance, astm_SourceFile)



@given(instance=astm_SourceFile_strategy)
def test_astm_sourcefile_pathName_setter(instance):
    original = instance.pathName
    instance.pathName = original
    assert instance.pathName == original

@given(instance=Operator_strategy)
@settings(max_examples=50)
def test_operator_instantiation(instance):
    assert isinstance(instance, Operator)

@given(instance=astm_BinaryOperator_strategy)
@settings(max_examples=50)
def test_astm_binaryoperator_instantiation(instance):
    assert isinstance(instance, astm_BinaryOperator)

@given(instance=astm_UnaryOperator_strategy)
@settings(max_examples=50)
def test_astm_unaryoperator_instantiation(instance):
    assert isinstance(instance, astm_UnaryOperator)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=astm_LabelType_strategy)
@settings(max_examples=50)
def test_astm_labeltype_instantiation(instance):
    assert isinstance(instance, astm_LabelType)

@given(instance=astm_TypeReference_strategy)
@settings(max_examples=50)
def test_astm_typereference_instantiation(instance):
    assert isinstance(instance, astm_TypeReference)

@given(instance=astm_NameSpaceType_strategy)
@settings(max_examples=50)
def test_astm_namespacetype_instantiation(instance):
    assert isinstance(instance, astm_NameSpaceType)

@given(instance=astm_FunctionType_strategy)
@settings(max_examples=50)
def test_astm_functiontype_instantiation(instance):
    assert isinstance(instance, astm_FunctionType)

@given(instance=astm_DataType_strategy)
@settings(max_examples=50)
def test_astm_datatype_instantiation(instance):
    assert isinstance(instance, astm_DataType)

@given(instance=GASTMSyntaxObject_strategy)
@settings(max_examples=50)
def test_gastmsyntaxobject_instantiation(instance):
    assert isinstance(instance, GASTMSyntaxObject)

@given(instance=astm_Statement_strategy)
@settings(max_examples=50)
def test_astm_statement_instantiation(instance):
    assert isinstance(instance, astm_Statement)

@given(instance=astm_Expression_strategy)
@settings(max_examples=50)
def test_astm_expression_instantiation(instance):
    assert isinstance(instance, astm_Expression)

@given(instance=astm_PreprocessorElement_strategy)
@settings(max_examples=50)
def test_astm_preprocessorelement_instantiation(instance):
    assert isinstance(instance, astm_PreprocessorElement)

@given(instance=astm_Type_strategy)
@settings(max_examples=50)
def test_astm_type_instantiation(instance):
    assert isinstance(instance, astm_Type)



@given(instance=astm_Type_strategy)
def test_astm_type_isConst_setter(instance):
    original = instance.isConst
    instance.isConst = original
    assert instance.isConst == original



@given(instance=astm_Type_strategy)
def test_astm_type_isVolatile_setter(instance):
    original = instance.isVolatile
    instance.isVolatile = original
    assert instance.isVolatile == original

@given(instance=astm_OtherSyntaxObject_strategy)
@settings(max_examples=50)
def test_astm_othersyntaxobject_instantiation(instance):
    assert isinstance(instance, astm_OtherSyntaxObject)

@given(instance=Visitable_strategy)
@settings(max_examples=50)
def test_visitable_instantiation(instance):
    assert isinstance(instance, Visitable)

@given(instance=astm_GASTMSemanticObject_strategy)
@settings(max_examples=50)
def test_astm_gastmsemanticobject_instantiation(instance):
    assert isinstance(instance, astm_GASTMSemanticObject)

@given(instance=astm_StorageSpecification_strategy)
@settings(max_examples=50)
def test_astm_storagespecification_instantiation(instance):
    assert isinstance(instance, astm_StorageSpecification)

@given(instance=astm_ActualParameter_strategy)
@settings(max_examples=50)
def test_astm_actualparameter_instantiation(instance):
    assert isinstance(instance, astm_ActualParameter)

@given(instance=astm_GASTMSourceObject_strategy)
@settings(max_examples=50)
def test_astm_gastmsourceobject_instantiation(instance):
    assert isinstance(instance, astm_GASTMSourceObject)

@given(instance=astm_FunctionMemberAttributes_strategy)
@settings(max_examples=50)
def test_astm_functionmemberattributes_instantiation(instance):
    assert isinstance(instance, astm_FunctionMemberAttributes)



@given(instance=astm_FunctionMemberAttributes_strategy)
def test_astm_functionmemberattributes_isFriend_setter(instance):
    original = instance.isFriend
    instance.isFriend = original
    assert instance.isFriend == original



@given(instance=astm_FunctionMemberAttributes_strategy)
def test_astm_functionmemberattributes_isThisConst_setter(instance):
    original = instance.isThisConst
    instance.isThisConst = original
    assert instance.isThisConst == original



@given(instance=astm_FunctionMemberAttributes_strategy)
def test_astm_functionmemberattributes_isInline_setter(instance):
    original = instance.isInline
    instance.isInline = original
    assert instance.isInline == original

@given(instance=astm_AccessKind_strategy)
@settings(max_examples=50)
def test_astm_accesskind_instantiation(instance):
    assert isinstance(instance, astm_AccessKind)

@given(instance=astm_GASTMObject_strategy)
@settings(max_examples=50)
def test_astm_gastmobject_instantiation(instance):
    assert isinstance(instance, astm_GASTMObject)

@given(instance=FunctionCallExpression_strategy)
@settings(max_examples=50)
def test_functioncallexpression_instantiation(instance):
    assert isinstance(instance, FunctionCallExpression)

@given(instance=astm_DelphiFunctionCallExpression_strategy)
@settings(max_examples=50)
def test_astm_delphifunctioncallexpression_instantiation(instance):
    assert isinstance(instance, astm_DelphiFunctionCallExpression)

@given(instance=astm_DefinitionObject_strategy)
@settings(max_examples=50)
def test_astm_definitionobject_instantiation(instance):
    assert isinstance(instance, astm_DefinitionObject)

@given(instance=astm_GlobalScope_strategy)
@settings(max_examples=50)
def test_astm_globalscope_instantiation(instance):
    assert isinstance(instance, astm_GlobalScope)

@given(instance=astm_CompilationUnit_strategy)
@settings(max_examples=50)
def test_astm_compilationunit_instantiation(instance):
    assert isinstance(instance, astm_CompilationUnit)



@given(instance=astm_CompilationUnit_strategy)
def test_astm_compilationunit_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original

@given(instance=GASTMSemanticObject_strategy)
@settings(max_examples=50)
def test_gastmsemanticobject_instantiation(instance):
    assert isinstance(instance, GASTMSemanticObject)

@given(instance=astm_Scope_strategy)
@settings(max_examples=50)
def test_astm_scope_instantiation(instance):
    assert isinstance(instance, astm_Scope)

@given(instance=astm_Project_strategy)
@settings(max_examples=50)
def test_astm_project_instantiation(instance):
    assert isinstance(instance, astm_Project)

@given(instance=astm_SourceLocation_strategy)
@settings(max_examples=50)
def test_astm_sourcelocation_instantiation(instance):
    assert isinstance(instance, astm_SourceLocation)



@given(instance=astm_SourceLocation_strategy)
def test_astm_sourcelocation_startColumn_setter(instance):
    original = instance.startColumn
    instance.startColumn = original
    assert instance.startColumn == original



@given(instance=astm_SourceLocation_strategy)
def test_astm_sourcelocation_startLine_setter(instance):
    original = instance.startLine
    instance.startLine = original
    assert instance.startLine == original



@given(instance=astm_SourceLocation_strategy)
def test_astm_sourcelocation_endLine_setter(instance):
    original = instance.endLine
    instance.endLine = original
    assert instance.endLine == original



@given(instance=astm_SourceLocation_strategy)
def test_astm_sourcelocation_endColumn_setter(instance):
    original = instance.endColumn
    instance.endColumn = original
    assert instance.endColumn == original

@given(instance=CompilationUnit_strategy)
@settings(max_examples=50)
def test_compilationunit_instantiation(instance):
    assert isinstance(instance, CompilationUnit)

@given(instance=astm_DelphiUnit_strategy)
@settings(max_examples=50)
def test_astm_delphiunit_instantiation(instance):
    assert isinstance(instance, astm_DelphiUnit)

@given(instance=BlockStatement_strategy)
@settings(max_examples=50)
def test_blockstatement_instantiation(instance):
    assert isinstance(instance, BlockStatement)

@given(instance=astm_DelphiWithStatement_strategy)
@settings(max_examples=50)
def test_astm_delphiwithstatement_instantiation(instance):
    assert isinstance(instance, astm_DelphiWithStatement)

@given(instance=astm_DelphiBlockStatement_strategy)
@settings(max_examples=50)
def test_astm_delphiblockstatement_instantiation(instance):
    assert isinstance(instance, astm_DelphiBlockStatement)

@given(instance=astm_NamedTypeReference_strategy)
@settings(max_examples=50)
def test_astm_namedtypereference_instantiation(instance):
    assert isinstance(instance, astm_NamedTypeReference)

@given(instance=astm_DelphiImplementationSection_strategy)
@settings(max_examples=50)
def test_astm_delphiimplementationsection_instantiation(instance):
    assert isinstance(instance, astm_DelphiImplementationSection)

@given(instance=astm_DelphiInterfaceSection_strategy)
@settings(max_examples=50)
def test_astm_delphiinterfacesection_instantiation(instance):
    assert isinstance(instance, astm_DelphiInterfaceSection)

@given(instance=astm_Name_strategy)
@settings(max_examples=50)
def test_astm_name_instantiation(instance):
    assert isinstance(instance, astm_Name)



@given(instance=astm_Name_strategy)
def test_astm_name_nameString_setter(instance):
    original = instance.nameString
    instance.nameString = original
    assert instance.nameString == original
