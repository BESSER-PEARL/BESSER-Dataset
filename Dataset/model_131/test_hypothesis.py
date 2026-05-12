import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    astm_Visitable,
    RDBColumnType,
    astm_RDBBFile,
    astm_RDBClob,
    astm_RDBChar,
    astm_RDBBlob,
    astm_RDBNClob,
    astm_RDBInt,
    astm_RDBRowid,
    astm_RDBDate,
    astm_RDBLong,
    astm_RDBTimestamp,
    astm_RDBBoolean,
    astm_RDBReal,
    astm_RDBDecimal,
    astm_RDBFloat,
    astm_RDBVarchar,
    astm_RDBNumber,
    astm_RDBInteger,
    IdentifierReference,
    astm_RDBTableAlias,
    astm_RDBRaw,
    astm_RDBString,
    RDBCursorStatement,
    astm_RDBFetchCursorStatement,
    astm_RDBCloseCursorStatement,
    astm_RDBOpenCursorStatement,
    RDBModifyStatement,
    astm_RDBDeleteStatement,
    astm_RDBUpdateStatement,
    astm_RDBTableReference,
    RDBConstraint,
    astm_RDBUniqueKey,
    astm_RDBRefIntegrity,
    astm_RDBCheckConstraint,
    astm_RDBColumnReference,
    ActualParameterExpression,
    astm_ByReferenceActualParameterExpression,
    astm_ByValueActualParameterExpression,
    UnaryOperator,
    astm_Decrement,
    astm_Increment,
    astm_Deref,
    astm_PostDecrement,
    astm_Not,
    astm_PostIncrement,
    astm_AddressOf,
    astm_BitNot,
    astm_Negate,
    astm_UnaryPlus,
    Literal,
    astm_RealLiteral,
    astm_CharLiteral,
    astm_BitLiteral,
    astm_BooleanLiteral,
    astm_StringLiteral,
    astm_IntegerlLiteral,
    QualifiedIdentifierReference,
    astm_QualifiedOverData,
    astm_QualifiedOverPointer,
    ForStatement,
    astm_ForCheckAfterStatement,
    astm_ForCheckBeforeStatement,
    AccessKind,
    astm_Private,
    astm_Public,
    FormalParameterType,
    astm_ByReferenceFormalParameterType,
    astm_ByValueFormalParameterType,
    astm_Protected,
    PrimitiveType,
    astm_Integer,
    astm_Float,
    astm_String,
    astm_ShortInteger,
    astm_LongInteger,
    astm_Boolean,
    astm_WideCharacter,
    astm_Character,
    astm_LongDouble,
    astm_Byte,
    astm_Double,
    astm_Void,
    VirtualSpecification,
    astm_PureVirtual,
    astm_NonVirtual,
    astm_Virtual,
    StorageSpecification,
    astm_FileLocal,
    astm_NoDef,
    astm_FunctionPersistent,
    astm_PerClassMember,
    astm_External,
    Scope,
    ActualParameter,
    astm_MissingActualParameter,
    astm_ActualParameterExpression,
    BinaryOperator,
    astm_NotEqual,
    astm_BitXor,
    astm_SpecificIn,
    astm_SpecificLessEqual,
    astm_Multiply,
    astm_BitRightShift,
    astm_Less,
    astm_Or,
    astm_SpecificLike,
    astm_Exponent,
    astm_Modulus,
    astm_Equal,
    astm_SpecificGreaterEqual,
    astm_SpecificConcatString,
    astm_BitOr,
    astm_And,
    astm_Divide,
    astm_BitLeftShift,
    astm_Add,
    astm_Greater,
    astm_Subtract,
    astm_NotGreater,
    astm_Assign,
    astm_NotLess,
    astm_BitAnd,
    astm_OperatorAssign,
    TypeReference,
    astm_NamedTypeReference,
    astm_UnnamedTypeReference,
    AggregateType,
    astm_UnionType,
    astm_AnnotationType,
    astm_StructureType,
    astm_ClassType,
    Type,
    astm_FunctionType,
    ConstructedType,
    astm_PointerType,
    astm_ReferenceType,
    astm_CollectionType,
    astm_RangeType,
    astm_ArrayType,
    astm_AggregateScope,
    DataType,
    astm_EnumType,
    astm_RDBDataBaseType,
    astm_RDBCursorType,
    astm_RDBTableType,
    astm_ExceptionType,
    astm_RDBUserType,
    astm_RDBColumnType,
    astm_FormalParameterType,
    astm_ConstructedType,
    astm_RDBTableSpaceType,
    astm_RDBViewType,
    astm_PrimitiveType,
    GASTMSyntaxObject,
    astm_Type,
    PreprocessorElement,
    astm_MacroDefinition,
    astm_MacroCall,
    astm_Comment,
    astm_IncludeUnit,
    astm_LabelType,
    astm_NameSpaceType,
    astm_AggregateType,
    astm_NamedType,
    TypeDefinition,
    astm_AggregateTypeDefinition,
    astm_NamedTypeDefinition,
    DataDefinition,
    astm_VariableDefinition,
    astm_BitFieldDefinition,
    astm_Expression,
    astm_TypeReference,
    astm_FunctionScope,
    astm_Statement,
    astm_FormalParameterDefinition,
    Definition,
    astm_RDBUserDefinition,
    astm_DataDefinition,
    astm_RDBTableDefinition,
    astm_EntryDefinition,
    astm_RDBCursorDefinition,
    astm_RDBColumnDefinition,
    astm_SpecificTriggerDefinition,
    astm_EnumLiteralDefinition,
    astm_RDBViewDefinition,
    astm_RDBTableSpaceDefinition,
    astm_RDBDatabaseDefinition,
    astm_FunctionDefinition,
    Declaration,
    astm_VariableDeclaration,
    astm_FormalParameterDeclaration,
    astm_FunctionDeclaration,
    GASTMSemanticObject,
    astm_Project,
    DeclarationOrDefinition,
    astm_Declaration,
    astm_Definition,
    DefinitionObject,
    astm_TypeDefinition,
    astm_LabelDefinition,
    astm_NameSpaceDefinition,
    astm_DeclarationOrDefinition,
    astm_ProgramScope,
    OtherSyntaxObject,
    astm_VirtualSpecification,
    astm_DerivesFrom,
    astm_Dimension,
    astm_RDBTrigger,
    astm_RDBIndexColumn,
    astm_FunctionMemberAttribute,
    astm_RDBIndex,
    astm_RDBConstraint,
    astm_Name,
    astm_PreprocessorElement,
    GASTMObject,
    astm_GASTMSyntaxObject,
    astm_DefinitionObject,
    astm_Scope,
    astm_GlobalScope,
    astm_CompilationUnit,
    GASTMSourceObject,
    astm_SourceLocation,
    astm_SourceFile,
    Visitable,
    astm_RDBHostVariableReference,
    astm_AccessKind,
    astm_DataType,
    astm_StorageSpecification,
    astm_GASTMSourceObject,
    astm_OtherSyntaxObject,
    astm_RDBTableSpaceReference,
    astm_FunctionMemberAttributes,
    astm_ActualParameter,
    astm_BinaryOperator,
    astm_GASTMSemanticObject,
    astm_UnaryOperator,
    astm_GASTMObject,
    NameReference,
    astm_IdentifierReference,
    astm_TypeQualifiedIdentifierReference,
    astm_QualifiedIdentifierReference,
    Expression,
    astm_ConditionalExpression,
    astm_NewExpression,
    astm_AggregateExpression,
    astm_RDBSelectExpression,
    astm_FunctionCallExpression,
    astm_RangeExpression,
    astm_CastExpression,
    astm_Literal,
    astm_RDBHostVariableExpression,
    astm_ArrayAccess,
    astm_AnnotationExpression,
    astm_BinaryExpression,
    astm_UnaryExpression,
    astm_NameReference,
    CatchBlock,
    astm_VariableCatchBlock,
    astm_TypesCatchBlock,
    astm_CatchBlock,
    LoopStatement,
    astm_WhileStatement,
    astm_DoWhileStatement,
    astm_ForStatement,
    astm_LabelAccess,
    SwitchCase,
    astm_DefaultBlock,
    astm_CaseBlock,
    astm_SwitchCase,
    astm_BlockScope,
    Statement,
    astm_ReturnStatement,
    astm_EmptyStatement,
    astm_RDBInsertStatement,
    astm_SwitchStatement,
    astm_DeleteStatement,
    astm_ExpressionStatement,
    astm_LoopStatement,
    astm_LabeledStatement,
    astm_BreakStatement,
    astm_RDBCursorStatement,
    astm_ContinueStatement,
    astm_DeclarationOrDefinitionStatement,
    astm_BlockStatement,
    astm_RDBSelectStatement,
    astm_ThrowStatement,
    astm_JumpStatement,
    astm_RDBModifyStatement,
    astm_RDBConnectStatement,
    astm_TerminateStatement,
    astm_TryStatement,
    astm_IfStatement,
    astm_SpecificSelectStatement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_astm_visitable_is_not_abstract():
    assert not inspect.isabstract(astm_Visitable)


def test_astm_visitable_constructor_exists():
    assert callable(astm_Visitable.__init__)


def test_astm_visitable_constructor_args():
    sig = inspect.signature(astm_Visitable.__init__)
    params = list(sig.parameters.keys())



def test_rdbcolumntype_is_not_abstract():
    assert not inspect.isabstract(RDBColumnType)


def test_rdbcolumntype_constructor_exists():
    assert callable(RDBColumnType.__init__)


def test_rdbcolumntype_constructor_args():
    sig = inspect.signature(RDBColumnType.__init__)
    params = list(sig.parameters.keys())



def test_astm_rdbbfile_is_not_abstract():
    assert not inspect.isabstract(astm_RDBBFile)


def test_astm_rdbbfile_constructor_exists():
    assert callable(astm_RDBBFile.__init__)


def test_astm_rdbbfile_constructor_args():
    sig = inspect.signature(astm_RDBBFile.__init__)
    params = list(sig.parameters.keys())



def test_astm_rdbclob_is_not_abstract():
    assert not inspect.isabstract(astm_RDBClob)


def test_astm_rdbclob_constructor_exists():
    assert callable(astm_RDBClob.__init__)


def test_astm_rdbclob_constructor_args():
    sig = inspect.signature(astm_RDBClob.__init__)
    params = list(sig.parameters.keys())



def test_astm_rdbchar_is_not_abstract():
    assert not inspect.isabstract(astm_RDBChar)


def test_astm_rdbchar_constructor_exists():
    assert callable(astm_RDBChar.__init__)


def test_astm_rdbchar_constructor_args():
    sig = inspect.signature(astm_RDBChar.__init__)
    params = list(sig.parameters.keys())



def test_astm_rdbblob_is_not_abstract():
    assert not inspect.isabstract(astm_RDBBlob)


def test_astm_rdbblob_constructor_exists():
    assert callable(astm_RDBBlob.__init__)


def test_astm_rdbblob_constructor_args():
    sig = inspect.signature(astm_RDBBlob.__init__)
    params = list(sig.parameters.keys())



def test_astm_rdbnclob_is_not_abstract():
    assert not inspect.isabstract(astm_RDBNClob)


def test_astm_rdbnclob_constructor_exists():
    assert callable(astm_RDBNClob.__init__)


def test_astm_rdbnclob_constructor_args():
    sig = inspect.signature(astm_RDBNClob.__init__)
    params = list(sig.parameters.keys())



def test_astm_rdbint_is_not_abstract():
    assert not inspect.isabstract(astm_RDBInt)


def test_astm_rdbint_constructor_exists():
    assert callable(astm_RDBInt.__init__)


def test_astm_rdbint_constructor_args():
    sig = inspect.signature(astm_RDBInt.__init__)
    params = list(sig.parameters.keys())



def test_astm_rdbrowid_is_not_abstract():
    assert not inspect.isabstract(astm_RDBRowid)


def test_astm_rdbrowid_constructor_exists():
    assert callable(astm_RDBRowid.__init__)


def test_astm_rdbrowid_constructor_args():
    sig = inspect.signature(astm_RDBRowid.__init__)
    params = list(sig.parameters.keys())



def test_astm_rdbdate_is_not_abstract():
    assert not inspect.isabstract(astm_RDBDate)


def test_astm_rdbdate_constructor_exists():
    assert callable(astm_RDBDate.__init__)


def test_astm_rdbdate_constructor_args():
    sig = inspect.signature(astm_RDBDate.__init__)
    params = list(sig.parameters.keys())



def test_astm_rdblong_is_not_abstract():
    assert not inspect.isabstract(astm_RDBLong)


def test_astm_rdblong_constructor_exists():
    assert callable(astm_RDBLong.__init__)


def test_astm_rdblong_constructor_args():
    sig = inspect.signature(astm_RDBLong.__init__)
    params = list(sig.parameters.keys())



def test_astm_rdbtimestamp_is_not_abstract():
    assert not inspect.isabstract(astm_RDBTimestamp)


def test_astm_rdbtimestamp_constructor_exists():
    assert callable(astm_RDBTimestamp.__init__)


def test_astm_rdbtimestamp_constructor_args():
    sig = inspect.signature(astm_RDBTimestamp.__init__)
    params = list(sig.parameters.keys())



def test_astm_rdbboolean_is_not_abstract():
    assert not inspect.isabstract(astm_RDBBoolean)


def test_astm_rdbboolean_constructor_exists():
    assert callable(astm_RDBBoolean.__init__)


def test_astm_rdbboolean_constructor_args():
    sig = inspect.signature(astm_RDBBoolean.__init__)
    params = list(sig.parameters.keys())



def test_astm_rdbreal_is_not_abstract():
    assert not inspect.isabstract(astm_RDBReal)


def test_astm_rdbreal_constructor_exists():
    assert callable(astm_RDBReal.__init__)


def test_astm_rdbreal_constructor_args():
    sig = inspect.signature(astm_RDBReal.__init__)
    params = list(sig.parameters.keys())



def test_astm_rdbdecimal_is_not_abstract():
    assert not inspect.isabstract(astm_RDBDecimal)


def test_astm_rdbdecimal_constructor_exists():
    assert callable(astm_RDBDecimal.__init__)


def test_astm_rdbdecimal_constructor_args():
    sig = inspect.signature(astm_RDBDecimal.__init__)
    params = list(sig.parameters.keys())



def test_astm_rdbfloat_is_not_abstract():
    assert not inspect.isabstract(astm_RDBFloat)


def test_astm_rdbfloat_constructor_exists():
    assert callable(astm_RDBFloat.__init__)


def test_astm_rdbfloat_constructor_args():
    sig = inspect.signature(astm_RDBFloat.__init__)
    params = list(sig.parameters.keys())



def test_astm_rdbvarchar_is_not_abstract():
    assert not inspect.isabstract(astm_RDBVarchar)


def test_astm_rdbvarchar_constructor_exists():
    assert callable(astm_RDBVarchar.__init__)


def test_astm_rdbvarchar_constructor_args():
    sig = inspect.signature(astm_RDBVarchar.__init__)
    params = list(sig.parameters.keys())



def test_astm_rdbnumber_is_not_abstract():
    assert not inspect.isabstract(astm_RDBNumber)


def test_astm_rdbnumber_constructor_exists():
    assert callable(astm_RDBNumber.__init__)


def test_astm_rdbnumber_constructor_args():
    sig = inspect.signature(astm_RDBNumber.__init__)
    params = list(sig.parameters.keys())



def test_astm_rdbinteger_is_not_abstract():
    assert not inspect.isabstract(astm_RDBInteger)


def test_astm_rdbinteger_constructor_exists():
    assert callable(astm_RDBInteger.__init__)


def test_astm_rdbinteger_constructor_args():
    sig = inspect.signature(astm_RDBInteger.__init__)
    params = list(sig.parameters.keys())



def test_identifierreference_is_not_abstract():
    assert not inspect.isabstract(IdentifierReference)


def test_identifierreference_constructor_exists():
    assert callable(IdentifierReference.__init__)


def test_identifierreference_constructor_args():
    sig = inspect.signature(IdentifierReference.__init__)
    params = list(sig.parameters.keys())



def test_astm_rdbtablealias_is_not_abstract():
    assert not inspect.isabstract(astm_RDBTableAlias)


def test_astm_rdbtablealias_constructor_exists():
    assert callable(astm_RDBTableAlias.__init__)


def test_astm_rdbtablealias_constructor_args():
    sig = inspect.signature(astm_RDBTableAlias.__init__)
    params = list(sig.parameters.keys())



def test_astm_rdbraw_is_not_abstract():
    assert not inspect.isabstract(astm_RDBRaw)


def test_astm_rdbraw_constructor_exists():
    assert callable(astm_RDBRaw.__init__)


def test_astm_rdbraw_constructor_args():
    sig = inspect.signature(astm_RDBRaw.__init__)
    params = list(sig.parameters.keys())



def test_astm_rdbstring_is_not_abstract():
    assert not inspect.isabstract(astm_RDBString)


def test_astm_rdbstring_constructor_exists():
    assert callable(astm_RDBString.__init__)


def test_astm_rdbstring_constructor_args():
    sig = inspect.signature(astm_RDBString.__init__)
    params = list(sig.parameters.keys())



def test_rdbcursorstatement_is_not_abstract():
    assert not inspect.isabstract(RDBCursorStatement)


def test_rdbcursorstatement_constructor_exists():
    assert callable(RDBCursorStatement.__init__)


def test_rdbcursorstatement_constructor_args():
    sig = inspect.signature(RDBCursorStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm_rdbfetchcursorstatement_is_not_abstract():
    assert not inspect.isabstract(astm_RDBFetchCursorStatement)


def test_astm_rdbfetchcursorstatement_constructor_exists():
    assert callable(astm_RDBFetchCursorStatement.__init__)


def test_astm_rdbfetchcursorstatement_constructor_args():
    sig = inspect.signature(astm_RDBFetchCursorStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm_rdbclosecursorstatement_is_not_abstract():
    assert not inspect.isabstract(astm_RDBCloseCursorStatement)


def test_astm_rdbclosecursorstatement_constructor_exists():
    assert callable(astm_RDBCloseCursorStatement.__init__)


def test_astm_rdbclosecursorstatement_constructor_args():
    sig = inspect.signature(astm_RDBCloseCursorStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm_rdbopencursorstatement_is_not_abstract():
    assert not inspect.isabstract(astm_RDBOpenCursorStatement)


def test_astm_rdbopencursorstatement_constructor_exists():
    assert callable(astm_RDBOpenCursorStatement.__init__)


def test_astm_rdbopencursorstatement_constructor_args():
    sig = inspect.signature(astm_RDBOpenCursorStatement.__init__)
    params = list(sig.parameters.keys())



def test_rdbmodifystatement_is_not_abstract():
    assert not inspect.isabstract(RDBModifyStatement)


def test_rdbmodifystatement_constructor_exists():
    assert callable(RDBModifyStatement.__init__)


def test_rdbmodifystatement_constructor_args():
    sig = inspect.signature(RDBModifyStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm_rdbdeletestatement_is_not_abstract():
    assert not inspect.isabstract(astm_RDBDeleteStatement)


def test_astm_rdbdeletestatement_constructor_exists():
    assert callable(astm_RDBDeleteStatement.__init__)


def test_astm_rdbdeletestatement_constructor_args():
    sig = inspect.signature(astm_RDBDeleteStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm_rdbupdatestatement_is_not_abstract():
    assert not inspect.isabstract(astm_RDBUpdateStatement)


def test_astm_rdbupdatestatement_constructor_exists():
    assert callable(astm_RDBUpdateStatement.__init__)


def test_astm_rdbupdatestatement_constructor_args():
    sig = inspect.signature(astm_RDBUpdateStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm_rdbtablereference_is_not_abstract():
    assert not inspect.isabstract(astm_RDBTableReference)


def test_astm_rdbtablereference_constructor_exists():
    assert callable(astm_RDBTableReference.__init__)


def test_astm_rdbtablereference_constructor_args():
    sig = inspect.signature(astm_RDBTableReference.__init__)
    params = list(sig.parameters.keys())



def test_rdbconstraint_is_not_abstract():
    assert not inspect.isabstract(RDBConstraint)


def test_rdbconstraint_constructor_exists():
    assert callable(RDBConstraint.__init__)


def test_rdbconstraint_constructor_args():
    sig = inspect.signature(RDBConstraint.__init__)
    params = list(sig.parameters.keys())



def test_astm_rdbuniquekey_is_not_abstract():
    assert not inspect.isabstract(astm_RDBUniqueKey)


def test_astm_rdbuniquekey_constructor_exists():
    assert callable(astm_RDBUniqueKey.__init__)


def test_astm_rdbuniquekey_constructor_args():
    sig = inspect.signature(astm_RDBUniqueKey.__init__)
    params = list(sig.parameters.keys())



def test_astm_rdbrefintegrity_is_not_abstract():
    assert not inspect.isabstract(astm_RDBRefIntegrity)


def test_astm_rdbrefintegrity_constructor_exists():
    assert callable(astm_RDBRefIntegrity.__init__)


def test_astm_rdbrefintegrity_constructor_args():
    sig = inspect.signature(astm_RDBRefIntegrity.__init__)
    params = list(sig.parameters.keys())



def test_astm_rdbcheckconstraint_is_not_abstract():
    assert not inspect.isabstract(astm_RDBCheckConstraint)


def test_astm_rdbcheckconstraint_constructor_exists():
    assert callable(astm_RDBCheckConstraint.__init__)


def test_astm_rdbcheckconstraint_constructor_args():
    sig = inspect.signature(astm_RDBCheckConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "RDBConstraintText" in params, "Missing parameter 'RDBConstraintText'"
    assert "RDBConstraintType" in params, "Missing parameter 'RDBConstraintType'"

def test_astm_rdbcheckconstraint_has_RDBConstraintText():
    assert hasattr(astm_RDBCheckConstraint, "RDBConstraintText")
    descriptor = None
    for klass in astm_RDBCheckConstraint.__mro__:
        if "RDBConstraintText" in klass.__dict__:
            descriptor = klass.__dict__["RDBConstraintText"]
            break
    assert isinstance(descriptor, property)

def test_astm_rdbcheckconstraint_has_RDBConstraintType():
    assert hasattr(astm_RDBCheckConstraint, "RDBConstraintType")
    descriptor = None
    for klass in astm_RDBCheckConstraint.__mro__:
        if "RDBConstraintType" in klass.__dict__:
            descriptor = klass.__dict__["RDBConstraintType"]
            break
    assert isinstance(descriptor, property)



def test_astm_rdbcolumnreference_is_not_abstract():
    assert not inspect.isabstract(astm_RDBColumnReference)


def test_astm_rdbcolumnreference_constructor_exists():
    assert callable(astm_RDBColumnReference.__init__)


def test_astm_rdbcolumnreference_constructor_args():
    sig = inspect.signature(astm_RDBColumnReference.__init__)
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



def test_unaryoperator_is_not_abstract():
    assert not inspect.isabstract(UnaryOperator)


def test_unaryoperator_constructor_exists():
    assert callable(UnaryOperator.__init__)


def test_unaryoperator_constructor_args():
    sig = inspect.signature(UnaryOperator.__init__)
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



def test_astm_deref_is_not_abstract():
    assert not inspect.isabstract(astm_Deref)


def test_astm_deref_constructor_exists():
    assert callable(astm_Deref.__init__)


def test_astm_deref_constructor_args():
    sig = inspect.signature(astm_Deref.__init__)
    params = list(sig.parameters.keys())



def test_astm_postdecrement_is_not_abstract():
    assert not inspect.isabstract(astm_PostDecrement)


def test_astm_postdecrement_constructor_exists():
    assert callable(astm_PostDecrement.__init__)


def test_astm_postdecrement_constructor_args():
    sig = inspect.signature(astm_PostDecrement.__init__)
    params = list(sig.parameters.keys())



def test_astm_not_is_not_abstract():
    assert not inspect.isabstract(astm_Not)


def test_astm_not_constructor_exists():
    assert callable(astm_Not.__init__)


def test_astm_not_constructor_args():
    sig = inspect.signature(astm_Not.__init__)
    params = list(sig.parameters.keys())



def test_astm_postincrement_is_not_abstract():
    assert not inspect.isabstract(astm_PostIncrement)


def test_astm_postincrement_constructor_exists():
    assert callable(astm_PostIncrement.__init__)


def test_astm_postincrement_constructor_args():
    sig = inspect.signature(astm_PostIncrement.__init__)
    params = list(sig.parameters.keys())



def test_astm_addressof_is_not_abstract():
    assert not inspect.isabstract(astm_AddressOf)


def test_astm_addressof_constructor_exists():
    assert callable(astm_AddressOf.__init__)


def test_astm_addressof_constructor_args():
    sig = inspect.signature(astm_AddressOf.__init__)
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



def test_astm_charliteral_is_not_abstract():
    assert not inspect.isabstract(astm_CharLiteral)


def test_astm_charliteral_constructor_exists():
    assert callable(astm_CharLiteral.__init__)


def test_astm_charliteral_constructor_args():
    sig = inspect.signature(astm_CharLiteral.__init__)
    params = list(sig.parameters.keys())



def test_astm_bitliteral_is_not_abstract():
    assert not inspect.isabstract(astm_BitLiteral)


def test_astm_bitliteral_constructor_exists():
    assert callable(astm_BitLiteral.__init__)


def test_astm_bitliteral_constructor_args():
    sig = inspect.signature(astm_BitLiteral.__init__)
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



def test_astm_integerlliteral_is_not_abstract():
    assert not inspect.isabstract(astm_IntegerlLiteral)


def test_astm_integerlliteral_constructor_exists():
    assert callable(astm_IntegerlLiteral.__init__)


def test_astm_integerlliteral_constructor_args():
    sig = inspect.signature(astm_IntegerlLiteral.__init__)
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



def test_astm_protected_is_not_abstract():
    assert not inspect.isabstract(astm_Protected)


def test_astm_protected_constructor_exists():
    assert callable(astm_Protected.__init__)


def test_astm_protected_constructor_args():
    sig = inspect.signature(astm_Protected.__init__)
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



def test_astm_string_is_not_abstract():
    assert not inspect.isabstract(astm_String)


def test_astm_string_constructor_exists():
    assert callable(astm_String.__init__)


def test_astm_string_constructor_args():
    sig = inspect.signature(astm_String.__init__)
    params = list(sig.parameters.keys())



def test_astm_shortinteger_is_not_abstract():
    assert not inspect.isabstract(astm_ShortInteger)


def test_astm_shortinteger_constructor_exists():
    assert callable(astm_ShortInteger.__init__)


def test_astm_shortinteger_constructor_args():
    sig = inspect.signature(astm_ShortInteger.__init__)
    params = list(sig.parameters.keys())



def test_astm_longinteger_is_not_abstract():
    assert not inspect.isabstract(astm_LongInteger)


def test_astm_longinteger_constructor_exists():
    assert callable(astm_LongInteger.__init__)


def test_astm_longinteger_constructor_args():
    sig = inspect.signature(astm_LongInteger.__init__)
    params = list(sig.parameters.keys())



def test_astm_boolean_is_not_abstract():
    assert not inspect.isabstract(astm_Boolean)


def test_astm_boolean_constructor_exists():
    assert callable(astm_Boolean.__init__)


def test_astm_boolean_constructor_args():
    sig = inspect.signature(astm_Boolean.__init__)
    params = list(sig.parameters.keys())



def test_astm_widecharacter_is_not_abstract():
    assert not inspect.isabstract(astm_WideCharacter)


def test_astm_widecharacter_constructor_exists():
    assert callable(astm_WideCharacter.__init__)


def test_astm_widecharacter_constructor_args():
    sig = inspect.signature(astm_WideCharacter.__init__)
    params = list(sig.parameters.keys())



def test_astm_character_is_not_abstract():
    assert not inspect.isabstract(astm_Character)


def test_astm_character_constructor_exists():
    assert callable(astm_Character.__init__)


def test_astm_character_constructor_args():
    sig = inspect.signature(astm_Character.__init__)
    params = list(sig.parameters.keys())



def test_astm_longdouble_is_not_abstract():
    assert not inspect.isabstract(astm_LongDouble)


def test_astm_longdouble_constructor_exists():
    assert callable(astm_LongDouble.__init__)


def test_astm_longdouble_constructor_args():
    sig = inspect.signature(astm_LongDouble.__init__)
    params = list(sig.parameters.keys())



def test_astm_byte_is_not_abstract():
    assert not inspect.isabstract(astm_Byte)


def test_astm_byte_constructor_exists():
    assert callable(astm_Byte.__init__)


def test_astm_byte_constructor_args():
    sig = inspect.signature(astm_Byte.__init__)
    params = list(sig.parameters.keys())



def test_astm_double_is_not_abstract():
    assert not inspect.isabstract(astm_Double)


def test_astm_double_constructor_exists():
    assert callable(astm_Double.__init__)


def test_astm_double_constructor_args():
    sig = inspect.signature(astm_Double.__init__)
    params = list(sig.parameters.keys())



def test_astm_void_is_not_abstract():
    assert not inspect.isabstract(astm_Void)


def test_astm_void_constructor_exists():
    assert callable(astm_Void.__init__)


def test_astm_void_constructor_args():
    sig = inspect.signature(astm_Void.__init__)
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



def test_astm_filelocal_is_not_abstract():
    assert not inspect.isabstract(astm_FileLocal)


def test_astm_filelocal_constructor_exists():
    assert callable(astm_FileLocal.__init__)


def test_astm_filelocal_constructor_args():
    sig = inspect.signature(astm_FileLocal.__init__)
    params = list(sig.parameters.keys())



def test_astm_nodef_is_not_abstract():
    assert not inspect.isabstract(astm_NoDef)


def test_astm_nodef_constructor_exists():
    assert callable(astm_NoDef.__init__)


def test_astm_nodef_constructor_args():
    sig = inspect.signature(astm_NoDef.__init__)
    params = list(sig.parameters.keys())



def test_astm_functionpersistent_is_not_abstract():
    assert not inspect.isabstract(astm_FunctionPersistent)


def test_astm_functionpersistent_constructor_exists():
    assert callable(astm_FunctionPersistent.__init__)


def test_astm_functionpersistent_constructor_args():
    sig = inspect.signature(astm_FunctionPersistent.__init__)
    params = list(sig.parameters.keys())



def test_astm_perclassmember_is_not_abstract():
    assert not inspect.isabstract(astm_PerClassMember)


def test_astm_perclassmember_constructor_exists():
    assert callable(astm_PerClassMember.__init__)


def test_astm_perclassmember_constructor_args():
    sig = inspect.signature(astm_PerClassMember.__init__)
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



def test_astm_notequal_is_not_abstract():
    assert not inspect.isabstract(astm_NotEqual)


def test_astm_notequal_constructor_exists():
    assert callable(astm_NotEqual.__init__)


def test_astm_notequal_constructor_args():
    sig = inspect.signature(astm_NotEqual.__init__)
    params = list(sig.parameters.keys())



def test_astm_bitxor_is_not_abstract():
    assert not inspect.isabstract(astm_BitXor)


def test_astm_bitxor_constructor_exists():
    assert callable(astm_BitXor.__init__)


def test_astm_bitxor_constructor_args():
    sig = inspect.signature(astm_BitXor.__init__)
    params = list(sig.parameters.keys())



def test_astm_specificin_is_not_abstract():
    assert not inspect.isabstract(astm_SpecificIn)


def test_astm_specificin_constructor_exists():
    assert callable(astm_SpecificIn.__init__)


def test_astm_specificin_constructor_args():
    sig = inspect.signature(astm_SpecificIn.__init__)
    params = list(sig.parameters.keys())



def test_astm_specificlessequal_is_not_abstract():
    assert not inspect.isabstract(astm_SpecificLessEqual)


def test_astm_specificlessequal_constructor_exists():
    assert callable(astm_SpecificLessEqual.__init__)


def test_astm_specificlessequal_constructor_args():
    sig = inspect.signature(astm_SpecificLessEqual.__init__)
    params = list(sig.parameters.keys())



def test_astm_multiply_is_not_abstract():
    assert not inspect.isabstract(astm_Multiply)


def test_astm_multiply_constructor_exists():
    assert callable(astm_Multiply.__init__)


def test_astm_multiply_constructor_args():
    sig = inspect.signature(astm_Multiply.__init__)
    params = list(sig.parameters.keys())



def test_astm_bitrightshift_is_not_abstract():
    assert not inspect.isabstract(astm_BitRightShift)


def test_astm_bitrightshift_constructor_exists():
    assert callable(astm_BitRightShift.__init__)


def test_astm_bitrightshift_constructor_args():
    sig = inspect.signature(astm_BitRightShift.__init__)
    params = list(sig.parameters.keys())



def test_astm_less_is_not_abstract():
    assert not inspect.isabstract(astm_Less)


def test_astm_less_constructor_exists():
    assert callable(astm_Less.__init__)


def test_astm_less_constructor_args():
    sig = inspect.signature(astm_Less.__init__)
    params = list(sig.parameters.keys())



def test_astm_or_is_not_abstract():
    assert not inspect.isabstract(astm_Or)


def test_astm_or_constructor_exists():
    assert callable(astm_Or.__init__)


def test_astm_or_constructor_args():
    sig = inspect.signature(astm_Or.__init__)
    params = list(sig.parameters.keys())



def test_astm_specificlike_is_not_abstract():
    assert not inspect.isabstract(astm_SpecificLike)


def test_astm_specificlike_constructor_exists():
    assert callable(astm_SpecificLike.__init__)


def test_astm_specificlike_constructor_args():
    sig = inspect.signature(astm_SpecificLike.__init__)
    params = list(sig.parameters.keys())



def test_astm_exponent_is_not_abstract():
    assert not inspect.isabstract(astm_Exponent)


def test_astm_exponent_constructor_exists():
    assert callable(astm_Exponent.__init__)


def test_astm_exponent_constructor_args():
    sig = inspect.signature(astm_Exponent.__init__)
    params = list(sig.parameters.keys())



def test_astm_modulus_is_not_abstract():
    assert not inspect.isabstract(astm_Modulus)


def test_astm_modulus_constructor_exists():
    assert callable(astm_Modulus.__init__)


def test_astm_modulus_constructor_args():
    sig = inspect.signature(astm_Modulus.__init__)
    params = list(sig.parameters.keys())



def test_astm_equal_is_not_abstract():
    assert not inspect.isabstract(astm_Equal)


def test_astm_equal_constructor_exists():
    assert callable(astm_Equal.__init__)


def test_astm_equal_constructor_args():
    sig = inspect.signature(astm_Equal.__init__)
    params = list(sig.parameters.keys())



def test_astm_specificgreaterequal_is_not_abstract():
    assert not inspect.isabstract(astm_SpecificGreaterEqual)


def test_astm_specificgreaterequal_constructor_exists():
    assert callable(astm_SpecificGreaterEqual.__init__)


def test_astm_specificgreaterequal_constructor_args():
    sig = inspect.signature(astm_SpecificGreaterEqual.__init__)
    params = list(sig.parameters.keys())



def test_astm_specificconcatstring_is_not_abstract():
    assert not inspect.isabstract(astm_SpecificConcatString)


def test_astm_specificconcatstring_constructor_exists():
    assert callable(astm_SpecificConcatString.__init__)


def test_astm_specificconcatstring_constructor_args():
    sig = inspect.signature(astm_SpecificConcatString.__init__)
    params = list(sig.parameters.keys())



def test_astm_bitor_is_not_abstract():
    assert not inspect.isabstract(astm_BitOr)


def test_astm_bitor_constructor_exists():
    assert callable(astm_BitOr.__init__)


def test_astm_bitor_constructor_args():
    sig = inspect.signature(astm_BitOr.__init__)
    params = list(sig.parameters.keys())



def test_astm_and_is_not_abstract():
    assert not inspect.isabstract(astm_And)


def test_astm_and_constructor_exists():
    assert callable(astm_And.__init__)


def test_astm_and_constructor_args():
    sig = inspect.signature(astm_And.__init__)
    params = list(sig.parameters.keys())



def test_astm_divide_is_not_abstract():
    assert not inspect.isabstract(astm_Divide)


def test_astm_divide_constructor_exists():
    assert callable(astm_Divide.__init__)


def test_astm_divide_constructor_args():
    sig = inspect.signature(astm_Divide.__init__)
    params = list(sig.parameters.keys())



def test_astm_bitleftshift_is_not_abstract():
    assert not inspect.isabstract(astm_BitLeftShift)


def test_astm_bitleftshift_constructor_exists():
    assert callable(astm_BitLeftShift.__init__)


def test_astm_bitleftshift_constructor_args():
    sig = inspect.signature(astm_BitLeftShift.__init__)
    params = list(sig.parameters.keys())



def test_astm_add_is_not_abstract():
    assert not inspect.isabstract(astm_Add)


def test_astm_add_constructor_exists():
    assert callable(astm_Add.__init__)


def test_astm_add_constructor_args():
    sig = inspect.signature(astm_Add.__init__)
    params = list(sig.parameters.keys())



def test_astm_greater_is_not_abstract():
    assert not inspect.isabstract(astm_Greater)


def test_astm_greater_constructor_exists():
    assert callable(astm_Greater.__init__)


def test_astm_greater_constructor_args():
    sig = inspect.signature(astm_Greater.__init__)
    params = list(sig.parameters.keys())



def test_astm_subtract_is_not_abstract():
    assert not inspect.isabstract(astm_Subtract)


def test_astm_subtract_constructor_exists():
    assert callable(astm_Subtract.__init__)


def test_astm_subtract_constructor_args():
    sig = inspect.signature(astm_Subtract.__init__)
    params = list(sig.parameters.keys())



def test_astm_notgreater_is_not_abstract():
    assert not inspect.isabstract(astm_NotGreater)


def test_astm_notgreater_constructor_exists():
    assert callable(astm_NotGreater.__init__)


def test_astm_notgreater_constructor_args():
    sig = inspect.signature(astm_NotGreater.__init__)
    params = list(sig.parameters.keys())



def test_astm_assign_is_not_abstract():
    assert not inspect.isabstract(astm_Assign)


def test_astm_assign_constructor_exists():
    assert callable(astm_Assign.__init__)


def test_astm_assign_constructor_args():
    sig = inspect.signature(astm_Assign.__init__)
    params = list(sig.parameters.keys())



def test_astm_notless_is_not_abstract():
    assert not inspect.isabstract(astm_NotLess)


def test_astm_notless_constructor_exists():
    assert callable(astm_NotLess.__init__)


def test_astm_notless_constructor_args():
    sig = inspect.signature(astm_NotLess.__init__)
    params = list(sig.parameters.keys())



def test_astm_bitand_is_not_abstract():
    assert not inspect.isabstract(astm_BitAnd)


def test_astm_bitand_constructor_exists():
    assert callable(astm_BitAnd.__init__)


def test_astm_bitand_constructor_args():
    sig = inspect.signature(astm_BitAnd.__init__)
    params = list(sig.parameters.keys())



def test_astm_operatorassign_is_not_abstract():
    assert not inspect.isabstract(astm_OperatorAssign)


def test_astm_operatorassign_constructor_exists():
    assert callable(astm_OperatorAssign.__init__)


def test_astm_operatorassign_constructor_args():
    sig = inspect.signature(astm_OperatorAssign.__init__)
    params = list(sig.parameters.keys())



def test_typereference_is_not_abstract():
    assert not inspect.isabstract(TypeReference)


def test_typereference_constructor_exists():
    assert callable(TypeReference.__init__)


def test_typereference_constructor_args():
    sig = inspect.signature(TypeReference.__init__)
    params = list(sig.parameters.keys())



def test_astm_namedtypereference_is_not_abstract():
    assert not inspect.isabstract(astm_NamedTypeReference)


def test_astm_namedtypereference_constructor_exists():
    assert callable(astm_NamedTypeReference.__init__)


def test_astm_namedtypereference_constructor_args():
    sig = inspect.signature(astm_NamedTypeReference.__init__)
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



def test_astm_uniontype_is_not_abstract():
    assert not inspect.isabstract(astm_UnionType)


def test_astm_uniontype_constructor_exists():
    assert callable(astm_UnionType.__init__)


def test_astm_uniontype_constructor_args():
    sig = inspect.signature(astm_UnionType.__init__)
    params = list(sig.parameters.keys())



def test_astm_annotationtype_is_not_abstract():
    assert not inspect.isabstract(astm_AnnotationType)


def test_astm_annotationtype_constructor_exists():
    assert callable(astm_AnnotationType.__init__)


def test_astm_annotationtype_constructor_args():
    sig = inspect.signature(astm_AnnotationType.__init__)
    params = list(sig.parameters.keys())



def test_astm_structuretype_is_not_abstract():
    assert not inspect.isabstract(astm_StructureType)


def test_astm_structuretype_constructor_exists():
    assert callable(astm_StructureType.__init__)


def test_astm_structuretype_constructor_args():
    sig = inspect.signature(astm_StructureType.__init__)
    params = list(sig.parameters.keys())



def test_astm_classtype_is_not_abstract():
    assert not inspect.isabstract(astm_ClassType)


def test_astm_classtype_constructor_exists():
    assert callable(astm_ClassType.__init__)


def test_astm_classtype_constructor_args():
    sig = inspect.signature(astm_ClassType.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_astm_functiontype_is_not_abstract():
    assert not inspect.isabstract(astm_FunctionType)


def test_astm_functiontype_constructor_exists():
    assert callable(astm_FunctionType.__init__)


def test_astm_functiontype_constructor_args():
    sig = inspect.signature(astm_FunctionType.__init__)
    params = list(sig.parameters.keys())



def test_constructedtype_is_not_abstract():
    assert not inspect.isabstract(ConstructedType)


def test_constructedtype_constructor_exists():
    assert callable(ConstructedType.__init__)


def test_constructedtype_constructor_args():
    sig = inspect.signature(ConstructedType.__init__)
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



def test_astm_collectiontype_is_not_abstract():
    assert not inspect.isabstract(astm_CollectionType)


def test_astm_collectiontype_constructor_exists():
    assert callable(astm_CollectionType.__init__)


def test_astm_collectiontype_constructor_args():
    sig = inspect.signature(astm_CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_astm_rangetype_is_not_abstract():
    assert not inspect.isabstract(astm_RangeType)


def test_astm_rangetype_constructor_exists():
    assert callable(astm_RangeType.__init__)


def test_astm_rangetype_constructor_args():
    sig = inspect.signature(astm_RangeType.__init__)
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



def test_datatype_is_not_abstract():
    assert not inspect.isabstract(DataType)


def test_datatype_constructor_exists():
    assert callable(DataType.__init__)


def test_datatype_constructor_args():
    sig = inspect.signature(DataType.__init__)
    params = list(sig.parameters.keys())



def test_astm_enumtype_is_not_abstract():
    assert not inspect.isabstract(astm_EnumType)


def test_astm_enumtype_constructor_exists():
    assert callable(astm_EnumType.__init__)


def test_astm_enumtype_constructor_args():
    sig = inspect.signature(astm_EnumType.__init__)
    params = list(sig.parameters.keys())



def test_astm_rdbdatabasetype_is_not_abstract():
    assert not inspect.isabstract(astm_RDBDataBaseType)


def test_astm_rdbdatabasetype_constructor_exists():
    assert callable(astm_RDBDataBaseType.__init__)


def test_astm_rdbdatabasetype_constructor_args():
    sig = inspect.signature(astm_RDBDataBaseType.__init__)
    params = list(sig.parameters.keys())



def test_astm_rdbcursortype_is_not_abstract():
    assert not inspect.isabstract(astm_RDBCursorType)


def test_astm_rdbcursortype_constructor_exists():
    assert callable(astm_RDBCursorType.__init__)


def test_astm_rdbcursortype_constructor_args():
    sig = inspect.signature(astm_RDBCursorType.__init__)
    params = list(sig.parameters.keys())



def test_astm_rdbtabletype_is_not_abstract():
    assert not inspect.isabstract(astm_RDBTableType)


def test_astm_rdbtabletype_constructor_exists():
    assert callable(astm_RDBTableType.__init__)


def test_astm_rdbtabletype_constructor_args():
    sig = inspect.signature(astm_RDBTableType.__init__)
    params = list(sig.parameters.keys())



def test_astm_exceptiontype_is_not_abstract():
    assert not inspect.isabstract(astm_ExceptionType)


def test_astm_exceptiontype_constructor_exists():
    assert callable(astm_ExceptionType.__init__)


def test_astm_exceptiontype_constructor_args():
    sig = inspect.signature(astm_ExceptionType.__init__)
    params = list(sig.parameters.keys())



def test_astm_rdbusertype_is_not_abstract():
    assert not inspect.isabstract(astm_RDBUserType)


def test_astm_rdbusertype_constructor_exists():
    assert callable(astm_RDBUserType.__init__)


def test_astm_rdbusertype_constructor_args():
    sig = inspect.signature(astm_RDBUserType.__init__)
    params = list(sig.parameters.keys())



def test_astm_rdbcolumntype_is_not_abstract():
    assert not inspect.isabstract(astm_RDBColumnType)


def test_astm_rdbcolumntype_constructor_exists():
    assert callable(astm_RDBColumnType.__init__)


def test_astm_rdbcolumntype_constructor_args():
    sig = inspect.signature(astm_RDBColumnType.__init__)
    params = list(sig.parameters.keys())



def test_astm_formalparametertype_is_not_abstract():
    assert not inspect.isabstract(astm_FormalParameterType)


def test_astm_formalparametertype_constructor_exists():
    assert callable(astm_FormalParameterType.__init__)


def test_astm_formalparametertype_constructor_args():
    sig = inspect.signature(astm_FormalParameterType.__init__)
    params = list(sig.parameters.keys())



def test_astm_constructedtype_is_not_abstract():
    assert not inspect.isabstract(astm_ConstructedType)


def test_astm_constructedtype_constructor_exists():
    assert callable(astm_ConstructedType.__init__)


def test_astm_constructedtype_constructor_args():
    sig = inspect.signature(astm_ConstructedType.__init__)
    params = list(sig.parameters.keys())



def test_astm_rdbtablespacetype_is_not_abstract():
    assert not inspect.isabstract(astm_RDBTableSpaceType)


def test_astm_rdbtablespacetype_constructor_exists():
    assert callable(astm_RDBTableSpaceType.__init__)


def test_astm_rdbtablespacetype_constructor_args():
    sig = inspect.signature(astm_RDBTableSpaceType.__init__)
    params = list(sig.parameters.keys())



def test_astm_rdbviewtype_is_not_abstract():
    assert not inspect.isabstract(astm_RDBViewType)


def test_astm_rdbviewtype_constructor_exists():
    assert callable(astm_RDBViewType.__init__)


def test_astm_rdbviewtype_constructor_args():
    sig = inspect.signature(astm_RDBViewType.__init__)
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



def test_gastmsyntaxobject_is_not_abstract():
    assert not inspect.isabstract(GASTMSyntaxObject)


def test_gastmsyntaxobject_constructor_exists():
    assert callable(GASTMSyntaxObject.__init__)


def test_gastmsyntaxobject_constructor_args():
    sig = inspect.signature(GASTMSyntaxObject.__init__)
    params = list(sig.parameters.keys())



def test_astm_type_is_not_abstract():
    assert not inspect.isabstract(astm_Type)


def test_astm_type_constructor_exists():
    assert callable(astm_Type.__init__)


def test_astm_type_constructor_args():
    sig = inspect.signature(astm_Type.__init__)
    params = list(sig.parameters.keys())
    assert "isVolatile" in params, "Missing parameter 'isVolatile'"
    assert "isConst" in params, "Missing parameter 'isConst'"

def test_astm_type_has_isVolatile():
    assert hasattr(astm_Type, "isVolatile")
    descriptor = None
    for klass in astm_Type.__mro__:
        if "isVolatile" in klass.__dict__:
            descriptor = klass.__dict__["isVolatile"]
            break
    assert isinstance(descriptor, property)

def test_astm_type_has_isConst():
    assert hasattr(astm_Type, "isConst")
    descriptor = None
    for klass in astm_Type.__mro__:
        if "isConst" in klass.__dict__:
            descriptor = klass.__dict__["isConst"]
            break
    assert isinstance(descriptor, property)



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
    assert "macroName" in params, "Missing parameter 'macroName'"
    assert "body" in params, "Missing parameter 'body'"

def test_astm_macrodefinition_has_macroName():
    assert hasattr(astm_MacroDefinition, "macroName")
    descriptor = None
    for klass in astm_MacroDefinition.__mro__:
        if "macroName" in klass.__dict__:
            descriptor = klass.__dict__["macroName"]
            break
    assert isinstance(descriptor, property)

def test_astm_macrodefinition_has_body():
    assert hasattr(astm_MacroDefinition, "body")
    descriptor = None
    for klass in astm_MacroDefinition.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)



def test_astm_macrocall_is_not_abstract():
    assert not inspect.isabstract(astm_MacroCall)


def test_astm_macrocall_constructor_exists():
    assert callable(astm_MacroCall.__init__)


def test_astm_macrocall_constructor_args():
    sig = inspect.signature(astm_MacroCall.__init__)
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



def test_astm_includeunit_is_not_abstract():
    assert not inspect.isabstract(astm_IncludeUnit)


def test_astm_includeunit_constructor_exists():
    assert callable(astm_IncludeUnit.__init__)


def test_astm_includeunit_constructor_args():
    sig = inspect.signature(astm_IncludeUnit.__init__)
    params = list(sig.parameters.keys())



def test_astm_labeltype_is_not_abstract():
    assert not inspect.isabstract(astm_LabelType)


def test_astm_labeltype_constructor_exists():
    assert callable(astm_LabelType.__init__)


def test_astm_labeltype_constructor_args():
    sig = inspect.signature(astm_LabelType.__init__)
    params = list(sig.parameters.keys())



def test_astm_namespacetype_is_not_abstract():
    assert not inspect.isabstract(astm_NameSpaceType)


def test_astm_namespacetype_constructor_exists():
    assert callable(astm_NameSpaceType.__init__)


def test_astm_namespacetype_constructor_args():
    sig = inspect.signature(astm_NameSpaceType.__init__)
    params = list(sig.parameters.keys())



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



def test_datadefinition_is_not_abstract():
    assert not inspect.isabstract(DataDefinition)


def test_datadefinition_constructor_exists():
    assert callable(DataDefinition.__init__)


def test_datadefinition_constructor_args():
    sig = inspect.signature(DataDefinition.__init__)
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



def test_astm_expression_is_not_abstract():
    assert not inspect.isabstract(astm_Expression)


def test_astm_expression_constructor_exists():
    assert callable(astm_Expression.__init__)


def test_astm_expression_constructor_args():
    sig = inspect.signature(astm_Expression.__init__)
    params = list(sig.parameters.keys())



def test_astm_typereference_is_not_abstract():
    assert not inspect.isabstract(astm_TypeReference)


def test_astm_typereference_constructor_exists():
    assert callable(astm_TypeReference.__init__)


def test_astm_typereference_constructor_args():
    sig = inspect.signature(astm_TypeReference.__init__)
    params = list(sig.parameters.keys())



def test_astm_functionscope_is_not_abstract():
    assert not inspect.isabstract(astm_FunctionScope)


def test_astm_functionscope_constructor_exists():
    assert callable(astm_FunctionScope.__init__)


def test_astm_functionscope_constructor_args():
    sig = inspect.signature(astm_FunctionScope.__init__)
    params = list(sig.parameters.keys())



def test_astm_statement_is_not_abstract():
    assert not inspect.isabstract(astm_Statement)


def test_astm_statement_constructor_exists():
    assert callable(astm_Statement.__init__)


def test_astm_statement_constructor_args():
    sig = inspect.signature(astm_Statement.__init__)
    params = list(sig.parameters.keys())



def test_astm_formalparameterdefinition_is_not_abstract():
    assert not inspect.isabstract(astm_FormalParameterDefinition)


def test_astm_formalparameterdefinition_constructor_exists():
    assert callable(astm_FormalParameterDefinition.__init__)


def test_astm_formalparameterdefinition_constructor_args():
    sig = inspect.signature(astm_FormalParameterDefinition.__init__)
    params = list(sig.parameters.keys())



def test_definition_is_not_abstract():
    assert not inspect.isabstract(Definition)


def test_definition_constructor_exists():
    assert callable(Definition.__init__)


def test_definition_constructor_args():
    sig = inspect.signature(Definition.__init__)
    params = list(sig.parameters.keys())



def test_astm_rdbuserdefinition_is_not_abstract():
    assert not inspect.isabstract(astm_RDBUserDefinition)


def test_astm_rdbuserdefinition_constructor_exists():
    assert callable(astm_RDBUserDefinition.__init__)


def test_astm_rdbuserdefinition_constructor_args():
    sig = inspect.signature(astm_RDBUserDefinition.__init__)
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



def test_astm_rdbtabledefinition_is_not_abstract():
    assert not inspect.isabstract(astm_RDBTableDefinition)


def test_astm_rdbtabledefinition_constructor_exists():
    assert callable(astm_RDBTableDefinition.__init__)


def test_astm_rdbtabledefinition_constructor_args():
    sig = inspect.signature(astm_RDBTableDefinition.__init__)
    params = list(sig.parameters.keys())



def test_astm_entrydefinition_is_not_abstract():
    assert not inspect.isabstract(astm_EntryDefinition)


def test_astm_entrydefinition_constructor_exists():
    assert callable(astm_EntryDefinition.__init__)


def test_astm_entrydefinition_constructor_args():
    sig = inspect.signature(astm_EntryDefinition.__init__)
    params = list(sig.parameters.keys())



def test_astm_rdbcursordefinition_is_not_abstract():
    assert not inspect.isabstract(astm_RDBCursorDefinition)


def test_astm_rdbcursordefinition_constructor_exists():
    assert callable(astm_RDBCursorDefinition.__init__)


def test_astm_rdbcursordefinition_constructor_args():
    sig = inspect.signature(astm_RDBCursorDefinition.__init__)
    params = list(sig.parameters.keys())



def test_astm_rdbcolumndefinition_is_not_abstract():
    assert not inspect.isabstract(astm_RDBColumnDefinition)


def test_astm_rdbcolumndefinition_constructor_exists():
    assert callable(astm_RDBColumnDefinition.__init__)


def test_astm_rdbcolumndefinition_constructor_args():
    sig = inspect.signature(astm_RDBColumnDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "NotNull" in params, "Missing parameter 'NotNull'"

def test_astm_rdbcolumndefinition_has_NotNull():
    assert hasattr(astm_RDBColumnDefinition, "NotNull")
    descriptor = None
    for klass in astm_RDBColumnDefinition.__mro__:
        if "NotNull" in klass.__dict__:
            descriptor = klass.__dict__["NotNull"]
            break
    assert isinstance(descriptor, property)



def test_astm_specifictriggerdefinition_is_not_abstract():
    assert not inspect.isabstract(astm_SpecificTriggerDefinition)


def test_astm_specifictriggerdefinition_constructor_exists():
    assert callable(astm_SpecificTriggerDefinition.__init__)


def test_astm_specifictriggerdefinition_constructor_args():
    sig = inspect.signature(astm_SpecificTriggerDefinition.__init__)
    params = list(sig.parameters.keys())



def test_astm_enumliteraldefinition_is_not_abstract():
    assert not inspect.isabstract(astm_EnumLiteralDefinition)


def test_astm_enumliteraldefinition_constructor_exists():
    assert callable(astm_EnumLiteralDefinition.__init__)


def test_astm_enumliteraldefinition_constructor_args():
    sig = inspect.signature(astm_EnumLiteralDefinition.__init__)
    params = list(sig.parameters.keys())



def test_astm_rdbviewdefinition_is_not_abstract():
    assert not inspect.isabstract(astm_RDBViewDefinition)


def test_astm_rdbviewdefinition_constructor_exists():
    assert callable(astm_RDBViewDefinition.__init__)


def test_astm_rdbviewdefinition_constructor_args():
    sig = inspect.signature(astm_RDBViewDefinition.__init__)
    params = list(sig.parameters.keys())



def test_astm_rdbtablespacedefinition_is_not_abstract():
    assert not inspect.isabstract(astm_RDBTableSpaceDefinition)


def test_astm_rdbtablespacedefinition_constructor_exists():
    assert callable(astm_RDBTableSpaceDefinition.__init__)


def test_astm_rdbtablespacedefinition_constructor_args():
    sig = inspect.signature(astm_RDBTableSpaceDefinition.__init__)
    params = list(sig.parameters.keys())



def test_astm_rdbdatabasedefinition_is_not_abstract():
    assert not inspect.isabstract(astm_RDBDatabaseDefinition)


def test_astm_rdbdatabasedefinition_constructor_exists():
    assert callable(astm_RDBDatabaseDefinition.__init__)


def test_astm_rdbdatabasedefinition_constructor_args():
    sig = inspect.signature(astm_RDBDatabaseDefinition.__init__)
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



def test_astm_formalparameterdeclaration_is_not_abstract():
    assert not inspect.isabstract(astm_FormalParameterDeclaration)


def test_astm_formalparameterdeclaration_constructor_exists():
    assert callable(astm_FormalParameterDeclaration.__init__)


def test_astm_formalparameterdeclaration_constructor_args():
    sig = inspect.signature(astm_FormalParameterDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_astm_functiondeclaration_is_not_abstract():
    assert not inspect.isabstract(astm_FunctionDeclaration)


def test_astm_functiondeclaration_constructor_exists():
    assert callable(astm_FunctionDeclaration.__init__)


def test_astm_functiondeclaration_constructor_args():
    sig = inspect.signature(astm_FunctionDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_gastmsemanticobject_is_not_abstract():
    assert not inspect.isabstract(GASTMSemanticObject)


def test_gastmsemanticobject_constructor_exists():
    assert callable(GASTMSemanticObject.__init__)


def test_gastmsemanticobject_constructor_args():
    sig = inspect.signature(GASTMSemanticObject.__init__)
    params = list(sig.parameters.keys())



def test_astm_project_is_not_abstract():
    assert not inspect.isabstract(astm_Project)


def test_astm_project_constructor_exists():
    assert callable(astm_Project.__init__)


def test_astm_project_constructor_args():
    sig = inspect.signature(astm_Project.__init__)
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



def test_astm_labeldefinition_is_not_abstract():
    assert not inspect.isabstract(astm_LabelDefinition)


def test_astm_labeldefinition_constructor_exists():
    assert callable(astm_LabelDefinition.__init__)


def test_astm_labeldefinition_constructor_args():
    sig = inspect.signature(astm_LabelDefinition.__init__)
    params = list(sig.parameters.keys())



def test_astm_namespacedefinition_is_not_abstract():
    assert not inspect.isabstract(astm_NameSpaceDefinition)


def test_astm_namespacedefinition_constructor_exists():
    assert callable(astm_NameSpaceDefinition.__init__)


def test_astm_namespacedefinition_constructor_args():
    sig = inspect.signature(astm_NameSpaceDefinition.__init__)
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



def test_astm_virtualspecification_is_not_abstract():
    assert not inspect.isabstract(astm_VirtualSpecification)


def test_astm_virtualspecification_constructor_exists():
    assert callable(astm_VirtualSpecification.__init__)


def test_astm_virtualspecification_constructor_args():
    sig = inspect.signature(astm_VirtualSpecification.__init__)
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



def test_astm_dimension_is_not_abstract():
    assert not inspect.isabstract(astm_Dimension)


def test_astm_dimension_constructor_exists():
    assert callable(astm_Dimension.__init__)


def test_astm_dimension_constructor_args():
    sig = inspect.signature(astm_Dimension.__init__)
    params = list(sig.parameters.keys())



def test_astm_rdbtrigger_is_not_abstract():
    assert not inspect.isabstract(astm_RDBTrigger)


def test_astm_rdbtrigger_constructor_exists():
    assert callable(astm_RDBTrigger.__init__)


def test_astm_rdbtrigger_constructor_args():
    sig = inspect.signature(astm_RDBTrigger.__init__)
    params = list(sig.parameters.keys())



def test_astm_rdbindexcolumn_is_not_abstract():
    assert not inspect.isabstract(astm_RDBIndexColumn)


def test_astm_rdbindexcolumn_constructor_exists():
    assert callable(astm_RDBIndexColumn.__init__)


def test_astm_rdbindexcolumn_constructor_args():
    sig = inspect.signature(astm_RDBIndexColumn.__init__)
    params = list(sig.parameters.keys())
    assert "AscendingOrDescending" in params, "Missing parameter 'AscendingOrDescending'"

def test_astm_rdbindexcolumn_has_AscendingOrDescending():
    assert hasattr(astm_RDBIndexColumn, "AscendingOrDescending")
    descriptor = None
    for klass in astm_RDBIndexColumn.__mro__:
        if "AscendingOrDescending" in klass.__dict__:
            descriptor = klass.__dict__["AscendingOrDescending"]
            break
    assert isinstance(descriptor, property)



def test_astm_functionmemberattribute_is_not_abstract():
    assert not inspect.isabstract(astm_FunctionMemberAttribute)


def test_astm_functionmemberattribute_constructor_exists():
    assert callable(astm_FunctionMemberAttribute.__init__)


def test_astm_functionmemberattribute_constructor_args():
    sig = inspect.signature(astm_FunctionMemberAttribute.__init__)
    params = list(sig.parameters.keys())



def test_astm_rdbindex_is_not_abstract():
    assert not inspect.isabstract(astm_RDBIndex)


def test_astm_rdbindex_constructor_exists():
    assert callable(astm_RDBIndex.__init__)


def test_astm_rdbindex_constructor_args():
    sig = inspect.signature(astm_RDBIndex.__init__)
    params = list(sig.parameters.keys())
    assert "IsUnique" in params, "Missing parameter 'IsUnique'"
    assert "NotNull" in params, "Missing parameter 'NotNull'"

def test_astm_rdbindex_has_IsUnique():
    assert hasattr(astm_RDBIndex, "IsUnique")
    descriptor = None
    for klass in astm_RDBIndex.__mro__:
        if "IsUnique" in klass.__dict__:
            descriptor = klass.__dict__["IsUnique"]
            break
    assert isinstance(descriptor, property)

def test_astm_rdbindex_has_NotNull():
    assert hasattr(astm_RDBIndex, "NotNull")
    descriptor = None
    for klass in astm_RDBIndex.__mro__:
        if "NotNull" in klass.__dict__:
            descriptor = klass.__dict__["NotNull"]
            break
    assert isinstance(descriptor, property)



def test_astm_rdbconstraint_is_not_abstract():
    assert not inspect.isabstract(astm_RDBConstraint)


def test_astm_rdbconstraint_constructor_exists():
    assert callable(astm_RDBConstraint.__init__)


def test_astm_rdbconstraint_constructor_args():
    sig = inspect.signature(astm_RDBConstraint.__init__)
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



def test_astm_preprocessorelement_is_not_abstract():
    assert not inspect.isabstract(astm_PreprocessorElement)


def test_astm_preprocessorelement_constructor_exists():
    assert callable(astm_PreprocessorElement.__init__)


def test_astm_preprocessorelement_constructor_args():
    sig = inspect.signature(astm_PreprocessorElement.__init__)
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



def test_astm_definitionobject_is_not_abstract():
    assert not inspect.isabstract(astm_DefinitionObject)


def test_astm_definitionobject_constructor_exists():
    assert callable(astm_DefinitionObject.__init__)


def test_astm_definitionobject_constructor_args():
    sig = inspect.signature(astm_DefinitionObject.__init__)
    params = list(sig.parameters.keys())



def test_astm_scope_is_not_abstract():
    assert not inspect.isabstract(astm_Scope)


def test_astm_scope_constructor_exists():
    assert callable(astm_Scope.__init__)


def test_astm_scope_constructor_args():
    sig = inspect.signature(astm_Scope.__init__)
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



def test_gastmsourceobject_is_not_abstract():
    assert not inspect.isabstract(GASTMSourceObject)


def test_gastmsourceobject_constructor_exists():
    assert callable(GASTMSourceObject.__init__)


def test_gastmsourceobject_constructor_args():
    sig = inspect.signature(GASTMSourceObject.__init__)
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



def test_visitable_is_not_abstract():
    assert not inspect.isabstract(Visitable)


def test_visitable_constructor_exists():
    assert callable(Visitable.__init__)


def test_visitable_constructor_args():
    sig = inspect.signature(Visitable.__init__)
    params = list(sig.parameters.keys())



def test_astm_rdbhostvariablereference_is_not_abstract():
    assert not inspect.isabstract(astm_RDBHostVariableReference)


def test_astm_rdbhostvariablereference_constructor_exists():
    assert callable(astm_RDBHostVariableReference.__init__)


def test_astm_rdbhostvariablereference_constructor_args():
    sig = inspect.signature(astm_RDBHostVariableReference.__init__)
    params = list(sig.parameters.keys())



def test_astm_accesskind_is_not_abstract():
    assert not inspect.isabstract(astm_AccessKind)


def test_astm_accesskind_constructor_exists():
    assert callable(astm_AccessKind.__init__)


def test_astm_accesskind_constructor_args():
    sig = inspect.signature(astm_AccessKind.__init__)
    params = list(sig.parameters.keys())



def test_astm_datatype_is_not_abstract():
    assert not inspect.isabstract(astm_DataType)


def test_astm_datatype_constructor_exists():
    assert callable(astm_DataType.__init__)


def test_astm_datatype_constructor_args():
    sig = inspect.signature(astm_DataType.__init__)
    params = list(sig.parameters.keys())



def test_astm_storagespecification_is_not_abstract():
    assert not inspect.isabstract(astm_StorageSpecification)


def test_astm_storagespecification_constructor_exists():
    assert callable(astm_StorageSpecification.__init__)


def test_astm_storagespecification_constructor_args():
    sig = inspect.signature(astm_StorageSpecification.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastmsourceobject_is_not_abstract():
    assert not inspect.isabstract(astm_GASTMSourceObject)


def test_astm_gastmsourceobject_constructor_exists():
    assert callable(astm_GASTMSourceObject.__init__)


def test_astm_gastmsourceobject_constructor_args():
    sig = inspect.signature(astm_GASTMSourceObject.__init__)
    params = list(sig.parameters.keys())



def test_astm_othersyntaxobject_is_not_abstract():
    assert not inspect.isabstract(astm_OtherSyntaxObject)


def test_astm_othersyntaxobject_constructor_exists():
    assert callable(astm_OtherSyntaxObject.__init__)


def test_astm_othersyntaxobject_constructor_args():
    sig = inspect.signature(astm_OtherSyntaxObject.__init__)
    params = list(sig.parameters.keys())



def test_astm_rdbtablespacereference_is_not_abstract():
    assert not inspect.isabstract(astm_RDBTableSpaceReference)


def test_astm_rdbtablespacereference_constructor_exists():
    assert callable(astm_RDBTableSpaceReference.__init__)


def test_astm_rdbtablespacereference_constructor_args():
    sig = inspect.signature(astm_RDBTableSpaceReference.__init__)
    params = list(sig.parameters.keys())



def test_astm_functionmemberattributes_is_not_abstract():
    assert not inspect.isabstract(astm_FunctionMemberAttributes)


def test_astm_functionmemberattributes_constructor_exists():
    assert callable(astm_FunctionMemberAttributes.__init__)


def test_astm_functionmemberattributes_constructor_args():
    sig = inspect.signature(astm_FunctionMemberAttributes.__init__)
    params = list(sig.parameters.keys())
    assert "isThisConst" in params, "Missing parameter 'isThisConst'"
    assert "isFriend" in params, "Missing parameter 'isFriend'"
    assert "isInline" in params, "Missing parameter 'isInline'"

def test_astm_functionmemberattributes_has_isThisConst():
    assert hasattr(astm_FunctionMemberAttributes, "isThisConst")
    descriptor = None
    for klass in astm_FunctionMemberAttributes.__mro__:
        if "isThisConst" in klass.__dict__:
            descriptor = klass.__dict__["isThisConst"]
            break
    assert isinstance(descriptor, property)

def test_astm_functionmemberattributes_has_isFriend():
    assert hasattr(astm_FunctionMemberAttributes, "isFriend")
    descriptor = None
    for klass in astm_FunctionMemberAttributes.__mro__:
        if "isFriend" in klass.__dict__:
            descriptor = klass.__dict__["isFriend"]
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



def test_astm_actualparameter_is_not_abstract():
    assert not inspect.isabstract(astm_ActualParameter)


def test_astm_actualparameter_constructor_exists():
    assert callable(astm_ActualParameter.__init__)


def test_astm_actualparameter_constructor_args():
    sig = inspect.signature(astm_ActualParameter.__init__)
    params = list(sig.parameters.keys())



def test_astm_binaryoperator_is_not_abstract():
    assert not inspect.isabstract(astm_BinaryOperator)


def test_astm_binaryoperator_constructor_exists():
    assert callable(astm_BinaryOperator.__init__)


def test_astm_binaryoperator_constructor_args():
    sig = inspect.signature(astm_BinaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastmsemanticobject_is_not_abstract():
    assert not inspect.isabstract(astm_GASTMSemanticObject)


def test_astm_gastmsemanticobject_constructor_exists():
    assert callable(astm_GASTMSemanticObject.__init__)


def test_astm_gastmsemanticobject_constructor_args():
    sig = inspect.signature(astm_GASTMSemanticObject.__init__)
    params = list(sig.parameters.keys())



def test_astm_unaryoperator_is_not_abstract():
    assert not inspect.isabstract(astm_UnaryOperator)


def test_astm_unaryoperator_constructor_exists():
    assert callable(astm_UnaryOperator.__init__)


def test_astm_unaryoperator_constructor_args():
    sig = inspect.signature(astm_UnaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_astm_gastmobject_is_not_abstract():
    assert not inspect.isabstract(astm_GASTMObject)


def test_astm_gastmobject_constructor_exists():
    assert callable(astm_GASTMObject.__init__)


def test_astm_gastmobject_constructor_args():
    sig = inspect.signature(astm_GASTMObject.__init__)
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



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_astm_conditionalexpression_is_not_abstract():
    assert not inspect.isabstract(astm_ConditionalExpression)


def test_astm_conditionalexpression_constructor_exists():
    assert callable(astm_ConditionalExpression.__init__)


def test_astm_conditionalexpression_constructor_args():
    sig = inspect.signature(astm_ConditionalExpression.__init__)
    params = list(sig.parameters.keys())



def test_astm_newexpression_is_not_abstract():
    assert not inspect.isabstract(astm_NewExpression)


def test_astm_newexpression_constructor_exists():
    assert callable(astm_NewExpression.__init__)


def test_astm_newexpression_constructor_args():
    sig = inspect.signature(astm_NewExpression.__init__)
    params = list(sig.parameters.keys())



def test_astm_aggregateexpression_is_not_abstract():
    assert not inspect.isabstract(astm_AggregateExpression)


def test_astm_aggregateexpression_constructor_exists():
    assert callable(astm_AggregateExpression.__init__)


def test_astm_aggregateexpression_constructor_args():
    sig = inspect.signature(astm_AggregateExpression.__init__)
    params = list(sig.parameters.keys())



def test_astm_rdbselectexpression_is_not_abstract():
    assert not inspect.isabstract(astm_RDBSelectExpression)


def test_astm_rdbselectexpression_constructor_exists():
    assert callable(astm_RDBSelectExpression.__init__)


def test_astm_rdbselectexpression_constructor_args():
    sig = inspect.signature(astm_RDBSelectExpression.__init__)
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



def test_astm_castexpression_is_not_abstract():
    assert not inspect.isabstract(astm_CastExpression)


def test_astm_castexpression_constructor_exists():
    assert callable(astm_CastExpression.__init__)


def test_astm_castexpression_constructor_args():
    sig = inspect.signature(astm_CastExpression.__init__)
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



def test_astm_rdbhostvariableexpression_is_not_abstract():
    assert not inspect.isabstract(astm_RDBHostVariableExpression)


def test_astm_rdbhostvariableexpression_constructor_exists():
    assert callable(astm_RDBHostVariableExpression.__init__)


def test_astm_rdbhostvariableexpression_constructor_args():
    sig = inspect.signature(astm_RDBHostVariableExpression.__init__)
    params = list(sig.parameters.keys())



def test_astm_arrayaccess_is_not_abstract():
    assert not inspect.isabstract(astm_ArrayAccess)


def test_astm_arrayaccess_constructor_exists():
    assert callable(astm_ArrayAccess.__init__)


def test_astm_arrayaccess_constructor_args():
    sig = inspect.signature(astm_ArrayAccess.__init__)
    params = list(sig.parameters.keys())



def test_astm_annotationexpression_is_not_abstract():
    assert not inspect.isabstract(astm_AnnotationExpression)


def test_astm_annotationexpression_constructor_exists():
    assert callable(astm_AnnotationExpression.__init__)


def test_astm_annotationexpression_constructor_args():
    sig = inspect.signature(astm_AnnotationExpression.__init__)
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



def test_astm_namereference_is_not_abstract():
    assert not inspect.isabstract(astm_NameReference)


def test_astm_namereference_constructor_exists():
    assert callable(astm_NameReference.__init__)


def test_astm_namereference_constructor_args():
    sig = inspect.signature(astm_NameReference.__init__)
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



def test_astm_catchblock_is_not_abstract():
    assert not inspect.isabstract(astm_CatchBlock)


def test_astm_catchblock_constructor_exists():
    assert callable(astm_CatchBlock.__init__)


def test_astm_catchblock_constructor_args():
    sig = inspect.signature(astm_CatchBlock.__init__)
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



def test_astm_labelaccess_is_not_abstract():
    assert not inspect.isabstract(astm_LabelAccess)


def test_astm_labelaccess_constructor_exists():
    assert callable(astm_LabelAccess.__init__)


def test_astm_labelaccess_constructor_args():
    sig = inspect.signature(astm_LabelAccess.__init__)
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



def test_astm_switchcase_is_not_abstract():
    assert not inspect.isabstract(astm_SwitchCase)


def test_astm_switchcase_constructor_exists():
    assert callable(astm_SwitchCase.__init__)


def test_astm_switchcase_constructor_args():
    sig = inspect.signature(astm_SwitchCase.__init__)
    params = list(sig.parameters.keys())



def test_astm_blockscope_is_not_abstract():
    assert not inspect.isabstract(astm_BlockScope)


def test_astm_blockscope_constructor_exists():
    assert callable(astm_BlockScope.__init__)


def test_astm_blockscope_constructor_args():
    sig = inspect.signature(astm_BlockScope.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_astm_returnstatement_is_not_abstract():
    assert not inspect.isabstract(astm_ReturnStatement)


def test_astm_returnstatement_constructor_exists():
    assert callable(astm_ReturnStatement.__init__)


def test_astm_returnstatement_constructor_args():
    sig = inspect.signature(astm_ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm_emptystatement_is_not_abstract():
    assert not inspect.isabstract(astm_EmptyStatement)


def test_astm_emptystatement_constructor_exists():
    assert callable(astm_EmptyStatement.__init__)


def test_astm_emptystatement_constructor_args():
    sig = inspect.signature(astm_EmptyStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm_rdbinsertstatement_is_not_abstract():
    assert not inspect.isabstract(astm_RDBInsertStatement)


def test_astm_rdbinsertstatement_constructor_exists():
    assert callable(astm_RDBInsertStatement.__init__)


def test_astm_rdbinsertstatement_constructor_args():
    sig = inspect.signature(astm_RDBInsertStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm_switchstatement_is_not_abstract():
    assert not inspect.isabstract(astm_SwitchStatement)


def test_astm_switchstatement_constructor_exists():
    assert callable(astm_SwitchStatement.__init__)


def test_astm_switchstatement_constructor_args():
    sig = inspect.signature(astm_SwitchStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm_deletestatement_is_not_abstract():
    assert not inspect.isabstract(astm_DeleteStatement)


def test_astm_deletestatement_constructor_exists():
    assert callable(astm_DeleteStatement.__init__)


def test_astm_deletestatement_constructor_args():
    sig = inspect.signature(astm_DeleteStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm_expressionstatement_is_not_abstract():
    assert not inspect.isabstract(astm_ExpressionStatement)


def test_astm_expressionstatement_constructor_exists():
    assert callable(astm_ExpressionStatement.__init__)


def test_astm_expressionstatement_constructor_args():
    sig = inspect.signature(astm_ExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm_loopstatement_is_not_abstract():
    assert not inspect.isabstract(astm_LoopStatement)


def test_astm_loopstatement_constructor_exists():
    assert callable(astm_LoopStatement.__init__)


def test_astm_loopstatement_constructor_args():
    sig = inspect.signature(astm_LoopStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm_labeledstatement_is_not_abstract():
    assert not inspect.isabstract(astm_LabeledStatement)


def test_astm_labeledstatement_constructor_exists():
    assert callable(astm_LabeledStatement.__init__)


def test_astm_labeledstatement_constructor_args():
    sig = inspect.signature(astm_LabeledStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm_breakstatement_is_not_abstract():
    assert not inspect.isabstract(astm_BreakStatement)


def test_astm_breakstatement_constructor_exists():
    assert callable(astm_BreakStatement.__init__)


def test_astm_breakstatement_constructor_args():
    sig = inspect.signature(astm_BreakStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm_rdbcursorstatement_is_not_abstract():
    assert not inspect.isabstract(astm_RDBCursorStatement)


def test_astm_rdbcursorstatement_constructor_exists():
    assert callable(astm_RDBCursorStatement.__init__)


def test_astm_rdbcursorstatement_constructor_args():
    sig = inspect.signature(astm_RDBCursorStatement.__init__)
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



def test_astm_blockstatement_is_not_abstract():
    assert not inspect.isabstract(astm_BlockStatement)


def test_astm_blockstatement_constructor_exists():
    assert callable(astm_BlockStatement.__init__)


def test_astm_blockstatement_constructor_args():
    sig = inspect.signature(astm_BlockStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm_rdbselectstatement_is_not_abstract():
    assert not inspect.isabstract(astm_RDBSelectStatement)


def test_astm_rdbselectstatement_constructor_exists():
    assert callable(astm_RDBSelectStatement.__init__)


def test_astm_rdbselectstatement_constructor_args():
    sig = inspect.signature(astm_RDBSelectStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm_throwstatement_is_not_abstract():
    assert not inspect.isabstract(astm_ThrowStatement)


def test_astm_throwstatement_constructor_exists():
    assert callable(astm_ThrowStatement.__init__)


def test_astm_throwstatement_constructor_args():
    sig = inspect.signature(astm_ThrowStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm_jumpstatement_is_not_abstract():
    assert not inspect.isabstract(astm_JumpStatement)


def test_astm_jumpstatement_constructor_exists():
    assert callable(astm_JumpStatement.__init__)


def test_astm_jumpstatement_constructor_args():
    sig = inspect.signature(astm_JumpStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm_rdbmodifystatement_is_not_abstract():
    assert not inspect.isabstract(astm_RDBModifyStatement)


def test_astm_rdbmodifystatement_constructor_exists():
    assert callable(astm_RDBModifyStatement.__init__)


def test_astm_rdbmodifystatement_constructor_args():
    sig = inspect.signature(astm_RDBModifyStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm_rdbconnectstatement_is_not_abstract():
    assert not inspect.isabstract(astm_RDBConnectStatement)


def test_astm_rdbconnectstatement_constructor_exists():
    assert callable(astm_RDBConnectStatement.__init__)


def test_astm_rdbconnectstatement_constructor_args():
    sig = inspect.signature(astm_RDBConnectStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm_terminatestatement_is_not_abstract():
    assert not inspect.isabstract(astm_TerminateStatement)


def test_astm_terminatestatement_constructor_exists():
    assert callable(astm_TerminateStatement.__init__)


def test_astm_terminatestatement_constructor_args():
    sig = inspect.signature(astm_TerminateStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm_trystatement_is_not_abstract():
    assert not inspect.isabstract(astm_TryStatement)


def test_astm_trystatement_constructor_exists():
    assert callable(astm_TryStatement.__init__)


def test_astm_trystatement_constructor_args():
    sig = inspect.signature(astm_TryStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm_ifstatement_is_not_abstract():
    assert not inspect.isabstract(astm_IfStatement)


def test_astm_ifstatement_constructor_exists():
    assert callable(astm_IfStatement.__init__)


def test_astm_ifstatement_constructor_args():
    sig = inspect.signature(astm_IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_astm_specificselectstatement_is_not_abstract():
    assert not inspect.isabstract(astm_SpecificSelectStatement)


def test_astm_specificselectstatement_constructor_exists():
    assert callable(astm_SpecificSelectStatement.__init__)


def test_astm_specificselectstatement_constructor_args():
    sig = inspect.signature(astm_SpecificSelectStatement.__init__)
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
astm_Visitable_strategy = st.builds(
    astm_Visitable,
)
RDBColumnType_strategy = st.builds(
    RDBColumnType,
)
astm_RDBBFile_strategy = st.builds(
    astm_RDBBFile,
)
astm_RDBClob_strategy = st.builds(
    astm_RDBClob,
)
astm_RDBChar_strategy = st.builds(
    astm_RDBChar,
)
astm_RDBBlob_strategy = st.builds(
    astm_RDBBlob,
)
astm_RDBNClob_strategy = st.builds(
    astm_RDBNClob,
)
astm_RDBInt_strategy = st.builds(
    astm_RDBInt,
)
astm_RDBRowid_strategy = st.builds(
    astm_RDBRowid,
)
astm_RDBDate_strategy = st.builds(
    astm_RDBDate,
)
astm_RDBLong_strategy = st.builds(
    astm_RDBLong,
)
astm_RDBTimestamp_strategy = st.builds(
    astm_RDBTimestamp,
)
astm_RDBBoolean_strategy = st.builds(
    astm_RDBBoolean,
)
astm_RDBReal_strategy = st.builds(
    astm_RDBReal,
)
astm_RDBDecimal_strategy = st.builds(
    astm_RDBDecimal,
)
astm_RDBFloat_strategy = st.builds(
    astm_RDBFloat,
)
astm_RDBVarchar_strategy = st.builds(
    astm_RDBVarchar,
)
astm_RDBNumber_strategy = st.builds(
    astm_RDBNumber,
)
astm_RDBInteger_strategy = st.builds(
    astm_RDBInteger,
)
IdentifierReference_strategy = st.builds(
    IdentifierReference,
)
astm_RDBTableAlias_strategy = st.builds(
    astm_RDBTableAlias,
)
astm_RDBRaw_strategy = st.builds(
    astm_RDBRaw,
)
astm_RDBString_strategy = st.builds(
    astm_RDBString,
)
RDBCursorStatement_strategy = st.builds(
    RDBCursorStatement,
)
astm_RDBFetchCursorStatement_strategy = st.builds(
    astm_RDBFetchCursorStatement,
)
astm_RDBCloseCursorStatement_strategy = st.builds(
    astm_RDBCloseCursorStatement,
)
astm_RDBOpenCursorStatement_strategy = st.builds(
    astm_RDBOpenCursorStatement,
)
RDBModifyStatement_strategy = st.builds(
    RDBModifyStatement,
)
astm_RDBDeleteStatement_strategy = st.builds(
    astm_RDBDeleteStatement,
)
astm_RDBUpdateStatement_strategy = st.builds(
    astm_RDBUpdateStatement,
)
astm_RDBTableReference_strategy = st.builds(
    astm_RDBTableReference,
)
RDBConstraint_strategy = st.builds(
    RDBConstraint,
)
astm_RDBUniqueKey_strategy = st.builds(
    astm_RDBUniqueKey,
)
astm_RDBRefIntegrity_strategy = st.builds(
    astm_RDBRefIntegrity,
)
astm_RDBCheckConstraint_strategy = st.builds(
    astm_RDBCheckConstraint,
    RDBConstraintText=
        safe_text,
    RDBConstraintType=
        safe_text
)
astm_RDBColumnReference_strategy = st.builds(
    astm_RDBColumnReference,
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
UnaryOperator_strategy = st.builds(
    UnaryOperator,
)
astm_Decrement_strategy = st.builds(
    astm_Decrement,
)
astm_Increment_strategy = st.builds(
    astm_Increment,
)
astm_Deref_strategy = st.builds(
    astm_Deref,
)
astm_PostDecrement_strategy = st.builds(
    astm_PostDecrement,
)
astm_Not_strategy = st.builds(
    astm_Not,
)
astm_PostIncrement_strategy = st.builds(
    astm_PostIncrement,
)
astm_AddressOf_strategy = st.builds(
    astm_AddressOf,
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
astm_CharLiteral_strategy = st.builds(
    astm_CharLiteral,
)
astm_BitLiteral_strategy = st.builds(
    astm_BitLiteral,
)
astm_BooleanLiteral_strategy = st.builds(
    astm_BooleanLiteral,
)
astm_StringLiteral_strategy = st.builds(
    astm_StringLiteral,
)
astm_IntegerlLiteral_strategy = st.builds(
    astm_IntegerlLiteral,
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
astm_Protected_strategy = st.builds(
    astm_Protected,
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
astm_String_strategy = st.builds(
    astm_String,
)
astm_ShortInteger_strategy = st.builds(
    astm_ShortInteger,
)
astm_LongInteger_strategy = st.builds(
    astm_LongInteger,
)
astm_Boolean_strategy = st.builds(
    astm_Boolean,
)
astm_WideCharacter_strategy = st.builds(
    astm_WideCharacter,
)
astm_Character_strategy = st.builds(
    astm_Character,
)
astm_LongDouble_strategy = st.builds(
    astm_LongDouble,
)
astm_Byte_strategy = st.builds(
    astm_Byte,
)
astm_Double_strategy = st.builds(
    astm_Double,
)
astm_Void_strategy = st.builds(
    astm_Void,
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
astm_FileLocal_strategy = st.builds(
    astm_FileLocal,
)
astm_NoDef_strategy = st.builds(
    astm_NoDef,
)
astm_FunctionPersistent_strategy = st.builds(
    astm_FunctionPersistent,
)
astm_PerClassMember_strategy = st.builds(
    astm_PerClassMember,
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
astm_NotEqual_strategy = st.builds(
    astm_NotEqual,
)
astm_BitXor_strategy = st.builds(
    astm_BitXor,
)
astm_SpecificIn_strategy = st.builds(
    astm_SpecificIn,
)
astm_SpecificLessEqual_strategy = st.builds(
    astm_SpecificLessEqual,
)
astm_Multiply_strategy = st.builds(
    astm_Multiply,
)
astm_BitRightShift_strategy = st.builds(
    astm_BitRightShift,
)
astm_Less_strategy = st.builds(
    astm_Less,
)
astm_Or_strategy = st.builds(
    astm_Or,
)
astm_SpecificLike_strategy = st.builds(
    astm_SpecificLike,
)
astm_Exponent_strategy = st.builds(
    astm_Exponent,
)
astm_Modulus_strategy = st.builds(
    astm_Modulus,
)
astm_Equal_strategy = st.builds(
    astm_Equal,
)
astm_SpecificGreaterEqual_strategy = st.builds(
    astm_SpecificGreaterEqual,
)
astm_SpecificConcatString_strategy = st.builds(
    astm_SpecificConcatString,
)
astm_BitOr_strategy = st.builds(
    astm_BitOr,
)
astm_And_strategy = st.builds(
    astm_And,
)
astm_Divide_strategy = st.builds(
    astm_Divide,
)
astm_BitLeftShift_strategy = st.builds(
    astm_BitLeftShift,
)
astm_Add_strategy = st.builds(
    astm_Add,
)
astm_Greater_strategy = st.builds(
    astm_Greater,
)
astm_Subtract_strategy = st.builds(
    astm_Subtract,
)
astm_NotGreater_strategy = st.builds(
    astm_NotGreater,
)
astm_Assign_strategy = st.builds(
    astm_Assign,
)
astm_NotLess_strategy = st.builds(
    astm_NotLess,
)
astm_BitAnd_strategy = st.builds(
    astm_BitAnd,
)
astm_OperatorAssign_strategy = st.builds(
    astm_OperatorAssign,
)
TypeReference_strategy = st.builds(
    TypeReference,
)
astm_NamedTypeReference_strategy = st.builds(
    astm_NamedTypeReference,
)
astm_UnnamedTypeReference_strategy = st.builds(
    astm_UnnamedTypeReference,
)
AggregateType_strategy = st.builds(
    AggregateType,
)
astm_UnionType_strategy = st.builds(
    astm_UnionType,
)
astm_AnnotationType_strategy = st.builds(
    astm_AnnotationType,
)
astm_StructureType_strategy = st.builds(
    astm_StructureType,
)
astm_ClassType_strategy = st.builds(
    astm_ClassType,
)
Type_strategy = st.builds(
    Type,
)
astm_FunctionType_strategy = st.builds(
    astm_FunctionType,
)
ConstructedType_strategy = st.builds(
    ConstructedType,
)
astm_PointerType_strategy = st.builds(
    astm_PointerType,
)
astm_ReferenceType_strategy = st.builds(
    astm_ReferenceType,
)
astm_CollectionType_strategy = st.builds(
    astm_CollectionType,
)
astm_RangeType_strategy = st.builds(
    astm_RangeType,
)
astm_ArrayType_strategy = st.builds(
    astm_ArrayType,
)
astm_AggregateScope_strategy = st.builds(
    astm_AggregateScope,
)
DataType_strategy = st.builds(
    DataType,
)
astm_EnumType_strategy = st.builds(
    astm_EnumType,
)
astm_RDBDataBaseType_strategy = st.builds(
    astm_RDBDataBaseType,
)
astm_RDBCursorType_strategy = st.builds(
    astm_RDBCursorType,
)
astm_RDBTableType_strategy = st.builds(
    astm_RDBTableType,
)
astm_ExceptionType_strategy = st.builds(
    astm_ExceptionType,
)
astm_RDBUserType_strategy = st.builds(
    astm_RDBUserType,
)
astm_RDBColumnType_strategy = st.builds(
    astm_RDBColumnType,
)
astm_FormalParameterType_strategy = st.builds(
    astm_FormalParameterType,
)
astm_ConstructedType_strategy = st.builds(
    astm_ConstructedType,
)
astm_RDBTableSpaceType_strategy = st.builds(
    astm_RDBTableSpaceType,
)
astm_RDBViewType_strategy = st.builds(
    astm_RDBViewType,
)
astm_PrimitiveType_strategy = st.builds(
    astm_PrimitiveType,
    isSigned=
        st.booleans()
)
GASTMSyntaxObject_strategy = st.builds(
    GASTMSyntaxObject,
)
astm_Type_strategy = st.builds(
    astm_Type,
    isVolatile=
        st.booleans(),
    isConst=
        st.booleans()
)
PreprocessorElement_strategy = st.builds(
    PreprocessorElement,
)
astm_MacroDefinition_strategy = st.builds(
    astm_MacroDefinition,
    macroName=
        safe_text,
    body=
        safe_text
)
astm_MacroCall_strategy = st.builds(
    astm_MacroCall,
)
astm_Comment_strategy = st.builds(
    astm_Comment,
    text=
        safe_text
)
astm_IncludeUnit_strategy = st.builds(
    astm_IncludeUnit,
)
astm_LabelType_strategy = st.builds(
    astm_LabelType,
)
astm_NameSpaceType_strategy = st.builds(
    astm_NameSpaceType,
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
DataDefinition_strategy = st.builds(
    DataDefinition,
)
astm_VariableDefinition_strategy = st.builds(
    astm_VariableDefinition,
)
astm_BitFieldDefinition_strategy = st.builds(
    astm_BitFieldDefinition,
)
astm_Expression_strategy = st.builds(
    astm_Expression,
)
astm_TypeReference_strategy = st.builds(
    astm_TypeReference,
)
astm_FunctionScope_strategy = st.builds(
    astm_FunctionScope,
)
astm_Statement_strategy = st.builds(
    astm_Statement,
)
astm_FormalParameterDefinition_strategy = st.builds(
    astm_FormalParameterDefinition,
)
Definition_strategy = st.builds(
    Definition,
)
astm_RDBUserDefinition_strategy = st.builds(
    astm_RDBUserDefinition,
)
astm_DataDefinition_strategy = st.builds(
    astm_DataDefinition,
    isMutable=
        st.booleans()
)
astm_RDBTableDefinition_strategy = st.builds(
    astm_RDBTableDefinition,
)
astm_EntryDefinition_strategy = st.builds(
    astm_EntryDefinition,
)
astm_RDBCursorDefinition_strategy = st.builds(
    astm_RDBCursorDefinition,
)
astm_RDBColumnDefinition_strategy = st.builds(
    astm_RDBColumnDefinition,
    NotNull=
        st.booleans()
)
astm_SpecificTriggerDefinition_strategy = st.builds(
    astm_SpecificTriggerDefinition,
)
astm_EnumLiteralDefinition_strategy = st.builds(
    astm_EnumLiteralDefinition,
)
astm_RDBViewDefinition_strategy = st.builds(
    astm_RDBViewDefinition,
)
astm_RDBTableSpaceDefinition_strategy = st.builds(
    astm_RDBTableSpaceDefinition,
)
astm_RDBDatabaseDefinition_strategy = st.builds(
    astm_RDBDatabaseDefinition,
)
astm_FunctionDefinition_strategy = st.builds(
    astm_FunctionDefinition,
)
Declaration_strategy = st.builds(
    Declaration,
)
astm_VariableDeclaration_strategy = st.builds(
    astm_VariableDeclaration,
    isMutable=
        st.booleans()
)
astm_FormalParameterDeclaration_strategy = st.builds(
    astm_FormalParameterDeclaration,
)
astm_FunctionDeclaration_strategy = st.builds(
    astm_FunctionDeclaration,
)
GASTMSemanticObject_strategy = st.builds(
    GASTMSemanticObject,
)
astm_Project_strategy = st.builds(
    astm_Project,
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
DefinitionObject_strategy = st.builds(
    DefinitionObject,
)
astm_TypeDefinition_strategy = st.builds(
    astm_TypeDefinition,
)
astm_LabelDefinition_strategy = st.builds(
    astm_LabelDefinition,
)
astm_NameSpaceDefinition_strategy = st.builds(
    astm_NameSpaceDefinition,
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
astm_VirtualSpecification_strategy = st.builds(
    astm_VirtualSpecification,
)
astm_DerivesFrom_strategy = st.builds(
    astm_DerivesFrom,
    isVirtual=
        st.booleans()
)
astm_Dimension_strategy = st.builds(
    astm_Dimension,
)
astm_RDBTrigger_strategy = st.builds(
    astm_RDBTrigger,
)
astm_RDBIndexColumn_strategy = st.builds(
    astm_RDBIndexColumn,
    AscendingOrDescending=
        safe_text
)
astm_FunctionMemberAttribute_strategy = st.builds(
    astm_FunctionMemberAttribute,
)
astm_RDBIndex_strategy = st.builds(
    astm_RDBIndex,
    IsUnique=
        st.booleans(),
    NotNull=
        st.booleans()
)
astm_RDBConstraint_strategy = st.builds(
    astm_RDBConstraint,
)
astm_Name_strategy = st.builds(
    astm_Name,
    nameString=
        safe_text
)
astm_PreprocessorElement_strategy = st.builds(
    astm_PreprocessorElement,
)
GASTMObject_strategy = st.builds(
    GASTMObject,
)
astm_GASTMSyntaxObject_strategy = st.builds(
    astm_GASTMSyntaxObject,
)
astm_DefinitionObject_strategy = st.builds(
    astm_DefinitionObject,
)
astm_Scope_strategy = st.builds(
    astm_Scope,
)
astm_GlobalScope_strategy = st.builds(
    astm_GlobalScope,
)
astm_CompilationUnit_strategy = st.builds(
    astm_CompilationUnit,
    language=
        safe_text
)
GASTMSourceObject_strategy = st.builds(
    GASTMSourceObject,
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
astm_SourceFile_strategy = st.builds(
    astm_SourceFile,
    pathName=
        safe_text
)
Visitable_strategy = st.builds(
    Visitable,
)
astm_RDBHostVariableReference_strategy = st.builds(
    astm_RDBHostVariableReference,
)
astm_AccessKind_strategy = st.builds(
    astm_AccessKind,
)
astm_DataType_strategy = st.builds(
    astm_DataType,
)
astm_StorageSpecification_strategy = st.builds(
    astm_StorageSpecification,
)
astm_GASTMSourceObject_strategy = st.builds(
    astm_GASTMSourceObject,
)
astm_OtherSyntaxObject_strategy = st.builds(
    astm_OtherSyntaxObject,
)
astm_RDBTableSpaceReference_strategy = st.builds(
    astm_RDBTableSpaceReference,
)
astm_FunctionMemberAttributes_strategy = st.builds(
    astm_FunctionMemberAttributes,
    isThisConst=
        st.booleans(),
    isFriend=
        st.booleans(),
    isInline=
        st.booleans()
)
astm_ActualParameter_strategy = st.builds(
    astm_ActualParameter,
)
astm_BinaryOperator_strategy = st.builds(
    astm_BinaryOperator,
)
astm_GASTMSemanticObject_strategy = st.builds(
    astm_GASTMSemanticObject,
)
astm_UnaryOperator_strategy = st.builds(
    astm_UnaryOperator,
)
astm_GASTMObject_strategy = st.builds(
    astm_GASTMObject,
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
Expression_strategy = st.builds(
    Expression,
)
astm_ConditionalExpression_strategy = st.builds(
    astm_ConditionalExpression,
)
astm_NewExpression_strategy = st.builds(
    astm_NewExpression,
)
astm_AggregateExpression_strategy = st.builds(
    astm_AggregateExpression,
)
astm_RDBSelectExpression_strategy = st.builds(
    astm_RDBSelectExpression,
)
astm_FunctionCallExpression_strategy = st.builds(
    astm_FunctionCallExpression,
)
astm_RangeExpression_strategy = st.builds(
    astm_RangeExpression,
)
astm_CastExpression_strategy = st.builds(
    astm_CastExpression,
)
astm_Literal_strategy = st.builds(
    astm_Literal,
    value=
        safe_text
)
astm_RDBHostVariableExpression_strategy = st.builds(
    astm_RDBHostVariableExpression,
)
astm_ArrayAccess_strategy = st.builds(
    astm_ArrayAccess,
)
astm_AnnotationExpression_strategy = st.builds(
    astm_AnnotationExpression,
)
astm_BinaryExpression_strategy = st.builds(
    astm_BinaryExpression,
)
astm_UnaryExpression_strategy = st.builds(
    astm_UnaryExpression,
)
astm_NameReference_strategy = st.builds(
    astm_NameReference,
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
astm_CatchBlock_strategy = st.builds(
    astm_CatchBlock,
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
astm_LabelAccess_strategy = st.builds(
    astm_LabelAccess,
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
astm_SwitchCase_strategy = st.builds(
    astm_SwitchCase,
)
astm_BlockScope_strategy = st.builds(
    astm_BlockScope,
)
Statement_strategy = st.builds(
    Statement,
)
astm_ReturnStatement_strategy = st.builds(
    astm_ReturnStatement,
)
astm_EmptyStatement_strategy = st.builds(
    astm_EmptyStatement,
)
astm_RDBInsertStatement_strategy = st.builds(
    astm_RDBInsertStatement,
)
astm_SwitchStatement_strategy = st.builds(
    astm_SwitchStatement,
)
astm_DeleteStatement_strategy = st.builds(
    astm_DeleteStatement,
)
astm_ExpressionStatement_strategy = st.builds(
    astm_ExpressionStatement,
)
astm_LoopStatement_strategy = st.builds(
    astm_LoopStatement,
)
astm_LabeledStatement_strategy = st.builds(
    astm_LabeledStatement,
)
astm_BreakStatement_strategy = st.builds(
    astm_BreakStatement,
)
astm_RDBCursorStatement_strategy = st.builds(
    astm_RDBCursorStatement,
)
astm_ContinueStatement_strategy = st.builds(
    astm_ContinueStatement,
)
astm_DeclarationOrDefinitionStatement_strategy = st.builds(
    astm_DeclarationOrDefinitionStatement,
)
astm_BlockStatement_strategy = st.builds(
    astm_BlockStatement,
)
astm_RDBSelectStatement_strategy = st.builds(
    astm_RDBSelectStatement,
)
astm_ThrowStatement_strategy = st.builds(
    astm_ThrowStatement,
)
astm_JumpStatement_strategy = st.builds(
    astm_JumpStatement,
)
astm_RDBModifyStatement_strategy = st.builds(
    astm_RDBModifyStatement,
)
astm_RDBConnectStatement_strategy = st.builds(
    astm_RDBConnectStatement,
)
astm_TerminateStatement_strategy = st.builds(
    astm_TerminateStatement,
)
astm_TryStatement_strategy = st.builds(
    astm_TryStatement,
)
astm_IfStatement_strategy = st.builds(
    astm_IfStatement,
)
astm_SpecificSelectStatement_strategy = st.builds(
    astm_SpecificSelectStatement,
)

@given(instance=astm_Visitable_strategy)
@settings(max_examples=50)
def test_astm_visitable_instantiation(instance):
    assert isinstance(instance, astm_Visitable)

@given(instance=RDBColumnType_strategy)
@settings(max_examples=50)
def test_rdbcolumntype_instantiation(instance):
    assert isinstance(instance, RDBColumnType)

@given(instance=astm_RDBBFile_strategy)
@settings(max_examples=50)
def test_astm_rdbbfile_instantiation(instance):
    assert isinstance(instance, astm_RDBBFile)

@given(instance=astm_RDBClob_strategy)
@settings(max_examples=50)
def test_astm_rdbclob_instantiation(instance):
    assert isinstance(instance, astm_RDBClob)

@given(instance=astm_RDBChar_strategy)
@settings(max_examples=50)
def test_astm_rdbchar_instantiation(instance):
    assert isinstance(instance, astm_RDBChar)

@given(instance=astm_RDBBlob_strategy)
@settings(max_examples=50)
def test_astm_rdbblob_instantiation(instance):
    assert isinstance(instance, astm_RDBBlob)

@given(instance=astm_RDBNClob_strategy)
@settings(max_examples=50)
def test_astm_rdbnclob_instantiation(instance):
    assert isinstance(instance, astm_RDBNClob)

@given(instance=astm_RDBInt_strategy)
@settings(max_examples=50)
def test_astm_rdbint_instantiation(instance):
    assert isinstance(instance, astm_RDBInt)

@given(instance=astm_RDBRowid_strategy)
@settings(max_examples=50)
def test_astm_rdbrowid_instantiation(instance):
    assert isinstance(instance, astm_RDBRowid)

@given(instance=astm_RDBDate_strategy)
@settings(max_examples=50)
def test_astm_rdbdate_instantiation(instance):
    assert isinstance(instance, astm_RDBDate)

@given(instance=astm_RDBLong_strategy)
@settings(max_examples=50)
def test_astm_rdblong_instantiation(instance):
    assert isinstance(instance, astm_RDBLong)

@given(instance=astm_RDBTimestamp_strategy)
@settings(max_examples=50)
def test_astm_rdbtimestamp_instantiation(instance):
    assert isinstance(instance, astm_RDBTimestamp)

@given(instance=astm_RDBBoolean_strategy)
@settings(max_examples=50)
def test_astm_rdbboolean_instantiation(instance):
    assert isinstance(instance, astm_RDBBoolean)

@given(instance=astm_RDBReal_strategy)
@settings(max_examples=50)
def test_astm_rdbreal_instantiation(instance):
    assert isinstance(instance, astm_RDBReal)

@given(instance=astm_RDBDecimal_strategy)
@settings(max_examples=50)
def test_astm_rdbdecimal_instantiation(instance):
    assert isinstance(instance, astm_RDBDecimal)

@given(instance=astm_RDBFloat_strategy)
@settings(max_examples=50)
def test_astm_rdbfloat_instantiation(instance):
    assert isinstance(instance, astm_RDBFloat)

@given(instance=astm_RDBVarchar_strategy)
@settings(max_examples=50)
def test_astm_rdbvarchar_instantiation(instance):
    assert isinstance(instance, astm_RDBVarchar)

@given(instance=astm_RDBNumber_strategy)
@settings(max_examples=50)
def test_astm_rdbnumber_instantiation(instance):
    assert isinstance(instance, astm_RDBNumber)

@given(instance=astm_RDBInteger_strategy)
@settings(max_examples=50)
def test_astm_rdbinteger_instantiation(instance):
    assert isinstance(instance, astm_RDBInteger)

@given(instance=IdentifierReference_strategy)
@settings(max_examples=50)
def test_identifierreference_instantiation(instance):
    assert isinstance(instance, IdentifierReference)

@given(instance=astm_RDBTableAlias_strategy)
@settings(max_examples=50)
def test_astm_rdbtablealias_instantiation(instance):
    assert isinstance(instance, astm_RDBTableAlias)

@given(instance=astm_RDBRaw_strategy)
@settings(max_examples=50)
def test_astm_rdbraw_instantiation(instance):
    assert isinstance(instance, astm_RDBRaw)

@given(instance=astm_RDBString_strategy)
@settings(max_examples=50)
def test_astm_rdbstring_instantiation(instance):
    assert isinstance(instance, astm_RDBString)

@given(instance=RDBCursorStatement_strategy)
@settings(max_examples=50)
def test_rdbcursorstatement_instantiation(instance):
    assert isinstance(instance, RDBCursorStatement)

@given(instance=astm_RDBFetchCursorStatement_strategy)
@settings(max_examples=50)
def test_astm_rdbfetchcursorstatement_instantiation(instance):
    assert isinstance(instance, astm_RDBFetchCursorStatement)

@given(instance=astm_RDBCloseCursorStatement_strategy)
@settings(max_examples=50)
def test_astm_rdbclosecursorstatement_instantiation(instance):
    assert isinstance(instance, astm_RDBCloseCursorStatement)

@given(instance=astm_RDBOpenCursorStatement_strategy)
@settings(max_examples=50)
def test_astm_rdbopencursorstatement_instantiation(instance):
    assert isinstance(instance, astm_RDBOpenCursorStatement)

@given(instance=RDBModifyStatement_strategy)
@settings(max_examples=50)
def test_rdbmodifystatement_instantiation(instance):
    assert isinstance(instance, RDBModifyStatement)

@given(instance=astm_RDBDeleteStatement_strategy)
@settings(max_examples=50)
def test_astm_rdbdeletestatement_instantiation(instance):
    assert isinstance(instance, astm_RDBDeleteStatement)

@given(instance=astm_RDBUpdateStatement_strategy)
@settings(max_examples=50)
def test_astm_rdbupdatestatement_instantiation(instance):
    assert isinstance(instance, astm_RDBUpdateStatement)

@given(instance=astm_RDBTableReference_strategy)
@settings(max_examples=50)
def test_astm_rdbtablereference_instantiation(instance):
    assert isinstance(instance, astm_RDBTableReference)

@given(instance=RDBConstraint_strategy)
@settings(max_examples=50)
def test_rdbconstraint_instantiation(instance):
    assert isinstance(instance, RDBConstraint)

@given(instance=astm_RDBUniqueKey_strategy)
@settings(max_examples=50)
def test_astm_rdbuniquekey_instantiation(instance):
    assert isinstance(instance, astm_RDBUniqueKey)

@given(instance=astm_RDBRefIntegrity_strategy)
@settings(max_examples=50)
def test_astm_rdbrefintegrity_instantiation(instance):
    assert isinstance(instance, astm_RDBRefIntegrity)

@given(instance=astm_RDBCheckConstraint_strategy)
@settings(max_examples=50)
def test_astm_rdbcheckconstraint_instantiation(instance):
    assert isinstance(instance, astm_RDBCheckConstraint)



@given(instance=astm_RDBCheckConstraint_strategy)
def test_astm_rdbcheckconstraint_RDBConstraintText_setter(instance):
    original = instance.RDBConstraintText
    instance.RDBConstraintText = original
    assert instance.RDBConstraintText == original



@given(instance=astm_RDBCheckConstraint_strategy)
def test_astm_rdbcheckconstraint_RDBConstraintType_setter(instance):
    original = instance.RDBConstraintType
    instance.RDBConstraintType = original
    assert instance.RDBConstraintType == original

@given(instance=astm_RDBColumnReference_strategy)
@settings(max_examples=50)
def test_astm_rdbcolumnreference_instantiation(instance):
    assert isinstance(instance, astm_RDBColumnReference)

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

@given(instance=UnaryOperator_strategy)
@settings(max_examples=50)
def test_unaryoperator_instantiation(instance):
    assert isinstance(instance, UnaryOperator)

@given(instance=astm_Decrement_strategy)
@settings(max_examples=50)
def test_astm_decrement_instantiation(instance):
    assert isinstance(instance, astm_Decrement)

@given(instance=astm_Increment_strategy)
@settings(max_examples=50)
def test_astm_increment_instantiation(instance):
    assert isinstance(instance, astm_Increment)

@given(instance=astm_Deref_strategy)
@settings(max_examples=50)
def test_astm_deref_instantiation(instance):
    assert isinstance(instance, astm_Deref)

@given(instance=astm_PostDecrement_strategy)
@settings(max_examples=50)
def test_astm_postdecrement_instantiation(instance):
    assert isinstance(instance, astm_PostDecrement)

@given(instance=astm_Not_strategy)
@settings(max_examples=50)
def test_astm_not_instantiation(instance):
    assert isinstance(instance, astm_Not)

@given(instance=astm_PostIncrement_strategy)
@settings(max_examples=50)
def test_astm_postincrement_instantiation(instance):
    assert isinstance(instance, astm_PostIncrement)

@given(instance=astm_AddressOf_strategy)
@settings(max_examples=50)
def test_astm_addressof_instantiation(instance):
    assert isinstance(instance, astm_AddressOf)

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

@given(instance=astm_CharLiteral_strategy)
@settings(max_examples=50)
def test_astm_charliteral_instantiation(instance):
    assert isinstance(instance, astm_CharLiteral)

@given(instance=astm_BitLiteral_strategy)
@settings(max_examples=50)
def test_astm_bitliteral_instantiation(instance):
    assert isinstance(instance, astm_BitLiteral)

@given(instance=astm_BooleanLiteral_strategy)
@settings(max_examples=50)
def test_astm_booleanliteral_instantiation(instance):
    assert isinstance(instance, astm_BooleanLiteral)

@given(instance=astm_StringLiteral_strategy)
@settings(max_examples=50)
def test_astm_stringliteral_instantiation(instance):
    assert isinstance(instance, astm_StringLiteral)

@given(instance=astm_IntegerlLiteral_strategy)
@settings(max_examples=50)
def test_astm_integerlliteral_instantiation(instance):
    assert isinstance(instance, astm_IntegerlLiteral)

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

@given(instance=astm_Protected_strategy)
@settings(max_examples=50)
def test_astm_protected_instantiation(instance):
    assert isinstance(instance, astm_Protected)

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

@given(instance=astm_String_strategy)
@settings(max_examples=50)
def test_astm_string_instantiation(instance):
    assert isinstance(instance, astm_String)

@given(instance=astm_ShortInteger_strategy)
@settings(max_examples=50)
def test_astm_shortinteger_instantiation(instance):
    assert isinstance(instance, astm_ShortInteger)

@given(instance=astm_LongInteger_strategy)
@settings(max_examples=50)
def test_astm_longinteger_instantiation(instance):
    assert isinstance(instance, astm_LongInteger)

@given(instance=astm_Boolean_strategy)
@settings(max_examples=50)
def test_astm_boolean_instantiation(instance):
    assert isinstance(instance, astm_Boolean)

@given(instance=astm_WideCharacter_strategy)
@settings(max_examples=50)
def test_astm_widecharacter_instantiation(instance):
    assert isinstance(instance, astm_WideCharacter)

@given(instance=astm_Character_strategy)
@settings(max_examples=50)
def test_astm_character_instantiation(instance):
    assert isinstance(instance, astm_Character)

@given(instance=astm_LongDouble_strategy)
@settings(max_examples=50)
def test_astm_longdouble_instantiation(instance):
    assert isinstance(instance, astm_LongDouble)

@given(instance=astm_Byte_strategy)
@settings(max_examples=50)
def test_astm_byte_instantiation(instance):
    assert isinstance(instance, astm_Byte)

@given(instance=astm_Double_strategy)
@settings(max_examples=50)
def test_astm_double_instantiation(instance):
    assert isinstance(instance, astm_Double)

@given(instance=astm_Void_strategy)
@settings(max_examples=50)
def test_astm_void_instantiation(instance):
    assert isinstance(instance, astm_Void)

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

@given(instance=astm_FileLocal_strategy)
@settings(max_examples=50)
def test_astm_filelocal_instantiation(instance):
    assert isinstance(instance, astm_FileLocal)

@given(instance=astm_NoDef_strategy)
@settings(max_examples=50)
def test_astm_nodef_instantiation(instance):
    assert isinstance(instance, astm_NoDef)

@given(instance=astm_FunctionPersistent_strategy)
@settings(max_examples=50)
def test_astm_functionpersistent_instantiation(instance):
    assert isinstance(instance, astm_FunctionPersistent)

@given(instance=astm_PerClassMember_strategy)
@settings(max_examples=50)
def test_astm_perclassmember_instantiation(instance):
    assert isinstance(instance, astm_PerClassMember)

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

@given(instance=astm_NotEqual_strategy)
@settings(max_examples=50)
def test_astm_notequal_instantiation(instance):
    assert isinstance(instance, astm_NotEqual)

@given(instance=astm_BitXor_strategy)
@settings(max_examples=50)
def test_astm_bitxor_instantiation(instance):
    assert isinstance(instance, astm_BitXor)

@given(instance=astm_SpecificIn_strategy)
@settings(max_examples=50)
def test_astm_specificin_instantiation(instance):
    assert isinstance(instance, astm_SpecificIn)

@given(instance=astm_SpecificLessEqual_strategy)
@settings(max_examples=50)
def test_astm_specificlessequal_instantiation(instance):
    assert isinstance(instance, astm_SpecificLessEqual)

@given(instance=astm_Multiply_strategy)
@settings(max_examples=50)
def test_astm_multiply_instantiation(instance):
    assert isinstance(instance, astm_Multiply)

@given(instance=astm_BitRightShift_strategy)
@settings(max_examples=50)
def test_astm_bitrightshift_instantiation(instance):
    assert isinstance(instance, astm_BitRightShift)

@given(instance=astm_Less_strategy)
@settings(max_examples=50)
def test_astm_less_instantiation(instance):
    assert isinstance(instance, astm_Less)

@given(instance=astm_Or_strategy)
@settings(max_examples=50)
def test_astm_or_instantiation(instance):
    assert isinstance(instance, astm_Or)

@given(instance=astm_SpecificLike_strategy)
@settings(max_examples=50)
def test_astm_specificlike_instantiation(instance):
    assert isinstance(instance, astm_SpecificLike)

@given(instance=astm_Exponent_strategy)
@settings(max_examples=50)
def test_astm_exponent_instantiation(instance):
    assert isinstance(instance, astm_Exponent)

@given(instance=astm_Modulus_strategy)
@settings(max_examples=50)
def test_astm_modulus_instantiation(instance):
    assert isinstance(instance, astm_Modulus)

@given(instance=astm_Equal_strategy)
@settings(max_examples=50)
def test_astm_equal_instantiation(instance):
    assert isinstance(instance, astm_Equal)

@given(instance=astm_SpecificGreaterEqual_strategy)
@settings(max_examples=50)
def test_astm_specificgreaterequal_instantiation(instance):
    assert isinstance(instance, astm_SpecificGreaterEqual)

@given(instance=astm_SpecificConcatString_strategy)
@settings(max_examples=50)
def test_astm_specificconcatstring_instantiation(instance):
    assert isinstance(instance, astm_SpecificConcatString)

@given(instance=astm_BitOr_strategy)
@settings(max_examples=50)
def test_astm_bitor_instantiation(instance):
    assert isinstance(instance, astm_BitOr)

@given(instance=astm_And_strategy)
@settings(max_examples=50)
def test_astm_and_instantiation(instance):
    assert isinstance(instance, astm_And)

@given(instance=astm_Divide_strategy)
@settings(max_examples=50)
def test_astm_divide_instantiation(instance):
    assert isinstance(instance, astm_Divide)

@given(instance=astm_BitLeftShift_strategy)
@settings(max_examples=50)
def test_astm_bitleftshift_instantiation(instance):
    assert isinstance(instance, astm_BitLeftShift)

@given(instance=astm_Add_strategy)
@settings(max_examples=50)
def test_astm_add_instantiation(instance):
    assert isinstance(instance, astm_Add)

@given(instance=astm_Greater_strategy)
@settings(max_examples=50)
def test_astm_greater_instantiation(instance):
    assert isinstance(instance, astm_Greater)

@given(instance=astm_Subtract_strategy)
@settings(max_examples=50)
def test_astm_subtract_instantiation(instance):
    assert isinstance(instance, astm_Subtract)

@given(instance=astm_NotGreater_strategy)
@settings(max_examples=50)
def test_astm_notgreater_instantiation(instance):
    assert isinstance(instance, astm_NotGreater)

@given(instance=astm_Assign_strategy)
@settings(max_examples=50)
def test_astm_assign_instantiation(instance):
    assert isinstance(instance, astm_Assign)

@given(instance=astm_NotLess_strategy)
@settings(max_examples=50)
def test_astm_notless_instantiation(instance):
    assert isinstance(instance, astm_NotLess)

@given(instance=astm_BitAnd_strategy)
@settings(max_examples=50)
def test_astm_bitand_instantiation(instance):
    assert isinstance(instance, astm_BitAnd)

@given(instance=astm_OperatorAssign_strategy)
@settings(max_examples=50)
def test_astm_operatorassign_instantiation(instance):
    assert isinstance(instance, astm_OperatorAssign)

@given(instance=TypeReference_strategy)
@settings(max_examples=50)
def test_typereference_instantiation(instance):
    assert isinstance(instance, TypeReference)

@given(instance=astm_NamedTypeReference_strategy)
@settings(max_examples=50)
def test_astm_namedtypereference_instantiation(instance):
    assert isinstance(instance, astm_NamedTypeReference)

@given(instance=astm_UnnamedTypeReference_strategy)
@settings(max_examples=50)
def test_astm_unnamedtypereference_instantiation(instance):
    assert isinstance(instance, astm_UnnamedTypeReference)

@given(instance=AggregateType_strategy)
@settings(max_examples=50)
def test_aggregatetype_instantiation(instance):
    assert isinstance(instance, AggregateType)

@given(instance=astm_UnionType_strategy)
@settings(max_examples=50)
def test_astm_uniontype_instantiation(instance):
    assert isinstance(instance, astm_UnionType)

@given(instance=astm_AnnotationType_strategy)
@settings(max_examples=50)
def test_astm_annotationtype_instantiation(instance):
    assert isinstance(instance, astm_AnnotationType)

@given(instance=astm_StructureType_strategy)
@settings(max_examples=50)
def test_astm_structuretype_instantiation(instance):
    assert isinstance(instance, astm_StructureType)

@given(instance=astm_ClassType_strategy)
@settings(max_examples=50)
def test_astm_classtype_instantiation(instance):
    assert isinstance(instance, astm_ClassType)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=astm_FunctionType_strategy)
@settings(max_examples=50)
def test_astm_functiontype_instantiation(instance):
    assert isinstance(instance, astm_FunctionType)

@given(instance=ConstructedType_strategy)
@settings(max_examples=50)
def test_constructedtype_instantiation(instance):
    assert isinstance(instance, ConstructedType)

@given(instance=astm_PointerType_strategy)
@settings(max_examples=50)
def test_astm_pointertype_instantiation(instance):
    assert isinstance(instance, astm_PointerType)

@given(instance=astm_ReferenceType_strategy)
@settings(max_examples=50)
def test_astm_referencetype_instantiation(instance):
    assert isinstance(instance, astm_ReferenceType)

@given(instance=astm_CollectionType_strategy)
@settings(max_examples=50)
def test_astm_collectiontype_instantiation(instance):
    assert isinstance(instance, astm_CollectionType)

@given(instance=astm_RangeType_strategy)
@settings(max_examples=50)
def test_astm_rangetype_instantiation(instance):
    assert isinstance(instance, astm_RangeType)

@given(instance=astm_ArrayType_strategy)
@settings(max_examples=50)
def test_astm_arraytype_instantiation(instance):
    assert isinstance(instance, astm_ArrayType)

@given(instance=astm_AggregateScope_strategy)
@settings(max_examples=50)
def test_astm_aggregatescope_instantiation(instance):
    assert isinstance(instance, astm_AggregateScope)

@given(instance=DataType_strategy)
@settings(max_examples=50)
def test_datatype_instantiation(instance):
    assert isinstance(instance, DataType)

@given(instance=astm_EnumType_strategy)
@settings(max_examples=50)
def test_astm_enumtype_instantiation(instance):
    assert isinstance(instance, astm_EnumType)

@given(instance=astm_RDBDataBaseType_strategy)
@settings(max_examples=50)
def test_astm_rdbdatabasetype_instantiation(instance):
    assert isinstance(instance, astm_RDBDataBaseType)

@given(instance=astm_RDBCursorType_strategy)
@settings(max_examples=50)
def test_astm_rdbcursortype_instantiation(instance):
    assert isinstance(instance, astm_RDBCursorType)

@given(instance=astm_RDBTableType_strategy)
@settings(max_examples=50)
def test_astm_rdbtabletype_instantiation(instance):
    assert isinstance(instance, astm_RDBTableType)

@given(instance=astm_ExceptionType_strategy)
@settings(max_examples=50)
def test_astm_exceptiontype_instantiation(instance):
    assert isinstance(instance, astm_ExceptionType)

@given(instance=astm_RDBUserType_strategy)
@settings(max_examples=50)
def test_astm_rdbusertype_instantiation(instance):
    assert isinstance(instance, astm_RDBUserType)

@given(instance=astm_RDBColumnType_strategy)
@settings(max_examples=50)
def test_astm_rdbcolumntype_instantiation(instance):
    assert isinstance(instance, astm_RDBColumnType)

@given(instance=astm_FormalParameterType_strategy)
@settings(max_examples=50)
def test_astm_formalparametertype_instantiation(instance):
    assert isinstance(instance, astm_FormalParameterType)

@given(instance=astm_ConstructedType_strategy)
@settings(max_examples=50)
def test_astm_constructedtype_instantiation(instance):
    assert isinstance(instance, astm_ConstructedType)

@given(instance=astm_RDBTableSpaceType_strategy)
@settings(max_examples=50)
def test_astm_rdbtablespacetype_instantiation(instance):
    assert isinstance(instance, astm_RDBTableSpaceType)

@given(instance=astm_RDBViewType_strategy)
@settings(max_examples=50)
def test_astm_rdbviewtype_instantiation(instance):
    assert isinstance(instance, astm_RDBViewType)

@given(instance=astm_PrimitiveType_strategy)
@settings(max_examples=50)
def test_astm_primitivetype_instantiation(instance):
    assert isinstance(instance, astm_PrimitiveType)



@given(instance=astm_PrimitiveType_strategy)
def test_astm_primitivetype_isSigned_setter(instance):
    original = instance.isSigned
    instance.isSigned = original
    assert instance.isSigned == original

@given(instance=GASTMSyntaxObject_strategy)
@settings(max_examples=50)
def test_gastmsyntaxobject_instantiation(instance):
    assert isinstance(instance, GASTMSyntaxObject)

@given(instance=astm_Type_strategy)
@settings(max_examples=50)
def test_astm_type_instantiation(instance):
    assert isinstance(instance, astm_Type)



@given(instance=astm_Type_strategy)
def test_astm_type_isVolatile_setter(instance):
    original = instance.isVolatile
    instance.isVolatile = original
    assert instance.isVolatile == original



@given(instance=astm_Type_strategy)
def test_astm_type_isConst_setter(instance):
    original = instance.isConst
    instance.isConst = original
    assert instance.isConst == original

@given(instance=PreprocessorElement_strategy)
@settings(max_examples=50)
def test_preprocessorelement_instantiation(instance):
    assert isinstance(instance, PreprocessorElement)

@given(instance=astm_MacroDefinition_strategy)
@settings(max_examples=50)
def test_astm_macrodefinition_instantiation(instance):
    assert isinstance(instance, astm_MacroDefinition)



@given(instance=astm_MacroDefinition_strategy)
def test_astm_macrodefinition_macroName_setter(instance):
    original = instance.macroName
    instance.macroName = original
    assert instance.macroName == original



@given(instance=astm_MacroDefinition_strategy)
def test_astm_macrodefinition_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=astm_MacroCall_strategy)
@settings(max_examples=50)
def test_astm_macrocall_instantiation(instance):
    assert isinstance(instance, astm_MacroCall)

@given(instance=astm_Comment_strategy)
@settings(max_examples=50)
def test_astm_comment_instantiation(instance):
    assert isinstance(instance, astm_Comment)



@given(instance=astm_Comment_strategy)
def test_astm_comment_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=astm_IncludeUnit_strategy)
@settings(max_examples=50)
def test_astm_includeunit_instantiation(instance):
    assert isinstance(instance, astm_IncludeUnit)

@given(instance=astm_LabelType_strategy)
@settings(max_examples=50)
def test_astm_labeltype_instantiation(instance):
    assert isinstance(instance, astm_LabelType)

@given(instance=astm_NameSpaceType_strategy)
@settings(max_examples=50)
def test_astm_namespacetype_instantiation(instance):
    assert isinstance(instance, astm_NameSpaceType)

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

@given(instance=DataDefinition_strategy)
@settings(max_examples=50)
def test_datadefinition_instantiation(instance):
    assert isinstance(instance, DataDefinition)

@given(instance=astm_VariableDefinition_strategy)
@settings(max_examples=50)
def test_astm_variabledefinition_instantiation(instance):
    assert isinstance(instance, astm_VariableDefinition)

@given(instance=astm_BitFieldDefinition_strategy)
@settings(max_examples=50)
def test_astm_bitfielddefinition_instantiation(instance):
    assert isinstance(instance, astm_BitFieldDefinition)

@given(instance=astm_Expression_strategy)
@settings(max_examples=50)
def test_astm_expression_instantiation(instance):
    assert isinstance(instance, astm_Expression)

@given(instance=astm_TypeReference_strategy)
@settings(max_examples=50)
def test_astm_typereference_instantiation(instance):
    assert isinstance(instance, astm_TypeReference)

@given(instance=astm_FunctionScope_strategy)
@settings(max_examples=50)
def test_astm_functionscope_instantiation(instance):
    assert isinstance(instance, astm_FunctionScope)

@given(instance=astm_Statement_strategy)
@settings(max_examples=50)
def test_astm_statement_instantiation(instance):
    assert isinstance(instance, astm_Statement)

@given(instance=astm_FormalParameterDefinition_strategy)
@settings(max_examples=50)
def test_astm_formalparameterdefinition_instantiation(instance):
    assert isinstance(instance, astm_FormalParameterDefinition)

@given(instance=Definition_strategy)
@settings(max_examples=50)
def test_definition_instantiation(instance):
    assert isinstance(instance, Definition)

@given(instance=astm_RDBUserDefinition_strategy)
@settings(max_examples=50)
def test_astm_rdbuserdefinition_instantiation(instance):
    assert isinstance(instance, astm_RDBUserDefinition)

@given(instance=astm_DataDefinition_strategy)
@settings(max_examples=50)
def test_astm_datadefinition_instantiation(instance):
    assert isinstance(instance, astm_DataDefinition)



@given(instance=astm_DataDefinition_strategy)
def test_astm_datadefinition_isMutable_setter(instance):
    original = instance.isMutable
    instance.isMutable = original
    assert instance.isMutable == original

@given(instance=astm_RDBTableDefinition_strategy)
@settings(max_examples=50)
def test_astm_rdbtabledefinition_instantiation(instance):
    assert isinstance(instance, astm_RDBTableDefinition)

@given(instance=astm_EntryDefinition_strategy)
@settings(max_examples=50)
def test_astm_entrydefinition_instantiation(instance):
    assert isinstance(instance, astm_EntryDefinition)

@given(instance=astm_RDBCursorDefinition_strategy)
@settings(max_examples=50)
def test_astm_rdbcursordefinition_instantiation(instance):
    assert isinstance(instance, astm_RDBCursorDefinition)

@given(instance=astm_RDBColumnDefinition_strategy)
@settings(max_examples=50)
def test_astm_rdbcolumndefinition_instantiation(instance):
    assert isinstance(instance, astm_RDBColumnDefinition)



@given(instance=astm_RDBColumnDefinition_strategy)
def test_astm_rdbcolumndefinition_NotNull_setter(instance):
    original = instance.NotNull
    instance.NotNull = original
    assert instance.NotNull == original

@given(instance=astm_SpecificTriggerDefinition_strategy)
@settings(max_examples=50)
def test_astm_specifictriggerdefinition_instantiation(instance):
    assert isinstance(instance, astm_SpecificTriggerDefinition)

@given(instance=astm_EnumLiteralDefinition_strategy)
@settings(max_examples=50)
def test_astm_enumliteraldefinition_instantiation(instance):
    assert isinstance(instance, astm_EnumLiteralDefinition)

@given(instance=astm_RDBViewDefinition_strategy)
@settings(max_examples=50)
def test_astm_rdbviewdefinition_instantiation(instance):
    assert isinstance(instance, astm_RDBViewDefinition)

@given(instance=astm_RDBTableSpaceDefinition_strategy)
@settings(max_examples=50)
def test_astm_rdbtablespacedefinition_instantiation(instance):
    assert isinstance(instance, astm_RDBTableSpaceDefinition)

@given(instance=astm_RDBDatabaseDefinition_strategy)
@settings(max_examples=50)
def test_astm_rdbdatabasedefinition_instantiation(instance):
    assert isinstance(instance, astm_RDBDatabaseDefinition)

@given(instance=astm_FunctionDefinition_strategy)
@settings(max_examples=50)
def test_astm_functiondefinition_instantiation(instance):
    assert isinstance(instance, astm_FunctionDefinition)

@given(instance=Declaration_strategy)
@settings(max_examples=50)
def test_declaration_instantiation(instance):
    assert isinstance(instance, Declaration)

@given(instance=astm_VariableDeclaration_strategy)
@settings(max_examples=50)
def test_astm_variabledeclaration_instantiation(instance):
    assert isinstance(instance, astm_VariableDeclaration)



@given(instance=astm_VariableDeclaration_strategy)
def test_astm_variabledeclaration_isMutable_setter(instance):
    original = instance.isMutable
    instance.isMutable = original
    assert instance.isMutable == original

@given(instance=astm_FormalParameterDeclaration_strategy)
@settings(max_examples=50)
def test_astm_formalparameterdeclaration_instantiation(instance):
    assert isinstance(instance, astm_FormalParameterDeclaration)

@given(instance=astm_FunctionDeclaration_strategy)
@settings(max_examples=50)
def test_astm_functiondeclaration_instantiation(instance):
    assert isinstance(instance, astm_FunctionDeclaration)

@given(instance=GASTMSemanticObject_strategy)
@settings(max_examples=50)
def test_gastmsemanticobject_instantiation(instance):
    assert isinstance(instance, GASTMSemanticObject)

@given(instance=astm_Project_strategy)
@settings(max_examples=50)
def test_astm_project_instantiation(instance):
    assert isinstance(instance, astm_Project)

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

@given(instance=DefinitionObject_strategy)
@settings(max_examples=50)
def test_definitionobject_instantiation(instance):
    assert isinstance(instance, DefinitionObject)

@given(instance=astm_TypeDefinition_strategy)
@settings(max_examples=50)
def test_astm_typedefinition_instantiation(instance):
    assert isinstance(instance, astm_TypeDefinition)

@given(instance=astm_LabelDefinition_strategy)
@settings(max_examples=50)
def test_astm_labeldefinition_instantiation(instance):
    assert isinstance(instance, astm_LabelDefinition)

@given(instance=astm_NameSpaceDefinition_strategy)
@settings(max_examples=50)
def test_astm_namespacedefinition_instantiation(instance):
    assert isinstance(instance, astm_NameSpaceDefinition)

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

@given(instance=astm_VirtualSpecification_strategy)
@settings(max_examples=50)
def test_astm_virtualspecification_instantiation(instance):
    assert isinstance(instance, astm_VirtualSpecification)

@given(instance=astm_DerivesFrom_strategy)
@settings(max_examples=50)
def test_astm_derivesfrom_instantiation(instance):
    assert isinstance(instance, astm_DerivesFrom)



@given(instance=astm_DerivesFrom_strategy)
def test_astm_derivesfrom_isVirtual_setter(instance):
    original = instance.isVirtual
    instance.isVirtual = original
    assert instance.isVirtual == original

@given(instance=astm_Dimension_strategy)
@settings(max_examples=50)
def test_astm_dimension_instantiation(instance):
    assert isinstance(instance, astm_Dimension)

@given(instance=astm_RDBTrigger_strategy)
@settings(max_examples=50)
def test_astm_rdbtrigger_instantiation(instance):
    assert isinstance(instance, astm_RDBTrigger)

@given(instance=astm_RDBIndexColumn_strategy)
@settings(max_examples=50)
def test_astm_rdbindexcolumn_instantiation(instance):
    assert isinstance(instance, astm_RDBIndexColumn)



@given(instance=astm_RDBIndexColumn_strategy)
def test_astm_rdbindexcolumn_AscendingOrDescending_setter(instance):
    original = instance.AscendingOrDescending
    instance.AscendingOrDescending = original
    assert instance.AscendingOrDescending == original

@given(instance=astm_FunctionMemberAttribute_strategy)
@settings(max_examples=50)
def test_astm_functionmemberattribute_instantiation(instance):
    assert isinstance(instance, astm_FunctionMemberAttribute)

@given(instance=astm_RDBIndex_strategy)
@settings(max_examples=50)
def test_astm_rdbindex_instantiation(instance):
    assert isinstance(instance, astm_RDBIndex)



@given(instance=astm_RDBIndex_strategy)
def test_astm_rdbindex_IsUnique_setter(instance):
    original = instance.IsUnique
    instance.IsUnique = original
    assert instance.IsUnique == original



@given(instance=astm_RDBIndex_strategy)
def test_astm_rdbindex_NotNull_setter(instance):
    original = instance.NotNull
    instance.NotNull = original
    assert instance.NotNull == original

@given(instance=astm_RDBConstraint_strategy)
@settings(max_examples=50)
def test_astm_rdbconstraint_instantiation(instance):
    assert isinstance(instance, astm_RDBConstraint)

@given(instance=astm_Name_strategy)
@settings(max_examples=50)
def test_astm_name_instantiation(instance):
    assert isinstance(instance, astm_Name)



@given(instance=astm_Name_strategy)
def test_astm_name_nameString_setter(instance):
    original = instance.nameString
    instance.nameString = original
    assert instance.nameString == original

@given(instance=astm_PreprocessorElement_strategy)
@settings(max_examples=50)
def test_astm_preprocessorelement_instantiation(instance):
    assert isinstance(instance, astm_PreprocessorElement)

@given(instance=GASTMObject_strategy)
@settings(max_examples=50)
def test_gastmobject_instantiation(instance):
    assert isinstance(instance, GASTMObject)

@given(instance=astm_GASTMSyntaxObject_strategy)
@settings(max_examples=50)
def test_astm_gastmsyntaxobject_instantiation(instance):
    assert isinstance(instance, astm_GASTMSyntaxObject)

@given(instance=astm_DefinitionObject_strategy)
@settings(max_examples=50)
def test_astm_definitionobject_instantiation(instance):
    assert isinstance(instance, astm_DefinitionObject)

@given(instance=astm_Scope_strategy)
@settings(max_examples=50)
def test_astm_scope_instantiation(instance):
    assert isinstance(instance, astm_Scope)

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

@given(instance=GASTMSourceObject_strategy)
@settings(max_examples=50)
def test_gastmsourceobject_instantiation(instance):
    assert isinstance(instance, GASTMSourceObject)

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

@given(instance=astm_SourceFile_strategy)
@settings(max_examples=50)
def test_astm_sourcefile_instantiation(instance):
    assert isinstance(instance, astm_SourceFile)



@given(instance=astm_SourceFile_strategy)
def test_astm_sourcefile_pathName_setter(instance):
    original = instance.pathName
    instance.pathName = original
    assert instance.pathName == original

@given(instance=Visitable_strategy)
@settings(max_examples=50)
def test_visitable_instantiation(instance):
    assert isinstance(instance, Visitable)

@given(instance=astm_RDBHostVariableReference_strategy)
@settings(max_examples=50)
def test_astm_rdbhostvariablereference_instantiation(instance):
    assert isinstance(instance, astm_RDBHostVariableReference)

@given(instance=astm_AccessKind_strategy)
@settings(max_examples=50)
def test_astm_accesskind_instantiation(instance):
    assert isinstance(instance, astm_AccessKind)

@given(instance=astm_DataType_strategy)
@settings(max_examples=50)
def test_astm_datatype_instantiation(instance):
    assert isinstance(instance, astm_DataType)

@given(instance=astm_StorageSpecification_strategy)
@settings(max_examples=50)
def test_astm_storagespecification_instantiation(instance):
    assert isinstance(instance, astm_StorageSpecification)

@given(instance=astm_GASTMSourceObject_strategy)
@settings(max_examples=50)
def test_astm_gastmsourceobject_instantiation(instance):
    assert isinstance(instance, astm_GASTMSourceObject)

@given(instance=astm_OtherSyntaxObject_strategy)
@settings(max_examples=50)
def test_astm_othersyntaxobject_instantiation(instance):
    assert isinstance(instance, astm_OtherSyntaxObject)

@given(instance=astm_RDBTableSpaceReference_strategy)
@settings(max_examples=50)
def test_astm_rdbtablespacereference_instantiation(instance):
    assert isinstance(instance, astm_RDBTableSpaceReference)

@given(instance=astm_FunctionMemberAttributes_strategy)
@settings(max_examples=50)
def test_astm_functionmemberattributes_instantiation(instance):
    assert isinstance(instance, astm_FunctionMemberAttributes)



@given(instance=astm_FunctionMemberAttributes_strategy)
def test_astm_functionmemberattributes_isThisConst_setter(instance):
    original = instance.isThisConst
    instance.isThisConst = original
    assert instance.isThisConst == original



@given(instance=astm_FunctionMemberAttributes_strategy)
def test_astm_functionmemberattributes_isFriend_setter(instance):
    original = instance.isFriend
    instance.isFriend = original
    assert instance.isFriend == original



@given(instance=astm_FunctionMemberAttributes_strategy)
def test_astm_functionmemberattributes_isInline_setter(instance):
    original = instance.isInline
    instance.isInline = original
    assert instance.isInline == original

@given(instance=astm_ActualParameter_strategy)
@settings(max_examples=50)
def test_astm_actualparameter_instantiation(instance):
    assert isinstance(instance, astm_ActualParameter)

@given(instance=astm_BinaryOperator_strategy)
@settings(max_examples=50)
def test_astm_binaryoperator_instantiation(instance):
    assert isinstance(instance, astm_BinaryOperator)

@given(instance=astm_GASTMSemanticObject_strategy)
@settings(max_examples=50)
def test_astm_gastmsemanticobject_instantiation(instance):
    assert isinstance(instance, astm_GASTMSemanticObject)

@given(instance=astm_UnaryOperator_strategy)
@settings(max_examples=50)
def test_astm_unaryoperator_instantiation(instance):
    assert isinstance(instance, astm_UnaryOperator)

@given(instance=astm_GASTMObject_strategy)
@settings(max_examples=50)
def test_astm_gastmobject_instantiation(instance):
    assert isinstance(instance, astm_GASTMObject)

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

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=astm_ConditionalExpression_strategy)
@settings(max_examples=50)
def test_astm_conditionalexpression_instantiation(instance):
    assert isinstance(instance, astm_ConditionalExpression)

@given(instance=astm_NewExpression_strategy)
@settings(max_examples=50)
def test_astm_newexpression_instantiation(instance):
    assert isinstance(instance, astm_NewExpression)

@given(instance=astm_AggregateExpression_strategy)
@settings(max_examples=50)
def test_astm_aggregateexpression_instantiation(instance):
    assert isinstance(instance, astm_AggregateExpression)

@given(instance=astm_RDBSelectExpression_strategy)
@settings(max_examples=50)
def test_astm_rdbselectexpression_instantiation(instance):
    assert isinstance(instance, astm_RDBSelectExpression)

@given(instance=astm_FunctionCallExpression_strategy)
@settings(max_examples=50)
def test_astm_functioncallexpression_instantiation(instance):
    assert isinstance(instance, astm_FunctionCallExpression)

@given(instance=astm_RangeExpression_strategy)
@settings(max_examples=50)
def test_astm_rangeexpression_instantiation(instance):
    assert isinstance(instance, astm_RangeExpression)

@given(instance=astm_CastExpression_strategy)
@settings(max_examples=50)
def test_astm_castexpression_instantiation(instance):
    assert isinstance(instance, astm_CastExpression)

@given(instance=astm_Literal_strategy)
@settings(max_examples=50)
def test_astm_literal_instantiation(instance):
    assert isinstance(instance, astm_Literal)



@given(instance=astm_Literal_strategy)
def test_astm_literal_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=astm_RDBHostVariableExpression_strategy)
@settings(max_examples=50)
def test_astm_rdbhostvariableexpression_instantiation(instance):
    assert isinstance(instance, astm_RDBHostVariableExpression)

@given(instance=astm_ArrayAccess_strategy)
@settings(max_examples=50)
def test_astm_arrayaccess_instantiation(instance):
    assert isinstance(instance, astm_ArrayAccess)

@given(instance=astm_AnnotationExpression_strategy)
@settings(max_examples=50)
def test_astm_annotationexpression_instantiation(instance):
    assert isinstance(instance, astm_AnnotationExpression)

@given(instance=astm_BinaryExpression_strategy)
@settings(max_examples=50)
def test_astm_binaryexpression_instantiation(instance):
    assert isinstance(instance, astm_BinaryExpression)

@given(instance=astm_UnaryExpression_strategy)
@settings(max_examples=50)
def test_astm_unaryexpression_instantiation(instance):
    assert isinstance(instance, astm_UnaryExpression)

@given(instance=astm_NameReference_strategy)
@settings(max_examples=50)
def test_astm_namereference_instantiation(instance):
    assert isinstance(instance, astm_NameReference)

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

@given(instance=astm_CatchBlock_strategy)
@settings(max_examples=50)
def test_astm_catchblock_instantiation(instance):
    assert isinstance(instance, astm_CatchBlock)

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

@given(instance=astm_LabelAccess_strategy)
@settings(max_examples=50)
def test_astm_labelaccess_instantiation(instance):
    assert isinstance(instance, astm_LabelAccess)

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

@given(instance=astm_SwitchCase_strategy)
@settings(max_examples=50)
def test_astm_switchcase_instantiation(instance):
    assert isinstance(instance, astm_SwitchCase)

@given(instance=astm_BlockScope_strategy)
@settings(max_examples=50)
def test_astm_blockscope_instantiation(instance):
    assert isinstance(instance, astm_BlockScope)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=astm_ReturnStatement_strategy)
@settings(max_examples=50)
def test_astm_returnstatement_instantiation(instance):
    assert isinstance(instance, astm_ReturnStatement)

@given(instance=astm_EmptyStatement_strategy)
@settings(max_examples=50)
def test_astm_emptystatement_instantiation(instance):
    assert isinstance(instance, astm_EmptyStatement)

@given(instance=astm_RDBInsertStatement_strategy)
@settings(max_examples=50)
def test_astm_rdbinsertstatement_instantiation(instance):
    assert isinstance(instance, astm_RDBInsertStatement)

@given(instance=astm_SwitchStatement_strategy)
@settings(max_examples=50)
def test_astm_switchstatement_instantiation(instance):
    assert isinstance(instance, astm_SwitchStatement)

@given(instance=astm_DeleteStatement_strategy)
@settings(max_examples=50)
def test_astm_deletestatement_instantiation(instance):
    assert isinstance(instance, astm_DeleteStatement)

@given(instance=astm_ExpressionStatement_strategy)
@settings(max_examples=50)
def test_astm_expressionstatement_instantiation(instance):
    assert isinstance(instance, astm_ExpressionStatement)

@given(instance=astm_LoopStatement_strategy)
@settings(max_examples=50)
def test_astm_loopstatement_instantiation(instance):
    assert isinstance(instance, astm_LoopStatement)

@given(instance=astm_LabeledStatement_strategy)
@settings(max_examples=50)
def test_astm_labeledstatement_instantiation(instance):
    assert isinstance(instance, astm_LabeledStatement)

@given(instance=astm_BreakStatement_strategy)
@settings(max_examples=50)
def test_astm_breakstatement_instantiation(instance):
    assert isinstance(instance, astm_BreakStatement)

@given(instance=astm_RDBCursorStatement_strategy)
@settings(max_examples=50)
def test_astm_rdbcursorstatement_instantiation(instance):
    assert isinstance(instance, astm_RDBCursorStatement)

@given(instance=astm_ContinueStatement_strategy)
@settings(max_examples=50)
def test_astm_continuestatement_instantiation(instance):
    assert isinstance(instance, astm_ContinueStatement)

@given(instance=astm_DeclarationOrDefinitionStatement_strategy)
@settings(max_examples=50)
def test_astm_declarationordefinitionstatement_instantiation(instance):
    assert isinstance(instance, astm_DeclarationOrDefinitionStatement)

@given(instance=astm_BlockStatement_strategy)
@settings(max_examples=50)
def test_astm_blockstatement_instantiation(instance):
    assert isinstance(instance, astm_BlockStatement)

@given(instance=astm_RDBSelectStatement_strategy)
@settings(max_examples=50)
def test_astm_rdbselectstatement_instantiation(instance):
    assert isinstance(instance, astm_RDBSelectStatement)

@given(instance=astm_ThrowStatement_strategy)
@settings(max_examples=50)
def test_astm_throwstatement_instantiation(instance):
    assert isinstance(instance, astm_ThrowStatement)

@given(instance=astm_JumpStatement_strategy)
@settings(max_examples=50)
def test_astm_jumpstatement_instantiation(instance):
    assert isinstance(instance, astm_JumpStatement)

@given(instance=astm_RDBModifyStatement_strategy)
@settings(max_examples=50)
def test_astm_rdbmodifystatement_instantiation(instance):
    assert isinstance(instance, astm_RDBModifyStatement)

@given(instance=astm_RDBConnectStatement_strategy)
@settings(max_examples=50)
def test_astm_rdbconnectstatement_instantiation(instance):
    assert isinstance(instance, astm_RDBConnectStatement)

@given(instance=astm_TerminateStatement_strategy)
@settings(max_examples=50)
def test_astm_terminatestatement_instantiation(instance):
    assert isinstance(instance, astm_TerminateStatement)

@given(instance=astm_TryStatement_strategy)
@settings(max_examples=50)
def test_astm_trystatement_instantiation(instance):
    assert isinstance(instance, astm_TryStatement)

@given(instance=astm_IfStatement_strategy)
@settings(max_examples=50)
def test_astm_ifstatement_instantiation(instance):
    assert isinstance(instance, astm_IfStatement)

@given(instance=astm_SpecificSelectStatement_strategy)
@settings(max_examples=50)
def test_astm_specificselectstatement_instantiation(instance):
    assert isinstance(instance, astm_SpecificSelectStatement)
