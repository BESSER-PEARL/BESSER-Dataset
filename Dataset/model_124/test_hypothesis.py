import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ActualParameter,
    astm_gastm_ActualParameterExpression,
    BinaryOperator,
    astm_gastm_OperatorAssign,
    IdentifierReference,
    NameReference,
    astm_gastm_TypeQualifiedIdentifierReference,
    astm_gastm_QualifiedIdentifierReference,
    SwitchCase,
    astm_gastm_CaseBlock,
    CatchBlock,
    astm_gastm_VariableCatchBlock,
    astm_gastm_TypesCatchBlock,
    LoopStatement,
    astm_gastm_ForStatement,
    BlockScope,
    LabelDefinition,
    LabelAccess,
    Dimension,
    ConstructedType,
    astm_gastm_ArrayType,
    AggregateScope,
    DerivesFrom,
    FormalParameterType,
    EnumLiteralDefinition,
    DataType,
    astm_gastm_NamedType,
    astm_gastm_ConstructedType,
    astm_gastm_AggregateType,
    astm_gastm_FormalParameterType,
    astm_gastm_EnumType,
    astm_gastm_PrimitiveType,
    MacroDefinition,
    DataDefinition,
    astm_gastm_BitFieldDefinition,
    Expression,
    astm_gastm_Literal,
    astm_gastm_LabelAccess,
    astm_gastm_AnnotationExpression,
    astm_gastm_RangeExpression,
    astm_gastm_CastExpression,
    astm_gastm_NameReference,
    astm_gastm_FunctionCallExpression,
    astm_gastm_ArrayAccess,
    astm_gastm_BinaryExpression,
    astm_gastm_NewExpression,
    astm_gastm_ConditionalExpression,
    astm_gastm_UnaryExpression,
    LabelType,
    NameSpaceType,
    AggregateType,
    astm_gastm_ClassType,
    NamedType,
    TypeDefinition,
    astm_gastm_AggregateTypeDefinition,
    astm_gastm_NamedTypeDefinition,
    Definition,
    astm_gastm_EnumLiteralDefinition,
    astm_gastm_EntryDefinition,
    astm_gastm_DataDefinition,
    TypeReference,
    astm_gastm_UnnamedTypeReference,
    astm_gastm_NamedTypeReference,
    Name,
    DeclarationOrDefinition,
    astm_gastm_Declaration,
    astm_gastm_Definition,
    VirtualSpecification,
    astm_gastm_FunctionMemberAttributes,
    FunctionScope,
    Statement,
    astm_gastm_ExpressionStatement,
    astm_gastm_IfStatement,
    astm_gastm_BlockStatement,
    astm_gastm_JumpStatement,
    astm_gastm_BreakStatement,
    astm_gastm_DeleteStatement,
    astm_gastm_LabeledStatement,
    astm_gastm_EmptyStatement,
    astm_gastm_ContinueStatement,
    astm_gastm_DeclarationOrDefinitionStatement,
    astm_gastm_TryStatement,
    astm_gastm_SwitchStatement,
    astm_gastm_LoopStatement,
    astm_gastm_ThrowStatement,
    astm_gastm_ReturnStatement,
    FormalParameterDefinition,
    DelphiInterfaceSection,
    FunctionCallExpression,
    astm_sastm_DelphiFunctionCallExpression,
    BlockStatement,
    astm_sastm_DelphiWithStatement,
    astm_sastm_DelphiBlockStatement,
    NamedTypeReference,
    DelphiImplementationSection,
    astm_gastm_Multiply,
    astm_gastm_Subtract,
    astm_gastm_Add,
    astm_gastm_SpecificSelectStatement,
    astm_gastm_SpecificConcatString,
    astm_gastm_SpecificLike,
    astm_gastm_SpecificIn,
    astm_gastm_SpecificGreaterEqual,
    astm_gastm_SpecificLessEqual,
    astm_gastm_SpecificTriggerDefinition,
    ActualParameterExpression,
    astm_gastm_ByReferenceActualParameterExpression,
    astm_gastm_ByValueActualParameterExpression,
    astm_gastm_MissingActualParameter,
    astm_gastm_Assign,
    astm_gastm_BitRightShift,
    astm_gastm_BitLeftShift,
    astm_gastm_BitXor,
    astm_gastm_BitOr,
    astm_gastm_BitAnd,
    astm_gastm_NotLess,
    astm_gastm_Less,
    astm_gastm_NotGreater,
    astm_gastm_Greater,
    astm_gastm_NotEqual,
    astm_gastm_Equal,
    astm_gastm_Or,
    astm_gastm_And,
    astm_gastm_Exponent,
    astm_gastm_Modulus,
    astm_gastm_Divide,
    astm_gastm_PointerType,
    astm_gastm_CollectionType,
    UnaryOperator,
    astm_gastm_Not,
    astm_gastm_BitNot,
    astm_gastm_Increment,
    astm_gastm_Decrement,
    astm_gastm_PostDecrement,
    astm_gastm_Negate,
    astm_gastm_AddressOf,
    astm_gastm_PostIncrement,
    astm_gastm_Deref,
    astm_gastm_UnaryPlus,
    Literal,
    astm_gastm_RealLiteral,
    astm_gastm_StringLiteral,
    astm_gastm_BooleanLiteral,
    astm_gastm_BitLiteral,
    astm_gastm_CharLiteral,
    astm_gastm_IntegerLiteral,
    QualifiedIdentifierReference,
    astm_gastm_QualifiedOverData,
    astm_gastm_QualifiedOverPointer,
    astm_gastm_AggregateExpression,
    ForStatement,
    astm_gastm_ForCheckAfterStatement,
    astm_gastm_ForCheckBeforeStatement,
    astm_gastm_DoWhileStatement,
    astm_gastm_WhileStatement,
    astm_gastm_DefaultBlock,
    astm_gastm_TerminateStatement,
    AccessKind,
    astm_gastm_Private,
    astm_gastm_Protected,
    astm_gastm_Public,
    astm_gastm_ByReferenceFormalParameterType,
    astm_gastm_ByValueFormalParameterType,
    astm_gastm_AnnotationType,
    astm_gastm_UnionType,
    astm_gastm_StructureType,
    astm_gastm_RangeType,
    astm_gastm_ReferenceType,
    PrimitiveType,
    astm_gastm_LongInteger,
    astm_gastm_Byte,
    astm_gastm_LongDouble,
    astm_gastm_String,
    astm_gastm_Float,
    astm_gastm_Character,
    astm_gastm_Boolean,
    astm_gastm_ShortInteger,
    astm_gastm_Integer,
    astm_gastm_WideCharacter,
    astm_gastm_Double,
    astm_gastm_Void,
    astm_gastm_ExceptionType,
    astm_gastm_NonVirtual,
    astm_gastm_PureVirtual,
    astm_gastm_Virtual,
    StorageSpecification,
    astm_gastm_NoDef,
    astm_gastm_FunctionPersistent,
    astm_gastm_PerClassMember,
    astm_gastm_FileLocal,
    astm_gastm_External,
    astm_gastm_VariableDefinition,
    astm_gastm_FormalParameterDefinition,
    astm_gastm_IdentifierReference,
    astm_gastm_FunctionDefinition,
    FunctionMemberAttributes,
    FormalParameterDeclaration,
    Declaration,
    astm_gastm_VariableDeclaration,
    astm_gastm_FormalParameterDeclaration,
    astm_gastm_FunctionDeclaration,
    SourceFile,
    GASTMSourceObject,
    astm_gastm_SourceLocation,
    astm_gastm_SourceFile,
    astm_gastm_ActualParameter,
    astm_gastm_BinaryOperator,
    astm_gastm_UnaryOperator,
    astm_gastm_AccessKind,
    Type,
    astm_gastm_FunctionType,
    astm_gastm_LabelType,
    astm_gastm_NameSpaceType,
    astm_gastm_TypeReference,
    astm_gastm_DataType,
    astm_gastm_StorageSpecification,
    GASTMSyntaxObject,
    astm_gastm_PreprocessorElement,
    astm_gastm_Type,
    astm_gastm_Statement,
    astm_gastm_Expression,
    astm_gastm_DefinitionObject,
    astm_gastm_OtherSyntaxObject,
    astm_gastm_GASTMSemanticObject,
    astm_gastm_GASTMSourceObject,
    astm_gastm_GASTMObject,
    ProgramScope,
    OtherSyntaxObject,
    astm_gastm_Name,
    astm_gastm_CatchBlock,
    astm_gastm_DerivesFrom,
    astm_gastm_Dimension,
    astm_gastm_FunctionMemberAttribute,
    astm_gastm_VirtualSpecification,
    astm_gastm_SwitchCase,
    astm_gastm_CompilationUnit,
    AnnotationExpression,
    PreprocessorElement,
    astm_gastm_IncludeUnit,
    astm_gastm_Comment,
    astm_gastm_MacroCall,
    astm_gastm_MacroDefinition,
    SourceLocation,
    GASTMObject,
    astm_gastm_GASTMSyntaxObject,
    Scope,
    astm_gastm_AggregateScope,
    astm_gastm_FunctionScope,
    astm_gastm_ProgramScope,
    astm_gastm_BlockScope,
    astm_gastm_GlobalScope,
    DefinitionObject,
    astm_gastm_NameSpaceDefinition,
    astm_gastm_DeclarationOrDefinition,
    astm_gastm_TypeDefinition,
    astm_gastm_LabelDefinition,
    GlobalScope,
    CompilationUnit,
    astm_sastm_DelphiInterfaceSection,
    astm_sastm_DelphiImplementationSection,
    astm_sastm_DelphiUnit,
    GASTMSemanticObject,
    astm_gastm_Scope,
    astm_gastm_Project,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_actualparameter_is_not_abstract():
    assert not inspect.isabstract(ActualParameter)


def test_actualparameter_constructor_exists():
    assert callable(ActualParameter.__init__)


def test_actualparameter_constructor_args():
    sig = inspect.signature(ActualParameter.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_actualparameterexpression_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_ActualParameterExpression)


def test_astm_gastm_actualparameterexpression_constructor_exists():
    assert callable(astm_gastm_ActualParameterExpression.__init__)


def test_astm_gastm_actualparameterexpression_constructor_args():
    sig = inspect.signature(astm_gastm_ActualParameterExpression.__init__)
    params = list(sig.parameters.keys())



def test_binaryoperator_is_not_abstract():
    assert not inspect.isabstract(BinaryOperator)


def test_binaryoperator_constructor_exists():
    assert callable(BinaryOperator.__init__)


def test_binaryoperator_constructor_args():
    sig = inspect.signature(BinaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_operatorassign_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_OperatorAssign)


def test_astm_gastm_operatorassign_constructor_exists():
    assert callable(astm_gastm_OperatorAssign.__init__)


def test_astm_gastm_operatorassign_constructor_args():
    sig = inspect.signature(astm_gastm_OperatorAssign.__init__)
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



def test_astm_gastm_typequalifiedidentifierreference_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_TypeQualifiedIdentifierReference)


def test_astm_gastm_typequalifiedidentifierreference_constructor_exists():
    assert callable(astm_gastm_TypeQualifiedIdentifierReference.__init__)


def test_astm_gastm_typequalifiedidentifierreference_constructor_args():
    sig = inspect.signature(astm_gastm_TypeQualifiedIdentifierReference.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_qualifiedidentifierreference_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_QualifiedIdentifierReference)


def test_astm_gastm_qualifiedidentifierreference_constructor_exists():
    assert callable(astm_gastm_QualifiedIdentifierReference.__init__)


def test_astm_gastm_qualifiedidentifierreference_constructor_args():
    sig = inspect.signature(astm_gastm_QualifiedIdentifierReference.__init__)
    params = list(sig.parameters.keys())



def test_switchcase_is_not_abstract():
    assert not inspect.isabstract(SwitchCase)


def test_switchcase_constructor_exists():
    assert callable(SwitchCase.__init__)


def test_switchcase_constructor_args():
    sig = inspect.signature(SwitchCase.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_caseblock_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_CaseBlock)


def test_astm_gastm_caseblock_constructor_exists():
    assert callable(astm_gastm_CaseBlock.__init__)


def test_astm_gastm_caseblock_constructor_args():
    sig = inspect.signature(astm_gastm_CaseBlock.__init__)
    params = list(sig.parameters.keys())



def test_catchblock_is_not_abstract():
    assert not inspect.isabstract(CatchBlock)


def test_catchblock_constructor_exists():
    assert callable(CatchBlock.__init__)


def test_catchblock_constructor_args():
    sig = inspect.signature(CatchBlock.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_variablecatchblock_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_VariableCatchBlock)


def test_astm_gastm_variablecatchblock_constructor_exists():
    assert callable(astm_gastm_VariableCatchBlock.__init__)


def test_astm_gastm_variablecatchblock_constructor_args():
    sig = inspect.signature(astm_gastm_VariableCatchBlock.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_typescatchblock_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_TypesCatchBlock)


def test_astm_gastm_typescatchblock_constructor_exists():
    assert callable(astm_gastm_TypesCatchBlock.__init__)


def test_astm_gastm_typescatchblock_constructor_args():
    sig = inspect.signature(astm_gastm_TypesCatchBlock.__init__)
    params = list(sig.parameters.keys())



def test_loopstatement_is_not_abstract():
    assert not inspect.isabstract(LoopStatement)


def test_loopstatement_constructor_exists():
    assert callable(LoopStatement.__init__)


def test_loopstatement_constructor_args():
    sig = inspect.signature(LoopStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_forstatement_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_ForStatement)


def test_astm_gastm_forstatement_constructor_exists():
    assert callable(astm_gastm_ForStatement.__init__)


def test_astm_gastm_forstatement_constructor_args():
    sig = inspect.signature(astm_gastm_ForStatement.__init__)
    params = list(sig.parameters.keys())



def test_blockscope_is_not_abstract():
    assert not inspect.isabstract(BlockScope)


def test_blockscope_constructor_exists():
    assert callable(BlockScope.__init__)


def test_blockscope_constructor_args():
    sig = inspect.signature(BlockScope.__init__)
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



def test_astm_gastm_arraytype_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_ArrayType)


def test_astm_gastm_arraytype_constructor_exists():
    assert callable(astm_gastm_ArrayType.__init__)


def test_astm_gastm_arraytype_constructor_args():
    sig = inspect.signature(astm_gastm_ArrayType.__init__)
    params = list(sig.parameters.keys())



def test_aggregatescope_is_not_abstract():
    assert not inspect.isabstract(AggregateScope)


def test_aggregatescope_constructor_exists():
    assert callable(AggregateScope.__init__)


def test_aggregatescope_constructor_args():
    sig = inspect.signature(AggregateScope.__init__)
    params = list(sig.parameters.keys())



def test_derivesfrom_is_not_abstract():
    assert not inspect.isabstract(DerivesFrom)


def test_derivesfrom_constructor_exists():
    assert callable(DerivesFrom.__init__)


def test_derivesfrom_constructor_args():
    sig = inspect.signature(DerivesFrom.__init__)
    params = list(sig.parameters.keys())



def test_formalparametertype_is_not_abstract():
    assert not inspect.isabstract(FormalParameterType)


def test_formalparametertype_constructor_exists():
    assert callable(FormalParameterType.__init__)


def test_formalparametertype_constructor_args():
    sig = inspect.signature(FormalParameterType.__init__)
    params = list(sig.parameters.keys())



def test_enumliteraldefinition_is_not_abstract():
    assert not inspect.isabstract(EnumLiteralDefinition)


def test_enumliteraldefinition_constructor_exists():
    assert callable(EnumLiteralDefinition.__init__)


def test_enumliteraldefinition_constructor_args():
    sig = inspect.signature(EnumLiteralDefinition.__init__)
    params = list(sig.parameters.keys())



def test_datatype_is_not_abstract():
    assert not inspect.isabstract(DataType)


def test_datatype_constructor_exists():
    assert callable(DataType.__init__)


def test_datatype_constructor_args():
    sig = inspect.signature(DataType.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_namedtype_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_NamedType)


def test_astm_gastm_namedtype_constructor_exists():
    assert callable(astm_gastm_NamedType.__init__)


def test_astm_gastm_namedtype_constructor_args():
    sig = inspect.signature(astm_gastm_NamedType.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_constructedtype_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_ConstructedType)


def test_astm_gastm_constructedtype_constructor_exists():
    assert callable(astm_gastm_ConstructedType.__init__)


def test_astm_gastm_constructedtype_constructor_args():
    sig = inspect.signature(astm_gastm_ConstructedType.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_aggregatetype_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_AggregateType)


def test_astm_gastm_aggregatetype_constructor_exists():
    assert callable(astm_gastm_AggregateType.__init__)


def test_astm_gastm_aggregatetype_constructor_args():
    sig = inspect.signature(astm_gastm_AggregateType.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_formalparametertype_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_FormalParameterType)


def test_astm_gastm_formalparametertype_constructor_exists():
    assert callable(astm_gastm_FormalParameterType.__init__)


def test_astm_gastm_formalparametertype_constructor_args():
    sig = inspect.signature(astm_gastm_FormalParameterType.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_enumtype_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_EnumType)


def test_astm_gastm_enumtype_constructor_exists():
    assert callable(astm_gastm_EnumType.__init__)


def test_astm_gastm_enumtype_constructor_args():
    sig = inspect.signature(astm_gastm_EnumType.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_primitivetype_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_PrimitiveType)


def test_astm_gastm_primitivetype_constructor_exists():
    assert callable(astm_gastm_PrimitiveType.__init__)


def test_astm_gastm_primitivetype_constructor_args():
    sig = inspect.signature(astm_gastm_PrimitiveType.__init__)
    params = list(sig.parameters.keys())
    assert "isSigned" in params, "Missing parameter 'isSigned'"

def test_astm_gastm_primitivetype_has_isSigned():
    assert hasattr(astm_gastm_PrimitiveType, "isSigned")
    descriptor = None
    for klass in astm_gastm_PrimitiveType.__mro__:
        if "isSigned" in klass.__dict__:
            descriptor = klass.__dict__["isSigned"]
            break
    assert isinstance(descriptor, property)



def test_macrodefinition_is_not_abstract():
    assert not inspect.isabstract(MacroDefinition)


def test_macrodefinition_constructor_exists():
    assert callable(MacroDefinition.__init__)


def test_macrodefinition_constructor_args():
    sig = inspect.signature(MacroDefinition.__init__)
    params = list(sig.parameters.keys())



def test_datadefinition_is_not_abstract():
    assert not inspect.isabstract(DataDefinition)


def test_datadefinition_constructor_exists():
    assert callable(DataDefinition.__init__)


def test_datadefinition_constructor_args():
    sig = inspect.signature(DataDefinition.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_bitfielddefinition_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_BitFieldDefinition)


def test_astm_gastm_bitfielddefinition_constructor_exists():
    assert callable(astm_gastm_BitFieldDefinition.__init__)


def test_astm_gastm_bitfielddefinition_constructor_args():
    sig = inspect.signature(astm_gastm_BitFieldDefinition.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_literal_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_Literal)


def test_astm_gastm_literal_constructor_exists():
    assert callable(astm_gastm_Literal.__init__)


def test_astm_gastm_literal_constructor_args():
    sig = inspect.signature(astm_gastm_Literal.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_astm_gastm_literal_has_value():
    assert hasattr(astm_gastm_Literal, "value")
    descriptor = None
    for klass in astm_gastm_Literal.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_astm_gastm_labelaccess_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_LabelAccess)


def test_astm_gastm_labelaccess_constructor_exists():
    assert callable(astm_gastm_LabelAccess.__init__)


def test_astm_gastm_labelaccess_constructor_args():
    sig = inspect.signature(astm_gastm_LabelAccess.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_annotationexpression_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_AnnotationExpression)


def test_astm_gastm_annotationexpression_constructor_exists():
    assert callable(astm_gastm_AnnotationExpression.__init__)


def test_astm_gastm_annotationexpression_constructor_args():
    sig = inspect.signature(astm_gastm_AnnotationExpression.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_rangeexpression_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_RangeExpression)


def test_astm_gastm_rangeexpression_constructor_exists():
    assert callable(astm_gastm_RangeExpression.__init__)


def test_astm_gastm_rangeexpression_constructor_args():
    sig = inspect.signature(astm_gastm_RangeExpression.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_castexpression_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_CastExpression)


def test_astm_gastm_castexpression_constructor_exists():
    assert callable(astm_gastm_CastExpression.__init__)


def test_astm_gastm_castexpression_constructor_args():
    sig = inspect.signature(astm_gastm_CastExpression.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_namereference_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_NameReference)


def test_astm_gastm_namereference_constructor_exists():
    assert callable(astm_gastm_NameReference.__init__)


def test_astm_gastm_namereference_constructor_args():
    sig = inspect.signature(astm_gastm_NameReference.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_functioncallexpression_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_FunctionCallExpression)


def test_astm_gastm_functioncallexpression_constructor_exists():
    assert callable(astm_gastm_FunctionCallExpression.__init__)


def test_astm_gastm_functioncallexpression_constructor_args():
    sig = inspect.signature(astm_gastm_FunctionCallExpression.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_arrayaccess_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_ArrayAccess)


def test_astm_gastm_arrayaccess_constructor_exists():
    assert callable(astm_gastm_ArrayAccess.__init__)


def test_astm_gastm_arrayaccess_constructor_args():
    sig = inspect.signature(astm_gastm_ArrayAccess.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_binaryexpression_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_BinaryExpression)


def test_astm_gastm_binaryexpression_constructor_exists():
    assert callable(astm_gastm_BinaryExpression.__init__)


def test_astm_gastm_binaryexpression_constructor_args():
    sig = inspect.signature(astm_gastm_BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_newexpression_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_NewExpression)


def test_astm_gastm_newexpression_constructor_exists():
    assert callable(astm_gastm_NewExpression.__init__)


def test_astm_gastm_newexpression_constructor_args():
    sig = inspect.signature(astm_gastm_NewExpression.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_conditionalexpression_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_ConditionalExpression)


def test_astm_gastm_conditionalexpression_constructor_exists():
    assert callable(astm_gastm_ConditionalExpression.__init__)


def test_astm_gastm_conditionalexpression_constructor_args():
    sig = inspect.signature(astm_gastm_ConditionalExpression.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_unaryexpression_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_UnaryExpression)


def test_astm_gastm_unaryexpression_constructor_exists():
    assert callable(astm_gastm_UnaryExpression.__init__)


def test_astm_gastm_unaryexpression_constructor_args():
    sig = inspect.signature(astm_gastm_UnaryExpression.__init__)
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



def test_astm_gastm_classtype_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_ClassType)


def test_astm_gastm_classtype_constructor_exists():
    assert callable(astm_gastm_ClassType.__init__)


def test_astm_gastm_classtype_constructor_args():
    sig = inspect.signature(astm_gastm_ClassType.__init__)
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



def test_astm_gastm_aggregatetypedefinition_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_AggregateTypeDefinition)


def test_astm_gastm_aggregatetypedefinition_constructor_exists():
    assert callable(astm_gastm_AggregateTypeDefinition.__init__)


def test_astm_gastm_aggregatetypedefinition_constructor_args():
    sig = inspect.signature(astm_gastm_AggregateTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_namedtypedefinition_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_NamedTypeDefinition)


def test_astm_gastm_namedtypedefinition_constructor_exists():
    assert callable(astm_gastm_NamedTypeDefinition.__init__)


def test_astm_gastm_namedtypedefinition_constructor_args():
    sig = inspect.signature(astm_gastm_NamedTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_definition_is_not_abstract():
    assert not inspect.isabstract(Definition)


def test_definition_constructor_exists():
    assert callable(Definition.__init__)


def test_definition_constructor_args():
    sig = inspect.signature(Definition.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_enumliteraldefinition_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_EnumLiteralDefinition)


def test_astm_gastm_enumliteraldefinition_constructor_exists():
    assert callable(astm_gastm_EnumLiteralDefinition.__init__)


def test_astm_gastm_enumliteraldefinition_constructor_args():
    sig = inspect.signature(astm_gastm_EnumLiteralDefinition.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_entrydefinition_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_EntryDefinition)


def test_astm_gastm_entrydefinition_constructor_exists():
    assert callable(astm_gastm_EntryDefinition.__init__)


def test_astm_gastm_entrydefinition_constructor_args():
    sig = inspect.signature(astm_gastm_EntryDefinition.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_datadefinition_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_DataDefinition)


def test_astm_gastm_datadefinition_constructor_exists():
    assert callable(astm_gastm_DataDefinition.__init__)


def test_astm_gastm_datadefinition_constructor_args():
    sig = inspect.signature(astm_gastm_DataDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "isMutable" in params, "Missing parameter 'isMutable'"

def test_astm_gastm_datadefinition_has_isMutable():
    assert hasattr(astm_gastm_DataDefinition, "isMutable")
    descriptor = None
    for klass in astm_gastm_DataDefinition.__mro__:
        if "isMutable" in klass.__dict__:
            descriptor = klass.__dict__["isMutable"]
            break
    assert isinstance(descriptor, property)



def test_typereference_is_not_abstract():
    assert not inspect.isabstract(TypeReference)


def test_typereference_constructor_exists():
    assert callable(TypeReference.__init__)


def test_typereference_constructor_args():
    sig = inspect.signature(TypeReference.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_unnamedtypereference_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_UnnamedTypeReference)


def test_astm_gastm_unnamedtypereference_constructor_exists():
    assert callable(astm_gastm_UnnamedTypeReference.__init__)


def test_astm_gastm_unnamedtypereference_constructor_args():
    sig = inspect.signature(astm_gastm_UnnamedTypeReference.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_namedtypereference_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_NamedTypeReference)


def test_astm_gastm_namedtypereference_constructor_exists():
    assert callable(astm_gastm_NamedTypeReference.__init__)


def test_astm_gastm_namedtypereference_constructor_args():
    sig = inspect.signature(astm_gastm_NamedTypeReference.__init__)
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



def test_astm_gastm_declaration_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_Declaration)


def test_astm_gastm_declaration_constructor_exists():
    assert callable(astm_gastm_Declaration.__init__)


def test_astm_gastm_declaration_constructor_args():
    sig = inspect.signature(astm_gastm_Declaration.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_definition_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_Definition)


def test_astm_gastm_definition_constructor_exists():
    assert callable(astm_gastm_Definition.__init__)


def test_astm_gastm_definition_constructor_args():
    sig = inspect.signature(astm_gastm_Definition.__init__)
    params = list(sig.parameters.keys())



def test_virtualspecification_is_not_abstract():
    assert not inspect.isabstract(VirtualSpecification)


def test_virtualspecification_constructor_exists():
    assert callable(VirtualSpecification.__init__)


def test_virtualspecification_constructor_args():
    sig = inspect.signature(VirtualSpecification.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_functionmemberattributes_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_FunctionMemberAttributes)


def test_astm_gastm_functionmemberattributes_constructor_exists():
    assert callable(astm_gastm_FunctionMemberAttributes.__init__)


def test_astm_gastm_functionmemberattributes_constructor_args():
    sig = inspect.signature(astm_gastm_FunctionMemberAttributes.__init__)
    params = list(sig.parameters.keys())
    assert "isThisConst" in params, "Missing parameter 'isThisConst'"
    assert "isInline" in params, "Missing parameter 'isInline'"
    assert "isFriend" in params, "Missing parameter 'isFriend'"

def test_astm_gastm_functionmemberattributes_has_isThisConst():
    assert hasattr(astm_gastm_FunctionMemberAttributes, "isThisConst")
    descriptor = None
    for klass in astm_gastm_FunctionMemberAttributes.__mro__:
        if "isThisConst" in klass.__dict__:
            descriptor = klass.__dict__["isThisConst"]
            break
    assert isinstance(descriptor, property)

def test_astm_gastm_functionmemberattributes_has_isInline():
    assert hasattr(astm_gastm_FunctionMemberAttributes, "isInline")
    descriptor = None
    for klass in astm_gastm_FunctionMemberAttributes.__mro__:
        if "isInline" in klass.__dict__:
            descriptor = klass.__dict__["isInline"]
            break
    assert isinstance(descriptor, property)

def test_astm_gastm_functionmemberattributes_has_isFriend():
    assert hasattr(astm_gastm_FunctionMemberAttributes, "isFriend")
    descriptor = None
    for klass in astm_gastm_FunctionMemberAttributes.__mro__:
        if "isFriend" in klass.__dict__:
            descriptor = klass.__dict__["isFriend"]
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



def test_astm_gastm_expressionstatement_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_ExpressionStatement)


def test_astm_gastm_expressionstatement_constructor_exists():
    assert callable(astm_gastm_ExpressionStatement.__init__)


def test_astm_gastm_expressionstatement_constructor_args():
    sig = inspect.signature(astm_gastm_ExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_ifstatement_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_IfStatement)


def test_astm_gastm_ifstatement_constructor_exists():
    assert callable(astm_gastm_IfStatement.__init__)


def test_astm_gastm_ifstatement_constructor_args():
    sig = inspect.signature(astm_gastm_IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_blockstatement_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_BlockStatement)


def test_astm_gastm_blockstatement_constructor_exists():
    assert callable(astm_gastm_BlockStatement.__init__)


def test_astm_gastm_blockstatement_constructor_args():
    sig = inspect.signature(astm_gastm_BlockStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_jumpstatement_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_JumpStatement)


def test_astm_gastm_jumpstatement_constructor_exists():
    assert callable(astm_gastm_JumpStatement.__init__)


def test_astm_gastm_jumpstatement_constructor_args():
    sig = inspect.signature(astm_gastm_JumpStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_breakstatement_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_BreakStatement)


def test_astm_gastm_breakstatement_constructor_exists():
    assert callable(astm_gastm_BreakStatement.__init__)


def test_astm_gastm_breakstatement_constructor_args():
    sig = inspect.signature(astm_gastm_BreakStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_deletestatement_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_DeleteStatement)


def test_astm_gastm_deletestatement_constructor_exists():
    assert callable(astm_gastm_DeleteStatement.__init__)


def test_astm_gastm_deletestatement_constructor_args():
    sig = inspect.signature(astm_gastm_DeleteStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_labeledstatement_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_LabeledStatement)


def test_astm_gastm_labeledstatement_constructor_exists():
    assert callable(astm_gastm_LabeledStatement.__init__)


def test_astm_gastm_labeledstatement_constructor_args():
    sig = inspect.signature(astm_gastm_LabeledStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_emptystatement_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_EmptyStatement)


def test_astm_gastm_emptystatement_constructor_exists():
    assert callable(astm_gastm_EmptyStatement.__init__)


def test_astm_gastm_emptystatement_constructor_args():
    sig = inspect.signature(astm_gastm_EmptyStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_continuestatement_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_ContinueStatement)


def test_astm_gastm_continuestatement_constructor_exists():
    assert callable(astm_gastm_ContinueStatement.__init__)


def test_astm_gastm_continuestatement_constructor_args():
    sig = inspect.signature(astm_gastm_ContinueStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_declarationordefinitionstatement_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_DeclarationOrDefinitionStatement)


def test_astm_gastm_declarationordefinitionstatement_constructor_exists():
    assert callable(astm_gastm_DeclarationOrDefinitionStatement.__init__)


def test_astm_gastm_declarationordefinitionstatement_constructor_args():
    sig = inspect.signature(astm_gastm_DeclarationOrDefinitionStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_trystatement_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_TryStatement)


def test_astm_gastm_trystatement_constructor_exists():
    assert callable(astm_gastm_TryStatement.__init__)


def test_astm_gastm_trystatement_constructor_args():
    sig = inspect.signature(astm_gastm_TryStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_switchstatement_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_SwitchStatement)


def test_astm_gastm_switchstatement_constructor_exists():
    assert callable(astm_gastm_SwitchStatement.__init__)


def test_astm_gastm_switchstatement_constructor_args():
    sig = inspect.signature(astm_gastm_SwitchStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_loopstatement_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_LoopStatement)


def test_astm_gastm_loopstatement_constructor_exists():
    assert callable(astm_gastm_LoopStatement.__init__)


def test_astm_gastm_loopstatement_constructor_args():
    sig = inspect.signature(astm_gastm_LoopStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_throwstatement_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_ThrowStatement)


def test_astm_gastm_throwstatement_constructor_exists():
    assert callable(astm_gastm_ThrowStatement.__init__)


def test_astm_gastm_throwstatement_constructor_args():
    sig = inspect.signature(astm_gastm_ThrowStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_returnstatement_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_ReturnStatement)


def test_astm_gastm_returnstatement_constructor_exists():
    assert callable(astm_gastm_ReturnStatement.__init__)


def test_astm_gastm_returnstatement_constructor_args():
    sig = inspect.signature(astm_gastm_ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_formalparameterdefinition_is_not_abstract():
    assert not inspect.isabstract(FormalParameterDefinition)


def test_formalparameterdefinition_constructor_exists():
    assert callable(FormalParameterDefinition.__init__)


def test_formalparameterdefinition_constructor_args():
    sig = inspect.signature(FormalParameterDefinition.__init__)
    params = list(sig.parameters.keys())



def test_delphiinterfacesection_is_not_abstract():
    assert not inspect.isabstract(DelphiInterfaceSection)


def test_delphiinterfacesection_constructor_exists():
    assert callable(DelphiInterfaceSection.__init__)


def test_delphiinterfacesection_constructor_args():
    sig = inspect.signature(DelphiInterfaceSection.__init__)
    params = list(sig.parameters.keys())



def test_functioncallexpression_is_not_abstract():
    assert not inspect.isabstract(FunctionCallExpression)


def test_functioncallexpression_constructor_exists():
    assert callable(FunctionCallExpression.__init__)


def test_functioncallexpression_constructor_args():
    sig = inspect.signature(FunctionCallExpression.__init__)
    params = list(sig.parameters.keys())



def test_astm_sastm_delphifunctioncallexpression_is_not_abstract():
    assert not inspect.isabstract(astm_sastm_DelphiFunctionCallExpression)


def test_astm_sastm_delphifunctioncallexpression_constructor_exists():
    assert callable(astm_sastm_DelphiFunctionCallExpression.__init__)


def test_astm_sastm_delphifunctioncallexpression_constructor_args():
    sig = inspect.signature(astm_sastm_DelphiFunctionCallExpression.__init__)
    params = list(sig.parameters.keys())



def test_blockstatement_is_not_abstract():
    assert not inspect.isabstract(BlockStatement)


def test_blockstatement_constructor_exists():
    assert callable(BlockStatement.__init__)


def test_blockstatement_constructor_args():
    sig = inspect.signature(BlockStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm_sastm_delphiwithstatement_is_not_abstract():
    assert not inspect.isabstract(astm_sastm_DelphiWithStatement)


def test_astm_sastm_delphiwithstatement_constructor_exists():
    assert callable(astm_sastm_DelphiWithStatement.__init__)


def test_astm_sastm_delphiwithstatement_constructor_args():
    sig = inspect.signature(astm_sastm_DelphiWithStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm_sastm_delphiblockstatement_is_not_abstract():
    assert not inspect.isabstract(astm_sastm_DelphiBlockStatement)


def test_astm_sastm_delphiblockstatement_constructor_exists():
    assert callable(astm_sastm_DelphiBlockStatement.__init__)


def test_astm_sastm_delphiblockstatement_constructor_args():
    sig = inspect.signature(astm_sastm_DelphiBlockStatement.__init__)
    params = list(sig.parameters.keys())



def test_namedtypereference_is_not_abstract():
    assert not inspect.isabstract(NamedTypeReference)


def test_namedtypereference_constructor_exists():
    assert callable(NamedTypeReference.__init__)


def test_namedtypereference_constructor_args():
    sig = inspect.signature(NamedTypeReference.__init__)
    params = list(sig.parameters.keys())



def test_delphiimplementationsection_is_not_abstract():
    assert not inspect.isabstract(DelphiImplementationSection)


def test_delphiimplementationsection_constructor_exists():
    assert callable(DelphiImplementationSection.__init__)


def test_delphiimplementationsection_constructor_args():
    sig = inspect.signature(DelphiImplementationSection.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_multiply_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_Multiply)


def test_astm_gastm_multiply_constructor_exists():
    assert callable(astm_gastm_Multiply.__init__)


def test_astm_gastm_multiply_constructor_args():
    sig = inspect.signature(astm_gastm_Multiply.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_subtract_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_Subtract)


def test_astm_gastm_subtract_constructor_exists():
    assert callable(astm_gastm_Subtract.__init__)


def test_astm_gastm_subtract_constructor_args():
    sig = inspect.signature(astm_gastm_Subtract.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_add_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_Add)


def test_astm_gastm_add_constructor_exists():
    assert callable(astm_gastm_Add.__init__)


def test_astm_gastm_add_constructor_args():
    sig = inspect.signature(astm_gastm_Add.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_specificselectstatement_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_SpecificSelectStatement)


def test_astm_gastm_specificselectstatement_constructor_exists():
    assert callable(astm_gastm_SpecificSelectStatement.__init__)


def test_astm_gastm_specificselectstatement_constructor_args():
    sig = inspect.signature(astm_gastm_SpecificSelectStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_specificconcatstring_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_SpecificConcatString)


def test_astm_gastm_specificconcatstring_constructor_exists():
    assert callable(astm_gastm_SpecificConcatString.__init__)


def test_astm_gastm_specificconcatstring_constructor_args():
    sig = inspect.signature(astm_gastm_SpecificConcatString.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_specificlike_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_SpecificLike)


def test_astm_gastm_specificlike_constructor_exists():
    assert callable(astm_gastm_SpecificLike.__init__)


def test_astm_gastm_specificlike_constructor_args():
    sig = inspect.signature(astm_gastm_SpecificLike.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_specificin_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_SpecificIn)


def test_astm_gastm_specificin_constructor_exists():
    assert callable(astm_gastm_SpecificIn.__init__)


def test_astm_gastm_specificin_constructor_args():
    sig = inspect.signature(astm_gastm_SpecificIn.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_specificgreaterequal_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_SpecificGreaterEqual)


def test_astm_gastm_specificgreaterequal_constructor_exists():
    assert callable(astm_gastm_SpecificGreaterEqual.__init__)


def test_astm_gastm_specificgreaterequal_constructor_args():
    sig = inspect.signature(astm_gastm_SpecificGreaterEqual.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_specificlessequal_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_SpecificLessEqual)


def test_astm_gastm_specificlessequal_constructor_exists():
    assert callable(astm_gastm_SpecificLessEqual.__init__)


def test_astm_gastm_specificlessequal_constructor_args():
    sig = inspect.signature(astm_gastm_SpecificLessEqual.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_specifictriggerdefinition_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_SpecificTriggerDefinition)


def test_astm_gastm_specifictriggerdefinition_constructor_exists():
    assert callable(astm_gastm_SpecificTriggerDefinition.__init__)


def test_astm_gastm_specifictriggerdefinition_constructor_args():
    sig = inspect.signature(astm_gastm_SpecificTriggerDefinition.__init__)
    params = list(sig.parameters.keys())



def test_actualparameterexpression_is_not_abstract():
    assert not inspect.isabstract(ActualParameterExpression)


def test_actualparameterexpression_constructor_exists():
    assert callable(ActualParameterExpression.__init__)


def test_actualparameterexpression_constructor_args():
    sig = inspect.signature(ActualParameterExpression.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_byreferenceactualparameterexpression_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_ByReferenceActualParameterExpression)


def test_astm_gastm_byreferenceactualparameterexpression_constructor_exists():
    assert callable(astm_gastm_ByReferenceActualParameterExpression.__init__)


def test_astm_gastm_byreferenceactualparameterexpression_constructor_args():
    sig = inspect.signature(astm_gastm_ByReferenceActualParameterExpression.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_byvalueactualparameterexpression_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_ByValueActualParameterExpression)


def test_astm_gastm_byvalueactualparameterexpression_constructor_exists():
    assert callable(astm_gastm_ByValueActualParameterExpression.__init__)


def test_astm_gastm_byvalueactualparameterexpression_constructor_args():
    sig = inspect.signature(astm_gastm_ByValueActualParameterExpression.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_missingactualparameter_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_MissingActualParameter)


def test_astm_gastm_missingactualparameter_constructor_exists():
    assert callable(astm_gastm_MissingActualParameter.__init__)


def test_astm_gastm_missingactualparameter_constructor_args():
    sig = inspect.signature(astm_gastm_MissingActualParameter.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_assign_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_Assign)


def test_astm_gastm_assign_constructor_exists():
    assert callable(astm_gastm_Assign.__init__)


def test_astm_gastm_assign_constructor_args():
    sig = inspect.signature(astm_gastm_Assign.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_bitrightshift_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_BitRightShift)


def test_astm_gastm_bitrightshift_constructor_exists():
    assert callable(astm_gastm_BitRightShift.__init__)


def test_astm_gastm_bitrightshift_constructor_args():
    sig = inspect.signature(astm_gastm_BitRightShift.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_bitleftshift_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_BitLeftShift)


def test_astm_gastm_bitleftshift_constructor_exists():
    assert callable(astm_gastm_BitLeftShift.__init__)


def test_astm_gastm_bitleftshift_constructor_args():
    sig = inspect.signature(astm_gastm_BitLeftShift.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_bitxor_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_BitXor)


def test_astm_gastm_bitxor_constructor_exists():
    assert callable(astm_gastm_BitXor.__init__)


def test_astm_gastm_bitxor_constructor_args():
    sig = inspect.signature(astm_gastm_BitXor.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_bitor_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_BitOr)


def test_astm_gastm_bitor_constructor_exists():
    assert callable(astm_gastm_BitOr.__init__)


def test_astm_gastm_bitor_constructor_args():
    sig = inspect.signature(astm_gastm_BitOr.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_bitand_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_BitAnd)


def test_astm_gastm_bitand_constructor_exists():
    assert callable(astm_gastm_BitAnd.__init__)


def test_astm_gastm_bitand_constructor_args():
    sig = inspect.signature(astm_gastm_BitAnd.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_notless_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_NotLess)


def test_astm_gastm_notless_constructor_exists():
    assert callable(astm_gastm_NotLess.__init__)


def test_astm_gastm_notless_constructor_args():
    sig = inspect.signature(astm_gastm_NotLess.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_less_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_Less)


def test_astm_gastm_less_constructor_exists():
    assert callable(astm_gastm_Less.__init__)


def test_astm_gastm_less_constructor_args():
    sig = inspect.signature(astm_gastm_Less.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_notgreater_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_NotGreater)


def test_astm_gastm_notgreater_constructor_exists():
    assert callable(astm_gastm_NotGreater.__init__)


def test_astm_gastm_notgreater_constructor_args():
    sig = inspect.signature(astm_gastm_NotGreater.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_greater_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_Greater)


def test_astm_gastm_greater_constructor_exists():
    assert callable(astm_gastm_Greater.__init__)


def test_astm_gastm_greater_constructor_args():
    sig = inspect.signature(astm_gastm_Greater.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_notequal_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_NotEqual)


def test_astm_gastm_notequal_constructor_exists():
    assert callable(astm_gastm_NotEqual.__init__)


def test_astm_gastm_notequal_constructor_args():
    sig = inspect.signature(astm_gastm_NotEqual.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_equal_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_Equal)


def test_astm_gastm_equal_constructor_exists():
    assert callable(astm_gastm_Equal.__init__)


def test_astm_gastm_equal_constructor_args():
    sig = inspect.signature(astm_gastm_Equal.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_or_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_Or)


def test_astm_gastm_or_constructor_exists():
    assert callable(astm_gastm_Or.__init__)


def test_astm_gastm_or_constructor_args():
    sig = inspect.signature(astm_gastm_Or.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_and_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_And)


def test_astm_gastm_and_constructor_exists():
    assert callable(astm_gastm_And.__init__)


def test_astm_gastm_and_constructor_args():
    sig = inspect.signature(astm_gastm_And.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_exponent_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_Exponent)


def test_astm_gastm_exponent_constructor_exists():
    assert callable(astm_gastm_Exponent.__init__)


def test_astm_gastm_exponent_constructor_args():
    sig = inspect.signature(astm_gastm_Exponent.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_modulus_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_Modulus)


def test_astm_gastm_modulus_constructor_exists():
    assert callable(astm_gastm_Modulus.__init__)


def test_astm_gastm_modulus_constructor_args():
    sig = inspect.signature(astm_gastm_Modulus.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_divide_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_Divide)


def test_astm_gastm_divide_constructor_exists():
    assert callable(astm_gastm_Divide.__init__)


def test_astm_gastm_divide_constructor_args():
    sig = inspect.signature(astm_gastm_Divide.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_pointertype_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_PointerType)


def test_astm_gastm_pointertype_constructor_exists():
    assert callable(astm_gastm_PointerType.__init__)


def test_astm_gastm_pointertype_constructor_args():
    sig = inspect.signature(astm_gastm_PointerType.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_collectiontype_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_CollectionType)


def test_astm_gastm_collectiontype_constructor_exists():
    assert callable(astm_gastm_CollectionType.__init__)


def test_astm_gastm_collectiontype_constructor_args():
    sig = inspect.signature(astm_gastm_CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_unaryoperator_is_not_abstract():
    assert not inspect.isabstract(UnaryOperator)


def test_unaryoperator_constructor_exists():
    assert callable(UnaryOperator.__init__)


def test_unaryoperator_constructor_args():
    sig = inspect.signature(UnaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_not_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_Not)


def test_astm_gastm_not_constructor_exists():
    assert callable(astm_gastm_Not.__init__)


def test_astm_gastm_not_constructor_args():
    sig = inspect.signature(astm_gastm_Not.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_bitnot_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_BitNot)


def test_astm_gastm_bitnot_constructor_exists():
    assert callable(astm_gastm_BitNot.__init__)


def test_astm_gastm_bitnot_constructor_args():
    sig = inspect.signature(astm_gastm_BitNot.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_increment_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_Increment)


def test_astm_gastm_increment_constructor_exists():
    assert callable(astm_gastm_Increment.__init__)


def test_astm_gastm_increment_constructor_args():
    sig = inspect.signature(astm_gastm_Increment.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_decrement_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_Decrement)


def test_astm_gastm_decrement_constructor_exists():
    assert callable(astm_gastm_Decrement.__init__)


def test_astm_gastm_decrement_constructor_args():
    sig = inspect.signature(astm_gastm_Decrement.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_postdecrement_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_PostDecrement)


def test_astm_gastm_postdecrement_constructor_exists():
    assert callable(astm_gastm_PostDecrement.__init__)


def test_astm_gastm_postdecrement_constructor_args():
    sig = inspect.signature(astm_gastm_PostDecrement.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_negate_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_Negate)


def test_astm_gastm_negate_constructor_exists():
    assert callable(astm_gastm_Negate.__init__)


def test_astm_gastm_negate_constructor_args():
    sig = inspect.signature(astm_gastm_Negate.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_addressof_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_AddressOf)


def test_astm_gastm_addressof_constructor_exists():
    assert callable(astm_gastm_AddressOf.__init__)


def test_astm_gastm_addressof_constructor_args():
    sig = inspect.signature(astm_gastm_AddressOf.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_postincrement_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_PostIncrement)


def test_astm_gastm_postincrement_constructor_exists():
    assert callable(astm_gastm_PostIncrement.__init__)


def test_astm_gastm_postincrement_constructor_args():
    sig = inspect.signature(astm_gastm_PostIncrement.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_deref_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_Deref)


def test_astm_gastm_deref_constructor_exists():
    assert callable(astm_gastm_Deref.__init__)


def test_astm_gastm_deref_constructor_args():
    sig = inspect.signature(astm_gastm_Deref.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_unaryplus_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_UnaryPlus)


def test_astm_gastm_unaryplus_constructor_exists():
    assert callable(astm_gastm_UnaryPlus.__init__)


def test_astm_gastm_unaryplus_constructor_args():
    sig = inspect.signature(astm_gastm_UnaryPlus.__init__)
    params = list(sig.parameters.keys())



def test_literal_is_not_abstract():
    assert not inspect.isabstract(Literal)


def test_literal_constructor_exists():
    assert callable(Literal.__init__)


def test_literal_constructor_args():
    sig = inspect.signature(Literal.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_realliteral_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_RealLiteral)


def test_astm_gastm_realliteral_constructor_exists():
    assert callable(astm_gastm_RealLiteral.__init__)


def test_astm_gastm_realliteral_constructor_args():
    sig = inspect.signature(astm_gastm_RealLiteral.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_stringliteral_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_StringLiteral)


def test_astm_gastm_stringliteral_constructor_exists():
    assert callable(astm_gastm_StringLiteral.__init__)


def test_astm_gastm_stringliteral_constructor_args():
    sig = inspect.signature(astm_gastm_StringLiteral.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_booleanliteral_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_BooleanLiteral)


def test_astm_gastm_booleanliteral_constructor_exists():
    assert callable(astm_gastm_BooleanLiteral.__init__)


def test_astm_gastm_booleanliteral_constructor_args():
    sig = inspect.signature(astm_gastm_BooleanLiteral.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_bitliteral_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_BitLiteral)


def test_astm_gastm_bitliteral_constructor_exists():
    assert callable(astm_gastm_BitLiteral.__init__)


def test_astm_gastm_bitliteral_constructor_args():
    sig = inspect.signature(astm_gastm_BitLiteral.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_charliteral_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_CharLiteral)


def test_astm_gastm_charliteral_constructor_exists():
    assert callable(astm_gastm_CharLiteral.__init__)


def test_astm_gastm_charliteral_constructor_args():
    sig = inspect.signature(astm_gastm_CharLiteral.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_integerliteral_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_IntegerLiteral)


def test_astm_gastm_integerliteral_constructor_exists():
    assert callable(astm_gastm_IntegerLiteral.__init__)


def test_astm_gastm_integerliteral_constructor_args():
    sig = inspect.signature(astm_gastm_IntegerLiteral.__init__)
    params = list(sig.parameters.keys())



def test_qualifiedidentifierreference_is_not_abstract():
    assert not inspect.isabstract(QualifiedIdentifierReference)


def test_qualifiedidentifierreference_constructor_exists():
    assert callable(QualifiedIdentifierReference.__init__)


def test_qualifiedidentifierreference_constructor_args():
    sig = inspect.signature(QualifiedIdentifierReference.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_qualifiedoverdata_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_QualifiedOverData)


def test_astm_gastm_qualifiedoverdata_constructor_exists():
    assert callable(astm_gastm_QualifiedOverData.__init__)


def test_astm_gastm_qualifiedoverdata_constructor_args():
    sig = inspect.signature(astm_gastm_QualifiedOverData.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_qualifiedoverpointer_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_QualifiedOverPointer)


def test_astm_gastm_qualifiedoverpointer_constructor_exists():
    assert callable(astm_gastm_QualifiedOverPointer.__init__)


def test_astm_gastm_qualifiedoverpointer_constructor_args():
    sig = inspect.signature(astm_gastm_QualifiedOverPointer.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_aggregateexpression_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_AggregateExpression)


def test_astm_gastm_aggregateexpression_constructor_exists():
    assert callable(astm_gastm_AggregateExpression.__init__)


def test_astm_gastm_aggregateexpression_constructor_args():
    sig = inspect.signature(astm_gastm_AggregateExpression.__init__)
    params = list(sig.parameters.keys())



def test_forstatement_is_not_abstract():
    assert not inspect.isabstract(ForStatement)


def test_forstatement_constructor_exists():
    assert callable(ForStatement.__init__)


def test_forstatement_constructor_args():
    sig = inspect.signature(ForStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_forcheckafterstatement_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_ForCheckAfterStatement)


def test_astm_gastm_forcheckafterstatement_constructor_exists():
    assert callable(astm_gastm_ForCheckAfterStatement.__init__)


def test_astm_gastm_forcheckafterstatement_constructor_args():
    sig = inspect.signature(astm_gastm_ForCheckAfterStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_forcheckbeforestatement_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_ForCheckBeforeStatement)


def test_astm_gastm_forcheckbeforestatement_constructor_exists():
    assert callable(astm_gastm_ForCheckBeforeStatement.__init__)


def test_astm_gastm_forcheckbeforestatement_constructor_args():
    sig = inspect.signature(astm_gastm_ForCheckBeforeStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_dowhilestatement_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_DoWhileStatement)


def test_astm_gastm_dowhilestatement_constructor_exists():
    assert callable(astm_gastm_DoWhileStatement.__init__)


def test_astm_gastm_dowhilestatement_constructor_args():
    sig = inspect.signature(astm_gastm_DoWhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_whilestatement_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_WhileStatement)


def test_astm_gastm_whilestatement_constructor_exists():
    assert callable(astm_gastm_WhileStatement.__init__)


def test_astm_gastm_whilestatement_constructor_args():
    sig = inspect.signature(astm_gastm_WhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_defaultblock_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_DefaultBlock)


def test_astm_gastm_defaultblock_constructor_exists():
    assert callable(astm_gastm_DefaultBlock.__init__)


def test_astm_gastm_defaultblock_constructor_args():
    sig = inspect.signature(astm_gastm_DefaultBlock.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_terminatestatement_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_TerminateStatement)


def test_astm_gastm_terminatestatement_constructor_exists():
    assert callable(astm_gastm_TerminateStatement.__init__)


def test_astm_gastm_terminatestatement_constructor_args():
    sig = inspect.signature(astm_gastm_TerminateStatement.__init__)
    params = list(sig.parameters.keys())



def test_accesskind_is_not_abstract():
    assert not inspect.isabstract(AccessKind)


def test_accesskind_constructor_exists():
    assert callable(AccessKind.__init__)


def test_accesskind_constructor_args():
    sig = inspect.signature(AccessKind.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_private_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_Private)


def test_astm_gastm_private_constructor_exists():
    assert callable(astm_gastm_Private.__init__)


def test_astm_gastm_private_constructor_args():
    sig = inspect.signature(astm_gastm_Private.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_protected_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_Protected)


def test_astm_gastm_protected_constructor_exists():
    assert callable(astm_gastm_Protected.__init__)


def test_astm_gastm_protected_constructor_args():
    sig = inspect.signature(astm_gastm_Protected.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_public_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_Public)


def test_astm_gastm_public_constructor_exists():
    assert callable(astm_gastm_Public.__init__)


def test_astm_gastm_public_constructor_args():
    sig = inspect.signature(astm_gastm_Public.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_byreferenceformalparametertype_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_ByReferenceFormalParameterType)


def test_astm_gastm_byreferenceformalparametertype_constructor_exists():
    assert callable(astm_gastm_ByReferenceFormalParameterType.__init__)


def test_astm_gastm_byreferenceformalparametertype_constructor_args():
    sig = inspect.signature(astm_gastm_ByReferenceFormalParameterType.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_byvalueformalparametertype_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_ByValueFormalParameterType)


def test_astm_gastm_byvalueformalparametertype_constructor_exists():
    assert callable(astm_gastm_ByValueFormalParameterType.__init__)


def test_astm_gastm_byvalueformalparametertype_constructor_args():
    sig = inspect.signature(astm_gastm_ByValueFormalParameterType.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_annotationtype_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_AnnotationType)


def test_astm_gastm_annotationtype_constructor_exists():
    assert callable(astm_gastm_AnnotationType.__init__)


def test_astm_gastm_annotationtype_constructor_args():
    sig = inspect.signature(astm_gastm_AnnotationType.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_uniontype_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_UnionType)


def test_astm_gastm_uniontype_constructor_exists():
    assert callable(astm_gastm_UnionType.__init__)


def test_astm_gastm_uniontype_constructor_args():
    sig = inspect.signature(astm_gastm_UnionType.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_structuretype_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_StructureType)


def test_astm_gastm_structuretype_constructor_exists():
    assert callable(astm_gastm_StructureType.__init__)


def test_astm_gastm_structuretype_constructor_args():
    sig = inspect.signature(astm_gastm_StructureType.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_rangetype_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_RangeType)


def test_astm_gastm_rangetype_constructor_exists():
    assert callable(astm_gastm_RangeType.__init__)


def test_astm_gastm_rangetype_constructor_args():
    sig = inspect.signature(astm_gastm_RangeType.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_referencetype_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_ReferenceType)


def test_astm_gastm_referencetype_constructor_exists():
    assert callable(astm_gastm_ReferenceType.__init__)


def test_astm_gastm_referencetype_constructor_args():
    sig = inspect.signature(astm_gastm_ReferenceType.__init__)
    params = list(sig.parameters.keys())



def test_primitivetype_is_not_abstract():
    assert not inspect.isabstract(PrimitiveType)


def test_primitivetype_constructor_exists():
    assert callable(PrimitiveType.__init__)


def test_primitivetype_constructor_args():
    sig = inspect.signature(PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_longinteger_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_LongInteger)


def test_astm_gastm_longinteger_constructor_exists():
    assert callable(astm_gastm_LongInteger.__init__)


def test_astm_gastm_longinteger_constructor_args():
    sig = inspect.signature(astm_gastm_LongInteger.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_byte_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_Byte)


def test_astm_gastm_byte_constructor_exists():
    assert callable(astm_gastm_Byte.__init__)


def test_astm_gastm_byte_constructor_args():
    sig = inspect.signature(astm_gastm_Byte.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_longdouble_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_LongDouble)


def test_astm_gastm_longdouble_constructor_exists():
    assert callable(astm_gastm_LongDouble.__init__)


def test_astm_gastm_longdouble_constructor_args():
    sig = inspect.signature(astm_gastm_LongDouble.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_string_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_String)


def test_astm_gastm_string_constructor_exists():
    assert callable(astm_gastm_String.__init__)


def test_astm_gastm_string_constructor_args():
    sig = inspect.signature(astm_gastm_String.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_float_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_Float)


def test_astm_gastm_float_constructor_exists():
    assert callable(astm_gastm_Float.__init__)


def test_astm_gastm_float_constructor_args():
    sig = inspect.signature(astm_gastm_Float.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_character_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_Character)


def test_astm_gastm_character_constructor_exists():
    assert callable(astm_gastm_Character.__init__)


def test_astm_gastm_character_constructor_args():
    sig = inspect.signature(astm_gastm_Character.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_boolean_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_Boolean)


def test_astm_gastm_boolean_constructor_exists():
    assert callable(astm_gastm_Boolean.__init__)


def test_astm_gastm_boolean_constructor_args():
    sig = inspect.signature(astm_gastm_Boolean.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_shortinteger_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_ShortInteger)


def test_astm_gastm_shortinteger_constructor_exists():
    assert callable(astm_gastm_ShortInteger.__init__)


def test_astm_gastm_shortinteger_constructor_args():
    sig = inspect.signature(astm_gastm_ShortInteger.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_integer_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_Integer)


def test_astm_gastm_integer_constructor_exists():
    assert callable(astm_gastm_Integer.__init__)


def test_astm_gastm_integer_constructor_args():
    sig = inspect.signature(astm_gastm_Integer.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_widecharacter_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_WideCharacter)


def test_astm_gastm_widecharacter_constructor_exists():
    assert callable(astm_gastm_WideCharacter.__init__)


def test_astm_gastm_widecharacter_constructor_args():
    sig = inspect.signature(astm_gastm_WideCharacter.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_double_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_Double)


def test_astm_gastm_double_constructor_exists():
    assert callable(astm_gastm_Double.__init__)


def test_astm_gastm_double_constructor_args():
    sig = inspect.signature(astm_gastm_Double.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_void_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_Void)


def test_astm_gastm_void_constructor_exists():
    assert callable(astm_gastm_Void.__init__)


def test_astm_gastm_void_constructor_args():
    sig = inspect.signature(astm_gastm_Void.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_exceptiontype_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_ExceptionType)


def test_astm_gastm_exceptiontype_constructor_exists():
    assert callable(astm_gastm_ExceptionType.__init__)


def test_astm_gastm_exceptiontype_constructor_args():
    sig = inspect.signature(astm_gastm_ExceptionType.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_nonvirtual_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_NonVirtual)


def test_astm_gastm_nonvirtual_constructor_exists():
    assert callable(astm_gastm_NonVirtual.__init__)


def test_astm_gastm_nonvirtual_constructor_args():
    sig = inspect.signature(astm_gastm_NonVirtual.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_purevirtual_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_PureVirtual)


def test_astm_gastm_purevirtual_constructor_exists():
    assert callable(astm_gastm_PureVirtual.__init__)


def test_astm_gastm_purevirtual_constructor_args():
    sig = inspect.signature(astm_gastm_PureVirtual.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_virtual_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_Virtual)


def test_astm_gastm_virtual_constructor_exists():
    assert callable(astm_gastm_Virtual.__init__)


def test_astm_gastm_virtual_constructor_args():
    sig = inspect.signature(astm_gastm_Virtual.__init__)
    params = list(sig.parameters.keys())



def test_storagespecification_is_not_abstract():
    assert not inspect.isabstract(StorageSpecification)


def test_storagespecification_constructor_exists():
    assert callable(StorageSpecification.__init__)


def test_storagespecification_constructor_args():
    sig = inspect.signature(StorageSpecification.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_nodef_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_NoDef)


def test_astm_gastm_nodef_constructor_exists():
    assert callable(astm_gastm_NoDef.__init__)


def test_astm_gastm_nodef_constructor_args():
    sig = inspect.signature(astm_gastm_NoDef.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_functionpersistent_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_FunctionPersistent)


def test_astm_gastm_functionpersistent_constructor_exists():
    assert callable(astm_gastm_FunctionPersistent.__init__)


def test_astm_gastm_functionpersistent_constructor_args():
    sig = inspect.signature(astm_gastm_FunctionPersistent.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_perclassmember_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_PerClassMember)


def test_astm_gastm_perclassmember_constructor_exists():
    assert callable(astm_gastm_PerClassMember.__init__)


def test_astm_gastm_perclassmember_constructor_args():
    sig = inspect.signature(astm_gastm_PerClassMember.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_filelocal_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_FileLocal)


def test_astm_gastm_filelocal_constructor_exists():
    assert callable(astm_gastm_FileLocal.__init__)


def test_astm_gastm_filelocal_constructor_args():
    sig = inspect.signature(astm_gastm_FileLocal.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_external_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_External)


def test_astm_gastm_external_constructor_exists():
    assert callable(astm_gastm_External.__init__)


def test_astm_gastm_external_constructor_args():
    sig = inspect.signature(astm_gastm_External.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_variabledefinition_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_VariableDefinition)


def test_astm_gastm_variabledefinition_constructor_exists():
    assert callable(astm_gastm_VariableDefinition.__init__)


def test_astm_gastm_variabledefinition_constructor_args():
    sig = inspect.signature(astm_gastm_VariableDefinition.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_formalparameterdefinition_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_FormalParameterDefinition)


def test_astm_gastm_formalparameterdefinition_constructor_exists():
    assert callable(astm_gastm_FormalParameterDefinition.__init__)


def test_astm_gastm_formalparameterdefinition_constructor_args():
    sig = inspect.signature(astm_gastm_FormalParameterDefinition.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_identifierreference_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_IdentifierReference)


def test_astm_gastm_identifierreference_constructor_exists():
    assert callable(astm_gastm_IdentifierReference.__init__)


def test_astm_gastm_identifierreference_constructor_args():
    sig = inspect.signature(astm_gastm_IdentifierReference.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_functiondefinition_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_FunctionDefinition)


def test_astm_gastm_functiondefinition_constructor_exists():
    assert callable(astm_gastm_FunctionDefinition.__init__)


def test_astm_gastm_functiondefinition_constructor_args():
    sig = inspect.signature(astm_gastm_FunctionDefinition.__init__)
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



def test_astm_gastm_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_VariableDeclaration)


def test_astm_gastm_variabledeclaration_constructor_exists():
    assert callable(astm_gastm_VariableDeclaration.__init__)


def test_astm_gastm_variabledeclaration_constructor_args():
    sig = inspect.signature(astm_gastm_VariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "isMutable" in params, "Missing parameter 'isMutable'"

def test_astm_gastm_variabledeclaration_has_isMutable():
    assert hasattr(astm_gastm_VariableDeclaration, "isMutable")
    descriptor = None
    for klass in astm_gastm_VariableDeclaration.__mro__:
        if "isMutable" in klass.__dict__:
            descriptor = klass.__dict__["isMutable"]
            break
    assert isinstance(descriptor, property)



def test_astm_gastm_formalparameterdeclaration_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_FormalParameterDeclaration)


def test_astm_gastm_formalparameterdeclaration_constructor_exists():
    assert callable(astm_gastm_FormalParameterDeclaration.__init__)


def test_astm_gastm_formalparameterdeclaration_constructor_args():
    sig = inspect.signature(astm_gastm_FormalParameterDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_functiondeclaration_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_FunctionDeclaration)


def test_astm_gastm_functiondeclaration_constructor_exists():
    assert callable(astm_gastm_FunctionDeclaration.__init__)


def test_astm_gastm_functiondeclaration_constructor_args():
    sig = inspect.signature(astm_gastm_FunctionDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_sourcefile_is_not_abstract():
    assert not inspect.isabstract(SourceFile)


def test_sourcefile_constructor_exists():
    assert callable(SourceFile.__init__)


def test_sourcefile_constructor_args():
    sig = inspect.signature(SourceFile.__init__)
    params = list(sig.parameters.keys())



def test_gastmsourceobject_is_not_abstract():
    assert not inspect.isabstract(GASTMSourceObject)


def test_gastmsourceobject_constructor_exists():
    assert callable(GASTMSourceObject.__init__)


def test_gastmsourceobject_constructor_args():
    sig = inspect.signature(GASTMSourceObject.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_sourcelocation_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_SourceLocation)


def test_astm_gastm_sourcelocation_constructor_exists():
    assert callable(astm_gastm_SourceLocation.__init__)


def test_astm_gastm_sourcelocation_constructor_args():
    sig = inspect.signature(astm_gastm_SourceLocation.__init__)
    params = list(sig.parameters.keys())
    assert "startColumn" in params, "Missing parameter 'startColumn'"
    assert "startLine" in params, "Missing parameter 'startLine'"
    assert "endLine" in params, "Missing parameter 'endLine'"
    assert "endColumn" in params, "Missing parameter 'endColumn'"

def test_astm_gastm_sourcelocation_has_startColumn():
    assert hasattr(astm_gastm_SourceLocation, "startColumn")
    descriptor = None
    for klass in astm_gastm_SourceLocation.__mro__:
        if "startColumn" in klass.__dict__:
            descriptor = klass.__dict__["startColumn"]
            break
    assert isinstance(descriptor, property)

def test_astm_gastm_sourcelocation_has_startLine():
    assert hasattr(astm_gastm_SourceLocation, "startLine")
    descriptor = None
    for klass in astm_gastm_SourceLocation.__mro__:
        if "startLine" in klass.__dict__:
            descriptor = klass.__dict__["startLine"]
            break
    assert isinstance(descriptor, property)

def test_astm_gastm_sourcelocation_has_endLine():
    assert hasattr(astm_gastm_SourceLocation, "endLine")
    descriptor = None
    for klass in astm_gastm_SourceLocation.__mro__:
        if "endLine" in klass.__dict__:
            descriptor = klass.__dict__["endLine"]
            break
    assert isinstance(descriptor, property)

def test_astm_gastm_sourcelocation_has_endColumn():
    assert hasattr(astm_gastm_SourceLocation, "endColumn")
    descriptor = None
    for klass in astm_gastm_SourceLocation.__mro__:
        if "endColumn" in klass.__dict__:
            descriptor = klass.__dict__["endColumn"]
            break
    assert isinstance(descriptor, property)



def test_astm_gastm_sourcefile_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_SourceFile)


def test_astm_gastm_sourcefile_constructor_exists():
    assert callable(astm_gastm_SourceFile.__init__)


def test_astm_gastm_sourcefile_constructor_args():
    sig = inspect.signature(astm_gastm_SourceFile.__init__)
    params = list(sig.parameters.keys())
    assert "pathName" in params, "Missing parameter 'pathName'"

def test_astm_gastm_sourcefile_has_pathName():
    assert hasattr(astm_gastm_SourceFile, "pathName")
    descriptor = None
    for klass in astm_gastm_SourceFile.__mro__:
        if "pathName" in klass.__dict__:
            descriptor = klass.__dict__["pathName"]
            break
    assert isinstance(descriptor, property)



def test_astm_gastm_actualparameter_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_ActualParameter)


def test_astm_gastm_actualparameter_constructor_exists():
    assert callable(astm_gastm_ActualParameter.__init__)


def test_astm_gastm_actualparameter_constructor_args():
    sig = inspect.signature(astm_gastm_ActualParameter.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_binaryoperator_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_BinaryOperator)


def test_astm_gastm_binaryoperator_constructor_exists():
    assert callable(astm_gastm_BinaryOperator.__init__)


def test_astm_gastm_binaryoperator_constructor_args():
    sig = inspect.signature(astm_gastm_BinaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_unaryoperator_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_UnaryOperator)


def test_astm_gastm_unaryoperator_constructor_exists():
    assert callable(astm_gastm_UnaryOperator.__init__)


def test_astm_gastm_unaryoperator_constructor_args():
    sig = inspect.signature(astm_gastm_UnaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_accesskind_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_AccessKind)


def test_astm_gastm_accesskind_constructor_exists():
    assert callable(astm_gastm_AccessKind.__init__)


def test_astm_gastm_accesskind_constructor_args():
    sig = inspect.signature(astm_gastm_AccessKind.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_functiontype_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_FunctionType)


def test_astm_gastm_functiontype_constructor_exists():
    assert callable(astm_gastm_FunctionType.__init__)


def test_astm_gastm_functiontype_constructor_args():
    sig = inspect.signature(astm_gastm_FunctionType.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_labeltype_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_LabelType)


def test_astm_gastm_labeltype_constructor_exists():
    assert callable(astm_gastm_LabelType.__init__)


def test_astm_gastm_labeltype_constructor_args():
    sig = inspect.signature(astm_gastm_LabelType.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_namespacetype_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_NameSpaceType)


def test_astm_gastm_namespacetype_constructor_exists():
    assert callable(astm_gastm_NameSpaceType.__init__)


def test_astm_gastm_namespacetype_constructor_args():
    sig = inspect.signature(astm_gastm_NameSpaceType.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_typereference_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_TypeReference)


def test_astm_gastm_typereference_constructor_exists():
    assert callable(astm_gastm_TypeReference.__init__)


def test_astm_gastm_typereference_constructor_args():
    sig = inspect.signature(astm_gastm_TypeReference.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_datatype_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_DataType)


def test_astm_gastm_datatype_constructor_exists():
    assert callable(astm_gastm_DataType.__init__)


def test_astm_gastm_datatype_constructor_args():
    sig = inspect.signature(astm_gastm_DataType.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_storagespecification_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_StorageSpecification)


def test_astm_gastm_storagespecification_constructor_exists():
    assert callable(astm_gastm_StorageSpecification.__init__)


def test_astm_gastm_storagespecification_constructor_args():
    sig = inspect.signature(astm_gastm_StorageSpecification.__init__)
    params = list(sig.parameters.keys())



def test_gastmsyntaxobject_is_not_abstract():
    assert not inspect.isabstract(GASTMSyntaxObject)


def test_gastmsyntaxobject_constructor_exists():
    assert callable(GASTMSyntaxObject.__init__)


def test_gastmsyntaxobject_constructor_args():
    sig = inspect.signature(GASTMSyntaxObject.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_preprocessorelement_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_PreprocessorElement)


def test_astm_gastm_preprocessorelement_constructor_exists():
    assert callable(astm_gastm_PreprocessorElement.__init__)


def test_astm_gastm_preprocessorelement_constructor_args():
    sig = inspect.signature(astm_gastm_PreprocessorElement.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_type_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_Type)


def test_astm_gastm_type_constructor_exists():
    assert callable(astm_gastm_Type.__init__)


def test_astm_gastm_type_constructor_args():
    sig = inspect.signature(astm_gastm_Type.__init__)
    params = list(sig.parameters.keys())
    assert "isConst" in params, "Missing parameter 'isConst'"
    assert "isVolatile" in params, "Missing parameter 'isVolatile'"

def test_astm_gastm_type_has_isConst():
    assert hasattr(astm_gastm_Type, "isConst")
    descriptor = None
    for klass in astm_gastm_Type.__mro__:
        if "isConst" in klass.__dict__:
            descriptor = klass.__dict__["isConst"]
            break
    assert isinstance(descriptor, property)

def test_astm_gastm_type_has_isVolatile():
    assert hasattr(astm_gastm_Type, "isVolatile")
    descriptor = None
    for klass in astm_gastm_Type.__mro__:
        if "isVolatile" in klass.__dict__:
            descriptor = klass.__dict__["isVolatile"]
            break
    assert isinstance(descriptor, property)



def test_astm_gastm_statement_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_Statement)


def test_astm_gastm_statement_constructor_exists():
    assert callable(astm_gastm_Statement.__init__)


def test_astm_gastm_statement_constructor_args():
    sig = inspect.signature(astm_gastm_Statement.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_expression_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_Expression)


def test_astm_gastm_expression_constructor_exists():
    assert callable(astm_gastm_Expression.__init__)


def test_astm_gastm_expression_constructor_args():
    sig = inspect.signature(astm_gastm_Expression.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_definitionobject_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_DefinitionObject)


def test_astm_gastm_definitionobject_constructor_exists():
    assert callable(astm_gastm_DefinitionObject.__init__)


def test_astm_gastm_definitionobject_constructor_args():
    sig = inspect.signature(astm_gastm_DefinitionObject.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_othersyntaxobject_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_OtherSyntaxObject)


def test_astm_gastm_othersyntaxobject_constructor_exists():
    assert callable(astm_gastm_OtherSyntaxObject.__init__)


def test_astm_gastm_othersyntaxobject_constructor_args():
    sig = inspect.signature(astm_gastm_OtherSyntaxObject.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_gastmsemanticobject_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_GASTMSemanticObject)


def test_astm_gastm_gastmsemanticobject_constructor_exists():
    assert callable(astm_gastm_GASTMSemanticObject.__init__)


def test_astm_gastm_gastmsemanticobject_constructor_args():
    sig = inspect.signature(astm_gastm_GASTMSemanticObject.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_gastmsourceobject_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_GASTMSourceObject)


def test_astm_gastm_gastmsourceobject_constructor_exists():
    assert callable(astm_gastm_GASTMSourceObject.__init__)


def test_astm_gastm_gastmsourceobject_constructor_args():
    sig = inspect.signature(astm_gastm_GASTMSourceObject.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_gastmobject_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_GASTMObject)


def test_astm_gastm_gastmobject_constructor_exists():
    assert callable(astm_gastm_GASTMObject.__init__)


def test_astm_gastm_gastmobject_constructor_args():
    sig = inspect.signature(astm_gastm_GASTMObject.__init__)
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



def test_astm_gastm_name_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_Name)


def test_astm_gastm_name_constructor_exists():
    assert callable(astm_gastm_Name.__init__)


def test_astm_gastm_name_constructor_args():
    sig = inspect.signature(astm_gastm_Name.__init__)
    params = list(sig.parameters.keys())
    assert "nameString" in params, "Missing parameter 'nameString'"

def test_astm_gastm_name_has_nameString():
    assert hasattr(astm_gastm_Name, "nameString")
    descriptor = None
    for klass in astm_gastm_Name.__mro__:
        if "nameString" in klass.__dict__:
            descriptor = klass.__dict__["nameString"]
            break
    assert isinstance(descriptor, property)



def test_astm_gastm_catchblock_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_CatchBlock)


def test_astm_gastm_catchblock_constructor_exists():
    assert callable(astm_gastm_CatchBlock.__init__)


def test_astm_gastm_catchblock_constructor_args():
    sig = inspect.signature(astm_gastm_CatchBlock.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_derivesfrom_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_DerivesFrom)


def test_astm_gastm_derivesfrom_constructor_exists():
    assert callable(astm_gastm_DerivesFrom.__init__)


def test_astm_gastm_derivesfrom_constructor_args():
    sig = inspect.signature(astm_gastm_DerivesFrom.__init__)
    params = list(sig.parameters.keys())
    assert "isVirtual" in params, "Missing parameter 'isVirtual'"

def test_astm_gastm_derivesfrom_has_isVirtual():
    assert hasattr(astm_gastm_DerivesFrom, "isVirtual")
    descriptor = None
    for klass in astm_gastm_DerivesFrom.__mro__:
        if "isVirtual" in klass.__dict__:
            descriptor = klass.__dict__["isVirtual"]
            break
    assert isinstance(descriptor, property)



def test_astm_gastm_dimension_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_Dimension)


def test_astm_gastm_dimension_constructor_exists():
    assert callable(astm_gastm_Dimension.__init__)


def test_astm_gastm_dimension_constructor_args():
    sig = inspect.signature(astm_gastm_Dimension.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_functionmemberattribute_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_FunctionMemberAttribute)


def test_astm_gastm_functionmemberattribute_constructor_exists():
    assert callable(astm_gastm_FunctionMemberAttribute.__init__)


def test_astm_gastm_functionmemberattribute_constructor_args():
    sig = inspect.signature(astm_gastm_FunctionMemberAttribute.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_virtualspecification_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_VirtualSpecification)


def test_astm_gastm_virtualspecification_constructor_exists():
    assert callable(astm_gastm_VirtualSpecification.__init__)


def test_astm_gastm_virtualspecification_constructor_args():
    sig = inspect.signature(astm_gastm_VirtualSpecification.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_switchcase_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_SwitchCase)


def test_astm_gastm_switchcase_constructor_exists():
    assert callable(astm_gastm_SwitchCase.__init__)


def test_astm_gastm_switchcase_constructor_args():
    sig = inspect.signature(astm_gastm_SwitchCase.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_compilationunit_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_CompilationUnit)


def test_astm_gastm_compilationunit_constructor_exists():
    assert callable(astm_gastm_CompilationUnit.__init__)


def test_astm_gastm_compilationunit_constructor_args():
    sig = inspect.signature(astm_gastm_CompilationUnit.__init__)
    params = list(sig.parameters.keys())
    assert "language" in params, "Missing parameter 'language'"

def test_astm_gastm_compilationunit_has_language():
    assert hasattr(astm_gastm_CompilationUnit, "language")
    descriptor = None
    for klass in astm_gastm_CompilationUnit.__mro__:
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



def test_astm_gastm_includeunit_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_IncludeUnit)


def test_astm_gastm_includeunit_constructor_exists():
    assert callable(astm_gastm_IncludeUnit.__init__)


def test_astm_gastm_includeunit_constructor_args():
    sig = inspect.signature(astm_gastm_IncludeUnit.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_comment_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_Comment)


def test_astm_gastm_comment_constructor_exists():
    assert callable(astm_gastm_Comment.__init__)


def test_astm_gastm_comment_constructor_args():
    sig = inspect.signature(astm_gastm_Comment.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_astm_gastm_comment_has_text():
    assert hasattr(astm_gastm_Comment, "text")
    descriptor = None
    for klass in astm_gastm_Comment.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_astm_gastm_macrocall_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_MacroCall)


def test_astm_gastm_macrocall_constructor_exists():
    assert callable(astm_gastm_MacroCall.__init__)


def test_astm_gastm_macrocall_constructor_args():
    sig = inspect.signature(astm_gastm_MacroCall.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_macrodefinition_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_MacroDefinition)


def test_astm_gastm_macrodefinition_constructor_exists():
    assert callable(astm_gastm_MacroDefinition.__init__)


def test_astm_gastm_macrodefinition_constructor_args():
    sig = inspect.signature(astm_gastm_MacroDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"
    assert "macroName" in params, "Missing parameter 'macroName'"

def test_astm_gastm_macrodefinition_has_body():
    assert hasattr(astm_gastm_MacroDefinition, "body")
    descriptor = None
    for klass in astm_gastm_MacroDefinition.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)

def test_astm_gastm_macrodefinition_has_macroName():
    assert hasattr(astm_gastm_MacroDefinition, "macroName")
    descriptor = None
    for klass in astm_gastm_MacroDefinition.__mro__:
        if "macroName" in klass.__dict__:
            descriptor = klass.__dict__["macroName"]
            break
    assert isinstance(descriptor, property)



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



def test_astm_gastm_gastmsyntaxobject_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_GASTMSyntaxObject)


def test_astm_gastm_gastmsyntaxobject_constructor_exists():
    assert callable(astm_gastm_GASTMSyntaxObject.__init__)


def test_astm_gastm_gastmsyntaxobject_constructor_args():
    sig = inspect.signature(astm_gastm_GASTMSyntaxObject.__init__)
    params = list(sig.parameters.keys())



def test_scope_is_not_abstract():
    assert not inspect.isabstract(Scope)


def test_scope_constructor_exists():
    assert callable(Scope.__init__)


def test_scope_constructor_args():
    sig = inspect.signature(Scope.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_aggregatescope_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_AggregateScope)


def test_astm_gastm_aggregatescope_constructor_exists():
    assert callable(astm_gastm_AggregateScope.__init__)


def test_astm_gastm_aggregatescope_constructor_args():
    sig = inspect.signature(astm_gastm_AggregateScope.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_functionscope_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_FunctionScope)


def test_astm_gastm_functionscope_constructor_exists():
    assert callable(astm_gastm_FunctionScope.__init__)


def test_astm_gastm_functionscope_constructor_args():
    sig = inspect.signature(astm_gastm_FunctionScope.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_programscope_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_ProgramScope)


def test_astm_gastm_programscope_constructor_exists():
    assert callable(astm_gastm_ProgramScope.__init__)


def test_astm_gastm_programscope_constructor_args():
    sig = inspect.signature(astm_gastm_ProgramScope.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_blockscope_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_BlockScope)


def test_astm_gastm_blockscope_constructor_exists():
    assert callable(astm_gastm_BlockScope.__init__)


def test_astm_gastm_blockscope_constructor_args():
    sig = inspect.signature(astm_gastm_BlockScope.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_globalscope_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_GlobalScope)


def test_astm_gastm_globalscope_constructor_exists():
    assert callable(astm_gastm_GlobalScope.__init__)


def test_astm_gastm_globalscope_constructor_args():
    sig = inspect.signature(astm_gastm_GlobalScope.__init__)
    params = list(sig.parameters.keys())



def test_definitionobject_is_not_abstract():
    assert not inspect.isabstract(DefinitionObject)


def test_definitionobject_constructor_exists():
    assert callable(DefinitionObject.__init__)


def test_definitionobject_constructor_args():
    sig = inspect.signature(DefinitionObject.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_namespacedefinition_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_NameSpaceDefinition)


def test_astm_gastm_namespacedefinition_constructor_exists():
    assert callable(astm_gastm_NameSpaceDefinition.__init__)


def test_astm_gastm_namespacedefinition_constructor_args():
    sig = inspect.signature(astm_gastm_NameSpaceDefinition.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_declarationordefinition_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_DeclarationOrDefinition)


def test_astm_gastm_declarationordefinition_constructor_exists():
    assert callable(astm_gastm_DeclarationOrDefinition.__init__)


def test_astm_gastm_declarationordefinition_constructor_args():
    sig = inspect.signature(astm_gastm_DeclarationOrDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "linkageSpecifier" in params, "Missing parameter 'linkageSpecifier'"
    assert "isRegister" in params, "Missing parameter 'isRegister'"

def test_astm_gastm_declarationordefinition_has_linkageSpecifier():
    assert hasattr(astm_gastm_DeclarationOrDefinition, "linkageSpecifier")
    descriptor = None
    for klass in astm_gastm_DeclarationOrDefinition.__mro__:
        if "linkageSpecifier" in klass.__dict__:
            descriptor = klass.__dict__["linkageSpecifier"]
            break
    assert isinstance(descriptor, property)

def test_astm_gastm_declarationordefinition_has_isRegister():
    assert hasattr(astm_gastm_DeclarationOrDefinition, "isRegister")
    descriptor = None
    for klass in astm_gastm_DeclarationOrDefinition.__mro__:
        if "isRegister" in klass.__dict__:
            descriptor = klass.__dict__["isRegister"]
            break
    assert isinstance(descriptor, property)



def test_astm_gastm_typedefinition_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_TypeDefinition)


def test_astm_gastm_typedefinition_constructor_exists():
    assert callable(astm_gastm_TypeDefinition.__init__)


def test_astm_gastm_typedefinition_constructor_args():
    sig = inspect.signature(astm_gastm_TypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_labeldefinition_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_LabelDefinition)


def test_astm_gastm_labeldefinition_constructor_exists():
    assert callable(astm_gastm_LabelDefinition.__init__)


def test_astm_gastm_labeldefinition_constructor_args():
    sig = inspect.signature(astm_gastm_LabelDefinition.__init__)
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



def test_astm_sastm_delphiinterfacesection_is_not_abstract():
    assert not inspect.isabstract(astm_sastm_DelphiInterfaceSection)


def test_astm_sastm_delphiinterfacesection_constructor_exists():
    assert callable(astm_sastm_DelphiInterfaceSection.__init__)


def test_astm_sastm_delphiinterfacesection_constructor_args():
    sig = inspect.signature(astm_sastm_DelphiInterfaceSection.__init__)
    params = list(sig.parameters.keys())



def test_astm_sastm_delphiimplementationsection_is_not_abstract():
    assert not inspect.isabstract(astm_sastm_DelphiImplementationSection)


def test_astm_sastm_delphiimplementationsection_constructor_exists():
    assert callable(astm_sastm_DelphiImplementationSection.__init__)


def test_astm_sastm_delphiimplementationsection_constructor_args():
    sig = inspect.signature(astm_sastm_DelphiImplementationSection.__init__)
    params = list(sig.parameters.keys())



def test_astm_sastm_delphiunit_is_not_abstract():
    assert not inspect.isabstract(astm_sastm_DelphiUnit)


def test_astm_sastm_delphiunit_constructor_exists():
    assert callable(astm_sastm_DelphiUnit.__init__)


def test_astm_sastm_delphiunit_constructor_args():
    sig = inspect.signature(astm_sastm_DelphiUnit.__init__)
    params = list(sig.parameters.keys())



def test_gastmsemanticobject_is_not_abstract():
    assert not inspect.isabstract(GASTMSemanticObject)


def test_gastmsemanticobject_constructor_exists():
    assert callable(GASTMSemanticObject.__init__)


def test_gastmsemanticobject_constructor_args():
    sig = inspect.signature(GASTMSemanticObject.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_scope_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_Scope)


def test_astm_gastm_scope_constructor_exists():
    assert callable(astm_gastm_Scope.__init__)


def test_astm_gastm_scope_constructor_args():
    sig = inspect.signature(astm_gastm_Scope.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastm_project_is_not_abstract():
    assert not inspect.isabstract(astm_gastm_Project)


def test_astm_gastm_project_constructor_exists():
    assert callable(astm_gastm_Project.__init__)


def test_astm_gastm_project_constructor_args():
    sig = inspect.signature(astm_gastm_Project.__init__)
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
ActualParameter_strategy = st.builds(
    ActualParameter,
)
astm_gastm_ActualParameterExpression_strategy = st.builds(
    astm_gastm_ActualParameterExpression,
)
BinaryOperator_strategy = st.builds(
    BinaryOperator,
)
astm_gastm_OperatorAssign_strategy = st.builds(
    astm_gastm_OperatorAssign,
)
IdentifierReference_strategy = st.builds(
    IdentifierReference,
)
NameReference_strategy = st.builds(
    NameReference,
)
astm_gastm_TypeQualifiedIdentifierReference_strategy = st.builds(
    astm_gastm_TypeQualifiedIdentifierReference,
)
astm_gastm_QualifiedIdentifierReference_strategy = st.builds(
    astm_gastm_QualifiedIdentifierReference,
)
SwitchCase_strategy = st.builds(
    SwitchCase,
)
astm_gastm_CaseBlock_strategy = st.builds(
    astm_gastm_CaseBlock,
)
CatchBlock_strategy = st.builds(
    CatchBlock,
)
astm_gastm_VariableCatchBlock_strategy = st.builds(
    astm_gastm_VariableCatchBlock,
)
astm_gastm_TypesCatchBlock_strategy = st.builds(
    astm_gastm_TypesCatchBlock,
)
LoopStatement_strategy = st.builds(
    LoopStatement,
)
astm_gastm_ForStatement_strategy = st.builds(
    astm_gastm_ForStatement,
)
BlockScope_strategy = st.builds(
    BlockScope,
)
LabelDefinition_strategy = st.builds(
    LabelDefinition,
)
LabelAccess_strategy = st.builds(
    LabelAccess,
)
Dimension_strategy = st.builds(
    Dimension,
)
ConstructedType_strategy = st.builds(
    ConstructedType,
)
astm_gastm_ArrayType_strategy = st.builds(
    astm_gastm_ArrayType,
)
AggregateScope_strategy = st.builds(
    AggregateScope,
)
DerivesFrom_strategy = st.builds(
    DerivesFrom,
)
FormalParameterType_strategy = st.builds(
    FormalParameterType,
)
EnumLiteralDefinition_strategy = st.builds(
    EnumLiteralDefinition,
)
DataType_strategy = st.builds(
    DataType,
)
astm_gastm_NamedType_strategy = st.builds(
    astm_gastm_NamedType,
)
astm_gastm_ConstructedType_strategy = st.builds(
    astm_gastm_ConstructedType,
)
astm_gastm_AggregateType_strategy = st.builds(
    astm_gastm_AggregateType,
)
astm_gastm_FormalParameterType_strategy = st.builds(
    astm_gastm_FormalParameterType,
)
astm_gastm_EnumType_strategy = st.builds(
    astm_gastm_EnumType,
)
astm_gastm_PrimitiveType_strategy = st.builds(
    astm_gastm_PrimitiveType,
    isSigned=
        st.booleans()
)
MacroDefinition_strategy = st.builds(
    MacroDefinition,
)
DataDefinition_strategy = st.builds(
    DataDefinition,
)
astm_gastm_BitFieldDefinition_strategy = st.builds(
    astm_gastm_BitFieldDefinition,
)
Expression_strategy = st.builds(
    Expression,
)
astm_gastm_Literal_strategy = st.builds(
    astm_gastm_Literal,
    value=
        safe_text
)
astm_gastm_LabelAccess_strategy = st.builds(
    astm_gastm_LabelAccess,
)
astm_gastm_AnnotationExpression_strategy = st.builds(
    astm_gastm_AnnotationExpression,
)
astm_gastm_RangeExpression_strategy = st.builds(
    astm_gastm_RangeExpression,
)
astm_gastm_CastExpression_strategy = st.builds(
    astm_gastm_CastExpression,
)
astm_gastm_NameReference_strategy = st.builds(
    astm_gastm_NameReference,
)
astm_gastm_FunctionCallExpression_strategy = st.builds(
    astm_gastm_FunctionCallExpression,
)
astm_gastm_ArrayAccess_strategy = st.builds(
    astm_gastm_ArrayAccess,
)
astm_gastm_BinaryExpression_strategy = st.builds(
    astm_gastm_BinaryExpression,
)
astm_gastm_NewExpression_strategy = st.builds(
    astm_gastm_NewExpression,
)
astm_gastm_ConditionalExpression_strategy = st.builds(
    astm_gastm_ConditionalExpression,
)
astm_gastm_UnaryExpression_strategy = st.builds(
    astm_gastm_UnaryExpression,
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
astm_gastm_ClassType_strategy = st.builds(
    astm_gastm_ClassType,
)
NamedType_strategy = st.builds(
    NamedType,
)
TypeDefinition_strategy = st.builds(
    TypeDefinition,
)
astm_gastm_AggregateTypeDefinition_strategy = st.builds(
    astm_gastm_AggregateTypeDefinition,
)
astm_gastm_NamedTypeDefinition_strategy = st.builds(
    astm_gastm_NamedTypeDefinition,
)
Definition_strategy = st.builds(
    Definition,
)
astm_gastm_EnumLiteralDefinition_strategy = st.builds(
    astm_gastm_EnumLiteralDefinition,
)
astm_gastm_EntryDefinition_strategy = st.builds(
    astm_gastm_EntryDefinition,
)
astm_gastm_DataDefinition_strategy = st.builds(
    astm_gastm_DataDefinition,
    isMutable=
        st.booleans()
)
TypeReference_strategy = st.builds(
    TypeReference,
)
astm_gastm_UnnamedTypeReference_strategy = st.builds(
    astm_gastm_UnnamedTypeReference,
)
astm_gastm_NamedTypeReference_strategy = st.builds(
    astm_gastm_NamedTypeReference,
)
Name_strategy = st.builds(
    Name,
)
DeclarationOrDefinition_strategy = st.builds(
    DeclarationOrDefinition,
)
astm_gastm_Declaration_strategy = st.builds(
    astm_gastm_Declaration,
)
astm_gastm_Definition_strategy = st.builds(
    astm_gastm_Definition,
)
VirtualSpecification_strategy = st.builds(
    VirtualSpecification,
)
astm_gastm_FunctionMemberAttributes_strategy = st.builds(
    astm_gastm_FunctionMemberAttributes,
    isThisConst=
        st.booleans(),
    isInline=
        st.booleans(),
    isFriend=
        st.booleans()
)
FunctionScope_strategy = st.builds(
    FunctionScope,
)
Statement_strategy = st.builds(
    Statement,
)
astm_gastm_ExpressionStatement_strategy = st.builds(
    astm_gastm_ExpressionStatement,
)
astm_gastm_IfStatement_strategy = st.builds(
    astm_gastm_IfStatement,
)
astm_gastm_BlockStatement_strategy = st.builds(
    astm_gastm_BlockStatement,
)
astm_gastm_JumpStatement_strategy = st.builds(
    astm_gastm_JumpStatement,
)
astm_gastm_BreakStatement_strategy = st.builds(
    astm_gastm_BreakStatement,
)
astm_gastm_DeleteStatement_strategy = st.builds(
    astm_gastm_DeleteStatement,
)
astm_gastm_LabeledStatement_strategy = st.builds(
    astm_gastm_LabeledStatement,
)
astm_gastm_EmptyStatement_strategy = st.builds(
    astm_gastm_EmptyStatement,
)
astm_gastm_ContinueStatement_strategy = st.builds(
    astm_gastm_ContinueStatement,
)
astm_gastm_DeclarationOrDefinitionStatement_strategy = st.builds(
    astm_gastm_DeclarationOrDefinitionStatement,
)
astm_gastm_TryStatement_strategy = st.builds(
    astm_gastm_TryStatement,
)
astm_gastm_SwitchStatement_strategy = st.builds(
    astm_gastm_SwitchStatement,
)
astm_gastm_LoopStatement_strategy = st.builds(
    astm_gastm_LoopStatement,
)
astm_gastm_ThrowStatement_strategy = st.builds(
    astm_gastm_ThrowStatement,
)
astm_gastm_ReturnStatement_strategy = st.builds(
    astm_gastm_ReturnStatement,
)
FormalParameterDefinition_strategy = st.builds(
    FormalParameterDefinition,
)
DelphiInterfaceSection_strategy = st.builds(
    DelphiInterfaceSection,
)
FunctionCallExpression_strategy = st.builds(
    FunctionCallExpression,
)
astm_sastm_DelphiFunctionCallExpression_strategy = st.builds(
    astm_sastm_DelphiFunctionCallExpression,
)
BlockStatement_strategy = st.builds(
    BlockStatement,
)
astm_sastm_DelphiWithStatement_strategy = st.builds(
    astm_sastm_DelphiWithStatement,
)
astm_sastm_DelphiBlockStatement_strategy = st.builds(
    astm_sastm_DelphiBlockStatement,
)
NamedTypeReference_strategy = st.builds(
    NamedTypeReference,
)
DelphiImplementationSection_strategy = st.builds(
    DelphiImplementationSection,
)
astm_gastm_Multiply_strategy = st.builds(
    astm_gastm_Multiply,
)
astm_gastm_Subtract_strategy = st.builds(
    astm_gastm_Subtract,
)
astm_gastm_Add_strategy = st.builds(
    astm_gastm_Add,
)
astm_gastm_SpecificSelectStatement_strategy = st.builds(
    astm_gastm_SpecificSelectStatement,
)
astm_gastm_SpecificConcatString_strategy = st.builds(
    astm_gastm_SpecificConcatString,
)
astm_gastm_SpecificLike_strategy = st.builds(
    astm_gastm_SpecificLike,
)
astm_gastm_SpecificIn_strategy = st.builds(
    astm_gastm_SpecificIn,
)
astm_gastm_SpecificGreaterEqual_strategy = st.builds(
    astm_gastm_SpecificGreaterEqual,
)
astm_gastm_SpecificLessEqual_strategy = st.builds(
    astm_gastm_SpecificLessEqual,
)
astm_gastm_SpecificTriggerDefinition_strategy = st.builds(
    astm_gastm_SpecificTriggerDefinition,
)
ActualParameterExpression_strategy = st.builds(
    ActualParameterExpression,
)
astm_gastm_ByReferenceActualParameterExpression_strategy = st.builds(
    astm_gastm_ByReferenceActualParameterExpression,
)
astm_gastm_ByValueActualParameterExpression_strategy = st.builds(
    astm_gastm_ByValueActualParameterExpression,
)
astm_gastm_MissingActualParameter_strategy = st.builds(
    astm_gastm_MissingActualParameter,
)
astm_gastm_Assign_strategy = st.builds(
    astm_gastm_Assign,
)
astm_gastm_BitRightShift_strategy = st.builds(
    astm_gastm_BitRightShift,
)
astm_gastm_BitLeftShift_strategy = st.builds(
    astm_gastm_BitLeftShift,
)
astm_gastm_BitXor_strategy = st.builds(
    astm_gastm_BitXor,
)
astm_gastm_BitOr_strategy = st.builds(
    astm_gastm_BitOr,
)
astm_gastm_BitAnd_strategy = st.builds(
    astm_gastm_BitAnd,
)
astm_gastm_NotLess_strategy = st.builds(
    astm_gastm_NotLess,
)
astm_gastm_Less_strategy = st.builds(
    astm_gastm_Less,
)
astm_gastm_NotGreater_strategy = st.builds(
    astm_gastm_NotGreater,
)
astm_gastm_Greater_strategy = st.builds(
    astm_gastm_Greater,
)
astm_gastm_NotEqual_strategy = st.builds(
    astm_gastm_NotEqual,
)
astm_gastm_Equal_strategy = st.builds(
    astm_gastm_Equal,
)
astm_gastm_Or_strategy = st.builds(
    astm_gastm_Or,
)
astm_gastm_And_strategy = st.builds(
    astm_gastm_And,
)
astm_gastm_Exponent_strategy = st.builds(
    astm_gastm_Exponent,
)
astm_gastm_Modulus_strategy = st.builds(
    astm_gastm_Modulus,
)
astm_gastm_Divide_strategy = st.builds(
    astm_gastm_Divide,
)
astm_gastm_PointerType_strategy = st.builds(
    astm_gastm_PointerType,
)
astm_gastm_CollectionType_strategy = st.builds(
    astm_gastm_CollectionType,
)
UnaryOperator_strategy = st.builds(
    UnaryOperator,
)
astm_gastm_Not_strategy = st.builds(
    astm_gastm_Not,
)
astm_gastm_BitNot_strategy = st.builds(
    astm_gastm_BitNot,
)
astm_gastm_Increment_strategy = st.builds(
    astm_gastm_Increment,
)
astm_gastm_Decrement_strategy = st.builds(
    astm_gastm_Decrement,
)
astm_gastm_PostDecrement_strategy = st.builds(
    astm_gastm_PostDecrement,
)
astm_gastm_Negate_strategy = st.builds(
    astm_gastm_Negate,
)
astm_gastm_AddressOf_strategy = st.builds(
    astm_gastm_AddressOf,
)
astm_gastm_PostIncrement_strategy = st.builds(
    astm_gastm_PostIncrement,
)
astm_gastm_Deref_strategy = st.builds(
    astm_gastm_Deref,
)
astm_gastm_UnaryPlus_strategy = st.builds(
    astm_gastm_UnaryPlus,
)
Literal_strategy = st.builds(
    Literal,
)
astm_gastm_RealLiteral_strategy = st.builds(
    astm_gastm_RealLiteral,
)
astm_gastm_StringLiteral_strategy = st.builds(
    astm_gastm_StringLiteral,
)
astm_gastm_BooleanLiteral_strategy = st.builds(
    astm_gastm_BooleanLiteral,
)
astm_gastm_BitLiteral_strategy = st.builds(
    astm_gastm_BitLiteral,
)
astm_gastm_CharLiteral_strategy = st.builds(
    astm_gastm_CharLiteral,
)
astm_gastm_IntegerLiteral_strategy = st.builds(
    astm_gastm_IntegerLiteral,
)
QualifiedIdentifierReference_strategy = st.builds(
    QualifiedIdentifierReference,
)
astm_gastm_QualifiedOverData_strategy = st.builds(
    astm_gastm_QualifiedOverData,
)
astm_gastm_QualifiedOverPointer_strategy = st.builds(
    astm_gastm_QualifiedOverPointer,
)
astm_gastm_AggregateExpression_strategy = st.builds(
    astm_gastm_AggregateExpression,
)
ForStatement_strategy = st.builds(
    ForStatement,
)
astm_gastm_ForCheckAfterStatement_strategy = st.builds(
    astm_gastm_ForCheckAfterStatement,
)
astm_gastm_ForCheckBeforeStatement_strategy = st.builds(
    astm_gastm_ForCheckBeforeStatement,
)
astm_gastm_DoWhileStatement_strategy = st.builds(
    astm_gastm_DoWhileStatement,
)
astm_gastm_WhileStatement_strategy = st.builds(
    astm_gastm_WhileStatement,
)
astm_gastm_DefaultBlock_strategy = st.builds(
    astm_gastm_DefaultBlock,
)
astm_gastm_TerminateStatement_strategy = st.builds(
    astm_gastm_TerminateStatement,
)
AccessKind_strategy = st.builds(
    AccessKind,
)
astm_gastm_Private_strategy = st.builds(
    astm_gastm_Private,
)
astm_gastm_Protected_strategy = st.builds(
    astm_gastm_Protected,
)
astm_gastm_Public_strategy = st.builds(
    astm_gastm_Public,
)
astm_gastm_ByReferenceFormalParameterType_strategy = st.builds(
    astm_gastm_ByReferenceFormalParameterType,
)
astm_gastm_ByValueFormalParameterType_strategy = st.builds(
    astm_gastm_ByValueFormalParameterType,
)
astm_gastm_AnnotationType_strategy = st.builds(
    astm_gastm_AnnotationType,
)
astm_gastm_UnionType_strategy = st.builds(
    astm_gastm_UnionType,
)
astm_gastm_StructureType_strategy = st.builds(
    astm_gastm_StructureType,
)
astm_gastm_RangeType_strategy = st.builds(
    astm_gastm_RangeType,
)
astm_gastm_ReferenceType_strategy = st.builds(
    astm_gastm_ReferenceType,
)
PrimitiveType_strategy = st.builds(
    PrimitiveType,
)
astm_gastm_LongInteger_strategy = st.builds(
    astm_gastm_LongInteger,
)
astm_gastm_Byte_strategy = st.builds(
    astm_gastm_Byte,
)
astm_gastm_LongDouble_strategy = st.builds(
    astm_gastm_LongDouble,
)
astm_gastm_String_strategy = st.builds(
    astm_gastm_String,
)
astm_gastm_Float_strategy = st.builds(
    astm_gastm_Float,
)
astm_gastm_Character_strategy = st.builds(
    astm_gastm_Character,
)
astm_gastm_Boolean_strategy = st.builds(
    astm_gastm_Boolean,
)
astm_gastm_ShortInteger_strategy = st.builds(
    astm_gastm_ShortInteger,
)
astm_gastm_Integer_strategy = st.builds(
    astm_gastm_Integer,
)
astm_gastm_WideCharacter_strategy = st.builds(
    astm_gastm_WideCharacter,
)
astm_gastm_Double_strategy = st.builds(
    astm_gastm_Double,
)
astm_gastm_Void_strategy = st.builds(
    astm_gastm_Void,
)
astm_gastm_ExceptionType_strategy = st.builds(
    astm_gastm_ExceptionType,
)
astm_gastm_NonVirtual_strategy = st.builds(
    astm_gastm_NonVirtual,
)
astm_gastm_PureVirtual_strategy = st.builds(
    astm_gastm_PureVirtual,
)
astm_gastm_Virtual_strategy = st.builds(
    astm_gastm_Virtual,
)
StorageSpecification_strategy = st.builds(
    StorageSpecification,
)
astm_gastm_NoDef_strategy = st.builds(
    astm_gastm_NoDef,
)
astm_gastm_FunctionPersistent_strategy = st.builds(
    astm_gastm_FunctionPersistent,
)
astm_gastm_PerClassMember_strategy = st.builds(
    astm_gastm_PerClassMember,
)
astm_gastm_FileLocal_strategy = st.builds(
    astm_gastm_FileLocal,
)
astm_gastm_External_strategy = st.builds(
    astm_gastm_External,
)
astm_gastm_VariableDefinition_strategy = st.builds(
    astm_gastm_VariableDefinition,
)
astm_gastm_FormalParameterDefinition_strategy = st.builds(
    astm_gastm_FormalParameterDefinition,
)
astm_gastm_IdentifierReference_strategy = st.builds(
    astm_gastm_IdentifierReference,
)
astm_gastm_FunctionDefinition_strategy = st.builds(
    astm_gastm_FunctionDefinition,
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
astm_gastm_VariableDeclaration_strategy = st.builds(
    astm_gastm_VariableDeclaration,
    isMutable=
        st.booleans()
)
astm_gastm_FormalParameterDeclaration_strategy = st.builds(
    astm_gastm_FormalParameterDeclaration,
)
astm_gastm_FunctionDeclaration_strategy = st.builds(
    astm_gastm_FunctionDeclaration,
)
SourceFile_strategy = st.builds(
    SourceFile,
)
GASTMSourceObject_strategy = st.builds(
    GASTMSourceObject,
)
astm_gastm_SourceLocation_strategy = st.builds(
    astm_gastm_SourceLocation,
    startColumn=
        st.integers(),
    startLine=
        st.integers(),
    endLine=
        st.integers(),
    endColumn=
        st.integers()
)
astm_gastm_SourceFile_strategy = st.builds(
    astm_gastm_SourceFile,
    pathName=
        safe_text
)
astm_gastm_ActualParameter_strategy = st.builds(
    astm_gastm_ActualParameter,
)
astm_gastm_BinaryOperator_strategy = st.builds(
    astm_gastm_BinaryOperator,
)
astm_gastm_UnaryOperator_strategy = st.builds(
    astm_gastm_UnaryOperator,
)
astm_gastm_AccessKind_strategy = st.builds(
    astm_gastm_AccessKind,
)
Type_strategy = st.builds(
    Type,
)
astm_gastm_FunctionType_strategy = st.builds(
    astm_gastm_FunctionType,
)
astm_gastm_LabelType_strategy = st.builds(
    astm_gastm_LabelType,
)
astm_gastm_NameSpaceType_strategy = st.builds(
    astm_gastm_NameSpaceType,
)
astm_gastm_TypeReference_strategy = st.builds(
    astm_gastm_TypeReference,
)
astm_gastm_DataType_strategy = st.builds(
    astm_gastm_DataType,
)
astm_gastm_StorageSpecification_strategy = st.builds(
    astm_gastm_StorageSpecification,
)
GASTMSyntaxObject_strategy = st.builds(
    GASTMSyntaxObject,
)
astm_gastm_PreprocessorElement_strategy = st.builds(
    astm_gastm_PreprocessorElement,
)
astm_gastm_Type_strategy = st.builds(
    astm_gastm_Type,
    isConst=
        st.booleans(),
    isVolatile=
        st.booleans()
)
astm_gastm_Statement_strategy = st.builds(
    astm_gastm_Statement,
)
astm_gastm_Expression_strategy = st.builds(
    astm_gastm_Expression,
)
astm_gastm_DefinitionObject_strategy = st.builds(
    astm_gastm_DefinitionObject,
)
astm_gastm_OtherSyntaxObject_strategy = st.builds(
    astm_gastm_OtherSyntaxObject,
)
astm_gastm_GASTMSemanticObject_strategy = st.builds(
    astm_gastm_GASTMSemanticObject,
)
astm_gastm_GASTMSourceObject_strategy = st.builds(
    astm_gastm_GASTMSourceObject,
)
astm_gastm_GASTMObject_strategy = st.builds(
    astm_gastm_GASTMObject,
)
ProgramScope_strategy = st.builds(
    ProgramScope,
)
OtherSyntaxObject_strategy = st.builds(
    OtherSyntaxObject,
)
astm_gastm_Name_strategy = st.builds(
    astm_gastm_Name,
    nameString=
        safe_text
)
astm_gastm_CatchBlock_strategy = st.builds(
    astm_gastm_CatchBlock,
)
astm_gastm_DerivesFrom_strategy = st.builds(
    astm_gastm_DerivesFrom,
    isVirtual=
        st.booleans()
)
astm_gastm_Dimension_strategy = st.builds(
    astm_gastm_Dimension,
)
astm_gastm_FunctionMemberAttribute_strategy = st.builds(
    astm_gastm_FunctionMemberAttribute,
)
astm_gastm_VirtualSpecification_strategy = st.builds(
    astm_gastm_VirtualSpecification,
)
astm_gastm_SwitchCase_strategy = st.builds(
    astm_gastm_SwitchCase,
)
astm_gastm_CompilationUnit_strategy = st.builds(
    astm_gastm_CompilationUnit,
    language=
        safe_text
)
AnnotationExpression_strategy = st.builds(
    AnnotationExpression,
)
PreprocessorElement_strategy = st.builds(
    PreprocessorElement,
)
astm_gastm_IncludeUnit_strategy = st.builds(
    astm_gastm_IncludeUnit,
)
astm_gastm_Comment_strategy = st.builds(
    astm_gastm_Comment,
    text=
        safe_text
)
astm_gastm_MacroCall_strategy = st.builds(
    astm_gastm_MacroCall,
)
astm_gastm_MacroDefinition_strategy = st.builds(
    astm_gastm_MacroDefinition,
    body=
        safe_text,
    macroName=
        safe_text
)
SourceLocation_strategy = st.builds(
    SourceLocation,
)
GASTMObject_strategy = st.builds(
    GASTMObject,
)
astm_gastm_GASTMSyntaxObject_strategy = st.builds(
    astm_gastm_GASTMSyntaxObject,
)
Scope_strategy = st.builds(
    Scope,
)
astm_gastm_AggregateScope_strategy = st.builds(
    astm_gastm_AggregateScope,
)
astm_gastm_FunctionScope_strategy = st.builds(
    astm_gastm_FunctionScope,
)
astm_gastm_ProgramScope_strategy = st.builds(
    astm_gastm_ProgramScope,
)
astm_gastm_BlockScope_strategy = st.builds(
    astm_gastm_BlockScope,
)
astm_gastm_GlobalScope_strategy = st.builds(
    astm_gastm_GlobalScope,
)
DefinitionObject_strategy = st.builds(
    DefinitionObject,
)
astm_gastm_NameSpaceDefinition_strategy = st.builds(
    astm_gastm_NameSpaceDefinition,
)
astm_gastm_DeclarationOrDefinition_strategy = st.builds(
    astm_gastm_DeclarationOrDefinition,
    linkageSpecifier=
        safe_text,
    isRegister=
        st.booleans()
)
astm_gastm_TypeDefinition_strategy = st.builds(
    astm_gastm_TypeDefinition,
)
astm_gastm_LabelDefinition_strategy = st.builds(
    astm_gastm_LabelDefinition,
)
GlobalScope_strategy = st.builds(
    GlobalScope,
)
CompilationUnit_strategy = st.builds(
    CompilationUnit,
)
astm_sastm_DelphiInterfaceSection_strategy = st.builds(
    astm_sastm_DelphiInterfaceSection,
)
astm_sastm_DelphiImplementationSection_strategy = st.builds(
    astm_sastm_DelphiImplementationSection,
)
astm_sastm_DelphiUnit_strategy = st.builds(
    astm_sastm_DelphiUnit,
)
GASTMSemanticObject_strategy = st.builds(
    GASTMSemanticObject,
)
astm_gastm_Scope_strategy = st.builds(
    astm_gastm_Scope,
)
astm_gastm_Project_strategy = st.builds(
    astm_gastm_Project,
)

@given(instance=ActualParameter_strategy)
@settings(max_examples=50)
def test_actualparameter_instantiation(instance):
    assert isinstance(instance, ActualParameter)

@given(instance=astm_gastm_ActualParameterExpression_strategy)
@settings(max_examples=50)
def test_astm_gastm_actualparameterexpression_instantiation(instance):
    assert isinstance(instance, astm_gastm_ActualParameterExpression)

@given(instance=BinaryOperator_strategy)
@settings(max_examples=50)
def test_binaryoperator_instantiation(instance):
    assert isinstance(instance, BinaryOperator)

@given(instance=astm_gastm_OperatorAssign_strategy)
@settings(max_examples=50)
def test_astm_gastm_operatorassign_instantiation(instance):
    assert isinstance(instance, astm_gastm_OperatorAssign)

@given(instance=IdentifierReference_strategy)
@settings(max_examples=50)
def test_identifierreference_instantiation(instance):
    assert isinstance(instance, IdentifierReference)

@given(instance=NameReference_strategy)
@settings(max_examples=50)
def test_namereference_instantiation(instance):
    assert isinstance(instance, NameReference)

@given(instance=astm_gastm_TypeQualifiedIdentifierReference_strategy)
@settings(max_examples=50)
def test_astm_gastm_typequalifiedidentifierreference_instantiation(instance):
    assert isinstance(instance, astm_gastm_TypeQualifiedIdentifierReference)

@given(instance=astm_gastm_QualifiedIdentifierReference_strategy)
@settings(max_examples=50)
def test_astm_gastm_qualifiedidentifierreference_instantiation(instance):
    assert isinstance(instance, astm_gastm_QualifiedIdentifierReference)

@given(instance=SwitchCase_strategy)
@settings(max_examples=50)
def test_switchcase_instantiation(instance):
    assert isinstance(instance, SwitchCase)

@given(instance=astm_gastm_CaseBlock_strategy)
@settings(max_examples=50)
def test_astm_gastm_caseblock_instantiation(instance):
    assert isinstance(instance, astm_gastm_CaseBlock)

@given(instance=CatchBlock_strategy)
@settings(max_examples=50)
def test_catchblock_instantiation(instance):
    assert isinstance(instance, CatchBlock)

@given(instance=astm_gastm_VariableCatchBlock_strategy)
@settings(max_examples=50)
def test_astm_gastm_variablecatchblock_instantiation(instance):
    assert isinstance(instance, astm_gastm_VariableCatchBlock)

@given(instance=astm_gastm_TypesCatchBlock_strategy)
@settings(max_examples=50)
def test_astm_gastm_typescatchblock_instantiation(instance):
    assert isinstance(instance, astm_gastm_TypesCatchBlock)

@given(instance=LoopStatement_strategy)
@settings(max_examples=50)
def test_loopstatement_instantiation(instance):
    assert isinstance(instance, LoopStatement)

@given(instance=astm_gastm_ForStatement_strategy)
@settings(max_examples=50)
def test_astm_gastm_forstatement_instantiation(instance):
    assert isinstance(instance, astm_gastm_ForStatement)

@given(instance=BlockScope_strategy)
@settings(max_examples=50)
def test_blockscope_instantiation(instance):
    assert isinstance(instance, BlockScope)

@given(instance=LabelDefinition_strategy)
@settings(max_examples=50)
def test_labeldefinition_instantiation(instance):
    assert isinstance(instance, LabelDefinition)

@given(instance=LabelAccess_strategy)
@settings(max_examples=50)
def test_labelaccess_instantiation(instance):
    assert isinstance(instance, LabelAccess)

@given(instance=Dimension_strategy)
@settings(max_examples=50)
def test_dimension_instantiation(instance):
    assert isinstance(instance, Dimension)

@given(instance=ConstructedType_strategy)
@settings(max_examples=50)
def test_constructedtype_instantiation(instance):
    assert isinstance(instance, ConstructedType)

@given(instance=astm_gastm_ArrayType_strategy)
@settings(max_examples=50)
def test_astm_gastm_arraytype_instantiation(instance):
    assert isinstance(instance, astm_gastm_ArrayType)

@given(instance=AggregateScope_strategy)
@settings(max_examples=50)
def test_aggregatescope_instantiation(instance):
    assert isinstance(instance, AggregateScope)

@given(instance=DerivesFrom_strategy)
@settings(max_examples=50)
def test_derivesfrom_instantiation(instance):
    assert isinstance(instance, DerivesFrom)

@given(instance=FormalParameterType_strategy)
@settings(max_examples=50)
def test_formalparametertype_instantiation(instance):
    assert isinstance(instance, FormalParameterType)

@given(instance=EnumLiteralDefinition_strategy)
@settings(max_examples=50)
def test_enumliteraldefinition_instantiation(instance):
    assert isinstance(instance, EnumLiteralDefinition)

@given(instance=DataType_strategy)
@settings(max_examples=50)
def test_datatype_instantiation(instance):
    assert isinstance(instance, DataType)

@given(instance=astm_gastm_NamedType_strategy)
@settings(max_examples=50)
def test_astm_gastm_namedtype_instantiation(instance):
    assert isinstance(instance, astm_gastm_NamedType)

@given(instance=astm_gastm_ConstructedType_strategy)
@settings(max_examples=50)
def test_astm_gastm_constructedtype_instantiation(instance):
    assert isinstance(instance, astm_gastm_ConstructedType)

@given(instance=astm_gastm_AggregateType_strategy)
@settings(max_examples=50)
def test_astm_gastm_aggregatetype_instantiation(instance):
    assert isinstance(instance, astm_gastm_AggregateType)

@given(instance=astm_gastm_FormalParameterType_strategy)
@settings(max_examples=50)
def test_astm_gastm_formalparametertype_instantiation(instance):
    assert isinstance(instance, astm_gastm_FormalParameterType)

@given(instance=astm_gastm_EnumType_strategy)
@settings(max_examples=50)
def test_astm_gastm_enumtype_instantiation(instance):
    assert isinstance(instance, astm_gastm_EnumType)

@given(instance=astm_gastm_PrimitiveType_strategy)
@settings(max_examples=50)
def test_astm_gastm_primitivetype_instantiation(instance):
    assert isinstance(instance, astm_gastm_PrimitiveType)



@given(instance=astm_gastm_PrimitiveType_strategy)
def test_astm_gastm_primitivetype_isSigned_setter(instance):
    original = instance.isSigned
    instance.isSigned = original
    assert instance.isSigned == original

@given(instance=MacroDefinition_strategy)
@settings(max_examples=50)
def test_macrodefinition_instantiation(instance):
    assert isinstance(instance, MacroDefinition)

@given(instance=DataDefinition_strategy)
@settings(max_examples=50)
def test_datadefinition_instantiation(instance):
    assert isinstance(instance, DataDefinition)

@given(instance=astm_gastm_BitFieldDefinition_strategy)
@settings(max_examples=50)
def test_astm_gastm_bitfielddefinition_instantiation(instance):
    assert isinstance(instance, astm_gastm_BitFieldDefinition)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=astm_gastm_Literal_strategy)
@settings(max_examples=50)
def test_astm_gastm_literal_instantiation(instance):
    assert isinstance(instance, astm_gastm_Literal)



@given(instance=astm_gastm_Literal_strategy)
def test_astm_gastm_literal_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=astm_gastm_LabelAccess_strategy)
@settings(max_examples=50)
def test_astm_gastm_labelaccess_instantiation(instance):
    assert isinstance(instance, astm_gastm_LabelAccess)

@given(instance=astm_gastm_AnnotationExpression_strategy)
@settings(max_examples=50)
def test_astm_gastm_annotationexpression_instantiation(instance):
    assert isinstance(instance, astm_gastm_AnnotationExpression)

@given(instance=astm_gastm_RangeExpression_strategy)
@settings(max_examples=50)
def test_astm_gastm_rangeexpression_instantiation(instance):
    assert isinstance(instance, astm_gastm_RangeExpression)

@given(instance=astm_gastm_CastExpression_strategy)
@settings(max_examples=50)
def test_astm_gastm_castexpression_instantiation(instance):
    assert isinstance(instance, astm_gastm_CastExpression)

@given(instance=astm_gastm_NameReference_strategy)
@settings(max_examples=50)
def test_astm_gastm_namereference_instantiation(instance):
    assert isinstance(instance, astm_gastm_NameReference)

@given(instance=astm_gastm_FunctionCallExpression_strategy)
@settings(max_examples=50)
def test_astm_gastm_functioncallexpression_instantiation(instance):
    assert isinstance(instance, astm_gastm_FunctionCallExpression)

@given(instance=astm_gastm_ArrayAccess_strategy)
@settings(max_examples=50)
def test_astm_gastm_arrayaccess_instantiation(instance):
    assert isinstance(instance, astm_gastm_ArrayAccess)

@given(instance=astm_gastm_BinaryExpression_strategy)
@settings(max_examples=50)
def test_astm_gastm_binaryexpression_instantiation(instance):
    assert isinstance(instance, astm_gastm_BinaryExpression)

@given(instance=astm_gastm_NewExpression_strategy)
@settings(max_examples=50)
def test_astm_gastm_newexpression_instantiation(instance):
    assert isinstance(instance, astm_gastm_NewExpression)

@given(instance=astm_gastm_ConditionalExpression_strategy)
@settings(max_examples=50)
def test_astm_gastm_conditionalexpression_instantiation(instance):
    assert isinstance(instance, astm_gastm_ConditionalExpression)

@given(instance=astm_gastm_UnaryExpression_strategy)
@settings(max_examples=50)
def test_astm_gastm_unaryexpression_instantiation(instance):
    assert isinstance(instance, astm_gastm_UnaryExpression)

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

@given(instance=astm_gastm_ClassType_strategy)
@settings(max_examples=50)
def test_astm_gastm_classtype_instantiation(instance):
    assert isinstance(instance, astm_gastm_ClassType)

@given(instance=NamedType_strategy)
@settings(max_examples=50)
def test_namedtype_instantiation(instance):
    assert isinstance(instance, NamedType)

@given(instance=TypeDefinition_strategy)
@settings(max_examples=50)
def test_typedefinition_instantiation(instance):
    assert isinstance(instance, TypeDefinition)

@given(instance=astm_gastm_AggregateTypeDefinition_strategy)
@settings(max_examples=50)
def test_astm_gastm_aggregatetypedefinition_instantiation(instance):
    assert isinstance(instance, astm_gastm_AggregateTypeDefinition)

@given(instance=astm_gastm_NamedTypeDefinition_strategy)
@settings(max_examples=50)
def test_astm_gastm_namedtypedefinition_instantiation(instance):
    assert isinstance(instance, astm_gastm_NamedTypeDefinition)

@given(instance=Definition_strategy)
@settings(max_examples=50)
def test_definition_instantiation(instance):
    assert isinstance(instance, Definition)

@given(instance=astm_gastm_EnumLiteralDefinition_strategy)
@settings(max_examples=50)
def test_astm_gastm_enumliteraldefinition_instantiation(instance):
    assert isinstance(instance, astm_gastm_EnumLiteralDefinition)

@given(instance=astm_gastm_EntryDefinition_strategy)
@settings(max_examples=50)
def test_astm_gastm_entrydefinition_instantiation(instance):
    assert isinstance(instance, astm_gastm_EntryDefinition)

@given(instance=astm_gastm_DataDefinition_strategy)
@settings(max_examples=50)
def test_astm_gastm_datadefinition_instantiation(instance):
    assert isinstance(instance, astm_gastm_DataDefinition)



@given(instance=astm_gastm_DataDefinition_strategy)
def test_astm_gastm_datadefinition_isMutable_setter(instance):
    original = instance.isMutable
    instance.isMutable = original
    assert instance.isMutable == original

@given(instance=TypeReference_strategy)
@settings(max_examples=50)
def test_typereference_instantiation(instance):
    assert isinstance(instance, TypeReference)

@given(instance=astm_gastm_UnnamedTypeReference_strategy)
@settings(max_examples=50)
def test_astm_gastm_unnamedtypereference_instantiation(instance):
    assert isinstance(instance, astm_gastm_UnnamedTypeReference)

@given(instance=astm_gastm_NamedTypeReference_strategy)
@settings(max_examples=50)
def test_astm_gastm_namedtypereference_instantiation(instance):
    assert isinstance(instance, astm_gastm_NamedTypeReference)

@given(instance=Name_strategy)
@settings(max_examples=50)
def test_name_instantiation(instance):
    assert isinstance(instance, Name)

@given(instance=DeclarationOrDefinition_strategy)
@settings(max_examples=50)
def test_declarationordefinition_instantiation(instance):
    assert isinstance(instance, DeclarationOrDefinition)

@given(instance=astm_gastm_Declaration_strategy)
@settings(max_examples=50)
def test_astm_gastm_declaration_instantiation(instance):
    assert isinstance(instance, astm_gastm_Declaration)

@given(instance=astm_gastm_Definition_strategy)
@settings(max_examples=50)
def test_astm_gastm_definition_instantiation(instance):
    assert isinstance(instance, astm_gastm_Definition)

@given(instance=VirtualSpecification_strategy)
@settings(max_examples=50)
def test_virtualspecification_instantiation(instance):
    assert isinstance(instance, VirtualSpecification)

@given(instance=astm_gastm_FunctionMemberAttributes_strategy)
@settings(max_examples=50)
def test_astm_gastm_functionmemberattributes_instantiation(instance):
    assert isinstance(instance, astm_gastm_FunctionMemberAttributes)



@given(instance=astm_gastm_FunctionMemberAttributes_strategy)
def test_astm_gastm_functionmemberattributes_isThisConst_setter(instance):
    original = instance.isThisConst
    instance.isThisConst = original
    assert instance.isThisConst == original



@given(instance=astm_gastm_FunctionMemberAttributes_strategy)
def test_astm_gastm_functionmemberattributes_isInline_setter(instance):
    original = instance.isInline
    instance.isInline = original
    assert instance.isInline == original



@given(instance=astm_gastm_FunctionMemberAttributes_strategy)
def test_astm_gastm_functionmemberattributes_isFriend_setter(instance):
    original = instance.isFriend
    instance.isFriend = original
    assert instance.isFriend == original

@given(instance=FunctionScope_strategy)
@settings(max_examples=50)
def test_functionscope_instantiation(instance):
    assert isinstance(instance, FunctionScope)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=astm_gastm_ExpressionStatement_strategy)
@settings(max_examples=50)
def test_astm_gastm_expressionstatement_instantiation(instance):
    assert isinstance(instance, astm_gastm_ExpressionStatement)

@given(instance=astm_gastm_IfStatement_strategy)
@settings(max_examples=50)
def test_astm_gastm_ifstatement_instantiation(instance):
    assert isinstance(instance, astm_gastm_IfStatement)

@given(instance=astm_gastm_BlockStatement_strategy)
@settings(max_examples=50)
def test_astm_gastm_blockstatement_instantiation(instance):
    assert isinstance(instance, astm_gastm_BlockStatement)

@given(instance=astm_gastm_JumpStatement_strategy)
@settings(max_examples=50)
def test_astm_gastm_jumpstatement_instantiation(instance):
    assert isinstance(instance, astm_gastm_JumpStatement)

@given(instance=astm_gastm_BreakStatement_strategy)
@settings(max_examples=50)
def test_astm_gastm_breakstatement_instantiation(instance):
    assert isinstance(instance, astm_gastm_BreakStatement)

@given(instance=astm_gastm_DeleteStatement_strategy)
@settings(max_examples=50)
def test_astm_gastm_deletestatement_instantiation(instance):
    assert isinstance(instance, astm_gastm_DeleteStatement)

@given(instance=astm_gastm_LabeledStatement_strategy)
@settings(max_examples=50)
def test_astm_gastm_labeledstatement_instantiation(instance):
    assert isinstance(instance, astm_gastm_LabeledStatement)

@given(instance=astm_gastm_EmptyStatement_strategy)
@settings(max_examples=50)
def test_astm_gastm_emptystatement_instantiation(instance):
    assert isinstance(instance, astm_gastm_EmptyStatement)

@given(instance=astm_gastm_ContinueStatement_strategy)
@settings(max_examples=50)
def test_astm_gastm_continuestatement_instantiation(instance):
    assert isinstance(instance, astm_gastm_ContinueStatement)

@given(instance=astm_gastm_DeclarationOrDefinitionStatement_strategy)
@settings(max_examples=50)
def test_astm_gastm_declarationordefinitionstatement_instantiation(instance):
    assert isinstance(instance, astm_gastm_DeclarationOrDefinitionStatement)

@given(instance=astm_gastm_TryStatement_strategy)
@settings(max_examples=50)
def test_astm_gastm_trystatement_instantiation(instance):
    assert isinstance(instance, astm_gastm_TryStatement)

@given(instance=astm_gastm_SwitchStatement_strategy)
@settings(max_examples=50)
def test_astm_gastm_switchstatement_instantiation(instance):
    assert isinstance(instance, astm_gastm_SwitchStatement)

@given(instance=astm_gastm_LoopStatement_strategy)
@settings(max_examples=50)
def test_astm_gastm_loopstatement_instantiation(instance):
    assert isinstance(instance, astm_gastm_LoopStatement)

@given(instance=astm_gastm_ThrowStatement_strategy)
@settings(max_examples=50)
def test_astm_gastm_throwstatement_instantiation(instance):
    assert isinstance(instance, astm_gastm_ThrowStatement)

@given(instance=astm_gastm_ReturnStatement_strategy)
@settings(max_examples=50)
def test_astm_gastm_returnstatement_instantiation(instance):
    assert isinstance(instance, astm_gastm_ReturnStatement)

@given(instance=FormalParameterDefinition_strategy)
@settings(max_examples=50)
def test_formalparameterdefinition_instantiation(instance):
    assert isinstance(instance, FormalParameterDefinition)

@given(instance=DelphiInterfaceSection_strategy)
@settings(max_examples=50)
def test_delphiinterfacesection_instantiation(instance):
    assert isinstance(instance, DelphiInterfaceSection)

@given(instance=FunctionCallExpression_strategy)
@settings(max_examples=50)
def test_functioncallexpression_instantiation(instance):
    assert isinstance(instance, FunctionCallExpression)

@given(instance=astm_sastm_DelphiFunctionCallExpression_strategy)
@settings(max_examples=50)
def test_astm_sastm_delphifunctioncallexpression_instantiation(instance):
    assert isinstance(instance, astm_sastm_DelphiFunctionCallExpression)

@given(instance=BlockStatement_strategy)
@settings(max_examples=50)
def test_blockstatement_instantiation(instance):
    assert isinstance(instance, BlockStatement)

@given(instance=astm_sastm_DelphiWithStatement_strategy)
@settings(max_examples=50)
def test_astm_sastm_delphiwithstatement_instantiation(instance):
    assert isinstance(instance, astm_sastm_DelphiWithStatement)

@given(instance=astm_sastm_DelphiBlockStatement_strategy)
@settings(max_examples=50)
def test_astm_sastm_delphiblockstatement_instantiation(instance):
    assert isinstance(instance, astm_sastm_DelphiBlockStatement)

@given(instance=NamedTypeReference_strategy)
@settings(max_examples=50)
def test_namedtypereference_instantiation(instance):
    assert isinstance(instance, NamedTypeReference)

@given(instance=DelphiImplementationSection_strategy)
@settings(max_examples=50)
def test_delphiimplementationsection_instantiation(instance):
    assert isinstance(instance, DelphiImplementationSection)

@given(instance=astm_gastm_Multiply_strategy)
@settings(max_examples=50)
def test_astm_gastm_multiply_instantiation(instance):
    assert isinstance(instance, astm_gastm_Multiply)

@given(instance=astm_gastm_Subtract_strategy)
@settings(max_examples=50)
def test_astm_gastm_subtract_instantiation(instance):
    assert isinstance(instance, astm_gastm_Subtract)

@given(instance=astm_gastm_Add_strategy)
@settings(max_examples=50)
def test_astm_gastm_add_instantiation(instance):
    assert isinstance(instance, astm_gastm_Add)

@given(instance=astm_gastm_SpecificSelectStatement_strategy)
@settings(max_examples=50)
def test_astm_gastm_specificselectstatement_instantiation(instance):
    assert isinstance(instance, astm_gastm_SpecificSelectStatement)

@given(instance=astm_gastm_SpecificConcatString_strategy)
@settings(max_examples=50)
def test_astm_gastm_specificconcatstring_instantiation(instance):
    assert isinstance(instance, astm_gastm_SpecificConcatString)

@given(instance=astm_gastm_SpecificLike_strategy)
@settings(max_examples=50)
def test_astm_gastm_specificlike_instantiation(instance):
    assert isinstance(instance, astm_gastm_SpecificLike)

@given(instance=astm_gastm_SpecificIn_strategy)
@settings(max_examples=50)
def test_astm_gastm_specificin_instantiation(instance):
    assert isinstance(instance, astm_gastm_SpecificIn)

@given(instance=astm_gastm_SpecificGreaterEqual_strategy)
@settings(max_examples=50)
def test_astm_gastm_specificgreaterequal_instantiation(instance):
    assert isinstance(instance, astm_gastm_SpecificGreaterEqual)

@given(instance=astm_gastm_SpecificLessEqual_strategy)
@settings(max_examples=50)
def test_astm_gastm_specificlessequal_instantiation(instance):
    assert isinstance(instance, astm_gastm_SpecificLessEqual)

@given(instance=astm_gastm_SpecificTriggerDefinition_strategy)
@settings(max_examples=50)
def test_astm_gastm_specifictriggerdefinition_instantiation(instance):
    assert isinstance(instance, astm_gastm_SpecificTriggerDefinition)

@given(instance=ActualParameterExpression_strategy)
@settings(max_examples=50)
def test_actualparameterexpression_instantiation(instance):
    assert isinstance(instance, ActualParameterExpression)

@given(instance=astm_gastm_ByReferenceActualParameterExpression_strategy)
@settings(max_examples=50)
def test_astm_gastm_byreferenceactualparameterexpression_instantiation(instance):
    assert isinstance(instance, astm_gastm_ByReferenceActualParameterExpression)

@given(instance=astm_gastm_ByValueActualParameterExpression_strategy)
@settings(max_examples=50)
def test_astm_gastm_byvalueactualparameterexpression_instantiation(instance):
    assert isinstance(instance, astm_gastm_ByValueActualParameterExpression)

@given(instance=astm_gastm_MissingActualParameter_strategy)
@settings(max_examples=50)
def test_astm_gastm_missingactualparameter_instantiation(instance):
    assert isinstance(instance, astm_gastm_MissingActualParameter)

@given(instance=astm_gastm_Assign_strategy)
@settings(max_examples=50)
def test_astm_gastm_assign_instantiation(instance):
    assert isinstance(instance, astm_gastm_Assign)

@given(instance=astm_gastm_BitRightShift_strategy)
@settings(max_examples=50)
def test_astm_gastm_bitrightshift_instantiation(instance):
    assert isinstance(instance, astm_gastm_BitRightShift)

@given(instance=astm_gastm_BitLeftShift_strategy)
@settings(max_examples=50)
def test_astm_gastm_bitleftshift_instantiation(instance):
    assert isinstance(instance, astm_gastm_BitLeftShift)

@given(instance=astm_gastm_BitXor_strategy)
@settings(max_examples=50)
def test_astm_gastm_bitxor_instantiation(instance):
    assert isinstance(instance, astm_gastm_BitXor)

@given(instance=astm_gastm_BitOr_strategy)
@settings(max_examples=50)
def test_astm_gastm_bitor_instantiation(instance):
    assert isinstance(instance, astm_gastm_BitOr)

@given(instance=astm_gastm_BitAnd_strategy)
@settings(max_examples=50)
def test_astm_gastm_bitand_instantiation(instance):
    assert isinstance(instance, astm_gastm_BitAnd)

@given(instance=astm_gastm_NotLess_strategy)
@settings(max_examples=50)
def test_astm_gastm_notless_instantiation(instance):
    assert isinstance(instance, astm_gastm_NotLess)

@given(instance=astm_gastm_Less_strategy)
@settings(max_examples=50)
def test_astm_gastm_less_instantiation(instance):
    assert isinstance(instance, astm_gastm_Less)

@given(instance=astm_gastm_NotGreater_strategy)
@settings(max_examples=50)
def test_astm_gastm_notgreater_instantiation(instance):
    assert isinstance(instance, astm_gastm_NotGreater)

@given(instance=astm_gastm_Greater_strategy)
@settings(max_examples=50)
def test_astm_gastm_greater_instantiation(instance):
    assert isinstance(instance, astm_gastm_Greater)

@given(instance=astm_gastm_NotEqual_strategy)
@settings(max_examples=50)
def test_astm_gastm_notequal_instantiation(instance):
    assert isinstance(instance, astm_gastm_NotEqual)

@given(instance=astm_gastm_Equal_strategy)
@settings(max_examples=50)
def test_astm_gastm_equal_instantiation(instance):
    assert isinstance(instance, astm_gastm_Equal)

@given(instance=astm_gastm_Or_strategy)
@settings(max_examples=50)
def test_astm_gastm_or_instantiation(instance):
    assert isinstance(instance, astm_gastm_Or)

@given(instance=astm_gastm_And_strategy)
@settings(max_examples=50)
def test_astm_gastm_and_instantiation(instance):
    assert isinstance(instance, astm_gastm_And)

@given(instance=astm_gastm_Exponent_strategy)
@settings(max_examples=50)
def test_astm_gastm_exponent_instantiation(instance):
    assert isinstance(instance, astm_gastm_Exponent)

@given(instance=astm_gastm_Modulus_strategy)
@settings(max_examples=50)
def test_astm_gastm_modulus_instantiation(instance):
    assert isinstance(instance, astm_gastm_Modulus)

@given(instance=astm_gastm_Divide_strategy)
@settings(max_examples=50)
def test_astm_gastm_divide_instantiation(instance):
    assert isinstance(instance, astm_gastm_Divide)

@given(instance=astm_gastm_PointerType_strategy)
@settings(max_examples=50)
def test_astm_gastm_pointertype_instantiation(instance):
    assert isinstance(instance, astm_gastm_PointerType)

@given(instance=astm_gastm_CollectionType_strategy)
@settings(max_examples=50)
def test_astm_gastm_collectiontype_instantiation(instance):
    assert isinstance(instance, astm_gastm_CollectionType)

@given(instance=UnaryOperator_strategy)
@settings(max_examples=50)
def test_unaryoperator_instantiation(instance):
    assert isinstance(instance, UnaryOperator)

@given(instance=astm_gastm_Not_strategy)
@settings(max_examples=50)
def test_astm_gastm_not_instantiation(instance):
    assert isinstance(instance, astm_gastm_Not)

@given(instance=astm_gastm_BitNot_strategy)
@settings(max_examples=50)
def test_astm_gastm_bitnot_instantiation(instance):
    assert isinstance(instance, astm_gastm_BitNot)

@given(instance=astm_gastm_Increment_strategy)
@settings(max_examples=50)
def test_astm_gastm_increment_instantiation(instance):
    assert isinstance(instance, astm_gastm_Increment)

@given(instance=astm_gastm_Decrement_strategy)
@settings(max_examples=50)
def test_astm_gastm_decrement_instantiation(instance):
    assert isinstance(instance, astm_gastm_Decrement)

@given(instance=astm_gastm_PostDecrement_strategy)
@settings(max_examples=50)
def test_astm_gastm_postdecrement_instantiation(instance):
    assert isinstance(instance, astm_gastm_PostDecrement)

@given(instance=astm_gastm_Negate_strategy)
@settings(max_examples=50)
def test_astm_gastm_negate_instantiation(instance):
    assert isinstance(instance, astm_gastm_Negate)

@given(instance=astm_gastm_AddressOf_strategy)
@settings(max_examples=50)
def test_astm_gastm_addressof_instantiation(instance):
    assert isinstance(instance, astm_gastm_AddressOf)

@given(instance=astm_gastm_PostIncrement_strategy)
@settings(max_examples=50)
def test_astm_gastm_postincrement_instantiation(instance):
    assert isinstance(instance, astm_gastm_PostIncrement)

@given(instance=astm_gastm_Deref_strategy)
@settings(max_examples=50)
def test_astm_gastm_deref_instantiation(instance):
    assert isinstance(instance, astm_gastm_Deref)

@given(instance=astm_gastm_UnaryPlus_strategy)
@settings(max_examples=50)
def test_astm_gastm_unaryplus_instantiation(instance):
    assert isinstance(instance, astm_gastm_UnaryPlus)

@given(instance=Literal_strategy)
@settings(max_examples=50)
def test_literal_instantiation(instance):
    assert isinstance(instance, Literal)

@given(instance=astm_gastm_RealLiteral_strategy)
@settings(max_examples=50)
def test_astm_gastm_realliteral_instantiation(instance):
    assert isinstance(instance, astm_gastm_RealLiteral)

@given(instance=astm_gastm_StringLiteral_strategy)
@settings(max_examples=50)
def test_astm_gastm_stringliteral_instantiation(instance):
    assert isinstance(instance, astm_gastm_StringLiteral)

@given(instance=astm_gastm_BooleanLiteral_strategy)
@settings(max_examples=50)
def test_astm_gastm_booleanliteral_instantiation(instance):
    assert isinstance(instance, astm_gastm_BooleanLiteral)

@given(instance=astm_gastm_BitLiteral_strategy)
@settings(max_examples=50)
def test_astm_gastm_bitliteral_instantiation(instance):
    assert isinstance(instance, astm_gastm_BitLiteral)

@given(instance=astm_gastm_CharLiteral_strategy)
@settings(max_examples=50)
def test_astm_gastm_charliteral_instantiation(instance):
    assert isinstance(instance, astm_gastm_CharLiteral)

@given(instance=astm_gastm_IntegerLiteral_strategy)
@settings(max_examples=50)
def test_astm_gastm_integerliteral_instantiation(instance):
    assert isinstance(instance, astm_gastm_IntegerLiteral)

@given(instance=QualifiedIdentifierReference_strategy)
@settings(max_examples=50)
def test_qualifiedidentifierreference_instantiation(instance):
    assert isinstance(instance, QualifiedIdentifierReference)

@given(instance=astm_gastm_QualifiedOverData_strategy)
@settings(max_examples=50)
def test_astm_gastm_qualifiedoverdata_instantiation(instance):
    assert isinstance(instance, astm_gastm_QualifiedOverData)

@given(instance=astm_gastm_QualifiedOverPointer_strategy)
@settings(max_examples=50)
def test_astm_gastm_qualifiedoverpointer_instantiation(instance):
    assert isinstance(instance, astm_gastm_QualifiedOverPointer)

@given(instance=astm_gastm_AggregateExpression_strategy)
@settings(max_examples=50)
def test_astm_gastm_aggregateexpression_instantiation(instance):
    assert isinstance(instance, astm_gastm_AggregateExpression)

@given(instance=ForStatement_strategy)
@settings(max_examples=50)
def test_forstatement_instantiation(instance):
    assert isinstance(instance, ForStatement)

@given(instance=astm_gastm_ForCheckAfterStatement_strategy)
@settings(max_examples=50)
def test_astm_gastm_forcheckafterstatement_instantiation(instance):
    assert isinstance(instance, astm_gastm_ForCheckAfterStatement)

@given(instance=astm_gastm_ForCheckBeforeStatement_strategy)
@settings(max_examples=50)
def test_astm_gastm_forcheckbeforestatement_instantiation(instance):
    assert isinstance(instance, astm_gastm_ForCheckBeforeStatement)

@given(instance=astm_gastm_DoWhileStatement_strategy)
@settings(max_examples=50)
def test_astm_gastm_dowhilestatement_instantiation(instance):
    assert isinstance(instance, astm_gastm_DoWhileStatement)

@given(instance=astm_gastm_WhileStatement_strategy)
@settings(max_examples=50)
def test_astm_gastm_whilestatement_instantiation(instance):
    assert isinstance(instance, astm_gastm_WhileStatement)

@given(instance=astm_gastm_DefaultBlock_strategy)
@settings(max_examples=50)
def test_astm_gastm_defaultblock_instantiation(instance):
    assert isinstance(instance, astm_gastm_DefaultBlock)

@given(instance=astm_gastm_TerminateStatement_strategy)
@settings(max_examples=50)
def test_astm_gastm_terminatestatement_instantiation(instance):
    assert isinstance(instance, astm_gastm_TerminateStatement)

@given(instance=AccessKind_strategy)
@settings(max_examples=50)
def test_accesskind_instantiation(instance):
    assert isinstance(instance, AccessKind)

@given(instance=astm_gastm_Private_strategy)
@settings(max_examples=50)
def test_astm_gastm_private_instantiation(instance):
    assert isinstance(instance, astm_gastm_Private)

@given(instance=astm_gastm_Protected_strategy)
@settings(max_examples=50)
def test_astm_gastm_protected_instantiation(instance):
    assert isinstance(instance, astm_gastm_Protected)

@given(instance=astm_gastm_Public_strategy)
@settings(max_examples=50)
def test_astm_gastm_public_instantiation(instance):
    assert isinstance(instance, astm_gastm_Public)

@given(instance=astm_gastm_ByReferenceFormalParameterType_strategy)
@settings(max_examples=50)
def test_astm_gastm_byreferenceformalparametertype_instantiation(instance):
    assert isinstance(instance, astm_gastm_ByReferenceFormalParameterType)

@given(instance=astm_gastm_ByValueFormalParameterType_strategy)
@settings(max_examples=50)
def test_astm_gastm_byvalueformalparametertype_instantiation(instance):
    assert isinstance(instance, astm_gastm_ByValueFormalParameterType)

@given(instance=astm_gastm_AnnotationType_strategy)
@settings(max_examples=50)
def test_astm_gastm_annotationtype_instantiation(instance):
    assert isinstance(instance, astm_gastm_AnnotationType)

@given(instance=astm_gastm_UnionType_strategy)
@settings(max_examples=50)
def test_astm_gastm_uniontype_instantiation(instance):
    assert isinstance(instance, astm_gastm_UnionType)

@given(instance=astm_gastm_StructureType_strategy)
@settings(max_examples=50)
def test_astm_gastm_structuretype_instantiation(instance):
    assert isinstance(instance, astm_gastm_StructureType)

@given(instance=astm_gastm_RangeType_strategy)
@settings(max_examples=50)
def test_astm_gastm_rangetype_instantiation(instance):
    assert isinstance(instance, astm_gastm_RangeType)

@given(instance=astm_gastm_ReferenceType_strategy)
@settings(max_examples=50)
def test_astm_gastm_referencetype_instantiation(instance):
    assert isinstance(instance, astm_gastm_ReferenceType)

@given(instance=PrimitiveType_strategy)
@settings(max_examples=50)
def test_primitivetype_instantiation(instance):
    assert isinstance(instance, PrimitiveType)

@given(instance=astm_gastm_LongInteger_strategy)
@settings(max_examples=50)
def test_astm_gastm_longinteger_instantiation(instance):
    assert isinstance(instance, astm_gastm_LongInteger)

@given(instance=astm_gastm_Byte_strategy)
@settings(max_examples=50)
def test_astm_gastm_byte_instantiation(instance):
    assert isinstance(instance, astm_gastm_Byte)

@given(instance=astm_gastm_LongDouble_strategy)
@settings(max_examples=50)
def test_astm_gastm_longdouble_instantiation(instance):
    assert isinstance(instance, astm_gastm_LongDouble)

@given(instance=astm_gastm_String_strategy)
@settings(max_examples=50)
def test_astm_gastm_string_instantiation(instance):
    assert isinstance(instance, astm_gastm_String)

@given(instance=astm_gastm_Float_strategy)
@settings(max_examples=50)
def test_astm_gastm_float_instantiation(instance):
    assert isinstance(instance, astm_gastm_Float)

@given(instance=astm_gastm_Character_strategy)
@settings(max_examples=50)
def test_astm_gastm_character_instantiation(instance):
    assert isinstance(instance, astm_gastm_Character)

@given(instance=astm_gastm_Boolean_strategy)
@settings(max_examples=50)
def test_astm_gastm_boolean_instantiation(instance):
    assert isinstance(instance, astm_gastm_Boolean)

@given(instance=astm_gastm_ShortInteger_strategy)
@settings(max_examples=50)
def test_astm_gastm_shortinteger_instantiation(instance):
    assert isinstance(instance, astm_gastm_ShortInteger)

@given(instance=astm_gastm_Integer_strategy)
@settings(max_examples=50)
def test_astm_gastm_integer_instantiation(instance):
    assert isinstance(instance, astm_gastm_Integer)

@given(instance=astm_gastm_WideCharacter_strategy)
@settings(max_examples=50)
def test_astm_gastm_widecharacter_instantiation(instance):
    assert isinstance(instance, astm_gastm_WideCharacter)

@given(instance=astm_gastm_Double_strategy)
@settings(max_examples=50)
def test_astm_gastm_double_instantiation(instance):
    assert isinstance(instance, astm_gastm_Double)

@given(instance=astm_gastm_Void_strategy)
@settings(max_examples=50)
def test_astm_gastm_void_instantiation(instance):
    assert isinstance(instance, astm_gastm_Void)

@given(instance=astm_gastm_ExceptionType_strategy)
@settings(max_examples=50)
def test_astm_gastm_exceptiontype_instantiation(instance):
    assert isinstance(instance, astm_gastm_ExceptionType)

@given(instance=astm_gastm_NonVirtual_strategy)
@settings(max_examples=50)
def test_astm_gastm_nonvirtual_instantiation(instance):
    assert isinstance(instance, astm_gastm_NonVirtual)

@given(instance=astm_gastm_PureVirtual_strategy)
@settings(max_examples=50)
def test_astm_gastm_purevirtual_instantiation(instance):
    assert isinstance(instance, astm_gastm_PureVirtual)

@given(instance=astm_gastm_Virtual_strategy)
@settings(max_examples=50)
def test_astm_gastm_virtual_instantiation(instance):
    assert isinstance(instance, astm_gastm_Virtual)

@given(instance=StorageSpecification_strategy)
@settings(max_examples=50)
def test_storagespecification_instantiation(instance):
    assert isinstance(instance, StorageSpecification)

@given(instance=astm_gastm_NoDef_strategy)
@settings(max_examples=50)
def test_astm_gastm_nodef_instantiation(instance):
    assert isinstance(instance, astm_gastm_NoDef)

@given(instance=astm_gastm_FunctionPersistent_strategy)
@settings(max_examples=50)
def test_astm_gastm_functionpersistent_instantiation(instance):
    assert isinstance(instance, astm_gastm_FunctionPersistent)

@given(instance=astm_gastm_PerClassMember_strategy)
@settings(max_examples=50)
def test_astm_gastm_perclassmember_instantiation(instance):
    assert isinstance(instance, astm_gastm_PerClassMember)

@given(instance=astm_gastm_FileLocal_strategy)
@settings(max_examples=50)
def test_astm_gastm_filelocal_instantiation(instance):
    assert isinstance(instance, astm_gastm_FileLocal)

@given(instance=astm_gastm_External_strategy)
@settings(max_examples=50)
def test_astm_gastm_external_instantiation(instance):
    assert isinstance(instance, astm_gastm_External)

@given(instance=astm_gastm_VariableDefinition_strategy)
@settings(max_examples=50)
def test_astm_gastm_variabledefinition_instantiation(instance):
    assert isinstance(instance, astm_gastm_VariableDefinition)

@given(instance=astm_gastm_FormalParameterDefinition_strategy)
@settings(max_examples=50)
def test_astm_gastm_formalparameterdefinition_instantiation(instance):
    assert isinstance(instance, astm_gastm_FormalParameterDefinition)

@given(instance=astm_gastm_IdentifierReference_strategy)
@settings(max_examples=50)
def test_astm_gastm_identifierreference_instantiation(instance):
    assert isinstance(instance, astm_gastm_IdentifierReference)

@given(instance=astm_gastm_FunctionDefinition_strategy)
@settings(max_examples=50)
def test_astm_gastm_functiondefinition_instantiation(instance):
    assert isinstance(instance, astm_gastm_FunctionDefinition)

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

@given(instance=astm_gastm_VariableDeclaration_strategy)
@settings(max_examples=50)
def test_astm_gastm_variabledeclaration_instantiation(instance):
    assert isinstance(instance, astm_gastm_VariableDeclaration)



@given(instance=astm_gastm_VariableDeclaration_strategy)
def test_astm_gastm_variabledeclaration_isMutable_setter(instance):
    original = instance.isMutable
    instance.isMutable = original
    assert instance.isMutable == original

@given(instance=astm_gastm_FormalParameterDeclaration_strategy)
@settings(max_examples=50)
def test_astm_gastm_formalparameterdeclaration_instantiation(instance):
    assert isinstance(instance, astm_gastm_FormalParameterDeclaration)

@given(instance=astm_gastm_FunctionDeclaration_strategy)
@settings(max_examples=50)
def test_astm_gastm_functiondeclaration_instantiation(instance):
    assert isinstance(instance, astm_gastm_FunctionDeclaration)

@given(instance=SourceFile_strategy)
@settings(max_examples=50)
def test_sourcefile_instantiation(instance):
    assert isinstance(instance, SourceFile)

@given(instance=GASTMSourceObject_strategy)
@settings(max_examples=50)
def test_gastmsourceobject_instantiation(instance):
    assert isinstance(instance, GASTMSourceObject)

@given(instance=astm_gastm_SourceLocation_strategy)
@settings(max_examples=50)
def test_astm_gastm_sourcelocation_instantiation(instance):
    assert isinstance(instance, astm_gastm_SourceLocation)



@given(instance=astm_gastm_SourceLocation_strategy)
def test_astm_gastm_sourcelocation_startColumn_setter(instance):
    original = instance.startColumn
    instance.startColumn = original
    assert instance.startColumn == original



@given(instance=astm_gastm_SourceLocation_strategy)
def test_astm_gastm_sourcelocation_startLine_setter(instance):
    original = instance.startLine
    instance.startLine = original
    assert instance.startLine == original



@given(instance=astm_gastm_SourceLocation_strategy)
def test_astm_gastm_sourcelocation_endLine_setter(instance):
    original = instance.endLine
    instance.endLine = original
    assert instance.endLine == original



@given(instance=astm_gastm_SourceLocation_strategy)
def test_astm_gastm_sourcelocation_endColumn_setter(instance):
    original = instance.endColumn
    instance.endColumn = original
    assert instance.endColumn == original

@given(instance=astm_gastm_SourceFile_strategy)
@settings(max_examples=50)
def test_astm_gastm_sourcefile_instantiation(instance):
    assert isinstance(instance, astm_gastm_SourceFile)



@given(instance=astm_gastm_SourceFile_strategy)
def test_astm_gastm_sourcefile_pathName_setter(instance):
    original = instance.pathName
    instance.pathName = original
    assert instance.pathName == original

@given(instance=astm_gastm_ActualParameter_strategy)
@settings(max_examples=50)
def test_astm_gastm_actualparameter_instantiation(instance):
    assert isinstance(instance, astm_gastm_ActualParameter)

@given(instance=astm_gastm_BinaryOperator_strategy)
@settings(max_examples=50)
def test_astm_gastm_binaryoperator_instantiation(instance):
    assert isinstance(instance, astm_gastm_BinaryOperator)

@given(instance=astm_gastm_UnaryOperator_strategy)
@settings(max_examples=50)
def test_astm_gastm_unaryoperator_instantiation(instance):
    assert isinstance(instance, astm_gastm_UnaryOperator)

@given(instance=astm_gastm_AccessKind_strategy)
@settings(max_examples=50)
def test_astm_gastm_accesskind_instantiation(instance):
    assert isinstance(instance, astm_gastm_AccessKind)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=astm_gastm_FunctionType_strategy)
@settings(max_examples=50)
def test_astm_gastm_functiontype_instantiation(instance):
    assert isinstance(instance, astm_gastm_FunctionType)

@given(instance=astm_gastm_LabelType_strategy)
@settings(max_examples=50)
def test_astm_gastm_labeltype_instantiation(instance):
    assert isinstance(instance, astm_gastm_LabelType)

@given(instance=astm_gastm_NameSpaceType_strategy)
@settings(max_examples=50)
def test_astm_gastm_namespacetype_instantiation(instance):
    assert isinstance(instance, astm_gastm_NameSpaceType)

@given(instance=astm_gastm_TypeReference_strategy)
@settings(max_examples=50)
def test_astm_gastm_typereference_instantiation(instance):
    assert isinstance(instance, astm_gastm_TypeReference)

@given(instance=astm_gastm_DataType_strategy)
@settings(max_examples=50)
def test_astm_gastm_datatype_instantiation(instance):
    assert isinstance(instance, astm_gastm_DataType)

@given(instance=astm_gastm_StorageSpecification_strategy)
@settings(max_examples=50)
def test_astm_gastm_storagespecification_instantiation(instance):
    assert isinstance(instance, astm_gastm_StorageSpecification)

@given(instance=GASTMSyntaxObject_strategy)
@settings(max_examples=50)
def test_gastmsyntaxobject_instantiation(instance):
    assert isinstance(instance, GASTMSyntaxObject)

@given(instance=astm_gastm_PreprocessorElement_strategy)
@settings(max_examples=50)
def test_astm_gastm_preprocessorelement_instantiation(instance):
    assert isinstance(instance, astm_gastm_PreprocessorElement)

@given(instance=astm_gastm_Type_strategy)
@settings(max_examples=50)
def test_astm_gastm_type_instantiation(instance):
    assert isinstance(instance, astm_gastm_Type)



@given(instance=astm_gastm_Type_strategy)
def test_astm_gastm_type_isConst_setter(instance):
    original = instance.isConst
    instance.isConst = original
    assert instance.isConst == original



@given(instance=astm_gastm_Type_strategy)
def test_astm_gastm_type_isVolatile_setter(instance):
    original = instance.isVolatile
    instance.isVolatile = original
    assert instance.isVolatile == original

@given(instance=astm_gastm_Statement_strategy)
@settings(max_examples=50)
def test_astm_gastm_statement_instantiation(instance):
    assert isinstance(instance, astm_gastm_Statement)

@given(instance=astm_gastm_Expression_strategy)
@settings(max_examples=50)
def test_astm_gastm_expression_instantiation(instance):
    assert isinstance(instance, astm_gastm_Expression)

@given(instance=astm_gastm_DefinitionObject_strategy)
@settings(max_examples=50)
def test_astm_gastm_definitionobject_instantiation(instance):
    assert isinstance(instance, astm_gastm_DefinitionObject)

@given(instance=astm_gastm_OtherSyntaxObject_strategy)
@settings(max_examples=50)
def test_astm_gastm_othersyntaxobject_instantiation(instance):
    assert isinstance(instance, astm_gastm_OtherSyntaxObject)

@given(instance=astm_gastm_GASTMSemanticObject_strategy)
@settings(max_examples=50)
def test_astm_gastm_gastmsemanticobject_instantiation(instance):
    assert isinstance(instance, astm_gastm_GASTMSemanticObject)

@given(instance=astm_gastm_GASTMSourceObject_strategy)
@settings(max_examples=50)
def test_astm_gastm_gastmsourceobject_instantiation(instance):
    assert isinstance(instance, astm_gastm_GASTMSourceObject)

@given(instance=astm_gastm_GASTMObject_strategy)
@settings(max_examples=50)
def test_astm_gastm_gastmobject_instantiation(instance):
    assert isinstance(instance, astm_gastm_GASTMObject)

@given(instance=ProgramScope_strategy)
@settings(max_examples=50)
def test_programscope_instantiation(instance):
    assert isinstance(instance, ProgramScope)

@given(instance=OtherSyntaxObject_strategy)
@settings(max_examples=50)
def test_othersyntaxobject_instantiation(instance):
    assert isinstance(instance, OtherSyntaxObject)

@given(instance=astm_gastm_Name_strategy)
@settings(max_examples=50)
def test_astm_gastm_name_instantiation(instance):
    assert isinstance(instance, astm_gastm_Name)



@given(instance=astm_gastm_Name_strategy)
def test_astm_gastm_name_nameString_setter(instance):
    original = instance.nameString
    instance.nameString = original
    assert instance.nameString == original

@given(instance=astm_gastm_CatchBlock_strategy)
@settings(max_examples=50)
def test_astm_gastm_catchblock_instantiation(instance):
    assert isinstance(instance, astm_gastm_CatchBlock)

@given(instance=astm_gastm_DerivesFrom_strategy)
@settings(max_examples=50)
def test_astm_gastm_derivesfrom_instantiation(instance):
    assert isinstance(instance, astm_gastm_DerivesFrom)



@given(instance=astm_gastm_DerivesFrom_strategy)
def test_astm_gastm_derivesfrom_isVirtual_setter(instance):
    original = instance.isVirtual
    instance.isVirtual = original
    assert instance.isVirtual == original

@given(instance=astm_gastm_Dimension_strategy)
@settings(max_examples=50)
def test_astm_gastm_dimension_instantiation(instance):
    assert isinstance(instance, astm_gastm_Dimension)

@given(instance=astm_gastm_FunctionMemberAttribute_strategy)
@settings(max_examples=50)
def test_astm_gastm_functionmemberattribute_instantiation(instance):
    assert isinstance(instance, astm_gastm_FunctionMemberAttribute)

@given(instance=astm_gastm_VirtualSpecification_strategy)
@settings(max_examples=50)
def test_astm_gastm_virtualspecification_instantiation(instance):
    assert isinstance(instance, astm_gastm_VirtualSpecification)

@given(instance=astm_gastm_SwitchCase_strategy)
@settings(max_examples=50)
def test_astm_gastm_switchcase_instantiation(instance):
    assert isinstance(instance, astm_gastm_SwitchCase)

@given(instance=astm_gastm_CompilationUnit_strategy)
@settings(max_examples=50)
def test_astm_gastm_compilationunit_instantiation(instance):
    assert isinstance(instance, astm_gastm_CompilationUnit)



@given(instance=astm_gastm_CompilationUnit_strategy)
def test_astm_gastm_compilationunit_language_setter(instance):
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

@given(instance=astm_gastm_IncludeUnit_strategy)
@settings(max_examples=50)
def test_astm_gastm_includeunit_instantiation(instance):
    assert isinstance(instance, astm_gastm_IncludeUnit)

@given(instance=astm_gastm_Comment_strategy)
@settings(max_examples=50)
def test_astm_gastm_comment_instantiation(instance):
    assert isinstance(instance, astm_gastm_Comment)



@given(instance=astm_gastm_Comment_strategy)
def test_astm_gastm_comment_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=astm_gastm_MacroCall_strategy)
@settings(max_examples=50)
def test_astm_gastm_macrocall_instantiation(instance):
    assert isinstance(instance, astm_gastm_MacroCall)

@given(instance=astm_gastm_MacroDefinition_strategy)
@settings(max_examples=50)
def test_astm_gastm_macrodefinition_instantiation(instance):
    assert isinstance(instance, astm_gastm_MacroDefinition)



@given(instance=astm_gastm_MacroDefinition_strategy)
def test_astm_gastm_macrodefinition_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original



@given(instance=astm_gastm_MacroDefinition_strategy)
def test_astm_gastm_macrodefinition_macroName_setter(instance):
    original = instance.macroName
    instance.macroName = original
    assert instance.macroName == original

@given(instance=SourceLocation_strategy)
@settings(max_examples=50)
def test_sourcelocation_instantiation(instance):
    assert isinstance(instance, SourceLocation)

@given(instance=GASTMObject_strategy)
@settings(max_examples=50)
def test_gastmobject_instantiation(instance):
    assert isinstance(instance, GASTMObject)

@given(instance=astm_gastm_GASTMSyntaxObject_strategy)
@settings(max_examples=50)
def test_astm_gastm_gastmsyntaxobject_instantiation(instance):
    assert isinstance(instance, astm_gastm_GASTMSyntaxObject)

@given(instance=Scope_strategy)
@settings(max_examples=50)
def test_scope_instantiation(instance):
    assert isinstance(instance, Scope)

@given(instance=astm_gastm_AggregateScope_strategy)
@settings(max_examples=50)
def test_astm_gastm_aggregatescope_instantiation(instance):
    assert isinstance(instance, astm_gastm_AggregateScope)

@given(instance=astm_gastm_FunctionScope_strategy)
@settings(max_examples=50)
def test_astm_gastm_functionscope_instantiation(instance):
    assert isinstance(instance, astm_gastm_FunctionScope)

@given(instance=astm_gastm_ProgramScope_strategy)
@settings(max_examples=50)
def test_astm_gastm_programscope_instantiation(instance):
    assert isinstance(instance, astm_gastm_ProgramScope)

@given(instance=astm_gastm_BlockScope_strategy)
@settings(max_examples=50)
def test_astm_gastm_blockscope_instantiation(instance):
    assert isinstance(instance, astm_gastm_BlockScope)

@given(instance=astm_gastm_GlobalScope_strategy)
@settings(max_examples=50)
def test_astm_gastm_globalscope_instantiation(instance):
    assert isinstance(instance, astm_gastm_GlobalScope)

@given(instance=DefinitionObject_strategy)
@settings(max_examples=50)
def test_definitionobject_instantiation(instance):
    assert isinstance(instance, DefinitionObject)

@given(instance=astm_gastm_NameSpaceDefinition_strategy)
@settings(max_examples=50)
def test_astm_gastm_namespacedefinition_instantiation(instance):
    assert isinstance(instance, astm_gastm_NameSpaceDefinition)

@given(instance=astm_gastm_DeclarationOrDefinition_strategy)
@settings(max_examples=50)
def test_astm_gastm_declarationordefinition_instantiation(instance):
    assert isinstance(instance, astm_gastm_DeclarationOrDefinition)



@given(instance=astm_gastm_DeclarationOrDefinition_strategy)
def test_astm_gastm_declarationordefinition_linkageSpecifier_setter(instance):
    original = instance.linkageSpecifier
    instance.linkageSpecifier = original
    assert instance.linkageSpecifier == original



@given(instance=astm_gastm_DeclarationOrDefinition_strategy)
def test_astm_gastm_declarationordefinition_isRegister_setter(instance):
    original = instance.isRegister
    instance.isRegister = original
    assert instance.isRegister == original

@given(instance=astm_gastm_TypeDefinition_strategy)
@settings(max_examples=50)
def test_astm_gastm_typedefinition_instantiation(instance):
    assert isinstance(instance, astm_gastm_TypeDefinition)

@given(instance=astm_gastm_LabelDefinition_strategy)
@settings(max_examples=50)
def test_astm_gastm_labeldefinition_instantiation(instance):
    assert isinstance(instance, astm_gastm_LabelDefinition)

@given(instance=GlobalScope_strategy)
@settings(max_examples=50)
def test_globalscope_instantiation(instance):
    assert isinstance(instance, GlobalScope)

@given(instance=CompilationUnit_strategy)
@settings(max_examples=50)
def test_compilationunit_instantiation(instance):
    assert isinstance(instance, CompilationUnit)

@given(instance=astm_sastm_DelphiInterfaceSection_strategy)
@settings(max_examples=50)
def test_astm_sastm_delphiinterfacesection_instantiation(instance):
    assert isinstance(instance, astm_sastm_DelphiInterfaceSection)

@given(instance=astm_sastm_DelphiImplementationSection_strategy)
@settings(max_examples=50)
def test_astm_sastm_delphiimplementationsection_instantiation(instance):
    assert isinstance(instance, astm_sastm_DelphiImplementationSection)

@given(instance=astm_sastm_DelphiUnit_strategy)
@settings(max_examples=50)
def test_astm_sastm_delphiunit_instantiation(instance):
    assert isinstance(instance, astm_sastm_DelphiUnit)

@given(instance=GASTMSemanticObject_strategy)
@settings(max_examples=50)
def test_gastmsemanticobject_instantiation(instance):
    assert isinstance(instance, GASTMSemanticObject)

@given(instance=astm_gastm_Scope_strategy)
@settings(max_examples=50)
def test_astm_gastm_scope_instantiation(instance):
    assert isinstance(instance, astm_gastm_Scope)

@given(instance=astm_gastm_Project_strategy)
@settings(max_examples=50)
def test_astm_gastm_project_instantiation(instance):
    assert isinstance(instance, astm_gastm_Project)
